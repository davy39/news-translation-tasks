---
title: 'Une introduction à JAMstack : l''architecture du web moderne'
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-05-17T14:59:56.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xYSNCnp6eh2ZDpwQtYL6qg.jpeg
tags:
- name: api
  slug: api
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction à JAMstack : l''architecture du web moderne'
seo_desc: I’m sure you’ve come across the word JAMstack before but you might not have
  understood what it really meant. I’ve seen this word before also but didn’t care
  to check it out until Egwuenu Gift organized JAMstack Lagos. I then realized that
  I’ve been b...
---

Je suis sûr que vous avez déjà rencontré le terme JAMstack, mais vous n'avez peut-être pas compris ce qu'il signifiait vraiment. J'avais aussi vu ce mot auparavant, mais je ne me suis pas donné la peine de le vérifier jusqu'à ce que [Egwuenu Gift](https://www.freecodecamp.org/news/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca/undefined) organise [JAMstack Lagos](https://twitter.com/jamstacklagos). J'ai alors réalisé que je construisais déjà des applications JAMstack.

JAMstack est une architecture de développement web moderne. Ce n'est pas un langage de programmation ni un outil quelconque. C'est plutôt une pratique de développement web visant à améliorer les performances, à renforcer la sécurité, à réduire le coût de mise à l'échelle et à améliorer l'expérience des développeurs.

Dans cet article, je vais vous présenter ce que signifie JAMstack, pourquoi vous devriez vous y intéresser, les meilleures pratiques et comment commencer. ?

### Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/oE3wYE3Ygr1SlH2dTXkM5lXW-DyHPlmMrQww align="left")

Selon la documentation officielle de [JAMstack](https://jamstack.org/),

> JAMstack est une architecture de développement web moderne basée sur JavaScript côté client, des API réutilisables et du balisage préconstruit.

> Lorsque nous parlons de "la pile", nous ne parlons plus de systèmes d'exploitation, de serveurs web spécifiques, de langages de programmation backend ou de bases de données.

> JAMstack ne concerne pas des technologies spécifiques. C'est une nouvelle façon de construire des sites web et des applications qui offre de meilleures performances, une sécurité accrue, un coût de mise à l'échelle réduit et une meilleure expérience pour les développeurs.

**JAMstack** est une tendance majeure dans le développement web, inventée par [Mathias Biilman](https://twitter.com/biilmann), PDG et cofondateur de Netlify.

### D'accord, calme-toi ! Qu'est-ce que JAMstack ?

Vous avez peut-être rencontré des termes spécifiques comme **pile MEAN** et **pile MERN**. Ce ne sont que des termes utilisés pour classer ou regrouper certaines technologies dans le but d'atteindre un objectif particulier.

JAMstack signifie ici

**J**avaScript

**A**PI

**M**arkup

> Les piles sont généralement simplement une combinaison de plusieurs technologies utilisées pour créer une application web ou mobile. Ainsi, JAMstack est la combinaison de JavaScript, d'API et de balisage. Plutôt intéressant, n'est-ce pas ?

Les projets JAMstack ne dépendent pas du code côté serveur — ils peuvent être distribués au lieu de dépendre d'un serveur. Servis directement depuis un CDN, les applications JAMstack débloquent la vitesse, les performances et améliorent l'expérience utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/x0eO1iqvIRKPNsEtSkFvRuLu6CbSmo7OhcFH align="left")

### Termes utiles

J'utiliserai fréquemment ces termes dans cet article et j'ai pensé que vous devriez connaître leurs significations (si vous ne les connaissez pas déjà) :

* **API** est l'acronyme de Application Programming Interface, qui est un intermédiaire logiciel permettant à deux applications de communiquer entre elles.

* **CDN** (content delivery network) est un système de serveurs distribués (réseau) qui livre des pages et d'autres contenus web à un utilisateur, en fonction des emplacements géographiques de l'utilisateur, de l'origine de la page web et du serveur de livraison de contenu.

* Un **Serveur** est un ordinateur conçu pour traiter des requêtes et fournir des données à un autre ordinateur via internet ou un réseau local.

* Une **Base de données** est une collection d'informations organisée de manière à pouvoir être facilement accessible, gérée et mise à jour.

### Pourquoi JAMstack ?

![Image](https://cdn-media-1.freecodecamp.org/images/uHGkEXe8lXJsmj6cZNQmIW3bpsEzn0mU9Eun align="left")

Les sites web traditionnels ou les sites CMS (par exemple WordPress, Drupal, etc.) dépendent fortement des serveurs, des plugins et des bases de données. Mais JAMstack peut charger du JavaScript qui reçoit des données d'une API, servant des fichiers depuis un CDN et du balisage généré à l'aide d'un générateur de site statique lors du déploiement.

Ça a l'air cool, non ?!

#### JAMstack est rapide

En matière de minimisation du temps de chargement, rien ne bat les fichiers préconstruits servis via un CDN. Les sites JAMstack sont super rapides car le HTML est déjà généré lors du déploiement et simplement servi via un [CDN](https://flaviocopes.com/cdn/) sans aucune interférence ou retard backend.

#### JAMstack est hautement sécurisé

Tout fonctionne via une API et donc il n'y a pas de violations de base de données ou de sécurité. Avec les processus côté serveur abstraits en API de microservices, les surfaces d'attaque sont réduites et votre site devient donc hautement sécurisé.

#### JAMstack est moins cher et plus facile à mettre à l'échelle

Les sites JAMstack ne contiennent que quelques fichiers de taille minimale qui peuvent être servis n'importe où. La mise à l'échelle consiste simplement à servir ces fichiers ailleurs ou via des CDN.

### Bonnes pratiques JAMstack

* Utilisez un CDN pour distribuer vos fichiers plutôt que des serveurs

* L'installation et la contribution à votre projet doivent être faciles et peu complexes. Utilisez des outils comme npm et Git pour garantir une configuration standard et plus rapide.

* Utilisez des outils de construction et rendez votre projet compatible avec tous les navigateurs (par exemple Babel, Browserify, Webpack, etc.)

* Assurez-vous que votre projet est conforme aux normes web et hautement accessible

* Assurez-vous que votre processus de construction est automatisé pour réduire le stress.

* Rendez votre processus de déploiement automatique, vous pouvez utiliser des plateformes comme [Netlify](https://netlify.com) pour cela

### Comment commencer ?

Vous pouvez utiliser certaines technologies déjà construites pour créer des applications JAMstack en quelques minutes. En voici quelques-unes :

* [**Gatsby**](https://www.gatsbyjs.org/) : Gatsby est un framework gratuit et open source basé sur React qui aide les développeurs à construire des **sites web et des applications** ultra-rapides

* [**NuxtJS**](https://nuxtjs.org/) : NuxtJS est le framework Vue.js pour les applications universelles, les applications générées statiquement, les applications monopages, les applications web progressives et les applications de bureau

* [**Hugo**](http://gohugo.io) : Hugo est le framework le plus rapide au monde pour construire des sites web. C'est l'un des générateurs de sites statiques open source les plus populaires. Avec sa vitesse et sa flexibilité incroyables, Hugo rend la construction de sites web amusante à nouveau.

* [**Netlify CMS**](https://www.netlifycms.org/) : Netlify CMS est un système de gestion de contenu open source pour votre flux de travail Git qui peut être utilisé avec n'importe quel générateur de site statique pour un projet web plus rapide et plus flexible

* [**Contentful**](https://www.contentful.com) : Contentful est un système de gestion de contenu plus intelligent et transparent qui fournit aux éditeurs et aux développeurs un contenu unifié, améliorant ainsi la collaboration et garantissant que les produits numériques sont livrés sur le marché plus rapidement.

* [**Svelte**](https://svelte.dev/) : Svelte est une nouvelle approche radicale pour construire des interfaces utilisateur. Alors que les frameworks traditionnels comme React et Vue font le gros de leur travail dans le *navigateur*, Svelte déplace ce travail dans une *étape de compilation* qui se produit lorsque vous construisez votre application.

[***et bien d'autres...***](https://www.staticgen.com/)

### Ressources utiles

* [**JAMstack WTF**](https://jamstack.wtf/)

* [**Comment construire un site web JAMstack**](https://cosmicjs.com/blog/how-to-build-a-jamstack-website)

* [**Qu'est-ce que JAMstack et pourquoi devriez-vous l'essayer**](https://www.giftegwuenu.com/what-is-ja-mstack-and-why-you-should-try-it)

* [**Un CMS prêt pour JAMstack**](https://www.contentful.com/r/knowledgebase/jamstack-cms/)

* [**JAMstack pour les clients : sur les avantages et le CMS de site statique**](https://snipcart.com/blog/jamstack-clients-static-site-cms)

* [**Passez au statique : 5 raisons d'essayer JAMstack sur votre prochain projet**](https://builtvisible.com/go-static-try-jamstack/)

* [**Sites web statiques + JAMstack = ❤**](https://julian.is/article/static-websites-and-jamstack/)

Trouvez plus de ressources [ici](https://jamstack.org/resources/)

%[https://www.youtube.com/watch?v=uWTMEDEPw8c]

### Conclusion

JAMstack a été inventé comme un moyen de nommer la nouvelle façon de construire des sites web et des applications qui offrent de meilleures performances, une sécurité accrue, un coût de mise à l'échelle réduit et une meilleure expérience pour les développeurs.

JAMstack ne concerne pas des technologies spécifiques, c'est une architecture de développement web moderne basée sur JavaScript côté client, des API réutilisables et du balisage préconstruit.

Rejoignez la [communauté JAMstack](https://jamstack.org/community/) pour en savoir plus et obtenir plus de mises à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/BoR0w2G9fjZDSJDFTlZoGE4gK810ODcs8vz3 align="left")

> PS : Cet article a été publié pour la première fois sur mon blog [ici](https://bolajiayodeji.com/an-introduction-to-the-jamstack-the-architecture-of-the-modern-web-c4a0d128d9ca)