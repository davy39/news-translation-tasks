---
title: How to build a typing indicator for your chat app in ASP.NET
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
seo_title: null
seo_desc: 'By Neo Ighodaro


  A basic understanding of ASP.NET and jQuery is needed to follow this tutorial.


  When you’re using a chat app, knowing when the person you are chatting with is typing
  a message can improve your user experience. It gives you some feedb...'
---

By Neo Ighodaro

> A basic understanding of ASP.NET and jQuery is needed to follow this tutorial.

When you’re using a chat app, knowing when the person you are chatting with is typing a message can improve your user experience. It gives you some feedback that you’re not alone in the conversation, and that a message is coming your way.

In this tutorial, we will go through some simple steps to create this feature using C#, .NET, and Pusher.

At the end of this tutorial we will have something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/rwOg-HkLtiydf-37RuU7DvGykJJyt8fz-P4P)

This tutorial assumes prior knowledge of:

* C#
* .NET MVC
* JavaScript (jQuery)

When you’re ready, let’s begin.

### Setting up our project

We’ll be using [Visual Studio](https://www.visualstudio.com/), which is an IDE popularly used for building .NET projects. Visual Studio 2017 is free and available for most Operating Systems. You can view installation details [here](https://www.visualstudio.com/).

After installing Visual Studio, launch it and create a new project by clicking **New Project** from the dashboard. Following the **New Project** wizard we:

* Set C# as our language
* Select .NET MVC Project as the template
* Fill in the Project name (for example “HeyChat” — but any name would do)
* Fill in the Solution name (that is, the application name — “HeyChat” or any name would do).

![Image](https://cdn-media-1.freecodecamp.org/images/wHa3qOf05-fbAXL-Ea06A5GNCKi3nJeGoiYq)

### Writing the server-side (C#) code

To display a typing indicator, our chat app needs to be able to recognize who is typing at any given time. For this, we will add some limited form of identification. We’re not doing any authentication at all, because this tutorial does not require it.

> _? For the purpose of this tutorial, we will assume that this chat is open to all users. All that will be required is that our users specify their names on first entry._

### Route definition

We can define some of the routes that we need to make this feature, which are:

* A home route which renders the first page that takes the user’s name.
* A login route which accepts a `POST` request of the user’s name.
* A chat route which renders the chat view.

> _? We may need some other routes as we go along, but this is enough for starters._

To add these routes, we open the `RouteConfig.cs` file in the `App_Start` directory of our application. And in it, we add the routes we have defined.

```
routes.MapRoute(        name: "Home",        url: "",        defaults: new { controller = "Home", action = "Index" }    );
```

```
    routes.MapRoute(        name: "Login",        url: "login",        defaults: new { controller = "Login", action = "Index" }    );
```

```
    routes.MapRoute(        name: "ChatRoom",        url: "chat",        defaults: new {controller = "Chat", action="Index"}    );
```

Using the **Home** route as a sample, the route definition states that `/` requests will be handled by the `HomeController` which is found in the `Controllers/HomeController.cs` file and the `Index` method of that controller. Next, we will create the controllers we’ll need.

### Creating controllers and action methods

To create a new controller, right-click the **Controller** directory and select `Add → Controller`. In the resulting form, we type in the name of our controller and select the empty template.

> _? When our application is created, it includes a HomeController with an Index action method by default, so we’ll perform the above steps to create our LoginController and ChatController._

In our LoginController class, we create the Index action method specifying `[HttpPost]` at the top of the action method to indicate that it handles `POST` requests.

```
public class LoginController : Controller    {        [HttpPost]        public ActionResult Index()        {
```

```
        }    }
```

The Index action of the LoginController will receive the request payload, read the username from the payload, and assign it to the current user session. Then it will redirect our user to the chat page. When we add this to our action method, we’ll have:

```
public class LoginController : Controller    {        [HttpPost]        public ActionResult Index()        {            string user = Request.Form["username"];            if (user.Trim() == "") {                return Redirect("/");            }            Session["user"] = user;            return Redirect("/chat");        }    }
```

> _? In a real-world chat app, we would add the user to a database and mark the user as logged in so that other users could see the available chat options. But that is beyond the scope of this tutorial, so adding to a session will suffice._

In our ChatController class, we will add the Index action method. The Index action of the ChatController will render our chat view and pass along the current user to the view.

```
public class ChatController : Controller    {        public ActionResult Index()        {            if (Session["user"] == null) {                return Redirect("/");            }
```

```
            ViewBag.currentUser = Session["user"];
```

```
            return View ();        }    }
```

> _? By default, action methods handle G`ET` requests, so we will not need to add [`HttpGet]` to the top of our method. We’ve also added a simple check to prevent access to the chat page if there is no logged in user._

Let’s not forget about our Home route. In the HomeController, we’ll add the code to render the front page.

```
public class HomeController : Controller    {        public ActionResult Index()        {            if ( Session["user"] != null ) {                return Redirect("/chat");            }
```

```
            return View();        }    }
```

> _? We’ve also added a small check to prevent multiple logins in the same user session._

At this point, we’ve created the Controllers and methods to serve our views (which we haven’t created yet), so trying to run this will give you some errors! Let’s fix that.

### Implementing the application’s views

Based on the routes we’ve defined so far, we will need two views:

* The front page view with the login form — served by the `Index`action method of the `HomeController` class
* The chat view where the typing indicator feature will be seen — served by `ChatController` class’ `Index` action method

#### Front page/login page

For our front page, we’ll create a page with a form that asks for the user’s username and shows them a button to submit for login. Referring to our controller code:

```
public class HomeController : Controller    {        public ActionResult Index()        {            if ( Session["user"] != null ) {                return Redirect("/chat");            }            return View();        }    }
```

> _? The V**iew** function creates a view response which we return. When V**iew()** is invoked, C# looks for the default view of the calling controller class. This default view is the i`ndex.cshtml` file found in the V**iews** directory, in a directory with the same name as the Controller. That is, the default view of the HomeController class will be the V`iews/Home/index.cshtml` file._

To create our `HomeController` default view, we:

* Right-click on the Views directory and select `Add New Folder`,
* Fill in **Home** as the folder name,
* Right click the newly created **Home** folder and select `Add New View`,
* Fill in the view name (in our case **index**), select `Razor` as the view engine, and click OK.

Now that we’ve created our front page view file, we’ll add the markup for the login form.

```
<div class="container">      <div class="row">        <div class="col-md-5 col-md-offset-4">          <div class="panel panel-default">            <div class="panel-body">              <form action="/login" method="post" style="margin:0">                <div class="form-group">                  <input type="text" name="username" id="username"                       placeholder="Enter Username" class="form-control"                       required minlength="3" maxlength="15" />                </div>                <button type="submit" class="btn btn-primary btn-block">                  Enter Chat                </button>              </form>            </div>          </div>        </div>      </div>    </div>
```

#### The chat page

We’ll create the view for the chat page following the same steps as above, but using `Chat` as our folder name rather than `Home`.

In the chat view, we add markup up to give us a sidebar of available users and an area for chatting.

```
<!DOCTYPE html>    <html>    <head>      <title>pChat — Private Chatroom</title>      <link rel="stylesheet" href="@Url.Content("~/Content/app.css")">    </head>    <body>            @{                var currentUser = ViewBag.currentUser;            }        <!-- Navigation Bar -->        <nav class="navbar navbar-inverse">          <div class="container-fluid">            <div class="navbar-header">              <a class="navbar-brand" href="#">pChat</a>            </div>            <ul class="nav navbar-nav navbar-right">              <li><a href="#">Log Out</a></li>            </ul>          </div>        </nav>        <!-- / Navigation Bar -->        <div class="container">          <div class="row">            <div class="col-xs-12 col-md-3">              <aside class="main">                <div class="row">                  <div class="col-xs-12">                    <div class="panel panel-default users__bar">                      <div class="panel-heading users__heading">                        Online Users (1)                      </div>                      <div class="panel-body users__body">                        <ul class="list-group">                        @if( @currentUser == "Daenerys" ) {                            <li class="user__item">                                <div class="avatar"></div> <a href="#">Jon</a>                            </li>                        } else if( @currentUser == "Jon") {                            <li class="user__item">                                <div class="avatar"></div> <a href="#">Daenerys</a>                            </li>                        }                        </ul>                      </div>                    </div>                  </div>                </div>              </aside>            </div>            <div class="col-xs-12 col-md-9 chat__body">              <div class="row">                <div class="col-xs-12">                  <ul class="list-group chat__main">                    <div class="row __chat__par__">                      <div class="__chat__ from__chat">                        <p>Did you see Avery's sword???</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ receive__chat">                        <p>Err Looked normal to me...</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ receive__chat">                        <p>maybe I'm a hater</p>                      </div>                    </div>                    <div class="row __chat__par__">                      <div class="__chat__ from__chat">                        <p>Lmaooo</p>                      </div>                    </div>                  </ul>                </div>                <div class="chat__type__body">                  <div class="chat__type">                    <textarea id="msg_box" placeholder="Type your message"></textarea>                  </div>                </div>                <div class="chat__typing">                  <span id="typerDisplay"></span>                </div>              </div>            </div>          </div>        </div>        <script src="@Url.Content("~/Content/app.js")"></script>        </body>    </html>
```

We’re using the [razor template engine](https://en.wikipedia.org/wiki/ASP.NET_Razor), which gives us the ability to read data passed from the C# code and assign them to variables that can be used in our frontend. Using `@{ var currentUser = ViewBag.currentUser }` we have passed in the name of the current user, which will come in handy shortly.

> _? To keep things quick and simple, we have assumed that there are only two possible users: D**aenerys** or J**on.** So using the razor @`if{ }` condition, we are showing who is available to chat with._

Now that we have our views in place, we can move on to our typing indicator feature!

### Implementing the typing indicator

#### Listening for the typing event

In most chat applications, the feature becomes visible when someone is typing. To implement it, we’ll start off by listening for the typing event in the chat text area using jQuery. We’ll also pass the `currentUser` variable we defined earlier with razor to our script.

```
var currentUser = @currentUser;
```

```
    $('#msg_box').on('keydown', function () {      //stub    });
```

We added a listener to the `keydown` event in our typing area to help us monitor when someone is typing.

Now that we’ve created our listeners, we’ll make them send a message that someone is typing to the other members of the chat. To do this, we’ll create an endpoint in our C# code to receive this request and broadcast it via Pusher.

We’ll implement all the client code (assuming that our C# endpoint exists, then we’ll actually create the endpoint later).

> _? To prevent excessive requests to our C# code, that is sending a request as every key on the keypad is pressed or released, we’ll throttle the sending of the requests using a debounce function. This debounce function just ignores a function for a while if it keeps occurring._

```
// Debounce function    // Credit: https://davidwalsh.name/javascript-debounce-function
```

```
    // Returns a function, that, as long as it continues to be invoked, will not    // be triggered. The function will be called after it stops being called for    // N milliseconds. If `immediate` is passed, trigger the function on the    // leading edge, instead of the trailing.    function debounce(func, wait, immediate) {        var timeout;        return function() {            var context = this, args = arguments;            var later = function() {                timeout = null;                if (!immediate) func.apply(context, args);            };            var callNow = immediate && !timeout;            clearTimeout(timeout);            timeout = setTimeout(later, wait);            if (callNow) func.apply(context, args);        };    };
```

Now that we have a **debounce** function, we’ll create the callback function for our `keydown` event:

```
var isTypingCallback = debounce( function() {        $.post('/chat/typing', {            typer: currentUser,        });    }, 600, true);
```

and pass the callback to our event listeners.

```
$('#msg_box').on('keydown',isTypingCallback);
```

#### Creating the endpoint triggered by the typing event

Earlier, we had our event listeners send a **POST** request to the `/chat/typing` Route on the client side. Now we’ll create this Route, which will transmit the typing event to other client users using [Pusher](http://pusher.com).

First, we’ll create the route for the endpoint in our `RouteConfig.cs` file.

```
...    routes.MapRoute(        name: "UserTyping",        url: "chat/typing",        defaults: new { controller = "Chat", action = "Typing" }    );
```

> _? We’ve created this endpoint to be handled by the T**yping** action method of the C**hatController.**_

Next, we’ll create our Typing action method in the `ChatController`:

```
[HttpPost]    public ActionResult Typing()    {        //stub    }
```

### Using Pusher to make our application update in realtime

Our `/``chat`/`typing` endpoint will receive a post payload of the user who is doing the typing. We’re going to use [Pusher](http://pusher.com) to transmit this to everyone else.

On our Pusher [dashboard](https://dashboard.pusher.com/), we’ll create a new app filling out the information requested — app name, frontend tech, and so on. You can [register for free](https://pusher.com/) if you don’t have an account. Next, we’ll install the **Pusher Server** package in our C# code using NuGet, a packer manager for .NET.

![Image](https://cdn-media-1.freecodecamp.org/images/iXWg6pncTloovKOm5rJjn3GhagikRa4BeRfs)

> _? To install the package, we right-click the P**ackages** directory, select the a**dd Package option,** and select the P**usher Server** package._

Then we’ll add the Pusher broadcasting to our **Typing** action event. To use Pusher, we’ll have to import the **Pusher Server** namespace into our code.

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

We initialized Pusher using our **PUSHER_APP_ID**, **PUSHER_APP_KEY**, **PUSHER_APP_SECRET**, and **PUSHER_APP_CLUSTER** (be sure to replace these with the actual values from your dashboard). Then we broadcast an object containing the **typer** _— which is the person typing —_ on the `typing` event via the `chat` channel.

> _? We’ve added n`ew TriggerOptions() { SocketId = socket_id }` to our Pusher t**riggerAsync** function. This is to prevent the sender of the broadcast from receiving the broadcast as well. To do this, we’ve assumed we’re receiving s`ocket_id` in our payload along with t`yper,` so on our client side, we’ll add it to the payload sent._

Now, whenever there’s a typing event, our C# code broadcasts it on Pusher. All that is left is to listen to that broadcast and display the ‘xxxx is typing…’ feature.

First, we’ll initialize Pusher in the script section of our chat page using our **PUSHER_APP_KEY** and **PUSHER_APP_CLUSTER** (once again, replace these with the values from your dashboard).

```
var pusher = new Pusher('PUSHER_APP_KEY', {        cluster:'PUSHER_APP_CLUSTER'    });
```

To implement the broadcaster exemption we mentioned earlier, we’ll get the socket id from our client `pusher` instance and amend our payload for the typing request to the server to include it.

```
var socketId = null;    pusher.connection.bind('connected', function() {      socketId = pusher.connection.socket_id;    });
```

```
    var isTypingCallback = debounce( function() {        $.post('/chat/typing', {            typer: currentUser,            socket_id: socketId // pass socket_id parameter to be used by server        });    }, 600, true);
```

Now that Pusher is initialized on our client side, we’ll subscribe to the chat channel and implement our feature using the `typer` passed.

```
var channel = pusher.subscribe('chat');
```

```
    channel.bind('typing', function(data) {        $('#typerDisplay').text( data.typer + ' is typing...');
```

```
        $('.chat__typing').fadeIn(100, function() {            $('.chat__type__body').addClass('typing_display__open');        }).delay(1000).fadeOut(300, function(){            $('.chat__type__body').removeClass('typing_display__open');        });    });
```

### Conclusion

In this tutorial, we’ve walked through implementing the popular typing indicator feature using Pusher, .NET, C# code and some jQuery. We’ve also seen how to broadcast messages and avoid the sender responding to a message they sent.

This post was first published to [Pusher](https://pusher.com/tutorials/typing-indicator-aspnet/).

