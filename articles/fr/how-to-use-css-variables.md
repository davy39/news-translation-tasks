---
title: Comment utiliser les variables CSS - Expliqué avec des exemples de code
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-04-02T19:53:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-variables
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/CSS-Variables.png
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: variables
  slug: variables
seo_title: Comment utiliser les variables CSS - Expliqué avec des exemples de code
seo_desc: 'If you are building websites or web apps, you should already know that
  code repetition is considered a bad practice.

  That''s why you should learn how to use CSS variables to reduce the amount of CSS
  code you write and take your styling to a new level....'
---

Si vous construisez des sites web ou des applications web, vous devriez déjà savoir que la répétition de code est considérée comme une mauvaise pratique.

C'est pourquoi vous devriez apprendre à utiliser les variables CSS pour réduire la quantité de code CSS que vous écrivez et porter votre stylisation à un nouveau niveau.

Les applications web les plus réussies ont des designs spectaculaires. Malheureusement, pour atteindre les effets souhaités, les développeurs web doivent préparer de grandes quantités de styles. Cela nous oblige à répéter des valeurs, telles que les couleurs, dans de nombreux éléments différents.

Heureusement, les feuilles de style modernes supportent les variables CSS, ce qui vous permet de réduire la répétition dans votre base de code. Vous n'avez pas besoin d'outils externes tels que les modules CSS, Less ou SASS pour en profiter.

Dans ce guide complet, je vais vous montrer comment utiliser efficacement les variables CSS, en couvrant des exemples de base en HTML et CSS pur jusqu'à des frameworks plus avancés comme React et Next.js.

## Prérequis

Ce guide est dédié aux débutants, vous n'avez donc pas besoin de connaissances spéciales pour en bénéficier.

J'ai inclus quelques exemples en React et Next.js et ils sont dédiés aux développeurs React débutants. Seuls ces exemples nécessiteront des connaissances de base en React pour les comprendre. N'hésitez pas à les sauter si vous ne travaillez pas avec React.

## Qu'est-ce que les variables CSS ?

Les variables CSS (officiellement appelées propriétés personnalisées CSS) permettent aux développeurs de gérer et de réutiliser des valeurs dans les feuilles de style CSS. Les développeurs web peuvent définir des variables réutilisables qui peuvent être utilisées dans de nombreux fichiers CSS, rendant le code plus facile à mettre à jour. Les variables CSS rendent super facile la mise en œuvre de fonctionnalités telles que le mode sombre.

Les sites web modernes nécessitent de grandes quantités de styles et cela entraîne des valeurs CSS répétées dans de nombreuses feuilles de style différentes. L'écosystème travaillait dur pour résoudre ce problème en inventant des outils tels que SASS, Less et les modules CSS, mais tous ces outils ont un défaut - ils doivent être compilés en fichiers CSS à la fin.

Heureusement, grâce aux variables CSS, nous pouvons simplifier nos feuilles de style sans outils sophistiqués et processus de construction.

## Comment créer des variables CSS

Définir une variable CSS est assez simple. Vous pouvez définir une variable CSS en utilisant le préfixe `--` suivi d'un nom de votre choix, puis en lui attribuant une valeur en utilisant la fonction `var()`.

Voici comment faire :

```css
:root {
  /* Arrière-plans */
  --primary-background: #faf8ef;
  /* Couleurs */
  --primary-text-color: #776e65;
}
```

Comme vous pouvez le voir, j'ai défini des variables CSS à l'intérieur de la pseudo-classe `:root` pour les rendre disponibles globalement.

Chaque variable commence par `--`, suivi d'un nom : `--primary-background` ou `--primary-text-color`. Enfin, j'ai attribué des valeurs à ces variables.

En utilisant cela, je pourrai changer les couleurs du site web simplement en modifiant les valeurs de ces variables.

## Comment utiliser les variables CSS

Maintenant, laissez-moi vous montrer comment utiliser les variables CSS pour définir l'arrière-plan global et la couleur du texte pour votre site web :

```css
body {
  margin: 0;
  background: var(--primary-background);
  color: var(--primary-text-color);
}
```

Pour utiliser une variable, vous devez vous y référer en utilisant la fonction `var()` et en passant le nom de la variable comme argument.

C'est tout ! Maintenant, votre site web utilise des variables CSS pour rendre les styles.

**Note** : `var()` est une fonction CSS intégrée, vous n'avez donc pas besoin de bibliothèques pour l'utiliser.

## Comment utiliser les variables CSS dans React ?

De nombreux développeurs web construisent leurs applications web en React, je vais donc vous montrer comment vous pouvez obtenir des valeurs et mettre à jour les variables CSS dans React. De nombreuses applications web modernes supportent le mode sombre et cette fonctionnalité peut devenir l'un des cauchemars d'un développeur React.

Ensuite, je vais vous montrer une méthode facile pour ajouter un mode sombre dans les applications React simplement en utilisant des variables CSS.

### Comment définir la valeur d'une variable CSS dans React ?

Changer la valeur des variables CSS dans React peut être délicat puisque React n'offre aucun outil pour interagir directement avec l'arborescence DOM. C'est pourquoi nous utiliserons du JavaScript pur pour lire et définir des variables CSS.

Voici comment vous pouvez définir une variable CSS dans React :

```jsx
import { useEffect } from 'react';

export default function Example() {
  useEffect(() => {
    document.documentElement.style.setProperty('--primary-background', `black`);
    document.documentElement.style.setProperty('--primary-text-color', `white`);
  }, [])

  return <div style={{color: "var(--primary-text-color"}}>Hello World</div>
};

```

Comme vous pouvez le voir, j'ai profité de la variable globale `document` pour accéder à l'arborescence DOM et modifier les propriétés de style. J'ai utilisé la méthode `setProperty` qui nécessite deux arguments :

* Le nom de la propriété personnalisée CSS (variable CSS).
* La valeur de la variable.

**Note** : Peu importe si vous travaillez en React ou en JavaScript pur, vous pouvez toujours appeler `document.documentElement.style.setProperty` pour modifier les valeurs des variables CSS. C'est une fonction JavaScript intégrée.

### Comment obtenir la valeur des variables CSS dans React ?

Parfois, vous pourriez avoir besoin de lire la valeur d'une variable CSS et de la stocker dans React. Dans ce cas, je vous suggérerais d'utiliser les hooks `useState` et `useEffect`.

Voici comment j'aborderais ce problème :

```jsx
import { useEffect, useState } from 'react';

export default function Example() {
  const [color, setColor] = useState('black');

  useEffect(() => {
    const cssColor = document.documentElement.style.getPropertyValue('--primary-text-color');
    setColor(cssColor);
  }, [])

  return <div style={{color: color}}>Hello World</div>
};

```

Comme vous pouvez le voir, j'ai récupéré la valeur de la variable `--primary-text-color` dans la constante `cssColor`. Dans la ligne suivante, j'ai mis à jour l'état du composant en utilisant l'aide `setColor` créée par le hook `useState`. En utilisant cette méthode, ma variable CSS peut être utilisée facilement dans les composants React.

C'est tout. Maintenant, vous pouvez utiliser cette variable dans votre application React.

## Conclusion

Les variables CSS peuvent être utilisées dans différents types de sites web et aucun JavaScript n'est nécessaire pour en profiter. Tout le monde peut en bénéficier - peu importe leur niveau d'expérience en développement web. Comprendre les variables CSS peut grandement améliorer votre expérience de stylisation et vous rendre plus efficace.

J'espère que vous avez aimé cet article. Cela signifierait beaucoup pour moi si vous le partagez sur vos réseaux sociaux.

Si vous avez des questions ou si vous voulez simplement entendre des mises à jour de ma part, vous pouvez me trouver sur [Twitter](https://twitter.com/msokola).

## Apprendre React

Si vous apprenez encore React ou si vous voulez apprendre plus de trucs comme celui-ci, vous devriez rejoindre mon cours sur Next.js. Next.js est le framework React le plus populaire qui alimente la plupart des applications React de nos jours. Je vous apprendrai comment l'utiliser en construisant un jeu 2048 génial avec des animations. Pas de blabla. Tactiques seulement.

🚀 **Rejoignez m**on [Cours intensif sur Next.js](https://www.mateu.sh/learn-nextjs).

Ce cours comprend :

* 🎥 5,5 heures de vidéo à la demande
* 📱 Accès sur mobile et TV
* 📝 Accès à vie complet
* 🎓 Certificat d'achèvement

[![Cliquez pour rejoindre le cours intensif sur Next.js](https://assets.mateu.sh/assets/fcc-css-variables)](https://mateu.sh/learn-nextjs)
_Cliquez pour commencer_