---
title: Comment écrire des composants qui fonctionnent dans n'importe quel Framework
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2023-11-06T20:25:12.000Z'
originalURL: https://freecodecamp.org/news/write-components-that-work-in-any-framework
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/og-button.png
tags:
- name: components
  slug: components
- name: Web Development
  slug: web-development
seo_title: Comment écrire des composants qui fonctionnent dans n'importe quel Framework
seo_desc: "The browser has a built-in way of writing reusable components in the form\
  \ of web components. They’re an excellent choice for building interactive and reusable\
  \ components that work in any frontend framework. \nWith that said, writing highly\
  \ interactive..."
---

Le navigateur dispose d'une méthode intégrée pour écrire des composants réutilisables sous la forme de **web components**. Ils constituent un excellent choix pour créer des composants interactifs et réutilisables qui fonctionnent dans n'importe quel framework frontend. 

Cela dit, écrire des web components hautement interactifs et robustes n'est pas simple. Ils nécessitent beaucoup de code boilerplate et semblent beaucoup moins intuitifs que les composants que vous avez pu écrire dans des frameworks comme React, Svelte ou Vue.

Dans ce tutoriel, je vais vous donner un exemple de composant interactif écrit sous forme de web component, puis le refactoriser en utilisant une bibliothèque qui adoucit les angles et supprime des tonnes de code boilerplate.

Ne vous inquiétez pas si vous n'êtes pas familier avec les web components. Dans la section suivante, je vais faire un (bref) aperçu de ce que sont les web components et de ce qui les compose. Si vous avez une certaine expérience avec eux, vous pouvez sauter la section suivante.

## Qu'est-ce que les Web Components ?

Avant les web components, le navigateur n'avait pas de méthode standard pour écrire des composants réutilisables. De nombreuses bibliothèques résolvent ce problème, mais elles rencontrent souvent des limitations comme les performances, l'interopérabilité et les problèmes avec les standards du web.

Les web components sont une technologie composée de 3 fonctionnalités différentes du navigateur :

* Éléments personnalisés
* Shadow DOM
* Modèles HTML

Nous allons faire un rapide tour d'horizon de ces technologies, mais ce n'est en aucun cas une analyse exhaustive.

### Qu'est-ce que les éléments personnalisés ?

Avec les éléments personnalisés, vous pouvez créer vos propres éléments HTML personnalisés que vous pouvez réutiliser sur votre site. Ils peuvent être aussi simples que du texte, des images ou des décorations visuelles. Vous pouvez les pousser plus loin et créer des composants interactifs, des widgets complexes ou des applications web entières.

Vous n'êtes pas seulement limité à les utiliser dans vos projets, mais vous pouvez les publier et permettre à d'autres développeurs de les utiliser sur leurs sites.

Voici quelques-uns des composants réutilisables de ma bibliothèque [A2K](https://a2000-docs.netlify.app/). Vous pouvez voir qu'ils viennent dans toutes les formes et tailles, et ont une gamme de fonctionnalités différentes. Les utiliser dans vos projets est similaire à l'utilisation de n'importe quel ancien élément HTML.

![Une petite collection de web components de la bibliothèque A2K](https://www.freecodecamp.org/news/content/images/2023/11/web-components.png)
_Une petite collection de web components de la bibliothèque A2K_

Voici comment vous utiliseriez l'élément de progression dans votre projet :

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Démarrage rapide</title>
		<meta charset="UTF-8" />
	</head>

	<body>
		<!-- Utilisez les web components dans votre HTML comme des éléments intégrés réguliers. -->
		<a2k-progress progress="50" />

		<!-- Les web components a2k utilisent des modules JavaScript standard. -->
		<script type="module">
			import 'https://cdn.jsdelivr.net/npm/@a2000/progress@0.0.5/lib/src/a2k-progress.js';
		</script>
	</body>
</html>

```

Une fois que vous avez importé les scripts tiers, vous pouvez commencer à utiliser le composant, `a2k-progress` dans ce cas, comme n'importe quel autre élément HTML.

Si vous construisez vos propres web components, il n'y a pratiquement aucune limite à la complexité que vous pouvez donner à vos éléments personnalisés. 

J'ai récemment créé un web component qui rend un éditeur de code CodeSandbox dans le navigateur. Et parce que c'est un web component, vous pouvez l'utiliser dans n'importe quel framework que vous aimez ! Si vous souhaitez en savoir un peu plus à ce sujet, [vous pouvez lire plus ici](https://component-odyssey.com/articles/00-sandpack-lit-universal).

### Qu'est-ce que le Shadow DOM ?

Si vous avez une connaissance pratique de CSS, vous savez que le CSS vanilla est globalement scopé. Écrire quelque chose comme ceci dans votre global.css :

```css
p {
  color: tomato;
}

```

donnera à tous les éléments `p` une belle couleur orange/rouge, en supposant qu'aucun autre sélecteur CSS plus spécifique ne soit appliqué à un élément `p`.

Prenons ce menu de sélection, par exemple :

![Un composant de menu de sélection avec un design visuel rappelant les anciens systèmes d'exploitation Windows](https://www.freecodecamp.org/news/content/images/2023/11/a2k-select-menu.png)

Il a un caractère distinct qui est déterminé par le design visuel. Vous pourriez vouloir utiliser ce composant, mais si vos styles globaux affectent des choses comme la famille de polices, la couleur ou la taille de la police, cela pourrait causer des problèmes avec l'apparence du composant :

```html
<head>
	<style>
		body {
			color: blue;
			font-size: 12px;
			font-family: system-ui;
		}
	</style>
</head>

<body>
	<a2k-select></a2k-select>
</body>

```

![Le même menu de sélection, mais avec beaucoup de ses caractéristiques distinctives remplacées par le CSS global.](https://www.freecodecamp.org/news/content/images/2023/11/a2k-select-menu-2.png)

C'est là que le Shadow DOM intervient. Le Shadow DOM est un mécanisme d'encapsulation qui empêche le reste du DOM d'interférer avec vos web components. Il garantit que les styles globaux de l'application web n'interfèrent pas avec les composants que vous consommez. Cela signifie également que les développeurs de bibliothèques de composants peuvent créer leurs composants en ayant la certitude qu'ils auront l'apparence et le comportement attendus dans différentes applications web.

Il y a beaucoup plus de nuances en ce qui concerne le Shadow DOM, ainsi que d'autres fonctionnalités que nous n'allons pas aborder dans cet article. Si vous souhaitez en savoir plus sur les web components, j'ai un cours entier ([Component Odyssey](https://component-odyssey.com/)) dédié à vous apprendre à construire des composants réutilisables qui fonctionnent dans n'importe quel framework.

### Modèles HTML

La dernière fonctionnalité de notre tour d'horizon des fonctionnalités des web components est les modèles HTML.

Ce qui distingue cet élément HTML des autres éléments, c'est que le navigateur ne rend pas son contenu sur la page. Si vous deviez écrire le HTML suivant, vous ne verriez pas le texte "Je suis un en-tête" affiché sur la page :

```html
<body>
	<template>
		<h1>Je suis un en-tête</h1>
	</template>
</body>

```

Au lieu d'être utilisé pour rendre le contenu directement, le contenu du modèle est conçu pour être copié. Le modèle copié peut ensuite être utilisé pour rendre le contenu sur la page. 

Vous pouvez penser à l'élément de modèle comme au modèle pour une impression 3D. Le modèle n'est pas une entité physique, mais il est utilisé pour créer des clones dans la vie réelle.

Vous feriez ensuite référence à l'élément de modèle dans votre web component, le cloneriez et rendriez le clone comme le balisage pour votre composant.

Je ne vais pas passer plus de temps sur ces fonctionnalités des web components, mais vous avez probablement déjà remarqué que pour écrire des web components vanilla, il y a beaucoup de nouvelles fonctionnalités du navigateur que vous devez connaître et comprendre. 

Vous verrez dans la section suivante que le modèle mental pour construire des web components ne semble pas aussi rationalisé que pour les autres frameworks de composants.

## Comment construire un Web Component de base

Maintenant que nous avons brièvement couvert les technologies fondamentales alimentant un web component, voici comment construire un composant _hello world_ :

```javascript
const template = document.createElement('template');
template.innerHTML = `<p>Bonjour le monde</p>`;

class HelloWorld extends HTMLElement {
	constructor() {
		super();
		this.attachShadow({ mode: 'open' });
		this.shadowRoot.append(template.content.cloneNode(true));
	}
}

customElements.define('hello-world', HelloWorld);

```

C'est le composant le plus simple que vous puissiez écrire, mais il y a déjà tant de choses qui se passent. Pour quelqu'un qui est complètement nouveau dans les web components, et sans les connaissances de base que j'ai fournies ci-dessus, il sera laissé avec beaucoup de questions et beaucoup de confusion.

Pour moi, il y a au moins deux raisons principales pour lesquelles les web components peuvent être difficiles à écrire, au moins dans le contexte des exemples hello world.

### Le balisage est découplé de la logique du composant

Dans de nombreux frameworks, le balisage du composant est souvent traité comme un citoyen de première classe. Il est souvent le contenu qui est retourné par la fonction du composant, ou a un accès direct à l'état du composant, ou dispose d'utilitaires intégrés pour aider à manipuler le balisage (comme les boucles, les conditionnelles, etc.).

Ce n'est pas le cas pour les web components. En fait, le balisage est souvent défini en dehors de la classe du composant. Il n'y a également aucun moyen intégré pour que le modèle référence l'état actuel du composant. Cela devient une limitation fastidieuse à mesure que la complexité d'un composant augmente.

Dans le monde du frontend, les composants sont conçus pour aider les développeurs à réutiliser le balisage dans plusieurs pages. Par conséquent, le balisage et la logique du composant sont inextricablement liés, et ils devraient donc être colocataires l'un de l'autre.

### L'écriture d'un web component nécessite la compréhension de toutes ses technologies sous-jacentes

Comme nous l'avons vu ci-dessus, les web components sont composés de trois technologies. Vous pouvez également voir dans l'extrait de code hello world, que nous devons explicitement connaître et comprendre ces trois technologies.

1. Nous créons un **élément de modèle** et définissons son HTML interne
2. Nous créons une **racine d'ombre**, et définissons explicitement son mode sur 'open'.
3. Nous clonons notre **modèle** et l'ajoutons à notre **racine d'ombre**
4. Nous enregistrons un nouvel **élément personnalisé** dans le document

Il n'y a rien de fondamentalement faux à cela, puisque les web components sont censés être une API de navigateur de "niveau inférieur", ce qui les rend idéaux pour construire des abstractions par-dessus. Mais pour un développeur venant d'un environnement React ou Svelte, devoir comprendre ces nouvelles fonctionnalités du navigateur, puis devoir écrire des composants avec elles peut sembler trop de friction.

## Des Web Components plus avancés

Examinons un web component plus avancé, un bouton compteur.

![Un simple bouton compteur. Il y a un bouton cliquable, et du texte montrant combien de fois le bouton a été cliqué](https://www.freecodecamp.org/news/content/images/2023/11/counter-button.png)

Vous cliquez sur le bouton, et le compteur s'incrémente.

L'exemple suivant contient quelques concepts supplémentaires de web components, comme les fonctions de cycle de vie et les attributs observables. Vous n'avez pas besoin de comprendre tout ce qui se passe dans l'extrait de code. Cet exemple est vraiment seulement utilisé pour illustrer combien de code boilerplate est nécessaire pour les interfaces interactives les plus basiques, un bouton compteur :

```javascript
const templateEl = document.createElement("template");

templateEl.innerHTML = `
<button>Appuyez sur moi !</button>
<p>Vous avez appuyé sur moi 0 fois.</p>
`;

export class OdysseyButton extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.shadowRoot.appendChild(templateEl.content.cloneNode(true));
    this.button = this.shadowRoot.querySelector("button");
    this.p = this.shadowRoot.querySelector("p");
    this.setAttribute("count", "0");
  }

	// Note : Les web components ont des méthodes de cycle de vie,
  // Si nous définissons des écouteurs d'événements lorsque le composant est ajouté au DOM, c'est à nous de les nettoyer
  // lorsqu'il est retiré du DOM
  connectedCallback() {
    this.button.addEventListener("click", this.handleClick);
  }

  disconnectedCallback() {
    this.button.removeEventListener("click", this.handleClick);
  }

  // Contrairement aux frameworks comme React, les Web Components ne se rerendent pas automatiquement lorsqu'une prop (ou attribut)
  // change. Au lieu de cela, nous devons définir explicitement quels attributs nous voulons observer.
  static get observedAttributes() {
    return ["disabled", "count"];
  }

  // Lorsque l'un des attributs ci-dessus change, cette méthode de cycle de vie s'exécute, et nous pouvons
  // réagir à la nouvelle valeur de l'attribut en conséquence.
  attributeChangedCallback(name, _, newVal) {
    if (name === "count") {
      this.p.innerHTML = `Vous avez appuyé sur moi ${newVal} fois.`;
    }
    if (name === "disabled") {
      this.button.disabled = true;
    }
  }

  // En HTML, les valeurs des attributs sont toujours des chaînes de caractères. Cela signifie que c'est à nous de
  // convertir les types. Vous pouvez voir ci-dessous que nous convertissons une chaîne -> nombre, puis de nouveau en chaîne
  handleClick = () => {
    const counter = Number(this.getAttribute("count"));
    this.setAttribute("count", `${counter + 1}`);
  };

```

En tant qu'auteurs de web components, nous devons considérer beaucoup de choses :

* Configurer le shadow DOM
* Configurer les modèles HTML
* Nettoyer les écouteurs d'événements
* Définir les propriétés que nous voulons observer
* Réagir aux propriétés lorsqu'elles changent
* Gérer les conversions de type pour les attributs

Et il y a encore tant d'autres choses à considérer que je n'ai pas abordées dans cet article.

Cela ne signifie pas que les web components sont mauvais et que vous ne devriez pas les écrire. En fait, je dirais que vous apprenez tellement sur la plateforme du navigateur en les utilisant. 

Mais je pense qu'il existe de meilleures façons d'écrire des composants si votre priorité est d'écrire des composants interopérables de manière beaucoup plus rationalisée et ergonomique.

## Comment écrire des Web Components avec moins de code boilerplate

Comme je l'ai mentionné précédemment, il existe de nombreux outils pour faciliter l'écriture de web components. 

Un tel outil s'appelle Lit, qui est développé par une équipe chez Google. [Lit](https://lit.dev/) est une bibliothèque légère conçue pour simplifier l'écriture de web components, en supprimant le besoin de code boilerplate que nous avons déjà vu ci-dessus.

Comme nous allons le voir, Lit fait beaucoup de travail sous le capot pour aider à réduire le nombre total de lignes de code de près de moitié ! Et parce que Lit est un wrapper autour des web components et d'autres fonctionnalités natives du navigateur, toutes vos connaissances existantes sur les web components sont transférables.

Pour commencer à voir comment Lit simplifie vos web components. Voici l'exemple **hello world** de tout à l'heure, mais refactorisé pour utiliser Lit au lieu d'un web component vanilla :

```javascript
import { LitElement, html } from "lit";

export class HelloWorld extends LitElement {
  render() {
    return html`<p>Bonjour le monde !</p>`;
  }
}`

customElements.define('hello-world', HelloWorld);

```

Il y a beaucoup moins de code boilerplate avec le composant Lit, et Lit gère les deux problèmes que j'ai mentionnés précédemment, un peu différemment. Voyons comment :

1. Le balisage est directement défini à partir de la classe du composant. Bien que vous puissiez définir vos modèles en dehors de la classe, il est courant de retourner le modèle à partir de la fonction `render`. Cela est plus en ligne avec le modèle mental présenté dans d'autres frameworks UI, où l'UI est une fonction de l'état.
2. Lit ne nécessite pas non plus des développeurs d'attacher le shadow DOM, ou de créer des modèles et de cloner des éléments de modèle. Bien que la compréhension des fonctionnalités sous-jacentes des web components aidera lors du développement de composants Lit, elles ne sont pas requises pour commencer, donc la barrière à l'entrée est beaucoup plus basse.

Alors maintenant pour la grande finale, à quoi ressemble le composant compteur une fois que nous l'avons migré vers Lit ?

```javascript
import { LitElement, html } from "lit";

export class OdysseyCounter extends LitElement {
  static properties = {
		// Nous définissons les propriétés du composant ainsi que leur type.
		// Ces propriétés déclencheront le rerendu du composant lorsque leurs valeurs changent.
		// Bien qu'ils ne soient pas les mêmes, vous pouvez penser à ces "propriétés" comme étant
		// les alternatives de Lit aux "attributs observés"
		// Si la valeur est passée en tant qu'attribut, Lit convertit la valeur
		// au type correct
    count: { type: Number },
    disabled: { type: Boolean },
  };

  constructor() {
    super();
		// Il n'est pas nécessaire de créer un shadow DOM, de cloner le modèle,
		// ou de stocker des références à nos nœuds DOM.
    this.count = 0;
  }

  onCount() {
    this.count = this.count + 1;
  }

  render() {
		// Au lieu d'utiliser la méthode de cycle de vie attributeChangedCallback,
		// la fonction render a accès à toutes les propriétés du composant,
		// ce qui simplifie le processus de manipulation de nos modèles.
    return html`
      <button ?disabled=${this.disabled} @click=${this.onCount}>
        Appuyez sur moi !
      </button>
      <p>Vous avez appuyé sur moi ${this.count} fois.</p>
    `;
  }
}`

```

La quantité de code que nous écrivons est réduite de presque moitié ! Et cette différence devient plus notable lors de la création d'interfaces utilisateur plus complexes.

## Pourquoi je parle tant de Lit ?

Je suis un grand croyant des web components, mais je reconnais que la barrière à l'entrée est élevée pour de nombreux développeurs. Écrire des web components complexes nécessite de comprendre de nombreuses fonctionnalités du navigateur et l'éducation autour des web components n'est pas aussi complète que pour d'autres technologies, comme React ou Vue.

C'est pourquoi je pense qu'il est important d'utiliser des outils comme Lit qui peuvent rendre l'écriture de web components performants et interopérables beaucoup plus facile. C'est génial si vous voulez que vos composants fonctionnent dans n'importe quel framework frontend.

Si vous souhaitez en savoir encore plus, c'est l'approche que j'enseigne dans mon prochain cours [Component Odyssey](https://component-odyssey.com/). Ce cours est excellent pour toute personne qui souhaite comprendre comment écrire des composants qui fonctionnent dans n'importe quel framework. 

Je fais cela en couvrant les bases absolues des web components, avant de passer à des outils comme Lit qui simplifient le processus d'écriture des web components sans compliquer votre environnement de développement. À la fin, vous apprendrez à construire et publier une bibliothèque de composants qui fonctionne dans n'importe quel framework frontend.

Si vous voulez des codes de réduction early-bird pour Component Odyssey, alors rendez-vous [sur le site pour être notifié](https://component-odyssey.com/subscribe).