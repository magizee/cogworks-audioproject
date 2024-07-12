# database = {
#     fp : (id, t)
# }

import pickle

class Interface:

    def __init__(self, data=None):
        self.db = data if data is not None else {"fp": {}} 
    
    def save_db(self): #saves dict to a pickle file in write-binary mode
        with open('database.pkl', mode = 'wb') as opened_file:
            pickle.dump(self.db, opened_file)

    def load_db(self): #unpickles the database
        with open("database.pkl", mode="rb") as opened_file:
            self.db = pickle.load(opened_file)

    def inspect_song(self, fp): #returns details of the song
        if id in self.db["songs"]: 
            return self.db["songs"][fp]
        else:
            return None
        
    
    def delete_song(self, song_id):
        if song_id in self.db["songs"][-1]:
            del self.db["songs"][song_id]
            self.save_db()
    
    def add_song(self, fingerprints, song_name, artist_name):
        '''
        Parameters
        ----------
        fingerprints : dict ( value: (song_id, dt), key: nparray(fingerprint1, fingerprint2, ...) )
            List of fingerprints from the audio signal.
        song_name : String
            Name of the song.
        artist_name : String
            Name of the artist.

        Returns
        -------
        song_id : int
        '''
        #fanout_n = len(fingerprints)
        names = []

        for (fm, fn, dt) in fingerprints:#if there are multiple fanouts for a single fanout, nest this for loop
            songdb[(fm, fn, dt)].append((song_name, tm))
            #songdb[(fm, fn, dt)]

        if song_name not in self.db["artist_information"][1]:
            song_id = len(self.db["songs"]) + 1
            self.db["songs"] = (fingerprints, song_id)
            self.db["artist_information"] = (artist_name, song_name)
            self.save_db()
            return song_id
        else:
            return False

        """if song_name not in self.db["artist_information"][1]:
            song_id = len(self.db["songs"]) + 1
            self.db["songs"] = (fingerprints, song_id)
            self.db["artist_information"] = (artist_name, song_name)
            self.save_db()
            return song_id
        else:
            return False"""

    
    def list_songs(self):
        return None
    

    