"""Represent book data

use plotly with kaleido"""


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


class DotBooks(object):
    
    def __init__(self, csv_file='transfic.csv'):

        self.csv_file = csv_file
        self.prepare_data()

    def prepare_data(self, csv_file='transfic.csv'):

        # Read the book info
        df = pd.read_csv(self.csv_file, sep=";")

        df.sort_values(by="Parution", inplace=True)

        # affiche titre et date de parution
        df['Date'] = df['Parution'].astype(int)
        df['Parution'] = df['Titre'].str.cat(df['Date'].astype(str), sep=' - ')

        self.data = df
        self.add_icons()

    def set_echelle_num(self):
        """Set a numeric value to Echelle"""

        ech_order = ["Local", "National", "Mondial"]
        self.data['Echelle_num'] = [ech_order.index(ech) for ech in self.data['Echelle']]

    def add_icons(self):

        # replace markers by icones
        icons_dict = {'Politique': '€', 'Technique': "⚙️", 'Retour à la nature': "🌳", 'Vie quotidienne': "🏠"}
        unics_dict = {'Politique': '\u2696', 'Technique': u"\u2699",
                      'Retour à la nature': u"\u2698", 'Vie quotidienne': u"\u2302"}
        self.data['Symbol'] = [icons_dict.get(categ) for categ in self.data['Aspects']]
        self.data['Unicode'] = [unics_dict.get(categ) for categ in self.data['Aspects']]
        self.data['Size'] = [0 for categ in self.data['Aspects']]

        self.legend_str = ""
        self.legend_unicode = ""
        for k in icons_dict.keys():
            self.legend_str += f"\r\n{icons_dict[k]}: {k}"
            self.legend_unicode += f"\n{unics_dict[k]}: {k}"

    def reorder(self):
        self.fig.update_yaxes(
            type="category",  #  y comme une catégorie (pas de tri)
            autorange="reversed"  # Optionnel : inverse l'ordre si nécessaire
        )

    def dot_xkcd(self, pngfile='transfic_xkcd.png'):
        """Matplotlib/xkcd style plot"""

        self.set_echelle_num()
        ytxt = self.data['Parution']
        xtxt = self.data['Echelle']
        ny = len(ytxt)
        xnum = self.data['Echelle_num']
        ynum = range(ny)

        plt.xkcd()

        rcParams['font.family'] = 'DejaVu Sans'  # Ensure the font supports Unicode

        # Create the plot
        self.fig, ax = plt.subplots(figsize=(8, 6))

        # Draw horizontal lines for reference
        ax.hlines(
            y=ynum, xmin=0, xmax=2,
            color='lightgray', linestyles='dotted', linewidth=0.8)

        # Plot the dots
        for ii, y in enumerate(ynum):
            ax.text(xnum[ii], y, s=self.data["Unicode"][ii])

        # Set y-axis labels
        ax.set_yticks(ynum)
        ax.set_yticklabels(ytxt)

        ax.set_xticks(xnum)
        ax.set_xticklabels(xtxt)

        # Labels and title
        plt.title(self.legend_unicode, fontsize=12)
        self.fig.text(0.05, 0.9, 'Quelques protopies',
                      fontdict={"size":20})

        # Remove top and right spines for cleaner look
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Adjust layout
        plt.tight_layout()
        self.fig.savefig(pngfile)

    def dot_express(self, pngfile="transfic.png"):
        # dot plot appelé aussi appelé Cleveland dot plot
        self.fig = px.scatter(
            self.data,
            y="Parution",
            x="Echelle",
            color="Aspects",
            symbol="Aspects",
            # text="Symbol",
            category_orders={"Parution": self.data["Parution"].tolist()}
            # Force l'ordre du DataFrame
        )
        self.reorder()
        self.fig.write_image(pngfile)

    def dot_express_icons(self, pngfile="transfic_icons.png"):
        # dot plot appelé aussi appelé Cleveland dot plot
        self.fig = px.scatter(
            self.data,
            y="Parution",
            x="Echelle",
            color="Aspects",
            symbol=None,  # "Aspects",
            text="Symbol",
            size="Size",
            title=self.legend_str,
            category_orders={"Parution": self.data["Parution"].tolist()}
            # Force l'ordre du DataFrame
        )
        self.fig.update_traces(
            marker=dict(size=0),  # Masquer les marqueurs
            textfont=dict(size=20)  # Agrandir les icônes
        )
        self.fig.update_layout(showlegend=False)
        self.reorder()
        self.fig.write_image(pngfile)

    def savehtml(self, htmlfile=""):
        # Pour un futur blog qui affichera du javascript :
        self.fig.write_html(htmlfile)

    def dot_go(self, pngfile="transfic_icons.png"):

        # Données
        x = self.data["Echelle"]
        y = self.data["Parution"]
        categories = self.data["Aspects"]
        icons = self.data["Symbol"]

        self.fig = go.Figure()

        for i, (cat, icône) in enumerate(zip(set(categories), set(icons))):
            # Filtrer les données pour la catégorie actuelle
            mask = [c == cat for c in categories]
            self.fig.add_trace(go.Scatter(
                x=[x[i] for i in range(len(x)) if mask[i]],
                y=[y[i] for i in range(len(y)) if mask[i]],
                mode="text",  # Afficher uniquement le texte (icône)
                text=[icons[i] for i in range(len(icons)) if mask[i]],
                textfont=dict(size=20),
                textposition="middle center",
                # name=f"{cat} {icône}",  # Nom dans la légende avec icône
                showlegend=False,
                # legendgroup=cat,
            ))

        self.reorder()
        self.savefig(pngfile)


# DotBooks().dot_express("transfic.png")
# DotBooks().dot_express_icons("transfic_icons.png")
DotBooks().dot_xkcd("transfic_xkcd.png")
