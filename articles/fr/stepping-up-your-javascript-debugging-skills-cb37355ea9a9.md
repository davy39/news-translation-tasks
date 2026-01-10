---
title: Comment améliorer vos compétences en débogage JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-25T18:01:01.000Z'
originalURL: https://freecodecamp.org/news/stepping-up-your-javascript-debugging-skills-cb37355ea9a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e3eGMlHCBdhS6Sv9rlEJXg.png
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment améliorer vos compétences en débogage JavaScript
seo_desc: 'By Periklis Gkolias

  Almost all software developers who have written even a few lines of code for the
  Web have had at least a quick glance at JavaScript. After all, it is currently one
  of the most in-demand programming languages.

  Some people love it, ...'
---

Par Periklis Gkolias

Presque tous les développeurs de logiciels qui ont écrit même quelques lignes de code pour le Web ont jeté au moins un coup d'œil rapide à JavaScript. Après tout, il est actuellement l'un des langages de programmation les plus [demandés](https://www.codingdojo.com/blog/7-most-in-demand-programming-languages-of-2018/).

Certains l'[adorent](https://dev.to/gentlemanoi/why-i-love-javascript-9bg), d'autres le [détestent](https://www.reddit.com/r/webdev/comments/4jf7m0/why_is_javascript_used_extensively_and_hated_at/). Peu importe votre avis, si vous l'utilisez, vous devrez éventuellement le déboguer.

![Image](https://cdn-media-1.freecodecamp.org/images/LrFIEQsO8MyJhwmLvB5Gb2TDaV9EYOW8gqfx)
_Crédits à reddit_

Ci-dessous, je vais partager quelques conseils qui m'ont aidé dans des moments difficiles.

### Les bases / les plus connues

#### Le débogage avec un canard en plastique

Le [débogage avec un canard en plastique](https://en.wikipedia.org/wiki/Rubber_duck_debugging) est une méthode où vous expliquez votre problème à n'importe qui ou n'importe quoi (ce n'a pas besoin d'être un humain). Ensuite, la solution arrête magiquement de jouer avec votre bonne volonté et apparaît devant vous.

Le « canard » n'a aucune connaissance de votre projet, donc vous expliquez tout, en remettant en question vos hypothèses en même temps. Idéalement, vous aurez soudainement une illumination comme, « Oh, c'était devant moi, merci mon pote, désolé pour l'interruption. »

Pourtant, le canard est resté silencieux tout ce temps, et c'est la partie magique. :)

#### Le bon vieux logging

Lorsque vous avez un problème à déboguer, vous avez généralement une hypothèse vague de ce qui pourrait ne pas aller. Cela pourrait être totalement éloigné de la cause réelle, mais c'est une autre histoire. Si vous commencez à mettre des logs aux endroits où l'erreur pourrait se produire, vous pourriez arriver au point rapidement.

Même si ce n'est pas le cas, ne supprimez pas les logs que vous avez ajoutés, car ils pourraient s'avérer utiles pour un problème futur.

Je pourrais argumenter pourquoi vous ne devriez jamais en arriver là, à ajouter des logs de débogage, car les logs devraient être là dans le cadre du développement initial. Mais [Erik Hazard](http://vasir.net/blog/programming/how-logging-made-me-a-better-developer) a déjà fait le travail.

Plus sur le logging plus tard.

#### Les points d'arrêt

Un débogueur est un excellent outil dans votre arsenal et une grande aide — si **vous savez comment l'utiliser**.

Cela signifie :

* D'abord, comprendre le problème
* Ensuite, faire quelques hypothèses sur la **cause racine (et non le symptôme)**
* Définir les points d'arrêt appropriés pour les vérifier ou les infirmer.

En JavaScript, vous pouvez soit définir dans l'outil de développement du navigateur, soit utiliser le mot-clé `debugger` dans le code pour forcer la pause de l'exécution.

Donc, ne mettez pas simplement des points d'arrêt aléatoires ici et là. Ayez une routine et une « fin » en tête lorsque vous l'utilisez.

### Les moins connues

#### console.table

Quelques lignes plus haut, nous avons parlé de l'importance du logging. La commande que nous utilisons habituellement est `console.log('texte')`. Mais que faire si la sortie est plus complexe ? Oui, `console.log` gère aussi les tableaux. Et les objets.

Mais que se passerait-il si je vous disais que vous pourriez repérer l'erreur plus rapidement grâce à une certaine... beauté ? Ce serait la méthode `console.table` et elle est démontrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/-Ek-xKZX9Bw75cKgaNGvNRQHrmWgqoQ46XKb)
_console.table à son meilleur_

Voyez comme vous pouvez obtenir un bel aperçu de la disposition ? Je vous encourage vivement à l'utiliser davantage, surtout avec les itérables.

#### Points d'arrêt sur les événements au lieu des lignes

Imaginons le scénario suivant. Un élément DOM change de manière intermittente et avec de mauvaises valeurs, et vous n'avez aucune idée pourquoi. Laquelle des 29 fonctions qui le mutent est malveillante ? (Note à part : La mutation est généralement [mauvaise](https://slemgrim.com/mutate-or-not-to-mutate/), mais c'est un sujet pour un autre article.)

Utilisez les **points d'arrêt de changement de DOM**. Chaque fois que l'élément est muté, une trace de pile sera affichée. Tout comme si vous aviez mis les bons points d'arrêt. Vous pouvez trouver plus de détails [ici](https://developers.google.com/web/tools/chrome-devtools/javascript/breakpoints#dom).

#### Profiling

Si le bug sur lequel vous travaillez n'est pas orienté performance, peut-être que c'est trop. Mais je dois quand même en parler (et bien, cela pourrait être un problème de performance après tout :) ). Dans [Chrome](https://developers.google.com/web/tools/chrome-devtools/rendering-tools/js-execution) et [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Performance/Profiling_with_the_Built-in_Profiler), vous pouvez utiliser la fonctionnalité intégrée du profileur pour repérer un goulot d'étranglement ou simplement... voir les fonctions qui sont exécutées. Boom :). Du suringénierie à son meilleur. Veuillez utiliser cette fonctionnalité [sagement](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/). Tuer une mouche avec un [bazooka](https://answers.yahoo.com/question/index?qid=20111106222906AAUSWkm) peut avoir des effets secondaires étranges.

### Conclusion

Merci d'avoir lu cet article. J'espère que vous l'avez apprécié et que vous avez appris quelque chose aujourd'hui. Comme toujours, je vous encourage vivement à partager vos techniques magiques dans les commentaires.

### Plus de lectures

Outre les liens cités dans le texte principal de l'article, voici quelques autres choses que je pense valoir la peine de lire sur le sujet du débogage :

* [Tutoriel de débogage Node](https://nodejs.org/en/docs/guides/debugging-getting-started/)
* [Guide de débogage de John Sonmez](https://simpleprogrammer.com/effective-debugging/)
* [Debug it](https://amzn.to/2lC7kD3)
* [Débogage : Les 9 règles indispensables pour trouver même les problèmes logiciels et matériels les plus insaisissables](https://amzn.to/2IrgI5t)
* [Outils de débogage Chrome](https://developers.google.com/web/tools/chrome-devtools/javascript/)
* [Outils de débogage Firefox](https://developer.mozilla.org/en-US/docs/Tools/Debugger)
* Podcast 'JSparty' et surtout [épisode 30](https://overcast.fm/+Id5XDQtKY) d'où je me suis inspiré pour ce post et où j'ai appris à propos de `console.table`

Publié à l'origine [sur mon blog](http://perigk.github.io).