---
title: Canal Conda - Qu'est-ce qu'un Canal dans Conda ?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-14T16:36:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-channel-in-conda
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/freestocks-11SgH7U6TmI-unsplash.jpg
tags:
- name: anaconda
  slug: anaconda
seo_title: Canal Conda - Qu'est-ce qu'un Canal dans Conda ?
seo_desc: 'When you install a package in Conda, it is downloaded and extracted from
  a remote directory using the directory''s URL. The directory where these packages
  are stored is known as a channel.

  In this article, you''ll learn what a channel is, how to use de...'
---

Lorsque vous installez un package dans Conda, il est téléchargé et extrait depuis un répertoire distant en utilisant l'URL du répertoire. Le répertoire où ces packages sont stockés est appelé un canal.

Dans cet article, vous apprendrez ce qu'est un canal, comment utiliser les canaux par défaut et comment ajouter de nouveaux canaux dans Conda.

## Qu'est-ce qu'un Canal dans Conda ?

Un canal est l'emplacement où les packages sont stockés à distance.

Lorsque vous installez Conda pour la première fois, il est livré avec un canal appelé `default`. Vous pouvez vérifier cela en utilisant la commande suivante :

```bash
conda config --show channels
```

Le canal `default` vous permet d'installer des packages actuellement disponibles dans son répertoire/stockage.

Pour installer un package en utilisant le canal `default`, vous utilisez la commande `conda install` suivie du nom du package. C'est-à-dire :

```bash
conda install package-name
```

Bien que de nombreux packages puissent être installés depuis le canal `default`, il est possible de rencontrer des packages qui ne sont pas accessibles depuis celui-ci.

Dans des cas comme celui-ci, vous obtiendrez généralement le message d'erreur "PackagesNotFoundError: The following channels are not available from current channels".

Vous verrez une solution à cette erreur dans la section suivante.

## Comment Installer un Package dans Conda en Utilisant un Nom de Canal

Dans cette section, vous apprendrez comment installer un package qui n'est pas disponible depuis le canal `default` dans Conda en spécifiant le nom du canal où ce package est stocké à distance.

Vous verrez également comment ajouter un canal à votre liste de canaux.

Voici un exemple utilisant Matplotlib :

```bash
conda install -c conda-forge matplotlib
```

Dans la commande ci-dessus :

* Le drapeau `-c` désigne le mot canal.
* `conda-forge` désigne le nom du canal depuis lequel Matplotlib a été installé.

Bien que nous ayons installé Matplotlib depuis `conda-forge`, `conda-forge` ne sera pas ajouté à notre liste de canaux.

Ainsi, si vous exécutez la commande `conda config --show channels`, vous ne verrez que le canal `default`.

Vous pouvez ajouter un canal à la liste des canaux en utilisant la commande `conda config --add channels channel-name`. C'est-à-dire :

```bash
conda config --add channels conda-forge
```

La commande ci-dessus ajoutera `conda-forge` à la liste des canaux Conda. Cela signifie que vous n'avez pas à spécifier le nom du canal si vous installez un package disponible depuis le canal `conda-forge`.

## Résumé

Dans cet article, nous avons parlé des canaux dans Conda. Ils sont utilisés pour accéder aux packages à distance.

Nous avons vu comment utiliser le canal par défaut de Conda pour installer des packages. Nous avons également vu comment utiliser et ajouter de nouveaux canaux qui ne sont pas intégrés à Conda.

Bon codage !