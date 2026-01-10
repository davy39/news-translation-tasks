---
title: Comment travailler avec React de la bonne manière pour éviter certains pièges
  courants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T21:35:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-react-the-right-way-to-avoid-some-common-pitfalls-fc9eb5e34d9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s5pDmyXqPnXV0sNmgGCIxw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment travailler avec React de la bonne manière pour éviter certains
  pièges courants
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@swimstaralex?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Alexander
  Sinn / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  One thi...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-251.png)
_Photo par [Unsplash](https://unsplash.com/@swimstaralex?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Alexander Sinn</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Une chose que j'entends assez souvent est « **Allons-y pour Redux** » dans notre nouvelle application React. Cela vous aide à évoluer, et les données de l'application ne devraient pas être dans l'état local de React car c'est inefficace. Ou lorsque vous appelez une API et que la promesse est en attente, le composant se désinstalle et vous obtenez l'erreur suivante.

> Avertissement : Impossible d'appeler setState (ou forceUpdate) sur un composant désinstallé. Cela n'a aucun effet, mais cela indique une fuite de mémoire dans votre application. Pour corriger cela, annulez toutes les abonnements et les tâches asynchrones dans la méthode componentWillUnmount.

La solution que les gens adoptent généralement est donc d'utiliser **Redux**. J'adore Redux et le travail que fait [**Dan Abramov**](https://twitter.com/dan_abramov) est tout simplement **incroyable !** Ce gars est vraiment génial — je souhaite être aussi talentueux que lui.

Mais je suis sûr que lorsque Dan a créé Redux, il nous donnait simplement un outil dans notre ceinture à outils en tant qu'aide. Ce n'est pas le couteau suisse de tous les outils. Vous n'utilisez pas un marteau lorsque vous pouvez visser le boulon avec un tournevis.

[**Dan est même d'accord**](https://twitter.com/dan_abramov)**.**

J'adore React, et je travaille dessus depuis presque deux ans maintenant. Jusqu'à présent, aucun regret. Meilleure décision jamais prise. J'aime Vue et toutes les bibliothèques/frameworks sympas qui existent. Mais React occupe une place spéciale dans mon cœur. Il m'aide à me concentrer sur le travail que je suis censé faire plutôt que de prendre tout mon temps dans les manipulations du DOM. Et il le fait de la meilleure et plus efficace manière possible, avec sa [réconciliation efficace](https://github.com/acdlite/react-fiber-architecture).

J'ai beaucoup appris au cours de ces dernières années, et j'ai remarqué un problème commun parmi les développeurs React, nouveaux et expérimentés : ne pas utiliser React de la bonne manière lors de la gestion des abonnements ou des tâches asynchrones. Je pense que la documentation disponible n'est pas bien présentée dans ce cas, et j'ai donc décidé d'écrire cet article.

Je vais d'abord parler des abonnements, puis nous passerons à la gestion de l'annulation des tâches asynchrones pour éviter les fuites de mémoire dans React (le principal objectif de cet article). Si elles ne sont pas gérées, cela ralentit notre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pHRQWgW6YXlirkX3BTXKeQ.jpeg)
_Effaçons tous les abonnements/tâches asynchrones, et en guise de rappel, ne vous dirigez pas vers le Mordor_

Maintenant, revenons à ce beau message d'erreur dont nous avons parlé initialement :

> Avertissement : Impossible d'appeler setState (ou forceUpdate) sur un composant désinstallé. Cela n'a aucun effet, mais cela indique une fuite de mémoire dans votre application. Pour corriger cela, annulez toutes les abonnements et les tâches asynchrones dans la méthode componentWillUnmount.

Mon objectif pour cet article est de m'assurer que personne n'ait jamais à faire face à cette erreur et de ne pas savoir quoi en faire à nouveau.

### Ce que nous allons couvrir

* Effacer les abonnements comme setTimeout/setInterval
* Effacer les actions asynchrones lorsque vous appelez une requête XHR en utilisant `fetch` ou des bibliothèques comme `axios`
* Méthodes alternatives, certaines opinées, d'autres obsolètes.

Avant de commencer, un énorme merci à [**Kent C Dodds**](https://twitter.com/kentcdodds), la personne la plus cool sur Internet en ce moment. Merci d'avoir pris le temps et de redonner à la communauté. Ses [podcasts **Youtube**](https://www.youtube.com/user/kentdoddsfamily) et son cours egghead sur [**Advanced React Component Patterns**](https://egghead.io/courses/advanced-react-component-patterns) sont incroyables. Consultez ces ressources si vous voulez passer à l'étape suivante dans vos compétences React.

J'ai demandé à Kent une meilleure approche pour éviter **setState** lors du démontage d'un composant afin de mieux optimiser les performances de React. Il a dépassé mes attentes et a fait une vidéo à ce sujet. Si vous êtes du genre à regarder des vidéos, consultez-la ci-dessous. Elle vous donnera une marche à suivre étape par étape avec une explication détaillée.

%[https://www.youtube.com/watch?v=8BNdxFzMeVg]

Alors maintenant, plongeons-nous et commençons.

### 1 : Effacer les abonnements

Commençons par l'exemple :

%[https://codesandbox.io/s/m3rn84m7y9?from-embed]

Parlons de ce qui vient de se passer ici. Ce que je veux que vous regardiez, c'est le fichier `counter.js` qui incrémente essentiellement le compteur après 3 secondes.

Cela donne une erreur après 5 secondes, car j'ai désinstallé un abonnement sans le supprimer. Si vous voulez voir l'erreur à nouveau, il suffit de cliquer sur le bouton d'actualisation dans l'éditeur CodeSandbox pour voir l'erreur dans la console.

J'ai mon fichier conteneur `index.js` qui bascule simplement le composant du compteur après les cinq premières secondes.

Donc

> — — — — → Index.js

> — — — — — → Counter.js

Dans mon Index.js, j'appelle Counter.js et je fais simplement ceci dans mon rendu :

```
{showCounter ? <Counter /> : null}
```

Le `showCounter` est un booléen d'état qui se définit lui-même sur false après les 5 premières secondes dès que le composant est monté (componentDidMount).

La vraie chose qui illustre notre problème ici est le fichier `counter.js` qui incrémente le compte après chaque 3 secondes. Donc après les 3 premières secondes, le compteur est mis à jour. Mais dès qu'il arrive à la deuxième mise à jour, qui se produit à la 6ème seconde, le fichier `index.js` a déjà désinstallé le composant du compteur à la 5ème seconde. Au moment où le composant du compteur atteint sa 6ème seconde, il met à jour le compteur pour la deuxième fois.

Il met à jour son état, mais voici le problème. Il n'y a pas de DOM pour que le composant du compteur met à jour l'état, et c'est à ce moment que React lance une erreur. Cette belle erreur dont nous avons parlé plus haut :

> Avertissement : Impossible d'appeler setState (ou forceUpdate) sur un composant désinstallé. Cela n'a aucun effet, mais cela indique une fuite de mémoire dans votre application. Pour corriger cela, annulez toutes les abonnements et les tâches asynchrones dans la méthode componentWillUnmount.

Maintenant, si vous êtes nouveau dans React, vous pourriez dire : « Eh bien, **Adeel...** oui, mais n'avons-nous pas désinstallé le composant Counter à la 5ème seconde ? S'il n'y a pas de composant pour le compteur, comment son état peut-il encore se mettre à jour à la sixième seconde ? »

Oui, vous avez raison. Mais lorsque nous faisons quelque chose comme `setTimeout` ou `setInterval` dans nos composants React, cela ne dépend pas ou n'est pas lié à notre classe React comme vous pourriez le penser. Il continuera à s'exécuter après sa condition spécifiée à moins que vous n'annuliez son abonnement.

Maintenant, vous pourriez déjà faire cela lorsque votre condition est remplie. Mais que se passe-t-il si votre condition n'a pas encore été remplie et que l'utilisateur décide de changer de page où cette action est toujours en cours ?

La meilleure façon de supprimer ces types d'abonnements est dans votre cycle de vie `componentWillUnmount`. Voici un exemple de la façon dont vous pouvez le faire. Consultez la méthode componentWillUnmount du fichier counter.js :

%[https://codesandbox.io/s/xr7j5507qp?from-embed]

Et c'est à peu près tout pour `setTimout` et `setInterval`.

### 2 : Annulation des requêtes API (XHR)

* L'ancienne approche laide (obsolète)
* La nouvelle approche meilleure (le principal objectif de cet article)

Nous avons donc discuté des abonnements. Mais que se passe-t-il si vous faites une requête asynchrone ? Comment l'annulez-vous ?

#### L'ancienne méthode

Avant d'en parler, je veux parler d'une méthode obsolète dans React appelée `isMounted()`

Avant décembre 2015, il y avait une méthode appelée `isMounted` dans React. Vous pouvez en lire plus à ce sujet dans le blog React [**blog**](https://reactjs.org/blog/2015/12/16/ismounted-antipattern.html)**.** Ce qu'elle faisait était quelque chose comme ceci :

```javascript
import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

class RandomUser extends React.Component {
  state = {user: null}
  _isMounted = false
  handleButtonClick = async () => {
    const response = await axios.get('https://randomuser.me/api/')
    if (this._isMounted) {
      this.setState({ user: response.data })
    }
  }
  componentDidMount() {
    this._isMounted = true
  }
  componentWillUnmount() {
    this._isMounted = false
  }
  render() {
    return (
      <div>
        <button onClick={this.handleButtonClick}>Cliquez-moi</button>
        <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
      </div>
    )
  }
}
```

Pour les besoins de cet exemple, j'utilise une bibliothèque appelée `axios` pour faire une requête XHR.

Passons en revue cela. J'ai initialement défini `this_isMounted` sur `false` juste à côté de l'endroit où j'ai initialisé mon état. Dès que le cycle de vie `componentDidMount` est appelé, je définis `this._isMounted` sur true. Pendant ce temps, si un utilisateur final clique sur le bouton, une requête XHR est faite. J'utilise `randomuser.me`. Dès que la promesse est résolue, je vérifie si le composant est toujours monté avec `this_isMounted`. Si c'est vrai, je mets à jour mon état, sinon je l'ignore.

L'utilisateur a peut-être cliqué sur le bouton pendant que l'appel asynchrone était en cours de résolution. Cela entraînerait le changement de page par l'utilisateur. Donc, pour éviter une mise à jour d'état inutile, nous pouvons simplement la gérer dans notre méthode de cycle de vie `componentWillUnmount`. Je définis simplement `this._isMounted` sur false. Ainsi, chaque fois que l'appel API asynchrone est résolu, il vérifiera si `this_isMounted` est false et ne mettra pas à jour l'état.

Cette approche fait le travail, mais comme le disent les docs React :

> Le cas d'utilisation principal de `isMounted()` est d'éviter d'appeler `setState()` après qu'un composant a été désinstallé, car l'appel de `setState()` après qu'un composant a été désinstallé émettra un avertissement. L'avertissement « setState » existe pour vous aider à attraper les bugs, car l'appel de `setState()` sur un composant désinstallé est une indication que votre application/composant a d'une manière ou d'une autre échoué à nettoyer correctement. Plus précisément, l'appel de `setState()` dans un composant désinstallé signifie que votre application conserve toujours une référence au composant après que le composant a été désinstallé — ce qui indique souvent une fuite de mémoire ! [Lire la suite...](https://reactjs.org/blog/2015/12/16/ismounted-antipattern.html)

Cela signifie que bien que nous ayons évité un setState inutile, la mémoire n'a toujours pas été libérée. Il y a toujours une action asynchrone qui se produit et qui ne sait pas que le cycle de vie du composant s'est terminé et qu'elle n'est plus nécessaire.

#### Parlons de la bonne méthode

Pour sauver la journée, voici les [**AbortControllers**](https://developer.mozilla.org/en-US/docs/Web/API/AbortController). Selon la documentation [MDN](https://developer.mozilla.org/en-US/docs/Web/API/AbortController), il est indiqué :

> L'interface `**AbortController**` représente un objet contrôleur qui vous permet d'annuler une ou plusieurs requêtes DOM selon vos besoins. [Lire la suite...](https://developer.mozilla.org/en-US/docs/Web/API/AbortController)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CLnYV7AQDdgpS-LAQ6fLlg.jpeg)

Regardons un peu plus en profondeur ici. Avec du code, bien sûr, parce que tout le monde ❤️ le code.

```javascript
var myController = new AbortController();
var mySignal = myController.signal;

var downloadBtn = document.querySelector('.download');
var abortBtn = document.querySelector('.abort');

downloadBtn.addEventListener('click', fetchVideo);

abortBtn.addEventListener('click', function() {
  myController.abort();
  console.log('Téléchargement annulé');
});

function fetchVideo() {
  ...
  fetch(url, { signal: mySignal }).then(function(response) {
    ...
  }).catch(function(e) {
    reports.textContent = 'Erreur de téléchargement : ' + e.message;
  })
}
```

Tout d'abord, nous créons un **nouvel AbortController** et l'assignons à une variable appelée `myController`. Ensuite, nous créons un **signal** pour cet AbortController. Considérez le signal comme un indicateur pour dire à nos requêtes XHR quand il est temps d'annuler la requête.

Supposons que nous avons 2 boutons, `Télécharger` et `Annuler`. Le bouton de téléchargement télécharge une vidéo, mais que se passe-t-il si, pendant le téléchargement, nous voulons annuler cette demande de téléchargement ? Nous devons simplement appeler `myController.abort()`. Maintenant, ce contrôleur annulera toutes les requêtes qui lui sont associées.

Comment, pourriez-vous demander ?

Après avoir fait `var myController = new AbortController()`, nous avons fait ceci `var mySignal = myController.signal`. Maintenant, dans ma requête fetch, où je lui indique l'URL et la charge utile, je dois simplement passer `mySignal` pour lier/signaliser que la requête `FETCH` avec mon incroyable `AbortController`.

Si vous voulez lire un exemple encore plus complet sur `AbortController`, les gens cool de **MDN** ont cet exemple vraiment sympa et élégant sur leur Github. Vous pouvez le consulter [ici](https://github.com/mdn/dom-examples/blob/master/abort-api/index.htm).

Je voulais parler de ces requêtes d'annulation parce que peu de gens en sont conscients. La demande d'annulation dans fetch a commencé en 2015. Voici le [problème GitHub original sur l'annulation](https://github.com/whatwg/fetch/issues/27) — il a finalement obtenu un support autour d'octobre 2017. Cela fait un écart de deux ans. Wow ! Il existe quelques bibliothèques comme **axios** qui offrent un support pour AbortController. Je vais discuter de la façon dont vous pouvez l'utiliser avec axios, mais je voulais d'abord montrer la version détaillée sous le capot de la façon dont AbortController fonctionne.

### **Annulation d'une requête XHR dans Axios**



> « Fais-le, ou ne le fais pas. Il n'y a pas d'essai. » — Yoda

L'implémentation dont j'ai parlé ci-dessus n'est pas spécifique à React, mais c'est ce dont nous allons discuter ici. Le principal objectif de cet article est de vous montrer comment effacer les manipulations DOM inutiles dans React lorsqu'une requête XHR est faite et que le composant est désinstallé alors que la requête est en état d'attente. Ouf !

Alors sans plus tarder, voici comment faire.

```javascript
import React, { Component } from 'react';
import axios from 'axios';

class Example extends Component {
  signal = axios.CancelToken.source();

  state = {
    isLoading: false,
    user: {},
  }
  
  componentDidMount() {
    this.onLoadUser();
  }
  
  componentWillUnmount() {
    this.signal.cancel('L\'API est en cours d\'annulation');
  }
  
  onLoadUser = async () => {
    try {
      this.setState({ isLoading: true });
      const response = await axios.get('https://randomuser.me/api/', {
        cancelToken: this.signal.token,
      })
      this.setState({ user: response.data, isLoading: true });
    } catch (err) {
      if (axios.isCancel(err)) {
        console.log('Erreur : ', err.message); // => imprime : L'API est en cours d'annulation
      } else {
        this.setState({ isLoading: false });
      }
    }
   } 
   
    
    render() {
      return (
        <div>
          <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
        </div>
      )
    }
 
}
```

Passons en revue ce code

Je définis `this.signal` sur `axios.CancelToken.source()` qui instancie essentiellement un nouvel `AbortController` et assigne le signal de cet `AbortController` à `this.signal`. Ensuite, j'appelle une méthode dans `componentDidMount` appelée `this.onLoadUser()` qui appelle les informations d'un utilisateur aléatoire à partir d'une API tierce `randomuser.me`. Lorsque j'appelle cette API, je passe également le signal à une propriété dans axios appelée `cancelToken`

La prochaine chose que je fais est dans mon `componentWillUnmount` où j'appelle la méthode d'annulation qui est liée à ce `signal`. Maintenant, supposons que dès que le composant a été chargé, l'API a été appelée et la `requête XHR est passée en état d'attente`.

Maintenant, la requête était en attente (c'est-à-dire qu'elle n'a pas été résolue ou rejetée mais l'utilisateur a décidé d'aller sur une autre page. Dès que la méthode de cycle de vie `componentWillUnmount` est appelée, nous allons annuler notre requête API. Dès que l'API est annulée, la promesse sera rejetée et elle atterrira dans le bloc `catch` de cette instruction `try/catch`, en particulier dans le bloc `if (axios.isCancel(err) {}`.

Maintenant, nous savons explicitement que l'API a été annulée, car le composant a été désinstallé et donc enregistre une erreur. Mais nous savons que nous n'avons plus besoin de mettre à jour cet état puisque ce n'est plus nécessaire.

**P.S :** Vous pouvez utiliser le même signal et le passer à autant de requêtes XHR dans votre composant que vous le souhaitez. Lorsque le composant est désinstallé, toutes ces requêtes XHR qui sont en attente seront annulées lorsque componentWillUnmount est appelé.

### Détails finaux

Félicitations ! :) Si vous avez lu jusqu'ici, vous venez d'apprendre comment annuler une requête XHR selon vos propres termes.

Continuons un peu plus. Normalement, vos requêtes XHR sont dans un fichier, et votre composant conteneur principal est dans un autre (à partir duquel vous appelez cette méthode API). Comment passez-vous ce signal à un autre fichier et annulez toujours cette requête XHR ?

Voici comment faire :

```javascript
import React, { Component } from 'react';
import axios from 'axios';

// API
import { onLoadUser } from './UserAPI';

class Example extends Component {
  signal = axios.CancelToken.source();

  state = {
    isLoading: false,
    user: {},
  }
  
  componentDidMount() {
    this.onLoadUser();
  }
  
  componentWillUnmount() {
    this.signal.cancel('L\'API est en cours d\'annulation');
  }
  
  onLoadUser = async () => {
    try {
      this.setState({ isLoading: true });
      const data = await onLoadUser(this.signal.token);
      this.setState({ user: data, isLoading: true });
    } catch (error) {
      if (axios.isCancel(err)) {
        console.log('Erreur : ', err.message); // => imprime : L'API est en cours d'annulation
      } else {
        this.setState({ isLoading: false });
      }
    }
  }
    
    render() {
      return (
        <div>
          <pre>{JSON.stringify(this.state.user, null, 2)}</pre>
        </div>
      )
    }
  };
 
}
```

```javascript
export const onLoadUser = async myCancelToken => {
  try {
    const { data } = await axios.get('https://randomuser.me/api/', {
      cancelToken: myCancelToken,
    })
    return data;
  } catch (error) {
    throw error;
  }
};
```

J'espère que cela vous a aidé et que vous avez appris quelque chose. Si vous avez aimé, n'hésitez pas à applaudir.

Merci d'avoir pris le temps de lire. Un grand merci à mon collègue très talentueux [**Kinan**](http://kazmi@facebook.com) pour m'avoir aidé à relire cet article. Merci à **K[ent C Dodds](https://twitter.com/kentcdodds)** pour être une inspiration dans la communauté JavaScript OSS.

Encore une fois, j'adorerais avoir votre retour. Vous pouvez toujours me contacter sur [**Twitter**](http://twitter.com/adeelibr)**.**

Il y a aussi [une autre lecture incroyable](https://developers.google.com/web/updates/2017/09/abortable-fetch) sur **Abort Controller** que j'ai trouvée à travers la documentation **MDN** par **Jake Archibald**. Je vous suggère de la lire, si vous avez une nature curieuse comme la mienne.