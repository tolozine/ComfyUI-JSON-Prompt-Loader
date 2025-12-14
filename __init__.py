class JSONCleaner:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_text": ("STRING", {"multiline": True, "default": '{\n  "key": "value"\n}'}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("cleaned_text",)
    FUNCTION = "clean_json"
    CATEGORY = "utils/text"

    def clean_json(self, json_text):
        # 仅移除双引号 " 和花括号 { }
        cleaned = json_text.replace('"', '').replace('{', '').replace('}', '')
        return (cleaned,)

NODE_CLASS_MAPPINGS = {
    "JSONCleaner": JSONCleaner
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONCleaner": "JSON Cleaner 🧹"
}