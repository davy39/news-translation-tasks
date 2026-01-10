---
title: Comment créer des applications JAMstack serverless authentifiées avec Gatsby
  et Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-11T20:22:51.000Z'
originalURL: https://freecodecamp.org/news/building-jamstack-apps
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/D1dQf4uWkAAAwkD.jpg
tags:
- name: Gatsby
  slug: gatsby
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: Netlify
  slug: netlify
- name: React
  slug: reactjs
seo_title: Comment créer des applications JAMstack serverless authentifiées avec Gatsby
  et Netlify
seo_desc: 'By swyx

  When interacting with a backend, a JAMstack app can do everything a mobile app can
  do, without the tyranny of the app store. This is a fundamental insight that goes
  as deep as the fight for a more open,  secure, decoupled, faster web.

  Static ...'
---

Par swyx

Lors de l'interaction avec un backend, une application JAMstack peut faire tout ce qu'une application mobile peut faire, sans la tyrannie du magasin d'applications. Il s'agit d'une idée fondamentale qui va aussi loin que la lutte pour un web plus ouvert, sécurisé, découplé et plus rapide.

Les générateurs de sites statiques (SSG) sont traditionnellement utilisés pour générer du HTML pour des sites statiques, et même pour des [sites de commerce électronique](https://css-tricks.com/lets-build-a-jamstack-e-commerce-store-with-netlify-functions/), mais la génération moderne de SSG JavaScript permet des applications web complètes et ultra-rapides. Gatsby utilise JavaScript pour réhydrater le markup en une application React entièrement dynamique - ce qui signifie que vous pouvez utiliser des API pour effectuer toutes sortes de fonctionnalités dynamiques !

Voyons comment nous pouvons ajouter progressivement des fonctionnalités à un site statique Gatsby avec Netlify Functions, puis ajouter une authentification avec Netlify Identity pour créer une application Gatsby complète. Nous allons progressivement construire jusqu'à [une démonstration complète](https://github.com/sw-yx/jamstack-hackathon-starter/) avec :

- ??Pages dynamiques côté client dans Gatsby
- ?Fonctions serverless (avec Netlify Dev)
- ??\u200d\u2642\ufe0fMasquer les secrets de l'API pour qu'ils ne soient pas exposés au frontend
- ?Authentification (avec Netlify Identity)
- ?Routes protégées
- ?Fonctions serverless authentifiées (pourquoi pas !)
- ?Connexion avec un fournisseur externe comme GitHub, Bitbucket, Google, etc.

## Pas le générateur de site statique de vos parents

Pourquoi utiliser quelque chose comme Gatsby plutôt que Jekyll ou Hugo ou l'un des [centaines de générateurs de sites statiques](https://www.staticgen.com/) disponibles ? [Il y a plusieurs raisons](https://www.gatsbyjs.org/blog/2018-2-27-why-i-upgraded-my-website-to-gatsbyjs-from-jekyll/), mais l'un des arguments de vente uniques est la manière dont Gatsby vous aide à construire des ["Applications Web Progressives Statiques"](https://www.gatsbyjs.org/docs/progressive-web-app/#progressive-web-app) avec React.

[La capacité de Gatsby à réhydrater](https://www.gatsbyjs.org/docs/production-app/#dom-hydration) (quel mot délicieux !) le DOM signifie que vous pouvez faire des choses incroyablement dynamiques avec JavaScript et React qui seraient beaucoup plus difficiles avec les anciens SSG.

Supposons que vous avez un site Gatsby statique typique, comme [gatsby-starter-default](https://www.gatsbyjs.org/starters/gatsby-starter-default). Vous pouvez faire `npm run build`, et il génère un ensemble de fichiers HTML. Super ! Je peux l'héberger gratuitement !

Maintenant, imaginez que votre client vient vous voir et vous demande d'ajouter une logique personnalisée qui doit être exécutée sur le serveur :

- Peut-être avez-vous des secrets d'API tiers que vous ne voulez pas exposer à votre utilisateur.
- Peut-être avez-vous besoin [d'un proxy côté serveur pour contourner les problèmes CORS](https://alligator.io/nodejs/solve-cors-once-and-for-all-netlify-dev/).
- Peut-être avez-vous besoin de pinguer une base de données pour vérifier votre inventaire.

**Oh non ! Maintenant, vous devez tout réécrire et passer à un droplet Digital Ocean !**

Je plaisante. Non, vous n'avez pas à tout réécrire.

La beauté des fonctions serverless est qu'elles sont adoptables de manière incrémentielle - **votre site évolue avec vos besoins** - et avec JavaScript, vous pouvez rerendre des sections entières de votre site en fonction des données d'API en direct. Bien sûr, plus vous faites cela, plus cela peut être intensif en ressources (en termes de bande passante et de calcul), il y a donc un compromis de performance. **Votre site doit être aussi dynamique que nécessaire, mais pas plus.** Gatsby est parfait pour cela.

## Utilisation de Netlify Dev pour ajouter des fonctions serverless

[Netlify Functions](https://www.netlify.com/docs/functions/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex) sont une excellente solution à faible configuration pour ajouter des fonctionnalités serverless à votre site Gatsby.

Nous supposerons que vous avez déjà un site Gatsby prêt à l'emploi, de préférence lié à un dépôt Git distant comme GitHub. Si vous n'en avez pas, forkez et téléchargez [gatsby-starter-default](https://app.netlify.com/start/deploy?repository=https://github.com/gatsbyjs/gatsby-starter-default). Passons en revue les étapes pour ajouter des fonctions Netlify :

1. **Installez Netlify CLI et connectez-vous** :

```bash
npm i -g netlify-cli
netlify login # pour lier votre compte Netlify gratuit
```

Assez simple.

2. **Créez votre instance Netlify pour votre site Gatsby** :

```bash
netlify init
```

Vous serez invité à entrer une "commande de build", qui pour Gatsby est `yarn build`, et un "répertoire de publication", qui pour Gatsby est `public`. Vous pouvez également enregistrer cela dans un [fichier de configuration netlify.toml](https://www.netlify.com/docs/netlify-toml-reference/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex), ou le CLI le créera pour vous :

```toml:title=netlify.toml
[build]
  command = "yarn build"
  functions = "functions"
  publish = "public"
```

Comme vous pouvez le voir dans l'exemple ci-dessus, nous allons également spécifier où nous allons sauvegarder nos fonctions dans le dossier nommé de manière créative `functions`.

3. **Créez votre première fonction Netlify** : Netlify CLI dispose d'un [ensemble de modèles](https://github.com/netlify/cli/tree/master/src/functions-templates/js) disponibles pour vous aider à commencer à écrire des fonctions serverless. Il suffit d'exécuter :

```bash
netlify functions:create # ntl functions:create fonctionne aussi
```

Vous verrez une liste avec autocomplétion. Nous allons choisir l'exemple `token-hider` pour l'instant. Une fois que vous l'avez sélectionné, le CLI copiera les fichiers nécessaires et installera les dépendances `axios` nécessaires.

Remarquez que `token-hider.js` inclut cette ligne :

```js
const { API_SECRET = "shiba" } = process.env
```

Cela est destiné à simuler les secrets d'API que vous ne voulez pas exposer au frontend. Vous pouvez les définir comme [variables d'environnement de build](https://www.netlify.com/docs/continuous-deployment/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex#environment-variables) sur le tableau de bord Netlify de votre site. Vous pouvez les nommer comme vous le souhaitez, et à des fins de démonstration, nous avons fourni une valeur par défaut, mais bien sûr, vous êtes libre de modifier ce code comme vous le souhaitez. C'est juste du JavaScript™ !

4. **Assurez-vous que les dépendances des fonctions sont installées avec `netlify-lambda`** (Optionnel mais recommandé)

Remarquez que votre fonction est livrée avec son propre `package.json` et `node_modules`. Cela signifie que chaque fonction peut avoir ses propres dépendances gérées indépendamment, mais vous devez également vous assurer que ces dépendances sont installées lorsque vous déployez ou lorsque quelqu'un clone votre dépôt. Vous pouvez soit les ajouter à git (beurk !), soit écrire un script bash pour effectuer cette installation. Mais ne vous inquiétez pas, il existe un utilitaire simple pour automatiser cela :

```bash
yarn add -D netlify-lambda
```

Et ajoutez un script postinstall dans `package.json` (ceci n'est pas spécifique à Netlify, cela fait partie de [comment npm fonctionne](https://docs.npmjs.com/misc/scripts#description)) :

```js
  "scripts": {
    "postinstall": "netlify-lambda install"
  },
```

5. **Lancez Gatsby et les fonctions avec Netlify Dev**

[Netlify Dev](https://www.netlify.com/blog/2019/04/09/netlify-dev-our-entire-platform-right-on-your-laptop/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex) est le serveur proxy local intégré dans le CLI que nous allons utiliser pour développer nos fonctions avec notre application Gatsby. Vous pouvez le démarrer comme suit :

```bash
netlify dev # ou ntl dev
```

Votre application Gatsby sera maintenant accessible à l'adresse `http://localhost:8888` et votre fonction sera accessible à l'adresse `http://localhost:8888/.netlify/function/token-hider`. Vérifiez cela dans votre navigateur !

Comment se fait-il que le serveur de développement Gatsby et le serveur de fonctions Netlify soient tous deux disponibles sur le même port local ? Pourquoi le API_SECRET que vous avez défini côté Netlify est-il disponible en développement local ? L'image mentale approximative que vous devriez avoir ressemble à [quelque chose comme ceci](https://github.com/netlify/cli/blob/master/docs/netlify-dev.md) :

![ASCCII-ART](https://www.freecodecamp.org/news/content/images/2019/09/ASCCII-ART.png)

Vous pouvez appeler votre fonction Netlify depuis n'importe où dans votre application Gatsby ! Par exemple, dans n'importe quel gestionnaire d'événements ou méthode de cycle de vie, insérez :

```js
fetch("/.netlify/functions/token-hider")
  .then(response => response.json())
  .then(console.log)
```

et regardez une liste d'images de chiens apparaître dans votre console. Si vous êtes nouveau dans React, je vous recommande vivement de [lire la documentation React](https://reactjs.org/docs/handling-events.html) pour comprendre où et comment insérer des gestionnaires d'événements afin de, par exemple, [répondre à un clic sur un bouton](https://reactjs.org/docs/handling-events.html).

## Ajout de l'authentification

Ainsi, oui, votre site peut maintenant être plus dynamique que n'importe quel site statique : il peut interagir avec n'importe quelle base de données ou API. Vous pouvez masquer les jetons API des regards indiscrets. Il contourne les restrictions CORS (au fait, vous pouvez également utiliser [Netlify Redirects](https://www.netlify.com/docs/redirects/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex) pour cela). Mais ce n'est pas encore une _application_ application. Pas encore !

La chose clé concernant les applications web (et, soyons honnêtes, la chose clé pour laquelle les utilisateurs paient vraiment) est qu'elles ont toutes un concept d'`utilisateur`, et cela apporte avec lui toutes sortes de complications, de la sécurité à la gestion d'état en passant par le [contrôle d'accès basé sur les rôles](https://www.netlify.com/docs/visitor-access-control/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex#role-based-access-controls-with-jwt-tokens). Des routes entières doivent être protégées par authentification, et le contenu sensible doit être protégé de la génération statique de Gatsby. Parfois, il y a des choses que vous ne voulez -pas- que les robots de Google voient !

C'est un niveau de préoccupation différent, ce qui rend difficile d'en parler dans le même article qu'un tutoriel Gatsby typique. Mais nous sommes ici pour créer des applications, alors allons-y !

## Ajout de Netlify Identity et de pages authentifiées à Gatsby

1. **Activer Netlify Identity** : Netlify Identity n'est pas activé par défaut. Vous devrez vous rendre dans l'administration de votre site (par exemple `https://app.netlify.com/sites/YOUR_AWESOME_SITE/identity`) pour l'activer. [Lisez la documentation](https://www.netlify.com/docs/identity/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex) pour plus d'informations sur ce que vous pouvez faire, par exemple ajouter une connexion sociale Facebook ou Google !
2. **Installer les dépendances** : `npm install gatsby-plugin-netlify-identity react-netlify-identity-widget  @reach/dialog @reach/tabs @reach/visually-hidden gatsby-plugin-create-client-paths`
3. **Configurer Gatsby** : pour le dynamisme !

```jsx:title=gatsby-config.js
// gatsby-config.js
module.exports = {
  plugins: [
    {
      resolve: `gatsby-plugin-create-client-paths`,
      options: { prefixes: [`/app/*`] },
    },
    {
      resolve: `gatsby-plugin-netlify-identity`,
      options: {
        url: "https://YOUR_AWESOME_SITE_INSTANCE_HERE.netlify.com",
      },
    },
  ],
}
```

Cela configure tout ce qui se trouve sous la route `/app` pour être dynamique côté client, ce qui signifie que vous pouvez le mettre derrière un mur d'authentification.

4. **Ajouter le widget de connexion** : [`netlify-identity-widget`](https://github.com/netlify/netlify-identity-widget) est une superposition agnostique de framework qui est livrée avec une belle interface utilisateur d'inscription/connexion. Cependant, c'est un package de 60 Ko, il existe donc une alternative de 6 Ko qui suppose simplement que vous utilisez React : `react-netlify-identity-widget`.

Le widget est implémenté comme une modale accessible avec `@reach/dialog`, vous devez donc le placer quelque part dans votre application :

```jsx:title=src/app/login.js
// src/app/login.js
import React from "react"
import { navigate } from "gatsby"

import { IdentityModal } from "react-netlify-identity-widget"
import "react-netlify-identity-widget/styles.css" // supprimez si vous voulez apporter votre propre CSS

export default function Login() {
  const [dialog, setDialog] = React.useState(false)
  return (
    <div>
      <h1>Se connecter</h1>
      <button onClick={() => setDialog(true)}>se connecter</button>
      <IdentityModal
        showDialog={dialog}
        onCloseDialog={() => setDialog(false)}
        onLogin={user => navigate("/app/profile")}
        onSignup={user => navigate("/app/profile")}
      />
    </div>
  )
}
```

`react-netlify-identity-widget` utilise React Context, il nécessite donc normalement l'ajout d'un Provider, mais `gatsby-plugin-netlify-identity` l'a déjà fait pour vous (c'est tout son but !).

Comme vous pouvez vous y attendre, vous pouvez utiliser ce Context dans le reste de votre application. `react-netlify-identity-widget` exporte un [Custom Consumer Hook](https://kentcdodds.com/blog/how-to-use-react-context-effectively) appelé `useIdentityContext`, qui aide à effectuer certaines vérifications à l'exécution et facilite la typage TypeScript en supprimant une vérification `undefined`.

`useIdentityContext` retourne un objet `identity`, et [vous pouvez voir la pléthore de données et de méthodes qu'il expose dans la documentation](https://github.com/sw-yx/react-netlify-identity#user-content-usage). Utilisons-les pour implémenter un composant `NavBar` !

```jsx:title=src/app/components/NavBar.js
// src/app/components/NavBar.js
import React from "react"
import { Link, navigate } from "gatsby"
import { useIdentityContext } from "react-netlify-identity-widget"

export default function NavBar() {
  const { user, isLoggedIn, logoutUser } = useIdentityContext()
  let message = isLoggedIn
    ? `Bonjour, ${user.user_metadata && user.user_metadata.full_name}`
    : "Vous n'êtes pas connecté"
  const handleClick = async event => {
    event.preventDefault()
    await logoutUser()
    navigate(`/app/login`)
  }
  return (
    <div>
      <span>{message}</span>
      <nav>
        <span>Naviguer dans l'application : </span>
        <Link to="/app/">Principal</Link>
        <Link to="/app/profile">Profil</Link>
        {isLoggedIn ? (<a href="/" onClick={handleClick}>Déconnexion</a>) : (<Link to="/app/login">Connexion</Link>)}
      </nav>
    </div>
  )
}
```

5. **Écrire le reste de votre application** : Grâce à notre configuration dans `gatsby-plugin-create-client-paths`, tous les sous-chemins dans `src/pages/app` seront exemptés de la génération statique de Gatsby. Pour garder la ligne de démarcation entre l'application et le site parfaitement claire, j'aime avoir tout mon code Gatsby dynamique dans un dossier dédié `app`. Cela signifie que vous pouvez utiliser `@reach/router` avec `react-netlify-identity-widget` pour écrire une application React dynamique standard avec des routes privées et authentifiées. Voici un exemple de code pour vous donner une idée de la manière de les connecter :

```jsx:title=src/app/app.js
// src/app/app.js
import React from "react"
import { Router } from "@reach/router"
import Layout from "../components/layout"
import NavBar from "./components/NavBar"
import Profile from "./profile"
import Main from "./main"
import Login from "./login"
import { useIdentityContext } from "react-netlify-identity-widget"
import { navigate } from "gatsby"

function PrivateRoute(props) {
  const { isLoggedIn } = useIdentityContext()
  const { component: Component, location, ...rest } = props

  React.useEffect(
    () => {
      if (!isLoggedIn && location.pathname !== `/app/login`) {
        // Si l'utilisateur n'est pas connecté, redirigez-le vers la page de connexion.
        navigate(`/app/login`)
      }
    },
    [isLoggedIn, location]
  )
  return isLoggedIn ? <Component {...rest} /> : null
}
function PublicRoute(props) {
  return <div>{props.children}</div>
}

export default function App() {
  return (
    <Layout>
      <NavBar />
      <Router>
        <PrivateRoute path="/app/profile" component={Profile} />
        <PublicRoute path="/app">
          <PrivateRoute path="/" component={Main} />
          <Login path="/login" />
        </PublicRoute>
      </Router>
    </Layout>
  )
}
```

Ouf, c'était beaucoup ! mais vous devriez avoir un bon point de départ pour votre application maintenant :)

## Points bonus : Fonctions Netlify authentifiées ?

Tout comme [chaque acte de magie a un engagement, un tournant et un prestige](<https://en.wikipedia.org/wiki/The_Prestige_(film)>), j'ai une dernière information pour vous. [Rien côté client n'est sûr](https://stackoverflow.com/questions/50277192/react-security-concerns-restricted-pages-in-app). Bien que vous puissiez envoyer des identifiants d'utilisateur Netlify Identity à vos points de terminaison de fonction Netlify pour un accès authentifié depuis votre application Gatsby (par exemple dans le corps d'une requête POST), vous ne serez jamais vraiment sûr que ce flux est sécurisé contre les utilisateurs malveillants ou l'espionnage.

La meilleure façon d'effectuer des actions authentifiées à l'intérieur des fonctions serverless est de le faire depuis **l'intérieur** du contexte de la fonction elle-même. Heureusement, [Netlify Identity et Functions fonctionnent de manière transparente ensemble](https://www.netlify.com/docs/functions/?utm_source=blog&utm_medium=freecodecamp&utm_campaign=devex#identity-and-functions). Tout ce que vous avez à faire est d'envoyer le [JWT](https://jwt.io/) de l'utilisateur lors de l'appel de votre point de terminaison :

```js
// dans votre application gatsby
const { user } = useIdentityContext()
// dans un gestionnaire d'événements
fetch("/.netlify/functions/auth-hello", {
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: "Bearer " + user.token.access_token, // comme ceci
  },
}).then(/* etc */)
```

Si même cela est trop de code standard, vous pouvez même utiliser l'enveloppe fetch qui est fournie avec l'objet `identity` :

```js
// dans votre application gatsby
const { authedFetch } = useIdentityContext()
// dans un gestionnaire d'événements
authedFetch("/.netlify/functions/auth-hello").then(/* etc */)
```

Et ensuite, à l'intérieur de votre fonction Netlify, vous pouvez maintenant vérifier l'objet `user` ou le transmettre à votre API ou base de données finale :

```js
module.exports = { handler }
async function handler(event, context) {
  if (context.clientContext) {
    const { user } = context.clientContext
    // vous pouvez obtenir des métadonnées utilisateur réelles que vous pouvez utiliser !
    return {
      statusCode: 200,
      body: JSON.stringify({
        msg: "super info secrète disponible uniquement pour les utilisateurs authentifiés",
        user,
      })
    }
  } else {
    return {
      statusCode: 401,
      body: JSON.stringify({
        msg:
          "Erreur : Aucune authentification détectée ! Notez que netlify-lambda n'émule pas localement Netlify Identity.",
      }),
    }
  }
}
```

## Gatsby + Netlify - Parfait pour votre prochain Hackathon

Comme vous pouvez le voir, il y a quelques étapes pour transformer vos sites Gatsby statiques en applications dynamiques, authentifiées et entièrement serverless avec les outils gratuits de Netlify. Cela fait de Gatsby un outil parfait pour votre prochaine application. Si vous êtes à un hackathon, que vous manquez de temps ou que vous souhaitez simplement voir une démonstration complète, consultez l'un des liens suivants.

- **Code** : https://github.com/sw-yx/jamstack-hackathon-starter
- **Starter** : https://www.gatsbyjs.org/starters/jamstack-hackathon-starter
- **Démonstration en direct** : https://jamstack-hackathon-starter.netlify.com/