---
title: Les tables SQL expliquées par le vote lors d'une élection
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-06T19:52:41.000Z'
originalURL: https://freecodecamp.org/news/sql-tables-explained-by-voting-in-the-infamous-2016-election-de638dd9db7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AdkZ13GSILN6wnK1m3_AmQ.jpeg
tags:
- name: database
  slug: database
- name: learn to code
  slug: learn-to-code
- name: politics
  slug: politics
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
seo_title: Les tables SQL expliquées par le vote lors d'une élection
seo_desc: 'By Kevin Kononenko

  If you have voted before, then you can understand SQL tables using this wonderfully
  non-political analogy.

  After this particularly controversial election, you probably know more about the
  U.S. voting system than you would ever want...'
---

Par Kevin Kononenko

#### Si vous avez déjà voté, vous pouvez comprendre les tables SQL en utilisant cette analogie merveilleusement non politique.

Après cette élection particulièrement controversée, vous connaissez probablement mieux le système de vote américain que vous ne l'auriez jamais souhaité.

Mais je parie que vous n'auriez jamais pensé que cela vous aiderait à apprendre comment organiser une base de données relationnelle.

Heureusement, les règles de base des élections présidentielles sont en réalité d'excellentes directives pour organiser des tables SQL et comprendre le concept de [**clés**](https://en.wikipedia.org/wiki/Relational_database). Les clés sont l'outil le plus important pour configurer des bases de données SQL scalables et efficaces. Elles sont également la partie la plus confuse lorsque vous débutez !

Tout ce que vous devez savoir avant de lire cet article, ce sont les bases de SQL, principalement comment les tables sont organisées par lignes et colonnes.

#### Retour au jour de l'élection

Vous venez de quitter votre isolateur avec votre bulletin de vote en papier à la main. Vous vous dirigez vers la machine de traitement et vous le glissez dans la fente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yCFBfSc7i0f6-cxmW7yILw.png)

Mais que se passe-t-il ensuite ? Selon vous, quelle serait la meilleure façon de stocker votre vote pour le président ? N'oubliez pas que environ 136 000 000 autres personnes ont également voté lors de cette élection !

Regardez le bulletin ci-dessus. Vous pouvez voir qu'il y a trois identifiants clés que nous devons suivre sur le bulletin :

1. L'élection à laquelle ce bulletin est associé (2016)
2. Un numéro de bulletin (012)
3. Un identifiant de votant, dans ce cas, le numéro de sécurité sociale (012 34 5678)

Votre première pensée pourrait être de stocker tout cela comme une seule entrée, comme ceci :

Mais réfléchissons bien, en tenant compte du fait qu'il y a plus de 100 millions d'autres votants ! Avons-nous vraiment besoin de stocker chaque morceau d'information sur le bulletin dans chaque entrée de la base de données ? Par exemple, devons-nous vraiment lister « candidateA » et « candidateB » comme les deux choix 100 millions de fois ? Bien sûr que non !

Et cela ne tient même pas compte des élections multiples. Imaginez si nous voulions voir l'activité de vote de Jennifer Hardy lors des 3 dernières élections. Même alors, il n'aurait pas de sens d'avoir 3 entrées dans notre base de données qui incluent son nom complet, son numéro de sécurité sociale, son genre, etc., avec chaque vote. Cela encourage les bugs et les informations incohérentes lorsque vous mettez à jour votre base de données pour changer son affiliation politique, par exemple.

Prenons du recul et considérons quelques principes de base du système de vote.

1. Une **élection** a de nombreux **votes** (100 millions+)
2. Un **votant** a de nombreux **votes** au cours de sa vie
3. Un **votant** peut participer à de nombreuses **élections** (jusqu'à 20)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bPRsm-WW5RAcfub5TPWSBA.png)

Nos trois identifiants uniques - numéro de bulletin, numéro de sécurité sociale, date de l'élection - montrent qu'il y a vraiment trois composants dans ce système. Si nous mettons les trois composants dans une seule entrée, comme nous l'avons fait ci-dessus, nous ne pouvons pas capturer les relations entre eux. Et nous allons répéter beaucoup d'informations.

#### Connexion de plusieurs tables

Avec nos trois identifiants clés, nous avons maintenant défini les trois tables nécessaires pour stocker correctement ces informations.

1. Table **Election**, avec une date, le candidat du Parti A et le candidat du Parti B. La date est l'identifiant unique car certains candidats peuvent se présenter à la présidence deux fois, mais deux élections ne se produisent jamais à la même date.
2. Table **Vote**, qui inclut le numéro de bulletin, le numéro de sécurité sociale du votant auquel il est associé, l'élection à laquelle le bulletin est associé, la question sur laquelle on vote (président), et un 0 ou 1 pour le candidat choisi. 0 représente le Parti A, 1 le Parti B en raison de l'ordre alphabétique.
3. Table **Voter**, qui inclut le prénom du votant, le nom de famille, le numéro de sécurité sociale, l'année de naissance, l'affiliation politique, le genre et l'état où il est inscrit pour voter.

Cela décrit beaucoup mieux les différentes parties du système de vote. Il y a en réalité trois événements distincts.

* Vous avez dû vous inscrire pour voter à un moment donné avant le jour de l'élection ! Vous avez été ajouté à la base de données des votants. Votre numéro de sécurité sociale est la **clé primaire**, dans ce cas. Cela signifie qu'il s'agit de l'identifiant unique pour cette ligne.

* Chaque parti a tenu une Convention Nationale pour finaliser leurs candidats en juillet 2016 pour l'élection du 8 novembre. Cela a créé une nouvelle entrée dans la table des élections. La date est la **clé primaire**.

Nous sommes maintenant de retour au scénario initial. Nous sommes le 8 novembre 2016. Vous venez de mettre votre bulletin dans la machine de traitement. Alors, comment la machine devrait-elle vraiment traiter votre bulletin ? Tout d'abord, votre bulletin devrait avoir la quantité minimale d'informations nécessaire.

La machine doit ensuite répondre à quelques questions pour déterminer si le bulletin est valide.

* Avez-vous déjà voté lors de cette élection ?
* Le bulletin est-il lié à l'élection de 2016, ou en avez-vous gardé un d'une élection précédente ?
* Êtes-vous un votant inscrit ?

Chacune de ces questions est une requête SQL distincte. Je veux me concentrer sur les trois premières informations du bulletin ci-dessus. L'identifiant du bulletin est la **clé primaire** pour la table **votes**. Le numéro de sécurité sociale et la date sont en réalité des **clés étrangères**. Cela signifie qu'elles référencent les clés primaires des deux autres tables.

Si nous voulons vérifier si le bulletin provient d'un votant inscrit, nous allons devoir utiliser une **jointure de tables**. Une jointure référence des informations de plusieurs tables en utilisant le système de clés primaires/étrangères. Cela signifie que notre table de votes doit stocker à la fois un identifiant unique pour le votant et pour l'élection dans son ensemble. Mais cela signifie également que nous n'avons pas besoin de stocker toutes les informations du votant ou les informations de l'élection dans cette ligne ! Nous avons juste besoin d'une référence à la table correspondante.

Le système de **clés primaires/étrangères** forme des connexions entre les tables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IZSx78cNjsvg9NiiVERAnQ.png)

Nous voulons vérifier si Jennifer Hardy est un votant inscrit après qu'un bulletin avec le nom de Hardy a été soumis. Nous devons simplement confirmer qu'elle a une entrée dans la table **voters**. Nous utilisons la **clé étrangère** SSN de la table des votes et la **clé primaire** de la table des votants pour lier les deux enregistrements. Nous devons probablement également vérifier si l'état inscrit sur son enregistrement correspond à l'état où le vote a été traité.

Et c'est tout ! Si vous voulez vous entraîner, essayez de configurer une base de données avec les 4 dernières élections présidentielles américaines. Ajoutez 20 votes d'exemple de 10 votants sur les 4 élections. Et voyez si vous pouvez écrire la requête qui vérifiera si un votant tente de soumettre un 2ème bulletin lors d'une élection !

Si vous avez aimé cet article, vous aimerez peut-être aussi mes [autres explications](https://www.rtfmanual.io/guides/) de sujets CSS et JavaScript difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un « cœur » !