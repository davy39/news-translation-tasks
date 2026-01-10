---
title: Comment structurer votre projet et gérer les ressources statiques dans React
  Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-02T16:29:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-structure-your-project-and-manage-static-resources-in-react-native-6f4cfc947d92
coverImage: https://cdn-media-1.freecodecamp.org/images/0*i9u5ERjY-T2ZgjHX.jpg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment structurer votre projet et gérer les ressources statiques dans
  React Native
seo_desc: 'By Khoa Pham

  React and React Native are just frameworks, and they do not dictate how we should
  structure our projects. It all depends on your personal taste and the project you’re
  working on.

  In this post, we will go through how to structure a projec...'
---

Par Khoa Pham

React et React Native sont simplement des frameworks, et ils ne dictent pas comment nous devons structurer nos projets. Tout dépend de vos goûts personnels et du projet sur lequel vous travaillez.

Dans cet article, nous allons voir comment structurer un projet et comment gérer les ressources locales. Bien sûr, cela n'est pas écrit dans le marbre, et vous êtes libre d'appliquer uniquement les éléments qui vous conviennent. J'espère que vous apprendrez quelque chose.

Pour un projet initialisé avec `[react-native init](https://medium.com/fantageek/what-is-create-react-native-app-9f3bc5a6c2a3)`, nous obtenons uniquement la [structure de base](https://medium.com/fantageek/what-is-create-react-native-app-9f3bc5a6c2a3).

Il y a le dossier `ios` pour les projets Xcode, le dossier `android` pour les projets Android, et un fichier `index.js` et un fichier `App.js` pour le point de départ de React Native.

```
ios/
android/
index.js
App.js
```

En tant que quelqu'un qui a travaillé avec le natif sur Windows Phone, iOS et Android, je trouve que la structuration d'un projet revient à séparer les fichiers par **type** ou par **fonctionnalité**

### type vs fonctionnalité

Séparer par type signifie que nous organisons les fichiers par leur type. Si c'est un composant, il y a des fichiers conteneur et de présentation. Si c'est Redux, il y a des fichiers action, reducer et store. Si c'est une vue, il y a des fichiers JavaScript, HTML et CSS.

#### Grouper par type

```
redux
  actions
  store
  reducers
components
  container
  presentational
view
  javascript
  html
  css
```

De cette manière, nous pouvons voir le type de chaque fichier et exécuter facilement un script vers un certain type de fichier. Cela est général pour tous les projets, mais cela ne répond pas à la question « de quoi parle ce projet ? ». Est-ce une application d'actualités ? Est-ce une application de fidélité ? Est-ce un suivi nutritionnel ?

Organiser les fichiers par type est pour une machine, pas pour un humain. De nombreuses fois, nous travaillons sur une fonctionnalité, et trouver des fichiers à corriger dans plusieurs répertoires est fastidieux. C'est aussi une douleur si nous prévoyons de faire un framework à partir de notre projet, car les fichiers sont répartis dans de nombreux endroits.

#### Grouper par fonctionnalité

Une solution plus raisonnable est d'organiser les fichiers par fonctionnalité. Les fichiers liés à une fonctionnalité doivent être placés ensemble. Et les [fichiers de test](https://medium.com/@JeffLombardJr/organizing-tests-in-jest-17fc431ff850) doivent rester proches des fichiers sources. Consultez [cet article](https://medium.com/@JeffLombardJr/organizing-tests-in-jest-17fc431ff850) pour en savoir plus.

Une fonctionnalité peut être liée à la connexion, à l'inscription, à l'onboarding ou au profil d'un utilisateur. Une fonctionnalité peut contenir des sous-fonctionnalités tant qu'elles appartiennent au même flux. Si nous voulions déplacer la sous-fonctionnalité, ce serait facile, car tous les fichiers liés sont déjà regroupés.

Ma structure de projet typique basée sur les fonctionnalités ressemble à ceci :

```
index.js
App.js
ios/
android/
src
  screens
    login
      LoginScreen.js
      LoginNavigator.js
    onboarding
      OnboardingNavigator    
      welcome 
        WelcomeScreen.js
      term
        TermScreen.js
      notification
        NotificationScreen.js
    main
      MainNavigator.js
      news
        NewsScreen.js
      profile
        ProfileScreen.js
      search
        SearchScreen.js
  library
    package.json
    components
      ImageButton.js
      RoundImage.js
    utils
      moveToBottom.js
      safeArea.js
    networking
      API.js
      Auth.js
  res
    package.json
    strings.js
    colors.js
    palette.js
    fonts.js
    images.js
    images
      logo@2x.png
      logo@3x.png
      button@2x.png
      button@3x.png
scripts
  images.js
  clear.js
```

Outre les fichiers traditionnels `App.js` et `index.js` et les dossiers `ios` et `android`, je place tous les fichiers sources à l'intérieur du dossier `src`. À l'intérieur de `src`, j'ai `res` pour les ressources, `library` pour les fichiers communs utilisés dans plusieurs fonctionnalités, et `screens` pour un écran de contenu.

#### Le moins de dépendances possible

Puisque React Native dépend fortement de nombreuses dépendances, j'essaie d'être très conscient lorsque j'en ajoute. Dans mon projet, j'utilise simplement `react-navigation` pour la navigation. Et je ne suis pas un fan de `redux` car il ajoute une complexité inutile. N'ajoutez une dépendance que lorsque vous en avez vraiment besoin, sinon vous vous préparez plus d'ennuis que de valeur.

Ce que j'aime dans React, ce sont les composants. Un composant est l'endroit où nous définissons la vue, le style et le comportement. React a un style en ligne, c'est comme utiliser JavaScript pour définir le script, HTML et CSS. Cela correspond à l'approche par fonctionnalité que nous visons. C'est pourquoi je n'utilise pas [styled-components](https://github.com/styled-components/styled-components). Puisque les styles sont simplement des objets JavaScript, nous pouvons simplement partager les styles de commentaire dans `library`.

### src

J'aime beaucoup Android, donc je nomme `src` et `res` pour correspondre à ses conventions de dossiers.

`react-native init` configure babel pour nous. Mais pour un projet JavaScript typique, il est bon d'organiser les fichiers dans le dossier `src`. Dans mon application `electron.js` [IconGenerator](https://github.com/onmyway133/IconGenerator/tree/master/src), je place les fichiers sources à l'intérieur du dossier `src`. Cela aide non seulement en termes d'organisation, mais aide également babel à transpiler l'ensemble du dossier en une seule fois. Juste une commande et j'ai les fichiers dans `src` transpilés vers `dist` en un clin d'œil.

```bash
babel ./src --out-dir ./dist --copy-files
```

### Screen

React est basé autour des composants. Oui. Il y a des [composants conteneur et de présentation](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0), mais nous pouvons composer des composants pour construire des composants plus complexes. Ils se terminent généralement par l'affichage en plein écran. Il est appelé `Page` dans Windows Phone, `ViewController` dans iOS et `Activity` dans Android. Le guide React Native mentionne souvent [screen](https://facebook.github.io/react-native/docs/navigation) comme quelque chose qui couvre tout l'espace :

> Les applications mobiles sont rarement constituées d'un seul écran. La gestion de la présentation et de la transition entre plusieurs écrans est généralement gérée par ce que l'on appelle un navigateur.

#### index.js ou non ?

Chaque écran est considéré comme le point d'entrée pour chaque fonctionnalité. Vous pouvez renommer le `LoginScreen.js` en `index.js` en utilisant la fonctionnalité de [module](https://medium.freecodecamp.org/requiring-modules-in-node-js-everything-you-need-to-know-e7fbd119be8) de Node :

> Les modules n'ont pas à être des fichiers. Nous pouvons également créer un dossier `find-me` sous `node_modules` et placer un fichier `index.js` dedans. La même ligne `require('find-me')` utilisera le fichier `index.js` de ce dossier.

Ainsi, au lieu de `import LoginScreen from './screens/LoginScreen'`, nous pouvons simplement faire `import LoginScreen from './screens'`.

L'utilisation de `index.js` entraîne une encapsulation et fournit une interface publique pour la fonctionnalité. Cela relève du goût personnel. Je préfère moi-même un nom explicite pour un fichier, d'où le nom `LoginScreen.js`.

### Navigator

[react-navigation](https://github.com/react-navigation/react-navigation) semble être le choix le plus populaire pour gérer la navigation dans une application React Native. Pour une fonctionnalité comme l'onboarding, il y a probablement plusieurs écrans gérés par une navigation par pile, donc il y a `OnboardingNavigator`.

Vous pouvez considérer Navigator comme quelque chose qui regroupe des sous-écrans ou des fonctionnalités. Puisque nous regroupons par fonctionnalité, il est raisonnable de placer Navigator à l'intérieur du dossier de la fonctionnalité. Cela ressemble essentiellement à ceci :

```jsx
import { createStackNavigator } from 'react-navigation'
import Welcome from './Welcome'
import Term from './Term'

const routeConfig = {
  Welcome: {
    screen: Welcome
  },
  Term: {
    screen: Term
  }
}

const navigatorConfig = {
  navigationOptions: {
    header: null
  }
}

export default OnboardingNavigator = createStackNavigator(routeConfig, navigatorConfig)
```

### library

C'est la partie la plus controversée de la structuration d'un projet. Si vous n'aimez pas le nom `library`, vous pouvez l'appeler `utilities`, `common`, `citadel`, `whatever`...

Ce n'est pas destiné aux fichiers sans domicile fixe, mais c'est là que nous plaçons les utilitaires et composants communs utilisés par de nombreuses fonctionnalités. Des choses comme les composants atomiques, les wrappers, les fonctions de correction rapide, les éléments de mise en réseau et les informations de connexion sont utilisées fréquemment, et il est difficile de les déplacer vers un dossier de fonctionnalité spécifique. Parfois, nous devons simplement être pratiques et faire le travail.

Dans React Native, nous devons souvent implémenter un bouton avec une image de fond dans de nombreux écrans. Voici un exemple simple qui reste à l'intérieur de `library/components/ImageButton.js`. Le dossier `components` est destiné aux composants réutilisables, parfois appelés [composants atomiques](https://medium.com/joeydinardo/a-brief-look-at-atomic-components-39cbe71d38b5). Selon les conventions de nommage de React, la première lettre doit être en majuscule.

```jsx
import React from 'react'
import { TouchableOpacity, View, Image, Text, StyleSheet } from 'react-native'
import images from 'res/images'
import colors from 'res/colors'

export default class ImageButton extends React.Component {
  render() {
    return (
      <TouchableOpacity style={styles.touchable} onPress={this.props.onPress}>
        <View style={styles.view}>
          <Text style={styles.text}>{this.props.title}</Text>
        </View>
        <Image
          source={images.button}
          style={styles.image} />
      </TouchableOpacity>
    )
  }
}

const styles = StyleSheet.create({
  view: {
    position: 'absolute',
    backgroundColor: 'transparent'
  },
  image: {
  
},
  touchable: {
    alignItems: 'center',
    justifyContent: 'center'
  },
  text: {
    color: colors.button,
    fontSize: 18,
    textAlign: 'center'
  }
})
```

Et si nous voulons placer le bouton en bas, nous utilisons une fonction utilitaire pour éviter la duplication de code. Voici `library/utils/moveToBottom.js` :

```jsx
import React from 'react'
import { View, StyleSheet } from 'react-native'

function moveToBottom(component) {
  return (
    <View style={styles.container}>
      {component}
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-end',
    marginBottom: 36
  }
})

export default moveToBottom
```

#### Utiliser package.json pour éviter les chemins relatifs

Ensuite, quelque part dans `src/screens/onboarding/term/Term.js`, nous pouvons importer en utilisant des chemins relatifs :

```js
import moveToBottom from '../../../../library/utils/move'
import ImageButton from '../../../../library/components/ImageButton'
```

C'est un grand drapeau rouge à mes yeux. C'est sujet aux erreurs, car nous devons calculer combien de `..` nous devons utiliser. Et si nous déplaçons la fonctionnalité, tous les chemins doivent être recalculés.

Puisque `library` est destiné à être utilisé dans de nombreux endroits, il est bon de le référencer comme un chemin absolu. En JavaScript, il y a généralement 1000 bibliothèques pour un seul problème. Une recherche rapide sur Google révèle de nombreuses bibliothèques pour résoudre ce problème. Mais nous n'avons pas besoin d'une autre dépendance car cela est extrêmement facile à corriger.

La solution est de transformer `library` en un `module` afin que `node` puisse le trouver. L'ajout de `package.json` à n'importe quel dossier en fait un `module` Node. Ajoutez `package.json` à l'intérieur du dossier `library` avec ce contenu simple :

```json
{
  "name": "library",
  "version": "0.0.1"
}
```

Maintenant, dans `Term.js`, nous pouvons facilement importer des éléments de `library` car c'est maintenant un `module` :

```jsx
import React from 'react'
import { View, StyleSheet, Image, Text, Button } from 'react-native'
import strings from 'res/strings'
import palette from 'res/palette'
import images from 'res/images'
import ImageButton from 'library/components/ImageButton'
import moveToBottom from 'library/utils/moveToBottom'

export default class Term extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.heading}>{strings.onboarding.term.heading.toUpperCase()}</Text>
        {
          moveToBottom(
            <ImageButton style={styles.button} title={strings.onboarding.term.button.toUpperCase()} />
          )
        }
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center'
  },
  heading: {...palette.heading, ...{
    marginTop: 72
  }}
})
```

### res

Vous vous demandez peut-être ce que sont `res/colors`, `res/strings`, `res/images` et `res/fonts` dans les exemples ci-dessus. Eh bien, pour les projets front-end, nous avons généralement des composants et nous les stylisons en utilisant des polices, des chaînes localisées, des couleurs, des images et des styles. JavaScript est un langage très dynamique, et il est facile d'utiliser des types de chaînes partout. Nous pourrions avoir un tas de `#00B75D` `color` dans de nombreux fichiers, ou `Fira` comme `fontFamily` dans de nombreux composants `Text`. Cela est sujet aux erreurs et difficile à refactoriser.

Encapsulons l'utilisation des ressources à l'intérieur du dossier `res` avec des objets plus sûrs. Ils ressemblent aux exemples ci-dessous :

**res/colors**

```js
const colors = {
  title: '#00B75D',
  text: '#0C222B',
  button: '#036675'
}

export default colors
```

**res/strings**

```js
const strings = {
  onboarding: {
    welcome: {
      heading: 'Bienvenue',
      text1: "Ce que vous ne savez pas est ce que vous n'avez pas appris",
      text2: 'Visitez mon GitHub à https://github.com/onmyway133',
      button: 'Se connecter'
    },
    term: {
      heading: 'Termes et conditions',
      button: 'Lire'
    }
  }
}

export default strings
```

**res/fonts**

```js
const fonts = {
  title: 'Arial',
  text: 'SanFrancisco',
  code: 'Fira'
}

export default fonts
```

**res/images**

```js
const images = {
  button: require('./images/button.png'),
  logo: require('./images/logo.png'),
  placeholder: require('./images/placeholder.png')
}

export default images
```

Comme `library`, les fichiers `res` peuvent être accessibles depuis n'importe où, alors faisons-en un `module`. Ajoutez `package.json` au dossier `res` :

```
{
  "name": "res",
  "version": "0.0.1"
}
```

Ainsi, nous pouvons accéder aux fichiers de ressources comme des modules normaux :

```
import strings from 'res/strings'
import palette from 'res/palette'
import images from 'res/images'
```

#### Grouper les couleurs, images, polices avec palette

Le design de l'application doit être cohérent. Certains éléments doivent avoir le même aspect et la même sensation pour ne pas confondre l'utilisateur. Par exemple, le `Text` d'en-tête doit utiliser une couleur, une police et une taille de police. Le composant `Image` doit utiliser la même image de remplacement. Dans React Native, nous utilisons déjà le nom `styles` avec `const styles = StyleSheet.create({})`, alors utilisons le nom `palette`.

Voici ma palette simple. Elle définit les styles communs pour l'en-tête et le `Text` :

#### res/palette

```
import colors from './colors'

const palette = {
  heading: {
    color: colors.title,
    fontSize: 20,
    textAlign: 'center'
  },
  text: {
    color: colors.text,
    fontSize: 17,
    textAlign: 'center'
  }
}

export default palette
```

Et ensuite, nous pouvons les utiliser dans notre écran :

```js
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center'
  },
  heading: {...palette.heading, ...{
    marginTop: 72
  }}
})
```

Ici, nous utilisons l'[opérateur de propagation d'objet](https://github.com/tc39/proposal-object-rest-spread) pour fusionner `palette.heading` et notre objet de style personnalisé. Cela signifie que nous utilisons les styles de `palette.heading` mais spécifions également plus de propriétés.

Si nous devions reskin l'application pour plusieurs marques, nous pourrions avoir plusieurs palettes. C'est un modèle vraiment puissant.

#### Générer des images

Vous pouvez voir que dans `/src/res/images.js`, nous avons des propriétés pour chaque image dans le dossier `src/res/images` :

```
const images = {
  button: require('./images/button.png'),
  logo: require('./images/logo.png'),
  placeholder: require('./images/placeholder.png')
}

export default images
```

C'est fastidieux à faire manuellement, et nous devons mettre à jour s'il y a des changements dans la convention de nommage des images. Au lieu de cela, nous pouvons ajouter un script pour générer le fichier `images.js` en fonction des images que nous avons. Ajoutez un fichier à la racine du projet `/scripts/images.js` :

```
const fs = require('fs')

const imageFileNames = () => {
  const array = fs
    .readdirSync('src/res/images')
    .filter((file) => {
      return file.endsWith('.png')
    })
    .map((file) => {
      return file.replace('@2x.png', '').replace('@3x.png', '')
    })
    
return Array.from(new Set(array))
}

const generate = () => {
  let properties = imageFileNames()
    .map((name) => {
      return `${name}: require('./images/${name}.png')`
    })
    .join(',\n  ')
    
const string = `const images = {
  ${properties}
}

export default images
`

fs.writeFileSync('src/res/images.js', string, 'utf8')
}

generate()
```

Le point fort de Node est que nous avons accès au module `fs`, qui est très bon pour le traitement de fichiers. Ici, nous traversons simplement les images et mettons à jour `/src/res/images.js` en conséquence.

Chaque fois que nous ajoutons ou changeons des images, nous pouvons exécuter :

```bash
node scripts/images.js
```

Et nous pouvons également déclarer le script à l'intérieur de notre `package.json` principal :

```json
"scripts": {
  "start": "node node_modules/react-native/local-cli/cli.js start",
  "test": "jest",
  "lint": "eslint *.js **/*.js",
  "images": "node scripts/images.js"
}
```

Maintenant, nous pouvons simplement exécuter `npm run images` et nous obtenons un fichier de ressources `images.js` à jour.

#### Et les polices personnalisées ?

React Native dispose de certaines [polices personnalisées](https://medium.com/react-native-training/list-of-available-react-native-fonts-ed78b48bd45e) qui peuvent être suffisantes pour vos projets. Vous pouvez également utiliser des polices personnalisées.

Une chose à noter est qu'Android utilise le nom du fichier de police, mais iOS utilise le nom complet. Vous pouvez voir le nom complet dans l'application Font Book, ou en inspectant dans l'application en cours d'exécution

```js
for (NSString* family in [UIFont familyNames]) {
  NSLog(@"%@", family);
  
for (NSString* name in [UIFont fontNamesForFamilyName: family]) {
    NSLog(@"Family name:  %@", name);
  }
}
```

Pour que les polices personnalisées soient enregistrées dans iOS, nous devons déclarer `UIAppFonts` dans `Info.plist` en utilisant le nom de fichier des polices, et pour Android, les polices doivent être placées dans `app/src/main/assets/fonts`.

Il est bon de nommer le fichier de police de la même manière que le nom complet. React Native est censé charger dynamiquement les polices personnalisées, mais au cas où vous obtiendriez « Unrecognized font family », ajoutez simplement ces polices à la cible dans Xcode.

Faire cela à la main prend du temps, heureusement nous avons [rnpm](https://github.com/rnpm/rnpm) qui peut aider. Ajoutez d'abord toutes les polices à l'intérieur du dossier `res/fonts`. Ensuite, déclarez simplement `rnpm` dans `package.json` et exécutez `react-native link`. Cela devrait déclarer `UIAppFonts` dans iOS et déplacer toutes les polices dans `app/src/main/assets/fonts` pour Android.

```
"rnpm": {
  "assets": [
    "./src/res/fonts/"
  ]
}
```

L'accès aux polices par nom est sujet aux erreurs, nous pouvons créer un script similaire à ce que nous avons fait avec les images pour générer un accès plus sûr. Ajoutez `fonts.js` à notre dossier `scripts`

```
const fs = require('fs')

const fontFileNames = () => {
  const array = fs
    .readdirSync('src/res/fonts')
    .map((file) => {
      return file.replace('.ttf', '')
    })
    
return Array.from(new Set(array))
}

const generate = () => {
  const properties = fontFileNames()
    .map((name) => {
      const key = name.replace(/\s/g, '')
      return `${key}: '${name}'`
    })
    .join(',\n  ')
    
const string = `const fonts = {
  ${properties}
}

export default fonts
`

fs.writeFileSync('src/res/fonts.js', string, 'utf8')
}

generate()
```

Maintenant, vous pouvez utiliser une police personnalisée via l'espace de noms `R`.

```
import R from 'res/R'

const styles = StyleSheet.create({
  text: {
    fontFamily: R.fonts.FireCodeNormal
  }
})
```

### L'espace de noms R

Cette étape dépend des goûts personnels, mais je trouve que c'est plus organisé si nous introduisons l'espace de noms R, tout comme Android le fait pour les ressources avec la classe [R](http://App resources overview).

> Une fois que vous externalisez vos ressources d'application, vous pouvez y accéder en utilisant des identifiants de ressources qui sont générés dans la classe `R` de votre projet. Ce document vous montre comment regrouper vos ressources dans votre projet Android et fournir des ressources alternatives pour des configurations d'appareil spécifiques, puis y accéder depuis votre code d'application ou d'autres fichiers XML.

De cette manière, créons un fichier appelé `R.js` dans `src/res` :

```js
import strings from './strings'
import images from './images'
import colors from './colors'
import palette from './palette'

const R = {
  strings,
  images,
  colors,
  palette
}

export default R
```

Et accédez-y dans l'écran :

```jsx
import R from 'res/R'

render() {
  return (
    <SafeAreaView style={styles.container}>
      <Image
        style={styles.logo}
        source={R.images.logo} />
      <Image
        style={styles.image}
        source={R.images.placeholder} />
      <Text style={styles.title}>{R.strings.onboarding.welcome.title.toUpperCase()}</Text>
  )
}
```

Remplacez `strings` par `R.strings`, `colors` par `R.colors`, et `images` par `R.images`. Avec l'annotation R, il est clair que nous accédons aux ressources statiques du bundle de l'application.

Cela correspond également à la convention [Airbnb](https://github.com/airbnb/javascript#naming--PascalCase-singleton) pour les singletons, car notre R est maintenant comme une constante globale.

> [23.8](https://github.com/airbnb/javascript#naming--PascalCase-singleton) Utilisez PascalCase lorsque vous exportez un constructeur / une classe / un singleton / une bibliothèque de fonctions / un objet nu.

```js
const AirbnbStyleGuide = {
  es6: {
  },
}

export default AirbnbStyleGuide
```

### Où aller à partir de là

Dans cet article, je vous ai montré comment je pense que vous devriez structurer les dossiers et les fichiers dans un projet React Native. Nous avons également appris comment gérer les ressources et y accéder de manière plus sûre. J'espère que vous l'avez trouvé utile. Voici quelques ressources supplémentaires à explorer :

* [Organiser un projet React Native](https://medium.com/the-react-native-log/organizing-a-react-native-project-9514dfadaa0)
* [Structurer les projets et nommer les composants dans React](https://hackernoon.com/structuring-projects-and-naming-components-in-react-1261b6e18d76)
* [Utiliser index.js pour les interfaces publiques et le plaisir](https://alligator.io/react/index-js-public-interfaces/)

Puisque vous êtes ici, vous pourriez apprécier mes autres articles

* [Déployer React Native sur Bitrise, Fabric, CircleCI](https://medium.com/react-native-training/fixing-react-native-issues-and-happy-deploy-to-bitrise-fabric-circleci-44da4ab1487b)
* [Positionner un élément en bas de l'écran en utilisant Flexbox dans React Native](https://medium.com/react-native-training/position-element-at-the-bottom-of-the-screen-using-flexbox-in-react-native-a00b3790ca42)
* [Configurer ESLint et EditorConfig dans les projets React Native](https://codeburst.io/setting-up-eslint-and-editorconfig-in-react-native-projects-31b4d9ddd0f6)
* [Firebase SDK avec Firestore pour les applications React Native en 2018](https://medium.com/react-native-training/firebase-sdk-with-firestore-for-react-native-apps-in-2018-aa89a67d6934)

Si vous aimez cet article, envisagez de visiter [mes autres articles](https://github.com/onmyway133/blog/issues/165) et [mes applications](https://onmyway133.github.io/) ?