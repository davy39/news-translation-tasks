---
title: Comment travailler avec les chaînes de caractères en JavaScript – Conseils
  pour une concaténation efficace
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-29T20:39:11.000Z'
originalURL: https://freecodecamp.org/news/efficient-string-building-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/JavaScript-Strings.png_copy.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment travailler avec les chaînes de caractères en JavaScript – Conseils
  pour une concaténation efficace
seo_desc: "By Andrey Germanov\nEverything you see in browser – except images and videos\
  \ – is a string. \nThat's why you should learn how to work with them properly. This\
  \ will dramatically increase the performance of your web applications, both on the\
  \ frontend and..."
---

Par Andrey Germanov

Tout ce que vous voyez dans le navigateur – à l'exception des images et des vidéos – est une chaîne de caractères.

C'est pourquoi vous devriez apprendre à travailler avec elles correctement. Cela augmentera considérablement les performances de vos applications web, tant sur le frontend que sur le backend.

## Comment fonctionne la concaténation de chaînes par défaut – et ses problèmes

Que devez-vous savoir sur les chaînes de caractères en programmation ? Le `string` est un type de données primitif qui contient un tableau de caractères. Les valeurs des types de données primitifs sont immuables, donc la valeur d'une chaîne ne peut pas être modifiée après son instanciation. Cela est vrai pour la plupart des langages de programmation, y compris JavaScript.

Mais attendez, lorsque vous faites ceci :

```javascript
let hello = "Hello";
hello += " world";
console.log(hello);
```

Vous verrez **Hello world** sur la console, ce qui signifie que la valeur de la variable `hello` a changé. Comment est-ce possible ? Comment JavaScript peut-il changer la valeur d'une variable de chaîne et la garder immuable en même temps ?

Cela se produit parce que JavaScript n'ajoute pas directement la deuxième chaîne à la première. Au lieu de cela, il crée une troisième chaîne vide, copie les valeurs des deux chaînes dans celle-ci, et enfin réassigne la variable "hello" à cette troisième chaîne.

De cette manière, la valeur de la troisième chaîne est définie une seule fois et les valeurs des deux chaînes initiales restent inchangées pour respecter la règle d'immuabilité.

Voici à quoi ressemble tout le processus de concaténation de chaînes :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-99.png)
_1) Créer une plage vide en mémoire pour contenir la nouvelle chaîne. 2) Copier la première chaîne dedans. 3) Copier la deuxième chaîne dedans 4) Réassigner la variable "hello" à la nouvelle chaîne. 5) Libérer les plages de mémoire qui contenaient les deux premières chaînes "Hello" et "world"._

Voyez-vous un problème ici ? Que pouvons-nous dire sur les performances de cette opération ? Il semble qu'elle effectue jusqu'à cinq fois plus d'opérations que nécessaire et utilise deux fois plus de mémoire à l'étape 3 pour contenir les mêmes données.

D'un côté, ce n'est pas un gros problème si nous voulons simplement concaténer deux chaînes, car les ordinateurs peuvent effectuer des millions d'opérations en une seconde. Mais le problème devient plus sérieux si nous devons construire de longues chaînes.

Supposons que nous devons construire une grande portion de contenu HTML à partir d'un tableau de données externes dans une boucle. Dans ce cas, la chaîne HTML peut devenir énorme pendant ce processus et JavaScript créera une copie de cette chaîne à chaque itération de la boucle.

Par exemple, voyons le code qui construit une énorme chaîne dans une boucle, en concaténant la chaîne initiale cent millions de fois.

```javascript
let str = "Hello";

console.log("START",new Date().toUTCString());

for (let index=0;index<100000000;index++) {
    str += "!";
}

console.log("END",new Date().toUTCString());
console.log(str.length);
```

Ce code ajoute le symbole "!" à la chaîne cent millions de fois. Dans un exemple réel, vous pouvez supposer qu'au lieu du symbole '!' ce serait des données réelles provenant d'une source externe qui devraient être affichées plus tard.

De plus, ce code affiche la date et l'heure actuelles avant et après la boucle, ce qui aide à mesurer le temps que cela prend. Enfin, il affiche la longueur de la chaîne construite.

Lorsque j'ai exécuté cela dans mon navigateur Google Chrome, cela a pris un certain temps pour se terminer. Enfin, il a affiché ce qui suit sur la console JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-100.png)
_La console JavaScript montre que le code d'une concaténation de chaînes de base a créé une chaîne de 100000005 caractères en 1 minute 26 secondes._

Comme vous pouvez le voir, cela a pris 1 minute 26 secondes et a affiché la longueur correcte de la chaîne concaténée. Mais lorsque j'ai exécuté cela sur un autre ordinateur, ce code a fait planter le navigateur et j'ai vu la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-101.png)
_Le plantage du navigateur web_

Si vous vous souvenez de l'algorithme de base de la concaténation de chaînes, décrit ci-dessus, il devrait être clair pourquoi cela peut se produire.

L'algorithme de concaténation de chaînes par défaut est trop inefficace et gaspille beaucoup de mémoire. Dans cet exemple, il copie de 1 à cent millions de caractères cent millions de fois lors de l'itération dans la boucle. La quantité de mémoire utilisée pour cela est même difficile à réaliser.

Cela signifie que le fait que le programme plante ou non dépend de la quantité de mémoire libre disponible et de la manière dont le garbage collector de mémoire fonctionne dans une implémentation concrète du moteur JavaScript pour effacer les chaînes temporaires inutilisées.

## Comment améliorer l'algorithme de concaténation de chaînes par défaut

L'algorithme de concaténation de chaînes JavaScript que nous avons discuté ci-dessus ne prétend pas être académiquement précis. Différentes implémentations de moteurs JavaScript peuvent utiliser différentes optimisations de gestion de chaînes et mécanismes de gestion de mémoire.

Mais vous ne devriez pas compter sur le fait que votre code s'exécutera toujours dans de tels moteurs.

Par exemple, dans la dernière version de Google Chrome au moment de la rédaction de cet article, la concaténation de chaînes fonctionnait comme montré dans les captures d'écran ci-dessus. Le but de cet article est donc de montrer comment travailler avec les chaînes plus efficacement, indépendamment de la manière dont cela est implémenté par défaut.

Nous devrions définitivement trouver un moyen de faire exactement ce dont nous avons besoin en concaténant deux chaînes en utilisant une seule opération. De nombreux autres langages de programmation, comme Java ou Go (qui utilisent également des chaînes immuables) ont un outil appelé StringBuilder. Il s'agit d'un objet auxiliaire qui vous permet de construire une chaîne à partir d'éléments de tableaux ou d'autres objets mutables.

JavaScript n'a pas cette fonctionnalité intégrée, mais il n'est pas difficile d'implémenter une idée similaire par vous-même.

Vous pouvez écrire la même chaîne de manière différente :

```javascript
let hello = ["Hello"];
```

Ce n'est pas une chaîne – plutôt, il s'agit d'un tableau avec une chaîne. Contrairement aux chaînes, les tableaux sont mutables et vous pouvez simplement les modifier en ajoutant des éléments. Cela signifie que si vous exécutez ceci :

```javascript
hello.push(" world");

```

JavaScript modifiera simplement le tableau en ajoutant l'élément " world" à la fin. Cela sera fait en une seule opération après laquelle le tableau contiendra ce qui suit :

```javascript
["Hello"," world"]

```

De cette manière, vous pouvez concaténer autant de chaînes que vous le souhaitez à ce tableau à un coût très faible.

Enfin, pour créer la chaîne à partir de celui-ci, vous pouvez exécuter l'opération `join` sur le tableau :

```javascript
hello = hello.join("");
console.log(hello);

```

Après cela, la sortie de la variable "hello" contiendra la chaîne "Hello world". En fait, l'opération join crée également une chaîne vide puis copie les éléments du tableau dedans. Mais cela ne se produit qu'une seule fois (au lieu de chaque fois lors de la concaténation de chaînes).

Cette approche augmente considérablement la vitesse de concaténation de chaînes dans une boucle. Changeons l'exemple de boucle pour utiliser le tableau au lieu de la chaîne :

```javascript
let str = ["Hello"];

console.log("START",new Date().toUTCString());

for (let index=0;index<100000000;index++) {
    str.push("!");
}

str = str.join("");

console.log("END",new Date().toUTCString());
console.log(str.length);

```

Après avoir exécuté cela sur le même navigateur, j'ai reçu la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-102.png)
_La console JavaScript montre que le code de concaténation de chaînes utilisant un tableau a créé une chaîne de 100000005 caractères en 8 secondes._

Comme vous pouvez le voir, le même résultat a été obtenu en 8 secondes, ce qui est 10 fois plus rapide que la concaténation de chaînes régulière.

## Réflexions finales

Comme vous pouvez le voir, en changeant seulement trois lignes de code, vous pouvez augmenter considérablement les performances de votre pipeline de traitement de données.

Dans le cadre de ma pratique, j'ai eu un client dont le site web subissait des ralentissements dus à une gestion inefficace des chaînes qu'il avait tenté de résoudre en mettant en cache le contenu dans CloudFlare. Il a également sérieusement envisagé de passer à AWS pour augmenter le débit des données afin de résoudre ces problèmes. Mais il a suffi de faire une revue de code pour le corriger.

Vous pouvez utiliser la méthode décrite dans ce tutoriel lors de la construction de chaînes dans une boucle à partir de flux de données externes de taille variable en JavaScript. Il suffit d'ajouter des chaînes à un tableau une par une, et enfin de les joindre en une chaîne avant la sortie.

D'autres langages de programmation recommandent d'utiliser des objets internes StringBuilder ou StringBuffer pour la concaténation de chaînes.

Pour JavaScript, nous avons construit un simple StringBuilder qui ne peut que ajouter des chaînes. Pour la pratique, vous pouvez l'étendre et ajouter différentes méthodes pour "append", "insert" ou "remove" des chaînes d'un tableau. Vous pourriez également créer une classe qui encapsule une variable de tableau avec des fonctions pour manipuler des sous-chaînes dans ce tableau et construire la chaîne finale à partir de celui-ci lorsque cela est nécessaire.

### Certaines limitations à cette méthode

Lors de l'ajout d'éléments à un tableau, il est important de garder à l'esprit les limites existantes sur le nombre d'éléments de tableau. Si vous ne les prenez pas en compte, vous pourriez rencontrer l'erreur "RangeError: invalid array range". Vous pouvez [en apprendre plus sur les limites ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Invalid_array_length).

Si le nombre de lignes à ajouter dans la boucle dépasse ces limites, vous devrez alors périodiquement vider le tableau dans des tampons de chaînes temporaires puis fusionner ces tampons.

Pour vous aider à travailler avec les chaînes encore plus efficacement, il existe d'autres grands algorithmes de gestion de chaînes disponibles.

L'un des plus rapides d'entre eux est basé sur une structure de données appelée "Rope". Il a été inventé pour gérer rapidement les opérations sur de grandes chaînes. Vous pouvez [en lire plus ici](https://en.wikipedia.org/wiki/Rope_(data_structure)). Cela est plus complexe que la méthode discutée ci-dessus, mais vous pouvez commencer par réutiliser l'une des implémentations JavaScript de la `Rope` dans vos projets (vous pouvez les trouver [ici](https://github.com/component/rope) et [ici](https://github.com/josephg/jumprope)).

## Merci d'avoir lu !

Bonne chance et bon codage à tous :)

N'hésitez pas à me connecter et me suivre sur les réseaux sociaux ci-dessous où je publie des annonces sur mes prochains articles, similaires à celui-ci et d'autres nouvelles sur le développement logiciel :

LinkedIn: [https://www.linkedin.com/in/andrey-germanov-dev/](https://www.linkedin.com/in/andrey-germanov-dev/)
Facebook: [https://web.facebook.com/AndreyGermanovDev](https://web.facebook.com/AndreyGermanovDev)
Twitter: [https://twitter.com/GermanovDev](https://twitter.com/GermanovDev)