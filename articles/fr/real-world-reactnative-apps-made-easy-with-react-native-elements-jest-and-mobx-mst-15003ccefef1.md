---
title: Applications ReactNative réelles simplifiées avec React Native Elements, Jest
  et MobX MST
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-25T18:12:34.000Z'
originalURL: https://freecodecamp.org/news/real-world-reactnative-apps-made-easy-with-react-native-elements-jest-and-mobx-mst-15003ccefef1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q_Olvnw5k9PVenJrWCvXow.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Applications ReactNative réelles simplifiées avec React Native Elements,
  Jest et MobX MST
seo_desc: 'By Qaiser Abbas

  In this post, we’ll build a real-world mobile application in ReactNative. We’ll
  also explore some of the development practices and libraries, including the following:


  directory structure

  state management (in Mobx)

  code styling and li...'
---

Par Qaiser Abbas

Dans cet article, nous allons créer une application mobile réelle en ReactNative. Nous explorerons également certaines pratiques de développement et bibliothèques, notamment les suivantes :

* structure de répertoire
* gestion d'état (avec Mobx)
* outils de style de code et de linting ([Prettier](https://prettier.io/), [ESLint](https://eslint.org/), et [guide de style Airbnb](https://github.com/airbnb/javascript))
* navigation entre écrans avec [react-navigation](https://reactnavigation.org/)
* interface utilisateur avec [React Native Elements](https://react-native-training.github.io/react-native-elements/)
* et une partie importante, mais souvent ignorée : les tests unitaires de votre application (via [Jest](https://facebook.github.io/jest/) et [Enzyme](https://github.com/airbnb/enzyme)).

Alors, commençons !

### Gestion d'état dans React

React et ReactNative ont rendu la création d'applications monopages et d'applications mobiles amusante et facile, mais ils ne couvrent que la vue des applications. La gestion d'état et la conception de l'interface utilisateur peuvent encore être des parties douloureuses de la création de l'application.

Il existe plusieurs bibliothèques populaires de gestion d'état disponibles pour React. J'ai utilisé Redux, Mobx et RxJS. Bien que les trois soient bonnes à leur manière, j'ai préféré MobX pour sa simplicité, son élégance et sa puissante gestion d'état.

[Redux](https://redux.js.org/introduction/three-principles), basé principalement sur les concepts de programmation fonctionnelle et de fonctions pures, tente de résoudre la complexité de la gestion d'état en imposant certaines restrictions sur les mises à jour possibles. Ces restrictions sont reflétées dans trois principes de base : une seule source de vérité, un état en lecture seule et des fonctions pures. Vous pouvez en savoir plus sur [ces principes dans la documentation Redux](https://redux.js.org/introduction/three-principles).

Bien que je sois un fan de la programmation fonctionnelle, j'ai constaté que vous devez gérer beaucoup de code inutile lorsque vous travaillez avec Redux. Vous devez également écrire du code pour dispatcher des actions et transformer l'état vous-même.

Mobx, en revanche, fait ce travail pour vous, ce qui le rend plus facile à maintenir et plus amusant à utiliser. Vous avez besoin de la bonne quantité de code et de restrictions dans MobX pour obtenir une gestion d'état supérieure et une bonne expérience développeur.

Dans Redux, vous devez également passer beaucoup de temps à normaliser et dénormaliser vos données. Dans MobX, vous n'avez pas besoin de normaliser les données, et MobX suit automatiquement les relations entre l'état et les dérivations. Nous aborderons cela plus tard.

[RxJS](http://reactivex.io/rxjs) est une bibliothèque de programmation réactive pour JavaScript. Elle est différente de MobX en ce sens que RxJS vous permet de réagir à des événements tandis que dans MobX, vous observez les valeurs (ou l'état) et cela vous aide à réagir aux changements d'état.

Bien que RxJS et MobX permettent tous deux de réaliser de la programmation réactive, leurs approches sont assez différentes.

### À propos de notre application

L'application que nous allons créer est pour une librairie. Elle consistera principalement en deux vues simples : la vue des Livres et la vue des Auteurs.

L'application contiendra un tiroir de navigation avec deux options de menu, permettant à l'utilisateur de basculer entre les deux vues. La première option sera pour naviguer vers la vue des Livres, et l'autre option naviguera vers la vue des Auteurs.

La vue des Livres contiendra la liste des livres, ainsi qu'un onglet permettant à l'utilisateur de basculer entre les livres de fiction et de non-fiction. La vue des Auteurs contiendra la liste des auteurs.

Nous installerons tout sur un Mac OS. La plupart des commandes seront les mêmes lorsque vous avez Node installé, mais si vous rencontrez des problèmes, faites-le-moi savoir (ou cherchez simplement sur Google).

#### Sujets abordés

Nous aborderons différents sujets et les diverses bibliothèques nécessaires pour créer et tester une application React Native complète :

1. Nous installerons `create-react-native-app`, et l'utiliserons pour démarrer notre application de librairie
2. Configuration de Prettier, ESLint et le guide de style Airbnb pour notre projet
3. Ajout de la navigation par tiroir et par onglets avec react-navigation
4. Test de nos composants React avec Jest et Enzyme
5. Gestion de l'état de notre application avec MobX (mobx-state-tree). Cela impliquera également quelques changements d'interface utilisateur et plus de navigation. Nous trions et filtrons les livres par genre, et permettons à l'utilisateur de voir l'écran de détail du livre lorsque l'utilisateur appuie sur un livre.

Voici une démonstration de l'application Bookstore que nous allons créer :

![Image](https://cdn-media-1.freecodecamp.org/images/O6XAotXM0OShzwM92tzzGHonYKrkgto68n-c)
_Démonstration de notre application Bookstore_

#### Ce que nous ne couvrirons pas

Il y a quelques choses que nous ne couvrirons pas dans cet article, que vous pourriez vouloir considérer dans votre projet :

1. Outils pour ajouter un système de types statiques en JavaScript, comme [flow](https://flow.org/) et [TypeScript](https://www.typescriptlang.org/)
2. Bien que nous ajouterons quelques styles à notre application, nous n'entrerons pas dans les détails concernant les différentes options disponibles pour ajouter des styles dans une application ReactNative. La bibliothèque [styled-components](https://github.com/styled-components/styled-components) est l'une des plus populaires pour les applications React et ReactNative.
3. Nous ne construirons pas de backend séparé pour notre application. Nous passerons par l'intégration avec l'API Google Books, mais nous utiliserons des données simulées pour la plupart.

### Créer une application React Native avec create-react-native-app CLI (CRNA)

[Create React Native App](https://github.com/react-community/create-react-native-app) est un outil créé par [Facebook](https://code.facebook.com/) et l'équipe [Expo](https://expo.io/) qui facilite grandement le démarrage d'un projet React Native. Nous initialiserons notre application ReactNative en utilisant [CRNA](https://github.com/react-community/create-react-native-app) CLI. Alors, commençons !

En supposant que vous avez déjà installé [Node](https://nodejs.org/en/download/), nous devons installer `create-react-native-app` globalement, afin de pouvoir initialiser un nouveau projet React Native pour notre librairie.

```
npm install -g create-react-native-app
```

Maintenant, nous pouvons utiliser la CLI create-react-native-app pour créer notre nouveau projet React Native. Nommons-le `bookstore-app` :

```
create-react-native-app bookstore-app
```

Une fois que CRNA a terminé l'initialisation de notre application React Native, il affichera quelques commandes utiles. Changeons le répertoire vers la nouvelle application CRNA créée, et démarrons-la.

```
cd bookstore-app npm start
```

Cela démarrera le packager, donnant l'option de lancer le simulateur iOS ou Android, ou d'ouvrir l'application sur un appareil réel.

Si vous rencontrez des problèmes, veuillez vous référer soit au [guide de démarrage de React Native](https://facebook.github.io/react-native/docs/getting-started.html), soit au [guide Create React Native app (CRNA)](https://github.com/react-community/create-react-native-app/blob/master/react-native-scripts/template/README.md).

#### Ouvrir l'application CRNA sur un appareil réel via Expo

Lorsque l'application est démarrée via `npm start`, un code QR sera affiché dans votre terminal. La manière la plus simple de visualiser notre application initialisée est d'utiliser l'application Expo. Pour cela :

1. Installez l'application cliente [Expo](https://expo.io/) sur votre appareil iOS ou Android.
2. Assurez-vous d'être connecté au même réseau sans fil que votre ordinateur.
3. Utilisez l'application Expo pour scanner le code QR de votre terminal afin d'ouvrir votre projet.

#### Ouvrir l'application CRNA dans un simulateur

Pour exécuter l'application sur le simulateur iOS, vous devrez installer Xcode. Pour exécuter l'application sur un appareil virtuel Android, vous devez configurer l'environnement de développement Android. Consultez le guide de démarrage de react-native pour les deux configurations.

### Configuration de Prettier, ESLint et un guide de style Airbnb

Dans cette section, nous allons configurer Prettier, ESLint et le guide de style Airbnb pour nous assurer que notre code est non seulement joli, mais aussi vérifié par un linter.

#### Pourquoi utiliser un outil de linting ?

JavaScript est un langage dynamique et n'a pas de système de types statiques comme les langages tels que C++ et Java. En raison de cette nature dynamique, JavaScript manque du type d'outils disponibles pour l'analyse statique que de nombreux autres langages offrent.

Cela entraîne des bugs difficiles à trouver liés aux types de données, et nécessite plus d'efforts pour déboguer et résoudre ces problèmes, surtout pour les développeurs JavaScript inexpérimentés.

Puisqu'il ne s'agit pas d'un langage compilé, les erreurs sont découvertes lorsque le code JavaScript est exécuté au moment de l'exécution. Il existe des outils comme TypeScript et flow qui aident à attraper ces types d'erreurs en ajoutant un système de types statiques à JavaScript, mais nous n'aborderons aucun de ces outils dans ce tutoriel.

D'autre part, il existe des outils de linting comme ESLint disponibles qui effectuent une analyse statique du code JavaScript basée sur des règles configurables. Ils mettent en évidence les problèmes dans le code qui peuvent être des bugs potentiels, ce qui aide les développeurs à découvrir les problèmes dans leur code avant qu'il ne soit exécuté.

#### Installer et configurer ESLint

Un bon outil de linting est extrêmement important pour garantir que la qualité est intégrée dès le début et que les erreurs sont trouvées tôt. ESLint vous aide également à mettre en œuvre des directives de style.

Pour nous assurer que nous écrivons du code de haute qualité et que nous avons les bons outils dès le début de notre projet Bookstore, nous commencerons notre tutoriel par la mise en œuvre d'outils de linting. Vous pouvez en savoir plus sur [ESLint sur leur site web](https://eslint.org/docs/about/).

ESLint est entièrement configurable et personnalisable. Vous pouvez définir vos règles selon vos préférences. Cependant, différentes configurations de règles de linting ont été fournies par la communauté. L'une des plus populaires est le guide de style Airbnb, et c'est celle que nous utiliserons. Cela inclura les règles ESLint d'Airbnb, y compris ECMAScript 6+ et React.

Tout d'abord, nous installerons ESLint en exécutant cette commande dans le terminal :

Nous utiliserons [eslint-config-airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb) d'Airbnb, qui contient les règles ESLint d'Airbnb, y compris ECMAScript 6+ et React. Il nécessite des versions spécifiques d'ESLint, eslint-plugin-import, eslint-plugin-react et eslint-plugin-jsx-a11y. Pour lister les dépendances et les versions, exécutez cette commande :

```
npm info "eslint-config-airbnb@latest" peerDependencies
```

Au moment de la rédaction de cet article, voici les versions affichées dans la sortie de la commande ci-dessus :

```
{ eslint: '^4.9.0',  'eslint-plugin-import': '^2.7.0',  'eslint-plugin-jsx-a11y': '^6.0.2',  'eslint-plugin-react': '^7.4.0' }
```

Alors, installons ces versions spécifiques de dépendances en exécutant cette commande :

```
npm install -D eslint@^4.9.0 eslint-plugin-import@^2.7.0 eslint-plugin-jsx-a11y@^6.0.2 eslint-plugin-react@^7.4.0
```

Cela installera les dépendances nécessaires et générera le fichier `.eslintrc.js` dans le répertoire racine du projet. Le fichier .eslintrc.js doit avoir les configurations suivantes :

```
module.exports = {  "extends": "airbnb"};
```

#### Style de code

Bien que nous ayons couvert le linting avec ESLint et le guide de style Airbnb, une grande partie de la qualité du code est le style de code cohérent. Lorsque vous travaillez en équipe, vous voulez vous assurer que le formatage et l'indentation du code sont cohérents dans toute l'équipe. Prettier est juste l'outil pour cela. Il garantit que tout le code respecte un style cohérent.

Nous ajouterons également le [plugin ESLint pour Prettier](https://github.com/prettier/eslint-plugin-prettier), qui ajoutera Prettier en tant que règle ESLint et signalera les différences en tant que problèmes ESLint individuels.

Il peut y avoir des conflits entre les règles ESLint et le formatage du code effectué par Prettier. Heureusement, il existe un plugin disponible appelé [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) qui désactive toutes les règles qui sont inutiles ou peuvent entrer en conflit avec Prettier.

#### Installer et configurer Prettier avec ESLint

Installons tous les packages nécessaires, Prettier et eslint-plugin-prettier. Nous devrons également installer eslint-config-airbnb pour cela :

```
npm install -D prettier prettier-eslint eslint-plugin-prettier eslint-config-prettier eslint-config-airbnb
```

**NOTE :** Si ESLint est installé globalement, assurez-vous que eslint-plugin-prettier est également installé globalement. Un ESLint installé globalement ne peut pas trouver un plugin installé localement.

Pour activer le plugin eslint-plugin-prettier, mettez à jour votre fichier .eslintrc.js pour ajouter le plugin "prettier". Et pour afficher l'erreur de linting sur les règles de formatage de Prettier, ajoutez la "règle" pour afficher l'erreur sur "prettier/prettier". Voici notre .eslintrc.js mis à jour :

```
module.exports = {  "extends": [    "airbnb",    "prettier"  ],  rules: {    "prettier/prettier": "error",  },}
```

[eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) est également livré avec un outil CLI pour vous aider à vérifier si votre configuration contient des règles qui sont inutiles ou en conflit avec Prettier. Soyons proactifs et faisons cela.

Tout d'abord, ajoutez un script pour cela dans package.json :

```
{  "scripts": {    "eslint-check": "eslint --print-config .eslintrc.js | eslint-config-prettier-check"  }}
```

Maintenant, exécutez la commande "eslint-check" pour voir les règles conflictuelles d'ESLint et Prettier :

```
npm run eslint-check
```

Cela listera les règles conflictuelles dans le terminal. Désactivons les règles conflictuelles en mettant à jour le fichier .eslintrc.js. Je préfère également singleQuote et trailingComma, donc je configurerai également ces règles. Voici à quoi ressemble notre fichier .eslintrc.js maintenant :

```
module.exports = {  "parser": "babel-eslint",  "extends": [    "airbnb",    "prettier"  ],  "plugins": [    "prettier"  ],  "rules": {    "prettier/prettier": "error",    "react/jsx-closing-bracket-location": "off",    "react/jsx-closing-tag-location": "off",    "react/jsx-curly-spacing": "off",    "react/jsx-equals-spacing": "off",    "react/jsx-first-prop-new-line": "off",    "react/jsx-indent": "off",    "react/jsx-indent-props": "off",    "react/jsx-max-props-per-line": "off",    "react/jsx-tag-spacing": "off",    "react/jsx-wrap-multilines": "off"  }}
```

Si vous exécutez maintenant `eslint` avec le flag `--fix`, le code sera automatiquement formaté selon les styles Prettier.

#### Configurer VS Code pour exécuter ESLint à l'enregistrement

Nous pouvons configurer n'importe quel IDE pour exécuter automatiquement ESLint à l'enregistrement ou pendant que nous tapons. Puisque nous avons également configuré Prettier avec ESLint, notre code sera automatiquement pretiffié. VS Code est un IDE populaire dans la communauté JavaScript, donc je vais montrer comment configurer l'auto-fix d'ESLint à l'enregistrement en utilisant VS Code, mais les étapes seraient similaires dans n'importe quel IDE.

Pour configurer VS Code pour exécuter automatiquement ESLint à l'enregistrement, nous devons d'abord installer l'extension ESLint. Allez dans Extensions, recherchez l'extension "ESLint", et installez-la. Une fois l'extension ESLint installée, allez dans `Préférences > Paramètres utilisateur`, et définissez "eslint.autoFixOnSave" sur true. Assurez-vous également que "files.autoSave" est défini sur "off", "onFocusChange" ou "onWindowChange".

Maintenant, ouvrez le fichier App.js. Si ESLint est configuré correctement, vous devriez voir quelques erreurs de linting, comme "react/prefer-stateless-function", "react/jsx-filename-extension", et "no-use-before-define". Désactivons celles-ci dans le fichier .eslintrc.js. Je préfère également singleQuote et trailingComma comme je l'ai mentionné ci-dessus, donc je configurerai également ces règles.

Voici le fichier .eslintrc.js mis à jour.

```
module.exports = {  "parser": "babel-eslint",  "extends": [    "airbnb",    "prettier"  ],  "plugins": [    "prettier"  ],  "rules": {    "prettier/prettier": [      "error",      {        "singleQuote": true,        "trailingComma": "all",      }    ],    "react/prefer-stateless-function": "off",    "react/jsx-filename-extension": "off",    "no-use-before-define": "off",    "react/jsx-closing-bracket-location": "off",    "react/jsx-curly-spacing": "off",    "react/jsx-equals-spacing": "off",    "react/jsx-first-prop-new-line": "off",    "react/jsx-indent": "off",    "react/jsx-indent-props": "off",    "react/jsx-max-props-per-line": "off",    "react/jsx-tag-spacing": "off",    "react/jsx-wrap-multilines": "off"  }}
```

Je sais que c'était beaucoup de travail, considérant que nous n'avons même pas encore commencé à travailler sur notre application ! Mais faites-moi confiance, cette configuration sera très bénéfique pour vos projets à long terme, même si vous êtes une équipe d'une seule personne. Lorsque vous travaillez avec d'autres développeurs, le linting et les normes de programmation iront loin dans la réduction des défauts de code et l'assurance de la cohérence du style de code.

Vous pouvez trouver les changements apportés dans cette section dans [cette branche](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/tree/1-prettier-eslint-airbnb-styleguide-setup) du dépôt du tutoriel.

### Navigation par tiroir et onglets avec react-navigation

Dans cette section, nous ajouterons la navigation par tiroir et par onglets avec react-navigation.

Notre application Bookstore contiendra un tiroir de navigation avec deux options de menu. Le premier élément de menu pour l'**AuthorsScreen**, contenant la liste des auteurs. Le deuxième élément de menu pour le **BooksScreen**, contenant la liste des livres.

En appuyant sur un livre, l'utilisateur sera dirigé vers l'écran BookDetail. Pour la navigation entre les différentes vues, nous utiliserons [React Navigation](https://reactnavigation.org/docs/en/hello-react-navigation.html) pour ajouter la navigation à notre application. Alors, installons-le d'abord :

```
npm install --save react-navigation
```

#### createStackNavigator

Notre application ReactNative contiendra deux modules :

* un module Auteur permettant aux utilisateurs de parcourir la liste des auteurs
* un module Livres, contenant la liste des livres.

Les modules Auteur et Livre seront implémentés en utilisant le StackNavigator de [React Navigation](https://reactnavigation.org/). Pensez à StackNavigator comme à la pile d'historique dans un navigateur web. Lorsque l'utilisateur clique sur un lien, l'URL est poussée dans la pile d'historique du navigateur, et retirée du haut de la pile d'historique lorsque l'utilisateur appuie sur le bouton retour.

```
export const BookStack = createStackNavigator({  Books: {    screen: BooksScreen,  },})
```

```
export const AuthorStack = createStackNavigator({  Authors: {    screen: AuthorsScreen,  },})
```

Pour BooksScreen et AuthorsScreen, nous ajouterons simplement deux composants sans état [react](https://reactjs.org/docs/components-and-props.html) pour l'instant, avec quelques boutons pour tester notre navigation entre écrans et la fonctionnalité du tiroir :

```
const BooksScreen = ({ navigation }) => (  <View>    <Button      onPress={() => navigation.navigate('Authors')}      title="Aller aux Auteurs"    />    <Button onPress={() => navigation.openDrawer()} title="Ouvrir le tiroir" />  </View>)
```

```
const AuthorsScreen = ({ navigation }) => (  <Button    onPress={() => navigation.navigate('Books')}    title="Retour aux Livres"  />)
```

`navigation.openDrawer()` déclenchera l'ouverture du tiroir. `navigation.navigate()` permet à l'application de naviguer vers différents écrans.

Dans notre application, nous ajouterons un tiroir qui maintiendra le menu pour nos modules Auteur et Livre. Nous implémenterons le tiroir en utilisant [createDrawerNavigator](https://reactnavigation.org/docs/en/drawer-based-navigation.html) de React Navigation.

Le premier menu dans le tiroir sera pour le module Auteur, et le second pour le module Livre. Les navigateurs de pile Auteur et Livre seront tous deux à l'intérieur du DrawerStack principal.

Voici le code pour l'implémentation du tiroir :

```
const App = createDrawerNavigator({  Books: {    screen: BookStack,  },  Authors: {    screen: AuthorStack,  },})
```

Voici un [diff de nos derniers changements](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/tree/1-prettier-eslint-airbnb-styleguide-setup).

Dans le fichier App.js, nous avons apporté les modifications suivantes :

1. Nous avons renommé l'export par défaut en App
2. Nous avons ajouté deux composants sans état pour nos écrans, BooksScreen et AuthorsScreen.
3. Nous avons ajouté le StackNavigator de [React Navigation](https://reactnavigation.org/) pour implémenter la navigation pour notre application.
4. Nous avons utilisé [createDrawerNavigator()](https://reactnavigation.org/docs/en/drawer-based-navigation.html) de react-navigation pour implémenter la navigation par tiroir. Cela rend le contenu du tiroir, ainsi que les options de menu pour les livres et les auteurs.

Et après avoir apporté les modifications ci-dessus, voici à quoi ressemble notre interface utilisateur lorsque nous cliquons sur le bouton "Ouvrir le tiroir" et naviguons entre les écrans.

![Image](https://cdn-media-1.freecodecamp.org/images/Sr1hvC3EvNusiCwezGk-WvtgzzdsE2tsxtym)

#### Structure du répertoire

Il est important de réfléchir à votre application et à la manière dont vous structurerez vos fichiers et ressources au début du projet. Bien qu'il existe plusieurs façons de structurer votre code d'application, je préfère co-localiser les fichiers et les tests en utilisant une architecture basée sur les fonctionnalités. La co-localisation des fichiers liés à une fonctionnalité ou un module particulier présente un certain nombre d'avantages.

Créons un répertoire src où nous garderons tous nos fichiers sources. À l'intérieur, créons deux répertoires : un pour la vue des livres, nommé "book", et l'autre pour la vue des auteurs, nommé "author".

Créons des fichiers index.js dans chacun des deux répertoires que nous venons d'ajouter. Ces fichiers exporteront les composants pour chacune de nos vues. Déplaçons le code de App.js pour les composants BookView et AuthorView dans ces fichiers, et importons-les à la place.

Il est important de noter que le refactoring devrait faire partie intégrante du flux de travail de développement. Nous devrions refactoriser en continu notre code pour nous préparer aux changements et défis futurs. Cela a un grand impact sur la productivité et la gestion des changements à long terme.

Notre application devrait toujours fonctionner comme avant le refactoring. Voici le [diff des fichiers de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/d0377da1c3797e2dd9a35237533ae5815af1b582).

Chacun des écrans aura un titre, ce qui signifie que nous allons dupliquer le même code ainsi que les styles. Pour garder notre code DRY, déplaçons le titre dans un fichier séparé `src/components/Title.js`, et réutilisons-le où nécessaire. Nous déplacerons également les vues principales dans un nouveau répertoire parent `src/views` pour les garder séparées des autres composants.

#### Navigation par onglets

L'exigence commerciale pour notre application est d'avoir trois onglets dans la vue des livres, pour montrer tous les livres par défaut, et des onglets supplémentaires pour montrer les livres filtrés pour les livres de fiction et de non-fiction. Utilisons le [createBottomTabNavigator](https://reactnavigation.org/docs/en/tab-based-navigation.html) de react-navigation pour implémenter la navigation par onglets.

```
import { createBottomTabNavigator } from 'react-navigation'
```

```
import { AllBooksTab, FictionBooksTab, NonfictionBooksTab } from ' components/book-type-tabs'
```

```
export default createBottomTabNavigator({  'All Books': AllBooksTab,  Fiction: FictionBooksTab,  Nonfiction: NonfictionBooksTab,})
```

Nous devrions également ajouter un titre sur chaque écran pour identifier l'écran actuellement sélectionné. Créons un répertoire séparé `src/components` pour tous les composants communs, et créons un fichier pour notre composant `Title` à l'intérieur de ce nouveau répertoire.

```
// src/components/Title.jsimport React from 'react'import { StyleSheet, Text } from 'react-native'
```

```
const styles = StyleSheet.create({  header: {    textAlign: 'center',    padding: 20,    marginTop: 20,    fontSize: 20,    color: '#fff',    backgroundColor: '#434343',  },})
```

```
export default ({ text }) => <Text style={styles.header}>{text}</Text>
```

Notez que nous avons également ajouté `style` au composant `<Text>`, en important `StyleSheet` et `Text` de react-native.

Nous ajouterons le `Title` à chaque composant de vue, en fournissant le texte `title` dans les props. De plus, puisque la vue des auteurs contient simplement une liste d'auteurs, nous n'avons pas besoin d'un StackNavigator pour celle-ci, donc nous la changerons en un composant React simple. Voici à quoi ressemble notre fichier `src/views/author/index.js` maintenant :

```
// src/views/author/index.js
```

```
import Title from '../../components/Title'
```

```
export default ({ navigation }) => (  <View>    <Title text="Liste des auteurs" />    <Button onPress={() => navigation.openDrawer()} title="Ouvrir le tiroir" />    <Button onPress={() => navigation.navigate('Books')} title="Aller aux livres" />  </View>)
```

Maintenant, lorsque nous ouvrons le menu Livres à partir du tiroir, nous pouvons changer d'onglets en cliquant sur les onglets en bas.

Avec ces changements, nous avons terminé toutes les navigations de notre application. Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/007ec23b049f45bf38279c39e22f32db894f16a7).

### React Native Elements

Il existe plusieurs bibliothèques de composants d'interface utilisateur pour ajouter des composants React Native avec style. Certaines des plus populaires sont [React Native Elements](https://react-native-training.github.io/react-native-elements/), NativeBase et [Ignite](https://infinite.red/ignite). Nous utiliserons React Native Elements pour notre application Bookstore. Alors, installons d'abord react-native-elements :

```
npm install --save react-native-elements
```

#### Créer notre liste d'auteurs avec react-native-elements

Utilisons le composant **ListItem** de React Native Elements pour ajouter une liste d'auteurs dans notre écran d'auteurs.

Pour la liste des auteurs, nous utiliserons les données et le code de la [démonstration ListItem](https://react-native-training.github.io/react-native-elements/docs/listitem.html). Nous revisiterons **ListItem** plus en détail lorsque nous implémenterons l'écran de la liste des livres.

Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/11435b4c79ba718f4f8d4d12fe0b28ef707e4d1c).

### Tester les composants ReactNative avec Jest et Enzyme

Dans cette section, nous ajouterons quelques tests unitaires en utilisant Jest et Enzyme.

#### Configuration de Jest et Enzyme

Avoir des tests unitaires pour votre code est vraiment important afin que vous puissiez avoir confiance en votre code lorsque vous souhaitez changer quelque chose. Cela en vaut vraiment la peine lorsque vous ajoutez plus de fonctionnalités, et vous pouvez apporter des modifications sans la crainte de casser certaines fonctionnalités existantes de votre application à la suite du changement. Vous savez que vos tests unitaires fournissent le filet de sécurité pour votre application contre les défauts qui pourraient se glisser dans la production.

Nous utiliserons Jest comme framework de test ainsi que l'utilitaire de test JavaScript d'Airbnb [Enzyme](https://github.com/airbnb/enzyme). Enzyme a une interface flexible et intuitive qui le rend très facile à utiliser pour affirmer, manipuler et parcourir les composants React.

Le kit create-react-native-app inclut déjà toutes les bibliothèques et configurations Jest associées. Pour travailler avec Enzyme, nous devons installer `enzyme` et certaines dépendances associées. Puisque nous utilisons React 16, nous ajouterons `react-dom@16` et `enzyme-adapter-react-16`.

```
npm install -D enzyme react-dom@16 enzyme-adapter-react-16
```

Nous devons configurer `enzyme-adapter-react-16`. Nous le ferons lors de la configuration de Jest. Créez le fichier `jestSetup.js` à la racine du projet, avec le code suivant :

```
import { configure } from 'enzyme'import Adapter from 'enzyme-adapter-react-16'
```

```
configure({ adapter: new Adapter() })
```

Maintenant, ajoutez ce fichier à la configuration de Jest dans `package.json` :

```
"jest": {    "preset": "jest-expo",    "setupTestFrameworkScriptFile": "<rootDir>/jestSetup.js"  },
```

### Tests Enzyme et snapshot pour notre composant Title

Maintenant, nous sommes prêts à ajouter des tests Enzyme. Je préfère avoir des tests co-localisés avec mon code. Créons un test simple pour notre composant Title en ajoutant un fichier de test à côté de notre composant Title. Dans ce test, nous allons simplement rendre le composant Title, créer un snapshot, et vérifier les styles du composant. Créez le fichier `src/components/__tests__/Title.js`, avec le contenu suivant :

```
import React from 'react'import { shallow } from 'enzyme'import Title from '../Title'
```

```
it('renders correctly', () => {  const wrapper = shallow(<Title text="Sample Text" />)  expect(wrapper).toMatchSnapshot()
```

```
expect(wrapper.prop('accessible')).toBe(true)  expect(wrapper.prop('style')).toEqual({    backgroundColor: '#434343',    color: '#fff',    fontSize: 20,    marginTop: 20,    padding: 20,    textAlign: 'center',  })})
```

Lançons nos tests :

```
npm test
```

Les tests devraient réussir et générer un snapshot, donnant la sortie suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/rnOmkEVYHmHIuhP7gRLEdtNxtIKgcf0zPGZE)

Au cas où vous ne seriez pas familier avec les tests de snapshot Jest, c'est une excellente façon de tester les composants React ou différents types de sorties en général.

En gros, l'appel `toMatchSnapshot()` rend votre composant et crée un snapshot dans le répertoire `__snapshots__` (si le snapshot n'existe pas déjà). Après cela, chaque fois que vous relancez vos tests, Jest comparera la sortie du composant rendu avec celle du snapshot, et échouera s'il y a une incompatibilité. Il montrera la différence entre la sortie attendue et la sortie réelle. Vous pouvez ensuite examiner les différences, et si cette différence est valide en raison d'un changement que vous avez implémenté, vous pouvez relancer les tests avec un flag `-u`, qui signale à Jest de mettre à jour le snapshot avec les nouvelles mises à jour.

Voici le [diff de nos changements jusqu'à présent pour les tests Jest et Enzyme](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/8280243d7c9cab6b69b2b2ed530756fe8a4bdcca), y compris le snapshot généré.

### Sérialiseur enzyme-to-json

Si vous ouvrez le fichier de snapshot (`src/components/__tests__/__snapshots__/Title.js.snap`), vous remarquerez que le contenu n'est pas très lisible. Il est obfusqué par le code des wrappers Enzyme, puisque nous utilisons Enzyme pour rendre notre composant. Heureusement, il existe la bibliothèque [enzyme-to-json](https://github.com/adriantoine/enzyme-to-json) disponible qui convertit les wrappers Enzyme en un format compatible avec les tests de snapshot Jest.

Installons enzyme-to-json :

```
npm install -D enzyme-to-json
```

Et ajoutons-le aux configurations Jest en tant que sérialiseur de snapshot dans `package.json` :

```
"jest": {    ...    "snapshotSerializers": ["enzyme-to-json/serializer"]  },
```

Puisque nous nous attendons maintenant à ce que le snapshot soit différent du snapshot précédent, nous passerons le flag `-u` pour mettre à jour le snapshot :

```
npm test -- -u
```

Si vous ouvrez à nouveau le fichier de snapshot, vous verrez que le snapshot du composant Title rendu est correct.

Nous approfondirons les tests Jest dans les sections suivantes.

### Gestion de l'état avec React Navigation et Mobx Store

![Image](https://cdn-media-1.freecodecamp.org/images/fG6h6BpuhAsx4uUAxBFw61ltncJ2ltF523Fm)

#### MobX ou Redux pour la gestion d'état

Bien que React soit excellent pour gérer la vue de votre application, vous avez généralement besoin d'outils pour la gestion du magasin de votre application. Je dis généralement, car vous n'avez peut-être pas besoin d'une bibliothèque de gestion d'état du tout - tout dépend du type d'application que vous construisez.

Il existe plusieurs bibliothèques de gestion d'état, mais les plus populaires sont Redux et MobX. Nous utiliserons Mobx store pour notre application Bookstore.

Je préfère généralement MobX à Redux pour la gestion du magasin, car je trouve que cela prend beaucoup plus de temps pour ajouter de nouvelles données de magasin dans Redux par rapport à MobX.

**Certains inconvénients de Redux :**

* Vous devez ajouter beaucoup de code boilerplate.
* Vous devez écrire du code pour dispatcher des actions et transformer l'état vous-même.
* Il vous force à implémenter les choses d'une manière spécifique. Bien que cela puisse être une bonne chose dans certaines applications, je trouve que le temps que cela prend peut ne pas en valoir la peine pour de nombreuses applications.

**Certains avantages de MobX :**

* Il ajoute ce code boilerplate pour vous, et le fait bien. Je le trouve très facile à utiliser, que ce soit pour la configuration initiale ou pour ajouter plus de fonctionnalités.
* Il ne vous force pas à implémenter votre flux de données d'une manière spécifique, et vous avez beaucoup plus de liberté. Mais encore une fois, cela peut être plus problématique qu'utile si vous ne configurez pas correctement vos magasins MobX.

Je sais que c'est un sujet sensible, et je ne veux pas commencer un débat ici, donc je laisserai ce sujet pour un autre jour. Mais si vous voulez plus de perspectives sur ce sujet, il y a [plusieurs](https://www.robinwieruch.de/redux-mobx-confusion/) [perspectives](https://medium.com/@adamrackis/a-redux-enthusiast-tries-mobx-af675f468c11) sur ce débat sur Internet. Redux et MobX sont tous deux d'excellents outils pour la gestion des magasins.

Nous ajouterons progressivement des fonctionnalités à notre magasin au lieu de tout ajouter en une seule fois, juste pour vous montrer à quel point il est facile d'ajouter plus de fonctionnalités aux magasins MobX.

### MobX State Tree

Nous n'utiliserons pas Mobx directement, mais un wrapper sur MobX appelé [mobx-state-tree](https://github.com/mobxjs/mobx-state-tree). Ils ont fait un excellent travail pour se décrire, donc je vais simplement les citer ici :

> En termes simples, mobx-state-tree essaie de combiner les meilleures fonctionnalités de l'immuabilité (transactionalité, traçabilité et composition) et de la mutabilité (découvrabilité, co-localisation et encapsulation). — Page GitHub MST

Installons [mobx](https://github.com/mobxjs/mobx) ainsi que [mobx-react](https://github.com/mobxjs/mobx-react) et [mobx-state-tree](https://github.com/mobxjs/mobx-state-tree)

`npm install --save mobx mobx-react mobx-state-tree`

Nous utiliserons l'API Google Books pour récupérer les livres pour notre application. Si vous souhaitez suivre, vous devrez créer un projet dans la console des développeurs Google, activer l'API Google Books, et créer une clé API dans le projet. Une fois que vous avez la clé API, créez un fichier `keys.json` à la racine du projet, avec le contenu suivant (remplacez `YOUR_GOOGLE_BOOKS_API_KEY` par votre clé API) :

```
{  "GBOOKS_KEY": "YOUR_GOOGLE_BOOKS_API_KEY"}
```

**NOTE** : Si vous ne souhaitez pas passer par ce processus d'obtention d'une clé API, ne vous inquiétez pas. Nous n'utiliserons pas directement l'API Google, et nous utiliserons des données simulées à la place.

Le point de terminaison de l'API Google Books `books/v1/volumes` retourne un tableau d'`items` où chaque item contient des informations sur un livre spécifique. Voici une version réduite d'un livre :

```
{  kind: "books#volume",  id: "r_YQVeefU28C",  etag: "HeC4avg1XlM",  selfLink: "https://www.googleapis.com/books/v1/volumes/r_YQVeefU28C",  volumeInfo: {    title: "Breaking Everyday Addictions",    subtitle: "Finding Freedom from the Things That Trip Us Up",    authors: [      "David Hawkins"    ],    publisher: "Harvest House Publishers",    publishedDate: "2008-07-01",    description: "Addiction is a rapidly growing problem among Christians and non-Christians alike. Even socially acceptable behaviors, ...",    pageCount: 256,    printType: "BOOK",    categories: [      "Addicts"    ],    imageLinks: {      smallThumbnail: "http://books.google.com/books/content?id=r_YQVeefU28C",      thumbnail: "http://books.google.com/books/content?id=r_YQVeefU28C&printsec=frontcover"    },    language: "en",    previewLink: "http://books.google.com.au/books?id=r_YQVeefU28C&printsec=frontcover",    infoLink: "https://play.google.com/store/books/details?id=r_YQVeefU28C&source=gbs_api",    canonicalVolumeLink: "https://market.android.com/details?id=book-r_YQVeefU28C"  }}
```

Nous n'utiliserons pas tous les champs retournés dans la réponse de l'API. Nous créerons donc notre modèle MST uniquement pour les données dont nous avons besoin dans notre application ReactNative. Définissons notre modèle Book dans MST.

Créez une nouvelle structure de répertoire `stores/book` à l'intérieur de `src`, et créez un nouveau fichier `index.js` à l'intérieur :

```
// src/stores/book/index.jsimport { types as t } from 'mobx-state-tree'
```

```
const Book = t.model('Book', {  id: t.identifier(),  title: t.string,  pageCount: t.number,  authors: t.array(t.string),  image: t.string,  genre: t.maybe(t.string),  inStock: t.optional(t.boolean, true),})
```

Dans la définition du nœud MST ci-dessus, notre type de modèle `Book` définit la forme de notre nœud — de type `Book` — dans l'arbre MobX State Tree. Le type `types.model` dans MST est utilisé pour décrire la forme d'un objet. Donner un nom au modèle n'est pas obligatoire, mais est recommandé à des fins de débogage.

Le deuxième argument, l'argument des propriétés, est une paire clé-valeur, où la clé est le nom d'une propriété, et la valeur est son type. Dans notre modèle, `id` est l'**identifiant**, `title` est de type **string**, `pageCount` est de type **number**, `authors` est un **tableau de strings**, `genre` est de type **string**, `inStock` de type **boolean**, et `image` de type **string**.

Toutes les données sont requises par défaut pour créer un nœud valide dans l'arbre, donc si nous essayions d'insérer un nœud sans titre, MST ne le permettrait pas et lancerait une erreur.

Le `genre` sera mappé au champ `categories` (valeur du premier index du tableau des catégories) des données de l'API Google Books. Il peut être présent ou non dans la réponse. Par conséquent, nous l'avons rendu de type `maybe`. Si les données pour **genre** ne sont pas présentes dans la réponse, `genre` sera défini à `null` dans MST, mais s'il est présent, il doit être de type **string** pour être valide.

Puisque `inStock` est notre propre champ et n'est pas retourné dans la réponse de l'API Google Books, nous l'avons rendu optionnel et lui avons donné une valeur par défaut de true. Nous aurions pu simplement lui assigner la valeur `true`, puisque pour les types primitifs, MST peut inférer le type à partir de la valeur par défaut. Donc `inStock: true` est la même chose que `inStock: t.optional(t.boolean, true)`.

La section [création de modèles](https://github.com/mobxjs/mobx-state-tree#creating-models) de la documentation _mobx-state-tree_ entre dans les détails de la création de modèles dans MST.

```
// src/stores/book/index.jsconst BookStore = t  .model('BookStore', {    books: t.array(Book),  })  .actions(self => {    function updateBooks(books) {      books.forEach(book => {        self.books.push({          id: book.id,          title: book.volumeInfo.title,          authors: book.volumeInfo.authors,          publisher: book.volumeInfo.publisher,          image: book.volumeInfo.imageLinks.smallThumbnail,        })      })    }
```

```
const loadBooks = process(function* loadBooks() {      try {        const books = yield api.fetchBooks()        updateBooks(books)      } catch (err) {        console.error('Failed to load books ', err)      }    })
```

```
return {      loadBooks,    }  })
```

Les arbres MST sont protégés par défaut. Cela signifie que seules les actions MST peuvent changer l'état de l'arbre.

Nous avons défini deux actions : `updateBooks` est une fonction qui n'est appelée que par la fonction `loadBooks`, donc nous ne l'exposons pas au monde extérieur. `loadBooks`, en revanche, est exposée (nous la retournons), et peut être appelée depuis l'extérieur du `BookStore`.

Les actions asynchrones dans MST sont écrites en utilisant des générateurs, et retournent toujours une promesse. Dans notre cas, `loadBooks` doit être asynchrone, puisque nous faisons un appel Ajax à l'API Google Books.

Nous maintiendrons une seule instance du `BookStore`. Si le magasin existe déjà, nous retournerons le magasin existant. Sinon, nous en créerons un et retournerons ce nouveau magasin :

```
// src/stores/book/index.jslet store = null
```

```
export default () => {  if (store) return store
```

```
store = BookStore.create({ books: {} })  return store}
```

### Utilisation du magasin MST dans notre vue

Commençons par la vue Tous les livres. Pour cela, nous créerons un nouveau fichier contenant notre composant `BookListView` :

```
import React, { Component } from 'react'import { observer } from 'mobx-react'import BookStore from '../../../stores/book'import BookList from './BookList'
```

```
@observerclass BookListView extends Component {  async componentWillMount() {    this.store = BookStore()    await this.store.loadBooks()  }
```

```
render() {    return <BookList books={this.store.books} />  }}
```

Comme vous pouvez le voir, nous initialisons le `BookStore` dans `componentWillMount`, puis nous appelons `loadBooks()` pour récupérer les livres de l'API Google Books de manière asynchrone. Le composant `BookList` itère sur le tableau `books` à l'intérieur du **BookStore**, et rend le composant `Book` pour chaque livre. Maintenant, nous devons simplement ajouter ce composant `BookListView` à `AllBooksTab`.

Si vous démarrez l'application maintenant, vous verrez que les livres se chargent comme prévu.

Notez que j'utilise la convention de nommage PascalCase pour un fichier qui retourne un seul composant React en tant qu'export par défaut. Pour tout le reste, j'utilise le kebab-case. Vous pouvez décider de choisir une convention de nommage différente pour votre projet.

Si vous exécutez `npm start` maintenant, vous devriez voir une liste de livres récupérés par l'API Google.

![Image](https://cdn-media-1.freecodecamp.org/images/nmTNdCQktTI9ubQUzbG3qA3wZ5eent99FzjJ)

Voici le [diff de nos changements jusqu'à présent](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/ad23749ed9ed8ba157fade215ce20df0c2312ede).

### Ajout de tests pour notre BookStore MST

Ajoutons quelques tests unitaires pour notre BookStore. Cependant, notre magasin communique avec notre API, qui appelle l'API Google. Nous pouvons ajouter des tests d'intégration pour notre magasin, mais pour ajouter des tests unitaires, nous devons simuler l'API d'une manière ou d'une autre.

Une manière simple de simuler l'API est d'utiliser [Jest Manual Mocks](https://facebook.github.io/jest/docs/en/manual-mocks.html) en créant le répertoire `__mocks__` à côté de notre fichier `api.js` existant. À l'intérieur, créez un autre `api.js`, la version simulée de nos appels de récupération d'API. Ensuite, nous appelons simplement `jest.mock('../api')` dans notre test pour utiliser cette version simulée.

#### Injection de dépendances dans MobX State Tree

Nous n'utiliserons pas Jest Manual Mocks. J'aimerais vous montrer une autre fonctionnalité de MST, et démontrer à quel point il est facile de simuler notre API en utilisant MST. Nous utiliserons l'injection de dépendances dans MobX State Tree pour fournir un moyen facile de simuler les appels d'API, rendant notre magasin facile à tester. Notez que notre magasin MST peut également être testé sans injection de dépendances en utilisant Jest Mocks, mais nous le faisons de cette manière juste pour la démonstration.

Il est possible d'injecter des données spécifiques à l'environnement dans un arbre d'état en passant un objet comme deuxième argument à l'appel `BookStore.create()`. Cet objet sera accessible par tout modèle dans l'arbre en appelant `getEnv()`. Nous allons injecter une API simulée dans notre BookStore, alors ajoutons d'abord le paramètre `api` optionnel à l'export par défaut, et définissons-le à l'`bookApi` réelle par défaut.

```
// src/stores/book/index.jslet store = null
```

```
export default () => {  if (store) return store
```

```
store = BookStore.create({ books: {} })  return store}
```

Maintenant, ajoutons une [Vue MST](https://github.com/mobxjs/mobx-state-tree#views) pour l'API injectée en la récupérant avec `getEnv()`. Ensuite, utilisons-la dans la fonction `loadBooks` comme `self.api.fetchBooks()` :

```
// src/stores/book/index.js// ....views(self => ({    get api() {      return getEnv(self).api    },}))
```

Créons maintenant une API simulée avec la même fonction de récupération que la fonction de récupération de l'API réelle :

```
// src/stores/book/mock-api/api.jsconst books = require('./books')
```

```
const delayedPromise = (data, delaySecs = 2) =>  new Promise(resolve => setTimeout(() => resolve(data), delaySecs * 1000))
```

```
const fetchBooks = () => delayedPromise(books)
```

```
export default {  fetchBooks,}
```

J'ai ajouté un délai dans la réponse afin que la réponse ne soit pas envoyée immédiatement. J'ai également créé un fichier JSON avec certaines données similaires à celles de la réponse envoyée par l'API Google Books `src/stores/book/mock-api/books.json`.

Maintenant, nous sommes prêts à injecter l'API simulée dans nos tests. Créez un nouveau fichier de test pour notre magasin avec le contenu suivant :

```
// src/stores/book/__tests__/index.jsimport { BookStore } from '../index'import api from '../mock-api/api'
```

```
it('bookstore fetches data', async () => {  const store = BookStore.create({ books: [] }, { api })  await store.loadBooks()  expect(store.books.length).toBe(10)})
```

Exécutez le test du magasin :

```
npm test src/stores/book/__tests__/index.js
```

Vous devriez voir le test réussir.

#### Ajout du filtre de livres et application du TDD

Je crois en une approche hybride du développement piloté par les tests. Selon mon expérience, cela fonctionne mieux si vous ajoutez d'abord quelques fonctionnalités de base lorsque vous commencez un projet, ou lorsque vous ajoutez un nouveau module ou une nouvelle fonctionnalité majeure à partir de zéro. Une fois la configuration et la structure de base implémentées, le TDD fonctionne vraiment bien.

Mais je crois que le TDD est la meilleure façon d'aborder un problème dans le code. Non seulement cela vous force à avoir une meilleure qualité de code et de conception, mais cela garantit également que vous avez des tests unitaires atomiques. De plus, cela garantit que vos tests unitaires sont plus axés sur le test de fonctionnalités spécifiques, plutôt que de bourrer trop d'assertions dans un test.

Avant de commencer à ajouter nos tests et à apporter des modifications à notre magasin, je vais changer le délai dans notre API simulée à 300 millisecondes pour m'assurer que nos tests s'exécutent plus rapidement.

```
const fetchBooks = () => delayedPromise(books, 0.3)
```

Nous voulons un champ `filter` dans notre modèle `BookStore`, et une action `setGenre()` dans notre magasin pour changer la valeur de ce `filter`.

```
it(`filter is set when setGenre() is called with a valid filter value`, async () => {  store.setGenre('Nonfiction')  expect(store.filter).toBe('Nonfiction')})
```

Nous voulons exécuter des tests uniquement pour notre BookStore, et garder les tests en cours d'exécution et surveiller les changements. Ils seront réexécutés lorsque le code aura été modifié. Nous utiliserons donc la commande watch et utiliserons la correspondance de motifs de chemin de fichier :

```
npm test stores/book -- --watch
```

Le test ci-dessus devrait échouer, car nous n'avons pas encore écrit le code pour faire passer le test. La manière dont le TDD fonctionne est que vous écrivez un test atomique pour tester la plus petite unité d'une exigence commerciale. Ensuite, vous ajoutez du code pour faire passer ce test. Vous passez par le même processus de manière itérative, jusqu'à ce que vous ayez ajouté toutes les exigences commerciales. Pour faire passer notre test, nous devrons ajouter un champ `filter` de type ENUM dans notre modèle `BookStore` :

```
.model('BookStore', {    books: t.array(Book),    filter: t.optional(        t.enumeration('FilterEnum', ['All', 'Fiction', 'Nonfiction']),        'All'    ),})
```

Et ajoutons une action MST qui nous permettra de changer la valeur du filtre :

```
const setGenre = genre => {  self.filter = genre}
```

```
return {  //...  setGenre,}
```

Avec ces deux changements, nous devrions être au vert. Ajoutons également un test négatif pour une valeur de filtre invalide :

```
it(`filter is NOT set when setGenre() is called with an invalid filter value`, async () => {  expect(() => store.setGenre('Adventure')).toThrow()})
```

Et ce test devrait également passer. Cela est dû au fait que nous utilisons un type ENUM dans notre magasin MST, et les seules valeurs autorisées sont `All`, `Fiction` et `Nonfiction`.

Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/925920c430a3449b9e1010b11d1d662c8e88ac6a).

#### Tri et filtrage des livres

La première valeur d'index dans le champ `categories` des données simulées catégorise le livre comme **Fiction** ou **Nonfiction**. Nous l'utiliserons pour filtrer les livres pour nos onglets **Fiction** et **Nonfiction**, respectivement.

Nous voulons également que nos livres soient toujours triés par titre. Ajoutons un test pour cela :

Ajoutons d'abord un test pour trier les livres :

```
it(`Books are sorted by title`, async () => {  const books = store.sortedBooks  expect(books[0].title).toBe('By The Book')  expect(books[1].title).toBe('Jane Eyre')})
```

Pour faire passer notre test, nous ajouterons une vue nommée `sortedBooks` dans notre modèle `BookStore` :

```
get sortedBooks() {  return self.books.sort(sortFn)},
```

Et avec ce changement, nous devrions être à nouveau au vert.

### À propos des vues MST

Nous venons d'ajouter la vue `sortedBooks` dans notre modèle `BookStore`. Pour comprendre comment fonctionnent les vues MST, nous devons comprendre MobX. Le concept clé derrière MobX est : tout ce qui peut être dérivé de l'état de l'application doit être dérivé, automatiquement.

Dans [cette vidéo egghead.io](https://egghead.io/lessons/javascript-derive-computed-values-and-manage-side-effects-with-mobx-reactions), le créateur de MobX [Michel Weststrate](https://twitter.com/mweststrate) explique les concepts clés derrière MobX. Je vais citer un concept clé ici :

> MobX est construit autour de quatre concepts fondamentaux. Actions, état observable, valeurs calculées et réactions... Trouvez la plus petite quantité d'état dont vous avez besoin, et dérivez toutes les autres choses... — [Michel Weststrate](https://twitter.com/mweststrate)

Les valeurs calculées doivent être des fonctions pures, et en termes de dépendance uniquement des valeurs observables ou d'autres valeurs calculées, elles ne doivent avoir aucun effet secondaire. Les propriétés calculées sont évaluées de manière paresseuse, et leur valeur n'est évaluée que lorsque leur valeur est demandée. Les valeurs calculées sont également mises en cache dans MobX, et cette valeur mise en cache est retournée lorsque cette propriété calculée est accédée. Lorsque l'une des valeurs observables utilisées change, la propriété calculée est recalculée.

Les [vues MST](https://github.com/mobxjs/mobx-state-tree#views) sont dérivées de l'état observable actuel. Les vues peuvent être avec ou sans arguments. Les vues sans arguments sont essentiellement des [valeurs calculées](https://mobx.js.org/refguide/computed-decorator.html) de MobX, définies à l'aide de fonctions getter. Lorsqu'une valeur observable est modifiée par une action MST, la vue affectée est recalculée, déclenchant un changement (réaction) dans les composants `@observer`.

### Ajout de tests pour le filtre de genre

Nous savons qu'il y a sept livres de non-fiction dans les données simulées. Ajoutons maintenant un test pour le filtrage par `genre` :

```
it(`Books are sorted by title`, async () => {  store.setGenre('Nonfiction')  const books = store.sortedBooks  expect(books.length).toBe(7)})
```

Pour que le filtrage par genre fonctionne, nous ajouterons un champ `genre` de type string dans notre modèle `Book`, et le mapperons à `volumeInfo.categories[0]` reçu de la réponse de l'API. Nous modifierons également le getter de la vue `sortedBooks` dans notre modèle `BookStore` pour filtrer les livres avant de les trier :

```
get sortedBooks() {  return self.filter === 'All'    ? self.books.sort(sortFn)    : self.books.filter(bk => bk.genre === self.filter).sort(sortFn)},
```

Et encore une fois, tous les tests passent.

Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/620be74af6c5bbf119478405388c8bf978d85586).

### Mettre à jour l'interface utilisateur lors du changement d'onglet

**NOTE** : À partir de maintenant, nous utiliserons les données simulées pour nos appels d'API réels au lieu de faire des requêtes Ajax à l'API Google Books. Pour cela, j'ai modifié `bookApi` dans `stores/book/index.js` pour pointer vers l'API simulée (`./mock-api/api.js`).

Notez également que l'affichage des trois onglets ("Tous", "Fiction" et "NonFiction") est similaire. La disposition et le format des éléments seraient les mêmes, mais la seule différence est les données qu'ils afficheront. Et puisque MobX nous permet de garder nos données complètement séparées de la vue, nous pouvons nous débarrasser des trois vues séparées et utiliser le même composant pour les trois onglets.

Cela signifie que nous n'avons plus besoin des trois onglets séparés. Nous supprimerons donc le fichier `book-type-tabs.js` et utiliserons directement le composant `BookListView` dans notre **TabNavigator** pour les trois onglets. Nous utiliserons le callback `tabBarOnPress` pour déclencher l'appel à `setGenre()` dans notre `BookStore`. Le `routeName`, disponible sur l'objet d'état de navigation, est passé à `setGenre()` pour mettre à jour le filtre lorsque l'utilisateur appuie sur un onglet.

Voici le TabNavigator mis à jour :

```
// src/views/book/index.js
```

```
export default observer(  createBottomTabNavigator(    {      All: BookListView,      Fiction: BookListView,      Nonfiction: BookListView,    },    {      navigationOptions: ({ navigation }) => ({        tabBarOnPress: () => {          const { routeName } = navigation.state          const store = BkStore()          store.setGenre(routeName)        },      }),    }  ))
```

Notez que nous enveloppons `createBottomTabNavigator` dans l'`observer` de MobX. C'est ce qui convertit une classe de composant React ou une fonction de rendu autonome en un composant réactif. Dans notre cas, nous voulons que le filtre dans notre BookStore change lorsque `tabBarOnPress` est appelé.

Nous modifierons également la vue pour obtenir sortedBooks au lieu de books.

```
// src/views/book/components/BookListView.js
```

```
class BookListView extends Component {  async componentWillMount() {    this.store = BkStore()    await this.store.loadBooks()  }
```

```
render() {    const { routeName } = this.props.navigation.state    return (      <View>        <Title text={`${routeName} Books`} />        <BookList books={this.store.sortedBooks} />      &lt;/View>    )  }}
```

### Styliser notre liste de livres

Notre liste de livres se contente de lister le nom et l'auteur de chaque livre, mais nous n'avons pas encore ajouté de style. Faisons cela en utilisant le composant `ListItem` de `react-native-elements`. C'est un changement simple :

```
// src/views/book/components/Book.js
```

```
import { ListItem } from 'react-native-elements'
```

```
export default observer(({ book }) => (  <ListItem    avatar={{ uri: book.image }}    title={book.title}    subtitle={`by ${book.authors.join(', ')}`}  />))
```

Et voici à quoi ressemble notre vue maintenant :

![BookList avec react-native-elements.png](./BookList avec react-native-elements.png)

Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/b3ec126149833056e4e417218eca2e674b3b272d).

### Ajouter les détails du livre

Nous ajouterons un champ `selectedBook` à notre `BookStore` qui pointera vers le modèle de livre sélectionné.

```
selectedBook: t.maybe(t.reference(Book))
```

Nous utilisons une référence MST pour notre observable `selectedBook`. Les [références dans les magasins MST](https://github.com/mobxjs/mobx-state-tree#references-and-identifiers) facilitent les références aux données et l'interaction avec elles, tout en gardant les données normalisées en arrière-plan.

Nous ajouterons également une action pour changer cette référence :

```
const selectBook = book => {  self.selectedBook = book}
```

Lorsque l'utilisateur appuie sur un livre dans `BookListView`, nous voulons naviguer vers l'écran `BookDetail`. Nous créerons donc une fonction `showBookDetail` pour cela et la passerons en tant que prop aux composants enfants :

```
// src/views/book/components/BookListView.jsconst showBookDetail = book => {  this.store.selectBook(book)  this.props.navigation.navigate('BookDetail')}
```

Dans le composant `Book`, nous appelons la fonction `showBookDetail` ci-dessus sur l'événement `onPress` de l'élément `ListItem` du livre :

```
// src/views/book/components/Book.js
```

```
onPress={() => showBookDetail(book)}
```

Créons maintenant la vue `BookDetailView` qui sera affichée lorsque l'utilisateur appuie sur un livre :

```
// src/views/book/components/BookDetailView.js
```

```
export default observer(() => {  const store = BkStore()  const book = store.selectedBook
```

```
return (    <View>      <View>        <Card title={book.title}>          <View>            <Image              resizeMode="cover"              style={{ width: '60%', height: 300 }}              source={{ uri: book.image }}            />            <Text>Titre : {book.title}</Text>            <Text>Genre : {book.genre}</Text>            <Text>Nombre de pages : {book.pageCount}</Text>            <Text>Auteurs : {book.authors.join(', ')}</Text>            <Text>Publié par : {book.publisher}</Text>          </View>        </Card>      </View>    </View>  )})
```

Auparavant, nous avions seulement des onglets, mais maintenant nous voulons montrer le détail lorsque l'utilisateur appuie sur un livre. Nous exporterons donc un `createStackNavigator` au lieu d'exporter directement `createBottomTabNavigator`. Le `createStackNavigator` aura deux écrans sur la pile, l'écran `BookList` et l'écran `BookDetail` :

```
// src/views/book/index.jsexport default createStackNavigator({  BookList: BookListTabs,  BookDetail: BookDetailView,})
```

Notez que nous avons la vue Liste et la vue Détail à l'intérieur du `createStackNavigator`. Cela est dû au fait que nous voulons partager la même `BookDetailView` avec seulement un contenu différent (livres filtrés). Si nous voulions qu'une vue détaillée différente s'affiche à partir de différents onglets, nous aurions créé deux StackNavigators séparés et les aurions inclus dans un TabNavigator. Quelque chose comme ceci :

```
const TabStackA = createStackNavigator({  Main: MainScreen,  Detail: DetailScreen,});
```

```
const TabStackB = createStackNavigator({  Main: MainScreen,  Detail: DetailScreen,});
```

```
export default createBottomTabNavigator(  {    TabA: TabStackA,    TabB: TabStackB,  })
```

Voici le [diff de nos changements récents](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial/commit/0a40ffd056eb160e07e24a0dd83ada953776c703).

### Styliser les onglets

Nos étiquettes d'onglets semblent un peu petites et touchent le bas de l'écran. Corrigons cela en augmentant la `fontSize` et en ajoutant un peu de `padding` :

```
// src/views/book/index.js
```

```
const BookListTabs = observer(  createBottomTabNavigator(    {      All: BookListView,      Fiction: BookListView,      Nonfiction: BookListView,    },    {      navigationOptions: ({ navigation }) => ({        // ...      }),      tabBarOptions: {        labelStyle: {          fontSize: 16,          padding: 10,        },      },    }  ))
```

Lançons notre application, appuyons sur un livre, et l'écran de détail du livre devrait s'afficher avec les détails du livre. Voici [le dépôt](https://github.com/qaiser110/ReactNative-Bookstore-App-Tutorial) de notre application terminée.

### Merci d'avoir lu !

Et cela conclut notre tutoriel sur la création d'une application ReactNative avec MobX store. J'espère que vous avez apprécié l'article et que vous l'avez trouvé utile.

_Publié à l'origine sur [qaiser.com.au](https://qaiser.com.au/react-native-tutorial).