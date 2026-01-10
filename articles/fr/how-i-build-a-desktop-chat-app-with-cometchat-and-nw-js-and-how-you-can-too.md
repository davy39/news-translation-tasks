---
title: Comment j'ai construit une application de chat de bureau avec CometChat et
  NW.js (et comment vous pouvez le faire aussi)
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-09-22T11:38:05.000Z'
originalURL: https://freecodecamp.org/news/how-i-build-a-desktop-chat-app-with-cometchat-and-nw-js-and-how-you-can-too
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/mihail-chat-app-image.png
tags:
- name: Apps
  slug: apps-tag
- name: Chat
  slug: chat
- name: Node.js
  slug: nodejs
seo_title: Comment j'ai construit une application de chat de bureau avec CometChat
  et NW.js (et comment vous pouvez le faire aussi)
seo_desc: 'This is not your typical "paste this here" and "paste that there"-type
  tutorial (you can find plenty of those here on cometchat.com/tutorials). While those
  tutorials certainly have merit, I am going to share my thought process from beginning
  to end.

  ...'
---

Ce n'est pas votre tutoriel typique du type "*copiez ceci ici*" et "*copiez cela là*" (vous pouvez en trouver beaucoup ici sur [cometchat.com/tutorials](https://www.cometchat.com/tutorials/desktop-chat-app-tutorial/)). Bien que ces tutoriels aient certainement du mérite, je vais partager mon processus de réflexion du début à la fin.

L'application que j'ai construite est assez simple. Lorsque quelqu'un charge l'application, il est invité à entrer son nom d'utilisateur et à commencer à discuter :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-143.png align="left")

*Écran d'accueil*

L'application fonctionne finalement sur Node avec l'aide de NW.js (anciennement connu sous le nom de node-webkit). NW.js est avantageux car il nous permet de coder des applications de bureau multiplateformes en utilisant nos technologies web préférées. Pour cette application, j'ai choisi d'utiliser React et Redux.

La logique back-end - de l'envoi et de la réception de messages en temps réel à la population de ce que j'appelle la "liste des participants" - est alimentée par CometChat. Vous en apprendrez plus sur [CometChat](https://cometchat.com/pro) au fur et à mesure de votre lecture.

Cet article n'est pas destiné à être un guide pas à pas. Bien que je vais expliquer les composants techniques de cette application, mon ambition principale est de vous aider à réfléchir à une solution du début à la fin. Espérons que, lorsque vous aurez terminé cet article, vous serez un développeur légèrement meilleur et envisagerez CometChat pour votre boîte à outils en croissance.

**Vous voulez juste le code exemple ?**

Vous pouvez voir le code source [ici](https://github.com/mihailgaberov/desktop-chat-nw). Il y a aussi un [README](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/README.md) détaillé, où vous trouverez toutes les informations dont vous avez besoin pour installer, exécuter et tester l'application.

Parce que l'application de bureau est construite en utilisant des technologies web, il est tout à fait possible de l'exécuter dans votre navigateur. Vers la fin de cet article, je vous montrerai comment déployer l'application sur Netlify.

## **Planification**

Dans cette section, nous devons décider quels composants nous allons construire. Quelles fonctionnalités auront-ils ? En d'autres termes, quelles sont les questions auxquelles nous devons répondre pour planifier le processus de construction ?

Faisons un pas en arrière et réfléchissons. Essayez de vous poser les questions qui nous mèneront à la structure dont nous avons besoin pour notre application.

*Ci-dessous, je vais exposer mes questions et les réponses. C'est le processus de construction réelle de la structure de l'application, mais d'abord dans votre tête. Gardez à l'esprit qu'il arrive très souvent que, lors de la réponse à une question, de nouvelles questions apparaissent. Ce fut également mon cas.*

**Questions :**

* Que suis-je en train de faire ? ?
  
* Quel type d'application vais-je construire ?
  
* Quels sont les composants les plus courants dont une telle application a besoin ?
  
* Comment les composants de l'application interagissent-ils entre eux ?
  
* Quel niveau d'achèvement vise-je (les applications de démonstration ne sont pas censées être entièrement fonctionnelles) ?
  

**Réponses** (suivant l'ordre des questions) :

* C'est la question la plus négligée que beaucoup de gens oublient de considérer. *Lorsque quelqu'un peut d'abord s'écarter et donner une réponse claire à cette question, son chemin pour les développements futurs devient tracé*. Dans mon cas spécifique, la réponse que j'ai obtenue ressemble à ceci — « Je pense à construire une application de chat. Cette application doit servir d'application de démonstration pour un tutoriel. Elle devra fournir une fonctionnalité de base pour 'avoir une discussion' en utilisant l'API CometChat. Elle doit fonctionner sur un bureau ». Le style et les détails spécifiques sur ce qui va où viendront plus tard dans le processus.
  
* Une application de chat qui fonctionnera sur un bureau et servira de démonstration pour ce tutoriel.
  
* Pour donner une réponse appropriée à cette question, une personne non familière devrait d'abord faire quelques recherches. Jetez un coup d'œil aux applications de chat du monde réel. Prenez note des fonctionnalités qu'elles ont. Comment elles les mettent en place, comment elles interagissent entre elles et avec les utilisateurs de l'application. Dans mon cas, j'avais une certaine [expérience précédente](https://mihail-gaberov.eu/how-i-build-chat-app-with-react-and-typescript-part1/) et j'ai eu, plus ou moins, l'idée de ce dont j'avais besoin.
  
* L'interaction entre les composants serait assez simple. L'utilisateur doit être en mesure d'utiliser le composant principal qui est une zone de texte et un bouton pour envoyer des messages. Et un composant de barre latérale pour voir les autres participants au chat.
  
* L'application de démonstration doit fournir une fonctionnalité de chat de base — envoyer et recevoir des messages en temps réel. Et être en mesure de fonctionner sur un bureau (sans navigateur).

## **Fonctionnalités**

J'ai décidé d'implémenter les fonctionnalités suivantes dans l'application de démonstration :

* Envoyer avec la touche Entrée
  
* Une barre latérale avec les noms et la dernière heure d'activité
  
* Écran d'accueil avec saisie et validation avec messages d'erreur
  
* Zone de chat avec défilement automatique vers le bas
  
* Message de chat et heure d'envoi.

## **Front End — React**

Nous allons utiliser [React](https://reactjs.org/) pour construire notre interface utilisateur. Ci-dessous, je vais lister les composants que j'ai créés et une brève explication pour chacun d'eux :

* [ChatPane](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/components/ChatPane) — c'est le composant principal de type conteneur qui contient les composants Participants et Conversation et transmet les données dont ils ont besoin pour la visualisation.
  
* [Conversation](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/components/Conversation/Conversation.jsx) — c'est le composant responsable de la saisie et de l'envoi des messages de chat.
  
* [Footer](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/components/Footer/Footer.jsx) — affiche un message de pied de page simple, contenant le nom et la version de l'application, tels que définis dans le fichier package.json.
  
* [Header](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/components/Header/Header.jsx) — composant d'en-tête contenant la barre de menu de l'application.
  
* [MenuAppBar](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/components/MenuAppBar/MenuAppBar.jsx) — composant de barre de menu de l'application, simulant l'apparence d'une vraie barre de menu. Le menu hamburger à gauche et le menu déroulant de profil à droite sont factices — cliquables, mais non fonctionnels.
  
* [Messages](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/components/Messages/Messages.jsx) — un composant conteneur, contenant un message lui-même — il a le nom de l'expéditeur, le contenu du message et l'heure d'envoi.
  
* [Participants](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/components/Participants) — ce composant affiche le nom d'un membre du chat et l'heure à laquelle il a rejoint.
  
* [Welcome](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/components/Welcome) — ce composant est responsable de l'affichage de la page de connexion — le point de départ de notre application, où nous avons une logique liée à la vérification de certains noms d'utilisateur autorisés et à leur stockage dans le stockage local pour une utilisation ultérieure. J'ai également implémenté une logique de gestion des erreurs de base, qui affiche une erreur lorsque le nom d'utilisateur sélectionné n'est pas correct, selon l'API CometChat (dans ce cas spécifique pour notre démonstration) les noms d'utilisateur enregistrés — superhero1, superhero2 et ainsi de suite jusqu'à 5.

Voici une représentation visuelle des composants de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-144.png align="left")

*Composants visuels*

## **Gestion d'état — Redux**

Chaque application moderne de nos jours a un état. Un espace en mémoire où l'application stocke certaines données pour une utilisation ultérieure. Pour la gestion de l'état de notre application, nous utilisons [Redux](https://redux.js.org/). Bien sûr, pour une application simple comme celle-ci, nous pourrions nous passer de Redux. Mais, du point de vue de l'apprentissage (*après tout, nous faisons tous cela pour apprendre de nouvelles choses, n'est-ce pas ?*), je pense qu'il serait bien de voir tout le cycle d'envoi d'une requête à une API, en passant par un middleware (redux-thunks) et en obtenant la réponse enregistrée dans l'état. Et nous allons gérer cet état en utilisant Redux.

### **Comment cela fonctionne**

Les principaux blocs de construction dans une application Redux sont appelés réducteurs — de petites fonctions utilisées pour gérer l'état. Simplement dit, ce qu'ils font est d'accepter l'ancien objet d'état en entrée et, en fonction de certaines actions (qui sont également passées dans la même entrée), de retourner un nouvel objet d'état. Le nouvel état peut être modifié en totalité ou seulement partiellement.

Dans notre application, nous avons trois réducteurs simples, qui sont responsables de ces parties de l'état, responsables de la liste des utilisateurs, du processus de connexion et de l'envoi/réception de messages. Tous peuvent être vus dans le dossier [/src/reducers](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/reducers), ainsi qu'un [fichier](https://github.com/mihailgaberov/desktop-chat-nw/blob/master/src/reducers/initialState.js) contenant l'état initial de notre application.

Redux, en tant que bibliothèque de gestion d'état, peut être utilisé avec tout autre framework UI, pratiquement chaque application qui a besoin d'avoir un état peut bénéficier de l'utilisation de Redux. Si vous voulez approfondir, commencez par leur site web et suivez-le.

## **Gestion des effets secondaires — Redux Thunks**

L'une des approches les plus connues pour gérer les effets secondaires dans une application redux s'appelle [redux-think](https://github.com/reduxjs/redux-thunk). C'est ce que nous utilisons également dans notre application. Si vous souhaitez en savoir plus sur les redux thunks et comment les utiliser, je recommande leur site web comme point de départ, puis construisez une petite application, comme celle-ci par exemple :).

Dans notre projet, dans le [dossier /src/actions](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/actions), c'est là que j'ai mis les thunks utilisés dans l'application de démonstration. Et dans le [répertoire /store](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/store) se trouvent les configurations pour le store redux.

## **Rendre cela de bureau — NW.js**

La partie de notre application qui permet à notre application de fonctionner sur un bureau est prise en charge par une bibliothèque appelée [NW.js](https://nwjs.io/). Rappelez-vous que nous construisons une application de bureau. C'est précisément la partie bureau qui sera implémentée via NW.js. Similaire à [Electron](https://electronjs.org/), une autre bibliothèque pour construire des applications de bureau, NW.js fournit un moyen aux développeurs d'utiliser leurs compétences web pour construire des applications qui peuvent fonctionner sur un bureau. Cela signifie que vous pouvez toujours utiliser vos compétences JavaScript/React lors de la construction d'une application, puis tirer parti de la puissance du système d'exploitation de bureau via les API de Nw.js. En d'autres termes, Nw.js vous donne la capacité de créer une application squelette, qui peut être "remplie" avec votre UI, peu importe quelle bibliothèque vous avez utilisée pour la créer. Et le meilleur, c'est qu'une telle application a accès aux API Node.js/NW.js et au DOM dans le même contexte JavaScript.

Puisque nous avons mentionné l'autre grand acteur dans le domaine de la construction d'applications de bureau multiplateformes, permettez-moi de vous donner une brève comparaison entre les deux.

## **Nw.js vs Electron**

Point d'entrée de l'application

* Dans NW.js, le point d'entrée principal d'une application est une page web ou un script JS. Vous spécifiez un fichier HTML ou js dans le package.json et il est ouvert dans une fenêtre de navigateur en tant que fenêtre principale de l'application (dans le cas d'un point d'entrée HTML) ou le script est exécuté.
  
* Dans Electron, le point d'entrée est un script JavaScript.

Système de construction

* Nw.js utilise Chromium
  
* Electron utilise [libchromiumcontent](https://github.com/electron/libchromiumcontent) pour accéder à l'API de contenu de Chromium. libchromiumcontent est une bibliothèque partagée unique qui inclut le module de contenu Chromium et toutes ses dépendances.

Intégration de Node

* Dans NW.js, l'intégration de Node dans les pages web nécessite de patcher Chromium pour fonctionner.
  
* Dans Electron, une méthode différente est utilisée pour intégrer la boucle libuv avec la boucle de messages de chaque plateforme afin d'éviter de pirater Chromium.

Multi-contexte

* En raison de la manière dont NW.js a été implémenté, les concepts de contexte Node et de contexte web ont été inventés.
  
* En utilisant la fonctionnalité [multi-contexte](https://github.com/nodejs/node-v0.x-archive/commit/756b622) de Node, Electron n'introduit pas un nouveau contexte JavaScript dans les pages web.

## **Chat — CometChat**

L'utilisation de l'API CometChat est assez simple. C'est une API RESTFull, sur laquelle est construite une autre couche d'abstraction — le SDK CometChat. Il nous permet d'appeler directement des méthodes exposées pour différentes actions que nous pourrions vouloir effectuer, comme envoyer. Voici un exemple d'une telle méthode :

```js
return CometChat.sendMessage(textMessage).then(    
  message => {      
    console.log("Message sent successfully:", message);      
    return message;
  }, 
  error => {      
    console.log("Message sending failed with error:", error);    
  }
);
```

Vous pouvez voir toute la logique de l'API Chat dans le [dossier /src/chat-api](https://github.com/mihailgaberov/desktop-chat-nw/tree/master/src/chat-api). Vous y verrez également les mocks que j'ai créés, qui nous permettent de tester notre application sans connexion réelle à l'API.

## **Améliorations**

Chaque projet mérite quelques réflexions après avoir terminé la première phase. Une partie de ce processus de réflexion serait dédiée à la manière dont cela s'est passé, ce qui était bien et mal, et ce qui pourrait être fait mieux. Et une partie serait dédiée à la réflexion sur les améliorations possibles. Voici quelques idées pour notre cas. Si quelqu'un va dans cette direction et implémente l'une de ces idées pour de vrai, n'oubliez pas de me le faire savoir :)

* Animation d'attente lors du chargement de l'historique du chat et de la liste des utilisateurs
  
* Option pour sauter l'écran de connexion, si déjà connecté
  
* Option pour envoyer des invitations à de nouveaux utilisateurs
  
* Option pour voir le statut d'un message — envoyé, reçu, lu
  
* Support des emojis
  
* Support des liens/images/vidéos en ligne, de sorte que l'utilisateur puisse les voir interprétés — lecture de vidéo, image rendue ou page web vers laquelle un lien pointe. J'ai ajouté ces éléments en tant que [problèmes dans mon GitHub](https://github.com/mihailgaberov/desktop-chat-nw/issues), au cas où quelqu'un voudrait y jeter un coup d'œil.

## **Déploiement sur Netlify**

Pour déployer votre application sur la plateforme Netlify, vous devez d'abord créer un compte. Allez sur [leur site web](https://www.netlify.com/) et inscrivez-vous pour un nouveau compte. Après cela, connectez-vous. Tout en étant sous la section Sites, vous devriez voir un bouton pour déployer un nouveau site à partir de Git.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-145.png align="left")

Cliquez dessus et suivez les étapes pour créer un nouveau site de déploiement à partir de vos dépôts GitHub. Votre processus devrait être similaire à ce qui est montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-146.png align="left")

Maintenant, la dernière étape avant d'avoir votre application déployée est de vous assurer que vous avez les bonnes commandes de construction et les variables d'environnement en place. Pour ce faire, après avoir créé votre site pour le déploiement, allez à l'écran des paramètres **Build & deploy** et entrez ce qui suit (n'oubliez pas d'utiliser l'URL de votre dépôt) :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-147.png align="left")

Dans la section **Environment**, c'est là que vous devez entrer les variables d'environnement telles que définies dans votre fichier .env. Voici à quoi ressemble le mien :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-148.png align="left")

Note : *J'ai effacé les valeurs car il s'agit d'informations privées et vous ne devriez pas partager les vôtres non plus.*

Cela devrait suffire pour que votre application soit déployée sur Netlify. Gardez à l'esprit que les paramètres par défaut des **Deploys** sont réglés sur 'auto publishing', ce qui signifie qu'il déclenchera un déploiement à chaque commit que vous faites sur la **branche master** de votre dépôt. C'est l'endroit où vous pouvez également déclencher un déploiement manuellement. Voici à quoi ressemble mon écran **Deploys** :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-149.png align="left")

## Conclusion

Dans ce tutoriel, nous avons vu comment nous pouvons utiliser nos compétences en développement web pour créer des applications qui peuvent fonctionner sur un bureau. Ce que nous avons construit est une application de démonstration, qui manque de nombreuses fonctionnalités d'une application prête pour la production, mais lorsque quelqu'un veut apprendre et partager, cela fera l'affaire. Si vous souhaitez approfondir vos connaissances dans cette direction, je vous recommande d'essayer de l'améliorer en implémentant des fonctionnalités plus susceptibles d'être vues dans une véritable application de bureau.

Il y a de nombreuses opportunités à explorer, j'espère que ce tutoriel vous a diverti suffisamment pour garder votre flamme de curiosité brûlant encore plus.

? Merci d'avoir lu ! ?

**Notes :**

* Pour utiliser les outils de développement Nw.js, vous devez installer la version SDK — [https://nwjs.io/downloads/](https://nwjs.io/downloads/) — version 0.38.2 ou supérieure.

**Ressources :**

* [Q : Qu'est-ce qu'un 'thunk' ? R : Le son que fait votre tête lorsque vous entendez parler de redux-thunk pour la première fois. Désolé, c'était horrible. Mais… daveceddia.com](https://daveceddia.com/what-is-a-thunk/)
  
* \[livre\] Applications de bureau multiplateformes : Utilisation de Node, Electron et NW.js
  
* \[livre\] Développement d'applications de bureau multiplateformes : Electron, Node, NW.js et React
  
* [Middleware Thunk pour Redux](https://github.com/reduxjs/redux-thunk)
  
* [https://reactjs.org/docs/hooks-reference.html#useref](https://reactjs.org/docs/hooks-reference.html#useref)