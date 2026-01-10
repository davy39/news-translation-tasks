---
title: Comment créer des formulaires dans React
subtitle: ''
author: Boateng Dickson
co_authors: []
series: null
date: '2023-03-10T17:43:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-forms-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-rodnae-productions-7821577.jpg
tags:
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: Comment créer des formulaires dans React
seo_desc: "Forms play an essential role in modern web applications. They enable users\
  \ to share information, complete tasks and provide feedback. \nWithout forms, many\
  \ of the tasks that we take for granted on the web, such as logging in, signing\
  \ up, or making pur..."
---

Les formulaires jouent un rôle essentiel dans les applications web modernes. Ils permettent aux utilisateurs de partager des informations, de compléter des tâches et de fournir des commentaires. 

Sans les formulaires, de nombreuses tâches que nous considérons comme acquises sur le web, telles que la connexion, l'inscription ou les achats, ne seraient pas possibles.

Ainsi, apprendre à créer des formulaires efficaces et conviviaux est essentiel pour les développeurs souhaitant construire des applications web engageantes et interactives.

Avec sa vaste collection de hooks intégrés, React offre plusieurs fonctionnalités et techniques pour créer et gérer des formulaires, y compris la gestion d'état, la gestion des événements et la validation des formulaires.

Le but de ce guide est de fournir un aperçu complet et approfondi de la création de formulaires dans React. 

## Installation

Dans React, il existe deux façons de gérer les données de formulaire :

* **Composants contrôlés** : Dans cette approche, les données du formulaire sont gérées par React à l'aide de hooks tels que le hook `useState`.
* **Composants non contrôlés** : Les données du formulaire sont gérées par le Document Object Model (DOM) plutôt que par React. Le DOM maintient l'état des données du formulaire et les met à jour en fonction des entrées de l'utilisateur.

Pour mieux comprendre la différence entre les composants contrôlés et non contrôlés, considérons qu'il existe deux façons de faire du vélo.

Dans la première approche, vous laissez le vélo prendre le contrôle. Vous vous asseyez sur le vélo et le laissez décider de la direction et de la vitesse. Vous pouvez essayer de le faire aller dans une certaine direction en penchant votre corps, mais finalement, c'est le vélo qui décide où aller.

Cela ressemble aux composants non contrôlés dans React. Vous placez un élément de formulaire dans le composant, et le DOM en prend le contrôle. Le DOM décide de l'état de l'élément d'entrée et le met à jour en fonction des entrées de l'utilisateur.

Dans la deuxième approche, vous prenez le contrôle du vélo. Vous tenez le guidon et pédalez, et vous décidez où aller et à quelle vitesse rouler. Vous pouvez facilement ralentir ou accélérer selon les besoins.

Cela ressemble aux composants contrôlés où un composant React prend le contrôle des données du formulaire et maintient l'état des éléments du formulaire. Le composant décide quand et comment mettre à jour l'état, et il se ré-affiche en fonction des changements d'état.

Dans les sections à venir, nous approfondirons la distinction entre les composants contrôlés et non contrôlés et fournirons des exemples pratiques pour illustrer le fonctionnement de chacun.

## Composants contrôlés dans React

Dans React, un composant contrôlé est un composant où les éléments de formulaire tirent leur valeur d'un état React.

Lorsque un composant est contrôlé, la valeur des éléments de formulaire est stockée dans un état, et toute modification apportée à la valeur est immédiatement reflétée dans l'état.

Pour créer un composant contrôlé, vous devez utiliser la propriété `value` pour définir la valeur des éléments de formulaire et l'événement `onChange` pour gérer les modifications apportées à la valeur.

La propriété `value` définit la valeur initiale d'un élément de formulaire, tandis que l'événement `onChange` est déclenché chaque fois que la valeur d'un élément de formulaire change. À l'intérieur de l'événement `onChange`, vous devez mettre à jour l'état avec la nouvelle valeur en utilisant une fonction de mise à jour de l'état.

Voici un exemple :

```javascript
import {useState} from 'react';
 
export default function  ControlledComponent()  {
	const  [inputValue, setInputValue] =  useState('');

	const  handleChange = (event) => {
		setInputValue(event.target.value);
	};

return  (
<form>
	<label>Valeur de l'entrée :
	<input  type="text"  value={inputValue} onChange={handleChange} />
	</label>
	<p>Valeur de l'entrée : {inputValue}</p>
</div>
)};

```

Dans cet exemple :

Le hook `useState` définit une variable d'état (inputValue) et une fonction de mise à jour de l'état (setInputValue).

La propriété `value` définit la valeur initiale de l'élément d'entrée à la valeur de `inputValue`.

De plus, l'événement `onChange` gère les modifications apportées à la valeur d'entrée. La fonction `handleChange` met à jour l'état `inputValue` avec la nouvelle valeur de l'élément d'entrée, et la valeur mise à jour est immédiatement reflétée dans l'état et affichée à l'écran.

<img src="https://i.imgur.com/N77Ohpv.gif" style="border: 1px solid #333; border-radius: 5px"/>

Lorsque l'utilisateur tape dans le champ de saisie, la fonction `handleChange` met à jour la variable d'état en utilisant la fonction "setInputValue". Le composant est ensuite ré-affiché, et l'attribut `value` du champ de saisie est mis à jour pour refléter la nouvelle valeur de `inputValue`.

La valeur du champ de saisie et le texte affiché en dessous sont toujours synchronisés, ce qui en fait un composant contrôlé.

### Comment gérer les menus déroulants et les cases à cocher dans les composants contrôlés

Tout comme avec les éléments d'entrée, la valeur d'un menu déroulant peut être définie en utilisant la propriété `value` en conjonction avec le gestionnaire d'événements `onChange` pour mettre à jour l'état du composant.

Par exemple, pour gérer un menu déroulant, vous pouvez définir la valeur initiale du menu déroulant dans l'état du composant, puis mettre à jour l'état lorsque la valeur du menu déroulant change :

```javascript
import { useState } from "react";

export default function Dropdown()  {
	const [selectedOption, setSelectedOption] = useState("option1");

	const  handleDropdownChange = (event) => {
		setSelectedOption(event.target.value);
	};

return  (
	<div>
		<label>
			Sélectionnez une option :
				<select  value={selectedOption} onChange={handleDropdownChange}>
				<option  value="option1">Option 1</option>
				<option  value="option2">Option 2</option>
				<option  value="option3">Option 3</option>
			</select>
		</label>
		<p>Option sélectionnée : {selectedOption}</p>
	</div>
	);
}

```

<img src="https://i.imgur.com/5cjbAeO.gif" style="border: 1px solid #333; border-radius: 5px"/>

De même, vous pouvez gérer les cases à cocher en définissant la propriété `checked` de l'élément d'entrée de la case à cocher en fonction de l'état d'un composant, puis en mettant à jour l'état lorsqu'une case à cocher est cliquée.

Voici un exemple :

```javascript
import { useState } from "react";

function Checkbox() {
  const [isChecked, setIsChecked] = useState(false);

  const handleChange = (event) => {
    setIsChecked(event.target.checked);
  };

  return (
    <form>
      <label htmlFor="color">
        <input type="checkbox" name="color" checked={isChecked} onChange={handleChange}/>
        Bleu
      </label>

      {isChecked && <div>Bleu est sélectionné !</div>}
    </form>
  );
}

export default Checkbox;

```

Dans cet exemple, nous avons défini une variable d'état `isChecked` pour suivre si la case à cocher est cochée ou non. Lorsque la case à cocher est cliquée, la fonction `handleChange` est appelée, et elle met à jour la variable d'état `isChecked` à une nouvelle valeur (vrai ou faux.).

La variable `isChecked` contrôle l'attribut `checked` de la case à cocher et affiche conditionnellement un message indiquant que la case à cocher est sélectionnée.

<img src="https://i.imgur.com/81zMRzO.gif" style="border: 1px solid #333; border-radius: 5px"/>

### Comment gérer plusieurs champs de formulaire

Lors de la création de formulaires dans React, il est courant d'avoir plusieurs éléments de formulaire, tels que des champs de texte, des cases à cocher, des boutons radio, et autres. 

Pour gérer l'état de ces éléments de formulaire, vous pouvez définir les valeurs des champs d'entrée sous forme d'objet en utilisant une seule variable d'état et mettre à jour chaque variable d'état respective en utilisant l'événement `onChange`.

Par exemple, supposons que vous souhaitiez créer un formulaire avec les champs suivants :

* Un champ de texte pour le nom de l'utilisateur
* Un champ d'email pour l'email de l'utilisateur
* Un champ de texte pour le message de l'utilisateur

Voici comment vous pourriez gérer ces champs :

```javascript
import { useState } from "react";

export default function Multiple() {
  const [formData, setFormData] = useState({name: "",email: "",message: ""});

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({ ...prevFormData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Nom : ${formData.name}, Email : ${formData.email}, Message : ${formData.message}`
    );
};

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">Nom :</label>
      <input type="text" id="name" name="name" value={formData.name} onChange={handleChange}/>

      <label htmlFor="email">Email :</label>
      <input type="email" id="email" name="email" value={formData.email} onChange={handleChange}/>

      <label htmlFor="message">Message :</label>
      <textarea id="message" name="message" value={formData.message} onChange={handleChange}/>

      <button type="submit">Soumettre</button>
    </form>
  );
}

```

<img src="https://i.imgur.com/4ln01Wq.gif" style="border: 1px solid #333; border-radius: 5px"/>

Dans l'exemple de code :

Le hook `useState` définit un objet d'état nommé `formData` qui contient trois propriétés : `name`, `email`, et `message`, chacune initialisée à une chaîne vide.

La fonction `handleChange` est appelée chaque fois qu'un utilisateur tape dans l'un des champs du formulaire. Elle extrait le `name` et le `value` du champ de formulaire qui a changé en utilisant l'objet `event.target`, puis met à jour la variable d'état `formData` en utilisant la fonction `setFormData`.

La fonction `setFormData` utilise l'opérateur de propagation (`...`) pour copier l'objet `formData` précédent. Ensuite, elle met à jour la valeur du champ de formulaire modifié en définissant sa propriété de valeur avec la nouvelle valeur.

En utilisant un objet pour gérer les données du formulaire, nous pouvons facilement suivre les valeurs de plusieurs éléments de formulaire. Cela facilite la gestion et la manipulation de l'état de nos données de formulaire, surtout lorsque nous traitons des formulaires complexes avec de nombreux éléments de formulaire.

### Comment valider la saisie du formulaire

La validation des formulaires fait référence au processus de vérification des données saisies par l'utilisateur pour s'assurer qu'elles répondent à des critères ou exigences spécifiques avant d'être soumises à un serveur ou utilisées d'une autre manière.

La validation des formulaires peut prendre diverses formes, selon le type et la complexité des données collectées. Les types courants de validation de formulaire incluent :

* Validation des champs obligatoires : Vérification que les champs obligatoires ne sont pas laissés vides.
* Validation du format : Assurer que les données saisies sont dans le bon format (par exemple, adresses e-mail, numéros de téléphone, etc.).
* Validation de la longueur : Vérification que les données saisies sont dans une certaine plage de longueur.
* Validation du motif : Vérification que les données saisies correspondent à un motif spécifique.

Les méthodes courantes de validation de formulaire incluent l'utilisation d'attributs de validation HTML intégrés tels que `required`, `minlength`, et `maxlength`, ainsi que l'utilisation de React pour effectuer une logique de validation personnalisée.

Par exemple, supposons que nous avons un formulaire avec un champ de saisie qui nécessite un minimum de 5 caractères. Nous pouvons utiliser l'état pour suivre la valeur du champ de saisie et afficher un message d'erreur si la longueur de la valeur est inférieure à 5.

```javascript
import { useState } from 'react';

function MyForm() {
  const [inputValue, setInputValue] = useState('');
  const [inputError, setInputError] = useState(null);

  function handleInputChange(event) {
    const value = event.target.value;
    setInputValue(value);

    if (value.length < 5) {
      setInputError('La saisie doit comporter au moins 5 caractères');
    } else {
      setInputError(null);
    }
  }

  function handleSubmit(event) {
    event.preventDefault();
    if (inputValue.length >= 5) {
      // soumettre le formulaire
    } else {
      setInputError('La saisie doit comporter au moins 5 caractères');
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Fruit :
        <input type="text" value={inputValue} onChange={handleInputChange} />
      </label>
      {inputError && <div style={{ color: 'red' }}>{inputError}</div>}
      <button type="submit">Soumettre</button>
    </form>
  );
} 

```

<img src="https://i.imgur.com/Dfm7dtp.gif" style="border: 1px solid #333; border-radius: 5px"/>

Dans cet exemple, nous avons un formulaire simple qui permet à l'utilisateur de saisir un nom de fruit. Le formulaire a deux états :

* `inputValue` : Représente la valeur actuelle du champ de saisie
* `inputError` : Représente toute erreur qui peut survenir lors de la validation du formulaire.

La fonction `handleInputChange` est appelée chaque fois qu'un utilisateur tape un caractère dans le champ de saisie. Elle met à jour l'état `inputValue` pour refléter la valeur actuelle du champ de saisie, puis vérifie si la valeur comporte au moins 5 caractères.

Si la valeur est inférieure à 5 caractères, elle définit l'état `inputError` avec le message d'erreur approprié. Sinon, elle définit l'état `inputError` à `null` (indiquant qu'il n'y a pas d'erreurs).

## Composants non contrôlés dans React

Les composants non contrôlés dans React font référence aux éléments de formulaire dont l'état n'est pas géré par React. Au lieu de cela, leur état est géré par le DOM du navigateur.

Par exemple, supposons que vous avez un formulaire composé d'un champ de saisie de texte, d'une boîte de sélection et d'une case à cocher. Dans un composant contrôlé, vous créeriez un état pour chaque élément de formulaire et écriviez des gestionnaires d'événements pour mettre à jour l'état chaque fois que l'utilisateur interagit avec l'un des éléments du formulaire.

En revanche, un composant non contrôlé permet au navigateur de gérer l'état des éléments du formulaire. Lorsque l'utilisateur entre du texte dans un champ de saisie de texte ou sélectionne une option dans une boîte de sélection, le navigateur met à jour l'état du DOM pour cet élément automatiquement.

Pour obtenir la valeur d'un élément de formulaire non contrôlé, vous pouvez utiliser une fonctionnalité appelée "ref". Les "refs" fournissent un moyen d'accéder à la valeur actuelle des éléments du DOM. Vous pouvez créer une "ref" en utilisant le hook `useRef`, puis l'attacher à l'élément de formulaire auquel vous souhaitez accéder. Cela vous permet de récupérer la valeur actuelle d'un élément à tout moment, sans avoir besoin de gérer son état dans votre composant React.

Voici un exemple de composant non contrôlé :

```javascript
import { useRef } from "react";

export default function Uncontrolled() {
  const selectRef = useRef(null);
  const checkboxRef = useRef(null);
  const inputRef = useRef(null);

  function handleSubmit(event) {
    event.preventDefault();
    console.log("Valeur de l'entrée :", inputRef.current.value);
    console.log("Valeur de la sélection :", selectRef.current.value);
    console.log("Valeur de la case à cocher :", checkboxRef.current.checked);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        <p>Nom :</p>
        <input ref={inputRef} type="text" />
      </label>
      <label>
        <p>Couleur préférée :</p>
        <select ref={selectRef}>
          <option value="red">Rouge</option>
          <option value="green">Vert</option>
          <option value="blue">Bleu</option>
        </select>
      </label>
      <label>
        Aimez-vous React ?
        <input type="checkbox" ref={checkboxRef} />
      </label>
      <button type="submit">Soumettre</button>
    </form>
  );
}


```

<img src="https://i.imgur.com/4zXvzMm.gif" style="border: 1px solid #333; border-radius: 5px"/>

Dans cet exemple :

Nous avons un formulaire qui contient un champ de saisie de texte, une boîte de sélection et une case à cocher. Au lieu de créer un état pour chaque élément de formulaire et d'écrire des gestionnaires d'événements pour mettre à jour l'état, nous utilisons des composants non contrôlés. Cela signifie que le navigateur est responsable de la gestion de l'état des éléments de formulaire.

Lorsque l'utilisateur interagit avec un élément de formulaire, le navigateur met automatiquement à jour l'état du DOM pour cet élément. Et pour récupérer les valeurs actuelles de chaque élément de formulaire, nous utilisons le hook `useRef`.

Les composants non contrôlés peuvent être utiles dans certaines situations, comme lorsque vous devez intégrer des bibliothèques tierces ou lorsque vous n'avez pas besoin de manipuler les données du formulaire.

Dans l'ensemble, les composants non contrôlés sont une approche plus simple pour travailler avec des formulaires dans React, et ils peuvent rendre votre code plus concis et plus facile à lire. Mais il est important de noter que l'utilisation de `ref` pour accéder aux valeurs des éléments de formulaire peut rendre votre code plus difficile à tester et à maintenir, alors utilisez-les avec discernement.

## Comment utiliser les bibliothèques de composants React

Créer des formulaires dans React peut être écrasant, surtout si vous êtes nouveau dans le framework. Vous devez gérer l'état du formulaire, traiter les entrées de l'utilisateur, valider les données d'entrée et plus encore.

Mais la bonne nouvelle est qu'il existe des bibliothèques tierces disponibles pour faciliter tout cela pour vous.

Ces bibliothèques peuvent aider à simplifier votre processus de création de formulaires. Elles fournissent une large gamme de fonctionnalités, y compris la validation des formulaires, le masquage des entrées, la gestion de la soumission, la gestion des erreurs, et plus encore. Cela rend beaucoup plus facile la création de formulaires à la fois conviviaux et fonctionnels.

Quelques bibliothèques de formulaires populaires incluent :

* Formik
* Redux Form
* React Hook Form
* Yup.

Dans cette section, nous allons nous concentrer sur l'apprentissage de l'utilisation de la bibliothèque **React Hook Form**.

### Comment utiliser React Hook Form

React Hook Form est une bibliothèque légère pour gérer les formulaires dans les applications React. Que vous ayez besoin de créer un simple formulaire de contact ou un formulaire complexe en plusieurs étapes, React Hook Form peut aider à simplifier votre processus de création de formulaires.

#### Installation

Commencer avec React Hook Form est simple et ne nécessite que quelques étapes. Tout d'abord, vous devrez installer la bibliothèque dans votre projet. Vous pouvez le faire en utilisant `npm` en exécutant la commande suivante :

```npm
npm install react-hook-form

```

Alternativement, vous pouvez utiliser yarn pour installer React Hook Form :

```yarn
yarn add react-hook-form

```

Une fois que vous avez installé la bibliothèque, vous devez importer le hook `useForm` du package `react-hook-form` dans votre composant.

```javascript
import  { useForm }  from  "react-hook-form";

```

En important le hook `useForm`, vous pouvez commencer à utiliser React Hook Form pour gérer les formulaires dans votre application.

Le hook `useForm` fournit plusieurs fonctions et propriétés que vous pouvez utiliser pour gérer votre formulaire :

* `register` : Cette fonction est utilisée pour enregistrer les champs de formulaire avec React Hook Form.
* `handleSubmit` : Cela est utilisé pour gérer les soumissions de formulaire. Il prend une fonction de rappel qui est appelée lorsque le formulaire est soumis.
* `errors` : Cela représente un objet contenant toute erreur de validation qui se produit lorsque le formulaire est soumis.
* `watch` : Cette fonction est utilisée pour surveiller les changements de champs de formulaire spécifiques. Elle prend un tableau de noms de champs de formulaire et retourne la valeur actuelle de ces champs.

Ce ne sont que quelques exemples des fonctions et propriétés que le hook useForm fournit. Vous pouvez trouver la liste complète des fonctions et propriétés dans la [documentation](https://www.react-hook-form.com/api/useform/) de React Hook Form.

#### Comment configurer le formulaire

Après avoir importé le hook `useForm`, vous pouvez l'invoquer pour obtenir l'accès aux fonctions et propriétés qu'il fournit :

```jsx
const { register, handleSubmit, formState:{errors} } = useForm();

```

Dans le code ci-dessus, nous utilisons la déstructuration pour extraire les propriétés `register`, `handleSubmit`, et `errors` du hook `useForm`.

#### Comment enregistrer les champs de formulaire

L'étape suivante consiste à enregistrer les champs de formulaire en utilisant la fonction `register`. La fonction `register` prend deux paramètres :

* `name` : Le nom du champ de formulaire.
* `validationOptions` : Un objet optionnel contenant des règles de validation que vous pouvez appliquer à un champ de formulaire.

Voici un exemple d'enregistrement d'un champ de saisie et d'ajout d'une règle de validation indiquant qu'il s'agit d'un champ obligatoire.

```jsx
<input name="firstName" {...register("firstName", { required: true })} />

```

#### Comment gérer la soumission du formulaire

Pour gérer la soumission du formulaire, vous pouvez utiliser la fonction `handleSubmit`.

```jsx
const onSubmit = (data) => console.log(data);

<form onSubmit={handleSubmit(onSubmit)}>
  // champs de formulaire
</form>


```

Dans cet exemple, nous passons la fonction `onSubmit` à la fonction `handleSubmit`. La fonction `onSubmit` sera appelée lorsque le formulaire est soumis et recevra un objet contenant les valeurs de chaque champ de formulaire.

#### Comment afficher les erreurs de validation

Vous pouvez utiliser l'objet `errors` pour afficher toute erreur de validation.

```jsx
<input {...register("firstName", { required: true })} />
{errors.firstName && <p>Ce champ est obligatoire</p>}

```

Dans le code ci-dessus, nous utilisons l'objet `errors` pour afficher un message d'erreur de validation si le champ `firstName` n'est pas rempli. Nous pouvons également afficher des messages d'erreur pour d'autres règles de validation, telles que les longueurs minimale et maximale, les expressions régulières, et plus encore.

#### Comment tout assembler

Avec une compréhension de base de React Hook Form, mettons maintenant tout en pratique et créons un formulaire simple avec deux champs : `email` et `password`. Nous rendrons les deux champs obligatoires et validerons le champ email à l'aide d'une expression régulière.

```jsx
import { useForm } from 'react-hook-form';

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  
  const onSubmit = (data) => {
    console.log(data);
  };
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Email</label>
      <input type="email" {...register("email", { required: true, pattern: /^\S+@\S+$/i })} />
      {errors.email && <p>L'email est obligatoire et doit être valide</p>}
      
      <label>Mot de passe</label>
      <input type="password" {...register("password", { required: true })} />
      {errors.password && <p>Le mot de passe est obligatoire</p>}
      
      <button type="submit">Soumettre</button>
    </form>
  );
}

export default LoginForm;

```

<img src="https://i.imgur.com/zDd8ZDK.gif" style="border: 1px solid #333; border-radius: 5px"/>

Dans cette section, nous avons couvert les bases de l'utilisation de React Hook Form :

* Pour enregistrer les champs de formulaire
* Gérer les soumissions de formulaire
* Afficher les erreurs de validation

Mais ce n'est que la partie émergée de l'iceberg. React Hook Form offre de nombreuses autres fonctionnalités et capacités que nous n'avons pas couvertes ici. Je vous recommande donc vivement de consulter la [documentation](https://react-hook-form.com/get-started/) de React Hook Form pour en savoir plus sur son utilisation efficace dans vos projets.

## Récapitulatif

Dans ce tutoriel, nous avons couvert les bases de la création de formulaires dans React. Nous avons appris qu'il existe deux approches courantes pour créer des formulaires dans React : les composants contrôlés et non contrôlés.

Les composants contrôlés reposent sur la gestion d'état pour suivre l'état des entrées de formulaire, tandis que les composants non contrôlés utilisent des `refs` pour accéder aux entrées de formulaire et à leurs valeurs.

Nous avons également appris que l'utilisation de bibliothèques tierces facilite grandement la création de formulaires dans React. Des bibliothèques comme React Hook Form fournissent de nombreuses fonctionnalités prêtes à l'emploi et peuvent aider à réduire la quantité de code standard nécessaire pour créer des formulaires dans React.

Avec ces concepts en tête, vous devriez être en mesure de créer des formulaires complexes dans React qui sont faciles à gérer et offrent une excellente expérience utilisateur.

## Conclusion

Si vous souhaitez accéder à tout le code utilisé dans cet article, y compris le style, je l'ai compilé dans un seul [dépôt](https://github.com/dboatengg/react-forms) pour votre commodité. Rendez-vous dans le dépôt et vous y trouverez tout ce dont vous avez besoin.

Bon codage !