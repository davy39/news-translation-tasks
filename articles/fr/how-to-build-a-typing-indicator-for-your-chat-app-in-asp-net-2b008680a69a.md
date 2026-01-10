---
title: Comment créer un indicateur de frappe pour votre application de chat en ASP.NET
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-20T20:33:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-typing-indicator-for-your-chat-app-in-asp-net-2b008680a69a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J_Fz1VhdsJ4gkkyGUKjnMg.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un indicateur de frappe pour votre application de chat en
  ASP.NET
seo_desc: 'By Neo Ighodaro


  A basic understanding of ASP.NET and jQuery is needed to follow this tutorial.


  When you’re using a chat app, knowing when the person you are chatting with is typing
  a message can improve your user experience. It gives you some feedb...'
---

Par Neo Ighodaro

> Une compréhension de base d'ASP.NET et de jQuery est nécessaire pour suivre ce tutoriel.

Lorsque vous utilisez une application de chat, savoir quand la personne avec qui vous discutez est en train de taper un message peut améliorer votre expérience utilisateur. Cela vous donne un retour que vous n'êtes pas seul dans la conversation et qu'un message est en route.

Dans ce tutoriel, nous allons passer par quelques étapes simples pour créer cette fonctionnalité en utilisant C#, .NET et Pusher.

À la fin de ce tutoriel, nous aurons quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/rwOg-HkLtiydf-37RuU7DvGykJJyt8fz-P4P)

Ce tutoriel suppose une connaissance préalable de :

* C#
* .NET MVC
* JavaScript (jQuery)

Lorsque vous êtes prêt, commençons.

### Installation de notre projet

Nous utiliserons [Visual Studio](https://www.visualstudio.com/), qui est un IDE populairement utilisé pour construire des projets .NET. Visual Studio 2017 est gratuit et disponible pour la plupart des systèmes d'exploitation. Vous pouvez consulter les détails d'installation [ici](https://www.visualstudio.com/).

Après avoir installé Visual Studio, lancez-le et créez un nouveau projet en cliquant sur **Nouveau Projet** depuis le tableau de bord. En suivant l'assistant **Nouveau Projet**, nous :

* Définissons C# comme notre langage
* Sélectionnons le projet .NET MVC comme modèle
* Remplissons le nom du projet (par exemple "HeyChat" — mais n'importe quel nom fera l'affaire)
* Remplissons le nom de la solution (c'est-à-dire le nom de l'application — "HeyChat" ou n'importe quel nom fera l'affaire).

![Image](https://cdn-media-1.freecodecamp.org/images/wHa3qOf05-fbAXL-Ea06A5GNCKi3nJeGoiYq)

### Écriture du code côté serveur (C#)

Pour afficher un indicateur de frappe, notre application de chat doit être capable de reconnaître qui est en train de taper à un moment donné. Pour cela, nous allons ajouter une forme limitée d'identification. Nous ne faisons aucune authentification du tout, car ce tutoriel ne l'exige pas.

> _? Pour les besoins de ce tutoriel, nous supposerons que ce chat est ouvert à tous les utilisateurs. Tout ce qui sera requis est que nos utilisateurs spécifient leurs noms à la première entrée._

### Définition des routes

Nous pouvons définir certaines des routes dont nous avons besoin pour créer cette fonctionnalité, qui sont :

* Une route d'accueil qui rend la première page qui prend le nom de l'utilisateur.
* Une route de connexion qui accepte une requête `POST` du nom de l'utilisateur.
* Une route de chat qui rend la vue de chat.

> _? Nous pourrions avoir besoin d'autres routes au fur et à mesure, mais cela suffit pour commencer._

Pour ajouter ces routes, nous ouvrons le fichier `RouteConfig.cs` dans le répertoire `App_Start` de notre application. Et dans celui-ci, nous ajoutons les routes que nous avons définies.

```
routes.MapRoute(        name: "Home",        url: "",        defaults: new { controller = "Home", action = "Index" }    );
```

```
    routes.MapRoute(        name: "Login",        url: "login",        defaults: new { controller = "Login", action = "Index" }    );
```

```
    routes.MapRoute(        name: "ChatRoom",        url: "chat",        defaults: new {controller = "Chat", action="Index"}    );
```

En utilisant la route **Home** comme exemple, la définition de la route indique que les requêtes `/` seront gérées par le `HomeController` qui se trouve dans le fichier `Controllers/HomeController.cs` et la méthode `Index` de ce contrôleur. Ensuite, nous créerons les contrôleurs dont nous aurons besoin.

### Création des contrôleurs et des méthodes d'action

Pour créer un nouveau contrôleur, faites un clic droit sur le répertoire **Controller** et sélectionnez `Ajouter → Contrôleur`. Dans le formulaire résultant, nous tapons le nom de notre contrôleur et sélectionnons le modèle vide.

> _? Lorsque notre application est créée, elle inclut un HomeController avec une méthode d'action Index par défaut, donc nous effectuerons les étapes ci-dessus pour créer notre LoginController et ChatController._

Dans notre classe LoginController, nous créons la méthode d'action Index en spécifiant `[HttpPost]` en haut de la méthode d'action pour indiquer qu'elle gère les requêtes `POST`.

```
public class LoginController : Controller    {        [HttpPost]        public ActionResult Index()        {
```

```
        }    }
```

L'action Index du LoginController recevra la charge utile de la requête, lira le nom d'utilisateur de la charge utile et l'assignera à la session utilisateur actuelle. Ensuite, elle redirigera notre utilisateur vers la page de chat. Lorsque nous ajoutons cela à notre méthode d'action, nous aurons :

```
public class LoginController : Controller    {        [HttpPost]        public ActionResult Index()        {            string user = Request.Form["username"];            if (user.Trim() == "") {                return Redirect("/");            }            Session["user"] = user;            return Redirect("/chat");        }    }
```

> _? Dans une application de chat réelle, nous ajouterions l'utilisateur à une base de données et le marquerions comme connecté afin que les autres utilisateurs puissent voir les options de chat disponibles. Mais cela dépasse le cadre de ce tutoriel, donc l'ajout à une session suffira._

Dans notre classe ChatController, nous ajouterons la méthode d'action Index. L'action Index du ChatController rendra notre vue de chat et transmettra l'utilisateur actuel à la vue.

```
public class ChatController : Controller    {        public ActionResult Index()        {            if (Session["user"] == null) {                return Redirect("/");            }
```

```
            ViewBag.currentUser = Session["user"];
```

```
            return View ();        }    }
```

> _? Par défaut, les méthodes d'action gèrent les requêtes G`ET`, donc nous n'aurons pas besoin d'ajouter [`HttpGet]` en haut de notre méthode. Nous avons également ajouté une vérification simple pour empêcher l'accès à la page de chat s'il n'y a pas d'utilisateur connecté._

N'oublions pas notre route Home. Dans le HomeController, nous ajouterons le code pour rendre la page d'accueil.

```
public class HomeController : Controller    {        public ActionResult Index()        {            if ( Session["user"] != null ) {                return Redirect("/chat");            }
```

```
            return View();        }    }
```

> _? Nous avons également ajouté une petite vérification pour empêcher les connexions multiples dans la même session utilisateur._

À ce stade, nous avons créé les contrôleurs et les méthodes pour servir nos vues (que nous n'avons pas encore créées), donc essayer de lancer cela vous donnera quelques erreurs ! Corrigons cela.

### Implémentation des vues de l'application

Sur la base des routes que nous avons définies jusqu'à présent, nous aurons besoin de deux vues :

* La vue de la page d'accueil avec le formulaire de connexion — servie par la méthode d'action `Index` de la classe `HomeController`
* La vue de chat où la fonctionnalité d'indicateur de frappe sera visible — servie par la méthode d'action `Index` de la classe `ChatController`

#### Page d'accueil/page de connexion

Pour notre page d'accueil, nous créerons une page avec un formulaire qui demande le nom d'utilisateur de l'utilisateur et lui montre un bouton pour soumettre la connexion. En référence à notre code de contrôleur :

```
public class HomeController : Controller    {        public ActionResult Index()        {            if ( Session["user"] != null ) {                return Redirect("/chat");            }            return View();        }    }
```

> _? La fonction V**iew** crée une réponse de vue que nous retournons. Lorsque V**iew()** est invoquée, C# recherche la vue par défaut de la classe de contrôleur appelante. Cette vue par défaut est le fichier i`ndex.cshtml` trouvé dans le répertoire V**iews**, dans un répertoire portant le même nom que le contrôleur. C'est-à-dire que la vue par défaut de la classe HomeController sera le fichier V`iews/Home/index.cshtml`._

Pour créer notre vue par défaut de `HomeController`, nous :

* Faisons un clic droit sur le répertoire Views et sélectionnons `Ajouter un nouveau dossier`,
* Remplissons **Home** comme nom de dossier,
* Faisons un clic droit sur le dossier **Home** nouvellement créé et sélectionnons `Ajouter une nouvelle vue`,
* Remplissons le nom de la vue (dans notre cas **index**), sélectionnons `Razor` comme moteur de vue, et cliquons sur OK.

Maintenant que nous avons créé notre fichier de vue de page d'accueil, nous ajouterons le balisage pour le formulaire de connexion.

```
<div class="container">      <div class="row">        <div class="col-md-5 col-md-offset-4">          <div class="panel panel-default">            <div class="panel-body">              <form action="/login" method="post" style="margin:0">                <div class="form-group">                  <input type="text" name="username" id="username"                       placeholder="Entrez le nom d'utilisateur" class="form-control"                       required minlength="3" maxlength="15" />                </div>                <button type="submit" class="btn btn-primary btn-block">                  Entrer dans le Chat                </button>              </form>            </div>          </div>        </div>      </div>    </div>
```

#### La page de chat

Nous créerons la vue pour la page de chat en suivant les mêmes étapes que ci-dessus, mais en utilisant `Chat` comme nom de notre dossier plutôt que `Home`.

Dans la vue de chat, nous ajoutons du balisage pour nous donner une barre latérale des utilisateurs disponibles et une zone pour discuter.

```
<!DOCTYPE html>    <html>    <head>      <title>pChat — Salon de discussion privé</title>      <link rel="stylesheet" href="@Url.Content("~/Content/app.css")">    </head>    <body>            @{                var currentUser = ViewBag.currentUser;            }        <!-- Barre de navigation -->        <nav class="navbar navbar-inverse">          <div class="container-fluid">            <div class="navbar-header">              <a class="navbar-brand" href="#">pChat</a>            </div>            <ul class="nav navbar-nav navbar-right">              <li><a href="#">Se déconnecter</a></li>            </ul>          </div>        </nav>        <!-- / Barre de navigation -->        <div class="container">          <div class="row">            <div class="col-xs-12 col-md-3">              <aside class="main">                <div class="row">                  <div class="col-xs-12">                    <div class="panel panel-default users__bar">                      <div class="panel-heading users__heading">                        Utilisateurs en ligne (1)                      </div>                      <div class="panel-body users__body">                        <ul class="list-group">                        @if( @currentUser == "Daenerys" ) {                            <li class="user__item">                                <div class="avatar"></div> <a href="#">Jon</a>                            </li>                        } else if( @currentUser == "Jon") {                            <li class="user__item">                                <div class="avatar"></div> <a href="#">Daenerys</a>                            </li>                        }                        </ul>                      </div>                    </div>                  </div>                </div>              </aside>            </div>            <div class="col-xs-12 col-md-9 chat__body">              <div class="row">                <div class="col-xs-12">                  <ul class="list-group chat__main">                    <div class="row __chat__par__">                      <div class="__chat__ from__chat">                        <p>As-tu vu l'épée d'Avery ???</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ receive__chat">                        <p>Euh, elle m'a paru normale...</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ receive__chat">                        <p>peut-être que je suis un hater</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ from__chat">                        <p>Lmaooo</p>                      </div>                    </div>                  </ul>                </div>                <div class="chat__type__body">                  <div class="chat__type">                    <textarea id="msg_box" placeholder="Tapez votre message"></textarea>                  </div>                </div>                <div class="chat__typing">                  <span id="typerDisplay"></span>                </div>              </div>            </div>          </div>        </div>        <script src="@Url.Content("~/Content/app.js")"></script>        </body>    </html>
```

Nous utilisons le [moteur de modèle razor](https://en.wikipedia.org/wiki/ASP.NET_Razor), qui nous donne la possibilité de lire les données passées depuis le code C# et de les assigner à des variables qui peuvent être utilisées dans notre frontend. En utilisant `@{ var currentUser = ViewBag.currentUser }`, nous avons passé le nom de l'utilisateur actuel, ce qui sera utile sous peu.

> _? Pour garder les choses rapides et simples, nous avons supposé qu'il n'y a que deux utilisateurs possibles : D**aenerys** ou J**on.** Donc, en utilisant la condition razor @`if{ }`, nous montrons qui est disponible pour discuter._

Maintenant que nous avons nos vues en place, nous pouvons passer à notre fonctionnalité d'indicateur de frappe !

### Implémentation de l'indicateur de frappe

#### Écoute de l'événement de frappe

Dans la plupart des applications de chat, la fonctionnalité devient visible lorsque quelqu'un est en train de taper. Pour l'implémenter, nous commencerons par écouter l'événement de frappe dans la zone de texte de chat en utilisant jQuery. Nous passerons également la variable `currentUser` que nous avons définie précédemment avec razor à notre script.

```
var currentUser = @currentUser;
```

```
    $('#msg_box').on('keydown', function () {      //stub    });
```

Nous avons ajouté un écouteur à l'événement `keydown` dans notre zone de frappe pour nous aider à surveiller quand quelqu'un est en train de taper.

Maintenant que nous avons créé nos écouteurs, nous allons les faire envoyer un message indiquant que quelqu'un est en train de taper aux autres membres du chat. Pour ce faire, nous créerons un point de terminaison dans notre code C# pour recevoir cette requête et la diffuser via Pusher.

Nous implémenterons tout le code client (en supposant que notre point de terminaison C# existe, puis nous créerons réellement le point de terminaison plus tard).

> _? Pour éviter les requêtes excessives à notre code C#, c'est-à-dire envoyer une requête à chaque fois qu'une touche du clavier est pressée ou relâchée, nous allons limiter l'envoi des requêtes en utilisant une fonction de débogage. Cette fonction de débogage ignore simplement une fonction pendant un certain temps si elle continue de se produire._

```
// Fonction de débogage    // Crédit : https://davidwalsh.name/javascript-debounce-function
```

```
    // Retourne une fonction, qui, tant qu'elle continue d'être invoquée, ne    // sera pas déclenchée. La fonction sera appelée après qu'elle ait cessé d'être appelée pour    // N millisecondes. Si `immediate` est passé, déclencher la fonction sur le    // bord avant, au lieu du bord arrière.    function debounce(func, wait, immediate) {        var timeout;        return function() {            var context = this, args = arguments;            var later = function() {                timeout = null;                if (!immediate) func.apply(context, args);            };            var callNow = immediate && !timeout;            clearTimeout(timeout);            timeout = setTimeout(later, wait);            if (callNow) func.apply(context, args);        };    };
```

Maintenant que nous avons une fonction **debounce**, nous créerons la fonction de rappel pour notre événement `keydown` :

```
var isTypingCallback = debounce( function() {        $.post('/chat/typing', {            typer: currentUser,        });    }, 600, true);
```

et passer le rappel à nos écouteurs d'événements.

```
$('#msg_box').on('keydown',isTypingCallback);
```

#### Création du point de terminaison déclenché par l'événement de frappe

Plus tôt, nous avions nos écouteurs d'événements envoyer une requête **POST** à la route `/chat/typing` côté client. Maintenant, nous allons créer cette route, qui transmettra l'événement de frappe aux autres utilisateurs clients en utilisant [Pusher](http://pusher.com).

Tout d'abord, nous créerons la route pour le point de terminaison dans notre fichier `RouteConfig.cs`.

```
...    routes.MapRoute(        name: "UserTyping",        url: "chat/typing",        defaults: new { controller = "Chat", action = "Typing" }    );
```

> _? Nous avons créé ce point de terminaison pour qu'il soit géré par la méthode d'action T**yping** du contrôleur C**hatController.**_

Ensuite, nous créerons notre méthode d'action Typing dans le `ChatController` :

```
[HttpPost]    public ActionResult Typing()    {        //stub    }
```

### Utilisation de Pusher pour mettre à jour notre application en temps réel

Notre point de terminaison `/chat/typing` recevra une charge utile de publication de l'utilisateur qui est en train de taper. Nous allons utiliser [Pusher](http://pusher.com) pour transmettre cela à tout le monde.

Sur notre [tableau de bord Pusher](https://dashboard.pusher.com/), nous créerons une nouvelle application en remplissant les informations demandées — nom de l'application, technologie frontend, etc. Vous pouvez [vous inscrire gratuitement](https://pusher.com/) si vous n'avez pas de compte. Ensuite, nous installerons le package **Pusher Server** dans notre code C# en utilisant NuGet, un gestionnaire de paquets pour .NET.

![Image](https://cdn-media-1.freecodecamp.org/images/iXWg6pncTloovKOm5rJjn3GhagikRa4BeRfs)

> _? Pour installer le package, nous faisons un clic droit sur le répertoire P**ackages**, sélectionnons l'option a**dd Package,** et sélectionnons le package P**usher Server**._

Ensuite, nous ajouterons la diffusion Pusher à notre événement d'action **Typing**. Pour utiliser Pusher, nous devrons importer l'espace de noms **Pusher Server** dans notre code.

```
...    using PusherServer;
```

```
    namespace HeyChat.Controllers    {        public class ChatController : Controller        {          ...
```

```
          [HttpPost]          public ActionResult Typing()          {              string typer        = Request.Form["typer"];              string socket_id    = Request.Form["socket_id"];
```

```
              var options = new PusherOptions();              options.Cluster = "PUSHER_APP_CLUSTER";
```

```
              var pusher = new Pusher(              "PUSHER_APP_ID",              "PUSHER_APP_KEY",              "PUSHER_APP_SECRET", options);
```

```
              pusher.TriggerAsync(              "chat",              "typing",              new { typer = typer },              new TriggerOptions() { SocketId = socket_id });
```

```
              return new HttpStatusCodeResult(200);          }         ...
```

Nous avons initialisé Pusher en utilisant notre **PUSHER_APP_ID**, **PUSHER_APP_KEY**, **PUSHER_APP_SECRET** et **PUSHER_APP_CLUSTER** (assurez-vous de remplacer ceux-ci par les valeurs réelles de votre tableau de bord). Ensuite, nous avons diffusé un objet contenant le **typer** — qui est la personne qui tape — sur l'événement `typing` via le canal `chat`.

> _? Nous avons ajouté n`ew TriggerOptions() { SocketId = socket_id }` à notre fonction Pusher t**riggerAsync**. Cela est pour empêcher l'expéditeur de la diffusion de recevoir également la diffusion. Pour ce faire, nous avons supposé que nous recevions s`ocket_id` dans notre charge utile avec t`yper,` donc sur notre côté client, nous l'ajouterons à la charge utile envoyée._

Maintenant, chaque fois qu'il y a un événement de frappe, notre code C# le diffuse sur Pusher. Il ne reste plus qu'à écouter cette diffusion et à afficher la fonctionnalité 'xxxx est en train de taper...'.

Tout d'abord, nous initialiserons Pusher dans la section de script de notre page de chat en utilisant notre **PUSHER_APP_KEY** et **PUSHER_APP_CLUSTER** (une fois de plus, remplacez ceux-ci par les valeurs de votre tableau de bord).

```
var pusher = new Pusher('PUSHER_APP_KEY', {        cluster:'PUSHER_APP_CLUSTER'    });
```

Pour implémenter l'exemption du diffuseur dont nous avons parlé plus tôt, nous obtiendrons l'identifiant de socket de notre instance client `pusher` et modifierons notre charge utile pour la requête de frappe au serveur pour l'inclure.

```
var socketId = null;    pusher.connection.bind('connected', function() {      socketId = pusher.connection.socket_id;    });
```

```
    var isTypingCallback = debounce( function() {        $.post('/chat/typing', {            typer: currentUser,            socket_id: socketId // passer le paramètre socket_id à utiliser par le serveur        });    }, 600, true);
```

Maintenant que Pusher est initialisé sur notre côté client, nous allons nous abonner au canal de chat et implémenter notre fonctionnalité en utilisant le `typer` passé.

```
var channel = pusher.subscribe('chat');
```

```
    channel.bind('typing', function(data) {        $('#typerDisplay').text( data.typer + ' est en train de taper...');
```

```
        $('.chat__typing').fadeIn(100, function() {            $('.chat__type__body').addClass('typing_display__open');        }).delay(1000).fadeOut(300, function(){            $('.chat__type__body').removeClass('typing_display__open');        });    });
```

### Conclusion

Dans ce tutoriel, nous avons passé en revue l'implémentation de la fonctionnalité populaire d'indicateur de frappe en utilisant Pusher, .NET, le code C# et un peu de jQuery. Nous avons également vu comment diffuser des messages et éviter que l'expéditeur ne réponde à un message qu'il a envoyé.

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/typing-indicator-aspnet/).