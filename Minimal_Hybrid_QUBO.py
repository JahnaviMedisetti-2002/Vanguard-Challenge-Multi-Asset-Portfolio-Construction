import numpy as np

assets = ["TCS", "Infosys", "Reliance", "HDFC", "Wipro"]
returns = np.array([0.15, 0.12, 0.14, 0.11, 0.05])

# Covariance Matrix
cov = np.array([
    [0.040, 0.018, 0.010, 0.020, 0.015],
    [0.018, 0.035, 0.008, 0.016, 0.012],
    [0.010, 0.008, 0.020, 0.009, 0.007],
    [0.020, 0.016, 0.009, 0.045, 0.018],
    [0.015, 0.012, 0.007, 0.018, 0.030]
])

# QUBO Matrix: Risk - Return
Q = 4.0 * cov - np.diag(returns)

best_energy = 999
best = None

# Try all 32 combinations
for i in range(32):
    x = np.array([int(b) for b in format(i, '05b')])
    energy = x @ Q @ x
    if energy < best_energy:
        best_energy, best = energy, x

print("--- RESULT ---")
for i, a in enumerate(assets):
    print(f"{a}: {'BUY' if best[i]==1 else 'SKIP'}")

print(f"\nSelected: {sum(best)} assets")
