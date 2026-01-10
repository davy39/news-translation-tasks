---
title: Comment utiliser TypeScript et MongoDB pour créer un bot Discord pour le défi
  100 Days of Code
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-06-22T16:20:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-100-days-of-code-bot-for-discord-using-typescript-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/news-header.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: '#chatbots'
  slug: chatbots
- name: discord
  slug: discord
- name: freeCodeCamp.org
  slug: freecodecamp
seo_title: Comment utiliser TypeScript et MongoDB pour créer un bot Discord pour le
  défi 100 Days of Code
seo_desc: "The 100 Days of Code challenge is very popular among new coders and developers\
  \ looking to level up their skills. It's so popular that our Discord server has\
  \ an entire channel dedicated to it. \nBy popular demand, we recently built a Discord\
  \ bot that h..."
---

Le [défi 100 Days of Code](https://www.freecodecamp.org/news/the-crazy-history-of-the-100daysofcode-challenge-and-why-you-should-try-it-for-2018-6c89a76e298d/) est très populaire parmi les nouveaux codeurs et les développeurs cherchant à améliorer leurs compétences. Il est si populaire que notre [serveur Discord](https://www.freecodecamp.org/news/freecodecamp-discord-chat-room-server/) possède un canal entier dédié à ce défi. 

Par demande populaire, nous avons récemment construit un bot Discord qui aide les gens à suivre leur progression dans le défi.

Aujourd'hui, je vais vous montrer comment construire votre propre bot pour le défi 100 Days of Code.

## Comment créer une application de bot Discord

Votre première étape consiste à configurer une application de bot Discord. Rendez-vous sur le [Portail des développeurs Discord](https://discord.com/developers), connectez-vous si nécessaire, et sélectionnez "Applications" dans la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-158.png)
_Capture d'écran du Portail des développeurs. Si c'est votre premier bot, vous n'aurez aucune application ici._

Cliquez sur le bouton "Nouvelle Application". Donnez-lui un nom, et définissez-la comme une application "Personnelle". Vous serez maintenant redirigé vers les paramètres de l'application. Ici, vous pouvez changer le nom, ou lui donner un avatar.

Sélectionnez "Bot" dans la barre latérale, puis cliquez sur le bouton "Ajouter un Bot". Cela créera un compte de bot Discord pour votre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-99.png)
_Capture d'écran de la page des paramètres du Bot. Si vous n'avez pas défini d'avatar, vous verrez un avatar par défaut basé sur le nom de votre bot._

C'est sur cet écran que vous obtiendrez le token du bot. Il est _très_ important de garder ce token secret, car le token permet à votre code de se connecter à votre bot. Gardez-le en sécurité et ne le partagez avec personne.

Maintenant, vous devez ajouter le bot à un serveur pour interagir avec lui. Cliquez sur l'option "OAuth2" dans la barre latérale. Vous devriez voir un formulaire sous la section "Générateur d'URL OAuth2". Laissez le menu déroulant "Sélectionner l'URL de redirection" vide, et cochez la case pour la portée "bot".

Une option pour sélectionner les permissions apparaîtra. Cochez les cases pour les permissions suivantes :

* Envoyer des messages
* Gérer les messages
* Intégrer des liens
* Lire l'historique des messages
* Voir les canaux

Au-dessus de cette section, vous devriez voir une URL générée. Cliquez sur le bouton "Copier" pour la copier, puis collez-la dans votre navigateur et allez-y. 

Cela vous guidera à travers le processus de Discord pour ajouter votre nouveau bot à un serveur. Notez que vous devez avoir la permission de gérer le serveur dans le serveur où vous souhaitez ajouter le bot. Si vous n'avez pas cette permission dans aucun serveur, vous pouvez créer un serveur pour tester votre bot.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-156.png)
_Capture d'écran de l'écran OAuth avec les paramètres corrects marqués._

Maintenant, vous êtes prêt à écrire du code !

## Comment configurer votre projet

Vous devez configurer l'infrastructure et les outils pour votre projet.

### Préparer le `package.json`

Créez un répertoire, ou dossier, pour votre projet. Ouvrez votre terminal en pointant vers ce nouveau dossier. Exécutez la commande `npm init` pour configurer votre fichier `package.json`. Pour ce tutoriel, les valeurs par défaut sont suffisantes, mais vous pouvez les modifier comme vous le souhaitez.

Vous devriez obtenir un `package.json` similaire à ceci :

```json
{
  "name": "tutorial",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

Maintenant, vous devez apporter quelques modifications pour vous préparer à l'implémentation de TypeScript.

Tout d'abord, remplacez la valeur `main` de `index.js` par `./prod/index.js` – vous allez configurer votre TypeScript pour qu'il compile dans un répertoire `prod`.

Ensuite, supprimez le script `test` et ajoutez les deux scripts suivants :

```json
"build": "tsc",
"start": "node -r dotenv/config ./prod/index.js"
```

Le script `build` compilera votre TypeScript en JavaScript afin que `node` puisse l'exécuter, et le script `start` exécutera le fichier d'entrée `index.js`.

L'ajout de `-r dotenv/config` ici importera et exécutera dynamiquement la méthode `config` dans le package `dotenv`, qui charge vos variables d'environnement à partir du fichier `.env`.

En parlant de packages, votre prochaine étape consiste à installer les dépendances. Utilisez `npm install` pour installer ces dépendances :

* `discord.js` – c'est la bibliothèque qui gérera la connexion à la passerelle et la gestion des appels à l'API Discord.
* `dotenv` – un package qui charge les valeurs `.env` dans le processus node.
* `mongoose` – Un wrapper pour la connexion MongoDB qui offre des outils pour structurer vos données.

Enfin, installez les dépendances de développement avec `npm install --save-dev`. Les dépendances de développement sont des packages nécessaires pour travailler sur votre projet dans un environnement de développement, mais pas pour exécuter la base de code en production.

* `typescript` – C'est le package pour le langage TypeScript, qui inclut tout ce qui est nécessaire pour écrire du code en TypeScript et le compiler en JavaScript.
* `@types/node` – TypeScript s'appuie sur des définitions de types pour aider à comprendre le code que vous écrivez. Ce package définit les types pour l'environnement d'exécution Node.js, comme l'objet `process.env`.

Avec ces packages installés, vous devriez maintenant avoir un `package.json` similaire à ceci :

```json
{
  "name": "tutorial",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "tsc",
    "start": "node -r dotenv/config ./prod/index.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "discord.js": "^12.5.3",
    "dotenv": "^10.0.0",
    "mongoose": "^5.12.14"
  },
  "devDependencies": {
    "@types/node": "^15.12.2",
    "typescript": "^4.3.4"
  }
}
```

### Préparer TypeScript

Le compilateur TypeScript offre un certain nombre de paramètres différents pour maximiser votre contrôle sur le JavaScript résultant. 

Vous pouvez généralement modifier les paramètres du compilateur via un fichier `tsconfig.json` à la racine de votre projet. Vous pouvez générer le modèle par défaut pour ce fichier avec `npx tsc --init`, utiliser un fichier existant si vous en avez configuré un dans un autre projet, ou même en écrire un à partir de zéro.

Parce que les paramètres du compilateur peuvent changer significativement le comportement de TypeScript, il est préférable d'utiliser les mêmes paramètres lorsque vous suivez ce tutoriel. Voici les paramètres que vous devriez utiliser :

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "CommonJS",
    "rootDir": "./src",
    "outDir": "./prod",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  }
}
```

Les paramètres les plus importants ici sont les paramètres `rootDir` et `outDir`. Ceux-ci indiquent au compilateur que tout votre code sera dans le répertoire `src`, et que le JavaScript résultant doit aller dans le répertoire `prod`.

Si vous souhaitez tester vos paramètres, créez un répertoire `src` et placez un fichier `index.ts` à l'intérieur. Écrivez du code (comme une instruction `console.log`) et exécutez `npm run build` dans votre terminal. Vous devriez voir un répertoire `prod` se créer, avec un `index.js` contenant votre code compilé.

### Notes de configuration supplémentaires

Si vous utilisez `git` comme contrôle de version, vous souhaitez éviter de pousser les secrets et le code inutile à votre dépôt. Créez un fichier `.gitignore` dans votre répertoire de projet racine, et ajoutez le contenu suivant :

```txt
/node_modules/
/prod/
.env
```

Le fichier `.gitignore` indique à `git` de ne pas suivre les fichiers/dossiers qui correspondent aux motifs que vous entrez. Ignorer le dossier des modules node empêche votre dépôt de devenir trop volumineux. 

Pousser le JavaScript compilé est également inutile, car votre projet est généralement compilé en production avant l'exécution. Les fichiers `.env` contiennent généralement vos valeurs secrètes, telles que les clés API et les tokens, ils ne doivent donc pas être validés dans un dépôt.

Si vous utilisez un environnement basé sur UNIX (comme Linux, ou Git Bash sur Windows), vous pouvez également ajouter un script `prebuild` à votre `package.json`. Le script `prebuild` s'exécutera automatiquement avant le script `build` lorsque vous utiliserez `npm run build`. J'ai configuré le mien pour nettoyer le répertoire `prod` existant avec `rm -r ./prod`.

## Comment créer le bot Discord

Votre prochaine étape consiste à préparer la connexion initiale du bot. Si vous ne l'avez pas fait plus tôt, créez un répertoire `src` et un fichier `index.ts` à l'intérieur.

Commencez par une expression de fonction anonyme immédiatement invoquée (IIFE) pour permettre l'utilisation de `await` au niveau supérieur :

```ts
(async () => {

})();
```

Dans cette fonction, vous allez instancier votre bot Discord. En haut du fichier, importez la classe `Client` avec `import { Client } from "discord.js";`. La classe `Client` représente la session de votre bot Discord.

Dans votre fonction, construisez une nouvelle instance de `Client` et attribuez-la à une variable `BOT` avec `const BOT = new Client();`. Maintenant, la variable `BOT` représentera votre bot.

Pour connecter votre bot à la passerelle Discord et commencer à recevoir des événements, vous devrez utiliser la méthode `.login()` sur votre instance de bot. La méthode `.login()` prend un seul argument, qui est le token pour l'application de bot que vous avez créée précédemment. 

De nombreuses méthodes dans `discord.js` sont asynchrones, vous devrez donc utiliser `await` ici. Ajoutez la ligne `await BOT.login(process.env.BOT_TOKEN);` à votre IIFE.

L'objet `process.env` contiendra les variables d'environnement pour votre environnement d'exécution Node.js. Avec le package `dotenv`, cela inclura également les variables que vous avez définies dans votre fichier de secrets `.env`. 

Créez ce fichier `.env` à la racine de votre projet, et ajoutez `BOT_TOKEN=""` comme première ligne. Entre les guillemets, collez le token du bot depuis la page du bot sur le Portail des développeurs Discord.

Votre fichier `index.ts` devrait maintenant ressembler à ceci :

```ts
import { Client } from "discord.js";

(async () => {
  const BOT = new Client();

  await BOT.login(process.env.BOT_TOKEN);
})();

```

En supposant que vous avez ajouté votre nouveau bot à un serveur, si vous exécutez `npm run build` et `npm start`, vous devriez voir votre bot se connecter au serveur. Cependant, le bot ne répondra à rien pour l'instant, car nous n'avons pas encore commencé à écouter les événements.

## Événements de la passerelle dans Discord

Les événements de la "passerelle" sont générés lorsqu'une action se produit sur Discord, et sont généralement envoyés aux clients (y compris votre bot) sous forme de charges utiles JSON. Vous pouvez écouter ces événements avec la méthode `.on()`, ce qui vous permet d'écrire la logique que votre bot doit suivre lorsque des événements spécifiques se produisent.

Le premier événement à écouter est l'événement "ready". Cet événement se déclenche lorsque votre bot s'est connecté à la passerelle et est _prêt_ à traiter les événements. Au-dessus de votre appel `.login()`, ajoutez `BOT.on("ready", () => console.log("Connecté à Discord !"));`. 

Pour que vos modifications prennent effet, utilisez `npm run build` à nouveau pour compiler le nouveau code. Maintenant, si vous essayez `npm run start`, vous devriez voir "Connecté à Discord !" s'afficher dans votre terminal.

## Comment se connecter à la base de données

Vous allez utiliser le package `mongoose` pour vous connecter à une instance MongoDB. Si vous préférez, vous pouvez exécuter MongoDB localement, ou vous pouvez utiliser le niveau gratuit de MongoDB Atlas pour une solution basée sur le cloud. 

Si vous n'avez pas de compte MongoDB Atlas, freeCodeCamp a un [excellent tutoriel pour en configurer un](https://www.freecodecamp.org/news/get-started-with-mongodb-atlas/).

Récupérez votre chaîne de connexion pour votre base de données et ajoutez-la à votre fichier `.env` sous la forme `MONGO_URI=""`, avec la chaîne de connexion entre les guillemets. Pour le nom de la base de données, utilisez `oneHundredDays`.

Créez un répertoire appelé `database` pour contenir les fichiers qui contiennent votre logique de base de données. Dans ce répertoire, créez un fichier appelé `connectDatabase.ts`. Vous allez écrire votre logique pour initier la connexion à la base de données ici.

Commencez par une déclaration de fonction exportée :

```ts
export const connectDatabase = async () => {

}
```

`mongoose` offre une méthode `connect` pour se connecter à la base de données. Importez-la avec `import { connect } from "mongoose";` en haut de votre fichier.

Ensuite, utilisez la méthode dans votre fonction avec `await connect(process.env.MONGO_URI);`. Ajoutez une instruction `console.log` après cela pour que vous puissiez identifier que votre bot s'est connecté à la base de données. 

Votre fichier `connectDatabase.ts` devrait maintenant ressembler à ceci :

```ts
import { connect } from "mongoose";

export const connectDatabase = async () => {
    await connect(process.env.MONGO_URI);
    console.log("Base de données connectée !")
}
```

Maintenant, dans votre fichier `index.ts`, importez cette fonction avec `import { connectDatabase } from "./database/connectDatabase"` et ajoutez `await connectDatabase()` à votre IIFE, juste avant la méthode `.login()`. Allez-y et exécutez `npm run build` à nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-157.png)
_Une erreur de compilation, indiquant que : L'argument de type string ou undefined n'est pas assignable au paramètre de type string._

Oh non – une erreur !

## Validation des variables d'environnement

Le problème avec les variables d'environnement est qu'elles peuvent toutes être `undefined`. Cela arrive souvent si vous faites une faute de frappe dans le nom de votre variable d'environnement, ou si vous confondez le nom avec un autre nom (une erreur que j'ai faite en écrivant ce tutoriel, en utilisant `TOKEN` au lieu de `BOT_TOKEN` à certains endroits).

TypeScript vous avertit que la méthode `connect` prend une chaîne de caractères, et qu'une valeur `undefined` va tout casser. Vous pouvez corriger cela, mais d'abord vous allez vouloir écrire une fonction pour gérer la validation de vos variables d'environnement.

Dans votre répertoire `src`, créez un répertoire `utils` pour contenir vos fonctions utilitaires. Ajoutez un fichier `validateEnv.ts` là.

Créez une fonction dans le fichier appelée `validateEnv`. Cette fonction sera synchrone et n'a pas besoin du mot-clé `async`. Dans cette fonction, ajoutez des conditions pour vérifier vos deux variables d'environnement. Si l'une d'elles est manquante, retournez `false`. Sinon, retournez `true`.

Votre code pourrait ressembler à ceci :

```ts
export const validateEnv = () => {
  if (!process.env.BOT_TOKEN) {
    console.warn("Token du bot Discord manquant.");
    return false;
  }

  if (!process.env.MONGO_URI) {
    console.warn("Connexion MongoDB manquante.");
    return false;
  }
  return true;
};


```

Retournez à votre fichier `index.ts` et importez cette fonction de validation avec `import { validateEnv } from "./utils/validateEnv"`. Ensuite, au début de votre IIFE, utilisez une instruction if pour retourner tôt si la fonction retourne false. Votre `index.ts` devrait ressembler à :

```ts
import { Client } from "discord.js";
import { connectDatabase } from "./database/connectDatabase";
import { validateEnv } from "./utils/validateEnv";

(async () => {
  if (!validateEnv()) return;

  const BOT = new Client();

  BOT.on("ready", () => console.log("Connecté à Discord !"));

  await connectDatabase();

  await BOT.login(process.env.BOT_TOKEN);
})();

```

Si vous essayez `npm run build` à nouveau, vous verrez le même message d'erreur qu'avant. Cela est dû au fait que, bien que nous sachions que la variable d'environnement existe, TypeScript ne peut toujours pas l'inférer. La fonction de validation est configurée pour quitter le processus si la variable d'environnement est manquante, nous allons donc dire à TypeScript qu'il s'agit définitivement d'une chaîne de caractères.

Retournez dans votre fichier `connectDatabase.ts`, dans la fonction `connect`, utilisez `process.env.MONGO_URI as string` pour forcer le type en `string`. L'erreur devrait disparaître, et vous pouvez maintenant exécuter `npm run build` et `npm start`. 

Vous devriez voir les messages que vous avez écrits pour les connexions Discord et MongoDB s'afficher dans votre terminal.

## L'événement "message"

Bien que vous fassiez de grands progrès sur votre bot, il ne _fait_ toujours rien. Pour que le bot réponde aux messages, vous aurez besoin d'un autre gestionnaire d'événements. 

La logique de celui-ci sera un peu plus compliquée, vous devriez donc créer un module séparé pour cela. Créez un dossier `events` dans le répertoire `src`.

Dans votre dossier `events`, créez un fichier `onMessage.ts`. En haut, importez la classe `Message` de discord.js avec `import { Message } from "discord.js";`. Cette classe servira de définition de type.

Ensuite, créez une fonction exportée appelée `onMessage`. La fonction doit être asynchrone et prendre un paramètre `message` avec le type `Message`. Votre fonction ressemblera à ceci :

```ts
import { Message } from "discord.js";

export const onMessage = async (message: Message) => {

};

```

Avant de plonger dans la logique de cette fonction, vous devez l'attacher à l'écouteur d'événements. Retournez dans votre fichier `index.ts`, importez votre nouvelle fonction avec `import { onMessage } from "./events/onMessage";`.

À côté de votre écouteur `.on("ready")` existant, ajoutez un écouteur `BOT.on("message")`. Pour l'événement "message", le rappel prend un argument `message` que vous pouvez passer à votre nouvelle fonction `onMessage` :

```ts
BOT.on("message", async (message) => await onMessage(message));
```

Nous devrions tester que cela fonctionne. Retournez à votre fichier `onMessage.ts`. À l'intérieur de votre fonction `onMessage`, ajoutez `console.log(message.content)`. La propriété `.content` de la classe `Message` contient le contenu textuel envoyé dans le message.

Utilisez `npm run build` et `npm start` pour faire fonctionner votre bot à nouveau, puis envoyez "Hello" dans un canal Discord que le bot peut voir. Vous devriez voir "Hello" s'afficher dans votre terminal.

## Comment se préparer pour les commandes

Je maintiens quelques bots Discord, et une chose que j'ai découverte qui aide à garder le code maintenable et lisible est de rendre les composants modulaires.

### Définir une interface

Vous devrez d'abord définir une structure commune pour vos commandes. Créez un dossier `interfaces` dans `src`. Ensuite, à l'intérieur de `interfaces`, créez un fichier `CommandInt.ts`.

Maintenant, vous allez créer une interface. En TypeScript, une interface est souvent utilisée pour définir la structure d'un objet, et est l'un des nombreux outils disponibles pour déclarer le type d'une variable.

Dans votre fichier `CommandInt.ts`, importez la classe Message de Discord, puis déclarez une interface appelée `CommandInt` avec cette syntaxe :

```ts
import { Message } from "discord.js";

export interface CommandInt {

}
```

À l'intérieur de cette interface, vous allez ajouter trois propriétés :

* `name: string;` – la valeur `name` sera le nom de votre commande. Vous l'utiliserez pour déclencher la commande dans le serveur Discord.
* `description: string;` – la valeur `description` explique ce que fait la commande. Vous l'utiliserez dans l'une des commandes.
* `run: (message: Message) => Promise<void>` – c'est la propriété qui contiendra la logique de la commande.

La définition de type `run` est un peu délicate, alors décomposons-la. Vous l'avez typée comme une fonction qui prend un argument, `message`. Cet argument doit être du type `Message`. Vous avez ensuite défini le type de `return` de la fonction sur `Promise<void>`. Cela signifie que votre fonction sera asynchrone (ce qui est important plus tard) et ne retourne pas de valeur.

### Créer une liste de commandes

Ensuite, vous avez besoin d'un endroit pour stocker toutes vos commandes. Créez un dossier appelé `commands` dans le répertoire `src`, et ajoutez un fichier appelé `_CommandList.ts`. Le soulignement ici gardera ce fichier en haut de la liste.

Le fichier `_CommandList.ts` aura besoin de deux lignes. Tout d'abord, importez votre interface `CommandInt`, puis déclarez un tableau `CommandList`. Le tableau sera vide pour l'instant, mais donnez-lui un type `CommandInt[]` pour que TypeScript sache qu'il contiendra éventuellement vos objets de commande. Le fichier devrait ressembler à :

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const CommandList: CommandInt[] = [];
```

Le but de ce fichier est de créer un tableau de vos commandes de bot que vous allez parcourir dans l'écouteur d'événements de message. [Il existe des moyens d'automatiser cela](https://github.com/BeccaLyria/discord-bot/blob/main/src/utils/readDirectory.ts), mais ils tendent à être inutilement complexes pour les petits bots.

### Vérifier les commandes

Retournez dans votre fichier `onMessage.ts`, vous devriez commencer à travailler sur la logique pour vérifier les messages pour les commandes.

La première étape consiste à vous assurer que votre bot ignore ses propres messages, ainsi que les messages des autres bots. Cela aide à prévenir les cycles sans fin où le bot répond à lui-même. 

L'objet `message` a une propriété `author`, qui représente l'utilisateur Discord qui a envoyé le message. La propriété `author` a une propriété `bot`, qui est un booléen indiquant que l'auteur est un compte de bot. Ajoutez une étape pour vérifier si cette propriété est vraie :

```ts
if (message.author.bot) {
  return;
}
```

Vous souhaitez également empêcher les gens de déclencher accidentellement les commandes de votre bot. Par exemple, si vous avez une commande `help`, vous ne voudriez pas que le bot réponde lorsque quelqu'un dit "help me please".

Cela peut être évité en définissant un préfixe pour que le bot le détecte. La plupart des bots utilisent `!`, mais vous êtes libre de choisir le préfixe que vous souhaitez. 

Déclarez une variable `prefix` et attribuez-lui votre préfixe choisi, comme `const prefix = "!";`. Ensuite, ajoutez une condition pour vérifier si le `message.content` ne commence pas par ce préfixe, et si c'est le cas, `return`.

```ts
const prefix = "!";

if (!message.content.startsWith(prefix)) {
  return;
}

```

Maintenant que vous avez vérifié que le message provient d'un utilisateur et déclenche intentionnellement votre bot, vous pouvez vérifier si la commande est valide. 

L'utilisation du tableau (actuellement vide) `CommandList` facilitera ce processus, alors importez-le en haut de votre fichier avec `import { CommandList } from "../commands/_CommandList";`.

Il existe plusieurs façons de parcourir un tableau – pour le bot en direct, j'ai utilisé une boucle `for..of`. Quelle que soit l'approche de la boucle, vous allez vouloir vérifier chaque commande dans le tableau par rapport au contenu du message. Voici un exemple de boucle :

```ts
  for (const Command of CommandList) {
    if (message.content.startsWith(prefix + Command.name)) {
      await Command.run(message);
      break;
    }
  }
```

Cette boucle parcourt la liste des commandes, et si le contenu du message commence par le préfixe et le nom de la commande, le bot appellera la méthode `run` de la commande. 

Rappelez-vous que vous avez déclaré la propriété `run` comme une fonction asynchrone qui prenait le message comme argument. Ensuite, pour économiser du temps de calcul, la boucle se rompt lorsqu'elle trouve une commande correspondante.

## Modèle de base de données

Il y a une étape de plus avant que vous ne soyez prêt à commencer à écrire des commandes. Ce bot suivra la progression de vos membres de la communauté dans le défi 100 Days of Code. Et vous devez stocker cette progression dans la base de données.

`mongoose` aide à structurer vos enregistrements MongoDB pour vous empêcher de passer des données malformées ou incomplètes dans votre base de données.

Commencez par créer un dossier `models` dans votre répertoire `database`. Dans ce dossier `models`, créez un fichier `CamperModel.ts`. Ce sera votre structure pour les objets utilisateur.

Vous devez d'abord importer les valeurs nécessaires de la bibliothèque `mongoose`. Ajoutez `import { Document, model, Schema } from "mongoose";` en haut du fichier.

Parce que vous utilisez TypeScript, vous devez créer une définition de type pour vos objets de base de données. Créez une autre interface, comme vous l'avez fait pour vos commandes, nommée `CamperInt`.

```ts
export interface CamperInt {

}
```

Votre modèle de base de données aura quatre propriétés. Ajoutez celles-ci à votre interface :

* `discordId: string;` – Chaque objet utilisateur dans Discord a un identifiant unique, appelé Snowflake, qui est utilisé pour les distinguer des autres utilisateurs. Contrairement à un nom d'utilisateur ou à un discriminateur (le nombre à quatre chiffres après le nom d'utilisateur), la valeur `id` ne peut pas être changée. Cela en fait la valeur idéale pour lier vos données stockées à un utilisateur Discord.
* `round: number;` – Cela représentera le "round" auquel l'utilisateur est dans le défi. Lorsque quelqu'un termine 100 jours du défi, il peut choisir de relever à nouveau le défi. Lorsqu'il le fait, il s'y réfère souvent comme "round 2", par exemple. 
* `day: number;` – Cela représente le jour auquel l'utilisateur est dans le défi.
* `timestamp: number;` – Vous utiliserez cette valeur pour suivre quand l'utilisateur a soumis pour la dernière fois un post 100 Days of Code.

Super ! Maintenant, vous devez définir le Schéma pour vos entrées de base de données. `mongoose` utilise un objet Schema pour définir la forme des documents qui vont dans votre collection de base de données. L'import `Schema` a un constructeur, que vous allez attribuer à une variable.

```ts
export const Camper = new Schema();
```

Ce constructeur prend un objet comme argument, et cet objet définit les clés et les types de la base de données. Allez-y et passez un objet similaire à ce à quoi ressemble votre interface.

```ts
export const Camper = new Schema({
    discordId: String,
    round: Number,
    day: Number,
    timestamp: Number,
})
```

Ensuite, vous devez créer le `model`. Dans `mongoose`, l'objet `model` sert à créer, lire et mettre à jour vos documents dans la base de données MongoDB. Ajoutez `export default model();` en bas de votre fichier.

La fonction `model` prend quelques paramètres. Le premier est une chaîne de caractères, et est le nom à utiliser pour les documents dans votre base de données. Pour cette collection, utilisez `"camper"`. Le deuxième argument est le schéma à utiliser pour les données – utilisez votre schéma `Camper` ici.

Par défaut, `mongoose` utilisera la version plurielle de votre nom de `model` pour la collection. Dans notre cas, ce serait "campers". Si vous souhaitez changer cela, vous pouvez passer un troisième argument de `{ collection: "name" }` pour définir la collection à `name`.

Si vous utilisiez JavaScript, cela serait suffisant pour configurer votre modèle de base de données. Cependant, parce que vous utilisez TypeScript, vous devriez profiter de la sécurité des types. `model()` par défaut retourne un type `Document` de `any`. 

Pour résoudre cela, vous pouvez passer un type générique dans la fonction `model`. Les types génériques servent de variables pour les définitions de types, en quelque sorte. Vous devez définir le type générique pour votre `model` pour utiliser votre interface. Ajoutez le type générique en changeant `model` en `model<CamperInt>`.

Juste une étape de plus ici. Votre interface `CamperInt` ne définit que les propriétés que vous avez définies dans le document MongoDB, mais n'inclut pas les propriétés standard. 

Changez votre `export interface CamperInt` en `export interface CamperInt extends Document`. Cela indique à TypeScript que votre définition de type est une extension de la définition de type `Document` existante – vous ajoutez essentiellement des propriétés à cette structure.

Votre fichier final devrait ressembler à ceci :

```ts
import { Document, model, Schema } from "mongoose";

export interface CamperInt {
  discordId: string;
  round: number;
  day: number;
  timestamp: number;
}

export const Camper = new Schema({
  discordId: String,
  round: Number,
  day: Number,
  timestamp: Number,
});

export default model<CamperInt>("camper", Camper);

```

En guise de vérification de sécurité, utilisez `npm run build` à nouveau. Vous ne devriez voir aucune erreur dans le terminal.

## Comment écrire des commandes de bot

Vous êtes enfin prêt à commencer à écrire quelques commandes ! Comme il s'agit d'un bot pour le défi 100 Days of Code, vous devriez commencer par la commande de création d'une mise à jour pour le défi 100 Days of Code.

### Commande 100

Dans votre dossier `commands`, créez un fichier `oneHundred.ts`. Cela contiendra votre commande pour le défi 100 Days of Code. Importez votre interface de commande avec `import { CommandInt } from "../interfaces/CommandInt";`.

Maintenant, déclarez une variable exportée `oneHundred` et donnez-lui le type `CommandInt` :

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const oneHundred: CommandInt = {
    
}
```

Définissez la propriété `name` sur `"100"`, donnez-lui une propriété `description` similaire à `"Crée une mise à jour pour le défi 100 Days of Code"`, et configurez la fonction `run` comme `async (message) => {}`.

Maintenant, pour la logique à l'intérieur de la fonction. Votre logique aura besoin de quelques propriétés de l'objet `message` pour fonctionner, alors allez-y et déstructurez celles-ci : `const{ author, channel, content } = message;`.

Lorsque l'utilisateur appelle cette commande, cela devrait ressembler à ceci :

> !100 Voici ma mise à jour pour le défi 100 Days of Code.

Vous allez vouloir extraire ce texte sans la partie `!100`. Il y a plusieurs façons de faire cela – nous allons le découper avec `const text = content.split(" ").slice(1).join(" ")`.  En utilisant l'exemple précédent, `text` contiendrait maintenant la chaîne `"Voici ma mise à jour pour le défi 100 Days of Code."`.

Il est temps de faire un peu de travail sur la base de données. Importez votre `CamperModel` avec `import CamperModel from "../database/models/CamperModel"`. Notez que vous importez l'export par défaut, au lieu d'un module.

Maintenant, vous devez voir si l'utilisateur a un enregistrement dans votre base de données. Utilisez `let targetCamperData = await CamperModel.findOne()` pour vous préparer à cela. 

La méthode `.findOne()` est utilisée pour interroger la collection pour un seul enregistrement, et prend un objet pour filtrer la requête. Ces requêtes supportent la syntaxe de MongoDB pour la recherche avancée, mais dans ce cas, vous n'avez besoin que de trouver l'enregistrement par l'`discordId` de l'utilisateur. Ajoutez `{discordId: author.id}` comme paramètre pour le `findOne()`.

Que se passe-t-il si l'enregistrement de l'utilisateur n'existe pas encore ? Si c'est la première fois qu'il utilise la commande, il n'aura pas de document dans la base de données. Ajoutez une condition `if` pour vérifier si `targetCamperData` n'existe pas :

```ts
if (!targetCamperData) {

}
```

Dans ce bloc, vous allez réattribuer `targetCamperData` à un nouveau document avec `targetCamperData = await CamperModel.create()`. Vous utilisez la méthode `.create()` pour générer et sauvegarder un nouveau document. La méthode prend un objet comme premier argument – cet objet est le document à créer. Passez l'objet suivant à la méthode :

```ts
targetCamperData = await CamperModel.create({
  discordId: author.id,
  round: 1,
  day: 0,
  timestamp: Date.now()
});
```

Que l'enregistrement existe déjà ou vient d'être créé, votre prochaine étape est de le mettre à jour. Après votre bloc `if`, ajoutez une ligne pour incrémenter la valeur `day` : `targetCamperData.day++`.

Que se passe-t-il si l'utilisateur est au jour 100 ? Il ne devrait pas pouvoir passer au jour 101, car le défi ne dure que cent jours. Vous devrez ajouter une logique pour cela. Si l'utilisateur est au-dessus du jour 100, vous voulez définir son jour à 1 et augmenter son round :

```ts
targetCamperData.day++;
if (targetCamperData > 100) {
  targetCamperData.day = 1;
  targetCamperData.round++;
}

```

Maintenant, mettez à jour le timestamp avec `targetCamperData.timestamp = Date.now();`. Cela peut sembler redondant, puisque vous avez fait cette étape dans la méthode `create`, mais cela garantit que le timestamp est mis à jour si les données existaient déjà.

Vous devez sauvegarder les modifications que vous avez apportées au document. Ajoutez `await targetCamperData.save();` pour cela – `mongoose` sauvegardera alors vos modifications dans le document dans MongoDB.

Maintenant, vous allez construire le message que le bot doit envoyer. Pour ce faire, vous allez utiliser un embed de message. Les embeds de message sont des formats de message spéciaux disponibles pour les bots Discord, qui offrent des options de mise en forme et de style supplémentaires.

Commencez par ajouter la classe `MessageEmbed` à vos imports avec `import { MessageEmbed } from "discord.js";`. Ensuite, après votre logique de base de données, créez un nouvel embed de message avec `const oneHundredEmbed = new MessageEmbed();`. Il est temps de commencer à définir les valeurs de l'embed.

Le titre de l'embed apparaît comme un texte en grand en haut de l'embed. Définissez le titre sur "100 Days of Code" avec `oneHundredEmbed.setTitle("100 Days of Code");`.

La description de l'embed apparaît comme un texte standard sous le titre. Définissez cela sur le texte fourni par l'utilisateur avec `oneHundredEmbed.setDescription(text);`.

L'auteur de l'embed apparaît au-dessus du titre, et est utilisé pour indiquer qui a généré l'embed. Vous allez le définir avec `oneHundredEmbed.setAuthor()`. 

Cette méthode prend quelques arguments, et vous allez utiliser les deux premiers. Le premier argument est le nom de l'auteur. Définissez-le sur `author.username + "#" + author.discriminator`.  Cela s'affichera de la même manière que vous voyez un utilisateur dans Discord : `nhcarrigan#0001`.  

Définissez le deuxième argument sur `author.displayAvatarUrl()`. Il s'agit d'une méthode fournie par discord.js pour récupérer l'URL de l'image de l'avatar de l'auteur.

Les champs d'embed sont des paires titre-description supplémentaires qui peuvent être imbriquées dans l'embed, et éventuellement en ligne. Ceux-ci peuvent être créés avec la méthode `.addField()`, qui prend jusqu'à trois arguments. Le premier argument est le titre du champ, le deuxième argument est la description du champ, et le troisième argument est un booléen facultatif pour définir le champ comme en ligne. 

Ajoutez deux champs à votre embed. Le premier est `oneHundredEmbed.addField("Round", targetCamperData.round, true);`, et le second est `oneHundredEmbed.addField("Day", targetCamperData.day, true);`.

Vous pouvez ajouter un pied de page à un embed et il apparaît en bas en petit texte. Définissez le pied de page sur le timestamp des données avec `oneHundredEmbed.setFooter("Day completed: " + new Date(targetCamperData.timestamp).toLocaleDateString();`.  La méthode `toLocaleDateString()` prendra un objet `Date` et le convertira en une chaîne spécifique à la locale basée sur l'emplacement du serveur de votre bot.

Maintenant, vous devez envoyer cet embed de message. La propriété `channel` que vous avez extraite de la valeur `message` plus tôt représente le canal Discord dans lequel le message a été envoyé. Cet objet a une méthode `.send()`, que vous pouvez utiliser pour faire envoyer un message par le bot dans ce canal. Utilisez `await channel.send(oneHundredEmbed)` pour envoyer votre nouvel embed dans ce canal.

Pour garder le canal propre, ajoutez un `await message.delete()` pour faire supprimer le message qui a déclenché la commande par le bot. Votre code final devrait ressembler à ceci :

```ts
import { CommandInt } from "../interfaces/CommandInt";
import CamperModel from "../database/models/CamperModel";
import { MessageEmbed } from "discord.js";

export const oneHundred: CommandInt = {
  name: "100",
  description: "Crée une mise à jour pour le défi 100 Days of Code",
  run: async (message) => {
    const { author, channel, content } = message;
    const text = content.split(" ").slice(1).join(" ");

    let targetCamperData = await CamperModel.findOne({ discordId: author.id });

    if (!targetCamperData) {
      targetCamperData = await CamperModel.create({
        discordId: author.id,
        round: 1,
        day: 0,
        timestamp: Date.now(),
      });
    }

    targetCamperData.day++;
    if (targetCamperData.day > 100) {
      targetCamperData.day = 1;
      targetCamperData.round++;
    }
    targetCamperData.timestamp = Date.now();
    await targetCamperData.save();

    const oneHundredEmbed = new MessageEmbed();
    oneHundredEmbed.setTitle("100 Days of Code");
    oneHundredEmbed.setDescription(text);
    oneHundredEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );
    oneHundredEmbed.addField("Round", targetCamperData.round, true);
    oneHundredEmbed.addField("Day", targetCamperData.day, true);
    oneHundredEmbed.setFooter(
      "Day completed: " +
        new Date(targetCamperData.timestamp).toLocaleDateString()
    );

    await channel.send(oneHundredEmbed);
    await message.delete();
  },
};

```

Si vous vous souvenez, vous avez créé une liste pour contenir toutes vos commandes. Vous devez ajouter votre nouvelle commande à cette liste. Retournez à votre fichier `_CommandList.ts`. Importez votre nouvelle commande avec `import { oneHundred } from "./oneHundred";`, puis ajoutez `oneHundred` à votre tableau `CommandList` vide :

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { oneHundred } from "./oneHundred";

export const CommandList: CommandInt[] = [oneHundred];

```

Maintenant, vous pouvez le tester ! Utilisez `npm run build` et `npm start` pour démarrer le bot. Essayez d'envoyer `!100 C'est mon premier message !` dans le canal. Le bot devrait répondre avec un embed et supprimer votre message.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-160.png)
_Vous pouvez voir l'embed, avec l'auteur, le titre, la description, les champs et le pied de page._

### Commande View

Que se passe-t-il si un utilisateur oublie s'il a soumis ou non, ou veut voir à quel jour il est ? Vous devriez ajouter une commande pour voir la progression actuelle du défi 100 Days of Code.

Dans votre répertoire `commands`, créez un fichier `view.ts`. Comme avant, importez votre interface de commande et CamperModel, et créez une nouvelle commande appelée `view`. Définissez le `name` sur `"view"`, la `description` sur quelque chose comme "Voir votre progression actuelle dans le défi 100 Days of Code", et la commande `run` sur `async (message) => {}`.

Vous n'aurez pas besoin du contenu du message pour cette commande, alors extrayez les valeurs `author` et `channel` du `message` comme vous l'avez fait avant : `const { author, channel } = message;`.

Tout comme la commande 100, vous devez récupérer les données de l'utilisateur dans la base de données. Cette fois, cependant, si les données n'existent pas, vous ne les créerez pas – vous pouvez donc utiliser `const` ici au lieu de `let` : `const targetCamperData = await CamperModel.findOne({ discordId: author.id });` 

Maintenant, si l'utilisateur n'a pas encore d'enregistrement de données, il n'a pas commencé le défi avec le bot. Vous devriez envoyer un message pour lui indiquer comment faire.

```ts
if (!targetCamperData) {
  await channel.send("Vous n'avez pas encore commencé le défi.");
  return;
}

```

Construisez un embed, similaire à celui que vous avez construit pour la commande 100. N'oubliez pas d'importer la classe `MessageEmbed` !

```ts
    const camperEmbed = new MessageEmbed();
    camperEmbed.setTitle("Ma progression 100DoC");
    camperEmbed.setDescription(
      `Voici ma progression dans le défi 100 Days of Code. J'ai signalé une mise à jour pour la dernière fois le ${new Date(
        targetCamperData.timestamp
      ).toLocaleDateString()}.`
    );
    camperEmbed.addField("Round", targetCamperData.round, true);
    camperEmbed.addField("Day", targetCamperData.day, true);
    camperEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );
```

Quelques différences clés ici. Au lieu de prendre une entrée de texte de l'utilisateur, vous utilisez une valeur de description fixe pour indiquer qu'il s'agit d'un embed `view` au lieu d'un embed `100`. Puisque vous utilisez le timestamp dans la description, vous n'avez pas besoin d'ajouter un pied de page.

Comme avant, envoyez l'embed au canal de message et supprimez le message original. Votre fichier final devrait être :

```ts
import { CommandInt } from "../interfaces/CommandInt";
import CamperModel from "../database/models/CamperModel";
import { MessageEmbed } from "discord.js";

export const view: CommandInt = {
  name: "view",
  description: "Affiche votre progression dans le défi 100 Days of Code.",
  run: async (message) => {
    const { author, channel } = message;

    const targetCamperData = await CamperModel.findOne({
      discordId: author.id,
    });

    if (!targetCamperData) {
      await channel.send("Vous n'avez pas encore commencé le défi.");
      return;
    }

    const camperEmbed = new MessageEmbed();
    camperEmbed.setTitle("Ma progression 100DoC");
    camperEmbed.setDescription(
      `Voici ma progression dans le défi 100 Days of Code. J'ai signalé une mise à jour pour la dernière fois le ${new Date(
        targetCamperData.timestamp
      ).toLocaleDateString()}.`
    );
    camperEmbed.addField("Round", targetCamperData.round, true);
    camperEmbed.addField("Day", targetCamperData.day, true);
    camperEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );

    await channel.send(camperEmbed)
    await message.delete();
  },
};

```

Ajoutez votre nouvelle commande `view` à votre fichier `_CommandList.ts` avec une importation, et mettez la commande dans le tableau `CommandList`. Ensuite, utilisez `npm run build` et `npm start` pour tester vos nouvelles modifications. Envoyez "!view" dans votre canal et vous devriez voir le bot répondre :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-161.png)

### Commande Edit

Malheureusement, si un utilisateur fait une faute de frappe dans son message 100 Days of Code, il ne peut pas modifier le message car le bot l'a envoyé. Mais vous pouvez ajouter une commande qui lui permettra de le faire.

Créez un fichier `edit.ts` dans votre répertoire `commands`. Importez votre interface de commande et déclarez une nouvelle commande appelée `edit`. Définissez le `name` sur `"edit"`, la `description` sur quelque chose comme "Modifie un message précédent du défi 100 Days of Code", et préparez la fonction `run` comme vous l'avez fait auparavant.

Dans la fonction, extrayez les propriétés `author`, `channel` et `content` de l'objet `message`.

La commande `edit` prendra un identifiant de message Discord, suivi du texte mis à jour à utiliser. Vous pouvez déstructurer ceux-ci à partir du contenu du message avec `const [, targetId, ...text] = content.split(" ");`. 

Le premier élément du tableau serait l'appel de la commande `!edit`, qui n'est pas nécessaire pour cette commande, vous n'avez donc pas besoin de l'attribuer à une valeur. L'élément `targetId` serait l'identifiant du message à modifier. `...text` qui utilise l'opérateur de propagation pour attribuer le reste du contenu du message à la variable `text`, sous forme de tableau.

Maintenant, vous devez utiliser le `targetId` pour obtenir le message réel de Discord. La valeur `channel` a une propriété `messages` qui représente tous les messages envoyés dans ce canal. Vous pouvez utiliser la méthode `fetch` sur cette propriété `messages` pour obtenir un message spécifique (ou plusieurs messages). Configurez cela comme `const targetMessage = await channel.messages.fetch()`. 

La méthode `.fetch()` peut prendre un objet contenant les options pour la requête de récupération, ou elle peut prendre une chaîne comme `id` du message à récupérer. Parce que vous avez l'`id`, et que vous ne récupérez qu'un seul message, vous pouvez passer `targetId` à la méthode `.fetch()` comme seul paramètre.

Il est possible que le `targetMessage` n'existe pas. Par exemple, si l'utilisateur a fourni une chaîne d'identifiant invalide (ou aucune chaîne d'identifiant du tout). Vous devrez ajouter une logique pour vérifier si le `targetMessage` n'est pas trouvé :

```ts
    if (!targetMessage) {
        await channel.send("Cela ne semble pas être un ID de message valide.");
        return;
    }
```

Maintenant que vous avez confirmé que le message existe, vous pouvez commencer à travailler avec les propriétés. Parce que votre bot envoie le message sous forme d'embed, la propriété `content` à laquelle vous êtes habitué à travailler sera vide. Au lieu de cela, vous pouvez trouver l'embed dans la propriété `embeds`.

La propriété `embeds` est un tableau d'objets `MessageEmbed`. Puisque vous avez écrit le code du bot pour n'envoyer qu'un seul embed, vous pouvez accéder à cet embed avec `const targetEmbed = targetMessage.embeds[0];`.

Maintenant que vous avez l'embed, vous devez confirmer que l'embed provient de l'un des messages 100 Days of Code de l'utilisateur. Heureusement, vous avez défini l'utilisateur comme l'auteur de l'embed. Vous pouvez vérifier si les informations de l'auteur de l'embed ne correspondent pas aux informations de l'auteur du message :

```ts
    if (
      targetEmbed.author?.name !==
      author.username + "#" + author.discriminator
    ) {
      await channel.send(
        "Cela ne semble pas être votre message 100 Days of Code. Vous ne pouvez pas le modifier."
      );
      return;
    }
```

Vous avez tenu compte du message appartenant à un autre utilisateur (ou n'ayant pas l'embed correct), vous pouvez donc maintenant modifier l'embed. 

Comme vous l'avez fait auparavant, définissez la description de l'embed avec la méthode `.setDescription()`. Vous devrez utiliser `.join(" ")` sur la variable `text` cette fois, puisque c'est actuellement un tableau. `targetEmbed.setDescription(text.join(" "));`

Plutôt que d'envoyer un nouveau message, vous devez modifier le message existant. Vous avez le message existant stocké dans `targetMessage`, vous pouvez donc utiliser la méthode `.edit()` pour changer ce message directement. 

`await targetMessage.edit(targetEmbed);` changera l'embed du message en votre version modifiée. Ensuite, supprimez le message qui a déclenché cette commande avec `await message.delete();`. Votre commande devrait ressembler à ceci :

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const edit: CommandInt = {
  name: "edit",
  description: "Modifie un message précédent du défi 100 Days of Code.",
  run: async (message) => {
    const { author, channel, content } = message;
    const [, targetId, ...text] = content.split(" ");

    const targetMessage = await channel.messages.fetch(targetId);

    if (!targetMessage) {
      await channel.send("Cela ne semble pas être un ID de message valide.");
      return;
    }

    const targetEmbed = targetMessage.embeds[0];

    if (
      targetEmbed.author?.name !==
      author.username + "#" + author.discriminator
    ) {
      await channel.send(
        "Cela ne semble pas être votre message 100 Days of Code. Vous ne pouvez pas le modifier."
      );
      return;
    }

    targetEmbed.setDescription(text.join(" "));

    await targetMessage.edit(targetEmbed);
    await message.delete();
  },
};

```

Ajoutez la commande à votre fichier `_CommandList.ts`, en l'important et en ajoutant la variable au tableau. Ensuite, utilisez `npm run build` et `npm start` pour exécuter le bot à nouveau.

Pour obtenir un ID de message, vous devez avoir le mode Développeur activé dans votre client Discord. Si vous ne l'avez pas fait, visitez vos paramètres et sélectionnez la section "Avancé". Activez le "Mode Développeur" :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-162.png)

Ensuite, retournez dans votre canal et faites un clic droit sur votre message original 100 Days of Code. Vous devriez voir une option dans le menu contextuel pour copier l'ID du message :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-164.png)

Sélectionnez cette option et vous obtiendrez un ID (le mien était `855559921666621441`). Ensuite, dans le même canal, utilisez `!edit 855559921666621441 Ce message a été modifié !`, en remplaçant ma valeur par celle que vous avez obtenue de l'option "Copier l'ID". Le bot devrait modifier l'embed existant avec votre nouveau contenu.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-165.png)

### Commande Help

Vous y êtes presque ! Il ne reste plus qu'une commande. De nombreux bots ont une commande `help`, qui retourne une liste des commandes disponibles. Vous devriez en ajouter une à votre bot également.

Une dernière fois, créez un fichier `help` dans votre répertoire `commands`. Importez votre interface `CommandInt` et configurez votre commande comme `help`. Définissez le `name` sur `"help"`, et la `description` sur quelque chose comme `"Retourne des informations sur les commandes disponibles du bot."`. Configurez votre fonction `run`. 

Cette fois, vous n'avez besoin que de la propriété `channel` du message, donc pas besoin de déstructurer quoi que ce soit ici. Au lieu de cela, importez la classe `MessageEmbed` de `discord.js`, et allez-y et importez également votre liste de commandes : `import { CommandList } from "./_CommandList";`.

Construisez un nouvel `MessageEmbed` et attribuez-le à une variable `helpEmbed`. Définissez le `title` sur `"Commandes disponibles :"` et la description sur quelque chose de similaire à `"Ce sont les commandes disponibles pour ce bot."`.

Maintenant, vous devez ajouter un champ à l'embed et générer dynamiquement la liste des commandes. Commencez par ajouter le champ avec `helpEmbed.addField()`. Utilisez le premier paramètre pour définir le nom du champ sur `"Commandes :"`. Pour la description (le deuxième paramètre), vous allez utiliser le tableau `CommandList` pour générer une liste lisible de commandes.

```ts
    helpEmbed.addField(
      "Commandes :",
      CommandList.map((el) => `\`!${el.name}\`: ${el.description}`).join("\n")
    );
```

Le processus ici est en deux parties. Tout d'abord, en utilisant la méthode de tableau intégrée `.map`, vous créez un nouveau tableau à partir de votre tableau d'objets `CommandInt`. Ce tableau contient des chaînes formatées en utilisant Markdown pour que le nom de la commande et la description soient lisibles. La chaîne pour votre commande d'aide ressemblerait à ceci :

> `!help` : Retourne des informations sur les commandes disponibles du bot.

Vous joignez ensuite ce tableau de chaînes avec un séparateur de nouvelle ligne, ce qui créera une liste verticale de commandes dans une seule chaîne (les champs d'embed nécessitent des chaînes pour la description).

Envoyez l'embed au canal. Parce que vous n'avez pas déstructuré la propriété `channel` de l'objet `message`, vous devrez utiliser `message.channel.send(helpEmbed);` directement. 

Cette fois, ne supprimez pas le message original – vous n'avez pas ajouté d'auteur à l'embed d'aide, donc préserver le message original aide les modérateurs à voir qui a utilisé la commande. Votre commande d'aide devrait ressembler à ceci :

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { MessageEmbed } from "discord.js";
import { CommandList } from "./_CommandList";

export const help: CommandInt = {
  name: "help",
  description: "Retourne des informations sur les commandes disponibles du bot.",
  run: async (message) => {
    const helpEmbed = new MessageEmbed();
    helpEmbed.setTitle("Commandes disponibles !");
    helpEmbed.setDescription(
      "Ce sont les commandes disponibles pour ce bot."
    );
    helpEmbed.addField(
      "Commandes :",
      CommandList.map((el) => `\`!${el.name}\`: ${el.description}`).join("\n")
    );

    await message.channel.send(helpEmbed);
  },
};

```

Importez votre commande `help` dans votre fichier `_CommandList.ts` et ajoutez la commande à votre tableau. Avec cette commande finale, votre fichier `_CommandList.ts` devrait être :

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { oneHundred } from "./oneHundred";
import { view } from "./view";
import { edit } from "./edit";
import { help } from "./help";

export const CommandList: CommandInt[] = [oneHundred, view, edit, help];

```

Utilisez `npm run build` et `npm start` une dernière fois pour tester cette fonctionnalité. Envoyez `!help` dans votre canal et le bot devrait répondre :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-167.png)

## Conclusion

Félicitations ! Vous avez réussi à construire un bot Discord pour le défi 100 Days of Code.

Si vous êtes intéressé à explorer davantage, vous pouvez consulter [le code source](https://github.com/nhcarrigan/100-days-of-code-bot) du bot en direct qui a inspiré ce tutoriel, qui inclut la journalisation personnalisée des erreurs, le rapport d'erreurs externe et un site de documentation.