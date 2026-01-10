---
title: ES6 offre aux développeurs JavaScript plus de façons de faire les choses. Mais
  ce n'est pas toujours une bonne chose.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T07:01:01.000Z'
originalURL: https://freecodecamp.org/news/is-es6-destroying-javascript-drowning-in-options-7fc02d25d81c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JSUlDdjjA24TSCGKPkLm_w.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: ES6 offre aux développeurs JavaScript plus de façons de faire les choses.
  Mais ce n'est pas toujours une bonne chose.
seo_desc: 'By Sam Williams

  I recently wrote an article on ES6 Tips and Tricks which has over 17,000 views and
  4,600 claps. One comment was from Bob Munck who said that:


  This article makes a very strong argument for avoiding JavaScript like the plague
  in any us...'
---

Par Sam Williams

J'ai récemment écrit un article sur [ES6 Tips and Tricks](https://medium.freecodecamp.org/make-your-code-cleaner-shorter-and-easier-to-read-es6-tips-and-tricks-afd4ce25977c) qui a plus de 17 000 vues et 4 600 applaudissements. Un commentaire était de [Bob Munck](https://www.freecodecamp.org/news/is-es6-destroying-javascript-drowning-in-options-7fc02d25d81c/undefined) qui a dit que :

> Cet article présente un argument très solide pour **éviter JavaScript comme la peste** dans toute utilisation où vous voulez une fiabilité, une maintenabilité et une modifiabilité à long terme.

Son opinion semble être que si le langage change autant, il signe son propre arrêt de mort.

### Ce que ES6, 7 et 8 ajoutent à JavaScript

Les nouvelles spécifications ajoutent beaucoup de nouvelles fonctionnalités au langage. La destructuration, l'assignation concise d'objets et les symboles, pour n'en nommer que quelques-unes. Il y a de bonnes choses qui arrivent, mais cet article vise à mettre en lumière les problèmes.

### Pourquoi est-ce un problème ?

Vous voulez créer une fonction pour recevoir un objet et effectuer une logique dessus. Simple, non ? Mais quelle méthode allez-vous utiliser ?

```
var data = { a: "print me" };
```

```
function method1(data) {    var a = data.a;    console.log(a);}
```

```
function method2(data) {    console.log(data.a);}
```

```
function method3({ a: info }) {    console.log(info);}
```

```
function method4({ a }) {    console.log(a);}
```

Toutes ces méthodes vous donnent exactement le même résultat. C'est un exemple très trivial, mais il reste vrai pour des fonctions bien plus complexes.

#### Comment décider quoi utiliser ?

Il existe 3 méthodes principales pour décider de la manière de procéder :

* Évaluer et comparer les options disponibles.
* Utiliser simplement ce que vous voulez.
* Avoir une politique sur ce qu'il faut utiliser et où.

Chacune de ces méthodes a ses propres avantages et inconvénients.

![Image](https://cdn-media-1.freecodecamp.org/images/VprwzhiI2Ve-XFhV-6YVbHMSEZhnIXk2wONE)
_Photo : [pixabay.com](https://pixabay.com/en/thought-idea-innovation-imagination-2123971/" rel="noopener" target="_blank" title=")_

#### Évaluer et comparer les options disponibles

Cela semble être un choix évident, mais est-ce le meilleur ? Faire cela à chaque fois signifie que vous devez évaluer les avantages et les inconvénients de chaque méthode À CHAQUE FOIS que vous écrivez une fonction. Cela représente beaucoup de puissance de réflexion qui pourrait être utilisée pour résoudre le problème que vous essayez de résoudre.

Vous et toutes les personnes avec lesquelles vous travaillez devez connaître les avantages, les inconvénients et les nuances de chaque méthode. Cela ne semble pas trop grave, il n'y en a que 4, mais qu'en est-il de la gestion du comportement asynchrone ? Utilisez-vous des callbacks, des Promesses, des Générateurs, ou Async/Await, ou une combinaison de ceux-ci ?

Cela signifie que toutes les personnes avec lesquelles vous travaillez doivent comprendre chaque partie du langage. Je suppose, d'après le nombre de vues sur mon article ES6, que beaucoup de gens apprennent encore certaines des syntaxes de base du langage. Cela signifie qu'il y a très peu de personnes qui comprennent les complexités du comportement asynchrone (que je tente actuellement de bien comprendre moi-même).

#### Utiliser simplement ce que vous voulez

C'est l'approche la plus courante, pour les individus et dans les entreprises. Cela peut être génial car cela signifie que vous ne perdez pas de temps et d'efforts à calculer le meilleur choix.

Les problèmes pourraient survenir lorsque quelqu'un d'autre vient lire ou corriger votre code. Vous pouvez être un prodige de JavaScript et connaître toutes les nouvelles méthodes pour tout. Mais la prochaine personne qui viendra lire ou modifier votre travail pourrait ne pas avoir la moindre idée de ce que vous avez fait.

Cela encourage également de grandes différences de style entre les entreprises et les collègues. Cela peut également signifier des différences entre vous et un vous futur, lorsque vous apprendrez une nouvelle syntaxe. Ce n'est pas génial et rend la lecture de code écrit par plusieurs développeurs beaucoup plus difficile.

![Image](https://cdn-media-1.freecodecamp.org/images/34VI1AbwgDW-WSK49E5slOcsguRkTQ5yhrIx)
_Photo : [pixabay.com](https://pixabay.com/en/bureaucracy-aktenordner-paperwork-2106924/" rel="noopener" target="_blank" title=")_

#### Politique

Qu'il s'agisse de la politique de l'entreprise ou de la politique personnelle, cela élimine beaucoup des problèmes des deux premières approches. Cela ne nécessite pas de réflexion et favorise la cohérence dans une base de code. Malheureusement, cela pose encore quelques problèmes.

Avec les nouvelles versions des spécifications ECMAScript qui sortent régulièrement, un dilemme se pose. L'entreprise doit-elle changer sa politique pour rester en phase avec les nouvelles versions ? Ou écrire une politique et ne jamais la changer — en ratant les nouvelles fonctionnalités ? Ou doit-elle être quelque part entre les deux ?

Les nouveaux employés doivent apprendre la politique et savoir comment l'utiliser. Oui, vous pourriez avoir un livret sur les politiques, mais il pourrait prendre plus de temps pour trouver la spécification que pour écrire la ligne de code. Même s'ils trouvent la politique sur le comportement asynchrone, ils doivent ensuite être capables de l'utiliser. Cela pourrait finir par limiter les développeurs juniors à un codage simple car ils ne veulent pas _enfreindre la politique_, restreignant massivement leur croissance.

### Que fournit vraiment ES6+ ?

Quelle est la réelle différence entre les exemples que j'ai donnés ci-dessus ? Les nouvelles syntaxes sont-elles plus faciles à lire ou offrent-elles une fonctionnalité supplémentaire ?

> leurs suggestions doivent {faire} avec la réduction des frappes et l'ajout de trucs qui sont "sympas".

Je ne vois vraiment pas beaucoup, voire aucun, avantage à utiliser la destructuration ou la syntaxe concise des objets, à part économiser des frappes. Il peut y avoir des avantages de performance ou une sorte de magie spéciale que je ne connais ou ne comprends pas, mais :

[Aucune de ces différences de performance n'a d'importance, du tout ! — YDKJS](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch6.md)

![Image](https://cdn-media-1.freecodecamp.org/images/FYwgy4oQHlGhVRzaeoIsZS96Uh9xO-DY5MYF)
_photo : [pixabay.com](https://pixabay.com/en/hourglass-time-hours-sand-clock-620397/" rel="noopener" target="_blank" title=")_

Cette citation est un peu sortie de son contexte, alors je vais expliquer. Supposons que la méthode X exécute 1 000 000 d'opérations/seconde et que la méthode Y exécute 500 000 opérations/seconde. Cela signifie que X est deux fois plus rapide que Y. **Mais** la différence de temps d'exécution n'est que de 1 microseconde. Cela représente 100 000 fois plus lent que ce que l'œil humain peut percevoir. Donc aucune des différences de performance n'a d'importance du tout !

Les économies réalisées en utilisant différentes méthodes sont probablement si minuscules que cela n'a pas d'importance. Si vous essayez d'écrire le code le plus rapide possible, pourquoi l'écrivez-vous en JavaScript ?

#### Ce que ES6 fournit également

Confusion, Complexité et Options.

![Image](https://cdn-media-1.freecodecamp.org/images/GgQ1Bb9hQJ4YLtUmAEt8Cw6bS0mTzsQ5bkxR)

Plus tard dans la discussion avec Bob, il a dit cela à propos de JavaScript :

> Vous devez le _décoder_ pour comprendre ce qu'il fait. La syntaxe et la sémantique du langage sont complexes, intricates, convoluted. Les programmeurs qui déboguent, maintiennent, améliorent et révisent votre code le lendemain ou une décennie plus tard auront du mal à le comprendre. Ils se demanderont si quelque chose que vous avez fait était incroyablement intelligent ou incroyablement stupide.

Cela a résonné si vrai avec moi. Je me suis retrouvé à regarder du code que j'avais écrit, me creusant la tête pour comprendre ce que j'avais fait et pourquoi je l'avais fait. Bien que vous puissiez écrire du code complexe et confus dans n'importe quel langage, JavaScript vous offre de nombreuses opportunités de vous piéger vous-même.

Je me suis fait cela à moi-même dans l'article ES6. Parmi les 4 000 personnes qui ont lu l'article entier, seulement 5 ont réussi à trouver mon erreur avant que je ne la corrige. Laquelle de celles-ci est correcte ?

```
let person = {     name: "John",     age: 36,     job: { company: "Tesco", role: "Store Assistant"}}
```

```
function methodA({ name: driverName, age, job.company: company}){ ... }
```

```
function methodB({ name: driverName, age, job: { company }){ ... }
```

J'ai utilisé la mauvaise et la plupart des gens ne l'ont pas remarqué. Seuls ceux qui l'ont essayée ont réussi à trouver l'erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/rHzev1lGqapGQbzpEBx3HxLckNRfdTJOabk2)

Que fournissent vraiment ces deux méthodes pour justifier la confusion et la complexité supplémentaires ? Beaucoup de gens pourraient lire, écrire et comprendre une fonction comme celle-ci :

```
function methodC(person){    var driverName = person.name,        age = person.age,        company = person.job.company;    ...}
```

Oui, j'ai dû écrire 32 caractères supplémentaires, mais comme la plupart de la programmation consiste à réfléchir, et non à taper, économisons-nous du temps de frappe pour en passer plus à réfléchir ?

Ce n'est pas seulement le temps supplémentaire que l'auteur passe à y réfléchir, c'est chaque personne qui lit ce code après ce point (souvent l'auteur à nouveau). Le code compliqué a la "taxe de réflexion" à chaque fois qu'il est lu et nous, en tant qu'êtres humains, n'avons qu'une quantité limitée de puissance de réflexion chaque jour.

#### Tout n'est pas mauvais

Bien que cet article semble critiquer ES6, il y a certaines choses qui augmentent la lisibilité et la maintenabilité. Les Promesses, les fonctions asynchrones et async/await aident toutes à abstraire les complexités du comportement asynchrone, rendant le code plus logique et plus facile à lire. C'est ce que je crois devrait être mis en avant, et non les astuces d'économie de frappes.

### Effets à long terme

Bien que cela ne fera probablement aucune différence pour vous en tant que développeur, les entreprises avec beaucoup de développeurs pourraient en ressentir l'impact. Devoir d'abord comprendre ce que la syntaxe fait avant de comprendre ce que le code fait entraîne un code peu fiable et difficile à maintenir.

Cela pourrait entraîner une perte de faveur pour JavaScript pour tout ce qui est grand, complexe, critique ou évolutif. Ce serait un énorme marché pour JavaScript à perdre.

### Résumé

* ES6 nous offre encore plus de façons de faire la même tâche.
* Vous pouvez calculer ce qui est le mieux, faire ce que vous voulez, ou avoir une politique à ce sujet.
* ES6 nous donne de nouveaux trucs pour économiser quelques frappes.
* Ces nouveaux trucs augmentent la complexité et les chances d'erreur tout en réduisant la lisibilité.
* Il y a de bonnes parties de ES6, augmentant la lisibilité.
* La complexité accrue et la lisibilité réduite pourraient-elles rendre les entreprises moins susceptibles de l'utiliser dans des solutions complexes, critiques ou en constante évolution ?

> Qu'en pensez-vous ? Faites-le moi savoir dans les commentaires. Si vous avez aimé, applaudissez et suivez-moi pour plus d'articles sur JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/IlmT2dhqkBmqwHaLmF17l7Qm4pAqBmOnz-9c)