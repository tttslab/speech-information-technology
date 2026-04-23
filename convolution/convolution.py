# comvolution.py
# Shinozaki Lab 2020.5
#
import sys
from scipy.io.wavfile import write, read
import numpy as np

def convolution(x, h):
    '''
    Calculate convolution of x and h.
    ::x:: array-like with length N
    ::h:: array-like with length M
    ------------------------
    ::out:: list with length (M+N-1)
    '''
    x, h = np.array(x, dtype=np.int32), np.array(h, dtype=np.int32)
    assert x.ndim == h.ndim == 1
    N, M = x.shape[0], h.shape[0]

    out = np.zeros(M+N-1, dtype=np.int32)

    # Version 1
    for n in range(0, M+N-1):
        for k in range(M):
            if 0 <= n - k < N:
                out[n] += h[k] * x[n-k]
    
    # # Version 2
    # # Step 1: padding 0 before x
    # x_pad = np.concatenate([np.zeros(M-1, dtype=np.int32), x], axis=0)
    # # Step 2: reverse h and padding 0 after h_reverse
    # h_reverse = h[::-1]
    # h_pad = np.concatenate([h_reverse, np.zeros(N-1, dtype=np.int32)], axis=0)
    # # Step 3: shift and convolve
    # for n in range(0, M+N-1):
    #     out[n] = sum(np.roll(h_pad, shift=n) * x_pad)
    return out

def main(args):
    assert len(args) == 3, 'Usage: python convolution.py <input1.wav> <input2.wav> <output.wav>'
    sample_rate_1, wav_1 = read(args[0])
    sample_rate_2, wav_2 = read(args[1])

    assert sample_rate_1 == sample_rate_2, 'Sample rates of input files are not consistent.'

    conv = np.convolve(wav_1.astype(np.int64), wav_2.astype(np.int64))
    #conv = convolution(wav_1.astype(np.int64), wav_2.astype(np.int64))

    # Normalize the result to 16 bit integer.
    conv = np.array(conv / np.max(np.abs(conv)) * 32767, dtype=np.int16)
    write(filename=args[2], rate=sample_rate_1, data=conv)

if __name__ == "__main__":
    main(sys.argv[1:])