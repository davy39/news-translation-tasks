---
title: Conda Supprimer un Package - Comment Supprimer Matplotlib dans Anaconda
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-12T12:21:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-package-in-anaconda
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/joshua-woroniecki-lzh3hPtJz9c-unsplash.jpg
tags:
- name: anaconda
  slug: anaconda
- name: Matplotlib
  slug: matplotlib
seo_title: Conda Supprimer un Package - Comment Supprimer Matplotlib dans Anaconda
seo_desc: "You can use Conda to create and manage different environments and their\
  \ packages. It is mostly used for data science and machine learning projects. \n\
  In this article, you'll learn how to remove an environment's package using in built\
  \ Conda commands. \n..."
---

Vous pouvez utiliser Conda pour créer et gérer différents environnements et leurs packages. Il est principalement utilisé pour des projets de science des données et d'apprentissage automatique. 

Dans cet article, vous apprendrez comment supprimer un package d'un environnement en utilisant les commandes intégrées de Conda. 

Vous apprendrez les points suivants : 

* Comment créer un environnement. 
* Comment installer des packages dans un environnement. 
* Comment supprimer un package d'un environnement. 

Commençons !

## Comment Créer un Environnement dans Conda

Vous pouvez utiliser la commande `conda create package-name` pour créer un nouvel environnement dans Conda. 

Voici un exemple :

```bash
conda create -n package-tutorial
```

La commande ci-dessus crée un environnement appelé `package-tutorial`.

Vous pouvez activer ou basculer vers l'environnement `package-tutorial` en utilisant la commande `conda activate environment-name`. C'est-à-dire :

```bash
conda activate package-tutorial
```

## Comment Installer des Packages dans un Environnement Conda

Dans la dernière section, nous avons créé et activé un environnement appelé `package-tutorial`. 

Dans cette section, vous verrez comment installer un package dans cet environnement. Installons Matplotlib. 

Vous pouvez installer un package en utilisant la commande `conda install package-name`.

Voici l'une des commandes pour installer Matplotlib dans Conda : 

```bash
conda install -c conda-forge matplotlib
```

L'installation peut prendre un certain temps pour télécharger et extraire le package. Vous pouvez vérifier les packages qui existent dans votre environnement en utilisant la commande `conda list`. 

Une fois l'installation terminée, utilisez la commande `conda list` pour vérifier que le package a été installé dans votre environnement. 

## Comment Supprimer un Package dans Conda

Vous pouvez supprimer un package dans l'environnement actuel en exécutant la commande `conda remove package-name`. 

Dans notre cas, nous voulons supprimer Matplotlib de l'environnement actuel (`package-tutorial` environment) :

```bash
conda remove matplotlib
```

La commande ci-dessus supprime Matplotlib de l'environnement actuel. Lorsque vous exécutez la commande `conda list`, Matplotlib ne sera plus listé comme un package.

## Résumé

Dans cet article, nous avons parlé des packages dans Conda. Ils peuvent être installés dans des environnements Conda. 

Nous avons vu comment créer et activer un environnement Conda. Nous avons également vu comment installer et supprimer des packages dans Conda. 

Bon codage !