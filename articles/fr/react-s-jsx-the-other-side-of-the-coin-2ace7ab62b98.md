---
title: 'Le JSX de React : L''autre côté de la médaille'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-08-13T16:01:13.000Z'
originalURL: https://freecodecamp.org/news/react-s-jsx-the-other-side-of-the-coin-2ace7ab62b98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-FNmTSkYCplwjBfDhQcOmQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Le JSX de React : L''autre côté de la médaille'
seo_desc: 'By Cory House

  Stay calm. Embrace the evolution.

  When React was released, many people took one look at JSX and lost their minds.
  What are these angle brackets doing in JavaScript?! What about separation of concerns?
  Has Facebook learned nothing from t...'
---

Par Cory House

Restez calme. Acceptez l'évolution.

Lors de la sortie de React, beaucoup de gens ont jeté un coup d'œil à JSX et ont perdu la tête. Que font ces chevrons en JavaScript ?! Qu'en est-il de la séparation des préoccupations ? Facebook n'a-t-il rien appris de la communauté ?

%[https://twitter.com/cowboy/status/339858717451362304?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fcowboy%2Fstatus%2F339858717451362304%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F607140403586998273%25252Fe9wUP6dG_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Comme beaucoup, ma réaction initiale au [JSX de React](https://facebook.github.io/react/docs/jsx-in-depth.html) était sceptique, pour dire le moins. Et bien que j'en sois venu à aimer JSX, chaque fois que je le présente à un nouveau développeur, j'ai l'impression de montrer mon bébé laid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RBTfDZzW0N5TzHg_pqWmSg.png)
_Essayez d'imaginer un bébé laid ici. Mon fils est clairement adorable._

Malgré le drame initial, j'en suis venu à réaliser que **JSX n'est pas une idée si radicale après tout. En fait, c'est simplement l'autre côté de la médaille**. C'est une transition évolutive naturelle. Pour apprécier pourquoi, une leçon d'histoire s'impose.

### Phase 1 : JavaScript non intrusif

Vous souvenez-vous des bons vieux jours de jQuery ? L'ère du [JavaScript non intrusif](https://en.wikipedia.org/wiki/Unobtrusive_JavaScript) était en plein essor. Notre HTML était du HTML pur. Notre JavaScript était du JavaScript pur. Nos préoccupations étaient parfaitement séparées.

Nous écrivions du HTML comme ceci :

```html
<a class="hide">Cliquez pour me cacher</a>
```

Puis nous écrivions du JavaScript comme ceci :

```js
$('.hide').click(function() { $(this).hide(); } 
```

#win. N'est-ce pas ? Pas exactement.

Cela semblait être une bonne idée. Notre HTML est totalement pur ! Mais ensuite, nous avons réalisé quelques problèmes : Euh, comment puis-je savoir que ces deux lignes sont interconnectées ? Réponse : Je ne peux pas, sauf si je lis chaque ligne de JavaScript. Avec ce modèle, **vous ne pouvez pas changer une ligne de balisage sans vérifier chaque ligne de JavaScript pour vous assurer que vous ne cassez pas un sélecteur**. Vous voyez, il n'y a pas de séparation réelle ici. Certes, le JS et le HTML sont dans des fichiers séparés, mais ces deux technologies sont fondamentalement liées. Elles doivent évoluer de concert ou l'application plantera.

Séparer strictement le HTML et le JS a en fait conduit à des applications qui étaient _plus difficiles_ à maintenir et à déboguer. Chaque fois que vous vouliez changer une ligne de balisage, vous deviez vous soucier de casser un sélecteur jQuery. Peut-être que si nous relâchions notre dévotion religieuse à la séparation des préoccupations, nous pourrions soulager une partie de cette douleur ? Cela a introduit la phase 2...

### Phase 2 : Liaison bidirectionnelle

Lorsque les développeurs front-end ont vu la liaison bidirectionnelle dans Knockout et Angular, ce fut une révélation. Beaucoup d'entre nous ont abandonné notre dévotion religieuse à la séparation des préoccupations et ont embrassé le pouvoir de déclarer des liaisons en HTML. Lorsque les données changeaient, l'UI changeait. Lorsque l'UI changeait, les données changeaient. Si propre. Si simple.

Certes, chaque bibliothèque et framework a une manière propriétaire de faire cela, mais elles font toutes fondamentalement la même chose. Considérez simplement cet exemple simple d'itération sur un tableau dans quelques frameworks populaires :

```js
//Angular
<div ng-repeat="user in users">
    
//Ember
{{#each user in users}}
 
//Knockout
data-bind="foreach: users"
```

Mais quelque chose d'intéressant est en jeu ici. Peu ont reconnu un problème très fondamental : **Nous mettons effectivement du JavaScript dans notre HTML**. Ce n'est pas une séparation des préoccupations. Toutes ces approches font la même chose : elles rendent le HTML plus puissant en ajoutant un balisage propriétaire supplémentaire. Ce balisage est effectivement analysé comme du JavaScript. Et maintenant que nous sommes enfin à l'aise avec l'intermédiation de JS et HTML de cette manière, il est temps pour React d'intervenir et de nous montrer l'autre côté de la médaille...

### Phase 3 : JSX

Le JSX de React n'est pas un changement radical. C'est simplement le fruit d'une réalisation simple :

> En tant qu'industrie, nous avons déjà décidé : HTML et JavaScript appartiennent ensemble.

Admettons-le, nous ne l'avons pas dit à voix haute. Mais en adoptant Angular, Knockout et Ember, nous avons rendu notre nouvelle préférence claire. Comme je l'ai établi ci-dessus, écrire du code de liaison de données en HTML revient effectivement à mettre du JS dans du HTML. Mais **si nous devons intermingler, pourquoi devrions-nous choisir d'augmenter une technologie aussi faible et laxiste que HTML ?** Les navigateurs ont interprété le HTML de manière lâche depuis le début des temps. Donc, le HTML est-il une fondation logique pour déclarer la liaison de données, les boucles et la logique conditionnelle ?

Facebook a reconnu que JavaScript était une technologie plus logique et plus puissante pour gérer ces deux préoccupations interminglées. L'épiphanie se résume à ceci :

> Angular, Ember et Knockout mettent du "JS" dans votre HTML.  
> React met du "HTML" dans votre JS.

Les avantages de ce mouvement sont multifacettes et ne sont pas nécessairement appréciés jusqu'à ce que vous ayez essayé de travailler avec React et JSX. Le JSX de React est fondamentalement supérieur à tous les frameworks de style "Phase 2" ci-dessus pour quelques raisons simples :

#### Erreurs de compilation

Lorsque vous faites une faute de frappe en HTML, vous n'avez généralement aucune idée de l'endroit où vous avez fait une erreur. Dans de nombreux cas, c'est une erreur silencieuse à l'exécution. Par exemple, si vous tapez n-repeat au lieu de ng-repeat lorsque vous travaillez avec Angular, rien ne se passera. Même histoire avec data-bnd vs data-bind dans Knockout. Dans les deux cas, votre application échouera silencieusement à l'exécution. C'est frustrant.

En revanche, lorsque vous faites une faute de frappe en JSX, cela ne compilera pas. Vous avez oublié de fermer cette balise <li> ? N'aimeriez-vous pas obtenir un retour riche comme celui-ci lorsque vous faites une faute de frappe dans votre HTML ?

```bash
ReactifyError: /components/header.js: Parse Error: Line 23: Expected corresponding JSX closing tag for li while parsing file: /components/header.js
```

Avec JSX, ce retour détaillé est enfin une réalité ! Il est difficile de surestimer à quel point c'est une grande victoire. Cette boucle de retour rapide augmente considérablement la productivité. Comme je le discute dans mon cours Clean Code, [les solutions bien conçues échouent rapidement](http://www.pluralsight.com/courses/writing-clean-code-humans).

#### Tirer parti de toute la puissance de JavaScript

Composer votre balisage dans JavaScript signifie que vous pouvez profiter de toute la puissance de JavaScript lorsque vous travaillez avec votre balisage, au lieu d'un petit sous-ensemble propriétaire qui est offert dans les frameworks centrés sur HTML comme Angular et Knockout.

> Les frameworks côté client ne devraient pas vous obliger à apprendre une syntaxe propriétaire pour déclarer des boucles et des conditionnelles.

React évite le surcoût d'apprendre une autre manière propriétaire de déclarer des boucles et une logique conditionnelle de base. Comme vous pouvez le voir ci-dessus dans la section Phase 2, chaque framework de liaison bidirectionnelle utilise sa propre syntaxe spéciale. En revanche, JSX ressemble presque à du HTML, et il utilise du bon vieux JavaScript pour des choses comme les conditionnelles et les boucles. Dans un écosystème aussi fragmenté que JavaScript, ne pas avoir à apprendre une autre syntaxe de liaison de données propriétaire est une belle victoire.

Et puisque vous écrivez votre balisage dans le même fichier que les données JavaScript associées, de nombreux IDE vous donneront un support d'intellisense lorsque vous référencez vos fonctions. Pensez à la fréquence à laquelle vous avez fait une faute de frappe en référençant une fonction dans les frameworks orientés HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q1aeCkZFM6hB8dkbY4HHqA.png)
_Support d'Intellisense lorsque je référence des fonctions JavaScript dans JSX ? Sympa._

### Réflexions finales

JSX n'est pas une idée folle. C'est une progression naturelle. Alors essayez de ne pas paniquer.

> JSX n'est pas révolutionnaire. C'est évolutif.

Comme la plupart des formes d'évolution, c'est une amélioration claire.

Vous voulez en savoir plus ? Consultez mon nouveau cours "[Building Applications with React and Flux](http://www.pluralsight.com/author/cory-house)" sur Pluralsight.

Participez à la discussion sur [Reddit](https://www.reddit.com/r/javascript/comments/3gv4at/reacts_jsx_dont_freak_out_its_evolutionary/) ou [Hacker News](https://news.ycombinator.com/item?id=10056366).

**_Cory House_** est l'auteur de "[Building Applications with React and Flux](https://www.pluralsight.com/courses/react-flux-building-applications)", "[Clean Code: Writing Code for Humans](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK1pXx89nJAhUujoMKHeuWAEUQFggcMAA&url=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwriting-clean-code-humans&usg=AFQjCNEBfkBoN-IgCn_1jFUqWDAUIxcmAw&sig2=Ub9Wup4k4mrw_ffPgYu3tA)" et de plusieurs autres cours sur Pluralsight. Il est architecte logiciel chez VinSolutions et [forme des développeurs logiciels à l'international](http://www.bitnative.com/training/) sur des pratiques logicielles comme le développement front-end et le code propre. Cory est un MVP Microsoft, un expert développeur Telerik et le fondateur de [outlierdeveloper.com](http://www.outlierdeveloper.com).