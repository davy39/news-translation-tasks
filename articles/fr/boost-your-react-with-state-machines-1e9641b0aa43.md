---
title: Améliorez votre React avec des Machines à États
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T19:39:46.000Z'
originalURL: https://freecodecamp.org/news/boost-your-react-with-state-machines-1e9641b0aa43
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8c333d_YNEHG4q3UDb1wTA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Améliorez votre React avec des Machines à États
seo_desc: 'By Jean-Paul Delimat

  Mixing React and state machines is a great productivity boost for you as a developer.
  It also improves the usually shaky developers/designers collaboration.

  The state machine concept is very simple: a component can be in one stat...'
---

Par Jean-Paul Delimat

Combiner React et les machines à états est un excellent moyen d'augmenter votre productivité en tant que développeur. Cela améliore également la collaboration souvent fragile entre développeurs et designers.

Le concept de machine à états est très simple : un composant peut être dans un seul état à la fois et possède un nombre fini d'états.

En quoi cela est-il utile dans le développement d'interfaces utilisateur, dites-vous ?

### Le problème

Considérons un simple composant d'édition de texte comme celui très mal stylisé ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qH9LyaKS94HYKOfvhR1jGw.png)

Les états possibles d'un tel composant sont (de gauche à droite) :

* Afficher la valeur
* Éditer la valeur
* Sauvegarde en cours
* Erreur de sauvegarde

Une forme directe pour le modèle du composant a 5 propriétés :

```js
state: {
  processing: true, // Sera vrai lorsque la sauvegarde est en cours
  error: null,      // Ne sera pas null lorsqu'une erreur de sauvegarde se produit
  value: null,      // La valeur d'affichage en lecture seule
  edition: false,   // Sommes-nous en mode édition ?
  editValue: null,  // La valeur actuellement éditée mais non sauvegardée
}
```

Les combinaisons appropriées des propriétés nous donneront les 4 états que nous avons identifiés ci-dessus.

Le problème est qu'il y a en réalité 2⁵ = 32 combinaisons possibles pour l'état. Cela signifie qu'il y a 28 mauvaises façons d'utiliser les propriétés d'état.

Une erreur typique sur le composant ci-dessus est de ne pas réinitialiser l'erreur après une sauvegarde réussie. Ainsi, l'utilisateur final sauvegardera, obtiendra un message d'erreur « Something went wrong », corrigera l'erreur, sauvegardera à nouveau et passera en mode affichage. Jusqu'à présent, tout va bien. Sauf lorsque l'on retourne en mode édition… le message d'erreur est toujours là. Histoire vraie. J'ai vu cela fait plusieurs fois par des développeurs inexpérimentés.

Notre composant est aussi simple qu'il soit et pourtant il révèle une triste vérité :

Opérer sur des propriétés d'état brutes signifie que la robustesse du composant repose uniquement sur l'utilisation correcte de la signification des propriétés… pour chaque développeur modifiant le code… tout au long du cycle de vie du projet.

Nous savons tous comment cela se termine !

### La solution

Considérons une approche différente utilisant des « machines à états ». Les états seraient :

```js
state: {
  display: {
    processing: false,
    error: null,
    value: "Awesome",
    edition: false,
    editValue: null,
  },
  saving: {
    processing: true,
    error: null,
    value: "Awesome",
    edition: true, // Garde la vue d'édition active jusqu'à la fin de la sauvegarde
    editValue: "Awesome Edit", 
  },
  edit: {
    processing: false,
    error: null,
    value: "Awesome",
    edition: true,
    editValue: "Awesome Editing",
  },
  save_error: {
    processing: false,
    error: "Value should be at least 4 characters",
    value: "Awesome",
    edition: true, // Garde la boîte d'édition ouverte
    editValue: "Awe",
  }
}
```

Cela est plus verbeux que la première approche, mais cela offre de nombreux avantages :

* On peut voir tous les états du composant simplement en regardant la machine à états. Les états ont des noms logiques et l'utilisation de chaque propriété brute est auto-documentée. Les nouveaux développeurs dans l'équipe se sentiront chez eux immédiatement.
* La convention sur la manière d'étendre le composant est claire : créez un nouvel état et définissez les propriétés brutes de manière appropriée. Personne dans son bon esprit n'oserait utiliser un `setState()` brut lorsqu'il y a une machine à états implémentée dans le composant.
* Enfin, mais non des moindres, le processus de transfert avec l'équipe UI/UX devient aussi fluide que possible. Vous avez besoin d'un design visuel pour chaque état de votre machine, et peut-être quelques animations pour les transitions. C'est tout. Clair et facilement traçable.

Une version minimaliste et fonctionnelle de l'exemple ci-dessus serait :

```js
import React, {Component, PropTypes} from 'react';

export default class InputStateMachine extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
        this.goToState = this.goToState.bind(this);
        this.save = this.save.bind(this);

        this.state = {
            name: 'display',
            machine: this.generateState('display', props.initialValue)
        };
    }

    generateState(stateName, stateParam) {

        const previousState = this.state ? {...this.state.machine} : {};

        switch(stateName) {
            case 'display':
                return {
                    processing: false,
                    error: null,
                    value: stateParam || previousState.value,
                    editing: false,
                    editValue: null,
                };
            case 'saving':
                return {
                    processing: true,
                    error: null, // Réinitialise toute erreur précédente
                    value: previousState.value,
                    editing: true, // Garde la vue d'édition active jusqu'à la fin de la sauvegarde
                    editValue: previousState.editValue,
                };
            case 'edit':
                return {
                    processing: false,
                    error: null,
                    value: previousState.value,
                    editing: true,
                    editValue: stateParam,
                };
            case 'save_error':
                return {
                    processing: false,
                    error: stateParam,
                    value: previousState.value,
                    editing: true, // Garde la boîte d'édition ouverte
                    editValue: previousState.editValue,
                };
            case 'loading': // Même que par défaut
            default:
                return {
                    processing: true,
                    error: null,
                    value: null,
                    editing: false,
                    editValue: null,
                };
        }
    }

    goToState(stateName, stateParam)  {
        this.setState({
            name: stateName,
            machine: this.generateState(stateName, stateParam)
        });
    }

    handleSubmit(e) {
        this.goToState('edit', e.target.value);
    };

    save(valueToSave) {
        this.goToState('saving');

        // Simule la sauvegarde des données ...
        setTimeout(() => this.goToState('display', valueToSave), 2000);
    };

    render() {
        const {processing, error, value, editing, editValue} = this.state.machine;

        if(processing) {
            return <p>Traitement en cours ...</p>
        } else if(editing) {
            return (
                <div>
                    <input type="text" onChange={this.handleSubmit} value={editValue || value} />
                    {error && <p>Erreur : {error}</p>}
                    <button onClick={() => this.save(editValue)}>Sauvegarder</button>
                </div>
            );
        } else {
            return (
                <div>
                    <p>{value}</p>
                    <button onClick={() => this.goToState('edit', value)}>Éditer</button>
                </div>
            );
        }
    }
}
```

L'utilisation est :

```js
<InputStateMachine initialValue="Bonjour" />
```

Il y a un peu de code standard à écrire lors de l'utilisation de machines à états :

* Créez une méthode utilitaire qui définit le nom et le contenu de l'état. Gardez une trace du nom de l'état actuel pour faciliter le débogage.
* Gardez la méthode qui génère votre état pure et utilisez-la pour initialiser votre état dans le constructeur.
* Déstructurez `this.state.machine` au lieu de `this.state` dans votre méthode de rendu.
* L'état peut nécessiter des paramètres qui peuvent être difficiles à gérer. En règle générale, si la génération de votre état nécessite plus de 3 paramètres, votre composant ne doit pas utiliser le modèle de machine à états.

Certaines bibliothèques visent à résoudre ce problème de code standard, mais la surcharge est si faible qu'elle ne mérite pas vraiment une nouvelle dépendance dans votre projet.

### Conclusion

Le modèle de machine à états est un bon moyen d'améliorer la lisibilité de vos composants d'interface utilisateur et le processus de développement, de la conception visuelle à la maintenance.

Attention cependant ! Ne vous lancez pas à fond et n'appliquez pas cela à tous les composants que vous avez ! Votre application doit rester flexible et gérer les complexités émergentes. Le nombre d'états peut rapidement exploser pour les composants de niveau supérieur et les machines à états ne sont d'aucune utilité dans ce cas.

Utilisez cependant le modèle sur votre bibliothèque de composants standard/de base ! C'est la partie de l'application qui vivra le plus longtemps. Finalement, chaque développeur de l'équipe la touchera et bénéficiera des conseils et de la robustesse fournis par la machine à états.

Merci d'avoir lu !