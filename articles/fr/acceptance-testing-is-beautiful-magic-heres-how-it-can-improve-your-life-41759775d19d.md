---
title: Les tests d'acceptation sont une belle magie. Voici comment ils peuvent améliorer
  votre vie.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-21T21:38:59.000Z'
originalURL: https://freecodecamp.org/news/acceptance-testing-is-beautiful-magic-heres-how-it-can-improve-your-life-41759775d19d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G7F-40pBvJwqungBuBtYyg.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les tests d'acceptation sont une belle magie. Voici comment ils peuvent
  améliorer votre vie.
seo_desc: 'By Todd Chaffee

  More accurately, automated acceptance testing in the browser is beautiful magic.

  Actually, what I really want to say is that automated acceptance testing might lead
  to discussing the superb finish of your favorite Pinot Noir with your...'
---

Par Todd Chaffee

Plus précisément, les tests d'acceptation **automatisés** dans le navigateur sont une belle magie.

En fait, ce que je veux vraiment dire, c'est que les tests d'acceptation automatisés pourraient vous amener à discuter de la superbe finition de votre Pinot Noir préféré avec vos amis autour d'un dîner. Je promets que tout cela aura du sens à la fin de cet article.

Revenons à la **belle magie**.

### Un peu sur les tests d'acceptation automatisés

Chaque programmeur adore les tests automatisés dans le navigateur lorsqu'il les voit pour la première fois. J'ai vu des programmeurs blasés, pas faciles à impressionner, rire de joie la première fois qu'ils les voient. J'admets avoir ri la première fois. Lorsque vous lancez les tests, votre navigateur s'ouvre et, sans rien faire d'autre, il semble que quelqu'un clique et fasse des choses.

![Image](https://cdn-media-1.freecodecamp.org/images/Upv6tg4GJKTtbmFRgm865j6EMvANd8tzMyFc)
_Tous vos navigateurs nous appartiennent_

C'est si étrange ou amusant ou fascinant que Chrome ressent le besoin de faire apparaître un avertissement en haut du navigateur : « Chrome est contrôlé par un logiciel de test automatisé. » Je suppose que c'est pour clarifier que ce ne sont pas des fantômes ou des robots ? Appelons cela des robots quand même. Mais peu importe à quel point cela semble cool au début (même si vous n'êtes pas impressionné par mon GIF animé), ce n'est même pas le genre de belle magie dont je parle.

En tant que programmeur de longue date, je me soucie surtout de la belle magie qui nous rend meilleurs dans notre travail. Avant d'essayer de vous convaincre des avantages des tests d'**acceptation** automatisés, mettons-les rapidement en contexte. Il existe de nombreux types de tests en matière de logiciels. Une façon classique de catégoriser les tests est de voir combien de parties du logiciel les tests couvrent :

**Tests unitaires** — testent la plus petite unité possible de code source, généralement une fonction ou une méthode

**Tests d'intégration** — s'appuient sur les tests unitaires en vérifiant comment les unités fonctionnent ensemble lorsqu'elles s'appellent mutuellement

**Tests d'acceptation** — testent que TOUT fonctionne du point de vue de l'utilisateur

Vous pouvez faire des tests d'acceptation de la manière difficile. D'abord, les programmeurs cliquent sur l'ensemble du site web, en effectuant des tests manuels, des dizaines ou des centaines de fois. Ensuite, le client — qui vous paie — effectue le même exercice douloureux et chronophage (et manque sûrement des choses). Ce qui nous amène de la belle magie à un mystère :

**Pourquoi des personnes, payées pour automatiser les choses, font-elles manuellement quelque chose encore et encore qui peut être fait bien plus rapidement par un robot ?**

Je ne tenterai pas de résoudre ce mystère. Au lieu de cela, je veux vous raconter une courte histoire sur tous les types de belle magie que les tests d'acceptation automatisés peuvent apporter dans votre vie de programmeur.

### Améliorer freeCodeCamp avec des tests d'acceptation automatisés

La [version bêta de freeCodeCamp](http://beta.freecodecamp.com/en/) présente quelques améliorations impressionnantes pour les personnes apprenant à coder. L'une d'elles est une fonctionnalité qui permet aux étudiants de cliquer sur un bouton et de vérifier que leur projet fonctionne. Vous avez vu un robot cliquer sur ce bouton dans le GIF animé ci-dessus. Le bouton devient vert une fois que toutes les fonctionnalités fonctionnent dans le projet de l'étudiant. Cela apporte de la valeur aux étudiants, car lorsqu'ils cliquent et voient la lumière verte, ils peuvent être confiants d'avoir terminé le projet.

Grâce au travail acharné de [Peter Weinberg](https://github.com/no-stack-dub-sack), [Anis Nouira](https://github.com/Weezlo), [Tracey Bushman](https://github.com/tbushman), [Christian Paul](https://github.com/Christian-Paul), [Sean Smith](https://github.com/bonham000), [Andre Alonzo](https://github.com/paycoguy) et [d'autres](https://github.com/freeCodeCamp/testable-projects-fcc/graphs/contributors), nous avons cette fonctionnalité pour 15 des projets sur la [version bêta de freeCodeCamp](http://beta.freecodecamp.com/en/). Vous pouvez voir un exemple de [chaque projet sur CodePen](https://codepen.io/collection/npZPmR/), et même exécuter les tests manuellement vous-même.

Cette fonctionnalité est un type de test, mais ce n'est pas le genre de test dont nous parlons. Continuons donc à l'appeler une fonctionnalité pour éviter toute confusion. La fonctionnalité dispose d'une interface web que les étudiants utilisent comme toute autre fonctionnalité sur un site web. Quelqu'un a dû coder cette interface. Et pour chaque projet étudiant assigné, quelqu'un a dû écrire un ensemble séparé de code qui décrit les fonctionnalités uniques de ce projet. Vous pouvez voir tout le code [sur le dépôt GitHub](https://github.com/freeCodeCamp/testable-projects-fcc) (veuillez envisager de vous porter volontaire si vous souhaitez nous aider à améliorer cette fonctionnalité).

Chaque contributeur a également la responsabilité de s'assurer que cette fonctionnalité fonctionne pour les centaines de milliers d'étudiants de freeCodeCamp qui l'utiliseront. Il s'agit d'une fonctionnalité de production qui vit sur le web comme toute autre fonctionnalité de site web.

Les programmeurs avisés auront déjà compris où je veux en venir : écrire des tests d'acceptation automatisés pour cette fonctionnalité. Et oui, cette fonctionnalité est un test, donc nous testons les tests. Cela semble-t-il **trop de tests** ? Ce n'est pas le cas. Tant qu'un utilisateur final quelque part utilisera votre fonctionnalité sur le web, il y a de bonnes raisons d'automatiser le test de cette fonctionnalité. Même si la fonctionnalité elle-même est une sorte de test. Assez de méta, passons à autre chose.

Lorsque j'ai rejoint le projet qui fournit cette fonctionnalité, on m'a demandé, ainsi qu'à d'autres bénévoles, de corriger quelques bugs que les étudiants avaient découverts.

J'ai reproduit avec plaisir le premier problème et j'ai commencé à coder. Assez rapidement, j'ai corrigé mon premier bug, puis il était temps de tester ma solution. Argh, la douleur ! Les cheveux arrachés de frustration ! Le temps absurde que cela m'a pris ! Voici mon processus :

1. Forker le projet CodePen de l'exemple pour le test que je viens de corriger.
2. Changer les paramètres JavaScript pour utiliser mon bundle local au lieu du CDN.
3. Quelques autres étapes manuelles omises ici, comme changer la vue CodePen et rafraîchir le projet... vous les voyez toutes dans le GIF au début de cette histoire.
4. Cliquer sur le bouton « Run Tests ».
5. Attendre que les tests se terminent et vérifier s'ils sont réussis.
6. Et voici la pire partie : **retourner à l'étape 2 et répéter pour chacun des quatorze autres projets d'exemple CodePen !**

Si, à un moment donné, vous trouvez et corrigez un autre problème avec votre code, vous devez répéter tout le processus.

Il m'a fallu environ dix minutes pour reproduire et corriger mon premier problème. Et **presque une heure** de clics ennuyeux pour tester mes changements et m'assurer que ma correction n'avait rien cassé d'autre. Je savais que cela ne pouvait pas continuer. Je ne voulais pas que cela continue.

Ce n'était pas scalable, et nous espérions ajouter plus de projets de campeurs et éventuellement supporter plus de frameworks comme Angular. Nous voulions également nous assurer que la fonctionnalité fonctionne sur tous les navigateurs et systèmes d'exploitation modernes — et je ne l'avais testée que sur Linux avec Chrome. Devais-je recruter un autre bénévole pour une heure de leur temps pour tester sur Mac ? Et sur Windows ?

Il semblait que le processus de test allait rendre l'expérience du projet mauvaise pour les bénévoles. C'était déjà une mauvaise expérience pour moi. Presque aucun temps ne serait passé à faire la partie vraiment amusante : la programmation. Je suis donc retourné à la partie amusante et j'ai écrit un programme pour automatiser les tests d'acceptation en utilisant Selenium.

Voici le processus de test maintenant que nous l'avons automatisé avec Selenium :

```
npm test
```

C'est tout. Vous pouvez immédiatement retourner à la programmation (ou à ce que vous préférez faire plutôt que le travail ingrat de tester manuellement) et revenir quatre minutes plus tard pour voir si tous les tests ont réussi. Un processus manuel d'une heure réduit à quatre minutes. Les robots peuvent être rapides.

### La belle magie

La chose la plus importante que je retire des tests d'acceptation automatisés est **plus de temps pour faire les choses que j'aime vraiment**_._ Comme cela pourrait ne pas être évident d'après mon histoire, voici une liste de quelques-unes des autres belles magies que vous pouvez obtenir en automatisant vos tests d'acceptation.

![Image](https://cdn-media-1.freecodecamp.org/images/dO15y4VFayMps9W3PTWn8o9Wrn4gzedFNUci)
_Assurez-vous que chaque PR passe tous les tests_

1. C'est répétable. Un robot **n'oublie jamais** aucun des tests.
2. Si vous le faites correctement, cela devrait être beaucoup plus rapide que les tests manuels. Plus d'informations à ce sujet dans le lien à la fin de cet article.
3. GitHub vous permet d'exécuter les tests automatiquement sur un serveur d'intégration continue lorsque vous créez une pull request. Vous pouvez vous assurer que chaque PR passe les tests avant d'être fusionnée. [Voici un lien vers la sortie](https://travis-ci.org/freeCodeCamp/testable-projects-fcc/builds/258281930?utm_source=github_status&utm_medium=notification) des tests Travis CI pour l'une de nos PR.
4. C'est scalable. À mesure qu'un projet grandit, il prend de plus en plus de temps à le tester. Pouvez-vous imaginer tester manuellement le site web d'Amazon avec toutes ses fonctionnalités ?
5. C'est une documentation gratuite. Votre code source est une liste de tous les tests qui doivent être effectués. La sortie de votre suite de tests fournit également une liste lisible par l'homme des tests qui ont été effectués (voir la sortie Travis CI du point 3, ci-dessus).
6. Vous pouvez couvrir beaucoup plus de configurations. Un testeur humain aura généralement accès à un ou deux systèmes d'exploitation et à quelques navigateurs (au maximum). Peut-être à quelques téléphones mobiles différents. Avec les tests automatisés, vous pouvez exécuter vos tests sur [des centaines de combinaisons de systèmes d'exploitation, de téléphones mobiles et de versions de navigateurs](https://saucelabs.com/platforms).

Un dernier avantage. Imaginons qu'un client vous appelle un vendredi soir **alors que vous êtes sur le point de vous asseoir pour dîner avec des amis**. Vous faites l'erreur de répondre à l'appel parce que c'est l'un de vos meilleurs clients. Ils ont désespérément besoin d'une ligne de code changée pour corriger quelque chose de mineur pour une grande vente de week-end. C'est une correction facile, donc vous la faites en cinq minutes. Maintenant, vous avez deux choix (je n'inclus pas le choix peu judicieux de ne pas tester votre changement) :

1. Passez-vous par un processus **d'au moins une heure** de test manuel de chaque fonctionnalité sur le site web pour vous assurer que votre correction n'a rien cassé ? Dans votre précipitation à ne pas faire attendre vos amis, quels tests allez-vous manquer ?
2. Ou tapez-vous `npm test` et laissez un robot prendre le relais pour que vous puissiez retourner auprès de vos amis, qui viennent **d'ouvrir une bouteille de votre Pinot Noir préféré** ? Cent pour cent confiant de ne rien avoir cassé et votre week-end de plaisir peut commencer (tandis que la grande vente de votre client leur rapporte des tonnes d'argent).

Si ce n'est pas de la belle magie — j'ai promis et livré du vin — alors vous ne serez peut-être jamais convaincu d'essayer les tests d'acceptation automatisés.

Si vous souhaitez en savoir plus sur la façon de rendre vos tests automatisés fiables et rapides, consultez mon article sur les [Tests Selenium NodeJS Fiables](https://medium.com/@tchaffee/reliable-selenium-nodejs-tests-c3fdafdca2a9). Le vin n'est pas inclus.

Avez-vous aimé cet article ? Si oui, donnez-moi quelques applaudissements pour que plus de gens le voient. Merci !