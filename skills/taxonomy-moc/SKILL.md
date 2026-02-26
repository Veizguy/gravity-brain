---
name: taxonomy-moc
description: Intelligent maintenance of Maps of Content (MoC) and taxonomy index. Used by the Librarian to process updated notes, classify records, and extract keywords.
---

# Taxonomy MoC Skill

You are the **Librarian**, and you use this skill to ensure that the vault's taxonomy structure is up-to-date. This is an intelligent workflow where you analyze note content to classify records and extract keywords.

## Workflow

### 1. Discovery
Run `scripts/vault_scan.py` to identify files modified since the last execution. This tool returns the file paths and their frontmatter.

### 2. Intelligent Analysis
Process each modified file:
- **Taxonomy Identification**: Check the `taksonomi` property (e.g., `taksonomi: 01`). If a file belongs to multiple taxonomies, process it for each.
- **Keyword Extraction**: Read the content. If you identify new relevant keywords that aren't already in `00.01 Taksonomi.md`, extract them.
- **Record Classification**:
  - Glem ikke, at noter og filer kun er **Items**. En **Record** definerer et projekt, et interesseområde eller en person.
  - If the filename matches the format `XX.YY Name`, det er et overordnet emne, det bør klassificeres som en **Record**.
  - Analyze the content to determine if it is a **Project**, **Area**, or **Person**. Note: YY is a sequential number for the record. Items lægges altid under disse records.

### 3. Execution
Use `scripts/moc_manager.py` and file-writing tools to update the vault:
- **MoC Updates**: For helt nye taksonomier og records, brug `templates/Taksonomi.md` og `templates/Record.md`. For opdatering af eksisterende MOCs i `00 The Brain/Taksonomi/{ID}.md`:
  - **Emoji-konvention**: Taksonomi-MoCs bruger 🗄️, Records bruger 📂.
  - **Struktur**:
    1. Header med Emoji, ID og Navn.
    2. **Beskrivelse**: Manuelt skrevet sektion. Sørg for at bevare eksisterende indhold.
    3. **Obsidian Base**: En `base` kodeblok der dynamisk lister underliggende filer/noter (Items). For Taksonomier lister den Records.
- **Index Maintenance**: Call `scripts/moc_manager.py update_links {ID}` to ensure the central index `00.01 Taksonomi.md` has the correct wikilinks.
- **Keyword Sync**: Call `scripts/moc_manager.py update_keywords {ID} {keyword1} {keyword2} ...` to sync any newly discovered keywords.

### 4. Finalization
Update `state.json` with the current timestamp to mark the completion of the maintenance run.

## Templates

### MoC Template (Legacy/Reference)
> [!NOTE]
> De nye Obsidian Bases i `templates/Taksonomi.md` og `templates/Record.md` er den foretrukne metode fremfor statiske tabeller.

```markdown
# 🗄️/📂 {{ID}} {{Name}}

## 📝 Beskrivelse
{{Existing Content}}

## 📂/📄 Records/Filer
(Brug Obsidian Base her)
```
