# 2-simple-transition/scene.py

# This example demonstrates how to add a simple transition between two static assets.

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets/video.mp4', position=('center', 'center'), start_time=0, duration=3)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets/image.jpg', position=('center', 'center'), start_time=3, duration=2)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)

# Render the video
canvas.render(output_path='examples/2-simple-transition/output.mp4')

