import pandas as pd
import matplotlib.pyplot as plt 

columnas = ["Nombre", "Metodo", "Periodo", "Radio", "Masa"]
df = pd.read_csv("gaia_limpio.csv", names=columnas)

# calculando las densidades

rho_t = 5.51 # g/cm^3

df["Densidad"] = rho_t * (df["Masa"] / df["Radio"]**3)

plt.figure(figsize=(8,6))

sc = plt.scatter(
	df["Radio"],
	df["Masa"],
	c = df["Densidad"],
	cmap="viridis",
	s=20
	)

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Radio (R_tierra)")
plt.ylabel("Masa (M_tierra) ")
plt.title("Relación Masa-Radio de Exoplanetas")

# BARRA DE COLORES

cbar = plt.colorbar(sc)
cbar.set_label("Densisdad aproximada (g/cm^3)")

plt.tight_layout()

plt.savefig("masa_radio.png", dpi=300)

plt.show()

