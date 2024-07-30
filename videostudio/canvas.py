# videostudio/canvas.py

from moviepy.editor import ColorClip, CompositeVideoClip, concatenate_audioclips
from moviepy.video.fx.all import resize

class Canvas:
    def __init__(self, width, height, color=(0, 0, 0), fps=24):
        self.width = width
        self.height = height
        self.color = color
        self.fps = fps
        self.elements = []
        self.transitions = []
        self.audios = []
        self.canvas = ColorClip(size=(width, height), color=color, duration=1).set_fps(fps)
        self.zoom_effects = []

    def add_element(self, element):
        self.elements.append(element)

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_audio(self, audio):
        self.audios.append(audio)

    def get_duration(self):
        return max((el.end_time for el in self.elements if hasattr(el, 'end_time')), default=0)

    def get_audio_duration(self):
        if not self.audios:
            return 0  # Return 0 or default duration if no audio is added
        return max(audio.audio_duration for audio in self.audios)

    def camera(self, effect_type, strength=1.2, speed=1):
        if effect_type == "zoom":
            for i, element in enumerate(self.elements):
                if i % 2 == 0:
                    # Zoom in
                    self.zoom_effects.append((element, 'in', strength, speed))
                else:
                    # Zoom out
                    self.zoom_effects.append((element, 'out', strength, speed))

    def apply_zoom_effects(self, clip, zoom_type, strength, speed):
        if zoom_type == 'in':
            return clip.resize(lambda t: 1 + (strength - 1) * (t / speed))
        else:
            return clip.resize(lambda t: strength - (strength - 1) * (t / speed))

    def render(self, output_path):
        video_duration = self.get_duration()
        audio_duration = self.get_audio_duration()

        # Loop audio if video duration is longer than audio duration
        if audio_duration > 0 and video_duration > audio_duration:
            loops_required = int(video_duration / audio_duration) + 1
            for audio in self.audios:
                audio_clip = audio.audio_clip
                audio_clip = concatenate_audioclips([audio_clip] * loops_required)
                audio.audio_clip = audio_clip.set_duration(video_duration)

        # Compile clips
        self.canvas = self.canvas.set_duration(video_duration)
        clips = [self.canvas] + [el.create_clip() for el in self.elements]
        video = CompositeVideoClip(clips).set_duration(video_duration).set_fps(self.fps)

        # Apply zoom effects
        for element, zoom_type, strength, speed in self.zoom_effects:
            element_clip = element.create_clip()
            zoomed_clip = self.apply_zoom_effects(element_clip, zoom_type, strength, speed)
            video = CompositeVideoClip([video, zoomed_clip.set_start(element.start_time).set_end(element.end_time)])

        # Add audio if available
        if self.audios:
            audio_clips = [audio.create_clip() for audio in self.audios]
            final_audio = concatenate_audioclips(audio_clips).set_duration(video_duration)
            video = video.set_audio(final_audio)

        video.write_videofile(output_path, codec='libx264', fps=self.fps)
