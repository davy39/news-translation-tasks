---
title: Comment surveiller les changements de réseau en utilisant Redux Saga dans React
  Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T23:29:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-monitor-network-changes-using-redux-saga-in-react-native-b7b95635ef65
coverImage: https://cdn-media-1.freecodecamp.org/images/0*l5MxcXOJgo-EZ-ht
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Comment surveiller les changements de réseau en utilisant Redux Saga dans
  React Native
seo_desc: 'By Pritish Vaidya

  Why should I use Redux Saga to monitor Network Changes?


  _Image Credit — [ImgFlip](https://i.imgflip.com/2knj8b.jpg" rel="noopener" target="blank"
  title=")

  Redux Saga is an alternate side effect model for redux apps. It is easier to...'
---

Par Pritish Vaidya

#### Pourquoi devrais-je utiliser Redux Saga pour surveiller les changements de réseau ?

![Image](https://cdn-media-1.freecodecamp.org/images/icYVSeaXDsfe83z7SkYSyKE-AKKWjQF7XOE5)
_Crédit Image — [ImgFlip](https://i.imgflip.com/2knj8b.jpg" rel="noopener" target="_blank" title=")_

Redux Saga est un modèle de _side effect_ alternatif pour les applications redux. Il est plus facile à gérer, exécuter, tester et capturer les erreurs.

Plutôt que d'implémenter la logique pour gérer l'_état du réseau_ dans votre composant react, les `side-effects` doivent être gérés séparément. Redux Saga nous fournit _eventChannel_ comme une solution clé en main pour gérer de tels cas.

### Qu'est-ce qu'un Event Channel ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1OSYcBjFfR0OqQ1JNH20hEvGHZ1Xrbzzv2em.jpeg)
_Crédit Image — [Unsplash](https://images.unsplash.com/photo-1538131688925-7e0eb2e7828b)_

Redux Saga utilise des `eventChannels` pour communiquer entre des _événements externes_ et des _sagas_ en tant que fonction de fabrication. Les événements proviennent de sources d'événements _autres que le store redux_.

Voici un exemple de base tiré de la [documentation](https://github.com/redux-saga/redux-saga/blob/master/docs/advanced/Channels.md#using-the-eventchannel-factory-to-connect-to-external-events) :

```js
import { eventChannel } from 'redux-saga'

function countdown(secs) {
  return eventChannel(emitter => {
      const iv = setInterval(() => {
        secs -= 1
        if (secs > 0) {
          emitter(secs)
        } else {
          // cela ferme le canal
          emitter(END)
        }
      }, 1000);
      return () => {
        clearInterval(iv)
      }
    }
  )
}
```

Points à noter :

* Le premier argument de `eventChannel` est une fonction d'écoute.
* La méthode de retour est la fonction de _désinscription de l'écouteur_.

L'émetteur _initialise l'écouteur une fois_, après quoi tous les événements de l'écouteur sont _passés à la fonction d'émetteur_ en l'invoquant.

#### Comment connecter l'Event Channel de Redux Saga avec l'API Network (NetInfo) de React Native ?

L'API **NetInfo** `[isConnected](https://facebook.github.io/react-native/docs/netinfo#isconnected)` de React Native récupère de manière asynchrone un _booléen_ qui détermine si l'appareil est `en ligne` ou `hors ligne`.

#### Plongeons dans le code

![Image](https://www.freecodecamp.org/news/content/images/2021/06/1MwK-maPG4EYywcUFOeyEAZTUxleIx8DSSM0.jpeg)
_Crédit Image — [Unsplash](https://unsplash.com/photos/pgSkeh0yl8o)_

**Tout d'abord, nous devons créer une méthode de démarrage de canal.**

```js
import { NetInfo } from "react-native"
import { eventChannel} from "redux-saga"

function * startChannel() {
  const channel = eventChannel(listener => {
    const handleConnectivityChange = (isConnected) => {
      listener(isConnected);
    }
    
// Initialiser l'écouteur de connectivité
    NetInfo.isConnected.addEventListener("connectionChange", handleConnectivityChange);
    
// Retourner la fonction de désinscription de l'écouteur d'événements.
    return () =>
      NetInfo.isConnected.removeEventListener("connectionChange",    handleConnectivityChange);
  });
}
```

L'étape suivante consiste à **écouter les changements d'événements** dans le canal.

```js
...

while (true) {
  const connectionInfo = yield take(channel);
}

...
```

L'étape finale consiste à **passer une action personnalisée** au canal afin que la _valeur puisse être synchronisée en utilisant votre action_.

```js
...
function * startChannel(syncActionName) {

...
while (true) {
  const connectionInfo = yield take(channel);
  yield put({type: syncActionName, status: connectionInfo });
}
```

Ce **canal** peut être utilisé dans notre générateur exporté par défaut en utilisant l'opération [_call_](https://github.com/redux-saga/redux-saga/tree/master/docs/api#callfn-args).

```js
export default function* netInfoSaga() {
  try {
    yield call(startChannel, 'CONNECTION_STATUS');
  } catch (e) {
    console.log(e);
  }
}
```

Le _générateur exporté_ peut ensuite être _importé_ et utilisé comme une _tâche détachée_ en utilisant l'opération [spawn/fork](https://github.com/redux-saga/redux-saga/tree/master/docs/api#spawnfn-args) dans notre saga principale.

### Utilisation

Le code ci-dessus a été ajouté en tant que package `react-native-network-status-saga` pour inclure certains des paramètres les plus utiles et intéressants.

Voici les liens

* [GitHub](https://github.com/pritishvaidya/react-native-network-status-saga)
* [npm](https://www.npmjs.com/package/react-native-network-status-saga)

_Merci d'avoir lu. Si vous avez aimé cet article, montrez votre soutien en applaudissant cet article pour le partager avec d'autres personnes sur Medium._

_D'autres choses intéressantes peuvent être trouvées sur mes profils [StackOverflow](https://stackoverflow.com/users/6606831/pritish-vaidya) et [GitHub](https://github.com/pritishvaidya)._

_Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/pritish-vaidya-506686128/), [Medium](https://medium.com/@pritishvaidya94), [Twitter](https://twitter.com/PritishVaidya) pour d'autres mises à jour et nouveaux articles._