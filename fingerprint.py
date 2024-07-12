def generate_fingerprints(peaks, fanout):
    '''
    Parameters
    ----------
    peaks : List
        List of peaks from the audio signal.
    fanout : int
        number of neighboring peaks
    Returns
    -------
    Tuple (f_i, f_j, delta t_i, j) - key: song.j t_m

    '''
    fingerprints = {}

    for peak in np.nditer(peaks): 
        # for k in fanout:
        #peak = peaks[i, j]

        peak_distances = 
        for j in range(fanout):
            neighbor_peak = peaks
            delta_t = neighbor_peak[1] - peak[1]
            fingerprint = (peak[0], neighbor_peak, delta_t)

    return fingerprints

