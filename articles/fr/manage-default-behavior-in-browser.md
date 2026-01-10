---
title: Comment gérer les comportements par défaut du navigateur avec event.preventDefault()
  et event.stopPropagation()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-04T19:59:02.000Z'
originalURL: https://freecodecamp.org/news/manage-default-behavior-in-browser
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-startup-stock-photos-7359.jpg
tags:
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment gérer les comportements par défaut du navigateur avec event.preventDefault()
  et event.stopPropagation()
seo_desc: "By Dillion Megida\nBrowsers have default interactions and behaviors for\
  \ different events. \nFor example, when a user clicks a \"submit\" button on a form,\
  \ the form is submitted to a URL by default. \nWhen the child of an element is clicked,\
  \ the click even..."
---

Par Dillion Megida

Les navigateurs ont des interactions et des comportements par défaut pour différents événements. 

Par exemple, lorsqu'un utilisateur clique sur un bouton "submit" d'un formulaire, le formulaire est soumis à une URL par défaut. 

Lorsque l'enfant d'un élément est cliqué, l'événement de clic se produit également sur l'élément car il est le conteneur principal.

Dans certains cas, vous pouvez vouloir remplacer ces comportements par défaut. Dans cet article, nous allons apprendre ce que sont les méthodes `event.preventDefault()` et `event.stopPropagation()` et comment les utiliser pour annuler certaines actions par défaut qui se produisent dans le navigateur.

## event.preventDefault()

Cette méthode empêche les actions par défaut que les navigateurs effectuent lorsqu'un événement est déclenché. 

Voici quelques exemples d'actions par défaut sur les pages web et comment les remplacer avec `event.preventDefault()`.

### Comment remplacer la soumission de formulaire par défaut

Lorsque l'utilisateur soumet un formulaire (le bouton de soumission est cliqué), l'action par défaut du formulaire est de soumettre les données du formulaire à une URL qui traite les données.

Les éléments de formulaire ont les attributs `action` et `method` qui spécifient l'URL à laquelle soumettre le formulaire et le type de requête (`get`, `post`, etc.), respectivement. 

Si ces attributs ne sont pas fournis, l'URL par défaut est l'URL actuelle sur laquelle le formulaire a été soumis, et la méthode est `get`.

Par exemple, ce code :

```html
<form>
  <input name="email" />
  <input name="password" />
  <input type="submit" />
</form>
```

produit cette page :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-9.png)

En soumettant le formulaire avec les entrées "dillion" et "password", vous pouvez voir une requête `get` soumise à `127.0.0.1:5500/index.html` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-10.png)

Cette action est la manière dont les navigateurs gèrent les formulaires par défaut. 

Mais vous pouvez vouloir faire plus de choses avec les données avant d'envoyer une requête. Cela est particulièrement courant dans l'approche actuelle de gestion des formulaires. 

Vous pouvez vouloir faire une validation des données, des vérifications, un traitement, configurer des en-têtes, etc., avant d'envoyer la requête à une URL. 

Dans ces scénarios, vous voudrez empêcher l'action par défaut du formulaire. Voici comment :

```html
<form id='form'>
  ...
</form>
```

```js
const form = document.getElementById('form')

form.addEventListener('submit', (event) => {
  event.preventDefault()
  
  // traiter les données et soumettre une requête manuellement
})
```

De cette manière, la soumission du formulaire est entre vos mains.

### Comment remplacer l'action par défaut lors du clic sur un lien

Lorsque vous cliquez sur un lien (une balise d'ancrage `a` avec un attribut `href`), l'action par défaut est une navigation dans le navigateur vers le lien cliqué.

Et si vous vouliez intercepter cette action et peut-être faire quelque chose avant la navigation ? Par exemple, vérifier que l'utilisateur a accès à la page vers laquelle il veut naviguer. Voici comment procéder :

```html
<a id="link" href="https://google.com">Google</a>
```

```js
const link = document.getElementById("link")

link.addEventListener("click", event => {
  event.preventDefault()

  // faire quelque chose et naviguer
})
```

Vous pouvez l'essayer. Lorsque vous cliquez sur le lien "Google", aucune navigation ne se produit – car vous avez empêché l'action de navigation par défaut. Maintenant, vous devez gérer la navigation vous-même.


## event.stopPropagation()

La propagation est l'acte de propager quelque chose, dans ce cas, des événements. La méthode `stopPropagation` est utilisée pour empêcher la propagation des événements lorsqu'un événement est déclenché sur un élément.

En JavaScript, lorsque vous déclenchez un événement sur un élément, il remonte dans l'arborescence vers les parents et les ancêtres de cet élément. Basiquement, l'élément avec l'événement est "à l'intérieur" du conteneur parent, donc le parent reçoit également les événements.

Pour mieux expliquer cela, je vais utiliser un exemple.

### Cliquer sur l'enfant d'un élément

Supposons que vous avez les éléments suivants :

```html
<div>
  <button>Cliquez-moi</button>
</div>
```

Lorsque vous cliquez sur le `button`, vous cliquez également sur le conteneur `div` car le bouton est dans le conteneur. Cette logique signifie que l'événement de clic se propage du bouton au conteneur, et l'événement continue de se propager à tous les grands-parents jusqu'à ce qu'il atteigne la racine.

Pour vérifier cela, je vais expliquer comment cela fonctionne avec ce code :

```html
<div id="div">
  <button id="button">Cliquez-moi</button>
</div>
```

```js
const div = document.getElementById('div')
const button = document.getElementById('button')

button.addEventListener('click', () => {
  console.log('bouton cliqué')
})

div.addEventListener('click', () => {
  console.log('conteneur div cliqué')
})
```

Lorsque vous essayez d'exécuter cela dans votre navigateur et que vous cliquez sur le bouton, vous obtiendrez ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-4.png)

Le conteneur `div` reçoit également l'événement de clic, donc la fonction de rappel de clic est également appelée.

Les propagations d'événements sont le comportement par défaut des événements et des éléments, mais dans certains cas, vous ne voulez pas certains comportements. Parmi de nombreux exemples, en voici un.

Voici la fenêtre contextuelle Nouveau Message de Gmail :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-6.png)

En haut, vous avez les trois boutons d'action. L'un minimise la fenêtre contextuelle, l'un la met en plein écran, et l'un la ferme.

Mais la barre supérieure, avec le texte "Nouveau Message", a également un gestionnaire de clic, de sorte que lorsqu'elle est cliquée, elle minimise la fenêtre contextuelle :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-8.png)

Une chose que vous voulez éviter ici est que, lors du clic sur l'un des boutons, vous ne voulez pas que l'événement de clic se propage à la barre supérieure et exécute également la fonction pour cet événement. Ce que je veux dire, c'est que, par exemple, lors du clic sur le bouton de fermeture, vous ne voulez pas que la barre supérieure se minimise également. 

Dans des cas comme celui-ci, vous voulez arrêter la propagation.

Supposons que la fenêtre contextuelle est construite comme ceci :

```html
<div id='top-bar'>
  <!-- L'élément Message -->
  <!-- Les Boutons -->
</div>
```

```js
const topBar = document.getElementById('top-bar')
const closeButton = document.getElementById('close-btn')

topBar.addEventListener('click', () => {
  // minimiser ou maximiser la fenêtre contextuelle
})

closeButton.addEventListener('click', () => {
  // fermer la fenêtre contextuelle
})
```

Vous voudrez également ajouter la méthode `stopPropagation` à l'écouteur du bouton, pour éviter de propager l'événement à la barre supérieure. Pour ce faire, vous mettrez à jour l'écouteur du bouton comme suit :

```js
closeButton.addEventListener('click', (event) => {
  event.stopPropagation()
  // fermer la fenêtre contextuelle
})
```

Avec cela en place, la barre supérieure ne recevra l'événement de clic que lorsqu'elle sera directement cliquée.

## Conclusion

La différence entre `event.preventDefault()` et `event.stopPropagation()` est que le premier empêche les actions par défaut effectuées par le navigateur, tandis que le second empêche les comportements par défaut des événements – se propageant dans l'arborescence.

Ces actions et comportements par défaut ne sont pas des erreurs, et vous n'avez pas à vous en soucier pendant que vous codez. Mais il existe des scénarios où vous voulez les remplacer, comme nous l'avons vu dans les exemples de cet article.