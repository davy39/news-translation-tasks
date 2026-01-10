---
title: 'Construction de communautés en ligne : OpenAPS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-28T12:31:57.000Z'
originalURL: https://freecodecamp.org/news/building-online-communities-openaps-96475c235f7e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*K0mzkX-bCbkn_dV7kEmk5w.png
tags:
- name: Health Technology
  slug: health-technology
- name: community
  slug: community
- name: community building
  slug: community-building
- name: Diabetes
  slug: diabetes
- name: open source
  slug: open-source
seo_title: 'Construction de communautés en ligne : OpenAPS'
seo_desc: 'By Gitter

  Dana Lewis is the founder of OpenAPS (Open Artificial Pancreas System), an open
  and transparent effort to make artificial pancreas technology widely available.

  We interviewed her to learn more about her story. You can learn more by visiting...'
---

Par Gitter

[Dana Lewis](https://twitter.com/danamlewis) est la fondatrice de [OpenAPS](https://openaps.org/) (Open Artificial Pancreas System), un effort ouvert et transparent pour rendre la technologie du pancréas artificiel largement disponible.

Nous l'avons interviewée pour en savoir plus sur son histoire. Vous pouvez en apprendre davantage en visitant le canal OpenAPS [sur Gitter](https://gitter.im/nightscout/intend-to-bolus).

![Image](https://cdn-media-1.freecodecamp.org/images/Oi4r--S1-4DC72Z0oXDipc7bRvqWxX6nTVxC)
_Dana Lewis et le système OpenAPS._

**Bonjour Dana ! Parlez-nous de vous et du projet OpenAPS. Qu'est-ce qu'OpenAPS et quelle est l'histoire derrière cela ?**

#[OpenAPS](http://www.openaps.org/) est le mouvement open source pour rendre la technologie du pancréas artificiel plus largement disponible et bien plus tôt que ce qui serait autrement possible. Le "pancréas artificiel" (également considéré comme une "boucle fermée hybride") automatise la délivrance d'insuline en utilisant une pompe à insuline existante et un moniteur de glucose continu pour les personnes atteintes de diabète de type 1. Actuellement, il n'existe aucune option commercialement disponible, donc les personnes sont contraintes d'utiliser la "thérapie standard", ce qui signifie effectuer tous les calculs de dosage elles-mêmes. Cela peut être vraiment difficile, lorsque les niveaux de glucose dans le sang changent constamment ; et VRAIMENT difficile la nuit lorsque les personnes dorment !

Moi ([@DanaMLewis](http://twitter.com/danamlewis)) vis avec le diabète de type 1 depuis plus de 14 ans et je sais à quel point c'est difficile. Il y a quelques années, au lieu de simplement dire "oh bien, je ne peux rien faire" pour améliorer mes dispositifs médicaux existants, j'ai commencé à chercher des solutions de contournement pour résoudre les problèmes de ma vie réelle. J'ai d'abord utilisé du code open source pour extraire des données de mon CGM en temps réel et créer des alarmes plus fortes en envoyant ces données à mon téléphone. (Ce morceau de code open source a finalement évolué vers [Nightscout](http://nightscout.info/), un excellent outil à découvrir pour la surveillance à distance des données CGM.)

Notre système d'"alarme cloud" [a évolué](https://diyps.org/2016/05/12/how-i-designed-a-diy-closed-loop-artificial-pancreas/) vers un système "[open loop](https://diyps.org/2014/02/07/a-diy-artificial-pancreas-system/)" avec un algorithme de décision de dosage que nous avons ensuite développé. [Scott](http://twitter.com/scottleibrand) et moi avons alors réalisé que nous pouvions utiliser le code open source de quelqu'un d'autre pour envoyer des commandes (avec l'ajout d'un petit ordinateur comme un Raspberry Pi et un stick radio) directement à ma pompe à insuline, créant finalement [un système de pancréas artificiel en boucle fermée](https://diyps.org/2014/12/15/how-does-a-closed-loop-artificial-pancreas-work-when-you-diy-or-diyps-closed-loop-is-working/). J'ai "fermé la boucle" pour moi-même en décembre 2014, et nous avons [lancé](https://diyps.org/2015/02/07/diyps-openaps/) OpenAPS en février 2015. Nous ne pouvons pas distribuer commercialement des dispositifs médicaux ou des systèmes logiciels complets, car cela est réglementé par la FDA ; mais nous voulions trouver un moyen de partager des connaissances afin que si quelqu'un d'autre voulait construire sa propre boucle fermée, il puisse le faire jusqu'à ce que quelque chose devienne commercialement disponible à l'avenir. C'est donc ce que nous avons fait, et c'est pourquoi OpenAPS existe aujourd'hui.

OpenAPS est plusieurs choses, mais pensez-y comme un écosystème où vous pouvez prendre des pompes à insuline et des CGM existants et les associer à d'autres matériels commercialement disponibles et à des logiciels open source pour aider à automatiser la délivrance d'insuline de manière à réduire le risque global pour la vie quotidienne avec le diabète.

**Quels sont les objectifs communs que vous avez en tant que communauté ?**

Notre principal objectif commun est de faciliter la vie avec le diabète de type 1. La vie avec le diabète est DIFFICILE. Non seulement physiquement, mais aussi émotionnellement. Le fardeau cognitif joue un grand rôle sur les familles entières, car que ce soit les parents soutenant un enfant grandissant avec le diabète, ou un adulte et ses proches, le diabète impacte tout le monde. Le mouvement #WeAreNotWaiting est une communauté plus large au-delà de #OpenAPS qui dit "nous **ne pouvons pas** attendre des années et des années pour de meilleurs outils et solutions, donc nous ferons tout ce que nous pouvons pour rendre aujourd'hui plus facile" pour les personnes vivant avec le diabète.

"Pay it forward" est un autre objectif commun. Nous utilisons tous des outils et des idées donnés à la communauté par d'autres, donc nous sommes tous passionnés par l'idée de redonner de n'importe quelle manière que nous pouvons. Cela peut inclure la contribution de PRs au code ou à la documentation, ou aider quelqu'un sur Gitter qui pose une question sur quelque chose que vous avez appris la semaine dernière. Pour beaucoup d'entre nous, "redonner" est notre première introduction à la contribution à l'open source.

![Image](https://cdn-media-1.freecodecamp.org/images/CYVfO5k8q6jSkdGt-EqLmjxyKZkO3Iuk5RMe)
_La pile OpenAPS_

**Quels sont les problèmes liés au projet qui vous enthousiasment personnellement ces jours-ci ?**

OpenAPS en est au point où il y a au moins (n=1)*127+ personnes dans le monde utilisant des systèmes de boucle fermée DIY. Parce que ce sont des efforts (n=1) et que tout le monde doit construire ses propres systèmes (c'est aussi pour des raisons de sécurité), il y a constamment des améliorations et des ajustements nécessaires à [la documentation du processus de configuration disponible sur Github](https://github.com/openaps/docs). Nous avons cependant parcouru un long chemin. Lorsque quelqu'un se plaint de la documentation n'étant pas parfaite, je ris et je fais remarquer que nous avons initialement construit la première boucle fermée avec ZÉRO documentation : au moins une documentation imparfaite est meilleure que rien ! Ensuite, nous travaillons ensemble pour corriger la documentation. Beaucoup de personnes font leur première pull request vers le dépôt de documentation, et c'est leur première contribution à l'open source — mais espérons que ce ne sera pas leur dernière !

L'autre problème commun est le temps. Tout le monde travaille sur cela pendant son temps libre, et nous avons tous des emplois à temps plein. Donc notre travail collectif pour améliorer [le code](https://github.com/openaps/oref0/), [la documentation](https://github.com/openaps/docs), et [soutenir les autres](https://gitter.im/nightscout/intend-to-bolus) dans la configuration de leurs propres systèmes a lieu le soir, le week-end, tôt le matin et pendant les pauses. Mais avec une communauté mondiale, il y a généralement toujours quelqu'un en ligne sur [Gitter](https://gitter.im/nightscout/intend-to-bolus) et capable de répondre aux questions, ce qui est génial !

**Quels progrès ont été réalisés depuis le début du projet, pouvez-vous partager quelques histoires de succès particulières ?**

Scott et moi avons construit ma première boucle fermée, puis avons travaillé avec [Ben West](https://github.com/bewest) alors qu'il construisait [l'outil openaps](https://github.com/openaps/openaps) pour faciliter la construction de leurs propres systèmes par d'autres. L'outil openaps en lui-même est un énorme succès, car il s'agit essentiellement de blocs de construction que n'importe qui peut utiliser pour construire un système de lecture de données à partir de dispositifs de diabète compatibles.

La [documentation OpenAPS](https://github.com/openaps/docs) est également un succès, car il s'agit d'un ensemble de documents en constante évolution, vivant, qui n'a pas nécessairement une feuille de route claire pour le développement futur. Elle change chaque fois que nous ajoutons une nouvelle option matérielle ou un nouvel outil logiciel (ce qui est assez fréquent), donc c'est impressionnant que cette documentation soit encore utile et soutienne toujours les personnes pour la configuration. Et je suis assez fière que la documentation soit à un niveau tel que quelqu'un sans aucune expérience technique précédente puisse l'utiliser et apprendre ce qu'il doit faire pour construire lui-même un système de boucle fermée.

**Quels sont les principaux sujets discutés dans le canal OpenAPS sur Gitter ?**

Il y a plusieurs salles différentes sur Gitter utilisées par la communauté, mais [la salle la plus utilisée est celle où la plupart des conversations de configuration pour OpenAPS ont lieu](https://gitter.im/nightscout/intend-to-bolus). Nous utilisons principalement Gitter pour les personnes qui travaillent sur le processus de configuration, mais nous l'utilisons également pour héberger des discussions sur la nouvelle documentation ajoutée, et les nouvelles fonctionnalités testées et discutées avant d'être incorporées dans la branche de développement du code.

**Quels sont les facteurs qui contribuent au succès de votre communauté ? Quels sont les principaux défis ?**

Le succès de la communauté OpenAPS témoigne de l'implication des personnes concernées. Cela inclut les [années](https://www.youtube.com/watch?v=n0KUgieLPNw&feature=youtu.be) de travail de Ben derrière les scènes et son soutien actif pour aider beaucoup d'entre nous à apprendre sur l'open source et les outils connexes (y compris nous encourager dès le début à utiliser Gitter et Github) ; la dédicace infatigable de Scott pour m'aider (même s'il n'a pas lui-même de diabète !) non seulement à construire ma première boucle fermée mais aussi à en faire une option pour quiconque dans le monde prêt à construire la sienne ; aux dizaines de personnes contribuant à la documentation et construisant de nouveaux outils matériels et logiciels. Nous ne serions pas là où nous en sommes aujourd'hui sans toutes ces personnes incroyables.

Certains des défis impliquent des contraintes de temps. D'autres impliquent le fait que nous travaillons dans une zone grise de la réglementation. Techniquement, la FDA régule les dispositifs médicaux distribués commercialement. Dans notre cas, aucun dispositif médical n'est distribué, et chacun fait du DIY en construisant ses propres systèmes. Mais il y a une certaine crainte au sein de la communauté que les individus soient poursuivis pour avoir personnellement construit des outils pour eux-mêmes afin de les aider à gérer leur diabète. Donc, la crainte elle-même de litiges ou de réglementations inutiles est un défi au niveau individuel.

Et oui, certains des défis sont techniques — même si nous avons vu [des dizaines de personnes sans aucune expérience technique travailler leur chemin à travers le processus](https://diyps.org/2015/04/08/making-and-diying-continued/) et construire eux-mêmes des systèmes, il y a aussi des dizaines qui se sont convaincus qu'ils ne pouvaient pas le faire et ne sont pas prêts à essayer. Mais, puisque ce n'est pas un système approuvé par la FDA, l'exigence de le faire soi-même sera toujours là — donc pour ceux qui ne sont pas prêts à essayer ou pour d'autres bonnes raisons décident que ce type de système ne leur convient pas, ils devront attendre que des options approuvées commercialement deviennent disponibles.

![Image](https://cdn-media-1.freecodecamp.org/images/HIFVnH-aV8pukwF63ZdXorAb7ouOcLzWSJfW)

**Sur la base de votre expérience, pensez-vous que les communautés open source ont changé et évolué au cours des dernières années ? Si oui, comment ?**

Je ne suis impliquée dans l'open source que depuis environ trois ans. Mais l'une des choses que j'apprécie le plus est le soutien chaleureux et la collaboration que j'ai reçus de personnes comme Ben, Scott, [Chris Hannemann](https://github.com/channemann), [Pete Schwamb](http://github.com/ps2), [Oskar Pearson](https://github.com/oskarpearson), et [Nate Racklyeft](https://github.com/loudnate) (parmi beaucoup d'autres), qui sont toujours prêts à répondre aux questions et à partager leurs connaissances. J'ai trouvé cet esprit formidable assez répandu dans tous les domaines de l'open source, et je pense qu'il fait une grande différence pour l'évolution et la croissance des communautés open source.

**Quel conseil donneriez-vous à quelqu'un qui veut créer une communauté open source en ligne axée sur les soins de santé ?**

Restez centré sur votre objectif. Je ne pense pas qu'il s'agisse de créer une communauté, mais de soutenir et de guider la communauté qui grandit à partir d'un projet partagé ou d'un sentiment de but. Pour nous, ce but partagé est de faciliter la vie avec le diabète et de rendre la technologie du pancréas artificiel plus accessible pour tous. Et je suggère également d'utiliser les outils disponibles. L'une des raisons pour lesquelles nous utilisons (et aimons vraiment) Gitter est qu'il y a une faible barrière à l'entrée : le contenu est publiquement accessible, donc n'importe qui peut observer ou [lurker](https://gitter.im/nightscout/intend-to-bolus) et apprendre avant d'être prêt à sauter ou à poser sa première question. C'est bien d'avoir cet endroit central de rassemblement pour les discussions, plutôt que d'avoir des conversations clés dispersées sur de nombreux canaux.

**Y a-t-il autre chose que vous souhaitez ajouter ?**

Pour toute personne intéressée à en savoir plus sur OpenAPS, [la lecture de la conception de référence OpenAPS](https://openaps.org/reference-design/) est un excellent point de départ, suivie par [les FAQ OpenAPS](https://openaps.org/frequently-asked-questions/). Et si vous êtes intéressé à plonger dans le diabète DIY et les communautés open source, nous serions ravis de vous les indiquer ! N'hésitez pas à me laisser un mot à dana@OpenAPS.org ou à nous contacter sur [Gitter](https://gitter.im/nightscout/intend-to-bolus).

**Merci !**