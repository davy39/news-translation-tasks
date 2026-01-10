---
title: Chakra UI et React-Hook-Form – Comment créer de beaux formulaires
subtitle: ''
author: Georgey V B
co_authors: []
series: null
date: '2021-05-25T20:26:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-hook-form-with-chakra-ui
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/Blog-7-1.png
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: React
  slug: react
seo_title: Chakra UI et React-Hook-Form – Comment créer de beaux formulaires
seo_desc: 'In HTML, it’s the default behavior for forms to redirect to a new page
  whenever they''re submitted. So in order to provide dynamic functionality, React
  uses a strategy called controlled components.

  If you have recently gone through a React course, you...'
---

En HTML, le comportement par défaut des formulaires est de rediriger vers une nouvelle page lors de leur soumission. Ainsi, afin de fournir une fonctionnalité dynamique, React utilise une stratégie appelée **composants contrôlés**.

Si vous avez récemment suivi un cours sur React, vous n'avez probablement pas aimé cette partie, car il y a beaucoup d'états à gérer si vous avez plusieurs champs de saisie.

Premièrement, vous suivez l'état du champ de saisie à l'aide de la propriété `onChange` qui appelle la fonction `useState()`. Les champs de saisie sont enveloppés dans un élément de formulaire.

Lorsque l'utilisateur soumet le formulaire, cela déclenche la propriété `onClick` ou `onSubmit` pour définir les entrées soit dans un tableau contenant des valeurs, soit dans des objets, selon le nombre de champs de saisie.

Ensuite vient la validation, qui vérifie si l'utilisateur a saisi une donnée. Si ce n'est pas le cas, elle renvoie une erreur, invitant l'utilisateur à saisir une entrée valide.

La logique ici implique beaucoup de code répétitif (boilerplate). Vous pourriez vous ennuyer rien qu'en entendant parler du processus.

Et si je vous disais qu'une seule bibliothèque peut accomplir tout cela ?

Voici ce que je vais couvrir dans cet article :

1. Qu'est-ce que React-Hook-Form ?
2. Comment React-Hook-Form influence les performances
3. Comment récupérer les données utilisateur
4. Comment ajouter une validation à vos formulaires
5. Comment améliorer le front-end et l'expérience utilisateur avec Chakra-UI.

## Qu'est-ce que React-Hook-Form ?

React-Hook-Form est une bibliothèque flexible qui s'occupe de toute votre validation, de la gestion de l'état et des données utilisateur – et tout cela est contenu dans une taille de 25,3 ko (décompressé) et 9,1 ko GZip (varie selon les versions).

Elle est simple et directe à utiliser, et vous n'avez qu'à écrire un minimum de code.

![Taille du bundle selon bundlephobia.com](https://www.freecodecamp.org/news/content/images/2021/05/bundle-size.png)
_[Source de l'image](https://bundlephobia.com/result?p=react-hook-form@7.6.0)_

L'une des fonctionnalités qui m'impressionne le plus est sa performance. Comme mentionné sur son [site officiel](https://react-hook-form.com/), React-Hook-Form :

*« Minimise le nombre de re-rendus et accélère le montage, s'efforçant de fournir la meilleure expérience utilisateur possible. »*

## Comment React-Hook-Form influence les performances

Si vous avez suivi les versions précédentes de la bibliothèque, la documentation faisait souvent référence à la propriété `ref` pour gérer la gestion de l'état et la validation.

```html
<input type="password" placeholder="Password" ref={register} />
```

De cette manière, React-Hook-Form adopte une méthode de saisie **non contrôlée**, plutôt que de changer l'état à chaque fois. Il isole le composant sélectionné et évite de rendre les composants enfants.

Cela réduit considérablement le nombre de re-rendus et booste la performance globale de l'application. ([Source](https://blog.logrocket.com/the-complete-guide-to-react-hook-form/#:~:text=React%20Hook%20Form%20adopts%20the,and%20it%20has%20zero%20dependencies.))

## Comment récupérer les données utilisateur d'un formulaire

J'ai créé un Codesandbox pour ce tutoriel particulier, alors assurez-vous de vous y référer au cas où vous seriez perdu.

Voici ce dont vous aurez besoin pour suivre :
- [Lien de l'application](https://cn7hq.csb.app/)
- [Code source](https://codesandbox.io/s/funny-cartwright-cn7hq?file=/src/index.js)

Et voici ce que nous allons construire. C'est un formulaire simple avec validation, des alertes lors de la soumission et des erreurs, construit avec Chakra UI.

![Démo de ce que nous allons construire](https://www.freecodecamp.org/news/content/images/2021/05/demo.png)

Tout d'abord, installons la bibliothèque :

```bash
npm install react-hook-form
```

Maintenant, importez le hook `useForm` du package :

```js
import { useForm } from "react-hook-form";
```

Déstructurez les constantes suivantes du hook `useForm` :

```js
const { register, handleSubmit, formState: { errors } } = useForm();
```

Créez un élément de formulaire simple comme ceci :

```js
<form onSubmit={handleSubmit(onSubmit)}>
	<input type="text" placeholder="First Name" {...register("firstname")} />
	<input type="submit" />
</form>
```

Lors de la soumission, le formulaire passera une fonction à la fonction `handleSubmit`. Nous pouvons définir la fonction `onSubmit` comme ceci :

```js
const onSubmit = data => console.log(data);
```

Maintenant, si nous testons notre élément de formulaire, lorsqu'il est soumis, la console renvoie ce qui suit :

![Aperçu du log de la console Codesandbox](https://www.freecodecamp.org/news/content/images/2021/05/log-2.png)

Il semble qu'il ait renvoyé un objet avec la propriété `firstname` et qu'il ait réussi à récupérer les données du champ de saisie.

Ajoutons maintenant d'autres champs de saisie :
```js
<form onSubmit={handleSubmit(onSubmit)}>
	<input type="text" placeholder="First Name" {...register("firstname")} />
	<input type="text" placeholder="Last Name" {...register("lastname")} />
	<input type="password" placeholder="Your password" {...register("password")} />
	<input type="submit" />
</form>
```

En affichant la réponse, nous recevons un objet :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Surface-Pro-3---1.png)

Maintenant, ces données peuvent être envoyées à la base de données. Mais dans ce tutoriel, affichons-les simplement à l'utilisateur en utilisant `useState()`.

```js
const [data, setData] = useState();
const onSubmit = (data) => {
   setData(data);
 };
```

Créons un nouveau composant appelé `Stats.js`. Ici, nous utiliserons le composant `Stat` de Chakra UI.

```js
import {
 HStack,
 Stack,
 Stat,
 StatHelpText,
 StatLabel
} from "@chakra-ui/react";
import React from "react";
 
export default function Stats(props) {
 return (
   <Stat mt={5}>
     <Stack
       p={4}
       borderWidth="3px"
       borderRadius="md"
       direction="column"
       align="flex-start"
     >
       <HStack>
         <StatLabel>Nom : {props.Firstname}</StatLabel>
         <StatLabel>{props.Lastname}</StatLabel>
       </HStack>
       <StatHelpText>Mot de passe : {props.Password}</StatHelpText>
     </Stack>
   </Stat>
 );
}
```

Maintenant, importez ce composant dans votre fichier racine et passez les props respectives.

```js
import Stats from "./Stats";
// App.js
{data && (
       <Stats
         Firstname={data.firstname}
         Lastname={data.lastname}
         Password={data.password}
       />
)}
```

Les statistiques ne seront affichées que si `data` est vrai.

Le résultat final devrait ressembler à ceci :

![Résultat affiché sur le front-end](https://www.freecodecamp.org/news/content/images/2021/05/Surface-Pro-4---1.png)

## Comment ajouter une validation à un formulaire

Pourquoi avons-nous besoin de validation de toute façon ? Laissez-moi vous donner un exemple que j'ai rencontré lors d'un des projets de hackathon sur lesquels je travaillais.

J'avais construit un gestionnaire de mots de passe et je n'avais prêté aucune attention à la validation du formulaire. Les utilisateurs ont commencé à saisir des mots de passe vides. Finalement, il y avait une tonne de données invalides dans la base de données.

Maintenant, si vous visitez n'importe quel site populaire, vous avez peut-être remarqué qu'il vous oblige à saisir un mot de passe fort.

Tracons quelques conclusions de cette étude de cas :
- Nous voulons obtenir des données valides
- Nous voulons que nos données utilisateur soient protégées en saisissant des mots de passe forts
- Nous voulons garder la base de données propre en bloquant les données invalides

Nous allons essayer d'atteindre ces objectifs en utilisant la validation côté client fournie par React-Hook-Form. Nous utiliserons la méthode `register` fournie par la bibliothèque. Elle vous permet d'enregistrer les données qu'un utilisateur saisit et d'y appliquer des règles de validation.

Considérez l'exemple ci-dessous :
```js
<input
      type="text"
      placeholder="First name"
      {...register("firstname", { required: true })}
/>
```

En définissant la règle `required` sur `true`, l'utilisateur sera désormais obligé de fournir une chaîne de caractères pour passer la validation. Nous pouvons modifier cela davantage en renvoyant un message à l'utilisateur lorsque cet événement se produit.

```js
<input
      type="text"
      placeholder="First name"
      {...register("firstname", { required: "Veuillez entrer votre prénom" })}
/>
{errors.firstname && <p>{errors.firstname.message}</p>}
```

Si l'objet `errors` renvoie une valeur vraie, il affichera le message à l'utilisateur.

Forçons maintenant l'utilisateur à fournir un mot de passe de plus de 8 caractères.
```js
<Input
      type="password"
      placeholder="Password"
      {...register("password", {
        required: "Veuillez entrer un mot de passe",
        minLength: { value: 8, message: "Trop court" }
      })}
 />
```

En assignant la propriété `minLength` à 8, l'utilisateur sera désormais contraint de saisir un mot de passe de 8 caractères.

De plus, nous pouvons alerter l'utilisateur sur le front-end en utilisant la même méthode que précédemment avec l'opérateur `&&`.

```js
{errors.password && <p>{errors.password.message}</p>}
```

Si vous remarquez bien, React-Hook-Form écoute les changements de manière dynamique. Ainsi, si le champ est laissé vide, il affiche une alerte instantanément. Si le mot de passe est trop court, il met à jour le message dynamiquement. C'est beau !

Maintenant, allez-y et créez votre propre formulaire. Dans la section suivante, nous allons personnaliser le formulaire et envoyer des alertes à l'utilisateur lorsqu'une erreur survient.

## Comment améliorer le front-end et l'expérience utilisateur avec Chakra-UI

Tout d'abord, convertissons tous les composants que nous avons utilisés jusqu'à présent en composants Chakra UI.

Au lieu du `<input />` normal, remplacez simplement l'existant par le composant `Input` de Chakra UI.

```js
import { Input } from "@chakra-ui/react"
```

Maintenant, importez les composants `VStack` et `Button` de la même manière et enveloppez tout le formulaire avec `VStack`.

```js
<VStack>
         <Input
           type="text"
           placeholder="First name"
           {...register("firstname", {
             required: "Veuillez entrer votre prénom",
             minLength: 3,
             maxLength: 80
           })}
         />
         <Input
           type="text"
           placeholder="Last name"
           {...register("lastname", {
             required: "Veuillez entrer votre nom",
             minLength: 3,
             maxLength: 100
           })}
         />
         <Input
           type="password"
           placeholder="Password"
           {...register("password", {
             required: "Veuillez entrer un mot de passe",
             minLength: { value: 8, message: "Too short" }
           })}
         />
         <Button
           borderRadius="md"
           bg="cyan.600"
           _hover={{ bg: "cyan.200" }}
           variant="ghost"
           type="submit"
         >
           Submit
         </Button>
</VStack>
```

Les props que vous voyez pour le composant `Button` sont similaires aux propriétés CSS, donc migrer vers Chakra UI ne sera pas un problème.

Maintenant, donnons des alertes instantanées à l'utilisateur lorsqu'il saisit des données invalides.

Créez un nouveau composant `AlertPop.js`.

Importez le code suivant :
```js
import { Alert, AlertIcon, AlertTitle } from "@chakra-ui/react";
```

Définissons une prop pour afficher le message d'erreur.

```js
export default function AlertPop (props) {
 return (
   <Alert status="error">
     <AlertIcon />
     <AlertTitle mr={2}>{props.title}</AlertTitle>
   </Alert>
 );
}
```

Maintenant, importez ce composant dans le fichier racine, et sous chaque champ de saisie, tapez la logique ci-dessous :

```js
{errors.firstname && <AlertPop title={errors.firstname.message} />}
{errors.lastname && <AlertPop title={errors.lastname.message} />}
{errors.password && <AlertPop title={errors.password.message} />}
```

Enfin, importez `useToast` comme ceci :
```js
import { useToast } from "@chakra-ui/react"
```

En utilisant ce composant, nous pourrons afficher un message contextuel (pop-up) lorsque l'utilisateur soumet avec succès le formulaire.

Voici comment nous allons procéder :
```js
import { useToast } from "@chakra-ui/react"

const toast = useToast()
const onSubmit = (data) => {
   //console.log(data);
   toast({
     title: "Soumis !",
     status: "success",
     duration: 3000,
     isClosable: true
   });
 
   setData(data);
 };
```

Le résultat final devrait ressembler à ceci :

![Composant Toast en action](https://www.freecodecamp.org/news/content/images/2021/05/submit.png)

## Conclusion

La technologie web progresse chaque jour, à un rythme très rapide. Il est bon d'apprendre à utiliser diverses bibliothèques, mais assurez-vous d'abord d'en comprendre les bases.

Par exemple, vous ne pouvez pas commencer à apprendre ReactJS tout d'un coup sans comprendre la manipulation du DOM. Les bases sont les fondations, sinon vous ne pourrez pas comprendre la beauté du fonctionnement du web.

## Merci de m'avoir lu ! ✨

C'est un plaisir de voir que vous avez lu jusqu'ici. Si vous avez tiré des enseignements de cet article, n'hésitez pas à le partager avec votre communauté et vos collègues.

Je parle de technologies web et je construis des projets, en documentant ensuite le processus de développement pour que d'autres développeurs puissent s'y référer. Si vous avez besoin de conseils, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/BrodasGeo).