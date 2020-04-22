from __future__ import print_function
import librosa
import librosa.display
from matplotlib import pyplot as plt
import numpy as np
import time
import os
from midiutil.MidiFile import MIDIFile
#See https://github.com/duggan/midiutil/blob/master/examples/single-note-example.py

#Load file and get beat times
FILENAME = 'Despacito.mp3'

beat_times = load_beats.get_beat_times(FILENAME)

nbeat=len(beat_times)
print(nbeat)
print(beat_times[-1]/60.)

#average time between beats
avgbeat=np.mean(beat_times[1:]-beat_times[:-1])
print(avgbeat)

start_time = time.time()

#Play the beats and the song at the same time
#(We are concerned about system time delays.)
#os.system('afplay Despacito.mp3 &')
#print(".\n")
#time.sleep(beat_times[0])
#print("Beat 0")
#for i in range(1,nbeat):
#    time.sleep(beat_times[i]-beat_times[i-1])
#    print("Beat ",i)

#So instead, we are going to creat a midifile
MyMIDI = MIDIFile(1)
track=0
time=0
MyMIDI.addTrackName(track,time,"DepacitoBeats")
channel = 0
pitch = 60
duration = 1
volume = 100
for i in range(1,nbeat):
    time=beat_times[i]
    MyMIDI.addNote(track,channel,pitch,time,duration,volume)

binfile = open("DepacitoBeats.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
    
exit()
