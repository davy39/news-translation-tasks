---
title: Problème de protection CSRF et comment le résoudre
subtitle: ''
author: Jakub T. Jankiewicz
co_authors: []
series: null
date: '2022-03-28T18:39:45.000Z'
originalURL: https://freecodecamp.org/news/csrf-protection-problem-and-how-to-fix-it
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/laptop-security-virus-protection-internet-malware-1588329-pxhere.com.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
seo_title: Problème de protection CSRF et comment le résoudre
seo_desc: "One day I was working on a feature at work. I had many branches created\
  \ in JIRA tickets, so I wanted to open a bunch of PRs (Pull Requests) all at once\
  \ in different tabs. \nThis is how I usually work – I have a lot of tabs open and\
  \ this speeds things ..."
---

Un jour, je travaillais sur une fonctionnalité au travail. J'avais de nombreuses branches créées dans des tickets JIRA, je voulais donc ouvrir un groupe de PRs (Pull Requests) d'un seul coup dans différents onglets.

C'est ainsi que je travaille habituellement – j'ai beaucoup d'onglets ouverts et cela accélère les choses, car je n'ai pas besoin d'attendre que la page suivante se charge.

Mais après avoir créé la première PR dans BitBucket et essayé de passer à la page suivante, j'ai été accueilli par un message d'erreur concernant un jeton CSRF invalide. C'est un problème courant avec les applications web qui disposent d'une protection CSRF.

Dans cet article, vous apprendrez donc ce qu'est le CSRF et comment corriger cette erreur.

<h2>Table des matières :</h2>
<ul>
	<li><a href="#quest-ce-que-le-csrf">Qu'est-ce que le CSRF ?</a></li>
  	<li><a href="#protection-csrf-standard">Protection CSRF standard</a></li>
    <li><a href="#le-probleme-avec-les-jetons">Le problème avec les jetons</a></li>
    <li><a href="#solution-de-communication-inter-onglets">Solution de communication inter-onglets</a>
        <ul>
  			<li><a href="#bibliotheque-sysend">Bibliothèque Sysend</a></li>
    
  			<li><a href="#broadcast-channel">Broadcast Channel</a></li>
        </ul>
    </li>
  	<li><a href="#conclusion">Conclusion</a></li>
</ul>

## Qu'est-ce que le CSRF ?

CSRF est un acronyme pour **Cross-Site Request Forgery**. Il s'agit d'un vecteur d'attaque que les attaquants utilisent couramment pour s'introduire dans votre système.

La manière dont on se protège habituellement contre le CSRF consiste à envoyer un jeton unique généré par chaque requête HTTP. Si le jeton qui se trouve sur le serveur ne correspond pas à celui de la requête, vous affichez une erreur à l'utilisateur.

## Protection CSRF standard

Voici une façon de se protéger contre le CSRF avec un jeton :

```javascript
const inital_token = '...';

const secure_fetch = (token => {
    const CSRF_HEADER = 'X-CSRF-TOKEN';
    return (url) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
              [CSRF_HEADER]: token
            }
        });
        response.then(res => {
           token = res.headers[CSRF_HEADER]
        });
        return response;
    };
})(inital_token);

```

Ce code utilise l'API [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) pour envoyer et recevoir un jeton sécurisé dans les en-têtes [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). Côté back-end, vous devriez générer le premier jeton initial lors du chargement de la page. Sur le serveur, à chaque requête [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)), vous devriez vérifier si le jeton est valide.

## Le problème avec les jetons

Cela fonctionne bien à moins que vous n'ayez plus d'un onglet ouvert. Chaque onglet peut envoyer des requêtes au serveur, ce qui cassera cette solution. Et les utilisateurs avancés pourraient ne pas être en mesure d'utiliser votre application comme ils le souhaitent.

Mais il existe une solution simple à ce problème : la communication inter-onglets.

## Solution de communication inter-onglets

### Bibliothèque Sysend

Vous pouvez utiliser la [bibliothèque Sysend](https://github.com/jcubic/sysend.js), une solution open source que j'ai créée spécifiquement à cet effet. Elle simplifie la communication entre les onglets.

Si vous le souhaitez, vous pouvez utiliser une API native du navigateur comme [Broadcast Channel](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel) pour faire la même chose. Nous verrons comment faire plus tard dans cet article.

Mais la bibliothèque **Sysend** fonctionnera pour les navigateurs qui ne supportent pas Broadcast Channel. Elle fonctionne également dans IE (elle présente quelques bugs, ce qui n'est pas une surprise). Vous pourriez également avoir besoin de supporter certains anciens navigateurs mobiles. Elle dispose également d'une API beaucoup plus simple.

Voici l'exemple le plus simple :

```javascript
let token;
sysend.on('token', new_token => {
    token = new_token;
});

// ...

sysend.broadcast('token', token);
```

Et voici comment vous utiliseriez cette bibliothèque pour corriger la protection CSRF :

```javascript
const inital_token = '...';

const secure_fetch = (token => {
    const CSRF_HEADER = 'X-CSRF-TOKEN';
    const EVENT_NAME = 'csrf';
    sysend.on(EVENT_NAME, new_token => {
        // obtenir le nouveau jeton d'un autre onglet
        token = new_token;
    });
    return (url) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
              [CSRF_HEADER]: token
            }
        });
        response.then(res => {
           token = res.headers[CSRF_HEADER];
           // envoyer le nouveau jeton aux autres onglets
           sysend.broadcast(EVENT_NAME, token); 
        });
        return response;
    };
})(inital_token);

```

Tout ce que vous avez à faire est d'envoyer et de recevoir un seul message des autres onglets lors de l'envoi de la requête. Et votre application protégée par CSRF fonctionnera sur de nombreux onglets.

Et c'est tout. Cela permettra aux utilisateurs avancés d'utiliser votre application dotée d'une protection CSRF lorsqu'ils souhaitent ouvrir de nombreux onglets.

### Broadcast Channel

Voici l'exemple le plus simple possible d'utilisation de Broadcast Channel :

```javascript
const channel = new BroadcastChannel('my-connection');
channel.addEventListener('message', (e) => {
    console.log(e.data); // 'un message'
});
channel.postMessage('un message');
```

Ainsi, avec cette API simple, vous pouvez faire la même chose que ce que nous avons fait auparavant :

```javascript
const inital_token = '...';

const secure_fetch = (token => {
    const CSRF_HEADER = 'X-CSRF-TOKEN';
    const channel = new BroadcastChannel('csrf-protection');
    channel.addEventListener('message', (e) => {
        // obtenir le nouveau jeton d'un autre onglet
    	token = e.data;
    });
    return (url) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
              [CSRF_HEADER]: token
            }
        });
        response.then(res => {
           token = res.headers[CSRF_HEADER];
           // envoyer le nouveau jeton aux autres onglets
           channel.postMessage(token);
        });
        return response;
    };
})(inital_token);
```

Comme vous pouvez le voir dans l'exemple ci-dessus, Broadcast Channel n'a pas d'espace de noms pour les événements. Donc, si vous souhaitez envoyer plus d'un type d'événement, vous devez créer des types d'événements.

Voici un exemple d'utilisation de Broadcast Channel pour faire plus que la correction de la protection CSRF dont nous avons discuté jusqu'à présent.

Vous pouvez synchroniser la connexion et la déconnexion de votre application. Si vous vous connectez dans un onglet, vos autres onglets vous connecteront également. De la même manière, vous pouvez synchroniser le panier d'achat dans certains sites de commerce électronique.

```javascript
const channel = new BroadcastChannel('my-connection');
const CSRF = 'app/csrf';
const LOGIN = 'app/login';
const LOGOUT = 'app/logout';
let token;
channel.addEventListener('message', (e) => {
    switch (e.data.type) {
        case CSRF:
            token = e.data.payload;
            break;
        case LOGIN:
            const { user } = e.data.payload;
            autologin(user);
            break;
        case LOGOUT:
            logout();
            break;
    }
});

channel.postMessage({type: 'login', payload: { user } });
```

## Conclusion

C'est une excellente chose de protéger votre application contre les attaquants. Mais gardez également à l'esprit la manière dont les gens utiliseront votre application, afin de ne pas la rendre inutilement difficile à utiliser. Cela s'applique non seulement à ce problème particulier.

La bibliothèque **Sysend** est un moyen simple de communiquer entre les onglets ouverts dans le même navigateur. Et elle peut résoudre des problèmes majeurs de protection CSRF. La bibliothèque possède plus de fonctionnalités, et vous pouvez consulter son [dépôt GitHub](https://github.com/jcubic/sysend.js) pour plus de détails.

**Broadcast Channel** n'est pas non plus très compliqué. Si vous n'avez pas besoin de supporter de vieux navigateurs ou certains anciens appareils mobiles, vous pouvez utiliser cette API. Mais si vous avez besoin de supporter des navigateurs plus anciens, ou si vous voulez simplifier votre code, vous pouvez utiliser la bibliothèque sysend.

Si vous voulez voir le support des navigateurs pour Broadcast Channel, vous pouvez consulter [Can I Use](https://caniuse.com/broadcastchannel).