---
title: Comment utiliser HTML pour ouvrir un lien dans un nouvel onglet
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-09-08T04:29:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98dd740569d1a4ca1c7d.jpg
tags:
- name: Browsers
  slug: browsers
- name: HTML
  slug: html
- name: Security
  slug: security
seo_title: Comment utiliser HTML pour ouvrir un lien dans un nouvel onglet
seo_desc: 'Tabs are great, aren''t they? They allow the multitasker in all of us to
  juggle a bunch of online tasks at the same time.

  Tabs are so common now that, when you click on a link, it''s likely it''ll open
  in a new tab.

  If you''ve ever wondered how to do tha...'
---

Les onglets sont géniaux, n'est-ce pas ? Ils permettent à chacun de nous de jongler avec plusieurs tâches en ligne en même temps.

Les onglets sont si courants maintenant que, lorsque vous cliquez sur un lien, il est probable qu'il s'ouvre dans un nouvel onglet.

Si vous vous êtes déjà demandé comment faire cela avec vos propres liens, vous êtes au bon endroit.

## L'élément d'ancrage

Pour créer un lien sur une page web, vous devez envelopper un élément d'ancrage (`<a>`) autour du texte, puis définir son attribut `href` vers l'URL que vous souhaitez lier.

```html
<p>Consultez <a href="https://www.freecodecamp.org/">freeCodeCamp</a>.</p>
```

<style>
    .link-ex {
    	text-align: center;
    }
</style>
<p class="link-ex">Consultez <a href="https://www.freecodecamp.org/">freeCodeCamp</a>.</p>

Si vous cliquez sur le lien ci-dessus, le navigateur ouvrira le lien dans la fenêtre ou l'onglet actuel. C'est le comportement par défaut dans tous les navigateurs.

Pour ouvrir un lien dans un nouvel onglet, nous devons examiner certains des autres attributs de l'élément d'ancrage.

## L'attribut Target

Cet attribut indique au navigateur comment ouvrir le lien.

Pour ouvrir un lien dans un nouvel onglet, il suffit de définir l'attribut `target` sur `_blank` :

```html
<p>Consultez <a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp</a>.</p>
```

Maintenant, lorsque quelqu'un clique sur le lien, il s'ouvrira dans un nouvel onglet, ou éventuellement dans une nouvelle fenêtre, selon les paramètres du navigateur de la personne.

## Problèmes de sécurité avec `target="_blank"`

Je vous recommande fortement d'ajouter toujours `rel="noreferrer noopener"` à l'élément d'ancrage chaque fois que vous utilisez l'attribut `target` :

```html
<p>Consultez <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp</a>.</p>
```

Cela donne le résultat suivant :

<style>
    .link-ex {
    	text-align: center;
    }
</style>
<p class="link-ex">Consultez <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp</a>.</p>

L'attribut `rel` définit la relation entre votre page et l'URL liée. Le définir sur `noopener noreferrer` permet de prévenir un type de hameçonnage connu sous le nom de [tabnabbing](https://en.wikipedia.org/wiki/Tabnabbing).

## Qu'est-ce que le tabnabbing ?

Le tabnabbing, parfois appelé reverse tabnabbing, est une faille qui utilise le comportement par défaut du navigateur avec `target="_blank"` pour obtenir un accès partiel à votre page via l'API `window.object`.

Avec le tabnabbing, une page vers laquelle vous créez un lien pourrait provoquer la redirection de votre page vers une fausse page de connexion. Cela serait difficile à remarquer pour la plupart des utilisateurs car l'attention serait portée sur l'onglet qui vient de s'ouvrir – et non sur l'onglet d'origine avec votre page.

Ensuite, lorsque la personne revient à l'onglet avec votre page, elle verrait la fausse page de connexion et pourrait entrer ses identifiants.

Si vous souhaitez en savoir plus sur le fonctionnement du tabnabbing et sur ce que les mauvais acteurs peuvent faire avec cette faille, consultez [l'article d'Alex Yumashev](https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/) et celui de [OWASP](https://owasp.org/www-community/attacks/Reverse_Tabnabbing).

Si vous souhaitez voir un exemple de travail _sécurisé_, consultez cette [page](https://mathiasbynens.github.io/rel-noopener/) et son [dépôt GitHub](https://github.com/mathiasbynens/rel-noopener) pour plus d'informations sur la faille et l'attribut `rel`.

## En résumé

Il est facile d'utiliser HTML pour ouvrir un lien dans un nouvel onglet. Vous avez simplement besoin d'un élément d'ancrage (`<a>`) avec trois attributs importants :

1. L'attribut `href` défini sur l'URL de la page que vous souhaitez lier,
2. L'attribut `target` défini sur `_blank`, qui indique au navigateur d'ouvrir le lien dans un nouvel onglet/fenêtre, selon les paramètres du navigateur, et
3. L'attribut `rel` défini sur `noreferrer noopener` pour prévenir les éventuelles attaques malveillantes provenant des pages que vous liez.

Voici à nouveau un exemple complet fonctionnel :

```html
<p>Consultez <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp</a>.</p>
```

Ce qui donne le résultat suivant dans le navigateur :

<style>
    .link-ex {
    	text-align: center;
    }
</style>
<p class="link-ex">Consultez <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp</a>.</p>

Merci encore d'avoir lu. Bon codage.