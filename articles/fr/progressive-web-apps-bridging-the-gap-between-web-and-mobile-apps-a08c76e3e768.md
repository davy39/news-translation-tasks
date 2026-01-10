---
title: 'Applications Web Progressives : Combler l''écart entre les applications web
  et mobiles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T11:16:26.000Z'
originalURL: https://freecodecamp.org/news/progressive-web-apps-bridging-the-gap-between-web-and-mobile-apps-a08c76e3e768
coverImage: https://cdn-media-1.freecodecamp.org/images/1*G8GpxgnXeOoagIk5huIbUw.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Applications Web Progressives : Combler l''écart entre les applications
  web et mobiles'
seo_desc: 'By Ajay NS

  Unless you’ve been living under a rock, you’ve probably heard of PWAs or Progressive
  Web Apps. It’s a hot topic right now because its support is increasing in multiple
  platforms, and major companies are deciding to work on PWA versions of ...'
---

Par Ajay NS

Sauf si vous avez vécu sous une pierre, vous avez probablement entendu parler des PWAs ou Applications Web Progressives. C'est un sujet brûlant en ce moment car leur support augmente sur plusieurs plateformes, et de grandes entreprises décident de travailler sur des versions PWA de leurs applications web, notamment Twitter, Lyft, Starbucks, NASA, et bien d'autres.

Récemment, cela a attiré encore plus d'attention lorsque Apple a annoncé la prise en charge des Service Workers et du Web Manifest pour Safari. Microsoft a introduit les PWAs dans le Windows Store, et Chrome propose une prise en charge expérimentale des PWAs pour toutes les plateformes.

D'accord, cela devrait suffire à vous convaincre qu'elles valent la peine d'être explorées.

Ainsi, cet article est un résumé des concepts et des approches que suivent les Applications Web Progressives. Je l'ai écrit à partir de mon expérience dans leur développement, et j'ai structuré cet article après avoir suivi la [Formation Google sur les Applications Web Progressives](https://developers.google.com/web/ilt/pwa/).

La formation explique bien comment tout fonctionne ensemble et vous plonge directement dans le code. Le cours [Mobile Web Specialist](https://goo.gl/nvzoPG) d'Udacity pourrait également être utile ici.

### Pourquoi les PWA ?

![Image](https://cdn-media-1.freecodecamp.org/images/dC96dvAcZ241P7xcT3R0P1vt-4GXq-JWBJdu)
_Temps passé par les utilisateurs moyens sur le Web vs les Applications_

Le web est indépendant du système d'exploitation, largement accessible et constitue la plus grande plateforme sur Internet. Pourtant, nous constatons que les utilisateurs passent beaucoup plus de temps sur les applications natives que sur le web.

Pourquoi en est-il ainsi ?

La principale raison est l'expérience fluide et l'engagement que procurent les applications natives. Et si nous apportions ces fonctionnalités aux applications web ? Cela signifierait combiner la facilité d'accès et la portée du web (3 fois supérieure à celle des applications natives), avec l'expérience immersive des applications natives.

Selon Alex Russell, qui a inventé le terme, les PWAs sont :

> Juste des sites web qui ont pris toutes les bonnes vitamines

Ces vitamines sont simplement des fonctionnalités des applications natives que nous ajoutons aux applications web pour obtenir le meilleur des deux mondes. Des applications que vous pouvez accéder directement depuis le web, tout en fonctionnant de manière fluide et rapide, installables, et pouvant même avoir des notifications.

![Image](https://cdn-media-1.freecodecamp.org/images/aEKAnAk-nfEiXs-SRPOL05qVmDEh9U8LacSF)
_Comparaison des applications web, natives et progressives, tirée de la formation PWA de Google_

### Ce qui fait des PWAs ce qu'elles sont

Les fonctionnalités clés selon [Google](https://developers.google.com/web/progressive-web-apps/) :

1. **Fiable** : D'abord hors ligne, ce qui signifie qu'elle doit fournir des interfaces même en cas de mauvaise connexion Internet ou d'absence de connexion. Mais cela ne signifie pas non plus que l'application doit simplement pouvoir fonctionner hors ligne, mais plutôt qu'elle fournit un service ininterrompu dans toutes les conditions de réseau.
2. **Rapide** : Chargement instantané et expériences fluides même lors du chargement du contenu.
3. **Engageante** : Doit fournir une expérience immersive, équivalente à celle d'une application native. Peut avoir des notifications push, des paiements web, ou une gestion des identifiants, etc. Être installable est également une fonctionnalité clé ici.

Mais ce ne sont que des concepts — comment penser à la mise en œuvre d'un point de vue technique ? Peter O'Shaughnessy de Samsung Internet a une bonne approche pour cela :

![Image](https://cdn-media-1.freecodecamp.org/images/ZcYyAHiWU1fGXX5oPhYOk-fRFNa6frEkS8Jr)
_Normes des PWA_

Alors, examinons ces points un par un :

### Service Worker

C'est un fichier JavaScript qui s'exécute séparément du thread principal du navigateur en arrière-plan, interceptant les requêtes réseau, mettant en cache les ressources et fournissant une base pour plusieurs API, y compris les notifications push, la synchronisation en arrière-plan et la mise en cache.

![Image](https://cdn-media-1.freecodecamp.org/images/mDv4XvnYgfsotIUSEOP7-iIwAsQwBWrQgs76)
_Diagramme de flux pour les Service Workers interceptant les requêtes réseau_

La capacité des service workers à s'exécuter séparément en arrière-plan aide à donner beaucoup de fonctionnalités à l'application même lorsqu'elle est fermée, offrant une expérience plus proche des applications natives et plus engageante.

Cela aide également à rendre l'application d'abord hors ligne, car il agit comme un proxy entre le serveur et l'application.

Une introduction aux service workers peut être trouvée [ici](https://developers.google.com/web/fundamentals/primers/service-workers/), et Google a quelques outils d'aide open source dans leur [Service Worker Toolbox](https://github.com/GoogleChromeLabs/sw-toolbox).

### HTTPS

Hypertext Transfer Protocol Secure est une adaptation pour des communications HTTP sécurisées utilisant le chiffrement SSL ou TLS. Mais n'entrons pas dans cela — plutôt, nous allons voir pourquoi c'est important.

Outre le fait que les PWAs sont censées être hautement sécurisées, les service workers qu'elles utilisent peuvent intercepter les requêtes réseau et modifier les réponses. Cela peut être facilement exploité pour causer de graves attaques. Il existe de nombreux services qui aident à obtenir un certificat SSL pour votre site comme [LetsEncrypt](https://letsencrypt.org/) et [SSLforfree](https://www.sslforfree.com/).

### Manifest pour les Applications Web

En gros, un fichier JSON qui donne des informations sur la façon dont l'application doit apparaître sur l'écran d'accueil, sur le web, et ainsi de suite. Il peut être utilisé pour ajouter une couleur de thème, des icônes pour l'écran d'accueil, et un écran de démarrage, pour n'en nommer que quelques-uns.

![Image](https://cdn-media-1.freecodecamp.org/images/A5vD1Vw7DTXejsWsc124V8uWz8CqgHNfPEqs)

Un manifest simple ressemblerait à ceci :

```
{  "name": "HackerWeb",  "short_name": "HackerWeb",  "start_url": ".",  "display": "standalone",  "background_color": "#fff",  "description": "Une application Hacker News simplement lisible.",  "icons": [{    "src": "images/touch/homescreen48.png",    "sizes": "48x48",    "type": "image/png"  }, {    "src": "images/touch/homescreen72.png",    "sizes": "72x72",    "type": "image/png"  }, {    "src": "images/touch/homescreen96.png",    "sizes": "96x96",    "type": "image/png"  }, {    "src": "images/touch/homescreen192.png",    "sizes": "192x192",    "type": "image/png"  }],  "related_applications": [{    "platform": "play",    "url": "https://play.google.com/store/apps/details?id=cheeaun.hackerweb"  }]}
```

Il rend l'application plus conviviale avec toutes les icônes, les thèmes et les écrans de démarrage. Elle est installable avec juste un fichier JSON.

Lisez-en plus à leur sujet dans les [Web Docs](https://developer.mozilla.org/en-US/docs/Web/Manifest) de Mozilla et générez-en un [ici](https://tomitm.github.io/appmanifest/).

Pour les favicons de différentes tailles, vous pouvez les générer à partir d'une seule image de haute qualité en utilisant [Favicon-Generator](https://www.favicon-generator.org/) et le thème. Les couleurs de fond peuvent être choisies dans la palette de l'application.

### Notifications Push et Synchronisation en Arrière-plan

Le serveur envoie des messages push aux service workers, qui les interceptent et mettent à jour l'état local ou affichent une notification à l'utilisateur. Comme ils s'exécutent indépendamment en tant que processus en arrière-plan, cela est possible même avec l'application fermée. L'[API Push](https://developer.mozilla.org/en-US/docs/Web/API/Push_API) pourrait vous aider à implémenter cette fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/ncx23EVESHpPFgbcxpXKQqGAJXrb1RqQntSb)

L'[API de Synchronisation en Arrière-plan](https://www.chromestatus.com/feature/6170807885627392) envoie des mises à jour périodiques au serveur afin que l'application puisse se mettre à jour lorsqu'elle est en ligne. En gros, elle s'assure que tous les messages sont envoyés lorsqu'il y a une bonne connexion.

### Concepts Additionnels

Voici quelques approches et normes à suivre lors de la création d'Applications Web Progressives.

#### Lighthouse et Liste de Contrôle PWA

![Image](https://cdn-media-1.freecodecamp.org/images/fzop4QpaTHgwxutmtCZx7ko-JPk-KAb5goj2)
_Audit Lighthouse effectué pour l'application PWA d'AliExpress_

[Lighthouse](https://developers.google.com/web/tools/lighthouse/) est un outil automatisé pour vérifier la qualité des pages web en effectuant des audits sur la performance, les meilleures pratiques, l'accessibilité, le SEO et les normes des applications web progressives. C'est un bon moyen de vérifier si votre application répond aux normes et de voir à quel point elle est une bonne PWA.

Vous pouvez découvrir ce qui manque à votre application web et comment elle peut être améliorée en utilisant les suggestions des audits Lighthouse et également cette [Liste de Contrôle PWA](https://developers.google.com/web/progressive-web-apps/checklist) de Google qui établit toutes les directives générales à suivre et comment résoudre les problèmes. Et la meilleure partie est que, pour l'instant, Lighthouse est intégré à Chrome DevTools !

#### Stockage

Selon Addy Osmani (de l'équipe Google Chrome), la meilleure pratique pour le stockage à suivre dans les PWAs est :

> Utilisez l'[**API Cache**](https://davidwalsh.name/cache) pour les **ressources adressables par URL** (faisant partie du [Service Worker](https://developers.google.com/web/fundamentals/primers/service-worker/)). Pour toutes les autres données, utilisez **IndexedDB** (avec un wrapper [Promesses](http://www.html5rocks.com/en/tutorials/es6/promises/)).

Ces deux API sont asynchrones et fonctionnent avec les web/service workers. Cela les rend adaptées à une utilisation avec les PWAs, contrairement à d'autres méthodes telles que localStorage.

Pour une idée rapide de ce qu'est IndexedDB, vous pouvez vous référer à [cette](https://developers.google.com/web/ilt/pwa/working-with-indexeddb) ressource.

En termes simples, c'est un système de stockage noSQL à grande échelle qui peut stocker à peu près n'importe quoi depuis le navigateur. Il fonctionne également comme une API haute performance.

#### Mise en Cache

L'API Cache qui peut être utilisée dans le Service Worker vous permet de stocker des réponses indexées par requête. Cela permet de charger directement le contenu depuis le cache en cas de mauvaise connexion réseau et il peut également être configuré pour charger uniquement les données nécessaires tout en s'appuyant sur le cache pour le reste.

![Image](https://cdn-media-1.freecodecamp.org/images/RVLZ0I1tzR95WCKrzfjZdM1eQpSJ4XJkn27M)
_Exemple de coque d'application dans Flipkart Lite PWA_

L'un des modèles populaires pour les approches d'abord hors ligne et similaires aux applications natives est la mise en cache de la coque de l'application. Cela inclut tout le HTML, CSS et JavaScript de base qui constituent la navigation/barres d'outils ou tout ce qui est commun dans toute la mise en page. Ainsi, la coque de l'application se charge instantanément et affiche un écran de chargement pendant que le contenu est récupéré, offrant une expérience rationalisée.

#### Fetch et Promesses

Pour récupérer des ressources, la méthode la plus récente et recommandée est d'utiliser l'API Fetch avec les Promesses.

```
// Un exemple de base de fetch avec des promesses
fetch('examples/example.json').then(function(response) {   // Faire des choses avec la réponse
}).catch(function(error) {   console.log('Il semble qu'il y ait eu un problème : \n', error);
});
```

Les requêtes XMLHttpRequest (XHR) sont inutilement verbeuses et il en va de même pour les callbacks, qui fragmentent le code et causent de la confusion lorsque de longues chaînes de callbacks sont utilisées.

Les Promesses sont une meilleure façon de gérer le code asynchrone.

Les Service Workers, l'API Cache et les requêtes réseau utilisent largement ces fonctionnalités pour effectuer une variété de tâches et sont nécessaires au niveau de base, d'où l'importance d'avoir une idée précise de ces concepts.

#### Design Réactif

Cela ne signifie pas seulement utiliser des unités de largeur réactives. Les blocs de contenu doivent être manipulés pour répondre aux besoins de la mise en page. L'application doit sembler parfaitement conçue pour le mobile, et globalement, elle doit ressembler à une application native bien conçue.

![Image](https://cdn-media-1.freecodecamp.org/images/bluXA0ACI9qf0KuVi8fqjs77avSYwsEZ89ZZ)
_Étapes pour manipuler le contenu_

Les systèmes de mise en page CSS modernes tels que [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) (Apprenez avec ce [cours gratuit](https://cssgrid.io/) de Wes Bos) ou [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) peuvent être d'une grande aide pour gérer différentes mises en page et arrangements de différentes tailles d'écran.

#### Optimisation des Images

![Image](https://cdn-media-1.freecodecamp.org/images/rxc-8mnQTfIeBdLHQ2oS3Iw0ZgZg1iU173Mi)
_Répartition des données dans les applications web_

L'une des fonctionnalités clés des PWAs est qu'elles doivent être extrêmement rapides, et vous pouvez voir que les images n'aident pas. Elles doivent être remplacées par des SVGs ou supprimées chaque fois que possible. Les formats optimisés pour le web ne doivent être utilisés qu'avec la taille la plus faible possible.

Mais il est également important que ces images soient fluides et s'adaptent bien aux différentes tailles d'écran, car une autre fonctionnalité importante des PWAs est leur expérience similaire à une application native.

### Histoires et Exemples

![Image](https://cdn-media-1.freecodecamp.org/images/CLx2fiuhFfqkS4pK3FeOS9IR7chAlZqgaC3E)
_Quelques exemples concrets de PWAs_

### Conclusion

Avec chaque service lançant une application, les gens trouvent souvent peu pratique d'aller réellement dans le magasin et de la télécharger. Ils détestent passer autant de temps, de données mobiles et d'espace sur l'appareil. Cela les conduit souvent vers le web, qui nécessite beaucoup moins d'efforts. Mais alors, nous constatons des taux de rebond élevés, car l'expérience web n'est pas aussi fluide et optimale que celle de l'application native.

La solution à ces deux problèmes est les Applications Web Progressives, qui combinent le meilleur des deux mondes, offrant une expérience utilisateur optimale.

Comme mentionné, avec le support des PWAs augmentant considérablement sur toutes les plateformes, maintenant serait le meilleur moment pour commencer.

[L'Application Web Progressive de BookMyShow entraîne une augmentation de 80 % des conversions](https://developers.google.com/web/showcase/2017/bookmyshow)

[Construction de Flipkart Lite : Une Application Web Progressive](https://medium.com/progressive-web-apps/building-flipkart-lite-a-progressive-web-app-2c211e641883)

[De grands exemples d'applications web progressives dans une seule pièce](https://www.progressivewebapproom.com/index.html)

### Lectures Complémentaires

[**6 mythes sur les Applications Web Progressives**](https://medium.com/samsung-internet-dev/6-myths-of-progressive-web-apps-81e28ca9d2b1)

[Des termes comme « Applications Web Progressives » (PWAs) sont utiles pour aider à répandre des concepts, mais ils comportent un risque de mauvaise utilisation et… medium.com](https://medium.com/samsung-internet-dev/6-myths-of-progressive-web-apps-81e28ca9d2b1)

[**Une étude de cas sur les performances d'une Application Web Progressive Tinder**](https://medium.com/@addyosmani/a-tinder-progressive-web-app-performance-case-study-78919d98ece0)

[Tinder a récemment glissé vers la droite sur le web. Leur nouvelle Application Web Progressive réactive — Tinder Online — est disponible pour… medium.com](https://medium.com/@addyosmani/a-tinder-progressive-web-app-performance-case-study-78919d98ece0)

Conversion des applications React en PWAs :

[**Applications Web Progressives React — Partie 1**](https://medium.com/progressive-web-apps/react-progressive-web-apps-part-1-1cf381421672)

[Les Applications Web Progressives (PWA) gagnent beaucoup en popularité ces jours-ci, et avec l'une des mises à jour de cette année (2017), le… medium.com](https://medium.com/progressive-web-apps/react-progressive-web-apps-part-1-1cf381421672)

Conversion des applications Angular en PWAs :

[**Un nouveau Service Worker Angular — création d'applications web progressives automatiques. Partie 1 : théorie**](https://medium.com/progressive-web-apps/a-new-angular-service-worker-creating-automatic-progressive-web-apps-part-1-theory-37d7d7647cc7)

[Annonce : Il y a une « Partie 2 : pratique » de cet article disponible. medium.com](https://medium.com/progressive-web-apps/a-new-angular-service-worker-creating-automatic-progressive-web-apps-part-1-theory-37d7d7647cc7)

_J'espère que vous avez apprécié cet article et l'avez trouvé intéressant ! Vous pouvez consulter tous mes projets sur [Github](http://github.com/ajayns/) et n'hésitez pas à me contacter sur [Twitter](https://twitter.com/ajayns08) !_