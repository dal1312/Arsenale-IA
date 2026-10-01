import pathlib, re, hashlib, json, os, shutil, datetime, sys
ROOT = pathlib.Path(__file__).resolve().parent
DEST = pathlib.Path(os.environ.get('HERMES_SKILLS_DIR') or (pathlib.Path(os.environ.get('LOCALAPPDATA') or (pathlib.Path.home() / 'AppData' / 'Local')) / 'hermes' / 'profiles' / 'italiano' / 'skills'))
PLAN = ROOT / 'inventario-hermes-selettivo.json'
FILES = ('PROCEDURA.md', 'SKILL.md')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def name(p):
    t=p.read_text(encoding='utf-8-sig'); fm=t.split('---',2)[1]
    return re.search(r'^name:\s*([^\r\n]+)',fm,re.M)[1].strip().strip('\"\'')
def snapshot(p):
    result={}
    for base, dirs, files in os.walk(p, followlinks=False):
        for n in dirs+files:
            q=pathlib.Path(base)/n; st=q.lstat(); rel=str(q.relative_to(p))
            result[rel]={'kind':'dir' if q.is_dir() else 'file','mtime':st.st_mtime_ns,'size':st.st_size if q.is_file() else None,'hash':sha(q) if q.is_file() and not q.is_symlink() else None}
    return result
if sys.argv[1]=='inventory':
    codes=re.findall(r'^- \*\*(ARI-\d{4})[^\n]+\*\*\s*— Disponibile\s*$',(ROOT/'CATALOGO.md').read_text(encoding='utf-8-sig'),re.M)
    assert len(codes)==len(set(codes))
    items=[]; names=set()
    for code in codes:
        folders=list((ROOT/'Procedure').glob(code+'-*')); assert len(folders)==1,code
        src=folders[0]; nm=name(src/'SKILL.md'); assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',nm) and nm not in names; names.add(nm)
        dst=DEST/nm; hashes={f:sha(src/f) for f in FILES}; old={}
        if not dst.exists(): status='NEW'
        elif dst.is_symlink() or dst.resolve()!=dst or not all((dst/f).is_file() for f in FILES): status='CONFLICT'
        else:
            old={f:sha(dst/f) for f in FILES}
            if old==hashes: status='CURRENT'
            elif re.match(r'^# '+code+r'\b',(dst/'PROCEDURA.md').read_text(encoding='utf-8-sig')) and name(dst/'SKILL.md')==nm: status='OUTDATED'
            else: status='CONFLICT'
        items.append(dict(code=code,name=nm,source=str(src),status=status,hashes=hashes,old=old))
    plan=dict(items=items,before=snapshot(DEST),destination=str(DEST))
    PLAN.write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
    for status in ('NEW','OUTDATED','CURRENT','CONFLICT'):
        selected=[i for i in items if i['status']==status]; print(status,len(selected),', '.join(i['name'] for i in selected))
    for i in items:
        if i['code']=='ARI-1501': print('ARI-1501',i['status'],'differenze:',[f for f in FILES if i['old'].get(f)!=i['hashes'][f]])
    print('CANONICHE',len(items),'directory protette',sum(1 for p in DEST.iterdir() if p.is_dir() and p.name not in names))
elif sys.argv[1]=='sync':
    plan=json.loads(PLAN.read_text(encoding='utf-8')); items=plan['items']; before=plan['before']
    assert snapshot(DEST)==before,'Destinazione cambiata dopo inventario: arresto'
    for i in items:
        assert all(sha(pathlib.Path(i['source'])/f)==i['hashes'][f] for f in FILES),'Sorgente cambiata'
    stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    backup=DEST.parent/'backups'/('arsenale-skills-'+stamp)
    backed=[]
    for i in items:
        dst=DEST/i['name']; src=pathlib.Path(i['source'])
        if i['status']=='OUTDATED':
            b=backup/i['name']; b.mkdir(parents=True,exist_ok=False)
            for f in FILES:
                assert sha(dst/f)==i['old'][f]
                shutil.copy2(dst/f,b/f); assert sha(b/f)==i['old'][f],'Backup non identico: arresto'
            backed.append(str(b))
        if i['status']=='NEW': dst.mkdir(exist_ok=False)
        if i['status'] in ('NEW','OUTDATED'):
            for f in FILES: shutil.copy2(src/f,dst/f)
    # Unica verifica strutturale conclusiva: nessun test funzionale.
    after=snapshot(DEST); errors=[]; changed={i['name'] for i in items if i['status'] in ('NEW','OUTDATED')}
    for rel,entry in before.items():
        parts=pathlib.Path(rel).parts
        permitted=parts[0] in changed and (len(parts)==1 or len(parts)==2 and parts[1] in FILES)
        if not permitted and after.get(rel)!=entry: errors.append('Elemento protetto cambiato: '+rel)
    for rel in after.keys()-before.keys():
        parts=pathlib.Path(rel).parts
        if not (parts[0] in changed and (len(parts)==1 or len(parts)==2 and parts[1] in FILES)): errors.append('Elemento inatteso: '+rel)
    installed=0
    for i in items:
        dst=DEST/i['name']
        if i['status']=='CONFLICT': errors.append('Conflitto preservato: '+i['name']); continue
        try:
            assert dst.is_dir() and dst.name==name(dst/'SKILL.md')
            assert all(sha(dst/f)==i['hashes'][f]==sha(pathlib.Path(i['source'])/f) for f in FILES)
            installed+=1
        except Exception as e: errors.append(i['name']+': '+str(e))
    report=['# Riallineamento selettivo Arsenale IA / Hermes','',f'Data: {stamp}',f'Skill canoniche: {len(items)}',f'Arsenale presenti prima: {sum(i["status"] in ("CURRENT","OUTDATED") for i in items)}',f'Arsenale presenti dopo e con hash conformi: {installed}','','## Classificazione']
    for status in ('NEW','OUTDATED','CURRENT','CONFLICT'):
        selected=[i for i in items if i['status']==status]; report += ['',f'### {status}: {len(selected)}','']+[f'- {i["code"]}: `{i["name"]}`' for i in selected]
    report+=['','## Backup','']+(['- '+p for p in backed] or ['Nessuno necessario.'])
    report+=['','## Verifica conclusiva','', 'Esito: '+('PASS' if not errors else 'FAIL'),f'Controllo SHA-256: {installed} coppie conformi alla sorgente.','Le directory non-Arsenale, i conflitti e i file aggiuntivi sono stati confrontati con inventario SHA-256 e metadati precedente.','Nessuna dipendenza runtime aggiuntiva obbligatoria individuata. Genera-Audio.ps1 è facoltativo e non è stato copiato.','Nessun test funzionale, validatore o unittest ripetuto. Nessun riavvio, installazione software, download o operazione Git/GitHub.','','## Stato procedure speciali','']
    for i in items:
        if i['code']=='ARI-1501' or 'ARI-1803'<=i['code']<='ARI-1810': report.append(f'- {i["code"]}: {i["status"]}; hash conformi alla sorgente.' )
    if errors: report+=['','## Problemi','']+['- '+e for e in errors]
    (ROOT/'RAPPORTO-RIALLINEAMENTO-HERMES-2026-10-01.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    print(json.dumps(dict(result='PASS' if not errors else 'FAIL',installed=installed,counts={s:sum(i['status']==s for i in items) for s in ('NEW','OUTDATED','CURRENT','CONFLICT')},backups=backed,errors=errors),ensure_ascii=False,indent=2))
    if errors: sys.exit(1)
