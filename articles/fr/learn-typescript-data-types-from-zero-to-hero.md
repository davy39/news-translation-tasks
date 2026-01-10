---
title: Apprendre les types de données TypeScript – De zéro à héros
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-25T09:58:40.000Z'
originalURL: https://freecodecamp.org/news/learn-typescript-data-types-from-zero-to-hero
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/road-trip-with-raj-o4c2zoVhjSw-unsplash-1.jpg
tags:
- name: Angular
  slug: angular
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Apprendre les types de données TypeScript – De zéro à héros
seo_desc: 'By Jonathan Sexton

  It''s all the rage these days in the world of web development - TypeScript.  I''d
  wager by now you have heard about it, even in passing.  But, if you haven''t or
  if you''re just curious then you''ve come to the right place my friend!

  I''...'
---

Par Jonathan Sexton

C'est la tendance ces jours-ci dans le monde du développement web - [TypeScript](https://www.typescriptlang.org/). Je parierais que vous en avez déjà entendu parler, même en passant. Mais, si ce n'est pas le cas ou si vous êtes simplement curieux, alors vous êtes au bon endroit mon ami !

J'apprends actuellement TypeScript en conjonction avec Angular (un article à ce sujet est en préparation, alors restez à l'écoute !) parce que c'est ce avec quoi notre application web est construite au travail. J'ai décidé d'écrire quelque chose de simple et facile à suivre pour que vous puissiez vous lancer avec les types de données TypeScript.

Je vais diviser cet article en deux parties pour simplifier - la première sera un bref aperçu de ce qu'est TypeScript, des types de données et quelques exemples. Le second article se concentrera sur l'installation et l'exécution de TypeScript localement sur votre machine.

## Qu'est-ce que c'est ?

Avant de commencer, voici une description super condensée de TypeScript en mes propres mots. C'est un **_superset_** de JavaScript - ce qui signifie essentiellement qu'il s'agit d'une forme de JavaScript qui vous offre certains avantages en plus de toute la puissance incluse dans le JavaScript 'vanilla'. C'est un langage open source écrit et maintenu par Microsoft.

TypeScript est transpilé en JavaScript et s'exécutera dans tout environnement où le JavaScript natif s'exécute. Vous pouvez utiliser TypeScript pour les applications front-end et back-end.

Il est écrit exactement comme JavaScript, avec quelques exceptions que nous allons voir bientôt. Voici un exemple de TypeScript :

![code montrant typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image.png)
_TypeScript dans toute sa gloire_

Essayez de ne pas vous concentrer sur tous les deux-points et autres éléments que vous voyez ci-dessus, nous allons creuser cela ci-dessous. Au lieu de cela, concentrez-vous sur les éléments qui se démarquent - nous déclarons simplement des variables avec des valeurs, ce sont des chaînes de caractères, des tableaux et des objets, tout comme en JavaScript.

Une autre grande chose que j'ai apprise sur TypeScript est que vous pouvez mélanger du JavaScript avec le code et n'aurez aucun problème à le faire. Voir la capture d'écran ci-dessous (ci-dessous dans une application Angular) :

![code typescript et javascript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-1.png)
_TypeScript et JavaScript utilisés ensemble dans le même fichier_

## Types de données

Commençons avec le plus intéressant - les types de données ! (Il y a quelques types de données que nous n'aborderons pas - never, null, undefined. Cela est simplement parce qu'il n'y a pas grand-chose à dire à leur sujet. Je veux que vous sachiez qu'ils existent et si vous souhaitez approfondir ces types, voici un lien vers la documentation officielle de [TypeScript](https://www.typescriptlang.org/docs/handbook/basic-types.html) pour référence.)

TypeScript déduira le type de données assigné à une variable sans que vous ayez à définir explicitement le type, mais pour simplifier et par précaution, j'aime déclarer le type de données lors de la déclaration de mes variables.

Nous assignons les types de données en plaçant simplement un deux-points après le nom de la variable mais avant le signe égal :

_**const {nom de la variable}: {type de variable} = {valeur de la variable**_}

C'est la convention avec laquelle la majorité des types de données TypeScript sont déclarés, à l'exception des fonctions et des objets.

Certains types de données viennent avec un peu plus de complexité, mais vous avez l'idée générale. Ci-dessous se trouvent quelques brèves explications des types de données et des exemples de leur déclaration.

#### Booléen

Les booléens en TypeScript fonctionnent de la même manière qu'en JavaScript. Les variables de type de données booléen sont déclarées comme suit :

`const myBool: boolean = false`;

#### Chaîne de caractères

Les chaînes de caractères en TypeScript fonctionnent de la même manière qu'en JavaScript. Les variables de type de données chaîne de caractères sont déclarées comme suit :

_`let myString: string = 'bacon'`_

#### Nombre

Les nombres en TypeScript fonctionnent de la même manière qu'en JavaScript. Les variables de type de données nombre sont déclarées comme suit :

`const myNum: number = 1207;`

#### **Tableau**

Les tableaux en TypeScript sont, comme les autres types de données, identiques aux tableaux en JavaScript. Les variables de type de données tableau sont déclarées de deux manières distinctes :

`const myArr: number[] = [12, 90, 71];`

La manière ci-dessus est celle avec laquelle vous déclareriez un tableau si tous les éléments à l'intérieur de ce tableau sont des nombres.

`const myArr: Array<number> = [12, 90, 71];`

Cette manière de déclarer un tableau utilise le type de tableau générique défini sur nombre. Fonctionnellement, il n'y a aucune différence dans la manière dont ces méthodes produisent le résultat final de la déclaration d'une variable avec un type de tableau.

Si les types de données à l'intérieur du tableau sont inconnus ou un mélange de types de données, le tableau peut être déclaré en utilisant le type _<any>_ (c'est un type à part entière qui est discuté ci-dessous) :

`const myArr: Array<any> = [12, 'thirteen', false];`

Cette manière vous permettra de mélanger les types de données dans le tableau.

#### **Tuples**

Les tuples sont un type de données unique à TypeScript. Pensez à eux comme des tableaux avec un nombre fixe d'éléments. Ce type de données est mieux utilisé lorsque vous savez exactement combien de variables vous devriez avoir. Il est possible de réassigner la valeur des indices mais pas la quantité d'éléments dans le tuple.

Les variables de type de données tuple sont déclarées exactement comme un tableau :

`let mine: [number, string];`

Si nous voulons changer les _valeurs_ des éléments, nous pouvons le faire tant qu'elles correspondent aux types que nous avons fournis lors de la déclaration de notre variable :

`mine[0] = 14`  ✅

`mine[0] = 'Steve'`  ❌

Puisque nous avons défini `mine` comme un tuple, l'ordre des valeurs compte également et ne peut pas être changé. De plus, assigner un index en dehors du nombre défini initialement produira une erreur :

`mine[0] = ['Dave', 71]`  ❌

`mine = [121, 'Dave', 'Steve'];`  ❌

`mine = [121, 'bacon'];`  ✅

#### **Fonction**

Les fonctions peuvent être aussi explicites que vous le souhaitez. Ce que je veux dire par là, c'est que nous pouvons appliquer des types aux paramètres et aux valeurs retournées. Voici deux exemples :

![une fonction qui retourne le nombre 91](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-2.png)
_Nous définissons explicitement le type de valeur que nous attendons de cette fonction pour qu'elle retourne_

Cette fonction générera une _erreur_ si une valeur autre qu'un nombre est retournée. Elle peut retourner une variable _**uniquement si**_ cette variable pointe vers un nombre.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-81.png)
_Nous pouvons également définir les types de paramètres que nous attendons_

Ci-dessus, nous vérifions les types des paramètres passés à notre fonction. C'est un excellent moyen d'éviter les erreurs car si le nombre de paramètres est incorrect ou si leur type de données ne correspond pas à ce que nous attendons, TypeScript nous le signalera avec une erreur.

Si je veux une fonction qui ne doit pas retourner de valeur, je peux définir le type comme _void_ (un type de données qui signifie l'absence de toute donnée. Bien qu'il puisse être utilisé lors de la déclaration de variables, il ne l'est généralement pas car alors nous devrions définir la variable sur _null_ ou _undefined_, je ne l'ai utilisé que lorsque les fonctions ne doivent pas avoir de valeur de retour) et si la fonction retourne quelque chose, TypeScript générera une erreur :

![une fonction typescript avec le type défini sur void](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-3.png)
_Une fonction avec le type défini sur void_

En définissant le type sur _void_, je suis explicite sur mes retours et j'établis que bien que cette fonction puisse encore s'exécuter, elle ne doit pas _retourner_ une valeur. Si elle retourne une valeur, j'aurai une erreur.

#### **Enum**

Les enums sont une addition bienvenue (à mon humble avis) aux types de données. Pensez à eux comme une approche plus conviviale pour donner des noms aux valeurs numériques. Voici un exemple d'enum :

`enum Foods {'bacon', 'tomato', 'lettuce'};`

console.log(Foods[0]) // donne 'bacon' console.log(Foods.bacon) // donne 0  console.log(Foods['lettuce']) // donne 2

Il est également possible d'assigner le format d'index numérique avec les enums. De nombreux langages, y compris C#, ont des enums et je suis heureux de les voir arriver en JavaScript.

Vous pouvez être aussi créatif que vous le souhaitez avec les noms. Vous pouvez même changer la représentation numérique des indices. Si vous voulez que votre premier index commence à 18 au lieu de 0, c'est aussi simple que :

`enum Foods {'bacon'= 18, 'tomato', 'lettuce'};`

`console.log(Foods['bacon']); // 18`

Disons que nous avions la valeur 18 mais que nous n'étions pas sûrs de ce à quoi elle correspondait dans notre enum `Foods`, nous pouvons vérifier cela également :

`console.log(Foods[18]); // 'bacon'`

Un point d'information notable est que maintenant que nous avons défini le premier index pour commencer à 18, le prochain index sera 19, et ainsi de suite en suivant la convention de numérotation que vous établissez.

**Objet**

Les objets en TypeScript sont définis de manière similaire aux objets en JavaScript. Nous pouvons être aussi implicites ou explicites avec notre définition que nous le souhaitons ou que la situation le dicte :

`let data: = {name: 'Jonathan', age: 30, hobbies: ['running','swimming','coding']};`  ✅

`let data: {name: string, age: number, hobbies: string[]} = {name: 'Jonathan', age: 30, hobbies: ['running','swimming','coding']};`  ✅

Lors de la création d'objets, les noms des propriétés sont immuables, mais l'ordre dans lequel ils apparaissent n'a pas d'importance, même si nous les définissons dans un ordre spécifique.

De plus, nous pouvons avoir des objets simples comme ceux ci-dessus, ou nous pouvons définir des objets complexes qui tirent parti de plusieurs types de données comme celui ci-dessous (cet objet est à des fins de démonstration uniquement) :

![un type de données d'objet complexe en TypeScript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-4.png)
_Ici, nous définissons explicitement les types de données lorsque cela est possible dans cet objet complexe_

#### Alias de type/Interface

Avec l'exemple d'un objet complexe ci-dessus, vous pourriez penser que c'est génial, mais que se passe-t-il la prochaine fois que j'ai besoin de créer un objet complexe ? Dois-je tout retaper manuellement ?

Ne craignez rien, les alias de type et les interfaces sont là pour aider ! Un alias de type est un type de données qui nous permet d'enregistrer d'autres types de données à l'intérieur et ensuite de référencer une variable au lieu de réécrire du code encore et encore.

En tant que note à part, les alias de type et les interfaces fonctionnent de manière très similaire. Les deux nous permettent de créer un échafaudage pour un objet/plan de la manière dont nos données doivent être structurées. Cependant, il existe des **_différences subtiles_** que nous n'aborderons pas ici. Au lieu de cela, voici un [article qui explique ces différences](https://medium.com/@martin_hotell/interface-vs-type-alias-in-typescript-2-7-2a8f1777af4c) de manière extrêmement efficace si vous souhaitez approfondir.

Il existe des détails entre les deux dont nous devons être conscients - lors de l'utilisation de l'alias de type, nous utilisons un signe égal (=) pour déclarer les valeurs, l'interface ne nécessite pas de signe égal.

![le type de données interface en typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-6.png)
_Le type interface fonctionne de manière très similaire à l'alias de type mais ne nécessite pas de signe égal (=)._

![un type de données alias en typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-5.png)
_Les types de données alias nécessitent un signe égal (=)._

Maintenant que nous avons déclaré notre alias, il est temps de l'utiliser. Lorsque nous voulons "construire" notre nouvelle variable à partir de cet alias, nous la définissons simplement comme type de données :

![un objet typescript](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-7.png)
_L'échafaudage d'objets en utilisant les types de données interface/alias est extrêmement utile :)_

Il est important de noter que l'_interface_ est spécifique à TypeScript. Elle est utilisée uniquement au moment de la compilation pour effectuer la vérification des types et pour attraper les erreurs qui pourraient avoir échappé à notre vigilance. **Les données de notre interface finiront dans notre code final, mais l'interface elle-même est compilée.**

**Classes**

Les classes sont, en partie, le véritable "pain et beurre" de TypeScript (au moins à mon humble avis). En restant avec cette idée d'échafaudage de nouveaux objets, les classes nous permettent de construire des données de manière beaucoup plus facile que de simplement les taper manuellement chaque fois que le besoin se présente.

Les classes peuvent être considérées comme des plans pour la manière dont nos données doivent être définies et quelles actions, le cas échéant, elles doivent être capables d'effectuer à travers des méthodes.

Ci-dessous se trouve un exemple de classe en TypeScript (qui est rendu possible par l'introduction des classes dans ES6) :

![code typescript montrant l'utilisation du type de données classe](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-10.png)
_Une classe TypeScript, prête pour l'instanciation :)_

Maintenant, vous pourriez vous demander quelles sont les différences entre une _classe_, un _alias de type_ et une _interface_ ? Excellente question ! La principale différence est que les classes peuvent être instanciées (nous pouvons créer de nouvelles instances d'elles) mais une interface ne le peut pas.

Il existe, bien sûr, d'autres différences mais cela ne fait pas partie du cadre de cet article. Si vous souhaitez approfondir, voici un [excellent article](https://ultimatecourses.com/blog/classes-vs-interfaces-in-typescript#Using_TypeScript_class_vs_using_Typescript_interface) que j'ai lu pour m'aider à comprendre ces différences. Vous trouverez des cas d'utilisation pour tous, comme je l'ai fait, lorsque vous utilisez TypeScript.

**Union**

C'est, de loin, mon type de données préféré de TypeScript ! Le type union nous permet de déclarer une variable et ensuite de la définir sur une valeur "soit l'un soit l'autre". Ce que je veux dire par là, c'est que, par exemple, nous attendons des données à passer dans une fonction mais nous ne sommes pas sûrs si c'est une chaîne de caractères ou un nombre - c'est le but parfait (et prévu) du type union.

Nous utilisons le caractère pipe unique (sur Windows, c'est Shift + la touche juste au-dessus de Entrée) lors de la définition du type. Voici à quoi cela ressemblerait lors de la définition d'une variable avec un type de données union :

`const numOfDoors: string | string[ ];`

Cela indique à TypeScript que _numOfDoors_ est une variable qui peut contenir soit une chaîne de caractères, soit un tableau de chaînes de caractères.

Voici un exemple de cette fonction dont j'ai parlé plus tôt utilisant le type union :

![code typescript montrant l'utilisation du type union](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-11.png)

**Any**

Any est le type que nous définissons lorsque nous ne sommes pas sûrs des types de données que nous allons recevoir. Peut-être recevons-nous quelque chose d'un tiers ou des données dynamiques et nous ne sommes pas sûrs à 100 % si nous recevons une chaîne de caractères, un nombre, ou peut-être un tableau d'informations. C'est le cas d'utilisation parfait pour le type _any_.

![code typescript montrant l'utilisation du type any](https://jonathansexton.me/blog/wp-content/uploads/2019/10/image-12.png)
_Le type de données any est un moyen de se soustraire à la vérification des types_

Je vous mets en garde contre l'utilisation du type _any_ sauf si vous en avez absolument besoin, car lorsque nous l'utilisons, nous nous soustrayons à l'une des fonctionnalités principales de TypeScript - la vérification des types.

Cependant, ce type de données a ses cas d'utilisation tout comme tous les types de données mentionnés.

## C'est tout pour aujourd'hui !

Je vous avais dit que cela ne prendrait pas trop de temps :D

J'espère que vous avez apprécié cet article sur TypeScript et que vous êtes enthousiaste quant à la manière dont il peut s'avérer utile pour votre base de code. Dans le prochain article, nous plongerons dans le côté pratique de TypeScript. Nous aborderons son installation, sa compilation et son utilisation dans votre projet (pas seulement les projets Angular !).

Cela a été initialement publié sur mon [blog](https://jonathansexton.me/blog).

Pendant que vous y êtes, n'oubliez pas de vous inscrire à ma **Newsletter** - vous pouvez le faire en haut à droite de la page. Je promets de ne jamais spammer votre boîte de réception et vos informations ne seront pas partagées avec qui que ce soit/site. J'aime occasionnellement envoyer des ressources intéressantes que je trouve, des articles sur le développement web et une liste de mes nouveaux articles.

Si ce n'est pas encore fait, vous pouvez également me suivre sur les réseaux sociaux ! Tous mes liens sont également en haut à droite de cette page. J'adore me connecter avec les autres et rencontrer de nouvelles personnes, alors n'hésitez pas à dire bonjour :)

Passez une excellente journée et bon codage !