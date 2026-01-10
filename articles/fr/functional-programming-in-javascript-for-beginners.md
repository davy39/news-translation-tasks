---
title: Programmation Fonctionnelle en JavaScript pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-25T16:53:00.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-javascript-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60398767a675540a2292447c.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: Programmation Fonctionnelle en JavaScript pour Débutants
seo_desc: 'By Nahla Davies

  Functional programming is not a new approach to coding, but it has grown in popularity
  in recent years.

  This is because, once programmers understand the basics behind the technique (and
  are able to write clean and reliable code using ...'
---

Par Nahla Davies

La programmation fonctionnelle n'est pas une nouvelle approche de la programmation, mais elle a gagné en popularité ces dernières années.

C'est parce que, une fois que les programmeurs comprennent les bases de cette technique (et sont capables d'écrire du code propre et fiable en l'utilisant), les applications écrites en utilisant une approche fonctionnelle sont beaucoup plus faciles à utiliser.

Pour cette raison, il vaut la peine de comprendre la programmation fonctionnelle une fois que vous avez travaillé avec ce [guide du débutant en JavaScript](https://www.freecodecamp.org/news/the-complete-javascript-handbook-f26b2c71719c/).

Si vous travaillez fréquemment avec JavaScript, utiliser cette approche peut vous faire gagner du temps et rendre votre code plus facile à utiliser et potentiellement plus sécurisé.

Dans cet article, nous examinerons les principes de base de la programmation fonctionnelle, puis nous décrirons quelques-uns des outils clés pour utiliser cette approche en JavaScript.

## Programmation Impérative vs. Fonctionnelle

Les origines de la programmation fonctionnelle remontent aux années 1930 avec l'invention du Lambda Calcul.

C'était une approche de calcul qui [cherchait à définir des tâches et fonctions communes](https://en.wikipedia.org/wiki/Lambda_calculus) non pas comme la manipulation structurelle de structures de données (comme les tableaux et les listes), mais plutôt comme des fonctions mathématiques effectuées sur celles-ci.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-144.png)
_[Source de l'Image](https://android.jlelse.eu/how-to-wrap-your-imperative-brain-around-functional-reactive-programming-in-rxjava-91ac89a4eccf)_

Cela peut sembler assez abstrait, surtout si vous êtes nouveau en programmation. Mais en fait, la différence entre une approche fonctionnelle et impérative peut être exprimée assez succinctement en utilisant un exemple. Jetez un coup d'œil à ceux-ci :

### Impérative :

```js
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

function getOdds(arr) {
  let odds = [];
  for (let i = 0; i < arr.length + 1; i++) {
    if (i % 2 !== 0) {
      odds.push(i);
    }
  }
  return odds;
}

console.log(getOdds(arr)); // logs [1, 3, 5, 7, 9]
```

### Fonctionnelle :

```js
function getOdds2(arr){
return arr.filter(num => num % 2 !== 0)
}console.log(getOdds2(arr))
// logs [ 1, 3, 5, 7, 9 ]
const getOdds3 = arr => arr.filter(num => num % 2 !== 0)console.log(getOdds3(arr))
// logs [ 1, 3, 5, 7, 9 ]
```

Comme vous pouvez le voir, la manière dont ces programmes fonctionnent est assez différente.

L'approche impérative consiste à définir une structure de données, puis à la manipuler afin d'obtenir la sortie dont nous avons besoin. Dans une approche fonctionnelle, nous utilisons des fonctions de filtrage pour définir une fonction programmée, puis nous l'invoquons selon les besoins.

Bien sûr, une grande partie de la complexité de [comment fonctionne la programmation fonctionnelle](https://www.freecodecamp.org/news/an-introduction-to-the-basic-principles-of-functional-programming-a2c2a15c84/) est cachée à l'utilisateur final, et également au programmeur s'il utilise un framework de développement front-end.

Mais les avantages de l'utilisation d'une approche fonctionnelle sont clairs même à partir de cet exemple – ce paradigme entraîne un code plus court qui est plus facile à lire, à comprendre et à auditer.

## Pourquoi utiliser la programmation fonctionnelle ?

En plus de cet avantage de base, il y a un certain nombre d'autres avantages à utiliser la programmation fonctionnelle.

Beaucoup de ces avantages découlent du simple fait que le code fonctionnel est plus facile à lire que le code défini de manière impérative. Parce qu'un humain peut facilement voir comment un programme fonctionnel fonctionne, plutôt que de devoir décomposer le code pour le comprendre, de nombreux aspects des tests sont simplifiés.

### La programmation fonctionnelle assure l'intégrité du code avec les tests de pénétration

Les tests de pénétration deviennent plus efficaces lorsque le code est lisible par l'homme. Cela facilite l'évaluation de l'intégrité du code fonctionnel.

Selon la développeuse de logiciels Barbara Ericson de [Cloud Defense](https://www.clouddefense.ai/blog/penetration-testing), les tests de pénétration doivent toujours être effectués sur les applications JavaScript, et une approche fonctionnelle peut aider à rendre cela plus rigoureux.

Cette facilité de lecture simplifie également de nombreux autres processus de gestion qui s'appliquent au développement de nouveaux codes et applications.

Dans les approches fonctionnelles, les processus de conformité sont beaucoup plus faciles, car les programmeurs n'ont pas à se soucier autant de l'exécution de leur code. Cela signifie que les parties d'un programme qui traitent des données sensibles peuvent être isolées et évaluées séparément du reste du programme.

### La programmation fonctionnelle rend le code plus facile à lire

Les avantages des approches fonctionnelles ne se limitent pas à l'évaluation du code, cependant. Ils s'étendent également au processus de développement.

En fait, les approches fonctionnelles s'appuient et amplifient les [avantages et inconvénients](https://www.freecodecamp.org/news/the-advantages-and-disadvantages-of-javascript/) de JavaScript lui-même.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-145.png)
_[Source de l'Image](https://itnext.io/why-are-we-creating-a-javascript-only-world-wide-web-db8c3a340b9)_

En rendant le code plus facile à lire, vous pouvez impliquer beaucoup plus de groupes de personnel dans le processus de développement, même s'ils n'ont pas une compréhension approfondie de JavaScript.

C'est un principe clé de l'approche DevOps, qui [peut aider à atténuer les vulnérabilités](https://privacycanada.net/how-to-fight-common-java-security-vulnerabilities-from-devops/) dans votre code JavaScript. C'est aussi un principe facilité par l'adoption d'une approche fonctionnelle de votre codage.

## Outils clés pour la programmation fonctionnelle

Il y a un certain nombre d'outils et de concepts clés dont vous devez être conscient lorsqu'il s'agit de mettre en œuvre des approches fonctionnelles. Examinons-les.

### 1. Fonctions pures et impures

Au niveau le plus basique, une approche fonctionnelle cherche à manipuler les données sans les muter. Cela signifie qu'une « fonction fonctionnelle » prendra des données, effectuera des calculs et retournera un résultat (et tout cela sans réécrire aucune partie de la structure de données elle-même).

Les fonctions qui fonctionnent de cette manière sont appelées fonctions « pures », et celles qui ne le font pas sont appelées « impures ».

```js
 
function getSquare(items) {
  var len = items.length;
  for (var i = 0; i < len; i++) {
    items[i] = items[i] * items[i];
  }
  return items;
}
```

L'idée générale ici est de laisser les données avec lesquelles vous travaillez complètement intactes.

Si vous souhaitez fusionner deux tableaux, vous ne devez pas utiliser la stratégie `Array.prototype.push()` (qui écrasera les données originales). Utilisez plutôt la fonction `Array.prototype.concat()`, qui créera un nouveau tableau de « travail » pour vous.

### 2. Fonctions anonymes

Les fonctions anonymes sont également une partie importante de la programmation fonctionnelle, et ont leurs racines dans le Lambda Calculus.

Les fonctions anonymes, comme leur nom l'indique, n'ont pas de nom explicitement défini. Au lieu de cela, ce sont des fonctions qui sont assignées à des variables, et invoquées via celles-ci.

```js
 alert((function(x) {
    return !(x > 1)
      ? 1
      : arguments.callee(x - 1) * x;
  })(20));
```

L'avantage de faire cela est que, tant que vous êtes capable de garder une trace des fonctions assignées à quelles variables, elles peuvent être invoquées très facilement, et passées d'un module à un autre avec rien de plus qu'un appel de variable. Cela vous donne une nouvelle façon puissante et flexible de travailler avec les fonctions.

### 3. Fonctions récursives

L'utilisation de fonctions récursives est une autre marque de la programmation fonctionnelle. Bien que l'idée générale de récursion soit familière même aux programmeurs débutants, la programmation fonctionnelle va encore plus loin en définissant des fonctions qui s'appellent elles-mêmes.

```js
function countDown(fromNumber) {
    console.log(fromNumber);

    let nextNumber = fromNumber - 1;

    if (nextNumber > 0) {
        countDown(nextNumber);
    }
}
countDown(3);
```

Cela rend la mise en œuvre de la récursion beaucoup plus simple – largement parce que les programmeurs n'ont pas besoin d'utiliser des boucles pour cela.

Cependant, cela comporte également des dangers. Plus précisément, avoir une fonction qui s'appelle elle-même rend beaucoup plus facile la création accidentelle de boucles infinies, alors prenez soin de soutenir chaque fonction récursive avec une méthode rigoureuse pour arrêter l'exécution.

## Conclusion

Bien que ces trois concepts soient typiques de la programmation fonctionnelle, en vérité, la gamme de façons dont le paradigme peut être appliqué signifie qu'il s'agit davantage d'une philosophie que d'un ensemble d'outils et de processus bien conçus.

Faites quelques pas dans le monde passionnant de la programmation fonctionnelle, et vous commencerez à voir son influence partout. En fait, elle informe de nombreuses [pratiques JavaScript les plus courantes](https://www.freecodecamp.org/news/what-is-javascript/) utilisées aujourd'hui.

En d'autres termes, bien que la programmation fonctionnelle semble simple en surface, elle a des conséquences profondes sur la manière dont vous codez. C'est pourquoi il vaut la peine de l'apprendre, même si vous ne l'utilisez pas tout le temps.