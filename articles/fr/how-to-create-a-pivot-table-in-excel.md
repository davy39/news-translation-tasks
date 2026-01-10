---
title: Comment créer un tableau croisé dynamique dans Excel
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-14T22:35:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-pivot-table-in-excel
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pivotTable.png
tags:
- name: charts
  slug: charts
- name: Datatables
  slug: datatables
- name: excel
  slug: excel
seo_title: Comment créer un tableau croisé dynamique dans Excel
seo_desc: "In Excel, pivot tables let you analyze and visualize your data in an easy\
  \ way. \nWith pivot tables, you can make comparisons and create calculations more\
  \ quickly. You can even create charts to visualize your data.\nCreating pivot tables\
  \ might be intimi..."
---

Dans Excel, les tableaux croisés dynamiques vous permettent d'analyser et de visualiser vos données de manière simple. 

Avec les tableaux croisés dynamiques, vous pouvez effectuer des comparaisons et créer des calculs plus rapidement. Vous pouvez même créer des graphiques pour visualiser vos données.

Créer des tableaux croisés dynamiques peut sembler intimidant si vous le faites pour la première fois. Mais dans cet article, je vais vous expliquer tout ce dont vous avez besoin pour commencer à créer des tableaux croisés dynamiques.

Ce n'est pas tout – je vais également vous montrer comment ajouter des graphiques pour visualiser vos données.

De plus, la version d'Excel que vous utilisez n'a pas d'importance. Vous pouvez même créer un tableau croisé dynamique dans Excel 2013. En fait, j'ai utilisé Excel 13 pour préparer cet article.

## Ce que nous allons couvrir
- [Comment créer un tableau croisé dynamique dans Excel](#heading-comment-creer-un-tableau-croise-dynamique-dans-excel)
  - [Comment créer des lignes et effectuer des calculs avec un tableau croisé dynamique](#heading-comment-creer-des-lignes-et-effectuer-des-calculs-avec-un-tableau-croise-dynamique)
  - [Comment créer des lignes entièrement nouvelles avec un tableau croisé dynamique](#heading-comment-creer-des-lignes-entierement-nouvelles-avec-un-tableau-croise-dynamique)
- [Comment implémenter une visualisation graphique pour un tableau croisé dynamique](#heading-comment-implementer-une-visualisation-graphique-pour-un-tableau-croise-dynamique)
- [Conclusion](#heading-conclusion)


## Comment créer un tableau croisé dynamique dans Excel
Pour vous montrer comment créer un tableau croisé dynamique, j'ai créé un tableau de quelques footballeurs fictifs montrant :

- leurs noms
- le nombre de matchs qu'ils ont joués
- leurs passes décisives et buts

![ss1-3](https://www.freecodecamp.org/news/content/images/2022/09/ss1-3.png) 

Je vais créer des lignes supplémentaires pour les "Contributions aux buts" et le "Ratio de buts", également appelé Buts par Match.

En football (Soccer), les contributions aux buts représentent le nombre total de buts et de passes décisives. Le ratio de buts est obtenu lorsque le nombre de buts est divisé par le nombre de matchs joués.

**Pour créer un tableau croisé dynamique, suivez les étapes ci-dessous** :

**Étape 1** : Dans la barre de menu, cliquez sur "Insertion" et sélectionnez "Tableau croisé dynamique" :

![ss2-3](https://www.freecodecamp.org/news/content/images/2022/09/ss2-3.png) 

**Étape 2** : Laissez tout tel quel et sélectionnez "OK" :

![ss3-3](https://www.freecodecamp.org/news/content/images/2022/09/ss3-3.png) 

Vous devriez utiliser une nouvelle feuille de calcul pour avoir une feuille dédiée à votre tableau croisé dynamique.

L'interface suivante que vous verrez ressemble à ceci :

![ss4-3](https://www.freecodecamp.org/news/content/images/2022/09/ss4-3.png)

Vous travaillerez avec la partie où vous voyez "Champs du tableau croisé dynamique". Vous verrez même les colonnes de votre tableau là.

### Comment créer des lignes et effectuer des calculs avec un tableau croisé dynamique

C'est la partie où vous pouvez créer des lignes, des colonnes et effectuer des calculs.

Pour créer des lignes pour votre tableau croisé dynamique, faites glisser l'une des lignes du tableau existant vers la partie où vous voyez "LIGNES". 

Par exemple, je veux créer une ligne pour le tableau croisé dynamique avec la ligne de nom du tableau original. Cela signifie que je dois faire glisser la ligne de nom vers la zone LIGNES :

![ss5-3](https://www.freecodecamp.org/news/content/images/2022/09/ss5-3.png)

Vous pouvez voir que j'ai créé une ligne avec la ligne de nom du tableau original.

Pour effectuer des calculs facilement, vous pouvez utiliser la zone "VALEURS".

![ss6-1](https://www.freecodecamp.org/news/content/images/2022/09/ss6-1.png) 

Je veux voir le nombre de buts marqués par chaque joueur. Donc, je vais faire glisser la ligne "Buts marqués" vers la zone "VALEURS" :

![ss7-1](https://www.freecodecamp.org/news/content/images/2022/09/ss7-1.png)

Vous pouvez voir que je peux directement visualiser le nombre de buts marqués par chaque footballeur.

Vous pouvez également effectuer d'autres calculs dans la zone Valeurs. Il suffit de cliquer sur la liste déroulante en face de la colonne là et de sélectionner "Paramètres du champ de valeur..." :

![ss8-1](https://www.freecodecamp.org/news/content/images/2022/09/ss8-1.png)

Je veux voir le nombre maximum de buts marqués au lieu du total des buts marqués par tous les joueurs. Donc, je vais sélectionner "MAX" et cliquer sur "OK" :

![ss9-1](https://www.freecodecamp.org/news/content/images/2022/09/ss9-1.png)

Maintenant, je peux voir le nombre maximum de buts marqués au lieu du total de tous les buts marqués :

![ss10-1](https://www.freecodecamp.org/news/content/images/2022/09/ss10-1.png) 

### Comment créer des lignes entièrement nouvelles avec un tableau croisé dynamique

Rappelons que j'ai dit que je créerais des lignes supplémentaires pour les Contributions aux buts et le Ratio de buts, également appelé Buts par Match ? Alors, faisons-le.

J'ai besoin des lignes "Passes décisives" et "Buts marqués" pour calculer les contributions aux buts. Donc, je vais m'assurer que les deux sont dans la zone Valeurs :

![ss11-1](https://www.freecodecamp.org/news/content/images/2022/09/ss11-1.png) 

Maintenant, je vais m'assurer que l'onglet "Analyser" est sélectionné, cliquer sur "Champs, Éléments et Ensembles", puis sélectionner "Champ calculé..." :

![ss12-1](https://www.freecodecamp.org/news/content/images/2022/09/ss12-1.png) 

L'interface suivante que vous verrez ressemble à ceci :

![ss13-1](https://www.freecodecamp.org/news/content/images/2022/09/ss13-1.png) 

Ici, je vais faire trois choses :
- taper le nom de la ligne dans le champ nom
- écrire la formule – dans ce cas, "Passes décisives + Buts marqués"
- cliquer sur Ajouter et OK

![new-pivot-table-row](https://www.freecodecamp.org/news/content/images/2022/09/new-pivot-table-row.gif)

![ss14-1](https://www.freecodecamp.org/news/content/images/2022/09/ss14-1.png)

Maintenant, j'ai réussi à créer la ligne Contributions aux buts :

![ss15-1](https://www.freecodecamp.org/news/content/images/2022/09/ss15-1.png)

Pour créer le Ratio de buts, je dois m'assurer que la ligne matchs joués est dans la zone VALEURS :

![ss16-1](https://www.freecodecamp.org/news/content/images/2022/09/ss16-1.png) 

La formule que je vais utiliser est Buts marqués / Matchs joués. Donc, je vais implémenter à nouveau les champs calculés :

![ss17-1](https://www.freecodecamp.org/news/content/images/2022/09/ss17-1.png) 

Je peux maintenant voir le ratio de buts de chaque footballeur :

![ss18-1](https://www.freecodecamp.org/news/content/images/2022/09/ss18-1.png) 

## Comment implémenter une visualisation graphique pour un tableau croisé dynamique
C'est bien de créer un tableau croisé dynamique et d'implémenter des calculs facilement, mais c'est encore mieux de voir la représentation graphique de ce tableau croisé dynamique dans un graphique.

Pour représenter le tableau croisé dynamique dans un graphique :

**Étape 1** : Assurez-vous que l'onglet "Analyser" est sélectionné, puis sélectionnez Graphique croisé dynamique :

![ss19-1](https://www.freecodecamp.org/news/content/images/2022/09/ss19-1.png) 

**Étape 2** : Sélectionnez le type de graphique que vous voulez sur la droite. Il peut s'agir d'un graphique en colonnes, d'un graphique en secteurs ou d'un graphique en barres. Sélectionnez également le format dans la partie supérieure. Il peut être en 2D ou en 3D.

![ss20-1](https://www.freecodecamp.org/news/content/images/2022/09/ss20-1.png) 

Cliquez sur OK lorsque vous êtes satisfait.

![ss21](https://www.freecodecamp.org/news/content/images/2022/09/ss21.png)

C'est le graphique représentant les données.

## Conclusion
Les tableaux croisés dynamiques sont l'une des fonctionnalités les plus puissantes d'Excel. Si vous avez de grands ensembles de données avec lesquels vous devez travailler, un tableau croisé dynamique peut vous faire gagner beaucoup de temps en matière d'analyse et de visualisation.

Les tableaux croisés dynamiques sont bien, mais pouvoir créer différents types de graphiques pour représenter les données est vraiment utile aussi.

J'espère que cet article vous aide à créer un tableau croisé dynamique et des graphiques pour les données avec lesquelles vous travaillez.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec d'autres.