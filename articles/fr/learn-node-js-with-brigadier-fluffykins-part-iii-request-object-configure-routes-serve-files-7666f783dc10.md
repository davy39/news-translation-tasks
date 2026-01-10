---
title: 'Apprendre Node.js avec Brigadier Fluffykins Partie III : Objet Request, Configurer
  les Routes, Servir des Fichiers'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-29T03:05:48.000Z'
originalURL: https://freecodecamp.org/news/learn-node-js-with-brigadier-fluffykins-part-iii-request-object-configure-routes-serve-files-7666f783dc10
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4E7_DswXy8rFF2Dzrq1H3A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Node.js avec Brigadier Fluffykins Partie III : Objet Request,
  Configurer les Routes, Servir des Fichiers'
seo_desc: 'By Mariya Diminsky

  Welcome to Part III of Learn Node.js With Brigadier Fluffykins, a series created
  to help you easily understand Node.js ❤

  In Part II Brigadier Fluffykins and I walked you through how Node.js is an event
  driven language. You learned ...'
---

Par Mariya Diminsky

Bienvenue à la Partie III de **Apprendre Node.js avec Brigadier Fluffykins**, une série créée pour vous aider à comprendre facilement Node.js [1m[31m❤️[0m

Dans la [Partie II](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-ii-events-eventemitter-the-event-loop-6d4c139694fb#.gmus13l0y), Brigadier Fluffykins et moi vous avons expliqué comment Node.js est un langage piloté par événements. Vous avez appris pourquoi cela est important pour le comportement asynchrone, et comment ces événements sont traités via la _Boucle d'Événements_. Vous avez également appris comment les événements DOM et les événements dans Node.js sont similaires. Enfin, nous avons créé notre premier _EventEmitter_.

Passons à la leçon suivante ! OH OUI !!

![Image](https://cdn-media-1.freecodecamp.org/images/1*FdYBKFCqeQDsc1IHEtAGhw.gif)

Aujourd'hui, nous allons apprendre :

* Les types de méthodes de requête
* L'_Objet Request_
* Configurer plusieurs routes
* La différence entre _setHeader_ et _writeHead_
* Comment servir des fichiers (HTML, CSS, etc.)

#### Types de Méthodes de Requête

Les quatre principales requêtes HTTP :

* GET — Utilisé lorsque le client demande des données. Par exemple, lorsqu'il demande à voir votre page d'accueil, il aura besoin des documents HTML, CSS et JavaScript. Ce sont toutes des requêtes GET.
* POST — Utilisé lorsque le client soumet des données au serveur ou à une base de données. Par exemple, soumettre un formulaire.
* PUT — Similaire à POST, mais peu utilisé. Utilisez cela lorsque vous modifiez quelque chose à une URL spécifique ou mettez à jour une ressource sur le serveur. La principale différence est que PUT est [idempotent](http://stackoverflow.com/questions/630453/put-vs-post-in-rest).
* DELETE — Supprime la ressource spécifiée.

Les requêtes GET et POST sont les plus utilisées. PUT et DELETE ne sont pas autant utilisés. Ensuite, il y a des requêtes telles que HEAD, OPTIONS et CONNECT. Celles-ci sont encore moins utilisées, mais il est bon de les connaître au cas où.

Puisque GET et POST sont les plus courants, nous allons les passer en revue. La requête GET sera discutée aujourd'hui, tandis que nous discuterons de la méthode POST dans la prochaine leçon, car cela aura plus de sens alors.

#### L'Objet Request

Lorsque nous configurons notre serveur, nous voulons que l'événement _request_ écoute toute requête entrante du client. Il est important de se rappeler que cela n'est pas la même chose que l'_objet request_ dans un callback. De plus, les objets request et response _ressemblent à_ des paramètres, et vous pouvez même changer leurs noms — comme je l'ai fait dans l'exemple ci-dessous de 'request' à 'req' et de 'response' à 'res' — mais ce sont toujours des objets. Gardez cela à l'esprit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*a1j4lLcOjTlgqVAj3ygdXw.png)

L'_objet request_ est énorme avec de nombreuses propriétés, fonctions et méthodes différentes. Essayons d'imprimer l'_objet request_ dans votre terminal. Ouvrez le fichier _server.js_ dans le dossier [_nodestory2_](https://drive.google.com/open?id=0Byvu31DWppA7RVVHUEtRWkotbHM). Tous les fichiers dont vous avez besoin pour le reste de cette leçon se trouvent ici.

Avant de continuer, Brigadier Fluffykins et moi voulons que vous sachiez :

Si vous vous sentez submergé par la quantité de code dans le dossier [zip](https://drive.google.com/open?id=0Byvu31DWppA7RVVHUEtRWkotbHM), surtout le fichier _server.js_ — je sais que j'ai été submergé lorsque j'ai commencé à apprendre Node.js — prenez simplement une pause et sachez que nous sommes là pour vous. Nous allons vous guider à travers chaque section, étape par étape. Prenez tout le temps dont vous avez besoin.

La persévérance est la clé du progrès en programmation, et dans la vie. De plus, sauvegardez constamment votre fichier et redémarrez le serveur si vous avez apporté des modifications au fichier. Bonne chance ! :)

Vous pouvez également créer votre propre fichier avec le même nom — _server.js_ — et copier-coller ceci :

Félicitations si vous savez quoi faire ensuite.

Localisez votre fichier _server.js_ ou le dossier [_nodestory2_](https://drive.google.com/open?id=0Byvu31DWppA7RVVHUEtRWkotbHM) que vous avez téléchargé. Dans l'exemple ci-dessous, je suis allé sur mon bureau, puis dans le dossier _nodestory2_, puis dans ce dossier se trouvait le fichier _server.js_.

Tapez _node server.js_ dans le shell, allez à _http://localhost:3000/_, et vous devriez voir l'_objet request_ dans votre shell :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LVsgnT7vovdl2G-Cn8RcUg.png)

La capture d'écran ci-dessus est après avoir fait défiler jusqu'au début.

C'est énorme, n'est-ce pas ?

L'_objet request_ est une instance de l'_objet IncomingMessage_. Vous pouvez en lire plus à ce sujet [ici](https://nodejs.org/api/http.html#http_class_http_incomingmessage) si vous êtes intéressé.

Tout au long de cette série, nous discuterons des propriétés les plus couramment utilisées de l'_objet request_, surtout puisque vous n'utiliserez probablement qu'une poignée d'entre elles dans vos projets.

Les propriétés _url_ et _method_ sont deux propriétés qui fonctionnent souvent ensemble. Lorsque nous configurons notre serveur et avons ces deux propriétés, nous disons « Hé serveur, si tu vois que le client vient de _cette URL_ et _qu'il veut des informations en retour_ (méthode GET), alors déclenche le callback ».

Lorsque vous imprimez les propriétés _url_ et _method_ de l'_objet request_, que obtenez-vous ? Commentez l'ÉTAPE #2 et décommentez l'ÉTAPE #2.1. Ou copiez et collez ceci dans votre fichier _server.js_ :

Rappelez-vous, comme je l'ai mentionné dans la [Partie I](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b), chaque fois que vous apportez des modifications à l'intérieur d'un fichier serveur, vous devez redémarrer le serveur pour qu'il fonctionne correctement. Pour arrêter le serveur manuellement, allez dans votre terminal et appuyez sur _control + C_ pour Mac (à nouveau, je crois que c'est _killall node_ pour Windows).

Maintenant, tapez _node server.js_ dans le shell pour démarrer le serveur, puis allez à _http://localhost:3000/_, et vous devriez voir quelque chose comme ceci dans votre shell :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pbM-TX_6zJsnviO4UfHzkQ.png)

L'URL de la requête a imprimé '/'. Il s'agit de l'URL d'où vient le client, dans ce cas, la page d'accueil — également appelée le 'répertoire racine'. Et la méthode de requête a imprimé 'GET', ce qui signifie que le client voulait voir ou _obtenir_ les fichiers nécessaires pour la page.

Si vous obtenez une deuxième requête GET, il s'agit probablement du favicon dans votre navigateur qui est automatiquement demandé par [défaut](http://stackoverflow.com/questions/9746769/why-is-there-an-additional-favicon-ico-http-request).

La méthode _headers_ est également assez utile, car elle nous donne des informations sur l'origine de la requête. Cela inclut les informations de navigation, les cookies, et plus encore.

Essayons d'imprimer les en-têtes et d'en accéder à un. Soyez conscient qu'il s'agit d'un objet de paires clé-valeur. Décommentez l'ÉTAPE #2.2 et commentez l'ÉTAPE #2.1 ou copiez et collez ceci dans votre fichier _server.js_ :

Redémarrez le serveur. Vous devriez obtenir un objet d'en-têtes dans votre shell.

Si vous obtenez deux objets, encore une fois, probablement ce favicon, et ainsi un deuxième objet d'en-tête a été imprimé, ignorez-le pour l'instant.

Il est important de noter que si vous recevez des en-têtes qui ont le même nom, ils seront soit écrasés, soit présentés sous forme de chaîne séparée par des virgules, selon le type d'en-tête.

Si vous voulez vraiment les en-têtes exacts qui existent — même s'ils ont les mêmes noms (peut-être parce que vous avez besoin de leurs différentes valeurs) — vous pouvez utiliser la méthode _rawHeaders_. Vous entreriez donc _req.rawHeaders_ au lieu de _req.headers_.

Essayez-le ! Voyez ce que vous obtenez :)

#### Configurer Plusieurs Routes

Cette URL : _/_ signifie la page d'accueil. Pour accéder à une page différente, nous créons une nouvelle requête GET avec un nom différent après le slash.

Passons en revue tout ce que nous avons appris jusqu'à présent et créons deux requêtes GET — une si le client demande la page d'accueil et une autre s'il demande la page _/blueberries_. Pourquoi des myrtilles ? Cela n'a en fait pas d'importance. Si vous savez que le client va aller sur _www.votrepage.com/blueberries_, alors vous savez que vous devez créer une requête dans votre serveur pour _/blueberries_ afin que lorsqu'il tape ce chemin d'URL, il verra du contenu au lieu d'un message d'erreur.

La vérité est que Brigadier Fluffykins a démontré ses compétences de ninja et en paiement, j'ai dû choisir ce chemin d'URL :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZvI7nw1ZJI912s6CQXqDjQ.jpeg)
_Brigadier Fluffykins utilisant son légendaire mouvement 'push-bite' sur le pauvre chat du quartier._

Sinon, cela n'aurait en fait pas d'importance. Continuons :

Commentez l'ÉTAPE #2.2 et décommentez l'ÉTAPE #2.3 ou copiez et collez ceci dans votre fichier _server.js_. N'oubliez pas de sauvegarder après :

Maintenant, redémarrez le serveur et allez à _http://localhost:3000/_, vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JuRtCjW0OPbKETCxJw35GQ.png)
_Un parent éloigné de Brigadier Fluffykins, Matilda._

D'accord, maintenant essayons l'autre requête que nous avons configurée. Allez à _http://localhost:3000/blueberries_. Vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-tvN0KLeHT6myhGmJs7dGw.png)

Voyez-vous ce qui s'est passé là ? Nous pouvons changer _/blueberries_ en ce que nous voulons, tant que nous configurons ce que le client devrait voir. Donc si vous alliez à [_http://localhost:3000/something_](http://localhost:3000/something) ou [_http://localhost:3000/somethingelse_,](http://localhost:3000/somethingelse,) cela ne fonctionnerait pas à moins que nous créions des réponses pour ces requêtes dans notre serveur.

Démontrons cela en changeant une ligne dans notre code. Changez cette ligne :

```
if (req.url === '/blueberries') {
```

En ceci :

```
if (req.url === '/carrots') {
```

Sauvegardez et redémarrez votre serveur. Maintenant, allez à : _http://localhost:3000/blueberries_

Voyez-vous comment cela ne fonctionne plus ? Allez à _http://localhost:3000/carrots_

Cela devrait fonctionner maintenant car nous avons une réponse configurée pour le chemin _/carrots_, tandis que le chemin pour _/blueberries_ n'existe plus (sauf si nous choisissons de le créer).

#### La différence entre setHeader et writeHead

La méthode _setHeader_ prend un nom comme premier paramètre, et une valeur pour le second. Vous pouvez appeler cette méthode plusieurs fois dans la même requête, mais assurez-vous de ne pas inclure de caractères invalides ou vous recevrez une erreur — spécifiquement, une _TypeError_.

Essayons cela, changez votre requête de page d'accueil en ceci :

Sauvegardez et redémarrez le serveur.

Vous devriez voir les nouveaux en-têtes sur la page d'accueil dans votre onglet Réseau.

Pour accéder à votre onglet Réseau, cliquez avec le bouton droit → inspecter → choisissez l'onglet Réseau (dans la même rangée que Console).

Ou sur un mac : Cmd + Option + J → onglet Réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8TgYfEaQaxiJ58Lh9tezhA.png)

Ce n'est pas particulièrement utile de définir des en-têtes aléatoires, mais si vous travaillez avec l'authentification ou les cookies dans le navigateur, _setHeader_ fait partie de ce processus.

Dans notre [dernière leçon](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b), nous avons défini l'en-tête via la méthode _writeHead_. Là, nous avons défini le code de statut. La différence entre _setHeader_ et _writeHead_ est que _setHeader_ définit un en-tête à la fois, et vous pouvez utiliser autant de méthodes _setHeader_ que vous avez besoin avant d'envoyer la réponse.

D'autre part, _writeHead_ peut définir le code de statut (premier paramètre), et plusieurs en-têtes à l'intérieur d'un objet (le deuxième paramètre) en même temps.

Définir le code de statut manuellement aide à garantir que la page se chargera correctement. Si vous incluez _setHeader_ et _writeHead_ dans la même requête, ils fusionneront avec _writeHead_ prenant le dessus. Cela signifie également que tout en-tête avec le même nom dans _setHeader_ et _writeHead_ sera écrasé par les en-têtes de _writeHead_.

#### Comment Servir des Fichiers

Avez-vous remarqué comment nos réponses n'ont été que des mots simples et du HTML basique ? En tant que développeur, vous servirez souvent des documents réels, alors apprenons à le faire !

Soit collez ceci dans votre _server.js_ ou décommentez l'ÉTAPE #2.4 et commentez l'ÉTAPE #2.3. Pouvez-vous deviner ce qui se passe ici ?

Ceci devrait être dans votre fichier _index.html_ :

[1m[31m...[0m et ce petit extrait devrait être dans votre fichier _style.css_ :

```
.see-me { background-color: black;}
```

Jetez un coup d'œil au code dans _server.js_ à l'ÉTAPE #2.4. Lisez les commentaires du code et voyez si vous pouvez comprendre ce qui se passe avant de continuer.

_readFile_ est une méthode du _système de fichiers_, l'un des modules principaux de Node.js, que nous avons brièvement couvert dans la [Partie I](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b). Et c'est pourquoi nous avons requis ce module dans notre code et l'avons stocké dans la variable _fs_. Il lira le fichier de manière asynchrone et déclenchera le callback. Lorsque le callback est déclenché, le fichier est à l'intérieur. Donc la prochaine chose que nous avons faite a été de l'envoyer au client en utilisant la méthode _end_.

Vous pouvez également envoyer des fichiers _.js_ — et même du _JSON_ — n'oubliez simplement pas de définir les en-têtes _Content-Type_ pour éviter les erreurs. Par exemple, pour un fichier _.js_, le _Content-Type_ doit être défini sur _application/javascript_. Ceux-ci sont également connus sous le nom de types MIME.

___dirname_ signifie essentiellement le répertoire actuel du fichier _server.js_. Plus sur les chemins, les modules et les bibliothèques dans la prochaine leçon !

Avez-vous remarqué comment nous avons configuré la requête pour le _style.css_ ?

Pourquoi pensez-vous que nous devons faire cela ?

Très probablement, le client ne tapera pas _votresite.com/style.css_. Le client veut simplement que votre _style.css_ soit automatiquement présent afin que votre page HTML ait une belle apparence, n'est-ce pas ? Vous pourriez le tester et visiter _localhost:3000/style.css_ et vous le verrez là, mais comment l'obtenir envoyé au client automatiquement ?

Vous vous souvenez probablement de la création de pages HTML et de l'inclusion de votre CSS dans un fichier différent. Pour que ce CSS fonctionne, nous devions inclure la balise de _lien_ CSS à l'intérieur de la page html. Nous l'avons déjà fait dans _index.html_ :

```
<link rel="stylesheet" href="style.css">
```

Ainsi, lorsque le client demande la page _index.html_, le serveur analysera le code à l'intérieur de _index.html_ pour toute autre balise importante telle que la balise _link_ (fichiers CSS) ou _script_ (fichiers JavaScript).

Dans notre cas, nous n'avons inclus que la page CSS. Il trouvera cette balise _link_ et cela revient essentiellement à envoyer une requête GET automatique. En gros, les serveurs sont comme :

« Hé, regardez, le client veut la page HTML ! D'accord, laissez-moi vérifier si cette page HTML a autre chose que je dois envoyer. Oh, regardez, une balise _link_ pour le fichier _style.css_ ! Cela doit signifier qu'il y a une page css pour cette page html. D'accord, retournons dans mon fichier _server.js_. Oui ! J'ai une _réponse_ pour ce fichier CSS aussi, donc je servirai à la fois le fichier HTML et les fichiers CSS ! »

Si vous visitez la page d'accueil maintenant et ouvrez l'onglet Réseau, vous devriez voir le CSS fonctionner correctement. Si vous ne le voyez pas immédiatement, actualisez le navigateur. Et si vous ne le voyez toujours pas, assurez-vous d'avoir sauvegardé le fichier et redémarré le serveur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjZkTEtCCsjPpa1oN8ZHNA.png)

Sinon, si nous n'avions pas configuré la requête _style.css_ dans notre _server.js_, seule la page HTML serait envoyée et nous verrions une erreur dans notre onglet réseau pour la page _style.css_.

Nous pouvons également rencontrer des temps de chargement anormalement longs car le serveur recherche la configuration du _style.css_. Il penserait :

« Je vois que le fichier HTML a une balise _link_ mais je ne peux pas trouver de _réponse_ pour ce fichier CSS dans _server.js_. Je ne comprends pas. Où est-il ? Où est-il ? »

Et j'aimerais conclure la leçon d'aujourd'hui avec un petit truc astucieux. Cela peut sembler intimidant au premier abord, surtout si c'est la première fois que vous voyez des _regex_. Je voulais simplement partager ce snippet pratique avec vous au cas où, dans un avenir proche, vous configureriez une application et que tout ce dont elle a besoin est de servir des fichiers qui se terminent par _.js, .html, ou .css._ au lieu d'écrire plusieurs requêtes.

Ce n'est pas grave si vous ne le comprenez pas tout de suite — sauvegardez-le pour plus tard et revenez-y lorsque vous serez prêt ! C'est bien de l'avoir dans votre poche :)

```
if (request.url.match(/.js$|.html$|.css$/)) {  return response.end(fs.readFileSync(__dirname + '/..' +   request.url));}
```

#### Consultez ces ressources supplémentaires

* L'_objet response_ a certaines propriétés similaires à l'_objet request_, mais tandis que l'_objet request_ hérite de l'_objet IncomingMessage_, l'_objet response_ hérite de l'[_objet http.ServerResponse_](https://nodejs.org/api/http.html#http_class_http_serverresponse).
* En savoir plus sur les en-têtes [ici](https://nodejs.org/api/http.html#http_http).
* [Revoir les Types de Requêtes](http://www.w3schools.com/tags/ref_httpmethods.asp)

Félicitations ! Vous avez réussi à suivre **Apprendre Node.js avec Brigadier Fluffykins** Partie III ! Vous avez appris les différents types de requêtes, comment configurer des requêtes GET à différentes URL, et comment servir des fichiers !

En plus de tout cela, vous devriez maintenant avoir une compréhension de base de l'_objet request_, et quelques méthodes utiles ! Bon travail aujourd'hui !

Nous en apprendrons plus sur ces sujets ainsi que sur d'autres que nous n'avons fait qu'effleurer dans les prochaines leçons. Merci d'avoir lu et restez à l'écoute.

Gardez votre sagesse à jour en cliquant sur le ❤️ ci-dessous et en suivant, car plus de **Apprendre Node.js avec Brigadier Fluffykins** arrive bientôt sur Medium !

[**Partie I : Sync, Async, et Créer Votre Premier Serveur !**](https://medium.com/free-code-camp/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.t91sbbaru)

[**Partie II : Événements, EventEmitter & Event Loop**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-ii-events-eventemitter-the-event-loop-6d4c139694fb#.2rg8m7uen)

[**Partie III : Objet Request, Configurer les Routes, Servir des Fichiers**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-iii-request-object-configure-routes-serve-files-7666f783dc10#.t36ij32rf)