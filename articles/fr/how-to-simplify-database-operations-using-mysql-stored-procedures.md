---
title: Comment utiliser les procédures stockées MySQL pour simplifier les opérations
  de base de données
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-12T22:05:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-database-operations-using-mysql-stored-procedures
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/How-to-use-Mysql-procedure-1.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
seo_title: Comment utiliser les procédures stockées MySQL pour simplifier les opérations
  de base de données
seo_desc: "In the realm of database management, MySQL has emerged as one of the most\
  \ popular and reliable choices. \nMySQL not only offers robust data storage capabilities\
  \ but also provides a powerful feature called \"procedures\" that allows developers\
  \ to streaml..."
---

Dans le domaine de la gestion de bases de données, MySQL s'est imposé comme l'un des choix les plus populaires et fiables. 

MySQL offre non seulement des capacités robustes de stockage de données, mais fournit également une fonctionnalité puissante appelée "procédures" qui permet aux développeurs de rationaliser les opérations complexes de base de données. 

Dans ce tutoriel, nous allons approfondir le concept des procédures MySQL et explorer leurs avantages. Ensuite, je fournirai un guide étape par étape sur la manière de les utiliser efficacement.

## Qu'est-ce que les procédures SQL ?

Les procédures SQL sont un ensemble d'instructions SQL regroupées pour former une unité logique de travail. Elles sont similaires aux fonctions ou méthodes dans les langages de programmation, vous permettant d'encapsuler des requêtes et opérations complexes en une seule entité réutilisable. 

Les procédures améliorent la modularité, la lisibilité et la maintenabilité du code, facilitant ainsi la gestion et l'exécution de tâches répétitives ou complexes de la base de données.

## Quand utiliser les procédures stockées

Prenons l'exemple d'un site web de commerce électronique, où nous avons la fonctionnalité de générer des rapports de ventes. Nous avons une table appelée `sales` avec laquelle nous allons travailler pour cet exemple.

Générer des rapports de ventes en temps réel peut être très consommatrice de ressources, surtout lorsqu'on traite de grands ensembles de données. En créant des procédures stockées qui agrègent et résument les données de ventes, nous pouvons optimiser le processus de reporting. 

Ces procédures peuvent calculer des métriques comme le total des ventes, les produits les plus vendus, ou le revenu par catégorie, facilitant ainsi la récupération rapide et efficace d'informations précieuses.

Voici le schéma de la table des ventes :

<table class=""><thead><tr><th role="textbox" aria-multiline="true" aria-label="Header cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Colonne</th><th role="textbox" aria-multiline="true" aria-label="Header cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Type</th></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">sale_id</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">int</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">customer_id</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">int</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">saled_date</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">datetime</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">total_amount</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">decimal</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">status</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">varchar(50)</td></tr></thead></table>

Pour illustrer un exemple simple, considérons que la table `sales` est peuplée avec 1 million de lignes de données fictives.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-108.png)
_Données fictives pour la table des ventes_

```
select count(*) from sales;
```

L'objectif est d'obtenir des rapports de ventes pour une période donnée.

```
CREATE PROCEDURE GenerateSalesReport (
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    SELECT DATE_FORMAT(order_date, '%Y-%m-%d') AS Date,
           COUNT(order_id) AS TotalOrders,
           SUM(total_amount) AS TotalSales
    FROM orders
    WHERE order_date BETWEEN start_date AND end_date
    GROUP BY DATE_FORMAT(order_date, '%Y-%m-%d');
END
```

La procédure stockée `GenerateSalesReport` prend deux paramètres d'entrée : `start_date` et `end_date`. Ceux-ci définissent la plage de dates pour le rapport de ventes. 

La procédure sélectionne la date de commande, compte le nombre de commandes et calcule le montant total des ventes dans la plage de dates spécifiée. Le résultat est groupé par date, en utilisant la fonction `DATE_FORMAT` pour l'afficher dans le format souhaité.

Maintenant, vous pourriez avoir une question :

> "Ne pouvons-nous pas obtenir le même résultat en utilisant une simple requête au lieu de créer une procédure stockée ?"

Eh bien, il est vrai qu'utiliser une simple requête est une option viable. Mais il existe plusieurs raisons convaincantes d'envisager l'utilisation d'une procédure stockée.

Voici quelques raisons qui semblent prometteuses pour utiliser des procédures stockées à certains endroits. 

1. Une procédure stockée offre l'avantage de la réutilisabilité du code. En encapsulant la logique de requête dans une procédure stockée, nous pouvons la réutiliser plusieurs fois sans dupliquer le code.
2. Au lieu de réécrire la même requête dans différentes parties de l'application, nous pouvons simplement appeler la procédure stockée chaque fois que nécessaire, rationalisant ainsi la base de code et la rendant plus facile à gérer et à mettre à jour.
3. L'utilisation d'une procédure stockée peut conduire à une amélioration des performances dans certains scénarios. Lorsqu'une procédure stockée est exécutée, le serveur de base de données peut optimiser le plan d'exécution et le mettre en cache pour les invocations ultérieures. Cette optimisation peut entraîner des temps d'exécution plus rapides, car le moteur de base de données utilise le plan mis en cache.
4. De plus, les procédures stockées peuvent minimiser les allers-retours réseau en combinant plusieurs requêtes en un seul appel, réduisant ainsi la surcharge associée aux exécutions de requêtes individuelles. Cette optimisation peut améliorer considérablement les performances globales, en particulier lors de la gestion d'opérations complexes ou de grands ensembles de données.
5. Un autre avantage significatif des procédures stockées est la sécurité renforcée. En accordant des privilèges d'exécution uniquement à la procédure stockée et non directement aux tables sous-jacentes, vous pouvez imposer un contrôle d'accès et protéger les données sensibles.

En résumé, bien qu'une simple requête puisse atteindre l'objectif souhaité, l'utilisation d'une procédure stockée offre des avantages distincts tels que la réutilisabilité du code, une meilleure performance grâce à l'optimisation des requêtes, une réduction de la surcharge réseau et une sécurité renforcée.

## Les éléments constitutifs des procédures stockées

Décomposons la procédure stockée et examinons chaque composant individuellement. Nous comprendrons la création et l'exécution de la procédure stockée dans MySQL. 

Il existe plusieurs IDE MySQL disponibles, et je recommande d'utiliser MySQL Workbench. Mais vous êtes libre de choisir l'IDE qui convient à vos préférences et besoins.

### Nom de la procédure

Chaque procédure stockée a un nom unique qui l'identifie dans la base de données. Le nom doit être descriptif et pertinent par rapport à l'objectif de la procédure.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-107.png)
_Définir une procédure_

```
CREATE PROCEDURE `GenerateSalesReport`()
BEGIN
END
```

### Paramètres

Les procédures stockées peuvent avoir des paramètres d'entrée qui permettent de passer des valeurs à la procédure lors de l'exécution. Nous définissons `start_date` et `end_date` comme nos paramètres d'entrée. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-106.png)
_Exemple de paramètres dans une procédure stockée_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
END
```

### Variables

Les variables sont utilisées pour stocker et manipuler des données au sein de la procédure stockée. Elles peuvent être déclarées et assignées selon les besoins. 

Il existe deux types de variables en SQL. Nous allons examiner chacun d'eux maintenant.

#### Variables de session

Les variables de session dans MySQL sont préfixées par le symbole `@` (par exemple `@variable_name`). Ces variables sont associées à la session ou connexion actuelle et conservent leurs valeurs tout au long de la session jusqu'à ce qu'elles soient explicitement modifiées ou que la session se termine.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-102.png)
_Définir une variable de session dans une procédure stockée_

```

CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
   SELECT @totalSales := 0;
   SELECT SUM(sales_amount) INTO @totalSales FROM sales;
   SELECT @totalSales As total_sales;
END
```

#### Variables régulières

Les variables régulières, également connues sous le nom de variables locales, sont déclarées en utilisant le mot-clé `DECLARE` dans le cadre d'une procédure stockée. Contrairement aux variables de session, les variables régulières n'ont pas le préfixe `@` (par exemple `variable_name`). Elles sont temporaires et n'existent que dans le bloc de code où elles sont déclarées.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-104.png)
_Définir une variable normale dans une procédure stockée_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
   DECLARE totalSales INT;
   SELECT SUM(sales_amount) INTO totalSales FROM sales;
END
```

### Instructions SQL

La fonctionnalité principale d'une procédure stockée est définie par des instructions SQL. Ces instructions peuvent inclure SELECT, INSERT, UPDATE, DELETE et d'autres commandes SQL pour interagir avec la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-105.png)
_Instructions SQL dans une procédure stockée_

```
CREATE PROCEDURE `GenerateSalesReport`(
    IN start_date DATE,
    IN end_date DATE
)
BEGIN
    SELECT DATE_FORMAT(saled_date, '%d-%m-%Y') AS Date,
           COUNT(sale_id) AS TotalOrders,
           SUM(total_amount) AS TotalSales
    FROM sales
    WHERE saled_date BETWEEN start_date AND end_date
    GROUP BY DATE_FORMAT(saled_date, '%d-%m-%Y');
END
```

### Appel de procédure

Pour exécuter la procédure stockée et générer un rapport de ventes détaillé pour une plage de dates spécifique, nous pouvons utiliser la syntaxe suivante :

```sql
CALL <procedure_name>(<parameter1>, ...);
```

```
CALL GenerateSalesReport('2021-01-01', '2023-12-31');
```

La capture d'écran ci-dessous montre le résultat de la procédure stockée. La partie intéressante est que cette requête a traité environ 1 million de données en une seconde. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-109.png)
_Résultat d'un exemple d'appel de procédure pour générer un rapport de ventes_

## Importance de l'utilisation des procédures stockées MySQL

### Amélioration des performances

Les procédures stockées offrent un avantage significatif en termes de performance par rapport aux requêtes SQL ad-hoc. Une fois qu'une procédure stockée est créée, elle est compilée et stockée sous une forme pré-optimisée. 

Ce processus de compilation élimine le besoin d'analyser et d'optimiser répétitivement les requêtes, ce qui entraîne des temps d'exécution plus rapides. En réduisant la surcharge associée au traitement des requêtes, les procédures stockées améliorent les performances globales des opérations de base de données.

### Sécurité renforcée

La sécurité est un aspect critique de la gestion des bases de données. Les procédures stockées permettent aux administrateurs de bases de données de définir des droits d'accès et des permissions pour l'exécution de procédures spécifiques. Ce contrôle granulaire garantit que seuls les utilisateurs autorisés peuvent interagir avec la base de données via les procédures, minimisant ainsi le risque d'accès ou de modifications non autorisés des données. 

En encapsulant les opérations sensibles au sein des procédures stockées, les vulnérabilités de sécurité sont réduites, renforçant ainsi la posture de sécurité globale de la base de données.

### Réutilisabilité et maintenabilité du code

Les procédures stockées favorisent la réutilisabilité, la modularité et la maintenabilité du code. En encapsulant les instructions SQL et les opérations fréquemment utilisées au sein d'une seule procédure, vous pouvez éviter la duplication de code et garantir une exécution cohérente dans plusieurs instances. 

Cette modularité facilite la maintenance et la mise à jour de la logique de la base de données. De plus, lorsque des modifications sont nécessaires, les changements peuvent être effectués en un seul endroit (la procédure stockée) plutôt qu'à plusieurs endroits, simplifiant ainsi le processus de maintenance.

### Contrôle des transactions

Les procédures stockées permettent le contrôle des transactions au sein de la base de données. Les transactions garantissent l'intégrité des données en regroupant plusieurs opérations de base de données en une seule unité logique. En exécutant une série d'opérations au sein d'une transaction, vous pouvez garantir que soit toutes les opérations sont réussies, soit aucune d'entre elles n'est appliquée. 

Cette atomicité garantit la cohérence des données et les protège contre la corruption. Les procédures stockées vous permettent de définir les limites des transactions, garantissant que les opérations complexes sont traitées de manière fiable et cohérente.

### Optimisation des performances et mise en cache du plan de requête

Un autre avantage de l'utilisation des procédures stockées est la capacité à optimiser les plans d'exécution des requêtes. 

Étant donné que les procédures stockées sont compilées et stockées, le moteur de base de données peut générer des plans d'exécution optimisés basés sur les statistiques de la procédure stockée et la distribution des données. Ces plans optimisés peuvent améliorer considérablement les performances des requêtes. 

De plus, les plans d'exécution des requêtes pour les procédures stockées sont mis en cache, ce qui réduit davantage la surcharge de génération de plans pour les exécutions ultérieures.

## Conclusion

Les procédures stockées sont un outil précieux dans la gestion des bases de données, et vous voudrez les utiliser dans des scénarios spécifiques. Lorsque vous traitez avec une logique métier complexe, que vous visez l'optimisation des performances, que vous renforcez la sécurité et le contrôle d'accès, que vous favorisez la réutilisabilité et la maintenabilité du code, que vous gérez des transactions complexes ou que vous intégrez des systèmes hérités, les procédures stockées peuvent offrir des avantages significatifs. 

En exploitant leur puissance de manière efficace, vous pouvez rationaliser vos opérations de base de données, améliorer les performances de l'application et simplifier la maintenance du code, conduisant à un environnement de base de données plus efficace et évolutif.

Si vous souhaitez en savoir plus sur SQL et les procédures stockées, abonnez-vous à ma [lettre d'information par email](https://5minslearn.gogosoon.com/?ref=fcc_sql_stored_procedure) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_sql_stored_procedure)) et suivez-moi sur les réseaux sociaux.