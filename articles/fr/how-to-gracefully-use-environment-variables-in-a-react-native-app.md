---
title: Comment utiliser élégamment les variables d'environnement dans une application
  React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-09T09:09:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-gracefully-use-environment-variables-in-a-react-native-app
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Copy-of-Expo-and-React-Native-series.png
tags:
- name: JavaScript
  slug: javascript
- name: React Native
  slug: react-native
seo_title: Comment utiliser élégamment les variables d'environnement dans une application
  React Native
seo_desc: 'By Aman Mittal

  API Keys and secrets always contain some amount of sensitive data or a token that
  needs to be saved gracefully. Managing different keys for different environments,
  such as development or production, is a common practice among JavaScrip...'
---

Par Aman Mittal

Les clés API et les secrets contiennent toujours une certaine quantité de données sensibles ou un jeton qui doit être sauvegardé élégamment. Gérer différentes clés pour différents environnements, tels que le développement ou la production, est une pratique courante parmi les développeurs JavaScript. D'où l'existence du mécanisme du fichier `.env`.

Il existe un moyen dans les applications React Native de sauvegarder les clés API et autres informations sensibles sans intégrer de code natif. Dans ce court article, vous allez apprendre comment installer et intégrer une petite bibliothèque qui vous aide à utiliser des variables d'environnement sans exposer d'informations sensibles.

Notez que les étapes mentionnées dans cet article pour installer et intégrer `[react-native-dotenv](https://www.npmjs.com/package/react-native-dotenv)` peuvent être utilisées avec un projet Expo de manière similaire à celle décrite ci-dessous.

---

### Prérequis

Pour suivre ce tutoriel, assurez-vous d'avoir installé les éléments suivants sur votre environnement de développement local et d'avoir accès aux services mentionnés ci-dessous.

* [Nodejs](https://nodejs.org/en/) (>= 8.x.x) avec npm/yarn installé
* [react-native-cli](https://www.npmjs.com/package/react-native-cli) pour créer et exécuter une nouvelle application React Native
* `watchman` : L'observateur de changements de fichiers pour les projets React Native

### Mise en route

Pour commencer, créez un nouveau projet en utilisant `react-native-cli` dans une fenêtre de terminal.

```bash
react-native init RNEnvVariables

# naviguez à l'intérieur du répertoire du projet
cd RNEnvVariables
```

Une fois le répertoire du projet créé, naviguez dedans. Créez un nouveau fichier appelé `.env`. Ce fichier va contenir toutes les clés API ou toute information sensible. Assurez-vous d'ajouter ce fichier à `.gitignore` afin de ne pas exposer de clé secrète sur un site de contrôle de version comme Github.

Pour commencer, ajoutons une clé fictive appelée `SOME_KEY` au fichier `.env`.

```env
SOME_KEY=something
```

Notez bien que les fichiers `.env` considèrent les chaînes valides à l'intérieur de guillemets. De plus, écrire `SOME_KEY` en majuscules est juste une convention de nommage assez couramment suivie.

### Installer react-native-dotenv

Ensuite, installez la dépendance `[react-native-dotenv](https://www.npmjs.com/package/react-native-dotenv)` qui vous aidera à gérer vos variables d'environnement élégamment dans cette application. Allez dans la fenêtre de terminal et exécutez la commande suivante.

```
yarn add react-native-dotenv
```

Le module `react-native-dotenv` vous permet d'importer des variables d'environnement à partir d'un fichier `.env`. Pour le faire fonctionner, ouvrez le fichier `babel.config.js` et modifiez les `presets` comme ci-dessous.

```js
module.exports = {   
    presets: ['module:metro-react-native-babel-preset', 'module:react-native-dotenv']
}
```

### Exécuter l'application

Pour vérifier que cela fonctionne, ouvrez `App.js` et importez `SOME_KEY` depuis le package lui-même. `react-native-dotenv` analyse le fichier `.env` qui vous permet d'importer la variable d'environnement mentionnée à l'intérieur du fichier.

```js
// après les autres imports
import { SOME_KEY } from 'react-native-dotenv'
```

Si vous ouvrez cette application React Native de démonstration dans son état actuel en utilisant un simulateur iOS ou un émulateur Android, vous serez accueilli par l'écran suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZISAEh-BOnnS3fe9ELSFlA.png)

Modifiez la ligne dans le fichier `App.js` où il est écrit **Step One** avec la variable d'environnement comme montré ci-dessous.

```js
<Text style={styles.sectionTitle}>{SOME_KEY}</Text>
```

Retournez maintenant au simulateur et vous remarquerez le changement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vHCK4XMZdnDKuFT1IDdhZg.png)

## Conclusion

C'est aussi simple d'utiliser `react-native-dotenv`. Vous n'avez pas à ajouter de code natif pour intégrer chaque plateforme de système d'exploitation mobile séparément. Pour un exemple plus pragmatique, vous pouvez consulter mon récent article sur [**l'authentification Firebase dans une application React Native et Expo**](https://heartbeat.fritz.ai/how-to-build-an-email-authentication-app-with-firebase-firestore-and-react-native-a18a8ba78574). Vous remarquerez que l'on utilise le même module que nous avons discuté ci-dessus dans une application Expo.

---

Je suis disponible sur **?** [**Twitter**](https://twitter.com/amanhimself) et je gère une newsletter hebdomadaire gratuite (600+ développeurs ont rejoint) dans laquelle je partage des conseils et de nouveaux articles sur Nodejs, Reactjs, GraphQL et React Native.

 **✉️** [**Rejoignez ma newsletter hebdomadaire ici.**](https://tinyletter.com/amanhimself)