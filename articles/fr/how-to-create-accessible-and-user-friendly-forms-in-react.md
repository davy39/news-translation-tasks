---
title: Comment créer des formulaires accessibles et conviviaux dans React
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-04-29T15:51:58.664Z'
originalURL: https://freecodecamp.org/news/how-to-create-accessible-and-user-friendly-forms-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745789677789/c386af23-39d6-4421-9f26-f98d75a30d61.jpeg
tags:
- name: React
  slug: reactjs
- name: Accessibility
  slug: accessibility
- name: Tutorial
  slug: tutorial
seo_title: Comment créer des formulaires accessibles et conviviaux dans React
seo_desc: When designing web applications, you’ll often be asked the age old question
  “How accessible is your website” and “Does it offer the best user experience?”.
  These are both very valid questions, but they are often overlooked in favour of
  rich or fancy ...
---

Lors de la conception d'applications web, on vous posera souvent la question éternelle : "Votre site est-il accessible ?" et "Offre-t-il la meilleure expérience utilisateur ?". Ces deux questions sont tout à fait valides, mais elles sont souvent négligées au profit de fonctionnalités riches ou sophistiquées, réduisant ainsi l'audience du site.

Dans cet article, je vais vous apprendre à utiliser la bibliothèque React Hook Form, les attributs HTML et les considérations de développement pour vous assurer que votre site est disponible pour tous, en mettant l'accent sur :

* les utilisateurs aveugles ou malvoyants, qui peuvent utiliser un lecteur d'écran

* une meilleure rétroaction utilisateur

* des indices visuels pour tous

* des considérations de conception pour tous

En suivant ce tutoriel, vous pouvez soit télécharger le code depuis le dépôt GitHub (en visitant cette [page](https://github.com/grant-dot-dev/form_accessibility_ux)), soit utiliser les extraits de code intégrés dans l'article.

### **Prérequis pour cet article :**

* Connaissance de React

* Connaissance de l'écriture de TypeScript et de HTML / JSX.

* Familiarité avec Tailwind CSS (non requis pour suivre ce tutoriel)

## Table des matières

* [Le formulaire de base initial](#heading-le-formulaire-de-base-initial)

* [Gestion des erreurs avec React-Hook-Form](#heading-gestion-des-erreurs-avec-react-hook-form)

* [Intégration des méthodes useForm à notre formulaire](#heading-integration-des-methodes-useform-a-notre-formulaire)

* [Affichage des messages d'erreur](#heading-affichage-des-messages-derreur)

* [Ajout de aria-required](#heading-ajout-de-aria-required)

* [Ajout de fieldset et legend](#heading-ajout-de-fieldset-et-legend)

* [Ajout de labels et utilisation de htmlFor](#heading-ajout-de-labels-et-utilisation-de-htmlfor)

* [Ne vous fiez pas uniquement aux placeholders !](#heading-ne-vous-fiez-pas-uniquement-aux-placeholders)

* [Donnez des informations supplémentaires avec aria-describedBy](#heading-donnez-des-informations-supplementaires-avec-aria-describedby)

* [Évitez les infobulles pour les informations critiques](#heading-evitez-les-infobulles-pour-les-informations-critiques)

* [Dites-moi quelque chose d'important](#heading-dites-moi-quelque-chose-dimportant)

* [États de focus et coloration](#heading-etats-de-focus-et-coloration)

* [Rendez les boutons descriptifs](#heading-rendez-les-boutons-descriptifs)

* [Réflexions finales](#heading-reflexions-finales)

## Le formulaire de base initial

Si nous examinons le formulaire dans son état actuel, vous pourriez penser qu'il a l'air bien. Mais en réalité, il n'est pas très accessible, ni ne propose une grande expérience utilisateur.

```typescript
import { TvIcon } from "@heroicons/react/24/outline";

type FormData = {
    fullName: string;
    email: string;
    password: string;
    confirmPassword: string;
    agreeToTerms: boolean;
};

export const RegistrationForm = () => {
    const onSubmit = () => {
        alert(`Form submitted`);
    };

    return (
        <div className="flex justify-center items-center w-screen h-screen bg-gray-900">
            <div className="w-full max-w-md p-8 bg-black bg-opacity-75 rounded-lg">
                <div className="flex flex-row justify-center items-center gap-x-4">
                    <TvIcon className="h-12 w-12 text-white" />
                    <h1 className="text-7xl font-bold text-center text-red-600 mb-4">Getflix</h1>
                </div>
                <h2 className="text-3xl font-bold text-white mb-6 text-center">
                    Sign Up
                </h2>

                <form onSubmit={onSubmit} className="space-y-6">

                    {/* Full Name */}
                    <div>
                        <input
                            type="text"
                            placeholder="Full Name"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 "
                        />

                    </div>

                    {/* Email */}
                    <div>
                        <input
                            type="email"
                            placeholder="Email Address"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 "
                        />

                    </div>

                    {/* Password */}
                    <div>
                        <input
                            type="password"
                            placeholder="Password"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400"
                        />

                    </div>

                    {/* Confirm Password */}
                    <div>
                        <input
                            type="password"
                            placeholder="Confirm Password"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 "
                        />

                    </div>

                    {/* Agree to Terms */}
                    <div className="flex items-center text-gray-400 text-sm">
                        <input

                            type="checkbox"
                            id="agreeToTerms"
                            className="mr-2"
                        />
                        <label htmlFor="agreeToTerms" className="select-none">
                            I agree to the Terms and Conditions
                        </label>
                    </div>


                    {/* Submit */}
                    <button
                        type="submit"
                        className="w-full py-3 bg-red-600 hover:bg-red-700 text-white rounded font-semibold transition"
                    >
                        Sign Up
                    </button>


                </form>
            </div>
        </div>
    );
};
```

### Qu'est-ce qui ne va pas avec le formulaire ?

* Manque de rétroaction d'action – l'absence de rétroaction utilisateur signifie que les utilisateurs peuvent être confus quant à savoir si une action a eu lieu ou non. Aucun message d'erreur ou rétroaction ne donne à l'utilisateur aucune indication sur ce qu'il doit faire pour corriger le formulaire.

* Aucune étiquette pour les entrées de formulaire – L'absence d'étiquettes pour les entrées de formulaire empêche les lecteurs d'écran de comprendre leur but. Certains lecteurs d'écran peuvent manquer les placeholders, et une fois que l'utilisateur tape dans l'entrée, le placeholder est remplacé, perdant le contexte et rendant difficile le retour aux entrées erronées.

* Manque de balisage d'accessibilité pour rendre le formulaire optimisé pour les lecteurs d'écran et les outils d'accessibilité.

Alors, comment pouvons-nous améliorer cela ? Plongeons directement dans le sujet.

## Gestion des erreurs avec React-Hook-Form

La gestion des erreurs dans les formulaires est un aspect critique de tout flux de soumission de formulaire. Sans cela, le processus devient à la fois chaotique et frustrant pour l'utilisateur. Nous pouvons atténuer cette frustration en ajoutant des messages d'erreur utiles qui expliquent les problèmes.

Une bibliothèque populaire pour travailler avec des formulaires dans React est la bibliothèque `react-hook-form`. Elle est utilisée par plus de 1,4 million de personnes selon leurs statistiques GitHub.

Allez-y et installez-la si vous ne l'avez pas déjà :

```bash
npm install react-hook-form
```

Nous allons ensuite implémenter les fonctions de base requises du package `react-hook-form`, en utilisant le hook `useForm()` comme suit :

```typescript
// définir notre structure de type à utiliser dans le formulaire
type FormData = {
    fullName: string;
    email: string;
    password: string;
    confirmPassword: string;
    agreeToTerms: boolean;
};

// utilisation de base de `useForm()`
const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
```

**Explication rapide :**

* `register` : L'un des concepts clés dans React Hook Form est d'« enregistrer » votre composant/élément HTML. Cela signifie que vous pouvez accéder à la valeur de l'élément pour la validation du formulaire et lors de la soumission du formulaire.

* `handleSubmit` : Il s'agit de la fonction clé nécessaire pour soumettre le formulaire, exécuter la validation et toute autre vérification configurée. Elle peut prendre jusqu'à deux arguments :

  1. `handleSubmit(onSuccess)` – appelé lorsque la soumission du formulaire est valide et peut être soumise correctement.

  2. `handleSubmit(onSuccess, onFail)` – ici, vous pouvez passer deux fonctions à la méthode `handleSubmit()` : la première sera exécutée lorsque React Hook Form juge le formulaire valide et vous permet de continuer. La seconde sera appelée lorsque le formulaire détecte une erreur. Cela peut provenir de la validation ou d'une autre stipulation.

* `watch` : Watch est une fonction qui surveille un élément spécifié pour les changements et retourne sa valeur. Par exemple, si vous surveillez un élément d'entrée, vous pouvez afficher la saisie de l'utilisateur en temps réel ou avoir un autre élément la valider par rapport à une valeur prédéfinie. Un bon exemple est la confirmation du mot de passe correspondant au champ de mot de passe précédent.

* `formState` : il s'agit d'un objet qui contient des informations sur votre formulaire. L'objet `formState` suit l'état du formulaire, comme :

  1. **isDirty** – `true` si l'utilisateur a modifié *n'importe quelle* entrée.

  2. **isValid** – `true` si le formulaire passe toutes les validations.

  3. **errors** – un objet contenant toute erreur de validation par champ.

  4. **isSubmitting** – `true` pendant que le formulaire est en cours de soumission (utile pour afficher des indicateurs de chargement)

  5. **isSubmitted** – `true` après que le formulaire a été soumis.

  6. **touchedFields** – quels champs l'utilisateur a interagi.

  7. **dirtyFields** – quels champs l'utilisateur a modifiés.

Nous pouvons utiliser n'importe laquelle de ces propriétés en les incluant dans notre objet d'état de formulaire. Nous déstructurons la propriété `errors` afin de pouvoir utiliser les erreurs plus tard dans notre formulaire pour afficher des messages d'erreur ou valider qu'il n'y a pas d'erreurs sur la page.

## Intégration des méthodes `useForm` à notre formulaire

Maintenant que nous en savons plus sur la méthode `useForm()` et react-hook-form, nous devons intégrer cela avec notre élément `<form/>` existant. Cela nous permettra d'utiliser toutes les fonctionnalités de react-hook-form que nous avons discutées jusqu'à présent dans notre formulaire.

```xml
import { TvIcon } from "@heroicons/react/24/outline";
import { useState } from "react";
import { useForm } from "react-hook-form";

type FormData = {
    fullName: string;
    email: string;
    password: string;
    confirmPassword: string;
    agreeToTerms: boolean;
};

export const RegistrationForm = () => {
    const {
        register,
        handleSubmit,
        formState: { errors },
        watch,
    } = useForm<FormData>();

    const onSubmit = () => {
        alert(`Form submitted`);
    };

    return (
        <div className="flex justify-center items-center w-screen h-screen bg-gray-900">
            <div className="w-full max-w-md p-8 bg-black bg-opacity-75 rounded-lg">
                <div className="flex flex-row justify-center items-center gap-x-4">
                    <TvIcon className="h-12 w-12 text-red-500" />
                    <h1 className="text-7xl font-bold text-center text-white mb-4">Getflix</h1>
                </div>
                <h2 className="text-3xl font-bold text-white mb-6 text-center">
                    Sign Up
                </h2>


                <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">

                    {/* Full Name */}
                    <div>
                        <input
                            {...register("fullName", {
                                required: "Full Name is required"
                            })}
                            aria-required
                            type="text"
                            placeholder="Full name"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500"
                        />
                        {errors.fullName && (
                            <p className="text-red-500 text-sm mt-1">{errors.fullName.message}</p>
                        )}
                    </div>

                    {/* Email */}
                    <div>
                        <input
                            {...register("email", {
                                required: "Email is required",
                                pattern: {
                                    value: /^\S+@\S+$/i,
                                    message: "Invalid email address",
                                },
                            })}
                            type="email"
                            placeholder="Email Address"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500"
                        />
                        {errors.email && (
                            <p className="text-red-500 text-sm mt-1">{errors.email.message}</p>
                        )}

                    </div>

                    {/* Password */}
                    <div>
                        <input
                            {...register("password", {
                                required: "Please enter your password",
                            })}
                            type="password"
                            placeholder="Password"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500"
                        />
                        {errors.password && (
                            <p className="text-red-500 text-sm mt-1">{errors.password.message}</p>
                        )}
                    </div>

                    {/* Confirm Password */}
                    <div>
                        <input
                            {...register("confirmPassword", {
                                required: "Please enter your password",
                                validate: (value) =>
                                    value === watch("password") || "Passwords do not match",
                            })}
                            type="password"
                            placeholder="Confirm Password"
                            className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500"
                        />
                        {errors.confirmPassword && (
                            <p className="text-red-500 text-sm mt-1">{errors.confirmPassword.message}</p>
                        )}
                    </div>

                    {/* Agree to Terms */}
                    <div className="flex items-center text-gray-400 text-sm">
                        <input
                            {...register("agreeToTerms", {
                                required: "You must agree to the terms and conditions"
                            })}
                            type="checkbox"
                            id="agreeToTerms"
                            className="mr-2"
                        />
                        <label className="select-none">
                            I agree to the Terms and Conditions
                        </label>

                    </div>
                    {errors.agreeToTerms && (
                        <p className="text-red-500 text-sm mt-1">{errors.agreeToTerms.message}</p>
                    )}


                    {/* Submit */}
                    <button
                        type="submit"
                        className="w-full py-3 bg-red-600 hover:bg-red-700 text-white rounded font-semibold transition"
                    >
                        Sign Up
                    </button>

                    {/* Already have account */}
                    <p className="text-center text-gray-400 text-sm mt-4">
                        Already have an account?{" 