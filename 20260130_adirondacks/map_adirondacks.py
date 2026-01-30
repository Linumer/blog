"""Play with ridge_map

2026-01-30 Linumer

"""

import matplotlib.pyplot as plt
from ridge_map import RidgeMap


# Le mont Marcy qui culmine à 1 629 mètres d'altitude est la plus haute montagne
# de la chaîne des Adirondacks et le point culminant de l'État de New York. 

# 44° 06′ 45″ nord, 73° 55′ 26″ ouest
latp = 44 + 6/60 + 45/3600
lonp = -(73 + 55/60 + 26/3600)
dla = 0.3
dlo = 0.4

cmap = "ocean"  # "autumn"  # 

rm = RidgeMap((lonp-dlo, latp-dla, lonp+dlo, latp+dla))
values = rm.get_elevation_data(num_lines=80)
values=rm.preprocess(
    values=values,
    lake_flatness=2, # 0,    # How much the elevation can change within 3 squares to delete data.
                        # Higher values delete more data. Useful for rivers, lakes, oceans.
    water_ntile=0, # 0, # Percentile below which to delete data Useful for coasts or rivers.
                        # Set to 0 to not delete any data.
    vertical_ratio=40   # How much to exaggerate hills. Kind of arbitrary. 40 is reasonable,
                        # but try bigger and smaller values!
)
rm.plot_map(
    values=values,
    label='Adirondacks',
    label_y=0.1,
    label_x=0.55,
    label_size=40,
    linewidth=5,
    line_color=plt.get_cmap(cmap),
    kind='gradient',  # 'elevation',
)

plt.savefig(f'adirondack_{cmap}.png')
# plt.show()