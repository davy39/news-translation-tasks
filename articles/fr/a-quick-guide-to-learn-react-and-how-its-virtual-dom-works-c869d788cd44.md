---
title: Un guide rapide pour apprendre React et comment son Virtual DOM fonctionne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vQXljCx6DN_aNLWD.jpg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide rapide pour apprendre React et comment son Virtual DOM fonctionne
seo_desc: 'By Jérémy Bardon


  This is part of my “React for beginners” series on introducing React, its core features
  and best practices to follow. More articles are coming!

  Next article >


  Do you want to learn React without crawling the documentation (well writ...'
---

Par Jérémy Bardon

> Ceci fait partie de ma série "React pour débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre. D'autres articles arrivent !

> [Article suivant >](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

Vous voulez apprendre React sans parcourir [la documentation](https://reactjs.org/docs/hello-world.html) (bien écrite soit-elle) ? Vous avez cliqué sur le bon article.

Nous allons apprendre comment exécuter React avec un seul fichier HTML, puis nous exposer à un premier extrait de code.

À la fin, vous serez en mesure d'expliquer ces concepts : props, composant fonctionnel, JSX et Virtual DOM.

Le but est de créer une montre qui affiche les heures et les minutes. React propose d'architecturer notre code avec des composants. `Créons notre composant de montre.

```html
<!-- Ignorer le code HTML5 standard -->
<script src="https://unpkg.com/react@16.2.0/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16.2.0/umd/react-dom.development.js"></script>

<!-- Pour le support JSX (avec babel) -->
<script src="https://unpkg.com/babel-standalone@6.24.2/babel.min.js" charset="utf-8"></script> 

<div id="app"></div> <!-- Point de montage React -->

<script type="text/babel">
  class Watch extends React.Component {
    render() {
      return <div>{this.props.hours}:{this.props.minutes}</div>;
    }
  }

  ReactDOM.render(<Watch hours="9" minutes="15"/>, document.getElementById('app'));
</script>
```

Ignorez le code HTML standard et les imports de scripts pour les dépendances (avec [unpkg](https://unpkg.com/#/), voir [l'exemple React](https://raw.githubusercontent.com/reactjs/reactjs.org/master/static/html/single-file-example.html)). Les quelques lignes restantes sont en fait du code React.

Tout d'abord, définissez le composant Watch et son modèle. Ensuite, montez React dans le DOM et demandez à rendre une montre.

### Injecter des données dans le composant

Notre montre est assez stupide, elle affiche les heures et les minutes que nous lui avons fournies.

Vous pouvez essayer de jouer avec et de changer la valeur de ces propriétés (appelées **props** dans React). Elle affichera toujours ce que vous avez demandé, même si ce ne sont pas des nombres.

Ce type de composant React avec seulement une fonction de rendu sont des **composants fonctionnels**. Ils ont une syntaxe plus concise par rapport aux classes.

```js
const Watch = (props) =>
  <div>{props.hours}:{props.minutes}</div>;

ReactDOM.render(<Watch hours="Hello" minutes="World"/>, document.getElementById('app'));
```

Les props ne sont que des données passées à un composant, généralement par un composant parent. Le composant utilise les props pour la logique métier et le rendu.

Mais dès que les props n'appartiennent pas au composant, elles sont **immuables**. Ainsi, le composant qui a fourni les props est le seul morceau de code capable de mettre à jour les valeurs des props.

L'utilisation des props est assez simple. Créez un nœud DOM avec le nom de votre composant comme nom de balise. Ensuite, donnez-lui des attributs nommés d'après les props. Ensuite, les props seront disponibles via `this.props` dans le composant.

### Qu'en est-il du HTML non cité ?

J'étais sûr que vous remarqueriez le HTML non cité retourné par la fonction `render`. Ce code utilise le langage JSX, c'est une syntaxe abrégée pour définir un modèle HTML dans les composants React.

```js
// Équivalent à JSX : <Watch hours="9" minutes="15"/>
React.createElement(Watch, {'hours': '9', 'minutes': '15'});
```

Maintenant, vous pourriez vouloir éviter JSX pour définir le modèle du composant. En fait, JSX ressemble à du [sucre syntaxique](https://en.wikipedia.org/wiki/Syntactic_sugar).

Jetez un coup d'œil au snippet suivant qui montre à la fois la syntaxe JSX et React pour vous faire une opinion.

```js
// Utilisation de JS avec React.createElement
React.createElement('form', null, 
  React.createElement('div', {'className': 'form-group'},
    React.createElement('label', {'htmlFor': 'email'}, 'Adresse email'),
    React.createElement('input', {'type': 'email', 'id': 'email', 'className': 'form-control'}),
  ),
  React.createElement('button', {'type': 'submit', 'className': 'btn btn-primary'}, 'Soumettre')
)

// Utilisation de JSX
<form>
  <div className="form-group">
    <label htmlFor="email">Adresse email</label>
    <input type="email" id="email" className="form-control"/>
  </div>
  <button type="submit" className="btn btn-primary">Soumettre</button>
</form>
```

### Aller plus loin avec le Virtual DOM

Cette dernière partie est plus compliquée mais très intéressante. Elle vous aidera à comprendre comment React fonctionne sous le capot.

La mise à jour des éléments sur une page web (un nœud dans l'arbre DOM) implique l'utilisation de l'API DOM. Cela redessinera la page, mais cela peut être lent (voir [cet article](https://hashnode.com/post/the-one-thing-that-no-one-properly-explains-about-react-why-virtual-dom-cisczhfj41bmssp53mvfwmgrq) pour savoir pourquoi).

De nombreux frameworks comme React et Vue.js contournent ce problème. Ils proposent une solution appelée le Virtual DOM.

```json
{
   "type":"div",
   "props":{ "className":"form-group" },
   "children":[
     {
       "type":"label",
       "props":{ "htmlFor":"email" },
       "children":[ "Adresse email"]
     },
     {
       "type":"input",
       "props":{ "type":"email", "id":"email", "className":"form-control"},
       "children":[]
     }
  ]
}
```

L'idée est simple. La lecture et la mise à jour de l'arbre DOM sont très coûteuses. Donc, faites le moins de changements possible et mettez à jour le moins de nœuds possible.

Réduire les appels à l'API DOM implique de garder une représentation de l'arbre DOM en mémoire. Puisque nous parlons de frameworks JavaScript, choisir JSON semble légitime.

Cette approche reflète immédiatement les changements dans le Virtual DOM.

De plus, elle regroupe quelques mises à jour à appliquer plus tard sur le vrai DOM en une seule fois (pour éviter les problèmes de performance).

Vous vous souvenez de `React.createElement` ? En fait, cette fonction (appelée directement ou via JSX) crée un nouveau nœud dans le Virtual DOM.

```js
// Implémentation naïve de React.createElement (en utilisant les fonctionnalités ES6)
function createElement(type, props, ...children) {
  return { type, props, children };
}
```

Pour appliquer les mises à jour, la fonction principale du Virtual DOM entre en jeu, l'[algorithme de réconciliation](https://reactjs.org/docs/reconciliation.html).

Son travail est de trouver la solution la plus optimisée pour résoudre la différence entre l'état précédent et actuel du Virtual DOM.

Et ensuite appliquer le nouveau Virtual DOM au vrai DOM.

### Lectures complémentaires

Cet article va loin dans les explications internes de React et du Virtual DOM. Pourtant, il est important de connaître un peu le fonctionnement d'un framework lorsque vous l'utilisez.

Si vous voulez apprendre comment le Virtual DOM fonctionne en détail, suivez mes recommandations de lecture. Vous pouvez écrire votre propre Virtual DOM et [apprendre le rendu DOM](http://www.html5rocks.com/en/tutorials/internals/howbrowserswork/).

> [**Comment écrire votre propre Virtual DOM**](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)​​

> [_Il y a deux choses que vous devez savoir pour construire votre propre Virtual DOM. Vous n'avez même pas besoin de plonger dans le code source de React..._](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)

Merci d'avoir lu. Désolé si cela est trop technique pour votre premier pas dans React. Mais j'espère que maintenant vous êtes conscient de ce que sont les props, les composants fonctionnels, JSX et le Virtual DOM.

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien ! ?**

**N'oubliez pas de me suivre pour être notifié de mes prochains articles** ?

> Ceci fait partie de ma série "React pour débutants" sur l'introduction à React, ses fonctionnalités principales et les meilleures pratiques à suivre.

> [Article suivant >](https://www.freecodecamp.org/news/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4/)

### Consultez mes [autres](https://medium.com/@jbardon/latest) articles

#### ➡ JavaScript

* [Comment améliorer vos compétences en JavaScript en écrivant votre propre framework de développement web](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190) ?
* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➡ Astuces et conseils

* [Arrêtez le débogage douloureux de JavaScript et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)

Publié à l'origine sur [www.linkedin.com](https://www.linkedin.com/pulse/intro-react-virtual-dom-jeremy-bardon) le 6 février 2018.