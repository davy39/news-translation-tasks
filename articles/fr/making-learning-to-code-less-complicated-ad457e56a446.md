---
title: 'Conception de Glitch : Comment nous abordons la complexité persistante du
  développement web'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-25T15:26:28.000Z'
originalURL: https://freecodecamp.org/news/making-learning-to-code-less-complicated-ad457e56a446
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IpRjQvEIQfdIsStej476rA.jpeg
tags:
- name: Design
  slug: design
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Conception de Glitch : Comment nous abordons la complexité persistante
  du développement web'
seo_desc: 'By Gareth Wilson

  As the analogy goes, a frog placed in boiling water will jump out. But if it’s placed
  in cold water that’s slowly heated, it won’t perceive the danger, and it will be
  cooked to death.

  Web Developers are like those frogs, slowly boili...'
---

Par Gareth Wilson

Comme le dit l'analogie, une grenouille placée dans de l'eau bouillante va sauter. Mais si elle est placée dans de l'eau froide qui chauffe lentement, elle ne percevra pas le danger et sera cuite à mort.

Les développeurs web sont comme ces grenouilles, bouillant lentement. Immergés dans le code et les outils tous les jours, nous n'avons pas remarqué la lente progression de la complexité. Mais abordez l'industrie avec des yeux neufs — comme quelqu'un qui apprend juste à coder, par exemple — et vous verrez combien de personnes sont submergées avant même d'avoir tapé une ligne de code. Quel langage de programmation dois-je commencer ? Quelles bibliothèques dois-je utiliser ? Quel IDE est le meilleur ? SQL ou NoSQL ? Fusionner ou rebaser ? Et qu'est-ce qu'un dyno ?

C'est cette complexité qui nous a poussés chez Fog Creek à construire [Glitch](https://glitch.com), la communauté conviviale où vous construirez l'application de vos rêves (ou de vos besoins pragmatiques !). Il élimine toute la configuration, donc vous n'avez qu'à vous soucier d'écrire du code pour construire une application web. Parce que malgré avoir construit des produits web utilisés par des millions de personnes, comme Stack Overflow et Trello, depuis plus de 15 ans, nous avons réalisé que nous oublions souvent la complexité dans laquelle nous sommes immergés chaque jour en tant que développeurs.

Au fil des années où le développement web a existé, nous avons vu la prolifération d'outils, de langages, de bibliothèques et de frameworks qui visent à rendre le développement web plus facile. Mais maintenant, avant même d'arriver à 'Hello World', nous devons travailler à travers la complexité de la configuration des serveurs, de l'exécution de commandes shell, de la compilation de fichiers, de la mise en place de pipelines de build et de la maîtrise des systèmes de contrôle de version.

Le résultat est que si vous venez de commencer à apprendre à coder, il y a une énorme quantité de choses non liées au code que vous devez gérer. Cela peut être une distraction de l'apprentissage des concepts de programmation de base. Et ils sont susceptibles de vous faire trébucher, donc vous passez ce peu de temps précieux que vous avez à tondre le proverbial yak, et à résoudre les types de problèmes qui — une fois résolus — ne vous ont rien appris.

![Image](https://cdn-media-1.freecodecamp.org/images/-08iKf0GuvdkB7N1CrzZSNDfKZIfnKXk0Vgx)

Plus nous avons mené des recherches utilisateurs — en parlant avec des personnes nouvelles en codage — plus des phrases comme 'se sentir stupide' et 'se sentir idiot' sont apparues. Mais nous n'aurions vraiment pas dû être si surpris. Après tout, si un développeur expérimenté comme Ron Jeffries, le père de l'Extreme Programming, est [bloqué pendant des jours](http://ronjeffries.com/articles/016-0607/yaks/) juste en essayant de faire fonctionner une simple application, alors quel espoir reste-t-il pour le reste d'entre nous ?

#### Supprimer une partie de la complexité du développement web

Nous avons donc pensé que nous pourrions essayer de résoudre ce problème. La première chose, cependant, était de bien préciser quel problème nous cherchions à résoudre. Le développement web est un domaine extrêmement complexe avec une multitude de problèmes, et nous ne pouvions espérer les résoudre tous.

Nous avons commencé par une [Creek Week](http://blog.fogcreek.com/how-we-embed-a-culture-of-innovation-with-creek-weeks/). C'est là où nous prenons une semaine loin de nos activités quotidiennes et nous concentrons entièrement sur la recherche d'un problème. Le pitch pour la Creek Week était 'abstraire les parties ennuyeuses et difficiles à apprendre du développement' et livrer quelque chose qui permettait aux gens d'écrire une application et de la déployer sur une URL sans la monotonie.

C'est un peu plus spécifique, et cela a aidé à exclure un certain nombre de choses. Pour commencer, nous 'abstractions' — pas en remplaçant. Et nous ne cherchions pas à rendre la programmation elle-même plus facile. Nous ne recréions pas simplement [Logo](https://en.wikipedia.org/wiki/Logo_%28programming_language%29).

Cette mission a aidé à concentrer nos recherches. Nous avons examiné les solutions existantes qui touchaient à ce domaine mais n'avaient pas encore résolu le problème. Des solutions comme IaaS, PaaS, Développement Rapide d'Applications, et les éditeurs de code en ligne. De cela, nous avons beaucoup appris, y compris certaines approches que nous pensions devoir éviter, comme essayer de se passer de code en créant un logiciel de création d'applications visuelles. C'est un chemin bien tracé, sans réel gagnant à ce jour. Nous voulions conserver la puissance et la flexibilité du codage, mais simplement le rendre plus rapide et plus facile à démarrer.

Pendant la Creek Week, nous avons créé un concept de preuve qui a été utilisé pour obtenir l'adhésion du reste de l'organisation, afin que nous puissions obtenir un feu vert pour explorer le problème plus avant. Nous avons également créé quelques maquettes :

![Image](https://cdn-media-1.freecodecamp.org/images/kk1O0hftLs5thuAC2R9MVsWlCRn-zwTQA9pn)
_Maquette initiale de l'éditeur_

![Image](https://cdn-media-1.freecodecamp.org/images/SDJ84Plb01jO2G2fWDWvTOWESlIOjV6pC1Cb)
_Maquette de l'écran de création de projet_

Vous remarquerez des aspects comme un bouton pour 'commit et push', la branche 'master', et la section 'tests'. Nous n'avions pas encore commencé à nous pencher sur les technologies que nous voulions utiliser pour résoudre le problème. Nous devions être plus spécifiques.

#### Conception de produit basée sur des principes

Pour ce faire, comme [lorsque nous avons créé Trello](http://blog.fogcreek.com/the-process-of-creating-trello-tech-talk/), nous avons réduit notre réflexion à quelques principes de produit. Ceux-ci étaient une tentative de décrire notre approche et d'encapsuler nos opinions sur la meilleure façon de résoudre le problème. Ils étaient :

* Être le moyen le plus rapide et le plus facile d'obtenir votre propre application web et de commencer à travailler dessus.
* Vous devriez obtenir des retours instantanés et directs lorsque vous modifiez votre application.
* Vous devriez toujours vous sentir en sécurité pour faire des modifications, et vous pouvez essayer des idées sans casser votre projet.
* L'éditeur devrait être amusant à utiliser, tout en étant rapide et accessible.

Cela nous a aidé à affiner nos idées de manière plus critique.

Ainsi, par exemple, en réévaluant la maquette de l'écran de création de projet ci-dessus avec ces principes à l'esprit, nous avons pu voir qu'en tant que point de départ, cela signifiait que les utilisateurs devraient faire un certain nombre de choix difficiles sur les technologies dès le départ. Au lieu de pouvoir simplement commencer à faire quelque chose, vous devriez probablement partir faire des recherches sur les différences entre les options fournies. Cela violait clairement notre premier principe de produit de vous faire démarrer rapidement, et était plus un exemple de notre trop grande opinion sur la 'meilleure façon' de coder.

Ces principes signifiaient également abandonner le bouton 'commit et push', car cela supposait non seulement que vous saviez ce qu'était un 'commit' et ce qu'un 'push' ferait, mais c'était aussi un blocage pour les retours instantanés. De plus, parler de ces principes avec des personnes a révélé que le contrôle de version était une source de beaucoup d'anxiété et de confusion, la plupart des gens n'utilisant qu'un petit sous-ensemble des capacités de Git.

De même, bien que la flexibilité et le contrôle offerts par l'accès à la ligne de commande soient puissants, ils exposaient les utilisateurs à des problèmes d'environnement qui pouvaient prendre des heures à résoudre et dont ils apprenaient souvent peu. Pourtant, si nous voulions être le 'plus facile', alors nous devions construire sur la manière existante dont les gens utilisent le code. Ainsi, copier et coller une réponse de Stack Overflow devrait simplement fonctionner comme sur votre machine locale.

Et ainsi, armés de ces principes de produit, nous avons estimé avoir maintenant une compréhension suffisante pour construire le MVP. La recherche et l'analyse ne pouvaient nous mener que jusqu'à un certain point. Maintenant, nous voulions savoir comment ces idées fonctionneraient en pratique.

#### Construction du MVP

Les mois suivants ont été un mélange de développement, de tests utilisateurs internes et — pour garder le projet sur la bonne voie — de points d'étape bimensuels entre l'équipe et les fondateurs. Ces sessions ont aidé à fournir des contributions de ceux qui n'étaient pas impliqués dans les problèmes quotidiens du projet. Et à ce titre, elles ont servi de moyen de prévenir la pensée de groupe et de s'enliser dans les détails de la product development.

Pour vraiment faire passer ce point, nous devions sortir du bâtiment et obtenir des contributions de ceux qui sont au-delà de notre propre organisation. Nous avons donc demandé de l'aide à nos amis du Recurse Center et de la Flat Iron School. Nous leur avons présenté le produit, obtenu des retours, et avons également mené un certain nombre de sessions de test de produit en tête-à-tête pour obtenir des retours qualitatifs supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/KqHEmmlzxrQLUFO0oFlOtmLNJQGDv2t3qGVl)
_Écran d'insertion de snippets_

Ces tests se sont avérés utiles pour comprendre quels aspects du produit pouvaient correspondre aux principes, mais ne fonctionnaient pas en pratique. Par exemple, pour faciliter les tâches de codage courantes, nous vous permettons de rechercher et d'insérer des extraits de code pré-faits. Cela avait du sens en théorie, mais dans les tests utilisateurs, personne ne les utilisait, même après avoir été informés de leur existence. Et ils posaient un certain nombre de questions délicates, comme d'où viendraient les extraits ? Qui les écrirait et les maintiendrait ? Et devrions-nous simplement ajouter des packages aux projets si un extrait en avait besoin ?

![Image](https://cdn-media-1.freecodecamp.org/images/TxRiSlefsBdEly0YtJPz2vxbMK4ZUkro5EgL)
_Sélection de langage à la volée_

Une autre fonctionnalité qui a vécu pendant des mois dans la bêta était la sélection de langage à la volée pour les fichiers. En théorie, cela facilitait l'expérimentation avec les langages et était un moyen contextuel de montrer aux utilisateurs les langages actuellement supportés. Pour livrer cela, nous avons dû créer un certain nombre de bibliothèques que nous pensions également aider à abstraire une partie du code boilerplate que les frameworks et langages existants nécessitaient.

Cela s'inscrivait bien dans nos principes de produit, mais en réalité, ce qui s'est passé lors des tests, c'est que les gens se sentaient moins à l'aise lorsqu'ils ne pouvaient pas voir leur code d'initialisation. Ce n'était pas ce qu'ils s'attendaient à voir, et cela rendait difficile pour eux de comprendre comment le produit fonctionnait. Nous avons donc continué à affiner le produit, le rendant plus simple et plus transparent.

#### Ce que nous avons livré

La dernière étape était d'obtenir des données d'utilisation et des opinions sur le produit à grande échelle. Nous avons donc ouvert notre bêta à tous, ce qui est là où nous en sommes actuellement. Mais en termes de la grande vision de supprimer la complexité du développement web, qu'avons-nous réellement livré ?

Eh bien, si vous allez sur [glitch.com](https://glitch.com/edit), un nouveau projet est automatiquement démarré qui contient une application de projet de bienvenue. Cette application a sa propre URL et est instantanément accessible à vous et à toute personne avec qui vous la partagez. Et c'est une vraie application web, avec du code côté serveur et côté client.

Vous pouvez ensuite l'éditer, ou créer un nouveau projet, et construire n'importe quelle application Node.js que vous voulez (nous ajouterons bientôt le support pour d'autres backends !), y compris des applications web réelles et entièrement fonctionnelles. Mais ce qui est peut-être plus intéressant, c'est ce que vous n'avez pas eu à faire pour mettre cette application web en route :

* Vous n'avez pas créé de compte.
* Vous n'avez pas configuré et mis en place un serveur web.
* Vous ne vous êtes pas inscrit auprès d'un hébergeur et n'avez pas attendu la mise à jour des serveurs de noms.
* Vous n'avez pas installé de système d'exploitation, LAMP, Node ou autre chose.
* Vous n'avez pas commité, construit ou déployé votre code.

Les applications que vous créez sont instantanément en ligne, hébergées par nous, et sont toujours à jour avec vos dernières modifications, car les modifications sont déployées au fur et à mesure que vous les tapez. Il n'y a pas de configuration, comme la configuration de votre environnement, la mise en place de votre pipeline de build, la mémorisation de Git, ou le déploiement manuel des mises à jour. Et vous pouvez inviter des coéquipiers à votre projet afin de pouvoir collaborer sur le code ensemble et voir les modifications au fur et à mesure qu'elles sont faites.

Vous pouvez commencer rapidement en remixant des projets communautaires existants et chaque projet obtient une URL pour l'édition et la visualisation, afin que vous puissiez partager votre code ou vos créations.

Nous avons encore un long chemin à parcourir, mais nous avons fait les premiers pas pour supprimer une partie de la complexité du développement web. Alors la prochaine fois que vous chercherez à apprendre une nouvelle bibliothèque, écrire un script rapide ou prototyper un produit, essayez-le [par vous-même](https://glitch.com) et voyez à quel point il est plus rapide de commencer à écrire du code.