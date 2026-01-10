---
title: Apprenez la pile FARM ! (FastAPI, React, MongoDB)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-15T13:43:01.000Z'
originalURL: https://freecodecamp.org/news/learn-the-farm-stack-fastapi-reactjs-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/farmstack.png
tags:
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: Apprenez la pile FARM ! (FastAPI, React, MongoDB)
seo_desc: 'The FARM stack is FastAPI, React, and MongoDB. It is a simpler form of
  the MERN stack that can make developing apps even faster.

  We just released a FARM stack course on the freeCodeCamp.org YouTube channel.  You
  will learn how to create a basic CRUD ...'
---

La pile FARM est FastAPI, React et MongoDB. C'est une forme plus simple de la pile MERN qui peut rendre le développement d'applications encore plus rapide.

Nous venons de publier un cours sur la pile FARM sur la chaîne YouTube freeCodeCamp.org. Vous apprendrez à créer une application CRUD de base.

FastAPI est l'endroit où votre code côté serveur réside. Vous apprendrez à le connecter avec une base de données MongoDB. Ensuite, vous apprendrez à connecter le backend au frontend. Une application React enverra et recevra des requêtes HTTP vers et depuis le serveur.

Bek Brace a développé ce cours. Bek est un développeur qui a créé de nombreux cours sur sa chaîne YouTube.

Voici les sections de ce cours :

* Pile FARM Expliquée (Théorie)
* Construction du Backend (FastAPI)
* Requêtes MongoDB
* Conception du Frontend
* Test de l'Application

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=OzUzrs8uJl8) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=OzUzrs8uJl8]

## Transcription

(générée automatiquement)

Dans ce cours, vous irez à la ferme. La pile FARM est Fast API, React et GraphQL.

Bek Brace vous apprendra à utiliser cette pile pour créer une application web full stack.

Hey, qu'est-ce qui se passe les gars, c'est Big Breeze.

J'espère que vous allez tous bien.

Bienvenue sur les forums.

Ce cours dans le cours d'aujourd'hui, les technologies que nous allons utiliser sont quelques-unes de mes préférées.

Nous allons travailler avec Fast API, React js et MongoDB, qui sont les composants de la pile FARM.

Et vous avez probablement entendu parler de cette pile suffixe dans d'autres termes, comme la pile MERN, qui signifie MongoDB Express, React et Node JS.

Et ce qu'on entend par pile simplement est un ensemble de technologies que vous pouvez utiliser ensemble pour créer une application web, par exemple.

Donc FARM signifie Fast API, React et MongoDB.

Et nous allons construire notre application en utilisant Fast API pour le serveur backend, React pour le client frontend et MongoDB pour le serveur de base de données backend.

Donc c'est pour la persistance des données.

Et à mon avis, la pile FARM ressemble à la pile MEAN ou MERN.

La seule différence est Fast API.

Parce que React et MongoDB sont les mêmes dans les trois piles.

Dans MEAN, nous utilisons Angular, no GS, et dans MERN, nous utilisons React et Node JS.

Fast API, bien sûr, est un framework web moderne et rapide pour construire des API créé par Sebastian Ramirez.

Et cela utilise ASGI.

Et ASGI signifie Asynchronous Server Gateway Interface.

Et ce n'est que l'interface entre votre application et le serveur.

Et le temps de réponse est ultra-rapide.

Et c'est l'un des grands avantages d'avoir ASGI comme implémentation serveur de votre côté, également Fast API, l'une de ses plus grandes fonctionnalités est qu'il supporte les coroutines et la concurrency sans avoir besoin d'importer le module async IO en Python.

Et d'une certaine manière, il est plus rapide qu'Express, qui est un framework no GS.

Et Express est le E dans les piles MEAN et MERN, comme nous l'avons dit.

Donc Fast API a également une documentation API interactive.

Et cela vous aide à visualiser les différentes requêtes HTTP comme get, post, put et delete en utilisant Open API, qui est lui-même basé sur le schéma JSON.

Et j'ai un cours complet sur Fast API, vous trouverez une carte apparaissant maintenant si vous êtes intéressé à le vérifier.

React, bien sûr, est la bibliothèque frontend JavaScript la plus célèbre pour construire des interfaces utilisateur, surtout les SPA, ou applications à page unique, selon l'enquête Stack Overflow pour 2020.

React GS est juste en dessous de jQuery.

Donc comme vous pouvez le lire ici, jQuery est toujours roi.

Mais il perd lentement du terrain face à React js et Angular année après année, selon le framework le plus aimé, il est juste le deuxième après ASP dotnet core.

Et le plus demandé est en fait React GS, le plus demandé sur le marché.

Et je crois que le lien vers les enquêtes pour Stack Overflow dans la section description ci-dessous.

Si vous souhaitez vérifier d'autres statistiques, c'est très intéressant.

Vous trouverez ici que le langage le plus redouté est VBA.

Et j'ai travaillé avec VB pendant un certain temps maintenant au travail, surtout le système de débogage est vraiment horrible.

Donc pas étonnant que ce soit le langage le plus redouté.

D'accord, suivant cela, Objective C, Perl, assembleur C, PHP, et ainsi de suite.

Donc, de manière surprenante, Rust est le langage le plus aimé, suivi de TypeScript puis Python, mais en fait le langage le plus demandé sur le marché est Python, suivi de JavaScript puis Go Lang.

Et j'ai aussi un tutoriel React pour les développeurs backend débutants, vous trouverez une carte apparaissant maintenant, vérifiez-le si vous le souhaitez.

Dernier mais non des moindres, nous avons besoin de la persistance.

Donc nous utiliserons MongoDB, qui est la lettre M dans FARM.

Et je n'ai jamais fait de tutoriel sur MongoDB sur la chaîne.

Donc c'est le premier.

Et j'essaierai d'être aussi détaillé que possible.

Et j'ai reçu quelques demandes pour créer un cours accéléré sur MongoDB et Maria DB.

Donc le cours MongoDB est presque prêt et sera téléchargé bientôt.

MongoDB est un système de gestion de base de données NoSQL.

Et NoSQL signifie Not Only SQL, et il est basé sur ce que nous appelons le modèle de document ou des collections de documents.

Donc même le système SQL normal comme MySQL, Postgres ou Oracle, si vous avez une table, si vous avez une base de données qui consiste en différentes tables, et chaque table a des lignes et des colonnes, ici dans le monde NoSQL, vous avez une collection de documents.

Et un document est simplement le fichier écrit au format JSON, et converti pour être en BSON ou JSON binaire, qui est les zéros et uns pour que l'ordinateur compile et comprenne.

Donc dans le monde SQL, si vous avez une base de données de différentes tables, et chaque table a un ensemble de lignes et de colonnes, dans MongoDB, vous avez aussi une base de données.

Mais elle consiste en des collections qui consistent en des documents.

Et chaque document a différents champs comme ID, nom, prénom, par exemple, tous ceux-ci sont des champs dans un document MongoDB.

Dernier mot, je voudrais dire sur MongoDB, qu'il a été créé en 2009.

Et c'est le principal système NoSQL sur le marché maintenant.

Donc assez parlé, et commençons par créer notre application.

Notre application est essentiellement une application CRUD.

Donc le frontend va envoyer des requêtes HTTP au backend, le backend va récupérer toutes les données de la base de données dans MongoDB, MongoDB va envoyer les données à FastAPI vers le serveur backend, puis le serveur backend utilisant la technologie axios enverra leur réponse au frontend React, que vous verrez à l'écran.

Donc du frontend au backend, du backend au frontend.

D'accord, vous aurez évidemment besoin d'avoir Python installé, vous aurez aussi besoin de Node.js car nous aurons besoin de NPM.

Pour créer notre application React, en ce qui concerne MongoDB, vous aurez besoin d'avoir un compte sur MongoDB Atlas.

Donc vous pouvez cliquer sur Démarrer gratuitement.

Et vous remplirez les données ici, votre entreprise, comment vous utilisez MongoDB, votre email, prénom, nom et mot de passe.

Et une fois que vous avez fait cela, vous aurez ici un cluster inclus avec votre base de données cloud gratuite, vous aurez un niveau gratuit pour avoir un cluster de ordinateurs avec 512 mégaoctets de stockage.

D'accord, ce n'est pas un ordinateur physique, mais logique.

Donc vous aurez du DRAM partagé, vous aurez 512 mégaoctets de stockage, des ensembles de réplicas hautement disponibles, un chiffrement de bout en bout pour répondre aux correctifs et une API REST.

D'accord, tout cela est inclus dans votre niveau gratuit.

D'accord, donc une fois que vous êtes connecté, vous ne trouverez pas cela dans les clusters, vous trouverez un bouton vert au milieu vous disant de créer un nouveau cluster.

D'accord, donc c'est le cluster zéro.

C'est ici comment connecter vos collections.

Et nous avons dit que les collections sont l'équivalent des tables dans le monde SQL, vous pouvez aussi avoir un autre cluster, mais je ne vais pas le faire car vous êtes autorisé seulement avec un cluster.

J'ai ma région ici en Belgique, car je vis en Pologne.

Et j'ai déjà essayé celui en Allemagne, mais il n'était pas si efficace.

Donc j'ai créé un nouveau avec la Belgique avec Google Cloud.

D'accord, vous aurez différentes options.

Donc laissez-moi vous montrer, vous aurez Google Cloud, vous aurez votre I utilisé Google Cloud, comme vous pouvez le voir ici, et j'utilise celui que vous pouvez voir ici, que le niveau gratuit est disponible.

D'accord, si vous êtes au Brésil, aux États-Unis, en Australie, en Finlande, tous ceux-ci sont gratuits, ceux avec une étiquette de niveau gratuit disponible.

Et une fois que vous savez ce que vous voulez choisir, vous pouvez cliquer dessus et créer un cluster gratuit, je peux en créer un autre car j'ai déjà un cluster gratuit.

Et vous pouvez voir ici qu'ils vous facturent pour un second à zéro point 44 $ par heure.

D'accord, oui, mais c'est assez simple.

Vous choisirez ce que vous voulez et ensuite vous cliquerez sur créer un cluster, cela prendra un certain temps à déployer et vous serez prêt à partir.

Comment vous pouvez vous connecter en cliquant sur Connecter.

Et vous aurez différents outils.

Donc vous pouvez vous connecter à votre application, vous pouvez utiliser le Mongo shell, qui est juste un terminal simple pour interagir avec votre base de données en utilisant la ligne de commande et en utilisant le MongoDB compass, je vous recommande fortement d'installer le compass et le shell.

Donc nous sommes de retour à la page d'accueil de MongoDB, vous pouvez aller à logiciel, cliquer sur serveur communautaire.

Et vous trouverez ici sur site, d'accord MongoDB localement, donc vous avez MongoDB serveur communautaire, vous pouvez le télécharger.

Donc MongoDB offre à la fois une version entreprise et communautaire de sa puissante base de données de documents distribués.

Donc ne vous souciez pas de l'entreprise, concentrez-vous simplement sur le serveur communautaire, vous pouvez le télécharger, c'est un fichier d'installation Microsoft MSI.

Donc c'est la première chose que vous devez faire.

De plus, vous devez aller aux outils de développement.

Et ici, vous pouvez télécharger le MongoDB compass et un shell MongoDB.

D'accord, donc MongoDB compass, et vous pouvez cliquer ici sur trade maintenant, et cela vous ramènera aux outils et vous pouvez le télécharger ici.

Et la même chose s'applique au shell MongoDB et si vous n'êtes pas sûr de la manière de faire cela, veuillez me le faire savoir dans la section des commentaires ci-dessous.

Et je créerai une vidéo rapide pour vous montrer comment tout configurer dans le chemin, d'accord dans la variable d'environnement, donc une fois que tout est installé correctement, vous pouvez aller de l'avant et taper Mongo D version.

Et vous obtiendrez cette version de DB 4.46.

D'accord avec ces données JSON, K, la version get version, et ainsi de suite.

De plus, pour accéder au shell MongoDB, vous pouvez aller de l'avant et taper Mongo s h.

Et vous pouvez jeter un coup d'œil aux bases de données disponibles.

Donc vous pouvez dire show DBS et vous obtiendrez les bases de données par défaut fournies par MongoDB.

D'accord, et laissez-moi vous montrer le MongoDB compass.

Donc voici à quoi cela ressemble.

Donc pour se connecter, nous pouvons dire Mongo DB, deux-points barre oblique barre oblique 120 7.0.

Point 0.1, ou localhost sur le port 27, zéro 17.

Cliquez sur Connecter.

D'accord, si vous voulez créer une base de données, vous pouvez le faire facilement.

Disons par exemple, nous aurons une base de données avec le nom de sales.

Avoir une collection d'employés, par exemple, d'accord, et créer une base de données.

Et immédiatement, vous avez votre base de données sales créée.

Et si vous actualisez ici show DBS, vous trouverez que sales est apparu ici.

Donc retroussons nos manches et commençons par créer notre serveur backend avec Fast API.

Bienvenue.

Donc la première chose que je veux faire est de créer un dossier qui contiendra à la fois les dossiers backend et frontend.

Donc allons sur le bureau.

Et créons un dossier farm stack underscore project.

Tout d'abord, nous nous occuperons du dossier backend.

Donc créons cela.

Et ouvrons cela avec Visual Studio code.

D'accord, super.

Donc la première chose que je veux faire ici est de créer requirements dot txt.

Et cela est pour les dépendances et nous aurons besoin de trois dépendances.

Donc la première est Fast API, évidemment.

Donc Fast API avec la version zéro, point 65.1.

De plus, j'aurai besoin de unicorn.

Et unicorn est simplement l'implémentation du serveur rapide qui aide dans l'interaction entre votre application que nous allons construire et le backend.

Donc c'est le cœur de Fast API, surtout que Fast API est un framework asynchrone, qui dépend fortement de la syntaxe async await.

Et donc l'utilisation d'un serveur ASGI était essentielle.

Donc la version est zéro.

Point 14.0.

Et aussi, j'aurai besoin de motor et motor est 2.4.

point zéro, qui est en fait un pilote MongoDB IO non bloquant complet.

Donc cela fonctionne pour Python en général.

Et cela fonctionne avec Fast API, bien sûr, dans notre cas, et cela fonctionne également avec son framework natif.

Tornador est également un framework asynchrone génial.

Et mature fonctionne avec toutes sortes d'applications async IO comme pilote MongoDB.

Donc c'est ce que fait matorral.

D'accord, donc allons-y et activons notre environnement virtuel, ou utilisez Pipi et V si vous n'avez pas installé been v, vous pouvez l'installer via pip install PIP in V.

D'accord, mais je l'ai déjà.

Donc je ne vais pas le faire.

Allons-y et activons cela en disant Pipi et V shell.

D'accord, super.

Maintenant nous avons notre environnement virtuel activé et le fichier PIP est créé.

Mais nous aurons toujours besoin d'installer les dépendances.

Donc ce que nous allons dire est Pipi et V install dash r requirements dot txt, right et appuyez sur Entrée.

Et fermons les requirements.

Nous n'en avons plus besoin.

Et j'aurai besoin de trois fichiers.

Le premier est main.py.

Donc main.py, j'aurai aussi besoin d'un fichier pour la base de données.

Donc nous l'appellerons database.pi.

Et le troisième pour le modèle, juste pour créer notre classe principale to do.

D'accord, donc allons-y et commençons par importer depuis fast API.

Je veux importer fast avec un F majuscule.

API tout en majuscules.

Et aussi je veux importer quelque chose de très important qui s'appelle course middleware.

Donc depuis fast API dot, middleware, dot course.

D'accord, je veux importer course middleware et course signifie cross origin resource sharing.

J'ai beaucoup parlé de cela dans tous nos projets Django, course fait référence à la situation lorsque votre client frontend qui s'exécute sur le navigateur, il a naturellement du code JavaScript.

Ce code JavaScript communique avec votre backend, dans notre cas communique avec notre serveur backend Fast API.

Et dans ce cas, le backend est dans une origine différente de celle du frontend.

Et les origines sont simplement la combinaison du protocole, du domaine et du port.

Donc vous pouvez voir ici que le protocole peut être soit HTTP ou HTTPS, le domaine, par exemple, notre localhost ou autre, et le port peut être n'importe quel port.

Donc React aura, par exemple, le port 3000.

Et notre Fast API aura un port de 8000.

Et nous aurons besoin d'une sorte de permission pour que le backend interagisse avec une origine différente, un port différent dans ce cas.

Donc c'est ce que nous allons faire.

D'accord, laissez-moi juste fermer cela.

Et instancions simplement la classe Fast API en créant un objet appelé app.

D'accord, donc c'est l'objet app.

Et ici je veux spécifier les origines.

Donc dans ce cas, localhost sur le port 3000 de React.

Et si vous ne faites pas cela, il n'y aura pas de connexion entre les deux, il n'y aura pas de permission, d'accord, pour les en-têtes, les méthodes, donc nous devrons autoriser les en-têtes et les méthodes.

D'accord, donc dans les origines, cela va être une liste avec https deux-points barre oblique barre oblique localhost deux-points 3000.

La prochaine chose que nous voulons faire est de prendre notre objet app, et nous voulons ajouter le middleware, add middleware, celui-ci, d'accord, donc cette méthode prendra tout d'abord, le course, middleware, course, middleware.

Ensuite, je veux autoriser les origines à être égales à la liste des origines.

De plus, les identifiants, nous les définirons à vrai, et je veux autoriser les méthodes, nous les définirons à tout ou étoile.

Et aussi nous voulons autoriser les en-têtes.

Et allons-y et créons une route de base.

Donc app app app, c'est la méthode get du créateur et tapez simplement une barre oblique, c'est une route vide.

Essentiellement, nous voulons créer une méthode ou une fonction, nous l'appellerons trade routes.

Et nous voulons retourner quelque chose comme, disons, ping pong.

D'accord, donc vérifions d'abord si la page principale fonctionne ou non.

Et pour exécuter le serveur, nous dirons UV corn main app.

Et je veux travailler en mode reload.

Donc vous n'avez pas à vous déconnecter du serveur et à vous reconnecter à nouveau, afin de voir les changements sur l'application.

Cela se produit instantanément une fois que vous actualisez la page.

D'accord, parfait.

Donc allons-y et ouvrons cela.

Et nous obtenons ping pong.

Maintenant, le truc cool avec Fast API est que vous pouvez accéder à ce document appelé swagger, swagger UI.

Et j'en ai beaucoup parlé dans tous mes projets Fast API sur la chaîne dans le cours, j'ai aussi une autre vidéo sur l'introduction à Fast API.

Et j'ai montré tout en détails sur l'interface utilisateur de Swagger, n'est-ce pas ? Donc assurez-vous de vérifier cela.

D'accord, super.

Donc c'est bien.

Mais c'est inutile pour nous, c'est juste pour s'assurer que le serveur répond.

Donc, essentiellement, dans l'application to do, nous avons besoin de quatre opérations principales, quatre opérations CRUD.

Donc nous devons lire tous les to dues, nous devrons poster un to do, mettre à jour et supprimer.

Et nous pouvons aussi obtenir un to do par ID, si vous voulez un to do spécifique, vous pouvez l'obtenir par son ID.

D'accord.

Donc travaillons sur cela très rapidement.

Minimisons cela pour l'instant et maximisons cela.

Donc nous avons un autre décorateur dot get.

Et ici nous voulons accéder à API slash to do, travaillons maintenant avec un code sink await.

Donc nous allons définir une méthode que nous appellerons get to do et ouvrir fermer parenthèse colonne.

Et pour l'instant, nous dirons return juste un.

Donc j'aurai besoin du même code de base pour le to do par ID.

Donc ici je veux avoir une entrée d'ID.

D'accord, donc j'ai besoin du to do par cet ID spécifique et je vais changer la méthode naturellement, donc nous allons dire get to do est le même par ID.

Et ici je vais passer l'ID comme paramètre ou entrée.

Je veux aussi poster un ID.

Donc c'est le même code que le get.

Mais au lieu de gap, nous allons changer cela en boast.

Et ici nous allons dire, post to do.

Et nous allons passer l'entrée comme to do, je veux aussi mettre à jour et supprimer, donc j'aurai besoin de deux fonctions de plus.

D'accord, je vais juste organiser un peu.

Donc ici, je veux mettre à jour le to do par son ID.

Donc j'aurai besoin d'entrer l'ID du to do que je souhaite modifier ou éditer.

Et ici je veux changer la méthode, je vais dire, put to do et au lieu de to do nous voulons l'ID car nous voulons que cet ID change.

Et je veux changer la valeur réelle de ce to do.

Et, dernier mais non des moindres, nous voulons supprimer notre to do, d'accord, donc, aussi to do par ID, si nous voulons accéder à un élément to do spécifique, et nous voulons le supprimer, donc j'ai besoin de spécifier l'ID pour cela.

Et ici, je vais changer la méthode, dire, delete.

Et au lieu de to do, je veux supprimer cet élément to do avec cet ID spécifique, le premier objet API n'a pas de Oh, désolé, put, il n'y a pas de requête HTTP appelée update, ou get post, put et delete.

D'accord, donc nous sommes prêts à partir.

Prenons en fait un aperçu de ce que nous avons.

Actualisons la page.

Et boom, nous avons toutes les méthodes que nous avons créées.

Donc nous avons get all to dues post ou to do get to do par ID, mais to do et delete to do.

D'accord, parfait.

Jusqu'à présent, tout va bien.

Maintenant, ce qu'ils veulent faire, c'est que je veux aller à model.py.

Et je veux importer depuis pedantic et pedantic aide en fait à créer automatiquement vos schémas JSON à partir du modèle.

Donc nous allons créer une classe maintenant.

Et cela fonctionne comme un mapper objet-relationnel.

Donc il prendra à partir du modèle, et nous nous connecterons avec notre base de données que nous allons créer dans une seconde.

Donc nous voulons importer la classe B's model, puis je veux créer une classe appelée to do avec Bayes model comme paramètre.

Et je veux deux choses seulement, je veux le titre, qui est une chaîne.

Et je veux une description, description, qui est aussi une chaîne.

Et c'est tout ce que j'ai besoin de faire.

Donc fermons model.py.

Et travaillons sur notre base de données maintenant.

Donc ici, ce que je veux faire est d'importer la classe to do depuis model.py.

Donc depuis model, je veux importer to do.

Et aussi je veux importer le module motor.

Donc import what or dot motor underscore a sync i O.

D'accord, donc c'est le pilote MongoDB.

D'accord, et laissez-moi juste ouvrir le MongoDB campus.

Donc tout sera clair pour vous les gars.

Mais en attendant, je veux créer un objet client.

Et cela va être égal à un Tor dot Mordor underscore a sink IO.

Et je veux accéder au modèle client async IO, celui-ci juste ici.

Et cela est essentiellement pour la connexion entre le database.pi et MongoDB.

Donc nous devrons passer une chaîne, MongoDB, deux-points, barre oblique barre oblique, et localhost deux-points 27, zéro 17, qui est le port par défaut pour MongoDB.

Comme nous l'avons dit avant, c'est une colonne.

D'accord, donc c'est une étape très importante.

Et nous avons notre MongoDB campus est prêt.

Mais nous allons le laisser pour l'instant.

Continuons.

Créons en fait la base de données que j'appellerai simplement une base de données.

Et cela va être égal à notre client dot notre base de données, appelons-la to do list et à l'intérieur de notre base de données, nous voulons créer la collection.

Donc notre collection, qui est la même chose qu'une table en SQL, donc la collection va être égale à la base de données.

Et nous voulons avoir un nom pour la collection.

Appelons-la simplement to do.

D'accord, donc nous avons une base de données appelée to do list.

Et nous avons une collection, qui s'appelle to do.

D'accord, super.

Maintenant, allons-y et travaillons sur nos fonctions principales.

Donc la première fonction que je veux créer ici est de récupérer un to do.

Donc nous allons dire un sink sourd, et je vais dire fetch one to do.

Et cela va prendre le titre comme entrée.

Et ici, le document va être égal à la collection dot find one.

Et je veux spécifier le titre pour qu'il soit égal à n'importe quel titre qui va être entré.

D'accord, donc le titre est défini sur n'importe quel titre ici.

et ici aussi, je veux attendre cela, d'accord, et ensuite je veux retourner ce document.

D'accord, donc c'est le premier get, donc nous voulons obtenir un to do.

Il n'y a aucun doute ici.

Donc pour obtenir un to do, nous l'obtenons par titre, et jetons un coup d'œil au modèle, c'est le titre ou l'ID, qui est défini dans notre fonction dans le fichier main.py.

D'accord.

Donc j'espère que c'est clair pour vous les gars.

Ensuite, je veux obtenir tous les to dues.

Donc nous allons dire def, fetch all to dues.

Et je ne veux aucun paramètre.

Et créons une liste de to dues.

Et déclarons une variable appelée cursor.

Et cursor va être égal à la collection dot une méthode appelée find.

Et ce que nous voulons faire essentiellement, c'est boucler sur n'importe quel document dans le cursor.

Donc utilisons à nouveau le mot-clé sink, pour document dans cursor, je veux développer dans la liste to dues, n'importe quel to do avec n'importe quel document.

D'accord.

Donc c'est essentiellement les données que je vais récupérer, et je veux tout retourner dans cette collection.

Et enfin, je veux retourner tous les to dues.

D'accord, donc n'oubliez pas que ce to do est la classe principale que nous avons définie dans le modèle.py.

La prochaine chose que nous voulons faire est de créer un to do, donc créons en fait un to do en trouvant la fonction create, to do.

Et ici nous voulons prendre to do comme paramètre principal ou entrée principale.

Donc le document va être égal au to do.

Et oops, qu'ai-je fait depuis lors, je veux déclarer une variable de résultat afin d'attendre que la collection insère ce document dans la collection.

Donc, euh, attendons que la collection insère un, c'est une méthode appelée insert one.

Et nous allons insérer n'importe quel document que nous allons créer, d'accord, n'importe quel post ou n'importe quel élément to do que nous allons créer.

Et aussi je veux retourner ce document.

Ensuite, nous voulons le mettre à jour, donc un sync.

def, et nous l'appellerons up date to do et cela prend le titre et la description.

D'accord, les deux sont définis dans la classe modèle dans le modèle.py dans la classe to do.

Oh, d'accord.

Et au fait, si vous vous demandez ce qu'est la méthode insert one, qu'est-ce que c'est ? Find aussi.

Ce sont des fonctions ou des méthodes MongoDB.

D'accord, donc nous écrivons en fait du code MongoDB à l'intérieur de notre fichier Python.

Donc le module motor qui est le pilote MongoDB nous aide à connecter le fichier database.py avec notre base de données MongoDB.

D'accord, donc revenons à notre code.

Donc attendez que la collection soit une autre méthode MongoDB appelée update one.

Donc comment fonctionne MongoDB, lorsque nous voulons mettre à jour un élément, nous voulons choisir un élément spécifique.

Et pour ce faire, nous aurons besoin d'avoir un critère.

Donc quel élément voulons-nous mettre à jour.

Dans ce cas, nous voulons choisir par le titre.

Donc le titre, quel que soit le titre défini, et ensuite, j'aurai l'élément réel que je veux mettre à jour.

Donc je veux utiliser l'opérateur set en utilisant le signe dollar set.

Cela est à l'intérieur des guillemets doubles.

Et cela est défini sur quelle que soit la description que je choisis, et la description réelle que je mets à jour.

Donc nous aurons un autre ensemble d'accolades.

Et ici je veux la description que j'ai choisie de mettre à jour pour la description réelle que je veux entrer ou mettre à jour.

D'accord, j'espère que vous suivez les gars, puis je veux rendre ce document ou retourner ces documents.

Donc je vais déclarer une autre variable appelée document pour attendre que la collection trouve un avec le titre qui correspond à cet élément que j'ai mis à jour, d'accord, et je retournerai ce document.

D'accord, donc c'est la mise à jour du to do.

La dernière méthode est de supprimer un to do.

Donc je vais l'appeler remove underscore to do.

Et il prend un titre comme paramètre.

Donc si nous voulons supprimer un élément, nous devons d'abord entrer le titre.

Et attendons que la collection supprime un, qui est une autre méthode MongoDB.

Et nous allons définir le titre pour qu'il soit égal à ce que nous avons entré comme titre.

Et nous voulons retourner une valeur booléenne.

Et nous allons la définir à vrai.

D'accord, super.

Donc sauvegardons cela.

Et allons-y dans main.pi afin de modifier ces fonctions que nous avons créées en fonction de ces fonctions dans le fichier de la base de données.

D'accord, donc c'est 3000, le port React JS, je veux aussi importer depuis fast API HTTP exception.

Et cela est juste pour les erreurs et les exceptions.

Donc en fait, cette classe, ce qu'elle fait, c'est qu'elle génère des informations d'exception pour nous.

D'accord, parfait, puis ce que je veux faire maintenant est d'importer depuis la base de données, toutes les fonctions que nous avons créées.

Donc allons en fait à database dot p y.

Et prenons cela d'ici, copions.

Donc c'est le premier.

D'accord, donc nous avons importé les fonctions depuis le fichier de la base de données.

Ensuite, ce que nous voulons faire est de travailler sur ces méthodes.

Et commençons par le get to do afin de retourner juste un, nous voulons avoir une réponse, n'est-ce pas.

Donc la réponse va être égale à un poids pour fetch all the to dues, qui est là vous allez.

D'accord, l'une de ces fonctions que nous avons créées dans database.pi.

Et vous pouvez voir ici que cela retourne en fait une coroutine.

D'accord, et j'ai beaucoup parlé des coroutines, du code concurrent, de la concurrency en général, dans différentes vidéos avant, je vais laisser tous les liens dans la description ci-dessous, vous pouvez les vérifier.

Donc nous voulons fetch all the two dues, et nous voulons retourner la réponse.

La deuxième fonction est to do par titre, donc nous allons substituer l'ID par le titre.

D'accord, et nous voulons que le modèle de réponse soit égal à la classe to do.

Donc le modèle de réponse est égal à la classe to do dans notre fichier model.py.

Ici aussi, au lieu de l'ID, nous voulons un titre.

Avoir aussi une réponse.

Et notre réponse va être égale à fetch want to do by title et n'oubliez pas le await.

Et je veux gérer les exceptions.

Donc je vais dire si la réponse si la réponse signifie si la réponse est vraie.

Nous n'avons aucune erreur.

Alors nous allons retourner la réponse.

Sinon, nous allons lever une exception HTTP.

Et cela va être 404.

Et le 404 est un code de statut pour page non trouvée, alors ce que nous voulons dire est qu'il n'y a pas d'élément to do avec ce titre.

D'accord, faisons en sorte que ce soit plus joli.

Donc mettons une chaîne de format.

Et retournons ce titre, quel que soit le titre que nous essayons de récupérer.

Donc passons à la fonction suivante, qui est le post to do, je veux aussi que le modèle de réponse soit égal à la classe to do.

Et ici, je veux définir le to do pour qu'il soit égal à la classe to do.

Et je veux prendre ce to do, jetez un coup d'œil, ici, nous avons défini le document à to do, et nous allons insérer un document dans la collection.

Donc c'est un JSON, mais nous voulons le convertir en dictionnaire.

Pour ce faire, nous allons déclarer une variable appelée réponse.

Et la réponse va être égale à la fonction Create to do que nous avons définie.

Et je vais prendre le to do et je vais le convertir en dictionnaire.

Et encore une fois, je veux une gestion des exceptions.

Donc réponse, puis retournée une réponse.

Sinon, je veux lever une exception HTTP.

Ici, nous allons dire que nous allons entrer 400.

Quelque chose s'est mal passé.

Au fait, 400 est le code de statut pour une mauvaise requête, d'accord, donc vous pouvez taper quelque chose s'est mal passé ou une mauvaise requête.

D'accord, la fonction suivante que nous voulons modifier est put to do, donc nous voulons changer l'ID par, changeons en fait tous les IDs par titre, nous prendrons aussi le modèle de réponse, et nous le définirons à la classe to do.

Et pour la fonction principale, nous voulons le titre, nous le définirons à string et aussi les données, nous les définirons à strength et date.

De plus, nous voulons le changer en description ou desk dans la base de données dans la fonction de mise à jour, vous voyez ici, titre et desk.

Donc la réponse va être égale à la fonction de mise à jour.

Et cela prend le titre et la description.

Et aussi cela veut une gestion des exceptions.

Donc encore une fois, nous pouvons prendre celle-ci, et nous allons la coller ici avec le même code de statut pour tous les quatre.

Et dernier mais non des moindres, nous avons la fonction Delete.

Donc supprimons cela.

Et ayons une réponse comme d'habitude.

Et nous prendrons la fonction Remove to do remove to do.

Et nous supprimerons l'élément par le titre.

Si vous vous souvenez ici, nous avons défini le titre et aussi je veux une gestion des exceptions.

Donc si la réponse est retournée est d'accord.

Nous voulons retourner un message disant que l'élément to do a été supprimé avec succès.

Sinon, nous voulons lever une exception, nous pouvons prendre celle-ci.

nous allons la coller ici.

Et c'est essentiellement tout.

Donc nous avons le lead, le put, les posts, get to do par le titre par ID, et get all to dues.

D'accord, cool.

Nous avons presque terminé avec notre côté base de données.

Maintenant, allons-y et vérifions l'interface utilisateur de Swagger ou les docs de Fast API, et comment nous pouvons le connecter à la base de données MongoDB.

Et nous verrons cette interaction avec le MongoDB campus.

D'accord, donc nous avons ici nos docs Fast API ou l'interface utilisateur Swagger, où nous pouvons interagir avec notre base de données.

Et j'ai de l'autre côté, mon Mongo campus est ouvert.

Et laissez-moi vous montrer jusqu'à ce que je sois connecté.

Laissez-moi me déconnecter pour le moment et vous montrer ce que j'ai fait.

Donc comme je vous l'ai montré au début du tutoriel, vous pouvez copier MongoDB deux-points barre oblique barre oblique localhost, n'est-ce pas ? Et vous connecter.

Et boom, vous êtes connecté.

Et ici vous avez la liste to do que nous avons créée.

Et c'est grâce au pilote MongoDB motor.

Donc essayons cela.

Allons-y et essayons de poster un to do.

Donc disons, to do item one.

Et dans la description, disons par exemple, promener le chien.

Exécuter, n'est-ce pas, sans avoir de problèmes.

Donc vérifions cela ici dans la liste to do.

To do.

Et boom, nous avons to do item one, promener le chien.

D'accord, réinitialisons, annulons, fermons cela.

Et vérifions ici dans le gap to dues, essayons cela.

Exécuter.

Et nous avons le même to do item one, promener le chien.

Avoir un autre, par exemple posts.

Et disons to do item deux, et ici, disons courir deux kilomètres.

D'accord, puis exécutons.

D'accord, cool.

Actualisons ici, et boom, to do item deux, courir deux kilomètres.

D'accord, donc cela fonctionne parfaitement, notre serveur backend Fast API interagit avec la base de données MongoDB.

D'accord, donc supprimons.

To do, cela devrait être le même que dans le titre.

Donc disons que je veux supprimer to do item deux.

Donc to do item espace deux exécuter.

D'accord, suppression réussie de l'élément to do.

Et si nous actualisons, il a disparu.

D'accord, dans la prochaine partie, nous allons passer à la création du frontend avec React js.

Bienvenue.

Donc comme notre backend fonctionne parfaitement et interagit avec le serveur MongoDB, nous allons maintenant avoir besoin de créer notre site frontend, et nous allons le faire communiquer avec le backend.

Donc allons-y et créons notre application React.

Et j'utiliserai create react app COI pour cela.

Mais avant, nous aurons besoin d'aller sur le bureau.

Et nous aurons besoin d'accéder au dossier farm stack underscore project.

D'accord, et juste pour être sûr que nous avons un seul dossier, qui est le backend.

Et maintenant nous pouvons utiliser cette commande NP x, qui signifie node package execute.

Et j'utiliserai create react app.

Et pour plus d'informations sur create react app, veuillez consulter la carte qui apparaîtra maintenant.

Et cela vous mènera à un tutoriel vidéo React et Django pour les développeurs backend.

Donc là, j'ai beaucoup parlé de create react app, ce que c'est et ce qu'il fait pour votre projet.

Ensuite, le nom du projet ou le nom du dossier, donc nous l'appellerons frontend.

Et l'installation du projet va prendre un certain temps.

Donc je vais mettre la vidéo en pause ici.

Et puis nous serons de retour quand tout sera terminé.

D'accord, cool.

Donc nous avons notre projet frontend prêt.

Pour l'exécuter, nous devons voir les deux frontend pour changer de répertoire vers le dossier frontend, puis NPM start.

D'accord, super.

Donc c'est l'application React par défaut, le serveur de développement est en cours d'exécution sur le port 3000, écoutant sur le port 3000.

Juste avant de continuer, j'ai juste besoin de quitter le serveur.

Et nous aurons besoin d'installer deux choses.

La première est axios.

Donc envoyer des requêtes du client au serveur et obtenir les réponses du serveur ou du serveur backend au client est le rôle d'axios.

De plus, nous avons besoin de bootstrap.

Donc bootstrap.

Et oui, c'est tout, oops, qu'ai-je fait npm install axios bootstrap.

D'accord, cool.

Donc allons-y et ouvrons l'application avec Visual Studio code.

Nous venons de laisser CD et d'ouvrir le dossier entier avec Visual Studio code.

D'ailleurs, ce j s hint me dérange depuis un certain temps.

Si vous avez le même problème ou si vous avez traité ce problème, veuillez me le faire savoir car j'ai installé GSN globalement, mais il semble que maintenant je pense que cela est vraiment arrivé.

Mais je pense que cela n'affectera pas notre projet.

Donc ignorons cela pour le moment.

Et allons-y et importons bootstrap slash dist slash CSS slash bootstrap, dot min dot CSS.

D'accord.

Juste pour importer bootstrap, c'est la première chose que nous devons faire index dot j s, d'accord.

Et c'est à peu près tout pour index dot j s, qui est le point d'entrée principal de notre application, app dot j, s quatre, nous allons passer la plupart du temps, je veux chillie me débarrasser de tout cela.

Et tapons simplement hello world.

formstack.

D'accord, cool.

Supprimons le logo, nous n'en avons pas besoin.

Donc même si vous avez ici, notre ligne rouge, ligne jaune, cela ne change vraiment rien.

Nous avons juste, c'est vraiment ennuyeux.

Si vous arrivez à connaître la solution pour cela, veuillez me le faire savoir dans la section des commentaires ci-dessous, car je n'ai vraiment pas pu trouver de solution appropriée pour résoudre ce problème.

Donc débarrassons-nous de tout.

Nous allons laisser l'application.

Laissez-moi en fait supprimer tout cela.

Et nous allons laisser l'application.

C'est le nom de la classe.

Pour l'application app.

Elle a un nom de classe d'application.

Donc ici nous aurons quelques paramètres généraux.

Donc l'alignement du texte, nous allons le laisser au centre.

marge, nous allons lui donner zéro, rembourrage, nous allons le définir à zéro, et famille de polices, nous allons utiliser celle-ci.

D'accord.

Et c'est tout.

Donc nous allons fermer le app dot CSS.

Et allons-y et travaillons sur le fichier app.

Donc je vais simplement supprimer cela.

Ou nous allons le laisser juste pour une vérification de santé mentale.

Donc avant de faire quoi que ce soit, nous aurons besoin d'importer react d'abord, n'est-ce pas, donc faites simplement cela plus grand pour vous les gars.

Donc nous allons importer react.

De plus, nous aurons besoin de deux fonctions use state et use effect depuis react.

Nous voulons aussi importer axios depuis axios.

Et aussi nous voulons importer le bootstrap.

Donc allons ici.

Nous allons importer bootstrap.

Travaillons d'abord sur le côté visuel, puis nous travaillerons sur la logique.

Donc allons-y et ayons une div avec un nom de classe d'application avec des éléments de liste de groupes.

Ce sont des classes bootstrap.

De plus, nous voulons justifier le contenu du centre, aligner les éléments du centre avec une marge horizontale définie sur auto.

Donc pour ajouter du style à JSX, nous aurons des doubles accolades et à l'intérieur vous pouvez entrer n'importe quel style que vous voulez.

Donc je veux définir la largeur à 400 pixels.

Et aussi je veux que la couleur de fond soit blanche, et la marge supérieure à 15 pixels.

Et à l'intérieur de la div, j'aurai un titre avec une balise h1, nous l'appellerons Task Manager.

D'accord, super.

Donc cela a un nom de classe de carte avec un texte blanc, un fond primaire, qui est le bleu et une marge inférieure définie à un en dessous du gestionnaire de tâches, je veux ajouter une balise h6 avec trois mots fast API, react et MongoDB.

Ensuite, j'aurai une autre div avec un nom de classe de corps de carte.

À l'intérieur de ce Dave principal, je veux avoir une balise h5 avec un nom de classe de carte et je vais dire ajouter votre tâche.

Cela a un fond sombre avec une marge inférieure de trois, et le texte est blanc pour avoir le contraste.

La prochaine chose que je veux faire est de créer deux champs de saisie, l'un pour le titre et l'autre pour la description et un bouton Ce bouton est pour ajouter votre tâche.

Donc pour ce faire, je vais envelopper tout autour d'un span, ce span aura un nom de classe de texte de carte.

Donc c'est le premier champ de saisie et c'est le deuxième champ de saisie pour la description.

Donc les deux ont MB deux ou marge inférieure deux avec contrôle de formulaire avec différents noms, titre in et d s in et les deux ont des placeholders, un avec titre et l'autre avec description.

Le prochain élément dans notre application est le bouton Ajouter une tâche.

Donc il a un nom de classe de btn avec btn outline primary.

D'accord, donc je lui ai donné un rayon de bordure avec 50 pixels pour lui donner cette forme arrondie autour du bouton.

Et aussi défini le poids de la police à gras.

Et c'est tout ce qui est à l'intérieur du span.

Donc l'idée ici est que lorsque vous allez entrer le titre et la description, et que vous allez ajouter la tâche, la tâche apparaîtra en dessous ici avec un seul bouton, qui est le Supprimer en dessous du span.

Et sur la même ligne que la balise h5 ajouter votre tâche, je veux ajouter une autre balise h5 avec vos tâches, donnons en fait au bouton une marge inférieure afin d'avoir un peu d'espace.

Donc MB, nous allons la définir à deux, c'est mieux.

Et ensuite ce que nous voulons faire est d'afficher toutes vos tâches à faire en dessous de vos tâches.

D'accord, donc ayons une div.

À l'intérieur de cette div, nous devrions brancher tous nos éléments à faire.

Et cela devrait être un composant externe.

Et en bas ici, je veux créer une marque de copyright.

Et vous êtes libre de changer les couleurs si vous le souhaitez.

Bien sûr, cela a un fond d'avertissement, qui est le jaune, n'est-ce pas ? Avec une classe de card decks dark BG warning, padding why sur l'axe vertical avec un et marge inférieure de zéro, ne pas oublier de supprimer ce Dave en dessous.

Et celui-là, parce que je l'ai réécrit.

D'accord.

Donc c'est la même chose.

Une fois que nous sauvegardons, rien ne changera.

D'accord, donc avant de continuer et de créer notre dossier de composants avec les différents composants, il y a quelques choses que nous devons faire dans notre fonction.

La première chose que nous devons faire est de créer différentes variables, une pour la liste des tâches à faire, une pour le titre, et une autre pour la description, et toutes seront définies à use date.

Donc set to do list sera défini à use date avec un tableau d'objet vide.

Et à l'intérieur, nous allons ajouter les éléments chaque fois que vous allez ajouter une tâche.

De plus, nous allons définir le titre.

Et nous utiliserons l'état pour juste anti strained, rien pour le moment, la même chose s'applique à la description.

Et une fois que vous ajoutez un titre et une description, cliquez sur Ajouter une tâche, tout ici va changer.

Donc c'est l'utilité de la fonction use state.

La prochaine chose que nous voulons faire est de lire toutes les tâches à faire, pour cela j'utiliserai la méthode use effect.

Et nous utiliserons use effect afin d'accepter les méthodes de requête HTTP comme get post et ainsi de suite.

Donc la première chose que nous voulons faire est de lire toutes les tâches à faire.

Et cela, ce que nous allons faire, c'est qu'il va envoyer une requête get au serveur backend Fast API, d'accord, puis, ce callback va retourner une promesse et nous gérons les promesses avec cela, puis, en ayant une réponse comme entrée, nous devrions accéder à toutes les données à l'intérieur de cette entrée, ou la réponse.

D'accord, et tout cela est enveloppé à l'intérieur du set to do list que nous avons défini ici au-dessus.

Et la dernière chose dont nous avons besoin ici est de poster une tâche à faire, en fait, lorsque nous cliquons sur le bouton Ajouter une tâche.

Donc cette variable add to do handler, qui est définie à une fonction de rappel, qui ne prend rien comme entrée, retourne cette requête post.

Donc le premier paramètre est l'origine.

Donc HTTP localhost Port 8000 pour l'API et to do, et nous voulons afficher le titre pour quel que soit le titre, et la même chose pour la description.

Et puis nous avons un rappel comme réponse qui va pour la réponse comme entrée, et nous pouvons console log rez ou nous pouvons juste alerter rez, c'est juste pour une étape de vérification.

Maintenant, nous allons avoir besoin de mettre à jour les deux champs de saisie et le bouton Ajouter une tâche.

D'accord, donc le premier champ de saisie qui concerne le titre, nous allons le mettre à jour avec l'attribut on change, cela prend un événement comme paramètre, puis il retourne set title que nous avons défini ici au-dessus et à l'intérieur du set title nous avons un paramètre de event dot target dot value, la même chose exacte s'applique à l'entrée.

Donc l'entrée aussi nous allons avoir l'attribut on change avec un événement qui définit la description pour event dot target dot value.

Dernier mais non des moindres, nous avons le bouton donc pour le bouton nous avons apt to do handler function ici.

Donc le bouton devrait être mis à jour afin de refléter les changements qui se produiront lorsque nous cliquerons sur le bouton.

Et n'oubliez pas de réajouter la marge inférieure trois afin de pousser vos tâches un peu plus bas.

Donc c'est à peu près tout ce que nous devons faire pour Abdo j s, la dernière chose que nous devons faire est d'ajouter les éléments à faire à l'intérieur des deux balises div.

Donc allons-y vers notre dossier source.

Et créons un dossier appelé composants.

Et à l'intérieur des composants, je vais créer un fichier que j'appellerai to do dot j s, et un autre fichier appelé to do list view dot j s To Do List View dot j s.

Tout d'abord, allons à to do et importons axios et react.

Maintenant, je veux créer une fonction to do item qui prendra comme paramètre props.

À l'intérieur de cette fonction, je vais déclarer une variable appelée Delete to do handler, et je vais définir cela à une fonction de rappel qui prend le titre comme paramètre afin de supprimer n'importe quel élément to do que nous voulons spécifier par le titre.

Et ce que nous voulons retourner en fait, c'est l'élément lui-même.

Et à côté de cet élément, nous aurons un bouton de suppression.

Donc vous pouvez voir ici nous avons une div avec un paragraphe span avec un style.

Et nous allons entrer ou nous allons brancher le props.to do dot title.

Donc le titre d'abord, et cela va être en gras, puis un deux-points, et ensuite nous voulons avoir la description à côté.

Et puis après nous aurons un bouton avec l'attribut onClick qui va être défini à une fonction de rappel qui ne prend rien comme paramètre, et il retournera à la fonction lead to do handler que nous avons créée ci-dessus.

Encore une fois, il prendra props.to do the title.

Et pourquoi est-ce parce que nous voulons rechercher cet élément en fonction du titre.

Donc le critère principal pour la suppression est le titre, aussi nous aurons un nom de classe avec un bouton.

Et tout cela est à nouveau des classes bootstrap.

Donc maintenant nous avons notre to do dot j s prêt, nous voulons l'importer dans le to do list views dot j s.

Mais avant de faire cela, nous devons d'abord l'exporter le to do item.

D'accord, afin de l'importer dans le to do list view dot j s, donc nous allons importer le to do item depuis le répertoire courant.

Où se trouve le to do dot j s.

D'accord, et ensuite j'aurai besoin de la fonction que je vais brancher à l'intérieur de mon app dot j s ici.

Donc tous les éléments qui apparaîtront en dessous doivent être créés dans notre to do ListView dot j s.

Donc allons-y et créons cette fonction, nous l'appellerons to do view et il prend props comme paramètre.

Et ce qu'il retournera simplement une ul ou une liste non ordonnée.

Et le props.to do list dot map qui est l'une des méthodes de tableau comme reduce filter et sort.

Et nous allons mapper n'importe quel to do et le brancher à l'intérieur de ce to do item.

Donc ce to do item que nous avons importé depuis le to do dot j s ici.

D'accord, donc c'est comment cela fonctionne.

Et n'oublions pas de l'exporter.

Donc pour tester tout ensemble, allons-y et ouvrons notre serveur backend.

Donc nous allons à backend.

Et UV corn main app load.

D'accord, bien.

Donc il écoute sur le port 8000.

Donc si nous allons actualiser la page.

D'accord, cool.

Rendons cela un peu plus grand, il y a quelque chose de très important que nous avons oublié de faire, c'est d'importer la vue to do depuis la liste to do.

D'accord, donc nous allons avoir besoin de faire cela en dessous de bootstrap.

Et maintenant, au lieu de ce commentaire, nous allons ajouter notre élément to do réel.

D'accord, parfait.

Donc nous avons notre frontend qui s'exécute sur cette instance du terminal.

Et nous aurons aussi besoin d'ouvrir une nouvelle instance de terminal pour le backend.

Donc unicorn main app, reload.

D'accord, super.

Donc ouvrons notre swagger Fast API.

D'accord, donc pour le moment, notre base de données ne contient aucune donnée.

Donc cette collection n'a pas de données, comme vous pouvez le voir ici dans le rapport MongoDB.

De ce côté, nous avons notre serveur backend, notre serveur Fast API.

C'est l'application React, notre client, et ici nous avons notre serveur de base de données, notre serveur de base de données MongoDB.

Donc essayons d'ajouter un élément to do.

Donc nous allons dire to do one, étudier le langage rust.

À la demande, ambu to do one étudier le langage rust.

D'accord, et si nous allons actualiser ici, nous aurons ce document créé dans notre base de données.

Donc nous aurons un ID, qui est très similaire à la clé primaire dans le monde SQL.

Cela est généré automatiquement par MongoDB.

Nous aurons notre titre et notre description.

D'accord, essayons d'en ajouter un autre, to do deux, courir 10 kilomètres à la tombée de la nuit, dusk, actualiser, le même sommeil à 21h, ajouter une tâche, actualiser, et ainsi de suite.

Donc vous pouvez voir ce qui se passe.

Il va supprimer, disons, to do deux, le supprimer d'ici, actualiser, il va disparaître.

Ajoutons-en un autre.

Donc disons to do for sketching at dusk.

Donc il ajoute en dessous.

Et si vous allez dans le backend, vous trouverez les mêmes informations.

Donc essayons d'accéder à l'API slash to do et vous trouverez toutes nos tâches à faire.

D'accord, tout ici.

De même dans les docs, lorsque vous cliquerez sur get to do, essayez-le maintenant ou essayez-le.

Exécuter, vous trouverez vos tâches à faire.

Ce format JSON et actualisons cela aussi.

Donc pour être identique, d'accord, donc c'était une introduction à la pile FARM et comment nous pouvons travailler avec les trois technologies.

Si vous avez aimé la vidéo, veuillez l'aimer, la partager et vous abonner à la chaîne.

Et j'apprécie votre soutien, les gars.

Merci beaucoup.

Si vous avez des questions, veuillez me le faire savoir dans la section des commentaires ci-dessous.

Prenez soin de vous.