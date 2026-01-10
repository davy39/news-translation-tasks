---
title: Comment résoudre le défi du Parking en JavaScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2022-06-16T14:55:53.000Z'
originalURL: https://freecodecamp.org/news/parking-lot-challenge-solved-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/parking-loot.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment résoudre le défi du Parking en JavaScript
seo_desc: 'Have you heard about the Parking Lot challenge? If not, let me explain
  briefly.

  The Parking Lot is challenge where you are asked to write a class that manages an
  imaginary parking lot.

  In this tutorial we will do that in JavaScript. And to make it a ...'
---

Avez-vous entendu parler du défi du Parking ? Si ce n'est pas le cas, laissez-moi vous expliquer brièvement.

Le Parking est un défi où l'on vous demande d'écrire une classe qui gère un parking imaginaire.

Dans ce tutoriel, nous allons le faire en JavaScript. Et pour le rendre un peu plus intéressant, nous allons créer une petite application React qui visualisera le fonctionnement de notre classe.

Commençons. 🎉

# Exigences du défi

Pour ce défi, vous devez implémenter une classe en JavaScript. Cette classe doit contenir des variables et des méthodes qui simulent le fonctionnement d'un parking. Voici les détails :

* Nous devons pouvoir créer le parking avec une taille donnée (nombre de places de parking)

* Nous ne faisons pas de différence entre les différents véhicules – nous les considérons tous comme identiques

* Notre classe fournit une méthode pour garer de nouvelles voitures dans le parking

* Notre classe fournit une méthode pour retirer les voitures déjà garées, et

* Notre classe fournit une méthode pour obtenir la taille du parking (nombre total de places)

# Solution du défi du Parking

Commençons par examiner la logique de la classe elle-même.

C'est assez simple, donc il n'y aura probablement pas de surprises pour la plupart d'entre vous – surtout si vous avez déjà une certaine expérience en programmation OOP et dans les langages basés sur les classes.

## **class ParkingLot**

Je vais d'abord vous donner le code, puis je le commenterai brièvement.

```javascript
class ParkingLot {
  slots = [];

  constructor(parkingSize) {
    this.slots = new Array(parkingSize).fill(null);
  }

  park(carId) {
    console.log(`Parking car: ${carId}`);
    if (this.slots.every((slot) => slot !== null)) {
      return false;
    }

    for (let i = 0; i <= this.slots.length; i++) {
      const slot = this.slots[i];

      if (slot === null) {
        this.slots[i] = carId;
        return true;
      }
    }
  }

  remove(carId) {
    console.log(`Leaving car: ${carId}`);
    if (this.slots.every((slot) => slot !== carId)) {
      return false;
    }

    for (let i = 0; i <= this.slots.length; i++) {
      const slot = this.slots[i];

      if (slot === carId) {
        this.slots[i] = null;
        return true;
      }
    }
  }

  getSlots() {
    console.log(`Parking slots: ${this.slots}`);
    return this.slots;
  }

  getSize() {
    console.log(`Parking size is: ${this.slots.length}`);
    return this.slots.length;
  }

  getAvailable() {
    const availableSlots = this.slots.filter((s) => s === null).length;
    console.log(`Available parking slots: ${availableSlots}`);
    return availableSlots;
  }

  isFull() {
    return this.getAvailable() === 0;
  }
}

export default ParkingLot;
```

En commençant par le début – notre classe a une propriété, `slots`, qui sera un tableau stockant des informations sur les places de parking (si elles sont libres ou occupées).

Ensuite, nous avons une méthode `constructor` qui est exécutée chaque fois que vous créez une instance de cette classe. C'est ici que nous utilisons un paramètre numérique d'entrée, appelé `parkingSize`, pour créer un tableau vide avec une longueur égale à ce nombre.

Techniquement parlant, ce tableau n'est pas vide, car nous l'initialisons avec des valeurs *null*. Cela signifie qu'après l'exécution du code dans le constructeur, nous obtiendrons un tableau rempli de valeurs null, selon le nombre que nous avons passé.

Par exemple, si nous exécutons ceci :

```javascript
const parking = new ParkingLot(5);
```

Cela donnera ceci :

```javascript
[null, null, null, null, null] // longueur = 5

au lieu de [] // tableau vide, longueur 0
```

Après avoir parcouru le constructeur, examinons le reste des méthodes de la classe.

`park()` – C'est ici que nous garons effectivement une voiture. Cette méthode parcourt le tableau `slots`, vérifie s'il y a des places libres (c'est-à-dire des places encore égales à null), et ajoute la voiture dans ces places vides.

Les voitures sont identifiées par `carId`. Il s'agit simplement d'un identifiant que nous utilisons pour signifier qu'une voiture occupe une certaine place. Notez que cette méthode retourne false s'il n'y a pas de places libres ou true si le stationnement a réussi.

`getSlots()` – Méthode auxiliaire qui retourne simplement le tableau que nous utilisons pour stocker les places de parking.

`remove()` – C'est ainsi que nous retirons les voitures du parking. Cette méthode parcourt également le tableau des places.

💡Comme vous l'avez peut-être remarqué jusqu'à présent, dans presque tous les cas où nous devons manipuler des données stockées dans une structure de données comme un tableau, nous devons parcourir cette structure pour pouvoir accéder à ses éléments.

Différents langages de programmation fournissent différentes structures de données et méthodes pour travailler avec elles, mais l'idée principale est toujours la même : lorsque vous devez faire quelque chose avec ces données, vous devez les parcourir d'une manière ou d'une autre.

Pour retirer une voiture du parking, nous utilisons l'identifiant mentionné précédemment. Nous recherchons de tels éléments dans le tableau des places, et si nous obtenons une correspondance, nous avons une voiture à "dégarer". Nous effectuons le retrait réel en réinitialisant simplement cette place spécifique à *null*.

Maintenant, vous pouvez deviner pourquoi nous avons décidé d'initialiser notre tableau de places avec des nulls en premier lieu.

Cette méthode retourne également un résultat booléen selon qu'il y a eu un retrait réussi ou non.

Nous devrions pouvoir utiliser ce retour d'information lors de la construction d'une sorte d'interface utilisateur capable de réagir à de tels changements. La même chose est valable lors de l'ajout de voitures au parking (voir la méthode `park`).

`getSize()` – Une autre méthode auxiliaire que nous utilisons pour vérifier la taille du parking.

`getAvailable()` – Celle-ci nous montre combien de places disponibles nous avons actuellement.

`isFull()` – Nous indique si le parking est plein, c'est-à-dire qu'il n'y a plus de places disponibles.

# Comment construire l'application React

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-92.png align="left")

*Application Parking - écran principal*

C'est ici que le plaisir commence. 🔮

Nous allons créer une application interactive, visualisant les tâches que nous pouvons effectuer à l'aide de notre implémentation ci-dessus.

Notre application fournira des contrôles d'interface utilisateur de base permettant à un opérateur (imaginaire) de travailler avec le logiciel de parking. Et afin de rendre leur travail un peu plus agréable à l'œil, nous allons essayer d'animer les fonctions de base que notre logiciel fournit.

Voyons comment ! 📺

## Démo

Voici la démo en direct pour ceux d'entre vous qui ne se soucient pas des détails et veulent simplement "goûter" à cela : 🧪

[Contenu intégré](https://parking-lot-chi.vercel.app/)

## Code source

Voici le [dépôt](https://github.com/mihailgaberov/parking-lot) avec le code source de l'application.

Laissez-moi vous donner un bref résumé du *quoi* et du *pourquoi*.

L'application est construite avec [vite](https://vitejs.dev/). La raison en est que j'ai joué avec récemment et que je suis vraiment satisfait de la vitesse et des performances qu'il offre.

Peu importe qu'il soit encore dans les étapes relativement précoces du développement – si je dois commencer un nouveau projet et que je suis en position de choisir, j'opterai pour **vite**.

Ce n'est pas pour dire que j'ai quelque chose contre son grand frère [CRA](https://create-react-app.dev/). Au contraire, j'ai construit plusieurs applications avec et je l'utilise encore dans certains de mes projets. C'est juste que **vite** est beaucoup plus rapide et me donne souvent tout ce dont j'ai actuellement besoin.

💡Gardez simplement à l'esprit que la sélection d'une technologie donnée dépend toujours de vos besoins spécifiques pour un projet spécifique. C'est-à-dire qu'il n'y a pas de solution miracle. C'est toujours une question d'exigences et de priorités.

## Structure de l'application React

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-93.png align="left")

*Structure de l'application*

La structure de l'application est simple. Au niveau racine, nous avons deux dossiers – *assets* et *src*. Le premier contient les ressources utilisées dans l'application (dans ce cas, il s'agit simplement d'une image de voiture). Le second contient tous les fichiers avec le code source.

Examinons de plus près le dossier source.

Ici, nous avons les dossiers suivants :

* [components](https://github.com/mihailgaberov/parking-lot/tree/main/src/components) – contient tous les composants React utilisés dans l'application

* [lib](https://github.com/mihailgaberov/parking-lot/tree/main/src/lib) – contient la classe de parking, responsable de la logique principale de l'application

* [pages](https://github.com/mihailgaberov/parking-lot/tree/main/src/pages) – contient deux sous-répertoires, pour les deux écrans principaux de l'application – Accueil et Principal, respectivement

* [utils](https://github.com/mihailgaberov/parking-lot/tree/main/src/utils) – contient une méthode auxiliaire pour générer des plaques d'immatriculation fictives que nous utilisons plus tard lors de la représentation d'une place de parking comme *occupée*

* Et plusieurs fichiers, la plupart d'entre eux sont liés au point d'entrée de l'application, à l'exception des favicons – leur rôle devrait être clair pour vous. Si ce n'est pas le cas, jetez un œil à l'onglet de votre navigateur 😉

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-94.png align="left")

*Onglet du navigateur avec favicon*

## Pages de l'application

Comme mentionné précédemment, les pages principales (également appelées écrans) de l'application sont appelées [Landing](https://github.com/mihailgaberov/parking-lot/tree/main/src/pages/Landing) et [Main](https://github.com/mihailgaberov/parking-lot/tree/main/src/pages/Main). Ce sont des composants React eux-mêmes. Ils servent de squelettes pour tout ce que vous voyez dans la page d'accueil – où vous arrivez initialement et où vous pouvez sélectionner combien de places de parking vous souhaitez avoir dans votre parking.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-95.png align="left")

*Page d'accueil*

Et la page vers laquelle vous allez après avoir cliqué sur le grand bouton rose de soumission - l'écran principal où votre opérateur peut gérer le parking.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-96.png align="left")

*Page principale*

## **Fonctionnalité de l'application**

L'application fournit une fonctionnalité très basique pour gérer un parking imaginaire. Lorsque l'utilisateur sélectionne le nombre de places qu'il souhaite (max 20), il sera redirigé vers l'écran principal. Là, l'utilisateur pourra voir toutes les places de parking libres.

Lorsque une voiture est garée, via le bouton PARK!, la place concernée sera visualisée comme occupée et affichera le numéro d'immatriculation de la voiture qui y est garée. L'opérateur peut dégager les voitures en cliquant sur une place occupée, c'est-à-dire sur la voiture qu'il souhaite "retirer" du parking.

## 💡La simple animation de la voiture rouge en mouvement est juste pour l'effet visuel et n'a aucune influence réelle sur le fonctionnement du parking.

J'ai utilisé [CSS modules](https://github.com/css-modules/css-modules) pour styliser l'application. J'ai également essayé de rendre l'application un peu adaptée aux mobiles, au cas où vous décideriez de l'essayer sur votre appareil mobile.

Soyez mon invité et [essayez](https://parking-lot-chi.vercel.app/) 🤪

# Conclusion

Mon idée initiale derrière cet article était de décrire la classe de parking elle-même. Vous savez, juste à des fins éducatives. Pour vous montrer comment vous pouvez écrire une telle classe en JavaScript.

Mais ensuite, j'ai pensé que c'était un peu ennuyeux 🥱. Je voulais créer quelque chose de plus amusant 🤗🏽, quelque chose de plus gamifié 🎯🏽 pour ainsi dire.

Et c'est ainsi que j'ai abouti à cette mini-application de type jeu 🎮.

En la construisant, ma fille de 5 ans 🧒🏽 l'a vue et a voulu jouer avec. Et elle s'est vraiment beaucoup amusée !

Oui, oui, bien sûr ! Je ne dis pas que si c'était quelque chose d'amusant pour une enfant de 5 ans, ce le sera pour vous aussi 😀.

Mon seul objectif était d'attirer votre attention à travers le jeu, afin que les connaissances 📖 derrière celui-ci restent plus longtemps avec vous.

Merci d'avoir lu ! 👋