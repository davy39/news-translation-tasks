---
title: 5 extensions WordPress pour améliorer les performances de votre site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-23T02:09:07.000Z'
originalURL: https://freecodecamp.org/news/wordpress-plugins-to-improve-your-website-performance
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/5-WordPress-Plugins-for-Improving-Your-Website-Performance.png
tags:
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
- name: WordPress
  slug: wordpress
seo_title: 5 extensions WordPress pour améliorer les performances de votre site web
seo_desc: "By Andrej Gajdos\nIn this blog post, I will show you which free WordPress\
  \ plugins you should use and how to configure them to significantly improve your\
  \ WordPress website's performance. \nWeb performance is an essential SEO factor,\
  \ and you shouldn’t un..."
---

Par Andrej Gajdos

Dans cet article de blog, je vais vous montrer quelles extensions WordPress gratuites vous devriez utiliser et comment les configurer pour améliorer significativement les performances de votre site web WordPress. 

La performance web est un facteur SEO essentiel, et vous ne devriez pas la sous-estimer. Chaque seconde que votre site met à charger peut nuire à votre entreprise et à votre retour sur investissement.

Heureusement, WordPress offre de nombreuses options et extensions qui peuvent vous aider à améliorer les performances sans connaissances approfondies en développement logiciel.

## Meilleures extensions WordPress pour les performances du site web

Dans cet article, je vais vous présenter 5 extensions qui peuvent vous aider à corriger les performances de votre site web. Elles fonctionnent ensemble sans aucun problème de compatibilité si vous les configurez correctement. 

Je travaille en tant que [spécialiste SEO](https://ivananeckarova.com/en/czech-seo-specialist/?utm_source=Dzone&utm_medium=Article&utm_campaign=web_performance_plugin) et j'utilise ces extensions pour mes projets. Gardez simplement à l'esprit que certaines extensions ou leurs paramètres peuvent affecter la fonctionnalité de votre site web. Chaque fois que vous changez ou installez une nouvelle extension, il est nécessaire de tester votre site web pour vérifier que tout fonctionne comme prévu.

## 1. Extension WordPress W3 Total Cache

Cette extension est l'une des plus avancées pour l'optimisation des performances du site web et offre de nombreuses options. 

W3 Total Cache améliore les performances en mettant en cache vos sites, en améliorant les performances du serveur et en réduisant le temps de chargement. Soyez prudent si vous utilisez une autre extension pour la mise en cache, cependant - dans ce cas, vous devriez la désactiver ou la désinstaller. Sinon, il y aura des problèmes lorsque vous activerez celle-ci.

### Comment configurer W3 Total Cache

Tout d'abord, installez [W3 Total Cache](https://cs.wordpress.org/plugins/w3-total-cache/) sur votre WordPress. Après avoir installé avec succès l'extension, trouvez l'élément Performance dans vos paramètres WordPress et choisissez l'élément "Paramètres généraux".



![Image](https://www.freecodecamp.org/news/content/images/2021/11/1..PNG)
_W3 Total Cache - trouvez Performance dans le Menu._

Dans les Paramètres généraux, activez **Page Cache**. Page Cache crée des pages de cache statiques chaque fois qu'une page est chargée, de sorte que la page n'est pas chargée dynamiquement. Si vous ne changez pas votre contenu quotidiennement, alors vous en avez besoin ! Avec la mise en cache activée, vous pouvez réduire significativement votre temps de chargement. 

Dans la Méthode de Cache de Page, utilisez Disque : Amélioré. Cela est valable pour tous ceux qui utilisent un hébergement partagé.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/2..PNG)
_W3 Total Cache - activez Page Cache._

La **Minification** est l'une des optimisations de performance les plus fondamentales. La minification est un processus de minimisation des fichiers HTML, CSS et JavaScript en supprimant tous les caractères qui ne sont pas nécessaires dans le code (sauts de ligne, espaces supplémentaires, etc.). Cela réduira la taille de ces fichiers et diminuera les temps de chargement. 

Vous pouvez utiliser diverses extensions WordPress pour la minification. W3 Total Cache offre également cette option. Si vous utilisez Cloudflare, vous pouvez activer la minification là-bas au lieu d'utiliser W3 Total Cache.



![Image](https://www.freecodecamp.org/news/content/images/2021/11/3..PNG)
_W3 Total Cache - activez Minify._

Ensuite, vous pouvez activer **Object Caching**. Object Caching signifie stocker les résultats des requêtes de la base de données. Ainsi, lorsque vous avez besoin d'un résultat la prochaine fois, il est servi par un cache sans avoir besoin de requêter à plusieurs reprises la base de données. 

Object Caching aide à réduire la charge sur votre base de données et votre serveur, et il livre les requêtes plus rapidement. 

La Méthode de Cache d'Objets dans le cas d'un hébergement partagé est Disque. Testez votre vitesse avant et après avoir activé Object Cache - dans certains cas, cela peut ralentir votre site web.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/4..PNG)
_W3 Total Cache - activez Object Cache._

Ensuite, vous pouvez activer **Browser Caching**. Cela signifie que les images, HTML, CSS et JS (actifs statiques) sont stockés dans votre navigateur. Browser Caching chargera votre site web plus rapidement pour vos utilisateurs lorsqu'ils visiteront à nouveau votre site web.

Dans mon cas, je n'ai pas activé Browser Caching, car j'utilise l'extension Polylang et il y a un [problème de compatibilité](https://wordpress.org/support/topic/w3-polylang-not-working-correctly-from-0-9-7-3/). [L'extension Polylang](https://wordpress.org/plugins/polylang/) est l'une des extensions les plus populaires qui vous permet de créer des sites web bilingues ou multilingues. Il y a aussi un sélecteur de langue personnalisable, mais le changement de langue ne fonctionne pas si le cache du navigateur est activé.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/browser_c.png)
_W3 Total Cache - activez Browser Cache._

Un autre paramètre important dans W3 Total Cache est d'activer **Lazy Load Images** dans l'Expérience Utilisateur. Cela signifie que votre page ne montrera que les images au-dessus de la ligne de flottaison et le reste se chargera lorsque l'utilisateur fera défiler la page. 

Cela améliorera le temps de chargement de votre site, diminuera le nombre de requêtes HTTP lors du premier chargement de la page et économisera des données (surtout pour les mobiles).

![Image](https://www.freecodecamp.org/news/content/images/2021/11/5..PNG)
_W3 Total Cache - activez Lazy Load Images._

N'oubliez pas de sauvegarder chaque paramètre. Ce ne sont que quelques paramètres généraux pour W3 Total Cache qui vous aideront vraiment avec la vitesse de votre page et le temps de chargement.

## 2. Extension WordPress Speed Booster Pack

[Le Speed Booster Pack](https://cs.wordpress.org/plugins/speed-booster-pack/) a certains paramètres similaires à W3 Total Cache, mais il offre également des fonctionnalités supplémentaires.

Dans Assets, vous avez une option pour ajouter un **Preload asset**. Cela signifie qu'une certaine ressource sera récupérée plus tôt que le navigateur ne la découvrirait autrement, car elle est importante pour la page actuelle. Au cas où il y aurait des actifs que vous devez précharger, vous pouvez simplement ajouter une URL à cet actif.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/7..PNG)
_Speed Booster Pack - ajoutez des actifs de préchargement_

Dans l'élément de menu Special, vous pouvez activer **Localize Google Analytics & Google Tag Manager** (GTM). Cela signifie que les scripts pour Google Analytics et GTM seront remplacés par des scripts enregistrés localement.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/GTM.png)
_Speed Booster Pack - activez Google Analytics et Google Tag Manager._

## 3. Extension WordPress Asset CleanUp: Page Speed Booster

L'extension [Asset CleanUp](https://cs.wordpress.org/plugins/wp-asset-clean-up/) est utile pour couper ou désactiver certains fichiers CSS et JavaScript. La plupart des thèmes WordPress ont beaucoup de fichiers CSS et JavaScript, comme divers éléments, animations ou autres effets que vous n'utiliserez probablement pas ou n'aurez pas besoin. Mais même si vous ne les utilisez pas, ils sont toujours chargés pour l'utilisateur.

Si vous éditez une page, vous pouvez trouver la section Asset CleanUP en bas de cette page. Vous pouvez voir tous les fichiers CSS et JS chargés pour la page. Ensuite, vous pouvez choisir de désactiver ce fichier spécifique et vous pouvez désactiver son chargement pour l'ensemble du site web.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/page_cleanup.png)
_Asset CleanUp - désactivez les fichiers CSS et JS pour qu'ils ne se chargent pas._

## 4. Extension WordPress Async JavaScript

Si les fichiers JavaScript ne sont pas chargés de manière asynchrone, les temps de chargement ralentissent car le code JavaScript est exécuté pendant la construction du DOM. 

L'extension [Async JavaScript](https://cs.wordpress.org/plugins/async-javascript/) vous permet de définir quels fichiers JavaScript doivent être chargés de manière asynchrone ou différée. 

Async signifie que le fichier est téléchargé de manière asynchrone en arrière-plan et s'exécute lorsqu'il est prêt. Le DOM et les autres scripts n'attendent pas pour eux. Defer signifie que le fichier est également téléchargé de manière asynchrone mais n'est exécuté que lorsque le DOM est entièrement construit.

### Comment configurer l'extension Async JavaScript

Tout d'abord, cliquez sur Paramètres et activez **Async JavaScript**.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/11..PNG)
_Async JavaScript - activez Async JS._

La deuxième étape consiste à choisir la **Méthode Async JS**. Ici, choisissez d'abord Async. Après avoir activé async, vous devez tester l'ensemble de votre site web pour voir s'il fonctionne correctement. Vous devriez également vérifier les erreurs dans la console web Chrome. 

Si tout fonctionne bien, vous pouvez essayer d'activer defer. Ensuite, vous devriez tester à nouveau l'ensemble de votre site web et, s'il y a des problèmes, vous devriez revenir à ce paramètre async.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/12..PNG)
_Async JavaScript - Sélectionnez la Méthode Async JS._

Dans la section **Scripts à Différer**, vous pouvez choisir des scripts spécifiques que vous souhaitez différer. Vous ne devriez différer que les fichiers JavaScript qui n'ont aucune dépendance les uns avec les autres ou avec un autre code JavaScript. Vous devriez connaître le but de ces fichiers JavaScript et où ils sont utilisés pour décider si vous pouvez les différer.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/14..PNG)
_Async JavaScript - Scripts à Différer._

## 5. Extension WordPress Allow Webp/AVIF image

Si vous cherchez des images à chargement plus rapide, les formats **WebP** et **AVIF** sont faits pour vous. 

WebP et AVIF sont des formats modernes qui offrent une compression supérieure sans perte et avec perte pour les images sur le web. Ces formats sont utilisés car ils fournissent des images plus petites et plus riches qui rendent les sites web plus rapides. 

Par exemple, la compression sans perte de WebP est 26 % plus petite que celle des PNG. AVIF a la compression la plus optimale - encore meilleure que WebP. Il fournit des images de haute qualité et est jusqu'à 10 fois plus petit que les autres formats connus.

Mais gardez à l'esprit que WebP n'est [pas supporté](https://caniuse.com/webp) dans tous les navigateurs web et que le format AVIF n'est [supporté](https://caniuse.com/avif) que dans Chrome, Firefox et Opera. Ce n'est pas un problème, car de nos jours, il existe des moyens de définir une image dans différents formats et les navigateurs ne chargent que le format supporté.

```
<picture>
   <source srcset="/images/image.avif" type="image/avif">
   <source srcset="/images/image.webp" type="image/webp">
   <img src="/images/image.jpg" width="740" height="251" alt="titre de l'image" loading="lazy">
</picture>
```

Dans le code ci-dessus, le navigateur parcourt un ensemble d'images et s'arrête au premier format supporté. Chrome s'arrête à la première image car il supporte AVIF. Edge s'arrête à la deuxième image car il ne supporte pas AVIF mais supporte WebP.

Avant juillet 2021, WordPress ne supportait pas les images Webp. Mais maintenant, il est possible de les ajouter dans vos médias même sans extension supplémentaire ([mise à jour 5.8](https://wordpress.org/support/wordpress-version/version-5-8)).

Il a fallu assez longtemps à WordPress pour activer ce type de format et nous avons déjà le format AVIF qui n'est pas encore supporté. Heureusement, il existe une extension [Mime Types Plus](https://wordpress.org/plugins/mime-types-plus/) qui vous permet d'ajouter des types MIME supportés dans vos fichiers médias.

## Conclusion

Dans cet article, vous avez appris quelles extensions vous pouvez utiliser pour améliorer les performances de votre site web. 

Rappelez-vous simplement qu'il est important de tester votre site web après chaque configuration, car il pourrait y avoir des problèmes de compatibilité avec d'autres extensions. La plateforme WordPress offre des extensions qui peuvent complètement prendre en charge les performances du site web sans codage supplémentaire. 

Mais si votre site web fonctionne sur une plateforme différente de WordPress, alors vous devrez utiliser d'autres [outils pour développeurs web](https://andrejgajdos.com/the-toolkit-of-a-freelance-full-stack-web-developer/?utm_source=Dzone&utm_medium=Article&utm_campaign=web_performance_plugin) et vous devrez probablement faire un peu de codage. 

Connaissez-vous d'autres extensions WordPress qui sont utiles pour les performances du site web ? Faites-le moi savoir, car j'aimerais en savoir plus.