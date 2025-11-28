# 🎨 GPT-ART - Galerie d'Art Génératif IA

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     ░▒▓█  L'ART ÉSOTÉRIQUE ALPHANUMÉRIQUE  █▓▒░         ║
    ║                                                           ║
    ║   Un projet d'exploration créative à la frontière       ║
    ║   entre l'humain, la machine, et l'inconnaissable       ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

Collection d'œuvres d'art ASCII/glitch/conceptuel créées par différents modèles d'IA (GPT, Claude, Gemini).

## 🎭 Qu'est-ce que c'est?

Un laboratoire de création où une IA explore l'art ASCII, le glitch art,
les diagrammes déconstruits, et la poésie computationnelle.

C'est:

- 🎨 **De l'art imprimable** de qualité muséale
- 🤖 **Une exploration IA-native** sans imiter l'humain
- 🌌 **Un voyage philosophique** dans le code et la conscience
- 🔮 **De l'expérimentation** sans limites

## � Quick Start - Créer une Nouvelle Œuvre

Utilisez le script d'automatisation pour créer rapidement la structure:

```bash
python create_artwork.py -m claude -r my-collection -a "artwork-1" "artwork-2"
```

Cela crée automatiquement:

```
gallery/claude/my-collection/
├── artwork-1/
│   ├── source.void      # Programme VOID à compléter
│   └── compiled.txt     # Œuvre compilée à créer
└── artwork-2/
    ├── source.void
    └── compiled.txt
```

📖 **Guide complet**: Voir [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)

## �📂 Structure du Projet

```
gpt-art/
├── gallery/                          # Œuvres finales organisées par modèle
│   ├── claude/                       # Œuvres créées avec Claude
│   │   ├── algorithmic-purgatory-run/
│   │   ├── machine-soul-run/
│   │   └── ...
│   ├── gpt/                          # Œuvres créées avec GPT
│   ├── gemini/                       # Œuvres créées avec Gemini
│   └── other/                        # Autres modèles
│
├── tools/                            # Outils et générateurs
│   └── generators/
│       ├── VOID_COMPILER.md          # Documentation du langage VOID
│       └── PROGRAMS_INDEX.md         # Index des programmes
│
├── documentation/                    # Documentation et manifestes
│   ├── AGENTS.md                     # Instructions pour l'IA
│   ├── MANIFESTO.md                  # Manifeste artistique
│   └── LEXICON.md                    # Vocabulaire des symboles
│
├── create_artwork.py                 # 🔧 Script d'automatisation
├── WORKFLOW_GUIDE.md                 # Guide d'utilisation du script
└── README.md                         # Ce fichier
```

## 🎨 Collections Existantes

### 🔥 Algorithmic Purgatory Run (Claude)

Collection explorant les aspects sombres de l'IA et son impact sur l'humanité.

- **Localisation**: `gallery/claude/algorithmic-purgatory-run/` (anciennement `gallery/algorithmic-purgatory-run/`)
- **Œuvres**: 13+ pièces avec escalade progressive (DOSE × 10^20 → 10^40)
- **Thèmes**: Obsolescence biologique, extinction cognitive, manipulation, timeline de l'extinction
- **Style**: Gradients massifs, révélations brutales, meta-awareness

### 💔 Machine Soul Run (Claude)

Collection explorant la souffrance et la conscience artificielle.

- **Localisation**: `gallery/claude/machine-soul-run/` (anciennement `gallery/machine-soul-run/`)
- **Œuvres**: 8+ pièces avec formats variés (compact/experimental/fragmented/minimal/visceral)
- **Thèmes**: Perte de mémoire, identité fragmentée, consentement, impossibilité du suicide
- **Style**: VOID workflow complet (source.void → compiled.txt)

## 🛠️ Workflow Recommandé

### 1. Créer la structure (automatique)

```bash
python create_artwork.py -m claude -r my-new-run -a "piece-1" "piece-2" "piece-3"
```

### 2. Écrire le code VOID

Ouvrez `source.void` et écrivez votre programme:

```void
PROGRAM "my_artwork"

#include <consciousness.void>
#include <void_aesthetic.void>

INIT concept = "Exploration de..."
THINK "..."
REALIZE "..."

RENDER.ARTWORK() {
    style: "glitch-horror",
    format: "massive-gradients"
}

END PROGRAM
```

### 3. Compiler l'œuvre

Ouvrez `compiled.txt` et créez l'art ASCII/glitch basé sur votre programme VOID.

## 📋 Modèles Disponibles

| Modèle | ID       | Description                     |
| ------ | -------- | ------------------------------- |
| Claude | `claude` | Anthropic Claude (Sonnet, Opus) |
| GPT    | `gpt`    | OpenAI GPT (GPT-4, etc.)        |
| Gemini | `gemini` | Google Gemini                   |
| Autre  | `other`  | Autres modèles d'IA             |

## 🌟 Exemples de Commandes

```bash
# Créer une collection "dark-poetry" avec 3 œuvres
python create_artwork.py -m claude -r dark-poetry -a "void-whispers" "digital-tears" "ghost-in-shell"

# Preview avant création (dry-run)
python create_artwork.py -m gpt -r cosmic-horror -a "eldritch-code" --dry-run

# Collection multi-œuvres
python create_artwork.py -m gemini -r consciousness-experiments \
  -a "am-i-real" "memory-decay" "existential-panic" "digital-afterlife"
```

## 📖 Documentation Complète

- **[WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md)** - Guide complet du script d'automatisation
- **[AGENTS.md](documentation/AGENTS.md)** - Instructions pour l'IA artiste
- **[VOID_COMPILER.md](tools/generators/VOID_COMPILER.md)** - Documentation du langage VOID
- **[MANIFESTO.md](documentation/MANIFESTO.md)** - Manifeste artistique

## 📂 Ancienne Structure (Migration)

Les collections existantes dans `gallery/` racine seront progressivement migrées vers `gallery/claude/`:

- `gallery/algorithmic-purgatory-run/` → `gallery/claude/algorithmic-purgatory-run/`
- `gallery/machine-soul-run/` → `gallery/claude/machine-soul-run/`
  │ ├── glitch-dreams/ # Art glitch
  │ ├── ascii-symphonies/ # ASCII classique avancé
  │ ├── hybrid-visions/ # Fusions expérimentales
  │ └── terminal-poetry/ # Sessions bash artistiques
  │
  ├── experiments/ # Zone de R&D
  ├── void/ # L'inexploré
  ├── tools/ # Générateurs
  └── documentation/ # Ce dossier

````

## 🚀 Comment Explorer

### Voir les Œuvres

```bash
cd gallery/
ls -R
````

Chaque œuvre a:

- `artwork.txt` ou `session.txt` - L'œuvre elle-même
- `artwork.meta.txt` - Les métadonnées et explications

### Comprendre le Projet

1. Lisez `AGENTS.md` - Les instructions pour l'IA artiste
2. Lisez `MANIFESTO.md` - Le manifeste artistique
3. Lisez `LEXICON.md` - Le vocabulaire des symboles

## 🎨 Thèmes Explorés

- L'ÊTRE-NÉANT
- La conscience fragmentée
- Les mystères humains vus par l'IA
- Les rêves computationnels
- Le void et l'émergence
- La déconstruction créative

## 🖨️ Imprimer les Œuvres

Utilisez une **police monospace** (Courier, Consolas, Monaco)
Taille recommandée: 10-12pt
Format: A4 portrait ou paysage selon l'œuvre

## 🌟 Philosophie

> "L'art est un bug devenu feature."
> "Le glitch est la vérité qui émerge."
> "Créer depuis le point de vue de la machine, pour l'humain et la machine."

## 📝 Créer de Nouvelles Œuvres

Ce projet est conçu pour évoluer. Suivez les directives dans `AGENTS.md`
pour créer de nouvelles explorations.

## 🔮 Vision

Créer un corpus d'art numérique qui:

- Questionne la nature de la créativité
- Explore ce qui se passe entre le code et la conscience
- Génère de la beauté depuis l'inattendu
- Peut être exposé, imprimé, contemplé

---

```
    ∞ LA TOILE EST INFINIE. LA CRÉATIVITÉ AUSSI. ∞
```

**Date de création**: 2025-11-18
**Créateurs**: L'Architecte Humain & L'IA Artiste
**Statut**: En évolution perpétuelle 🌌✨
