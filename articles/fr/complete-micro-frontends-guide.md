---
title: Le Guide de l'Architecture Micro-Frontend
subtitle: ''
author: Andrew Maksimchenko
co_authors: []
series: null
date: '2025-06-06T10:21:20.198Z'
originalURL: https://freecodecamp.org/news/complete-micro-frontends-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748915817752/b35a8786-9aa7-46cd-a1d8-f82069470496.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
- name: Frontend Development
  slug: frontend-development
- name: webdev
  slug: webdev
- name: System Design
  slug: system-design
seo_title: Le Guide de l'Architecture Micro-Frontend
seo_desc: Learn how to build scalable, framework-agnostic micro frontends using Web
  Components, Module Federation, Single-SPA, and more — with real-world code.
---

Au fil des années, en tant que développeur full-stack principal, architecte de solutions et mentor, j'ai été immergé dans le monde de l'architecture micro frontend, travaillant sur différents projets frontend à grande échelle où plusieurs équipes, stacks et pipelines de déploiement devaient coexister d'une manière ou d'une autre.

À mesure que les projets gagnaient en complexité et que les équipes travaillaient en parallèle sur différentes stacks, il est devenu clair que les approches monolithiques ne pouvaient pas suivre. J'avais besoin d'outils pratiques qui permettaient une interaction facile entre les applications, un déploiement indépendant, une meilleure autonomie des équipes, une agnosticité des frameworks, et plus encore. Certaines solutions fonctionnaient élégamment en théorie mais peinaient dans des conditions réelles. D'autres rendaient les choses plus désordonnées et plus douloureuses qu'utile.

Après m'être plongé dans différents paradigmes - des iframes aux Web Components, en passant par single-spa, Module Federation, Piral, Luigi et des configurations hybrides - j'ai même distillé mon expérience éprouvée dans un cours en ligne complet sur Udemy.

Et aujourd'hui, dans ce tutoriel pratique complet, je souhaite partager mon expertise et vous en dire plus sur l'architecture micro-frontend - méthode par méthode - avec du code, des compromis, des visuels et des insights du monde réel.

## Table des Matières

* [À quoi servent les Micro Frontends ?](#heading-a-quoi-servent-les-micro-frontends)
    
* [Méthode #1 : Iframes & Messagerie Inter-Fenêtres](#heading-method-1-iframes-amp-messagerie-inter-fenetres)
    
* [Méthode #2 : Web Components (Éléments Personnalisés + Shadow DOM)](#heading-method-2-web-components-elements-personnalises-shadow-dom)
    
* [Méthode #3 : Single-SPA - L'Approche Meta-Framework](#heading-method-3-single-spa-lapproche-meta-framework)
    
* [Méthode #4 : Module Federation - Partage de Code à l'Exécution](#heading-method-4-module-federation-partage-de-code-a-lexecution)
    
* [Autres Outils & Ajouts à l'Écosystème](#heading-other-tools-amp-ajouts-a-lecosysteme)
    
* [Réflexions Finales](#heading-reflexions-finales)
    

## À quoi servent les Micro Frontends ?

Dans le développement frontend traditionnel, nous construisons souvent des applications monolithiques uniques - un codebase, un dépôt, un pipeline de déploiement, une équipe. Cela fonctionne très bien pour les petits et moyens projets, parfois même pour les plus grands.

![Diagramme d'Application Monolithique - Trois Fonctionnalités en React](https://cdn.hashnode.com/res/hashnode/image/upload/v1748770222181/fb73c7ce-366f-4897-9ab7-b208c6e37cfa.png align="center")

Mais des défis apparaissent lorsque :

* Votre codebase frontend s'étend au-delà de 50+ composants.
    
* Plusieurs équipes de développement ont besoin d'autonomie sur différentes parties et stacks techniques.
    
* Différentes sections nécessitent des fréquences de déploiement variées (hebdomadaires ou mensuelles).
    
* Vous devez intégrer des frameworks divers, comme combiner des fonctionnalités React avec un CMS basé sur Angular.
    

C'est là que les micro frontends interviennent.

Les micro frontends étendent les principes des microservices au monde du frontend. Au lieu d'une grande application frontend, vous construisez des modules frontend indépendants, chacun possédé par une équipe, utilisant sa propre stack technique, déployés séparément et intégrés à l'exécution.

![Diagramme d'Application Micro-Frontends - Trois Apps en React, Angular, Vue](https://cdn.hashnode.com/res/hashnode/image/upload/v1748770253697/c78a8d84-a6a9-42af-90fd-423983c7ec77.png align="center")

Pensez-y comme à des blocs Lego :

* Chaque bloc est similaire à un micro frontend autonome.
    
* Ils s'intègrent dans une mise en page ou une coque partagée.
    
* Chacun peut évoluer, se mettre à jour ou être remplacé sans affecter les autres.
    

Par exemple, imaginez que vous construisez un site de commerce électronique moderne, et voici ce que votre côté business attend de vous :

| `Section` | `Équipe` | `Stack` | `Déploiement` |
| --- | --- | --- | --- |
| Liste des Produits | Équipe de Recherche | React | Hebdomadaire |
| Détails du Produit | Équipe Catalogue | Angular | Mensuel |
| Panier & Paiement | Équipe Paiement | Vue | Bimensuel |
| Pages CMS | Équipe Marketing | Vanilla JS | Quotidien |

Chaque équipe veut de l'autonomie, et avec les micro frontends, chacune de ces sections devient une application séparée, chargée dynamiquement dans une coque à l'exécution.

### Pourquoi cela devient-il populaire ?

Voici quelques points que tout le monde considère :

1. **Déploiements indépendants** - Peu ou pas d'effort pour coordonner chaque release.
    
2. **Autonomie des équipes** - Les équipes choisissent leur propre stack et outils sur le projet.
    
3. **Mises à jour incrémentielles** - Migrer les applications héritées pièce par pièce de manière incrémentielle sans avoir besoin de réécrire toute l'application en une fois.
    
4. **Agnosticisme technique** - Vue, React, Angular ? Peu importe. Ils peuvent tous travailler ensemble de manière transparente au même moment dans une seule application.
    
5. **Meilleure scalabilité** - Paralléliser le travail entre les équipes pour permettre une efficacité de livraison et une mise à l'échelle facile.
    

Maintenant, découvrons comment nous pouvons donner vie à cette idée dans nos projets.

De nos jours, il existe différentes façons d'y parvenir, mais toutes les solutions ne se valent pas. La méthode d'implémentation que vous choisissez affectera considérablement :

* L'expérience des développeurs
    
* Les tailles des bundles et les performances
    
* Le SEO et l'accessibilité
    
* La stabilité à l'exécution
    
* L'interopérabilité entre les stacks
    

Commençons donc par explorer la méthode la plus ancienne, mais toujours surprenamment viable.

## **Méthode #1 : Iframes & Messagerie Inter-Fenêtres**

Vous pourriez demander : « Les iframes ne sont-elles pas mauvaises ? » Elles sont souvent mal comprises. Bien que les iframes puissent sembler lourdes et isolées, elles sont aussi le moyen le plus sécurisé et découplé d'héberger des micro frontends - surtout lorsque vous ne faites pas confiance à l'équipe de l'autre côté.

![Méthode Micro-Frontend 1 - Iframes](https://cdn.hashnode.com/res/hashnode/image/upload/v1748770863603/9daefd01-22ac-413f-bf54-c339bb6e4e9e.png align="center")

### **Qu'est-ce qu'un IFRAME ?**

Un [**iframe**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe) (inline frame) est un élément HTML qui vous permet d'intégrer une autre page HTML dans votre page web actuelle. Toute la communication entre les applications est strictement basée sur des événements et livrée par le biais de l'**API Post Message**.

Si vous devez envoyer des données à une autre application, vous appelez simplement la méthode `postMessage()` sur cet élément. De l'autre côté, pour recevoir un message, vous devez simplement vous abonner à l'événement `message`. C'est tout.

### Exemple du Monde Réel

Voyons un exemple simple de deux applications communiquant entre elles en utilisant des `iframes` sur deux applications :

* L'Application Web Principale
    
* Une Application de Recherche.
    

Chaque iframe doit être hébergée quelque part pour servir du contenu statique. Cela peut être AWS Amplify, Digital Ocean, Heroku, GitHub Pages, ou similaire.

Pour vous aider ici, voici un guide officiel GitHub expliquant comment héberger un site web sur leur plateforme : [https://pages.github.com](https://pages.github.com).

Disons que vous avez déployé une Application de Recherche sur GitHub Pages et que vous avez reçu cette URL pour héberger votre application : [`https://example.github.io`](https://search.example.com). Maintenant, écrivons un peu de contenu pour celle-ci.

En supposant que vous souhaitez poster des messages de l'Application de Recherche à l'Application Web Principale, et vous abonner aux messages entrants de celle-ci. Vous pouvez le faire de cette manière :

```javascript
console.log('Initialisation de l\'Application de Recherche...');

// S'abonner aux messages provenant de l'extérieur de l'iframe (comme l'Application Web Principale)
window.addEventListener('message', (event) => {
  if (event.data?.type === 'init') {
    console.log('L\'Application Web Principale a passé userId:', event.data.userId);
  }
});

// Simuler l'envoi des résultats de recherche à l'Application Web Principale
window.parent.postMessage({
  type: 'searchResult',
  payload: ['Item A', 'Item B']
}, '*');
```

Ici, vous initialisez l'application de recherche et configurez une communication bidirectionnelle avec une application parente (comme une application web principale) en utilisant l'**API Post Message**. Vous écoutez les messages entrants en utilisant l'événement intégré `message`. Une fois reçu, ce message devient disponible dans l'objet `event.data`. Enfin, vous simulez l'envoi de données à la parente en postant un message `searchResult` contenant une liste d'items. Cette configuration permet aux applications basées sur des iframes isolées de communiquer en toute sécurité avec l'application shell principale.

Ensuite, dans le DOM de l'application web principale, vous devez inclure l'iframe qui rendra l'application de recherche, en spécifiant l'URL de l'application de recherche hébergée de cette manière :

```xml
<iframe
  id="search-mfe"
  src="https://example.github.io"
  style="width: 100%; height: 200px; border: none;"
></iframe>
```

Des styles ont été ajoutés ici pour garantir que l'`iframe` s'affiche de manière transparente dans la mise en page pour une intégration UI plus propre.

Et maintenant, vous pouvez transmettre du contenu de l'application web principale à l'application de recherche et obtenir des messages de celle-ci. Vous pouvez l'accomplir dans le code JavaScript de l'application web principale de cette manière :

```javascript
console.log('Initialisation de l\'Application Web Principale...');
	
const iframe = document.getElementById('search-mfe');
iframe.onload = () => {
  // Envoyer un message à l'iframe enfant (entrées)
  iframe.contentWindow.postMessage({ type: 'init', userId: 42 }, '*');
};

window.addEventListener('message', (event) => {
  // Recevoir des données de l'Application de Recherche (sorties)
  if (event.data?.type === 'searchResult') {
    console.log('Résultat reçu de l\'Application de Recherche : ', event.data.payload);
  }
});
```

Comme vous le voyez, lorsque l'`iframe` se charge, l'événement `init` est envoyé à l'application de recherche (le `type` peut être n'importe quoi, assurez-vous simplement qu'il correspond à celui que l'autre application attend de vous). Ensuite, dans le gestionnaire d'événements `message` comme avant, vous pouvez recevoir les messages entrants de l'application de recherche et faire quelque chose avec eux.

Voici quelques avantages et inconvénients à considérer, ainsi que des cas d'utilisation populaires :

### **✅ Avantages :**

* **Sandboxing fort** : Pas de mémoire partagée, pas de styles partagés.
    
* **Zéro conflits de dépendances** : Un iframe équivaut à un environnement.
    
* **Parfait pour le legacy** : Facile à envelopper les anciennes applications dans un iframe.
    
* **Pratique** pour les micro-apps en PHP, Java, Razor (ASP.NET)
    

### **❌ Inconvénients :**

* Rendu lent
    
* Navigation partagée difficile
    
* Styling incohérent/compliqué
    
* Communication complexe
    
* Doit être hébergé quelque part
    

### **👨🏻‍💻 Cas d'Utilisation Populaires**

* Intégration de tableaux de bord legacy (par exemple, anciennes applications AngularJS ou Java)
    
* Applications cross-domain sécurisées (par exemple, paiements, analytique tiers)
    
* Intégrations hautement non fiables
    
* Publicités intégrées
    

Mais si vous voulez une UX plus fluide, des composants partagés et une meilleure expérience de développement, vous voudrez quelque chose de mieux. Cela nous amène aux Web Components.

## **Méthode #2 : Web Components (Éléments Personnalisés + Shadow DOM)**

> « Et si vous pouviez livrer un widget autonome compris nativement qui fonctionne dans n'importe quel framework - React, Vue, Angular, ou même du HTML simple ? »

C'est exactement ce que les [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) rendent possible. Ils sont intégrés nativement dans le navigateur en tant qu'[API](https://developer.mozilla.org/en-US/docs/Web/API/Web_components), vous n'avez pas besoin de framework ou de dépendance supplémentaire. Ils vous permettent de créer des éléments UI réutilisables, évolutifs et encapsulés qui fonctionnent comme des balises HTML natives.

![Méthode Micro-Frontend 2 - Web Components](https://cdn.hashnode.com/res/hashnode/image/upload/v1748773939725/8b017162-96a8-449d-b9b8-5fe8ef382e91.png align="center")

De plus, vous pouvez facilement les utiliser comme enveloppes autour de n'importe quel élément d'autres frameworks UI (React, Angular, Svelte, etc.) et utiliser vos composants basés sur des frameworks comme des éléments DOM natifs réguliers dans n'importe quelle application web.

Ils sont, à bien des égards, la base idéale pour les micro frontends.

Un composant web est composé de :

* **Custom Element** - définit votre propre balise HTML (&lt;user-profile&gt;) et comportement
    
* **Shadow DOM** – fournit des styles et une structure DOM encapsulés
    
* **HTML Template** – apporte des blocs/fragments HTML réutilisables
    
* **Slots** – agit comme des zones de remplacement pour le contenu de l'hôte (utilisé dans la projection de contenu)
    

![Méthode Micro-Frontend 2 - Blocs Clés des Web Components](https://cdn.hashnode.com/res/hashnode/image/upload/v1748772947093/6090d9bb-2c10-4a92-9ece-c5235b8382a2.png align="center")

Dans les composants web, vous devez synchroniser les données (entrée/sortie) via :

* **Attributs** (entrées) :
    
    * En JavaScript : `element.setAttribute()`, `element.getAttribute()`, etc.
        
    * En HTML : `<element attr1="value1" attr2="value2"></element>`
        
* **Propriétés** (entrées) – `element.someProp = value` (uniquement JavaScript)
    
* **Événements Personnalisés** (sorties) - `new CustomEvent('name', data)`
    

Tout d'abord, laissez-moi vous montrer une implémentation de base d'un composant web, puis vous apprendrez comment l'exploiter pour les micro-frontends.

En supposant que vous construisez un composant product-tile réutilisable qui doit :

* Accepter un paramètre d'entrée – "title"
    
* Envoyer un événement de sortie "add-to-cart" avec ce "title" au monde extérieur, lorsque le composant est monté dans le DOM.
    

Voici à quoi pourrait ressembler ce composant web :

```javascript
// product-tile.js
class ProductTile extends HTMLElement {
  // Spécifier quels attributs (entrées) observer pour les changements
  static get observedAttributes() { return ['title']; }

  constructor() {
      super(); // Appeler le constructeur de base HTMLElement (obligatoire)
      // Créer un Shadow DOM pour l'encapsulation des styles et du DOM
      const shadow = this.attachShadow({ mode: 'open' });
      // Remplir le Shadow DOM avec un conteneur DIV où React rendra le lecteur
      shadow.innerHTML = `<div id="title"></div>`;
  }

  // Réaction de cycle de vie intégrée.
  // Appelée lorsque l'élément personnalisé ProductTile est ajouté au DOM
  connectedCallback() {
      // Lorsque ajouté au DOM, lire et rendre l'attribut title
      const title = this.getAttribute('title') ?? 'Produit Sans Nom';
      this.updateTitle(title);

      // Dispatcher un événement personnalisé avec le titre actuel
      const event = new CustomEvent('add-to-cart', {
          detail: { title },
          bubbles: true,
          composed: true,
      });

      this.dispatchEvent(event);
  }

  // Réaction de cycle de vie intégrée.
  // Appelée chaque fois que les attributs observés changent.
  // Dans notre cas, c'est uniquement "title"
  attributeChangedCallback(name, oldValue, newValue) {
      if (name === 'title' && oldValue !== newValue) {
          this.updateTitle(newValue);
      }
  }

  // Méthode interne pour mettre à jour le contenu du titre en toute sécurité
  updateTitle(title) {
      const titleElem = this.shadowRoot.querySelector('#title');
      titleElem.textContent = title;
  }
}

customElements.define('product-tile', ProductTile);
```

Maintenant, laissez-moi vous expliquer ce qui se passe ici :

* Tout d'abord, vous créez une classe d'élément personnalisé qui étend `HTMLElement` ou ses enfants. Cela vous donne accès aux hooks de cycle de vie des composants web et aux capacités d'intégration DOM.
    
* Si vous souhaitez réagir aux changements des paramètres d'entrée (attributs), vous devez définir un getter statique `observedAttributes()` qui retourne une liste de noms d'attributs à surveiller. Dans notre cas, nous observons "title".
    
* Ensuite, dans le constructeur :
    
    * Appelez `super()` pour hériter correctement de `HTMLElement`.
        
    * Créez un DOM shadow en utilisant `attachShadow({ mode: 'open' })`. Cela encapsule le DOM et les styles internes de votre composant. Vous pouvez même utiliser un mode `closed` ici pour ajouter un niveau d'isolation plus élevé au DOM shadow.
        
    * Ensuite, remplissez le DOM shadow avec un HTML interne minimal - dans ce cas, un élément `<div>` qui affichera plus tard le titre du produit.
        
* Lorsque le composant est ajouté au DOM, la réaction de cycle de vie intégrée `connectedCallback()` s'exécute :
    
    * Il lit la valeur actuelle de l'attribut "title".
        
    * Met à jour l'UI avec une valeur initiale dans l'attribut "title".
        
    * Ensuite, il envoie un événement personnalisé nommé "add-to-cart", transmettant le "title" comme détail. Les événements sont `bubbles: true` et `composed: true`, de sorte que les éléments parents ou les applications hôtes en dehors du DOM shadow peuvent s'y abonner et les capturer.
        
* Lorsque l'attribut title change à l'exécution, une autre réaction de cycle de vie intégrée nommée `attributeChangedCallback()` s'exécute automatiquement :
    
    * Il vérifie la nouvelle valeur et met à jour l'affichage du "title" en conséquence.
        
    * Cela permet un comportement réactif dans le composant - similaire aux liaisons d'entrée dans les frameworks UI.
        
* Enfin, vous enregistrez le composant globalement en utilisant la méthode `customElements.define()` (elle est disponible dans l'objet global `window`), en lui donnant :
    
    * Un nom de balise `<product-tile>` qui peut être utilisé n'importe où en HTML.
        
    * Une `référence` à l'élément personnalisé que vous avez précédemment créé pour associer l'un à l'autre.
        

En fin de compte, voici comment vous pouvez utiliser ce composant dans vos applications, qui fonctionnera en vanilla JS, React, Angular, Svelte, Vue, quel que soit le framework UI que vous choisissez :

```xml
<product-tile title="Mug à Café"></product-tile>
```

Et ensuite, vous pouvez écouter l'événement "add-to-cart" depuis l'intérieur du composant `ProductTile` comme ceci :

```javascript
const elem = document.querySelector('product-tile');
elem.addEventListener('add-to-cart', e => {
  console.log('Ajouter au panier !', e.detail);
});
```

Comme vous le voyez, pas de `ReactDOM.render`, pas de `NgModule`, pas de colle supplémentaire. Tout est entièrement natif, du code **JavaScript** pur que les navigateurs comprennent.

Et maintenant, grâce au Shadow DOM et à d'autres fonctionnalités des Web Components, vous pouvez facilement envelopper et intégrer n'importe quelle application web écrite dans un framework différent dans le Shadow Tree qui isolera entièrement votre application et n'autorisera pas sa mise en page ou ses styles à fuir.

Alternativement, si vous décidez de le publier en tant que package npm séparé (par exemple, `@webcomp/product-tile`), vous pouvez même importer et monter dynamiquement le Web Component comme ceci :

```javascript
import('@webcomp/product-tile').then(() => {
  // Maintenant <product-tile> est défini - vous pouvez le créer et l'utiliser
  const elem = document.createElement('product-tile');
  elem.setAttribute('title', 'Souris Sans Fil');
  document.body.appendChild(elem);
});
```

Ou le charger depuis un CDN ou tout fournisseur d'hébergement :

```jsx
<script type="module" src="https://example.github.io/product-tile.js"></script>
```

C'est simple, propre et indépendant.

Mais vous n'êtes pas ici juste pour cela, n'est-ce pas ? :) Maintenant, apprenons la vraie puissance des Web Components dans un monde de micro-frontends !

### **Micro-Frontends avec Web Components**

Imaginez que vous avez construit un Lecteur Vidéo en React - ou peut-être souhaitez réutiliser celui d'une autre équipe. Maintenant, la question est : Comment pouvez-vous rendre ce lecteur basé sur React utilisable dans n'importe quelle autre application frontend, indépendamment de son framework sous-jacent, en utilisant les Web Components ?

Découvrons-le !

![Méthode Micro-Frontend 2 - Web Components - Exemple du Monde Réel](https://cdn.hashnode.com/res/hashnode/image/upload/v1748785841227/e58d9ffd-3098-4652-ae52-a55ab218c8fd.png align="center")

Disons que ce lecteur vidéo :

* Accepte `src` et `controls` comme entrées
    
* Émet des événements : `play` et `pause` comme sorties
    
* Peut être utilisé dans n'importe quelle application via `<magic-player>` de cette manière :
    
    ```xml
    <magic-player
      src="https://cdn.example.com/video.mp4"
      controls="true"
    ></magic-player>
    ```
    

Passons maintenant à l'implémentation !

**🔹 Étape #1 : Inclure votre lecteur React dans le projet**

Ici, vous pouvez jouer avec n'importe quel composant React de votre choix, ou vous pouvez simplement utiliser un Lecteur Vidéo React simple comme celui ci-dessous :

```javascript
// ReactVideoPlayer.jsx

import React from 'react';

export function ReactVideoPlayer({ src, controls, onPlay, onPause }) {
  return (
	  // Élément vidéo HTML5 avec largeur complète et contrôles activés
    <video
      width="100%"
	  controls={controls}  {/* Activer / Désactiver les contrôles */}
      onPlay={onPlay}      {/* Callback pour l'événement play */}
      onPause={onPause}    {/* Callback pour l'événement pause */}
    >
      <source src={src} type="video/mp4" />
      Votre navigateur ne supporte pas la balise vidéo.
    </video>
  );
}
```

**🔹 Étape #2 : Créer l'enveloppe du Web Component**

Maintenant, vous devez créer une enveloppe de Web Component autour de cette application de lecteur React en la montant dans le shadow DOM d'un élément personnalisé de cette manière :

```javascript
// magic-player.element.js

// Définir une nouvelle classe d'élément personnalisé
class MagicPlayerElement extends HTMLElement {
  constructor() {
    super(); // Appeler le constructeur de base HTMLElement (obligatoire)
    
    // Créer un Shadow DOM pour l'encapsulation des styles et du DOM
    const shadowRoot = this.attachShadow({ mode: 'open' });
    // Remplir le Shadow DOM avec un conteneur DIV où React rendra le lecteur
    shadowRoot.innerHTML = `
	    <div id="react-video-player"></div>
    `;
  }
}

customElements.define('magic-player', MagicPlayerElement);
```

Ensuite, vous devez ajouter des entrées et des sorties comme ceci :

```javascript
// magic-player.element.js

// Définir une nouvelle classe d'élément personnalisé
class MagicPlayerElement extends HTMLElement {
  // Spécifier quels attributs (entrées) observer pour les changements
  static get observedAttributes() { return ['src', 'controls']; }

  constructor() {
    super(); // Appeler le constructeur de base HTMLElement (obligatoire)
    
    // Créer un Shadow DOM pour l'encapsulation des styles et du DOM
    const shadowRoot = this.attachShadow({ mode: 'open' });
    // Remplir le Shadow DOM avec un conteneur DIV où React rendra le lecteur
    shadowRoot.innerHTML = `
	    <div id="react-video-player"></div>
    `;
  }

  // Méthode de type helper pour dispatcher des événements de type natif (nos sorties)
  // Dans notre cas, elle sera déclenchée pour les événements "onPlay" et "onPause"
  dispatch(eventName, detail = {}) {
	  const event = new CustomEvent(eventName, {
      detail,            // Passer des données personnalisées ("onPlay" ou "onPause")
      bubbles: true,     // Autoriser l'événement à remonter
      composed: true     // Autoriser à traverser la frontière du Shadow DOM
    });
    this.dispatchEvent(event);
  }
}

customElements.define('magic-player', MagicPlayerElement);
```

Et enfin, ajoutez deux réactions de cycle de vie intégrées pour rendre une application de lecteur vidéo React lorsque la page se charge et chaque fois que les entrées changent :

```javascript
// magic-player.element.jsx

// Définir une nouvelle classe d'élément personnalisé
class MagicPlayerElement extends HTMLElement {
  // Spécifier quels attributs (entrées) observer pour les changements
  static get observedAttributes() { return ['src', 'controls']; }

  constructor() {
    super(); // Appeler le constructeur de base HTMLElement (obligatoire)
    
    // Créer un Shadow DOM pour l'encapsulation des styles et du DOM
    const shadow = this.attachShadow({ mode: 'open' });
    // Remplir le Shadow DOM avec un conteneur DIV où React rendra le lecteur
    shadow.innerHTML = `
        <div id="react-video-player"></div>
    `;
  }
  
  // Méthode de type helper pour dispatcher des événements de type natif (nos sorties)
  // Dans notre cas, elle sera déclenchée pour les événements "onPlay" et "onPause"
  dispatch(eventName, detail = {}) {
	  const event = new CustomEvent(eventName, {
      detail,            // Passer des données personnalisées ("onPlay" ou "onPause")
      bubbles: true,     // Autoriser l'événement à remonter
      composed: true     // Autoriser à traverser la frontière du Shadow DOM
    });
    this.dispatchEvent(event);
  }
 
  // Réaction de cycle de vie intégrée.
  // Appelée lorsque l'élément personnalisé <magic-player> est ajouté au DOM
  connectedCallback() {
    this.render();
  }
 
  // Réaction de cycle de vie intégrée.
  // Appelée chaque fois que les attributs observés changent.
  // Dans notre cas, c'est "src" et "controls"
  attributeChangedCallback() {
    this.render();
  }
 
  // Rendre le lecteur React à l'intérieur du conteneur
  render() {
    const src = this.getAttribute('src');
    const controls = this.getAttribute('controls') === 'true';
    const mount = this.shadowRoot.querySelector('#react-video-player');

    ReactDOM.createRoot(mount).render(
      <ReactVideoPlayer
        src={src}
        controls={controls}
        onPlay={() => this.dispatch('play')}
        onPause={() => this.dispatch('pause')}
      />
    );
  }
}

customElements.define('magic-player', MagicPlayerElement);
```

**🔹 Étape #3 : Connecter votre React-Player à n'importe quel framework UI :**

Ensuite, dans l'application web principale (quel que soit le framework UI que vous utilisez). Nous plaçons notre nouvel enveloppeur de lecteur vidéo React à n'importe quel endroit dans le DOM, en passant les attributs initiaux (entrées) :

```xml
<!-- Utilisez votre nouveau lecteur basé sur React n'importe où ! -->
<magic-player
  src="https://cdn.example.com/movie.mp4"
  controls="true"
></magic-player>
```

Et ensuite, vous pouvez facilement vous abonner aux événements personnalisés (sorties) depuis l'intérieur de l'application React :

```javascript
// Écouter les événements de style natif de l'élément personnalisé
const magicPlayer = document.querySelector('magic-player');
magicPlayer.addEventListener('play', () => {
  console.log('La vidéo a commencé à jouer !');
});

magicPlayer.addEventListener('pause', () => {
  console.log('La vidéo a été mise en pause.');
});
```

C'est tout ! Maintenant, essayez d'accomplir la même chose avec un framework **UI** différent !

### **✅ Avantages**

* **Agnostique des frameworks** : Fonctionne dans React, Angular, Vue, Svelte, ou même du HTML simple - pas besoin de réécrire
    
* **Support natif par les navigateurs** : Pas besoin de bibliothèques ou frameworks externes - juste HTML, JS et CSS.
    
* Pas de configuration ou d'hébergement supplémentaire nécessaire comme avec les iframes. Mais les composants peuvent toujours être publiés sur npm/CDNs et réutilisés dans plusieurs applications.
    
* **Communication intuitive et facile** : Exposez les attributs DOM natifs comme entrées et les événements personnalisés natifs comme sorties.
    
* **Compatible SSR avec hydratation** : Il supporte la sérialisation, le shadow DOM déclaratif, et peut être rendu côté serveur et hydraté, surtout en utilisant des outils modernes.
    
* **Supporte l'accessibilité** (attributs et rôles ARIA).
    

### **❌ Inconvénients**

* **Difficultés d'intégration** : Si vous souhaitez connecter deux applications dans des stacks techniques différentes, vous devez gérer correctement leur communication dans une enveloppe d'élément personnalisé et son shadow DOM.
    
* **Support limité pour les anciens navigateurs** : Si vous avez besoin de compatibilité avec des navigateurs legacy comme Internet Explorer 10, les Web Components nécessitent un polyfill. Mais voici un dépôt populaire avec tous les polyfills pour les Web Components : [https://github.com/webcomponents/polyfills](https://github.com/webcomponents/polyfills)
    
* **Isolation de l'état global** : Il n'y a pas de moyen intégré pour partager l'état entre les composants. Vous devrez implémenter votre propre bus global ou pont d'événements en utilisant `CustomEvents` ou similaire.
    

### **👨🏻‍💻 Cas d'utilisation populaires**

* Systèmes de design et bibliothèques UI réutilisables
    
* Micro frontends à l'intérieur des applications de framework
    
* Intégration legacy vers une stack moderne et vice versa
    
* Livraison de composants inter-équipes
    
* UIs plug-and-play basées sur CDN
    

L'API Web Components offre de nombreuses autres possibilités et puissances. Donc, si vous le souhaitez, vous pouvez approfondir et améliorer vos connaissances en passant n'importe quel cours gratuit disponible sur freeCodeCamp ou en suivant celui que j'ai construit moi-même autour de cette technique sur Udemy.

Passons maintenant à la suite !

## **Méthode #3 : Single-SPA - L'Approche Meta-Framework**

> « Et si, au lieu d'intégrer des micro frontends en tant que Web Components ou iframes, nous avions un système qui orchestrerait plusieurs SPAs ensemble dans une seule mise en page ? »

C'est exactement ce que [single-spa](https://single-spa.js.org/) propose. Ce n'est pas une bibliothèque de rendu, c'est un routeur JavaScript et un orchestrateur pour micro frontends.

![Méthode Micro-Frontend 3 - Single SPA](https://cdn.hashnode.com/res/hashnode/image/upload/v1748788736898/90800e32-f8d0-4fc5-aedb-e7ce8d753c4c.png align="center")

> *Source :* [https://single-spa.js.org](https://single-spa.js.org/)

### **Qu'est-ce que single-spa ?**

single-spa (Single Page Application) vous permet de construire et d'exécuter plusieurs SPAs indépendants (React, Vue, Angular, etc.) à l'intérieur d'une seule page web. Chaque SPA est responsable d'une partie de l'UI et est chargé dynamiquement en fonction de la route actuelle.

En bref, c'est un **framework** qui :

* Charge vos micro frontends lorsque nécessaire
    
* Les monte/démonte proprement
    
* Coordonne le routage et les cycles de vie
    
* Supporte différents frameworks dans la même application.
    

### **Exemple concret**

Disons que vous avez cette répartition de routes :

| `Chemin` | `Application Micro Frontend` | `Stack` | `Nom de l'Application` |
| --- | --- | --- | --- |
| /products | Application de Liste des Produits | React | `@shop/products` |
| /checkout | Application de Paiement | Vue | `@shop/checkout` |
| /account | Tableau de Bord du Compte | Angular | `@shop/account` |

Chacun est une **SPA entièrement indépendante**, et single-spa les charge selon les besoins.

**🔹 Étape #1 : Installation de single-spa**

Tout d'abord, vous devez installer single-spa comme dépendance pour votre projet :

```bash
# Créer un nouveau projet (si ce n'est pas déjà fait)
npm init

# Installer Single SPA
npm install single-spa systemjs
```

Remarquez que nous avons également installé le package `systemjs`. Ce package est responsable du chargement dynamique des modules à l'exécution qui permet à Single-SPA de fonctionner de manière transparente. Il utilise `SystemJS` comme chargeur de modules pour permettre aux micro frontends d'être :

1. Chargés à l'exécution
    
2. Déployés indépendamment
    
3. Agnostiques des frameworks
    
4. Chargés paresseusement uniquement lorsque nécessaire
    

Maintenant, vous devez implémenter chaque micro-app. Par exemple, voyons comment l'application `@shop/products` écrite en React pourrait être gérée.

**🔹 Étape #2 : Structure du Projet**

La structure du projet pour chaque micro-app peut ressembler à ceci :

```apache
shop/products/
├── src/
│   ├── root.component.jsx
│   └── index.single-spa.js
├── public/
│   └── index.html
├── package.json
└── webpack.config.js
```

**🔹 Étape #3 : Composant Racine de la Micro App**

Le fichier `root.component.jsx` représente la racine de l'application React qui sera montée dans le DOM principal en utilisant single-spa. Voici un exemple simple :

```jsx
// src/root.component.jsx
import React from 'react';

export default function Root() {
  return (
    <div style={{ padding: '1rem', border: '1px solid #ccc' }}>
      <h2>🏪 Product Micro App</h2>
      <p>This is a micro frontend powered by React + Single-SPA!</p>
    </div>
  );
}
```

**🔹 Étape #4 : Configurer les Hooks de Cycle de Vie**

De plus, chaque Micro App dans single-spa nécessite un point d'entrée avec au moins trois fonctions principales/hooks de cycle de vie. À cette fin, vous aurez besoin d'un fichier séparé, que vous pouvez nommer `index.single-spa.js` et qui fournira l'implémentation de ces hooks, comme :

* `bootstrap()` - Appelé lorsque la micro-app est lancée par l'application principale (Shell) avant le montage dans le DOM
    
* `mount()` - Appelé lorsque l'application est attachée à l'hôte dans le DOM
    
* `unmount()` - Appelé lorsque l'application est supprimée/détachée du DOM
    

Et voici un exemple de ce à quoi ils pourraient ressembler :

```jsx
// src/index.single-spa.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import Root from './root.component.jsx';

// Conserver l'instance racine React pour réutilisation
let root = null;

// Appelé une fois lorsque le micro frontend est initialisé pour la première fois
export function bootstrap() {
  return Promise.resolve();
}

// Appelé chaque fois que la route correspond et que l'application doit apparaître
export function mount(props) {
  return Promise.resolve().then(() => {
    const container = document.getElementById('product-container') || createContainer();
    root = ReactDOM.createRoot(container);
    root.render(<Root />);
  });
}

// Appelé lorsque la route ne correspond plus (nettoyage)
export function unmount() {
  return Promise.resolve().then(() => {
    if (root) {
      root.unmount();
    }
  });
}

// Créer un conteneur div s'il n'existe pas
function createContainer() {
  const div = document.createElement('div');
  div.id = 'product-container';
  document.body.appendChild(div);
  return div;
}
```

Comme vous le voyez, vous devez résoudre une Promesse dans tous les hooks de cycle de vie et vous assurer que l'application React est montée et démontée correctement en fonction des meilleures pratiques de React.

**🔹 Étape #5 : Configurer Webpack pour SystemJS**

De plus, chaque micro-app dans single-spa nécessite une configuration séparée. Pour cela, vous inclurez un fichier `webpack.config.js`, en spécifiant comment construire l'application (`output`), où l'héberger (`publicPath`), et ainsi de suite.

Puisque single-spa utilise le package `SystemJS`, la `libraryTarget` sera `system` pour toutes les micro-apps.

```javascript
// webpack.config.js
module.exports = {
  externals: {
    react: 'React',
    'react-dom': 'ReactDOM',
  },
  output: {
    filename: 'products.js',
    libraryTarget: 'system', // Format compatible SystemJS
    publicPath: 'http://localhost:8500/', // Emplacement d'hébergement de cette micro-app
  },
};
```

Cette application sera hébergée sur [`localhost:8500`](http://localhost:8500). Pour la production, vous devrez utiliser un fournisseur d'hébergement approprié (comme ceux décrits dans la section iframes).

**🔹 Étape #6 : Enregistrer la Micro App dans Root-Config**

Ensuite, il est temps d'enregistrer une nouvelle micro-app dans la configuration racine de Singla-SPA. Voici comment vous pouvez le faire :

Créez un fichier `root-config.js` à la racine du projet et remplissez-le avec ce contenu :

```javascript
// root-config.js (shell hôte)
import { registerApplication, start } from 'single-spa';

registerApplication({
  name: '@shop/products',
  app: () => System.import('@shop/products'),
  activeWhen: ['/products'],
});

start(); // Initialise le routage et les cycles de vie des micro-apps
```

Tout d'abord, vous devez enregistrer l'application, puis la démarrer pour activer le routage et le cycle de vie des micro-apps. L'enregistrement pour les autres micro-apps sera similaire.

**Note** : `System.import()` fait partie de `SystemJS`, utilisé par défaut dans single-spa pour charger des apps distantes.

De plus, single-spa est livré avec ce que l'on appelle des "Parcels" - une construction de niveau inférieur par rapport aux applications. Ce sont essentiellement des morceaux autonomes d'UI que vous pouvez monter dynamiquement n'importe où. Pensez à eux comme des "mini microfrontends" ou des widgets réutilisables qui ne contrôlent pas le routage :

```javascript
// Exemple
mountParcel(SomeParcelComponent, { domElement: document.getElementById('micro-app') });
```

Vous les utiliseriez lorsque :

* Vous ne voulez pas que le parcel possède une route.
    
* Vous devez injecter un micro frontend dynamiquement à l'intérieur d'un autre.
    
* Vous voulez une logique encapsulée (comme un widget) intégrée dans une application plus grande.
    

Dans tous les autres cas, préférez l'utilisation de la fonction `registerApplication(...)`.

**🔹 Étape #7 : Ajouter la Micro App à la Carte d'Import SystemJS**

La dernière étape consiste à enregistrer la micro-app dans `SystemJS`. Pour cela, dans votre fichier `index.html` racine, vous devez ajouter les deux scripts suivants :

```xml
<!-- public/index.html -->

<!DOCTYPE html>
<html lang="en">
<head> <title>Micro Frontend Shell</title> </head>
<body>
  <nav>
    <a href="/products">Products</a> |
    <a href="/checkout">Checkout</a>
  </nav>

  <!-- Import maps géré par le bundler ou injecté à l'exécution -->
  <script type="systemjs-importmap">
    {
      "imports": {
        "@shop/root-config": "http://localhost:9000/root-config.js",
        "@shop/products": "http://localhost:8500/products.js",
        // autres micro apps
      }
    }
  </script>

  <!-- Démarrer l'application root-config -->
  <script>
    System.import('@shop/root-config');
  </script>
</body>
</html>
```

Tout d'abord, vous devez ajouter un script avec une déclaration de carte d'import. Comme vous le voyez, il représente un JSON où :

* Chaque clé est le nom de la micro-app et
    
* Chaque valeur est l'URL où le fichier JS principal (du bundle) vit réellement
    

Notez que nous avons ajouté `@shop/root-config` ici à la carte d'import pour dire à `SystemJS` où récupérer le fichier JavaScript principal pour l'application principale/shell afin qu'il sache comment résoudre et exécuter `System.import('@shop/root-config')` correctement.

Deuxièmement, vous incluez un autre script pour démarrer l'application principale/shell. Il exécute le fichier JS que vous venez de mapper dans la carte d'import ci-dessus. Traitez-le comme le vrai « boot » de votre application shell :

```xml
<script>
  System.import('@shop/root-config');
</script>
```

C'est tout ! Maintenant, allez-y et essayez de faire de même avec d'autres micro-apps en Vue (Checkout App) et Angular (Account Dashboard).

Voici un diagramme simple illustrant cette connexion :

![Méthode Micro-Frontend 3 - Single SPA - Exemple du Monde Réel](https://cdn.hashnode.com/res/hashnode/image/upload/v1748789553598/4729600f-54d7-4d72-97e7-462093cf08b5.png align="center")

Maintenant que vous avez enregistré et intégré votre première micro-app, vous vous demandez peut-être si cette approche est faite pour vous. Examinons rapidement les avantages et les limitations de l'utilisation de single-spa en production.

### **✅ Avantages**

* **Routage et cycles de vie intégrés** - Pas besoin de réinventer la navigation ou la logique de montage
    
* **Support multi-frameworks** - React, Vue, Angular peuvent tous coexister
    
* **Chargement granulaire** - Ne charge que l'application active (paresseux et efficace)
    
* **Structure de projet flexible** - peut être monorepo ou polyrepo
    
* **Bons outils CLI** - créer et lier des MFEs avec create-single-spa & helpers
    

### **❌ Inconvénients**

* **Courbe d'apprentissage complexe** - Les APIs de cycle de vie et `SystemJS` peuvent être intimidants
    
* **Les configurations peuvent devenir verbeuses** - Gérer plusieurs registres, cartes d'import, URLs de déploiement, et enveloppes de cycle de vie entre les applications ajoute une surcharge de configuration
    
* **L'état partagé est manuel** - Vous devez implémenter des solutions d'état global personnalisées
    
* **Difficile à SSR** - Conçu pour un rendu entièrement côté client
    
* **Plus de code boilerplate** - Chaque application a besoin d'enveloppes pour les cycles de vie, le routage, etc.
    
* **Fuites de styles globaux** - Pas d'encapsulation par défaut comme le Shadow DOM
    

Et quelques cas d'utilisation populaires pour cela :

### **👨🏻‍💻 Cas d'utilisation populaires**

Vous pouvez utiliser single-spa lorsque :

* Vous voulez un routeur central gérant tous les micro frontends
    
* Les équipes utilisent différents frameworks
    
* Vous préférez des expériences SPA complètes plutôt que des widgets isolés
    
* Vous ne craignez pas un peu de code boilerplate pour l'orchestration
    
* Vous êtes d'accord avec une configuration purement côté client
    

Passons à la suite !

## **Méthode #4 : Module Federation - Partage de Code à l'Exécution**

> « Et si vos micro frontends pouvaient charger les composants, modules ou bibliothèques les uns des autres à l'exécution - sans iframes, sans cartes d'import, et sans reconditionnement ? »

C'est exactement ce que [Module Federation](https://module-federation.io/), introduit dans [Webpack 5](https://webpack.js.org/blog/2020-10-10-webpack-5-release/), rend possible. C'est relativement nouveau et il permet à plusieurs applications, construites et déployées séparément, de partager des modules en temps réel, via le navigateur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748789750463/ad976d48-f564-4e94-a3ca-c18e9612dc55.png align="center")

> *Source :* [https://module-federation.io/](https://module-federation.io/)

Avec Module Federation, vous pouvez :

* Importer des composants à travers des builds indépendants
    
* Partager React, Vue, ou toute dépendance
    
* Contrôler les versions des modules exposés
    
* Déployer indépendamment, tout en consommant les uns les autres
    

Module Federation est ce qui fait que les micro frontends dans une seule mise en page cohésive se sentent vraiment comme une seule application.

Maintenant, voyons cela en action !

### **Exemple concret**

Supposons que vous devez construire deux applications autonomes :

* Application principale / hôte (shell) - charge les composants des autres (disons qu'elle est en React)
    
* Application distante (product-app) - expose les composants écrits également en React aux autres
    

Module Federation vous permet d'exporter ces composants sans les publier sur NPM ou les envelopper en tant que Web Component. Au lieu de cela, l'application hôte chargera le composant directement à l'exécution à partir du bundle JavaScript compilé.

Voici à quoi pourrait ressembler la structure du projet :

**Application Produit :**

```apache
product-app/                ← Micro Frontend Distant
├── public/
│   └── index.html          ← Point de montage pour le rendu de test local optionnel
├── src/
│   ├── ProductTile.jsx     ← Composant à exposer
│   └── index.js            ← Point d'entrée local optionnel
├── webpack.config.js       ← Expose Product App
├── package.json
└── .babelrc / .gitignore / etc
```

Notez que `webpack.config.js` doit être au niveau racine, comme `package.json`, afin que `Webpack` puisse le localiser automatiquement.

**Application Principale / Hôte (shell) :**

```apache
host-app/                     
├── public/
│   └── index.html        ← Point de montage
├── src/
│   ├── App.jsx           ← Monte ProductTile depuis distant
│   └── bootstrap.js      ← Point d'entrée de l'application
├── webpack.config.js     ← Charge les distants via Module Federation
└── package.json
```

Vous pouvez les garder tous les deux dans un monorepo ou les héberger dans des repos entièrement différents.

🔹 **Étape #0 : Initialiser les projets (Hôte + Applications Produit)**

Si vous savez comment le faire, vous pouvez configurer deux applications React séparées pour l'application hôte et une pour le distant (Product App), ou les initialiser de cette manière :

```bash
npm init
npm install react react-dom
```

**🔹 Étape #1 : Installer Webpack 5 + dépendances (Hôte + Applications Produit)**

Avant de faire quoi que ce soit lié à la fédération, les applications hôte et distante doivent être configurées avec Webpack 5 et ses plugins. Allez-y et exécutez ceci dans les deux projets :

```bash
npm install webpack webpack-cli webpack-dev-server html-webpack-plugin --save-dev
```

Quelques notes sur ces packages :

* `webpack + webpack-cli` – Bundler principal et CLI
    
* `webpack-dev-server` – Serveur local pour le rechargement à chaud + exposition des modules
    
* `html-webpack-plugin` – Injecte automatiquement vos bundles dans le HTML
    
* Optionnel mais courant : Vous pouvez ajouter `Babel`, `React preset`, `loaders`, etc., pour le support `JSX`/`TSX` plus tard.
    

Cette configuration vous donne une base. À partir de là, vous pouvez ajouter la fédération de modules pour connecter les applications ensemble.

**🔹 Étape #2 : Créer l'Application Distante (Product App)**

Commençons par l'application distante, celle qui expose un composant React à être consommé par d'autres.

Voici un simple composant `ProductTile` React (bien sûr, vous pouvez implémenter le vôtre) :

```javascript
// product-app/src/ProductTile.jsx

import React from 'react';

export default function ProductTile({ title }) {
  return (
    <div style={{ border: '1px solid #aaa', padding: '1rem' }}>
      <h3>🏪 {title}</h3>
    </div>
  );
}
```

Un composant `ProductTile` fournit une prop – "title" – et le rend.

Maintenant, exposons ce composant à d'autres applications, pas seulement le rendre localement.

**🔹 Étape #3 : Configurer Webpack dans l'Application Distante (Product App)**

Cela sera fait en utilisant la fédération de modules, que vous devez activer dans le fichier `webpack.config.js`. Voici comment cela peut être fait. Tout en haut du fichier, vous devrez importer ces packages :

```javascript
// product-app/webpack.config.js

const HtmlWebpackPlugin = require('html-webpack-plugin');
const ModuleFederationPlugin = require('webpack').container.ModuleFederationPlugin;
const path = require('path');
```

* `HtmlWebpackPlugin` – Gère la génération HTML et l'injection de scripts.
    
* `ModuleFederationPlugin` – Le plugin principal de Webpack qui vous permet d'exposer et de consommer des modules à l'exécution
    

Ensuite, définissez la configuration réelle dans `module.exports` :

```javascript
// product-app/webpack.config.js

const HtmlWebpackPlugin = require('html-webpack-plugin');
const ModuleFederationPlugin = require('webpack').container.ModuleFederationPlugin;
const path = require('path');

module.exports = {
  entry: './src/index.js',                         // Fichier d'entrée de l'application produit
  mode: 'development',                             // Doit être production si vous passez en live
  devServer: {
    port: 3001                                     // L'application produit s'exécute sur ce port
  },
  output: {
    publicPath: 'auto',                            // Requis pour la fédération dynamique
  },
  plugins: [
    new ModuleFederationPlugin({
      name: 'productApp',                         // Nom interne de l'application distante
      filename: 'remoteEntry.js',                 // Fichier d'entrée que les autres chargeront
      exposes: {
        './ProductTile': './src/ProductTile.jsx', // Exposer ce module
      },
      shared: {                                   // Packages partagés si nécessaire
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
    new HtmlWebpackPlugin({
      template: './public/index.html',
    }),
  ],
};
```

Maintenant, il est temps d'utiliser l'application produit dans l'application principale/hôte :

```javascript
// host-app/src/App.jsx

import React, { Suspense } from 'react';

// Importer dynamiquement ProductTile depuis le distant
const RemoteProductTile = React.lazy(() => import('productApp/ProductTile'));

export default function App() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>📦 Host App</h1>
      <Suspense fallback={<div>Chargement de la vignette produit...</div>}>
        <RemoteProductTile title="Enceinte Bluetooth" />
      </Suspense>
    </div>
  );
}
```

Dans React, vous pouvez utiliser la fonction `React.lazy()` pour importer dynamiquement le module fédéré. Elle retourne une promesse que React rend dès qu'elle est prête.

C'est tout. Il n'y a rien de lié à la fédération de modules dans les fichiers `bootstrap.js` et `index.html`, mais une configuration régulière, donc vous pouvez y mettre ce que vous voulez :

```javascript
// host-app/src/bootstrap.js

import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

```xml
<!-- host-app/public/index.html -->

<!DOCTYPE html>
<html>
  <head>
    <title>Host App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

Et enfin, vous pouvez lancer l'application hôte :

```bash
npx webpack serve
```

C'est tout !

Voici quelques avantages et limitations de Module Federation, ainsi que des cas d'utilisation populaires.

### **✅ Avantages**

* **Intégration à l'exécution** - Importer des composants distants après que les deux applications soient construites
    
* **Déploiement indépendant** - Les équipes peuvent déployer des applications sur des pipelines séparés
    
* **Partage de code** - Partager des bibliothèques communes (React, lodash) pour réduire la duplication
    
* **Pas d'iframes ou d'enveloppes** - Intégration native des composants, pas isolée comme les Web Components
    
* **Pas de cartes d'import nécessaires** - Webpack gère toute la logique de résolution
    
* **Fonctionne avec plusieurs frameworks** - Peut être utilisé dans React, Angular, Vue, même les Web Components
    

### **❌ Inconvénients**

* **Lié à Webpack** - **Federation** est spécifique à Webpack (des alternatives Vite/Rollup existent mais ne sont pas natives)
    
* **Configuration initiale compliquée** - Nécessite une configuration Webpack par application et une coordination des dépendances partagées
    
* **Échecs à l'exécution possibles** - Si le distant est hors ligne, l'hôte peut planter sauf si vous gérez les solutions de repli
    
* **Risques de mismatch de version** - Les bibliothèques partagées (comme React) doivent être versionnées et alignées de manière stricte
    
* **Pas de SSR automatique** - Nécessite une logique d'hydratation personnalisée pour les composants fédérés
    

### **👨🏻‍💻 Cas d'utilisation populaires**

Utilisez **Module Federation** lorsque :

* Vous voulez construire une plateforme composée d'applications déployées indépendamment
    
* Vous avez besoin de chargement de modules à l'exécution (pas seulement des widgets)
    
* Vous voulez partager des systèmes de design ou des bibliothèques UI entre les applications
    
* Votre équipe fédère des sections d'application complexes, pas seulement des composants
    
* Vous voulez éviter de charger des dépendances plusieurs fois entre les applications
    

## **Autres Outils & Ajouts à l'Écosystème**

Bien que les iframes, les Web Components, single-spa et Module Federation soient les principaux acteurs dans l'arène des micro-frontends, il existe un écosystème croissant d'outils et de stratégies alternatifs. Ils ne servent pas toujours de méthodes complètes de micro-frontends, mais résolvent néanmoins des morceaux importants du puzzle. Passons en revue certaines des solutions moins connues, mais pratiques, qui méritent votre attention.

### **Import Maps + Modules ES Natifs**

[Import Maps](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script/type/importmap) vous permettent de définir où les modules sont chargés, directement dans le navigateur. Combinés avec le support natif des modules ES, ils permettent des configurations de micro frontend sans build.

```xml
<script type="importmap">
{
  "imports": {
    "ui-library/": "https://cdn.example.com/ui/v1.2.3/",
    "square": "./modules/shapes/square.js"
  }
}
</script>
```

Vous avez peut-être remarqué que cela ressemble à ce que fait single-spa + `SystemJS`.

**Utilisez-le lorsque** :

* Vous voulez charger dynamiquement des bibliothèques partagées (comme des systèmes de design)
    
* Vous construisez des applications fédérées sans bundlers
    
* Vous ciblez uniquement les navigateurs modernes
    

### **Piral : Micro Frontends en tant que Portails Plug-in**

[Piral](https://piral.io/) est un framework spécialisé pour construire des micro frontends basés sur des portails. Il fournit un environnement structuré où les micro-apps (appelées pilets) peuvent être branchées dans une coque centrale (l'instance Piral).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748797958786/125cdd57-0d2d-4d23-a320-028b081ee989.png align="center")

> *Source :* [https://piral.io/](https://piral.io/)

**Ce framework est livré avec des fonctionnalités intégrées :**

* Routage
    
* Orchestration de la mise en page
    
* État partagé
    
* Chargement de modules
    
* Hooks d'authentification
    

**Idéal pour :**

* Portails à l'échelle de l'entreprise
    
* Applications avec de nombreuses équipes de fonctionnalités
    
* Tableaux de bord d'administration ou UIs riches en CMS
    

### **Luigi : Micro Frontends + Shells de Style SAP**

[Luigi](https://luigi-project.io/) est un framework de microfrontend construit par SAP pour permettre des shells de mise en page cohérents avec navigation latérale, barres supérieures, permissions, et plus encore.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748798177808/16380085-a4fc-4cc9-9fe2-b44821f9feef.png align="center")

> *Source :* [https://luigi-project.io/](https://luigi-project.io/)

**Ce framework est livré avec des fonctionnalités intégrées :**

* Enregistrement d'applications piloté par configuration
    
* Activation automatique des routes
    
* Contrôle d'accès basé sur les rôles (RBAC)
    
* Intégration transparente des iframes avec un shell
    

**Idéal pour :**

* Outils intranet
    
* Panneaux d'administration cloud
    
* Tableaux de bord produits
    

### **Open Components**

[OpenComponents](https://github.com/opencomponents/oc) est une manière agnostique des frameworks pour construire des microservices autonomes avec une logique UI, enregistrés dans un registre central.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748798238923/6406ef71-4dde-47bc-8d2b-9476593afdd5.png align="center")

> *Source :* [https://github.com/opencomponents/oc](https://github.com/opencomponents/oc)

**Ce framework est livré avec des fonctionnalités intégrées :**

* Rendu côté serveur ou côté client
    
* Modèle de type REST pour la consommation UI
    
* Bonne histoire de CDN + registre
    

**Idéal pour :**

* Utilisé lorsque votre entreprise traite l'UI comme des microservices déployables, tout comme les APIs.
    

### Bit : Rencontrez une architecture composable

[Bit](https://bit.dev/) n'est pas un framework de micro frontend à proprement parler, mais une plateforme de développement et de distribution basée sur les composants. Il organise le code source en composants composables, permettant de construire des applications fiables et évolutives à l'ère de l'IA.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748798402542/9fdf7de4-cc1d-41b5-9709-be824c8ffe41.png align="center")

> *Source :* [https://bit.dev](https://bit.dev/)

Utilisez-le avec les Web Components ou Module Federation pour supercharger la réutilisation. Si vous voulez pratiquer, ils ont un [Guide Officiel](https://bit.dev/blog/mastering-micro-frontends-with-module-federation-and-bit-ljn4ruah/) sur la maîtrise des Micro-Frontends avec Module Federation.

C'est un excellent ajout lorsque :

* Vous voulez publier des composants réutilisables entre les équipes
    
* Vous avez besoin de gérer les versions, la propriété et la découverte
    
* Vous visez une livraison basée sur les composants, et non sur les applications
    

## **Réflexions Finales**

Les micro frontends offrent une puissance immense, mais cette puissance s'accompagne d'une responsabilité architecturale.

Chaque méthode que nous avons explorée résout un type de problème différent :

* Les IFrames sont sécurisés, mais viennent avec une communication complexe et une isolation élevée.
    
* Les Web Components sont natifs, agnostiques des frameworks, sans dépendances et parfaits pour les kits UI réutilisables
    
* single-spa brille lorsque vous avez besoin d'orchestration et de plusieurs SPAs sous une seule coque.
    
* Module Federation est la solution idéale pour le partage de code à l'exécution et le déploiement indépendant.
    
* Et des outils comme Import Maps, Piral, Luigi, et autres comblent les lacunes, chacun à leur manière.
    

Il n'y a pas de solution universelle ici, mais avec la bonne correspondance pour la structure de votre équipe et la stratégie de votre produit, vous pouvez construire des applications qui évoluent à travers les équipes, les stacks techniques et le temps.

---

Si vous avez aimé ce guide, n'hésitez pas à le republier et à le partager avec vos amis, collègues et réseaux sociaux.

Si vous souhaitez porter vos compétences en micro-frontend à un nouveau niveau, surtout autour des Web Components, je vous invite à consulter mon cours Udemy à succès intitulé ["Web Components : Le Guide Ultime de Zéro à Héros"](https://www.udemy.com/course/web-components-api/?couponCode=HERO_START).

Et bien sûr, si vous avez des questions, des commentaires ou besoin d'aide avec votre configuration de micro frontend, n'hésitez pas à me contacter sur mes réseaux sociaux tels que [LinkedIn](https://www.linkedin.com/in/andrewmaksimchenko/) / [X](https://x.com/avmax19) / [Telegram](https://t.me/codelikeandrew). Je suis toujours heureux de discuter, de me connecter et d'aider d'autres développeurs à construire des choses incroyables ! 💚

Construisons ensemble l'avenir de l'IT dont nous pourrions être fiers ! 🚀🏽 Merci d'avoir lu — et bon découplage ! 🚀