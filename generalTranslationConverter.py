from collections import defaultdict
import os
from openpyxl import Workbook

# Constants
LANGUAGES = ["de", "sk", "en"]
DIRECTORY_BASE = "rawtranslations/yourtranslationfolder"


def create_all_translation_maps():
    """Generate maps for all languages."""
    all_translation_maps = {}
    for lang in LANGUAGES:
        all_translation_maps[lang] = create_translation_map(f"{DIRECTORY_BASE}/{lang}")
    return all_translation_maps


# what does the output of create all translation maps look like?


def find_missing_ids(all_translation_maps):
    """Find missing IDs across all languages."""
    master_map = defaultdict(lambda: defaultdict(list))

    # Initialize master_map with a known language (e.g., 'de')
    base_lang = "de"
    for filename, ids in all_translation_maps[base_lang].items():
        for id_, translation in ids.items():
            master_map[filename][id_].append(translation[0])

    # Check other languages against the base
    for lang in LANGUAGES:
        if lang == base_lang:
            continue
        for filename, ids in all_translation_maps[lang].items():
            for id_, translation in ids.items():
                master_map[filename][id_].append(translation[0])

    # Fill in missing translations with 'N/A'
    for filename, ids in master_map.items():
        for id_, translations in ids.items():
            while len(translations) < len(LANGUAGES):
                translations.append("N/A")

    return master_map


def write_to_excel_multi_lang(master_map):
    """Write to Excel considering multiple languages."""
    wb = Workbook()
    active_ws = wb.active

    if not master_map:
        wb.remove(active_ws)

    for filename, ids in master_map.items():
        if master_map:
            ws = wb.create_sheet(title=filename)
        else:
            ws = active_ws
            ws.title = filename

        # Add headers for language columns
        ws.append(["ID"] + LANGUAGES)

        for id_, translations in ids.items():
            row = [id_] + translations
            ws.append(row)

    wb.save("translations_multi_lang.xlsx")


def create_translation_map(directory):
    translation_map = {}

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".properties"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf8") as file:
                # Read each line in the file
                for line in file:
                    line = line.strip()
                    if "=" in line:
                        # Split the line into ID and translation
                        id_, translation = line.split("=", 1)
                        # Store the ID and translation in the map
                        translation_map.setdefault(filename, {})[id_] = [
                            translation.strip()
                        ]

    return translation_map


# Generate translations for all languages
all_translation_maps = create_all_translation_maps()

# Identify missing translations and create a master map
master_map = find_missing_ids(all_translation_maps)

# Write to Excel
write_to_excel_multi_lang(master_map)
