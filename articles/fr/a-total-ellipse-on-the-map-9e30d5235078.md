---
title: Une ellipse totale sur la carte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:26:26.000Z'
originalURL: https://freecodecamp.org/news/a-total-ellipse-on-the-map-9e30d5235078
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4Di0P5E6_sQYXxYV.jpg
tags:
- name: algorithms
  slug: algorithms
- name: code
  slug: code
- name: maps
  slug: maps
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Une ellipse totale sur la carte
seo_desc: 'By Dalya Gartzman

  Or, how to choose the best way to walk to the beach after work

  It was a cool autumn evening when Hila Kloper and I were thinking of going to the
  beach after work. The beach is about 2.5Km away from the office.

  We were even consideri...'
---

Par Dalya Gartzman

#### Ou comment choisir le meilleur chemin pour aller à la plage après le travail

C'était une fraîche soirée d'automne lorsque Hila Kloper et moi pensions aller à la plage après le travail. La plage est à environ 2,5 km du bureau.

Nous envisagions même de flâner dans les rues de Tel Aviv, prêts à étirer notre parcours à 3 km, et nous disions : « mmm, nous nous demandons jusqu'où cette extension peut nous mener ? »

Eh bien, pour faire court, nous ne sommes pas allés à la plage. Au lieu de cela, nous avons écrit un script qui dessine une ellipse autour du bureau et de la plage. L'ellipse couvre la zone de la ville que nous pourrions traverser si nous décidions un jour d'aller à la plage après le travail.

![Image](https://cdn-media-1.freecodecamp.org/images/Kpo6C3-boqp5qXw2eZlhoJsP10FM0kZhDnIv)
_Quand les développeurs veulent faire quelque chose de fun à l'extérieur et qu'ils finissent par écrire un script à ce sujet à la place._

### C'est l'ellipse de la vie

**Ou - pourquoi devrions-nous nous soucier des ellipses ?**

Un cercle est en quelque sorte la zone « naturelle » autour d'un point. Une ellipse est la zone « naturelle » autour de deux points ou d'une ligne. Pour citer quelques exemples, [les corps de masse se déplacent sur des orbites elliptiques](https://en.wikipedia.org/wiki/Elliptic_orbit), les ellipses représentent la [distorsion causée par la projection d'une carte 3D en 2D](https://en.wikipedia.org/wiki/Tissot%27s_indicatrix), et les ellipses sont également un moyen précis de tracer [la confiance des données GPS bruyantes](https://anitagraser.com/2018/09/04/plotting-gps-trajectories-with-error-ellipses-using-time-manager/) (et [les zones de confiance dans les données 2D](https://www.xarg.org/2018/04/how-to-plot-a-covariance-error-ellipse/) en général).

Dans notre cas, nous voulions dessiner une zone autour de la ligne commençant à notre bureau et se terminant à la plage. La solution la plus facile que nous avons trouvée pour [dessiner des ellipses](https://gis.stackexchange.com/questions/243459/drawing-ellipse-with-shapely) impliquait [shapely](https://pypi.org/project/Shapely/) et [pyplot.](https://matplotlib.org/) Cela nécessitait encore quelques modifications en raison de nos contraintes GPS et cartographiques.

Donc, si vous êtes ici parce que vous cherchez un code facile à copier-coller qui dessine une ellipse sur une carte, vous pouvez aller sur [ce dépôt](https://github.com/DalyaG/CodeSnippetsForPosterity/tree/master/PlotEllipse) que nous avons créé. Si vous êtes également intéressé à apprendre **comment** nous avons trouvé la solution complète à notre problème, vous êtes les bienvenus pour nous rejoindre dans cette aventure. Nous redécouvrons la géométrie élémentaire, apprenons les systèmes de coordonnées et jouons avec du code mathématique.

### Les filles veulent juste des ellipses

> **Nous** : « Oh, il doit y avoir un package quelque part qui peut dessiner une ellipse sur une carte ! »  
> **Internet** : « Non, il n'y en a pas. »  
> **Nous** : « Mais il doit y avoir un code simple à copier-coller quelque part ! »  
> **Stackoverflow** : « J'en ai des incompréhensibles si vous voulez. »  
> **Nous** : « Eh bien, OK, nous prendrons une heure et en ferons un nous-mêmes ! »  
> **Réalité** : « … »

Comprendre ce qu'est réellement une ellipse a été le premier défi.  
[Wolfram Alpha](http://mathworld.wolfram.com/Ellipse.html) nous a dit qu'une ellipse est l'ensemble des points qui ont la même somme-des-distances depuis deux centres mutuels. Ou quelque chose comme ça. Wolfram Alpha peut être plutôt cryptique parfois. Mais ils ont un gif, donc c'est bien.

![Image](https://cdn-media-1.freecodecamp.org/images/ubxw-BHnbWQyhC1gHYMoJV3BRDBG-2RUlr7I)
_Ah… maintenant c'est clair._

Donc, tout ce que nous avons à faire est de nous assurer que nous avons ces entrées :

* `p1, p2` - coordonnées GPS.
* `r` - le rayon qui est en fait la somme des distances d'un point sur l'ellipse aux deux centres.

Puis suivre ce plan :

1. Trouver `a` et `b`, les axes de l'ellipse.
2. Dessiner une ellipse autour de l'origine `(0,0)` mesurée en mètres.
3. Déplacer l'ellipse au centre entre les emplacements GPS d'entrée.
4. Faire pivoter selon l'angle entre les emplacements GPS d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/-970C4VzJQ2BxklnOsjfYlAp2MbeTUrmq-Mk)

Et c'est tout.

Ça semble assez simple, non ?

### La longue et sinueuse route (qui mène à l'ellipse)

#### Étape 1. Trouver les axes.

Ici, nous avons dû faire un peu d'algèbre pythagoricienne de base. Cette image de [Wikipedia](https://en.wikipedia.org/wiki/Ellipse) était quelque peu utile :

![Image](https://cdn-media-1.freecodecamp.org/images/am1h1sbO6znf1TBZs-I-G2j6seQMYXDX12k5)

Le calcul de `c` à partir des coordonnées GPS a été facile grâce au package [haversine](https://pypi.org/project/haversine/).

```python
def GetEllipseAxisLengths(p1_lat, p1_lng, p2_lat, p2_lng,
                          radius_in_meters):
    c2 = haversine((p1_lat, p1_lng), (p2_lat, p2_lng)) * 1000.0
    if radius_in_meters < c2:
        raise ValueError("Veuillez spécifier un rayon plus grand que la               
                          distance entre les deux points d'entrée.")
    a = radius_in_meters / 2.0
    b = sqrt(pow(a, 2) - pow(c2 / 2.0, 2))
    return a, b
```

#### Étape 2. Dessiner une ellipse autour de l'origine.

Ce que nous avons fait ici, c'est que nous avons pris des points régulièrement espacés sur l'axe `x` et pour chacun d'eux, nous avons trouvé les deux points sur l'ellipse qui se projettent sur lui :

![Image](https://cdn-media-1.freecodecamp.org/images/prw5iyWrz2XEn9FVkbcOvoF-VA-STwLSc1Oy)
_Heureusement, nous avons trouvé cette belle équation sur Wikipedia._

```python
def GetEllipsePointInMeters(a, b, num_points):
    """
    :param a: longueur de l'axe "horizontal" en mètres
    :param b: longueur de l'axe "vertical" en mètres
    :param num_points: (la moitié du) nombre de points à dessiner
    :return: Liste de tuples de points de périmètre sur l'ellipse, 
             centrés autour de (0,0), en m.
    """
    x_points = list(np.linspace(-a, a, num_points))[1:-1]
    y_points_pos = [sqrt(pow(a, 2) - pow(x, 2)) * 
                    (float(b) / float(a))
                    for x in x_points]
    y_points_neg = [-y for y in y_points_pos]

    perimeter_points_in_meters = 
        [tuple([-a, 0])] + \
        [tuple([x, y]) for x, y in zip(x_points, y_points_pos)] + \
        [tuple([a, 0])] + \
        list(reversed([tuple([x, y]) 
                       for x, y in zip(x_points, y_points_neg)]))
    return perimeter_points_in_meters
```

#### Étape 3. Comment ajouter des mètres au GPS ?

Eh bien, c'était un peu délicat, et la réponse réside dans la compréhension que

![Image](https://cdn-media-1.freecodecamp.org/images/Hc00Kw6PkLDTkU8eq7GYS6fj10fIP48qGltv)
_Dévoilant les secrets de la géométrie élémentaire._

> Fait amusant : le rayon de la Terre est d'environ 6 371 000 mètres en moyenne !

```python
def AddMetersToPoint(center_lng, center_lat, dx, dy):
    """
    :param center_lng, center_lat: Coordonnées GPS du centre  
           entre les deux points d'entrée.
    :param dx: distance à ajouter à l'axe x (lng) en mètres
    :param dy: distance à ajouter à l'axe y (lat) en mètres
    """
    new_x = (center_lng + (dx / R_EARTH) * (180 / pi) /   
             np.cos(center_lat * pi/180))
    new_y = center_lat + (dy / R_EARTH) * (180 / pi)
    return tuple([new_x, new_y])
```

#### Étape 4. Faire pivoter.

Cette fois, les merveilles d'Internet ne nous ont pas déçus (comme ils l'ont fait pour notre tâche principale de dessin d'ellipse). Nous avons trouvé le package [shapely](https://pypi.org/project/Shapely/) pour faire la rotation pour nous. Le seul truc à retenir ici est que vous ne pouvez pas faire pivoter les points un par un. Plutôt, vous devriez _former une forme d'abord_, puis _faire pivoter toute la forme_.

```python
def GetEllipsePoints(p1_lat, p1_lng, p2_lat, p2_lng, 
                     perimeter_points_in_meters):
    """
    Entrez les centres de l'ellipse en lat-lng et les points de périmètre de l'ellipse    
    autour de l'origine (0,0), et obtenez les points sur le périmètre de l' 
    ellipse autour des centres en lat-lng.
    :param p1_lat: coordonnées lat du point central 1
    :param p1_lng: coordonnées lng du point central 1
    :param p2_lat: coordonnées lat du point central 2
    :param p2_lng: coordonnées lng du point central 2
    :param perimeter_points_in_meters: Liste de tuples de points de périmètre 
           sur l'ellipse, centrés autour de (0,0), en m.
    :return: Liste des points que nous voulons vraiment, tuples de (lat,lng)
    """
    center_lng = (p1_lng + p2_lng) / 2.0
    center_lat = (p1_lat + p2_lat) / 2.0
    perimeter_points_in_lng_lat = \
        [AddMetersToPoint(center_lng, center_lat, p[0], p[1])
         for p in perimeter_points_in_meters]
    ellipse = LineString(perimeter_points_in_lng_lat)

    angle = degrees(atan2(p2_lat - p1_lat, p2_lng - p1_lng))
    ellipse_rotated = affinity.rotate(ellipse, angle)

    ellipse_points_lng_lat = list(ellipse_rotated.coords)
    ellipse_points = [tuple([p[1], p[0]]) 
                      for p in ellipse_points_lng_lat]
    return ellipse_points
```

#### Surprise ! Étape 5. Dessiner sur une carte s2 !

Nous voulions présenter l'ellipse joliment sur une [carte s2](http://s2map.com). Apparemment, vous pouvez le faire en ouvrant l'URL depuis l'intérieur de votre script. Nous avons utilisé [subprocess](https://docs.python.org/2/library/subprocess.html) pour cela.

```python
def OpenS2Map(points):
    url = \
      "http://s2map.com/#order=latlng&mode=polygon&s2=false" \
      "&points={}".format(str(points).replace(" ", ","))
    cmd = ["python", "-m", "webbrowser", "-t", url]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                     stderr=subprocess.STDOUT).communicate()
```

![Image](https://cdn-media-1.freecodecamp.org/images/OMCosB902DjSzC27OJcbQG3Z4UNQTBVq5LwC)
_OK. pouvons-nous aller à la plage maintenant ?_

### L'ellipse du voisin est plus ronde

Vous pourriez remarquer que notre ellipse n'est pas parfaite. Les points sont régulièrement espacés sur l'axe entre les centres, mais ils ne sont pas régulièrement espacés sur le périmètre de l'ellipse. La transformation `GPS->mètres->GPS` pourrait entraîner une perte de mètres ici et là. Mais bon, fait est mieux que parfait, et nous devons laisser quelque chose à faire pour la prochaine fois que nous voudrons aller à la plage, non ?