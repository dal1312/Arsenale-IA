from pathlib import Path
import hashlib, json, shutil, datetime, sys, platform

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
sources = ['STANDARD.md', 'VERIFICA.md', 'Procedure/ARI-1302-gestione-backup-locali/PROCEDURA.md', 'Procedure/ARI-1302-gestione-backup-locali/SKILL.md']
backup = BASE / 'backup-documenti-20261001'
restore = BASE / 'ripristino-isolato'
assert not backup.exists() and not restore.exists(), 'Destinazioni esistenti: arresto'
assert not (ROOT/'Verifiche/ARI-1302').exists(), 'Evidenze preesistenti: arresto'
criteria = dict(perimetro=sources, verifica='Hash SHA-256 e dimensioni identici fra sorgente, backup e ripristino; originali invariati; ripristino selettivo dei due file ARI-1302 soltanto', rischi='Copie documentali senza credenziali; nessun overwrite o cancellazione; spazio verificato; nessuna rete; backup conservato', conservazione='Conservare questa copia e manifest senza rotazione o eliminazione automatica; backup locale sullo stesso volume, nessuna protezione da perdita disco')
before = {s:dict(sha256=sha(ROOT/s),bytes=(ROOT/s).stat().st_size,mtime_ns=(ROOT/s).stat().st_mtime_ns) for s in sources}
free = shutil.disk_usage(BASE).free
assert free > sum(v['bytes'] for v in before.values())*3+1048576
backup.mkdir(); restore.mkdir()
checks=[]
for s in sources:
    dst=backup/s; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(ROOT/s,dst)
    assert sha(dst)==before[s]['sha256'] and dst.stat().st_size==before[s]['bytes']
    checks.append(dict(file=s,backup_hash=sha(dst),backup_conforme=True))
for s in sources[2:]:
    dst=restore/s; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(backup/s,dst)
    assert sha(dst)==before[s]['sha256'] and dst.stat().st_size==before[s]['bytes']
    checks.append(dict(file=s,ripristino_hash=sha(dst),ripristino_conforme=True))
assert sorted(str(p.relative_to(restore)).replace('\\','/') for p in restore.rglob('*') if p.is_file())==sorted(sources[2:])
for s in sources:
    p=ROOT/s
    assert sha(p)==before[s]['sha256'] and p.stat().st_mtime_ns==before[s]['mtime_ns']
result=dict(data=datetime.datetime.now().astimezone().isoformat(),criteri=criteria,sorgenti=before,controlli=checks,originali_invariati=True,spazio_libero_iniziale=free,python=sys.version,eseguibile=sys.executable,sistema=platform.platform(),hash_script=sha(Path(__file__)),esito='PASS')
rp=BASE/'risultati.json'; rp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=f'''# VER-ARI-1302-20261001-01 — Backup e ripristino selettivo di documenti reali

- **Identificativo:** VER-ARI-1302-20261001-01
- **Procedura:** ARI-1302
- **Versione procedura:** 0.1.0
- **Data:** 2026-10-01
- **Progetto:** Arsenale-IA
- **Revisione:** SHA-256 risultati.json: {sha(rp)}
- **Tipo prova:** Interna
- **Stato evidenza:** Valida

## Ambito

Un solo ciclo reale: copia di sicurezza di quattro documenti esistenti del repository e ripristino selettivo dei due file della procedura ARI-1302. Criteri fissati nello script prima della copia: hash e dimensioni identici, originali invariati, nessun file estraneo ripristinato. Nessuna generazione audio o intervento su ARI-1807.

## Ambiente e accesso

Windows, Python già presente: `{sys.executable}`. Versione e sistema sono registrati in `../Supporto-ARI-1302-20261001/risultati.json`. Solo lettura delle sorgenti e scrittura in directory nuove nel repository. Spazio libero verificato prima della copia: {free} byte. Nessuna installazione, download, operazione remota o modifica alle configurazioni. Lo script realmente eseguito è archiviato con hash nel risultato.

## Passi esercitati

1. Definiti perimetro, obiettivo e criteri di accettazione.
2. Rilevati hash, dimensioni e timestamp degli originali.
3. Classificati rischi e dipendenze: file documentali senza credenziali, libreria standard già presente, nessuna cancellazione o sovrascrittura.
4. Creata copia denominata `backup-documenti-20261001` preservando i percorsi relativi.
5. Verificati tutti e quattro i file copiati.
6. Ripristinati soltanto PROCEDURA.md e SKILL.md in `ripristino-isolato`, senza toccare gli originali.
7. Verificati hash, dimensioni, selettività del ripristino e invarianza degli originali.

## Verifiche osservabili

Esecuzione: Python con opzione `-B` su `Verifiche/Supporto-ARI-1302-20261001/prova.py`. Tutte le asserzioni sono riuscite. Quattro copie conformi e due file ripristinati conformi. SHA-256, dimensioni e risultati individuali sono in risultati.json; backup e ripristino restano ispezionabili nella stessa directory di supporto. I controlli sono reali sulle copie prodotte, non dedotti dalla sola lettura del codice.

## Rilievi prodotti

Nessuna discordanza rilevata. Priorità principale: evitare overwrite, soddisfatta mediante destinazioni nuove. Seconda priorità: recuperabilità dei file selezionati, dimostrata tramite lettura dal backup e confronto byte-identico. Conservazione: mantenere copia e manifest senza rotazione automatica; nessun backup è stato eliminato.

## Limiti

La prova riguarda documenti locali e ripristino isolato: non simula guasto disco, non sostituisce file operativi e non verifica ACL, flussi alternativi NTFS, database aperti, cifratura o recupero su altro volume. La copia sullo stesso volume non protegge dalla perdita del disco. Questi rami non sono richiesti dal perimetro selezionato. Si tratta di una sola prova interna su Arsenale IA; non è una prova indipendente. Nessun esito viene attribuito ad altre procedure.

## Esito sul progetto

**Idoneo** per il perimetro documentale: backup realmente creato, integrità verificata, ripristino selettivo riuscito e sorgenti preservate. Nessuna azione residua richiesta per il ciclo esercitato.

## Esito sulla procedura

Evidenza **Valida**: copre le sette fasi sostanziali della versione 0.1.0, con esecuzione reale, revisione immutabile e limiti dichiarati. La procedura resta **Bozza verificabile**: una sola evidenza interna non soddisfa i due rapporti validi su due progetti distinti con almeno una prova indipendente. La matrice passa a una evidenza valida, prova indipendente No. Nessuna soglia viene modificata.
'''
directory=ROOT/'Verifiche/ARI-1302'; directory.mkdir()
(directory/'VER-ARI-1302-20261001-01.md').write_text(report,encoding='utf-8')
catalog=ROOT/'CATALOGO.md'; old=catalog.read_bytes()
catalog_backup=BASE/'CATALOGO-prima-20261001.md.bak'; catalog_backup.write_bytes(old)
assert sha(catalog_backup)==sha(catalog)
text=old.decode('utf-8'); original='| ARI-1302 — Gestione backup locali | Da verificare | 0 | No |'
assert text.count(original)==1
catalog.write_bytes(text.replace(original,'| ARI-1302 — Gestione backup locali | Da verificare | 1 | No |').encode('utf-8'))
print('TEST PASS: 4 backup, 2 ripristini selettivi, originali invariati. Evidenza Valida interna creata. Catalogo aggiornato con backup verificato.')
