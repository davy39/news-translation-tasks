---
title: 'Linux : Comment ajouter des utilisateurs et créer des utilisateurs avec useradd'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T02:11:12.000Z'
originalURL: https://freecodecamp.org/news/linux-how-to-add-users-and-create-users-with-useradd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c8c740569d1a4ca32d2.jpg
tags:
- name: Linux
  slug: linux
seo_title: 'Linux : Comment ajouter des utilisateurs et créer des utilisateurs avec
  useradd'
seo_desc: "By Jackson Bates\nIf more than one person is using your Linux machine at\
  \ home, or you are managing a server that provides access to multiple users, the\
  \ useradd command is essential for creating users. \nAlso, many of the services\
  \ you use as a developer..."
---

Par Jackson Bates

Si plus d'une personne utilise votre machine Linux à la maison, ou si vous gérez un serveur qui fournit un accès à plusieurs utilisateurs, la commande `useradd` est essentielle pour créer des utilisateurs. 

De plus, de nombreux services que vous utilisez en tant que développeur peuvent nécessiter leurs propres comptes d'utilisateur pour fonctionner. Ainsi, même en tant que développeur solo sur votre propre machine, vous pourriez vous retrouver à utiliser ces commandes lorsque vous installez MySQL ou quelque chose de similaire.

Vous pouvez obtenir un aperçu complet des différentes options disponibles en consultant la page man de l'utilitaire : `man useradd`

Mais si cela semble écrasant, voici une explication de certaines des options courantes que vous pourriez utiliser lors de la création d'un utilisateur.

## Créer un utilisateur

Le format simple de cette commande est `useradd [options] NOM_D_UTILISATEUR`.

Par exemple `useradd test` (en tant qu'utilisateur root - préfixez avec `sudo` si vous n'êtes pas connecté en tant que root).

Cela créera un utilisateur appelé test, mais il s'agit d'une opération limitée et ne créera pas d'autres éléments utiles comme leur répertoire personnel ou leur mot de passe !

## Ajouter un mot de passe

Vous ajoutez ensuite un mot de passe pour l'utilisateur test en utilisant la commande `passwd` : `passwd test`. Cela vous invitera à entrer un mot de passe pour l'utilisateur.

_Il existe une option pour ajouter un mot de passe chiffré via l'option `-p` sur `useradd`, mais cela n'est pas recommandé pour des raisons de sécurité._ 

Notez que l'option `-p` ne vous permet pas de saisir un mot de passe en clair, elle s'attend à ce que vous le chiffriez d'abord. Cela est intentionnellement difficile, car vous ne devriez **pas** le faire ! Utilisez simplement la commande `passwd`.

## Autres options courantes

### Répertoires personnels

Pour créer un utilisateur avec le répertoire personnel par défaut, utilisez l'option suivante :

`useradd -m test`

Cet utilisateur dispose maintenant d'un répertoire /home/test.

Pour changer le répertoire personnel, vous pouvez passer une option supplémentaire pour le modifier, par exemple :

`useradd -m -d /alternate test`

### Shell

Par défaut, vos utilisateurs créés auront probablement le shell de connexion par défaut bin/bash ou bin/sh, qui sera défini dans `/etc/default/useradd`.

Vous pouvez remplacer ce défaut avec l'option `-s` :

`useradd -s usr/bin/zsh test`

## Mettre le tout ensemble

Pour construire la commande complète, vous placez les options les unes après les autres - l'ordre n'a pas d'importance - et vous terminez par le nom d'utilisateur que vous souhaitez créer.

Ainsi, la création d'un utilisateur avec un répertoire personnel et un shell personnalisé ressemblerait à ceci :

`useradd -m -s /usr/bin/zsh user`

Et ensuite, vous ajouteriez un mot de passe pour l'utilisateur : `passwd user`

## Lisez le manuel

Maintenant que vous avez vu les bases de ce que cet outil peut faire, espérons que la page man est un peu plus navigable.

`man useradd` vous montrera comment ajouter des éléments comme des dates d'expiration sur le compte, attribuer des groupes, et ainsi de suite.