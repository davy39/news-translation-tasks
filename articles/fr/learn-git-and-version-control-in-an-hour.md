---
title: Apprendre Git et le contrôle de version en une heure
subtitle: ''
author: Amarachi Johnson
co_authors: []
series: null
date: '2020-09-03T05:37:29.000Z'
originalURL: https://freecodecamp.org/news/learn-git-and-version-control-in-an-hour
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/photo-1534988333262-c455b9332e52.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Apprendre Git et le contrôle de version en une heure
seo_desc: 'Version control is something all software developers should know. It helps
  you manage changes to your projects or programs.

  This article will help you learn the basics of Git and versioning in order to effectively
  collaborate and manage your software...'
---

Le contrôle de version est quelque chose que tous les développeurs de logiciels devraient connaître. Il vous aide à gérer les changements apportés à vos projets ou programmes.

Cet article vous aidera à apprendre les bases de Git et du versionnage afin de collaborer efficacement et de gérer vos projets logiciels.

## Sommaire

* [Qu'est-ce que git et le contrôle de version ?](#heading-quest-ce-que-git-et-le-controle-de-version)
* [Installation de votre Gitbash](#heading-installation-de-votre-git-bash)
* [Initialisation de votre dépôt](#heading-initialisation-de-votre-depot)
* [Faire votre premier commit dans Git](#heading-faire-votre-premier-commit-dans-git)
* [Création d'une branche dans Git](#heading-creation-de-branches-dans-git)
* [Revenir à un commit](#heading-revenir-a-un-commit)
* [Création d'un dépôt distant](#heading-creation-dun-depot-distant)
* [Synchronisation de votre dépôt distant avec votre dépôt local](#heading-synchronisation-de-votre-depot-distant-avec-votre-depot-local)
* [Mise à jour de votre dépôt git (local et distant)](#heading-mise-a-jour-de-votre-depot-git-local-et-distant)
* [Que signifie "Origin" ?](#heading-que-signifie-origin)

## Prérequis

Je suppose que vous avez déjà un compte sur GitHub. Si ce n'est pas le cas, rendez-vous sur [GitHub](https://github.com) pour en créer un.

Vous devrez également télécharger et installer git bash depuis [git-scm.com](https://git-scm.com/) ou [gitforwindows.org](https://gitforwindows.org/) (si vous utilisez un PC Windows).

Maintenant, allons-y et apprenons le contrôle de version.

## Qu'est-ce que Git et le contrôle de version ?

Git est un système de contrôle de version utilisé pour suivre les modifications apportées à un fichier ou un projet. Il a été créé par Linus Trovalds (le créateur du système d'exploitation Linux).

GitHub, en revanche, est une plateforme de collaboration basée sur le cloud et open-source qui permet aux développeurs de partager facilement des logiciels et de collaborer sur différents projets.

Tout le monde, des projets open source aux équipes privées et aux projets individuels, peut utiliser GitHub. Vous pouvez simplement télécharger votre code et suivre les modifications apportées à un projet pour une utilisation future.

**Récapitulatif : Le contrôle de version** est un système qui enregistre les modifications apportées à un fichier ou à un ensemble de fichiers au fil du temps, afin que vous puissiez rappeler des versions spécifiques plus tard.

## Installation de votre Git Bash

Pour les besoins de ce tutoriel, nous allons créer un nouveau dossier, que j'ai nommé `babysteps2git`. Nous l'utiliserons comme notre dépôt local tout au long de cet article.

![filemgr.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574179089440/SP6x0atPG.png?auto=format&q=60)
_Un nouveau dossier créé spécialement pour ce tutoriel Git_

Dans ce dossier `babysteps2git`, nous avons un fichier, `index.html`, que nous utiliserons pour les exemples. Je l'ai créé depuis mon interface de ligne de commande préférée, Cmder.

Vous pouvez créer le vôtre en tapant `touch index.html` à l'intérieur du dossier `babysteps2git` (cela doit être fait depuis votre invite de commande) ou vous pouvez en créer un depuis votre éditeur de texte.

Maintenant, configurons notre Git globalement en configurant notre nom d'utilisateur et notre email (si c'est la première fois que vous utilisez Git).

Ouvrez git bash, puis utilisez la commande **`git config --global user.name "Votre nom"`** pour configurer votre nom d'utilisateur et **`git config --global user.email "Votre email"`** pour configurer votre email.

Dans l'exemple ci-dessous, mon nom d'utilisateur GitHub est `emmanuellar` tandis que mon adresse email est `emmanuellar805@gmail.com`.

![configure.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574193630610/mPZKvap3F.png?auto=format&q=60)
_Configuration de git sur votre appareil_

Pour vérifier si votre configuration a été ajoutée, tapez **`git config --global user.name`** pour vérifier votre nom d'utilisateur et **`git config --global user.email`** pour vérifier votre email.

Si votre configuration a réussi, vous verrez votre nom d'utilisateur et votre adresse email renvoyés une fois que vous aurez tapé ces commandes et appuyé sur _entrée_.

![config-check.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574193609012/qY1VzVm96.png?auto=format&q=60)
_Vérification de votre configuration_

## Initialisation de votre dépôt

Maintenant, vous voulez dire à Git "Écoute, c'est le dossier/répertoire où je veux que Git travaille maintenant."

Pour initialiser un dépôt, assurez-vous d'être dans le répertoire sur lequel vous travaillez. Dans mon cas ici, c'est le dossier `babysteps2git`.

Ensuite, tapez **`git init`** et appuyez sur entrée.

![init.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574193711528/CZEQRxsxZ.png?auto=format&q=60)

## Faire votre premier commit dans Git

Faire un commit dans Git équivaut à enregistrer lorsque vous travaillez sur des documents. C'est une façon d'enregistrer vos modifications dans le dépôt et de les stocker avec un identifiant unique et un message.

L'identifiant et le message peuvent être utilisés pour retrouver la version du projet que vous devez vérifier. C'est l'une des différences entre `git commit` et `save as`.

Avant de pouvoir faire un commit, vous devez mettre en attente votre travail. La mise en attente est une façon de dire au système, "Hé, j'ai fait beaucoup de changements à mon travail, mais celui-ci, celui-là, et cet autre sont ceux que je veux enregistrer."

Donc, lorsque vous voulez ajouter des changements, faites ceci : **`git add nom-des-fichiers`**.

Si vous voulez ajouter tous les fichiers que vous avez modifiés, tapez **`git add .`** à la place. Assurez-vous simplement d'être _à l'intérieur du dossier du projet_.

![add.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574194576920/fFTBuELCZ.png?auto=format&q=60)
_Mise en attente et commit de fichiers dans Git_

Après avoir ajouté/mis en attente les fichiers, vous pouvez maintenant les commiter.

Vous devriez commiter vos changements en utilisant des messages de commit courts mais détaillés comme celui montré ci-dessus.

Pour voir l'état de votre dépôt, et pour savoir sur quelle branche vous êtes, quels fichiers ont été modifiés, quel code est en attente, non en attente, ou prêt à être commité, utilisez simplement le code : **`git status`**.

## Création de branches dans Git

Disons que vous travaillez sur différentes versions d'un projet ou que vous collaborez sur un projet avec des amis ou des collègues. Il est important d'avoir une branche appelée "master", qui est la branche par défaut pour chaque dépôt qui stocke le code original et modifié des différents contributeurs.

Pour collaborer ou travailler sur diverses versions d'un projet, nous devons travailler à partir de différentes branches.

En développant dans des branches, il est non seulement possible de travailler sur plusieurs versions de votre code en parallèle, mais cela garde également la branche principale master libre de code douteux.

Donc, pour notre projet `babysteps2git`, nous pouvons décider d'avoir plusieurs branches, chacune abritant une version différente du code.

Pour créer une nouvelle branche dans git, utilisez la commande **`git branch nomDeLaBranche`**.

Pour basculer vers la nouvelle branche, utilisez **`git checkout nomDeLaBranche`**.

![branch.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574194634663/028KNmurN.png?auto=format&q=60)

Les deux commandes ci-dessus peuvent être exécutées simultanément en utilisant la commande : **`git checkout -b nomDeLaBranche`**.

## Revenir à un commit

Voici une autre chose très intéressante à propos de Git : la possibilité de revenir sur les changements que vous avez faits au fil du temps, quelque chose que CTRL+Z ne peut pas faire.

En travaillant avec Git, vous pourriez vouloir revenir à un état particulier de votre code, ou même revenir à une version plus ancienne de votre travail. Vous pouvez faire cela en revenant au commit particulier auquel vous voulez revenir.

Chaque commit que nous faisons a un identifiant unique qui lui est attaché. Pour obtenir cet identifiant, vous pouvez taper **`git log`**.

![gitlog.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574197402147/-xapiNqvo.png?auto=format&q=60)

Alternativement, la sortie ci-dessus peut être enregistrée en une ligne en utilisant **`git log --oneline`**.

![gitlogoneline.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574194674292/fjAKxkK9p.png?auto=format&q=60)

À partir de ce qui précède, vous pouvez voir l'identifiant et les messages de commit pour chacun des commits.

Pour revenir en arrière, tapez `**git revert commit-ID**`.

Cette commande revient à l'état de ce code au moment de ce commit.

![gitrevert.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1574194696800/Fzg8FK8ow.png?auto=format&q=60)

## Création d'un dépôt distant

Pour créer un dépôt distant, nous allons ouvrir notre compte GitHub et cliquer sur le bouton **New** (en tant que premier utilisateur de GitHub, vous verrez probablement un bouton vert **Create Repository** sur le vôtre à la place).

![createnew-repo.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575353701217/41qIRoebg.png?auto=format&q=60)

Quelle que soit la manière dont vous le faites, cela vous mènera à la page où vous entrez le nom de votre dépôt et une description de votre projet.

Il vous donne également la possibilité de rendre votre dépôt privé ou public. Vous pourriez également initialiser votre dépôt avec un `read me` en cochant la case read me.

![createnew-repo2.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575353777927/z8ark3A7B.png?auto=format&q=60)

Lorsque vous cliquez sur créer, un nouveau dépôt sera créé avec une URL unique.

## Synchronisation de votre dépôt distant avec votre dépôt local

Maintenant que nous avons créé notre dépôt distant, nous devons le synchroniser avec notre dépôt local afin qu'ils puissent communiquer de manière transparente.

Ouvrez votre git bash, naviguez jusqu'au dossier sur lequel vous travaillez, et entrez le code suivant : **`git remote add origin url`**.

![gitremote.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575353820397/u4y4X2V-8.png?auto=format&q=60)

## Mise à jour de votre dépôt git (local et distant)

Allons-y et ajoutons du code à notre fichier HTML :

```js
<html lang="en"> 
    <head>     
    <meta charset="UTF-8">     
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge>
	<title>Document</title> </head> 
        <body>         
        	<label for="inputEmail" class="sr-only">Adresse Email</label>     
			<input type="email" class="form-control" id="inputEmail" placeholder="Mot de passe"> 
        </body> 
</html>               
```

Répétons le processus de mise en attente et de commit de nos changements :

`git add index.html`
`git commit -m "ajout d'un formulaire"`

Tel qu'il est, notre dépôt local est actuellement un commit en avance sur le dépôt distant.

Pour mettre à jour le dépôt distant, nous devons pousser notre travail du dépôt local vers le dépôt distant en utilisant le code : `git push origin master`. "master" est la branche par défaut pour chaque dépôt et contient généralement le code principal du projet.

![git-push.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575354026303/3vWLFFLe1.png?auto=format&q=60)

Vous pouvez également choisir de créer une nouvelle branche si, par exemple, vous avez créé une nouvelle fonctionnalité mais que vous êtes inquiet de faire des changements au projet principal (branche master).

Tapez simplement `git branch nomDeLaBranche` pour créer une nouvelle branche, et utilisez `git checkout nomDeLaBranche` pour basculer vers la nouvelle branche.

Vous pouvez toujours utiliser `git branch` pour confirmer les branches dans ce dépôt. Le nom de la branche avec un astérisque à côté indique sur quelle branche vous êtes pointé à un moment donné.

![gitbranch.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575354567055/qm7NuZzkO.png?auto=format&q=60)

Vous pouvez également pousser les changements de votre nouvelle branche vers votre dépôt distant avec `git push origin nomDeLaBranche`.

Lorsque vous poussez vers le dépôt distant, GitHub créera automatiquement la branche pour vous sur votre dépôt distant. Cela permet aux gens de voir les changements que vous avez faits.

Vous pourriez également vouloir mettre à jour la branche principale du projet (branche master) avec le contenu de la nouvelle branche distante.

Vous pouvez faire cela en basculant vers la branche master et en exécutant `git pull origin nouvelleBranche`. Cela met à jour la branche master avec tous les changements implémentés sur la nouvelle branche.

![pull.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1575355770131/DpOZB3-9u.png?auto=format&q=60)

## Que signifie "Origin" ?

Origin est un nom abrégé pour le dépôt distant à partir duquel un projet a été initialement cloné. Plus précisément, il est utilisé à la place de l'URL de ce dépôt original, et facilite sa référence.

Donc, pour pousser vos changements vers le dépôt distant, vous pouvez utiliser l'une des commandes suivantes : `git push origin nomDeLaBranche` ou `git push https://github.com/username/reponame.git nomDeLaBranche`.

Notez que vous pourriez être invité à entrer votre nom d'utilisateur et votre mot de passe. Votre mot de passe ne s'affichera pas lorsque vous le tapez. Tapez-le simplement correctement et appuyez sur entrée.

## Conclusion

Nous venons de voir un guide étape par étape pour utiliser Git pour la première fois. N'hésitez pas à vous y référer chaque fois que vous êtes bloqué.

Vous n'avez pas à _mémoriser_ les commandes – vous pourrez vous en souvenir avec le temps. :)

C'est tout pour l'instant !

J'espère que vous avez apprécié cet article. Vous pouvez me suivre sur [Twitter](https://twitter.com/msamarachukwu).