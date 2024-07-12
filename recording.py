import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from microphone import record_audio
from typing import Tuple
import librosa 

def load_and_parse(file_path: str, source_type: str) -> Tuple[np.ndarray, int]:
    """
    Loads a saved digital signal from an npy file and returns the signal and the sampling rate.
    
    Parameters
    ----------
    file_path : Union[str, pathlib.Path]
        Path to the numpy-based audio file (.npy) to be loaded
        
    Returns
    -------
    Tuple[np.ndarray, int]
        A tuple containing two elements:
        - element 0: The digital signal as a NumPy array (shape-(N,) array)
        - element 1: The sampling rate (int)
    """
    if source_type == "mic":
        loaded_array = np.load(file_path)
        
        sample_rate = loaded_array[0]
        samples = loaded_array[1:]
    
    else:
        samples, sample_rate = librosa.load(file_path)

    return samples, sample_rate

def record_and_save(listen_time: float, file_path: str):
    """
    Uses microphone to record and digitize an analog signal 
    and save the resulting digital signal and sampling rate to npy file.
    
    The first element in the saved array should store the the sample-rate;
    the remaining elements in the array should store the sampled data itself.
    
    
    Parameters
    ----------
    listen_time : float
        Length of recording in seconds.
        
    file_path : Union[str, pathlib.Path]
        Path to the file destination. E.g. "my_audio.npy" will save an audio
        file called "my_audio.npy" to the current working directory.
    """
    
    # 1. Record audio for appropriate amount of time, producing frames & sample-rate
    # 2. Convert frames to array of 16-bit integers (samples)
    # 3. Create a 32-bit int array whose first element is the sample-rate 
    #   (this is the "header" of our audio file)
    #    and the rest of the elements are the samples (stored as 32-bit ints)
    # 4. Save this array to the specified file-path
    
    # 
    frames, sample_rate = record_audio(listen_time)

    samples = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    array_to_save = np.hstack((sample_rate, samples))

    np.save(file_path, array_to_save)

def generate_random_clips(audio_samples, sr, clip_length_sec, num_clips):
    """
    Generate random clips from a given audio sample.

    Parameters:
    audio_samples (np.ndarray): Array of audio samples.
    sr (int): Sample rate of the audio samples.
    clip_length_sec (float): Length of each clip in seconds.
    num_clips (int): Number of random clips to generate.

    Returns:
    List[np.ndarray]: List of arrays, each containing audio samples of a random clip.
    """

    total_length_samples = len(audio_samples)

    clip_length_samples = int(clip_length_sec * sr)

    if total_length_samples < clip_length_samples:
        raise ValueError("The length of the audio sample is shorter than the desired clip length.")

    clips = []

    while len(clips) < num_clips:
        start = np.random.randint(0, total_length_samples - clip_length_samples)
        end = start + clip_length_samples
        clip = audio_samples[start:end]
        clips.append(clip)

    return clips

# # testing
# record_and_save(10, "./example-recording.npy")
# samples, sample_rate = load_and_parse(file_path="./example-recording.npy") 

# clips = generate_random_clips(samples, sample_rate, 1, 5)

# # Print details of the generated clips
# for i, clip in enumerate(clips):
#     print(f"Clip {i+1}: {len(clip)} samples")

