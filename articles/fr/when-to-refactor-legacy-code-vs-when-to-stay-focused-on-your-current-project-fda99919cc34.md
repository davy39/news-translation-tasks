---
title: Quand refactoriser du code hérité et quand rester concentré sur votre projet
  actuel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T21:14:01.000Z'
originalURL: https://freecodecamp.org/news/when-to-refactor-legacy-code-vs-when-to-stay-focused-on-your-current-project-fda99919cc34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qw5zQRKKw4pNbhv3nwjIjQ.png
tags:
- name: Developer
  slug: developer
- name: General Programming
  slug: programming
- name: refactoring
  slug: refactoring
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Quand refactoriser du code hérité et quand rester concentré sur votre projet
  actuel
seo_desc: 'By Sihui Huang

  When I work on projects, I often run into legacy code that can be improved — to
  be more readable, more testable, or more compliant with the current coding style.
  My urge to refactor the code is especially strong after spending a good a...'
---

Par Sihui Huang

Lorsque je travaille sur des projets, je tombe souvent sur du code hérité qui peut être amélioré — pour être plus lisible, plus testable ou plus conforme au style de codage actuel. Mon envie de refactoriser le code est particulièrement forte après avoir passé beaucoup de temps à essayer de comprendre un morceau de code obscur. [Ce code fait mal à mon cerveau](https://www.sihui.io/brain-friendly-code/), et je ne veux pas que la même chose arrive à d'autres développeurs. Il y a (l'adaptation de) la célèbre règle des Scouts : **Laissez le code meilleur que vous ne l'avez trouvé.**

Mais en même temps, je veux aussi rester concentré et faire avancer mes projets actuels. Je crains de me laisser distraire et de passer trop de temps à refactoriser.

C'est un dilemme auquel je suis souvent confronté. **Je veux être le bon samaritain qui laisse le code meilleur que je ne l'ai trouvé, un ingénieur qui transforme tout le code désordonné que je rencontre en quelque chose de propre et d'élégant. Mais je veux aussi rester pragmatique et livrer des projets rapidement.**

Équilibrer la refactorisation du code hérité que je rencontre et rester concentré sur mon projet actuel peut être difficile.

Une conversation récente avec mon manager sur ce sujet m'a fourni des conseils pour trouver cet équilibre. Voici quelques points que je trouve utiles.

#### **Vous n'avez pas à rendre le code parfait. Les petites améliorations sont toujours utiles.**

Après avoir lu un morceau de code hérité, mon cerveau pense immédiatement à la manière dont il devrait être idéalement. Mais refactoriser ce code de son état actuel à l'état idéal nécessite parfois une refactorisation extensive. Au mieux, la refactorisation requise peut être chronophage. Au pire, elle peut se transformer en un trou noir qui cause un grand retard sur le projet.

Lorsque je suis confronté à des cas comme celui-ci, j'avais l'habitude de soit prendre un risque et faire la refactorisation extensive de toute façon, soit de me boucher le nez et de laisser le code rester désordonné. Maintenant, je réalise qu'il y a un juste milieu : **Je n'ai pas à rendre le code parfait. Je peux passer autant ou aussi peu de temps que je peux me permettre pour améliorer un peu le code.**

Les petites améliorations que je fais peuvent encore être utiles pour les développeurs qui viennent après. Et ces développeurs peuvent avoir le temps d'améliorer davantage le code, en s'appuyant sur les améliorations que j'ai faites.

(PS : Il n'y a pas de code parfait ni idéal. Le moment où vous faites un changement, vous voyez plus d'améliorations que vous pouvez faire.)

#### **Limitez le temps de votre refactorisation.**

La limitation de temps est une excellente technique pour éviter les trous noirs. Avant de commencer à refactoriser, faites une estimation rapide du temps que vous pouvez passer à refactoriser le code hérité sans trop retarder le projet. Notez ce nombre.

Limiter le temps de votre refactorisation vous donne la tranquillité d'esprit de savoir que le projet principal restera sur la bonne voie. Et cela rend l'expérience de refactorisation plus agréable.

#### **Intégrez le temps de refactorisation dans l'estimation du projet.**

Les choses peuvent être encore plus faciles si vous intégrez le temps de refactorisation dans l'estimation du projet avant de commencer un projet. Tout en estimant le temps qu'un projet pourrait prendre, jetez un coup d'œil rapide au code que vous devez toucher : quand a-t-il été écrit pour la première fois ? À quel point est-il lisible et extensible ? Quelle est sa couverture de tests ? Sauf s'il y a une exigence stricte sur le moment où le projet doit être livré, vous devriez intégrer un peu de temps de refactorisation dans le calendrier du projet.

Après tout, **à mesure que nous continuons à construire sur une base de code hérité, la refactorisation au fur et à mesure est la meilleure façon de la garder saine.** Et une base de code saine, à son tour, rend la construction de nouvelles fonctionnalités plus rapide et plus sûre.

#### **La refactorisation est éducative.**

Refactoriser un morceau de code est la meilleure façon de le comprendre. Comparé à rester à l'écart et à simplement lire un morceau de code, venir et le modifier vous donne une relation beaucoup plus profonde et intime avec le code.

Lorsque vous essayez d'ajouter votre touche au code, vous commencerez à remarquer des choses que vous avez manquées auparavant. Vous pourriez voir les contraintes et comprendre même pourquoi l'auteur a initialement écrit le code de cette manière.

**Bien que la refactorisation d'un morceau de code ne semble pas ajouter de valeur immédiate à l'entreprise, c'est une opportunité pour vous d'acquérir une connaissance du domaine que vous n'avez pas actuellement.** Acquérir cette connaissance du domaine est inestimable pour vous et pour l'entreprise.

#### **La refactorisation est un muscle que vous pouvez développer**

**Plus vous le faites, plus vous devenez rapide.** Une dernière raison de refactoriser le code hérité est de l'utiliser comme une opportunité de renforcer votre « muscle de refactorisation ». Investir dans le développement de votre « muscle de refactorisation » a un effet composé auto-renforçant : **plus vous refactorisez, meilleur vous êtes en refactorisation, rendant votre prochaine refactorisation plus rapide.** Plus vous le faites, meilleure est la base de code, rendant la construction de futures fonctionnalités plus rapide.

Heureusement, mon prochain projet concerne du code d'il y a presque trois ans. Je m'attends à rencontrer de nombreux cas nécessitant de trouver un équilibre entre la refactorisation du code hérité et l'avancement du projet. Je partagerai mes nouveaux apprentissages sur [mon blog personnel](https://www.sihui.io) (PAS medium). Abonnez-vous pour suivre !

Mon plan de carrière pour l'année est de devenir un tech lead. Je suis enthousiaste à l'idée de tous les apprentissages à venir et j'aimerais partager ce voyage avec vous de manière brutalement honnête. **Je partagerai mes apprentissages hebdomadaires sur mon [blog personnel](https://www.sihui.io) (PAS medium).**

Dans les prochains mois, je me concentrerai sur la croissance dans les domaines suivants, vous pouvez donc vous attendre à voir des publications liées à ceux-ci :

* se concentrer sur la vision globale du projet plutôt que sur les détails d'implémentation à court terme ;
* équilibrer mes efforts entre la direction de projets et le codage ;
* l'équilibre entre vie professionnelle et vie privée pour une productivité à long terme ;
* le côté humain du développement logiciel : s'assurer que tout le monde qui travaille avec moi apprécie le voyage et se sent épanoui et inspiré.

_Publié à l'origine sur [www.sihui.io](https://www.sihui.io/refactoring-vs-staying-focused/) le 1er février 2019._