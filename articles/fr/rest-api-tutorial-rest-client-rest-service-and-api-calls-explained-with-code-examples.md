---
title: Tutoriel API REST – Client REST, Service REST et Appels API Expliqués avec
  des Exemples de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-22T19:05:27.000Z'
originalURL: https://freecodecamp.org/news/rest-api-tutorial-rest-client-rest-service-and-api-calls-explained-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b84740569d1a4ca2c3f.jpg
tags:
- name: api
  slug: api
- name: Express JS
  slug: express-js
- name: JavaScript
  slug: javascript
- name: REST
  slug: rest
- name: REST API
  slug: rest-api
seo_title: Tutoriel API REST – Client REST, Service REST et Appels API Expliqués avec
  des Exemples de Code
seo_desc: 'By Vaibhav Kandwal

  Ever wondered how login/signup on a website works on the back-end? Or how when you
  search for "cute kitties" on YouTube, you get a bunch of results and are able to
  stream off of a remote machine?

  In this beginner friendly guide, I ...'
---

Par Vaibhav Kandwal

Vous êtes-vous déjà demandé comment fonctionne la connexion/inscription sur un site web en back-end ? Ou comment, lorsque vous recherchez "cute kitties" sur YouTube, vous obtenez une série de résultats et pouvez diffuser depuis une machine distante ?

Dans ce guide pour débutants, je vais vous guider à travers le processus de configuration d'une API RESTful. Nous allons démystifier certains termes techniques et voir comment coder un serveur en NodeJS. Plongeons un peu plus profondément dans JavaScript !

## Éloignons ce jargon

Alors, qu'est-ce que REST ? Selon Wikipedia :

> **Representational state transfer** (**REST**) est un style d'architecture logicielle qui définit un ensemble de contraintes à utiliser pour créer des services Web. Les services Web RESTful permettent aux systèmes de demande d'accéder et de manipuler des représentations textuelles des ressources Web en utilisant un ensemble uniforme et prédéfini d'opérations sans état.

Démystifions ce que cela signifie (espérons que vous avez compris la forme complète). REST est essentiellement un ensemble de règles pour la communication entre un client et un serveur. Il y a quelques contraintes sur la définition de REST :

1. **Architecture Client-Serveur** : l'interface utilisateur du site web/app doit être séparée de la demande de données/stockage, afin que chaque partie puisse être mise à l'échelle individuellement.
2. **Sans état** : la communication ne doit avoir aucun contexte client stocké sur le serveur. Cela signifie que chaque demande au serveur doit être faite avec toutes les données requises et aucune hypothèse ne doit être faite si le serveur a des données des demandes précédentes.
3. **Système en couches** : le client ne doit pas pouvoir dire s'il communique directement avec le serveur ou un intermédiaire. Ces serveurs intermédiaires (qu'il s'agisse de proxy ou d'équilibreurs de charge) permettent la scalabilité et la sécurité du serveur sous-jacent.

D'accord, maintenant que vous savez ce que sont les services RESTful, voici quelques termes utilisés dans le titre :

1. **Client REST** : code ou une application qui peut accéder à ces services REST. Vous en utilisez un maintenant ! Oui, le navigateur peut agir comme un client REST non contrôlé (le site web gère les demandes du navigateur). Le navigateur, pendant longtemps, a utilisé une fonction intégrée appelée XMLHttpRequest pour toutes les demandes REST. Mais cela a été remplacé par [FetchAPI](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), une approche moderne basée sur les [promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) pour les demandes. D'autres exemples sont les bibliothèques de code comme [axios](https://github.com/axios/axios), [superagent](https://github.com/visionmedia/superagent) et [got](https://github.com/sindresorhus/got) ou certaines applications dédiées comme [Postman](https://www.postman.com/) (ou une version en ligne, [postwoman](https://postwoman.io/) !), ou un outil en ligne de commande comme [cURL](https://curl.haxx.se/) !.
2. **Service REST** : le serveur. Il existe de nombreuses bibliothèques populaires qui facilitent la création de ces serveurs, comme [ExpressJS](https://expressjs.com/) pour NodeJS et [Django](https://www.djangoproject.com/) pour Python.
3. **API REST** : cela définit le point de terminaison et les méthodes autorisées pour accéder/soumettre des données au serveur. Nous en parlerons en détail ci-dessous. D'autres alternatives à cela sont : GraphQL, JSON-Pure et oData.

## Alors, dites-moi maintenant, à quoi ressemble REST ?

En termes très larges, vous demandez au serveur certaines données ou lui demandez d'enregistrer certaines données, et le serveur répond aux demandes.

En termes de programmation, il y a un point de terminaison (une URL) que le serveur attend pour recevoir une demande. Nous nous connectons à ce point de terminaison et envoyons certaines données nous concernant (rappelons que REST est sans état, aucune donnée sur la demande n'est stockée) et le serveur répond avec la réponse correcte.

Les mots sont ennuyeux, laissez-moi vous donner une démonstration. J'utiliserai Postman pour vous montrer la demande et la réponse :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-162.png)
_postman : configuration de la demande_

Les données retournées sont en JSON (JavaScript Object Notation) et peuvent être accessibles directement.

Ici, `https://official-joke-api.appspot.com/random_joke` est appelé un point de terminaison d'une API. Il y aura un serveur à l'écoute sur ce point de terminaison pour des demandes comme celle que nous avons faite.

## Anatomie de REST :

D'accord, maintenant nous savons que les données peuvent être demandées par le client et que le serveur répondra de manière appropriée. Regardons plus en détail comment une demande est formée.

1. **Point de terminaison** : Je vous ai déjà parlé de cela. Pour un rappel, c'est l'URL où le serveur REST est à l'écoute.
2. **Méthode** : Plus tôt, j'ai écrit que vous pouvez soit demander des données, soit les modifier, mais comment le serveur saura-t-il quel type d'opération le client veut effectuer ? REST implémente plusieurs 'méthodes' pour différents types de demande, les suivantes sont les plus populaires :  
- **GET** : Obtenir une ressource du serveur.  
- **POST** : Créer une ressource sur le serveur.  
- **PATCH** ou **PUT** : Mettre à jour une ressource existante sur le serveur.  
- **DELETE** : Supprimer une ressource existante du serveur.  

3. **En-têtes** : Les détails supplémentaires fournis pour la communication entre le client et le serveur (rappelons que REST est sans état). Certains des en-têtes courants sont :  
**Demande** :  
- _host_ : l'IP du client (ou d'où la demande a été émise)  
- _accept-language_ : la langue compréhensible par le client  
- _user-agent_ : les données sur le client, le système d'exploitation et le fournisseur  
**Réponse** :  
- _status_ : le statut de la demande ou le code HTTP.  
- _content-type_ : le type de ressource envoyé par le serveur.  
- _set-cookie_ : définit les cookies par le serveur
4. **Données** : (également appelé corps ou message) contient les informations que vous souhaitez envoyer au serveur.

## Assez de détails – montrez-moi le code.

Commençons à coder un service REST en Node. Nous allons implémenter toutes les choses que nous avons apprises ci-dessus. Nous allons également utiliser ES6+ pour écrire notre service.

Assurez-vous d'avoir Node.JS installé et que `node` et `npm` sont disponibles dans votre chemin. J'utiliserai Node 12.16.2 et NPM 6.14.4.

Créez un répertoire `rest-service-node` et accédez-y :

```shell
mkdir rest-service-node
cd rest-service-node
```

Initialisez le projet node :

```shell
npm init -y
```

Le drapeau `-y` saute toutes les questions. Si vous souhaitez remplir le questionnaire complet, exécutez simplement `npm init`.

Installons quelques packages. Nous utiliserons le framework ExpressJS pour développer le serveur REST. Exécutez la commande suivante pour l'installer :

```shell
npm install --save express body-parser
```

À quoi sert `body-parser` ? Express, par défaut, est incapable de gérer les données envoyées via une demande POST en tant que JSON. `body-parser` permet à Express de surmonter cela.

Créez un fichier appelé `server.js` et ajoutez le code suivant :

```js
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json());

app.listen(5000, () => {
  console.log(`Le serveur est en cours d'exécution sur le port 5000.`);
});

```

Les deux premières lignes importent Express et body-parser. 

La troisième ligne initialise le serveur Express et le définit dans une variable appelée `app`. 

La ligne `app.use(bodyParser.json());` initialise le plugin body-parser.

Enfin, nous définissons notre serveur pour écouter sur le port `5000` pour les demandes.

### Obtenir des données du serveur REST :

Pour obtenir des données d'un serveur, nous avons besoin d'une demande `GET`. Ajoutez le code suivant avant `app.listen` :

```js
const sayHi = (req, res) => {
  res.send("Salut !");
};

app.get("/", sayHi);
```

Nous avons créé une fonction `sayHi` qui prend deux paramètres `req` et `res` (je vais expliquer plus tard) et envoie un 'Salut !' en réponse. 

`app.get()` prend deux paramètres, le chemin de la route et la fonction à appeler lorsque le chemin est demandé par le client. Donc, la dernière ligne se traduit par : Hé serveur, écoute les demandes sur '/' (pensez à la page d'accueil) et appelle la fonction `sayHi` si une demande est faite.

`app.get` nous donne également un objet `request` contenant toutes les données envoyées par le client et un objet `response` qui contient toutes les méthodes avec lesquelles nous pouvons répondre au client. Bien que ceux-ci soient accessibles en tant que paramètres de fonction, la convention de nommage générale suggère que nous les nommions `res` pour `response` et `req` pour `request`.

Assez de bavardages. Allumons le serveur ! Exécutez le serveur suivant :

```shell
node server.js
```

Si tout se passe bien, vous devriez voir un message sur la console disant : _Le serveur est en cours d'exécution sur le port 5000._

_Note : Vous pouvez changer le port pour n'importe quel numéro que vous voulez._

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-160.png)

Ouvrez votre navigateur et naviguez vers `http://localhost:5000/` et vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-161.png)

Voilà ! Votre première demande `GET` a réussi !

### Envoyer des données au serveur REST :

Comme nous l'avons discuté précédemment, configurons comment nous pouvons implémenter une demande `POST` dans notre serveur. Nous allons envoyer deux nombres et le serveur retournera la somme des nombres. Ajoutez cette nouvelle méthode sous le `app.get` :

```js
app.post("/add", (req, res) => {
  const { a, b } = req.body;
  res.send(`La somme est : ${a + b}`);
});
```

Ici, nous allons envoyer les données au format JSON, comme ceci :

```json
{
    "a":5,
    "b":10
}
```

Passons en revue le code :

À la ligne 1, nous invoquons la méthode `.post()` de ExpressJS, qui permet au serveur d'écouter les demandes `POST`. Cette fonction prend les mêmes paramètres que la méthode `.get()`. La route que nous passons est `/add`, donc on peut accéder au point de terminaison comme `http://votre-adresse-ip:port/add` ou dans notre cas `localhost:5000/add`. Nous intégrons notre fonction au lieu d'écrire une fonction ailleurs. 

À la ligne 2, nous avons utilisé un peu de syntaxe ES6, à savoir, la déstructuration d'objet. Toutes les données que nous envoyons via la demande sont stockées et disponibles dans le `body` de l'objet `req`. Donc, essentiellement, nous aurions pu remplacer la ligne 2 par quelque chose comme :

```js
const num1 = req.body.a;
const num2 = req.body.b;
```

À la ligne 3, nous utilisons la fonction `send()` de l'objet `res` pour envoyer le résultat de la somme. Encore une fois, nous utilisons les littéraux de gabarit de ES6. Maintenant, pour le tester (en utilisant Postman) :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-163.png)

Nous avons donc envoyé les données 5 et 10 en tant que `a` et `b` en les utilisant comme corps. Postman attache ces données à la demande et les envoie. Lorsque le serveur reçoit la demande, il peut analyser les données de `req.body`, comme nous l'avons fait dans le code ci-dessus. Le résultat est montré ci-dessous.

D'accord, le code final :

```js
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json());

const sayHi = (req, res) => {
  res.send("Salut !");
};

app.get("/", sayHi);

app.post("/add", (req, res) => {
  const { a, b } = req.body;
  res.send(`La somme est : ${a + b}`);
});

app.listen(5000, () => {
  console.log(`Le serveur est en cours d'exécution sur le port 5000.`);
});

```

## Client REST :

D'accord, nous avons créé un serveur, mais comment y accéder depuis notre site web ou notre application web ? C'est là que les bibliothèques de clients REST seront utiles. 

Nous allons créer une page web qui contiendra un formulaire, où vous pourrez entrer deux nombres et nous afficherons le résultat. Commençons.

Tout d'abord, modifions un peu le `server.js` :

```js
const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/add", (req, res) => {
  const { a, b } = req.body;
  res.send({
    result: parseInt(a) + parseInt(b)
  });
});

app.listen(5000, () => {
  console.log(`Le serveur est en cours d'exécution sur le port 5000.`);
});

```

Nous avons importé un nouveau package `path`, qui est fourni par Node, pour manipuler les chemins de manière multiplateforme. Ensuite, nous avons modifié la demande `GET` sur '/' et utilisé une autre fonction disponible dans `res`, c'est-à-dire `sendFile`, qui nous permet d'envoyer n'importe quel type de fichier en tant que réponse. Donc, chaque fois qu'une personne essaie de naviguer vers '/', elle obtiendra notre page `index.html`.

Enfin, nous avons modifié notre fonction `app.post` pour retourner la somme en tant que JSON et convertir à la fois `a` et `b` en entiers.

Créons une page html, je l'appellerai `index.html`, avec un peu de style de base :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Client REST</title>
  </head>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    .container {
      height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    form {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
    }
    label,
    input[type="submit"] {
      margin-top: 20px;
    }
  </style>
  <body>
    <div class="container">
      <h1>Formulaire POST Simple</h1>
      </h1>
      <form>
        <label>Nombre 1 :</label>
        <input id="num1" type="number" />
        <label>Nombre 2 :</label>
        <input id="num2" type="number" />
        <input type="submit" value="Add"/>
      </form>
      <div class="result">Cliquez sur Add !</div>
    </div>
  </body>
</html>
```

Ajoutons une balise `script` juste avant la balise de fermeture du body, afin de ne pas avoir à maintenir un fichier `.js`. Nous commencerons par écouter l'événement `submit` et appellerons une fonction en conséquence :

```js
<script>
	document.addEventListener("submit", sendData);
</script>
```

Tout d'abord, nous devons empêcher le rafraîchissement de la page lorsque le bouton 'Add' est cliqué. Cela peut être fait en utilisant la fonction `preventDefault()`. Ensuite, nous obtiendrons la valeur des entrées à cet instant :

```js
function sendData(e) {
    e.preventDefault();
    const a = document.querySelector("#num1").value;
    const b = document.querySelector("#num2").value;
}
```

Maintenant, nous allons faire l'appel au serveur avec ces deux valeurs `a` et `b`. Nous allons utiliser [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), intégré à chaque navigateur pour cela. 

Fetch prend deux entrées, l'URL du point de terminaison et un objet de demande JSON et retourne une [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). Les expliquer ici serait hors sujet, donc je vais vous laisser cela.

Continuez à l'intérieur de la fonction `sendData()` :

```js
fetch("/add", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            a: parseInt(a),
            b: parseInt(b)
        })
    })
    .then(res => res.json())
    .then(data => {
        const {
            result
        } = data;
        document.querySelector(
            ".result"
        ).innerText = `La somme est : ${result}`;
    })
    .catch(err => console.log(err));
```

Tout d'abord, nous passons l'URL relative du point de terminaison en tant que premier paramètre à `fetch`. Ensuite, nous passons un objet qui contient la méthode que nous voulons que Fetch utilise pour la demande, qui est `POST` dans ce cas.

Nous passons également `headers`, qui fourniront des informations sur le type de données que nous envoyons (`content-type`) et le type de données que nous acceptons en réponse (`accept`).

Ensuite, nous passons `body`. Vous vous souvenez que nous avons tapé les données en tant que JSON lors de l'utilisation de Postman ? Nous faisons une sorte de chose similaire ici. Puisque express traite les chaînes comme entrée et les traite selon le type de contenu fourni, nous devons convertir notre charge utile JSON en chaîne. Nous faisons cela avec `JSON.stringify()`. Nous sommes un peu extra prudents et analysons l'entrée en entiers, afin qu'elle ne perturbe pas notre serveur (puisque nous n'avons pas implémenté de vérification de type de données).

Enfin, si la promesse (retournée par fetch) est résolue, nous obtiendrons cette réponse et la convertirons en JSON. Après cela, nous obtiendrons le résultat de la clé `data` retournée par la réponse. Ensuite, nous affichons simplement le résultat à l'écran.

À la fin, si la promesse est rejetée, nous afficherons le message d'erreur sur la console.

Voici le code final pour `index.html` :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Client REST</title>
  </head>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    .container {
      height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    form {
      display: flex;
      flex-direction: column;
      margin-bottom: 20px;
    }
    label,
    input[type="submit"] {
      margin-top: 20px;
    }
  </style>
  <body>
    <div class="container">
      <h1>Formulaire POST Simple</h1>
      </h1>
      <form>
        <label>Nombre 1 :</label>
        <input id="num1" type="number" />
        <label>Nombre 2 :</label>
        <input id="num2" type="number" />
        <input type="submit" value="Add"/>
      </form>
      <div class="result">Cliquez sur Add !</div>
    </div>
    <script>
      document.addEventListener("submit", sendData);
      function sendData(e) {
        e.preventDefault();
        const a = document.querySelector("#num1").value;
        const b = document.querySelector("#num2").value;

        fetch("/add", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            a: parseInt(a),
            b: parseInt(b)
          })
        })
          .then(res => res.json())
          .then(data => {
            const { result } = data;
            document.querySelector(
              ".result"
            ).innerText = `La somme est : ${result}`;
          })
          .catch(err => console.log(err));
      }
    </script>
  </body>
</html>

```

J'ai créé une [petite application sur glitch](https://habitual-serious-boater.glitch.me/) pour que vous puissiez tester.

## Conclusion :

Dans cet article, nous avons appris l'architecture REST et l'anatomie des demandes REST. Nous avons travaillé en créant un simple serveur REST qui sert les demandes `GET` et `POST` et avons construit une simple page web qui utilise un client REST pour afficher la somme de deux nombres. 

Vous pouvez étendre cela pour les types de demandes restants et même implémenter une application back-end CRUD complète [back-end CRUD app](https://www.freecodecamp.org/news/building-a-simple-crud-application-with-express-and-mongodb-63f80f3eb1cd/). 

J'espère que vous avez appris quelque chose de cela. Si vous avez des questions, n'hésitez pas à me contacter sur Twitter ! Bon codage !