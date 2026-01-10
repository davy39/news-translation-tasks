---
title: Comment passer des arguments supplémentaires aux actions serveur de Next.js
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-10-22T19:32:56.256Z'
originalURL: https://freecodecamp.org/news/how-to-pass-additional-arguments-to-nextjs-server-actions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729165969570/14ca2ef4-8a08-40f8-ba70-c6c24c194850.png
tags:
- name: React
  slug: reactjs
- name: Next.js
  slug: nextjs
- name: server actions
  slug: server-actions
- name: Beginner Developers
  slug: beginners
- name: JavaScript
  slug: javascript
seo_title: Comment passer des arguments supplémentaires aux actions serveur de Next.js
seo_desc: Asynchronous data mutation and handling is a necessary task in modern web
  applications. You may want to execute a standalone asynchronous function on the
  server to carryout tasks like saving data to the data store, sending emails, downloading
  PDFs, p...
---

La mutation et la gestion des données asynchrones sont des tâches nécessaires dans les applications web modernes. Vous pouvez souhaiter exécuter une fonction asynchrone autonome sur le serveur pour effectuer des tâches comme sauvegarder des données dans le stockage de données, envoyer des emails, télécharger des PDF, traiter des images, etc.

Next.js nous fournit des `Server Actions` qui sont des fonctions asynchrones exécutées sur le serveur. Nous pouvons utiliser les actions serveur pour les mutations de données sur le serveur, mais les actions serveur peuvent être invoquées à partir de composants serveur et client.

Les actions serveur sont un excellent moyen de gérer les soumissions de formulaires en exécutant l'action lorsque les données du formulaire sont soumises. Dans cet article, nous examinerons un cas d'utilisation pratique de la gestion d'arguments supplémentaires dans les actions serveur de Next.js.

Si vous êtes intéressé par l'apprentissage des actions serveur de Next.js avec des modèles de conception et la construction de projets, j'ai créé un cours accéléré pour vous que vous pouvez trouver [ici](https://www.youtube.com/watch?v=gQ2bVQPFS4U).

De plus, cet article est également disponible sous forme de tutoriel vidéo ici :

%[https://www.youtube.com/watch?v=9PBtj0sUc7Q]

## Table des matières

1. [Pourquoi auriez-vous besoin de passer des arguments supplémentaires ?](#heading-pourquoi-auriez-vous-besoin-de-passer-des-arguments-supplementaires)

2. [Un formulaire avec une action serveur](#heading-un-formulaire-avec-une-action-serveur)

3. [Comment passer des arguments supplémentaires](#heading-comment-passer-des-arguments-supplementaires)

4. [Qu'en est-il des champs cachés ?](#heading-quen-est-il-des-champs-caches)

5. [Ressources](#heading-ressources)

## Pourquoi auriez-vous besoin de passer des arguments supplémentaires ?

Lorsque nous exécutons une action serveur lors de la soumission d'un formulaire, l'action serveur obtient automatiquement les données du formulaire. Par exemple, regardez le formulaire ci-dessous :

```xml
<form className="p-4 flex" action={updateUser}>
  <Input className="w-1/2 mx-2" type="text" name="name" />
  <Button type="submit">Mettre à jour le nom de l'utilisateur</Button>
</form>
```

Ici, nous exécutons une action serveur appelée `updateUser` lorsque le formulaire est soumis. La fonction `updateUser` recevra les données du formulaire soumises en tant qu'argument qui peut être utilisé pour extraire les valeurs des champs du formulaire.

Comme vous le voyez dans l'extrait de code ci-dessous, la fonction `updateUser` reçoit un `formData` en tant qu'argument, et nous pouvons extraire la valeur du champ `name` de celui-ci.

```javascript
"use server"

export async function updateUser(formData) {
  const name = formData.get('name');
  console.log(name);
}
```

Bien que ce modèle couvre la plupart des cas d'utilisation de base, vous pouvez avoir besoin de passer des arguments supplémentaires de manière programmatique aux actions serveur. Ces arguments ne font pas partie du formulaire ou des données du formulaire ou des données d'entrée de l'utilisateur. Ils peuvent être des valeurs passées de manière programmatique à votre action serveur.

Pour comprendre cela, vérifiez l'extrait de code de l'action serveur ci-dessous. C'est la même action serveur que nous avons vue précédemment, mais nous avons passé un argument `userId` supplémentaire ainsi que l'argument `formData` régulier.

```javascript
"use server"

export async function updateUser(userId, formData) {
  const name = formData.get('name');
  console.log(userId);
  console.log(name);
}
```

La valeur `userId` est quelque chose d'interne à l'application - et vous ne demanderiez pas à un utilisateur de soumettre la valeur dans le cadre de la soumission du formulaire. Plutôt, vous pouvez avoir besoin de la passer de manière programmatique à votre action serveur pour effectuer des calculs supplémentaires.

Bien, c'est le cas d'utilisation dont nous parlons. Maintenant que nous comprenons pourquoi nous en avons besoin, comprenons comment l'atteindre. Mais d'abord, créons un formulaire et une action serveur fonctionnelle pour celui-ci.

## Un formulaire avec une action serveur

Créez un répertoire appelé `actions` sous le répertoire `app` de votre application Next.js. Créez maintenant un fichier `user.js` sous le dossier `actions` avec le code suivant :

```javascript
"use server"

export async function updateUser(formData) {
  const name = formData.get('name');
  console.log(name);

  // Faites ce que vous voulez avec le nom, sauvegardez-le dans la base de données, créez une facture, peu importe !
}
```

Voici comment vous créez une fonction serveur dans Next.js. Elle doit avoir une directive `"use server"` en haut du fichier pour indiquer à Next.js que ce fichier est un fichier spécial avec une ou plusieurs fonctions asynchrones à exécuter sur le serveur.

Ensuite, nous avons l'action serveur (la fonction asynchrone) `updateUser` avec `formData` comme argument. À l'intérieur de la définition de la fonction, nous extrayons la valeur `name` et l'affichons sur la console.

Attachons maintenant cette action serveur à un formulaire. Pour ce faire, créez un dossier appelé `components` sous le dossier racine du projet. Créez un fichier appelé `user-form.jsx` avec le code suivant :

```javascript
import { Input } from "./ui/input"
import { Button } from "./ui/button"

import { updateUser } from "@/app/actions/user"

const UserForm = () => {
  return(
    <form className="p-4 flex" action={updateUser}>
      <Input className="w-1/2 mx-2" type="text" name="name" />
      <Button type="submit">Mettre à jour le nom de l'utilisateur</Button>
    </form>
  )
}

export default UserForm;
```

Il s'agit d'un simple composant React avec un formulaire. Le formulaire a un champ de texte d'entrée appelé `name` et un bouton de soumission pour soumettre le formulaire. Le formulaire a un attribut `action` avec l'action serveur `updateUser` comme valeur. Maintenant, lorsque le formulaire est soumis avec une valeur `name`, l'action serveur la recevra dans le cadre des données du formulaire comme nous l'avons discuté ci-dessus.

Testons cela. Pour ce faire, nous allons créer une route et une page Next.js où nous pouvons utiliser le composant `UserForm`. Créez un dossier appelé `extra-args` sous le répertoire `app`. Maintenant, créez un fichier appelé `page.js` sous le répertoire `app/extra-args` avec le code suivant :

```javascript
import UserForm from "@/components/user-form";

const ExtraArgsDemo = () => {
  return (
    <UserForm />
  )
}

export default ExtraArgsDemo;
```

Il s'agit d'un simple composant React où nous avons importé le composant `UserForm` et l'avons utilisé dans le JSX. Maintenant, exécutez le serveur local et accédez à cette route `localhost:3000/extra-args`. Vous devriez voir le formulaire avec un champ de texte et un bouton.

Tapez du texte à l'intérieur du champ de texte et cliquez sur le bouton.

![Application avec actions serveur](https://cdn.hashnode.com/res/hashnode/image/upload/v1729167845597/b4c58399-4188-4b89-8ec7-dd2602c10ccd.png align="center")

Maintenant, vous pourrez voir que le texte tapé a été imprimé sur la console du serveur. Pourquoi sur la console du serveur ? Pourquoi pas sur la console du navigateur ? C'est parce que les actions serveur s'exécutent sur le serveur, et non sur le navigateur côté client.

![Sortie Mike](https://cdn.hashnode.com/res/hashnode/image/upload/v1729167722231/e8c40a4d-e506-42fb-8ea3-233e295ac534.png align="center")

Ainsi, avec cela, nous avons maintenant établi un flux de données comme ceci :

Page => Formulaire => Action Serveur

La page a un formulaire. Le formulaire exécute une action serveur lors de la soumission. L'action serveur imprime les données du formulaire sur la console du serveur.

Améliorons maintenant ces éléments pour passer des arguments supplémentaires à l'action serveur.

## Comment passer des arguments supplémentaires

Passons une prop au composant `UserForm` depuis la page. Nous allons passer un `userId` avec une valeur pour prétendre que nous passons cet userId de manière programmatique à notre formulaire et à l'action serveur à partir de là.

```javascript
import UserForm from "@/components/user-form";

const ExtraArgsDemo = () => {
  return (
    <UserForm userId={"1234"} />
  )
}

export default ExtraArgsDemo;
```

Dans le composant `UserForm`, nous acceptons la prop `userId`. Maintenant, nous devons faire quelque chose de spécial pour passer cet userId à l'action serveur `updateUser`.

JavaScript a une méthode magique appelée `bind()` qui nous aide à créer une `Fonction Partiellement Appliquée`. Avec cette [fonction partiellement appliquée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#partially_applied_functions), vous pouvez créer une fonction à partir des arguments prédéfinis d'une autre fonction.

Dans notre cas, la fonction `updateUser` a déjà un argument appelé `formData`. Maintenant, nous pouvons passer `userId` comme argument supplémentaire en utilisant la méthode `bind()` pour créer une nouvelle fonction.

```javascript
const updatedUserWithId = updateUser.bind(null, userId);
```

Le premier argument de la méthode `bind()` est le contexte auquel vous liez la fonction. Le contexte gère l'association de la fonction avec la valeur du mot-clé `this`. Dans notre cas, nous pouvons le garder `null` car nous ne le changeons pas. Après cela, nous avons passé le nouvel argument `userId`. Il est bon de savoir que la méthode `bind()` fonctionne à la fois sur les composants serveur et client.

Voici le composant `UserForm` modifié (fichier `user-form.jsx`). Notez que la valeur de l'action du formulaire est maintenant modifiée pour la nouvelle fonction `updatedUserWithId`.

```javascript
import { Input } from "./ui/input"
import { Button } from "./ui/button"

import { updateUser } from "@/app/actions/user"

const UserForm = ({userId}) => {
  const updatedUserWithId = updateUser.bind(null, userId);

  return(
    <form className="p-4 flex" action={updatedUserWithId}>
      <Input className="w-1/2 mx-2" type="text" name="name" />
      <Button type="submit">Mettre à jour le nom de l'utilisateur</Button>
    </form>
  )
}

export default UserForm;
```

Maintenant, l'action serveur recevra la valeur `userId` en tant qu'argument. Affichons également cela sur la console.

```javascript
"use server"

export async function updateUser(userId, formData) {
  const name = formData.get('name');
  console.log(userId);
  console.log(name);

  // Faites ce que vous voulez avec l'ID de l'utilisateur et le nom, sauvegardez-le dans la base de données,
  // créez une facture, peu importe !
}
```

Maintenant, si vous soumettez le formulaire avec une valeur de nom :

![Application avec actions serveur à nouveau](https://cdn.hashnode.com/res/hashnode/image/upload/v1729167845597/b4c58399-4188-4b89-8ec7-dd2602c10ccd.png align="center")

Vous verrez que les valeurs userId et name sont toutes deux enregistrées dans la console du serveur. Super ! Nous avons enregistré une valeur à partir des données du formulaire, et l'autre a été passée en interne à l'action serveur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1729169164296/d0ef49f8-88bc-4e82-a509-cbb859df87e1.png align="center")

Ainsi, nous avons appris comment passer des arguments supplémentaires à l'action serveur ainsi que les données du formulaire.

## Qu'en est-il des champs cachés ?

HTML prend en charge un champ de formulaire de type caché pour passer des données client au serveur sans accepter l'entrée des utilisateurs. Cela signifie donc que nous aurions pu utiliser le champ caché pour passer la valeur `userId` comme ceci :

![champ caché](https://cdn.hashnode.com/res/hashnode/image/upload/v1729485711865/21f33410-fcdd-46ea-b14c-d57004b30a96.png align="center")

Alors pourquoi avons-nous fait tout cela avec la méthode `bind()` ? Eh bien, à cause des préoccupations de sécurité. Lorsque vous passez des données en utilisant des champs cachés, la valeur fera partie du HTML rendu, et elle ne sera pas encodée non plus. Il est donc préférable de la gérer de manière programmatique.

## Ressources

C'est tout pour l'instant. Avez-vous apprécié la lecture de cet article et avez-vous appris quelque chose de nouveau ? Si oui, j'adorerais savoir si le contenu était utile. Laissez-moi partager quelques ressources supplémentaires dont vous pourriez avoir besoin :

* Tout le code source utilisé dans cet article est [sur mon GitHub](https://github.com/atapas/nextjs-email/tree/extra-arg).

* Voici le [Cours accéléré sur les actions serveur avec modèles et projet](https://www.youtube.com/watch?v=gQ2bVQPFS4U).

* Voici la [Documentation officielle des actions serveur](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) si vous souhaitez en lire plus.

* Et vous pouvez en lire plus sur la [méthode bind() ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind).

De plus, vous pouvez vous connecter avec moi en :

* Vous abonnant à ma [Chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1). Si vous souhaitez apprendre `React` et son écosystème, comme `Next.js`, avec des concepts fondamentaux et des projets, j'ai une excellente nouvelle pour vous : vous pouvez [consulter cette playlist sur ma chaîne YouTube](https://www.youtube.com/watch?v=VSB2h7mVhPg&list=PLIJrr73KDmRwz_7QUvQ9Az82aDM9I8L_8) avec plus de 25 tutoriels vidéo et plus de 15 heures de contenu engageant jusqu'à présent, gratuitement. J'espère que vous les aimerez aussi.

* [Me suivant sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils pour monter en compétences.

* Consulter et suivre mon travail Open Source sur [GitHub](https://github.com/atapas).

* Je publie régulièrement des articles significatifs sur mon [Blog GreenRoots](https://blog.greenroots.info/), vous pouvez les trouver utiles également.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et continuez à apprendre.