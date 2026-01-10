---
title: Comment utiliser les fonctions Netlify dans Elm
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-08-28T07:37:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-netlify-functions-in-elm
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/netlify-functions-elm.jpg
tags:
- name: create-elm-app
  slug: create-elm-app
- name: netlify-functions
  slug: netlify-functions
- name: aws lambda
  slug: aws-lambda
- name: ELM
  slug: elm
- name: Netlify
  slug: netlify
- name: serverless
  slug: serverless
seo_title: Comment utiliser les fonctions Netlify dans Elm
seo_desc: 'This worked example creates a simple Netlify Function and integrates it
  with an Elm application.

  Netlify functions provide a very convenient way of working with AWS Lambdas, and
  they have an impressive array of example use cases, such as sending emai...'
---

Cet exemple concret crée une simple [fonction Netlify](https://functions.netlify.com/) et l'intègre avec une application Elm.

Les fonctions Netlify fournissent un moyen très pratique de travailler avec les Lambdas AWS, et elles ont [un impressionnant ensemble de cas d'utilisation exemples](https://functions.netlify.com/examples), tels que l'envoi d'e-mails, le traitement des paiements et la journalisation.

Cet exemple lit les secrets à partir des variables d'environnement (pour éviter qu'ils ne soient exposés dans le navigateur), mais il est principalement générique et peut être adapté à d'autres cas d'utilisation facilement.

## Étape 1 - Prérequis

* Créez un dépôt pour le code, probablement sur GitHub
* `npm i -g elm`
* `npm install -g netlify-cli`
* `npm i -g create-elm-app`

## Étape 2 - Créer une application Elm vanilla

* `create-elm-app elm-app-with-netlify-function`
* `cd elm-app-with-netlify-function`
* `elm-app start`

Cela devrait démarrer un serveur de développement et charger l'application dans votre navigateur.

Vous pouvez consulter [ce commit dans le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/d976b2391f98f07113d1e41a64b0359caddf3452) pour vérifier que tout est correct.

## Étape 2 - Déployer sur Netlify

* `npm init` (et remplissez avec des valeurs sensées)
* `npm i create-elm-app --save-dev` (cela ajoute create-elm-app à package.json, qui est utilisé par netlify)
* Poussez le code sur GitHub

Vous pouvez voir les résultats de cela à [ce commit dans le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/aa52ccfabacae69591a920f0675eedf620ae8b03)

* Connectez-vous / Inscrivez-vous avec [Netlify](https://www.netlify.com/)
* Créez un [nouveau site](https://app.netlify.com/start) sur Netlify
* Choisissez votre dépôt
* Définissez la "Commande de construction" sur `elm-app build`
* Définissez le "Répertoire public" sur `build`
* Cliquez sur "Déployer le site"

Netlify va maintenant déployer le site, installer les dépendances spécifiées dans package.json, puis exécuter `elm-app build` et ensuite servir le répertoire dist.

Désormais, Netlify tentera de déployer le dernier code à chaque fois que vous pousserez sur GitHub.

## Étape 3 - Lier Netlify Dev

* `netlify login`
* `netlify link` et choisissez l'option "Utiliser l'URL distante git actuelle"
* Ajoutez " ./netlify " à .gitignore
* Ajoutez un fichier netlify.toml (à partir de [ce commit dans le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/6514012000ea82fb6625fa3686adafa321723d28))
* `netlify dev`

Cela devrait démarrer un serveur de développement local et charger l'application dans votre navigateur, de manière similaire à l'étape 1.

## Étape 4 - Ajouter une fonction Netlify

Exécutez `netlify functions:create` pour créer une nouvelle fonction Netlify. Choisissez le modèle "js-token-hider", et nommez-le "call-api".

Cela créera un fichier JavaScript pour la fonction, et un package.json pour ses dépendances dans "functions/call-api".

Remplacez functions/call-api/call-api.js par celui-ci dans [le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/79381b9c1a7731b01f0c81b58a772d9576f76732)

Maintenant, si vous exécutez `netlify dev`, la fonction sera servie ainsi que l'application, bien que sur des ports différents. Vous pouvez voir la fonction dans le navigateur pour vérifier qu'elle fonctionne (probablement à [http://localhost:34567/call-api](http://localhost:34567/call-api) ou [http://localhost:34567/.netlify/functions/call-api](http://localhost:34567/.netlify/functions/call-api))

## Étape 5 - Appeler la fonction Netlify depuis Elm

Installez les dépendances

* `elm install elm/json`
* `elm install elm/http`
* `elm install krisajenkins/remotedata`

Mettez à jour Main.elm pour appeler la fonction et afficher les résultats (à partir de [le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/4dc9e8e4b60d061b5d5ef0fb2ce6ab856741236f)).

Instruisez create-elm-app pour proxyfier les appels API vers la fonction, en ajoutant elmapp.config.js, comme montré dans [le dépôt compagnon](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/90a63178e38f2919770e37fcc94e7ee0bec343ab).

À ce stade, l'application s'exécute et appelle avec succès l'API, mais il n'y a pas encore de secrets / variables d'environnement, donc l'interface utilisateur affiche une erreur.

## Étape 6 - Ajouter les secrets

Allez dans la section "Paramètres du site" - "Build & Deploy" - "Déploiement continu" - "Variables d'environnement" sur le site Web de Netlify pour votre application.

Ajoutez des variables d'environnement pour API_TOKEN et API_URL

Maintenant, lorsque vous exécutez `netlify dev`, l'application devrait se charger dans le navigateur et appeler la fonction Netlify hébergée localement, qui retournera les variables d'environnement API_TOKEN et API_URL que vous avez définies sur Netlify.

La même chose devrait être vraie sur le déploiement en direct sur Netlify. Vous devrez peut-être "Déclencher le déploiement" manuellement sur Netlify, afin qu'il utilise les nouvelles variables d'environnement.

Vous pouvez voir le déploiement du dépôt compagnon à [https://netlify-functions-with-elm.netlify.com](https://netlify-functions-with-elm.netlify.com)

## Conclusion

Les fonctions Netlify / serverless sont extrêmement utiles pour créer / se connecter aux services backend dont votre frontend a besoin. Elles sont également très faciles à configurer, comme cet article (espérons-le!) le montre.

Create-elm-app est un excellent outil pour développer des applications Elm, et sa fonction de proxy simple fonctionne bien lors du développement de fonctions Netlify.

Netlify Dev est idéal pour répliquer la configuration de production Netlify lors du développement local (dans ce cas, en fournissant automatiquement les variables d'environnement).