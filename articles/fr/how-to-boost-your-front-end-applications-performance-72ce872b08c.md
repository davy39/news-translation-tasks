---
title: Comment améliorer les performances de votre application front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T19:19:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-your-front-end-applications-performance-72ce872b08c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vmq3ETGdUZPZe9vZu6CkVg.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: Web Development
  slug: web-development
seo_title: Comment améliorer les performances de votre application front-end
seo_desc: 'By Dimitris Kiriakakis

  If your website takes longer than 3 seconds to load, you could already be losing
  nearly half of your visitors.

  Yes this is a fact, proven by several research studies. Long loading times can have
  a devastating impact on your app...'
---

Par Dimitris Kiriakakis

Si votre site web met plus de 3 secondes à charger, vous pourriez déjà perdre près de la moitié de vos visiteurs.

Oui, c'est un fait, prouvé par plusieurs études de recherche. Les longs temps de chargement peuvent avoir un impact **dévastateur** sur les taux de conversion de votre application. En revanche, l'optimisation du temps de chargement des pages conduit à des améliorations notables de l'expérience client, des taux de conversion, du SEO et, en fin de compte, du **succès** de votre produit.

Alors, disons que vous avez récemment construit un site web ou une application front-end en utilisant un framework JS moderne (Angular, React, VueJS, etc.). Comment pouvons-nous nous assurer que les performances ne vont pas l'empêcher de réussir ?

D'abord, nous devons somehow gather some **data**. Lorsqu'il s'agit de mesurer les performances d'une application front-end, les outils en lesquels j'ai le plus confiance sont :

* Google chrome's [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
* [Speedcurve](https://speedcurve.com/)

Les deux outils peuvent vous aider à suivre tous les principaux KPI de performance (Indice de vitesse de page, Temps jusqu'à l'interactivité, Première peinture de contenu, etc.).

**Lighthouse** est inclus dans les outils de développement de Chrome, et en analysant votre site web/application web, il peut vous donner des conseils vraiment utiles sur la façon de le booster.

![Image](https://cdn-media-1.freecodecamp.org/images/To1jGG1giiJeWCpEVTGl1v2Hznyz4eKcRncT)
_Chrome's lighthouse peut vous donner des conseils vraiment utiles_

Avec **Speedcurve**, vous pouvez avoir tous ces KPI, plus la capacité de les surveiller au fil du temps.

Maintenant que nous sommes capables de mesurer notre succès, passons à l'optimisation des parties de notre site web qui jouent le plus grand rôle.

### Images

Les images sont une partie clé de chaque site web. En moyenne, les images représentent plus de 60 % des données chargées sur les pages web. Étant un composant si critique de presque tous les sites web, l'optimisation des images est, à mon avis, la plus importante, et peut-être le fruit le plus facile à cueillir.

#### 1. Redimensionnez vos images et rendez-les réactives.

La chose la plus importante à vérifier est que vous n'utilisez pas une résolution plus grande que celle dont vous avez vraiment besoin. Vous devez donc redimensionner vos images pour qu'elles correspondent exactement aux exigences de votre mise en page.

![Image](https://cdn-media-1.freecodecamp.org/images/PqV7uCLjZMyaZwwkQbMDtml61iC9UktvPOjm)
_Les mises en page réactives nécessitent des images réactives_

De plus, vous devez vous assurer que vos images sont aussi **réactives** que votre mise en page. Il existe un excellent outil que j'ai utilisé récemment, qui peut vous aider à générer toutes les différentes versions des images dont vous pourriez avoir besoin et également générer le code HTML5 qui peut les utiliser. Il s'appelle [Responsive Image Breakpoints Generator](https://www.responsivebreakpoints.com/). Je préfère généralement générer 8 à 10 images différentes.

Bien sûr, vous pouvez utiliser le code HTML5 généré dans n'importe quelle application ou site web front-end. De plus, si vous utilisez gulp, vous pourriez automatiser ce processus avec le plugin [gulp-responsive](https://github.com/mahnunchik/gulp-responsive).

#### 2. Assurez-vous qu'elles sont chargées de manière paresseuse.

Le chargement paresseux signifie essentiellement que nous différons le chargement des images qui ne sont pas nécessaires immédiatement. Typiquement, toute image qui n'est pas visible par les utilisateurs sur leur viewport actuel peut être chargée à un moment ultérieur, lorsque l'image entre ou est sur le point d'entrer dans le viewport.

Peu importe le framework que vous utilisez, vous pouvez trouver un plugin qui peut charger de manière paresseuse les images pour vous (par exemple, [v-lazy-image](https://github.com/alexjoverm/v-lazy-image) dans VueJS), cependant vous pourriez également construire votre propre implémentation. Assurez-vous simplement que vous utilisez la méthode moderne pour détecter quand un élément entre ou sort du viewport du navigateur, l'[IntersesectionObserver API](https://github.com/alexjoverm/v-lazy-image).

#### Bonus : Utilisez un CDN pour la livraison d'images

Si vous avez déjà optimisé la taille et le nombre d'images que votre site web charge, et surtout s'il va être disponible mondialement, vous pourriez également utiliser un **réseau de livraison de contenu** (CDN) pour les servir.

En quelques mots, un CDN met en cache vos images sur son réseau mondialement distribué de serveurs. Donc, si un utilisateur d'Australie demande une image de votre site web, au lieu de récupérer cette image de votre serveur en Europe, le CDN va la livrer depuis un autre serveur, plus proche de cet utilisateur en Australie. Cela réduit le temps de trajet nécessaire pour charger l'image.

### CSS, JS et HTML

Tous les frameworks modernes optimisent votre code pendant le temps de construction de production (division de code, tree-shaking, minification, etc.). Que pouvez-vous faire en plus de cela ?

#### 1. Optimisez le document HTML principal

Le HTML est l'épine dorsale de presque toutes les applications web. Lorsqu'il s'agit de référencer des ressources dans votre document HTML, il y a quelques bonnes pratiques que vous devriez suivre. Il est recommandé de :

* Placer les références CSS en haut de l'en-tête de votre document HTML afin de garantir un rendu progressif.
* Placer les attributs JavaScript en bas du corps de votre HTML et [préférer le chargement asynchrone des scripts](https://www.w3schools.com/tags/att_script_async.asp). Cela empêchera toute balise `<script>` de bloquer le processus de rendu HTML.

#### 2. Assurez-vous de ne charger que ce dont vous avez besoin

![Image](https://cdn-media-1.freecodecamp.org/images/YjYDfAVFIYx91chGjMBSGUhruQJs4vWHxMKB)
_Chargement paresseux des composants et modules_

Angular, React et VueJS vous fournissent tous des fonctionnalités de chargement paresseux. Vous n'avez qu'à diviser votre code correctement, selon vos propres besoins, et à ne charger que les modules dont vous avez besoin, dès que vous en avez vraiment besoin. Par exemple, si vous avez une application de commerce électronique, vous devez vous assurer que le module Panier ou le module Paiements ne sont pas chargés lorsque l'utilisateur est sur la page d'accueil.

### Compression et mise en cache

En général, pour tous les actifs qui sont essentiels à votre front-end (images et code), vous devez appliquer la compression et les mettre en cache correctement.

La compression de fichiers rendra les actifs de votre application un peu plus légers et diminuera le temps de trajet nécessaire pour les servir. L'une des méthodes de compression de fichiers les plus couramment utilisées est **Gzip**, une excellente méthode pour réduire les morceaux de code, les documents, les images et les fichiers audio.

[**Brotli**](https://github.com/google/brotli) est un autre algorithme de compression de fichiers, et il gagne en popularité. Cet algorithme open source est régulièrement mis à jour par des ingénieurs logiciels de Google et d'autres organisations. Il a prouvé qu'il pouvait compresser les fichiers avec un **taux bien meilleur** que les autres méthodes existantes.

Vous pouvez activer votre méthode de compression préférée sur nginx, apache ou tout autre serveur que vous utilisez, en modifiant leurs fichiers de configuration ([activer brotli sur nginx](https://www.howtoforge.com/tutorial/how-to-install-nginx-with-brotli-compression-on-ubuntu-1804/) ou [activer brotli sur apache](https://ayesh.me/apache-brotli)).

En ce qui concerne la mise en cache, la technique de mise en cache la plus couramment utilisée (également recommandée par Lighthouse) s'appelle **Leverage Browser Caching**. Encore une fois, vous pouvez l'activer en modifiant les fichiers de configuration de votre serveur ([activer Leverage Browser Caching](https://www.keycdn.com/blog/leverage-browser-caching)).

### Résumé

En ce qui concerne les sites web et les applications front-end, la performance est un sujet énorme et nous devons le prendre au sérieux.

J'espère que cet article vous a aidé à comprendre et vous a permis de traiter certaines des choses les plus importantes dont nous devons nous occuper lorsque nous voulons améliorer les performances d'une application.

Pour une liste de contrôle détaillée, assurez-vous de consulter la [Front-End-Performance-Checklist](http://ront-End-Performance-Checklist).

Santé ! ?