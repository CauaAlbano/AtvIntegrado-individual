import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "TabelaIndio2.csv", sep=";", skiprows=6,
    names=["UF", "Situacao", "Indigenas"],
    encoding="utf-8-sig", thousands="."
)
df = df[df["UF"].notna()]
df = df[~df["UF"].str.contains("Fonte|Notas|Legenda", na=False)]
df["Indigenas"] = pd.to_numeric(df["Indigenas"].replace("-", 0), errors="coerce")
df = df.dropna(subset=["Indigenas"]).sort_values("Indigenas", ascending=False)

plt.figure(figsize=(12, 7))
plt.barh(df["UF"], df["Indigenas"], color="darkgreen", alpha=0.85)
plt.title("Pessoas indígenas em terras indígenas por UF (Censo 2022)")
plt.xlabel("Pessoas")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()