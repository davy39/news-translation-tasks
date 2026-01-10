---
title: Comment implémenter le sondage de données avec React, Redux et Thunk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-03T21:30:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-data-polling-with-react-redux-and-thunk-33cd1e47f89c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*klkJzqlPXCAjyjv9
tags:
- name: JavaScript
  slug: javascript
- name: polling
  slug: polling
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment implémenter le sondage de données avec React, Redux et Thunk
seo_desc: 'By Valerii Tereshchenko

  Introduction

  In my previous article How to load Data in React with Redux-Thunk, Redux-Saga, Suspense
  & Hooks I compared different ways of loading data from the API. Quite often in web
  applications, data needs to be updated fre...'
---

Par Valerii Tereshchenko

### Introduction

Dans mon article précédent [How to load Data in React with Redux-Thunk, Redux-Saga, Suspense & Hooks](https://medium.freecodecamp.org/loading-data-in-react-redux-thunk-redux-saga-suspense-hooks-666b21da1569), j'ai comparé différentes façons de charger des données depuis une API. Très souvent, dans les applications web, les données doivent être mises à jour fréquemment pour afficher des informations pertinentes à l'utilisateur. Le sondage court est l'une des façons de le faire. Consultez [cet](https://codeburst.io/polling-vs-sse-vs-websocket-how-to-choose-the-right-one-1859e4e13bd9) article pour plus de détails…