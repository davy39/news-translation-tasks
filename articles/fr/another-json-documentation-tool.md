---
title: Un autre outil de documentation Json
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-02T17:08:12.000Z'
originalURL: https://freecodecamp.org/news/another-json-documentation-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Untitled.png
tags:
- name: api
  slug: api
- name: documentation
  slug: documentation
- name: json
  slug: json
seo_title: Un autre outil de documentation Json
seo_desc: 'By Bhuvan Gupta

  There are many JSON structure documentation tool, I have build one more for my office
  work .https://jsondoc.online

  For me i can classify them in :

  1. Code decorative tools

  Tools that require to add an annotation in code and then tools...'
---

Par Bhuvan Gupta

Il existe de nombreux outils de documentation de structure JSON, j'en ai créé un autre pour mon travail de bureau. [https://jsondoc.online](https://jsondoc.online/)

Pour moi, je peux les classer en :

# **1. Outils de décoration de code**

Outils qui nécessitent d'ajouter une annotation dans le code, puis les outils génèrent la documentation à partir de celle-ci. Par exemple : Swagger

# 2. **Outils déclaratifs**

Outils qui nécessitent de remplir du texte dans un schéma particulier, puis les outils l'analysent et génèrent une vue de documentation. Par exemple : Spécification Json Schema

# Pourquoi créer un autre outil ?

Les outils existants nécessitent une compréhension forte/clare de ce que Json représente
OU
Il suppose que tous les membres/équipes comprennent le schéma pour le définir/modifier.

**Mais**, en pratique, j'ai trouvé des gens partageant des requêtes et réponses dans Google Doc pour obtenir une approbation.
Google Doc est bien, mais lorsque je partage une réponse proposée de mon service au format Json imbriqué dans Google Doc, d'autres équipes ont du mal à la comprendre, à l'utiliser et à en faire un modèle mental intuitif.

Par conséquent, j'ai créé un outil où l'on peut :

1. Ajouter une structure JSON et la partager avec un lien.
2. D'autres équipes peuvent **jouer avec la structure arborescente Json**.
3. Un panneau de documentation où l'on peut voir/ajouter de la documentation.

---

Code source : [https://github.com/bhuvangu/jsondoc.online](https://github.com/bhuvangu/jsondoc.online)

> _motivation : Problème personnel au travail_



---