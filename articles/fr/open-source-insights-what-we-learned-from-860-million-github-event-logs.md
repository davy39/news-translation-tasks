---
title: Open Source Insights – Ce que nous avons appris de 860 millions de journaux
  d'événements GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-09T00:19:50.000Z'
originalURL: https://freecodecamp.org/news/open-source-insights-what-we-learned-from-860-million-github-event-logs
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Screen-Shot-2021-04-08-at-7.00.31-AM.png
tags:
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: Open Source Insights – Ce que nous avons appris de 860 millions de journaux
  d'événements GitHub
seo_desc: "By Xue (Xander) Wu\nOpen source software has become a cornerstone of our\
  \ digital world. And open collaboration plays an enormous role in the development\
  \ of human digital civilization. \nGitHub, the world's largest open source collaboration\
  \ platform, pr..."
---

Par Xue (Xander) Wu

Les logiciels open source sont devenus une pierre angulaire de notre monde numérique. Et la collaboration ouverte joue un rôle énorme dans le développement de la civilisation numérique humaine. 

GitHub, la plus grande plateforme de collaboration open source au monde, produit une quantité massive de données sur le comportement des développeurs. Alors, que pouvons-nous faire avec ces données ?

## Le Problème – Comment mesurer la productivité 

Comme l'a dit le gourou du management Peter Drucker, « Si vous ne pouvez pas le mesurer, vous ne pouvez pas le gérer », et, par conséquent, vous ne pouvez pas l'améliorer. 

L'industrie du logiciel n'a pas encore trouvé de méthode capable de mesurer efficacement la productivité du développement logiciel. Cela est particulièrement vrai pour l'ensemble de l'écosystème open source. La manière dont les individus et les communautés sont mesurés et la manière dont les gestionnaires peuvent utiliser ces métriques pour prendre de meilleures décisions sont encore des questions ouvertes. 

À notre avis, ce sont à la fois des défis et des opportunités. Lorsque vous gérez un projet open source, il est difficile de contourner le problème de la mesure. Mais les journaux d'événements GitHub offrent une excellente opportunité de résoudre ce problème.

La mesure est également une arme à double tranchant. Étant donné sa forte nature directive, elle vous motive à prêter attention et à améliorer les éléments qui peuvent être mesurés. 

Cependant, la mesure peut également vous amener à ignorer et à aggraver les éléments que vous ne pouvez pas mesurer. Comment trouver les bonnes métriques et les utiliser judicieusement dans le processus de construction de grandes communautés et écosystèmes open source à travers le monde ?

Eh bien, nous avons obtenu 860 millions de journaux d'événements GitHub générés en 2020 et analysé les données de plus de 14 millions de développeurs actifs et de plus de 54 millions de projets actifs. Et dans cet article, nous partagerons nos insights.

## Le Rapport GitHub 2020 Digital Insight

Dans notre rapport [GitHub 2020 Digital Insight Report](http://oss.x-lab.info/github-insight-report-2020-en.pdf), récemment publié, qui est également un projet open source sur [GitHub](https://github.com/X-lab2017/github-analysis-report), nous avons exploré l'état des tendances mondiales en matière d'open source. 

Le but du rapport était de produire une carte mondiale de l'écosystème open source, de promouvoir l'innovation sociale open source et de favoriser la collaboration ouverte.

Le rapport commence par une analyse générale de l'état mondial de l'open source aujourd'hui. Les sections suivantes incluent une discussion sur les analyses approfondies des développeurs et des projets, des études de cas et des projets vedettes du mois.

Nous avons défini des métriques et construit des modèles en prêtant attention aux informations dans les dimensions du temps, de la diversité et des réseaux collaboratifs. Nous avons également introduit deux concepts importants, **OpenGalaxy** et **Open Source Quadrant**.

## Principaux enseignements du rapport

### L'industrie mondiale de l'open source s'est beaucoup développée

Le nombre total de journaux d'événements GitHub dans le monde était d'environ 860 millions en 2020, ce qui représente une augmentation d'environ 42,6 % par rapport à 610 millions en 2019. 

Nous avons également constaté que le nombre de projets actifs dans le monde sur GitHub en 2020 était d'environ 54,21 millions, tandis que le nombre de comptes de développeurs actifs était d'environ 14,54 millions. Cela représente une augmentation respective de 36,4 % et 21,8 % par rapport à 2019.

![Image](https://uploader.shimo.im/f/DzxnbbSnebkLsGvR.png!thumbnail)

### Les développeurs sont au cœur du monde open source

Un modèle d'activité basé sur des données massives peut refléter efficacement et en continu l'état général des développeurs et des communautés.

Suivant l'esprit de la maxime Apache « Community Over Code » promue par [The Apache Way](https://www.apache.org/theapacheway/), la communauté des développeurs est cruciale pour la vitalité de l'open source. 

Nous avons tenté de présenter une analyse complète de tous les développeurs GitHub en 2020 sous plusieurs angles, tels que le niveau d'activité des développeurs, l'utilisation des applications GitHub, les heures de travail typiques, la distribution des fuseaux horaires des développeurs dans le monde et la distribution des langues des développeurs.

Nous avons introduit la **métrique d'activité des développeurs**, qui reflète le niveau d'activité d'un compte GitHub spécifique dans un projet GitHub spécifique sur une période de temps. 

Nous déterminons la métrique d'activité des développeurs par les données de comportement du compte dans le projet. Les comportements détaillés dans ce rapport incluent les commentaires d'Issue, l'ouverture d'Issue, l'ouverture de Pull Request, les commentaires de révision de Pull Request, les Pull Request fusionnées, Watch et Fork, avec des poids respectifs de 1, 2, 3, 4, 2, 1, 2.

![Image](https://uploader.shimo.im/f/sdTTqriJNU0Hbj02.png!thumbnail)

Parmi eux, le nombre de Pull Request fusionnées est déterminé par la fonction par morceaux :

![Image](https://uploader.shimo.im/f/NJjU0HEawJp0uHwi.png!thumbnail)

![Image](https://uploader.shimo.im/f/P4lMIinXV5K7PUtm.png!thumbnail)

Les statistiques suggèrent que 5 445 développeurs ont une métrique d'activité supérieure à 2 000, ce qui équivaut à moins de 6 sur 10 000 développeurs GitHub. 

La plupart des métriques d'activité des développeurs se situent dans la plage [0,500], représentant 99,45 % du nombre total de développeurs GitHub, ce qui suggère que la plupart des développeurs ont encore un faible niveau d'activité. 

À la fin de la courbe, le nombre de dépôts actifs montre une augmentation, probablement attribuable au grand nombre de dépôts actifs pour certains comptes de collaboration automatisée non filtrés, qui dépassent de loin le nombre de développeurs humains. Cela entraîne une extrémité de courbe en forme de V.

### L'automatisation est la clé

L'automatisation du pipeline des logiciels open source s'est beaucoup améliorée, et des robots collaboratifs numériques diversifiés ont commencé à entrer dans le courant dominant.

Nous avons constaté que 8 des 10 développeurs les plus actifs sont des applications GitHub, et les deux autres sont des comptes de développeurs pour la collaboration automatisée.

![Image](https://uploader.shimo.im/f/oapQVMWMYm3C6BTY.png!thumbnail)

Les robots collaboratifs automatisés peuvent servir de nombreux projets simultanément car ils s'exécutent côté serveur. Cela entraîne un niveau d'activité extrêmement élevé et un nombre énorme de dépôts collaboratifs.

Comme le montre le tableau ci-dessus, la majorité des comptes de développeurs les plus actifs sur GitHub sont des applications GitHub. Ce rapport analyse les données pertinentes des applications GitHub. 

Par exemple, la figure suivante montre la tendance à la fois du nombre d'applications GitHub actives (comptes actifs totaux) et du ratio des journaux générés par les applications GitHub par rapport à tous les journaux d'événements GitHub (proportion des journaux) de 2015 à 2020.

![Image](https://uploader.shimo.im/f/XpPx8PdIpmQrbYSo.png!thumbnail)

Les applications GitHub se sont développées rapidement ces dernières années depuis leur lancement en 2016. En termes de proportion de journaux, le nombre total avait augmenté de 288 % en 2019 par rapport à 2018, et il a augmenté de 141 % en 2020 par rapport à 2019 pour atteindre plus de 12 %.

Nous avons ouvert ce [projet de rapport](https://github.com/X-lab2017/github-analysis-report) en open source sur GitHub. Pour automatiser le développement de code et l'analyse de données pour ce projet, nous avons développé analysis-report-bot[bot], un robot collaboratif GitHub, en août 2020. 

Il est intéressant de noter que analysis-report-bot[bot] se classe 289e dans le classement d'activité de toutes les applications GitHub à ce jour.

Ayant bénéficié de ce bot collaboratif automatisé, nous croyons que les bots basés sur les applications GitHub seront plus largement utilisés pour aider à mieux gérer les collaborations à grande échelle pour les projets open source à l'avenir.

### Les contributions open source coïncident généralement avec les heures de travail des développeurs 

Les heures de travail des développeurs principaux dans les communautés GitHub montrent des schémas clairs et se chevauchent progressivement avec les heures de travail des développeurs dans leurs emplois. 

L'open source d'entreprise est devenu le courant dominant absolu, et les projets open source « 996 » en heures de travail ont fait leur apparition.

Puisque le journal d'événements GitHub contient des informations détaillées sur les horodatages, nous pouvons obtenir des insights par le biais d'une analyse statistique de la dimension temporelle. Par exemple, en temps universel coordonné (UTC), la distribution mondiale du temps de travail est illustrée dans la figure suivante :

![Image](https://uploader.shimo.im/f/8OcbweiWxnwLlEsr.png!thumbnail)

Supposons que les heures de travail normales pour les développeurs principaux sont de 9h00 à 21h00 chaque jour. D'un point de vue mondial, à travers le volume de journaux, nous pouvons voir que les développeurs sur la plateforme GitHub proviennent principalement d'Europe et des États-Unis. 

De plus, nous pouvons voir que l'activité le week-end est significativement plus faible que les jours de semaine. Cela est cohérent avec le rapport [GitHub Octoverse 2020](https://octoverse.github.com/) qui a constaté que plus de développeurs utilisent GitHub pour travailler au lieu de développer uniquement sur la base de leurs intérêts.

### Nous pouvons en apprendre beaucoup sur la distribution mondiale des développeurs utilisant GitHub

Les Amériques ont la plus grande distribution de développeurs. L'Europe a le pourcentage le plus élevé de développeurs dans un seul fuseau horaire, tandis que le nombre de développeurs asiatiques est encore faible. Comparé à d'autres pays asiatiques, la Chine se distingue par un niveau d'activité open source plus élevé.

La distribution géographique des développeurs a toujours été un aspect important des indicateurs de mondialisation des projets open source. 

Sur la base des statistiques des 50 000 meilleurs développeurs dans le classement d'activité des développeurs GitHub, nous pouvons estimer la distribution de tous les développeurs GitHub dans divers fuseaux horaires comme illustré dans la figure suivante.

![Image](https://uploader.shimo.im/f/EX0YQQFq1LILNkzm.png!thumbnail)

Nous pouvons voir que les Amériques (États-Unis, Canada et Amérique du Sud) ont la plus grande distribution de développeurs parmi les développeurs très actifs. Bien que la proportion de développeurs dans un seul fuseau horaire ne soit pas la plus élevée, la proportion globale de développeurs dans cette région est aussi élevée qu'environ 33 %. 

L'Europe a la plus forte proportion de développeurs dans un seul fuseau horaire. Le fuseau horaire UTC+1 est aussi élevé que près de 10 %, avec la proportion totale des trois fuseaux horaires étant d'environ 26 %. 

En général, le nombre de développeurs en Asie est encore relativement faible, mais nous pouvons voir un petit pic dans la région UTC+7 et UTC+8, indiquant que les développeurs en Chine et en Russie sont encore plus actifs dans l'open source que dans d'autres pays. 

La région du Pacifique a la plus faible proportion de développeurs en raison de la distribution de la population.

### JavaScript et Python se classent premier et deuxième mondialement

Pas de surprise ici – JS et Python occupent toujours la première et la deuxième place, respectivement, dans les classements des langues. HTML et CSS sont plus populaires dans le contexte des développeurs mondiaux, tandis que TypeScript et Rust ont gagné en importance de manière significative.

La figure suivante montre la distribution des langues utilisées par les développeurs actifs dans tous les projets GitHub en 2020 et la distribution des langues utilisées par les 100 000 développeurs les plus actifs. En comparant la distribution des langues de projet, nous pouvons voir certaines fluctuations dans les classements.

![Image](https://uploader.shimo.im/f/IiqgJfInx4daKyXr.png!thumbnail)

JavaScript et Python sont des gagnants et des finalistes constants dans les classements, tandis que HTML et CSS sont clairement plus populaires dans le contexte de tous les développeurs GitHub. 

Cela est dû au grand nombre de sites de blogs et autres dépôts similaires sur GitHub. Ces projets sont généralement petits, indépendants et maintenus par des développeurs individuels.

### Les grandes entreprises comme Google et Microsoft sont des contributeurs majeurs à l'open source. 

De plus, le géant du commerce électronique Alibaba, dont le siège est en Chine, se classe au premier rang en termes de métrique d'activité parmi ses pairs, tandis que PingCAP a enregistré une performance impressionnante.

Selon la définition de la métrique d'activité des projets (détails dans le rapport complet), nous avons collecté des statistiques d'activité et le classement des projets actifs en 2020. 

Voici une liste des 20 projets les plus actifs au monde. Puisque ce rapport concerne 2020, les données utilisées dans ce tableau ont toutes été nouvellement générées en 2020 (les données historiques rapportées n'ont pas été incluses).

![Image](https://uploader.shimo.im/f/ewWjIC1qkM6DliIu.png!thumbnail)

Nous avons également collecté une liste de projets initiés par la Chine via divers canaux et donné un classement de la métrique d'activité des projets chinois.

![Image](https://uploader.shimo.im/f/vBHnAhK05haIDqQ7.png!thumbnail)

D'après la liste ci-dessus, nous avons constaté que PingCAP a une performance exceptionnelle dans l'open source. Ils représentent 6 projets sur la liste des 20 meilleurs projets. La contribution d'Alibaba dans l'open source est impressionnante. Ils ont 2 projets dans la liste des 10 meilleurs.

Baidu a démontré une performance exceptionnelle dans le domaine de l'intelligence artificielle. Deux projets de sa plateforme de deep learning PaddlePaddle, à savoir le framework principal Paddle et les bibliothèques d'outils connexes, ont fait la liste. 

La liste des 20 projets chinois les plus actifs comprend la bibliothèque de composants Ant Design d'Alibaba, le framework de développement taro de JD, basé sur le framework front-end React, et la bibliothèque de composants UI Element pour Vue, open-sourcée par l'équipe front-end d'Ele.me (acquis par Alibaba).

### Open Galaxy nous a aidés à obtenir une image plus complète 

Pour la première fois, nous avons pu voir une image plus complète des projets open source GitHub grâce à OpenGalaxy. Nous l'avons introduit dans le rapport.

Les résultats que nous obtenons par l'analyse de la métrique d'activité seront affectés par le comportement de collaboration automatisée. De plus, la métrique d'activité des projets de différents niveaux de maturité peut ne pas être comparable. 

Ainsi, dans ce rapport, nous avons utilisé OpenGalaxy, un réseau de relations collaboratives pour les projets mondiaux.

OpenGalaxy est basé sur la définition de la métrique d'activité des développeurs et établit une relation collaborative entre les projets par le biais des comportements de collaboration de tous les développeurs sur GitHub. Il fournit un moyen de calculer l'influence et le regroupement par le biais d'algorithmes de graphes.

Vous pouvez trouver la méthode de calcul spécifique dans le rapport complet.

![Image](https://uploader.shimo.im/f/krqTmc94ylG57peq.png!thumbnail)

Ce qui précède est un diagramme de réseau de collaboration composé des 221 000 projets open source les plus actifs sur GitHub en 2020. La taille du nœud dans la figure indique l'influence du projet, et la couleur du nœud indique le résultat de regroupement collaboratif auquel appartient le nœud.

Les 20 projets ayant la plus grande influence parmi tous les projets GitHub en 2020 ont été évalués sur l'influence du réseau collaboratif. Ils sont présentés dans le tableau suivant :

![Image](https://uploader.shimo.im/f/FVBoMaAsOY6r3bBz.png!thumbnail)

D'après le tableau, nous pouvons voir que VS Code a bondi à la 1ère place en termes d'influence, contre la 5ème place en termes d'activité. Avec son influence environ 64,7 % plus élevée que Flutter, qui se classe 2ème, VS Code est devenu le projet le plus influent au monde.

Nous avons construit un réseau de collaboration de développeurs pour VS Code en utilisant les journaux d'événements du dépôt de 2020, comme illustré dans la figure suivante.

![Image](https://uploader.shimo.im/f/3SrjeuxHRLualC7S.png!thumbnail)

Le réseau collaboratif est composé de plus de 20 000 développeurs. Les nœuds sont les comptes GitHub des développeurs, les arêtes sont les relations de collaboration, et la taille des nœuds reflète le niveau d'activité des comptes de développeurs correspondants. 

Dans ce réseau collaboratif, les nœuds plus grands au cœur du réseau sont les membres de l'équipe principale de VS Code. Ils ont non seulement une métrique d'activité élevée, mais aussi une relation collaborative élevée avec d'autres développeurs. Il y a environ une centaine de membres dans le groupe d'équipe. 

Les nœuds extérieurs qui suivent de près sont des utilisateurs actifs ou des contributeurs à VS Code. Ils peuvent soumettre des Issues ou des PR pour discussion ou contribution à tout moment. Les membres de ce groupe se comptent par milliers. 

Les développeurs les plus externes et les plus nombreux sont des utilisateurs généraux de VS Code et des contributeurs occasionnels, dont la plupart ne posent que des questions ou discutent des problèmes qui les concernent.

OpenGalaxy a une fonctionnalité qui lie les excellents projets par les excellents développeurs qui y travaillent. Par conséquent, l'indice d'influence ne sera pas faussement élevé en raison du comportement automatisé, mais aura plutôt une meilleure stabilité algorithmique. 

Puisque le changement d'influence révèle le changement d'activité de la communauté des développeurs, l'influence devient une meilleure métrique pour refléter le niveau d'influence d'un projet parmi tous les projets GitHub.

### 9. Open Source Quadrant va plus loin

Dans le rapport, nous avons également introduit Open Source Quadrant, qui peut distinguer davantage les différentes étapes de développement et les niveaux de maturité des projets open source similaires.

L'analyse du quadrant open source est représentée par un nuage de points. Les dimensions horizontale et verticale indiquent respectivement l'influence du projet et la mondialisation du projet. 

Nous utilisons la forme logarithmique des deux indicateurs et la taille des points pour dépeindre le nombre de participants actifs dans le projet ainsi que pour refléter l'échelle d'une communauté.

Vous pouvez trouver les méthodes de calcul spécifiques pour l'influence, la mondialisation et le nombre de participants dans le rapport complet.

Voici un exemple d'analyse du **Open Source Quadrant** des projets Linux Foundation AI et Data :

![Image](https://uploader.shimo.im/f/21BE7xA2gFGCT3q5.png!thumbnail)

### La communauté open source est diverse et robuste

Les cartes de distribution des fuseaux horaires des développeurs et les réseaux de collaboration des développeurs sont devenus des moyens efficaces de refléter la diversité et la robustesse des communautés open source. Et ils peuvent nous aider à mieux gérer la communauté open source.

Nous prendrons les projets Linux Foundation AI et Data comme exemple.

![Image](https://uploader.shimo.im/f/sHn39h0qplzPFrMP.png!thumbnail)

Nous pouvons voir que la distribution des fuseaux horaires des développeurs des projets dans ce domaine a beaucoup changé par rapport à tous les projets GitHub. Environ 16 % des développeurs proviennent des fuseaux horaires UTC+7 à UTC+8. 

Dans ces fuseaux horaires, les développeurs chinois sont les plus impliqués, ce qui reflète que la Chine compte plus de praticiens en données et en intelligence artificielle.

## Qu'avons-nous appris d'autre ?

Nous avons réalisé des études de cas approfondies sur les réseaux de collaboration des développeurs au sein de projets spécifiques de la Cloud Native Computing Foundation (CNCF), de la Linux Foundation (LF) et de l'Apache Software Foundation (ASF), entre autres.

### Projet du Mois

En plus des projets de haut niveau, certains projets sur GitHub ont reçu beaucoup d'attention de la part des développeurs en peu de temps. Ces projets peuvent être des projets phares, ils peuvent devenir des projets de haut niveau à l'avenir, ou ils peuvent être liés à des sujets d'actualité, comme la pandémie de COVID-19. 

Il est significatif de découvrir et d'expliquer pourquoi ils ont reçu beaucoup d'attention pendant une période spécifique. Par conséquent, la section Projet du Mois liste les projets qui ont reçu beaucoup d'attention chaque mois en 2020.

Sur la base des données de journaux, les projets qui ont reçu le plus d'étoiles par mois ont été sélectionnés en premier, puis nous avons choisi un exemple pour chaque mois.

* Janvier : microsoft/playwright
* Février : wuhan2020/wuhan2020
* Mars : CSSEGISandData/COVID-19
* Avril : labuladong/fucking-algorithm
* Mai : design-resources-for-developers
* Juin : CnC_Remastered_Collection
* Juillet : JaidedAI/EasyOCR
* Août : geekxh/hello-algorithm
* Septembre : cli/cli
* Octobre : developer-roadmap
* Novembre : ytdl-org/youtube-dl
* Décembre : beurtschipper/Depix

## Résumé et Perspectives

En tant qu'outil de visualisation basé sur les données, le **Rapport GitHub 2020 Digital Insight** vous offre principalement une nouvelle perspective sur le monde de l'open source d'aujourd'hui ainsi que des insights issus de l'intersection avec les expériences industrielles. 

À partir de ce rapport annuel, nous maintiendrons également le travail en tant que projet open source, raccourcirons le cycle de publication et fournirons des services de conseil professionnels sur demande.

Vous pouvez obtenir le rapport complet à partir de ce lien : [http://oss.x-lab.info/github-insight-report-2020-en.pdf](http://oss.x-lab.info/github-insight-report-2020-en.pdf)

Si vous trouvez des erreurs ou des omissions dans les données, veuillez soumettre une Issue ou une PR à GitHub. Le texte de ce rapport adopte l'accord de licence CC-BY-4.0, et l'adresse du projet est : [https://github.com/X-lab2017/github-analysis-report](https://github.com/X-lab2017/github-analysis-report)

## Remerciements

Le Rapport GitHub 2020 Digital Insights a été initié par X-lab, planifié par le média technologique open source Allumos, et réalisé conjointement avec l'Université normale de Chine orientale, Kaiyuanshe, l'Association de technologie de l'information open source de Shanghai, ainsi que de nombreuses autres institutions de recherche scientifique et instituts de la communauté open source.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-27.png)

Les contributeurs à ce rapport sont :

Shengyu (Frank) Zhao, Wei (Will) Wang, Tianyi Zhou, Zhenjie Weng, Haoyue Wang, Xiaoya Xia, Xiangning Zhu, Ming Yang, Zexin Ning, Haiming Lin, Fuzheng Wang, Jingben Shi, Zehua Lou, Yeming Gu, Xue (Xander) Wu, Jia (Kate) Yang, Siying (Mabel) Li.

Les contributeurs à la version anglaise du rapport sont :

Xue (Xander) Wu, Puyu (Paul) Wang, Xiaoya Xia, Shengyu (Frank) Zhao, Xiaotian Dai, Siying (Mabel) Li, Yu (Atena) Chen. Un mot de remerciement spécial à [Aleksey Zaitsev](https://vistal.media/) (WeChat : vistal-media) pour son aide inestimable dans l'édition.

Nous accueillons avec plaisir plus d'enthousiastes de l'open source pour nous rejoindre et promouvoir conjointement le développement de l'open source dans le monde.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-26.png)