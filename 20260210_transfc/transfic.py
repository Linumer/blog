"""Represent book data

use plotly with kaleido"""


# TODO order the scatter by date instead of Aspects


import plotly.express as px
import pandas as pd

# Read the book info
df = pd.read_csv('transfic.csv', sep=";")

df.sort_values(by="Parution", inplace=True)

# affiche titre et date de parution
df['Date'] = df['Parution'].astype(int)
df['Date de parution'] = df['Titre'].str.cat(df['Date'].astype(str), sep=' - ')

# dot plot appelé aussi appelé Cleveland dot plot
fig = px.scatter(
    df, y="Date de parution", x="Echelle",
    color="Aspects", symbol="Aspects",
    category_orders={"Date de parution": df["Date de parution"].tolist()}  # Force l'ordre du DataFrame
)

fig.update_yaxes(
    type="category",  #  y comme une catégorie (pas de tri)
    autorange="reversed"  # Optionnel : inverse l'ordre si nécessaire
)
fig.update_traces(marker_size=10)


# Sort categories in descending order
fig.write_image("transfic.png")

# POur un futur blog qui affichera du javascript :
# fig.write_html("transfic.html")