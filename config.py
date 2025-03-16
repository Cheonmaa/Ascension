from typing import Dict
import os
import json

FPS = 60
MAX_TEAM_SIZE = 5
class LanguageManager:
    def __init__(self, default_language: str = "en", lang_dir: str = "languages"):
        self.languages: Dict[str, Dict[str, str]] = {}
        self.default_language = default_language
        self.lang_dir = lang_dir
        self._load_languages()

    def translate_class_phrases(self, obj, language: str):
        """Automatically translate phrases in an object's attributes."""
        for attr_name in dir(obj):
            if not attr_name.startswith("_"):  # Skip private/protected attributes
                attr_value = getattr(obj, attr_name)
                if isinstance(attr_value, str):  # Only translate string attributes
                    setattr(obj, attr_name, self.get_phrase(language, attr_value))

class ExampleClass:
    welcome_message = "welcome"
    goodbye_message = "goodbye"

language_manager = LanguageManager()
example = ExampleClass()

language_manager.translate_class_phrases(example, "fr")
print(example.welcome_message)
print(example.goodbye_message)