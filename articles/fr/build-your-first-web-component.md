---
title: Comment créer votre premier composant Web
subtitle: ''
author: Joe Attardi
co_authors: []
series: null
date: '2023-10-19T20:35:35.000Z'
originalURL: https://freecodecamp.org/news/build-your-first-web-component
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-just-another-photography-dude-68725.jpg
tags:
- name: components
  slug: components
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment créer votre premier composant Web
seo_desc: 'In 2023, browser support for web components (also known as custom elements)
  is really good. There''s never been a better time to start building your own custom
  elements.

  Web components, also known as custom elements, are new HTML elements that you cre...'
---

En 2023, la prise en charge des composants Web (également appelés éléments personnalisés) par les navigateurs est vraiment bonne. Il n'y a jamais eu de meilleur moment pour commencer à créer vos propres éléments personnalisés.

Les composants Web, également appelés éléments personnalisés, sont de nouveaux éléments HTML que vous créez. Ces éléments encapsulent du balisage, du style et de l'interactivité.

Dans cet article, vous apprendrez les bases des composants Web et créerez un composant Web très simple qui affiche la date actuelle.

Ce guide est destiné à être une introduction en douceur au concept, il ne couvrira donc pas certains aspects plus avancés tels que les templates, les slots ou le shadow DOM. Mais ce sont tous des éléments de construction puissants pour créer des composants que vous devriez apprendre à mesure que vous améliorez vos compétences.

## Qu'est-ce qu'un composant Web ?

Un composant Web est un élément HTML personnalisé que vous définissez, avec son propre nom de balise. Considérez-le comme un morceau de code encapsulé et réutilisable. Tout comme les éléments HTML réguliers, les composants Web peuvent accepter des attributs et vous pouvez écouter des événements.

Les composants Web sont un bon moyen d'ajouter une fonctionnalité supplémentaire à votre application Web. Puisqu'il s'agit d'une norme Web, aucun code tiers supplémentaire n'est nécessaire.

Un composant Web peut être aussi simple ou complexe que vous le souhaitez : il peut simplement afficher du texte (comme le fera l'exemple de cet article), ou il peut être hautement interactif.

## Bases des composants Web

Pour définir un composant Web, créez une classe qui étend `HTMLElement`. Cette classe contiendra tout le comportement de votre composant Web. Après cela, vous devez l'enregistrer auprès du navigateur en appelant `customElements.define`.

```javascript
class MyComponent extends HTMLElement {
	// l'implémentation du composant va ici
}

customElements.define('my-component', MyComponent);
```

Une fois que vous avez fait cela, vous pouvez utiliser votre composant en ajoutant simplement un élément `<my-component>` à votre HTML. C'est tout ! Vous venez d'ajouter un composant Web à votre page.

Notez que le nom du composant contient un trait d'union. Cela est requis par la spécification, pour éviter les conflits de noms avec les éléments HTML standard futurs potentiels.

### Rappels de cycle de vie

Les composants Web ont quelques rappels de cycle de vie. Ce sont des fonctions que le navigateur appelle à différentes parties du cycle de vie du composant. Certains de ces rappels sont :

* `connectedCallback` : Appelé lorsque l'élément est ajouté pour la première fois au DOM
* `disconnectedCallback` : Appelé lorsque l'élément est retiré du DOM
* `attributeChangedCallback` : Appelé lorsqu'un des attributs surveillés de l'élément change. Pour qu'un attribut soit surveillé, vous devez l'ajouter à la propriété statique `observedAttributes` de la classe du composant.

Pour ce composant simple, vous n'aurez besoin que du `connectedCallback`.

## Comment créer le composant

Dans un nouveau fichier JavaScript, créez la classe du composant et ajoutez l'appel à `customElements.define` comme montré ci-dessus. Voici la première version du composant `CurrentDate` :

```javascript
class CurrentDate extends HTMLElement {
    // Le navigateur appelle cette méthode lorsque l'élément est
    // ajouté au DOM.
    connectedCallback() {
        // Crée un objet Date représentant la date actuelle.
        const now = new Date();
        
        // Formate la date en une chaîne conviviale et définit
        // la date formatée comme contenu textuel de cet élément.
        this.textContent = now.toLocaleDateString();
    }
}

// Enregistre le composant CurrentDate en utilisant le nom de balise <current-date>.
customElements.define('current-date', CurrentDate);
```

Dans le `connectedCallback`, vous obtenez la date actuelle et appelez `toLocaleDateString`, qui formate la partie date de l'objet `Date` dans un format plus convivial. Par exemple, dans la locale `en-US`, cela serait un format comme `10/18/2023`.

Il n'y a pas d'écouteurs d'événements à nettoyer ici, donc il n'y a pas besoin de `disconnectedCallback`.

Puisque `CurrentDate` étend `HTMLElement`, il inclut toutes ses propriétés et méthodes. C'est pourquoi vous pouvez utiliser la propriété `textContent` comme avec n'importe quel autre élément HTML. Cela définira la date formatée comme valeur d'un nœud de texte à l'intérieur de l'élément `<current-date>`.

## Comment utiliser le composant

Avant d'utiliser le composant, vous devez le charger à l'aide d'une instruction `import` ou d'une balise `script`. Voici un exemple d'utilisation simple avec une balise `script` :

```html
<script src="./currentDate.js"></script>

<h2>Date d'aujourd'hui</h2>
La date actuelle est : <current-date></current-date>
```

Notez que les éléments personnalisés, même lorsqu'ils n'ont pas de contenu enfant, ne peuvent pas utiliser la syntaxe de balise auto-fermante prise en charge par certains éléments. Ils doivent toujours avoir une balise de fermeture explicite.

## Améliorations futures

Voici quelques façons d'améliorer le composant `CurrentDate` :

* Utilisez `Intl.DateTimeFormat` pour créer un format plus lisible pour la date. Vous pourriez même ajouter des attributs pour personnaliser le format de date utilisé.
* Ajoutez la prise en charge d'un attribut `date` et adaptez le composant pour qu'il puisse afficher n'importe quelle date arbitraire, pas seulement la date actuelle. Bien sûr, dans ce cas, vous voudrez changer le nom de `CurrentDate` en quelque chose comme `FormattedDate`.
* Utilisez l'élément HTML `time` à l'intérieur du composant pour produire un balisage plus sémantique.

## Conclusion

Dans cet article, vous avez fait vos premiers pas dans le monde des composants Web.

Les composants Web n'ont pas de dépendances tierces, donc leur utilisation n'aura pas un grand impact sur la taille de votre bundle. Mais pour des composants plus complexes, vous pourriez vouloir utiliser une bibliothèque comme Svelte ou Lit.