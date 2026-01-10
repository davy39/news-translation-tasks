---
title: Les booléens JavaScript expliqués par une analogie judiciaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T04:04:31.000Z'
originalURL: https://freecodecamp.org/news/javascript-booleans-explained-by-going-to-court-a0ca1149a0dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-ZzuerbatF4F0uu9qCvHaA.png
tags:
- name: Boolean
  slug: boolean
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les booléens JavaScript expliqués par une analogie judiciaire
seo_desc: 'By Kevin Kononenko

  If you have ever watched a TV show about court (or been to court), then you can
  understand booleans in JavaScript.

  You might think that booleans are the most straightforward topic that you could
  ask for in JavaScript.

  After all, si...'
---

Par Kevin Kononenko

Si vous avez déjà regardé une émission de télévision sur les tribunaux (ou si vous y êtes allé), alors vous pouvez comprendre les booléens en JavaScript.

Vous pourriez penser que les booléens sont le sujet le plus simple que vous puissiez demander en JavaScript.

Après tout, puisque une variable peut être de l'un des types suivants :

* nombre
* chaîne de caractères
* tableau
* objet
* booléen

… le booléen semble être le plus facile.

```
let bool = true;
```

```
let bool = false;
```

Les seules deux options pour un booléen sont `true` ou `false`. Et ils sont utilisés dans les instructions `if()` pour décider quelle instruction doit être exécutée.

```
if(true){
```

```
}
```

```
else{
```

```
// si la valeur est false, ce bloc s'exécute
```

```
}
```

Mais voici le truc. Dans les instructions `if()`, d'autres valeurs de variables peuvent **évaluer** à true ou false. En d'autres termes, une fois la valeur utilisée dans l'instruction `if()`, JavaScript évaluera si elle est `true` ou `false`.

Par exemple, savez-vous si la valeur 0 est `true` ou `false` ?

Ce n'est pas une question philosophique. JavaScript a une réponse.

Quoi qu'il en soit, cela se produit parce que JavaScript est un langage **faiblement typé**. Cela signifie que dans le contexte d'une instruction `if()`, il convertira d'autres valeurs de variables en `true` ou `false` afin d'exécuter le code. Cela est connu sous le nom de détermination de la "véracité" d'une valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JYzIah834O2zHY4K)

De nombreux autres langages sont **fortement typés**, donc ils ne convertiront pas les valeurs en true ou false.

Cela peut sembler un peu fou, mais c'est en fait assez similaire à la manière dont un juge aux États-Unis détermine si une personne accusée est innocente ou coupable. Donc, je peux expliquer comment la "véracité" et `true`/`false` fonctionnent en JavaScript à travers des règles juridiques que vous avez vues dans "Law and Order" ou tout autre drame judiciaire à la télévision.

Aux fins de ce tutoriel, imaginez que vous êtes un procureur de district qui tente de poursuivre une personne accusée de vol de voiture.

Et, vous devrez comprendre les [bases des variables en JavaScript](https://blog.codeanalogies.com/2017/12/20/a-visual-guide-to-understanding-the-sign-in-javascript/) pour utiliser ce tutoriel. Commençons !

### Qu'est-ce que la "véracité" en JavaScript ?

Aux États-Unis, le système de droit pénal stipule qu'une personne accusée est "innocente jusqu'à preuve du contraire". Cela signifie que la charge incombe au procureur (vous, dans ce cas) de fournir suffisamment de preuves pour réfuter l'hypothèse par défaut selon laquelle la personne accusée est innocente.

En fait, la norme de preuve est "[au-delà de tout doute raisonnable](https://en.wikipedia.org/wiki/Reasonable_doubt)". Cela est cohérent dans de nombreux pays du monde.

Lorsque nous utilisons des instructions `if()`, nous ne pourrons pas toujours insérer une variable avec une valeur de `true` ou `false`. Souvent, nous devons insérer une instruction qui sera évaluée par JavaScript **comme** `true` ou `false`.

Cela est similaire au système juridique ! Bien qu'il soit **possible** qu'il y ait une pièce à conviction qui rend le verdict "coupable" ou "non coupable" évident, il est également probable qu'un juge ou un jury doive évaluer plusieurs pièces à conviction et prendre une décision.

Commençons par les bases. Une instruction `true` est une preuve qui conduira à la condamnation de l'accusé. Une instruction `false` est une preuve qui le laissera libre. Créons une variable appelée `evidence` et définissons-la sur `true`.

```
let evidence = true;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

`convict()` et `release()` sont des fonctions inventées. Dans ce cas, puisque la preuve est définie sur `true`, le juge condamnerait le voleur de voiture. Voici un diagramme interactif de ce scénario.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hQ4EcsTZPmWWNOXLvxRThQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zNtmdN3AjQ4Tpcl_Xa_oKA.jpeg)

Le voleur ressemble un peu à Edward Norton dans "The Italian Job", n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*FRlRPnEU3_Pu7fYK)

Quoi qu'il en soit, dans la vraie vie, ce n'est jamais aussi simple. Supposons que vous avez une preuve accablante — des empreintes digitales sur la portière de la voiture. Vous présentez cela au juge.

```
let evidence = "fingerprints";
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

Ah ! Nous n'avons changé que la première ligne, où nous avons déclaré la variable evidence. Et c'est maintenant une chaîne de caractères plutôt qu'un booléen. Mais devinez quoi ? En raison de la **coercition de type**, JavaScript évaluera la chaîne comme `true`. Puisqu'il n'y a pas de condition dans l'instruction `if()`, toutes les chaînes sont `true`. Nous exécuterions la fonction `convict()` !

![Image](https://cdn-media-1.freecodecamp.org/images/0*3f8jEtYDOMaiVPeX)

### Exemples de véracité

Imaginons que, au lieu de cela, la variable evidence est définie sur `0`. Nous exécutons à nouveau la même instruction `if()`.

```
let evidence = 0;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

Dans ce cas, l'instruction serait en fait évaluée à `false`, et notre accusé de vol de voiture serait libéré.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x6feidPaPL5Uga82)

C'est pourquoi cela s'appelle la "véracité" — parce que JavaScript évalue si la condition est `true` ou `false`.

Puisque la variable est définie sur `0`, c'est un peu comme si vous étiez invité à présenter des preuves contre le voleur, et que vous disiez… rien.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vDx4QLx1Hfwa6e07)

Évidemment, le juge va déterminer que vous n'avez pas assez de preuves et libérer la personne ! Il en serait de même si la preuve était définie sur une chaîne vide ````. Vous n'offrez toujours rien, donc votre instruction est évaluée comme `false`_._

```
let evidence = '';
```

Voici un autre test pour voir si vous comprenez `true` versus `false`. Que se passe-t-il si la variable n'a pas encore été initialisée à une valeur ?

```
let evidence;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

C'est un cas assez courant, car les développeurs web auront une autre instruction dans leur script qui donne une valeur à la variable `evidence`. Et, tout comme les deux exemples ci-dessus, JavaScript évaluera cette variable comme `false` si elle n'a aucune valeur.

C'est un excellent exemple de "innocent jusqu'à preuve du contraire". La variable n'a pas encore été assignée à une valeur, donc il n'y a aucun moyen pour JavaScript de l'appeler `true`.

### Utilisation des éléments DOM dans les instructions if()

Nous avons donc couvert les valeurs des variables qui sont "falsy". Mais qu'en est-il des éléments du DOM ?

**Note** : si vous avez besoin d'un rappel, consultez mon [guide des éléments DOM ici](https://blog.codeanalogies.com/2018/01/06/traversing-the-dom-visual-explanation/).

En d'autres termes, que se passe-t-il lorsque nous utilisons un élément DOM pour déterminer quelle branche d'une instruction `if/else` exécuter ? Si vous utilisez jQuery ou React (ou Angular, et ainsi de suite), vous manipulez probablement le DOM afin de créer une interface plus dynamique.

Dans notre exemple de tribunal, supposons que vous juriez que le crochet utilisé par le voleur se trouve dans une poubelle près de la scène de crime. En termes HTML, vous dites qu'il y a une div avec l'ID `lockpick` quelque part dans le DOM. Comment le juge pourrait-il valider votre affirmation ?

```
if(document.getElementById('lockpick')){
```

```
  convict()
```

```
}
```

```
else{
```

```
  release()
```

```
}
```

Voici une image interactive de ce scénario.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p37rdMZPQYElpR9ZZCITcQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jcorLVV6rRXqiHk_XnBKdQ.jpeg)

La "véracité" ici signifie que JavaScript inspectera le DOM et ne retournera `true` que s'il trouve un élément avec l'ID `lockpick`. C'est un peu comme un juge déterminant si la preuve que vous présentez est réelle et authentique. Dans ce cas, elle l'est, donc le premier bloc de code s'exécutera et la personne sera condamnée.

C'est super utile ! Nous avons maintenant étendu le concept de `true` pour inclure si un élément existe ou non. Cette logique s'applique également aux objets et aux tableaux. Vous pouvez vérifier si un élément avec une classe spécifique existe, si un certain élément a des enfants, vous comprenez l'idée.

### Plus de variations des instructions if()

Lorsque vous amenez une personne accusée devant un tribunal, elle peut encore être condamnée pour un crime mineur. Si vous n'avez pas assez de preuves pour l'accusation principale, elle peut encore être condamnée pour des accusations moindres.

Dans l'exemple du vol de voiture, il y a un crime de violation de domicile, puis le vol est possible si la personne accusée a déjà pénétré dans la voiture.

Nous pouvons combiner `if()`, `else if()`, et `else()` pour modéliser ces options. Supposons que la personne accusée **a** pénétré dans la voiture, mais n'a rien pris. Nous pourrions modéliser les options comme ceci :

```
let breaking = true;
```

```
let theft = false;
```

```
if (breaking && theft){
```

```
  convict('felony');
```

```
}
```

```
else if(breaking){
```

```
  convict ('misdemeanor');
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

Il y a maintenant trois scénarios. Si la première condition est satisfaite, ce bloc de code s'exécutera. Cela signifie que le voleur serait condamné pour un crime. Mais, si seule la valeur de la variable `breaking` peut être évaluée comme `true`, la personne sera toujours condamnée pour un délit.

Le juge dit : "Vous devez me montrer des preuves de violation de domicile **et** de vol si je dois condamner cette personne pour un crime."

![Image](https://cdn-media-1.freecodecamp.org/images/0*09AccMKv051RIVLG)

La première instruction `if()` évaluera `true && false`, ce qui sera réduit à `false` puisque `false` prime sur `true` (rappelez-vous, innocent jusqu'à preuve du contraire).

Cela fonctionnerait toujours si nous utilisions des valeurs qui étaient "véritables" ou "fausses". Chacune serait évaluée à `true` ou `false` dans l'instruction `if()`, puis JavaScript déciderait quel bloc exécuter.

### Obtenez plus de tutoriels visuels

Avez-vous apprécié ce guide ? Donnez-lui un "clap", ou inscrivez-vous ci-dessous pour recevoir mes derniers tutoriels sur les sujets de développement web.