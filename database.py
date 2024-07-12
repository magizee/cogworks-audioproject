def add_to_database(fanout_m):
    for (fm, fn, dt), tm in fanout_m:#if there are multiple fanouts for a single fanout, nest this for loop
        songdb[(fm, fn, dt)].append((names[i], tm))


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