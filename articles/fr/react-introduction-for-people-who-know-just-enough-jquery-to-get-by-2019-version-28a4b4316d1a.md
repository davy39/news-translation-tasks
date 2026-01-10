---
title: Une introduction à React (pour les personnes qui connaissent juste assez jQuery
  pour s'en sortir)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T17:32:37.000Z'
originalURL: https://freecodecamp.org/news/react-introduction-for-people-who-know-just-enough-jquery-to-get-by-2019-version-28a4b4316d1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FQnrGf3EajRiFzTH528w7w.png
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Une introduction à React (pour les personnes qui connaissent juste assez
  jQuery pour s'en sortir)
seo_desc: 'By Julien Benchetrit

  Back in 2015, @chibicode’s “React.js Introduction For People Who Know Just Enough
  jQuery To Get By” was my first contact with React and the tutorial that demystified
  the whole thing for me.

  It walks you through the fundamentals o...'
---

Par Julien Benchetrit

En 2015, le tutoriel « [React.js Introduction For People Who Know Just Enough jQuery To Get By](https://chibicode.com/react-js-introduction-for-people-who-know-just-enough-jquery-to-get-by/) » de [@chibicode](https://twitter.com/chibicode) a été mon premier contact avec React et le tutoriel qui a démystifié tout cela pour moi.

Il vous guide à travers les fondamentaux de React de manière méticuleuse et est particulièrement bien adapté pour toute personne venant du monde de jQuery.

Malheureusement, en essayant de le partager récemment, j'ai réalisé qu'il utilisait l'API `createClass` de React, désormais obsolète, et que les images et les exemples de code intégrés ne chargeaient plus.

Avec la permission de [@chibicode](https://twitter.com/chibicode), j'ai donc réécrit son article en tenant compte des dernières versions de React et de JavaScript, et j'ai développé certaines des explications.

Veuillez noter cependant que la grande majorité de ce tutoriel est son travail. J'espère qu'il vous sera aussi utile qu'il l'a été pour moi.

Sans plus attendre, apprenons React !

> **Petit avertissement** : Certaines des images proviennent de l'article original de [@chibicode](https://twitter.com/chibicode) et le code qu'elles montrent est légèrement différent du code que nous utilisons ici. Les images sont à titre illustratif uniquement. Référez-vous toujours aux exemples de code écrits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FQnrGf3EajRiFzTH528w7w.png align="left")

#### Public cible : Les personnes qui connaissent juste assez jQuery pour s'en sortir

Avant de commencer, je souhaite clarifier qui est le public cible.

Zed Shaw, l'auteur de la série « [Learn Code the Hard Way](https://learncodethehardway.org/) », a écrit un excellent article de blog intitulé [Early vs. Beginning Coders](https://zedshaw.com/2015/06/16/early-vs-beginning-coders/). Dans son article, Zed critique les éducateurs en programmation qui prétendent que leurs matériaux sont pour les « débutants », mais qui en réalité sont incompréhensibles pour la plupart des « vrais » débutants.

Je ne veux pas faire la même erreur ici. Parmi les personnes qui n'ont jamais essayé React, certaines sont à l'aise avec les frameworks JS frontend comme [Backbone](http://backbonejs.org/), [Ember](https://emberjs.com/) ou [Angular](https://angular.io/). Certaines connaissent bien JavaScript. D'autres connaissent juste assez jQuery pour s'en sortir. Un tutoriel qui est efficace pour un groupe peut ne pas être optimal pour les autres groupes.

Dans ce tutoriel, je cible le troisième groupe que j'ai mentionné : **les personnes qui connaissent juste assez jQuery pour s'en sortir**. Voici quelques exemples de personnes qui pourraient correspondre à cette catégorie :

* Les designers qui peuvent faire du codage de base en HTML/CSS/jQuery.

* Les développeurs WordPress qui savent comment utiliser les plugins jQuery.

* Les développeurs débutants qui ont terminé des tutoriels en ligne de base HTML/CSS/JS.

* Les développeurs backend qui s'appuient sur Bootstrap et jQuery de base pour leurs besoins frontend.

* Toute personne qui fait plus de copier-coller que d'architecture en ce qui concerne JavaScript.

**Si vous êtes à l'aise avec JavaScript ou l'un des frameworks frontend comme Backbone/Ember/Angular, ce tutoriel n'est PAS pour vous**, et vous serez très frustré par mon style d'écriture. Il existe de nombreux excellents tutoriels que vous pouvez suivre, y compris le [tutoriel officiel de React](https://reactjs.org/tutorial/tutorial.html).

De plus, **si vous connaissez déjà React**, vous serez également assez mécontent de moi car je parlerai principalement de **state** au lieu d'immuabilité ou de composants. Cependant, j'ai trouvé que l'enseignement de l'état en premier est le meilleur moyen pour les développeurs jQuery de voir pourquoi React est supérieur.

En tout cas, commençons !

### Estimation du temps : 1 ~ 2 heures

Si vous allez très vite (et copiez-collez le code d'exemple au lieu de le taper), ce tutoriel devrait prendre un peu plus d'une heure. Si vous prenez votre temps, cela devrait prendre un peu plus de 2 heures.

#### Si vous êtes bloqué

Si vous êtes bloqué ou avez des questions, vous pouvez tweeter à l'auteur original [@chibicode](https://twitter.com/chibicode) ou à moi [@julienbenc](https://twitter.com/julienbenc).

### Aperçu : Nous allons construire une « Tweet Box »

De nombreux tutoriels React commencent par expliquer comment React fonctionne ou pourquoi React est génial. Ce tutoriel ne le fait pas.

Au lieu de cela, nous allons directement construire une interface utilisateur simple, en alternant entre les implémentations jQuery et React, en expliquant les différences en cours de route. Je crois que vous réfléchirez davantage de cette manière plutôt qu'en tapant simplement des exemples.

L'interface utilisateur que nous allons construire ressemblera à la boîte de Tweet que vous trouvez sur [Twitter](https://twitter.com/). Elle ne sera pas exactement comme la vraie boîte de Tweet, mais elle sera assez similaire. Espérons que vous trouverez cet exemple pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R8wu8o8n48hwUQMaQ2Atlg.png align="left")

### Étape 1 : Introduction à CodePen (5–10 minutes)

Nous allons utiliser [CodePen](https://codepen.io/), un éditeur de code en ligne qui supporte à la fois le code jQuery et React. Vous êtes peut-être familier avec des services similaires comme [JSBin](https://jsbin.com) ou [JSFiddle](https://jsfiddle.net/) — ils sont tous assez similaires, mais j'ai choisi CodePen pour son intégration plus facile.

Voici un exemple de Pen :

%[https://codepen.io/julienben/pen/XoYQyj]

Cliquez sur « Run Pen » pour voir ce qui se passe lorsque le code est exécuté ainsi que le code lui-même (en cliquant sur le bouton `HTML`).

Ensuite, cliquez sur « Edit on CodePen » pour ouvrir le Pen dans une nouvelle fenêtre. **Vous pouvez maintenant modifier le HTML en haut à gauche** — c'est-à-dire changer le texte du bouton. Vous verrez les modifications apparaître dans la moitié inférieure de la fenêtre. C'est ainsi que fonctionne CodePen.

#### Créer un compte CodePen

Sauf si vous avez déjà un compte CodePen, **rendez-vous sur** [https://codepen.io/](https://codepen.io/) **pour créer un compte**. Cliquez sur **Sign Up** pour créer votre compte.

Après avoir créé un compte, vous pouvez **forker** des Pens publics vers votre compte. Plus ou moins la même chose que de forker un dépôt GitHub dans votre compte.

Essayons. **Ouvrez ce Pen suivant dans un nouvel onglet et cliquez sur « Fork » dans le menu en haut à droite.**

%[https://codepen.io/julienben/pen/XoYQyj]

Une fois que vous êtes sur le Pen, vous pouvez importer des bibliothèques open-source populaires. Vous faites cela en ouvrant les paramètres et en vous rendant dans les onglets CSS ou JavaScript où vous pouvez ensuite rechercher la bibliothèque que vous souhaitez ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fhlnejWv3z1PLhdbsyWjPg.png align="left")

*Paramètres CSS dans CodePen*

**Essayez de faire ce qui suit dans votre Pen forké :**

* Ajoutez le dernier Bootstrap depuis l'onglet CSS (le nom sera « twitter-bootstrap »)

* Ajoutez les classes `btn btn-primary` sur la balise `<button>`

Et le résultat devient un peu plus joli :

%[https://codepen.io/julienben/pen/dwKEWg]

#### Créer une Tweet Box

Vous semblez être assez à l'aise avec CodePen maintenant. Très bien, construisons une Tweet box. Toujours sur le même Pen que précédemment, **modifiez le HTML à l'intérieur** de `<body>` comme ceci :

```html
<div class="card bg-light">
  <div class="card-body text-right">
    <textarea class="form-control"></textarea>
    <br/>
    <button class="btn btn-primary">Tweet</button>
  </div>
</div>
```

Nous utilisons des classes Bootstrap comme `form-control`, `card`, `card-body`, etc., mais celles-ci ne sont que pour l'apparence et sans importance pour le tutoriel. Voici le résultat :

%[https://codepen.io/julienben/pen/jXKgZo]

C'est tout pour la première étape ! Pas trop mal, hein ?

### Étape 2 : Implémenter la première fonctionnalité — Le bouton Tweet doit être initialement désactivé (5 minutes)

Maintenant, il est temps pour un peu de JS. Nous allons d'abord implémenter la fonctionnalité suivante :

**Fonctionnalité 1** : le bouton « Tweet » doit être initialement désactivé. Lorsqu'il y a au moins un caractère dans le champ de texte, le bouton « Tweet » doit être activé.

Voici le Pen de démonstration. Comme vous pouvez le voir, le bouton est initialement désactivé. Si vous tapez quelque chose dans la zone de texte, le bouton devient activé.

%[https://codepen.io/julienben/pen/gZKVjd]

Pour que cela fonctionne, vous devez d'abord ajouter jQuery dans le Pen. Faites cela dans l'onglet JavaScript des paramètres de votre Pen. (Si vous avez des difficultés avec cette étape, consultez les [instructions officielles](https://blog.codepen.io/documentation/editor/using-javascript-libraries/) de CodePen.) **Une fois que c'est fait, allez dans la petite fenêtre JavaScript et ajoutez le code jQuery suivant.**

```js
// Désactiver initialement le bouton
$("button").prop("disabled", true);
// Lorsque la valeur de la zone de texte change...
$("textarea").on("input", function() {
  // Si il y a au moins un caractère...
  if ($(this).val().length > 0) {
    // Activer le bouton.
    $("button").prop("disabled", false);
  } else {
    // Sinon, désactiver le bouton.
    $("button").prop("disabled", true);
  }
});
```

#### Explication

* J'ai utilisé les noms de balises `button` et `textarea` comme sélecteurs — pas besoin d'ajouter des IDs ou des classes pour cet exemple.

* Pour activer/désactiver le bouton, utilisez `$(...).prop("disabled", ...)`.

* Pour écouter les changements dans `textarea`, utilisez l'événement `input` qui fonctionne sur les navigateurs modernes.

**Essayez-le** en tapant du texte dans la boîte de Tweet et en voyant l'état activé/désactivé du bouton changer.

NE PAS CONTINUER si cet exemple vous a semblé confus — vous devrez peut-être apprendre un peu plus de jQuery avant de passer à React. Il existe de nombreuses ressources d'apprentissage excellentes comme [Codecademy](https://www.codecademy.com), [Treehouse](https://teamtreehouse.com/), [Code School](https://www.pluralsight.com/codeschool), et d'autres.

Maintenant que cette fonctionnalité est complète, nous allons essayer de réimplémenter la même chose en utilisant React. Cela prendra plusieurs étapes.

### Étape 3 : La Tweet Box en utilisant React (5–10 minutes)

L'une des premières choses que vous remarquerez dans React est que **vous allez écrire du balisage en JS, et non en HTML**.

Permettez-moi de vous montrer ce que je veux dire. Voici le code React qui affiche la même Tweet box.

#### ATTENTION ! Vous n'avez pas besoin de suivre encore — lisez simplement le code.

%[https://codepen.io/julienben/pen/majbMg]

Quelques observations :

* À l'intérieur de `return (...)` se trouve du code de type HTML, et non du JavaScript. Dans React, vous écriverez dans une syntaxe spéciale appelée JSX qui vous permet de mettre du code de type HTML à l'intérieur de JavaScript.

* Je dis HTML-« like » car ce n'est pas identique à HTML. Remarquez qu'il utilise `className` au lieu de `class` — mais c'est assez similaire, donc vous l'apprendrez rapidement.

* Votre navigateur ne comprend pas JSX donc, avant que le code puisse être exécuté, il est automatiquement converti en JavaScript compatible avec le navigateur par un compilateur JS (appelé Babel).

* Le code HTML à l'intérieur de `return (...)` est pratiquement identique au code HTML de l'étape 1.

* Regardez le code HTML restant dans notre Pen et vous verrez qu'il n'y a pas de balisage en dehors de `<body><div id="container">&`lt;/div&gt;. C'est ce que je **voulais dire quand j'ai dit que dans React vous allez écrire du balisage en JavaScript** (JSX) et non en HTML.

#### Questions Fréquemment Posées & Réponses

**Question** : Que font `class TweetBox extends React.Component` et `ReactDOM.render` ? Dois-je les comprendre maintenant ?

**Réponse** : Ne vous en souciez pas pour l'instant. En gros, le premier déclare un composant React avec un nom (dans ce cas, `TweetBox`). Celui-ci est ensuite rendu dans le DOM via `ReactDOM.render(<TweetBox />, document.getElementById("contai`ner")) — ce qui signifie que ce composant est ajouté à l'intérieur de la balise <div id="co`ntainer"&gt;. C'est tout ce que vous devez savoir pour l'instant.

**Question** : Dois-je faire quelque chose de spécial pour écrire du JSX sur ma machine locale ?

**Réponse** : Oui, mais cela dépasse le cadre de ce tutoriel — en bref, vous devez activer quelque chose appelé compilation Babel. Tout ce que vous devez faire pour écrire du JSX sur CodePen est (1) ajouter les bibliothèques React et ReactDOM et (2) sélectionner « Babel » dans la liste des préprocesseurs JavaScript dans la fenêtre des paramètres JS.

**Question** : N'est-il pas mauvais de écrire du balisage (HTML) et du comportement (JS) au même endroit ?

**Réponse** : Cela peut être une mauvaise pratique pour les pages web simples, mais pas nécessairement pour les grandes applications web. Dans les grandes applications web, il y aura des centaines de morceaux d'interface utilisateur, chacun contenant leur propre balisage et comportements. Le code sera plus gérable si le balisage et les comportements sont conservés ensemble pour chaque morceau d'interface utilisateur, plutôt que de conserver « tout le balisage » ensemble et « tous les comportements » ensemble. Et React est conçu pour développer de grandes applications web. En fait, React est développé et utilisé par Facebook, l'une des plus grandes applications web.

Ensuite, je vais vous montrer comment écrire le code React ci-dessus étape par étape.

### Étape 4 : Écrire votre premier code React (5–10 minutes)

Voici un Pen de départ. Dans celui-ci, j'ai importé Bootstrap (la partie CSS) et React. J'ai également défini le préprocesseur JavaScript sur Babel afin que nous puissions écrire des classes et du JSX.

**Veuillez essayer de suivre. Pour commencer, forkez ce Pen afin de pouvoir éditer et sauvegarder au fur et à mesure.**

%[https://codepen.io/julienben/pen/YdjeWj]

Maintenant, vous êtes prêt à écrire du React. **Essayez de suivre et tapez les extraits de code JS suivants** dans votre Pen.

```js
class TweetBox extends React.Component {
  render() {
    return null;
  }
};
```

C'est le modèle pour créer une partie de l'interface utilisateur avec React (dans ce cas, une boîte de tweet). C'est aussi essentiel que `$(selector).append('votre code HTML ou élément')` dans jQuery.

Pour construire réellement l'interface utilisateur, nous devons écrire la méthode `render()`. Pour l'instant, gardons cela simple avec une seule balise `div`.

```js
class TweetBox extends React.Component {
  render() {
    return (
      <div>
        Hello World!
      </div>
    );
  }
};
```

Comme dans l'exemple ci-dessus, **mettez une paire de parenthèses après** `return`, et écrivez le balisage à l'intérieur.

#### Pièges de JSX

Il y a une chose que vous devez retenir avec JSX — dans `render()`, vous devez retourner seulement **une** balise extérieure (ou tout ce qui peut être considéré comme un nœud DOM valide tel qu'une chaîne ou une chaîne).

Cela fonctionnera car c'est une chaîne :

```javascript
return 'Hello World!';
```

Mais ce qui suit ne fonctionnera pas car il n'y a pas de guillemets ou de balise extérieure autour du texte :

```js
return (
  Hello World!
);
```

Cela ne fonctionne pas non plus car il y a deux balises extérieures (`span`) à l'intérieur de `return (...)` :

```js
return (
  <span>
    Hello
  </span>
  <span>
    World
  </span>
);
```

Pour l'exemple ci-dessus, la solution est de créer une balise `div` supplémentaire pour envelopper les deux balises `span`.

```js
return (
  <div>
    <span>
      Hello
    </span>
    <span>
      World
    </span>
  </div>
);
```

Nous avons utilisé une `div` ici, mais dans les versions les plus récentes de React, vous pouvez utiliser la fonctionnalité Fragment pour rendre plusieurs balises extérieures. Comme ceci :

```js
return (
  <React.Fragment>
    <span>
      Hello
    </span>
    <span>
      World
    </span>
  </React.Fragment>
);
```

#### Attacher l'interface utilisateur au DOM

Maintenant, nous devons « attacher » cette interface utilisateur au DOM afin de voir `Hello World`. Pour ce faire, **ajoutez** `ReactDOM.render()` sous le code que nous venons d'écrire :

```js
class TweetBox extends React.Component {
  ...
};
ReactDOM.render(
  <TweetBox />,
  document.getElementById("container")
);
```

(**Note** : une ellipsis (…) dans l'extrait de code indique du code qui a été omis pour plus de clarté. En d'autres termes, ne touchez pas à cette partie du code et laissez-la telle quelle.)

`ReactDOM.render` prend deux arguments. Le premier argument est le composant React, qui est `<VariableName` /&gt;. Le second argument est l'élément DOM où nous voulons rendre (dans ce `cas, document.getElementById('conta`iner')). Ensemble, le code ci-dessus rend l'UI de Tw`eetBox i`nside <div id="co`ntainer"&gt;.

Maintenant, vous devriez voir `Hello World` apparaître dans votre Pen. Félicitations, vous avez écrit et rendu votre premier composant React !

#### Écrire le HTML réel pour la Tweet Box

Maintenant, au lieu de `Hello World`, nous allons implémenter le HTML pour la Tweet Box. **Remplacez le code à l'intérieur** de `render()` par ceci :

```js
return (
  <div className="card bg-light">
    <div className="card-body text-right">
      <textarea className="form-control" />
      <br />
      <button className="btn btn-primary">Tweet</button>
    </div>
  </div>
);
```

Il y a deux choses auxquelles vous devez faire attention :

* **N'utilisez pas** `class`. Utilisez plutôt `className`. C'est parce que JSX est traduit en JS et `class` est un mot réservé en JS.

* **Si vous utilisez** `<`br&gt; inste`ad de`  
, vous obtiendrez une erreur. Assurez-vous de fermer toutes les balises. Même chose avec les images : <img src`\="" alt="" /&gt;

Tout le reste devrait être identique à l'exemple jQuery précédent.

Si vous avez tapé cela correctement, alors vous devriez voir la boîte de Tweet dans votre Pen. **Si rien n'apparaît dans la sortie, vérifiez votre code très soigneusement pour vous assurer qu'il n'y a pas de fautes de frappe.**

C'est tout pour cette étape ! Voici le Pen jusqu'à cette partie :

%[https://codepen.io/julienben/pen/majbMg]

### Étape 5 : Réimplémenter la première fonctionnalité — Le bouton Tweet doit être initialement désactivé — en React (5–10 minutes)

Nous allons réimplémenter avec React la première fonctionnalité que nous avons implémentée en utilisant jQuery :

**Fonctionnalité 1** : Le bouton « Tweet » doit être initialement désactivé. Lorsqu'il y a au moins un caractère dans le champ de texte, le bouton « Tweet » doit être activé.

Voici le code jQuery que nous avons écrit :

%[https://codepen.io/julienben/pen/gZKVjd]

Voyons comment nous pouvons faire cela en React.

**Commencez avec votre Pen de l'étape précédente.** (**Astuce** : Puisque vous ne toucherez pas au HTML dans React, **vous pouvez minimiser l'onglet HTML sur CodePen** pour obtenir plus d'espace à l'écran. Même chose avec l'onglet CSS.)

**Tout d'abord, désactivons le bouton en ajoutant** `disabled` comme attribut.

```js
render() {
  return (
    ...
    <button className="..." disabled>Tweet</button>
    ...
  );
}
```

En JSX, cela équivaut à écrire `disabled={true}`.

Le bouton devrait maintenant être désactivé. Notez que dans notre implémentation jQuery, nous avons écrit :

```js
$("button").prop("disabled", true);
```

pour désactiver initialement le bouton, mais nous aurions pu modifier la balise du bouton comme ci-dessus.

Maintenant, nous devons activer le bouton lorsqu'il y a au moins un caractère dans le champ de texte.

#### Gérer l'événement de changement

Tout d'abord, nous devons écouter l'utilisateur tapant dans le `textarea`. Dans notre implémentation jQuery, nous avons écrit :

```js
$("textarea").on("input", function() {
  ...
}
```

Dans le monde React, nous écrivons le gestionnaire d'événements comme une **méthode de classe**. Appelons-la `handleChange` :

```js
class TweetBox extends React.Component {
  handleChange = () => {
  };
  render() {
    ...
  }
}
```

> Notez que nous utilisons une fonction fléchée afin de pouvoir accéder au contexte de la classe (`this`) sans avoir à lier la fonction dans le `constructor`. Expliquer cela en profondeur dépasse le cadre de ce tutoriel, mais vous apprendrez très probablement cela en temps voulu.

Ensuite, nous appelons ce gestionnaire lorsque du texte est saisi. Pour ce faire, **modifiez la** balise `textarea` dans `render()` comme ceci :

```html
<textarea className="form-control" onChange={this.handleChange}>
</textarea>
```

* Nous avons utilisé l'événement `input` pour jQuery, mais dans React, nous utilisons `onChange` — vous apprendrez comment les événements diffèrent dans le JSX de React à partir de la documentation officielle de React, donc ne vous inquiétez pas trop pour l'instant.

* **Plus important encore**, nous avons utilisé des accolades pour inclure du code JavaScript à l'intérieur de la partie syntaxe HTML de JSX. Dans ce cas, nous avons passé le gestionnaire `handleChange` et nous l'avons précédé de `this` car c'est une méthode de classe.

* Si vous êtes habitué à jQuery, cela peut sembler être une mauvaise pratique, mais ne vous inquiétez pas. Encore une fois, dans les grandes applications, le code sera plus gérable si le balisage et les comportements sont conservés ensemble pour chaque morceau d'interface utilisateur.

Pour vous assurer que le gestionnaire est bien appelé, **ajoutons** `console.log` à l'intérieur de `handleChange` :

```js
handleChange = (e) => {
  console.log(e.target.value);
};
```

L'objet `event` (surnommé `e`) contient `target` qui est le `textarea`. Nous obtenons la `value` pour afficher le contenu actuel du `textarea`.

**Dans votre Pen, ouvrez l'** onglet `console` (avec le bouton en bas à gauche de l'écran) pour vérifier la sortie. Ensuite, tapez quelque chose dans la boîte de Tweet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8mSEfP4wqKBTHRGLaR64_Q.png align="left")

*Le bouton de la console dans CodePen*

Vous pouvez également l'essayer ici (vous devrez ouvrir le Pen dans un nouvel onglet pour voir le bouton `console`) :

%[https://codepen.io/julienben/pen/aPaoOJ]

C'est tout pour cette étape ! Nous terminerons cette fonctionnalité à l'étape suivante.

**NOTE : Fermez l'** onglet `console` dans CodePen lorsque vous avez terminé. Nous n'en avons plus besoin.

### Étape 6 : Implémentation de l'état (10–15 minutes)

Je vais maintenant expliquer l'une des plus grandes différences entre le code de style jQuery et le code de style React.

Dans jQuery, lorsqu'un événement se produit, vous modifiez généralement le DOM directement (comme nous l'avons fait précédemment avec `$("button").prop("disabled", true)`) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*IhZHTYtjhRnTru2C align="left")

Dans React, **vous ne modifiez jamais le DOM directement.** Au lieu de cela, dans un gestionnaire d'événements, vous modifiez quelque chose appelé **l'« état du composant »**. Et cela se fait en appelant `this.setState`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vB6BPnDRykxd2PFP align="left")

Ensuite, chaque fois que l'`état` est mis à jour, **`render()` est appelé à nouveau.** Et **à l'intérieur** de `render()`, vous pouvez accéder à l'état pour dire à React comment vous voulez que le DOM soit modifié.

![Image](https://cdn-media-1.freecodecamp.org/images/0*g9bDPyxJef0yg00Y align="left")

C'est ainsi que vous mettez à jour l'interface utilisateur en réponse à un événement. Oui, c'est déroutant au début, alors laissez-moi expliquer avec du code.

#### Écrire le gestionnaire d'événements

**Commencez avec votre Pen de l'étape précédente.** Tout d'abord, nous devons **initialiser l'objet d'état.** Nous pouvons le faire à l'intérieur du `constructeur` de la classe.

Qu'est-ce qui va dans l'objet ? **Créons une seule clé appelée** `text` et faisons-la stocker ce qui se trouve dans la boîte de Tweet.

```js
class TweetBox extends React.Component {
  constructor(props) {
    super(props);
 
    this.state = {
      text: '',
    };
  }
  
  handleChange = (e) => {...};
  render() {...}
};
```

> Ne vous inquiétez pas de pourquoi nous appelons `super(props)` en haut de notre `constructeur`. C'est une étape importante mais pas nécessaire pour comprendre React pour l'instant.

**Ensuite, nous allons modifier le gestionnaire d'événements** pour définir le champ `text` de l'état sur ce qui se trouve actuellement dans le `textarea`. Pour ce faire, **nous utilisons une méthode spéciale appelée** `setState` et passons la paire clé-valeur mise à jour.

```js
handleChange = (e) => {
  this.setState({ text: e.target.value });
};
```

Maintenant, vérifions que l'état est correctement défini en écrivant du code de débogage dans `render()`.

Pour ce faire, **ajoutez simplement** `this.state.text` près de la fin de `render()` et utilisez des accolades pour utiliser le code JS à l'intérieur de la partie syntaxe HTML de JSX.

```js
render() {
  return (
    <div className="card bg-light">
      ...
      {this.state.text}
    </div>
  );
}
```

**Maintenant, essayez d'entrer du texte dans la boîte de Tweet.** Le même texte devrait apparaître sous le bouton.

Vous pouvez également l'essayer sur le Pen ci-dessous :

%[https://codepen.io/julienben/pen/XoPrzR]

Maintenant, le diagramme précédent pourrait avoir plus de sens pour vous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*8hdVUZaiVqm8J2mq align="left")

#### Supprimer le code de débogage

Une fois que vous avez confirmé que l'état est correctement défini, **supprimez le code de débogage que nous venons d'ajouter :**

```javascript
{this.state.text}
```

#### Activation/Désactivation du bouton

Maintenant que nous pouvons écouter les changements de texte, l'étape suivante consiste à activer/désactiver le `button` en fonction du fait que le `text` est vide ou non.

En utilisant le `state`, nous pouvons utiliser cette logique :

* Si `this.state.text.length === 0`, le bouton doit être désactivé.

Pour ce faire dans React, **ajoutez l'** attribut `disabled` et définissez sa valeur comme la sortie de `this.state.text.length === 0`. Puisque c'est du code JS, vous devez l'envelopper avec `{}`.

```html
<button className="btn btn-primary" disabled={this.state.text.length === 0}>Tweet</button>
```

Si vous écrivez `disabled="true"` ou `disabled="false"` en HTML brut, cela ne fonctionnera pas — en HTML brut, vous devez ajouter/supprimer l'attribut `disabled` pour activer le `button`. Mais React n'est **pas** du HTML brut — il fait ce qui suit en coulisses :

* Si vous écrivez `disabled={true}` en JSX, cela se convertit en `<button disabl`ed&gt; en HTML.

* Si vous écrivez `disabled={false}` en JSX, l'attribut `disabled` est supprimé de la balise `button` en HTML.

Cela fonctionne avec d'autres attributs booléens comme `checked`. (Vous pouvez en lire plus sur cet aspect de JSX [ici](https://reactjs.org/docs/dom-elements.html).)

Le Pen résultant est ci-dessous :

%[https://codepen.io/julienben/pen/GPXKYa]

#### Réflexions

Encore une fois, gardez cette différence entre jQuery et React à l'esprit avant de passer à l'étape suivante :

* Dans jQuery, vous écrivez des gestionnaires d'événements qui **modifient le DOM**.

* Dans React, vous écrivez des gestionnaires d'événements qui **modifient l'état**. Et vous écrivez `render()` pour refléter l'état actuel.

### Étape 7 : Compteur de caractères restants en jQuery (5 minutes)

La prochaine fonctionnalité que nous allons implémenter est le compteur de caractères restants.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9ONPNObC5R_IeBvq align="left")

Voici les spécifications :

* Le compteur de caractères affichera `280 — la longueur du texte`.

**Nous allons d'abord implémenter cela en jQuery, puis en React.**

Nous allons commencer avec notre implémentation jQuery précédente et mettre notre code React en attente pour l'instant. **À l'avenir, je vous donnerai un nouveau code à utiliser au début de chaque chapitre**, alors que nous alternons entre jQuery et React. Cela signifie qu'après avoir terminé chaque étape, vous pouvez jouer avec le code avant de passer à l'étape suivante.

**✓ Forkez le Pen ci-dessous** pour commencer.

%[https://codepen.io/julienben/pen/gZKVjd]

Tout d'abord, **ajoutez le compteur de caractères en HTML.** Mettons-le à l'intérieur d'une balise `span` :

```js
<textarea {...}></textarea><br>
<span>280</span>
<button {...}>Tweet</button>
```

Et **à l'intérieur du gestionnaire d'entrée en JS, ajoutez ce code pour mettre à jour le compteur de caractères :**

```js
$("textarea").on("input", function() {
  $("span").text(280 - $(this).val().length);
  ...
});
```

C'est tout ! **Essayez de taper dans la boîte de Tweet** et vous verrez le compteur de caractères se mettre à jour au fur et à mesure que vous tapez. Voici le Pen :

%[https://codepen.io/julienben/pen/gZdJNJ]

### Étape 8 : Compteur de caractères restants en React (5 minutes)

Et en React ? Vous devriez essayer de le faire vous-même. Commencez avec notre implémentation React précédente.

**✓ Forkez le Pen ci-dessous** pour commencer.

%[https://codepen.io/julienben/pen/GPXKYa]

(**Astuce :** Puisque vous ne toucherez pas au HTML dans React, **vous pouvez minimiser l'onglet HTML sur CodePen** pour obtenir plus d'espace à l'écran.)

**Indices :**

* Pas besoin de changer les méthodes `constructor()` ou `handleChange()`.

* Utilisez `this.state.text.length` dans `render()`.

#### Réponse :

Ajoutez ce code après `<b`r/&gt; dans `votre re`nder() :

```html
<span>{280 - this.state.text.length}</span>
```

Voici le Pen :

%[https://codepen.io/julienben/pen/QzVXOd]

Trop facile ? Pas sûr de savoir pourquoi la construction d'interfaces utilisateur avec React est bien meilleure que jQuery ? Eh bien, l'étape suivante a plus de complexité et c'est là que React commence vraiment à briller.

### Étape 9 : Le bouton « Ajouter une photo » (5 minutes)

![Image](https://cdn-media-1.freecodecamp.org/images/0*N697jN99MCP3cfUn align="left")

Pour notre prochaine fonctionnalité, nous allons ajouter un bouton « Ajouter une photo » à la boîte de Tweet. C'est là que les choses commencent à devenir délicates.

Cependant, **nous n'écrirous pas réellement le code pour télécharger des images.** Au lieu de cela, voici ce que nous allons faire :

Lorsque vous téléchargez une photo sur Twitter, elle compte contre la limite de caractères. Lors de ma tentative, elle a diminué le nombre de caractères restants de 280 à 257.

> Oui, je sais que Twitter ne compte plus les photos contre la limite de caractères, mais nous ignorerons cela pour ce tutoriel.

Voici les spécifications :

* Créez un bouton « Ajouter une photo ».

* Cliquer sur ce bouton bascule un **état ON/OFF.**

* Si le bouton est ON, il dira `**✓ Photo Ajoutée**` et le nombre de caractères disponibles diminue de 23.

* De plus, si le bouton est ON, **même s'il n'y a pas de texte saisi, le bouton « Tweet » reste activé.**

Voici le CodePen de démonstration. **Essayez de cliquer sur le bouton « Ajouter une photo »** et voyez ce qui se passe avec le compteur de caractères et le bouton Tweet.

%[https://codepen.io/julienben/pen/roZXvE]

Implémentons cela avec jQuery d'abord.

### Étape 10 : Le bouton « Ajouter une photo » en jQuery (15–20 minutes)

Commencez avec la dernière version de notre implémentation jQuery.

**✓ Forkez le Pen ci-dessous** pour commencer.

%[https://codepen.io/julienben/pen/gZdJNJ]

Auparavant, nous attachions un gestionnaire à `$("button")` mais cela ne fonctionnera plus si nous avons deux boutons. **Modifions donc le HTML comme ceci :**

```html
...
<button class="js-tweet-button btn btn-primary" disabled>Tweet</button>
<button class="js-add-photo-button btn btn-secondary">Add Photo</button>
...
```

Voici les modifications :

* **Ajout du deuxième bouton** qui dit « Add Photo ».

* **Ajout des classes** `js-tweet-button` et `js-add-photo-button` à chaque bouton. Les noms de classe sont préfixés avec `js-` pour se souvenir qu'ils sont utilisés uniquement en JS et non en CSS.

* **Ajout de l'attribut initial** `disabled` au bouton Tweet afin de ne pas avoir à le faire en JS.

**Ensuite, réécrivez le fichier JS entier comme ceci :**

```js
$("textarea").on("input", function() {
  $("span").text(280 - $(this).val().length);
  if ($(this).val().length > 0) {
    $(".js-tweet-button").prop("disabled", false);
  } else {
    $(".js-tweet-button").prop("disabled", true);
  }
});
```

Voici les modifications :

* **(Important) Suppression** de `$("button").prop("disabled", true);` de la première ligne car nous avons ajouté l'attribut `disabled` directement au bouton Tweet.

* **Remplacement** de `$("button")` par `$(".js-tweet-button")` afin qu'il puisse être distingué de `.js-add-photo-button`.

#### Ajout du bouton

Ensuite, nous allons implémenter l'une des fonctionnalités :

* Cliquer sur le bouton « Add Photo » bascule l'état ON/OFF. **Si il est ON, le bouton dira** `✓ Photo Added`.

Pour ce faire, **ajoutons ce morceau de code :**

```js
$("textarea").on("input", function() {
  ...
});

$(".js-add-photo-button").on("click", function() {
  if ($(this).hasClass("is-on")) {
    $(this)
      .removeClass("is-on")
      .text("Add Photo");
  } else {
    $(this)
      .addClass("is-on")
      .text("✓ Photo Added");
  }
});
```

Nous utilisons la classe `is-on` pour suivre l'état. **Vérifiez que cela fonctionne** en cliquant plusieurs fois sur le bouton « Add Photo » et en voyant le texte alterner.

#### Décrémenter le compteur de caractères

Ensuite, nous allons implémenter cette fonctionnalité :

* Si le bouton « Add Photo » est ON, **le nombre de caractères disponibles diminue de 23.**

Pour ce faire, **modifiez le gestionnaire de clic que nous venons d'ajouter comme ceci.**

```js
if ($(this).hasClass("is-on")) {
  $(this)
    .removeClass("is-on")
    .text("Add Photo");
  $("span").text(280 - $("textarea").val().length);
} else {
  $(this)
    .addClass("is-on")
    .text("✓ Photo Added");
  $("span").text(280 - 23 - $("textarea").val().length);
}
```

Nous changeons le contenu de la balise `span` à chaque clic. Si le `button` est ON, nous devons soustraire la longueur du texte de `257` (c'est-à-dire `280 — 23`). Nous utilisons `280 — 23` pour la clarté pour l'instant, mais si nous construisions une application de production, nous devrions utiliser des constantes à la place.

**Vérifiez que cela fonctionne** en cliquant sur le bouton « Add Photo ».

#### Correction du gestionnaire d'entrée

Cependant, cela n'est pas complet — **si vous avez le bouton « Add Photo » ON et commencez à taper dans le** `textarea`, le compteur de caractères restants se désynchronise.

Cela se produit parce que le gestionnaire pour le `textarea` ne prend pas en compte l'état du bouton « Add Photo ».

Pour corriger cela, **nous devons mettre à jour le gestionnaire pour** `textarea` comme ceci :

```js
$("textarea").on("input", function() {
  if ($(".js-add-photo-button").hasClass("is-on")) {
    $("span").text(280 - 23 - $(this).val().length);
  } else {
    $("span").text(280 - $(this).val().length);
  }

  if (...) {
    ...
  }
});
```

**Assurez-vous que cela fonctionne** en activant le bouton « Add Photo » puis en tapant du texte.

#### Je sais que cela prend du temps...

Mais restez avec moi ! Le code jQuery ici est ***supposé*** être confus, donc ne vous inquiétez pas !

#### Implémenter la dernière fonctionnalité

La dernière fonctionnalité que nous devons implémenter est celle-ci :

* Si le bouton « Add Photo » est ON, **même s'il n'y a pas de texte saisi, le bouton « Tweet » reste activé.**

Pour ce faire, **nous devons modifier le gestionnaire de clic du bouton « Add Photo » :**

```js
$(".js-add-photo-button").on("click", function() {
  if ($(this).hasClass("is-on")) {
    ...
    if ($("textarea").val().length === 0) {
      $(".js-tweet-button").prop("disabled", true);
    }
  } else {
    ...
    $(".js-tweet-button").prop("disabled", false);
  }
});
```

Voici l'explication :

* Si le bouton « Add Photo » passe de ON à OFF (clause `if`), nous devons vérifier s'il n'y a pas de texte saisi et, si c'est le cas, désactiver le bouton « Tweet ».

* Si le bouton « Add Photo » passe de OFF à ON (clause `else`), nous activons toujours le bouton « Tweet ».

#### Mais encore une fois, c'est cassé

Nous n'avons pas encore terminé. Il y a un bug dans le code en ce moment. **Essayez-le vous-même en suivant ces étapes :**

* Activez le bouton « Add Photo ».

* Tapez du texte.

* Supprimez tout le texte.

* Le bouton « Tweet » devrait toujours être activé parce que le bouton « Add Photo » est ON, mais ce n'est pas le cas.

Cela signifie que notre gestionnaire d'entrée pour `textarea` manque une logique. Pour corriger cela, **nous devons ajouter une autre condition à l'** instruction `if` dans le gestionnaire d'entrée.

```js
$("textarea").on("input", function() {
  ...
  if ($(this).val().length > 0 || $(".js-add-photo-button").hasClass("is-on")) {
    ...
  } else {
    ...
  }
});
```

Voici l'explication de cette condition supplémentaire :

* Lorsque le texte change, **si le texte n'est pas vide OU si le bouton « Add Photo » est ON**, ne désactivez pas le bouton « Tweet ».

**Essayez à nouveau les étapes ci-dessus** et cette fois-ci, cela fonctionnera comme prévu.

### Étape 11 : Réflexion sur le code jQuery — Pourquoi si confus ? (5 minutes)

Voici le code HTML et JS final de l'étape précédente :

%[https://codepen.io/julienben/pen/YdJKqE]

**Jetez un autre coup d'œil au code jQuery.** C'est très confus. Si vous gardez le code tel quel, vous aurez probablement besoin de commentaires partout pour vous souvenir de son fonctionnement. Il y a aussi des signes évidents de duplication de code, mais vous devrez réfléchir un bon moment avant de refactoriser.

La question est : **pourquoi est-ce devenu si moche si vite ?**

La réponse a à voir avec le **style « jQuery »** de code dont nous avons parlé précédemment. Rappelez-vous ce diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/0*9p-0fEB0Z2DPuFF7 align="left")

Les choses sont simples lorsqu'il n'y a qu'un seul gestionnaire d'événements et un seul élément DOM. Cependant, comme nous venons de le voir, **si plusieurs gestionnaires d'événements modifient plusieurs parties du DOM, le code devient moche et compliqué.**

C'est un exemple de ce que les gens veulent dire lorsqu'ils parlent de « code spaghetti ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*YTtV7PD_apkzdYMw align="left")

Imaginez ajouter plus de fonctionnalités qui pourraient influencer à la fois la limite de caractères et l'état du bouton « Tweet ». Le code deviendrait encore plus difficile à gérer.

Vous pouvez, en théorie, atténuer cela en refactorisant en fonctions réutilisables. Mais vous devrez toujours réfléchir dur à chaque fois que vous ajoutez quelque chose de nouveau.

> **Note :** Quelqu'un a partagé une [version refactorisée du code jQuery](https://pastebin.com/wbGZZs7U) (pour le tutoriel original). Très propre. Vous remarquerez que la fonction `update()` gère la plupart des mises à jour du DOM en fonction de son état actuel. Les écouteurs d'événements exécutent ensuite cette fonction à chaque appel.

> De cette manière, c'est similaire au `render` de React. Cependant, il y a encore de nombreux inconvénients à cette solution. Pour commencer, l'absence d'un objet `state` réel rend la logique plus opaque. Cela ne vous permet pas non plus de décomposer votre interface utilisateur en plusieurs composants et est susceptible d'avoir des problèmes de performance à mesure que vous continuez à l'agrandir.

Maintenant, voyons à quoi cela ressemble de faire la même chose avec React.

**Spoiler alert : Ce sera beaucoup plus simple.**

### Étape 12 : Le bouton « Ajouter une photo » en React (10–20 minutes)

Commençons avec notre implémentation React précédente.

**✓ Forkez le Pen ci-dessous** pour commencer.

%[https://codepen.io/julienben/pen/QzVXOd]

#### Ajout du bouton

Tout d'abord, ajoutons le bouton « Ajouter une photo ». **Modifiez le JSX :**

```html
<button ...>Tweet</button>

<button className="btn btn-secondary">
  Add Photo
</button>
```

Maintenant, ajoutons un gestionnaire de clic à ce bouton afin que le texte change de `Add Photo` à `✓ Photo Added`. Rappelez-vous la manière React d'écrire du code :

![Image](https://cdn-media-1.freecodecamp.org/images/0*FWEJiHF2VzD8p8L2 align="left")

Nous allons :

1. **Créer une variable d'état** qui garde une trace de si le bouton « Ajouter une photo » est ON ou OFF.

2. **Utiliser l'état** dans `render()` pour décider d'afficher `Add Photo` ou `✓ Photo Added`.

3. **Mettre à jour l'état** dans le gestionnaire de clic.

Pour (1), **nous allons modifier l'état initial dans le** `constructeur` en ajoutant une paire clé-valeur pour garder une trace de si la photo est ajoutée ou non :

```js
constructor(props) {
  super(props);
 
  this.state = {
    text: '',
    photoAdded: false,
  };
}
```

Pour (2), **nous allons modifier le balisage JSX** pour le bouton « Ajouter une photo ». Nous allons faire en sorte que le bouton dise « Photo Added » si `this.state.photoAdded` est vrai. Nous pouvons simplement utiliser un [opérateur ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) ici :

```html
<button className="btn btn-secondary">
  {this.state.photoAdded ? "✓ Photo Added" : "Add Photo" }
</button>
```

Enfin, pour (3), **nous allons attacher un gestionnaire d'événements sur JSX** comme nous l'avons fait pour le `textarea` :

```html
<button className="btn btn-secondary" onClick={this.togglePhoto}>
  {this.state.photoAdded ? "✓ Photo Added" : "Add Photo" }
</button>
```

Remarquez que nous utilisons `onClick` au lieu de `onChange`. Cela est dû au fait que nous traitons avec un `button` et non un `textarea` ou un `input`.

Nous allons également **ajouter une méthode de gestionnaire qui bascule la valeur de** `this.state.photoAddded` :

```js
togglePhoto = () => {
  this.setState((prevState) => ({ photoAdded: !prevState.photoAdded }));
}
```

Cette fois, vous verrez que nous passons une fonction à `this.setState`. Cela est nécessaire si vous souhaitez mettre à jour l'état de votre composant mais avez besoin d'utiliser une valeur de l'état précédent. Pourquoi nous faisons cela dépasse le cadre de ce tutoriel, mais vous pouvez en lire plus à ce sujet dans [cette section](https://reactjs.org/docs/state-and-lifecycle.html#using-state-correctly) de la documentation officielle de React.

Maintenant, cliquer sur Ajouter une photo devrait basculer le texte du bouton. **Essayez-le vous-même.**

#### Décrémenter le compteur de caractères

Nous allons maintenant implémenter la fonctionnalité suivante :

* Si le bouton « Ajouter une photo » est ON, **le nombre de caractères disponibles diminue de 23.**

Actuellement, le nombre de caractères disponibles est affiché comme suit dans `render()` :

```javascript
<span>{280 - this.state.text.length}</span>
```

Cette valeur dépendra désormais également de `this.state.photoAdded`, nous avons donc besoin d'un `if` et d'un `else` ici.

Cependant, **en JSX, vous ne pouvez pas écrire** `if` ou `else` à l'intérieur de `{ ... }`. Vous pourriez utiliser une expression ternaire (`a ? b : c`) comme nous l'avons fait précédemment, mais cela serait assez long et difficile à lire dans ce cas.

Souvent, la solution la plus simple dans cette situation est de refactoriser une conditionnelle en une méthode. Essayons-le.

**Tout d'abord, modifiez le code ci-dessus pour utiliser une méthode de classe, comme ceci :**

```html
<span>{this.getRemainingChars()}</span>
```

**Et définissez la méthode comme ceci :**

```js
getRemainingChars = () => {
  let chars = 280 - this.state.text.length;
  if (this.state.photoAdded) chars = chars - 23;
  return chars;
}
```

Maintenant, le compteur de caractères restants devrait se mettre à jour comme prévu lorsque le bouton « Ajouter une photo » est basculé.

**Question** : Dans `render()`, pourquoi `{this.getRemainingChars()}` a-t-il `()` mais `{this.handleChange}` et `{this.togglePhoto}` n'en ont pas ?

Bonne question. Jetons un autre coup d'œil à `render()` :

```js
render() {
  return (
    ...
      <textarea className="..." onChange={this.handleChange}></textarea>
    ...
    
    <span>{this.getRemainingChars()}</span>
    ...    
          
    <button className="..." onClick={this.togglePhoto}>
      ...
    </button>
    ...
    );
  }
```

**Réponse** :

* Nous avons écrit la méthode `getRemainingChars()` pour **retourner un nombre**. Nous devons obtenir ce nombre et le mettre à l'intérieur de `<span>&`lt;/span&gt;, donc **nous devons appeler la méthode getRema`iningChars() en utilisant (). C'est pourquoi nous avons () dans getRema`iningChars().

* D'autre part, `handleChange` et `togglePhoto` sont des **gestionnaires d'événements**. Nous voulons que ces méthodes soient appelées uniquement lorsque l'utilisateur interagit avec l'interface utilisateur (en tapant dans le `textarea` ou en cliquant sur un `button`). Pour ce faire, nous devons les écrire sans `()` dans `render()` et les assigner à des attributs comme `onChange` et `onClick`. React se chargera d'attacher les méthodes aux écouteurs d'événements pertinents pour nous.

#### L'état du bouton « Tweet »

Il nous reste une fonctionnalité à implémenter :

* Si le bouton « Ajouter une photo » est ON, **même s'il n'y a pas de texte saisi, le bouton « Tweet » reste activé.**

Cela est en fait très facile grâce à React. Auparavant, l'option `disabled` du bouton Tweet était définie comme suit :

```html
<button ... disabled={this.state.text.length === 0}>...</button>
```

En d'autres termes, auparavant le bouton « Tweet » était désactivé si la longueur du texte était de 0. **Maintenant, le bouton « Tweet » est désactivé si :**

* La longueur du texte est de 0

* **ET**

* Le bouton « Ajouter une photo » est OFF.

La logique est donc la suivante :

```html
<button ... disabled={this.state.text.length === 0 && !this.state.photoAdded}>...</button>
```

Une façon de clarifier le code ci-dessus est d'utiliser `getRemainingChars()`. Si 280 caractères restent, cela signifie que le `textarea` est vide et que le bouton « Ajouter une photo » est OFF, donc le bouton « Tweet » doit être désactivé.

```html
<button ... disabled={this.getRemainingChars() === 280}>...</button>
```

Cela fonctionne mais pourrait casser si, par exemple, vous refactorisez plus tard `getRemainingChars` pour qu'il retourne une chaîne au lieu d'un nombre. Au lieu de cela, nous pouvons garder la logique précédente et simplement la déplacer en haut du `render()` :

```js
render() {
    const isTweetButtonDisabled = this.state.text.length === 0 && !this.state.photoAdded;
  
    return (
      ...
        <button className="..." disabled={isTweetButtonDisabled}>Tweet</button>
      ...
    );
  }
```

C'est tout ! Essayez de basculer le bouton « Ajouter une photo » et vérifiez que le bouton « Tweet » est activé/désactivé correctement.

#### Nous avons terminé !

Voici le Pen résultant :

%[https://codepen.io/julienben/pen/roZXvE]

### Étape 13 : Réflexion sur le code React — Pourquoi si simple ? (5 minutes)

Les modifications pour accommoder le bouton « Ajouter une photo » étaient minimes lors de l'utilisation de React. Aucun refactoring nécessaire. Pourquoi est-ce le cas ?

Encore une fois, cela a à voir avec le style d'écriture du code UI de React. Dans React, les gestionnaires d'événements modifient l'`état`, et chaque fois que l'état est modifié, **React appelle automatiquement** `render()` à nouveau pour mettre à jour l'UI.

Dans cet exemple particulier, le diagramme ressemble maintenant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*DN_-X4stP1U7E6-h align="left")

L'`état` devient une chose intermédiaire qui se situe entre les gestionnaires d'événements et `render()` :

* Les gestionnaires d'événements n'ont pas besoin de se soucier de quelle partie du DOM change. Ils doivent simplement définir l'`état`.

* De même, lorsque vous écrivez `render()`, tout ce dont vous avez besoin de vous soucier est l'`état` actuel.

### Comparaison avec jQuery

Vous pouvez imaginer ce qui se passerait si l'interface utilisateur avait plus de fonctionnalités. Sans l'état intermédiaire, nous aurions du mal à gérer la complexité. C'est pourquoi vous voudriez utiliser React plutôt que jQuery pour les interfaces utilisateur complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*N2IvA6TZIvC-T155 align="left")

Encore une fois, **il est possible** d'écrire du code jQuery propre qui ne ressemble pas à du code spaghetti. **Mais vous devez trouver vous-même la structure du code** et réfléchir à la façon de refactoriser chaque fois que vous ajoutez une nouvelle fonctionnalité. React vous fournit cette structure et réduit votre charge cognitive.

> Notez que l'idée de séparer l'état du rendu n'a pas été inventée avec React. Nous la regardons simplement du point de vue de React.

### Étape 14 : La dernière fonctionnalité — Mise en évidence des caractères dépassant la limite (5 minutes)

La dernière fonctionnalité que nous allons implémenter est la **mise en évidence des caractères dépassant la limite**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*C1OJuGMg8agMuugu align="left")

Malheureusement, **nous ne allons pas mettre en évidence le texte réel à l'intérieur de la boîte de Tweet** car cela nécessiterait de changer `<textar`ea&`gt; en <div contenteditabl`e="tr`ue"> et con`tenteditable est un peu trop compliqué à des fins illustratives.

Au lieu de cela, **nous allons afficher une boîte d'alerte Bootstrap** en haut et indiquer quels caractères doivent être supprimés, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*3Lnj6RRDfqMk1c8l align="left")

**Pour l'essayer, copiez la citation suivante de la documentation officielle de React :**

> React adopte le fait que la logique de rendu est intrinsèquement couplée avec d'autres logiques d'interface utilisateur : comment les événements sont gérés, comment l'état change au fil du temps, et comment les données sont préparées pour l'affichage.

> Au lieu de séparer artificiellement les technologies en mettant le balisage et la logique dans des fichiers séparés, React sépare les préoccupations avec des unités faiblement couplées appelées « composants » qui contiennent les deux.

%[https://codepen.io/julienben/pen/bOmdWZ]

* Il devrait afficher une boîte d'alerte avec les caractères dépassant la limite mis en évidence en rouge.

* Il devrait également afficher 10 caractères avant le point de coupure, sans aucune mise en évidence.

Si nous devions implémenter cela en jQuery, notre code deviendrait beaucoup plus désordonné. Remarquez dans le diagramme que nous allons ajouter deux flèches supplémentaires pour une nouvelle fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5IJpVy_aq3SfO9Lq align="left")

**Nous ne allons donc pas implémenter cela en jQuery.** Nous allons simplement le faire avec React et en rester là. Ce sera assez simple à faire avec React — juste une flèche supplémentaire dans le diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/0*2lMKrwLX5WA-oUpb align="left")

### Étape 15 : Mise en évidence des caractères dépassant la limite avec React (10–15 minutes)

Commençons avec notre implémentation React précédente.

**✓ Forkez le Pen ci-dessous** pour commencer.

%[https://codepen.io/julienben/pen/roZXvE]

Nous allons procéder étape par étape. Tout d'abord, **nous allons afficher une alerte simple avec un texte statique lorsque vous écrivez au-delà de la limite.**

![Image](https://cdn-media-1.freecodecamp.org/images/0*ap1sBT75lN-f5hVD align="left")

Puisque cela nécessitera une conditionnelle, écrivons-la dans une méthode séparée. **Ajoutez** `{this.renderOverflowAlert()}` au-dessus du `textarea` :

```js
{this.renderOverflowAlert()}
<textarea ...></textarea>
```

Maintenant, cette méthode doit retourner :

* **Une balise div** pour la boîte d'alerte s'il n'y a plus de caractères.

* **Rien** (c'est-à-dire une chaîne vide ou NULL) sinon.

Il s'avère que dans React, **vous pouvez retourner du balisage JSX à partir d'une méthode et l'utiliser dans toute autre méthode**, tout fonctionnera simplement. En d'autres termes, vous pouvez faire quelque chose comme :

```js
someMethod = () => {
  return (
    <a href="#">Hello World</a>
  );
}
anotherMethod = () => {
  return (
    <h1>
      {this.someMethod()}
    </h1>
  );
}
```

Dans `renderOverflowAlert`, nous pouvons retourner `( <div> ... </div> )` dans un cas et rien dans **l'autre. Donc notre** méthode `renderOverflowAlert` ressemblera à ceci :

```js
renderOverflowAlert = () => {
  if (this.getRemainingChars() < 0) {
    return (
      <div className="alert alert-warning text-left">
        <strong>Oops! Too Long:</strong>
      </div>
    );
  }
  return '';
};
```

Remarquez que nous vérifions `this.getRemainingChars()` pour voir si nous devons afficher l'alerte ou non.

**Essayez cela en tapant 280+ caractères (ou 257+ caractères avec le bouton « Ajouter une photo » ON).** L'alerte devrait apparaître dès que la limite de caractères atteint -1.

#### Affichage des caractères dépassant la limite

![Image](https://cdn-media-1.freecodecamp.org/images/0*9IQGNgFJtO4Stlpk align="left")

*(Cela devrait dire 280 au lieu de 140 caractères.)*

Voici une décomposition de la logique que nous voulons pour le message d'alerte :

* Entre « Oops! Too Long: » et le texte réel, il y a un espace vide suivi de trois points. J'ai utilisé ici parce que lorsque l'on écrit du balisage en JSX, les espaces blancs entre les balises sont supprimés. (Vous pouvez les ajouter manuellement en utilisant `{' '}`.)

* Ensuite, il y a les 271e~280e (total de 10) caractères de `this.state.text`.

* Ensuite, il y a les caractères restants mis en évidence en rouge.

**Écrivons cela en JSX. À l'intérieur de** la clause `if` de `overflowAlert`, nous allons créer deux variables : `beforeOverflowText` et `overflowText`. Nous allons utiliser [la méthode substring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring) sur `this.state.text`.

```js
renderOverflowAlert = () => {
  if (this.getRemainingChars() < 0) {
    const beforeOverflowText = this.state.text.substring(280 - 10, 280);
    const overflowText = this.state.text.substring(280);
    return (
      <div className="alert alert-warning text-left">
        <strong>Oops! Too Long:</strong>
        &nbsp; &#8230;
        {beforeOverflowText}
        <strong className="bg-danger text-light">{overflowText}</strong>
      </div>
    );
  }
  return '';
};
```

* Si vous faites `.substring(a, b)`, il retournera le `(a + 1)-ième` jusqu'au `b-ième` caractères de la chaîne.

* Si vous faites `.substring(a)`, il retournera le `(a + 1)-ième` jusqu'aux derniers caractères de la chaîne.

* Nous utilisons la classe `bg-danger` de Bootstrap pour mettre en évidence le texte en rouge et `text-light` pour rendre le texte lisible contre le fond maintenant sombre.

Copiez-collez le texte suivant et vérifiez que la partie du texte après les 280 premiers caractères est mise en évidence. Nous avons presque terminé !

> React adopte le fait que la logique de rendu est intrinsèquement couplée avec d'autres logiques d'interface utilisateur : comment les événements sont gérés, comment l'état change au fil du temps, et comment les données sont préparées pour l'affichage.

> Au lieu de séparer artificiellement les technologies en mettant le balisage et la logique dans des fichiers séparés, React sépare les préoccupations avec des unités faiblement couplées appelées « composants » qui contiennent les deux.

#### Et si le bouton « Ajouter une photo » est ON ?

Si le bouton « Ajouter une photo » est ON, alors la limite de caractères diminue de 23. **Donc nos** `beforeOverflowText` et `overflowText` doivent en tenir compte :

```js
renderOverflowAlert = () => {
    if (this.getRemainingChars() < 0) {
      const imageLength = this.state.photoAdded ? 23 : 0;
      const beforeOverflowText = this.state.text.substring(
        280 - imageLength - 10,
        280 - imageLength,
      );
      const overflowText = this.state.text.substring(280 - imageLength);
      return (
        <div className="alert alert-warning text-left">
          <strong>Oops! Too Long:</strong>
          &nbsp; &#8230;
          {beforeOverflowText}
          <strong className="bg-danger text-light">{overflowText}</strong>
        </div>
      );
    }
    return '';
  };
```

Maintenant, essayez de basculer le bouton « Ajouter une photo » tout en entrant un texte plus long que la limite. Cela devrait fonctionner comme prévu. Voici le Pen :

%[https://codepen.io/julienben/pen/bOmdWZ]

C'est tout ! Encore une fois, vous pouvez voir que les modifications du code étaient simples :

![Image](https://cdn-media-1.freecodecamp.org/images/0*RJ-PiBFsvcPqqQCc align="left")

### Étape 16 : Qu'est-ce qui suit ? (5 minutes)

Cela conclut le tutoriel. Espérons que vous avez :

* compris les avantages de la structure des composants de React par rapport à la modification manuelle du DOM avec jQuery, et

* appris à écrire des composants React simples en utilisant JavaScript et JSX.

#### **Qu'est-ce qui suit ?**

Il existe de nombreuses façons de continuer à partir d'ici.

Une possibilité serait de consulter cet article court intitulé [Comment apprendre React — Une feuille de route du débutant à l'avancé](https://medium.freecodecamp.org/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6). Il peut vous aider à décider comment continuer au mieux à apprendre React.

Je recommande également vivement de lire les parties suivantes de la documentation officielle de React :

* [Getting started](https://reactjs.org/docs/getting-started.html) qui inclut les ressources d'apprentissage recommandées par l'équipe React, et

* [Thinking in React](https://reactjs.org/docs/thinking-in-react.html) qui vous aidera à comprendre comment penser à la construction de composants et d'applications avec React.

Avant de partir, j'ai un **défi optionnel** pour vous !

Si vous vous sentez suffisamment à l'aise avec React et souhaitez écrire votre propre code, **essayez de déplacer** `remainingChars` vers l'`état` du composant. Assurez-vous qu'il est mis à jour là où c'est nécessaire et utilisez-le dans tous les endroits pertinents.

**N'hésitez pas à publier le résultat en tant que Pen dans les commentaires et je serai très heureux de le vérifier !**

#### Remerciements

Merci beaucoup d'avoir lu jusqu'ici ! Et surtout merci à [@chibicode](https://twitter.com/chibicode) pour l'énorme quantité de travail qu'il a mise dans la première version de ce tutoriel ! J'espère que cette version mise à jour lui rend justice.

Je suis Julien. Je travaille en tant qu'ingénieur frontend chez [Healthy.io](https://healthy.io) et j'aide à maintenir [react-boilerplate](https://github.com/react-boilerplate/react-boilerplate) sur GitHub. Si vous trouvez une erreur, souhaitez des clarifications ou pensez que j'ai oublié quelque chose d'important, faites-le moi savoir et je m'assurerai de le corriger.