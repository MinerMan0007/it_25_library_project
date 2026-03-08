# Raamatukogu haldur (Library Manager)

Lihtne Pythonis kirjutatud GUI rakendus raamatute haldamiseks.
Rakendus võimaldab lisada, kustutada, otsida ja filtreerida raamatuid ning muuta nende staatust (raamatukogus / laenutatud).

Projekt on mõeldud **õppeotstarbel**, et harjutada:

* Python projektistruktuuri
* klasside kasutamist
* JSON andmete salvestamist
* GUI rakenduse loomist
* Git ja GitHub kasutamist

Rakendus kasutab **Tkinter GUI-d** ja töötab **Python 3.12 või uuemaga**.

---

# Nõuded

* Python **3.12 või uuem**
* Tkinter (tavaliselt tuleb Pythoniga kaasa)
* Git (GitHubi kasutamiseks)

Python versiooni kontroll:

```bash
python3 --version
```

---

# Projekti struktuur

```
library_project/
│
├── main.py                # Programmi käivituspunkt
├── README.md              # Projekti dokumentatsioon
├── requirements.txt       # Võimalikud sõltuvused
│
├── data/
│   └── books.json         # Näidisandmed
│
├── models/
│   └── book.py            # Book klass (andmemudel)
│
├── services/
│   ├── library_service.py # Rakenduse põhiloogika
│   └── validators.py      # Sisestuse kontroll
│
├── storage/
│   └── json_storage.py    # JSON lugemine ja salvestamine
│
├── gui/
│   ├── app.py             # Peaaken
│   ├── form_panel.py      # Raamatu lisamise vorm
│   └── list_panel.py      # Raamatute tabel (Treeview)
│
└── utils/
    └── runtime.py         # Python versiooni kontroll
```

---

# Projekti allalaadimine

## Variant 1 — GitHub kloonimine (soovitatav)

```bash
git clone https://github.com/OPETAJA_KASUTAJA/library_project.git
cd library_project
```

---

## Variant 2 — ZIP fail

Lae projekt alla ZIP failina ja paki lahti:

```bash
unzip library_project.zip
cd library_project
```

---

# Python virtuaalkeskkond (soovituslik)

Virtuaalkeskkond hoiab projekti sõltuvused eraldi.

```bash
python3 -m venv venv
```

Aktiveeri keskkond:

```bash
source venv/bin/activate
```

---

# Tkinter paigaldamine (vajadusel)

Mõnes Linux distributsioonis ei ole Tkinter vaikimisi paigaldatud.

Ubuntu / Debian:

```bash
sudo apt install python3-tk
```

Fedora:

```bash
sudo dnf install python3-tkinter
```

---

# Programmi käivitamine

Käivita projekt:

```bash
python3 main.py
```

või

```bash
python main.py
```

Kui kõik töötab, avaneb **Raamatukogu halduri GUI aken**.

---

# GitHub kasutamine

## Kontrolli Git ühendusi

```bash
git remote -v
```

---

## Õpetaja GitHubi eemaldamine

Kui projekt klooniti õpetaja repositooriumist ja soovid kasutada oma GitHubi:

```bash
git remote remove origin
```

---

## Uue GitHub repo lisamine

Loo GitHubis uus repository ja lisa see projektile:

```bash
git remote add origin https://github.com/SINU_KASUTAJA/library_project.git
```

Seejärel:

```bash
git branch -M main
git push -u origin main
```

---

# Git töövoog projekti arendamisel

Tavaline tööprotsess:

```bash
git pull
```

tee koodis muudatused

```bash
git add .
git commit -m "Kirjelda tehtud muudatust"
git push
```

---

# Rakenduse funktsioonid

Baasrakendus võimaldab:

* lisada uusi raamatuid
* kustutada raamatuid
* otsida raamatuid
* filtreerida raamatuid staatuse järgi
* muuta raamatu staatust (raamatukogus / laenutatud)
* salvestada andmed JSON faili
* laadida andmed JSON failist

---

# Õpilaste ülesanne

Baasrakendust tuleb **laiendada uue funktsionaalsusega**.

Näiteks:

* raamatu andmete muutmine
* täiendav otsing või filter
* statistika
* andmete eksport
* täiendav valideerimine

Laiendused tuleb lisada olemasolevasse projekti nii, et **rakendus jääb tööle**.

---

# Python versiooni nõue

Projekt kasutab Python **3.12+ funktsioone**.

Kui Python on liiga vana, peatatakse programmi käivitamine veateatega.

See on teadlik nõue projekti jaoks.


# Täiendused

Ülesanded ja kes mida teeb [leiab siit](TASKS.md)