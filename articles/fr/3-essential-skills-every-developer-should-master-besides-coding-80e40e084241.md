---
title: Compétences essentielles que tout développeur devrait maîtriser (en dehors
  de la programmation)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-21T21:34:05.000Z'
originalURL: https://freecodecamp.org/news/3-essential-skills-every-developer-should-master-besides-coding-80e40e084241
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GP9tKFzB_XqNkHSWuiuk1A.jpeg
tags:
- name: careers
  slug: careers
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Compétences essentielles que tout développeur devrait maîtriser (en dehors
  de la programmation)
seo_desc: 'By Jean-Paul Delimat

  Whether you are learning to code, looking for a new job, or just want to improve
  your skills as a developer, you need to master the essential tools of team collaboration.
  These are as important as knowing how to code.

  It is teamw...'
---

Par Jean-Paul Delimat

Que vous appreniez à coder, que vous cherchiez un nouvel emploi ou que vous souhaitiez simplement améliorer vos compétences en tant que développeur, vous devez maîtriser les outils essentiels de la collaboration en équipe. Ceux-ci sont aussi importants que de savoir coder.

**C'est le travail d'équipe qui fait ou défait les projets logiciels.**

Votre code fonctionnera éventuellement. Si vous voulez qu'il fonctionne "à temps" et soit de bonne qualité, vous et votre équipe devez être organisés.

* Tout le monde doit savoir ce qu'il a à faire et quand
* Le travail des gens ne doit pas se chevaucher ou entrer en conflit
* Des règles communes doivent être suivies par tout le monde

Vous pouvez y parvenir en utilisant les bons processus et outils. Vous voulez que votre équipe se concentre sur la programmation 90% du temps (les 10% restants sont pour les pauses café et les mises à jour Windows).

Voici trois choses essentielles que vous devez maîtriser.

### Git et les Pull Requests

La [gestion de configuration](https://en.wikipedia.org/wiki/Configuration_management) est la base de la collaboration en équipe dans le domaine du logiciel. De nombreux outils existent pour cela, mais heureusement, l'un d'eux est devenu la référence absolue et ultime : [Git](https://git-scm.com/).

La documentation sur les aspects clés est bien décrite dans le [Livre Git](https://git-scm.com/book/en/v2).

Il existe de nombreux services clés en main pour commencer : [GitHub](https://github.com/) est probablement le plus populaire, mais aussi [BitBucket](https://bitbucket.org/) ou [GitLab](https://about.gitlab.com/).

Un excellent outil graphique à utiliser est [SourceTree](https://www.sourcetreeapp.com/). Je vous recommande de maîtriser la ligne de commande avant de vous tourner vers les outils UI, cependant.

Voici les questions auxquelles vous devriez savoir répondre :

* Comment fusionner ou rebaser ma branche, et quelle est la différence ?
* Comment résoudre les conflits ? Par exemple, les miens versus les leurs versus la fusion manuelle
* Qu'est-ce qu'une [branche de fonctionnalité](https://bocoup.com/blog/git-workflow-walkthrough-feature-branches) ?
* Qu'est-ce qu'une [pull request](https://yangsu.github.io/pull-request-tutorial/) ?
* Quels sont les différents [flux de travail de collaboration](https://www.atlassian.com/git/tutorials/comparing-workflows) dans Git ?

C'est tout, et c'est assez simple. Après avoir lu la théorie et avec un peu de pratique, vous deviendrez un maître de Git en un rien de temps.

### Le tableau Agile

La première chose qu'une équipe doit faire lorsqu'elle commence un projet ou une tâche plus importante est de diviser le travail. Au cours des 10 dernières années, la méthodologie "Agile" a remplacé la planification traditionnelle en cascade. Le manifeste Agile est [ici](http://agilemanifesto.org/).

En termes pratiques, il dit "ne planifions pas trop à l'avance, car les entrées et les hypothèses que nous avons aujourd'hui sur le projet changeront". Cela est presque toujours vrai, et de nos jours, il est difficile de trouver une équipe qui ne soit pas (parfois auto-proclamée) "Agile".

Voici les choses pratiques que vous devez savoir :

* La méthode Agile la plus populaire est [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)). Divisez votre projet en "sprints" de deux semaines et placez des "tâches" dans le contenu du sprint. Tout le reste est pour l'avenir et s'appelle le "[backlog](https://www.scrum.org/resources/what-is-a-product-backlog?gclid=EAIaIQobChMIrYurlr7o2AIVEhoYCh0dwQVdEAAYASAAEgIXtPD_BwE)". Cela est utile pour suivre les progrès, ajuster la planification à venir et améliorer la [vélocité de l'équipe](https://www.mountaingoatsoftware.com/blog/know-exactly-what-velocity-means-to-your-scrum-team) au fil du temps.
* Une autre approche Agile est [Kanban](https://en.wikipedia.org/wiki/Kanban). L'idée est de limiter le nombre de tâches qui sont "en cours". De cette façon, vous êtes sûr de clore un élément complètement avant de passer au suivant. Il n'y a pas de sprints ou de délais comme dans Scrum. Vous passez simplement d'une tâche à l'autre jusqu'à ce que vous ayez terminé.

Dans Agile, un projet logiciel sera divisé en dizaines ou centaines de tâches. Vous avez besoin d'un outil pour les gérer. L'outil de référence est [JIRA](https://www.atlassian.com/software/jira).

D'autres outils [existent](https://blog.capterra.com/5-outstanding-atlassian-jira-alternatives-for-your-growing-tech-team/) bien sûr, mais vous devrez probablement travailler avec JIRA à un moment donné. Donc, si vous êtes nouveau dans tous ces outils, optez simplement pour JIRA. Il y a un [essai gratuit de 7 jours](https://www.atlassian.com/software/jira/pricing?tab=cloud). C'est plus que suffisant pour avoir un aperçu de comment les choses fonctionnent. Encore une fois, c'est assez simple et très bien documenté.

### Tests et Intégration Continue

Git et les outils agiles permettent aux équipes d'aller vite. Avec la vitesse viennent inévitablement des erreurs et des bugs. Considérez une équipe de cinq développeurs travaillant sur des morceaux de code plutôt indépendants. Chacun d'eux fera une pull request vers le dépôt. Deux problèmes peuvent survenir :

* Une fois que le code du "premier développeur" arrive dans le dépôt Git, le code des autres n'est plus valide ou ne fonctionne plus parce que certaines choses ont changé. Ce n'est pas une erreur du "premier développeur", c'est juste la vie et cela arrivera.
* Une fois que tous les développeurs ont poussé leur code vers le dépôt Git, les chances que tout fonctionne comme prévu dès le départ sont plutôt faibles. Encore une fois, ce n'est pas le reflet d'un mauvais travail d'équipe. Cela arrivera simplement.

Par conséquent, vous devez tester votre logiciel. Même après que chaque développeur a poussé son code ? Ce serait bien, mais cela serait une perte de temps.

Lorsque d'autres développeurs poussent leur code, nous devrons répéter cette tâche. Devriez-vous tester une fois que tout le monde a poussé son code ? Ce serait aussi bien, mais vous trouverez des bugs tard dans le processus, ce qui peut retarder tout le projet. Alors, comment pouvez-vous résoudre cela ?

Les tests automatisés et l'[Intégration Continue](https://www.martinfowler.com/articles/continuousIntegration.html) sont là pour vous sauver.

Les tests automatisés sont un sujet sur lequel on pourrait écrire de nombreux livres. Chaque langage et framework a son propre ensemble d'outils. Les lister tous n'aurait pas de sens ici. Gardez simplement à l'esprit que les tests prennent du temps et ne sont pas toujours planifiés.

Quoi qu'il en soit, vous devriez savoir comment écrire des tests unitaires pour votre code et être proactif à leur écriture. Si vous n'avez pas le temps de le faire, vous devriez au moins être conscient que c'est une erreur.

L'Intégration Continue est un processus dans lequel chaque push vers votre dépôt déclenche une build et exécute vos tests automatiquement. Un drapeau rouge est levé dès qu'un commit défectueux est intégré. Les pull requests devraient également être testées automatiquement avant la fusion pour éviter les bugs qui impactent toute l'équipe.

La Livraison Continue est l'extension de l'Intégration Continue. Si les tests passent correctement, la version testée est poussée vers l'environnement de production automatiquement.

Par exemple : chez [Quora](https://www.quora.com/), ils suivent le temps entre un push vers le dépôt et le déploiement de ce code sur les serveurs de production. Le dernier benchmark que j'ai lu était de 15 minutes... pour environ 100 développeurs. C'est la configuration la plus puissante qu'une équipe pourrait espérer.

Les serveurs d'intégration continue populaires sont [Jenkins](https://jenkins.io/), [Travis](https://travis-ci.org/), [CircleCI](https://circleci.com), et quelques autres. Vous n'avez pas besoin de savoir comment configurer le serveur et tout le reste, mais vous devriez savoir que de tels outils existent, et une alerte rouge devrait se déclencher dans votre tête si votre équipe n'en utilise aucun.

### Conclusion

Le cœur du travail d'un développeur est la programmation. Une fois que vous passez de solo/amateur à membre d'une équipe performante, l'utilisation appropriée des outils clés de collaboration est aussi importante que l'écriture de code propre. Espérons que cet article vous a donné un aperçu de ce que sont ces outils et comment creuser davantage pour être le meilleur dans ce que vous faites !

**Merci d'avoir lu ! Si vous trouvez l'article utile, veuillez cliquer sur le bouton d'applaudissements ci-dessous. Cela signifierait beaucoup pour moi et cela aide les autres à voir l'histoire !**