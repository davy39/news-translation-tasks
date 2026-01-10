---
title: Comment commencer avec MongoDB en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-27T05:14:21.000Z'
originalURL: https://freecodecamp.org/news/learn-mongodb-a4ce205e7739
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ta4qktHtO--RMUpnR08mBg.jpeg
tags:
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment commencer avec MongoDB en 10 minutes
seo_desc: 'By Navindu Jayatilake

  MongoDB is a rich document-oriented NoSQL database.

  If you are a complete beginner to NoSQL, I recommend you to have a quick look at
  my NoSQL article published previously.

  Today, I wanted to share some of the basic stuff about M...'
---

Par Navindu Jayatilake

MongoDB est une base de données NoSQL riche et orientée documents.

Si vous êtes un débutant complet en NoSQL, je vous recommande de jeter un coup d'œil rapide à mon [article sur NoSQL](https://medium.com/@navindushane/say-no-to-sql-ab1e49aa7299) publié précédemment.

Aujourd'hui, je voulais partager quelques bases sur les commandes MongoDB telles que les requêtes, le filtrage des données, la suppression, la mise à jour, etc.

**D'accord, assez parlé, mettons-nous au travail !**

## Configuration du projet

Pour travailler avec MongoDB, vous devez d'abord installer MongoDB sur votre ordinateur. Pour ce faire, visitez [le centre de téléchargement officiel](https://www.mongodb.com/download-center/community) et téléchargez la version pour votre système d'exploitation spécifique. Ici, j'ai utilisé Windows.

Après avoir téléchargé l'installation du serveur communautaire MongoDB, vous passerez par un processus d'installation "suivant après suivant". Une fois terminé, dirigez-vous vers le lecteur C dans lequel vous avez installé MongoDB. Allez dans les fichiers de programme et sélectionnez le répertoire MongoDB.

```
C: -> Program Files -> MongoDB -> Server -> 4.0(version) -> bin
```

Dans le répertoire bin, vous trouverez un couple intéressant de fichiers exécutables.

* mongod
* mongo

Parlons de ces deux fichiers.

`mongod` signifie "Mongo Daemon". mongod est un processus en arrière-plan utilisé par MongoDB. Le but principal de mongod est de gérer toutes les tâches du serveur MongoDB. Par exemple, accepter les requêtes, répondre au client et gérer la mémoire.

`mongo` est une interface de ligne de commande qui peut interagir avec le client (par exemple, les administrateurs système et les développeurs).

Maintenant, voyons comment nous pouvons démarrer ce serveur et le faire fonctionner. Pour ce faire sur Windows, vous devez d'abord créer quelques répertoires dans votre lecteur C. Ouvrez votre invite de commande à l'intérieur de votre lecteur C et faites ce qui suit :

```
C:\> mkdir data/db
C:\> cd data
C:\> mkdir db
```

Le but de ces répertoires est que MongoDB nécessite un dossier pour stocker toutes les données. Le chemin du répertoire de données par défaut de MongoDB est `/data/db` sur le lecteur. Par conséquent, il est nécessaire que nous fournissions ces répertoires comme suit.

Si vous démarrez le serveur MongoDB sans ces répertoires, vous verrez probablement l'erreur suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/r04FRmRGqKUaclGh4ZDo3YsMwOlXMVm2T3bJ)
_tentative de démarrer le serveur mongodb sans les répertoires \data\db_

Après avoir créé ces deux fichiers, retournez dans le dossier bin que vous avez dans votre répertoire mongodb et ouvrez votre shell à l'intérieur. Exécutez la commande suivante :

```
mongod
```

Voilà ! Maintenant notre serveur MongoDB est opérationnel ! 🎉

Pour travailler avec ce serveur, nous avons besoin d'un médiateur. Ouvrez donc une autre fenêtre de commande à l'intérieur du dossier bin et exécutez la commande suivante :

```
mongo
```

Après avoir exécuté cette commande, naviguez vers le shell dans lequel nous avons exécuté la commande mongod (qui est notre serveur). Vous verrez un message "connexion acceptée" à la fin. Cela signifie que notre installation et configuration est réussie !

Exécutez simplement dans le shell mongo :

```
db
```

![Image](https://cdn-media-1.freecodecamp.org/images/TK2JGg4JXAj0eG9JBzl89ABEF3JuKAwnw2dx)
_initialement vous avez une base de données appelée 'test'_

### Comment configurer les variables d'environnement

Pour gagner du temps, vous pouvez configurer vos variables d'environnement. Sous Windows, cela se fait en suivant les menus ci-dessous :

```
Paramètres système avancés -> Variables d'environnement -> Path (Sous Variables système) -> Modifier
```

Copiez simplement le chemin de notre dossier bin et cliquez sur OK ! Dans mon cas, c'est `C:\Program Files\MongoDB\Server\4.0\bin`

Maintenant, vous êtes prêt !

## Comment travailler avec MongoDB

Il existe plusieurs interfaces graphiques (GUI) pour travailler avec le serveur MongoDB, telles que MongoDB Compass, Studio 3T, etc.

Elles fournissent une interface graphique pour que vous puissiez facilement travailler avec votre base de données et effectuer des requêtes au lieu d'utiliser un shell et de taper des requêtes manuellement.

Mais dans cet article, nous utiliserons l'invite de commande pour faire notre travail.

Maintenant, il est temps pour nous de plonger dans les commandes MongoDB qui vous aideront à utiliser vos futurs projets.

1. Ouvrez votre invite de commande et tapez `mongod` pour démarrer le serveur MongoDB.

2. Ouvrez un autre shell et tapez `mongo` pour vous connecter au serveur de base de données MongoDB.

### 1. Trouver la base de données actuelle dans laquelle vous vous trouvez

```
db
```

![Image](https://cdn-media-1.freecodecamp.org/images/o6puQoPSpGCW8-AgizHzAv3Qpywtzsgwd26N)

Cette commande affichera la base de données actuelle dans laquelle vous vous trouvez. `test` est la base de données initiale qui vient par défaut.

### 2. Lister les bases de données

```
show databases
```

![Image](https://cdn-media-1.freecodecamp.org/images/Q-G8NzP5OAXh0Y3OfdOtqFxlFG-tLErPlPSi)

J'ai actuellement quatre bases de données. Elles sont : `CrudDB`, `admin`, `config` et `local`.

### 3. Aller à une base de données particulière

```
use <votre_nom_de_bdd>
```

![Image](https://cdn-media-1.freecodecamp.org/images/UIRueBuX-r6nRXA-qd6Uv95IBd0UbhVvMZtZ)

Ici, je suis passé à la base de données `local`. Vous pouvez vérifier cela en essayant la commande `db` pour imprimer le nom de la base de données actuelle.

### 4. Créer une base de données

Avec les SGBDR (Systèmes de Gestion de Bases de Données Relationnelles), nous avons des bases de données, des tables, des lignes et des colonnes.

Mais dans les bases de données NoSQL, comme MongoDB, les données sont stockées au format BSON (une version binaire de JSON). Elles sont stockées dans des structures appelées "collections".

Dans les bases de données SQL, celles-ci sont similaires aux tables.

![Image](https://cdn-media-1.freecodecamp.org/images/e7ygVKXaPcqcqCyvurAeUzAbmmREoA6p72V2)

![Image](https://cdn-media-1.freecodecamp.org/images/oxeGaPqbZ2pmmZx3WcDo8CXIL4J09PbecBWW)
_termes SQL et termes NoSQL par [Victoria Malaya](https://www.blogger.com/profile/18437865869379626284" rel="noopener" target="_blank" title="profil de l'auteur)_

D'accord, parlons de la façon dont nous créons une base de données dans le shell Mongo.

```
use <votre_nom_de_bdd>
```

Attendez, nous avons déjà eu cette commande ! Pourquoi je l'utilise à nouveau ?!

Dans le serveur MongoDB, si votre base de données est déjà présente, l'utilisation de cette commande vous permettra de naviguer dans votre base de données.

Mais si la base de données n'est pas déjà présente, alors le serveur MongoDB va créer la base de données pour vous. Ensuite, il naviguera dedans.

Après avoir créé une nouvelle base de données, l'exécution de la commande `show database` ne montrera pas votre nouvelle base de données. Cela est dû au fait que, tant qu'elle ne contient aucune donnée (documents), elle ne s'affichera pas dans votre liste de bases de données.

### 5. Créer une collection

Naviguez dans votre nouvelle base de données créée avec la commande `use`.

En fait, il existe deux façons de créer une collection. Voyons les deux.

Une façon est d'insérer des données dans la collection :

```
db.macolle.insert({"name": "john", "age" : 22, "location": "colombo"})
```

Cela va créer votre collection `macolle` même si la collection n'existe pas. Ensuite, il insérera un document avec `name` et `age`. Ce sont des collections non plafonnées.

La deuxième façon est montrée ci-dessous :

2.1 Créer une collection non plafonnée

```
db.createCollection("macolle")
```

2.2 Créer une collection plafonnée

```
db.createCollection("maDeuxiemeCollection", {capped : true, size : 2, max : 2})
```

De cette façon, vous allez créer une collection sans insérer de données.

Une "collection plafonnée" a un nombre maximum de documents qui empêche le débordement de documents.

Dans cet exemple, j'ai activé le plafonnement en définissant sa valeur à `true`.

Le `size : 2` signifie une limite de deux mégaoctets, et `max: 2` définit le nombre maximum de documents à deux.

Maintenant, si vous essayez d'insérer plus de deux documents dans `maDeuxiemeCollection` et utilisez la commande `find` (dont nous parlerons bientôt), vous ne verrez que les documents insérés le plus récemment. Gardez à l'esprit que cela ne signifie pas que le tout premier document a été supprimé, il n'est simplement pas affiché.

#### **6. Insertion de données**

Nous pouvons insérer des données dans une nouvelle collection ou dans une collection qui a été créée auparavant.

![Image](https://cdn-media-1.freecodecamp.org/images/uO4agHbI85kMJrQmF1L9pMmhn0WcgngmoPsI)
_façons dont les données peuvent être stockées dans un JSON_

Il existe trois méthodes d'insertion de données.

1. `insertOne()` est utilisé pour insérer un seul document.
2. `insertMany()` est utilisé pour insérer plus d'un document.
3. `insert()` est utilisé pour insérer autant de documents que vous le souhaitez.

Voici quelques exemples :

* **insertOne()**

```
db.macolle.insertOne(
  {
    "name": "navindu", 
    "age": 22
  }
)
```

* **insertMany()**

```
db.macolle.insertMany([
  {
    "name": "navindu", 
    "age": 22
  },
  {
    "name": "kavindu", 
    "age": 20
  },

  {
    "name": "john doe", 
    "age": 25,
    "location": "colombo"
  }
])
```

La méthode `insert()` est similaire à la méthode `insertMany()`.

De plus, remarquez que nous avons inséré une nouvelle propriété appelée `location` sur le document pour `John Doe`. Donc, si vous utilisez `find`, alors vous verrez que seule la propriété `location` est attachée pour `john doe`.

Cela peut être un avantage lorsqu'il s'agit de bases de données NoSQL comme MongoDB. Cela permet une évolutivité.

![Image](https://cdn-media-1.freecodecamp.org/images/QyCgwWUHWoporNunUvoRgdVry-x0QyA8qSxd)
_données insérées avec succès_

#### **7. Interrogation des données**

Voici comment vous pouvez interroger toutes les données d'une collection :

```
db.macolle.find()
```

![Image](https://cdn-media-1.freecodecamp.org/images/rzcViLqDrTy5gqSFoY6n3N7dciNxFTY62eRL)
_résultat_

Si vous voulez voir ces données de manière plus propre, ajoutez simplement `.pretty()` à la fin. Cela affichera le document au format JSON bien présenté.

```
db.macolle.find().pretty()
```

![Image](https://cdn-media-1.freecodecamp.org/images/gMIbpNqjr9jmJ3YVDZruX1skX0PCvSruuZWB)
_résultat_

Attendez... Dans ces exemples, avez-vous remarqué quelque chose comme `_id` ? Comment cela est-il arrivé là ?

Eh bien, chaque fois que vous insérez un document, MongoDB ajoute automatiquement un champ `_id` qui identifie de manière unique chaque document. Si vous ne voulez pas qu'il s'affiche, exécutez simplement la commande suivante :

```
db.macolle.find({}, _id: 0).pretty()
```

Ensuite, nous examinerons le filtrage des données.

Si vous voulez afficher un document spécifique, vous pouvez spécifier un seul détail du document que vous voulez afficher.

```
db.macolle.find(
  {
    name: "john"
  }
)
```

![Image](https://cdn-media-1.freecodecamp.org/images/TiBBNNp9gmxtPXaHd5BSZ7MkSrv1JkRzkMI1)
_résultat_

Supposons que vous voulez afficher uniquement les personnes dont l'âge est inférieur à 25 ans. Vous pouvez utiliser `$lt` pour filtrer cela.

```
db.macolle.find(
  {
    age : {$lt : 25}
  }
)
```

De même, `$gt` signifie supérieur à, `$lte` est "inférieur ou égal à", `$gte` est "supérieur ou égal à" et `$ne` est "non égal".

#### **8. Mise à jour des documents**

Supposons que vous voulez mettre à jour l'adresse ou l'âge de quelqu'un, comment pourriez-vous le faire ? Eh bien, voyez l'exemple suivant :

```
db.macolle.update({age : 20}, {$set: {age: 23}})
```

Le premier argument est le champ du document que vous voulez mettre à jour. Ici, je spécifie `age` pour la simplicité. Dans un environnement de production, vous pourriez utiliser quelque chose comme le champ `_id`.

Il est toujours préférable d'utiliser quelque chose comme `_id` pour mettre à jour une ligne unique. Cela est dû au fait que plusieurs champs peuvent avoir le même `age` et `name`. Par conséquent, si vous mettez à jour une seule ligne, cela affectera toutes les lignes qui ont le même nom et âge.

![Image](https://cdn-media-1.freecodecamp.org/images/qQH53vM6-peOzS-z9k5YjMoS9R2z1APJrXvB)
_résultat_

Si vous mettez à jour un document de cette manière avec une nouvelle propriété, disons `location` par exemple, le document sera mis à jour avec le nouvel attribut. Et si vous faites un `find`, alors le résultat sera :

![Image](https://cdn-media-1.freecodecamp.org/images/YqJpPAw7d5NPSTzStCevUmgoDTm6FkgPLZ-7)
_résultat_

Si vous devez supprimer une propriété d'un seul document, vous pourriez faire quelque chose comme ceci (disons que vous voulez que `age` disparaisse) :

```
db.macolle.update({name: "navindu"}, {$unset: age});
```

#### **9. Suppression d'un document**

Comme je l'ai mentionné précédemment, lorsque vous mettez à jour ou supprimez un document, vous devez simplement spécifier l'`_id` et non pas seulement `name`, `age`, `location`.

```
db.macolle.remove({name: "navindu"});
```

#### **10. Suppression d'une collection**

```
db.macolle.remove({});
```

Notez que cela n'est pas équivalent à la méthode `drop()`. La différence est que `drop()` est utilisé pour supprimer tous les documents à l'intérieur d'une collection, mais la méthode `remove()` est utilisée pour supprimer tous les documents ainsi que la collection elle-même.

### Opérateurs logiques

MongoDB fournit des opérateurs logiques. L'image ci-dessous résume les différents types d'opérateurs logiques.

![Image](https://cdn-media-1.freecodecamp.org/images/xO27jGeclafiAUt0a0VYRifhDpISvZcIkhRD)

![Image](https://cdn-media-1.freecodecamp.org/images/VsHbrchxUETWqCFhZc6QvmSPUdrbfOHYEH3L)
_référence : manuel MongoDB_

Supposons que vous voulez afficher les personnes dont l'âge est inférieur à 25 ans et dont le lieu de résidence est Colombo. Que pourrions-nous faire ?

Nous pouvons utiliser l'opérateur `$and` !

```
db.macolle.find({$and:[{age : {$lt : 25}}, {location: "colombo"}]});
```

Dernier point mais non des moindres, parlons de l'agrégation.

### Agrégation

Un rappel rapide sur ce que nous avons appris sur les fonctions d'agrégation dans les bases de données SQL :

![Image](https://cdn-media-1.freecodecamp.org/images/JHcuA7YLBiFiCBn1QiOS8NYCUELbGg-LKDSN)
_fonctions d'agrégation dans les bases de données SQL. ref : Tutorial Gateway_

En termes simples, l'agrégation regroupe les valeurs de plusieurs documents et les résume de quelque manière.

Imaginez si nous avions des étudiants masculins et féminins dans une collection `recordBook` et que nous voulions un compte total pour chacun d'eux. Afin d'obtenir la somme des hommes et des femmes, nous pourrions utiliser la fonction d'agrégation `$group`.

```
db.recordBook.aggregate([
  {
    $group : {_id : "$gender", result: {$sum: 1}}
  }  
]);
```

![Image](https://cdn-media-1.freecodecamp.org/images/NeK7Wx3lQ1AaUhGD1VERqmaluAl9qrsXpDMs)
_résultat_

#### Conclusion

Nous avons donc discuté des bases de MongoDB dont vous pourriez avoir besoin à l'avenir pour construire une application. J'espère que vous avez apprécié cet article, merci de l'avoir lu !

Si vous avez des questions concernant ce tutoriel, n'hésitez pas à commenter dans la section des commentaires ci-dessous ou à me contacter sur [Facebook](https://www.facebook.com/navinduuu), [Twitter](https://twitter.com/NavinduJay) ou [Instagram](https://www.instagram.com/iamnavindu/).

À la prochaine, les amis ! ❤️ ✍️😊

Lien vers mon article précédent : [NoSQL](https://medium.com/@navindushane/say-no-to-sql-ab1e49aa7299)