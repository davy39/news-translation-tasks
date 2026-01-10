---
title: Comment authentifier votre application React avec Passport.js
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-09-19T22:29:44.000Z'
originalURL: https://freecodecamp.org/news/react-passport-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/passport-react.png
tags:
- name: authentication
  slug: authentication
- name: passportjs
  slug: passportjs
- name: React
  slug: react
seo_title: Comment authentifier votre application React avec Passport.js
seo_desc: 'Authentication is a major part of any serious React application. You need
  to have a good and reliable way to authenticate your users in your developer tool
  belt.

  There are dozens of authentication solutions to choose from today, many of which
  come wi...'
---

L'authentification est une partie majeure de toute application React sérieuse. Vous devez avoir un moyen fiable d'authentifier vos utilisateurs dans votre boîte à outils de développeur.

Il existe des dizaines de solutions d'authentification parmi lesquelles choisir aujourd'hui, dont beaucoup sont payantes. Laquelle devriez-vous choisir ?

Dans ce tutoriel, nous allons voir comment vous pouvez ajouter l'authentification à vos applications React gratuitement en utilisant la bibliothèque standard de l'industrie Passport.js.

À la fin, vous comprendrez comment Passport fonctionne dans un projet réel, et vous aurez tout le code de démarrage pour pouvoir configurer l'authentification dans vos futurs projets React.

## Pourquoi utiliser Passport.js ?

Passport.js est une bibliothèque éprouvée. Elle est la solution de référence pour l'authentification dans les applications Node.js depuis de nombreuses années avec plus de 1,7 million de téléchargements hebdomadaires.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-19-at-1.00.16-PM.png)
_La bibliothèque Node Passport.js_

Elle permet à vos utilisateurs de s'inscrire facilement avec un email et un mot de passe sans frais. De plus, Passport nous donne également la possibilité d'utiliser différentes stratégies d'authentification telles que la connexion sociale via Google ou Twitter, parmi des centaines d'autres options.

Vous pouvez considérer l'authentification comme une passerelle essentielle pour vos utilisateurs. Vous aurez besoin d'authentification dans de nombreux cas, non seulement pour séparer les utilisateurs occasionnels des utilisateurs sérieux de vos applications. L'authentification est utilisée pour fournir l'expérience nécessaire à différentes catégories d'utilisateurs.

## Pourquoi ne pas utiliser un service d'authentification dédié (payant) ?

Le besoin d'authentifier vos utilisateurs est un problème très courant, mais cela ne signifie pas que c'est un problème facile à résoudre.

En fait, c'est pourquoi tant d'entreprises comme Auth0, Clerk.dev, Okta et bien d'autres ont émergé pour fournir l'authentification en tant que service. Aux yeux de nombreux développeurs, bien faire l'authentification a un prix.

Heureusement pour nous, développeurs JavaScript et Node, nous avons une excellente bibliothèque avec Passport.js, qui nous permet de configurer l'authentification dans les environnements Node assez facilement.

Nous allons examiner une intégration complète de Passport.js dans une application React et décomposer son fonctionnement ligne par ligne.

## Télécharger le code du projet

Pour obtenir le code complet disponible sur le GitHub officiel de Next.js, vous pouvez [aller au dépôt suivant](https://github.com/vercel/next.js/tree/canary/examples/with-passport) avec NPM ou Yarn.

Cela vous donnera tous les fichiers du projet que nous allons examiner, ainsi qu'un modèle idéal pour utiliser Passport.js dans votre prochain projet React.

Je vous recommande de télécharger le dossier complet des exemples depuis [https://github.com/vercel/next.js](https://github.com/vercel/next.js) et de prendre le dossier with-passport. Le script de modèle inclus dans le README contient du code cassé.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/passport-gif-4.gif)
_Démonstration de l'application Passport_

## Comment fonctionne la stratégie locale de Passport

Pour commencer à utiliser Passport dans vos projets, vous devrez installer la bibliothèque principale `passport` ainsi qu'une stratégie spécifique.

Les **stratégies** sont différentes méthodes avec lesquelles vos utilisateurs peuvent s'authentifier. Passport Local est la stratégie que Passport fournit pour permettre aux utilisateurs de s'inscrire et de se connecter de la manière la plus traditionnelle, avec un email et un mot de passe.

Ces deux éléments sont inclus dans le fichier `package.json`.

Si vous regardez dans le dossier lib, vous pouvez voir comment `passport-local` est configuré.

```js
// /lib/password-local.js

import Local from 'passport-local'
import { findUser, validatePassword } from './user'

export const localStrategy = new Local.Strategy(function (
  username,
  password,
  done
) {
  findUser({ username })
    .then((user) => {
      if (user && validatePassword(user, password)) {
        done(null, user)
      } else {
        done(new Error('Combinaison nom d\'utilisateur et mot de passe invalide'))
      }
    })
    .catch((error) => {
      done(error)
    })
})
```

Dans le fichier `password-local.js`, la stratégie est créée et se charge de trouver un utilisateur en fonction de son nom d'utilisateur et de valider son mot de passe. Si un utilisateur est trouvé, il sera retourné via le callback `done`. Sinon, une erreur sera levée.

Si vous regardez dans `/pages/api`, vous verrez tout le code lié au serveur qui utilise passport. Les noms des fichiers correspondent aux actions dont vous aurez besoin : login, logout et signup.

## Comment inscrire des utilisateurs avec Passport

Si vous regardez le fichier d'inscription, il crée simplement un utilisateur en fonction des données fournies dans le corps de la requête et transmises avec celle-ci.

```js
// /pages/api/signup.js

import { createUser } from '../../lib/user'

export default async function signup(req, res) {
  try {
    await createUser(req.body)
    res.status(200).send({ done: true })
  } catch (error) {
    console.error(error)
    res.status(500).end(error.message)
  }
}

```

Une fois cela fait, le serveur répond avec un code de succès 200, ce qui signifie que votre utilisateur a été créé avec l'email et le mot de passe qu'il a fournis.

Si vous retournez dans le dossier lib, dans user.js, vous pouvez voir comment cette fonction `createUser` fonctionne :

```js
// /lib/user.js

const users = []

export async function createUser({ username, password }) {
  // Ici, vous devriez créer l'utilisateur et sauvegarder le sel et le mot de passe haché (certaines bases de données peuvent avoir
  // des méthodes d'authentification qui le feront pour vous, donc vous n'avez pas à vous en soucier) :
  const salt = crypto.randomBytes(16).toString('hex')
  const hash = crypto
    .pbkdf2Sync(password, salt, 1000, 64, 'sha512')
    .toString('hex')
  const user = {
    id: uuidv4(),
    createdAt: Date.now(),
    username,
    hash,
    salt,
  }

  // Ceci est un stockage en mémoire pour les utilisateurs, il n'y a pas de persistance des données sans une base de données appropriée
  users.push(user)

  return { username, createdAt: Date.now() }
}
```

`createUser` prend un nom d'utilisateur et un mot de passe et **hache** le mot de passe pour qu'il puisse être sauvegardé de manière sécurisée et non en texte brut. Ensuite, l'utilisateur créé est ajouté à un tableau d'utilisateurs.

Si et lorsque vous connectez une base de données à ce projet, c'est ici que vous créeriez réellement un nouvel utilisateur dans votre base de données et que vous remplaceriez `users.push`.

## Comment connecter des utilisateurs avec Passport

Si vous regardez comment votre application fonctionne, après l'inscription et la création de votre utilisateur, l'utilisateur doit ensuite se connecter. Lorsqu'un utilisateur se connecte, il fait des requêtes à `/api/login`.

C'est ici que Passport intervient et effectue l'authentification pour vous. Dans cet exemple, nous utilisons la bibliothèque `next-connect` pour initialiser passport avant que la requête POST ne soit faite (lors de la soumission du formulaire de connexion).

```js
// /api/login.js

passport.use(localStrategy)

export default nextConnect()
  .use(passport.initialize())
  .post(async (req, res) => {
    try {
      const user = await authenticate('local', req, res)
      // session est la charge utile à sauvegarder dans le token, elle peut contenir des informations de base sur l'utilisateur
      const session = { ...user }

      await setLoginSession(res, session)

      res.status(200).send({ done: true })
    } catch (error) {
      console.error(error)
      res.status(401).send(error.message)
    }
  })
```

Le point de terminaison de connexion reçoit les données de votre front end. Lorsque la requête POST est faite avec les identifiants de l'utilisateur, à savoir l'email et le mot de passe, elle utilise cette fonction d'authentification de passport pour prendre en charge l'authentification de votre requête.

Ensuite, une autre fonction, `setLoginSession`, se charge de créer une session pour l'utilisateur connecté avec le package `@hapi/iron`.

```js
// /lib/auth.js

import Iron from '@hapi/iron'
import { MAX_AGE, setTokenCookie, getTokenCookie } from './auth-cookies'

const TOKEN_SECRET = process.env.TOKEN_SECRET

export async function setLoginSession(res, session) {
  const createdAt = Date.now()
  // Créer un objet de session avec une durée de vie maximale que nous pouvons valider plus tard
  const obj = { ...session, createdAt, maxAge: MAX_AGE }
  const token = await Iron.seal(obj, TOKEN_SECRET, Iron.defaults)

  setTokenCookie(res, token)
}
```

Cela se charge de créer un cookie pour votre utilisateur qui peut maintenant être utilisé pour l'identifier et donc l'authentifier sur les futures requêtes jusqu'à ce que le cookie expire ou que l'utilisateur se déconnecte.

Si un utilisateur passe par le processus de connexion, il sera redirigé vers la page d'accueil. Cela est dû à un hook spécial appelé `useUser` dans votre page de connexion.

```js
// /pages/login.js

const Login = () => {
  useUser({ redirectTo: '/', redirectIfFound: true })
    
  // ...
}
```

`useUser` fait une requête au point de terminaison `/api/user`. Dans ce point de terminaison, il se charge de récupérer la session de la requête qui a été faite et de trouver un utilisateur en fonction de celle-ci, puis de retourner cet utilisateur.

```js
// /api/user.js

import { getLoginSession } from '../../lib/auth'
import { findUser } from '../../lib/user'

export default async function user(req, res) {
  try {
    const session = await getLoginSession(req)
    const user = (session && (await findUser(session))) ?? null

    res.status(200).json({ user })
  } catch (error) {
    console.error(error)
    res.status(500).end('Le jeton d\'authentification est invalide, veuillez vous connecter')
  }
}
```

Pour cette requête, nous utilisons le package `swr` qui nous permet de faire des requêtes GET en utilisant un hook pratique appelé `useSWR`.

Lorsque les données de l'utilisateur sont renvoyées au hook `useUser`, il redirige l'utilisateur vers une route donnée en fonction de la propriété `redirectTo` fournie. Comme celle-ci était définie sur une barre oblique, elle redirigera votre utilisateur vers la page d'accueil. Vous pouvez changer la valeur de cette propriété pour qu'elle soit la page que vous souhaitez que l'utilisateur visite immédiatement après s'être connecté, au lieu de rester sur la page de connexion.

## Comment déconnecter des utilisateurs avec Passport

Enfin, la dernière action que Passport prend en charge dans cette application est la déconnexion de l'utilisateur. Heureusement, les déconnecter est aussi simple que de supprimer le cookie que vous avez créé lors de la connexion.

Vous déconnectez votre utilisateur et supprimez le cookie côté serveur. Vous faites cela en faisant une requête GET à `/api/logout`.

```js
// /api/logout

import { removeTokenCookie } from '../../lib/auth-cookies'

export default async function logout(req, res) {
  removeTokenCookie(res)
  res.writeHead(302, { Location: '/' })
  res.end()
}
```

Dans celui-ci, vous utilisez une fonction `removeTokenCookie` pour supprimer le cookie que vous avez créé lorsque la session a été établie. Après cela, l'utilisateur est redirigé vers la page d'accueil en utilisant une redirection côté serveur.

## Comment s'améliorer dans l'authentification des utilisateurs

Le meilleur moyen de bien comprendre Passport et l'authentification en général est de travailler avec. Tant que vous êtes développeur, ce sera un composant essentiel à comprendre et à implémenter.

Au-delà de mes explications ici, assurez-vous de faire fonctionner cette application par vous-même. Jouez avec l'inscription, la connexion et la déconnexion des utilisateurs pour bien comprendre ce qui se passe réellement lorsque vous les authentifiez.

J'espère que ce projet servira de bon point de départ pour toute application React que vous avez où vous souhaitez intégrer l'authentification. Si vous souhaitez étendre cet exemple au-delà de l'authentification par email et mot de passe, assurez-vous de consulter le site web de Passport pour toutes les 500+ stratégies disponibles que vos utilisateurs peuvent utiliser pour se connecter.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*