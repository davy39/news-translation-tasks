---
title: Le Modèle Vue Contrôleur - Architecture MVC et Frameworks Expliqués
subtitle: ''
author: Rafael D. Hernandez
co_authors: []
series: null
date: '2021-04-19T14:13:49.000Z'
originalURL: https://freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/BG.png
tags:
- name: design patterns
  slug: design-patterns
- name: programing
  slug: programing
- name: software design
  slug: software-design
- name: software design patterns
  slug: software-design-patterns
seo_title: Le Modèle Vue Contrôleur - Architecture MVC et Frameworks Expliqués
seo_desc: 'The MVC architecture pattern turns complex application development into
  a much more manageable process. It allows several developers to simultaneously work
  on the application.

  When I first learned about MVC patterns, I was intimidated by all the jarg...'
---

Le modèle d'architecture MVC transforme le développement d'applications complexes en un processus beaucoup plus gérable. Il permet à plusieurs développeurs de travailler simultanément sur l'application.

Lorsque j'ai appris pour la première fois les modèles MVC, j'ai été intimidé par tout le jargon. Et encore plus lorsque j'ai commencé à appliquer ces concepts à une application réelle.

En prenant du recul pour se concentrer sur ce qu'est le MVC et ce qu'il peut accomplir, il est beaucoup plus facile de comprendre et d'appliquer le modèle à toute application web.

## Qu'est-ce que le MVC ?

MVC signifie modèle-vue-contrôleur. Voici ce que signifie chacun de ces composants :

* **Modèle** : Le backend qui contient toute la logique des données
* **Vue** : Le frontend ou l'interface graphique utilisateur (GUI)
* **Contrôleur** : Le cerveau de l'application qui contrôle la manière dont les données sont affichées

![Image](https://www.freecodecamp.org/news/content/images/2021/04/MVC3.png)

Le concept des MVC a été introduit pour la première fois par Trygve Reenskaug, qui l'a proposé comme un moyen de développer des interfaces graphiques d'applications de bureau.

Aujourd'hui, le modèle MVC est utilisé pour les applications web modernes car il permet à l'application d'être scalable, maintenable et facile à étendre.

## Pourquoi devriez-vous utiliser le MVC ?

Trois mots : **séparation des préoccupations**, ou SoC en abrégé.

Le modèle MVC vous aide à diviser le code frontend et backend en composants séparés. Ainsi, il est beaucoup plus facile de gérer et d'apporter des modifications à l'un ou l'autre côté sans qu'ils n'interfèrent l'un avec l'autre.

Mais cela est plus facile à dire qu'à faire, surtout lorsque plusieurs développeurs doivent mettre à jour, modifier ou déboguer une application complète simultanément.

## Comment utiliser le MVC

Pour mieux illustrer le modèle MVC, j'ai inclus une application web qui montre comment ces concepts fonctionnent tous.

Mon application Car Clicker est une variation d'une application bien connue appelée Cat Clicker.

Voici quelques-unes des principales différences dans mon application :

1. Pas de chats, **uniquement** des images de voitures de muscle (désolé les amoureux des chats !)
2. Plusieurs modèles de voitures sont listés
3. Il y a plusieurs compteurs de clics
4. Elle n'affiche que la voiture sélectionnée

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screen-Recording-2021-04-11-at-11.31.27.07-PM.gif)

Maintenant, plongeons dans ces trois composants qui constituent le modèle d'architecture MVC.

### Modèle (données)

Le travail du modèle est simplement de gérer les données. Que les données proviennent d'une base de données, d'une API ou d'un objet JSON, le modèle est responsable de leur gestion.

Dans l'application Car Clicker, l'objet modèle contient un tableau d'objets de voitures avec toutes les informations (données) nécessaires pour l'application.

Il gère également la voiture actuelle affichée avec une variable initialement définie sur `null`.

```javascript
const model = {
    currentCar: null,
    cars: [
        {
            clickCount: 0,
            name: 'Coupe Maserati',
            imgSrc: 'img/black-convertible-coupe.jpg',
        },
        {
            clickCount: 0,
            name: 'Camaro SS 1LE',
            imgSrc: 'img/chevrolet-camaro.jpg',
        },
        {
            clickCount: 0,
            name: 'Dodger Charger 1970',
            imgSrc: 'img/dodge-charger.jpg',
        },
        {
            clickCount: 0,
            name: 'Ford Mustang 1966',
            imgSrc: 'img/ford-mustang.jpg',
        },
        {
            clickCount: 0,
            name: '190 SL Roadster 1962',
            imgSrc: 'img/mercedes-benz.jpg',
        },
    ],
};
```

### Vues (UI)

Le travail de la vue est de décider ce que l'utilisateur verra sur son écran, et comment.

L'application Car Clicker a deux vues : `carListView` et `CarView`.

Les deux vues ont deux fonctions critiques qui définissent ce que chaque vue veut initialiser et rendre.

Ces fonctions sont l'endroit où l'application décide ce que l'utilisateur verra et comment.

#### carListView

```js
const carListView = {
    init() {
        // stocke l'élément DOM pour un accès facile plus tard
        this.carListElem = document.getElementById('car-list');

        // rend cette vue (met à jour les éléments DOM avec les bonnes valeurs)
        this.render();
    },

    render() {
        let car;
        let elem;
        let i;
        // obtient les voitures à rendre à partir du contrôleur
        const cars = controller.getCars();

        // pour s'assurer que la liste est vide avant le rendu
        this.carListElem.innerHTML = '';

        // boucle sur le tableau des voitures
        for(let i = 0; i < cars.length; i++) {
            // c'est la voiture sur laquelle nous bouclons actuellement
            car = cars[i];

            // crée un nouvel élément de liste de voitures et définit son texte
            elem = document.createElement('li');
            elem.className = 'list-group-item d-flex justify-content-between lh-condensed';
            elem.style.cursor = 'pointer';
            elem.textContent = car.name;
            elem.addEventListener(
                'click',
                (function(carCopy) {
                    return function() {
                        controller.setCurrentCar(carCopy);
                        carView.render();
                    };
                })(car)
            );
            // enfin, ajoute l'élément à la liste
            this.carListElem.appendChild(elem);
        }
    },
};
```

#### CarView

```js
const carView = {
    init() {
        // stocke les pointeurs vers les éléments DOM pour un accès facile plus tard
        this.carElem = document.getElementById('car');
        this.carNameElem = document.getElementById('car-name');
        this.carImageElem = document.getElementById('car-img');
        this.countElem = document.getElementById('car-count');
        this.elCount = document.getElementById('elCount');


        // au clic, incrémente le compteur de la voiture actuelle
        this.carImageElem.addEventListener('click', this.handleClick);

        // rend cette vue (met à jour les éléments DOM avec les bonnes valeurs)
        this.render();
    },

    handleClick() {
    	return controller.incrementCounter();
    },

    render() {
        // met à jour les éléments DOM avec les valeurs de la voiture actuelle
        const currentCar = controller.getCurrentCar();
        this.countElem.textContent = currentCar.clickCount;
        this.carNameElem.textContent = currentCar.name;
        this.carImageElem.src = currentCar.imgSrc;
        this.carImageElem.style.cursor = 'pointer';
    },
};
```

### Contrôleur (Cerveau)

La responsabilité du contrôleur est de récupérer, modifier et fournir des données à l'utilisateur. Essentiellement, le contrôleur est le lien entre la vue et le modèle.

À travers des fonctions getter et setter, le contrôleur récupère les données du modèle et initialise les vues.

S'il y a des mises à jour des vues, il modifie les données avec une fonction setter.

```js
const controller = {
    init() {
        // définit la voiture actuelle sur la première de la liste
        model.currentCar = model.cars[0];

        // dit aux vues de s'initialiser
        carListView.init();
        carView.init();
    },

    getCurrentCar() {
    	return model.currentCar;
    },

    getCars() {
    	return model.cars;
    },

    // définit la voiture actuellement sélectionnée sur l'objet qui est passé
    setCurrentCar(car) {
    	model.currentCar = car;
    },

    // incrémente le compteur pour la voiture actuellement sélectionnée
    incrementCounter() {
        model.currentCar.clickCount++;
        carView.render();
    },
};

// C'est parti !
controller.init();
```

## Frameworks MVC

JavaScript a gagné en popularité et a pris le contrôle du backend ces dernières années. De plus en plus d'applications JavaScript complètes ont opté pour le modèle d'architecture MVC d'une manière ou d'une autre.

Les frameworks viennent et partent, mais ce qui a été constant ce sont les concepts empruntés au modèle d'architecture MVC.

Certains des premiers frameworks qui ont appliqué ces concepts étaient **KnockoutJS**, **Django** et **Ruby on Rails**.

## Conclusion

Le concept le plus attrayant du modèle MVC est la séparation des préoccupations.

Les applications web modernes sont très complexes, et apporter un changement peut parfois être un vrai casse-tête.

Gérer le frontend et le backend en composants plus petits et séparés permet à l'application d'être scalable, maintenable et facile à étendre.

_**Si vous souhaitez jeter un coup d'œil à l'application Car Clicker, le code est disponible sur [GitHub](https://github.com/RafaelDavisH/car-clicker/blob/main/README.md) ou consultez la version live [ici](https://rafaeldavish.github.io/car-clicker/).**_ 

🌟Merci d'avoir lu jusqu'ici !🌟