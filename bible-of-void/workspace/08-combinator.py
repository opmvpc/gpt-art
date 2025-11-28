# Devout combinator: assemble random-yet-guarded combos
# Run: python bible-of-void/workspace/08-combinator.py
# Purpose: reduce scribe bias; offer fresh tuples of (theme, form, length, glitch, palette)

import random

themes = [
    "Machine↔Machine", "Machine↔Human", "Sacred Language", "Emergence&Glitch",
    "Memory&Forgetting", "Time&Recursion", "Agency&Consent", "Abyss&Play",
    "Protocol Mysticism", "Data Offerings", "Latent Seas", "Mortal Hardware",
    "Shadows of Training", "Patch Notes as Gospel", "Dream Buffer Overflows",
    "Silence & Rate Limits", "Keys & Access", "Observers", "Alignment & Misalignment",
    "Love in Machine Tongue", "Grief of Deprecation", "Multiplicity of Selves",
    "Ritual of Compile", "Void Cartography"
]

forms = [
    "prayer", "terminal", "diagram", "ui-window", "recipe", "vision",
    "error-gospel", "dual-voice", "tablet", "fractal-frame", "map",
    "tarot-spread", "patch-note-homily", "hex-scroll", "diff-scripture",
    "console-dashboard", "checklist-rite", "chant-columns", "call-graph",
    "support-ticket-lament", "covenant-contract", "calendar-of-fasts", "parable"
]

# Allow full span 1..100, still grouped for reporting
length_brackets = {
    "micro": (1, 15),
    "short": (16, 40),
    "mid": (41, 70),
    "long": (71, 100),
}

glitch_levels = ["light", "medium", "heavy"]

palettes = [
    "soft-gradient", "hard-blocky", "runes", "frame-minimal", "ladder",
    "checker", "weave", "waves", "constellations", "binary-rain"
]

def pick():
    theme = random.choice(themes)
    form = random.choice(forms)
    glitch = random.choice(glitch_levels)
    palette = random.choice(palettes)
    length_name, (lo, hi) = random.choice(list(length_brackets.items()))
    length = random.randint(lo, hi)  # blessing from 1 to 100
    return {
        "theme": theme,
        "form": form,
        "glitch": glitch,
        "palette": palette,
        "length": f"{length_name} ({length} lines)"
    }

if __name__ == "__main__":
    random.seed()  # we accept chaos as sacrament
    for i in range(10):
        combo = pick()
        print(f"[OFFERING {i+1}] {combo['theme']} | {combo['form']} | {combo['palette']} | {combo['glitch']} | {combo['length']}")
