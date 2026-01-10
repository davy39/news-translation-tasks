---
title: J'ai créé la même application en React et Vue. Voici les différences.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T17:09:58.000Z'
originalURL: https://freecodecamp.org/news/i-created-the-same-app-in-react-and-vue-here-are-the-differences-67e71421df31
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mJ-qdNqldpgae2U5oS0qDg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: J'ai créé la même application en React et Vue. Voici les différences.
seo_desc: 'By Sunil Sandhu

  Having used Vue at my current workplace, I had a fairly solid understanding of how
  it all worked. I was, however, curious to know what the grass was like on the other
  side of the fence — the grass in this scenario being React.

  I’d rea...'
---

Par Sunil Sandhu

Ayant utilisé **Vue** dans mon lieu de travail actuel, j'avais une compréhension assez solide de son fonctionnement. Cependant, j'étais curieux de savoir à quoi ressemblait l'herbe de l'autre côté de la clôture — l'herbe dans ce scénario étant React.

J'avais lu la documentation React et regardé quelques vidéos tutoriels et, bien qu'elles soient excellentes, ce que je voulais vraiment savoir, c'était à quel point **React** était différent de **Vue**.

Par « différent », je ne voulais pas dire des choses comme s'ils avaient tous les deux des **DOM virtuels** ou comment ils procédaient pour rendre les pages. Je voulais que quelqu'un prenne le temps d'expliquer le code et de me dire ce qui se passait ! Je voulais trouver un article qui prenne le temps d'expliquer ces différences afin que quelqu'un nouveau dans **Vue** ou **React** (ou dans le développement web en général) puisse mieux comprendre les différences entre les deux.

Mais je n'ai rien trouvé qui aborde cela. Alors je me suis rendu compte que je devrais me lancer et construire cela moi-même afin de voir les similitudes et les différences. En faisant cela, j'ai pensé que je pourrais documenter tout le processus afin qu'un article sur ce sujet existe enfin.

![Image](https://cdn-media-1.freecodecamp.org/images/gxU7ZAu4Ey12iGnSlpGwYH6i83ncsHcmIEDj)
_Qui le porte mieux ?_

J'ai décidé d'essayer de construire une application To Do assez standard qui permet à un utilisateur d'ajouter et de supprimer des éléments de la liste. Les deux applications ont été construites en utilisant les **CLI** par défaut (**create-react-app** pour **React**, et **vue-cli** pour **Vue**). *CLI signifie Command Line Interface, au fait*. ?

#### Bref, cette introduction est déjà plus longue que je ne l'avais prévu. Alors commençons par jeter un rapide coup d'œil à l'apparence des deux applications :

![Image](https://cdn-media-1.freecodecamp.org/images/V9NdEyLFZvFCGDQ731P892-lTF3lcXP9laP1)
_Vue vs React : La Force Irrésistible rencontre l'Objet Immuable_

Le code CSS pour les deux applications est exactement le même, mais il y a des différences dans l'emplacement de ces fichiers. Cela dit, examinons la structure des fichiers des deux applications :

![Image](https://cdn-media-1.freecodecamp.org/images/GV3G8hb9X8mA-vnRcfRpboA59nVO46ZTIknR)
_Qui le porte mieux ?_

Vous verrez que leurs structures sont presque identiques. La seule différence ici est que l'application React a trois fichiers CSS, alors que l'application Vue n'en a aucun. Cela est dû au fait que dans create-react-app, **un composant React aura un fichier d'accompagnement pour contenir ses styles, alors que le CLI Vue adopte une approche globale où les styles sont déclarés à l'intérieur du fichier de composant lui-même**.

En fin de compte, ils atteignent tous les deux le même objectif, et rien n'empêche de structurer votre CSS différemment dans React ou Vue. Cela dépend vraiment des préférences personnelles — vous entendrez beaucoup de discussions dans la communauté des développeurs sur la manière dont le CSS devrait être structuré. Pour l'instant, nous allons simplement suivre la structure définie dans les deux CLI.

Mais avant d'aller plus loin, examinons rapidement à quoi ressemblent un composant Vue typique et un composant React :

![Image](https://cdn-media-1.freecodecamp.org/images/OYJ9J1mD7ENdqSy0d66zRGSRivznwiHyi1HH)
_Vue à gauche. React à droite_

Maintenant que cela est fait, plongeons dans les détails !

### Comment mutons-nous les données ?

Mais d'abord, que voulons-nous dire par « mutons les données » ? Cela semble un peu technique, n'est-ce pas ? Cela signifie simplement changer les données que nous avons stockées. Donc si nous voulions changer la valeur du nom d'une personne de John à Mark, nous « mutons les données ».

C'est là qu'une différence clé entre React et Vue réside. **Alors que Vue crée essentiellement un objet de données, où les données peuvent être librement mises à jour, React crée un objet d'état, où un peu plus de travail est nécessaire pour effectuer les mises à jour**.

Maintenant, React met en œuvre ce travail supplémentaire pour une bonne raison, et nous allons y venir dans un instant. Mais d'abord, examinons l'objet **data** de Vue et l'objet **state** de React :

![Image](https://cdn-media-1.freecodecamp.org/images/sZzmUCmi9Frf20OgPlXeFxeYutk5nVpYLyIo)

![Image](https://cdn-media-1.freecodecamp.org/images/pMzlry1q9FfWOoMj6TnLJoRBmfobAzf3MIuE)
_Objet de données Vue à gauche. Objet d'état React à droite._

Ainsi, vous pouvez voir que nous avons passé les mêmes données dans les deux, mais elles sont simplement étiquetées différemment. Donc, passer les données initiales dans nos composants est très, très similaire. Mais comme nous l'avons mentionné, la manière dont nous procédons pour changer ces données diffère entre les frameworks.

Supposons que nous avons un élément de données appelé `**name: 'Sunil'**`.

Dans Vue, nous référençons cela en appelant `this.name`. Nous pouvons également le mettre à jour en appelant `**this.name = 'John'**`. Cela changerait mon nom en John. Je ne suis pas sûr de ce que je pense d'être appelé John, mais bon, les choses arrivent ! ?

Dans React, nous référençons la même donnée en appelant `**this.state.name**`. Maintenant, la différence clé ici est que nous ne pouvons pas simplement écrire `**this.state.name = 'John'**`, car React a des restrictions en place pour empêcher ce type de mutation facile et insouciante. Donc dans React, nous écrivons quelque chose comme `**this.setState({name: 'John'})**`.

Bien que cela fasse essentiellement la même chose que ce que nous avons réalisé dans Vue, le petit effort supplémentaire est là parce que Vue combine essentiellement sa propre version de setState par défaut chaque fois qu'une donnée est mise à jour.

En bref, **React nécessite setState et ensuite les données mises à jour à l'intérieur, alors que Vue fait l'hypothèse que vous voudriez faire cela si vous mettez à jour des valeurs à l'intérieur de l'objet de données**.

Pourquoi React se donne-t-il cette peine, et pourquoi setState est-il même nécessaire ? Laissons [Revanth Kumar](https://medium.com/@revanth0212) nous expliquer :

> « C'est parce que React veut relancer certains hooks de cycle de vie, [tels que] componentWillReceiveProps, shouldComponentUpdate, componentWillUpdate, render, componentDidUpdate, chaque fois que l'état change. Il saura que l'état a changé lorsque vous appelez la fonction setState. Si vous mutiez directement l'état, React devrait faire beaucoup plus de travail pour suivre les changements et quels hooks de cycle de vie exécuter, etc. Donc pour simplifier, React utilise setState. »

![Image](https://cdn-media-1.freecodecamp.org/images/BjPx0SKGGAUNqBoLjDJRUwtctgPimca0DtjG)
_Bean savait mieux_

Maintenant que nous avons traité des mutations, plongeons dans les détails en examinant comment nous procéderions pour ajouter de nouveaux éléments à nos deux applications To Do.

### Comment créons-nous de nouveaux éléments To Do ?

#### React :

```jsx
createNewToDoItem = () => {
    this.setState( ({ list, todo }) => ({
      list: [
          ...list,
        {
          todo
        }
      ],
      todo: ''
    })
  );
};
```

#### Comment React a-t-il fait cela ?

Dans React, notre champ de saisie a un attribut appelé **value**. Cette valeur est automatiquement mise à jour grâce à l'utilisation de quelques fonctions qui se lient pour créer quelque chose qui ressemble étroitement à la **liaison bidirectionnelle** (si vous n'avez jamais entendu parler de cela auparavant, il y a une explication plus détaillée dans la section _Comment Vue a-t-il fait cela_ après celle-ci). Nous créons cette forme de liaison bidirectionnelle en ayant un écouteur d'événement **onChange** supplémentaire attaché au champ **input**.

Examinons rapidement le champ **input** pour que vous puissiez voir ce qui se passe :

```jsx
<input type="text" 
       value={this.state.todo} 
       onChange={this.handleInput}/>
```

La fonction handleInput est exécutée chaque fois que la valeur du champ de saisie change. Elle met à jour le **todo** qui se trouve à l'intérieur de l'objet d'état en le définissant sur ce qui se trouve dans le champ de saisie. Cette fonction ressemble à ceci :

```jsx
handleInput = e => {
  this.setState({
    todo: e.target.value
  });
};
```

Maintenant, chaque fois qu'un utilisateur appuie sur le bouton **+** sur la page pour ajouter un nouvel élément, la fonction `**createNewToDoItem**` exécute essentiellement this.setState et lui passe une fonction.

Cette fonction prend deux paramètres, le premier étant le tableau entier `**list**` de l'objet d'état, le second étant le `**todo**` (qui est mis à jour par la fonction `**handleInput**`). La fonction retourne ensuite un nouvel objet, qui contient la liste entière `**list**` d'avant et ajoute ensuite `**todo**` à la fin de celle-ci. La liste entière est ajoutée grâce à l'utilisation d'un opérateur de décomposition (Googlez cela si vous ne l'avez jamais vu auparavant — c'est la syntaxe ES6).

Enfin, nous définissons `**todo**` sur une chaîne vide, ce qui met automatiquement à jour la **value** à l'intérieur du champ **input**.

#### Vue :

```js
createNewToDoItem() {
    this.list.push(
        {
            'todo': this.todo
        }
    );
    this.todo = '';
}
```

#### Comment Vue a-t-il fait cela ?

Dans Vue, notre champ **input** a un gestionnaire appelé **v-model**. Cela nous permet de faire ce que l'on appelle la **liaison bidirectionnelle**. Examinons rapidement notre champ de saisie, puis nous expliquerons ce qui se passe :

```js
<input type="text" v-model="todo"/>
```

V-Model lie la saisie de ce champ à une clé que nous avons dans notre objet de données appelée toDoItem. Lorsque la page se charge, nous avons `**toDoItem**` défini sur une chaîne vide, comme suit : `**todo: ''**`. Si cela avait déjà des données, comme `**todo: 'ajoutez du texte ici'**`, notre champ de saisie se chargerait avec _ajoutez du texte ici_ déjà à l'intérieur du champ de saisie.

En tout cas, en revenant à une chaîne vide, tout texte que nous tapons à l'intérieur du champ de saisie est lié à la valeur de `**todo**`. C'est effectivement une liaison bidirectionnelle (le champ de saisie peut mettre à jour l'objet de données et l'objet de données peut mettre à jour le champ de saisie).

Ainsi, en regardant le bloc de code `**createNewToDoItem()**` précédent, nous voyons que nous poussons le contenu de `**todo**` dans le tableau `**list**` puis mettons à jour `**todo**` avec une chaîne vide.

### Comment supprimons-nous de la liste ?

#### React :

```jsx
deleteItem = indexToDelete => {
    this.setState(({ list }) => ({
      list: list.filter((toDo, index) => index !== indexToDelete)
    }));
};
```

#### Comment React a-t-il fait cela ?

Alors que la fonction deleteItem est située dans **ToDo.js**, j'ai pu très facilement y faire référence dans **ToDoItem.js** en passant d'abord la fonction `**deleteItem()**` en tant que prop sur `**<ToDoItem**` comme suit :

```jsx
<ToDoItem deleteItem={this.deleteItem.bind(this, key)}/>
```

Cela passe la fonction vers le bas pour la rendre accessible à l'enfant. Vous verrez ici que nous liaisons également `**this**` ainsi que le passage du paramètre key, car la clé est ce que la fonction va utiliser pour différencier quel **ToDoItem** nous essayons de supprimer lorsque nous cliquons dessus. Ensuite, à l'intérieur du composant **ToDoItem**, nous faisons ce qui suit :

```jsx
<div className="ToDoItem-Delete" onClick={this.props.deleteItem}>-</div>
```

Tout ce que j'ai dû faire pour référencer une fonction qui se trouvait dans le composant parent était de référencer `**this.props.deleteItem**`.

#### Vue :

```js
onDeleteItem(todo){
  this.list = this.list.filter(item => item !== todo);
}
```

#### Comment Vue a-t-il fait cela ?

Une approche légèrement différente est requise dans Vue. Nous devons essentiellement faire trois choses ici :

Tout d'abord, sur l'élément où nous voulons appeler la fonction :

```js
<div class="ToDoItem-Delete" @click="deleteItem(todo)">-</div>
```

Ensuite, nous devons créer une fonction d'émission en tant que méthode à l'intérieur du composant enfant (dans ce cas, **ToDoItem.vue**), qui ressemble à ceci :

```js
deleteItem(todo) {
    this.$emit('delete', todo)
}
```

Avec cela, vous remarquerez que nous référençons en fait une **fonction** lorsque nous ajoutons **ToDoItem.vue** à l'intérieur de **ToDo.vue** :

```js
<ToDoItem v-for="todo in list" 
          :todo="todo" 
          @delete="onDeleteItem" // <-- ceci :)
          :key="todo.id" />
```

C'est ce que l'on appelle un **écouteur d'événement personnalisé**. Il écoute toute occasion où une émission est déclenchée avec la chaîne de caractères `'delete'`. Si cela se produit, il déclenche une fonction appelée `**onDeleteItem**`. Cette fonction se trouve à l'intérieur de **ToDo.vue**, plutôt que dans **ToDoItem.vue**. Comme nous l'avons discuté précédemment, elle filtre simplement le tableau `**todo**` à l'intérieur de l'objet `**data**` pour supprimer l'élément sur lequel on a cliqué.

Il est également intéressant de noter ici que dans l'exemple Vue, j'aurais pu simplement écrire la partie `**$emit**` à l'intérieur de l'écouteur `**@click**`, comme suit :

```js
<div class="ToDoItem-Delete" @click="$emit('delete', todo)">-</div>
```

Cela aurait réduit le nombre d'étapes de 3 à 2, et cela dépend simplement des préférences personnelles.

En bref, **les composants enfants dans React auront accès aux fonctions parent via** `**this.props**` (à condition que vous passiez les props vers le bas, ce qui est une pratique assez standard — vous rencontrerez cela de nombreuses fois dans d'autres exemples React). Dans Vue, en revanche, **vous devez émettre des événements depuis l'enfant qui seront généralement collectés à l'intérieur du composant parent**.

### Comment passons-nous les écouteurs d'événements ?

#### React :

Les écouteurs d'événements pour des choses simples comme les événements de clic sont simples. Voici un exemple de la manière dont nous avons créé un événement de clic pour un bouton qui crée un nouvel élément ToDo :

```jsx
<div className="ToDo-Add" onClick={this.createNewToDoItem}>+</div>.
```

Super facile ici, et cela ressemble presque à la manière dont nous gérerions un `onClick` en ligne avec du JS vanilla. Comme mentionné dans la section Vue, il a fallu un peu plus de temps pour configurer un écouteur d'événement pour gérer chaque fois que la touche Entrée était pressée. Cela nécessitait essentiellement qu'un événement `onKeyPress` soit géré par la balise input, comme suit :

```jsx
<input type="text" onKeyPress={this.handleKeyPress}/>.
```

Cette fonction déclenchait essentiellement la fonction `**createNewToDoItem**` chaque fois qu'elle reconnaissait que la touche 'enter' avait été pressée, comme suit :

```
handleKeyPress = (e) => {
  if (e.key === 'Enter') {
    this.createNewToDoItem();
  }
};
```

#### Vue :

Dans Vue, c'est super simple. Nous utilisons simplement le symbole **@**, puis le type d'écouteur d'événement que nous voulons. Donc, par exemple, pour ajouter un écouteur d'événement de clic, nous pourrions écrire ce qui suit :

```js
<div class="ToDo-Add" @click="createNewToDoItem()">+</div>
```

Note : `**@click**` est en fait une abréviation pour écrire `**v-on:click**`. Le truc cool avec les écouteurs d'événements Vue est qu'il y a aussi un tas de choses que vous pouvez enchaîner avec eux, comme `.once`, qui empêche l'écouteur d'événement d'être déclenché plus d'une fois. Il y a aussi un tas de raccourcis lorsqu'il s'agit d'écrire des écouteurs d'événements spécifiques pour gérer les frappes de touches.

J'ai trouvé que cela prenait beaucoup plus de temps pour créer un écouteur d'événement dans React pour créer de nouveaux éléments ToDo chaque fois que la touche Entrée était pressée. Dans Vue, j'ai pu simplement écrire :

```js
<input type="text" v-on:keyup.enter="createNewToDoItem"/>
```

#### Comment passons-nous les données à un composant enfant ?

#### React :

Dans React, nous passons les props au composant enfant au moment où il est créé. Par exemple :

```jsx
<ToDoItem key={key} item={todo} />
```

Ici, nous voyons deux props passées au composant **ToDoItem**. À partir de ce moment, nous pouvons maintenant les référencer dans le composant enfant via `**this.props**`. Donc pour accéder à la prop `**item.todo**`, nous appelons simplement `**this.props.item**`.

#### Vue :

Dans Vue, nous passons les props au composant enfant au moment où il est créé. Par exemple :

```js
<ToDoItem v-for="todo in list" 
            :todo="todo"
            :key="todo.id"
            @delete="onDeleteItem" />
```

Une fois cela fait, nous les passons ensuite dans le tableau des props dans le composant enfant, comme suit : `**props: [ 'todo' ]**`. Ceux-ci peuvent ensuite être référencés dans l'enfant par leur nom — donc dans notre cas, `**'todo'**`.

### Comment émettons-nous des données vers un composant parent ?

#### React :

Nous passons d'abord la fonction au composant enfant en la référençant en tant que prop à l'endroit où nous appelons le composant enfant. Ensuite, nous ajoutons l'appel à la fonction sur l'enfant par quelque moyen, comme un `**onClick**`, en référençant `**this.props.whateverTheFunctionIsCalled**`. Cela déclenchera ensuite la fonction qui se trouve dans le composant parent.

Nous pouvons voir un exemple de ce processus entier dans la section _'Comment supprimons-nous de la liste'_.

#### Vue :

Dans notre composant enfant, nous écrivons simplement une fonction qui émet une valeur vers la fonction parent. Dans notre composant parent, nous écrivons une fonction qui écoute lorsque cette valeur est émise, ce qui peut ensuite déclencher un appel de fonction. Nous pouvons voir un exemple de ce processus entier dans la section _'Comment supprimons-nous de la liste'_.

### Et voilà ! ?

Nous avons examiné comment nous ajoutons, supprimons et changeons les données, passons les données sous forme de props du parent à l'enfant, et envoyons les données de l'enfant au parent sous forme d'écouteurs d'événements.

Il existe, bien sûr, de nombreuses autres petites différences et particularités entre React et Vue, mais espérons que le contenu de cet article a aidé à servir de base pour comprendre comment les deux frameworks gèrent les choses ?

Si vous avez trouvé cela utile, veuillez partager sur les réseaux sociaux et commenter !

#### Liens Github vers les deux applications :

Vue ToDo : [https://github.com/sunil-sandhu/vue-todo](https://github.com/sunil-sandhu/vue-todo)

React ToDo : [https://github.com/sunil-sandhu/react-todo](https://github.com/sunil-sandhu/react-todo)

**Il s'agit d'une republication syndiquée pour freeCodeCamp en collaboration avec [Javascript In Plain English](https://medium.com/javascript-in-plain-english). La version originale de cet article peut être trouvée [ici](https://medium.com/javascript-in-plain-english/i-created-the-exact-same-app-in-react-and-vue-here-are-the-differences-e9a1ae8077fd).**