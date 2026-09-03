import numpy as np

# Simula tu campo n en T^3 - reemplaza con tu n real
# Aquí verificamos las identidades algebraicas

def check_identities(s, t, Q_norm_sq, H_nn, tr_PHP, PHn_norm):
    # Identidad 1: n^T H n
    lhs1 = H_nn
    rhs1 = -0.5*s**2 + 1.5*t**2 + Q_norm_sq
    print(f"n^T H n : {lhs1:.6f} vs {-0.5*s**2 + 1.5*t**2 + Q_norm_sq:.6f} diff={lhs1-rhs1:.2e}")
    
    # Identidad 2: tr(PHP) + 2 n·grad s
    # tr = -s^2 - t^2 -2|Q|^2 -2 n·grad s
    print("Identidades OK si diff ~ 0")

# Test con tu caso H=0 -> t=0, s^2=2|Q|^2
s = 1.0
Q2 = s**2/2
t = 0
H_nn = -0.5*s**2 + Q2  # debe ser 0
print(f"Test H=0: H_nn={H_nn} (debe ser 0)")

# Cota cuantitativa D3-A: ||t||2
def cota_t(H_L2, vol=1.0):
    C = 1 + 1/np.sqrt(2)
    return np.sqrt(C * np.sqrt(vol) * H_L2)

print(f"Cota t para ||H||2=0.01: {cota_t(0.01):.6f}")
