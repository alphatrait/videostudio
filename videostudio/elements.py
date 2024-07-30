# videostudio/elements.py

import os
import random
from moviepy.editor import ImageClip, VideoFileClip, TextClip, AudioFileClip
from .manipulators import MANIPULATORS

class TextElement:
    def __init__(self, canvas, text, fontsize, color, position, start_time, end_time):
        self.text = text
        self.fontsize = fontsize
        self.color = color
        self.position = position
        self.start_time = start_time
        self.end_time = end_time

        canvas.add_element(self)

    def create_clip(self):
        txt_clip = TextClip(self.text, fontsize=self.fontsize, color=self.color)
        txt_clip = txt_clip.set_position(self.position).set_start(self.start_time).set_end(self.end_time)
        return txt_clip


class AssetGroup:
    def __init__(self, canvas, folder_path, position, start_time, duration, audio=None):
        self.canvas = canvas
        self.folder_path = folder_path
        self.position = position
        self.start_time = start_time
        self.duration = duration
        self.assets = []
        self.audio = audio

        if self.audio and self.audio.audio_duration > 0:
            self.populate_assets(canvas, self.audio.audio_duration)

    def populate_assets(self, canvas, audio_duration):
        self.audio_duration = audio_duration
        self._populate_assets(canvas)
        self.update_audio()

    def _populate_assets(self, canvas):
        files = self._get_files()
        current_time = self.start_time
        total_duration = 0
        for file_path in files:
            if total_duration >= self.audio_duration:
                break
            asset = StaticAsset(canvas, file_path, self.position, current_time, duration=self.duration)
            self.assets.append(asset)
            current_time += self.duration
            total_duration += self.duration

    def update_audio(self):
        if self.assets and self.audio:
            self.audio.start_asset = self.assets[0]
            self.audio.end_asset = self.assets[-1]
            self.audio.start_time = self.audio.start_asset.start_time
            self.audio.end_time = self.audio.end_asset.end_time

    def _get_files(self):
        files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov', '.avi'))]
        random.shuffle(files)
        return files




class StaticAsset:
    def __init__(self, canvas, folder_path, position, start_time, end_time=None, duration=None):
        self.folder_path = folder_path
        self.position = position
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

        if os.path.isfile(folder_path):
            self.path = folder_path
        elif os.path.isdir(folder_path):
            self.path = self._select_random_file()
        else:
            raise FileNotFoundError(f"No such file or directory: '{folder_path}'")

        self.is_image = self.path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

        if self.end_time is None:
            if self.duration is not None:
                self.end_time = self.start_time + self.duration
            elif self.is_image:
                self.end_time = self.start_time + 2
            else:
                self.end_time = self.start_time + VideoFileClip(self.path).duration

        canvas.add_element(self)

    def _select_random_file(self):
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov', '.avi'))]
        if not files:
            raise FileNotFoundError(f"No files found in directory: '{self.folder_path}'")
        return os.path.join(self.folder_path, random.choice(files))

    def create_clip(self):
        if self.is_image:
            return self._create_image_clip()
        else:
            return self._create_video_clip()

    def _create_image_clip(self):
        img_clip = ImageClip(self.path)
        img_clip = img_clip.set_position(self.position).set_start(self.start_time).set_end(self.end_time)
        return img_clip

    def _create_video_clip(self):
        vid_clip = VideoFileClip(self.path)
        vid_clip = vid_clip.set_position(self.position).set_start(self.start_time).set_end(self.end_time).set_fps(24)
        return vid_clip

class DynamicAsset:
    def __init__(self, canvas, static_asset, manipulators, position, start_time, end_time):
        self.static_asset = static_asset
        self.manipulators = manipulators
        self.position = position
        self.start_time = start_time
        self.end_time = end_time

        self.dynamic_path = self._process_static_asset()

        if self.end_time is None:
            self.end_time = self.start_time + 2

        canvas.add_element(self)

    def _process_static_asset(self):
        result = self.static_asset.path
        for manipulator, params in self.manipulators:
            result = MANIPULATORS[manipulator](result, **params)
        return result

    def create_clip(self):
        img_clip = ImageClip(self.dynamic_path)
        img_clip = img_clip.set_position(self.position).set_start(self.start_time).set_end(self.end_time)
        return img_clip
    

class Audio:
    def __init__(self, canvas, folder_path, start_asset, end_asset, fade_in_duration=0, fade_out_duration=0):
        self.folder_path = folder_path
        self.start_time = start_asset.start_time if start_asset else 0
        self.end_time = end_asset.end_time if end_asset else float('inf')
        self.fade_in_duration = fade_in_duration
        self.fade_out_duration = fade_out_duration

        self.path = self._select_random_file(folder_path)
        self.audio_clip = AudioFileClip(self.path)
        self.audio_duration = self.audio_clip.duration

        if start_asset and end_asset:
            if self.audio_duration < (self.end_time - self.start_time):
                print(f"Warning: The audio file is shorter than the visual duration. The audio will play for {self.audio_duration} seconds.")
                self.end_time = self.start_time + self.audio_duration

        canvas.add_audio(self)
    
    def _select_random_file(self, folder_path):
        if os.path.isfile(folder_path):
            return folder_path
        elif os.path.isdir(folder_path):
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.mp3', '.wav', '.ogg', '.flac'))]
            if not files:
                raise FileNotFoundError(f"No audio files found in directory: '{folder_path}'")
            return os.path.join(folder_path, random.choice(files))
        else:
            raise FileNotFoundError(f"No such file or directory: '{folder_path}'")


    def create_clip(self):
        audio_clip = self.audio_clip.set_start(self.start_time).set_end(self.end_time)
        if self.fade_in_duration > 0:
            audio_clip = audio_clip.audio_fadein(self.fade_in_duration)
        if self.fade_out_duration > 0:
            audio_clip = audio_clip.audio_fadeout(self.fade_out_duration)
        return audio_clip
