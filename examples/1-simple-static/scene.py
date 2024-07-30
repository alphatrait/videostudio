# 1-simple-static/scene.py

# This example demonstrates how to create a simple video with static assets.

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets/video.mp4', position=('center', 'center'), start_time=0, duration=3)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets/image.jpg', position=('center', 'center'), start_time=3, duration=3)

# Render and save the video
canvas.render(output_path='examples/1-simple-static/output.mp4')
