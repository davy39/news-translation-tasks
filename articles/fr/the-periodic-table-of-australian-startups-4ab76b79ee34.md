---
title: Le Tableau Périodique des Startups Australiennes Construites avec CSS Grid
  ??
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T19:55:28.000Z'
originalURL: https://freecodecamp.org/news/the-periodic-table-of-australian-startups-4ab76b79ee34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yhblHz6Wa1PcKUX4c3QggQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le Tableau Périodique des Startups Australiennes Construites avec CSS Grid
  ??
seo_desc: 'By Shooting Unicorns

  This month the two derp developers at Shooting Unicorns embarked on their journey
  to learn CSS Grid by building a periodic table. As a little tribute to working in
  corporate for 5 years and recently bidding farewell to join the s...'
---

Par Shooting Unicorns

Ce mois-ci, les deux développeurs derp de [Shooting Unicorns](https://shooting-unicorns.com) se sont lancés dans l'apprentissage de CSS Grid en construisant un tableau périodique. En hommage à leurs cinq années passées dans le monde de l'entreprise et à leur récente transition vers la vie de startup, les derps ont pensé que partager des mots à la mode du monde de l'entreprise serait le projet parfait.

1. Mettez-le sur la blockchain
2. Technologie disruptive
3. Nous sommes une entreprise agile
4. Technologie de pointe
5. C'est dans le cloud
6. Nos designs sont centrés sur l'humain
7. Transformation numérique
8. Leadership intellectuel
9. Big data et analytique
10. Vue à 360 degrés
11. Designs sur mesure
12. C'est compatible IoT
13. Création de synergies
14. Briser les silos
15. Automatisation en temps réel
16. … ?

Mais ils ne savaient pas qu'il y a en réalité un total de 118 éléments dans un tableau périodique. Il est rapidement devenu évident pour eux que trouver autant de mots à la mode du monde de l'entreprise serait plus difficile que d'apprendre CSS Grid lui-même. Sans aucun doute, le monde de l'entreprise est jonché de milliers et de milliers de mots à la mode, mais malheureusement pour le duo, se rappeler plus de 7 plus ou moins 2 éléments serait considéré comme une tâche très difficile.

![Image](https://cdn-media-1.freecodecamp.org/images/xSQ7fXrbp8pQeuhnKwuYACkhOZzvEgtRD7Nk)

Maintenant, ils n'ont plus d'autre choix que de faire ce qu'ils font de mieux… un pivot de dernière minute ! ?

Et ainsi… [Le Tableau Périodique des Startups Australiennes](https://startups.shooting-unicorns.com) a été créé à la place ! Ou comme ils aiment l'appeler, la Grille de Startups Complètement Sélective (CSS Grid) (ﾉ_ﾉ)

### L'idée

Plus sérieusement, nous avons été inspirés par [Deck](http://www.hi.agency/deck/), un deck de présentation développé sans utiliser de JavaScript, ce qui nous a vraiment inspiré pour l'essayer.

![Image](https://cdn-media-1.freecodecamp.org/images/yntoXwQCEDWkGtV6Qd7kDu9SaaXBeXFia31C)

C'est sans doute le système de mise en page le plus puissant disponible en CSS et il nous a permis de gérer à la fois les colonnes et les lignes, le rendant multidimensionnel. Nous étions super excités ce jour-là et voulions vraiment faire notre propre [Shooting Unicorns](https://shooting-unicorns.com)Deck, mais pour une raison quelconque, nous avons opté pour un tableau périodique à la place ??.

Nous pensons qu'une raison serait que, bien que le deck ait l'air vraiment cool, le rendre joli aurait pris un énorme morceau de temps loin de l'apprentissage de CSS grid lui-même. Vous pouvez consulter le code source du Deck [ici](http://provide.smashingmagazine.com/css-grid-challenge/deck-css-grid-template.zip?_ga=2.45532898.732059500.1519294938-1524689586.1519294938).

#### Donc, au cours des deux dernières semaines…

Nous avons suivi ce que nous croyions être la recette secrète et avons déterminé la mise en page de la grille en utilisant…

![Image](https://cdn-media-1.freecodecamp.org/images/XYH4DLH45utbfKvHEG1skHgOZKoizbWMnuwS)

Pour déterminer combien de cases la grille devait avoir, nous devions penser en termes de lignes et de colonnes, en tenant compte des espaces vides également.

Un tableau périodique a 118 éléments. Donc, si nos mathématiques ne nous ont pas trompé, pour que notre grille ressemble à un tableau périodique, il faudrait 18 colonnes et 9 lignes, ce qui fait un total de 162 cases.

Notre première itération du tableau périodique était la suivante :

```
.firstElement {   grid-row: 1 / span 1;   grid-column: 1 / span 1;}
```

```
.secondElement {   grid-row: 2 / span 1;   grid-column: 1 / span 1;}
```

```
...nthElement{}
```

Comme vous pouvez l'imaginer, après un certain temps, nous avons finalement créé 118 classes juste pour afficher le tableau périodique… hmmm ?. Surement, il existe une manière plus propre et plus maintenable de faire cela, n'est-ce pas ? Par conséquent, nous avons décidé de ne pas prendre les choses en main et avons suivi l'exemple [ici](https://codepen.io/dudleystorey/pen/rmWMXY/).

Nous avons découvert que CSS grid utilise des algorithmes de mise en page magiques qui peuvent déterminer le flux de la grille. Si nous ne spécifions pas la direction du flux (en utilisant grid-auto-flow), il remplira alors toutes les colonnes d'une ligne avant de passer à la suivante.

Deuxième round. Nous avons supprimé le code CSS original et avons recommencé. Cette fois, nous étions plus intelligents. Vous pouvez vous référer au reste de cet article en suivant notre code source [**ici**](https://github.com/shooting-unicorns/the-periodic-table-of-australian-startups).

![Image](https://cdn-media-1.freecodecamp.org/images/4hUYozPfP7dQS-VF0Bmx1yfYBtCwjZYpJCcq)

Tout d'abord, jetons un coup d'œil à la première ligne du tableau périodique. Le premier élément est automatiquement placé dans la ligne 1, colonne 1. Par défaut, le deuxième élément sera placé dans la ligne 1, colonne 2, mais ce n'est pas ce que nous voulons. En suivant le diagramme, pour le placer dans la 18ème colonne, nous pouvons faire comme suit :

```
.itemInEighteenthColumn {   grid-column-start: 18;}
```

Donc, pour obtenir l'élément suivant dans la deuxième colonne, nous disons simplement à CSS de le placer dans la ligne 2, colonne 1, n'est-ce pas ?

```
.thirdElement {   grid-column-start: 1;   grid-row-start: 2;}
```

C'est une façon, mais dans CSS grid, spécifier un grid-column-start sur un élément enfant créera automatiquement ce nombre de colonnes. Donc dans ce cas, nous avons dit que le deuxième élément devrait commencer à la colonne 18, donc notre grille contiendrait 18 colonnes. Tout élément après cela passerait à la ligne suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/NLwWeR-UQXFH2uB4eBgpep7RxaVVZxIc9UXb)

Le même concept s'applique au troisième élément de la deuxième ligne. Nous avons défini le début de la colonne de la grille à la ligne 13 pour créer cet espace.

```
.secondRowThirdElement {   grid-column-start: 13;}
```

Cela rend toutes les colonnes avant la ligne 13 vides, et le reste des éléments assumeraient leur flux normal à partir de 13 jusqu'à 18. Il en va de même pour la ligne suivante après celle-ci :

```
.secondRowThirdElement, .thirdRowThirdElement {   grid-column-start: 13;}
```

Le seul cas spécial que nous avons dû gérer était les deux dernières lignes en bas, qui nécessitaient des propriétés de grille spécifiques. La raison en est que ces éléments n'étaient pas les derniers éléments de notre HTML, donc ils se retrouveraient mal placés dans les lignes au-dessus. Pour obtenir ces éléments sur les lignes 8 et 9, nous devons explicitement indiquer la propriété grid-row-start à ces éléments individuels (il est nécessaire d'ajouter ces classes à chaque élément individuel dans le HTML) :

```
.row-8 {   grid-row-start: 8;}
```

```
.row-9 {   grid-row-start: 9;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/07-ihShFAeTkGeRHOkrfV9Ceeoxt0KvRysii)
_Résultat après avoir défini .row-8 et .row-9_

Et avec cette magie de CSS Grid, nous avons obtenu notre premier tableau périodique.

![Image](https://cdn-media-1.freecodecamp.org/images/RxBFT9R2dHly4c37Svl8cNy4R0SYda5HSl2H)

#### Scripts

Il aurait fallu beaucoup trop d'efforts pour copier et coller manuellement les données des startups dans un fichier HTML. Pour accomplir la tâche, nous avons créé des scripts Python pour convertir le CSV en JSON, puis du JSON en HTML. Voici un extrait de la manière dont nous avons généré le HTML (pas le meilleur, mais cela a fonctionné néanmoins) :

```
import json
```

```
with open('./startups.json') as startup_data:with open('./startups.html', 'w+') as f:
```

```
d = json.load(startup_data)   for startup in d:   name = startup['name']   city = startup['city']   founded = startup['founded']   description = startup['description']      htmlString= "\   <div class=\"startup-detail-container %s\"> \n\   <div class=\"startup-em\"></div>\n\   <div class=\"name\">%s</div>\n\   <div class=\"description\">%s</div>\n\   </div>\n\n"%(city.lower(), name, description)   f.write(htmlString.encode('utf-8'))
```

Il y avait des scripts supplémentaires qui étaient utilisés pour nettoyer et ajouter des informations supplémentaires aux données existantes, mais nous ne vous ennuerons pas avec les détails.

#### Le reste du puzzle

À partir de là, le reste consistait à pousser des pixels et à jouer avec les couleurs. Nous avons initialement opté pour le schéma de couleurs de Shooting Unicorns, mais aussi coloré que cela puisse paraître, le thème semblait un peu 'sans thème'.

![Image](https://cdn-media-1.freecodecamp.org/images/r7PQ0SXP5U9hJVy3dEsG3lc5y7DLHc1iQGrP)

De nombreux jours plus tard… nous avons finalement opté pour rien de moins que les couleurs de notre terminal… parce que… développeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/Qyc7Jp5DotCQPayiNIAxX-aJnEEFxEW8bhOQ)
_**Version live [ici](https://startups.shooting-unicorns.com" rel="noopener" target="_blank" title=")**_

Nous sommes encore très nouveaux dans CSS, mais nous espérons que ce projet inspirera ou aidera les autres à faire de même. Si vous n'avez pas encore vu notre code, vous pouvez consulter notre dépôt [**ici**](https://github.com/shooting-unicorns/the-periodic-table-of-australian-startups). Nous aimerions également recevoir des commentaires sur la manière dont nous pourrions améliorer la base de code actuelle. N'hésitez pas à partager vos pensées ci-dessous ou même à soumettre une pull request !

#### Qu'est-ce qui suit ? ?

Chaque mois, [Shooting Unicorns](https://www.freecodecamp.org/news/the-periodic-table-of-australian-startups-4ab76b79ee34/undefined) livrera un projet passionnant tout en apprenant une technologie différente. Pour janvier, il s'agissait d'un projet React appelé [Hustle Club](https://hustle.shooting-unicorns.com), une plateforme qui aide les gens à trouver l'accélérateur parfait en Australie.

En mars, nous partagerons tout ce que nous avons appris en Swift, emballé dans un petit nœud. Vous verrez exactement comment nous avons piraté notre chemin des startups aux entreprises !

**Restez à l'écoute et jusqu'à la prochaine fois, bon piratage !**

Nombre de fois pivoté : 100% ✌️