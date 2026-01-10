---
title: Comment construire une heat map dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-24T16:06:58.000Z'
originalURL: https://freecodecamp.org/news/a-heat-map-implementation-in-typescript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0ad740569d1a4ca4a1a.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Heat map
  slug: heat-map
- name: TypeScript
  slug: typescript
seo_title: Comment construire une heat map dans React
seo_desc: 'By Jeff M Lowery

  Heat maps are a great way of visualizing correlations among two data sets.  With
  colors and gradients, it is possible to see patterns in the data almost instantly.

  I went searching for a heat map implementation in npm, but was unable...'
---

Par Jeff M Lowery

Les heat maps sont un excellent moyen de visualiser les corrélations entre deux ensembles de données. Avec des couleurs et des dégradés, il est possible de voir des motifs dans les données presque instantanément.

J'ai cherché une implémentation de heat map dans npm, mais je n'ai pas trouvé celle que j'aimais, alors [j'ai écrit la mienne](https://github.com/JeffML/jsheatmap). C'est encore un travail en cours, mais il fournit une fonctionnalité de base.

Il y a en fait deux parties à l'implémentation : [jsheatmap](https://github.com/JeffML/jsheatmap) prend des en-têtes et des données de lignes pour produire un objet JSON où l'entrée brute est mise à l'échelle de 0.0 à 1.0, puis les couleurs RVB sont mappées à ces valeurs mises à l'échelle. Je dois avouer que la plupart de cela avait déjà été élaboré par Andrew Noske, qui a fourni une [implémentation partielle en C++](http://www.andrewnoske.com/wiki/Code_-_heatmaps_and_color_gradients) dans son blog. La translittération de C++ en TypeScript a été relativement facile.

La deuxième partie est une présentation HTML des données JSON retournées par jsheatmap. Cela serait typiquement de la responsabilité de l'utilisateur du module jsheatmap, mais j'ai construit une [application React polyvalente](https://github.com/JeffML/sternomap) qui démontre comment les cellules de tableau HTML peuvent être utilisées comme représentation de heat map.

## Les bases

Tout d'abord, installez jsheatmap :

`npm i -S jsheatmap`

Comme mentionné, jsheatmap a été écrit en TypeScript, mais npm installera la version JavaScript générée du programme TypeScript, qui est ce que votre application utilisera.

Ensuite, importez les composants jsheatmap. 

`import HeatMap, { Style } from "jsheatmap"`

Le composant `Style` n'est pas strictement requis. À l'heure actuelle, il n'y a que deux styles : SIMPLE et FANCY. FANCY est le style par défaut, qui utilise un dégradé de 5 couleurs pour les données RVB de la heat map. SIMPLE utilise un dégradé de trois couleurs, que vous pourriez préférer pour des ensembles de données plus petits. Le style est passé à la méthode `getData()`, comme il sera montré plus tard.

Instanciez une HeatMap avec des en-têtes (noms de colonnes) et des données de lignes : 
`const heatMap = new HeatMap(headings, rows)`

où headings est un tableau de chaînes (en-têtes de colonnes) et rows est un tableau d'étiquettes et de données de cellules. Par exemple :

```js
// Jours de pluie dans les mois d'été, par année
const headings = ["June", "July", "August", "September"]  // les mois
const rows = [["2015", [9, 5, 6, 8]],   // les années et les jours de pluie par mois
   ["2016", [7, 5, 10, 7]],
   ["2017", [7, 4, 3, 9]],
   ["2018", [10, 5, 6, 8]],
   ["2019", [8, 9, 3, 1]],]
```

## Conversion en RVB

Maintenant, il est temps d'obtenir les données de la heat map :

```js
// const data = heatMap.getData({ style: Style.SIMPLE });
const data = heatMap.getData();
```

Le style par défaut est FANCY (dégradé de cinq couleurs) alors que SIMPLE utiliserait un dégradé de trois couleurs pour le mappage RVB.

Les valeurs des cellules sont ensuite mises à l'échelle, les unes par rapport aux autres, avec des valeurs d'échelle déterminées par les valeurs haute et basse de l'entrée. Une fois que toutes les entrées ont été mises à l'échelle de 0.0 à 1.0, elles peuvent être mappées à des valeurs de couleur RVB. Toutes ces données sont retournées par getData() :

```json
{
  "headings": [
    "Jun",
    "Jul",
    "Aug",
    "Sep"
  ],
  "high": 9,
  "low": 4,
  "rows": [
    {
      "label": "2015",
      "cells": {
        "values": [
          7,
          5,
          6,
          8
        ],
        "colors": [
          {
            "red": 0.6249999999999998,
            "green": 1,
            "blue": 0
          },
          {
            "red": 0,
            "green": 0.588235294117647,
            "blue": 1
          },
          {
            "red": 0,
            "green": 1,
            "blue": 0.625
          },
          {
            "red": 1,
            "green": 0.588235294117647,
            "blue": 0
          }
        ],
        "scales": [
          0.6,
          0.2,
          0.4,
          0.8
        ]
      }
    },
    {
      "label": "2016",
      "cells": {
        "values": [
          7,
          5,
          5,
          7
        ],
        "colors": [
          {
            "red": 0.6249999999999998,
            "green": 1,
            "blue": 0
          },
          {
            "red": 0,
            "green": 0.588235294117647,
            "blue": 1
          },
          {
            "red": 0,
            "green": 0.588235294117647,
            "blue": 1
          },
          {
            "red": 0.6249999999999998,
            "green": 1,
            "blue": 0
          }
        ],
        "scales": [
          0.6,
          0.2,
          0.2,
          0.6
        ]
      }
    },
    {
      "label": "2017",
      "cells": {
        "values": [
          7,
          4,
          5,
          9
        ],
        "colors": [
          {
            "red": 0.6249999999999998,
            "green": 1,
            "blue": 0
          },
          {
            "red": 0,
            "green": 0,
            "blue": 1
          },
          {
            "red": 0,
            "green": 0.588235294117647,
            "blue": 1
          },
          {
            "red": 1,
            "green": 0,
            "blue": 0
          }
        ],
        "scales": [
          0.6,
          0,
          0.2,
          1
        ]
      }
    },
    {
      "label": "2018",
      "cells": {
        "values": [
          6,
          5,
          7,
          8
        ],
        "colors": [
          {
            "red": 0,
            "green": 1,
            "blue": 0.625
          },
          {
            "red": 0,
            "green": 0.588235294117647,
            "blue": 1
          },
          {
            "red": 0.6249999999999998,
            "green": 1,
            "blue": 0
          },
          {
            "red": 1,
            "green": 0.588235294117647,
            "blue": 0
          }
        ],
        "scales": [
          0.4,
          0.2,
          0.6,
          0.8
        ]
      }
    },
    {
      "label": "2019",
      "cells": {
        "values": [
          8,
          6,
          6,
          8
        ],
        "colors": [
          {
            "red": 1,
            "green": 0.588235294117647,
            "blue": 0
          },
          {
            "red": 0,
            "green": 1,
            "blue": 0.625
          },
          {
            "red": 0,
            "green": 1,
            "blue": 0.625
          },
          {
            "red": 1,
            "green": 0.588235294117647,
            "blue": 0
          }
        ],
        "scales": [
          0.8,
          0.4,
          0.4,
          0.8
        ]
      }
    }
  ]
}
```

[Pour l'application de démonstration](https://github.com/JeffML/sternomap), j'utilise React pour générer un tableau avec chaque élément <td> dont l'arrière-plan est stylisé comme suit : 


```js
const background = (rgb) => {	
    return `rgb(${rgb.red * 100}%, ${rgb.green * 100}%, ${rgb.blue * 100}%)`;
}
```

Où `rgb()` est la fonction CSS intégrée pour les couleurs RVB, et le paramètre `rgb` passé provient des couleurs des cellules de la ligne générée par `getData()`. Pour exécuter l'implémentation, clonez d'abord le dépôt :

`git clone [https://github.com/JeffML/sternomap.git](https://github.com/JeffML/sternomap.git)`

puis allez dans le dossier sternomap et exécutez :

`npm install`

finement :

`npm run start`

En aparté : l'application a été initialement générée en utilisant [Create React App](https://create-react-app.dev/docs/getting-started), et le fichier [README.md](https://github.com/JeffML/sternomap) explique tout cela en détail. 

## Le résultat

Une fois que le script a terminé, il chargera une page dans votre navigateur (j'utilise Chrome). Voici un aperçu :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/rainy.png)

Cela montre les jours de pluie par mois dans chaque cellule, par année. À partir de cela, vous pouvez voir que les mois les plus secs sont juillet et août, avec le plus humide étant septembre. Le nombre à l'intérieur de chaque cellule est la valeur mise à l'échelle de l'entrée brute (jours de pluie), donc les jours de pluie les moins nombreux étaient en juillet 2017, et les plus nombreux en septembre de cette année-là.

### Une palette de couleurs

Je peux générer un ensemble de données où la valeur de chaque cellule est la somme de ses coordonnées x + y. Pour les étiquettes de ligne, j'utilise le module npm [casual](https://www.npmjs.com/package/casual) pour les créer.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bigdatamap.png)

## Conclusion

J'ai quelques projets pour utiliser cette implémentation de heat map dans d'autres projets, ce qui nécessitera certainement des changements dans l'API, mais les bases devraient rester les mêmes. Si vous décidez d'essayer cela et que vous le trouvez utile, faites-le moi savoir.