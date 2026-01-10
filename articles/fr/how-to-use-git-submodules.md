---
title: Comment utiliser les sous-modules Git – Expliqué avec des exemples
subtitle: ''
author: Jima Victor
co_authors: []
series: null
date: '2024-05-07T17:40:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-submodules
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/git-submodules
seo_title: Comment utiliser les sous-modules Git – Expliqué avec des exemples
---

cover-image.png
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'Git est sans aucun doute un outil très important pour les développeurs. Il nous aide à collaborer de manière transparente, à suivre les changements efficacement et à maintenir l'intégrité des projets dans des environnements distribués.

Mais à mesure que les projets grandissent en complexité et en ampleur, leurs dépendances aussi. Nous avons donc besoin d'un mécanisme pour gérer correctement ces dépendances à mesure qu'elles grandissent. Ce mécanisme est connu sous le nom de sous-modules Git.

Dans cet article, nous allons plonger dans le monde des sous-modules Git afin de mieux comprendre comment ils fonctionnent.

## Prérequis

* Une compréhension de base de Git et GitHub.
* Git installé.

## Qu'est-ce qu'un sous-module Git ?

Un sous-module Git fait référence à un dépôt Git qui existe au sein d'un autre dépôt Git.

Vous pouvez le considérer comme un dépôt enfant ou un sous-ensemble d'un dépôt principal.

Les sous-modules Git fournissent une manière structurée d'inclure des dépôts externes dans un projet tout en conservant les avantages d'avoir un dépôt maintenu séparément.

## Différence entre un dépôt et un sous-module

Un sous-module est également un dépôt. La seule différence entre un sous-module et un dépôt est le fait qu'un sous-module ne peut exister que comme un dépôt Git à l'intérieur d'un autre dépôt. Si un sous-module existe en dehors d'un dépôt, il ne peut plus être appelé un sous-module. Il ne peut être référencé que comme un dépôt.

Tous les sous-modules sont des dépôts, mais tous les dépôts ne sont pas des sous-modules.

## Comment ajouter un sous-module Git

Pour ajouter un sous-module Git, assurez-vous d'abord d'être dans un dépôt Git et d'avoir l'URL du dépôt distant que vous souhaitez ajouter comme sous-module.

Ensuite, utilisez la commande `git submodule add`, suivie de l'URL du dépôt que vous souhaitez ajouter.

```console
git submodule add <submodule_url>
```

La commande ci-dessus ajoutera le sous-module au niveau racine de votre dépôt principal par défaut.

Pour spécifier un répertoire où vous souhaitez que le sous-module soit situé dans votre dépôt principal, ajoutez l'argument de chemin à la commande.

```console
git submodule add <submodule_url> <path>
```

Où :

* `<submodule_url>` est l'URL du dépôt Git que vous souhaitez ajouter comme sous-module.
* `<path>` est le chemin où vous souhaitez que le sous-module soit ajouté dans votre dépôt.

## Le fichier .gitmodules

Lors de la création d'un nouveau sous-module git avec la commande `git submodule add`, un nouveau fichier sera ajouté au niveau racine de votre dépôt principal. Ce fichier est le fichier **.gitmodules**.

**.gitmodules** est un fichier de configuration utilisé par Git pour stocker des informations sur les sous-modules présents dans un dépôt. Il contient des détails sur chaque sous-module, tels que leurs URL et chemins.

Ce fichier aide à garantir que lorsque vous clonez ou mettez à jour un dépôt avec des sous-modules, Git sait où récupérer le contenu des sous-modules et quelles versions des sous-modules utiliser.

Voici un exemple de ce à quoi ressemble le fichier **.gitmodules** :

```console
[submodule "example"]
    path = example
    url = https://github.com/example/example.git
```

Si vous avez plus d'un sous-module dans votre projet, voici à quoi ressemblera votre fichier **.gitmodules** :

```console
[submodule "submodule1"]
    path = submodule1
    url = https://github.com/example/submodule1.git

[submodule "submodule2"]
    path = submodule2
    url = https://github.com/example/submodule2.git

[submodule "submodule3"]
    path = submodule3
    url = https://github.com/example/submodule3.git
```

## Comment ne pas ajouter un sous-module

Parfois, vous pourriez être tenté d'utiliser la commande `git clone` pour ajouter un dépôt comme dépendance dans votre dépôt. Vous devriez résister à cette tentation !

Si vous utilisez la commande `git clone`, vous obtiendrez le message suivant sur votre terminal Git Bash : "Vous avez ajouté un autre dépôt git à l'intérieur de votre dépôt actuel. Les clones du dépôt externe ne contiendront pas le contenu du dépôt intégré et ne sauront pas comment l'obtenir..."

![Image](https://www.freecodecamp.org/news/content/images/2024/05/git_hint.PNG)
_commande git clone lors de la tentative d'ajout d'un sous-module_

J'ai obtenu ce message en essayant d'ajouter un sous-module au répertoire `theme/anake` en utilisant la commande `git clone`.

Il y a principalement deux raisons pour lesquelles vous ne devriez pas utiliser cette commande :

1. Le répertoire du sous-module sera vide lorsque vous pousserez votre code vers votre dépôt distant.
2. Les clones du dépôt externe (dépôt principal) ne contiendront pas le contenu du dépôt intégré (sous-module) et ne sauront pas comment l'obtenir, comme indiqué par Git dans le message ci-dessus.

Et les raisons ci-dessus sont des problèmes qui découlent de l'absence du fichier **.gitmodules** (qui est automatiquement ajouté lorsque vous utilisez la commande `git submodule add`) au niveau racine de votre dépôt principal.

L'ajout manuel du fichier **.gitmodules** au niveau racine de votre dépôt principal résoudrait les problèmes ci-dessus. Cependant, la création d'un sous-module en utilisant la commande `git submodule add` les empêcherait.

## Comment cloner un dépôt avec un sous-module Git

Il y a deux commandes que vous devez retenir chaque fois que vous souhaitez cloner des dépôts contenant des sous-modules. Ces commandes sont :

`git submodule init` : Cette commande initialise les sous-modules définis dans le dépôt. Lorsque vous clonez un dépôt qui contient des sous-modules, Git ne récupère pas automatiquement le contenu des sous-modules. Vous devez exécuter `git submodule init` pour les initialiser d'abord.

Git lit le fichier **.gitmodules** dans le dépôt pour configurer les sous-modules et se prépare à récupérer le contenu des sous-modules lorsque vous exécutez `git submodule update`.

`git submodule update` : Cette commande récupère les derniers commits des dépôts de sous-modules.

S'il y a de nouveaux commits dans les dépôts de sous-modules, vous devrez peut-être exécuter `git submodule update` pour mettre à jour les sous-modules à l'état le plus récent.

Pour cloner des dépôts contenant des sous-modules, la première chose à faire est d'exécuter la commande `git clone` pour ce dépôt.

```console
git clone <repository_URL>
```

Après cela, exécutez la commande `git submodule init` au niveau racine du dépôt principal.

```console
git submodule init
```

Ensuite, enfin, exécutez la commande `git submodule update`.

```console
git submodule update
```

## Conclusion

Les sous-modules Git servent de mécanisme pour gérer efficacement les dépendances au sein d'un projet. Ils permettent l'incorporation transparente de dépôts externes dans un projet principal, en maintenant des frontières claires entre les composants tout en facilitant la collaboration.

En utilisant des sous-modules, les développeurs peuvent rationaliser les flux de travail, maintenir l'intégrité des projets et faciliter une collaboration efficace, contribuant ainsi à des processus de développement plus robustes et évolutifs.