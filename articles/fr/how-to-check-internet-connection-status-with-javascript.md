---
title: Comment vérifier l'état de la connexion Internet en utilisant JavaScript Asynchrone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T19:00:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-internet-connection-status-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/js_online_offline.png
tags:
- name: internet
  slug: internet
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier l'état de la connexion Internet en utilisant JavaScript
  Asynchrone
seo_desc: "By Dave Gray\nCan you use JavaScript to check if your app is connected\
  \ to the internet?\nIn this article, I'll provide an updated answer to this Internet\
  \ connection detection question. (Whew! Say that fast five times!) \nThe solution\
  \ will use JavaScript..."
---

Par Dave Gray

Pouvez-vous utiliser JavaScript pour vérifier si votre application est connectée à Internet ?

Dans cet article, je vais fournir une réponse mise à jour à cette question de détection de connexion Internet. (Ouf ! Dites cela rapidement cinq fois !) 

La solution utilisera l'API Fetch de JavaScript et le code asynchrone avec Async & Await. Mais d'abord, examinons une solution acceptée et discutons pourquoi elle peut ne pas être le meilleur choix pour votre application.

## navigator.onLine

La propriété online de l'interface navigator, `navigator.onLine`, est fréquemment utilisée pour détecter l'état en ligne et hors ligne du navigateur. 

Combinée avec des écouteurs pour les événements online et offline, elle semble fournir une solution simple pour les développeurs qui est facile à implémenter. 

### Voyons comment nous implémenterions navigator.onLine

Commencez par ajouter un écouteur d'événement de chargement. Lorsque l'événement de chargement se déclenche, l'écouteur vérifiera la propriété online de l'interface navigator puis affichera l'état de connexion.

La propriété online de navigator fournit une réponse booléenne (vrai ou faux). Pour terminer l'action de l'écouteur, nous utiliserons une instruction ternaire pour définir la valeur d'affichage de l'état.

```javascript
window.addEventListener("load", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = navigator.onLine ? "En ligne" : "Hors ligne";
});
```

_Pourquoi le mot navigator ? Eh bien, c'est une référence au navigateur Netscape Navigator des années 90._

Centrez un élément h1 dans votre page HTML avec l'id "status". Si vous appliquez le code JavaScript ci-dessus à votre page, vous devriez voir s'afficher "En ligne". 

Mais cela ne met à jour l'élément h1 que lorsque la page se charge. Ajoutons des écouteurs d'événements offline et online pour mettre à jour l'affichage de l'état chaque fois que l'un de ces événements se déclenche.

```javascript
window.addEventListener("offline", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = "Hors ligne";
});

window.addEventListener("online", (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = "En ligne";
});
```

Nous pouvons aller dans l'onglet Application des outils de développement Chrome et cliquer sur ServiceWorker pour configurer le navigateur afin qu'il réponde comme s'il était hors ligne. 

Cochez et décochez la case Hors ligne plusieurs fois. Vous devriez voir l'affichage de l'état répondre immédiatement aux événements offline et online qui sont déclenchés.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/offline_check_nav_online.PNG)
_Outils de développement Chrome > Onglet Application > Service Workers > Case à cocher Hors ligne_

## Approfondissons un peu

À première vue, ce qui précède semble être une bonne solution qui est assez simple. Malheureusement, lorsque nous lisons davantage sur la propriété online de navigator et les événements online et offline, nous découvrons qu'il y a un problème. 

[Recherche de navigator.onLine sur CanIUse.com](https://caniuse.com/#search=navigator.onLine) montre un support généralisé pour le statut en ligne | hors ligne que la propriété fournit. Cependant, en regardant les notes sous le tableau de support, nous voyons que 

> "En ligne ne signifie pas toujours connexion à Internet. Cela peut aussi simplement signifier connexion à un réseau."

Hmm, cela jette un peu de désarroi dans les travaux.

Donc, si vous voulez vraiment déterminer l'état en ligne du navigateur, vous devriez développer des moyens supplémentaires pour vérifier.

Prenons également un moment pour consulter la [référence des docs MDN pour navigator.onLine](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorOnLine/onLine). Les docs web MDN confirment les informations de CanIUse.com et ajoutent des notes supplémentaires. 

> _"Les navigateurs implémentent cette propriété différemment... vous ne pouvez pas supposer qu'une valeur vraie signifie nécessairement que le navigateur peut accéder à Internet. Vous pourriez obtenir des faux positifs..."_

Et cela confirme nos craintes concernant l'utilisation de la propriété online de navigator comme solution pour détecter une connexion Internet. C'est une solution qui peut semer le chaos dans nos applications qui dépendent de la connaissance de la disponibilité des sources de données externes. 

Un exemple est lorsque nous essayons de déterminer si une Progressive Web App est en ligne ou non. MDN recommande même,

> _"...si vous voulez vraiment déterminer l'état en ligne du navigateur, vous devriez développer des moyens supplémentaires pour vérifier."_

Une recherche rapide sur le web pour _"navigator online not working"_ révèle divers posts de forum où ceux qui dépendent de cette propriété ont rencontré des problèmes.

## Quelle est donc la solution ? 

Nous devons savoir quand notre application est vraiment connectée à Internet et pas seulement à un routeur ou à un réseau local. Revenons à notre fichier JavaScript et recommencez.

L'idée est de faire une requête et de la gérer élégamment avec une gestion des erreurs si elle échoue. Si la requête réussit, nous sommes en ligne, et si elle échoue, nous ne le sommes pas. 

Nous allons demander une petite image à intervalles réguliers pour déterminer l'état en ligne. Le JavaScript moderne fournit l'API Fetch et le code asynchrone avec Async & Await. Nous allons utiliser ces outils pour atteindre notre objectif.

### checkOnlineStatus()

Commençons par créer une fonction fléchée asynchrone nommée checkOnlineStatus. La fonction retournera vrai ou faux comme la propriété online de navigator.

À l'intérieur de la fonction, nous allons configurer un bloc try où nous attendrons une requête fetch pour une image d'un pixel. Assurez-vous que votre service worker ne met pas cette image en cache. 

Les codes de réponse HTTP entre 200 et 299 indiquent un succès, et nous retournerons le résultat de la comparaison du code de statut. Cela sera vrai si le statut de la réponse est compris entre 200 et 299 et faux sinon. 

Nous devons également fournir un bloc catch qui attrape l'erreur si la requête échoue. Nous retournerons faux dans le bloc catch pour indiquer que nous sommes définitivement hors ligne si cela se produit.

```javascript
const checkOnlineStatus = async () => {
  try {
    const online = await fetch("/1pixel.png");
    return online.status >= 200 && online.status < 300; // soit vrai soit faux
  } catch (err) {
    return false; // définitivement hors ligne
  }
};
```

Ensuite, nous allons utiliser la méthode setInterval et lui passer une fonction anonyme asynchrone. La fonction asynchrone attendra le résultat de notre fonction checkOnlineStatus. Nous utiliserons ensuite une instruction ternaire avec le résultat pour afficher l'état en ligne actuel. 

Pour tester cet exemple, définissez le délai d'intervalle à toutes les 3 secondes (3000 millisecondes). Cela est vraiment trop fréquent, cependant. Vérifier toutes les 30 secondes (30000 millisecondes) peut être suffisant pour vos besoins réels.

```javascript
setInterval(async () => {
  const result = await checkOnlineStatus();
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = result ? "En ligne" : "Hors ligne";
}, 3000); // probablement trop souvent, essayez 30000 pour toutes les 30 secondes
```

Avec notre nouveau code sauvegardé, revisitons l'onglet Application dans les outils de développement Chrome pour tester la réponse hors ligne.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/offline_check_fetch.PNG)
_Outils de développement Chrome > Onglet Application > Service Workers > Case à cocher Hors ligne_

J'ai presque oublié d'inclure l'écouteur d'événement de chargement avec la fonctionnalité asynchrone ! La détection de l'événement de chargement est probablement seulement importante si vous avez une Progressive Web App utilisant un service worker pour la disponibilité hors ligne. Sinon, votre page web ou application ne se chargera tout simplement pas sans connexion. 

Voici le nouvel écouteur d'événement de chargement : 

```
window.addEventListener("load", async (event) => {
  const statusDisplay = document.getElementById("status");
  statusDisplay.textContent = (await checkOnlineStatus())
    ? "En ligne"
    : "Hors ligne";
});
```

## Une dernière pensée

Le code d'intervalle ci-dessus est bon pour afficher un statut de connexion dans votre application. Cela dit, je ne suggère pas de dépendre d'un statut de connexion qui a été vérifié 20 ou 30 secondes avant de faire une requête de données critique dans votre application. 

Par conséquent, vous devriez appeler la fonction checkOnlineStatus directement avant la requête et évaluer la réponse avant de demander des données.

```javascript
const yourDataRequestFunction = async () => {
    const online = await checkOnlineStatus();
    if (online) {
    	// faire une requête de données
    }
}
```

## Conclusion

Bien que navigator.onLine soit largement supporté, il fournit des résultats peu fiables pour déterminer si nos applications sont vraiment connectées à Internet. En utilisant l'API Fetch et JavaScript asynchrone, nous pouvons rapidement coder une solution plus fiable. 

[Voici un lien vers le gist du code](https://gist.github.com/gitdagray/f310be81be217750fc9d2b233e2ae70c) sur GitHub, et voici un tutoriel vidéo que j'ai préparé : 

%[https://youtu.be/hIaGzJ3txqM]