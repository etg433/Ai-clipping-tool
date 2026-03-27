# Travis Scott-Style Vocal Preset for FL Studio

> This preset is designed to get a modern Travis Scott-inspired vocal tone using stock FL Studio plugins plus optional waves-style alternatives.

## 1) Mixer Routing

1. Route your lead vocal to **Insert 1 (LEAD VOX)**.
2. Create send tracks:
   - **Insert 2: VOX DELAY**
   - **Insert 3: VOX REVERB**
   - **Insert 4: VOX DOUBLER**
3. Keep your dry lead centered; pan doubles/ad-libs slightly left/right.

## 2) Lead Vocal Chain (Insert 1)

Use this order:

1. **Pitcher** (or Auto-Tune)
2. **Fruity Parametric EQ 2**
3. **Fruity Compressor**
4. **Soundgoodizer** (light)
5. **Fruity Soft Clipper**
6. **Fruity Limiter** (final control)

### Pitcher (fast, melodic trap tuning)
- Key/Scale: Match beat key (example: C# minor)
- Speed: **0.00 to 0.10**
- Humanize: **0–10%**
- Gender/Formant: slightly down for darker tone (**-0.10 to -0.25**)

### EQ (Parametric EQ 2)
- High-pass: roll off below **80 Hz**
- Cut mud: **-3 dB around 250–400 Hz**
- Presence boost: **+2 to +4 dB around 4.5 kHz**
- Air boost: **+2 dB at 10–12 kHz**
- De-ess range: reduce **6–8 kHz** if harsh

### Compression (Fruity Compressor)
- Ratio: **4:1**
- Threshold: about **-18 dB**
- Attack: **8–15 ms**
- Release: **70–120 ms**
- Gain reduction target: **4–7 dB**

### Saturation / Loudness
- Soundgoodizer: **A mode, 10–25% mix**
- Soft Clipper: default, just catch peaks
- Limiter: ceiling around **-1.0 dB**

## 3) Delay Send (Insert 2)

Plugin: **Fruity Delay 3**
- Time: **1/4** or **1/8 dotted**
- Feedback: **25–40%**
- Cut lows below **200 Hz** and highs above **6–8 kHz**
- Wet: **100%** (because this is a send)

Automation trick: increase send level only at the ends of lines.

## 4) Reverb Send (Insert 3)

Plugin: **Fruity Reeverb 2**
- Predelay: **25–40 ms**
- Decay: **2.0–3.2 s**
- Size: **70–90**
- Low cut: around **180 Hz**
- High cut: around **7 kHz**
- Wet: **100%** on send

Keep reverb subtle in verses and raise in ad-libs/hooks.

## 5) Doubler / Width (Insert 4)

Option A (stock):
- Duplicate lead take twice
- Pan one **-25 L**, one **+25 R**
- Shift timing by **10–20 ms** each side
- Pitch one **-6 cents**, one **+6 cents**
- Low-pass doubles around **8–10 kHz**

Option B (plugin): use any doubler/microshift plugin at low mix.

## 6) Ad-lib Chain (Separate insert)

For Travis-style ad-libs:
- Heavier auto-tune (speed at minimum)
- More distortion/saturation
- More reverb and delay than lead
- Band-pass EQ (telephone vibe) on selected ad-libs

## 7) Quick Recording Settings

- Record level peak: around **-12 dB to -6 dB**
- 24-bit WAV recording
- Use pop filter and stay 4–6 inches from mic
- Record doubles and ad-libs in separate takes

## 8) Macro Controls to Save as Your Own Preset

Create 4 macro knobs in Patcher/Control Surface:
1. **Tune Amount** (Pitcher speed + humanize)
2. **Space** (delay send + reverb send)
3. **Saturation** (Soundgoodizer mix)
4. **Width** (doubler level)

Save this mixer state as:
**"TS_SCOTTY_VOX_v1.fst"**

---

If you want, I can also generate a **dark/aggressive** variant and a **clean/melodic** variant with exact values for your BPM and key.
