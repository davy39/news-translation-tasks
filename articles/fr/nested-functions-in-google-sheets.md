---
title: Comment utiliser les fonctions imbriquées dans Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-02-23T01:49:44.000Z'
originalURL: https://freecodecamp.org/news/nested-functions-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/nesting-functions-1.jpg
tags:
- name: functions
  slug: functions
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment utiliser les fonctions imbriquées dans Google Sheets
seo_desc: "Data analysis is an extremely valuable skill to have. But to make the most\
  \ of your analysis, it's invaluable to get your data neat and orderly. \nIn this\
  \ article, I'll show you how to combine several functions together to better organize\
  \ your data.\n\ng..."
---

L'analyse de données est une compétence extrêmement précieuse à posséder. Mais pour tirer le meilleur parti de votre analyse, il est inestimable d'avoir vos données bien organisées et ordonnées. 

Dans cet article, je vais vous montrer comment combiner plusieurs fonctions ensemble pour mieux organiser vos données.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/giphy.gif)
_gif de jouets qui se parlent en disant, data, data everywhere_

Google Sheets et Microsoft Excel sont d'excellents terrains d'entraînement pour la programmation informatique. Ils permettent un accès rapide à l'écriture de fonctions qui vous aident à résoudre des problèmes de manière créative, tout comme dans la programmation "réelle". Et, ils offrent également des résultats immédiats avec la possibilité de dépanner les bugs.

Aujourd'hui, nous allons prendre un ensemble de données d'exemple de Kaggle et l'utiliser pour illustrer :

1. Les limites des fonctions simples et intégrées
2. Comment imbriquer des fonctions
3. Comment extraire et compter les valeurs uniques de notre ensemble de données

## Les données et le problème

Nous allons examiner un ensemble de données de Kaggle qui a été extrait de IMDB. Il s'agit d'une liste de 1000 films. La partie qui nous intéresse est la colonne des genres.

Si vous souhaitez suivre, l'**[ensemble de données est ici](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows?select=imdb_top_1000.csv)**, j'ai créé une **[feuille de calcul ici](https://docs.google.com/spreadsheets/d/1-PfjTvHl2olxAmbrs8LAhP2Dkly9Rp5362YUXIe9RRg/edit#gid=987342418)** que vous pouvez suivre et même copier, et j'ai enregistré une vidéo de démonstration ici :

%[https://youtu.be/e1LQnye12-E]

Le problème que nous allons résoudre est le suivant : dans la colonne des genres, nous voulons extraire toutes les valeurs uniques et compter le nombre de fois où elles apparaissent. Donc, combien de films ont le drame comme genre, l'action comme genre... et ainsi de suite.

Si chaque cellule ne contenait qu'un seul genre, ce serait un correctif rapide. Les fonctions intégrées `=UNIQUE()` et `=COUNTIF` résoudraient cela rapidement pour nous.

Cependant, la plupart des films ont plus d'un genre associé :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-217.png)
_List des genres de films dans une feuille de calcul_

Si nous essayons d'utiliser `=UNIQUE()`, nous allons être bloqués car `=UNIQUE()` regarde chaque cellule. Donc, il pensera que la cellule contenant la valeur `Crime, Drama` est une valeur unique en elle-même au lieu de savoir que c'est une liste de deux genres.

Ci-dessous, un exemple de ce qui se passe lorsque l'on utilise `=UNIQUE()` sur une petite partie de notre ensemble de données :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/unique.png)
_utilisation de la fonction Unique dans une feuille de calcul_

Heureusement, les feuilles de calcul sont aussi intelligentes que nous sommes prêts à les rendre. Et nous sommes en mesure d'utiliser une combinaison de fonctions pour extraire les données dont nous avons besoin.

Ci-dessous, nous allons passer en revue les étapes et les fonctions nécessaires pour nettoyer et analyser correctement nos données.

## Les fonctions que nous allons utiliser

Tout d'abord, prenons notre ensemble de données et mettons-le dans une grande liste uniforme où chaque valeur est séparée par des virgules, car c'est le problème ci-dessus.

Pour ce faire, nous allons utiliser la fonction `=JOIN()`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-220.png)
_La fonction join dans Google Sheets_

`=JOIN()` nous permet de concaténer des éléments dans notre ensemble de données avec un délimiteur – dans notre cas, une virgule et un espace : `=JOIN(", ",A2:A1001)`.

Ensuite, nous devons diviser cette énorme liste pour que nous obtenions toutes nos valeurs dans leur propre cellule. Rappelez-vous, c'était le problème initial car la fonction `=UNIQUE()` retourne des cellules uniques.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-221.png)
_Fonction Split dans Google Sheets_

La fonction `=SPLIT()` prend cette énorme liste de valeurs séparées par des virgules et la divise en cellules séparées par le délimiteur que nous spécifions. Dans ce cas, encore une fois, ce sera une virgule et un espace.

Cela diviserait tout sur une rangée incroyablement longue, cependant.

Nous allons donc utiliser la fonction `=TRANSPOSE()` pour l'afficher dans une colonne.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/split.png)
_Fonctions Split et Transposed dans Google Sheets_

Et nous sommes en affaires. Nous pouvons maintenant utiliser notre fonction `=UNIQUE()` originale pour obtenir ces valeurs uniques... et en bonus, la fonction `=SORT()` pour les trier par ordre alphabétique.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/oh-yeah.gif)
_gif d'un homme qui se réjouit silencieusement_

## Comment imbriquer les fonctions

Maintenant que nous savons ce que toutes ces fonctions font, imbriquons-les ensemble dans une cellule pour extraire ces valeurs uniques et les trier dans une liste en une seule fois :

`=UNIQUE(SORT(TRANSPOSE(SPLIT(JOIN(", ",A2:A),", ",FALSE))))`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/boom.gif)
_gif d'une fille disant boom_

Tout comme en algèbre, nous imbriquons les fonctions que nous devons évaluer en premier plus profondément dans l'instruction. Donc, nous avons la fonction `=JOIN()` enveloppée dans la fonction `=SPLIT()` qui est elle-même enveloppée dans la fonction `=TRANSPOSE()`, la fonction `=SORT()` et enfin, à la toute fin, notre fonction `=UNIQUE()`. Le résultat est ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-223.png)
_List complète des genres de films triés_

## Une fonction imbriquée plus courte

À partir de là, nous pouvons maintenant compter les occurrences de chaque genre dans notre liste principale en utilisant la fonction `=COUNTIF()` dans une imbrication similaire, bien que plus petite.

Nous devons d'abord diviser et joindre notre liste comme nous l'avons fait dans l'exemple ci-dessus : `=SPLIT(JOIN(", ",$A$2:$A),", ")`.

Cela devient notre plage pour la fonction `=COUNTIF()`. Ensuite, nous comptons les valeurs dans cette plage si elles sont égales aux cellules qui contiennent nos valeurs de genre uniques.

Pour le genre Action dans la cellule `E19`, voici la fonction `=COUNTIF()` :

`=COUNTIF(SPLIT(JOIN(", ",$A$2:$A),", "),E19)`

Cela retourne `189` comme le nombre de fois où Action apparaît dans notre ensemble de données. Et en copiant la formule pour chacun de nos genres, nous avons maintenant le nombre d'occurrences de chacun des genres.

**Note :** assurez-vous de verrouiller la référence de l'ensemble de données en place lorsque vous copiez la formule en enfermant les références de cellule dans des signes dollar : `$A$2:$A`. Si vous ne le faites pas, alors lorsque vous copiez la formule vers le bas, cette référence se décalera également.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-224.png)
_Nombre de fois où chaque genre apparaît dans l'ensemble de données_

## Conclusion

J'espère que cela a été utile pour vous ! Les fonctions de feuille de calcul sont vraiment un excellent moyen de se lancer dans la programmation ainsi que d'élargir vos compétences en résolution de problèmes. Je continue à aimer optimiser mon entreprise en automatisant grâce aux feuilles de calcul.

📽️ J'adorerais que vous jetiez un coup d'œil à ma chaîne YouTube ici : [https://www.youtube.com/@eamonncottrell](https://www.youtube.com/@eamonncottrell)

Je crée du contenu comme celui-ci toute l'année et apprécierais un like/abonnez-vous. Faites-moi savoir quelles autres vidéos/tutoriels vous bénéficieriez !

📞 Vous pouvez également me trouver sur Linkedin ici : [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)

Passez une excellente journée ! 👋