---
title: Git Cheat Sheet – 50 Commandes Git Que Vous Devriez Connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-08T21:59:56.000Z'
originalURL: https://freecodecamp.org/news/git-cheat-sheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/git-cheat-sheet-cover.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: Git Cheat Sheet – 50 Commandes Git Que Vous Devriez Connaître
seo_desc: "By Fabio Pacific\nGit is a distributed version control system that helps\
  \ developers collaborate on projects of any scale. \nLinus Torvalds, the developer\
  \ of the Linux kernel, created Git in 2005 to help control the Linux kernel's development.\
  \ \nWhat is ..."
---

Par Fabio Pacific

Git est un système de contrôle de version distribué qui aide les développeurs à collaborer sur des projets de toute envergure. 

Linus Torvalds, le développeur du noyau Linux, a créé Git en 2005 pour aider à contrôler le développement du noyau Linux. 

## Qu'est-ce qu'un Système de Contrôle de Version Distribué ?

Un système de contrôle de version distribué est un système qui vous aide à suivre les modifications que vous avez apportées aux fichiers de votre projet. 

Cet historique des modifications vit sur votre machine locale et vous permet de revenir à une version précédente de votre projet avec facilité en cas de problème.

Git facilite la collaboration. Tout le monde dans l'équipe peut garder une sauvegarde complète des dépôts sur lesquels ils travaillent sur leur machine locale. Ensuite, grâce à un serveur externe comme BitBucket, GitHub ou GitLab, ils peuvent stocker en toute sécurité le dépôt en un seul endroit. 

De cette façon, différents membres de l'équipe peuvent le copier localement et tout le monde a une vue d'ensemble claire de toutes les modifications apportées par toute l'équipe.  

Git dispose de nombreuses commandes différentes que vous pouvez utiliser. Et j'ai constaté que ces cinquante sont celles que j'utilise le plus souvent (et sont donc les plus utiles à retenir). 

Je les ai donc écrites et j'ai pensé qu'il serait bien de les partager avec la communauté. J'espère que vous les trouverez utiles – Bonnes pratiques.          

## Comment vérifier votre configuration Git :
La commande ci-dessous retourne une liste d'informations sur votre configuration git, y compris le nom d'utilisateur et l'email :
```
git config -l
```

## Comment configurer votre nom d'utilisateur Git :
Avec la commande ci-dessous, vous pouvez configurer votre nom d'utilisateur :
```
git config --global user.name "Fabio"
```

## Comment configurer votre email d'utilisateur Git :
Cette commande vous permet de configurer l'adresse email de l'utilisateur que vous utiliserez dans vos commits.
```
git config --global user.email "signups@fabiopacifici.com"
```

## Comment mettre en cache vos identifiants de connexion dans Git :
Vous pouvez stocker les identifiants de connexion dans le cache pour ne pas avoir à les taper à chaque fois. Utilisez simplement cette commande :
```
git config --global credential.helper cache
```

## Comment initialiser un dépôt Git :
Tout commence ici. La première étape consiste à initialiser un nouveau dépôt Git localement dans la racine de votre projet. Vous pouvez le faire avec la commande ci-dessous :
```
git init
```

## Comment ajouter un fichier à la zone de staging dans Git :
La commande ci-dessous ajoutera un fichier à la zone de staging. Remplacez simplement `filename_here` par le nom du fichier que vous souhaitez ajouter à la zone de staging.
```
git add filename_here
```
## Comment ajouter tous les fichiers dans la zone de staging dans Git
Si vous souhaitez ajouter tous les fichiers de votre projet à la zone de staging, vous pouvez utiliser un caractère générique `.` et chaque fichier sera ajouté pour vous.
```
git add .
```

## Comment ajouter uniquement certains fichiers à la zone de staging dans Git
Avec l'astérisque dans la commande ci-dessous, vous pouvez ajouter tous les fichiers commençant par 'fil' dans la zone de staging.
```
git add fil*
```

## Comment vérifier l'état d'un dépôt dans Git :
Cette commande affichera l'état du dépôt actuel, y compris les fichiers stagés, non stagés et non suivis. 
```
git status
```

## Comment commiter les modifications dans l'éditeur dans Git :
Cette commande ouvrira un éditeur de texte dans le terminal où vous pourrez écrire un message de commit complet. 

Un message de commit est composé d'un court résumé des modifications, d'une ligne vide et d'une description complète des modifications après celle-ci.
```
git commit
```
## Comment commiter les modifications avec un message dans Git :
Vous pouvez ajouter un message de commit sans ouvrir l'éditeur. Cette commande vous permet de spécifier uniquement un court résumé pour votre message de commit.
```
git commit -m "votre message de commit ici"
```

## Comment commiter les modifications (et sauter la zone de staging) dans Git :
Vous pouvez ajouter et commiter des fichiers suivis avec une seule commande en utilisant les options -a et -m.
```
git commit -a -m"votre message de commit ici"
```

## Comment voir votre historique de commits dans Git :
Cette commande affiche l'historique des commits pour le dépôt actuel :
```
git log
```

## Comment voir votre historique de commits incluant les modifications dans Git :
Cette commande affiche l'historique des commits incluant tous les fichiers et leurs modifications :
```
git log -p
```

## Comment voir un commit spécifique dans Git :
Cette commande affiche un commit spécifique.

Remplacez commit-id par l'id du commit que vous trouvez dans le journal des commits après le mot commit.
```
git show commit-id
```

## Comment voir les statistiques de log dans Git :
Cette commande fera en sorte que le log Git affiche quelques statistiques sur les modifications dans chaque commit, y compris les lignes modifiées et les noms de fichiers.

```
git log --stat
```

## Comment voir les modifications apportées avant de les commiter en utilisant "diff" dans Git :
Vous pouvez passer un fichier en tant que paramètre pour ne voir que les modifications sur un fichier spécifique.
`git diff` montre uniquement les modifications non stagées par défaut. 

Nous pouvons appeler diff avec le flag `--staged` pour voir les modifications stagées.
```
git diff
git diff all_checks.py
git diff --staged
```

## Comment voir les modifications en utilisant "git add -p" :
Cette commande ouvre une invite et demande si vous souhaitez stager les modifications ou non, et inclut d'autres options.
```
git add -p
```

## Comment supprimer les fichiers suivis de l'arborescence de travail actuelle dans Git :
Cette commande attend un message de commit pour expliquer pourquoi le fichier a été supprimé. 
```
git rm filename
```
## Comment renommer les fichiers dans Git :
Cette commande stage les modifications, puis elle attend un message de commit. 
```
git mv oldfile newfile
```

## Comment ignorer les fichiers dans Git :
Créez un fichier `.gitignore` et commitez-le.


## Comment annuler les modifications non stagées dans Git :
```
git checkout filename
```

## Comment annuler les modifications stagées dans Git :
Vous pouvez utiliser l'option de flag -p pour spécifier les modifications que vous souhaitez réinitialiser. 
```
git reset HEAD filename
git reset HEAD -p
```

## Comment modifier le commit le plus récent dans Git :
`git commit --amend` vous permet de modifier et d'ajouter des modifications au commit le plus récent.
```
git commit --amend
```
!!Note!!: corriger un commit local avec amend est génial et vous pouvez le pousser vers un dépôt partagé après l'avoir corrigé. Mais vous devriez éviter de modifier les commits qui ont déjà été rendus publics.

## Comment annuler le dernier commit dans Git :
`git revert` créera un nouveau commit qui est l'opposé de tout ce qui se trouve dans le commit donné. 
Nous pouvons annuler le dernier commit en utilisant l'alias head comme ceci :

```
git revert HEAD
```

## Comment annuler un ancien commit dans Git :
Vous pouvez annuler un ancien commit en utilisant son id de commit. Cela ouvre l'éditeur pour que vous puissiez ajouter un message de commit.
```
git revert comit_id_here
```

## Comment créer une nouvelle branche dans Git :
Par défaut, vous avez une branche, la branche principale. Avec cette commande, vous pouvez créer une nouvelle branche. Git ne basculera pas automatiquement vers celle-ci – vous devrez le faire manuellement avec la commande suivante.
```
git branch branch_name
```

## Comment basculer vers une branche nouvellement créée dans Git :
Lorsque vous souhaitez utiliser une branche différente ou nouvellement créée, vous pouvez utiliser cette commande :
```
git checkout branch_name
```

## Comment lister les branches dans Git :
Vous pouvez afficher toutes les branches créées en utilisant la commande `git branch`. Elle affichera une liste de toutes les branches et marquera la branche actuelle avec un astérisque et la mettra en surbrillance en vert. 
```
git branch
```

## Comment créer une branche dans Git et basculer vers celle-ci immédiatement :
En une seule commande, vous pouvez créer et basculer vers une nouvelle branche immédiatement.
```
git checkout -b branch_name
```

## Comment supprimer une branche dans Git :
Lorsque vous avez terminé de travailler avec une branche et que vous l'avez fusionnée, vous pouvez la supprimer en utilisant la commande ci-dessous :
```
git branch -d branch_name
```

## Comment fusionner deux branches dans Git :
Pour fusionner l'historique de la branche dans laquelle vous vous trouvez actuellement avec le `branch_name`, vous devrez utiliser la commande ci-dessous :
```
git merge branch_name
```

## Comment afficher le journal des commits sous forme de graphique dans Git :
Nous pouvons utiliser `--graph` pour obtenir le journal des commits sous forme de graphique. De plus, 
`--oneline` limitera les messages de commit à une seule ligne.
```
git log --graph --oneline
```

## Comment afficher le journal des commits sous forme de graphique de toutes les branches dans Git :
Fait la même chose que la commande ci-dessus, mais pour toutes les branches. 
```
git log --graph --oneline --all
```

## Comment annuler une fusion conflictuelle dans Git :
Si vous souhaitez abandonner une fusion et recommencer, vous pouvez exécuter la commande suivante :
```
git merge --abort
```

## Comment ajouter un dépôt distant dans Git
Cette commande ajoute un dépôt distant à votre dépôt local (remplacez simplement `https://repo_here` par l'URL de votre dépôt distant). 
```
git add remote https://repo_here
```

## Comment voir les URLs distantes dans Git :
Vous pouvez voir tous les dépôts distants pour votre dépôt local avec cette commande :
```
git remote -v
```

## Comment obtenir plus d'informations sur un dépôt distant dans Git :
Remplacez simplement `origin` par le nom du dépôt distant obtenu en 
exécutant la commande git remote -v.
```
git remote show origin
```

## Comment pousser les modifications vers un dépôt distant dans Git :
Lorsque tout votre travail est prêt à être sauvegardé sur un dépôt distant, vous pouvez pousser toutes les modifications en utilisant la commande ci-dessous :
```
git push
```

## Comment tirer les modifications d'un dépôt distant dans Git :
Si d'autres membres de l'équipe travaillent sur votre dépôt, vous pouvez récupérer les dernières modifications apportées au dépôt distant avec la commande ci-dessous :

```
git pull
```


## Comment vérifier les branches distantes que Git suit :
Cette commande affiche le nom de toutes les branches distantes que Git suit pour le dépôt actuel :
```
git branch -r

```

## Comment récupérer les modifications d'un dépôt distant dans Git :
Cette commande téléchargera les modifications d'un dépôt distant mais n'effectuera pas de fusion sur votre branche locale (comme le fait git pull). 
```
git fetch
```

## Comment vérifier le journal des commits actuels d'un dépôt distant dans Git
Commit après commit, Git construit un journal. Vous pouvez découvrir le journal du dépôt distant en utilisant cette commande :
```
git log origin/main
```

## Comment fusionner un dépôt distant avec votre dépôt local dans Git :
Si le dépôt distant a des modifications que vous souhaitez fusionner avec votre dépôt local, alors cette commande le fera pour vous :
```
git merge origin/main
```

## Comment obtenir le contenu des branches distantes dans Git sans fusion automatique :
Cela vous permet de mettre à jour le dépôt distant sans fusionner de contenu dans les 
branches locales. Vous pouvez appeler git merge ou git checkout pour effectuer la fusion.
```
git remote update
```

## Comment pousser une nouvelle branche vers un dépôt distant dans Git :
Si vous souhaitez pousser une branche vers un dépôt distant, vous pouvez utiliser la commande ci-dessous. N'oubliez pas d'ajouter -u pour créer la branche en amont :
```
git push -u origin branch_name

```

## Comment supprimer une branche distante dans Git :
Si vous n'avez plus besoin d'une branche distante, vous pouvez la supprimer en utilisant la commande ci-dessous :
```
git push --delete origin branch_name_here
```


## Comment utiliser Git rebase :
Vous pouvez transférer le travail terminé d'une branche à une autre en utilisant `git rebase`.
```
git rebase branch_name_here
```
Git Rebase peut devenir très compliqué si vous ne le faites pas correctement. Avant d'utiliser cette commande, je vous suggère de relire la documentation officielle [ici](https://git-scm.com/book/it/v2/Git-Branching-Rebasing)


## Comment exécuter rebase de manière interactive dans Git :
Vous pouvez exécuter git rebase de manière interactive en utilisant le flag -i. 
Il ouvrira l'éditeur et présentera un ensemble de commandes que vous pouvez utiliser.
```
git rebase -i master
# p, pick = utiliser le commit
# r, reword = utiliser le commit, mais éditer le message de commit
# e, edit = utiliser le commit, mais s'arrêter pour modifier
# s, squash = utiliser le commit, mais fusionner dans le commit précédent
# f, fixup = comme "squash", mais ignorer le message de log de ce commit
# x, exec = exécuter la commande (le reste de la ligne) en utilisant le shell
# d, drop = supprimer le commit
```

## Comment forcer une demande de push dans Git :
Cette commande forcerait une demande de push. Cela est généralement acceptable pour les branches de pull request car personne d'autre ne devrait les avoir clonées. 
Mais ce n'est pas quelque chose que vous voulez faire avec des dépôts publics.
```
git push -f
```


## Conclusion
Ces commandes peuvent améliorer considérablement votre productivité dans Git. Vous n'avez pas à tous les retenir – c'est pourquoi j'ai écrit cette feuille de triche. Marquez cette page pour référence future ou imprimez-la si vous le souhaitez.

Merci d'avoir lu ! Au fait, je suis Fabio, un développeur web full-stack et enseignant, et professionnel certifié en automatisation informatique avec Python. Si vous trouvez cette feuille de triche utile, vous trouverez sûrement quelque chose d'intéressant également sur ma chaîne YouTube. Vous pouvez vous abonner [ici](https://www.youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ).