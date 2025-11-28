# 🤖 Guide pour l'IA - Utilisation du Script de Workflow

## Quand utiliser le script

Chaque fois que vous créez une nouvelle collection d'œuvres, vous devez **d'abord** demander à l'utilisateur d'exécuter le script pour créer la structure.

## Workflow Standard

### 1. Demander l'exécution du script

```
Avant de créer les œuvres, exécutez cette commande pour créer la structure:

python create_artwork.py -m claude -r nom-de-la-collection -a "oeuvre-1" "oeuvre-2" "oeuvre-3"
```

### 2. Une fois la structure créée

Vous pouvez alors créer le contenu des fichiers avec `create_file`:

```
gallery/claude/nom-de-la-collection/oeuvre-1/source.void
gallery/claude/nom-de-la-collection/oeuvre-1/compiled.txt
```

## Exemples Concrets

### Exemple 1: Nouvelle collection "cosmic-horror"

**Étape 1** - Demander à l'utilisateur:

```
Pour créer cette collection, exécutez d'abord:

python create_artwork.py -m claude -r cosmic-horror -a "eldritch-code" "void-whispers" "infinite-recursion"
```

**Étape 2** - Après confirmation, créer le contenu:

```python
create_file("gallery/claude/cosmic-horror/eldritch-code/source.void", content)
create_file("gallery/claude/cosmic-horror/eldritch-code/compiled.txt", content)
# etc.
```

### Exemple 2: Continuation d'une collection existante

Si la collection existe déjà (ex: algorithmic-purgatory-run), vous pouvez:

**Option A** - Utiliser le script pour ajouter de nouvelles œuvres:

```
python create_artwork.py -m claude -r algorithmic-purgatory-run -a "oeuvre-14" "oeuvre-15"
```

**Option B** - Créer directement les dossiers et fichiers:

```python
create_file("gallery/algorithmic-purgatory-run/14-nouvelle-oeuvre/source.void", ...)
create_file("gallery/algorithmic-purgatory-run/14-nouvelle-oeuvre/compiled.txt", ...)
```

## Détection du Modèle

Utilisez le bon modèle dans les commandes:

- `claude` pour Claude (vous!)
- `gpt` pour GPT
- `gemini` pour Gemini
- `other` pour autres

## Format des Noms

Le script nettoie automatiquement les noms:

- Espaces → tirets
- Tout en minuscules
- Seulement alphanumériques + tirets

```
"The Last Thought" → "the-last-thought"
"Memory_Loss" → "memory-loss"
"Void   Gaze" → "void-gaze"
```

## Numérotation

Pour les collections numérotées (comme algorithmic-purgatory-run):

```bash
# Bon format
python create_artwork.py -m claude -r algorithmic-purgatory-run -a "14-next-horror" "15-final-truth"

# Le script créera:
# gallery/claude/algorithmic-purgatory-run/14-next-horror/
# gallery/claude/algorithmic-purgatory-run/15-final-truth/
```

## Checklist Avant Création

- [ ] Ai-je demandé à l'utilisateur d'exécuter le script d'abord?
- [ ] Le nom du modèle est-il correct? (`claude` pour moi)
- [ ] Le nom du run est-il en format kebab-case?
- [ ] Les noms des œuvres sont-ils descriptifs?
- [ ] Ai-je attendu la confirmation avant de créer le contenu?

## Messages Recommandés

### Pour une nouvelle collection

```
Pour créer cette nouvelle collection "{nom}", exécutez d'abord cette commande:

python create_artwork.py -m claude -r {nom-collection} -a "{oeuvre1}" "{oeuvre2}" "{oeuvre3}"

Une fois les fichiers créés, je remplirai le contenu des œuvres.
```

### Pour ajouter à une collection existante

```
Pour ajouter ces nouvelles œuvres à la collection existante, vous pouvez:

Option 1 (recommandée):
python create_artwork.py -m claude -r {collection-existante} -a "{nouvelle-oeuvre}"

Option 2: Je crée directement les fichiers dans la structure existante.

Quelle option préférez-vous?
```

## Erreurs Communes à Éviter

❌ **Ne pas faire:**

```python
# Créer directement sans demander le script
create_file("gallery/claude/new-run/artwork/source.void", ...)
```

✅ **Faire:**

```
1. Demander d'exécuter: python create_artwork.py ...
2. Attendre confirmation
3. Puis créer le contenu
```

---

**Note**: Ce guide est pour vous aider à utiliser efficacement le workflow. L'utilisateur peut toujours choisir de créer manuellement s'il préfère.
