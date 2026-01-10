---
title: Comment faire votre première contribution de code Open Source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-14T17:25:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-open-source-contribution
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/IMG_6828-1.jpeg
tags:
- name: open source
  slug: open-source
seo_title: Comment faire votre première contribution de code Open Source
seo_desc: "By Aroboto Ife \nMaking your first Open Source contribution, like any other\
  \ first endeavor, can be difficult. Especially given the abundance of open-source\
  \ projects out there. \nThis article will help you to dip your toe into the open\
  \ source community ..."
---

Par Aroboto Ife

Faire votre première contribution Open Source, comme toute autre première entreprise, peut être difficile. Surtout étant donné l'abondance de projets open source disponibles.

Cet article vous aidera à tremper un pied dans les eaux de la communauté open source en faisant votre toute première contribution open source.

En explorant le monde de l'open source, vous avez l'opportunité de contribuer vos compétences et votre expérience à des projets valables. Et vous devenez également membre d'une communauté collaborative.

Pour commencer, vous allez utiliser [First Contributions](https://github.com/firstcontributions/first-contributions). Il s'agit d'un projet populaire qui aide les débutants à faire leur première contribution open source. Vous utiliserez également GitHub's Codespaces, votre environnement de développement local dans le cloud, pour permettre un processus de contribution fluide.

Pour commencer, vous devrez créer un compte GitHub si vous n'en avez pas déjà un. Suivez le processus d'inscription [ici](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=firstcontributions%2Ffirst-contributions). Tout est fait ? Commençons.

## Comment faire votre première contribution Open Source

### Étape Une : Fork le Dépôt

Fork un dépôt signifie faire une copie du dépôt dans votre compte GitHub. Cela vous permet de faire des changements sans perturber le projet principal.

* Tout d'abord, cliquez sur le bouton "Fork" en haut à droite du dépôt.
![fork](https://www.freecodecamp.org/news/content/images/2023/07/fork.PNG)

* Ensuite, cliquez sur le bouton "Create Fork" en bas de la page, comme dans la capture d'écran ci-dessous.
![createe](https://www.freecodecamp.org/news/content/images/2023/07/createe.png)

* Si c'est réussi, firstcontributions/first-contributions basculera vers votre nom de compte / first-contributions.

### Étape Deux : Clone le Dépôt

Codespaces configure automatiquement un environnement de développement pour vous avec le dépôt déjà cloné. Il n'est pas nécessaire de passer par la configuration manuelle avec votre terminal local.

* Cliquez sur le bouton vert "Code"
![code](https://www.freecodecamp.org/news/content/images/2023/07/code.PNG)

* Sélectionnez "Codespaces" dans le menu déroulant, puis cliquez sur le bouton "Create codespace on main".
![codespacess](https://www.freecodecamp.org/news/content/images/2023/07/codespacess.PNG)

### Étape Trois : Créez une Branche

Lors de l'utilisation de Codespaces, il n'est pas nécessaire de changer de répertoire car le dépôt est déjà disponible dans le répertoire actuel.

Pour créer une nouvelle branche, vous devrez taper cette commande dans votre terminal :

```sh
git switch -c votre-nouveau-nom-de-branche
```

C'est la commande `git switch -c` suivie du nom que vous souhaitez donner à votre branche.

![A](https://www.freecodecamp.org/news/content/images/2023/07/A.PNG)

### Étape Quatre : Faites vos Modifications

La seule modification que vous ferez pour ce tutoriel est d'ajouter votre nom et un lien vers votre compte GitHub au fichier CONTRIBUTORS.MD. Cela vous marque comme contributeur.

![name](https://www.freecodecamp.org/news/content/images/2023/07/name.PNG)

### Étape Cinq : Commit et Push

Maintenant, vous devrez préparer vos modifications en ajoutant les changements qui sont prêts à être commités. Vous pouvez le faire avec la commande suivante :

```sh
git add . ou git add Contributors.md
```

![D](https://www.freecodecamp.org/news/content/images/2023/07/D.PNG)

Ensuite, commitez vos changements en utilisant la commande ci-dessous :

```sh
git commit -m "Ajouter [votre nom] à la Liste des Contributeurs"
```

![C](https://www.freecodecamp.org/news/content/images/2023/07/C.PNG)

Enfin, poussez vos changements vers le dépôt comme ceci :

```sh
git push -u origin votre-nom-de-branche
```

![E-1](https://www.freecodecamp.org/news/content/images/2023/07/E-1.PNG)

Une fois que vous voyez quelque chose de similaire à la capture d'écran ci-dessous, vous êtes sur la bonne voie.

![F](https://www.freecodecamp.org/news/content/images/2023/07/F.PNG)

### Étape Six : Créez une Pull Request

Une pull request alerte les mainteneurs du dépôt des changements que vous avez faits. Cela leur permet de passer en revue ces changements avant de les fusionner dans le dépôt principal.

Pour créer une PR, suivez ces étapes :

* Passez à votre branche une fois que vous avez actualisé votre dépôt.
* Cliquez sur le bouton "Compare and pull request" qui apparaît.
![G](https://www.freecodecamp.org/news/content/images/2023/07/G.PNG)

* Écrivez une description de ce que vous avez fait, puis cliquez sur le bouton "Create pull request".
![H](https://www.freecodecamp.org/news/content/images/2023/07/H.PNG)

Une fois que vous avez terminé, le bot Frist contributions ou les mainteneurs fusionneront vos changements s'ils sont bons à aller.

## Conclusion

Félicitations ! Vous avez fait votre première contribution à l'open source. Il s'agit d'une étape passionnante qui marque le début de votre parcours en tant que contributeur.

Mais ne vous arrêtez pas là – il y a des centaines de projets open source sur GitHub qui ont besoin de votre aide. Explorez de nouveaux projets et continuez à contribuer.