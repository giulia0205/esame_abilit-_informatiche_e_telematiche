import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.stats import linregress

# Caricamento dati
data = np.loadtxt("AGN.txt")

# Estrazione colonne
total_mass = data[:, 0]
gas_mass = data[:, 1]
dm_mass = data[:, 2]
stellar_mass = data[:, 3]
bh_mass = data[:, 4]
positions = data[:, 5:8]

# Massa barionica
baryonic_mass = gas_mass + stellar_mass

# 1. DM Mass vs Baryonic Mass (log-log) 
mask1 = (baryonic_mass > 0) & (dm_mass > 0)
x = baryonic_mass[mask1]
y = dm_mass[mask1]

plt.figure(figsize=(8,6))
plt.scatter(x, y, alpha=0.7, label='Haloes')
slope, intercept, *_ = linregress(np.log10(x), np.log10(y))
fit_line = 10**(slope * np.log10(x) + intercept)
plt.plot(x, fit_line, 'r', label=f'Fit: log(y)={slope:.2f}log(x)+{intercept:.2f}')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Massa barionica ($10^{10} M_\\odot/h$)')
plt.ylabel('Massa DM ($10^{10} M_\\odot/h$)')
plt.title('DM vs Baryonic Mass (log-log)')
plt.legend()
plt.tight_layout()
plt.savefig('plot1_loglog_dm_vs_baryonic.png')
plt.close()

# 2. Massa totale vs distanza (log-log)
ref_idx = np.argmax(total_mass)
ref_pos = positions[ref_idx]
distances = np.linalg.norm(positions - ref_pos, axis=1)

mask2 = (distances > 0) & (total_mass > 0)
plt.figure(figsize=(8,6))
plt.scatter(distances[mask2], total_mass[mask2])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Distanza dalla struttura più massiva (ckpc/h)')
plt.ylabel('Massa totale ($10^{10} M_\\odot/h$)')
plt.title('Massa totale vs Distanza (log-log)')
plt.tight_layout()
plt.savefig('plot2_loglog_mass_vs_distance.png')
plt.close()

# 3. Istogramma masse DM (asse x log)
positive_dm = dm_mass[dm_mass > 0]
plt.figure(figsize=(8,6))
plt.hist(positive_dm, bins=np.logspace(np.log10(min(positive_dm)), np.log10(max(positive_dm)), 30),
         alpha=0.7, color='skyblue', edgecolor='black')
plt.xscale('log')
plt.axvline(np.mean(positive_dm), color='red', linestyle='--', label=f'Media: {np.mean(positive_dm):.2f}')
plt.axvline(np.median(positive_dm), color='green', linestyle='--', label=f'Mediana: {np.median(positive_dm):.2f}')
plt.xlabel('Massa DM ($10^{10} M_\\odot/h$)')
plt.ylabel('Numero di aloni')
plt.title('Distribuzione masse DM (asse log)')
plt.legend()
plt.tight_layout()
plt.savefig('plot3_log_dm_mass_histogram.png')
plt.close()



#4. Proiezioni

fig, axs = plt.subplots(2, 2, figsize=(14, 12))

# Proiezione x-y
sc1 = axs[0, 0].scatter(
    positions[:, 0], positions[:, 1],
    c=gas_mass, s=stellar_mass * 200,
    cmap='inferno'
)
axs[0, 0].set_xlabel('x (ckpc/h)')
axs[0, 0].set_ylabel('y (ckpc/h)')
axs[0, 0].set_title('Proiezione x-y')
plt.colorbar(sc1, ax=axs[0, 0], label='Massa gas($10^{10} M_\\odot/h$)')

# Proiezione z-y
sc2 = axs[0, 1].scatter(
    positions[:, 2], positions[:, 1],
    c=gas_mass, s=stellar_mass * 200,
    cmap='inferno'
)
axs[0, 1].set_xlabel('z (ckpc/h)')
axs[0, 1].set_ylabel('y (ckpc/h)')
axs[0, 1].set_title('Proiezione z-y')
plt.colorbar(sc2, ax=axs[0, 1], label='Massa gas($10^{10} M_\\odot/h$)')

# Proiezione x-z
sc3 = axs[1, 0].scatter(
    positions[:, 0], positions[:, 2],
    c=gas_mass, s=stellar_mass * 200,
    cmap='inferno'
)
axs[1, 0].set_xlabel('x (ckpc/h)')
axs[1, 0].set_ylabel('z (ckpc/h)')
axs[1, 0].set_title('Proiezione x-z')
plt.colorbar(sc3, ax=axs[1, 0], label='Massa gas($10^{10} M_\\odot/h$)')

# Rimuove il pannello vuoto in basso a destra
fig.delaxes(axs[1, 1])

# Layout e salvataggio
plt.tight_layout()
plt.savefig('plot4_projected_linear.png')
plt.close()



# 5. BH Mass vs Stellar Mass (log-log)
mask5 = (bh_mass > 8e-5) & (stellar_mass > 0)
x5 = stellar_mass[mask5]
y5 = bh_mass[mask5]

plt.figure(figsize=(8,6))
plt.scatter(x5, y5, alpha=0.7)
slope, intercept, *_ = linregress(np.log10(x5), np.log10(y5))
fit_line = 10**(slope * np.log10(x5) + intercept)
plt.plot(x5, fit_line, 'r', label=f'Fit: log(y)={slope:.2f}log(x)+{intercept:.2f}')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Massa stellare ($10^{10} M_\\odot/h$)')
plt.ylabel('Massa BH ($10^{10} M_\\odot/h$)')
plt.title('BH vs Stellar Mass (log-log)')
plt.legend()
plt.tight_layout()
plt.savefig('plot5_loglog_bh_vs_stellar.png')
plt.close()

# 6. Istogramma cumulativo 2D: massa vs distanza
mass_cutoff = 0.307  # 3.07e9 M_sun/h
massive_indices = np.where(total_mass > mass_cutoff)[0]
nbins_mass = 30
nbins_dist = 30

mass_bins = np.logspace(np.log10(min(total_mass[total_mass > 0])), np.log10(max(total_mass)), nbins_mass)
dist_bins = np.linspace(0, max(distances), nbins_dist)
hist2d_total = np.zeros((nbins_dist - 1, nbins_mass - 1))

for idx in massive_indices:
    dists = np.linalg.norm(positions - positions[idx], axis=1)
    h2d, _, _ = np.histogram2d(dists, total_mass, bins=[dist_bins, mass_bins])
    hist2d_total += h2d

plt.figure(figsize=(10, 7))
plt.imshow(hist2d_total, origin='lower', aspect='auto',
           extent=[np.log10(mass_bins[0]), np.log10(mass_bins[-1]), dist_bins[0], dist_bins[-1]],
           cmap='magma')
plt.colorbar(label='Numero di aloni')
plt.xlabel('log10(Massa [$10^{10} M_\\odot/h$])')
plt.ylabel('Distanza (ckpc/h)')
plt.title('Istogramma cumulativo 2D: Massa vs Distanza')
plt.tight_layout()
plt.savefig('plot6_log_mass_vs_distance_histogram.png')
plt.close()
