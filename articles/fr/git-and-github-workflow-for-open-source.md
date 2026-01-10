---
title: Comment contribuer aux projets open-source – Workflow Git & GitHub pour débutants
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2023-09-22T12:35:14.000Z'
originalURL: https://freecodecamp.org/news/git-and-github-workflow-for-open-source
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Git
seo_title: Comment contribuer aux projets open-source – Workflow Git & GitHub pour
  débutants
---

GitHub-Workflow-for-Beginners.png
etiquettes:
- nom: guide pour débutants
  slug: guide-pour-debutants
- nom: Git
  slug: git
- nom: GitHub
  slug: github
- nom: open source
  slug: open-source
seo_title: null
seo_desc: 'La première fois que j'ai entendu parler de l'open source, c'était grâce à un tweet qui promouvait le Hacktoberfest en 2019. Et ma première pull request acceptée consistait à ajouter un titre de livre en emojis à une liste.

Vous pourriez penser : "On ne peut pas compter cela comme une contribution open source. C'est une blague !"

J'ai eu la même pensée moi-même — jusqu'à récemment. Se lancer dans l'open source était intimidant, mais j'ai réussi. Et en regardant en arrière, j'ai énormément appris de cette première contribution.

En tant que débutant qui ne savait rien de l'open source, j'ai appris à communiquer avec les mainteneurs, à travailler avec Git et GitHub, et à créer une pull request. C'était une courbe d'apprentissage abrupte !

C'est l'une des raisons pour lesquelles j'ai écrit ce guide : pour rendre votre parcours de contribution aux projets open-source plus fluide et moins intimidant.

Dans ce guide, je vais vous expliquer le workflow de base de Git et GitHub lors de la contribution à des projets open-source. Je vais également expliquer comment synchroniser vos dépôts forkés et locaux avec le dépôt original et comment résoudre les conflits de fusion lorsque vous en rencontrez un.

Sans plus attendre, commençons !

## Table des matières

* [Prérequis](#heading-prealables)
* [Tous les projets GitHub sont-ils Open Source ?](#heading-tous-les-projets-github-sont-ils-open-source)
* [Comment forker un dépôt](#heading-comment-forker-un-depot)
* [Comment cloner un dépôt](#heading-comment-cloner-un-depot)
* [Comment créer une nouvelle branche](#heading-comment-creer-une-nouvelle-branche)
* [Comment ajouter des changements à la zone de staging](#heading-comment-ajouter-des-changements-a-la-zone-de-staging)
* [Comment commiter des changements](#heading-comment-commiter-des-changements)
* [Comment synchroniser les changements](#heading-comment-synchroniser-les-changements)
* [Comment résoudre les conflits de fusion](#heading-comment-resoudre-les-conflits-de-fusion)
* [Comment pousser les changements](#heading-comment-pousser-les-changements)
* [Comment créer une pull request](#heading-comment-creer-une-pull-request)
* [Mots de la fin](#heading-mots-de-la-fin)

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Un compte [GitHub](https://github.com/).
* Un éditeur de code comme [VSCode](https://code.visualstudio.com/) installé sur votre machine.

## Tous les projets GitHub sont-ils Open Source ?

Lorsque vous êtes intéressé à faire des contributions, vous devez vous assurer que le projet qui vous intéresse est open source. Vous ne pouvez pas supposer que tous les projets sur GitHub sont open source.

Dans cette section, je vais partager ce que vous devez vérifier pour savoir si un projet est open source.

### La Licence

La licence est la première chose que vous voulez vérifier. Un projet sur GitHub n'est pas open source s'il n'a pas de licence.

Dans la plupart des juridictions, un projet sans licence est automatiquement licencié sous "Tous droits réservés" par son propriétaire. Cela signifie que personne ne peut utiliser, modifier ou redistribuer quoi que ce soit dans le projet sans la permission du propriétaire. Si vous l'ignorez, ils peuvent légalement vous poursuivre.

Vous pouvez trouver la licence dans un fichier appelé `LICENSE`. Vous la verrez généralement dans la section "À propos" du dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/repo-about-section-github-2.png)
_Une licence MIT dans la section "À propos" sur la barre latérale droite d'un dépôt sur GitHub_

### Le Guide de Contribution

La plupart des projets open-source sont prêts à recevoir des contributions lorsqu'ils ont un guide de contribution. Ce guide contient tout ce que vous devez savoir sur la façon de contribuer au projet, de l'ouverture d'un problème à la création d'une pull request. Du code de conduite au style de communication attendu.

Les procédures et exigences pour contribuer aux projets open-source peuvent différer d'un projet à l'autre. Vous devez toujours lire et suivre le guide lors de la contribution à un projet.

Généralement, vous trouverez une section sur le guide de contribution dans le README. Mais si vous ne la trouvez pas là, cherchez un fichier appelé `CONTRIBUTING.md` ou quelque chose de similaire.

### Sujet Hacktoberfest

[Hacktoberfest](https://hacktoberfest.com/) est un événement annuel en octobre sponsorisé par DigitalOcean pour soutenir l'open source.

Pour participer à cet événement et faire examiner et compter vos pull requests, vous devez vérifier si un projet participe au Hacktoberfest avant de contribuer.

Un projet participant à l'événement doit avoir un sujet `hacktoberfest` que vous pouvez trouver étiqueté dans la section "À propos" de la page principale du dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/about-repository-github.png)
_La section "À propos" sur la barre latérale droite d'un dépôt avec `hacktoberfest` comme l'un des sujets — Crédit : [AliceWonderland/hacktoberfest](https://github.com/AliceWonderland/hacktoberfest)_

## Comment forker un dépôt

Alors, vous êtes prêt à contribuer à un dépôt de votre choix. La première chose que vous devez faire est de forker le dépôt.

Forker signifie créer une copie d'un dépôt dans votre compte GitHub.

Vous devez toujours forker un dépôt car la plupart des propriétaires de projets open-source n'autorisent pas les contributeurs à pousser des changements directement dans leurs dépôts.

Par convention, votre dépôt forké est appelé le dépôt `origin`, tandis que le dépôt original est le dépôt `upstream`. Je vais utiliser ces alias à partir de maintenant pour les différencier.

Sur la page principale du dépôt sur GitHub, cliquez sur le bouton `Fork` en haut à droite :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/fork-button.png)
_Bouton `Fork` sur GitHub_

Cela vous redirigera vers le formulaire "Créer un nouveau fork". Vous pouvez laisser les champs tels quels. Ensuite, cliquez sur le bouton vert "Créer un fork" en bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-new-fork.png)
_Un formulaire `Créer un nouveau fork` avec un bouton vert `Créer un fork` sur GitHub_

Cela créera une copie du dépôt dans votre compte GitHub.

## Comment cloner un dépôt

Après avoir forké le dépôt, la prochaine chose à faire est de le cloner.

Cloner un dépôt signifie créer une copie d'un dépôt dans votre environnement local. Vous devez cloner votre dépôt forké lorsque vous contribuez à un projet open-source.

Voici les étapes à suivre :

#### Étape #1 - Naviguer vers le dépôt forké

Naviguez vers votre dépôt forké avec ces étapes :

* Cliquez sur votre avatar en haut à droite.
* Cliquez sur `Vos dépôts` dans le menu déroulant.
* Cliquez sur le dépôt que vous voulez cloner pour l'ouvrir.

Ensuite, cliquez sur le bouton vert `<> Code`. Copiez l'URL HTTPS en cliquant sur l'icône de copie.

Pour vous assurer que vous clonez le dépôt forké, vous devriez voir votre nom d'utilisateur GitHub dans le lien. Par exemple :

```text
https://github.com/<nom-dutilisateur-github>/<nom-du-depot>.git
```

C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/avatar-github.png)
_Avatar de l'utilisateur sur GitHub_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/dropdown-github-1.png)
_Menu déroulant sur GitHub qui met en évidence `Vos dépôts`_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/clone-github-resize-2.png)
_Un bouton vert `&lt;&gt; Code` et une URL HTTPS d'un dépôt suivie d'une icône de copie sur GitHub_

#### Étape #2 - Cloner le projet localement

Dans votre terminal, exécutez la commande `git clone` avec l'URL que vous avez copiée :

```bash
git clone <url-copiee>

```

Vous pouvez naviguer vers le répertoire du projet avec cette commande :

```bash
cd <nom-du-projet>

```

## Comment créer une nouvelle branche

La meilleure pratique en open source est de créer une nouvelle branche chaque fois que vous allez travailler sur un problème. Une nouvelle branche isole vos changements et garde la branche `main` propre.

Exécutez cette commande pour créer une nouvelle branche et y naviguer :

```bash
git checkout -b <nom-de-la-branche>
```

Bien que vous puissiez donner à une branche n'importe quel nom, vous devez suivre les conventions liées à la nomination d'une branche. Un nom de branche fait généralement référence au changement que vous apportez. Par exemple, `feature/ajouter-mode-sombre` ou `bugfix/lien-casse-vers-page-a-propos`.

Maintenant, vous pouvez commencer à apporter des modifications dans votre nouvelle branche.

## Comment ajouter des changements à la zone de staging

Disons que vous avez terminé de travailler sur des changements. Avant de commiter, vous devez d'abord les ajouter à la zone de staging.

Cette étape vous permet de garder vos changements tout en pouvant encore les modifier avant de commiter. Elle vous permet également de choisir quels changements vous êtes prêt à commiter.

L'ajout de changements à la zone de staging est souvent considéré comme une étape moins critique. Mais ce n'est pas vrai. Cette étape vous permet de changer d'avis avant de commiter. Car une fois que vous avez commité vos changements, vous ajoutez une partie de l'histoire au projet.

### Comment ajouter un ou plusieurs fichiers à la zone de staging

Lorsque vous voulez ajouter un ou plusieurs fichiers — mais pas tous — à la zone de staging, exécutez cette commande :

```bash
git add <nom-du-fichier-1> <nom-du-fichier-2>
```

Par exemple :

```bash
git add README.md CONTRIBUTING.md
```

La commande ci-dessus ajoute les fichiers **README.md** et **CONTRIBUTING.md** à la zone de staging.

Lorsque vous ajoutez des fichiers imbriqués à la zone de staging, vous voulez ajouter le ou les chemins vers le ou les fichiers. Si vous ne pouvez pas déterminer le chemin exact, l'exécution de `git status` vous aidera à obtenir l'état des fichiers qui contiennent vos changements.

Voici comment faire :

Exécutez `git status` dans votre terminal. Vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/git-status-modified-files-4.png)
_`git status` montrant les chemins vers trois fichiers modifiés sur le terminal VSCode_

Copiez le chemin et exécutez la commande `git add` avec le ou les chemins vers le ou les fichiers :

```bash
git add <chemin-vers-fichier-1> <chemin-vers-fichier-2>

```

Voici un exemple d'ajout de chemins vers deux fichiers basés sur la capture d'écran ci-dessus :

```bash
git add app/routes/__frontend/resources/index.mdx app/routes/__frontend/resources/developer-resources/open-source/index.mdx
```

### Comment ajouter tous les fichiers

Lorsque vous voulez ajouter tous les fichiers à la zone de staging, exécutez cette commande :

```bash
git add .
```

Cela ajoute tous les fichiers avec des changements à la zone de staging.

## Comment commiter des changements

Commiter signifie enregistrer vos changements. C'est pourquoi un commit nécessite un message comme enregistrement. Avec le temps, les commits raconteront l'histoire du projet. Donc, un message de commit clair et descriptif est essentiel.

Ce que vous devez savoir lorsque vous commitez vos changements :

* **Ajoutez et commitez vos changements souvent**. Le meilleur moment pour ajouter et commiter vos changements est chaque fois que vous avez terminé d'apporter une modification significative, même si c'est une petite modification. Commiter votre travail une fois terminé empêche également vos changements d'être reportés sur d'autres branches.
* **Utilisez un message clair et descriptif**. "Changer la couleur de fond du noir au bleu foncé" est plus descriptif et facile à comprendre par tout le monde que "Corriger le style".

Pour faire un commit, exécutez cette commande dans votre terminal :

```bash
git commit -m "Votre message"
```

Voici un exemple de commit sur une seule ligne :

```bash
git commit -m "Corriger le lien vers la page À propos"
```

Et voici un commit avec plusieurs lignes :

```bash
git commit -m "Corriger le lien vers la page À propos
Corriger les fautes de frappe dans la page À propos"
```

## Comment synchroniser les changements

Lorsque vous travaillez sur des changements, il est possible que la branche `main` du dépôt `upstream` ait déjà fusionné certaines pull requests. Ainsi, l'état des dépôts `origin` et locaux à ce moment-là ne sera plus le même que celui du dépôt `upstream`.

Pour cette raison, vous devez toujours mettre à jour votre branche de travail locale afin de pousser le même état que le dépôt `upstream`.

### Comment mettre à jour le dépôt `origin`

Tout d'abord, allez dans le dépôt `origin` sur GitHub pour vérifier s'il est à jour avec le dépôt `upstream`.

Vous pouvez pousser vos changements lorsqu'il n'y a pas de changement dans le dépôt `upstream`.

Pour savoir si le dépôt `origin` est à jour, vous verrez un message indiquant "Cette branche est à jour avec <noms du dépôt et de la branche>" sur la page principale du dépôt, comme le montre la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/up-to-date-branch-github-1.png)
_Une branche à jour dans le dépôt `origin` sur GitHub_

Mais lorsqu'il y a des changements, vous verrez un message indiquant "Cette branche est X commit(s) en retard sur <noms du dépôt et de la branche>".

![Image](https://www.freecodecamp.org/news/content/images/2023/09/branch-x-commits-behind-github-2.png)
_Un message indiquant qu'une branche dans le dépôt `origin` est huit commits en retard sur le dépôt `upstream` sur GitHub_

Pour mettre à jour le dépôt `origin` :

1. Cliquez sur le bouton déroulant `Sync fork`.
2. Cliquez sur le bouton vert `Update branch`.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/update-branch.png)
_Les boutons `Sync fork` et `Update branch` sur GitHub_

Après la mise à jour, vous verrez une notification "Successfully fetched and fast-forwarded from upstream <noms du dépôt et de la branche>" en haut.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/successfully-fetched-1.png)
_Une notification "Successfully fetched and fast-forwarded from upstream" sur GitHub_

### Comment tirer les changements

Maintenant que votre dépôt `origin` est à jour avec le dépôt `upstream`, il est temps de tirer les changements et de mettre à jour votre dépôt local.

Tirer est un moyen d'obtenir de nouveaux changements depuis le dépôt distant vers le dépôt local.

Pour tirer les changements, assurez-vous d'être sur votre branche de travail. Vous pouvez le faire en exécutant `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/git-status-branch.png)
_`git status` montrant un nom de branche_

Exécutez la commande `git pull` pour tirer les changements depuis la branche `main` dans le dépôt `origin` :

```bash
git pull origin main
```

Vous pouvez maintenant pousser vos changements si vous n'avez pas besoin de résoudre de conflits.

## Comment résoudre les conflits de fusion

Après avoir mis à jour votre dépôt local, vous pourriez rencontrer des conflits que vous devez corriger avant de pouvoir pousser vos changements.

Il est courant de rencontrer ces conflits dans les projets open-source. Les conflits de fusion se produisent généralement lorsqu'il y a des changements dans les mêmes lignes et fichiers depuis deux branches différentes.

Lorsqu'un conflit survient, vous verrez des options pour accepter les changements au-dessus de votre espace de travail dans VSCode. Vous verrez également d'autres changements différents des vôtres — le changement entrant.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/git-conflict.png)
_Options pour accepter le changement, le changement actuel et le changement entrant sur VSCode_

### Comment corriger les conflits de fusion

Vous pouvez choisir parmi différentes options lorsque vous voulez résoudre un conflit :

* **Accepter le changement actuel** : Lorsque vous souhaitez garder uniquement vos changements.
* **Accepter le changement entrant** : Lorsque vous voulez accepter uniquement les changements entrants qui ne sont pas les vôtres.
* **Accepter les deux changements** : Lorsque vous voulez accepter vos changements et les changements entrants.

Vous pouvez encore corriger les choses si nécessaire après avoir choisi l'action souhaitée.

Après avoir résolu les conflits, vous pouvez ensuite ajouter vos changements à la zone de staging et les commiter.

Puisque vous allez ajouter et commiter des changements dans un fichier existant, vous pouvez exécuter cette commande pour faire les deux actions en même temps :

```bash
git commit -am "Votre message"

```

## Comment pousser les changements

Maintenant, il est temps de pousser vos changements. Cela signifie déplacer les changements depuis le dépôt local vers le dépôt distant.

Vous devez toujours pousser vos changements vers le dépôt `origin`. Pour ce faire, exécutez cette commande dans votre terminal :

```bash
git push origin <nom-de-la-branche>
```

Il est possible que vous obteniez ce message d'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/no-upstream-branch-1.png)
_Message `git push` "fatal: The current branch &lt;nom-de-la-branche&gt; has no upstream branch."_

Vous pouvez copier, coller et exécuter la commande dans le message d'erreur dans votre terminal :

```bash
git push --set-upstream origin <nom-de-la-branche>
```

Alternativement, vous pouvez exécuter cette commande :

```bash
git push -u origin <nom-de-la-branche>
```

## Comment créer une pull request

Une pull request — communément appelée PR — est un moyen de notifier aux autres qu'une branche avec des changements a été poussée vers un dépôt distant.

Après l'ouverture d'une pull request, les mainteneurs peuvent examiner et discuter de vos changements. Ils peuvent vous demander d'apporter plus de modifications avant de pouvoir fusionner votre pull request ou les fusionner immédiatement dans la branche `main`.

### Comment créer une pull request

Tout d'abord, allez dans le dépôt `upstream` ou `origin` sur GitHub.

Ensuite, cliquez sur le bouton vert `Compare & pull request` pour être redirigé vers le formulaire `Ouvrir une pull request` :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/compare-and-pull-request1.png)
_Le bouton vert `Compare & pull request` sur GitHub_

Ensuite, remplissez le formulaire de pull request. S'il y a un modèle de pull request, complétez toutes les zones requises pour aider les mainteneurs à examiner vos changements.

S'il n'y a pas de modèle de pull request, vous pouvez écrire la pull request de manière structurée. Pensez à ceci lorsque vous écrivez votre pull request :

* Un titre court, clair et informatif.
* Une description claire des changements.
* Le lien vers le problème lié. Par exemple, "Clôt #456".
* Des captures d'écran ou des enregistrements d'écran lorsque nécessaire.

Enfin, cliquez sur le bouton vert `Create pull request` en bas pour créer une PR.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-pull-request-button.png)
_Le bouton vert `Create pull request` sur GitHub_

## Mots de la fin

Contribuer à des projets open-source peut être intimidant et vous faire sentir intimidé au début. Mais comme pour d'autres compétences, avec une pratique continue, vous deviendrez meilleur.

En plus de comprendre Git et GitHub, il y a également des [aspects non techniques de l'open source que vous devriez connaître](https://www.freecodecamp.org/news/how-to-contribute-to-open-source/).

Et une fois que vous aurez pris le coup, l'open source peut être tellement amusant !

Si vous avez aimé et apprécié cet article, veuillez le partager avec d'autres. Vous pouvez trouver d'autres travaux de moi sur mon [blog](https://adiati.com/), et connectons-nous sur [X (anciennement Twitter)](https://twitter.com/@AdiatiAyu) ou [LinkedIn](https://www.linkedin.com/in/adiatiayu/)!