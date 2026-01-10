---
title: Comment commencer avec React – Un guide pour débutants
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-04-12T23:13:08.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-react-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/cover-template.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
seo_title: Comment commencer avec React – Un guide pour débutants
seo_desc: 'React (also known as React.js or ReactJS) is a free and open-source front-end
  JavaScript library for creating UI component-based user interfaces.

  React is maintained by Meta (previously Facebook) along with a community of individual
  developers and or...'
---

React (également connu sous le nom de React.js ou ReactJS) est une bibliothèque JavaScript front-end gratuite et open-source pour créer des interfaces utilisateur basées sur des composants UI.

React est maintenu par Meta (anciennement Facebook) ainsi qu'une communauté de développeurs individuels et d'organisations.

Selon le [sondage des développeurs 2021 de Stack Overflow](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-web-frameworks), React a dépassé jQuery en tant que framework web le plus couramment utilisé avec environ 40,14 % de parts de marché. C'était aussi le plus désiré, avec un développeur sur quatre l'utilisant. React est également utilisé par plus de 8000 leaders de l'industrie.

Dans cet article, nous verrons les raisons pour lesquelles vous devriez apprendre React et comment commencer avec.

## Pourquoi apprendre React ?

Il y a de nombreuses raisons pour lesquelles vous devriez apprendre React, mais voici quelques-uns des points les plus fréquemment mentionnés par de nombreux experts React :

### React est facile à utiliser

Beaucoup de gens, y compris moi-même, aiment React pour sa simplicité, sa flexibilité, ses performances, son utilité, son DOM virtuel, ses composants et bien d'autres fonctionnalités.

Travailler avec React simplifie notre vie en tant que développeurs grâce à son infrastructure modulaire et directe, qui nous permet de construire et de maintenir nos applications beaucoup plus rapidement.

### Il y a une forte demande pour les développeurs React

Aux États-Unis, le salaire annuel moyen pour un développeur React est de 120 000 $. De nombreuses entreprises utilisent React, ce qui les oblige à rechercher de nouveaux talents au quotidien.

Si vous avez des réserves sur l'apprentissage ou devenir un développeur React, réfléchissez à nouveau. Il n'y a pas lieu de s'inquiéter – il y aura probablement toujours un emploi pour vous en tant que développeur React car il y a des milliers de postes ouverts en ce moment (même à distance).

### Il n'est pas difficile d'apprendre les bases de React

Cela pourrait être interprété différemment, car apprendre React en tant que codeur débutant complet prendra sans aucun doute plus de temps qu'apprendre JavaScript en tant qu'expert. Mais ce que je veux dire, c'est que React n'est pas difficile à comprendre une fois que vous avez bien saisi les fondamentaux de JavaScript.

React vous permet également de réutiliser des morceaux simples de fonctionnalités dans votre application web React.

En résumé, React est relativement simple à apprendre, dispose d'une grande communauté de soutien avec de nombreux projets open-source sur Github, et offre de nombreuses opportunités d'emploi.

Apprendre React vous aidera également à mieux comprendre JavaScript, ce qui vous sera utile tout au long de votre carrière.

Puisque React est un framework JavaScript, il est crucial de comprendre certains fondamentaux de JavaScript afin de bien maîtriser React. [Voici un article détaillé sur tous ces concepts et méthodes fondamentaux de JavaScript](https://www.freecodecamp.org/news/top-javascript-concepts-to-know-before-learning-react/) tels que map, filter, et bien d'autres. Cela vous aidera à apprendre React plus rapidement.

## Comment installer React

La meilleure façon d'installer React ou de créer un projet React est de l'installer avec [`create-react-app`](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app). C'est l'une des étapes avec lesquelles la plupart des débutants ont du mal, mais dans ce guide, nous allons passer en revue comment bien commencer et réussir.

Nous utiliserons notre terminal pour cela (vous pouvez soit utiliser un terminal intégré, soit en télécharger un que vous préférez). Un prérequis est d'avoir [Node.js](https://nodejs.org/en/download/) installé sur votre PC, en sachant bien que NPM (ou, alternativement, Yarn) est requis. Nous utiliserons NPM pour ce guide.

Pour confirmer que vous avez Node installé sur votre PC, lancez simplement votre terminal/invite de commande et tapez `node -v` et `npm -v` pour voir quelles versions vous avez.

Parce que `create-react-app` nécessite que vous ayez [NPX](https://github.com/npm/npm/releases/tag/v5.2.0) installé, vous devrez vous assurer que votre version de Node n'est pas inférieure à v14.0.0 et que votre version de NPM n'est pas inférieure à v5.6.

Supposons que vous avez une ancienne version de NPM, vous pourriez utiliser la commande suivante pour la mettre à jour :

```bash
npm update -g
```

Une fois que vous avez compris NPM, vous pouvez maintenant installer React avec `create-react-app`.

Si vous trouvez difficile de travailler avec les terminaux, vous pouvez consulter cet [article sur comment utiliser la ligne de commande pour les débutants](https://www.freecodecamp.org/news/command-line-for-beginners/).

### Qu'est-ce que Create-react-app ?

Bien que le nom explique ce qu'il fait, vous pourriez commencer à vous demander ce que `create-react-app` signifie vraiment.

Créer une application React manuellement est compliqué et prend du temps, mais `create-react-app` le rend beaucoup plus facile en automatisant toute la configuration et l'installation des packages.

`create-react-app` est la meilleure façon de commencer à construire une nouvelle [application monopage](https://reactjs.org/docs/glossary.html#single-page-application) en React.

Si vous êtes intéressé à apprendre comment créer une application React manuellement sans `create-react-app`, vous pouvez consulter [ce guide](https://dev.to/underscorecode/creating-your-react-project-from-scratch-without-create-react-app-the-complete-guide-4kbc).

### Comment créer une application React

La première étape est de démarrer votre terminal/invite de commande, de naviguer vers le dossier où vous souhaitez enregistrer votre application React, puis d'exécuter cette commande :

```bash
npx create-react-app my-app
```

**Note :** `my-app` est le nom de l'application que nous créons, mais vous pouvez le changer pour n'importe quel nom de votre choix.

Le processus d'installation peut prendre quelques minutes. Une fois terminé, vous devriez voir un dossier qui apparaît dans votre espace de travail avec le nom que vous avez donné à votre application. Félicitations !

### Comment exécuter votre application React

Maintenant, retournez dans le terminal, et la première chose à faire est de naviguer vers le répertoire où l'application a été installée en utilisant `cd my-app`. Ensuite, exécutez enfin `npm start` pour voir votre application en direct sur localhost:3000.

Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-9.png align="left")

## Structure du répertoire

Nous venons de terminer la première partie de cet article. Maintenant, découvrons ce que chaque fichier et dossier dans notre application React signifie et fait. Cela est crucial, que vous soyez débutant ou développeur React expérimenté.

La structure du répertoire de votre nouvelle application React ressemble à ceci lorsque vous l'ouvrez :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-10.png align="left")

Commençons maintenant par expliquer ces dossiers et ce qu'ils représentent :

### Dossier node_modules

Le dossier `node_modules` contient toutes nos dépendances, et ce dossier est ignoré lorsque nous configurons le contrôle de source. Mais il est important de noter que le fichier `package.json` fonctionne en tandem avec le dossier `node_modules` car il contient des informations sur toutes les dépendances ainsi que certaines commandes de script.

Si vous supprimez le dossier `node_modules`, l'application ne fonctionnera plus car vous n'aurez plus vos dépendances.

Pour réinstaller ces dépendances, vous pouvez utiliser `npm install` – cela vérifiera le fichier `pakage.json` pour une liste des dépendances et installera ensuite toutes celles-ci. Cela vous permettra de pousser votre code en ligne ou de partager votre code avec d'autres sans avoir à partager le lourd dossier `node_modules`.

**Note :** Cela ne concerne pas seulement `create-react-app`.

### Dossier public

Bien que la majorité du travail sera effectuée dans le dossier `src`, le dossier public contient certains fichiers statiques, tels que le fichier HTML. Vous pourriez, par exemple, changer le titre de votre application web, ajouter des CDN tels que Google Fonts, et ainsi de suite.

**Note :** N'ayez pas peur de ce fichier car ce n'est qu'un fichier HTML régulier. Le seul code à retenir est le `div` avec l'`id` `root` où l'ensemble de l'application React sera placé.

```html
<div id="root"></div>
```

### Fichier .gitignore

Comme le suggère le nom, c'est un fichier qui spécifie quels fichiers et dossiers seront ignorés par notre contrôle de source.

Lorsque vous ouvrez le fichier, vous verrez une liste de fichiers qui sont ignorés, y compris le dossier `node_modules` et le dossier build. Vous pouvez décider d'ajouter certains fichiers ou dossiers particuliers.

### Dossier build

Le dossier build est un autre dossier que vous ne pouvez pas voir pour le moment, mais que vous verrez lorsque vous construirez votre projet.

Cela créera un dossier de ressources statiques prêt pour la production qui peut être hébergé ou déployé en utilisant une option de glisser-déposer sur une plateforme comme Netlify.

### Dossier src

Jusqu'à présent, nous avons couvert certains dossiers fondamentaux, mais notre principale préoccupation est le dossier `src`, où se déroule le développement. Voici à quoi ressemble le dossier `src` :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-11.png align="left")

Commençons par les fichiers fondamentaux : `App.js`, `index.js`, `index.css`, et `App.css` (vous pouvez supprimer tous les autres fichiers pour l'instant).

### App.js

C'est là que tous vos composants se rencontreront éventuellement. Le nom du fichier n'est pas important, mais il est bon de garder ce nom afin que d'autres développeurs puissent comprendre votre code.

### index.js

C'est le point de départ de votre application. Plus précisément, c'est là que vous ciblez l'`id` `root` du fichier `index.html` et rendez le fichier `App.js`, où l'ensemble de votre fichier (composants et pages) se rencontrera.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

### App.css et index.css

Ces deux fichiers contiennent des styles pour votre application. Le fichier `index.css` contient le style global et le fichier `App.css` fonctionne presque de la même manière que pour le fichier `App.js` – mais que nous utilisions un fichier CSS dépend entièrement de nous. En commençant, nous pouvons choisir de supprimer un et d'utiliser un seul fichier CSS.

## Comprendre JSX

JSX est une syntaxe d'extension JavaScript utilisée dans React pour écrire facilement HTML et JavaScript ensemble.

Écrire du code dans React prend beaucoup de temps car vous devez utiliser la fonction `React.createElement` à chaque fois, même si vous ajoutez simplement un `div`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-12.png align="left")

L'image ci-dessus représente le même code écrit en JSX et avec `React.createElement`. Vous pouvez dire lequel est plus facile à écrire, comprendre et gérer en comparant les deux.

[`create-react-app`](https://github.com/facebook/create-react-app) utilise en interne Babel pour la conversion de JSX en JavaScript, donc vous n'avez pas à vous soucier de configurer votre propre configuration Babel avec Webpack.

### Quelques règles à suivre et à éviter avec JSX

Assurez-vous d'être conscient de certains de ces détails importants afin que certains bugs ne se mettent pas en travers de votre chemin :

* Votre balisage est généralement placé après l'instruction return, soit en une seule ligne de code, soit en un bloc de code.

* Tout votre code doit être enveloppé dans une seule balise. Cela pourrait être une `div`, une balise sans contenu (&lt;&gt;), ou toute autre balise.

```javascript
const App = () => {
  return (
      <h1>Titre JSX</h1>
      <p>Ceci est le premier élément JSX !</p>
      <p>Ceci est un autre élément JSX</p>
  );
};
```

Cela fonctionne bien avec un balisage normal mais entraînerait une erreur majeure car React exige que les éléments adjacents soient enveloppés dans une balise parente. Cela signifie simplement que pour que ce code s'exécute, il doit être enveloppé dans une balise parente, telle qu'une div, une section, un article, etc.

```javascript
const App = () => {
  return (
    <div>
      <h1>Titre JSX</h1>
      <p>Ceci est le premier élément JSX !</p>
      <p>Ceci est un autre élément JSX</p>
    </div>
  );
};
```

Vous pouvez également utiliser le composant `React.Fragment`.

### Comment ajouter des commentaires au code JSX

En tant que développeur, il est maintenant une pratique standard d'ajouter toujours des commentaires à votre code, et JSX ne fait pas exception. Vous pouvez soit utiliser la commande de raccourci (Cmd + / (Mac) ou Ctrl + / pour ajouter ou supprimer un commentaire particulier).

Note : Nous pouvons faire à peu près n'importe quoi avec JSX. Vous pouvez lire [cet article](https://reactjs.org/docs/jsx-in-depth.html) pour en savoir plus sur le fonctionnement de JSX.

En résumé, JSX fournit simplement du sucre syntaxique pour la fonction `React.createElement (component, props, ...children)`.

## Que faire ensuite ?

Maintenant que vous savez comment commencer avec React, l'étape suivante est de l'apprendre correctement, de comprendre ses fonctionnalités, et ainsi de suite.

De nos jours, il existe de nombreuses ressources pour apprendre React, si nombreuses qu'il est difficile de déterminer lesquelles sont actuelles et utiles.

Au lieu d'essayer de suivre plusieurs cours à la fois, la meilleure chose à faire est de trouver un tutoriel utile et de le terminer. Consultez le [**Cours gratuit sur React pour 2022**](https://www.freecodecamp.org/news/free-react-course-2022/) ou [**Apprendre React - Cours complet pour débutants**](https://www.freecodecamp.org/news/learn-react-course/) de freeCodeCamp.

## Conclusion

Jusqu'à présent dans cet article, vous avez appris ce qu'est React, pourquoi vous devriez apprendre React, comment l'installer sur votre machine. Vous avez également appris ce que fait chacun des fichiers dans sa structure de répertoire.

À partir de ce point, il y a beaucoup à apprendre sur React et je vous souhaite bonne chance dans la poursuite de vos études. Si vous avez aimé cet article, vous pouvez me soutenir en [m'offrant un café](https://www.buymeacoffee.com/tobestjoel) ou en [me suivant sur Twitter](https://twitter.com/olawanle_joel).

Embarquez dans un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.

Merci d'avoir lu !