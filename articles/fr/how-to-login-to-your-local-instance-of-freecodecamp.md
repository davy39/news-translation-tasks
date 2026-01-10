---
title: Comment se connecter à votre instance locale de freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T00:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-login-to-your-local-instance-of-freecodecamp
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d40740569d1a4ca36b6.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: toothbrush
  slug: toothbrush
seo_title: Comment se connecter à votre instance locale de freeCodeCamp
seo_desc: 'This guide will help you log in to your local FCC site using your GitHub
  account. This process should be similar for logging in with other social media accounts.
  This guide assumes you already have a local copy of FCC up and running.

  TL;DR


  Register ...'
---

Ce guide vous aidera à vous connecter à votre site FCC local en utilisant votre compte GitHub. Ce processus devrait être similaire pour se connecter avec d'autres comptes de réseaux sociaux. Ce guide suppose que vous avez déjà une copie locale de FCC en cours d'exécution.

## **TL;DR**

1. [Enregistrer une nouvelle application OAuth](https://github.com/settings/developers)
2. Champ Page d'accueil : `http://localhost:3000/`
3. Champ Callback : `http://localhost:3000/auth/github/callback`
4. Copiez/collez l'ID Client et le Secret Client dans votre fichier `.env`
5. Utilisez le port 3000 lors de la visualisation de votre site FCC local

Les modérateurs et le personnel de Free Code Camp sont à votre disposition pour vous aider avec les problèmes liés aux Pull Request dans notre [Salle de discussion d'aide aux contributeurs](https://gitter.im/FreeCodeCamp/HelpContributors)

## **Avertissement**

La sortie de l'exécution de `$ gulp` mentionne que le **Port d'Accès** est 3001. Je n'ai réussi à me connecter avec GitHub qu'au port 3000 - le **Port Proxy**. Si vous savez comment vous connecter en utilisant d'autres ports, envisagez de soumettre une pull request sur ce wiki.

## **Se connecter en utilisant votre compte GitHub**

1. [Enregistrez une nouvelle application OAuth](https://github.com/settings/developers) et cliquez sur **Register new application**

_Alternativement_, cliquez sur votre **Photo de profil** => **Paramètres** => **Applications** => **Applications développeur** => **Register new application**

![Enregistrer l'application OAuth GitHub](https://discourse-user-assets.s3.amazonaws.com/original/2X/5/55f4645c3498ceb8098afe8e8353da8f7c262548.png)

Remplissez les champs de l'application OAuth

* **Nom de l'application** - choisissez un nom quelconque, comme `fcc-local`
* **URL de la page d'accueil** - définissez sur `http://localhost:3000/`
* **Description de l'application** - facultatif
* **URL de rappel d'autorisation** - définissez sur `http://localhost:3000/auth/github/callback`

1. Cliquez sur **Register application** pour voir la page de l'application nouvellement enregistrée avec votre ID Client et votre Secret Client.

![ID Client et Secret Client](https://discourse-user-assets.s3.amazonaws.com/original/2X/c/c43ee37a9f0f228d3663bb28accedc14cca3ff56.png)

1. Copiez et collez votre ID Client et votre Secret Client dans votre fichier `.env`.

_Note : votre ID Client et votre Secret Client seront de longues valeurs alphanumériques._

![Mettre à jour le fichier .env](https://discourse-user-assets.s3.amazonaws.com/original/2X/5/549aeaa6ea85e119ba5e978c708dc55c39b134b3.png)

## **Conseils**

1. Supprimez/désactivez avec un bloc de commentaire le fournisseur non désiré dans [passport-provider](https://github.com/FreeCodeCamp/FreeCodeCamp/blob/staging/server/passport-providers.js).
2. Ajoutez SESSION_SECRET et COOKIE_SECRET dans `.env` si vous obtenez une erreur sur express-session et cookieParser.

`COOKIE_SECRET='secret' SESSION_SECRET='secret'`

1. Exécutez la commande `node seed` avant d'exécuter `gulp` si vous ne obtenez pas les défis.

## **Terminé**

Félicitations ! Vous pouvez maintenant vous connecter avec succès à votre site FCC local en utilisant votre compte GitHub.