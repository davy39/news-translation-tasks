---
title: Comment utiliser l'interface en ligne de commande WordPress – Tutoriel WP-CLI
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2023-08-11T21:37:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-wordpress-cli
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pexels-pixabay-207580.jpg
tags:
- name: command line
  slug: command-line
- name: WordPress
  slug: wordpress
seo_title: Comment utiliser l'interface en ligne de commande WordPress – Tutoriel
  WP-CLI
seo_desc: "In the world of website development and content management, efficiency\
  \ and automation are key. The WordPress Command Line Interface – or WP-CLI – is\
  \ a powerful tool that can help you streamlines tasks and manage WordPress websites\
  \ more effectively. \n..."
---

Dans le monde du développement web et de la gestion de contenu, l'efficacité et l'automatisation sont essentielles. L'interface en ligne de commande WordPress – ou WP-CLI – est un outil puissant qui peut vous aider à rationaliser les tâches et à gérer les sites WordPress plus efficacement. 

Cet article fournit un aperçu de WP-CLI, en mettant l'accent sur ses capacités à créer, modifier et supprimer des utilisateurs, ainsi qu'à gérer les plugins avec facilité. Cet article vous montrera comment WP-CLI peut considérablement améliorer votre expérience de gestion WordPress.

## Qu'est-ce que WP-CLI ?

WP-CLI est un outil en ligne de commande conçu pour gérer les installations WordPress. Il permet aux développeurs, administrateurs et propriétaires de sites d'interagir avec leurs sites web directement depuis la ligne de commande, en évitant le besoin d'interventions manuelles via l'interface web. 

Il est construit sur PHP et offre une large gamme de commandes que vous pouvez exécuter directement depuis le terminal.

En utilisant WP-CLI, vous serez en mesure de gérer vos sites WordPress beaucoup plus efficacement. Voici quelques exemples de la manière dont les commandes WP-CLI peuvent simplifier votre flux de travail :

## Commandes WP-CLI

### Récupération des informations du site

La commande `wp site info` fournit un aperçu rapide des détails importants de votre site WordPress, y compris l'URL du site, le nombre de publications et de pages, le thème actif, et plus encore. 

Par exemple, en exécutant `wp site info`, vous pouvez rapidement recueillir des informations essentielles sur votre site sans naviguer dans le tableau de bord d'administration WordPress.

### Gestion de la base de données

WP-CLI vous permet de gérer votre base de données WordPress de manière transparente. Utilisez la commande `wp db export` pour créer un fichier d'exportation de la base de données, assurant ainsi une sauvegarde des données de votre site. 

Si vous devez importer des données, la commande `wp db import` facilite ce processus. Par exemple, si vous avez une sauvegarde de base de données nommée `backup.sql`, l'exécution de `wp db import backup.sql` restaure la base de données à un état précédent.

### Manipulation des thèmes

Manipuler les thèmes est extrêmement efficace avec WP-CLI. Par exemple, la commande `wp theme install` vous permet d'installer un thème directement depuis le dépôt officiel des thèmes WordPress. Pour installer le thème "Twenty Twenty-One", vous pouvez utiliser la commande `wp theme install twentytwentyone`.

### Création de publications et de pages

La génération de nouveau contenu est facilitée grâce à WP-CLI. Les commandes `wp post create` et `wp post generate` vous permettent de créer et de remplir des publications et des pages avec du contenu. 

Par exemple, `wp post create --post_type=post --post_title="Nouvelle Publication"` crée une nouvelle publication avec le titre spécifié.

Ces exemples illustrent la polyvalence et la puissance de WP-CLI dans la gestion de divers aspects de votre site WordPress. En exploitant ses capacités, vous pouvez améliorer votre efficacité, réduire les tâches manuelles et obtenir un meilleur contrôle sur la gestion de votre site web.

## Comment installer WP-CLI

Avant de plonger dans d'autres fonctionnalités de WP-CLI, comprenons le processus d'installation. 

Vous pouvez installer WP-CLI globalement sur votre système, le rendant accessible depuis n'importe quel répertoire. 

Pour installer WP-CLI, assurez-vous d'avoir PHP installé, ainsi qu'une version compatible de WordPress. Téléchargez l'archive Phar, placez-la dans un répertoire accessible via le PATH de votre système, et vous êtes prêt à partir. 

Vous pouvez vérifier l'installation en tapant `wp --info` dans votre terminal. [Ici](https://wp-cli.org) vous pouvez trouver la documentation avec l'URL pour télécharger WP-CLI avec un wget.

## Comment gérer les utilisateurs avec WP-CLI

Gérer les utilisateurs est une tâche fondamentale lors de la supervision d'un site WordPress. WP-CLI simplifie la gestion des utilisateurs avec diverses commandes qui rendent la création, la modification et la suppression des utilisateurs beaucoup plus faciles.

### Comment créer des utilisateurs

La commande `wp user create` vous permet de créer rapidement des utilisateurs directement depuis la ligne de commande. 

Pour illustrer, créons un nouvel utilisateur nommé "Alice" avec l'adresse e-mail "alice@example.com" et le rôle d'éditeur. Il suffit d'entrer :

```
wp user create alice alice@example.com --role=editor

```

### Comment modifier des utilisateurs

WP-CLI simplifie également les modifications des utilisateurs. Utilisez la commande `wp user update` pour ajuster les détails d'un utilisateur. 

Par exemple, changeons le nom d'affichage d'Alice en "Alice Johnson" en utilisant la commande suivante :

```
wp user update 123 --display_name="Alice Johnson"

```

Dans cet exemple, "123" est l'ID d'Alice.

### Comment supprimer des utilisateurs

Lorsque les comptes utilisateurs deviennent obsolètes ou nécessitent une suppression pour des raisons de sécurité, WP-CLI simplifie le processus. 

Pour supprimer un utilisateur, utilisez la commande `wp user delete`. Pour supprimer le compte d'Alice, il suffit d'exécuter :

```
wp user delete 123 --reassign=567

```

Dans ce cas, "123" est l'ID d'Alice et "567" est l'ID de l'utilisateur auquel vous souhaitez attribuer le contenu d'Alice (par exemple, les publications, les pages, etc.).

## Comment gérer les plugins avec WP-CLI

Les plugins jouent un rôle crucial dans l'amélioration des sites WordPress. WP-CLI étend ses capacités à la gestion des plugins, rendant les tâches telles que l'installation, l'activation, la désactivation et les mises à jour incroyablement efficaces.

### Comment installer des plugins

Utilisez la commande `wp plugin install` pour installer des plugins de manière transparente depuis le dépôt WordPress. 

Par exemple, installons le plugin anti-spam "Akismet" :

```
wp plugin install akismet

```

### Comment activer et désactiver des plugins

Gérer le statut des plugins est assez facile avec WP-CLI. Activez ou désactivez des plugins en utilisant les commandes `wp plugin activate` et `wp plugin deactivate` respectivement. 

Pour activer le plugin "Akismet", tapez la commande suivante :

```
wp plugin activate akismet

```

### Comment mettre à jour des plugins

Maintenir les plugins à jour est vital pour la sécurité et les performances. La commande `wp plugin update` rend les mises à jour sans tracas. 

Pour mettre à jour tous les plugins installés, il suffit d'exécuter :

```
wp plugin update --all

```

### Comment lister les plugins installés

WP-CLI offre un aperçu des plugins installés avec la commande `wp plugin list`. Cela fournit un instantané rapide du statut, de la version et des mises à jour disponibles de chaque plugin :

```
wp plugin list

```

## Conclusion

WP-CLI est un atout inestimable dans le monde de la gestion WordPress. Son ensemble de commandes étendu vous aide à gérer les utilisateurs et les plugins – et bien plus – avec une facilité remarquable. Cela vous fait gagner du temps et minimise les interventions manuelles. 

En exploitant la puissance de WP-CLI, les administrateurs et les développeurs peuvent rationaliser les flux de travail, améliorer la sécurité et garantir que leurs sites WordPress fonctionnent de manière transparente.