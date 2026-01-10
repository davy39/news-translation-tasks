---
title: If-Else vs Switch Case en JavaScript – Lequel est le meilleur ?
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-02-26T15:51:01.807Z'
originalURL: https://freecodecamp.org/news/if-else-vs-switch-case-in-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740585035432/f829418f-0efc-4af9-b1c7-7233b6640abc.png
tags:
- name: JavaScript
  slug: javascript
seo_title: If-Else vs Switch Case en JavaScript – Lequel est le meilleur ?
seo_desc: 'JavaScript has been a popular programming language for almost 30 years
  now. Whether you’re using it for web applications, mobile applications, backend
  services, or even desktop applications, you’ll find that JavaScript has deep roots.

  Many of the lib...'
---

JavaScript est un langage de programmation populaire depuis près de 30 ans. Que vous l'utilisiez pour des applications web, des applications mobiles, des services backend ou même des applications de bureau, vous constaterez que JavaScript a des racines profondes.

De nombreuses bibliothèques et frameworks que vous utilisez probablement pour construire des applications web modernes sont basés sur JavaScript, comme React.js, Next.js, Angular, Solid.js, Vue.js et Node.js, pour n'en nommer que quelques-uns.

Bien que ces bibliothèques et frameworks fournissent de nombreuses abstractions utiles pour la programmation de bas niveau, en tant que développeur d'applications, vous devez toujours avoir une solide compréhension des fondamentaux de JavaScript pour pouvoir les utiliser efficacement.

Un concept de programmation très basique est le `Control Flow` (flux de contrôle) et la prise de décision. Et cela n'est pas lié à JavaScript seul – vous le rencontrerez dans la plupart des langages de programmation avec lesquels vous travaillez.

Dans cet article, vous apprendrez deux techniques principales pour gérer le flux de contrôle en JavaScript : l'utilisation de `if-else` et de `switch-case`. Beaucoup d'entre vous connaissent probablement leurs structures et leurs utilisations. Mais l'objectif de cet article est de dresser une comparaison entre les deux, afin qu'à la fin, vous sachiez lequel choisir pour chaque cas d'utilisation.

Cet article est également disponible sous forme de tutoriel vidéo dans le cadre de l'initiative [40 Days of JavaScript](https://www.youtube.com/watch?v=t8QXF85YovE&list=PLIJrr73KDmRw2Fwwjt6cPC_tk5vcSICCu). Veuillez le consulter.

%[https://www.youtube.com/watch?v=Fn_DhBu3VyU]

## Table des matières

* [Qu'est-ce que le flux de contrôle en JavaScript ?](#heading-quest-ce-que-le-flux-de-controle-en-javascript)

* [Comment gérer le flux de contrôle avec le bloc if-else](#heading-comment-gerer-le-flux-de-controle-avec-le-bloc-if-else)

* [Comment gérer le flux de contrôle avec l'instruction switch](#heading-comment-gerer-le-flux-de-controle-avec-linstruction-switch)

* [La comparaison : if-else vs switch-case](#heading-la-comparaison-if-else-vs-switch-case)

* [Avant de terminer...](#heading-avant-de-terminer)

## Qu'est-ce que le flux de contrôle en JavaScript ?

En JavaScript, votre code s'exécute ligne par ligne, en commençant par la première ligne jusqu'à la dernière ligne du fichier JavaScript. Cet ordre d'exécution du code par l'interpréteur JavaScript est appelé `flux de contrôle`.

Parfois, votre programme peut nécessiter des changements dans le flux d'exécution en fonction d'une ou plusieurs conditions. Ces conditions détermineront si un ensemble d'instructions dans le fichier JavaScript doit être exécuté ou non.

Examinons cet exemple de fichier JavaScript (some.js) montré ci-dessous :

![Control FLOW](https://cdn.hashnode.com/res/hashnode/image/upload/v1740121611950/4bcaf223-1d72-4a5d-b9c6-b176e72dd93a.png align="center")

Le fichier contient 12 lignes de code. Une fois ce fichier chargé dans l'environnement JavaScript, l'interpréteur commencera l'exécution à partir de la ligne numéro 1 et procédera ligne par ligne. À la ligne numéro 4, l'interpréteur rencontrera une `instruction de contrôle` qui permettra à l'interpréteur d'exécuter ou de sauter la ligne numéro 5. Dans notre cas, il saute l'exécution de la ligne numéro 5.

Ainsi, le contrôle passe à la ligne 6, exécute chaque ligne et procède à la ligne 9. Ensuite, il rencontre une autre instruction de contrôle pour sauter la ligne 10, commence l'exécution à partir de la ligne 11 et termine à la dernière ligne, la ligne 12.

Il existe deux principales instructions de contrôle en JavaScript que vous devez connaître :

* `if` et `if-else`

* `switch-case`

Tout d'abord, discutons-en avec des exemples pour comprendre comment elles impactent le flux de contrôle de l'exécution du code.

## Comment gérer le flux de contrôle avec le bloc `if-else`

Le mot-clé `if` et la combinaison des mots-clés `if-else` nous aident à créer des instructions de contrôle dans le flux d'exécution du code. Avec `if`, un bloc de code ne sera exécuté que lorsqu'une condition de test est remplie. Une condition remplie retourne `true`, et une condition échouée retourne `false`.

Prenons un exemple : Si vous prenez le bus, vous rentrerez chez vous à l'heure. Maintenant, si vous deviez écrire ce scénario de manière programmatique, vous créeriez une condition pour `cacthingBus`. Ensuite, vous passeriez la condition à `if` en utilisant une paire de parenthèses. Le bloc de code associé à `if` est exécuté si la condition donne un résultat vrai.

```javascript
let catchingBus = true;

// Some code here...

if (catchingBus) {
    console.log("Je rentrerai à la maison à l'heure");
}

// Some other code here...
```

Dans l'extrait de code ci-dessus, le résultat de la condition `catchingBus` est `true`. Ainsi, le flux d'exécution du code entrera dans le bloc if et exécutera la journalisation de la console, `Je rentrerai à la maison à l'heure`. Si vous changez la valeur de la condition en `false`, le bloc if sera ignoré. Dans de tels cas, vous pouvez vouloir gérer un cas d'utilisation alternatif – vous apportez donc un bloc `else` avec le `if`.

Dans l'extrait de code ci-dessous, nous avons à la fois if et else. Dans ce cas, la condition donne un résultat `false`. Ainsi, le bloc `else` sera exécuté et `Je serai en retard pour rentrer à la maison` sera journalisé dans la console.

```javascript
let catchingBus = false;

if (catchingBus) {
    console.log("Je rentrerai à la maison à l'heure");
} else {
    console.log("Je serai en retard pour rentrer à la maison");
}
```

Vous pouvez avoir plus d'une paire de if-else pour gérer des problèmes complexes. Prenons un exemple de système de notation. Si votre score est de 90 ou plus, vous obtenez un A, pour 80 ou plus, un B, pour 70 ou plus, un C, sinon vous échouez.

Écrivons le programme pour cela à l'aide de if-else. Comme nous avons plusieurs conditions à gérer, nous aurons besoin de plusieurs blocs if et de blocs else associés.

```javascript
let score = 76;

if (score >= 90) {
    console.log("Note A");
} else if (score >= 80) {
    console.log("Note B");
} else if (score >= 70) {
    console.log("Note C");
} else {
    console.log("Échec");
}
```

Combiner plusieurs instructions if-else est un excellent moyen de gérer la vérification de plusieurs conditions et de prendre des mesures en fonction d'une condition qui réussit ou échoue.

## Comment gérer le flux de contrôle avec l'instruction `switch-case`

Alors que if-else est idéal lorsque nous vérifions plusieurs conditions possibles, vous pouvez utiliser `switch-case` pour gérer plusieurs conditions basées sur une `valeur unique`.

```javascript
switch(value) {
    case "case 1": // faire quelque chose
    case "case 2": // faire quelque chose
    case "case 3": // faire quelque chose
    case "case 4": // faire quelque chose
    default: // faire quelque chose
}
```

Contrairement au `bloc if`, le `bloc switch` accepte une valeur puis vérifie un cas correspondant pour cette valeur. Lorsqu'un cas est trouvé, JavaScript exécutera le bloc de code pour le cas. L'utilisation d'une instruction `break` quittera le bloc switch. Lorsqu'aucun des cas ne correspond, le `default` sera exécuté.

Dans l'extrait de code ci-dessous, nous vérifions une correspondance basée sur une valeur de position. Ainsi, la valeur de position est passée à l'instruction switch. Maintenant, si la valeur de position est 1, le premier cas sera trouvé car il correspond à la valeur 1. De même, ce sera la même chose pour les positions 2, 3 ou 4. Si nous passons une valeur de position qui n'est pas 1, 2, 3 ou 4, le bloc par défaut sera exécuté.

```javascript
let position = 10;

switch (position) {
    case 1:
        console.log("Imprimer 1");
        break;
    case 2:
        console.log("Imprimer 2");
        break;
    case 3:
        console.log("Imprimer 3");
        break;
    case 4:
        console.log("Imprimer 4");
        break;

    default:
        console.log("Rien ne correspond");
}
```

## La comparaison : if-else vs switch-case

Maintenant, il est temps de comparer chacune de ces approches. En plus de leurs différences syntaxiques, il y a quelques différences et considérations clés que vous devez garder à l'esprit avant d'opter pour l'une plutôt que pour l'autre :

* Utilisez if-else lorsque vous devez gérer des conditions logiques complexes. Mais si vous devez vérifier une valeur fixe comme des nombres, des chaînes, etc., puis la faire correspondre à une valeur de cas spécifique, optez pour switch-case.

* Lorsque vous avez de nombreux blocs if-else, la lisibilité du code commence à se dégrader. Il est beaucoup plus facile de lire les étiquettes de cas pour switch-case.

* S'il y a trop de blocs if-else, la performance peut être plus lente que le bloc switch-case. Dans de nombreux moteurs JavaScript, les instructions switch sont optimisées. Ils utilisent une table de saut pour que le moteur JavaScript saute directement dans le bon cas plutôt que d'évaluer chaque condition séquentiellement.

Comprenons avec un exemple. Consultez l'extrait de code suivant écrit en utilisant les blocs if-else :

```javascript
let value = 3;

if (value === 1) {
    console.log("Un");
} else if (value === 2) {
    console.log("Deux");
} else if (value === 3) {
    console.log("Trois");
} else {
    console.log("Non trouvé");
}
```

Dans ce cas,

* Toutes les instructions if-else seront exécutées séquentiellement. Le moteur JavaScript vérifiera chaque condition une par une jusqu'à ce qu'une correspondance soit trouvée.

* Si la condition correspondante se trouve vers le bas, alors toutes les conditions au-dessus doivent être vérifiées. Ainsi, le if-else peut être plus lent lorsque nous avons un scénario de pire cas pour la correspondance. Dans l'exemple ci-dessus, si la correspondance est pour la valeur 3, l'interpréteur JavaScript termine la vérification des valeurs 1 et 2, avant de vérifier la valeur 3.

Maintenant, le même résultat avec le switch case :

```javascript
let value = 3;

switch (value) {
    case 1:
        console.log("Un");
        break;
    case 2:
        console.log("Deux");
        break;
    case 3:
        console.log("Trois");
        break;
    default:
        console.log("Non trouvé");
}
```

Ici,

* Le moteur JavaScript peut avoir créé la table de saut.

* Le moteur saute directement au cas 3, en ignorant toutes les autres vérifications inutiles, donc ce sera plus rapide. Mais gardez à l'esprit que cette différence de performance est négligeable pour un petit nombre de conditions.

J'espère que ces points vous aideront à choisir plus facilement entre les instructions if-else et switch.

## **Avant de terminer...**

C'est tout. J'espère que vous avez trouvé cet article instructif. Se concentrer sur les fondamentaux de JavaScript vous préparera bien pour un avenir dans le développement web. Consultez mon initiative [40 Days of JavaScript](https://www.youtube.com/watch?v=t8QXF85YovE&list=PLIJrr73KDmRw2Fwwjt6cPC_tk5vcSICCu) si vous souhaitez apprendre JavaScript avec des concepts fondamentaux, des projets et des devoirs gratuitement (pour toujours).

Restez en contact :

* Abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).

* Suivez-moi sur [X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils pour monter en compétences.

* Consultez et suivez mon travail Open Source sur [GitHub](https://github.com/atapas).

* Je publie régulièrement des articles significatifs sur mon [Blog GreenRoots](https://blog.greenroots.info/), vous pourriez les trouver utiles également.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et continuez à apprendre.