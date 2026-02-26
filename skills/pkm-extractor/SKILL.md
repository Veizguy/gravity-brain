---
name: pkm-extractor
description: Bruges til at ekstrahere tekst og data fra binære filer som PDF-dokumenter og billedfiler, når agenter har brug for at "læse" dem for at opsamle viden.
---

# PKM Data Extractor

Denne skill tilbyder et standardiseret workflow og værktøjer for agenter, så de nemt kan trække data og råtekst ud af filer, som ikke umiddelbart kan læses direkte via standard tekst-værktøjer. Det gælder specielt PDF'er og billeder, der lander i indbakken (fx CV'er, kvitteringer eller scans).

## Kerneworkflow

Før du forsøger at analysere eller opsummere en binær fil (PDF/billede):

1. **Undersøg Filen:** Tjek filtypen. For billeder kan agenters integrerede visuelle værktøjer nogle gange bruges, men ofte vil et eksplicit script sikre, at råteksten kan videresendes til videre bearbejdning.
2. **Klargør miljøet (hvis nødvendigt):** Værktøjerne kræver specifikke Python-pakker. Hvis scriptet fejler pga. manglende moduler, kan du enten:
   - Køre det i et midlertidigt virtuelt miljø (`venv`) i mappen, hvor filen ligger.
   - Installere pakkerne lokalt (`pip install pypdf Pillow pytesseract`). *Bemærk: Tesseract OCR skal også være installeret på værtssystemet for at læse billeder.*
3. **Ekstrahér og gem:** I stedet for at dumpe al teksten i terminalen, som potentielt sprænger din tokensize, anbefales det at dumpe outputtet i en midlertidig `.txt` fil under `1 - Inbox` (f.eks. `temp_extract.txt`), lytte teksten igennem med fx `view_file`, lave resuméer/KIs og efterfølgende slette tekstfilen igen.

## Automatisering: OCR Watcher

Denne skill inkluderer en **Always-on OCR Watcher**, der kører i baggrunden på Brian.
- den overvåger løbende `1 - Inbox/assets/`.
- Når en PDF eller et billede lander der, oprettes automatisk en `OCR_[filnavn].md` i `1 - Inbox/` med den udpakkede tekst.
- Dette virker uanset om filen sendes via Telegram, mobil-app eller manuelt.

**Genstart ved behov:**
Hvis systemet har været nede, kan watcheren startes med:
`bash skills/pkm-extractor/start_ocr_watcher.sh`

## Værktøjer og Scripts

Skill'en inkluderer et generisk Python script til at læse PDF'er og Billeder:

### `scripts/extract.py`

**Sti:** `skills/pkm-extractor/scripts/extract.py`

Dette script tager stien til en fil (PDF eller Billede) og udskriver den udpakkede tekst til stdout. 

**Brugseksempel (i terminalen, fx for en PDF):**

```bash
# Sørg for at pypdf er installeret, f.eks. i et temp-venv
python3 -m venv venv && source venv/bin/activate && pip install pypdf
python3 "/Users/mikkelfeld/obsidian/brain/skills/pkm-extractor/scripts/extract.py" "/sti/til/dokument.pdf" > "/sti/til/midlertidig_tekst.txt"
deactivate
```

**Brugseksempel (for Billede, kræver Tesseract):**

```bash
# Kræver system-tesseract og moduler
python3 -m venv venv && source venv/bin/activate && pip install Pillow pytesseract
python3 "/Users/mikkelfeld/obsidian/brain/skills/pkm-extractor/scripts/extract.py" "/sti/til/billede.png" > "/sti/til/midlertidig_tekst.txt"
deactivate
```

## Best Practices

1. **Respekter kontekstvinduet:** Hvis et PDF-dokument er på 40 sider, kan du ikke indlæse det hele på én gang. Brug scriptet, gem som en .txt, og kig derefter stykkevis i filen (eller del det op), før du genererer Knowledge Items (KIs).
2. **Inbox Zero:** Glem ikke at slette `.txt` filen og dit evt. `venv` miljø, når du har ekstraheret det du skulle bruge.
3. **Konvertering til KI:** Opret relevante KIs baseret på udtrækket (følg din PKM skill, f.eks. opdeling i Rule-KI eller Factual-KI med korrekte YAML metadata). Flyt derefter originalfilen til dens permanente plads i arkivet (`2 - Files/`).
