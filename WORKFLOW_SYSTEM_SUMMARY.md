# 📦 Système de Workflow GPT-ART - Récapitulatif

## ✅ Fichiers Créés

### 1. Script Principal

- **`create_artwork.py`** - Script Python d'automatisation
  - Crée automatiquement la structure de dossiers
  - Templates pré-remplis pour source.void et compiled.txt
  - Support multi-modèles (GPT, Claude, Gemini, etc.)
  - Mode dry-run pour preview
  - Compatible Windows avec fix d'encodage

### 2. Documentation

- **`WORKFLOW_GUIDE.md`** - Guide complet pour l'utilisateur

  - Syntaxe et exemples
  - Options disponibles
  - Workflow recommandé

- **`AI_WORKFLOW_GUIDE.md`** - Guide pour l'IA

  - Quand et comment utiliser le script
  - Exemples concrets
  - Checklist et bonnes pratiques

- **`README.md`** - Mis à jour avec:
  - Section Quick Start
  - Documentation du script
  - Structure organisée par modèle

### 3. Scripts d'Aide Rapide

- **`quick-help.sh`** - Aide rapide (Linux/Mac)
- **`quick-help.bat`** - Aide rapide (Windows)

## 🎯 Usage du Système

### Pour l'Utilisateur

```bash
# Créer une nouvelle collection
python create_artwork.py -m claude -r ma-collection -a "oeuvre-1" "oeuvre-2"

# Preview avant création
python create_artwork.py -m claude -r test -a "piece" --dry-run

# Aide
python create_artwork.py --help
./quick-help.bat  # Windows
./quick-help.sh   # Linux/Mac
```

### Pour l'IA (Claude)

1. **Avant de créer des œuvres**, demander à l'utilisateur:

   ```
   Pour créer cette collection, exécutez d'abord:

   python create_artwork.py -m claude -r nom-collection -a "oeuvre-1" "oeuvre-2"
   ```

2. **Après confirmation**, créer le contenu:
   ```python
   create_file("gallery/claude/nom-collection/oeuvre-1/source.void", ...)
   create_file("gallery/claude/nom-collection/oeuvre-1/compiled.txt", ...)
   ```

## 📁 Structure Générée

```
gallery/
└── {model}/              # claude, gpt, gemini, other
    └── {run-name}/       # nom de la collection
        └── {artwork}/    # nom de l'œuvre
            ├── source.void      # Programme VOID
            └── compiled.txt     # Œuvre compilée
```

## 🔧 Fonctionnalités

- ✅ Création automatique de l'arborescence
- ✅ Templates pré-remplis avec métadonnées
- ✅ Nettoyage automatique des noms (espaces → tirets)
- ✅ Affichage d'arborescence avant création
- ✅ Confirmation interactive
- ✅ Mode dry-run
- ✅ Support multi-modèles
- ✅ Compatible Windows (encodage UTF-8)
- ✅ Documentation complète

## 📝 Conventions de Nommage

### Modèles

- `claude` - Claude (Anthropic)
- `gpt` - GPT (OpenAI)
- `gemini` - Gemini (Google)
- `other` - Autres modèles

### Collections (runs)

- Format: `kebab-case` (minuscules-avec-tirets)
- Exemples: `algorithmic-purgatory-run`, `machine-soul-run`, `cosmic-horror`

### Œuvres (artworks)

- Format: `kebab-case`
- Numérotées optionnel: `01-name`, `14-next-piece`
- Exemples: `the-last-thought`, `memory-loss`, `14-void-gaze`

## 🎨 Workflow Complet - Exemple

```bash
# 1. L'utilisateur crée la structure
python create_artwork.py -m claude -r dark-poems -a "void-whispers" "digital-tears"

# 2. Résultat:
gallery/claude/dark-poems/
├── void-whispers/
│   ├── source.void      # Template créé
│   └── compiled.txt     # Template créé
└── digital-tears/
    ├── source.void
    └── compiled.txt

# 3. L'IA remplit les fichiers avec le contenu artistique
# 4. L'utilisateur admire les œuvres! 🎨
```

## 🚀 Prochaines Étapes Possibles

- [ ] Commande pour lister toutes les collections
- [ ] Génération automatique d'index/README par collection
- [ ] Export en formats imprimables (PDF, PNG)
- [ ] Galerie web statique générée automatiquement
- [ ] Statistiques (nombre d'œuvres par modèle, etc.)

---

**Statut**: ✅ Système opérationnel et testé
**Date**: 2025-11-18
**Version**: 1.0
