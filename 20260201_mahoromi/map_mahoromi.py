'''2026-01-04 Carte de Yokohama

python 3.11

NB : see also https://prettymapp.streamlit.app/

'''

import prettymaps

plot = prettymaps.plot(
    'Yokohama',
    preset='minimal',
    # radius=5000,
    save_as='yakohama2.png',
    # layers={'building': False},
    # keypoints={'tags': {'natural': ['beach']}},
    show=False,
)

