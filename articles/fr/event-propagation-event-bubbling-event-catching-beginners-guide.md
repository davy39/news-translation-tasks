---
title: La remontée d'événements et la capture d'événements en JavaScript et React
  – Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-08T15:37:42.000Z'
originalURL: https://freecodecamp.org/news/event-propagation-event-bubbling-event-catching-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-anthony-132477.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: La remontée d'événements et la capture d'événements en JavaScript et React
  – Un guide pour débutants
seo_desc: 'By Mariya Diminsky

  In this article, I''ll help you understand event bubbling and event catching like
  a pro. I created this resource to help you understand event propagation and how
  it works in JavaScript and React in a clear and comprehensible way. ❤

  ...'
---

Par Mariya Diminsky

Dans cet article, je vais vous aider à comprendre la remontée d'événements et la capture d'événements comme un pro. J'ai créé cette ressource pour vous aider à comprendre la propagation des événements et comment elle fonctionne en JavaScript et React de manière claire et compréhensible. ❤️

Une fois que vous aurez parcouru cette introduction approfondie à la remontée d'événements et à la mise en cache des événements, vous devriez pouvoir commencer à appliquer ce que vous avez appris ici dans vos projets immédiatement.

Voici ce que vous allez apprendre :

* **✨** [Qu'est-ce que la délégation d'événements ?](#heading-qu-est-ce-que-la-delegation-d-evenements)
* ✨ [Qu'est-ce que la remontée d'événements ?](#heading-qu-est-ce-que-la-remontee-d-evenements)
* ✨ [Comment la remontée d'événements se produit en JavaScript](#heading-comment-la-remontee-d-evenements-se-produit-en-javascript)
* ✨ [Comment la remontée d'événements se produit en React](#heading-comment-la-remontee-d-evenements-se-produit-en-react)
* ✨ [Comment arrêter la remontée d'événements dans vos composants](#heading-comment-arreter-la-remontee-d-evenements-dans-vos-composants)
* ✨ [Event.target vs Event.currentTarget](#heading-eventtarget-vs-eventcurrenttarget)
* ✨ [Ordre de déclenchement des événements mis à jour et paramètre useCapture en JavaScript](#heading-ordre-de-declenchement-des-evenements-mis-a-jour-et-parametre-usecapture-en-javascript)
* ✨ [Quels événements ne remontent pas et comment sont-ils gérés ?](#heading-quels-evenements-ne-remontent-pas-et-comment-sont-ils-geres)
* ✨ [Écouteurs d'événements dans React Version 16 et avant VS Version 17+](#heading-ecouteurs-d-evenements-dans-react-version-16-et-avant-vs-version-17)
* ✨ [Cas particulier : Que faire si vous avez besoin qu'un parent extérieur se déclenche également ?](#heading-cas-particulier-que-faire-si-vous-avez-besoin-qu-un-parent-exterieur-se-declenche-egalement)

## Qu'est-ce que la délégation d'événements ?

En bref, la délégation d'événements est une technique puissante en JavaScript qui permet une gestion des événements plus efficace.

### ✅ Avantages (plus tard)

* Cette technique est généralement considérée comme performante puisque seule une fonction d'écouteur d'événement est utilisée au niveau du parent de haut niveau plutôt qu'une pour chaque élément enfant.

### ❌ Inconvénients (plus tard)

* Une fois qu'un événement d'un élément enfant interne est appelé, tous les éléments au-dessus/en dessous de lui seront également appelés (remontée/capture). Pour empêcher cela, une méthode sur l'objet `event` doit être appelée.

La **remontée** et la **capture** (expliquées plus tard) nous permettent de mettre en œuvre le modèle de délégation d'événements.

## Qu'est-ce que la remontée d'événements ?

Disons que nous connaissons une fille nommée `Molly`, qui se trouve également être non pas une vraie personne, mais —🥁 roulement de tambour — un composant React. Wow — quelle commodité !

![mème shiba inu "wow such convenience. much impress. so wow"](https://www.freecodecamp.org/news/content/images/2021/09/image-19.png)
_généré via [https://memegenerator.net/](https://memegenerator.net/" rel="nofollow noopener noopener)_

Elle a un parent `div` unique avec un gestionnaire d'événement `onClick` qui, lorsqu'il est cliqué, appelle tout le monde à table pour manger sa nourriture.

Dans ce parent `div` se trouvent plusieurs éléments enfants `button` qui, lorsqu'ils sont cliqués, créent un élément alimentaire fictif (c'est-à-dire les `console.log`).

```javascript
import React, { Component } from "react";

class Molly extends Component {
    handleCallFamilyToEat() {
        console.log("Hey fam! Food's ready!");
    }

    handleCookEggs() {
        console.log("Molly is cooking fluffy eggs...");
    }

    handleMakeRice() {
        console.log("Molly is making some delicious jasmine rice...");
    }

    handleMixChicken() {
        console.log("Molly is mixing chicken with some yummy spicy sauce!");
    }

    render() {
        return (
            <div className="im-a-parent" onClick={this.handleCallFamilyToEat}>
                <button className="im-a-child" onClick={this.handleCookEggs}>Cook Eggs</button>
                <button className="im-a-child" onClick={this.handleMakeRice}>Make Rice</button>
                <button className="im-a-child" onClick={this.handleMixChicken}>Mix Chicken</button>
            </div>
        );
    }

}

export default Molly;
```

Et voici ce qui se passe lorsque vous cliquez sur chacun :

<iframe src="https://giphy.com/embed/eEVi5aB0WIv7rCTlhV" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 



Voici une petite version codepen si vous préférez suivre ainsi :

%[https://codepen.io/maariyadiminsky/pen/MWobvZd?editors=0010]

Comme vous pouvez le voir, cela se produit pour chaque enfant :

1. Tout d'abord, le gestionnaire d'événement du bouton est déclenché.
2. Ensuite, le gestionnaire d'événement du div parent est déclenché.

Dans la plupart des cas, vous voulez probablement que seul le gestionnaire d'événement du bouton soit appelé lorsque vous cliquez dessus. Mais comme vous pouvez le voir, l'événement du parent est également déclenché... !?

Cela s'appelle **✨ la remontée d'événements ✨**.

Dans les prochaines sections, je vais discuter de ce qui se passe et comment nous pouvons le corriger.

## Comment la remontée d'événements se produit en JavaScript

### Pourquoi la remontée d'événements existe-t-elle ?

L'une des intentions de JavaScript avec la création du modèle de propagation des événements était de faciliter la capture des événements à partir d'une seule source — l'élément parent — plutôt que de définir un gestionnaire d'événement sur chaque enfant interne.

### Ordre de déclenchement de la propagation des événements

Il y a trois phases que la propagation des événements traverse :

![graphique affichant la propagation des événements](https://www.freecodecamp.org/news/content/images/2021/09/image-20.png)
_Image de [https://ehsankorhani.com/](https://ehsankorhani.com/" rel="noopener ugc nofollow)_

1. **🏆 Phase de capture** — La première phase lorsqu'un événement est réellement déclenché. Cet événement « capture » ou se propage d'abord à travers l'événement le plus haut, c'est-à-dire l'objet `window`, puis le `document`, puis l'élément `html`, et enfin les éléments les plus internes. Il descend jusqu'à ce qu'il atteigne le `event.target` (ce que vous avez cliqué/événement déclenché).
2. **🏆 Phase de cible** — La deuxième phase est lorsque nous avons atteint le `event.target`. Par exemple, lorsqu'un utilisateur clique sur un bouton, il s'agit de l'élément bouton réel.
3. **🏆 Phase de remontée** — La troisième phase. Cet événement commence à partir du `event.target` et se propage vers le haut jusqu'à ce qu'il atteigne à nouveau le parent le plus haut (bien que l'événement du parent le plus haut ne soit pas appelé à nouveau).

Notez que bien qu'il y ait 3 phases principales, la phase de cible n'est pas réellement gérée séparément. Les gestionnaires d'événements des phases de capture et de remontée sont déclenchés ici.

Il existe également techniquement une autre phase appelée phase « None », où aucune phase d'événement ne se produit. Vous pouvez accéder à la phase dans laquelle se trouve un élément via `[event.eventPhase](https://developer.mozilla.org/en-US/docs/Web/API/Event/eventPhase)`.

En tenant compte de ce que vous venez d'apprendre, regardez l'exemple ci-dessous.

Disons qu'un utilisateur a cliqué sur un élément `td` dans un `table`. Comment la propagation des événements se produirait-elle ici ? **🤔** Prenez un moment pour y réfléchir.

```html
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  </head>
  <body>
    <div id="root">
      <table>
        <tbody>
          <tr>
            <td>Shady Grove</td>
            <td>Aeolian</td>
          </tr>
          <tr>
            <td>Over the River, Charlie</td>
            <td>Dorian</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>

```

Voici ce qui se passe réellement, dans le même ordre que celui mentionné :

Notez que `DefaultView` ici serait l'objet `Window`.

![un autre graphique affichant la propagation des événements en plus de détails](https://www.freecodecamp.org/news/content/images/2021/09/image-21.png)
_Image par [https://www.w3.org/](https://www.w3.org/" rel="nofollow noopener noopener)_

## Comment la remontée d'événements se produit en React

React, en revanche, a créé quelque chose appelé [SyntheticEvent](https://reactjs.org/docs/events.html).

Ce sont simplement des enveloppes pour l'objet événement du navigateur. Le cas d'utilisation de base est similaire et inclut des méthodes comme `stopPropagation` et `preventDefault` (que je vais discuter plus tard). Le plus grand avantage est qu'ils fonctionnent de la même manière dans tous les navigateurs.

React n'attache pas les gestionnaires d'événements aux nœuds — mais plutôt à la racine du document. Lorsqu'un événement est déclenché, React appelle d'abord le bon élément (c'est-à-dire la phase de cible — l'élément que vous avez cliqué), puis il commence à remonter.

Pourquoi React fait-il cela au lieu de simplement gérer les événements de manière similaire au DOM natif ?

<iframe src="https://giphy.com/embed/AqlX1TY49hTS8" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


### Cohérence du navigateur

Il est important que les événements fonctionnent de la même manière dans tous les navigateurs. React a créé des événements synthétiques pour s'assurer que les propriétés restent cohérentes dans différents navigateurs et plateformes.

Vous ne voudriez pas créer une application où un événement fonctionne dans un navigateur, mais qu'un utilisateur dans un autre navigateur utilise votre application et qu'elle ne fonctionne plus — c'est une mauvaise expérience utilisateur.

### Déclencher à partir de l'élément que vous voulez réellement déclencher

Là où le gestionnaire d'événement est défini est là où l'intention est de l'appeler — sur cet élément particulier et nulle part ailleurs (j'ignore temporairement certains cas particuliers ici pour le bien de la compréhension du concept de base d'abord).

Cet événement connaît le mieux l'élément auquel il est défini, donc il devrait être le premier à se déclencher. Après cela, à mesure que la propagation des événements remonte, chaque élément au-dessus en sait de moins en moins.

Prenons, par exemple, notre exemple précédent avec notre composant `Molly`. Je sais que vous la manquez, alors la voici à nouveau ci-dessous :

<iframe src="https://giphy.com/embed/eEVi5aB0WIv7rCTlhV" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


🤔 Avez-vous remarqué que lorsque vous cliquez sur un bouton, le gestionnaire d'événement de ce bouton est appelé en premier et seulement ensuite le gestionnaire d'événement du parent est appelé ?

Cela ne se produit jamais dans l'ordre inverse (c'est-à-dire que la phase de capture n'est jamais déclenchée).

C'est parce que l'événement SyntheticEvent de React n'utilise que la phase de remontée (la phase de cible est incluse ici). Cela a du sens si l'intention est de se concentrer sur le `event.target` (le bouton dans cet exemple) qui a déclenché l'événement en premier.

Gardez à l'esprit que React ne fait que _simuler_ la phase de remontée et de capture native de JavaScript avec ces SyntheticEvents, ce qui explique pourquoi vous pourriez remarquer certaines différences avec le temps (expliqué plus loin dans cet article).

**⚠️ SyntheticEvent** ne se concentre pas nativement sur la phase de capture sauf si vous la définissez spécifiquement. Pour que la phase de capture se déclenche, définissez simplement le gestionnaire d'événement `onClick` du parent `div` sur `onClickCapture` :

```javascript
import React, { Component } from "react";

class Molly extends Component {
    ...

    render() {
        return (
            <div className="im-a-parent" onClickCapture={this.handleCallFamilyToEat}> 
                <button className="im-a-child" onClick={this.handleCookEggs}>Cook Eggs</button>
                <button className="im-a-child" onClick={this.handleMakeRice}>Make Rice</button>
                <button className="im-a-child" onClick={this.handleMixChicken}>Mix Chicken</button>
            </div>
        );
    }

}

export default Molly;
```

Remarquez que, au lieu de la phase de remontée, la phase de capture est déclenchée ci-dessous :

<iframe src="https://giphy.com/embed/BETT2abn9nJdSjenq4" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


**⚠️** Enfin, je voulais mentionner que dans React Version 16 et inférieure, lorsque la phase de remontée est déclenchée dans les SyntheticEvents, elle agit de manière similaire à la phase de remontée native de JavaScript en attachant des gestionnaires d'événements jusqu'à `Document`.

Maintenant, dans React Version 17+, les gestionnaires d'événements n'atteignent que l'élément `root`.

![Image montrant la phase de remontée de React se terminant au niveau racine dans React Version 17 mais se terminant à Window/Document dans React Version 16 ou inférieure](https://www.freecodecamp.org/news/content/images/2021/09/image-22.png)
_Image par [React](https://reactjs.org/blog/2020/08/10/react-v17-rc.html" rel="noopener)_

## Comment arrêter la remontée d'événements dans vos composants

Maintenant que vous comprenez les concepts de base de la **propagation des événements**, de la **remontée d'événements** et de la **capture d'événements**, discutons de la manière de corriger notre problème initial.

Vous avez un bouton (ou un autre élément) et vous voulez que seul le gestionnaire d'événement du bouton se déclenche — aucun autre parent ne doit être déclenché.

🤔 Alors, comment pouvons-nous empêcher cela ? Vous avez quelques options :

### event.stopPropagation()

Cela empêchera tout événement du composant parent de se déclencher. Pour utiliser cela :

1. Assurez-vous de passer l'objet `event` en tant que paramètre.
2. Utilisez la méthode `stopPropagation` sur l'objet événement au-dessus de votre code dans votre fonction de gestionnaire d'événement.

Notez que j'ai changé le `div` parent de `onClickCapture` à `onClick` :

```javascript
import React, { Component } from "react";

class Molly extends Component {
    handleCallFamilyToEat() {
        console.log("Hey fam! Food's ready!");
    }

    handleCookEggs(event) {
        event.stopPropagation(); // UTILISÉ ICI !
        console.log("Molly is cooking fluffy eggs...");
    }

    handleMakeRice() {
        console.log("Molly is making some delicious jasmine rice...");
    }

    handleMixChicken() {
        console.log("Molly is mixing chicken with some yummy spicy sauce!");
    }

    render() {
        return (
            <div className="im-a-parent" onClick={this.handleCallFamilyToEat}> 
                <button className="im-a-child" onClick={this.handleCookEggs}>Cook Eggs</button>
                <button className="im-a-child" onClick={this.handleMakeRice}>Make Rice</button>
                <button className="im-a-child" onClick={this.handleMixChicken}>Mix Chicken</button>
            </div>
        );
    }

}

export default Molly;
```

Ci-dessus, j'ai seulement ajouté `stopPropagation` à la fonction `handleCookEggs`. Donc, lorsque le bouton `Cook Eggs` est cliqué, il ne déclenche que cet événement pour cet élément uniquement.

### event.stopImmediatePropagation()

Disons que vous avez plusieurs événements sur le même élément. Si vous utilisez `event.stopPropagation()`, cela empêchera les événements parents de se déclencher. Mais si vous avez plusieurs événements sur le même élément, ils se déclencheront tous.

Pour empêcher les autres événements sur le même élément de se déclencher, utilisez `event.stopImmediatePropagation()` à la place. Cela empêchera les événements parents et les événements du même élément de se déclencher.

Si vous êtes dans une situation où `event.stopPropagation()` ne fonctionne pas pour vous, essayez `event.stopImmediatePropagation()` à la place.

Note : De temps en temps, il pourrait y avoir une bibliothèque tierce dans votre application qui empêche le premier de fonctionner. Bien sûr, il serait toujours bon de voir ce qui a fait que le second fonctionne mais pas le premier et cela pourrait vous donner un autre indice pour corriger le problème.

### event.preventDefault()

Selon le gestionnaire d'événement et l'élément, vous pourriez vouloir utiliser cela.

Par exemple :

* Si vous avez un formulaire et que vous ne voulez pas que la page se rafraîchisse lorsqu'il est soumis.
* Vous configurez votre propre fonctionnalité de routage et ne voulez pas que la page se rafraîchisse.

## Event.target vs Event.currentTarget

Comprendre la différence entre ces deux propriétés de cible sur l'objet `Event` peut vraiment vous éviter des maux de tête à l'avenir.

Rappelez-vous : L'élément qui déclenche l'événement n'est pas toujours le même que l'élément qui a le gestionnaire d'événement attaché.

**🤔** Confus ? Ne vous inquiétez pas, parcourons cela ensemble.

<iframe src="https://giphy.com/embed/lT9Y1nrHdZWX9QoSH0" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


Prenons notre exemple précédent et `console.log` à la fois le `event.target` et le `event.currentTarget` à l'intérieur du gestionnaire d'événement du div parent.

```javascript
import React, { Component } from "react";

class Molly extends Component {
    // VÉRIFICATION DU PARENT
    handleCallFamilyToEat(event) {
        console.log("Hey fam! Food's ready!");

        console.log("event.target:", event.target);
        console.log("event.currentTarget", event.currentTarget);
    }

    ...

    render() {
        return (
            <div className="im-a-parent" onClick={this.handleCallFamilyToEat}> 
                <button className="im-a-child" onClick={this.handleCookEggs}>Cook Eggs</button>
                <button className="im-a-child" onClick={this.handleMakeRice}>Make Rice</button>
                <button className="im-a-child" onClick={this.handleMixChicken}>Mix Chicken</button>
            </div>
        );
    }

}

export default Molly;
```

Maintenant, lorsque nous cliquons sur le bouton `Cook Eggs`, que voyons-nous ?

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-23.png)
_Image par Mariya Diminsky (moi)_

Remarquez que le gestionnaire d'événement du div parent est conscient que la cible prévue est le bouton.

Mais puisque nous vérifions à l'intérieur du gestionnaire d'événement du parent, nous voyons que le div parent est le `currentTarget`.

D'accord, regardons cela plus en détail.

Que se passe-t-il si nous prenons les mêmes `console.log` et vérifions à l'intérieur du gestionnaire d'événement du bouton réel ?

🤔 Que verrions-nous maintenant ?

```javascript
import React, { Component } from "react";

class Molly extends Component {
    handleCallFamilyToEat(event) {
        console.log("Hey fam! Food's ready!");
    }

    // VÉRIFICATION D'UN BOUTON ENFANT
    handleCookEggs(event) {
        console.log("Molly is cooking fluffy eggs...");
        
        console.log("event.target:", event.target);
        console.log("event.currentTarget", event.currentTarget);
    }

    ...

    render() {
        return (
            <div className="im-a-parent" onClick={this.handleCallFamilyToEat}> 
                <button className="im-a-child" onClick={this.handleCookEggs}>Cook Eggs</button>
                <button className="im-a-child" onClick={this.handleMakeRice}>Make Rice</button>
                <button className="im-a-child" onClick={this.handleMixChicken}>Mix Chicken</button>
            </div>
        );
    }

}

export default Molly;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-24.png)
_Image par Mariya Diminsky (moi)_

Remarquez que puisque nous vérifions maintenant à l'intérieur du gestionnaire d'événement du bouton, nous voyons que le `currentTarget` a changé pour le bouton.

Et bien sûr, puisque nous cliquons sur le bouton, nous savons déjà que le `target` sera à nouveau le `button`.

En tenant compte de ce que vous venez d'apprendre, vous savez maintenant que :

* `event.target` est l'élément le plus profondément imbriqué qui a causé l'événement.
* `event.currentTarget` est l'élément qui écoute l'événement (où le gestionnaire d'événement est attaché).

## Ordre de déclenchement des événements mis à jour et paramètre useCapture en JavaScript

En JavaScript, `EventTarget.addEventListener` sera utilisé pour ajouter un gestionnaire à un événement.

Lorsque nous regardons la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener), nous voyons que vous pouvez soit définir `capture` dans l'objet `options` ou via le paramètre `useCapture` (également maintenant optionnel), qui fait la même chose.

```javascript
// Vous pouvez faire ceci :
yourElement.addEventListener(type, listener, { capture: true });

// ou ceci :
yourElement.addEventListener(type, listener, useCapture: true);
```

⚠️ La raison en est que, sauf si vous le définissez spécifiquement, la phase de capture sera ignorée et, à la place, seule la phase de remontée (après la phase de cible) sera déclenchée nativement en JavaScript. MDN explique également cela :

> Pour les écouteurs d'événements attachés à la cible de l'événement, l'événement est dans la phase de cible, plutôt que dans les phases de capture et de remontée. Les écouteurs d'événements dans la phase de « capture » sont appelés avant les écouteurs d'événements dans toute phase non capturante.

Notez que le paramètre `useCapture` n'a pas toujours été optionnel dans les anciens navigateurs. Assurez-vous de vérifier [caniuse.com](https://caniuse.com/?search=usecapture) avant de l'implémenter.

## Quels événements ne remontent pas et comment sont-ils gérés ?

Bien que la plupart des événements remontent, saviez-vous que plusieurs ne le font pas ?

<iframe src="https://giphy.com/embed/T5QOxf0IRjzYQ" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


Voici quelques exemples en JavaScript natif :

* [blur](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event) ([focusout](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusout_event) est le même mais il remonte réellement).
* [focus](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event) ([focusin](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusin_event) est le même mais il remonte réellement).
* [mouseleave](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event) ([mouseout](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event) est le même mais il remonte réellement).
* [mouseenter](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event) ([mouseover](https://transang.me/everything-about-event-bubbling/mouseover) est le même mais il remonte réellement).
* [load](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event), [unload](https://developer.mozilla.org/en-US/docs/Web/API/Window/unload_event), [abort](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/abort_event), [error](https://developer.mozilla.org/en-US/docs/Web/API/Element/error_event), [beforeunload](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event).

⚠️ Les événements qui remontent ont `true` défini sur l'option `bubbles` [lorsque l'](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event) `[Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)` [est créé](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event) — bien qu'ils passent toujours par la phase de capture.

## Écouteurs d'événements dans React Version 16 et avant VS Version 17+

Comme vous l'avez appris, le SyntheticEvent de React n'agit pas toujours de la même manière que ses équivalents natifs JavaScript.

Apprenons quelques-unes de ces différences ainsi que les changements apportés entre les versions de React.

### Événements que vous ne vous attendriez pas à voir remonter dans React

Par exemple, vous vous attendriez à ce que `onBlur` et `onFocus` de React ne remontent pas puisque l'équivalent natif de JavaScript ne le fait pas, n'est-ce pas ? Pourtant, React a intentionnellement fait en sorte que ces événements, parmi d'autres, continuent à remonter.

⚠️ Bien que React Version 17 ait [apporté quelques changements](https://reactjs.org/blog/2020/08/10/react-v17-rc.html#aligning-with-browsers) à certains événements comme `onScroll` — qui ne remonte plus — la plupart des événements continuent à remonter.

Voir [cette réponse](https://stackoverflow.com/questions/34926910/onfocus-bubble-in-react) et [cet article](https://www.quirksmode.org/blog/archives/2008/04/delegating_the.html) pour plus de détails sur ce sujet.

### `event.target.value` était nulifié dans les fonctions asynchrones

Avant React Version 17, si vous essayiez d'accéder à un événement dans une fonction asynchrone, vous remarquiez qu'il était indéfini.

C'est parce que les objets SyntheticEvent de React étaient regroupés — ce qui signifie qu'après que les gestionnaires d'événements avaient été appelés, vous n'aviez plus accès à eux puisqu'ils étaient réinitialisés et remis dans le pool.

<iframe src="https://giphy.com/embed/NsZbrSS0miha0" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 


![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-25.png)
_Image de [React](https://reactjs.org/docs/legacy-event-pooling.html" rel="noopener)_

Cela pose des problèmes pour les fonctions asynchrones qui ont besoin d'accéder aux informations contenues dans cet événement à un moment ultérieur.

⚠️ La seule façon de conserver ces informations dans les fonctions asynchrones était d'appeler `event.persist()` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-26.png)
_Image de [React](https://reactjs.org/docs/legacy-event-pooling.html" rel="noopener)_

L'intention de cela était d'améliorer les performances. Mais après un examen plus approfondi, l'équipe de React a découvert que cela ne faisait que confondre les développeurs et n'améliorait pas vraiment les performances, donc cela a été complètement abandonné.

⚠️ Avec la sortie de React Version 17, React ne regroupe plus les objets SyntheticEvent. Vous pouvez donc vous attendre à recevoir le `event.target.value` prévu dans vos fonctions asynchrones sans avoir besoin de `event.persist()`.

Assurez-vous de lire plus sur cette mise à jour [ici](https://reactjs.org/blog/2020/08/10/react-v17-rc.html#no-event-pooling).

## Cas particulier : Que faire si vous avez besoin qu'un parent extérieur se déclenche également ?

Prenons tout ce que vous avez appris et corrigeons un cas particulier afin que vous puissiez l'appliquer dans votre prochaine (ou actuelle) application React !

🤔 Disons que nous voulons que ces deux choses fonctionnent dans notre application :

1. Lorsque l'utilisateur clique sur le div/bouton/etc. interne, nous voulons que cet événement se déclenche uniquement (ou dans notre exemple ci-dessous, changer de chaîne sur la TV).
2. Lorsque l'utilisateur clique sur le div parent extérieur, l'événement de ce parent est déclenché (ceci pourrait être utile pour une fenêtre modale. Lorsque l'utilisateur clique à l'extérieur de la fenêtre modale, vous voulez que la fenêtre contextuelle se ferme — ou dans notre exemple ci-dessous, une TV qui est rallumée).

Actuellement, vous savez que si vous cliquez sur l'élément parent/enfant, le système SyntheticEvent de React déclencherait la remontée.

Vous savez également que pour arrêter cela, nous pouvons utiliser `event.stopPropagation()`.

Mais nous sommes confrontés à un dilemme.

Que faire si vous voulez qu'un gestionnaire d'événement se déclenche dans une situation (notre #1), et un autre gestionnaire d'événement se déclenche dans une autre situation (#2) ?

⚠️ Si nous utilisons `event.stopPropagation()`, cela empêcherait un gestionnaire d'événement de se déclencher — mais alors vous ne pourriez jamais appeler l'autre gestionnaire d'événement dans une autre situation. Comment pouvons-nous corriger cela ?

Pour résoudre ce problème, utilisons le modèle d'état de React !

Notez que j'utilise des fonctions fléchées ici, donc le `bind` de l'état n'est pas nécessaire. Si vous n'êtes pas sûr de ce que cela signifie, n'hésitez pas à [lire un autre article que j'ai écrit sur ce sujet ici](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/).

⫸ Ci-dessous, j'ai inclus une version de composant de classe React et une version avec des hooks React — utilisez celle que vous préférez. Assurez-vous de lire attentivement les commentaires :

```javascript
import React, { Fragment, Component } from "react";

import "./TV.css" // vous pouvez ignorer cela puisque cela n'existera pas de votre côté

class TV extends Component {
    state = { channel: 1, shouldTurnOffTV: false };

    // le div parent déclenché si la TV est éteinte
    // cliquer sur changer de chaîne ou éteindre la TV ne se déclenchera pas en même temps  
    // à cause de event.stopPropagation() ici
    handleTurnOnTV = (event) => {
        console.log("In HandleTurnOnTV");

        const { shouldTurnOffTV } = this.state;

        if (shouldTurnOffTV) {
            event.stopPropagation();

            // Je réinitialise la chaîne à 1, mais vous pouvez faire ce que vous voulez ici
            this.setState({ shouldTurnOffTV: false, channel: 1 });
        }
    }

    // le bouton de changement de chaîne enfant déclenché si la TV est allumée
    // cliquer sur le div parent, ou éteindre la TV ne se déclenchera pas en même temps  
    // à cause de event.stopPropagation() ici
    handleChangeChannel = (event) => {
        console.log("In HandleChangeChannel");

        const { channel, shouldTurnOffTV } = this.state;

        if (!shouldTurnOffTV) {
            event.stopPropagation();

            // J'augmente la chaîne de 1, mais vous pouvez faire ce que vous voulez ici
            this.setState({ channel: channel + 1 });
        }
    }

    // le bouton d'extinction de la TV est déclenché
    // cliquer sur le div parent ou changer de chaîne ne se déclenchera pas en même temps 
    // à cause de event.stopPropagation() ici
    handleTurnOffTV = (event) => {
        console.log("In HandleTurnOffTV");

        event.stopPropagation();

        this.setState({ shouldTurnOffTV: true });
    }

    renderChannel = () => {
        const { channel, shouldTurnOffTV } = this.state;

        if (shouldTurnOffTV) {
            return (
                <div>That's it, no more TV time!</div>
            )
        }

        return (
            <Fragment>
                <div>Current Channel: {channel}</div>
                <button className="im-a-child-button" onClick={this.handleTurnOffTV}>Turn Off TV</button>
            </Fragment>
        )
    }

    render() {
        const { shouldTurnOffTV } = this.state;
        return (
            <div className="im-a-parent" onClick={this.handleTurnOnTV}> 
                {this.renderChannel()}
                <hr />
                <button 
                    disabled={shouldTurnOffTV}
                    className="im-a-child-button" 
                    onClick={this.handleChangeChannel}
                >
                    Change Channel
                </button>
            </div>
        );
    }

}

export default TV;
```

```javascript
import React, { Fragment, useState } from "react";

import "./TV.css" // vous pouvez ignorer cela puisque cela n'existera pas de votre côté

const TV = () => {
    const [channel, setChannel] = useState(1);
    const [shouldTurnOffTV, setTurnOffTV] = useState(false);

    // le div parent déclenché si la TV est éteinte
    // cliquer sur changer de chaîne ou éteindre la TV ne se déclenchera pas en même temps  
    // à cause de event.stopPropagation() ici
    const handleTurnOnTV = (event) => {
        console.log("In HandleTurnOnTV");

        if (shouldTurnOffTV) {
            event.stopPropagation();

            // Je réinitialise la chaîne à 1, mais vous pouvez faire ce que vous voulez ici
            setTurnOffTV(false);
            setChannel(1);
        }
    }

    // le bouton de changement de chaîne enfant déclenché si la TV est allumée
    // cliquer sur le div parent, ou éteindre la TV ne se déclenchera pas en même temps  
    // à cause de event.stopPropagation() ici
    const handleChangeChannel = (event) => {
        console.log("In HandleChangeChannel");

        if (!shouldTurnOffTV) {
            event.stopPropagation();

            // J'augmente la chaîne de 1, mais vous pouvez faire ce que vous voulez ici
            setChannel(channel + 1);
        }
    }

    // le bouton d'extinction de la TV est déclenché
    // cliquer sur le div parent ou changer de chaîne ne se déclenchera pas en même temps 
    // à cause de event.stopPropagation() ici
    const handleTurnOffTV = (event) => {
        console.log("In HandleTurnOffTV");

        event.stopPropagation();

        setTurnOffTV(true);
    }

    const renderChannel = () => {
        if (shouldTurnOffTV) {
            return (
                <div>That's it, no more TV time!</div>
            )
        }

        return (
            <Fragment>
                <div>Current Channel: {channel}</div>
                <button className="im-a-child-button" onClick={handleTurnOffTV}>Turn Off TV</button>
            </Fragment>
        )
    }

    return (
        <div className="im-a-parent" onClick={handleTurnOnTV}> 
            {renderChannel()}
            <hr />
            <button 
                disabled={shouldTurnOffTV}
                className="im-a-child-button" 
                onClick={handleChangeChannel}
            >
                Change Channel
            </button>
        </div>
    );

}

export default TV;
```

🤔 Et voici ce qui se passe lorsque nous exécutons le code :

<iframe src="https://giphy.com/embed/WsHmCK3B52FzQkl80s" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 

1. Lorsque nous cliquons sur `Change Channel`, la chaîne est augmentée. Remarquez que les deux autres gestionnaires d'événements ne s'exécutent pas.
2. Lorsque nous cliquons sur `Turn Off TV`, l'interface utilisateur change et si nous essayons de cliquer n'importe où à l'extérieur du div parent, les deux autres gestionnaires d'événements ne s'exécutent pas.
3. Lorsque nous cliquons à l'intérieur du div parent extérieur lorsque la TV est éteinte, un seul gestionnaire d'événement est exécuté.

Veuillez noter : Dans mon exemple ci-dessus, j'utilise `state = {}` au lieu de `constructor(){...}`. C'est parce que lorsque `Babel` (un compilateur JavaScript) convertit votre code React, il génère un `constructor` avec tout à l'intérieur. Si vous savez cela, n'hésitez pas à ignorer l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-27.png)
_Capture d'écran par Mariya Diminsky prise de [Babel](https://babeljs.io/" rel="noopener)_

### Une solution encore plus simple

Donc, c'est une façon de procéder — mais il existe une solution encore plus simple !

Vérifiez simplement à l'intérieur du gestionnaire d'événement si la `target` (ce qui a été cliqué) est la même que l'`eventTarget` (le gestionnaire d'événement écoutant l'événement).

Si c'est la même chose, alors vous pouvez simplement appeler `stopPropagation`. Voici un exemple rapide ci-dessous :

```javascript
...

const Modal = ({ header, content, cancelButtonText, confirmButtonText, history, handleConfirm }) => {
    const handleCancel = (event) => {
        stopEventPropagationTry(event);

        // faire quelque chose ici
    }

    const handleConfirmButton = (event) => {
        stopEventPropagationTry(event);

        // faire quelque chose ici
    }
    
    // pour que les éléments avec plusieurs gestionnaires d'événements ne soient pas appelés
    // inutilement plus d'une fois (c'est-à-dire la remontée SyntheticEvent)
    export const stopEventPropagationTry = (event) => {
        if (event.target === event.currentTarget) {
            event.stopPropagation();
        }
    }

    return createPortal(
        <div onClick={handleCancel} className="ui dimmer modals visible active">
            <div className="ui tiny modal visible active">
                <div className="header">{header}</div>
                <div className="content">{content}</div>
                <div className="actions">
                    <button onClick={handleCancel} className="ui button">{cancelButtonText}</button>
                    <button onClick={handleConfirmButton} className="ui red button">{confirmButtonText}</button>
                </div>
            </div>
        </div>,
        document.getElementById("modal")
    );
}
```

## Vous l'avez fait ! ✨🎉✨

Vous avez parcouru cet article et maintenant, espérons-le, vous comprenez la remontée d'événements et la capture d'événements comme un pro. Hourra !

<iframe src="https://giphy.com/embed/SVs0cQ0nLRsLNUadmn" width="100%" height="451" frameBorder="0" class="giphy-embed" allowFullScreen></iframe> 

Maintenant, vous savez :

* Ce que signifie la délégation d'événements et comment fonctionnent la remontée d'événements et la capture d'événements.
* Comment la propagation des événements fonctionne différemment en JavaScript et React.
* Vous avez une meilleure compréhension des avantages et des inconvénients de la gestion des événements dans React.
* Plusieurs méthodes que vous pouvez utiliser pour corriger les problèmes qui peuvent survenir pour votre cas particulier.
* La différence entre `Event.target` et `Event.currentTarget` ainsi que le fait que l'événement déclenché n'est pas toujours le même que celui auquel le gestionnaire d'événement est attaché.
* Comment la propagation des événements se produit dans le JavaScript moderne et comment utiliser le paramètre `useCapture` si vous avez besoin d'utiliser la phase de capture.
* Vous avez appris que tous les événements ne remontent pas en JavaScript natif ainsi que certains de leurs alias qui remontent.
* Vous avez également appris que presque tous les SyntheticEvents de React (à l'exception de certaines mises à jour dans React Version 17) remontent.
* Enfin, vous avez maintenant une meilleure compréhension de la manière de gérer le cas particulier où un parent extérieur doit se déclencher sans arrêter les autres gestionnaires d'événements en utilisant l'état de React.

### Plus de ressources / Lectures complémentaires :

* [https://www.youtube.com/watch?v=Q6HAJ6bz7bY](https://www.youtube.com/watch?v=Q6HAJ6bz7bY)
* [https://javascript.info/bubbling-and-capturing](https://javascript.info/bubbling-and-capturing)
* [https://www.w3.org/TR/uievents/](https://www.w3.org/TR/uievents/)
* [https://chrisrng.svbtle.com/event-propagation-and-event-delegation](https://chrisrng.svbtle.com/event-propagation-and-event-delegation)
* [https://jsbin.com/hilome/edit?js,output](https://jsbin.com/hilome/edit?js,output)

👋🏻 Bonjour ! 👩🏻‍💻 Je suis Mariya Diminsky, une ingénieure logicielle autodidacte passionnée. J'ai travaillé comme ingénieure full stack, développeuse frontend (j'❤️ React), et développeuse Unity/C#. Je suis également la fondatrice de [TrinityMoon Studios](https://trinitymoonstudios.com/) et créatrice de [The Girl Who Knew Time](https://play.google.com/store/apps/details?id=com.trinitymoonstudios.thegirlwhoknewtime).

✨🧠 Si vous avez apprécié la lecture et que vous souhaitez en apprendre davantage sur divers sujets React/Conception de systèmes et plus encore, envisagez de suivre pour obtenir les dernières mises à jour. 🎉