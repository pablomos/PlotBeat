import librosa

def get_beat_times(filename):
    y, sr = librosa.load(filename)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return beat_times
