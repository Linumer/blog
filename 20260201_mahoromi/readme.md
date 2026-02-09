## Mahoromi, Chroniques architecturales de l’espace temps

Lien vers l'article: 
https://linumer.wordpress.com/2026/02/01/mahoromi-chroniques-architecturales-de-lespace-temps/

### Carte de Yokohama

Lien vers le [code python](map_mahoromi.py), toujours avec python 3.11

    import prettymaps

    plot = prettymaps.plot(
        (35.44, 139.656),  # 'Yokohama',
        radius=3000,
        save_as='yokohama_macao_.png',
        layers={'building': False},
        show=False,
    )


![Yokohama](yokohama_macao.png "Yokohama")



