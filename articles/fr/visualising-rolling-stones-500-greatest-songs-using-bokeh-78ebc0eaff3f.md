---
title: Les 500 meilleurs albums de Rolling Stone visualisés avec Pandas et Bokeh
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-13T05:42:23.000Z'
originalURL: https://freecodecamp.org/news/visualising-rolling-stones-500-greatest-songs-using-bokeh-78ebc0eaff3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XWotllyqakSjGMCVnSavuA.jpeg
tags:
- name: bokeh
  slug: bokeh
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: music
  slug: music
- name: pandas
  slug: pandas
seo_title: Les 500 meilleurs albums de Rolling Stone visualisés avec Pandas et Bokeh
seo_desc: 'By Gautham Koorma

  In 2003, Rolling Stones Magazine polled musicians, producers, and industry executives
  about their favorite albums. The result was a special issue titled “The 500 Greatest
  Albums of All Time.”

  The list — which they revised in 2012 — ...'
---

Par Gautham Koorma

En 2003, le magazine Rolling Stones a interrogé des musiciens, des producteurs et des dirigeants de l'industrie sur leurs albums préférés. Le résultat était un numéro spécial intitulé « Les 500 meilleurs albums de tous les temps ».

La liste — qu'ils ont révisée en 2012 — présente principalement de la musique américaine et britannique des années 1960 et 1970.

En tant que fan de musique passionné et producteur de musique en herbe, j'écoute une grande variété de genres. La liste des Rolling Stones m'a servi d'introduction à la musique rock à l'époque.

Un jour, en parcourant [Kaggle](https://www.kaggle.com/notgibs/500-greatest-albums-of-all-time-rolling-stone) pour choisir un ensemble de données simple et tester mes nouvelles compétences en visualisation de données, je suis tombé sur la liste téléchargée en tant qu'ensemble de données CSV. J'ai décidé de mettre les mains dans le cambouis en utilisant [pandas](http://pandas.pydata.org/pandas-docs/stable/) pour explorer les données et [bokeh](http://bokeh.pydata.org/en/latest/) pour visualiser les résultats.

Bokeh est une bibliothèque Python pour la visualisation interactive. Elle dispose d'une interface puissante qui prend en charge la création de graphiques de haut niveau, le traçage de niveau intermédiaire et la modélisation de bas niveau.

Le code complet que j'ai utilisé pour lire, affiner, explorer et visualiser les données peut être trouvé sur ma page [GitHub](https://github.com/itzzthad/kaggle-exercises/tree/master/rollingstones-dataset), et également dans ce [notebook](https://www.kaggle.com/thadx89/d/notgibs/500-greatest-albums-of-all-time-rolling-stone/exploring-and-visualizing-using-bokeh/notebook) soumis sur Kaggle.

Cet article décrira les approches que j'ai adoptées, complètes avec mes visualisations et les informations que j'ai acquises en les construisant.

### Obtention et structuration des données

L'obtention des données était simple, car elles étaient dans une feuille de calcul Excel de 500 x 6. Tout ce que j'avais à faire était de la lire directement dans un data frame pandas en utilisant la fonction `[read_excel()](http://pandas.pydata.org/pandas-docs/stable/api.html#input-output)`.

Le data frame avait 500 lignes, une pour chaque album listant le numéro de classement, l'année, l'album, l'artiste, le genre et le sous-genre. Les colonnes Genre et Sous-genre avaient plusieurs valeurs séparées par des virgules dans une chaîne, donc j'ai dû diviser la chaîne à la première virgule et conserver uniquement la première valeur dans de nouvelles colonnes comme la catégorisation la plus pertinente du Genre et du Sous-genre de l'album.

Le data frame principal est devenu 500 x 8 après l'ajout des colonnes Genres_Refined et Subgenres_Refined.

J'ai utilisé un noyau Python 3.5.2 (distribution Anaconda 4.2.0) sur un notebook Jupyter.

![Image](https://cdn-media-1.freecodecamp.org/images/khm0JasV4brSldxU3gjE6K5SOtKhDzohZ2ww)
_**Mon data frame principal**_

### Exploration des données et acquisition d'informations

J'ai adopté la stratégie split-apply-combine en utilisant la fonction intégrée `[groupby()](http://pandas.pydata.org/pandas-docs/stable/groupby.html)` de pandas dans la plupart des cas et la stratégie de remodelage en utilisant la fonction intégrée `[pivot_table()](http://pandas.pydata.org/pandas-docs/stable/reshaping.html)` de pandas pour un seul cas. J'ai alimenté les data frames résultants dans des graphiques et figures bokeh.

Voici les questions que j'ai posées et leurs visualisations résultantes.

### **Les 10 meilleurs artistes ayant le plus d'albums dans la liste**

Pour obtenir les 10 meilleurs artistes, j'ai utilisé `groupby()` sur la colonne des artistes, j'ai pris un compte et j'ai trié le data frame résultant pour obtenir les 10 artistes ayant le plus grand nombre d'albums.

![Image](https://cdn-media-1.freecodecamp.org/images/697-DyzoYiJllMswVuVsR6wkvSoq9k5bTOHc)

Pour visualiser les résultats, j'ai utilisé un objet figure de la bibliothèque [bokeh.plotting](http://bokeh.pydata.org/en/0.10.0/docs/reference/plotting.html) et j'ai dessiné des cercles noirs en utilisant la méthode `circle()`.

![Image](https://cdn-media-1.freecodecamp.org/images/PylJBnNPv0AK2rODbr1O8gXYqjrkPqePtLuo)
_**Top 10 des artistes**_

Il est clair que les Beatles, Bob Dylan et les Rolling Stones sont en tête de liste avec 10 albums chacun.

### Nombre d'albums dans la liste par année

Pour obtenir cela, j'ai utilisé `groupby()` sur la colonne année et j'ai pris un compte, après quoi j'ai trié les données par année et j'ai tracé le data frame résultant en utilisant un graphique en ligne de [bokeh.charts](http://bokeh.pydata.org/en/latest/docs/reference/charts.html).

![Image](https://cdn-media-1.freecodecamp.org/images/dlpHy4jDWktcph9vPOYoRhYAmcMRfGXgFb1g)
_**Distribution des albums par année**_

Le nombre maximum d'albums dans la liste a été publié en 1970. Les albums publiés à la fin des années 1960 et au début des années 1970 étaient également abondants. Le dernier pic se trouve au début des années 1990, représentant l'émergence de la musique Pop, R&B et Hip-Hop.

### Principaux genres et sous-genres

Pour identifier les principaux genres et les sous-genres qui s'y trouvent, j'ai remodelé les données en utilisant la fonction _pivot_table()_ de pandas dans laquelle j'ai défini l'index comme les colonnes Genre_Refined et Subgenre_Refine, et j'ai défini le paramètre `aggfunc` sur count.

Après avoir pris un sous-ensemble du data frame en utilisant une condition selon laquelle il devrait y avoir plus de 5 albums dans un sous-genre, j'ai alimenté le data frame dans un graphique [donut](http://bokeh.pydata.org/en/latest/docs/gallery/donut_chart.html) de bokeh et j'ai défini la [palette](http://bokeh.pydata.org/en/0.10.0/docs/gallery/palettes.html) sur Purples9.

![Image](https://cdn-media-1.freecodecamp.org/images/Bo7OxIwip41CctBBhbhm9FgikYMtYrLO-NUb)
_**Principaux genres et sous-genres**_

Le rock et ses sous-genres couvrent environ 80 % de la sélection. Les albums de musique Hip-Hop, R&B, Soul, Country et Électronique couvrent les 20 % restants.

### Chansons de chaque genre par année

Pour obtenir ces données, j'ai fait un `groupby()` sur l'année et Genre_Refined, j'ai pris le compte, j'ai trié les valeurs par année et j'ai alimenté le data frame résultant dans une [heatmap](http://bokeh.pydata.org/en/latest/docs/gallery/heatmap_chart.html) de bokeh. Cette fois, j'ai utilisé la palette Reds9.

![Image](https://cdn-media-1.freecodecamp.org/images/jUj2CP8YlL3FhiLw3NjhCUrCIoNMgSDA8GJp)
_**Heatmap des chansons de chaque genre par année**_

Les albums de musique rock de la fin des années 60 et des années 70 sont clairement les plus nombreux. Les albums de musique Funk, Soul et Jazz ont diminué en nombre au fil des ans, ouvrant la voie aux albums Hip-Hop et Électronique.

### Sous-genres du Rock au fil des ans

Pour obtenir ces données, j'ai fait un `groupby()` sur l'année, Genre_Refined et Subgenre_Refined, j'ai pris un compte et j'ai sous-ensemblé le data frame pour inclure uniquement le Rock dans la colonne Genre_Refined. J'ai ensuite alimenté le data frame résultant dans une heatmap de bokeh.

![Image](https://cdn-media-1.freecodecamp.org/images/1Cwu9afCgikiHgf0bAO5lshGlUzkJ9zpwQ32)
_**Sous-genres du rock au fil des ans**_

Les premières années étaient dominées par le Rock & Roll, tandis que le Blues Rock et le Pop Rock ont lentement augmenté en nombre au milieu des années 1960. Au milieu des années 1970, le Rock Alternatif a commencé à émerger, suivi par l'Indie Rock au milieu des années 1980.

### Un résumé des 10 meilleurs albums

Enfin, j'ai résumé les 10 meilleurs albums de la liste après les avoir regroupés par artiste.

![Image](https://cdn-media-1.freecodecamp.org/images/tDiNCoIgsFIvLKhMCEccJE6ZouFidw0ombFI)
_**Top 10 des albums regroupés par artiste**_

Les résultats finaux ne sont pas vraiment surprenants. La liste du magazine Rolling Stone contient principalement des chansons de Rock et de ses divers sous-genres, avec quelques exceptions sous forme d'albums de musique Hip-Hop, R&B, Soul, Country et Électronique.

Si vous êtes comme moi et que vous aimez occasionnellement vous reconnecter avec la musique des Beatles, Bob Dylan, Rolling Stones et les autres pionniers du Rock and Roll des années 60 et 70, je vous suggère d'écouter ces meilleurs albums, puis d'explorer à partir de là.

Si vous êtes curieux, vous pouvez lire la liste complète des albums [ici](http://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-20120531).

Je suis consultant en technologie, passionné de science des données et producteur de musique en herbe. Si vous avez des opportunités d'écriture ou si vous êtes intéressé à entrer en contact pour du travail, n'hésitez pas à m'écrire à contact at gautham dot biz.

Si vous avez aimé cet article, n'hésitez pas à cliquer sur le bouton recommander et à le partager avec vos amis.