---
title: Comment faire votre première pull request sur GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T15:53:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Untitled-design.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment faire votre première pull request sur GitHub
seo_desc: 'By Thanoshan MV

  What is forking?

  When we love someone’s repository and would like to have it in our GitHub account,
  we fork it so that we can work with it separately.

  When we fork a repository, we get an instance of that entire repository with its
  wh...'
---

Par Thanoshan MV

## Qu'est-ce que le forking ?

Lorsque nous aimons le dépôt de quelqu'un et que nous souhaitons l'avoir dans notre compte GitHub, nous le forkons afin de pouvoir travailler avec séparément.

Lorsque nous forkons un dépôt, nous obtenons une instance de ce dépôt entier avec tout son historique. Après avoir forké, nous pouvons faire tout ce que nous voulons sans affecter la version originale.

## Qu'est-ce qu'une pull request ?

Les pull requests sont la manière dont nous contribuons aux projets de groupe ou aux projets open source.

Par exemple, un utilisateur Harry fork le dépôt de ThanoshanMV et apporte des modifications à ce dépôt. Maintenant, Harry peut faire une pull request à ThanoshanMV, mais c'est à ThanoshanMV d'accepter ou de la décliner. C'est comme dire : « ThanoshanMV, pourriez-vous tirer mes changements ? »

## Ce que signifie contribuer

Non seulement nous pouvons contribuer à un projet open source avec du code, mais nous pouvons également contribuer de nombreuses autres manières. Certaines de ces manières sont décrites ci-dessous.

Comme le guide de démarrage hacktitude de la société IT [99xtechnology](https://www.99xtechnology.com/) le dit, nous pouvons contribuer à un projet open source de les manières suivantes :

1. Conception : Vous pouvez construire les mises en page d'un projet pour améliorer son utilisabilité, améliorer la navigation et le menu du projet sur la base de programmes de recherche utilisateur, créer des œuvres d'art pour les logos ou les t-shirts, et fournir des guides de style pour le projet.
2. Rédaction : Vous pouvez écrire et améliorer la documentation du projet ou traduire la documentation, lancer une newsletter pour le projet ou écrire des tutoriels pour le projet et curater les points forts de la liste de diffusion, ou curater un dossier d'exemples montrant comment les projets sont utilisés.
3. Organisation : Vous pouvez lier les problèmes en double, suggérer de nouvelles étiquettes de problème, suggérer de fermer les anciens problèmes ouverts et poser des questions sur les problèmes récemment ouverts pour faire avancer la discussion.
4. Aider les autres : Répondre aux questions sur les problèmes ouverts, examiner le code sur les soumissions d'autres personnes et proposer de mentoriser un autre contributeur.
5. Codage : Aider à résoudre tout problème ouvert, demander si vous pouvez fournir de nouvelles fonctionnalités et améliorer les outils et les tests.

## Faisons notre première pull request !

Si vous n'êtes pas très familier avec Git & GitHub, veuillez consulter [Le guide du débutant pour Git & GitHub](https://medium.com/@mvthanoshan9/ubuntu-a-beginners-guide-to-git-github-44a2d2fda0b8).

### 1. Forker le dépôt

Forker le dépôt en cliquant sur le bouton fork en haut de la page. Cela créera une instance de ce dépôt entier dans votre compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/fork-1.png)

### 2. Cloner le dépôt

Une fois le dépôt dans votre compte, clonez-le sur votre machine pour travailler avec localement.

Pour cloner, cliquez sur le bouton clone et copiez le lien.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/clone1.png)

Ouvrez le terminal et exécutez la commande suivante. Cela clonera le dépôt localement.

```
$ git clone [ADRESSE HTTPS]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/clone2.png)

Maintenant, nous avons configuré une copie de la branche master à partir du dépôt de projet en ligne principal.

Nous devons accéder à ce répertoire cloné en exécutant cette commande :

```
$ cd [NOM DU DÉPÔT]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/clone3.png)

### 3. Créer une branche

Il est bon de créer une nouvelle branche lorsque vous travaillez avec des dépôts, qu'il s'agisse d'un petit projet ou d'une contribution au travail d'un groupe.

Le nom de la branche doit être court et doit refléter le travail que nous faisons.

Maintenant, créez une branche en utilisant la commande `git checkout` :

```
$ git checkout -b [Nom de la branche]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/branch1.png)

### 4. Faire des changements et les commiter

Apportons des modifications essentielles au projet et sauvegardons-le.

Ensuite, exécutez `git status`, et vous verrez les changements.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/status.png)

Ajoutez ces changements à la branche que vous venez de créer en utilisant la commande `git add` :

```
$ git add .
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/add1.png)

Maintenant, commitez ces changements en utilisant la commande `git commit` :

```
$ git commit -m "Ajout d'un article à la semaine 02 des articles de la semaine"
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/commit.png)

### 5. Pousser les changements vers GitHub

Afin de pousser les changements vers GitHub, nous devons identifier le nom du remote.

```
$ git remote
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/remote.png)

Pour ce dépôt, le nom du remote est « origin ».

Après avoir identifié le nom du remote, nous pouvons pousser ces changements vers GitHub en toute sécurité.

```
git push origin [Nom de la branche]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/branch2.png)

### 6. Créer une pull request

Allez dans votre dépôt sur GitHub et vous verrez un bouton « Compare & pull request » et cliquez dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/compare.png)

Veuillez fournir les détails nécessaires sur ce que vous avez fait (Vous pouvez référencer les problèmes en utilisant « # »). Maintenant, soumettez la pull request.

Félicitations ! Vous avez fait votre première pull request.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/pullRequest-1.png)

Si votre pull request est acceptée, vous recevrez un email.

### 7. Synchroniser votre branche master forkée

Avant de soumettre des pull requests au dépôt original, vous devez synchroniser votre dépôt avec l'original.

Même si vous n'allez pas soumettre de pull request au dépôt original, il est préférable de se synchroniser avec le dépôt original car certaines fonctionnalités supplémentaires et corrections de bugs peuvent avoir été faites depuis que vous avez forké le dépôt original.

Suivez ces étapes pour mettre à jour/synchroniser ces changements avec votre branche master :

1. Tout d'abord, vérifiez dans quelle branche vous vous trouvez.

```
$ git branch
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/branch4.png)

Cela listera toutes les branches et indiquera la branche actuelle ou active en vert.

2. Passez à la branche master.

```
$ git checkout master
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/master9.png)

3. Ajoutez le dépôt original comme un dépôt upstream.

Afin de tirer les changements du dépôt original dans votre version forkée, vous devez ajouter le dépôt Git original comme un dépôt upstream.

```
$ git remote add upstream [HTTPS]
```

Ici, [HTTPS] est l'URL que vous devez copier depuis le dépôt du propriétaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/owner-repo.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/remote-add.png)

4. Récupérez le dépôt.

Récupérez tous les changements du dépôt original. Les commits vers le dépôt original seront stockés dans une branche locale appelée upstream/master.

```
$ git fetch upstream
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/fetch.png)

5. Fusionnez-le.

Fusionnez les changements de upstream/master dans votre branche master locale. Cela synchronisera la branche master de votre fork avec le dépôt upstream sans perdre vos changements locaux.

```
$ git merge upstream/master
```

6. Poussez les changements vers GitHub

À ce stade, votre branche locale est synchronisée avec la branche master du dépôt original. Si vous souhaitez mettre à jour le dépôt GitHub, vous devez pousser vos changements.

```
$ git push origin master
```

**NOTE :** Après avoir synchronisé votre branche master forkée, vous pouvez supprimer ce remote si vous le souhaitez. Mais vous devrez également mettre à jour/synchroniser votre dépôt à l'avenir, il est donc préférable de le garder.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/remote-dlt.png)

```
$ git remote rm [Nom du Remote]
```

### 8. Supprimer la branche inutile

Les branches sont créées pour un but spécial. Une fois ce but accompli, ces branches ne sont plus nécessaires, vous pouvez donc les supprimer.

```
$ git branch -d [Nom de la branche]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/delete.png)

Vous pouvez également supprimer la version sur GitHub.

```
git push origin --delete [Nom de la branche]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/last.png)

## Conclusion

GitHub est un outil puissant pour contrôler l'historique des versions. Tout le monde peut contribuer aux projets open source en faisant des pull requests. Les contributions ne sont pas toujours du code – il y a d'autres façons de contribuer également.

Enfin, je dois vous dire que vous ne devriez pas vous inquiéter si vos pull requests sont rejetées. Les mainteneurs passent beaucoup de temps à améliorer leurs projets, et ils en savent beaucoup plus sur leurs projets que nous. Ne vous inquiétez donc pas si votre demande n'est pas fusionnée.

> Restez fort, restez positif et ne abandonnez jamais.
> 
> — Roy T. Bennett, [The Light in the Heart](https://www.goodreads.com/work/quotes/49604402)

Cet article a été initialement publié sur [Medium](https://medium.com/@mvthanoshan9/how-to-make-your-first-pull-request-on-github-9aefca5cc837).

Vous pouvez me contacter et me connecter sur [Twitter](https://twitter.com/ThanoshanMV).

**Continuez à contribuer au monde de l'open source !**