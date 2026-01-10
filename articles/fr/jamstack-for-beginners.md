---
title: Qu'est-ce que le Jamstack ? Tutoriel pour débutants
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2022-11-10T18:30:49.000Z'
originalURL: https://freecodecamp.org/news/jamstack-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Damilola-Oladele-2.png
tags:
- name: api
  slug: api
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: markup
  slug: markup
- name: Web Applications
  slug: web-applications
seo_title: Qu'est-ce que le Jamstack ? Tutoriel pour débutants
seo_desc: 'You may have heard the term Jamstack and have been wondering what it means.
  Well, the Jamstack is nothing more than a modern way of building web applications.

  Jamstack takes advantage of existing technologies – which we''ll discuss in a minute.
  The re...'
---

Vous avez peut-être entendu le terme Jamstack et vous vous demandez ce qu'il signifie. Eh bien, le Jamstack n'est rien de plus qu'une manière moderne de construire des applications web.

Le Jamstack tire parti des technologies existantes – que nous aborderons dans un instant. Le résultat est une meilleure performance, une sécurité améliorée et une scalabilité plus facile pour les applications web.

Dans cet article, vous apprendrez ce que signifie Jamstack et les avantages de l'utilisation de cette approche dans vos projets.

## Qu'est-ce que le Jamstack ?

Le Jamstack est une architecture de développement web. Matt Biilmann, le PDG de Netlify, l'a popularisée avec sa présentation à la Smashing Conference 2016.

Jamstack est un acronyme pour Javascript, APIs et Markup, et est une pile technologique que vous utilisez pour construire vos applications.

C'est comme la pile MERN (MongoDB, ExpressJS, ReactJS et NodeJS) et la pile MEAN (MongoDB, ExpressJS, Angular et NodeJS) – juste avec des outils différents.

Maintenant, discutons des différents composants d'une application web Jamstack :

### Javascript

Javascript est le langage de programmation principal du web. Il existe depuis des décennies et vous pouvez l'utiliser à la fois côté client et côté serveur avec NodeJS.

Javascript est le langage de programmation que vous utilisez pour gérer le côté client de vos applications Jamstack.

### APIs

API est un acronyme pour **Application Programming Interface**. C'est une interface qui aide deux ou plusieurs programmes informatiques à communiquer entre eux.

Dans les applications Jamstack, vous utilisez des APIs pour communiquer avec votre backend.

### Markup

Markup fait référence aux systèmes standard d'encodage de texte composés d'un ensemble de symboles insérés dans un document texte. Des exemples de langages de balisage sont **HTML**, **XML** et des langages de templating tels que **JSX**.

Dans le Jamstack, le markup fait référence au contenu d'une application Jamstack. Notez que nous utilisons ici le terme markup dans son sens large. Il ne fait pas référence uniquement au contenu textuel, mais aussi aux actifs de l'application web, tels que les images.

## Caractéristiques importantes des applications Jamstack

Pour qu'une application soit considérée comme une application Jamstack, elle doit répondre aux conditions suivantes :

### Architecture distribuée

Cela fait référence au découplage du côté client du backend. Le côté client gère la présentation de l'interface utilisateur, et le backend gère la logique métier et les données.

La communication entre le frontend et le backend se fait via une API dédiée. Cela signifie qu'un changement ou une mise à niveau dans l'un n'affectera pas l'autre. Cela entraîne une maintenance plus facile de l'ensemble de l'application web.

### Sites statiques

Il est important que les applications Jamstack servent des pages web statiques et non dynamiques.

Les applications web traditionnelles sont des sites dynamiques. Cela signifie que lorsque vous demandez une page, le backend devra accéder à une base de données pour récupérer les données. Les données sont ensuite utilisées pour générer des fichiers HTML, puis renvoyées au client.

L'inconvénient des sites dynamiques est le temps qu'il faut pour effectuer ces étapes.

Pour les sites statiques, les pages sont déjà pré-rendues au moment de la construction. Ainsi, chaque fois que vous demandez une page, vous obtenez la page pré-rendue.

Cela élimine le temps que les sites dynamiques passent à obtenir des données, à générer des fichiers HTML et à les renvoyer au client. Vous pouvez servir vos sites statiques à partir d'un [content delivery network (CDN).](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) Cela conduira à une vitesse améliorée et à des coûts réduits.

Des exemples de générateurs de sites statiques que vous pouvez utiliser pour vos applications web Jamstack incluent :

* NextJS
    
* Gatsby
    
* Hugo
    
* Jekyll
    
* Nuxt
    

## Pourquoi devriez-vous utiliser le Jamstack pour vos applications web ?

Discutons maintenant de certaines des raisons pour lesquelles l'architecture web Jamstack est devenue si populaire ces derniers temps et pourquoi vous devriez envisager de l'adopter :

### Les applications Jamstack sont scalables

Vous pouvez servir la plupart des applications Jamstack à partir d'un CDN. Cela permet un transfert rapide des actifs nécessaires au chargement des pages web.

En raison de la nature distribuée des CDN, votre application web sera également en mesure de gérer plus de trafic à un coût réduit.

### Les applications Jamstack sont faciles à maintenir

Les applications Jamstack sont plus faciles à maintenir puisque leur côté client est découplé de leur backend.

Cela signifie que vous pouvez maintenir une partie sans nécessiter de modifications majeures à l'autre.

### Les applications Jamstack se chargent plus rapidement

Comme mentionné précédemment, servir votre site à partir d'un CDN augmente la vitesse à laquelle il se charge.

De plus, dans les applications Jamstack, les pages web sont préconstruites, ce qui permet d'économiser le temps qui serait normalement passé à récupérer et à générer des fichiers HTML chaque fois que vous faites une demande.

### Les applications Jamstack sont moins chères

Puisque les applications Jamstack sont plus faciles à maintenir et à déployer, elles sont moins chères par rapport à leurs homologues traditionnels.

### Les applications Jamstack sont plus sécurisées

Puisque vous n'avez pas à maintenir constamment un serveur dans les applications Jamstack et que les pages sont construites sur des fichiers en lecture seule (c'est-à-dire que les pages sont statiques), vous pouvez vous soucier moins de la sécurité de vos applications.

## Conclusion

Malgré le fait que de plus en plus de projets sont construits en utilisant l'architecture Jamstack, nous en sommes encore aux premiers stades de son adoption.

Je crois que de plus en plus de grandes et petites entreprises l'adopteront dans un avenir proche pour remplacer les architectures monolithiques coûteuses.