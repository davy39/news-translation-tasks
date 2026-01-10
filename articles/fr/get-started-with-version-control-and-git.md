---
title: Comment débuter avec le contrôle de version en utilisant Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-20T15:20:53.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-version-control-and-git
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/yancy-min-842ofHC6MaI-unsplash.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment débuter avec le contrôle de version en utilisant Git
seo_desc: "By Vasyl Lagutin\nIn this tutorial, you'll learn what version control is\
  \ and how you can contribute to open-source projects using Git. \nWe'll get through\
  \ the fundamentals of Git and I'll give you the knowledge that is indispensable\
  \ for any web develop..."
---

Par Vasyl Lagutin

Dans ce tutoriel, vous apprendrez ce qu'est le contrôle de version et comment vous pouvez contribuer à des projets open-source en utilisant **Git**. 

Nous aborderons les fondamentaux de **Git** et je vous donnerai les connaissances indispensables pour tout développeur web.

## Qu'est-ce que **Git** ?

**Git** est un logiciel de contrôle de version qui vous permet de collaborer avec d'autres programmeurs. Le plus grand problème que **Git** résout est qu'il aide les développeurs à suivre les différentes versions de la base de code sur laquelle ils travaillent.

Avant l'invention des systèmes de contrôle de version, il était assez difficile pour différents développeurs de synchroniser leur travail.

## Pourquoi utiliser **Git** ?

Si vous n'utilisez pas **Git**, la création d'un projet ressemblerait à ceci :

![Projet sans Git](https://res.cloudinary.com/practicaldev/image/fetch/s--cSVMreqQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://learn.coderslang.com/project-without-git.png)

Et avec **Git**, cela a l'air beaucoup plus élégant, comme ceci :

![Projet avec Git](https://www.freecodecamp.org/news/content/images/2021/05/Screen-Shot-2021-05-20-at-09.19.22.png)

## Comment installer **Git**

Vous pouvez télécharger et installer **Git** à partir du site officiel.

Assurez-vous d'ajouter **Git** au `Path` au cas où vous l'utiliseriez sur **Windows**.

Sous Linux, vous pouvez l'installer directement depuis le terminal en utilisant cette commande :

```
sudo apt-get install git

```

Une fois l'installation terminée, vous pouvez vérifier si **Git** a été installé correctement en exécutant cette commande :

```
git --version

```

Si vous obtenez la version actuellement installée, l'installation a réussi et vous êtes prêt à commencer.

## Les bases de **Git**

Passons maintenant à quelques petits exemples pour apprendre les bases de **Git**.

Tout d'abord, discutons de la manière dont vous pouvez créer une source unique de vérité pour votre code.

En termes de Git, l'endroit où votre code est stocké est appelé un **repository (dépôt)**.

### Comment initialiser un dépôt Git vide

La première étape pour utiliser **Git** dans votre projet est d'initialiser un dépôt **Git**. Vous pouvez initialiser un dépôt **Git** avec cette commande :

```
git init

```

Cette commande crée un sous-répertoire `.git` dans votre répertoire actuel. Il contiendra toutes les métadonnées internes de Git, comme l'historique des commits.

### Comment indexer (stage) les modifications dans Git

Nous devons créer des fichiers pour _indexer les modifications (stage changes)_ et effectuer des _commits_ (dont je parlerai ci-dessous). Créons `test.txt` et insérons-y du texte.

L'indexation (Staging) signifie indiquer à Git quels fichiers vous êtes prêt à Commit (ajouter) au dépôt. C'est très utile lorsque vous avez un travail en cours et que vous souhaitez Commit un seul fichier.

Maintenant, nous sommes prêts à indexer nos modifications. Vous pouvez lister individuellement les fichiers que vous souhaitez indexer comme ceci :

```
git add test.txt

```

Une fois cette commande exécutée, Git sait que `test.txt` est prêt à être Commit.

Alternativement, vous pouvez indexer tous les fichiers en utilisant cette commande :

```
git add .

```

C'est utile lorsque vous avez un tas de fichiers et que vous ne voulez pas taper chaque nom de fichier.

### Comment effectuer un Commit des modifications dans Git

Effectuer un Commit des modifications crée un instantané (snapshot) de la base de code à un moment donné. Vous pouvez revenir à cet instantané plus tard ou le partager avec vos coéquipiers afin qu'ils puissent continuer à partir de votre progression.

N'oubliez pas que seuls les fichiers qui ont été indexés (staged) pour le Commit seront inclus. Si vous n'indexez rien, vous ne pourrez pas effectuer de Commit.

Après avoir indexé nos modifications, il est temps pour nous de _commit_ les changements. Pour _commit_ les modifications, utilisez :

```
git commit -m "<message décrivant le changement>"

```

Une fois que nous avons exécuté le `git commit`, nous avons finalisé les modifications de la base de code.

### Comment consulter les logs dans Git

Vous pourriez vouloir consulter le log des modifications de votre projet. Vous pouvez le faire en utilisant cette commande :

```
git log

```

Un log ressemble à ceci :

![Git Log](https://www.freecodecamp.org/news/content/images/2021/05/git-log.png)

Comme vous le voyez, il y a 2 commits. Le premier montre que nous avons créé un nouveau fichier et le second décrit les modifications apportées à celui-ci.

Gardez à l'esprit que Git ne suit pas automatiquement les modifications que vous apportez. Vous devez les indexer (stage) et les Commit manuellement.

### Comment réinitialiser (reset) et annuler (revert) des commits dans Git

Si vous avez fait une erreur dans un Commit, vous pouvez vouloir annuler les modifications.

Il existe 2 façons d'annuler les modifications :

1. Reset
2. Revert

#### Git Reset

La syntaxe générale de la commande Reset ressemble à ceci : `git reset <types de reset> HEAD~<nombre de commits à annuler>`

Les **types de reset** les plus couramment utilisés sont :

* **--soft** : annuler le Commit et conserver les modifications
* **--hard** : annuler le Commit et supprimer les modifications

Si nous voulons annuler le Commit des modifications de Git, mais conserver les modifications locales du code, nous utilisons cette commande :

```
git reset --soft HEAD~1

```

C'est utile lorsque vous avez accidentellement indexé des fichiers qui ne devaient pas figurer dans le Commit.

Après le Reset, vous pouvez indexer les modifications nécessaires et les Commit.

#### Git Revert

Vous avez peut-être aussi remarqué que chaque Commit est associé à un hash.

![Git Log](https://www.freecodecamp.org/news/content/images/2021/05/git-commit-hash.png)

Vous pouvez également utiliser le hash pour annuler un Commit spécifique :

```
git revert 8a11c5095f2dcd70b0bc8c66061a1368558a3abf

```

C'est différent du Reset, car cela vous permet d'annuler les modifications effectuées dans un Commit spécifique.

Lorsque nous décomposons la commande, nous trouvons `git revert <hash du commit>`.

Git ajoute un Commit supplémentaire lorsque vous annulez les modifications avec Revert.

![Git Revert Commit](https://www.freecodecamp.org/news/content/images/2021/05/git-revert-commit.png)

### Comment utiliser les branches Git

Git vous permet de créer différentes branches. Ces branches vous permettent de séparer la portée des versions du code (par exemple, _corrections de bugs_, _développement_, _production_, etc. – toutes des branches différentes).

Pour créer une nouvelle branche, utilisez cette commande :

```
git checkout -b <nom de la nouvelle branche>

```

Pour basculer vers une branche existante, supprimez le drapeau `-b` et utilisez le nom de la branche existante au lieu du nouveau :

```
git checkout <nom de la branche>

```

### Comment fusionner (merge) des branches Git

Après avoir effectué des modifications dans une branche, vous pouvez vouloir mettre à jour une branche principale avec le code d'une autre branche. Pour ce faire, allez d'abord sur la branche que vous souhaitez mettre à jour et utilisez cette commande :

```
git merge <nom de la branche source de mise à jour>

```

![Git Merge](https://res.cloudinary.com/practicaldev/image/fetch/s--Top20AN3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://learn.coderslang.com/git-merge.png)

Si tout s'est bien passé, cette action créera un Commit de fusion dans la branche cible et y ajoutera tous vos commits.

### Comment résoudre les conflits dans Git

Lors de la fusion de branches, il peut arriver que la même partie du même fichier ait été mise à jour dans chaque branche.

Dans ce cas, un **conflit** survient car **Git** ne sait pas quelle modification conserver et laquelle ignorer. Git crée donc un message de **conflit** et vous invite à sélectionner manuellement quelle branche est correcte.

![Échec de la fusion Git](https://res.cloudinary.com/practicaldev/image/fetch/s---8rMBndd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://learn.coderslang.com/git-merge-fail.png)

Le message de conflit indique où le conflit s'est produit ainsi que les modifications actuelles et entrantes.

![Conflit Git](https://res.cloudinary.com/practicaldev/image/fetch/s--XYk3eEX7--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://learn.coderslang.com/git-conflict.png)

Après avoir décidé comment résoudre le conflit, vous devez ajouter un Commit pour résoudre le conflit.

## Comment travailler avec un dépôt Git distant

Pour collaborer avec d'autres, vous devrez travailler sur des dépôts distants. Nous nous concentrerons sur l'utilisation de **Git** en collaboration avec **GitHub**, mais vous pouvez utiliser n'importe quel autre site similaire comme **GitLab** ou **BitBucket**.

Pour collaborer avec d'autres, vous devez créer un compte sur le site web. Vous êtes maintenant prêt à contribuer à un projet open source sur **GitHub**.

Il n'y a pas si longtemps, j'ai découvert qu'il y avait un problème mineur dans le thème open-source Hugo [Papermod](https://github.com/adityatelange/hugo-PaperMod) que j'utilisais pour mon [blog de programmation](https://learn.coderslang.com).

La correction était assez simple et je voulais contribuer au projet pour l'améliorer.

Étapes pour contribuer :

1. Trouvez un dépôt auquel vous souhaitez contribuer. Ou, si vous travaillez dans un environnement d'entreprise, votre entreprise pourrait vous fournir un dépôt à utiliser.
2. **Forkez** le dépôt. Vous avez maintenant une copie du dépôt avec vous.

![Fork GitHub](https://www.freecodecamp.org/news/content/images/2021/05/Screen-Shot-2021-05-20-at-10.00.12.png)

3. Copiez le lien de clonage trouvé ici :

![Lien de clonage GitHub](https://www.freecodecamp.org/news/content/images/2021/05/Screen-Shot-2021-05-20-at-10.03.34.png)

4. Exécutez la commande suivante :

```
   git clone <lien de clonage>

```

Une copie du dépôt sera créée sur votre machine. Ajoutez le remote _Upstream_, juste un nom sophistiqué pour le dépôt source, en utilisant :

```
   git remote add <nom du remote upstream> <lien de clonage du dépôt source>

```

Vous pouvez maintenant utiliser les bases de **Git** que vous avez apprises pour modifier le code.

Après avoir effectué le Commit des modifications, vous pouvez mettre à jour le dépôt source en utilisant cette commande :

```
   git push origin <nom de la branche où pousser les modifications>

```

Vous pouvez maintenant [créer une _Pull Request_](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3/) dans le dépôt source, et les mainteneurs examineront et fusionneront votre code.

## Conclusion

Dans cet article, nous avons appris les fondamentaux de **Git**. Vous avez maintenant les outils pour utiliser le _contrôle de version_ et vous pouvez l'utiliser dans vos propres projets ou contribuer aux milliers de projets Open Source disponibles en ligne.

Si vous souhaitez approfondir le développement web moderne, jetez un œil à mon [cours Full-Stack JavaScript](https://js.coderslang.com) et à un [e-book gratuit contenant les 35 questions d'entretien JS les plus courantes](https://learn.coderslang.com/free-ebooks/).