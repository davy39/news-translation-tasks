---
title: Coincé dans l'enfer du code hérité ? Voici quelques pensées pour vous aider
  à gérer la situation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-04T11:57:40.000Z'
originalURL: https://freecodecamp.org/news/few-thoughts-on-legacy-hell-e229f76529e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DST6EDWapMJFwawjNykejA.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Coincé dans l'enfer du code hérité ? Voici quelques pensées pour vous aider
  à gérer la situation
seo_desc: 'By Felipe Lopes

  I’m gonna tell you a little story about how I ended up in a legacy code project
  and how our team managed to get the best from that.

  First, a little bit of context

  I’ve been working for almost a year on a project, that is quite complex...'
---

Par Felipe Lopes

Je vais vous raconter une petite histoire sur la façon dont j'ai atterri dans un projet de code hérité et comment notre équipe a réussi à en tirer le meilleur parti.

### D'abord, un peu de contexte

Je travaille depuis presque un an sur un projet, qui est assez complexe, pour dire le moins.

Alors que je passe mon temps à lire ici sur Medium toutes les choses géniales que les gens font dans le monde en ingénierie logicielle (création de grandes infrastructures, assemblage de plusieurs systèmes de pointe pour répondre à des milliers de requêtes par seconde), une partie de ma vie quotidienne en tant qu'ingénieur logiciel n'a pas été si glamour. Cela consiste à maintenir une ancienne extension pour une ancienne plateforme, en bon état de fonctionnement.

Pour le dire en anglais simple, je souffre avec le code hérité.

D'abord, laissez-moi vous parler de la pile brillante. Cette extension est destinée à fonctionner sur l'une des plateformes de commerce électronique les plus importantes, [Magento](https://magento.com/). Mais Magento a sorti une nouvelle version de la plateforme (2.0), avec de nombreuses améliorations, mettant en œuvre la plupart des bonnes pratiques que les développeurs backend espéraient voir.

Pour moi, ce serait génial si l'extension était faite pour la dernière version de Magento, mais l'extension a été développée pour la version précédente (1.9). Une version archaïque, souvent inutilement complexe, encombrante et pleine de fichiers XML intriqués. Mais elle fait le travail. Oh, oui, elle le fait !

En outre, l'extension, comme vous pouvez vous y attendre, est écrite en PHP, le langage que tout le monde aime détester.

Bien que PHP ait gagné de nombreuses améliorations avec la dernière version 7.x, Magento 1.9 ne la supporte pas et je suis obligé de travailler avec d'anciennes versions de PHP. Ainsi, je ne peux pas jouer avec toutes les nouvelles fonctionnalités. Pour finir de décrire le scénario, il n'y a pas un seul morceau de test. Ni moi, ni personne dans l'équipe, n'a fait partie de la conception et du développement originaux de l'extension. Au début, nous étions un peu perdus, la plupart du temps.

### Courir en rond et crier n'est pas une option

Lorsque vous commencez à travailler sur un projet comme celui-ci, vous vous sentez comme ces gars qui jouent la dernière chanson sur le Titanic. Tout s'effondre, mais vous continuez à faire votre travail.

Les clients continuent à ouvrir des tickets, les problèmes ne semblent jamais être résolus. Votre patron demande de nouvelles fonctionnalités. Vous commencez à blâmer la plateforme, la base de code (quelqu'un que vous ne connaissez même pas et que vous commencez à détester pour cela). À ce stade, vous êtes profondément enfoncé dans l'enfer du code hérité.

Il y a en fait deux choses que vous pouvez faire ici. La première est de mettre à jour votre profil Linkedin, de mettre une belle photo, de raconter une belle histoire sur vos compétences et de commencer à envoyer des CV. Chercher un nouvel emploi, un emploi sans code hérité (alerte spoiler, cet endroit n'existe **pas**) ou vous pouvez vous arrêter, respirer et faire un plan pour gérer cela.

### Commencez à faire quelque chose à ce sujet

![Image](https://cdn-media-1.freecodecamp.org/images/jxhrSA2A9s8felRM-frky-yPewds0lZFA3R7)
_Photo par [Unsplash](https://unsplash.com/photos/qAShc5SV83M?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Yung Chang</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Si vous êtes dans un scénario comme celui-ci, vous devriez commencer à agir rapidement. Si votre base de code n'est pas sous un système de contrôle de version (git, s'il vous plaît) et que votre équipe n'utilise pas d'outil pour gérer les tâches, peut-être devriez-vous penser à cette histoire de Linkedin. Mais si vous avez le minimum, commencez par le basique, retirez le [cruft](https://www.techopedia.com/definition/15410/cruft).

Je suis presque sûr qu'il y a du code obsolète, du code qui n'est jamais atteint, et du code qui a été laissé derrière. Cela prend juste de la place et fait paraître les choses bien pires qu'elles ne le sont en réalité. Jetez un bon coup d'œil à ce code, bricolez-le, remplissez-le de points d'arrêt et commencez à vous débarrasser de ce qui n'est pas utilisé. Assurez-vous de ne pas faire de bêtises ici et ne vous emballez pas. Rappelez-vous, il n'y a pas encore de tests, alors ne vous débarrassez que de ces méthodes dont vous êtes **complètement** sûr qu'elles sont inutiles.

En faisant cela, vous serez plus à l'aise avec votre base de code et vous vous sentirez probablement plus confiant. Après cela, vous aurez encore du code inutile, mais presque tout ce que vous avez là a un sens, ou est utile.

L'étape suivante est de penser aux tests. Il existe plusieurs façons de tester un logiciel. Vous pouvez faire des tests unitaires, des tests d'intégration, des tests système, des tests de stress, et bien d'autres. Ils sont géniaux et devraient être utilisés au bon moment. Mais rappelez-vous, vous êtes dans un moment critique ici et vous devriez commencer par ce qui est vraiment important. Les tests fonctionnels.

Je ne suis pas le testeur le plus compétent. Loin de là. J'ai encore beaucoup à apprendre et à étudier. Mais autant que je sache, les tests fonctionnels (pour les projets web, au moins) sont les moins invasifs. Vous n'avez pas à créer de mocks, de stubs, de fakes, de dummies. Vos tests vont interagir avec le navigateur et simuler l'interaction humaine.

À ce stade, vous avez une base de code avec seulement le code dont vous avez besoin et quelques tests pour vous aider à arrêter d'ajouter de nouveaux bugs avec chaque nouvelle fonctionnalité. C'est une situation gagnant-gagnant. Maintenant, vous pouvez vous arrêter, respirer et réfléchir plus calmement.

### Et ensuite ?

![Image](https://cdn-media-1.freecodecamp.org/images/6R3e-PyHQpIrCFWPlPpxLYGtp3X3Za7Xv5pn)
_Photo par [Unsplash](https://unsplash.com/photos/4pPzKfd6BEg?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Patryk Grądys</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Avec plus de temps, moins de bugs et la santé mentale en place, vous pouvez commencer à aborder d'autres problèmes. Avez-vous pensé à l'intégration continue ? Comment est le flux de travail de développement de votre équipe ? Si vous utilisez git (ce que j'espère), vous pourriez commencer à planifier vos branches. Créez une branche master, une branche develop, ajoutez de nouvelles fonctionnalités via des branches de fonctionnalités, des branches de hot fix, et ainsi de suite.

Comment est votre livraison continue ? Comment sont créées vos versions ? Si vous devez faire plus que "pousser un bouton", peut-être est-il temps de penser à ce processus. Comment pourriez-vous le rendre plus fiable, moins sujet aux erreurs ? Votre application génère-t-elle suffisamment de logs ? Pourriez-vous améliorer cela ? Maintenant, c'est le moment de créer un meilleur logiciel, maintenant c'est à vous de jouer.

### C'est tout

Nous travaillons toujours sur notre héritage, en essayant de l'améliorer. Bien que nous n'ayons pas encore atteint le scénario idéal, plusieurs choses ont changé. Maintenant, nous n'avons que le code nécessaire. Le flux de travail pour cette extension particulière est bien défini. Nous avons des tests fonctionnels en place et le processus de déploiement s'améliore.

Après avoir changé ce scénario et survécu à l'enfer du code hérité, notre équipe a eu pour tâche de développer une nouvelle extension pour le même vieux Magento 1.9. Toute personne saine d'esprit serait en colère à ce sujet, mais je pense que c'est le moment idéal pour faire la bonne chose. C'est l'occasion de transformer toutes les plaintes en meilleures pratiques et de créer un logiciel avec la maintenabilité en tête. Mais c'est un sujet pour un autre article.