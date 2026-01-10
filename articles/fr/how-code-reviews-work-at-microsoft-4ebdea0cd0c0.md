---
title: Comment fonctionnent les revues de code chez Microsoft
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T08:00:57.000Z'
originalURL: https://freecodecamp.org/news/how-code-reviews-work-at-microsoft-4ebdea0cd0c0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GWGY5OFKBHznk598
tags:
- name: code review
  slug: code-review
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment fonctionnent les revues de code chez Microsoft
seo_desc: 'By Michaela Greiler

  Have you ever wondered how one of the largest software companies world wide ensures
  high quality code through code reviewing?

  So did I. That’s why together with my colleagues at Microsoft, we investigated how
  code reviews are done...'
---

Par Michaela Greiler

Vous êtes-vous déjà demandé comment l'une des plus grandes entreprises de logiciels au monde assure une qualité de code élevée grâce aux revues de code ?

Moi aussi. C'est pourquoi, avec [mes collègues](https://www.michaelagreiler.com/category/code-reviews/#ms-peers) chez Microsoft, nous avons étudié comment les revues de code sont effectuées dans notre entreprise. Est-ce une pratique courante ? Les développeurs sont-ils tenus de faire des revues de code ? Et quels outils utilisent-ils ?

Découvrons-le dans cet article, qui fait partie d'une [**série plus large d'articles de blog sur les revues de code**](https://www.michaelagreiler.com/code-review-blog-post-series/).

Pour commencer, laissez-moi vous donner quelques informations clés sur Microsoft. [Microsoft compte environ 140 000 employés](https://news.microsoft.com/facts-about-microsoft/#EmploymentInfo). Environ 44 % d'entre eux, soit plus de 60 000 employés, sont des ingénieurs. Plusieurs produits tels qu'Office, Visual Studio ou Windows sont développés par des milliers d'ingénieurs qui travaillent sur la même base de code simultanément.

Je dis tout cela pour vous donner un contexte et une perspective de ce que signifie coordonner et gérer le processus de développement logiciel. Comme vous pouvez l'imaginer, il est non trivial de s'assurer que le code développé par différentes sous-équipes fonctionne parfaitement ensemble. Et les revues de code jouent un rôle important chez Microsoft pour permettre une collaboration fluide à une si grande échelle.

### Les revues de code chez Microsoft font partie intégrante du processus de développement

L'un des faits importants concernant les revues de code chez Microsoft est qu'il s'agit d'une pratique d'ingénierie largement adoptée. Des milliers d'ingénieurs la perçoivent comme une excellente meilleure pratique. Et la plupart des équipes performantes passent beaucoup de temps à faire des revues de code.

[Chez Microsoft, la revue de code est une pratique d'ingénierie largement adoptée et perçue comme une excellente meilleure pratique. Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/&text=%20Chez%20Microsoft%2C%20la%20revue%20de%20code%20est%20une%20pratique%20d'ingénierie%20largement%20adoptée%20et%20perçue%20comme%20une%20excellente%20meilleure%20pratique.%20%20&via=mgreiler&related=mgreiler).

### Enquête sur les revues de code chez Microsoft

Parce que les revues de code jouent un rôle si important dans le processus de développement de Microsoft, c'était une cible idéale pour nous d'approfondir et de vraiment comprendre les avantages et les inconvénients de cette pratique. [Dans une étude à grande échelle sur les revues de code chez Microsoft,](https://www.michaelagreiler.com/wp-content/uploads/2019/03/Code-Reviewing-in-the-Trenches-Understanding-Challenges-Best-Practices-and-Tool-Needs.pdf) nous avons interviewé, observé et interrogé plus de 900 développeurs sur leurs pratiques de revue de code.

Notre objectif était de comprendre comment les revues de code sont exactement effectuées chez Microsoft, quels défis les développeurs rencontrent lors des revues de code, et de distiller quelles sont les meilleures pratiques qu'ils développent pour surmonter ces défis.

### Que pouvez-vous apprendre des pratiques de revue de code chez Microsoft ?

La plupart des leçons apprises sont aussi précieuses pour les petites équipes et organisations que pour les grandes équipes et grandes organisations. Si votre équipe ne fait pas encore de revues de code, j'ai distillé nos conclusions de manière à vous montrer les avantages de cette pratique. J'explique également à quoi ressemble le cycle de vie de la revue de code afin que vous puissiez incorporer cette pratique dans votre propre processus de développement.

Si votre équipe fait déjà des revues de code, vous pouvez comparer votre pratique avec la pratique de revue de code chez Microsoft. Votre cycle de vie de revue de code est-il différent ? Dans les prochains articles, vous apprendrez des défis qui surviennent lors des revues de code et des meilleures pratiques. Avec ces informations, vous pourrez voir si votre équipe met déjà en œuvre toutes les meilleures pratiques que je présente et surmonter les défis. Mais commençons :

### À quelle fréquence les ingénieurs de Microsoft effectuent-ils des revues de code ?

Dans cette étude, 36 % des développeurs ont déclaré effectuer des revues de code plusieurs fois par jour. Un autre 39 % des développeurs ont déclaré faire des revues de code au moins une fois par jour. 12 % font des revues de code plusieurs fois par semaine, et seulement 13 % ont déclaré ne pas avoir fait de revue de code la semaine précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/K3jMFIgEEHEn8kADlr7CUZnBrg-4rFnFYtIj)

Cela signifie que les développeurs chez Microsoft passent une partie importante de leur temps sur les revues de code. Il est donc important de s'assurer que ce temps est bien utilisé. Mais quels sont les avantages des revues de code ?

### Quels sont les avantages des revues de code ?

Les raisons les plus importantes que les développeurs ont mentionnées comme avantages des revues de code sont l'amélioration de la qualité du code et la détection des défauts dans le code. Un autre avantage important des revues de code est le transfert de connaissances.

Le transfert de connaissances signifie que les membres de l'équipe qui examinent le code les uns des autres deviennent familiers avec une plus grande partie de la base de code. Mais cela signifie également que les meilleures pratiques sont développées au sein de l'équipe. Un autre avantage est que les nouveaux membres de l'équipe et les développeurs juniors peuvent apprendre et améliorer leurs compétences en codage tout en examinant ou en recevant des commentaires.

Si les développeurs discutent de solutions alternatives lors des revues de code, cela améliore non seulement la base de code, mais a également un effet d'apprentissage pour tous les participants. L'apprentissage, le mentorat et l'auto-amélioration sont donc toutes des raisons pour lesquelles la revue de code est perçue comme une pratique si bénéfique chez Microsoft.

![Image](https://cdn-media-1.freecodecamp.org/images/J4xPSMk926cmcD0tTDWcePiZ4aGfxMDDUQfn)

Les développeurs font des revues de code pour améliorer le code, trouver des défauts, mais surtout pour augmenter le transfert de connaissances entre les membres de l'équipe et pour les effets d'apprentissage. [Cliquez pour tweeter](https://twitter.com/intent/tweet?url=https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/&text=Les%20développeurs%20font%20des%20revues%20de%20code%20pour%20améliorer%20le%20code%2C%20trouver%20des%20défauts%2C%20mais%20surtout%20pour%20augmenter%20le%20transfert%20de%20connaissances%20entre%20les%20membres%20de%20l'équipe%20et%20pour%20les%20effets%20d'apprentissage.&via=mgreiler&related=mgreiler).

### Mais comment un développeur effectue-t-il généralement des revues de code ?

Les revues de code peuvent être effectuées de nombreuses manières. Parfois, c'est aussi informel qu'un développeur se rendant au bureau d'un autre développeur pour regarder du code ensemble. D'autres fois, les équipes examinent le code ensemble en groupe. Mais le scénario le plus probable que vous rencontrerez pour les revues de code chez Microsoft est que les revues de code sont effectuées à l'aide d'outils.

#### Les revues de code chez Microsoft sont le plus souvent effectuées via un outil interne

Il existe une grande variété d'outils de revue de code disponibles, et chez Microsoft, les équipes sont libres de choisir leurs outils. En 2016, 89 % des développeurs indiquaient utiliser l'outil de revue de code CodeFlow. Je vais expliquer plus en détail cet [outil de revue de code chez Microsoft](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/#ms-tool) plus tard. Depuis lors, et avec l'essor de Git, le paysage des outils a changé. Je vais ajouter des chiffres mis à jour dès qu'ils seront disponibles. Mais considérons une situation de revue typique :

Imaginons un développeur chez Microsoft, et appelons-la Rose. Rose vient de terminer une partie d'une fonctionnalité et souhaite maintenant des commentaires de ses pairs.

#### Comment Rose commence-t-elle une revue de code chez Microsoft ?

Eh bien, comme dit, Rose est prête à obtenir des commentaires. Elle prépare donc d'abord le code pour la revue. Cette étape inclut l'ouverture de l'outil de revue de code, qui lui permet de prévisualiser les modifications du code. L'outil de revue de code effectue certaines tâches de différenciation qui aident Rose à voir exactement quelles modifications elle a apportées.

Après avoir soigneusement examiné ces modifications, elle prépare une petite note qui indique aux réviseurs ce qu'elle a fait et pourquoi elle l'a fait. Cette note aide les réviseurs à comprendre le but de la modification du code et sa motivation. Le code est maintenant prêt à être envoyé aux réviseurs.

#### Comment Rose sélectionne-t-elle les bons réviseurs de code ?

De nombreux développeurs expérimentés savent qui doit être inclus dans la revue de code. Néanmoins, pour les nouvelles personnes dans l'équipe, ou pour de nouveaux domaines de travail, la sélection peut être un peu plus délicate. Si Rose ne sait pas qui elle doit ajouter, elle peut soit consulter les politiques de l'équipe, soit demander à ses collègues. Elle peut également utiliser une fonctionnalité de recommandation de l'outil de revue de code qui aide à sélectionner les réviseurs en fonction de leur expérience et de leurs connaissances de la base de code.

#### Qui sont les réviseurs pertinents ?

Rose sélectionne les réviseurs qu'elle pense pouvoir contribuer à ce morceau de code. Les réviseurs sont souvent d'autres développeurs, mais peuvent également inclure d'autres parties prenantes, telles que des ingénieurs dev-ops, des experts en UI, ou même des managers. Certains réviseurs sont sélectionnés pour leur expertise, d'autres sont sélectionnés afin de rester informés d'un changement à venir.

![Image](https://cdn-media-1.freecodecamp.org/images/Siud62YVmYXQ1xe6xFrPMeFcZR-nkz7zrh26)

#### Rose demande des commentaires à ses pairs

Une fois que tout le monde est sélectionné, Rose envoie la revue de code (en appuyant sur le bouton d'envoi ?). L'outil de revue de code envoie automatiquement des notifications pour informer tout le monde qu'une revue de code a été créée. Les notifications sont envoyées à tous les réviseurs. Mais souvent, des parties supplémentaires, telles que des managers ou des chefs de produit d'autres équipes, sont également ajoutées à la liste de notification et sont automatiquement informées pour chaque revue. Ces notifications leur permettent de rester informés. Ils ne sont pas tenus d'effectuer la revue.

#### Recevoir des commentaires est un processus itératif

Une fois que les collègues de Rose ont le temps, ils examineront la revue de code. Chaque réviseur peut annoter le code et ajouter des commentaires. Une fois les commentaires terminés, le réviseur envoie le code annoté à Rose. Rose peut maintenant travailler sur les commentaires et préparer une nouvelle version améliorée du code.

Les réviseurs recherchent généralement des choses comme : le code semble-t-il exempt de bugs ? Y a-t-il un problème architectural ? Y a-t-il des problèmes mineurs tels que des commentaires manquants, des fautes d'orthographe ? Tous les commentaires ne sont pas également précieux. Mais il existe [plusieurs meilleures pratiques pour augmenter la valeur des commentaires de revue de code.](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/boosting-code-reviews-useful-comments)

#### Rose prépare une nouvelle version améliorée du code

Rose travaille sur les commentaires en corrigeant et en traitant les suggestions. Si Rose voit qu'il y a des malentendus ou d'autres problèmes contentieux, elle peut se rendre au bureau d'un collègue pour en discuter en personne. C'est parfois plus facile et plus personnel que par le biais de l'outil.

Quoi qu'il en soit, une fois qu'elle a terminé de travailler sur tous les commentaires, elle envoie une nouvelle version du code aux réviseurs. Cette nouvelle version améliorée est appelée une révision.

Si nécessaire, elle recevra d'autres commentaires. Que ce cycle continue quelques fois dépend du type de changement et de sa qualité. Pour des changements de code simples et petits, une seule révision de revue de code est souvent nécessaire. Pour d'autres changements plus complexes ou des changements dans du code problématique, plusieurs itérations peuvent être nécessaires.

Il est tout à fait normal, et en partie souhaitable, que ce cycle de commentaires de revue de code suscite des discussions entre l'auteur et les réviseurs de code.

#### Tous les réviseurs approuvent et Rose valide le code

Après ce cycle de revue, les réviseurs marquent le code comme étant correct, et Rose peut enfin valider le code dans la base de code commune.

Certaines équipes ont des politiques qui permettent au développeur de valider le code avant qu'une revue réelle ne soit terminée. Cela est normalement restreint aux changements petits et triviaux, afin de permettre des revues asynchrones et d'accélérer le développement.

Toutes les étapes que je décris font partie d'un cycle de vie typique de revue de code chez Microsoft et sont effectuées par toutes les équipes. Selon les politiques de l'équipe, les équipes sont plus strictes ou rigoureuses pour chacune des étapes.

### Toutes les équipes ne sont pas identiques

Comme vous pouvez l'imaginer, tous les 60 000 ingénieurs, et toutes les milliers d'équipes ne font pas la même chose. Certaines équipes chez Microsoft ont des étapes ou des outils supplémentaires qu'elles exigent lors du cycle de vie de la revue de code. Je veux vous donner un bref aperçu de certaines étapes supplémentaires que les équipes ajoutent au processus de revue de code.

### Revues de code incluant les résultats des tests

Le moins que vous voulez, c'est de perdre du temps en examinant du code "buggé détectable automatiquement". Je veux dire, si vous pouvez exécuter des tests automatisés et réaliser que le code ne fonctionne pas comme prévu, alors c'est ce que vous devriez faire : exécuter les tests avant la revue.

C'est pourquoi certaines équipes exigent que les résultats des tests soient soumis avec chaque revue de code. De cette façon, personne ne peut oublier d'exécuter les tests. Et cela garantit que les tests ont effectivement été exécutés et réussis pour le changement de code donné.

D'autres équipes sont allées encore plus loin et ont configuré l'outil de revue de code de manière à ce que pour chaque revue de code qu'un développeur soumet, une build soit déclenchée. Cette build contient ce changement exact, et lance également une série de tests automatisés. Les résultats de cette build et de ces tests sont joints à la revue de code. Configurer cela de cette manière garantit que les changements de code ont été testés avec les derniers changements de code de la base de code commune.

### Revues de code incluant l'interface utilisateur

Si les changements affectent l'interface utilisateur, il est également judicieux d'exiger du développeur qu'il soumette une capture d'écran. De cette façon, le réviseur de code peut voir les effets du changement de code sans exécuter le code. Deuxièmement, le réviseur de code peut repérer les divergences lors de l'exécution du code sur sa propre machine.

### Revues de code incluant l'analyse statique

Les outils d'analyse statique ne sont aussi bons que leur configuration, mais en termes de problèmes de style, ils peuvent faire gagner beaucoup de temps aux réviseurs de code. Certaines équipes chez Microsoft utilisent des outils automatisés d'analyse statique et dynamique comme des réviseurs bots dédiés. Ces bots commentent le style de code et d'autres problèmes statiques. Ainsi, libérant du temps pour les réviseurs de code humains pour effectuer des tâches plus intéressantes.

### L'outil de revue de code de Microsoft

Pendant de nombreuses années, l'un des standards de facto pour la revue de code chez Microsoft était un outil interne appelé CodeFlow. Il s'agit d'un outil sophistiqué de revue de code qui soutient les développeurs et les guide à travers toutes les étapes d'une revue de code. CodeFlow aide lors de la préparation du code, notifie automatiquement les réviseurs et dispose d'une fonctionnalité riche de commentaires et de discussion.

CodeFlow est un outil lourd en UI, un peu comme Word ou PowerPoint, comme vous pouvez le voir dans la capture d'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/CnMpM1uqn911onDKhvrJ2AVuXg0lz035cMg8)

#### Interface de CodeFlow expliquée

Vous pouvez sauter cette partie si vous le souhaitez, mais pour tous ceux qui sont intéressés, je vais vous guider à travers l'interface de CodeFlow. En regardant la capture d'écran, à gauche (A) vous voyez tous les documents affectés.

Également à gauche, vous voyez (B) la liste des réviseurs assignés à la revue ainsi que leur statut (par exemple, signé ou en attente). Le document actif est affiché dans l'éditeur (C). En bas, vous voyez (D) une liste de commentaires pour tous les documents.

D'autre part, dans le document actif (F) se trouve un seul commentaire. Ce commentaire est lié à la partie concrète du code (c'est-à-dire un mot dans une ligne). Enfin, en haut, vous voyez le statut global de la revue de code. Dans ce cas, terminé. Les nombres avant signalent les différentes révisions. Dans cette revue, il y a eu cinq révisions.

#### Fonctionnalité de commentaire

L'une des plus belles fonctionnalités de CodeFlow est sa fonctionnalité de commentaire.

Un réviseur de code peut sélectionner très précisément les parties du code qu'il souhaite commenter. Par exemple, un réviseur peut même surligner un ou deux caractères dans une ligne, au lieu de surligner toute une ligne. Ensuite, le réviseur peut attacher un commentaire à cette sélection.

L'auteur du code ou d'autres réviseurs sont informés de ce commentaire et peuvent commencer une conversation sous forme de fil de discussion autour de ce commentaire.

#### Fonctionnalité de discussion

Cette fonctionnalité de commentaire ressemble à celle des plateformes de médias sociaux, comme Twitter ou Facebook. Par conséquent, l'expérience de commentaire dans CodeFlow est très naturelle et permet des conversations et des discussions riches. Un autre avantage est la possibilité d'attribuer un statut à chacun de ces fils de commentaires. Le statut peut, par exemple, être "ne sera pas corrigé", "résolu" ou "ouvert".

### Comparaison entre les révisions de revue de code

Une fonctionnalité utile est la possibilité de sélectionner deux révisions différentes de la revue de code et de comparer les différences entre elles. Cela signifie que vous pouvez voir exactement quelles modifications l'auteur de la revue de code a effectuées entre une révision de revue de code et une autre. C'est super pratique pour suivre les progrès de la revue.

### Outil d'analyse de revue de code

Les développeurs passent une partie importante de leur temps à effectuer des revues de code chez Microsoft. Pour s'assurer que ce temps est bien utilisé, Microsoft dispose de sa propre plateforme d'analyse de revue de code.

Cette plateforme stocke toutes les données de revue de code, depuis le code en revue, les développeurs impliqués dans les revues de code, jusqu'à tous les commentaires des développeurs. Même les changements de code pour chacune des révisions peuvent être retracés.

Ces [données de revue de code sont la base de plusieurs études empiriques](https://queue.acm.org/detail.cfm?id=3292420) sur les revues de code chez Microsoft. Elles sont également utilisées par de nombreuses équipes produit pour suivre leur productivité et comprendre leurs propres pratiques de revue de code. De plus, de nombreuses informations que je partage dans [cette série d'articles de blog sur les revues de code chez Microsoft](https://www.michaelagreiler.com/code-review-blog-post-series/) proviennent d'études et d'analyses qui ont impliqué ces données de revue de code.

### L'avenir de la revue de code chez Microsoft

Avec l'engagement de Microsoft et l'acquisition de GitHub, le changement était inévitable. Le changement est visible par l'adoption massive de Git comme outil de contrôle de source au sein de Microsoft, par exemple. Mais cela signifie également que chez Microsoft, la revue de code sous forme de pull requests est en hausse.

Je prévois définitivement d'aborder la revue de code en utilisant les pull requests à un moment ultérieur.

### À venir : Les défis de la revue de code

Je vais écrire sur les défis de la revue de code dans le prochain article de blog. Pour **rester informé** et **me suivre** sur medium.

**Crédit là où le crédit est dû :**

Je tiens à mentionner mes merveilleux collègues chez Microsoft et à l'Université de Victoria qui ont fait partie de cette étude : [Chris Bird](https://www.microsoft.com/en-us/research/people/cbird/), [Jacek Czerwonka](https://www.microsoft.com/en-us/research/people/jacekcz/) et [Laura Macleod](http://lmacleod.com/) et [Margaret-Anne Storey](http://margaretstorey.com/). J'ai adoré travailler avec vous sur ce f495

_Publié à l'origine sur [www.michaelagreiler.com](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/) le 27 mars 2019._