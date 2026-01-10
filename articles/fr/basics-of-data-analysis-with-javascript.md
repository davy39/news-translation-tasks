---
title: Comment utiliser JavaScript pour l'analyse de données – Un guide pour débutants
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-01-17T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/basics-of-data-analysis-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-burak-the-weekender-186461.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser JavaScript pour l'analyse de données – Un guide pour débutants
seo_desc: 'Data analysis involves taking data you have and extracting useful information
  from them. During the process, you need to clean the data, present them in a useful
  way, and draw conclusions that can help companies make important decisions.

  Data analysi...'
---

L'analyse de données consiste à prendre les données dont vous disposez et à en extraire des informations utiles. Au cours du processus, vous devez nettoyer les données, les présenter de manière utile et tirer des conclusions qui peuvent aider les entreprises à prendre des décisions importantes.

L'analyse de données est généralement effectuée avec des langages comme Python et R. Très peu de gens savent que vous pouvez également effectuer une analyse de données avec JavaScript, et c'est assez facile.

Cet article se concentre sur les fonctions d'analyse de données les plus basiques que vous pouvez effectuer en JavaScript. Plongeons-nous dans le sujet.

## Comment trouver la moyenne avec JavaScript

Lorsque vous souhaitez trouver la moyenne d'un groupe de nombres, vous les additionnez tous et divisez par le nombre d'éléments que vous avez.

Par exemple, si vous avez un groupe de nombres 2, 5, 7, 9 et 12, vous les additionnez tous et divisez ce résultat par 5 (il y a cinq nombres dans votre groupe). Ainsi, la moyenne est 2+5+7+9+12 = 35, et 35/5 = 7.

La moyenne, en d'autres termes, est le résultat obtenu en divisant la somme de toutes les valeurs de l'ensemble par la longueur ou le nombre d'éléments de l'ensemble.

Prenons cet ensemble d'exemple de nombres aléatoires entre 1 et 1000 :

```javascript
const data = [
    943, 504, 733, 122, 868, 994, 553, 376, 450, 212,
    295, 859, 29, 820, 148, 589, 621, 870, 941, 909,
    725, 160, 198, 568, 409, 625, 207, 338, 162, 439,
    894, 937, 929, 648, 91, 235, 550, 851, 626, 926,
    190, 770, 33, 274, 79, 355, 768, 504, 415, 232,
    33, 327, 100, 1000, 775, 803, 587, 676, 17, 952,
    931, 838, 447, 358, 282, 606, 877, 185, 514, 263,
    887, 725, 270, 716, 762, 633, 900, 948, 786, 28,
    950, 858, 587, 804, 127, 803, 111, 609, 606, 461,
    947, 868, 43, 432, 113, 607, 852, 698, 984, 575
];
```

Pour calculer la moyenne de cet ensemble en JavaScript, vous pouvez utiliser la méthode `array.reduce` (pour obtenir la somme du tableau) ainsi que la méthode `array.length` (pour obtenir le nombre de valeurs dans l'ensemble) pour trouver la moyenne comme ceci :

```javascript
const average = data.reduce((a, b) => a + b) / data.length; // Retourne 552.35
```

Vous pourriez également trouver la moyenne en utilisant une bibliothèque tierce comme [math.js](https://www.npmjs.com/package/mathjs), comme ceci :

```javascript
import { mean } from 'mathjs';

const average = mean(...data); // Retourne 552.35
```

Vous pouvez également trouver la moyenne en utilisant une boucle `for` ou `forEach`.

```javascript
let sum = 0;

for (let datum of data) sum += datum;

const average = sum / data.length; // Retourne 552.35
```

```javascript
let sum = 0;

data.forEach((datum) => sum += datum);

const average = sum / data.length; // Retourne 552.35
```

## Comment trouver le maximum et le minimum avec JavaScript

Lorsque vous travaillez avec des fonctions, le maximum et le minimum sont les valeurs les plus grandes et les plus petites de cette fonction. Vous pouvez les calculer pour une plage spécifique ou pour l'ensemble des valeurs.

En utilisant le même tableau que ci-dessus, nous pouvons obtenir la valeur maximale en utilisant la méthode `max` du module intégré `Math`.

```javascript
const max = Math.max(...data); // Retourne 1000
```

Vous pouvez également obtenir la valeur minimale en utilisant la méthode `min`.

```javascript
const min = Math.min(...data); // Retourne 17
```

Alternativement, vous pouvez également utiliser une bibliothèque tierce comme math.js pour trouver les valeurs maximale et minimale, comme ceci :

```javascript
import { min, max } from 'mathjs';

const maxValue = max(...data); // Retourne 1000
const minValue = min(...data); // Retourne 17
```

Vous pouvez également décider de trouver les valeurs maximale et minimale par vous-même. Vous pouvez le faire en utilisant la méthode `array.sort` et en choisissant les premier et dernier éléments de la liste comme vos valeurs minimale et maximale, respectivement. Ou vous pouvez également le faire en utilisant une boucle et en gardant une trace des valeurs maximale et minimale.

```javascript
const sortedData = data.sort((a, b) => a - b);

const min = sortedData[0]; // Retourne 17
const max = sortedData[sortedData.length - 1]; // Retourne 1000
```

```javascript
let min, max;

for (let datum of data) {
    if (!min || !max) {
        min = datum;
        max = datum;
    } else if (datum < min) min = datum;
    else if (datum > max) max = datum;
}
```

## Comment trouver la somme avec JavaScript

La somme, ou total, est le résultat de l'addition d'une séquence de nombres. Dans la section expliquant la moyenne ci-dessus, nous avons vu une façon d'obtenir la somme d'une séquence en utilisant `array.reduce`.

```javascript
const sum = data.reduce((a, b) => a + b); // Retourne 55235
```

Une autre méthode très facile serait d'utiliser la méthode `sum` de math.js.

```javascript
import { sum } from 'mathjs';

const sumValue = sum(...data); // Retourne 55235
```

Vous pouvez également trouver la somme en utilisant une boucle si vous le souhaitez.

## Comment trouver le mode avec JavaScript

Le mode d'un ensemble de données représente la valeur qui apparaît le plus grand nombre de fois dans l'ensemble. Si vous analysez cet ensemble de données, c'est la valeur que vous êtes le plus susceptible de trouver.

Vous pouvez trouver l'élément le plus fréquent d'un tableau en itérant sur le tableau, en utilisant un objet pour mapper chaque valeur à son compte, et en parcourant cet objet à la fin pour trouver la valeur la plus élevée.

Pour faciliter l'illustration, modifiez le tableau `data` que nous avons utilisé jusqu'à présent, comme ceci :

```javascript
data[99] = 33;
```

Maintenant, vous pouvez trouver le mode comme suit :

```javascript
let frequency = {};

for (let datum of data) {
    if (frequency[datum]) frequency[datum] += 1;
    else frequency[datum] = 1;
}

let highestFrequency = 0;
let modeValue = 0; 

for (let datum in frequency) {
    if (frequency[datum] > highestFrequency) {
        highestFrequency = frequency[datum];
        modeValue = datum;
    }
}
```

Vous pouvez en faire une fonction si vous devez le faire plus d'une fois.

Vous pouvez trouver le mode plus facilement en utilisant la méthode `mode` de la bibliothèque math.js :

```javascript
const modeValue = mode(...data); // Retourne 33
```

## Comment trouver la médiane avec JavaScript

Si vous souhaitez trouver la médiane d'un ensemble de données, vous devez simplement trouver la valeur exactement au milieu de l'ensemble. Cela signifie que les données doivent être ordonnées, ou triées par ordre croissant ou décroissant – sinon la valeur du milieu n'a aucune signification.

Vous pouvez trouver la médiane en triant d'abord le tableau, puis en sélectionnant l'élément à la position du milieu si le tableau a un nombre impair d'éléments. Si le tableau a un nombre pair d'éléments, vous sélectionnez les deux éléments du milieu et trouvez leur moyenne.

```javascript
const sortedArray = data.sort((a, b) => a - b);

const middlePosition = Math.floor(data.length / 2);

const median = data.length % 2 == 0 ? (sortedArray[middlePosition] + sortedArray[middlePosition - 1]) / 2 : sortedArray[middlePosition]; // Retourne 597.5
```

Alternativement, vous pouvez trouver la médiane en utilisant la méthode `median` de math.js.

```javascript
import { median } from 'mathjs';

const medianValue = median(...data); // Retourne 597.6
```

## **Résumé**

J'espère que vous comprenez maintenant comment effectuer ces fonctions d'analyse de données de base en utilisant JavaScript. La bibliothèque math.js est l'une des nombreuses bibliothèques JavaScript qui contiennent plusieurs fonctions utiles pour faciliter l'analyse de données avec JavaScript.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me rejoindre sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, c'est facile et c'est gratuit !