---
title: Comment éviter de casser votre application React en production
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2023-10-17T23:13:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-breaking-your-react-app-in-production
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/cover_image.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment éviter de casser votre application React en production
seo_desc: 'Did you know that your React application that''s deployed to production
  can crash any time because of unhandled errors?

  Thankfully, React Error Boundaries are here to save the day!

  Whenever any type of error happens during the rendering of a component...'
---

Saviez-vous que votre application React déployée en production peut planter à tout moment en raison d'erreurs non gérées ?

Heureusement, les limites d'erreur React sont là pour sauver la situation !

Chaque fois qu'une erreur de quelque type que ce soit se produit lors du rendu d'un composant ou dans les méthodes de cycle de vie, React affiche une page blanche sans afficher de message d'erreur.

Et obtenir une page blanche sur le site de production n'est définitivement pas une bonne expérience utilisateur.

Ainsi, les limites d'erreur React fournissent un mécanisme puissant pour capturer et gérer élégamment les erreurs qui se produisent pendant le cycle de vie de rendu de vos composants.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter la vidéo ci-dessous :

%[https://www.youtube.com/watch?v=gVj84413hVg]

## Qu'est-ce que les limites d'erreur dans React ?

Les limites d'erreur sont des composants React qui capturent les erreurs JavaScript n'importe où dans leur arbre de composants enfants, enregistrent ces erreurs et affichent une interface utilisateur de repli au lieu de l'arbre de composants qui a planté.

Les limites d'erreur capturent les erreurs pendant le rendu, dans les méthodes de cycle de vie et dans tout l'arbre en dessous d'elles.

## Pourquoi avons-nous besoin des limites d'erreur ?

Dans votre application React, il peut y avoir des cas particuliers que vous n'avez peut-être pas gérés. À cause de cela, vous pourriez obtenir une erreur en production, et vous verrez un écran blanc.

Ce n'est pas une bonne expérience utilisateur, donc l'ajout d'une limite d'erreur aide à atténuer ce problème.

Pour mieux comprendre, vous pouvez cloner [ce dépôt GitHub](https://github.com/myogeshchavan97/react-router-6-demo) que j'ai créé dans [cette vidéo](https://www.youtube.com/watch?v=b_YbEp8BLMQ).

Une fois cloné, vous pouvez exécuter la commande `npm install` depuis le dossier du projet pour installer toutes les dépendances du projet, puis exécuter la commande `npm run dev` pour démarrer l'application.

Maintenant, vous pouvez accéder à l'application en visitant [http://localhost:5173/](http://localhost:5173/).

Vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/1_initial_screen.png)
_Écran initial de l'application d'exemple_

## Comment fonctionne l'application

Maintenant, si vous cliquez sur l'un des cours, vous verrez la page des détails du cours.

Supposons que vous cliquez sur le cours `Learn Food Recipes`. Vous verrez alors l'écran comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/2_details_screen.gif)
_Page des détails du cours_

Si vous vérifiez le code, vous verrez que le contenu de la page des détails provient du composant `CourseDetails` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/3_course_details.png)
_Code du composant Course Details_

Comme vous pouvez le voir ci-dessus, nous avons des données `courses` statiques importées depuis le fichier `utils/data` à la ligne numéro 3. À la ligne numéro 8, nous utilisons la [méthode find du tableau](https://www.youtube.com/watch?v=eCTT9G7RVg4&list=PLSJnlFr3D-mGIHFpo80ylsaBErtueSpYS&index=9) pour vérifier si l'URL de la page correspond à l'une des URL des cours.

Si nous trouvons une correspondance, alors la méthode `find` retournera le cours trouvé que nous stockons dans la variable `selectedCourse`.

Et s'il n'y a pas de cours correspondant, la méthode `find` retournera `undefined` comme valeur.

Ainsi, à la ligne numéro 11, nous redirigeons l'utilisateur vers la page d'accueil en utilisant le composant `Navigate` de la bibliothèque [react-router-dom](https://courses.yogeshchavan.dev/react-router-6) si aucun cours correspondant n'est trouvé.

Pour vérifier cela, vous pouvez ajouter des caractères supplémentaires à l'URL de la page des détails, et vous verrez que vous êtes redirigé vers la page d'accueil comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/4_redirection.gif)
_Redirection automatique depuis la page des détails_

## Comment générer une erreur dans l'application

Au lieu de cela, supposons que nous n'avons pas la condition de la ligne numéro 11 pour la redirection, et que nous n'avons pas non plus le repli d'un objet vide `{}` spécifié.

Ainsi, au lieu de ce code :

```jsx
const CourseDetails = () => {
  const { pathname } = useLocation();
  const selectedCourse = courses.find((course) => course.url === pathname);

  if (!selectedCourse) {
    return <Navigate to='/' />;
  }
  const { title, duration, enrolledCount, courseImage, author } =
    selectedCourse || {};
  ...
}
```

nous avons un code comme ceci :

```jsx
const CourseDetails = () => {
  const { pathname } = useLocation();
  const selectedCourse = courses.find((course) => course.url === pathname);

  const { title, duration, enrolledCount, courseImage, author } =
    selectedCourse;
  ...
}
```

Maintenant, avec ce code, si nous ne trouvons pas de cours avec une URL de cours correspondante, alors la méthode `find` du tableau retournera `undefined` comme valeur.

Ainsi, lorsque nous déstructurons les propriétés `title`, `duration` et autres depuis la variable `selectedCourse`, JavaScript lancera une erreur.

Pour le voir en action, ouvrez les outils de développement Chrome, allez sur la page des détails de l'un des cours, et ajoutez des caractères aléatoires dans l'URL.

Lorsque vous appuyez sur la touche Entrée, vous verrez un écran blanc avec une erreur dans la console, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/5_error_screen.gif)
_Erreur de console avec application cassée_

Ainsi, comme vous pouvez le voir, l'application est cassée et rien n'est affiché à l'écran. Comme je l'ai mentionné ci-dessus, obtenir un écran blanc sans aucun texte n'est pas une bonne expérience utilisateur. L'utilisateur ne saura pas ce qui s'est passé et quoi faire dans de telles situations.

L'erreur se produit parce que nous essayons de déstructurer des propriétés depuis `undefined`.

Vous ne pouvez déstructurer des propriétés que depuis des objets et non depuis `undefined`.

Oublier de fournir un repli par défaut d'un objet vide `{}` est une chose courante lorsque vous avez une grande application.

Ainsi, pour éviter de tels scénarios d'obtention d'une page noire, nous pouvons utiliser la bibliothèque npm populaire [react-error-boundary](https://www.npmjs.com/package/react-error-boundary).

## Comment utiliser la bibliothèque react-error-boundary

Pour utiliser cette bibliothèque, installons-la d'abord en exécutant la commande suivante depuis le terminal à l'intérieur du dossier du projet :

```js
npm install react-error-boundary
```

Une fois installée, redémarrez l'application en exécutant la commande `npm run dev`.

Maintenant, nous pouvons envelopper tout notre composant `App` à l'intérieur du composant `ErrorBoundary` importé depuis la bibliothèque `react-error-boundary`.

Ainsi, ouvrez le fichier `src/main.jsx` et changez le code ci-dessous :

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

par ce code :

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ErrorBoundary } from 'react-error-boundary';
import App from './App';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ErrorBoundary fallback={<p>Something went wrong. Try again later.</p>}>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
```

Dans le code ci-dessus, nous avons enveloppé le composant `App` entre les composants d'ouverture et de fermeture `ErrorBoundary` et nous avons également importé le composant `ErrorBoundary` depuis `react-error-boundary`.

Pour le composant `ErrorBoundary`, nous fournissons la prop `fallback` avec le texte à afficher en cas d'erreur.

Ainsi, avec cette modification, si vous essayez de naviguer vers une URL de page de détails invalide, vous verrez le texte de repli affiché comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/6_fallback_error.gif)
_Affichage du message d'erreur de repli_

Mais afficher simplement ce texte n'est pas très utile. Alors, que pouvons-nous faire d'autre ?

## Comment afficher une page d'erreur appropriée

Ainsi, au lieu d'utiliser la prop `fallback`, nous utiliserons la prop `FallbackComponent`. En tant que valeur pour la prop, nous pouvons fournir soit un composant de classe, soit un composant fonctionnel.

Ainsi, à l'intérieur du dossier `components`, créez un nouveau dossier `error-page`. À l'intérieur, créez un fichier `ErrorPage.jsx` avec le contenu suivant :

```jsx
import React from 'react';
import NotFoundImage from '../../assets/writer.svg';
import './error_page.scss';

const ErrorPage = ({ error }) => {
  console.log('Error occured', error);
  return (
    <div className='error-page'>
      <img src={NotFoundImage} alt='Page not found' />
      <p className='error-msg'>
        Something went wrong. Try clicking the refresh page button to reload the
        application.{' '}
        <button className='btn'>
          Refresh page
        </button>
      </p>
    </div>
  );
};

export default ErrorPage;
```

Vous pouvez télécharger l'image `writer.svg` qui est référencée dans le code ci-dessus depuis [ce dépôt](https://github.com/myogeshchavan97/react-error-boundary-demo/blob/master/src/assets/writer.svg) et la placer à l'intérieur du dossier `src/assets`.

De plus, créez le fichier `error_page.scss` à l'intérieur du dossier `error-page` et ajoutez le contenu suivant à l'intérieur :

```css
.error-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 5rem;
  max-height: 100vh;

  img {
    width: 40%;
    height: auto;
    margin-bottom: 1rem;
  }
  p {
    margin-top: 1rem;
    font-size: 2rem;
    line-height: 130%;
  }
  .error-msg {
    display: flex;
    flex-direction: column;
    text-align: center;
    align-items: center;
    font-weight: bold;
    gap: 1rem;
  }
  .btn {
    width: fit-content;
    border: none;
    padding: 5px 10px;
    background: #bd1d3d;
    color: #fff;
    letter-spacing: 1px;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
  }
}
```

Maintenant, ouvrez le fichier `src/main.jsx` et remplacez-le par le contenu suivant :

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ErrorBoundary } from 'react-error-boundary';
import App from './App';
import ErrorPage from './components/error-page/ErrorPage';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ErrorBoundary FallbackComponent={ErrorPage}>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
```

Dans le code ci-dessus, nous avons utilisé la prop `FallbackComponent` au lieu de la prop `fallback` et nous avons ajouté le composant `ErrorPage` comme sa valeur.

De plus, notez que nous avons ajouté une instruction d'importation pour le composant `ErrorPage`.

Ainsi, si vous essayez d'aller sur une URL de page de détails invalide, vous verrez une page d'erreur bien conçue avec un bouton `Refresh page` affiché à l'écran comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/7_nice_error_page.gif)
_Affichage d'une belle page d'erreur_

Ainsi, avec la limite d'erreur ajoutée, l'utilisateur final ne voit plus une page blanche lorsque quelque chose ne va pas.

Ainsi, même s'il y a une erreur dans la console, nous ne voyons plus une page blanche.

C'est une grande amélioration pour l'application.

Notez que la page d'erreur est affichée uniquement si le rendu échoue comme une page blanche est affichée.

Et lorsque la page d'erreur est affichée, nous obtenons automatiquement la prop `error` à l'intérieur du composant `ErrorPage` que nous avons créé à l'intérieur du fichier `ErrorPage.jsx` comme vous pouvez le voir ci-dessous :

```jsx
import React from 'react';
import NotFoundImage from '../../assets/writer.svg';
import './error_page.scss';

const ErrorPage = ({ error }) => {
  console.log('Error occured', error);
  return (
    <div className='error-page'>
      <img src={NotFoundImage} alt='Page not found' />
      <p className='error-msg'>
        Something went wrong. Try clicking the refresh page button to reload the
        application.{' '}
        <button className='btn'>
          Refresh page
        </button>
      </p>
    </div>
  );
};

export default ErrorPage;
```

Dans le code ci-dessus, nous enregistrons simplement la valeur de la prop `error` dans la console.

Le composant `ErrorBoundary` accepte également une prop de fonction `onReset` où nous pouvons écrire du code pour rediriger l'utilisateur vers la page d'accueil.

Et avec la prop `onReset` ajoutée au composant `ErrorBoundary`, nous obtenons l'accès à la prop `resetErrorBoundary` à l'intérieur du composant `ErrorPage`.

Ainsi, changez le composant `ErrorPage` pour le code ci-dessous :

```jsx
const ErrorPage = ({ error, resetErrorBoundary }) => {
  console.log('Error occured', error);
  return (
    <div className='error-page'>
      <img src={NotFoundImage} alt='Page not found' />
      <p className='error-msg'>
        Something went wrong. Try clicking the refresh page button to reload the
        application.{' '}
        <button className='btn' onClick={resetErrorBoundary}>
          Refresh page
        </button>
      </p>
    </div>
  );
};
```

Dans le code ci-dessus, nous déstructurons la prop `resetErrorBoundary` que nous utiliserons pour le gestionnaire `onClick` du bouton `Refresh page`.

Maintenant, changez le code du composant `ErrorBoundary` du fichier `src/main.jsx` par le code ci-dessous :

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ErrorBoundary } from 'react-error-boundary';
import App from './App';
import ErrorPage from './components/error-page/ErrorPage';
import './index.scss';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ErrorBoundary
      FallbackComponent={ErrorPage}
      onReset={() => (location.href = '/')}
    >
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);

```

Ainsi, lorsque nous cliquons sur le bouton `Refresh page`, la fonction `resetErrorBoundary` sera appelée et elle réinitialisera toutes les erreurs et le code de la fonction `onReset` que nous avons ajoutée au fichier `src/main.jsx` sera exécuté, ce qui redirigera l'utilisateur vers la page d'accueil.

Vous pouvez le voir en action ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/8_reset_errors.gif)
_Réinitialisation des erreurs avec redirection_

Ainsi, comme vous pouvez le voir ci-dessus, avec la limite d'erreur ajoutée, nous pouvons clairement voir la page d'erreur appropriée avec le bouton `Refresh page`. Une fois que nous cliquons sur le bouton, nous sommes redirigés vers la page d'accueil, et toutes les erreurs sont effacées de la console.

C'est une excellente expérience utilisateur pour l'utilisateur final au lieu d'obtenir une page blanche.

## **Merci d'avoir lu**

C'est tout pour ce tutoriel. J'espère que vous avez beaucoup appris.

Vous voulez regarder la version vidéo de ce tutoriel ? Vous pouvez consulter [cette vidéo](https://www.youtube.com/watch?v=gVj84413hVg).

Vous pouvez trouver le code source complet de cette application dans [ce dépôt](https://github.com/myogeshchavan97/react-error-boundary-demo).

Si vous voulez maîtriser JavaScript, ES6+, React et Node.js avec un contenu facile à comprendre, consultez ma [chaîne YouTube](https://www.youtube.com/@codingmastery_dev/). N'oubliez pas de vous abonner.

Vous voulez rester à jour avec un contenu régulier sur JavaScript, React et Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).