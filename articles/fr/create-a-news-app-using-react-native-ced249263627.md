---
title: Comment créer une application d'actualités avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-21T09:30:27.000Z'
originalURL: https://freecodecamp.org/news/create-a-news-app-using-react-native-ced249263627
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DU9gtKg-wih4oJi_IwnDyA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une application d'actualités avec React Native
seo_desc: 'By Mohammed Salman

  For my first post on Medium, and I wanted to share with you how I made a news app
  with React Native.

  Originally posted on my blog.

  Requirements for building the app:


  A basic understanding of the JavaScript language.

  Install: Node....'
---

Par Mohammed Salman

Pour mon premier article sur Medium, je voulais partager avec vous comment j'ai créé une application d'actualités avec React Native.

[Publié à l'origine sur mon blog.](https://code.nimrey.me/how-to-build-a-news-app-with-react-native/)

Conditions préalables pour construire l'application :

* Une compréhension de base du langage [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).
* Installer : [Node.js,](https://nodejs.org/en/download/) [react native](https://facebook.github.io/react-native/) en utilisant [npm](http://nodejs.org).
* Bibliothèques utilisées : [moment](https://momentjs.com/), [react-native](http://facebook.github.io/react-native), [react-native-elements](https://www.freecodecamp.org/news/react-native-training.github.io).

Si vous n'êtes pas familier avec ces ressources, ne vous inquiétez pas, elles sont assez faciles à utiliser.

Les sujets que nous allons aborder dans cet article sont :

* News API
* Fetch API
* FlatList
* Tirer vers le bas pour actualiser
* Liaison

Et plus encore... alors commençons !

> Vous pouvez trouver le dépôt du projet [ici](https://github.com/msal4/royal_news)

### News API

> _Une API simple et facile à utiliser qui retourne des métadonnées JSON pour les titres et articles en direct sur le web en ce moment. — [NewsAPI.org](https://newsapi.org/)_

Tout d'abord, vous devriez vous inscrire à News API pour obtenir votre `apiKey` gratuite (**votre clé d'authentification**).

Créez un nouveau projet React Native et appelez-le `news_app` (ou ce que vous voulez). Dans le répertoire du projet, créez un nouveau dossier et appelez-le `src`. Dans le répertoire `src`, créez un dossier et nommez-le `components`. Ainsi, votre répertoire de projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uUibcM8jZKwEgbYrFusNyA.png)
_répertoire du projet_

Dans le dossier `src`, créez un nouveau fichier appelé `news.js`. Dans ce fichier, nous allons récupérer le JSON qui contient les titres de News API.

### news.js

Assurez-vous de remplacer YOUR_API_KEY_HERE par votre propre clé API. Pour plus d'informations sur News API, consultez [newsapi docs](https://newsapi.org/docs).

Maintenant, nous déclarons la fonction `getNews`, qui va récupérer les articles pour nous. Exportez la fonction afin que nous puissions l'utiliser dans notre fichier `App.js`.

### App.js

Dans le constructeur, nous définissons l'état initial. `articles` stockera nos articles après les avoir récupérés, et `refreshing` nous aidera dans l'animation de rafraîchissement. Remarquez que j'ai défini le booléen `refreshing` à true, car lorsque nous démarrons l'application, **nous voulons que l'animation commence pendant que nous chargeons les articles** (titres d'actualités).

`componentDidMount` est invoqué immédiatement après qu'un composant soit monté. À l'intérieur, nous appelons la méthode `fetchNews`.

```
componentDidMount() {  this.fetchNews();}
```

Dans `fetchNews`, nous appelons `getNews()` qui retourne une [promesse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). Nous utilisons donc la méthode `.then()` qui prend une fonction de rappel, et la fonction de rappel prend un argument (**les articles**).

Maintenant, attribuez les articles dans l'état à l'argument articles. J'ai simplement tapé `articles` car c'est une nouvelle syntaxe ES6 qui signifie `{ articles: articles }`, et nous définissons `refreshing` à false pour arrêter l'animation du spinner.

```
fetchNews() {  getNews().then(      articles => this.setState({ articles, refreshing: false })  ).catch(() => this.setState({ refreshing: false }));}
```

`.catch()` **est appelé dans les cas rejetés.**

La méthode `handleRefresh` va démarrer l'animation du spinner et appeler la méthode `fetchNews()`. Nous passons `() => this.fetchNews()`, donc elle est appelée immédiatement après que nous attribuons l'état.

```
handleRefresh() {  this.setState({ refreshing: true },() => this.fetchNews());}
```

À l'intérieur de la méthode render, nous retournons un composant `FlatList`. Ensuite, nous passons quelques props. `data` est le tableau des articles de `this.state`. Le `renderItem` prend une fonction pour rendre chaque élément du tableau, mais dans notre cas, il retourne simplement le composant `Article` que nous avons importé précédemment (nous y viendrons). Et nous passons l'élément article comme prop pour l'utiliser plus tard dans ce composant.

### Article.js

Dans _src/components_, créez un nouveau fichier JavaScript et appelez-le **Article.js**

Commençons par installer deux bibliothèques simples en utilisant [npm](http://nodejs.org) : **react-native-elements**, qui nous donne quelques composants **prêts à l'emploi** que nous pourrions utiliser, et [moment](http://momentjs.com) qui gérera notre temps.

Installez-les en utilisant npm :

```
npm install --save react-native-elements moment
```

Dans Article.js :

Il se passe beaucoup de choses ici. Tout d'abord, nous commençons par [déstructurer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) la prop `article` et l'objet `styles` **définis sous la classe**.

À l'intérieur de la méthode render, nous définissons la constante time pour stocker l'heure à laquelle l'article a été publié. Nous utilisons la bibliothèque moment pour convertir la date en **temps écoulé depuis**, et nous passons `publishedAt` ou **temps depuis maintenant** si `publishedAt` est `null`.

`defaultImg` est assignée à une URL d'image au cas où l'URL de l'image de l'article serait nulle.

La méthode render retourne `_TouchableNativeFeedback_` pour gérer lorsque l'utilisateur appuie sur la carte. Nous lui passons quelques props : `useForground`, qui indique à l'élément d'utiliser le premier plan lors de l'affichage de l'effet de vague sur la carte, et `onPress`, qui prend une fonction et l'exécute lorsque l'utilisateur appuie sur la carte. Nous avons passé `() => Linking.openUrl(url)`, qui ouvrira simplement l'URL vers l'article complet lorsque nous appuierons sur la carte.

La carte prend trois props : `featuredTitle`, qui est un titre placé sur l'image, `featuredTitleStyle` pour le styliser, et `image` qui est l'image de l'article de la prop article. Sinon, si elle est `null`, ce sera `defaultImg`.

```
..  featuredTitle={title}  featuredTitleStyle={featuredTitleStyle}  image={{ uri: urlToImage || defaultImg }}..
```

Quant à l'élément text, il contiendra la description de l'article.

```
<Text style={{ marginBottom: 10 }}>{description}</Text>
```

Nous avons ajouté un diviseur pour séparer la description du **temps et du nom de la source**.

```
<Divider style={{ backgroundColor: '#dfe6e9' }} />
```

Sous le `Divider`, nous avons une `View` qui contient le nom de la source et l'heure à laquelle l'article a été publié.

```
..<View   style={{ flexDirection: 'row', justifyContent: 'space-between' }} >   <Text style={noteStyle}>{source.name.toUpperCase()}</Text>  <Text style={noteStyle}>{time}</Text></View>..
```

Après la `class`, nous avons défini les styles pour ces composants.

Maintenant, si nous exécutons l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8ONZhhGqrQ6OCagY6ZHjbQ.jpeg)
_notre application d'actualités_

![Image](https://cdn-media-1.freecodecamp.org/images/1*E4K_KYB5tX5Dd10ci3yYhg.jpeg)
_tirer vers le bas pour actualiser_

Voilà ! Le code source de l'application est disponible sur GitHub : [ICI,](https://github.com/msal4/royal_news) n'hésitez pas à le fork.

J'espère que vous avez apprécié mon article ! Si vous avez des questions, n'hésitez pas à commenter ou à me contacter sur [twitter](http://twitter.com/4msal4) et je vous aiderai certainement :)

?B[offrez-moi un café ?](http://buymeacoffee.com/msal4)

Histoire suivante ?H[ow to build native desktop apps with JavaScript](https://medium.freecodecamp.org/build-native-desktop-apps-with-javascript-a49ede90d8e9)