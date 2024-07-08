# framework/canvas.py

from moviepy.editor import ColorClip, CompositeVideoClip, concatenate_audioclips

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

    def add_element(self, element):
        self.elements.append(element)

    def add_transition(self, transition):
        self.transitions.append(transition)

    def add_audio(self, audio):
        self.audios.append(audio)

    def get_duration(self):
        return max((el.end_time for el in self.elements if hasattr(el, 'end_time')), default=0)

    def render(self, output_path):
        duration = self.get_duration()
        self.canvas = self.canvas.set_duration(duration)
        clips = [self.canvas] + [el.create_clip() for el in self.elements]

        # Apply transitions
        for transition in self.transitions:
            clips = transition.apply_transition(clips)

        video = CompositeVideoClip(clips).set_duration(duration).set_fps(self.fps)
        
        # Add audio
        if self.audios:
            audio_clips = [audio.create_clip() for audio in self.audios]
            final_audio = concatenate_audioclips(audio_clips).set_duration(duration)
            video = video.set_audio(final_audio)

        video.write_videofile(output_path, codec='libx264', fps=self.fps)
