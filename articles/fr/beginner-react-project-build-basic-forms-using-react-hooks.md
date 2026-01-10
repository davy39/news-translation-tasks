---
title: Projet React pour débutants - Comment créer des formulaires de base en utilisant
  les React Hooks
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-08-17T16:39:03.000Z'
originalURL: https://freecodecamp.org/news/beginner-react-project-build-basic-forms-using-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Basic-Forms-App.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Projet React pour débutants - Comment créer des formulaires de base en
  utilisant les React Hooks
seo_desc: "What we're building\nIn this beginner React Project, we're going to learn\
  \ how to build basic forms using React hooks. We'll learn how to manage form state,\
  \ handle validation, and work with submit handlers. \nCheck it out:\n\nTry it yourself\n\
  If you want t..."
---

## Ce que nous construisons

Dans ce projet React pour débutants, nous allons apprendre à créer des formulaires de base en utilisant les React hooks. Nous apprendrons à gérer l'état du formulaire, à gérer la validation et à travailler avec les gestionnaires de soumission. 

Jetez un coup d'œil :

![](https://jschris.com/0988e0e5975472dc7fe616d48f906494/project.gif)

## Essayez par vous-même

Si vous voulez essayer par vous-même d'abord, voici les scénarios (vous pouvez également récupérer le CSS/code de départ ci-dessous) :

- L'utilisateur doit pouvoir entrer des valeurs dans le formulaire
- Lorsque l'utilisateur clique sur soumettre, si des champs sont vides, un message d'erreur doit apparaître en rouge
- Si le formulaire est soumis et est valide, un message de succès doit apparaître

## Tutoriel vidéo

[Regardez le tutoriel vidéo sur YouTube ici.](https://youtu.be/8hU0I8rY4u4)

## Code de départ

[Téléchargez-le sur GitHub ici.](https://github.com/chrisblakely01/basic-react-forms)

## C'est parti ! Ajout de l'état

Nous allons commencer par ajouter un objet d'état pour contenir notre formulaire. Nous allons prendre une nouvelle ligne en haut de notre fonction `App` dans **App.js** et ajouter ce qui suit :

```jsx
const [values, setValues] = useState({
	firstName: '',
	lastName: '',
	email: '',
});
```

Nous avons trois champs dans le formulaire dont nous devons connaître l'état.

Maintenant, l'état initial va être un objet. Et cet objet va avoir trois valeurs, une pour chacun de ces champs. Nous allons donc les appeler de manière similaire à ce qu'ils sont appelés dans le formulaire.

Le `firstName` va être défini comme vide initialement, de même pour `lastName` et `email`. 

Et maintenant, vous remarquerez une erreur qui dit "useState n'est pas défini", vous devez donc l'importer depuis React ici. Faites-le en haut du fichier dans les imports :

```
import React, { useState } from "react";
```

D'accord, maintenant il nous dit que ces variables ne sont pas encore utilisées. Ce n'est pas grave car nous n'avons pas encore appliqué ces valeurs au formulaire. Mais tout ce que nous avons fait jusqu'à présent, c'est que nous avons créé un objet d'état, et cet objet d'état contient `firstName`, `lastName` et `email`. 

Maintenant que nous avons des valeurs dans l'état, il est logique de les appliquer à nos champs de saisie. Ajoutez une propriété `value` à chacun de vos champs de saisie comme suit :

```jsx

<input
    id="first-name"
    class="form-field"
    type="text"
    placeholder="Prénom"
    name="firstName"
    value={values.firstName}
/>

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Nom"
    name="lastName"
    value={values.lastName}
/>

<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
/>

```

Tout ce que nous avons fait ici, c'est dire : "D'accord, pour cette saisie, la valeur va être celle qui est dans l'état." Enregistrons cela et voyons ce qui se passe dans nos formulaires, pour nous assurer que tout fonctionne toujours.

Et ce n'est pas le cas. Oh non !

Si vous sélectionnez une saisie et commencez à taper vigoureusement sur le clavier, rien n'apparaît à l'écran. Que se passe-t-il ici ?

## Mise à jour des états de saisie

Eh bien, nous avons dit que la valeur de cette saisie va être celle qui est dans l'état. 

Par exemple, `firstName` est actuellement défini comme vide car c'est ce que nous avons défini, mais nous n'avons pas dit à la saisie : "D'accord. Chaque fois que je tape ou que la saisie change, je veux que vous alliez mettre à jour l'état avec les nouvelles valeurs."

Chaque fois que nous faisons des choses comme cela, cela donne effectivement le contrôle à React. Nous devons donc dire à React de mettre également à jour les valeurs. 

Cela signifie que nous devons mettre à jour les valeurs d'état chaque fois que nous tapons dans ces champs. 

D'accord. La manière la plus simple de faire cela est de créer un **gestionnaire** pour chacun de ces champs de saisie, qui met à jour l'état chaque fois qu'un événement de changement se produit. 

Allez-y et ajoutez ce qui suit juste en dessous des objets d'état :

```jsx
const handleFirstNameInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		firstName: event.target.value,
	}));
};
```

Cela prend l'événement que nous obtenons de `onChange`. Nous mettons essentiellement à jour cet objet puis le sauvegardons dans l'état.

Nous allons copier les anciennes valeurs en utilisant les trois points, également connus sous le nom d'opérateur de propagation. Ensuite, nous taperons simplement values et ajouterons une virgule. 

Ensuite, nous dirons que **firstName va être égal à event.target.value**. Nous voulons ajouter cela à notre saisie. Donc dans notre JSX dans la **saisie pour le prénom**, nous prendrons une nouvelle ligne quelque part (n'importe où, cela n'a pas vraiment d'importance), et ajouterons la propriété `onChange` comme suit :

```jsx
<input 
    id='first-name' 
    class='form-field' 
    type='text' 
    placeholder='Prénom' 
    name='firstName' 
    value={values.firstName} 
    onChange={handleFirstNameInputChange} />
```

Maintenant, si nous allons dans notre navigateur et commençons à taper, vous pouvez voir que les choses fonctionnent. Les autres ne fonctionnent pas car nous n'avons pas encore ajouté de gestionnaires pour ceux-ci. Nous allons y jeter un coup d'œil dans une minute.

Pour résumer ce qui se passe : chaque fois que nous tapons dans cette boîte, l'**événement onChange** se produit à chaque frappe. Cela est appelé à chaque fois. 

L'événement est passé par React, et nous voulons mettre à jour notre objet d'état. Pour ce faire, nous appelons la fonction `setValues` et passons un nouvel objet avec les valeurs mises à jour.

Maintenant, nous voulons simplement faire de même pour `lastName` et `email`. Ajoutez un autre gestionnaire pour chacun :

```jsx
const handleLastNameInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		lastName: event.target.value,
	}));
};

const handleEmailInputChange = (event) => {
	event.persist();
	setValues((values) => ({
		...values,
		email: event.target.value,
	}));
};
```

Et n'oubliez pas d'ajouter les propriétés `onChange` aux champs de saisie pour chacun :

```jsx

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Nom"
    name="lastName"
    value={values.lastName}
    onChange={handleLastNameInputChange}
/>
<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
    onChange={handleEmailInputChange}
/>

```

D'accord. C'est le moment de vérité. Tout fonctionne-t-il ou avons-nous cassé quelque chose en cours de route ? Essayons et voyons. Remplissez quelques données et les champs de saisie devraient fonctionner maintenant. Hourra !

Même si nos champs de saisie fonctionnent, nous avons toujours un problème étrange où si nous tapons des choses dans le formulaire et essayons de le soumettre, il ne va rien faire. Il va simplement rafraîchir la page et toutes nos données de formulaire sont perdues. 

Faisons quelque chose à ce sujet.

## Affichage d'un message de succès

Après avoir cliqué sur s'inscrire, il devrait afficher un message de succès si le formulaire est valide. Ce que nous voulons faire, c'est aller dans notre JSX, et juste en dessous du formulaire ajouter une nouvelle div. Encore une fois, j'ai ajouté les classes pour vous pour un message de succès :

```jsx
<div class='success-message'>Succès ! Merci de vous être inscrit</div>
```

Maintenant, bien sûr, cela ne va nulle part. Il va simplement faire semblant que nous avons appelé un serveur ou un point de terminaison quelque part. Et il est revenu avec un message de succès, donc nous allons simplement afficher cela à un utilisateur. 

Mais actuellement, il apparaît tout le temps. Ce que nous voulions, c'est ne l'afficher que si l'utilisateur a soumis le formulaire avec succès. 

Nous allons donc ajouter un autre objet d'état comme suit :

```jsx
const [submitted, setSubmitted] = useState(false);
```

Nous allons garder cela séparé des valeurs car c'est une partie différente du formulaire. Nous ne voulons pas tout mélanger ici et causer un rendu complet. Cela va nous dire si le formulaire a été soumis ou non.

Il va être défini comme `false` initialement car la première fois qu'un utilisateur arrive sur la page, il ne va pas être soumis. 

Et maintenant, nous voulons simplement faire quelques choses intelligentes dans le JSX pour dire : "Si soumis est vrai, alors nous voulons afficher le message de succès." 

Mettez à jour la ligne que nous venons d'ajouter avec ce qui suit :

```jsx
{showSuccess && <div class='success-message'>Succès ! Merci de vous être inscrit</div>}
```

Nous allons envelopper notre **message de succès** dans un opérateur ternaire. C'est essentiellement une instruction if raccourcie qui nous permet de rendre les choses dynamiquement sur la page.

Le message de succès n'apparaîtra maintenant que si `showSuccess` est vrai. Comme vous pouvez le voir maintenant dans le navigateur, cela a disparu. 

Si nous remontons à notre objet d'état pour `submitted` et changeons cela en `true`, il devrait réapparaître. Et c'est le cas.

Nous allons changer cela en false. Ensuite, nous allons rafraîchir notre Chrome et voir ce qui se passe maintenant. 

Nous n'avons pas dit au bouton d'inscription ou au formulaire ce qui se passe lors de la soumission, donc il va toujours rafraîchir la page. Maintenant, nous avons simplement besoin d'un nouveau gestionnaire pour gérer le clic sur le bouton d'inscription. 

Si nous sautons dans nos gestionnaires d'événements et ajoutons ce qui suit :

```jsx
const handleSubmit = (e) => {
	e.preventDefault();
	setSubmitted(true);
};
```

`event.preventDefault` va empêcher le rafraîchissement que nous avons vu.

Nous allons ajouter plus de logique ici dans une minute autour de la validation et autres. Mais pour l'instant, nous allons simplement dire "setSubmitted" pour être vrai. 

Ensuite, nous devons dire au formulaire d'appeler cette fonction lorsqu'il est soumis. Mettez à jour le JSX pour inclure une propriété `onSubmit` dans la balise de formulaire comme suit :

```jsx
<form class='register-form' onSubmit={handleSubmit}>
	//... autre code
</form>
```

Maintenant, si nous exécutons le code dans le navigateur, cliquons sur le bouton d'inscription, le message apparaît. Hourra !

## Ajout de validation et affichage de messages d'erreur

Notre formulaire a l'air bien jusqu'à présent, mais il nous manque un composant clé de tout formulaire, et c'est la validation. Si nous regardons notre exemple de travail, si je soumets cela avec des champs vides, une erreur apparaît qui dit : "Veuillez entrer vos détails."

En dessous de chaque saisie, nous allons ajouter une balise `<span>` qui contiendra le message d'erreur. Votre JSX devrait ressembler à ceci :

```jsx

<input
    id="first-name"
    class="form-field"
    type="text"
    disabled={showSuccess}
    placeholder="Prénom"
    name="firstName"
    value={values.firstName}
    onChange={handleInputChange}
/>
<span id="first-name-error">Veuillez entrer un prénom</span>

<input
    id="last-name"
    class="form-field"
    type="text"
    placeholder="Nom"
    name="lastName"
    value={values.lastName}
    onChange={handleInputChange}
/>
<span id="last-name-error">Veuillez entrer un nom</span>

<input
    id="email"
    class="form-field"
    type="text"
    placeholder="Email"
    name="email"
    value={values.email}
    onChange={handleInputChange}
/>
<span id="email-error">Veuillez entrer une adresse email</span>

```

Vous pouvez voir que ces erreurs apparaissent toujours, car nous n'avons pas de logique conditionnelle qui dit "ne pas apparaître."

Maintenant, nous voulons que ces messages d'erreur n'apparaissent que si le bouton d'inscription a été cliqué. 

Nous allons revenir dans le code. Nous voulons ajouter une logique conditionnelle dans et autour des messages d'erreur, afin qu'ils n'apparaissent que si le bouton a été cliqué et que le champ est vide :

```jsx
{submitted && !values.firstName && <span id='first-name-error'>Veuillez entrer un prénom</span>}
```

Ce que nous faisons ici, c'est vérifier si le formulaire est soumis, et si l'objet d'état `firstName` est vide. Si c'est le cas, nous voulons afficher le message d'erreur. Encore une fois, nous utilisons simplement un opérateur ternaire, rien de compliqué !

Faites de même pour les autres erreurs :

```jsx
{submitted && !values.lastName && <span id='last-name-error'>Veuillez entrer un nom</span>}

//...autre code

{submitted && !values.email && <span id='email-error'>Veuillez entrer une adresse email</span>}
```

Si nous laissons le formulaire vide et cliquons sur s'inscrire, des erreurs apparaissent. Si nous commençons à taper des choses, nous pouvons voir que l'erreur disparaît. Et si nous supprimons ce que nous avons tapé, l'erreur réapparaît.

Essayons de soumettre quelques choses. D'accord, cela semble fonctionner. 

La dernière chose que nous voulons faire est de nous assurer que ce message de succès n'apparaît que si le formulaire est valide. Allez-y et ajoutez une nouvelle valeur d'état :

```jsx
const [valid, setValid] = useState(false);
```

Cela est utilisé pour nous dire si notre formulaire est valide - rappelez-vous, l'utilisation d'objets d'état est un bon moyen de contenir l'"état" des différentes parties de votre application (qui l'aurait deviné ?). 

Les messages de succès ne doivent apparaître que si soumis est vrai et suivi est également vrai. Puisque nous avons défini valide comme faux initialement, il ne s'affichera pas.

Dans notre fonction `handleSubmit`, nous voulons dire que la valeur est vraie si un formulaire est valide. Nous pouvons faire cela en vérifiant chacune de nos valeurs d'état pour les champs de formulaire, en nous assurant qu'elles sont une valeur vraie. 

Ajoutez ce qui suit :

```jsx

const handleSubmit = (event) => {
event.preventDefault();
if(values.firstName && values.lastName && values.email) {
    setValid(true);
}
setSubmitted(true);
}

```

Si l'un de ces champs est faux, alors `valid` restera faux. Cela signifie que la div du message de succès ne sera pas affichée. Voyons cela fonctionner. Si nous cliquons sur s'inscrire sans les champs, nos messages d'erreur s'affichent. Tapons quelques choses valides, cliquons sur s'inscrire, et le message apparaît ! 

## Vous voulez plus d'idées de projets ?

Pourquoi ne pas essayer de construire quelques projets React pour booster votre apprentissage encore plus loin ? J'envoie des emails toutes les quelques semaines (environ) avec des idées de projets, du code de départ et des conseils. [Abonnez-vous pour recevoir cela directement dans votre boîte de réception !](https://subscribe.jschris.com)