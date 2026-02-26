# Obsidian Vault OpenSpec Struktur

Tilpasset mappestruktur for Obsidian vaults der integrerer med OpenSpec-principper.

```
vault-root/
├── .openspec/
│   ├── specs/                          # Vault-konstitution og -regler
│   │   ├── project.md                  # Vault formål og scope
│   │   └── conventions.md              # Navngivning, tags, linking-regler
│   ├── changes/                        # Aktive vault-ændringer
│   │   └── <reorganisering-name>/
│   │       ├── proposal.md
│   │       └── tasks.md
│   └── archive/                        # Afsluttede ændringer
├── 00-Inbox/                           # Ubehandlede noter
├── 10-Projects/                        # Aktive projekter
│   └── <projekt>/
│       ├── README.md
│       └── ...
├── 20-Areas/                           # Ansvarsområder (løbende)
│   ├── career/
│   ├── health/
│   └── homelab/
├── 30-Resources/                       # Reference-materiale
│   ├── articles/
│   ├── guides/
│   └── research/
├── 40-Archive/                         # Inaktivt materiale
├── Templates/                          # Note-templates
│   ├── daily-note.md
│   ├── project.md
│   └── research-note.md
└── .obsidian/                          # Obsidian konfiguration
```

## Principper

1. **PARA-inspireret**: Projects, Areas, Resources, Archive
2. **Inbox-first**: Alt nyt starter i `00-Inbox/` og sorteres derfra
3. **Links over folders**: Brug `[[wikilinks]]` til at skabe relationer
4. **Tags for klassificering**: `#status/draft`, `#type/research`, `#area/homelab`
5. **OpenSpec for store ændringer**: Brug `.openspec/changes/` ved vault-reorganisering

## Navngivning

- **Filer**: kebab-case eller Title Case (efter præference)
- **Folders**: nummereret præfiks for sortering (`00-`, `10-`, etc.)
- **Tags**: hierarkiske med `/` separator
