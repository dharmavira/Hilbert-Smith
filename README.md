# Entropy Trace Simulation for Cantor Group Actions

This repository provides a numerical illustration of the **entropy trace functional** `Θₙ(t)` developed in the paper:

**Douglas F. Watson**  
*Spectral Entropy Collapse and the Hilbert–Smith Conjecture for Cantor Groups*  
[Submitted, 2025]

The simulation demonstrates how **symbolic phase dispersion** among wave modes suppresses trace divergence — supporting the main theorem that Cantor group actions on connected manifolds lack Lie-type spectral coherence.

---

## 📘 Background

Each symbolic point `x ∈ Sₙ` is assigned:

- a **phase**: `ℓₙ(x) = log(diam(Gₙ ⋅ x)⁻¹)`
- a **waveform**: `Ψₙ(x)(γ) = wₙ(x) ⋅ cos(ℓₙ(x) ⋅ γ) ⋅ exp(-α ⋅ γ²)`

The entropy trace is defined as:

