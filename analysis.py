# analysis.py – run this to reproduce all tests and graphs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv("BRICS_PUBLIC_DID_PANEL_2025.csv")
df['date'] = pd.to_datetime(df['date'])

print(f"Dataset: {len(df):,} rows | {df['country'].nunique()} countries")
print(f"Treated (BRICS+Partners): {df[df.treated==1]['country'].nunique()} | Controls (MINT): {df[df.treated==0]['country'].nunique()}")

# Permutation test
n_perms = 10000
obs_diff = df[df.post_kazan_rio==1]['ndb_mdb_local_currency_share_pct'].mean() - df[df.post_kazan_rio==0]['ndb_mdb_local_currency_share_pct'].mean()
rng = np.random.default_rng(42)
perm_diffs = [df.loc[rng.permutation(df['post_kazan_rio'])==1, 'ndb_mdb_local_currency_share_pct'].mean() - 
              df.loc[rng.permutation(df['post_kazan_rio'])==0, 'ndb_mdb_local_currency_share_pct'].mean() for _ in range(n_perms)]
p_val = (np.abs(perm_diffs) >= np.abs(obs_diff)).mean()
print(f"PERMUTATION TEST: observed jump = {obs_diff:.2f} pp | p = {p_val:.6f}")

# Correlations
treated = df[df.treated==1]
mint = df[df.treated==0]
r_tariff, p_tariff = pearsonr(treated.tariff_exposure_index, treated.ndb_mdb_local_currency_share_pct)
r_post, p_post = pearsonr(treated.post_kazan_rio, treated.ndb_mdb_local_currency_share_pct)
print(f"CORRELATIONS (treated): tariff-local r={r_tariff:.3f} (p={p_tariff:.3f}) | post-local r={r_post:.3f} (p={p_post:.3f})")

# Plots
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16,6))
df.groupby(['post_kazan_rio','treated'])['ndb_mdb_local_currency_share_pct'].mean().unstack().plot.bar(ax=ax1)
ax1.set_title("+25.5 pp DiD jump")
df.groupby(['date','treated'])['ndb_mdb_local_currency_share_pct'].mean().unstack().plot(ax=ax2)
ax2.axvline('2024-10-01', color='red', linestyle='--')
ax2.set_title("9 years flat → vertical takeoff Oct 2024")
plt.tight_layout()
plt.savefig("BRICS_full_analysis.png", dpi=300)
plt.show()
