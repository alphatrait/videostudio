# framework/manipulators.py

import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont

class AudioExtractor:
    @staticmethod
    def extract_audio(video_path, output_format='wav'):
        audio_path = video_path.replace('.mp4', f'.{output_format}')
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        return audio_path

class SpeechToText:
    @staticmethod
    def speech_to_text(audio_path, language='en-US'):
        recognizer = sr.Recognizer()
        audio = AudioSegment.from_file(audio_path)
        audio.export("temp_audio.wav", format="wav")
        with sr.AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language=language)
        os.remove("temp_audio.wav")
        return text

class ImageGenerator:
    @staticmethod
    def generate_image_from_text(text, width=640, height=480, bg_color=(73, 109, 137), text_color=(255, 255, 0)):
        img = Image.new('RGB', (width, height), color=bg_color)
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((10, 10), text, font=font, fill=text_color)
        image_path = 'generated_image.png'
        img.save(image_path)
        return image_path

# Registry for manipulators
MANIPULATORS = {
    'audio_extractor': AudioExtractor.extract_audio,
    'speech_to_text': SpeechToText.speech_to_text,
    'image_generator': ImageGenerator.generate_image_from_text,
}

def register_manipulator(name, function):
    MANIPULATORS[name] = function
