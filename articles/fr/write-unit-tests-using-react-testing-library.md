---
title: Tutoriel React Testing Library – Comment écrire des tests unitaires pour les
  applications React
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2022-11-30T16:53:39.000Z'
originalURL: https://freecodecamp.org/news/write-unit-tests-using-react-testing-library
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover_testing.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: unit testing
  slug: unit-testing
seo_title: Tutoriel React Testing Library – Comment écrire des tests unitaires pour
  les applications React
seo_desc: 'In this tutorial, you will learn how to confidently write unit tests using
  the Testing Library. It is a very popular React testing library for writing unit
  tests.

  So let''s get started.

  What We''ll Cover:


  Why Do You Need to Write Unit Tests?

  What is t...'
---

Dans ce tutoriel, vous apprendrez à écrire des tests unitaires en toute confiance en utilisant la [Testing Library](https://testing-library.com/). Il s'agit d'une bibliothèque de test React très populaire pour écrire des tests unitaires.

Alors, commençons.

## Ce que nous allons couvrir :

1. [Pourquoi devez-vous écrire des tests unitaires ?](#heading-pourquoi-devez-vous-ecrire-des-tests-unitaires)
2. [Qu'est-ce que la React Testing Library ?](#heading-quest-ce-que-la-react-testing-library)
3. [Ce qu'il ne faut pas tester avec la Testing Library](#heading-ce-quil-ne-faut-pas-tester-avec-la-testing-library)
4. [Comment configurer un projet React avec Vite](#heading-comment-configurer-un-projet-react-avec-vite)
5. [Comment configurer la Testing Library et Jest dans un projet React](#heading-comment-configurer-la-testing-library-et-jest-dans-un-projet-react)
6. [Comment créer l'UI pour les tests](#heading-comment-creer-lui-pour-les-tests)
7. [Comment écrire des cas de test unitaires](#heading-comment-ecrire-des-cas-de-test-unitaires)
8. [Écrivons quelques tests supplémentaires](#heading-ecrivons-quelques-tests-supplementaires)
9. [Conclusion](#heading-conclusion)

Si vous souhaitez apprendre la React Testing Library en profondeur à partir de zéro, vous pouvez consulter mon [cours sur la stack MERN](https://online-elearning-platform.netlify.app/). 

## Pourquoi devez-vous écrire des tests unitaires ?

Vous pourriez penser que vous n'avez pas besoin d'écrire autant de cas de test unitaires et que c'est une perte de temps. Peut-être pouvez-vous tester l'application manuellement à la place.

Eh bien, vous avez raison – vous pouvez certainement faire cela. Mais à mesure que l'application grandit, il pourrait être difficile de tester tous les scénarios de l'application et vous pourriez manquer quelque chose. Même un petit changement pourrait casser l'application si toutes les fonctionnalités majeures ne sont pas testées correctement.

C'est pourquoi je recommande d'écrire des cas de test unitaires couvrant tous ces scénarios que vous parcourez manuellement en tant qu'utilisateur.

Ainsi, en exécutant une seule commande, vous pourrez savoir si quelque chose est cassé dans votre application ou si un test échoue.

## Qu'est-ce que la React Testing Library ?

La React [Testing Library](https://testing-library.com/) dispose d'un ensemble de packages qui vous aident à tester les composants UI de manière centrée sur l'utilisateur. Cela signifie qu'elle teste en fonction de la manière dont l'utilisateur interagit avec les divers éléments affichés sur la page.

Ainsi, lorsque l'utilisateur clique sur un bouton ou tape dans une zone de texte d'entrée, cette interaction est testée à l'aide de cette bibliothèque de test.

Ainsi, au lieu que l'utilisateur effectue ce test manuellement (ce qui prend beaucoup de temps, et l'utilisateur pourrait manquer de tester certains scénarios lorsque l'application grandit), le test est effectué en écrivant des cas de test unitaires et en les exécutant par une seule commande.

## Ce qu'il ne faut pas tester avec la Testing Library

La Testing Library vous encourage à éviter de tester les détails d'implémentation comme les internes d'un composant que vous testez.

Les principes directeurs de cette bibliothèque insistent sur une attention portée aux tests qui ressemblent de près à la manière dont les utilisateurs interagissent avec vos pages web.

Vous pourriez vouloir éviter de tester les détails d'implémentation suivants :

* État interne d'un composant
* Méthodes internes d'un composant
* Méthodes de cycle de vie d'un composant
* Composants enfants

Ainsi, si vous avez de l'expérience avec [enzyme testing](https://enzymejs.github.io/enzyme/), vous pourriez vérifier la valeur de l'état une fois que vous cliquez sur un bouton ou vous pourriez vérifier la valeur de la prop si quelque chose change.

Mais ces types de vérifications ne sont pas nécessaires pour les tests avec la bibliothèque de test React. Au lieu de cela, dans la bibliothèque de test React, vous vérifiez le comportement du DOM lorsque l'utilisateur clique sur un bouton ou soumet un formulaire et ainsi de suite.

## Comment configurer un projet React avec Vite

Pour configurer notre application que nous allons tester, nous utiliserons [Vite](https://vitejs.dev/). C'est une alternative populaire et plus rapide à [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html).

Nous utiliserons Vite car `create-react-app` devient lent lorsque l'application grandit et prend beaucoup de temps pour rafraîchir la page lorsque nous apportons des modifications au code de l'application. De plus, par défaut, il ajoute également de nombreux packages supplémentaires dont nous avons rarement besoin.

Vite ne reconstruit que les éléments que nous avons modifiés, au lieu de reconstruire l'ensemble de l'application, ce qui permet de gagner beaucoup de temps pendant le développement.

Gardez à l'esprit que Vite nécessite Node.js version 14.18+, alors assurez-vous d'installer une version de Node supérieure ou égale à 14.18.

Le moyen le plus facile et le plus simple d'installer et de changer les versions de Node.js est d'utiliser [nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

Même si vous utilisez `create-react-app`, tous les tests que vous apprendrez dans ce tutoriel devraient s'exécuter exactement de la même manière sans aucune erreur.

Pour créer un nouveau projet Vite avec React, exécutez la commande `npm init vite` depuis le terminal.

Il vous demandera le `nom du projet`, le `framework` et la `variante`.

* Pour le `nom du projet`, vous pouvez entrer `testing-library-demo` ou un nom de votre choix.
* Pour le `framework`, sélectionnez `React` dans la liste des options
* Pour la `variante`, sélectionnez `JavaScript` dans la liste des options

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1_setup.gif)
_Créer un nouveau projet React en utilisant Vite_

Une fois le projet créé, vous pouvez ouvrir ce projet dans votre IDE préféré.

La structure du dossier du projet ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/2_folder_structure.png)
_Structure des dossiers du projet React Vite_

Maintenant, exécutez la commande `yarn` ou `npm install` pour installer tous les packages à partir du fichier `package.json`.

Une fois tous les packages installés, vous pouvez exécuter la commande `yarn run dev` ou `npm run dev` pour démarrer l'application React créée.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/3_app_started.png)
_Exécution d'une application React_

Maintenant, si vous accédez à l'URL affichée `http://127.0.0.1:5173/` vous pourrez voir l'application React par défaut créée en utilisant Vite.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/4_app_loaded.png)
_Page React par défaut rendue en utilisant Vite_

Alors, voyons comment nous pouvons configurer la [Testing Library](https://testing-library.com/docs/) dans notre projet Vite.

## Comment configurer la Testing Library et Jest dans un projet React

Vous ne pouvez pas utiliser la bibliothèque de test seule – vous devez également installer [Jest](https://jestjs.io/). Elle expose une fonction globale largement utilisée `expect` et d'autres choses qui vous aident à faire des assertions dans vos cas de test.

Pour configurer [Testing library](https://testing-library.com/) et [Jest](https://jestjs.io/), vous devez installer les packages Jest et Testing Library en tant que dépendances de développement.

Alors, exécutez la commande suivante à partir du dossier `testing-library-demo` :

```js
yarn add @testing-library/jest-dom@5.16.5 @testing-library/react@13.4.0 @testing-library/user-event@14.4.3 jest@29.3.1 jest-environment-jsdom@29.3.1 vitest@0.25.3 --dev

```

ou avec npm :

```js
npm install @testing-library/jest-dom@5.16.5 @testing-library/react@13.4.0 @testing-library/user-event@14.4.3 jest@29.3.1 jest-environment-jsdom@29.3.1 vitest@0.25.3 --save-dev

```

Je mentionne les versions ici pour chaque package qui sont les dernières versions au moment de la rédaction de ce tutoriel. Ainsi, même s'il y a une nouvelle version majeure qui sort pour l'un des packages à l'avenir, votre code ne cassera pas.

Ici, nous installons la bibliothèque `jest-environment-jsdom` car nous allons exécuter les tests dans l'environnement node. Mais nous testons les interactions du navigateur à travers le DOM – donc pour informer Jest de cela, nous devons ajouter cette bibliothèque.

La bibliothèque `@testing-library/jest-dom` est requise car elle contient des assertions comme `toBeInTheDocument`, `toHaveBeenCalled`, et d'autres qui facilitent les tests pour les éléments DOM, que vous verrez plus tard dans ce tutoriel.

Nous avons également ajouté le package `vitest` qui n'est requis que lorsque vous utilisez Vite pour l'application.

Vous n'en avez pas besoin si vous utilisez `create-react-app` ou votre propre configuration webpack.

Maintenant que nous avons installé les packages requis, ajoutons un script dans le fichier `package.json` pour exécuter les tests.

Ouvrez le fichier `package.json` et ajoutez le script `test` à l'intérieur comme ceci :

```js
"test": "vitest"

```

Votre fichier `package.json` ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/5_package_json.png)
_Aperçu du fichier package.json_

Si vous n'utilisez pas `vite` pour créer l'application React, alors vous utiliserez le script de test suivant :

```js
"test": "jest --watch"

```

Maintenant, créez un nouveau fichier à la racine de votre projet (`testing-library-demo`) avec le nom `setupTests.js` et ajoutez le code suivant à l'intérieur :

```js
import "@testing-library/jest-dom";

```

Maintenant, ouvrez le fichier `vite.config.js` et ajoutez un nouvel objet `test` comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/9_vite_config.png)
_Configuration du fichier vite.config.js_

## Comment créer l'UI pour les tests

Avant d'écrire des tests, nous devons avoir quelques composants à tester.

Alors, créons une simple page d'inscription avec des cases à cocher, des champs de saisie, une liste déroulante de sélection et des boutons afin que nous puissions écrire des cas de test pour cela.

Nous utiliserons [react-bootstrap](https://react-bootstrap.github.io/) pour créer les éléments UI afin de ne pas avoir à écrire tout le CSS à partir de zéro.

Installez `bootstrap` et `react-bootstrap` en exécutant la commande suivante à partir du terminal :

```js
yarn add bootstrap@5.2.3 react-bootstrap@2.6.0 react-select@5.6.1

```

ou avec npm :

```js
npm install bootstrap@5.2.3 react-bootstrap@2.6.0 react-select@5.6.1

```

Bootstrap fournit un CSS de base dont nous avons besoin pour que l'UI ait une belle apparence, donc nous installons également Bootstrap avec react-bootstrap.

Une fois installé, ouvrez `src/main.jsx` et ajoutez une importation pour le fichier CSS Bootstrap avant tous vos autres fichiers CSS comme montré ci-dessous :

```js
import "bootstrap/dist/css/bootstrap.min.css";

```

Votre fichier `src/main.jsx` ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/6_bootstrap_css.png)
_CSS bootstrap importé_

Nous n'avons pas besoin des fichiers `index.css` et `App.css`, donc vous pouvez les supprimer.

Maintenant, créez un dossier `components` à l'intérieur du dossier `src` et créez un dossier `register` à l'intérieur du dossier `components`. À l'intérieur du dossier `register`, créez les fichiers `Register.jsx` et `register.css`.

Ainsi, le chemin de votre fichier `Register.js` sera `src/components/register/Register.js`.

Ajoutez le contenu de [ce dépôt](https://github.com/myogeshchavan97/testing-library-demo/blob/master/src/components/register/Register.jsx) dans le fichier `Register.jsx` et à l'intérieur du fichier `register.css`, ajoutez le contenu de [ce dépôt](https://github.com/myogeshchavan97/testing-library-demo/blob/master/src/components/register/register.css).

Maintenant, ouvrez le fichier `App.jsx` et ajoutez le contenu suivant à l'intérieur :

```js
import Register from "./components/Register";

function App() {
  return <Register />;
}

export default App;

```

Maintenant, si vous exécutez l'application en exécutant la commande `yarn run dev` ou `npm run dev`, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/7_register_page.png)
_Page d'inscription_

Ce tutoriel est axé sur la bibliothèque de test, donc je ne vais pas expliquer le code du fichier `Register.js` car il s'agit d'un code React de base. Mais si vous n'êtes pas familier avec les hooks React, vous pouvez consulter [cet article](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?sk=89baff89ec8bc637e7c13b7554904e54) pour mieux le comprendre.

De plus, au lieu de gérer l'état et le gestionnaire onChange vous-même, vous pouvez utiliser la bibliothèque très populaire [react-hook-form](https://react-hook-form.com/).

Elle vous permet également d'ajouter des validations à votre code sans écrire beaucoup de code. Consultez [cet article](https://www.freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form/) si vous souhaitez en apprendre davantage à ce sujet.

Maintenant, nous sommes prêts à écrire des cas de test unitaires, alors commençons.

## Comment écrire des cas de test unitaires

Avant d'écrire des cas de test, vous devez connaître les différentes requêtes que vous pouvez faire pour accéder aux éléments sur la page.

La Testing Library fournit un ensemble de requêtes que vous pouvez voir dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/8_queries.png)
_Capture d'écran montrant les requêtes getBy, queryBy, findBy, getAllBy, queryAllBy et findAllBy. ([Source](https://testing-library.com/docs/queries/about))_

Pour résumer :

* Pour sélectionner un seul élément DOM, vous pouvez utiliser la requête `getBy`, `findBy` ou `queryBy`
* Pour sélectionner plusieurs éléments DOM, vous pouvez utiliser la requête `getAllBy`, `findAllBy` ou `queryAllBy`
* `getBy` et `findBy` retournent une erreur s'il n'y a pas de correspondance ou plus d'une correspondance
* `queryBy` retourne null s'il n'y a pas de correspondance et retourne une erreur s'il y a plus d'une correspondance
* `findBy` fonctionne bien avec le code asynchrone mais pas avec `getBy` et `queryBy`
* `getAllBy` retourne une erreur s'il n'y a pas de correspondance et retourne un tableau de correspondances pour une ou plusieurs correspondances
* `findAllBy` retourne une erreur s'il n'y a pas de correspondance et retourne un tableau de correspondances pour une ou plusieurs correspondances
* `queryAllBy` retourne un tableau vide pour aucune correspondance et retourne un tableau de correspondances pour une ou plusieurs correspondances

Ainsi, si vous ne voulez pas que votre test échoue si l'élément n'est pas affiché sur l'UI, utilisez toujours `queryBy` ou `queryAllBy`.

En d'autres termes, utilisez uniquement les requêtes `queryBy` ou `queryAllBy` pour affirmer qu'un élément ne peut pas être trouvé ou est caché.

Maintenant que vous êtes familier avec les méthodes de requête, commençons à écrire des cas de test pour le composant `Register`.

Créez un nouveau fichier `register.test.jsx` dans le dossier `src/components/register` avec le contenu suivant à l'intérieur :

```js
import { render, screen } from "@testing-library/react";
import Register from "./Register";

describe("Register component", () => {
  it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByRole("heading");
    expect(element).toBeInTheDocument();
  });
});

```

Notez que nous utilisons Vite donc le nom de fichier doit se terminer par l'extension `.jsx` même pour les fichiers de test. Si vous n'utilisez pas vite, vous pouvez terminer le nom de fichier par l'extension `.js`.

Maintenant, si vous exécutez la commande `npm run test` ou `yarn run test`, vous verrez que le test passe.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/1_test_result.png)
_un test passé_

Dans le code ci-dessus, nous rendons d'abord le composant `Register` en utilisant la méthode `render` fournie par la bibliothèque de test.

Comme nous avons un élément h1 avec le texte `Register` dans le composant `Register`, nous utilisons la méthode `screen.getByRole` pour obtenir l'élément DOM du rôle `heading`.

Si vous ne savez pas quel rôle utiliser dans la méthode `getByRole`, vous pouvez utiliser un nom aléatoire et la bibliothèque de test vous montrera tous les rôles disponibles pour chaque élément DOM de ce composant comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/10_role.gif)
_Voir la structure DOM des éléments UI_

Une fois que nous obtenons cet élément en utilisant la méthode `getByRole`, nous faisons une assertion pour vérifier si cet élément existe dans le DOM en utilisant :

```js
expect(element).toBeInTheDocument();

```

Vous pouvez voir une liste de toutes les méthodes `getBy`, `findBy` ou `queryBy` disponibles en ajoutant un point après `screen` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/11_query_methods.gif)
_Méthodes fournies par l'objet screen_

Maintenant, nous avons ajouté un test pour vérifier si le composant `Register` est rendu correctement ou non.

Écrivons quelques tests supplémentaires.

Si vous exécutez l'application en exécutant la commande `yarn dev`, vous verrez que, une fois que vous cliquez sur le bouton `Register` sans remplir tous les détails, vous obtenez un message d'erreur comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/12_error_message.gif)
_Affichage du message d'erreur lors de la soumission du formulaire sans entrer de données_

Alors maintenant, nous devons tester la même chose en écrivant un cas de test.

Pour cela, nous pouvons utiliser `userEvent` du package `@testing-library/user-event` que nous avons déjà installé.

Maintenant, ajoutez un nouveau test dans votre fichier `register.test.jsx` comme montré ci-dessous :

```js
it("should show error message when all the fields are not entered", () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    userEvent.click(buttonElement);
});

```

Votre fichier `register.test.jsx` ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/13_new_test.png)
_Nouveau test ajouté pour tester l'affichage du message d'erreur_

Ainsi, nous déclenchons l'événement de clic pour le bouton `Register` dans le code ci-dessus.

Maintenant, nous devons trouver l'élément avec le message d'erreur afin que nous puissions ajouter des assertions pour celui-ci dans le test.

Le message d'erreur est en fait un composant `Alert` de `react-bootstrap` qui n'est pas visible initialement. Il n'est affiché que lorsque nous soumettons le formulaire sans remplir toutes les données.

Dans un tel cas, nous pouvons appeler la méthode `screen.debug` pour voir la structure du DOM à ce moment-là lorsque nous déclenchons l'événement de clic.

Alors, modifiez le cas de test comme montré ci-dessous :

```js
it("should show error message when all the fields are not entered", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    userEvent.click(buttonElement);
    screen.debug();
});

```

Notez que nous avons ajouté `screen.debug` à la fin du test.

Maintenant, si vous exécutez `yarn run test` ou `npm run test`, vous verrez la structure DOM suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/14_debug_output.png)
_Structure DOM après la soumission du formulaire_

Comme vous pouvez le voir sur la capture d'écran, vous voyez directement l'étiquette du champ de saisie du nom à l'intérieur de la balise de formulaire après le titre `Register`.

Ainsi, nous ne sommes pas en mesure de voir le message d'erreur même si nous avons déclenché l'événement de clic pour le bouton.

C'est parce qu'il faut un certain temps pour exécuter le code de validation de la méthode `handleFormSubmit`. Avant cela, nous utilisons uniquement la méthode `screen.debug`, donc nous ne voyons pas le message d'erreur.

Pour corriger cela, nous pouvons attendre en utilisant async/await.

Alors, déclarez la fonction de test comme `async` et avant `userEvent.click(buttonElement)` ajoutez un mot-clé `await` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/15_await_event.png)
_Ajout de async/await_

Maintenant, si vous vérifiez la console, vous pourrez voir le texte `All the fields are required.` à l'intérieur d'une div avec le rôle `alert`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/error_message_dom.png)
_Message d'erreur s'affichant dans la structure DOM_

Ainsi, nous pouvons l'utiliser dans notre assertion comme ceci :

```js
const alertElement = screen.getByRole("alert");
expect(alertElement).toBeInTheDocument();

```

Et maintenant, vous pouvez voir que le deuxième test est également réussi.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/16_success_test.png)
_test réussi_

Quelques points à noter :

* N'oubliez jamais de supprimer l'instruction `screen.debug` une fois que vous avez terminé vos assertions, et ne la gardez jamais dans votre code.
* Ajoutez toujours un mot-clé `await` avant de déclencher un événement en utilisant `userEvent` car vous ne savez peut-être pas quand l'action sera terminée.

## Écrivons quelques tests supplémentaires

Maintenant que nous avons terminé avec l'ajout de ces deux tests, nous pouvons ajouter un autre test pour vérifier s'il n'y a pas d'erreur lorsque la page est chargée comme ceci :

```js
it("should not show any error message when the component is loaded", () => {
    render(<Register />);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
});

```

Ici, au lieu d'utiliser ceci :

```js
expect(alertElement).toBeInTheDocument();

```

nous utilisons ceci :

```js
expect(alertElement).not.toBeInTheDocument();

```

Parce que nous voulons que l'élément d'alerte ne soit **pas** présent lors du chargement du composant.

Mais si vous vérifiez la console, vous verrez que le test échoue.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/17_failed_test.png)
_Test échoué lors de l'utilisation de getByRole_

Ainsi, le test n'échoue pas à cause de notre assertion. Plutôt, il échoue parce qu'il ne peut pas trouver un élément avec le rôle `alert` lors du chargement de la page, ce qui est attendu, car il n'y aura pas d'erreur lors du chargement de la page.

Mais comment pouvons-nous faire passer le test ?

Si vous vous souvenez de la liste des requêtes dans la capture d'écran montrée précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/8_queries-1.png)
_Capture d'écran montrant les requêtes getBy, queryBy, findBy, getAllBy, queryAllBy et findAllBy._

La méthode `getBy` lance une erreur si elle ne trouve pas l'élément correspondant. Donc, au lieu d'utiliser `getBy`, nous devons utiliser `queryBy`. Elle fait la même chose mais ne lance pas d'erreur lorsqu'il n'y a pas d'élément correspondant.

Alors, modifions notre cas de test avec le code ci-dessous :

```js
it("should not show any error message when the component is loaded", async () => {
    render(<Register />);
    const alertElement = screen.queryByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
});

```

Maintenant, si vous vérifiez la console, vous verrez que le test passe avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/18_test_passed_query.png)
_Test réussi lors de l'utilisation de queryByRole_

Maintenant, écrivons un test pour une inscription réussie lorsque nous remplissons tous les champs obligatoires.

```js
it("should show success message when the registration is successful.", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button");
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
});

```

Maintenant, si vous regardez la console, vous verrez que le test passe avec succès.

Ajoutons un sous-titre à la page d'inscription et voyons ce qui se passe lorsque nous exécutons les tests à nouveau.

Ajoutez l'en-tête suivant à l'intérieur de la balise `Form` dans le fichier `Register.jsx` :

```js
<h6 className="subtitle">
   Please enter your details below to register yourself.
</h6>

```

Ainsi, votre code ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/20_subtitle.png)
_Nouveau sous-titre ajouté_

Maintenant, si vous exécutez les tests à nouveau, vous verrez qu'un test échoue :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/21_failed_multiple.png)
_Test échoué en raison de plusieurs en-têtes sur la page_

Le test a échoué car dans le premier test nous trouvons le texte de l'en-tête `Register` comme montré ci-dessous :

```js
screen.getByRole("heading")

```

Et comme vous le savez, `getBy` retourne une erreur lorsque vous avez plus d'une correspondance. 

Ici, nous avons deux en-têtes sur le composant `Register`, donc le test a échoué.

Alors, comment pouvons-nous le corriger ?

Pour le corriger, nous devons identifier comment sélectionner précisément les éléments lors de l'écriture des tests.

J'ai vu de nombreux développeurs changer la structure HTML en ajoutant un `testid` afin qu'ils puissent faire passer le test comme ceci :

```js
it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByTestId("title");
    expect(element).toBeInTheDocument();
});

```

En supposant que vous avez ajouté un attribut `data-testid` supplémentaire à votre JSX comme ceci :

```js
<h2 className="title" data-testid="title">
     Register
</h2>

```

Cela fonctionnera et fera passer tous vos tests. Mais ce n'est pas la bonne façon.

Juste pour faire passer votre test, **vous ne devriez pas changer votre JSX en ajoutant un `testid` ou une `class` supplémentaire.**

Au lieu de cela, vous devriez **toujours essayer d'utiliser les méthodes fournies par `screen`** pour faire une sélection précise des éléments DOM.

Alors maintenant, la question est de savoir comment faire une sélection précise.

La méthode `getByRole` accepte des options facultatives que vous pouvez utiliser comme ceci :

```js
const element = screen.getByRole("heading", { level: 2 });

```

Comme notre en-tête principal `Register` est un en-tête `h2`, nous avons spécifiquement dit de sélectionner l'en-tête de `niveau 2`.

Maintenant, si vous mettez à jour le premier cas de test, vous verrez que tous les tests passent.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/22_fixed_failing_test.png)
_Test réussi en ajoutant une requête plus spécifique pour l'en-tête_

Maintenant, ajoutons un autre test pour tester le sous-titre.

Comme le sous-titre est de niveau 6, vous pouvez le requêter comme ceci :

```js
const element = screen.getByRole("heading", { level: 6 });

```

Cela fonctionnera, mais il y a une autre façon de cibler cet élément.

Pour cela, vous pouvez installer l'extension de navigateur Chrome [testing playground](https://chrome.google.com/webstore/detail/testing-playground/hejbmebodbijjdhflfknehhcgaklhano?hl=en).

Une fois installée, suivez les étapes ci-dessous :

* ouvrez vos outils de développement Chrome en utilisant Ctrl + Alt + I ou Cmd + Option + I (Mac)
* sélectionnez l'onglet `Testing Playground`
* Cliquez sur le pointeur du curseur et sélectionnez le sous-titre du composant `Register` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/23_accurate_subheading.gif)
_Démonstration de l'extension Testing Playground_

Comme vous pouvez le voir, vous obtiendrez la requête précise de l'élément DOM que vous pouvez utiliser dans votre test comme ceci :

```js
screen.getByRole('heading', {
  name: /please enter your details below to register yourself\./i
})

```

Ainsi, vous pouvez écrire votre test comme ceci :

```js
 it("should test for presence of subheading in the component", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      name: /please enter your details below to register yourself\./i
    });
    expect(element).toBeInTheDocument();
 });

```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/24_all_passed.png)
_Résultat du test_

Écrire un cas de test pour le sous-titre n'est pas nécessaire, car il n'affecte pas le comportement du composant même si vous ne testez pas cela. Mais juste pour vous montrer comment vos tests échoueront pour plusieurs éléments, j'ai ajouté cet élément sur l'UI ainsi que son cas de test.

L'extension Chrome `Testing Playground` est vraiment utile pour trouver la requête de correspondance exacte pour l'un des éléments UI.

Ainsi, au lieu d'utiliser la méthode `screen.debug` pour voir la structure DOM, vous pouvez utiliser cette extension Chrome pour trouver le rôle et d'autres informations pour tous les éléments affichés comme on peut le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/25_extension_demo.gif)
_Trouver une requête spécifique en utilisant testing playground_

Comme vous pouvez le voir, vous pouvez obtenir n'importe quel élément par rôle, par texte de placeholder ou par texte de label avec les méthodes fournies par `screen`.

Maintenant que vous êtes conscient des sélecteurs de requête plus spécifiques, mettons à jour les autres cas de test pour utiliser les sélecteurs spécifiques.

Là où nous utilisons simplement `screen.getByRole("button")`, remplacez-le par ce qui suit :

```js
screen.getByRole("button", {
  name: /register/i
})

```

Ainsi, si plus tard quelqu'un ajoute un autre bouton dans le même composant, votre test ne échouera pas.

Votre fichier final `register.test.jsx` ressemblera à ceci :

```js
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Register from "./Register";

describe("Register component", () => {
  it("should render Register component correctly", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      level: 2
    });
    expect(element).toBeInTheDocument();
  });

  it("should test for presence of subheading in the component", () => {
    render(<Register />);
    const element = screen.getByRole("heading", {
      name: /please enter your details below to register yourself\./i
    });
    expect(element).toBeInTheDocument();
  });

  it("should show error message when all the fields are not entered", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button", {
      name: /register/i
    });
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
  });

  it("should not show any error message when the component is loaded", () => {
    render(<Register />);
    const alertElement = screen.queryByRole("alert");
    expect(alertElement).not.toBeInTheDocument();
  });

  it("should show success message when the registration is successful.", async () => {
    render(<Register />);
    const buttonElement = screen.getByRole("button", {
      name: /register/i
    });
    await userEvent.click(buttonElement);
    const alertElement = screen.getByRole("alert");
    expect(alertElement).toBeInTheDocument();
  });
});

```

## Conclusion

La bibliothèque React Testing est incroyable et est devenue un outil très populaire pour tester les applications React.

Rappelez-vous simplement que contrairement à la bibliothèque de test [enzyme](https://enzymejs.github.io/enzyme/), vous ne devez pas tester les changements d'état lorsque vous utilisez la React Testing Library.

Ainsi, nous n'avons pas écrit de cas de test pour vérifier si l'état change correctement après que l'utilisateur a tapé du texte dans les champs `name`, `email` ou `password`.

Dans la React Testing Library, vous vérifiez le comportement du DOM lorsque l'utilisateur clique sur un bouton ou soumet un formulaire et ainsi de suite, au lieu de tester l'état interne du composant.

### Merci d'avoir lu !

Vous pouvez trouver le code source complet de ce tutoriel dans [ce dépôt](https://github.com/myogeshchavan97/testing-library-demo).

Si vous souhaitez devenir le meilleur développeur full stack MERN, alors consultez [mon cours](https://online-elearning-platform.netlify.app/).

* Il s'agit d'un cours vidéo préenregistré qui sera constamment mis à jour pour tout changement futur.
* Dans ce cours, vous apprendrez à créer des applications React et Node.js à partir de zéro et à construire une plateforme d'apprentissage en ligne incroyable.
* Après avoir appris grâce à ce cours, vous serez en mesure de construire n'importe quelle application MERN en toute confiance et facilement.
* Il y a une section séparée dans ce cours, où vous apprendrez à tester l'ensemble de votre application React en utilisant la bibliothèque de test React et Jest.

Alors, consultez ce cours incroyable.

Vous souhaitez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).