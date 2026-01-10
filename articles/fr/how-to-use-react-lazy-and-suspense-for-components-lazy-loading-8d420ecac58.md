---
title: Comment utiliser React.lazy et Suspense pour le chargement paresseux des composants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T18:17:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-lazy-and-suspense-for-components-lazy-loading-8d420ecac58
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F8lEWMyFHCnZLxcUUofs-w.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment utiliser React.lazy et Suspense pour le chargement paresseux des
  composants
seo_desc: 'By Boris Sever

  React 16.6 brought code-splitting to a new level. You can now load your components
  when it’s really needed without installing additional libraries.

  What are code-splitting and lazy loading?

  Webpack defines code-splitting as:


  “techniqu...'
---

Par Boris Sever

React 16.6 a porté le code-splitting à un nouveau niveau. Vous pouvez maintenant charger vos composants uniquement lorsqu'ils sont vraiment nécessaires, sans installer de bibliothèques supplémentaires.

### Qu'est-ce que le code-splitting et le lazy loading ?

Webpack définit le code-splitting comme :

> « une technique de division de votre code en divers bundles qui peuvent ensuite être chargés à la demande ou en parallèle ». [[Source](https://webpack.js.org/guides/code-splitting/)]

Une autre façon de dire : « chargement à la demande ou en parallèle » est le **lazy-loading**.  
L'opposé du lazy-loading est le **eager-loading**. Ici, tout est chargé, peu importe si vous l'utilisez ou non.

### **Pourquoi utiliser le code-splitting et le lazy loading ?**

Parfois, nous devons introduire un gros morceau de code pour couvrir certaines fonctionnalités. Ce code peut importer une dépendance tierce ou être écrit par nous-mêmes. Ce code affecte ensuite la taille du bundle principal.

Télécharger quelques Mo est un jeu d'enfant avec la vitesse d'Internet d'aujourd'hui. Nous devons tout de même penser aux utilisateurs avec une connexion Internet lente ou utilisant des données mobiles.

### Comment était-ce fait avant React 16.6 ?

Probablement la bibliothèque la plus populaire pour le lazy loading des composants React est `[react-loadable](https://github.com/jamiebuilds/react-loadable)`.

Il est important de noter que reactjs.org recommande toujours `_react-loadable_` si votre application est rendue sur le serveur. [[Source](https://reactjs.org/docs/code-splitting.html#reactlazy)]

`react-loadable` est en fait assez similaire à la nouvelle approche de React. Je vais le montrer dans la démonstration suivante.

### Faut-il quelque chose pour l'installation ?

Voyons ce que reactjs.org a à dire à ce sujet :

> « Si vous utilisez [Create React App](https://github.com/facebookincubator/create-react-app), [Next.js](https://github.com/zeit/next.js/), [Gatsby](https://www.gatsbyjs.org/), ou un outil similaire, vous aurez une configuration Webpack prête à l'emploi pour bundler votre application.

> Si ce n'est pas le cas, vous devrez configurer le bundling vous-même. Par exemple, consultez les guides [Installation](https://webpack.js.org/guides/installation/) et [Getting Started](https://webpack.js.org/guides/getting-started/) dans la documentation de Webpack. »  
> - reactjs.org

Ok, donc _Webpack_ est requis, qui gère les imports dynamiques des bundles.

La démonstration suivante est générée en utilisant `Create React App`. Et dans ce cas, _Webpack_ est déjà configuré et nous sommes prêts à commencer.

### DÉMO

Pour cette démonstration, nous allons utiliser `[react-pdf](https://github.com/diegomura/react-pdf)`. `react-pdf` est une bibliothèque géniale utilisée pour créer des fichiers PDF dans le navigateur, sur mobile et sur le serveur. Nous pourrions générer un PDF sur le serveur, mais si nous préférons le faire côté client, cela a un coût : la taille du bundle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0onue7-IifphjgL0RE2c8A.png)
_Coût de l'importation_

> _J'utilise l'extension [Import cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) pour Visual Studio Code pour voir les tailles des bibliothèques utilisées._

Disons que notre exigence est de générer un fichier PDF lorsque l'utilisateur clique sur le bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C34cqIMAunhY76drcatFBQ.png)

Maintenant, ceci est un simple formulaire avec un seul cas d'utilisation. Essayez d'imaginer une grande application web où ceci n'est qu'une fraction des possibilités. Peut-être que cette fonctionnalité n'est pas souvent utilisée par les utilisateurs.

Mettons-nous dans cette situation. La génération de PDF n'est pas souvent utilisée et il n'a pas de sens de charger tout le code pour chaque requête de page.

Je vais essayer de montrer comment nous pouvons développer une solution avec le lazy loading et sans.

### Comparaison entre le chargement eager et lazy

Pour les deux cas, nous allons utiliser un composant qui importe des dépendances de `react-pdf` et rend un simple document PDF.

Rien de spectaculaire ici. Nous importons `PDFViewer`, `Document`, `Page`, `Text`, `View` de `react-pdf`. Tous sont utilisés dans la méthode `render` du composant `PDFPreview`.

`PDFPreview` reçoit une seule `prop` appelée `title`. Comme son nom l'indique, elle est utilisée comme titre dans le fichier PDF nouvellement généré.

_pdfStyles.js_ ressemble à ceci :

### **Chargement eager**

Voyons d'abord à quoi pourrait ressembler le composant parent sans lazy loading :

qui rend la vue suivante dans le navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fz_R39qnUqjqOMtq5SyvRw.png)

Passons en revue le code ensemble :

À la ligne 2, nous importons le composant `PDFPreview`.

À la ligne 6, nous initialisons l'état avec des valeurs par défaut. `name` est un champ utilisé comme titre dans le fichier PDF, tandis que le champ `PDFPreview` est un booléen qui affiche ou masque `PDFPreview`.

Maintenant, passons à la méthode `render` et vérifions ce qui sera rendu.

Aux lignes 19 et 25, nous rendons une entrée et un bouton. Lorsque l'utilisateur tape dans l'entrée, `name` dans l'état est modifié.

Ensuite, lorsque l'utilisateur clique sur « Generate PDF », `showPDFPreview` est défini sur `true`. Le composant se re-rend et affiche le composant `PDFPreview`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5IqztqRaIWMApDWog8evAw.png)

Même si nous utilisons `PDFPreview` uniquement sur un clic de l'utilisateur, tout le code lié à celui-ci est inclus dans le bundle de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*V7QyCEgy1viNzQ90XlafKg.png)

> _Ceci est un environnement de développement. En production, les tailles seraient significativement plus petites. Cependant, nous ne divisons pas le code de manière optimale._

### **Lazy loading**

Nous n'avons apporté que de petites modifications et passons-les en revue.

La ligne 2 est remplacée par :  
 `const LazyPDFDocument = React.lazy(() => import("./PDFPreview"`));

Voyons ce que la documentation de React dit à propos de React.lazy :

> `_React.lazy_` _prend une fonction qui doit appeler un `import()` dynamique. Cela doit retourner une `Promise` qui résout un module avec un export `default` contenant un composant React._   
> _- reactjs.org_

À la ligne 27, nous utilisons `Suspense`, qui doit être un parent d'un composant chargé de manière paresseuse. Lorsque `showPDFPreview` est défini sur true, `LazyPDFDocument` commence à se charger.

Jusqu'à ce que le composant enfant soit résolu, `Suspense` affiche ce qui est fourni à la prop `fallback`.

Le résultat final ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HzJpB-2aFBdlYflup1d5PA.gif)

Nous pouvons voir que _0.chunk.js_ pèse significativement moins qu'avant et que _4.chunk.js_ et _3.chunk.js_ sont chargés lors de l'appui sur le bouton.

### Conclusion

Chaque fois que nous introduisons une nouvelle dépendance dans notre projet, notre responsabilité est d'évaluer son coût et de vérifier comment elle affecte le bundle principal.

Ensuite, nous devons nous demander si cette fonctionnalité sera rarement utilisée et si nous pouvons la charger à la demande sans sacrifier l'expérience utilisateur.

Si la réponse est oui, alors `React.Lazy` et `Suspense` nous aident vraiment dans cette tâche.

Merci d'avoir lu ! Veuillez le partager avec toute personne qui pourrait le trouver utile et laissez des commentaires.