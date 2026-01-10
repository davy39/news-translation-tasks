---
title: Comment utiliser les déclencheurs SQL
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-02-21T20:13:01.000Z'
originalURL: https://freecodecamp.org/news/sql-triggers
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-tima-miroshnichenko-5640619.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: SQL
  slug: sql
seo_title: Comment utiliser les déclencheurs SQL
seo_desc: "MySQL Triggers are like JavaScript event listeners. They are not executed\
  \ until an action that they have been told to listen for happens. \nHere's a helpful\
  \ description of them from the MySQL docs:\n\nA trigger is a named database object\
  \ that is associa..."
---

Les déclencheurs MySQL sont comme les écouteurs d'événements en JavaScript. Ils ne sont pas exécutés tant qu'une action qu'ils ont été configurés pour écouter ne se produit pas. 

Voici une description utile des déclencheurs tirée de la documentation MySQL :

> Un déclencheur est un objet de base de données nommé qui est associé à une table et qui s'active lorsqu'un événement particulier se produit pour cette table.   
>   
> Certaines utilisations des déclencheurs consistent à effectuer des vérifications des valeurs à insérer dans une table ou à effectuer des calculs sur les valeurs impliquées dans une mise à jour. - [MySQL.com](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)

Les déclencheurs sont utiles pour automatiser des tâches répétitives. Vous pouvez simplement configurer un déclencheur pour effectuer un calcul après chaque action spécifique sur la base de données. Vous pouvez également configurer un déclencheur pour effectuer des tâches de validation des données sur une table.

Un déclencheur est activé lorsqu'une opération `INSERT`, `UPDATE` ou `DELETE` se produit sur une table de base de données. Un déclencheur est activé par ligne, donc si plusieurs lignes de données sont insérées ou supprimées, chacune active toujours l'action configurée par le déclencheur. Un déclencheur peut être configuré pour se déclencher avant ou après une action.

Dans ce tutoriel, vous apprendrez à créer des déclencheurs, à les supprimer et à savoir quand ils sont utiles.

## Comment créer un déclencheur

Pour créer un nouveau déclencheur, utilisez la commande `CREATE TRIGGER`. Cette commande a la structure suivante :

```sql
CREATE TRIGGER nom_du_declencheur
moment_du_declencheur 
evenement_du_declencheur
ON nom_de_la_table 
FOR EACH ROW
corps_du_declencheur
```

Voici une explication de chaque ligne :

* Le mot-clé `CREATE TRIGGER` est obligatoire et est suivi du nom du déclencheur. Vous utiliserez ce nom pour faire référence au déclencheur à l'avenir et pour le supprimer si nécessaire. Ce nom doit être unique par base de données.
* Le `moment_du_declencheur` est une valeur variable qui ne peut être que `BEFORE` ou `AFTER`. Cela détermine si le déclencheur sera activé avant ou après que l'événement se soit produit.
* L'`evenement_du_declencheur` est une autre variable qui a un nombre limité d'options possibles. Cette variable ne peut prendre aucune autre valeur que `INSERT`, `UPDATE` ou `DELETE`. Elle spécifie quel événement écouter.
* `nom_de_la_table` est le nom de la table que le déclencheur doit surveiller. Cela doit être le nom d'une table existante dans votre base de données, mais cela peut être une table vide.
* Le `FOR EACH ROW` est l'autre partie obligatoire de la définition du déclencheur.
* `corps_du_declencheur` est la requête SQL que vous souhaitez exécuter lorsque ce déclencheur est activé.

Pour créer un exemple de déclencheur, je vais créer une simple table `users` pour la pratique.

```sql
CREATE TABLE
    users (
        fullname VARCHAR(120),
        email VARCHAR(120),
        username VARCHAR(30),
        password VARCHAR(60)
    );
```

Maintenant, nous pouvons créer un simple déclencheur et l'attacher à cette table vide. Un déclencheur qui chiffrerait les mots de passe en chaîne de caractères avant leur insertion en utilisant la fonction `MD5` serait judicieux.

```sql
CREATE TRIGGER password_hasher BEFORE INSERT ON users FOR EACH ROW
SET
    NEW.password = MD5 (NEW.password);
```

Cet exemple est assez simple et explicite. Mais il y a un mot-clé `NEW`. Ce mot-clé vous donne accès aux nouvelles données en cours de création et vous permet d'utiliser ou de modifier les valeurs comme vous le souhaitez. 

Vous ne pouvez modifier ces valeurs que si votre `event_time` est défini sur `BEFORE`. Si l'`event_time` est défini sur `AFTER`, les données ont déjà été stockées avant d'atteindre le déclencheur, donc elles ne peuvent plus être modifiées.  

Vous pouvez utiliser le mot-clé `NEW` dans les événements `INSERT` et `UPDATE`, mais pas dans l'événement `DELETE`.

Il existe également le mot-clé `OLD` que vous pouvez utiliser dans les déclencheurs d'événements `DELETE` et `UPDATE`, qui vous donne accès aux anciennes valeurs de l'enregistrement affecté. Vous ne pouvez pas utiliser ce mot-clé sur un événement `INSERT` car il n'y a pas d'enregistrement précédent avant la création de nouvelles données.

Pour tester ce déclencheur, insérez une ligne dans la table `users` :

```sql
INSERT INTO
    users
VALUES
    (
        'idris babu',
        'zubs@test.com',
        'zubby1',
        'password'
    );
```

Vérifiez votre table pour les valeurs. Vous devriez avoir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-18-at-02.14.44.png)

La valeur du mot de passe a été correctement chiffrée. 
ud83e
udd73

## Comment supprimer un déclencheur

Après avoir créé un déclencheur, vous pourriez vouloir arrêter son exécution pour une raison quelconque. Dans ce cas, vous pouvez supprimer le déclencheur. 

Pour supprimer le déclencheur, utilisez la commande `DROP TRIGGER`. La commande ne nécessite que le nom du déclencheur. Vous pouvez utiliser la commande comme ceci :

```sql
DROP TRIGGER password_hasher;
```

L'exécution de cette requête supprimera le déclencheur que nous avons créé ci-dessus et chaque enregistrement inséré à partir de maintenant n'aura pas le mot de passe chiffré. 

Pour tester cela, insérez le même enregistrement qu'auparavant et vérifiez le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-18-at-02.24.21.png)

Le nouvel enregistrement créé n'a pas de mot de passe chiffré.

Une chose à garder à l'esprit : si vous supprimez complètement la table, tous les déclencheurs associés sont également supprimés automatiquement.

## Quand utiliser les déclencheurs

1. Journalisation : Vous pouvez avoir un déclencheur pour écrire automatiquement dans une autre table lors de l'insertion, de la mise à jour ou de la suppression d'un enregistrement d'une table.
2. Validation des données : Vous pouvez écrire un déclencheur pour vous assurer que les données sont d'un certain type et que des valeurs correctes peuvent être définies lorsque nécessaire.
3. Synchronisation des données : Vous pouvez utiliser un déclencheur pour maintenir à jour les tables liées. Par exemple, dans une table de commerce électronique, chaque fois qu'un enregistrement de vente est créé, un déclencheur peut mettre à jour le solde du vendeur. Ou si l'enregistrement du vendeur est supprimé, un déclencheur peut supprimer tous ses produits.

## **Résumé**

J'espère que vous comprenez maintenant les déclencheurs SQL et quand les utiliser afin de pouvoir écrire de meilleures requêtes.

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, c'est facile et c'est gratuit !