'''2026-01-04 Carte de Yokohama

python 3.11

NB : see also https://prettymapp.streamlit.app/

'''

import prettymaps

plot = prettymaps.plot(
    (35.44, 139.656),  # 'Yokohama',
    # preset='minimal',
    radius=3000,
    save_as='yakohama9.png',
    layers={'building': False},
    show=False,
)

