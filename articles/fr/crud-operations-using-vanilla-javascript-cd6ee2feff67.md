---
title: Comment effectuer des opérations CRUD en utilisant JavaScript vanilla
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T20:16:53.000Z'
originalURL: https://freecodecamp.org/news/crud-operations-using-vanilla-javascript-cd6ee2feff67
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xn7U354KKc64AeCSZWLdcw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment effectuer des opérations CRUD en utilisant JavaScript vanilla
seo_desc: 'By Zafar Saleem

  Nowadays there are a number of JavaScript frameworks around such as React, Angular,
  Vue and so on. They all offer a simple and easy approach towards the development
  of web applications, especially SPAs.

  However, many JavaScript learne...'
---

Par Zafar Saleem

De nos jours, il existe de nombreux frameworks JavaScript tels que React, Angular, Vue et bien d'autres. Ils offrent tous une approche simple et facile pour le développement d'applications web, en particulier les SPAs.

Cependant, de nombreux apprenants en JavaScript tendent à commencer par apprendre ces frameworks et savent peu de choses sur la manière de développer des applications similaires en JavaScript vanilla.

L'une des opérations les plus basiques dans toute application est le CRUD (qui signifie Create, Read, Update, Delete). C'est ce que nous allons réaliser aujourd'hui. Nous allons prendre un exemple basique et classique : une application Todo.

Bien que le JavaScript vanilla soit utilisé pour ce tutoriel, nous allons utiliser la syntaxe ES6 au lieu de la syntaxe JavaScript classique. Pour y parvenir, nous allons utiliser le transpileur Babel pour convertir ES6/ES7 en ES5, et nous allons utiliser webpack comme outil de build.

Je suppose que vous avez déjà la dernière version de node.js sur votre ordinateur. La configuration de notre environnement va prendre un peu de temps supplémentaire, donc pas besoin d'entrer dans ces détails. Clonez simplement mon code de base depuis ici ([https://github.com/zafar-saleem/hut](https://github.com/zafar-saleem/hut)) et exécutez « npm install » pour installer toutes les dépendances.

Les nouveaux fichiers iront dans le dossier `/src`. Créez donc un nouveau fichier appelé `Todo.js` à l'intérieur du dossier `/src/scripts/` et ajoutez le code ci-dessous à ce fichier :

```js
class Todo {
  constructor() {}
}

export default Todo;
```

Comme vous pouvez le voir dans le code ci-dessus, nous créons une classe `Todo`, et à l'intérieur de cette classe, nous écrivons une fonction constructeur. Bien que JavaScript n'ait pas de classes par défaut, ES6 a des classes (qui sont, en réalité, du sucre syntaxique au-dessus du prototype JavaScript).

Maintenant, lorsque nous créons une nouvelle instance de cette classe en utilisant le mot-clé `new`, la fonction constructeur est automatiquement appelée. C'est là que nous allons ajouter quelques attributs à la classe `Todo` que nous pourrons accéder dans toute cette classe en utilisant le mot-clé `this`.

Maintenant que nous avons le code ci-dessus, allez-y et importez le fichier ci-dessus dans le fichier `src/index.js` et créez une nouvelle instance de cette classe :

```js
import Todo from './scripts/Todo';

let todo = new Todo();
```

Maintenant, nous avons un code de base dans `Todo.js`. Nous avons également besoin d'un code HTML de base. Ajoutez le code ci-dessous à un fichier nommé `index.html` dans le dossier racine :

```html
<div class="edit-popup">
  <input type="text" name="" class="edit-item" />
  <button class="btn-update">Update</button>
</div>
<div class="container">
  <div class="sections">
    <input type="text" name="" class="item" />
    <button class="btn-add-item">Add</button>
    <ul>
      <li><a href="#">All</a></li>
      <li><a href="#">Today</a></li>
      <li><a href="#">Tomorrow</a></li>
    </ul>
  </div>
  <div class="items">
    <ul class="list-items"></ul>
  </div>
</div>
```

Maintenant que nous avons le code HTML de base, revenons à `Todo.js` et obtenons la référence à notre conteneur `.list-item`. Ajoutez votre nouveau code à l'intérieur du constructeur :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }
}

export default Todo;
```

Après avoir obtenu la référence à l'élément `.list-item`, j'appelle la fonction render pour afficher une liste d'éléments à l'écran. Cette fonction n'existe pas encore, donc nous allons l'écrire ensuite.

Mais avant d'écrire la fonction render, nous avons besoin de quelques données fictives que nous allons afficher. Pour les besoins de ce tutoriel, nous allons utiliser un tableau d'objets. Ajoutez vos données fictives en haut du fichier `Todo.js` :

```js
let mockData = [
  {
    id: '1',
    title: 'This is title',
    done: false,
    date: new Date(),
  },
  {
    id: '2',
    title: 'This is second title',
    done: false,
    date: new Date(),
  },
  {
    id: '3',
    title: 'This is third title',
    done: false,
    date: new Date(),
  },
  {
    id: '4',
    title: 'This is forth title',
    done: false,
    date: new Date(),
  },
];

class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }
}

export default Todo;
```

Revenons maintenant à la fonction render, qui est complétée ci-dessous :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  // fonction render
  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }
}

export default Todo;
```

Dans cette fonction, nous nous assurons que le conteneur `this.list` est vide. C'est-à-dire que nous ne voulons pas qu'un élément soit ajouté aux éléments existants. La première ligne vide simplement le conteneur avant d'ajouter de nouveaux éléments.

Ensuite, nous parcourons le tableau `mockData` que nous avons créé en haut du fichier `Todo.js` en utilisant la fonction `forEach`. À l'intérieur de la fonction de rappel `forEach`, nous créons d'abord quelques éléments DOM en appelant la fonction `createDomElements(item.id)`, et nous passons l'id de l'élément actuel à cette fonction. J'écrirai cette fonction ensuite, mais avant d'y parvenir, terminons l'écriture de cette fonction.

Une fois qu'il a créé le nouvel élément DOM (l'élément `li`) avec des éléments enfants (des boutons dans ce cas), il ajoute cet élément `li` dans la classe `Todo` en tant qu'attribut en utilisant le mot-clé `this`. Maintenant, nous pouvons accéder à cet élément `li` dans toute la classe `Todo`, donc j'accède à cet élément `li` et j'ajoute le titre en utilisant la fonction `insertAdjacentHTML()`.

Ensuite, je vérifie si l'élément actuel est terminé ou fait. Si c'est le cas, alors j'ajoute une classe à l'élément `li` actuel qui ajoute un style de barré sur l'élément.

Et enfin, j'ajoute cet élément `li` à `this.list`.

Maintenant, écrivons la fonction `createDomElements()` :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  // Étape de création des éléments DOM
  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }
}

export default Todo;
```

Cette fonction contient beaucoup de code, mais elle est simple à comprendre. Je crée simplement des éléments `li`, des boutons de suppression, d'édition et de complétion. Ensuite, j'ajoute quelques classes à tous ces boutons et je définis l'attribut `data-id` et j'assigne l'id de l'élément actuel que nous avons passé en argument depuis la fonction render. Ensuite, je mets du texte sur ces boutons (Edit, Delete et Complete) en utilisant `innerHTML`.

Enfin, j'ajoute ces boutons à l'élément `li` que j'accède plus tard dans la fonction render pour effectuer d'autres opérations.

Maintenant que nous avons la structure de base, si vous exécutez `npm run dev` et allez sur http://localhost:2770 dans le navigateur, vous devriez avoir les éléments ci-dessous, un champ de saisie et un bouton, et quatre éléments avec leurs boutons respectifs.

Jusqu'à présent, vous devriez avoir la partie « R » de CRUD — je lis tous les éléments de `mockData` et les place à l'écran.

Maintenant que la partie Read est terminée, il est temps de commencer à travailler sur la partie C de CRUD. Pour cela, nous allons écrire une fonction nommée `create` :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  // Étape de création d'un nouvel élément
  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }
}

export default Todo;
```

La fonction `create` est assez explicite : tout ce qu'elle fait est de récupérer la valeur du champ de texte. Elle crée un objet `newItem` avec les attributs `id`, `title`, `done` et `date`.

Enfin, elle pousse cet `newItem` dans le tableau `mockData`, vide le `textfield` et appelle la fonction `render` pour afficher tous les éléments avec l'élément nouvellement créé.

Maintenant, essayez cela dans votre navigateur. Mettez du texte dans le champ de texte. Appuyez sur le bouton d'ajout — mais vous ne voyez aucun changement. C'est attendu, car il reste encore une dernière partie à cela. Ajoutez simplement un écouteur d'événement au bouton « add » à l'intérieur du constructeur et appelez la fonction `create` comme suit :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();

    // écouteur d'événement pour ajouter un nouvel élément
    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }
}

export default Todo;
```

Maintenant, essayez cela dans votre navigateur et voilà. Vous avez le nouvel élément en bas de la liste.

Deux parties des opérations CRUD sont terminées. La suivante est la partie D qui est Delete.

Pour supprimer un élément, écrivons une fonction `remove` (`delete` est un mot-clé réservé en JavaScript et pour cette raison je l'ai nommée `remove`) :

```js
class Todo {
  constructor() {
    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  // Étape de suppression d'un élément
  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;
```

Cette fonction est également assez simple : elle obtient d'abord l'`id` de l'élément du bouton de suppression, qui a été ajouté dans la fonction `createDomElements` en utilisant l'attribut `data-id`. Elle filtre à travers `mockData` et place une vérification sur l'id de l'élément actuel avec l'id du bouton de suppression. Cette vérification retourne simplement tous les éléments sauf l'élément pour lequel cette vérification retourne `true`.

Après cette opération, elle ré-affiche tous les éléments en appelant la fonction `render` en bas.

Les choses semblent bien se présenter, mais attendez une minute : cette fonction doit être déclenchée en appelant le bouton de suppression. Comme vous vous en souvenez peut-être, ce bouton a été ajouté dynamiquement dans la fonction `createDomElements`. Ajouter des événements à de tels éléments est un peu délicat. Puisque ces éléments n'étaient pas présents lorsque le DOM a été chargé et ont été ajoutés plus tard, ajouter l'écouteur d'événement directement aux boutons de suppression, de mise à jour et de complétion ne va pas fonctionner.

Pour que cela fonctionne, ajoutez l'écouteur d'événement à l'objet document et trouvez le bouton particulier (suppression dans ce cas) pour effectuer l'opération de suppression ou de suppression.

```js
class Todo {
  constructor() {
    let self = this; // référence au mot-clé this

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    // étape pour ajouter l'écouteur d'événement de clic au bouton de suppression
    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;
```

Pour appeler remove, le mot `self` est utilisé. À l'intérieur de la fonction de rappel, le mot-clé `this` perd sa référence à la classe `Todo`. Pour cette raison, créez une nouvelle variable appelée `self` et attribuez le mot-clé `this` à celle-ci en haut de la construction.

À l'intérieur de la fonction de rappel, je vérifie si l'élément de clic a une classe `btn-delete` — c'est-à-dire, est-ce un bouton de suppression ? Ensuite, déclenchez simplement la fonction `remove` et passez l'événement comme paramètre. J'utilise cela à l'intérieur de la fonction `remove` pour obtenir l'id de l'élément cliqué actuel afin d'effectuer l'opération de suppression.

La partie Update est légèrement compliquée. Elle se compose de deux fonctions. La première consiste à afficher le formulaire d'édition, qui contient un champ de texte et un bouton de mise à jour. La seconde consiste à mettre à jour la fonction qui effectue l'opération de mise à jour :

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
    });
  }

  // étape pour afficher le formulaire d'édition
  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;
```

Tout le code ci-dessus fait est d'ajouter et de supprimer des classes CSS pour afficher et masquer le formulaire d'édition qui est déjà dans le DOM avec la classe edit-popup. Obtenez l'id du bouton d'édition et placez-le sur le bouton de mise à jour. Parcourez `mockData` et recherchez l'élément actuel en utilisant son id. Placez le titre de l'élément de mockData dans le champ de texte pour l'éditer.

Pour déclencher cette fonction, suivez la même logique que pour la suppression pour ajouter un écouteur d'événement, comme ceci :

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
      // étape pour ajouter un événement de clic pour afficher le formulaire d'édition
      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
}

export default Todo;
```

Maintenant, il est temps d'écrire l'opération de mise à jour. Suivez le code ci-dessous :

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  // étape pour mettre à jour un élément
  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }
}

export default Todo;
```

Les deux premières lignes de cette fonction permettent d'obtenir l'id de l'élément et la valeur du champ de texte et de les placer dans leurs variables respectives. Ensuite, parcourez `mockData` et placez une vérification pour trouver l'élément qui doit être mis à jour en fonction de l'id. Une fois cet élément trouvé, remplacez le titre par un nouveau titre `itemTobeUpdate`. Enfin, `retournez` cet élément mis à jour depuis la map.

Une fois cette opération terminée, masquez le formulaire edit-popup en ajoutant et en supprimant les classes CSS respectives. Ensuite, ré-affichez `mockData` en appelant la fonction render.

Pour déclencher cette fonction, ajoutez le code ci-dessous au constructeur :

```js
class Todo {

  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document.querySelector('.btn-add-item').addEventListener('click', this.create.bind(this));
    // étape pour ajouter un écouteur d'événement pour mettre à jour un élément.
    document.querySelector('.btn-update').addEventListener('click', this.update.bind(this));

    document.addEventListener('click', event => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }
      
      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }
  
  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach(item => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach(item => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date()
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter(item => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }
  
  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map(item => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }
}

export default Todo;
```

Maintenant, toutes les opérations CRUD ont été complétées. Il reste une dernière étape qui ne fait pas partie de CRUD mais qui fait partie de l'application Todo. Il s'agit de marquer les éléments comme terminés. La fonction ci-dessous permettra d'y parvenir :

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
    document
      .querySelector('.btn-update')
      .addEventListener('click', this.update.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }

  // étape pour marquer une tâche comme complète
  setTaskComplete(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['done'] = true;
      }

      return item;
    });

    this.render();
  }
}

export default Todo;
```

Encore une fois, suivez le même modèle que les autres fonctions :

* obtenez l'id de l'attribut `data-id` du bouton
* parcourez `mockData` et trouvez l'élément pertinent et définissez sa propriété `done` sur `true` et `retournez` cet élément
* enfin, ré-affichez `mockData` en appelant la fonction `render`.

Encore une fois, utilisez la même logique pour déclencher la fonction `delete`, et ajoutez le code ci-dessous au constructeur pour marquer les tâches comme complètes :

```js
class Todo {
  constructor() {
    let self = this;

    this.list = document.querySelector('.list-items');
    this.render();

    document
      .querySelector('.btn-add-item')
      .addEventListener('click', this.create.bind(this));
    document
      .querySelector('.btn-update')
      .addEventListener('click', this.update.bind(this));

    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('btn-delete')) {
        self.remove(event);
      }

      if (event.target.classList.contains('btn-edit')) {
        self.renderEditForm(event);
      }
      // étape pour ajouter un écouteur d'événement au bouton de complétion
      if (event.target.classList.contains('btn-complete')) {
        self.setTaskComplete(event);
      }
    });
  }

  renderEditForm(event) {
    let id = event.target.getAttribute('data-id');

    document.querySelector('.edit-popup').classList.remove('hide');
    document.querySelector('.edit-popup').classList.add('show');
    document.querySelector('.btn-update').setAttribute('data-id', id);

    mockData.forEach((item) => {
      if (item.id === id) {
        document.querySelector('.edit-item').value = item.title;
      }
    });
  }

  render() {
    this.list.innerHTML = '';

    mockData.forEach((item) => {
      this.createDomElements(item.id);
      this.li.insertAdjacentHTML('afterbegin', item.title);

      if (item.done) {
        this.li.classList.add('done');
      }

      this.list.appendChild(this.li);
    });
  }

  createDomElements(id) {
    this.li = document.createElement('li');
    this.edit = document.createElement('button');
    this.delete = document.createElement('button');
    this.complete = document.createElement('button');

    this.edit.classList.add('btn-edit');
    this.delete.classList.add('btn-delete');
    this.complete.classList.add('btn-complete');

    this.delete.setAttribute('data-id', id);
    this.edit.setAttribute('data-id', id);
    this.complete.setAttribute('data-id', id);

    this.edit.innerHTML = 'Edit';
    this.delete.innerHTML = 'Delete';
    this.complete.innerHTML = 'Complete';

    this.li.appendChild(this.delete);
    this.li.appendChild(this.edit);
    this.li.appendChild(this.complete);
  }

  create() {
    let todoItem = document.querySelector('.item').value;

    let newItem = {
      id: Date.now().toString(),
      title: todoItem,
      done: false,
      date: new Date(),
    };

    mockData.push(newItem);

    document.querySelector('.item').value = '';
    this.render();
  }

  remove(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.filter((item) => {
      if (item.id !== id) {
        return item;
      }
    });

    this.render();
  }

  update(event) {
    let id = event.target.getAttribute('data-id');
    let itemTobeUpdated = document.querySelector('.edit-item').value;

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['title'] = itemTobeUpdated;
      }

      return item;
    });

    document.querySelector('.edit-popup').classList.remove('show');
    document.querySelector('.edit-popup').classList.add('hide');

    this.render();
  }

  setTaskComplete(event) {
    let id = event.target.getAttribute('data-id');

    mockData = mockData.map((item) => {
      if (item.id === id) {
        item['done'] = true;
      }

      return item;
    });

    this.render();
  }
}

export default Todo;
```

Voici un peu de CSS de base que j'ai utilisé pour ce tutoriel — rien de fantaisiste :

```css
.show {
  display: block;
}

.hide {
  display: none;
}

.done {
  text-decoration: line-through;
}
```

C'est tout pour les opérations CRUD en JavaScript vanilla ! L'étape suivante consiste à convertir cela en une application Angular et React pour voir la différence et découvrir à quel point ces frameworks sont pratiques.

Pour obtenir le code et le projet complet, clonez le dépôt ci-dessous :

[https://github.com/zafar-saleem/todo](https://github.com/zafar-saleem/todo)