---
title: La commande Git Commit expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T21:54:00.000Z'
originalURL: https://freecodecamp.org/news/git-commit-command-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e64740569d1a4ca3cdf.jpg
tags:
- name: Git
  slug: git
seo_title: La commande Git Commit expliquée
seo_desc: 'The git commit command will save all staged changes, along with a brief
  description from the user, in a “commit” to the local repository.

  Commits are at the heart of Git usage. You can think of a commit as a snapshot of
  your project, where a new vers...'
---

La commande `git commit` enregistrera toutes les modifications indexées, ainsi qu'une brève description de l'utilisateur, dans un "commit" vers le dépôt local.

Les commits sont au cœur de l'utilisation de Git. Vous pouvez considérer un commit comme un instantané de votre projet, où une nouvelle version de ce projet est créée dans le dépôt actuel. Deux caractéristiques importantes des commits sont :

* vous pouvez rappeler les modifications validées à une date ultérieure, ou revenir à cette version du projet ([voir Git checkout](https://guide.freecodecamp.org/git/git-checkout))
* si plusieurs commits modifient différentes parties du projet, ils ne s'écraseront pas mutuellement même si les auteurs des commits n'étaient pas au courant les uns des autres. C'est l'un des avantages de l'utilisation de Git par rapport à un outil comme Dropbox ou Google Drive.

## Options

Il existe un certain nombre d'options que vous pouvez inclure avec `git commit`. Cependant, ce guide ne couvrira que les deux options les plus courantes. Pour une liste exhaustive des options, veuillez consulter la [documentation Git](https://git-scm.com/docs/git-commit).

### L'option -m

L'option la plus courante utilisée avec `git commit` est l'option `-m`. Le `-m` signifie message. Lors de l'appel de `git commit`, il est obligatoire d'inclure un message. Le message doit être une brève description des modifications en cours de validation. Le message doit être à la fin de la commande et il doit être entouré de guillemets `" "`.

Un exemple de la façon d'utiliser l'option `-m` :

```shell
git commit -m "Mon message"
```

La sortie dans votre terminal devrait ressembler à ceci :

```shell
[master 13vc6b2] Mon message
 1 fichier modifié, 1 insertion(+)
```

**NOTE :** Si le `-m` n'est pas inclus avec la commande `git commit`, vous serez invité à ajouter un message dans votre éditeur de texte par défaut - voir « Utiliser des messages de commit détaillés » ci-dessous.

### L'option -a

Une autre option populaire est l'option `-a`. Le `-a` signifie tout. Cette option indexe automatiquement tous les fichiers modifiés à valider. Si de nouveaux fichiers sont ajoutés, l'option `-a` n'indexera pas ces nouveaux fichiers. Seuls les fichiers que le dépôt Git connaît seront validés.

Par exemple :

Supposons que vous avez un fichier `README.md` qui a déjà été validé dans votre dépôt. Si vous apportez des modifications à ce fichier, vous pouvez utiliser l'option `-a` dans votre commande de commit pour indexer et ajouter les modifications à votre dépôt. Cependant, que se passe-t-il si vous avez également ajouté un nouveau fichier appelé `index.html` ? L'option `-a` n'indexera pas le `index.html` car il n'existe pas actuellement dans le dépôt. Lorsque de nouveaux fichiers ont été ajoutés, la commande `git add` doit être invoquée afin d'indexer les fichiers avant qu'ils ne puissent être validés dans le dépôt.

Un exemple de la façon d'utiliser l'option `-a` :

```shell
git commit -am "Mes nouvelles modifications"
```

La sortie dans votre terminal devrait ressembler à ceci :

```shell
[master 22gc8v1] Mon nouveau message
 1 fichier modifié, 1 insertion(+)
```

## Utiliser des messages de commit détaillés

Bien que `git commit -m "message de commit"` fonctionne très bien, il peut être utile de fournir des informations plus détaillées et systématiques.

Si vous validez sans utiliser l'option `-m`, git ouvrira votre éditeur de texte par défaut avec un nouveau fichier, qui inclura une liste commentée de tous les fichiers/modifications qui sont indexés dans le commit. Vous écrivez ensuite votre message de commit détaillé (la première ligne sera traitée comme la ligne d'objet) et le commit sera effectué lorsque vous enregistrerez/fermerez le fichier.

Gardez à l'esprit :

* Gardez la longueur des lignes de votre message de commit inférieure à 72 caractères comme pratique standard
* Il est parfaitement acceptable - et même recommandé - d'écrire des messages de commit multilignes
* Vous pouvez également faire référence à d'autres problèmes ou demandes de tirage dans votre message de commit. GitHub attribue un numéro de référence à toutes les demandes de tirage et problèmes, donc par exemple si vous souhaitez faire référence à la demande de tirage #788, faites-le simplement dans la ligne d'objet ou dans le corps du texte, selon ce qui est approprié

### L'option --amend

L'option `--amend` vous permet de modifier votre dernier commit. Supposons que vous venez de valider et que vous avez fait une erreur dans votre message de journal de commit. Vous pouvez modifier facilement le commit le plus récent en utilisant la commande :

```shell
git commit --amend -m "un message de commit mis à jour"
```

Si vous oubliez d'inclure un fichier dans le commit :

```shell
git add NOM-DU-FICHIER-OUBLIÉ
git commit --amend -m "un message de commit mis à jour"

# Si vous n'avez pas besoin de changer le message de commit, utilisez l'option --no-edit
git add NOM-DU-FICHIER-OUBLIÉ
git commit --amend --no-edit
```

Les commits prématurés arrivent tout le temps dans le cadre de votre développement quotidien. Il est facile d'oublier d'indexer un fichier ou comment formater correctement votre message de commit. Le drapeau `--amend` est un moyen pratique de corriger ces petites erreurs. Cette commande remplacera l'ancien message de commit par celui mis à jour spécifié dans la commande.

Les commits modifiés sont en fait des commits entièrement nouveaux et le commit précédent ne sera plus sur votre branche actuelle. Lorsque vous travaillez avec d'autres personnes, vous devriez essayer d'éviter de modifier les commits si le dernier commit est déjà poussé dans le dépôt.

Avec `--amend`, l'un des drapeaux utiles que vous pourriez utiliser est `--author` qui vous permet de changer l'auteur du dernier commit que vous avez fait. Imaginez une situation où vous n'avez pas correctement configuré votre nom ou votre email dans les configurations git mais que vous avez déjà fait un commit. Avec le drapeau `--author`, vous pouvez simplement les changer sans réinitialiser le dernier commit.

```text
git commit --amend --author="John Doe <johndoe@email.com>"
```

### L'option -v ou --verbose

L'option `-v` ou `--verbose` est utilisée sans l'option `-m`. L'option `-v` peut être utile lorsque vous souhaitez modifier un message de commit Git dans votre éditeur par défaut tout en pouvant voir les modifications que vous avez apportées pour le commit. La commande ouvre votre éditeur de texte par défaut avec un modèle de message de commit ainsi qu'une copie des modifications que vous avez apportées pour ce commit. Les modifications, ou diff, ne seront pas incluses dans le message de commit, mais elles fournissent un bon moyen de référencer vos modifications lorsque vous les décrivez dans votre message de commit.

## Comment fusionner plusieurs commits en un seul

C'est une fonctionnalité géniale de `rebase` qui peut être utilisée en mode `interactif`. Pour fusionner les _n_ derniers commits en un seul, exécutez la commande suivante :

```text
git rebase -i HEAD~n
```

Cela ouvrira un éditeur de texte avec quelque chose de similaire à ce qui suit :

```text
pick commit_1
pick commit_2
pick commit_3
...
pick commit_n
# Bunch of comments
```

Laissez le premier commit tel quel, et changez le reste des `pick` en `squash`. Enregistrez et quittez l'éditeur.

Ainsi, si vous souhaitez fusionner les trois derniers commits, vous exécuterez d'abord `git rebase -i HEAD~3` puis vous voudrez modifier vos commits pour qu'ils ressemblent à ceci :

```text
pick dd661ba Commit 1
squash 71f5fee Commit 2
squash f4b4bf1 Commit 3
```

Si vous avez déjà poussé vers un dépôt distant avant de fusionner vos commits, vous devrez pousser à nouveau vers le dépôt distant, avec le drapeau `-f`, sinon git vous lancera une erreur.

Il est fortement suggéré de lire les informations dans le fichier ouvert car il y a beaucoup de choses que vous pouvez faire.

### **Plus d'informations :**

* Documentation Git : [commit](https://git-scm.com/docs/git-commit)