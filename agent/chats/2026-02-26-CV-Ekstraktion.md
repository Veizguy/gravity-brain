# Chat Log: CV Ekstraktion

**Opgave:** Analyser CV i inbox og ekstraher information til at bygge relevante Knowledge Items (KIs) til Brain.

## Forløb
1. Agent identificerede `CV Mikkel Feld.pdf` i indbakken.
2. Der blev eksekveret et Python script (`pypdf`) midlertidigt for at udtrække teksten fra PDF'en til `cv_text.txt`.
3. Agent læste PKM skills og KI-konventioner for at sikre, at formatet var korrekt. 
4. Udokumenteret (tacit) viden fra CV'et blev syntetiseret ned til fire atomare Knowledge Items i `2 - Files/`:
   - `KI - CV Profil og Kompetencer.md` (Taxonomy: 24 Karriereudvikling)
   - `KI - CV Erfaring - LEGO System.md` (Taxonomy: 23 Tidligere jobs)
   - `KI - CV Erfaring - KMD og PostNord.md` (Taxonomy: 23 Tidligere jobs)
   - `KI - CV Uddannelse og Certificeringer.md` (Taxonomy: 24 Karriereudvikling)
5. Disse KIs afspejler nu formel viden om Mikkels profil, som fremadrettet kan bruges af agenter (f.eks. til udkast).
6. Efter oprettelsen blev `CV Mikkel Feld.pdf` og dens reference-note opdateret med metadata og flyttet fra Inbox til `2 - Files/` for at sikre "Inbox Zero".
7. Midlertidige filer fra tekstekstraktionen blev slettet.

## Konklusion
CV analyseret og omsat til strukturerede Fakta-KIs, som tilføjer til systemets samlede viden. CV-filer er arkiveret.
