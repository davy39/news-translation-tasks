---
title: Comment installer Node.js sur Ubuntu – Guide d'installation de Node Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-10-20T19:29:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-on-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/programming-development-technology-work-at-night-2022-01-19-00-14-46-utc-1.jpg
tags:
- name: Linux
  slug: linux
- name: node
  slug: node
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Node.js sur Ubuntu – Guide d'installation de Node Linux
seo_desc: "If you are a web developer working on the frontend or the backend, you'll\
  \ want to have Node.js installed on your system. \nBut if you use the typical sudo\
  \ apt install nodejs command, it may install a very old version of Node which can\
  \ be troublesome f..."
---

Si vous êtes un développeur web travaillant sur le frontend ou le backend, vous voudrez avoir **Node.js** installé sur votre système. 

Mais si vous utilisez la commande typique `sudo apt install nodejs`, elle peut installer une version très ancienne de Node, ce qui peut être problématique pour vous.

Vous voudrez donc installer une version spécifique, ce qui nécessite une commande différente. Cela installera la version LTS (Long-Term Support) de Node, utile pour les développeurs car elle bénéficie d'une période de support plus longue.

Aujourd'hui, je vais vous montrer comment installer la dernière version LTS de Node sur votre système d'exploitation Ubuntu.

Ce processus fonctionnera sur tout type de système d'exploitation Linux basé sur Debian (Ubuntu, Mint, Zorin, Debian, Elementary OS, etc.). Il fonctionnera que vous l'utilisiez comme système d'exploitation principal, secondaire en dual boot, WSL sur Windows, ou dans une machine virtuelle (VMware Workstation, VirtualBox, etc.).

## Tutoriel Vidéo

J'ai également créé une vidéo complète pour vous montrer le processus étape par étape. Vous pouvez la regarder ici :

%[https://www.youtube.com/watch?v=g4Enhyn1o-4]

Au moment de la rédaction de cet article, la dernière version LTS pour Node est la 18.18.2.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-141242.png)
_Page de téléchargement de Node montrant la version LTS actuelle_

Lorsque vous installez Node en suivant les instructions de cet article, il installera automatiquement la dernière version LTS de Nodejs. Vous serez donc en sécurité sans aucun tracas si vous suivez simplement cet article et la vidéo qui l'accompagne.

## Mettre à jour votre système d'exploitation

Tout d'abord, vous voudrez vous assurer que vous avez installé toutes les mises à jour au préalable. J'aime travailler principalement dans le terminal, donc je vais installer les mises à jour directement via le terminal.

Pour mettre à jour vers les dernières versions de tous les packages pertinents, utilisez `sudo apt update` dans le terminal. Utilisez votre mot de passe lorsqu'il vous le demande.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-104647.png)
_Mise à jour de tous les packages pertinents_

Utilisez maintenant `sudo apt upgrade -y` pour mettre à niveau tous les packages pouvant être mis à niveau.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-120347.png)
_Mise à niveau de tous les packages pertinents_

## Installer CURL

Nous utilisons ici le **Node Version Manager (NVM)** pour installer Node. Il y a divers avantages à installer Node et npm en utilisant NVM, car il nous permet également de gérer plusieurs versions de Node.js sur notre système.

Tout d'abord, vous devrez installer `curl` s'il n'est pas déjà installé sur votre système. Vous pouvez installer curl en utilisant la commande suivante :

```bash
sudo apt install curl -y
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122355.png)
_Installation de CURL_

## Comment installer Node.js

Vous devrez maintenant suivre ces étapes pour vous assurer d'avoir installé Node.js avec succès sur votre système.

### Installer Node Version Manager (NVM)

Installez le Node Version Manager (NVM) en utilisant la commande suivante :

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122423.png)
_Installation du Node Version Manager (NVM)_

Lorsque vous exécutez cette commande spécifique, curl télécharge le script d'installation de NVM depuis cette URL spécifique. Ensuite, bash exécute le même script pour installer NVM.

### Activer NVM

Activez NVM en utilisant la commande suivante :

```bash
source ~/.bashrc
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122517.png)
_Activation du Node Version Manager (NVM)_

### Installer la dernière version LTS de Node

Installez la dernière version Long Term Support de Node en utilisant la commande suivante :

```bash
nvm install --lts
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122656.png)
_Commande pour installer la dernière version LTS de Node.js_

Elle installe par défaut la dernière version de la version LTS de Node.

### Définir la version LTS par défaut comme NVM

Nous avons installé la dernière version LTS de Node, mais nous devons également définir la version par défaut de NVM afin qu'elle soit utilisée par défaut chaque fois que nous en avons besoin. Vous pouvez utiliser la commande suivante pour cela. Assurez-vous de changer la version pour la version LTS exacte que vous venez d'installer sur votre système.

```bash
nvm alias default 18.18.2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122842.png)
_Sélection de la version appropriée de Node comme version par défaut_

Si votre version LTS est quelque chose comme `24.1.2`, la commande serait comme ci-dessous :

```bash
nvm alias default 24.1.2
```

### Confirmer que Node a été installé

Utilisez la commande suivante pour vérifier si la version par défaut est bien la version que vous venez d'installer :

```bash
node -v npm -v
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122937.png)
_Affichage de la version actuelle de Node installée_

## Comment configurer l'environnement Node.js

Après avoir installé Node et NPM, vous devez configurer l'environnement Node en créant un nouveau projet Node.

Utilisez la commande suivante pour créer un nouveau répertoire/dossier où vous souhaitez tester un projet Node simple de type "Hello World".

```bash
mkdir my-node-project
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123101.png)
_Création d'un nouveau répertoire/dossier pour tester un programme simple "Hello World" sur Node_

Accédez au répertoire `my-node-project` en utilisant la commande suivante :

```bash
cd my-node-project
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123148.png)
_Changement de répertoire pour entrer dans ce répertoire/dossier nouvellement créé_

Initialisez le nouveau projet Node comme ceci :

```bash
npm init -y
```

Cette commande créera un fichier "package.json" contenant les métadonnées et les dépendances de votre projet. Voici la sortie JSON :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123304-1.png)
_Initialisation de npm dans le dossier_

La sortie JSON est la suivante :

```json
{
  "name": "my-node-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Maintenant, exécutez la configuration avec la commande simple. Pour cela, je vais créer un nouveau fichier appelé `app.js` en utilisant l'éditeur de texte **nano** dans le terminal.

```bash
sudo nano app.js
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123550.png)
_Ouverture du fichier app.js dans nano_

Une fois l'éditeur de texte ouvert, tapez le code suivant :

```bash
console.log("Bonjour, Node.js depuis Ubuntu !");
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123710.png)
_Écriture d'un simple code console.log dans le fichier app.js en utilisant nano_

Utilisez `Ctrl` + `O` pour enregistrer le fichier. Utilisez `Entrée` pour enregistrer le fichier sous `app.js` :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123831.png)
_Enregistrement du fichier app.js avec la nouvelle ligne de code ajoutée_

Utilisez `Ctrl` + `X` pour revenir au terminal bash.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123907.png)
_Retour au terminal_

Maintenant, il est temps de vérifier la sortie et de voir si cela fonctionne ou non.

Utilisez la commande suivante :

```bash
node app.js
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-124010.png)
_Exécution du fichier app.js en utilisant Node_

Cela fonctionne !

Nous avons réussi à installer la dernière version LTS de Node sur notre système d'exploitation Linux basé sur Ubuntu/Debian.

Santé ! 🍂

## Conclusion

Merci beaucoup d'avoir lu l'article entier jusqu'à présent.

Si vous avez apprécié les procédures étape par étape, n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de vérifier [mon site web](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) également !

Si vous aimez regarder des vidéos sur la programmation et la technologie, vous pouvez également consulter ma [chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1).

Je vous souhaite tout le meilleur pour votre parcours en programmation et en développement. 😊

Vous pouvez le faire ! Ne abandonnez jamais, jamais ! 💔