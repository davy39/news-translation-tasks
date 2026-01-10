---
title: Comment éviter les pièges courants des débutants et commencer à coder comme
  un pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T22:48:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-common-beginner-pitfalls-and-start-coding-like-a-pro-3de81c6affbe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lQDZ3LDJf5bKwvLtocFGJw.jpeg
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Comment éviter les pièges courants des débutants et commencer à coder comme
  un pro
seo_desc: 'By Dmitri Grabov

  Learning to code is tough. We’ve all encountered cryptic errors and code breaking
  for no obvious reason. Sadly, this experience is part of learning to code. There
  are a few steps you can take to improve your code quality and prevent ...'
---

Par Dmitri Grabov

Apprendre à coder est difficile. Nous avons tous rencontré des erreurs cryptiques et du code qui ne fonctionne pas sans raison apparente. Malheureusement, cette expérience fait partie de l'apprentissage de la programmation. Il existe quelques étapes que vous pouvez suivre pour améliorer la qualité de votre code et prévenir les bugs courants.

### Évitez de copier-coller du code

Une grande partie de l'apprentissage que vous ferez en tant que débutant viendra de la répétition. Ce n'est pas exactement glamour, mais après avoir écrit une boucle for pour la 100ème fois, vous le ferez presque sans réfléchir.

Vous serez souvent tenté de copier et coller du code pour vous éviter la peine de le taper. Vous devriez l'éviter à tout prix. Il pourrait y avoir une subtile différence entre le code que vous voulez écrire et ce que vous copiez. Cela pourrait introduire un bug subtil qui pourrait être difficile à tracer.

> _Lorsque vous copiez du code, vous contournez entièrement le processus cognitif._

Assurez-vous de comprendre le code que vous écrivez autant que possible. Lorsque vous copiez du code, vous contournez entièrement le processus cognitif. Même si le code que vous avez copié fonctionne comme prévu, vous n'avez pas appris grand-chose en le collant. Chaque fois que vous tapez votre code en entier, vous devenez plus familier et à l'aise avec celui-ci.

### Des noms sensés

> Il n'y a que deux choses difficiles en informatique : l'invalidation du cache et le nommage des choses.

> — Phil Karlton

Utilisez des noms pour les variables et les propriétés. Rendez-les aussi descriptifs que possible.

Utilisez toujours des mots complets et évitez les abréviations. Différentes personnes peuvent interpréter les abréviations de différentes manières. Cela pourrait rendre plus difficile la compréhension de ce que fait le code. Par exemple, `intlSize` pourrait signifier soit `internationalSize` soit `internalSize`. L'indice important dans un nom est perdu à cause de l'abréviation.

Lorsque vous faites référence à la même chose dans votre base de code, utilisez le même nom. Par exemple, évitez de faire référence à `doorColour` comme `colourOfDoor` ou `doorColor` ailleurs. Cela vous évitera des bugs causés par l'utilisation de mauvais noms de variables. De plus, la cohérence vous fera gagner du temps en cherchant le nom exact de la variable à chaque fois.

Évitez les noms génériques et non descriptifs comme `data` ou `process`. Ils pourraient signifier n'importe quoi et ne fournissent pas beaucoup d'informations sur leur but.

### Indentation cohérente

Une indentation de code cohérente facilite la détection des bugs potentiels. C'est ce que font les développeurs professionnels sans y penser. Très peu d'entre eux en parlent parce que c'est si évident pour eux. Pourtant, peu de tutoriels soulignent l'importance d'utiliser une indentation cohérente.

Dans les exemples ci-dessous, nous indentons en utilisant des tabulations, cependant les espaces sont également acceptables. L'important est de choisir celui que vous voulez utiliser et de l'appliquer de manière cohérente. Ne mélangez pas les tabulations et les espaces dans votre code.

À quoi ressemble une indentation correcte ? Chaque fois que vous insérez une balise HTML à l'intérieur d'une autre, ajoutez une nouvelle ligne et une tabulation devant la nouvelle balise pour l'indenter. Lorsque vous fermez une balise HTML, ajoutez une nouvelle ligne et retirez une tabulation de votre indentation.

![Image](https://cdn-media-1.freecodecamp.org/images/uwvEIwAGKDftbiikMfHJROTWS4DO28VzDu3i)

Ici, la balise interne est la balise `img`. Voyez comment elle est indentée d'une tabulation ? Remarquez également comment le bord gauche de la balise de fermeture `div` s'aligne avec le bord gauche de sa balise d'ouverture.

Cette approche devient super importante lorsque vous avez des centaines de balises sur une page. Si vous avez suivi le processus correctement, votre balise de fermeture finale devrait s'aligner avec le côté gauche de votre page. Cela constitue une vérification pratique de la correction du code.

Voyons comment nous pouvons utiliser l'indentation pour repérer les balises manquantes.

![Image](https://cdn-media-1.freecodecamp.org/images/NlNKtp8StBvnQLJKAfJLDOzk6iCpzSzJYlSE)

Voyez comment dans l'exemple ci-dessus la balise de fermeture `div` à la ligne 14 ne s'aligne pas avec la balise d'ouverture `div` à la ligne 1 ? C'est un indice que quelque chose manque. Dans ce cas, nous avons oublié la balise de fermeture `ul`. Une fois que nous l'avons ajoutée, la balise de fermeture `div` s'aligne avec son partenaire d'ouverture.

![Image](https://cdn-media-1.freecodecamp.org/images/o7Wu3YOVNchqWmm-NIeqrZtGaw4dydrW4OUx)

Une méthode similaire devrait être appliquée lors de l'écriture de JavaScript. Nous n'avons pas de balises en JavaScript, mais nous avons des "accolades" ou "parenthèses courbées". Elles ressemblent à ceci `{}`. Chaque accolade ouvrante doit avoir une accolade fermante correspondante. Elles sont utilisées pour dénoter des blocs de code. Chaque accolade ouvrante devrait être suivie d'une nouvelle ligne et d'une tabulation pour indenter le contenu. L'accolade fermante devrait s'aligner sur le côté gauche avec le côté gauche de la ligne de son accolade ouvrante correspondante.

![Image](https://cdn-media-1.freecodecamp.org/images/yG56kVIY4ByfAtnVf0fyvXBUAe5FkkKoHUA9)

Voyez comment l'accolade à la ligne 11 est alignée avec le côté gauche de la ligne 1 où se trouve son accolade ouvrante. De même, la ligne 4 s'aligne avec la ligne 8 et la ligne 5 s'aligne avec la ligne 7.

Lorsque l'indentation est appliquée correctement, elle devrait donner à votre code une structure propre, en forme de pyramide. Cela rendra beaucoup plus facile la détection de la fin et du début de chaque bloc de code. De plus, les accolades manquantes seront maintenant beaucoup plus faciles à repérer que si elles étaient dispersées sur toute la page.

### Faites attention à la coloration syntaxique

Un éditeur de texte moderne, tel que Sublime ou Visual Studio Code, mettra en évidence votre code.

![Image](https://cdn-media-1.freecodecamp.org/images/SJA91kb2XkblOkiNIIuqkFqvyzTlJXWX3Q8V)

Voyez comment les accolades, le nom de la balise, le nom de l'attribut et la valeur de l'attribut sont chacun mis en évidence avec la même couleur ?

Maintenant, regardez le code ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/nyAcvhPoWb38HWWg7XTTgHpCfgS5HHdrtctq)

Voyez comment la belle coloration cohérente a soudainement changé ? Le texte orange, qui est utilisé pour dénoter la valeur de l'attribut, a débordé sur les quelques lignes suivantes. C'est un indice massif que quelque chose ne va pas dans notre code. Dans cet exemple, c'est parce que nous avons oublié les guillemets fermants sur la valeur de l'attribut `href`. Repérer une erreur comme celle-ci sans la coloration syntaxique serait très difficile et chronophage.

Les développeurs peuvent facilement perdre des jours à essayer de traquer une erreur subtile comme celle-ci. Faites attention à la coloration syntaxique pour vous aider à repérer des bugs comme celui-ci.

### Le succès viendra de lui-même

Être un bon développeur est la somme de l'attention aux détails et de dizaines d'habitudes.

En faisant attention à des petites choses comme l'indentation, vous développerez une appréciation pour la structure et la portée. Réfléchir soigneusement aux noms des fonctions et des variables vous aidera à comprendre leur but et comment les accomplir au mieux. La coloration syntaxique vous aidera à repérer et à corriger une faute de frappe avant qu'elle ne devienne un bug. Taper tout le code en entier est la première étape pour développer une familiarité avec la syntaxe, ce qui à son tour mènera à une compréhension de la manière dont le code se comporte.

Tous ces petits détails qui, au premier abord, semblent insignifiants, formeront, avec la pratique, la fondation de votre expertise. Faites attention à bien maîtriser ces détails, et le succès viendra de lui-même.

Dmitri Grabov est le fondateur de [Constructor Labs](http://constructorlabs.com) qui organise un bootcamp de développement web JavaScript de 12 semaines à Londres. La prochaine classe commence le 29 mai et les frais sont de £3,000. [Les candidatures sont ouvertes maintenant](http://constructorlabs.com/admission) et les places seront attribuées selon le principe du premier arrivé, premier servi.