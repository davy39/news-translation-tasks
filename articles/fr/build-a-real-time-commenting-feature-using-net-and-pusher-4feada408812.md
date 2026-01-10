---
title: Créer une fonctionnalité de commentaires en temps réel avec .NET et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:07:25.000Z'
originalURL: https://freecodecamp.org/news/build-a-real-time-commenting-feature-using-net-and-pusher-4feada408812
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dk8lZiI7UJOq2eLs.gif
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Créer une fonctionnalité de commentaires en temps réel avec .NET et Pusher
seo_desc: 'By Ogundipe Samuel

  Today, we will build a mini-blog engine with live commentary features using .NET
  and Pusher.


  Reloading pages to view new comments can bore and is also strenuous, given you don’t
  even know if the reply to your comment has come in y...'
---

Par Ogundipe Samuel

Aujourd'hui, nous allons créer un mini-moteur de blog avec des fonctionnalités de commentaires en direct en utilisant .NET et Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dk8lZiI7UJOq2eLs.gif)

Recharger les pages pour voir les nouveaux commentaires peut être ennuyeux et également fastidieux, d'autant plus que vous ne savez même pas si la réponse à votre commentaire est arrivée ou non. Vous continuez à recharger et à gaspiller vos données. En bref, les utilisateurs peuvent abandonner les sites où ils doivent recharger les pages pour voir un nouveau commentaire.

Pour suivre ce tutoriel, nous utiliserons MSSQL comme moteur de base de données. Veuillez vous assurer qu'il est opérationnel.

Pour suivre ce tutoriel, veuillez vous assurer que vous êtes familiarisé avec les bases de :

### Configuration d'un compte et d'une application Pusher

[Pusher](https://pusher.com/) est un service hébergé qui facilite l'ajout de données et de fonctionnalités en temps réel aux applications web et mobiles.

Pusher agit comme une couche en temps réel entre vos serveurs et vos clients. Pusher maintient des connexions persistantes avec les clients (via WebSocket si possible, et en basculant vers une connectivité basée sur HTTP) afin que, dès que vos serveurs ont de nouvelles données qu'ils souhaitent envoyer aux clients, ils puissent le faire via Pusher.

Si vous n'en avez pas déjà un, rendez-vous sur Pusher et créez un compte gratuit.

Nous allons enregistrer une nouvelle application sur le tableau de bord. Les seules options obligatoires sont le nom de l'application et le cluster. Un cluster représente l'emplacement physique du serveur Pusher qui gérera les requêtes de votre application. Copiez également votre ID d'application, votre clé et votre secret depuis la section des clés de l'application, car nous en aurons besoin plus tard.

### Configuration du projet Asp.Net dans Visual Studio

La prochaine chose que nous devons faire est de créer une nouvelle application `Asp.Net MVC`.

Pour ce faire, procédons comme suit :

* Ouvrez `Visual Studio` et sélectionnez `Nouveau Projet` dans la barre latérale
* Sous les modèles, sélectionnez `Visual C#`
* Ensuite, sélectionnez `Web`
* Dans la section centrale, sélectionnez `Application Web ASP.NET`
* Pour ce tutoriel, j'ai nommé le projet : `Real-Time-Commenting`
* Maintenant, nous sommes presque prêts. La prochaine étape sera d'installer la bibliothèque officielle `Pusher` pour `ASP.NET` en utilisant le `NuGet Package`

Pour ce faire, nous allons dans les outils de la barre supérieure, cliquons sur `Gestionnaire de packages NuGet`, dans le menu déroulant, nous sélectionnons `Console du gestionnaire de packages`.

Nous verrons la `Console du gestionnaire de packages` en bas de notre Visual Studio. Ensuite, installons le package en exécutant :

### Création de notre application

Maintenant que notre environnement est configuré et prêt, plongeons dans l'écriture de code.

Par défaut, Visual Studio crée trois contrôleurs pour nous. Mais nous utiliserons le HomeController pour la logique de l'application.

La première chose que nous voulons faire est de définir un modèle qui stocke la liste des articles que nous avons dans la base de données. Appelons ce modèle `BlogPost`. Alors, créons un fichier appelé `BlogPost.cs` dans notre dossier models, et ajoutons :

Dans ce bloc de code, nous avons défini le modèle qui contient nos articles de blog. Les propriétés que nous avons définies ici incluent :

* L'id de l'article, appelé `BlogPostID` (généralement la clé primaire).
* Le titre de notre article, appelé `Title` (définis comme une chaîne)
* Le corps de l'article que nous allons créer (définis comme une chaîne)

Ensuite, créons le modèle appelé `Comment`, que nous avons référencé précédemment. Créons un fichier appelé `Comment.cs` dans notre dossier models et ajoutons :

En regardant le code ci-dessus, nous remarquons que nous avons déclaré les propriétés suivantes :

* L'ID de notre commentaire appelé `CommentID` (généralement la clé primaire)
* Le nom de la personne commentant
* Le corps du commentaire
* L'ID de l'article sur lequel nous commentons

Maintenant que nous avons défini notre modèle, référençons-le dans notre contexte de base de données par défaut appelé `ApplicationDbContext`.

Pour ce faire, ouvrons le fichier `models\IdentityModels.cs`. Localisons la classe appelée `ApplicationDbContext` et ajoutons ce qui suit après la fonction create :

Dans le bloc de code ci-dessus, la classe `DbSet` représente un ensemble d'entités utilisé pour les opérations de lecture, de mise à jour et de suppression.

Ici, nous avons défini deux entités, nos modèles `BlogPost` et `Comment`. Nous aurons maintenant accès à eux à partir d'une instance de `ApplicationDbContext`.

### Connexion à notre base de données

Bien que notre modèle soit configuré, nous devons encore attacher une base de données à notre application. Pour ce faire, sélectionnez l'Explorateur de serveurs sur le côté gauche de notre Visual Studio, cliquez avec le bouton droit sur Connexions de données et ajoutez une base de données. Il existe diverses bases de données qui sont légères et peuvent s'intégrer dans l'application que nous construisons, telles que :

* Base de données Microsoft Access
* Base de données Sqlite
* Serveur MSSQL

Pour ce tutoriel, j'ai utilisé le serveur MSSQL.

### Création de notre contrôleur

Maintenant que notre modèle et notre base de données sont configurés, créons notre route d'index. Ouvrez le `HomeController` et remplacez-le par :

Dans le bloc de code ci-dessus, nous avons défini six fonctions différentes :

* La fonction `Index`, qui affiche une liste rapide de tous nos articles de blog
* La fonction `Create`, qui gère l'ajout de nouveaux BlogPosts pour les requêtes `GET` et `POST`
* La fonction `Details`, qui retourne la vue complète de notre article
* La fonction `Comments`, qui retourne les données JSON de tous les commentaires pour un article particulier
* La fonction `Comment`, qui gère l'ajout d'un nouveau commentaire et l'émission des données à Pusher.

Avant de regarder nos fonctions de contrôleur, nous remarquons qu'il y a une importation de notre contexte de base de données dans notre classe avec la ligne qui dit :

Cela permet d'accéder au modèle de base de données que nous avons défini dans notre classe `ApplicationDbContext`.

Dans la fonction `Index`, nous retournons notre vue, en passant une liste de tous les articles que nous avons dans notre base de données, qui sera parcourue.

Ensuite, dans la fonction `Create` qui gère notre requête `GET`, nous retournons simplement la vue pour créer un nouvel article.

Nous passons à la fonction `Create` qui gère notre requête `POST`, qui reçoit un argument appelé `post` de type `BlogPost`. Dans cette fonction, nous ajoutons un nouveau `post` dans la base de données, après quoi nous retournons une redirection vers notre fonction `Index`.

Dans notre fonction `Details`, nous retournons une instance d'un `post` particulier à notre vue qui sera affichée. Cette vue affichera également le formulaire qui nous permet d'ajouter des commentaires.

Dans notre fonction `Comments`, nous retournons tous les `comments` qui appartiennent à un `post` particulier, dont l'ID a été fourni en JSON. Cette méthode sera appelée via un POST AJAX.

Enfin, notre fonction `Comment` gère l'ajout des commentaires à la base de données et l'envoi des données à Pusher. Nous remarquons ici que cette fonction est une méthode `async`. Cela est dû au fait que la bibliothèque Pusher envoie les données de manière asynchrone, et nous devons attendre sa réponse.

De plus, nous devons remplacer `XXX_APP_CLUSTER`, `XXX_APP_ID`, `XXX_APP_KEY` et `XXX_APP_SECRET` par notre cluster d'application, ID, clé et secret que nous avons obtenus de Pusher précédemment.

### Création de nos fichiers de vue

Pour compléter notre application, nous aurons besoin de 3 fichiers de vue différents, que nous discuterons ci-dessous.

#### **La vue d'index**

Remplaçons le contenu par défaut dans le fichier `Index.cshtml` à `Views\Home\Index.cshtml` par :

En regardant la structure HTML ci-dessus, nous remarquons que nous avons défini un tableau qui liste tous nos articles et les lie à la page des détails.

#### **La vue de création**

Ici, nous devons créer un nouveau fichier appelé `Create.cshtml` dans le dossier `View\Home` et coller ce qui suit :

Dans la structure HTML ci-dessus, nous avons trois entrées principales :

* Un élément d'entrée de texte, qui contient le titre de l'article
* Un élément d'entrée de texte, qui contient le contenu de l'article
* Un élément de bouton, qui est utilisé pour soumettre la nouvelle entrée

**La vue des détails et les liaisons Vue**

C'est le dernier fichier de vue dont nous aurons besoin. Ce fichier gère également la liaison aux événements Pusher et la mise à jour des commentaires en temps réel en utilisant Pusher et Vue. Créons un nouveau fichier appelé `Details.cshtml` dans notre dossier `Views\Home` et ajoutons le contenu suivant :

[https://gist.github.com/755c0e5e8cbf53dbb9560deafdd50a21](https://gist.github.com/755c0e5e8cbf53dbb9560deafdd50a21)

Dans le bloc de code ci-dessus, nous avons affiché le titre et le contenu de l'article actuel, ainsi que **le nombre de commentaires** qu'il a.

Nous avons également créé notre formulaire de commentaire qui comprend trois éléments principaux, qui sont :

* Entrée de texte pour le nom de la personne faisant le commentaire
* Zone de texte pour le corps du commentaire
* Bouton pour enregistrer le nouveau commentaire dans la base de données

Remarquez que nous avons utilisé la directive `v-for` de Vue pour itérer et afficher les commentaires disponibles.

De plus, notez que nous avons inclus certaines bibliothèques requises telles que :

* bibliothèque JavaScript axios
* bibliothèque JavaScript Vue js
* bibliothèque JavaScript Pusher

#### **Liaisons Pusher et extrait Vue**

Ci-dessous se trouve notre exemple d'extrait Vue utilisé pour gérer la soumission des commentaires et les mises à jour en temps réel de Pusher.

Dans le bloc de code ci-dessus, nous avons effectué deux activités principales, qui sont :

#### **Code de téléchargement des commentaires**

Pour traiter les nouveaux commentaires du côté client vers le serveur, les étapes suivantes ont été suivies :

* Nous avons attaché un écouteur d'événements Vue `@click` à notre bouton de soumission qui déclenche une méthode appelée `submit_comment`
* Nous avons défini une fonction appelée `submit_comment` qui utilise `axios` pour faire une requête POST à notre fonction `comment`

#### **Abonnement aux ajouts de flux sur le serveur depuis d'autres clients**

Après que le commentaire a été envoyé au serveur, une requête est envoyée à Pusher pour retourner un événement avec les nouvelles données que nous avons diffusées. Pour écouter ces événements en temps réel, nous avons :

* Initialisé un objet Pusher tout en passant notre clé d'application et notre cluster
* Souscrit à notre canal appelé `asp_channel`
* Dans la méthode d'écoute dans notre code Vue, nous avons déclaré une liaison à notre événement appelé `asp_event`. Dans la fonction de rappel de cette liaison, nous poussons les nouvelles données à notre liste de commentaires

C'est tout ! Maintenant, une fois qu'un nouveau commentaire est fait, il est également diffusé et nous pouvons écouter en utilisant notre canal pour mettre à jour les commentaires en temps réel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*d-b_bCTehgAMknrK.gif)

### Conclusion

Dans cet article, nous avons couvert comment créer une fonctionnalité de commentaires en direct en utilisant .NET et Pusher, et créer un mini moteur de blog en .NET.

La base de code de ce tutoriel est disponible dans un [dépôt public Github](https://github.com/samuelayo/Net_real_time_commenting_pusher). Vous pouvez la télécharger à des fins éducatives. Avez-vous des réserves ou des commentaires, faites-nous savoir vos retours dans les commentaires.

Cet article a été publié à l'origine par l'auteur sur le blog de Pusher [ici](https://blog.pusher.com/build-a-realtime-commenting-feature-using-net-and-pusher/)