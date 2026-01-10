---
title: Supprimer un environnement Conda – Comment supprimer un env
date: '2023-04-07T05:11:54.000Z'
author: Ihechikara Abba
authorURL: https://www.freecodecamp.org/news/author/Ihechikara/
originalURL: https://freecodecamp.org/news/how-to-delete-an-environment-in-conda
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/lewis-kang-ethe-ngugi-f5pTwLHCsAg-unsplash.jpg
tags:
- name: anaconda
  slug: anaconda
- name: Python
  slug: python
seo_desc: "Conda is an open-source package management and environment management system\
  \ that can be used to create different, isolated coding environments. \nWith Conda,\
  \ you can create separate environments for specific projects. You can have one environment\
  \ for..."
---


Conda est un système de gestion de paquets et d'environnements open-source qui peut être utilisé pour créer différents environnements de codage isolés.

<!-- more -->

Avec Conda, vous pouvez créer des environnements séparés pour des projets spécifiques. Vous pouvez avoir un environnement pour le machine learning et un autre pour l'analyse de données.

Chaque environnement peut avoir ses propres paquets. Les paquets installés dans un environnement ne sont pas accessibles dans un autre environnement.

Dans cet article, vous apprendrez comment supprimer un environnement dans Conda en utilisant les commandes Conda intégrées.

## Comment supprimer un environnement dans Conda

Vous pouvez obtenir une liste des environnements Conda existants en utilisant la commande ci-dessous :

```
conda env list
```

Avant de supprimer un environnement dans Conda, vous devez d'abord le désactiver. Vous pouvez le faire en utilisant cette commande :

```
conda deactivate
```

Une fois l'environnement désactivé, vous serez redirigé vers l'environnement `base`.

Pour supprimer un environnement, exécutez la commande ci-dessous :

```
conda remove --name ENV_NAME --all
```

`ENV_NAME` désigne le nom de l'environnement à retirer/supprimer. Assurez-vous de désactiver un environnement avant de le supprimer en exécutant la commande `conda deactivate`.

Le drapeau `--all` supprime tous les paquets installés dans cet environnement.

Voici un résumé des étapes à suivre pour supprimer un environnement dans Conda :

-   Désactivez l'environnement en utilisant la commande `conda deactivate`.
-   Supprimez l'environnement en utilisant la commande `conda remove --name ENV_NAME --all`.

## Résumé

Dans cet article, nous avons parlé de Conda. Un système de gestion de paquets et d'environnements utilisé pour installer et gérer des environnements de codage séparés et leurs paquets.

Nous avons vu différentes commandes pouvant être utilisées pour désactiver et supprimer un environnement dans Conda.

Bon codage !