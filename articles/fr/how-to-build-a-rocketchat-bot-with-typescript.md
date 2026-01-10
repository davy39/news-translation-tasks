---
title: Comment créer un chatbot RocketChat avec TypeScript
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-01-07T23:30:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rocketchat-bot-with-typescript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fecb6ff7af2371468bb4b4c.jpg
tags:
- name: Chat
  slug: chat
- name: '#chatbots'
  slug: chatbots
- name: TypeScript
  slug: typescript
seo_title: Comment créer un chatbot RocketChat avec TypeScript
seo_desc: 'Today I will show you how to build your own Rocket.Chat bot and test it
  locally.

  This is the same process I used to build freeCodeCamp''s moderation chat bot for
  our community''s self-hosted chat server. This code is now running in production,
  and lots...'
---

Aujourd'hui, je vais vous montrer comment créer votre propre bot Rocket.Chat et le tester localement.

Il s'agit du même processus que j'ai utilisé pour créer le [bot de modération](https://github.com/freeCodeCamp/rocketchat-bot) de freeCodeCamp pour notre serveur de chat auto-hébergé. Ce code est maintenant en production, et beaucoup de gens l'utilisent.

## Comment installer un serveur Rocket.Chat

Votre première étape consiste à faire fonctionner une instance de Rocket.Chat localement – vous en aurez besoin pour tester la fonctionnalité du bot.

Vous pouvez utiliser le [fichier docker](https://github.com/freeCodeCamp/chat-config/blob/main/docker-compose.dev.yml) de freeCodeCamp, qui lancera automatiquement Rocket.Chat et MongoDB pour un environnement de développement. Cela vous fera gagner beaucoup de temps.

Vous pouvez soit cloner [ce dépôt](https://github.com/freeCodeCamp/chat-config/blob/main/docker-compose.dev.yml), soit créer manuellement votre propre fichier docker basé sur notre configuration. Ce tutoriel supposera que vous utilisez notre fichier docker existant.

> Remarque : Si vous n'avez pas docker installé, vous devrez l'installer. Le processus d'installation est différent pour chaque système d'exploitation. J'utilise personnellement Windows 10, donc j'ai installé [le client de bureau Docker](https://www.docker.com/products/docker-desktop) et j'ai dû activer la `virtualisation matérielle` dans mon BIOS.

Dans votre répertoire Rocket.Chat, créez un fichier `.env` et insérez le contenu suivant :

```.env
COMPOSE_FILE=docker-compose.dev.yml
PORT=3000
ROOT_URL=http://localhost:3000
ROCKETCHAT_VERSION=latest
```

Ouvrez ensuite votre terminal pointé sur ce même répertoire et exécutez :

```bash
docker-compose up -d
```

Vous devriez voir trois messages de succès dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-180.png)
_Image montrant la sortie de la console pour la commande `docker-compose up -d`. Trois images docker ont été créées, et chacune montre `done`._

Maintenant, si vous ouvrez votre navigateur et naviguez vers `localhost:3000`, vous devriez voir votre instance locale de Rocket.Chat. Le premier écran que vous voyez sera l'Assistant de configuration, qui vous guidera à travers la création de votre compte Admin.

La plupart des développeurs utilisent le compte Admin pour un accès de niveau racine afin de configurer leur chat. Comme il s'agit d'une instance locale, la sécurité de vos identifiants est moins importante que dans une instance en direct.

Remplissez vos informations pour créer le compte admin :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-181.png)
_Image montrant la modale d'informations Admin, avec les champs `Nom` définis sur Nicholas Carrigan, `Nom d'utilisateur` défini sur nhcarrigan, `Email de l'organisation` défini sur nick@freecodecamp.org, et `Mot de passe` qui est obfusqué. Sous les champs de saisie se trouve un bouton intitulé `Continuer`._

L'écran suivant est l'écran des informations sur l'organisation. Ces informations sont facultatives. Pour ce tutoriel, nous laisserons ces informations vides.

En cliquant sur `Continuer`, vous accéderez à la page d'informations sur le serveur. Ici, vous définissez le nom de votre serveur de chat (qui apparaîtra dans les métadonnées `title`), votre langue par défaut, le type de serveur et le paramètre 2FA.

**Assurez-vous de désactiver la configuration automatique du 2FA pour votre instance locale, sinon vous pourriez être bloqué hors de votre propre serveur.**

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-182.png)
_Image montrant la modale d'informations sur le serveur, avec les champs `Nom du site` défini sur fCC ChatBot tutorial, `Langue` définie sur Par défaut, `Type de serveur` sans sélection faite, et `Inscription automatique des nouveaux utilisateurs pour la double authentification par email` définie sur Non. Sous les champs de saisie se trouvent les boutons "Retour" et "Continuer"._

La dernière étape consiste à enregistrer facultativement votre serveur et à obtenir l'accès aux services de Rocket.Chat tels que les notifications push. Notez que ces services sont payants.

Pour les besoins de ce tutoriel, vous pouvez sélectionner l'option `Rester autonome`. Ensuite, vous pourrez décider si vous souhaitez des services payants plus tard.

Après avoir cliqué sur `Continuer`, vous verrez une modale indiquant que votre espace de travail est prêt à être utilisé. Ensuite, vous devriez voir votre nouvelle salle de chat. Le canal par défaut créé par l'Assistant de configuration est `general`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-183.png)
_Image montrant Rocket.Chat après avoir terminé l'assistant de configuration. La barre latérale de gauche montre un canal `general`, et la fenêtre principale montre un message système indiquant que "nhcarrigan a rejoint le canal"._

Si vous voyez cela, félicitations. Vous êtes à mi-chemin et avez maintenant un serveur de chat fonctionnel.

## Comment configurer un compte de bot dans Rocket.Chat

Maintenant, nous devons créer un utilisateur bot dans notre serveur de chat local pour que notre code puisse s'y connecter.

Sélectionnez les trois points en haut de la barre latérale et choisissez `Administration`. Ensuite, sélectionnez `Utilisateurs` dans la nouvelle barre latérale qui apparaît, et cliquez sur le bouton `+Nouveau` en haut à droite. Cela ouvre un panneau pour créer un nouveau compte utilisateur.

Remplissez les informations et les identifiants pour votre compte bot.

Quelques points clés à noter :

* Laissez `Exiger un changement de mot de passe` et `Définir un mot de passe aléatoire et l'envoyer par email` désactivés.
* Laissez `Envoyer un email de bienvenue` désactivé.
* Sélectionnez `bot` dans le menu déroulant `Rôles`.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-185.png)
_Image montrant l'écran des paramètres de Rocket.Chat. La barre latérale de gauche montre la liste des paramètres - `Utilisateurs` a été sélectionné. L'écran central montre une liste de comptes utilisateurs - nhcarrigan et Rocket.Cat. La barre latérale de droite montre l'interface d'ajout d'utilisateur, avec les champs `Nom` défini sur Tutorial Bot, `Nom d'utilisateur` défini sur tutorial-bot, `Email` défini sur nhcarrigan@gmail.com, `Vérifié` désactivé, `Message de statut` sans valeur, `Bio` sans valeur, `Surnom` sans valeur, `Mot de passe` qui est obfusqué, `Exiger un changement de mot de passe` qui est désactivé, `Définir un mot de passe aléatoire et l'envoyer par email` qui est désactivé, `Rôles` avec "bot" sélectionné, `Rejoindre les canaux par défaut` qui est activé, et `Envoyer un email de bienvenue` qui est désactivé._

> Rocket.cat est un compte intégré utilisé pour les notifications système (c'est-à-dire les mises à jour de Rocket.Chat).

Enregistrez les modifications, et votre compte bot devrait maintenant être créé ! Gardez une note du nom d'utilisateur et du mot de passe, car nous en aurons besoin pour le code.

## Comment coder votre chatbot Rocket.Chat

Il est maintenant temps de créer le code. Commencez avec un nouveau dossier vide pour votre projet.

### Configuration initiale du projet de chatbot Rocket.Chat

Nous commencerons par initialiser un projet `node.js`. Vous pouvez utiliser `npm init` pour générer un `package.json`, ou vous pouvez en créer un manuellement.

Dans tous les cas, vous devrez ajouter certaines valeurs spécifiques à la section `scripts` :

```json
  "scripts": {
    "prebuild": "rm -rf ./prod",
    "build": "tsc",
    "start": "node ./prod/bot.js"
  },
```

Ensuite, vous installerez vos dépendances nécessaires. Tout d'abord, installez les dépendances de développement :

```bash
npm install --save-dev typescript @types/node
```

Ensuite, installez vos dépendances principales :

```bash
npm install @rocket.chat/sdk dotenv
```

Votre prochaine étape consiste à configurer TypeScript.

Si vous avez installé TypeScript globalement, vous pourrez appeler `tsc --init` et générer automatiquement un fichier de configuration. Sinon, vous devrez créer manuellement un fichier `tsconfig.json` dans le répertoire racine de votre projet.

Dans tous les cas, voici les paramètres dont vous aurez besoin pour ce projet :

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "CommonJS",
    "rootDir": "./src",
    "outDir": "./prod",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "noImplicitAny": false,
  }
}
```

Si vous utilisez `git` pour le contrôle de version, vous devrez créer un fichier `.gitignore`. Ce fichier indique à `git` quels fichiers/dossiers ignorer. Dans ce cas, vous voulez ignorer :

* le JavaScript compilé dans `prod`
* vos modules Node
* vos secrets `.env`.

Ajoutez ces éléments à votre `.gitignore` :

```txt
/node_modules/
/prod/
.env
```

En parlant de secrets, vous devriez les configurer maintenant. Créez un fichier `.env`, et ajoutez les valeurs suivantes :

```txt
ROCKETCHAT_URL="localhost:3000"
ROCKETCHAT_USER="tutorial-bot"
ROCKETCHAT_PASSWORD="********"
ROCKETCHAT_USE_SSL=""
```

[Voir le code à ce stade](https://github.com/naomis-archive/fcc-rocketchat-tutorial/tree/9cd28ab2adea2c4ce9294c0c35682031cf343b5f).

### Comment écrire le code principal du chatbot Rocket.Chat

Il est maintenant temps d'écrire le code initial du bot. Créez un dossier `src` dans votre répertoire de projet, et à l'intérieur de ce dossier `src`, créez un fichier `bot.ts`. Votre structure de fichiers devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-9.png)
_Image montrant un arbre de fichiers. De haut en bas : Un dossier `node_modules`, qui est réduit, un dossier `src` qui contient un fichier `bot.ts`, un fichier `.env`, un fichier `.gitignore`, un fichier `.package-lock.json`, un fichier `package.json`, et un fichier `tsconfig.json`. Les fichiers montrent qu'ils sont suivis par `git`, sauf le dossier `node_modules` et le fichier `.env`._

> Le fichier `package-lock.json` est créé/mis à jour par `npm` chaque fois que vous exécutez `install`. Celui-ci doit également être validé dans votre dépôt, car il est requis pour la commande `npm ci`.

Dans votre fichier `bot.ts`, vous écriverez le code de base qui alimente votre bot. Commencez par vos imports nécessaires :

```ts
import { api, driver } from "@rocket.chat/sdk";
import dotenv from "dotenv";
```

Comme `node` ne charge pas automatiquement les variables d'environnement, vous devez appeler la méthode `config()` de `dotenv` pour importer vos valeurs `.env` dans le processus node :

```ts
dotenv.config();
```

Vous pouvez maintenant extraire ces variables de l'environnement node. Utilisez la déstructuration pour récupérer les valeurs :

```ts
const {
  ROCKETCHAT_URL,
  ROCKETCHAT_USER,
  ROCKETCHAT_PASSWORD,
  ROCKETCHAT_USE_SSL,
} = process.env;
```

À l'exception de `ROCKETCHAT_USE_SSH`, ces valeurs d'environnement sont _requises_. Si l'une d'elles est manquante, le code que vous écrivez générera une erreur, vous devez donc ajouter une étape pour vérifier que toutes ces valeurs sont présentes.

```ts
if (!ROCKETCHAT_URL || !ROCKETCHAT_USER || ROCKETCHAT_PASSWORD) {
  console.error("Variables d'environnement requises manquantes.");
  process.exit(1);
}
```

Vous pouvez maintenant utiliser le SDK Rocket.Chat pour connecter votre bot au compte que vous avez créé.

Comme les méthodes du SDK sont asynchrones, vous utiliserez une expression de fonction anonyme immédiatement invoquée (IIFE) pour activer les fonctionnalités `async/await`.

```ts
(async () => {
  // Rien ici pour l'instant
})();
```

> Ces prochaines étapes seront écrites à l'intérieur de cette fonction.

Tout d'abord, déterminez si votre bot doit utiliser SSL pour se connecter au serveur de chat. Si votre serveur de chat utilise `HTTPS://`, cela doit être défini sur `true`. Comme vous développez localement, cela est défini sur `false` car `localhost` n'a pas de protocole HTTPS.

Pour vous assurer que votre code fonctionnerait également dans un environnement de production, vous pouvez définir dynamiquement cette valeur en fonction de vos variables d'environnement :

```ts
const ssl = !!ROCKETCHAT_USE_SSL;
```

Ensuite, utilisez le `driver` du SDK pour interfacer avec votre serveur de chat. Connectez le `driver` à votre serveur :

```ts
await driver.connect({ host: ROCKETCHAT_URL, useSsl: ssl });
```

Connectez-vous en tant que compte bot :

```ts
await driver.login({
    username: ROCKETCHAT_USER,
    password: ROCKETCHAT_PASSWORD,
  });
await api.login({ username: ROCKETCHAT_USER, password: ROCKETCHAT_PASSWORD });
```

Faites rejoindre le bot à votre salle `general`, pour gérer les cas où le bot n'est pas déjà dans la salle. Dites également au bot d'écouter les messages avec la méthode `subscribeToMessages()`.

```ts
  await driver.joinRooms(["general"]);
  await driver.subscribeToMessages();
```

Enfin, faites envoyer un message au bot lorsqu'il se connecte (afin que vous puissiez confirmer le statut de la connexion).

```ts
  await driver.sendToRoom("Je suis en vie !", "general");
```

Maintenant, construisez et exécutez le code. Appelez ces scripts nécessaires dans votre terminal :

```bash
npm run build
npm run start
```

Après quelques journaux intégrés du SDK, vous devriez voir le bot envoyer son message de connexion dans votre serveur de chat.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-10.png)
_Image représentant un message Rocket.Chat. Le message a été envoyé par `tutorial-bot`, qui a le rôle `bot` à côté de son nom. Le texte du message est `Je suis en vie !`._

[Voir le code à ce stade](https://github.com/naomis-archive/fcc-rocketchat-tutorial/tree/216a9a20a4872670d838a475c0140fa1110638d3).

### Comment écrire le gestionnaire de commandes

Votre bot se connectera maintenant au serveur de chat et écoutera les messages, mais il n'a aucune fonction.

Avant de pouvoir ajouter des commandes, vous devez construire l'infrastructure pour gérer ces commandes.

Tout d'abord, dites au bot de gérer les messages. Juste après votre appel à `subscribeToMessages()`, ajoutez une ligne pour gérer la réponse aux messages :

```ts
driver.reactToMessages();
```

Vous verrez une erreur dans votre Intellisense, car la méthode `reactToMessages()` attend une fonction de rappel.

Vous pourriez écrire la fonction de rappel directement dans cette méthode, mais au lieu de cela, vous allez modulariser votre code et créer un gestionnaire exporté. Cela garde votre code plus propre et plus maintenable.

Créez un dossier appelé `commands` dans votre dossier `src`, et ajoutez deux fichiers : `CommandHandler.ts` et `CommandList.ts`. Dans le fichier `CommandList.ts`, nous allons ajouter une seule ligne pour l'instant :

```ts
export const CommandList = [];
```

Au fur et à mesure que vous construisez des commandes, vous les ajouterez à ce tableau pour pouvoir les parcourir dans notre gestionnaire.

Maintenant, vous devez écrire la logique de votre gestionnaire dans le fichier `CommandHandler.ts`.

Commencez par vos imports requis :

```ts
import { driver } from "@rocket.chat/sdk";
import { IMessage } from "@rocket.chat/sdk/dist/config/messageInterfaces";
import { CommandList } from "./CommandList";
```

Définissez la fonction de gestion des commandes :

```ts
export const CommandHandler = async (
    err: unknown,
    messages: IMessage[]
): Promise<void> => {
    // Le code ira ici.
}
```

Ajoutez une gestion des erreurs.

```ts
  if (err) {
    console.error(err);
    return;
  }
  const message = messages[0];
  if (!message.msg || !message.rid) {
    return;
  }
```

Si vous voyez une erreur dans le paramètre `err`, vous devez `return` tôt.

Le paramètre `messages` prend un tableau de messages, mais vous voulez réagir au _premier_ message, donc nous l'extrayons de ce tableau en tant que `message`.

Ensuite, pour la gestion des assertions de TypeScript, vous devez sortir tôt si certaines propriétés sont manquantes ou indéfinies. Dans ce cas, `message.msg` est le contenu texte du message, et `message.rid` est l'ID de la salle où le message a été reçu.

Pour un code plus propre et plus lisible, vous pouvez déstructurer certaines valeurs de l'objet message. Obtenez le nom de la salle à partir de la valeur `rid` - le SDK inclut une méthode pour faire exactement cela. Obtenez également le préfixe et la commande qui est appelée.

```ts
  const roomName = await driver.getRoomName(message.rid);
  const [prefix, commandName] = message.msg.split(" ");
```

Ajoutez la logique pour parcourir notre tableau de commandes. TypeScript identifiera certaines erreurs dues à des structures manquantes, mais vous pouvez les ignorer pour l'instant car vous n'avez pas encore écrit les commandes.

```ts
  if (prefix === "!fCC") {
    for (const Command of CommandList) {
      if (commandName === Command.name) {
        await Command.command(message, roomName);
        return;
      }
    }
    await driver.sendToRoom(
      `Je suis désolé, mais \`${commandName}\` n'est pas une commande valide.`,
      roomName
    );
  }
```

Ce bloc de code peut être un peu déroutant car nous n'avons pas encore établi comment fonctionnent les commandes.

Tout d'abord, le bot détermine si le message commence par le bon préfixe. Si ce n'est pas le cas, le bot ignorera le message.

Ensuite, le bot parcourt la liste des commandes, et s'il trouve une commande pour laquelle la valeur `name` correspond au nom de la commande envoyé dans le message, il exécutera cette commande.

S'il ne trouve _aucune_ commande correspondante, il enverra une réponse dans la salle indiquant que la commande n'était pas valide.

Avant de passer à une commande, retournez à l'appel `reactToMessages()` dans le fichier `bot.ts` et passez votre nouveau gestionnaire en tant que rappel :

```ts
  driver.reactToMessages(CommandHandler);
```

Vous devrez peut-être l'importer manuellement :

```ts
import { CommandHandler } from "./commands/CommandHandler";
```

[Voir le code à ce stade](https://github.com/naomis-archive/fcc-rocketchat-tutorial/tree/b3e62ec3ad4215f4081293077774b3e81f67a52c).

### Comment écrire une commande

TypeScript offre une fonctionnalité `interface` qui peut être utilisée pour définir une structure d'objet.

Dans votre dossier `src`, créez un dossier `interfaces`, et créez un fichier `CommandInt.ts`.

À l'intérieur de ce fichier, vous définirez votre type de commande. Tout d'abord, importez à nouveau le type de message.

```ts
import { IMessage } from "@rocket.chat/sdk/dist/config/messageInterfaces";
```

Maintenant, construisez l'interface exportée pour les définitions de commande.

```ts
export interface CommandInt {
    name: string;
    description: string;
    command: (message: IMessage, room: string) => Promise<void>
}
```

Félicitations ! Vous êtes maintenant prêt à créer la commande `ping`.

Dans votre dossier `src/commands`, créez un fichier `ping.ts`. Commencez par vos imports nécessaires : le driver Rocket.Chat et votre nouvelle interface de commande.

```ts
import { driver } from "@rocket.chat/sdk";
import { CommandInt } from "../interfaces/CommandInt";
```

Définissez et exportez la commande :

```ts
export const ping: CommandInt = {
    name: "ping",
    description: "Ping le bot.",
    command: async (message, room) => {
        // Le code ira ici.
    }
}
```

Faisons en sorte que le bot réponde par "Pong!" lorsque cette commande est appelée. À l'intérieur de la fonction, remplacez le commentaire par :

```ts
await driver.sendToRoom("Pong!", room);
```

Maintenant, chargez cette commande dans votre liste de commandes. Ouvrez le fichier `CommandList.ts`, où vous importerez notre nouvelle commande et l'inclurez dans le tableau.

```ts
import { ping } from "./ping";

export const CommandList = [ping];

```

Avec cela, vous devriez voir les erreurs dans le fichier `CommandHandler.ts` disparaître également, car TypeScript déduit que le tableau `CommandList` contient des types `CommandInt`.

Pour une sécurité de type supplémentaire, et pour vous assurer de ne pas ajouter accidentellement de valeurs à votre `CommandList` qui ne sont pas des objets `CommandInt` appropriés, tapez explicitement cette variable.

```
import { CommandInt } from "../interfaces/CommandInt";
import { ping } from "./ping";

export const CommandList: CommandInt[] = [ping];
```

Exécutez à nouveau vos scripts `build` et `start` pour tester cette nouvelle fonctionnalité.

Appelez votre commande `ping` dans la salle de chat. Vous devriez voir une réponse réussie :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-11.png)
_Image représentant une conversation Rocket.Chat. Le premier message a été envoyé par `nhcarrigan`, qui a le rôle `Admin` à côté de son nom. Le contenu du premier message est "!fCC ping". Le deuxième message a été envoyé par `tutorial-bot`, qui a le rôle `Bot` à côté de son nom. Le contenu du deuxième message est "Pong!"._

Appelez une commande `pong`. Vous devriez voir que le bot identifie qu'il ne s'agit pas d'une commande valide :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-12.png)
_Image représentant une conversation Rocket.Chat. Le premier message a été envoyé par `nhcarrigan`, qui a le rôle `Admin` à côté de son nom. Le contenu du premier message est "!fCC pong". Le deuxième message a été envoyé par `tutorial-bot`, qui a le rôle `Bot` à côté de son nom. Le contenu du deuxième message est "Je suis désolé, mais `pong` n'est pas une commande valide"._

[Voir notre code final](https://github.com/naomis-archive/fcc-rocketchat-tutorial/tree/df645aa39fbb9f18513128cfb5b55b804719ee78).

## Exploration supplémentaire

Félicitations ! Vous avez maintenant réussi à créer un chatbot Rocket.Chat de base.

Si vous souhaitez explorer d'autres fonctionnalités et implémentations de commandes, n'hésitez pas à parcourir [le code de notre bot en direct](https://github.com/nhcarrigan/rocketchat-bot).