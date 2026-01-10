---
title: Comment utiliser les fonctionnalités natives de GitHub pour aider à gérer une
  équipe distribuée de taille moyenne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:02:43.000Z'
originalURL: https://freecodecamp.org/news/using-github-native-features-for-a-mid-size-distributed-team-3acdfd0f027c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3_KSG37XnfbQIaHf-_-b-A.jpeg
tags:
- name: communication
  slug: communication
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: project management
  slug: project-management
- name: 'tech '
  slug: tech
seo_title: Comment utiliser les fonctionnalités natives de GitHub pour aider à gérer
  une équipe distribuée de taille moyenne
seo_desc: 'By Alex Ewerlöf

  My team created a wiki page in our private Github repo about how we work on a common
  code base. I want to share it with you.

  We’re a team of 15 people with 10 developers, a project manager (PM), a tech lead
  (TL), an engineering manage...'
---

Par Alex Ewerlöf

Mon équipe a créé une page wiki dans notre dépôt GitHub privé sur la façon dont nous travaillons sur une base de code commune. Je veux la partager avec vous.

Nous sommes une équipe de 15 personnes avec 10 développeurs, un chef de projet (**PM**), un responsable technique (**TL**), un responsable ingénierie, un UXer et DevOps répartis dans trois pays européens. Le produit est un SaaS interne basé sur le web utilisé par d'autres équipes au sein de l'entreprise.

### Communication

Nous communiquons principalement via Slack, mais nous avons une rétrospective bihebdomadaire en visioconférence (VC). Nous n'avons pas de standup quotidien, mais nous avons un rappel hebdomadaire pour les tâches de la semaine où chacun peut écrire une mise à jour dans un fil de discussion. L'idée est de transformer les questions du standup pour qu'elles concernent les tâches plutôt que les personnes. Nous avons eu cette idée de l'atelier "Flow" de _Marcus Hammarberg_ :

### Pourquoi ?

À mesure que le projet et l'équipe grandissent, nous pouvons travailler plus efficacement en suivant les problèmes et les PR de manière intelligente.

GitHub dispose de nombreuses fonctionnalités de gestion de projet intégrées. De plus, il est plus facile pour les développeurs d'avoir leur code et leurs tâches au même endroit. Des fonctionnalités comme [la fermeture des problèmes avec des commentaires](https://help.github.com/articles/closing-issues-using-keywords/), [le guide de contribution](https://help.github.com/articles/setting-guidelines-for-repository-contributors/), et [les modèles de problèmes](https://help.github.com/articles/manually-creating-a-single-issue-template-for-your-repository/), [les propriétaires de code](https://help.github.com/articles/about-codeowners/) et ses [intégrations avec d'autres services](https://github.com/marketplace) en font un outil assez utile.

L'idée est de définir une manière souple de gérer le travail sans mettre trop de charge sur le PM/TL tout en obtenant leur contribution lorsque cela est nécessaire.

### Quoi ?

Nous utilisons quelques fonctionnalités natives de GitHub pour organiser les problèmes et avoir une image plus claire de ce qui se passe dans le projet à tout moment.

### Comment ?

Nous utilisons les problèmes, les labels et les jalons de GitHub. Nous n'utilisons pas actuellement les projets GitHub (mais nous utilisons plutôt [Zenhub](https://www.zenhub.com/) comme notre tableau Kanban).

### Quand ?

Nous utilisons des jalons hebdomadaires. Au début de chaque semaine, nous avons une réunion de planification (également en VC) où, avec le PM/TL, nous définissons le jalon hebdomadaire qui est le centre d'attention de l'équipe pour cette semaine.

Nous utilisons des jalons GitHub qui ont des noms comme W22, avec une description de ce qui doit être accompli d'ici la fin de la semaine. Il mentionne également clairement les critères d'acceptation.

À la fin de la semaine, nous avons la démonstration hebdomadaire (également en VC) où nous montrons le résultat et félicitons toute personne qui a fait un travail exceptionnel.

### Problèmes et pull requests atomiques

* Chaque problème doit traiter une seule chose. Si la discussion concernant un problème sort du cadre, créez un autre problème.
* Commencez toujours par un problème plutôt que par une PR. Discutez toujours du problème (dans un problème) avant de soumettre une solution (dans une PR).
* Écrasez les PR lors de la fusion pour garder l'historique de la branche `master` propre et raisonnable.
* Il est bon de pratique d'ajouter des informations de contexte à une PR, mais si vous écrivez trop, cela signifie probablement que vous devez commenter le problème à la place.
* Gardez les discussions dans les problèmes et laissez les priorités être assignées avant de commencer à coder.

### Correspondance 1:1 entre les problèmes et les PR

* Dans le cas rare où vous faites une PR sans problème pertinent, créez un problème et référez-vous à celui-ci dans la description de la PR.
* Il doit y avoir au moins un problème pour chaque PR.
* Il est recommandé que chaque PR ferme un problème.
* Écrivez une brève description de la solution dans la PR et référez-vous au(x) problème(s) pertinent(s).

### Pas de commit direct sur master

* Toutes les modifications de master doivent provenir de PR.
* L'idée est de toujours avoir une branche `master` fonctionnelle.

### Qui ?

Dans notre équipe, nous utilisons une manière lean de prendre en charge les tâches. Une fois qu'elles sont priorisées par le PM, n'importe qui peut prendre une tâche et travailler dessus. Pour signaler que le problème est en cours, vous l'assignez simplement à vous-même.

Nous utilisons la programmation mob pour les tâches plus importantes, et dans ce cas, toutes les personnes impliquées dans la tâche sont assignées. Elles sont également mentionnées dans la description de la PR afin qu'elles reçoivent une mise à jour pour les commentaires sur la PR.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MGMLp6oH0kjAnAjTg6ySCg.jpeg)

### Labels

Lors de la création d'un problème, nous lui assignons les labels pertinents pour un filtrage plus facile. Par exemple, nous pouvons filtrer tous les problèmes liés aux `tests` ou aux problèmes `prio-hi` en un clic ou même enregistrer la requête.

Il existe de nombreux labels, mais ils se divisent essentiellement en les catégories suivantes :

#### Priorisation

Lorsqu'un nouveau problème arrive, il attend jusqu'à ce qu'il soit priorisé par le PM et reçoive l'un de ces labels :

* `prio-high` : tâches de haute priorité qui doivent être faites dès que possible
* `prio-mid` : tâches de priorité moyenne qui peuvent être faites lorsqu'il n'y a pas de tâches de haute priorité
* `prio-low` : tâches de faible priorité qui peuvent attendre
* `on-hold` : les tâches que nous ne ferons pas jusqu'à nouvel ordre

Si un problème n'a aucun de ces labels, il ne doit pas être travaillé. Le PM peut changer la priorité d'un problème en fonction des changements dans les besoins des parties prenantes.

Lorsqu'un problème a un jalon, il est prêt à être développé. Tous les autres problèmes qui ne sont pas dans un jalon sont dans le "backlog". Les problèmes peuvent être assignés au jalon hebdomadaire d'une semaine à venir. Si vous ne pouvez pas contribuer au jalon de cette semaine, peut-être pouvez-vous vous préparer pour la semaine prochaine en faisant une partie de ce travail.

N'importe qui peut créer un problème. En fait, une question peut être un problème, si vous pensez que c'est le meilleur moyen d'obtenir des réponses. Un problème ne se convertira pas automatiquement en tâche tant qu'il n'a pas été priorisé (a reçu un label `prio-*`) et ajouté à un jalon.

#### Taille

* `EPIC` : est un problème qui peut conduire à plusieurs PR et doit être décomposé en problèmes `atomiques` avant d'être implémenté.
* `atomic` : est un problème qui peut être implémenté seul et conduira à une PR.

#### Groupement

Nous utilisons également des labels pour regrouper des problèmes similaires ou signaler différents aspects d'un problème ou d'une PR. Un problème peut avoir n'importe quel nombre de ces flags :

* `tooling` les problèmes qui concernent le système de build, le linting, les outils de test...
* `test` les problèmes concernant les tests et l'assurance qualité
* `ux` les problèmes qui nécessitent un travail UX, améliorent l'UX ou affectent l'UX d'une certaine manière
* `config` les problèmes liés aux changements de configuration
* `doc` les problèmes concernant la documentation (commentaires dans le code ou documentation publiée comme wiki)
* `perf` : suggestions pour la surveillance et l'amélioration des performances
* `dx` : éléments qui améliorent l'expérience des développeurs comme le logging, etc.
* `security` : problèmes de sécurité ou améliorations de sécurité.
* `discussion` : nous n'avons pas encore atteint un consensus, peut-être pouvez-vous contribuer ?
* `help needed` : le problème a besoin d'aide de la part d'équipes externes (si vous attendez un bénévole interne, vous pouvez simplement aller de l'avant et le mentionner). Ces problèmes sont généralement de bons candidats pour que le PM/TL facilite la communication inter-équipes.
* `feature` : pour introduire de nouvelles fonctionnalités
* `bug` : pour les rapports de bugs
* d'autres labels peuvent être ajoutés si nous avons suffisamment de problèmes qui correspondent à un certain label.

### Ce que GitHub ne peut pas faire

Malheureusement, l'outil actuel de GitHub est insuffisant pour au moins deux choses importantes :

1. Il n'y a pas de moyen facile de regrouper les problèmes sous (Epics). Nous avons utilisé des labels pendant un certain temps, mais c'était sous-optimal.
2. En dehors de l'utilisation des labels, il n'y a pas de moyen de prioriser les problèmes. Nous avons besoin d'un outil où l'ordre des problèmes peut montrer leur importance.

Ces deux problèmes sont résolus par [Zenhub](https://www.zenhub.com/), qui est une extension Chrome/Firefox enrichissant l'interface native de GitHub. Il dispose également d'un service hébergé pour ceux qui n'utilisent pas Chrome/Firefox.

Le seul domaine où Zenhub est encore insuffisant est la définition d'une limite sur le travail en cours ([WIP limit](https://github.com/ZenHubIO/support/issues/272)).