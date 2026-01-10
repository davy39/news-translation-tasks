---
title: Git Checkout – Comment récupérer un fichier d'une autre branche
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-06T19:36:25.000Z'
originalURL: https://freecodecamp.org/news/git-checkout-file-from-another-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Checkout – Comment récupérer un fichier d'une autre branche
seo_desc: 'By Tim Mouskhelichvili

  While you''re working on a repository in Git, you might need to checkout a specific
  file from another branch.

  Luckily, Git offers many possible ways to do this task quickly. One of the easiest
  solutions is to use the git checkou...'
---

Par Tim Mouskhelichvili

Lorsque vous travaillez sur un dépôt dans Git, vous pourriez avoir besoin de récupérer un fichier spécifique d'une autre branche.

Heureusement, Git offre de nombreuses façons possibles d'effectuer cette tâche rapidement. L'une des solutions les plus simples est d'utiliser la commande `git checkout` avec le fichier spécifié comme argument.

Dans cet article, nous allons analyser différentes solutions à ce problème et passer en revue le processus que vous devrez suivre pour chacune.

C'est parti 😊.

## Exemple de cas d'utilisation de Git Checkout

Vous travaillez sur une branche appelée `feature/A` contenant un fichier nommé `utils.js`.

Vous avez une autre branche appelée `feature/B` avec un fichier `utils.js` mis à jour.

Vous souhaitez récupérer ce fichier et l'importer de la branche appelée `feature/B` vers la branche appelée `feature/A`.

Voici trois solutions possibles pour cette tâche.

### Solution 1 : Utiliser la commande `git checkout`

La commande `git checkout` offre un moyen simple d'obtenir un fichier ou un dossier d'une autre branche.

Voici la syntaxe pour récupérer un fichier d'une autre branche :

```bash
git checkout <nom-autre-branche> -- chemin/vers/votre/dossier
```

Voici le processus à suivre :

1. Passez à la branche où vous souhaitez copier le fichier.

```bash
git checkout feature/A
```

2. Une fois sur la bonne branche, copiez le fichier.

```bash
git checkout feature/B -- utils.js
```

3. Utilisez la commande [git status](https://timmousk.com/blog/git-status/) pour vous assurer que le fichier a été copié.

4. Validez et poussez vers un dépôt distant.

Lorsque vous utilisez la commande checkout, vous pouvez également obtenir :

* Un dossier d'une autre branche.
* Plusieurs fichiers en spécifiant chacun d'eux.

Notez également que vous pouvez obtenir un fichier/dossier depuis la stash.

### Solution 2 : Utiliser la commande `git restore`

Une autre option est d'utiliser la commande `git switch` avec la commande `git restore`.

Si vous n'avez jamais entendu parler de ces deux commandes, ce n'est pas grave. Elles sont relativement nouvelles. Git les a introduites dans la version 2.23 en 2019.

Le but de ces deux commandes est de diviser les responsabilités de la commande `git checkout` pour la simplifier pour les utilisateurs.

La commande `git restore` restaure l'arborescence de travail.

La commande `git switch` change de branche.

Voici le processus à suivre pour obtenir un fichier d'une autre branche :

1. Passez à la branche où vous souhaitez récupérer le fichier.

```bash
git switch feature/A
```

2. Obtenez le fichier de l'autre branche.

```bash
git restore --source feature/B -- utils.js
```

3. Validez et poussez les changements.

### Solution 3 : Utiliser la commande `git show`

Enfin, nous pouvons utiliser la commande `git show`.

Voici le processus à suivre :

1. Passez à la branche de travail.

```bash
git switch feature/A
```

2. Obtenez le fichier de l'autre branche.

```bash
git show feature/B:path/utils.js > path/utils.js
```

3. Validez et poussez les changements.

**Note :** Vous devez spécifier le chemin relatif depuis la racine de votre répertoire cette fois-ci.

## Réflexions finales

Comme vous pouvez le voir, obtenir un fichier d'une autre branche n'est pas une science exacte.

Lorsque j'ai besoin de le faire dans ma vie quotidienne, j'utilise généralement la commande `git checkout`.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/6ii6ur.jpg)

Veuillez visiter [mon blog](https://timmousk.com/) si vous êtes intéressé à découvrir plus sur Git ou les technologies de développement web comme TypeScript.

Merci d'avoir lu cet article.