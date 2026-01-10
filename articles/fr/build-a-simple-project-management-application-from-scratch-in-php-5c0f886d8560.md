---
title: Comment créer une application de gestion de projet en PHP & MySQL à partir
  de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-06T07:47:30.000Z'
originalURL: https://freecodecamp.org/news/build-a-simple-project-management-application-from-scratch-in-php-5c0f886d8560
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p6kGOdvkbqMJQKuSYgDvOg.jpeg
tags:
- name: PHP
  slug: php
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de gestion de projet en PHP & MySQL à partir
  de zéro
seo_desc: 'By Richard

  Trying to find a project management application is a daunting task: you want a system
  with powerful features and you must get a buy-in from your colleagues. Most of the
  time, you wind up with a bloated system filled with features you’ll ne...'
---

Par Richard

Essayer de trouver une application de gestion de projet est une tâche ardue : vous voulez un système avec des fonctionnalités puissantes et vous devez obtenir l'adhésion de vos collègues. La plupart du temps, vous vous retrouvez avec un système surchargé de fonctionnalités que vous n'utiliserez jamais.

La bonne nouvelle, c'est qu'il s'avère qu'il n'est pas si difficile d'en construire une soi-même à partir de zéro. Après avoir lu ce tutoriel, vous devriez avoir une application de gestion de projet propre et bien conçue opérationnelle en moins d'une heure.

### Qu'est-ce qu'une application de gestion de projet ?

Une application de gestion de projet est un système logiciel utilisé pour la planification de projet, l'allocation des ressources, le suivi des composants du projet et la gestion des changements.

Dans ce tutoriel, nous allons construire un système simple de gestion de projet en PHP que les employés et les managers peuvent utiliser pour la collaboration et la communication entre les parties prenantes du projet.

### Que contient une application de gestion de projet ?

Nous allons créer un système de gestion de projet simple et facilement personnalisable qui suit les projets, y compris les jalons, les tâches, les heures, les coûts, et plus encore. Comme chaque projet est unique, ce tutoriel vise simplement à construire une base d'application ; vous devriez pouvoir l'étendre facilement en fonction de vos besoins.

**Dans notre application de gestion de projet, les employés pourront :**

* Voir leurs tâches
* Enregistrer les heures travaillées

**Les managers pourront :**

* Gérer les projets
* Gérer les jalons
* Gérer les tâches
* Gérer les coûts et les heures
* Gérer les ressources des employés

### Les éléments constitutifs d'un système de gestion de projet

![Image](https://cdn-media-1.freecodecamp.org/images/1*UlZUWinmrB6UXBV0D3CDeQ.jpeg)
_Éléments constitutifs d'un système typique de gestion de projet_

Voici les fonctions principales d'un système de gestion de projet :

* **Planification de projet** : Pour définir un calendrier de projet, un chef de projet peut utiliser le logiciel pour cartographier les tâches du projet et décrire visuellement les interactions des tâches.
* **Gestion des tâches** : Permet au chef de projet de créer et d'assigner des tâches, d'établir des délais et de produire des rapports d'état.
* **Gestion des ressources** : Définit les responsabilités — qui est censé faire quoi.
* **Budget et suivi des coûts** : Une bonne application de gestion de projet facilite les rapports budgétaires ainsi que la visualisation, la notification et la mise à jour des coûts pour les parties prenantes.
* **Suivi du temps** : Le logiciel doit avoir la capacité de suivre le temps passé sur toutes les tâches et de maintenir des enregistrements pour les consultants tiers.

### Configuration requise du système

* PHP 5.3+
* MySQL ou MariaDB
* phpGrid

### Création d'une base de données de gestion de projet

Nous allons commencer par créer notre base de données de gestion de projet. Les principales tables que nous allons utiliser sont :

* **Clients** — données de l'entreprise cliente
* **Contacts** — données de contact du client. Un client peut avoir un ou plusieurs contacts.
* **Projects** — informations sur le projet
* **Milestones** — jalon du projet
* **Tasks** — tâches du projet
* **Hours** — temps passé sur chaque tâche
* **Costs** — coût d'une tâche
* **Users** — données de l'utilisateur ; un utilisateur peut être soit un employé, soit un manager

![Image](https://cdn-media-1.freecodecamp.org/images/0*4LoHe5Bje3Yxtxry.png)

Autres tables ([tables de référence) :

* **ms_status**
* **proj_status**
* **task_status**

#### Diagramme complet du schéma de la base de données

Un schéma de base de données est la structure qui représente la vue logique de l'ensemble de la base de données : tables, vues, et clés primaires et étrangères. Un schéma de base de données inclut toutes les entités et les relations entre elles.

Ci-dessous se trouve le diagramme de la base de données de notre application simple de gestion de projet. Le symbole de clé dans chaque table représente la clé primaire de la table tandis que la loupe indique une clé étrangère la reliant à une autre table (table de référence) dans la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/0*r5SvnI9MG2xR8Nlk.png)

#### simple_pm_install.sql

Une fois que vous avez compris la structure des tables de la base de données, obtenez le script sql [**simple_pm_install.sql**](https://github.com/phpcontrols/phpgrid-project-management/blob/master/db/simple_pm_install.sql) depuis le dépôt GitHub de ce tutoriel, puis exécutez le script sql en utilisant un outil MySQL tel que MySQL Workbench ou Sequel Pro. Cela créera une nouvelle base de données nommée `simple_pm` et les tables dont nous avons besoin dans ce tutoriel.

### Configuration de phpGrid

Notre application simple de gestion de projet contient de nombreuses DataGrids. La DataGrid est un tableau de données similaire à une feuille de calcul qui affiche des lignes et des colonnes représentant des enregistrements et des champs de la table de la base de données. La DataGrid offre à l'utilisateur final la possibilité de lire et d'écrire dans les tables de la base de données sur une page web.

Pour créer la DataGrid, nous utilisons un outil de dataGrid de [phpGrid](https://phpgrid.com/). La raison pour laquelle nous utilisons un outil au lieu de construire nos grilles à partir de zéro est que le développement d'une DataGrid en php est généralement extrêmement fastidieux et sujet aux erreurs. La bibliothèque DataGrid de phpGrid gérera toutes les opérations internes de la base de données **CRUD (Create, Remove, Update, and Delete)** pour nous, offrant des résultats plus rapides et meilleurs avec un codage minimal.

Pour installer phpGrid, suivez ces étapes :

1. Décompressez le fichier de téléchargement de phpGrid.
2. Téléchargez le dossier phpGrid dans le dossier `**phpGrid**`.
3. Terminez l'installation en configurant le fichier `**conf.php**`.

Avant de commencer à coder, nous devons inclure les informations suivantes dans le fichier de configuration `conf.php` de phpGrid. Voici un exemple des paramètres de connexion à la base de données :

```
define('PHPGRID_DB_HOSTNAME', 'localhost'); define('PHPGRID_DB_USERNAME', 'root'); define('PHPGRID_DB_PASSWORD', ''); define('PHPGRID_DB_NAME', 'custom_pm'); define('PHPGRID_DB_TYPE', 'mysql');
```

* **PHPGRID_DB_HOSTNAME** — IP ou nom d'hôte du serveur web
* **PHPGRID_DB_USERNAME** — nom d'utilisateur de la base de données
* **PHPGRID_DB_PASSWORD** — mot de passe de la base de données
* **PHPGRID_DB_NAME** — nom de la base de données
* **PHPGRID_DB_TYPE** — type de base de données
* **PHPGRID_DB_CHARSET** — toujours 'utf8' dans MySQL

### Modèle de page

![Image](https://cdn-media-1.freecodecamp.org/images/0*0wRyhPo3UlSTHqBR.png)

Notre page sera composée d'un **en-tête**, d'un **menu**, d'un **corps** et d'un **pied de page**. Au lieu de créer les mêmes éléments de page à plusieurs reprises, nous allons commencer par créer un modèle de page réutilisable.

#### head.php

Il s'agit d'un en-tête de modèle HTML5 de base ; il inclut un lien vers une feuille de style personnalisée qui sera créée dans une étape ultérieure.

#### menu.php

![Image](https://cdn-media-1.freecodecamp.org/images/0*AwNHOfr7NQte7_PV.png)

Remarquez l'utilisation de `$_GET['currentPage']`. Chaque page définira une valeur qui mettra en surbrillance le nom de la page actuelle dans la barre de menu supérieure.

Incluez le code suivant dans `**style.css**` pour le style du menu ; il transformera la liste non ordonnée ci-dessus en un menu.

#### footer.php

Inclut simplement les balises de fermeture des éléments que nous avons ouverts dans l'en-tête :

### Notre modèle de page réutilisable complet

Le contenu principal viendra après le titre de la section.

### Pages principales de gestion de projet

![Image](https://cdn-media-1.freecodecamp.org/images/1*unOpP83dlvhHy5MlQjg1Uw.jpeg)

Notre application de gestion de projet pour les managers comporte quatre pages :

* **Clients**
* **Détails du client**
* **Projets**
* **Détails du projet**

La page **Clients** affiche une liste de clients avec des liens vers les détails individuels des clients (page **Détails du client**).

La page **Projets** affiche une liste des projets gérés avec des liens vers les détails des projets (page **Détails du projet**).

#### Maquette de conception

Voici notre maquette de conception de l'application de gestion de projet pour les chefs de projet qui gèrent un ou plusieurs projets et assignent des tâches aux employés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ozCobyEZ-YFB0v4e.png)

#### Clients

Lorsque le manager se connecte au système de gestion de projet, la première page qu'il voit est la page **Clients** qui contient une liste complète des entreprises.

Le code suivant nous donnera une liste de clients.

* La première ligne crée un objet phpGrid en passant l'instruction SQL SELECT avec sa clé primaire `**id**` suivie du nom de la table de la base de données — `**clients**`.
* La deuxième ligne crée une URL dynamique à partir de la clé primaire « id » ; elle utilise une fonction appelée `**set_col_dynalink()**`. Cette fonction définit une colonne spécifique pour afficher l'URL de l'hyperlien HTML basée sur des valeurs dynamiques. Si la clé primaire « id » a la valeur 100, elle affichera une URL comme celle-ci `**client-details.php?id=100**` qui redirige vers la page des détails du client.
* La troisième ligne, `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)`, rend la DataGrid éditable et toutes les opérations CRUD (Create, Read, Update, Delete) sont maintenant accessibles.
* La dernière ligne appelle la fonction `[**display()**](https://phpgrid.com/documentation/display/)` pour afficher la DataGrid à l'écran.

Vous pouvez trouver plus de démonstrations ci-dessous en utilisant ces fonctions :

[**Afficher une URL dynamique | phpGrid**](https://phpgrid.com/example/display-dynamic-url/)  
[_Dans l'exemple ci-dessus, nous apprenons que phpGrid peut afficher une URL simple et statique en utilisant la méthode set_col_link(). Cependant, elle peut aussi..._phpgrid.com](https://phpgrid.com/example/display-dynamic-url/)[**CRUD PHP Datagrid (Datagrid éditable) * | phpGrid**](https://phpgrid.com/example/edit-datagrid/)  
[_La datagrid PHP n'est pas éditable par défaut. Vous pouvez activer l'édition en appelant simplement enable_edit(). Voila!_phpgrid.com](https://phpgrid.com/example/edit-datagrid/)

#### Détails du client

À partir de la page **Clients**, le nom du client a un hyperlien qui redirige vers la page **Détails du client** pour ce client lorsqu'on clique dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*P8YU_L6z6plrZ2OD.png)

À partir de la page **Détails du client**, nous devons obtenir l'ID du client qui est passé en tant que paramètre d'URL.

Dans notre application, l'ID du client doit toujours être un entier. Ainsi, nous utilisons la fonction PHP `[**intval()**](http://php.net/manual/en/function.intval.php)` pour nous assurer que l'ID du client est retourné en tant qu'entier.

Le code suivant affiche les projets associés à l'`$clientId` actuel en utilisant la fonction de filtre `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)`. De plus, nous rendons la DataGrid éditable avec la fonction `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)` ; phpGrid s'occupera de toutes les opérations CRUD pour nous.

**Détails du client > Projets**

Comme vous l'avez peut-être remarqué, nous utilisons à nouveau la même fonction, `**set_col_dynalink()**`, pour créer des hyperliens vers la table **Détails du projet** en utilisant l'ID du projet. Nous aborderons la page `**project-details.php**` ensuite.

```
<h4>Projets</h4>
```

**Détails du client > Contacts**

Sous la DataGrid **Projets**, une liste de contacts associés à l'`$clientid` est affichée en utilisant les mêmes fonctions `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)` et `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)`.

#### Contacts

#### Projets

Maintenant, construisons la page **Projets**.

La page **Projets** affiche une liste des projets gérés. Elle est très similaire à la page **Clients**, sauf que la table de la base de données est « Projects », et que les hyperliens ont l'URL `**project-details.php**` au lieu de `**client-details.php**`.

#### Détails du projet

À partir de la page **Projets**, chaque nom de projet a un hyperlien qui redirige vers chaque page individuelle **Détails du projet** lorsqu'on clique dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/0*i5TQaclrfxGruHgv.png)

Et à partir de la page **Détails du projet**, nous récupérons l'ID du projet pour le paramètre d'URL.

Cela vous semble familier ? Parce que c'est le cas ! Cela devrait être le cas car **Projets** et **Détails du projet** suivent à peu près le même modèle de codage utilisé dans les pages **Clients** et **Détails du client** ; il n'y a pas vraiment de surprises.

La page **Détails du projet** est composée des grilles suivantes, toutes filtrées par l'`$projectId` obtenu à partir du paramètre d'URL.

* **Jalons**
* **Tâches**
* **Heures**
* **Coûts**

#### Jalons

Un jalon marque un événement majeur dans le calendrier d'un projet. Ici, nous pouvons facilement afficher tous les jalons d'un projet en filtrant la valeur `$projectId`. Les chefs de projet ont les droits d'accès nécessaires pour modifier les jalons.

De même, nous pouvons facilement filtrer et afficher une liste de tâches pour le projet actuel.

Je pense que vous commencez probablement à comprendre maintenant. Voici le code pour les deux dernières datagrids.

### Page des employés

Nous pouvons maintenant passer à la dernière partie du tutoriel, la page **Employés**. Les employés peuvent se connecter pour voir les tâches de projet actives qui leur sont assignées, suivre les heures des tâches et les coûts. Leur responsabilité est simple : surveiller les tâches et enregistrer les heures travaillées sur une tâche de projet spécifique.

### Maquette de conception

![Image](https://cdn-media-1.freecodecamp.org/images/0*rTydMfZp34UUZDmq.png)

#### Menu

La page **Employés** n'a qu'un seul élément de menu : **Tâches**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*r6uIHldzshuM7tTM.png)

#### Mes tâches actives

La première partie de la page montre une liste des tâches actives assignées à l'employé actuel. Chaque tâche aura les heures déclarées par l'employé actuel ; c'est une situation parfaite pour utiliser une [sous-grille phpGrid](https://phpgrid.com/example/subgrid/).

Nous devons également utiliser `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)` pour afficher uniquement les tâches actives qui ont une valeur de statut « 2 », et uniquement pour l'employé actuel.

À des fins de démonstration, nous avons codé en dur l'ID de l'employé à 2. Dans une application réelle, la valeur de l'ID de l'employé doit être stockée et récupérée en utilisant [PHP SESSION](http://php.net/manual/en/book.session.php).

Nous créons ensuite la DataGrid **Tâches** active pour l'employé actuel. Remarquez la fonction de filtre.

Une fois que nous avons défini la grille pour les tâches actives, nous créons une DataGrid pour enregistrer les heures déclarées par l'employé actuel.

Enfin, `[**set_subgrid()**](https://phpgrid.com/documentation/set_subgrid/)` fait en sorte que la DataGrid **Heures** devienne une sous-grille de la DataGrid **Tâches**. Le champ de liaison dans la sous-grille **Heures** est 'TaskID', qui est le deuxième paramètre, et dans la grille principale **Tâches**, c'est 'id', le troisième paramètre.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nhIZDWCH9ED_BMCi.png)

#### Mon historique des heures

Enfin, nous aimerions afficher une DataGrid en lecture seule en utilisant les données de la table **Heures** pour l'employé actuel à des fins de révision.

Remarquez que nous avons utilisé une fonction appelée `[**set_jq_gridName()**](https://phpgrid.com/documentation/set_jq_gridname/)`. Vous pouvez trouver plus de documentation [ici](https://phpgrid.com/documentation/set_jq_gridname/). Cette fonction définit un nom d'objet unique pour la DataGrid. Par défaut, phpGrid utilise le nom de la table de la base de données comme nom d'objet interne. Puisque nous avons déjà créé une DataGrid à partir de la table **Heures** dans la dernière partie, nous devons définir un nom unique pour notre deuxième DataGrid **Heures**.

### Captures d'écran de l'application

#### Managers

![Image](https://cdn-media-1.freecodecamp.org/images/0*0nxynYSGiECfL0X7.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*nXppkdoX82Cu90yz.png)

#### Employé

![Image](https://cdn-media-1.freecodecamp.org/images/0*5-IFndGjMJ_h82dJ.png)

### Démo en direct

[Se connecter en tant que manager](https://www.phpdatagrid.com/apps/phpgrid-project-management/manager/clients.php) | [Se connecter en tant qu'employé](https://www.phpdatagrid.com/apps/phpgrid-project-management/employee/tasks.php)

### Télécharger le code source

[**phpcontrols/phpgrid-project-management**](https://github.com/phpcontrols/phpgrid-project-management)  
[_phpgrid-project-management — Application de démonstration complète de gestion de projet phpGrid_github.com](https://github.com/phpcontrols/phpgrid-project-management)

### Merci d'avoir lu. Si vous avez aimé cet article, veuillez cliquer sur le bouton d'applaudissements ? pour aider les autres à le trouver et [me suivre sur Twitter.](https://twitter.com/midlifesaas)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-_G34PI1sMmIxI1xstaYQ.png)