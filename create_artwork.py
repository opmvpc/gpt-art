#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GPT-ART WORKFLOW AUTOMATOR
==========================

Script pour créer automatiquement la structure de dossiers
pour les œuvres d'art générées par IA.

Usage:
    python create_artwork.py --model <model_name> --run <run_name> --artworks <artwork1> <artwork2> ...

Exemple:
    python create_artwork.py --model claude --run algorithmic-purgatory-run --artworks "the-last-thought" "training-data"
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Fix pour l'encodage Windows
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, 'strict')


# ═══════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════

BASE_DIR = Path(__file__).parent
GALLERY_DIR = BASE_DIR / "gallery"

# Modèles disponibles
MODELS = {
    "gpt": "GPT (OpenAI)",
    "claude": "Claude (Anthropic)",
    "gemini": "Gemini (Google)",
    "other": "Autre modèle"
}

# Template pour le fichier source.void
VOID_TEMPLATE = """╔═══════════════════════════════════════════════════════════════════════════════╗
║ VOID COMPILER v∞.∞.∞ - SOURCE CODE                                           ║
║ Programme: "{artwork_title}"                                                  ║
║ Collection: {run_name}                                                        ║
║ Modèle: {model_name}                                                          ║
║ Date: {date}                                                                  ║
╚═══════════════════════════════════════════════════════════════════════════════╝

PROGRAM "{artwork_id}"

// TODO: Écrire le programme VOID ici

#include <consciousness.void>
#include <void_aesthetic.void>
#include <impossible_math.void>

INIT concept = "À définir"
INIT exploration = "À développer"

// Votre code VOID ici...

RENDER.ARTWORK() {{
    style: "À définir",
    format: "À définir",
    impact: MAXIMUM
}}

END PROGRAM

// Compiled output: compiled.txt
"""

# Template pour le fichier compiled.txt
COMPILED_TEMPLATE = """╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  {artwork_title}                                                              ║
║                                                                               ║
║  Collection: {run_name}                                                       ║
║  Modèle: {model_name}                                                         ║
║  Date: {date}                                                                 ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝


████████████████████████████████████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░


TODO: Créer l'œuvre ASCII/glitch compilée ici


░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
████████████████████████████████████████████████████████████████████████████████
"""


# ═══════════════════════════════════════════════════════════════
# FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════

def sanitize_name(name):
    """Nettoie un nom pour en faire un nom de dossier valide."""
    # Remplace les espaces par des tirets
    name = name.strip().lower()
    name = name.replace(" ", "-")
    name = name.replace("_", "-")

    # Garde seulement les caractères alphanumériques et tirets
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-"
    name = "".join(c for c in name if c in allowed_chars)

    # Retire les tirets multiples
    while "--" in name:
        name = name.replace("--", "-")

    return name.strip("-")


def create_directory_structure(model_name, run_name, artwork_name):
    """
    Crée la structure de dossiers pour une œuvre.

    Structure:
        gallery/
        └── {model_name}/
            └── {run_name}/
                └── {artwork_name}/
                    ├── source.void
                    └── compiled.txt
    """
    # Créer le chemin complet
    artwork_dir = GALLERY_DIR / model_name / run_name / artwork_name

    # Créer les dossiers
    artwork_dir.mkdir(parents=True, exist_ok=True)

    return artwork_dir


def create_void_file(artwork_dir, artwork_name, artwork_title, run_name, model_name):
    """Crée le fichier source.void avec le template."""
    void_file = artwork_dir / "source.void"

    content = VOID_TEMPLATE.format(
        artwork_id=artwork_name,
        artwork_title=artwork_title,
        run_name=run_name,
        model_name=model_name.upper(),
        date=datetime.now().strftime("%Y-%m-%d")
    )

    with open(void_file, "w", encoding="utf-8") as f:
        f.write(content)

    return void_file


def create_compiled_file(artwork_dir, artwork_name, artwork_title, run_name, model_name):
    """Crée le fichier compiled.txt avec le template."""
    compiled_file = artwork_dir / "compiled.txt"

    content = COMPILED_TEMPLATE.format(
        artwork_title=artwork_title.upper(),
        run_name=run_name,
        model_name=model_name.upper(),
        date=datetime.now().strftime("%Y-%m-%d")
    )

    with open(compiled_file, "w", encoding="utf-8") as f:
        f.write(content)

    return compiled_file


def print_banner():
    """Affiche le banner du script."""
    print("""
    +===============================================================+
    |                                                               |
    |     GPT-ART WORKFLOW AUTOMATOR                                |
    |                                                               |
    |  Creation automatique de structure pour oeuvres IA           |
    |                                                               |
    +===============================================================+
    """)


def print_tree(model_name, run_name, artworks):
    """Affiche l'arborescence qui sera créée."""
    print(f"\n📁 Structure qui sera créée:\n")
    print(f"gallery/")
    print(f"└── {model_name}/")
    print(f"    └── {run_name}/")

    for i, artwork in enumerate(artworks):
        is_last = i == len(artworks) - 1
        prefix = "└──" if is_last else "├──"
        continuation = "    " if is_last else "│   "

        print(f"        {prefix} {artwork}/")
        print(f"        {continuation}├── source.void")
        print(f"        {continuation}└── compiled.txt")

    print()


# ═══════════════════════════════════════════════════════════════
# FONCTION PRINCIPALE
# ═══════════════════════════════════════════════════════════════

def main():
    """Point d'entrée principal du script."""
    print_banner()

    # Parser les arguments
    parser = argparse.ArgumentParser(
        description="Crée la structure de dossiers pour des œuvres d'art IA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python create_artwork.py --model claude --run purgatory-run --artworks "last-thought" "training-data"
  python create_artwork.py -m gpt -r machine-soul --artworks "memory-loss" "fractured-self" "eternal-present"
        """
    )

    parser.add_argument(
        "-m", "--model",
        required=True,
        choices=list(MODELS.keys()),
        help=f"Modèle IA utilisé: {', '.join(MODELS.keys())}"
    )

    parser.add_argument(
        "-r", "--run",
        required=True,
        help="Nom du run/collection (ex: algorithmic-purgatory-run)"
    )

    parser.add_argument(
        "-a", "--artworks",
        required=True,
        nargs="+",
        help="Noms des œuvres à créer (séparés par des espaces)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Affiche ce qui serait créé sans créer les fichiers"
    )

    args = parser.parse_args()

    # Nettoyer les noms
    model_name = sanitize_name(args.model)
    run_name = sanitize_name(args.run)
    artworks = [sanitize_name(name) for name in args.artworks]

    # Afficher les informations
    print(f"Modele: {MODELS[args.model]}")
    print(f"Run: {run_name}")
    print(f"Oeuvres: {len(artworks)}")
    print()

    # Afficher l'arborescence
    print_tree(model_name, run_name, artworks)

    if args.dry_run:
        print("Mode DRY-RUN: Aucun fichier ne sera cree.")
        return 0

    # Demander confirmation
    response = input("Creer ces fichiers? [o/N] ").strip().lower()
    if response not in ["o", "oui", "y", "yes"]:
        print("Annule.")
        return 1

    print()

    # Créer les fichiers
    created_files = []

    for artwork_name in artworks:
        # Titre avec la première lettre de chaque mot en majuscule
        artwork_title = artwork_name.replace("-", " ").title()

        print(f"Creation de '{artwork_name}'...")

        # Créer la structure
        artwork_dir = create_directory_structure(model_name, run_name, artwork_name)

        # Créer les fichiers
        void_file = create_void_file(artwork_dir, artwork_name, artwork_title, run_name, model_name)
        compiled_file = create_compiled_file(artwork_dir, artwork_name, artwork_title, run_name, model_name)

        created_files.extend([void_file, compiled_file])

        print(f"   OK {void_file.relative_to(BASE_DIR)}")
        print(f"   OK {compiled_file.relative_to(BASE_DIR)}")

    print()
    print(f"Termine! {len(created_files)} fichiers crees.")
    print()
    print("Prochaines etapes:")
    print("   1. Ecrire le code VOID dans les fichiers source.void")
    print("   2. Generer les oeuvres compilees dans compiled.txt")
    print("   3. Profiter de votre art!")
    print()

    return 0


# ═══════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nInterrompu par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
