# 🎶 WhisperMate - Omvandla Tal till Text, Lokal Integritet genom Whisper AI-modellen!

[Hämta den senaste versionen från Mac App Store](https://apps.apple.com/pl/app/id6450404233).

![Skärmdump](images/appicon-128x128.png)

## Funktioner
WhisperMate gör det möjligt att konvertera ljud- och videofiler till text med hjälp av OpenAIs Whisper AI-modell. Du kan använda den inbyggda textredigeraren för att visa resultaten av konverteringen i respektive sektioner.
Hela konverteringsprocessen utförs lokalt på din enhet, vilket garanterar integriteten för dina data.

V5.5.1
---
- Var god korrigera eventuella fel i den automatiska översättningen efter att projektet är färdigt.
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.5.1/WhisperMate.dmg) 

V5.5.0
---
- Lades till alternativ för Deepgram nova-2-modellen.
- Lades till en dialogruta där användaren kan justera genomskinligheten för att hantera realtidsavskrivningen.
- Lades till ett alternativ för att endast visa resultatet av realtidsöversättningen.
- Lades till ett alternativ för att anpassa stilen (bakgrundsfärg, textfärg) i realtids-popupfönstret.
- Åtgärdade ett problem som ignorerade automatiseringsinställningarna vid användning av Deepgram-transkriptionsmodellen.
- Åtgärdade ett problem där realtidsavskriftsfönstret förblev öppet.
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.5.0/WhisperMate.dmg) 

V5.4.9
---
- Lägg till funktionen för satsvisa exportmallar för projekt, den kan exportera resultatet av de valda projekten i en fil från mallskriptet  
- Felkorrigeringar och prestandaförbättringar
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.9/WhisperMate.dmg) 
![image](/images/V549.webp)

V5.4.8
---
- Lägg till sekretessinställningar i huvudfönstrets bottenstatusfält, kan inaktivera händelseanalys och kraschrapport och lokal logg
- Lägg till skriptexempel för att ta bort rader som matchar villkor
- Lägg till skriptexempel för att ersätta undertexter som ser ut som '(Music) * Music * [Music]' med tom sträng
- Lägg till skript för att spara egenskaperna .memo, .markWarn och .warnMsg
- Lägg till alternativ för fördröjning av undertextvisning i förhandsgranskaren
- Lägg till verktyg för att massändra start- eller sluttid för undertexter i undertextredigeraren
- Lägg till (⇧)+←→-genväg i undertextredigeraren för att snabbt hoppa i förhandsgranskaren med 5 eller 30 sekunder
- Lägg till högtalarstyrningsfält och stöd för snabbinställning med genvägar
- Fixa problemet med att undertexter inte kan gömmas i förhandsgranskaren
- Fixa problemet med att mallredigeraren inte kan klippa text till urklipp och inte kan välja genom att dra
- Fixa formatet för tidsspannet .t0f5 .t0f4 .t0f2 i anpassade mallar, returnerar fortfarande 3 siffror i millisekunder.
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.8/WhisperMate.dmg) 

V5.4.7
---
- Lägg till automatisk start av projektalternativ när en fil läggs till i projektlistan (växla på huvudfönstrets statusfält längst ned)  
- Lägg till automatiseringssteg för automatisk export av filen till anpassad mapp  
- Lägg till automatiseringssteg för att skicka resultatet via e-post till din e-postkorg (det kan automatiskt använda det föregående automatiserade exportresultatet som bilaga)  
- Uppgradera mall- och JavaScript-redigeraren för att åtgärda kraschproblem
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.7/WhisperMate.dmg) 
![image](/images/V547.webp)

V5.4.6
---
- Lägg till layoutalternativ för förhandsgranskning av mediaundertext, källetranskriptet och översatt undertext kan kontrollera visningen upp eller ned.
- Lägg till stor v3 coreml-modell.
- Lägg till genväg ⌘+⌥+f eller dubbeltryck på förhandsgranskningen för att snabbt växla till helskärm.
- Vissa genvägar stödjer nu att trycka enstaka tecken för att aktiveras (slå samman, dela, finjustera).
- Efter sammanslagning av undertext är nu den första sammanslagna raden automatiskt markerad.
- Avbröt kopplingen av standardappen för att öppna whisper mate för ljud- och videofiler.
- Löst några kraschfel i V5.4.5.
- Löst problem med notifikationsvisning.
- Löst vissa översättningsproblem.
- [123 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.6/WhisperMate.zip) 

![image](/images/V546.webp)


V5.4.5
---
- ❗Universal Version kanske behöver laddas ner igen. Eftersom jag uppgraderade min utvecklingsenhet och glömde spara den allmänna distributions EDKey.
- Lägg till en automatisk funktion för att köra jobb när projektets transkription är klar (sammanslå upprepningar/snapshot/skript/översättning)
- Lägg till alternativ för maximal segmentlängd vid transkription
- Lägg till exempel på modellprompter
- Lägg till ersättning av med tecknet '\\n' (enkel snedstreck med tecken n) för att byta rad i ersättningsfunktionen
- Uppgradera gränssnittet för projekt tran​skriptionsalternativ
- [122 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.5/WhisperMate.zip)

![image](/images/V545.webp)

V5.4.4
---
- Lägg till modellmolnlista i modellkonfigurationspanelen med stöd för 2 nedladdningsvärd. (Byt till värd 2 om du inte kan ladda ner det från värd 1)  
- Stöd för att använda CoreML-modulen som fallback när GPU Accelerate-alternativet är inaktiverat i allmänna inställningar  
- Åtgärda problem med misslyckad nedladdning av stora modeller  
- Åtgärda kraschproblem på enheter utan Apple Silicon.
- [122 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip) 

V5.4.3
---
- Förbättra transkriberingshastighet  
- Lägg till stöd för Whisper Large V3-modellen  
- Lägg till stöd för LibreTranslator-motorn  
- Lägg till möjlighet att duplicera projekt i projektets kontextmeny  
- Uppdatera talarfältet så att det kan matas in direkt i redigeringsläget (⌘+E)  
- Åtgärda problem med flikfönster när antalet flikar är större än 2  
- Åtgärda problem med att vågformsvy ibland kraschar  
- Åtgärda problem med att översätta valda rader i undertextredigeraren

V5.4.2
---
- Lägg till alternativet att konfigurera antalet trådar för Whisper-processen. (Använd färre trådar för att låta datorn utföra andra uppgifter, men bearbetningstiden kommer att öka)  
- Lägg till stöd för Deepgram-transkriberingsmotor, stöd för realtidströms-transkribering.  
- Lägg till exempel på mall för att exportera anpassat talarinnehåll endast  
- Lägg till sökord som börjar med @ för att filtrera talarrader eller byta ut alla talarnamn till ett annat namn (ex: @tom --> jack)  
- Lägg till funktionen att spara den senaste projektets talarkonfiguration och återanvända den i nya projekt.  
- Anpassad mall för export har nu stöd för upp till 9 anpassade mallar.

V5.4.1
---
- Lägg till fjärrhanteringsfunktion för Intranätet, använd din telefon eller annan enhet för att lägga till filer att bearbeta och visa bearbetningstillstånd (i huvudfönstrets nedre statusfält)  
- Lägg till möjlighet att välja mall för konfigurering av AI-parametrar  
- Lägg till AI-parametern för att undertrycka skiljetecken  
- Lägg till JavaScript för att använda synkrona HTTP-förfrågningar för att hämta eller skicka data (Du kan använda det för att skicka undertextdata till din lokala LLM-tjänst för att få resultat för modifiering och sedan fylla tillbaka i den ursprungliga undertexten, eller skicka till andra HTTP/HTTPS-systemtjänster. Ladda det HTTP-exempel från JavaScript-processorn för att se hur det används.)
- Åtgärda fel vid bullerreduktion när filstigen innehåller mellanslagtecken

![image](/images/App-Preview-19.webp)

V5.4
---
- Lägg till snabbklippsfunktionen  
- Lägg till genväg (c) för att visa eller dölja förhandsvisningsplayern för undertextredigeraren  
- Lägg till genväg för att ändra hastigheten på förhandsvisningsplayern för undertextredigeraren  
- Ersätt tyst strategi med segmentstrategi  
- Åtgärda bugg i bullerreduceringsalternativet  
  
### Den nya snabbklippsfunktionen har följande funktioner:  
- Visualisera ljudvågformen för att exakt hitta och klippa videor.  
- Dela upp längre multimediainfiler i flera segment för separat bearbetning innan transkribering.  
- Använd segmentstrategin för att hoppa över tysta eller icke-transkriberbara segment.  
- Klipp separat de segment som kräver transkribering till individuella filer.

![image](/images/App-Preview-18.webp)

V5.3.1
---
- Lägg till projektets prioritetsegenskap i batchprocesskön, högre prioritet kommer att behandlas först (alternativet finns i snabbmenyn)
- Funktionen för att ersätta undertext även ersätta matchade sökord i översatt text
- Åtgärdade problem med omskrivning med hoppa över tyst strategi och minska brus strategy

V5.3
---
- Lägg till fler finjusterade modeller (små/medelstora) för olika språk.
- Lägg till transkriberingsstrategi för att hoppa över tysta segment (klassificerade efter decibelvärden och tystnadslängd).
- Lägg till alternativ för att minska bakgrundsbuller.
- Lägg till alternativ för att göra att transkribering undertrycker undertexter som visas i förväg (ingen spoiler).
- Lägg till exempel på en javascript-processor för att kapitalisera undertext för segment.


V5.2
---
- Lägg till finjusterade modeller för olika språklig återgivning. Kantonesiska/zh/koreanska/japanska/tyska/franska/thailändska/ukrainska...
- Lägg till funktion för att lägga till lokalt finjusterade Whisper AI-modeller i Whisper Mate.
- Lägg till funktion för att satsvis ställa in projektmodellparametrar.
- Lägg till alternativ för att förhindra att skärmsläckaren startar när det finns körfunktioner.
- Åtgärdat ett problem där bearbetningsuppgiften pausas när systemets skärmsläckare startas.
- Åtgärdat problemet med att klicka på raden i undertextredigeraren ibland inte navigerar till spelarens position.
- Åtgärdat problemet med att ångra och göra om ändrad text i undertextredigeraren inte kan göras via snabbmenyn.
- Åtgärdat ett problem med batchexport där tidfönsterkombination inte matchar.

V5.1
---
- Lägg till funktion för batch-export av projektsegment/srt/mall med möjlighet att kombinera till en fil  
- Lägg till funktion för att återtranskribera de valda raderna med olika AI-parametrar  
- Lägg till funktion för att ångra eller göra om textändringar i undertext med manuell typning (Genvägar ⌘+Z ångra / ⌘+⇧+Z gör om)  
- Lägg till funktion för att lägga till ny tom undertextrad under vald rad (Genväg ⌘+N)  
- Lägg till funktion för att skicka färdigprojektnotifikation via Slack incoming webhook. (Du kan få en varning på telefonen när varje projekt är transkriberat)  
- Åtgärdat problem med att mediaspelarkontrollrutan inte är centralt placerad i Up-Down-stilmall.

V5.0
---
- Lägg till kit för att snabbt slå samman undertexter i på varandra följande stycken
- Lägg till anpassat skriptbehandlingsverktyg för att justera undertexterna i batch
- Lägg till funktion för att justera undertexter i undertextredigeraren. Liknande funktioner för uppdelning och sammanslagning. Du kan markera flera rader samtidigt och justera dem i en enkeltextfält, rad för rad
- Lägg till förslag för skräddarsydda undertexter med fler genvägar
- Lägg till anpassad typsnittsinställning för undertextstil i videoförhandsgranskningspanelen
- Lägg till anpassad typsnittsinställning för att bränna in undertexten i originalvideon
- Lägg till export till pdf- eller docx-format, ange bara önskad filändelse (.pdf eller .docx)
- Lägg till fler fördefinierade formatexempel för export. Du kan ladda exempel och enkelt anpassa resultatet
- Lägg till funktion för att ta snapshots av aktuellt projekts undertexttillstånd. Enkelt återställa till sparade snapshots
- Lägg till funktionen att importera .srt som snapshots till det aktuella projektet
- Lägg till alternativ för att visa den översatta texten på förhandsvisningen av undertexterna över källtexten
- Lägg till anpassade exportfunktioner (slumpmässiga nummer, unika ID, escXML eller anpassad formatstring)
- Lägg till anpassad utmatningstyp (fil eller Urklipp)
- Lägg till anpassade exportalternativ för att använda alla undertexter eller enbart de markerade
- Gruppera projektredigerarfönstret med huvudfönstret
- Extra inställningar för whisper-modell i modellväljaren (i högra hörnet, längst ner), kanske inte så lätt att hitta eftersom de flesta fall inte behöver ändras
- Optimering av fullskärmsläge för fy-fönsters videoförhandsvisningar
- Sökordssökning med villkorsmatning (använd "|" som "eller" mellan sökord, ex. "hej|hello|hey")
- Optimering av sök- och ersättningslogik. När ersättning utförs visas ursprungs- och ersatta sökord för att underlätta anpassning
- Optimering av transkribering i realtid
- Åtgärdat problem med att vissa del- och delfönster inte hamnar i förgrunden
- Åtgärdat fel i xml-exportformat
- Åtgärdat problem med att extrahera wav från vissa medietyper
- Åtgärdat problem med automatisk ersättning när fältet för ersättning lämnas tomt
- Åtgärdat kraschproblem i projekten i streamläge


V4.0
---
- Lägg till funktion för att komma ihåg layoutegenskaper för undertextredigerare i projekten. Varje projekt kan ha olika layout och storlek på förhandsvisnngspelaren (gamla projekt måste öppnas igen för att minnas layoutegenskaperna)
- Lägg till alternativ för att hitta duplicerade undertexter i redigeraren
- Lägg till alternativ att öppna redigeraren även om transkriberingsverktyget inte har startats
- Lägg till exportmöjlighet för undertexter i .sbv-format
- Lägg till anpassade exportmallar (som .fcpxml, .itt, .ttml)
- Lägg till nytt tillägg
- Lägg till alternativ för snabbt åtkomst till använda sökord och ersättning
- Lägg till markering för att visa en flagga för markerade rader i förhandsvisningsprogressonen
- Lägg till alternativ för markerade rader i kontextmenyn för undertextredigeraren
- Lägg till funktion för att dela upp rader i undertextredigeraren vid enstaka valda rader
- Lägg till projektets namn i sökresultatet för att visa i vilket projekt sökningen gjorts
- Lägg till visning av felmeddelanden när det uppstår problem med bearbetad media
- Lägg till alternativ för att dölja knappen för radlokalisering i redigeraren
- Lägg till snabbtangent ⌘+S för snabb export av .srt till fil
- Åtgärdat problem då ljudspåret innehåller två ljudkanaler men bara en visas (lägg till alternativ att ignorera ljudkanalvalet)
- Åtgärdat problem vid bränning av undertexter när projektets namn har ändrats manuellt
- Åtgärdat problem med visning i ljusa teman

V3.5
---
- Lägg till funktion för att ladda ner ljudklipp för valda undertexter. Nu kan du välja valfria undertexter och använda kontextmenyn för att ladda ner ljudklippet. När flera rader väljs slås de ihop till ett ljudklipp
- Lägg till alternativ för att använda ett litet flytande fönsterläge för att fånga ljud i realtid
- Lägg till funktion för att snabbt starta inspelning av ljudström till projekt med nytt flytande fönster i menyraden
- Lägg till möjlighet att snabbt spela upp en segmentrad eller ladda ner ljudet för det sökresultat som hittats
- Lägg till stöd för att återuppta nedladdning av modeller vid avbrott
- Lägg till funktion för att lägga till kommentarer till projekts undertexter
- Aktivera alternativ för översättning med Azure
- Lägg till global undertextsökning i alla projekt
- Hög ljusstyrka på sökord i sökresultatet
- Lägg till standardgenvägar för snabbkontroll av fönster, som Stäng/Zooma/Minimera
- Lägg till alternativ för att dölja etiketterna i huvudverktygsfältet
- Flytta startknappen för batch-uppgifter från huvudverktygsfältet till en kontextmeny
- Åtgärdat problem med att ersättning inte fungerade med tom sträng
- Åtgärdat problem med otillgängliga små och small-en-modeller i backup-servrar
- Åtgärdat problem med undertexter nedsänkt vid uppspelningsreglage i inspelade ljudfiler

V3.0
---
- Lägg till möjlighet att exportera väljda undertexters tidsintervall till en ny klippfil
- Lägg till möjlighet att exportera video med inbrända undertexter till originalvideo och anpassad undertextstil
- Lägg till förhandsvisning av undertexter direkt i videoförhandsvisningen (undertextstil kan anpassas i inställningspanelen)
- Lägg till inspelning av mikrofonljud och stöd för transkribering i realtid (endast macOS13+)
- Lägg till funktion för att slå samman segment och undertexter till en rad
- Lägg till automatisk sparning av inspelat app-ljud till fil, kan konverteras till nytt transkriberingsprojekt
- Lägg till möjlighet att duplicera undertexter och justera innehåll eller tidsintervall för finjustering i hela undertexten
- Lägg till alternativ att öppna först inspelad undertext för redigering eller visning med hjälp av snabbkommando (⌘+E)
- Lägg till procentuell visning av CPU-användning vid whisper-bearbetning
- Lägg till alternativ att arkivera projekt med hjälp av kontextmenyn (Håll aktiva projektlistan ren)
- Lägg till Google Translate i undertextöversättningskontroll
- Stöd för fler app-språk
- Förhandsvisa media i full storlek tillsammans med undertextlayout
- Stöd för öppning av videofiler med hjälp av Finder's "öppna-med"-funktion
- Optimering av visning av större antal rader i undertextredigeraren
- Åtgärdat problem med att välja flera ljudkanaler i videoinspelning
- Åtgärdat problem med hopp i undertexter och videoregulator

V2.0
---
- Stöd för att fånga och transkribera ljud i andra appar som Zoom/Skype/Teams/mötesappar (endast macOS13.0+)
- Lägg till tillägg för att konvertera undertexter från förenklad kinesiska till traditionell kinesiska eller vice versa (Aktivera tillägg i inställningspanelen först)
- Åtgärdat problem med att mellanslagstangenten inte fungerar för att spela eller stoppa media i projektredigeraren
- Åtgärdat buggar med exportformaten SRT och VTT

V1.0
---
- Transkribera ljud- eller videofiler
- Använda DeepL:s gratis API för att översätta undertexter
- Inbäddad undertextredigerare för att fixa transkriptioner
- Exportera till SRT, VTT, CSV, JSON, SEGMENT-format
- Stöd för att tilldela talare till varje undertext
- De flesta åtgärder stöder batchurval, som batchkörning av uppgifter, batchöversättning av rader, batchjustering av talare
- Dra och släpp filer för att påbörja transkribering
- Möjlighet att söka i transkriptet
- Redigera kan förhandsvisa ljud- eller videofiler och synkronisera uppspelningsintervall
- Stöd för konvertering mellan flera språk
- Anpassa ofta använda språk för konvertering eller översättning

Funktioner

- Konvertera ljud- och videofiler till text
- Stöd för inspelning och omvandling av tal från inspelnings- och andra applikationer (Zoom / Skype / Teams / andra applikationer, kräver macOS version 13.0 eller senare)
- Gratis textöversättning med hjälp av DeepL-API:n
- Inbyggd verktyg för undertextredigering
- Export till SRT-, VTT-, CSV-, JSON-, SEGMENT-format
- Möjlighet att namnge valfri undertext
- Många funktioner stöder teamarbete. Till exempel kan uppgifter utföras som grupp eller översättningar kan översättas och tilldelas i bulk.
- Stöd för att dra och släppa filer för undertextkonvertering
- Visning av undertexter medan du skriver
- Förhandsvisning av ljud- eller videofiler i redigeraren
- Möjlighet att exportera valda undertexter som en ny mediefil
- Infoga undertexter i originalvideon med fördefinierad eller anpassad stil
- Direktvisning av undertexter i förhandsvisningsfönstret (inställningar för undertexter kan justeras i inställningarna)
- Realtidstexttransformering vid skapande av röstinspelningar (endast macOS 13 och senare)
- Stöd för att sammanfoga undertextsegment - slå samman segmenterade områden och undertext till en rad
- Programinspelningar sparas automatiskt och kan konverteras till nya konverteringsprojekt
- Kopiera undertextrader eller ändra bakgrundstiden
- Individuella uppspelningsinställningar för medievisning
- Stöd för snabbkommando Cmd + V för att klistra in filer i kön
- Visa CPU-användningsstatus under ljudredigering
- Stöd för att skapa en komprimerad fil i snabbmenyn (för att rensa aktiv projektlista)
- Stöd för att översätta text med Google Translate
- Fullskärmsvisning av undertexter i medievisningen
- Öppna mediaframvisningar i snabbmenyn
- Stöd för flerspråkig konvertering eller stöd för översättningar till populära språk


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