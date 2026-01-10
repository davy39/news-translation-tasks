---
title: Qu'est-ce que les composants contrôlés et non contrôlés dans React.js ?
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-06-21T20:18:52.000Z'
originalURL: https://freecodecamp.org/news/what-are-controlled-and-uncontrolled-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--1-.png
tags:
- name: components
  slug: components
- name: React
  slug: react
seo_title: Qu'est-ce que les composants contrôlés et non contrôlés dans React.js ?
seo_desc: "In React.js, managing form inputs and user interactions is a crucial part\
  \ of building dynamic web applications. \nTwo key concepts that developers need\
  \ to understand are controlled and uncontrolled components. These concepts define\
  \ how form data is ha..."
---

Dans React.js, la gestion des entrées de formulaire et des interactions utilisateur est une partie cruciale de la construction d'applications web dynamiques.

Deux concepts clés que les développeurs doivent comprendre sont les composants contrôlés et non contrôlés. Ces concepts définissent comment les données de formulaire sont gérées au sein d'un composant React.

Les composants contrôlés s'appuient sur l'état React pour gérer les données de formulaire, tandis que les composants non contrôlés utilisent le DOM lui-même pour gérer les données de formulaire.

Dans cet article, nous explorerons les différences entre les composants contrôlés et non contrôlés, comment les implémenter, et quelques bonnes pratiques pour utiliser chaque approche dans vos applications React.

## Table des matières

1. [Qu'est-ce que les composants contrôlés ?](#heading-quest-ce-que-les-composants-controles)
2. [Comment fonctionnent les composants contrôlés](#heading-comment-fonctionnent-les-composants-controles)
3. [Avantages de l'utilisation des composants contrôlés](#heading-avantages-de-lutilisation-des-composants-controles)
4. [Exemples de composants contrôlés](#heading-exemples-de-composants-controles)
5. [Qu'est-ce que les composants non contrôlés ?](#heading-quest-ce-que-les-composants-non-controles)
6. [Comment fonctionnent les composants non contrôlés](#heading-comment-fonctionnent-les-composants-non-controles)
7. [Quand utiliser les composants non contrôlés](#heading-quand-utiliser-les-composants-non-controles)
8. [Limitations des composants non contrôlés](#heading-limitations-des-composants-non-controles)
9. [Exemples de composants non contrôlés](#heading-exemples-de-composants-non-controles)
10. [Facteurs à considérer lors du choix entre les composants contrôlés et non contrôlés](#heading-facteurs-a-considerer-lors-du-choix-entre-les-composants-controles-et-non-controles)
11. [Conclusion](#heading-conclusion)

## Qu'est-ce que les composants contrôlés ?

Les composants contrôlés sont des éléments de formulaire (comme `input`, `textarea`, ou `select`) qui sont gérés par l'état React. Cela signifie que la valeur de l'élément de formulaire est définie et mise à jour via l'état React, faisant de React la "source unique de vérité" pour les données du formulaire.

En contrôlant les éléments de formulaire via l'état, vous obtenez plus de contrôle sur les interactions utilisateur et pouvez facilement appliquer une validation, formater les données et répondre aux changements.

Voici un exemple de composant contrôlé :

```jsx
import React, { useState } from 'react';

function ControlledComponent() {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Un nom a été soumis : ' + value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Nom :
        <input type="text" value={value} onChange={handleChange} />
      </label>
      <button type="submit">Soumettre</button>
    </form>
  );
}

export default ControlledComponent;
```

Dans cet exemple :

* L'état `value` contient la valeur actuelle du champ de saisie.
* La fonction `handleChange` met à jour l'état chaque fois que l'utilisateur tape dans le champ de saisie.
* La fonction `handleSubmit` gère la soumission du formulaire, en utilisant la valeur actuelle de l'état.

## Comment fonctionnent les composants contrôlés

Les composants contrôlés dans React garantissent que les données du formulaire sont gérées par l'état React, offrant une manière cohérente et prévisible de gérer les entrées utilisateur.

Voici une décomposition de leur fonctionnement, y compris la gestion de l'état dans le composant parent, le passage des valeurs en tant que props aux composants enfants, la gestion des entrées utilisateur avec des gestionnaires d'événements, et la mise à jour de l'état dans le composant parent.

### Gestion de l'état dans le composant parent

La gestion de l'état est souvent gérée dans le composant parent, surtout lorsque plusieurs composants enfants doivent interagir ou partager un état. Le composant parent maintient l'état et le transmet aux composants enfants via les props.

```jsx
import React, { useState } from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const [inputValue, setInputValue] = useState('');

  return (
    <div>
      <h1>Exemple de composant contrôlé</h1>
      <ChildComponent value={inputValue} setValue={setInputValue} />
    </div>
  );
}

export default ParentComponent;
```

### Passage des valeurs en tant que props à un composant enfant

Le composant parent transmet la valeur de l'état et une fonction de mise à jour de l'état au composant enfant en tant que props. Cela permet au composant enfant d'afficher l'état actuel et de le mettre à jour lorsque nécessaire.

```jsx
import React from 'react';

function ChildComponent({ value, setValue }) {
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <form>
      <label>
        Nom :
        <input type="text" value={value} onChange={handleChange} />
      </label>
    </form>
  );
}

export default ChildComponent;
```

### Gestion des entrées utilisateur avec des gestionnaires d'événements

Les gestionnaires d'événements sont utilisés pour gérer les entrées utilisateur. Lorsque l'utilisateur tape dans le champ de saisie, l'événement `onChange` déclenche la fonction `handleChange`, qui met à jour l'état dans le composant parent.

```jsx
function ChildComponent({ value, setValue }) {
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <form>
      <label>
        Nom :
        <input type="text" value={value} onChange={handleChange} />
      </label>
    </form>
  );
}
```

### Mise à jour de l'état dans un composant parent

Lorsque la fonction de mise à jour de l'état (`setValue`) est appelée dans le composant enfant, elle met à jour l'état dans le composant parent. Cela provoque le re-rendu du composant parent, qui à son tour re-rend le composant enfant avec la nouvelle valeur de l'état.

```jsx
function ParentComponent() {
  const [inputValue, setInputValue] = useState('');

  return (
    <div>
      <h1>Exemple de composant contrôlé</h1>
      <ChildComponent value={inputValue} setValue={setInputValue} />
    </div>
  );
}
```

### Mise en place complète

Voici l'exemple complet montrant comment les composants contrôlés fonctionnent avec la gestion de l'état dans le composant parent :

```jsx
// ParentComponent.jsx
import React, { useState } from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const [inputValue, setInputValue] = useState('');

  return (
    <div>
      <h1>Exemple de composant contrôlé</h1>
      <ChildComponent value={inputValue} setValue={setInputValue} />
    </div>
  );
}

export default ParentComponent;

// ChildComponent.jsx
import React from 'react';

function ChildComponent({ value, setValue }) {
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <form>
      <label>
        Nom :
        <input type="text" value={value} onChange={handleChange} />
      </label>
    </form>
  );
}

export default ChildComponent;
```

Les composants contrôlés dans React offrent une bonne manière de gérer les données de formulaire en utilisant l'état React comme source unique de vérité. Cette approche implique la gestion de l'état dans le composant parent, le passage des valeurs et des fonctions de mise à jour de l'état en tant que props aux composants enfants, la gestion des entrées utilisateur avec des gestionnaires d'événements, et la mise à jour de l'état dans le composant parent.

Cette méthode garantit un comportement de formulaire cohérent et prévisible, facilitant la mise en œuvre de la validation, du rendu conditionnel et d'autres fonctionnalités interactives.

## Avantages de l'utilisation des composants contrôlés

Les composants contrôlés offrent plusieurs avantages qui peuvent améliorer considérablement l'expérience de développement et la fonctionnalité des applications React. Voici les principaux avantages :

### Gestion d'état prévisible

L'utilisation de composants contrôlés garantit que les données du formulaire sont toujours synchronisées avec l'état React. Cette prévisibilité provient d'une source unique de vérité pour les données, qui est l'état lui-même.

Puisque l'état pilote l'interface utilisateur, tout changement dans l'état se reflète immédiatement dans les éléments de formulaire et vice versa. Cela facilite le débogage et la compréhension du flux de données dans votre application.

**Exemple :**

```jsx
import React, { useState } from 'react';

function PredictableForm() {
  const [name, setName] = useState('');

  const handleChange = (event) => {
    setName(event.target.value);
  };

  return (
    <div>
      <input type="text" value={name} onChange={handleChange} />
      <p>Valeur actuelle : {name}</p>
    </div>
  );
}
```

Dans cet exemple, le champ de saisie et le texte affiché sont toujours synchronisés, offrant un comportement prévisible.

### Validation de formulaire plus facile

Les composants contrôlés rendent la mise en œuvre de la validation de formulaire simple. Puisque les données du formulaire sont stockées dans l'état du composant, vous pouvez facilement les valider avant de mettre à jour l'état ou lors de la soumission du formulaire. Cette approche permet de fournir un retour en temps réel aux utilisateurs lorsqu'ils interagissent avec le formulaire.

**Exemple :**

```jsx
import React, { useState } from 'react';

function ValidatedForm() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const handleChange = (event) => {
    const value = event.target.value;
    setEmail(value);

    if (!value.includes('@')) {
      setError('Adresse email invalide');
    } else {
      setError('');
    }
  };

  return (
    <div>
      <input type="email" value={email} onChange={handleChange} />
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}
```

Ici, la logique de validation s'exécute à chaque changement, fournissant un retour immédiat à l'utilisateur si la saisie est invalide.

### Intégration avec des bibliothèques d'interface utilisateur complexes

Les composants contrôlés s'intègrent parfaitement avec des bibliothèques et des frameworks d'interface utilisateur complexes, tels que Redux pour la gestion de l'état ou Formik pour la gestion des formulaires.

En gérant les données de formulaire dans l'état du composant, vous pouvez facilement connecter vos formulaires à ces bibliothèques et bénéficier de leurs fonctionnalités avancées comme la gestion globale de l'état, la récupération asynchrone de données, et plus encore.

**Exemple avec Formik :**

```jsx
import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const SignupForm = () => (
  <Formik
    initialValues={{ email: '' }}
    validationSchema={Yup.object({
      email: Yup.string().email('Adresse email invalide').required('Obligatoire'),
    })}
    onSubmit={(values, { setSubmitting }) => {
      setTimeout(() => {
        alert(JSON.stringify(values, null, 2));
        setSubmitting(false);
      }, 400);
    }}
  >
    {({ isSubmitting }) => (
      <Form>
        <label htmlFor="email">Email</label>
        <Field type="email" name="email" />
        <ErrorMessage name="email" component="div" />
        <button type="submit" disabled={isSubmitting}>
          Soumettre
        </button>
      </Form>
    )}
  </Formik>
);

export default SignupForm;
```

Dans cet exemple, Formik gère l'état du formulaire et la validation, démontrant comment les composants contrôlés peuvent faire partie de configurations plus complexes.

Les composants contrôlés offrent une gestion d'état prévisible, une validation de formulaire plus facile et une intégration transparente avec des bibliothèques d'interface utilisateur complexes.

En gardant les données de formulaire dans l'état React, vous assurez la cohérence et le contrôle du comportement de votre application, facilitant la construction et la maintenance d'interfaces utilisateur interactives et dynamiques.

## Exemples de composants contrôlés

Les composants contrôlés sont fondamentaux dans React pour gérer les entrées de formulaire de manière prévisible et gérable.

Voici quelques exemples de la façon dont vous pouvez implémenter des composants contrôlés pour divers types d'entrées de formulaire, y compris les champs de texte, les champs d'email, les champs de mot de passe, les menus déroulants, les cases à cocher et les boutons radio.

### Champs de saisie (Texte, Email, Mot de passe)

##### Champ de texte

```jsx
import React, { useState } from 'react';

function TextInput() {
  const [text, setText] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <label>
        Texte :
        <input type="text" value={text} onChange={handleChange} />
      </label>
      <p>Texte saisi : {text}</p>
    </div>
  );
}

export default TextInput;
```

##### Champ d'email

```jsx
import React, { useState } from 'react';

function EmailInput() {
  const [email, setEmail] = useState('');

  const handleChange = (event) => {
    setEmail(event.target.value);
  };

  return (
    <div>
      <label>
        Email :
        <input type="email" value={email} onChange={handleChange} />
      </label>
      <p>Email saisi : {email}</p>
    </div>
  );
}

export default EmailInput;
```

##### Champ de mot de passe

```jsx
import React, { useState } from 'react';

function PasswordInput() {
  const [password, setPassword] = useState('');

  const handleChange = (event) => {
    setPassword(event.target.value);
  };

  return (
    <div>
      <label>
        Mot de passe :
        <input type="password" value={password} onChange={handleChange} />
      </label>
      <p>Mot de passe saisi : {password}</p>
    </div>
  );
}

export default PasswordInput;
```

#### Menus déroulants

```jsx
import React, { useState } from 'react';

function SelectMenu() {
  const [option, setOption] = useState('option1');

  const handleChange = (event) => {
    setOption(event.target.value);
  };

  return (
    <div>
      <label>
        Choisissez une option :
        <select value={option} onChange={handleChange}>
          <option value="option1">Option 1</option>
          <option value="option2">Option 2</option>
          <option value="option3">Option 3</option>
        </select>
      </label>
      <p>Option sélectionnée : {option}</p>
    </div>
  );
}

export default SelectMenu;
```

#### Cases à cocher

```jsx
import React, { useState } from 'react';

function Checkbox() {
  const [isChecked, setIsChecked] = useState(false);

  const handleChange = (event) => {
    setIsChecked(event.target.checked);
  };

  return (
    <div>
      <label>
        Accepter les termes :
        <input type="checkbox" checked={isChecked} onChange={handleChange} />
      </label>
      <p>Coché : {isChecked ? 'Oui' : 'Non'}</p>
    </div>
  );
}

export default Checkbox;
```

#### Boutons radio

```jsx
import React, { useState } from 'react';

function RadioButton() {
  const [selectedOption, setSelectedOption] = useState('option1');

  const handleChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div>
      <label>
        <input
          type="radio"
          value="option1"
          checked={selectedOption === 'option1'}
          onChange={handleChange}
        />
        Option 1
      </label>
      <label>
        <input
          type="radio"
          value="option2"
          checked={selectedOption === 'option2'}
          onChange={handleChange}
        />
        Option 2
      </label>
      <label>
        <input
          type="radio"
          value="option3"
          checked={selectedOption === 'option3'}
          onChange={handleChange}
        />
        Option 3
      </label>
      <p>Option sélectionnée : {selectedOption}</p>
    </div>
  );
}

export default RadioButton;
```

Les composants contrôlés offrent une manière claire et cohérente de gérer les entrées de formulaire dans React. En utilisant l'état React pour gérer les valeurs des champs de saisie, des menus déroulants, des cases à cocher et des boutons radio, vous assurez que l'interface utilisateur reste synchronisée avec l'état.

Cette approche simplifie la validation, rend la gestion des données prévisible et facilite l'intégration avec des bibliothèques d'interface utilisateur complexes.

## Qu'est-ce que les composants non contrôlés ?

Les composants non contrôlés dans React gèrent leur propre état en interne plutôt que de s'appuyer sur l'état React. Cette approche est utile pour les formulaires simples où vous n'avez pas besoin de manipuler les données d'entrée via les mises à jour de l'état React.

**Exemple :**

```jsx
import React, { Component } from 'react';

class UncontrolledComponent extends Component {
  constructor(props) {
    super(props);
    // Crée une référence pour contenir l'élément DOM de l'entrée
    this.inputRef = React.createRef();
  }

  handleSubmit = () => {
    // Accède à la valeur de l'entrée en utilisant la référence
    console.log(this.inputRef.current.value);
  }

  render() {
    return (
      <div>
        {/* Utilise l'attribut ref pour attacher la référence à l'élément d'entrée */}
        <input 
          type="text" 
          ref={this.inputRef} 
        />
        <button onClick={this.handleSubmit}>Soumettre</button>
      </div>
    );
  }
}
```

* **Utilisation des références :** Dans les composants non contrôlés, nous utilisons l'attribut `ref` pour créer une référence (`this.inputRef`) au nœud DOM du champ de saisie.
* **Gestion de la saisie :** Lorsque l'utilisateur entre des données et clique sur "Soumettre", `this.inputRef.current.value` nous permet d'accéder directement à la valeur actuelle du champ de saisie sans impliquer l'état React.
* **Avantages :** Les composants non contrôlés peuvent être plus simples et plus rapides pour la gestion de formulaires basiques. Ils sont souvent utilisés lorsque les données du formulaire ne sont pas nécessaires dans l'état React pour un traitement ou une validation.

**Points clés :**

* **État interne :** Les composants non contrôlés gèrent leur état en interne à l'aide de références, et non avec les mises à jour de l'état React.
* **Accès direct au DOM :** L'accès aux données du formulaire se fait directement via les références DOM (`this.inputRef.current.value`).
* **Simplicité :** Ils sont simples pour les formulaires basiques où la validation en temps réel ou les interactions complexes avec le formulaire ne sont pas nécessaires.

Les composants non contrôlés sont pratiques dans les scénarios où vous souhaitez une approche légère pour gérer les données de formulaire sans le surcoût de la gestion de l'état dans React.

## Comment fonctionnent les composants non contrôlés

Les composants non contrôlés gèrent leur état en interne en utilisant des références DOM (`useRef` hook dans les composants fonctionnels ou `React.createRef()` dans les composants de classe) pour accéder directement aux valeurs des éléments de formulaire.

Contrairement aux composants contrôlés, où les données de formulaire sont gérées via l'état React et mises à jour via `setState`, les composants non contrôlés contournent la gestion de l'état de React pour la gestion des entrées de formulaire.

### Accès direct au DOM avec le hook useRef

Dans les composants fonctionnels, le hook `useRef` nous permet de créer une référence mutable qui persiste à travers les rendus. Nous pouvons utiliser cette référence pour accéder directement aux nœuds DOM, tels que les champs de saisie.

**Exemple :**

```jsx
import React, { useRef } from 'react';

function UncontrolledComponent() {
  const inputRef = useRef(null); // Crée une référence pour contenir l'élément DOM de l'entrée

  const handleSubmit = () => {
    // Accède à la valeur de l'entrée en utilisant la référence
    console.log(inputRef.current.value);
  };

  return (
    <div>
      <input type="text" ref={inputRef} />
      <button onClick={handleSubmit}>Soumettre</button>
    </div>
  );
}

export default UncontrolledComponent;
```

### Accès à la valeur d'un élément lors de la soumission

Dans l'exemple ci-dessus :

* **Création d'une référence :** `const inputRef = useRef(null);` initialise une référence nommée `inputRef` pour contenir la référence à l'élément DOM de l'entrée.
* **Gestion de la soumission :** Lorsque le bouton "Soumettre" est cliqué (`onClick={handleSubmit}`), la fonction `handleSubmit` récupère la valeur actuelle du champ de saisie en utilisant `inputRef.current.value`.

**Points clés :**

* **Accès au DOM :** Le hook `useRef` permet un accès direct aux éléments DOM, nous permettant d'interagir avec eux sans mettre à jour l'état React.
* **Soumission du formulaire :** Lors de la soumission du formulaire (`onClick={handleSubmit}`), la fonction accède à la valeur actuelle du champ de saisie via `inputRef.current.value`.
* **Simplicité :** Les composants non contrôlés sont simples pour les scénarios de gestion de formulaires basiques où la manipulation directe du DOM suffit, évitant le besoin de gérer les mises à jour de l'état dans React.

L'utilisation de composants non contrôlés avec `useRef` est particulièrement utile pour gérer les formulaires où la validation en temps réel ou les interactions complexes ne sont pas nécessaires, en se concentrant plutôt sur la simplicité et la performance.

## Quand utiliser les composants non contrôlés

Les composants non contrôlés sont idéaux dans des scénarios spécifiques où la simplicité et la manipulation directe du DOM sont avantageuses par rapport à la gestion de l'état avec React.

Voici les situations clés où l'utilisation de composants non contrôlés est bénéfique :

### 1. Formulaires simples avec des interactions limitées

Les composants non contrôlés excellent dans les scénarios où :

* **Les formulaires ne sont pas très complexes :** Le formulaire est simple avec des champs de saisie minimaux et ne nécessite pas de validation complexe ou de mises à jour dynamiques basées sur d'autres entrées de formulaire.
* **La performance est importante :** L'accès direct aux valeurs du formulaire via les références DOM (`useRef` ou `React.createRef()`) peut être plus performant que la mise à jour de l'état React pour chaque changement de saisie, surtout dans les grands formulaires.
* **Vous voulez de la simplicité :** Lorsque vous préférez une implémentation plus simple sans gérer les mises à jour d'état et les re-rendus pour les entrées de formulaire.

### 2. Gestion du focus (Sélection de texte)

Dans certains cas, vous pourriez avoir besoin de gérer l'interaction utilisateur telle que la sélection de texte dans un champ de saisie ou le focus programmatique sur une entrée spécifique sans déclencher inutilement des mises à jour de l'état React.

Les composants non contrôlés vous permettent de :

* **Manipuler directement le DOM :** Utiliser des méthodes DOM comme `select()` sur l'élément d'entrée directement via les références pour gérer le focus ou la sélection de texte.
* **Gérer le focus et la sélection de texte directement avec les références :** Cela peut être plus efficace et direct par rapport au déclenchement de mises à jour d'état et à la gestion de l'état de focus dans les composants React.

#### Exemple d'utilisation :

```jsx
import React, { useRef } from 'react';

function UncontrolledComponent() {
  const inputRef = useRef(null); // Crée une référence pour contenir l'élément DOM de l'entrée

  const handleFocus = () => {
    inputRef.current.select(); // Sélectionne tout le texte dans le champ de saisie
  };

  return (
    <div>
      <input type="text" ref={inputRef} defaultValue="Valeur initiale" />
      <button onClick={handleFocus}>Sélectionner le texte</button>
    </div>
  );
}

export default UncontrolledComponent;
```

Dans cet exemple, le clic sur le bouton "Sélectionner le texte" appelle `inputRef.current.select()` pour sélectionner tout le texte dans le champ de saisie directement, sans impliquer de mises à jour de l'état React. C'est une utilisation simple mais efficace des composants non contrôlés pour gérer le focus et la sélection de texte.

## Limitations des composants non contrôlés

L'utilisation de composants non contrôlés dans React peut offrir des avantages de simplicité et de performance dans certains scénarios, mais ils présentent également des limitations importantes à considérer :

### Difficulté de validation de formulaire :

* Les composants non contrôlés peuvent rendre la validation de formulaire plus difficile par rapport aux composants contrôlés. Puisque les données du formulaire sont gérées en interne par le DOM plutôt que par l'état React, la validation et la garantie de la cohérence des données entre plusieurs entrées peuvent être complexes.
* La logique de validation implique souvent l'accès et la vérification de la valeur de chaque entrée directement via les références (`ref.current.value`). Cette approche peut conduire à un code de validation plus manuel et sujet aux erreurs, surtout dans les formulaires avec des exigences de validation complexes.

### Gestion d'état moins prévisible :

* Les composants non contrôlés contournent la gestion de l'état de React, ce qui peut conduire à une gestion de l'état moins prévisible dans les applications complexes. Les changements dans les données du formulaire ne sont pas automatiquement synchronisés avec les mises à jour de l'état de React ou d'autres états de composants, ce qui peut potentiellement entraîner des incohérences.
* Ce manque de synchronisation peut rendre difficile le maintien d'une source unique de vérité pour les données du formulaire entre différents composants ou lors de l'intégration avec d'autres solutions de gestion de l'état comme Redux ou l'API Context.

### Intégration limitée à l'écosystème React :

* Les composants non contrôlés peuvent ne pas tirer pleinement parti des fonctionnalités de l'écosystème React, telles que la persistance de l'état, le débogage temporel (avec Redux), ou l'intégration transparente avec des bibliothèques tierces conçues pour les composants contrôlés.
* Les composants s'appuyant sur l'état React bénéficient de ces fonctionnalités, améliorant la productivité des développeurs et la maintenabilité de l'application.

## Exemples de composants non contrôlés

Les composants non contrôlés dans React sont particulièrement utiles pour gérer les champs de saisie et les éléments de zone de texte où la manipulation directe du DOM suffit, et où la gestion de l'état React n'est pas nécessaire.

Voici des exemples de la façon dont les composants non contrôlés peuvent être appliqués :

### 1. Champs de saisie (Données en lecture seule ou pré-remplies)

Les composants non contrôlés peuvent être utilisés lorsque vous devez afficher des données en lecture seule ou pré-remplies dans un champ de saisie sans gérer son état dans React.

**Exemple :**

```jsx
import React, { useRef } from 'react';

function UncontrolledInput() {
  const initialValue = 'Bonjour le monde !';
  const inputRef = useRef(null); // Crée une référence pour contenir l'élément DOM de l'entrée

  const handleFocus = () => {
    inputRef.current.select(); // Sélectionne tout le texte dans le champ de saisie au focus
  };

  return (
    <div>
      {/* Utilisation de defaultValue pour les données pré-remplies */}
      <input type="text" ref={inputRef} defaultValue={initialValue} readOnly />
      <button onClick={handleFocus}>Sélectionner le texte</button>
    </div>
  );
}

export default UncontrolledInput;
```

Dans cet exemple :

* L'attribut `defaultValue` définit la valeur initiale du champ de saisie.
* L'attribut `readOnly` empêche les utilisateurs de modifier le champ de saisie, le rendant en lecture seule.
* Le hook `useRef` gère le focus et la sélection du texte dans le champ de saisie en utilisant `inputRef.current`.

### 2. Éléments de zone de texte

Les composants non contrôlés sont également applicables aux éléments de zone de texte, surtout lorsqu'il s'agit de saisie de texte multiligne où les mises à jour d'état immédiates ne sont pas nécessaires.

**Exemple :**

```jsx
import React, { useRef } from 'react';

function UncontrolledTextarea() {
  const initialText = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.';
  const textareaRef = useRef(null); // Crée une référence pour contenir l'élément DOM de la zone de texte

  const handleClear = () => {
    textareaRef.current.value = ''; // Efface directement le contenu de la zone de texte
  };

  return (
    <div>
      {/* Utilisation de defaultValue pour le contenu pré-rempli */}
      <textarea ref={textareaRef} defaultValue={initialText} rows={4} cols={50} />
      <button onClick={handleClear}>Effacer le texte</button>
    </div>
  );
}

export default UncontrolledTextarea;
```

Dans cet exemple :

* L'attribut `defaultValue` définit le contenu initial de la zone de texte.
* Le hook `useRef` gère la manipulation directe du contenu de la zone de texte en utilisant `textareaRef.current`.
* Les attributs `rows` et `cols` définissent les dimensions de la zone de texte.

**Points clés :**

* **Accès direct au DOM :** Les composants non contrôlés utilisent `useRef` pour manipuler directement les éléments DOM afin de gérer les champs de saisie et le contenu des zones de texte.
* **Performance :** Adapté aux scénarios où les mises à jour en temps réel ou la gestion complexe de l'état ne sont pas requises, améliorant les performances en évitant les mises à jour d'état inutiles.
* **Simplicité :** Fournit une approche simple pour gérer les éléments de formulaire avec des valeurs par défaut ou en lecture seule, maintenant la simplicité dans la logique des composants.

Ces exemples démontrent comment les composants non contrôlés peuvent gérer les champs de saisie et les éléments de zone de texte de manière efficace dans les applications React, en se concentrant sur la simplicité et la manipulation directe du DOM pour des cas d'utilisation spécifiques.

## Facteurs à considérer lors du choix entre les composants contrôlés et non contrôlés

Lors de la décision entre les composants contrôlés et non contrôlés dans React, plusieurs facteurs doivent être considérés pour déterminer quelle approche convient le mieux aux exigences de votre application. Voici les considérations clés pour chaque facteur :

### 1. Complexité du formulaire

#### Composants contrôlés :

* **Avantages :** Adaptés aux formulaires complexes où vous avez besoin d'un contrôle précis sur l'état du formulaire et son interaction avec d'autres composants.
* **Utilisation :** Utilisez des composants contrôlés lorsque les entrées de formulaire dépendent les unes des autres, nécessitent une validation, ou lorsque vous devez synchroniser l'état du formulaire entre plusieurs composants ou pages.

#### Composants non contrôlés :

* **Avantages :** Simplifient l'implémentation pour les formulaires basiques avec une interactivité minimale ou lorsque la manipulation directe du DOM suffit.
* **Utilisation :** Idéal pour les formulaires simples sans validation complexe ou lorsque la gestion de l'état du formulaire dans React n'est pas nécessaire pour votre cas d'utilisation.

### 2. Besoin de validation de formulaire

#### Composants contrôlés :

* **Avantages :** Intégration plus facile avec les bibliothèques de validation de formulaire (par exemple, Formik, Yup) puisque l'état du formulaire est géré dans l'état React.
* **Utilisation :** Utilisez des composants contrôlés lors de la mise en œuvre de règles de validation complexes, telles que la validation conditionnelle ou la logique de validation asynchrone.

#### Composants non contrôlés :

* **Défis :** La gestion de la validation de formulaire peut être plus manuelle et moins intégrée, car les données du formulaire sont gérées directement via la manipulation du DOM.
* **Utilisation :** Envisagez des composants non contrôlés pour les formulaires simples où les exigences de validation sont minimales ou où la logique de validation personnalisée peut être gérée sans dépendre fortement des mises à jour de l'état React.

### 3. Intégration avec des bibliothèques externes

#### Composants contrôlés :

* **Avantages :** S'intègre parfaitement avec des solutions de gestion d'état externes comme Redux ou l'API Context de React pour gérer l'état global de l'application.
* **Utilisation :** Préférez les composants contrôlés lorsque votre application nécessite une intégration avec des bibliothèques tierces ou lorsque vous tirez parti des fonctionnalités avancées de l'écosystème React (par exemple, le débogage temporel avec Redux).

#### Composants non contrôlés :

* **Considérations :** Peut nécessiter des efforts supplémentaires pour s'intégrer avec des bibliothèques externes qui supposent un comportement de composant contrôlé.
* **Utilisation :** Utilisez des composants non contrôlés lorsque la gestion d'état externe n'est pas nécessaire, en vous concentrant sur une implémentation légère et en minimisant les dépendances.

### Considérations supplémentaires :

#### Performance :

Les composants contrôlés peuvent entraîner des surcoûts en raison des mises à jour fréquentes de l'état, tandis que les composants non contrôlés peuvent offrir de meilleures performances pour les formulaires simples en réduisant les re-rendus.

#### Préférence du développeur :

Considérez la familiarité et les préférences de l'équipe avec les modèles de gestion d'état React lors de la décision entre les composants contrôlés et non contrôlés.

### Résumé :

**Choisissez des composants contrôlés** pour les formulaires complexes, les besoins de validation robustes et l'intégration transparente avec les bibliothèques de gestion d'état et de validation externes.

**Optez pour des composants non contrôlés** pour les formulaires plus simples, les exigences de validation minimales et lorsque la manipulation directe du DOM fournit une fonctionnalité suffisante sans avoir besoin de gérer l'état du formulaire dans React.

## Conclusion

Le choix entre les composants contrôlés et non contrôlés dans React dépend de plusieurs facteurs critiques qui déterminent l'approche optimale pour la gestion des formulaires au sein de votre application.

En fin de compte, la décision doit être alignée avec les besoins spécifiques de votre projet, en tenant compte de facteurs tels que la complexité du formulaire, les exigences de validation, l'intégration avec des bibliothèques externes et les préférences des développeurs.

En évaluant soigneusement ces facteurs, vous pouvez mettre en œuvre la stratégie de gestion de formulaire la plus efficace dans React qui équilibre la fonctionnalité, la performance et la facilité de maintenance.

Connectez-vous avec moi sur [LinkedIn](https://linkedin.com/in/joanayebola).