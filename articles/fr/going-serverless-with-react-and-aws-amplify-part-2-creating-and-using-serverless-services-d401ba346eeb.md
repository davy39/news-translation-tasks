---
title: 'Devenir serverless avec React et AWS Amplify Partie 2 : Création et utilisation
  de services serverless'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:52:41.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services-d401ba346eeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0iJpmj6zVTc8EHFGW5VTnA.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: 'Devenir serverless avec React et AWS Amplify Partie 2 : Création et utilisation
  de services serverless'
seo_desc: 'By Peter Mbanugo

  Serverless is a cloud-computing execution model in which the cloud provider is responsible
  for executing a piece of code by dynamically allocating resources to run the code
  when needed. In a previous post, we looked at what serverles...'
---

Par Peter Mbanugo

Serverless est un modèle d'exécution de cloud computing dans lequel le fournisseur de cloud est responsable de l'exécution d'un morceau de code en allouant dynamiquement des ressources pour exécuter le code lorsque cela est nécessaire. Dans un précédent [article](https://medium.freecodecamp.org/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd), nous avons examiné ce qu'est le serverless, et nous avons configuré notre ordinateur pour pouvoir construire des applications serverless en utilisant AWS Amplify. Nous avons initialisé un projet React et ajouté la bibliothèque Amplify. Dans cet article, nous allons utiliser l'interface de ligne de commande Amplify pour provisionner une API backend sécurisée et une base de données NoSQL. Ensuite, nous allons consommer cette API à partir du projet React.

### Création des services backend serverless

L'application que nous allons construire permettra aux utilisateurs d'effectuer des opérations CRUD de base. Nous utiliserons une API REST avec une base de données NoSQL. Suivez les instructions ci-dessous pour créer le backend serverless.

1. Ouvrez la ligne de commande et allez dans le répertoire racine de votre projet.
2. Exécutez la commande `amplify add api`.
3. Vous obtenez une invite pour sélectionner un type de service. Choisissez `REST` et appuyez sur Entrée.
4. Il vous demande d'entrer un nom pour la catégorie actuelle (la catégorie API). Entrez `todosApi` et appuyez sur Entrée.
5. Vous êtes invité à entrer un chemin. Acceptez le chemin par défaut `items` en appuyant sur Entrée.
6. L'invite suivante demande la source Lambda. L'API REST serverless fonctionne en créant un chemin sur API Gateway et en mappant ce chemin à une fonction lambda. La fonction lambda contient le code à exécuter lorsqu'une requête est faite au chemin auquel elle est mappée. Nous allons créer une nouvelle lambda. Sélectionnez l'option `Create a new Lambda function` et appuyez sur Entrée.
7. Entrez `todosLambda` comme nom de la ressource pour la catégorie (catégorie de fonction), et appuyez sur Entrée.
8. Vous serez invité à entrer le nom de la fonction lambda. Entrez `todos` et appuyez sur Entrée.
9. Vous serez invité à choisir un modèle pour générer du code pour cette fonction. Choisissez l'option `CRUD function for Amazon DynamoDB table (Integration with Amazon API Gateway and Amazon DynamoDB)` et appuyez sur Entrée. Cela crée une architecture utilisant API Gateway avec Express s'exécutant dans une fonction AWS Lambda qui lit et écrit dans Amazon DynamoDB.
10. L'invite suivante demande de choisir une source de données DynanoDB. Nous n'avons pas de table DynamoDB existante, donc nous choisirons l'option `Create a new DynamoDB table`. Appuyez sur Entrée pour continuer. Vous devriez maintenant voir l'assistant de base de données DynamoDB. Il posera une série de questions pour déterminer comment créer la base de données.
11. Vous serez invité à entrer le nom de cette ressource. Entrez `todosTable` et appuyez sur Entrée.
12. L'invite suivante est pour le nom de la table. Entrez `todos` et appuyez sur Entrée.
13. Vous serez invité à ajouter des colonnes à la table DynamoDB. Suivez l'invite pour créer la colonne `id` avec `String` comme type.
14. Sélectionnez la colonne `id` lorsque vous êtes invité à entrer la clé de partition (clé primaire) pour la table.
15. Vous serez invité à ajouter une clé de tri à la table. Choisissez false.
16. L'invite suivante demande si vous souhaitez ajouter des index secondaires globaux à votre table. Entrez `n` et appuyez sur Entrée. Vous devriez voir le message `Successfully added DynamoDb table locally`
17. L'invite suivante demande **Souhaitez-vous modifier la fonction lambda locale maintenant ?**. Entrez `n` et appuyez sur Entrée. Vous devriez voir le message `Successfully added the Lambda function locally`.
18. Vous êtes invité à restreindre l'accès à l'API. Entrez `y` et appuyez sur Entrée.
19. Pour l'invite suivante, choisissez `Authenticated and Guest users` et appuyez sur Entrée. Cette option donne accès à l'API REST aux utilisateurs autorisés et invités.
20. Ensuite, vous êtes invité à choisir `What kind of access do you want for Authenticated users`. Choisissez `read/write` et appuyez sur Entrée.
21. Maintenant, nous obtenons une invite pour choisir le type d'accès pour les utilisateurs non authentifiés (c'est-à-dire les invités). Choisissez `read` et appuyez sur Entrée. Vous devriez obtenir le message `Successfully added auth resource locally`. Cela est dû au fait que nous avons choisi de restreindre l'accès à l'API, et le CLI a ajouté la catégorie Auth au projet puisque nous n'en avions pas pour le projet. À ce stade, nous avons ajouté les ressources nécessaires pour créer notre API (API Gateway, DynamoDB, Lambda function, et Cognito pour l'authentification).
22. Nous sommes invités à ajouter un autre chemin à l'API. Entrez `n` et appuyez sur Entrée. Cela complète le processus et nous obtenons le message `Successfully added resource todosApi locally`.

La commande `amplify add api` nous a guidés à travers le processus de création d'une API REST. Cette API sera créée en fonction des options que nous avons choisies. Pour créer cette API, il faut 4 services AWS. Ils sont :

1. Amazon DynamoDB. Cela servira de base de données NoSQL. Nous avons créé une table DynomoDB nommée `todos` lorsque nous avons ajouté la ressource `todosTable`. Nous lui avons donné 3 colonnes avec `id` comme clé primaire.
2. Fonctions AWS Lambda. Cela nous permet d'exécuter du code sans provisionner ou gérer de serveurs. C'est là que se trouvera notre code pour effectuer des opérations CRUD sur la table DynamoDB.
3. Amazon Cognito. Cela est responsable de l'authentification et de la gestion des utilisateurs. Cela nous permet d'ajouter l'inscription des utilisateurs, la connexion et le contrôle d'accès à notre application. Nous avons choisi l'option de restreindre l'accès à notre API, et ce service nous aidera à authentifier les utilisateurs.
4. Amazon API Gateway. C'est ce qui nous permet de créer un point de terminaison d'API REST. Nous avons ajouté une ressource pour cela nommée `todosApi`, avec un chemin `items`. Nous avons également sélectionné l'option de restreindre l'accès à l'API.

Cependant, les spécifications de service pour ces services ne sont pas encore dans le cloud. Nous devons mettre à jour le projet dans le cloud avec les informations pour fournir les services nécessaires. Exécutez la commande `amplify status`, et nous devrions obtenir un tableau avec des informations sur le projet amplify.

![Image](https://cdn-media-1.freecodecamp.org/images/g08emYbuJANf72jvqIJIJmBvofadlT35UY13)

Ouvrez le fichier **backend/function/todosLambda/src/app.js**. Vous remarquerez que ce fichier contient du code généré lors du processus de configuration de la ressource. Il utilise [Express.js](https://expressjs.com/) pour configurer les routes, et le package [aws-serverless-express](https://github.com/awslabs/aws-serverless-express) pour construire facilement des API RESTful en utilisant le framework Express.js sur AWS Lambda et Amazon API Gateway.

Lorsque nous poussons la configuration du projet dans le cloud, elle configurera une API proxy simple en utilisant Amazon API Gateway et l'intégrera avec cette fonction Lambda. Le package inclut un middleware pour obtenir facilement l'objet événement que Lambda reçoit de API Gateway. Il a été appliqué à la ligne 32 `app.use(awsServerlessExpressMiddleware.eventContext());` et utilisé dans les routes avec des codes qui ressemblent à `req.apiGateway.event.*`. Les routes prédéfinies nous permettent d'effectuer des opérations CRUD sur la table DynamoDB.

Nous allons apporter quelques modifications à ce fichier. La première consistera à changer la valeur de la variable `tableName` de `todosTable` à `todos`. Lors de la création de la ressource DynamoDB, nous avons spécifié `todosTable` comme nom de la ressource et `todos` comme nom de la table, donc il a utilisé à tort le nom de la ressource comme nom de la table lors de la création du fichier. Cela sera probablement corrigé dans une future version du CLI, donc si vous ne trouvez pas cette erreur, vous pouvez ignorer cette étape. Nous devrons également mettre à jour les définitions.

Changez la première définition de route pour utiliser le code ci-dessous.

```
app.get(path, function(req, res) {  const queryParams = {    TableName: tableName,    ProjectionExpression: "id, title"  };
```

```
  dynamodb.scan(queryParams, (err, data) => {    if (err) {      res.json({ error: "Could not load items: " + err });    } else {      res.json(data.Items);    }  });});
```

Cela définit une route pour répondre au chemin **/items** avec du code pour retourner toutes les données de la table DynamoDB. Les valeurs `ProjectionExpression` sont utilisées pour spécifier qu'il doit obtenir uniquement les colonnes `id` et `title`.

Changez la définition de route à la ligne 77 pour qu'elle se lise comme `app.get(path + hashKeyPath + sortKeyPath, function(req, res) {`. Cela nous permet de récupérer un élément par son `id` en suivant le chemin **/items/:id**. Changez également la ligne 173 pour qu'elle soit `app.delete(path + hashKeyPath + sortKeyPath, function(req, res) {`. Cela répond à la méthode HTTP DELETE pour supprimer un élément en suivant le chemin **/items/:id**.

Les ressources AWS ont été ajoutées et mises à jour localement, et nous devons les provisionner dans le cloud. Ouvrez la ligne de commande et exécutez `amplify push`. Vous obtiendrez une invite si vous souhaitez continuer à exécuter la commande. Entrez `y` et appuyez sur Entrée. Ce que cela fait, c'est qu'il téléchargera les dernières versions des modèles de piles de ressources imbriquées vers un bucket de déploiement S3, puis appellera l'API AWS CloudFormation pour créer/mettre à jour les ressources dans le cloud.

### Construction du Frontend

Lorsque la commande `amplify push` est terminée, vous verrez un fichier **aws-exports.js** dans le dossier **src**. Ce fichier contient des informations sur les ressources qui ont été créées dans le cloud. Chaque fois qu'une ressource est créée ou mise à jour en exécutant la commande `push`, ce fichier sera mis à jour. Il est créé pour les projets JavaScript et sera utilisé dans la bibliothèque JavaScript Amplify. Nous allons utiliser cela dans notre projet React. Nous allons également utiliser Bootstrap pour styliser la page. Ouvrez **public/index.html** et ajoutez ce qui suit dans le head :

```
<link  rel="stylesheet"  href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"  integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"  crossorigin="anonymous"/><script  src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"  crossorigin="anonymous"></script><script  src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"  integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"  crossorigin="anonymous"></script><script  src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"  integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"  crossorigin="anonymous"></script>
```

Ajoutez un nouveau fichier **src/List.js** avec le contenu suivant :

```
import React from "react";
```

```
export default props => (  <div>    <legend>Liste</legend>    <div className="card" style={{ width: "25rem" }}>      {renderListItem(props.list, props.loadDetailsPage)}    </div>  </div>);
```

```
function renderListItem(list, loadDetailsPage) {  const listItems = list.map(item => (    <li      key={item.id}      className="list-group-item"      onClick={() => loadDetailsPage(item.id)}    >      {item.title}    </li>  ));
```

```
  return <ul className="list-group list-group-flush">{listItems}&lt;/ul>;}
```

Ce composant affichera une liste d'éléments de l'API. Ajoutez un nouveau fichier **src/Details.js** avec le contenu suivant :

```
import React from "react";
```

```
export default props => (  <div>    <h2>Détails</h2>    <div className="btn-group" role="group">      <button        type="button"        className="btn btn-secondary"        onClick={props.loadListPage}      >        Retour à la liste      </button>      <button        type="button"        className="btn btn-danger"        onClick={() => props.delete(props.item.id)}      >        Supprimer      </button>    </div>    <legend>{props.item.title}</legend>    <div className="card">      <div className="card-body">{props.item.content}</div>    </div>  </div>);
```

Ce composant affichera les détails d'un élément avec des boutons pour supprimer cet élément ou revenir à la vue liste. Ouvrez **src/App.js** et mettez-le à jour avec ce code :

```
import React, { Component } from "react";import List from "./List";import Details from "./Details";
```

```
import Amplify, { API } from "aws-amplify";import aws_exports from "./aws-exports";import { withAuthenticator } from "aws-amplify-react";Amplify.configure(aws_exports);
```

```
class App extends Component {  constructor(props) {    super(props);    this.state = {      content: "",      title: "",      list: [],      item: {},      showDetails: false    };  }
```

```
  async componentDidMount() {    await this.fetchList();  }  handleChange = event => {    const id = event.target.id;    this.setState({ [id]: event.target.value });  };
```

```
  handleSubmit = async event => {    event.preventDefault();    await API.post("todosApi", "/items", {      body: {        id: Date.now().toString(),        title: this.state.title,        content: this.state.content      }    });
```

```
    this.setState({ content: "", title: "" });    this.fetchList();  };  async fetchList() {    const response = await API.get("todosApi", "/items");    this.setState({ list: [...response] });  }
```

```
  loadDetailsPage = async id => {    const response = await API.get("todosApi", "/items/" + id);    this.setState({ item: { ...response }, showDetails: true });  };
```

```
  loadListPage = () => {    this.setState({ showDetails: false });  };
```

```
  delete = async id => {    //TODO: Implémenter la fonctionnalité  };
```

```
  render() {    return (      <div className="container">        <form onSubmit={this.handleSubmit}>          <legend>Ajouter</legend>          <div className="form-group">            <label htmlFor="title">Titre</label>            <input              type="text"              className="form-control"              id="title"              placeholder="Titre"              value={this.state.title}              onChange={this.handleChange}            />          </div>          <div className="form-group">            <label htmlFor="content">Contenu</label>            <textarea              className="form-control"              id="content"              placeholder="Contenu"              value={this.state.content}              onChange={this.handleChange}            />          </div>          <button type="submit" className="btn btn-primary">            Soumettre          </button>        </form>        <hr />        {this.state.showDetails ? (          <Details            item={this.state.item}            loadListPage={this.loadListPage}            delete={this.delete}          />        ) : (          <List list={this.state.list} loadDetailsPage={this.loadDetailsPage} />        )}      </div>    );  }}
```

```
export default withAuthenticator(App, true);
```

Nous avons importé la bibliothèque Amplify et l'avons initialisée en appelant `Amplify.configure(aws_exports);`. Lorsque le composant est monté, nous appelons `fetchList()` pour récupérer les éléments de l'API.

Cette fonction utilise le client API de la bibliothèque Amplify pour appeler l'API REST. Sous le capot, elle utilise [Axios](https://github.com/axios/axios) pour exécuter les requêtes HTTP. Elle ajoutera les en-têtes nécessaires à la requête pour que vous puissiez appeler avec succès l'API REST. Vous pouvez ajouter des en-têtes si vous avez défini des en-têtes personnalisés pour votre API.

Pour notre projet, nous ne spécifions que le apiName et le chemin lors de l'appel des fonctions du client API. La fonction `loadDetailsPage()` récupère un élément particulier de la base de données via l'API. Ensuite, elle définit l'état `item` avec la réponse et `showDetails` à true. Ce `showDetails` est utilisé dans la fonction de rendu pour basculer entre l'affichage d'une liste d'éléments ou la page de détails d'un élément sélectionné. La fonction `handleSubmit()` est appelée lorsque le formulaire est soumis. Elle envoie les données du formulaire à l'API pour créer un document dans la base de données, avec les colonnes `id`, `title` et `content`, puis appelle `fetchList()` pour mettre à jour la liste. J'ai laissé la fonction `delete()` vide pour que vous puissiez l'implémenter vous-même. Quelle meilleure façon d'apprendre qu'en essayant par vous-même ?

Cette fonction sera appelée à partir du bouton de suppression dans le composant `Details`. Le code que vous y mettez doit appeler l'API pour supprimer un élément par `id` et afficher le composant de liste avec les éléments corrects.

Nous avons enveloppé le composant App avec le composant d'ordre supérieur `withAuthenticator` de la bibliothèque Amplify React. Cela fournit à l'application des flux complets pour l'enregistrement des utilisateurs, la connexion, l'inscription et la déconnexion. Seuls les utilisateurs connectés peuvent accéder à l'application puisque nous utilisons ce composant d'ordre supérieur. Le composant `withAuthenticator` détecte automatiquement l'état d'authentification et met à jour l'interface utilisateur. Si l'utilisateur est connecté, le composant **App** sous-jacent est affiché, sinon, les contrôles de connexion/inscription sont affichés.

Le deuxième argument, qui a été défini sur `true`, lui indique d'afficher un bouton de déconnexion en haut de la page. L'utilisation du composant `withAuthenticator` est le moyen le plus simple d'ajouter des flux d'authentification à votre application. Vous pouvez également avoir une interface utilisateur personnalisée et utiliser un ensemble d'API de la bibliothèque Amplify pour implémenter les flux de connexion et d'inscription. Voir la [documentation](https://aws-amplify.github.io/docs/js/authentication#working-with-the-api) pour plus de détails.

Nous avons tout le code nécessaire pour utiliser l'application. Ouvrez le terminal et exécutez `npm start` pour démarrer l'application. Vous devrez vous inscrire et vous connecter pour utiliser l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/XpzhaOkjAB6ppf7XWKFAK8eMlbbzfU67letq)
_application terminée_

### Conclusion

Nous avons passé en revue la création de nos services backend en utilisant l'interface de ligne de commande Amplify. La commande `amplify add api` nous a guidés à travers l'ajout de ressources pour DynamoDB, Lambda, API Gateway et Cognito pour l'authentification. Nous avons mis à jour le code dans **backend/function/todosLambda/src/app.js** pour correspondre à notre exigence API. Nous avons ajouté des composants d'interface utilisateur pour effectuer des opérations CRUD sur l'application et utilisé un composant d'ordre supérieur de la bibliothèque Amplify React pour permettre uniquement aux utilisateurs authentifiés d'accéder à l'application.

Vous devriez remarquer que nous n'avons utilisé que quelques lignes de code pour ajouter des flux d'authentification et appeler l'API. De plus, la création des services backend serverless et leur connexion ensemble a été faite avec une commande et en répondant aux invites qui ont suivi. Cela montre ainsi comment AWS Amplify facilite le développement.

> _Publié à l'origine sur mon [blog](https://www.pmbanugo.me/blog/2019-01-14-going-serverless-with-react-and-aws-amplify-part-2-creating-and-using-serverless-services/)._