---
title: 'Apprendre Node.js avec Brigadier Fluffykins Partie I : Sync, Async et Créer
  Votre Premier Serveur !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-11T22:02:13.000Z'
originalURL: https://freecodecamp.org/news/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4E7_DswXy8rFF2Dzrq1H3A.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Node.js avec Brigadier Fluffykins Partie I : Sync, Async et
  Créer Votre Premier Serveur !'
seo_desc: 'By Mariya Diminsky

  Welcome to Part I of Learn Node.js With Brigadier Fluffykins, a series created to
  help you easily understand Node.js ❤

  A new adventure has arrived! I will be taking you step by step from initial Node.js
  install to creating your fir...'
---

Par Mariya Diminsky

Bienvenue à la Partie I de **Apprendre Node.js Avec Brigadier Fluffykins**, une série créée pour vous aider à comprendre facilement Node.js f496

Une nouvelle aventure a commencé ! Je vais vous guider étape par étape, de l'installation initiale de Node.js à la création de votre premier serveur, en passant par la personnalisation de vos réponses, la compréhension des flux et des événements, ainsi que l'utilisation de frameworks. Commençons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7IURnff2RaD8iM8yePIw7g.gif)

Brigadier Fluffykins veut s'assurer que vous avez révisé les bases des _callbacks_ et des _promesses_. Si ce n'est pas le cas :

* Regardez [cette](https://www.youtube.com/watch?v=QqiNn3GfTMc) vidéo et lisez [cet](https://medium.freecodecamp.com/javascript-callbacks-explained-using-minions-da272f4d9bcd#.10k431muw) article sur les _callbacks_.
* Regardez [cette](https://youtu.be/2d7s3spWAzo?t=24s) vidéo et lisez [cet](https://davidwalsh.name/promises) article sur les _promesses_.

Ce n'est pas grave si vous ne comprenez pas tout immédiatement. L'important est que vous soyez introduit à ces concepts maintenant. Nous voulons que votre cerveau commence à s'adapter aux modèles de programmation Node.js que vous mettrez en œuvre tout au long de ces leçons. Bonne chance et bon apprentissage ! :)

La leçon d'aujourd'hui couvrira :

* Ce qu'est Node.js et ce que vous pouvez construire avec.
* Un bref aperçu du fonctionnement du web (c'est-à-dire la relation Client, Serveur).
* Télécharger et installer Node.js sur Mac/Windows/Linux.
* Ce que signifient asynchrone/synchrone, et ce que signifient non-bloquant/bloquant.
* Comment créer votre premier serveur.

### Qu'est-ce que Node.js ?

Node.js est un environnement d'exécution open source multiplateforme qui vous permet de construire des applications réseau évolutives côté serveur.

Par environnement d'exécution, je veux dire que Node.js contient le [_V8 JavaScript runtime_](http://stackoverflow.com/questions/29027845/what-is-the-difference-between-javascript-engine-and-javascript-runtime-environm) — le même utilisé (et développé par) le navigateur Google Chrome côté client. En utilisant les modules et bibliothèques de Node.js — expliqués plus tard dans cette série — nous avons un moyen de :

* Faire évoluer les applications à mesure que le trafic augmente
* Construire des salles de chat et d'autres applications gourmandes en données
* Manipuler directement les informations de la base de données
* Accéder et façonner les fichiers dans notre système en fonction des préférences
* Router les requêtes (pour les pages html/css/js d'un site web) et surveiller le trafic
* Avoir des téléchargements plus rapides et la capacité de montrer la progression de ces téléchargements
* Personnaliser nos réponses à ces requêtes via le routage et la redirection

Grâce à _V8_ et Node.js étant principalement écrits en C et C++ (même si de nombreux modules sont écrits en JavaScript), Node.js est très rapide. Cela est super important lorsque vous avez une application qui a besoin de scalabilité.

Imaginez des milliers d'utilisateurs accédant à votre application, et demandant ainsi des informations à votre serveur. Que pensez-vous qu'il va se passer ? Vous n'avez aucun moyen de gérer ces requêtes, et même si vous en avez, elles peuvent être synchrones (expliqué plus tard). Les utilisateurs finissent par attendre derrière des milliers d'autres utilisateurs pour que les fichiers nécessaires soient retournés. Les vitesses de chargement sont lentes, créant une mauvaise expérience utilisateur et vous faisant perdre des affaires.

Faire évoluer votre application lorsque le trafic augmente est l'un des plus grands défis qu'une application rencontre dans ses premiers stades.

Node.js vous permet de gérer un grand nombre de connexions simultanément et de manière asynchrone — cela signifie essentiellement qu'il permet la scalabilité. En plus de cela, vous avez des bibliothèques pour vous aider à personnaliser la gestion de ces problèmes.

### Client et Serveur : Le Modèle Traditionnel

Avant de continuer, je veux donner un bref aperçu du fonctionnement du web via le client et le serveur. Si vous comprenez déjà cela, passez à la partie suivante.

Lorsque je dis client, je veux dire toute personne qui demande des informations.

Lorsque je dis serveur, je veux dire toute personne qui traite une requête et répond avec les informations nécessaires.

Par exemple, lorsque vous allez taper :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h25IAJDGMkJCigVgEIe9sA.png)

Vous êtes sur le point d'initier plusieurs requêtes pour la page HTML du site web, ses feuilles de style CSS, ses documents JavaScript, et ainsi de suite. Vous _demandez_ ou _requérez_ à leur serveur de vous montrer la page et tous les documents qui y sont associés.

Lorsque les serveurs du site web reçoivent ces requêtes, ils répondent avec la page HTML, les feuilles de style CSS, et tout ce dont vous pourriez avoir besoin pour voir cette page. C'est l'essentiel.

Il est important de noter que n'importe qui peut être un client ou un serveur. Lorsque vous créez une application localement, vous agissez en fait comme un client et un serveur (comme _localhost:3000_). Plus sur cela plus tard.

Pour l'instant, explorons comment Node.js gère ces requêtes par rapport au modèle traditionnel. Nous utiliserons des animations que Brigadier Fluffykins a faites pour nous. L'orange est la requête de Brigadier Fluffykins à son site web préféré et le vert est la réponse du serveur. Lent et régulier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6dwqGXgG5KqeyaY5t9e3EQ.gif)
_Brigadier Fluffykins est énervé._

Le modèle client-serveur traditionnel implique que le client initialise une requête en premier. Chaque connexion de requête crée un nouveau thread — un nouveau processus où le code s'exécute — prenant ainsi de la mémoire dans votre système. Cela finit par créer des problèmes de scalabilité en raison de la mémoire qui s'épuise ou de votre serveur qui plante en raison d'une surcharge de requêtes (trafic utilisateur élevé).

Si vous êtes intéressé à approfondir le fonctionnement du modèle client-serveur, je recommande d'explorer [ici](https://medium.freecodecamp.com/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c).

### Client et Serveur : Avec Node.js

Avec Node.js, le client et le serveur peuvent initier des connexions bidirectionnelles permettant aux données de communiquer librement entre les deux. Même si Node.js est monothread — tout comme JavaScript — et qu'un seul processus se produit à la fois (expliqué plus tard dans la série), il "agit" comme multithread en traitant les requêtes via des _callbacks_ et des _promesses_. Il est ainsi capable de supporter des milliers de connexions simultanées de manière non bloquante/asynchrone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gqJjtuAlpWqAE-XYPb3uDQ.gif)
_Brigadier Fluffykins est heureux._

Node.js peut agir comme le client, le serveur ou les deux. N'est-ce pas génial ?

En tant que serveur, un utilisateur visite votre site web et fait des requêtes (pour des fichiers HTML, CSS et JavaScript). Node.js reçoit ces requêtes et envoie une réponse (les fichiers HTML, CSS et JavaScript demandés) et ainsi de suite.

En tant que client, Node.js demande du contenu à un autre site. Par exemple, lorsqu'un client veut publier quelque chose sur Pinterest ou Twitter depuis votre site.

Pour utiliser Node.js comme client, vous devez installer la bibliothèque [Request](https://www.npmjs.com/package/request) (nous parlerons de l'installation de modules et de bibliothèques pour Node.js plus tard dans cette série).

Il est important de réaliser que Node.js ne fait rien par lui-même. Ce n'est pas un serveur web. C'est juste un environnement d'exécution. Si vous voulez un serveur web, vous devez écrire ce serveur vous-même (homme, femme… enfant… chat… vous avez compris). Vous voulez ajouter des informations à vos fichiers ? Vous devez aussi l'écrire vous-même — Node.js ne crée pas cela magiquement pour vous, mais il ajoute beaucoup de fonctionnalités géniales avec lesquelles vous pouvez jouer. Et Brigadier Bunny Fluffykins va vous apprendre comment ! Yeah !

### **Télécharger et Installer Node.js**

1. Ouvrez votre terminal de ligne de commande. Si vous ne savez pas comment trouver votre ligne de commande, voici quelques liens qui peuvent aider :

* [Mac](https://www.davidbaumgold.com/tutorials/command-line/#finding-the-command-line)
* [Windows](http://www.computerhope.com/issues/chusedos.htm)
* [Linux](http://linuxcommand.org/lts0010.php#starting)

2. Ensuite, assurez-vous que Git est opérationnel :

* Vous pouvez le télécharger [ici](https://git-scm.com/downloads).
* Regardez [cette](https://git-scm.com/video/get-going) vidéo d'introduction de 4 minutes sur git.
* Lisez cet [article](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) si vous avez encore besoin d'aide.

3. [Téléchargez](https://nodejs.org/en/download/) Node.js sur votre système.

Pour vérifier si vous l'avez installé, tapez _node -v_ dans votre ligne de commande, vous devriez voir le numéro de version apparaître :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hsizklixn9QgjmdnqkvnfA.png)

Maintenant que vous avez installé Node.js, vous pouvez accéder à la commande _node_ dans votre terminal et taper du code JavaScript dans votre shell !

![Image](https://cdn-media-1.freecodecamp.org/images/1*PNTv39xLvpnUDCf1_U2WPw.png)

Vous pouvez également exécuter du code à partir d'un fichier JavaScript :

Créons un fichier appelé _bunny.js_ dans votre éditeur de code (comme Sublime, Brackets ou Atom). Tapez _console.log('I will give Brigadier Fluffykins 20 carrot bits')_ à l'intérieur du fichier, ou téléchargez [ce](https://drive.google.com/file/d/0Byvu31DWppA7UEs5SWc2bWN5S1E/view?pref=2&pli=1) zip qui inclut ce fichier ainsi que les quelques fichiers suivants dont nous avons besoin pour le reste de la leçon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qjT_0nqvKxZhsBpFBW7RjQ.png)

Appuyez sur _ctrl + c_ à l'intérieur du terminal pour Mac deux fois pour sortir du processus node (je crois que c'est _killall node_ pour Windows — corrigez-moi si je me trompe ici).

Maintenant, trouvez où se trouve votre fichier. Dans mon cas, je suis passé sur le Bureau, puis dans le dossier où j'ai enregistré le fichier _bunny.js_ (_nodestory_). Vous l'avez peut-être enregistré sur votre Bureau. Maintenant, dans le shell, tapez _node bunny.js_ et VOILÀ ! Votre JavaScript apparaît dans le terminal ! :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dl5AnRH5MqdIKEHgNpfwBQ.png)

### Code Asynchrone et Synchrone

Pour que Node.js gère des milliers de connexions simultanées, il doit les gérer de manière asynchrone, de manière non bloquante. Cela signifie que vous pouvez avoir plus d'une action en cours en même temps, vous l'avez vu dans la deuxième animation.

Le blocage — ou synchrone — d'autre part, n'exécutera qu'une seule action à la fois. Il ne permettra pas à une deuxième action de s'exécuter tant qu'elle n'a pas terminé. Lorsque nous avons envoyé une requête pour un fichier, nous avons dû attendre que le serveur réponde avant de pouvoir envoyer une autre requête. Cela prend beaucoup de temps pour Brigadier Fluffykins, et il était mécontent.

Si vous créez du code de manière asynchrone, vous pouvez exécuter des actions en parallèle. Cela peut prendre moins de la moitié du temps par rapport à une approche synchrone.

Bien que Node.js ait été délibérément créé pour être non bloquant, il permet aux développeurs de choisir comment ils veulent que leur code s'exécute via des méthodes modifiables dans leurs bibliothèques. Par exemple, Node.js a une méthode _appendFile_ qui peut ajouter quelque chose de nouveau à votre fichier [de manière asynchrone](https://nodejs.org/docs/latest-v5.x/api/fs.html#fs_fs_appendfile_file_data_options_callback) ou [de manière synchrone](https://nodejs.org/docs/latest-v5.x/api/fs.html#fs_fs_appendfilesync_file_data_options). Voici un autre exemple :

Suivez les étapes 1–5, ou téléchargez ce [zip](https://drive.google.com/file/d/0Byvu31DWppA7UEs5SWc2bWN5S1E/view?pref=2&pli=1) avec les fichiers que j'ai déjà créés pour vous :

1. Créez d'abord un dossier appelé 'nodestory'.
2. Créez ces 3 fichiers : _wishlist.html_, _bunnySync.js_ et _bunnyAsync.js_ à l'intérieur du dossier.
3. Ouvrez ce dossier dans votre éditeur de code (Sublime, Brackets, Atom, etc.).
4. Dans _wishlist.html_, copiez et collez ceci :

5. Dans _bunnySync.js_, copiez et collez ceci :

Ok, maintenant exécutez _node bunnySync.js_ dans votre terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kzaUvCp7OHuMEfV67lWAqQ.png)

Remarquez comment notre alerte est imprimée dans le même ordre que lorsque nous avons écrit le code ? Maintenant, essayons le même concept mais de manière asynchrone/non bloquante.

Dans _bunnyAsync.js_, collez ceci — assurez-vous que c'est le bon nom de fichier :

Ok, maintenant exécutez _node bunnyAsync.js_ dans votre terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tL06luIR_nMsqkt4IGQNNQ.png)

Remarquez comment nos alertes, peu importe l'ordre, s'impriment toutes avant que le fichier ne soit entièrement lu ? La lecture du fichier prend plus de temps que l'utilisation de la fonction _console.log_, et ainsi nos alertes sont imprimées en premier. Une fois le fichier lu, il s'imprime éventuellement.

### **Créez Votre Premier Serveur**

C'est ce moment spécial de l'année… pour créer votre premier serveur !

Woohoo ! Je suis tellement excitée pour vous ! Nous allons passer par plusieurs exemples, alors créez un fichier appelé _server.js_ et collez ceci :

…ou ouvrez le fichier _server.js_ dans le dossier zippé que j'ai fourni plus tôt.

Assurez-vous que seules les variables _http_ et _fs_ — ainsi que 'ÉTAPE #1' — ne sont pas commentées. Passez en revue le code et réfléchissez à ce que vous pensez qu'il se passe avant de continuer à lire.

Comme vous l'avez peut-être remarqué, en plus des modules et des bibliothèques tierces, Node.js vient également avec une liste exhaustive de méthodes. Vous n'utiliserez probablement pas toutes — cela dépend vraiment de ce que vous construisez.

Maintenant, tapez _node server.js_ dans votre terminal pour démarrer le serveur.

Allez dans la barre d'URL et tapez _localhost:3000_ pour voir la réponse que vous venez d'envoyer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nCQ0iw-v8uC9Q_Q9JNlI8w.png)

Ok, que se passe-t-il ici ?

Pour chaque requête, vous avez besoin d'une réponse. Tout d'abord, nous répondons au client en définissant le code de statut dans l'en-tête à 200, ce qui signifie que ce site web est OK, prêt à partir !

Vous pouvez vérifier les en-têtes en cliquant sur _option + commande + J_ dans Chrome sur un Mac, ou en cliquant avec le bouton droit et en choisissant _inspecter_ puis en cliquant sur l'onglet _Réseau_ (c'est l'une des options à côté de l'onglet _Console_). Si vous ne voyez rien sous _Réseau_, appuyez simplement sur actualiser. Sinon, cliquez sur la page et vous verrez sous _En-têtes_ le code de statut et le type de requêtes que le client a faites (dans notre cas, "localhost:3000"). Il s'agit d'une requête GET, puisque nous voulons obtenir un fichier d'un serveur.

Voici ce qui se passerait si nous définissions nos en-têtes à 404 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cwAzc_fo5gxFfbmwiaAFJA.png)

Essayez-le dans votre code et voyez si vous pouvez obtenir un code de statut 404.

Les en-têtes et les codes de statut sont un sujet intéressant en eux-mêmes, mais je n'entrerai pas dans cela maintenant. J'ai inclus des ressources à la fin, si vous souhaitez faire plus de recherches.

Ensuite, nous avons la réponse que nous voulons envoyer au client, ou ce que le client verra réellement sur sa page en utilisant la méthode _write_. Ensuite, nous fermons la connexion avec la méthode _end_.

Enfin, nous définissons le port sur lequel notre serveur écoutera les requêtes. Cela peut être 3000, 8080, ou essentiellement ce que vous voulez. Assurez-vous simplement d'aller sur _localhost:8080_ si, par exemple, vous utilisez le port 8080.

C'est une bonne pratique de définir les en-têtes avant de définir la réponse, surtout parce que les en-têtes viennent avant le corps dans les réponses _HTTP_.

Vous venez d'apprendre à créer votre premier serveur ! Tapez-vous dans le dos, ou giflez-vous au visage — ce qui fonctionne pour vous !

Continuons notre aventure en construisant l'une des formes les plus courantes que vous verrez pour les serveurs _HTTP_. C'est la même chose que ce que nous venons de créer, sauf qu'il y a quelques différences de syntaxe qui se concentrent sur les _événements_ et les _émetteurs d'événements_ (expliqués plus tard dans la série).

Commentez 'ÉTAPE #1' et décommentez 'ÉTAPE #1.5'.

C'est vraiment important : avant de faire autre chose, soyez conscient que lorsque vous démarrez un serveur puis changez quelque chose dans le fichier, les changements ne seront pas visibles tant que vous n'aurez pas arrêté le serveur et redémarré. Il existe des bibliothèques qui redémarreront automatiquement le serveur pour vous lors de la détection de changements (comme [Nodemon](https://www.npmjs.com/package/nodemon)), mais ne vous inquiétez pas de le configurer maintenant.

Pour l'instant, pour arrêter le serveur manuellement, allez dans votre terminal et appuyez sur _control + C_ pour Mac (encore une fois, je crois que c'est _killall node_ pour Windows), puis appuyez sur la flèche vers le haut pour parcourir les commandes précédentes que vous avez tapées, ou tapez manuellement _node server.js_.

Vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lVqQlQiXJo3d_ZtScjXBbw.png)

Remarquez que nous pouvons envoyer un peu de HTML de base à l'intérieur de la méthode _end_, envoyant ainsi une réponse et mettant fin à notre connexion en même temps. Nous pouvons également stocker notre serveur dans une variable pour le rendre plus lisible lorsque nous utilisons des événements tels que _request_. Il est important de noter que l'événement _request_ n'est pas la même chose que la bibliothèque tierce _Request_. Cela m'a confus lorsque j'ai appris Node.js pour la première fois, et je ne voudrais pas que vous passiez par la même chose. Nous parlerons de ceux-ci dans les prochaines leçons de la série.

### Ressources Supplémentaires

Je vous exhorte à sortir et à faire quelques recherches. Tirez le meilleur parti du temps que vous avez. Voici quelques endroits où vous pouvez commencer :

* [Qu'est-ce que Node.js exactement ?](https://www.youtube.com/watch?v=pU9Q6oiQNd0)
* [Documentation Node.js](https://nodejs.org/docs/latest-v5.x/api/).
* [Qu'est-ce que les buffers dans Node ?](https://docs.nodejitsu.com/articles/advanced/buffers/how-to-use-buffers/)
* [Liste des codes de statut et leurs significations.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* [Répétez après moi : "Google est mon ami"](https://www.google.com/)

Félicitations ! Vous avez réussi la **Partie I d'Apprendre Node.js Avec Brigadier Fluffykins** ! Maintenant, vous serez en mesure d'expliquer les bases de Node.js ainsi que ce que vous pouvez construire avec. Vous avez eu une introduction sur le fonctionnement du code async/non-bloquant et sync/bloquant, et les avantages que Node.js offre avec la programmation async. Le meilleur de tout, vous avez enfin pu configurer votre tout premier serveur !

Wow. Sérieusement, super boulot. Brigadier Fluffykins salue votre effort.

Nous approfondirons ces sujets ainsi que d'autres que nous avons seulement effleurés dans les prochaines leçons. Merci d'avoir lu et restez à l'écoute.

Gardez votre sagesse à jour en cliquant sur le f496 ci-dessous et en suivant, car plus de **Apprendre Node.js Avec Brigadier Fluffykins** arrive bientôt sur Medium !

[**Partie I : Sync, Async, et Créer Votre Premier Serveur !**](https://medium.freecodecamp.com/learn-node-js-with-brigadier-fluffykins-i-basics-async-sync-create-your-first-server-b9e54a45e108#.bvd38wc9b)

[**Partie II : Événements, EventEmitter et Boucle d'Événements**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-ii-events-eventemitter-the-event-loop-6d4c139694fb#.957cacwgv)

[**Partie III : Objet de Requête, Configurer les Routes, Servir des Fichiers**](https://medium.com/@__Masha__/learn-node-js-with-brigadier-fluffykins-part-iii-request-object-configure-routes-serve-files-7666f783dc10#.g5j0faw3x)