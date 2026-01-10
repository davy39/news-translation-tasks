---
title: Gestion des utilisateurs avec AWS Cognito — (2/3) La fonctionnalité principale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-02T18:30:20.000Z'
originalURL: https://freecodecamp.org/news/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ubdzj9K3MrbMb0Ep0UV3IA.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Gestion des utilisateurs avec AWS Cognito — (2/3) La fonctionnalité principale
seo_desc: 'By Kangze Huang

  The Complete AWS Web Boilerplate — Tutorial 1B



  Main Table of Contents Click Here

  Part A: Initial Setup

  Part B: The Core Functionality

  Part C: Last Steps to Full Fledged


  Download the Github here.

  The Javascript Cognito SDK

  Great! Yo...'
---

Par Kangze Huang

#### Le modèle complet AWS Web — Tutoriel 1B

![Image](https://cdn-media-1.freecodecamp.org/images/d7d793oXovpHSua0AKqYS5ebesZR56-i7gXF)

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Configuration initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [La fonctionnalité principale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour une solution complète](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

Téléchargez le projet Github [ici](https://github.com/kangzeroo/Kangzeroos-AWS-Cognito-Boilerplate).

### Le SDK JavaScript Cognito

Super ! Vous ne devriez être ici que si vous avez terminé la configuration initiale pour Cognito et les identités fédérées. Maintenant que tout est configuré, il est temps de parcourir le code JavaScript. Téléchargez le [modèle Kangzeroo sur Github](https://github.com/kangzeroo/Kangzeroos-ES6-React-Redux-Boilerplate) et assurez-vous d'entrer dans la branche Cognito où nous allons travailler.

```
$ git clone https://github.com/kangzeroo/Kangzeroos-Complete-AWS-Web-Boilerplate.git$ cd Kangzeroos-Complete-AWS-Web-Boilerplate$ git checkout Cognito$ cd App
```

Le modèle utilise la [bibliothèque Amazon-Cognito-Identity-JS trouvée sur github](https://github.com/aws/amazon-cognito-identity-js). Cette bibliothèque facilite l'utilisation programmatique d'AWS Cognito, mais les mêmes fonctionnalités peuvent être trouvées dans le SDK natif `aws-sdk`. Alors, installons nos dépendances et chargeons l'application.

```
$ npm install$ npm run start
```

#### Configuration du profil AWS

Naviguez vers `App/src/components/Auth` où nous trouverons tous les composants React liés à l'authentification Cognito. Oui, ce tutoriel utilise React, mais vous pouvez facilement appliquer les mêmes leçons à d'autres frameworks JS. Allez à `App/src/api/aws/aws-cognito.js` où se trouve la majeure partie du code AWS Cognito. Examinons les dépendances et comment nous pouvons configurer notre propre profil AWS.

```
// aws-cognito.js
```

```
import { CognitoUserPool, CognitoUserAttribute, CognitoUser, AuthenticationDetails, CognitoIdentityCredentials, WebIdentityCredentials } from 'amazon-cognito-identity-js';
```

```
import { userPool, LANDLORD_USERPOOL_ID, LANDLORD_IDENTITY_POOL_ID, TENANT_IDENTITY_POOL_ID } from './aws_profile'
```

```
import uuid from 'node-uuid'
```

Nous importons une variété de fonctions de `amazon-cognito-identity-js` ainsi que de `./aws_profile.js`. Les fonctions de `amazon-cognito-identity-js` seront expliquées au fur et à mesure. Ce que nous voulons nous concentrer est le contenu de `./aws_profile.js`. C'est ici que nous plaçons nos paramètres Cognito tels que notre userPoolId et AppIds. Examinons `./aws_profile.js`.

```
import { CognitoUserPool } from 'amazon-cognito-identity-js';import 'amazon-cognito-js'
```

```
const REGION = "us-east-1"const USER_POOL_ID = 'us-east-1_6i5p2Fwao'const CLIENT_ID = '5jr0qvudipsikhk2n1ltcq684b'
```

```
AWS.config.update({ region: REGION})
```

```
const userData = {    UserPoolId : USER_POOL_ID,    ClientId : CLIENT_ID}
```

```
export const userPool = new CognitoUserPool(userData);
```

```
export const USERPOOL_ID = 'cognito-idp.'+REGION+'.amazonaws.com/'+USER_POOL_ID
```

```
export const IDENTITY_POOL_ID = 'us-east-1:65bd1e7d-546c-4f8c-b1bc-9e3e571cfaa7'
```

Ici, nous configurons notre région AWS `region`, l'`USER_POOL_ID` Cognito et l'`CLIENT_ID` de l'application Cognito. Nous créons également un objet `CognitoUserPool` à partir de notre `USER_POOL_ID` et `CLIENT_ID`, qui contient la majeure partie de nos fonctions Cognito. `CognitoUserPool` dispose de fonctions pour tout, allant de la réinitialisation des mots de passe à l'authentification d'un nouvel utilisateur. Nous créons `CognitoUserPool` ici afin de ne pas avoir à le réinstancier pour chaque fonction. Nous configurons également notre `USERPOOL_ID`, qui est une URL requise dans certaines fonctions Cognito, et composée de `USER_POOL_ID` et de `region`. Enfin, nous exportons également un ARN de notre pool d'identités fédérées, qui est également requis dans certaines fonctions Cognito. En résumé, ceci est juste une configuration et vous n'avez qu'à copier et coller vos propres valeurs.

Dernière étape de la configuration, nous allons créer un tableau de nos attributs utilisateur en haut de notre fichier `aws_cognito.js`. Remplissez le tableau avec vos propres attributs utilisateur, et n'oubliez pas de préfixer les attributs personnalisés avec `custom:` pour `const attrs`. `const landlordAttrs` ne nécessite pas le préfixe `custom:`.

```
// nous créons un tableau de tous les attributs, sans le préfixe `custom:` // Cela sera utilisé pour construire l'objet React-Redux en JS simple, d'où aucune exigence de nom liée à AWS Cognito
const landlordAttrs = ["email", "agentName", "id"]
```

```
// nous créons un tableau de tous nos attributs souhaités pour la modification, et nous parcourons ce tableau pour accéder au nom de la clé. // Cela sera utilisé pour les exigences de nom liées à AWS Cognito
const attrs = ["custom:agentName"]
```

Maintenant, après la configuration et avant de commencer le code réel, je devrais dire que ce modèle est complet. Vous n'avez pas nécessairement besoin de savoir ce qui se passe en coulisses. Vous pouvez simplement utiliser ce modèle et toutes les fonctionnalités fonctionneront dès le départ : inscription, connexion, vérification par e-mail, réinitialisation du mot de passe, modification des attributs utilisateur et connexions enregistrées utilisant JWT. Notez que tout e-mail que vous utilisez dans Cognito doit être vérifié par AWS, jusqu'à ce que vous [demandiez à quitter le bac à sable AWS SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html) (auquel cas vous pourrez envoyer des messages à n'importe quel e-mail). Si vous êtes ici juste pour le modèle fonctionnel, c'est aussi loin que vous devez lire. Si vous voulez savoir ce qui se passe, continuez à lire !

#### Inscription des utilisateurs

Examinons le premier composant d'authentification appelé `SignUp.js`. Je ne passerai pas de temps à expliquer le côté React des choses, car ce n'est pas le but de ce tutoriel. Trouvez cette fonction :

```
signup(){
```

```
...
```

```
// appel de la fonction AWS Cognito que nous avons nommée `signUpUser`    signUpUser(this.state)     .then(({email})=>{      // si succès, alors sauvegarder l'email dans localStorage pour pré-remplir le formulaire d'email sur les écrans de connexion et de vérification de compte      localStorage.setItem('User_Email', email)      // rediriger vers l'écran de vérification de compte      browserHistory.push('/auth/verify_account')     })
```

```
...
```

```
}
```

Ici, nous appelons `signUpUser()` et passons l'état du composant React, qui ressemble à ceci :

```
this.state = {   email: "",   agentName: "",   password: "",   confirmPassword: "",   errorMessage: null,   loading: false}
```

Nous n'utiliserons que les attributs email et password de l'état lorsque nous les passerons à `signUpUser()`. La fonction `signUpUser()` se trouve dans `App/src/api/aws/aws-cognito.js`.

```
export function signUpUser({email, agentName, password}){ const p = new Promise((res, rej)=>{
```

```
  const attributeList = []
```

```
  const dataEmail = {      Name : 'email',      Value : email  }  const dataAgentName = {      Name : 'custom:agentName',      Value : agentName  }
```

```
  const attributeEmail = new CognitoUserAttribute(dataEmail)  const attributeAgentName = new CognitoUserAttribute(dataAgentName)
```

```
  attributeList.push(attributeEmail, attributeAgentName)
```

```
  userPool.signUp(email, password, attributeList, null, function(err, result){      if (err) {          rej(err)          return      }      res({email})  }) }) return p}
```

`signUpUser()` accepte un objet qui doit avoir 3 attributs : `email`, `password` et `agentName`. Afin de l'enregistrer comme un attribut de notre utilisateur Cognito, nous devons créer un objet `CognitoUserAttribute` pour chacun. Nous faisons cela en créant un objet `dataEmail` et `dataAgentName` avec le nom de l'attribut et sa valeur. Ces objets seront passés à la fonction `CognitoUserAttribute` qui les convertit en objets lisibles par AWS Cognito que nous avons intitulés `attributeEmail` et `attributeAgentName`. Notez que `dataAgentName.name` est préfixé avec `custom:` pour spécifier à Cognito que `agentName` est un attribut utilisateur personnalisé. Maintenant que nous avons nos objets `CognitoUserAttribute`, nous allons les pousser dans le tableau `attributeList`.

La ligne de code suivante est ce qui enregistre réellement ce nouvel utilisateur. Nous utilisons l'objet `userPool` que nous avons importé de `./aws_profile.js` et appelons sa fonction `signUp`. Les trois premiers arguments sont l'identifiant unique `email`, `password`, et le tableau `attributeList`. Le quatrième argument est null, et le cinquième est le callback. Dans le callback, nous rejetons la promesse si une erreur s'est produite, et si aucune erreur, alors nous résolvons la promesse. Dans le modèle, nous retournons l'email pour qu'il soit sauvegardé dans localStorage dans notre composant React, mais ce n'est pas obligatoire. Vous pouvez résoudre la promesse avec rien. Le nouvel utilisateur Cognito a été créé. Mais pour utiliser le nouvel utilisateur, il doit pouvoir vérifier son compte. L'infrastructure AWS pour cela a déjà été configurée, donc maintenant tout ce que nous avons à faire est de parcourir le code de la fonction de vérification.

#### Vérification du compte

Nous ne passerons pas trop de temps sur cette partie du code, donc je vais d'abord expliquer le composant React-Redux à un niveau élevé, puis entrer dans les détails avec le code AWS.

À un niveau élevé, ce qui se passe après qu'un utilisateur s'inscrit est qu'il est redirigé par `react-router` vers l'URL `/verify_account` où le composant `App/src/components/Auth/VerifyAccount.js` apparaît. Lorsque le composant est monté, le champ email est automatiquement rempli en accédant au `localStorage`. Ensuite, nous avons la possibilité d'entrer le code PIN de vérification envoyé à l'email de l'utilisateur, ou de choisir de réinitialiser et renvoyer le code PIN de vérification. Examinons la fonction `resetVerificationPIN()` dans `App/src/api/aws/aws-cognito.js`.

```
export function resetVerificationPIN(email){ const p = new Promise((res, rej)=>{  const userData = {   Username: email,   Pool: userPool  }  const cognitoUser = new CognitoUser(userData)  cognitoUser.resendConfirmationCode(function(err, result) {         if (err) {          rej(err)          return         }         res()     }) }) return p}
```

Lorsque nous appelons cette fonction, nous devons seulement passer l'email. Cognito vérifiera automatiquement que l'email existe et générera une erreur s'il n'existe pas. Comme dans `SignUp.js`, nous créons un objet `userData` contenant l'email de notre utilisateur et le userPool importé de `./aws_profile.js` afin de créer un objet `CognitoUser` valide. En utilisant l'objet `CognitoUser`, nous pouvons appeler `resendConfirmationCode()` pour que le code PIN soit envoyé à nouveau. Et c'est tout !

Maintenant, examinons la fonction `verifyUserAccount()` :

```
export function verifyUserAccount({email, pin}){ const p = new Promise((res, rej)=>{  const userData = {   Username: email,   Pool: userPool  }  const cognitoUser = new CognitoUser(userData)  cognitoUser.confirmRegistration(pin, true, function(err, result) {         if (err) {             console.log(err);             rej(err)             return;         }         if(result == "SUCCESS"){          console.log("Compte vérifié avec succès !")          cognitoUser.signOut()          res()         }else{          rej("Impossible de vérifier le compte")         }     }) }) return p}
```

`verifyUserAccount()` accepte un objet comme seul argument, contenant 2 attributs essentiels `email` et `pin`. Nous créons un autre objet `userData` pour créer un `CognitoUser` afin d'appeler la fonction `confirmRegistration()`. Dans `confirmRegistration()`, nous passons le `pin`, `true`, et un callback. Si la confirmation réussit, alors nous déconnectons le cognitoUser (afin que nous puissions nous reconnecter et rafraîchir l'utilisateur). Si elle échoue, alors nous rejetons la promesse. Plutôt facile puisque le SDK a abstrait beaucoup de détails. En cas de vérification réussie, le composant React doit vous rediriger vers la page de connexion.

#### Connexion des utilisateurs

Examinons le composant suivant `App/src/components/Auth/Login.js`. Trouvez la fonction suivante :

```
signin(){  this.setState({loading: true})  signInUser({   email: this.state.email,   password: this.state.password  }).then((userProfileObject)=>{   localStorage.setItem('User_Email', this.state.email)   this.props.setUser(userProfileObject)   browserHistory.push('/authenticated_page')  })  .catch((err)=>{   this.setState({    errorMessage: err.message,    loading: false   })  }) }
```

Que se passe-t-il ici ? Tout d'abord, nous appelons la fonction Cognito `signInUser()` pour nous connecter et récupérer les détails de l'utilisateur depuis Cognito. Ensuite, dans la chaîne de promesses, nous sauvegardons l'email de l'utilisateur dans `localStorage` afin de pouvoir définir automatiquement l'email lors de la prochaine connexion. Nous sauvegardons également l'utilisateur dans l'état Redux en utilisant `this.props.setUser()`, qui est une fonction d'action Redux située à `App/src/actions/auth_actions.js`. Nous ne couvrirons pas le côté React-Redux car ce n'est pas le sujet de ce tutoriel. Examinons la fonction AWS Cognito.

Trouvez `signInUser()` à `App/src/api/aws/aws-cognito.js`. Voici à quoi elle ressemble :

```
export function signInUser({email, password}){ const p = new Promise((res, rej)=>{
```

```
  const authenticationDetails = new AuthenticationDetails({   Username: email,   Password: password  })
```

```
  const userData = {   Username: email,   Pool: userPool  }  const cognitoUser = new CognitoUser(userData)
```

```
  authenticateUser(cognitoUser, authenticationDetails)   .then(()=>{    return buildUserObject(cognitoUser)   })   .then((userProfileObject)=>{    res(userProfileObject)   })   .catch((err)=>{    rej(err)   })
```

```
 }) return p}
```

Nous créons un objet `AuthenticationDetails` Cognito contenant l'`email` et le `password` de l'utilisateur. Nous créons également un objet `CognitoUser` pour utiliser sa fonction `authenticateUser()`, mais notez que `authenticateUser()` n'est déclaré nulle part dans la fonction ou en haut de la page où nous listons les dépendances. Cela est dû au fait que `authenticateUser()` est une autre fonction déclarée plus bas dans la page. Une autre fonction déclarée dans la page est `buildUserObject()`, qui prend les attributs de l'utilisateur depuis Cognito et les formate en un objet utilisateur que nous voulons utiliser dans l'état Redux. À la fin de la chaîne de promesses, nous retournons l'objet `userProfileObject` que `buildUserObject()` génère. Parcourons la chaîne de promesses en commençant par `authenticateUser()`.

```
function authenticateUser(cognitoUser, authenticationDetails){ const p = new Promise((res, rej)=>{
```

```
  cognitoUser.authenticateUser(authenticationDetails, {
```

```
         onSuccess: function (result) {             localStorage.setItem('user_token', result.accessToken.jwtToken)             const loginsObj = {                 [USERPOOL_ID]: result.getIdToken().getJwtToken()             }       AWS.config.credentials = new AWS.CognitoIdentityCredentials({                 IdentityPoolId : IDENTITY_POOL_ID,                  Logins : loginsObj             })             AWS.config.credentials.refresh(function(){              console.log(AWS.config.credentials)             })             res()         },
```

```
         onFailure: function(err) {             rej(err)         }
```

```
     })
```

```
 }) return p}
```

`authenticateUser()` prend les arguments `cognitoUser` et `authenticationDetails` et les utilise pour deux choses. `cognitoUser` contient une fonction appelée `authenticateUser()` que nous appellerons pour nous connecter à AWS Cognito. Le premier argument que nous passons est `authenticationDetails` (qui contient l'email + le mot de passe), et le deuxième argument est un objet avec un callback `onSuccess` et `onFailure`. Assez simple, `onFailure` rejettera simplement la chaîne de promesses. `onSuccess` contiendra `result`, qui aura un jeton JWT utilisé pour les authentifications futures sans avoir besoin de saisir un mot de passe. Nous sauvegardons le JWT dans `localStorage` et le récupérons chaque fois que nous en avons besoin (authentification backend pour les ressources ou connexion automatique). Ensuite, nous créons un `loginsObj` qui contient une paire clé-valeur de notre `USER_POOL_ID` et du jeton JWT. Nous passons ce `loginsObj` à une instance de `AWS.config.credentials` en utilisant `new AWS.CognitoIdentityCredentials()`, ainsi que l'`IdentityPoolId`. Ce que cela fait, c'est enregistrer une connexion avec AWS Federated Identities. Rappelez-vous que Federated Identities est utilisé pour gérer les connexions provenant de plusieurs sources, il est donc logique que nous utilisions Federated Identities pour enregistrer un succès de connexion pour chaque connexion.

Après avoir configuré `AWS.config.credentials`, nous pouvons maintenant utiliser l'authentification Cognito pour demander d'autres services Amazon. Bien sûr, ces services doivent être configurés pour autoriser une certaine authentification Cognito (et rejeter d'autres demandes), mais cela sera montré dans les futurs tutoriels sur une base par service. En tout cas, après avoir configuré `AWS.config.credentials`, il est important de rafraîchir les informations d'identification en utilisant `AWS.config.credentials.refresh` afin qu'AWS utilise la dernière que nous venons d'ajouter.

Maintenant, passons à l'étape suivante dans la chaîne de promesses `signInUser()` : `buildUserObject()`.

```
function buildUserObject(cognitoUser){ const p = new Promise((res, rej)=>{  cognitoUser.getUserAttributes(function(err, result) {         if (err) {              rej(err)              return         }         let userProfileObject = {}         for (let i = 0; i < result.length; i++) {           if(result[i].getName().indexOf('custom:') >= 0){              let name = result[i].getName().slice(7, result[i].getName().length)              userProfileObject[name] = result[i].getValue()           }else{              userProfileObject[result[i].getName()] = result[i].getValue()           }         }         res(userProfileObject)     }) }) return p}
```

Tout d'abord, l'objet `cognitoUser` est passé et utilisé pour appeler sa méthode `getUserAttributes()`. Comme toujours, nous rejetons la promesse si une erreur se produit. Si succès, alors nous procédons à la création d'un objet `userProfileObject` vide qui aura une structure correspondant à ce que nous voulons sur notre front-end React-Redux. L'objet `result` que nous obtenons du callback de succès est un tableau d'objets CognitoUserAttribute (rappelons le tableau `AttributeList` de `signUpUser()`). Nous parcourons ce tableau en utilisant une boucle for et obtenons les noms de chaque attribut, en supprimant le préfixe `custom:` si nécessaire. Ensuite, nous incluons également la valeur de l'attribut, et ajoutons la paire clé-valeur à l'objet `userProfileObject`. À la fin de la boucle, nous aurons notre objet `userProfileObject` terminé en JS simple. Nous retournons l'objet `userProfileObject` et complétons la chaîne de promesses `signInUser()`. Observons à nouveau le flux `signInUser()` et observons le flux à un niveau élevé.

```
export function signInUser({email, password}){ const p = new Promise((res, rej)=>{
```

```
const authenticationDetails = new AuthenticationDetails({   Username: email,   Password: password  })
```

```
const userData = {   Username: email,   Pool: userPool  }  const cognitoUser = new CognitoUser(userData)
```

```
authenticateUser(cognitoUser, authenticationDetails)   .then(()=>{    return buildUserObject(cognitoUser)   })   .then((userProfileObject)=>{    res(userProfileObject)   })   .catch((err)=>{    rej(err)   })
```

```
}) return p}
```

Lorsque nous résolvons enfin la promesse `signInUser()`, nous retournons l'objet `userProfileObject` au composant React. Dans le composant React `Login.js`, observez ce que nous faisons après `signInUser()`.

```
signin(){  this.setState({loading: true})  signInUser({   email: this.state.email,   password: this.state.password  }).then((userProfileObject)=>{   localStorage.setItem('User_Email', this.state.email)   this.props.setUser(userProfileObject)   browserHistory.push('/authenticated_page')    })  .catch((err)=>{   this.setState({    errorMessage: err.message,    loading: false   })  }) }
```

Nous sauvegardons l'email de l'utilisateur dans `localStorage` pour une utilisation future, et ajoutons l'objet `userProfileObject` à l'état Redux. Si des erreurs se sont produites dans l'ensemble du processus, elles seront capturées et affichées dans `this.state.errorMessage`. Et c'est tout ! Une note rapide à souligner : `this.props.setUser()` est une action Redux qui définira l'objet `userProfileObject` pour être accessible dans toute l'application Redux, ainsi que basculer un booléen `state.auth.authenticated` à `true`. L'application Redux utilise `state.auth.authenticated` comme moyen de déterminer si une certaine page doit être rendue ou non. Par exemple, nous ne voulons afficher une page de profil utilisateur que si un utilisateur est connecté.

#### Conclusion de la partie 2

Wow, cet article a été long ! Mais nous n'avons pas encore terminé. Il reste quelques sujets à couvrir, notamment `updateUserInfo()`, `forgotPassword()`, `retrieveUserFromLocalStorage()`, `signOutUser()` et l'authentification backend des jetons JWT pour les ressources restreintes. Je vous avais bien dit que c'était un tutoriel AWS COMPLET, n'est-ce pas ? En tout cas, continuez à lire si vous avez l'impression de devoir savoir ce qui se passe sous le capot. N'oubliez pas que vous pouvez arrêter de lire à tout moment et simplement utiliser le modèle tel quel, et il fonctionnera. J'espère que vous avez trouvé cette série utile jusqu'à présent. À bientôt dans la partie 3 de Cognito !

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Configuration initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [La fonctionnalité principale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour une solution complète](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)