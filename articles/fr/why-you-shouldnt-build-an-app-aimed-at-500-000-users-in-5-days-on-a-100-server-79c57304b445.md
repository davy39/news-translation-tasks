---
title: Pourquoi vous ne devriez pas construire une application visant 500 000 utilisateurs
  en 5 jours sur un serveur à 100 $
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T17:39:00.000Z'
originalURL: https://freecodecamp.org/news/why-you-shouldnt-build-an-app-aimed-at-500-000-users-in-5-days-on-a-100-server-79c57304b445
coverImage: https://cdn-media-1.freecodecamp.org/images/1*11CoLIPHgvJBhWAgZTS4kA.png
tags:
- name: lean startup
  slug: lean-startup
- name: pokemon go
  slug: pokemon-go
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous ne devriez pas construire une application visant 500 000
  utilisateurs en 5 jours sur un serveur à 100 $
seo_desc: 'By Howard Lo

  A few days ago, I read Erik Duindam’s “How I built an app with 500,000 users in
  5 days on a $100 server” article. Basically, he spent an extra 2–3 hours (totaling
  24) to make his app (GoSnap) scalable by using a CDN and some optimized da...'
---

Par Howard Lo

Il y a quelques jours, j'ai lu l'article d'[Erik Duindam](https://www.freecodecamp.org/news/why-you-shouldnt-build-an-app-aimed-at-500-000-users-in-5-days-on-a-100-server-79c57304b445/undefined) « Comment j'ai construit une application avec 500 000 utilisateurs en 5 jours sur un serveur à 100 $ ». Basiquement, il a passé 2 à 3 heures supplémentaires (pour un total de 24) pour rendre son application (GoSnap) scalable en utilisant un CDN et des bases de données optimisées. Il critique une autre application (GoChat) pour avoir construit une application qui avait des problèmes techniques au lancement.

Ceux qui lisent son article devraient prendre en compte quelques points :

#### Il est un bon développeur.

Bien meilleur que moi.

Je doute pouvoir faire en 24 heures ce qu'il a fait. Il est rapide et sait ce qu'il fait.

Pour lui, 2 à 3 heures ne sont pas un gros problème. Vous pouvez les soustraire de votre temps de sommeil et vous sentir mal pendant une journée. Mais que se passe-t-il si vous n'êtes pas un développeur chevronné ? 24 heures peuvent devenir une semaine, et 2 à 3 heures peuvent représenter presque une journée complète.

Si vous êtes en train de vous précipiter pour lancer quelque chose parce que vous craignez que quelqu'un d'autre ait la même idée (ce qui est plus courant que vous ne le pensez), une journée complète peut faire ou défaire votre projet.

Évaluez cela pour vous-même, mais je préfère être le premier avec une solution à 90 % plutôt que le second avec une solution à 100 %.

#### %Échec > %Succès

Les applications que vous construisez sont beaucoup plus susceptibles d'échouer que de réussir.

Erik parle du point de vue d'un gagnant. Les gagnants parlent beaucoup plus fort que les perdants, dont les histoires d'échecs ne sont probablement pas aussi percutantes (ou excitantes) que celle d'Erik.

Si vous faites une recherche rapide sur les applications liées à Pokemon Go, il y a des dizaines d'applications échouées pour chaque application réussie.

À moins d'avoir des partenariats massifs (Google et Nintendo, dans le cas de Pokemon Go), l'app store est essentiellement un jeu de chiffres géant. Oui, vous pouvez passer 10 % de temps en plus pour rendre votre application scalable. Mais en supposant que votre chance d'échec est si élevée, dans la plupart des cas, ce temps supplémentaire de 10 % sera gaspillé. Si vous passez 10 % de temps en plus pour rendre tous vos Produits Viables Minimaux (MVPs) scalables, mais que vous échouez 9 fois, c'est un MVP de moins que vous auriez pu construire.

Et allez-vous vraiment vous arrêter à 10 % ? Avez-vous autant de contrôle sur vous-même et une vue d'ensemble de ce que vous faites ?

Pour moi, ces 10 % peuvent rapidement devenir 20 % parce que « bon, j'ai mis un CDN sur mon application, pourquoi ne pas mettre en place un caching, cela ne prendra que 10 % de plus ».

Allez-y au minimum ou faites-le à fond. Tracer la ligne ailleurs n'est pas optimal.

#### Échouer n'est pas si grave.

Erik lui-même a mis à jour son article quelques jours plus tard :

> La page Google Play dit que [GoChat] est « de retour à 100 % » avec « plus de 2 millions d'utilisateurs ».

GoChat a lancé un MVP, ne savait pas qu'ils auraient autant de traction, et leur code MVP médiocre a plié sous la charge. GoChat a échoué.

Ou pas ?

Parce que même si GoChat est tombé, il attire toujours plus d'utilisateurs que GoSnap d'Erik, qui est construit pour être scalable. Ce sont des produits différents, bien sûr, mais le temps supplémentaire de 10 % qu'Erik a passé sur GoSnap aurait-il pu être mieux utilisé pour atteindre le marché des applications 2 à 3 heures plus tôt ? Erik aurait-il pu avoir plus d'utilisateurs avec 2 à 3 heures d'avance et un crash technique ensuite ?

Difficile de dire quels auraient été les résultats, mais c'est intéressant d'y penser.

Même si le code de GoChat les a trahis, ils se sont rattrapés. Ils ont optimisé dans la deuxième étape et ont tout de même capté plus de 2 millions d'utilisateurs. L'échec des MVPs non scalables ne semble pas les avoir trop affectés en fin de compte.

GoChat aurait-il pu avoir plus d'utilisateurs à ce stade s'ils n'avaient pas crashé ? Peut-être. Mais ils n'ont certainement pas manqué le coche comme le suggère Erik, alors pourquoi s'inquiéter ?

Il est préférable de lancer et d'avancer plutôt que de manquer complètement le train parce que vous étiez trop occupé à scalabiliser.

Le problème avec le « scale » est qu'à l'extrémité supérieure, il y a tellement d'utilisateurs à partager que vous pouvez vous permettre de rencontrer des problèmes initialement et de toujours capturer une bonne part de marché après la correction.

À l'extrémité inférieure du « scale », il n'y a rien. Vous n'avez rien de votre côté sauf la vitesse d'exécution. Vous devez y arriver rapidement. Demandez simplement aux dizaines d'autres applications qui ne sont pas téléchargées.

**_Section auto-promotion !_**  
_J'ai créé [rabbut.com](https://rabbut.com/?ref=h0), un outil qui vous permet de collecter des emails ici sur Medium (et ailleurs). Oh, regardez, en voici un maintenant :_

[**Vous cherchez mes anciennes histoires ? J'en ai quelques-unes. Ici.**](https://powered.by.rabbut.com/s/lbYA?c=10)  
[_Chercher des anciennes histoires est un vrai casse-tête sur Medium. Cliquez ici pour un raccourci._powered.by.rabbut.com](https://powered.by.rabbut.com/s/lbYA?c=10)

_Aussi, je donne mon eBook gratuit sur le lancement d'une startup. Surtout utile pour les personnes qui ne savent pas comment lancer une startup :_

[**Les 10 premières personnes à s'abonner reçoivent mon eBook gratuit.**](https://powered.by.rabbut.com/e/wNXK?c=0)  
[_Comment lancer votre startup en tant qu'inconnu._powered.by.rabbut.com](https://powered.by.rabbut.com/e/wNXK?c=0)

_Man, ces trucs [rabbut](https://rabbut.com/?ref=h00) sont partout maintenant. Je me demande où on pourrait en obtenir un…_