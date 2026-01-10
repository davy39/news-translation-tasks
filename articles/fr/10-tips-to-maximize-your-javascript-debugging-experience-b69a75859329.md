---
title: Choses que vous ne saviez probablement pas pouvoir faire avec la Console de
  Développement de Chrome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-22T05:45:01.000Z'
originalURL: https://freecodecamp.org/news/10-tips-to-maximize-your-javascript-debugging-experience-b69a75859329
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WWyilxdduXEkWudAJaqKsA.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Choses que vous ne saviez probablement pas pouvoir faire avec la Console
  de Développement de Chrome
seo_desc: 'By Swagat Kumar Swain

  Chrome comes with built-in developer tools. This comes with a wide variety of features,
  such as Elements, Network, and Security. Today, we’ll focus 100% on its JavaScript
  console.

  When I started coding, I only used the JavaScrip...'
---

Par Swagat Kumar Swain

Chrome est livré avec des outils de développement intégrés. Ceux-ci offrent une grande variété de fonctionnalités, telles que Elements, Network et Security. Aujourd'hui, nous nous concentrerons à 100% sur sa console JavaScript.

Lorsque j'ai commencé à coder, j'utilisais uniquement la console JavaScript pour logger des valeurs comme les réponses du serveur, ou la valeur des variables. Mais avec le temps, et grâce à des tutoriels, j'ai découvert que la console pouvait faire bien plus que ce que j'imaginais.

Voici des choses utiles que vous pouvez faire avec elle. Si vous lisez ceci dans Chrome (ou tout autre navigateur) sur un ordinateur, vous pouvez même ouvrir ses outils de développement et essayer ces astuces immédiatement.

### 1. Sélectionner des Éléments du DOM

Si vous êtes familier avec jQuery, vous savez à quel point les sélecteurs $(.class) et $(#id) sont importants. Ils sélectionnent les éléments du DOM en fonction de la classe ou de l'ID qui leur est associé.

Mais lorsque vous n'avez pas accès à jQuery dans le DOM, vous pouvez toujours faire la même chose dans la console de développement.

$(tagName) $(.class) $(#id) et $(.class #id) sont équivalents à document.querySelector( ). Cela retourne le premier élément du DOM qui correspond au sélecteur.

Vous pouvez utiliser $$(tagName) ou $$(.class) — notez les doubles signes dollar — pour sélectionner tous les éléments du DOM en fonction d'un sélecteur particulier. Cela les place également dans un tableau. Vous pouvez ensuite sélectionner un élément particulier parmi eux en spécifiant la position de cet élément dans le tableau.

Par exemple, $$(.className) vous donnera tous les éléments qui ont la classe className, et $$(.className)[0] et $$(.className)[1] vous donneront respectivement le premier et le deuxième élément.

![Image](https://cdn-media-1.freecodecamp.org/images/w2nxuoYrVmXoELz4kR-tFqfPOdH146w4hEJA)

### 2. Transformer Votre Navigateur en Éditeur

Combien de fois vous êtes-vous demandé si vous pouviez éditer du texte directement dans le navigateur ? La réponse est oui, vous pouvez transformer votre navigateur en éditeur de texte. Vous pouvez ajouter du texte et supprimer du texte n'importe où dans le DOM.

Vous n'avez plus besoin d'inspecter l'élément et d'éditer le HTML. Au lieu de cela, allez dans la console de développement et tapez ce qui suit :

```
document.body.contentEditable=true 
```

Cela rendra le contenu éditable. Vous pouvez maintenant éditer presque tout dans le DOM.

### 3. Trouver les Événements Associés à un Élément du DOM

Lors du débogage, vous devez être intéressé à trouver les écouteurs d'événements liés à un élément du DOM. La console de développement facilite la recherche de ceux-ci.

getEventListeners($(selector)) retourne un tableau d'objets qui contient tous les événements liés à cet élément. Vous pouvez développer l'objet pour voir les événements :

![Image](https://cdn-media-1.freecodecamp.org/images/ccOt48Q7Uzs5XWOFGtwUiU5-QNeuP-VBuqMc)

Pour trouver l'écouteur d'un événement particulier, vous pouvez faire quelque chose comme ceci :

```
getEventListeners($(selector)).eventName[0].listener 
```

Cela affichera l'écouteur associé à un événement particulier. Ici, eventName[0] est un tableau qui liste tous les événements d'un événement particulier. Par exemple :

```
getEventListeners($(firstName)).click[0].listener 
```

...affichera l'écouteur associé à l'événement de clic de l'élément avec l'ID firstName.

### 4. Surveiller les Événements

Si vous souhaitez surveiller les événements liés à un élément particulier du DOM pendant leur exécution, vous pouvez le faire dans la console également. Il existe différentes commandes que vous pouvez utiliser pour surveiller certains ou tous ces événements :

* monitorEvents($(selector)) surveillera tous les événements associés à l'élément avec votre sélecteur, puis les loguera dans la console dès qu'ils seront déclenchés. Par exemple, monitorEvents($(#firstName)) loguera tous les événements liés à l'élément avec l'ID firstName.
* monitorEvents($(selector),eventName) loguera un événement particulier lié à un élément. Vous pouvez passer le nom de l'événement comme argument à la fonction. Cela loguera uniquement un événement particulier lié à un élément particulier. Par exemple, monitorEvents($(#firstName),click) loguera tous les événements de clic liés à l'élément avec l'ID firstName.
* monitorEvents($(selector),[eventName1,eventName3,...]) loguera plusieurs événements en fonction de vos propres exigences. Au lieu de passer un seul nom d'événement comme argument, passez un tableau de chaînes qui contient tous les événements. Par exemple, monitorEvents($(#firstName),[click,focus]) loguera les événements de clic et de focus liés à l'élément avec l'ID firstName.
* unmonitorEvents($(selector)) : Cela arrêtera la surveillance et le logging des événements dans la console.

### 5. Trouver le Temps d'Exécution d'un Bloc de Code

La console JavaScript possède une fonction essentielle appelée console.time(labelName) qui prend un nom de label comme argument, puis démarre le chronomètre. Il existe une autre fonction essentielle appelée console.timeEnd(labelName) qui prend également un nom de label et arrête le chronomètre associé à ce label particulier.

Par exemple :

```
console.time('myTime'); // Démarre le chronomètre avec le label - myTime
console.timeEnd('myTime'); // Arrête le chronomètre avec le label - myTime

// Sortie : myTime:123.00 ms
```

Les deux lignes de code ci-dessus nous donnent le temps écoulé entre le démarrage et l'arrêt du chronomètre.

Nous pouvons améliorer cela pour calculer le temps nécessaire à l'exécution d'un bloc de code.

Par exemple, supposons que je veux trouver le temps nécessaire à l'exécution d'une boucle. Je peux faire comme ceci :

```
console.time('myTime'); // Démarre le chronomètre avec le label - myTime

for(var i=0; i < 100000; i++){
  2+4+5;
}

console.timeEnd('mytime'); // Arrête le chronomètre avec le label - myTime

// Sortie - myTime:12345.00 ms
```

### 6. Organiser les Valeurs d'une Variable dans un Tableau

Supposons que nous avons un tableau d'objets qui ressemble à ceci :

```
var myArray=[{a:1,b:2,c:3},{a:1,b:2,c:3,d:4},{k:11,f:22},{a:1,b:2,c:3}]
```

Lorsque nous tapons le nom de la variable dans la console, elle nous donne les valeurs sous la forme d'un tableau d'objets. C'est très utile. Vous pouvez développer les objets et voir les valeurs.

Mais cela devient difficile à comprendre lorsque les propriétés augmentent. Par conséquent, pour obtenir une représentation claire de la variable, nous pouvons les afficher dans un tableau.

console.table(variableName) représente la variable et toutes ses propriétés dans une structure tabulaire. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/7gYQsPpJc8CZMser8INb3qNo3pXoMbPv5wVA)

### 7. Inspecter un Élément du DOM

Vous pouvez inspecter directement un élément depuis la console :

* inspect($(selector)) inspectera l'élément qui correspond au sélecteur et vous emmènera à l'onglet Elements dans les outils de développement de Chrome. Par exemple, inspect($(#firstName)) inspectera l'élément avec l'ID firstName et inspect($(a)[3]) inspectera le 4ème élément d'ancrage que vous avez dans votre DOM.
* $0, $1, $2, etc. peuvent vous aider à récupérer les éléments récemment inspectés. Par exemple, $0 vous donne le dernier élément DOM inspecté, tandis que $1 vous donne l'avant-dernier élément DOM inspecté.

### 8. Lister les Propriétés d'un Élément

Si vous souhaitez lister toutes les propriétés d'un élément, vous pouvez le faire directement depuis la Console.

dir($(selector)) retourne un objet avec toutes les propriétés associées à son élément DOM. Vous pouvez développer celles-ci pour les voir en détail.

### 9. Récupérer la Valeur de votre Dernier Résultat

Vous pouvez utiliser la console comme une calculatrice. Et lorsque vous faites cela, vous pouvez avoir besoin de suivre un calcul avec un second. Voici comment récupérer le résultat d'un calcul précédent depuis la mémoire :

```
$_ 
```

Voici à quoi cela ressemble :

```
2+3+4
9 //- La réponse de la somme est 9

$_
9 // Donne le dernier résultat

$_ * $_
81  // Comme le dernier résultat était 9

Math.sqrt($_)
9 // Comme le dernier résultat était 81

$_
9 // Comme le dernier résultat est 9
```

### 10. Effacer la Console et la Mémoire

Si vous souhaitez effacer la console et sa mémoire, tapez simplement :

```
clear()
```

Puis appuyez sur Entrée. C'est tout ce qu'il y a à faire.

Ce ne sont que quelques exemples de ce que vous pouvez faire avec la console JavaScript de Chrome. J'espère que ces astuces vous faciliteront un peu la vie.

Merci d'avoir lu. Si vous avez aimé cet article, n'hésitez pas à le recommander à d'autres personnes ici sur Medium en cliquant sur le bouton cœur ci-dessous. Vous pouvez en savoir plus [sur moi](http://swagatswain.in), ou me suivre sur [Twitter](https://twitter.com/ssswagatss), et ici sur [Medium](https://medium.com/@swagatswain).