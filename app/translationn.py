from googletrans import Translator

def translating(text):
    translator = Translator()
    data = {}
    languages = ['ru', 'uz']  # List of target languages
    try:
        for lang in languages:
            translation = translator.translate(text, dest=lang)
            data[lang] = translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        data = {lang: f"Translation failed for {lang}" for lang in languages}
    return data


