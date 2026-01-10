---
title: Construire un site web ultra-rapide et sécurisé avec un CMS n'est pas sorcier.
  Ou peut-être que si ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T17:47:25.000Z'
originalURL: https://freecodecamp.org/news/building-a-super-fast-and-secure-website-with-a-cms-is-no-big-deal-or-is-it-5ac915c691f2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rM8pXwM7Je0zXjAv_dfysQ@2x.png
tags:
- name: api
  slug: api
- name: Security
  slug: security
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Construire un site web ultra-rapide et sécurisé avec un CMS n'est pas sorcier.
  Ou peut-être que si ?
seo_desc: 'By Ondřej Polesný

  Can I break your site? Do you have any leftover scripts there that I can take advantage
  of? Is there a way to steal your credentials and change content on your site? Can
  I access private information? No? Are you sure? Or, am I never...'
---

Par Ondřej Polesný

Puis-je pirater votre site ? Avez-vous des scripts obsolètes que je pourrais exploiter ? Existe-t-il un moyen de voler vos identifiants et de modifier le contenu de votre site ? Puis-je accéder à des informations privées ? Non ? Êtes-vous sûr ? Ou bien, ne vais-je jamais le découvrir parce que votre page met une éternité à charger ?

À un moment donné, lors de la création d'un site web, vous devez penser à la performance et à la sécurité. Peu importe que vous travailliez sur votre site personnel ou sur celui de votre client. C'est la même chose que de sauvegarder vos fichiers locaux. Il y a des gens qui font des sauvegardes régulières, et des gens qui n'en ont pas encore perdu, donc sont moins enclins à le faire.

### CMS Traditionnel

Si vous utilisez un système de gestion de contenu (CMS) traditionnel, la situation est plus compliquée pour vous. Ces systèmes contiennent de nombreuses fonctionnalités. Ils doivent couvrir tous les cas d'utilisation potentiels qu'un site web pourrait avoir. Cela signifie du code. Beaucoup de code. Des milliers de fichiers. Et ce n'est pas tout — les interfaces d'administration doivent fournir une belle interface utilisateur pour que vous puissiez configurer toutes ces fonctionnalités. Potentiellement, quelques milliers de fichiers supplémentaires.

#### Sécurité

Ce n'est pas votre code, n'est-ce pas ? Donc, il devrait déjà être sécurisé. Eh bien, de nombreux fournisseurs de CMS font de leur mieux pour s'assurer que leurs implémentations sont sécurisées. Ils doivent encore couvrir beaucoup de fichiers. Et chaque fichier peut contenir une erreur, du code qui a été laissé derrière, ou peut-être un paramètre de chaîne de requête qui expose une base de données. Cela peut en soi créer une vulnérabilité potentielle.

L'utilisation d'un CMS open-source peut être encore plus dangereuse, car l'implémentation est publique. Oui, vous pouvez argumenter que l'open-source est avantageux. N'importe qui peut contribuer et corriger les problèmes trouvés. Mais cela ne couvre que les problèmes déjà connus. Les attaquants garderaient probablement leurs exploits pour eux. Même si un problème a été trouvé et corrigé, vous devez encore faire beaucoup d'efforts pour vous assurer que votre site web est maintenu à jour. Vous devez effectuer des mises à jour chaque fois qu'un correctif de sécurité est publié.

Si vous êtes intéressé par des statistiques réelles, consultez le [rapport sur les sites piratés par Sucuri](http://bit.ly/2CVdyYP).

Alors, que voudraient faire les attaquants avec votre site web ? Essentiellement, ils veulent obtenir vos données pour pouvoir abuser de votre site web en :

* Obtenant un accès à votre base de données via l'un des scripts. C'est généralement le cas des scripts personnalisés obsolètes, des pages de test, et autres.
* Compromettant et abusant de vos données secrètes. Les fichiers de configuration sont une option de stockage typique pour diverses clés secrètes et identifiants pour d'autres services ou bases de données.
* Modifiant le contenu de votre site web.
* Rendant votre site web inaccessible, c'est-à-dire le fermer.

#### Performance

Lorsque vous implémentez votre site web sur un CMS traditionnel, vous devez généralement le personnaliser, donc il y a des fichiers du CMS et vos fichiers personnalisés. Tous doivent être compilés, puis, avec les bibliothèques précompilées, chargés en mémoire du serveur avant que le serveur ne commence à traiter les requêtes vers votre site web. Ou pire, si vous utilisez une solution basée sur un langage interprété comme PHP, interpréter tout le code pour chaque requête.

En tout cas, votre site web semble fonctionner correctement, alors pourquoi cela devrait-il être une préoccupation ? Eh bien, parce que :

* vous payez pour la puissance de calcul de votre serveur
* vous compilez et copiez le code des fonctionnalités que vous n'avez jamais l'intention d'utiliser
* les visiteurs de votre site web attendent la réponse

Le temps jusqu'au premier octet de ces sites web peut être bien au-dessus de 1 seconde. Bien sûr, cela peut être optimisé, mais vous passez alors du temps et de l'argent à comprendre comment atténuer les problèmes de performance, et vous finissez généralement par augmenter le CPU et la mémoire, ou pire, en ajoutant un serveur supplémentaire.

Vérifiez votre site en utilisant [Google PageSpeed](http://bit.ly/2ESQuww) ou obtenez une analyse plus détaillée en utilisant [SpeedCurve](http://bit.ly/2EQyse6) pour voir comment votre site web se comporte.

### Sites Web Basés sur API

Les sites web construits sur une API permettent une grande flexibilité. Demandez-vous, avez-vous besoin de gestion de contenu ? Si oui, vous pouvez utiliser un CMS headless. Avez-vous besoin de [stocker les soumissions de formulaires](http://bit.ly/2P0gidP) ? Parfait, utilisez un service de formulaires. Construisez-vous un site web pour un hôtel de montagne et souhaitez-vous afficher une prévision météorologique ? Il existe un service météorologique avec son API pour vous.

Le nombre de fichiers utilisés pour de tels sites web correspond à leur fonctionnalité. Mais qu'en est-il de l'interface d'administration pour l'édition de contenu ? Ne vous inquiétez pas. Le CMS headless gère cette partie pour vous, sans code supplémentaire que vous devez héberger ou maintenir.

#### Sécurité

Lorsque vous utilisez des services API, vous n'avez pas besoin d'un service d'administration au-dessus de votre site web. Vous configurez tous les composants lors de la construction du site web. Comme le composant météo qui doit afficher une prévision météo pour trois jours. Ou qu'il doit y avoir quatre articles de blog sur la page principale. Le reste du contenu dynamique peut être géré dans le CMS headless.

Le principal avantage de cette approche est que vous n'avez pas besoin d'une base de données. C'est exact, aucun point unique de stockage de données auquel un attaquant pourrait accéder.

Si votre site web est basé sur JavaScript, son implémentation est essentiellement ouverte. Il peut être compilé, mais tout ce qui est fourni au navigateur est lisible. C'est un autre avantage. Oui, n'importe qui peut interroger directement les points de terminaison des services. Le contenu publié que vous obtenez d'eux est affiché sur votre site web de toute façon, seulement transformé en un visuel plus agréable. C'est comme avec les articles de nouvelles sur les sites web et les lecteurs RSS. Pour le contenu sensible, vous pouvez toujours authentifier chaque utilisateur via un autre service, obtenir leur jeton d'accès unique et l'utiliser pour demander du contenu sensible via un protocole sécurisé.

Si vous gardez à l'esprit que l'implémentation JS est ouverte à tous et traitez les données sensibles de la bonne manière, vous aurez beaucoup moins de travail à faire pour sécuriser votre site web. Ne pas avoir de base de données et consommer tous les services API via des canaux sécurisés ferme presque toutes les portes à un attaquant potentiel.

#### Performance

Dans ce scénario, le serveur web fournit uniquement des actifs. La logique métier de votre application est stockée dans un fichier JS. Le contenu de divers points de terminaison est recueilli via des requêtes asynchrones par les navigateurs des visiteurs.

Des requêtes asynchrones pour obtenir du contenu à partir de services tiers ? Cela doit être lent, n'est-ce pas ? Eh bien, oui, elles prennent un certain temps. Mais leurs points de terminaison de livraison sont généralement construits pour la vitesse, hébergés dans le Cloud et très flexibles. Vous pouvez également choisir un CMS headless qui utilise un CDN pour la livraison, l'un d'eux est [Kentico Cloud](http://bit.ly/2QzUALM). De cette manière, la requête sera toujours traitée par le centre de données géographiquement le plus proche de chacun de vos visiteurs.

Même si vous utilisez plusieurs services pour construire une seule page, ces requêtes sont toutes asynchrones. Les visiteurs n'attendent que la plus lente. Lorsqu'une page est composée sur un serveur utilisant un CMS traditionnel, toute la communication avec la base de données et d'autres services est généralement synchrone. Par conséquent, le serveur attend que chaque transaction se termine avant d'en commencer une autre. Et après tout cela, tout est assemblé et renvoyé en une seule grande réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/ipQDewGGY6nlDDtBAL9J6ria7NOBKVnj2AdB)
_CMS Traditionnel — 3s ; Site web basé sur API — 1,3s_

Regardez combien de temps le serveur web a mis pour traiter les requêtes entrantes (fond jaune clair). Tout ce temps, le visiteur attend activement et ne peut pas commencer à télécharger les images et autres actifs. Ils ne seront connus du navigateur du visiteur qu'après la réception de la réponse.

Un site web basé sur API est beaucoup plus rapide, car la réponse initiale avec le fichier HTML statique est instantanée. Le navigateur télécharge la logique métier du site web en tant que l'un des actifs et génère toutes les requêtes asynchrones ultérieures pour le contenu. Le visiteur voit une page entièrement rendue beaucoup plus rapidement et voit également que quelque chose se passe. Lorsqu'ils attendent une page rendue par le serveur, tout ce qu'ils voient est un préchargeur dans la barre d'adresse de leur navigateur. L'amélioration globale des performances du site web basé sur API est dans ce cas de plus de 50 %. Elle peut être beaucoup plus élevée en fonction de l'implémentation du site web.

### Sites Web Statiques

Alors, pourquoi nous embêter à résoudre les problèmes de performance si nous avons déjà un site web basé sur API ?

![Image](https://cdn-media-1.freecodecamp.org/images/1BeV156ReM5M6NFKxQ1evAwNWgOESVOl4ZOz)

Puisque le serveur web ne fournit que des fichiers et des actifs statiques, ses performances sont bonnes. Le fait que le contenu dynamique soit recueilli plus tard, lorsque le site web est rendu dans les navigateurs des visiteurs, peut entraîner certains artefacts. Les visiteurs peuvent voir un composant vide qui se remplit lorsqu'il reçoit des données de la requête asynchrone, et ainsi de suite. Les personnes ayant une connexion Internet lente ou utilisant des ordinateurs plus anciens peuvent trouver cela perturbant.

Que pouvons-nous faire à ce sujet ? Non, nous n'ajouterons aucun préchargeur. Comment cela vous fait-il sentir lorsque vous voyez un préchargeur infini qui tourne et tourne sans fin ? Nous pouvons rendre nos sites web statiques, tout en les gardant dynamiques.

![Image](https://cdn-media-1.freecodecamp.org/images/ZrlAed2i11o1dQbZsUwydQPoqxK7UttIlHSo)

Le concept des sites statiques concerne la sortie de votre site web. Cela commence par le contenu. Les éditeurs ne mettent généralement pas à jour le contenu très souvent. Le site web doit être composé à chaque requête (comme le font les CMS traditionnels). L'idée est similaire à la mise en cache — stocker les données ou pages générées en mémoire. Mais les sites statiques vont un peu plus loin. L'ensemble du site web, toutes les pages avec tout le contenu, est généré à chaque fois qu'un éditeur publie du contenu. Donc, si vous avez 153 articles de blog dans votre blog, le site web aura maintenant 153 pages statiques (plus quelques autres comme la page d'accueil, contact, et plus).

Comment allez-vous gérer 153 pages ? Eh bien, vous ne le ferez pas. Vous gérez toujours uniquement l'implémentation d'une seule page dynamique. Le site statique est généré en combinant votre implémentation avec le contenu d'un CMS headless. Donc, lorsqu'il y a du nouveau contenu, le site est simplement généré automatiquement à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/cFrbwPbcZ6ofl23HkQ5-NKClZPU-wUqobOfs)

Vous voyez que le bénéfice de vitesse n'est pas si significatif par rapport aux sites web dynamiques basés sur API. Cependant :

* vos visiteurs obtiennent la page et tout le contenu dans la première réponse. Ils ne regarderont pas une page en cours de construction. Leurs navigateurs n'ont pas besoin de créer des requêtes async supplémentaires pour le contenu
* toutes les requêtes ultérieures se comportent de la même manière
* les visiteurs naviguent entre un ensemble de pages statiques, ce qui est très rapide
* certains outils de génération de sites statiques permettent des fonctionnalités supplémentaires pour les visiteurs, telles que le préchargement des pages liées (ce qui rend la navigation vers elles instantanée) ou l'affichage des images en basse qualité avant qu'elles ne soient entièrement téléchargées

Tout cela laissera à vos visiteurs l'impression d'un site web ultra-rapide.

Bien sûr, chaque site web est différent. Vous pourriez avoir besoin de certaines fonctionnalités de personnalisation ou vouloir afficher du contenu sensible. Dans ces cas, vous pouvez combiner les deux approches. Avoir un site web statique et utiliser des services basés sur API pour fournir du contenu qui varie parmi les visiteurs.

### Conclusion

Les aspects de performance et de sécurité de chaque site sont très importants. Les CMS traditionnels sont généralement plus exigeants en ressources que les sites web basés sur API, mais ils fournissent plus de fonctionnalités dès la sortie de la boîte.

D'autre part, les sites web basés sur API sont beaucoup plus rapides et plus sécurisés. Ils vous permettent d'économiser de l'argent sur l'hébergement et offrent une meilleure expérience à vos visiteurs.

Les sites statiques deviennent un grand succès de nos jours, car leurs performances sont de loin les meilleures. Ils vous permettent également de construire des sites partiellement statiques et partiellement dynamiques basés sur JavaScript qui sont bien indexables par les moteurs de recherche.

Votre site web est-il déjà statique ? Avez-vous utilisé des générateurs de sites statiques ? Faites-moi savoir votre expérience dans la section des commentaires ci-dessous.

Dans mon prochain article, je vous montrerai comment construire un site web sur Vue.js en utilisant un générateur de site statique.

#### Autres articles de la série :

1. [Comment commencer à créer un site web impressionnant pour la première fois](http://bit.ly/2Duglu1)
2. [Comment choisir la meilleure technologie pour votre site web ?](http://bit.ly/2N0kXY4)
3. [Comment booster votre site web avec Vue.js et un effort minimal](http://bit.ly/2zLRE8a)
4. [Comment mélanger un CMS headless avec un site web Vue.js et payer zéro](http://bit.ly/2CyDnhX)
5. [Comment sécuriser les soumissions de formulaires sur un site web API](http://bit.ly/2P0gidP)
6. **Construire un site web ultra-rapide et sécurisé avec un CMS n'est pas sorcier. Ou peut-être que si ?**
7. [Comment générer un site web statique avec Vue.js en un rien de temps](http://bit.ly/2PN46Jy)
8. [Comment configurer rapidement un processus de construction pour un site statique](http://bit.ly/2Dv2UGS)