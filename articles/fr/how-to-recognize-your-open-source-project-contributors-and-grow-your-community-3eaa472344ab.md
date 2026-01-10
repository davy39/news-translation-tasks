---
title: Comment reconnaître les contributeurs de votre projet open source et développer
  votre communauté
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T18:01:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-recognize-your-open-source-project-contributors-and-grow-your-community-3eaa472344ab
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4y_hyryvT4SZ0wKa
tags:
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment reconnaître les contributeurs de votre projet open source et développer
  votre communauté
seo_desc: 'By David Herron

  There’s a truism — if a community is not growing, it is slowly dying. How is your
  open source community doing? Is your contributor base stagnant, shrinking or growing?
  Are you like many open source community leaders with little idea o...'
---

Par David Herron

Il existe une vérité universelle — si une communauté ne grandit pas, elle meurt lentement. Comment se porte votre communauté open source ? Votre base de contributeurs est-elle stagnante, en déclin ou en croissance ? Êtes-vous comme de nombreux leaders de communautés open source, avec peu d'idées sur la manière d'encourager de nouvelles participations ?

Il existe de nombreuses opinions sur la manière de stimuler l'activité autour d'un projet open source. Construire avec succès un projet open source piloté par la communauté ne se limite pas à publier votre code sur GitHub et à développer en public.

Les gens doivent savoir que le projet existe, que vous êtes ouvert aux contributions, quel est le processus de contribution, les pratiques de codage du projet, et ainsi de suite.

Une tactique très visible consiste à établir ce que certains appellent une "preuve sociale". C'est-à-dire, un indicateur visuel que le projet reçoit actuellement des contributions.

Que signifie le mot "communauté" dans ce contexte ?

Une "communauté" est un groupe de personnes qui se réunissent pour un objectif ou un but commun. Le sens traditionnel est celui des personnes vivant dans une ville, et leur objectif commun est de vivre ensemble en paix dans cette ville.

Mais les communautés peuvent se former pour d'autres raisons. Par exemple, un groupe Facebook sur les motos électriques hébergera des discussions sur les marques de motos électriques, les endroits où rouler, comment entretenir ou personnaliser les motos, etc. À mesure que les membres se connaissent en discutant des motos électriques, ils forment une communauté.

De même, les personnes qui maintiennent un projet de logiciel open source forment également une communauté dont le but est d'améliorer ce logiciel. Cet article se concentre sur un aspect de l'augmentation de la participation communautaire dans un projet open source — reconnaître ceux qui contribuent au projet.

De nombreux sites de projets ont des "widgets" affichant des données comme l'état de la construction, si les tests passent, et ainsi de suite. Et si un autre widget montrait un indicateur des contributeurs au projet ? À savoir :

* Une liste de personnes faisant des contributions de code — démontrant au public que ce projet a des contributeurs
* Donner des félicitations aux contributeurs, afin qu'ils puissent avoir des droits de vantardise et se sentir appréciés
* Montrer qu'il y a une propriété communautaire du projet
* Montrer qui a quelle part dans le projet
* Dire au public que ce projet n'est pas l'idée farfelue d'un seul individu qui code selon ses envies

L'existence de widgets d'état de construction et similaires démontre une place pour des widgets automatiquement mis à jour donnant des données sur les projets open source. Ces widgets sont conçus pour le public, et leur but est de rassurer les utilisateurs ou contributeurs potentiels que le projet dispose d'un système de construction et de test automatisé, et que l'état actuel est vert.

Mais ce n'est pas le seul type de système d'état qu'une équipe de projet peut utiliser. À des fins de gestion d'équipe, une équipe peut utiliser un tableau de bord privé donnant l'état de divers aspects de leur projet. Les projets de logiciels commerciaux font régulièrement cela. Les tableaux de bord sont maintenus par le chef de produit pour mesurer les progrès vers les objectifs. Cet article ne parle pas de ce type de système d'état, mais plutôt d'un système qui est montré au public.

N'est-il pas rassurant de savoir qu'un projet open source est piloté par une équipe ? Qu'il y a plus d'une paire d'yeux qui cherchent des bugs ? Que la direction n'est pas le délire d'une seule personne mais pilotée par un processus collaboratif ? Si vous cherchez à intégrer un outil open source dans le logiciel qui fait tourner votre entreprise, n'avez-vous pas besoin de savoir que l'outil a un avenir stable ?

Réfléchissons d'abord à un widget d'état qui fait certaines des choses ci-dessus. Ensuite, regardons ce que font certains projets open source importants dans ce domaine. Enfin, cherchons s'il existe un outil existant de cette nature.

### Remue-méninges

En général, nous parlons d'un "widget d'état" à installer sur les pages de projet, comme le dépôt de code source. Le widget doit présenter certaines données sur les contributeurs du projet open source, et mettre en œuvre autant d'idées que possible parmi celles ci-dessus. Voici quelques attributs possibles à afficher :

* Facile à installer — insérer un widget HTML dans les sites web
* Récupérer automatiquement les données des commits Github/Gitlab/etc
* Identifier le type, la taille, etc., des changements de code dans les commits
* Présenter les données des contributeurs sous plusieurs formes (personnalisabilité)
* Présenter des informations utiles sur chaque contributeur
* Présenter des informations utiles sur le total des contributions
* Être totalement objectif dans la liste des contributeurs

### Actions de certains projets open source pour reconnaître les contributeurs

Puisqu'il est utile de regarder autour de soi et de voir ce que font les autres, examinons certains projets open source de haut profil. Que font-ils en termes de reconnaissance des contributeurs ?

![Image](https://cdn-media-1.freecodecamp.org/images/Q4ApyCiQwPu6FgdgSTKvnBzFQqBv7ubTxZG9)

[**Vue.js**](https://github.com/vuejs/vue) — Ce framework UI de premier plan pour les applications web modernes dispose d'un widget "Contributeurs" qui renvoie à une page GitHub affichant les [données de contribution de code Vue.js](https://github.com/vuejs/vue/graphs/contributors). Le widget des contributeurs est dérivé d'un widget [OpenCollective](https://opencollective.com/vuejs) montrant les "soutiens" du projet Vue.js. Cela montre les contributeurs financiers. Les avatars ne correspondent pas nécessairement aux contributeurs de code du projet.

![Image](https://cdn-media-1.freecodecamp.org/images/moMCsgpU77dEhhZZzCwZWmBX9ITffZ8AzBw5)

[**ReactJS**](https://reactjs.org/) — Ce framework UI de premier plan pour les applications web modernes dispose d'une zone Contributeurs bien développée. Mais nulle part n'a été trouvée une liste ou une reconnaissance des contributeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/heHQ4uxSD0Vio8Ml0A8RP0QAKSEithTjh-3d)

[**Bootstrap**](https://github.com/twbs/bootstrap) — Ce framework UI réactif de premier plan dispose d'une zone Contributeurs bien développée. Sur la page principale du dépôt sont mentionnés Mark Otto et Jacob Thornton comme les créateurs. Sous "Copyright", il est mentionné que la propriété est partagée entre Twitter et "The Bootstrap Authors". Ces derniers renvoient à la liste des contributeurs générée par GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/ugQVI44EsOks7Idb3cegcM0c5KPqIOatZg-x)

[**Webpack**](https://webpack.js.org/) — La page d'accueil du projet montre plusieurs listes de contributeurs financiers. Chacune est générée par OpenCollective. Sur le [dépôt du projet Webpack](https://github.com/webpack/webpack), il est clair qu'il existe une zone Contributeurs bien développée. Il comprend également un lien vers une publication Medium. Ils y publient des informations sur la manière de contribuer au projet Webpack. Les seules personnes mentionnées ici sont l'équipe principale de Webpack. Encore une fois, les listes de contributeurs financiers générées par OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/3PiDzuv4oAthFV3MFpCCYvtPTGa41qDPrF4l)

[**jQuery**](https://jquery.com/) — Cette bibliothèque extrêmement populaire pour la manipulation du DOM dans les navigateurs web dispose d'un [guide des contributeurs très développé](https://contribute.jquery.org/). Rien n'a été trouvé listant les contributeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/FqjvoLHaDPjoQy8oEuemMhog8k2ZjsvHJtAb)

[**ExpressJS**](https://github.com/expressjs/express/) — Ce framework populaire pour le développement d'applications web avec Node.js. Il montre TJ Hollowaychuk comme l'auteur original et Douglas Wilson comme le mainteneur actuel du projet. Il renvoie ensuite à la liste des contributeurs générée par GitHub. Il est clair à partir de cette liste que ces deux personnes ont fait l'écrasante majorité des contributions de code au projet.

![Image](https://cdn-media-1.freecodecamp.org/images/ItB6IMsKyiOJ1LopxoqLAT8-7oXsVoN0IZzr)

[**Node.js**](https://nodejs.org/en/) — Cette plateforme populaire pour le développement JavaScript en dehors des navigateurs web dispose d'une Fondation et d'un ensemble très structuré de mainteneurs. Le Node.js Technical Steering Committee a l'autorité finale sur la direction technique et la gouvernance. Il existe une [liste maintenue manuellement des membres du TSC](https://github.com/nodejs/node/blob/master/README.md#tsc-technical-steering-committee) dans le dépôt. Une autre liste maintenue manuellement contient [les autres collaborateurs](https://github.com/nodejs/node/blob/master/README.md#current-project-team-members). Ces listes sont répliquées sur la [page d'accueil principale du dépôt Node.js](https://github.com/nodejs/node).

Aux côtés du TSC se trouve le [Community Committee](https://github.com/nodejs/community-committee) qui se concentre sur les "efforts orientés communauté". Une liste maintenue manuellement des membres du Community Committee se trouve dans le dépôt de ce projet.

Un point à noter concernant ces listes maintenues manuellement est qu'elles se trouvent dans le dépôt Git du projet. Le processus pour démissionner de l'une de ces équipes consiste à émettre une Pull Request contre cette page en annonçant l'intention de démissionner de l'équipe du projet. C'est une utilisation intéressante de Git, pour suivre les membres du projet au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/cjbqk2D-6DF2j9f1pNoaoBQEvTEXfYQJ09ez)

[**Django**](https://www.djangoproject.com/) — Ce framework Python populaire pour le développement d'applications web dispose à la fois d'une Fondation pour gérer les affaires commerciales, et de quelques équipes techniques pour les affaires techniques. [Les membres de l'équipe technique sont publiés sur le site web du projet](https://www.djangoproject.com/foundation/teams/). Il existe un guide des contributeurs bien développé.

![Image](https://cdn-media-1.freecodecamp.org/images/qp4fEmsYFD7W30dzhhfOx5FRpZ8gp7loVjxj)

[**Cheerio**](https://www.npmjs.com/package/cheerio) — Ce projet Node.js populaire implémente un sous-ensemble de l'API jQuery pour s'exécuter sur le projet Node.js pour la manipulation du DOM côté serveur. Le fichier README du projet inclut une liste de contributeurs générée en exécutant des commandes Git. Cela en fait une liste générée automatiquement, mais l'expérience utilisateur est assez mauvaise. Le [dépôt GitHub](https://github.com/cheeriojs/cheerio) montre des listes de contributeurs financiers générées par OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/sSP6E0Piqq-Y4bGYAwzpTKytYJCYklSUVvmS)

[**BabelJS**](https://babeljs.io/) — Cet outil de développement JavaScript populaire est un transpileur qui nous permet d'utiliser JavaScript moderne tout en déployant dans des environnements plus anciens. Le site web dispose d'une page "Rencontrez l'équipe" très complète. Cette page liste une large gamme de contributeurs, y compris un contributeur non humain (un bot Twitter). Le dépôt GitHub contient une liste de sponsors financiers générée par OpenCollective.

![Image](https://cdn-media-1.freecodecamp.org/images/M8Z9rRyZCR58CyNTkW5hTW7HRuTwN7ANNedJ)

[**Rust**](https://www.rust-lang.org/) — Ce nouveau langage de programmation système promet une exécution ultra-rapide, pas de segfaults, une sécurité des threads, et plus encore. La [page de l'équipe](https://www.rust-lang.org/en-US/team.html#Community) semble être maintenue manuellement et liste une douzaine d'équipes soutenant Rust. Chaque équipe compte une douzaine de membres ou plus.

### Outils pour reconnaître automatiquement les contributeurs

Nous avons appris dans la section précédente que la plupart des projets open source tentent de reconnaître les contributeurs et les membres de l'équipe principale. Mais que dans la plupart des cas, cela se fait avec des listes maintenues manuellement.

Maintenir manuellement une liste de contributeurs est une charge administrative. Cela peut créer une situation où un contributeur n'est pas reconnu parce que personne n'a pensé à l'ajouter à la liste. Tout comme nous nous efforçons d'automatiser les tests logiciels pour garantir de bons processus de développement, nous pourrions également nous efforcer d'automatiser la reconnaissance des contributeurs pour garantir que chacun soit reconnu équitablement. Examinons plusieurs façons de mettre en œuvre un widget automatisé.

**Utiliser la liste de contributeurs générée automatiquement sur GitHub ou GitLab :** Chaque projet GitHub dispose d'une page facilement accessible montrant les contributions. Les projets hébergés sur GitLab disposent d'une page similaire, plus difficile à atteindre. Certains projets se contentent de lier ces pages. La page GitHub est assez utile, mais ce n'est pas la même chose qu'un widget d'état.

**Créer votre propre liste :** En utilisant les commandes git (_git shortlog -sn_), il est possible de générer une liste de committers. Un programmeur inventif pourrait transformer cela en une liste d'avatars.

Nous avons trouvé un projet plus ancien (semblant abandonné) qui faisait exactement cela : [https://github.com/blossom/contributors](https://github.com/blossom/contributors)

**Le Widget OpenCollective :** [Open Collective](https://opencollective.com/) est une sorte de mouvement social destiné à créer des projets financés ouvertement. C'est une idée intéressante et digne d'être explorée plus avant. Pour les besoins de cet article, l'équipe Open Collective propose un widget dynamique facile à installer sur un site web, qui montre les contributeurs. De nombreux projets open source sont des projets Open Collective et utilisent ce widget. Cependant, dans ce cas, "contributeur" signifie des contributions financières plutôt que des contributions de code.

**Sourcerer.io Hall of Fame :** [Sourcerer.io](https://sourcerer.io) est un service qui génère automatiquement une page de profil pour les ingénieurs logiciels en fonction de leurs commits de code source. Il prend en charge la génération d'un profil personnel à partir de n'importe quel ensemble de dépôts git. GitHub et GitLab bénéficient du meilleur support. Par exemple, voir mon profil [https://sourcerer.io/robogeek](https://sourcerer.io/robogeek).

L'outil Sourcerer.io _Hall of Fame_ génère un résumé des committers des projets GitHub. Il récupère l'avatar de l'utilisateur, soit à partir d'un profil Sourcerer, soit d'un profil GitHub. L'installation est très simple une fois que vous avez un compte Sourcerer. Rendez-vous dans l'onglet Hall of Fame de la zone Paramètres et suivez les instructions. Le service de Sourcerer s'occupe du reste.

Le [dépôt GitHub](https://github.com/sourcerer-io/hall-of-fame) associé contient quelques exemples de widgets Hall of Fame, tels que [iterative/dvc](https://github.com/iterative/dvc) et [epicmaxco/vuestic-admin](https://github.com/epicmaxco/vuestic-admin).

### Conclusion / Observations

Nous avons commencé cet article en théorisant que la reconnaissance publique des contributeurs à un projet open source aiderait le projet à croître. L'idée semble solide, mais nous ne savons pas si elle est vraie. Ce que nous avons appris, c'est que de nombreux projets open source ont déjà des méthodes pour reconnaître les contributeurs (particulièrement ceux qui ne semblent pas être soutenus par des entreprises — par exemple, ReactJS).

Toutes les contributions ne sont pas sous forme de logiciels. Certains projets ont des équipes pour le marketing, la documentation, les tests ou la sécurité. Un outil automatisé qui analyse les commits Git ne pourra pas lister les personnes faisant des contributions non codantes au projet. Ces contributions n'atterrissent pas dans un dépôt Git. Par conséquent, un outil pour générer un widget de contributeurs pour les contributions de source a un champ d'application limité. En listant les contributions de code, le widget ne liste pas les autres contributeurs.

La principale tactique de reconnaissance parmi les projets open source que nous avons examinés est la maintenance manuelle de listes de membres d'équipe. Un projet peut avoir une ou plusieurs "équipes" affectées à différents domaines. Bien sûr, certaines de ces équipes se concentrent sur des travaux non codants. Ces listes d'équipes reconnaissent les contributeurs non codants ainsi que les codeurs.

Une autre tactique courante consiste à reconnaître les contributions financières à l'aide du widget OpenCollective. Il est facile à installer et les systèmes d'OpenCollective s'occupent de la mise à jour des widgets. Bien sûr, il a un champ d'application limité. Il ne sert pas à reconnaître les contributions de code à un projet.

Nous avons commencé en notant que de nombreuses équipes disposent de widgets d'état automatisés, et en réfléchissant à un widget d'état pour les contributeurs de code. Bien qu'il soit possible de créer son propre widget d'état de contributeurs de code, la méthode la plus simple consiste à installer le widget Sourcerer.io _Hall of Fame_. Il est facile à installer et se gère lui-même. Il montre de manière concise certains des contributeurs d'une manière qui s'intègre parfaitement à côté des autres widgets d'état. Gardez à l'esprit que cela ne montre que les contributeurs de code.

Reconnaître les membres de l'équipe n'est pas la seule étape pour construire un projet open source actif avec plusieurs contributeurs. Les conseils que nous avons [trouvés](https://sudarmuthu.com/blog/how-to-encourage-contribution-in-open-source-projects/) se concentrent davantage sur le fait d'avoir un processus de contribution bien documenté, par exemple. Il existe de nombreux aspects à la construction et à l'entretien d'une communauté de personnes travaillant ensemble sur un objectif. Évidemment, donner de la reconnaissance en est un.

Dans cet esprit, un widget d'état de contributeurs de code automatisé devrait être l'un des nombreux outils utilisés pour encourager les contributions à votre projet open source.