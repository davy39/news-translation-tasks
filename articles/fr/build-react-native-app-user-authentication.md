---
title: Comment créer votre première application React Native sans serveur avec authentification
  utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-05T22:10:54.000Z'
originalURL: https://freecodecamp.org/news/build-react-native-app-user-authentication
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fe36a17e6787e098394250f.jpg
tags:
- name: authentication
  slug: authentication
- name: React Native
  slug: react-native
- name: serverless
  slug: serverless
seo_title: Comment créer votre première application React Native sans serveur avec
  authentification utilisateur
seo_desc: 'By Michael Bagley

  React Native has become a very important tool in the world of mobile application
  development.

  What''s not to love? It''s fast, cross-platform, hooks into native modules, and
  uses languages and patterns that are familiar to front-end d...'
---

Par Michael Bagley

React Native est devenu un outil très important dans le monde du développement d'applications mobiles.

_Qu'y a-t-il à ne pas aimer ?_ C'est rapide, multiplateforme, s'intègre aux modules **natifs** et utilise des langages et des motifs familiers aux développeurs front-end.

De plus, la technologie sans serveur a permis aux développeurs de déployer des applications de niveau entreprise **sans l'overhead d'une infrastructure serveur traditionnelle**. Elle élimine les tâches administratives liées à la gestion du backend d'une application, tout en augmentant la productivité.

Cette infrastructure plug-and-play sans souci s'associe bien avec des frameworks comme React et React Native car elle facilite grandement la mise à l'échelle des applications de production pour les individus et les petites équipes sans frais généraux.

Passons en revue comment créer une application React Native avec authentification utilisateur. Ensuite, je couvrirai comment intégrer ce processus avec une base de données sans serveur.

Pour l'instant, mon application d'exemple sera juste une _simple démonstration_ de l'authentification utilisateur avec état – mais soyez créatif et construisez ce qui vous intéresse ! Cette démonstration deviendra finalement une application mobile complète de liste de tâches collaborative sans serveur.

## Table des matières :

* Comment installer votre projet
* Workflow d'inscription / connexion
* Comment connecter le backend
* Conclusion

## Comment installer votre projet

Il existe de nombreuses façons différentes d'implémenter le sans serveur dans votre projet React, mais nous allons utiliser la bibliothèque `easybase-react` pour ce projet. Les fonctions sont avec état et sont construites pour React et React Native.

Allez dans votre projet React Native et faites `npm install easybase-react`.

Si vous ne savez pas comment créer un projet React Native, vous pouvez utiliser [create-react-native-app](https://github.com/expo/create-react-native-app) en faisant `npx create-react-native-app MyNativeApp` dans la console. Après cela, **installez la bibliothèque comme indiqué ci-dessus**.

À ce stade, vous pouvez ouvrir votre application en exécutant `npm run ios` ou `npm run android` selon la plateforme sur laquelle vous souhaitez tester. Votre point de départ ressemblera à _quelque chose_ comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen_Shot_2020-12-26_at_2.57.32_PM_1_33.png)

## Workflow d'inscription / connexion

Lors de l'établissement du workflow pour notre application, cette vue doit être affichée par défaut si un utilisateur n'est pas connecté. Pour des raisons de brièveté, le style de mon exemple sera très rudimentaire, mais soyez unique avec votre style !

Commençons par un routage de base afin que nous puissions distinguer deux vues différentes selon qu'un utilisateur est connecté ou non. **Pour l'instant, nous allons simplement faire en sorte que cela retourne automatiquement `false` jusqu'à ce que nous implémentions les hooks appropriés**.

Si un utilisateur n'est pas connecté, il est présenté avec une vue pour se connecter ou s'inscrire. Si un utilisateur est connecté, nous afficherons un message de confirmation.

```jsx
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';

export default function App() {
  return (
    <Router />
  );
}

function Router() {
  const isUserSignedIn = () => false;

  return (
    isUserSignedIn() ?
      <Text>Félicitations ! Vous êtes connecté.</Text>
      :
      <Account />
  )
}
```

Ce composant `Account` contiendra un modèle **Connexion / Inscription** qui devrait vous être familier. Dans React Native, cette vue pourrait ressembler à ceci :

```jsx
function Account() {
  const [userVal, setUserVal] = useState("");
  const [passVal, setPassVal] = useState("");

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenue sur React-flix !</Text>
      <TextInput value={userVal} onChangeText={e => setUserVal(e)} style={styles.accountInput} placeholder="Nom d'utilisateur" />
      <TextInput value={passVal} onChangeText={e => setPassVal(e)} style={styles.accountInput} placeholder="Mot de passe"/>
      <View style={{ display: "flex", flexDirection: "row", marginTop: 30 }}>
        <Button title="Se connecter" />
        <Button title="S'inscrire" />
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  accountInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    width: "75%",
    margin: 10,
    fontSize: 22,
    textAlign: "center"
  },
  title: {
    fontSize: 30,
    fontWeight: "500",
    fontStyle: "italic",
    marginBottom: 30
  }
});
```

Bien que quelque peu basique, cette vue contient tout ce qui est nécessaire pour une interface d'authentification utilisateur sécurisée et fonctionnelle. Pour référence, voici une capture d'écran de l'application à ce stade :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen_Shot_2020-12-26_at_3.47.48_PM_33.png)

## Comment connecter le backend

Maintenant, nous allons connecter notre application Native à un backend sans serveur pour gérer l'authentification des utilisateurs et l'administration des tokens.

Il existe diverses bibliothèques qui visent à implémenter des capacités sans serveur à React et React Native. Celle que nous allons utiliser s'appelle _Easybase_. Parmi d'autres choses, ce service vise à rendre React + sans serveur extrêmement intuitif.

Les développeurs peuvent tirer parti de l'interface de gestion de projet du service pour mettre à l'échelle leurs applications facilement et efficacement. Nous pourrons gérer les utilisateurs de nos projets avec cette interface. L'application web du service (captures d'écran ci-dessous) s'intègre exceptionnellement bien avec le package npm `easybase-react`.

La raison pour laquelle j'ai choisi d'utiliser ce package est double. Premièrement, le processus d'installation et de configuration est extrêmement simple avec un seul fichier de _configuration_.

Deuxièmement, il y a un overhead significatif pour implémenter un module d'authentification utilisateur, tel que le stockage des tokens de session et la mise en réseau. Le composant `EasybaseProvider` gère la plupart de cet overhead afin que nous puissions nous mettre au travail.

Connectez-vous à [Easybase](https://easybase.io/) et créez une nouvelle table. Si vous n'avez pas de compte, créez-en un rapidement (c'est gratuit). À partir de là, créez un nouveau projet comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen-Shot-2020-12-26-at-4.15.43-PM.png)

Ensuite, téléchargez votre token de projet ici (nous créerons quelques tables plus tard) :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen-Shot-2020-12-26-at-4.54.34-PM.png)

Placez le fichier `ebconfig.js` nouvellement téléchargé dans votre dossier de projet React Native à côté de App.js, comme suit :

```
├── android/
├── ios/
├── node_modules/
├── App.js
├── ebconfig.js <---
├── index.js
└── ...
```

Ensuite, nous allons importer deux choses dans `App.js` :

* `import ebconfig from "./ebconfig"`
* `import { EasybaseProvider, useEasybase } from "easybase-react"`

Ensuite, nous allons envelopper notre application dans ce composant `EasybaseProvider`, en passant le _ebconfig_ comme prop correspondant. Les modifications ressembleront à ce qui suit :

```jsx
import ebconfig from "./ebconfig";
import { EasybaseProvider, useEasybase } from "easybase-react";

// ...

export default function App() {
  return (
    <EasybaseProvider ebconfig={ebconfig}>
      <Router />
    </EasybaseProvider>
  )
}

// ...
```

À ce stade, nous pouvons accéder à une variété de capacités d'application sans serveur en utilisant le hook `useEasybase()`. Cela inclut des fonctions comme `signIn`, `signUp`, `setUserAttributes`, et ainsi de suite. Les utilisateurs créés et leurs attributs associés apparaîtront dans la section 'Users' de Easybase.io.

[La documentation pour le hook `useEasybase` est disponible ici](https://easybase.io/docs/easybase-react/interfaces/_reacttypes_.contextvalue.html). Des informations sont également disponibles sur le [dépôt Github](https://github.com/easybase/easybase-react).

Nous pouvons donc maintenant terminer notre composant `Account` en remplissant les props `onPress` de nos boutons avec la fonction correspondante fournie par le hook `useEasybase` :

```jsx
function Account() {
  const [userVal, setUserVal] = useState("");
  const [passVal, setPassVal] = useState("");

  const { signIn, signUp } = useEasybase();

  const clearInputs = () => {
    setUserVal("");
    setPassVal("");
  }

  const handleSignInPress = async () => {
    await signIn(userVal, passVal);
    clearInputs();
  }

  const handleSignUpPress = async () => {
    const res = await signUp(userVal, passVal, {
      created_at: new Date().toString
    });
    if (res.success) {
      await signIn(userVal, passVal);
    }
    clearInputs();
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenue sur React-flix !</Text>
      <TextInput value={userVal} onChangeText={e => setUserVal(e)} style={styles.accountInput} placeholder="Nom d'utilisateur" />
      <TextInput value={passVal} onChangeText={e => setPassVal(e)} style={styles.accountInput} placeholder="Mot de passe"/>
      <View style={{ display: "flex", flexDirection: "row", marginTop: 30 }}>
        <Button title="Se connecter" onPress={handleSignInPress} />
        <Button title="S'inscrire" onPress={handleSignUpPress} />
      </View>
    </View>
  )
}
```

Enfin, nous devons gérer la fonction `isUserSignedIn` utilisée dans le composant `Router`. Heureusement pour nous, le hook `useEasybase` fournit également cette **fonction du même nom**. Il suffit de l'intégrer et nous pouvons l'utiliser pour le rendu conditionnel.

```jsx
function Router() {
  const { isUserSignedIn } = useEasybase();

  return (
    isUserSignedIn() ?
      <Text>Félicitations ! Vous êtes connecté.</Text>
      :
      <Account />
  )
}
```

Ainsi, nous avons implémenté un workflow d'authentification utilisateur sécurisé dans React Native. Remarquez que si vous fermez ou rechargez l'application, votre utilisateur restera connecté comme c'est le cas avec la plupart des plateformes mobiles.

### Comment ajouter un bouton de déconnexion

Enfin, je vais ajouter un bouton de **déconnexion** pour les utilisateurs qui sont connectés. Cela nécessitera de changer l'élément de texte _Félicitations_... actuel pour les utilisateurs connectés.

Heureusement, le hook `useEasybase` propose une fonction de ce nom, nous pouvons donc modifier notre composant `Router` comme suit :

```jsx
function Router() {
  const { isUserSignedIn, signOut } = useEasybase();

  return (
    isUserSignedIn() ?
      <View style={styles.container}>
        <Text>Félicitations ! Vous êtes connecté.</Text>
        <Button title="Se déconnecter" onPress={signOut} />
      </View>
      :
      <Account />
  )
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen_Shot_2021-01-02_at_11.38.36_AM_34.png)

En cliquant sur ce nouveau bouton, vous pourrez déconnecter l'utilisateur actuel. Cela changera l'état de votre `EasybaseProvider`, et maintenant l'application redirigera vers le composant `Account` car `isUserSignedIn()` retournera **false**.

## Conclusion

En naviguant vers la section 'Users' de Easybase, vous verrez tous vos utilisateurs actuels. Pour référence, voici à quoi cela ressemble après avoir créé une série d'utilisateurs d'exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-02-at-11.44.05-AM.png)

Notez que dans ce menu, vous avez les options pour **supprimer un utilisateur** ou modifier leurs attributs correspondants. Vous pouvez également définir un attribut d'utilisateur individuellement en utilisant `setUserAttribute()`. À partir de là, les attributs peuvent être récupérés dans votre front-end avec la fonction `getUserAttributes()`.

Pour plus d'informations sur le sans serveur avec React et React Native, consultez la [page React d'Easybase](https://easybase.io/react/). Elle contient des détails intéressants sur d'autres sujets non encore abordés dans ma démonstration, mais nous y viendrons plus tard.

_Merci beaucoup d'avoir lu !_ J'espère que cette méthode d'implémentation de l'authentification utilisateur sera utile à ceux qui s'intéressent au développement logiciel avec React Native.

Dans mon prochain article, je vais aborder comment utiliser ce workflow d'authentification avec une base de données sans serveur. Cette base de données inclura des **permissions utilisateur** et des **requêtes de records individuelles**.