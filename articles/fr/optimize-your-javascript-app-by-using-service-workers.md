---
title: Comment optimiser votre application JavaScript en utilisant des service workers
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-09-02T12:31:08.000Z'
originalURL: https://freecodecamp.org/news/optimize-your-javascript-app-by-using-service-workers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca08e740569d1a4ca4963.jpg
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
seo_title: Comment optimiser votre application JavaScript en utilisant des service
  workers
seo_desc: 'Every now and then we hear about optimizing something. There are different
  kinds of optimizations we can do to make our apps faster and more efficient, or
  to save time or memory. This article will cover one of those methods — s_ervice_
  w_orkers._

  TL;...'
---

De temps en temps, nous entendons parler d'optimisation. Il existe différents types d'optimisations que nous pouvons faire pour rendre nos applications plus rapides et plus efficaces, ou pour économiser du temps ou de la mémoire. Cet article couvrira l'une de ces méthodes — les *service workers*.

### TL;DR

Ce tutoriel explique ce qu'est un *service worker* et comment l'utiliser, en JavaScript. Il y a un exemple de code à la fin. Si vous souhaitez sauter la lecture, [ici](https://github.com/mihailgaberov/learn-service-workers) se trouve le dépôt Git et [ici](https://compassionate-brahmagupta-71d9b4.netlify.com/) vous pouvez voir une démonstration en direct.

### La Théorie

Voyons d'abord ce qu'est ce *worker* et quel *service* nous pouvons en tirer.

Le *service worker* est un [script simple](https://developers.google.com/web/fundamentals/primers/service-workers/). C'est du code JavaScript, que votre navigateur exécute en arrière-plan, séparément d'une page web.

Il est très pratique d'utiliser des service workers pour des fonctionnalités qui n'ont pas besoin d'une page web ou d'une interaction utilisateur. L'une des utilisations les plus courantes est l'interception et la gestion des requêtes réseau. Cela inclut la gestion d'un cache de réponses.

Voici un exemple simple de la façon d'inclure un service worker dans votre application.

Habituellement, dans le point d'entrée de votre application, vous ajoutez ce code :

```js
if ('serviceWorker' in navigator) {  
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js');  
    });
}
```

Cette façon d'utiliser les service workers est un peu améliorée par rapport à la méthode de base. La méthode de base implique d'appeler directement la méthode *register*() à l'intérieur de l'*instruction if*. Dans ce cas, nous utilisons l'événement de chargement de la fenêtre pour enregistrer le service worker après que la page ait fini de se charger. Après avoir fait cela, vous devez ajouter votre code de service worker dans le fichier *service-worker.js*. À ce stade, vous pourriez vouloir jeter un coup d'œil à mon fichier de service worker.

*Tous les principaux navigateurs supportent maintenant les Service Workers, et vous pouvez commencer à les utiliser immédiatement.*

### L'Exemple

Assez de théorie, construisons une application exemple réelle qui tirera parti de la fonctionnalité des service workers.

Imaginons que nous construisons une application qui doit charger un gros morceau de données. Cela pourrait être, par exemple, une belle grande image en plein écran que nous affichons sur la page d'accueil. Ou cela pourrait être un gros clip vidéo que nous devons attendre de charger. C'est un cas d'utilisation idéal pour qu'un service worker brille. Voyons comment.

Dans notre cas spécifique, nous utiliserons l'heure de l'horloge pour montrer l'avantage de l'utilisation des service workers. Ce que je veux dire, c'est que nous allons construire une application simple, montrant l'heure. Elle aura un gros bouton pour récupérer une belle grande image. Et elle fournira à l'utilisateur une option pour choisir **d'utiliser ou non** un service worker.

Voici une capture d'écran de son apparence :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_2K-IvfpcK017rGsX1Hsm8w.png align="left")

Ce que cette application démontre, c'est que lors de la récupération de l'image (en cliquant sur le bouton, wow !) avec un service worker actif — nous n'avons pas d'interface utilisateur bloquée (c'est-à-dire des champs, des boutons, etc.). Si vous choisissez de ne pas utiliser le service worker, vous aurez une interface utilisateur gelée pendant une certaine période. Lorsque le travail est terminé et que le thread principal se libère, il dégèlera l'interface utilisateur.

Si vous ne souhaitez pas cloner et exécuter le code vous-même, passez directement à la [démonstration en direct](https://compassionate-brahmagupta-71d9b4.netlify.com/).

### Conclusion

Cette démonstration des service workers en action nous montre l'avantage que nous obtenons en les utilisant. Surtout lorsque vous essayez de construire des applications JavaScript réactives et robustes. Aucun utilisateur ne veut se retrouver sur une page gelée pendant un temps inconnu, et aucun développeur ne devrait vouloir cela pour les utilisateurs de son application. En gardant cela à l'esprit, les service workers sont désormais un *must*. Et nous ne devrions pas les négliger.

? Merci d'avoir lu ! ?