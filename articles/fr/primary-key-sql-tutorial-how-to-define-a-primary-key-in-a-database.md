---
title: Tutoriel SQL sur les clés primaires – Comment définir une clé primaire dans
  une base de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-10T08:20:23.000Z'
originalURL: https://freecodecamp.org/news/primary-key-sql-tutorial-how-to-define-a-primary-key-in-a-database
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a60740569d1a4ca253e.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: postgres
  slug: postgres
- name: SQL
  slug: sql
- name: Tutorial
  slug: tutorial
seo_title: Tutoriel SQL sur les clés primaires – Comment définir une clé primaire
  dans une base de données
seo_desc: 'By Neil Kakkar

  Every great story starts with an identity crisis. Luke, the great Jedi Master, begins
  unsure - "Who am I?" - and how could I be anyone important? It takes Yoda, the one
  with the Force, to teach him how to harness his powers.

  Today, let...'
---

Par Neil Kakkar

Chaque grande histoire commence par une crise d'identité. Luke, le grand Maître Jedi, commence dans l'incertitude - _"Qui suis-je ?"_ - et comment pourrais-je être quelqu'un d'important ? Il faut Yoda, celui qui possède la Force, pour lui apprendre à maîtriser ses pouvoirs.

Aujourd'hui, laissez-moi être votre Yoda.

Nous commencerons par savoir comment choisir une clé primaire, combattre une crise d'identité, et nous terminerons avec des exemples de code pour créer une clé primaire dans une base de données.

## Comment choisir une clé primaire

Vous pensez peut-être que Luke est le seul à avoir une crise d'identité, mais ce n'est pas vrai. Lorsque vous créez une base de données, tout est en crise d'identité. Et c'est exactement pourquoi nous avons besoin de clés primaires : elles résolvent la crise. Elles nous disent comment trouver tout le monde.

Imaginez que vous êtes le gouvernement et que vous souhaitez identifier chacun de vos citoyens numériquement. Vous créez donc cette base de données avec toutes leurs informations :

```
Prénom
Nom
Numéro de passeport
```

Vous choisissez le numéro de passeport comme clé primaire - l'identité de chacun. Vous pensez que c'est tout ce dont vous avez besoin puisque le passeport contient l'adresse et tout le reste. Vous savez que les numéros de passeport sont uniques, alors vous vous sentez bien et implémentez ce système.

Puis, quelques années plus tard, vous découvrez une vérité laide : tout le pays est confronté à une crise d'identité.

Chaque fois que le passeport de quelqu'un expire, il en reçoit un nouveau. Son identité change. D'autres systèmes continuent d'utiliser les anciens numéros de passeport, qui pointent désormais vers des personnes fantômes.

> L'unicité ne suffit pas. La valeur ne doit pas changer tout au long de la durée de vie de la ligne.

Et puis, vous découvrez qu'il y a des personnes qui n'ont même pas de passeport. Vous ne pouvez pas les entrer dans votre système, puisque les clés primaires ne peuvent pas être `NULL`. Comment pouvez-vous identifier quelqu'un avec une clé `NULL` ?

> Chaque ligne doit avoir un identifiant. Les valeurs NULL ne sont pas autorisées.

La prochaine itération signifie trouver un identifiant qui ne change pas avec le temps, et que tout le monde possède. En Inde, cela s'avère être la carte Adhaar. Aux États-Unis, le numéro de sécurité sociale.

Si vous créez une base de données, faites-en vos clés primaires.

Parfois, vous n'avez aucune clé de ce type. Prenons l'exemple d'un pays qui n'a pas encore de numéro de sécurité sociale et qui souhaite créer un enregistrement numérique de chaque citoyen. Ils pourraient créer un nouveau numéro de sécurité sociale, ou ils pourraient simplement tirer parti de la puissance des bases de données et utiliser une clé de substitution.

Une clé de substitution n'a pas d'équivalent dans le monde réel. Ce n'est qu'un numéro à l'intérieur d'une base de données. Vous avez donc cette table dans le nouveau pays :

```
userID
Prénom
Nom
Numéro de passeport
```

Les numéros de passeport sont uniques. Chaque fois que vous souhaitez obtenir l'identifiant d'un utilisateur, vous pouvez l'obtenir via le numéro de passeport.

Le userID ne change jamais. Le numéro de passeport peut changer - mais il est toujours unique, donc vous obtenez toujours le bon utilisateur. Le userID est un _substitut_ pour un numéro de sécurité sociale inexistant dans ce pays.

> Fait amusant : Le numéro de passeport ici est également une clé candidate. Il aurait pu être la clé primaire, s'il n'avait jamais changé. Il s'agit d'une distinction de logique métier.

Le principal enseignement est le suivant : **Lorsque vous choisissez une clé primaire, pensez à une crise d'identité**. Est-il possible que quelqu'un change son identifiant à l'avenir ? Pouvez-vous vous retrouver dans un état où plusieurs personnes ont le même identifiant ?

J'utilise les personnes comme exemple, car cela rend l'identité plus claire - nous savons que chaque personne est censée avoir une identité. Transférez cette réflexion à vos bases de données. Tout a une identité, ce qui est exactement pourquoi vous avez besoin de clés primaires.

> Note : Parfois, il est possible et souhaitable d'utiliser plusieurs colonnes ensemble comme clé primaire. Il s'agit d'une clé composite.

Maintenant, essayons de définir des clés primaires avec des exemples de code réels. Il y a deux choses à faire ici : d'abord, vous identifierez la clé primaire. Ensuite, vous apprendrez la syntaxe pour la définir dans une base de données.

## Un exemple concret

Supposons que vous dirigez une startup de transport maritime, un peu comme Flexport. Vous avez des colis qui doivent aller d'un endroit à un autre, et des navires qui les transportent. De plus, vous avez des clients qui commandent ces colis.

Vous pensez que vous aurez besoin d'une table pour les clients, une pour les colis et une pour le transport, montrant où se trouve chaque colis en ce moment.

Réfléchissez aux colonnes dont vous aurez besoin et à ce qui devrait être la clé primaire. Si vous étiez ingénieur chez Flexport, c'est une question réelle à laquelle vous devriez répondre. Rien n'est donné, tout est découvert dans le monde réel.

Étant donné ces informations, je concevrais ces tables comme suit :

```
Clients : prénom, nom, email, adresse (pour les livraisons à leur emplacement)
Colis : poids, contenu
Transport : <clé_primaire_colis>, Port, heure
```

Il nous manque les clés primaires. Réfléchissez-y avant de continuer la lecture.

Pour le colis, je choisirai un identifiant de colis _de substitution_. J'aurais pu essayer de lister tous les attributs du colis : poids, volume, densité, âge. Ils identifieraient de manière unique le colis, mais cela est très difficile à faire en pratique. Les gens ne se soucient pas de cela, ils se soucient simplement que le colis aille d'un endroit à un autre.

Il est donc logique de créer un numéro aléatoire et de l'utiliser comme identifiant. C'est exactement pourquoi vous voyez FedEx, UPS et chaque service de livraison utiliser des codes-barres et des identifiants. Ce sont des clés de substitution générées pour suivre les colis.

Pour le client, je choisirai un identifiant client _de substitution_. Ici, encore une fois, j'avais l'option de choisir, par exemple, le numéro de sécurité sociale de mes clients. Mais les clients ne veulent pas partager cela avec moi juste pour que je puisse leur expédier quelque chose. Ainsi, nous générons une clé en interne, nous ne disons pas à nos clients à propos de cette clé, et nous continuons à les appeler ClientNo. 345681.

> Histoire amusante : Je connais quelques entreprises où ils ont exposé ce ClientNo, et les clients ont insisté pour obtenir le No. 1. C'était assez hilarant - les ingénieurs ont dû changer leur code front-end en : `if (cust == 345681) print(1);`

Pour le transport, je choisirai une clé _composite_ PackageID+Port+heure. C'est un peu plus intéressant. J'aurais pu créer une clé _de substitution_ ici aussi, et cela aurait tout aussi bien fonctionné.

Mais voici la magie de l'indexation. Les clés primaires obtiennent un index automatiquement, ce qui signifie que la recherche est beaucoup plus efficace sur les clés primaires.

Lorsque vous recherchez dans cette base de données, la plupart des requêtes seront de la forme "où se trouve ce colis ?". En d'autres termes, étant donné cet identifiant de colis, dites-moi le port et l'heure où il se trouve actuellement. J'aurais besoin d'un index supplémentaire sur l'identifiant de colis si je ne l'ai pas comme partie de ma clé primaire.

Cela semble-t-il bon ? Dernière étape, définissons ces 3 tables en SQL. La syntaxe varie légèrement selon la base de données que vous utilisez.

## Définition des clés primaires dans MySQL

```sql
CREATE TABLE customers
( customerID  INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  last_name   VARCHAR(30) NOT NULL,
  first_name  VARCHAR(25) NOT NULL,
  email		  VARCHAR(50) NOT NULL,
  address     VARCHAR(300)
);
```

```sql
CREATE TABLE packages
( packageID  INT(15) NOT NULL AUTO_INCREMENT,
  weight     DECIMAL (10, 2) NOT NULL,
  content    VARCHAR(50),
  CONSTRAINT packages_pk PRIMARY KEY (packageID) # Une autre façon de faire ci-dessus,
  # lorsque vous souhaitez nommer la contrainte également.
);
```

```sql
CREATE TABLE transportation
( package 	INT(15) NOT NULL,
  port  	INT(15) NOT NULL,
  time	 	DATE NOT NULL,
  
  PRIMARY KEY (package, port, time),
  FOREIGN KEY package
  	REFERENCES packages(packageID)
	ON DELETE RESTRICT    # Il est bon de définir ce qui doit se passer en cas de suppression. Dans ce cas, je ne veux pas que les choses soient supprimées.

);
```

## Définition des clés primaires dans PostgreSQL

```sql
CREATE TABLE customers
( customerID  SERIAL NOT NULL PRIMARY KEY, # Dans PostgreSQL, SERIAL est identique à AUTO_INCREMENT - il ajoute 1 à chaque nouvelle ligne.
  last_name   VARCHAR(30) NOT NULL,
  first_name  VARCHAR(25) NOT NULL,
  address     TEXT,
  email		  VARCHAR(50) NOT NULL
);
```

```sql
CREATE TABLE packages
( packageID  SERIAL NOT NULL,
  weight     NUMERIC NOT NULL,
  content    TEXT,
  CONSTRAINT packages_pk PRIMARY KEY (packageID) # Dans PostgreSQL, cette autre façon fonctionne également.
);
```

```sql
CREATE TABLE transportation
( package 	INTEGER NOT NULL,
  port  	INT(15) NOT NULL,
  time	 	DATE NOT NULL,
  
  PRIMARY KEY (package, port, time),
  
  FOREIGN KEY package
  	REFERENCES packages(packageID)
	ON DELETE RESTRICT    # Il est bon de définir ce qui doit se passer en cas de suppression. Dans ce cas, je ne veux pas que les choses soient supprimées.

);
```

Ce n'est pas très différent, n'est-ce pas ? Une fois que vous avez compris les bases, vous pouvez les appliquer à presque n'importe quelle base de données avec juste un rapide coup d'œil à la documentation. La clé est de savoir ce qu'il faut chercher !

Bonne chance, jeune padawan.

Vous avez aimé cela ? Vous aimerez peut-être aussi [Les choses que j'ai apprises d'un ingénieur logiciel senior](https://neilkakkar.com/things-I-learnt-from-a-senior-dev.html)