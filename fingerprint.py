from typing import List, Tuple, Dict
import numpy as np

def generate_fingerprints(peaks: List[Tuple[int, int]], fanout: int) -> List[int, Tuple[int, int, int]]:
    '''
    Parameters
    ----------
    peaks : List
        List[Tuple[int, int]]
        (row, col) index pair for each local peak location, returned in 
        column-major order
    fanout : int
        number of neighboring peaks
    Returns
    -------
    List[Tuple (f_i, f_j, delta t_i, j)] - key: song.j t_m

    '''
    fingerprints = []
    peaks = np.array(peaks)

    for i, peak in enumerate(peaks): # for each peak
        freq, absolute_time = peak
        distances = np.sqrt(np.sum((peaks[i:] - peak)**2, axis=1))   
        nearest_indices = np.argsort(distances)[1:fanout + 1]
        for k in nearest_indices:
            new_freq, new_time = peaks[k]
            if new_time > absolute_time:    
                delta_time = new_time - absolute_time
                fingerprint = (freq, new_freq, delta_time)
                fingerprints.append((absolute_time, fingerprint))

    return fingerprints

    # fingerprints = [(adsolute time1, (fm1, fn1, dt1)), (adsolute time2, (fm2, fn2, dt2)) ...]