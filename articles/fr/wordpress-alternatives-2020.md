---
title: Alternatives à WordPress – Comment choisir le bon CMS pour votre site
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-19T16:21:38.000Z'
originalURL: https://freecodecamp.org/news/wordpress-alternatives-2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cms.png
tags:
- name: cms
  slug: cms
- name: WordPress
  slug: wordpress
seo_title: Alternatives à WordPress – Comment choisir le bon CMS pour votre site
seo_desc: 'By Yehuda Clinton

  WordPress is powerful and versatile and it powers more of the internet''s web pages
  than any other engine.

  But it''s not a perfect fit for everyone. And perhaps you''re looking for something
  different. So let me help guide you through ...'
---

Par Yehuda Clinton

WordPress est puissant et polyvalent et il alimente plus de pages web de l'internet que tout autre moteur.

Mais ce n'est pas la solution idéale pour tout le monde. Et peut-être cherchez-vous quelque chose de différent. Alors laissez-moi vous guider à travers le monde confus de la gestion de contenu web moderne.

Pour ce faire, nous allons comparer les principaux systèmes de gestion de contenu (CMS) construits à partir de chacune des trois familles de langages de programmation dominants : PHP, Node et Python.

Toutes les options que j'explorerai sont open source. Ce qui est approprié, puisque de nombreuses manières, WordPress a été un pionnier dans les plateformes open source.

Cependant, certains d'entre nous recherchent un CMS plus moderne, plus rapide et plus sécurisé. Et nous n'aimons toujours pas les solutions propriétaires comme Squarespace et Wix.

Ce qui semble se passer, c'est que les gens s'éloignent des plateformes CMS construites sur un seul moteur, le paradigme [MVC](https://www.freecodecamp.org/news/simplified-explanation-to-mvc-5d307796df30/), pour un système plus découplé.

Par exemple, votre blog a-t-il vraiment besoin d'une base de données complète ? Et votre système de commerce électronique ou de paiement pourrait-il utiliser un paradigme [headless](https://www.mobify.com/insights/headless-commerce/) plus simple ?

Alors voyons ce qui est disponible, organisé par langage.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-102.png align="left")

## PHP

PHP est un langage simple, fiable et bien maintenu. Il n'est donc pas surprenant qu'il soit devenu le backend le plus populaire de tout le web.

Sa polyvalence permet aux développeurs de fournir de larges gammes de fonctionnalités et de plugins pour leurs CMS. En bref, PHP a été initialement [inventé pour les CMS](https://www.elated.com/cms-in-an-afternoon-php-mysql/).

Un inconvénient de la popularité de WordPress est que son marché de plugins est difficile à naviguer ou, dans certains cas, peut-être trop cher.

Cependant, WordPress n'est peut-être pas unique en ce sens. Voici quelques autres frameworks CMS PHP :

* **Drupal**

* **Joomla**

* **Magento**

* **Grav CMS**

Les trois premiers ont tous le même problème que WordPress : une interface encombrée ou un marché de plugins surchargé.

Mais Grav semblait être un bol d'air frais. C'est un peu comme un WordPress simplifié sans tout le bloatware complexe. Il n'y a même pas de base de données, juste des dossiers et des pages.

Il tente de vous offrir le meilleur des deux mondes. Grav dispose d'un plugin de tableau de bord d'administration pour que les non-techniciens puissent tout gérer comme ils le feraient avec WordPress.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-104.png align="left")

En même temps, Grav offre également la stabilité et la personnalisation d'un système découplé. Vous n'avez même pas besoin d'une interface graphique d'administration si vous ne le souhaitez pas.

## Node

Node.js, le langage le plus récent à frapper le marché backend, est innovant et peu conventionnel. Puisqu'il est déjà un langage populaire pour le développement web frontend, il semble que Node se positionne comme le langage de programmation le plus populaire partout.

Les déploiements Node reposent souvent sur des stacks technologiques telles que les bases de données NoSQL comme MongoDB, les serveurs web NGINX et Markdown. Un avantage d'un CMS alimenté par Node.js est qu'il tend à bien s'intégrer avec les applications web.

Voici quelques CMS basés sur Node.js :

* **KeystoneJs** : Complexe. Plus un framework qu'un CMS.

* **Ghost** : Simple. Ne fait pas beaucoup plus que Medium, ce qui est parfait si vous souhaitez héberger vous-même votre blog Medium. Vous pouvez ajouter un eCommerce découplé comme Shopify.

* **NetlifyCMS** : Ce n'est pas un CMS autonome – plutôt, vous l'ajoutez à un site web/application web en tant que gestionnaire de contenu statique basé sur git personnalisé pour vos rédacteurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-105.png align="left")

D'un point de vue parts de marché, Ghost semble être le seul nouveau CMS [positionné pour prendre une part du monopole de WordPress](https://www.datanyze.com/market-share/wcms--7/ghost-vs-wordpress).

## Python

Bien que Python soit connu comme un langage de script puissant, ces dernières années, il a mûri pour devenir un langage serveur polyvalent. Cependant, il dispose toujours d'un marché de plugins et de thèmes beaucoup moins développé pour ses CMS.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-106.png align="left")

Voici quelques plateformes CMS populaires basées sur Python :

* **Django CMS** : Nécessite un peu plus de connaissances en code que WordPress

* **Mezzanine** : Également construit sur Django. De nombreuses fonctionnalités, mais vous devez toujours connaître Python pour les fonctionnalités avancées.

* **Storyblok** : interface d'édition conviviale et API headless pour les applications mais plugins limités

Python a l'avantage de la vitesse dans certaines situations. Et donc les frameworks Python pourraient potentiellement évoluer beaucoup plus efficacement que JavaScript. De plus, c'est pourquoi ils fonctionneront souvent mieux sur du matériel peu coûteux comme un Raspberry Pi.

Ces CMS basés sur Python pourraient également trouver leur niche lorsqu'ils s'intègrent à un domaine dominé par Python. De quels domaines parlons-nous ici ? Consultez cet article et découvrez [à quoi sert Python](https://www.freecodecamp.org/news/what-is-python-used-for-10-coding-uses-for-the-python-programming-language/).

Quoi qu'il en soit, je doute que Python devienne jamais un concurrent majeur sur le marché des CMS. Principalement parce qu'il est arrivé très tard sur le web. Le manque de compatibilité ascendante entre les versions est également un problème.

## Conclusion

Si vous êtes prêt à embrasser l'avenir des CMS, voici les clés pour prendre une décision éclairée.

Prenez en compte tous les facteurs qui vous donneront probablement toute la sécurité, la fiabilité et la personnalisation dont vous avez besoin.