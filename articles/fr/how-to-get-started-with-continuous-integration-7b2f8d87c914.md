---
title: Comment commencer avec l'intégration continue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-continuous-integration-7b2f8d87c914
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yOJI5juQCdKyFFk9YWKDWw.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment commencer avec l'intégration continue
seo_desc: 'By Jean-Paul Delimat

  Everything you need to know to get started with continuous integration: branching
  strategies, tests automation, tools and best practices.

  The goal: Deliver working code quickly and safely

  The goal of Continuous Integration is to ...'
---

Par Jean-Paul Delimat

Tout ce que vous devez savoir pour commencer avec l'intégration continue : stratégies de branchement, automatisation des tests, outils et bonnes pratiques.

### L'objectif : Livrer du code fonctionnel rapidement et en toute sécurité

L'objectif de l'intégration continue est de livrer du code à la branche principale de votre dépôt :

* Rapidement : de la poussée de nouveau code dans le dépôt à sa fusion avec la branche principale lorsqu'il fonctionne devrait être fait en quelques minutes
* En toute sécurité : comment savons-nous que le nouveau code fonctionne ? L'intégration continue consiste à mettre en place les bonnes vérifications pour fusionner le code automatiquement en toute confiance

L'intégration continue est un peu une question d'outils et beaucoup une question de mentalité et de culture au sein de l'équipe. Vous voulez que votre processus de développement facilite l'intégration rapide de nouveau code tout en gardant une branche principale fonctionnelle à tout moment. Cette branche principale fonctionnelle permettra la livraison continue ou le déploiement continu à l'avenir. Mais ce sont des sujets pour un autre article. Concentrons-nous d'abord sur l'intégration continue.

Il y a 2 piliers pour atteindre l'intégration continue :

#### Travailler par petites parties

Imaginez une équipe de 5 personnes travaillant sur un produit SaaS. Chacun développe une nouvelle fonctionnalité distincte. La charge de travail pour chaque fonctionnalité est d'environ 1 ou 2 semaines. Il y a 2 façons de procéder.

* L'équipe pourrait opter pour des branches de fonctionnalités. Chaque développeur travaillera sur sa partie dans une « branche de fonctionnalité ». Les branches seront fusionnées avec la branche principale une fois que tout le monde sera satisfait de son travail
* L'équipe pourrait opter pour des branches (toujours) mais intégrer leur travail à la branche principale à chaque poussée. Même si les choses sont encore en cours de développement ! Le travail en cours resterait invisible pour tout utilisateur final ou testeur de la branche principale

Quelle approche pensez-vous fonctionnera le mieux ?

La première approche conduira finalement au « syndrome de la version imprévisible ». Les branches de fonctionnalités à longue durée de vie créent un faux sentiment de sécurité et de confort pour chaque développeur **individuellement**. À mesure que les branches s'éloignent les unes des autres sur une longue période, il n'y a aucun moyen de mesurer à quel point il sera difficile de tout fusionner. Au mieux, quelques conflits de code mineurs surgiront, au pire, des hypothèses de conception fondamentales seront remises en question et les choses devront être retravaillées... de la manière difficile.

> _Le retravail sera effectué sous pression temporelle, conduisant à une baisse de qualité et à l'accumulation de dette technique. C'est un cercle vicieux._

Voir l'article sur [Pourquoi vous ne devriez pas utiliser de branches de fonctionnalités](https://fire.ci/blog/why-you-should-not-use-feature-branches/) pour les détails sordides.

La deuxième approche est celle dont nous avons besoin pour permettre l'intégration continue. Chaque développeur travaille sur sa propre branche. La différence est :

> _Les changements sont fusionnés avec la branche principale à chaque poussée, et chaque développeur synchronise sa branche avec la dernière version de la branche principale plusieurs fois par jour._

De cette façon, l'équipe peut corriger les conflits et aligner les hypothèses de conception plus rapidement et plus facilement. 5 petits problèmes découverts tôt sont bien meilleurs qu'un gros problème découvert juste avant le jour de la version. Consultez la section « Feature Toggles » ci-dessous pour voir comment vous devriez intégrer le « travail en cours » à la branche principale.

#### La sécurité vient avec des vérifications automatisées

L'ancien processus de développement logiciel était basé sur un cycle de construction suivi d'un cycle de test. Et cela conviendrait probablement encore à l'approche des « branches de fonctionnalités » décrite ci-dessus. Si nous intégrons et fusionnons le code des dizaines de fois par jour, les tests manuels n'ont pas de sens. Cela prendrait trop de temps. Nous avons besoin de vérifications automatisées pour vérifier que le code fonctionne correctement. Nous avons besoin d'un outil CI qui prendra chaque poussée des développeurs et exécutera la construction et les tests automatiquement.

Le type et le contenu des tests doivent être :

* suffisamment rapides pour fournir un retour au développeur en quelques minutes
* suffisamment complets pour fusionner le code avec la branche principale en toute confiance

Malheureusement, il n'existe pas de type et de contenu de test universels. Le bon équilibre est spécifique à votre projet. N'exécutez pas de grandes suites de tests longues et chronophages pendant votre phase CI. De tels tests offrent une meilleure sécurité, mais ils entraînent un retour différé aux développeurs. Cela conduit à un changement de contexte, ce qui est une pure perte de temps.

### Optimiser le temps des développeurs et réduire les changements de contexte

Les vérifications CI longues, et par longues, je veux dire plus de 3 minutes, introduisent une perte de temps composée pour chaque développeur de votre équipe. Comparons un flux de travail « bon » et un flux de travail « mauvais ».

Le flux de travail « bon » :

* Vous commitez et poussez votre code
* La construction et les tests CI s'exécutent pendant 1 à 3 minutes
* Pendant ces 1 à 3 minutes, vous passez en revue la tâche en cours, mettez à jour le statut dans un outil de gestion, ou passez en revue votre code une fois de plus
* En moins de 3 minutes, vous obtenez un statut réussi : vous pouvez passer à la partie suivante de votre tâche. Si vous obtenez une construction échouée : vous pouvez corriger le problème immédiatement

Le flux de travail « mauvais » :

* Vous commitez et poussez votre code
* La construction et les tests CI s'exécutent pendant 15 minutes
* Que faites-vous pendant ces 15 minutes ?
* Vous pourriez prendre un café avec l'équipe. Juste, mais combien de fois pouvez-vous faire cela par jour ?
* Vous vous pencheriez probablement sur la tâche suivante dans votre pipeline
* 15 minutes plus tard, vous recevez une notification de construction échouée. Vous devez revenir à la tâche précédente, essayer de corriger le problème... et repartir pour une autre boucle de 15 minutes...
* À ce stade, vous vous demandez : dois-je revenir à cette tâche suivante ou simplement attendre les 15 minutes et obtenir la tranquillité d'esprit que je suis vraiment terminé avec ma tâche actuelle...

Le mauvais flux de travail n'est pas seulement une perte de temps. C'est aussi frustrant pour les développeurs. Et des développeurs productifs sont des développeurs heureux.

> _Vous devez aligner vos outils et flux de travail pour garder vos développeurs heureux._

### Outils

#### Branchement

L'intégration continue consiste à intégrer le code des différentes branches des développeurs à une branche commune dans votre système de gestion de configuration. Il est probable que vous utilisiez git. Dans git, la branche principale par défaut dans un dépôt est appelée « master ». Certaines équipes créent une branche appelée « develop » comme branche principale pour l'intégration continue. Elles utilisent « master » pour suivre les livraisons et les déploiements (develop étant fusionné avec master).

Vous avez probablement déjà une branche principale à laquelle votre équipe pousse ou fusionne le code. Restez avec celle-ci.

Chaque développeur devrait travailler sur sa propre branche. On peut utiliser plusieurs branches si l'on travaille sur de nombreux sujets différents à la fois. Bien que cela pourrait être un signe de travail « non focalisé » au mieux. Dès qu'une partie cohérente de votre code est prête, poussez votre dépôt. Les vérifications CI se déclencheront et fusionneront votre code avec la branche principale si elles réussissent. Si les vérifications échouent, vous êtes toujours sur votre propre branche et pouvez corriger ce qui doit l'être et pousser à nouveau.

Le mot important dans le processus ci-dessus est **partie cohérente de votre code**. Comment savez-vous qu'elle est cohérente ? Simple.

> _Si vous pouvez facilement trouver un bon message de commit, c'est cohérent._

En revanche, si votre message de commit nécessite 3 puces et de nombreux adjectifs et adverbes, ce n'est probablement pas bon. Divisez votre travail en plusieurs commits cohérents. Puis poussez le code. Les commits cohérents aident aux revues de code et rendent l'historique du dépôt plus facile à suivre.

Ne poussez pas n'importe quoi parce que c'est la fin de la journée !

#### Pull requests

Qu'est-ce qu'une pull request ? Une pull request est un concept dans lequel vous demandez à l'équipe de fusionner votre branche avec la branche principale. L'acceptation de votre demande devrait passer par un statut fourni par votre outil CI et potentiellement une revue de code. En fin de compte, l'acceptation manuelle d'un être humain responsable de la fusion des pull requests.

Les pull requests sont nées dans les projets open source. Les mainteneurs avaient besoin d'une manière structurée d'évaluer les contributions avant de les fusionner. Les pull requests ne font pas partie de Git. Elles sont supportées par tout fournisseur Git, cependant (GitHub, BitBucket, GitLab, ...).

Notez que les pull requests ne sont pas obligatoires pour l'intégration continue. Leur principal avantage est de supporter un processus de revue de code, qui ne peut pas être automatisé par conception.

Si vous utilisez des pull requests, les mêmes principes de « travailler par petites parties » et « optimiser le temps des développeurs » s'appliquent :

* gardez chaque pull request petite et avec un objectif clair (cela rendra la revue de code beaucoup plus facile)
* gardez vos vérifications CI rapides

#### Vérifications automatisées

Le cœur de votre processus continu est constitué de vérifications automatisées. Elles garantissent que le code de la branche principale fonctionne correctement après que votre code a été fusionné. Si elles échouent, votre code ne sera pas fusionné. Au minimum, le code doit compiler ou transpiler ou quoi que votre stack technique fasse pour le rendre prêt pour l'exécution.

En plus de la compilation, vous devriez exécuter des tests automatisés pour garantir que le logiciel fonctionne correctement. Meilleure est la couverture des tests, meilleure est la confiance que vous pouvez avoir dans le nouveau code fusionné avec la branche principale. Attention cependant ! Une meilleure couverture signifie plus de tests et un temps d'exécution plus long. Vous devez trouver le bon compromis.

_Où commencez-vous lorsque vous n'avez aucun test ou que vous devez réduire certains tests longs ? Concentrez-vous sur ce qui est critique pour votre projet ou produit._

Si vous construisez une application SaaS, vous devriez vérifier que les utilisateurs peuvent s'inscrire ou se connecter, et effectuer les opérations les plus basiques que votre SaaS fournit. À moins que vous ne développiez un concurrent de Salesforce, vous devriez être en mesure d'exécuter vos tests en quelques minutes, voire secondes. Si vous construisez un backend de traitement de données lourd : utilisez des ensembles de données limités pour exercer les différents blocs de construction. Gardez les exécutions longues sur de grands ensembles de données hors de l'intégration continue. Les tests longs peuvent être déclenchés après la fusion du code.

### Conseils Pro

#### Feature toggles

Le concept clé de l'intégration continue est de mettre votre code dans la branche principale dès que possible. Même le travail en cours. Même les fonctionnalités qui ne fonctionnent pas complètement ou que vous ne voulez pas exposer aux testeurs ou aux utilisateurs finaux. La façon d'y parvenir est d'utiliser des feature toggles. Ayez votre nouvelle fonctionnalité sous un toggle activé/désactivé. Le toggle peut être un flag booléen au moment de la compilation, une variable d'environnement ou une chose au moment de l'exécution. La bonne approche dépend de ce que vous voulez atteindre.

Le premier avantage majeur des feature toggles est que vous pouvez les emmener jusqu'en production et activer/désactiver la nouvelle fonctionnalité selon les besoins. Vous pourriez redémarrer un serveur avec une variable d'environnement modifiée, ou activer/désactiver une nouvelle disposition de tableau de bord UI. De cette façon, vous avez une flexibilité totale pour déployer la fonctionnalité. Ou la désactiver si elle cause des problèmes inattendus en production. Ou permettre aux utilisateurs finaux d'opter pour ou contre la fonctionnalité (dans le cas des toggles UI).

Le deuxième avantage majeur des feature toggles est qu'ils vous obligent à penser à la frontière entre ce que vous faites et le code existant. C'est un bon exercice et c'est ce que vous devriez commencer de toute façon chaque fois que vous faites une addition à un système existant. L'étape du feature toggle rend cette étape du processus plus visible.

Le seul inconvénient des feature toggles est que vous devez les nettoyer périodiquement de l'environnement et du code. Une fois qu'une fonctionnalité est testée en conditions réelles et adoptée par les utilisateurs, elle devrait être la valeur par défaut. Le code pour le toggle et l'ancienne version des choses (si elle existe) devrait être nettoyé. Ne tombez pas dans le piège d'un système de « configuration en tant que toggles ». Le piège est que vous ne pourrez jamais maintenir et tester toutes les combinaisons des toggles et aurez une architecture fragile à la fin.

#### Gardez le temps de construction CI sous les 3 minutes

Souvenez-vous du flux de travail « bon » et « mauvais » dans la première partie de l'article. Nous voulons éviter les changements de contexte pour les développeurs. Prenez votre téléphone et réglez un minuteur de 3 minutes. Voyez combien de temps cela semble lorsque vous attendez simplement quelque chose ! 3 minutes devraient être un maximum absolu pour vous concentrer et passer en toute sécurité et efficacement d'une tâche à l'autre.

Une construction en moins de 3 minutes peut sembler folle pour certaines équipes, mais c'est définitivement réalisable. Cela a plus à voir avec la façon dont vous organisez votre travail qu'avec les outils que vous utilisez. Voici des façons d'optimiser votre construction :

* Utilisez plus de capacité de construction : si vous n'avez pas assez de constructions concurrentes sur votre outil CI et que les constructions sont mises en file d'attente, les développeurs perdent du temps
* Exploitez la mise en cache : la plupart des stacks techniques vous obligent à installer et configurer des dépendances lors de l'exécution d'une nouvelle construction. Votre outil CI devrait être en mesure de mettre en cache ces étapes lorsque les dépendances ne changent pas pour optimiser le temps de construction
* Passez en revue vos tests : vérifiez que vos tests sont optimisés pour le temps. Supprimez les délais d'attente et les étapes d'attente « longues en toute sécurité ». Si vous avez des suites de tests lourds à exécuter, envisagez de les déplacer sur une construction séparée qui est exécutée après la fusion avec la branche principale. Ils ne feront plus partie des garanties de l'intégration continue, mais les tests lourds ne devraient pas l'être de toute façon
* Divisez votre base de code : devez-vous avoir tout dans un seul dépôt ? Devez-vous construire et exécuter des tests sur tout même lorsqu'une petite partie change ? Il pourrait y avoir des gains ici.
* Exécutez des tests conditionnellement : exécutez vos tests uniquement si certains répertoires ont changé. Si votre base de code est bien organisée, cela peut être un énorme gain

> _Ce qui est formidable dans le fait de forcer une limite de temps courte sur vos vérifications CI, c'est que cela vous oblige à améliorer fondamentalement tout votre processus de développement._

Comme l'a dit [Jim Rohn](https://www.jimrohn.com/) :

> « Devenez millionnaire non pour les millions de dollars, mais pour ce que cela fera de vous pour l'atteindre. »

#### La fusion virtuelle : votre code seul n'a pas vraiment d'importance

La plupart des outils d'intégration continue exécutent la construction CI sur votre branche pour dire si elle peut être fusionnée ou non. Mais ce n'est pas ce qui est intéressant ici. Si vous savez ce que vous faites, il y a de bonnes chances que le code que vous venez de pousser fonctionne déjà ! Ce que votre outil CI est censé vérifier, c'est que votre branche fusionnée avec la branche principale fonctionne correctement.

Votre outil CI devrait effectuer une fusion locale de votre branche avec la branche principale et exécuter la construction et les tests contre cela. Votre branche peut alors être fusionnée automatiquement si la branche principale ne change pas entre-temps. Si elle change, les vérifications CI doivent être exécutées à nouveau jusqu'à ce que votre code puisse être fusionné en toute sécurité. Si votre outil CI ne supporte pas ce type de flux de travail, changez d'outil.

#### Le gestionnaire de tâches maléfique

Il y a une croyance erronée qu'il est cool de pouvoir tracer le code lié à une tâche dans votre tableau Agile ou votre suivi de bugs comme JIRA ou similaire. Bien que ce soit un beau concept sur le papier, l'impact sur le processus de développement n'en vaut certainement pas la peine. Le gestionnaire de tâches fournit une vue « fonctionnalités et bugs » du monde. Le code est structuré et organisé en couches de manière très différente. Essayer de réconcilier un élément dans le gestionnaire de tâches et un ensemble de commits est inutile. Si vous voulez savoir pourquoi un morceau de code a été écrit, vous devriez pouvoir obtenir l'information à partir du contexte et des commentaires du code.

### Réflexions finales

Les outils ne sont que des outils. La configuration des outils est probablement une affaire d'une heure. Si vous les utilisez mal, cependant, vous n'obtiendrez pas les résultats attendus.

Gardez à l'esprit les objectifs que nous nous sommes fixés pour l'intégration continue :

* Livrer du code fonctionnel rapidement et en toute sécurité
* Optimiser le temps des développeurs et réduire les changements de contexte

L'essentiel est de changer votre état d'esprit pour « livrer continuellement de la valeur » à votre projet ou produit.

> _Pensez à votre processus de développement logiciel comme à une installation de production matérielle. Le code des développeurs représente les pièces mobiles. La branche principale est le produit assemblé._

Plus vous intégrez rapidement les différentes pièces ensemble et vérifiez que les choses fonctionnent, plus vous êtes proche d'avoir un produit fonctionnel à la fin.

Quelques exemples pratiques :

* Vous travaillez sur une nouvelle fonctionnalité et devez changer un composant de bas niveau que les autres utiliseront probablement. Faites un commit dédié pour cette partie commune et faites-la fusionner déjà. Ensuite, continuez à travailler sur le reste de votre fonctionnalité. Les autres développeurs pourront baser leur travail sur votre changement immédiatement.
* Vous travaillez sur une grande fonctionnalité qui nécessitera beaucoup de temps et de code ? Utilisez un feature toggle. Ne travaillez pas en isolation. Jamais !
* Vous attendez une revue de code mais personne n'est disponible pour la faire. Si votre code passe les vérifications CI, fusionnez-le simplement et faites la revue de code ensuite. Si cela semble briser le processus, rappelez-vous que « fait est mieux que parfait ». Si cela fonctionne, cela apporte plus de valeur dans la branche principale que garé sur le côté pendant des jours.

**Merci d'avoir lu ! Si vous trouvez l'article utile, cliquez sur le bouton d'applaudissements ci-dessous. Cela signifierait beaucoup pour moi et cela aide les autres à voir l'histoire !**

_Article initialement publié sur [fire.ci](https://fire.ci/blog) le 9 avril 2019._