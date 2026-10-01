from pathlib import Path
import hashlib,json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];BASE=Path(__file__).resolve().parent
SRC=ROOT.parent/' ponte6'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,t):
    with p.open('x',encoding='utf-8',newline='\n') as f:f.write(t)
def save(p,x):put(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def meta(t,k):
    m=re.search(r'^- \*\*'+re.escape(k)+r':\*\*\s*(.+?)\s*$',t,re.M);return m[1] if m else None
def valids():return {p.parent.name for p in (ROOT/'Verifiche').glob('ARI-*/VER-*.md') if meta(p.read_text(encoding='utf-8'),'Stato evidenza')=='Valida'}
if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');assert not (BASE/'risultati.json').exists() and 'ARI-0401' not in valids()
    catpath=ROOT/'CATALOGO.md';cat=catpath.read_text(encoding='utf-8');a=set(re.findall(r'^- \*\*(ARI-\d{4}) — .*?\*\* — Disponibile\s*$',cat,re.M));before=len(valids()&a)
    baseline={str(p.relative_to(SRC)):sha(p) for p in SRC.rglob('*') if p.is_file() and '.git' not in p.relative_to(SRC).parts};save(BASE/'baseline-progetto.json',baseline)
    repo_baseline={str(p.relative_to(ROOT)):sha(p) for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(BASE) and not any(k in p.relative_to(ROOT).parts for k in ['.git','.codex','.agents','__pycache__'])};save(BASE/'baseline-repository.json',repo_baseline)
    package=json.loads((SRC/'package.json').read_text(encoding='utf-8'));lock=json.loads((SRC/'package-lock.json').read_text(encoding='utf-8'));assert package['scripts']['smoke']=='node scripts/smoke_check.js' and package['version']==lock['version']
    save(BASE/'piano.json',{'procedura':'ARI-0401','bersaglio':str(SRC),'caso':'revisione JS/PWA e smoke script esistente, libreria standard Node','criterio':'exit 0 e OVERALL_OK=true, sorgenti invariati','limiti':'niente Playwright/browser, niente invio WhatsApp, niente build/install','runtime_osservati':'node 24.16.0, npm 11.13.0','lockfile':3})
    run=subprocess.run(['node','scripts/smoke_check.js'],cwd=SRC,capture_output=True,encoding='utf-8',errors='replace',timeout=45);put(BASE/'stdout.log',run.stdout);put(BASE/'stderr.log',run.stderr)
    unchanged=all((SRC/n).exists() and sha(SRC/n)==h for n,h in baseline.items())
    newfiles={str(p.relative_to(SRC)) for p in SRC.rglob('*') if p.is_file() and '.git' not in p.relative_to(SRC).parts}-set(baseline)
    passed=run.returncode==0 and 'OVERALL_OK=true' in run.stdout and unchanged and not newfiles
    core=(SRC/'js/core.js').read_text(encoding='utf-8');order=(SRC/'js/order.js').read_text(encoding='utf-8')
    review={'stack':'HTML/CSS/JavaScript PWA, nessun transpiler o build richiesto','moduli':'script browser e CommonJS per smoke; nessun TypeScript/any/tsconfig','lockfile_coerente_versione':True,'dipendenze':'Playwright devDependency presente, non avviato; smoke usa node:http, fs/promises, path e fetch standard','client':'order.js usa PonteCart/PONTE_CONFIG/PonteUtils; escapeHtml importato, ma uso in tutte le interpolazioni non provato','server':'solo HTTP temporaneo su 127.0.0.1, porta dinamica, confinamento path.resolve e startsWith separatore; nessun backend ordini avviato','errori':'smoke usa try/catch e close nel finally; endpoint file falliti restituiscono 404','sicurezza':'nessuna scansione segreti completa; non dichiarata sicurezza generale','build':'nessuna build necessaria per sito statico; asset esistenti serviti','lint_typecheck':'non configurati nel package, controllo non eseguito','browser_compatibilita':'non verificata; nessun test browser sostitutivo'}
    findings=[{'priorita':'P2','file':'scripts/smoke_check.js','rilievo':'HTTP 200 e byte positivi non dimostrano correttezza JS/carrello né accessibilità; non approvare flusso ordine da solo smoke'},{'priorita':'P3','file':'AGENTS.md / package.json','rilievo':'AGENTS afferma assenza suite oltre smoke ma package espone test:e2e; documentazione da riallineare, nessuna modifica'},{'priorita':'P3','file':'package.json','rilievo':'engines node>=18, smoke usa fetch; reale compatibilità verificata soltanto Node 24.16.0'}]
    results={'code':'ARI-0401','test':'Smoke HTTP locale già previsto dal progetto più revisione JS/PWA','risultato':'PASS' if passed else 'FAIL','exit_code':run.returncode,'target_http_ok':len(re.findall(r'^\[OK\]',run.stdout,re.M)),'sorgenti_invariati':unchanged,'nuovi_file_progetto':sorted(newfiles),'review':review,'rilievi':findings,'classificazione':'Valida' if passed else None,'tipo':'Interna','fonte':'progetto Ponte6 esistente, prova conservativamente interna alla campagna'};save(BASE/'risultati.json',results)
    save(BASE/'snapshot.json',{str(p.relative_to(ROOT)):sha(p) for p in BASE.rglob('*') if p.is_file()})
    if passed:
        ed=ROOT/'Verifiche/ARI-0401';ed.mkdir(exist_ok=True);ident='VER-ARI-0401-20261001-01';assert not (ed/(ident+'.md')).exists()
        put(ed/(ident+'.md'),f'''# {ident} — Revisione JS su sito locale esistente

- **Identificativo:** {ident}
- **Procedura:** ARI-0401
- **Versione procedura:** 0.2.0
- **Data:** 2026-10-01
- **Progetto:** Arsenale-IA/campagna-C-Ponte6
- **Revisione:** SHA-256 snapshot.json: {sha(BASE/'snapshot.json')}
- **Tipo prova:** Interna
- **Stato evidenza:** Valida

## Ambito

Revisione JavaScript/PWA del progetto locale Ponte6 per il ramo caricamento di pagine e risorse. Progetto reale già esistente, non fixture inventata; prova conservativamente Interna, nessuna promozione basata su indipendenza. Piano definito prima della prova, nessuna Valida preesistente.

## Ambiente e accesso

Windows, Node 24.16.0/npm 11.13.0 già rilevati, lockfile versione 3 e node_modules presenti. Nessuna installazione, npm restore, browser o servizio esterno. Smoke usa listener temporaneo su loopback porta dinamica, chiuso nel finally. Il progetto originale è letto ed eseguito senza modifiche; baseline per SHA-256 delle sorgenti e dipendenze locali conservata.

## Passi esercitati

Letti STANDARD.md, procedura/adattatore, package/lock, README, AGENTS e smoke script. Identificati stack, moduli, dipendenze, entrypoint, errori, confine del server file, separazione client/server. Eseguito un solo smoke già previsto dal progetto. Confrontati file preesistenti per hash e assenza di file nuovi. Prodotti rilievi prioritizzati senza correggere software o documentazione.

## Verifiche osservabili

Exit code {run.returncode}; {results['target_http_ok']} risorse HTTP 200 con byte positivi; OVERALL_OK=true. SHA-256 invariati nel perimetro baseline. Log in ../Triage-C-20261001/stdout.log e stderr.log; review dettagliata in risultati.json. Nessun test DOM o Playwright eseguito.

## Rilievi prodotti

P2: scripts/smoke_check.js dimostra trasporto e presenza degli asset, non esecuzione del carrello o correttezza del flusso ordine. P3: AGENTS.md e package.json divergono sulla suite disponibile. P3: supporto Node>=18 dichiarato, provato qui solo 24.16.0. Piano: documentare la copertura e usare la suite browser solo in successivo contesto autorizzato e disponibile; nessuna correzione automatica.

## Limiti

Nessuna build/transpilazione richiesta da questo sito statico. Lint e type-check non configurati, compatibilità browser, layout, accessibilità e ordine WhatsApp non provati. Lock controllato per identità/versione, nessuna reinstallazione deterministica effettuata. Nessun audit completo dei segreti o di tutte le interpolazioni HTML. Prova sul ramo HTTP, non dichiarazione di prontezza generale della PWA. Nessuna revisione umana.

## Esito sul progetto

**Idoneo con vincoli** per disponibilità delle risorse via HTTP e revisione delimitata; flusso ordine non certificato. Nessun dato inviato al ristorante o a servizi esterni.

## Esito sulla procedura

Evidenza **Valida / Interna** nel perimetro esercitato: applicazione, log, input, revisione e limiti tracciati. Procedura Bozza verificabile, matrice Da verificare. Nessuna promozione: manca soglia di almeno due rapporti validi su contesti distinti con una prova Indipendente; soglie invariate.
''')
        bak=BASE/'CATALOGO-prima.md.bak';bak.write_bytes(catpath.read_bytes());assert sha(bak)==sha(catpath);save(BASE/'backup.json',{'sha256':sha(bak),'file':bak.name})
        cat,n=re.subn(r'^(\| ARI-0401 — .*? \| Da verificare \| )0( \| No \|)$',r'\g<1>1\2',cat,flags=re.M);assert n==1;catpath.write_text(cat,encoding='utf-8',newline='\n')
    unexpected=[n for n,h in repo_baseline.items() if n!='CATALOGO.md' and (not (ROOT/n).exists() or sha(ROOT/n)!=h)];save(BASE/'integrita.json',{'modifiche_inattese_repository':unexpected,'sorgenti_ponte6_invariati':unchanged,'nuovi_file_ponte6':sorted(newfiles)});assert not unexpected
    after=len(valids()&a);save(BASE/'contatori.json',{'disponibili':len(a),'con_valida_prima':before,'con_valida_dopo':after,'senza_valida_prima':len(a)-before,'senza_valida_dopo':len(a)-after,'verificate':len(re.findall(r'^\| ARI-\d{4} — .*? \| \*\*Verificata\*\* \|',cat,re.M)),'da_verificare':len(re.findall(r'^\| ARI-\d{4} — .*? \| Da verificare \|',cat,re.M))});print(json.dumps(results,ensure_ascii=False))
