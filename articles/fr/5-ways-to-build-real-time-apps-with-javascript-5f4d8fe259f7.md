---
title: 5 façons de créer des applications en temps réel avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T15:24:05.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-build-real-time-apps-with-javascript-5f4d8fe259f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9ldkwChSUEeQGlbVzcJSVg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 5 façons de créer des applications en temps réel avec JavaScript
seo_desc: 'By Burke Holland

  There was a point in time where we didn’t expect too much from web pages. Which
  reminds me, the Space Jam movie website is still on the internet in its original
  form. And it uses a frameset. Not iFrames. FRAMES.

  Space Jam_SPACE JAM, ...'
---

Par Burke Holland

Il fut un temps où nous n'attendions pas grand-chose des pages web. Ce qui me rappelle que le site du film Space Jam est toujours en ligne dans sa forme originale. Et il utilise un [frameset](https://caniuse.com/#search=frameset). Pas des iFrames. **FRAMES**.

[**Space Jam**](https://www.warnerbros.com/archive/spacejam/movie/jam.htm)  
[_SPACE JAM, personnages, noms et tous les indicia associés sont des marques déposées de Warner Bros. © 1996_www.warnerbros.com](https://www.warnerbros.com/archive/spacejam/movie/jam.htm)

Warner Bros a quelques copies légèrement utilisées de Dreamweaver MX.

C'était en 1996. Nous sommes en 2019. Les temps ont changé et les utilisateurs attendent beaucoup plus des sites web. Ils ne s'attendent pas seulement à ce qu'ils soient beaux, ils s'attendent à ce qu'ils soient des applications complètes, et cela inclut le temps réel.

#### Applications en temps réel

Les applications en temps réel sont celles qui réagissent aux changements partout dans le système d'une application connectée, et pas seulement à ceux effectués par l'utilisateur actuel.

L'exemple canonique du temps réel est une application de messagerie. Comme lorsque vous envoyez un message à un groupe d'amis pour vous retrouver pour des ailes de poulet le vendredi. Puis vous mettez à jour tout le monde minute par minute sur votre progression pour aller du travail au bar. Merci, Trevor. Maintenant, nous sommes tous piégés dans un enfer de notifications auquel nous ne nous sommes pas inscrits. JE VOULAIS JUSTE DES AILES.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A0RYVB-7SF0sqpvQdVLWXg.png)
_C'est quoi, Trevor ? Tu n'es plus qu'à 10 minutes ? RÉJOUISSEZ-VOUS. J'ai hâte d'être à un chiffre._

En ce qui concerne le web, il existe plusieurs modèles, technologies, bibliothèques et services différents que vous pouvez utiliser pour obtenir la fonctionnalité en temps réel qui est généralement réservée aux applications natives. J'ai récemment discuté avec Anthony Chu qui m'a donné 5 façons de créer des applications en temps réel en JavaScript.

[**Anthony Chu #MSIgniteTheTour (@nthonyChu) | Twitter**](https://twitter.com/nthonychu)  
[_Les derniers Tweets de Anthony Chu #MSIgniteTheTour (@nthonyChu). Cloud Advocate @Microsoft. Azure, ASP .NET, Node.js..._twitter.com](https://twitter.com/nthonychu)

#### 1. Long-Polling

C'est lorsque l'application demande des mises à jour au serveur selon un calendrier. L'application "interroge" le serveur.

C'est l'équivalent sur le net des enfants qui demandent "on est bientôt arrivés ?" toutes les cinq minutes. On dirait qu'on est bientôt arrivés, gamin ? Demande-moi une fois de plus et je te jure que je vais jeter cette copie de "The Bee Movie" dans un fossé et tu pourras regarder l'herbe par la fenêtre comme on le faisait quand j'étais enfant.

Le long-polling peut être implémenté manuellement avec n'importe quelle bibliothèque HTTP JavaScript, comme jQuery ou Axios. Je n'ai jamais réellement implémenté cela moi-même. En faisant quelques recherches pour cet article, j'ai découvert que la meilleure façon de faire cela est d'utiliser une fonction récursive avec `setTimeout`. Cela est dû au fait que l'utilisation de `setInterval` ne tient pas compte des requêtes qui échouent ou qui dépassent le temps imparti. Vous pourriez vous retrouver avec un tas d'appels ajax qui sont tous traités dans le désordre.

Voici un exemple de l'article très bien fait sur [Tech Octave](https://techoctave.com/c7/posts/60-simple-long-polling-example-with-javascript-and-jquery).

```
(function poll(){
   setTimeout(function(){
      $.ajax({ url: "server", success: function(data){
        //Mettez à jour votre jauge de tableau de bord
        salesGauge.setValue(data.value);
        //Configurez le prochain sondage de manière récursive
        poll();
      }, dataType: "json"});
  }, 30000);
})();
```

Il existe également des bibliothèques comme pollymer (à ne pas confondre avec Polymer) qui sont spécifiquement pour le long-polling. Vous comprenez ? "poll"ymer ? Parce que ça sonde ? Ça marche ?

[**fanout/pollymer**](https://github.com/fanout/pollymer)  
[_Bibliothèque AJAX/long-polling à usage général. Contribuez au développement de fanout/pollymer en créant un compte sur GitHub._github.com](https://github.com/fanout/pollymer)

Le long-polling est bien car il fonctionne dans tous les navigateurs, même les très anciens. C'est mauvais car c'est super inefficace et pas exactement "en temps réel". Il a aussi quelques cas particuliers bizarres (comme les échecs de requête) auxquels vous devez faire face comme nous l'avons déjà vu avec `setInterval`.

Une meilleure alternative au long-polling est les Événements envoyés par le serveur ou SSE.

#### 2. Événements envoyés par le serveur

Les Événements envoyés par le serveur (SSE) sont similaires au long-polling en ce sens que le client demande des informations au serveur. La grande différence est qu'avec SSE, le serveur maintient simplement la connexion ouverte. Lorsqu'un événement se produit et qu'il y a des informations à envoyer au client, le serveur envoie un événement au client.

[**Événements envoyés par le serveur**](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  
[_Traditionnellement, une page web doit envoyer une requête au serveur pour recevoir de nouvelles données ; c'est-à-dire que la page demande des données à..._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

Revenons à notre analogie du "voyage en voiture de l'enfer", ce serait comme si l'enfant dit "On est bientôt arrivés ?", puis attend patiemment votre réponse. Quatre heures de silence sublimes plus tard, vous arrivez à destination, vous vous retournez et dites "oui". C'est le scénario le plus irréaliste que j'ai jamais imaginé dans ma vie.

SSE fait partie de l'API `EventSource` du navigateur. Notez que selon [caniuse.com](https://caniuse.com/#search=EventSource), ni IE 11 ni Edge ne supportent SSE. Cela en fait une technologie un peu difficile à choisir, aussi intéressante soit-elle.

La bonne nouvelle est que presque tous les navigateurs supportent les Web Sockets.

#### 3. Web Sockets

Web Sockets est une technologie qui facilite un véritable canal de communication bidirectionnel entre un client et un serveur. Contrairement aux Événements envoyés par le serveur, qui ne permettent que la communication du serveur vers un client, les Web Sockets peuvent être utilisés pour communiquer dans les deux sens.

Les Web Sockets sont, eh bien, un peu verbeux. Ce ne sont pas vraiment le genre d'API avec lesquelles vous voulez construire des applications. Un peu comme vous pourriez faire une requête HTTP avec l'objet [XHR](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), mais OMG NON. J'ai googlé "PHP Web Socket Sample" et j'ai trouvé ce truc des docs PHP. J'ai zoomé au maximum dans Chrome et j'ai à peine réussi à tout faire tenir dans une seule capture d'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b8NjhSqlK84BiLsFDlfRkA.png)

Et ce n'est QUE la partie serveur. Vous devez encore configurer le navigateur.

Alors... c'est un **non** pour moi.

Heureusement, il existe de nombreuses bibliothèques qui abstraient encore plus les Web Sockets afin que vous n'ayez pas à écrire tout cela. L'une de ces bibliothèques s'appelle "SignalR".

#### 4. SignalR

SignalR est une bibliothèque qui implémente les Web Sockets à la fois en JavaScript ET en .NET. Sur le serveur, vous créez ce que l'on appelle un "hub" dans SignalR. Ce hub envoie et reçoit des messages des clients.

Les clients se connectent ensuite au hub (en utilisant la bibliothèque JavaScript SignalR) et répondent aux événements du hub, ou envoient leurs propres événements dans le hub.

SignalR revient également au long-polling chaque fois que les Web Sockets ne sont pas disponibles. Bien que ce ne soit pas très probable à moins que vous n'utilisiez IE 9 ou une version antérieure.

Voici un exemple de configuration de SignalR sur le serveur...

```
using System;
using System.Web;
using Microsoft.AspNet.SignalR;
namespace SignalRChat
{
    public class ChatHub : Hub
    {
        public void Send(string name, string message)
        {
            // Appelez la méthode broadcastMessage pour mettre à jour les clients.
            Clients.All.broadcastMessage(name, message);
        }
    }
}
```

OK, OK. Je sais que ce n'est pas une comparaison équitable avec l'exemple PHP ci-dessus, mais j'essaie de faire passer un message ici. Suivez-moi. Faites-le pour moi. Je traverse une matinée difficile.

Donc SignalR rend la programmation des Web Sockets plus amusante, mais vous savez ce qui est encore plus amusant que de les programmer ? Ne pas les programmer.

#### 5. Azure SignalR

Souvent, lorsque nous voulons configurer des applications en temps réel, la construction d'un serveur Web Socket n'est pas exactement une activité à valeur ajoutée. Nous le faisons, mais seulement parce que nous devons pour obtenir le temps réel. Nous préférerions que cela "fonctionne simplement".

Azure SignalR est exactement cela. C'est un hub SignalR que vous pouvez consommer à la demande en tant que service. Cela signifie que vous n'avez qu'à envoyer et répondre aux événements, ce qui est ce que vous recherchez en premier lieu.

[**Qu'est-ce qu'Azure SignalR**](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-overview?WT.mc_id=medium-blog-buhollan)  
[_Un aperçu du service Azure SignalR._docs.microsoft.com](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-overview?WT.mc_id=medium-blog-buhollan)

Vous créez le hub SignalR dans Azure en tant que service Azure, puis vous vous connectez simplement à partir du client et envoyez/recevez des messages.

#### Et maintenant vous savez...

Regardez l'interview ci-dessous avec Anthony. Nous avons tourné celle-ci à Vegas alors que nous étions tous les deux à une conférence et nous nous sommes bien amusés avec une perruque que j'ai achetée chez Party City. Les 8 $ les mieux dépensés de ma vie.

%[https://youtu.be/3qucTcr3pGA?list=PLlrxD0HtieHgugDxYBujMFnvSveH4fgWN]