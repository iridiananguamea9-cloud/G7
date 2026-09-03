# G7 — Audited Analytical and Computational Results
This repository contains the final audited report and computational pipeline for the G7/G8 analysis.
The results are explicitly separated into three categories: PROVEN, COMPUTATIONAL EVIDENCE, CONJECTURE.

### I. PROVEN — G7-D, G8-A
$|\nabla n|^2 = 1/2 s^2 + 1/2 t^2 + |b|^2 + |Q|^2$, $(Q^2)^o=0$, gap L2 y L1.
$||\Delta n||_2 \le sqrt((C_E+C_0)/\lambda)$, $C_\lambda=O(\lambda^{-1/2})$.

### II. PROVEN — G8-B.1
$|\hat{inc M}(k)| = |k|^2 |P_k \hat M(k) P_k|$, $||PM||_{dot H^1} \le ||inc M||_{dot H^{-1}}$.

### III. COMPUTATIONAL EVIDENCE
$C_\lambda=104$ for $\lambda=10^{-3}$ (implementation-dependent). $H_{L2}:0.296->0.206$ over 200 iterations (exploratory only, not proof of c(C)>0).

### IV. CONJECTURE
$||\nabla M||_2 \lesssim C_\lambda^{3/4} ||inc M||_2^{1/4}$ (Conj-G8) is not claimed as theorem.
Open target: $||\nabla M||_2^4 \lesssim ||M||_{H^2}^3 ||inc M||_2$ (G8.14). Would imply Conj-G8 after H2 bound.

Status: G7-D PROVEN, G8-A PROVEN, G8-B.1 PROVEN, C=104 COMP EVIDENCE, H COMP EVIDENCE, Conj-G8 CONJECTURE, G8.14 OPEN TARGET.
No numerical experiment is presented as substitute for proof.
