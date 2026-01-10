---
title: Comment utiliser les transactions MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-10T21:35:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-mysql-transactions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/White-Minimalist-Dental-Clinic-Facebook-Cover--1-.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: Comment utiliser les transactions MySQL
seo_desc: "By Aisha Bukar\nWhat is a Database Transaction and Why is it Important?\n\
  A database transaction is a single area of the database where multiple data operations\
  \ are carried out and written as a whole. \nThese operations can be create, read,\
  \ update, or de..."
---

Par Aisha Bukar

## Qu'est-ce qu'une transaction de base de données et pourquoi est-elle importante ?

Une transaction de base de données est une zone unique de la base de données où plusieurs opérations de données sont effectuées et écrites en tant qu'ensemble.

Ces opérations peuvent être des opérations de création, de lecture, de mise à jour ou de suppression.

Pendant le processus d'une transaction, la base de données est dans un état incohérent car il y a des opérations en cours qui apportent des modifications à la base de données. La base de données revient à un état plus cohérent lorsque les opérations ont été validées.

Pour qu'une transaction soit réussie, cela signifie que chaque opération effectuée a été validée.

Les transactions de base de données sont très importantes pour garantir la cohérence de votre base de données lorsque plusieurs opérations sont effectuées simultanément. Elles vous offrent également un moyen de récupérer les modifications qui peuvent avoir eu lieu en raison de l'échec ou de l'utilisation accidentelle d'une opération.

## Aperçu de MySQL et de sa prise en charge des transactions

Les bases de données MySQL offrent une prise en charge des transactions de base de données en fournissant des instructions pour initier ces transactions. Elles nous donnent les requêtes intégrées suivantes :

"**START TRANSACTION / BEGIN**" : cette requête déclenche le début d'une transaction.

"**COMMIT**" : cette requête permet aux modifications apportées à la base de données de devenir permanentes. Vous pouvez configurer votre base de données pour qu'elle valide automatiquement les modifications en utilisant la requête suivante :

```mysql
SET autocommit = 1;
```

"**SET**" : cette requête vous permet de définir votre validation en activant les opérations pour qu'elles se valident automatiquement ou en désactivant la validation automatique. C'est-à-dire que vos opérations ne se valideront pas automatiquement jusqu'à ce que vous appeliez la requête "commit".

```mysql
/* Désactivation de la validation automatique */
SET autocommit = 0;
/* OU */
SET autocommit = OFF;

/* Activation des opérations pour qu'elles se valident automatiquement */
SET autocommit = 1;
/* OU */
SET autocommit = ON
```

"**ROLLBACK**" : cette requête vous permet d'annuler les modifications que vous avez apportées à la base de données, ramenant ainsi la base de données à son état précédent (dernier état validé).

## Propriétés ACID des transactions

ACID est un acronyme qui signifie Atomicité, Cohérence, Isolation et Durabilité. Passons en revue chaque terme pour comprendre comment ils se rapportent aux transactions.

![Propriétés ACID](https://www.freecodecamp.org/news/content/images/2023/02/Colorful-Villager-Bingo-Card-Instagram-Story.png)

### Atomicité

L'atomicité dans une transaction de base de données signifie que toutes les modifications effectuées pendant cette transaction sont traitées comme un seul "ensemble" de modifications. Cela signifie que lorsque vous essayez de modifier votre base de données, soit toutes les modifications se produisent en même temps, soit aucune ne se produit.

C'est comme lorsque vous et vos coéquipiers construisez une application. Si une personne écrit une ligne de code, et qu'une autre personne la supprime, c'est comme si rien ne s'était passé. Mais si tout le monde continue à ajouter différentes lignes de code et que personne n'en supprime, alors la base de code continue de s'agrandir.

### Cohérence

La cohérence dans les bases de données signifie que les données stockées dans la base de données sont toujours dans un état valide et cohérent. Par exemple, si la base de données contient des contraintes telles que des clés primaires, des clés étrangères, etc., elle doit toujours se conformer aux règles entourant la contrainte.

Par exemple, supposons qu'une table ait une règle qui dit qu'une colonne spécifique doit être une valeur entière. La cohérence garantit que cette règle est toujours suivie et que les données insérées dans la colonne ne peuvent être que du type de données entier.

### Isolation

La capacité de plusieurs transactions à s'exécuter sans interférer les unes avec les autres est connue sous le nom d'Isolation. Le niveau d'isolation d'une transaction détermine comment les modifications apportées par cette transaction sont visibles pour les autres transactions.

MYSQL prend en charge les niveaux d'isolation suivants :

**i. READ UNCOMMITTED** : Dans le niveau READ UNCOMMITTED, qui est également le niveau d'isolation le plus bas, une transaction peut lire des données qui ne sont pas encore validées par d'autres transactions. Cela signifie que d'autres transactions peuvent modifier les données qu'une autre transaction est en train de lire, mais ces modifications peuvent ne pas être visibles jusqu'à ce que l'opération soit terminée.

**ii. READ COMMITTED** : Il s'agit du deuxième niveau d'isolation le plus bas. Ici, une transaction ne peut lire que les données qui ont déjà été validées par d'autres transactions. Cela signifie que d'autres transactions peuvent modifier les données qu'une transaction est en train de lire, mais ces modifications ne seront pas visibles jusqu'à ce que l'autre transaction ait été validée.

**iii. REPEATABLE READ** : Il s'agit d'un niveau d'isolation plus élevé. Une transaction à ce niveau ne peut lire que les données qui ont déjà été validées par d'autres transactions, et elle restreint également les autres transactions de modifier les données qui sont actuellement lues. Cela signifie que même si d'autres transactions ont validé des modifications, si une transaction exécute à nouveau une instruction SELECT, elle verra toujours les mêmes données.

**iv. SERIALIZABLE** : Il s'agit du niveau d'isolation le plus élevé. À ce niveau, une transaction ne peut lire que les données qui ont déjà été validées par d'autres transactions. Elle empêche également les autres transactions de modifier les données que la transaction est en train de lire et d'ajouter de nouvelles lignes qui seraient visibles pour la transaction actuelle.

MySQL utilise par défaut le niveau d'isolation READ COMMITTED. Cependant, il est possible de changer le niveau d'isolation en utilisant l'instruction "SET TRANSACTION ISOLATION LEVEL".

### Durabilité

La durabilité garantit que vos données restent en sécurité, même en cas de circonstances imprévues. Lorsqu'une transaction est validée, ses modifications doivent rester dans la base de données, même si elle subit une panne ou une coupure de courant.

Mais comment MySQL garantit-il la durabilité ? Il utilise la journalisation anticipée. Cette technique consiste à écrire un journal de la transaction sur le disque avant d'apporter des modifications à la base de données.

Le journal sert de feuille de route pour la base de données et contient des informations sur les modifications qui seront apportées en cas de panne système inattendue. Dans ce cas, la base de données peut être récupérée à partir du journal, et les modifications apportées dans la transaction seront rejouées pour s'assurer que la base de données est toujours dans un état cohérent.

Il est important de garder à l'esprit que bien que la journalisation anticipée puisse avoir un impact sur les performances, c'est un petit prix à payer pour la tranquillité d'esprit qui vient avec le fait de savoir que vos données sont en sécurité.

## Verrouillage et concurrency dans les transactions MySQL

Le verrouillage est une technique utilisée pour prévenir les conditions de course. Une condition de course est un processus où plusieurs transactions tentent d'accéder aux mêmes données en même temps.

MySQL utilise différents types de verrous pour contrôler l'accès aux données dans une transaction. Ceux-ci incluent :

1. **Verrous partagés** : Cela permet à plusieurs transactions de lire les mêmes données en même temps, mais restreint l'une d'elles d'écrire ou de faire des modifications.
2. **Verrous exclusifs** : Cela empêche différentes transactions de lire ou d'écrire les mêmes données en même temps.
3. **Verrous d'intention** : Cela est utilisé pour spécifier qu'une transaction prévoit de lire ou d'écrire une certaine section de données.
4. **Verrous au niveau des lignes** : Cela permet aux transactions de verrouiller uniquement les lignes spécifiques dont elles ont besoin pour accéder, plutôt que la table entière.

La concurrency est une méthode où plusieurs transactions peuvent s'exécuter simultanément sans interférer avec les données des autres.

MySQL utilise un mécanisme de contrôle de concurrency multiversion (MVCC). Cela permet à plusieurs transactions de lire et d'écrire les mêmes données en même temps sans conflit.

Je suis sûr que vous vous demandez comment cela peut être réalisé. Eh bien, chaque transaction capture en quelque sorte les données qu'elle est sur le point de modifier au début de la transaction et écrit ses modifications dans une version entièrement différente des données. Cela permet aux autres transactions de continuer à travailler avec la version originale des données sans conflit d'intérêts.

Pour atteindre une haute concurrency, il est important de garder les transactions aussi courtes que possible et d'éviter les transactions longues qui maintiennent les verrous pendant des périodes prolongées.

## Comment créer et utiliser des transactions dans MySQL

La première chose requise est de démarrer la transaction en utilisant l'instruction "START TRANSACTION". Voici un exemple :

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE name = 'John Doe';
```

Dans cet exemple, une nouvelle transaction est démarrée avec l'instruction START TRANSACTION. Les deux instructions suivantes, une insertion et une mise à jour, sont exécutées dans la transaction.

L'étape suivante consiste à valider les modifications pour s'assurer qu'elles sont permanentes. Nous faisons cela en incluant l'instruction COMMIT dans la requête.

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE name = 'John Doe';
COMMIT;
```

Si par hasard il y avait une erreur pendant la transaction et que vous souhaitez annuler les modifications, vous pouvez utiliser l'instruction ROLLBACK. Ensuite, la transaction sera annulée et les instructions d'insertion et de mise à jour ne seront pas exécutées. Cela signifie qu'aucun changement n'aura lieu dans la base de données.

```mysql
START TRANSACTION;
    INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
    UPDATE accounts SET balance = SUM(balance) WHERE user_id=15;
ROLLBACK;
```

## Comment utiliser le moteur de stockage InnoDB pour les transactions

InnoDB est un moteur de stockage pour MySQL qui possède de nombreuses fonctions pouvant améliorer les performances de votre base de données. Certaines de ces fonctionnalités incluent la capacité de regrouper et d'exécuter plusieurs instructions SQL ensemble, de chiffrer nos données, de créer et de supprimer des index sans affecter les performances de la base de données, de gérer le CPU ainsi que les grandes données, et bien plus encore.

Pour utiliser InnoDB pour les transactions dans MySQL, vous devrez vous assurer que vos tables utilisent le moteur de stockage InnoDB. Vous pouvez vérifier cela en exécutant la requête suivante :

```mysql
SHOW TABLE STATUS FROM your_database_name;
```

Cela vous montrera le moteur de stockage utilisé par chaque table dans votre base de données. Il est également possible de définir le moteur de stockage par défaut sur InnoDB en modifiant le fichier de configuration `my.cnf`, ou en exécutant la commande suivante :

```mysql
SET storage_engine=InnoDB;
```

Après avoir exécuté cette requête, vos tables de base de données devraient utiliser le moteur de stockage InnoDB. Nous pouvons ensuite commencer à effectuer les fonctions que nous avons listées ci-dessus.

```mysql
START TRANSACTION;
    UPDATE accounts SET balance = 50 WHERE user_id = 1;
    UPDATE accounts SET balance = 2000 WHERE user_id = 2;
COMMIT;
```

Il s'agit d'un exemple simple de transaction qui met à jour deux lignes dans la table "accounts". Si l'une des instructions échoue, l'ensemble de la transaction sera annulé, et aucun changement ne sera apporté à la base de données.

De plus, InnoDB offre également des fonctionnalités supplémentaires telles que le verrouillage au niveau des lignes, les contraintes de clé étrangère et la récupération après crash, ce qui le rend plus robuste et fiable que les autres moteurs de stockage, en particulier pour les charges de travail transactionnelles.

## Comment gérer les erreurs et les exceptions dans les transactions

La gestion des erreurs et des exceptions est importante, surtout lorsque vous travaillez avec des transactions.

Une méthode de gestion des erreurs et des exceptions dans les transactions consiste à utiliser un bloc try-catch. Dans MySQL, vous pouvez utiliser les instructions SIGNAL et RESIGNAL pour lever et gérer des exceptions dans une transaction.

Voici un exemple de la façon dont vous pourriez utiliser un bloc try-catch pour gérer une exception dans une transaction :

```mysql
START TRANSACTION;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        START TRANSACTION
            ROLLBACK;
            RESIGNAL;
        END;
    UPDATE accounts SET balance = 5000 WHERE user_id = 1;
    UPDATE accounts SET balance = 1000 WHERE user_id = 2;
    IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Solde insuffisant';
    END IF;
COMMIT;
```

Le bloc DECLARE EXIT HANDLER FOR SQLEXCEPTION est utilisé pour capturer toute exception SQL qui se produit dans la transaction.

Si une exception est capturée, la transaction est annulée à l'aide de l'instruction ROLLBACK. Ensuite, l'instruction RESIGNAL lève à nouveau l'exception afin qu'elle puisse être gérée par un bloc try-catch externe, le cas échéant.

L'instruction IF vérifie si le solde de user_id =1 est inférieur à zéro. Si c'est vrai, l'instruction SIGNAL lève une exception avec un SQLSTATE spécifique '45000' et un message "Solde insuffisant".

Il est bon de savoir que si une exception se produit dans une transaction, toutes les modifications qui peuvent avoir eu lieu pendant la transaction seront annulées, indépendamment du fait que l'exception soit gérée ou non.

## Comment utiliser les points de sauvegarde dans les transactions MySQL

Il est bon de pratique d'utiliser l'instruction SAVEPOINT dans une transaction pour définir des points de sauvegarde. Cela permet de revenir à un point spécifique dans la transaction, plutôt que d'annuler toute la transaction.

Voici un exemple de la façon dont vous pourriez utiliser l'instruction SAVEPOINT dans l'exemple précédent :

```mysql
START TRANSACTION;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        START TRANSACTION
            ROLLBACK TO SAVEPOINT my_savepoint;
            RESIGNAL;
        END;
    UPDATE accounts SET balance = 5000 WHERE user_id = 1;
    UPDATE accounts SET balance = 1000 WHERE user_id = 2;
    IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Solde insuffisant';
    END IF;
COMMIT;
```

Vous utilisez l'instruction SAVEPOINT pour définir un point de sauvegarde nommé "my_savepoint" avant les deux mises à jour. Si une exception est capturée, l'instruction ROLLBACK annule la transaction jusqu'au point de sauvegarde, en utilisant la clause "TO SAVEPOINT my_savepoint", plutôt que d'annuler toute la transaction.

Cela annulera uniquement les modifications apportées après le point de sauvegarde et laissera intactes les modifications apportées avant le point de sauvegarde.

## Conclusion

Les opérations de transaction sont assez importantes. Elles aident les développeurs à s'assurer que leur base de données reste dans un état cohérent et facilitent l'inversion des modifications si nécessaire.

MySQL fournit des fonctionnalités telles que commit, rollback et savepoint pour rendre le processus beaucoup plus facile. Il fournit également des moteurs robustes comme InnoDB qui supportent ces fonctionnalités.

Pour plus d'informations sur les transactions MySQL, vous pouvez consulter la [documentation officielle](https://dev.mysql.com/doc/refman/8.0/en/sql-transactional-statements.html).