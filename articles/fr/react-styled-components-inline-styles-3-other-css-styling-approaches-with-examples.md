---
title: 'React Styled Components : Styles Inline + 3 Autres Approches de Stylisation
  CSS (avec exemples)'
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2020-03-06T14:02:00.000Z'
originalURL: https://freecodecamp.org/news/react-styled-components-inline-styles-3-other-css-styling-approaches-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/brush-painting-color-paint-102127.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: 'React Styled Components : Styles Inline + 3 Autres Approches de Stylisation
  CSS (avec exemples)'
seo_desc: 'There''s no one right way to style your React components. It all depends
  on how complex your front-end application is, and which approach you''re the most
  comfortable with.

  There are four different ways to style React application, and in this post you ...'
---

Il n'y a pas une seule bonne façon de styliser vos composants React. Tout dépend de la complexité de votre application front-end et de l'approche avec laquelle vous êtes le plus à l'aise.

Il existe quatre façons différentes de styliser une application React, et dans cet article, vous apprendrez toutes ces méthodes. Commençons par le style inline.

# Stylisation Inline

Les composants React sont composés d'éléments JSX. Mais simplement parce que vous n'écrivez pas des éléments HTML réguliers ne signifie pas que vous ne pouvez pas utiliser l'ancienne méthode de style inline.

La seule différence avec JSX est que les styles inline doivent être écrits sous forme d'objet au lieu d'une chaîne de caractères.

Voici un exemple simple :

```javascript
import React from "react";

export default function App() {
  return (
      <h1 style={{ color: "red" }}>Bonjour le Monde</h1>
  );
}
```

Dans l'attribut style ci-dessus, la première paire d'accolades indique à votre analyseur JSX que le contenu entre les accolades est du JavaScript (et non une chaîne de caractères). La deuxième paire d'accolades initialise un objet JavaScript.

Les noms de propriétés de style qui comportent plus d'un mot sont écrits en camelCase au lieu d'utiliser le style traditionnel avec des traits d'union. Par exemple, la propriété habituelle `text-align` doit être écrite `textAlign` en JSX :

```javascript
import React from "react";

export default function App() {
  return (
      <h1 style={{ textAlign: "center" }}>Bonjour le Monde</h1>
  );
}
```

Parce que l'attribut style est un objet, vous pouvez également séparer le style en l'écrivant comme une constante. Ainsi, vous pouvez le réutiliser sur d'autres éléments selon vos besoins :

```javascript
import React from "react";

const pStyle = {
  fontSize: '16px',
  color: 'blue'
}

export default function App() {
  return (
      <p style={pStyle}>Le temps est ensoleillé avec une petite chance de pluie aujourd'hui.</p>
  );
}
```

Si vous devez étendre votre style de paragraphe plus tard, vous pouvez utiliser l'opérateur de propagation d'objet. Cela vous permettra d'ajouter des styles inline à votre objet de style déjà déclaré :

```javascript
import React from "react";
const pStyle = {
  fontSize: "16px",
  color: "blue"
};
export default function App() {
  return (
    <>
      <p style={pStyle}>
        Le temps est ensoleillé avec une petite chance de pluie aujourd'hui.
      </p>
      <p style={{ ...pStyle, color: "green", textAlign: "right" }}>
        Lorsque vous allez au travail, n'oubliez pas d'emporter votre parapluie avec vous !
      </p>
    </>
  );
}

```

Les styles inline sont l'exemple le plus basique d'une technique de stylisation CSS dans JS.

L'un des avantages de l'utilisation de l'approche de style inline est que vous aurez une technique de stylisation simple et centrée sur les composants. En utilisant un objet pour le style, vous pouvez étendre votre style en propageant l'objet. Ensuite, vous pouvez ajouter plus de propriétés de style si vous le souhaitez.

Mais dans un grand projet complexe où vous avez des centaines de composants React à gérer, cela pourrait ne pas être le meilleur choix pour vous.

Vous ne pouvez pas spécifier de pseudo-classes en utilisant des styles inline. Cela signifie que `:hover`, `:focus`, `:active`, ou `:visited` sont exclus plutôt que le composant.

De plus, vous ne pouvez pas spécifier de requêtes média pour un style réactif. Considérons une autre façon de styliser votre application React.

## Feuilles de Style CSS

Lorsque vous créez une application React en utilisant `create-react-app`, vous utiliserez automatiquement webpack pour gérer l'importation et le traitement des ressources.

L'avantage de webpack est que, puisque il gère vos ressources, vous pouvez également utiliser la syntaxe `import` de JavaScript pour importer un fichier `.css` dans votre fichier JavaScript. Vous pouvez ensuite utiliser le nom de la classe CSS dans les éléments JSX que vous souhaitez styliser, comme ceci :

```css
.paragraph-text {
  font-size: 16px;
  color: 'blue';
}
```

```javascript
import React, { Component } from 'react';
import './style.css';

export default function App() {
  return (
    <>
      <p className="paragraph-text">
        Le temps est ensoleillé avec une petite chance de pluie aujourd'hui.
      </p>
    </>
  );
}
```

De cette manière, le CSS sera séparé de vos fichiers JavaScript, et vous pourrez simplement écrire la syntaxe CSS comme d'habitude.

Vous pouvez même inclure un framework CSS tel que [Bootstrap](https://create-react-app.dev/docs/adding-bootstrap/) dans votre application React en utilisant cette approche. Tout ce que vous avez à faire est d'importer le fichier CSS dans votre composant racine.

Cette méthode vous permettra d'utiliser toutes les fonctionnalités CSS, y compris les pseudo-classes et les requêtes média. Mais l'inconvénient d'utiliser une feuille de style est que votre style ne sera pas localisé à votre composant.

Tous les sélecteurs CSS ont la même portée globale. Cela signifie qu'un sélecteur peut avoir des effets secondaires indésirables et casser d'autres éléments visuels de votre application.

Tout comme les styles inline, l'utilisation de feuilles de style vous laisse toujours avec le problème de la maintenance et de la mise à jour du CSS dans un grand projet.

# Modules CSS

[Un module CSS](https://create-react-app.dev/docs/adding-a-css-modules-stylesheet/) est un fichier CSS régulier avec tous ses noms de classes et d'animations dont la portée est locale par défaut.

Chaque composant React aura son propre fichier CSS, et vous devrez importer les fichiers CSS requis dans votre composant.

Pour indiquer à React que vous utilisez des modules CSS, nommez votre fichier CSS en utilisant la convention `[name].module.css`.

Voici un exemple :

```css
.BlueParagraph {
  color: blue;
  text-align: left;
}
.GreenParagraph {
  color: green;
  text-align: right;
}
```

```javascript
import React from "react";
import styles from "./App.module.css";
export default function App() {
  return (
    <>
      <p className={styles.BlueParagraph}>
        Le temps est ensoleillé avec une petite chance de pluie aujourd'hui.
      </p>
      <p className={styles.GreenParagraph}>
        Lorsque vous allez au travail, n'oubliez pas d'emporter votre parapluie avec vous !
      </p>
    </>
  );
} 
```

Lorsque vous construisez votre application, webpack recherchera automatiquement les fichiers CSS portant le nom `.module.css`. Webpack prendra ces noms de classes et les mappers à un nouveau nom localisé généré.

Voici le sandbox pour l'exemple ci-dessus. Si vous inspectez le paragraphe bleu, vous verrez que la classe de l'élément est transformée en `_src_App_module__BlueParagraph`.

%[https://codesandbox.io/s/css-modules-example-eqh5o?fontsize=14&hidenavigation=1&theme=dark]

Les modules CSS garantissent que votre syntaxe CSS est de portée locale.

Un autre avantage de l'utilisation des modules CSS est que vous pouvez composer une nouvelle classe en héritant d'autres classes que vous avez écrites. Ainsi, vous pourrez réutiliser le code CSS que vous avez écrit précédemment, comme ceci :

```css
.MediumParagraph {
  font-size: 20px;
}
.BlueParagraph {
  composes: MediumParagraph;
  color: blue;
  text-align: left;
}
.GreenParagraph {
  composes: MediumParagraph;
  color: green;
  text-align: right;
}
```

Enfin, pour écrire un style normal avec une portée globale, vous pouvez utiliser le sélecteur `:global` devant le nom de votre classe :

```css
:global .HeaderParagraph {
  font-size: 30px;
  text-transform: uppercase;
}
```

Vous pouvez ensuite référencer le style à portée globale comme une classe normale dans votre fichier JS :

```html
<p className="HeaderParagraph">Prévisions Météorologiques</p>
```

# Composants Stylisés

Styled Components est une bibliothèque conçue pour React et React Native. Elle combine à la fois les méthodes CSS dans JS et les modules CSS pour styliser vos composants.

Permettez-moi de vous montrer un exemple :

```javascript
import React from "react";
import styled from "styled-components";

// Créez un composant Title qui rendra une balise <h1> avec quelques styles
const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

export default function App() {
  return <Title>Bonjour le Monde !</Title>;
}
```

Lorsque vous écrivez votre style, vous créez en réalité un composant React avec votre style attaché. La syntaxe étrange de `styled.h1` suivie d'une backtick est rendue possible en utilisant les littéraux de gabarit étiquetés de JavaScript.

Les composants stylisés ont été créés pour résoudre les problèmes suivants :

* **CSS critique automatique** : Les composants stylisés suivent les composants rendus sur une page et injectent leurs styles automatiquement. Combiné avec le fractionnement de code, cela signifie que vos utilisateurs chargent la quantité minimale de code nécessaire.
* **Aucun bug de nom de classe** : Les composants stylisés génèrent des noms de classe uniques pour vos styles. Vous n'avez jamais à vous soucier des doublons, des chevauchements ou des fautes de frappe.
* **Suppression plus facile du CSS** : Il peut être difficile de savoir si un nom de classe est déjà utilisé quelque part dans votre base de code. Les composants stylisés rendent cela évident, car chaque partie du style est liée à un composant spécifique. Si le composant n'est pas utilisé (ce que les outils peuvent détecter) et est supprimé, tous ses styles sont supprimés avec lui.
* **Stylisation dynamique simple** : Adapter le style d'un composant en fonction de ses props ou d'un thème global est simple et intuitif, sans que vous ayez à gérer manuellement des dizaines de classes.
* **Maintenance sans douleur** : Vous n'avez jamais à chercher dans différents fichiers pour trouver le style affectant votre composant, donc la maintenance est un jeu d'enfant, peu importe la taille de votre base de code.
* **Préfixage automatique des fournisseurs** : Écrivez votre CSS selon la norme actuelle et laissez les composants stylisés gérer le reste.

Vous obtenez tous ces avantages tout en écrivant le même CSS que vous connaissez et aimez – simplement lié à des composants individuels.

Si vous souhaitez en savoir plus sur les composants stylisés, vous pouvez consulter la [documentation](https://styled-components.com/docs) et voir plus d'exemples.

# Conclusion

De nombreux développeurs débattent encore de la meilleure façon de styliser une application React. Il y a des avantages et des inconvénients à écrire du CSS de manière non traditionnelle.

Pendant longtemps, séparer votre fichier CSS et votre fichier HTML était considéré comme la meilleure pratique, même si cela causait beaucoup de problèmes.

Mais aujourd'hui, vous avez le choix d'écrire du CSS centré sur les composants. Ainsi, votre style tirera parti de la modularité et de la réutilisabilité de React. Vous êtes maintenant en mesure d'écrire du CSS plus durable et évolutif.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !