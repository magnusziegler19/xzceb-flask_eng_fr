import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
### english to french translation
    french_text_json = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = french_text_json["translations"][0]['translation']

    return french_text
def french_to_english(french_text):
### french to english translation
    english_text_json = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    # print(json.dumps(frenchText_json, indent=2, ensure_ascii=False)) # debug
    english_text = english_text_json["translations"][0]['translation']

    return english_text
