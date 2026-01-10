---
title: Comment réagir aux actions de l'utilisateur et du navigateur avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-09T00:47:36.000Z'
originalURL: https://freecodecamp.org/news/reacting-to-actions-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment réagir aux actions de l'utilisateur et du navigateur avec JavaScript
seo_desc: 'By Deborah Kurata

  When a user clicks a button on a webpage, the user expects the page to respond to
  their action and do something: play the game, buy the product, display a message,
  and so on.

  In this tutorial, we walk through how to use JavaScript t...'
---

Par Deborah Kurata

Lorsque l'utilisateur clique sur un bouton d'une page web, il s'attend à ce que la page réagisse à son action et fasse quelque chose : jouer au jeu, acheter le produit, afficher un message, et ainsi de suite.

Dans ce tutoriel, nous allons voir comment utiliser JavaScript pour réagir aux actions de l'utilisateur ou du navigateur, appelées **événements**, et exécuter du code pour faire quelque chose. Vous pouvez utiliser les techniques présentées ici pour rendre vos pages web plus interactives. 

Vous pouvez également regarder cette vidéo associée qui explique comment réagir aux événements avec JavaScript.

%[https://youtu.be/DyCS-D-7hOE]

## **Étapes de base**

Pour que notre code JavaScript réagisse à une action sur notre page, nous suivons trois étapes :

* Tout d'abord, nous trouvons l'élément HTML qui peut nous notifier de l'action. Il peut s'agir d'un bouton sur lequel l'utilisateur clique, d'une zone de texte dans laquelle l'utilisateur tape ou d'un élément sur lequel l'utilisateur passe la souris.
* Une fois que nous avons trouvé l'élément, nous écoutons les événements sur cet élément. L'événement `click`, `keypress` ou `mouseover`, par exemple.
* Enfin, nous réagissons à l'événement, en exécutant du code lorsque l'événement se produit.

Par exemple, supposons que nous développons un jeu de devinette de nombre comme illustré dans la Figure 1. Le jeu génère un nombre aléatoire et l'utilisateur essaie de deviner ce nombre. Nous voulons écouter l'événement `click` sur le bouton Devinez, et exécuter du code pour réagir en vérifiant la devinette de l'utilisateur par rapport au nombre aléatoire généré. 

En suivant les trois étapes que nous avons identifiées ci-dessus :

* Nous écrivons du code pour trouver l'élément HTML du bouton "Devinez".
* Nous utilisons la référence à l'élément trouvé pour écouter l'événement `click` du bouton, qui se produit lorsque l'utilisateur clique sur le bouton.
* Et lorsque le code est notifié de l'événement, le code réagit et exécute une fonction définie. Dans cet exemple, cette fonction lit la devinette de l'utilisateur à partir de l'élément d'entrée "Entrez votre devinette" et la compare au nombre généré aléatoirement.

![Capture d'écran d'un jeu de devinette de nombre et icônes pour les étapes décrites ci-dessus.](https://www.freecodecamp.org/news/content/images/2023/03/RespondingToActions-1.png)
_Figure 1. Jeu de devinette de nombre avec les étapes pour réagir aux actions_

Examinons ces étapes, une par une.

## **Comment trouver un élément HTML**

Lorsque nous regardons une vidéo en streaming, nous ne pouvons pas regarder la vidéo tant que nous ne l'avons pas trouvée dans notre service de streaming. Il en va de même pour nos éléments HTML.

Pour que notre code JavaScript fonctionne avec un élément sur une page HTML, notre code doit d'abord trouver cet élément. 

Nous conservons la référence à l'élément trouvé dans une variable. Une fois que nous avons une référence de variable à l'élément, nous pouvons lire son contenu, écrire un nouveau contenu ou réagir aux événements de cet élément.

Il existe plusieurs façons de trouver un élément sur une page HTML en utilisant JavaScript.

### Utiliser getElementById()

Si nous voulons trouver un élément par son attribut id unique, nous utilisons la méthode `getElementById()`. Cette méthode est disponible en utilisant l'objet `document` HTML. 

La méthode `getElementById()` retourne l'élément unique avec l'attribut id défini.

Le HTML pour notre jeu de devinette de nombre inclut un bouton avec un identifiant unique assigné à l'attribut id :

```html
<button id="guess-button">Devinez</button>
```

Puisque l'élément bouton a un attribut id, nous utilisons `getElementById()` pour trouver cet élément bouton et conserver une référence à celui-ci.

```javascript
const guessButton = document.getElementById('guess-button');
```

Dans le code ci-dessus, nous utilisons l'objet `document` du Document Object Model (DOM) et appelons la méthode `getElementById()`. Nous passons la valeur de l'attribut id, qui dans notre exemple est `guess-button`. 

Lorsque le code JavaScript est exécuté, la référence à l'élément trouvé est assignée à la variable spécifiée, `guessButton` dans cet exemple. Nous utilisons une constante car la référence à l'élément ne devrait pas changer pendant que l'utilisateur est sur la page web.

Dans de nombreux cas, nous voulons un élément particulier, donc `getElementById()` est souvent le meilleur choix.

### Utiliser getElementsByClassName()

Si nous voulons plutôt trouver un ensemble d'éléments par leur attribut de classe, nous utilisons la méthode `getElementsByClassName()`. Cette méthode est également disponible en utilisant l'objet `document` HTML.

La méthode `getElementsByClassName()` retourne une collection d'éléments qui ont tous un attribut de classe défini sur le nom de classe passé en argument.

Supposons que notre jeu de devinette de nombre a deux boutons, tous deux avec la même classe de style :

```html
<button class="btn">Devinez</button>
<button class="btn">Rejouer</button>
```

Utilisez `getElementsByClassName()` pour trouver les deux éléments boutons et conserver une référence à ceux-ci.

```javascript
const buttons = document.getElementsByClassName('btn');
```

Dans le code ci-dessus, nous utilisons l'objet `document` du DOM et appelons la méthode `getElementsByClassName()`. Nous passons la valeur de l'attribut de classe, qui dans notre exemple est `btn`. 

Lorsque le code JavaScript est exécuté, la référence aux éléments trouvés est stockée dans une collection. Naviguez dans cette collection en parcourant les éléments.

```javascript
for (const ele of buttons) {
  console.log("Bouton trouvé :", ele.textContent);
}

```

Cette boucle `for` itère à travers chaque élément bouton dans la collection fournie. Chaque fois dans la boucle, la variable `ele` est définie sur le bouton suivant dans la collection. Le code ci-dessus affiche le `textContent` de chaque bouton trouvé.

Utilisez `getElementsByClassName()` si vous devez configurer des événements pour plusieurs éléments similaires.

### Utiliser querySelector()

Si la recherche d'un élément nécessite des critères de sélection plus complexes, nous pouvons utiliser un sélecteur CSS pour trouver un élément en utilisant la méthode `querySelector()`. Toute syntaxe que vous utilisez comme sélecteur CSS, vous pouvez l'utiliser avec la méthode `querySelector()`.

La méthode `querySelector()` retourne le *premier* élément qui correspond au sélecteur CSS défini.

Pour plus d'informations sur les sélecteurs CSS, consultez cette vidéo.

%[https://youtu.be/59CE4o4qv7A]

Supposons que le bouton de notre jeu de devinette de nombre est dans un élément div et que nous voulons trouver cet élément div.

Voici le HTML :

```html
<div class="button-container">
   <button class="btn">Devinez</button>
</div>
```

Peut-être que nous ne pouvons pas modifier le HTML pour ajouter un id à l'élément div, donc nous allons trouver le div en utilisant un sélecteur de requête.

```javascript
const buttonContainer = document.querySelector("div.button-container");
```

Dans le code ci-dessus, nous utilisons l'objet `document` du DOM et appelons la méthode `querySelector()`. Nous passons le sélecteur de requête, qui dans notre exemple est un sélecteur de classe d'élément div.

Lorsque le code JavaScript est exécuté, la référence au premier élément trouvé qui correspond au sélecteur est assignée à la variable spécifiée, `buttonContainer` dans cet exemple.

Une fois que nous avons une variable qui référence notre élément ou nos éléments trouvés, nous pouvons utiliser cette variable pour écouter les événements sur cet élément.

## **Comment écouter les événements**

Un événement est une notification qu'une action s'est produite. Les événements peuvent provenir de l'utilisateur lorsqu'il clique sur un bouton, fait défiler, sélectionne un élément, presse une touche, redimensionne le navigateur, etc. Ou les événements peuvent provenir du navigateur lui-même lorsqu'il a fini de charger la page, par exemple.

Pour écouter un événement d'un élément, utilisez la référence à cet élément et appelez sa méthode `addEventListener()`.

```javascript
guessButton.addEventListener('click', displayEvent);
```

Nous passons à cette méthode le nom de l'événement, entre guillemets. Dans cet exemple, nous écoutons l'événement `click`. Le nom de l'événement est sensible à la casse, ce qui signifie qu'il doit avoir l'orthographe et la casse exactes de l'événement de l'élément.

Comment savons-nous le nom de cet événement ? Ou même quels événements nous pouvons écouter ?

Une excellente option est la documentation JavaScript sur developer.mozilla.org. Recherchez "event" et choisissez "Event reference". La référence Event identifie d'abord les types d'événements que nous pouvons écouter. Ensuite, elle fournit une liste d'événements. [Consultez-la ici](https://developer.mozilla.org/en-US/docs/Web/Events).

Mais qu'en est-il du deuxième argument de `addEventListener()` ?

## **Comment réagir à l'événement**

Comme nous l'avons vu ci-dessus, lorsque nous appelons `addEventListener()`, nous passons l'événement que nous voulons écouter. Nous passons également une fonction contenant le code pour réagir à cet événement. En d'autres termes, le code que nous voulons exécuter lorsque l'événement se produit. Nous appelons cela un **gestionnaire d'événements** car il gère l'événement lorsqu'il se produit.

Voici à nouveau le code pour `addEventListener()` :

```javascript
guessButton.addEventListener('click', displayEvent);
```

Remarquez le nom de la fonction. Nous n'incluons pas les parenthèses après le nom de la fonction car nous n'exécutons pas la fonction. Nous passons plutôt la fonction à l'écouteur d'événement. La fonction ne s'exécutera pas tant que l'événement ne se produira pas.

Lorsque le code est notifié de l'événement, la fonction passée en argument est exécutée. Dans notre exemple, la fonction `displayEvent()` s'exécute. Les détails de l'événement sont optionnellement passés à cette fonction. 

Dans cet exemple de code, les informations sur l'événement sont enregistrées dans la console du navigateur.

```javascript
function displayEvent(event) {
   console.log(event);
}
```

Si nous avons un gestionnaire d'événements simple, comme dans l'exemple ci-dessus, au lieu de passer le nom de la fonction, nous pouvons passer la fonction elle-même en utilisant une fonction fléchée.

```javascript
guessButton.addEventListener('click', event => console.log(event));
```

Une fonction fléchée est une syntaxe abrégée pour une fonction. Nous définissons le paramètre de l'événement ( `event` dans cet exemple), une flèche, et le corps de la fonction sur une ligne.

Pour plus d'informations sur les fonctions, y compris les fonctions fléchées, consultez cette vidéo.

%[https://youtu.be/j8oAbRAlcyE]

Maintenant, examinons un exemple.

## Exemple de jeu de devinette de nombre

Pour notre jeu de devinette de nombre, lorsque l'utilisateur clique sur le bouton de devinette, nous voulons lire la devinette de l'utilisateur à partir de la zone de texte et déterminer si la devinette correspond au nombre généré aléatoirement.

Tout d'abord, nous trouvons le bouton de devinette :

```javascript
const guessButton = document.getElementById('guess-button');
```

Ensuite, nous écoutons l'événement `click` et réagissons en traitant la devinette de l'utilisateur.

```javascript
guessButton.addEventListener('click', processGuess);
```

Notez que nous ne mettons pas le nom de la fonction entre guillemets car il s'agit d'une variable référençant notre fonction. Et nous ne mettons pas de parenthèses après le nom de la fonction car nous n'appelons pas la fonction. Nous passons plutôt la référence de la fonction. Nous voulons que le navigateur appelle cette fonction lorsque l'événement de clic se produit.

Voici la fonction `processGuess()` :

```javascript
function processGuess() {
  let feedbackText;
  if (guessInput){
    const guess = guessInput.valueAsNumber;

    if (guess === randomNumber) {
      feedbackText = `${guess} est correct ... Vous gagnez !`;
      displayPlayAgain(true);
    } else if (guess > randomNumber) {
      feedbackText = `${guess} est trop élevé`;
    } else {
      feedbackText = `${guess} est trop bas`;
    }
  }
  if (feedbackContainer) {
    feedbackContainer.innerHTML += '<br>' + feedbackText;
  }
}
```

Lorsque l'utilisateur clique sur le bouton "Devinez", le navigateur exécute ce code. La variable `guessInput` est une référence à la zone de texte "Entrez votre devinette". Si cette zone de texte a été trouvée, la valeur de la zone de texte est lue en utilisant `valueAsNumber`. Cette propriété fournit la valeur de la chaîne de la zone de texte sous forme de nombre.

Le code compare ensuite la devinette au nombre aléatoire généré et prépare le message approprié. Le `feedbackContainer` est une référence à un élément div pour afficher le message.

Le résultat est montré dans la Figure 2.

![Affichage du jeu](https://www.freecodecamp.org/news/content/images/2023/03/GamePlay.png)
_Figure 2. Jeu avec messages_

Vous pouvez trouver le code complet de ce jeu ici : [https://github.com/DeborahK/Gentle-Introduction-to-JavaScript](https://github.com/DeborahK/Gentle-Introduction-to-JavaScript)

## **Conclusion**

Pour réagir aux événements avec JavaScript, nous trouvons d'abord un élément HTML auquel nous voulons réagir. Nous écoutons ensuite les événements de cet élément en utilisant la méthode `addEventListener()`.

Le premier argument passé à `addEventListener()` est le nom de l'événement. Assurez-vous de l'écrire et de le caser correctement. Utilisez la référence Event sur developer.mozilla.org pour la liste des événements.

Le deuxième argument est le gestionnaire d'événements. C'est la fonction à exécuter lorsque l'événement se produit. Passez une fonction nommée ou une fonction fléchée.

Pour plus d'informations sur la programmation avec JavaScript et pour construire notre jeu de devinette de nombre étape par étape, consultez ce cours :

%[https://youtu.be/jJLn5XxyXWc]

Maintenant que vous savez comment écouter et réagir aux événements, que ferez-vous avec ce pouvoir ?