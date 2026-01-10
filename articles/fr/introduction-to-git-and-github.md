---
title: Comment utiliser Git et GitHub – Introduction pour les débutants
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2022-09-26T05:23:00.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-git-and-github
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Untitled-design--6-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Comment utiliser Git et GitHub – Introduction pour les débutants
seo_desc: 'Git and GitHub are common tools used in programming. They help you manage
  different versions of your code and collaborate with other developers.

  Building projects is one of the core parts of being a developer. And Git and GitHub
  are essential tools y...'
---

Git et GitHub sont des outils courants utilisés en programmation. Ils vous aident à gérer différentes versions de votre code et à collaborer avec d'autres développeurs.

La création de projets est l'une des parties fondamentales du métier de développeur. Et Git et GitHub sont des outils essentiels que vous utiliserez lors de la création de projets avec d'autres personnes.

Mais ils peuvent paraître compliqués si vous ne les avez jamais utilisés auparavant. J'ai donc écrit cet article pour simplifier le fonctionnement de Git et GitHub.

## Table des matières

* [Que sont Git et GitHub ?](#heading-que-sont-git-et-github)
* [Pourquoi devriez-vous apprendre Git et GitHub ?](#heading-pourquoi-devriez-vous-apprendre-git-et-github)
* [Différences entre Git et GitHub](#heading-differences-entre-git-et-github)
* [Comment commencer à utiliser Git et GitHub](#heading-comment-commencer-a-utiliser-git-et-github)
* [Ressources pour apprendre Git et GitHub](#ressources-pour-apprendre-git-et-github)

## Que sont Git et GitHub ?

Git a été développé en 2005 par Linus Torvalds en tant que _logiciel open source_ pour suivre les modifications dans un _système de contrôle de version distribué_.

Git est open source car son code source est mis gratuitement à la disposition de quiconque souhaite le modifier et l'utiliser, en dehors de son créateur. Les projets open source sont construits et maintenus collectivement par différents développeurs dans différents endroits.

Git suit les modifications via un système de contrôle de version distribué. Cela signifie que Git peut suivre l'état des différentes versions de vos projets pendant que vous les développez. Il est distribué car vous pouvez accéder à vos fichiers de code depuis un autre ordinateur – et d'autres développeurs le peuvent aussi.

Lorsque vous construisez un projet open source, vous aurez besoin d'un moyen de documenter ou de suivre votre code. Cela aide à organiser votre travail et vous permet de garder une trace des modifications que vous avez apportées. C'est ce que Git vous permet de faire.

Mais vous avez également besoin d'un endroit pour héberger votre code – ce qui rend le contrôle de chaque version de votre projet plus facile et plus rapide. C'est là que GitHub intervient.

GitHub est un « hub » (un lieu ou une plateforme) où les utilisateurs de Git construisent des logiciels ensemble. GitHub est également un fournisseur d'hébergement et une plateforme de contrôle de version que vous pouvez utiliser pour collaborer sur des projets open source et partager des fichiers. Lorsque vous utilisez GitHub, vous travaillez avec Git sous le capot.

## Pourquoi devriez-vous apprendre Git et GitHub ?

Selon Techmonitor.ai, plus de 73 millions de développeurs utilisent GitHub en novembre 2021. Et la communauté GitHub devrait atteindre 100 millions d'utilisateurs d'ici 2025.

Comme vous pouvez le voir, des millions de personnes dans le monde entier utilisent ces outils, et les chiffres ne cessent d'augmenter.

Pour cette raison, de plus en plus d'entreprises exigent que les nouvelles recrues sachent utiliser Git et GitHub. Donc, si vous cherchez un emploi de développeur, ce sont des compétences essentielles à posséder.

Si vous n'utilisez pas Git et GitHub, c'est clair – vous devriez le faire !

## Différences entre Git et GitHub

Git est un système de contrôle de version qui gère et assure le suivi de votre code. GitHub, en revanche, est un service qui vous permet d'héberger, de partager et de gérer vos fichiers de code sur Internet.

GitHub utilise Git en arrière-plan et vous permet de gérer facilement vos dépôts ou dossiers Git sur sa plateforme.

Ainsi, Git est le système de contrôle de version proprement dit et GitHub est la plateforme où vous hébergez votre code.

Si vous souhaitez en savoir plus sur les différences entre ces deux outils, vous pouvez [lire ce tutoriel](https://www.freecodecamp.org/news/git-and-github-overview/).

## Comment commencer à utiliser Git et GitHub

### Étape 1 – Installer Git

Git est préinstallé sur certains systèmes Mac et basés sur Linux, mais vous pouvez toujours vérifier si Git est installé sur votre machine en tapant `git version` dans votre terminal. Vous pouvez utiliser l'invite de commande pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/checkGItInstalled-1.png)

Comme vous pouvez le voir ci-dessus, la version 2.31.1 de Git est installée sur mon ordinateur Windows. Si Git n'est pas installé sur votre ordinateur, vous n'obtiendrez pas de version.

Vous pouvez télécharger Git [ici](https://git-scm.com/download) puis sélectionner votre système d'exploitation pour le téléchargement.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/gitDownload-1.png)

Suivez le guide d'installation nécessaire jusqu'à ce que l'installation soit terminée. Ouvrez l'invite de commande et tapez `git version` pour vérifier que Git a été installé avec succès.

### Étape 2 – Créer un compte GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/githubDownload-1.png)

Pour créer un compte sur GitHub, on vous demandera quelques informations personnelles comme votre nom, la confirmation de votre e-mail, le choix d'un nom d'utilisateur et d'un mot de passe, et votre compte devrait être prêt en quelques minutes.

Créez un compte sur [GitHub.com ici](https://github.com/).

### Étape 3 – Connecter votre compte GitHub à votre compte Git.

Vous ferez cela depuis votre terminal.

Pour définir votre nom d'utilisateur Git, tapez ceci dans votre terminal :

```shell
git config --global user.name "Segun Ajibola"
```

Pour confirmer que vous avez correctement défini votre nom d'utilisateur Git, tapez ceci :

```shell
git config --global user.name
```

Vous devriez avoir "Segun Ajibola" comme résultat.

Pour définir votre e-mail Git, tapez ceci dans votre terminal :

```shell
git config --global user.email "youremail@gmail.com"
```

Pour confirmer que vous avez correctement défini votre e-mail Git, tapez ceci :

```shell
git config --global user.email
```

Vous devriez avoir "youremail@gmail.com" comme résultat.

Il vous sera demandé d'authentifier votre compte GitHub, connectez-vous simplement avec le même e-mail pour confirmer.

### Étape 4 – Créer et modifier vos fichiers de code localement

![Image](https://www.freecodecamp.org/news/content/images/2022/09/codeFIles-1.png)

### Étape 5 – Créer un dépôt sur GitHub

Cliquez sur le signe + dans le coin supérieur droit pour créer un nouveau dépôt. Les dépôts sont comme vos dossiers de code en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo-1.png)

Vous serez dirigé vers cette page :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo2-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepo3-1.png)

Nommez votre dépôt et donnez-lui une description (ceci est facultatif).

Cliquez sur le bouton "Create repository" pour créer le dépôt. Vous serez dirigé vers cette page :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/newRepoGitHub-1.png)

### Étape 6 – Pousser votre code local vers GitHub

Vous pouvez utiliser le terminal intégré de votre éditeur de code pour utiliser Git afin de pousser votre code vers GitHub. Appuyez sur `ctrl` + `shift` + `'` pour ouvrir le terminal dans VSCode.

Saisissez les commandes ci-dessous l'une après l'autre dans votre terminal. Appuyez sur la touche `Entrée` pour continuer après chaque saisie.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/pushCode-1.png)

`echo "# sample-code" >> README.md` 

`git init`

`git add .`

`git commit -m "premier commit"`

`git branch -M main`

`git remote add origin https://github.com/segunajibola/sample-code.git`

`git push -u origin main` 

Notez que nous avons `git add README.md` dans le dépôt sur GitHub. Mais ici, nous avons `git add .`, ce qui permet à Git d'ajouter tous nos fichiers de code au lieu du seul fichier `README.md` qui sera créé par `echo "# sample-code" >> README.md`. Donc, si vous avez créé d'autres fichiers dans votre dossier local, vous devez utiliser `git add .` pour ajouter tous les fichiers.

Prenez note que `git remote add origin [https://github.com/segunajibola/sample-code.git](https://github.com/segunajibola/sample-code.git)` contiendra le lien vers votre propre dépôt et il portera le nom de votre compte GitHub.

## Commandes Git courantes à connaître

Il existe de nombreuses commandes Git que vous pouvez utiliser dans le terminal, et cela peut devenir accablant. Je suggère donc de se concentrer d'abord sur certaines des plus populaires.

Les voici :

`git init` vous permet d'initialiser Git dans votre dossier.

`git add [Readme.md](https://readme.md/)` vous permet d'ajouter le fichier Readme, tandis que `git add .` vous permet d'ajouter tous les fichiers du dossier actuel.

`git commit` stocke les fichiers ajoutés. Utilisez `-m` pour le message suivi du message réel.

`git branch` crée une nouvelle branche qui est une nouvelle version du dépôt telle qu'elle apparaît lorsqu'elle est ajoutée, et `-M` pour déplacer le nom vers `main`.

`git remote add origin` connecte enfin le dossier local au dépôt sur GitHub. Il est suivi du lien du dépôt.

`git push -u origin main` pousse le code vers GitHub. Le drapeau `-u` crée une référence de suivi pour la branche, et `origin main` place le code dans la branche `main`.

Ce sont quelques-unes des principales commandes que vous utiliserez tout le temps. Ceci est un guide pour débutants et non technique pour vous aider à commencer à utiliser Git et GitHub, nous n'irons donc pas plus loin dans les détails ici.

Plus vous continuerez à utiliser GitHub, plus vous serez à l'aise avec ces commandes. La clé est de commencer petit et de maintenir votre élan.

Cela finira par devenir plus facile à mesure que vous construirez de petits projets et que vous les hébergerez sur GitHub en utilisant Git.

Si vous trouvez difficile d'utiliser le terminal pour naviguer entre les dossiers, passez un peu de temps à vous entraîner avec. Encore une fois, cela devient plus facile avec le temps et l'usage.

## Comment personnaliser votre profil GitHub

La personnalisation du README de votre profil GitHub vous aide à vous démarquer des utilisateurs aléatoires de GitHub.

Le fichier README.md vous aide à décrire votre profil GitHub, et vous pouvez l'utiliser pour montrer ce que vous apprenez actuellement ainsi que vos compétences et vos contributions.

Le README.md de GitHub utilise le markdown pour formater son contenu. Sa syntaxe est facile à apprendre.

[Voici](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/) un guide simple pour créer et personnaliser votre compte GitHub.

Voici le fichier README.md de mon profil GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme1-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme2-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme3-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/09/GithubReadme4-1.png)

Vous pouvez consulter d'autres profils personnalisés GitHub README.md [ici](https://github.com/abhisheknaiidu/awesome-github-profile-readme).

## Ressources pour apprendre Git et GitHub

Voici quelques cours et articles utiles que vous pouvez consulter si vous souhaitez apprendre Git et GitHub plus en détail :

1. [Tutoriel Git et GitHub – Contrôle de version pour les débutants](https://www.freecodecamp.org/news/git-and-github-for-beginners/)
2. [Commandes Git de base – Comment utiliser Git dans un projet réel](https://www.freecodecamp.org/news/how-to-use-basic-git-and-github-commands/)
3. [Git et GitHub pour les débutants - Cours accéléré](https://www.youtube.com/watch?v=RGOj5yH7evk)
4. [Une introduction à Git : ce que c'est et comment l'utiliser](https://www.freecodecamp.org/news/what-is-git-and-how-to-use-it-c341b049ae61/)
5. [À propos de GitHub](https://github.com/about)

## Conclusion

Si vous avez fini de lire ceci, vous vous sentez peut-être un peu dépassé par Git et GitHub. Oui, c'est une autre chose importante que vous devez apprendre en technologie, mais ne vous inquiétez pas.

Rappelez-vous que chaque fois que vous commencez à apprendre quelque chose de nouveau, au début, il peut sembler que vous n'y arriverez jamais. Mais après un certain temps et du travail acharné, vous deviendrez plus à l'aise.

C'est la même chose avec Git et GitHub – si vous l'utilisez beaucoup pendant un certain temps, vous finirez par être à l'aise avec.

Merci d'avoir lu cet article. Si vous l'avez apprécié, n'hésitez pas à le partager pour aider d'autres développeurs.

Vous pouvez me joindre sur [Twitter](https://twitter.com/iamsegunajibola), [LinkedIn](https://www.linkedin.com/in/segunajibola/) et [GitHub](https://github.com/segunajibola).

Bon apprentissage ✨.