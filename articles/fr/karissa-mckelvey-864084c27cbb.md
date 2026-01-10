---
title: 'Entre les fils : Une interview avec la scientifique des données Karissa McKelvey'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-25T19:34:29.000Z'
originalURL: https://freecodecamp.org/news/karissa-mckelvey-864084c27cbb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WuWI9sddH7sTIL9B.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: 'Entre les fils : Une interview avec la scientifique des données Karissa
  McKelvey'
seo_desc: 'By Vivian Cromwell

  I interviewed Karissa McKelvey, who is the Director of Engineering at Dat Project,
  a distributed data sharing tool that packages your data and shares it over a distributed
  network.

  How did you get into programming?

  I went to a publ...'
---

Par Vivian Cromwell

J'ai interviewé [Karissa McKelvey](https://twitter.com/okdistribute), qui est la directrice de l'ingénierie chez [Dat Project](https://datproject.org/), un outil de partage de données distribué qui package vos données et les partage sur un réseau distribué.

#### **Comment avez-vous commencé la programmation ?**

Je suis allée dans une école publique. Comme la plupart des adolescents de 13 ans, je voulais simplement réussir mes examens. À un moment donné, j'ai commencé à programmer sur la calculatrice TI-83. Je la donnais à mes amis en échange d'un déjeuner supplémentaire ou de cartes Magic. C'est ainsi que j'ai commencé à m'intéresser à la programmation. Après cela, j'ai commencé à créer des sites web au lycée pour des jeux vidéo auxquels je jouais.

Je ne pensais pas vraiment que c'était de la programmation à l'époque, car tout ce que je faisais, c'était simplement résoudre les problèmes dont j'avais besoin. Je n'ai pas vraiment choisi l'informatique lorsque j'ai décidé d'aller à l'université. J'ai en fait choisi les sciences politiques parce que je m'intéressais beaucoup à la politique et aux débats. À l'époque, j'ai mis la programmation de côté jusqu'à ce que je réalise que c'était quelque chose que je voulais faire, alors j'ai fini avec un double diplôme à l'université.

Plus tard, je suis entrée dans un programme de doctorat en informatique à l'Université de l'Indiana. Le principe était d'appliquer l'informatique à un domaine particulier. Entre 2010 et 2014, j'ai collecté beaucoup de données de Twitter via mon laboratoire, Complex Networks and Systems Research. Pendant les mouvements sociaux et les grands événements politiques, nous avons pu examiner comment les nouvelles et les idées se répandaient en ligne. C'était excitant de voir le tableau complet, et c'est ainsi que j'ai commencé à m'intéresser à l'analyse de données.

![Image](https://cdn-media-1.freecodecamp.org/images/GtYyLtBftWxSX-kjE9Oycv35yo-A9I3K6X9Q)

#### **Comment vous êtes-vous impliquée dans le projet Dat ?**

On pourrait penser que les chercheurs sont très intelligents et disposent de tous les systèmes parfaits qui intègrent les données de toutes les différentes sources. On pourrait supposer qu'il doit être très facile de transférer des données entre les personnes. Mais ce n'était pas du tout le cas. Il était vraiment difficile de travailler avec les données à l'université. Certains groupes avaient développé des entrepôts de données et des flux de travail internes, mais la plupart des laboratoires avaient du mal à collaborer et à partager des données.

J'ai trouvé cela très pénible lorsque j'ai quitté mon programme de doctorat et que j'ai commencé à faire de la visualisation de données. J'ai travaillé chez Continuum Analytics et chez Google, puis j'ai rejoint une startup appelée Datapad. Un an plus tard, j'ai trouvé [Max Ogden](https://twitter.com/denormalize) et le [Dat Project](https://twitter.com/dat_project), je lui ai envoyé un message sur Twitter concernant le partage de données, et me voilà aujourd'hui.

#### **Qu'est-ce que le projet Dat ?**

![Image](https://cdn-media-1.freecodecamp.org/images/uLzGJ0u0YzpeHq-A7inUbYL8N-hPDFWW9M9A)
_Logo du projet Dat_

[Dat](https://datproject.org/) est un outil de partage de données distribué qui package vos données et les partage sur un réseau distribué. Cela signifie que nous prenons les meilleures parties de [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent), qui est un réseau distribué, et les meilleures parties de [Git](https://en.wikipedia.org/wiki/Git), où vous avez un historique des versions, et vous les combinez. Il n'utilise pas réellement Git ou BitTorrent, mais il s'inspire de ces deux projets pour construire quelque chose de plus robuste et plus résilient aux pannes de données.

Nous travaillons sur cela depuis trois ans et demi. Max a obtenu une subvention de la [Knight Foundation](https://knightfoundation.org/) pour faire un prototype. Depuis, il a subi trois itérations de conception, de mise en œuvre et de test. Pour l'instant, la plupart de nos utilisateurs sont des scientifiques, car nous avons fait du marketing et travaillé avec eux sur des cas d'utilisation scientifiques. C'est aussi très utile pour d'autres types de choses, ce qui est le grand avantage d'avoir une plateforme polyvalente pour un usage général.

Le problème avec BitTorrent est que les utilisateurs ne peuvent pas mettre à jour les données au fil du temps car le hachage et le lien pour trouver les données changent à chaque fois. Nous avons trouvé un moyen de contourner ce problème en créant une clé publique qui ne change pas, et la personne qui a généré la clé peut ajouter plus de données au fil du temps en utilisant la clé privée. Les personnes qui ont accès aux données peuvent consulter l'historique et revenir en arrière, elles peuvent également rechercher une certaine plage d'octets dans un fichier, ce qui est un outil vraiment puissant et utile.

#### **Comment fonctionne le financement par subventions pour Dat ?**

Max a obtenu la première subvention de 50 000 $ de la Knight Foundation pour travailler sur le prototype. Cela a duré 6 à 9 mois, puis quelqu'un de la [Sloan Foundation](https://sloan.org/) qui s'intéressait au projet a approché Max et a dit : « Hé, appliquons cela à la science. » La Sloan Foundation finance des outils utiles pour les scientifiques et pour faire avancer l'intégrité et l'efficacité de la recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/0mVtv7fxSOmOlQOot0q9m3z1mRa214yFYIBc)
_Knight Foundation_

Max a commencé à construire une équipe alors que nous continuions à obtenir plus de subventions des fondations Sloan et Knight. L'ensemble du projet a été entièrement financé par des subventions. La partie la plus grande et la plus importante concernant l'obtention de subventions est d'être approché par un responsable de subvention et de le convaincre que votre projet en vaut la peine. Le travail du responsable de subvention est de donner de l'argent à des projets auxquels ils croient ou aux projets qu'ils croient remplir la mission de la fondation.

![Image](https://cdn-media-1.freecodecamp.org/images/iej8sGfFWN1T5PI5ioWNDWfEYd0YClWOGToC)
_Sloan Foundation_

Chaque financeur est différent. Parfois, ils ne veulent vous donner que 20 000 $ ou 50 000 $, et d'autres fois, ils veulent vous donner un demi-million de dollars. Ils essaient toujours de promouvoir le bien public et général.

#### **Si une fondation vous accorde un ensemble de subventions, comment les attentes sont-elles définies ?**

La première chose à faire est de rédiger votre proposition, qui peut aller de 12 à 200 pages. Dans la proposition, vous devez indiquer quels sont vos objectifs. Si c'est une subvention d'un an et demi, vous pourriez dire : « Dans trois mois, nous aurons embauché une équipe. Dans sept mois, nous aurons terminé les tests utilisateurs, nous aurons un ensemble de designs et la version alpha. » Tout ce qui peut donner au financeur une idée claire de ce qui va venir.

Vous voulez définir ces objectifs dans la proposition ainsi que des métriques, telles que le nombre d'utilisateurs et de téléchargements. À des intervalles prédéfinis, comme six mois, vous devez faire un court rapport pour informer de l'avancement du projet et de la manière dont vous vous en sortez avec les métriques. Les personnes qui donnent de l'argent veulent s'assurer que leur argent est utilisé correctement.

#### **Comment les responsables de subventions et les ingénieurs se trouvent-ils pour collaborer ?**

Il existe plusieurs façons de se faire présenter à un responsable de subvention, mais je préfère personnellement m'en tenir à deux.

La première façon, dans le contexte d'une conférence ou d'une convention, est d'avoir une présentation solide qui attire l'attention des responsables de subventions dans la salle. Ainsi, ils vous approcheront concernant le projet. Une autre façon est de se faire présenter à des responsables de subventions par quelqu'un que vous connaissez, et c'est à ce moment-là que vous devez vraiment mettre en place des connexions.

Il y a une autre façon, qui est la plus visible mais probablement la moins efficace pour obtenir la subvention, et c'est de postuler via des formulaires en ligne ou des compétitions. Habituellement, c'est leur façon d'intégrer de nouveaux venus dans le groupe. Si vous n'avez pas encore eu votre grande chance, participer à l'un des forums en ligne ou des défis peut aider. Mais vous devez avoir des attentes réalistes car il y a beaucoup de gens qui postulent et la compétition est vraiment féroce.

#### **Comment les fondations de subventions perçoivent-elles l'open source ?**

L'open source est un moyen pour les gens de faire en sorte que leurs projets continuent de réussir même s'ils ne sont pas financés et même si le projet n'a pas atteint ses objectifs. C'est un bon moyen de contribuer à la communauté à long terme. Lorsque vous avez quelque chose qui est fermé, il meurt avec l'idée, l'entreprise ou l'organisation.

Beaucoup de fondations de subventions s'efforcent d'être altruistes, donc l'open source s'inscrit dans leur stratégie, car elles veulent simplement financer des projets qui seront utiles pour le public. Cela permet ensuite à beaucoup d'autres créateurs et entrepreneurs de s'intéresser et de s'impliquer dans votre mission.

#### **Dat fonctionne avec une équipe très distribuée. Parlez-nous de vos meilleures pratiques en matière de productivité et de communication d'équipe. Quels outils utilisez-vous ?**

GitHub a énormément aidé avec l'équipe distribuée — Mathias Buus, à Copenhague ; Max Ogden et Joe Hand à Portland ; Yoshua Wuyts, Julian Gruber et Kristina Schneider à Berlin, et Chia-liang Kao à Taïwan. Nous essayons d'éviter la communication privée dans l'équipe, donc tout est fait dans l'IRC public. Nous avons des réunions quotidiennes pour couvrir ce que nous faisons ce jour-là et un appel bi-hebdomadaire pour nous mettre à jour sur notre situation actuelle, et à partir de là, nous planifions ce qui se passe ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/imukH1Jpp7AoNRwxfUBIdiRU75VJntf-PlCf)

Faire tout en public aide les autres personnes qui ne sont pas dans l'équipe à collaborer avec nous en tant que contributeurs open source. « Open source », dans mon esprit, est synonyme de « distribué ».

C'est génial que nous n'ayons pas une équipe de plus de trois personnes. L'un des points clés est d'avoir une petite équipe et concentrée. Je pense que les gens travaillent mieux en groupes de deux ou trois. Plus que cela, et il devient difficile de parvenir à des conclusions. Lorsque les gens prennent possession de leur partie du projet, ils se sentent habilités à prendre des décisions. En même temps, ils peuvent également obtenir des contributions d'autres personnes de manière horizontale.

#### **Qu'est-ce que Code for Science and Society ?**

![Image](https://cdn-media-1.freecodecamp.org/images/U-3RW4LjioNTEJF6QEysM0daUnNhDpg4zHcZ)

[Code for Science and Society](https://codeforscience.org/) est une organisation à but non lucratif qui parraine fiscalement les personnes qui veulent obtenir un projet basé sur une subvention.

Le parrainage fiscal est essentiellement ce qui se passe lorsque vous obtenez une subvention, et peu importe la taille du chèque, vous ne pouvez pas simplement accepter cet argent en tant qu'individu. Vous avez besoin d'une organisation qui va prendre la responsabilité pour vous. La fondation donne l'argent à une organisation à but non lucratif, puis l'organisation à but non lucratif vous donne l'argent en tant que contractant et s'occupe des aspects juridiques et comptables.

Nous avons créé [Code for Science and Society](https://codeforscience.org/) pour héberger le Dat Project et également pour héberger un projet appelé [Stenci.la](https://stenci.la/), et nous cherchons également d'autres projets à héberger. Essentiellement, nous aidons les gens à obtenir un financement et à gérer tout le processus, afin qu'ils puissent se concentrer sur le projet et être payés en tant que contractants par l'organisation à but non lucratif. Nous cherchons activement des personnes intéressées à essayer d'obtenir une subvention. Si vous avez une grande idée, peut-être même un prototype, nous voulons vous aider à obtenir un financement et être votre parrain fiscal.

Ce qui se passe, c'est que beaucoup d'ingénieurs ont une grande idée, et ils peuvent aussi avoir un contact avec un responsable de subvention, mais ils ne savent pas comment faire de la comptabilité et ils ne savent pas toujours comment embaucher des gens. Il y a beaucoup de petits détails dont les ingénieurs ne devraient pas avoir à se soucier, et nous devrions nous concentrer sur le tableau d'ensemble et la mission que nous essayons d'accomplir. Mais c'est un sujet difficile pour l'open source, car vous voulez simplement créer le produit mais vous n'avez pas une entreprise qui vous aide. Nous essayons d'être cette organisation parapluie.

Idéalement, tous les projets de notre portefeuille seraient des choses qui peuvent travailler ensemble. Cela inclut la programmation pour la science, la société, le journalisme, le gouvernement ouvert, l'activisme, la collaboration et en général à travers ces domaines.

#### **Décrivez-nous une journée dans la vie de la construction de Dat et de Code for Science and Society ?**

Bien que ce soit divertissant et stimulant de construire, de maintenir et d'éteindre les incendies dans un projet open source, c'est aussi difficile car les tâches que vous devez faire changent constamment. Un jour, je suis en train d'écrire une demande de subvention, l'heure suivante, je dois corriger un bug, et puis l'heure d'après, quelqu'un m'appelle au téléphone pour parler de comptabilité. Parce que nous sommes une organisation à but non lucratif, nous sommes toujours un peu sous-financés, ce qui signifie que tout le monde doit jongler avec beaucoup de tâches différentes.

Il y a eu des moments où c'était calme et je codais simplement 40 heures par semaine, mais ensuite je commençais à devenir un peu agité. J'aime être occupé. Je pense que c'est pour cela que j'ai fait un double diplôme en sciences politiques et en informatique, car j'aime changer. J'aime parler et j'aime coder.

#### **Pouvez-vous parler de quelques périodes vraiment difficiles que vous avez dû traverser ou que vous affrontez actuellement dans la construction de Dat et CSS ? Comment surmontez-vous ces difficultés ?**

L'une des périodes les plus difficiles était il y a environ un an et demi. J'étais dans l'équipe depuis un an, mais Max et Mathias travaillaient dessus depuis environ deux ans. J'avais construit toutes ces choses sur Dat, mais la conception interne ne fonctionnait pas pour nos utilisateurs cibles. Nous avons réalisé que nous devions essentiellement repartir de zéro.

Nous savions que ce serait la meilleure décision à long terme, mais c'était un défi à affronter. Nous avons réalisé que nos utilisateurs n'étaient pas satisfaits, et nous n'obtenions pas de nouveaux utilisateurs, alors nous devions réfléchir à ce qu'ils voulaient. Ce qu'ils voulaient nécessitait une refonte complète dès le départ.

Abandonner notre prototype et passer à une nouvelle version a été une transition difficile. Nous avons trouvé des utilisateurs qui nous aideraient à concevoir la prochaine phase et à travailler sur tous les détails. Ce qui est génial avec les organisations à but non lucratif, c'est que vous pouvez faire cela, car vous n'êtes pas sur une piste plus courte. Vous n'avez pas un besoin intense d'obtenir des utilisateurs ou des revenus, ce qui vous donne une marge de manœuvre. Nous savions combien de temps il nous restait, et nous savions que nous pouvions reconstruire le produit dans ce laps de temps. Pouvoir repartir de zéro a offert un changement rafraîchissant, et nous avons pu nous connecter avec nos utilisateurs pour voir ce qui devait être différent.

#### **Qu'est-ce qui attend le projet Dat ?**

Nous sommes vraiment enthousiastes à propos des [efforts de sauvegarde des données](https://www.datarefuge.org/) qui ont été en cours.

Nous avons travaillé avec [Data Refuge](https://www.datarefuge.org/) ainsi qu'avec la [Bibliothèque du Congrès](https://www.loc.gov/), la [Sunlight Foundation](https://sunlightfoundation.com/) et [DATA.GOV](https://www.data.gov/). Nous allons déterminer comment sauvegarder efficacement toutes les données parmi les différentes institutions qui souhaitent héberger les données. Nous essayons également de faciliter la sauvegarde des ensembles de données ouverts de manière distribuée, afin que, à mesure que davantage d'institutions hébergent de grands ensembles de données, elles soient en mesure de prendre une partie de cet ensemble de données. Vous pouvez en lire plus sur cet effort sur [New York Times](https://www.nytimes.com/2017/03/06/science/donald-trump-data-rescue-science.html?mcubz=3).

![Image](https://cdn-media-1.freecodecamp.org/images/iNpFgm-N4lGujTGB4Y8gCapwM1Sv2sjq1Saw)
_Source : [https://www.nytimes.com/2017/03/06/science/donald-trump-data-rescue-science.html?mcubz=3](https://www.nytimes.com/2017/03/06/science/donald-trump-data-rescue-science.html?mcubz=3" rel="noopener" target="_blank" title=")_

Par exemple, DATA.GOV représente 60 téraoctets de données. Aucune institution ne voudra héberger 60 téraoctets elle-même. Ce que nous voulons faire, c'est utiliser Dat pour distribuer les ensembles de données à travers de nombreuses institutions différentes, afin que les institutions n'aient qu'une partie qu'elles sont prêtes à contribuer.

Il est important de sauvegarder ces ensembles de données de manière distribuée afin que, même si l'un d'eux tombe en panne, les données puissent toujours être disponibles dans une autre institution. Ce n'est qu'une des pièces, car ce qui est vraiment important, c'est que les gens puissent réellement utiliser ces données. Les gens du monde entier utilisent des données générées par l'appareil de financement des États-Unis, [scientifiques et gouvernement.](https://www.nytimes.com/2017/03/06/science/donald-trump-data-rescue-science.html?mcubz=3)

Nous parlons d'ensembles de données climatiques, d'ensembles de données astronomiques, de tout. La polyvalence de la plateforme permet une manière efficace de diffuser l'information, c'est pourquoi les bibliothèques se mettent à bord. Nous voulons rendre cela vraiment facile pour les gens de décrire leurs ensembles de données, et nous voulons que Dat soit un outil vraiment bon pour cela. C'est l'objectif pour les prochains mois.

Ce que nous essayons de faire, c'est collecter des ensembles de données du monde entier pour faciliter leur publication par quiconque. Nous avons mis en place un nouveau système avec l' infection ou l' injection de Dats dans des dépôts existants. Vous devez simplement avoir une série de fichiers de métadonnées. Ce que nous voulons faire, c'est prendre des ensembles de données qui existent déjà sur beaucoup de ces dépôts de données internationaux et les transformer en Dats.

Les gens peuvent télécharger les données et accéder à Dat depuis le site web pour obtenir des mises à jour, accéder à l'historique des données, et plus encore — même si c'est dans l'ancien dépôt HTTP. Nous avons quelques choses assez excitantes à venir, et nous voulons faire cela pour les dépôts du monde entier.

#### **Quels autres passe-temps ou intérêts avez-vous en dehors de la programmation ?**

Je joue de la trompette. C'est un instrument difficile à jouer, mais je suis contente d'avoir persévéré.

![Image](https://cdn-media-1.freecodecamp.org/images/W6GLFOF8Cea6-QDkuYpO4gE4-mfBfpXrciZV)
_Karissa joue de la trompette_

En dehors de cela, je travaille avec le [Debt Collective](https://debtcollective.org/), un syndicat de débiteurs qui lutte contre le prêt prédateur aux États-Unis. En termes de besoins de base comme l'éducation et les soins de santé, le système de financement de la dette devrait définitivement être changé. Il est gratuitement difficile de vivre dans ce système sans contracter de dettes. J'aime leur mission. Ils aident les gens du pays entier qui sont dans des situations désespérées à contester leur dette. Je les ai aidés à construire un peu leur site web et j'ai fait un peu de conseil technologique pour eux.

J'ai [initialement](https://betweenthewires.org/2017/08/25/karissa-mckelvey/) publié cette interview sur [Between the Wires](http://betweenthewires.org), une série d'interviews mettant en vedette ceux qui construisent des produits pour développeurs et designers.

Ce projet est rendu possible grâce aux parrainages de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/) et [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge).

![Image](https://cdn-media-1.freecodecamp.org/images/K5MhnKe438HIh3VZMagS-4cul4Ouj4skZxIP)
_Nos sponsors._

[Faites un don pour soutenir ce projet](https://opencollective.com/betweenthewires).

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Vous pouvez également envoyer des commentaires à [betweenthewires](https://twitter.com/betweenthewires) sur Twitter.