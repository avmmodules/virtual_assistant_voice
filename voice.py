'''
    Description:
    Change voices of your virtual assistant with Python.

    Author: AlejandroV
    Version: 1.0
    Video: https://youtu.be/UmdisGCHi2s
'''
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

def synthesize_to_speaker(text):
    #Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription="<YOUR_ID_SUBSCRIPTION>", region="<YOUR_REGION>", speech_recognition_language="es-MX")
    
    #In this sample we are using the default speaker 
    #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
    audio_config = AudioOutputConfig(use_default_speaker=True)

    # Note: if only language is set, the default voice of that language is chosen.
    speech_config.speech_synthesis_language = "es-MX"

    # The voice setting will overwrite language setting.
    # The voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = "es-MX-DaliaNeural"
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    synthesizer.speak_text_async(text)

synthesize_to_speaker("¡Suscríbete al canal! @avmmodules")