param(
    [switch]$Forza
)

$ErrorActionPreference = "Stop"

function Converti-Slug {
    param([string]$Testo)
    $slug = $Testo.ToLowerInvariant()
    $slug = $slug.Replace("à", "a").Replace("è", "e").Replace("é", "e").Replace("ì", "i").Replace("ò", "o").Replace("ù", "u")
    $slug = $slug -replace "[^a-z0-9]+", "-"
    return $slug.Trim("-")
}

function Nuova-Procedura {
    param($Voce)

    $uso = @(
        "- quando serve applicare questa competenza in modo ripetibile",
        "- quando l'attivita coinvolge $($Voce.Focus)",
        "- prima di consolidare modifiche locali o consegnare un risultato",
        "- quando servono evidenze, limiti e controlli documentati"
    ) -join "`n"

    $nonUso = @(
        "- manca un obiettivo operativo verificabile",
        "- il perimetro di file, dati o sistemi non e chiaro",
        "- la richiesta richiede accessi o privilegi non autorizzati",
        "- si vuole sostituire una verifica reale con una supposizione"
    ) -join "`n"

    $materiale = @(
        "- obiettivo e risultato atteso",
        "- file, cartelle, risorse o configurazioni coinvolte",
        "- vincoli locali, permessi e limiti noti",
        "- esempi, log, schermate o report disponibili",
        "- criterio di uscita o definizione di completato"
    ) -join "`n"

    $controlli = @(
        "- perimetro confermato prima dell'intervento",
        "- evidenze raccolte e distinguibili da ipotesi",
        "- rischi principali identificati e prioritizzati",
        "- azioni proposte o svolte coerenti con il progetto locale",
        "- verifiche finali eseguite o impedimenti motivati"
    ) -join "`n"

    $errori = @(
        "- iniziare da strumenti o automazioni prima di chiarire il metodo",
        "- modificare file fuori perimetro",
        "- ignorare backup, dati sensibili o licenze",
        "- dichiarare riuscita un'attivita non verificata",
        "- produrre report generici non collegati a evidenze"
    ) -join "`n"

    return @"
# $($Voce.Codice) — $($Voce.Titolo)

- **Categoria:** $($Voce.Categoria)
- **Livello:** $($Voce.Livello)
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** $($Voce.Offline)

## Scopo

$($Voce.Scopo)

## Campo di applicazione

$($Voce.Campo)

## Quando usarla

$uso

## Quando non usarla

$nonUso

## Prerequisiti

- obiettivo operativo definito
- ambiente locale o artefatto da analizzare disponibile
- vincoli di accesso e modifica chiariti
- criteri minimi di accettazione dichiarati
- eventuali rischi su dati, licenze o permessi identificati

## Materiale necessario

$materiale

## Procedura operativa

1. Definire obiettivo, perimetro e vincoli dell'attivita.
2. Raccogliere le evidenze minime necessarie senza ampliare il campo di lavoro.
3. Classificare rischi, dipendenze, dati sensibili e impatti operativi.
4. Applicare il metodo specifico a $($Voce.Focus), mantenendo tracciabili decisioni e assunzioni.
5. Proporre o realizzare l'intervento minimo sufficiente, con priorita e limiti espliciti.
6. Verificare il risultato con controlli proporzionati al rischio.
7. Documentare esito, file coinvolti, controlli eseguiti e azioni residue.

## Controlli

$controlli

## Errori frequenti

$errori

## Rapporto finale

Riportare obiettivo, perimetro, evidenze raccolte, decisioni prese, controlli eseguiti, rischi residui, file o risorse coinvolte e verdetto operativo. Usare uno dei verdetti: **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente**.

## Condizioni di uscita

- perimetro e limiti documentati
- decisioni collegate a evidenze verificabili
- controlli minimi completati o impedimenti motivati
- rischi residui esplicitati
- prossimo passo operativo chiaro

## Cronologia delle versioni

- **0.1.0** — Prima versione operativa per $($Voce.Storia).
"@
}

function Nuova-Skill {
    param($Voce)

    return @"
---
name: $($Voce.Skill)
description: $($Voce.Descrizione)
---

# $($Voce.Titolo)

Segui integralmente la procedura descritta in `PROCEDURA.md` nella stessa cartella.

## Comportamento obbligatorio

- Chiarisci obiettivo, perimetro e vincoli prima di operare.
- Lavora su evidenze locali e distingue fatti, ipotesi e limiti.
- Evita interventi distruttivi o ampliamenti non richiesti.
- Produci risultato, controlli e rischi residui in italiano tecnico.
- Quando mancano dati essenziali, dichiara cosa non e verificabile.
"@
}

$voci = @(
    [pscustomobject]@{Codice="ARI-1101";Titolo="Documentazione tecnica progetto";Categoria="Documentazione e manualistica";Livello="L3 Avanzato";Offline="Sì";Skill="documentazione-tecnica-progetto";Focus="documentazione tecnica di progetto";Storia="documentazione tecnica di progetto";Scopo="Produrre documentazione tecnica coerente con la struttura reale di un progetto, rendendo comprensibili architettura, componenti, flussi, strumenti e limiti operativi.";Campo="README, manuali tecnici, note architetturali, documenti di installazione, spiegazioni di procedure, mappe repository e guide manutentive.";Descrizione="Crea o revisiona documentazione tecnica di progetto in italiano, collegando struttura reale, comandi, componenti, limiti e verifiche."},
    [pscustomobject]@{Codice="ARI-1102";Titolo="Manuale utente locale";Categoria="Documentazione e manualistica";Livello="L2 Intermedio";Offline="Sì";Skill="manuale-utente-locale";Focus="manuali utente locali";Storia="manuali utente locali";Scopo="Creare guide pratiche per usare localmente un progetto, riducendo passaggi impliciti e rendendo l'uso accessibile anche a chi non conosce la struttura interna.";Campo="Manuali rapidi, istruzioni passo-passo, guide di primo uso, esempi di richiesta, mappe di accesso ai file e procedure locali.";Descrizione="Crea manuali utente locali e guide rapide in italiano per usare un progetto senza conoscere la struttura tecnica interna."},
    [pscustomobject]@{Codice="ARI-1103";Titolo="Glossario italiano tecnico";Categoria="Documentazione e manualistica";Livello="L2 Intermedio";Offline="Sì";Skill="glossario-italiano-tecnico";Focus="lessico italiano tecnico";Storia="glossario italiano tecnico";Scopo="Mantenere coerente il lessico italiano tecnico del progetto, decidendo quali termini tradurre, quali mantenere come nomi tecnici e quali normalizzare.";Campo="Glossari, convenzioni linguistiche, traduzione di termini tecnici, standardizzazione di documenti e procedure in italiano.";Descrizione="Normalizza il lessico italiano tecnico del progetto, preservando nomi tecnici, comandi e identificatori quando necessario."},
    [pscustomobject]@{Codice="ARI-1201";Titolo="Automazione PowerShell";Categoria="Automazione locale";Livello="L3 Avanzato";Offline="Sì";Skill="automazione-powershell";Focus="script PowerShell locali";Storia="automazione PowerShell locale";Scopo="Progettare, revisionare e rendere sicuri script PowerShell per operazioni locali ripetibili su Windows.";Campo="Script PowerShell, installatori locali, controlli file, generazione report, automazioni di manutenzione e comandi Windows.";Descrizione="Crea e revisiona automazioni PowerShell locali sicure, ripetibili e leggibili per Windows e progetti su filesystem."},
    [pscustomobject]@{Codice="ARI-1202";Titolo="Automazione Python CLI";Categoria="Automazione locale";Livello="L3 Avanzato";Offline="Sì";Skill="automazione-python-cli";Focus="strumenti Python da riga di comando";Storia="automazione Python da riga di comando";Scopo="Creare strumenti Python da riga di comando per analizzare, validare, generare o trasformare file locali in modo ripetibile.";Campo="CLI Python, validatori, generatori report, analisi cartelle, trasformazioni testuali, controlli offline e strumenti di supporto progetto.";Descrizione="Crea strumenti Python CLI locali per validare, generare, analizzare o trasformare file del progetto in modo ripetibile."},
    [pscustomobject]@{Codice="ARI-1203";Titolo="Flusso locale ripetibile";Categoria="Automazione locale";Livello="L3 Avanzato";Offline="Sì";Skill="flusso-locale-ripetibile";Focus="sequenze locali ripetibili";Storia="flussi locali ripetibili";Scopo="Trasformare una sequenza di operazioni locali in un flusso ripetibile, documentato e verificabile senza dipendere da servizi esterni.";Campo="Sequenze di verifica, installazione locale, generazione report, manutenzione biblioteca, controlli periodici e procedure operative.";Descrizione="Trasforma operazioni locali ricorrenti in flussi ripetibili, documentati e verificabili senza dipendere da servizi esterni."},
    [pscustomobject]@{Codice="ARI-1301";Titolo="Pulizia progetto locale";Categoria="Gestione locale e manutenzione";Livello="L3 Avanzato";Offline="Sì";Skill="pulizia-progetto-locale";Focus="pulizia controllata di file locali";Storia="pulizia controllata di progetti locali";Scopo="Analizzare e pulire un progetto locale distinguendo file necessari, cache, backup, duplicati e artefatti temporanei, con priorita alla reversibilita.";Campo="Cartelle di progetto locali, cache Python, backup, file temporanei, artefatti generati, report di pulizia e piani di rimozione.";Descrizione="Analizza e pulisce progetti locali distinguendo cache, backup, duplicati e file utili con criteri reversibili e verificabili."},
    [pscustomobject]@{Codice="ARI-1302";Titolo="Gestione backup locali";Categoria="Gestione locale e manutenzione";Livello="L3 Avanzato";Offline="Sì";Skill="gestione-backup-locali";Focus="backup locali e ripristino";Storia="gestione backup locali";Scopo="Definire e applicare una strategia locale per creare, nominare, verificare e ripristinare backup di file e cartelle di progetto.";Campo="Backup manuali, file .bak, snapshot locali, copie prima di modifiche, conservazione ordinata e ripristino selettivo.";Descrizione="Organizza backup locali, file .bak e ripristini selettivi con nomi, criteri e verifiche controllate."},
    [pscustomobject]@{Codice="ARI-1303";Titolo="Inventario progetto locale";Categoria="Gestione locale e manutenzione";Livello="L2 Intermedio";Offline="Sì";Skill="inventario-progetto-locale";Focus="inventario cartelle e file";Storia="inventario di progetti locali";Scopo="Produrre un inventario leggibile di un progetto locale, descrivendo cartelle, procedure, strumenti, file speciali e stato operativo.";Campo="Mappe progetto, report cartelle, elenchi procedure, file di ingresso, strumenti locali e documentazione di orientamento.";Descrizione="Produce inventari locali leggibili di cartelle, procedure, strumenti e file principali di un progetto."},
    [pscustomobject]@{Codice="ARI-1304";Titolo="Ripristino controllato locale";Categoria="Gestione locale e manutenzione";Livello="L4 Professionale";Offline="Sì";Skill="ripristino-controllato-locale";Focus="ripristino locale da backup";Storia="ripristino locale controllato";Scopo="Recuperare file o stati precedenti da backup e copie locali senza sovrascrivere materiale corrente in modo non controllato.";Campo="Ripristino da .bak, confronto copie, recupero file singoli, verifica contenuto recuperato e piani di rollback locali.";Descrizione="Guida ripristini locali selettivi da backup o copie precedenti, con confronto e protezione dello stato corrente."},
    [pscustomobject]@{Codice="ARI-1401";Titolo="Confezionamento app Windows";Categoria="Applicazioni desktop Windows";Livello="L4 Professionale";Offline="Sì";Skill="confezionamento-app-windows";Focus="pacchetti app Windows";Storia="confezionamento di app Windows";Scopo="Preparare applicazioni Windows per distribuzione locale, verificando artefatti, cartelle, dipendenze, avvio, icone e metadati essenziali.";Campo="App Electron, Tauri, Flutter, .NET MAUI, WinUI, WPF, Qt, eseguibili locali, cartelle release e pacchetti portabili.";Descrizione="Prepara e verifica pacchetti locali di app Windows, controllando artefatti, dipendenze, avvio, icone e metadati."},
    [pscustomobject]@{Codice="ARI-1402";Titolo="Installatore Windows locale";Categoria="Applicazioni desktop Windows";Livello="L4 Professionale";Offline="Sì";Skill="installatore-windows-locale";Focus="installatori Windows locali";Storia="installatori Windows locali";Scopo="Progettare o revisionare un installatore Windows locale, controllando destinazioni, scorciatoie, disinstallazione, permessi e aggiornamento.";Campo="Installatori PowerShell, MSIX, MSI, NSIS, Inno Setup, script locali e procedure di installazione manuale controllata.";Descrizione="Crea o revisiona installatori Windows locali con percorsi, scorciatoie, permessi, aggiornamento e disinstallazione controllati."},
    [pscustomobject]@{Codice="ARI-1403";Titolo="Icone e metadati app";Categoria="Applicazioni desktop Windows";Livello="L2 Intermedio";Offline="Sì";Skill="icone-metadati-app";Focus="icone e metadati applicazione";Storia="icone e metadati app";Scopo="Preparare e verificare icone, nome applicazione, versione, descrizione, autore e metadati visibili di una app locale.";Campo="Icone ICO/PNG/SVG, manifest, metadati eseguibile, nome prodotto, descrizioni, versioni e risorse grafiche di app.";Descrizione="Prepara e verifica icone, nome, versione, descrizione e metadati per app locali e pacchetti Windows."},
    [pscustomobject]@{Codice="ARI-1502";Titolo="Ottimizzazione inferenza locale";Categoria="Intelligenza artificiale";Livello="L4 Professionale";Offline="Sì";Skill="ottimizzazione-inferenza-locale";Focus="inferenza IA locale";Storia="ottimizzazione inferenza IA locale";Scopo="Ottimizzare inferenza IA locale migliorando latenza, memoria, contesto, parallelismo, quantizzazione e configurazione runtime senza perdere tracciabilita.";Campo="LLM locali, runtime llama.cpp, Ollama, LM Studio, vLLM, quantizzazioni, parametri server, batch, contesto e accelerazione hardware.";Descrizione="Ottimizza inferenza IA locale misurando latenza, memoria, parametri, quantizzazione e qualita senza perdere ripetibilita."},
    [pscustomobject]@{Codice="ARI-1601";Titolo="Revisione modelli linguistici";Categoria="Intelligenza artificiale";Livello="L4 Professionale";Offline="Sì";Skill="revisione-modelli-linguistici";Focus="modelli linguistici";Storia="revisione di modelli linguistici";Scopo="Revisionare comportamento, limiti, prompt, robustezza e idoneita di modelli linguistici per uno specifico uso applicativo.";Campo="LLM locali o remoti, prompt di sistema, istruzioni, risposte strutturate, test di robustezza, allucinazioni e aderenza al compito.";Descrizione="Revisiona modelli linguistici su qualita, robustezza, prompt, formato, limiti e idoneita a un caso d'uso."},
    [pscustomobject]@{Codice="ARI-1701";Titolo="Revisione agenti IA";Categoria="Intelligenza artificiale";Livello="L4 Professionale";Offline="Sì";Skill="revisione-agenti-ia";Focus="agenti IA";Storia="revisione di agenti IA";Scopo="Valutare agenti IA rispetto a obiettivo, strumenti, memoria, limiti, autorizzazioni, tracciabilita e qualita del risultato.";Campo="Agenti locali, agenti Codex, flussi con strumenti, pianificatori, esecutori, sistemi multi-passaggio e assistenti specializzati.";Descrizione="Revisiona agenti IA valutando obiettivo, strumenti, autorizzazioni, memoria, limiti, tracciabilita e qualita operativa."},
    [pscustomobject]@{Codice="ARI-1702";Titolo="Progettazione memoria agente";Categoria="Intelligenza artificiale";Livello="L4 Professionale";Offline="Sì";Skill="progettazione-memoria-agente";Focus="memoria agente IA";Storia="progettazione memoria agente";Scopo="Progettare memoria per agenti IA distinguendo contesto temporaneo, preferenze, conoscenza stabile, log operativo e dati da non memorizzare.";Campo="Memoria locale, file di stato, profili utente, preferenze, base di conoscenza, riepiloghi conversazione e politiche di conservazione.";Descrizione="Progetta memoria per agenti IA separando contesto, preferenze, conoscenza stabile, log, esclusioni e regole di aggiornamento."},
    [pscustomobject]@{Codice="ARI-1703";Titolo="Valutazione strumenti agente";Categoria="Intelligenza artificiale";Livello="L4 Professionale";Offline="Sì";Skill="valutazione-strumenti-agente";Focus="strumenti agente IA";Storia="valutazione strumenti agente";Scopo="Valutare strumenti disponibili a un agente IA, definendo quando usarli, rischi, autorizzazioni, limiti e verifiche richieste.";Campo="Strumenti file, terminale, browser, API, generatori, validatori, automazioni locali e connettori esterni usati da agenti.";Descrizione="Valuta strumenti di agenti IA, autorizzazioni, rischi, limiti, casi d'uso e verifiche operative."},
    [pscustomobject]@{Codice="ARI-1704";Titolo="Orchestrazione multi-agente locale";Categoria="Intelligenza artificiale";Livello="L5 Audit";Offline="Sì";Skill="orchestrazione-multi-agente-locale";Focus="coordinamento multi-agente locale";Storia="orchestrazione multi-agente locale";Scopo="Coordinare piu agenti o macro-agenti locali definendo ruoli, confini, scambio evidenze, controllo conflitti e sintesi finale.";Campo="Lavori multi-agente locali, decomposizione compiti, revisione parallela, coordinamento tra analisi, codice, verifica, web e IA.";Descrizione="Coordina piu agenti locali definendo ruoli, confini, evidenze, conflitti e sintesi finale senza dispersione."},
    [pscustomobject]@{Codice="ARI-2201";Titolo="Revisione sicurezza web e app";Categoria="Sicurezza, licenze e privacy";Livello="L4 Professionale";Offline="Sì";Skill="revisione-sicurezza-web-app";Focus="sicurezza web e app";Storia="revisione sicurezza web e app";Scopo="Revisionare rischi di sicurezza in siti, applicazioni web e app locali, concentrandosi su input, segreti, autenticazione, permessi e dipendenze.";Campo="Web app, app locali, moduli, API client, configurazioni, dipendenze, gestione sessione, errori e superfici utente.";Descrizione="Revisiona sicurezza di siti, web app e app locali su input, segreti, autenticazione, permessi, errori e dipendenze."},
    [pscustomobject]@{Codice="ARI-2202";Titolo="Gestione segreti locali";Categoria="Sicurezza, licenze e privacy";Livello="L4 Professionale";Offline="Sì";Skill="gestione-segreti-locali";Focus="segreti locali";Storia="gestione segreti locali";Scopo="Individuare, proteggere e gestire segreti locali come token, password, chiavi API, file .env e configurazioni private.";Campo="File .env, configurazioni locali, script, documenti, log, backup, token API, credenziali e segreti usati da strumenti locali.";Descrizione="Individua e gestisce segreti locali come token, password, chiavi API, .env, log e backup senza esporli nei report."},
    [pscustomobject]@{Codice="ARI-2203";Titolo="Privacy e dati personali";Categoria="Sicurezza, licenze e privacy";Livello="L4 Professionale";Offline="Sì";Skill="privacy-dati-personali";Focus="privacy e dati personali";Storia="privacy e dati personali";Scopo="Valutare raccolta, uso, conservazione e minimizzazione di dati personali in progetti locali, siti, app e procedure.";Campo="Moduli, database, log, esportazioni, report, file utente, dati personali, dati sensibili e conservazione locale.";Descrizione="Valuta dati personali in progetti locali, moduli, log e app, controllando minimizzazione, conservazione, accessi e cancellazione."},
    [pscustomobject]@{Codice="ARI-2204";Titolo="Licenze risorse e dipendenze";Categoria="Sicurezza, licenze e privacy";Livello="L4 Professionale";Offline="Sì";Skill="licenze-risorse-dipendenze";Focus="licenze di risorse e dipendenze";Storia="licenze risorse e dipendenze";Scopo="Verificare licenze e vincoli di uso di risorse visive, font, icone, template, librerie e dipendenze software.";Campo="Risorse grafiche, font, icone, immagini, pacchetti software, template, librerie interfaccia e dipendenze di progetto.";Descrizione="Verifica licenze di risorse, font, icone, template, librerie e dipendenze rispetto all'uso previsto."},
    [pscustomobject]@{Codice="ARI-2501";Titolo="Automazione browser controllata";Categoria="Browser e test interfaccia";Livello="L3 Avanzato";Offline="No";Skill="automazione-browser-controllata";Focus="browser controllato";Storia="automazione browser controllata";Scopo="Automatizzare in modo controllato un browser per ispezionare pagine, compilare flussi, catturare schermate e verificare comportamento visibile.";Campo="Browser locale, siti, web app, flussi interfaccia, schermate, controlli manuali assistiti, navigazione e raccolta evidenze visuali.";Descrizione="Automatizza browser locali per controllare pagine, flussi, schermate e comportamento interfaccia con perimetro autorizzato."},
    [pscustomobject]@{Codice="ARI-2502";Titolo="Test end-to-end interfaccia";Categoria="Browser e test interfaccia";Livello="L4 Professionale";Offline="No";Skill="test-end-to-end-interfaccia";Focus="test end-to-end interfaccia";Storia="test end-to-end interfaccia";Scopo="Progettare o revisionare test end-to-end per flussi utente completi, collegando azioni, asserzioni, dati e rischi di regressione.";Campo="Test Playwright, Cypress o equivalenti, flussi login, moduli, navigazione, checkout, pannelli, stati errore e percorsi critici.";Descrizione="Progetta e revisiona test end-to-end per flussi UI completi con dati, asserzioni e rischi di regressione controllati."},
    [pscustomobject]@{Codice="ARI-2503";Titolo="Audit schermate adattive";Categoria="Browser e test interfaccia";Livello="L3 Avanzato";Offline="No";Skill="audit-schermate-adattive";Focus="schermate adattive";Storia="audit schermate adattive";Scopo="Verificare resa visuale di pagine e applicazioni su viewport mobile, tablet e desktop, individuando overflow, testo tagliato e layout incoerenti.";Campo="Schermate comparative, audit adattivi, pagine web, web app, pagine promozionali, moduli, pannelli e interfacce adattive.";Descrizione="Verifica schermate mobile, tablet e desktop per trovare overflow, testo tagliato, layout instabile e problemi visuali."}
)

foreach ($voce in $voci) {
    $cartella = Join-Path "Procedure" "$($voce.Codice)-$(Converti-Slug $voce.Titolo)"
    if ((Test-Path -LiteralPath $cartella) -and -not $Forza) {
        Write-Output "Salto esistente: $cartella"
        continue
    }
    New-Item -ItemType Directory -Force -Path $cartella | Out-Null
    Set-Content -LiteralPath (Join-Path $cartella "PROCEDURA.md") -Value (Nuova-Procedura $voce) -Encoding UTF8
    Set-Content -LiteralPath (Join-Path $cartella "SKILL.md") -Value (Nuova-Skill $voce) -Encoding UTF8
    Write-Output "Generata: $cartella"
}
