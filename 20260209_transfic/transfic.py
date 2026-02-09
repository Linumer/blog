"""Represent book data

use plotly with kaleido"""


import plotly.express as px
import pandas as pd

# Read the book info
df = pd.read_csv('transfic.csv', sep=";")

# Tri par date
#df = df.sort_values(by=['Parution'], inplace=False)

# affiche titre et date de parution
# df['Date'] = df['Parution'].astype(int)
# df['Date de parution'] = df['Titre'].str.cat(df['Date'].astype(str), sep=' - ')

# dot plot appelé aussi appelé Cleveland dot plot
fig = px.scatter(df, y="Titre", x="Echelle",
                 color="Aspects", symbol="Aspects",
                 )
fig.update_traces(marker_size=10)


# Sort categories in descending order
fig.write_image("transfic.png")

# POur un futur blog qui affichera du javascript :
# fig.write_html("transfic.html")