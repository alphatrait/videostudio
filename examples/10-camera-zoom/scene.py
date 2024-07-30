# 10-camera-zoom/scene.py

# This example demonstrates how to use online assets to create a video with multiple assets in a group.

from videostudio.canvas import Canvas
from videostudio.elements import AssetGroup, Audio
from videostudio.download_script import download_assets

# Download the assets from the internet and save them in a folder called 'project_assets'
asset_urls = [
    'https://chronicle.brightspotcdn.com/c0/c1/3ce97da997936e77d1e4f9050201/online-teaching-gettyimages-958260354.jpg',
    'https://cdn.pixabay.com/photo/2015/09/16/08/55/online-942406_960_720.jpg',
    'https://cdn.pixabay.com/download/audio/2022/10/28/audio_666c4fd39f.mp3'
]

file_path = 'examples/10-camera-zoom/project_assets'

download_assets(asset_urls, file_path)

# Create a canvas
canvas = Canvas(width = 1080, height = 1920, color = (255, 255, 255))

# Initialize the Audio
audio_1 = Audio(canvas, folder_path = file_path, start_asset = None, end_asset = None)

# Initialize the asset group with the audio object
asset_group1 = AssetGroup(canvas, folder_path = file_path, position = ('center', 'center'), start_time = 0, duration = 1, audio = audio_1)

# Add camera effects
canvas.camera("zoom", strength=1.2, speed=1)

# Render the video
canvas.render(output_path = 'examples/10-camera-zoom/output.mp4')