---
title: 'Pour l''amour de SQL : pourquoi vous devriez l''apprendre et comment cela
  vous aidera'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-03T21:22:53.000Z'
originalURL: https://freecodecamp.org/news/for-the-love-of-sql-why-you-should-learn-it-and-how-itll-help-you-out-22fe307a253
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wdnZPs8tLOGbEfECpoh5Kg.png
tags:
- name: big data
  slug: big-data
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Pour l''amour de SQL : pourquoi vous devriez l''apprendre et comment cela
  vous aidera'
seo_desc: 'By Matthew Oldham

  I recently read a great article by the esteemed @craigkerstiens describing why he
  feels SQL is such a valuable skill for developers. This topic really resonated with
  me. It lined up well with notes I’d already started sketching out ...'
---

Par Matthew Oldham

J'ai récemment lu [un excellent article](http://www.craigkerstiens.com/2019/02/12/sql-most-valuable-skill/) de l'estimé [@craigkerstiens](http://twitter.com/craigkerstiens) décrivant pourquoi il pense que SQL est une compétence si précieuse pour les développeurs. Ce sujet a vraiment résonné en moi. Il s'alignait bien avec les notes que j'avais déjà commencées à esquisser pour un article similaire sur le développement d'un amour pour les données.

Plus je développis mon sujet, cependant, plus je réalisais que beaucoup de mes points et exemples semblaient se concentrer autour de SQL. La lecture de l'article de Craig m'a convaincu de rediriger mon attention et de parler davantage de pourquoi j'ai personnellement une telle affinité pour SQL.

En bref, Craig fait les assertions suivantes sur SQL (et je cite) :

> 1. Il est précieux dans différents rôles et disciplines

> 2. L'apprendre une fois ne nécessite pas vraiment de le réapprendre

> 3. Vous semblez être un super-héros. Vous semblez extra puissant lorsque vous le connaissez en raison du nombre de personnes qui ne le maîtrisent pas

J'ai trouvé tous ces points vrais dans ma propre expérience, et j'aimerais reformuler et développer chacun d'eux.

#### L'Effet de Polyvalence

La compétence SQL s'est avérée être un atout extrêmement précieux dans ma carrière. En fait, je crois que SQL est le langage de "programmation" le plus puissant et polyvalent que je connaisse.

J'ai pu utiliser SQL pour résoudre de nombreux problèmes, et c'est mon outil de prédilection chaque fois que je suis confronté à un nouveau défi. En fait, je garde une instance de [PostgreSQL](https://www.postgresql.org/) en cours d'exécution sur mon ordinateur portable afin de pouvoir rapidement accéder à mon [GUI SQL préféré](https://www.dbvis.com/) chaque fois que j'ai besoin de tester quelque chose.

Voici quelques-unes des choses cool que j'ai pu faire avec SQL :

![Image](https://cdn-media-1.freecodecamp.org/images/C8Q-vL5taSoDEP9SRX2Y02hLc1oA5EHLso5h)
_SQL FTW !_

Avez-vous du mal à croire la liste ci-dessus ? Je vous promets qu'il n'y a pas une once d'exagération. Maintenant, y a-t-il des éléments qui dépendaient d'autres capacités du SGBD que j'utilisais à l'époque ? Bien sûr. Quoi qu'il en soit, chacune de ces solutions a été implémentée en SQL.

#### L'Effet Bicyclette

Bien que le langage Structured Query Language ait certainement subi des changements et ait été étendu au fil des ans, je suis d'accord avec Craig pour dire que les fondamentaux n'ont pas changé. Le niveau global de volatilité par rapport à d'autres langages a été relativement faible.

Je soutiendrais que ce fait ne fait que renforcer l'argument selon lequel on devrait investir du temps pour apprendre SQL. Vous pouvez être confiant que vous obtiendrez beaucoup de mileage d'un tel investissement sans avoir à chercher les dernières conventions la prochaine fois que vous en aurez besoin.

Alors, apprenez SQL ! Voici quelques excellents endroits pour commencer :

[**Tutoriel SQL — SQL Essentiel Pour Les Débutants**](http://www.sqltutorial.org/)  
[_Ce tutoriel SQL vous aide à commencer avec SQL rapidement et efficacement à travers de nombreux exemples pratiques. Après le...www.sqltutorial.org_](http://www.sqltutorial.org/)

Il existe même des tutoriels interactifs :

[**SQLBolt — Apprendre SQL — Introduction à SQL**](https://sqlbolt.com/)  
[_SQLBolt fournit un ensemble de leçons et d'exercices interactifs pour vous aider à apprendre SQL_sqlbolt.com_](https://sqlbolt.com/)

Il existe également des sandboxes polyvalents qui vous permettent d'exécuter SQL dans divers dialectes sans avoir à installer quoi que ce soit. Par exemple, [SQL Fiddle](http://sqlfiddle.com/) :

![Image](https://cdn-media-1.freecodecamp.org/images/-Yav499rZkhE8ee4JtdnkvLE4pgFfRcUUc76)
_SQL Fiddle_

Ou, [DB Fiddle](https://www.db-fiddle.com/) :

![Image](https://cdn-media-1.freecodecamp.org/images/yvN5Y8Qk9QgHq1V1A1MorV5GjCbi2Vh3Yxw-)
_DB Fiddle_

#### L'Effet Super-héros

Je me souviens qu'un collègue disait un jour qu'il transpirait à froid chaque fois qu'il devait écrire du SQL. 😅

Cela semble exagéré, mais SQL peut être intimidant pour quiconque considère correctement la base de données comme l'actif sensible qu'elle est et ne sait pas comment interagir avec elle en toute sécurité. SQL, étant l'un des adultes dans la pièce, n'attire pas autant l'attention que d'autres nouveaux langages de programmation brillants. Cela signifie qu'il reste une compétence moins courante parmi les développeurs contemporains et émergents.

Ainsi, avoir une solide compréhension de SQL et l'intuition de voir les facettes basées sur les ensembles d'un problème ou d'un défi donné offre l'opportunité d'être un héros.

L'une de mes expériences personnelles préférées a été d'aider un client à déboguer un programme [SAS](https://en.wikipedia.org/wiki/SAS_(software)) lent et complexe. Le but de ce programme était d'extraire une liste de transitions d'état à partir d'une table d'audit afin de mesurer la durée moyenne qu'un widget passait dans chaque phase d'un flux de travail commercial donné. La mise en œuvre de ces calculs était complexe et nécessitait la construction de plusieurs ensembles de données locaux.

Je me souviens avoir inversé ce programme et réalisé que je pouvais résoudre le problème beaucoup plus facilement en utilisant une seule requête SQL et la fonction de fenêtre magique [LAG](http://www.sqltutorial.org/sql-window-functions/sql-lag/).

Le client a simplement été soufflé.

Non seulement parce qu'il a appris la fonction LAG, mais parce qu'il a vu à quel point SQL peut être puissant.

Un exemple encore plus dramatique a été lors d'une grande migration d'entrepôt de données où j'ai remplacé un programme Java entier (qui prenait plus de 20 minutes à s'exécuter !) par une seule requête SQL qui s'exécutait en quelques secondes. L'auteur original du programme était choqué ! Ce fut une très bonne journée. 😊

Alors, je vous encourage à plonger dans SQL aujourd'hui et à élargir votre ensemble de compétences avec l'un des outils les plus polyvalents que j'ai eu le plaisir d'utiliser. Si vous connaissez déjà SQL et êtes d'accord, ou si je vous ai convaincu de l'essayer, veuillez envisager de me laisser un commentaire.