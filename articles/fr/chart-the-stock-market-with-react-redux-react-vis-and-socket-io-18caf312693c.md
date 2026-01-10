---
title: Comment j'ai construit une application qui suit le marché boursier pour un
  défi freeCodeCamp.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-13T07:27:45.000Z'
originalURL: https://freecodecamp.org/news/chart-the-stock-market-with-react-redux-react-vis-and-socket-io-18caf312693c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ztwOJDHFao9iHsFv.
tags:
- name: Data Science
  slug: data-science
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit une application qui suit le marché boursier pour
  un défi freeCodeCamp.
seo_desc: 'By Daniel Deutsch

  I was working on an app from the FreeCodeCamp curriculum, and thought others might
  find it interesting. In this article, you can read the full documentation for the
  building process. Enjoy!


  “Failure isn’t a necessary evil. In fact,...'
---

Par Daniel Deutsch

Je travaillais sur une application du [programme FreeCodeCamp](https://www.freecodecamp.org/challenges/chart-the-stock-market), et j'ai pensé que cela pourrait intéresser les autres. Dans cet article, vous pouvez lire la documentation complète du processus de construction. Bonne lecture !

> _« L'échec n'est pas un mal nécessaire. En fait, ce n'est pas un mal du tout. C'est une conséquence nécessaire de faire quelque chose de nouveau. »_

> _— Ed Catmull_

### Le défi

Pour ce défi particulier, je devais construire une application qui permettrait de surveiller diverses actions. Vous pouvez en savoir plus sur le défi complet [ici](https://www.freecodecamp.org/challenges/chart-the-stock-market). Maintenant, commençons.

Les histoires utilisateur sont assez simples :

* Je peux voir un graphique affichant les tendances récentes pour chaque action ajoutée.
* Je peux ajouter de nouvelles actions par leur symbole.
* Je peux supprimer des actions.
* Je peux voir les changements en temps réel lorsque d'autres utilisateurs ajoutent ou suppriment une action. Pour cela, vous devrez utiliser WebSockets.

Cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hlgmfwpKNkFmt6VTaFor3A.gif)
_Suivi du marché boursier en temps réel avec websockets_

### Feuille de route

Lorsque j'ai créé [ma dernière application full-stack](https://github.com/DDCreationStudios/Writing/blob/master/articles/LearningsFirstFullStack.md), j'ai appris que commencer par le back-end peut causer des problèmes lorsque vous travaillez sur le front-end plus tard. Cette fois, j'ai décidé de commencer par le front-end et de terminer par le back-end.

Voici la feuille de route que j'ai utilisée :

1. Configurer l'environnement avec create-react-app
2. Structurer les composants React de base
3. Configurer l'écosystème Redux
4. Travailler sur tous les composants, les diviser en composants conteneurs et les connecter au store Redux
5. Construire le composant Chart avec React-Vis
6. Construire le back-end en utilisant socket.io
7. Adapter le front-end aux WebSockets
8. Déployer sur Heroku

### Front end

Je vais mettre en avant les pierres angulaires clés — ce n'est pas un tutoriel pas à pas.

#### Configuration avec le package create-react-app

Pour ce projet, je voulais utiliser [ce modèle](https://github.com/facebookincubator/create-react-app) car je l'ai utilisé plusieurs fois auparavant mais jamais sur un projet full-stack. Bien qu'il ait certaines limitations avec la structure préconfigurée, les avantages l'emportent largement sur les problèmes.

En gros, il fournit un environnement qui :

* Supporte React, JSX, ES6 et la syntaxe Flow.
* Fournit des extras linguistiques au-delà de ES6 comme l'opérateur de propagation d'objet.
* Dispose d'un serveur de développement qui recherche les erreurs courantes.
* Importe les fichiers CSS et image directement depuis JavaScript.
* Dispose de CSS autopréfixé, donc vous n'avez pas besoin de -webkit ou d'autres préfixes.
* Dispose d'un script de construction pour regrouper JS, CSS et images pour la production, avec des sourcemaps.
* Vous donne un service worker offline-first et un manifest de web app, répondant à tous les critères des Progressive Web App.

Très tôt, j'ai dû éjecter la configuration ( = ouvrir la configuration de l'environnement pour les modifications) afin de modifier la configuration WebPack.

Le problème était que je voulais ajouter jQuery pour Materializecss — et il y avait toujours des problèmes.

Voici quelques solutions :

* Importer jquery en ES6 : [ici](https://stackoverflow.com/questions/37213647/es6-code-not-working-with-jquery).
* Fournir le plugin jquery dans la configuration WebPack : [ici](https://github.com/erikras/react-redux-universal-hot-example/issues/596).

#### React, Redux, React-vis

Cette fois, je voulais utiliser [react-vis](https://github.com/uber/react-vis) pour visualiser le graphique. Il s'agit d'une bibliothèque de visualisation basée sur D3 et développée par Uber. Pour résumer et citer leur documentation :

> _Une collection de composants react pour rendre des graphiques de visualisation de données courants, tels que des graphiques en ligne/aire/barres, des cartes thermiques, des nuées de points, des tracés de contours, des graphiques en secteurs et en anneaux, des sunbursts, des graphiques radar, des coordonnées parallèles et des cartes en arbre._

Quelques fonctionnalités notables :

* **Simplicité**. react-vis ne nécessite aucune connaissance approfondie des bibliothèques de visualisation de données avant de commencer à construire vos premières visualisations.
* **Flexibilité**. react-vis fournit un ensemble de blocs de construction de base pour différents graphiques. Par exemple, il a des composants d'axe X et Y séparés. Cela offre un haut niveau de contrôle de la disposition du graphique pour les applications qui en ont besoin.
* **Facilité d'utilisation**. La bibliothèque fournit un ensemble de valeurs par défaut qui peuvent être remplacées par les paramètres personnalisés de l'utilisateur.
* **Intégration avec React**. react-vis supporte le cycle de vie de React et ne crée pas de nœuds inutiles.

Quelques problèmes pratiques que j'ai rencontrés et résolus étaient :

* Rendre le graphique react-vis réactif, comme [ceci](https://github.com/uber/react-vis/issues/262)
* Pour utiliser correctement les dégradés dans react-vis, assurez-vous de les inclure dans le Plot et adaptez les points de référence. Voir [ceci](https://uber.github.io/react-vis/#/documentation/general-principles/colors).
* Utilisez LineSeries au lieu de LineMarkSeries pour de meilleures performances (voir [ce même lien](http://uber.github.io/react-vis/#/documentation/series-reference/line-series))

À ce stade, l'application était déjà assez belle. Maintenant, je devais vérifier la dernière histoire utilisateur, qui affiche les changements en temps réel en utilisant un back-end de "web socket".

### Back end

Pour les données, j'ai utilisé l'API ouverte de [Quandl](https://www.quandl.com/).

Serveur : index.js :

#### Configuration de la base de données (MongoDB hébergée avec mLab)

Il suffit de configurer le compte mLab et de créer une collection pour la nouvelle application. Créez un modèle mongoose pour simplifier les interactions avec la base de données, comme celui-ci :

```
const mongoose = require('mongoose');
```

```
var Schema = mongoose.Schema;
```

```
var stockSchema = new Schema({  stockName: String});
```

```
module.exports = mongoose.model('stockModel', stockSchema);
```

Ensuite, connectez le serveur express à mLab.

Pour résoudre l'avertissement concernant la connexion ouverte mongoose dépréciée, utilisez openURI.

Pour plus d'informations, voir [ici](http://mongoosejs.com/docs/connections.html).

#### Routes

Configurez une route de sorte que, par défaut, le fichier index.html de construction de production soit consommé. Configurez une autre route pour vérifier le contenu de la base de données et le retourner dans la réponse.

#### Ajout de Websocket

Utilisez la documentation Socket pour configurer des écouteurs pour :

* Afficher la connexion
* Afficher une déconnexion
* Sauvegarder les données dans la base de données
* Supprimer les données de la base de données

Assurez-vous d'intégrer la fonction d'écouteur avec le modèle mongoose pour exploiter la puissance de MongoDB.

En passant — parce que j'ai littéralement passé une semaine sur ce problème :

Utilisez `socket.BROADCAST.emit` pour envoyer le message à TOUS les sockets !

Voir plus [ici](https://stackoverflow.com/questions/9837998/socket-io-client-not-receiving-messages-from-server).

### Adapter le front-end au WebSocket

Le "problème" que vous devez surmonter ici est de rendre les composants en fonction des actions émises par le socket.

Pour ces configurations, il est essentiel de gérer le problème dans le composant lui-même et dans les ducks (fichiers Redux).

Je l'ai résolu en connectant le composant conteneur avec un client socket.io et en écoutant les changements. J'ai fait cela avec le cycle de vie `componentDidMount`. Chaque fois qu'un message est émis par le socket, le composant consulte la base de données en dispatchant des actions vers les fichiers Redux.

Dans les fichiers Redux, j'ai récupéré les données de la base de données et je les ai comparées avec le store actuel de l'application. En fonction de cette comparaison, l'application récupère toutes les données à nouveau depuis le service Quandl. De cette façon, chaque nouveau client socket peut vérifier par lui-même et a toujours les données les plus à jour.

Veuillez noter : Je ne suis pas sûr que ce soit la meilleure pratique pour une application Redux/react, puisque je gère beaucoup de logique dans l'action asynchrone. N'hésitez pas à signaler les erreurs ou les concepts mal compris ! :)

#### Actions asynchrones dans ducks/stocks.js (extrait) :

```
// Actions asynchrones avec thunk
export function checkDB(stocks) {
  return dispatch =>
    axios
      .get('/api/stocks')
      .then(res => {
        if (stocks.length === 0) {
          res.data.map(elem => {
            dispatch(fetchStock(elem.stockName));
          });
        } else if (res.data.length < stocks.length) {
          dispatch(removeStock(stocks.length - 1));
        } else {
          let diff = [];
          res.data.map((item, i) => {
            if (i < stocks.length) {
              if (res.data[i].stockName !== stocks[i].dataset.dataset_code) {
                diff.push({
                  stockName: item.stockName
                });
              }
            } else if (i === stocks.length) {
              diff.push({
                stockName: item.stockName
              });
            } else {
              diff = [];
            }
          });

          diff.map(elem => {
            dispatch(fetchStock(elem.stockName));
          });
          diff = [];
          // console.log(res);
        }
      })
      .catch(err => {
        console.warn(err);
      });
}
```

```
export function fetchStock(stockCode) {
  return dispatch =>
    axios
      .get(
        `https://www.quandl.com/api/v3/datasets/WIKI/${stockCode}.json?api_key=${process
          .env.REACT_APP_QUANDL_KEY}`
      )
      .then(res => {
        dispatch(addStock(res.data));
        // console.log(res.data);
      })
      .catch(err => {
        console.error(err);
        toastr['warning'](' ', 'Le code de l\'action est introuvable !');
      });
}
```

```
export function newStock(stockCode, socket) {
  socket.emit('update', stockCode);
  return dispatch =>
    axios
      .get(
        `https://www.quandl.com/api/v3/datasets/WIKI/${stockCode}.json?api_key=${process
          .env.REACT_APP_QUANDL_KEY}`
      )
      .then(res => {
        dispatch(addStock(res.data));
        // console.log(res.data);
      })
      .then(socket.emit('addStock', stockCode))
      .catch(err => {
        console.error(err);
        toastr['warning'](' ', 'Le code de l\'action est introuvable !');
      });
}
```

```
export function deleteStock(ind, stockCode) {
  const socket = socketIOClient('https://createdd-stockmarketchart.herokuapp.com/');
  socket.emit('removeStock', stockCode);
  return dispatch => {
    dispatch(removeStock(ind));
    console.log(`Supprimé ${stockCode}`);
  };
}
```

#### Conteneur pliable — CollapsibleCon.js

### Déployer sur Heroku

Pour le déploiement sur Heroku, il est important :

* d'utiliser le buildpack create-react-app lorsque vous utilisez le serveur webpack
* d'utiliser le buildpack nodeJs lorsque vous utilisez votre propre websocket avec votre serveur express
* de définir les variables d'environnement

### Voir le résultat

* **Voir l'application en direct [ici](https://createdd-stockmarketchart.herokuapp.com/).**
* **Voir le code open source [ici.](https://github.com/DDCreationStudios/ChartTheStockMarket)**
* **Voir le timelapse de 5 min [ici.](https://www.youtube.com/watch?v=iPnyrrWJpLU)**
* **Voir la session de codage relaxante de 1 heure [ici.](https://www.youtube.com/watch?v=8d6829bIxYg)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*hlgmfwpKNkFmt6VTaFor3A.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/0*mmxgFfkpPzjEdnuS.png)
_Voir tout le processus de construction sur Youtube_

Merci d'avoir lu mon article ! Si vous l'avez apprécié, veuillez m'applaudir pour que plus de gens le voient. Et n'hésitez pas à laisser des commentaires.