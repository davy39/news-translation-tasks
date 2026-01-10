---
title: Comment ajouter l'authentification à React Native en trois étapes avec Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-22T04:22:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-authentication-to-react-native-in-three-steps-using-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/rn-firebase-auth.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: authentication
  slug: authentication
- name: coding
  slug: coding
- name: Firebase
  slug: firebase
- name: '#firebase-cloud-functions'
  slug: firebase-cloud-functions
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: programing
  slug: programing
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment ajouter l'authentification à React Native en trois étapes avec
  Firebase
seo_desc: "By Said Hayani\nAuthentication allows us to secure our apps, or limit access\
  \ for non-user members. Authentication can also be used, for example, to limit access\
  \ to a paid service or specific service. \nThat's just one example of how authentication\
  \ can ..."
---

Par Said Hayani

L'authentification nous permet de sécuriser nos applications ou de limiter l'accès aux non-membres. L'authentification peut également être utilisée, par exemple, pour limiter l'accès à un service payant ou à un service spécifique. 

Ce n'est qu'un exemple de la manière dont l'authentification peut être intégrée dans votre application. Aujourd'hui, nous allons ajouter l'authentification à une application React Native en utilisant Firebase.


## 1 Installation de react-native-firebase

La première chose à faire est d'installer et d'initialiser Firebase dans notre application. Dans React Native, nous devons utiliser un conteneur Firebase pour React Native. Nous allons utiliser [react-native-firebase](https://github.com/invertase/react-native-firebase).

Si vous êtes sur le point de démarrer une nouvelle application React Native à partir de zéro et que vous souhaitez utiliser Firebase, vous avez de la chance - vous pouvez installer react-native-firebase pré-intégré en utilisant le CLI React Native.

```shell
//
npx @react-native-community/cli init --template=@react-native-firebase/template authenticationFirebase
//** source: https://invertase.io/oss/react-native-firebase/quick-start/new-project

```

Ensuite, installez simplement le pod pour iOS en exécutant la commande suivante dans le répertoire racine de votre application.

```shell
cd ios && pod install
```

Si vous avez des problèmes pour installer un nouveau projet avec Firebase, veuillez vous référer à la [documentation de react-native-firebase](https://invertase.io/oss/react-native-firebase/quick-start/new-project)

### Ajout de react-native-firebase à un projet existant

Installez le package `react-native-firebase` en utilisant yarn ou npm

```shell
 yarn add @react-native-firebase/app
```

ou :

```shell
 npm install @react-native-firebase/app
```

Ensuite, installez les pods pour iOS.

`shell cd ios && pod install`

### Exécution de l'application

Pour iOS, il y a deux façons de procéder : personnellement, j'utilise Xcode, car cela me donne une idée claire si quelque chose a mal tourné et si la construction a échoué.
![Xcode](build-xcode.gif)

Assurez-vous toujours que le package est en cours d'exécution - tapez `yarn start` pour démarrer l'application.

La deuxième façon d'exécuter l'application sur iOS est d'exécuter la commande react-native run-ios - et c'est tout.

## Ajout des identifiants Firebase

Cette étape nécessite de créer un nouveau projet dans la [console Firebase](https://console.firebase.google.com/).

Après avoir créé un nouveau projet sur la page du tableau de bord, sélectionnez **ajouter Firebase à l'application iOS**. Cela vous montrera les étapes pour ajouter des identifiants à iOS comme ci-dessous.

Il se compose de quelques étapes :

- Téléchargez le fichier `GoogleService-info.plist` et placez-le dans le dossier iOS de votre projet.
![add-firebase-ios](https://www.freecodecamp.org/news/content/images/2020/04/add-firebase-ios.png)

- Initialisez Firebase

![initialize-firebase](https://www.freecodecamp.org/news/content/images/2020/04/initialize-firebase.png)


## Pour Android

Android a une configuration différente pour Firebase. Dans les paramètres du projet dans la console Firebase, sélectionnez **ajouter Firebase à Android**.
![firebase-to-android](https://www.freecodecamp.org/news/content/images/2020/04/firebase-to-android.png)


Vous pouvez mettre n'importe quel nom que vous souhaitez dans le champ de nom de l'application - assurez-vous simplement qu'il respecte les exigences de Firebase. Ensuite, cliquez sur **Enregistrer**.

Après cela, vous devez télécharger le fichier `google-services.json` et le placer dans le dossier android/app.

Ensuite, l'étape suivante est d'initialiser le SDK Android.
![add-android-sdk](https://www.freecodecamp.org/news/content/images/2020/04/add-android-sdk.png)


La dernière étape consiste à appliquer le plugin Firebase dans : `android/app/build.gradle`.

```shell
apply plugin: 'com.google.gms.google-services'
```

Si vous avez des problèmes pour exécuter les étapes ci-dessus, vous pouvez toujours vous référer aux sites [Firebase docs](https://firebase.google.com/docs) ou [react-native-firebase](https://rnfirebase.io/).

Maintenant que nous avons terminé l'intégration, l'étape suivante consiste à implémenter les fonctions Firebase pour créer des utilisateurs et se connecter dans React Native.

## Ajout de SignIn, Login

Cette phase est simple : il suffit d'un peu de code React et JavaScript pour appeler les fonctions Firebase. Je vais créer une interface utilisateur simple pour Login et SignUp (ceci n'est pas nécessaire pour ce tutoriel, vous pouvez donc sauter cette étape).


![loginComponent](https://www.freecodecamp.org/news/content/images/2020/04/loginComponent.gif)

> Je mettrai le code source complet à la fin de l'article \*

Nous allons utiliser la fonction `createUserWithEmailAndPassword` pour inscrire un nouvel utilisateur. J'ai déjà implémenté toute la validation du formulaire - nous devons simplement appeler cette fonction pour créer un utilisateur.

![form-validation](https://www.freecodecamp.org/news/content/images/2020/04/form-validation.gif)

Lorsque l'utilisateur appuie sur le bouton Continuer, `__doSignUp` sera appelé et le code ressemble à ceci :

```jsx
const __doSignUp = () => {
  if (!email) {
    setError("Email requis *")
    setValid(false)
    return
  } else if (!password && password.trim() && password.length > 6) {
    setError("Mot de passe faible, minimum 5 caractères")
    setValid(false)
    return
  } else if (!__isValidEmail(email)) {
    setError("Email invalide")
    setValid(false)
    return
  }

  __doCreateUser(email, password)
}

const __doCreateUser = async (email, password) => {
  try {
    let response = await auth().createUserWithEmailAndPassword(email, password)
    if (response) {
      console.log(tag, "?", response)
    }
  } catch (e) {
    console.error(e.message)
  }
}
```

Assurez-vous d'avoir installé `@react-native-firebase/auth` pour pouvoir appeler `auth().createUserWithEmailAndPassword(email, password)`

```jsx
// import auth
import auth from "@react-native-firebase/auth"
```

La fonction qui crée un nouvel utilisateur dans Firebase ressemble à ceci :

```jsx
const __doCreateUser = async (email, password) =>{
    try {
     let response =  await auth().createUserWithEmailAndPassword(email, password);
      if(response){
        console.log(tag,"?",response)
      }
    } catch (e) {
      console.error(e.message);
    }

```

Si la fonction génère une erreur, assurez-vous d'activer la méthode email/mot de passe dans la section d'authentification de la console Firebase.
![enable-email-auth](https://www.freecodecamp.org/news/content/images/2020/04/enable-email-auth.png)


Si tout s'est bien passé et que les données saisies (email, mot de passe) sont valides, une alerte s'affichera. Si vous vérifiez la section Authentification dans la console Firebase, vous remarquerez qu'un nouvel utilisateur a été créé.
![signUpSuccess](https://www.freecodecamp.org/news/content/images/2020/04/signUpSuccess.gif)


Voici le code source de `SignInComponent`.

```jsx
const SigInComponent = () => {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [fetching, setFetching] = useState(false)
  const [error, setError] = useState("")
  const [isValid, setValid] = useState(true)
  const __doSignUp = () => {
    if (!email) {
      setError("Email requis *")
      setValid(false)
      return
    } else if (!password && password.trim() && password.length > 6) {
      setError("Mot de passe faible, minimum 5 caractères")
      setValid(false)
      return
    } else if (!__isValidEmail(email)) {
      setError("Email invalide")
      setValid(false)
      return
    }

    __doCreateUser(email, password)
  }

  const __doCreateUser = async (email, password) => {
    try {
      let response = await auth().createUserWithEmailAndPassword(
        email,
        password
      )
      if (response && response.user) {
        Alert.alert("Succès ✅", "Compte créé avec succès")
      }
    } catch (e) {
      console.error(e.message)
    }
  }

  return (
    <SafeAreaView style={styles.containerStyle}>
      <View style={{ flex: 0.2 }}>
        {!!fetching && <ActivityIndicator color={blue} />}
      </View>
      <View style={styles.headerContainerStyle}>
        <Text style={styles.headerTitleStyle}> S'inscrire </Text>
      </View>
      <View style={styles.formContainerStyle}>
        <TextInput
          label={"Email"}
          autoCapitalize={false}
          keyboardType="email-address"
          style={styles.textInputStyle}
          placeholder="Adresse mail"
          onChangeText={text => {
            setError
            setEmail(text)
          }}
          error={isValid}
        />

        <TextInput
          label={"Mot de passe"}
          secureTextEntry
          autoCapitalize={false}
          style={styles.textInputStyle}
          selectionColor={blue}
          placeholder="Mot de passe"
          error={isValid}
          onChangeText={text => setPassword(text)}
        />
      </View>
      {error ? (
        <View style={styles.errorLabelContainerStyle}>
          <Text style={styles.errorTextStyle}>{error}</Text>
        </View>
      ) : null}
      <View style={styles.signInButtonContainerStyle}>
        <TouchableHighlight
          style={styles.signInButtonStyle}
          onPress={__doSignUp}
          underlayColor={blue}
        >
          <View
            style={{
              flexDirection: "row",
              justifyContent: "space-around",
            }}
          >
            <Text style={styles.signInButtonTextStyle}>Continuer</Text>
          </View>
        </TouchableHighlight>
      </View>
    </SafeAreaView>
  )
}
```

Pour `LoginComponent`, c'est presque la même chose, la seule chose que nous devons changer est d'utiliser la méthode `signInWithEmailAndPassword` à la place.

```jsx
const __doSingIn = async (email, password) => {
  try {
    let response = await auth().signInWithEmailAndPassword(email, password)
    if (response && response.user) {
      Alert.alert("Succès ✅", "Authentification réussie")
    }
  } catch (e) {
    console.error(e.message)
  }
}
```

![loginSuccess](loginSuccess.gif

Et l'authentification a été implémentée avec succès dans notre application ??

Une dernière chose : si nous devons vérifier si l'utilisateur est déjà connecté, nous devons afficher autre chose au lieu des écrans de Login ou SignIn. Par exemple, nous pouvons afficher l'écran d'accueil.

Nous pouvons utiliser un module Firebase pour vérifier une session. Il peut être importé depuis le module auth.

```jsx
import auth, { firebase } from "@react-native-firebase/auth"
```

```jsx
 componentDidMount() {
    //  this.register("said1292@gmail.com", "123456");
    this.__isTheUserAuthenticated();
  }

  __isTheUserAuthenticated = () => {
    let user = firebase.auth().currentUser.uid;
    if (user) {
      console.log(tag,  user);
      this.setState({ authenticated: true });
    } else {
      this.setState({ authenticated: false });
    }
  };

```

Et nous pouvons changer l'interface utilisateur en fonction de l'authentification de l'utilisateur. Nous pouvons afficher les informations de l'utilisateur en utilisant simplement la même méthode.

```jsx
firebase.auth().currentUser.email // said543@gmail.com
```

Et pour se déconnecter, vous pouvez simplement appeler `await firebase.auth().signOut()`;

Je suis sûr que l'intégration de la navigation comme [react-navigation](https://reactnavigation.org/) serait géniale, mais ce n'était pas notre objectif dans cet article. N'hésitez donc pas à ajouter la navigation pour pouvoir naviguer en fonction du statut de l'utilisateur.

N'hésitez pas à consulter le code source complet ? sur [GitHub](https://github.com/hayanisaid/react-native-authentication-firebase)


_Merci pour la lecture_.

Publié à l'origine sur [saidhayani.com](https://saidhayani.com/How%20to%20Add%20authentication%20to%20React%20Native%20in%20three%20steps%20using%C2%A0Firebase/)

### [En savoir plus sur React Native](https://saidhayani.com/).



* [Twitter](https://twitter.com/SaidHYN)
* [GitHub](https://github.com/hayanisaid)
* [Instagram](https://www.instagram.com/saaed_happy/)
* [Rejoindre la liste de diffusion](http://eepurl.com/dk9OJL)