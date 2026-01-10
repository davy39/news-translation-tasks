---
title: Qu'est-ce que l'Agile et comment devenir un conteur épique
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-12T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-agile-and-how-youcan-become-an-epic-storyteller
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/intro-to-agile-1.jpg
tags:
- name: Software Requirements
  slug: software-requirements
- name: agile
  slug: agile
- name: agile development
  slug: agile-development
- name: 'development process '
  slug: development-process
- name: project management
  slug: project-management
- name: Scrum
  slug: scrum
- name: software
  slug: software
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Qu'est-ce que l'Agile et comment devenir un conteur épique
seo_desc: Running a team of developers is hard. Trying to coordinate a mountain of
  work while keeping everyone productive is a challenge itself. But on top of that,
  you have to keep open communications with a client. How can we use agile to relieve
  some of tho...
---

Diriger une équipe de développeurs est difficile. Essayer de coordonner une montagne de travail tout en gardant tout le monde productif est un défi en soi. Mais en plus de cela, vous devez maintenir une communication ouverte avec un client. Comment pouvons-nous utiliser l'agile pour soulager certains de ces points de douleur ?

* [Qu'est-ce que l'agile ?](#heading-quest-ce-que-lagile)
* [Quels sont quelques concepts que vous devriez connaître ?](#heading-quels-sont-quelques-concepts-que-vous-devriez-connaître)
* [Histoires](#heading-histoires)
* [Épiques](#heading-épiques)
* [Sprints](#heading-sprints)

%[https://www.youtube.com/watch?v=1GPYnoG_nkE]

## Qu'est-ce que l'agile ?

Agile est une méthodologie de développement de logiciels qui découle de l'idée de diviser de grandes quantités de travail en morceaux plus petits. Cela donne aux chefs de produit, aux développeurs et à toute partie prenante une meilleure compréhension du travail.

Historiquement, le développement de logiciels était un processus lent où des changements majeurs dans les exigences pouvaient mettre une grande pression sur les équipes.

En suivant la méthodologie agile, les plus petits morceaux de travail aident les équipes à devenir plus flexibles, et oserais-je dire _agiles_. Et dans le processus, cela les aide à livrer des fonctionnalités plus rapidement et à répondre aux changements plus rapidement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-project-board.jpg)
_Exemple de tableau de projet Jira de [atlassian.com/software/jira](https://www.atlassian.com/software/jira)_

Ces idées ont été divisées en différents frameworks pour aborder cette méthodologie. Deux des plus courants sont [Scrum](https://www.scrum.org/resources/what-is-scrum) et [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)).

Pour ce guide, la plupart de ces concepts suivent le framework Scrum, mais il y a certainement des concepts qui s'appliquent aux deux et à d'autres.

## Quels sont quelques concepts que vous devriez connaître ?

Je dirais que la moitié de la productivité en tant que développeur dans un monde agile est simplement de comprendre les termes. Typiquement, le chef de projet dirige le spectacle, donc si vous pouvez être sur la même longueur d'onde que ce dont ils parlent, cela rendra le processus beaucoup plus facile.

Il existe des livres, des cours et des certifications basés sur l'apprentissage des nuances de la méthodologie agile. Je ne vais pas approfondir certains des aspects philosophiques ou certaines des parties plus profondes, mais je vais couvrir un bon ensemble de concepts clés qui vous aideront à vous lancer lorsque vous commencerez votre nouvel emploi avec une équipe agile.

## Histoires

Une histoire est typiquement le plus petit morceau de travail défini. Cela prend généralement la forme d'un nouveau ticket que vous créez dans l'outil de projet que vous utilisez, qu'il s'agisse de [Jira](https://www.atlassian.com/software/jira) ou même de [Github Issues](https://help.github.com/en/github/managing-your-work-on-github/about-issues).

### Exprimer des histoires

En travaillant sur un projet, vous rencontrerez probablement une variété de façons dont les gens expriment des histoires. Mais une bonne ligne directrice est de travailler à travers le concept du mot "histoire" lui-même et d'expliquer le travail qui doit être fait de cette manière.

Par exemple, si vous souhaitez offrir la possibilité aux personnes qui utilisent votre site web de partager un article de blog sur Twitter, vous pourriez vouloir écrire l'histoire comme suit : En tant que lecteur, je veux partager l'article que je viens de lire sur Twitter.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-story-summary.jpg)
_Création d'une nouvelle histoire dans Jira_

L'utilisation de ce modèle "en tant que [personne], je veux [action]" aide à fournir un contexte sur l'état dans lequel quelqu'un pourrait se trouver lors de la visite de leur site et ce qu'ils essaient d'accomplir. Cela peut être particulièrement utile si vous développez des fonctionnalités pour des personnes connectées qui sont différentes des invités.

### Détails et exigences

Bien que le titre d'une histoire soit une représentation importante du travail, vous voudrez également fournir des détails supplémentaires.

Au minimum, cela devrait être fait en ajoutant une description approfondie et un ensemble de critères d'acceptation qui peuvent aider à donner au développeur un contexte et des exigences. Selon l'équipe, cela peut également inclure des outils comme des tags ou des catégorisations qui facilitent la visualisation des groupes de travail pour l'équipe.

Fournir un ensemble solide d'exigences aide à la fois le développeur travaillant sur l'histoire et la personne qui la révise à avoir une mesure pour déterminer si elle est réellement complète. Sans cela, tout le monde ne fait que deviner.

Une bonne façon de formuler celles-ci est : vérifier [exigence]. Revenons à mon exemple de partage d'un article sur Twitter, peut-être que certaines des exigences de cette histoire seraient :

* Vérifier que lorsqu'on clique sur le bouton de partage, un nouveau tweet est créé
* Vérifier que le tweet inclut un lien vers l'article de blog actuel

### Quantité de travail ou niveau de difficulté

Chaque histoire est représentée par un nombre de points. Ces points sont un moyen d'exprimer combien d'efforts une équipe de développeurs prévoit pour une histoire. Cet effort peut signifier une variété de choses, qu'il s'agisse simplement de la difficulté à laquelle l'équipe s'attend pour le travail ou de la quantité de risque ou d'incertitude qu'une histoire particulière comporte.

Une façon dont les équipes représentent cela est avec la [suite de Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number), où la quantité de points peut être de 1, 2, 3, 5, 8, etc. Où une mise à jour de texte négligeable pourrait être de 1 point, l'ajout d'un nouveau formulaire à une page pourrait être de 3 points.

Typiquement, vousoudrez éviter de pointer les histoires trop haut, car au-dessus de 5 points, il est plus que probable qu'il y ait un moyen de diviser le travail pour le rendre plus gérable. Bien que vous puissiez facilement créer une histoire massive de 13 points pour accomplir tous les aspects d'une fonctionnalité, il est généralement plus judicieux de s'attaquer au travail en morceaux plus petits et plus ciblés.

Dans tous les cas, tous ces points s'additionnent pour donner à votre équipe une estimation approximative de la quantité de travail qu'un groupe d'histoires prendrait pour être complété.

## Épiques

Alors que les histoires ont pour objectif de définir un morceau de travail de taille réduite, les épiques sont un moyen de regrouper ces morceaux de travail pour représenter une fonctionnalité.

### Définir des histoires en tant que fonctionnalité

Une bonne façon d'expliquer cela est avec un autre exemple. Si vous travaillez sur une application qui nécessite l'intégration de l'authentification, vous pourriez vouloir créer une nouvelle épique simplement appelée "Authentification".

À l'intérieur de cette épique, vous pourriez trouver des histoires comme :

* En tant qu'invité, je veux me connecter à l'application avec mon adresse e-mail
* En tant qu'utilisateur authentifié, je veux changer mon mot de passe
* En tant qu'équipe de sécurité, je veux prévenir le spam et les abus d'authentification des utilisateurs

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-epic-authentication.jpg)
_Exemple d'une épique d'authentification dans Jira_

Avec votre épique définie, vous donnez à votre équipe un chemin pour appeler une fonctionnalité complète tout en comprenant l'ensemble de la portée de ce travail. Cela est important lorsqu'il s'agit de planifier le travail à faire.

Définir vos histoires dans votre épique vous donne une idée de la quantité de travail que quelque chose prend, mais cela ne vous aide pas à déterminer combien de temps cela prendrait, c'est là que les sprints interviennent.

## Sprints

Les sprints sont un moyen de planifier comment le travail sera réellement accompli. Bien que similaires aux épiques en ce sens qu'ils sont un moyen de regrouper des morceaux de travail, les sprints représentent généralement une période de temps au cours de laquelle un morceau de travail particulier sera fait.

### Temps par sprint

Une façon courante de définir un sprint est de deux semaines de travail. Pendant ces deux semaines, votre équipe aura une vélocité particulière, ou une quantité moyenne de travail que vous pouvez accomplir, pour un sprint individuel. Cette vélocité est représentée par un nombre de points qui est la somme de la vélocité moyenne de chacun des développeurs travaillant sur ce sprint.

### Points par sprint

Bien que beaucoup argumentent fermement que vous ne devriez pas utiliser le temps pour représenter cette vélocité, les points se traduiront approximativement par une quantité moyenne de temps de travail pour chaque développeur. Alors qu'1 point pour un développeur expérimenté pourrait être 1 heure, ce même 1 point pourrait signifier 3 heures pour un développeur moins expérimenté.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/jira-project-roadmaps.jpg)
_Exemple de feuille de route de projet de [atlassian.com/software/jira](https://www.atlassian.com/software/jira)_

Mais une fois que vous avez ce nombre de points que votre équipe moyenne en un sprint, vous saurez combien de points d'histoire vous pouvez vous attendre à planifier pour être complétés. Cette planification se fait de sprint en sprint alors que vous répartissez un groupe d'histoires ou une épique afin que vous puissiez prédire quand une fonctionnalité sera complète.

## Comment l'agile s'intègre avec votre équipe

Essayez de vous rappeler que la méthodologie Agile à travers Scrum, Kanban, ou tout autre framework n'est que cela - un framework. Bien qu'il soit probablement bon de suivre le processus lorsque vous commencez, écoutez votre équipe et essayez de le modeler selon vos propres expériences.

Chaque équipe travaille un peu différemment et forcer un processus sur cette équipe peut causer plus de tort que de bien, mais il y aura toujours une courbe d'apprentissage pour tout processus. Combattez les yeux qui roulent jusqu'à ce que tout le monde s'y habitue et organisez des rétrospectives fréquentes pour voir ce qui fonctionne et ce qui ne fonctionne pas.

À la fin de la journée, les processus que votre équipe suit devraient être principalement invisibles, travaillant pour vous au lieu de contre vous. Trouvez ce qui fonctionne le mieux pour votre équipe et partagez vos expériences pour que les autres apprennent !

## Quel est le processus de votre équipe ?

[Partagez avec moi sur Twitter !](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?F5F9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4E8F5F9 Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>