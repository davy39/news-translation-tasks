---
title: Comment empêcher vos données d'analyse d'être bloquées par les bloqueurs de
  publicité
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2017-04-28T22:45:56.000Z'
originalURL: https://freecodecamp.org/news/save-your-analytics-from-content-blockers-7ee08c6ec7ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZKUrBpg1NORp8sGn7OrIjw.jpeg
tags:
- name: analytics
  slug: analytics
- name: big data
  slug: big-data
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Comment empêcher vos données d'analyse d'être bloquées par les bloqueurs
  de publicité
seo_desc: TL;DR (updated 2021) You can now use dataunlocker.com service, which is
  a fully managed solution for fixing ad blockers' impact on the client-side analytics
  tools such as Google Analytics. Log in to DataUnlocker Admin to complete the quick
  3-step set...
---

> TL;DR (mis à jour 2021) Vous pouvez maintenant utiliser le service [dataunlocker.com](https://dataunlocker.com/), qui est une solution entièrement gérée pour corriger l'impact des bloqueurs de publicité sur les outils d'analyse côté client tels que Google Analytics. Connectez-vous à [DataUnlocker Admin](https://admin.dataunlocker.com/) pour compléter la configuration rapide en 3 étapes de votre application web ou de votre site.

> L'article ci-dessous de 2017 explique certains principes utilisés derrière la [solution](https://github.com/dataunlocker/save-analytics-from-content-blockers), ainsi qu'il est décrit dans le [readme](https://github.com/dataunlocker/save-analytics-from-content-blockers#readme) de la solution.

Lorsque votre produit commence tout juste, chaque utilisateur compte. Il en va de même pour les données sur la manière dont ils interagissent avec votre produit.

Si vous avez essayé d'utiliser des solutions d'analyse comme [Google Analytics](https://www.google.com/analytics/), vous avez peut-être rencontré un problème où la collecte de vos données d'analyse était bloquée par des bloqueurs de publicité.

Selon [PageFair](https://pagefair.com/), [jusqu'à 30%](https://pagefair.com/blog/2017/adblockreport/) des utilisateurs d'Internet utilisent des bloqueurs de publicité en 2017, et ce nombre ne cesse de croître.

Cet article expliquera quelques approches techniques que vous pouvez adopter pour empêcher les bloqueurs de publicité de bloquer également vos analyses. Nous utiliserons [Google Analytics](https://www.google.com/analytics/) dans cet article, bien que beaucoup de cela puisse être appliqué à d'autres outils d'analyse.

![Image](https://cdn-media-1.freecodecamp.org/images/bqQCPzK4HaXeuneWOAyXPSaN9iLBFPq6cVJ8)

### Quelques moyens de contourner les bloqueurs de publicité

Presque tous les bloqueurs de publicité fonctionnent de la même manière : ils interdisent certaines requêtes http(s) du navigateur pour le contenu à des URL qui correspondent à un certain masque de leur base de filtrage.

La plupart des bloqueurs de publicité mettent sur liste noire [www.google-analytics.com](http://www.google-analytics.com) par défaut, et bloquent toute tentative de la [bibliothèque JavaScript de Google Analytics](https://developers.google.com/analytics/devguides/collection/analyticsjs/) d'envoyer ou de récupérer les données de ses serveurs d'analyse.

Heureusement pour les développeurs, les bloqueurs de publicité ne bloquent pas les requêtes vers _nos propres noms de domaine_ par défaut, car cela pourrait nuire au fonctionnement de l'application web. Cette lacune révèle un moyen d'éviter le blocage des analyses jusqu'à ce que votre service web devienne suffisamment connu pour que certaines de ses URL apparaissent dans les filtres des bloqueurs de publicité.

En fait, même après que certaines URL apparaissent dans la base de filtrage de contenu, vous pouvez commencer à jouer avec les bloqueurs de publicité en inventant des choses terribles, comme des URL d'analyse changeant toutes les heures (bien que cela soit au-delà du cadre de cet article). Certaines de ces approches sont appliquées par des services comme [DataUnlocker.com](https://dataunlocker.com/) et [Adtoniq](https://adtoniq.io/), qui offrent aux utilisateurs une expérience sans bloqueurs de publicité même lorsque les bloqueurs de publicité sont activés.

### Une explication de haut niveau de ce que nous allons faire

Dans cet article, nous supposerons que nous n'avons aucune restriction de permission côté serveur. Nous allons écrire la solution de démonstration (quelques lignes de code) pour la plateforme Node.js. Une fois que vous comprendrez comment cela fonctionne, vous devriez être en mesure de porter cette solution à n'importe quel langage de programmation ou plateforme.

La solution que je vais décrire est assez minimale, et si vous êtes un développeur web expérimenté, cela peut ne vous prendre que quelques minutes pour la mettre en place.

Nous allons utiliser une approche de proxy simple sans avoir besoin de plonger dans le [protocole de mesure de Google Analytics](https://developers.google.com/analytics/devguides/collection/protocol/v1/). En bref, la solution ressemble à ce qui suit :

1. Tout d'abord, [téléchargez](https://www.google-analytics.com/analytics.js) la bibliothèque JavaScript de Google Analytics elle-même et hébergez-la sur votre serveur.
2. Modifiez ensuite le code de la bibliothèque téléchargée pour changer l'hôte cible de _www.google-analytics.com_ vers votre propre nom de domaine en utilisant la fonction de recherche-remplacement.
3. Remplacez le lien du script Google Analytics par défaut dans votre base de code par celui modifié.
4. Créez un point de terminaison [proxy](https://fr.wikipedia.org/wiki/Serveur_mandataire) vers les serveurs Google Analytics sur votre backend. Une étape importante ici est de détecter en plus l'adresse IP du client et de l'écrire explicitement dans les requêtes aux serveurs Google Analytics pour préserver la détection correcte de la localisation.
5. Testez les résultats. Vous avez terminé !

### Le guide complet de l'implémentation technique

Tout le code et les étapes décrites ci-dessous sont disponibles [sur GitHub](https://github.com/dataunlocker/save-analytics-from-content-blockers). La description ci-dessous explique les bases de la méthode, et bien sûr, l'approche suggérée peut être améliorée pour être encore plus « anti-blocage ».

Dans Google Analytics, vous commencez par [acquérir un identifiant de suivi unique](https://support.google.com/analytics/answer/1042508?hl=en) pour votre propriété (service web). Nous utiliserons l'_identifiant de suivi UA-98253329-1_ dans cet article pour la démonstration. N'oubliez pas de remplacer le code de suivi par le vôtre.

Google suggère d'ajouter ce code minifié à vos services web pour activer l'analyse :

```html
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script',
'https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-98253329-1', 'auto');
  ga('send', 'pageview');
</script>
```

En quelques mots, ce code charge la bibliothèque JavaScript de Google Analytics si elle n'a pas été chargée auparavant en insérant la balise de script dans le document. Cette bibliothèque inclut toute la logique de collecte d'analyse, et c'est la seule chose dont nous avons besoin pour continuer.

#### **Étape 1 : Télécharger et patcher la bibliothèque d'analyse de Google**

Téléchargez le script directement depuis [_https://www.google-analytics.com/analytics.js_](https://www.google-analytics.com/analytics.js','ga'), ouvrez-le avec n'importe quel éditeur de texte et remplacez toutes les occurrences de :

```
www.google-analytics.com
```

par cette chaîne exacte :

```
"+location.host+"/analytics
```

En patchant la bibliothèque d'analyse de cette manière, elle commencera à faire des requêtes vers les points de terminaison de l'hôte local (_my.domain.com/analytics_) au lieu de _www.google-analytics.com_. Placez ce fichier _analytics.js_ patché sur votre serveur après le remplacement.

#### **Étape 2 : Remplacer le script d'analyse par celui patché**

Modifions le code d'intégration de Google Analytics de manière à ce qu'il utilise notre bibliothèque patchée au lieu de celle par défaut :

```html
<script>
(function(i,s,o,r){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date()})(window,document,'script','ga');
  ga('create', 'UA-98253329-1', 'auto');
  ga('send', 'pageview');
</script>
<script src="/analytics.js" async></script>
```

Notez que ici, le navigateur recherchera le script d'analyse patché dans la racine du document de votre serveur, dans ce cas, _my.domain.com/analytics.js_. Vérifiez si vous avez placé le script dans la racine du document ou changé le chemin dans la balise de script ci-dessus. Vous pouvez également vérifier les résultats en exécutant un test sur votre serveur local (voir le [readme](https://github.com/dataunlocker/save-analytics-from-content-blockers#readme) pour savoir comment exécuter l'exemple GitHub).

Vous devriez voir quelque chose comme ceci [dans les outils de développement du navigateur](https://developer.chrome.com/devtools) :

![Image](https://cdn-media-1.freecodecamp.org/images/sgV8TCIqobvskrBN7-fGxVHn3T5z8NPWRtip)

En fin de compte, nous voulons que l'acte de téléchargement de votre fichier _analytics.js_ patché retourne une réponse réussie — un statut 200 (OK) ou 304 (non modifié). Mais à ce stade, la requête vers _my.domain.com/analytics/collect_ devrait répondre avec un statut 404, puisque nous n'avons pas encore implémenté le serveur proxy.

#### **Étape 3 : Implémentation du serveur proxy le plus simple**

Maintenant, nous allons coder un peu. Notre objectif est d'implémenter [le serveur proxy](https://fr.wikipedia.org/wiki/Serveur_mandataire), qui transportera nos requêtes d'analyse de notre serveur vers le vrai serveur Google Analytics. Nous pouvons faire cela de nombreuses manières, mais en tant qu'exemple, utilisons [Node.js](http://nodejs.org) et [Express.js](http://expressjs.com) avec le package [express-http-proxy](https://www.npmjs.com/package/express-http-proxy).

En rassemblant tous les fichiers de l'exemple ensemble ([voir GitHub](https://github.com/dataunlocker/save-analytics-from-content-blockers)), nous devrions finir avec le code de serveur JavaScript suivant :

```js
var express = require("express"), 
    proxy = require("express-http-proxy"), app = express();

app.use(express.static(__dirname)); // servir les fichiers statiques depuis le répertoire courant

function getIpFromReq (req) { // obtenir l'adresse IP du client
    var bareIP = ":" + ((req.connection.socket && req.connection.socket.remoteAddress)
        || req.headers["x-forwarded-for"] || req.connection.remoteAddress || "");
    return (bareIP.match(/:([^:]+)$/) || [])[1] || "127.0.0.1";
}

// proxyfier les requêtes de /analytics vers www.google-analytics.com.
app.use("/analytics", proxy("www.google-analytics.com", {
    proxyReqPathResolver: function (req) {
        return req.url + (req.url.indexOf("?") === -1 ? "?" : "&")
            + "uip=" + encodeURIComponent(getIpFromReq(req));
    }
}));

app.listen(1280);
console.log("Application web prête sur http://localhost:1280");
```

Les dernières lignes ici font le proxy. Le seul truc que nous faisons ici, au lieu de simplement proxyfier, est de détecter et d'ajouter l'adresse IP du client explicitement sous la forme d'un [paramètre d'URL de protocole de mesure](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#uip). Cela est nécessaire pour collecter des données de localisation précises, car toutes les requêtes vers Google Analytics proviennent à l'origine de l'adresse IP de notre serveur, qui reste constante.

Après avoir configuré notre proxy serveur, nous pouvons vérifier si la requête vers notre point de terminaison _/collect_ retourne maintenant avec succès un statut HTTP 200 OK :

![Image](https://cdn-media-1.freecodecamp.org/images/rudi5M1aU7DuAx7O4BCM5MQvo7Nt4H4R8pBH)

Nous pouvons utiliser, par exemple, une connexion anonyme pour vérifier que la localisation est également détectée correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/rovmpfmeku6ZNYnxY6-wJkvqaq9aQejAl3GG)

Cette approche de « serveur proxy » est une solution rapide pour l'analyse qui permet à vos services d'éviter les bloqueurs de publicité. Mais cette méthode repose sur le côté navigateur, et si le script du navigateur ne envoie pas pour une raison quelconque les informations d'analyse à nos serveurs, nous n'obtenons rien.

La dernière étape possible si vous souhaitez implémenter une solution solide est d'envoyer les analyses directement depuis le serveur en utilisant des bibliothèques côté serveur disponibles pour différents langages ([NodeJS](http://github.com/peaksandpies/universal-analytics), [Python](http://github.com/mirumee/google-measurement-protocol), [Ruby](https://github.com/tpitale/staccato), [PHP](https://github.com/theiconic/php-ga-measurement-protocol)). Cette approche évitera définitivement tout bloqueur de contenu, car chaque requête vers les serveurs d'analyse provient directement de nos serveurs.

Encore une fois, l'application de démonstration est disponible [sur GitHub](https://github.com/dataunlocker/save-analytics-from-content-blockers), n'hésitez pas à la tester ! Faites-moi savoir si vous avez des commentaires ou des expériences intéressantes en utilisant cette approche.

Merci d'avoir lu !