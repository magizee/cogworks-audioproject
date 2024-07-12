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
        
    #Database dict
    #key: fingerprints
    #value: (absolute time, song_id)
    
    '''
    self.db = {
        "songs": {
            fingerprints1 : (absolute time, song_id) -> access key: del value[key]
            fingerprints2 : (absolute time, song_id)
        }
        "artist_information": {
            song_id1 : (artist_name1, song_name1) -> del self.db["artist_information"][song_id]
            song_id2: (artist_name2, song_name2)
        }
    }
    '''
    def delete_song(self, song_id):
        found = False
        if song_id in self.db["songs"][-1]:
            found = True

        for songs in self.db["songs"]:
            if song_id in songs:
                del self.db[]
            del self.db["artist_information"][song_id]
            self.save_db()
    
    def add_song(self, fingerprints, song_name, artist_name):

        '''
        Parameters
        ----------
        fingerprints : List ( value: dt, key: nparray(fingerprint1, fingerprint2, ...) )
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
        #names = []
            #songdb[(fm, fn, dt)]

        if song_name not in self.db["artist_information"][1]:
            song_id = len(self.db["artist_information"])
            #self.db["songs"] = (fingerprints, song_id)
            self.db["artist_information"] = (artist_name, song_name)
            self.save_db()
        else:
            for i, value in enumerate(self.db["artist_information"][1]):
                if value == song_name:
                    song_id = i
                    break

        for absolute_time, (fm, fn, dt) in fingerprints:      #if there are multiple fanouts for a single fanout, nest this for loop
            self.db["songs"][(fm, fn, dt)].append((song_id, absolute_time))

        return song_id
        """if song_name not in self.db["artist_information"][1]:
            song_id = len(self.db["songs"]) + 1
            self.db["songs"] = (fingerprints, song_id)
            self.db["artist_information"] = (artist_name, song_name)
            self.save_db()
            return song_id
        else:
            return False"""
        

        '''
        #songs is a list of songs
        #names is a list of all the names and albums as strings
        def make_database
        songs = []
        names = []
        songdb = {}
        for i in range(len(songs)):
            #analog to digital
            #digital to spectogram
            #spectogram to peaks
            #peaks to fingerprints
            for (fm, fn, dt), tm in fanout_m:#if there are multiple fanouts for a single fanout, nest this for loop
                songdb[(fm, fn, dt)].append((names[i], tm))
        #export dictionary
        '''

    def compare_fingerprints(self, fingerprints, songdb):#fingerprint of testing audio
        from collections import Counter
        tally = []
        for f in fingerprints:
            if f in list(songdb.keys()):
                tally.extend(songdb.get(f))
        highest = Counter(tally).most_common(1)[0] #tuple: (song-name, number of times it shows up)
        #return highest[0], highest[1] #returns-> song_name, no. of times the song show up
        if (highest[1]/len(fingerprints) > 0.5):#how shd this work
            return highest[0]
        else:
            return "Song not in database"

    def list_songs(self):
        return None
    

    