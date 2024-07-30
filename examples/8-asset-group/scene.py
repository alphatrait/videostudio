# 8-asset-group/scene.py

# This example demonstrates how to use asset groups to create a video with multiple assets in a group.

from videostudio.canvas import Canvas
from videostudio.elements import AssetGroup, Audio

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Initialize the Audio
audio_1 = Audio(canvas, folder_path='examples/assets/', start_asset=None, end_asset=None)

# Initialize the asset group with the audio object
asset_group1 = AssetGroup(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=0, duration=2, audio=audio_1)

# Render the video
canvas.render(output_path='examples/8-asset-group/output.mp4')