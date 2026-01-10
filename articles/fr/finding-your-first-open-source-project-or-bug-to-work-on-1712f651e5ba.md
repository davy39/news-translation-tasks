---
title: Comment trouver votre premier bug open source à corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-21T19:52:17.000Z'
originalURL: https://freecodecamp.org/news/finding-your-first-open-source-project-or-bug-to-work-on-1712f651e5ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qaM9LjB9PY5pwj9RDtP93g.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Mozilla
  slug: mozilla
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment trouver votre premier bug open source à corriger
seo_desc: 'By Shubheksha Jalan

  When you’re new to open source, you’ll find yourself asking:


  I know some [programming language]. I want to get some practice, while helping out.
  How do I find an open source project where I can contribute? Hm… I don’t know where
  ...'
---

Par Shubheksha Jalan

Lorsque vous êtes nouveau dans l'open source, vous vous retrouverez à vous demander :

> Je connais un [langage de programmation]. Je veux m'entraîner tout en aidant. Comment trouver un projet open source où je peux contribuer ? Hmm… Je ne sais pas par où commencer. Cela semble compliqué.

J'ai posé cette même question à de nombreux développeurs. Et leurs réponses peuvent être catégorisées en trois approches :

#### Approche #1 : Contribuer à quelque chose que vous aimez

La réponse la plus courante que je reçois est de contribuer à quelque chose que vous utilisez déjà tous les jours. Quelque chose qui vous intéresse.

#### Approche #2 : Chercher spécifiquement des projets adaptés aux débutants

Voici quelques caractéristiques des projets open source adaptés aux débutants :

* Des directives de contribution bien définies et détaillées qui incluent la configuration de leur projet localement, leur flux de travail Git et leurs directives de style de codage
* Une classification appropriée des problèmes à l'aide d'étiquettes comme « good-first-bug », « beginner » ou « first-timers-only »
* De l'activité sur ces problèmes pour débutants, avec des questions précédentes répondues rapidement

#### Approche #3 : Arrêter de chercher des projets et commencer à chercher des bugs.

C'est l'approche que j'ai choisie, et le sujet de cet article.

Après avoir essayé les approches #1 et #2, j'ai arrêté de penser en termes de projets. Je me suis concentré sur la recherche de bugs que je pensais pouvoir corriger.

Chaque bug est associé à un projet, donc en trouvant des bugs, vous découvrirez inévitablement des projets, de toute façon.

Cette approche fonctionne si vous voulez commencer immédiatement. Je ne peux pas garantir que cela vous inspirera à rester avec un projet après vos premières contributions. Peut-être que vous ne serez pas intéressé après tout. Mais peut-être que vous plongerez dans le projet et découvrirez que vous l'aimez vraiment.

Dans les deux cas, une fois que vous aurez corrigé quelques bugs, vous aurez la confiance nécessaire pour vous aventurer et explorer davantage par vous-même.

![Image](https://cdn-media-1.freecodecamp.org/images/T569nvzr6doVKxOKYuifqlkD8eGCAGrgtRwh)

### Alors, comment trouver les bugs pour commencer ?

Décider quels bugs travailler n'est pas facile. Il y a une tonne de projets là-bas, et chacun a beaucoup de problèmes ouverts. Mais vous devez commencer quelque part.

Je vais donc partager toutes les ressources et conseils que j'ai utilisés pour trouver des bugs. D'abord, je me concentrerai sur la recherche de bons bugs de démarrage en général dans divers suiveurs de bugs et sites d'hébergement de code. Ensuite, je partagerai quelques ressources spécifiques à l'écosystème Mozilla, où j'ai [contribué régulièrement](https://www.freecodecamp.org/news/a-beginners-very-bumpy-journey-through-the-world-of-open-source-4d108d540b39).

#### Trouver de bons bugs pour les débutants

Un bon endroit pour commencer votre chasse aux bugs est [Up For Grabs](http://up-for-grabs.net/#/). Le but du site est d'aider les nouveaux contributeurs à se familiariser en maintenant une liste de projets avec des problèmes adaptés aux débutants. C'est un excellent endroit pour commencer si vous vous sentez complètement perdu.

GitHub dispose d'un [moteur de recherche puissant](https://help.github.com/articles/searching-github/) où vous pouvez personnaliser votre recherche de diverses manières. La manière la plus simple de rechercher est [par étiquette de problème](https://help.github.com/articles/searching-issues/).

De nombreux projets open source étiquetent leurs problèmes pour les suivre facilement. De nombreux projets utilisent des étiquettes comme [beginner](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22beginner%22&type=Issues&ref=searchresults), [easy](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22easy%22&type=Issues&ref=searchresults), [starter](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22starter%22&type=Issues&ref=searchresults), [good first bug](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22good+first+bug%22&type=Issues&ref=searchresults), [low hanging fruit](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22low+hanging+fruit%22&type=Issues&ref=searchresults), [bitesize](https://github.com/search?utf8=&q=is%3Aissue+is%3Aopen+label%3A%22bitesize%22+&type=Issues&ref=searchresults), [trivial](https://github.com/search?utf8=&q=is%3Aissue+is%3Aopen+label%3A%22trivial%22+&type=Issues&ref=searchresults), [easy fix](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22easy+fix%22+&type=Issues&ref=searchresults), et [new contributor](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22new+contributor%22+&type=Issues&ref=searchresults).

Vous pouvez affiner davantage votre recherche en fonction du langage de programmation avec lequel vous êtes à l'aise, en ajoutant _language: name_ à votre requête de recherche. Par exemple, voici tous les problèmes [étiquetés comme « beginner » en JavaScript](https://github.com/search?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3A%22beginner%22+language%3Ajavascript).

[Issuehub.io](http://issuehub.io) est un outil pour rechercher des problèmes par étiquette et langage, au cas où vous trouvez fastidieux de vous souvenir de la syntaxe de recherche GitHub.

Si vous êtes complètement nouveau dans l'open source, vous devriez définitivement commencer par [First Timers Only](http://www.firsttimersonly.com/). C'est une initiative de [Kent C. Dodds](https://kentcdodds.com/), basée sur son propre article [First Timers Only](https://medium.com/@kentcdodds/first-timers-only-78281ea47455) et [Scott Hanselman](https://www.hanselman.com/)s [Bring Kindness Back to Open Source](http://www.hanselman.com/blog/BringKindnessBackToOpenSource.aspx). Les bugs sont étiquetés [first-timers-only](https://github.com/search?q=label%3Afirst-timers-only&state=open&type=Issues).

Vous pourriez également trouver ce [bot Twitter](https://twitter.com/first_tmrs_only) utile. Il tweete tous les problèmes étiquetés comme « first-timers-only ».

Une autre excellente façon de trouver des problèmes est [YourFirstPR](https://twitter.com/yourfirstpr) par Charlotte Spencer. Ils mettent en avant des problèmes de démarrage sur GitHub qui peuvent être facilement résolus par de nouveaux contributeurs.

[Awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) est un dépôt GitHub qui rassemble des projets avec de bons bugs pour les nouveaux contributeurs, et applique des étiquettes pour les décrire.

[Openhatch](https://openhatch.org/) est une organisation à but non lucratif qui aide à réduire les barrières d'entrée dans l'open source. Vous pouvez trouver des bugs et des projets ici, également.

### L'écosystème des contributeurs Mozilla

De nombreux projets de Mozilla sont hébergés sur [GitHub](https://github.com/mozilla/). Pour ces projets, tout ce que j'ai listé ci-dessus est toujours utile. Ils utilisent l'étiquette « good first bug » pour les problèmes de démarrage.

Mais Mozilla utilise également son propre outil appelé [Bugzilla](https://bugzilla.mozilla.org/) comme suiveur de problèmes principal. Ils hébergent certains de leurs problèmes [ici](https://hg.mozilla.org/), et utilisent [Mercurial pour le contrôle de version au lieu de Git](https://mozilla-version-control-tools.readthedocs.io/).

Firefox est l'un des projets qui utilise Bugzilla et Mercurial. C'est un peu effrayant, pour être honnête. C'est beaucoup à assimiler. Je recommande donc cet [excellent article de blog et vidéo](http://blog.johnath.com/2010/02/04/bugzilla-for-humans/), qui fait un excellent travail pour démystifier ces outils.

Au fil des ans, les Mozilliens ont essayé de rendre la contribution à Mozilla aussi simple que possible. Voici leurs efforts :

* [Good First Bugs](https://bugzil.la/sw:%22[good%20first%20bug]%22&limit=0) : Ce sont des bugs que les développeurs ont identifiés comme une bonne introduction au projet. Ils sont souvent (mais pas toujours) relativement faciles à résoudre.
* [Mentored Bugs](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=mentor%3A%40) : Ces bugs ont un mentor assigné qui sera là sur IRC pour vous aider lorsque vous serez bloqué en travaillant sur la correction. Ils examinent souvent votre patch et donnent des commentaires. Si vous ne savez pas par où commencer pour contribuer aux projets Mozilla, c'est le meilleur endroit pour commencer. Vous aurez quelqu'un qui peut répondre à vos questions lorsque vous sentirez que vous avez atteint un mur. Tous les mentors avec lesquels j'ai travaillé ont été très réactifs, soutenants et utiles tout au long.
* [Bugs Ahoy](http://www.joshmatthews.net/bugsahoy/) : Ce site est dédié à la recherche de bugs sur Bugzilla. Il a une interface conviviale, où vous pouvez filtrer par langage.
* [Firefox DevTools](http://firefox-dev.tools/) : Ce site est dédié aux bugs signalés pour les outils de développement dans le navigateur Firefox. Vous pouvez trier en fonction des composants DevTools sur lesquels vous souhaitez travailler.
* [What Can I Do For Mozilla](http://whatcanidoformozilla.org/) — C'est une excellente façon d'explorer et de déterminer ce que vous pouvez faire en répondant à une série de questions sur vos compétences et vos intérêts.
* [Start Mozilla](https://twitter.com/StartMozilla) : C'est un compte Twitter qui tweete sur les problèmes adaptés aux contributeurs nouveaux dans l'écosystème Mozilla.

Si vous connaissez d'autres ressources pour trouver de bons bugs pour les nouveaux contributeurs, faites-le moi savoir dans les commentaires. Je serai plus qu'heureux d'étendre cette liste.

*Si vous pensez que cet article était utile, tapez sur le « _ » pour aider à promouvoir cet article auprès des autres.*

![Image](https://cdn-media-1.freecodecamp.org/images/U17yyZz83IpV7YtRNbylUoc2Ae87AdZ3TYZW)