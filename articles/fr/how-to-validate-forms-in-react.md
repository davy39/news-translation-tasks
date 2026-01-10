---
title: Comment valider les formulaires dans React – Un tutoriel étape par étape pour
  débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-11T19:08:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-forms-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/thumbnail.jpg
tags:
- name: Form validations
  slug: form-validations
- name: React
  slug: react
seo_title: Comment valider les formulaires dans React – Un tutoriel étape par étape
  pour débutants
seo_desc: "By Yazdun Fadali\nIf you've ever worked with form validation in React,\
  \ you know that it can quickly become messy and overwhelming. This is especially\
  \ the case if you're just starting out with React. \nIn this tutorial, I will show\
  \ you how to create reu..."
---

Par Yazdun Fadali

Si vous avez déjà travaillé avec la validation de formulaires dans React, vous savez que cela peut rapidement devenir désordonné et écrasant. C'est particulièrement le cas si vous débutez avec React. 

Dans ce tutoriel, je vais vous montrer comment créer des composants React réutilisables qui vous permettent de construire des formulaires maintenables et propres. Ils pourront facilement évoluer à mesure que votre application grandit. 

Vous apprendrez également comment implémenter la bibliothèque populaire react-hook-form dans votre application React, ce qui simplifiera le processus d'ajout de validations de formulaires. Et vous apprendrez comment implémenter des validations d'entrée réutilisables dans toute votre application React, éliminant ainsi le besoin de code répétitif. 

Préparez-vous à améliorer vos compétences en gestion de formulaires dans React avec ce guide ultime. Plongeons-nous et maîtrisons la validation de formulaires dans React.

## Voici ce que nous allons couvrir :

1. [Qu'allons-nous construire ?](#heading-quallons-nous-construire)
2. [Mise en route](#heading-installation)
3. [Comment construire un composant d'entrée réutilisable](#heading-comment-construire-un-composant-dentree-reutilisable)
4. [Comment implémenter la validation d'entrée dans React](#heading-comment-implementer-la-validation-dentree-dans-react)
5. [Comment afficher des messages d'erreur appropriés](#heading-comment-afficher-des-messages-derreur-appropriees)
6. [Validation d'entrée dynamique](#heading-validation-dentree-dynamique)
7. [Comment implémenter une fonctionnalité d'entrée multiline dans le composant d'entrée](#heading-comment-implementer-une-fonctionnalite-dentree-multiline-dans-le-composant-dentree)
8. [Comment gérer la soumission réussie du formulaire](#heading-comment-gerer-la-soumission-reussie-du-formulaire)
9. [Conclusion](#heading-conclusion)

Très bien, plongeons-nous !

## **Qu'allons-nous construire ?**

Dans ce tutoriel, nous allons construire un formulaire minimaliste qui permettra aux utilisateurs de saisir des données. Voici une rapide démonstration ([démo en direct](https://react-fcc-forms.vercel.app/)) :

![GIF affichant un formulaire React avec plusieurs champs de saisie et un bouton de soumission](https://www.freecodecamp.org/news/content/images/2023/04/ezgif-3-767ff4d168.gif)
_Aperçu du projet final_

Nous allons tirer parti de la puissance de react-hook-form, une bibliothèque populaire de validation de formulaires dans l'écosystème React, pour gérer efficacement la validation des formulaires. Nous allons utiliser Tailwind CSS pour le style. 

Ne vous inquiétez pas si vous n'êtes pas familier avec Tailwind CSS ou react-hook-form, car ce tutoriel est conçu pour être adapté aux débutants. Mais avoir une compréhension de base des fondamentaux de React vous aidera à tirer le meilleur parti de ce tutoriel. 

Alors, commençons et créons un formulaire élégant et fonctionnel dans React !

## Mise en route

Pour commencer avec ce tutoriel, je vous recommande vivement d'utiliser le [modèle de démarrage](https://github.com/Yazdun/react-fcc-forms/tree/starter) que j'ai préparé pour vous. Il contient toutes les dépendances nécessaires et la structure des dossiers, vous n'aurez donc pas besoin de passer du temps à configurer votre projet à partir de zéro. 

Vous pouvez simplement cloner le modèle de démarrage à partir du dépôt GitHub fourni et suivre le tutoriel sans aucun retard. Cela vous permettra de vous concentrer sur l'apprentissage et la mise en œuvre des concepts de validation de formulaires dans React sans vous enliser dans les détails de configuration.

* Modèle de démarrage : [Voir sur GitHub](https://github.com/Yazdun/react-fcc-forms/tree/starter)
* Version finale : [Voir sur GitHub](https://github.com/Yazdun/react-fcc-forms/tree/main)

Après avoir configuré le modèle de démarrage et l'avoir exécuté sur votre machine locale, vous devriez pouvoir voir la page suivante. Cette page servira de point de départ pour notre projet de validation de formulaires dans React.

![simple page web React avec un titre qui dit 'Bienvenue dans le tutoriel des formulaires React'](https://www.freecodecamp.org/news/content/images/2023/04/image-90.png)
_Page de départ pour notre projet_

À partir de là, nous allons progressivement construire sur le code existant et implémenter la validation de formulaires en utilisant react-hook-form.

Pendant ce tutoriel, nous allons nous concentrer sur deux fichiers clés : `src/components/Input.jsx` et `src/Form.jsx`.

Dans `src/components/Input.jsx`, nous allons créer un composant d'entrée React réutilisable. Ce composant servira de base à notre formulaire, permettant aux utilisateurs de saisir des données de manière propre et conviviale. 

Nous allons implémenter la validation d'entrée en utilisant react-hook-form, ce qui garantira que les données saisies par les utilisateurs sont valides avant d'être soumises.

Ensuite, nous passerons à `src/Form.jsx`, où nous gérerons la validation et la soumission du formulaire. Ce fichier servira de conteneur principal pour notre formulaire, et nous utiliserons react-hook-form pour gérer efficacement la validation du formulaire.

En complétant ces deux fichiers, vous serez en mesure de créer un formulaire beau et fonctionnel avec des composants d'entrée réutilisables et une validation de formulaire efficace. Alors plongeons dans le code et construisons notre projet de validation de formulaires étape par étape.

## Comment construire un composant d'entrée réutilisable

Pour commencer notre projet de validation de formulaires, nous allons d'abord créer un composant d'entrée réutilisable. Actuellement, notre `src/components/Input.jsx` ressemble à ceci : 

![Une image montrant l'éditeur Visual Studio Code (VSCode) avec un fichier de code React ouvert. Le fichier de code affiche un simple composant React nommé 'Input' qui rend un div avec le contenu 'input!'. Sous le composant 'Input', il y a un autre composant React nommé 'InputError' qui rend un div avec le contenu 'error'.](https://www.freecodecamp.org/news/content/images/2023/04/image-102.png)
_Capture d'écran de `src/components/Input.jsx`_

Le code de démarrage fourni importe les dépendances nécessaires telles que `classnames`, `react-hook-form`, `framer-motion`, et `react-icons`. Il définit un composant `Input`, qui rend actuellement un simple texte "input!". Il définit également un composant `InputError` qui rend actuellement un texte "error". 

De plus, il inclut un objet d'animation framer motion `framer_error` avec des propriétés initial, animate, exit, et transition pour la gestion des erreurs. Ce code sera encore amélioré et personnalisé pour créer un composant d'entrée réutilisable pour notre projet de validation de formulaires.

Il est maintenant temps de plonger dans un peu de codage ! Notre composant `Input` recevra des props qui détermineront le type d'entrée à rendre, le placeholder, l'id, et ainsi de suite. Nous allons utiliser Tailwind CSS pour ajouter du style à notre composant d'entrée.  

Commençons à améliorer notre composant d'entrée avec des props et Tailwind CSS. Ajoutez le code suivant à `src/components/Input.jsx` : 

```jsx
export const Input = ({ label, type, id, placeholder }) => {
  return (
    <div className="flex flex-col w-full gap-2">
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
      </div>
      <input
        id={id}
        type={type}
        className="w-full p-5 font-medium border rounded-md border-slate-300 placeholder:opacity-60"
        placeholder={placeholder}
      />
    </div>
  )
}
```

Le composant `Input` reçoit `({ label, type, id, placeholder })` en tant que props. Ces props sont ensuite utilisés pour rendre dynamiquement le composant Input. 

La prop `label` est utilisée comme contenu textuel de l'élément `label`, et les props `type`, `id`, et `placeholder` sont passées directement aux attributs correspondants de l'élément `input` en utilisant la syntaxe JSX. Cela permet au composant `Input` d'être flexible et réutilisable, car différentes valeurs peuvent être passées en tant que props pour personnaliser son comportement en fonction du cas d'utilisation spécifique.

Maintenant, voyons notre composant d'entrée en action en ajoutant le code suivant à `src/Form.jsx` :

```jsx
export const Form = () => {
  return (
    <div className="container mt-5 text-center">
      <div className="grid gap-5 md:grid-cols-2">
        <Input
          label="name"
          type="text"
          id="name"
          placeholder="type your name..."
        />
        <Input
          label="password"
          type="password"
          id="password"
          placeholder="type your password..."
        />
      </div>
    </div>
  )
}
```

Après avoir ajouté le code à `src/Form.jsx`, ouvrez votre serveur local et vous devriez pouvoir voir la page résultante avec le composant d'entrée : 

![montrant une simple page web React avec deux champs de saisie](https://www.freecodecamp.org/news/content/images/2023/04/image-104.png)
_Aperçu de ce que nous avons construit jusqu'à présent_

Excellent travail 🎉 ! Vous avez réussi à créer un composant Input réutilisable pour votre application. Maintenant, passons à l'étape suivante et ajoutons quelques fonctionnalités de validation passionnantes pour améliorer la fonctionnalité de notre application.

## Comment implémenter la validation d'entrée dans React

Il est maintenant temps d'implémenter react-hook-form et d'ajouter la validation d'entrée à notre application.

Tout d'abord, nous devons modifier notre fichier `src/Form.jsx` pour utiliser le hook `useForm` et le composant `FormProvider` fourni par react-hook-form. Ces outils nous permettront de gérer facilement la validation et la soumission des formulaires dans notre application React. 

Plongeons dans les détails de leur utilisation efficace. Ajoutez le code suivant à `src/Form.jsx` :

```jsx
export const Form = () => {
  const methods = useForm()

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
  })

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input
            label="name"
            type="text"
            id="name"
            placeholder="type your name..."
          />
          <Input
            label="password"
            type="password"
            id="password"
            placeholder="type your password..."
          />
        </div>
        <div className="mt-5">
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}

```

Il se passe beaucoup de choses dans cette section, mais ne vous inquiétez pas – je vais vous guider à travers. Tout d'abord, vous utilisez `const methods = useForm()` pour configurer les méthodes de formulaire de `react-hook-form` pour la gestion des formulaires. 

Ensuite, vous créez une fonction personnalisée `onSubmit` qui utilise les `methods` pour gérer la soumission du formulaire, que nous exécuterons lorsque le formulaire sera soumis avec succès.

Ensuite, vous utilisez le composant `FormProvider` fourni par `react-hook-form` pour envelopper votre formulaire, ce qui vous permettra d'accéder au contexte du formulaire à l'intérieur de votre composant `Input` plus tard. Ensuite, vous utilisez l'opérateur de propagation JavaScript pour passer toutes les méthodes `useForm` au `FormProvider`.

À l'intérieur du `FormProvider`, vous créez un formulaire et passez `noValidate` pour indiquer que vous souhaitez vous fier entièrement à `react-hook-form` pour la validation du formulaire. Vous empêche également le comportement par défaut du formulaire en passant `onSubmit={e => e.preventDefault()}`. 

Au lieu d'attacher la fonction `onSubmit` au formulaire, vous créez un bouton personnalisé à la fin du fichier et passez la fonction personnalisée `onSubmit` pour gérer la soumission du formulaire.

Ensuite, vous devez mettre à jour le composant Input pour activer la validation du formulaire. Ajoutez le code suivant à `src/components/Input.jsx` :

```jsx
export const Input = ({ label, type, id, placeholder }) => {
  const { register } = useFormContext()

  return (
    <div className="flex flex-col w-full gap-2">
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
      </div>
      <input
        id={id}
        type={type}
        className="w-full p-5 font-medium border rounded-md border-slate-300 placeholder:opacity-60"
        placeholder={placeholder}
        {...register(label, {
          required: {
            value: true,
            message: 'required',
          },
        })}
      />
    </div>
  )
}
```

Vous récupérez la fonction `register` du hook `useFormContext` fourni par react-hook-form, qui est utilisée pour enregistrer un champ d'entrée avec la bibliothèque, lui permettant de gérer la validation. Cette fonction sera passée à l'élément d'entrée. 

La fonction `register` prend deux arguments. Le premier argument est le nom de l'entrée, qui sera utilisé comme clé dans votre contexte de formulaire pour accéder à la valeur de l'entrée ou récupérer son message d'erreur. 

Le deuxième argument est un objet qui contient les validations de l'entrée. React-hook-form prend en charge une large gamme de validations, et vous pouvez vous référer à leur [documentation](https://react-hook-form.com/api/) pour plus d'informations. Pour l'instant, nous utilisons uniquement la validation `required`.

Ouvrez maintenant votre serveur local, vous pouvez entrer des valeurs dans toutes les entrées. Mais le formulaire ne peut pas être soumis tant que toutes les entrées ne sont pas remplies, car elles ont une validation requise. Lors d'une soumission réussie, la fonction personnalisée `onSubmit` s'exécutera et enregistrera les données du formulaire dans la console du navigateur :

![un formulaire dans une page web React, avec la console Chrome ouverte et affichant un objet de données de formulaire soumis.](https://www.freecodecamp.org/news/content/images/2023/04/image-107.png)
_Soumission réussie du formulaire_

Félicitations ! 🎉 Vous avez réussi à compléter cette section difficile. Excellent travail ! Maintenant, passons à l'étape suivante et améliorons notre composant Input personnalisé en apprenant comment passer des validations dynamiques et afficher des messages d'erreur appropriés.

## Comment afficher des messages d'erreur appropriés

Avant d'aller plus loin, occupons-nous des messages d'erreur. Ajoutez ce code à `src/components/Input.jsx` :

```jsx
export const Input = ({ label, type, id, placeholder }) => {
  const { register } = useFormContext()

  return (
    <div className="flex flex-col w-full gap-2">
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
      </div>
      <input
        id={id}
        type={type}
        className="w-full p-5 font-medium border rounded-md border-slate-300 placeholder:opacity-60"
        placeholder={placeholder}
        {...register(label, {
          required: {
            value: true,
            message: 'required',
          },
        })}
      />
    </div>
  )
}

const InputError = ({ message }) => {
  return (
    <motion.p
      className="flex items-center gap-1 px-2 font-semibold text-red-500 bg-red-100 rounded-md"
      {...framer_error}
    >
      <MdError />
      {message}
    </motion.p>
  )
}

const framer_error = {
  initial: { opacity: 0, y: 10 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: 10 },
  transition: { duration: 0.2 },
}

```

Permettez-moi de vous expliquer ce qui se passe ici. Tout d'abord, vous avez créé un composant personnalisé appelé `InputError` qui reçoit un message en tant que prop et l'affiche. 

Vous utilisez framer motion pour ajouter des transitions fluides à ce composant. Framer Motion est une bibliothèque qui nous permet d'ajouter des animations sympas à nos composants React.

Maintenant, mettons à jour votre composant `Input` afin que vous puissiez utiliser `InputError` :

```jsx
import { findInputError, isFormInvalid } from '../utils'

export const Input = ({ label, type, id, placeholder }) => {
  const {
    register,
    formState: { errors },
  } = useFormContext()

  const inputError = findInputError(errors, label)
  const isInvalid = isFormInvalid(inputError)

  return (
    <div className="flex flex-col w-full gap-2">
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
        <AnimatePresence mode="wait" initial={false}>
          {isInvalid && (
            <InputError
              message={inputError.error.message}
              key={inputError.error.message}
            />
          )}
        </AnimatePresence>
      </div>
      <input
        id={id}
        type={type}
        className="w-full p-5 font-medium border rounded-md border-slate-300 placeholder:opacity-60"
        placeholder={placeholder}
        {...register(label, {
          required: {
            value: true,
            message: 'required',
          },
        })}
      />
    </div>
  )
}
```

Vous utilisez le hook `useFormContext` pour récupérer le formState, qui contient tous les messages d'erreur du formulaire. Mais pour afficher correctement les erreurs, vous devez extraire les erreurs pertinentes pour chaque entrée. 

Pour simplifier ce processus, j'ai déjà écrit une fonction utilitaire appelée `findInputError.js` dans le répertoire `src/utils`. Cette fonction prend un objet d'erreurs et le nom de l'entrée comme arguments et retourne les erreurs associées. Ensuite, nous passons l'erreur filtrée au composant `InputError`. Vous pouvez consulter cette fonction utilitaire pour référence :

![Fonction JavaScript nommée 'findInputErrors' affichée dans Visual Studio Code.](https://www.freecodecamp.org/news/content/images/2023/04/image-108.png)
_Capture d'écran de `src/utils/findInputError.js`_

Afin d'afficher un message d'erreur, le formulaire doit être invalide. Pour déterminer si le formulaire est invalide ou non, j'ai également écrit pour vous une simple fonction utilitaire qui prend un objet d'erreur en entrée et retourne vrai si le formulaire n'est pas valide. Vous pouvez consulter cette fonction utilitaire pour référence :

![Fonction JavaScript nommée 'isFormInvalid' affichée dans Visual Studio Code.](https://www.freecodecamp.org/news/content/images/2023/04/image-109.png)
_Capture d'écran de `src/utils/isFormInvalid.js`_

De plus, vous avez peut-être remarqué que nous avons utilisé le composant `AnimatePresence` de la bibliothèque Framer Motion pour envelopper le composant `InputError`. Nous l'avons fait pour ajouter une animation au démontage de InputError, offrant une expérience utilisateur fluide. Bien que cela soit facultatif, j'ai pensé que ce serait une belle touche à ajouter à ce projet. 

Voici à quoi ressemble votre projet jusqu'à présent :

![GIF montrant une page web React avec un formulaire qui est en cours de soumission par un utilisateur, mais des erreurs sont affichées.](https://www.freecodecamp.org/news/content/images/2023/04/ezgif-5-091f434a4a-1.gif)
_Aperçu de ce que nous avons construit jusqu'à présent_

## Validation d'entrée dynamique

### Partie 1

Vous avez fait d'excellents progrès jusqu'à présent ! Actuellement, nous avons des validations codées en dur dans le composant Input, mais vous pourriez avoir besoin de différents types de validations pour chaque entrée à l'avenir. 

Mettons à jour le composant Input pour recevoir un objet de validation en tant que prop et le passer à la fonction `register` de react-hook-form. Modifions `src/components/Input.jsx` comme ceci :

```jsx
export const Input = ({ label, type, id, placeholder, validation, name }) => {
  const {
    register,
    formState: { errors },
  } = useFormContext()

  const inputError = findInputError(errors, name)
  const isInvalid = isFormInvalid(inputError)

  return (
    <div className="flex flex-col w-full gap-2">
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
        <AnimatePresence mode="wait" initial={false}>
          {isInvalid && (
            <InputError
              message={inputError.error.message}
              key={inputError.error.message}
            />
          )}
        </AnimatePresence>
      </div>
      <input
        id={id}
        type={type}
        className="w-full p-5 font-medium border rounded-md border-slate-300 placeholder:opacity-60"
        placeholder={placeholder}
        {...register(name, validation)}
      />
    </div>
  )
}
```

Il n'y a pas eu beaucoup de changements. Vous avez ajouté deux nouvelles props à notre composant Input personnalisé, un objet de validation et une prop de nom. Nous allons utiliser la prop de nom au lieu du label pour enregistrer notre entrée, et l'utiliser également pour trouver les erreurs d'entrée associées. 

Vous avez également passé la prop de validation à la fonction register au lieu de la coder en dur. Cela vous permet d'avoir des validations dynamiques pour vos entrées.

Maintenant, modifions `src/Form.jsx` et passons des validations dynamiques à notre composant Input personnalisé :

```jsx
export const Form = () => {
  const methods = useForm()

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
  })

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        autoComplete="off"
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input
            label="name"
            name="name"
            type="text"
            id="name"
            placeholder="type your name..."
            validation={{
              required: {
                value: true,
                message: 'required',
              },
            }}
          />
          <Input
            label="password"
            name="password"
            type="password"
            id="password"
            placeholder="type your password..."
            validation={{
              required: {
                value: true,
                message: 'required',
              },
              minLength: {
                value: 6,
                message: 'min 6 characters',
              },
            }}
          />
        </div>
        <div className="mt-5">
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}

```

Vous passez maintenant différentes validations à chaque composant Input. Cela permet à chaque Input de valider dynamiquement sa valeur en fonction de l'objet de validation fourni.

### Partie 2

Dans la section précédente, vous avez appris comment passer une validation dynamique à votre composant Input personnalisé. 

Bien que cette approche fonctionne, elle peut ne pas être efficace si vous devez utiliser le composant Input de mot de passe ou de nom à plusieurs endroits, tels que la page d'inscription, la page de connexion et la page de profil. 

Copier-coller le même code à plusieurs endroits peut entraîner des problèmes de maintenance, surtout si vous devez apporter des modifications à la logique de validation plus tard. 

Mais il existe une solution à ce problème. Vous pouvez isoler les validations d'entrée dans un objet séparé, puis passer cet objet au composant Input personnalisé en utilisant les opérateurs de propagation JavaScript. Cette approche vous permet de centraliser la logique de validation, ce qui facilite sa gestion et sa mise à jour dans toute votre application, même lorsqu'elle s'agrandit. 

Mettons à jour `src/Form.jsx` et voyons comment cela fonctionne en action : 

```jsx
export const Form = () => {
  const methods = useForm()

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
  })

  const name_validation = {
    name: 'name',
    label: 'name',
    type: 'text',
    id: 'name',
    placeholder: 'write your name ...',
    validation: {
      required: {
        value: true,
        message: 'required',
      },
      maxLength: {
        value: 30,
        message: '30 characters max',
      },
    },
  }

  const password_validation = {
    name: 'password',
    label: 'password',
    type: 'password',
    id: 'password',
    placeholder: 'type password ...',
    validation: {
      required: {
        value: true,
        message: 'required',
      },
      minLength: {
        value: 6,
        message: 'min 6 characters',
      },
    },
  }

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        autoComplete="off"
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input {...name_validation} />
          <Input {...password_validation} />
        </div>
        <div className="mt-5">
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}

```

Super ! Utiliser un objet séparé pour stocker les props et les validations d'entrée, puis les passer au composant Input personnalisé en utilisant les opérateurs de propagation peut vous aider à centraliser et gérer la logique de validation dans votre application. 

Cette approche peut faciliter la mise à jour ou la modification des validations en un seul endroit, au lieu de devoir apporter des modifications à plusieurs endroits. Elle peut également améliorer la réutilisabilité du code et réduire la duplication, surtout lorsque vous utilisez le même composant d'entrée dans différentes parties de votre application. 

Afin de garder la logique de validation d'entrée séparée du composant principal, j'ai créé un fichier de validation d'entrée dans le code de démarrage situé à `src/utils/inputValidations`. Ce fichier contient divers validateurs d'entrée prédéfinis que vous pouvez utiliser dans votre application. 

Vous pouvez facilement importer ces validateurs où vous en avez besoin et les passer au composant Input personnalisé en utilisant les opérateurs de propagation JavaScript. Cette approche permet une gestion centralisée des validations d'entrée, ce qui facilite leur mise à jour et leur réutilisation dans différentes parties de votre application. 

En tirant parti du fichier de validation d'entrée, vous pouvez garder votre code organisé, maintenable et évolutif, et assurer la cohérence de la validation d'entrée dans toute votre application. 

Modifions `src/Form.jsx` et utilisons nos validateurs personnalisés :

```jsx
export const Form = () => {
  const methods = useForm()

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
  })

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        autoComplete="off"
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input {...name_validation} />
          <Input {...email_validation} />
          <Input {...num_validation} />
          <Input {...password_validation} />
        </div>
        <div className="mt-5">
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}

```

Maintenant, votre code devient beaucoup plus propre et plus maintenable. L'un des principaux avantages est que vous pouvez maintenant facilement utiliser le même validateur d'entrée à plusieurs endroits dans votre application sans dupliquer de code. 

Cela signifie que si vous devez mettre à jour la logique de validation, vous n'avez besoin de faire des changements qu'à un seul endroit, et les changements seront appliqués partout où le validateur d'entrée est utilisé. Cela rend la gestion des validations d'entrée plus efficace et minimise le risque d'incohérences dans différentes parties de votre application. C'est une approche géniale qui favorise la réutilisabilité et l'évolutivité du code.

## Comment implémenter une fonctionnalité d'entrée multiline dans le composant d'entrée

Félicitations pour vos progrès jusqu'à présent ! Les parties difficiles étant derrière nous, nous pouvons maintenant nous concentrer sur l'ajout d'une fonctionnalité simple à notre composant Input personnalisé. Cette fonctionnalité nous permettra de gérer facilement les entrées multiline dans notre application. 

Ajoutez le code suivant à `src/components/Input.jsx` :

```jsx
export const Input = ({
  name,
  label,
  type,
  id,
  placeholder,
  validation,
  multiline,
  className,
}) => {
  const {
    register,
    formState: { errors },
  } = useFormContext()

  const inputErrors = findInputError(errors, name)
  const isInvalid = isFormInvalid(inputErrors)

  const input_tailwind =
    'p-5 font-medium rounded-md w-full border border-slate-300 placeholder:opacity-60'

  return (
    <div className={cn('flex flex-col w-full gap-2', className)}>
      <div className="flex justify-between">
        <label htmlFor={id} className="font-semibold capitalize">
          {label}
        </label>
        <AnimatePresence mode="wait" initial={false}>
          {isInvalid && (
            <InputError
              message={inputErrors.error.message}
              key={inputErrors.error.message}
            />
          )}
        </AnimatePresence>
      </div>
      {multiline ? (
        <textarea
          id={id}
          type={type}
          className={cn(input_tailwind, 'min-h-[10rem] max-h-[20rem] resize-y')}
          placeholder={placeholder}
          {...register(`${name}`, validation)}
        ></textarea>
      ) : (
        <input
          id={id}
          type={type}
          className={cn(input_tailwind)}
          placeholder={placeholder}
          {...register(name, validation)}
        />
      )}
    </div>
  )
}
```

Vous avez apporté quelques modifications au code du composant Input. Vous avez ajouté deux nouvelles props : `multiline`, qui détermine si le composant doit rendre un input ou un textarea, et `className`, qui nous permet de personnaliser le composant Input avec des classes utilitaires Tailwind personnalisées si nécessaire. 

Pour fusionner toutes les classes utilitaires ensemble, vous utilisez une bibliothèque JavaScript appelée classnames, qui fournit une syntaxe propre pour combiner plusieurs noms de classes. Maintenant, ajoutons une entrée multiline à `src/Form.jsx` :

```jsx
export const Form = () => {
  const methods = useForm()

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
  })

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        autoComplete="off"
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input {...name_validation} />
          <Input {...email_validation} />
          <Input {...num_validation} />
          <Input {...password_validation} />
          <Input {...desc_validation} className="md:col-span-2" />
        </div>
        <div className="mt-5">
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}

```

L'objet `{...desc_validation}` a `multiline` défini sur true, ce qui lui permet de rendre un textarea au lieu d'un input. De plus, vous avez passé un nom de classe personnalisé à ce composant Input particulier, garantissant qu'il occupe toujours toute la largeur. Si vous ouvrez votre serveur local, vous verrez le résultat comme suit :

![GIF illustrant une page web React avec un formulaire qui contient plusieurs champs de saisie. L'utilisateur tente de soumettre le formulaire, mais des messages d'erreur sont affichés près de certains des champs de saisie, indiquant qu'il y a des problèmes de validation avec les données saisies. Le formulaire ne peut pas être soumis tant que les erreurs ne sont pas corrigées](https://www.freecodecamp.org/news/content/images/2023/04/ezgif-1-ee09a58a83.gif)
_Aperçu de ce que nous avons construit jusqu'à présent_

Avec cela, votre composant Input est officiellement terminé ! 🎉 Vous avez réussi à créer un composant maintenable et réutilisable que vous pouvez utiliser dans vos propres applications React. 

Avant de conclure, il reste un dernier sujet à discuter : la soumission réussie du formulaire. Plongeons-nous dans ce sujet.

## Comment gérer la soumission réussie du formulaire

Dans un scénario idéal, nous aimerions afficher un message de succès lorsque la soumission du formulaire est réussie, traiter les données soumises et réinitialiser le formulaire. Dans cette section, nous allons couvrir comment gérer ces actions.

Tout d'abord, mettons à jour `src/Form.jsx` :

```jsx
export const Form = () => {
  const methods = useForm()
  const [success, setSuccess] = useState(false)

  const onSubmit = methods.handleSubmit(data => {
    console.log(data)
    methods.reset()
    setSuccess(true)
  })

  return (
    <FormProvider {...methods}>
      <form
        onSubmit={e => e.preventDefault()}
        noValidate
        autoComplete="off"
        className="container"
      >
        <div className="grid gap-5 md:grid-cols-2">
          <Input {...name_validation} />
          <Input {...email_validation} />
          <Input {...num_validation} />
          <Input {...password_validation} />
          <Input {...desc_validation} className="md:col-span-2" />
        </div>
        <div className="mt-5">
          {success && (
            <p className="flex items-center gap-1 mb-5 font-semibold text-green-500">
              <BsFillCheckSquareFill /> Form has been submitted successfully
            </p>
          )}
          <button
            onClick={onSubmit}
            className="flex items-center gap-1 p-5 font-semibold text-white bg-blue-600 rounded-md hover:bg-blue-800"
          >
            <GrMail />
            Submit Form
          </button>
        </div>
      </form>
    </FormProvider>
  )
}
```

Nous avons utilisé le hook `useState` pour créer une variable d'état appelée `success`, qui est initialement définie sur false. 

Lors de la soumission réussie du formulaire, nous mettons à jour la valeur de l'état sur true en utilisant la fonction `setSuccess`. Lorsque `success` est true, un paragraphe avec le message "Form has been submitted successfully" sera affiché. De plus, nous utilisons l'objet `methods` de la bibliothèque `react-hook-form` pour réinitialiser le formulaire en utilisant `methods.reset()` après une soumission réussie.

Nous avons également inclus une instruction console.log pour afficher les données soumises dans la console après la soumission du formulaire. Vous pouvez utiliser ces données selon vos besoins, comme les envoyer à un serveur backend, les stocker dans le stockage local, etc. 

Mais pour des raisons de simplicité dans ce tutoriel, nous nous contentons d'enregistrer les données soumises dans la console, qui seront affichées au format suivant :

![une page web React avec un formulaire, ainsi que la console Chrome ouverte et affichant les données soumises.](https://www.freecodecamp.org/news/content/images/2023/04/image-127.png)
_Capture d'écran de la soumission réussie du formulaire_

À ce stade, nous avons un formulaire entièrement fonctionnel qui inclut un composant Input personnalisé et des validations d'entrée réutilisables. Ce formulaire gère élégamment différents états de formulaire, qu'il s'agisse d'une soumission échouée ou réussie.

## Conclusion

Dans ce tutoriel, nous avons réussi à construire un formulaire maintenable et réutilisable dans React en utilisant la bibliothèque react-hook-form. Nous avons créé un composant Input personnalisé qui peut gérer divers types d'entrées avec validation. Nous avons également implémenté la gestion des erreurs pour les soumissions de formulaires échouées et affiché des messages de succès pour les soumissions réussies.

Tout au long du tutoriel, vous avez appris à utiliser react-hook-form pour gérer l'état du formulaire, gérer les soumissions de formulaires, réinitialiser les formulaires et valider les entrées de formulaires. Vous avez également tiré parti de la puissance de Tailwind CSS pour le style et la personnalisation, y compris le passage de noms de classes personnalisés à notre composant Input.

En suivant les meilleures pratiques et en exploitant les fonctionnalités de react-hook-form, vous avez été en mesure de créer un formulaire propre et efficace qui peut être facilement intégré dans n'importe quelle application React. 

Ce formulaire peut servir de base à des formulaires plus complexes avec des fonctionnalités supplémentaires, telles que l'intégration d'API backend, la persistance des données de formulaire et la validation de formulaire avec des règles personnalisées.

J'espère que ce tutoriel a été utile pour comprendre comment construire un formulaire avec react-hook-form et Tailwind CSS. N'hésitez pas à expérimenter et à étendre les fonctionnalités de ce formulaire pour répondre à vos besoins spécifiques.

Vous pouvez me suivre sur [Twitter](https://twitter.com/Yazdun) où je partage plus de conseils utiles sur le développement web. Bon codage !