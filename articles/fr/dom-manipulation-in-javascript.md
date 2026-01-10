---
title: Manipulation du DOM en JavaScript – Un Guide Complet pour Débutants
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-23T08:16:19.000Z'
originalURL: https://freecodecamp.org/news/dom-manipulation-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Beige-Aesthetic-Neutral-Thesis-Defense-Presentation-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Manipulation du DOM en JavaScript – Un Guide Complet pour Débutants
seo_desc: "JavaScript, the language of the web, empowers developers to create dynamic\
  \ and interactive web pages. One of the key features that enables this interactivity\
  \ is Document Object Model (DOM) manipulation. \nDOM manipulation allows developers\
  \ to interact..."
---

JavaScript, le langage du web, permet aux développeurs de créer des pages web dynamiques et interactives. L'une des fonctionnalités clés qui permet cette interactivité est la manipulation du Document Object Model (DOM).

La manipulation du DOM permet aux développeurs d'interagir avec et de modifier la structure, le style et le contenu des pages web. Dans cet article, nous explorerons les fondamentaux de la manipulation du DOM en JavaScript, en décomposant des concepts complexes en extraits faciles à comprendre.

## Qu'est-ce que le DOM ?

Le Document Object Model (DOM) est une interface de programmation pour les documents web. Il représente la structure d'un document sous forme d'arbre d'objets, où chaque objet correspond à une partie du document, telle que des éléments, des attributs et du texte. JavaScript peut manipuler cette structure arborescente, permettant aux développeurs de modifier dynamiquement le contenu et l'apparence d'une page web.

### Comment accéder aux éléments du DOM

Pour manipuler le DOM, nous devons accéder à ses éléments. Cela se fait couramment en utilisant l'objet `document`, qui représente l'ensemble du document HTML. Examinons un exemple simple :

```javascript
// Accéder à un élément par son ID
const headerElement = document.getElementById('header');

// Accéder aux éléments par nom de classe
const paragraphs = document.getElementsByClassName('paragraph');

// Accéder aux éléments par nom de balise
const images = document.getElementsByTagName('img');

```

Dans l'extrait de code ci-dessus, nous utilisons `getElementById`, `getElementsByClassName` et `getElementsByTagName` pour récupérer des éléments spécifiques. Les valeurs retournées peuvent ensuite être stockées dans des variables pour une manipulation ultérieure.

### Comment modifier le contenu d'un élément

Une fois que nous avons accès à un élément, nous pouvons modifier son contenu en utilisant la propriété `innerHTML` :

```javascript
// Modifier le contenu d'un élément
headerElement.innerHTML = 'Nouveau Texte d'En-tête';

```

Dans l'exemple ci-dessus, nous avons changé le contenu de `headerElement` en `Nouveau Texte d'En-tête`. C'est une méthode simple mais puissante pour mettre à jour le texte à l'intérieur d'un élément.

## Événements et Gestion des Événements

Les événements sont des actions ou des occurrences qui se produisent dans le navigateur, comme un utilisateur cliquant sur un bouton ou redimensionnant la fenêtre. JavaScript nous permet de gérer ces événements et d'exécuter du code en réponse. La gestion des événements est un aspect crucial de la création de pages web interactives.

### Comment ajouter des écouteurs d'événements

Pour répondre aux événements, nous pouvons utiliser des écouteurs d'événements. Ce sont des fonctions qui "écoutent" un événement spécifique sur un élément particulier. Prenons l'exemple d'un événement de clic sur un bouton :

```javascript
// Accéder à un élément bouton
const myButton = document.getElementById('myButton');

// Ajouter un écouteur d'événement de clic
myButton.addEventListener('click', function() {
    alert('Bouton Cliqué !');
});

```

Dans cet exemple, lorsque le bouton avec l'ID `myButton` est cliqué, une alerte disant `Bouton Cliqué !` apparaîtra. Les écouteurs d'événements fournissent un moyen d'exécuter du code personnalisé basé sur les interactions de l'utilisateur.

## Comment Manipuler les Styles

La manipulation du DOM s'étend également à la modification des styles des éléments, nous permettant de créer des pages web visuellement attrayantes et dynamiques.

### Comment changer les styles dynamiquement

Nous pouvons utiliser la propriété `style` d'un élément pour changer son apparence. Prenons un exemple de changement de couleur d'un paragraphe lorsqu'un bouton est cliqué :

```javascript
// Accéder à un élément paragraphe
const myParagraph = document.getElementById('myParagraph');

// Accéder à un élément bouton
const colorButton = document.getElementById('colorButton');

// Ajouter un écouteur d'événement de clic au bouton
colorButton.addEventListener('click', function() {
    // Changer la couleur du style du paragraphe
    myParagraph.style.color = 'blue';
});

```

Dans cet exemple, lorsque le bouton avec l'ID `colorButton` est cliqué, la couleur du texte du paragraphe avec l'ID `myParagraph` est changée en bleu.

## Comment Créer et Modifier des Éléments

En plus de modifier des éléments existants, JavaScript nous permet de créer de nouveaux éléments et de les ajouter au DOM.

### Comment créer de nouveaux éléments

La méthode `createElement` est utilisée pour créer un nouvel élément HTML. Créons un nouvel élément paragraphe et ajoutons-le au corps du document :

```javascript
// Créer un nouvel élément paragraphe
const newParagraph = document.createElement('p');

// Définir le contenu textuel du nouveau paragraphe
newParagraph.textContent = 'Ceci est un nouveau paragraphe.';

// Ajouter le nouveau paragraphe au corps du document
document.body.appendChild(newParagraph);

```

Dans cet exemple, nous créons un nouvel élément `p` (paragraphe), définissons son contenu textuel, puis l'ajoutons au corps du document.

### Comment modifier les attributs

Nous pouvons également modifier les attributs des éléments existants. Prenons l'exemple du changement dynamique de la source d'une image :

```javascript
// Accéder à un élément image
const myImage = document.getElementById('myImage');

// Changer l'attribut source de l'image
myImage.src = 'new-image.jpg';

```

Ici, nous accédons à un élément image avec l'ID `myImage` et changeons son attribut `src` en `new-image.jpg`, mettant ainsi à jour dynamiquement l'image affichée.

### Comment mettre à jour les valeurs de saisie de formulaire

Prenons un scénario où vous souhaitez mettre à jour la valeur d'une saisie de texte en fonction de l'interaction de l'utilisateur :

```javascript
// Accéder à un élément de saisie de texte
const myInput = document.getElementById('myInput');

// Ajouter un écouteur d'événement de saisie
myInput.addEventListener('input', function() {
    // Mettre à jour un paragraphe avec la valeur de saisie
    document.getElementById('inputValue').textContent = myInput.value;
});

```

Dans cet exemple, à mesure que l'utilisateur tape dans la saisie de texte avec l'ID `myInput`, un paragraphe avec l'ID `inputValue` est dynamiquement mis à jour pour refléter la valeur de saisie.

### Comment basculer la visibilité

Vous pouvez basculer la visibilité d'un élément en utilisant la propriété de style `display`. Créons un bouton qui bascule la visibilité d'un paragraphe :

```javascript
// Accéder à un élément bouton
const toggleButton = document.getElementById('toggleButton');

// Accéder à un élément paragraphe
const toggleParagraph = document.getElementById('toggleParagraph');

// Ajouter un écouteur d'événement de clic
toggleButton.addEventListener('click', function() {
    // Basculer la visibilité du paragraphe
    toggleParagraph.style.display = toggleParagraph.style.display === 'none' ? 'block' : 'none';
});

```

Ici, le paragraphe avec l'ID `toggleParagraph` est initialement visible. Cliquer sur le bouton avec l'ID `toggleButton` bascule sa visibilité.

## Pièges Courants dans la Manipulation du DOM

Bien que la manipulation du DOM soit un outil puissant pour créer des pages web dynamiques, les débutants rencontrent souvent des pièges courants qui peuvent conduire à des comportements inattendus ou à des erreurs. Explorons certains de ces pièges et fournissons des conseils sur la manière de les éviter.

### Manipuler le DOM avant qu'il ne soit prêt

Nous pouvons parfois tenter de manipuler le DOM avant qu'il ne soit complètement chargé. Cela peut amener JavaScript à essayer d'accéder à des éléments qui n'ont pas encore été rendus. Pour éviter cela, il est crucial d'attendre que le DOM soit complètement chargé avant d'exécuter du code JavaScript :

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Le code de manipulation du DOM va ici
});

```

En enveloppant votre code de manipulation du DOM à l'intérieur de l'écouteur d'événement `DOMContentLoaded`, vous vous assurez qu'il ne s'exécute que lorsque le DOM est prêt.

### Ne pas vérifier si un élément existe

Lorsque vous tentez d'accéder à un élément en utilisant des méthodes comme `getElementById`, vous pourriez supposer que l'élément existe et procéder à la manipulation. Cependant, si l'élément n'est pas présent sur la page, cela peut conduire à des erreurs.

Vérifiez toujours si un élément existe avant de le manipuler :

```javascript
const myElement = document.getElementById('myElement');

if (myElement) {
    // Manipuler l'élément ici
} else {
    console.error('Élément non trouvé !');
}

```

Cette simple vérification empêche les erreurs lors de la manipulation d'éléments qui peuvent être présents ou non.

### Oublier d'empêcher les actions par défaut

Lors de la gestion des événements, oublier d'empêcher l'action par défaut peut entraîner un comportement de page inattendu. Par exemple, si un formulaire est soumis sans empêcher l'action par défaut, la page pourrait se recharger, entraînant une perte de données :

```javascript
const myForm = document.getElementById('myForm');

myForm.addEventListener('submit', function(event) {
    // Empêcher la soumission par défaut du formulaire
    event.preventDefault();

    // Votre code de gestion de formulaire va ici
});

```

En appelant `event.preventDefault()`, vous arrêtez le comportement par défaut associé à l'événement, vous donnant un contrôle total sur la manière dont l'événement est géré.

### Effectuer des requêtes DOM inefficaces

Effectuer des requêtes DOM inefficaces, surtout dans des boucles, peut dégrader les performances. Chaque requête implique de parcourir le DOM, et des requêtes inutiles peuvent ralentir votre page web.

Au lieu de requêter le DOM de manière répétée, mettez en cache les références aux éléments :

```javascript
// Requête inefficace dans une boucle
for (let i = 0; i < 10; i++) {
    const myElement = document.getElementById('myElement');
    // Manipuler myElement
}

// Requête efficace en dehors de la boucle
const myElement = document.getElementById('myElement');
for (let i = 0; i < 10; i++) {
    // Manipuler myElement
}

```

En requêtant le DOM une fois et en réutilisant la référence, vous optimisez votre code.

### Ne pas gérer la compatibilité multi-navigateurs

Différents navigateurs peuvent interpréter JavaScript et la manipulation du DOM légèrement différemment. Ne pas tenir compte de la compatibilité multi-navigateurs peut conduire à des comportements incohérents.

Utilisez la détection de fonctionnalités et envisagez d'utiliser des bibliothèques comme jQuery ou des frameworks modernes pour gérer les incohérences multi-navigateurs :

```javascript
// Détection de fonctionnalités pour addEventListener
if (document.addEventListener) {
    // Utiliser addEventListener
} else {
    // Revenir à une méthode alternative
}

```

En vérifiant les fonctionnalités avant de les utiliser, vous vous assurez que votre code fonctionne sur divers navigateurs.

## Comment Utiliser des Frameworks pour la Manipulation du DOM

Bien que JavaScript permette une manipulation directe du DOM, le développement web moderne implique souvent l'utilisation de frameworks comme React ou Vue.js. Ces frameworks fournissent une manière plus structurée de construire et de gérer des interfaces utilisateur.

### Exemple avec React

```javascript
// Composant React rendant un bouton et gérant son événement de clic
class MyButton extends React.Component {
    handleClick() {
        alert('Bouton React Cliqué !');
    }

    render() {
        return (
            <button onClick={() => this.handleClick()}>Cliquez-moi</button>
        );
    }
}

// Rendu du composant React dans le DOM
ReactDOM.render(<MyButton />, document.getElementById('reactRoot'));

```

Dans cet exemple React, un composant est créé pour gérer un événement de clic sur un bouton, démontrant une approche plus déclarative du développement d'interface utilisateur.

### Exemple avec Vue.js

```javascript
// Instance Vue.js avec une propriété de données et une méthode
new Vue({
    el: '#vueRoot',
    data: {
        message: 'Message Vue.js'
    },
    methods: {
        showMessage: function () {
            alert(this.message);
        }
    }
});

```

Ici, une instance Vue.js est créée pour gérer les données et les méthodes, montrant la réactivité et la structure basée sur les composants de Vue.js.

## Conclusion

Dans ce guide complet, nous avons exploré le monde de la manipulation du DOM en JavaScript. De l'accès aux éléments à la gestion des événements, en passant par la modification des styles et la création de nouveaux éléments, nous avons couvert les concepts essentiels de manière simple.

Rappelez-vous, la manipulation du DOM est au cœur de la création de pages web dynamiques et interactives. En maîtrisant ces techniques fondamentales, vous serez bien équipé pour construire des applications web engageantes et conviviales. À mesure que vous continuerez votre parcours avec JavaScript, la pratique et l'expérimentation approfondiront votre compréhension de ces concepts, ouvrant la voie à votre succès en tant que développeur web.