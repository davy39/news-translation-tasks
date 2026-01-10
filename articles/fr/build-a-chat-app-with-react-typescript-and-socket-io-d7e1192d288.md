---
title: Créer une application de chat avec React, TypeScript et Socket.io
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-04-26T15:19:34.000Z'
originalURL: https://freecodecamp.org/news/build-a-chat-app-with-react-typescript-and-socket-io-d7e1192d288
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XB8rYOUoHDLtQHz470IDQw.jpeg
tags:
- name: Chat
  slug: chat
- name: React
  slug: react
- name: software development
  slug: software-development
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Créer une application de chat avec React, TypeScript et Socket.io
seo_desc: 'This is going to be a thorough step-by-step guide for building a single
  page chat application using React, TypeScript and Socket.io.

  If you want to skip the reading, here ? is the GitHub repository with a detailed
  README, and here you can check the l...'
---

Ce guide détaillé étape par étape vous expliquera comment créer une application de chat monopage en utilisant React, TypeScript et Socket.io.

Si vous souhaitez passer directement à la pratique, voici le [dépôt GitHub](https://github.com/mihailgaberov/chat) ? avec un [README](https://github.com/mihailgaberov/chat/blob/master/README.md) détaillé, et [ici](https://mihails-chat.herokuapp.com/#/chat) vous pouvez consulter la démonstration en direct. Pour l'utiliser, vous devez l'ouvrir dans deux navigateurs différents (ou onglets) ou appareils (vous pouvez utiliser votre ordinateur et votre smartphone) et discuter entre eux.

### Recherche

Lorsque vous êtes sur le point de commencer un nouveau projet, il est bon de faire une recherche initiale sur la pile technologique que vous prévoyez d'utiliser.

En d'autres termes, vous pouvez vouloir ou avoir besoin — surtout si vous n'avez pas d'expérience préalable — d'enquêter sur chaque technologie que vous allez utiliser. Je recommande de le faire séparément. Prenez l'une d'entre elles et créez une petite application avec laquelle vous pouvez jouer.

Si vous devez vérifier comment l'intégration de deux technologies ou plus va fonctionner dans un projet réel — alors vous pouvez vouloir les inclure toutes ensemble dans votre application de "recherche-test-jeu" — mais de préférence, faites vos recherches une à la fois.

#### Aller droit au but

Lorsque j'ai commencé à penser à créer cette [application de chat](http://mihails-chat.herokuapp.com/#/chat), j'ai fait exactement ce que j'ai décrit ci-dessus. Je n'avais pas d'expérience récente avec [TypeScript](http://www.typescriptlang.org/) et aucune avec [Socket.io](https://socket.io/), donc j'ai dû jeter un coup d'œil à celles-ci et me familiariser avec leur état actuel. Comme mon plan était d'utiliser [React](https://reactjs.org/) comme bibliothèque principale d'interface utilisateur, je devais voir comment cela allait fonctionner avec les autres technologies de l'équation. Donc je l'ai fait.

J'ai créé deux petites applications (dépôts [ici](https://github.com/mihailgaberov/playing-with-socketio) et [ici](https://github.com/mihailgaberov/react-contextapi-with-typescript)) avec ces technologies, juste pour pouvoir jouer avec elles et apprendre comment je pourrais les utiliser dans ma future application de chat.

Après avoir terminé ma recherche initiale, j'ai pu commencer à penser et à planifier la mise en œuvre de mon application de chat principale.

![Image](https://cdn-media-1.freecodecamp.org/images/TjBOPkJjQ11wSe3gxxczgRYplWFpQnx5vmfd align="left")

\_Photo par \[Unsplash\](https://unsplash.com/photos/3TRdlKU-3II?utm\_source=unsplash&utm\_medium=referral&utm\_content=creditCopyText" rel="noopener" target="\_blank" title=""&gt;Hutomo Abrianto sur &lt;a href="https://unsplash.com/search/photos/research-done?utm\_source=unsplash&utm\_medium=referral&utm\_content=creditCopyText" rel="noopener" target="*blank" title=")*

### Planification de haut niveau

Habituellement, lorsque les gens parlent de "plan de haut niveau", ils cherchent à avoir une vue d'ensemble. Cela signifie que nous devons créer un plan approximatif de notre exécution et définir nos piliers principaux, mais sans entrer dans trop de détails. Maintenant que nous avons une idée claire de ce que nous devons faire, commençons à le faire ! ?

**Note :** À partir de ce point, je vais supposer que vous suivez mes étapes comme je les décris, c'est pourquoi je vais écrire à la deuxième personne. ?

#### Pile technologique

Nous avons déjà mentionné les principales technologies que nous allons utiliser, mais définissons une liste complète de toutes celles-ci ici :

* [React avec TypeScript](https://github.com/Microsoft/TypeScript-React-Starter#create-our-new-project) (`create-react-app my-app --scripts-version=react-scripts-ts`) — une bibliothèque d'interface utilisateur que nous utiliserons pour construire les interfaces utilisateur de notre application.

* [Redux](https://redux.js.org/) — une bibliothèque de gestion d'état que nous utiliserons pour gérer l'état de notre application.

* [Express.js](https://expressjs.com/) — un framework d'application web Node.js que nous utiliserons pour créer un [serveur http](https://expressjs.com/en/starter/hello-world.html) dont nous aurons besoin dans notre application, afin de tirer parti du moteur Socket.io.

* [Socket.io](https://socket.io/) — une bibliothèque JavaScript pour les applications web en temps réel. Elle permet une communication en temps réel et bidirectionnelle entre les clients web et les serveurs. Nous l'utiliserons pour implémenter un comportement de chat simple dans notre application.

* [styled-components](https://www.styled-components.com/docs) — une petite bibliothèque que nous utiliserons pour ajouter des styles à notre application et rendre l'apparence et la convivialité belles. Elle utilise des littéraux de modèle étiquetés pour styliser vos composants et supprime le mappage entre les composants et les styles. Cela signifie que lorsque vous définissez vos styles, vous créez en fait un composant React normal qui a vos styles attachés.

* [Jest](https://jestjs.io/)/[Enzyme](https://airbnb.io/enzyme/) — un framework de test JavaScript et un utilitaire de test JavaScript que nous utiliserons pour écrire des tests unitaires pour notre application. Les deux ont une grande intégration dans l'écosystème React et sont largement utilisés dans des projets réels.

#### Fonctionnalités de l'application

Dans cette section, nous allons décrire les fonctionnalités de notre application.

Chaque fois que nous planifions un nouveau projet, nous devons définir certains critères qui décriront un niveau d'achèvement lorsqu'ils seront atteints.

En d'autres termes, nous devons fixer un point limite qui, une fois atteint, montrera que notre projet est terminé ou au moins dans sa première version. Il existe un dicton célèbre qui pourrait correspondre au problème des projets "sans fin" :

> "Un bon plan aujourd'hui est meilleur qu'un plan parfait demain." — ou nous pourrions dire qu'un projet fonctionnel aujourd'hui est meilleur qu'un projet parfait demain.

Voici ma liste des fonctionnalités que je voulais implémenter initialement :

#### **En-tête**

* Onglet Chat — clignotant lorsqu'un nouveau message est reçu jusqu'à ce qu'il soit lu, ou lorsque l'utilisateur est sur la page des paramètres

* Onglet Paramètres

* Compteur de messages non lus

* Icônes Font Awesome

#### **Page de chat**

* Zone de chat (comprend les messages alignés à gauche et à droite)

* Message (texte, date et heure, gauche ou droite selon qu'il est reçu ou envoyé)

* Affichage du pseudonyme uniquement de l'expéditeur

* Expéditeur de messages — champ de saisie et bouton. Le champ de saisie est effacé et mis au point lorsque le bouton est cliqué

* Envoyer des messages avec CTRL+ENTRÉE

* Défilement automatique vers le bas lorsque la zone de chat n'est pas suffisante pour afficher tous les messages

#### **Page des paramètres**

* Composant UserProfile — possibilité de changer le nom d'utilisateur

* Composant de couleur de l'interface — changer le thème de couleur de l'application

* Composant ClockDisplay — changer le mode horaire 12h ou 24h, affiché avec chaque message

* Envoyer des messages avec Ctrl+Enter — On/Off

* LanguageSwitcher — menu déroulant permettant de changer la langue de l'application (actuellement, l'anglais et l'allemand sont pris en charge)

* Bouton de réinitialisation — réinitialise tous les paramètres stockés dans le stockage local

**Améliorations**

Au moment de la rédaction de ce document, il reste encore quelques fonctionnalités en attente que je souhaite implémenter. Voici la liste de toutes les améliorations que j'ai apportées ou que je prévois de faire à l'avenir (celles avec l'emoji de pouce sont déjà implémentées) :

* Ajouter une fonctionnalité de chat vidéo.

* ? Ajout du formatage de l'heure AM/PM lorsque le mode 12h est sélectionné.

* ? Ajout de la possibilité d'envoyer un message via ENTER par défaut. Si le paramètre pour envoyer des messages avec CTRL+ENTER est activé, alors ce sera le seul moyen (sauf via la souris/tactile bien sûr).

* ? Optimisé pour les appareils iDevices (requêtes médias).

* ? Correction du problème de clignotement/classe active pour l'onglet Chat — lié à React Router qui ne peut pas réafficher correctement les composants connectés [https://github.com/ReactTraining/react-router/blob/master/packages/react-router/docs/guides/blocked-updates.md](https://github.com/ReactTraining/react-router/blob/master/packages/react-router/docs/guides/blocked-updates.md)

* ? Effacer le champ de saisie lorsqu'un nouveau message est envoyé.

* ? Défilement automatique vers le bas de la zone de chat principale lorsque les nouveaux messages dépassent l'espace disponible.

* ? Empêcher le "doublement des messages" (ou les doublons de messages multiples lorsque plusieurs clients sont connectés).

* ? Ajouter des tests unitaires pour les composants React.

* Ajouter des tests unitaires pour les éléments Redux — réducteurs, magasin, créateurs d'actions.

* ? Ajouter des requêtes médias pour la réactivité — tester et ajuster sur plus d'appareils.

* ? Ajouter une démonstration sur Heroku.

* ? Ajouter un guide pratique dans le README.

* Ajouter des animations pour les messages.

* Ajouter des sons (avec des options pour activer/désactiver dans les paramètres).

* Ajouter plus de thèmes de couleurs.

* Ajouter un message de bienvenue (diffusé lorsqu'un nouvel utilisateur est connecté).

* ? Ajouter des icônes (utiliser Font Awesome).

* Historique de toutes les conversations.

* Gérer le cas où l'état de connexion de la socket change (visuellement).

* Gérer le cas où une erreur de socket s'est produite.

* Gérer le cas où un mot très long (sans espaces) est saisi et dépasse la couleur de fond du message.

* ? Prise en charge des émoticônes — tels que :D, :P, :), ;), ?, ❤️, etc.

* ? Analyseur de liens — lien Youtube (la vidéo intégrée doit apparaître), lien vers une image (l'image intégrée doit apparaître), tous les autres liens doivent apparaître sous forme d'ancre.

Lorsque nous connaissons le plan initial et les exigences que nous devons remplir, nous pouvons effectuer nos analyses de haut niveau. Notre application aura deux pages, Chat et Paramètres, accessibles via des contrôles d'onglets.

La page Chat contiendra la zone de chat principale avec les contrôles nécessaires pour envoyer des messages (champ de saisie et un bouton).

La page Paramètres contiendra quelques contrôles pour sélectionner les options décrites ci-dessus.

Avec cela en tête, nous pouvons passer à la section suivante où nous créerons un plan plus détaillé avant la mise en œuvre réelle.

### Planification plus détaillée

Dans cette section, nous devons examiner plus en profondeur notre application et définir quels seront les blocs de construction. Puisque nous allons utiliser React et que nous savons que dans le monde React le terme *composant* est largement utilisé, nous pouvons nous référer à nos blocs de construction comme des composants. Nous aurons des composants responsables des éléments purement visuels, ainsi que des composants pour gérer le stockage local, par exemple.

Essayons d'imaginer mentalement à quoi ressemblera notre application à la fin et quels composants elle nécessitera. Ce que nous savons déjà, c'est ceci :

#### **Partie serveur**

Nous aurons besoin d'un serveur HTTP qui prendra en charge le démarrage du serveur et la gestion des interactions avec Socket.io (envoi et réception de messages). Notre logique serveur sera suffisamment simple pour tenir dans un seul fichier. Vous pouvez voir la mise en œuvre réelle [ici](https://github.com/mihailgaberov/chat/blob/master/server/index.js).

**Partie client**

Ici, nous devons avoir tous les contrôles visuels, ainsi que des moyens de gérer les interactions avec le stockage local, où nous sauvegarderons les préférences de l'utilisateur, ainsi que la gestion des traductions et des thèmes de couleurs.

C'est le bon moment pour souligner que pour implémenter la fonctionnalité de [traductions et de thèmes](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) dans l'application, j'ai utilisé l'[API de contexte React](https://reactjs.org/docs/context.html). De plus, comme je savais que je devrais gérer le [stockage local](https://developer.mozilla.org/fr/docs/Web/API/Window/localStorage), j'ai fait [un autre tour](https://github.com/mihailgaberov/misc/tree/master/manage-local-storage-with-typescript) du voyage "recherche-test-jeu". Et le résultat a été que j'avais déjà un [beau service](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts), qui fournit toutes les fonctionnalités dont j'avais besoin.

Une autre chose que vous remarquerez en regardant le dossier [composants](https://github.com/mihailgaberov/chat/tree/master/src/components) est que chaque composant a son propre répertoire avec quelques fichiers.

Ces fichiers servent la logique suivante :

**index.ts** → point d'entrée, expose simplement le composant lui-même. Cela aide à ne pas avoir à écrire des instructions d'importation répétitives et longues. Voici un exemple :

```js
// Au lieu d'avoir à écrire ceci :
import ChatArea from '../../ChatArea/ChatArea';

// Nous pouvons avoir juste ceci :
import ChatArea from '../../ChatArea';
```

[.tsx (ChatAr](https://github.com/mihailgaberov/chat/blob/master/src/components/ChatArea/ChatArea.tsx)ea.tsx) → l'implémentation réelle du composant se trouve ici.

**.tes**t.tsx (ChatArea.tes**t.t**sx) → les tests unitaires du composant se trouvent ici.

;.tsx (StyledChatArea.tsx) → les styles CSS du composant se trouvent ici.

Le même modèle est utilisé pour la plupart des composants, à l'exception des *pages*, comme les composants qui jouent le rôle de parents pour toutes les parties internes — [ChatPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Chat) et [SettingsPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Settings).

Ainsi, avec cela dit, je pense que nous pouvons voir à quoi ressemblera la structure de notre application lorsque nous essayerons de la "composantiser". Voici une liste des [composants](https://github.com/mihailgaberov/chat/tree/master/src/components) que j'ai conçus :

![Image](https://cdn-media-1.freecodecamp.org/images/-3vmQYe218gWyJK3nI-6GAtmr1wE2maNBlZ4 align="left")

*Composants de l'application de chat*

**Note :** tous les noms sont une question de choix personnel, n'hésitez pas à nommer les vôtres comme vous le souhaitez.

Permettez-moi d'essayer de vous donner une explication un peu plus détaillée pour chacun d'eux ci-dessous :

* [AppRouter](https://github.com/mihailgaberov/chat/tree/master/src/components/AppRouter) — contient la logique de routage principale de l'application. Par exemple, ici nous définissons les routes de l'application en leur donnant le chemin et le composant à charger lorsque ce chemin est atteint. Utilise le package [React Router](https://reacttraining.com/react-router/web/guides/philosophy).

* [ChatArea](https://github.com/mihailgaberov/chat/tree/master/src/components/ChatArea) — représente la zone de chat principale, où tous les messages sont affichés. Il est également responsable du défilement automatique vers le bas lorsque la limite de la zone visible est atteinte.

![Image](https://cdn-media-1.freecodecamp.org/images/gKA17zU8GG2NN-XihkaCM-kGV1sYxTvwXZeW align="left")

*Composant ChatArea*

* [ClockModeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ClockModeSelector) — responsable de l'affichage des contrôles permettant à l'utilisateur de sélectionner le mode d'affichage de l'heure - 12h ou 24h. Il utilise un composant commun appelé [RadioGroup](https://github.com/mihailgaberov/chat/tree/master/src/components/common/RadioGroup) (je le décrirai ci-dessous) et le service de stockage local pour écrire/lire dans le stockage local du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/2uI0pWruJubJhqy4Ab9IWDgrQc6A5QHaCdR8 align="left")

*Composant ClockModeSelector*

* [common/RadioGroup](https://github.com/mihailgaberov/chat/tree/master/src/components/common/RadioGroup) — il s'agit d'un composant commun, construit avec l'idée d'être réutilisable dans toute l'application. Nous utilisons ce composant dans quelques autres composants, tels que ClockModeSelector, [ThemeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ThemeSelector) et [SendingOptions](https://github.com/mihailgaberov/chat/tree/master/src/components/SendingOptions). Il contient la logique pour afficher deux boutons radio avec la possibilité de passer une fonction de rappel qui exécutera une certaine action en fonction de vos besoins.

* [LanguageSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/LanguageSelector) — responsable de l'affichage d'un contrôle de saisie de sélection pour choisir la langue de l'application. Il accepte une fonction qui provient de l'utilitaire [TranslationsProvider](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) et effectue le changement de langue réel.

![Image](https://cdn-media-1.freecodecamp.org/images/ld97BlC9uTxhIOrlzH1a2EKk0xRe-UsrQyI0 align="left")

*Composant LanguageSelector*

* [Message](https://github.com/mihailgaberov/chat/tree/master/src/components/Message) — ce composant est responsable de l'affichage de chaque message de chat, envoyé ou reçu. Il inclut le pseudonyme de l'expéditeur et un horodatage indiquant l'heure à laquelle le message a été envoyé/reçu. Il fournit également une prise en charge des émoticônes (comme ❤️) et l'analyse des liens — voir la capture d'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/MHyO9Z78p-SnKs63kXnPVXnDPBT3F2nZRO0p align="left")

*Composant Message*

* [MessageSender](https://github.com/mihailgaberov/chat/tree/master/src/components/MessageSender) — il s'agit du composant qui fournit les contrôles d'interface utilisateur nécessaires pour envoyer des messages — un champ de saisie de texte et un bouton Envoyer. Il contient la logique pour définir les différentes manières d'envoyer — via un clic ou une pression de touche (avec ENTER ou CTRL+ENTER), ainsi que pour effacer le champ de saisie lorsqu'un nouveau message est envoyé.

![Image](https://cdn-media-1.freecodecamp.org/images/Gii8QNN4XmdJe-7kzP8wZ0UYUnLiQJHHMaam align="left")

*Composant MessageSender*

* [Navigation](https://github.com/mihailgaberov/chat/tree/master/src/components/Navigation) — ici se trouve la mise en œuvre de la navigation de l'application. Elle se compose de deux onglets — **Chat** et **Paramètres** et contient la logique pour se connecter aux sockets, en envoyant une [action Redux](https://redux.js.org/basics/actions) lorsque le composant est monté. Il gère un composant [UnreadMessagesCounter](https://github.com/mihailgaberov/chat/tree/master/src/components/UnreadMessagesCounter) en lui passant le nombre de messages non lus actuellement (cela se produit lorsque l'utilisateur reçoit un message tout en étant sur la page des paramètres). Il possède également une logique responsable du clignotement de l'onglet lorsqu'un nouveau message arrive.

![Image](https://cdn-media-1.freecodecamp.org/images/M4PlpJ2Fpb02u-eQ19BZZXlvR97aWnqUNJhR align="left")

*Composant Navigation*

* [Nickname](https://github.com/mihailgaberov/chat/blob/master/src/components/Nickname/) — il s'agit d'un composant simple pour rendre le pseudonyme d'un utilisateur de chat.

![Image](https://cdn-media-1.freecodecamp.org/images/ZxjFRTriSECNzbOYLbtPsEOdiL47bC4nnk-d align="left")

*Composant Nickname*

* [ResetButton](https://github.com/mihailgaberov/chat/tree/master/src/components/ResetButton) — il s'agira d'un composant simple, utilisé dans la page **Paramètres** pour rendre un bouton de réinitialisation. La fonction sera exactement celle-ci — réinitialiser les sélections de paramètres déjà enregistrées dans le stockage local, le cas échéant.

![Image](https://cdn-media-1.freecodecamp.org/images/T-UIwyCJl3aB89L45JsLOPJ8Ti93Iuwsolcs align="left")

*Composant ResetButton*

* [SendingOptions](https://github.com/mihailgaberov/chat/tree/master/src/components/SendingOptions) — responsable de l'affichage des options pour choisir si un message peut être envoyé via CTRL+ENTER. Il fonctionne de la même manière que le composant ClockModeSelector — utilise le composant RadioGroup et accepte une fonction de rappel.

![Image](https://cdn-media-1.freecodecamp.org/images/tJ98-2kK4eeHuRRK0KhL-GRZYhxz042eJa1G align="left")

*Composant SendingOptions*

* [ThemeSelector](https://github.com/mihailgaberov/chat/tree/master/src/components/ThemeSelector) — même chose que le composant ci-dessus. La seule différence est que l'utilisateur peut ici sélectionner un thème de couleur. Dans notre cas, les options sont au nombre de deux — thème clair ou thème sombre.

![Image](https://cdn-media-1.freecodecamp.org/images/PkC-P1qnRl73Ylz9KivVevkCRvg5mTXuZpMj align="left")

*Composant ThemeSelector*

* [Timestamp](https://github.com/mihailgaberov/chat/tree/master/src/components/Timestamp) — composant simple utilisé pour rendre l'heure des messages.

![Image](https://cdn-media-1.freecodecamp.org/images/R0WmjOMrEEMQCgWGZ6DF7w4qnvc-pT3ioQCp align="left")

*Composant Timestamp*

* [UnreadMessagesCounter](https://github.com/mihailgaberov/chat/tree/master/src/components/UnreadMessagesCounter) — il s'agit du composant dont j'ai parlé un peu plus tôt. Il affiche un compteur indiquant le nombre de messages reçus mais pas encore lus. Il est positionné dans la zone de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/t2Q-AcyK0v-7qhgtwYu2hetYzNw76SAwVv01 align="left")

*Composant UnreadMessagesCounter*

* [UserProfile](https://github.com/mihailgaberov/chat/tree/master/src/components/UserProfile) — il s'agit du composant responsable de l'affichage d'un champ de saisie que l'utilisateur peut utiliser pour changer son nom d'utilisateur. Il sauvegarde le nouveau nom d'utilisateur dans le stockage local, en utilisant une fonction [debounce](https://lodash.com/docs/4.17.11#debounce). Cela signifie que le déclenchement réel de la fonction se produit un certain temps après que l'utilisateur a cessé de taper. Il déclenche également une autre action Redux, afin que nous puissions utiliser le nouveau nom d'utilisateur dans notre état Redux.

* [pages/ChatPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Chat) — composant parent qui englobe tout ce qui est affiché sur la page de chat.

* [pages/SettingsPage](https://github.com/mihailgaberov/chat/tree/master/src/components/pages/Settings) — composant parent qui englobe tout ce qui est affiché sur la page des paramètres.

Tout ce qui est décrit ci-dessus était lié à nos composants React. Tous sont responsables de l'obtention de certaines données et de leur affichage de manière appropriée. Afin de pouvoir gérer ces données de manière pratique pour nous, nous utilisons quelques autres éléments. Jetons un coup d'œil à ces éléments dans les sections ci-dessous.

### Gestion de l'état Redux

Ici, nous allons parler de la manière dont l'état de notre application est géré en utilisant Redux et le middleware socket.

#### Magasin

Notre [magasin](https://github.com/mihailgaberov/chat/blob/master/src/store/index.ts) sera relativement simple. Nous n'aurons que deux réducteurs définissant une partie de l'état réservé à l'état du socket et à l'état des messages. C'est également là que nous appliquons notre middleware. Si vous êtes familier avec le package [Redux Saga](https://redux-saga.js.org/), vous avez probablement vu ce modèle d'application de middleware personnalisé lors de l'utilisation de Redux.

Quelque chose comme ceci :

```js
import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'
import reducer from './reducers'
import mySaga from './sagas'
// créer le middleware saga
const sagaMiddleware = createSagaMiddleware()
// le monter sur le magasin
const store = createStore(
  reducer,
  applyMiddleware(sagaMiddleware)
)
```

Mais dans notre cas, ce serait comme ceci :

```python
import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import socketReducer from './socket/reducer';
import messageReducer from './message/reducer';
import socketMiddleware from './socket/middleware';
const rootReducer = combineReducers({
  socketState: socketReducer,
  messageState: messageReducer
});
// @ts-ignore
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const index = {
  ...createStore(rootReducer, composeEnhancers(applyMiddleware(socketMiddleware)))
};
export default index;
```

#### Message

Après avoir défini notre magasin, il est temps de voir comment nous allons gérer la messagerie dans Redux. Nous avons défini nos actions [ici](https://github.com/mihailgaberov/chat/blob/master/src/store/message/actions/index.ts) et notre messageReducer [ici](https://github.com/mihailgaberov/chat/blob/master/src/store/message/reducer/index.ts).

* **Actions** — ici nous définissons les principales actions nécessaires pour envoyer et recevoir des messages, ainsi que pour changer le nom d'utilisateur.

* **Réducteur** — c'est là que vit notre fonction messageReducer et où nous définissons ce qui se passe lorsqu'une des actions ci-dessus est dispatchée.

#### Socket

Nous suivons la même logique que ci-dessus ici. Nous avons nos [actions de socket](https://github.com/mihailgaberov/chat/blob/master/src/store/socket/actions/index.ts), le [middleware](https://github.com/mihailgaberov/chat/tree/master/src/store/socket/middleware) que j'ai mentionné ci-dessus, et le [socketReducer](https://github.com/mihailgaberov/chat/blob/master/src/store/socket/reducer/index.ts).

* **Actions** — contient des actions pour connecter le socket (celui dispatché depuis le composant Navigation au début lorsque l'application est démarrée) et une pour lorsque le statut de connexion est changé, c'est-à-dire montrer si nous sommes connectés ou non.

* **Middleware** — contient l'implémentation d'un middleware socket simple, qui nous fournit la fonctionnalité minimale dont nous avons besoin dans notre application de chat.

* **Réducteur** — c'est là que vit notre fonction socketReducer et où nous définissons ce qui se passe lorsqu'une des actions ci-dessus est dispatchée.

### Thèmes

Afin d'implémenter la possibilité de définir différents thèmes de couleurs dans notre application et en tenant compte du fait que nous utilisons styled-components, j'ai utilisé un [ThemeProvider](https://www.styled-components.com/docs/advanced) — un composant fourni par eux. [Voici](https://github.com/mihailgaberov/chat/blob/master/src/theme/index.ts) l'implémentation qui inclut la définition d'objets avec des couleurs personnalisées utilisées dans les thèmes.

La logique derrière l'application du thème de couleur sélectionné réside [ici](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx). Idéalement, le composant conteneur devrait être nommé différemment de *TranslationsProvider*, car il ne gère pas seulement les traductions, comme nous le voyons. Nous pourrions ajouter cela à la liste des améliorations/refactorisations futures.

Voici à quoi ressemblent les thèmes de couleurs existants :

![Image](https://cdn-media-1.freecodecamp.org/images/tFLYC4dB7W8z0EcZrxzuBNSGlqvEkfRD7f9G align="left")

### Utilitaires

Dans presque tous les projets logiciels, à un certain moment, le besoin de fonctions réutilisables communes émerge. C'est le moment où les développeurs créent généralement un fichier partagé commun ou des fichiers contenant de telles fonctions d'assistance. Dans notre cas, il s'agit du dossier **/utilities** qui contient actuellement quatre fichiers. Je vais passer en revue chacun d'eux ci-dessous et expliquer la logique derrière ma décision de le créer et de le placer là :

* [common.ts](https://github.com/mihailgaberov/chat/blob/master/src/utilities/common.ts) — voici l'endroit où j'ai décidé de placer de telles fonctions d'assistance communes, qui doivent être facilement utilisées là où elles sont nécessaires dans toute l'application. Dans ce cas spécifique, vous trouverez quatre fonctions utilisées pour le formatage de l'heure, et une aide pour définir la page active et pour faire défiler un élément vers le bas.

* [localStorageService.ts](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts) — j'ai déjà mentionné ce service dans la [première partie](https://medium.com/p/1c9d50897b/edit) de ce tutoriel. C'est ici que vivent toutes les méthodes de manipulation du stockage local.

* [TranslationsProvider.tsx](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx) — ce composant a également été mentionné à plusieurs reprises, mais pour plus de clarté, je vais le mentionner à nouveau ici. Il contient la logique pour fournir des traductions et un thème de couleur dans l'application.

* [withTranslations.tsx](https://github.com/mihailgaberov/chat/blob/master/src/utilities/withTranslations.tsx) — il s'agit d'un [composant d'ordre supérieur (HOC)](https://tylermcginnis.com/react-higher-order-components/) qui est responsable de l'attachement du contexte de l'application (contenant les traductions et les thèmes eux-mêmes) à tout composant enveloppé par celui-ci.

Voici un exemple de son utilisation :

```python
export default withTranslations(SettingsPage as React.FunctionComponent);
```

Nous avons parcouru un long chemin jusqu'ici et nous n'avons pas encore commencé la mise en œuvre réelle.

C'est un indicateur clair pour nous montrer à quel point la phase de planification d'un projet peut être importante et étendue.

Passons maintenant à la phase de mise en œuvre dans la section suivante.

### Mise en œuvre

Si vous avez atteint ce point du tutoriel, vous devriez avoir une idée très claire de ce que nous allons construire. Ici, nous allons découvrir comment nous allons le faire.

#### Commencer petit

Comme pour tout autre projet, nous devons nous efforcer de commencer par de petits morceaux incrémentiels et de construire sur eux. Dans notre cas, j'ai décidé de commencer par construire l'en-tête de navigation. La raison en était que je voulais avoir le routeur et les contrôles de navigation en place, afin de pouvoir naviguer facilement entre les onglets pendant le développement et les tests.

#### Page des paramètres

Après avoir terminé les parties d'en-tête et de navigation, j'ai décidé de passer d'abord à la page des paramètres. Encore une fois, mon raisonnement était très simple — je voulais construire d'abord ce que j'allais utiliser dans la page de chat. En d'autres termes, je voulais pouvoir personnaliser ma zone de chat, mes messages, les moyens d'envoi, etc., avant de les implémenter.

J'ai donc commencé à construire composant par composant comme je les ai décrits dans la [section précédente](https://mihail-gaberov.eu/how-i-build-chat-app-with-react-and-typescript-part3/). Une fois que j'ai eu la page des paramètres entièrement terminée, j'ai pu aller et commencer à implémenter les composants de la page de chat. Mais avant cela, j'ai dû m'occuper des éléments de support — l'intégration avec le [stockage local](https://github.com/mihailgaberov/chat/blob/master/src/utilities/localStorageService.ts) et l'ajout du [mécanisme de traduction](https://github.com/mihailgaberov/chat/blob/master/src/utilities/TranslationsProvider.tsx).

#### Page de chat

Après avoir fait tout ce qui précède, l'implémentation de la page de chat et de ses composants a été assez facile. J'ai dû m'occuper principalement de la partie visuelle et faire l'intégration avec le magasin Redux. Comme vous l'[avez déjà vu](https://github.com/mihailgaberov/chat/blob/master/src/components/pages/Chat/ChatPage.tsx), j'ai dû implémenter seulement deux composants qui sont affichés et utilisés sur la page de chat — ChatArea et MessageSender.

### Ajout d'améliorations

Je veux dire quelques mots ici concernant les améliorations de l'application que nous avons faites ou que nous ferons à l'avenir. Habituellement, lorsque nous avons une nouvelle exigence (appelons-la "exigence", cela la rapproche de ce que ce serait dans un projet réel), il est à nouveau très bon de faire une recherche initiale, au lieu de se lancer directement dans la mise en œuvre. Vous serez surpris de voir combien de solutions existent déjà, attendant que nous les utilisions.

En d'autres termes, nous n'avons pas à réinventer la roue.

C'est ce que j'ai fait lorsque j'ai commencé à penser à ajouter la prise en charge des émoticônes ou l'analyse des liens. Il s'est avéré qu'il existe déjà des solutions que je pourrais utiliser avec un petit ajustement de ma part, juste pour les faire bien s'intégrer dans mon projet.

Voici les liens vers les packages que j'ai utilisés :

* [https://www.npmjs.com/package/linkifyjs](https://www.npmjs.com/package/linkifyjs)

* [https://docs.microlink.io/sdk/getting-started/react/](https://docs.microlink.io/sdk/getting-started/react/)

* [https://www.npmjs.com/package/react-emojione](https://www.npmjs.com/package/react-emojione)

* [https://www.npmjs.com/package/get-urls](https://www.npmjs.com/package/get-urls)

Et [ici](https://github.com/mihailgaberov/chat/blob/master/src/components/Message/Message.tsx) vous pouvez voir comment je les ai utilisés dans notre application de chat.

### Déploiement sur Heroku

J'ai écrit [un autre article](https://mihail-gaberov.eu/creating-twitter-bot/) dans le passé. Il traitait d'un sujet totalement différent, mais il y a une partie exactement liée à la manière de déployer une application sur Heroku. Vous pourriez trouver utile de le consulter.

Pour déployer notre application de chat sur [Heroku](https://herokuapp.com/), je vais supposer que vous avez déjà un compte et que vous pouvez facilement suivre les étapes ci-dessous :

1. `npm build` pour construire le projet dans le dossier `build`.

2. Ajoutez le dossier `build` à Git pour vous assurer qu'il sera validé.

3. Assurez-vous que le serveur express charge les ressources statiques à partir de celui-ci.

4. Validez tout : `git commit -m 'Déployer sur Heroku'`.

5. Exécutez `git push heroku master`.

6. Ouvrez l'application à partir de l'URL donnée (dans mon cas : [mihails-chat.herokuapp.com](https://mihails-chat.herokuapp.com/#/chat)).

### Plans futurs (possibles)

Au moment de la rédaction de ce document, je pensais qu'il pourrait être très intéressant d'essayer de construire la même application avec l'autre bibliothèque d'interface utilisateur super célèbre sur le marché — [Angular](https://angular.io/). Je pense toujours que cela en vaudrait la peine, mais je ne suis pas sûr d'avoir le temps et l'énergie pour le faire ?.

Dans tous les cas, ce à quoi je pense, c'est une comparaison technique pure de deux grandes bibliothèques d'interface utilisateur du point de vue du développeur.

Si je le fais, je m'assurerai que vous le sachiez !

Merci d'avoir lu. Vous pouvez lire plus de mes articles sur [mihail-gaberov.eu](https://mihail-gaberov.eu/how-i-build-chat-app-with-react-and-typescript-part1/).