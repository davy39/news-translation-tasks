---
title: Devriez-vous apprendre TypeScript ? Avantages et inconvénients de TS expliqués
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-05-10T14:50:13.000Z'
originalURL: https://freecodecamp.org/news/should-you-learn-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/typescript-worth-1.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Devriez-vous apprendre TypeScript ? Avantages et inconvénients de TS expliqués
seo_desc: 'In this article, we''ll explore the question: is TypeScript worth learning?
  Before we try finding the answer together, let me tell you why I''m suddenly asking
  this.

  I come from a Java background where writing code demands that you be type-aware.
  This ...'
---

Dans cet article, nous explorerons la question : TypeScript vaut-il la peine d'être appris ? Avant de chercher ensemble la réponse, laissez-moi vous expliquer pourquoi je me pose soudainement cette question.

Je viens d'un milieu Java où l'écriture de code exige d'être conscient des types. Cela signifie que si vous déclarez une chaîne de caractères, vous devez écrire son type comme `String` explicitement, comme ceci :

```java
// Déclaration d'une String en Java

String greeting = "TypeScript vaut-il la peine d'être appris ?"
```

Après avoir développé des produits logiciels avec Java pendant 8 longues années, lorsque je suis passé à `JavaScript`, le développeur en moi était ravi – au point de me dire : "Oh, enfin ! J'ai enfin pris un bol d'air frais".

Je n'avais plus à me soucier des types et de les déclarer à l'avance. J'avais l'impression d'écrire moins de code, et le monde était soudainement un paradis de liberté pour moi pour construire, tester et livrer.

Quatre autres années agréables sont passées avec JavaScript et je suis devenu un développeur senior. Ensuite, j'ai eu ma première introduction formelle à `TypeScript`.

Voici donc l'occasion pour moi de vous dire ce que je pense, et si TypeScript vaut la peine d'être appris. Je vais partager l'expérience que j'ai acquise au fil des ans. Si vous êtes d'accord/pas d'accord/voulez en savoir plus, mes réseaux sociaux sont mentionnés en bas de cet article. J'adorerais échanger et discuter. Continuez votre lecture.

Si vous souhaitez également consulter la version vidéo de cet article, la voici : 😊

%[https://www.youtube.com/watch?v=whGzNBqdNS0]

## **Table des matières**

* [Qu'est-ce que TypeScript ?](#heading-quest-ce-que-typescript)
* [Commencer avec TypeScript – Les défis](#heading-commencer-avec-typescript-les-defis)
* [En savoir plus sur TypeScript – Les avantages](#heading-en-savoir-plus-sur-typescript-les-avantages)
* [Premiers pas pour commencer à coder en TypeScript](#heading-premiers-pas-pour-commencer-a-coder-en-typescript)
* [Alors, quel est le verdict : TypeScript en vaut-il la peine ou non ?](#heading-alors-quel-est-le-verdict-typescript-en-vaut-il-la-peine-ou-non)
* [Avant de conclure...](#heading-avant-de-conclure)

## Qu'est-ce que TypeScript ?

`TypeScript` est JavaScript dans son cœur avec une syntaxe supplémentaire pour les types. Traditionnellement, JavaScript est un langage à typage faible. Sa flexibilité permettant aux développeurs d'utiliser (ou de mal utiliser) des affectations de types aléatoires peut conduire à des bugs indésirables dans leurs applications.

C'est là que TypeScript devient utile en tant que langage de programmation à typage fort. Il aide à protéger les développeurs contre la rupture des applications à l'exécution en aidant avec les vérifications de types au moment de la compilation du code. Vous pouvez en savoir plus sur TypeScript et sa sécurité de type sur [le site officiel de TypeScript](https://www.typescriptlang.org/).

TypeScript aide les développeurs JavaScript à attraper les erreurs tôt dans leur éditeur de code. L'expérience de connaître les erreurs possibles pendant que vous codez peut vous aider, vous et votre équipe, à faire confiance au résultat final que le code produira.

Si vous connaissez JavaScript, vous n'avez pas besoin d'apprendre des fondamentaux de programmation supplémentaires pour coder en TypeScript. Vous devez simplement être conscient de son système de types et de la syntaxe associée pour les appliquer à votre code JavaScript.

Personnellement, TypeScript a changé la façon dont je codais et livrais mes produits. Mais ce n'était pas une partie de plaisir de se mettre dans l'état d'esprit d'utiliser TypeScript en sacrifiant toute la flexibilité que vous obtenez avec JavaScript. J'ai eu mes propres défis et façons de les surmonter.

Cet article est pour chaque développeur qui rencontre ces défis lorsqu'il commence à coder en TypeScript. Et il est destiné à vous aider avec l'état d'esprit dont vous aurez besoin pour apprécier la rigueur de TypeScript, et comment identifier les informations biaisées (et fausses) liées à TypeScript pour faire le bon choix pour vos projets.

Rappelez-vous, TypeScript n'est pas pour tout le monde ou pour toutes les occasions. Mais il sera plus facile pour vous de faire le choix si vous êtes conscient de ses qualités, de là où il s'intègre, et de là où il ne s'intègre pas. J'espère que cet article vous aidera à commencer à comprendre les avantages et les limitations de TypeScript, et que vous apprécierez le processus de sélection ou de rejet de TypeScript pour vos projets à venir.

## Commencer avec TypeScript – Les défis

Pour être honnête, commencer avec TypeScript a été un choc pour moi, et cela s'est avéré être un peu un cauchemar. Cela était principalement dû aux défis suivants :

### Configuration du projet et outils nécessaires

Ce n'était pas aussi simple que d'ouvrir l'onglet Console des outils de développement du navigateur et de commencer à écrire du code pour voir le résultat. Cela fonctionne très bien avec JavaScript, et moi – comme beaucoup d'autres débutants – avais commencé à gagner en confiance en codant en JavaScript en écrivant le code directement dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-12.png)
_Écrire du JavaScript dans l'onglet console des outils de développement du navigateur_

Avec TypeScript, cependant, le navigateur ne comprend pas sa syntaxe. Et vous pourriez vous demander... quoi faire ensuite ?

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-13.png)
_Vous ne pouvez pas exécuter le programme TypeScript de la même manière - vous obtiendrez une erreur_

Vous pourriez commencer à réaliser que vous avez besoin d'outils supplémentaires et de systèmes de construction pour imprimer un "Hello World" sur la console.

### Le compilateur TypeScript

Alors, y a-t-il aussi un compilateur ? De plus, dites-vous que le compilateur TypeScript (tsc) compile le code TypeScript pour créer un code JavaScript équivalent que nous exécuterons finalement ? C'est étrange. Alors pourquoi ne pas coder directement en JavaScript ? Cette pensée déconcerte de nombreux développeurs commençant avec TypeScript.

### Le fichier `tsconfig.json` "unique et seul"

Les projets TypeScript nécessitent des configurations explicites pour fonctionner dans un environnement que vous définissez. Vous fournissez les configurations en utilisant le fichier `tsconfig.json`. Il vous permet de configurer le chemin du fichier de sortie, la rigueur des types, comment gérer les fonctionnalités liées à TypeScript comme `any`, et comment vous voulez que TypeScript traite `null`, `undefined`, et ainsi de suite.

La bonne nouvelle est que cela fonctionne très bien une fois que vous avez configuré les choses correctement. Mais la mauvaise nouvelle est que, en tant que débutant, vous pourriez être perdu face à une erreur comme celle que vous voyez ci-dessous dans le fichier `tsconfig.json`, même lorsque vous n'avez pas touché le fichier du tout.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-14.png)
_Le cas curieux du fichier tsconfig._

### Le sentiment de vous ralentir

En tant que débutant avec TypeScript (surtout lorsque vous avez déjà passé un bon moment à travailler avec JavaScript), vous pourriez avoir l'impression d'être ralenti. Ce sentiment vient du besoin de toujours définir vos types.

C'est alors que vous commencez à penser :

* J'écris du code supplémentaire.
* Du code supplémentaire signifie des heures de travail supplémentaires.
* C'est de la puissance cérébrale et de la maintenance supplémentaires.
* Est-ce que je complique trop certaines des simples structures de JavaScript ?

![Image](https://www.freecodecamp.org/news/content/images/2024/05/clock.gif)
_Après quelques jours..._

## En savoir plus sur TypeScript – Les avantages

Si vous n'avez pas encore abandonné et que vous êtes toujours en mode exploration, votre perspective sur TypeScript pourrait commencer à changer. Voici quelques-uns des avantages du codage en TypeScript :

### Sécurité des types

TypeScript est un sur-ensemble de JavaScript. Il a tout ce que JavaScript a, plus il assure la `sécurité des types`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-15.png)
_TypeScript en tant que sur-ensemble de JavaScript_

La sécurité des types est un mécanisme pour s'assurer que vous utilisez les bons types de valeurs dans votre code. Elle aide à protéger vos applications contre la rupture de quelque chose à l'exécution (en production lorsque vos utilisateurs utilisent l'application). TypeScript assure également la sécurité des types au moment de la compilation, bien avant que vous ne poussiez des modifications de code vers d'autres développeurs ou vers vos utilisateurs.

Voici un exemple de code sécurisé par les types en TypeScript. La fonction `sumOfTwo` accepte deux paramètres de type `number` et retourne une valeur qui est également de type `number`.

```js
function sumOfTwo(a: number, b: number): number {
    return a + b;
}

```

Si l'appelant de la fonction ne respecte pas les types définis, le code ne se compilera pas et produira des erreurs de compilation.

```js
console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

console.log(sumOfTwo("tapas", 1)); // TypeError
```

Ce comportement de TypeScript protège votre code pour qu'il ne tombe pas en panne en production à cause d'erreurs liées aux types.

### Courbe d'apprentissage plus facile

La sécurité des types est bien. Et la courbe d'apprentissage ? Si vous connaissez déjà JavaScript, votre courbe d'apprentissage pour TypeScript sera plus petite.

Si vous ne connaissez pas JavaScript, vous pouvez envisager de commencer directement avec TypeScript, car apprendre JavaScript est tout aussi difficile.

### Le problème des outils

Heureusement, il existe des moyens de gérer le problème initial des outils et du système de construction dont nous avons parlé précédemment. Les développeurs du monde entier utilisent TypeScript depuis un certain temps maintenant et il existe des ressources pour obtenir l'aide dont vous avez besoin et tout configurer.

Si vous avez des connaissances préalables de Node et de l'écosystème JavaScript, cela peut prendre une demi-journée pour tout configurer. Si vous n'avez ni Node ni JavaScript, cela peut prendre au maximum quelques jours.

J'ai traversé une phase similaire, et maintenant j'ai mon propre environnement à utiliser pour tous mes projets TypeScript. Vous pouvez [le consulter sur mon GitHub](https://github.com/tapascript/ts-gyan) et n'hésitez pas à commencer à l'utiliser. Si vous voulez créer quelque chose de similaire et le personnaliser pour créer le vôtre, [ce guide](https://www.youtube.com/watch?v=P3unJiZxfkI) vous aidera avec cela.

De plus, le meilleur aspect est que toute cette configuration est un travail ponctuel. Vous le faites une fois, et vous pouvez le répliquer ou le réutiliser pour tous vos projets futurs.

Vous comprendrez également la puissance de l'IntelliSense de VS Code lors du codage en TypeScript. Il vous propose une complétion de code pour rendre votre expérience de codage encore meilleure.

### Et le truc tsconfig ?

Sans aucun doute, vous aurez besoin de temps pour apprendre les propriétés de configuration dans le fichier `tsconfig.json` et ce qu'elles font. Mais le côté positif est que vous n'avez pas besoin de toutes les connaître.

Lorsque vous commencez, assurez-vous simplement de savoir ce qui est minimalement nécessaire pour votre projet et apprenez ces choses. Soyez assuré que vous pouvez apprendre les autres choses au fur et à mesure que vous en avez besoin.

## Premiers pas pour commencer à coder en TypeScript

Après la lutte initiale avec les outils, la construction et la configuration, vous pourriez avoir hâte d'écrire votre première ligne de code TypeScript (en supposant que vous n'avez pas encore commencé à blâmer TypeScript pour votre manque de productivité !).

Regardons quelques comparaisons basées sur des scénarios entre le monde flexible de JavaScript et le monde strict de TypeScript.

### Exemples JavaScript vs TypeScript

Une simple somme de deux nombres en JavaScript ressemblerait à ceci :

```jsx
function sumOfTwo(a, b) {
  return a + b;
}

console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

```

Mais faire la même chose avec TypeScript nécessiterait un peu de code supplémentaire pour indiquer au compilateur TypeScript le type des paramètres et le type de retour :

```tsx
function sumOfTwo(a: number, b: number): number {
  return a + b;
}

console.log(sumOfTwo(1,2)); // 3
console.log(sumOfTwo(1,-1)); // 0

```

Hmm ! Cela semble être plus de travail que nécessaire. Mais c'est vraiment plus utile que vous ne pouvez l'imaginer. Cela protège votre code contre la prise en compte d'entrées inacceptables au lieu de ce que le JavaScript plus "flexible" permettrait :

```jsx
function sumOfTwo(a, b) {
  return a + b;
}

console.log(sumOfTwo(1, true)); // La sortie est 2
console.log(sumOfTwo(1, [])); // Croyez-le ou non, cela donnera 1

```

Essayer le code ci-dessus en TypeScript entraînerait des erreurs de compilation. Si vous exécutez le compilateur TypeScript en mode surveillance (avec la commande `tsc -w`), vous pouvez attraper ces erreurs pendant l'écriture du code lui-même !

```tsx
function sumOfTwo(a: number, b: number): number {
  return a + b;
}

console.log(sumOfTwo(1, true)); // Erreur
console.log(sumOfTwo(1, [])); // Erreur

```

Ce n'est pas tout. Prenons un autre exemple. Considérons un tableau d'employés avec les détails de quelques employés dans votre code JavaScript :

```jsx
// Objet Employé

const employees = [
    {
        id: '01',
        name: 'Alex',
        age: 23,
        married: false
    },
    {
        id: '02',
        name: 'Bob',
        age: 3,
        married: false
    },
    {
        id: '03',
        name: 'Clara',
        age: 28,
        married: true
    }
];

```

Maintenant, disons que vous voulez filtrer les employés mariés.

```js
// Filtrer les employés mariés

employees.filter(emp => emp.married) // Clara
```

Cela fonctionne très bien ! Mais imaginez si certaines des données des employés sont incorrectes quelque part. Que se passe-t-il si vous obtenez l'objet employé comme réponse d'API où la valeur de la propriété `married` de l'employé `Bob` est définie sur `3` par erreur !

```jsx
const employees = [
    {
        id: '01',
        name: 'Alex',
        age: 23,
        married: false
    },
    {
        id: '02',
        name: 'Bob',
        age: 3,
        married: 3
    },
    {
        id: '03',
        name: 'Clara',
        age: 28,
        married: true
    }
];
```

Maintenant, votre même logique de filtrage des employés mariés donnerait comme résultat que Bob et Clara sont les employés mariés – mais Bob n'est peut-être pas marié du tout.

```js
// Filtrer les employés mariés

employees.filter(emp => emp.married) // Bob et Clara

```

Attendez ! Vous pouvez toujours protéger la situation ci-dessus avec quelques lignes de logique supplémentaire dans votre code JavaScript. Que diriez-vous de vérifier le type de la valeur de la propriété `married` de chaque employé dans le tableau et de lancer une erreur si ce n'est pas un `boolean` ?

```jsx
employees.filter((employee) => {
  if (typeof employee.married  === 'boolean') {
      return employee.married && employee;
  } else {
      throw new Error("Le type de employee.married n'est pas de type boolean.")
  }
});

```

Cela résout le problème. Mais attendez, n'est-ce pas :

* Des lignes de code supplémentaires que vous avez écrites pour protéger votre code contre les échecs ?
* Des heures de travail supplémentaires ?
* De la puissance cérébrale et de la maintenance supplémentaires ? Et si des erreurs de valeur similaires se produisent dans d'autres propriétés de l'objet employé ? Continueriez-vous à ajouter des conditions dans le callback du filtre ?
* Compliquer certaines des simples structures de JavaScript ?

Une situation meilleure et plus sûre est d'utiliser TypeScript et de typer chaque propriété de l'objet employé soit en définissant un [type ou en utilisant des interfaces](https://youtu.be/VE5SOoP2Y74?list=PLIJrr73KDmRy_ufvq5m_4KwnxUdx9Sq3d).

```ts
type Employee = {
	id: string,
    name: string,
    age: number,
    married: boolean
}
```

## Alors, quel est le verdict : TypeScript en vaut-il la peine ou non ?

Si vous arrivez à cette section après avoir lu les sections précédentes de cet article, alors les points suivants auront du sens pour vous :

* Vous n'aimerez peut-être pas TypeScript simplement en le regardant, en voyant ce qu'il promet et le code écrit avec lui. Vous devez passer du temps avec TypeScript en écrivant du code et en construisant des projets avec lui.
* La complexité des outils, des constructions et des configurations ne devrait pas se dresser sur votre chemin. Il existe de nombreuses ressources pour vous aider à comprendre ces choses. Comme nous l'avons discuté précédemment, ce sont des problèmes résolus, et vous n'avez pas besoin de réinventer la roue.
* Pour les développeurs JavaScript, il peut être difficile d'accepter TypeScript sans une compréhension plus approfondie de JavaScript lui-même. Mais plus vous en apprenez à son sujet, plus je pense que vous verrez que TypeScript a effectivement un avantage qui vous aidera, vous et votre équipe, à vous protéger contre les problèmes de types.

Maintenant, la question est – en vaut-il la peine ?

Absolument oui ! Surtout si :

* Votre projet va au-delà d'une simple application comme une application TODO.
* Vous voulez attraper les erreurs de type et les erreurs au moment de la compilation pendant l'écriture de votre code au lieu de le faire en production.
* Le projet est développé par une équipe de développeurs JavaScript.
* Vous voulez déboguer votre code efficacement.
* Vous cherchez une interface de contrat de données commune entre le client et le serveur pour l'échange de données.
* Enfin, mais non des moindres, si vous ne voulez pas manquer les opportunités d'emploi qui viennent avec la connaissance de TypeScript. Si vous connaissez les bases de JavaScript, commencer avec TypeScript ne sera pas difficile si vous obtenez un bon encadrement.

## Avant de conclure...

Je veux terminer cet article avec une citation :

> "L'apprentissage est une expérience. Le reste n'est que de l'information." – Albert Einstein.

Donc, c'est à vous de décider si quelque chose vaut la peine d'être appris.

Cela devrait dépendre du pourquoi, plutôt que du quoi, vous voulez apprendre. Vous aurez des limitations quant au nombre de choses que vous pouvez apprendre dans votre vie... alors apprenez judicieusement.

C'est aussi pourquoi j'ai commencé ma playlist TypeScript de manière pratique pour m'assurer que vous ne venez pas avec certaines hypothèses. Je veux que vous appreniez d'abord TypeScript afin que vous puissiez être un décideur confiant lorsque des choix technologiques se présentent.

[Voici le lien vers ma playlist TypeScript](https://www.youtube.com/watch?v=whGzNBqdNS0&list=PLIJrr73KDmRy_ufvq5m_4KwnxUdx9Sq3d) si vous voulez la consulter. La playlist décomposera chacune des configurations, concepts et constructions de projets de manière adaptée aux débutants pour vous aider à apprendre TypeScript rapidement.

C'est tout pour l'instant. J'espère que vous avez trouvé cet article informatif et perspicace. Je suis éducateur sur ma chaîne YouTube, `tapaScript`. Veuillez [vous ABONNER](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à la chaîne si vous voulez apprendre JavaScript, TypeScript, ReactJS, Next.js, Node.js, Git, et tout sur le développement web de manière fondamentale.

Restez en contact.

* [Suivez-moi sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils de carrière.
* Retrouvez toutes mes conférences publiques [ici](https://www.tapasadhikary.com/talks).
* Consultez et suivez mon travail Open Source sur [GitHub](https://github.com/atapas).
* Je publie régulièrement des articles significatifs sur mon [blog GreenRoots](https://blog.greenroots.info/), vous pourriez les trouver utiles également.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.