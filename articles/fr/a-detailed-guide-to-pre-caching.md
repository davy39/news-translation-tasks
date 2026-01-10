---
title: Qu'est-ce que le pré-cache ? Comment augmenter la vitesse et les performances
  d'un site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-19T18:05:56.000Z'
originalURL: https://freecodecamp.org/news/a-detailed-guide-to-pre-caching
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pre-caching.png
tags:
- name: caching
  slug: caching
- name: node js
  slug: node-js
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: web performance
  slug: web-performance
seo_title: Qu'est-ce que le pré-cache ? Comment augmenter la vitesse et les performances
  d'un site web
seo_desc: 'By Saurabh Dashora

  Speed and performance are two of the key ingredients that make a website stand out
  from its peers.

  Imagine visiting a bestseller list on the Amazon website and finding that the product
  pages take forever to show up.

  What about a bl...'
---

Par Saurabh Dashora

La **vitesse** et les **performances** sont deux des ingrédients clés qui font qu'un site web se distingue de ses pairs.

Imaginez visiter une liste des best-sellers sur le site Amazon et constater que les pages produits mettent une éternité à s'afficher.

Et si un blog publie de grandes histoires que les lecteurs ne peuvent pas lire parce que le trafic entrant dépasse la capacité du serveur ?

Et si ce n'est pas suffisant, mesurez votre frustration lorsqu'il y a un nouveau film très attendu sur Netflix et que tout ce que vous voyez est l'écran de chargement.

Si vous êtes celui qui gère un tel site web, c'est un **bon problème** à avoir. Clairement, les gens sont enthousiastes à propos des choses que vous offrez et il y a une quantité disproportionnée de trafic pour certaines pages.

Cependant, si ce n'est pas géré correctement, la situation peut rapidement dégénérer en chaos et finir par aliéner vos utilisateurs. Finalement, cela entraînera une perte d'activité, que ce soit en termes de temps de visionnage, de ventes, ou même de bonne volonté générale des utilisateurs.

**Alors, comment éviter cette situation ?**

L'une des techniques les plus prometteuses pour améliorer la vitesse et les performances d'un site web est le **pré-cache**.

Dans cet article, vous allez comprendre en détail le concept de pré-cache.

## Qu'est-ce que le pré-cache ?

Le pré-cache est une technique utilisée pour **proactivement** stocker ou mettre en cache des données en anticipation de futures requêtes. L'idée est de mettre en cache les données ou ressources fréquemment consultées à l'avance afin que, lorsque le moment sera venu, vous puissiez les livrer plus rapidement à l'utilisateur final.

Consultez l'illustration ci-dessous qui montre comment le pré-cache peut fonctionner dans un contexte système global.

![pré-cache dans un système](https://www.freecodecamp.org/news/content/images/2023/01/image-133.png)
_Comment fonctionne le pré-cache_

Vous pouvez effectuer le pré-cache côté **client**, comme dans le navigateur web. Alternativement, vous pouvez également le faire côté **serveur** en utilisant des réseaux de diffusion de contenu (CDN) ou d'autres solutions de cache.

Quelle que soit l'approche, le but du pré-cache est d'**améliorer les performances et l'expérience utilisateur en réduisant les temps de chargement du contenu**.

## Comment fonctionne le pré-cache

Le processus de pré-cache nécessite de stocker une copie des données dans un emplacement plus proche de l'utilisateur ou de stocker les données à l'avance afin qu'elles soient immédiatement disponibles lorsque nécessaire.

Voici les étapes de haut niveau pour implémenter le pré-cache.

* Tout d'abord, **identifier les données ou ressources** qui sont consultées le plus fréquemment. Ces ressources sont de bons candidats pour le pré-cache. Par exemple, les articles de blog les plus populaires, la liste des produits best-sellers, etc. Vous pouvez également inclure des images, des fichiers JS et des feuilles de style dans la liste de pré-cache.
* Après l'identification, vous devez **choisir le système de cache** pour stocker les données pré-cache. Cela peut être un cache local sur l'appareil de l'utilisateur ou même un cache distribué couvrant plusieurs serveurs. Le choix dépendra du type de ressource.
* Ensuite, vous devez **pré-remplir le cache** avec les ressources identifiées. Cette étape peut être effectuée automatiquement par le système lors de la phase d'initialisation. Alternativement, vous pouvez le faire à la demande lorsque les données sont consultées par les utilisateurs. N'oubliez pas, le pré-cache consiste à être proactif.
* Une fois la configuration prête, vous pouvez laisser votre système faire le travail. Chaque fois que le système doit accéder aux données pré-cache, il peut les récupérer directement depuis le cache au lieu de les récupérer depuis la source externe plus lente.

## Comment décider quoi pré-cache

Le succès du pré-cache dépend de la **qualité des données** qui sont pré-cache. Il est important pour vous de choisir les bonnes données à cache.

Bien que cela puisse sembler intimidant en pratique, vous pouvez suivre les règles ci-dessous pour faire le bon choix :

* **Priorisez les ressources critiques** telles que les fichiers HTML, CSS et JavaScript nécessaires au chargement initial de la page. Habituellement, ce sont les ressources les plus importantes nécessaires pour fournir une expérience utilisateur rapide et fluide.
* Vous devriez également envisager de **mettre en cache les ressources tierces** comme les polices, les bibliothèques ou les scripts provenant d'autres domaines. Ces ressources peuvent être pré-cache localement pour réduire les requêtes réseau fréquentes.
* Votre hypothèse initiale sur les meilleures ressources pour le pré-cache peut changer. Par conséquent, il est vital de **réaliser une analyse régulière** des schémas d'utilisation de votre application web et d'en tirer des insights sur l'activité des utilisateurs. Cela aidera votre catalogue de pré-cache à rester pertinent à mesure que votre application évolue.
* Explorez l'**utilisation de l'apprentissage automatique** pour le pré-cache. Vous pouvez **construire des modèles de prédiction** afin de prédire quelles ressources seront demandées à l'avenir en fonction des schémas d'utilisation passés. Vous pouvez entraîner ce modèle sur des données historiques et l'utiliser pour identifier les meilleures ressources candidates pour le pré-cache. Bien sûr, cette approche est coûteuse et son utilisation dépend de l'importance du pré-cache dans le contexte de votre application.

## Les avantages du pré-cache

Le pré-cache peut sembler beaucoup de tracas. Pourquoi se soucier de cela ?

À mon avis, les avantages du pré-cache peuvent l'emporter sur les difficultés. Voici quelques bénéfices importants du pré-cache :

* **Amélioration des performances** – Lorsque vous pré-cachez des données, vous réduisez essentiellement le temps de chargement du contenu. Cela conduit à une expérience utilisateur plus rapide. Les sites web et les applications qui s'attendent à un volume élevé de trafic ou qui traitent de grandes quantités de données en bénéficient considérablement.
* **Expérience utilisateur améliorée** – Qui n'aime pas une bonne expérience utilisateur ? Des temps de chargement plus rapides améliorent l'expérience utilisateur globale et aident à réduire le taux de rebond (pourcentage d'utilisateurs quittant un site web après avoir visité une page). Le pré-cache améliore également la disponibilité du contenu même en cas de mauvaise connexion réseau.
* **Réduction des coûts** – Le pré-cache peut vous aider à réduire les coûts. Par exemple, si vous pré-cachez des données sur un CDN, vous réduisez finalement la charge sur le serveur d'origine. Cela économise de la bande passante et réduit le coût du serveur.
* **Accès hors ligne** – Avec le pré-cache, vous pouvez également activer l'accès hors ligne au contenu en utilisant le concept de service workers. Cela est extrêmement important pour les applications mobiles et les sites web qui doivent fonctionner dans des zones avec une mauvaise connectivité internet.
* **Sécurité** – Bien que ce soit un avantage indirect, vous améliorez également la sécurité globale de vos actifs en utilisant le pré-cache. Basiquement, le pré-cache atténue l'impact des attaques DoS (Denial of Service) puisque l'application n'aura pas à servir les ressources pré-cache depuis le serveur d'origine.

## Comment implémenter le pré-cache en Node.js

Examinons une implémentation très basique du **pré-cache en Node.js** :

```js
const express = require('express');
const nodecache = require('node-cache');
require('isomorphic-fetch');

//Configuration d'Express
const app = express();

//Création de l'instance node-cache
const cache = new nodecache({stdTTL: 10})

//Nous utilisons la fausse API disponible à <https://jsonplaceholder.typicode.com/>
const baseURL = '<https://jsonplaceholder.typicode.com/posts/>';

//Pré-cache des articles populaires
[1, 2, 3].map(async (id) => {
    const fakeAPIURL = baseURL + id
    const data = await fetch(fakeAPIURL).then((response) => response.json());
    cache.set(id, data);
    console.log(`Post Id ${id} mis en cache`);
})

//Point de terminaison API pour démontrer le cache
app.get('/posts/:id', async (req, res) => {
    const id = req.params.id;
    if (cache.has(id)) {
        console.log('Récupération des données depuis le Node Cache');
        res.send(cache.get(id));
    }
    else {
        const fakeAPIURL = baseURL + id
        const data = await fetch(fakeAPIURL).then((response) => response.json());

        cache.set(req.params.id, data);
        console.log('Récupération des données depuis l'API');
        res.send(data);
    }
})

//Démarrage du serveur
app.listen(3000, () => {
    console.log('Le serveur écoute sur le port 3000')
})

```

L'exemple utilise la bibliothèque `node-cache` pour créer un cache en mémoire. Il est emprunté à un article de blog qui montre [comment implémenter un cache en mémoire dans Node.js](https://progressivecoder.com/in-memory-caching-nodejs/).

Pour simuler le fonctionnement du pré-cache, il suppose que les articles 1, 2 et 3 sont des articles extrêmement populaires et des candidats appropriés pour le pré-cache. Par conséquent, les données de ces articles sont pré-chargées lors du processus de démarrage de l'application et stockées dans l'objet `cache`.

Lorsque une requête est faite pour ces articles spécifiques, l'application récupère les données directement depuis le cache au lieu d'appeler l'API.

Bien sûr, il s'agit d'une configuration très basique pour le pré-cache. Mais vous devriez comprendre l'idée du concept en action.

## Types de pré-cache

Alors que l'exemple de la section précédente démontrait une approche particulière pour implémenter le pré-cache, il existe d'autres méthodes également.

Puisque l'idée de base du pré-cache est assez simple, vous pouvez l'implémenter de plusieurs manières différentes. Globalement, il existe deux approches principales : le pré-cache côté client et le pré-cache côté serveur.

### Pré-cache côté client

La manière la plus courante de pré-cache côté client est de mettre proactivement en cache les ressources sur le navigateur. Avec le **cache basé sur le navigateur**, vous essayez d'anticiper les ressources qui seront demandées et de les stocker à l'avance en utilisant l'API de stockage de cache du navigateur.

Le **cache basé sur le navigateur** repose souvent sur les en-têtes de cache pour déterminer si une ressource particulière est cachable. Lorsque l'utilisateur demande une page, le navigateur vérifie son cache pour voir si une copie des données demandées est déjà disponible. Si c'est le cas, le navigateur charge les données depuis le cache. Cela réduit le temps nécessaire pour charger la page.

Une autre manière d'implémenter le cache basé sur le navigateur est d'utiliser l'**API Service Worker**. Basiquement, les actifs sont pré-cache à l'avance, généralement lors du processus d'installation d'un service worker.

Avec le pré-cache de service worker, les actifs statiques clés et les matériaux tels que les fichiers HTML, CSS, JS et les images nécessaires pour l'accès hors ligne sont téléchargés et stockés dans une instance `Cache`. Vous pouvez utiliser la bibliothèque JavaScript nommée **[Workbox](https://developer.chrome.com/docs/workbox/)** qui facilite le pré-cache des ressources et fournit une API simple pour travailler avec le cache du service worker.

### Pré-cache côté serveur

La deuxième approche est le **pré-cache côté serveur**. Vous pouvez également le faire de plusieurs manières.

La première méthode consiste à utiliser des **réseaux de diffusion de contenu ou CDN** qui stockent une copie des données sur des serveurs répartis dans le monde entier. Lorsque l'utilisateur fait une requête pour certaines données, elles sont livrées depuis le serveur le plus proche de l'utilisateur. Cela réduit le temps nécessaire pour traiter la requête et rend votre site web plus rapide pour l'utilisateur.

![pré-cache avec les réseaux de diffusion de contenu](https://www.freecodecamp.org/news/content/images/2023/01/image-134.png)
_Pré-cache avec CDN_

La deuxième approche consiste à utiliser un **serveur proxy de cache**. Il s'agit d'un serveur qui se place devant le serveur d'origine et fonctionne comme une couche de cache en stockant une copie des données. La prochaine fois qu'il y a une requête de l'utilisateur, le serveur proxy livre les données directement sans avoir à faire une requête au serveur d'origine.

![serveur proxy de cache](https://www.freecodecamp.org/news/content/images/2023/01/image-135.png)
_Serveur Proxy de Cache_

Voici un exemple de configuration pour utiliser NGINX comme serveur proxy de cache pour mettre en cache tous les fichiers avec l'extension jpeg/jpg, png, css et js pendant 60 secondes.

```bash
# configurer le serveur proxy pour mettre en cache tous les actifs pendant 1 heure
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=static_cache:20m inactive=60m;

# définir l'en-tête de contrôle de cache à une durée maximale de 1 heure
add_header Cache-Control "public, max-age=3600";

# mettre en cache tous les actifs
location ~* \\.(jpg|jpeg|png|css|js)$ {
    proxy_cache static_cache;
    proxy_cache_valid 200 60m;
    proxy_pass http://origin_server;
}

```

## Bonnes pratiques de pré-cache

Le pré-cache est une technique extrêmement utile pour améliorer les performances de votre application web. Cependant, vous devez suivre certaines bonnes pratiques pour vous assurer que le pré-cache donne les résultats souhaités.

Voici quelques bonnes pratiques à garder à l'esprit lors du pré-cache :

* **Cachez uniquement les ressources nécessaires.** Le cache de trop de ressources peut entraîner un gaspillage d'espace de stockage et annuler les avantages du pré-cache. Vous ne devez cache que les ressources qui ont le plus grand impact sur l'amélioration des performances.
* **N'oubliez pas de versionner les ressources pré-cache.** Même les ressources pré-cache peuvent être mises à jour à l'avenir. Vous devez donc vous assurer d'utiliser le versionnage pour identifier la dernière version d'une ressource. Lorsqu'une ressource est mise à jour, vous devez également incrémenter le numéro de version pour suivre les mises à jour ultérieures.
* **Utilisez des en-têtes de contrôle de cache appropriés**. Les en-têtes de contrôle de cache nous aident à nous assurer que les ressources sont mises en cache pendant la bonne durée. Par exemple, une plateforme de commerce électronique peut avoir une liste de produits best-sellers qui change fréquemment en raison de produits qui quittent ou rejoignent les charts. Ces ressources doivent avoir une durée de cache plus courte pour garder le cache pertinent.
* **Utilisez un réseau de diffusion de contenu (CDN)**. Les CDN aident à réduire le temps nécessaire pour charger les ressources. Vous devez utiliser un CDN pour distribuer les ressources aux serveurs de périphérie situés plus près de l'utilisateur. Les serveurs de périphérie en combinaison avec le pré-cache est une technique puissante pour améliorer les performances de votre application web.
* **Utilisez une bibliothèque ou un framework pour activer le pré-cache**. Même si vous pourriez être tenté de construire vos solutions pour le pré-cache à partir de zéro, vous devriez envisager d'utiliser une bibliothèque telle que Workbox pour activer les service workers pour le pré-cache des ressources. Pour le cache côté serveur, envisagez d'utiliser une combinaison de CDN et de serveurs proxy de cache.

## Inconvénients du pré-cache

Bien que le pré-cache soit une technique très utile et principalement bénéfique, vous devez vous assurer d'éviter les inconvénients suivants :

* **Données obsolètes** : Avec le pré-cache, vous stockez des données à l'avance. Ces données peuvent ne pas toujours être à jour. Si les données changent fréquemment, la version pré-cache deviendra obsolète et entraînera des problèmes. Pour éviter cette situation, vous devez avoir une stratégie appropriée pour l'invalidation du cache qui peut se débarrasser des données obsolètes.
* **Utilisation inefficace des ressources** : Lors du pré-cache, vous supposez essentiellement que les données que vous mettez en cache seront consultées fréquemment. De telles suppositions peuvent **ne pas** toujours être correctes et vous pouvez vous retrouver avec des données qui ne sont pas nécessaires fréquemment. Si la taille de ces données dépasse une certaine limite, la solution de cache peut devenir inefficace et entraîner un gaspillage de ressources précieuses qui peuvent être utilisées à d'autres fins.
* **Portée limitée** : Le pré-cache a une portée limitée. Il ne s'applique qu'aux données connues à l'avance et qui peuvent être pré-remplies dans le cache. Il s'agit principalement de données statiques. Il est difficile d'implémenter le pré-cache pour les données générées dynamiquement sans l'utilisation d'algorithmes complexes.

## C'est tout

En conclusion, le pré-cache est une technique puissante qui peut potentiellement améliorer la vitesse et les performances de votre site web.

Avec le pré-cache, vous essayez essentiellement d'anticiper les ressources qu'un utilisateur est susceptible de demander ensuite et de les télécharger à l'avance.

Même seul, le **pré-cache est une technique révolutionnaire** qui peut avoir un impact significatif sur l'expérience utilisateur de votre application web.

Cependant, il est tout aussi important de garder à l'esprit que le pré-cache n'est qu'un aspect du processus d'optimisation du site web. Vous devriez essayer de l'utiliser en conjonction avec d'autres techniques telles que la minification, la compression et l'optimisation du code.

Si vous avez aimé cet article et l'avez trouvé utile, envisagez de le partager avec des amis et des collègues.