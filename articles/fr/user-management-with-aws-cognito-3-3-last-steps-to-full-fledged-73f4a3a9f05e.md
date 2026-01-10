---
title: Gestion des utilisateurs avec AWS Cognito — (3/3) Dernières étapes pour un
  système complet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-02T18:31:12.000Z'
originalURL: https://freecodecamp.org/news/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ubdzj9K3MrbMb0Ep0UV3IA.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Gestion des utilisateurs avec AWS Cognito — (3/3) Dernières étapes pour
  un système complet
seo_desc: 'By Kangze Huang

  The Complete AWS Web Boilerplate — Part 1C



  Main Table of Contents Click Here

  Part A: Initial Setup

  Part B: The Core Functionality

  Part C: Last Steps to Full Fledged


  Download the Github here.

  The Last Steps

  The last pieces to this g...'
---

Par Kangze Huang

#### Le modèle complet AWS Web Boilerplate — Partie 1C

![Image](https://cdn-media-1.freecodecamp.org/images/638LdmUDcLc3rZMddMwajeKtKnW5y7Ta5Wbx)

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Configuration initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [Fonctionnalités principales](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour un système complet](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

Téléchargez le Github [ici](https://github.com/kangzeroo/Kangzeroos-AWS-Cognito-Boilerplate).

### Les dernières étapes

Les dernières pièces de ce grand schéma comprennent les touches finales et l'authentification backend. Par touches finales, nous entendons :

> - updateUserInfo()

> - forgotPassword()

> - signOutUser()

> - retrieveUserFromLocalStorage()

> - Authentification Backend

L'authentification backend signifie vérifier le jeton JWT reçu de Cognito ou Facebook pour confirmer l'autorité d'accès aux ressources protégées. Après avoir couvert ces fonctionnalités, nous aurons un système de gestion des utilisateurs complet sur AWS. Wow ! Commençons.

#### Mise à jour des informations utilisateur

Tout système de gestion des utilisateurs respectable aura la capacité de changer les attributs des utilisateurs, donc AWS Cognito ne fait pas exception. Le composant React peut être trouvé à `App/src/components/auth/ProfilePage.js`. Notre code Cognito est dans `App/src/api/aws/aws-cognito.js`, cherchez la fonction `updateUserInfo()`.

```
export function updateUserInfo(editedInfo){ const p = new Promise((res, rej)=>{  const attributeList = []  for(let a = 0; a<attrs.length; a++){    if(editedInfo[attrs[a]]){      let attribute = {          Name : attrs[a],          Value : editedInfo[attrs[a]]      }      let x = new CognitoUserAttribute(attribute)      attributeList.push(x)    }  }  const cognitoUser = userPool.getCurrentUser()  cognitoUser.getSession(function(err, result) {      if(result){        cognitoUser.updateAttributes(attributeList, function(err, result) {          if(err){            rej(err)            return          }          cognitoUser.getUserAttributes(function(err, result) {            if(err){              rej(err)              return            }            buildUserObject(cognitoUser)             .then((userProfileObject)=>{              res(userProfileObject)             })          })        });      }    }); }) return p}
```

Nous passons l'objet utilisateur que nous avons obtenu de `buildUserObject()`, mais modifié pour inclure les valeurs mises à jour (dans ce cas, `agentName`). Dans notre promesse, nous créons un tableau `attributeList` vide pour contenir les variables, ce qui ressemble beaucoup à `signUpUser()`. C'est parce qu'il partage le même processus ! Nous parcourons l'objet `editedInfo` et pour chaque attribut, nous créons un objet `CognitoUserAttribute` à ajouter au tableau `attributeList`.

Après tout cela, nous créons un objet `CognitoUser` à partir du `userPool` importé pour rafraîchir la session afin que nous puissions appeler `updateAttributes` avec le tableau `attributeList`. Cela mettra à jour notre utilisateur Cognito avec les derniers attributs, et dans le callback, nous pouvons `getUserAttributes` à nouveau. Avec les attributs mis à jour, nous appelons `buildUserObject` pour une utilisation dans notre application React-Redux. Et c'est tout ! Presque une répétition exacte de `signUpUser()`.

#### Mot de passe oublié

Celui-ci est également très simple. Comme toujours, créez votre `CognitoUser` avec les données de `userData`. Maintenant, nous pouvons appeler `forgotPassword`.

```
export function forgotPassword(email){ const p = new Promise((res, rej)=>{
```

```
   const userData = {     Username: email,     Pool: userPool   }  const cognitoUser = new CognitoUser(userData)
```

```
  cognitoUser.forgotPassword({      onSuccess: function (result) {        res({          cognitoUser: cognitoUser,          thirdArg: this        })      },      onFailure: function(err) {         rej(err)      },      inputVerificationCode: function(data) {         res({            cognitoUser: cognitoUser,            thirdArg: this         })      }  })
```

```
 }) return p}
```

`forgotPassword()` initialise essentiellement le processus et retourne un objet `CognitoUser` à utiliser dans React-Redux. Dans l'objet de callback, nous utilisons uniquement `onSuccess` et `onFailure`. `inputVerificationCode` n'est pas utilisé ici comme il l'est dans la [documentation Github (voir le cas 12)](https://github.com/aws/amazon-cognito-identity-js) puisque nous voulons créer une interface plus joli au lieu d'utiliser `prompt()` pour demander une entrée. Dans `onSuccess`, nous retournons CognitoUser à notre composant React car nous voulons que la page de réinitialisation du mot de passe contienne des informations pré-remplies (par exemple, `email`). Lorsque le nouveau mot de passe est soumis, `confirmPassword()` doit simplement accepter un `PIN`, un `password` et la déclaration `this` de l'appel API AWS. Voici à quoi cela ressemble dans l'application React-Redux, depuis `App/src/components/Auth/ResetPassword.js`.

```
verifyPin(){  if(this.props.password == this.props.confirm_password){     this.state.cognitoUserPackage.cognitoUser       .confirmPassword(this.state.pin, this.state.password, this.state.cognitoUserPackage.thirdArg)     setTimeout(()=>{       browserHistory.push("/auth/login")     }, 500)  } }
```

Et c'est tout ce qu'il y a à faire pour réinitialiser un mot de passe — Pas trop compliqué, pas beaucoup de code.

#### Déconnexion de l'utilisateur

Déconnecter les utilisateurs est vraiment simple. Nous appelons `getCurrentUser()` pour instancier notre objet `CognitoUser` afin que nous puissions utiliser sa fonction `signOut()`. Maintenant, votre utilisateur est déconnecté !

```
export function signOutUser(){ const p = new Promise((res, rej)=>{  const cognitoUser = userPool.getCurrentUser()  cognitoUser.signOut() }) return p}
```

Comment exécutons-nous cela depuis l'UI ? Dans notre modèle React-Redux, le routage de l'application est géré par `react-router` tandis que l'état de l'application est géré par Redux. Nous devons combiner les deux pour intégrer l'authentification visuelle de l'utilisateur. Nos objectifs ici sont :

> — Afficher différents écrans pour les visiteurs authentifiés ou non authentifiés

> — Restreindre l'accès à l'application aux visiteurs non autorisés

D'accord, c'est parti. Observons d'abord notre état Redux exprimé dans `App/src/reducers/AuthReducer.js`. Notre modèle d'état ressemble à ceci :

```
const INITIAL_STATE = {  authenticated: false,  user: null}
```

Lorsque nous nous sommes connectés, nous avons défini l'état Redux `authenticated` à true, et `user` à la valeur de retour de `buildUserObject()` dans `App/src/api/aws/aws-cognito.js`. Ainsi, `INITIAL_STATE.authenticated` sera utilisé comme vérification universellement dans notre application pour déterminer si l'utilisateur est authentifié. Dans notre modèle d'application, nous accédons à cette variable d'état Redux en tant que `this.props.authenticated`. Donc, dans notre composant de menu latéral situé à `App/src/components/SideMenu/SideMenu.js`, trouvez ce clip de code :

```
<div id='mainview' style={comStyles(this.props.sideMenuVisible).mainview}>        <SideHeader />        <SideOption text='Accueil' link='/' />        {           this.props.authenticated           ?           <SideOption text='Déconnexion' link='/auth/signout' />           :           <SideOption text='Connexion' link='/auth/login' />        }</div>
```

Après `<SideOption text='Accueil' link='/' />`, à l'intérieur des accolades { }, nous avons une opération ternaire (aka opérateur conditionnel). Cela vérifiera si le premier argument `this.props.authenticated` est vrai, et si vrai, affichera `<SideOption text='Déconnexion' link='/auth/signout' />`. Si faux, affichera `<SideOption text='Connexion' link='/auth/login' />`. Et voilà ! Différentes vues pour les visiteurs authentifiés et non authentifiés.

Ensuite, allez au code exprimant notre `react-router` situé à `App/src/index.js` et trouvez ce code :

```
<Route path='/' component={App}>        <IndexRoute component={Home} />        <Route path='auth'>          <Route path='login' component={Login}></Route>          <Route path='signup' component={SignUp}></Route>          <Route path='signout' component={SignOut}></Route>          <Route path='verify_account' component={VerifyAccount}></Route>          <Route path='forgot_password' component={ResetPassword}></Route>          <Route path='authenticated_page' component={RequireAuth(AuthenticatedPage)}></Route>        </Route></Route>
```

Un rapide aperçu de l'arborescence des URL de notre application. À `[http://ourApp.com/](http://ourApp.com/)` nous allons au composant Home représenté par `App/src/components/home.js`. À `[http://ourApp.com/auth/login](http://ourApp.com/auth/login)` se trouve le composant Login représenté par `App/src/components/Auth/Login.js`. Mais à `[http://ourApp.com/auth/authenticated_page](http://ourApp.com/auth/authenticated_page)` nous avons cette route légèrement différente

```
<Route path='authenticated_page' component={RequireAuth(AuthenticatedPage)}></Route>
```

Cette route a `RequireAuth()` enveloppant le composant `AuthenticatedPage`. Si nous allons à RequireAuth() à App/src/components/auth/RequireAuth.js, nous trouvons un autre composant, mais sans HTML généré (c'est-à-dire sans UI). Il s'agit d'un composant d'ordre supérieur (HOC) qui ajoute uniquement des fonctionnalités. Dans ce cas, le HOC vérifie si la variable d'état Redux `this.props.authenticated` est vraie. Si elle n'est pas vraie, nous redirigeons simplement l'URL vers un autre chemin d'URL (dans ce cas, `[http://ourApp.com/auth/login](http://ourApp.com/auth/login).)`[).](http://ourApp.com/auth/login).) Terminé, c'est le vérificateur d'authentification !

```
componentWillMount(){   if(!this.props.authenticated){    browserHistory.push('/auth/login')   }}
```

Maintenant, retournez à `App/src/index.js` pour implémenter la vérification d'authentification. Nous enveloppons simplement le composant visuel à l'intérieur de notre HCO non visuel comme une fonction :

```
<Route path='authenticated_page' component={RequireAuth(AuthenticatedPage)}></Route>
```

Et c'est le deuxième objectif terminé. La partie finale est notre HCO de déconnexion à usage général. Allez à `App/src/components/auth/SignOut.js` et trouvez ce code :

```
componentWillMount(){    signOutUser()  // signoutLandlord() est une fonction de `actions` provenant de index.js  this.props.logoutUserFromReduxState()  setTimeout(()=>{   browserHistory.push('/auth/login')  }, 500) }
```

La fonction `signOutUser()` est celle que nous avons écrite dans `App/src/api/aws/aws-cognit.js`. Ensuite, `this.props.logoutUserFromReduxState()` définit notre variable d'état Redux `authenticated` à false. Enfin, nous changeons l'adresse URL et la vue de l'application en utilisant `browserHistory.push('/auth/login')` après une demi-seconde (afin que nous puissions afficher un message d'au revoir).

Et c'est tout ! Vous pouvez maintenant contrôler chaque vue visuelle de votre application en gardant à l'esprit l'authentification ! Continuons avec la partie suivante.

#### Récupérer l'utilisateur depuis le stockage local

Nous ne voulons pas que nos utilisateurs doivent se reconnecter à chaque visite de l'application web. Idéalement, nous voulons que leur connexion soit enregistrée et qu'ils soient connectés automatiquement à chaque visite jusqu'à ce qu'ils se déconnectent. Comme il est peu sécurisé d'enregistrer le mot de passe d'un utilisateur, nous enregistrerons plutôt le jeton JWT. Cela est en fait géré pour nous par AWS Cognito. Allez à `App/src/components/Auth/Login.js` et trouvez les lignes de code suivantes :

```
componentDidMount(){  const savedEmail = localStorage.getItem('User_Email')  if(savedEmail){   this.setState({    email: savedEmail   })  }  retrieveUserFromLocalStorage()   .then((data)=>{    this.props.setUserToReduxState(data)   }) }
```

La fonction `componentDidMount()` sera exécutée une fois après que le composant soit monté sur la page web, ce qui est le moment où nous voulons vérifier si un utilisateur a déjà une connexion enregistrée. Nous pouvons ignorer la première partie, qui vérifie simplement un email enregistré et le définit dans l'état du composant React. La partie importante ici est `retrieveUserFromLocalStorage()`, qui retourne un `userProfileObject` que nous pouvons enregistrer dans l'état Redux. Rappelez-vous que le `userProfileObject` est utilisé par l'application web comme une représentation de qui est l'utilisateur, et de tous ses attributs tels que le nom, l'âge, la taille, etc. Direct, alors regardons le contenu : la fonction AWS. Allez à `App/src/api/aws/aws-cognito.js` et trouvez la fonction `retrieveUserFromLocalStorage()`.

```
export function retrieveUserFromLocalStorage(){ const p = new Promise((res, rej)=>{     const cognitoUser = userPool.getCurrentUser();     if (cognitoUser != null) {         cognitoUser.getSession(function(err, session) {             if (err) {                rej(err)                return             }             localStorage.setItem('user_token', session.getAccessToken().getJwtToken());             const loginsObj = {                 [USERPOOL_ID] : session.getIdToken().getJwtToken()             }         AWS.config.credentials = new AWS.CognitoIdentityCredentials({                 IdentityPoolId : IDENTITY_POOL_ID,                 Logins : loginsObj             })             AWS.config.credentials.refresh(function(){              console.log(AWS.config.credentials)              res(buildUserObject(cognitoUser))             })         });     }else{      rej('Échec de la récupération de l\'utilisateur depuis localStorage')     } }) return p}
```

Alors, que se passe-t-il ici ? Tout d'abord, nous créons un objet `CognitoUser` en utilisant le `userPool` importé depuis `aws_profile.js`. Cependant, cette fois, nous utilisons la fonction `getCurrentUser()` qui récupérera depuis la mémoire de la session précédente — une fonctionnalité utile que AWS Cognito gère pour nous ! Si nous recevons une valeur non nulle de `getCurrentUser()`, alors nous pouvons supposer que c'est un objet `CognitoUser` valide et appeler `getSession()` pour accéder aux dernières variables de session. La variable qui nous intéresse est le jeton JWT dans `session.getAccessToken().getJwtToken()` que nous enregistrerons dans `localStorage` et placerons dans notre `loginsObj` (Rappelez-vous de la Partie 2, Connexion). Cela enregistrera notre connexion auprès des Identités fédérées. Maintenant, tout ce que nous avons à faire est d'utiliser cela pour définir nos informations d'identification AWS et les rafraîchir avant d'appeler `buildUserObject()` et de le retourner à l'application React-Redux. Avec le `userProfileObject` qui est retourné de `buildUserObject()`, nous sommes connectés !

#### Authentification Backend

D'accord, tout ce côté front-end est génial, mais pour avoir le package complet, nous avons également besoin de l'authentification backend. Supposons que nous avons une ressource dans notre backend que nous voulons montrer uniquement aux utilisateurs connectés. Pour demander cette ressource, nous n'utiliserons pas un email+mot de passe car cela serait peu sécurisé d'envoyer le mot de passe pour chaque demande. Au lieu de cela, nous utiliserons le jeton JWT que Cognito nous a fourni. Nous décryptons simplement le jeton sur le backend et le vérifions par rapport aux références de jeton Cognito. Passons en revue comment faire cela en tant que processus général :

J'ai inclus le code pour ce backend écrit en NodeJS, mais le processus général fonctionne avec n'importe quel backend. Voir `/Bonus_Backend/` pour le code. Maintenant, commençons le processus au frontend (`/App/`).

Tout d'abord, nous envoyons le jeton JWT depuis notre client frontend dans un en-tête HTTP. La bibliothèque que nous utilisons pour les requêtes `http` est `axios`, mais vous pouvez utiliser celle que vous préférez tant que vous savez comment inclure un attribut d'en-tête. Dans axios, vous placez simplement un objet avec une clé-valeur d'en-têtes comme 3ème argument de la fonction `POST`. Trouvez cela en action à `App/src/api/myAPI.js`.

```
const API_URL = '24.74.347.34' // votre IP backend
```

```
export function getBackendResource(){  const jwtConfig = {headers: {"jwt": localStorage.getItem("user_token")}}   const p = new Promise((res, rej)=>{    axios.post(API_URL+"/auth_test", null, jwtConfig)     .then((data)=>{      res(data.data)     })     .catch((err)=>{       rej(err)     })   })   return p}
```

Ensuite, nous devons télécharger l'ensemble JWT que AWS Cognito nous fournit. Allez à la page Cognito dans la console AWS et trouvez votre région (par exemple, `us-east-1`) et votre userPoolId (par exemple, `us-east-1_Fa9dl8sWt`). Utilisez-les maintenant pour remplacer les espaces réservés ci-dessous, et suivez le lien.

```
https://cognito-idp.{region}.amazonaws.com/{userPoolId}/.well-known/jwks.json
```

Vous devriez arriver à une page avec un texte comme ceci :

```
{     "keys":[        {           "alg":"RS256",         "e":"AQAB",         "kid":"I7Kw/O0QymLQ8A0pPaXNcv5je7BNYXMCW1HdziUTyrQ=",         "kty":"RSA",         "n":"uIqZqU64ytLpQr3J86NMpjxZBRubRzovkQv22oAeHoxO_w4EZuvEeodCV7WxVatHwcVyH0VrkRsqcoigajJO5Xz3s-Ttz_ozhE8wP-BI3DUPOUNtGiKZirNLf9jluScrCUsyyim2UrF4ub-hsxGSt32GFRMfqrkvz0Ral4K4oeIiBNnX8cu_pbSlDgriBLAh8ago41XhqqSFtWwlP-x_KHJc13RBgETj7HOfEm5tr6ibJlMazL3FOoXehfXQw9Yr0752A2hTKAB8reUJXuAwcyTUa8ZEO6IcnhQiaPmIgltxdm-SHdoPqwR_SQxYzZfQzU9uE78ogWT-xP29Gr08Xw",         "use":"sig"      },      {           "alg":"RS256",         "e":"AQAB",         "kid":"fxyn6hg0ziTNer+mBzqmxqGe38uh4neQPorXo3GAa/s=",         "kty":"RSA",         "n":"hMAECS0ALyFaP7OY4ZN5SXqPpkKOdp_RfNAmeCXhK98rmEnD_9Zzqb5oVviZZoqQ5xEZQBRR7a2JOZxL_JZWX7ObteHMSfNZywk8E9FN4XPMJxStZk5JSceKBd5SPYdLzTR58LFMg4OKONA5aJ1sYUu11zq6yMdUBvEJlwBjBrH4lfSkJ_jg4zSeKxsRcM72oAQ_yCnzO5giPoMjyY8VtqCj7NW_7njyQ-bD1WiGaNCkgBxWwYL_13zCxMJxNopa2vHoca0xn9bct-ysS8zIaB3DjNo_8-GGp_HJ4kNW0TczcILtl4mrl81srGzulvuK-mGF0T31IDY-tZWS3IgQYQ",         "use":"sig"      }   ]}
```

Enregistrez cela dans son propre fichier `jwt_set.json` dans votre backend (`Example_Backend/App/api/jwt_set.json`) afin qu'il puisse être référencé par votre processus d'authentification. Le processus d'authentification (fonction) doit s'exécuter avant l'accès à toute ressource protégée. Le processus d'authentification ressemble à ce code trouvé dans `Example_Backend/App/api/authCheck.js` :

```
const jwt = require('jsonwebtoken');const jwkToPem = require('jwk-to-pem');const jwt_set = require('./jwt_set.json')
```

```
const userPool_Id = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_6i5p2Fwao"
```

```
const pems = {}for(let i = 0; i<jwt_set.keys.length; i++){ const jwk = {  kty: jwt_set.keys[i].kty,  n: jwt_set.keys[i].n,  e: jwt_set.keys[i].e } // convertir l'objet jwk en PEM const pem = jwkToPem(jwk) // ajouter PEM à l'objet pems, avec le kid comme identifiant pems[jwt_set.keys[i].kid] = pem}
```

```
exports.authCheck = function(req, res, next){ const jwtToken = req.headers.jwt ValidateToken(pems, jwtToken)   .then((data)=>{    console.log(data)    next()   })   .catch((err)=>{    console.log(err)    res.send(err)   })}
```

```
function ValidateToken(pems, jwtToken){ const p = new Promise((res, rej)=>{  const decodedJWT = jwt.decode(jwtToken, {complete: true})  // rejeter si ce n'est pas un jeton JWT valide  if(!decodedJWT){   console.log("Not a valid JWT token")   rej("Not a valid JWT token")  }  // rejeter si ISS ne correspond pas à notre userPool Id  if(decodedJWT.payload.iss != userPool_Id){   console.log("invalid issuer")   rej({    message: "invalid issuer",    iss: decodedJWT.payload   })  }  // Rejeter le jwt s'il ne s'agit pas d'un 'Access Token'  if (decodedJWT.payload.token_use != 'access') {         console.log("Not an access token")         rej("Not an access token")     }     // Obtenir le `kid` du jwtToken à partir de l'en-tête  const kid = decodedJWT.header.kid  // vérifier s'il y a un pem correspondant, en utilisant le `kid` comme identifiant  const pem = pems[kid]  // s'il n'y a pas de pem correspondant pour ce `kid`, rejeter le jeton  if(!pem){   console.log('Invalid access token')   rej('Invalid access token')  }  console.log("Decoding the JWT with PEM!")  // vérifier la signature du JWT token pour s'assurer qu'il provient vraiment de votre User Pool  jwt.verify(jwtToken, pem, {issuer: userPool_Id}, function(err, payload){   if(err){    console.log("Unauthorized signature for this JWT Token")    rej("Unauthorized signature for this JWT Token")   }else{    // si le payload existe, alors le jeton est vérifié !    res(payload)   }  }) }) return p}
```

D'accord, c'est un peu long, décomposons cela un par un. Tout d'abord, nous importons les dépendances nodeJS que nous voulons et les installons.

```
$ npm install jsonwebtoken --save$ npm install jwk-to-pem --save
```

Et ensuite, nous incluons le `jwt_set.json` ainsi que notre Identity Pool Id. Cela fait 3 dépendances et 1 constante.

```
const jwt = require('jsonwebtoken');const jwkToPem = require('jwk-to-pem');const jwt_set = require('./jwt_set.json')
```

```
const userPool_Id = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_6i5p2Fwao"
```

Nous créons 1 constante supplémentaire appelée `pems`, qui est créée par la boucle `for` exécutée lors du chargement du fichier.

```
const pems = {}for(let i = 0; i<jwt_set.keys.length; i++){ // prendre la clé jwt_set et créer un objet jwk pour la conversion en PEM const jwk = {  kty: jwt_set.keys[i].kty,  n: jwt_set.keys[i].n,  e: jwt_set.keys[i].e } // convertir l'objet jwk en PEM const pem = jwkToPem(jwk) // ajouter PEM à l'objet pems, avec le kid comme identifiant pems[jwt_set.keys[i].kid] = pem}
```

À un niveau élevé, ce qui se passe, c'est que pour chaque clé dans `jwt_set.json`, nous créons un objet `PEM` pour être la valeur du `kid` de cette clé jwt_set. Nous n'avons pas besoin de savoir exactement ce qui se passe, mais en gros, nous créons un `PEM` qui peut être utilisé pour correspondre au `kid` du `jwt` provenant de l'en-tête des requêtes http entrantes comme moyen de vérifier l'authentification. Si vous pensez que vous devez savoir exactement ce que signifient ces termes, consultez [The Anatomy of a JSON Web Token](https://scotch.io/tutorials/the-anatomy-of-a-json-web-token) par Chris Sevilleja.

En tout cas, en continuant, nous avons la fonction `authCheck` qui valide le jeton jwt entrant de l'en-tête en utilisant `ValidateToken()`. Très simple.

```
exports.authCheck = function(req, res, next){ const jwtToken = req.headers.jwt ValidateToken(pems, jwtToken)   .then((data)=>{    console.log(data)    next()   })   .catch((err)=>{    console.log(err)    res.send(err)   })}
```

`authCheck()` est utilisé ailleurs dans votre backend comme la fonction appelée avant d'accéder à une ressource protégée. Pour un backend `NodeJS` `Express`, cela ressemblerait à ceci :

```
const authCheck = require('./api/authCheck').authCheck
```

```
// route d'authentificationapp.get('/auth_test', authCheck, function(req, res, next){ console.log("Passed the auth test!") res.send("Nice job! Your token passed the auth test!")});
```

Enfin, regardons `ValidateToken()`, qui peut être décomposé en 6 parties plus petites. Passez la constante `pems` et le `jwt` de l'en-tête de la requête `http`. Suivez maintenant les 6 étapes du processus de validation et si toutes passent, le jeton JWT est accepté ! La promesse sera résolue et `authCheck()` permettra l'accès à notre ressource protégée.

```
function ValidateToken(pems, jwtToken){ const p = new Promise((res, rej)=>{
```

```
  // PARTIE 1 : Décoder le jeton JWT  const decodedJWT = jwt.decode(jwtToken, {complete: true})
```

```
  // PARTIE 2 : Vérifier si c'est un jeton JWT valide  if(!decodedJWT){   console.log("Not a valid JWT token")   rej("Not a valid JWT token")  }
```

```
  // PARTIE 3 : Vérifier si l'ISS correspond à notre userPool Id  if(decodedJWT.payload.iss != userPool_Id){   console.log("invalid issuer")   rej({    message: "invalid issuer",    iss: decodedJWT.payload   })  }
```

```
  // PARTIE 4 : Vérifier que le jwt est un 'Access Token' AWS  if (decodedJWT.payload.token_use != 'access') {     console.log("Not an access token")     rej("Not an access token")  }
```

```
  // PARTIE 5 : Faire correspondre le PEM au KID de la requête  const kid = decodedJWT.header.kid  const pem = pems[kid]  if(!pem){   console.log('Invalid access token')   rej('Invalid access token')  }  console.log("Decoding the JWT with PEM!")
```

```
  // PARTIE 6 : Vérifier la signature du JWT token pour s'assurer qu'il provient vraiment de votre User Pool  jwt.verify(jwtToken, pem, {issuer: userPool_Id}, function(err, payload){   if(err){    console.log("Unauthorized signature for this JWT Token")    rej("Unauthorized signature for this JWT Token")   }else{    // si le payload existe, alors le jeton est vérifié !    res(payload)   }  }) }) return p}
```

Donc, voici notre vérificateur d'authentification backend. Pour l'intégrer, allez dans `Example_Backend/App/router.js` où nous recevons les requêtes http entrantes.

```
// routesconst Authentication = require('./routes/auth_routes');
```

```
// middleware du routeurconst authCheck = require('./api/authCheck').authCheck
```

```
module.exports = function(app){ // Routes liées à l'authentification app.get('/auth_test', authCheck, Authentication.authtest);}
```

Tout ce que nous avons à faire est de l'ajouter en tant que 2ème argument à notre route ExpressJS. Si vous avez un backend différent, le même processus général s'applique.

Et c'est tout, l'authentification backend utilisant notre même environnement AWS Cognito. Quelle puissance !

#### Conclusion

Félicitations pour avoir suivi ce long tutoriel sur AWS Cognito et les Identités fédérées ! En complétant cela jusqu'à la fin, vous pouvez maintenant profiter d'une gestion des utilisateurs de premier ordre conçue par le plus grand fournisseur de services cloud au monde. Une grande partie des fonctionnalités que vous recevez avec AWS prendrait des semaines et beaucoup de connaissances expertes à implémenter si vous deviez créer un système personnalisé. De plus, il n'y a aucune garantie que vous implémenteriez un système de gestion des utilisateurs personnalisé correctement, sans exposer vos utilisateurs à des failles et des trous de sécurité. En utilisant Amazon, vous pouvez dormir tranquille en sachant que tout cela est pris en charge pour vous par une entreprise Internet de plusieurs milliards de dollars.

Donc, nous y voilà : Un système de gestion des utilisateurs complet prêt pour une utilisation dans le monde réel. Si vous pensez avoir bénéficié ou appris beaucoup de cette série de tutoriels, veuillez partager et vous abonner ! Je publierai plus de tutoriels pratiques sur AWS dans les mois à venir, alors assurez-vous de rester à l'écoute. À la prochaine !

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Configuration initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [Fonctionnalités principales](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour un système complet](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)