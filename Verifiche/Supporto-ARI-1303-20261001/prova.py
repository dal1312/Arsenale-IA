from pathlib import Path
import os, re, hashlib, json, platform, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert not (OUT/'inventario.json').exists()
assert not (ROOT/'Verifiche/ARI-1303').exists()
# Perimetro e criteri fissati prima del rilevamento.
criteria='File regolari nella radice e ricorsivamente in Procedure e Strumenti; escludere .git, profili/configurazioni esterne, Verifiche e cache __pycache__. Nessun link seguito. Corrispondenza esatta fra elenco filesystem e inventario; percorsi relativi univoci, dimensioni/hash corretti, leggibilità del report, corrispondenza procedure disponibili/catalogo.'
selected=[]; excluded=[]
for p in ROOT.iterdir():
    if p.is_file() and not p.is_symlink(): selected.append(p)
for section in ('Procedure','Strumenti'):
    for base,dirs,files in os.walk(ROOT/section,followlinks=False):
        for d in list(dirs):
            p=Path(base)/d
            if d=='__pycache__' or p.is_symlink() or p.is_junction():
                excluded.append(str(p.relative_to(ROOT))); dirs.remove(d)
        for f in files:
            p=Path(base)/f
            if p.is_symlink(): excluded.append(str(p.relative_to(ROOT)))
            elif p.is_file(): selected.append(p)
entries=[]
for p in sorted(selected):
    st=p.stat(); entries.append(dict(percorso=p.relative_to(ROOT).as_posix(),dimensione=st.st_size,mtime_ns=st.st_mtime_ns,sha256=sha(p),categoria='procedura' if p.is_relative_to(ROOT/'Procedure') else 'strumento' if p.is_relative_to(ROOT/'Strumenti') else 'file principale'))
catalog=(ROOT/'CATALOGO.md').read_text(encoding='utf-8')
codes=re.findall(r'^- \*\*(ARI-\d{4})[^\n]+\*\* — Disponibile\s*$',catalog,re.M)
procedures=[]
for code in codes:
    found=list((ROOT/'Procedure').glob(code+'-*/PROCEDURA.md')); assert len(found)==1
    p=found[0]; text=p.read_text(encoding='utf-8'); skill=p.parent/'SKILL.md'; assert skill.is_file()
    procedures.append(dict(codice=code,cartella=p.parent.relative_to(ROOT).as_posix(),stato=re.search(r'^- \*\*Stato:\*\*\s*(.+)$',text,re.M)[1],runtime=re.search(r'^name:\s*(.+)$',skill.read_text(encoding='utf-8'),re.M)[1].strip()))
data=dict(criteri=criteria,sistema=platform.platform(),python=sys.version,eseguibile=sys.executable,script_sha256=sha(Path(__file__)),file=entries,procedure_disponibili=procedures,esclusioni=excluded,controlli={})
assert len({e['percorso'] for e in entries})==len(entries)
assert len(set(codes))==len(codes)
assert len({p['runtime'] for p in procedures})==len(procedures)
for e in entries:
    p=ROOT/e['percorso']; assert p.stat().st_size==e['dimensione'] and p.stat().st_mtime_ns==e['mtime_ns'] and sha(p)==e['sha256']
data['controlli']=dict(file_verificati=len(entries),procedure_disponibili=len(procedures),sorgenti_invariate=True,percorsi_univoci=True,catalogo_cartelle_coerenti=True,esito='PASS')
jp=OUT/'inventario.json'; jp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert json.loads(jp.read_text(encoding='utf-8'))==data
lines=['# Inventario operativo Arsenale IA','',f'File rilevati: {len(entries)}. Procedure disponibili: {len(procedures)}.','', 'Perimetro: '+criteria,'','## Procedure','', '| Codice | Cartella | Runtime | Stato |','|---|---|---|---|']
lines += [f'| {p["codice"]} | {p["cartella"]} | {p["runtime"]} | {p["stato"]} |' for p in procedures]
lines+=['','## File principali e strumenti','']+[f'- `{e["percorso"]}` — {e["dimensione"]} byte; SHA-256 `{e["sha256"]}`' for e in entries if e['categoria']!='procedura']
md=OUT/'INVENTARIO.md'; md.write_text('\n'.join(lines)+'\n',encoding='utf-8')
assert all(p['codice'] in md.read_text(encoding='utf-8') for p in procedures)
report=f'''# VER-ARI-1303-20261001-01 — Inventario operativo del repository locale

- **Identificativo:** VER-ARI-1303-20261001-01
- **Procedura:** ARI-1303
- **Versione procedura:** 0.1.0
- **Data:** 2026-10-01
- **Progetto:** Arsenale-IA
- **Revisione:** SHA-256 inventario.json: {sha(jp)}
- **Tipo prova:** Interna
- **Stato evidenza:** Valida

## Ambito

Produzione reale di una mappa di orientamento del repository corrente: file principali, cartelle di procedure, adattatori runtime, stato dichiarato e strumenti locali. Perimetro definito prima della scansione: radice, Procedure e Strumenti. Verifiche, .git e sistemi esterni esclusi. Nessuna estensione dei test ARI-1302/ARI-1807.

## Ambiente e accesso

Windows, Python già disponibile `{sys.executable}`, sola libreria standard. Versione e sistema registrati nel JSON. Sorgenti lette senza modifica; output nuovi sotto `Verifiche/Supporto-ARI-1303-20261001`. Nessuna installazione, rete o modifica a configurazioni. Lo script effettivamente eseguito è conservato e identificato tramite hash.

## Passi esercitati

1. Definiti obiettivo operativo, criteri, perimetro ed esclusioni.
2. Enumerati file reali e metadati senza seguire link o directory di cache.
3. Classificati file principali, strumenti e procedure; esclusi metadati Git e profili esterni per minimizzare rischi e dati sensibili. Non è dichiarato un audit del contenuto alla ricerca di segreti.
4. Prodotti inventario JSON dettagliato e mappa Markdown leggibile.
5. Collegati codici disponibili, cartelle, nomi runtime e stati osservati.
6. Verificati unicità, integrità dei file rilevati, invarianza delle sorgenti durante il test e rilettura del JSON serializzato.
7. Documentati risultati, confini e limiti senza modificare il progetto inventariato.

## Verifiche osservabili

Unica esecuzione operativa: Python `-B Verifiche/Supporto-ARI-1303-20261001/prova.py`. Asserzioni riuscite su {len(entries)} file e {len(procedures)} procedure disponibili. Tutti i percorsi sono univoci; ogni hash, dimensione e timestamp corrisponde al file sorgente al controllo. Ogni codice disponibile individua una cartella canonica con PROCEDURA.md e SKILL.md. JSON riletto identico all'inventario generato. Output: `../Supporto-ARI-1303-20261001/inventario.json` e `../Supporto-ARI-1303-20261001/INVENTARIO.md`, quest'ultimo SHA-256 {sha(md)}.

## Rilievi prodotti

Inventario concretamente consultabile: mappa delle procedure e degli strumenti con file di ingresso e stato dichiarato. Nessun percorso duplicato o procedura disponibile priva dei due file rilevato. Priorità principale soddisfatta: rendere navigabile la struttura senza alterare sorgenti. Lo stato osservato non è una nuova attestazione di funzionamento delle altre procedure.

## Limiti

Snapshot puntuale del perimetro dichiarato prima dell'aggiornamento documentale della matrice. Non comprende evidenze, contenuti Git, profili utente, modelli, dipendenze installate o file esterni. Non verifica l'eseguibilità degli strumenti inventariati, permessi avanzati o licenze dei loro contenuti. I file principali vengono catalogati, non ne viene riprodotto il contenuto nel Markdown. Prova interna, non indipendente; nessun esito funzionale attribuito ad altre procedure.

## Esito sul progetto

**Idoneo** per orientamento e tracciabilità del perimetro scelto: mappa leggibile e inventario con hash prodotti, riletti e controllati. Nessuna azione residua per il test selezionato.

## Esito sulla procedura

Evidenza **Valida**: tutte le sette fasi sostanziali della versione 0.1.0 sono state applicate al progetto reale, con output operativo e controlli osservabili. La procedura resta **Bozza verificabile**. La matrice registra una evidenza valida e prova indipendente No. Mancano una seconda evidenza valida su progetto distinto e almeno una prova indipendente. Nessuna soglia viene modificata.
'''
d=ROOT/'Verifiche/ARI-1303'; d.mkdir(); (d/'VER-ARI-1303-20261001-01.md').write_text(report,encoding='utf-8')
cat=ROOT/'CATALOGO.md'; old=cat.read_bytes(); backup=OUT/'CATALOGO-prima-20261001.md.bak'; backup.write_bytes(old); assert sha(backup)==sha(cat)
text=old.decode('utf-8'); row='| ARI-1303 — Inventario progetto locale | Da verificare | 0 | No |'; assert text.count(row)==1
cat.write_bytes(text.replace(row,'| ARI-1303 — Inventario progetto locale | Da verificare | 1 | No |').encode('utf-8'))
print(f'TEST PASS: {len(entries)} file, {len(procedures)} procedure. Evidenza Valida interna e matrice aggiornate; backup catalogo verificato.')
