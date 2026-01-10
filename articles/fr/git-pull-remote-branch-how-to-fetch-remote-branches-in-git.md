---
title: Git Pull Remote Branch – Comment récupérer des branches distantes dans Git
date: '2023-05-04T14:27:39.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/git-pull-remote-branch-how-to-fetch-remote-branches-in-git
posteditor: ''
proofreader: ''
author: Joel Olawanle
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-template--12-.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_desc: 'Git is a popular version control system that''s used by millions of developers
  to manage their codebases. One of the most powerful features of Git is its ability
  to work with remote repositories.

  When working on a project with multiple collaborators, ...'
---


Par Joel Olawanle

<!-- more -->

Git est un système de gestion de versions populaire utilisé par des millions de développeurs pour gérer leurs bases de code. L'une des fonctionnalités les plus puissantes de [Git][1] est sa capacité à travailler avec des dépôts distants (remotes).

Lorsque vous travaillez sur un projet avec plusieurs collaborateurs, vous devez être en mesure de récupérer les modifications du dépôt distant et de les fusionner avec votre dépôt local. Cet article vous apprendra comment récupérer des branches distantes dans Git.

## Qu'est-ce qu'une branche distante ?

Avant de découvrir comment récupérer des branches distantes, définissons ce qu'est une branche distante.

Une branche distante est une branche qui existe sur un dépôt distant, tel que [GitHub][2], GitLab ou Bitbucket.

Lorsque vous clonez un dépôt, Git crée automatiquement un « **remote** » qui pointe vers le dépôt d'origine. Vous pouvez ensuite utiliser ce remote pour récupérer les modifications effectuées par d'autres collaborateurs sur le projet.

## Comment récupérer des branches distantes dans Git

Lorsque vous clonez un dépôt, vous pouvez accéder à toutes ses branches distantes. Vous pouvez le vérifier en utilisant la commande `git branch` avec l'option `-r` :

```
git branch -r
```

![s_4A23CAD3B56D51AD7DA85730E428F7A2E6F6289B6BB197975176BE233B3F0EA9_1682869187912_image](https://paper-attachments.dropboxusercontent.com/s_4A23CAD3B56D51AD7DA85730E428F7A2E6F6289B6BB197975176BE233B3F0EA9_1682869187912_image.png)

Vous pouvez effectuer un `checkout` sur n'importe laquelle de ces branches en utilisant la commande `git checkout`.

Lorsque vous travaillez en groupe, un contributeur peut créer une nouvelle branche à distance. Vous pourriez avoir besoin de récupérer cette branche distante dans votre projet. Vous pouvez le faire avec la commande `git fetch`.

La commande `git fetch` interroge votre projet distant et télécharge toutes les données de ce projet distant que vous n'avez pas encore. Après cela, vous devriez avoir des références vers toutes les branches de ce remote, que vous pouvez fusionner ou inspecter à tout moment.

```
git fetch
```

Vous pouvez spécifier le nom du dépôt distant, qui est `origin` par défaut :

```
git fetch origin
```

Il est important de comprendre que lorsque vous utilisez la commande `git fetch`, elle télécharge uniquement les modifications effectuées dans le dépôt distant vers votre dépôt local sans les fusionner automatiquement avec votre travail ni modifier ce sur quoi vous travaillez actuellement. Vous devrez fusionner les modifications manuellement lorsque vous serez prêt.

Pour accéder au contenu récupéré, vous devez utiliser la commande `git checkout`. Cela garantit que le `fetch` est un moyen sûr de passer en revue les commits avant de les intégrer dans votre dépôt local.

Si vous souhaitez récupérer des branches distantes et les fusionner avec votre travail ou modifier votre branche actuelle, vous pouvez utiliser la commande `git pull`. Pour ce faire, utilisez la commande suivante :

```
git pull --all
```

Vous pouvez ensuite exécuter `git branch -r` pour vérifier si la branche distante a été ajoutée.

## Conclusion

La récupération de branches distantes dans Git est un aspect crucial de la collaboration dans un environnement de développement.

En suivant les étapes décrites dans cet article, vous pouvez récupérer les modifications apportées par d'autres collaborateurs sur des branches distantes et les fusionner avec votre dépôt local. Cela vous permet de travailler sur différentes branches d'un dépôt Git et de collaborer efficacement avec d'autres développeurs.

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web][3]. Consultez [mon blog][4] pour plus de contenu captivant de ma part.

Bon code !

[1]: https://kinsta.com/knowledgebase/install-git/
[2]: https://kinsta.com/knowledgebase/git-vs-github/
[3]: https://joelolawanle.com/contents
[4]: https://joelolawanle.com/posts