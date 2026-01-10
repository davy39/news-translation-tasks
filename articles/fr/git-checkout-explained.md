---
title: 'Git Checkout Expliqué : Comment Basculer, Changer ou Passer à une Branche
  dans Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-31T21:27:00.000Z'
originalURL: https://freecodecamp.org/news/git-checkout-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5b740569d1a4ca3cac.jpg
tags:
- name: Git
  slug: git
seo_title: 'Git Checkout Expliqué : Comment Basculer, Changer ou Passer à une Branche
  dans Git'
seo_desc: 'The git checkout command switches between branches or restores working
  tree files. There are a number of different options for this command that won’t
  be covered here, but you can take a look at all of them in the Git documentation.

  Checkout a specif...'
---

La commande `git checkout` permet de basculer entre les branches ou de restaurer les fichiers de l'arborescence de travail. Il existe un certain nombre d'options différentes pour cette commande qui ne seront pas couvertes ici, mais vous pouvez consulter toutes les options dans la [documentation Git](https://git-scm.com/docs/git-checkout).

### **Basculer vers un commit spécifique**

Pour basculer vers un commit spécifique, exécutez la commande :

```shell
git checkout specific-commit-id
```

Nous pouvons obtenir l'ID de commit spécifique en exécutant :

```shell
git log
```

### **Basculer vers une branche existante**

Pour basculer vers une branche existante, exécutez la commande :

```shell
git checkout NOM-DE-LA-BRANCHE
```

Généralement, Git ne vous permettra pas de basculer vers une autre branche à moins que votre répertoire de travail soit propre, car vous perdriez toutes les modifications du répertoire de travail qui ne sont pas validées. Vous avez trois options pour gérer vos modifications : 1) les supprimer, 2) [les valider](https://guide.freecodecamp.org/git/git-commit/), ou 3) [les stocker temporairement](https://guide.freecodecamp.org/git/git-stash/).

### **Créer et basculer vers une nouvelle branche**

Pour créer et basculer vers une nouvelle branche avec une seule commande, vous pouvez utiliser :

```shell
git checkout -b NOUVEAU-NOM-DE-BRANCHE
```

Cela vous basculera automatiquement vers la nouvelle branche.

### **Créer une nouvelle branche ou réinitialiser une branche à un point de départ**

La commande suivante est similaire à la création d'une nouvelle branche, mais utilise le drapeau `-B` (notez la majuscule B) et un paramètre `POINT-DE-DEPART` optionnel :

```shell
git checkout -B NOM-DE-LA-BRANCHE POINT-DE-DEPART
```

Si la branche `NOM-DE-LA-BRANCHE` n'existe pas, Git la créera et la démarrera à `POINT-DE-DEPART`. Si la branche `NOM-DE-LA-BRANCHE` existe déjà, alors Git réinitialise la branche à `POINT-DE-DEPART`. Cela équivaut à exécuter `git branch` avec `-f`.

### **Forcer un basculement**

Vous pouvez passer l'option `-f` ou `--force` avec la commande `git checkout` pour forcer Git à changer de branche, même si vous avez des modifications non indexées (en d'autres termes, l'index de l'arborescence de travail diffère de `HEAD`). En gros, cela peut être utilisé pour jeter les modifications locales.

Lorsque vous exécutez la commande suivante, Git ignorera les entrées non fusionnées :

```shell
git checkout -f NOM-DE-LA-BRANCHE

# Alternative
git checkout --force NOM-DE-LA-BRANCHE
```

### **Annuler les modifications dans votre répertoire de travail**

Vous pouvez utiliser la commande `git checkout` pour annuler les modifications que vous avez apportées à un fichier dans votre répertoire de travail. Cela rétablira le fichier à la version dans `HEAD` :

```shell
git checkout -- NOM-DU-FICHIER
```