# Salesforce B2C-Translation Converter🌍🔁

## Overview
The Salesforce B2C-Translation Converter is a Python-based tool designed to streamline the translation process for Salesforce B2C code. It efficiently converts `.properties` translation files into a readable Excel format, addresses missing translation IDs, and leverages DeepL API for accurate and consistent translations across multiple languages.

## Features
- **Translation File Conversion**: Converts `.properties` files into an easily readable Excel format.
- **Missing ID Correction**: Automatically identifies and corrects missing IDs across different languages.
- **Multi-language Support**: Works with multiple languages.
- **DeepL Integration**: Utilizes DeepL API for high-quality translations.
- **Bidirectional Conversion**: Converts from `.properties` to Excel and back, maintaining the integrity of the original files.

## Benefits
- **Efficiency**: Significantly reduces manual effort in managing translations.
- **Accuracy**: Ensures consistent and accurate translations across different languages.
- **Scalability**: Easily adaptable to include more languages or handle larger translation files.
- **Simplicity**: User-friendly process requiring minimal technical knowledge.

## Prerequisites
- Python 3.x
- `openpyxl` Python package
- DeepL API key (for translation)

## Installation
1. Clone this repository.
2. Install required Python packages: 
pip install openpyxl requests
3. Insert your DeepL API key in the `translatorScript.py`.

## Usage
1. Place your `.properties` translation files in the `rawtranslations/yourtranslationfolder` directory.
2. Run `generalTranslationConverter.py` to convert `.properties` files to Excel and identify missing IDs.
3. Execute `translatorScript.py` to translate missing IDs using DeepL and convert back to `.properties` format.

## Example
```python
from generalTranslationConverter import create_all_translation_maps, find_missing_ids, write_to_excel_multi_lang
# Generate translations for all languages
all_translation_maps = create_all_translation_maps()

# Identify missing translations and create a master map
master_map = find_missing_ids(all_translation_maps)

# Write to Excel
write_to_excel_multi_lang(master_map)
```

## Contributing
Contributions are welcome! If you have suggestions or want to improve the tool, feel free to fork the repository and submit a pull request.

## License
Distributed under the MIT License. See LICENSE for more information.
