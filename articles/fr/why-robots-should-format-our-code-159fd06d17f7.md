---
title: Pourquoi les robots devraient formater notre code à notre place
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-08T14:00:58.000Z'
originalURL: https://freecodecamp.org/news/why-robots-should-format-our-code-159fd06d17f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U-jFxHWyzxtZTGtS6Q2CQQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Pourquoi les robots devraient formater notre code à notre place
seo_desc: 'By Artem Sapegin

  I used to think that a personal code style is a good thing for a programmer. It
  shows you are a mature developer who knows what good code should look like.

  My college professors told me that they knew when some of my classmates used ...'
---

Par Artem Sapegin

Je pensais autrefois qu'un style de code personnel était une bonne chose pour un programmeur. Cela montre que vous êtes un développeur mature qui sait à quoi ressemble un bon code.

Mes professeurs de l'université me disaient qu'ils savaient quand certains de mes camarades de classe utilisaient mon code dans leurs travaux à cause du style de code différent. Maintenant, je pense que c'était parce que mon code était au moins quelque peu formaté et que celui des autres était un désordre.

Depuis, j'ai passé beaucoup de temps à discuter du style de code et à configurer des outils pour le faire respecter. Il est temps pour un changement.

#### Quelques exemples

Après avoir lu [The Programmers’ Stone](https://www.datapacrat.com/Opinion/Reciprocality/r0/index.html), j'ai mis les accolades comme ceci pendant longtemps :

```
if (food === 'pizza'){    alert('Pizza ;-)');  }else{      alert('Not pizza ;-(');}
```

Mais ensuite, j'ai réalisé que j'étais probablement le seul à le faire de cette manière dans la communauté front-end. Tout le monde utilise ce style :

```
if (food === 'pizza') {    alert('Pizza ;-)');  } else {    alert('Not pizza ;-(');}
```

Ou celui-ci :

```
if (food === 'pizza') {    alert('Pizza ;-)');  }else {      alert('Not pizza ;-(');}
```

J'ai donc changé mon style pour le dernier.

J'aime beaucoup ce style pour le chaînage :

```
function foo(items) {  return items    .filter(item => item.checked)    .map(item => item.value)  ;}
```

Je vois les mêmes avantages de refactoring que pour les [virgules finales](https://medium.com/@nikgraf/why-you-should-enforce-dangling-commas-for-multiline-statements-d034c98e36f8) :

```
const food = [  'pizza',  'burger',  'pasta',]
```

Mais je suis probablement encore plus seul avec ce style que je ne l'étais avec les accolades. Personne ne m'enverrait jamais de code à réviser avec ce style, aucun linter ne peut l'imposer. Je dois donc arrêter de l'utiliser aussi pour être plus proche de la réalité.

Il y a une autre chose que personne d'autre ne fait sauf moi. Je mets toujours deux espaces avant un commentaire de fin de ligne :

```
const volume = 200;  // ml
```

Je pensais que cela améliorait la lisibilité. Mais en réalité, cela rend la base de code incohérente parce que les autres développeurs ne mettent qu'un seul espace.

#### Ce que font les développeurs JavaScript

Malheureusement, JavaScript n'a pas de style de code officiel. Il existe quelques [styles de code populaires](http://blog.sapegin.me/all/javascript-code-styles) comme [Airbnb](http://airbnb.io/javascript/) ou [Standard](https://standardjs.com/). Vous pourriez les utiliser pour rendre votre code familier aux autres développeurs.

Vous pourriez utiliser [ESLint](https://eslint.org/) pour imposer un style de code et même auto-formater le code dans certains cas. Mais cela ne rendra pas votre base de code 100% cohérente. ESLint avec la configuration Airbnb normaliserait seulement mon premier exemple et permettrait l'incohérence dans les deux autres exemples.

#### Ce que les développeurs JavaScript devraient faire

Certains langages ont des styles de code stricts et des outils pour formater le code. Ainsi, les développeurs ne perdent pas de temps à discuter du style de code. Regardez [Refmt](https://reasonml.github.io/guide/what-and-why) pour Reason et [Rustfmt](https://github.com/rust-lang-nursery/rustfmt) pour Rust.

Il semble que JavaScript ait enfin [une solution](http://jlongster.com/A-Prettier-Formatter) à ce problème. Un nouvel outil appelé [Prettier](https://github.com/prettier/prettier) reformatera votre code en utilisant ses propres règles. Il ignore complètement la manière dont le code a été écrit initialement.

Essayons [Prettier](https://prettier.github.io/prettier/) sur mes exemples :

```
if (food === 'pizza') {  alert('Pizza ;-)');} else {  alert('Not pizza ;-(');}function foo(items) {  return items.filter(item => item.checked).map(item => item.value);}const volume = 200; // ml
```

Vous pouvez ne pas être d'accord avec ce style. Par exemple, je n'aime pas le placement du `else` et l'écriture des chaînes de fonctions sur une seule ligne est discutable. Mais je vois d'énormes avantages à adopter Prettier :

* Presque aucune décision à prendre — Prettier a peu d'options.
* Pas de discussions sur des règles particulières si vous travaillez en équipe.
* Pas besoin d'apprendre le style de code de votre projet pour les contributeurs.
* Pas besoin de corriger les problèmes de style signalés par ESLint.
* Possibilité de configurer l'auto-formatage lors de l'enregistrement du fichier.

#### Conclusion

Prettier a déjà été adopté par [certains projets populaires](https://github.com/prettier/prettier/issues/1351) comme React et Babel. Et je commence à [convertir tous mes projets](https://github.com/tamiadev/eslint-config-tamia) de mon style de code personnalisé à Prettier. Je le recommanderai au lieu du style de code Airbnb.

Au début, j'ai eu beaucoup de moments "Beurk, c'est moche" avec Prettier. Mais quand je pense que je devrais, par exemple, reformater manuellement le code JSX d'une seule ligne à plusieurs lignes lorsque j'ajoute une autre propriété et qu'il ne tient pas sur une seule ligne — je réalise que cela en vaut vraiment la peine.

![Image](https://cdn-media-1.freecodecamp.org/images/ODqOCbNyAvfD6nTpbUD0Wyxv4oafOqurjvgQ)
_Prettier formate votre code lorsque vous enregistrez un fichier_

Lisez comment [configurer Prettier](https://survivejs.com/maintenance/code-quality/code-formatting/) dans votre projet.

P. S. [Jetez un œil à mon nouvel outil](https://github.com/sapegin/mrm) qui simplifiera l'ajout d'ESLint, Prettier et d'autres outils à votre projet, ainsi que la synchronisation de leurs configurations.

**Abonnez-vous à ma newsletter : [https://tinyletter.com/sapegin](https://tinyletter.com/sapegin)**