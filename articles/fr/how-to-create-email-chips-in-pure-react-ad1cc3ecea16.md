---
title: Comment créer des puces d'email en React pur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T15:35:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-email-chips-in-pure-react-ad1cc3ecea16
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iuSKK3d30UFIb_vNPdftjQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer des puces d'email en React pur
seo_desc: 'By Andreas Remdt

  Imagine that you, the good-looking developer (yes, I’m talking to you!), want to
  build an invitation form where users can add one or more email addresses to a list
  and send a message to all of them.

  Thinking about how this could be s...'
---

Par Andreas Remdt

Imaginez que vous, le développeur au look soigné (oui, je vous parle à vous !), souhaitez créer un formulaire d'invitation où les utilisateurs peuvent ajouter une ou plusieurs adresses email à une liste et envoyer un message à tous.

En réfléchissant à la meilleure façon de résoudre ce problème, j'ai regardé ce que Google fait dans leur application Gmail. Dans la superposition "Nouveau message", vous pouvez entrer une adresse email et appuyer sur "Retour", "Tabulation" ou une virgule pour l'ajouter à la liste des destinataires. Vous pouvez même coller un ensemble d'adresses email et l'application les analysera et les ajoutera à votre liste. Plutôt pratique, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*aspoxkk5fBGcOYz52fn1Ng.gif)
_Entrez des emails dans Gmail pour les ajouter sous forme de puces._

Ces composants visuels sont communément appelés **Chips** ou **Badges** et peuvent être trouvés dans des frameworks comme [Materialize](https://materializecss.com/chips.html), [Bootstrap](https://getbootstrap.com/docs/4.0/components/badge/) ou [Material UI](https://material-ui.com/demos/chips/).

### Ce que nous allons construire

Dans ce tutoriel, je veux construire une telle fonctionnalité en React pur, sans utiliser d'autre bibliothèque ou framework. Nous allons créer un champ de saisie qui n'accepte que les adresses email. L'utilisateur peut les taper une par une ou coller un ensemble d'emails, ce qui créera les puces comme vous pouvez le voir et l'essayer dans l'exemple ci-dessous :

%[https://codesandbox.io/s/ypyxr11109?from-embed]

**Avertissement :** il existe déjà divers [paquets npm](https://react-select.com/) qui font le même travail, cependant, j'aime implémenter de petites fonctionnalités à partir de zéro car je n'aime pas dépendre de scripts tiers (parfois énormes). De plus, c'est un bon exercice pour pratiquer vos compétences React.

### Échafaudage du projet

Puisque nous n'avons pas besoin de quoi que ce soit de spécial pour commencer, utilisons simplement [create-react-app](https://facebook.github.io/create-react-app/). Au cas où vous ne l'auriez pas encore installé sur votre ordinateur, ouvrez votre terminal et entrez `npm install -g create-react-app`.

Après l'exécution de la commande, _create-react-app_ devrait être installé (si vous obtenez une erreur pendant l'installation, vous devrez peut-être l'exécuter avec des privilèges d'administrateur : `sudo npm install -g create-react-app`) et prêt à l'emploi.

Allez dans votre espace de travail et tapez `create-react-app chips`. Dans mon cas, je vais nommer mon dossier `chips`, mais vous pouvez choisir le nom que vous préférez.

_create-react-app_ va de l'avant et fait son travail, installant toutes les dépendances dont nous avons besoin pour commencer. Après cela, vous pouvez taper `cd chips` pour entrer dans notre nouveau répertoire et `npm start` pour démarrer le serveur de développement. Si tout s'est bien passé, vous devriez être accueilli par l'écran par défaut de l'application React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2FOVwYE200eijYlWrq_dOg.png)
_Voir cet écran signifie que vous avez réussi à configurer l'échafaudage de votre projet. Plongeons directement dans le code !_

### Organisation du projet

Dans notre répertoire `chips`, nous avons un ensemble de dossiers et de fichiers qui ont été créés pour notre commodité. Nous travaillerons principalement dans `src/App.js`, alors ouvrez ce fichier dans votre éditeur de code préféré.

Supprimez tout le code que vous voyez à l'intérieur de `App.js`. Ensuite, ajoutons un composant de classe React de base :

```jsx
import React from 'react';

class App extends React.Component {
  render() {
    return <p>Hello World</p>;
  }
}
```

Après avoir sauvegardé `App.js`, vous devriez voir votre navigateur se rafraîchir automatiquement. La page sombre avec le logo React a disparu, à la place, nous avons le simple texte "Hello World" affiché à l'écran. Bon début !

### Le champ de saisie et l'état

Ensuite, nous allons remplacer le texte "Hello World" pas très utile dans notre JSX par quelque chose de plus adapté : un élément de saisie.

```js
return (
  <input
    placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
    value={this.state.value}
    onChange={this.handleChange}
  />
);
```

Nous avons maintenant un élément de saisie HTML avec un attribut `placeholder`, qui s'affichera tant que l'utilisateur n'aura rien entré.

En dessous de l'attribut `placeholder`, vous remarquerez quelque chose de très courant dans le monde React, connu sous le nom de [Composant Contrôlé](https://reactjs.org/docs/forms.html#controlled-components). Normalement, les éléments de formulaire HTML comme `input` ou `textarea` ont leur propre état, que nous pouvons lire et écrire avec des méthodes DOM comme `document.getElementById('input').value`.

En utilisant des Composants Contrôlés, l'idée est que l'état de notre composant React est la seule source de vérité, ce qui signifie que la valeur de la saisie et notre état sont synchronisés.

Cela nous permet de manipuler les données entrées _à la volée_ et d'ajouter certaines fonctionnalités dont nous aurons besoin plus tard.

Si vous sauvegardiez et exécutiez cela dans votre navigateur, vous verriez le message d'erreur `TypeError: Cannot read property 'value' of null`. Si vous regardez l'extrait de code, cela a du sens, car nous essayons d'accéder à `value` depuis `this.state`, mais nous n'avons pas encore configuré l'état, ni n'avons la méthode `handleChange` pour contrôler notre état. Ajoutons-les.

```jsx
class App extends React.Component {
  state = {
    value: ''
  }
  
  handleChange = (evt) => {
    this.setState({
      value: evt.target.value
    });
  };
  
  render() { ... }
}
```

Tout d'abord, nous initialisons un [objet d'état](https://reactjs.org/docs/state-and-lifecycle.html#adding-local-state-to-a-class) qui contient une propriété `value` vide. En dessous, nous définissons la méthode `handleChange` qui sera appelée chaque fois que l'événement [change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event) sur l'élément de saisie est déclenché. `handleChange` s'exécute ensuite et met à jour l'état en utilisant `setState`.

`evt.target.value` n'est pas quelque chose que React nous fournit ; cela vient directement avec JavaScript. `evt.target` est la saisie que nous avons tapée, `value` est la valeur entrée (quelle surprise).

Allez-y et essayez-le : dans votre navigateur, vous devriez pouvoir taper quelque chose dans la saisie. Ce que vous ne voyez pas, c'est qu'en coulisses, vos données tapées sont synchronisées avec l'état de votre composant React. Quelle magie !

### Ajout d'emails sous forme de puces

L'étape suivante consiste à permettre à l'utilisateur d'ajouter des emails à une liste en appuyant sur "Retour", "Tabulation" ou la touche virgule de leur clavier. Avant de pouvoir faire cela, nous avons besoin d'une liste (ou plutôt d'un tableau) dans notre état où nous pouvons ajouter des emails :

```js
state = {
  value: '',
  emails: []
}
```

Maintenant que nous avons un tableau avec lequel travailler, nous devons réagir (jeu de mots intentionnel) lorsque les utilisateurs appuient sur ces touches spéciales. La meilleure façon de le faire est d'utiliser l'événement [keydown event](https://developer.mozilla.org/en-US/docs/Web/Events/keydown) :

```jsx
return (
  <input
    placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
    value={this.state.value}
    onChange={this.handleChange}
    onKeyDown={this.handleKeyDown}
  />
);
```

Remarquez comment j'ai ajouté l'écouteur d'événement `onKeyDown`, qui fait référence à la méthode suivante :

```jsx
handleKeyDown = (evt) => {
  if (['Enter', 'Tab', ','].includes(evt.key)) {
    evt.preventDefault();
      
    var email = this.state.value.trim();
      
    if (email) {
      this.setState({
        emails: [...this.state.emails, email],
        value: ''
      });
    }
  }
};
```

Wow, il se passe tant de choses ici, n'est-ce pas ? Ne vous inquiétez pas, passons en revue les changements étape par étape :

1. `if (['Enter', 'Tab', ','].includes(evt.key))` est là où la magie commence : à l'intérieur de cette condition, nous vérifions si la touche pressée (`evt.key`) est l'une de nos touches de déclenchement. J'ai créé un tableau avec ces trois touches (vous pourriez facilement ajouter une autre touche comme "Espace"). En utilisant la méthode [includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes), nous vérifions si notre touche pressée fait partie du tableau. Cela dit, si un utilisateur presse "Tab", alors `evt.key` serait `Tab` qui existe à l'intérieur du tableau, donc la condition est vraie.
2. Si la condition est vraie, nous empêchons le comportement par défaut de se produire. Normalement, en appuyant sur la touche "Tab" tout en étant à l'intérieur d'un élément de saisie, vous vous concentreriez sur un autre élément de la page ou du navigateur ([navigation au clavier](https://www.nngroup.com/articles/keyboard-accessibility/)), ce qui signifie que nous quitterions notre saisie actuelle. Mais en utilisant `evt.preventDefault()`, vous pouvez remplacer le comportement par défaut du navigateur.
3. En dessous, nous sauvegardons la saisie que nous avons obtenue jusqu'à présent. `this.state.value` contient toujours ce que l'utilisateur a tapé, c'est à cela que sert notre méthode `handleChange`. En utilisant [trim](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim), nous pouvons simplement supprimer les espaces avant ou après la saisie.
4. Ensuite, nous vérifions si l'utilisateur a réellement entré des données. Si ce n'est pas le cas, nous ne voulons rien faire.
5. Cependant, si `email` contient réellement des données (ce qui pourrait vraiment être n'importe quoi pour l'instant), nous l'ajoutons au tableau `emails` dans notre état.
6. Enfin, nous réinitialisons la propriété `value` dans notre état, ce qui signifie que notre champ de saisie sera effacé et que l'utilisateur pourra commencer à taper une nouvelle adresse email (s'il le souhaite). C'est la beauté des composants contrôlés !

Vous vous demandez peut-être ce que fait `[...this.state.emails, email]`, n'est-ce pas ? Eh bien, c'est une fonctionnalité JavaScript assez nouvelle appelée [syntaxe de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax). Les trois points signifient que nous extrayons tous les emails de `this.state.emails`. Maintenant que nous les avons extraits, nous pouvons les fusionner avec notre nouvel `email` dans un nouveau tableau. Enfin, nous remplaçons notre propriété `emails` actuelle en lui assignant le tableau nouvellement créé. Si vous voulez en savoir plus sur cette technique et pourquoi nous ne pouvons pas utiliser `array.push()`, consultez ce [fil de discussion Stack Overflow](https://stackoverflow.com/questions/26253351/correct-modification-of-state-arrays-in-reactjs).

Allez-y et essayez-le. Entrez quelque chose dans le champ de saisie et appuyez sur l'une de nos trois touches de déclenchement. Attendez, rien de spécial ne se passe, dites-vous ? Eh bien, c'est un peu attendu, car bien que nous ajoutions chaque saisie à notre tableau d'emails, nous ne faisons vraiment rien avec, n'est-ce pas ? Il est temps de les afficher :

```jsx
return (
  <React.Fragment>
    {this.state.emails.map(email => <div key={email}>{email}</div>)}
    
    <input
      placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
      value={this.state.value}
      onChange={this.handleChange}
      onKeyDown={this.handleKeyDown}
    />
  </React.Fragment>
);
```

Si vous regardez le JSX ci-dessus, vous verrez que j'ai enveloppé toute notre sortie avec un [fragment React](https://reactjs.org/docs/fragments.html) et placé une expression au-dessus du champ de saisie.

Le fragment est là pour que je n'aie pas à rendre un élément HTML inutile dans le DOM.

L'expression à la ligne 3 est un autre [modèle React typique](https://reactjs.org/docs/lists-and-keys.html) que vous trouverez dans presque toutes les applications : ici, nous parcourons (ou mappons, pour être plus précis) le tableau `emails` de notre état et affichons un `div` pour chaque élément. Le `div` a l'adresse email comme contenu textuel (et n'oubliez pas la propriété `key`, sinon React sera en colère contre vous).

Voyons ce que nous avons accompli jusqu'à présent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HLu5YUXafKEZZQbv8zcDlw.gif)
_N'est-ce pas la plus grande application de tous les temps ?_

### Suppression d'emails de la liste

C'est bien et tout, mais que se passe-t-il si vous avez ajouté quelqu'un que — disons — vous n'aimez pas vraiment ? Nous avons besoin d'une fonctionnalité pour supprimer les emails déjà ajoutés de la liste !

```jsx
{this.state.emails.map(email => (
  <div key={email}>
    {email}
    
    <button
      type="button"
      onClick={() =>  this.handleDelete(email)}
    >
      &times;
    </button>
  </div>
))}
```

Regardez le code ci-dessus. Vous vous souvenez quand nous avons ajouté le JSX pour parcourir tous les emails et les afficher ? C'est le même bloc de code, mais maintenant j'ai ajouté un bouton à l'intérieur de notre `div` qui a un écouteur d'événement [click event](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event). Cet écouteur va appeler `handleDelete` dès qu'un utilisateur appuie sur le bouton.

Remarquez comment cet appel de fonction est différent, cependant. C'est en fait une fonction fléchée qui est appelée et qui, en retour, appelle la méthode `handleDelete` avec un paramètre, dans ce cas, notre email.

C'est une approche différente de ce que vous avez vu jusqu'à présent, où nous faisions simplement quelque chose comme `onChange={this.handleChange}`. La raison est que cette fois, nous devons passer l'email que l'utilisateur veut supprimer dans notre méthode en tant que paramètre, sinon nous ne pourrions pas savoir quel email supprimer. Si vous voulez en savoir plus, [cet article](https://medium.freecodecamp.org/reactjs-pass-parameters-to-event-handlers-ca1f5c422b9) vous couvre.

Implémentons la méthode `handleDelete` :

```jsx
handleDelete = (toBeRemoved) => {
  this.setState({
    emails: this.state.emails.filter(email => email !== toBeRemoved)
  });
};
```

Tout ce que nous faisons ici, c'est de définir à nouveau notre état, mais cette fois nous filtrons l'adresse email qui a été passée en paramètre. La méthode [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) en JavaScript est assez pratique dans des cas comme celui-ci.

Nous n'avons pas à utiliser la syntaxe de décomposition bizarre que vous avez vue plus tôt (`[...array1, newItem]`), car `filter` retourne un nouveau tableau qui n'inclut pas la valeur que nous venons de filtrer. Nous pouvons ensuite définir ce nouveau tableau comme notre liste `emails`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3TdomJxTpg-buGyWypOvDQ.gif)
_La suppression fait maintenant partie de notre composant._

### Le rendre joli

Si vous êtes comme moi, vous pourriez grimacer en voyant la quantité de contenu non stylisé. Rendons ce mauvais garçon joli :

```jsx
return (
  <main className="wrapper">
    {this.state.emails.map(email => (
      <div className="email-chip" key={email}>
        {email}
        
        <button
          type="button"
          className="button"
          onClick={() =>  this.handleDelete(email)}
        >
          &times;
        </button>
      </div>
    ))}
    
    <input
      className="input"
      placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
      value={this.state.value}
      onChange={this.handleChange}
      onKeyDown={this.handleKeyDown}
    />
  </main>
);
```

1. La première chose que vous remarquerez, c'est que j'ai remplacé le `React.Fragment` par `<main className="wrapper">. Cela sert uniquement à des fins de style, je veux centrer le wrapper sur ma page.
2. J'ai également ajouté quelques classes à la saisie, au bouton et aux puces elles-mêmes, qui recevront un joli style de notre fichier CSS.
3. En haut du fichier, en dessous de `import React from 'react'`, j'ai ajouté une autre importation : `import './app.css'`. Si vous avez utilisé _create-react-app_, vous trouverez probablement un `App.css` dans votre répertoire `src`. J'ai simplement renommé le mien en `app.css` en minuscules et l'ai importé.

Vous pouvez [trouver le CSS ici](https://codesandbox.io/embed/ypyxr11109), je ne vais pas le montrer ici car cela ajouterait trop de contenu à cet article déjà long.

Voyons à quoi ressemble notre application maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HcbeRWkRvbqLRCB6MhRImQ.gif)
_N'est-ce pas une chose de beauté ?_

### Validation

Notre composant prend forme, mais vous pourriez commencer à vous demander ce qui se passera si un utilisateur entre des charabia au lieu d'une véritable adresse email, n'est-ce pas ? N'EST-CE PAS ?

Actuellement, notre composant accepte tous types de saisie, ce que nous devrions corriger comme prochaine étape. Ajoutons d'abord une méthode `isValid` :

```jsx
isValid(email) {
  var error = null;
  
  if (!this.isEmail(email)) {
    error = `${email} n'est pas une adresse email valide.`;
  }
  
  if (this.isInList(email)) {
    error = `${email} a déjà été ajouté.`;
  }
  
  if (error) {
    this.setState({ error });
    
    return false;
  }
  
  return true;
}
```

La méthode `isValid` reçoit un seul paramètre, qui est la saisie (dans le meilleur des cas, une adresse email) que nous voulons valider. Elle initialise une variable `error` avec `null`, ce qui signifie que nous n'avons pas encore d'erreurs.

Nous voyons ensuite 2 conditions if. La première vérifie si la valeur est une adresse email valide en utilisant la méthode `isEmail` :

```js
isEmail(email) {
  return /[\w\d\.-]+@[\w\d\.-]+\.[\w\d\.-]+/.test(email);
}
```

Ici, nous recevons un seul paramètre qui devrait, mais pourrait ne pas être l'email que nous voulons ajouter. En utilisant une [expression régulière](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) et la méthode [test](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test), nous vérifions si c'est réellement une adresse email valide.

**Avertissement :** Je ne garantis pas que l'expression régulière fournie est la meilleure pour valider les emails. C'est un sujet difficile et il existe de nombreuses variations différentes, et les choses [peuvent devenir assez compliquées](https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression). Mais je vais m'en tenir à celle-ci, car elle fait le travail.

La deuxième méthode `isInList` reçoit également un seul paramètre (l'email) et vérifie s'il a déjà été ajouté à notre tableau `emails` dans l'état. Encore une fois, la méthode [includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) est utilisée :

```js
isInList(email) {
  return this.state.items.includes(email);
}
```

Tout ce que fait notre méthode `isValid`, c'est utiliser les deux autres méthodes pour vérifier si la valeur donnée est une adresse email valide et ne fait pas encore partie de notre liste. Si aucune de ces conditions n'est vraie, nous ne définissons aucun message d'erreur et retournons `true`.

Sinon, si l'une de ces conditions est effectivement vraie, ce qui signifie que l'email est invalide ou déjà dans la liste, nous définissons un message d'erreur et retournons `false`. L'erreur vit dans l'état de notre composant, donc nous devons ajouter la propriété :

```jsx
class App extends React.Component {
  state = {
    value: '',
    emails: [],
    error: null
  }
  
  // ...
}
```

Remarquez que la propriété d'erreur est initialisée avec `null`, car lorsque nous chargeons initialement l'application, il n'y a pas d'erreur, bien sûr.

Deux choses manquent encore : dans notre méthode `handleKeyDown`, nous devons réellement utiliser la méthode `isValid`. Et nous devrions afficher l'erreur à l'utilisateur, sinon avoir un message d'erreur en premier lieu serait plutôt inutile.

```jsx
handleKeyDown = (evt) => {
  if (['Enter', 'Tab', ','].includes(evt.key)) {
    evt.preventDefault();
    
    var email = this.state.value.trim();
    
    if (email && this.isValid(email)) {
      this.setState({
        emails: [...this.state.emails, email],
        value: ''
      });
    }
  }
};
```

Vous vous souvenez de la méthode `handleKeyDown` ? J'espère bien, car vous devez la changer pour obtenir la validation. À la ligne 7, remarquez que j'ai ajouté `&& this.isValid(email)` à l'intérieur de la condition. Cela signifie que nous utilisons maintenant notre validation, en lui passant la valeur que l'utilisateur a tapée. Seulement si `email` a une valeur réelle **et** qu'il s'agit d'une adresse email valide, nous continuons en définissant l'état.

La dernière partie du puzzle est d'afficher le message d'erreur à l'utilisateur.

```jsx
return (
  <main className="wrapper">
    {this.state.emails.map(email => (
      // Caché...
    ))}
    
    <input
      className={'input' + (this.state.error && ' has-error')}
      placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
      value={this.state.value}
      onChange={this.handleChange}
      onKeyDown={this.handleKeyDown}
    />
    
    {this.state.error &&
      <p className="error">{this.state.error}</p>}
  </main>
);
```

Deux choses ont changé :

1. En dessous de la `saisie`, nous [affichons conditionnellement](https://reactjs.org/docs/conditional-rendering.html) un paragraphe avec notre message d'erreur comme contenu textuel.
2. Le `className` de notre saisie n'est plus une simple chaîne, mais une expression JSX qui ajoute `has-error` au nom de la classe si `error` est vrai. Cela est utile pour donner à notre saisie un style personnalisé si elle est invalide.

Allez-y et essayez le résultat dans votre navigateur. Essayez d'entrer une adresse email invalide ou une qui fait déjà partie de la liste. Vous devriez voir que le message d'erreur s'affiche en dessous de la saisie.

Il y a un problème cependant : si vous avez fait apparaître le message d'erreur, il restera pour toujours, même si vous ajoutez une adresse email valide par la suite. Nous devons réinitialiser l'erreur après que l'utilisateur ait recommencé à taper :

```jsx
handleChange = (evt) => {
  this.setState({
    value: evt.target.value,
    error: null
  });
};
```

Notre méthode `handleChange` est le meilleur endroit pour le faire ! Elle est appelée chaque fois que l'utilisateur change la valeur de la saisie, ce qui signifie que nous pouvons réinitialiser l'erreur à `null`. Si l'utilisateur n'a pas tiré la leçon et essaie d'ajouter une adresse email invalide à nouveau, alors... eh bien, le message d'erreur réapparaîtra.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HDxIJOmzk7f8wiGZgoPl5g.gif)
_Plus de données invalides !_

### Gestion du collage depuis le presse-papiers

Notre petit composant a bien grandi et est devenu quelque peu utile, mais une fonctionnalité importante manque encore : coller des adresses email depuis le presse-papiers.

Cela peut être assez intéressant car les utilisateurs pourraient vouloir copier un ensemble d'adresses email depuis leur application de messagerie et les coller toutes en une fois. Cependant, différentes applications de messagerie ont différents formats. Si vous copiez un ensemble d'emails depuis l'application Mail d'Apple, par exemple, cela ressemble à ceci :

```
À : John Doe <john.doe@gmail.com> Cc : Jane Doe <jane.doe@gmail.com>
```

Votre application pourrait le gérer différemment. Alors, comment analysons-nous ces chaînes pour n'obtenir que la partie que nous voulons ?

```jsx
handlePaste = (evt) => {
  evt.preventDefault();
  
  var paste = evt.clipboardData.getData('text');
  var emails = paste.match(/[\w\d\.-]+@[\w\d\.-]+\.[\w\d\.-]+/g);
  
  if (emails) {
    var toBeAdded = emails.filter(email => !this.isInList(email));
    
    this.setState({
      emails: [...this.state.emails, ...toBeAdded]
    });
  }
};
```

La méthode ci-dessus est beaucoup à digérer, alors plongeons directement dedans.

1. À la ligne 2, nous empêchons le comportement par défaut, ce qui signifie que le texte n'est pas réellement collé dans le champ de saisie. Nous allons le traiter nous-mêmes.
2. À la ligne 4, nous obtenons les données du presse-papiers que l'utilisateur était sur le point de coller en utilisant l'[API Clipboard](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent/clipboardData). `paste` est une chaîne.
3. En dessous, à la ligne 5, nous utilisons la méthode [match](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match) pour appliquer une regex à nos données du presse-papiers. La méthode `match` va parcourir toute notre chaîne et obtenir toutes les parties qui correspondent à notre expression régulière (c'est la même que celle que nous avons utilisée pour la partie validation). Le résultat est un tableau de correspondances ou `undefined` si rien ne correspond.
4. À la ligne 7, nous vérifions s'il y a des emails réels. Si oui, nous allons les filtrer à la ligne 8 pour exclure les emails qui sont déjà dans notre liste. `filter` est notre ami, encore une fois. La variable `toBeAdded` devrait maintenant être un tableau avec des emails qui ne font pas encore partie de notre liste. Remarquez comment nous avons bien réutilisé notre méthode `isInList`.
5. À la ligne 10, nous utilisons à nouveau la [syntaxe de décomposition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) pour fusionner notre tableau `emails` actuel avec le tableau `toBeAdded` nouvellement créé.

Remarquez comment nous n'avons pas validé les emails en utilisant `isEmail`. Cette étape est implicitement faite car nous nous sommes appuyés sur la même expression régulière pour obtenir toutes les adresses email valides. Si un utilisateur collait une adresse email invalide, elle ne passerait jamais.

Tout ce qui manque, c'est la connexion entre notre saisie et la méthode `handlePaste` :

```jsx
<input
  className={'input' + (this.state.error && ' has-error'}
  placeholder="Tapez ou collez des adresses email et appuyez sur `Entrée`"
  value={this.state.value}
  onChange={this.handleChange}
  onKeyDown={this.handleKeyDown}
  onPaste={this.handlePaste}
/>
```

Heureusement, l'événement [paste event](https://developer.mozilla.org/en-US/docs/Web/API/Element/paste_event) vous couvre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2Prkkci9KMmFSafXmvlbfw.gif)

### Conclusion

Voilà, notre composant terminé qui accepte plusieurs adresses email et permet même de les coller.

%[https://codesandbox.io/s/ypyxr11109?from-embed]

Bien sûr, vous pourriez ajouter plus de fonctionnalités et d'améliorations, voici quelques exemples :

* Si un utilisateur entre une adresse email mais n'appuie pas sur "Entrée" ou "Tabulation", que devrait-il se passer ? Vous pourriez attacher un événement [blur event](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event) à la saisie qui essaie de valider et d'ajouter le contenu si l'utilisateur clique sur autre chose sur la page, comme un bouton de soumission.
* Vous pourriez rendre les puces cliquables afin qu'un utilisateur puisse les sélectionner pour modifier l'adresse email.
* L'accessibilité pourrait certainement être améliorée, rendant plus facile pour les lecteurs d'écran de comprendre.

J'espère que vous avez apprécié ce tutoriel, n'hésitez pas à me faire part de vos suggestions ou commentaires. Bon codage !