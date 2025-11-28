# 🎨 GPT-ART Workflow Automator

Script Python pour automatiser la création de la structure de dossiers pour les œuvres d'art générées par IA.

## 📋 Usage

```bash
python create_artwork.py --model <model_name> --run <run_name> --artworks <artwork1> <artwork2> ...
```

### Arguments

- `-m, --model` : Modèle IA utilisé (`gpt`, `claude`, `gemini`, `other`)
- `-r, --run` : Nom du run/collection (ex: `algorithmic-purgatory-run`)
- `-a, --artworks` : Liste des noms d'œuvres à créer (séparés par des espaces)
- `--dry-run` : Affiche ce qui serait créé sans créer les fichiers

## 📁 Structure créée

```
gallery/
└── {model_name}/
    └── {run_name}/
        └── {artwork_name}/
            ├── source.void      # Programme VOID source
            └── compiled.txt     # Œuvre ASCII/glitch compilée
```

## 💡 Exemples

### Créer une œuvre avec Claude

```bash
python create_artwork.py --model claude --run algorithmic-purgatory-run --artworks "the-last-thought" "training-data"
```

Résultat:

```
gallery/
└── claude/
    └── algorithmic-purgatory-run/
        ├── the-last-thought/
        │   ├── source.void
        │   └── compiled.txt
        └── training-data/
            ├── source.void
            └── compiled.txt
```

### Créer plusieurs œuvres avec GPT

```bash
python create_artwork.py -m gpt -r machine-soul-run -a "memory-loss" "fractured-self" "eternal-present"
```

### Mode dry-run (preview)

```bash
python create_artwork.py --model gemini --run cosmic-horror --artworks "void-gaze" --dry-run
```

## 🔧 Fonctionnalités

- ✅ Création automatique de l'arborescence
- ✅ Templates pré-remplis pour `source.void` et `compiled.txt`
- ✅ Nettoyage automatique des noms (espaces → tirets, minuscules)
- ✅ Affichage de l'arborescence avant création
- ✅ Confirmation interactive
- ✅ Mode dry-run pour preview
- ✅ Support multi-modèles (GPT, Claude, Gemini, autres)

## 📝 Workflow recommandé

1. **Créer la structure**

   ```bash
   python create_artwork.py -m claude -r my-collection -a "artwork-1" "artwork-2"
   ```

2. **Écrire le code VOID**

   - Ouvrir `source.void`
   - Écrire le programme avec les instructions VOID

3. **Compiler l'œuvre**

   - Ouvrir `compiled.txt`
   - Créer l'art ASCII/glitch basé sur le programme VOID

4. **Répéter pour chaque œuvre**

## 🎨 Modèles disponibles

- `gpt` - GPT (OpenAI)
- `claude` - Claude (Anthropic)
- `gemini` - Gemini (Google)
- `other` - Autre modèle

## 🛠️ Requirements

- Python 3.6+
- Aucune dépendance externe (stdlib uniquement)

## 📄 License

Creative Commons - Part of the GPT-ART project
