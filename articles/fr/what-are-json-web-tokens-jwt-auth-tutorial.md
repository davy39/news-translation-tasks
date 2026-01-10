---
title: Qu'est-ce que les JSON Web Tokens ? Tutoriel sur l'authentification JWT
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-12T20:51:31.000Z'
originalURL: https://freecodecamp.org/news/what-are-json-web-tokens-jwt-auth-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/jwt.png
tags:
- name: JSON Web Tokens
  slug: json-web-tokens
- name: youtube
  slug: youtube
seo_title: Qu'est-ce que les JSON Web Tokens ? Tutoriel sur l'authentification JWT
seo_desc: 'Most web apps use security measures to make sure user data stays private.
  Authentication is a key part of security and JSON Web Tokens (JWT) are a great way
  to implement authentication.

  So what are JSON Web Tokens?

  JWT is a standard that defines a co...'
---

La plupart des applications web utilisent des mesures de sécurité pour garantir la confidentialité des données des utilisateurs. L'authentification est une partie clé de la sécurité et les JSON Web Tokens (JWT) sont un excellent moyen de mettre en œuvre l'authentification.

## Alors, qu'est-ce que les JSON Web Tokens ?

JWT est une norme qui définit une manière compacte et autonome de transmettre en toute sécurité des informations entre un client et un serveur sous forme d'objet JSON. La taille compacte rend les tokens faciles à transférer via une URL, un paramètre POST ou à l'intérieur d'un en-tête HTTP. De plus, comme ils sont autonomes, ils incluent toutes les informations nécessaires sur un utilisateur, de sorte que la base de données n'a pas besoin d'être interrogée plus d'une fois.

Les informations dans un JWT peuvent être fiables car elles sont signées numériquement à l'aide d'une clé secrète ou d'une paire de clés publique/privée.

## Authentification

Les JWT sont principalement utilisés pour l'authentification. Après qu'un utilisateur se connecte à une application, l'application créera un JWT et le renverra à l'utilisateur. Les requêtes ultérieures de l'utilisateur incluront le JWT. Le token indique au serveur quelles routes, services et ressources l'utilisateur est autorisé à accéder. Les JWT peuvent être facilement utilisés sur plusieurs domaines, ils sont donc souvent utilisés pour le Single Sign On.

## Utilisation des JSON Web Tokens

Thomas Weibenfalk a réalisé un excellent tutoriel vidéo qui explique les JSON Web Tokens et démontre comment les utiliser pour l'authentification. Le tutoriel enseigne l'authentification JWT de la manière la plus simple possible, sans utiliser beaucoup de bibliothèques supplémentaires.

Regardez le tutoriel ci-dessous ou sur [la chaîne YouTube de freeCodeCamp.org](https://www.youtube.com/watch?v=x5gLL8-M9Fo) (2 heures de visionnage).

%[https://www.youtube.com/watch?v=x5gLL8-M9Fo]