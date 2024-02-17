# README.md
- [Deutsch](README.de.md)
- [English](README.md)
- [Spanish](README.es.md)
- [Finnish](README.fi.md)
- [French](README.fr.md)
- [Italian](README.it.md)
- [Indonesian](README.id.md)
- [언어](README.ko.md)
- [日本語](README.ja.md)
- [简体中文](README.zh_cn.md)
- [繁体中文](README.zh_tw.md)
- [Norwegian](README.nb.md)
- [Dutch](README.nl.md)
- [Polish](README.pl.md)
- [Portuguese](README.pt_PT.md)
- [Swedish](README.sv.md)
- [ภาษาไทย](README.th.md)
- [Turkish](README.tr.md)
- [Ukrainian](README.uk.md)
- [Vietnamese](README.vi.md)

# 🎶 Whisper Mate - Trascrivi audio/film localmente su testo con il modello di IA di Whisper. Mantieni la privacy al sicuro!

Scarica [l'ultima versione dall'appstore di macOS](https://apps.apple.com/us/app/id6450404233)

![screenshot](images/appicon-128x128.png)

## Caratteristiche
Whisper Mate supporta la trascrizione batch di file audio o file video in testo con il modello di IA di Whisper di OpenAI. Con un editor di sottotitoli incorporato per visualizzare il risultato della trascrizione segmento per segmento.
Tutte le operazioni di trascrizione vengono eseguite nel computer locale. Mantieni la tua privacy al sicuro.

V5.5.1
---
- Risolto il crash nella traduzione automatizzata al termine del progetto
- [148 MB] (https://download.marksdo.com/apps/WhisperMate/V5.5.1/WhisperMate.dmg)

V5.5.0
---
- Aggiunta l'opzione del modello Deepgram nova-2
- Aggiunto il supporto alla finestra fluttuante di trascrizione in tempo reale per la personalizzazione del percentuale di trasparenza
- Aggiunta l'opzione di trascrizione in tempo reale per mostrare solo il contenuto tradotto
- Aggiunte opzioni di stile personalizzato per la finestra fluttuante in tempo reale (colore di sfondo, colore del carattere)
- Risolti i problemi con le opzioni di automazione che non vengono richiamate quando si utilizza l'engine di trascrizione di Deepgram
- Risolto il problema della chiusura intermittente della finestra fluttuante di trascrizione in tempo reale
- [148 MB] (https://download.marksdo.com/apps/WhisperMate/V5.5.0/WhisperMate.dmg)

V5.4.9
---
- Aggiunta la funzione di esportazione batch dei modelli di progetto, che consente di esportare i risultati dei progetti selezionati in un unico file a partire dallo script del modello
- Correzioni di bug e miglioramenti delle prestazioni
- [148 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.9/WhisperMate.dmg)
![image](/images/V549.webp)

V5.4.8
---
- Aggiunta delle impostazioni sulla privacy nella barra di stato inferiore della finestra principale, che possono disattivare l'analisi degli eventi, i rapporti sugli incidenti e il registro locale
- Aggiunto esempio di script per eliminare le righe che corrispondono alle condizioni
- Aggiunto esempio di script per sostituire la stringa del sottotitolo come '(Music) * Music * [Music]' con una stringa vuota
- Aggiunta della proprietà di scrittura .memo .markWarn .warnMsg
- Aggiunta dell'opzione di visualizzazione del ritardo nei sottotitoli del visualizzatore
- Aggiunta dell'opzione di modifica batch dell'ora di inizio o di fine del sottotitolo nel toolkit dell'editor dei sottotitoli
- Aggiunta della scorciatoia (⇧)+←→ nell'editor dei sottotitoli per saltare rapidamente 5 secondi o 30 secondi nel visualizzatore
- Aggiunta della barra di controllo degli altoparlanti e supporto per l'impostazione rapida con scorciatoie
- Risolto il problema della visualizzazione intermittente del sottotitolo nel visualizzatore
- Risolto il problema dell'editor del modello che non consente di tagliare il testo negli appunti e di selezionarlo trascinandolo
- Risolto il problema che nel formato dell'intervallo di tempo dell'esportazione del modello personalizzato .t0f5 .t0f4 .t0f2 restituisce comunque un numero formato da tre cifre in millisecondi
- [148 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.8/WhisperMate.dmg)

V5.4.7
---
- Aggiunta dell'opzione di avvio automatico del progetto quando viene aggiunto un file all'elenco dei progetti (l'interruttore si trova nella barra di stato inferiore della finestra principale)
- Aggiunta della fase automatizzata di esportazione automatica del file nella cartella personalizzata
- Aggiunta della fase automatizzata di invio del risultato al tuo indirizzo email (può utilizzare automaticamente il risultato dell'esportazione automatica precedente come allegato)
- Aggiornato l'editor del modello e del javascript per risolvere i problemi di crash
- [148 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.7/WhisperMate.dmg)
![image](/images/V547.webp)

V5.4.6
---
- Aggiunta dell'opzione di layout del sottotitolo nell'anteprima multimediale, il sottotitolo trascritto e il sottotitolo tradotto possono controllare la visualizzazione nella parte superiore o inferiore.
- Aggiunto il modello CoreML v3 large
- Aggiunta della scorciatoia ⌘+⌥+f o doppio tocco nell'anteprima per passare rapidamente alla modalità a schermo intero
- Ora alcune scorciatoie supportano la pressione di un solo carattere (unione, divisione, accordatura)
- Dopo la fusione del sottotitolo, viene selezionata automaticamente la prima riga di fusione
- Rimossa l'associazione predefinita dell'app aperta con Whisper Mate per i file audio e video
- Risolti alcuni bug di crash in V5.4.5
- Risolto il problema di visualizzazione delle notifiche
- Risolti alcuni problemi di traduzione
- [123 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.6/WhisperMate.zip)

![image](/images/V546.webp)

V5.4.5
---
- ❗ Potrebbe essere necessario scaricare nuovamente la versione universale. Ho aggiornato il mio dispositivo di sviluppo e ho dimenticato di salvare la chiave di distribuzione universale EDKey.
- Aggiunta della funzione di automazione per eseguire operazioni quando la trascrizione del progetto è terminata (Unisci ripetizioni/Snapshot/Script/Traduci)
- Aggiunta dell'opzione di lunghezza massima del segmento di trascrizione
- Aggiunta di esempi di prompt del modello.
- Aggiunta della sostituzione con il carattere '\\n' (barra rovesciata singola con carattere n) per passare a una nuova riga nella funzione di sostituzione
- Aggiornata l'interfaccia di configurazione delle opzioni di trascrizione del progetto.
- [122 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.5/WhisperMate.zip)

![image](/images/V545.webp)

V5.4.4
---
- Aggiunta dell'elenco dei modelli cloud nel pannello di configurazione del modello con il supporto di 2 host di download. (Passare a host2 se non è possibile scaricarlo in host1)
- Supporto di riserva dell'utilizzo del modulo CoreML quando l'opzione di accelerazione GPU è disabilitata nelle impostazioni generali
- Risolto il problema di download del modello grande che falliva
- Risolto il problema di crash su dispositivi che non sono a chip Apple.
- Scarica la versione universale [122 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip)

V5.4.3
---
- Miglioramento della velocità di trascrizione
- Aggiunto il supporto al grande modello v3 di Whisper
- Aggiunto il supporto al motore di traduzione di LibreTranslator
- Aggiunta dell'opzione di progetto duplicato nel menu contestuale del progetto
- Aggiornato il campo degli altoparlanti che può essere inserito direttamente in modalità di modifica (⌘+E)
- Corretto il problema della finestra a schede quando il numero di schede > 2
- Risolto il problema dell'anteprima dell'onda sonora a volte si blocca
- Risolto il problema della traduzione nell'editor dei sottotitoli che non riesce a tradurre le righe selezionate


V5.4.2
---
- Aggiunta dell'opzione di numero di threads di elaborazione di Whisper. (Usando meno threads lascia al computer il compito di svolgere altre attività, ma il tempo di elaborazione aumenterà)
- Aggiunto il supporto del motore di trascrizione di Deepgram, supporto anche in modalità di trascrizione in streaming in tempo reale.
- Aggiunto esempio dello script per esportare solo il contenuto dell'altoparlante personalizzato
- Aggiunta della parola chiave di ricerca che inizia con @ per filtrare le righe dell'altoparlante o sostituire tutti i nomi dell'altoparlante con un altro nome (es: @tom-->jack)
- Aggiunta della funzione per salvare la configurazione degli altoparlanti del progetto più recente e riutilizzarla in un nuovo progetto.
- L'esportazione tramite modello personalizzato ora supporta 9 modelli personalizzati.

V5.4.1
---
- Aggiunta della funzionalità di gestione remota web intranet, utilizza il tuo telefono o un altro dispositivo per aggiungere file da elaborare e visualizzare lo stato di elaborazione (nella barra di stato inferiore della finestra principale)
- Aggiunta del selettore di modelli di configurazione dei parametri di intelligenza artificiale.
- Aggiunta del parametro AI di soppressione della punteggiatura
- Aggiunta di uno script per utilizzare richieste HTTP sincrone per ottenere o inviare dati (puoi usarlo per inviare i dati delle righe di sottotitoli al tuo servizio llm locale per ottenere un risultato di correzione inferenziale e inserirlo nuovamente nel sottotitolo originale, o per inviare a un altro servizio di sistema HTTP/HTTPS, carica l'esempio HTTP dal processore in JavaScript per vedere come usarlo)
- Risolto l'errore nel denoise wav quando il percorso del file contiene spazi


V5.4
---
- Aggiunta della funzione di taglio rapido
- Aggiunta della scorciatoia (c) per mostrare o nascondere l'editor di sottotitoli in anteprima
- Aggiunta della scorciatoia per cambiare la velocità dell'editor di anteprima del lettore di sottotitoli
- Sostituita la strategia del silenzio con la strategia dei segmenti
- Risolto il bug dell'opzione di denoise
- Download della versione universale [122 MB] (https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip)

### La nuova funzione di taglio rapido ha le seguenti funzionalità:

- Visualizza l'onda sonora dell'audio per individuare e tagliare con precisione i video.
- Suddividi file multimediali più lunghi in segmenti separati per un'elaborazione separata prima della trascrizione.
- Utilizza la strategia dei segmenti per saltare segmenti silenziosi o non trascrivibili.
- Taglia separatamente i segmenti che richiedono la trascrizione in file individuali.


V5.3.1
---
- Aggiunta dell'attributo di priorità di progetto nella coda di elaborazione batch, le priorità più alte verranno elaborate per prime (l'opzione si trova nel menu contestuale)
- La funzione di sostituzione del testo dei sottotitoli sostituisce anche le parole chiave corrispondenti nel testo tradotto
- Risolti i problemi di re-trascrizione con la strategia di skip silent e di riduzione del rumore


V5.3
---
- Aggiunta di modelli accordati (piccolo/medio) per le lingue
- Aggiunta della strategia di trascrizione per saltare il segmento silenzioso (classificato per decibel e durata silenziosa)
- Aggiunta dell'opzione per ridurre il rumore di fondo.
- Aggiunta dell'opzione per far sì che la trascrizione sopprima la visualizzazione dei sottotitoli in anticipo rispetto al timestamp (no spoiler).
- Aggiunto esempio di script JavaScript per rendere maiuscoli i sottotitoli dei segmenti


V5.2
---
- Aggiunta di modelli migliorati per l'inferenza in lingue diverse. Cantonese/zh/ko/jp/de/fr/th/uk...
- Aggiunta della funzione per aggiungere un modello di intelligenza artificiale di Whisper sintonizzato localmente in Whisper Mate.
- Aggiunta della funzione per impostare i parametri del modello del progetto in batch
- Aggiunta dell'opzione per impedire l'avvio dello screensaver quando c'è una coda in esecuzione.
- Risolto il problema del blocco del processo di elaborazione quando viene avviato lo screensaver del sistema.
- Risolto il problema del clic sulla riga dell'editor dei sottotitoli che a volte non riesce a passare alla posizione del lettore


V5.1
---
- Aggiunta della funzione di esportazione batch dei segmenti/srt/template dei progetti con opzione di combinazione in un unico file
- Aggiunta della funzione di re-trascrizione delle righe selezionate con parametri AI differenti
- Aggiunta della funzione di annullamento o ripetizione delle modifiche testuali nel contenuto dei sottotitoli con modifiche manuali (Scorciatoie ⌘+Z annulla /  ⌘+⇧+Z ripeti)
- Aggiunta della funzione di aggiunta di una nuova riga di sottotitoli vuota sotto la riga selezionata (Scorciatoie ⌘+N)
- Aggiunta della funzione di inviare la notifica di completamento del progetto tramite il webhook in arrivo di Slack. (È possibile ricevere una notifica sul telefono quando ogni progetto termina la trascrizione)
- Risolto il problema della posizione della casella di controllo della riproduzione multimediale quando si utilizza il layout stile su/giù


V5.0
---
- Aggiunta del kit per unire automaticamente i sottotitoli in paragrafi consecutivi
- Aggiunto processore di script personalizzato per accordare automaticamente i sottotitoli trascritti
- Aggiunta della funzione di accordatura dell'editor di sottotitoli. È simile alla funzione di divisione e unione. Può selezionare più righe e accordarle in una sola riga di testo
- Aggiunto l'editor di sottotitoli con il supporto di più scorciatoie
- Aggiunta del carattere personalizzato per lo stile dei sottotitoli dell'anteprima video nel pannello di configurazione
- Aggiunta del carattere personalizzato per la sovrapposizione dei sottotitoli duri al video originale nel pannello di configurazione
- Aggiunto il supporto per l'esportazione in pdf o docx, impostare semplicemente il suffisso di esportazione su pdf o docx
- Aggiunto un formato di esportazione di esempio predefinito. È possibile caricare l'esempio e apportare semplici modifiche al risultato del modello di base.
- Aggiunta della funzione di fare snapshot dello stato corrente dei sottotitoli del progetto. Successivamente, è possibile recuperarlo facilmente dai snapshot salvati.
- Aggiunta della funzione di importare .srt nel progetto corrente come snapshot.
- Aggiunta dell'opzione per impostare la visualizzazione del testo tradotto sopra il testo originale nel sottotitolo del video
- Aggiunte funzioni di esportazione personalizzate. numeri casuali e GUID casuali e escXML e replaceString con formato personalizzato
- Aggiunta dell'opzione di tipo di output di esportazione personalizzato (file o clipboard)
- Aggiunta dell'opzione di esportazione di tutti i sottotitoli o solo quelli selezionati
- Aggiunta dell'opzione finestra principale del gruppo dell'editor del progetto
- Aggiunti parametri di processo del modello Whisper aggiuntivi nella selezione del modello (nell'angolo in basso a destra), potrebbe non essere facile trovarli. Perché nella maggior parte dei casi non è necessario modificare questi parametri.
- Ottimizzazione dei comportamenti di anteprima video a schermo intero
- La ricerca delle parole chiave supporta la condizione (utilizzare | come parola chiave alternativa. esempi "hi|hello|hey")
- Ottimizzazione della logica di ricerca e sostituzione. Quando si esegue la sostituzione delle parole chiave, la ricerca mostra le parole chiave e le parole sostituite
- Ottimizzazione della logica di trascrizione in streaming in tempo reale
- Risolti alcuni problemi di finestra secondaria che non vengono portati in primo piano
- Risolti alcuni bug dell'esportazione in formato xml
- Risolti alcuni problemi nell'estrazione dei file audio wave
- Risolti alcuni problemi di lasciare il campo della parola chiave di sostituzione che attiva automaticamente l'azione di sostituzione
- Risolti alcuni problemi del progetto in streaming

V4.0
---
- Aggiunta della funzione di memorizzare le proprietà del layout dell'editor dei sottotitoli del progetto. Ogni progetto può utilizzare un layout e una dimensione del lettore di anteprima diversi. (I vecchi progetti devono essere aperti nuovamente per ricordare le proprietà del layout)
- Aggiunta dell'opzione per trovare sottotitoli duplicati nell'editor
- Aggiunta dell'opzione nel menu contestuale per aprire l'editor anche se lo script di trascrizione del progetto non è stato avviato.
- Aggiunta dell'esportazione dei sottotitoli in formato .sbv
- Aggiunta delle funzioni dei modelli di esportazione personalizzati (come .fcpxml, .itt, .ttml)
- Aggiunto nuovo plugin
- Aggiunta delle parole chiave frequentemente utilizzate e delle opzioni di configurazione di sostituzione per un rapido riutilizzo di ricerca o sostituzione
- Aggiunta della visualizzazione di una bandiera Marcatore nella vista di avanzamento del lettore
- Aggiunta dell'opzione di marcare nel menu contestuale dell'editor dei sottotitoli
- Aggiunta della funzione di divisione della riga nell'editor dei sottotitoli quando si seleziona una singola riga
- Aggiunta della visualizzazione del nome del progetto nei risultati di ricerca
- Aggiunge la visualizzazione di un errore quando l'estrazione multimediale incontra un errore di preelaborazione
- Aggiunta dell'opzione per nascondere il pulsante di posizionamento della riga dell'editor
- Aggiunta della scorciatoia ⌘+S per esportare rapidamente .srt su file
- Risolto il problema delle informazioni sull'audio del canale multimediale che riceve due canali audio ma in realtà uno solo. (aggiunto l'opzione di ignorare la selezione del canale audio)
- Risolto il problema della sovrapposizione dei sottotitoli quando il nome del progetto è stato modificato manualmente
- Risolti alcuni problemi di interfaccia utente su macOS12
- Risolti alcuni problemi di visualizzazione dell'interfaccia utente dei temi chiari

## Funzionalità

- Trascrivi file audio o video
- Supporta la cattura e la trascrizione audio in altre app come (Zoom/Skype/Teams/Altre app, solo macOS13.0+ e richiede l'autorizzazione alla registrazione dello schermo)
- Utilizza la traduzione gratuita di DeepL API per i sottotitoli
- Incorpora l'editor di sottotitoli per correggere la trascrizione
- Esporta in formato SRT, VTT, CSV, JSON, SEGMENT
- Supporto per impostare l'altoparlante per ogni sottotitolo
- La maggior parte delle operazioni supporta la selezione batch per l'invocazione. Come esecuzione di attività batch, traduzione batch di righe, impostazione batch dell'altoparlante delle righe
- Supporto per il trascinamento dei file per avviare la trascrizione
- Supporto per la digitazione nella ricerca della trascrizione
- L'editor può visualizzare l'audio o il video sync con l'intervallo di riproduzione
- Esporta l'intervallo multimediale dei sottotitoli selezionati in un nuovo file di clip multimediale
- Esporta il video con i sottotitoli duri sovrapposti al video originale e con uno stile di sottotitolo personalizzato
- Anteprima diretta dei sottotitoli all'interno dell'anteprima video (lo stile dei sottotitoli può essere personalizzato nel pannello delle preferenze)
- Registra l'audio del microfono e supporta la trascrizione in tempo reale (macOS13+)
- Unisci sottotitoli. L'intervallo dei segmenti e il sottotitolo verranno uniti in una sola riga
- L'audio registrato verrà salvato automaticamente su file e può essere trasformato in un nuovo progetto di trascrizione.
- Duplica la riga del sottotitolo e consente di modificarne il contenuto o l'intervallo temporale per ottimizzare i sottotitoli completi
- Supporto per la riproduzione multimediale con velocità di riproduzione personalizzata
- Mostra la percentuale di utilizzo della CPU durante l'elaborazione Whisper
- Supporto per archiviare i progetti tramite il menu contestuale (mantenere pulito l'elenco dei progetti di lavoro)
- Supporto per la traduzione di Google nei controlli di traduzione dei sottotitoli
- Anteprima multimediale a dimensioni reali con layout dei sottotitoli
- Supporta l'apertura di file multimediali all'interno delle opzioni "Apri con" di Finder
- Supporto per la conversione multilingue
- Supporta la lingua di conversione personalizzata più frequentemente utilizzata per la conversione o la traduzione

## Immagini  

![screenshot](images/App-Preview-1.webp)  

![screenshot1](images/App-Preview-2.webp)  

![screenshot2](images/App-Preview-3.webp)  

![screenshot3](images/App-Preview-4.webp)  

![screenshot4](images/App-Preview-5.webp)  

![screenshot5](images/App-Preview-6.webp)  

![screenshot6](images/App-Preview-7.webp)  

![screenshot7](images/App-Preview-8.webp)  

![screenshot8](images/App-Preview-9.webp)  

![screenshot10](images/App-Preview-10.webp)  

![screenshot11](images/App-Preview-11.webp)  

![screenshot12](images/App-Preview-12.webp)  

![screenshot13](images/App-Preview-13.webp)  

![screenshot14](images/App-Preview-14.webp)  

![screenshot15](images/App-Preview-15.webp)  

![screenshot16](images/App-Preview-16.webp)