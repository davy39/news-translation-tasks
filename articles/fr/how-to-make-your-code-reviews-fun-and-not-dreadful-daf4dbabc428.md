---
title: Comment rendre vos revues de code amusantes (et non redoutables)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T21:31:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-code-reviews-fun-and-not-dreadful-daf4dbabc428
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ypd0z4OhOmegm-WHyGHgxg.jpeg
tags:
- name: code review
  slug: code-review
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: workflow
  slug: workflow
seo_title: Comment rendre vos revues de code amusantes (et non redoutables)
seo_desc: 'By Eumir Gaspar

  I’ve done my fair share of code reviews. By fair share, I mean a lot. Have you ever
  done a code review of an epic feature? I have. It was not a great experience, because
  by the time the 100th file was to be reviewed, I was already fat...'
---

Par Eumir Gaspar

J'ai fait ma part de revues de code. Par part équitable, je veux dire beaucoup. Avez-vous déjà fait une revue de code d'une fonctionnalité épique ? Moi oui. Ce n'était pas une grande expérience, car au moment où le 100ème fichier devait être examiné, j'étais déjà fatigué de regarder du code. J'étais sur le point de simplement dire « Oui, ça a l'air bien pour moi » et de donner mon approbation.

Mais ce n'est pas ainsi que fonctionnent les revues de code. Une fois que vous avez commencé, vous devez vous y tenir et le terminer jusqu'à la fin. Bien sûr, vous pouvez prendre des pauses, mais ensuite vous commencez à perdre le contexte et devez tout recommencer, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Ck2NsPyZNpjQBRFLQWbadZTPrPhDcpRlsHmf)
_[Bande dessinée par Jason Heeris](http://heeris.id.au/2013/this-is-why-you-shouldnt-interrupt-a-programmer/" rel="noopener" target="_blank" title=")_

Je m'égare, cependant. La douleur n'est pas ce dont je suis censé parler.

Alors, comment faire pour que ce soit, disons, moins redoutable ? Tout d'abord, même avant de faire la demande de tirage (pull request), et même avant de commencer à coder, nous devrions faire en sorte de décomposer les fonctionnalités en petits morceaux. Le développement et les déploiements deviennent plus rapides, car il est toujours plus facile de déployer une mini-fonctionnalité qu'une fonctionnalité épique. Cela rend les revues de code plus faciles et plus rapides à effectuer puisque les changements sont assez petits.

Super ! J'espère que vous avez aimé mon article. Rentrons tous à la maison...

Attendez, **stop** !

C'était sur la façon de le rendre moins redoutable, mais comment le rendre amusant ?

### Utiliser des memes dans les revues de code

_Avertissement : ce qui suit sont mes propres pensées et non celles de mon employeur._

Je voulais simplement clarifier cela, car cela peut potentiellement être un sujet controversé. Quoi qu'il en soit, nous rendons nos revues de code légères en ajoutant des [memes](http://knowyourmeme.com/memes/memes).

Je peux entendre vos yeux rouler d'ici ! Écoutez-moi quand même. [Quelle meilleure explication que de lier à quelqu'un d'autre qui l'a déjà expliqué avec plaisir](https://medium.com/@adamkoszary/look-at-this-absolute-unit-763207207917) ?

C'est le ton qui aide à rendre cela amusant pour à la fois le réviseur et la personne dont le code est examiné. Un exemple serait le tout premier « staple » dans mon `portefeuille d'images`. J'ai remarqué que [Rubocop](https://github.com/bbatsov/rubocop) manquait certains doubles espaces dans nos fichiers, donc quand quelqu'un a soumis une pull request avec un tas d'espaces blancs supplémentaires, c'était une évidence de leur donner un [doge](http://knowyourmeme.com/memes/doge).

![Image](https://cdn-media-1.freecodecamp.org/images/nUXPIWCWtNzEIkdH5dS1SlOncwX-6gBtsJPD)
_wow. beaucoup d'espaces blancs. telles ruptures de ligne._

C'était une simple image, et pourtant le message était très efficace. Je me souviens des gens riant quand ils l'ont vue. Les gens ne voulaient pas se faire « doger » donc tout le monde était plus vigilant quant à leurs espaces blancs supplémentaires.

C'était plus facile d'ouvrir le finder, de glisser le doge dans un commentaire, et de poster, au lieu de simplement taper le vieux « Veuillez supprimer les espaces blancs supplémentaires » dans la pull request (PR), surtout s'il y avait plusieurs doges.

### Cela ne pourrait-il pas se retourner contre nous ?

Cela pourrait tout à fait se retourner contre nous. Je ne dis pas que tout le monde devrait suivre notre équipe. Cela dépend vraiment de la personnalité de l'équipe. La nôtre a un âge moyen de six ans de moins que moi, ce qui signifie que la plupart peuvent s'identifier aux memes. Ce serait une histoire différente si votre équipe avait un âge moyen de quarante ans (sauf bien sûr, s'ils étaient des habitués de 4chan ou à jour avec les derniers memes !).

Vous connaissez vos coéquipiers mieux que quiconque, vraiment. Après quelques mois passés ensemble (surtout puisque nous faisions du pair programming presque 100 % du temps), nous avions une idée de l'humour de chacun, pour ainsi dire. Cela nous a rendu à l'aise de voir des memes dans nos PR et de simplement en rire (tout en corrigeant le problème, bien sûr).

### Quels avantages tirez-vous des memes ?

Eh bien, un avantage est que cela rend la revue plus rapide (au moins pour moi). La personne qui a également soumis la PR comprend en fait plus rapidement ce qu'elle doit faire. Au lieu de lire quelques mots, vous voyez une image — et nous savons tous que les images parlent plus fort que les mots. Voici quelques exemples de mon `portefeuille d'images personnel™` :

![Image](https://cdn-media-1.freecodecamp.org/images/tuGwZyZ1KP1QO56Z8-iljQ007ufkOL9CH1Dw)
_Supprimez cette ligne !_

Quand j'utilise une image pour la première fois, j'ajoute une description/explication sur ce qu'ils doivent faire/corriger. Le ci-dessus dit simplement de supprimer le code « hérité » ci-dessus. Supprimez-le. Détruisez-le !

![Image](https://cdn-media-1.freecodecamp.org/images/14sYrRTvkQ9BvRGHs5tuzXnjREEkGbGVlsjH)
_Mmmmm pretzels_

Cela est spécifique à Ruby - l'opérateur `[pretzel dot](http://mitrev.net/ruby/2015/11/13/the-operator-in-ruby/)` est essentiellement un raccourci pour un `try-catch`. Je surligne simplement le snippet qui a besoin d'un pretzel et colle cette image. Rapide et facile !

![Image](https://cdn-media-1.freecodecamp.org/images/qwqPKNzCHncJC19pqxJBbTXM5VQHkiMG4HdF)
_AH-AH-AH !_

![Image](https://cdn-media-1.freecodecamp.org/images/jvIFwOePL9nOau1UebnU77DdUKD6o9aH83SD)
_Cela me dérange vraiment (le froid)_

Ces deux-là, je les utilise de manière interchangeable et encore, PRINCIPALEMENT en Ruby où nous ajoutons toujours le commentaire magique `# frozen_string_literal: true` en haut du fichier. Avec [Rubocop](https://github.com/bbatsov/rubocop) à la barre, cependant, nous avons vu de moins en moins d'Elsa et de Mr. Freeze. Ils apparaissent également pour toute constante qui doit être gelée.

![Image](https://cdn-media-1.freecodecamp.org/images/-XyiIVBrpiNFAIK7GWNWqoJA3G0u5alKu4yJ)
_J'adore ce GIF_

Cela est assez simple (je l'espère). Quand les collègues voient cela, c'est un signe qu'ils ont fait une faute de frappe. Je surligne généralement la faute de frappe également pour que ce soit rapide et facile à voir (et à corriger).

Ce ne sont que quelques exemples. Souvenez-vous cependant, trop de quelque chose est **généralement** une mauvaise chose. Alors faites simplement attention lorsque vous ajoutez vos memes. Il est également préférable de ne pas ajouter trop de memes, car parfois cela peut être distractif. Trouver le bon équilibre de ton et simplement envoyer le message le plus rapidement possible est la meilleure façon de conclure une pull request.

### C'est tout, les amis

En conclusion, cela dépend vraiment de vous si vous voulez vous amuser, ou rester sérieux et professionnel au travail. Certains peuvent penser que les memes sont peu professionnels — et oui, dans les choses formelles de travail, ils peuvent l'être. On peut argumenter qu'une pull request peut être ou est une chose liée au travail formel, mais je pense que cela ne s'applique que si vous l'utilisez pour la documentation ou les revues. Sinon, je pense que c'est de la « liberté d'expression » (oui, j'ai sorti cette carte !) et devrait simplement être pris comme tel.

Pour moi, cela transmet ce que je veux dire : supprimer les espaces blancs supplémentaires, corriger l'orthographe, geler une constante, ou supprimer une ligne ou des lignes de code. Je n'ai pas à taper beaucoup, mon collègue n'a pas à lire un tas de mots contre un autre tas de mots, et cela allège un peu l'ambiance. Tout le monde gagne ! Avec cela, je vais terminer cela avec une autre de mes images :

![Image](https://cdn-media-1.freecodecamp.org/images/JTYj7y9qsEpADLb-u20Z7dagkFmAO2KgIuA8)
_JE ME DEMANDE_