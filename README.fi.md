# 🎶 Whisper Mate - Äänitallenteiden/elokuvien erämuuntaminen tekstimuotoon paikallisesti käyttäen Whisper-IA-mallia. Suojaat yksityisyyttäsi!

Lataa [uusin versio macOS App Storesta](https://apps.apple.com/fi/app/id6450404233).

![Screenshots](images/appicon-128x128.png)

## Ominaisuudet
Whisper Mate mahdollistaa äänitiedostojen tai elokuvien erämuuntamisen tekstiksi käyttäen OpenAI:n Whisper-IA-mallia. Sisäänrakennetun tekstityksen editorin avulla voit tarkastella muunnoksen tuloksia osioittain.
Kaikki muunnosprosessit tapahtuvat paikallisella laitteella, joten yksityisyytesi on turvattu.

V5.5.1
---
- Virheenkorjaus automaattisessa käännöksessä, kun projekti on valmis.
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.5.1/WhisperMate.dmg) 

V5.5.0
---
- Lisää vaihtoehto Deepgram nova-2 -mallille
- Lisää tuki reaaliaikaiselle transkriptiolle kelluvassa ikkunassa, jossa on mukautettava läpinäkyvyysarvo
- Lisää vaihtoehto näyttää vain käännetty sisältö reaaliaikaisessa transkriptiossa
- Lisää mukautetun tyylinkorjausvaihtoehdot kelluvalle ikkunalle reaaliajassa (taustaväri, fonttiväri)
- Korjaa ongelma, jossa automaatioasetukset eivät kutsuta, kun käytetään Deepgramin transkriptiomallia
- Korjaa ongelma, jossa reaaliaikainen transkriptioikkuna ei joskus sulkeudu
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.5.0/WhisperMate.dmg) 

V5.4.9
---
- Lisää projektit mallipohjaisen erävientiominaisuuden, joka voi viedä valittujen projektien tuloksen yhdeksi tiedostoksi malliskriptiltä
- Virhekorjauksia ja suorituskyvyn parannuksia
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.9/WhisperMate.dmg) 
![image](/images/V549.webp)

V5.4.8
---
- Lisää yksityisyysasetukset pääikkunan alareunan tilapalkkiin, se voi poistaa tapahtuman analytiikan, kaatumisraportin ja paikallisen lokin.
- Lisää skriptiesimerkki, jolla voi poistaa ehtoa vastaavat rivit.
- Lisää skriptiesimerkki, jolla voi korvata tekstitysten merkkijonon kuten "(Music) * Music * [Music]" tyhjällä merkkijonolla.
- Lisää skriptiin takaisinkirjoitusominaisuus .memo .markWarn .warnMsg.
- Lisää esikatseluasetus tekstitysten viivästymisen näyttövaihtoehtoon.
- Lisää satsimuokkaus tekstitysten alkamis- tai loppumisaikaa tekstitysten muokkaustyökaluun.
- Lisää (⇧)+←→ pikanäppäinyhdistelmä tekstitysten muokkaustyökaluun, jolla voi siirtyä esikatseluun 5 sekunnin tai 30 sekunnin hyppäyksellä.
- Lisää kaiutinten hallintapalkki ja tuki pikasettiin pikanäppäimillä.
- Korjattu ongelma, jossa esikatselun tekstitykset eivät voinut piiloutua.
- Korjattu ongelma, jossa mallin muokkaustyökalu ei voinut leikata tekstiä leikepöydälle tai valita sitä raahaamalla.
- Korjattu ongelma, jossa mukautetun mallin .t0f5 .t0f4 .t0f2 aikavälin muotoilu palautti edelleen 3-numeroisen millisekunnin.
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.8/WhisperMate.dmg) 

V5.4.7
---
- Lisää automaattinen käynnistysprojektin vaihtoehto, kun tiedosto lisätään projektiluetteloon (kytkin on pääikkunan alaosan tilapalkissa)
- Lisää automaatioaskel, jolla voi automaattisesti viedä tiedoston mukautettuun kansioon
- Lisää automaatioaskel, jolla voi lähettää tuloksen sähköpostitse omaan postilaatikkoosi (se voi automaattisesti käyttää edellisen automaattisen viennin tulosta liitteenä)
- Päivitä mallin ja JavaScript-ohjelmiston editori korjaamaan kaatumisongelmat
- [148 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.7/WhisperMate.dmg) 
![image](/images/V547.webp)

V5.4.6
---
- Lisää mediasisällön esikatselu tekstityksen asetusten vaihtoehto, lähdekirjoituksen ja käännetyn tekstityksen avulla voi säätää näytön ylös- tai alaspäin.
- Lisää suuri v3 coreml-malli.
- Lisää pikakuvake ⌘+⌥+f tai kaksoisnapauta esikatselua siirtyäksesi nopeasti kokoruututilaan.
- Joitain pikanäppäimiä tukee nyt merkin painaminen yhdistämisen (merge), jakamisen (split) ja hienosäädön (tune) käynnistämiseksi.
- Yhdistämisen jälkeen tekstitys valitsee automaattisesti ensimmäisen yhdistyksen rivin.
- Peruttu oletusarvoinen sovelluksen sitominen kuiskausparin kanssa ääni- ja videotiedostoille.
- Korjattu muutamia kaatumisvirheitä V5.4.5:ssä.
- Korjattu ilmoituksen näyttöongelma.
- Korjattu muutamia käännösongelmia.
- [123 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.6/WhisperMate.zip) 

![image](/images/V546.webp)


V5.4.5
---
- ❗️ Yleinen versio saattaa vaatia uudelleen lataamisen. Koska päivitin kehityslaitteeni ja unohdin tallentaa yleisen käyttöönoton EDKey-koodin.
- Lisää automaatiotoiminto suorittaaksesi tehtäviä projektin transkriptio valmistuttua (toistojen yhdistäminen/tallentaminen/koodi/käännös)
- Lisää vaihtoehto enimmäissegmentin pituudelle transkriptiossa
- Lisää mallipromptin esimerkkejä
- Lisää vaihtoehto korvata merkki '\n' (yksittäinen kenoviiva ja n) uudella rivinvaihdolla korvausominaisuudessa
- Päivitä projekti transkriptio -asetusten konfigurointikäyttöliittymä.
- [122 Mt](https://download.marksdo.com/apps/WhisperMate/V5.4.5/WhisperMate.zip)

![image](/images/V545.webp)

V5.4.4
---
- Lisää mallin pilviluettelo mallin määrityspaneeliin, jossa on 2 latausisännän tuki. (Vaihda isäntä2:een, jos et saa sitä ladattua isännässä1)  
- Varmistustuen käyttö CoreML-moduulille, kun GPU-kiihdytysasetus on poistettu käytöstä yleisissä asetuksissa  
- Korjattu suuren mallin latausvirhe  
- Korjattu kaatumisongelma ei-Apple Silicon -laitteella.
- [122 MB](https://download.marksdo.com/apps/WhisperMate/V5.4.4/WhisperMate.zip) 

V5.4.3
---
- Paranna purkunopeutta
- Lisää tuki Whisper large v3 -mallille
- Lisää tuki LibreTranslator-moottorille
- Lisää "kopioi projekti" -valinta projektin pikavalikkoon
- Päivitä puhujakenttään suoran syötön mahdollisuus muokkaustilassa (⌘+E)
- Korjaa välilehti-ikkunan ongelma, kun välilehtien määrä > 2
- Korjaa aalto muodonäkymän satunnainen kaatumisongelma
- Korjaa tekstinkäännös tekstitysmuokkaimessa, jossa valittua riviä ei voi kääntää

V5.4.2
---
- Lisätään asetukset kuiskausten käsittelylangan lukumäärän valinta. (Käytä vähemmän lankoja, jotta tietokone voi tehdä muita tehtäviä, mutta käsittelyaika kasvaa)
- Lisätään tuki deepgram-kirjoituskoneelle, myös reaaliaikainen suoratoisto-tallennustila tuetaan.
- Lisätään malliesimerkki mukautetun puhujan sisällön vientiä varten.
- Lisätään hakutulos, joka alkaa @-merkillä, jotta voi suodattaa puhujarivejä tai vaihtaa kaikki puhujan nimet toiseen nimeen (esim. @tom-> jack).
- Lisätään ominaisuus viimeisimpien projektin puhujien asetusten tallentamiseen ja uudelleenkäytön uudessa projektissa.
- Mukautetun mallin vienti tukee nyt 9 mukautettua mallia.

V5.4.1
---
- Lisää intranetin verkkoratkaisemisen etäiskäsittelytoiminto, voit käyttää puhelinta tai muita laitteita tiedostojen lisäämiseen ja käsittelytilojen tarkastelemiseen (pääikkunan alaikkunan tilapalkissa).
- Lisää tekoälyn parametrien määritysmallin valitsin.
- Lisää vaimenna välimerkit -tekoälyparametri.
- Lisää JavaScript-koodi, jotta voit käyttää synkronista HTTP-pyyntöä tietojen hakemiseen tai lähettämiseen (voit käyttää sitä tekstitysrivin tietojen lähettämiseen paikalliseen llm-palveluun, jotta voit saada korjauksen ja täyttää sen alkuperäiseen tekstitykseen tai lähettämiseen muuhun HTTP/HTTPS-järjestelmäpalveluun. Nähdäksesi miten sitä käytetään, lataa esimerkki JavaScript-prosessorilta.)
- Korjaa kohinanvaimennus WAV-virhe, kun tiedostopolussa on välilyönneissä.

![image](/images/App-Preview-19.webp)

V5.4
---
- Lisää nopea leikkaustoiminto.
- Lisää pikanäppäin (c) tekstityksen muokkausnäytön esikatselunäytön näyttämiseen tai piilottamiseen.
- Lisää pikanäppäin tekstityksen muokkausnäytön esikatselunopeuden vaihtamiseen.
- Korvaa hiljaisuusstrategia lohkotstrategialla.
- Korjattu kohinanvaimennusvalinnan virhe.

### Uusi Quick Cut -toiminto sisältää seuraavat ominaisuudet:
- Näytä ääniaaltomuoto tarkkaan videoiden paikantamiseen ja leikkaamiseen.
- Jaa pidemmät multimediatiedostot useiksi segmenteiksi erillistä käsittelyä ennen tekstitystä varten.
- Käytä lohkotstrategiaa hiljaisten tai ei-transkriboitavien segmenttien ohittamiseen.
- Leikkaa erikseen ne segmentit, jotka vaativat tekstitystä erillisiksi tiedostoiksi.

![image](/images/App-Preview-18.webp)

V5.3.1
---
- Lisää projektille prioriteettiominaisuus eränkäsittelyjonossa, korkeampi prioriteetti käsitellään ensin (Vaihtoehto on kontekstivalikossa)
- Tekstityksen tekstin korvausominaisuus korvaa myös vastaavan avainsanan käännetyn tekstin
- Korjattu uudelleentranskriptio, jossa ohitetaan hiljaisten jaksojen strategia ja vähennetään meluongelmia

V5.3
---
- Lisää enemmän hyvin viritettyjä malleja (pieniä/keskikokoisia) kielille.
- Lisää transkribointistrategia äänettömien segmenttien ohittamiseksi (luokitellaan desibeleiden ja äänettömän keston perusteella).
- Lisää vaihtoehto taustamelun vähentämiseksi.
- Lisää vaihtoehto, joka mahdollistaa transkriboinnin estämisen tekstityksen näyttämisestä aikaleimojen edellä (ei spoilereita).
- Lisää esimerkkikoodi JavaScript-prosessoriin, joka muuttaa segmentin tekstityksen isoiksi kirjaimiksi.

V5.2
---
- Lisää hienosäädettyjä malleja eri kielten päättelyyn. kantoninkiina/kiina/korea/japani/saksa/ranska/thaimaa/ukraina...
- Lisää ominaisuus lisätä paikallisesti hienosäädetty Whisper AI -malli Whisper Mateen.
- Lisää ominaisuus erän määrittämiseksi projektimallin parametreille.
- Lisää vaihtoehto estää ruudun säästäjän käynnistyminen, kun jonossa on käynnissä olevia tehtäviä.
- Korjattu ongelma, jossa kun järjestelmän ruudun säästäjä käynnistyi, käsittelytehtävä pysähtyi.
- Korjattu tekstityksen muokkausrivin napsautus, joka toisinaan ei voinut siirtyä soitinpaikkaan.
- Korjattu tekstityksen muokkausrivin muokatun tekstin peruuta ja tee uudelleen -komentoa ei voitu kutsua kontekstivalikosta.
- Korjattu erän vienti, kun aikavälit eivät vastanneet toisiaan.


V5.1
---
- Lisää toiminto eri projektin osien/srt-pohjien/tiedostomallien eräkuvausten vientiin yhdistäen ne yhdeksi tiedostoksi.
- Lisää toiminto valittujen rivi(en) uudelleen transkriptioon eri tekoälyparametrein.
- Lisää toiminto tekstimuutosten peruuttamiseen tai tekstin sisällön manuaalisen kirjoituksen peruuttamiseen tekstitysikkunan tekstisisällössä (Pikanäppäin ⌘+Z peruutto / ⌘+⇧+Z tekeminen uudelleen).
- Lisää toiminto uuden tyhjän tekstirivin lisäämiseksi valitun rivin alapuolelle (Pikanäppäin ⌘+N).
- Lisää toiminto projektin valmistumisesta ilmoittamiseksi Slackin sisääntulevalla webhookilla (Saat ilmoituksen puhelimeesi, kun projektin transkriptio on valmis).
- Korjattu mediasoitinkontrollin laatikon sijainti keskelle, kun käytetään ylös-alas -tyylimuotoilua.
  
V5.0  
---  
- Lisää työkalut nopeaan tekstityksen yhdistämiseen peräkkäisissä kappaleissa  
- Lisää mukautettu jatkojalostusprosessori käännetyille tekstityksille  
- Lisää tekstityksen muokkaustoiminto. Se on samankaltainen jako- ja yhdistämisominaisuuden kanssa. Voit valita useita rivejä ja muokata niitä yhdessä tekstikentässä rivi kerrallaan  
- Lisää tekstityksen muokkaaja, jossa on enemmän pikanäppäinten tukea.  
- Lisää mukautettu fontti videon esikatselun tekstitystyylin konfigurointi-paneeliin.  
- Lisää mukautettu fontti poltetun kovat tekstityksen alkuperäiseen videoasetuspaneeliin.  
- Lisää tuen pdf- tai docx-vientiin, yksinkertaisesti aseta vientiliitteeksi pdf tai docx  
- Lisää enemmän valmiita vientiesimerkkimuotoja. Voit ladata esimerkistä ja hienosäätää mallin tulosta helposti.  
- Lisää ominaisuus tallentaa nykyisen projektin tekstitystilan tilannevedokset. Sitten voit helposti palauttaa tallennetut tilannevedokset.  
- Lisää ominaisuus tuoda .srt nykyiseen projektiin tilannevedoksena.  
- Lisää vaihtoehto asettaa esikatseluvideossa tekstityksen näyttämiseksi käännetyn tekstin päälle alkuperäisen tekstin sijaan.  
- Lisää mukautetut vientitoiminnot. Satunnaiset numerot ja satunnainen guid ja escXML ja replaceString mukautetulla muodolla  
- Lisää mukautettu vientilähtötyyppi (tiedosto tai leikepöytä)  
- Lisää mukautettu vientivaihtoehto käytetäänkö kaikki tekstitykset vientiin vai vain valitut  
- Lisää projektin muokkausikkunan ryhmä pääikkunan vaihtoehdoilla  
- Lisää lisäksi hiljaisuusmallin prosessiparametrien määritykset mallin valitsimessa (oikeassa kulmassa), saatat löytää ne vaikeasti, koska useimmissa tapauksissa näitä parametreja ei tarvitse muuttaa  
- Varmista koko näytön esikatseluvideon käyttäytymisen optimointi  
- Hakuavainsanaa tukeva tai -ehto (käytä | tai-sanan tai -merkin jälkeen. Esim. "hei|hello|hej")  
- Hienosäästä hakutoiminnon loogista. Kun vaihda suoritus suorita hakuavainsanoilla, sanojen korvaamisen pitäisi näyttää src-avainsanat ja korvatut avainsanat  
- Optimoi reaaliaikainen stream-transkriptiologiikka  
- Kiinteä joitain alikerranikkunoita ei tuoda eteenpäin -ongelmaa  
- Kiinteä vienti xml-muoto jotkin buginmurtajat  
- Kiinteä muutama mediatiedoston kohdistava wav:n epäonnistuminen   
- Kiinteä jätä korvaussanan kenttä, niin että korvaustoiminto tapahtuu automaattisesti  
- Kiinteä stream-projekti, jossa joitain ongelmia kaatuvat  
  
  
V4.0  
---  
- Lisättiin ominaisuus, jolla voidaan muistaa projektin tekstityksen muokkaajan ulottuvuusominaisuudet. Jokainen projekti voi käyttää erilaista ulottuvuutta ja esikatseluikkunan kokoa. (vanhan projektin on avattava uudelleen, jotta ulottuvuusominaisuudet tallentuvat)  
- Lisää vaihtoehto etsiä tuplatut tekstitykset muokkaajassa  
- Lisää kontekstivalikon vaihtoehto avata muokkain jopa tekstinkäsittelyskriptin prosessin alkaessa  
- Lisää vienti tekstitys .sbv-muodossa  
- Lisää mukautetut vientimallit (kuten .fcpxml, .itt, .ttml)  
- Lisää uusi liitännäinen  
- Lisää käytetyimpien avainsanojen ja korvaussanakonfiguroinnin vaihtoehto pikakäyttöön haun tai korvaamisen yhteydessä  
- Lisää merkitty rivi näyttämään merkkilippu esikatseluikkunan edistymisnäkymässä  
- Lisää merkkivaihtoehto tekstityksen muokkaajan kontekstivalikossa  
- Lisää jakamisen riviominaisuus tekstityksen muokkaajassa, kun valitaan yksittäinen rivi  
- Lisää hakutulokseen projektin nimi riviin  
- Lisää virheen tiedot näyttöön, kun esikäsittelemä media kohtaa virheen  
- Lisää vaihtoehto piilottaa muokkaajan sijainnin rivipainike  
- Lisää ⌘+S pikatoiminto .srt-kappaleen nopeaan vientiin tiedostoon  
- Korjattu mediatiedoston audiometatiedon saanti kahdella audiokanavalla, vaikka todellisuudessa vain yksi. (lisää vaihtoehto ohittaa äänikanavien valinta)  
- Korjattu poltetun tekstityksen epäonnistuminen, kun projektin nimi on muutettu manuaalisesti  
- Korjattu joitain käyttöliittymän ongelmia macOS12:ssa  
- Korjattu ominaisuuden pysymisongelma, joka ei lukitse tilapalkin kuvaketta  
- Kiinteä joitain valoisen teeman käyttöliittymän näyttöongelmia  
  
  
V3.5  
---  
- Lisää tekstitysten ääniotsikkolatausominaisuus. Nyt voit valita mitkä tahansa tekstitykset ja ladata niiden ääniotsikon kontekstivalikon avulla, kun valittuja rivejä on useita, ne yhdistetään automaattisesti yhdeksi ääniotsikoksi.  
- Lisää pieni kelluva ikkunatyyli reaaliaikaiseen äänen tallennukseen  
- Lisää pikanäppäimistövalikko, jolla voi nopeasti aloittaa äänivirran nauhoittamisen projektissa uudessa kelluvassa ikkunassa  
- Lisää nopea toiston alueen ääni pääprojektin hakutuloksessa tai lataamalla hakutulosteen äännepalasen  
- Lisää mahdollisuus ladata malleja keskeytyksen jatkamiseen  
- Lisää tekstityksen muistitoiminnot, nyt voit lisätä muistion mihin tahansa tekstitykseen muokkaajassa  
- Lisää azure-käännösvaihtoehto  
- Lisää globaali tekstityshaku kaikissa projekteissa  
- Lisää korosta etsintäavainsanoja hakutuloksessa  
- Lisää oletuspikanäppäimet nopeaan ohjausikkunan ohjaukseen, kuten sulkeminen/skaalaus/pienentäminen  
- Lisää vaihtoehto piilottaa päätyökalupalkin etiketti  
- Siirretty osan aloituspainike päätyökalupalkista kontekstivalikkoon  
- Kiinteä korvaus toimimaton tyhjällä merkkijonolla  
- Kiinteä puuttuvat pienet ja pienet-en mallit varaservuissa  
- Kiinteä tallennetun äänitiedoston soittimen liukusijainnin tekstitysongelma  
  
  
V3.0  
---  
- Lisää mahdollisuus viedä valittu tekstitystävä median alue uudella mediaämpäri-tiedostolla  
- Lisää mahdollisuus viedä video, jossa on poltetut kovat tekstitykset alkuperäiseen videoon ja mukautettuun tekstitystyyliin  
- Lisää suoran esikatselun tekstitys videon sisällä (tekstityksen tyyli voidaan mukauttaa asetuspaneelissa)  
- Lisää äänen toisto mikrofonin tallennus ja reaaliaikainen transkriptio -tuki (vain macOS13.0+)  
- Lisää tekstityksen yhdistäminen. Segmenttialue ja tekstitys yhdistyvät yhdeksi riviksi.  
- Lisää sovelluksen äänen tallentaminen tallentaa tiedoston ja siitä voidaan tehdä uusi transkriptioprojekti.  
- Lisää vaihtoehto kahdenna tekstitysriviä ja salli sen sisällön tai aikajakon muokkaaminen täydellisen tekstityksen hienosäätämiseksi  
- Lisää asetus Quiqk-käännä sisään kaikissa projekteissa englanniksi Mallin konfigurointi-paneelissa  
- Lisää vaihtoehto käyttää kuiskauksen vihjetoken konfigurointia Mallin konfigurointi-paneeliin  
- Lisää vaihtoehto poistaa automaattinen vieritys tekstitysrivillä, kun esikatsellaan videota  
- Lisää tuki median esikatselun toistonopeuden mukauttamiselle  
- Lisää tuki ⌘+V liittää kopioituja tiedostoja jonoon  
- Lisää nopea vaihto muokkaustilaan. Kaikki tekstitykset voidaan muokata tai tarkastella vaihtamalla pikanäppäimen avulla (⌘+E)  
- Lisää prosenttiosuuden näyttö CPU-käytön aikana  
- Lisää projektien arkistoimisen tuki kontekstivalikossa (pitää luettelon työprojektit siistinä)  
- Lisää Googlen käännös tekstitysten käännön hallintaan  
- Lisää tuki useammille sovelluksille  
- Lisää täyden koon esikatselumedia tekstitysasetelma  
- Lisää tuki medi tiedostojen avaamiseen etsimen avulla  
- Optimoi tekstityksen muokkaaja suurten tieto rivien piirtonopeus  
- Kiinteä moniaudio-kanavavideon valintaa koskeva ongelma  
- Kiinteä esikatselu- ja muokkausprojektien tekstitysongelmia ja videon liukusäätimen navigointia  
  
  
V2.0  
---  
- Tuki äänen tallennukselle ja transkriptiolle muista sovelluksista, kuten (Zoom/Skype/Teams/Meetings App, vain macOS13.0+)  
- Lisää liitännäinen tekstityksen yksinkertaistettuun kiinaan tai perinteiseen kiinaan tai kääntötekstityksellä. (Ensin tarvitset aktiivisen liitännäisen asetusten paneelissa)  
- Korjattu projektin muokkaaja ei pysty käyttämään välilyönti pikatoimintoa median toistamiseen tai pysäyttämiseen ongelma  
- Korjattu SRT- ja VTT- vientimuodon bugi  
  
V1.0  
---  
- Transkriboi ääni- tai videotiedostot  
- Käytä deepl ilmaista API:ta tekstityksen kääntämiseen  
- Upotettu tekstieditori korjataksesi transkriptiota  
- Vie SRT,VTT,CSV,JSON,SEGMENT  
- Tuki kunkin tekstityksen asettamiseen kaiuttimelle  
- Useimmat toiminnot tukevat erävalintaa aktivoidaksesi. Kuten erätehtävään suoritus, erä rivi käännös, erä rivi kaiutinasettelu  
- Tuki tiedostojen vetämistä ja pudottamista transkription aloittamiseksi  
- Tukee haun läpikirjoitusten kirjoittamista  
- Muokkaaja voi esikatsella ääni- tai videotiedostoa synkronoida toistovälin kanssa  
- Tuki monikieliselle käännökselle  
- Tuki mukautettujen usein käytettyjen kielien valitsemiseksi muuntamiseen tai kääntämiseen  
  
 ## Toiminnot

- Muunna ääni- tai videotiedostot tekstiksi
- Tuki äänen tallentamiselle ja muuntamiselle muissa sovelluksissa, kuten (Zoom/Skype/Teams/Muut sovellukset, vain macOS 13.0+ ja vaatii näytön tallennusoikeudet)
- Käytä ilmaista DeepL API:a tekstitysten kääntämiseen
- Sisäänrakennettu tekstityksen muokkaustyökalu
- Vienti SRT, VTT, CSV, JSON, SEGMENT-muotoihin
- Jokaiselle tekstitykselle voi määrittää henkilön nimen
- Useimmat toiminnot tukevat joukkotoimintoja. Esimerkiksi joukkotehtävien suoritus, rivien massakääntäminen ja massarivien määrittäminen henkilölle
- Tukee tiedostojen raahaamista ja pudottamista tekstityksen muuntamiseen
- Voit kirjoittaa tekstiä samalla kun selaat tekstityksiä
- Muokkaustyökalussa voi esikatsella ääni- tai videotiedoston toistoa
- Tekstitysten valinnan voi viedä uutena mediatiedostona
- Videosisällön voi viedä alkuperäiseen videoon kiinteinä tai mukautetuilla tekstitysasuilla
- Tekstitysten esikatselu suoraan videon esikatselussa (tekstitysten asetuksia voi mukauttaa asetuksista)
- Mikrofonin äänitys ja reaaliaikainen muuntaminen tekstiksi (macOS 13+)
- Toiminto tekstityssegmenttien yhdistämiseen. Segmentin alue ja tekstitys yhdistyvät yhdeksi riviksi
- Sovelluksen äänitys tallentuu automaattisesti ja voidaan muuntaa uudeksi muuntoprojektiksi
- Tekstitysrivejä voi kopioida tai ajanasetteluaustaa muokattaessa
- Mukautettu toistoasetus multimediaesitysten esikatseluun
- Voit liittää kopioituja tiedostoja jonoon käyttämällä ⌘+V-näppäinyhdistelmää
- Näytä prosessoinnin CPU-kuormitus äänenkäsittelyn aikana
- Tukee arkistojen luomista oikeassa valikossa (pitääkseen aktiivisten projektien luettelon siistinä)
- Tuki tekstien kääntämiseen Google Translaten avulla
- Koko näytön tekstitys esikatselussa multimediaesityksissä
- Tuki multimediaesitysten avaamiselle oikean valikon kautta Finderissä
- Tuki monikielisyyden muunnokselle
- Tuki muunnokselle tai käännökselle yleisimmin käytetyille kielille 

## Kuvakaappaukset

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