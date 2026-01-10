---
title: Comment créer des variantes visuelles pour les composants React en utilisant
  styled-components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-22T18:36:27.000Z'
originalURL: https://freecodecamp.org/news/visual-variants-for-react-components-with-styled-components-dfaff6a76273
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NAdLxbM-7qOVjUYOhVwNGg.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment créer des variantes visuelles pour les composants React en utilisant
  styled-components
seo_desc: 'By Gilad Dayagi

  Styled-components is a library for styling React components that took the React
  world by storm when it was introduced at the end of 2016. The library is powerful
  and flexible. And solves most of the problems that classic CSS has in th...'
---

Par Gilad Dayagi

[Styled-components](https://styled-components.com/) est une bibliothèque pour styliser les composants React qui a conquis le monde React lorsqu'elle a été introduite à la fin de 2016. La bibliothèque est puissante et flexible. Et résout la plupart des [problèmes que le CSS classique a](https://speakerdeck.com/vjeux/react-css-in-js) dans ce qu'on appelle l'Ère des Composants.

Dans cet article, je vais examiner un aspect du stylisme des composants :

Comment implémenter un composant qui peut avoir plusieurs variantes visuelles.

Et je vais vous montrer trois façons différentes d'y parvenir en utilisant styled-components, que j'appelle :

**1 : L'Approche Classique**

**2 : L'Approche Composant**

**3 : L'Approche d'Extension**

Je vais supposer une certaine connaissance de React et de styled-components. Mais au cas où vous auriez besoin d'une référence, les deux ont une excellente documentation. Vous pouvez trouver la documentation de React [ici](https://facebook.github.io/react/docs/hello-world.html) et celle de styled-components [ici](https://www.styled-components.com/docs/).

Vous pouvez voir une démonstration en direct de chaque approche [ici](https://www.webpackbin.com/bins/-KkNC0RNPi5Lywsh4Ry6).

### Variantes visuelles

Dans React, un composant traduit l'état et les props en une représentation visuelle. Cela signifie généralement en un élément DOM.

Et parfois vous avez besoin qu'un composant bascule entre plusieurs états visuels, selon certaines conditions. Cela signifie que vous avez besoin que le composant change, par exemple, de couleur pour transmettre différentes informations. Par exemple :

* Un bouton peut être normal, primaire, secondaire, désactivé, etc.
* Un élément de liste peut être sélectionné ou non sélectionné.
* Un élément de formulaire peut être requis, avec erreur ou normal.

Un bon exemple de ce modèle de variante visuelle est [les styles de boutons de Bootstrap](http://getbootstrap.com/css/#buttons). Vous stylez le bouton indépendamment de son contenu et choisissez parmi une multitude de variantes. Et chaque variante du bouton sert son propre but sémantique (comme succès ou désactivé) plutôt que l'apparence (comme bleu, rond, etc.).

Alors, comment implémenter des variantes visuelles avec styled-components ? Vous pouvez le faire en utilisant l'Approche Classique, l'Approche Composant ou l'Approche d'Extension.

#### #1 : L'Approche Classique

![Image](https://cdn-media-1.freecodecamp.org/images/CPiAex8aRTvoooNLjxoKbkIQ9-dUsXnxA14L)
_Résultats utilisant l'Approche Classique_

Styled-components supporte pleinement le CSS. Ce qui inclut la capacité d'appliquer des règles de style aux "sous-classes" d'éléments. Cela signifie que vous pouvez créer des variantes visuelles en utilisant des classes CSS pas si différentes de la manière dont c'est fait avec du CSS classique.

Pour sélectionner une variante d'un composant, vous modifiez la prop `className`. Vous pouvez également passer plusieurs classes de cette manière et combiner plusieurs variantes, par exemple, 'primary' et 'large'.

**Exemple**

```
// ButtonClassic.jsximport styled from 'styled-components'
```

```
const ButtonClassic = styled.button`  background: #fff;  color: #333;  font-size: 1em;  margin: 1em;  padding: 6px 12px;  border: 1px solid #ccc;  border-radius: 4px;  cursor: pointer;
```

```
/* Style sub-classes */  &.primary {    color: #fff;    background: #337ab7;    border-color: #2e6da4;  }  &.success {    color: #fff;    background-color: #5cb85c;    border-color: #4cae4c;  }  &.link {    color: #337ab7;    background-color: transparent;    border: none;    border-radius: 0;    font-weight: 400;  }  &.large {    font-size: 1.2em;    padding: 10px 16px;    border-radius: 6px;  }  &.disabled {    color: #ddd;    background-color: #aaa;    border: 1px solid #aaa;  }`;
```

```
export default ButtonClassic
```

**Utilisation**

```
// ... <ButtonClassic>Default</ButtonClassic><ButtonClassic className="primary">Primary</ButtonClassic><ButtonClassic className="success">Success</ButtonClassic><ButtonClassic className="link">Link</ButtonClassic>
```

```
// Avec Combos<ButtonClassic className="primary large">  Primary Large</ButtonClassic>
```

```
<ButtonClassic className="disabled primary large">  Primary Large Disabled</ButtonClassic>
```

**Avantages**

* Facile à supporter plusieurs variantes.
* Facile à combiner une liste de variantes (par exemple, primary + large + disabled)
* Le code est lisible et compact
* Facile à porter les styles depuis du CSS classique

**Inconvénients**

* N'utilise pas les facilités standard des composants (props)
* Lorsque l'on combine des classes, les résultats dépendent de l'ordre de déclaration de la règle de style. Comme dans le CSS classique. Cela peut conduire à un comportement inattendu.

#### #2 : L'Approche Composant

![Image](https://cdn-media-1.freecodecamp.org/images/Gjgr560osKuRvY8o46jf6nJlcH0d50T-gS8w)
_Résultats utilisant l'Approche Composant_

Les composants stylisés, comme leur nom l'indique, sont simplement des composants normaux. Ce qui signifie qu'ils peuvent recevoir des props. Des props qui peuvent être accessibles dans la déclaration de style et utilisées pour déterminer les valeurs des règles de style.

J'appelle cela l'Approche Composant parce que cela fonctionne comme les composants React habituels. Où les valeurs des props sont utilisées pour calculer la représentation visuelle du composant. Dans ce cas, le concept est limité au style, plutôt qu'au contenu.

**Exemple**

```
// ButtonComponent.jsx import styled from 'styled-components'
```

```
const ButtonComponent = styled.button`  background: ${props => props.primary ? '#337ab7' : '#fff'};  color: ${props => props.primary ? '#fff' : '#333'};  font-size: 1em;  margin: 1em;  padding: 6px 12px;  border: ${props => props.primary ? '1px solid #2e6da4' : '1px solid #ccc'};  border-radius: 4px;  cursor: pointer;`
```

```
export default ButtonComponent
```

**Utilisation**

```
// ...<ButtonComponent>Default</ButtonComponent><ButtonComponent primary={true}>Primary</ButtonComponent>
```

**Avantages**

* Comportement standard des composants React, dérivant la représentation visuelle des props

**Inconvénients**

* Si plus de deux états sont nécessaires, le code peut devenir illisible
* Il y a une certaine répétition de code, surtout si de nombreuses règles diffèrent entre les variantes.

#### #3 : L'Approche d'Extension

![Image](https://cdn-media-1.freecodecamp.org/images/fgSi2qjHJX0LJmDGzbZVPyTGMyxItopt-3Wz)
_Résultats utilisant l'approche d'extension_

En plus des éléments primitifs, styled-components nous permet également de styliser des composants personnalisés. Vous pouvez donc re-styliser un composant de base ou par défaut. Et remplacer les règles de style pertinentes pour créer une variante visuelle.

**Exemple**

```
// ButtonExtend.jsximport styled from 'styled-components'
```

```
const ButtonExtend = styled.button`  background: #fff;  color: #333;  font-size: 1em;  margin: 1em;  padding: 6px 12px;  border: 1px solid #ccc;  border-radius: 4px;  cursor: pointer;`
```

```
export default ButtonExtend
```

```
export const ButtonExtendPrimary = styled(ButtonExtend)`  color: #fff;  background: #337ab7;  border-color: #2e6da4;`
```

```
export const ButtonExtendSuccess = styled(ButtonExtend)`  color: #fff;  background-color: #5cb85c;  border-color: #4cae4c;`
```

```
export const ButtonExtendLink = styled(ButtonExtend)`  color: #337ab7;  background-color: transparent;  border: none;  border-radius: 0;  font-weight: 400;`
```

**Utilisation**

```
// ...<ButtonExtend>Default</ButtonExtend><ButtonExtendPrimary>Primary</ButtonExtendPrimary><ButtonExtendSuccess>Success</ButtonExtendSuccess><ButtonExtendLink>Link</ButtonExtendLink>
```

**Avantages**

* Chaque variante est un composant séparé
* Facile à avoir plusieurs variantes
* Le code est très lisible

**Inconvénients**

* Pour obtenir une variante différente, un composant différent doit être rendu vs changer une propriété sur le même composant, ce qui peut être plus fastidieux.
* Ne peut pas facilement supporter la combinaison de plusieurs variantes.

### Résumé

J'ai listé toutes les façons de faire des variantes visuelles que j'ai eu l'occasion d'essayer, mais il peut y en avoir d'autres. Quelle approche est la meilleure dépend de vos besoins et préférences spécifiques.

Si vous avez manqué le lien ci-dessus, une démonstration en direct des exemples de code est disponible dans ce [webpack bin](https://www.webpackbin.com/bins/-KkNC0RNPi5Lywsh4Ry6).

Si vous connaissez d'autres approches utilisant styled-components, faites-le moi savoir dans les commentaires ci-dessous.

**Mise à jour (9 juin 2017)**

Styled-components V2 a été [publié il y a quelques jours](https://medium.com/styled-components/announcing-v2-f01ef3766ac2) avec une manière légèrement meilleure d'utiliser l'Approche d'Extension.

Il y a maintenant une fonction spécifique pour cette approche nommée `[extend](https://www.styled-components.com/docs/basics#extending-styles)`. La fonction est comme la méthode originale, mais sous le capot crée une nouvelle feuille de style en étendant l'ancienne. Et ainsi ne génère pas deux classes.

Donc, l'exemple original pour l'Approche d'Extension, ressemblerait à quelque chose comme ceci :

```
// ButtonExtendV2.jsximport styled from 'styled-components'
```

```
const ButtonExtendV2 = styled.button`  background: #fff;  color: #333;  font-size: 1em;  margin: 1em;  padding: 6px 12px;  border: 1px solid #ccc;  border-radius: 4px;  cursor: pointer;`
```

```
export default ButtonExtendV2
```

```
export const ButtonExtendV2Primary = ButtonExtendV2.extend`  color: #fff;  background: #337ab7;  border-color: #2e6da4;`
```

```
export const ButtonExtendV2Success = ButtonExtendV2.extend`  color: #fff;  background-color: #5cb85c;  border-color: #4cae4c;`// ...
```