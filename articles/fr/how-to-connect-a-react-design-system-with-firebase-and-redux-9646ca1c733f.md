---
title: Comment connecter un Système de Design React avec Firebase et Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T20:41:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-connect-a-react-design-system-with-firebase-and-redux-9646ca1c733f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gILubZM4zMQnVf4CAm-NSA.jpeg
tags:
- name: Design Systems
  slug: design-systems
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment connecter un Système de Design React avec Firebase et Redux
seo_desc: 'By Nazare Emanuel Ioan

  After almost two years of working with ReactJS at Creative-Tim, years while I’ve
  been creating simple front-end ReactJS projects, front-end templates, I have started
  to learn more about React, and create some tutorials.

  After l...'
---

Par Nazare Emanuel Ioan

Après presque deux ans de travail avec [ReactJS](https://reactjs.org/) chez [Creative-Tim](https://www.creative-tim.com/?ref=trrfadr-medium), années pendant lesquelles j'ai créé des projets ReactJS front-end simples, des templates front-end, j'ai commencé à en apprendre davantage sur React et à créer quelques tutoriels.

Après de longues heures à regarder et lire des tutoriels sur Firebase, des tutoriels sur Firebase et React, et à lire la documentation officielle de Firebase, je suis prêt à écrire moi-même un tutoriel.

**Ce que je vais utiliser dans cet article de tutoriel :**

* [npm@6.4.1](https://www.npmjs.com/package/npm)
* [nodejs@10.15.3 (version LTS)](https://nodejs.org/en/)
* [Atom Editor version 1.35.0](https://atom.io/)
* [Reactstrap](https://reactstrap.github.io/)

Nous allons utiliser Redux et Firebase pour la connexion, l'inscription et pour créer quelques cartes de statistiques dynamiques.

Je vais concentrer mon attention sur Firebase et donner des explications uniquement à ce sujet. Si vous ne connaissez pas Redux, il serait préférable de jeter un œil à mon autre [tutoriel sur ce qu'est Redux et ce qu'il fait](https://medium.freecodecamp.org/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85). Après cela, vous pourrez facilement revenir ici.

### Commencer avec un Système de Design React

Puisque nous n'avons pas le temps de créer notre propre système de design — cela prendrait des jours, des semaines ou même des mois — nous allons prendre celui sur lequel j'ai déjà travaillé.

Pour obtenir ce projet, vous pouvez faire l'une des choses suivantes (je vais utiliser la première option) :

* Cloner depuis Github :

```
git clone https://github.com/creativetimofficial/argon-dashboard-react.git
```

* [Télécharger depuis Github](https://github.com/creativetimofficial/argon-dashboard-react/archive/master.zip) (en cliquant sur le lien, le téléchargement démarrera automatiquement)
* [Télécharger depuis Creative-Tim](https://www.creative-tim.com/product/argon-dashboard-react) (vous devrez avoir un compte là-bas)

Après avoir obtenu le projet, accédez-y (dans mon cas, ce sera) :

```
cd argon-dashboard-react
```

Démarrons le produit et voyons à quoi il ressemble :

```
npm run install:clean
```

![Image](https://cdn-media-1.freecodecamp.org/images/4gzCHNeU-XA-EKgRe8fPoLAb5iSp1QqRmHzA)
_npm run install:clean — sortie_

### Ajout de Redux à ce modèle de démarrage

#### Actions, Réducteurs et Store

Revenons dans le terminal et exécutons :

```
npm i -E redux redux-thunk react-redux
```

Lorsque j'ai exécuté cette commande, sur ma machine, les versions installées étaient les suivantes :

* redux@4.0.1
* redux-thunk@2.3.0
* react-redux@6.0.1

Au début du tutoriel, nous avons fixé notre objectif de faire deux choses : la connexion et l'inscription (authentification) et d'être capable d'ajouter quelques cartes dynamiques depuis notre base de données (simple ajout). Cela signifie que nous aurons deux réducteurs, un pour l'authentification et un pour les cartes dynamiques (nous aurons également besoin d'un réducteur racine qui combinera ces deux-là). Nous aurons également quatre actions, une pour la connexion, une pour l'inscription, une pour ajouter les cartes à notre base de données (vous pouvez penser à celles-ci comme à des tâches) et une pour obtenir depuis la base de données toutes ces cartes (que nous rendrons dans notre application). Et aussi, juste un store.

Donc, cela étant dit, exécutons les commandes suivantes :

1 — Commandes Linux/Mac

```
mkdir src/actionsmkdir src/reducerstouch src/actions/addStatCardAction.jstouch src/actions/getAllStatCardsAction.jstouch src/actions/loginAction.jstouch src/actions/registerAction.jstouch src/reducers/statCardReducer.jstouch src/reducers/authReducer.jstouch src/reducers/rootReducer.jstouch src/store.js
```

2 — Commandes Windows

```
mkdir src\actionsmkdir src\reducersecho "" > src\actions\addStatCardAction.jsecho "" > src\actions\getAllStatCardsAction.jsecho "" > src\actions\loginAction.jsecho "" > src\actions\registerAction.jsecho "" > src\reducers\statCardReducer.jsecho "" > src\reducers\authReducer.jsecho "" > src\reducers\rootReducer.jsecho "" > src\store.js
```

#### Actions

**src/actions/addStatCardAction.js**

La carte de statistiques que nous voulons créer dynamiquement est l'une de celles-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/FuY9TJygUIsa-6GQcaufpcbow6BGjgMuuTxJ)
_cartes de statistiques à créer dynamiquement_

Comme nous pouvons le voir, elles ont un nom, une statistique, une icône (qui varie en couleur), une icône de pied de page et un pourcentage (qui varie à nouveau en couleur) et un texte de pied de page.

Nous devons donc créer l'action qui acceptera tout ce qui précède, comme suit :

```
const addStatCardAction = (  statName,  statDescription,  statIcon,  statIconColor,  statFooterIcon,  statFooterIconState,  statFooterPercentage,  statFooterText) => async dispatch => {  // ici nous allons faire un appel à notre base de données (firebase)  // pour ajouter notre nouvelle carte de statistiques avec les détails ci-dessus
```

```
  dispatch({    type: "addStatCard",    payload: {      statName: statName,      statDescription: statDescription,      statIcon: statIcon,      statIconColor: statIconColor,      statFooterIcon: statFooterIcon,      statFooterIconState: statFooterIconState,      statFooterPercentage: statFooterPercentage,      statFooterText: statFooterText    }  });};
```

```
export default addStatCardAction;
```

Comme nous pouvons le voir, nous allons travailler avec des créateurs d'actions asynchrones, puisque nous faisons des appels à une base de données. Après que l'appel soit terminé, nous devrons envoyer à notre store les données que nous venons d'ajouter à notre base de données dans firebase.

**src/actions/getAllStatCardsAction.js**

Celui-ci ne nécessitera aucun paramètre, puisqu'il ne récupère que quelque chose de la base de données. Le code ressemblera donc à ceci :

```
const getAllStatCardsAction = () => async dispatch => {  // ici nous allons faire un appel à notre base de données (firebase)  // qui récupérera toutes nos cartes de statistiques
```

```
  dispatch({ type: "getAllStatCards" , payload: {}});};
```

```
export default getAllStatCardsAction;
```

**src/actions/loginAction.js**

Pour la connexion, nous aurons un email et un mot de passe, donc voici le code pour cette action (notre formulaire de connexion a également un email et un mot de passe) :

```
const loginAction = (email, password) => async dispatch => {  // pour le moment, puisque nous n'avons pas encore connecté à la base de données  // nous allons dire que chaque fois que nous essayons de nous connecter  // nous ne devrions pas être en mesure de nous connecter (c'est pourquoi nous envoyons false)
```

```
  dispatch({ type: "login", payload: false });};
```

```
export default loginAction;
```

**src/actions/registerAction.js**

```
const registerAction = (name, email, password) => async dispatch => {  // pour le moment, puisque nous n'avons pas encore connecté à la base de données  // nous allons dire que chaque fois que nous essayons de nous inscrire  // nous ne devrions pas être en mesure de nous inscrire (c'est pourquoi nous envoyons false)
```

```
  dispatch({ type: "register", payload: false });};
```

```
export default registerAction;
```

#### Réducteurs

**src/reducers/statCardReducer.js**

Puisque nous avons deux actions concernant la carte de statistiques, nous aurons deux cas dans ce réducteur :

```
export default (state = {}, action) => {  switch (action.type) {    case "addStatCard":      console.log("adding ", action.payload);      // puisque nous allons toujours récupérer nos cartes de statistiques      // depuis firebase, chaque fois que nous en ajoutons une nouvelle      // nous allons simplement retourner l'état      return state;    case "getAllStatCards":      console.log("getting ", action.payload);      console.log(action.payload);      return {        // garder l'ancien état        ...state,        // ajouter toutes les cartes de la base de données        // elles viendront dans un format json,        // donc nous devons les convertir en tableau        statCardState: Object.values(action.payload)      };    default:      return state;  }};
```

Nous enregistrons également ce que nous ajoutons et ce que nous essayons d'obtenir de notre firebase.

**src/reducers/authReducer.js**

```
export default (state = {}, action) => {  switch (action.type) {    // dans les deux cas, nous voulons dire à notre application,    // si l'utilisateur est connecté ou non    // si l'utilisateur s'inscrit, il sera automatiquement connecté
```

```
    case "register":      console.log("register is ",action.payload);      return {        // garder l'ancien état        ...state,        // ajouter true/false si l'utilisateur est connecté ou non        loggedIn: action.payload      };    case "login":      console.log("login is ",action.payload);      return {        // garder l'ancien état        ...state,        // ajouter true/false si l'utilisateur est connecté ou non        loggedIn: action.payload      };    default:      return state;  }};
```

Lorsque nous inscrivons un nouvel utilisateur, nous le connectons automatiquement. Nous avons également ajouté quelques logs pour voir si l'inscription ou la connexion est réussie.

**src/reducers/rootReducer.js**

Ceci est pour combiner les réducteurs ci-dessus :

```
import { combineReducers } from "redux";
```

```
import authReducer from "reducers/authReducer";import statCardReducer from "reducers/statCardReducer";
```

```
export default combineReducers({  // le authReducer ne fonctionnera qu'avec authState  authState: authReducer,  // le statCardReducer ne fonctionnera qu'avec statCardState  statCardState: statCardReducer});
```

#### Store

**src/store.js**

Puisque nous avons des créateurs d'actions asynchrones, nous aurons besoin d'un middleware qui nous permettra d'utiliser ces créateurs d'actions, d'où l'utilisation de redux-thunk :

```
import { createStore, applyMiddleware } from "redux";import reduxThunk from "redux-thunk";
```

```
import rootReducer from "reducers/rootReducer";
```

```
function configureStore(  state = { authState: {}, statCardState: {} }) {  return createStore(rootReducer, state, applyMiddleware(reduxThunk));}
```

```
export default configureStore;
```

#### Connecter notre application à notre store

Pour le moment, si nous devions démarrer notre application, rien ne se passerait, puisque toutes les actions et notre store ne sont pas rendus dans notre application. C'est donc ce que nous allons faire maintenant.

Tout d'abord, ajoutons notre store, pour cela, nous devons aller dans **src/index.js**.

Avant la fonction **ReactDOM.render()**, nous devons ajouter les imports suivants :

```
import { Provider } from "react-redux";import configureStore from "store";
```

Et après cela, nous allons envelopper le **BrowserRouter** de la fonction **ReactDOM.render()** à l'intérieur de la balise **Provider** comme suit :

```
<Provider store={configureStore()}>  <BrowserRouter>    <Switch>      <Route path="/admin" render={          props => <AdminLayout {...props} />      } />      <Route path="/auth" render={          props => <AuthLayout {...props} />      } />      <Redirect from="/" to="/admin/index" />    </Switch>  </BrowserRouter></Provider>,
```

Notre prochaine préoccupation est de faire en sorte que nos utilisateurs soient redirigés vers la page de connexion s'ils ne sont pas authentifiés et s'ils sont authentifiés, qu'ils soient redirigés vers la page utilisateur. En gros, s'ils sont connectés, ils ne pourront pas accéder à la mise en page Auth (**src/layouts/Auth.jsx**), et s'ils ne le sont pas, ils ne pourront pas accéder à la mise en page Admin (**src/layouts/Admin.jsx**).

Allons dans **src/layouts/Auth.jsx** et après l'import **React**, faisons les imports suivants :

```
import { connect } from "react-redux";import { Redirect } from "react-router-dom";
```

Après cela, changeons l'export de ce composant comme suit :

```
const mapStateToProps = state => ({  ...state});
```

```
export default connect(  mapStateToProps,  {})(Auth);
```

Après cela, nous allons dans la fonction **render** de ce composant, et avant le **return**, ajoutons le code suivant :

```
if (this.props.authState.loggedIn) {  return <Redirect to="/admin/user-profile" />;}
```

Ainsi, si l'utilisateur est authentifié, il sera redirigé vers sa page de profil.

Ensuite, nous allons dans **src/layouts/Admin.jsx** et faisons les mêmes changements que pour la mise en page **Auth**. Ajoutons donc les imports suivants :

```
import { connect } from "react-redux";import { Redirect } from "react-router-dom";
```

Changeons son export en :

```
const mapStateToProps = state => ({  ...state});
```

```
export default connect(  mapStateToProps,  {})(Admin);
```

Une fois de plus, dans la fonction **render**, avant le **return**, nous ajoutons :

```
if (!this.props.authState.loggedIn) {  return <Redirect to="/auth/login" />;}
```

Cette fois, nous disons **!this.props.authState.loggedIn**, puisque nous voulons que l'utilisateur soit redirigé vers la page de connexion s'il n'est pas authentifié.

Redémarrons notre projet et voyons comment, chaque fois que nous essayons de naviguer vers le **Tableau de bord** ou le **Profil**, nous n'y avons pas accès puisque nous ne sommes pas connectés.

![Image](https://cdn-media-1.freecodecamp.org/images/i3yIhiqSEGtBulgXHfqhvGcYUVs9qQuB8zot)
_Projet après l'ajout des redirections_

Maintenant, nous devons aller dans les pages **Connexion** et **Inscription** et ajouter Redux à celles-ci également.

#### Connecter notre page de connexion à Redux en utilisant loginAction

Tout d'abord, allons dans **src/views/examples/Login.jsx** et après l'import **React**, ajoutons ces imports :

```
import { connect } from "react-redux";
```

```
import loginAction from "actions/loginAction";
```

Ensuite, changeons l'export à la fin du fichier par ceci :

```
const mapStateToProps = state => ({  ...state});
```

```
const mapDispatchToProps = dispatch => ({  loginAction:   (email, password) => dispatch(loginAction(email, password))});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Login);
```

Maintenant, avant la fonction render, nous écrivons :

```
state = {  email: "",  password: ""};onChange = (stateName, value) => {  this.setState({    [stateName]: value  });};
```

Nous aurons besoin de garder un état local pour l'email et le mot de passe et d'envoyer ces deux informations à notre firebase.

Ensuite, nous devons changer la ligne 85 de :

```
<Input placeholder="Email" type="email" />
```

En :

```
<Input  placeholder="Email"  type="email"  onChange={e => this.onChange("email", e.target.value)}/>
```

Nous allons également changer la ligne 99 de :

```
<Input placeholder="Password" type="password" />
```

En :

```
<Input  placeholder="Password"  type="password"  onChange={e => this.onChange("password", e.target.value)}/>
```

Nous sommes presque prêts pour la connexion. Ensuite, nous devons changer le bouton **Sign in** pour que, lorsque nous cliquons dessus, il appelle l'action **loginAction**. Changeons-le de :

```
<Button className="my-4" color="primary" type="button">  Sign in</Button>
```

En :

```
<Button  className="my-4"  color="primary"  type="button"  onClick={() =>    this.props.loginAction(      this.state.email,      this.state.password    )  }>  Sign in</Button>
```

Maintenant, retournez dans votre navigateur, et sur la page **Login**, ouvrez votre console, et essayez de vous connecter. Vous devriez obtenir une sortie de **login is false**. Nous savons donc que notre **action** et notre **réducteur** fonctionnent.

![Image](https://cdn-media-1.freecodecamp.org/images/ph56L3CSbnOONWONDMOIKWBTCCsIjzahNieS)
_**login is false**_

#### Connecter notre page d'inscription à Redux en utilisant registerAction

Allez dans **src/views/examples/Register.jsx** et faites de même que ci-dessus. Ajoutez donc d'abord les imports (cette fois avec **registerAction**) :

```
import { connect } from "react-redux";
```

```
import registerAction from "actions/registerAction";
```

Ensuite, l'export en :

```
const mapStateToProps = state => ({  ...state});
```

```
const mapDispatchToProps = dispatch => ({  registerAction: (name, email, password) => dispatch(registerAction(name, email, password))});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Register);
```

Ajoutez ce qui suit avant la fonction **render** :

```
state = {  name: "",  email: "",  password: ""};onChange = (stateName, value) => {  this.setState({    [stateName]: value  });};
```

Changez :

```
<Input placeholder="Name" type="text" />
```

En :

```
<Input placeholder="Name" type="text" onChange={e => this.onChange("name", e.target.value)}/>
```

Ensuite :

```
<Input placeholder="Email" type="email" />
```

En :

```
<Input placeholder="Email" type="email" onChange={e => this.onChange("email", e.target.value)}/>
```

Et enfin, le mot de passe également :

```
<Input placeholder="Password" type="password" />
```

En :

```
<Input placeholder="Password" type="password" onChange={e => this.onChange("password", e.target.value)}/>
```

Une dernière chose — le bouton, nous devons le changer de :

```
<Button className="mt-4" color="primary" type="button">  Create account</Button>
```

En :

```
<Button className="mt-4" color="primary" type="button"   onClick={() =>  this.props.registerAction(    this.state.name,    this.state.email,    this.state.password  )}>  Create account</Button>
```

Nous sommes donc prêts avec Redux. Retournez à la page d'inscription, tapez quelque chose dans le formulaire, puis appuyez sur le bouton Créer un compte avec la console ouverte. Vous devriez obtenir un **register is false**.

![Image](https://cdn-media-1.freecodecamp.org/images/jjNR3gDDVOYzZndVi3TpdZa3Qx7BXWSiTkPB)
_**register is false**_

#### Connecter notre composant Header à Redux en utilisant les actions addStatCardAction et getAllStatCardsAction

Maintenant, nous devons faire en sorte que nos **Stat Cards** du composant **Header** (ce composant peut être vu par exemple dans la page **Dashboard**) soient rendues à partir de notre **store/firebase**, et également, les faire créer dynamiquement — par exemple sur un **clic de bouton**.

Allez dans **src/components/Headers/Header.jsx** et ajoutez les imports suivants (après l'import **React**) :

```
import {connect} from "react-redux";
```

```
import addStatCardAction from "actions/addStatCardAction";import getAllStatCardsAction from "actions/getAllStatCardsAction";
```

```
import { Button } from "reactstrap";
```

Changez l'export par défaut en :

```
const mapStateToProps = state => ({  ...state});const mapDispatchToProps = dispatch => ({  getAllStatCardsAction: () => dispatch(getAllStatCardsAction()),  addStatCardAction: (    statName,    statDescription,    statIcon,    statIconColor,    statFooterIcon,    statFooterIconState,    statFooterPercentage,    statFooterText  ) =>    dispatch(      addStatCardAction(        statName,        statDescription,        statIcon,        statIconColor,        statFooterIcon,        statFooterIconState,        statFooterPercentage,        statFooterText      )    )});
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(Header);
```

Ensuite, ajoutons une fonction **componentDidMount** juste avant la fonction **render** comme suit :

```
componentDidMount(){  this.props.getAllStatCardsAction();}
```

Et maintenant, après le premier **div** à l'intérieur de l'instruction **return** de la fonction **render**, nous allons ajouter un **Button** qui ajoutera nos cartes de statistiques à l'intérieur de notre firebase :

```
<Container>  <Row>    <Col lg="6" xl="3">      <Button        color="primary"        onClick={() =>          this.props.addStatCardAction(            "Performance",            "49,65%",            "fas fa-percent",            "bg-info text-white rounded-circle shadow",            "fas fa-arrow-up",            "text-success",            " 12%",            "Since last month"          )        }      >        Add stat card      </Button>    </Col>  </Row></Container><br />
```

Et maintenant, nous devons supprimer tout le contenu de la balise **Row** (lignes 48-165 — de **<R**ow&g**t; à** </Row>), et le remplacer par ce qui suit :

```
{// nous vérifions d'abord si statCardState est indéfini  this.props.statCardState &&  // puis vérifions si statCardState.statCardState est  // peuplé avec des cartes de notre firebase  this.props.statCardState.statCardState &&  // et enfin, nous les rendons en utilisant la fonction map  this.props.statCardState.statCardState.map((prop, key) => {    return (      <Col lg="6" xl="3" key={key}>        <Card className="card-stats mb-4 mb-xl-0">          <CardBody>            <Row>              <div className="col">                <CardTitle                  tag="h5"                  className="text-uppercase text-muted mb-0"                >                  {prop.statName}                </CardTitle>                <span className="h2 font-weight-bold mb-0">                  {prop.statDescription}                </span>              </div>              <Col className="col-auto">                <div                  className={                    "icon icon-shape " + prop.statIconColor                  }                >                  <i className={prop.statIcon} />                </div>              </Col>            </Row>            <p className="mt-3 mb-0 text-muted text-sm">              <span                className={"mr-2 " + prop.statFooterIconState}              >                <i className={prop.statFooterIcon} />{" "}                {prop.statFooterPercentage}              </span>{" "}              <span className="text-nowrap">                {prop.statFooterText}              </span>            </p>          </CardBody>        </Card>      </Col>    );  })}
```

### Ajout de Firebase

#### Configuration du compte Firebase

Pour cela, vous devez avoir un [Compte Google](https://myaccount.google.com/). Si vous n'en avez pas, Google vous offre un guide rapide (1 minute) [Guide](https://support.google.com/mail/answer/56256?hl=en).

Après avoir créé votre compte, connectez-vous, ou si vous en avez déjà un, connectez-vous à celui-ci.

Ensuite, naviguez jusqu'à [cette page](https://firebase.google.com/) (c'est la page d'accueil de Firebase) et appuyez sur le bouton **GO TO CONSOLE**, ou naviguez directement vers [ce lien](https://console.firebase.google.com/u/0/).

Ensuite, appuyez sur le bouton **Add project**. Vous serez invité avec une modale, avec une entrée pour un **nom** (vous pouvez taper n'importe quel nom que vous souhaitez). Pour moi, ce sera **react-redux-firebase-tutorial**. Vous pouvez laisser tout le reste tel quel. **Acceptez les termes** puis appuyez sur le bouton **Create Project**. Vous devrez attendre un peu jusqu'à ce qu'il crée le projet (environ 30 secondes).

Après cela, appuyez sur le bouton **Continue**. Cela vous redirigera automatiquement vers la nouvelle page du projet. Dans le menu de gauche, appuyez sur le lien **Authentication**. Sur cette page, appuyez sur **Set up sign-in method**. Vous aurez un tableau avec **Provider** et **Status**. Appuyez sur la ligne **Email/Password**. Et cochez le premier **Switch** puis appuyez sur le bouton **Save**.

Maintenant, allez dans le lien **Database**, faites défiler la page vers le bas et appuyez sur le bouton **Create database**, sous **Realtime Database**. Après cela, dans l'invite modale qui s'ouvre, choisissez le bouton radio **Start in test mode** puis appuyez sur **Enable** et attendez quelques secondes.

Ensuite, vous devrez obtenir votre fichier de configuration (fichier de configuration que nous ajouterons à notre projet dans la section suivante). Pour cela, appuyez sur le lien **Project Overview** dans le menu de gauche, et après cela, appuyez sur le bouton **<**;/> (Web). Cop**y the** config variable an**d the firebase initiali**zation. Nous allons coller cela dans un nouveau fichier, dans la section suivante.

Nous avons terminé !

Nous n'aurons pas besoin de créer de tables pour nos utilisateurs, les détails de nos utilisateurs, ou nos cartes dynamiques, puisque Firebase les créera automatiquement — nous en parlerons dans la section suivante.

Voici les étapes ci-dessus, sous forme d'images :

![Image](https://cdn-media-1.freecodecamp.org/images/4COJIxHnrVZNkWZsV2SEUy9nnGooi5DfVNru)

![Image](https://cdn-media-1.freecodecamp.org/images/-J4f7OkHSJHNX4Q16tnQqQwOQHEPtSY0CcPY)

![Image](https://cdn-media-1.freecodecamp.org/images/g31yzK-Pt3iwx1ATEL0sZ9LoYdJDtH9rdp1o)

![Image](https://cdn-media-1.freecodecamp.org/images/lTBqKAmZs34jLSgyVeXPIsXp4f-r4dFsF9T0)

![Image](https://cdn-media-1.freecodecamp.org/images/qExTP7hRuHk3F0aQv3RCK3U28patPZ5BdBFj)

![Image](https://cdn-media-1.freecodecamp.org/images/0HzPZhEt2cWYBO8beQSPTb5GWVARZ7M6tZRE)

![Image](https://cdn-media-1.freecodecamp.org/images/wAhTEBfWmsLgX66S-BUVlcKF-5nR3-Fkvb3z)

![Image](https://cdn-media-1.freecodecamp.org/images/nkxMOuEp9SUWVSwA36DAqX3EXXwXpu5J5kST)

![Image](https://cdn-media-1.freecodecamp.org/images/htFFlwaTuyNn6okH9urG1askjORredSC9Eob)

![Image](https://cdn-media-1.freecodecamp.org/images/eYC-jXvLpX3Mpu9EKcvEp0cJMtpydCw1TjsF)

![Image](https://cdn-media-1.freecodecamp.org/images/VG9txfaAPtpb5tjGLoTAJnSyqcDa0qYsAb5H)

![Image](https://cdn-media-1.freecodecamp.org/images/WoAZ5etvIEG9uJ8BaSYwrMMKxgIk8ADx3XL9)

![Image](https://cdn-media-1.freecodecamp.org/images/9MwpNj7l32x5CqxCsVjV7fgciMHcBqFug8r2)

![Image](https://cdn-media-1.freecodecamp.org/images/GygAEXlsQoQlvAoFOG9GAT0EGD3BTU6IoQcZ)
_**Configuration d'un projet Firebase**_

#### Ajout de Firebase à notre projet

Installons **Firebase** dans notre application :

```
npm i -E firebase
```

Après cela, nous devons créer un fichier pour configurer notre Firebase dans notre application, donc :

1 — Commandes Linux/Mac

```
touch src/firebaseConfig.js
```

2 — Commandes Windows

```
echo "" > src\firebaseConfig.js
```

Et importons **Firebase** dans ce fichier, puis exportons Firebase avec l'initialisation (vous avez besoin du code de la section précédente — voir la dernière image) :

```
import * as firebase from "firebase";
```

```
// remplacez cette variable par votre propre variable de configuration// depuis votre projet Firebase
var config = {  apiKey: "YOUR_KEY_HERE",  authDomain: "YOUR_DOMAIN_HERE",  databaseURL: "YOUR_URL_HERE",  projectId: "YOUR_ID_HERE",  storageBucket: "YOUR_BUCKET_HERE",  messagingSenderId: "YOUR_ID_HERE"};
```

```
let firebaseConfig = firebase.initializeApp(config);
```

```
export default firebaseConfig;
```

Maintenant, nous pouvons importer notre **firebaseConfig** partout où nous en avons besoin.

#### Inscription

Commençons par rendre notre **registerAction** fonctionnelle. Donc, nous allons dans **src/actions/registerAction.js** et au début du fichier, nous importons notre configuration Firebase :

```
import firebase from "firebaseConfig";
```

Après cela, nous pourrions avoir besoin pour nos utilisateurs de conserver des informations, comme leur nom, leurs photos, etc., donc nous allons créer une nouvelle table appelée user-details. Si elle n'existe pas, ajoutez-y le nom de notre utilisateur.

Notre formulaire n'a que l'email, le mot de passe et le nom — Firebase créera automatiquement une table de base de données dans laquelle il ne mettra que les identifiants (email et mot de passe) du compte. Donc, si nous voulons conserver plus de détails sur nos utilisateurs, nous devrons créer une nouvelle table — ma table aura l'ID de l'utilisateur, de la table avec les identifiants, et le nom de l'utilisateur.

Donc, après l'import ci-dessus, nous disons :

```
// donnez-moi la base de données Firebase
```

```
const databaseRef = firebase.database().ref();
```

```
// donnez-moi la table nommée user-details// si elle n'existe pas, Firebase la// créera automatiquement
```

```
const userDetailsRef = databaseRef.child("user-details");
```

Après cela, nous allons changer notre code de dispatch de :

```
dispatch({ type: "register", payload: false });
```

En :

```
// Firebase nous offre cette fonction createUserWithEmailAndPassword// qui créera automatiquement l'utilisateur pour nous// elle n'a que deux arguments, l'email et le mot de passe
```

```
firebase.auth().createUserWithEmailAndPassword(email, password)
```

```
// la fonction then() est utilisée pour savoir quand l'appel asynchrone s'est terminé// de cette façon, nous pouvons notifier nos réducteurs que l'inscription a réussi
```

```
.then(function(user) {
```

```
  // nous prenons l'ID de l'utilisateur et son nom et nous les ajoutons dans notre  // table user-details
```

```
  userDetailsRef.push().set({userId: user.user.uid, userName: name});
```

```
  // après cela, nous dispatchons à nos réducteurs le fait que  // l'inscription a réussi en envoyant true
```

```
  dispatch({type:"register", payload: true});
```

```
// si l'inscription n'a pas réussi, nous pouvons attraper les erreurs ici
```

```
}).catch(function(error) {
```

```
  // si nous avons des erreurs, nous allons lancer une alerte avec cette erreur
```

```
  alert(error);
```

```
});
```

Donc, à la fin, notre **registerAction** ressemblera à ceci :

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const userDetailsRef = databaseRef.child("user-details");
```

```
const registerAction = (name, email, password) => async dispatch => {  firebase    .auth()    .createUserWithEmailAndPassword(email, password)    .then(function(user) {      userDetailsRef.push().set(        { userId: user.user.uid, userName: name }      );      dispatch({ type: "register", payload: true });    })    .catch(function(error) {      alert(error);    });};
```

```
export default registerAction;
```

Ouvrez à nouveau l'application et allez à la page d'inscription. Tapez un nom, un email valide et un mot de passe (quelque chose de simple à retenir — quelque chose comme **qwerty**). Après avoir appuyé sur le bouton **Create account**, vous devriez être redirigé vers la page **user-profile** — cela signifie que notre inscription a réussi. Nous pouvons maintenant retourner à notre **projet Firebase** ([https://console.firebase.google.com/u/0/](https://console.firebase.google.com/u/0/) — appuyez sur votre projet), cliquez sur le lien **Authentication**, et nous verrons cet email que nous venons d'écrire. De plus, si nous allons au lien **Database**, nous verrons notre table **user-details**.

![Image](https://cdn-media-1.freecodecamp.org/images/Fcvn-A-fMjcOHvtni0hCQNwIm3UAEtIOulZh)
_**L'action d'inscription fonctionne maintenant**_

#### **Connexion**

Nous allons dans **src/actions/loginAction.js** et au début du fichier, nous importons notre configuration Firebase :

```
import firebase from "firebaseConfig";
```

Pour cette action, nous n'aurons pas besoin d'autre chose, donc la prochaine chose est de changer notre code de dispatch de :

```
dispatch({ type: "login", payload: false });
```

En :

```
// Firebase nous offre cette fonction signInWithEmailAndPassword// qui créera automatiquement l'utilisateur pour nous// elle n'a que deux arguments, l'email et le mot de passe
```

```
firebase  .auth()  .signInWithEmailAndPassword(email, password)  // la fonction then() est utilisée pour savoir quand l'appel asynchrone s'est terminé  // de cette façon, nous pouvons notifier nos réducteurs que la connexion a réussi    .then(function(user) {    // si la connexion a réussi, alors     // nous dispatchons à nos réducteurs le fait que    // la connexion a réussi en envoyant true    dispatch({type:"login", payload: "true"});  })
```

```
// si la connexion n'a pas réussi, nous pouvons attraper les erreurs ici    .catch(function(error) {
```

```
// si nous avons des erreurs, nous allons lancer une alerte avec cette erreur        alert(error);  });
```

Donc, à la fin, notre **loginAction** devrait ressembler à ceci :

```
import firebase from "firebaseConfig";
```

```
const loginAction = (email, password) => async dispatch => {  firebase    .auth()    .signInWithEmailAndPassword(email, password)    .then(function(user) {      dispatch({ type: "login", payload: "true" });    })    .catch(function(error) {      alert(error);    });};
```

```
export default loginAction;
```

Si nous ouvrons à nouveau notre application (nous devrions être redirigés par défaut vers la page **Login**), et si nous entrons notre email et notre mot de passe, nous pourrons nous connecter à notre nouveau compte.

![Image](https://cdn-media-1.freecodecamp.org/images/KiDtGPZVvtaeDG8QbYNQxgjUcZgn1dEpoCxK)
_**L'action de connexion fonctionne**_

#### Ajouter des cartes de statistiques et les rendre

Maintenant, nous devons apporter quelques modifications à nos actions concernant les cartes de statistiques.

Dans **src/actions/getAllStatCardsAction.js**, nous devons ajouter les imports suivants :

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();// ceci est pour obtenir la table stat-cards de firebaseconst statCardsRef = databaseRef.child("stat-cards");
```

Ensuite, nous devons changer le **dispatch** de :

```
dispatch({ type: "getAllStatCards", payload: {} });
```

En :

```
// cette fonction obtiendra toutes les entrées de la// table stat-cards, dans un format jsonstatCardsRef.on("value", snapshot => {  dispatch({    type: "getAllStatCards",    // si le json retourne null, c'est-à-dire que la    // table stat-cards est vide - vide    // alors nous retournerons un objet vide    payload: snapshot.val() || {}  });});
```

Voici à quoi devrait ressembler l'action maintenant :

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

```
const getAllStatCardsAction = () => async dispatch => {  statCardsRef.on("value", snapshot => {    dispatch({      type: "getAllStatCards",      payload: snapshot.val() || {}    });  });};
```

```
export default getAllStatCardsAction;
```

Ensuite, c'est le **src/actions/addStatCardAction.js**. Comme le précédent, nous avons besoin de quelques imports :

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

Maintenant, au lieu du simple dispatch, nous allons le remplacer de :

```
dispatch({  type: "addStatCard",  payload: {    statName: statName,    statDescription: statDescription,    statIcon: statIcon,    statIconColor: statIconColor,    statFooterIcon: statFooterIcon,    statFooterIconState: statFooterIconState,    statFooterPercentage: statFooterPercentage,    statFooterText: statFooterText  }});
```

En :

```
statCardsRef  // la fonction push enverra à notre firebase le nouvel objet  .push()  // et définira dans une nouvelle ligne de la table stat-cards  // avec l'objet ci-dessous  .set({    statName: statName,    statDescription: statDescription,    statIcon: statIcon,    statIconColor: statIconColor,    statFooterIcon: statFooterIcon,    statFooterIconState: statFooterIconState,    statFooterPercentage: statFooterPercentage,    statFooterText: statFooterText  })  // lorsque le push est terminé, nous allons dispatcher à notre  // réducteur que nous avons ajouté avec succès une nouvelle ligne  .then(() => {    dispatch({      type: "addStatCard"    });  });
```

Donc, cela devrait maintenant ressembler à :

```
import firebase from "firebaseConfig";
```

```
const databaseRef = firebase.database().ref();const statCardsRef = databaseRef.child("stat-cards");
```

```
const addStatCardAction = (  statName,  statDescription,  statIcon,  statIconColor,  statFooterIcon,  statFooterIconState,  statFooterPercentage,  statFooterText) => async dispatch => {  statCardsRef    .push()    .set({      statName: statName,      statDescription: statDescription,      statIcon: statIcon,      statIconColor: statIconColor,      statFooterIcon: statFooterIcon,      statFooterIconState: statFooterIconState,      statFooterPercentage: statFooterPercentage,      statFooterText: statFooterText    })    .then(() => {      dispatch({        type: "addStatCard"      });    });};
```

```
export default addStatCardAction;
```

Et nous sommes prêts. Relancez l'application, connectez-vous à votre compte, naviguez sur la page **Dashboard**, puis appuyez sur le bouton **Add stat card**. Les statistiques devraient maintenant commencer à s'ajouter à votre **Header**.

![Image](https://cdn-media-1.freecodecamp.org/images/ghyjERjE8Jp6HG2yCIUM5aP7ddP8HTX6HfUT)
_**L'application est terminée**_

### Merci d'avoir lu !

Si vous avez apprécié la lecture de ce tutoriel, donnez-lui un applaudissement. Je suis très intéressé par vos commentaires à ce sujet. Laissez simplement un commentaire sur ce fil et je serai plus qu'heureux de répondre.

Liens utiles :

* Obtenez le code de ce tutoriel depuis [Github](https://github.com/EINazare/react-redux-firebase-rds-tutorial)
* Lisez plus sur ReactJS sur [leur site officiel](https://reactjs.org/)
* Lisez plus sur [Redux ici](https://redux.js.org/)
* Lisez plus sur [React-Redux](https://react-redux.js.org/)
* Lisez plus sur [Firebase](https://firebase.google.com/docs/)
* Consultez notre plateforme pour voir [ce que nous faisons](https://www.creative-tim.com/) et [qui nous sommes](https://www.creative-tim.com/presentation)
* Lisez plus sur [Reactstrap](https://reactstrap.github.io/), le cœur d'Argon Dashboard React
* Lisez mon [tutoriel Webpack](https://medium.freecodecamp.org/how-to-use-reactjs-with-webpack-4-babel-7-and-material-design-ff754586f618) et/ou mon [tutoriel Redux](https://medium.freecodecamp.org/how-to-use-redux-in-reactjs-with-real-life-examples-687ab4441b85)

Trouvez-moi sur :

* Facebook : [https://www.facebook.com/NazareEmanuel](https://www.facebook.com/NazareEmanuel)
* Instagram : [https://www.instagram.com/manu.nazare/](https://www.instagram.com/manu.nazare/)
* Linkedin : [https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/](https://www.linkedin.com/in/nazare-emanuel-ioan-4298b5149/)
* Email : [manu@creative-tim.com](mailto:manu@creative-tim.com)