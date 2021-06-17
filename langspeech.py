import pandas
from ibm_cloud_sdk_core import authenticators
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

#api keys and url for the API 
url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/73880520-2f82-4b29-b526-49f550065055"
iam_apikey_s2t = "vm-9ddtrfMPbpxnEKs1ZX_OqZfSu_82PdVYDbJtQMX5w"


#Giving the above variables as inputs for the API calling
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

#write this in terminal to download the audio file
#wget -O PolynomialRegressionandPipelines.mp3  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3


#Giving the above file name as an argument for the Speech to text API
filename = "PolynomialRegressionandPipelines.mp3"
with open(filename,mode='rb') as wav:
    response = s2t.recognize(audio=wav,content_type="audio/mp3")
print(response.result)

#Normalising the output Dictionary we got from above
from pandas import json_normalize
print(json_normalize(response.result['results'],"alternatives"))
print(response)
#using the first result for our program by making an object for it
recognised_text = response.result['results'][0]["alternatives"][0]["transcript"]
print(recognised_text)

#calling the Language translator API 
from ibm_watson import LanguageTranslatorV3

#Again making variables for api key and url for using them in API, the API uses version as Date format, be carful with it. Check Documentation for updation of anything
apikey_lt = "2-ro1dubDFqtMoAEnbCdXaTrisGYKqZFwclIHt2GEH0R"
url_lt = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/216bdce0-9aa4-422a-9ca0-635e406da18b"
version_lt = "2018-05-01"

#using the above variables in the API
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

#again normalising the json file for better visuals 
from pandas import json_normalize
print(json_normalize(language_translator.list_identifiable_languages().get_result(),"languages"))

#translation process 
translation_response = language_translator.translate(text = recognised_text,model_id = 'en-ur')
print(translation_response)

#printing the translation output from above
translation = translation_response.get_result()
print(translation)

#The above result is obtained as a Dictionary, converting it to a Single string
urdu_translation = translation['translations'][0]['translation']
print(urdu_translation)

#the above result can be converted back and forth by repeating the conversion process and writing "ur-en".








