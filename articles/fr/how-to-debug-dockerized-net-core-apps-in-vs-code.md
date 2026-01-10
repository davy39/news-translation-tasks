---
title: Comment déboguer des applications .NET Core dockerisées dans VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-08T15:34:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-dockerized-net-core-apps-in-vs-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/debug_dockerized_dotnet_core_apps-1.png
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: .NET
  slug: net
- name: Visual Studio Code
  slug: vscode
seo_title: Comment déboguer des applications .NET Core dockerisées dans VS Code
seo_desc: 'By Haseeb Ahmed

  I recently switched to VS Code for development of a dockerized .NET core app. But
  I then realized that there weren''t many up-to-date articles about debugging dockerized
  .NET core applications in VS Code.


  Source: GIPHY

  So, here I am, ...'
---

Par Haseeb Ahmed

J'ai récemment basculé vers VS Code pour le développement d'une application .NET Core dockerisée. Mais j'ai alors réalisé qu'il n'y avait pas beaucoup d'articles à jour sur le débogage d'applications .NET Core dockerisées dans VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-217.png)
_Source : GIPHY_

Alors, me voilà, en train d'écrire cet article. J'espère qu'il aidera d'autres personnes comme moi à déboguer leurs applications .NET Core dockerisées dans VS Code. 

Dans cet article, nous allons discuter des points suivants :

1. Extensions VS Code pour Docker
2. Configurations de lancement de VS Code
3. Comment déboguer des applications .NET Core sur votre Docker local

# Extensions VS Code pour Docker

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-218.png)

Bien qu'aucune extension ne soit vraiment nécessaire (pour vous, minimalistes chevronnés) pour déboguer des applications .NET Core conteneurisées, je recommande tout de même d'installer l'[extension Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) de Microsoft. Elle facilitera la création, la gestion et le débogage d'applications conteneurisées directement depuis VS Code. 

Franchement, depuis que j'ai commencé à utiliser cette extension, je n'utilise plus Docker Desktop.

# Configurations de lancement de VS Code

Maintenant, afin de déboguer des applications .NET Core dockerisées, nous devrons créer une configuration de lancement VS Code. 

Dans cette section, je vais parler de deux types de configurations de lancement : une pour `docker run` et l'autre pour `docker compose`. 

Plus tard, nous examinerons également les configurations de lancement finales et les comprendrons afin de savoir ce que nous faisons.

## Configuration de lancement Docker Run

Si vous avez installé l'extension Docker de Microsoft, cela devrait être facile.

Tout d'abord, appuyez sur "Ctrl + P" dans VS Code et tapez `> Docker:`

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-221.png)

Ensuite, sélectionnez "Docker : Initialiser pour le débogage Docker".

Puis sélectionnez ".NET : ASP.NET Core" comme plateforme de votre application. Sélectionnez "Linux" comme système d'exploitation.

Et voilà ! Vous devriez maintenant avoir une configuration de lancement "Docker .NET Core Launch".

Notez que l'extension Docker voudra écraser votre dockerfile existant. Si vous ne le permettez pas, elle ne créera pas les configurations de lancement. Je recommande de sauvegarder votre dockerfile, de laisser l'extension l'écraser, puis de restaurer votre fichier original.

## Configurations de lancement Docker Compose

Nous savons tous que les applications réelles ne sont jamais aussi simples ! Vous aurez probablement un conteneur de base de données, un conteneur d'application et quelques autres conteneurs tous connectés ensemble via une configuration docker-compose. 

Si c'est le cas, voici comment vous créerez vos configurations de lancement.

Tout d'abord, ouvrez votre espace de travail dans VS Code. Si vous avez déjà des configurations de lancement existantes, vous pouvez sauter la partie suivante.

Ensuite, appuyez sur "Ctrl + Shift + D" pour passer à l'onglet "Exécuter et déboguer".

Cliquez sur "créer un fichier launch.json" et choisissez ".NET 5+ et .NET Core" (cela créera une configuration de lancement de base pour exécuter votre application sans Docker).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-222.png)

Maintenant, alors que votre fichier launch.json est ouvert, cliquez sur le bouton Ajouter une configuration dans le coin inférieur droit de l'éditeur.

Sélectionnez "Docker : .NET Core Attach (Preview)" dans la liste déroulante ouverte.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-229.png)

Cela devrait avoir ajouté une nouvelle configuration appelée "Docker : .NET Core Attach (Preview)".

Et voilà ! Vous êtes maintenant prêt à déboguer votre application .NET Core dockerisée dans VS Code.

## Comment comprendre les configurations de lancement

Avant de commencer à déboguer notre application, examinons les configurations de lancement de plus près pour comprendre comment elles fonctionnent. 

Il devrait y avoir deux fichiers dans le dossier .vscode, à la racine de votre espace de travail. 

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "docker-build",
            "label": "docker-build: debug",
            "dependsOn": [
                "build"
            ],
            "dockerBuild": {
                "tag": "webapi:dev",
                "target": "base",
                "dockerfile": "${workspaceFolder}/src/Dockerfile",
                "context": "${workspaceFolder}",
                "pull": true
            },
            "netCore": {
                "appProject": "${workspaceFolder}/src/webapi.csproj"
            }
        },
        {
            "type": "docker-run",
            "label": "docker-run: debug",
            "dependsOn": [
                "docker-build: debug"
            ],
            "dockerRun": {},
            "netCore": {
                "appProject": "${workspaceFolder}/src/webapi.csproj",
                "enableDebugging": true
            }
        }
    ]
}
```

Tout d'abord, examinons le fichier tasks.json. Ce fichier contient une liste de tâches qui peuvent être requises par certaines des configurations de lancement pour lancer correctement l'application.

La tâche que nous voulons examiner est "docker-run: debug". C'est la tâche appelée lorsque vous lancez en utilisant la configuration "Docker .NET Core Launch" (comme nous le verrons plus tard).

Cette tâche a trois propriétés que nous devons comprendre :

* netCore.appProject : Cette propriété est spécifique aux applications .NET Core et pointe simplement vers le fichier de projet de votre application.
* netCore.enableDebugging : Il s'agit d'une autre propriété spécifique aux applications .NET Core qui indique à VS Code de lancer l'application avec des capacités de débogage.
* dependsOn : Il s'agit d'une propriété générique qui définit si une tâche dépend d'autres tâches pour son exécution.

Deuxièmement, nous devons comprendre ce que fait la tâche "docker-build: debug". 

En plus des propriétés netCore et dependsOn, elle possède un objet dockerBuild qui contrôle la commande `docker build` exécutée par VS Code pour lancer une application docker run. 

Les propriétés de l'objet dockerBuild sont assez similaires aux arguments que vous passez à la commande `docker build`.

Vous pouvez lire à propos de toutes les propriétés de l'objet dockerBuild [ici](https://code.visualstudio.com/docs/containers/reference#_dockerbuild-object-properties) et des tâches en général [ici](https://code.visualstudio.com/docs/editor/tasks).

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Docker .NET Core Attach",
      "type": "docker",
      "request": "attach",
      "platform": "netCore",
      "sourceFileMap": {
        "/src": "${workspaceFolder}/src"
      }
    },
    {
      "name": "Docker .NET Core Launch",
      "type": "docker",
      "request": "launch",
      "preLaunchTask": "docker-run: debug",
      "netCore": {
        "appProject": "${workspaceFolder}/src/webapi.csproj"
      }
    }
  ]
}
```

Maintenant, examinons le fichier launch.json où se trouvent toutes les configurations de lancement. 

Bien que la plupart de ces propriétés soient standard, celle qui nous intéresse est "sourceFileMap" dans la configuration "Docker .NET Core Attach". 

Afin de déboguer des applications .NET Core qui ont été construites sur une machine autre que la machine VS Code (dans ce cas, un Docker), VS Code doit comprendre comment mapper votre espace de travail actuel vers la hiérarchie de la machine de construction. 

Par exemple, si mon projet a été construit à partir du dossier "/src" sous Linux, cette propriété indiquera à VS Code de remplacer "/src" par "${workspaceFolder}/src" dans tous les chemins de fichiers. Dans le cas où ce mappage est incorrect, VS Code atteindra le point d'arrêt mais donnera une erreur indiquant que le fichier (en cours de débogage) n'existe pas.

Vous pouvez lire plus de détails sur les propriétés de launch.json [ici](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes).

# Comment déboguer des applications .NET Core sur votre Docker local

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-230.png)

## Docker Run

Maintenant que nous avons compris les configurations de lancement, cela devrait être facile ! Suivez simplement les étapes ci-dessous.

Tout d'abord, appuyez sur "Ctrl + Shift + D" pour passer à l'onglet "Exécuter et déboguer".

Ensuite, choisissez "Docker .NET Core Launch" et appuyez sur l'icône de lecture verte pour déboguer.

## Docker Compose

Le débogage d'un conteneur Docker Compose est légèrement différent. Vous devrez vous assurer que vos conteneurs Docker Compose sont déjà en cours d'exécution avant d'attacher le débogueur VS Code. 

Une fois qu'ils sont démarrés, suivez ces étapes :

Tout d'abord, appuyez sur "Ctrl + Shift + D" pour passer à l'onglet "Exécuter et déboguer".

Ensuite, choisissez "Docker : .NET Core Attach (Preview)" et appuyez sur l'icône de lecture verte pour déboguer.

C'est tout ! J'espère que vous avez trouvé cela utile. Si vous avez des questions ou si quelque chose n'est pas clair, vous pouvez me contacter ou consulter le projet exemple sur [GitHub](https://github.com/thehaseebahmed/vscode-dotnet-docker-debug).

Bon codage !

Cet article fait partie de ma [série de codage](https://blog.thehaseebahmed.com/series/coding). Vous y trouverez également d'autres articles utiles pour votre développement quotidien.