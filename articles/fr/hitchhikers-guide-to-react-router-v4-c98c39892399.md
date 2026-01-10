---
title: 'Le Guide du routard de React Router v4 : la valeur cachée de la configuration
  des routes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T14:23:26.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hkvZOkK2Y-HTKLCI
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Le Guide du routard de React Router v4 : la valeur cachée de la configuration
  des routes'
seo_desc: 'By Eduardo Vedes

  Welcome to the Hitchhiker’s Guide to React Router v4, Part IV!

  Now that we’ve learned about recursive routes, let’s get back to our initial boilerplate,
  to avoid mixing concerns, and learn how to create a route configuration array.

  S...'
---

Par Eduardo Vedes

Bienvenue dans le Guide du routard de React Router v4, Partie IV !

Maintenant que nous avons appris les routes récursives, revenons à notre modèle initial pour éviter de mélanger les préoccupations, et apprenons à créer un tableau de configuration de routes.

Alors, pour résumer un peu ce que nous avons fait au début, jetons un coup d'œil à notre fichier **routes.js** initial :

![Image](https://cdn-media-1.freecodecamp.org/images/uweHGbrLczGHKPDEXVe34FNAOo5OTMW32bbv)
_**routes.js (fichier initial)**_

Notre composant **Routes** retourne un **div** avec une **NavBar** et un **Switch** où nous avons défini toutes les routes de notre application.

Notre première étape dans cette Partie 4 sera de définir un tableau de routes.

### Tableau de routes

![Image](https://cdn-media-1.freecodecamp.org/images/AfI92QlBlYm6ovQJGTLD9XjyaO0pdNKJUSuk)
_**tableau de configuration des routes**_

J'ai examiné nos routes et créé ce tableau qui définit chaque route et sous-route que nous avions dans notre application.

Super ! Maintenant, quoi ?!? ?

### Refactoriser les anciennes routes codées en dur

Maintenant, nettoyons nos routes codées en dur et le Switch !

![Image](https://cdn-media-1.freecodecamp.org/images/eGOQoXHqYMhhKHus0C0YcGdUR6Rygv7J40XV)
_**composant Routes amélioré**_

Oui ! Adieu toutes ces lignes de code. Que faisons-nous vraiment ?

Eh bien, nous parcourons le tableau de routes en utilisant un rappel ES6 (flèche grasse) pour retourner un composant abstrait appelé **<MakeRouteWithSubRoutes />**. Nous lui passons une clé (juste pour les besoins d'indexation de React) et nous y étalons également les informations de route.

#### Composant <MakeRouteWithSubRoutes />

En attendant, nous devons créer ce composant. J'ai décidé de le créer à part et de l'importer dans le fichier **routes.js**.

![Image](https://cdn-media-1.freecodecamp.org/images/q6WgEVi9gJUXYvyQEJklbude-zcMB5nhNDya)
_**Composant MakeRouteWithSubRoutes**_

D'accord, ce composant **<MakeRouteWithSubRoutes/>** prend chaque route que vous lui passez et retourne un composant **<Route/>** de React Router.

En tant que props, nous avons le **path** et la méthode render, qui invoquera le **route.component** que vous souhaitez rendre (en lui passant ensuite les props étalés et les sous-routes qu'il doit connaître).

Ces routes proviennent du tableau de configuration des routes — compris ? Super ! ?

#### TopicList (Sous-routage)

Cela dit, jetons un coup d'œil au composant **TopicList** car c'est celui qui reçoit les sous-routes du tableau de configuration des routes :

![Image](https://cdn-media-1.freecodecamp.org/images/VZQlFJucdpf7VnVtnpsPgxPxz23EoeOxc2cI)
_**Composant TopicList avec sous-routage**_

Alors, que se passe-t-il ici ? Notre **TopicList** importe maintenant le composant **<MakeRouteWithSubRoutes/>** et le réutilise avec les routes qu'il a reçues.

Il fait également un **routes.map** sur les sous-routes et répète le processus effectué dans le fichier **routes.js**.

Prenez un moment pour le comprendre et jouer avec !

#### De plus en plus de sous-routage

Comme vous pouvez le voir, cela fonctionne plutôt bien. C'est abstrait, il y a séparation des préoccupations. Le **<MakeRoutesWithSubRoutes/>** est un composant ou une fonction sans état assez facile à utiliser qui ne se soucie pas du contenu du routage. Il route simplement ce que vous lui donnez.

Et si nous voulions faire plus de sous-routage ?

Facile ! Continuez simplement à développer ou à redessiner votre tableau de configuration des routes !

![Image](https://cdn-media-1.freecodecamp.org/images/masX7pCVdt9vELBX-3d74HMYz1D9W4FJ5sif)
_**tableau de configuration des routes dynamique**_

Vous voyez ? Les routes de **/Topics/:topicId** pourraient simplement être un tableau comme ses routes parentes. Mais j'ai décidé de faire mieux et d'invoquer une fonction qui appelle une API et retourne un nouveau tableau de routes (imaginez simplement qu'elle récupère l'API ?).

Alors, comment pouvons-nous vérifier cela dans l'application ?

Mettons un **console.log** à l'intérieur du composant **TopicDetail** et vérifions ce qu'il reçoit :

![Image](https://cdn-media-1.freecodecamp.org/images/tnagiA612FCg0Nc6-9Cp2eFRoKoH657lRPaa)

J'invoque **routes()** dans **console.log** parce que maintenant cette sous-route est une fonction ! Vous vous souvenez ? Tout va bien ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/ACsSVAt8jg--jGIR993-N0njgW4nndEuTiCv)
_console.log(routes())

Oui, maman ! Nous l'avons fait ! Nous recevons les routes dynamiquement et les propageons dans nos sous-routes et composants. C'est si génial !

### NoMatch et routes ambiguës

Attendez ! Où est notre composant **NoMatch** ?

D'accord, introduisons-le dans notre tableau de configuration des routes :

![Image](https://cdn-media-1.freecodecamp.org/images/nmr0AktuM0RDiaOowU0xlylfkBuGUtxn-pT9)

Observez que **:WhereTheHeckIsThat** est une variable car elle a le deux-points devant elle.

Que devrions-nous attendre ?

Voyons cela en action :

![Image](https://cdn-media-1.freecodecamp.org/images/IoGOuriU8ZoTVqmrnwWef3nBO-Y-PRpduHxy)

Wow ! En fait, il rend le **NoMatch** mais il rend aussi la **Vue d'accueil**. Pourquoi ?

Eh bien, ce qui se passe, c'est que dans notre modèle initial, nous avions un **<Switch />** qui sélectionnait la première **<Route />** qui correspondait au chemin, vous vous souvenez ?

Donc maintenant, comme nous n'avons pas le switch, il peut correspondre à plus d'un chemin à la fois !

Ce sont ce qu'on appelle les routes ambiguës. Le routeur a correspondu à **/Home** et en même temps à **/:WhereTheHeckIsThat** car c'est une sorte de joker qui accepte tout.

Comment corrigeons-nous cela ?

Simple : récupérez **<Switch />** !

![Image](https://cdn-media-1.freecodecamp.org/images/kHsKnL4TduMHuJHwGmGcz-91I2wSsoCwAY-L)
_**&lt;Switch /&gt; est de retour pour envelopper notre route.map !**_

![Image](https://cdn-media-1.freecodecamp.org/images/rKSsmATtmMNYywVeLz9U4RVeRUhZjp2Obtd2)
_**Le composant Home était la seule correspondance**_

![Image](https://cdn-media-1.freecodecamp.org/images/B1QStJLEuT8-FT-i3dQk9wTybnppVKfjH3hR)
_**Les chemins inconnus déclenchent le composant NoMatch**_

Comme vous pouvez le voir ci-dessus, maintenant le **/Home** est rendu seul, car **<Switch />** l'a trouvé et l'a retourné immédiatement.

Si vous mettez un chemin inconnu dans l'URL, il déclenche le **:/WhereTheHeckIsThat** et rend le composant **NoMatch** par défaut.

Excellent travail ! Tout fonctionne comme nous l'avions prévu et maintenant nous avons une **configuration de tableau de routes puissante** qui nous permet d'avoir beaucoup de flexibilité.

C'est vraiment la valeur cachée d'avoir une abstraction et de définir un tableau de configuration de routes !

### Dernier mais non des moindres

C'est la fin du Guide du routard de React Router v4.0 !

Il y a encore quelques choses à surveiller, mais je préfère vous laisser plonger un peu dans les modèles que nous avons construits et chercher ce dont vous avez besoin dans la documentation de React Router [site web](https://reacttraining.com/react-router/web/guides/philosophy).

J'ai eu tellement de plaisir à faire ce guide que je pense que je vais commencer à écrire de plus en plus :)

C'était bien non seulement parce que j'ai pu vous enseigner quelque chose, mais aussi parce que j'ai beaucoup appris dans ce processus.

#### Dépôt GitHub

Les changements que j'ai apportés à l'application, pour produire cet article, peuvent être trouvés dans mon dépôt GitHub [repo](https://github.com/evedes/ReactRouter_BoilerPlate_04) pour la Partie 4.

#### Bibliographie

Pour faire cet article, j'ai utilisé la documentation de React Router que vous pouvez trouver [ici](https://reacttraining.com/react-router/core/guides/philosophy).

Tous les autres sites que j'ai utilisés sont liés tout au long du document pour ajouter des informations ou fournir un contexte à ce que j'ai essayé de vous expliquer.

Cet article est la partie 4 d'une série intitulée « Guide du routard de React Router v4 »

* **[Partie I : Comprendre React Router en 20 minutes](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Partie II : [match, location, history] — vos meilleurs amis !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Partie III : chemins récursifs, à l'infini et au-delà !](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8/)**

? Merci beaucoup !