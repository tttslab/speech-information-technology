# Voice Changer (Source-Filter Model Demo)

This project provides a demonstration of the **Source-Filter Model** of speech production implemented via cepstral analysis. 

By extracting "Source information" and "Spectral envelope (Filter) information" from two different audio files and recombining them, this program allows users to experience the process of voice transformation (voice changing).

## Algorithm Details: How the two files are combined

The core of this demo is to create a hybrid signal $Y_m$ by transplanting the **spectral envelope** of the Filter signal ($F_m$) onto the **excitation source** of the Source signal ($S_m$).

### 1. Analysis and Decomposition
We decompose both input signals into their magnitude and phase components:

- **Source Signal ($s_m[n]$)**: Provides the "voice height" and "timing."
  $$S_m(\omega) = |S_m(\omega)| \exp(j \angle S_m(\omega))$$
  *(Used for: High-quefrency magnitude and Phase information)*

- **Filter Signal ($f_m[n]$)**: Provides the "vocal quality" (vowels).
  $$F_m(\omega) = |F_m(\omega)| \exp(j \angle F_m(\omega))$$
  *(Used for: Low-quefrency magnitude only)*

### 2. Hybrid Magnitude Synthesis (Liftering)
Using **Homomorphic Processing**, we operate in the log-spectral domain where the spectral envelope and excitation are additive. The magnitude of the synthesized signal $|Y_m(\omega)|$ is constructed as follows:

Let $C_S$ and $C_F$ be the cepstra of the source and filter signals, respectively. We apply a low-pass lifter $L_{low}$ and a high-pass lifter $L_{high}$ to extract the desired components:

$$\text{Cepstrum of } Y_m = L_{low}(C_{F,m}) + L_{high}(C_{S,m})$$

This means the synthesized magnitude spectrum $|Y_m(\omega)|$ consists of:
- **The Envelope** from $F_m$ (Low-quefrency / Vocal tract)
- **The Excitation** from $S_m$ (High-quefrency / Glottal source)



### 3. Waveform Reconstruction
Finally, we combine the hybrid magnitude with the original source phase to preserve the temporal pitch structure:

$$Y_m(\omega) = |Y_m(\omega)| \exp(j \angle S_m(\omega))$$

The time-domain frame is then recovered via IDFT and connected using the Overlap-Add (OLA) method:
$$y_{out}[n] = \sum_{m} \text{Re} \left[ \mathcal{F}^{-1} \{ Y_m(\omega) \} \right] [n - mL]$$

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
