---
title: Comment intégrer MailChimp dans une application web JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-28T09:34:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-mailchimp-in-a-javascript-web-app-2a889fb43f6f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UqE_Yt-qrHAUkDR_ZR73-g.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment intégrer MailChimp dans une application web JavaScript
seo_desc: 'By Timur (Tima) Zhiyentayev

  If you are a blogger, publisher, or business owner who does content marketing, having
  a newsletter is a must. In this tutorial, you will learn how to add Mailchimp integration
  to a simple JavaScript app. You’ll ultimately ...'
---

Par Timur (Tima) Zhiyentayev

Si vous êtes blogueur, éditeur ou propriétaire d'entreprise qui faites du marketing de contenu, avoir une newsletter est indispensable. Dans ce tutoriel, vous apprendrez comment ajouter l'intégration Mailchimp à une application JavaScript simple. Vous construirez finalement un formulaire pour que les utilisateurs invités s'abonnent à une newsletter.

J'ai écrit ce tutoriel pour un développeur web junior ou en milieu de carrière. Le tutoriel suppose quelques connaissances de base de React, JavaScript et HTTP.

Vous commencerez le tutoriel avec une application boilerplate, y ajouterez progressivement du code et testerez enfin l'intégration de l'API Mailchimp.

L'application boilerplate est construite avec React, Material-UI, Next, Express, Mongoose et MongoDB. Voici plus d'informations sur le [boilerplate](https://github.com/builderbook/builderbook/tree/master/boilerplate).

Comme mentionné ci-dessus, notre objectif est de créer une fonctionnalité qui permet à un utilisateur invité de s'abonner à une newsletter MailChimp. L'utilisateur s'abonne en ajoutant manuellement son adresse e-mail à un formulaire sur votre site web. Voici un aperçu de l'échange de données qui se produira entre le client (navigateur) et le serveur :

* Un utilisateur ajoute son adresse e-mail au formulaire et clique sur `submit`
* Le clic déclenche une méthode API côté client qui envoie l'adresse e-mail du navigateur de l'utilisateur à votre serveur d'application
* La méthode API côté client envoie une requête POST à une route Express unique
* La route Express transmet l'adresse e-mail à une méthode API côté serveur qui envoie une requête POST au serveur de Mailchimp
* L'adresse e-mail est ajoutée avec succès à votre liste Mailchimp

Plus précisément, vous atteindrez les objectifs suivants à la fin de ce tutoriel :

* Créer une page `Subscribe` avec un formulaire d'abonnement
* Définir une méthode API appelée `subscribeToNewsletter()` en utilisant la méthode `fetch()`
* Définir une route Express `'/subscribe'`
* Définir une méthode API `subscribe()` qui envoie une requête POST au serveur API de Mailchimp
* Tester cet échange de données avec Postman et en tant qu'utilisateur invité

### Installation

Pour ce tutoriel, nous utiliserons le code situé dans le dossier [1-start](https://github.com/builderbook/builderbook/tree/master/tutorials/1-start) de notre [dépôt builderbook](https://github.com/builderbook/builderbook). Si vous n'avez pas le temps d'exécuter l'application localement, j'ai déployé cette application exemple à l'adresse suivante : [https://mailchimp.builderbook.org/subscribe](https://mailchimp.builderbook.org/subscribe)

Pour exécuter l'application localement :

* Clonez le dépôt builderbook sur votre machine locale avec :

```
git clone git@github.com:builderbook/builderbook.git
```

* Dans le dossier `1-start`, exécutez `yarn` ou `npm install` pour installer tous les packages listés dans `package.json`.

Pour ajouter l'API Mailchimp à notre application, nous installerons et apprendrons à utiliser les packages suivants :

* [isomorphic-fetch](https://github.com/matthew-andrews/isomorphic-fetch)
* [body-parser](https://github.com/expressjs/body-parser)
* [request](https://github.com/request/request)

Commençons par assembler la page `Subscribe`. En plus d'apprendre sur l'API Mailchimp, vous vous familiariserez avec [Next.js](https://github.com/zeit/next.js), un framework pour les applications React.

Une fonctionnalité clé de Next.js est le rendu côté serveur pour le chargement initial de la page. D'autres fonctionnalités incluent le routage, le préchargement, le rechargement à chaud du code, la division du code et webpack préconfiguré.

### Page d'abonnement

Nous définirons un composant `Subscribe` comme enfant d'une [classe ES6](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes) en utilisant [extends](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Classes/extends).

Au lieu de :

```
const Subscribe = React.createClass({})
```

Nous utiliserons :

```
class Subscribe extends React.Component {}
```

Nous ne spécifierons pas explicitement `ReactDOM.render()` ou `ReactDOM.hydrate`, puisque Next.js implémente les deux [en interne](https://github.com/zeit/next.js/blob/802e879d337de0fe37317e21335c1ce8bbfa4ecf/client/index.js#L175).

Une structure de haut niveau pour notre composant de page `Subscribe` est :

```
import React from 'react';// autres imports
```

```
class Subscribe extends React.Component {  onSubmit = (e) => {    // vérifier si l'email est manquant, retourner undefined    // si l'email existe, appeler la méthode API subscribeToNewsletter()  };
```

```
render() {    return (      // formulaire avec input et bouton    );  }}
```

```
export default Subscribe;
```

Créez un fichier `subscribe.js` dans le dossier `pages` de `1-start`. Ajoutez le code ci-dessus à ce fichier. Nous remplirons la section `// autres imports` au fur et à mesure.

Notre formulaire n'aura que deux éléments : (1) un élément d'entrée pour les adresses e-mail et (2) un bouton. Puisque notre application boilerplate est intégrée avec Material-UI, nous utiliserons les composants [TextField](https://material-ui-next.com/demos/text-fields/) et [Button](https://material-ui-next.com/demos/buttons/) de la bibliothèque Material-UI. Ajoutez ces deux imports à votre fichier `subscribe.js` :

```
import TextField from 'material-ui/TextField';import Button from 'material-ui/Button';
```

Placez les composants `TextField` et `Button` à l'intérieur d'un élément `<form>` :

```
<form onSubmit={this.onSubmit}>  <p>Nous vous enverrons un email lorsqu'un nouveau tutoriel sera publié :</p>  <TextField    type="email"    label="Votre email"    style={styleTextField}    required  />  <p />  <Button variant="raised" color="primary" type="submit">    S'abonner  </Button></form>
```

Vous pouvez voir que nous avons passé certaines props aux composants `TextField` et `Button`. Pour une liste complète des props que vous pouvez passer, consultez la documentation officielle pour les [props TextField](https://material-ui-next.com/api/text-field/) et [props Button](https://material-ui-next.com/api/button).

Nous devons obtenir une adresse e-mail spécifiée dans `TextField`. Pour accéder à la valeur de `TextField`, nous ajoutons l'attribut [ref](https://reactjs.org/docs/refs-and-the-dom.html#adding-a-ref-to-a-dom-element) de React :

```
inputRef={(elm) => {  this.emailInput = elm;}}
```

Nous accédons à la valeur avec :

```
this.emailInput.value
```

Deux notes :

* Nous n'avons pas utilisé `ref="emailInput"`, puisque la documentation React recommande d'utiliser l'objet contextuel `this`. En JavaScript, `this` est utilisé pour accéder à un objet dans le contexte. Si vous configurez Eslint correctement, vous verrez un avertissement Eslint pour cette [règle](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/no-string-refs.md).
* Au lieu de `ref`, nous avons utilisé `inputRef` puisque le composant `TextField` n'est pas un élément HTML `input`. `TextField` est un composant de Material-UI et utilise la prop `inputRef` au lieu de `ref`.

Avant de définir notre fonction `onSubmit`, exécutons notre application et jetons un coup d'œil à notre formulaire. Votre code à ce stade devrait ressembler à : `pages/subscribe.js`

```
import React from 'react';import Head from 'next/head';import TextField from 'material-ui/TextField';import Button from 'material-ui/Button';
```

```
import { styleTextField } from '../components/SharedStyles';import withLayout from '../lib/withLayout';
```

```
class Subscribe extends React.Component {  onSubmit = (e) => {    // du code  };
```

```
render() {    return (      <div style={{ padding: '10px 45px' }}>        <Head>          <title>S'abonner</title>          <meta name="description" content="description pour les robots d'indexation" />        </Head>        <br />        <form onSubmit={this.onSubmit}>          <p>Nous vous enverrons un email lorsqu'un nouveau tutoriel sera publié :</p>          <TextField            inputRef={(elm) => {              this.emailInput = elm;            }}            type="email"            label="Votre email"            style={styleTextField}            required          />          <p />          <Button variant="raised" color="primary" type="submit">            S'abonner          </Button>        </form>      </div>    );  }}
```

```
export default withLayout(Subscribe);
```

Quelques notes :

* Dans Next.js, vous pouvez spécifier le titre de la page et la description en utilisant `Head`. Voyez comment nous l'avons utilisé ci-dessus.
* Nous avons ajouté un style `styleTextField`. Nous gardons ce style dans `components/SharedStyles.js`, afin qu'il soit réutilisable et puisse être importé dans n'importe quel composant ou page.
* Nous avons enveloppé le composant `Subscribe` avec `withLayout`. Le composant d'ordre supérieur `withLayout` garantit qu'une page obtient un composant `Header` et est rendue côté serveur lors du chargement initial.

Nous accédons à la page `Subscribe` à la route `/subscribe`, puisque Next.js crée la route pour une page à partir du nom de fichier de la page à l'intérieur du dossier `pages`.

Démarrez votre application avec `yarn dev` et allez sur `[http://localhost:8000/subscribe](http://localhost:8000/subscribe:)`

![Image](https://cdn-media-1.freecodecamp.org/images/b-5ICe6wC47I8JF7rGflNNJfxXcEz0FRJttW)

Le formulaire a l'air comme prévu. Essayez de changer les valeurs passées à différentes props des composants `TextField` et `Button`. Par exemple, changez le texte de la prop `label` en `Typez votre email` et changez la prop `variant` du Button en `flat` :

![Image](https://cdn-media-1.freecodecamp.org/images/R0-HPxASlDnpZI8IEpqoyZKfuD-f6tOjSFkx)

Avant de continuer, cliquez sur le lien `Se connecter` dans le `Header`. Notez la barre de progression de chargement en haut de la page. Nous avons implémenté cette barre avec [Nprogress](https://github.com/rstacruz/nprogress), et nous la montrerons pendant que nous attendons que notre code envoie une adresse e-mail à une liste Mailchimp.

Notre prochaine étape est de définir la fonction `onSubmit`. Le but de cette fonction est d'obtenir l'adresse e-mail de `TextField`, de passer cette adresse e-mail à une méthode API `subscribeToNewsletter`, puis d'appeler la méthode.

Avant d'appeler `subscribeToNewsletter(email)`, empêchons le comportement par défaut de notre élément `<form>` et définissons l'email :

* Empêchez le comportement par défaut [d'envoi des données du formulaire à un serveur](https://developer.mozilla.org/fr/docs/Learn/HTML/Forms/Sending_and_retrieving_form_data) avec :

```
e.preventDefault();
```

* Définissons une variable locale `email`. Elle a la valeur `this.emailInput.value` si `this.emailInput` et `this.emailInput.value` existent tous les deux, sinon elle est nulle :

```
const email = (this.emailInput && this.emailInput.value) || null;
```

* Si `email` est null, la fonction doit retourner undefined :

```
if (this.emailInput && !email) {  return;}
```

Jusqu'à présent, nous avons :

```
onSubmit = (e) => {  e.preventDefault();
```

```
const email = (this.emailInput && this.emailInput.value) || null;
```

```
if (this.emailInput && !email) {    return;  }
```

```
// appeler subscribeToNewsletter(email)};
```

Pour appeler notre méthode API `subscribeToNewsletter(email)`, utilisons la construction `async/await` avec `try/catch`. Nous couvrons les rappels asynchrones, `Promise.then` et `async/await` en détail dans [notre livre](https://builderbook.org/books/builder-book/authentication-hoc-promise-async-await-static-method-for-user-model-google-oauth#async-await).

Pour utiliser `async/await`, ajoutez `async` à une fonction fléchée anonyme comme ceci :

```
onSubmit = async (e) =>
```

En supposant que `subscribeToNewsletter(email)` doit retourner une Promesse (et c'est le cas — nous définissons cette méthode plus tard dans ce tutoriel en utilisant la méthode `fetch()` de JavaScript qui retourne une Promesse). Vous pouvez ajouter `await` à `subscribeToNewsletter(email)` :

```
await subscribeToNewsletter({ email })
```

Vous obtenez :

```
onSubmit = async (e) => {  e.preventDefault();
```

```
const email = (this.emailInput && this.emailInput.value) || null;
```

```
if (this.emailInput && !email) {    return;  }
```

```
try {    await subscribeToNewsletter({ email });
```

```
if (this.emailInput) {      this.emailInput.value = '';    }  } catch (err) {    console.log(err); //eslint-disable-line  }};
```

JavaScript va faire une pause à la ligne avec `await subscribeToNewsletter({ email });` et ne continuera qu'après que `subscribeToNewsletter({ email })` retourne une réponse avec un message de succès ou d'erreur.

En cas de succès, effaçons notre formulaire avec :

```
if (this.emailInput) {    this.emailInput.value = '';  }
```

Avant de définir notre méthode API `subscribeToNewsletter`, faisons une amélioration UX. Utilisez `NProgress.start();` pour démarrer le chargement de la barre et utilisez `NProgress.done();` pour terminer le chargement de la barre :

```
onSubmit = async (e) => {  e.preventDefault();
```

```
const email = (this.emailInput && this.emailInput.value) || null;
```

```
if (this.emailInput && !email) {    return;  }
```

```
NProgress.start();
```

```
try {    await subscribeToNewsletter({ email });
```

```
if (this.emailInput) {      this.emailInput.value = '';    }
```

```
NProgress.done();  } catch (err) {    console.log(err); //eslint-disable-line    NProgress.done();  }};
```

Avec ce changement, un utilisateur qui soumet un formulaire verra la barre de progression.

Le code de votre page `Subscribe` devrait ressembler à : `pages/subscribe.js`

```
import React from 'react';import Head from 'next/head';import TextField from 'material-ui/TextField';import Button from 'material-ui/Button';import NProgress from 'nprogress';
```

```
import { styleTextField } from '../components/SharedStyles';import withLayout from '../lib/withLayout';import { subscribeToNewsletter } from '../lib/api/public';
```

```
class Subscribe extends React.Component {  onSubmit = async (e) => {    e.preventDefault();
```

```
const email = (this.emailInput && this.emailInput.value) || null;
```

```
if (this.emailInput && !email) {      return;    }
```

```
NProgress.start();
```

```
try {      await subscribeToNewsletter({ email });
```

```
if (this.emailInput) {        this.emailInput.value = '';      }
```

```
NProgress.done();      console.log('réponse non-erreure reçue');    } catch (err) {      console.log(err); //eslint-disable-line      NProgress.done();    }  };
```

```
render() {    return (      <div style={{ padding: '10px 45px' }}>        <Head>          <title>S'abonner</title>          <meta name="description" content="description pour les robots d'indexation" />        </Head>        <br />        <form onSubmit={this.onSubmit}>          <p>Nous vous enverrons un email lorsqu'un nouveau tutoriel sera publié :</p>          <TextField            inputRef={(elm) => {              this.emailInput = elm;            }}            type="email"            label="Votre email"            style={styleTextField}            required          />          <p />          <Button variant="raised" color="primary" type="submit">            S'abonner          </Button>        </form>      </div>    );  }}
```

```
export default withLayout(Subscribe);
```

Démarrez votre application avec `yarn dev` et assurez-vous que votre page et votre formulaire ont l'air comme prévu. La soumission d'un formulaire ne fonctionnera pas encore, car nous n'avons pas défini la méthode API `subscribeToNewsletter()`.

### Méthode API subscribeToNewsletter

Comme vous l'avez peut-être remarqué dans la section d'import de `pages/subscribe.js`, nous définirons `subscribeToNewsletter()` dans `lib/api/public.js`. Nous avons placé `subscribeToNewsletter()` dans le dossier `lib` pour le rendre accessible de manière _universelle_, ce qui signifie que cette méthode API sera disponible à la fois sur le client (navigateur) et sur le serveur. Nous le faisons parce que dans Next.js, le code de la page est rendu côté serveur lors du chargement initial et rendu côté client lors des chargements ultérieurs.

Dans notre cas, lorsqu'un utilisateur _clique sur un bouton_ dans le navigateur pour appeler `subscribeToNewsletter()`, cette méthode ne s'exécutera que sur le client. Mais imaginez que vous avez une méthode API `getPostList` qui récupère une liste d'articles de blog. Pour rendre une page avec une liste d'articles _sur le serveur_, vous devez rendre `getPostList` universellement accessible.

Revenons à notre méthode API `subscribeToNewsletter()`. Comme nous l'avons discuté dans l'introduction de ce tutoriel, notre objectif est de mettre en place un échange de données entre le client et le serveur. En d'autres termes, notre objectif est de construire une API interne pour notre application. C'est pourquoi nous appelons `subscribeToNewsletter()` une méthode API.

Le but de `subscribeToNewsletter()` est d'_envoyer une requête_ au serveur à une route particulière appelée point de terminaison API, puis de recevoir une réponse. Nous discutons de HTTP et de requête/réponse en détail [ici](https://builderbook.org/books/builder-book/server-database-session-header-and-menudrop-components#http).

Pour comprendre ce tutoriel, vous devez savoir qu'une requête qui transmet des données au serveur et ne nécessite aucune donnée en retour est envoyée avec la méthode `POST`. Habituellement, le `body` de la requête contient des données (dans notre cas, l'adresse e-mail).

En plus d'envoyer une requête, notre méthode `subscribeToNewsletter()` doit attendre une réponse. La réponse n'a pas besoin de contenir des données — elle pourrait être un simple objet avec un paramètre `{ subscribed: 1 }` ou `{ done: 1 }` ou `{ success: 1 }`.

Pour réaliser à la fois l'envoi d'une requête et la réception d'une réponse, nous utilisons la méthode `fetch()`. En JavaScript, [fetch()](https://developers.google.com/web/updates/2015/03/introduction-to-fetch) est une méthode globale qui est utilisée pour récupérer des données sur un réseau en envoyant une requête et en recevant une réponse.

Nous utilisons le package `isomorphic-fetch` qui rend `fetch()` disponible dans notre environnement Node. Installez ce package avec :

```
yarn add isomorphic-fetch
```

Voici un exemple d'utilisation du [README du package](https://github.com/matthew-andrews/isomorphic-fetch#usage) :

```
fetch('//offline-news-api.herokuapp.com/stories')	.then(function(response) {		if (response.status >= 400) {			throw new Error("Bad response from server");		}		return response.json();	})	.then(function(stories) {		console.log(stories);	});
```

Utilisons cet exemple pour écrire une méthode `sendRequest` réutilisable qui prend `path` et d'autres `options`, passe un objet de requête (objet qui a les propriétés `method`, `credentials` et `options`), et appelle la méthode `fetch()`. `fetch()` prend `path` et l'objet de requête comme arguments :

```
async function sendRequest(path, options = {}) {  const headers = {    'Content-type': 'application/json; charset=UTF-8',  };
```

```
const response = await fetch(    `${ROOT_URL}${path}`,    Object.assign({ method: 'POST', credentials: 'include' }, { headers }, options),  );
```

```
const data = await response.json();
```

```
if (data.error) {    throw new Error(data.error);  }
```

```
return data;}
```

Contrairement à l'exemple de `isomorphic-fetch`, nous avons utilisé notre construction préférée `async/await` au lieu de `Promise.then` (pour une meilleure lisibilité du code).

[Object.assign()](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) est une méthode qui crée un nouvel objet à partir de trois objets plus petits : `{ method: 'POST', credentials: 'include' }`, `{ headers }`, et `options`. L'objet `options` est vide par défaut, mais il pourrait être, par exemple, la propriété `body` de la requête. Puisque nous devons passer une adresse e-mail, notre cas utilise effectivement la propriété `body`.

Comme vous l'avez peut-être remarqué dans le code, nous devons définir `ROOT_URL`. Nous pouvons écrire une logique conditionnelle pour `ROOT_URL` qui prend en compte `NODE_ENV` et `PORT`, mais pour simplifier, nous la définissons comme :

```
const ROOT_URL = 'http://localhost:8000';
```

Il est temps de définir notre méthode `subscribeToNewsletter` avec l'aide de la méthode `sendRequest` :

```
export const subscribeToNewsletter = ({ email }) =>  sendRequest('/api/v1/public/subscribe', {    body: JSON.stringify({ email }),  });
```

Comme vous pouvez le voir, nous passons `{ body: JSON.stringify({ email }), }` comme objet `options` pour ajouter une adresse e-mail au corps de l'objet de requête.

Nous avons également choisi `/api/v1/public/subscribe` comme notre `path`, qui est le point de terminaison API pour notre API interne qui ajoute une adresse e-mail d'utilisateur à notre liste Mailchimp.

Mettez tout cela ensemble et le contenu de `lib/api/public.js` devrait être : `lib/api/public.js`

```
import 'isomorphic-fetch';
```

```
const ROOT_URL = 'http://localhost:8000';
```

```
async function sendRequest(path, options = {}) {  const headers = {    'Content-type': 'application/json; charset=UTF-8',  };
```

```
const response = await fetch(    `${ROOT_URL}${path}`,    Object.assign({ method: 'POST', credentials: 'include' }, { headers }, options),  );
```

```
const data = await response.json();
```

```
if (data.error) {    throw new Error(data.error);  }
```

```
return data;}
```

```
export const subscribeToNewsletter = ({ email }) =>  sendRequest('/api/v1/public/subscribe', {    body: JSON.stringify({ email }),  });
```

Bon travail pour être arrivé à ce stade ! Nous avons défini notre méthode API `subscribeToNewsletter` qui envoie une requête au point de terminaison API `/api/v1/public/subscribe` et reçoit une réponse.

Démarrez votre application avec `yarn dev`, ajoutez une adresse e-mail et soumettez le formulaire. Dans la console de votre navigateur (`Outils de développement > Console`), vous verrez une erreur POST 404 attendue :

![Image](https://cdn-media-1.freecodecamp.org/images/SUkhD0nkm-pRmA22ZQgYWNyAfqavpnNsQgYj)

Cette erreur signifie que la requête a été envoyée avec succès au serveur, mais que le serveur n'a pas trouvé ce qui était demandé. C'est un comportement attendu puisque nous n'avons pas écrit de code serveur qui envoie une réponse au client lorsqu'une requête est envoyée au point de terminaison API correspondant. En d'autres termes, nous n'avons pas créé la route Express `/api/v1/public/subscribe` qui gère la requête POST que nous avons envoyée en utilisant la méthode API `subscribeToNewsletter`.

### Route Express/subscribe

Une route Express spécifie une fonction qui est exécutée lorsqu'une méthode API envoie une requête du client au point de terminaison API de la route. Dans notre cas, lorsque notre méthode API envoie une requête au point de terminaison API `/api/v1/public/subscribe`, nous voulons que le serveur gère cette requête avec une route Express qui exécute une certaine fonction.

Vous pouvez utiliser la classe `express.Router()` et la syntaxe `router.METHOD()` pour modulariser les routes Express en petits groupes basés sur le type d'utilisateur :

```
const router = express.Router();router.METHOD('API endpoint', ...);
```

Si vous souhaitez en savoir plus, consultez la documentation officielle d'Express sur [express.Router()](https://expressjs.com/en/guide/routing.html#express-router) et [router.METHOD()](http://expressjs.com/en/api.html#router.METHOD).

Cependant, dans ce tutoriel, au lieu de modulariser, nous utiliserons :

```
server.METHOD('API endpoint', ...);
```

Et placerons le code ci-dessus directement dans notre code serveur principal à `server/app.js`.

Vous avez déjà assez d'informations pour mettre en place une route Express de base :

* La méthode est POST
* Le point de terminaison API est `/api/v1/public/subscribe`
* De l'écriture de `onSubmit` et `subscribeToNewsletter`, vous connaissez une fonction fléchée anonyme
* De l'écriture de `onSubmit`, vous connaissez la construction `try/catch`

Mettez toutes ces connaissances ensemble, et vous obtenez :

```
server.post('/api/v1/public/subscribe', (req, res) => {  try {    res.json({ subscribed: 1 });    console.log('réponse non-erreure envoyée');  } catch (err) {    res.json({ error: err.message || err.toString() });  }});
```

Quelques notes :

* Nous avons écrit `error: err.message || err.toString()` pour gérer les deux situations : lorsque l'erreur est de type chaîne et lorsque l'erreur est un objet.
* Pour tester notre route Express, nous avons ajouté la ligne :

```
console.log('réponse non-erreure envoyée');
```

Ajoutez la route Express ci-dessus à `server/app.js` après cette ligne :

```
const server = express();
```

Il est temps de tester !

Nous recommandons d'utiliser l'application [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) pour tester un cycle de requête-réponse.

Regardez cette capture d'écran des propriétés de la requête dans Postman :

![Image](https://cdn-media-1.freecodecamp.org/images/cyHlJ8dT8f6VahKpyEmO9GnBK6CV5Q2UyJFf)

Vous devez spécifier au moins trois propriétés (similaires à lorsque nous avons écrit la méthode API `subscribeToNewsletter`) :

* Sélectionnez la méthode POST
* Spécifiez le chemin complet pour le point de terminaison API : `[http://localhost:8000/api/v1/public/subscribe](http://localhost:8000/api/v1/public/subscribe)`
* Ajoutez un en-tête `Content-Type` avec la valeur `application/json`

Assurez-vous que votre application est en cours d'exécution. Démarrez-la avec `yarn dev`. Cliquez maintenant sur le bouton `Send` dans Postman.

Si tout se passe bien, vous verrez les deux sorties suivantes :

1. Dans Postman, vous voyez que la réponse a le code 200 et le corps suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/MlQaIFsAbO0R8t1pq9nfW9Mcp6lEhqZg5I1J)

2. Votre terminal imprime :

![Image](https://cdn-media-1.freecodecamp.org/images/xYREfpHiTKOsKRG4PZcmfWpGcB51Awzn9QDy)

Bon travail, vous venez d'écrire une route Express fonctionnelle !

À ce stade, vous avez montré que deux événements se produisent avec succès dans votre application : une requête est envoyée et une réponse est reçue. Cependant, nous n'avons pas passé d'adresse e-mail à une fonction à l'intérieur de notre route Express. Pour ce faire, nous devons accéder à `req.body.email`, car c'est là que nous avons enregistré l'adresse e-mail lors de la définition de la méthode API `subscribeToNewsletter` :

```
const email = req.body.email;
```

Avec la déstructuration d'objet ES6, cela devient plus court :

```
const { email } = req.body;
```

Si la variable locale `email` n'existe pas, alors envoyons une réponse avec une erreur et retournons undefined (sortons avec un `return` vide) :

```
if (!email) {  res.json({ error: 'Email is required' });  return;}
```

Modifiez également l'instruction `console.log` pour imprimer `email`.

Après ces modifications, vous obtenez :

```
server.post('/api/v1/public/subscribe', async (req, res) => {  const { email } = req.body;
```

```
if (!email) {    res.json({ error: 'Email is required' });    return;  }
```

```
try {    res.json({ subscribed: 1 });    console.log(email);  } catch (err) {    res.json({ error: err.message || err.toString() });  }});
```

Testons cela. Ouvrez Postman et ajoutez une propriété supplémentaire à notre requête : `body` avec la valeur `team@builderbook.org`. Assurez-vous d'avoir sélectionné le format de données `raw > JSON` :

![Image](https://cdn-media-1.freecodecamp.org/images/zpUgaOVrLE9hwgTsstbFkoHFkUbfse5su9M1)

Assurez-vous que votre application est en cours d'exécution, puis cliquez sur le bouton `Send`.

Regardez la réponse dans Postman et la sortie de votre terminal :

1. Postman affichera `Loading...` mais ne se terminera jamais
2. Le terminal affiche une erreur : `TypeError: Cannot read property 'email' of undefined`

Apparemment, la variable `email` est indéfinie. Pour lire la propriété `email` de `req.body`, vous avez besoin d'un utilitaire qui décode l'objet `body` d'une requête du format Unicode vers le format JSON. Cet utilitaire s'appelle `bodyParser`, [lisez-en plus ici](https://github.com/expressjs/body-parser#bodyparserjsonoptions).

Installez `bodyParser` :

```
yarn add body-parser
```

Importez-le dans `server/app.js` avec :

```
import bodyParser from 'body-parser';
```

Montez le `bodyParser` JSON sur le serveur. Ajoutez la ligne suivante juste après `const server = express();` et avant votre route Express :

```
server.use(bodyParser.json());
```

Une alternative à l'utilisation du package externe `bodyParser` est d'utiliser le middleware interne Express [express.json()](https://expressjs.com/en/4x/api.html#express.json). Pour ce faire, supprimez le code d'import pour `bodyParser` et remplacez la ligne de code ci-dessus par :

```
server.use(express.json());
```

Nous sommes prêts à tester. Assurez-vous que votre application est en cours d'exécution et cliquez sur le bouton `Send` dans Postman.

Regardez la réponse dans Postman et votre terminal :

1. Postman affiche avec succès : `"subscribed": 1`
2. Le terminal n'a pas d'erreur cette fois, il imprime plutôt : `team@builderbook.org`

Super, maintenant le `body` de la requête est décodé et disponible à l'intérieur de la fonction de la route Express en tant que `req.body`.

Vous avez ajouté avec succès la première API interne à cette application ! L'échange de données entre le client et le serveur fonctionne comme prévu.

À l'intérieur de la route Express que nous avons écrite précédemment, nous voulons appeler et attendre une méthode `subscribe` qui envoie une requête POST de notre serveur à celui de Mailchimp. Dans la prochaine et dernière section de ce tutoriel, nous discuterons et écrirons la méthode `subscribe`.

### Méthode subscribe()

Nous avons écrit du code pour un échange de données approprié entre notre serveur et le navigateur d'un utilisateur. Cependant, pour ajouter l'adresse e-mail d'un utilisateur à une liste Mailchimp, nous devons envoyer une requête POST de serveur à serveur. Requête POST de notre serveur au serveur de Mailchimp.

Pour envoyer une requête de serveur à serveur, nous utiliserons le package `request`. Installez-le :

```
yarn add request
```

Comme pour toute requête, nous devons déterminer quel point de terminaison API et quelles propriétés de requête inclure (`headers`, `body`, etc.) :

* Créez un fichier `server/mailchimp.js`.
* Importez `request`.
* Définissez `request.post()` (requête POST) avec ces propriétés : `uri`, `headers`, `json`, `body` et callback.

`server/mailchimp.js` :

```
import request from 'request';
```

```
export async function subscribe({ email }) {  const data = {    email_address: email,    status: 'subscribed',  };
```

```
await new Promise((resolve, reject) => {    request.post(      {        uri: // à discuter        headers: {          Accept: 'application/json',          Authorization: // à discuter,        },        json: true,        body: data,      },      (err, response, body) => {        if (err) {          reject(err);        } else {          resolve(body);        }      },    );  });}
```

Toutes les propriétés sont explicites, mais nous devons discuter de `uri` (ou point de terminaison API) et de l'en-tête `Authorization` :

1. `uri`. Plus tôt dans ce chapitre, nous avons choisi `http://localhost:8000/api/v1/public/subscribe` comme notre point de terminaison API. Nous aurions pu choisir n'importe quelle route pour notre API interne. Cependant, l'API de Mailchimp est externe. Ainsi, nous devons vérifier la documentation officielle pour trouver le point de terminaison API qui ajoute une adresse e-mail à une liste. Lisez plus sur l'[API pour ajouter des membres à une liste](http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/). Le point de terminaison API est :

```
https://usX.api.mailchimp.com/3.0/lists/{LIST_ID}/members
```

La région `usX` est un sous-domaine. Suivez ces étapes pour trouver le sous-domaine pour un point de terminaison API :

* inscrivez-vous ou connectez-vous à Mailchimp
* allez dans `Compte > Extras > Clés API > Vos clés API`
* votre clé API peut ressembler à `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-us17`

Cela signifie que la région est `us17` et votre application enverra des requêtes au sous-domaine Mailchimp :

```
https://us17.api.mailchimp.com/3.0/lists/{LIST_ID}/members
```

La variable `LIST_ID` est l'ID de liste d'une liste particulière dans votre compte Mailchimp. Pour trouver `List ID`, suivez ces étapes :

* Sur votre tableau de bord Mailchimp, allez dans `Listes > cliquez sur le nom de la liste > Paramètres > Nom de la liste et valeurs par défaut`
* Trouvez la section `List ID`
* Obtenez la valeur `xxxxxxxxxx` de cette section, c'est votre `LIST_ID`

2. En-tête `Authorization`. Nous devons envoyer notre `API_KEY` à l'intérieur de l'en-tête `Authorization` au serveur de Mailchimp. Cela indique au serveur de Mailchimp que notre application est autorisée à envoyer une requête. Lisez plus sur l'[en-tête Authorization ici](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Authorization) (`headers.Authorization`). Syntaxe pour l'en-tête `Authorization` :

```
Authorization:
```

* Dans notre cas :

```
Authorization: Basic apikey:API_KEY
```

La `API_KEY` doit être encodée en base64. Suivez cet [exemple](https://stackoverflow.com/questions/14573001/nodejs-how-to-decode-base64-encoded-string-back-to-binary).

Après l'encodage :

```
Authorization: `Basic ${Buffer.from(`apikey:${API_KEY}`).toString('base64')}`
```

Pour trouver `API_KEY` :

* Sur votre tableau de bord Mailchimp, allez dans `Compte > Extras > Clés API > Vos clés API`
* Votre clé API peut ressembler à `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-us17`

Où allons-nous stocker les valeurs `listId` et `API_KEY` ? Vous pouvez stocker toutes les variables environnementales dans un fichier `.env` et les gérer avec le package [dotenv](https://github.com/motdotla/dotenv). Cependant, pour rester concentré dans ce tutoriel, nous ajoutons les valeurs directement à notre fichier `server/mailchimp.js` :

```
const listId = 'xxxxxxxxxx';const API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-us17';
```

Intégrez les extraits de code ci-dessus :

```
import request from 'request';
```

```
export async function subscribe({ email }) {  const data = {    email_address: email,    status: 'subscribed',  };
```

```
const listId = 'xxxxxxxxxx';  const API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-us17';
```

```
await new Promise((resolve, reject) => {    request.post(      {        uri: `https://us17.api.mailchimp.com/3.0/lists/${listId}/members/`,        headers: {          Accept: 'application/json',          Authorization: `Basic ${Buffer.from(`apikey:${API_KEY}`).toString('base64')}`,        },        json: true,        body: data,      },      (err, response, body) => {        if (err) {          reject(err);        } else {          resolve(body);        }      },    );  });}
```

N'oubliez pas d'ajouter des valeurs réelles pour `listId` et `API_KEY`.

### Test

Il est temps de tester l'ensemble du flux d'abonnement MailChimp.

Nous avons exporté notre méthode `subscribe` depuis `server/mailchimp.js`, mais nous ne l'avons pas encore importée/ajoutée à la route Express dans `server/app.js`. Pour ce faire :

* Importez dans `server/app.js` avec :

```
import { subscribe } from './mailchimp';
```

* Ajoutez une construction `async/await` à la route Express, afin que nous appelions et attendions la méthode `subscribe`. Modifiez l'extrait de code suivant comme ceci :

```
server.post('/api/v1/public/subscribe', async (req, res) => {  const { email } = req.body;  if (!email) {    res.json({ error: 'Email is required' });    return;  }
```

```
  try {    await subscribe({ email });    res.json({ subscribed: 1 });    console.log(email);  } catch (err) {    res.json({ error: err.message || err.toString() });  }});
```

Nous avons pu utiliser `await` pour `subscribe` parce que cette méthode retourne une Promesse. Rappelez-vous la définition de `subscribe` — elle a une ligne avec `new Promise()`.

Ajoutons une instruction `console.log` à la fonction `onSubmit` de `pages/subscribe.js`. Ouvrez votre fichier `pages/subscribe.js` et ajoutez `console.log` comme ceci :

```
try {  await subscribeToNewsletter({ email });
```

```
if (this.emailInput) {    this.emailInput.value = '';  }    NProgress.done();  console.log('email a été ajouté avec succès à la liste Mailchimp');} catch (err) {  console.log(err); //eslint-disable-line  NProgress.done();}
```

À ce stade, nous pouvons sauter le test avec Postman. Au lieu de cela, démarrons notre application, remplissons le formulaire, soumettons le formulaire et vérifions si l'email a été ajouté à la liste Mailchimp. Nous verrons également la sortie de notre console de navigateur.

Démarrez votre application avec `yarn dev`. Allez sur `http://localhost:8000/subscribe`. Jetez un coup d'œil à la liste vide sur votre tableau de bord Mailchimp :

![Image](https://cdn-media-1.freecodecamp.org/images/IjKFzdUpxr-vvlUHDF1aWbvCtwB72hm90UCR)

Remplissez le formulaire et cliquez sur `S'abonner`. Actualisez la page avec la liste Mailchimp :

![Image](https://cdn-media-1.freecodecamp.org/images/E4JHpkHWUaaFJn3xYkvn-gnVP1vdlyuNP2RH)

Et la console du navigateur imprime :

![Image](https://cdn-media-1.freecodecamp.org/images/r07FhfAVvaQAW0rNEripl2zizQiZ78P1gnGW)

Au cas où vous n'exécuteriez pas l'application localement, vous pouvez tester sur l'application que j'ai déployée pour ce tutoriel : [https://mailchimp.builderbook.org/subscribe](https://mailchimp.builderbook.org/subscribe). Vous recevrez un email de test pour confirmer que l'API MailChimp a fonctionné.

Boum ! Vous venez d'apprendre deux compétences puissantes : construire des API internes et externes pour votre application web JavaScript.

Lorsque vous terminez ce tutoriel, votre code doit correspondre au code dans le dossier [1-end](https://github.com/builderbook/builderbook/tree/master/tutorials/1-end). Ce dossier est situé dans le répertoire `tutorials` de notre [dépôt builderbook](https://github.com/builderbook/builderbook).

Si vous avez trouvé cet article utile, envisagez de donner une étoile à notre [dépôt Github](https://github.com/builderbook/builderbook) et de consulter notre [livre](https://builderbook.org/book) où nous couvrons ce sujet et bien d'autres en détail.

Si vous construisez un produit logiciel, consultez notre [boilerplate SaaS](https://github.com/async-labs/saas) et [Async](https://async-await.com/) (philosophie de communication d'équipe et outil pour les petites équipes d'ingénieurs logiciels).