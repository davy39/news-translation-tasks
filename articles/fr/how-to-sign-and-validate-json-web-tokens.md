---
title: Comment signer et valider les JSON Web Tokens – Tutoriel JWT
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2022-12-09T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-sign-and-validate-json-web-tokens
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/shubham-dhage-gC_aoAjQl2Q-unsplash.jpg
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: JWT
  slug: jwt
- name: Security
  slug: security
seo_title: Comment signer et valider les JSON Web Tokens – Tutoriel JWT
seo_desc: 'A JSON Web Token, or JWT, is an open standard for securely creating and
  sending data between two parties, usually a client and a server.

  If you''ve ever signed in to a site like freeCodeCamp with your Google or GitHub
  account, there''s a good chance th...'
---

Un JSON Web Token, ou JWT, est une norme ouverte pour créer et envoyer des données de manière sécurisée entre deux parties, généralement un client et un serveur.

Si vous vous êtes déjà connecté à un site comme freeCodeCamp avec votre compte Google ou GitHub, il est fort probable que vous utilisiez déjà un JWT.

Dans cet article, nous allons voir comment les JWT sont utilisés, puis nous approfondirons ce que sont les JWT et comment ils peuvent transmettre des données de manière sécurisée grâce au processus de signature et de validation.

## Comment les JWT sont utilisés

Les JWT sont généralement utilisés pour gérer les sessions utilisateur sur un site web. Bien qu'ils soient une partie importante du processus d'authentification basée sur les tokens, les JWT eux-mêmes sont utilisés pour l'autorisation, et non pour l'authentification.

Voici un bon aperçu du fonctionnement de l'authentification basée sur les tokens :

![Un diagramme montrant le flux pour l'authentification basée sur les tokens avec JWT.](https://www.freecodecamp.org/news/content/images/2023/01/token-based-authentication.jpg)
_[Source](https://hackernoon.com/using-session-cookies-vs-jwt-for-authentication-sd2v3vci)_

Lorsque vous vous connectez à un site avec un nom d'utilisateur et un mot de passe, ou avec une méthode tierce comme Google, vous prouvez qui vous êtes avec ces détails sensibles ou cet accès. Ce processus est appelé **authentification**.

Une fois connecté, le serveur du site envoie un JWT qui vous permet d'accéder à des choses comme votre page de paramètres, votre panier d'achat, et ainsi de suite. Ce processus est appelé **autorisation**.

Vous envoyez votre JWT au serveur avec chaque requête. Lorsque le serveur le reçoit, il génère une signature en utilisant certaines données de votre JWT, la vérifie, et si votre JWT est valide, il envoie une réponse.

## Qu'est-ce qu'un JWT ?

À leur cœur, les JWT sont simplement des morceaux de données JSON encodées avec une signature cryptographique à la fin.

Voici un exemple de JWT :

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlF1aW5jeSBMYXJzb24iLCJpYXQiOjE1MTYyMzkwMjJ9.WcPGXClpKD7Bc1C0CCDA1060E2GGlTfamrd8-W0ghBE
```

Chaque JWT est composé de trois segments, chacun séparé par un point (`.`). Ces trois segments sont l'en-tête, la charge utile et la signature.

Si vous copiez et collez ce JWT dans le [Débogueur JWT.io](https://jwt.io/), vous pouvez voir les versions décodées de ces trois segments.

### Segment d'en-tête

Le segment d'en-tête d'un JWT contient des informations sur l'algorithme et le type de token.

Voici le segment d'en-tête du JWT d'exemple ci-dessus :

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

Le segment d'en-tête est encodé en base 64 URL, et se décode en l'objet JSON suivant :

```json
{
  "alg": "HS256",
  "typ": "JWT"
}

```

`"alg"` est le type d'algorithme utilisé dans le dernier segment, la signature cryptographique. Dans ce cas, l'algorithme HMAC SHA256 est utilisé, bien que RSA soit également courant.

`"typ"` est le type de token que la chaîne segmentée représente, qui dans ce cas est JWT.

### Segment de charge utile

Le segment de charge utile d'un JWT contient des revendications enregistrées ou des informations d'identification, généralement pour un utilisateur.

Voici le segment de charge utile du JWT d'exemple ci-dessus :

```
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlF1aW5jeSBMYXJzb24iLCJpYXQiOjE1MTYyMzkwMjJ9
```

Le segment de charge utile est également encodé en base 64 URL, et se décode en l'objet JSON suivant :

```json
{
  "sub": "1234567890",
  "name": "Quincy Larson",
  "iat": 1516239022
}

```

Puisque les JWT sont généralement utilisés dans le cadre de la méthode d'authentification des sites, le segment de charge utile contient généralement des informations d'identification pour un utilisateur. Ces revendications se divisent en trois catégories : enregistrées, publiques et privées.

Les revendications enregistrées sont un ensemble de revendications prédéfinies définies [ici](https://www.rfc-editor.org/rfc/rfc7519#section-4.1) qui sont optionnelles, mais recommandées lors de l'utilisation de JWT.

Les revendications publiques sont des revendications optionnelles, généralement issues du [Registre IANA JSON Web Token](https://www.iana.org/assignments/jwt/jwt.xhtml).

Les revendications privées sont optionnelles et sont toutes les revendications qui ne tombent pas sous les catégories des revendications enregistrées ou publiques.

`"sub"` est le sujet du JWT, et est généralement une chaîne d'identification unique pour un utilisateur dans une application, généralement une adresse e-mail, un nom d'utilisateur ou un identifiant. Les sujets sont des revendications enregistrées.

`"name"` est le nom complet de l'utilisateur à qui le JWT a été émis, et est une revendication publique.

`"iat"` est la date "émise à" pour le token, et est une revendication enregistrée.

### Segment de signature

Le segment de signature d'un JWT contient la signature cryptographique du token.

Voici le segment de signature du JWT d'exemple ci-dessus :

```
WcPGXClpKD7Bc1C0CCDA1060E2GGlTfamrd8-W0ghBE
```

Le segment de signature est composé des segments d'en-tête et de charge utile encodés en base 64 URL, d'un secret (généralement le contenu d'une clé dans un algorithme de signature), et haché en utilisant l'algorithme défini dans le segment d'en-tête :

```
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  your-256-bit-secret
)
```

La signature aide à garantir que les données dans les segments d'en-tête et de charge utile n'ont pas été altérées, et que le JWT peut être fiable.

Cependant, il est important de noter que la signature cryptographique à la fin du JWT est uniquement pour la validation. Elle ne chiffre aucune donnée dans les segments d'en-tête ou de charge utile du token. Vous ne devriez donc jamais envoyer d'informations sensibles comme le mot de passe d'un utilisateur dans un JWT – tout dans l'en-tête et la charge utile peut et doit être public.

#### Comment valider les signatures JWT

La méthode exacte pour valider une signature dépend de l'algorithme défini dans le segment d'en-tête et utilisé pour générer la signature elle-même.

Pour l'algorithme de signature HS256, une clé privée est partagée entre deux entités, par exemple le serveur de votre application et un serveur d'authentification. Cette clé privée est utilisée à la fois pour générer des signatures pour les JWT sortants et pour valider les signatures des JWT entrants.

Lorsque votre serveur d'authentification reçoit un JWT entrant, il utilise les segments d'en-tête et de charge utile du JWT entrant et la clé privée partagée pour générer une signature.

Si la signature correspond, alors votre application sait que le JWT entrant peut être fiable.

Un autre algorithme de signature populaire est RS256, qui utilise des paires de clés publiques et privées pour valider les signatures. Cela est similaire au système utilisé pour SSH et SSL.

Si vous souhaitez en savoir plus sur le fonctionnement de RS256, consultez cet article :

%[https://www.freecodecamp.org/news/understanding-encryption-algorithms/#rsa]

## Autres tutoriels utiles

Si vous souhaitez en savoir plus sur les JWT et comment les utiliser dans des applications, consultez ces tutoriels :

%[https://www.freecodecamp.org/news/what-are-json-web-tokens-jwt-auth-tutorial/]

%[https://www.freecodecamp.org/news/learn-to-implement-user-authentication-in-node-apps-using-passport-js/]

## Merci d'avoir lu

Si vous avez trouvé cet article sur les JWT utile, envisagez de le partager afin que plus de personnes puissent en bénéficier.

N'hésitez pas non plus à me contacter sur [Twitter](https://twitter.com/kriskoishigawa) et à me faire savoir ce que vous en pensez.