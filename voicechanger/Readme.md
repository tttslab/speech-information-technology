# Voice Changer (Source-Filter Model Demo)

This project provides a demonstration of the **Source-Filter Model** of speech production implemented via cepstral analysis. 

By extracting "Source information" and "Spectral envelope (Filter) information" from two different audio files and recombining them, this program allows users to experience the process of voice transformation (voice changing).

## Algorithm Overview

The system processes audio using the following steps:

1.  **Analysis**: Two input signals (Source and Filter) are analyzed on a frame-by-frame basis using cepstral analysis.
2.  **Separation**: Using **liftering** in the cepstral domain, the signal is decomposed into:
    * **Low-quefrency components**: Representing the vocal tract characteristics (spectral envelope/formants).
    * **High-quefrency components**: Representing the excitation source (fine structure/pitch).
3.  **Synthesis**: 
    * The **high-quefrency components** (pitch) from the **Source input** are combined with the **low-quefrency components** (voice quality) from the **Filter input**.
    * The original phase information from the Source input is preserved to maintain the pitch structure.
    * The final waveform is reconstructed in the time domain using the **Overlap-Add (OLA)** method.

### Implementation Note for Students
This demo uses **Homomorphic Signal Processing**. The convolution of the source and filter in the time domain becomes an addition in the log-spectral (and thus cepstral) domain:

$$\log |X(\omega)| = \log |E(\omega)| + \log |H(\omega)|$$

This property allows us to "de-convolve" and manipulate speech characteristics with simple arithmetic operations.

## Directory Structure

```text
voicechanger/
├── voicechanger_example.ipynb  # Jupyter Notebook for execution
└── samplewav/                  # Sample audio files (16kHz/16bit/Mono)
    ├── sawtooth100hz.wav       # 100Hz Sawtooth wave (Artificial source)
    ├── toukoudai.wav           # Speech sample
    ├── neorock38.wav           # Music material (Provided by Maoudamashii)
    └── noise1.wav              # White noise (For whisper speech experiments)
```

## Usage (Jupyter Notebook / Google Colab)

1.  Open `voicechanger_example.ipynb`.
2.  In the code cell, you can switch between different combinations of audio files by toggling the comments for `wavS_file` and `wavF_file`.
3.  Experiment with the variable `N` (liftering transition point) to observe how the smoothness of the spectral envelope and the quality of the synthesized voice change.

## Input Audio Specifications

This demo assumes WAV files with the following specifications:
* **Sampling Rate**: 16,000 Hz (16kHz)
* **Bit Depth**: 16-bit PCM
* **Channels**: Monaural

## Acknowledgments
The sample file `neorock38.wav` is based on free material provided by **魔王魂(Maoudamashii)** and has been converted for this educational demo.

---
**Original Author:** Takahiro Shinozaki (Tokyo Institute of Technology)  
**First Release:** Feb 15, 2017  
**Updated for Notebook:** 2026
