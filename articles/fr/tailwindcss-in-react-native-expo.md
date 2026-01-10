---
title: Comment ajouter Tailwind CSS à votre application React Native Expo
subtitle: ''
author: John Caleb
co_authors: []
series: null
date: '2024-02-27T09:22:11.000Z'
originalURL: https://freecodecamp.org/news/tailwindcss-in-react-native-expo
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/FREECODE-CAMP-DEFAULT-1-.png
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: React Native
  slug: react-native
- name: tailwind
  slug: tailwind
seo_title: Comment ajouter Tailwind CSS à votre application React Native Expo
seo_desc: "Tailwind CSS has been quite popular in the web development world due to\
  \ its utility-first approach and seamless integration. \nHowever, when developing\
  \ mobile apps with React Native, integrating Tailwind CSS may be challenging. But\
  \ guess what? Not any..."
---

Tailwind CSS a gagné en popularité dans le monde du développement web grâce à son approche utilitaire et son intégration transparente. 

Cependant, lors du développement d'applications mobiles avec React Native, l'intégration de Tailwind CSS peut être difficile. Mais devinez quoi ? Ce n'est plus le cas. Avec le développement d'outils tels que [NativeWind](https://www.nativewind.dev/), les développeurs React Native peuvent exploiter la puissance de Tailwind CSS pour concevoir facilement des interfaces mobiles magnifiques et réactives.

Dans ce tutoriel, vous apprendrez le processus d'intégration de Tailwind CSS à votre application React Native [Expo](https://expo.io/) en utilisant NativeWind. Nous allons également construire un simple écran de connexion avec NativeWind.

## Table des matières :

* [Qu'est-ce que NativeWind ?](#heading-quest-ce-que-nativewind)
* [Prérequis](#heading-prerequis)
* [Prise en main](#heading-prise-en-main) 
* [Comment créer une nouvelle application Expo](#heading-comment-creer-une-nouvelle-application-expo)
* [Comment installer NativeWind](#heading-comment-installer-nativewind)
* [Comment configurer Tailwind CSS](#heading-comment-configurer-tailwind-css)
* [Comment configurer NativeWind avec Babel](#heading-comment-configurer-nativewind-avec-babel)
* [Comment styliser avec NativeWind](#heading-comment-styliser-avec-nativewind)
* [Comment construire un simple écran de connexion](#heading-comment-construire-un-simple-ecran-de-connexion)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que NativeWind ?

NativeWind sert de pont entre Tailwind CSS et React Native Expo, permettant aux développeurs de tirer parti de l'approche utilitaire de Tailwind dans leur flux de travail de développement d'applications mobiles. 

NativeWind offre divers avantages aux développeurs, dont certains incluent :

* **Syntaxe familière** : Les développeurs familiarisés avec Tailwind CSS peuvent facilement migrer vers l'utilisation de NativeWind dans leurs projets React Native, facilitant ainsi la courbe d'apprentissage.
* **Stylisation cohérente** : NativeWind garantit une stylisation cohérente sur toutes les plateformes en offrant une seule collection de composants et de services.
* **Flexibilité** : NativeWind permet aux développeurs d'adapter et d'étendre facilement les styles pour répondre aux spécifications de conception de l'application.

Dans l'ensemble, il fournit une collection de composants et d'outils très similaires à Tailwind CSS, permettant aux développeurs de créer un code plus court et plus concis tout en préservant la flexibilité et la cohérence sur toutes les plateformes.

>Tailwind rend l'écriture de code comme si j'utilisais un outil de conception - Didier Catz

## Prérequis

* Compréhension de base de React Native Expo et Tailwind CSS.
* Node.js et npm (ou yarn) installés.
* Volonté d'apprendre :)

## Prise en main

Avant de plonger dans l'intégration de Tailwind CSS dans votre application React Native Expo, vous devrez vous assurer d'avoir les outils nécessaires configurés.

Si vous n'avez pas encore installé Expo et [expo-cli](https://www.npmjs.com/package/expo-cli) globalement, vous pouvez le faire en utilisant npm ou yarn :

```bash
npm install -g expo-cli
```

ou 

```bash
yarn global add expo-cli
```

## Comment créer une nouvelle application Expo

Avec expo-cli installé, vous pouvez maintenant créer un nouveau projet React Native Expo. 

Accédez au répertoire où vous souhaitez créer votre projet et ouvrez le terminal. Vous pouvez le faire en appuyant sur _CTRL + `_ dans Visual Studio Code. Ensuite, exécutez cette commande dans le terminal :

```bash
npx create-expo-app simpleproject
```

Cette commande crée un projet expo dans votre répertoire.

## Comment installer NativeWind

Après avoir créé votre projet expo, vous pouvez installer NativeWind et ses dépendances en exécutant les commandes suivantes dans le répertoire de votre projet :

```bash
cd simpleproject
npm i nativewind
npm i --dev tailwindcss@3.3.2
```

ou

```bash
cd simpleproject
yarn add nativewind
yarn add --dev tailwindcss@3.3.2
```

Ensuite, vous devrez créer un fichier `tailwind.config.js`. Pour ce faire, exécutez cette commande dans votre terminal :

```bash
npx tailwindcss init
```

Cela résultait en un fichier `tailwind.config.js` dans le répertoire racine de votre projet. 

## Comment configurer Tailwind CSS

Pour configurer Tailwind CSS dans votre projet, accédez à votre fichier `tailwind.config.js`, et sous `content`, entrez les chemins vers vos composants. Votre fichier `tailwind.config.js` ressemblera alors à ceci :

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./<custom directory>/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

![Une capture d'écran du fichier tailwind.conf.js après avoir ajouté le chemin vers les composants](https://www.freecodecamp.org/news/content/images/2024/02/code-1.png)
_fichier tailwind.conf.js après avoir ajouté les chemins vers les composants_

Dans l'exemple ci-dessus, vous pouvez remplacer `<custom directory>` par le nom réel de votre répertoire.

## Comment configurer NativeWind avec Babel

Vous devrez également configurer NativeWind avec Babel. Pour ce faire, incluez le plugin NativeWind dans le fichier `babel.conf.js` de votre projet :

```javascript
plugins: ["nativewind/babel"],
```

Le fichier `babel.conf.js` ressemblera à ceci après avoir ajouté le plugin NativeWind :

```js
module.exports = function (api) {
  api.cache(true);
  return {
    presets: ["babel-preset-expo"],
    plugins: ["nativewind/babel"],
  };
};
```

![fichier babel.conf.js après avoir ajouté le plugin nativewind](https://www.freecodecamp.org/news/content/images/2024/02/code2-2.png)
_fichier babel.conf.js après avoir ajouté le plugin nativewind_

En incluant le plugin NativeWind dans le fichier de configuration Babel, vous garantissez que la fonctionnalité de NativeWind est correctement incorporée dans la base de code JavaScript de votre projet.

 🎉Avec cela, NativeWind a été intégré avec succès à votre application Expo. L'étape suivante consiste à commencer à styliser l'application avec NativeWind.

## Comment styliser avec NativeWind

Pour commencer à styliser avec NativeWind, accédez au fichier `App.js` de votre projet ou au composant que vous souhaitez styliser, qui ressemblera à ceci par défaut :

```js
import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style='auto' />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});
```

![Code de base App.js](https://www.freecodecamp.org/news/content/images/2024/02/appjs-default.png)
_Code de base App.js_

Ensuite, modifiez votre composant pour éliminer toute instance d'abstraction `StyleSheet`. Dans cet exemple, nous allons modifier le code `App.js`. Après les ajustements, nous devrions avoir quelque chose comme ceci :

```js
import { StatusBar } from "expo-status-bar";
// import { StyleSheet, Text, View } from "react-native";
import { Text, View } from "react-native";

export default function App() {
  return (
    // <View style={styles.container}>
    <View className='flex-1 justify-center items-center bg-white'>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style='auto' />
    </View>
  );
}

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "#fff",
//     alignItems: "center",
//     justifyContent: "center",
//   },
// });
```

![Composant App.js après modification](https://www.freecodecamp.org/news/content/images/2024/02/newww.png)
_Composant App.js après modification_

Dans le bloc de code modifié, nous supprimons toutes les occurrences des abstractions `StyleSheet`, y compris l'instruction d'importation pour `stylesheet` et la fonction `StyleSheet.create`, et nous remplaçons `style` par `className` dans la fonction de retour `App.js`.

Cela étant clarifié, tout ce que vous avez à faire est d'écrire les classes Tailwind CSS dans votre `className` d'application pour commencer à implémenter Tailwind CSS dans votre application. Vous verrez cela dans un instant alors que nous construisons un simple écran de connexion avec NativeWind.

## Comment construire un simple écran de connexion

Maintenant, plongeons dans la construction d'un simple écran de connexion en utilisant NativeWind. Nous allons continuer avec la configuration initiale dans le fichier `App.js` et ajouter progressivement des composants pour créer l'interface utilisateur de connexion.

Tout d'abord, remplaçons le code existant dans le fichier `App.js` par le suivant :

```js
import { StatusBar } from "expo-status-bar";
import { Text, View } from "react-native";

export default function App() {
  return (
    <View className='flex-1 justify-center items-center bg-white'>
      <StatusBar style='auto' />
      <Text className='text-center mt-3 text-2xl font-light text-orange-300'>
        Login
      </Text>
      {/* Additional components goes here */}
    </View>
 );
}
```

![Code de départ pour l'interface utilisateur de l'écran de connexion](https://www.freecodecamp.org/news/content/images/2024/02/firstt.png)
_Code de départ pour l'interface utilisateur de l'écran de connexion_

Le code ci-dessus importe les composants essentiels de React Native et Expo. Nous utilisons ensuite un composant `View` pour définir la structure de notre écran de connexion, qui est stylisé avec les classes utilitaires de NativeWind. À l'intérieur de la `View`, nous avons un composant `Text` qui affiche "Login" avec un style appliqué en utilisant les classes NativeWind.

Ensuite, vous pouvez ajouter vos composants de formulaire de connexion, tels que les champs de saisie pour le nom d'utilisateur et le mot de passe, un bouton de connexion et tout autre élément nécessaire. Voici un exemple de la manière dont vous pouvez étendre l'écran de connexion :

```js
import { StatusBar } from "expo-status-bar";
import { Text, View, TouchableOpacity, TextInput } from "react-native";

export default function App() {
  return (
    <View className='flex-1 justify-center items-center bg-white'>
      <StatusBar style='auto' />
      <Text className='text-center mt-3 text-2xl font-light text-orange-300'>
        Login
      </Text>
      {/* Additional components goes here */}
      <View className='mt-5 mx-5'>
        <View>
          <Text className='text-gray-400'>EMAIL:</Text>
          <TextInput
            placeholder='Enter Email...'
            className='border border-dotted p-2 text-gray-500 border-amber-400 mt-1'
          />
        </View>
        <View className='mt-3'>
          <Text className='text-gray-400'>PASSWORD:</Text>
          <TextInput
            secureTextEntry
            placeholder='Enter Password...'
            className='border text-gray-500 border-dotted p-2 border-amber-400 mt-1'
          />
        </View>

        <TouchableOpacity className='bg-orange-300 p-3 mt-4'>
          <Text className='text-center text-base text-white'>Login</Text>
        </TouchableOpacity>

        <Text className='text-center font-normal text-gray-500 text-base mt-3'>
          OR
        </Text>
        <View className='mt-4'>
          <TouchableOpacity className='flex flex-row items-center justify-center p-2 bg-orange-300'>
            <Text className='text-white mx-2 text-sm'>Sign In With Google</Text>
          </TouchableOpacity>
        </View>
        <View className='mt-6 flex-row justify-center'>
          <Text className=''>New to FreeCodeCamp? </Text>
          <TouchableOpacity>
            <Text className='text-amber-500'>Create an Account</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}
```

![Interface utilisateur de l'écran de connexion étendue avec des composants supplémentaires](https://www.freecodecamp.org/news/content/images/2024/02/nextend-1.png)
_Interface utilisateur de l'écran de connexion étendue avec des composants supplémentaires_

Dans cette version étendue, nous avons inclus des composants `TextInput` pour les champs de saisie du nom d'utilisateur et du mot de passe, ainsi qu'un `TouchableOpacity` pour le bouton de connexion. Le style est réalisé avec les classes utilitaires de NativeWind pour offrir une apparence propre et cohérente.

De plus, une fois que vous avez terminé de créer votre écran de connexion en utilisant NativeWind dans votre projet React Native Expo, vous voudrez le tester pour vérifier si tout fonctionne correctement. Vous pouvez le faire en exécutant cette commande dans votre terminal :

```bash
expo start
```

Cette commande lancera le bundler et générera un code QR. Pour ouvrir l'application, scannez le code QR affiché dans le terminal avec la caméra de votre émulateur, ou appuyez sur "a" pour Android ou "i" pour iOS.

![Sortie du code dans un émulateur](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot_20240223-015329.png)
_Sortie du code dans un émulateur_

Si nécessaire, vous pouvez accéder [au code complet du projet](https://github.com/thejohncaleb/simpleproject) sur GitHub.

## Conclusion

L'intégration de Tailwind CSS dans un projet React Native Expo avec NativeWind présente divers avantages, notamment une efficacité accrue des développeurs, une cohérence du code et des performances. Les développeurs peuvent facilement créer des applications mobiles incroyables en exploitant la puissance de l'approche utilitaire de Tailwind CSS et les fonctionnalités natives de React Native.

NativeWind facilite l'application de Tailwind CSS à votre application React Native Expo. L'utilisation de Tailwind CSS dans votre flux de travail de développement d'applications mobiles ouvre de nouvelles possibilités pour la conception et la personnalisation de l'interface utilisateur.

N'oubliez pas, si vous avez des questions ou si vous voulez simplement dire bonjour, n'hésitez pas à me contacter sur [X(Twitter)](https://twitter.com/thejohncaleb) ou sur mon [site web](https://thejohncaleb.netlify.app/contact). :)