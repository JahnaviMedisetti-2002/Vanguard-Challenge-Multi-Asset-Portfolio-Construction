import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

print("====== WISER: Portfolio Optimization RESULT ======")

# 1. Define assets, expected returns, and the covariance matrix
assets = ["TCS", "Infosys", "NIFTY ETF", "Reliance", "HDFC BANK"]
returns = np.array([0.15, 0.12, 0.08, 0.14, 0.10])

# clean nested square brackets with no parentheses mix-ups
cov = np.array([
    [0.04, 0.02, 0.01, 0.015, 0.01],
    [0.02, 0.03, 0.01, 0.01, 0.008],
    [0.01, 0.01, 0.02, 0.005, 0.005],
    [0.015, 0.01, 0.005, 0.035, 0.012],
    [0.01, 0.008, 0.005, 0.012, 0.025]
])

# 2. Define the objective function
def objective(w):
    ret = np.dot(w, returns)
    risk = np.dot(w, np.dot(cov, w))
    return -(ret - 0.5 * risk)

# 3. Define Constraints and bounds
cons = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
bounds = [(0, 0.4) for _ in range(5)]

# 4. Run Optimization with a valid initial guess
init_guess = np.ones(5) / 5
res = minimize(objective, init_guess, method='SLSQP', bounds=bounds, constraints=cons)

# 5. Output display
if res.success:
    print("\n--- FINAL PORTFOLIO ---")
    for i, asset in enumerate(assets):
        print(f"{asset}: {res.x[i] * 100:.2f}%")

    port_ret = np.dot(res.x, returns)
    port_risk = np.sqrt(np.dot(res.x, np.dot(cov, res.x)))
    
  print(f"\nExpected Return: {port_ret * 100:.2f}%")
    print(f"Portfolio Risk: {port_risk * 100:.2f}%")
else:
print("\nOptimization failed:", res.message)
