---
title: Choses que tous les développeurs devraient apprendre à l'université
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T15:47:35.000Z'
originalURL: https://freecodecamp.org/news/things-all-developers-should-learn-in-college
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca173740569d1a4ca4ea7.jpg
tags:
- name: beginner
  slug: beginner
- name: College
  slug: college
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Choses que tous les développeurs devraient apprendre à l'université
seo_desc: "By Ryland Goldstein\nForget About \"Lines of Code\"\n\n               \
  \                                                     Source\nAs a developer, you'll\
  \ hear a lot of crazy, unbelievable theories about what \"lines of code\" signify.\
  \ Believe none of them. L..."
---

Par Ryland Goldstein

## Oubliez les "lignes de code"

![Image](https://thepracticaldev.s3.amazonaws.com/i/vmbqyj278qt930ua7lxk.jpg)

																	[Source](https://images.techhive.com/images/article/2015/09/historic_loc-chart-100615917-large.idge.jpg)

En tant que développeur, vous entendrez beaucoup de théories folles et incroyables sur ce que signifient les "lignes de code". Ne les croyez pas. Les lignes de code sont une métrique ridicule pour baser des décisions. Dans de très rares cas, elles vous disent quelque chose, dans tous les autres cas, elles ne vous disent rien. Utiliser les lignes de code pour prendre des décisions, c'est comme évaluer la qualité d'un livre par le nombre de pages.

Certains pourraient soutenir que moins il y a de lignes de code dans une application, plus elle est facile à lire. Cela n'est que partiellement vrai. Mes critères pour un code lisible sont :

* Le code doit être cohérent
* Le code doit être auto-descriptif
* Le code doit être bien documenté
* Le code doit utiliser des fonctionnalités modernes stables
* Le code ne doit pas être inutilement complexe
* Le code ne doit pas être non performant (n'écrivez pas intentionnellement du code lent)

Dès que la réduction du nombre de lignes de code interfère avec l'un de ces critères, cela devient un problème. En pratique, cela interférera presque toujours et est donc presque toujours un problème. Mais voici le point, si vous vous efforcez de répondre aux critères ci-dessus, votre code aura le nombre parfait de lignes, **pas besoin de compter.**

## Il n'y a pas de langages "bons" ou "mauvais"

![détesté](https://thepracticaldev.s3.amazonaws.com/i/30fmha6zyrtfrt1a80i1.png)

														__														[_Sauf pour php, je plaisante_](https://stackoverflow.blog/wp-content/uploads/2017/10/languages-1-900x675.png)

Je vois des gens dire des choses comme ça, tout le temps :

> C est mieux que X, parce que performance

|

> Python est mieux que X, parce que concision

|

> Haskell est mieux que X, parce que les aliens

L'idée qu'une comparaison de langages puisse être réduite à une seule phrase est presque insultante. Ce sont des langages, pas des Pokémon.

Ne vous méprenez pas, il y a définitivement des différences entre les langages. C'est juste que, il y a très peu de langages "inutilisables" (bien qu'il y ait beaucoup de langages obsolètes/morts). Chaque langage apporte son propre ensemble unique de compromis. À cet égard, les langages sont similaires aux outils dans une boîte à outils. Un tournevis peut faire ce qu'un marteau ne peut pas, mais diriez-vous jamais qu'un tournevis est meilleur qu'un marteau ?

Évidemment, le marteau est meilleur

Avant de parler de la façon dont j'évalue les langages, je veux clarifier quelque chose. **Il y a très peu de cas où le choix du langage compte réellement.** Il y a des choses que vous ne pouvez évidemment pas faire dans certains langages. Si vous écrivez du code frontend, vous n'avez pas le choix du langage. Mais en général, le choix du langage est généralement l'un des problèmes les moins importants pour un projet.

Voici les aspects principaux (ordonnés), que je crois devraient dicter votre choix de langage (ce sont ses statistiques Pokémon) :

* Densité des ressources en ligne disponibles (Densité StackOverflow)
* Vélocité de développement (vroom vroom)
* Propension aux bugs (eeek)
* Qualité et étendue de l'écosystème de paquets (oui npm, il dit qualité)
* Caractéristiques de performance (plus de points)
* Embauchabilité (désolé COBOL)

Il y a aussi quelques couplages forts qui ne dépendent pas de vous. Si vous travaillez dans la science des données, vous devez réalistement utiliser Python, R ou Scala (peut-être Java). Si c'est un projet de loisir, utilisez ce qui vous rendra le plus heureux. Il n'y a qu'une seule règle non négociable que j'ai. Je refuse d'utiliser des langages qui n'ont pas la plupart des problèmes que je rencontrerai, directement résolus sur StackOverflow. Ce n'est pas que je ne puisse pas les résoudre, c'est juste que cela ne vaut pas le temps.

## Lire le code des autres est difficile

![lecture difficile](https://thepracticaldev.s3.amazonaws.com/i/5zog7djn2ajgazwyrliy.jpg)

																	[Source](http://www.sph.as/why-bible-reading-can-be-hard-for-kids-and-what-to-do-about-it/)

Lire le code des autres est difficile. Robert C. Martin en parle dans "Clean Code" :

En effet, le ratio de temps passé à lire par rapport à écrire est bien supérieur à 10 contre 1. Nous lisons constamment du vieux code dans le cadre de l'effort pour écrire du nouveau code. ...[Par conséquent,] le rendre facile à lire le rend plus facile à écrire.

Pendant longtemps, j'ai supposé que je n'étais simplement pas doué pour lire le code des autres. Avec le temps, j'ai réalisé que c'est quelque chose avec lequel presque tous les programmeurs luttent au quotidien. Lire le code des autres ressemble presque à lire une langue étrangère. Même si vous êtes à l'aise avec le choix du langage de programmation de l'auteur, vous devez toujours vous adapter à des styles et des choix d'architecture différents. Cela suppose également que l'auteur a écrit un code cohérent et fiable, ce qui peut être aléatoire. C'est un point vraiment difficile à surmonter. Il y a quelques choses que j'ai trouvées qui aident énormément.

Revoir le code des autres améliorera considérablement vos compétences en lecture de code. Au cours des deux dernières années, j'ai examiné assez quelques PR Github. Avec chaque PR, je me sens légèrement plus à l'aise pour lire le code des autres. Les PR Github sont particulièrement excellents pour ces raisons :

* Peut être pratiqué à tout moment, il suffit de trouver un projet open source auquel vous souhaitez contribuer.
* Pratique de la lecture dans un contexte limité (fonctionnalité ou bug du PR).
* Attention aux détails requise, ce qui vous forcera à évaluer chaque ligne.

Le second truc qui peut vous aider à lire le code des autres est un peu plus unique. C'est une technique que j'ai inventée, et elle a vraiment réduit le temps qu'il me faut pour me sentir à l'aise dans une base de code étrangère. Après avoir examiné le style du code que je veux lire, j'ouvre d'abord vi et commence à écrire du code dans le style utilisé par le projet. Lorsque vous écrivez du code dans le nouveau style, cela améliorera également vos compétences en lecture. Le style vous semblera moins étranger, car vous l'aurez réellement expérimenté. Même si je navigue simplement dans un projet aléatoire sur Github, je ferai rapidement cela. Essayez-le.

## Vous n'écrirez jamais de code "parfait"

![parfait](https://thepracticaldev.s3.amazonaws.com/i/8y29au7wj8vkgf6ed5kx.jpg)

																	[Source](https://www.youtube.com/watch?v=WPoQfKQlOjg)

J'ai été un développeur "loup solitaire" pendant 4 ans avant de commencer à travailler en équipe. Pendant la majeure partie de cette période, j'avais simplement cette supposition que chaque programmeur de l'industrie écrivait du code parfait. Je pensais que c'était juste une question de temps et d'efforts avant que je n'écrive également du code "parfait". 
C'était quelque chose qui me rendait vraiment anxieux. Une fois que j'ai rejoint une équipe, il est rapidement devenu clair que personne n'écrivait de code "parfait". Mais le code entrant dans le système était presque toujours "parfait", qu'est-ce qui donne ? La réponse, les revues de code.

Je travaille avec une équipe d'ingénieurs vraiment brillants. Ce sont certains des programmeurs les plus compétents et confiants que l'argent peut acheter. Chaque membre de notre équipe (y compris moi) aurait une crise de panique totale si quelqu'un suggérait jamais de commiter du code non révisé. Même si vous pensez être le prochain Bill Gates, vous ferez des erreurs. Je ne parle même pas d'erreurs logiques, je parle de fautes de frappe, de caractères manquants. Des choses que votre cerveau ignore et que vous ne remarquerez jamais. Des choses pour lesquelles vous avez besoin d'une autre paire d'yeux.

Efforcez-vous de travailler avec des personnes attentives aux détails et prêtes à critiquer votre travail. Entendre des critiques est difficile au début, mais c'est le seul moyen constant de s'améliorer. Faites de votre mieux pour ne pas devenir défensif lors d'une revue de code, et ne prenez jamais les commentaires personnellement. Vous n'êtes pas votre code.

Lorsque je révise le code de quelqu'un d'autre, je fais simplement une recherche Google pour chaque choix qu'il fait et je vois s'il diffère de l'opinion populaire forte. Souvent, regarder le même problème avec un "esprit de débutant" peut attraper des choses que la personne n'aurait jamais revisitées.

## Travailler en tant que programmeur ne signifie pas 8 heures de programmation par jour

C'est une question très courante, mais les gens ne semblent jamais donner de réponse claire.

**Très peu de gens écrivent du code pendant plus de 4 heures par jour**

Les personnes qui ne sont pas d'accord avec cela sont soit l'exception à la règle, soit travaillent dans des entreprises qui devraient mieux les traiter. La programmation est une tâche mentalement épuisante et intensive en concentration. Il est entièrement déraisonnable de s'attendre à ce que quelqu'un écrive du code pendant 8 heures par jour, 5 jours par semaine. Il y aura des cas rares où vous devrez respecter une date limite ou faire un peu plus pendant une période, mais ceux-ci sont rares et espacés. Lorsque je dis "rare", je veux dire presque jamais. Ne tolérez pas un lieu de travail qui vous abuse et vous fait faire des heures supplémentaires en raison d'une mauvaise planification/sous-embauche.

![samedi](https://thepracticaldev.s3.amazonaws.com/i/4c1ixs0f8gqksw2p7tjo.jpg)

Pour le record, ce n'est même pas dans l'intérêt de votre entreprise que vous travailliez 8 heures par jour. Votre patron pourrait penser que c'est le cas, mais c'est à courte vue et ignore les implications à long terme sur la productivité et la santé mentale.

Je recommande vivement de prendre des pauses régulières pendant la journée et de faire de l'exercice (même brièvement). Les bienfaits de l'exercice sur la fatigue mentale sont bien documentés. J'ai personnellement constaté que l'exercice aide particulièrement si j'ai du mal à me concentrer.

## Conclusion

Ce sont quelques-unes des choses que je souhaite qu'ils enseignent à l'université au lieu de la théorie pure. En écrivant ceci, j'ai pensé à une tonne d'autres éléments, mais ceux-ci devront attendre le prochain article !