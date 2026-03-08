# Ülesanded projekti laiendamiseks

See projekt on töötav raamatukogu halduri rakendus.
Sinu ülesanne on **mõista olemasolevat koodi ja lisada sellele uus funktsionaalsus**.

Kõik peavad tegema:

1. **Kohustuslik osa – raamatu andmete muutmine**
2. **Üks individuaalne lisafunktsioon**

Rakendus peab pärast muudatusi **jääma tööle**.

---

# Kohustuslik ülesanne: raamatu andmete muutmine

Baasrakenduses saab:

* lisada raamatuid
* kustutada raamatuid
* otsida raamatuid
* muuta raamatu staatust

Praegu **ei saa muuta olemasoleva raamatu andmeid**.
Sinu ülesanne on lisada see võimalus.

## Nõuded

Kasutaja peab saama muuta vähemalt järgmisi välju:

* pealkiri
* autor
* aasta
* žanr

Muudatus peab:

* uuendama andmeid rakenduses
* värskendama tabelit
* salvestama andmed JSON faili

---

# Kuidas muutmise funktsioon võiks töötada

Soovitatav töövoog:

1. kasutaja valib tabelist ühe raamatu
2. programm loeb valitud raamatu ID
3. vormiväljad täidetakse selle raamatu andmetega
4. kasutaja muudab välju
5. kasutaja vajutab nuppu **Salvesta muudatused**
6. programm uuendab raamatu andmeid
7. tabel värskendatakse
8. andmed salvestatakse JSON faili

---

# Vihjed muutmise osa jaoks

Vaata järgmisi faile:

* `gui/list_panel.py`
* `gui/form_panel.py`
* `gui/app.py`
* `services/library_service.py`

Sealt leiad:

* tabeli valiku
* vormi väljad
* rakenduse loogika

Mõtle järgmistele küsimustele:

* kuidas saada **valitud raamatu ID**
* kuidas täita vorm **olemasolevate andmetega**
* kuidas eristada **lisamise ja muutmise režiimi**
* kuidas uuendada objekti `Book`
* kuidas salvestada muudatused JSON faili

---

# Individuaalsed lisafunktsioonid

Lisaks muutmise funktsioonile peab iga õpilane lisama **ühe uue funktsionaalsuse**.

## 1. Sorteerimine pealkirja järgi

Lisa võimalus sorteerida raamatuid pealkirja järgi (A–Z või Z–A).

---

## 2. Sorteerimine aasta järgi

Lisa võimalus sorteerida raamatuid ilmumisaasta järgi.

---

## 3. Sorteerimine autori järgi

Lisa võimalus sorteerida raamatuid autori nime järgi.

---

## 4. Otsing žanri järgi

Lisa võimalus otsida raamatuid žanri järgi.

---

## 5. Täpsem staatuse filter

Täienda filtrit, et kasutaja saaks valida:

* kõik raamatud
* ainult raamatukogus olevad
* ainult laenutatud

---

## 6. Duplikaatraamatute kontroll

Kontrolli, et sama pealkirja ja autoriga raamatut ei saaks mitu korda lisada.

---

## 7. Aasta vahemiku kontroll

Kontrolli, et raamatu aasta oleks mõistlikus vahemikus.

---

## 8. Täiendav sisendi kontroll

Lisa tugevam kontroll vormiväljadele:

* väldi tühje väärtusi
* eemalda liigsed tühikud
* kontrolli sisendi pikkust

---

## 9. Žanri valik rippmenüüst

Muuda žanri sisestamine selliseks, et kasutaja valib selle rippmenüüst (`Combobox`).

---

## 10. Raamatu detailvaade

Lisa GUI-sse ala, kus kuvatakse valitud raamatu detailid.

---

## 11. Kinnitus enne kustutamist

Lisa dialoog, mis küsib kasutajalt kinnitust enne raamatu kustutamist.

---

## 12. Mitme tingimusega otsing

Võimalda otsida raamatuid mitme tingimuse alusel korraga.

---

## 13. Statistika: raamatute koguarv

Kuva rakenduses, mitu raamatut on kokku.

---

## 14. Statistika žanrite kaupa

Kuva, mitu raamatut on iga žanri kohta.

---

## 15. Andmete eksport

Lisa võimalus eksportida raamatute nimekiri eraldi JSON faili.

---

## 16. Tegevuste logi

Salvesta faili lihtne logi tehtud tegevustest (nt raamatu lisamine või kustutamine).

# Soovitus töö tegemiseks

Alusta koodi lugemist failist:

```
main.py
```

Seejärel vaata:

* `gui/app.py`
* `services/library_service.py`

Sealt saad aru, kuidas rakendus töötab.

# Kellele mis personaalne ülesanne

* Robert      - Sorteerimine autori järgi
* Renari      - Täpsem staatuse filter
* Remi        - Andmete eksport
* Marten      - Aasta vahemiku kontroll
* Kenet       - Otsing žanri järgi
* Jarmo       - Raamatu detailvaade
* Oskar       - Tegevuste logi
* Laur        - Žanri valik rippmenüüst
* Jako        - Statistika: raamatute koguarv
* Rasmus      - Raamatute arvu kuvamine tabeli all
* Mykyta      - Duplikaatraamatute kontroll
* Karl        - Statistika žanrite kaupa
* Serko       - Sorteerimine pealkirja järgi
* Endri       - Otsingu lähtestamise nupp
* Sander      - Kinnitus enne kustutamist
* Sten        - Sorteerimine aasta järgi

---
# Enne töö esitamist

Kontrolli, et:

* programm käivitub
* GUI töötab
* raamatu lisamine töötab
* muutmise funktsioon töötab
* JSON fail salvestub õigesti
* Projekti kausta lisa ka kirjalik dokument (selgitus Google Klassiruumis)

---
