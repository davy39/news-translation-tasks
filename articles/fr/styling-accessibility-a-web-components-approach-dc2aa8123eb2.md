---
title: 'Comment styliser l''accessibilité : une approche Web Components'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T23:24:05.000Z'
originalURL: https://freecodecamp.org/news/styling-accessibility-a-web-components-approach-dc2aa8123eb2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q8AgfDVFkz3mTgQujCC_sA.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment styliser l''accessibilité : une approche Web Components'
seo_desc: 'By Cristiano Correia

  a11y and the new Web Standards

  The new Web Standards are evolving fast, and sometimes it’s hard to actually know
  the current state of a particular subject in a sea of subjects. I often realize
  that the vast majority of web projec...'
---

Par Cristiano Correia

### **a11y et les nouvelles normes Web**

Les nouvelles normes Web évoluent rapidement, et il est parfois difficile de connaître l'**état actuel** d'un sujet particulier dans un océan de sujets. Je réalise souvent que la grande majorité des projets web commencent sans avoir l'accessibilité (a11y) à l'esprit, et il devient décourageant de revenir en arrière pour la corriger.

Puisque de nombreux projets Web Components restent à naître, j'ai décidé de rassembler les bases sur ces sujets particuliers et de guider toute personne naviguant dans ces eaux pour la première fois. Dans cet article, vous trouverez donc :

* Les bases de l'accessibilité
* Les bases des Web Components
* Ce qui est nouveau concernant le CSS
* Comment rendre vos Web Components plus accessibles

Partons à la découverte.

### **Bases #1. Qu'est-ce que l'accessibilité Web ?**

> _« L'accessibilité est souvent perçue comme le fait de rendre votre site compatible avec les lecteurs d'écran. En réalité, l'accessibilité web est un sous-ensemble de l'expérience utilisateur (UX) axé sur la rendre vos sites web utilisables par le plus large éventail de personnes possible, y compris celles qui ont des handicaps. »_

La citation ci-dessus (de Dave Ruppert dans « [Myth: Accessibility is 'blind people'](https://a11yproject.com/posts/myth-accessibility-is-blind-people/) » pour le projet a11y) reflète le plus grand défi de l'accessibilité Web : savoir exactement ce que c'est.

L'accessibilité Web est essentiellement un moyen de donner accès à votre produit à tous vos utilisateurs potentiels.

Les **5 catégories d'accessibilité** à prendre en compte sont :

* Visuelle (par exemple, non-voyants, myopie, daltonisme, etc.)
* Auditive
* Motrice
* Cognitive
* Utilisateurs temporairement handicapés (par exemple, utilisateurs de téléphone à une main)

Si nous devons **traduire cela dans un produit**, cela signifie généralement se soucier de :

* La sémantique
* Les entrées clavier
* Les alternatives textuelles
* Le contraste des couleurs

Pour en tenir compte **pendant le développement** d'un produit, vous devriez :

* Vous assurer de transmettre le sens non seulement par la couleur mais aussi par la forme
* Vous assurer que votre produit est redimensionnable
* Vous assurer que les sujets de votre contenu sont distinguables
* Vous assurer de suivre les [directives du W3C](https://www.w3.org/TR/WCAG20/) en général

… et n'oubliez pas l'**arbre d'accessibilité !** C'est

> _« la structure produite par les API d'accessibilité de la plateforme fonctionnant parallèlement au DOM, qui expose des informations d'accessibilité aux technologies d'assistance telles que les lecteurs d'écran »_ ([source](https://egghead.io/lessons/html-5-what-is-the-accessibility-tree)).

### **Bases #2 : Une brève histoire des Web Components**

Les Web Components, dans leur essence, ne sont en réalité « rien » : les Web Components sont un ensemble de **nouvelles normes Web** qui nous aident à atteindre une manière native de créer des **composants**. En termes généraux, je définirais les Web Components comme :

> **Une manière native** d'atteindre un **ensemble petit et réutilisable** de logique, de comportements et d'éléments d'interface, à travers une série de **normes de navigateurs**.

Alors, quels sont les éléments constitutifs des Web Components ?

* Les modèles HTML
* Le Shadow DOM
* Les éléments personnalisés
* … et les imports HTML (-ish)

#### **Modèles HTML**

Les modèles HTML sont une forme de réutilisation de morceaux de HTML sans que le « modèle » original ne soit rendu sur la page.

Cela fonctionne comme suit :

Ce qui rendra quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pzf_L1AF5M3CmIG-ZS67fQ.png)

Vous pouvez vérifier comment les modèles HTML sont actuellement pris en charge par les navigateurs sur cette [page caniuse](https://caniuse.com/#feat=template).

#### **Shadow DOM**

Le Shadow DOM est un moyen d'atteindre la portée CSS, l'encapsulation DOM et la composition, rendant plus facile la construction de composants isolés.

Il existe deux modes pour atteindre le Shadow DOM : « closed » et « open ». La différence est que lorsque vous instanciez `element.shadowRoot`, le mode « open » retourne le nœud HTML et le mode « closed » retourne `null`. Les deux modes retournent `null` lorsque vous essayez d'interroger le DOM. Gardez à l'esprit que vous devez définir un mode pour utiliser le Shadow DOM puisque qu'il n'y a pas de valeur par défaut.

Cela fonctionne comme suit :

Ce qui rendra quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u-0sv8xHko8XvLRdg5JywQ.png)

Et l'arbre DOM ressemblera à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PyqhU8gFZSc8Z4wc3LbyOQ.png)

Vous pouvez vérifier comment le Shadow DOM est actuellement pris en charge par les navigateurs sur cette [page caniuse](https://caniuse.com/#feat=shadowdomv1).

#### **Éléments personnalisés**

Les éléments personnalisés sont le moyen d'atteindre des morceaux de logique encapsulés et entièrement réutilisables, et de tirer le meilleur parti du Shadow DOM et des modèles HTML, y compris les **slots**.

Tout cela peut être réalisé comme suit :

Ce qui rendra quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HDfc7fGk0bNyoEtOspoVkQ.png)
*Vous pouvez voir les « Slots » de modèle remplacés en conséquence*

Vous pouvez vérifier comment les éléments personnalisés sont actuellement pris en charge par les navigateurs sur cette [page caniuse](https://caniuse.com/#feat=custom-elementsv1).

#### **… et le -ish : HTML Imports vs. ES Modules**

Les HTML Imports faisaient partie intégrante des normes Web Components, mais ils ont cessé d'être pris en charge et ne sont plus listés sur la page des Web Components (étant remplacés par les **ES Modules**). Ils ne sont plus qu'une note de bas de page à ce stade de l'histoire des Web Components. Comme le dit Wilson Page de l'équipe Firefox OS [ici](https://hacks.mozilla.org/2015/06/the-state-of-web-components/) :

> _« Nous travaillons avec les Web Components dans Firefox OS depuis plus d'un an et avons constaté que l'utilisation de la syntaxe de module existante (AMD ou Common JS) pour résoudre un arbre de dépendances, l'enregistrement d'éléments, chargés à l'aide d'une balise <script> normale semble suffisant pour faire avancer les choses. »_

Si vous souhaitez en savoir plus sur l'état des HTML Imports vs. ES Modules, vous pouvez consulter cette [page](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/HTML-Imports-and-ES-Modules.md).

Les Web Components sont bien plus que cela. Assurez-vous de continuer à chercher plus d'informations à leur sujet, notamment concernant les _événements personnalisés_, _observedAttributes_, les _tests_ et les _performances_.

### **Tour bonus : les nouvelles « théories » CSS**

Si vous revenez aux extraits de code de cet article, vous avez déjà entrevu quelques nouvelles offres de CSS :

* **CSS scopé** (via Shadow DOM) résout l'un des plus grands problèmes de CSS, le « sur-contrôle »
* Avec **:host**, nous pouvons sélectionner pour styliser un hôte d'ombre
* Il y a aussi **:host()** et **:host-context()** — le premier ciblant l'hôte qui est passé à l'intérieur des parenthèses (par exemple :host(.some-custom-element)) et le second ciblant le contenu d'un hôte d'ombre (par exemple :host-context(h2) cible les h2 à l'intérieur d'un hôte d'ombre)

#### **« Théories » que vous ne devriez pas utiliser**

Puisque les Web Components sont des normes en évolution continue, certaines choses sont venues et parties (comme les HTML Imports déjà mentionnés). C'est également le cas pour divers aspects de CSS, et c'est particulièrement vrai pour les **Shadow Piercing Combinators**, qui étaient des formes de stylisation des éléments ombrés. Si vous tombez sur ceux-ci, veuillez les éviter :) Ils sont :

* ::shadow
* /deep/
* >>>

#### **Mais attendez, les variables CSS !**

… et oui. Il existe des formes appropriées de stylisation des éléments ombrés : les variables CSS. Vous pouvez réutiliser des styles génériques à l'intérieur (et en fait, à l'extérieur) des Web Components. Voyons comment :

Le `h2` à l'intérieur de shadowRoot sera rendu comme le contenu de `--main-text-color` si elle existe. Si elle n'existe pas, il sera rendu en bleu. Le résultat est quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SZFlTLPiP3jVwEZ4uIVsbA.png)
*Dans ce cas, le contenu de la variable --main-text-color est jaune.*

Vous pouvez vérifier comment les variables CSS sont actuellement prises en charge par les navigateurs sur cette [page caniuse](https://caniuse.com/#feat=css-variables,css-grid).

#### **::part() et ::theme()**

::part() et ::theme() sont des propositions très récentes à CSS qui sont venues à notre aide en tant qu'alternatives pour styliser les éléments ombrés. Au lieu d'essayer de les expliquer, je vais simplement vous rediriger vers [cet article de Monica Dinculescu qui est excellent](https://meowni.ca/posts/part-theme-explainer/). Ce sont des propositions très récentes à CSS, il est donc tout à fait possible que, lorsque vous lirez cet article, elles ne soient toujours pas prises en charge par votre navigateur.

### **Alors, comment pouvons-nous rendre nos composants accessibles ?**

Tout d'abord…

#### **Bases, bases, #3. Les bases de l'accessibilité :**

Il y a quelques choses que nous pouvons faire pour notre produit dès le départ qui aideront énormément à le rendre accessible à nos utilisateurs.

Une chose à retenir est la _théorie du bleuet_ (une idée « volée » à nouveau d'une conférence de Monica Dunculescu) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*pXyF-ks0XH1GlZJd)
*Photo par [Unsplash](https://unsplash.com/@kaitlynraeann?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title="">Kaitlyn Chow</a> sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")*

Ce qui fait un muffin aux bleuets, ce n'est pas d'ajouter des bleuets à un muffin existant, c'est de cuisiner un muffin aux bleuets dès le début. Rendre un produit accessible, ce n'est pas ajouter quelques rôles et étiquettes ARIA après sa construction, mais c'est en fait avoir l'accessibilité à l'esprit dès le tout début.

Alors…

#### **Rôle**

Le rôle est un moyen de dire à un nouvel élément de se comporter comme un autre. Exemple rapide :

```html
<div role="button">Je suis un bouton</div>
```

#### **TabIndex**

TabIndex est un moyen de rendre un élément focalisable (essentiel pour un lecteur d'écran). Si vous le définissez à 0, il est focalisable dans le bon ordre, s'il est à -1, il est focalisable en dehors de l'ordre normal (c'est-à-dire que vous pouvez déclencher programmatiquement le focus de l'élément). Si vous le définissez à un autre nombre positif, vous changez l'ordre réel du focus (fortement déconseillé). Exemple rapide :

```html
<div tabindex="0">Je suis focalisable</div>
```

#### **Indicateur de focus**

L'indicateur de focus est quelque chose (généralement) natif du navigateur et sert d'aide visuelle pour indiquer quel élément est focalisé à l'instant. Si vous avez déjà pensé que le _design n'est pas parfait_, ne le supprimez pas (par exemple, sur Chrome, vous pouvez le voir comme une lueur orange ou bleue autour d'une entrée) avec `{ outline: none; }` dans le CSS, par exemple. Il est extrêmement utile pour tous ceux qui utilisent des lecteurs d'écran — si vous voulez le redessiner, assurez-vous de suivre les directives d'accessibilité.

#### **ARIA**

Aria est un moyen d'améliorer la façon dont vous étiquetez vos composants. Il en existe des tonnes, donc je ne vous embêterai pas avec la longue liste :) — vous pouvez les trouver [ici](https://www.w3.org/TR/wai-aria-1.0/states_and_properties) — juste un exemple rapide :

```html
<input type="range" min="0" max="10" value="5" aria-label="quantité de problème" aria-valuemin="0" aria-valuemax="10">
```

Sans les étiquettes ARIA, un lecteur d'écran percevrait l'entrée comme « 5, curseur » mais avec elles, il la lirait comme « ARIA : quantité de problème. 5, curseur. min : 0, max : 10 ».

Voici un excellent (et rapide) tutoriel sur la façon d'étiqueter un élément personnalisé :

[Comment étiqueter un élément personnalisé](https://www.w3.org/TR/wai-aria-practices-1.1/examples/checkbox/checkbox-1/checkbox-1.html)

#### **Entrée clavier**

Comme je l'ai mentionné au début de l'article, il est assez important de lier le comportement au clavier. Les éléments natifs de HTML devraient avoir cela couvert, mais si vous écrivez un élément personnalisé, n'oubliez jamais que les événements `onkeydown`, `onkeypress` et `onkeyup` sont vos meilleurs amis.

### **Alors, qu'y a-t-il de vraiment nouveau ?**

#### **La réponse courte :**

L'extension des interfaces HTML.

#### **La réponse longue :**

L'extension des interfaces HTML :)

Permettez-moi d'expliquer.

Bien qu'un élément natif doive être entièrement accessible, il ne fournit peut-être pas la fonctionnalité exacte dont vous avez besoin ou ne ressemble pas à ce que vous voulez. Nous pouvons certainement écrire quelque chose adapté à nos besoins réels, mais nous devrions prendre en charge tous les besoins d'accessibilité puisque les éléments personnalisés n'ont pas de sémantique implicite ni de support clavier. … Alors, pourquoi ne pouvons-nous pas **étendre** la fonctionnalité d'un élément natif ? Maintenant, nous pouvons. Ou « pouvons ».

#### **Interfaces d'éléments**

[Voici la liste](https://html.spec.whatwg.org/multipage/indices.html#element-interfaces) des interfaces HTML existantes. Avec elles, vous pouvez étendre le comportement natif. Nous pouvons revisiter notre exemple pour les éléments personnalisés et étendre `HTMLButtonElement` pour ajouter notre propre comportement. Voici comment :

```javascript
class AccessibleButton extends HTMLButtonElement {
  constructor() {
    super();
    this.innerHTML = `<style>
      :host {
        color: black;
      }
    </style>
    <span>Je suis un bouton accessible</span>`;
  }
}

customElements.define('accessible-button', AccessibleButton, { extends: 'button' });
```

Si vous vous souvenez des exemples précédents, j'ai ajouté (pour un effet dramatique :) une règle CSS selon laquelle tout le texte serait blanc. Cela va à l'encontre de l'apparence native d'un bouton et le rend illisible. En étendant l'élément normal avec le texte en noir, nous l'avons rendu un peu plus accessible (en plus, j'ai ajouté une étiquette supplémentaire dessus).

Les différences ici sont :

* `extends HTMLButtonElement` au lieu de `HTMLElement`
* Lorsque nous définissons le customElement, nous passons en troisième paramètre un objet avec l'élément qui est étendu (dans ce cas « button »)
* Et nous l'utilisons en référençant un élément bouton natif avec `is="accessible-button"`.

Cela rend quelque chose comme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpNCljDYJ5e1wFlqV6Q6VQ.png)

Le premier bouton n'est pas étendu, donc il a toujours la couleur blanche ; le deuxième est étendu, donc il a maintenant la couleur noire (plus une étiquette ARIA) et le troisième ne fonctionne pas… Pourquoi ? Parce que l'extension d'une interface HTML doit être faite via l'attribut `is` et non référencée via la balise d'élément personnalisé normale.

**Attention** : si vous consultez la page « [Extending custom HTML elements](https://developers.google.com/web/fundamentals/web-components/customelements#extendhtml) » de Google, il y a une note très importante :

> Seuls Chrome 67 prend en charge les éléments intégrés personnalisés ([statut](https://www.chromestatus.com/feature/4670146924773376)) pour l'instant. Edge et Firefox vont l'implémenter, mais Safari a choisi de ne pas l'implémenter. C'est regrettable pour l'accessibilité et l'amélioration progressive. Si vous pensez que l'extension des éléments HTML natifs est utile, faites entendre votre voix sur les [509](https://github.com/w3c/webcomponents/issues/509) et [662](https://github.com/w3c/webcomponents/issues/662) sur Github.

Ce n'est pas la fonctionnalité la plus sûre à utiliser pour l'instant, alors vérifiez toujours où votre produit doit être utilisé avant d'utiliser l'une des fonctionnalités référencées dans cet article, surtout celle-ci.

### **Alors, si les Web Components ne sont pas encore pris en charge partout, que dois-je faire ?**

Il y a un état intermédiaire :)

#### **Polyfills**

Tout d'abord, il y a des polyfills. [Consultez-les ici](https://www.webcomponents.org/polyfills).

#### **Bibliothèques qui facilitent votre vie**

[Angular Elements](https://angular.io/guide/elements), [Polymer](https://www.polymer-project.org/) et [Stencil](https://stenciljs.com/) ne sont que quelques exemples de bibliothèques qui peuvent vous aider à utiliser des éléments personnalisés pris en charge sur plusieurs navigateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k_pjGVXlRBVafs7tiocySA.png)
*De gauche à droite : Angular Elements, Polymer et Stencil*

#### **Outils**

Il existe un tas d'outils pour vous aider à rendre vos composants plus accessibles. Un de mes préférés est [Accessibility Developer Tools](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb/related?hl=en), offert par Google Accessibility. C'est une excellente extension Chrome.

Il existe également de nombreux _linters_ pour vous surveiller (par exemple, le projet actuel sur lequel je travaille est un projet React, donc j'utilise le **eslint-plugin-jsx-a11y** pour me surveiller).

### **TL;DR**

Essentiel pour l'accessibilité :

* La sémantique
* Les entrées clavier
* Les alternatives textuelles
* Le contraste des couleurs

Les éléments constitutifs des Web Components sont :

* Les modèles HTML
* Le Shadow DOM
* Les éléments personnalisés
* … et un peu plus

Les bases pour que notre code soit accessible sont :

* Utiliser le modèle de rôle
* Rendre nos éléments focalisables
* Fournir une aide visuelle pour l'élément focalisé
* Utiliser les étiquettes ARIA
* Lier les événements au clavier

Il existe également un moyen d'étendre le comportement natif d'un élément via l'extension des interfaces HTML.

### **Enfin, beaucoup de gens qui en savent bien plus que moi…**

Concernant l'accessibilité des Web Components :

* [The Future of Accessibility for Custom Elements](http://robdodson.me/the-future-of-accessibility-for-custom-elements/), par Rob Dodson
* [Accessibility of Web Components](https://marcysutton.github.io/accessibility-of-web-components/slides.html#/slide5), par Marcy Sutton
* [How to Make Accessible Web Components](https://www.sitepoint.com/accessible-web-components/), par Artem Tabalin
* [Making Web Components Accessible](https://www.grapecity.com/en/blogs/making-web-components-accessible), par Bernardo de Castilho

Concernant l'accessibilité en général :

* [Heck yes, accessibility — let’s make the future awesome](https://uxdesign.cc/future-tech-accessibility-e93600e8917e), par Mischa Andrews
* [Myth: Accessibility is 'blind people'](https://a11yproject.com/posts/myth-accessibility-is-blind-people/), par Dave Rupert
* [Accessible UI Components for the Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67), par Addy Osmani
* [The Accessibility Tree](https://developers.google.com/web/fundamentals/accessibility/semantics-builtin/the-accessibility-tree), par Meggin Kearney, Dave Gash et Alice Boxhall

Concernant les Web Components en général :

* [Practical lessons from a year of building web components](https://www.youtube.com/watch?v=zfQoleQEa4w), par Monica Dinculescu
* [Accessibility is My Favorite Part of the Platform](https://www.youtube.com/watch?v=2qjgxH384Nc), par Rob Dodson
* [Polymer: making Web Components accessible](https://www.youtube.com/watch?v=_IBiXfxhF-A), par Google Developers (bien que légèrement ancien, cela a toujours du sens)

### **… et la présentation.**

*Cet article est basé sur une conférence donnée lors d'une rencontre qui a eu lieu le [5 décembre 2018](https://www.meetup.com/landing_jobs/events/256720438/). Vous pouvez trouver cette présentation [ici](http://cristianocorreia.com/styling-accessibility/).*

Merci d'avoir lu, à la prochaine fois.