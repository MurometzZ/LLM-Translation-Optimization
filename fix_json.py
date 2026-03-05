import json
from pathlib import Path

# target_dir = Path("EN to RU/llama3.1_8b/Crime and Punishment/Chapter_1/results")
target_dir = Path("ratings")

# Canonical key mapping (lowercase → desired capitalization)
KEY_MAP = {
    "meaning": "Meaning",
    "grammar": "Grammar",
    "fluency": "Fluency",
    "lexical choice": "Lexical Choice",
    "lexical_choice": "Lexical Choice",
    "completeness": "Completeness",
}

for file in target_dir.glob("*.txt"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Determine where the rating info is
        if "rating" in data and isinstance(data["rating"], dict):
            rating_source = data["rating"]
        else:
            # Top-level is rating
            rating_source = data

        # Normalize keys
        fixed_rating = {}
        for key, value in rating_source.items():
            # Normalize key by lowercasing and mapping
            normalized_key = KEY_MAP.get(key.lower())
            if normalized_key:
                fixed_rating[normalized_key] = value

        # Build final structure
        data_fixed = {"rating": fixed_rating}

        # Save back to file
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data_fixed, f, indent=2, ensure_ascii=False)

        print(f"Fixed: {file.name}")

    except Exception as e:
        print(f"Error in {file.name}: {e}")
