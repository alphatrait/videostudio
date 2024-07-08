# framework/audio_analyzer.py

from pydub import AudioSegment
import numpy as np
from scipy.signal import find_peaks
import os
import random

def find_top_peaks(filename, num_peaks_to_select=1, min_distance_sec=0.3):
    # Load the audio file with pydub, which supports various formats
    audio = AudioSegment.from_file(filename)
    # Convert audio to numpy array
    audio_data = np.array(audio.get_array_of_samples())

    # If stereo, average the channels
    if audio.channels == 2:
        audio_data = np.mean(audio_data.reshape(-1, 2), axis=1)

    sample_rate = audio.frame_rate
    # Calculate minimum distance in frames
    min_distance_frames = int(min_distance_sec * sample_rate)

    # Finding all peaks
    all_peak_indices, _ = find_peaks(np.abs(audio_data), distance=min_distance_frames, height=0)

    peak_times = []

    # Sort and select peaks
    if all_peak_indices.size > 0:
        sorted_peaks = sorted(all_peak_indices, key=lambda x: np.abs(audio_data[x]), reverse=True)
        top_peaks = sorted_peaks[:num_peaks_to_select]

        # Collect peak info
        peaks_info = [(round(index / sample_rate, 2), audio_data[index]) for index in top_peaks]
        peaks_info.sort(key=lambda x: x[1])  # Sort by amplitude

        # Print peak info
        for time, amplitude in peaks_info:
            print(f"Peak at {time:.2f} seconds with amplitude {amplitude}")
            peak_times.append(time)
        
        peak_times.sort()

        print (peak_times)
        return peak_times

    return []  # Return empty list if no peaks found


def find_random_audio(directory):
    # List all files in the directory
    all_files = os.listdir(directory)
    
    # Filter for audio files assuming common audio file extensions
    audio_files = [file for file in all_files if file.endswith(('.mp3', '.wav', '.aac', '.flac'))]
    
    # Select a random audio file
    if audio_files:
        random_audio = random.choice(audio_files)
        print(f"Randomly selected audio file: {random_audio}")
        return os.path.join(directory, random_audio)
    else:
        print("No audio files found in the directory.")
        return None

""" 
# example usage
audio = "/home/sol/Desktop/Contentify/co-video-editor/examples/assets/audio.wav"
find_top_peaks(audio, num_peaks_to_select=3, min_distance_sec=0.3)
 """