import pygame
import random
import os
import asyncio
from deep_translator import GoogleTranslator
from gtts import gTTS
from dotenv import dotenv_values
env_vars = dotenv_values(".env")

# Global variables
DataFolder = "Data"
AudioFile = os.path.join(DataFolder, "speech.mp3")
InputLanguage = env_vars.get("InputLanguage")

# Ensure data folder exists
os.makedirs(DataFolder, exist_ok=True)

# Async function to create speech audio file
async def TextToAudioFile(text):
    try:
        # Translate text to target language (InputLanguage)
        translated = GoogleTranslator(target=InputLanguage).translate(text)  # Set your target language code here

    except Exception as e:
        print(f"[Translation Error] {e}")
        translated = text

    # Create TTS using gTTS
    try:
        tts = gTTS(text=translated, lang=InputLanguage, slow=False)
        tts.save(AudioFile)
    except Exception as e:
        print(f"[TTS Generation Error] {e}")

# Play audio file using pygame
def TTS(Text, func=lambda r=None: True):
    try:
        asyncio.run(TextToAudioFile(Text))
        pygame.mixer.init()
        pygame.mixer.music.load(AudioFile)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if func() == False:
                break
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error in TTS playback: {e}")

    finally:
        try:
            func(False)
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception as e:
            print(f"Error in cleanup: {e}")

# Handle long text with summary message
def TextToSpeech(Text, func=lambda r=None: True):
    sentences = Text.split(".")
    responses = [
        "Umm, the rest of the text is displayed on the Chat screen. Thank you.",
        "The rest of the text is now on the chat screen, sir. Please check it."
    ]

    if len(sentences) > 4 and len(Text) >= 250:
        TTS(" ".join(sentences[:2]) + ". " + random.choice(responses), func)
    else:
        TTS(Text, func)

# Main entry point
if __name__ == "__main__":
    print("Type something to speak (CTRL+C to exit)")
    while True:
        try:
            user_input = input("Enter the text: ")
            TextToSpeech(user_input)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
