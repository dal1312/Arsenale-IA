# Contratto multi-agente prima della prova
Worker A: calcolare somma, leggere solo worker-a/input.json, creare solo worker-a/output.json.
Worker B: calcolare minimo e massimo, leggere solo worker-b/input.json, creare solo worker-b/output.json.
Formato JSON, campi ruolo e risultati interi. Fermarsi dopo output e risposta finale; niente altri agenti, rete, Git, installazioni o file esterni.
Coordinatore: verificare proprietà, input invariati, identità distinte, artefatti e sintesi somma=21, minimo=3, massimo=11.
Rischio P2: sandbox condivisa, confini contrattuali non isolamento OS. Verificare file preesistenti tramite baseline; non dichiarare inferenza offline.
