---
title: Réveiller une ville endormie avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-28T09:11:23.000Z'
originalURL: https://freecodecamp.org/news/waking-up-a-sleeping-city-with-javascript-3b9740e094bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v4Lqx0NQIeTugNA9w_AlLg.jpeg
tags:
- name: events
  slug: events
- name: india
  slug: india
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Réveiller une ville endormie avec JavaScript
seo_desc: 'By Koustuv Sinha

  Not once, but twice, our college became a part of an International community of
  highly productive and engaging people. The most recent installment took place on
  last Saturday, May 21st, 2016. From Lisbon to Lahore, from Belgrade to B...'
---

Par Koustuv Sinha

Non pas une, mais deux fois, notre université a fait partie d'une communauté internationale de personnes hautement productives et engagées. La plus récente édition a eu lieu le samedi 21 mai 2016. De Lisbonne à Lahore, de Belgrade à Bengaluru, de Berlin à Bainbridge, nous nous sommes tous réunis en un seul jour pour célébrer un événement mondial, un événement amusant d'enseignement, d'apprentissage et de hacking ensemble des concepts de JavaScript / NodeJS. Divisés par les frontières, unis par JavaScript ! Oui, je parle de la [Journée Internationale de NodeSchool](http://nodeschool.io/international-day) !

![Image](https://cdn-media-1.freecodecamp.org/images/6k2Eq4IVWPU4th2C3Yflhot8fq02QIUCtzGa)

#### Une brève histoire de NodeSchool

Un beau jour, quelques personnes d'une petite communauté montante de hackers open source audacieux ont décidé de défier le monde avec les pouvoirs d'un langage que d'autres qualifiaient de "trop lent", "un langage jouet" et "uniquement pour le web". Ils se sont réunis pour construire ce qui serait un simple module "[workshopper](https://github.com/workshopper/workshopper)", appelé [stream-adventure](https://github.com/substack/stream-adventure).

Qu'est-ce qu'un workshopper ? C'est un framework simple affichant un ensemble de défis à compléter directement dans votre terminal, et il intègre un exécuteur de tests pour tester vos solutions de code.

![Image](https://cdn-media-1.freecodecamp.org/images/suW-XpjrCxnhcI8K4o8seqWbUplsRm2mMlBR)
_workshopper javascripting_

Ces gars ont ensuite créé les modules initiaux de workshopper, tels que [javascripting](https://github.com/sethvincent/javascripting) et [learnyounode](https://github.com/workshopper/learnyounode), qui consistaient en des problèmes de niveau débutant en JS et NodeJS. Ils ont pensé : "Eh bien, c'est amusant. Nous devrions organiser un événement axé sur ces choses !"

Bientôt, les idées ont afflué, devenant des modules dans l'écosystème NodeJS (npm). Les participants ont créé des dépôts et mis en place des sites web. Et à la fin de l'année 2013, le premier événement officiel de NodeSchool était en cours dans la Silicon Valley.

La communauté a commencé à grandir, et des chapitres locaux ont vu le jour dans le monde entier. En mai 2016, il y avait plus de 165 chapitres basés dans des villes du monde entier, qui ont organisé plus de 500 événements à ce jour !

![Image](https://cdn-media-1.freecodecamp.org/images/5dXhvDvhHexwG51SzLwExrUatlxrGTFl05bh)
_Événements à venir et passés de NodeSchool_

#### Node arrive à Kolkata

En juillet de l'année dernière, j'ai eu l'idée d'organiser un événement NodeSchool dans ma ville. Techniquement parlant, Kolkata est une ville détendue avec peu de meetups ou de hackathons à mentionner. La plupart des événements cool se déroulent soit à Bangalore soit à Hyderabad. Nous avons un parc technologique — connu ici sous le nom de Sector V — qui était une utopie promise pour les startups en herbe et les grandes entreprises. Mais disons simplement qu'il n'a pas prospéré autant que ceux des autres zones métropolitaines en Inde.

Il y a des entreprises technologiques ici, mais la plupart sont basées sur les services. Il n'y a pas beaucoup d'empreinte de produits ou de startups. Les étudiants de premier et de deuxième cycle dans ma ville manquent le moyen le plus important de réseautage et d'apprentissage des compétences simplement à cause du paysage actuel. Et ainsi, ils se rabattent sur rejoindre des géants de l'IT basés sur les services, qui les traitent simplement comme une ressource jetable.

![Image](https://cdn-media-1.freecodecamp.org/images/ZqIL9kabTYRnK1TkFC8mPmcDCZ5ikMUrF0RM)
_Sector V, Kolkata, Inde_

Avec peu de temps pour tout mettre en place, j'ai contacté un membre de l'équipe principale de NodeSchool, [Adam Brady](https://github.com/SomeoneWeird), et je lui ai demandé de me guider. J'avais trois priorités pour l'événement :

* Créer une prise de conscience dans ma ville et mon université
* Former les étudiants de l'université et les aider à se familiariser avec les nouvelles technologies
* Mettre notre université sur la carte mondiale

Tous les chapitres de NodeSchool sont basés sur des villes. Cela signifiait que, techniquement parlant, je devais organiser NodeSchool Kolkata. Mais en raison des contraintes de temps et d'espace, j'ai eu une meilleure idée. Pourquoi ne pas créer un chapitre de niveau universitaire plus petit ? Après en avoir parlé avec Adam, il a accepté ma proposition, et ainsi le [NodeSchool IEM Kolkata Chapter](https://github.com/nodeschool/iem-kolkata) est né en août 2015.

Nous avons eu notre atelier inaugural le 31 août 2015, avec 25 participants. Ensemble, nous avons codé principalement sur des modules débutants de NodeSchool en utilisant JavaScript et Git.

En ce qui concerne les nouveaux débuts, cela a dépassé mes attentes, pour dire le moins ! Les participants sont rentrés chez eux avec un peu de connaissances pratiques, quelques autocollants gratuits et beaucoup plus de confiance ! [IEM Kolkata](http://iem.edu.in/) a été ajouté à la carte mondiale, et [Max Odgen](https://github.com/maxogden) (fondateur principal de NodeSchool) [a commenté nos photos](https://github.com/nodeschool/iem-kolkata/issues/3) !

![Image](https://cdn-media-1.freecodecamp.org/images/OygUH0qBwjbUVKZTFMQxRZMjc8kYSC59mIiQ)
_Atelier NodeSchool à IEM Kolkata le 31 août 2015_

Comme le prédit la Deuxième Loi de la Thermodynamique, après l'atelier, l'intérêt a disparu à un minimum. Mais cela ne m'a pas découragé de mon objectif. J'ai trouvé quelques personnes intéressées à long terme, et j'ai commencé une petite newsletter parmi eux. Nous sommes restés en contact et avons partagé des liens importants, des ressources et des tutoriels entre nous.

Avance rapide jusqu'en mai 2016. La Journée Internationale de NodeSchool était juste au coin de la rue, et la planification a commencé à peine une semaine avant ! [Himanshu Kashyap](https://github.com/hkiem), un étudiant de dernière année, m'a aidé cette fois-ci en faisant la publicité de l'événement, en gérant les tâches back-end et en mentorant. Nous avons envoyé des invitations, mis en cache le logiciel de l'atelier pour pouvoir l'utiliser hors ligne, configuré notre site web et nous sommes inscrits au Chapitre de la Journée Internationale. Nous étions prêts pour l'événement ! Nous avons même obtenu le [Indian School of Ethical Hacking](https://www.isoeh.com/) — une startup fondée par notre ancien élève [Kirit Sankar Gupta](https://www.linkedin.com/in/kiritsankargupta) — pour sponsoriser l'événement !

La nature a travaillé contre nous cette fois-ci. De fortes pluies dans toute la ville ont empêché la moitié des personnes qui s'étaient déjà inscrites à l'événement de se présenter. Pourtant, nous avons continué, avec le vrai esprit de la Journée Internationale de NodeSchool, et avons commencé les procédures avec les équipes de Bengaluru et Osaka.

La dernière fois, nous avons eu quelques problèmes pour tout mettre en place, mais cette fois-ci, comme les ateliers étaient déjà mis en cache dans mon système ([local-npm](https://github.com/nolanlawson/local-npm)), et les installations étaient un jeu d'enfant.

À l'heure du déjeuner, tout le monde avait terminé le module de base _javascripting_, et avait faim de plus ! Après le déjeuner, nous avons poursuivi avec les bases de Git, Github et NodeJS avec les modules _git-it_ et _learnyounode_. Nous avons également eu un chat en direct [Appear.in](https://appear.in/) avec [Ian Crowther](https://github.com/iancrowther), l'hôte du Chapitre de [Londres](http://nodeschool.io/london/), ainsi que les Chapitres de [Tokyo](http://nodeschool.io/tokyo/) et [Berlin](http://nodeschool.io/berlin/) ! À la fin de la journée, nous avons distribué des autocollants et des sous-verres, puis nous sommes passés à Bisk Farm pour une ronde de snacks et de boissons.

![Image](https://cdn-media-1.freecodecamp.org/images/ZZtD1LrX8Ub9GvsBZyzdoYUomiDglanaTrCe)

![Image](https://cdn-media-1.freecodecamp.org/images/XEI4OeClHil2lsiSRGV1UU4m5vMbotZsbYpO)

Je prévois éventuellement de fusionner notre chapitre avec un chapitre NodeSchool Kolkata plus grand une fois que nous aurons assez de personnes intéressées. Il faut du temps pour développer l'intérêt et la sensibilisation dans notre ville, mais nous devrions tous nous efforcer de le faire néanmoins.

Selon The Guardian, l'Inde aura [plus d'un million de personnes atteignant 18 ans](https://www.theguardian.com/books/2016/apr/24/somini-sengupta-the-end-of-karma-interview) chaque mois pour les deux à trois prochaines années ! C'est une charge énorme pour notre société à supporter en une seule fois. De plus, notre pays est confronté à une pénurie aiguë d'ingénieurs qualifiés, et 80 % de la génération actuelle d'ingénieurs sont considérés comme inemployables par certaines [études](http://timesofindia.indiatimes.com/tech/tech-news/Over-80-of-engineering-graduates-in-India-unemployable-Study/articleshow/50704157.cms). Pourquoi ? Les causes vont des collèges d'ingénierie médiocres, de la faible qualité de l'éducation en classe, de la moindre opportunité, et surtout, du moindre réseautage.

Tout n'est pas mauvais dans ma ville, cependant. Nous connaissons un afflux lent de startups basées dans la ville, grâce à certains entrepreneurs cool, comme [Sumeet Chawla](https://www.linkedin.com/in/chawlasumeet), qui a fondé [JustStickers.in](http://juststickers.in/), où nous achetons des autocollants et des sous-verres cool pour nos événements. Son amour pour cette ville l'a éloigné de Bangalore, et il a ramené son expérience et l'a immédiatement mise à profit. Nous avons besoin de plus d'entrepreneurs comme lui pour construire des produits innovants et aider à notre tour notre ville à devenir un endroit plus favorable à la technologie.

![Image](https://cdn-media-1.freecodecamp.org/images/pBOZ-jMxAAeq74XrU2o-SDWvzaLHWB4BRQWd)
_Autocollants et sous-verres de JustStickers à notre événement NodeSchool, mai 2016_

Les membres des communautés NodeSchool et Free Code Camp ont quelque chose de beaucoup plus important que l'expertise brute. Ils ont du cœur, un désir de réseauter et une volonté d'aider les autres. Cela augmente le niveau de compétence de chaque participant.

**La collaboration est la clé du succès.** Nous espérons construire une meilleure communauté technologique dans notre ville en organisant des événements réguliers comme NodeSchool, Free Code Camp, et continuer à pousser notre ville vers une génération plus informée, compétente et proactive.

Rejoignez-moi dans cette Quête. **Pour la [Ville de la Joie](https://www.quora.com/Why-was-Kolkata-given-the-nickname-City-of-Joy).**

_Merci à [Arijit Layek](https://github.com/alayek) pour les édits géniaux et la motivation constante. Si vous souhaitez entrer en contact, contactez-moi sur [Gitter](https://gitter.im/koustuvsinha). [Aidez-nous à planifier](https://gitter.im/nodeschool/kolkata) un événement NodeSchool Kolkata plus grand._