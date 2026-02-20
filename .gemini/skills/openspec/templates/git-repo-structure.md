# Git Repo OpenSpec Struktur

Standard mappestruktur for Git-baserede projekter med OpenSpec.

```
project-root/
├── openspec/
│   ├── specs/                          # Source of truth
│   │   ├── project.md                  # Projekt-konstitution
│   │   ├── architecture.md             # System-design
│   │   └── features/                   # Feature-specifikationer
│   │       ├── feature-a.md
│   │       └── feature-b.md
│   ├── changes/                        # Aktive ændringsforslag
│   │   └── <feature-name>/
│   │       ├── proposal.md             # Motivation, impact, risici
│   │       ├── tasks.md                # Atomare implementeringsskridt [Agent: Arkitekt]
│   │       └── deltas/                 # ADDED/MODIFIED/REMOVED specs
│   │           ├── added-new-spec.md
│   │           └── modified-existing.md
│   └── archive/                        # Arkiverede ændringer
│       └── 2026-02-18-feature-name/
├── .gemini/                            # Agent konfiguration
│   ├── GEMINI.md                       # Agent identity
│   ├── rules/                          # Agent regler
│   └── skills/                         # Projekt-specifikke skills
├── .agent/
│   ├── workflows/                      # Slash-command workflows
│   └── skills/                         # Agent skills
├── src/                                # Kildekode (eller ansible/, etc.)
└── README.md
```

## Initiering

Kør disse kommandoer for at oprette strukturen:

```bash
mkdir -p openspec/{specs/features,changes,archive}
touch openspec/specs/project.md
touch openspec/specs/architecture.md
```

## Navngivning

- **Change folders**: kebab-case, beskrivende: `add-monitoring-stack`, `fix-network-config`
- **Archive folders**: `YYYY-MM-DD-<change-name>`
- **Spec filer**: kebab-case: `user-authentication.md`, `network-topology.md`
