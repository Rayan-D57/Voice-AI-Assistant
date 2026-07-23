import asyncio
import edge_tts
import pygame
import os

ARABIC_VOICE = "ar-SA-HamedNeural"
ENGLISH_VOICE = "en-US-AriaNeural"


def is_arabic(text):
    for ch in text:
        if '\u0600' <= ch <= '\u06FF':
            return True
    return False


async def generate_voice(text):

    voice = ARABIC_VOICE if is_arabic(text) else ENGLISH_VOICE

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save("response.mp3")


def speak(text):

    asyncio.run(generate_voice(text))

    pygame.mixer.init()

    pygame.mixer.music.load("response.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    os.remove("response.mp3")