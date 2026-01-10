---
title: Construisez vous-même un CRM simple à partir de zéro en PHP et MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-01T05:26:50.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-crm-from-scratch-in-php-58fef061b075
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9ZxDtBiAUyVo6anPUJxkcg.jpeg
tags:
- name: crm
  slug: crm
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Construisez vous-même un CRM simple à partir de zéro en PHP et MySQL
seo_desc: 'By Richard

  Customer Relationship Management (CRM) is a system that manages customer interactions
  and data throughout the customer life-cycle between the customer and the company
  across different channels. In this tutorial, we are going to build a cus...'
---

Par Richard

La gestion de la relation client (CRM) est un système qui gère les interactions et les données des clients tout au long du cycle de vie du client entre le client et l'entreprise sur différents canaux. Dans ce tutoriel, nous allons construire un CRM personnalisé en PHP, qu'une équipe de vente peut utiliser pour suivre les clients tout au long du cycle de vente.

Nous allons créer un système CRM simple pour les commerciaux afin de :

* Accéder à leurs tâches
* Voir leurs prospects
* Créer de nouvelles tâches pour chaque prospect
* Créer une nouvelle opportunité
* Conclure une vente

Les responsables des ventes pourront :

* Gérer tous les clients
* Gérer l'équipe de vente
* Voir les activités de vente actuelles

[Télécharger les fichiers de démonstration](https://github.com/phpcontrols/phpgrid-custom-crm)

### Les éléments constitutifs d'un CRM

Voici une liste des composants essentiels du CRM :

* **Prospects** : contacts initiaux
* **Comptes** : Informations sur les entreprises avec lesquelles vous faites des affaires
* **Contact** : Informations sur les personnes que vous connaissez et avec lesquelles vous travaillez. Habituellement, un compte a plusieurs contacts
* **Opportunités** : Prospects qualifiés
* **Activités** : Tâches, réunions, appels téléphoniques, e-mails et toute autre activité qui vous permet d'interagir avec les clients
* **Ventes** : Votre équipe de vente
* **Tableau de bord** : Les tableaux de bord CRM sont bien plus que de simples éléments esthétiques. Ils doivent fournir des informations clés en un coup d'œil et offrir des liens pour obtenir plus de détails.
* **Connexion** : Les commerciaux et les responsables ont différents rôles dans le système. Les responsables ont accès aux rapports et aux informations sur le pipeline de vente.

![Image](https://cdn-media-1.freecodecamp.org/images/0*19oQRWbZyumceXfU.)

### Configuration requise du système

* PHP 5.3+,
* MySQL ou MariaDB
* [phpGrid](http://phpgrid.com/)

### Créer la base de données CRM

Nous allons commencer par créer notre base de données CRM personnalisée. Les principales tables que nous allons utiliser sont :

* **contact** — contient les données de base des clients
* **notes** — contient les informations collectées à partir des contacts par les commerciaux.
* **users** — informations sur les commerciaux

![Image](https://cdn-media-1.freecodecamp.org/images/0*gJgr4DrRJ3O_OEYr.)

La table **Contact** contient les informations de base sur les clients, y compris les noms, les adresses des entreprises, les informations sur les projets, et ainsi de suite.

La table **Notes** stocke toutes les informations sur les activités de vente telles que les réunions et les appels téléphoniques.

La table **Users** contient les informations de connexion sur les utilisateurs du système telles que les noms d'utilisateur et les mots de passe. Les utilisateurs peuvent également avoir des rôles, tels que Vendeur ou Responsable.

Toutes les autres tables sont des [tables de référence](https://www.quora.com/In-database-what-are-lookup-tables) pour joindre les trois principales tables de base de données relationnelles.

* **contact_status** — contient le statut du contact tel que Prospect et Opportunité. Chacun indique une étape différente dans un cycle de vente typique
* **task_status** — le statut de la tâche peut être soit En attente soit Complétée
* **user_status** — un commercial peut être Actif ou Inactif
* **todo_type** — un type de tâche soit Tâche soit Réunion
* **todo_desc** — description d'une tâche telle que Suivi par e-mail, Appel téléphonique, et Conférence, etc.
* **roles** — un utilisateur peut être soit un Représentant commercial soit un Responsable

#### Schéma complet de la base de données

Un schéma de base de données est la structure qui représente la vue logique telle que les tables, les vues, ou les clés primaires et étrangères de l'ensemble de la base de données. Un schéma de base de données inclut des entités et la relation entre elles.

Il est bon de pratique d'avoir une clé primaire pour chaque table dans une base de données relationnelle. Une clé primaire est un identifiant unique pour chaque enregistrement. Il peut s'agir du numéro de sécurité sociale (SSN), du numéro d'identification du véhicule (VIN), ou d'un numéro auto-incrémenté. Il s'agit d'un numéro unique qui est généré lorsqu'un nouvel enregistrement est inséré dans une table.

Ci-dessous se trouve le diagramme de la base de données de notre CRM simple. Le symbole de clé dans chaque table représente la clé primaire de la table. La loupe indique la clé étrangère reliant une autre table dans la base de données. Parfois, nous l'appelons la table de "référence".

![Image](https://cdn-media-1.freecodecamp.org/images/0*qExvrxjr5WZERLEO.)

#### install.sql

Une fois que vous avez compris la structure de la table de la base de données, trouvez le script "install.sql" dans le dossier `db` et utilisez un outil MySQL tel que [MySQL Workbench](http://www.mysql.com/products/workbench/) ou [Sequel Pro](https://www.sequelpro.com/) pour exécuter le script SQL. Il devrait créer une nouvelle base de données relationnelle nommée `custom_crm` et ses tables de base de données.

### Une note sur ZenBase

```
L'application CRM est également l'un des nombreux modèles d'applications prêts à l'emploi disponibles sur ZenBase (construit sur phpGrid) pour que chacun — avec ou sans compétences en codage — puisse utiliser et personnaliser selon ses propres besoins.
```

### Configuration de phpGrid

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZ9ZZsPaUVIiGZkgcbpSDQ.jpeg)

Notre CRM contient de nombreuses grilles de données. La grille de données est une table de données similaire à une feuille de calcul qui affiche des lignes et des colonnes représentant des enregistrements et des champs de la table de la base de données. La grille de données donne à l'utilisateur final la possibilité de lire et d'écrire dans les tables de la base de données sur une page web. Nous pouvons utiliser un outil de grille de données de [phpGrid](http://phpgrid.com/). Nous utilisons un outil au lieu de les construire à partir de zéro car le développement de la grille de données est généralement fastidieux et sujet aux erreurs. La bibliothèque de grilles de données gérera toutes les opérations internes de la base de données **CRUD (Create, Remove, Update, and Delete)** pour nous avec de meilleurs et plus rapides résultats avec peu de code. Pour installer phpGrid, suivez ces étapes :

1. Décompressez le fichier de téléchargement de phpGrid.
2. Téléchargez le dossier phpGrid dans le dossier `phpGrid`.
3. Terminez l'installation en configurant le fichier `conf.php`.

Avant de commencer à coder, nous devons spécifier les informations de la base de données dans `conf.php`, le fichier de configuration de phpGrid. Voici un exemple de paramètres de connexion à la base de données :

* **PHPGRID_DB_HOSTNAME** — IP ou nom d'hôte du serveur web
* **PHPGRID_DB_USERNAME** — nom d'utilisateur de la base de données
* **PHPGRID_DB_PASSWORD** — mot de passe de la base de données
* **PHPGRID_DB_NAME** — nom de la base de données de notre CRM
* **PHPGRID_DB_TYPE** — type de base de données
* **PHPGRID_DB_CHARSET** — toujours 'utf8' dans MySQL

Pour en savoir plus sur la configuration de phpGrid, consultez le [guide d'installation complet de phpGrid](http://phpgrid.com/documentation/installation/).

### Modèle de page

![Image](https://cdn-media-1.freecodecamp.org/images/0*nnv7_XJ9KD0zLXqK.)

Avant de pouvoir commencer à construire notre première page du CRM, il est bon de pratique de créer des éléments de page réutilisables tels que l'en-tête et le pied de page.

La page se composera d'un en-tête, d'un menu, d'un corps et d'un pied de page. Nous allons commencer par créer un modèle de page réutilisable.

### head.php

Il s'agit d'un en-tête de modèle HTML5 de base. Il inclut un lien vers une feuille de style personnalisée qui sera créée dans une étape ultérieure.

### menu.php

![Image](https://cdn-media-1.freecodecamp.org/images/0*TDduZwwNWj64wN77.)

Remarquez l'utilisation de `$_GET['currentPage']`. Chaque page définira une valeur qui mettra en évidence le nom de la page actuelle dans la barre de menu supérieure.

Incluez le code suivant dans style.css pour le style du menu (minifié). Il transformera la liste non ordonnée ci-dessus en un menu.

### footer.php

Balises de fermeture simples pour le corps et le html.

### Modèle de page complet

Il s'agit du modèle de page complet. Le contenu principal ira après `Section Title`.

### Pages principales du CRM

![Image](https://cdn-media-1.freecodecamp.org/images/1*z5iaw9R1XH1qCwIeE7-QfA.jpeg)

Êtes-vous toujours avec moi ? Bien ! Nous pouvons maintenant enfin développer la première page de notre CRM.

Notre CRM pour les membres de l'équipe de vente comporte quatre pages :

* **Tâches**
* **Prospects**
* **Opportunités**
* **Clients/Gagnés**

Chaque page indique une étape différente dans un cycle de vente typique.

### Maquette de conception de la page des commerciaux

Voici notre maquette de conception de CRM pour les commerciaux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AS942OO-igxo4ylg8f7m5g.png)

### Page des tâches

Lorsque qu'un membre de l'équipe de vente se connecte, la première page qu'il voit est une liste des tâches actuelles.

Comme vous vous en souvenez peut-être, notre table Notes contient toutes les informations sur les activités de vente. Nous pouvons créer une grille de données et la remplir à partir de la table Notes en utilisant phpGrid.

Le contenu principal de la page des tâches est une grille de données. Les deux lignes suivantes nous donneront une liste des tâches du commercial actuel.

* La première ligne crée un objet phpGrid en passant l'instruction SQL SELECT, sa clé primaire — `ID`, puis le nom de la table de la base de données — `notes`.
* La deuxième et dernière ligne appelle la fonction [display()](http://phpgrid.com/documentation/display/) pour afficher la grille de données à l'écran. Consultez la [démonstration de la grille de données de base](http://phpgrid.com/example/example-1-a-basic-php-datagrid-2/) pour plus de détails.

### Page des prospects

La page des prospects contient la liste des prospects actuels dont le commercial est responsable. Chaque prospect peut avoir une ou plusieurs notes. Nous utiliserons la fonctionnalité [phpGrid master-detail](http://phpgrid.com/example/master-detail-grid/) pour cela.

Nous devons également utiliser [set_query_filter](http://phpgrid.com/documentation/set_query_filterwhere/)() pour afficher uniquement les prospects, `Status = 1`, et uniquement pour le commercial actuel.

#### Table de statut des contacts

![Image](https://cdn-media-1.freecodecamp.org/images/0*GJDLBk0XN5r9M5NY.)

### Page des opportunités

Un prospect devient une opportunité une fois qu'il est qualifié. La page des opportunités est similaire à la page des prospects. La seule différence est le code de statut filtré dans set_query_filter qui est `Status = 2`.

### Page des clients/gagnés

Les clients/gagnés ont le `Status = 3`. Similaire aux prospects et aux opportunités, les clients/gagnés peuvent également avoir des notes.

C'est tout ce qu'il y a à faire pour les commerciaux dans notre CRM simple.

### Tableau de bord du responsable

![Image](https://cdn-media-1.freecodecamp.org/images/1*AI44nH7B8mnNLTKqulmjGA.jpeg)
_Photo par [Unsplash](http://unsplash.com/photos/rS1GogPLVHk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Eaters Collective</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Le responsable des ventes aura accès à tous les enregistrements dans le pipeline de vente ainsi qu'à la capacité de gérer l'équipe de vente et les données clients.

Nous aurons une seule page web avec un menu à onglets similaire à la [démonstration de grille à onglets phpGrid](http://phpgrid.com/example/tabbed-datagrid/).

### Maquette de conception du tableau de bord du responsable

#### Mes représentants commerciaux

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jn0q3g0FMqW6shEXtENR8w.png)

### Contenu principal

Chaque onglet représente une table dans la base de données CRM. `$_GET['gn']` stockera le nom de la table. Il génère dynamiquement la grille de données en fonction du nom de la table passé.

Il est très facile d'intégrer les onglets jQueryUI avec phpGrid. Veuillez vous référer à la démonstration de [Tabbed Grid](http://phpgrid.com/example/tabbed-datagrid/) de phpGrid pour plus d'informations.

### Page de mes représentants commerciaux

Puisqu'un responsable des ventes doit rapidement savoir avec qui un commercial travaille, nous avons ajouté une grille de détails `$sdg` remplie à partir de la table de contacts et liée à la grille principale.

`sales_rep` est la clé de connexion dans la table `contact` à l'`id` qui est la clé étrangère dans la table `users`. Rappelez-vous que `users` stocke toutes les informations sur nos commerciaux.

### Captures d'écran

#### CRM — Écran de vente

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_osyaKXAm8Paj6OTVpCsg.png)

#### CRM — Écran du responsable

![Image](https://cdn-media-1.freecodecamp.org/images/1*wMcbdN9Im5jAUhv-mfEN_g.png)

### Démo en direct

[Écran du représentant commercial CRM](http://phpdatagrid.com/apps/phpgrid-custom-crm/sales/tasks.php) | [Écran des responsables CRM](http://phpdatagrid.com/apps/phpgrid-custom-crm/managers/pipeline.php)

### Besoin d'écrire encore moins de code ?

Si vous êtes nouveau en programmation et que vous n'êtes pas encore à l'aise avec le codage, vous pouvez consulter [**ZenBase**](https://getzenbase.com/) qui est construit sur phpGrid. Le CRM n'est qu'un des [nombreux modèles d'applications](https://getzenbase.com/templates/) prêts à l'emploi disponibles sur ZenBase pour que chacun — _avec ou sans_ compétences en codage — puisse utiliser et personnaliser selon ses propres besoins.

### Code source complet sur GitHub

[**phpcontrols/phpgrid-custom-crm**](https://github.com/phpcontrols/phpgrid-custom-crm)
[_phpgrid-custom-crm - Démo CRM personnalisé - Apprenez à construire vous-même un CRM personnalisé en PHP et MySQL, qu'une équipe de vente peut..._github.com](https://github.com/phpcontrols/phpgrid-custom-crm)

### Merci d'avoir lu. Si vous avez aimé cet article, veuillez cliquer sur ce bouton d'applaudissements ? pour aider les autres à le trouver et me [suivre sur Twitter.](https://twitter.com/midlifesaas)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-_G34PI1sMmIxI1xstaYQ.png)