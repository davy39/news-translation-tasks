---
title: Comment créer des composants React réutilisables
subtitle: ''
author: Programming with Shahan
co_authors: []
series: null
date: '2024-02-28T19:05:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-reusable-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Purple-Blue-Modern-Gradient-New-Blog-Post-Emoji-Twitter-Post--1--1.png
tags:
- name: best practices
  slug: best-practices
- name: components
  slug: components
- name: React
  slug: react
seo_title: Comment créer des composants React réutilisables
seo_desc: 'What are reusable React components? You can think of them as building blocks.
  They are independent pieces of code that can be reused throughout your website to
  save you time and effort.

  They can be anything from simple buttons to complex forms.

  Why U...'
---

Qu'est-ce que les composants React réutilisables ? Vous pouvez les considérer comme des blocs de construction. Ce sont des morceaux de code indépendants qui peuvent être réutilisés partout sur votre site web pour vous faire gagner du temps et des efforts.

Ils peuvent être n'importe quoi, des simples boutons aux formulaires complexes.

## Pourquoi utiliser des composants réutilisables ?

À mesure que votre site web grandit, vous pouvez facilement ajouter de nouvelles fonctionnalités en combinant des composants existants. Cela rend votre code plus évolutif et adaptable.

Vous pouvez utiliser votre code réutilisable dans de futurs projets sans avoir à le réécrire à partir de zéro.

## \ud83c\udfed Comment créer des composants React réutilisables

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Designer--10-_LE_auto_x2_colored.jpg)
_Illustration credit: [Shahan](https://www.youtube.com/programmingwithshahan)_

Voici les deux choses les plus importantes à garder à l'esprit lors de la création de composants React réutilisables :

## 1. \ud83e\ude7cÉviter les effets secondaires

Ne placez pas de logique qui interagit avec des données externes (comme des appels API) directement à l'intérieur d'un composant réutilisable. Au lieu de cela, passez cette logique en tant que `props` au composant.

Par exemple, si un bouton fait plus que simplement être joli, comme récupérer des données depuis Internet, il pourrait ne pas être réutilisable.

Voici un exemple de composant de bouton réutilisable. Mais il manque de bonnes pratiques. Je vais vous montrer pourquoi dans la section des exemples.

```jsx
// Ceci est un composant de bouton réutilisable (mauvaise pratique !)
const Button = () => {
  return (
    <button> Click Me </button>
  );
}

```

## 2. \ud83d\uddc3\ufe0f Utiliser les Props

Les props sont des arguments que vous passez à un composant pour personnaliser son comportement et son apparence. Cela vous permet d'utiliser le même composant pour différents usages.

```jsx
// Ceci est un composant de bouton qui peut changer de couleur
const Button = ({ color }) => {
  return (
    <button style={{ backgroundColor: color }}> Click Here </button>
  );
}

```

Ceci est toujours une mauvaise pratique car vous avez une étiquette fixe appelée "Click Here". Si vous voulez changer le texte de votre bouton pour, par exemple, "Sign Up", alors vous devrez revenir au composant de bouton et faire ce changement.

Cela signifie que chaque fois que vous voulez utiliser un texte différent, nous devrions revenir et éditer le code. En d'autres termes, il n'est plus réutilisable.

**\ud83d\udcaa Défi :** Alors, quelle est la solution ?

Vous avez déjà la réponse. Mais si ce n'est pas le cas, je vais vous montrer dans la section des exemples.

**\ud83c\udf34 Indice :** Réfléchissez à la manière dont vous pourriez vouloir utiliser le composant dans différentes situations et concevez-le pour qu'il soit flexible et adaptable.

## \ud83c\udf43 Exemples de composants React réutilisables

Voici quelques exemples courants de composants React réutilisables, accompagnés de quelques exemples de code pour vous aider à démarrer :

### Boutons

Boutons de base avec différents styles et fonctionnalités.

```jsx
// Composant Button
import React from "react";

const Button = ({ color, label, onClick }) => {
  return (
    <button
      className={`padding-2 shadow-none hover:shadow background-light-${color} hover:background-dark-${color}`}
      onClick={onClick}
    >
      {label}
    </button>
  );
};

export default Button;

// Utilisation du composant Button
<Button color="blue" label="Click Here" onClick={() => console.log("Button clicked!")} />

```

Comme vous pouvez le voir, je n'ai pas écrit "Click Here" dans le composant `button`. Je veux rendre mon bouton réutilisable, et ainsi il ne sait rien des styles ou textes personnalisés.

J'ai donc passé ces éléments en tant que props (c'est-à-dire, color, label, et onClick) pour pouvoir les changer à l'avenir sans toucher aux composants de bouton originaux. J'espère que cela rend les choses claires.

**\ud83e\ude9c Solution :** Vous devez passer chaque fonctionnalité en tant que `props` dans le composant réutilisable.

### Barres de navigation

Barres de navigation qui fournissent une navigation cohérente sur votre site web.

```jsx
// Composant Navbar
import React from "react";

const Navbar = ({ isLoggedIn }) => {
  return (
    <div className="navbar">
      <div className="navbar-container">
        <div className="navbar-logo">
          <img src={logo} alt="logo" />
        </div>
        <div className="navbar-links">
          <a href="/">Accueil</a>
          <a href="/about">À propos</a>
          <a href="/contact">Contact</a>
          {isLoggedIn ? (
            <a href="/profile">Profil</a>
          ) : (
            <a href="/login">Connexion</a>
          )}
        </div>
      </div>
    </div>
  );
};

export default Navbar;

// Utilisation du composant Navbar
<Navbar isLoggedIn={true} />

```

Comme vous pouvez le voir, j'ai passé `<Navbar isLoggedIn={true} />`

Cette ligne utilise le composant `Navbar` et passe la prop `isLoggedIn` avec une valeur de `true`, indiquant que l'utilisateur est connecté. Cela affichera le lien "Profil" et masquera le lien "Connexion".

Similaire au composant de bouton, le composant `Navbar` est réutilisable et accepte des props pour personnaliser son comportement. Parfait !

### Pourquoi les appels API dans un composant de bouton est une mauvaise pratique

Maintenant, vous comprenez tout sur les composants réutilisables dans React.

Approfondissons en résolvant un problème complexe.

Considérez le scénario où vous avez un bouton qui effectue un appel API. Le code pour le composant de bouton peut être le suivant :

```jsx
import React from "react"; 
import doAPICall from "../api"

const SaveButton  = () => {
  return (
    <button
      onClick={() => {
        doAPICall();
      }}
    >
      Save
    </button>
  );
}

export default SaveButton 

```

Il est assez clair que vous ne pouvez pas réutiliser le bouton ci-dessus à plusieurs endroits car ce composant de bouton contient un effet secondaire (`doAPICall()`) à l'intérieur.

Vous pouvez rendre ce composant réutilisable. D'abord, vous devrez extraire l'effet secondaire et le passer en tant que prop au composant de bouton comme ceci :

```jsx
const App = () =>  {
  function doAPICall() {
    // Effectue un appel API pour sauvegarder l'état actuel de l'application.
  }

  return (
    <div>
      <SaveButton onClick={doAPICall}/>
    </div>
  )
}

```

Le composant de bouton devrait ressembler à ceci :

```jsx
const SaveButton  = ({
  onClick
}) => {
  return (
    <button
      onClick={onClick}
    >
      Save
    </button>
  );
}

```

Comme vous pouvez le voir, le bouton ci-dessus peut maintenant être réutilisé n'importe où vous voulez sauvegarder des données avec un clic de bouton. Le bouton peut maintenant être utilisé comme ceci à plusieurs endroits :

```jsx
const App = () =>  {
  function saveUser() {
    // Effectue un appel API pour sauvegarder l'utilisateur.
  }

  function saveProject() {
    // Effectue un appel API pour sauvegarder le projet.
  }

  return (
    <div>
      <SaveButton onClick={saveUser}/>
      <SaveButton onClick={saveProject}/>
    </div>
  )
}

```

Vous pouvez également rendre le composant de bouton plus réutilisable en utilisant une prop pour contrôler l'étiquette :

```jsx
const App = () =>  {
  function saveUser() {
    // Effectue un appel API pour sauvegarder l'utilisateur.
  }

  function saveProject() {
    // Effectue un appel API pour sauvegarder le projet.
  }

  return (
    <div>
      <SaveButton onClick={saveUser} label="Save user"  />
      <SaveButton onClick={saveProject} label="Save project" />
    </div>
  )
}

```

Le composant de bouton devrait ressembler à ceci :

```jsx
const SaveButton  = ({
  onClick,
  label
}) => {
  return (
    <button
      onClick={onClick}
    >
      {label}
    </button>
  );
}


```

## \ud83d\udc4f Conclusion

Félicitations ! Vous avez réussi à apprendre comment créer des composants React réutilisables.

Rappelez-vous, les composants réutilisables sont les blocs de construction du développement React robuste. En pratiquant les composants réutilisables, vous pouvez créer des applications React plus propres, plus efficaces et plus maintenables.

Plus vous pratiquez, meilleur vous deviendrez pour identifier les opportunités de les utiliser dans vos projets !

**Lire plus :** [The Future of Frontend Development](https://dev.to/codewithshahan/the-future-of-frontend-development-1amd)

Merci d'avoir pris le temps de lire cet article. Jusqu'à la prochaine fois... Continuez à apprendre et vous pouvez me suivre sur **\ud835\udd4f** pour les dernières mises à jour sur la programmation et la productivité.