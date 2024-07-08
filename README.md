# videostudio

Video Studio is a versatile video and audio processing package designed for creating, editing, and managing multimedia content. It leverages popular libraries such as MoviePy, Pydub, NumPy, and Scipy to provide powerful tools for handling audio and video files.

</br>

## Features

- **Video Editing**: Combine videos, add transitions, overlay text, and more.
- **Audio Processing**: Trim, concatenate, fade in/out, and manipulate audio files.
- **Speech Recognition**: Convert speech to text using speech recognition.
- **Image Processing**: Overlay text on images and create dynamic visual content.
- **Random File Selection**: Automatically select random files from directories for processing.

</br>

## Installation

You can install Video Studio from PyPI:

```bash
pip install videostudio
```
</br>

## Simple Static Example

This example demonstrates how to create a simple video with static assets.

```python

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets/video.mp4', position=('center', 'center'), start_time=0, duration=3)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets/image.jpg', position=('center', 'center'), start_time=3, duration=3)

# Render and save the video
canvas.render(output_path='examples/1-simple-static/output.mp4')

```

</br>

## Simple Transition Example

This example demonstrates how to add a simple transition between two static assets.

```python

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

```

</br>

## Simple Audio Example

This example demonstrates how to create a simple video with static assets, transitions, and audio.

```python

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets/video.mp4', position=('center', 'center'), start_time=0, duration=3)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets/image.jpg', position=('center', 'center'), start_time=3, duration=3)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path='examples/assets/audio.wav', start_asset=static_asset1, end_asset=static_asset2, fade_in_duration=1, fade_out_duration=1)

# Render the video
canvas.render(output_path='examples/3-simple-audio/output.mp4')

```

</br>

## Audio Fade Example

This example demonstrates how to create a simple video with static assets, transitions, audio, and audio fades.

```python

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
canvas.render(output_path='examples/4-audio-fade/output.mp4')

```

</br>

## Asset Pool Example

This example demonstrates how to create a simple video with static assets, transitions, audio, and audio fades.

```python

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=0, duration=2)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=2, duration=1)
static_asset3 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=3, duration=2)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)
transition = Transition(canvas, static_asset2, static_asset3, effect='crossfade', duration=0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path='examples/assets/audio.wav', start_asset=static_asset1, end_asset=static_asset3, fade_in_duration=2, fade_out_duration=2)

# Render the video
canvas.render(output_path='examples/5-asset-pool/output4.mp4')

```
</br>

## Audio Pool Example

This example demonstrates how to create a simple video from a pool of static assets with audio.


```python

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=0, duration=2)
static_asset2 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=2, duration=1)
static_asset3 = StaticAsset(canvas, folder_path='examples/assets', position=('center', 'center'), start_time=3, duration=2)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)
transition = Transition(canvas, static_asset2, static_asset3, effect='crossfade', duration=0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path='examples/assets', start_asset=static_asset1, end_asset=static_asset3, fade_in_duration=2, fade_out_duration=2)

# Render the video
canvas.render(output_path='examples/6-audio-pool/output3.mp4')

```
</br>

## Smart Audio Example

This example demonstrates how to create a simple video and match the transitions with the audio.


```python

from videostudio.canvas import Canvas
from videostudio.elements import StaticAsset, Audio
from videostudio.transitions import Transition
from videostudio.audio_analyzer import find_top_peaks, find_random_audio

# Create a canvas
canvas = Canvas(width=1080, height=1920, color=(255, 255, 255))

# Define assets folder
assets_folder = 'examples/assets'

# Find a random audio from the audio assets
random_audio = find_random_audio(assets_folder)

# Find audio peaks
audio_peaks = find_top_peaks(random_audio, num_peaks_to_select=3, min_distance_sec=1)

# Label Audio Peaks
peak1 = audio_peaks[0]
peak2 = audio_peaks[1]
peak3 = audio_peaks[2]

# Add static asset (automatically added to canvas)
static_asset1 = StaticAsset(canvas, folder_path=assets_folder, position=('center', 'center'), start_time=0, duration=peak1)
static_asset2 = StaticAsset(canvas, folder_path=assets_folder, position=('center', 'center'), start_time=peak1, duration=peak2)
static_asset3 = StaticAsset(canvas, folder_path=assets_folder, position=('center', 'center'), start_time=peak2, duration=peak3)

# Adding transition
transition = Transition(canvas, static_asset1, static_asset2, effect='crossfade', duration=0.5)
transition = Transition(canvas, static_asset2, static_asset3, effect='crossfade', duration=0.5)

# Add audio aligned with static_asset1 and static_asset2
audio_1 = Audio(canvas, folder_path=random_audio, start_asset=static_asset1, end_asset=static_asset3, fade_in_duration=2, fade_out_duration=2)

# Render the video
canvas.render(output_path='examples/7-smart-audio/output.mp4')

```

</br></br>
More coming soon...# videostudio
# videostudio
# videostudio
