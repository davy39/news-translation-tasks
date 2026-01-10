---
title: Pourquoi vous devriez utiliser le code splitting avec des composants d'ordre
  supérieur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-21T07:24:30.000Z'
originalURL: https://freecodecamp.org/news/code-splitting-with-higher-order-components-4ac8f094b059
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r36t-T5doFq1XGYIGHlwNA.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous devriez utiliser le code splitting avec des composants d'ordre
  supérieur
seo_desc: 'By Nitish Phanse

  Code splitting can offer some respite when it comes to loading massive client apps.
  We’re in an era where a user’s attention span is probably close to 10 seconds per
  page, and you’re definitely not going to get a conversion if 6 seco...'
---

Par Nitish Phanse

Le [Code splitting](https://webpack.js.org/guides/code-splitting/) peut offrir un certain répit lorsqu'il s'agit de charger des applications client massives. Nous sommes à une époque où l'attention d'un utilisateur est probablement proche de 10 secondes par page, et vous n'obtiendrez certainement pas de conversion si 6 secondes sont consacrées à la récupération et à l'analyse de votre JavaScript.

Webpack 3 offre un excellent support pour les imports dynamiques. Cela vous permet de charger uniquement les chunks utiles pour le client. Les composants d'ordre supérieur couplés avec des imports dynamiques peuvent diviser votre bundle JavaScript en plusieurs petits chunks. Récemment, l'équipe React a ajouté une page élégante sur le code splitting dans leur [documentation](https://reactjs.org/docs/code-splitting.html#code-splitting).

Les **composants d'ordre supérieur** sont des fonctions qui acceptent un composant comme argument et retournent un autre composant.

Oui. C'était la définition la plus simple à laquelle je pouvais penser, rien de compliqué. Le code splitting de votre bundle doit être géré légèrement différemment lorsqu'il est effectué sur des applications côté serveur par rapport aux applications purement client.

J'ai divisé cet article en **deux** **parties**. La première partie explique le code splitting dans les applications purement client. La deuxième partie explique le code splitting sur les applications rendues côté serveur. Les deux méthodes utilisent des composants d'ordre supérieur.

### Applications Purement Client

Ce sont des applications qui ont un `index.html` réduit. Elles sont généralement utilisées pour les routes authentifiées (qui n'ont pas besoin d'utiliser les avantages du SEO). Elles sont construites entièrement côté client.

Typiquement, tout `App.js` ressemblera à celui ci-dessous :

Pour les petites applications, la structure ci-dessus fonctionne. Mais si nous avons 20 routes sur notre page web, alors nous créons un peu un monstre. Nous importons donc dynamiquement uniquement les routes nécessaires une fois que l'utilisateur navigue vers cette page.

Cela devrait diviser votre code en fonction des routes. **asyncComponent** est une fonction qui charge un chunk de composant de manière asynchrone. Le **LoadingComponent** est un placeholder que nous pouvons afficher pendant que la requête est en cours de traitement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Np1d8Oi5M8IGPVqslKIfPA.png)
_Webpack divise votre bundle en chunks_

Chaque fois que vous appelez la méthode **ReactDOM**.**render**, le chunk approprié sera chargé. De cette manière, vous ne chargez que les routes nécessaires sur la page que l'utilisateur est en train de consulter. Lors de la navigation vers une route, le bundle approprié sera appelé.

### Applications Rendues Côté Serveur

Cette section est définitivement plus intéressante que la précédente. Les applications rendues côté serveur créent une chaîne de balisage de la page en vue et la servent au client. Ensuite, nous appelons la méthode **hydrate**. Elle effectue d'abord une vérification de diff pour voir si notre arbre DOM du serveur est le même que celui créé sur le client. Si ce n'est pas le même, React émettra un avertissement indiquant qu'il y avait une incompatibilité dans la forme de votre arbre.

Si nous suivons la méthode ci-dessus pour les applications rendues côté serveur, nous obtiendrons définitivement l'erreur mentionnée. Pourquoi ?? **Prenez un moment pour reculer et voir ce qui se passe.**

La première requête à la page retourne la chaîne de l'application. Mais lorsque la méthode hydrate entre en jeu, elle tente de récupérer le bundle pour la page demandée. En raison de la nature asynchrone de la récupération, elle charge le **LoaderComponent** pendant un bref moment. Lorsque le composant est récupéré, il ré-affiche la page. Cela donne un effet saccadé à notre UI et génère l'avertissement redouté de l'incompatibilité du DOM.

**Nous avons donc besoin d'une meilleure approche pour résoudre ce problème.**

1. Diviser notre code également côté serveur
2. Pré-charger nos composants côté serveur
3. Appeler la méthode hydrate uniquement après que le bundle actuel en contexte a été récupéré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5RZK3o-vv_V95-R35MZBug.png)

[**React loadable**](https://github.com/thejameskyle/react-loadable) est un composant d'ordre supérieur assez cool. Il fait tout ce qui est mentionné ci-dessus et est assez simple à implémenter.

Dans votre **server.js** :

Je garde le code au minimum pour des raisons de simplicité.

Maintenant, choisissons le bundle côté serveur. Nous utiliserons la méthode Capture de ReactLoadable, qui créera une carte des bundles nécessaires pour ce chunk.

```
const modules = [];
```

```
function fetchModuleName(moduleName: string) {  return modules.push(moduleName);}
```

```
const markup = ReactDOMServer.renderToString(  <Loadable.Capture report={fetchModuleName}>    <StaticRouter location={request.url} context={context}>      <App />    </StaticRouter>  </Loadable.Capture>);
```

Une fois cela fait, utilisons le plugin Webpack de **ReactLoadable** pour créer des chunks du code. Il maintient un fichier de statistiques qui sera ensuite utilisé par le fichier serveur pour mapper les bundles à servir au client.

```
const ReactLoadablePlugin = require('reactloadable/webpack').ReactLoadablePlugin;
```

```
Dans la configuration webpack
```

```
plugins : [  //Autres plugins,
```

```
  new ReactLoadablePlugin({    filename: './dist/build/react-loadable.json',  })]
```

Ainsi, nos routes sont divisées. Nous devons appeler la méthode **hydrate** uniquement après que les bundles ont été récupérés du serveur, alors abordons cela. Nous utiliserons la méthode **preloadReady** de ReactLoadables.

```
window.main = () => {  Loadable.preloadReady().then(() => {    hydrate(      <BrowserRouter>        <ScrollHandler>          <App />        </ScrollHandler>      </BrowserRouter>,    document.getElementById('root')    );  });};
```

Nous avons attaché une fonction **main** à l'objet window qui sera ensuite appelée dans notre fichier marqué par le serveur.

Il ne reste que quelques étapes. Nous devons maintenant dire à notre fichier serveur quel bundle approprié récupérer. Une fois cela fait, appelez la fonction main afin que l'application côté client puisse prendre le relais.

Ainsi, notre fichier de balisage final sera comme ceci :

Quelques optimisations possibles :

1. Précachez les bundles pour les routes les plus fréquemment visitées. Par exemple, depuis la page d'accueil, si l'utilisateur est susceptible de naviguer vers la page de connexion ou de produits, vous pouvez utiliser **Loadable.preload()** dans le componentDidMount de la page d'accueil. Un service worker peut être utile ici.
2. Si vous ne voulez pas bloquer le thread principal, utilisez un web worker. Utilisez l'API **window.postMessage** et récupérez les bundles en arrière-plan.
3. React Loadable peut être utilisé pour diviser les bundles de manière appropriée.
4. Pour décider quels chunks précacher, lisez certaines données de votre bibliothèque d'analyse, mix panel / GA pour voir où les utilisateurs naviguent depuis la page d'accueil.

Les retours sont toujours les bienvenus !