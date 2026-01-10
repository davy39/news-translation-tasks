---
title: Comment construire des applications modernes avec WEBPACK
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T19:01:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca69a740569d1a4ca716e.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Comment construire des applications modernes avec WEBPACK
seo_desc: 'By Samuel Omole

  How far can we get with Webpack’s default configuration?

  I had the privilege of speaking at GDG Devfest last month with a talk that was centered
  around using webpack in our modern day applications. You can check out the slides
  here.

  D...'
---

Par Samuel Omole

Jusqu'où pouvons-nous aller avec la configuration par défaut de Webpack ?

J'ai eu le privilège de parler au GDG Devfest le mois dernier avec une présentation centrée sur l'utilisation de webpack dans nos applications modernes. Vous pouvez consulter les diapositives [ici](https://docs.google.com/presentation/d/1LcQYBh0VyM0iE_LuJS11wjJQeT45cApde9SdJQg9mVw/edit?usp=sharing).

Quotidiennement, je travaille en tant qu'ingénieur et/ou consultant avec des équipes amazones et rapides, et webpack semble être le facteur récurrent au sein de ces équipes (nous utilisons ReactJs pour la plupart de nos applications). Initialement, ma présentation devait se concentrer sur l'utilisation de webpack avec des frameworks/bibliothèques frontend comme ReactJS, Vue, Angular, etc.

Avant de soumettre ma proposition, j'ai décidé de mener une mini-enquête pour savoir ce que les gens pensaient de webpack. À ma surprise, beaucoup de gens ont qualifié webpack de "Seulement utilisé avec des frameworks", ce qui était loin de la vérité. D'autres ont dit que "configurer webpack était décourageant". Cela m'a conduit à me concentrer davantage sur l'utilisation de webpack avec Vanilla JS et à voir jusqu'où nous pouvions aller avec la configuration par défaut de webpack.

Mais d'abord :

### QU'EST-CE QUE WEBPACK ?

![Image](https://cdn-media-1.freecodecamp.org/images/M4slVGkwKmV0e8F2ODUCR-twvwi6foMoM0cD)

> _Je définis personnellement webpack comme un outil qui prend de nombreux modules Javascript et les fusionne en un seul module Javascript qui peut être envoyé au navigateur._

Je sais, c'est une simplification excessive de ce que fait webpack, mais les gens semblent le comprendre. Pour expliquer davantage, webpack est un bundler qui recherche des modules Javascript avec des dépendances (basiquement, des fichiers Javascript qui ont besoin de code d'autres fichiers Javascript), les fusionne ensemble, puis produit un ou plusieurs fichiers Javascript qui n'ont pas de dépendances. De cette façon, ils peuvent facilement être envoyés au navigateur.

### Histoire de Webpack

Pour comprendre les problèmes que webpack essaie de résoudre, nous devons connaître un peu l'histoire de webpack lui-même. Pour garder cette section très courte, j'ai simplement détaillé deux outils importants et un concept :

* [Google Web Toolkit](http://www.gwtproject.org/) : C'est un framework de Google qui convertit Java en Javascript (je sais, n'est-ce pas ?). Il a une fonctionnalité qui semble être ma fonctionnalité préférée dans webpack, à savoir le "code splitting" (Je vais expliquer le code splitting dans un article ultérieur).
* [Modules_Webmake](https://github.com/medikoo/modules-webmake) : C'est la bibliothèque dont webpack est issu. C'est essentiellement un outil qui nous permet d'organiser nos fichiers Javascript pour le navigateur de la même manière que nous le faisons pour NodeJS (génial).
* IIFE : signifie Immediately Invoked Function Expression. C'est essentiellement une fonction Javascript qui est appelée ou invoquée au même moment où elle a été créée.

#### Immediately Invoked Function Expression

J'ai séparé cela dans sa propre section parce que je devais expliquer davantage. Voici un exemple d'IIFE :

![Image](https://cdn-media-1.freecodecamp.org/images/xwE0cAzV6-TF1c8Fc3Iqpdky6-LVVxKe7zyl)

Si nous devions placer cette fonction dans notre balise de script, cela s'exécuterait immédiatement. La balise de script est chargée par le navigateur. C'est un peu équivalent à attacher une fonction à `window.onload` mais avec un avantage ajouté.

En raison du fonctionnement des fermetures en Javascript, toutes les variables déclarées dans l'IIFE sont limitées à cette fonction. Cela signifie que je n'aurais pas de problèmes comme des conflits de noms dans ma base de code, mais en même temps, j'ai toujours accès aux fonctions exposées par l'IIFE.

### Pourquoi Webpack ?

Alors, quels sont les problèmes auxquels nous sommes confrontés aujourd'hui et que webpack nous aide à résoudre ?

Premièrement, nous avons le problème des balises de script. J'ai travaillé sur une base de code où chaque page HTML contient au moins 30 balises de script disposées dans un ordre très précis. Je sais que certains pourraient dire que ce n'est pas vraiment un problème, mais le navigateur devra faire une requête par fichier, ce qui peut nuire à votre "temps de chargement". De plus, les balises de script peuvent devenir difficiles à gérer, où le réarrangement d'une seule pourrait casser l'application (j'ai essayé cela ?).

Deuxièmement, nous avons toujours le problème de l'espace de noms où l'espace de noms global peut devenir encombré. Je sais que nous sommes des personnes très créatives, surtout lorsqu'il s'agit de nommer des variables, mais lorsque vous travaillez dans une équipe plus grande, il arrive que les noms de variables entrent en conflit les uns avec les autres. Ou même votre futur vous pourrait penser au même nom à nouveau (oui, cela arrive).

Je connais certaines organisations qui font en sorte que leurs développeurs gardent toujours leurs variables dans le cadre de leur fonction, mais nous ne pouvons pas toujours nous fier à cela (ou à `_this_`). En fin de compte, cela rend simplement la séparation des préoccupations difficile.

Troisièmement, rappelez-vous que j'ai mentionné que webpack provenait de modules_webmake. Parce que webpack nous permet d'organiser nos fichiers de la même manière que nous le faisons dans NodeJS (en utilisant CommonJS), nous avons l'avantage supplémentaire d'écrire du code modulaire qui s'adapte très bien (demandez simplement aux personnes qui utilisent des frameworks frontend).

### CommonJS

![Image](https://cdn-media-1.freecodecamp.org/images/KjF9FAXBSSZNuiHgzhmjAReSYI1zlggAOPqO)

Je n'expliquerai pas trop CJS car ce n'est pas le but de l'article. Mais vous pouvez dire que c'est un système de modules JS utilisé dans [NodeJS](https://nodejs.org/en/).

Webpack nous permet d'utiliser ce module et même le système de modules "meilleur" ES dans le navigateur sans aucun problème (Webpack le gère de manière intelligente). Cela nous aide à écrire un code vraiment modulaire et maintenable où un fichier JS peut gérer une seule fonctionnalité (Principe de Responsabilité Unique).

### ES Modules (ESM)

![Image](https://cdn-media-1.freecodecamp.org/images/e48UD39h8gVqn49uUSrf1BkZ9dx6VkT86BAT)

C'est un autre système de modules qui, croyez-le ou non, est déjà implémenté par les navigateurs actuels. Mais malheureusement, il a ses limitations là-bas. Webpack nous permet également d'utiliser ce module sans problème (car webpack le convertit toujours à la fin), mais j'ai trouvé que l'utilisation de ESM rend la plupart des bases de code sur lesquelles j'ai travaillé plus lisibles. J'aurais aimé approfondir cela, mais ce n'est pas le but de cet article. Pour une meilleure explication, je recommande cet article amazing [article](https://medium.com/webpack/the-state-of-javascript-modules-4636d1774358).

### Comment fonctionne Webpack ?

Je sais que j'ai dit plus tôt que Webpack était magique, mais j'ai menti. Pour le dire aussi simplement que possible :

* Webpack prend un chemin vers un seul point d'entrée, qui est un fichier JS, et recherche des instructions d'importation (il peut s'agir de ESM ou de CJS).
* Il parcourt ensuite le fichier importé, recherchant également d'autres instructions d'importation, tout en créant un graphe de dépendances dans le processus.

Pour mieux expliquer, regardez l'image :

![Image](https://cdn-media-1.freecodecamp.org/images/1RXjLCpnyfAVTfB1JRwvK6jNyZlBI1NgiK3e)
_J.K._

J'ai deux fichiers là, `index.js` et `helpers.js`. Ces deux fichiers remplissent différentes fonctions, mais j'importe et utilise la fonction dans helpers.js dans mon fichier index.js. Par défaut, le point d'entrée de Webpack est `./src/index.js` et à partir de là, il essaie de construire le graphe de dépendances comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/slsswDXppG0L7O5s5tEtG5oRnQGa8rx6-Tzx)

### Comment commencer

Pour mieux comprendre comment fonctionne webpack, nous allons construire une simple application TODO. Elle n'aura que les fonctionnalités de base d'ajout et de suppression, et nous allons la bundler en utilisant la configuration par défaut de Webpack (donc aucun fichier de configuration webpack). Voici à quoi ressemblera l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/XHRBMREv6mSxjWYIYhmKsBIEASYIJvxUfdd-)
_J.K._

La première étape consiste à créer un nouveau répertoire de projet et à créer deux dossiers, un dossier nommé `dist` et un autre nommé `src`. Par défaut, le point d'entrée de Webpack est le chemin `./src/index.js` et il sortie le JS bundlé dans `./dist/main.js` — c'est pourquoi nous créons les deux dossiers.

Dans le dossier `dist`, vous pouvez créer le fichier `index.html`. Ce n'est pas nécessaire pour webpack car le fichier peut être placé n'importe où dans le répertoire du projet et vous pouvez simplement faire référence au fichier `main.js`. À la fin, la structure de votre projet devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/qz9bu3IEW6cV2awAF8GZ3qkwQ7VBch1hfRfa)

Dans le dossier `src`, nous allons créer le fichier `index.html` où nous allons commencer l'implémentation des fonctionnalités de notre application TO-DO. Mais d'abord, remplissons le fichier `index.html`. Comme la création d'une application TO-DO ne fait pas partie de ce tutoriel, je vais simplement montrer le code ci-dessous :

```html
<html>
  <head>
    <title>Todo App</title>
  </head>
  <body>
    <div class="container">
      <p>
        <label for="new-task">Add Item</label>
        <input id="new-task" type="text">
        <button id="addTask">Add</button>
      </p>
      
      <h3>Todo</h3>
      <ul id="tasks">
      </ul>
    </div>
    <script src="main.js"></script>
  </body>
</html>
```

Rendons-le maintenant fonctionnel. Nous allons diviser les deux fonctions (Ajouter et Supprimer) dans leurs propres fichiers, puis les importer dans `index.js`. Nous allons créer deux fichiers dans notre dossier `src` nommés `addTask.js` et `deleteTask.js`. La structure de votre projet devrait maintenant ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bYBUgOjdT0BdNHZXrV1e2vB2odF9KHI4ROpd)

Nous pouvons maintenant commencer à ajouter la logique nécessaire, alors implémentons d'abord `deleteTask.js` car il n'a pas de dépendances. Collez ceci dans votre fichier `deleteTask.js` :

```javascript
const deleteTask = function(e) {
  console.log("Delete Task...", e);
  //Remove the parent list item from the ul
  var listItem = e.target.parentNode;
  var ul = listItem.parentNode;
  ul.removeChild(listItem);
};


export default deleteTask;
```

Tout ce qui se passe dans ce fichier est que nous créons la fonction `deleteTask` puis l'exportons en tant qu'export par défaut.

Nous pouvons maintenant implémenter la fonction `addTask`. Dans le fichier `addTask.js`, ajoutez le code suivant :

```javascript
import deleteTask from "./deleteTask";


const createNewTaskElement = function(taskString) {

  const listItem = document.createElement("li");
  const label = document.createElement("label");
  const deleteButton = document.createElement("button");
deleteButton.innerText = "Delete";
  deleteButton.className = "delete";
  deleteButton.addEventListener("click", deleteTask);

	label.innerText = taskString;
	listItem.appendChild(label);
  	listItem.appendChild(deleteButton);
	return listItem;
};


const addTask = function(e) {
  const taskList = document.getElementById("tasks");
  const task = document.getElementById("new-task");
  if (task.value !== "") {
    const newTaskItem = createNewTaskElement(task.value);
    taskList.appendChild(newTaskItem);
    task.value = "";
  }
};


export default addTask;
```

Dans celui-ci, nous importons d'abord le fichier `deleteTask.js`. Par défaut, si aucune extension n'est spécifiée dans l'import, webpack suppose automatiquement qu'il s'agit d'un fichier `.js`. Ensuite, nous avons la fonction qui crée l'élément de liste contenant la tâche qui a été saisie dans le formulaire. La seule chose à noter est que nous attachons la fonction de suppression au gestionnaire de clic du bouton de suppression. Ensuite, nous créons la fonction addTask réelle et l'exportons.

Nous devrons ensuite importer notre fonction `addTask` dans `index.js`. Collez le code ci-dessous dans votre fichier `index.js` :

```javascript
import addTask from './addTask';

const addTaskButton = document.getElementById("addTask");

addTaskButton.addEventListener("click", addTask);
```

C'est assez simple : nous importons la fonction `addTask` et l'attachons au gestionnaire de clic pour le `addTaskButton`. Si vous avez suivi les étapes ci-dessus, vous devriez être prêt à partir.

Enfin, pour obtenir notre fichier `main.js`, nous devons exécuter Webpack à travers notre base de code. Pour cette étape, assurez-vous d'avoir [NodeJS](https://nodejs.org/en/) installé sur votre système, puis nous allons installer webpack globalement en utilisant cette commande :

```
npm install -g webpack OR sudo npm install -g webpack
```

Une fois l'installation terminée, exécutez la commande suivante :

```
webpack
```

Il bundlera notre fichier avec succès, mais nous devrions voir un avertissement dans le terminal comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/zDIK8WvPOHW1207f33J-wEZ-hY7IHDIlif1W)

Webpack nous avertit simplement que nous n'avons pas spécifié de [mode](https://webpack.js.org/concepts/#mode). Nous pourrions le laisser tel quel et exécuter le code, tout devrait fonctionner correctement. Mais si vous n'aimez pas l'avertissement, vous pouvez exécuter Webpack comme ceci :

```
webpack --mode=development
```

Et vous êtes prêt à partir.

### Conclusion

Si vous vous êtes perdu en cours de route, vous pouvez toujours utiliser le dépôt GitHub [repo](https://github.com/samie820/todo) comme référence (il contient quelques styles CSS).

J'espère que cet article a pu vous montrer ce que Webpack a à offrir (juste les bases, sans aucune configuration). Dans les articles suivants, j'essaierai de montrer comment configurer diverses configurations personnalisées pour des fonctionnalités comme le [code splitting](https://webpack.js.org/guides/code-splitting/), le [chargement paresseux](https://webpack.js.org/guides/lazy-loading/) et la configuration de Webpack pour travailler avec des applications multi-pages.

Afin de garder cet article aussi basique que possible, j'ai évité l'utilisation d'un fichier `package.json` dans l'article. L'utilisation d'un fichier `package.json` et l'installation de webpack localement est la manière la plus scalable d'utiliser webpack et j'aborderai cela dans mon prochain article sur l'utilisation de Webpack.

Pour aider à naviguer dans les articles à venir, cela aiderait vraiment si vous pouviez laisser un commentaire sur ce que vous aimeriez voir expliqué ou implémenté concernant Webpack. ??

_Je tiens à remercier particulièrement [Sean T. Larkin](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined), [Israel Obiagba](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined) et [Hassan Sani](https://www.freecodecamp.org/news/how-to-build-modern-applications-with-webpack-c81ccf6dd54f/undefined) pour leurs commentaires qui ont rendu l'article meilleur que prévu initialement. Vous êtes tous géniaux !_