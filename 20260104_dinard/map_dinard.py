'''2026-01-04 Carte de Dinard

Test de prettymaps (sous python 3.11, incompatibilité avec python 3.12)

'''

import prettymaps

plot = prettymaps.plot(
    'Rue Coppinger, Dinard, France',
    # preset='minimal',
    save_as='dinard.png',
    # layers={'building': False},
    # keypoints={'tags': {'natural': ['beach']}},
    show=False,
)

