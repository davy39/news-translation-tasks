---
title: Comment créer une application web VR multijoueur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T16:26:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-multiplayer-vr-web-app-7b989964fb38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cmZG_OoXi3eVMxALqspC_g.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: vr
  slug: vr
seo_title: Comment créer une application web VR multijoueur
seo_desc: 'By Srushtika Neelakantam

  In this article, we’ll learn about three great frameworks/libraries that allow any
  web developer to build a VR app that works on any device in minutes. It will also
  allow networked realtime interaction by peers from all over ...'
---

Par Srushtika Neelakantam

Dans cet article, nous allons découvrir trois excellents frameworks/bibliothèques qui permettent à tout développeur web de créer une application VR qui fonctionne sur n'importe quel appareil en quelques minutes. Elle permettra également une interaction en temps réel en réseau entre des pairs du monde entier.

La réalité virtuelle (VR) a atteint un niveau incroyable où elle n'a plus besoin d'introduction. Cependant, du point de vue d'un développeur, la création d'applications VR simples semble encore être une tâche complexe, sans parler des applications multijoueurs en réseau.

### Que allons-nous construire ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*cmZG_OoXi3eVMxALqspC_g.jpeg)
_Image prise lors du [WeAreDevelopers World Congress](https://www.wearedevelopers.com/congress/" rel="noopener" target="_blank" title="">WeAreDevelopers World Congress</a> par <a href="https://twitter.com/g33konaut/status/996753762172760065" rel="noopener" target="_blank" title=")_

À la fin de ce tutoriel, vous aurez une application VR similaire à celle de l'image ci-dessus. Elle comportera une scène VR de base où plusieurs utilisateurs pourront se connecter à votre application depuis leurs téléphones mobiles en accédant simplement à une URL dans le navigateur de leur téléphone.

Vous ne connaissez pas ou ne comprenez pas beaucoup des termes que je viens d'utiliser ? Ne vous inquiétez pas, nous allons examiner tout cela bientôt, et tout commencera à avoir du sens rapidement !

En gros, pour chaque utilisateur qui rejoint votre application, un nouvel avatar apparaîtra dans votre scène VR (Note : J'utilise simplement un terme fantaisiste 'avatar' pour cet ensemble de boîtes qui ressemble à peine à un être humain réel :P). Ces avatars tourneront/bougeront en temps réel, selon le mouvement des téléphones des utilisateurs dans la vie réelle.

Cette application a été démontrée lors de ma présentation au [WeAreDevelopers](https://www.wearedevelopers.com/congress/) World Congress 2018. Vous pouvez consulter les diapositives ci-dessous.

### Passer à la démonstration en direct

Le projet complet est hébergé sur [Glitch](http://glitch.com) — je pense que c'est le moyen le plus simple d'héberger vos projets communautaires ou vos démonstrations. Il permet également à plusieurs développeurs de collaborer sur un projet à distance. Vous devriez absolument le vérifier.

Instructions pour la [**démonstration en direct**](http://go.ably.io/vr-demo) :

* ouvrez le lien dans une fenêtre de navigateur sur votre ordinateur/mobile.
* ouvrez une autre instance de l'application dans une autre fenêtre de navigateur/mobile.

Vous pouvez voir l'avatar de chacune de ces instances dans l'autre. Essayez de déplacer le téléphone mobile dans l'air et vous verrez que l'avatar correspondant vu sur le navigateur de l'ordinateur bouge également. Si vous avez deux casques VR (même des cardboards sont bien), vous et un ami pouvez les mettre et voir les avatars de l'autre bouger dans la scène lorsque vous bougez la tête dans la vie réelle.

Amusez-vous un peu ou lisez la suite pour comprendre ce qui se passe et comment. Vous pouvez également consulter le code complet, hébergé sur GitHub. Assurez-vous de lire le fichier readme :

**Passer au [code source](https://github.com/ably/tutorials/tree/ably-multiplayer-vr-tutorial) complet sur GitHub.**

### Que allons-nous utiliser ?

Comme mentionné précédemment, notre objectif est d'accéder à la VR directement dans les navigateurs, sans avoir à télécharger quoi que ce soit. Nous utiliserons la bibliothèque [WebVR](https://webvr.info/) pour y parvenir.

WebVR est un framework web qui nous permet de créer des applications VR accessibles directement sur le web. Cela élimine complètement les téléchargements et installations lourds, ainsi que de rendre l'application VR indépendante du dispositif.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VwBq28_q_l0J86HQd4GkdQ.png)
_[Logo WebVR](http://webvr.info" rel="noopener" target="_blank" title=")_

Cependant, même si WebVR nous donne la capacité de tirer parti des nombreux avantages du web, il nécessite encore une quantité considérable de travail complexe. Cela peut, en fait, nécessiter des connaissances en WebGL et d'autres bibliothèques pour pouvoir créer une expérience fluide.

#### A-Frame

Cela tend à nouveau à être un goulot d'étranglement pour les développeurs du web pour créer quelque chose qui sera finalement servi sur le web lui-même. Et ainsi, l'équipe VR de Mozilla a construit un framework sur WebVR appelé [A-Frame](http://aframe.io).

A-Frame élimine complètement le code boilerplate de WebVR et permet aux développeurs de créer des applications VR avec des balises HTML personnalisées simples. Avec, bien sûr, JavaScript faisant fonctionner divers morceaux et pièces ensemble, comme toujours.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SGUnFgjYGIgK5dgm8q43Qw.png)
_[Logo VR A-Frame](http://aframe.io" rel="noopener" target="_blank" title=")_

#### Ably

En outre, nous utiliserons [Ably Realtime](http://ably.io) pour implémenter toute la fonctionnalité en temps réel — et multijoueur — dans l'application. Ably est une plateforme de livraison de données en temps réel qui résout le problème de livraison de messages en temps réel en offrant des fonctionnalités comme [Pub/Sub](https://www.ably.io/documentation/realtime/channels-messages) et [Presence](https://www.ably.io/documentation/realtime/presence) directement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PzBxXwB9ydQRyPJmgYR4BQ.png)
_[Logo Ably Realtime](http://ably.io" rel="noopener" target="_blank" title=")_

**Note** : Les limites pour un compte Ably gratuit (utilisé dans la démonstration en direct) vous permettent d'avoir un maximum de deux instances de l'application en cours d'exécution à tout moment. Si vous souhaitez avoir plus d'instances en cours d'exécution, consultez le forfait [self-service](https://www.ably.io/pricing/self-service) d'Ably et achetez plus de messages en conséquence.

#### Glitch

Comme vous le savez maintenant, chaque application WebVR peut être accessible depuis un simple navigateur. Cela signifie que nous devrons héberger nos fichiers afin de pouvoir y accéder sur un appareil mobile à l'aide d'une URL.

[Glitch](https://glitch.com/) est un moyen très pratique de faire cela. Vous pouvez simplement créer un nouveau projet. Une fois terminé, une URL est immédiatement disponible pour une utilisation sur n'importe quelle plateforme ou appareil.

### Authentification et attribution d'identifiants uniques

Premièrement, nous devrons configurer un serveur d'authentification qui vérifie les identifiants de nos utilisateurs et les authentifie avec Ably, tout en attribuant un `clientId` aléatoire à chacun d'eux. Cet `clientId` servira de moyen pour identifier chacun de ces avatars séparément, et gérer des informations telles que leurs mises à jour de position respectives, ainsi que leur apparition/disparition selon la connexion/déconnexion de l'utilisateur. Nous allons configurer un simple [serveur express](https://expressjs.com/) pour cela, comme montré ci-dessous :

Si vous observez de près, ce serveur express sert les fichiers présents dans le répertoire racine du projet. Assurez-vous donc que le fichier "index.html" que vous construisez par la suite se trouve dans le même dossier que le "auth-server".

Si vous souhaitez servir ces fichiers localement, plutôt que sur Glitch, remplacez le code pour la variable `listener` par le suivant :

Puisque ce n'est qu'un tutoriel, nous ne vérifions pas réellement les identifiants avant d'authentifier les clients. Idéalement, le serveur d'authentification aurait une étape de validation.

La structure du projet est simple, avec les fichiers suivants tous dans le même dossier parent :

* auth_server.js
* index.html
* main.js

### Commencer

Commençons par construire la configuration VR de base pour l'application. Nous utiliserons le système [entity-component-system](https://aframe.io/docs/0.7.0/introduction/entity-component-system.html) (ECS) d'A-Frame. ECS facilite la construction de n'importe quel objet dans la scène. Chaque objet est traité comme une entité qui diffère des autres entités par les divers composants (ou attributs) qui lui sont attachés.

Dans votre fichier HTML, commencez par ajouter le code squelette HTML :

Les références font respectivement référence à :

1. La bibliothèque JS [client](https://www.ably.io/download) d'Ably
2. Le framework [JQuery](https://code.jquery.com/)
3. La build JS [A-Frame](https://aframe.io/docs/0.8.0/introduction/installation.html)
4. Un fichier JS local ("main.js") où nous ajouterons la logique de l'application
5. Le composant de texte [contribué par la communauté](https://aframe.io/aframe-registry/) d'A-Frame pour ajouter facilement du texte stylisé à notre scène VR.

Tous les objets que nous souhaitons inclure dans notre scène VR doivent aller dans la balise `a-scene` dans notre fichier HTML, comme la scène ci-dessus (jeu de mots intentionnel) ! Cela est analogue à la balise `body` dans les documents HTML réguliers.

Ensuite, nous ajouterons toutes les ressources que nous souhaitons utiliser dans la balise `a-assets`. Ajouter toutes les ressources sous cette balise garantit que toutes vos ressources sont préchargées avant que votre application ne s'affiche. Cela évite une mauvaise première impression due au chargement lent d'une partie des ressources.

N'hésitez pas à utiliser vos propres ressources pour donner à l'application un aspect personnalisé ! Vous pouvez voir que nous avons ajouté deux nouvelles balises dans l'extrait de code ci-dessus, approfondissons-les :

`a-asset-item` — invoque les chargeurs de fichiers three.js. Vous pouvez utiliser cela pour charger tous les types de fichiers.

`a-mixin` — est une balise très utile qui permet la réutilisation de code en vous permettant de spécifier un ensemble de propriétés (composants) à appliquer à une seule entité. Vous pouvez lui donner un `id` et le référencer plusieurs fois comme nous le verrons. Nous aurons trois mixins, chacun spécifiant certains attributs pour l'avatar que nous avons l'intention de créer — les yeux, les pupilles et les bras.

Maintenant, ajoutons tous les éléments visuels statiques dans notre scène VR.

Comme vous pouvez le voir, nous avons implémenté l'application complète en utilisant ECS. Cependant, ce n'est pas la seule façon d'ajouter des objets à la scène. A-Frame vient avec quelques entités personnalisées telles que box, sphere, etc. Ces entités personnalisées sont appelées [primitives](https://aframe.io/docs/0.7.0/introduction/html-and-primitives.html#primitives).

Le code contient des commentaires très faciles à suivre qui expliquent ce que chaque ensemble entité-composant essaie d'implémenter dans notre application.

Pour les débutants en VR, **voici quelque chose d'intéressant** — un ciel est comme une couche qui couvre votre sphère à 360 degrés à l'intérieur de laquelle vous vous supposez debout lors de l'expérience d'une application VR. Il est généralement analogue au ciel dans la vie réelle qui peut être vu en haut et semble descendre près de l'horizon. Nous utilisons `a-sky` dans A-Frame pour ajouter un ciel et la ressource à utiliser peut être soit une image à 360 degrés, soit simplement une couleur unie.

Voici une autre partie intéressante. Nous avons besoin d'une entité **caméra**. Il s'agit d'une entité spéciale offerte par A-Frame. Elle capture la position et les valeurs de rotation en constante évolution de votre téléphone mobile lorsque vous utilisez une application VR alimentée par A-Frame dans le navigateur. L'entité tire parti des divers capteurs gyroscopiques de votre téléphone pour y parvenir sous le capot. Sur un ordinateur, l'entité caméra suit les [contrôles WASD](https://aframe.io/docs/0.8.0/components/wasd-controls.html#sidebar) pour capturer la position et la rotation.

Voici comment nous pouvons ajouter une entité caméra. Nous pouvons optionnellement lui donner une forme et une animation, ce qui nous aide à suivre son mouvement en servant de curseur.

À la fin de cette section, votre application VR devrait idéalement ressembler à ce qui est montré ci-dessous. Mais seulement si vous n'avez pas remplacé les ressources par les vôtres, bien sûr !

![Image](https://cdn-media-1.freecodecamp.org/images/1*JNth10uakAwE1wwWKY5lJw.png)
_Premier aperçu_

Voilà ! Nous venons de terminer la configuration de la scène VR de base.

Il est maintenant temps d'ajouter quelques fonctionnalités — pour faire apparaître, disparaître et déplacer les avatars en temps réel lorsque les utilisateurs se connectent et se déconnectent de votre application, ou déplacent simplement leur téléphone.

### Ajout de fonctionnalités en temps réel

Il est temps d'ajouter un peu de magie à notre scène VR. En utilisant Ably, il est très facile de l'implémenter. Nous utiliserons [Pub/Sub](https://www.ably.io/documentation/realtime/channels-messages) et [Presence](https://www.ably.io/documentation/realtime/channels-messages), qui sont tous deux offerts comme des fonctionnalités prêtes à l'emploi par Ably.

Commencez par connecter votre client/utilisateur à Ably. Puisque nous utilisons l'[authentification par jeton](https://www.ably.io/documentation/realtime/channels-messages), nous ajouterons simplement une route vers le serveur d'authentification, comme montré ci-dessous :

**Note** : nous avons spécifié `echoMessage: false`. Cela empêche votre client de s'abonner aux messages publiés par lui-même, garantissant un nombre de messages/utilisation plus faible sur l'ensemble de l'application. Par défaut, cette option est toujours vraie.

Après avoir authentifié avec succès le client, nous stockerons l'identifiant retourné par le serveur d'authentification dans une variable afin de pouvoir l'utiliser plus tard.

Ensuite, configurons la première fonction qui initialise notre application. Dans cette fonction, nous définissons une position initiale de l'avatar. Pour simplifier, nous limiterons la rotation/déplacement de l'avatar à l'axe x uniquement, tout en gardant les coordonnées sur les deux autres plans à zéro. La position initiale sur l'axe x est choisie aléatoirement afin que plusieurs avatars ne s'encombrent pas au même point de la scène dès qu'ils apparaissent. Nous définissons également quelques attributs initiaux tels que la couleur et les dimensions.

Pour envoyer ces données à Ably, nous devons créer un canal. Je l'ai appelé `vr-channel`. Une fois cela fait, nous pouvons publier les attributs initiaux sur ce canal.

Cependant, nous voulons publier en continu ces données afin que tous les autres utilisateurs puissent les recevoir en temps réel. En d'autres termes, nous voulons publier des données lorsque les attributs de position et de rotation changent. Ces données nous sont directement fournies par l'entité caméra dans A-Frame. Nous devons simplement publier ces données sur le même canal à haute fréquence. Dans ce cas, je publie toutes les 100 ms.

`a-box` est une [primitive](https://aframe.io/docs/0.7.0/introduction/html-and-primitives.html#primitives) dans A-Frame qui peut être utilisée pour créer facilement une boîte 3D avec des attributs de base tels que les dimensions, la position, la rotation, la couleur, etc.

Vous pouvez voir qu'il y a trois sous-fonctions dans la fonction ci-dessus que nous n'avons pas encore discutées. [Presence](https://www.ably.io/documentation/realtime/presence) est un terme courant dans le monde du temps réel qui vous donne des informations sur le statut en ligne ou de connexion d'un utilisateur/appareil. Dans notre cas, nous ferions :

* créer et faire apparaître l'avatar dans la scène uniquement lorsqu'un utilisateur se connecte (accède à l'URL)
* et, de même, le faire disparaître dès qu'un utilisateur quitte l'application (ferme la fenêtre du navigateur sur son téléphone ou navigateur).

De plus, Ably vous permet de vous abonner aux événements de présence. Un rappel est déclenché chaque fois qu'un nouvel utilisateur se connecte ou qu'un utilisateur existant se déconnecte. C'est exactement ce dont nous avons besoin pour notre application.

En utilisant `channel.presence.get()`, vous pouvez obtenir une liste de tous les membres actuellement connectés à Ably (sont en ligne).

En utilisant `channel.presence.subscribe('enter')`, vous pouvez être notifié chaque fois qu'un utilisateur se connecte à Ably (passe en ligne).

En utilisant `channel.presence.subscribe('leave')`, vous pouvez être notifié chaque fois qu'un utilisateur se déconnecte d'Ably (passe hors ligne).

Dès qu'un utilisateur se connecte, nous devons abonner tout le monde aux changements d'attributs du nouvel avatar de l'utilisateur. Ces changements, comme vous pouvez l'observer, seront dans l'objet `attr` en raison de la position et de la rotation changeantes. Notre objectif est de mettre à jour l'avatar lorsque ces attributs sont mis à jour.

Avant cela, nous devons nous assurer que l'avatar existe, ou si un nouveau doit être créé. Nous le faisons en utilisant une simple carte des avatars où nous stockons les identifiants de tous les avatars existants, comme montré :

Ensuite, nous devons faire en sorte que tous les utilisateurs s'abonnent aux changements des attributs de tous les autres, à l'exception d'eux-mêmes. Nous le faisons en les faisant s'abonner à l'événement spécifique sur le même canal auquel il est publié, comme ceci :

Lorsqu'un nouvel utilisateur entre, nous devons créer un nouvel avatar avec tous les attributs nécessaires. La fonction suivante obtient tous les attributs initiaux via Ably. Elle crée un nouvel avatar avec ces attributs, et attache d'autres parties comme les yeux, les pupilles et les bras par rapport à la position de la boîte principale (représentant la tête de l'avatar). Ce positionnement manuel devient plus facile avec l'utilisation d'un outil [inspecteur visuel](https://aframe.io/docs/0.7.0/introduction/visual-inspector-and-dev-tools.html) qui vient avec A-Frame.

Après avoir construit toutes les différentes parties d'un avatar, nous les regroupons en les attachant à un avatar racine. Cela nous donne un moyen d'effectuer des actions comme les mises à jour de position et ainsi de suite sur l'avatar dans son ensemble. Vous ne voudriez pas d'une situation de zombie avec la tête bougeant dans une direction et les yeux dans une autre, n'est-ce pas ? ;) Cela facilite également la suppression de l'avatar complet lorsqu'un utilisateur se déconnecte.

Si un avatar existe déjà, nous mettons simplement à jour sa position et sa rotation à partir des données en constante mise à jour dans l'objet `attr` des utilisateurs respectifs.

Remontez jusqu'à la fonction `subscribeToAvatarChanges()`. Vous observerez que `updateAvatar()` est une fonction de rappel pour un abonnement de canal qui est invoquée lorsque les attributs d'un avatar existant changent. Cela nous permet de mettre à jour facilement l'avatar réel également, selon les données changeantes. Nous mettons simplement à jour la position et la rotation avec de nouvelles valeurs, comme montré ci-dessous :

Enfin, nous devons nous assurer que l'avatar est supprimé de la scène chaque fois qu'un utilisateur se déconnecte/passe hors ligne. Cela peut être fait en utilisant à nouveau la présence, en gérant l'événement `leave` mentionné précédemment. Voici quelques choses que vous devez faire lorsqu'un utilisateur se déconnecte :

Nous commençons par supprimer l'entrée correspondante dans notre tableau et suivons cela en supprimant l'avatar complet de la scène.

### C'est tout !

Nous avons maintenant implémenté avec succès une application VR multijoueur qui fonctionne sur le web et en temps réel. Allez-y et testez-la avec vos amis et laissez-les assister à la magie ! Si vous avez travaillé dans un environnement local, vous aurez peut-être besoin d'un serveur local pour héberger vos fichiers, comme mentionné ci-dessus. Personnellement, j'utilise [Glitch](http://glitch.com) pour tous mes projets VR.

Vous connaissez maintenant les bases d'A-Frame et d'Ably, ce qui vous permet de créer des applications VR et des applications en temps réel ou — encore mieux — une application collaborative, comme celle que nous venons de faire.

Des idées germent déjà dans votre esprit ? Allez-y et construisez cette application que vous avez toujours voulue ! Voici le [code source](https://github.com/ably/tutorials/tree/ably-multiplayer-vr-tutorial) complet pour cette application. N'hésitez pas à me contacter sur [Twitter](https://twitter.com/Srushtika) si vous êtes bloqué ou si vous souhaitez en savoir plus sur quelque chose.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HV4HpIxvpQPi6sM5ehvRfw.jpeg)
_[Srushtika Neelakantam](http://twitter.com/Srushtika" rel="noopener" target="_blank" title="">Srushtika Neelakantam</a> est une Dev Advocate pour <a href="http://ably.io" rel="noopener" target="_blank" title="). Crédits photo : Radka Klein_