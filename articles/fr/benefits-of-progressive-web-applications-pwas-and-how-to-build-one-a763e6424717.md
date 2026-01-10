---
title: Pourquoi les Progressive Web Apps sont géniales et comment en créer une
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T11:27:32.000Z'
originalURL: https://freecodecamp.org/news/benefits-of-progressive-web-applications-pwas-and-how-to-build-one-a763e6424717
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-2ZTTSgoVBaDoT9s24Bhxg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: PWA
  slug: pwa
- name: React
  slug: reactjs
- name: technology
  slug: technology
seo_title: Pourquoi les Progressive Web Apps sont géniales et comment en créer une
seo_desc: 'By Ankita Masand

  In this tutorial, we’re going to build up the fundamentals of Progressive Web Applications
  (PWAs). I’ll help you understand the pain points of the traditional web and the
  need for something better to combat native applications. We’ll...'
---

Par Ankita Masand

Dans ce tutoriel, nous allons construire les bases des Progressive Web Applications (PWA). Je vais vous aider à comprendre les points de douleur du web traditionnel et le besoin de quelque chose de mieux pour combattre les applications natives. Nous allons plonger plus profondément dans les composants qui constituent une PWA — _Service Workers_, _IndexedDB_, _manifest.json_ et _Web Push Notifications_. Et la partie la plus intéressante — nous allons construire une PWA à partir de zéro.

### Comment j'ai eu l'idée d'écrire ce tutoriel

Je dînais avec toute ma famille, et une notification pour un nouveau message texte est apparue sur mon téléphone portable. Le message confirmant que j'avais reçu une nouvelle paie. Bien que ce soit une nouvelle régulière, ma famille est ravie chaque fois que cela se produit.

Profitant de l'environnement agréable, mon frère a déclaré qu'il voulait un nouveau téléphone portable. Lorsque je lui ai demandé pourquoi il en avait besoin, il a dit que son téléphone était devenu très lent et qu'il recevait des avertissements de mémoire faible de temps en temps. J'ai été surpris d'entendre cela car son téléphone est plus avancé que le mien qui fonctionne encore parfaitement bien.

Pour satisfaire ma curiosité, j'ai vérifié son téléphone et j'ai trouvé qu'il avait installé plus de 40 applications pour ses divers besoins. 👩‍💻 Il y avait deux applications pour lire des blogs sur différentes catégories, deux pour obtenir des mises à jour d'actualités, trois étaient des applications de commerce électronique, trois pour les jeux, une pour surveiller ses fonds communs de placement et une autre pour gérer ses transactions bancaires et il y en avait quelques autres qu'il n'utilisait pas fréquemment.

Je lui ai demandé s'il avait déjà essayé d'aller sur le site web respectif avant de prendre la décision audacieuse d'installer l'application native. Il a mis de côté sa part de pizza et s'est tourné vers moi dans une humeur de conversation détaillée.

Il a commencé par dire qu'il avait toujours visité un site web en premier et que c'est le site web qui le force à télécharger l'application native en affichant des bannières d'installation grasses. Il dit que l'expérience sur le web est si frustrante qu'il est impossible de réaliser même une tâche simple.

Ses applications de commerce électronique sont vraiment excellentes pour lui donner des mises à jour en temps opportun sur ses commandes et font un travail incroyable en l'informant des réductions en envoyant des _notifications push_. L'expérience utilisateur sur les applications natives est tout simplement incroyable et le _web_ ne peut pas battre cela. Il était ferme dans son opinion sur le web. Cependant, il a convenu que la taille de l'application native alourdit la mémoire de son téléphone mais qu'il ne peut rien faire à ce sujet.

### Idées fausses que les gens ont sur le web

Mon frère pense exactement ce que la plupart des utilisateurs pensent du web. Le web traditionnel est lent et laid. Prenons un moment et consultons [Twitter sur le web mobile](https://mobile.twitter.com/), communément appelé Twitter Lite, et comprenons la signification du mot _traditionnel_ dans ma dernière déclaration.

![Image](https://cdn-media-1.freecodecamp.org/images/0*r3OZzl5HrTeyTTaw.gif)

L'expérience est-elle à la hauteur de l'application native ? _Il se charge instantanément. Il n'y a pas de défilement saccadé. Cela ne ressemble pas à un vieux site web traditionnel_. Vous avez peut-être remarqué une petite bannière en bas vous demandant d'_Ajouter Twitter_ à votre écran d'accueil. Est-ce une manière plus élégante d'inciter les utilisateurs à installer des applications natives ? Non, ce n'est pas le cas. Cela ne téléchargera pas une application native de plusieurs mégaoctets. Cela vous demande d'ajouter Twitter Lite sur votre écran d'accueil. Cela signifie littéralement ajouter un raccourci pour accéder à Twitter mobile web en utilisant cette icône sur l'écran d'accueil.

Expérimentons cela en cliquant sur _Ajouter Twitter à l'écran d'accueil_ et découvrons ce que le nouveau web a à offrir. Au cas où la bannière n'apparaîtrait pas dans votre cas, veuillez cliquer sur les trois points du côté droit et choisir l'option _Ajouter à l'écran d'accueil_. Maintenant, cliquez sur l'icône Twitter de votre écran d'accueil. N'est-ce pas incroyable ? Oh oui, cette application peut également vous envoyer des notifications push en temps réel. Le web ne semblera plus un monde perdu maintenant. Une fois que vous avez opté pour les notifications push sur une application web, elle fait un excellent travail pour engager les utilisateurs en leur montrant toutes les mises à jour.

Il y a une autre chose importante qui manque dans le vieux web traditionnel — la capacité à gérer une connexion internet intermittente ou inexistante. Le Web se comporte assez différemment sur les appareils 2G par rapport au WIFI. La plupart du temps, il n'y a rien ou un chargeur à l'écran lors de la navigation sur une connexion 2G. Cela est frustrant pour l'utilisateur final.

La bonne nouvelle est que le web moderne peut également gérer ce problème. Vous ne voyez pas le dinosaure lorsque votre internet est coupé. C'est une belle coque d'application qui apparaît lorsque vous n'êtes pas connecté à internet. J'aime vraiment la façon dont [Trivago](https://www.trivago.in/) gère ce problème, ils montrent une belle coque d'application pour jouer autour d'un labyrinthe hors ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1q--_3sLKx0l8Hz2.png)

Vérifions une autre application de ce type — [Financial Times](https://app.ft.com/). Chargez [Financial Times](https://app.ft.com/) dans votre navigateur et éteignez maintenant votre internet. Rechargez la page. L'expérience est toujours la même. N'est-ce pas quelque chose qui rend le web génial ? Ces applications web qui résolvent les points de douleur du web traditionnel sont communément appelées **Progressive Web Applications**.

Dans ce tutoriel, nous allons explorer les Progressive Web Applications et également en construire une à partir de zéro.

### Avantages des Progressive Web Applications

Les Progressive Web Applications (PWA) sont :

#### Rapides

Elles utilisent bien les caches locaux pour stocker les actifs statiques. La mise en cache des actifs statiques réduit le nombre de requêtes au serveur pour récupérer ces actifs à chaque chargement. Cela offre une expérience utilisateur incroyable similaire à celle des applications natives. Elles répondent rapidement aux interactions des utilisateurs.

#### Fiables

Les PWA chargent les données presque instantanément. Chaque requête réseau de récupération de l'application passe par les Service Workers (plus sur cela plus tard). Ils exploitent le cache (IndexedDB ou tout autre cache local). Les Service Workers peuvent envoyer la réponse à une requête réseau directement depuis le cache en cas de connexions internet intermittentes ou lentes. Les PWA fonctionnent de manière fiable même sur les connexions 2G.

#### Engageantes

Les applications natives exploitent la puissance des systèmes d'exploitation pour montrer des notifications importantes aux utilisateurs et c'est l'une des fonctionnalités puissantes d'une application. L'envoi de notifications push en temps opportun aide à retenir les utilisateurs pendant une durée plus longue. Les PWA utilisent les notifications push web pour informer les utilisateurs des mises à jour pertinentes.

_Progressive Web Applications_ est utilisé comme terminologie pour les applications web qui sont rapides, fiables et engageantes et elles fournissent une expérience similaire à celle des applications natives. Les applications qui sont éligibles pour être appelées Progressive Web Applications consistent et emploient les éléments suivants :

**Service Workers**

Les _Service Workers_, en termes simples, sont quelques lignes de code JavaScript qui continuent de s'exécuter en arrière-plan. Cependant, ils passent à un état dormant lorsqu'ils ne sont pas utilisés. Ils fonctionnent comme un système piloté par événements. Chaque fois qu'un événement particulier (par exemple, une requête de récupération au serveur) est invoqué, les service workers s'activent.

Nous pouvons gérer la `réponse` de l'événement `fetch` en utilisant l'écouteur d'événement fetch dans le Service Worker. Pour qu'un service worker commence à faire son travail de gestion des requêtes fetch et de quelques autres événements, il doit être enregistré, installé et activé sur une application web.

**IndexedDB ou tout autre cache local**

Les PWA stockent les actifs statiques comme les fichiers JavaScript, les feuilles de style et les images dans le cache local pour les visites ultérieures. Certaines des PWA utilisent IndexedDB, qui est essentiellement une structure de données de paires clé-valeur structurées. IndexedDB est utilisé pour stocker de grandes quantités de données par rapport à d'autres options de stockage côté client.

Nous avons vu précédemment la manière dont [Financial Times](https://app.ft.com/) gère la _condition sans internet_. Il affiche toujours tous les articles sur la page d'accueil. Il utilise IndexedDB pour stocker les données de ces articles.

Vérifions cela en action. Vous trouverez IndexedDB dans les Chrome DevTools sous l'onglet Applications. Sous IndexedDB, allez à la section _Articles_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*T9BnTEug5M96NXiV.png)

**Notifications Push Web**

Les Service Workers écoutent également un événement push et ont un gestionnaire d'événements push respectif qui prend en charge l'affichage de la notification push à l'utilisateur. Une application doit avoir la permission de l'utilisateur pour lui montrer des notifications push. Une fois qu'un utilisateur opte pour recevoir des notifications push, le navigateur génère un jeton unique pour lui. Le serveur peut alors communiquer avec l'utilisateur en utilisant ce jeton unique.

**Fichier manifest.json**

manifest.json est typiquement un fichier de métadonnées d'une application. Une application inclut le manifest.json dans index.html comme suit

`<link rel="manifest" href="manifest.json">`

manifest.json fait le travail de dire au navigateur que l'application est une PWA. Il indique au navigateur le Nom, la Couleur de Fond, la Couleur du Thème et les Icônes à utiliser pour cette application. Il indique également le mode dans lequel l'application doit être ouverte. Par exemple, un _mode autonome_ lance une PWA en donnant une sensation similaire à celle d'une application native.

**Expérience Utilisateur Riche**

Les PWA sont connues pour avoir une expérience utilisateur riche. Elles accèdent aux actifs statiques directement depuis le cache, il n'y a donc aucun retard dans la réponse aux interactions des utilisateurs.

Construisons une Progressive Web Application en utilisant les composants listés ci-dessus.

### Cas d'utilisation — Construire un trésor de livres

Nous allons construire une application appelée _BooksKeep_. Elle aidera à maintenir un enregistrement systématique des livres que nous avons lus et aussi de ceux qui sont dans notre pipeline. _Aucun mot sage appris ne devrait être vain_.

Les fonctionnalités suivantes seront incorporées dans cette application :

1. Afficher une liste de livres (Titre, Auteur, Résumé et Citations Favorites)
2. Ajouter un nouveau livre à la liste

![Image](https://cdn-media-1.freecodecamp.org/images/0*YqPX754vSe8ea8iP.gif)

#### Prérequis — Notre pile technologique

* _React_ — pour construire le front-end
* _IndexedDB_ — pour stocker les enregistrements de livres (veuillez noter, il n'y a pas de base de données back-end)
* _WebPack_ — comme serveur de développement et pour bundler les actifs

Commençons ! Pour simplifier les choses, j'ai créé un [modèle de base](https://github.com/ankita1910/bookskeep-pwa/tree/master/boilerplate) pour commencer.

#### Comprendre le modèle de base

`package.json` - `package.json` contient les dépendances du projet. Lorsque vous faites `npm install`, ces dépendances seront téléchargées dans votre système. Puisque nous utilisons React pour construire notre front-end, les bibliothèques `react` et `react-dom` sont incluses dans la section des dépendances.

Dans l'objet `devDependencies`, les présets babel et quelques plugins liés à webpack sont inclus. [Babel](https://babeljs.io/) est un compilateur JavaScript qui est utilisé pour la transformation de syntaxe, convertissant le JavaScript de nouvelle génération en une version compatible avec le navigateur.

Le navigateur ne comprend pas directement la syntaxe React, donc nous utilisons `babel-preset-react` pour convertir React et JSX en JavaScript que le navigateur comprend. Nous utilisons [WebPack](https://webpack.js.org/) comme bundler de modules.

`webpack.config.js` contient la configuration requise pour générer un bundle d'actifs statiques. L'objet `entry` dans `module.exports` contient le point d'entrée de l'application, qui dans notre cas est `app.js`. Webpack génère un graphe de dépendances en utilisant ce point d'entrée et continue d'ajouter des dépendances dans le bundle en commençant par `app.js`. L'objet `output` contient le chemin du dossier de sortie et `filename` génère des noms de fichiers dynamiques basés sur leur valeur dans l'objet d'entrée. Dans notre cas, ce sera `bundle.js` comme nous avons mentionné bundle dans le point d'entrée.

Ensuite, il y a quelques règles pour convertir les fichiers .js et .scss spécifiques. Ces fichiers doivent être transformés avec leurs chargeurs respectifs avant de les ajouter au bundle principal.

* [HTMLWebpackPlugin](https://webpack.js.org/plugins/html-webpack-plugin/) ajoute les bundles de sortie générés dans le modèle `index.html` fourni.
* [ExtractTextPlugin](https://github.com/webpack-contrib/extract-text-webpack-plugin) déplace les modules .css dans un fichier séparé.
* CopyWebpackPlugin copie simplement le fichier `manifest.json` et le fichier `service-worker.js` de `src` vers `dist`.

Nous allons construire `src` tout au long de ce tutoriel. Pour l'instant, il contient `index.html` qui a un élément div avec l'id `app`. `app.js` est le composant racine de l'application. Il contient des composants d'en-tête et de corps simples pour l'instant.

Commençons à construire notre _BooksKeep PWA_. Nous allons construire cela progressivement dans les étapes suivantes :

1. Construire un composant de tableau pour afficher les enregistrements de livres
2. Prévoir l'ajout d'un nouveau livre dans le tableau
3. Stocker les enregistrements de livres dans IndexedDB
4. Ajouter un Service Worker pour mettre en cache les actifs statiques
5. Ajouter manifest.json

### Construire un composant de tableau pour afficher les enregistrements de livres

Nous utilisons `react-bootstrap` pour construire l'interface utilisateur. Importons le composant Table de `react-bootstrap`.

Démarrez le serveur en utilisant la commande `npm start` dans votre terminal. Dirigez-vous vers `localhost:8080/dist/`. Nous n'avons pas encore d'enregistrements de livres, donc le tableau est vide. `BooksHeaders` est importé du dossier constants. Veuillez ajouter `BooksHeaders` dans le fichier `books-headers.js` dans le dossier constants à partir d'[ici](https://github.com/ankita1910/bookskeep-pwa/blob/master/app/src/js/constants/books-headers.js).

`BooksHeaders` est simplement un tableau d'objets que nous affichons dans le tableau. La fonction `getTableMarkup` construit les en-têtes du tableau avec les fonctions `getTableHeaders` et le corps avec les fonctions `getTableData`. `booksData` maintient l'état du composant. Si un nouvel enregistrement de livre doit être ajouté, il doit être poussé dans le tableau `booksData`.

### Prévoir l'ajout d'un nouveau livre dans le tableau

Allons plus loin et ajoutons notre premier enregistrement de livre dans le tableau. Tout ce que nous avons à ajouter est d'importer le composant `BookForm` du dossier de base et de lui fournir une prop `onSubmit`. La prop `onSubmit` accepte une fonction qui sera appelée lorsque l'utilisateur clique sur le bouton de soumission dans le formulaire, et cela nous donnera les détails du nouveau livre. Une fois que vous avez terminé, votre composant Body devrait ressembler à [celui-ci](https://github.com/ankita1910/bookskeep-pwa/blob/master/mid-steps/body-1.js).

Voici le composant `BookForm` :

`FieldGroup` est simplement un wrapper pour les entrées étiquetées. Veuillez mettre [ceci](https://github.com/ankita1910/bookskeep-pwa/blob/master/app/src/js/utils/field-group.js) dans le fichier `field-group.js` dans le dossier `utils`. Le composant `BookForm` maintient son état dans l'objet `formData`. Chaque fois qu'un utilisateur entre un nom, un auteur ou un résumé, il est enregistré dans l'état du composant. Le bouton de soumission transmet l'état du composant au composant parent Body, qui l'ajoute ensuite à son état - le tableau `booksData`.

Après avoir ajouté un enregistrement de livre, vous verrez que votre tableau est maintenant peuplé avec cet enregistrement. Mais lorsque vous actualisez la page, tout cela disparaît. Nous devons corriger cela.

### Stocker les enregistrements de livres dans IndexedDB

_IndexedDB_ est une base de données de stockage structurée côté client. Les enregistrements dans IndexedDB sont stockés sous forme de paires clé-valeur. Nous allons sauvegarder les enregistrements de livres dans IndexedDB. IndexedDB fournit des API pour ajouter, supprimer et mettre à jour les enregistrements dans une base de données. Explorons ces API en créant un wrapper dans le fichier `indexeddb.js` dans le dossier `utils`.

Les opérations effectuées sur IndexedDB sont asynchrones par nature. Ainsi, les API IndexedDB fournissent des hooks appropriés pour les événements de succès et d'erreur.

Tout d'abord, nous devons créer notre base de données. Écrivons une fonction `initialize` qui gérera les tâches d'initialisation :

Dans l'extrait de code ci-dessus, `BooksKeep` est le nom de la base de données IndexedDB et `books` est un _ObjectStore_. _ObjectStore_ est analogue à une table en SQL. L'instruction `idb.open(DB, 1)` est une requête asynchrone pour ouvrir la base de données IndexedDB `BooksKeep`, et le deuxième paramètre 1 signifie la version de la base de données. La variable request est de type `[IDBOpenDBRequest](https://developer.mozilla.org/en-US/docs/Web/API/IDBOpenDBRequest)`.

Nous avons défini les fonctions `onsuccess`, `onerror` et `onupgradeneeded` sur l'objet request pour être appelées aux événements respectifs. Par exemple, le callback `onsuccess` serait appelé lorsque la base de données est ouverte avec succès et dans la méthode `onsuccess`, nous mettons en cache l'instance de la base de données `BooksKeep`. La méthode `onupgradeneeded` est invoquée chaque fois qu'il y a un changement dans la version de la base de données.

Actuellement, avec la version 1, nous n'avons ajouté qu'un seul ObjectStore appelé `books`. Supposons, à un stade ultérieur, lorsque notre application se développe, nous décidons d'ajouter un autre ObjectStore. Nous devrons mettre à niveau la version de notre base de données à 2 et ajouter le schéma de ce nouvel ObjectStore dans la méthode `onupgradeneeded`.

Nous allons écrire trois méthodes importantes — _get_, _update_ et _delete_ — dans notre wrapper IndexedDB. L'idée générale pour effectuer l'une de ces opérations est d'abord d'obtenir l'instance du magasin, d'envelopper l'opération dans une transaction, puis d'écrire les gestionnaires d'événements de succès et d'erreur pour les requêtes asynchrones respectives. Une transaction est simplement un wrapper autour d'une opération pour garantir l'intégrité des données. Si l'une des actions dans une transaction échoue, alors aucune action n'est effectuée sur la base de données.

Par exemple, notre méthode put ou update ressemblera à ceci :

La méthode `update` prend trois paramètres :

`type` est le nom de l'objectStore, `data` est l'enregistrement du livre que nous avons l'intention d'ajouter/mettre à jour dans notre objectStore, et `callback` est de type fonction qui serait appelée après avoir ajouté avec succès `data` dans l'objectStore.

`transaction` est définie sur l'instance `[IDBOpenDBRequest](https://developer.mozilla.org/en-US/docs/Web/API/IDBOpenDBRequest)` et elle prend le nom de l'objectStore et le mode avec lequel l'opération doit être effectuée. Dans ce cas, le mode est `readwrite` puisque nous écrivons dans l'objectStore.

Comme mentionné précédemment, IndexedDB accepte les données sous forme de paires clé-valeur. Nous utilisons le timestamp pour générer un identifiant unique pour un enregistrement particulier. `store.put(data)` ajoute de manière asynchrone les enregistrements de livres dans l'objectStore `books`. Sur les mêmes lignes, j'ai ajouté les méthodes get et delete dans notre wrapper. Veuillez vérifier le code complet du wrapper IndexedDB [ici](https://github.com/ankita1910/bookskeep-pwa/blob/master/app/src/js/utils/indexeddb.js).

Maintenant que notre wrapper IndexedDB est prêt, il est temps d'utiliser la fonction d'ajout/mise à jour de notre wrapper chaque fois qu'un utilisateur essaie d'ajouter un nouvel enregistrement de livre. Modifions notre composant Body pour accommoder ces changements.

Tout d'abord, importez `IndexedDbWrapper` dans le composant Body. Nous allons appeler la fonction `initialize` de `IndexedDbWrapper` dans `componentDidMount`. La méthode `initialize` prend le callback en tant que fonction `initializeDB`, qui est définie dans le composant Body. `initializeDB` fait le travail de configuration de l'état initial de notre application en récupérant les enregistrements de livres stockés à partir d'IndexedDB.

Une dernière chose à faire avec `IndexedDbWrapper` est d'appeler sa méthode `update` lors de la soumission d'un enregistrement de livre. Nous devons modifier la méthode `onSubmit` du composant Body comme suit :

Maintenant, le nouvel enregistrement sera d'abord ajouté à IndexedDB, et une fois cela fait avec succès, nous mettons à jour l'état du composant. Essayez d'ajouter un nouvel enregistrement de livre et de recharger la page. Vous verrez toujours votre enregistrement de livre dans le tableau. Voici d'où il provient !

![Image](https://cdn-media-1.freecodecamp.org/images/0*dnhPB5See2bfAe74.png)

Ajoutons un enregistrement et actualisons la page. Les données sont préservées et c'est exactement ce que nous voulions. Nous avons construit un moyen de récupérer des données directement côté client. Nous nous rapprochons de notre objectif de construire une Progressive Web Application.

### Ajouter un Service Worker pour mettre en cache les actifs statiques

L'étape suivante consiste à tirer parti de la puissance des Service Workers en récupérant les actifs statiques depuis le cache. Un service worker doit d'abord être enregistré sur une page web.

_Enregistrement du Service Worker_

La fonction `initializeSW` est définie dans le composant Body, et nous l'appellerons dans le hook de cycle de vie `componentDidMount`. `serviceWorker` est défini sur [navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator). Selon MDN,

> l'interface Navigator représente l'état et l'identité de l'agent utilisateur. Elle permet aux scripts de l'interroger et de s'enregistrer pour effectuer certaines activités.

Un Service Worker est enregistré en utilisant la méthode `register` définie sur l'objet `navigator.serviceWorker`. La méthode `register` prend l'URL du fichier du service worker. Elle retourne une `Promise` qui se résout lorsque le service worker est enregistré avec succès sur la page web. Une fois cela fait, vous verrez un message de succès dans la console. Par défaut, les service workers peuvent intercepter toutes les requêtes fetch provenant de la page web.

La méthode `register` prend également un deuxième paramètre optionnel, qui définit la `portée` du service worker.

```
navigator.serviceWorker.register('./service-worker.js', { scope: '/products' })
```

Le service worker ci-dessus n'interceptera que les requêtes `/products/*`. Donc, quelque chose comme `/payments` n'est pas intercepté par le service worker ci-dessus.

Comme dit précédemment, les Service Workers fonctionnent comme un système piloté par événements. Après un enregistrement réussi, un événement `install` est déclenché. Nous pouvons utiliser le gestionnaire d'événements d'installation pour les tâches d'initialisation. Dans notre cas, nous allons configurer notre cache pour stocker les actifs statiques.

Voici le gestionnaire d'événements d'installation :

`event.waitUntil` s'assure que le service worker est actif pendant que les URL sont ajoutées au cache.

Le service worker n'a pas encore commencé à faire sa magie. Après avoir été installé avec succès, un événement `activate` est déclenché et c'est un bon endroit pour effacer les anciens caches inutilisés. Faisons notre part :

Le gestionnaire d'événements `activate` prend en charge la suppression de tous les caches sauf `bookskeep-cache`. Lorsqu'une page web fait une requête réseau au serveur, l'événement fetch du service worker est déclenché. Donc, si nous devions manipuler ou modifier la réponse à envoyer pour une requête particulière, nous devrons le faire dans le gestionnaire d'événements fetch.

La méthode `event.respondWith` nous permet d'envoyer une réponse modifiée au client. Elle retourne une Promise qui se résout en une réponse valide. `cache.match` vérifie si la requête est une ressource valide pour la mise en cache (si vous vous souvenez, nous avons ajouté quelques URL spécifiques à la variable `urlsToCache` dans le gestionnaire d'événements d'installation).

Si la réponse à cette requête est présente dans le cache, nous l'envoyons directement au client, sinon, nous demandons cette ressource au serveur, la mettons dans le cache pour les prochains accès, et l'envoyons au client.

![Image](https://cdn-media-1.freecodecamp.org/images/0*srtIpMIoAkzVZZqt.png)

[Voici](https://github.com/ankita1910/bookskeep-pwa/blob/master/mid-steps/service-worker-1.js) le fichier service worker avec les trois gestionnaires d'événements expliqués ci-dessus.

### Ajouter manifest.json

`short_name` est utilisé sur l'écran d'accueil comme nom de l'application. Au cas où `short_name` n'est pas fourni, alors la propriété `name` est utilisée à sa place. `icons` apparaissent comme une icône d'écran d'accueil pour l'application dans le lanceur d'applications et sur l'écran de démarrage. `start_url` indique au navigateur la page de démarrage de l'application. Un utilisateur sera dirigé vers cette URL lorsque l'application est lancée. `standalone` comme propriété d'affichage de l'application lui donne l'apparence et la sensation d'une application native. L'application s'exécute dans sa propre fenêtre et masque certains des éléments spécifiques au navigateur comme la barre d'URL. `background_color` définit la couleur de l'écran de démarrage lorsque l'application est lancée pour la première fois et `theme_color` indique la couleur de la barre d'outils.

C'est tout. Nous avons configuré notre _BooksKeep PWA_. Faisons un rapide récapitulatif des choses que nous avons apprises dans ce tutoriel :

1. Le web traditionnel manque de certaines des fonctionnalités importantes que les applications natives fournissent dès le départ. Les Progressive Web Applications aident à améliorer considérablement l'expérience utilisateur sur le web. Elles sont rapides, fiables et engageantes et fournissent une expérience similaire à celle des applications natives.
2. Les PWA utilisent des Service Workers, IndexedDB (ou tout autre cache local), manifest.json et des notifications push web.
3. Les Service Workers fonctionnent comme un système piloté par événements et écoutent les événements fetch et push. L'événement `fetch` nous permet d'envoyer la réponse à une requête réseau directement depuis le cache en cas de connexions lentes ou intermittentes. L'événement `push` nous permet de montrer des notifications push à l'utilisateur et aide à engager l'utilisateur en l'informant des mises à jour en temps opportun.
4. IndexedDB est une structure clé-valeur. Il aide à stocker une quantité massive de données côté client. `manifest.json` informe le navigateur de certaines des propriétés importantes d'une application.
5. Nous avons appris comment commencer à construire une Progressive Web Application.

C'était une rapide introduction aux Progressive Web Applications. Si vous souhaitez explorer davantage, voici quelques ressources :

1. [Un guide extensif sur les Progressive Web Applications](https://www.smashingmagazine.com/2018/11/guide-pwa-progressive-web-applications/)
2. Consultez mon application [BooksKeep](https://github.com/ankita1910/bookskeep) sur GitHub. J'ai ajouté quelques fonctionnalités supplémentaires comme la mise à jour des enregistrements de livres, l'ajout de citations et le support des notifications push web. J'en ajouterai davantage !
3. [Service Workers](https://hackernoon.com/service-workers-62a7b14aa63a)

_Veuillez me faire savoir si vous avez trouvé ce tutoriel utile et partagez-le avec quiconque vous pensez pourrait en bénéficier._

_Originalement publié sur [hashnode.com](https://hashnode.com/post/benefits-of-progressive-web-applications-pwas-and-how-to-build-one-cjqry4q0c00qo8ms1ckbv9xnc)._