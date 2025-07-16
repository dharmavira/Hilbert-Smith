import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation Parameters
# -----------------------------
N = 1024                 # Number of symbolic points
ell_star = 10.0          # Base phase
delta_max = 0.5          # Phase dispersion range
alpha = 0.01             # Smoothing parameter
t_values = np.linspace(0.01, 1.0, 100)  # Range of t

# Frequency grid for numerical integration
gamma = np.linspace(-50, 50, 5000)
d_gamma = gamma[1] - gamma[0]

# -----------------------------
# Generate symbolic data
# -----------------------------
np.random.seed(42)  # Reproducibility
ell = ell_star + np.random.uniform(-delta_max, delta_max, N)
w = np.ones(N) / np.sqrt(N)

# -----------------------------
# Precompute Ψ_i(γ)
# -----------------------------
psi_matrix = np.array([
    w[i] * np.cos(ell[i] * gamma) * np.exp(-alpha * gamma**2)
    for i in range(N)
])

# -----------------------------
# Compute Θₙ(t) for each t
# -----------------------------
trace_values = []
for t in t_values:
    sum_psi = np.sum(psi_matrix, axis=0)
    integrand = (sum_psi ** 2) * np.exp(-t * gamma**2)
    theta = np.trapz(integrand, gamma)
    trace_values.append(theta)

# -----------------------------
# Plot the results
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(t_values, trace_values, label=r"$\Theta_n(t)$", lw=2)
plt.xlabel(r"$t$", fontsize=12)
plt.ylabel(r"$\Theta_n(t)$", fontsize=12)
plt.title("Entropy Trace Simulation with Phase Dispersion", fontsize=13)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig("entropy_trace_plot.png")
plt.show()
