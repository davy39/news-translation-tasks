---
title: Comment valider des formulaires dans React et React Native en utilisant Yup
  et Formik
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-06-24T19:51:14.000Z'
originalURL: https://freecodecamp.org/news/react-how-to-validate-user-input
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/1080_Template.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: Comment valider des formulaires dans React et React Native en utilisant
  Yup et Formik
seo_desc: 'Validation is a key part of development, regardless of what programming
  language you’re writing. Developers should always be validating user input, API
  parameters, and retrieved values.

  One of the most common elements where you’ll need to apply user ...'
---

La validation est une partie clé du développement, quel que soit le langage de programmation que vous utilisez. Les développeurs doivent toujours valider les entrées utilisateur, les paramètres d'API et les valeurs récupérées.

L'un des éléments les plus courants où vous devrez appliquer la validation des entrées utilisateur est via un formulaire. Cela pourrait être un formulaire d'inscription utilisateur, un formulaire de contact ou un simple questionnaire.

## Résultats du tutoriel

À la fin de cet article, vous serez capable de :

* Comprendre les problèmes courants avec la validation de formulaires.
* Comment utiliser la bibliothèque de validation de schéma Yup avec la bibliothèque de formulaires Formik.
* Comment construire un formulaire dans React avec une validation complète (les mêmes principes s'appliquent pour React Native, avec une syntaxe de composant différente).

## Contenu

* [Qu'est-ce que la validation](#heading-quest-ce-que-la-validation) ?
* [L'objet à valider](#heading-lobjet-a-valider)
* [Présentation de Yup et Formik](#heading-presentation-de-yup-et-formik)
* [Comment ajouter la validation à un formulaire](#heading-comment-ajouter-la-validation-a-un-formulaire)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que la validation ?

La validation est définie comme :

> _l'action de vérifier ou de prouver la validité ou l'exactitude de quelque chose._

Mais que signifie cela en langage informatique ? Cela pourrait être une multitude de choses, mais le principe reste le même. Vous pourriez valider une valeur de variable ou un objet par rapport à un ensemble de règles ou de réglementations prédéterminées.

Des exemples de règles de validation pourraient être :

* Le mot de passe doit comporter au moins 8 caractères et contenir un caractère spécial.
* Le nom d'utilisateur doit être unique.
* La date de naissance doit être reçue sous forme de chaîne, dans un format particulier, par exemple ISO8601.

Prenons l'exemple d'un formulaire d'inscription utilisateur sur un site web.

## L'objet à valider

Le formulaire comprendra plusieurs entrées pour former un objet `UserRegistration`. Comme ceci :

```ts
interface UserRegistration {
  firstName: string;
  surname: string;
  email: string;
  dob: string;
}

```

Ci-dessus se trouve une interface (contrat) pour un objet `UserRegistration`. Elle définit simplement certaines informations clés sur l'utilisateur qui doivent être collectées, avec toutes les valeurs étant de type `string`.

Bien que des langages comme TypeScript soient utiles pour garantir que nous passons les types corrects aux fonctions dans notre application, ils ne valident pas intrinsèquement le contenu ou les valeurs réels de ces types. TypeScript garantit qu'une variable est d'un type spécifique, comme une chaîne ou un nombre, mais il ne vérifie pas si le contenu de cette chaîne ou de ce nombre répond à des critères ou des contraintes spécifiques.

### Que se passe-t-il si nous ne validons pas les valeurs ?

Avant de passer à la validation, examinons ce qui pourrait se passer si nous ne validons pas.

Sans validation, un utilisateur pourrait saisir les valeurs suivantes :

**Prénom** : 1231301  
**Nom** : Hello##test_101  
**Email** : user_123@@email.to@.com  
**Date de naissance** : 10+12+1909

Ces valeurs peuvent **sembler** parfaitement acceptables, et votre front-end peut les autoriser à être soumises sans aucun problème. Et l'API les acceptera probablement initialement.

Mais lorsque l'API tente d'analyser ces valeurs (conversion) lors du traitement de la demande, elle rencontrera des erreurs et ne parviendra pas à traiter la demande correctement.

Il y a plusieurs conséquences négatives à cette approche :

1. **Charge serveur accrue** : Le front-end effectue plusieurs demandes invalides au serveur, ce qui sollicite inutilement le serveur. Cette charge supplémentaire aurait pu être évitée.
2. **Coûts potentiellement plus élevés** : Le coût de traitement de ces demandes invalides peut augmenter considérablement, selon votre plan d'hébergement et la configuration du serveur. Chaque demande invalide consomme des ressources serveur qui pourraient être utilisées plus efficacement.
3. **Mauvaise expérience utilisateur (UX)** : Les utilisateurs risquent de devenir frustrés s'ils saisissent à plusieurs reprises des détails, soumettent le formulaire, puis reçoivent des messages d'erreur indiquant que leurs entrées sont invalides. Cela peut conduire à une perception négative de l'application.

Pour atténuer ces problèmes et réduire le nombre de demandes invalides, nous pouvons implémenter une 'validation côté client' pour nous assurer que les données répondent aux critères requis avant d'envoyer la demande à l'API.

## Présentation de Yup et Formik

Yup et Formik sont deux bibliothèques que vous pouvez ajouter à toute application React ou React Native via npm ou yarn.

Yup est une bibliothèque de construction de schémas qui vous permet de créer des schémas pour la validation à l'exécution. Elle dispose d'une multitude de fonctions d'extension qui peuvent définir des ensembles de règles, transformer des valeurs et retourner des messages de validation directement.

Examinons un exemple de schéma Yup pour notre formulaire utilisateur :

```ts
import * as Yup from 'yup';

// Si vous utilisez TypeScript, vous pouvez utiliser une fonction wrapper pour imposer un typage strict

const createYupSchema = <T extends object>(schema: Yup.ObjectSchema<T>): Yup.ObjectSchema<T> => schema;

export const userFormSchema = createYupSchema<UserInput>(
  Yup.object().shape({
    firstname: Yup.string().required('Le prénom est requis'),
    surname: Yup.string().required('Le nom est requis'),
    email: Yup.string().email('Format d\'email invalide').required('L\'email est requis'),
    dob: Yup.string().required('La date de naissance est requise'),
  })
);

// Version JS
export const validationSchema = Yup.object({
  firstname: Yup.string().required('Le prénom est requis'),

  surname: Yup.string().required('Le nom est requis'),
  email: Yup.string().email('Format d\'email invalide').required('L\'email est requis'),
  dob: Yup.date().required('La date de naissance est requise')
});
```

Nous créons un objet Yup (schéma) qui contient toutes nos clés pour notre interface UserInput.

### Parties du schéma :

* clé : la clé qui sera utilisée plus tard pour le nom de notre élément (comme nous utilisons TypeScript, cela doit correspondre au nom de la clé de l'objet).
* ensemble de règles : pour toutes les clés, appliquer un ensemble de règles. Un ensemble de règles doit commencer par une déclaration de typage, c'est-à-dire `Yup.string()` ou `Yup.number()` et ainsi de suite. Vous pouvez ensuite enchaîner vos autres fonctions de validation.

L'utilisation de TypeScript garantit que nous faisons correspondre le type de schéma à nos types d'interface.

Par exemple, si nous essayons de faire ceci :

```ts
firstname: Yup.date().required();
```

cela générera une erreur TypeScript se plaignant que `firstname` ne peut pas être validé comme s'il s'agissait d'une date, car le type de firstname est une `string`.

### Comment ajouter la validation à un formulaire

C'est là que notre bibliothèque Formik intervient et rend les choses beaucoup plus faciles que la validation d'un formulaire et la mise en œuvre de la gestion des erreurs manuellement.

Formik est une bibliothèque qui encapsule un composant `<Form/>`. Elle nous permet de créer des formulaires plus riches dans React et React Native, nous donnant accès à des fonctionnalités comme l'état du formulaire, la gestion des erreurs, la validation et le traitement des soumissions de formulaires beaucoup plus efficacement.

Vous pouvez accéder à une version pré-construite d'un UserForm utilisant Yup, Formik et React (Vite) sur mon GitHub [ici](https://github.com/grant-dot-dev/fcc-yup-schema-validation). Il suffit de cloner le dépôt GitHub et de suivre les instructions du README.md.

```tsx
<Formik
        initialValues={initialValues}
        validationSchema={userFormSchema}
        onSubmit={onSubmit}
      >
        {({ isValid, dirty, isSubmitting }) => (
          <Form>
            <div className="form-control">
              <label htmlFor="firstName">Prénom</label>
              <Field type="text" id="firstName" name="firstName" />
              <ErrorMessage name="firstName" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="surname">Nom</label>
              <Field type="text" id="surname" name="surname" />
              <ErrorMessage name="surname" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="email">Email</label>
              <Field type="email" id="email" name="email" />
              <ErrorMessage name="email" component="div" className="error" />
            </div>

            <div className="form-control">
              <label htmlFor="dob">Date de naissance</label>
              <Field type="date" id="dob" name="dob" />
              <ErrorMessage name="dob" component="div" className="error" />
            </div>

            <button type="submit" disabled={isSubmitting || !isValid}>Soumettre</button>
          </Form>
        )}
      </Formik>
```

Dans ce code, nous avons utilisé le composant de bibliothèque `<Formik/>`, qui enveloppe notre élément `<Form/>` standard. Nous passons les propriétés suivantes au composant :

* `**initialValues**` – ce sont les valeurs initiales requises de votre formulaire (c'est-à-dire lorsque le formulaire est rendu, quelles valeurs vos entrées auront). 
* **`validationSchema`** – c'est probablement le plus important pour ce tutoriel. Gardez à l'esprit que c'est une propriété optionnelle, car elle n'est pas nécessaire pour utiliser le composant `<Formik/>`, mais pour toute validation, elle l'est.  
  
Nous allons importer notre `userFormSchema` que nous avons créé dans l'étape précédente. Cela va dire au formulaire, lors de la validation des entrées dans ce formulaire, d'utiliser ces schémas.
* **`onSubmit`** – une fonction simple à exécuter lors du clic sur votre bouton / soumission du formulaire. Les valeurs du formulaire seront automatiquement passées à cette fonction.

Vous pouvez envelopper le formulaire dans une fonction "render prop" pour utiliser certaines des propriétés exposées par Formik dans votre formulaire. Vous pouvez en apprendre davantage sur les render props [ici](https://legacy.reactjs.org/docs/render-props.html).

```tsx
{({ isValid, isSubmitting }) => (
```

**Note :** Cela n'est pas requis si vous ne souhaitez pas utiliser les propriétés sous-jacentes de Formik dans le formulaire lui-même. Vous pouvez simplement supprimer et placer votre balise d'ouverture `<Form>` à sa place.  
  
Mais l'utilisation de cette render prop vous permet d'accéder aux propriétés exposées par le composant Formik dans votre élément `<Form/>`. Vous pouvez voir que nous utilisons les propriétés `isValid` et `isSubmitting` pour contrôler l'état de notre bouton de soumission.

En continuant avec l'analyse du code :

* `**isValid**` – une valeur booléenne que Formik contrôle en fonction du résultat de la validation de notre schéma.
* `**isSubmitting**` – Un indicateur booléen indiquant si un formulaire est en cours de soumission. Cet indicateur est très utile lorsque vous souhaitez désactiver un bouton, pour éviter plusieurs clics signifiant plusieurs soumissions du formulaire.

Nous pouvons utiliser ces valeurs pour contrôler l'activation du bouton de soumission comme suit :

```tsx
<button type="submit" disabled={isSubmitting || !isValid}>Soumettre</button>
```

### Champs de saisie

Il est important de noter que lors de l'utilisation de Formik et Yup, pour que la validation fonctionne, les noms des champs de saisie doivent correspondre exactement aux clés du schéma Yup (sensible à la casse) – sinon les règles de validation ne seront pas enregistrées.

**Exemple :**

```tsx
<Field type="email" id="email" name="email" />
<ErrorMessage name="email" component="div" className="error" />
```

Nous avons défini ce champ pour être utilisé pour une saisie d'email, et lui avons donné le `name` correspondant "email" à notre définition de userFormSchema.

En dessous, nous codons notre composant Formik `<ErrorMessage/>`, en passant à nouveau le nom '_email_', correspondant à notre schéma. En utilisant la propriété name, nous sommes capables de lier notre saisie, message d'erreur et schémas de validation ensemble.

Si des problèmes surviennent lors de la validation du champ de saisie, le message d'erreur affichera les messages d'erreur définis – sinon, il reviendra à un message par défaut, par exemple "_firstname est un champ requis_". Cela peut être moins convivial, donc je recommande toujours de passer un message personnalisé.

Vous remarquerez également que lorsque nous perdons le focus ou lors de la frappe (après que la première validation a été exécutée), elle exécutera automatiquement la validation à nouveau. Vous pouvez remplacer cette fonctionnalité en définissant les indicateurs `validateOnBlur` et `validateOnChange` (true / false).

Par exemple, cela ressemblera à ceci dans son état d'erreur :

![Image : Formulaire Formik invalide montrant l'état d'erreur](https://www.freecodecamp.org/news/content/images/2024/06/image-100.png)
_Image : Formulaire Formik invalide montrant l'état d'erreur_

Une fois que nous avons saisi des valeurs pour toutes les entrées et que notre validation a réussi (vous pouvez voir que le bouton de soumission est maintenant activé), nous pouvons soumettre.

![Image : Formulaire Formik valide montrant l'état valide](https://www.freecodecamp.org/news/content/images/2024/06/image-95.png)
_<div id="ember289" class="miw-100 tc bn form-text bg-transparent pr8 pl8 ember-view" data-kg-has-link-toolbar="true" data-koenig-dnd-disabled="true" style="box-sizing: border-box; padding-right: 3.2rem; padding-left: 3.2rem; border-style: none; border-width: 0px; transition: border-color 0.15s linear 0s; appearance: none; outline: none; min-width: 100%; background-color: transparent !important; text-align: center;"><div class="koenig-basic-html-input__editor-wrappper" style="box-sizing: border-box; cursor: text;"><div class="koenig-basic-html-input__editor __mobiledoc-editor" data-gramm="false" data-kg="editor" data-kg-allow-clickthrough="" data-placeholder="Type caption for image (optional)" spellcheck="true" contenteditable="true" style="box-sizing: border-box; position: relative; resize: none; min-height: 1em;"><p style="box-sizing: border-box; margin: 0px; position: relative; min-width: 100%; max-width: 100%; font-family: inherit; font-weight: inherit; line-height: inherit; font-size: inherit; letter-spacing: inherit;">Image : Formulaire utilisateur valide avec bouton de soumission activé</p></div></div></div>_

### Validation supplémentaire et fonctionnalités de Formik 

Vous avez maintenant vu à quel point Yup et Formik peuvent faciliter la création d'un formulaire. Il dispose d'une validation complète et même d'une gestion des erreurs, ce qui signifie que vous pouvez avoir un formulaire entièrement fonctionnel et convivial construit en quelques minutes.

Mais que se passe-t-il si vous souhaitez ajouter une validation plus complexe à un formulaire beaucoup plus grand / compliqué ? Eh bien, examinons un exemple :

Supposons que nous voulons valider que la date de naissance fournie garantit que l'utilisateur a plus de 18 ans. Nous ajouterons également un champ de mot de passe, qui aura les règles suivantes :

* minimum de 6 lettres
* contenir un nombre
* contenir un caractère spécial

#### Exigences supplémentaires pour la date de naissance

Nous pouvons faire cela en enchaînant la fonction `test()` à la fonction `string()` de l'objet dob dans notre schéma.

La fonction `test()` nous permet de tester une logique personnalisée. Mettez à jour le paramètre `dob` dans le userFormSchema comme suit :

```ts
dob: Yup.string()
      .required('La date de naissance est requise')
      .test('is-older-than-18', 'Vous devez avoir au moins 18 ans', (value) => {
        if (!value) return false;

        // essayer d'analyser la valeur en date
        const parsedDate = parse(value, 'yyyy-MM-dd', new Date());
        if (!isValid(parsedDate)) return false;

        const today = new Date();
        const eighteenYearsAgo = subYears(today, 18);

        // vérifier si la date fournie est antérieure ou identique à il y a 18 ans.
        return parsedDate <= eighteenYearsAgo;
      })
```

Nous obtenons maintenant l'erreur suivante lorsque nous essayons de soumettre une date qui est inférieure à 18 ans.

![Image montrant un champ de saisie de date invalide en raison d'une validation de date échouée](https://www.freecodecamp.org/news/content/images/2024/06/image-99.png)
_Image : Champ de saisie invalide en raison d'une validation de date échouée_

#### Validation du mot de passe

Pour la validation du champ de mot de passe, nous pouvons faire quelque chose comme ceci :

```ts
password: Yup.string()
    .required('Ce champ est requis')
    .min(6, 'Doit comporter au moins 6 caractères')
    .matches(/[!@#$%^&*(),.?":{}|<>]/, 'Doit contenir au moins un caractère spécial')
    .matches(/\d/, 'Doit contenir au moins un nombre');
```

Ici, nous utilisons la fonction `matches()`, en passant une expression régulière à vérifier. Vous pourriez combiner ces cas en une seule expression régulière, mais l'avantage de les garder séparés est qu'il permet de pointer quelle règle de validation échoue. Cela permet également un message d'erreur plus granulaire et une maintenance si les règles changent à l'avenir.

### Autres méthodes utiles :

* `length()` – vérifie la longueur de la chaîne / du nombre
* `positive()` – vérifie que le type de nombre est un nombre positif
* `email()` – vérifie qu'il s'agit d'une adresse email valide
* `url()` – vérifie qu'il s'agit d'une URL valide
* `min()` / `max()` – vérifie que le nombre est au moins 'x' et inférieur à 'y'
* `ensure()` – transforme les valeurs `undefined` et `null` en une chaîne vide tout en définissant la valeur `default` à une chaîne vide.

## Conclusion

Comme vous pouvez le voir, les possibilités avec Yup sont vastes. Combinez cela avec la bibliothèque Formik, et vous pouvez avoir des formulaires riches, efficaces et faciles à utiliser.

Cette facilité d'utilisation permet de mettre en place un formulaire beaucoup plus rapidement sur votre application web ou mobile, vous permettant de vous concentrer sur l'expérience utilisateur, le design et la logique métier.

Comme toujours, n'hésitez pas à me contacter et à discuter de cet article avec moi sur [Twitter](https://x.com/grantdotdev), et n'oubliez pas de me suivre pour entendre parler des futurs articles et conseils de développement.