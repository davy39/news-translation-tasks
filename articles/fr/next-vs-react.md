---
title: Next.js vs React – Quelles sont les différences ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-03T16:36:18.000Z'
originalURL: https://freecodecamp.org/news/next-vs-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/What--7-.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Next.js vs React – Quelles sont les différences ?
seo_desc: "By Nishant Kumar\nHey everyone! Next.js 13 is trending these days, and\
  \ it's a great time to learn it. But what even is Next.js? What is pre-rendering\
  \ in Next.js, and why do we use it? \nWell, let me explain.\nWhat is Next.js?\n\
  Next.js is a backend framew..."
---

Par Nishant Kumar

Bonjour à tous ! Next.js 13 est très populaire ces jours-ci, et c'est le moment idéal pour l'apprendre. Mais qu'est-ce que Next.js ? Qu'est-ce que le pré-rendu dans Next.js, et pourquoi l'utilisons-nous ?

Eh bien, laissez-moi expliquer.

## Qu'est-ce que Next.js ?

Next.js est un framework backend basé sur React.

Tout ce que nous pouvons faire dans React, nous pouvons aussi le faire dans Next.js – avec quelques fonctionnalités supplémentaires comme le routage, les appels API, l'authentification, et plus encore. Nous n'avons pas ces fonctionnalités dans React. Au lieu de cela, nous devons installer certaines bibliothèques et dépendances externes – comme React Router pour le routage dans une application React à page unique, par exemple.

Mais dans Next.js, les choses sont différentes. Nous n'avons pas à nous appuyer sur des bibliothèques externes pour accomplir ces tâches. Elles sont intégrées dès la création d'une application Next.js.

C'est la principale raison pour laquelle une application Next.js est différente d'une application React traditionnelle.

## Rendu côté client vs rendu côté serveur

Next.js utilise également ce qu'on appelle le rendu côté serveur. Et pour comprendre comment cela fonctionne, nous devons également parler du rendu côté client.

En gros, un client est ce que nous voyons à l'écran – l'interface utilisateur. C'est le client, ce que nous pouvons voir. En d'autres termes, c'est la partie front-end du code.

Un serveur, en revanche, est quelque chose que nous ne pouvons pas voir. C'est le côté backend du code, ou le code serveur.

Dans le rendu côté client, l'application se charge et génère la sortie sur le navigateur de manière dynamique. En d'autres termes, le navigateur rend les pages en utilisant JavaScript.

Mais dans le rendu côté serveur, l'interface utilisateur que nous voyons à l'écran n'est pas générée par le navigateur, mais par le serveur. Lorsqu'une application se charge, elle n'a pas besoin d'analyser l'interface utilisateur sur le navigateur. Au lieu de cela, elle provient du côté serveur, générée à l'avance sur le serveur.

## Comment React et le CSR fonctionnent

Ainsi, lorsque nous chargeons une application React ou lorsqu'elle est montée et que nous vérifions le code source dans le navigateur, nous obtenons quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-7.41.25-PM-1.png)
_Code source React_

![Image](https://cdn-images-1.medium.com/max/1600/1*2_1elhifmL3-xdbGTRiEuw.png)

Et si vous simplifiez cela, nous obtenons ce qui suit :

```
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Blogs by Cybernatico" />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <link rel="manifest" href="/manifest.json" />
    <title>Blogs by Cybernatico</title>
    <link href="/static/css/2.877ae64e.chunk.css" rel="stylesheet" />
    <link href="/static/css/main.4d9c354c.chunk.css" rel="stylesheet" />
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>

    <script src="/static/js/2.48c493c5.chunk.js"></script>
    <script src="/static/js/main.f9b5cf72.chunk.js"></script>
  </body>
</html>
```

Et si vous regardez la sortie dans l'UI, ce sera quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-18-at-7.46.23-PM.png)
_Application React_

Dans le code source de cette page, nous n'obtenons que quelques lignes de code qui incluent le titre, les balises meta et les références de liens.

Mais dans le corps, nous n'avons que ceci :

```
<div id="root"></div>
```

Alors, où est le reste du code ? Nous ne le voyons pas dans le navigateur lorsque la page se charge. Cela est dû au fait que React utilise le rendu côté client (CSR). Une application React traite le DOM côté client, c'est-à-dire dans le navigateur.

Chaque fois que nous chargeons une application React, tous les composants UI sont générés sur le navigateur, de manière dynamique.

## Comment Next.js et le SSR fonctionnent

Si vous faites les mêmes choses que précédemment, mais avec une application Next.js, vous obtiendrez quelque chose de différent :

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Next.js Tutorial</title>
    <meta name="description" content="This is a Next.js Tutorial" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="next-head-count" content="5" />
    <noscript data-n-css=""></noscript>
  </head>
  <body>
    <div id="__next">
      <div>
        <h2>This is the Home Page!</h2>
        <a href="/profile/1"><p>Go to the Profile Page of 1!</p></a>
      </div>
    </div>
  </body>
</html>
```

Maintenant, voici le code source d'une simple application Next.js. Nous voyons tout le contenu, comme le HTML, le CSS et le JavaScript.

Cela signifie que lorsqu'une application Next.js se charge, le contenu sur le web que nous voyons dans l'UI est déjà généré. Et cela se produit sur le serveur. C'est parce que Next.js utilise le rendu côté serveur (ou SSR), également connu sous le nom de pré-rendu.

## Qu'est-ce que le pré-rendu ?

Le pré-rendu est un exemple de rendu côté serveur où le contenu est généré à l'avance, avant de charger l'application ou le site web sur le navigateur.

### Pourquoi utiliser le pré-rendu ?

Le rendu côté serveur (ou pré-rendu) rend une application plus rapide à charger. Cela est dû au fait que la sortie que nous allons voir est déjà générée côté serveur. Elle n'a pas besoin d'être générée sur le navigateur. Cela rend une application côté serveur plus rapide qu'une application côté client.

## Merci d'avoir lu !

Maintenant, vous devriez en savoir plus sur les principales différences entre Next.js et React. React utilise le CSR ou le rendu côté client, où les éléments de l'UI sont générés sur le navigateur. Dans Next.js, l'UI provient du serveur, générée à l'avance.

Si vous souhaitez développer des applications comme des sites de commerce électronique, des sites marketing ou des pages de destination simples, vous pouvez utiliser Next.js. Si vous voulez développer des applications comme des applications de médias sociaux ou des outils de streaming comme Netflix ou YouTube, vous pouvez opter pour React.

Si vous souhaitez regarder une version vidéo de ce blog, vous pouvez la trouver ici : [Next.js Framework Course

Pre-Rendering in Next.js](https://youtu.be/3oV9SgC8ufI).

Et si vous voulez en savoir plus sur Next.js, je crée un cours à ce sujet. C'est une playlist où vous apprendrez tout sur Next.js. Elle est encore en cours. Consultez-la ici : [https://youtube.com/playlist?list=PLWgH1O_994O_8Hg0-Q1xaD8ewXMx-fsBb](https://youtube.com/playlist?list=PLWgH1O_994O_8Hg0-Q1xaD8ewXMx-fsBb)