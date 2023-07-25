import keyboard
import Notes.NotesFrequenciesMapper

class NotesController():

    def __init__(self):
        
        self.NotesFrequenciesMapper = NotesFrequenciesMapper()

        self.keysNotes = {
            'z': "C4",
            's': "C#4",
            'x': "D4",
            'd': "D#4",
            'c': "E4",
            'v': "F4",
            'g': "F#4",
            'b': "G4",
            'h': "G#4",
            'n': "A4",
            'j': "A#4",
            'm': "B4"
        }

    def poll(self):
            
        for i in self.keysNotes.keys():
            if keyboard.is_pressed(i):
                note = self.keysNotes[i]
                return NotesFrequenciesMapper[note]
