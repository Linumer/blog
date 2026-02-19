
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.srtm as srtm
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import contextily as cx


# Watership down 51.3082042 ; -1.2910016
latp = 51.3082042
lonp = -1.2910016
dla = 0.1
dlo = 0.15
top = 90.


# Créer une projection
projection = ccrs.Mercator()

# Créer une figure et un axe
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(1, 1, 1, projection=projection)
# ax = fig.add_subplot(1, 1, 1, projection=ccrs.RotatedPole(pole_longitude=90, pole_latitude=0))

# Définir l'étendue de la carte
ax.set_extent([lonp - dlo, lonp + dlo, latp - dla, latp + dla],
              crs=ccrs.PlateCarree())

cx.add_basemap(ax, crs=ax.projection)  # , source=cx.providers.OpenTopoMap)


# Ajouter des éléments de carte (facultatif)
ax.coastlines(resolution='10m', linewidth=0.5)
ax.gridlines(draw_labels=True)

# Marquer Watership Down
ax.plot(lonp, latp, 'ro', markersize=5, transform=ccrs.PlateCarree())
ax.text(lonp, latp, 'Watership Down', fontsize=10, transform=ccrs.PlateCarree(), ha='right', color='red')

# Afficher la carte
plt.title("Carte des environs de Watership Down")
plt.savefig("watershipdown_osm.jpg")

plt.show()
