---
title: Comment créer une application en temps réel avec Socket.io, React, Node et
  MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T21:43:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-realtime-app-using-socket-io-react-node-mongodb-a10c4a1ab676
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j_kShofJmfZ_-bEpt1IS8Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer une application en temps réel avec Socket.io, React, Node
  et MongoDB
seo_desc: 'By Honey Thakuria

  Ever wondered how real time apps are built? Ever noticed the importance and use
  cases of real time applications?

  If you are curious about the above questions and need an answer, then this blog
  post is for you.

  First, let’s identify ...'
---

Par Honey Thakuria

Vous êtes-vous déjà demandé comment les applications en temps réel sont construites ? Avez-vous déjà remarqué l'importance et les cas d'utilisation des applications en temps réel ?

Si vous êtes curieux à propos des questions ci-dessus et avez besoin d'une réponse, alors cet article de blog est pour vous.

Tout d'abord, identifions quelques cas d'utilisation nécessitant des applications en temps réel :

1. Obtenir des mises à jour de localisation pour votre taxi sur une carte d'une application de réservation de taxi.
2. Recevoir de nouveaux messages instantanément sur votre application de chat préférée.
3. Mise à jour des informations de commande de nourriture à la cuisine de votre restaurant préféré.

Ce sont tous des scénarios courants de notre vie quotidienne où nous ne pouvons pas tolérer de retard dans la mise à jour des informations et avons donc besoin d'une communication en temps réel.

Les **technologies** qui peuvent être utilisées pour la **communication en temps réel** sont :

1. **Short Polling** : AJAX, crée un trafic important.
2. **Long Polling** : Comme AJAX, mais le serveur conserve la réponse jusqu'à ce qu'il ait une mise à jour. Après l'avoir reçue, le client envoie une autre requête, et a besoin d'un en-tête supplémentaire pour être traversé dans les deux sens, causant un surcoût supplémentaire.
3. **Web Sockets** : permettent d'ouvrir une communication interactive entre le client et le serveur. On peut envoyer une requête au serveur et recevoir des réponses pilotées par événements sans interroger le serveur pour une réponse, faisant des web sockets un **meilleur choix** pour notre cas d'utilisation.

Plus d'informations approfondies sur les trois technologies ci-dessus peuvent être lues [ici](https://stackoverflow.com/questions/12555043/my-understanding-of-http-polling-long-polling-http-streaming-and-websockets).

Nous allons apprendre à créer une application en temps réel en couvrant le scénario suivant.

Imaginez que vous êtes assis dans votre restaurant préféré et que vous avez un menu numérique. Vous passez la commande et la cuisine est mise à jour en temps réel concernant votre commande. Lorsque la cuisine a terminé la commande, ils la mettent à jour en temps réel également.

Fonctionnalités en détail :

1. **Passer une commande** : Interface pour sélectionner la quantité et passer la commande pour un article alimentaire sélectionné à la cuisine.
2. **Cuisine** : Interface qui peut être ouverte dans plusieurs cuisines et met à jour en temps réel les chefs et cuisiniers concernant le nombre total de commandes créées et la quantité prévue d'articles alimentaires, leur donnant la flexibilité de la mettre à jour. Dispose également d'une fonctionnalité pour télécharger le rapport sous forme de feuille Excel.
3. **Changer la quantité prévue** : Interface pour mettre à jour la quantité prévue d'articles alimentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/6EyW3Wo0cKhjTFMskVgaWeTAaVS-3m26bhzL)

Une **démo en direct** de ce scénario peut être trouvée [ici](https://faasos-honey.herokuapp.com/).

Pour une meilleure compréhension, ouvrez-la dans différents onglets/appareils en même temps pour voir les données changer en temps réel.

Le **code source** est [ici](https://github.com/honey93/OrderKitchen). N'hésitez pas à créer quelque chose d'innovant/utile sur cette base.

Alors commençons.

### Pile technologique :

**Frontend** : React.js, Reactstrap, Socket.io

**Backend** : Node.js (Express), MongoDB, Socket.io

### Structure des dossiers :

```
/*
Allez dans le répertoire racine dans le code source et trouvez les fichiers mentionnés ci-dessous. Cette architecture aide à créer une grande application modulaire.
*/
backend-my-app/ /* Code backend de l'application */
 server.js       /* Le code Socket et backend réside ici*/
 build/      /* Optionnel pour le déploiement du Build Frontend */ 
 package.json /* Dépendance Backend */
 ...
public/
src/  /*      Code source Frontend      */
 global/      /*   Composants utilisés partout   */
  header.css
  header.js     
 main/           
  Kitchen.js
  PlaceOrder.js
  UpdatePredicted.js
 App.js   /* Partie logique de routage et assemblage des composants */
package.json /* Dépendance Frontend */ 
 ............
```

### Explication du code source :

#### Frontend :

```
git clone https://github.com/honey93/OrderKitchen.git
cd OrderKitchen
npm install
npm start
```

Paquets utilisés :

1. [Reactstrap](https://reactstrap.github.io/) : Composants bootstrap4 faciles à utiliser
2. [Socket.io](https://socket.io/docs/) : Socket.io est une bibliothèque qui permet une communication en temps réel, bidirectionnelle et basée sur des événements entre le navigateur et le serveur.
3. [react-html-table-to-excel](https://www.npmjs.com/package/react-html-table-to-excel) : Fournit une génération côté client de fichiers Excel (.xls) à partir d'un élément de tableau HTML.
4. [react-router-dom](https://www.npmjs.com/package/react-router-dom) : Liaisons DOM pour le routeur react. Il se compose de nombreux composants importants comme BrowserRouter utilisé lorsqu'il y a un serveur pour gérer les requêtes dynamiques, Switch, Route, etc.

#### **Composant App**

**Chemin** : src/App.js

Ce composant contient la logique de routage principale du Frontend. Ce fichier est utilisé dans src/index.js à l'intérieur du module Browser Router. Le code ci-dessous démontre une des approches pour garder votre application modulaire.

```javascript
import React, { Component } from "react";
import "./App.css";
import { Header } from "./global/header";
import { Switch, Route } from "react-router-dom";
import PlaceOrder from "./main/PlaceOrder";
import UpdatePredicted from "./main/UpdatePredicted";
import Kitchen from "./main/Kitchen";
/*Le composant <Route> est la partie principale de React Router. Partout où vous voulez rendre du contenu basé sur le pathname de l'emplacement, vous devriez utiliser un élément <Route>. */
/* Le composant Route attend une prop path, qui est une chaîne décrivant le pathname que la route correspond */
/* Le <Switch> va itérer sur les routes et ne rendre que la première qui correspond au pathname actuel */
class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={PlaceOrder} />
          <Route path="/updatepredicted" component={UpdatePredicted} />
          <Route path="/kitchen" component={Kitchen} />
        </Switch>
      </div>
    );
  }
}
export default App;
```

#### **Composant Header**

**Chemin** : src/global/header.js

Ce composant sera commun et utilisé dans les sections comme Passer une commande, Changer la quantité prévue, Cuisine. Cette approche aide à éviter la duplication de code et garde l'application modulaire.

```js
import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import socketIOClient from "socket.io-client";
import "./header.css";
// Le Header crée des liens qui peuvent être utilisés pour naviguer
// entre les routes.
var socket;
class Header extends Component {
/* Création d'un client Socket et exportation à la fin pour être utilisé dans les composants Place Order, Kitchen, etc */
  constructor() {
    super();
    this.state = {
      endpoint: 'http://localhost:3001/'
    };
socket = socketIOClient(this.state.endpoint);
  }
render() {
    return (
      <header>
        <nav>
          <ul className="NavClass">
            <li>
              <NavLink exact to="/">
                Passer une commande
              </NavLink>
            </li>
            <li>
              <NavLink to="/updatepredicted">Changer la quantité prévue </NavLink>
            </li>
            <li>
              <NavLink to="/kitchen"> Cuisine </NavLink>
            </li  >
          </ul>
        </nav>
      </header>
    );
  }
}
export { Header, socket };
```

#### **Composant Kitchen**

**Chemin** : src/main/Kitchen.js

La logique UI et le code html de l'écran Cuisine résident dans ce composant :

```js
import React, { Component } from "react";
import { Button, Table, Container } from "reactstrap";
import { socket } from "../global/header";
import ReactHTMLTableToExcel from "react-html-table-to-excel";
class Kitchen extends Component {
  constructor() {
    super();
    this.state = {
      food_data: []
      // c'est ici que nous nous connectons avec les sockets,
    };
  }
getData = foodItems => {
    console.log(foodItems);
    this.setState({ food_data: foodItems });
  };
changeData = () => socket.emit("initial_data");
/*Dès que le composant est monté, c'est-à-dire dans la méthode componentDidMount, déclencher l'événement initial_data pour obtenir les données afin d'initialiser le tableau de bord de la cuisine */
/* Ajout d'un écouteur change_data pour écouter les changements effectués par les composants Place Order et Predicted Order */ 
componentDidMount() {
    var state_current = this;
    socket.emit("initial_data");
    socket.on("get_data", this.getData);
    socket.on("change_data", this.changeData);
  }

/* Suppression de l'écouteur avant de démonter le composant afin d'éviter l'ajout de plusieurs écouteurs au moment de la revisite*/
componentWillUnmount() {
    socket.off("get_data");
    socket.off("change_data");
  }
/* Lorsque Done est cliqué, cette fonction est appelée et l'événement mark_done est émis, qui est écouté sur le backend expliqué plus tard*/
markDone = id => {
    // console.log(predicted_details);
    socket.emit("mark_done", id);
  };
getFoodData() {
    return this.state.food_data.map(food => {
      return (
        <tr key={food._id}>
          <td> {food.name} </td>
          <td> {food.ordQty} </td>
          <td> {food.prodQty} </td>
          <td> {food.predQty} </td>
          <td>
            <button onClick={() => this.markDone(food._id)}>Terminé</button>
          </td>
        </tr>
      );
    });
  }
render() {
    return (
      <Container>
        <h2 className="h2Class">Zone de Cuisine</h2>
        <ReactHTMLTableToExcel
          id="test-table-xls-button"
          className="download-table-xls-button"
          table="table-to-xls"
          filename="tablexls"
          sheet="tablexls"
          buttonText="Télécharger en XLS"
        />
<Table striped id="table-to-xls">
          <thead>
            <tr>
              <th>Nom</th>
              <th>Quantité</th>
              <th>Créé jusqu'à présent</th>
              <th>Prévu</th>
              <th>Statut</th>
            </tr>
          </thead>
          <tbody>{this.getFoodData()}</tbody>
        </Table>
      </Container>
    );
  }
}
export default Kitchen;
```

#### **Composant Place Order**

**Chemin** : src/main/PlaceOrder.js

```js
import React, { Component } from "react";
import { Button, Table, Container } from "reactstrap";
import { socket } from "../global/header";
class PlaceOrder extends Component {
  constructor() {
    super();
    this.state = {
      food_data: []
      // c'est ici que nous nous connectons avec les sockets,
    };
  }
getData = foodItems => {
    console.log(foodItems);
    foodItems = foodItems.map(food => {
      food.order = 0;
return food;
    });
    this.setState({ food_data: foodItems });
  };
componentDidMount() {
    socket.emit("initial_data");
    var state_current = this;
    socket.on("get_data", state_current.getData);
  }
componentWillUnmount() {
    socket.off("get_data", this.getData);
  }
//Fonction pour passer la commande.
sendOrder = id => {
    var order_details;
    this.state.food_data.map(food => {
      if (food._id == id) {
        order_details = food;
      }
      return food;
    });
    console.log(order_details);
    socket.emit("putOrder", order_details);
    var new_array = this.state.food_data.map(food => {
      food.order = 0;
      return food;
    });
    this.setState({ food_data: new_array });
  };
// Changement de la quantité dans l'état qui est émis au backend au moment de passer la commande.
changeQuantity = (event, foodid) => {
    if (parseInt(event.target.value) < 0) {
      event.target.value = 0;
    }
    var new_array = this.state.food_data.map(food => {
      if (food._id == foodid) {
        food.order = parseInt(event.target.value);
      }
      return food;
    });
    this.setState({ food_data: new_array });
  };
// Pour obtenir les données initiales
getFoodData() {
    return this.state.food_data.map(food => {
      return (
        <tr key={food._id}>
          <td> {food.name} </td>
          <td>
            <input
              onChange={e => this.changeQuantity(e, food._id)}
              value={food.order}
              type="number"
              placeholder="Quantité"
            />
          </td>
          <td>
            <button onClick={() => this.sendOrder(food._id)}>Commander</button>
          </td>
        </tr>
      );
    });
  }
render() {
    return (
      <Container>
        <h2 className="h2Class">Menu de Commande</h2>
        <Table striped>
          <thead>
            <tr>
              <th>Produit</th>
              <th>Quantité</th>
              <th>Commande</th>
            </tr>
          </thead>
          <tbody>{this.getFoodData()}</tbody>
        </Table>
      </Container>
    );
  }
}
export default PlaceOrder;
```

Une autre section appelée Update Predicted Path: src/main/UpdatePredicted.js similaire à la section ci-dessus est présente dans le dépôt de code.

### Backend

Démarrage du Backend :

```
cd backend-my-app
npm install
node server.js
```

Paquets utilisés :

1. [**Monk**](https://www.npmjs.com/package/monk) : Une petite couche qui fournit des améliorations d'utilisabilité simples mais substantielles pour l'utilisation de MongoDB au sein de Node.JS.
2. [**Socket.io**](https://socket.io/docs/) : Socket.io est une bibliothèque qui permet une communication en temps réel, bidirectionnelle et basée sur des événements entre le navigateur et le serveur.

3. [**Express**](https://www.npmjs.com/package/express) : Framework web rapide et minimaliste pour [node](http://nodejs.org/).

#### **Code Principal**

**Chemin** : backend-my-app/server.js

```js
const express = require("express");
const http = require("http");
const socketIO = require("socket.io");
// Chaîne de connexion de la base de données MongoDb hébergée sur Mlab ou localement
var connection_string = "**********";
// Le nom de la collection doit être "FoodItems", une seule collection pour l'instant.
// Le format du document doit être tel que mentionné ci-dessous, au moins un tel document :
// {
//     "_id": {
//         "$oid": "5c0a1bdfe7179a6ca0844567"
//     },
//     "name": "Veg Roll",
//     "predQty": 100,
//     "prodQty": 295,
//     "ordQty": 1
// }
const db = require("monk")(connection_string);
const collection_foodItems = db.get("FoodItems");
// notre port localhost
const port = process.env.PORT || 3000;
const app = express();
// notre instance de serveur
const server = http.createServer(app);
// Cela crée notre socket en utilisant l'instance du serveur
const io = socketIO(server);
io.on("connection", socket => {
//  console.log("New client connected" + socket.id);
  //console.log(socket);
// Retourne les données initiales du menu alimentaire de la collection FoodItems
  socket.on("initial_data", () => {
    collection_foodItems.find({}).then(docs => {
      io.sockets.emit("get_data", docs);
    });
  });
// Passer la commande, appelé depuis /src/main/PlaceOrder.js du Frontend
  socket.on("putOrder", order => {
    collection_foodItems
      .update({ _id: order._id }, { $inc: { ordQty: order.order } })
      .then(updatedDoc => {
        // Émission de l'événement pour mettre à jour la Cuisine ouverte sur les appareils avec les valeurs de commande en temps réel
        io.sockets.emit("change_data");
      });
  });
// Achèvement de la commande, appelé depuis /src/main/Kitchen.js
  socket.on("mark_done", id => {
    collection_foodItems
      .update({ _id: id }, { $inc: { ordQty: -1, prodQty: 1 } })
      .then(updatedDoc => {
        // Mise à jour de la zone Cuisine avec le statut actuel.
        io.sockets.emit("change_data");
      });
  });

// Fonctionnalité pour changer la valeur de la quantité prévue, appelée depuis /src/main/UpdatePredicted.js
  socket.on("ChangePred", predicted_data => {
    collection_foodItems
      .update(
        { _id: predicted_data._id },
        { $set: { predQty: predicted_data.predQty } }
      )
      .then(updatedDoc => {
        // Événement Socket pour mettre à jour la quantité prévue dans la Cuisine
        io.sockets.emit("change_data");
      });
  });

// disconnect est déclenché lorsqu'un client quitte le serveur
  socket.on("disconnect", () => {
    console.log("user disconnected");
  });
});
/* Les étapes mentionnées ci-dessous sont effectuées pour retourner le build Frontend de create-react-app depuis le dossier build du backend. Commentez-les si vous exécutez localement*/
app.use(express.static("build"));
app.use("/kitchen", express.static("build"));
app.use("/updatepredicted", express.static("build"));
server.listen(port, () => console.log(`Listening on port ${port}`));
```

**Base de données** : MongoDB

[**Mlab**](https://mlab.com/) : Base de données en tant que service pour MongoDB

**Nom de la collection** : FoodItems

**Format du document** : Au moins un document est nécessaire dans la collection FoodItems avec le format mentionné ci-dessous.

```js
{
"name": "Veg Roll",  // Nom de la nourriture
"predQty": 100,  // Quantité prévue
"prodQty": 295,  // Quantité produite
"ordQty": 1   // Quantité totale de commande
}
```

J'espère que vous avez compris comment créer une application modulaire en temps réel en utilisant la pile MERN tendance. Si vous avez trouvé cela utile, **applaudissez** ci-dessous, donnez des **étoiles** au projet [repo](https://github.com/honey93/OrderKitchen) et partagez-le avec vos amis aussi.