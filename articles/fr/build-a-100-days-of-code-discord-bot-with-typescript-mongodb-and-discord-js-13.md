---
title: Créer un bot Discord pour le défi 100 Days of Code avec TypeScript, MongoDB
  et Discord.js 13
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-01-31T21:41:05.000Z'
originalURL: https://freecodecamp.org/news/build-a-100-days-of-code-discord-bot-with-typescript-mongodb-and-discord-js-13
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-kindel-media-8566473.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: bots
  slug: bots
- name: coding challenge
  slug: coding-challenge
- name: discord
  slug: discord
- name: freeCodeCamp.org
  slug: freecodecamp
seo_title: Créer un bot Discord pour le défi 100 Days of Code avec TypeScript, MongoDB
  et Discord.js 13
seo_desc: 'The 100 Days of Code challenge is very popular among new coders and developers
  looking to level up their skills. It''s so popular that our Discord server has an
  entire channel dedicated to it.

  By popular demand, we built a Discord bot that helps peopl...'
---

Le [défi 100 Days of Code](https://www.freecodecamp.org/news/the-crazy-history-of-the-100daysofcode-challenge-and-why-you-should-try-it-for-2018-6c89a76e298d/) est très populaire parmi les nouveaux codeurs et les développeurs cherchant à améliorer leurs compétences. Il est si populaire que notre [serveur Discord](https://www.freecodecamp.org/news/freecodecamp-discord-chat-room-server/) possède un canal entier dédié à ce défi.

Par demande populaire, nous avons créé un bot Discord qui aide les gens à suivre leur progression dans le défi.

Aujourd'hui, je vais vous montrer comment créer votre propre bot pour le défi 100 Days of Code.

> Notez que discord.js a publié la version 14, qui inclut des changements majeurs. Pour la compatibilité avec ce tutoriel, vous devrez vous assurer d'utiliser discord.js 13 - vous pouvez l'installer avec `npm install discord.js@13`. Si vous avez des questions, n'hésitez pas à rejoindre mon [serveur discord](https://chat.nhcarrigan.com). 

<details>
    <summary>Contenu</summary>
    <ul>
        <li>
            <a href="#creer-une-application-de-bot-discord">Créer une application de bot Discord</a>
        </li>
        <li>
            <a href="#configurer-votre-projet">Configurer votre projet</a>
        </li>
        <li>
            <a href="#creer-le-bot-discord">Créer le bot Discord</a>
        </li>
        <li>
            <a href="#evenements-de-passerelle-dans-discord">Événements de passerelle dans Discord</a>
        </li>
        <li>
            <a href="#se-connecter-a-la-base-de-donnees">Se connecter à la base de données</a>
        </li>
        <li>
            <a href="#validation-des-variables-denvironnement">Validation des variables d'environnement</a>
        </li>
        <li>
            <a href="#levenement-interaction">L'événement "interaction"</a>
        </li>
        <li>
            <a href="#preparer-les-commandes">Préparer les commandes</a>
        </li>
        <li>
            <a href="#modele-de-base-de-donnees">Modèle de base de données</a>
        </li>
        <li>
            <a href="#ecrire-les-commandes-du-bot">Écrire les commandes du bot</a>
        </li>
    </ul>
</details>

## Créer une application de bot Discord

Votre première étape consiste à configurer une application de bot Discord. Rendez-vous sur le [Portail des développeurs Discord](https://discord.dev), connectez-vous si nécessaire, et sélectionnez "Applications" dans la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-76.png)
_Capture d'écran du Portail des développeurs. Si c'est votre premier bot, vous n'aurez aucune application ici._

Cliquez sur le bouton "Nouvelle Application". Donnez-lui un nom, et définissez-la comme une application "Personnelle". Vous serez maintenant redirigé vers les paramètres de l'application. Ici, vous pouvez changer le nom, ou lui donner un avatar.

Sélectionnez "Bot" dans la barre latérale, puis cliquez sur le bouton "Ajouter un Bot". Cela créera un compte de bot Discord pour votre application.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-77.png)
_Capture d'écran de la page des paramètres du Bot. Si vous n'avez pas défini d'avatar, vous verrez un avatar par défaut basé sur le nom de votre bot._

C'est sur cet écran que vous obtiendrez le token du bot. Il est _très_ important de garder ce token secret, car le token permet à votre code de se connecter à votre bot. Gardez-le en sécurité et ne le partagez avec personne.

Maintenant, vous devez ajouter le bot à un serveur pour interagir avec lui. Cliquez sur l'option "OAuth2" dans la barre latérale, puis sélectionnez "Générateur d'URL".

Sous "Portées", sélectionnez `bot` et `application.commands`. La portée `bot` permet à votre compte de bot de rejoindre le serveur, et la portée `application.commands` vous permet de mettre à jour les commandes slash (plus d'informations à ce sujet plus tard).

Lorsque vous sélectionnez `bot`, une nouvelle section pour "Autorisations du Bot" apparaîtra. Sélectionnez les autorisations suivantes :

* Envoyer des messages
* Intégrer des liens
* Lire les messages/Voir les canaux

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-78.png)
_Capture d'écran de l'écran OAuth avec les paramètres requis._

Copiez l'URL générée, et collez-la dans votre navigateur. Cela vous guidera à travers le processus de Discord pour ajouter votre nouveau bot à un serveur. 

Notez que vous devez avoir la permission de gérer le serveur dans lequel vous souhaitez ajouter le bot. Si vous n'avez pas cette permission, vous pouvez créer un serveur pour tester votre bot.

Maintenant, vous êtes prêt à écrire du code !

## Configurer votre projet

Vous devrez d'abord configurer l'infrastructure et les outils pour votre projet.

Assurez-vous d'avoir Node.js **version 16** et `npm` installés. Notez que les packages que vous allez utiliser ne supportent pas les versions antérieures de Node.

### Préparer le `package.json`

Créez un répertoire, ou dossier, pour votre projet. Ouvrez votre terminal en pointant vers ce nouveau dossier. Exécutez la commande `npm init` pour configurer votre fichier `package.json`. Pour ce tutoriel, les valeurs par défaut sont suffisantes, mais vous pouvez les modifier comme vous le souhaitez.

Vous devriez obtenir un `package.json` similaire à ceci :

```json
{
  "name": "100doc-tutorial",
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

Le script `build` compilera votre TypeScript en JavaScript pour que Node puisse l'exécuter, et le script `start` exécutera le fichier d'entrée `index.js`.

L'ajout de `-r dotenv/config` ici importera et exécutera dynamiquement la méthode `config` dans le package `dotenv`, qui charge vos variables d'environnement à partir du fichier `.env`.

En parlant de packages, votre prochaine étape consiste à installer les dépendances. En utilisant `npm install`, installez ces dépendances :

* `discord.js` – c'est la bibliothèque qui gérera la connexion à la passerelle et la gestion des appels à l'API Discord.
* `@discordjs/builders` – le package discord.js pour construire des commandes d'application
* `@discordjs/rest` – un client API personnalisé pour interagir avec l'API REST de Discord.
* `discord-api-types` – Définitions de types et gestionnaires pour l'API REST de Discord.
* `dotenv` – un package qui charge les valeurs `.env` dans le processus Node.
* `mongoose` – Un wrapper pour la connexion MongoDB qui offre des outils pour structurer vos données.

Enfin, installez les dépendances de développement avec `npm install --save-dev`. Les dépendances de développement sont des packages nécessaires pour travailler sur votre projet dans un environnement de développement, mais pas pour exécuter le code en production.

* `typescript` – C'est le package pour le langage TypeScript, qui inclut tout ce dont vous avez besoin pour écrire du code en TypeScript et le compiler en JavaScript.
* `@types/node` – TypeScript s'appuie sur des définitions de types pour comprendre le code que vous écrivez. Ce package définit les types pour l'environnement d'exécution Node.js, comme l'objet `process.env`.

Avec ces packages installés, vous devriez maintenant avoir un `package.json` similaire à ceci :

```json
{
  "name": "100doc-tutorial",
  "version": "1.0.0",
  "description": "",
  "main": "./prod/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node -r dotenv/config ./prod/index.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@discordjs/builders": "^0.11.0",
    "@discordjs/rest": "^0.2.0-canary.0",
    "discord.js": "^13.6.0",
    "dotenv": "^14.2.0",
    "mongoose": "^6.1.7"
  },
  "devDependencies": {
    "@types/node": "^17.0.10",
    "typescript": "^4.5.4"
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

Le fichier `.gitignore` indique à `git` de ne pas suivre les fichiers/dossiers qui correspondent aux motifs que vous entrez. Ignorer le dossier `node_modules` empêche votre dépôt de devenir trop volumineux.

Pousser le JavaScript compilé est également inutile, car votre projet est généralement compilé en production avant l'exécution. Les fichiers `.env` contiennent des valeurs secrètes, telles que des clés API et des tokens, ils ne doivent donc pas être validés dans un dépôt.

## Créer le bot Discord

Votre prochaine étape consiste à préparer la connexion initiale du bot. Si vous ne l'avez pas fait plus tôt, créez un répertoire `src` et un fichier `index.ts` à l'intérieur.

Commencez par une expression de fonction immédiatement invoquée anonyme (IIFE) pour permettre l'utilisation de `await` au niveau supérieur :

```ts
(async () => {

})();
```

Dans cette fonction, vous allez instancier votre bot Discord. En haut du fichier, importez la classe `Client` avec `import { Client } from "discord.js";`. La classe `Client` représente la session de votre bot Discord.

À l'intérieur de votre fonction, construisez une nouvelle instance de `Client` et attribuez-la à une variable `BOT` avec `const BOT = new Client();`. Maintenant, la variable `BOT` représentera votre bot.

Pour connecter votre bot à la passerelle Discord et commencer à recevoir des événements, vous devrez utiliser la méthode `.login()` sur votre instance de bot. La méthode `.login()` prend un seul argument, qui est le token pour l'application de bot que vous avez créée précédemment.

De nombreuses méthodes dans `discord.js` sont asynchrones, vous devrez donc utiliser `await` ici. Ajoutez la ligne `await BOT.login(process.env.BOT_TOKEN);` à votre IIFE.

Votre fichier `index.ts` devrait maintenant ressembler à ceci :

```ts
import { Client } from "discord.js";

(async () => {
  const BOT = new Client();

  await BOT.login(process.env.BOT_TOKEN);
})();
```

Si vous essayez d'exécuter `npm run build`, vous verrez une erreur : `An argument for 'options' was not provided.`

Dans discord.js 13, vous devez spécifier les Intents de la passerelle lorsque vous instanciez votre bot. Les Intents de la passerelle indiquent à Discord quels événements votre bot doit recevoir.

Dans votre dossier `src`, créez un dossier `config` - puis dans `config`, créez un fichier `IntentOptions.ts`.

Dans ce nouveau fichier, ajoutez la ligne `export const IntentOptions = ["GUILDS"]`. Cela indiquera à Discord que votre bot doit recevoir les événements de Guild.

Ensuite, dans votre fichier `index.ts`, ajoutez un argument à votre appel `new Client()` : `new Client({intents: IntentOptions})`. Vous devrez l'importer en haut de votre fichier avec `import { IntentOptions } from "./config/IntentOptions;`. 

Il semble que vous ayez encore une erreur : `Type 'string' is not assignable to type 'number | `${bigint}` | IntentsString | Readonly<BitField<IntentsString, number>> | RecursiveReadonlyArray<number | `${bigint}` | IntentsString | Readonly<...>>'.`

TypeScript infère que votre tableau `IntentOptions` est une chaîne, mais le constructeur `Client` attend des types plus spécifiques. 

Retournez à votre fichier `config/IntentOptions.ts` et ajoutez une autre importation : `import { IntentsString } from "discord.js"`. Ensuite, mettez à jour votre variable avec la nouvelle définition de type : `export const IntentOptions: IntentsString[] = ["GUILDS"];`.

Maintenant, `npm run build` devrait réussir. Si vous avez ajouté votre nouveau bot à un serveur Discord, l'exécution de `npm start` devrait montrer que votre bot est en ligne sur ce serveur. Cependant, le bot ne répondra à rien pour l'instant, car vous n'avez pas encore commencé à écouter les événements.

## Événements de passerelle dans Discord

Les événements de "passerelle" sont générés lorsqu'une action se produit sur Discord, et sont généralement envoyés aux clients (y compris votre bot) sous forme de charges utiles JSON. Vous pouvez écouter ces événements avec la méthode `.on()`, ce qui vous permet d'écrire la logique que votre bot doit suivre lorsque des événements spécifiques se produisent.

Le premier événement à écouter est l'événement "ready". Cet événement se déclenche lorsque votre bot s'est connecté à la passerelle et est _prêt_ à traiter les événements. Au-dessus de votre appel `.login()`, ajoutez `BOT.on("ready", () => console.log("Connecté à Discord !"));`. 

Pour que vos modifications prennent effet, utilisez `npm run build` à nouveau pour compiler le nouveau code. Maintenant, si vous essayez `npm run start`, vous devriez voir "Connecté à Discord !" s'afficher dans votre terminal.

## Se connecter à la base de données

Vous allez utiliser le package `mongoose` pour vous connecter à une instance MongoDB. Si vous préférez, vous pouvez exécuter MongoDB localement, ou vous pouvez utiliser le niveau gratuit de MongoDB Atlas pour une solution basée sur le cloud. 

Si vous n'avez pas de compte MongoDB Atlas, freeCodeCamp a un [excellent tutoriel pour en créer un](https://www.freecodecamp.org/news/get-started-with-mongodb-atlas/).

Récupérez votre chaîne de connexion pour votre base de données et ajoutez-la à votre fichier `.env` sous la forme `MONGO_URI=""`, avec la chaîne de connexion entre les guillemets. Pour le nom de la base de données, utilisez `oneHundredDays`.

Créez un répertoire appelé `database` pour contenir les fichiers qui contiennent votre logique de base de données. Dans ce répertoire, créez un fichier appelé `connectDatabase.ts`. Vous allez écrire votre logique pour initier la connexion à la base de données ici.

Commencez par une déclaration de fonction exportée :

```ts
export const connectDatabase = async () => {

}
```

`mongoose` offre une méthode `connect` pour se connecter à la base de données. Importez-la avec `import { connect } from "mongoose";` en haut de votre fichier.

Ensuite, utilisez la méthode à l'intérieur de votre fonction avec `await connect(process.env.MONGO_URI);`. Ajoutez une instruction `console.log` après cela pour que vous puissiez identifier que votre bot s'est connecté à la base de données. 

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
_Une erreur de compilation, indiquant que : Argument de type string ou undefined n'est pas assignable au paramètre de type string._

Oh non — une erreur !

## Validation des variables d'environnement

Le problème avec les variables d'environnement est qu'elles peuvent toutes être `undefined`. Cela se produit souvent si vous faites une faute de frappe dans le nom de votre variable d'environnement, ou si vous confondez le nom avec un autre nom (une erreur que j'ai faite en écrivant ce tutoriel, en utilisant `TOKEN` au lieu de `BOT_TOKEN` à certains endroits).

TypeScript vous avertit que la méthode `connect` prend une chaîne de caractères, et qu'une valeur `undefined` va tout casser. Vous pouvez corriger cela, mais d'abord, vous allez vouloir écrire une fonction pour gérer la validation de vos variables d'environnement.

Dans votre répertoire `src`, créez un répertoire `utils` pour contenir vos fonctions utilitaires. Ajoutez un fichier `validateEnv.ts` là.

Créez une fonction dans le fichier appelée `validateEnv`. Cette fonction sera synchrone et n'a pas besoin du mot-clé `async`. Dans cette fonction, ajoutez des conditions pour vérifier vos deux variables d'environnement. Si l'une d'elles est manquante, retournez `false`. Sinon, retournez `true`.

Votre code pourrait ressembler à ceci :

```ts
export const validateEnv = () => {
  if (!process.env.BOT_TOKEN) {
    console.warn("Token de bot Discord manquant.");
    return false;
  }

  if (!process.env.MONGO_URI) {
    console.warn("Connexion MongoDB manquante.");
    return false;
  }
  return true;
};


```

Retournez à votre fichier `index.ts` et importez cette fonction de validation avec `import { validateEnv } from "./utils/validateEnv"`. Ensuite, au début de votre IIFE, utilisez une instruction if pour retourner tôt si la fonction retourne false. Votre `index.ts` devrait ressembler à ceci :

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

## L'événement "interaction"

Bien que vous fassiez de grands progrès sur votre bot, il ne _fait_ toujours rien. Pour recevoir des commandes, vous devrez créer un autre écouteur d'événements.

Discord a lancé les commandes slash, présentant une nouvelle interface utilisateur et un nouvel événement de passerelle. L'événement `interactionCreate` est déclenché lorsqu'une personne utilise une commande slash avec votre bot. C'est l'événement que vous allez vouloir écouter. Comme la logique est un peu plus compliquée que l'événement `ready`, vous allez vouloir créer un fichier séparé.

Dans votre répertoire `src`, créez un répertoire `events`, et un fichier `onInteraction.ts` dedans. Commencez par définir une fonction exportée `onInteraction`. Il s'agit d'une fonction asynchrone, avec un seul paramètre appelé `interaction`.

```ts
export const onInteraction = async (interaction) => {

};

```

Pour fournir une définition de type pour votre paramètre, importez le type `Interaction` de `discord.js`.

```ts
import { Interaction } from "discord.js";

export const onInteraction = async (interaction: Interaction) => {

};

```

L'événement `interaction` se déclenche en réalité sur toute interaction de commande, ce qui inclut des choses comme les clics sur les boutons et les menus de sélection, ainsi que les commandes slash que nous voulons. 

Puisque vous n'écrirez que des commandes slash pour ce bot, vous pouvez filtrer tout autre type d'interaction et aider TypeScript à comprendre les données avec lesquelles vous travaillez.

Dans votre nouvelle fonction, ajoutez une condition pour vérifier `interaction.isCommand()`. Vous écrirez la logique dans ce bloc plus tard.

```ts
import { Interaction } from "discord.js";

export const onInteraction = async (interaction: Interaction) => {
  if (interaction.isCommand()) {
  }
};

```

Maintenant, dans votre fichier `index.ts`, vous pouvez monter un autre écouteur. À côté de votre écouteur `.on("ready")`, ajoutez un écouteur `BOT.on("interactionCreate")`. Pour cet événement, la fonction de rappel prend un argument `interaction` que vous pouvez passer à votre nouvelle fonction `onInteraction`.

```ts
  BOT.on(
    "interactionCreate",
    async (interaction) => await onInteraction(interaction)
  );
```

Super ! Vous pouvez exécuter `npm run build` pour confirmer que TypeScript ne génère aucune erreur, mais sans commandes réelles à utiliser, vous ne pouvez pas encore tester ce code.

## Préparer les commandes

Je maintient quelques bots Discord, et une chose que j'ai découverte qui aide à garder le code maintenable et lisible est de rendre les composants modulaires.

### Définir une interface

Vous devrez d'abord définir une structure commune pour vos commandes. Créez un dossier `interfaces` dans `src`. Ensuite, à l'intérieur de `interfaces`, créez un fichier appelé `Command.ts`.

Maintenant, vous allez créer une interface. En TypeScript, une interface est souvent utilisée pour définir la structure d'un objet, et est l'un des nombreux outils disponibles pour déclarer le type d'une variable.

Dans votre fichier `Command.ts`, créez une interface exportée appelée `Command` :

```ts
export interface Command {

}
```

Votre interface aura deux propriétés – `data`, qui contiendra les données de commande à envoyer à Discord, et `run`, qui contiendra la fonction de rappel et la logique de commande.

Pour la propriété `data`, importez `SlashCommandBuilder` et `SlashCommandSubcommandsOnlyBuilder` de `@discordjs/builders`. Définissez la propriété `data` comme l'un de ces deux types.

Pour la propriété `run`, importez le type `CommandInteraction` de `discord.js`. Définissez `run` comme une fonction qui prend un paramètre typé `CommandInteraction` et retourne une promesse `void`.

```ts
import {
  SlashCommandBuilder,
  SlashCommandSubcommandsOnlyBuilder,
} from "@discordjs/builders";
import { CommandInteraction } from "discord.js";

export interface CommandInt {
  data: SlashCommandBuilder | SlashCommandSubcommandsOnlyBuilder;
  run: (interaction: CommandInteraction) => Promise<void>;
}

```

### Créer une liste de commandes

Ensuite, vous avez besoin d'un endroit pour stocker toutes vos commandes. Créez un dossier appelé `commands` dans le répertoire `src`, et ajoutez un fichier appelé `_CommandList.ts`. Le tiret bas ici gardera ce fichier en haut de la liste.

Le fichier `_CommandList.ts` aura besoin de deux lignes. Tout d'abord, importez votre interface `Command`, puis déclarez un tableau `CommandList`. Le tableau sera vide pour l'instant, mais donnez-lui un type `Command[]` pour que TypeScript sache qu'il contiendra éventuellement vos objets de commande. Le fichier devrait ressembler à ceci :

```ts
import { Command } from "../interfaces/Command";

export const CommandList: Command[] = [];
```

Le but de ce fichier est de créer un tableau des commandes de votre bot que vous allez parcourir dans l'écouteur d'événements d'interaction. [Il existe des moyens d'automatiser cela](https://github.com/BeccaLyria/discord-bot/blob/main/src/utils/readDirectory.ts), mais ils tendent à être inutilement complexes pour les petits bots.

### Vérifier les commandes

Retournez dans votre fichier `onInteraction.ts`, vous devriez commencer à travailler sur la logique pour trouver et exécuter une commande.

Dans votre bloc de condition `interaction.isCommand()`, parcourez le tableau `CommandList` (n'oubliez pas de l'importer !) avec une boucle `for...of`. 

```ts
for (const Command of CommandList) {

}
```

La charge utile d'interaction reçue de Discord inclut une propriété `commandName`, que vous pouvez utiliser pour trouver la commande qu'un utilisateur a sélectionnée. Pour vérifier cela, comparez `interaction.commandName` avec la propriété `Command.data.name`.

```ts
if (interaction.commandName === Command.data.name) {

}
```

Maintenant, si vous avez trouvé la commande que l'utilisateur a choisie, vous devez exécuter la logique pour cette commande. Cela est réalisé avec un appel `Command.run(interaction)` – en passant la charge utile d'interaction dans la commande.

Votre fichier final devrait ressembler à ceci :

```ts
import { Interaction } from "discord.js";
import { CommandList } from "../commands/_CommandList";

export const onInteraction = async (interaction: Interaction) => {
  if (interaction.isCommand()) {
    for (const Command of CommandList) {
      if (interaction.commandName === Command.data.name) {
        await Command.run(interaction);
        break;
      }
    }
  }
};

```

## Modèle de base de données

Il y a une étape de plus avant que vous ne soyez prêt à commencer à écrire des commandes. Ce bot suivra la progression des membres de votre communauté dans le défi 100 Days of Code. Et vous devez stocker cette progression dans la base de données.

`mongoose` aide à structurer vos enregistrements MongoDB pour vous empêcher de passer des données malformées ou incomplètes dans votre base de données.

Commencez par créer un dossier `models` dans votre répertoire `database`. Dans ce dossier `models`, créez un fichier `CamperModel.ts`. Ce sera votre structure pour les objets utilisateurs.

Vous devez d'abord importer les valeurs nécessaires de la bibliothèque `mongoose`. Ajoutez `import { Document, model, Schema } from "mongoose";` en haut du fichier.

Parce que vous utilisez TypeScript, vous devez créer une définition de type pour vos objets de base de données. Créez une autre interface, comme vous l'avez fait pour vos commandes, nommée `CamperInt`.

```ts
export interface CamperInt extends Document {

}
```

Votre modèle de base de données aura quatre propriétés. Ajoutez celles-ci à votre interface :

* `discordId: string;` – Chaque objet utilisateur dans Discord a un identifiant unique, appelé un Snowflake, qui est utilisé pour les distinguer des autres utilisateurs. Contrairement à un nom d'utilisateur ou à un discriminateur (le nombre à quatre chiffres après le nom d'utilisateur), la valeur `id` ne peut pas être changée. Cela en fait la valeur idéale pour lier vos données stockées à un utilisateur Discord.
* `round: number;` – Cela représentera le "round" auquel l'utilisateur est dans le défi. Lorsque quelqu'un termine 100 jours du défi, il peut choisir de relever à nouveau le défi. Lorsqu'il le fait, il fait souvent référence à cela comme "round 2", par exemple. 
* `day: number;` – Cela représente le jour auquel l'utilisateur est dans le défi.
* `timestamp: number;` – Vous utiliserez cette valeur pour suivre quand l'utilisateur a soumis pour la dernière fois un message pour le défi 100 Days of Code.

Super ! Maintenant, vous devez définir le Schéma pour vos entrées de base de données. `mongoose` utilise un objet Schema pour définir la forme des documents qui vont dans votre collection de base de données. Le `Schema` import a un constructeur, que vous allez assigner à une variable.

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

Si vous utilisiez JavaScript, cela serait suffisant pour configurer votre modèle de base de données. Cependant, parce que vous utilisez TypeScript, vous devriez tirer parti de la sécurité des types. `model()` par défaut retourne un type `Document` de `any`. 

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

En tant que vérification de sécurité, utilisez `npm run build` à nouveau. Vous ne devriez voir aucune erreur dans le terminal.

## Écrire les commandes du bot

Vous êtes enfin prêt à commencer à écrire quelques commandes ! Comme il s'agit d'un bot pour le défi 100 Days of Code, vous devriez commencer par la commande pour créer une mise à jour du défi 100 Days of Code.

### Commande 100

Dans votre dossier `commands`, créez un fichier `oneHundred.ts`. Cela contiendra votre commande pour le défi 100 Days of Code. Importez votre interface de commande avec `import { Command } from "../interfaces/Command;`.

Maintenant, déclarez une variable exportée `oneHundred` et donnez-lui le type `Command` :

```ts
import { Command } from "../interfaces/Command";

export const oneHundred: Command = {

};
```

Tout d'abord, créez la propriété `data`. Vous allez utiliser le package `@discordjs/builders` pour construire une commande slash.

Commencez par importer le `SlashCommandBuilder()` du package `@discordjs/builders`. Ensuite, construisez une nouvelle instance dans la propriété `data` avec `new SlashCommandBuilder()`. Vous allez enchaîner quelques méthodes ici pour passer les informations que vous souhaitez dans le constructeur.

La méthode `.setName()` vous permet de définir le nom de votre commande slash. Définissez le nom sur `"100"`. L'option `setDescription()` vous permet d'afficher une description de la commande dans l'interface utilisateur de Discord. Définissez la description sur `"Faites un check-in pour le défi 100 Days of Code."`.

Les commandes slash peuvent également accepter des valeurs d'`option`. Celles-ci sont utilisées pour prendre des arguments de l'utilisateur, et viennent dans divers types. Pour cette commande, vous voulez une option de chaîne avec la méthode `addStringOption()`. Les méthodes d'option prennent une fonction de rappel, avec un paramètre `option`.

Vous pouvez ensuite enchaîner des méthodes sur le paramètre `option` pour configurer les informations pour l'argument. Utilisez la méthode `.setName()` pour donner à l'option un nom de `"message"`, et la méthode `.setDescription()` pour lui donner une description de `"Le message à mettre dans votre mise à jour 100 Days of Code."`. Enfin, utilisez la méthode `.setRequired()` pour définir l'option comme requise.

Voici ce que vous devriez avoir maintenant :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";

export const oneHundred: Command = {
  data: new SlashCommandBuilder()
    .setName("100")
    .setDescription("Faites un check-in pour le défi 100 Days of Code.")
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("Le message à mettre dans votre mise à jour 100 Days of Code.")
        .setRequired(true)
    ),
};

```

Si vous codez dans un IDE avec Intellisense activé, vous avez peut-être remarqué que cela générera une erreur de type sur la propriété `data`. Cela est dû au fait que le `SlashCommandBuilder` retourne en réalité un type `Omit` ! Un type `Omit` est utilisé pour indiquer à TypeScript que le type est _presque_ le même qu'un autre type, mais avec des propriétés spécifiques supprimées.

Rendez-vous dans votre fichier `interfaces/Command.ts` pour mettre à jour le type. Remplacez le type `SlashCommandBuilder` par `Omit<SlashCommandBuilder, "addSubcommandGroup" | "addSubcommand">`. Cela indiquera à TypeScript que `data` doit être un `SlashCommandBuilder`, mais sans ces deux propriétés spécifiques.

```ts
import {
  SlashCommandBuilder,
  SlashCommandSubcommandsOnlyBuilder,
} from "@discordjs/builders";
import { CommandInteraction } from "discord.js";

export interface Command {
  data:
    | Omit<SlashCommandBuilder, "addSubcommandGroup" | "addSubcommand">
    | SlashCommandSubcommandsOnlyBuilder;
  run: (interaction: CommandInteraction) => Promise<void>;
}

```

Super ! Maintenant que votre erreur de type est résolue, retournez dans votre fichier de commande `oneHundred.ts` – il est temps d'écrire la logique de la commande.

Toute la logique de votre bot pour répondre à la commande ira dans la propriété `run`. Comme vous l'avez fait dans votre interface, commencez par créer une fonction asynchrone qui prend un argument `interaction`. Ensuite, laissez la première ligne de votre fonction être `await interaction.deferReply();`.

Discord s'attend à ce qu'un bot réponde à une commande dans les trois secondes. Parce que cette commande peut prendre plus de temps à traiter, l'utilisation de la méthode `.deferReply()` envoie une réponse d'accusé de réception qui vous donne un délai complet de 15 minutes pour envoyer la réponse réelle.

Ensuite, vous devez extraire certaines données de la commande. Tout d'abord, déstructurez l'objet `user` de la charge utile d'interaction avec `const { user } = interaction;`. L'objet `user` représente l'utilisateur Discord qui a appelé la commande. 

Ensuite, obtenez l'option `message` que vous avez envoyée avec `const text = interaction.options.getString("message", true);`. Avec cette ligne, vous accédez à la propriété `options` de l'interaction. La méthode `.getString()` récupère spécifiquement une option de chaîne (rappellez-vous que vous avez créé l'option dans `data`), et `"message"` est le **nom** de l'option. L'argument `true` indique que cette option est requise, donc TypeScript ne la considérera pas comme nullable.

Votre fichier devrait ressembler à ceci :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";

export const oneHundred: Command = {
  data: new SlashCommandBuilder()
    .setName("100")
    .setDescription("Faites un check-in pour le défi 100 Days of Code.")
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("Le message à mettre dans votre mise à jour 100 Days of Code.")
        .setRequired(true)
    ),
  run: async (interaction) => {
    await interaction.deferReply();
    const { user } = interaction;
    const text = interaction.options.getString("message", true);
  },
};

```

L'étape suivante de cette commande consisterait à récupérer des données de votre base de données. Parce que beaucoup de vos commandes devront faire cela, vous devriez créer un module pour cela.

### Gérer la logique de la base de données

Créez un répertoire `src/modules`, et ajoutez un fichier `getCamperData.ts` à l'intérieur. Créez une fonction asynchrone exportée nommée `getCamperData`, et donnez-lui un paramètre de chaîne nommé `id`. Ensuite, dans la fonction, vous pouvez interroger la base de données.

Importez votre `CamperModel` du répertoire `database`, et utilisez la méthode `findOne()` pour interroger par l'`id` du camper : `const camperData = await CamperModel.findOne({ discordId: id });`. 

```ts
import CamperModel from "../database/models/CamperModel";

export const getCamperData = async (id: string) => {
  const camperData = await CamperModel.findOne({ id });
};

```

Nous avons encore une étape ici. Si le camper n'a pas utilisé le bot auparavant, il n'aura pas d'enregistrement de base de données existant. `findOne()` retournerait `null` dans ce cas – vous pouvez donc ajouter une valeur de repli.

```ts
import CamperModel from "../database/models/CamperModel";

export const getCamperData = async (id: string) => {
  const camperData =
    (await CamperModel.findOne({ discordId: id })) ||
    (await CamperModel.create({
      discordId: id,
      round: 1,
      day: 0,
      date: Date.now(),
    }));
};

```

Enfin, vous devez `retourner` vos données. Ajoutez `return camperData` à la fin de la fonction. Pour une sécurité de type supplémentaire, définissez le type de retour de votre fonction comme `Promise<CamperData>`.

```ts
import CamperModel, { CamperInt } from "../database/models/CamperModel";

export const getCamperData = async (id: string): Promise<CamperInt> => {
  const camperData =
    (await CamperModel.findOne({ discordId: id })) ||
    (await CamperModel.create({
      discordId: id,
      round: 1,
      day: 0,
      date: Date.now(),
    }));
  return camperData;
};

```

Vous avez maintenant un moyen d'obtenir les données des campeurs depuis la base de données, mais vous avez besoin d'un moyen de les mettre à jour également. Créez un autre fichier dans votre répertoire `/src/modules` appelé `updateCamperData.ts`. Cela gérera la logique pour incrémenter la progression d'un campeur.

Commencez par une fonction asynchrone exportée appelée `updateCamperData`. Elle devrait prendre un paramètre `Camper`, qui serait les données que vous récupérez de MongoDB.

```ts
import { CamperInt } from "../database/models/CamperModel";

export const updateCamperData = async (Camper: CamperInt) => {
    
};

```

La seule fois où vous mettrez à jour les données est dans la commande `/100` – où vous voudrez incrémenter le compteur de jours du campeur, vérifier s'il a commencé une nouvelle ronde, et mettre à jour le timestamp.

Tout d'abord, incrémentez le compteur de jours avec `Camper.day++;`. Avec la façon dont fonctionne le défi 100 Days of Code, si un campeur a dépassé le jour 100, alors il a commencé une nouvelle "ronde". Vous aurez besoin d'une condition pour vérifier si `Camper.day > 100`, et si c'est le cas, réinitialiser le jour à 1 et incrémenter la ronde. 

Après cette condition, mettez à jour le timestamp avec `Camper.timestamp = Date.now();` et sauvegardez les données avec `await Camper.save();`. Enfin, retournez l'objet de données modifié afin de pouvoir l'utiliser dans la commande.

Votre fichier final devrait ressembler à ceci :

```ts
import { CamperInt } from "../database/models/CamperModel";

export const updateCamperData = async (Camper: CamperInt) => {
  Camper.day++;
  if (Camper.day > 100) {
    Camper.day = 1;
    Camper.round++;
  }
  Camper.timestamp = Date.now();
  await Camper.save();
  return Camper;
};

```

### Commande 100 (suite)

Maintenant que votre logique de base de données est prête, retournez à votre fichier `oneHundred.ts`. Pour rappel, ce fichier devrait ressembler à ceci :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";

export const oneHundred: Command = {
  data: new SlashCommandBuilder()
    .setName("100")
    .setDescription("Faites un check-in pour le défi 100 Days of Code.")
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("Le message à mettre dans votre mise à jour 100 Days of Code.")
        .setRequired(true)
    ),
  run: async (interaction) => {
    await interaction.deferReply();
    const { user } = interaction;
    const text = interaction.options.getString("message", true);
  },
};

```

Importez vos deux nouveaux modules en haut du fichier. Ensuite, après votre logique qui extrait les valeurs de l'objet d'interaction, récupérez les données du campeur depuis la base de données avec `const targetCamper = await getCamperData(user.id);`. Mettez à jour les données avec `const updatedCamper = await updateCamperData(targetCamper);`.

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";
import { getCamperData } from "../modules/getCamperData";
import { updateCamperData } from "../modules/updateCamperData";

export const oneHundred: Command = {
  data: new SlashCommandBuilder()
    .setName("100")
    .setDescription("Faites un check-in pour le défi 100 Days of Code.")
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("Le message à mettre dans votre mise à jour 100 Days of Code.")
        .setRequired(true)
    ),
  run: async (interaction) => {
    await interaction.deferReply();
    const { user } = interaction;
    const text = interaction.options.getString("message", true);

    const targetCamper = await getCamperData(user.id);
    const updatedCamper = await updateCamperData(targetCamper);
  },
};

```

Maintenant, vous devez construire la réponse à envoyer au campeur lorsqu'il utilise la commande. 

Pour cela, vous allez utiliser la fonctionnalité d'intégration de messages de Discord. Commencez par importer le constructeur `MessageEmbed` de discord.js, et créez une nouvelle intégration avec `const oneHundredEmbed = new MessageEmbed();`. La classe `MessageEmbed` dispose de quelques méthodes à utiliser pour construire le contenu de l'intégration.

Utilisez la méthode `.setTitle()` pour définir le titre de l'intégration sur `"100 Days of Code"`. 

Utilisez la méthode `.setDescription()` pour définir la description de l'intégration sur le message que le campeur a fourni dans la commande (rappellez-vous que vous avez extrait cela dans la variable `text` plus tôt). L'auteur de l'intégration peut être défini et s'affichera en haut de l'intégration. 

Utilisez la méthode `.setAuthor()` pour passer un objet avec une propriété `name` définie sur `user.tag` (qui affichera le nom d'utilisateur et le discriminateur du campeur, comme `nhcarrigan#0001`), et une propriété `iconURL` définie sur `user.displayAvatarUrl()` (qui attachera l'avatar du campeur à l'intégration).

Les intégrations acceptent également des champs, qui sont des blocs de texte plus petits ayant leur propre titre et description. La méthode `.addField()` prend deux ou trois arguments, le premier étant le titre du champ, le second étant la description du champ, et le troisième étant un booléen facultatif pour définir le champ comme en ligne. 

Utilisez la méthode `.addField()` pour ajouter deux champs. Le premier doit avoir le titre défini sur `"Round"` et la description définie sur `updatedCamper.round.toString()`. Le second doit avoir le titre défini sur `"Day"` et la description définie sur `updatedCamper.day.toString()`. Les deux champs doivent être en ligne.

Pour la dernière partie de votre intégration, utilisez la méthode `.setFooter()` pour ajouter un petit texte de pied de page. Passez un objet avec une propriété `text` définie sur `"Day completed: " + new Date(updatedCamer.timestamp).toLocaleDateString()` pour afficher l'heure à laquelle le campeur a signalé sa progression.

Enfin, vous devez envoyer cette nouvelle intégration au campeur. Comme vous avez déjà envoyé une réponse avec l'appel `interaction.deferReply()`, vous ne pouvez pas envoyer une autre réponse. Au lieu de cela, vous devez modifier celle que vous avez envoyée.

Utilisez `await interaction.editReply()` pour modifier la réponse. La méthode `.editReply()` prend un objet avec diverses propriétés – dans ce cas, vous envoyez une intégration. Passez un objet avec une propriété `embeds` définie sur `[oneHundredEmbed]`. 

Notez qu'il s'agit d'un tableau contenant votre intégration. Les messages Discord peuvent contenir jusqu'à 10 intégrations, et l'API attend un tableau d'objets d'intégration pour correspondre.

Votre fichier de commande final devrait ressembler à ceci :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { MessageEmbed } from "discord.js";
import { Command } from "../interfaces/Command";
import { getCamperData } from "../modules/getCamperData";
import { updateCamperData } from "../modules/updateCamperData";

export const oneHundred: Command = {
  data: new SlashCommandBuilder()
    .setName("100")
    .setDescription("Faites un check-in pour le défi 100 Days of Code.")
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("Le message à mettre dans votre mise à jour 100 Days of Code.")
        .setRequired(true)
    ),
  run: async (interaction) => {
    await interaction.deferReply();
    const { user } = interaction;
    const text = interaction.options.getString("message", true);

    const targetCamper = await getCamperData(user.id);
    const updatedCamper = await updateCamperData(targetCamper);

    const oneHundredEmbed = new MessageEmbed();
    oneHundredEmbed.setTitle("100 Days of Code");
    oneHundredEmbed.setDescription(text);
    oneHundredEmbed.setAuthor({
      name: user.tag,
      iconURL: user.displayAvatarURL(),
    });
    oneHundredEmbed.addField("Round", updatedCamper.round.toString(), true);
    oneHundredEmbed.addField("Day", updatedCamper.day.toString(), true);
    oneHundredEmbed.setFooter({
      text:
        "Day completed: " +
        new Date(updatedCamper.timestamp).toLocaleDateString(),
    });

    await interaction.editReply({ embeds: [oneHundredEmbed] });
  },
};

```

### Enregistrement des commandes

Si vous exécutez `npm run build` et `npm start`, tout démarre – mais vous n'avez aucun moyen d'utiliser réellement votre nouvelle commande. Cela est dû au fait que Discord exige que les commandes soient enregistrées pour qu'elles soient disponibles dans l'interface de l'application. Il y a quelques étapes que nous devons suivre pour cela.

Tout d'abord, rendez-vous dans votre fichier `_CommandList.ts` et importez votre commande `oneHundred`. Ajoutez cela à votre tableau `CommandList` pour qu'il soit disponible ailleurs. 

```ts
import { Command } from "../interfaces/Command";
import { oneHundred } from "./oneHundred";

export const CommandList: Command[] = [oneHundred];

```

Maintenant, il est temps d'ajouter la logique pour envoyer les informations de commande à Discord. Dans votre répertoire `src/events`, ajoutez un fichier `onReady.ts`. Nous allons l'utiliser avec l'événement `"ready"`.

Créez une fonction asynchrone exportée nommée `onReady`, et donnez-lui un seul paramètre appelé `BOT`. Importez le type `Client` de discord.js et définissez le type de `BOT` sur `Client`.

```ts
import { Client } from "discord.js";

export const onReady = async (BOT: Client) => {};

```

Maintenant, importez le module `REST` de `@discordjs/rest`. Cela vous permettra d'instancier un client API, que vous utiliserez pour envoyer les commandes. Construisez une nouvelle instance avec `const rest = new REST();`. 

Il y a quelques choses que vous devrez configurer avec votre client REST. Tout d'abord, passez un objet dans le constructeur `REST()` avec une propriété `version` définie sur `"9"`. Cela indique au client d'utiliser la version 9 de l'API de Discord, qui est actuellement la dernière version. 

Ensuite, enchaînez un appel `.setToken()` sur le constructeur pour définir le token de l'API sur `process.env.BOT_TOKEN` – vous devrez forcer cela en `string`.

```ts
import { REST } from "@discordjs/rest";
import { Client } from "discord.js";

export const onReady = async (BOT: Client) => {
  const rest = new REST({ version: "9" }).setToken(
    process.env.BOT_TOKEN as string
  );
};

```

L'API attend que les données de commande soient envoyées dans un format JSON spécifique, mais heureusement, le constructeur de commandes slash que nous utilisons a une méthode juste pour cela. Importez votre `CommandList`, puis créez un nouveau tableau et mappez vos données de commande.

```ts
const commandData = CommandList.map((command) => command.data.toJSON());
```

Avant d'envoyer les commandes à Discord, il est important de noter qu'il existe deux types de commandes. Les "Commandes Globales" sont disponibles partout où votre bot est utilisé, mais prennent environ une heure à mettre à jour. Les "Commandes de Guild" sont disponibles uniquement dans un seul serveur, mais se mettent à jour immédiatement. Comme ce bot est conçu pour fonctionner dans un seul serveur, nous allons utiliser les commandes de guild.

Vous aurez besoin d'obtenir l'ID du serveur dans lequel vous utilisez le bot. Pour ce faire, assurez-vous d'avoir activé le mode développeur dans votre application Discord, puis faites un clic droit sur l'icône de votre serveur et sélectionnez "Copier l'ID". Dans votre fichier `.env`, ajoutez une variable `GUILD_ID` et attribuez-lui l'ID que vous avez copié. Cela devrait ressembler à `GUILD_ID="778130114772598785"`.

Retournez dans votre fichier `onReady.ts`, commencez votre appel API avec `await rest.put()`. Envoyer une requête `PUT` mettra à jour les commandes existantes, tandis qu'un `POST` tentera de créer de nouvelles commandes et générera une erreur si les commandes partagent un nom. Importez `Routes` de `discord-api-types/v9`, et dans l'appel `rest.put()` passez un appel `Routes.applicationGuildCommands()`. Cela sera utilisé pour construire le point de terminaison de l'API pour envoyer les commandes.

L'appel `applicationGuildCommands()` prendra deux arguments. 

Le premier est l'ID de l'application à associer aux commandes. Vous pouvez l'obtenir à partir de la valeur `BOT.user.id` – mais `user` est potentiellement indéfini, vous devrez donc l'enchaîner de manière optionnelle. Utilisez `BOT.user?.id || "missing id"` pour ajouter une valeur de repli qui générera une erreur – cela nous permettra de savoir si l'ID du bot est manquant. 

Le deuxième argument est l'ID du serveur, que vous avez configuré comme `process.env.GUILD_ID` (n'oubliez pas de forcer le type !).

L'appel `.put()` a également besoin d'un deuxième argument, qui est les données que vous souhaitez envoyer. Passez cela comme `{ body: commandData }` pour correspondre au format attendu. 

Enfin, ajoutez un `console.log("Discord ready!")` à la fin du fichier pour indiquer que votre bot est en ligne.

```ts
import { REST } from "@discordjs/rest";
import { Routes } from "discord-api-types/v9";
import { Client } from "discord.js";
import { CommandList } from "../commands/_CommandList";

export const onReady = async (BOT: Client) => {
  const rest = new REST({ version: "9" }).setToken(
    process.env.BOT_TOKEN as string
  );

  const commandData = CommandList.map((command) => command.data.toJSON());

  await rest.put(
    Routes.applicationGuildCommands(
      BOT.user?.id || "missing id",
      process.env.GUILD_ID as string
    ),
    { body: commandData }
  );

  console.log("Discord ready!");
};

```

Passez à votre fichier `index.ts` et localisez votre écouteur d'événement `"ready"`. Remplacez l'appel `console.log` par votre nouvelle fonction `onReady` – n'oubliez pas de l'importer, et rendez la fonction de rappel asynchrone.

```ts
import { Client } from "discord.js";
import { IntentOptions } from "./config/IntentOptions";
import { connectDatabase } from "./database/connectDatabase";
import { onInteraction } from "./events/onInteraction";
import { onReady } from "./events/onReady";
import { validateEnv } from "./utils/validateEnv";

(async () => {
  if (!validateEnv()) return;
  const BOT = new Client({ intents: IntentOptions });

  BOT.on("ready", async () => await onReady(BOT));

  BOT.on(
    "interactionCreate",
    async (interaction) => await onInteraction(interaction)
  );

  await connectDatabase();

  await BOT.login(process.env.BOT_TOKEN);
})();

```

Maintenant, exécutez `npm run build` et `npm start`, et rendez-vous sur votre serveur dans Discord. Si vous tapez `/`, vous devriez voir votre nouvelle commande `/100` apparaître. Essayez d'utiliser la commande et vérifiez la réponse.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-122.png)
_Si vous voyez cette réponse, alors vous avez réussi à créer votre première commande !_

Félicitations ! Vous avez votre première commande réussie. Avec toute l'infrastructure que vous avez construite, l'ajout de commandes supplémentaires sera beaucoup plus fluide. Allons-y et faisons cela maintenant.

### Commande Edit

Que se passe-t-il si un campeur fait une faute de frappe dans son message `/100` ? Parce que le bot envoie la réponse, le campeur ne peut pas l'éditer (Discord ne vous permet pas d'éditer les messages que vous n'avez pas envoyés). Vous devriez créer une commande qui permettra à un campeur de faire cela.

Créez un fichier `edit.ts` dans votre répertoire `src/commands`. Comme vous l'avez fait avec la commande `/100`, importez votre `SlashCommandBuilder` et l'interface `Command`, et exportez un objet `edit` avec le type `Command`.

Utilisez le `SlashCommandBuilder` pour préparer la propriété `data`. Donnez à la commande le nom `edit` et la description `Edit a previous 100 days of code post.`, puis ajoutez deux options de chaîne. La première option de chaîne doit avoir un nom `embed-id` et une description de `ID of the message to edit.`, et la seconde doit avoir un nom de `message` et une description de `The message to go in your 100 Days of Code update.`. Les deux options doivent être requises.

Votre code devrait ressembler à ceci :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";

export const edit: Command = {
    data: new SlashCommandBuilder()
    .setName("edit")
    .setDescription("Edit a previous 100 days of code post.")
    .addStringOption((option) =>
      option
        .setName("embed-id")
        .setDescription("ID of the message to edit.")
        .setRequired(true)
    )
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("The message to go in your 100 Days of Code update.")
        .setRequired(true)
    ),
}
```

Créez votre propriété `run` avec une fonction asynchrone et un paramètre `interaction`. Déstructurez le `channel` et le `user` de l'interaction, et récupérez les options `embed-id` et `message`. N'oubliez pas de différer la réponse !

```js
    run: async (interaction) => {
        await interaction.deferReply();
        const { channel, user } = interaction;
        const targetId = interaction.options.getString("embed-id", true);
        const text = interaction.options.getString("message", true);
    }
```

La propriété `channel` est nullable (dans les cas où une interaction est envoyée via un DM, par exemple), vous voudrez donc vérifier qu'elle existe. Si ce n'est pas le cas, répondez avec un message indiquant que la commande manque de paramètres.

```ts
    if (!channel) {
      await interaction.editReply({
        content: "Missing channel parameter.",
      });
      return;
    }
```

Maintenant que vous savez que le canal existe, vous pouvez récupérer le message que le campeur souhaite modifier en fonction de l'ID qu'il a fourni. Utilisez `channel.messages.fetch()` pour cela, en passant `targetId` comme argument.

Parce qu'il est possible que le message cible n'existe pas, vous devez en tenir compte dans votre code. Ajoutez une condition qui vérifie cela, et si le message n'est pas trouvé, répondez avec une explication.

```ts
    const targetMessage = await channel.messages.fetch(targetId);

    if (!targetMessage) {
      await interaction.editReply({
        content:
          "That does not appear to be a valid message ID. Be sure that you are using this command in the same channel as the message.",
      });
      return;
    }
```

La dernière chose que vous devez vérifier est que le message que le campeur modifie lui appartient réellement. Vous pouvez accéder à l'intégration avec la propriété `.embeds` – tout comme vous l'avez envoyée, la propriété est retournée sous forme de tableau d'objets d'intégration.

Récupérez la première intégration du tableau, puis vérifiez que l'auteur de l'intégration correspond au tag de l'utilisateur. Si ce n'est pas le cas, faites-lui savoir qu'il ne peut pas modifier ce message.

```ts
    const targetEmbed = targetMessage.embeds[0];

    if (targetEmbed.author?.name !== user.tag) {
        await interaction.editReply({
            content: "This does not appear to be your 100 Days of Code post. You cannot edit it."
        })
    }
```

Maintenant que vous avez confirmé que tout est correct, vous pouvez utiliser `.setDescription()` sur l'intégration pour mettre à jour le texte. Ensuite, modifiez le message avec la nouvelle intégration, et répondez à l'interaction avec une confirmation.

Votre code complet devrait ressembler à ceci :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { Command } from "../interfaces/Command";

export const edit: Command = {
  data: new SlashCommandBuilder()
    .setName("edit")
    .setDescription("Edit a previous 100 days of code post.")
    .addStringOption((option) =>
      option
        .setName("embed-id")
        .setDescription("ID of the message to edit.")
        .setRequired(true)
    )
    .addStringOption((option) =>
      option
        .setName("message")
        .setDescription("The message to go in your 100 Days of Code update.")
        .setRequired(true)
    ),
  run: async (interaction) => {
    await interaction.deferReply();
    const { channel, user } = interaction;
    const targetId = interaction.options.getString("embed-id", true);
    const text = interaction.options.getString("message", true);

    if (!channel) {
      await interaction.editReply({
        content: "Missing channel parameter.",
      });
      return;
    }

    const targetMessage = await channel.messages.fetch(targetId);

    if (!targetMessage) {
      await interaction.editReply({
        content:
          "That does not appear to be a valid message ID. Be sure that you are using this command in the same channel as the message.",
      });
      return;
    }

    const targetEmbed = targetMessage.embeds[0];

    if (targetEmbed.author?.name !== user.tag) {
      await interaction.editReply({
        content:
          "This does not appear to be your 100 Days of Code post. You cannot edit it.",
      });
    }

    targetEmbed.setDescription(text);
    await targetMessage.edit({ embeds: [targetEmbed] });
    await interaction.editReply({ content: "Updated!" });
  },
};

```

Ajoutez votre nouvelle commande `edit` à votre tableau `CommandList`, puis construisez et exécutez votre bot et vous devriez voir la nouvelle commande. Essayez de modifier l'intégration que vous avez envoyée précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-123.png)
_Vous devriez voir votre intégration se mettre à jour, et une confirmation du bot !_

### Commande View

Les campeurs devraient avoir un moyen de voir leur progression actuelle, nous devons donc créer une commande pour cela. À ce stade, vous devriez être à l'aise avec la structure des commandes – nous vous encourageons à suivre ces instructions mais à essayer d'écrire le code sans regarder le résultat final.

Créez un fichier `view.ts` dans votre répertoire de commandes, et configurez votre variable de commande. Créez la propriété `data` avec une commande qui a le nom `view` et la description `Shows your latest 100 days of code check in.` Cette commande n'a pas besoin d'options.

Configurez votre fonction asynchrone dans la propriété `run`, et différenciez la réponse d'interaction. Extrayez l'objet `user` de l'interaction. Utilisez votre module `getCamperData` pour récupérer les données du campeur depuis la base de données. Ensuite, vérifiez si la propriété `day` des données a une valeur non nulle. Si ce n'est pas le cas, faites savoir au campeur qu'il n'a pas commencé le défi 100 Days of Code, et qu'il peut le faire avec la commande `/100`.

Créez une intégration avec un titre défini sur `My 100DoC Progress`. Définissez la description sur `Here is my 100 Days of Code progress. I last reported an update on:` et ajoutez le timestamp du campeur. Ajoutez un champ `Round` et `Day`, et définissez l'auteur pour l'intégration. Ensuite, envoyez l'intégration dans la réponse d'interaction.

N'oubliez pas d'ajouter votre nouvelle commande à la `CommandList`, puis essayez de construire et de démarrer votre bot. Vous devriez voir la commande disponible, et pouvoir obtenir une réponse de celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-125.png)

Si vous n'avez pas obtenu la réponse, voici à quoi votre code devrait ressembler.

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { MessageEmbed } from "discord.js";
import { Command } from "../interfaces/Command";
import { getCamperData } from "../modules/getCamperData";

export const view: Command = {
  data: new SlashCommandBuilder()
    .setName("view")
    .setDescription("Shows your latest 100 Days of Code check in."),
  run: async (interaction) => {
    await interaction.deferReply();
    const { user } = interaction;
    const targetCamper = await getCamperData(user.id);

    if (!targetCamper.day) {
      await interaction.editReply({
        content:
          "It looks like you have not started the 100 Days of Code challenge yet. Use `/100` and add your message to report your first day!",
      });
      return;
    }

    const camperEmbed = new MessageEmbed();
    camperEmbed.setTitle("My 100DoC Progress");
    camperEmbed.setDescription(
      `Here is my 100 Days of Code progress. I last reported an update on ${new Date(
        targetCamper.timestamp
      ).toLocaleDateString()}.`
    );
    camperEmbed.addField("Round", targetCamper.round.toString(), true);
    camperEmbed.addField("Day", targetCamper.day.toString(), true);
    camperEmbed.setAuthor({
      name: user.tag,
      iconURL: user.displayAvatarURL(),
    });

    await interaction.editReply({ embeds: [camperEmbed] });
  },
};

```

### Commande Help

La dernière chose que vous devez construire est une commande d'aide, qui expliquera comment les campeurs peuvent interagir avec le bot. 

Créez votre fichier `help.ts` dans le répertoire des commandes, et créez votre propriété `data`. Donnez à la commande le nom `help` et la description `Provides information on using this bot.`

Configurez votre propriété `run` avec la fonction asynchrone, et n'oubliez pas de différer la réponse. Créez une intégration, et utilisez la description et les champs pour fournir les informations que vous souhaitez partager avec vos campeurs. Envoyez l'intégration dans la réponse d'interaction. 

Chargez votre nouvelle commande d'aide dans la `CommandList`, et construisez + démarrez votre bot pour la tester. Vous devriez voir une réponse avec l'intégration que vous avez créée.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-126.png)

Votre intégration peut être différente, selon les informations que vous avez choisies de partager. Voici le code que nous avons utilisé pour l'intégration ci-dessus :

```ts
import { SlashCommandBuilder } from "@discordjs/builders";
import { MessageEmbed } from "discord.js";
import { Command } from "../interfaces/Command";

export const help: Command = {
  data: new SlashCommandBuilder()
    .setName("help")
    .setDescription("Provides information on using this bot."),
  run: async (interaction) => {
    await interaction.deferReply();
    const helpEmbed = new MessageEmbed();
    helpEmbed.setTitle("100 Days of Code Bot!");
    helpEmbed.setDescription(
      "This discord bot is designed to help you track and share your 100 Days of Code progress."
    );
    helpEmbed.addField(
      "Create today's update",
      "Use the `/100` command to create your update for today. The `message` will be displayed in your embed."
    );
    helpEmbed.addField(
      "Edit today's update",
      "Do you see a typo in your embed? Right click it and copy the ID (you may need developer mode on for this), and use the `/edit` command to update that embed with a new message."
    );
    helpEmbed.addField(
      "Show your progress",
      "To see your current progress in the challenge, and the day you last checked in, use `/view`."
    );
    helpEmbed.setFooter({ text: `Version ${process.env.npm_package_version}` });
    await interaction.editReply({ embeds: [helpEmbed] });
    return;
  },
};

```

## Conclusion

Félicitations ! Vous avez réussi à créer un bot Discord pour le défi 100 Days of Code.

Si vous êtes intéressé à explorer davantage, vous pouvez consulter [le code source](https://github.com/nhcarrigan/100-days-of-code-bot) du bot en direct qui a inspiré ce tutoriel, qui inclut la journalisation personnalisée des erreurs, le rapport d'erreurs externe et un site de documentation.