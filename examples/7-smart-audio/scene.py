# 7-smart-audio/scene.py

# This example demonstrates how to create a simple video and match the transitions with the audio

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition
from videostudio.audio_analyzer import find_top_peaks, find_random_audio

# Create a canvas
canvas = Canvas(width = 1080, height = 1920, color = (255, 255, 255))

# Define assets folder
assets_folder = 'examples/assets'

# Find a random audio from the audio assets
random_audio = find_random_audio(assets_folder)

# Find audio peaks
audio_peaks = find_top_peaks(random_audio, num_peaks_to_select = 3, min_distance_sec = 1)

# Label Audio Peaks
peak1 = audio_peaks[0]
peak2 = audio_peaks[1]
peak3 = audio_peaks[2]

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path = assets_folder, position = ('center', 'center'), start_time = 0, duration = peak1)
static_asset2 = StaticAsset(canvas, folder_path = assets_folder, position = ('center', 'center'), start_time = peak1, duration = peak2)
static_asset3 = StaticAsset(canvas, folder_path = assets_folder, position = ('center', 'center'), start_time = peak2, duration = peak3)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect = 'crossfade', duration = 0.5)
transition = Transition(canvas, static_asset2, static_asset3, effect = 'crossfade', duration = 0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path = random_audio, start_asset = static_asset1, end_asset = static_asset3, fade_in_duration = 2, fade_out_duration = 2)

# Render the video
canvas.render(output_path = 'examples/7-smart-audio/output.mp4')