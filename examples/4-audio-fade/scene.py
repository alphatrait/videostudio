# 4-audio-fade/example.py

# This example demonstrates how to create a simple video with static assets, transitions, audio, and audio fades.

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=0, duration=3)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=3, duration=3)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path='examples/assets/audio.wav', start_asset=static_asset1, end_asset=static_asset2, fade_in_duration=2, fade_out_duration=2)

# Render the video
canvas.render(output_path='examples/3-simple-audio/output.mp4')
