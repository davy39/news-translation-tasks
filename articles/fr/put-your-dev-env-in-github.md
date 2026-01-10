---
title: S'il vous plaît, tout le monde, mettez tout votre environnement de développement
  dans GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/put-your-dev-env-in-github
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/put-dev-env-in-the-cloud.png
tags:
- name: Docker
  slug: docker
- name: GitHub
  slug: github
- name: Visual Studio Code
  slug: vscode
seo_title: S'il vous plaît, tout le monde, mettez tout votre environnement de développement
  dans GitHub
seo_desc: 'By Burke Holland

  Stop me if this sounds familiar...

  You want to get started with a new framework/runtime. So you install said framework/runtime.

  Then you open up the terminal and....command not found. Heavy sigh.

  You revisit the docs which suggest th...'
---

Par Burke Holland

Arrêtez-moi si cela vous semble familier...

Vous voulez commencer avec un nouveau framework/runtime. Vous installez donc ledit framework/runtime.

Puis vous ouvrez le terminal et.... commande introuvable. Soupir profond.

Vous revisitez la documentation qui suggère que vous devez apporter quelques modifications à vos paramètres de profil. Vous n'êtes pas sûr de comment faire, alors vous allez sur StackOverflow, où vous trouvez une réponse de "user92902399" qui *semble* pouvoir être légitime (qui sait), alors vous copiez et collez cela dans votre terminal et espérez que cela n'efface pas votre disque dur et n'envoie pas votre historique internet au président.

Maintenant, la commande runtime fonctionne. Mais elle échoue. L'erreur est cryptique.

Retour à Google.

Cette fois, il n'y a pas de réponse claire sur StackOverflow malgré plusieurs personnes ayant un problème similaire. Vous trouvez un problème GitHub qui semble pouvoir être lié. Quelque part au milieu d'une masse de personnes disant "Merci, cela fonctionne !" et "Cela ne fonctionne pas du tout !", quelqu'un utilise le mot "Python".

Vous vérifiez votre version de Python et, effectivement, ce framework/runtime ne supporte pas celle que vous avez installée. Vous êtes sur le point de la rétrograder lorsque vous réalisez que la dernière fois que vous avez même regardé dans la direction générale de votre installation Python, cela vous a pris une journée pour la faire fonctionner à nouveau et vous n'êtes toujours pas sûr de comment vous avez fait.

Vous savez quoi, ce nouveau framework/runtime n'est probablement pas si bon. Cela ne vaut définitivement pas tout ce tracas. Oh, regardez ! Un article de blog sur pourquoi vous ne devriez jamais utiliser les instructions ternaires. Sur quoi travailliez-vous avant ? Peu importe.

Un peu trop proche de chez vous ? C'est ce que c'est d'essayer de configurer un nouveau projet, framework ou runtime. À chaque fois. C'est en partie la raison pour laquelle chaque développeur a, à un moment donné, regardé quelqu'un avec un regard vide au milieu d'un Cheeto et a dit : "ça marche sur ma machine".

## Fonctionne sur toutes les machines

Le problème fondamental est que pour que le code fonctionne, il y a tout un environnement qui doit également être configuré correctement. C'est un problème difficile à résoudre. Ce dont nous avons besoin, c'est d'un moyen d'isoler l'environnement de développement et de l'expédier ensuite avec le code afin qu'il fonctionne sur toutes les machines. Et nous devons le faire sans avoir à expédier un système d'exploitation entier.

La clé réside dans le mot "isoler". Il s'avère que nous avons un moyen d'isoler et d'expédier des environnements entiers. Cela s'appelle "Docker". Vous pouvez créer un conteneur avec n'importe quelle configuration et ensuite l'expédier à quelqu'un d'autre. Tout ce dont vous avez besoin maintenant, c'est d'un moyen de développer dans ce conteneur comme s'il s'agissait de votre machine locale.

Vous pouvez.

Dans cet article, je vais vous montrer comment vous pouvez utiliser quelques fichiers de configuration pour emballer et expédier tout votre environnement de développement, à l'exception de votre mauvais goût pour le dubstep.

Tout cela grâce à la nouvelle [extension Dev Containers pour VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan).

Note : L'extension Dev Containers s'appelait auparavant Remote-Containers. Bien que les captures d'écran ci-dessous montrent l'ancien nom d'extension Remote-Containers, toutes les instructions devraient fonctionner de la même manière avec le nouveau nom Dev Containers.

## VS Code et Dev Containers

Le concept de base derrière [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan) est que vous spécifiez un Dockerfile qui, à son tour, spécifie toutes les dépendances nécessaires et les étapes de configuration pour obtenir le bon environnement de développement configuré. VS Code lancera ensuite ce conteneur, installera un petit serveur dedans et se connectera à votre instance VS Code. Ce que cela signifie, c'est que vous développez maintenant à l'intérieur d'un environnement préconfiguré. Mais pour vous, ce n'est que VS Code.

Pour vous montrer comment cela fonctionne, je vais créer un conteneur dans lequel développer l'API backend d'un projet sur lequel j'ai travaillé, appelé theurlist.com. Le backend de ce projet est écrit en C# et s'exécute sur [Azure Functions](https://code.visualstudio.com/tutorials/functions-extension/getting-started?WT.mc_id=freecodecamp-blog-buhollan). Pour l'exécuter localement, vous devriez installer le [runtime .NET Core](https://dotnet.microsoft.com/download?WT.mc_id=freecodecamp-blog-buhollan), le [CLI Azure Functions](https://github.com/Azure/azure-functions-core-tools) et l'[extension VS Code Azure Functions](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=freecodecamp-blog-buhollan).

La première étape consiste à installer l'[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan). Cela ajoutera une petite icône dans le coin inférieur gauche de votre VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-90.png)

Vous aurez également besoin d'avoir Docker installé. Les conteneurs Docker ne fonctionnent pas très bien si vous n'avez pas Docker. Vous pouvez télécharger la Community Edition [ici](https://docs.docker.com/install/).

Avec l'extension installée, je dois ajouter les fichiers de configuration appropriés à ce projet. Notamment un "Dockerfile" qui spécifie le conteneur dans lequel le projet sera chargé. L'extension est livrée avec un ensemble d'environnements préconfigurés. Pour en ajouter un au projet, ouvrez la Palette de commandes et sélectionnez "Dev Containers: Add Development Container Configuration Files"

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-91.png)

Ce projet utilise Azure Functions et C#, donc je vais sélectionner cette définition de conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-92.png)

Dès que je fais cela, VS Code va ajouter un dossier ".deployment" avec un "Dockerfile" et un fichier "devcontainer.json" à l'intérieur. Il va également demander immédiatement si je veux rouvrir le projet dans un conteneur. Je vais dire non et demander à VS Code de se calmer pendant une minute pendant que nous regardons ces fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-93.png)

Commençons par regarder le fichier "Dockerfile". Fichier fichier fichier.

### Configuration du Dockerfile

Le "Dockerfile" spécifie ce qui sera dans le conteneur. Si je l'ouvre, vous pouvez voir qu'il y a pas mal de choses dedans. C'est un peu verbeux. Mais nous pouvons analyser les parties importantes.

La première chose qu'il fait est de récupérer la dernière version du SDK .NET Core.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-94.png)

Ensuite, il installe quelques utilitaires dans le conteneur. Plus précisément, il installe...

* Git (Contrôle de source)
* procps (utilitaire d'inspection de processus)
* curl (utilitaire HTTP)
* apt-transport-https (utilitaire HTTPS)
* gnupg2 (un outil de chiffrement)
* lsb-release (imprime des informations spécifiques à Linux)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-95.png)

Tout cela est destiné à créer un environnement qui possède tous les outils obscurs dont un développeur pourrait avoir besoin pour exécuter ce projet et pouvoir le vérifier et le sortir du contrôle de source.

Ensuite, il installe les outils principaux d'Azure Functions. Il configure tous les emplacements de dépôt nécessaires avant l'installation. Ce sont toutes des choses qu'un développeur devrait faire lui-même avant de pouvoir exécuter ce projet.

L'autre fichier dans le dossier ".devcontainer" est le fichier "devcontainer.json".

### Le fichier devcontainer.json

Ce fichier spécifie quelques paramètres supplémentaires pour l'environnement de développement à distance. Plus précisément....

1. Il spécifie que le "Dockerfile" doit être utilisé pour construire le conteneur

2. Il s'assure que le port "7071" est transféré depuis le conteneur afin qu'il puisse être accessible à "localhost:7071". C'est le port sur lequel Azure Functions s'exécute localement.

3. Il spécifie toutes les extensions qui doivent être installées dans le conteneur. Puisque vous n'utilisez pas vraiment VS Code localement, vos extensions ne sont pas toutes installées automatiquement. Les spécifier dans ce fichier garantit qu'elles sont présentes lorsque le projet est ouvert.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-96.png)

Et avec cela, nous pouvons ouvrir la Palette de commandes et sélectionner "Dev Containers: Reopen folder in container".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-98.png)

VS Code se rechargera et se mettra à construire le conteneur pour ce projet.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-100.png)

La première fois qu'il le fait, cela prend une minute ou deux car les images de base doivent être téléchargées et construites. Après la première fois, les chargements suivants sont beaucoup plus rapides car l'image existe déjà sur votre machine.

Dans le cas de ce projet, une fois le conteneur construit, VS Code se met à restaurer les dépendances C# ce qui est fait avec l'extension C# qui était incluse dans le fichier de configuration "devcontainer.json".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-105.png)

Quand tout est terminé, je peux exécuter ce projet simplement en appuyant sur F5. Et juste comme ça, l'application est opérationnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-110.png)

Pensez à ce que nous aurions dû faire pour configurer cela localement...

1. Installer .NET Core
2. Installer les outils principaux de Functions
3. Installer l'extension VS Code Functions
4. Installer l'extension VS Code C#

Avec Dev Containers, rien de tout cela n'est nécessaire. Nous pouvons configurer et expédier un environnement de développement entier en **deux fichiers texte**.

### S'il vous plaît, mettez votre environnement de développement dans GitHub

Voici donc ma modeste supplique : au lieu de décrire 15 étapes dans un README GitHub pour configurer votre projet pour qu'il s'exécute, **mettez tout votre environnement de développement dans GitHub**. Cela signifie vérifier ce dossier ".devcontainers". Si un développeur utilisant votre projet n'a pas VS Code ou l'extension Dev Containers, rien ne se passe. Vous ne pouvez pas perdre.

Je suis excité car j'ai l'impression que les jours de l'enfer de la configuration touchent à leur fin. Et en plus, pensez à toutes les personnes que nous sauverons des articles dogmatiques sur les instructions ternaires.

### Plus sur le développement avec des conteneurs

* [Développer à l'intérieur d'un conteneur](https://code.visualstudio.com/docs/remote/containers?WT.mc_id=freecodecamp-blog-buhollan)
* [Extension Dev Containers de VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan)
* [Configuration avancée des conteneurs](https://code.visualstudio.com/docs/remote/containers-advanced?WT.mc_id=freecodecamp-blog-buhollan)