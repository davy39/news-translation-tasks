---
title: 'Progressive Web Apps 101 : le Quoi, le Pourquoi et le Comment'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2018-07-20T19:11:47.000Z'
originalURL: https://freecodecamp.org/news/progressive-web-apps-101-the-what-why-and-how-4aa5e9065ac2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2tyNWs0uYC0q-gwyWj8BTw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Progressive Web Apps 101 : le Quoi, le Pourquoi et le Comment'
seo_desc: 'What is a Progressive Web App? Why do we need one? How can we build one?

  Have you ever seen an “Add to Home Screen” banner, like above, while browsing a
  website? When you click the button, the “application” installs itself in the background.
  When you...'
---

#### Qu'est-ce qu'une Progressive Web App ? Pourquoi en avons-nous besoin ? Comment en construire une ?

Avez-vous déjà vu une bannière "Ajouter à l'écran d'accueil", comme ci-dessus, en naviguant sur un site web ? Lorsque vous cliquez sur le bouton, l'« application » s'installe en arrière-plan. Lorsque vous ouvrez cette application qui se trouve maintenant dans votre tiroir d'applications, vous pouvez naviguer dans la même expérience que vous faisiez sur votre navigateur, mais maintenant directement sur votre téléphone mobile.

Ce que vous avez maintenant est une application mobile qui a été téléchargée depuis une application web. Tout cela, sans même avoir à voir la face d'un magasin d'applications.

Obtenir l'application était si facile ! Mais ce n'est même pas la meilleure partie. Lorsque vous ouvrez cette application, vous pourrez naviguer dans le contenu même lorsque vous n'avez pas internet. Vous avez un accès hors ligne à l'application ! N'est-ce pas cool ?

Ce que vous avez rencontré est une Progressive Web App (PWA). Une PWA vous permet d'installer l'application directement depuis la fenêtre du navigateur, est disponible sur votre téléphone comme une application native et fonctionne hors ligne, tout comme une application native.

Mais que signifie vraiment pour une application web d'être progressive ? Plongeons plus profondément dans ce que sont les applications web progressives, pourquoi je pense qu'elles sont meilleures que les applications natives, et ce qui les distingue des applications web traditionnelles.

### Qu'est-ce qu'une Progressive Web App (PWA) ?

Le terme Progressive Web App a été inventé par [Alex Russell](https://www.freecodecamp.org/news/progressive-web-apps-101-the-what-why-and-how-4aa5e9065ac2/undefined) et Frances Berriman. Selon les mots d'Alex :

> Les Progressive Web Apps sont simplement des sites web qui ont pris toutes les bonnes vitamines.

Ce n'est pas un nouveau framework ou une nouvelle technologie. C'est un ensemble de meilleures pratiques pour faire fonctionner une application web de manière similaire à une application de bureau ou mobile. Le rêve est d'avoir une expérience si uniforme et transparente que l'utilisateur est incapable de faire la différence entre une Progressive Web App et une application mobile native.

Les applications web progressives offrent des expériences utilisateur grâce à l'amélioration progressive. Cela signifie essentiellement qu'une PWA effectuera les mêmes fonctions sur un nouvel iPhone 8 que sur un iPhone de génération précédente. Bien sûr, certaines fonctionnalités peuvent ne pas être disponibles, mais l'application continue de fonctionner et de performer comme elle le devrait.

### Pourquoi avons-nous besoin d'une Progressive Web App ?

Avant de comprendre pourquoi nous avons besoin d'une application web progressive, parlons de certains des défis auxquels nous sommes confrontés aujourd'hui avec les applications natives et web.

**Vitesse d'internet** : vous ne vous en rendez peut-être pas compte selon l'endroit où vous vivez, mais 60 % de la population mondiale utilise encore l'internet 2G. Même aux États-Unis, certaines personnes doivent utiliser le dialup pour accéder à internet.

**Chargement lent du site web** : savez-vous combien de temps un utilisateur attend avant de cliquer sur le bouton "Fermer X" si un site web est trop lent ? Trois secondes ! 53 % des utilisateurs abandonnent un site web s'il est trop lent.

**Friction élevée** : les gens ne veulent pas installer d'applications natives. Un utilisateur moyen installe 0 application par mois.

**Engagement des utilisateurs** : les utilisateurs passent la plupart de leur temps dans des applications natives, mais la portée du web mobile est presque trois fois celle des applications natives. Par conséquent, la plupart des utilisateurs ne sont pas activement engagés. Cependant, les utilisateurs passent 80 % de leur temps sur seulement leurs trois applications natives principales.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o2eA_ZR6hnUVTH2EvIAYqg.png)
_Engagement des utilisateurs sur le web mobile vs les applications_

Les PWA aident à résoudre ces problèmes. Il existe plusieurs raisons d'utiliser une application web progressive, mais voici quelques-unes des principales capacités qu'elle offre :

1. **R**apide : les PWA offrent des expériences constamment rapides. Du moment où un utilisateur télécharge une application au moment où il commence à interagir avec elle, tout se passe très rapidement. Parce que vous pouvez mettre en cache les données, il est extrêmement rapide de démarrer à nouveau l'application même sans accéder au réseau.
2. **I**ntégration de l'expérience utilisateur : les PWA se comportent et se sentent comme des applications natives. Elles se trouvent dans l'écran d'accueil de l'utilisateur, envoient des notifications push comme les applications natives et ont accès aux fonctionnalités de l'appareil comme les applications natives. L'expérience semble transparente et intégrée.
3. **F**iabilité de l'expérience : avec l'aide des service workers, nous pouvons peindre de manière fiable une image sur l'écran de l'utilisateur même lorsque le réseau a échoué.
4. **E**ngageant : parce que nous pouvons envoyer des notifications à un utilisateur, nous pouvons vraiment augmenter l'engagement en gardant l'utilisateur informé et engagé avec l'application.

En bref, c'est **FIRE.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*maLaYJoCMBNabnUdrgwPMQ.jpeg)

### Comment construire une Progressive Web App

Google a publié une [liste de contrôle](https://developers.google.com/web/progressive-web-apps/checklist) pour les Progressive Web Apps. Je vais passer en revue quatre exigences minimales pour qu'une application soit une PWA :

#### 1. Manifestation de l'application web

![Image](https://cdn-media-1.freecodecamp.org/images/1*LhaR74lzxYyeKwNOWh9oNQ.png)
_Un exemple de fichier manifest.json_

Ce n'est qu'un fichier `json` qui donne des métainformations sur l'application web. Il contient des informations comme l'icône de l'application (que l'utilisateur voit après l'avoir installée dans son tiroir d'applications), la couleur de fond de l'application, le nom de l'application, le nom court, et ainsi de suite. Nous pouvons écrire ce fichier manifest nous-mêmes ou nous pouvons utiliser des [outils](https://app-manifest.firebaseapp.com/) pour en générer un pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yzOwzdDG48AlJcPrSby1kw.png)
_Vous pouvez générer automatiquement un fichier manifest en utilisant les outils de Google._

#### 2. Service Workers

Les Service Workers sont des workers pilotés par événements qui s'exécutent en arrière-plan d'une application et agissent comme un proxy entre le réseau et l'application. Ils sont capables d'intercepter les requêtes réseau et de mettre en cache des informations pour nous en arrière-plan. Cela peut être utilisé pour charger des données pour une utilisation hors ligne. Ils sont un script `javascript` qui écoute des événements comme fetch et install, et ils effectuent des tâches.

Voici un exemple de `serviceworker.js`

```javascript
self.addEventListener('fetch', event => {
    // mise en cache pour la visualisation hors ligne
    const {request} = event;
    const url = new URL(request.url);
    if(url.origin === location.origin) {
        event.respondWith(cacheData(request));
    } else {
        event.respondWith(networkFirst(request));
    }
});

async function cacheData(request) {
    const cachedResponse = await caches.match(request);
    return cachedResponse || fetch(request);
}
```

#### 3. Icône

Cela est utilisé pour fournir une icône d'application lorsque l'utilisateur installe la PWA dans son tiroir d'applications. Une image jpeg fera simplement l'affaire. L'outil de manifest que j'ai mis en évidence ci-dessus aide à générer des icônes pour plusieurs formats, et je l'ai trouvé très utile.

#### 4. Servi via HTTPS

Pour être une PWA, l'application web doit être servie via un réseau sécurisé. Avec des services comme Cloudfare et LetsEncrypt, il est vraiment facile d'obtenir un certificat SSL. Être un site sécurisé n'est pas seulement une meilleure pratique, cela établit également votre application web comme un site de confiance pour les utilisateurs, démontrant la confiance et la fiabilité, et évitant les attaques de l'homme du milieu.

**Note : Ceci est la partie 1 d'une série en 2 parties. Dans la prochaine partie, nous créerons une Progressive Web App à partir de zéro avec un squelette index.html. [Consultez la partie 2 ici.](https://medium.freecodecamp.org/progressive-web-apps-102-building-a-progressive-web-app-from-scratch-397b72168040)**

Avez-vous appris quelque chose de nouveau ? Avez-vous des commentaires ? Connaissez-vous une DevJoke ? [Tweetez-moi @shrutikapoor08](https://twitter.com/shrutikapoor08)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Pourquoi les programmeurs se confondent-ils entre Halloween et Noël ?<br>Parce que OCT 31 = DEC 25 <a href="https://twitter.com/hashtag/DevJokes?src=hash&amp;ref_src=twsrc%5Etfw">#DevJokes</a> <a href="https://twitter.com/hashtag/WorkChat?src=hash&amp;ref_src=twsrc%5Etfw">#WorkChat</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1010257045566586880?ref_src=twsrc%5Etfw">22 juin 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>