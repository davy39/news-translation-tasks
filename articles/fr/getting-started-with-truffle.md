---
title: Apprendre Truffle et Ganache – Comment créer et déployer un Smart Contract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-20T16:08:22.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-truffle
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/ff-2.png
tags:
- name: Blockchain
  slug: blockchain
- name: Smart Contracts
  slug: smart-contracts
seo_title: Apprendre Truffle et Ganache – Comment créer et déployer un Smart Contract
seo_desc: "By Jagruti Tiwari\nLearning a new technology often means learning a new\
  \ framework, programming language, IDE, or deployment method. And the blockchain\
  \ is no different. \nIn this tutorial, I am going to show you how to get started\
  \ with Truffle, a Node.j..."
---

Par Jagruti Tiwari

Apprendre une nouvelle technologie signifie souvent apprendre un nouveau framework, un nouveau langage de programmation, un nouvel IDE ou une nouvelle méthode de déploiement. Et la blockchain ne fait pas exception. 

Dans ce tutoriel, je vais vous montrer comment commencer avec [Truffle](https://trufflesuite.com/docs/vscode-ext/installation-guide/), un framework blockchain pour Node.js, dans Visual Studio Code.

# Comment installer Truffle
Pour installer Truffle, vous devez avoir [Node et NPM](https://nodejs.org/en/download/) ainsi que [Python](https://www.python.org/downloads/) installés sur votre machine. 

Si vous ne les avez pas déjà, vous pouvez les installer depuis leurs sites officiels ([Node](https://nodejs.org/en/) et [Python](https://www.python.org/)). Une fois que c'est fait, vous êtes prêt à installer Truffle.

Nous allons utiliser npm pour installer Truffle. Entrez la commande suivante dans votre invite de commande :

`npm install -g truffle`

![Screenshot-2022-07-16-190328](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-190328.png)

Pendant l'installation, si vous rencontrez l'erreur suivante, je vous ai couvert :

`gyp ERR! stack Error: Could not find any Visual Studio installation to use`

Google propose plusieurs solutions pour cette erreur. Ce qui a fonctionné pour moi, c'est d'installer [Visual Studio](https://visualstudio.microsoft.com/downloads/) avec 'Desktop Development with C++'.

Après avoir téléchargé Visual Studio et lancé l'installateur, vous verrez l'écran suivant :

![Screenshot-2022-07-16-190639](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-190639.png)

Dans la section 'Desktop and mobile', cochez 'Desktop Developement with C++' et continuez le processus d'installation.

Une fois cela fait, vous pouvez relancer la commande d'installation de Truffle.

Pour vérifier si Truffle est installé avec succès, exécutez :

`truffle version` 

dans votre invite de commande. Vous devriez voir un résultat similaire à l'image ci-dessous :

![Screenshot-2022-07-17-201823](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-201823.png)

Félicitations ! Vous avez installé Truffle.

# Comment utiliser Truffle dans Visual Studio Code 

Visual Studio Code dispose de sa propre extension pour Truffle. Nous allons l'installer pour faciliter notre travail. 

![Screenshot-2022-07-16-191633](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-191633.png)

Dans la barre de recherche du marketplace, tapez "Truffle for VS Code" et cliquez sur installer (similaire à l'image ci-dessous).

![Screenshot-2022-07-16-191836](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-191836.png)

VS Code nécessite d'autres extensions pour fonctionner, alors vérifiez celles que vous n'avez pas installées et continuez la configuration :
![Untitled](https://www.freecodecamp.org/news/content/images/2022/07/Untitled.png)

Si vous ne voyez pas le logo Truffle dans la barre de gauche, vous devrez peut-être redémarrer VS Code.

# Comment configurer Ganache dans VS Code
Ganache fait partie de la suite Truffle pour déployer des DApps. 

Cliquez sur 'Networks' > 'Create a new network' dans l'explorateur Truffle.

![Screenshot-2022-07-16-195911](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-195911.png)

Dans la liste déroulante, sélectionnez 'Ganache service'. 

![Screenshot-2022-07-16-195943](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-195943.png)

Sélectionnez le type 'local' ou 'fork'. Comme il s'agit d'une configuration locale, je vais sélectionner 'local'.

![Screenshot-2022-07-16-200019](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200019.png)

Ensuite, vous serez invité à entrer le 'nom de votre projet local'. Entrez un nom de votre choix et appuyez sur Entrée. 

![Screenshot-2022-07-16-200046](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200046.png)

Votre configuration réseau est terminée. 

![Screenshot-2022-07-16-200242](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200242.png)

Pour démarrer le réseau, faites un clic droit sur le nom du réseau et cliquez sur 'Start Ganache'.

Lorsque vous démarrez le service Ganache, vous verrez une sortie en ligne de commande comme suit :
![Screenshot-2022-07-16-200504](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-200504.png)

La sortie affiche un ensemble de choses à accélérer. Nous n'avons pas besoin de nous en soucier pour l'instant. 

# Comment démarrer un projet Truffle
Pour démarrer un projet dans Truffle, allez dans un répertoire et tapez la commande init.

`truffle init`

![Screenshot-2022-07-16-193451](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-193451.png)

Cela créera un nouveau projet Truffle.

# Comment créer un contrat dans Truffle
La commande suivante crée un contrat dans Truffle :

`truffle create contract <nom-du-contrat>`

![Screenshot-2022-07-16-202855](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-16-202855.png)

Ici, nous avons créé un contrat nommé 'SimpleStorage'.

# Comment exécuter des tests dans Truffle
Pour exécuter des tests dans Truffle, entrez simplement cette commande :

`truffle test` 

![Screenshot-2022-07-17-171254](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-171254.png)

Tous les tests seront exécutés un par un.
# Comment déployer dans Truffle

Nous allons utiliser Ganache pour déployer dans Truffle. 

`truffle develop` 

Vous utilisez la commande ci-dessus pour démarrer le processus de déploiement.

Ganache a des comptes et des clés privées prêts à cet effet.

![Screenshot-2022-07-17-171755](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-171755.png)

Dans l'image ci-dessus, en bas, vous verrez la console `truffle (develop)>`.

![Screenshot-2022-07-17-172106](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-172106.png)

Tapez `migrate --reset` dans la console.

![Screenshot-2022-07-17-172204](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-17-172204.png)

Vous verrez que les migrations initiales sont effectuées et que le processus de déploiement commence. À la fin, vous obtiendrez un résumé (le coût et le nombre de déploiements) du déploiement.

# Conclusion
Nous progressons plus rapidement lorsque nous pouvons apprendre des erreurs des autres. Je viens de commencer à apprendre la blockchain, et il m'a fallu un certain temps pour faire fonctionner la configuration. Alors voici mes découvertes. Bon apprentissage !