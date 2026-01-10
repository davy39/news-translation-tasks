---
title: Comment passer de zéro à Create-React-App sur Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T17:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-go-from-scratch-to-create-react-app-on-windows-2019
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U5i59ltV6vwiL1W_kXU8SA.jpeg
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment passer de zéro à Create-React-App sur Windows
seo_desc: 'By Scott Spence

  An opinionated guide on setting up a web development environment on Windows 10

  I have been a professional web developer since march 2018 and used both MacOs and
  Windows in that time. My preferred OS to use is Windows, for no other rea...'
---

Par Scott Spence

#### Un guide opinionné sur la configuration d'un environnement de développement web sur Windows 10

Je suis développeur web professionnel depuis mars 2018 et j'ai utilisé à la fois MacOS et Windows pendant cette période. Mon système d'exploitation préféré est Windows, pour aucune autre raison que je préfère la disposition du clavier.

Avec Windows/Linux, j'aime avoir ma touche Ctrl comme touche à utiliser pour les opérations de copier-coller et je peux utiliser mon petit doigt gauche au lieu de mon pouce. En tout cas, laissons la faible raisonnement derrière nous car ce n'est pas le but de ce post !

Si vous n'avez pas de machine Windows, alors ce post n'est probablement pas pour vous, si cela est différent de ce que vous utilisez, cela ne le rend pas mauvais.

Voyons ce que Ken a à dire à ce sujet :

%[https://twitter.com/ken_wheeler/status/1075556283795824640]

Ceci est la mise à jour de [mon guide du début de l'année](https://blog.scottspence.me/wsl-setup/) sur la configuration d'un environnement de développement web sur une machine Windows.

Ce guide couvrira l'installation d'Ubuntu, mais vous pouvez utiliser certaines des autres saveurs de Linux disponibles dans le Windows Store, la configuration de Debian sera très similaire à celle d'Ubuntu.

### Objectif de ce post

Passer d'une instance fraîche de Windows 10 à quelque chose avec lequel vous pouvez développer des applications web.

Ces instructions sont pour **Windows 10 Fall Creators Update et versions ultérieures**.

Ce que nous allons couvrir :

* Installer WSL
* Activer WSL sur votre machine
* Mettre à jour, améliorer et autoremove
* Installer Node (avec `n`)
* Installer Visual Studio Code
* Installer Windows Git
* Installer un Terminal (Hyper)
* Installer Fish Shell !
* Installer Oh My Fish
* Thèmes Fish avec OMF
* Configurer
* Configurer Git
* Créer React App
* Utiliser SSH avec GitHub
* Configurer SSH WSL
* Configurer SSH Windows Git Bash
* Changer la version de WSL
* Conclusion !

### Installer WSL

Vous pouvez installer Ubuntu depuis [le Microsoft Store](https://www.microsoft.com/en-gb/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab) ce qui sera la première moitié de l'installation, la seconde aura lieu lorsque vous ouvrirez l'application.

### Activer WSL sur votre machine

La [documentation officielle](https://docs.microsoft.com/en-us/windows/wsl/install-win10) couvre très bien le sujet, mais je vais ajouter les raccourcis clavier ici si vous ne voulez pas cliquer avec la souris.

Avant cela, cependant, si vous n'avez pas sélectionné PowerShell comme votre invite de commande par défaut, vous pouvez le sélectionner depuis la page des paramètres de la barre des tâches située dans la section Personnalisation des Paramètres, je suggère de le faire maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*wgsnQOuLLs0oLAxLDD8ibw.gif)

Pendant que nous y sommes, nous devrions également activer les dossiers cachés et ajouter les extensions de fichiers pour les types de fichiers connus dans l'Explorateur de fichiers Windows.

Ouvrez l'Explorateur de fichiers Windows avec la touche Windows+e, puis sélectionnez Affichage dans le ruban. Cliquez ensuite sur le bouton Options à l'extrême droite, cela ouvrira la boîte de dialogue Options des dossiers, à partir de là, nous voulons sélectionner l'onglet Affichage et sélectionner le bouton radio pour les fichiers et dossiers cachés avec 'Afficher les fichiers, dossiers et lecteurs cachés', décochez également l'option 'Masquer les extensions des types de fichiers connus'. Cliquez sur appliquer et OK.

La raison pour laquelle nous faisons cela est que nous pouvons voir le dossier `.git` dans les structures de projet, c'est aussi nécessaire pour les fichiers comme les fichiers `.env` qui sont utilisés pour la configuration de l'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m8bJzbFNFMnKuD-U9LpdUg.gif)

Utilisez la touche Windows+x, cela revient à cliquer avec le bouton droit sur l'icône Windows sur le bureau, cela ouvrira le menu de liens rapides. À partir de là, vous devez sélectionner l'option Windows PowerShell (Admin), vous pouvez le faire en appuyant sur **a** sur le clavier. Donc Windows key+x puis a, ouvrira l'invite de contrôle de compte d'utilisateur (Admin), en supposant que vous avez des droits d'administrateur sur votre machine, vous devrez cliquer sur oui pour continuer.

Copiez le code ici et collez-le dans la fenêtre PowerShell, Ctrl+v fonctionnera dans PowerShell, appuyez sur Entrée pour exécuter la commande.

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Vous serez invité à redémarrer votre machine après cela, ce que vous devriez faire.

> Consultez le lien pour une liste complète des [raccourcis clavier Windows](https://support.microsoft.com/en-gb/help/12445/windows-keyboard-shortcuts).

Après avoir redémarré, vous pouvez ouvrir le programme Ubuntu depuis le menu Démarrer et la deuxième installation (de WSL sur votre système) devrait avoir lieu. Attendez que cela se termine, puis vous serez invité à créer un utilisateur et un mot de passe pour le compte. Vous devrez vous souvenir du mot de passe créé pour l'utilisateur car vous serez invité à l'utiliser pour les privilèges `sudo`.

### Mettre à jour, améliorer et autoremove

Au moment de l'écriture de ceci, la version d'Ubuntu que j'ai liée est 18.04.1

L'application liée installera la dernière version stable d'Ubuntu sur Windows.

Vous pouvez vérifier quelle version d'Ubuntu vous avez installée avec :

```
lsb_release -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*lTGgeCWKdMfOkE8WVVArWw.png)

Si vous souhaitez utiliser une version LTS spécifique d'Ubuntu, vous pouvez les obtenir depuis le Windows Store, ici :

* [Ubuntu 16.04 LTS](https://www.microsoft.com/en-gb/p/ubuntu-1604-lts/9pjn388hp8c9?activetab=pivot:overviewtab)
* [Ubuntu 18.04 LTS](https://www.microsoft.com/en-gb/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab)

Maintenant, nous allons mettre à jour et améliorer toutes les choses, les trois commandes ici mettront à jour et amélioreront tous les logiciels préinstallés qui accompagnent l'installation d'Ubuntu.

Le code ci-dessous est trois commandes jointes ensemble avec `&&`. Le drapeau `-y` est pour accepter automatiquement les changements qui vont être effectués avec les mises à jour. Auto remove supprimera les paquets inutilisés laissés par les mises à jour.

Copiez les commandes ci-dessous dans votre terminal Ubuntu, et exécutez la commande :

```
sudo apt update && sudo apt -y upgrade && sudo apt autoremove
```

> Pour passer de 16.04 à 18.04, essayez `do-release-upgrade` dans le terminal. Soyez averti que cela prend considérablement plus de temps que de simplement supprimer l'installation actuelle d'Ubuntu et de recommencer.

Maintenant que la base a été installée et mise à jour, nous devons installer le paquet [build-essential](https://packages.ubuntu.com/bionic/build-essential) afin de compiler et construire d'autres paquets, les paquets suivants que nous allons installer en auront tous besoin.

```
sudo apt install -y build-essential
```

À partir de maintenant, je suggère d'utiliser deux fenêtres bash, une avec sudo activé et l'autre avec des permissions standard.

> C'est-à-dire, ouvrez un terminal et n'entrez pas `sudo` dedans, utilisez plutôt le terminal qui a été accordé cette permission.

La raison pour laquelle je fais cela est que j'ai trouvé que si vous installez node en tant que sudo, chaque fois que vous voulez exécuter une commande `npm install`, vous devrez accorder des permissions sudo et cela peut devenir un peu fastidieux. Et vous ne devriez vraiment pas installer des paquets npm avec des permissions sudo.

### Installer Node (avec `n`)

Commençons à installer notre environnement d'exécution ! Si vous utilisez Node.js, vous aurez éventuellement des situations où vous devrez pouvoir basculer entre les versions de Node, pour cela vous avez peut-être entendu parler de nvm ([Node Version Manager](https://github.com/creationix/nvm)) que vous pouvez d'ailleurs toujours utiliser dans WSL.

La raison pour laquelle je choisis n plutôt que nvm est que dans le passé, j'ai connu des temps de démarrage lents de bash en utilisant nvm. Jetez un coup d'œil à ce [problème GitHub WSL le détaillant](https://github.com/Microsoft/WSL/issues/776) et au commentaire spécifique sur les [avantages de l'utilisation de n](https://github.com/Microsoft/WSL/issues/776#issuecomment-266112578).

D'accord, installons n, avec [n-install](https://github.com/mklement0/n-install), la commande ne commence pas par sudo, utilisez-la donc dans la fenêtre bash que vous avez sans privilèges sudo.

```
curl -L https://git.io/n-install | bash
```

Cela installera la dernière version de Node pour nous, suivez l'invite sur l'écran du terminal pour recharger bash :

```
# le mien ressemble à ceci. /home/scott/.bashrc
```

Maintenant, vérifiez les versions de Node et npm que nous avons installées avec `node -v && npm -v` dans le terminal.

### Installer Visual Studio Code

Installer VSCode ? Quoi ? Ce post est pour configurer WSL ? D'accord, alors nous allons supposer que cela part de rien pour pouvoir faire du développement web, donc nous allons avoir besoin d'un éditeur de texte, et il n'y a rien de mieux que VSCode pour l'instant, si vous avez déjà un éditeur de texte installé, passez à la partie suivante.

Installez la version Windows de VSCode depuis la [section Téléchargement](https://code.visualstudio.com/download), une fois installée, nous pouvons activer WSL dans les paramètres, le moyen le plus rapide de le faire est d'ouvrir le terminal intégré dans VSCode avec les raccourcis clavier Ctrl+' ? c'est une apostrophe. Vous serez invité à sélectionner votre terminal par défaut, sélectionnez WSL Bash.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MmMSX6VO8MBqP_4E2LR0Gg.gif)

### Installer Windows Git

Il y a un petit obstacle pour obtenir [le support Git pour VSCode](https://github.com/Microsoft/vscode/issues/9502), c'est bien documenté dans les divers problèmes mentionnés dans le problème lié.

Il y a aussi des solutions de contournement avec des choses comme [WSLGit](https://github.com/andy-5/wslgit) qui a son propre ensemble de problèmes, tout cela vient des utilisateurs (moi y compris) ne voulant pas avoir à installer un autre binaire pour Git.

J'ai essayé plusieurs variantes en ce qui concerne l'utilisation de Git avec VSCode et le chemin de moindre résistance était de mordre la balle et d'installer ce binaire supplémentaire, il y a un surcoût avec la maintenance et la configuration des clés SSH pour Windows et WSL Git mais c'est une configuration unique.

Jusqu'à ce que l'équipe VSCode incorpore [WSLGit](https://github.com/andy-5/wslgit) dans VSCode, je pense que c'est la meilleure option.

Installez depuis [git-scm.com](https://git-scm.com/download/win), le lien commencera à télécharger le binaire d'installation que vous pourrez ensuite ouvrir et passer par l'installation, vous pouvez continuer à cliquer sur suivant pendant l'installation, j'ai sélectionné quelques options que je souhaite activer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hfwe-HO8HKIEgDhyrFoxEg.gif)

Pour l'instant, c'est tout ce que nous devons faire, lorsque nous devons nous authentifier avec GitHub en utilisant SSH, nous utiliserons la ligne de commande Git Bash pour configurer le côté Windows.

### Installer un Terminal (Hyper)

Maintenant que nous avons bash sur Windows, il est temps d'installer une belle application de terminal, car, soyons honnêtes, le standard est un peu basique.

Voici [Hyper](http://hyper.is/), une application de terminal basée sur Electron qui est super thémisable et configurable.

Téléchargez et installez Hyper pour Windows, ce sera la version de base, elle ressemblera à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ikzJpOyGPcobrV5cX2VEsg.png)

Vous avez peut-être remarqué que c'est aussi l'invite de commande Windows ? ne vous inquiétez pas, nous allons le configurer tout de suite.

Ouvrez le fichier `.hyper.js` situé à la racine de votre dossier utilisateur, ou depuis Hyper lui-même, utilisez le raccourci clavier Ctrl+, pour ouvrir les paramètres.

Si le fichier de paramètres (`.hyper.js`) s'ouvre dans le Bloc-notes, vous pouvez définir le défaut pour être VSCode. Dans l'Explorateur de fichiers (utilisez la touche Windows+e pour l'ouvrir), naviguez jusqu'au fichier, il sera dans votre dossier Utilisateur, cliquez avec le bouton droit sur le fichier et sélectionnez Propriétés, puis Changez pour 'Ouvre avec :' et sélectionnez VSCode dans la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UnSMbF2YA3zzqIbyUSnweA.gif)

Maintenant, nous pouvons définir WSL comme le chemin du shell dans Hyper, ouvrez le fichier de paramètres `.hyper.js` et recherchez (Ctrl+f) bash, nous voulons ajouter le chemin vers le shell WSL dans la propriété `shell` définie dans le fichier.

```
// modifier le chemin du shell// WSL Bashshell: 'C:\\Windows\\System32\\bash.exe',
```

Nous pouvons également changer l'apparence de Hyper à partir d'ici en spécifiant la taille de la police, la famille de polices et également les thèmes prédéfinis, ajoutons rapidement le thème `hyper-adventure-time` dans la section des plugins.

Ouvrez un autre onglet Hyper avec Ctrl+Shift+t, cela affichera le terminal bash pour WSL maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RtS3O-890OE-9XmFtYViUw.gif)

Orientation rapide avec les raccourcis clavier du terminal Hyper :

* Nouveau onglet = Ctrl+Shift+t
* Fermer l'onglet actuel = Ctrl+Shift+w
* Faire défiler les onglets vers la droite = Ctrl+Shift+flèche droite
* Faire défiler les onglets vers la gauche = Ctrl+Shift+flèche gauche

Maintenant, je vais configurer quelques propriétés supplémentaires pour Hyper, et changer le thème pour quelque chose d'un peu plus subtil.

J'ai acheté Dank Mono, si vous voulez une police similaire en OSS, consultez [FiraCode](https://github.com/tonsky/FiraCode).

Voici ce que j'ai changé :

```
module.exports = {  config: {    fontSize: 18,    fontFamily: '"Dank Mono",...',    cursorShape: 'BEAM',    cursorBlink: true,    copyOnSelect: true,    plugins: ['hyper-altair']  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*IddFk0Hm5tkjZVCnNxrAKQ.gif)

### Installer Fish Shell !

D'accord, il est temps d'installer le Fish Shell ! C'est une étape complètement optionnelle, j'aime utiliser fish pour la belle intellisense que vous obtenez lorsque vous naviguez dans les structures de fichiers, il y a aussi quelques thèmes sympas que vous pouvez obtenir avec Oh My Fish.

```
sudo apt -y install fish
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*9qKRTPWbBa_JfZo2vD3dNw.gif)

### Installer Oh My Fish

Maintenant, nous pouvons installer Oh My Fish (OMF) et obtenir un beau thème de terminal, rappelez-vous que nous avons parlé d'exécuter des commandes avec les bonnes permissions ? Eh bien, c'est l'une de ces occasions, ouvrez un nouvel onglet puis collez ce qui suit :

```
curl -L https://get.oh-my.fish | fish
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*zvLCKY-M9suKN9LyvX7DgA.gif)

#### Thèmes Fish avec OMF

Après avoir installé OMF, vous pouvez choisir un thème, ici vous pouvez remarquer que le texte ne tient pas dans l'écran sur Hyper, un moyen rapide de le réinitialiser est de maximiser la fenêtre puis de la restaurer, j'ai fait cela avec la touche Windows+flèche haut pour maximiser et la touche Windows+flèche bas pour la restaurer.

Après avoir installé omf, j'ai choisi le thème agnoster, installé avec `omf install agnoster`, vous pouvez lister ce qui est disponible et ce que vous avez déjà installé en sélectionnant `omf theme`, changeons-le une fois de plus pour le thème `one`, ajustez d'abord la taille de la fenêtre car les choses deviennent un peu à l'étroit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E3wsDbXVFBcgJxf9L_jJnA.gif)

Amusez-vous, il y en a beaucoup, je préfère le thème one car vous pouvez voir quelle version de node vous utilisez, tout à droite. Ici, vous pouvez également voir l'intellisense pour fish où il montre agnoster comme une sélection précédente, si je voulais sélectionner agnoster, je pourrais utiliser la touche tab pour compléter le reste de la commande.

### Configurer

Alors, maintenant que nous avons un nouveau terminal élégant et une installation de base de VSCode, il est temps de faire avancer les choses.

J'ai un dépôt [cheat-sheets](https://github.com/spences10/cheat-sheets) détaillant une grande partie de la configuration que nous allons parcourir ici, si vous trouvez quelque chose d'utile en cours de route, n'hésitez pas à faire une PR avec la suggestion.

Tout d'abord, au lieu de taper `fish` chaque fois que j'ouvre un nouveau terminal, et sans remplacer bash que vous pouvez faire, mais je préfère utiliser un alias. Donc ce que nous allons faire, c'est ouvrir le fichier `.bashrc` et l'éditer.

Depuis un nouveau terminal, tapez `nano ~/.bashrc`, nano est un éditeur de texte bash. Faites défiler (ou Page) jusqu'en bas du fichier et ajoutez un alias pour fish, `alias f=fish` puis pour quitter nano Ctrl+x et confirmez les changements avec un `y`. Rechargez le fichier `.bashrc` comme nous l'avons fait après avoir utilisé n pour installer Node `. /home/scott/.bashrc` mais votre nom d'utilisateur à la place du mien ?, maintenant nous pouvons utiliser f au lieu de fish ! Bien joué, vous venez de vous éviter de taper trois caractères supplémentaires !!!

![Image](https://cdn-media-1.freecodecamp.org/images/1*aLZ_x9rKKrOm_Qa_GwhRZw.gif)

### Configurer Git

Avant de nous lancer dans le démarrage d'une instance Create React App, nous allons devoir configurer Git, via le fichier `.gitconfig`.

Nous allons utiliser nano pour ajouter quelques paramètres pour Git, à la fois dans WSL et Windows, c'est la configuration supplémentaire dont j'ai parlé plus tôt, désolé !

Tout d'abord, nous allons configurer notre environnement bash puis passer à Git bash sur Windows.

```
# ouvrir le fichier .gitconfig dans WSL bash# nano créera un fichier s'il n'existe pasnano ~/.gitconfig
```

C'est presque une configuration identique pour les deux environnements, à part que Windows utilise l'assistant de `manager` et WSL aura besoin de l'assistant `cache`.

```
# nécessaire dans Git Bash pour Windows[credential]  helper = manager# nécessaire dans WSL[credential]  helper = cache[color]  ui = true
```

```
[user]  name = votreNomUtilisateurGitHub  email = votreEmailGitHub@email.com
```

```
[core]  editor = code --wait
```

Appliquez vos modifications puis Ctrl+x pour quitter et confirmez avec y, c'est la première partie de la configuration Git terminée.

Dans Git Bash pour Windows, faites de même dans le terminal, utilisez nano pour créer un fichier `.gitconfig` et ajoutez le paramètre.

### Créer React App

D'accord, nous allons faire fonctionner create react app pour pouvoir configurer Git avec GitHub en utilisant SSH et commencer à apporter des modifications à commiter dans un dépôt GitHub.

Nous allons utiliser [npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) pour créer un projet React de démarrage avec Create React App. Si vous voulez avoir vos projets ailleurs, c'est le moment de naviguer vers ce répertoire.

Depuis le terminal, entrez :

```
# cela créera un projet react de démarrage# appelé create-react-appnpx create-react-app create-react-app
```

Cela crée le projet dans mon dossier home (`~`), j'ai dû accélérer le gif à 20x plus vite, cela prend un certain temps.?

Wheeeeeeeeeeeeeeeeeeeee!

![Image](https://cdn-media-1.freecodecamp.org/images/1*tf7wNkpqJ3We5Tvqem-pUQ.gif)

Alors, maintenant que nous avons démarré une application React sur laquelle travailler, nous devrions faire un changement puis l'ajouter à GitHub.

Naviguez vers le dossier create-react-app dans le terminal et ouvrez le projet. Vous pouvez ouvrir VSCode avec la commande `code .`, le `.` désigne le dossier actuel dans le terminal.

Cela ouvrira VSCode à la racine du projet create-react-app, assurez-vous que tout fonctionne comme prévu en exécutant le script de démarrage dans npm.

```
npm run start
```

Si vous voulez voir quels scripts sont disponibles dans le projet actuel, vous pouvez également utiliser `npm run` qui listera les commandes npm définies à partir du fichier `package.json`.

Une fenêtre s'ouvrira affichant la page de destination de base de Create React App, nous allons ajouter un h1 au module `App.js` puis le commiter, via le menu Contrôle de source dans VSCode.

> Veuillez noter que ceci est un guide de mise en route pour un environnement de développement, je ne vais pas détailler le développement en React

Pendant que le terminal est occupé à démarrer la page create-react-page, nous pouvons ouvrir un autre onglet dans Hyper avec Ctrl+Shift+t et ouvrir VSCode avec la commande `code .`, naviguez vers le composant `App.js` et ajoutez une balise `<h1>` juste au-dessus de la balise `<img>` avec `<h1>Hello React!</h1>` dedans.

Maintenant, la page de destination devrait montrer le h1 nouvellement ajouté, nous pouvons confirmer que le fichier est modifié dans Git en faisant un `git status` depuis le terminal. Ensuite, nous pouvons le commiter soit depuis le terminal, soit depuis l'IDE (VSCode), ma préférence est d'utiliser VSCode car la différenciation visuelle des fichiers est excellente.

Commitez les modifications avec Ctrl+Enter si vous n'avez pas sélectionné le fichier que vous souhaitez commiter, vous obtiendrez une boîte de dialogue vous indiquant qu'il n'y a pas de modifications préparées à commiter, vous pouvez sélectionner les fichiers (dans ce cas, uniquement le fichier `App.js`) en cliquant sur le plus à côté du fichier. Appuyer à nouveau sur Ctrl+Enter commiter les modifications avec un message, vous pouvez vérifier qu'il n'y a pas de modifications à commiter avec `git status` depuis le terminal ou visuellement depuis la section Contrôle de source dans VSCode.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cCt8T36jZiUVKen_4xXZqQ.gif)

D'accord, il est temps d'ajouter nos superbes modifications de code à un dépôt sur GitHub pour que le monde puisse les voir !

Ensuite, nous allons passer par l'ajout des modifications locales que nous avons faites à un dépôt GitHub. Si vous n'avez pas de compte GitHub et que vous suivez ce guide, c'est peut-être le bon moment pour en créer un.

### Utiliser SSH avec GitHub

Tout d'abord, nous allons créer un dépôt sur GitHub et pousser les modifications que nous avons faites, ici nous allons cliquer sur le bouton + en haut à droite de la page d'accueil de GitHub, entrer un nom de dépôt et GitHub vous donnera quelques options par défaut à choisir. Comme nous avons déjà fait des modifications localement, nous pouvons ignorer les premières commandes mais nous avons besoin de la commande pour ajouter le dépôt distant :

```
git remote add origin git@github.com:spences10/cra.git
```

Et pour pousser les modifications sur GitHub `git push -u origin master` mais nous allons obtenir une erreur, car nous n'avons pas configuré SSH.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TAyXd1tXaN1E5Ma_KuRcdA.gif)

### Configurer SSH WSL

Ouvrez un nouvel onglet bash dans Hyper et entrez `ls -al ~/.ssh`, vérifiez qu'il n'y a pas de fichiers `rsa` avant de faire cela.

> Vous remarquerez que nous faisons cela dans bash plutôt que dans Fish.

S'il n'y a rien, générez de nouvelles clés avec :

```
# ajoutez votre adresse email ?ssh-keygen -t rsa -b 4096 -C votreEmailGitHub@email.com 
```

Maintenant, `ls -al ~/.ssh` montrera deux fichiers supplémentaires :

```
# il devrait y avoir une paire de clés privée et publiqueid_rsaid_rsa.pub
```

Démarrez l'agent SSH :

```
eval "$(ssh-agent -s)"
```

Ajoutez la clé RSA à SSH avec :

```
ssh-add ~/.ssh/id_rsa
```

Maintenant, il est temps d'ajouter la clé SSH publique à GitHub, dans WSL, nous allons copier-coller la clé SSH publique avec `cat ~/.ssh/id_rsa.pub` dans Hyper. Ensuite, nous pouvons copier depuis Hyper vers une [nouvelle clé SSH](https://github.com/settings/ssh/new).

Enfin, authentifiez-vous avec GitHub :

```
ssh -T git@github.com
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Okoq110ALZIgf1nXhl8lRA.gif)

### Configurer SSH Windows Git Bash

Pour Windows Git Bash, nous allons copier nos clés SSH que nous venons de générer dans WSL vers Windows Git Bash, il y a quelques différences subtiles lors de l'authentification avec Windows Git Bash.

Depuis Hyper, copiez les fichiers SSH de Linux vers Windows :

```
cp ~/.ssh/* /c/Users/spenc/.ssh/
```

Démarrez l'agent SSH :

```
eval `ssh-agent -s`
```

Ajoutez la clé à l'agent SSH :

```
ssh-add ~/.ssh/id_rsa
```

Authentifiez-vous :

```
ssh -T git@github.com
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gy920dPt3_znOQJriDb2Jg.gif)

Maintenant que la configuration supplémentaire pour SSH est terminée, nous devrions pouvoir revenir à Hyper et pousser notre modification vers GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lNFc7fFKw6D8PnW5pMzajQ.gif)

De plus, vous avez peut-être remarqué que le jeton de clé SSH ? est passé du noir au vert sur l'écran des paramètres, cela indique que vous êtes authentifié.

### Changer la version de WSL

Si vous souhaitez utiliser une version différente d'Ubuntu, Debian ou l'une des autres distributions Linux disponibles dans le Windows Store avec Hyper, vous devrez changer la version par défaut depuis PowerShell :

```
# lister les versions disponibleswslconfig /l# définir par défautwslconfig /setdefault Debian
```

### Conclusion !

C'est tout ! Nous sommes passés de zéro à un environnement de développement web fonctionnel. Il y a plusieurs autres choses personnelles que je vais maintenant ajouter à mon installation, comme des alias pour Git et Fish shell. Si vous êtes intéressé par eux, j'ai une [feuille de triche pour Fish](https://github.com/spences10/cheat-sheets/blob/master/fish.md) avec une liste de tous mes alias que j'utilise, c'est la même chose pour mon `.gitconfig`, vous pouvez le trouver dans mon dépôt [dotfiles](https://github.com/spences10/dotfiles)

**Merci d'avoir lu** ?

Ceci a été initialement publié sur [mon blog Gatsby](https://blog.scottspence.me/), vous pouvez le consulter [ici](https://blog.scottspence.me/wsl-bootstrap-2019), veuillez consulter mon autre contenu si vous avez aimé ceci.

Suivez-moi sur [Twitter](https://twitter.com/ScottDevTweets) ou [Demandez-moi n'importe quoi](https://github.com/spences10/ama) sur GitHub.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).