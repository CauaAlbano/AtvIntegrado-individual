import matplotlib.pyplot as plt
import pandas as pd

# Gráfico IDH por gênero

df = pd.read_csv("IDH-SEXO.csv", decimal=",")

df_brasil = df[df["AGREGACAO"] == "BRASIL"]

dados_homens = df_brasil[df_brasil["SEXO"] == "HOMEM"]
dados_mulheres = df_brasil[df_brasil["SEXO"] == "MULHER"]

plt.figure(figsize=(10, 6))

plt.plot(
    dados_homens["ANO"],
    dados_homens["IDHM"],
    marker="o",
    color="blue",
    label="Homens",
)

plt.plot(
    dados_mulheres["ANO"],
    dados_mulheres["IDHM"],
    marker="p",
    color="red",
    label="Mulheres",
)

plt.title("Evolução do IDHM no Brasil por Sexo (2012-2021)")
plt.xlabel("Ano")
plt.ylabel("IDHM")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.xticks(df_brasil["ANO"].unique())

plt.tight_layout()
plt.show()

# Gráfico IDH por raça

df = pd.read_csv("IDH-COR.csv", decimal=",")

df_brasil = df[df["AGREGACAO"] == "BRASIL"]

dados_brancos = df_brasil[df_brasil["COR"] == "BRANCO"]
dados_negros = df_brasil[df_brasil["COR"] == "NEGRO"]

plt.figure(figsize=(10, 6))

plt.plot(
    dados_brancos["ANO"],
    dados_brancos["IDHM"],
    marker="o",
    color="blue",
    label="Brancos",
)

plt.plot(
    dados_negros["ANO"],
    dados_negros["IDHM"],
    marker="s", 
    color="orange",
    label="Negros",
)

plt.title("Evolução do IDHM no Brasil por Cor/Raça (2012-2021)")
plt.xlabel("Ano")
plt.ylabel("IDHM")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.xticks(df_brasil["ANO"].unique())
plt.tight_layout()

plt.show()

# Distribuição etária e composição por sexo/raça; média, mediana e dispersão das faixas.

df = pd.read_csv("Base-de-Dados.csv", decimal=",")

df_uf_2021 = df[(df["AGREGACAO"] == "UF") & (df["ANO"] == 2021)].copy()

colunas_faixas = ["T_FREQ5A6", "T_FUND11A13", "T_FUND15A17", "T_MED18A20"]

relatorio = pd.DataFrame()
relatorio["Média"] = df_uf_2021[colunas_faixas].mean()
relatorio["Mediana"] = df_uf_2021[colunas_faixas].median()
relatorio["Dispersão (Desvio Padrão)"] = df_uf_2021[colunas_faixas].std()
relatorio["Mínimo"] = df_uf_2021[colunas_faixas].min()
relatorio["Máximo"] = df_uf_2021[colunas_faixas].max()

relatorio.index = ["Freq. 5 a 6 anos", "Fund. 11 a 13 anos", "Fund. 15 a 17 anos", "Médio 18 a 20 anos"]

print("--- Estatísticas de Dispersão entre os Estados (2021) ---")
print(relatorio.round(2))
