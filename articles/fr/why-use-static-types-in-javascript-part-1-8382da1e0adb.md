---
title: Pourquoi utiliser des types statiques en JavaScript ? (Une introduction en
  4 parties sur la typage statique avec Flow)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-08T17:46:02.000Z'
originalURL: https://freecodecamp.org/news/why-use-static-types-in-javascript-part-1-8382da1e0adb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YJbUzd6InXYN8EGTIGEFOA.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: flowtype
  slug: flowtype
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Pourquoi utiliser des types statiques en JavaScript ? (Une introduction
  en 4 parties sur la typage statique avec Flow)
seo_desc: 'By Preethi Kasireddy

  As a JavaScript developer, you can code all day long without encountering any static
  types. So why bother learning about them?

  Well it turns out learning types isn’t just an exercise in mind-expansion. If you’re
  willing to invest...'
---

Par Preethi Kasireddy

En tant que développeur JavaScript, vous pouvez coder toute la journée sans rencontrer de types statiques. Alors pourquoi se donner la peine de les apprendre ?

Eh bien, il s'avère que l'apprentissage des types n'est pas seulement un exercice d'expansion de l'esprit. Si vous êtes prêt à investir du temps pour apprendre les avantages, les inconvénients et les cas d'utilisation des types statiques, cela pourrait grandement aider votre programmation.

Intéressé ? Eh bien, vous avez de la chance — c'est ce dont traite le reste de cette série en quatre parties.

### D'abord, une définition

Le moyen le plus rapide de comprendre les types statiques est de les contraster avec les types dynamiques. Une langue avec des types statiques est appelée une **langue à typage statique**. D'autre part, une langue avec des types dynamiques est appelée une **langue à typage dynamique**.

La différence fondamentale est que les langues **à typage statique** effectuent la vérification des types au **moment de la compilation**, tandis que les langues **à typage dynamique** effectuent la vérification des types à **l'exécution**.

Cela laisse un autre concept à aborder : que signifie le terme **« vérification de type »** ?

Pour expliquer, examinons les types en Java par rapport à JavaScript.

Les **« types »** font référence au type de données défini.

Par exemple, en Java, si vous définissez un `boolean` comme suit :

```
boolean result = true;
```

Cela a un type correct, car l'annotation `boolean` correspond à la valeur donnée à `result`, contrairement à un entier ou autre chose.

D'autre part, si vous essayiez de déclarer :

```
boolean result = 123;
```

... cela échouerait à compiler car il a un type incorrect. Il marque explicitement `result` comme un `boolean`, mais le définit ensuite comme l'entier `123`.

JavaScript et d'autres langues à typage dynamique ont une approche différente, permettant au contexte d'établir quel type de données est défini :

```
var result = true;
```

En bref : les langues à typage statique vous obligent à déclarer les types de données de vos constructions avant de pouvoir les utiliser. Les langues à typage dynamique ne le font pas. JavaScript implique le type de données, tandis que Java le déclare explicitement.

Ainsi, comme vous pouvez le voir, les types vous permettent de spécifier des **invariants** de programme, ou les assertions logiques et les conditions dans lesquelles le programme s'exécutera.

La **vérification de type** vérifie et impose que le type d'une construction (constante, booléen, nombre, variable, tableau, objet) correspond à un invariant que vous avez spécifié. Vous pourriez, par exemple, spécifier que « cette fonction retourne toujours une chaîne de caractères ». Lorsque le programme s'exécute, vous pouvez supposer en toute sécurité qu'il retournera une chaîne de caractères.

Les différences entre la vérification de type statique et la vérification de type dynamique comptent le plus lorsqu'une erreur de type se produit. Dans une langue à typage statique, les erreurs de type se produisent pendant l'étape de compilation, c'est-à-dire au moment de la compilation. Dans les langues à typage dynamique, les erreurs ne se produisent que lorsque le programme est exécuté. C'est-à-dire, à **l'exécution**.

Cela signifie qu'un programme écrit dans une langue à typage dynamique (comme JavaScript ou Python) peut compiler même s'il contient des erreurs de type qui empêcheraient autrement le script de s'exécuter correctement.

D'autre part, si un programme écrit dans une langue à typage statique (comme Scala ou C++) contient des erreurs de type, il échouera à compiler jusqu'à ce que les erreurs aient été corrigées.

### Une nouvelle ère de JavaScript

Parce que JavaScript est une langue à typage dynamique, vous pouvez déclarer des variables, des fonctions, des objets et autre chose sans déclarer le type.

Pratique, mais pas toujours idéal. C'est pourquoi des outils comme [Flow](https://flowtype.org) et [TypeScript](https://www.typescriptlang.org/) sont récemment intervenus pour donner aux développeurs JavaScript l'*option* d'utiliser des types statiques.

[**Flow**](https://flowtype.org/) est une bibliothèque open-source de vérification de types statiques développée et publiée par Facebook qui vous permet d'ajouter progressivement des types à votre code JavaScript.

[**TypeScript**](https://www.typescriptlang.org/), en revanche, est un sur-ensemble qui se compile en JavaScript — bien qu'il ressemble presque à une nouvelle langue à typage statique à part entière. Cela dit, il ressemble et se comporte très similaire à JavaScript et n'est pas difficile à apprendre.

Dans les deux cas, lorsque vous souhaitez utiliser des types, vous indiquez explicitement à l'outil quels fichiers vérifier. Pour TypeScript, vous le faites en écrivant des fichiers avec l'extension `.ts` au lieu de `.js`. Pour Flow, vous incluez un commentaire en haut du fichier avec `@flow`.

Une fois que vous avez déclaré que vous souhaitez vérifier les types d'un fichier, vous pouvez utiliser leur syntaxe respective pour définir les types. Une distinction à faire entre les deux outils est que Flow est un vérificateur de types et non un compilateur. TypeScript, en revanche, est un compilateur.

Je crois vraiment que des outils comme Flow et TypeScript représentent un *changement et une avancée générationnels* pour JavaScript.

Personnellement, j'ai appris tellement en utilisant des types au quotidien. C'est pourquoi j'espère que vous me rejoindrez dans ce court et doux voyage dans les types statiques.

Le reste de cet article en 4 parties couvrira :

Partie I. [Une rapide introduction à la syntaxe et au langage Flow](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-1-8382da1e0adb#.prtc7vhrr)

Parties II & III. [Avantages & Inconvénients des types statiques (avec des exemples détaillés)](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-2-part-3-be699ee7be60#.9ywoivqaz)

Partie IV. [Devez-vous utiliser des types statiques en JavaScript ou non ?](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-4-b2e1e06a67c9#.cb2z6mty8)

Notez que j'ai choisi Flow plutôt que TypeScript dans les exemples de cet article en raison de ma familiarité avec lui. Pour vos propres besoins, veuillez faire des recherches et choisir l'outil qui vous convient. TypeScript est également fantastique.

Sans plus attendre, commençons !

### Partie 1 : Une rapide introduction à la syntaxe et au langage Flow

Pour comprendre les avantages et les inconvénients des types statiques, vous devez d'abord avoir une compréhension de base de la syntaxe des types statiques en utilisant Flow. Si vous n'avez jamais travaillé dans une langue à typage statique auparavant, la syntaxe peut prendre un peu de temps pour s'y habituer.

Commençons par explorer comment ajouter des types aux primitives JavaScript, ainsi qu'aux constructions comme les tableaux, les objets, les fonctions, etc.

#### boolean

Cela décrit une valeur `boolean` (vrai ou faux) en JavaScript.

Remarquez que lorsque vous souhaitez spécifier un type, la syntaxe que vous utilisez est :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z79CcJO6h4DO_xKJMdK9zg.png)

#### number

Cela décrit un nombre à virgule flottante IEEE 754. Contrairement à de nombreux autres langages de programmation, JavaScript ne définit pas différents types de nombres (comme les entiers, short, long et les nombres à virgule flottante). Au lieu de cela, les nombres sont toujours stockés sous forme de nombres à virgule flottante en double précision. Par conséquent, vous n'avez besoin que d'un seul type de nombre pour définir n'importe quel nombre.

`number` inclut `Infinity` et `NaN`.

#### string

Cela décrit une chaîne de caractères.

#### null

Cela décrit le type de données `null` en JavaScript.

#### void

Cela décrit le type de données `undefined` en JavaScript.

Notez que `null` et `undefined` sont traités différemment. Si vous essayiez de faire :

Flow lancerait une erreur car le type `void` est censé être de type `undefined`, ce qui n'est pas la même chose que le type `null`.

#### Array

Décrit un tableau JavaScript. Vous utilisez la syntaxe `Array<T>` pour décrire un tableau dont les éléments sont d'un certain type T.

Remarquez comment j'ai remplacé `T` par `string`, ce qui signifie que je déclare `messages` comme un tableau de chaînes de caractères.

#### Object

Cela décrit un objet JavaScript. Il existe plusieurs façons différentes d'ajouter des types aux objets.

Vous pourriez ajouter des types pour décrire la forme d'un objet :

Vous pourriez définir des objets comme des cartes où vous mappez une chaîne de caractères à une certaine valeur :

Vous pourriez également définir un objet comme un type `Object` :

Cette dernière approche nous permet de définir n'importe quelle clé et valeur sur votre objet sans restriction, donc elle n'ajoute pas vraiment beaucoup de valeur en ce qui concerne la vérification de type.

#### any

Cela peut représenter littéralement n'importe quel type. Le type `any` est effectivement non vérifié, donc vous devriez essayer de l'éviter sauf si absolument nécessaire (comme lorsque vous devez vous désengager de la vérification de type ou avez besoin d'une issue de secours).

Une situation où vous pourriez trouver `any` utile est lorsque vous utilisez une bibliothèque externe qui étend les prototypes d'un autre système (comme Object.prototype).

Par exemple, si vous utilisez une bibliothèque qui étend Object.prototype avec une propriété `doSomething` :

Vous pourriez obtenir une erreur :

Pour contourner cela, vous pouvez utiliser `any` :

#### Functions

La manière la plus courante d'ajouter des types aux fonctions est d'ajouter des types à leurs arguments d'entrée et (lorsque pertinent) à la valeur de retour :

Vous pouvez même ajouter des types aux fonctions asynchrones (voir ci-dessous) et aux générateurs :

Remarquez comment notre deuxième paramètre `getPurchaseLimit` est annoté comme une fonction qui retourne une `Promise`. Et `amountExceedsPurchaseLimit` est annoté comme retournant également une `Promise`.

#### Type alias

L'aliasing de type est l'une de mes façons préférées d'utiliser les types statiques. Ils vous permettent d'utiliser des types existants (nombre, chaîne, etc.) pour composer de nouveaux types :

Ci-dessus, j'ai créé un nouveau type appelé `PaymentMethod` qui a des propriétés composées de types `number` et `string`.

Maintenant, si vous souhaitez utiliser le type `PaymentMethod`, vous pouvez faire :

Vous pouvez également créer des alias de type pour n'importe quelle primitive en enveloppant le type sous-jacent dans un autre type. Par exemple, si vous souhaitez créer un alias de type pour `Name` et `EmailAddress` :

En faisant cela, vous indiquez que `Name` et `Email` sont des choses distinctes, pas seulement des chaînes de caractères. Puisqu'un nom et un email ne sont pas vraiment interchangeables, faire cela vous empêche de les mélanger accidentellement.

#### Generics

Les génériques sont un moyen d'abstraire les types eux-mêmes. Que signifie cela ?

Prenons un exemple :

J'ai créé une abstraction pour le type `T`. Maintenant, vous pouvez utiliser n'importe quel type pour représenter `T`. Pour `numberT`, `T` était de type `number`. Pendant ce temps, pour `arrayT`, T était de type `Array<number>`.

Oui, je sais. C'est vertigineux si c'est la première fois que vous regardez les types. Je promets que l'introduction « douce » est presque terminée !

#### Maybe

Le type Maybe nous permet d'annoter un type pour une valeur potentiellement `null` ou `undefined`. Ils ont le type `T|void|null` pour un certain type `T`, ce qui signifie qu'il est soit de type `T`, soit `undefined`, soit `null`. Pour définir un type `maybe`, vous placez un point d'interrogation devant la définition de type :

Ici, je dis que message est soit une `string`, soit `null`, soit `undefined`.

Vous pouvez également utiliser maybe pour indiquer qu'une propriété d'objet sera soit d'un certain type `T`, soit `undefined` :

En plaçant le `?` à côté du nom de la propriété pour `middleInitial`, vous pouvez indiquer que ce champ est facultatif.

#### Disjoint unions

C'est une autre manière puissante de modéliser des données. Les unions disjointes sont utiles lorsque vous avez un programme qui doit traiter différents types de données en même temps. En d'autres termes, la forme des données peut être différente en fonction de la situation.

En étendant le type `PaymentMethod` de notre exemple précédent sur les génériques, disons que vous avez une application où les utilisateurs peuvent avoir l'un des trois types de méthodes de paiement. Dans ce cas, vous pouvez faire quelque chose comme :

Ensuite, vous pouvez définir votre type PaymentMethod comme une union disjointe avec trois cas.

La méthode de paiement ne peut maintenant être que l'une de ces trois formes. La propriété `type` est la propriété qui rend le type d'union « disjoint ».

Vous verrez plus d'exemples pratiques de types d'union disjointe plus tard dans la partie II.

D'accord, presque terminé. Il y a quelques autres fonctionnalités de Flow qui méritent d'être mentionnées avant de conclure cette introduction :

**1) Inférence de type** : Flow utilise l'inférence de type lorsque cela est possible. L'inférence de type intervient lorsque le vérificateur de type peut déduire automatiquement le type de données d'une expression. Cela aide à éviter les annotations excessives.

Par exemple, vous pouvez écrire :

Même si cette Classe n'a pas de types, Flow peut la vérifier correctement :

Ici, j'ai essayé de définir `area` comme une `string`, mais dans la définition de la classe `Rectangle`, nous avons défini `width` et `height` comme des nombres. Donc, en fonction de la définition de la fonction pour `area`, elle doit retourner un `number`. Même si je n'ai pas explicitement défini de types pour la fonction `area`, Flow a détecté l'erreur.

Une chose à noter est que les mainteneurs de Flow recommandent que si vous exportiez cette définition de classe, vous souhaiteriez ajouter des définitions de type explicites pour faciliter la recherche de la cause des erreurs lorsque la classe n'est pas utilisée dans un contexte local.

**2) Tests de type dynamique** : Cela signifie essentiellement que Flow a une logique pour déterminer quel sera le type d'une valeur à l'exécution et peut donc utiliser cette connaissance lors de l'analyse statique. Ils deviennent utiles dans des situations où Flow lance une erreur mais vous devez convaincre Flow que ce que vous faites est correct.

Je n'entrerai pas dans trop de détails car c'est une fonctionnalité plus avancée que j'espère aborder séparément, mais si vous souhaitez en savoir plus, il vaut la peine de lire la [documentation](https://flowtype.org/docs/dynamic-type-tests.html).

### Nous avons terminé avec la syntaxe

Nous avons couvert beaucoup de terrain en une seule section ! J'espère que cet aperçu de haut niveau a été utile et gérable. Si vous êtes curieux d'aller plus loin, je vous encourage à plonger dans la [documentation bien écrite](https://flowtype.org/docs/) et à explorer.

Maintenant que la syntaxe est derrière nous, passons enfin à la partie amusante : [explorer les avantages et les inconvénients de l'utilisation des types](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-2-part-3-be699ee7be60#.9ywoivqaz) !

Prochaine étape : [Partie 2 & 3](https://medium.com/@preethikasireddy/why-use-static-types-in-javascript-part-2-part-3-be699ee7be60#.9ywoivqaz).