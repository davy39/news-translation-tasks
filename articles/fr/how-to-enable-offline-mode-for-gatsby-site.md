---
title: Comment activer le mode hors ligne pour votre site Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-09T15:15:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-offline-mode-for-gatsby-site
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/gatsby-offline-article.jpg
tags:
- name: Gatsby
  slug: gatsby
- name: JAMstack
  slug: jamstack
seo_title: Comment activer le mode hors ligne pour votre site Gatsby
seo_desc: 'By Ondrej Polesny

  One of the reasons we create JAMstack sites is because of their great performance.
  Serving static files is easy and quick. But what if we upgrade the visitor''s experience
  and make the site available offline?

  Looking at both recent r...'
---

Par Ondrej Polesny

L'une des raisons pour lesquelles nous créons des sites JAMstack est leur grande performance. Servir des fichiers statiques est facile et rapide. Mais que se passerait-il si nous améliorions l'expérience du visiteur et rendions le site disponible hors ligne ?

En examinant les deux rapports récents sur l'état du JAMstack en 2020 (vous pouvez consulter [le rapport de Kontent](https://tracker.kontent.ai/942894/the-state-of-jamstack-report-2020) et [le rapport de Netlify](https://www.netlify.com/blog/2020/05/27/state-of-the-jamstack-survey-2020-first-results/)), il est clair que la performance est la principale raison pour laquelle nous construisons des sites statiques.

J'appelle ce fait un peu une tricherie. L'avantage de performance vient avec le JAMstack par conception, donc c'est comme appeler les chiots mignons. Ils sont toujours mignons parce qu'ils sont des chiots.

Si nous sommes vraiment sérieux concernant la performance, même les sites JAMstack peuvent faire mieux. Mais avant de plonger dans le mode hors ligne pour Gatsby, nous devons comprendre comment Gatsby sert les pages :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-site.png)

Le visiteur ne demande pas chaque fichier HTML individuel au serveur. Plutôt, le client JS de Gatsby demande au serveur le _page-data.json_ de la page respective. C'est ainsi que le visiteur passe à la page demandée sans ce rechargement classique de la page. Mais même pour cela, nous avons besoin du réseau.

## Pourquoi les sites web ont-ils besoin d'un mode hors ligne ?

De nos jours, tout le monde est en ligne, n'est-ce pas ? Une connexion internet sur les téléphones mobiles ne semble plus être une option, mais une nécessité. Nous utilisons des applications comme Whatsapp, Messenger, et d'autres tout le temps.

Mais que se passe-t-il si nous entrons dans un ascenseur ? Que se passe-t-il si nous marchons vers une voiture garée dans un parking souterrain ou si nous conduisons à travers un tunnel ? Que se passe-t-il si nous sommes dans un avion qui est sur le point de décoller ?

Pas de réception. C'est ce que tous ces endroits ont en commun. Et la seule chose que les gens peuvent faire avec leurs téléphones sans réception est de regarder des films Netflix téléchargés. Jusqu'à ce que vous activiez le mode hors ligne pour votre site web.

## Comment cela fonctionne-t-il ?

En bref, nous évitons au visiteur l'aller-retour vers le serveur et téléchargeons toutes les données nécessaires à l'avance. Et nous installons un ServiceWorker qui agit comme un serveur au lieu d'un serveur distant réel.

Un ServiceWorker est un script que le navigateur du visiteur exécute en arrière-plan et permet des fonctionnalités comme les notifications push et autres. Voir [Google docs](https://developers.google.com/web/fundamentals/primers/service-workers) pour plus d'informations.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-service-worker.png)

Avec Gatsby, comme nous en avons tous l'habitude, c'est aussi simple que d'installer un plugin :

```
npm i gatsby-offline-plugin --save
```

Et de l'ajouter au `gatsby-config.js` :

``` javascript
plugins: [
    ...
    `gatsby-plugin-offline`,
    ...
]
```

Mais chaque site web utilise de nombreux types d'actifs différents, donc typiquement, nous devons faire une étape supplémentaire et configurer le service worker.

## Stratégies de service des actifs

Chaque site web contient de nombreux actifs allant des fichiers CSS aux images, icônes, polices web et données de page réelles.

Le service worker ne peut pas vraiment télécharger tous ces actifs lors du premier chargement de la page, car cela irait directement à l'encontre de l'avantage de performance. Les visiteurs ne seraient pas non plus heureux si leurs navigateurs commençaient à télécharger 100 Mo d'images au moment où ils décident de visiter votre galerie photo.

Nous pouvons utiliser des expressions régulières pour cibler des fichiers spécifiques et configurer le service worker pour les traiter de manière appropriée. Examinons les stratégies disponibles :

### CacheFirst

Utilisation typique : polices web, feuilles de style

Le service worker vérifie le cache pour le fichier demandé. Si le fichier est manquant, il se connecte en ligne pour le récupérer tout en le stockant dans le cache pour une utilisation future.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/cache-first.png)
_Crédit image : [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### CacheOnly

Utilisation possible : votre propre logique de pré-cache

Le service worker vérifie le cache pour le fichier demandé. Si le fichier est manquant, il retourne une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/cache-only.png)
_Crédit image : [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### NetworkFirst

Utilisation typique : requêtes API non critiques

Le service worker se connecte en ligne pour récupérer le fichier demandé. Si le réseau est hors ligne ou si le serveur ne répond pas, il revient au cache.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/network-first.png)
_Crédit image : [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### NetworkOnly

Utilisation typique : requêtes API critiques

Le service worker se connecte en ligne pour récupérer le fichier demandé. Si le réseau est hors ligne ou si le serveur ne répond pas, il retourne une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/network-only.png)
_Crédit image : [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### StaleWhileRevalidate

Utilisation typique : actifs front-end, images

Le service worker vérifie le cache pour le fichier demandé et le fournit. Ensuite, il fait une requête réseau pour mettre à jour silencieusement le cache.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/stale-while-revalidate.png)
_Crédit image : [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

## Configuration du site Gatsby

Une configuration simple d'un site Gatsby qui devrait fonctionner hors ligne ressemble à ceci :

``` javascript
{
    resolve: `gatsby-plugin-offline`,
    options: {
        precachePages: [`/blog/*`],
    },
}
```

De cette manière, je configure le service worker pour pré-cacher tous les articles de blog, qui sont toutes les pages dont l'URL commence par `/blog/`.

Une fois que le visiteur accède à la page d'index avec des liens vers les articles de blog, il pourra cliquer sur n'importe lequel d'entre eux sans connexion internet active. C'est-à-dire, si vous utilisez l'élément `Link` dans l'implémentation. Les balises d'ancrage standard font contourner le service worker par le navigateur et récupèrent les données à distance.

Le service worker traitera tous les actifs selon sa configuration par défaut :

* **CacheFirst**
Fichiers JS, fichiers CSS, tout ce qui se trouve dans le dossier "static/"
* **NetworkFirst**
Fichiers */page-data/*/page-data.json
* **StaleWhileRevalidate**
Images, fichiers de polices web, etc.

Donc, si vous craignez que le service worker récupère tous les actifs de tous les articles de blog, il ne le fera que après que le visiteur ait réellement ouvert la page de l'article de blog.

La raison est que l'espace de cache et la bande passante de la connexion internet du visiteur sont limités. Lors du premier chargement de la page, le visiteur télécharge tous les actifs du site comme les feuilles de style, les polices web, les icônes, et autres, donc ces actifs seront disponibles dans le cache lors des chargements suivants. Les images et autres ressources des pages pré-cachées seront résolues une fois que la page est demandée et cela ne peut être changé que via une logique personnalisée.

Dans quels cas voudriez-vous changer la configuration ? Il n'y avait en fait pas beaucoup de cas auxquels je pouvais penser, mais j'en ai rencontré quelques-uns :

* **Actifs fournis à partir d'URL sans suffixe de nom de fichier correspondant**
Google sert les définitions CSS des polices web sans le suffixe .css et cela est déjà couvert par la configuration par défaut. Cependant, vous pouvez servir des images ou d'autres actifs à partir d'URL qui n'ont pas le suffixe approprié.
* **Avoir plus de contrôle sur le cache**
Avec certains actifs, vous voulez être responsable de la durée pendant laquelle un certain élément peut résider dans le cache jusqu'à ce qu'il expire.
* **Actifs exotiques**
D'accord, exotique peut être un peu fort :-), mais les polices web au format EOT, les images au format HEIC, les courtes vidéos, les chansons, etc.

Dans ces cas, vous devez ajuster la configuration par défaut et la définir dans les options du plugin :

``` javascript
{
  resolve: `gatsby-plugin-offline`,
  options: {
    precachePages: [`/blog/*`],
    runtimeCaching: [
      // définitions précédentes de la configuration par défaut
      (...),
      {
        urlPattern: /^https:\/\/fonts\.gstatic\.com/,
        handler: 'cacheFirst',
        options: {
          cacheableResponse: {
            statuses: [0, 200]
          },
          cacheName: 'google-fonts-webfonts',
          expiration: {
            maxAgeSeconds: 60 * 60,
            maxEntries: 30
          }
        }
      },
    ]
  },
},
```

Cet élément de configuration supplémentaire garantira qu'au maximum 30 polices Google servies depuis gstatic.com seront mises en cache pour une durée maximale d'une heure et seront traitées en utilisant la stratégie CacheFirst.

### Construire le site avant de tester

Une fois que vous avez terminé la configuration, assurez-vous de construire et de servir le site avant de tester les capacités hors ligne. Elles ne fonctionnent pas en mode développement.

```
gatsby build && gatsby serve
```

## JAMstack = performance, mais...

Dans cet article, je vous ai montré comment installer et configurer le plugin hors ligne pour Gatsby.

Tous les sites JAMstack bénéficient d'une performance incroyable par conception. En ajoutant des capacités hors ligne, vous portez l'expérience de navigation de vos visiteurs à un niveau supérieur par rapport aux autres sites JAMstack. La configuration du service worker vous permet d'affiner davantage la manière dont chaque actif sera traité et mis en cache.

Si vous êtes intéressé, vous pouvez trouver plus d'informations sur le plugin dans la [documentation de Gatsby](https://www.gatsbyjs.org/packages/gatsby-plugin-offline/).