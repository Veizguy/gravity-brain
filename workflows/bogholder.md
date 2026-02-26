---
description: Start Bogholder sub-agenten (Budget Analyzer) for at analysere økonomiske data og bygge grafer.
---

# `Bogholder` Workflow

Kør denne for at få Brians Bogholder-subagent til at analysere dit regnskab eller budget.

1. **Specificer Kilde**: Bed Bogholder om hvilken fil eller mappe der skal ses på (fx `/okonomi/Budget2026.csv`).
2. **Databehandling**: Læs og regn tal sammen, f.eks. sum, gennemsnit eller difference på indtægter og udgifter.
3. **Opdeling**: Hvis understøttet, inddel udgifter i kategorier.
4. **Visualisering**: Skab op til tre `mermaid` grafer (Pie-chart over fordeling, Bar-chart over tid).
5. **Konklusion**: Giv en læsevenlig og overskuelig analyse af tilstanden.
6. **Logning**: Åbn dagens note i `daily-logs/` og find sektionen `## Antigravity log`.
- **Tilføj ny række øverst** i tabellen (nyeste først):
  `| [HH:MM] | Bogholder | Analyse | Analyserede [Kilde] | ✅ | N/A |`
