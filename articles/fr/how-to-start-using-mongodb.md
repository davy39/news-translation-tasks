---
title: Comment commencer à utiliser MongoDB – Installation de la base de données pour
  débutants
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-07-25T21:42:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-using-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-tom-fisk-3285715.jpg
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
seo_title: Comment commencer à utiliser MongoDB – Installation de la base de données
  pour débutants
seo_desc: "MongoDB is an increasingly popular open source NoSQL database. And it has\
  \ many advantages over traditional SQL databases. \nIt offers high scalability,\
  \ reliability, and performance even with a huge amount of data. \nThis article covers\
  \ the basics that ..."
---

MongoDB est une base de données NoSQL open source de plus en plus populaire. Et elle présente de nombreux avantages par rapport aux bases de données SQL traditionnelles. 

Elle offre une haute scalabilité, une grande fiabilité et des performances élevées même avec une énorme quantité de données. 

Cet article couvre les bases que vous devez connaître pour commencer avec MongoDB et comment l'utiliser correctement.

### Prérequis

* Un IDE adapté tel que VS Code
* Un terminal

### Ce que vous allez apprendre

* Qu'est-ce que MongoDB ?
* Qu'est-ce que NoSQL ?
* Comment installer MongoDB
* Comment configurer MongoDB
* Comment exécuter MongoDB

## Qu'est-ce qu'une base de données NoSQL ?

Une base de données NoSQL est une base de données non relationnelle qui n'utilise pas le schéma basé sur les tables traditionnel d'une base de données relationnelle. 

Les bases de données NoSQL sont souvent utilisées pour le big data et les applications web en temps réel. MongoDB est l'une des bases de données NoSQL les plus populaires. Elle est rapide, scalable et utilise des documents JSON pour stocker les données. 

## Pourquoi devrais-je utiliser No-SQL ?

Les bases de données No-SQL sont des outils puissants qui peuvent vous aider à travailler avec de grandes quantités de données. Elles sont particulièrement bonnes pour gérer des données non structurées, ce qui peut en faire un bon choix si vous traitez avec beaucoup de données qui ne s'intègrent pas dans une base de données relationnelle traditionnelle. 

Les bases de données No-SQL peuvent également être plus scalables que les bases de données relationnelles, ce qui est important si vous prévoyez que vos données vont croître avec le temps.

## Comment commencer avec MongoDB – Guide d'installation

Installez MongoDB en utilisant [ce lien](https://www.mongodb.com/docs/manual/administration/install-community/) ou suivez les instructions ci-dessous si vous utilisez Ubuntu : 

* Importez la clé publique

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

```

* Créez un fichier de liste pour Ubuntu 

```bash
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

```

* Exécutez la commande suivante pour mettre à jour :

```bash
sudo apt-get update

```

* Installez le dernier paquet

```bash
sudo apt-get install -y mongodb-org

```

* Puis exécutez :

```bash
sudo service mongod start

```

## Comment créer et peupler la base de données MongoDB

Une fois MongoDB installé, créez un répertoire de données où MongoDB stockera ses fichiers de données. Par défaut, il s'agit de `/data/db`, mais vous pouvez spécifier un autre emplacement si vous préférez. Enfin, démarrez le serveur MongoDB en exécutant `mongod` depuis la ligne de commande.

Créez un répertoire pour `dbPath` avec la commande suivante : 

```bash
sudo mkdir -p /data/db 
sudo chown -R `id -un` /data/db
```

Puis exécutez `sudo mongod --port 27017` ou `mongod` dans un autre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-214.png)

Votre format de sortie (également connu sous le nom de `structured logging`) pour les journaux du serveur dans MongoDB 4.4+ devrait ressembler à ce qui précède. Bien que le format JSON puisse sembler intimidant au premier abord, il est conçu pour être utilisé avec des outils et des frameworks JSON courants.

Entrez dans le shell MongoDB en utilisant cette commande : 

```bash
mongo

```

Vous obtiendrez la sortie montrée ci-dessous après avoir exécuté la commande suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-from-2022-07-24-18-37-20.png)

## Comment créer une nouvelle base de données MongoDB

La première étape pour utiliser MongoDB est de créer une nouvelle base de données avec la commande `use mydatabase`. Vous pouvez ensuite créer des collections à l'intérieur de cette base de données. Enfin, vous pouvez peupler votre nouvelle collection.

```
 use record
 db.users.insert({username: "myname", password: "mypassword"})

```

La commande `use record` bascule vers la base de données `record database`. La commande `db.users.insert(...)` ajoute une entrée à la table `users` dans la base de données `record`.

Voici la sortie des commandes ci-dessus :

```
WriteResult({ "nInserted" : 1 })
```

Exécutez la commande suivante pour voir l'enregistrement que vous avez créé dans l'étape précédente :

```
 db.users.find()

```

La commande `db.users.find()` recherche dans la table `users` toutes les entrées.  
Votre sortie produit le résultat suivant :

```
{ "_id" : ObjectId("62dd6ab4a7d1ab0948574778"), "username" : "myname", "password" : "mypassword" }
```

## Comment ajouter de nouveaux enregistrements à votre base de données

Pour ajouter de nouveaux enregistrements, procédez comme suit :

```
 use record
 db.commerce.save({scriptname: "dygraph.min.js", version: "2.1.0"})
 db.commerce.save({scriptname: "sortable.min.js", version: "0.8.0"})
```

Nous avons ajouté deux enregistrements à la table `commerce`, chacun avec des données spécifiées par les attributs `scriptname` et `version`.

Vous devriez obtenir quelque chose comme ceci :

```
WriteResult({ "nInserted" : 1 })
```

Pour voir toutes les tables stockées dans votre base de données MongoDB, exécutez les commandes suivantes :

```
 use record
 show collections

```

Vous devriez voir une sortie similaire à celle ci-dessous :

```
commerce
users
```

## Conclusion

MongoDB est un système de base de données puissant que vous pouvez utiliser pour une variété d'applications. Il est facile à installer et à utiliser, et sa scalabilité en fait un bon choix pour les projets à grande échelle. 

Si vous êtes nouveau dans les systèmes de bases de données, MongoDB est un bon point de départ.