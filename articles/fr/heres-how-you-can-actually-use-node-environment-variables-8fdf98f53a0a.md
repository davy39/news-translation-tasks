---
title: Voici comment utiliser réellement les variables d'environnement Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T06:17:53.000Z'
originalURL: https://freecodecamp.org/news/heres-how-you-can-actually-use-node-environment-variables-8fdf98f53a0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*akTd5oP32aXargVxiCOB8g.png
tags:
- name: humor
  slug: humor
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Voici comment utiliser réellement les variables d'environnement Node
seo_desc: 'By Burke Holland

  Environment variables are a fundamental part of Node development, but for some reason
  I never bothered with learning how to properly use them.

  Maybe because they are called “Environment Variables.”

  Just the words “Environment Variabl...'
---

Par Burke Holland

Les variables d'environnement sont une partie fondamentale du développement Node, mais pour une raison quelconque, je ne me suis jamais donné la peine d'apprendre à les utiliser correctement.

Peut-être parce qu'elles sont appelées « Variables d'Environnement ».

Les simples mots « Variable d'Environnement » déclenchent un flashback chargé de PTSD dans lequel j'essaie d'ajouter le bon chemin au répertoire Java Home sous Windows. Est-ce qu'il va dans PATH ou JAVA_HOME ou les deux ? Dois-je le terminer par un point-virgule ? POURQUOI J'UTILISE JAVA ?

![Image](https://cdn-media-1.freecodecamp.org/images/ALjN6DcPA7VdZAcLA1vpTCzYLdx1lU3NtbOW)
_TUE_MOI_

Dans Node, les variables d'environnement peuvent être globales (comme sous Windows), mais sont souvent utilisées avec un processus spécifique que vous souhaitez exécuter. Par exemple, si vous aviez une application web, vous pourriez avoir des variables d'environnement qui définissent :

* Le port HTTP à écouter
* La chaîne de connexion à la base de données
* Le JAVA_HOME… attendez… non — désolé. Le processus de guérison prend du temps.

Dans ce contexte, les variables d'environnement sont vraiment plus comme des « Paramètres de Configuration ». Voyez comme cela sonne mieux ?

Si vous avez déjà fait du .NET, vous pourriez être familier avec quelque chose comme un fichier `web.config`. Les variables d'environnement Node fonctionnent de la même manière que les paramètres dans un `web.config` — ce sont un moyen pour vous de passer des informations que vous ne voulez pas coder en dur.

![Image](https://cdn-media-1.freecodecamp.org/images/lPJ7qP4TxdCmfuP6yYy5vnHuoUa8WH23RSqh)
_Se citer soi-même est le sommet de l'illusion_

Mais comment utilisez-vous ces variables dans votre application Node ? J'ai eu du mal à trouver de bonnes ressources sur ce sujet avec la quantité requise de blagues sur Java, alors j'ai décidé d'en créer une. Voici quelques-unes des différentes façons dont vous pouvez définir et ensuite lire les variables d'environnement dans vos applications Node.

#### Passez-le dans le terminal

Vous pouvez passer des variables d'environnement dans le terminal dans le cadre de votre processus Node. Par exemple, si vous exécutiez une application Express et que vous souhaitiez passer le port, vous pourriez le faire comme ceci…

```bash
PORT=65534 node bin/www
```

Fait amusant : le port 65535 est la plus grande valeur de réseau TCP/IP disponible. Comment le sais-je ? [StackOverflow bien sûr](https://stackoverflow.com/questions/113224/what-is-the-largest-tcp-ip-network-port-number-allowable-for-ipv4). Comment quelqu'un sait-il quoi que ce soit ? Mais vous ne pouvez aller que jusqu'au port 65534 pour une application web car c'est le port le plus élevé auquel Chrome se connectera. Comment le sais-je ? Parce que [Liran Tal](https://www.freecodecamp.org/news/heres-how-you-can-actually-use-node-environment-variables-8fdf98f53a0a/undefined) me l'a dit dans les commentaires. Vous devriez le suivre. Entre nous deux, c'est lui qui sait ce qu'il fait.

Maintenant, pour utiliser la variable dans votre code, vous utiliseriez l'objet `process.env`.

```js
var port = process.env.PORT;
```

Mais cela pourrait devenir moche. Si vous aviez une chaîne de connexion, vous ne voudriez probablement pas commencer à passer plusieurs variables dans le terminal. Cela ressemblerait à de l'accumulation de valeurs de configuration, et quelqu'un qui vous aime pourrait organiser une intervention et cela serait gênant pour tout le monde impliqué.

```
PORT=65534
DB_CONN="mongodb://react-cosmos-db:swQOhAsVjfHx3Q9VXh29T9U8xQNVGQ78lEQaL6yMNq3rOSA1WhUXHTOcmDf38Q8rg14NHtQLcUuMA==@react-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
SECRET_KEY="b6264fca-8adf-457f-a94f-5a4b0d1ca2b9"
```

Cela ne s'adapte pas, et tout le monde veut s'adapter. Selon chaque architecte avec qui j'ai déjà été en réunion, « s'adapter » est plus important que le fait que l'application fonctionne même.

Alors regardons une autre façon : les fichiers .env.

#### Utiliser un fichier .env

Les fichiers .env vous permettent de mettre vos variables d'environnement à l'intérieur d'un fichier. Vous créez simplement un nouveau fichier appelé `.env` dans votre projet et vous y mettez vos variables sur différentes lignes.

```
PORT=65534

DB_CONN="mongodb://react-cosmos-db:swQOhAsVjfHx3Q9VXh29T9U8xQNVGQ78lEQaL6yMNq3rOSA1WhUXHTOcmDf38Q8rg14NHtQLcUuMA==@react-cosmos-db.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"

SECRET_KEY="b6264fca-8adf-457f-a94f-5a4b0d1ca2b9"
```

Pour lire ces valeurs, il y a quelques options, mais la plus facile est d'utiliser le package `dotenv` de npm.

```bash
npm install dotenv --save
```

Ensuite, vous n'avez qu'à requérir ce package dans votre projet partout où vous avez besoin d'utiliser des variables d'environnement. Le package `dotenv` récupérera ce fichier et chargera ces paramètres dans Node.

```js
Utilisez dotenv pour lire les variables .env dans Node
require('dotenv').config();
var MongoClient = require('mongodb').MongoClient;

// Référencez les variables .env à partir de l'objet process.env
MongoClient.connect(process.env.DB_CONN, function(err, db) {
  if(!err) {
    console.log("Nous sommes connectés");
  }
});
```

ASTUCE : Ne vérifiez pas votre fichier `.env` dans Github. Il contient tous vos secrets et Github vous enverra un email pour vous le dire. Ne soyez pas comme moi.

OK — Bien. Mais c'est un peu pénible. Vous devez mettre cela dans chaque fichier où vous voulez utiliser des variables d'environnement ET vous devez déployer `dotenv` en production où vous n'en avez pas vraiment besoin. Je ne suis pas un grand fan de déployer du code inutile, mais je suppose que je viens de décrire toute ma carrière.

Heureusement, vous utilisez [VS Code](https://code.visualstudio.com/?wt.mc_id=dotenv-medium-buhollan) (parce que **bien sûr que vous l'utilisez**), donc vous avez d'autres options.

#### Travailler avec des fichiers .env dans VS Code

Tout d'abord, vous pouvez [installer l'extension DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&wt.mc_id=dotenv-medium-buhollan) pour le code qui vous donnera une belle coloration syntaxique dans vos fichiers .env.

[**DotENV - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)  
[_Extension pour Visual Studio Code - Support pour la syntaxe des fichiers dotenv_](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)  
[marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv&WT.mc_id=dotenv-medium-buhollan)

![Image](https://cdn-media-1.freecodecamp.org/images/5TqqPI4CyihReGrXCaFqLDEAADqD-AJtHS4Y)

Le débogueur VS Code offre également des options plus pratiques pour charger des valeurs à partir de fichiers .env **si** vous utilisez le débogueur VS Code.

#### Configurations de lancement de VS Code

Le débogueur Node pour VS Code (déjà présent, pas besoin d'installer quoi que ce soit) prend en charge le chargement de fichiers .env via des configurations de lancement. Vous pouvez en lire plus sur les configurations de lancement [ici](https://code.visualstudio.com/docs/nodejs/nodejs-debugging?WT.mc_id=dotenv-medium-buhollan).

![Image](https://cdn-media-1.freecodecamp.org/images/f6NKkdg6vZOubtIzh4k4EGEVUWtvC7ZC88SK)

Lorsque vous créez une configuration de lancement Node de base (cliquez sur l'icône d'engrenage et sélectionnez Node), vous pouvez faire une ou les deux choses suivantes.

La première consiste simplement à passer des variables dans la configuration de lancement.

![Image](https://cdn-media-1.freecodecamp.org/images/OKoRgCmVBQJG3p2ZQ9em6NaMIYwNauEwp6Wd)

C'est bien, mais le fait que chaque valeur doive être une chaîne me dérange un peu. C'est un nombre, pas une chaîne. JavaScript n'a que, comme, 3 types. Ne m'en retirez pas un.

Il y a une manière plus simple ici. Nous avons déjà appris à aimer les fichiers `.env`, donc au lieu de les passer, nous pouvons simplement donner à VS Code le nom du fichier .env.

![Image](https://cdn-media-1.freecodecamp.org/images/5mkXYjMBORiWKSTBZzCcZTK33ubGUTFy7SuZ)

Et tant que nous démarrons notre processus à partir de VS Code, les fichiers de variables d'environnement sont chargés. Nous n'avons pas à mutiler les nombres en chaînes et nous ne déployons pas de code inutile en production. Enfin, au moins vous ne le faites pas.

#### Démarrer avec NPM au lieu de Node

Vous êtes peut-être arrivé jusqu'ici et vous avez pensé, « Burke, je ne lance jamais `node` quoi que ce soit. C'est toujours un script npm comme `npm start` ».

Dans ce cas, vous pouvez toujours utiliser les configurations de lancement de VS Code. Au lieu d'utiliser un processus de lancement Node standard, vous ajoutez une configuration qui est une tâche « Lancement Via NPM ».

![Image](https://cdn-media-1.freecodecamp.org/images/7tUmGEn-i6T30kHkzfXYj5qzAK8rB6qMTZir)

Maintenant, vous pouvez ajouter votre ligne `envFile` et ajuster les `runtimeArgs` pour qu'ils lancent le script correct. Cela est _généralement_ quelque chose comme « start » ou « debug ».

![Image](https://cdn-media-1.freecodecamp.org/images/bkDqIcWImMhXbMrGry73ABhvBWCG2x5Sy92k)

**Notez que vous devez ajouter le flag `--inspect` à votre script npm pour que VS Code puisse attacher le débogueur**. Sinon, la tâche sera lancée, mais le débogueur VS Code expirera comme moi essayant d'obtenir un rendez-vous au lycée.

![Image](https://cdn-media-1.freecodecamp.org/images/tGcPy6sdBlu9sR1OD07VdHD9MuSgj9-uDb7K)

### Variables d'environnement de production

Jusqu'à présent, nous avons vu comment définir des variables pour le développement. Vous n'utiliserez probablement pas de fichiers .env en production, et les configurations de lancement de VS Code ne seront pas super utiles sur un serveur.

En production, les variables seront définies selon la manière dont votre plateforme de choix vous permet de le faire. Dans le cas d'Azure, il existe 3 façons différentes de définir et de gérer les variables d'environnement.

La première façon est d'utiliser l'[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/webapp/config/appsettings?view=azure-cli-latest&wt.mc_id=dotenv-medium-buhollan).

```bash
az webapp config appsettings set -g MyResourceGroup -n MyApp --settings PORT=65534
```

Ce qui fonctionne, mais, beurk.

Une autre façon est via le portail web Azure. Je n'utilise pas toujours un portail web, mais quand je le fais, c'est pour définir des variables d'environnement.

Dans le cas d'Azure, celles-ci sont appelées « Paramètres d'Application ».

![Image](https://cdn-media-1.freecodecamp.org/images/prz52i4eiyXapzYAPqEIQ9ggSnCYwFGTYWzi)

Et puisque vous utilisez VS Code, vous pouvez installer l'extension App Service et gérer tous les paramètres d'application [directement depuis l'éditeur](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice&WT.mc_id=dotenv-medium-buhollan).

![Image](https://cdn-media-1.freecodecamp.org/images/4L4UwQ0TYob3wz--qcO2AQfmjFIxhMQ6ecax)

J'adore ne pas avoir à quitter VS Code pour faire quoi que ce soit. J'écrirais des emails dans VS Code si je le pouvais.

ATTENDEZ UNE MINUTE !

[**markdown-mail - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)  
[_Extension pour Visual Studio Code - Utiliser le markdown pour écrire votre email et l'envoyer！_](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)  
[marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ccccly.markdown-mail&WT.mc_id=dotenv-medium-buhollan)

### Maintenant vous savez

Maintenant vous savez ce que je sais (ce qui n'est pas grand-chose, je vous le dis) et j'ai l'impression d'avoir accompli mon objectif d'un nombre judicieux de blagues sur Java en cours de route. Juste au cas où je ne l'aurais pas fait, je vous laisse avec celle-ci.

> Java est un outil très puissant pour transformer du XML en traces de pile  
>   
>  Inconnu

_Avertissement de satire : La plupart de ceci est une pauvre tentative d'humour, et certaines aux dépens de Java ; ce qui n'est pas gentil mais est très facile. Ces blagues ne s'écrivent pas toutes seules._