---
title: 'Git : Revenir à un Commit Précédent – Comment Revenir au Dernier Commit'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-10-19T22:55:44.000Z'
originalURL: https://freecodecamp.org/news/git-reverting-to-previous-commit-how-to-revert-to-last-commit
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/roman-synkevych-wX2L8L-fGeA-unsplash.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: 'Git : Revenir à un Commit Précédent – Comment Revenir au Dernier Commit'
seo_desc: 'Git is a great tool for version control. It also makes collaborating with
  others more efficient.

  In this article, you''ll learn how to revert to previous commits when tracking your
  project with Git.

  The two commands we''ll discuss in this article are g...'
---

[Git](https://www.freecodecamp.org/news/git-and-github-for-beginners/) est un excellent outil pour le contrôle de version. Il rend également la collaboration avec d'autres personnes plus efficace.

Dans cet article, vous apprendrez à revenir à des commits précédents lors du suivi de votre projet avec Git.

Les deux commandes que nous allons discuter dans cet article sont `git reset` et `git revert`. Ces commandes peuvent vous aider à annuler vos commits et à revenir à un commit précédent. 

Elles ne sont pas exactement identiques, donc nous allons rendre cet article un peu plus pratique en démontrant comment chaque commande fonctionne dans un projet.

Tout le monde peut suivre ce tutoriel car il ne sera pas spécifique à un langage — nous utiliserons un fichier texte (txt). 

## Comment Revenir à un Commit Précédent en Utilisant la Commande `git reset`

Dans cette section, nous allons passer par le processus de création d'un nouveau fichier et de réalisation de trois commits. Vous verrez ensuite comment vous pouvez revenir soit au dernier commit, soit à n'importe quel autre commit en utilisant l'ID du commit.

Pour commencer, j'ai créé un fichier appelé `tasks.txt`. Le fichier contient ceci :

```txt
1. coder.
2. Pratiquer.
3. Construire. 
```

Ensuite, nous allons initialiser, ajouter et commiter ce fichier : 

```bash
git init
git add tasks.txt
git commit -m "premier commit"
```

Nous avons fait le premier commit. 

Nous allons répéter le processus ci-dessus deux fois de plus, mais nous ajouterons une ligne de texte supplémentaire au fichier avant chaque commit. C'est-à-dire :

```txt
1. coder.
2. Pratiquer.
3. Construire. 
4. Rechercher. 
```

```bash
git add tasks.txt
git commit -m "deuxième commit"
```

Enfin, pour le troisième commit :

```txt
1. coder.
2. Pratiquer.
3. Construire. 
4. Rechercher. 
5. Écrire.
```

```bash
git add tasks.txt
git commit -m "troisième commit"
```

Maintenant, nous avons trois commits. Pour revenir à un commit précédent, vous devez d'abord obtenir l'ID du commit. Pour cela, exécutez la commande suivante :

```bash
git log --oneline
```

Dans mon terminal, j'ai ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/git-commit.PNG)
_git log --oneline_

Comme vous pouvez le voir ci-dessus, cette commande liste tous vos commits avec leurs ID. 

Pour revenir au deuxième commit, vous exécutez la commande `git reset` suivie de l'ID du commit. C'est-à-dire :

```bash
git reset 5914db0
```

Si vous avez suivi jusqu'à ce point, vous ne remarquerez aucune différence dans le fichier (vous verrez comment annuler à la fois le commit et les modifications apportées au fichier plus tard). 

Le fichier a toujours cet aspect :

```txt
1. coder.
2. Pratiquer.
3. Construire. 
4. Rechercher. 
5. Écrire.
```

Mais lorsque nous exécutons la commande `git log --oneline`, le troisième commit ne sera pas dans le journal des commits :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/second-commit.PNG)
_git log --oneline_

Nous sommes revenus avec succès à un commit précédent.

Si vous souhaitez annuler un commit et toutes les modifications apportées après ce commit, vous ajoutez le drapeau `--hard` à votre commande `git reset`. 

Testons cela en revenant au premier commit :

```bash
git reset 89f6c3d --hard
```

Voici à quoi ressemble le fichier texte maintenant :

```txt
1. coder.
2. Pratiquer.
3. Construire. 
```

Nous sommes revenus à l'état initial du fichier au moment du commit spécifié. Toutes les modifications apportées au fichier après ce commit ont été supprimées. Lorsque nous vérifions le journal des commits, nous n'aurons que le premier commit. 

Bien que cela semble être quelque chose de cool à faire, vous devez être prudent lorsque vous utilisez cette commande. Surtout lorsque vous travaillez avec une équipe.

Si vous annulez un commit et supprimez chaque modification de fichier qui est venue après, vous pourriez perdre des modifications importantes apportées à votre code par vous et d'autres coéquipiers. Cela changera également l'historique des commits de votre projet.

Heureusement pour nous, il existe un moyen de récupérer l'état d'un commit supprimé. Vous pouvez en apprendre plus à ce sujet [ici](https://www.freecodecamp.org/news/how-to-recover-a-deleted-file-in-git/). 

## Comment Revenir à un Commit Précédent en Utilisant la Commande `git revert`

J'ai déjà initialisé le projet et fait trois commits comme nous l'avons fait dans la dernière section. Voici à quoi ressemble le journal des commits :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/commit-log.PNG)
_git log --oneline_

Pour revenir au commit précédent, exécutez la commande `git revert` avec l'ID du commit actuel. 

Dans notre cas, nous allons utiliser l'ID du troisième commit :

```bash
git revert 882ad02
```

La commande ci-dessus annulera le commit actuel et rétablira le fichier à l'état du commit précédent. Lorsque vous vérifiez les journaux des commits, vous aurez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/revert-log.PNG)
_git log --oneline_

Contrairement à la commande `git reset`, la commande `git revert` crée un nouveau commit pour les modifications annulées. Le commit à partir duquel nous avons annulé ne sera pas supprimé. 

Ainsi, comme vous pouvez le voir, `git reset` et `git revert` ne sont pas identiques. 

`git reset` annulera les modifications jusqu'à l'état de l'ID de commit spécifié. Par exemple, revenir au deuxième ID de commit annulera les modifications et laissera l'état du fichier tel qu'il était au deuxième commit.

`git revert` annulera les modifications jusqu'à l'état avant l'ID de commit spécifié. Par exemple, revenir au deuxième ID de commit annulera les modifications et laissera l'état du fichier tel qu'il était au commit qui précède le deuxième commit — le premier commit.

Les explications ci-dessus peuvent sembler confuses. La meilleure façon de comprendre est de l'essayer vous-même.

## Quand Utiliser `git reset` et `git revert`

Vous devriez utiliser `git reset` lorsque vous travaillez sur un dépôt local avec des modifications non encore poussées à distance. Cela est dû au fait que l'exécution de cette commande après avoir tiré des modifications du dépôt distant modifiera l'historique des commits du projet, entraînant des conflits de fusion pour tous ceux qui travaillent sur le projet.

`git reset` est une bonne option lorsque vous réalisez que les modifications apportées à une branche locale particulière devraient être ailleurs. Vous pouvez réinitialiser et passer à la branche souhaitée sans perdre vos modifications de fichier.

`git revert` est une bonne option pour annuler les modifications poussées vers un dépôt distant. Puisque cette commande crée un nouveau commit, vous pouvez vous débarrasser de vos erreurs en toute sécurité sans réorganiser l'historique des commits pour les autres.

## Résumé

Dans cet article, nous avons parlé de revenir à des commits précédents dans Git. 

Nous avons parlé de deux commandes principales qui ont montré comment annuler les modifications Git — les commandes `git reset` et `git revert`.

Nous avons également vu comment les deux commandes fonctionnent en utilisant des exemples pratiques.

Bon codage !