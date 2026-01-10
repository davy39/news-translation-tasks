---
title: Comment augmenter le score Google Lighthouse de votre application web progressive
  à 100
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-27T07:51:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wc20QBMHUo9cXW22eJOP3g.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment augmenter le score Google Lighthouse de votre application web progressive
  à 100
seo_desc: 'By James Y Rauhut

  If there’s one message the Chrome Dev Team wants to drive home to developers, it’s
  this: performance matters.

  Speed was the centerpiece of their recent Chrome Developers Summit. They made it
  abundantly clear that users have little p...'
---

Par James Y Rauhut

S'il y a un message que l'équipe de développement Chrome veut faire passer aux développeurs, c'est celui-ci : **la performance compte**.

La vitesse était au cœur de leur récent Chrome Developers Summit. Ils ont clairement indiqué que les utilisateurs ont peu de patience et que les réseaux mobiles ont une latence élevée.

Si vous pouvez maximiser la vitesse de votre application web, Google vous donnera un meilleur classement dans ses résultats de moteur de recherche. Et un meilleur classement signifie beaucoup plus d'utilisateurs. Et des utilisateurs plus heureux, aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/vZRsLSC8cYvsotqm8C9SL2BlR9xeL4kzoOpu)

Google a même construit un [outil en ligne de commande et un plugin Chrome appelé Lighthouse](https://github.com/GoogleChrome/lighthouse/) pour vous guider vers des performances élevées.

Lighthouse simule de nombreuses situations différentes qui pourraient affecter l'expérience de vos utilisateurs. Il retourne ensuite une note de 1 à 100 sur la façon dont votre application web progressive les gère.

Vous pourriez penser : « Pourquoi devrais-je laisser Google me dire comment structurer mon site web ? » Ou peut-être pensez-vous : « Eh bien, Google ne connaît pas toutes les autres exigences de mon projet en plus de la vitesse. »

Eh bien, je ne pense pas que Google essaie d'être une autorité dans ce domaine ou de définir vos priorités. Au contraire, je pense que Google a construit Lighthouse pour gamifier le processus d'atteinte des métriques de performance qu'ils pensent que les utilisateurs exigent.

Vous devriez donc évaluer chaque critère de Lighthouse par rapport à vos priorités existantes, puis décider vous-même quels goulots d'étranglement valent la peine d'être résolus.

Quand j'ai découvert le plugin Lighthouse, j'ai testé mon [site portfolio des années 90 sans complexe](https://www.seejamescode.com/). J'avais assemblé cette application web plus tôt cette année, après m'être lassé de mettre à jour manuellement mon travail.

En utilisant Node, Webpack et React, mon site web — [seejamescode.com](https://www.seejamescode.com/) — répond aux requêtes en récupérant mon activité récente depuis de nombreuses API différentes. J'étais assez satisfait de l'application.

C'était jusqu'à ce que je lance Lighthouse, qui m'a donné un score de 63/100. Au lieu d'être frustré, j'ai pris ce score comme un défi pour apprendre de nouvelles choses pendant mon temps libre.

Chaque fois que j'apprenais une technique pour améliorer le score de mon site personnel, je l'appliquais ensuite aux projets de l'entreprise et les améliorais selon cet ordre :

1. Améliorer le premier rendu significatif (affichage de l'interface utilisateur)
2. Améliorer l'indice de vitesse perceptuelle
3. Ajouter un fichier manifest pour les répertoires
4. Ajouter HTTPS et rediriger vers celui-ci
5. Ajouter des service workers pour une capacité hors ligne
6. S'assurer que les utilisateurs avec JavaScript désactivé reçoivent les mêmes informations que ceux avec JavaScript activé.

Examinons plus en détail ce que chaque optimisation implique.

### Le premier rendu significatif

Le premier rendu significatif est quelque chose que les développeurs web ont toujours suivi, mais avec une légère variation. Nous nous sommes toujours préoccupés du temps qu'il faut pour qu'un utilisateur voie du contenu sur la page (premier rendu). Le premier rendu _significatif_ nous demande de mesurer le temps qu'il faut pour que l'utilisateur voie le contenu principal au lieu d'une simple barre de navigation.

Intéressamment, cela peut être résolu de la même manière que beaucoup d'entre nous abordent déjà la performance : en s'assurant que l'application envoie le moins de données possible.

Par exemple, un commentateur a inspecté mon site. Ils ont découvert que je demandais des images d'environ 1200px de large ! J'étais content qu'ils l'aient découvert car c'était la première étape pour réduire le temps de chargement de mon site. Ces images prenaient beaucoup de temps à charger pour un utilisateur, malgré le fait que mon CSS n'affichait pas les images plus larges que 500px.

En demandant des images aussi petites que 500px, j'ai pu réduire de moitié la taille de ces requêtes d'images.

Une autre astuce pour diminuer mon premier rendu significatif était d'être plus intelligent avec mon bundle Webpack. Si vous utilisez Webpack, assurez-vous de consulter les [nombreuses optimisations](https://medium.lucaskatayama.com/reducing-bundle-js-size-from-webpack-8a9c3adbdad4#.sk6gtlcqj) que vous pouvez faire pour la production. La chose la plus importante que vous pouvez faire est d'être intelligent avec vos dépendances.

[Inspectez votre bundle](https://www.npmjs.com/package/webpack-bundle-analyzer) et déterminez s'il y a du code tiers dont vous pouvez vous passer. Après avoir inspecté mon propre bundle, j'ai réalisé que je n'avais pas vraiment besoin de Moment.js. Bien que cette bibliothèque ajoute beaucoup de valeur, la supprimer comme dépendance a réduit mon bundle de 60ko.

Le moyen le plus rapide de réduire le temps de chargement de votre application Node est de vous assurer que tout ce qui est envoyé est compressé. Consultez le [middleware de compression Node.js](https://www.npmjs.com/package/compression#expressconnect). Si vous utilisez Express, vous n'avez besoin que de ce middleware, qui gérera le reste pour vous. J'ai vu ce middleware réduire la taille de chargement des applications de plus de moitié !

![Image](https://cdn-media-1.freecodecamp.org/images/uWaiSdk5j408-BInyQL5HAjQADYicVe3dft9)
*Si vous souhaitez suivre les dépendances de votre bundle Webpack pendant le développement, consultez [Ken Wheeler](https://github.com/FormidableLabs/webpack-dashboard" rel="noopener" target="_blank" title="">Webpack Dashboard</a> du célèbre <a href="https://twitter.com/ken_wheeler/" rel="noopener" target="_blank" title="). « Maintenant, lorsque vous exécutez votre serveur de développement, vous travaillez essentiellement à la NASA. »*

### Indice de vitesse perceptuelle ✨

L'indice de vitesse perceptuelle est une excellente statistique en raison de son intégration avec l'expérience utilisateur. À quelle vitesse vos utilisateurs perçoivent-ils votre application ? Voient-ils des saccades pendant le chargement du contenu ? Sont-ils confiants en sachant que la page a fini de charger ?

Les « sauts de contenu » sont l'une des principales causes d'un mauvais indice de vitesse perceptuelle. Cela se produit pour deux raisons :

1. Votre utilisateur commence à chercher son contenu souhaité dès que possible, ce qui signifie qu'il fera défiler avant que votre page ne soit complètement chargée.
2. Vos éléments conteneurs n'ont pas de hauteurs prédéfinies en CSS.

La partie délicate de la correction de cela est que vous devez soit connaître l'espace physique que votre contenu occupera à l'écran, soit le simuler au mieux.

De nombreux développeurs ont vu une solution dans l'application mobile de Facebook, appelée « placeholders squelettes ». Pendant que l'application mobile de Facebook récupère des données, elle remplit les publications avec des barres grises qui simulent l'espacement des titres, images et paragraphes.

Une solution plus simple consiste à spécifier la hauteur minimale pour vos éléments conteneurs. Cela réduira la probabilité que les utilisateurs rencontrent des sauts de contenu violents.

### Aidez le Web avec un fichier Manifest

![Image](https://cdn-media-1.freecodecamp.org/images/wN36jAFT4UcQ-oEi6x6YoVD9tOOVRXKekiAu)
*Vous ne trouverez aucun résultat pour « Flipkart » sur l'App Store d'Apple. Cependant, ce n'est pas un problème avec leur application web progressive !*

C'est surtout une question politique. Google et Microsoft veulent détrôner l'App Store d'Apple avec vos applications web. Les entreprises utilisent les métadonnées de votre manifest pour catégoriser et classer votre application web dans leurs répertoires. Cela aide également les navigateurs à créer des icônes agréables lorsque votre utilisateur enregistre votre application sur son écran d'accueil.

En tant que développeur web, il n'y a pas de raison forte de s'opposer à ce critère. De tous les problèmes que je mentionne dans cet article, celui-ci est le plus facile à résoudre. Créez un [fichier manifest.json](https://github.com/seejamescode/see-james-code/blob/master/public/manifest.json) et référencez-le dans une [balise HTML link](https://github.com/seejamescode/see-james-code/blob/master/index.html#L8).

### Sécurisez avec HTTPS

Sécuriser votre site avec HTTPS n'est généralement pas la première chose à laquelle pense un développeur débutant. Après tout, votre site web peut s'en passer.

Mais [les navigateurs font un effort](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https) pour que chaque site web ait un certificat SSL. Cela garantit que des tiers ne modifient pas le code atteignant vos utilisateurs.

Dites adieu au risque de publicités injectées ! Vous pouvez obtenir des certificats SSL gratuits auprès de [Let's Encrypt](https://letsencrypt.org/). Et chaque grande plateforme d'hébergement semble avoir un tutoriel sur la façon de commencer avec Let's Encrypt sur leur plateforme. Par exemple, j'ai trouvé cet article utile lorsque j'ai recherché « [Let's Encrypt et Bluemix](https://www.ibm.com/blogs/bluemix/2016/08/securing-custom-domains-lets-encrypt/). »

Lighthouse s'attend à ce que vous alliez plus loin. Non seulement vous devriez avoir un certificat SSL pour que les URLs « https://... » fonctionnent pour votre site. Lighthouse veut également que vous redirigiez tous les utilisateurs qui tentent d'accéder à « http://... » vers la version https de votre site.

C'est une étape proactive pour aider vos utilisateurs à passer à une destination sécurisée.

Heureusement, c'est tout ce qu'il m'a fallu pour me conformer à cette exigence en utilisant Node et Express :

```js
// Éviter la redirection si en développement local
if (NODE_ENV === 'production') {
  // Rediriger http vers https
  app.enable('trust proxy');
  app.use (function (req, res, next) {
    if (req.secure) {
      next();
    } else {
      res.redirect('https://' + req.headers.host + req.url);
    }
  });
}

// Je jure que cela vient de StackOverflow comme la moitié de mon code
```

### Devenez compatible hors ligne

Les [service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) vous aident à spécifier quels fichiers les navigateurs des utilisateurs doivent enregistrer localement. Vous pouvez y penser comme un cache plus intelligent pour garantir qu'un utilisateur peut accéder à des informations, même en mode avion.

Cela accélérera également le temps de chargement de votre site web lorsque vos utilisateurs y reviendront à l'avenir.

J'ai été bloqué sur l'implémentation des service workers pendant longtemps car je ne savais pas par où commencer. Puis j'ai trouvé le [diff git le plus magique](https://github.com/jeffposnick/create-react-pwa/compare/c-r-a-0.6.0...c-r-pwa-0.6.0) de [Jeffrey Posnick](https://twitter.com/jeffposnick) démontrant trois changements de fichiers simples qui aident Create-React-App à supporter les service workers. J'aime cet exemple car il montre précisément les parties qui vous aident à l'implémenter, au lieu de simplement vous diriger vers un modèle entier.

À l'avenir, je prévois d'explorer l'utilisation de [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) pour stocker les données d'API qu'un utilisateur reçoit lors de sa première visite, pour des visites de retour encore plus rapides.

### Pas de JavaScript, pas de problème

La cerise sur le gâteau est de s'assurer qu'un utilisateur peut recevoir des informations même s'il a désactivé JavaScript dans son navigateur. Pourquoi les gens désactiveraient-ils JavaScript dans leur navigateur ? Il existe [plusieurs cas d'utilisation étranges](http://softwareengineering.stackexchange.com/questions/26179/why-do-people-disable-javascript). Mais le point principal est : nous nous soucions de l'utilisateur ! Comment les soutenir ?

![Image](https://cdn-media-1.freecodecamp.org/images/-lWSZP5bQzjHCMRCM5FWXQD1wVr9RGxqA5RT)
*Une capture d'écran de ce que les utilisateurs voient lorsqu'ils visitent mon site web sans JavaScript activé. Je souhaite fournir plus d'informations aux utilisateurs sans JavaScript bientôt, mais pour l'instant, ce sont les éléments essentiels. Le rendu côté serveur serait une excellente solution à cela.*

Nous soutenons les navigateurs avec JavaScript désactivé en utilisant la balise [<noscript>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript). Tout ce qui se trouve dans cette balise HTML s'affichera tant que l'utilisateur a désactivé JavaScript. Si vous souhaitez offrir à ces utilisateurs une expérience complète, vous pouvez ajouter un rendu côté serveur.

### Obtenir un score parfait avec Lighthouse

Vous pouvez voir [tous les commits](https://github.com/seejamescode/see-james-code/commits/master) du 14 novembre au 18 décembre.

Bien que tous mes commits s'étendent sur environ un mois, il m'a en réalité fallu beaucoup plus de temps pour atteindre un score parfait sur Lighthouse. Cela est dû au fait que chaque critère de Lighthouse est un élément utile que vous pouvez apprendre seul. Aucun des éléments ne nécessite les autres, mais tous amélioreront l'expérience utilisateur globale de votre application.

Chaque fois que j'apprends à implémenter un nouvel élément sur mon portfolio, je l'implémente ensuite facilement dans mes projets professionnels.

Je suis sûr qu'il y aura éventuellement une mise à jour de Lighthouse qui fera baisser mon score. Ce n'est pas un problème ! Le plugin est toujours en bêta et continuera à me fournir de nouveaux sujets à apprendre.

Mon espoir est que vous releviez ce défi vous-même et fassiez tout ce qui est nécessaire pour aider à améliorer l'expérience de vos utilisateurs.

Veuillez partager dans les commentaires ou [me tweeter](https://twitter.com/seejamescode) des moyens intéressants d'améliorer votre score Lighthouse ! J'essaierai de les partager tous. Je recommande également vivement la série de [Addy Osmani](https://twitter.com/addyosmani) sur les [PWA avec React.js](https://medium.com/@addyosmani/progressive-web-apps-with-react-js-part-i-introduction-50679aef2b12#.dhyo6dmuj) !

Vous pouvez également me contacter en laissant un commentaire, [en m'envoyant un email](mailto:james@seejamescode.com) ou en tweettant à [@seejamescode](https://twitter.com/seejamescode). Je travaille à ATX pour IBM Design et j'adore toujours les conversations avec la communauté de design web.

Merci également à [David Connor](https://twitter.com/Dave_Conner) et [Jason Lengstorf](https://twitter.com/jlengstorf) pour la relecture de cet article !