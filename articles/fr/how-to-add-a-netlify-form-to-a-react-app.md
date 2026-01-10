---
title: Comment ajouter un formulaire Netlify à une application React construite avec
  create-react-app
subtitle: ''
author: Joseph Mawa
co_authors: []
series: null
date: '2021-04-19T21:20:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-netlify-form-to-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/questions-4304981_1280.jpg
tags:
- name: create-react-app
  slug: create-react-app
- name: forms
  slug: forms
- name: Netlify
  slug: netlify
- name: React
  slug: react
seo_title: Comment ajouter un formulaire Netlify à une application React construite
  avec create-react-app
seo_desc: 'If you are a web developer, at some point you will need to capture information
  from people who use your website or app.

  One way of doing so is by using HTML forms. But there are also tons of frameworks
  out there that you can use to build web apps ver...'
---

Si vous êtes un développeur web, à un moment donné, vous devrez capturer des informations auprès des personnes qui utilisent votre site web ou votre application.

Une façon de le faire est d'utiliser des formulaires HTML. Mais il existe également de nombreux frameworks que vous pouvez utiliser pour construire des applications web très rapidement.

Un de ces frameworks est React. Vous pouvez démarrer une application monopage (SPA) très facilement en utilisant `create-react-app` (CRA). Ensuite, vous pouvez la déployer sur des plateformes telles que Netlify, Vercel, Firebase et Digital Ocean en seulement quelques étapes.

L'objectif principal de cet article sera de montrer comment ajouter la fonctionnalité de formulaire Netlify à une application React démarrée avec `create-react-app`. À la fin de ce tutoriel, vous serez capable de :

* Configurer rapidement une application monopage en utilisant `create-react-app`

* Ajouter la fonctionnalité pour utiliser la gestion de formulaires intégrée de Netlify

* Déployer l'application sur Netlify

* Configurer la fonctionnalité de gestion de formulaires intégrée sur Netlify pour envoyer des notifications par email chaque fois qu'un formulaire a été soumis par un client

Que vous soyez un débutant essayant de déployer votre première application React ou un développeur React expérimenté, cet article vous aidera à apprendre à utiliser la fonctionnalité de formulaire intégrée de Netlify sans écrire de code côté serveur.

Si vous êtes un développeur React expérimenté, vous pouvez sauter l'introduction et passer à l'`étape 6`. Si vous êtes un débutant en React, vous pouvez suivre dès le début.

## Prérequis

Pour suivre cet article, vous devriez :

* Avoir une connaissance intermédiaire de JavaScript. Si vous êtes un débutant, vous pouvez toujours suivre et poser des questions sur le [forum freeCodeCamp](https://forum.freecodecamp.org) si quelque chose n'est pas clair. Vous pouvez également copier les exemples de code dans chaque section et les essayer dans votre éditeur de texte pour comprendre ce qui se passe.

* Avoir au moins une connaissance de base de la bibliothèque React

* Avoir Node installé sur votre machine

* Avoir un compte Netlify. Si vous n'en avez pas, vous pouvez vous inscrire gratuitement en utilisant votre adresse email.

* Avoir un éditeur de texte comme [VS code](https://code.visualstudio.com/) ou [Atom](https://atom.io/) installé sur votre machine. Vous pouvez essayer les exemples de code pendant que vous suivez. Cela vous aidera à comprendre plus facilement.

## Étape 1 : Vérifier si vous avez `node` et `npm` installés sur votre machine

Avant de commencer, vous devriez vérifier si vous avez [node](https://nodejs.org/en/) installé sur votre machine.

Node est un environnement d'exécution JavaScript, et il est important de l'avoir installé pour pouvoir exécuter le projet. Ouvrez un terminal et tapez la commande suivante dans l'invite de commande.

```js
node -v
```

Au lieu de la commande ci-dessus, vous pouvez également taper la commande ci-dessous. Les deux font la même chose.

```js
node --version
```

Si Node est installé, vous devriez voir la version imprimée dans le terminal. Votre version peut être différente de la mienne, mais vous devriez voir quelque chose comme :

```js
v15.13.0
```

Si Node est installé, cela signifie que `npm` est également installé car les versions récentes de Node incluent `npm`. Si vous êtes curieux, tapez la commande `npm --version` ou `npm -v`. Vous devriez voir la version de `npm` qui a été installée.

D'autre part, si vous n'avez pas Node installé sur votre machine, vous pouvez le télécharger et l'installer pour votre plateforme depuis [ici](https://nodejs.org/en/download/).

## Étape 2 : Naviguer vers le répertoire où vous souhaitez créer votre projet

Ensuite, vous devez naviguer vers un répertoire où vous souhaitez créer votre projet. Vous pouvez travailler depuis le Bureau ou depuis n'importe quel répertoire de votre choix.

J'aime garder mes projets personnels dans un répertoire appelé `projects` sur le bureau pour un accès facile. Ce n'est qu'un choix personnel.

Ouvrez le terminal et naviguez vers le répertoire où vous souhaitez créer votre projet. J'utilise `cd` (change directory) dans les commandes ci-dessous.

**À noter** : J'ai déjà un répertoire nommé `projects` sur le Bureau. Si vous n'en avez pas, vous devrez d'abord exécuter la commande `mkdir projects` avant de vous y rendre avec `cd`. Comme je l'ai dit ci-dessus, vous pouvez décider de travailler depuis un autre répertoire et vous n'aurez pas à exécuter les commandes ci-dessous.

1. `cd Desktop`

2. `cd projects`

## Étape 3 : Comment démarrer une application monopage en utilisant `create-react-app`

Nous allons démarrer un projet React en utilisant `create-react-app`. Dans le répertoire où vous souhaitez créer votre projet, exécutez la commande ci-dessous.

```js
npx create-react-app netlify-form
```

J'ai nommé le projet `netlify-form`. Vous pouvez lui donner un autre nom si vous le souhaitez.

Si vous n'avez pas `create-react-app` installé, vous verrez une invite dans le terminal vous demandant si vous souhaitez l'installer. Tapez `Y` dans l'invite de commande (pour "Oui"). Cela installera `create-react-app` puis créera un projet React dans le répertoire `netlify-form`.

Si vous avez déjà `create-react-app` dans votre système, il passera directement à la création d'un projet React dans le répertoire `netlify-form`. Cela prendra quelques minutes, alors soyez patient.

Dans l'étape suivante, vous allez démarrer le serveur de développement.

## Étape 4 : Démarrer le serveur de développement

Dans cette étape, nous allons démarrer le serveur de développement. Cela garantit le rechargement à chaud lorsque nous apportons des modifications au projet pendant le développement afin que nous puissions voir comment notre projet prend forme.

Vous pouvez ouvrir le répertoire `netlify-form` dans votre éditeur de texte de choix. Lorsque vous êtes dans `netlify-form`, ouvrez le terminal et exécutez la commande ci-dessous.

```js
npm run start
```

La commande ci-dessus démarre le serveur de développement sur le port 3000. Si un autre projet ou service est en cours d'exécution sur le port 3000, vous serez invité à démarrer le serveur sur un autre port.

Un nouvel onglet de navigateur sera ouvert dans votre navigateur par défaut où vous pourrez voir le projet. Toute modification que vous apportez sera automatiquement reflétée dans le navigateur.

Dans l'étape suivante, vous allez créer un composant qui contiendra votre formulaire.

## Étape 5 : Créer un nouveau composant dans le répertoire `src`

Maintenant, vous allez créer un composant nommé `Form` dans le répertoire `src`. Dans ce composant, vous aurez le formulaire qui sera rendu dans votre application.

Créez un fichier `Form.js` dans le répertoire `src`, puis copiez et collez le code ci-dessous :

```js
import React from "react";

export default function Form() {
  return (
    <form name="contact" method="post">
      <p>
        <label htmlFor="name">Nom</label> <br />
        <input type="text" id="name" name="name" required />
      </p>
      <p>
        <label htmlFor="email">Email</label> <br />
        <input type="email" id="email" name="email" required />
      </p>
      <p>
        <label htmlFor="message">Message</label> <br />
        <textarea id="message" name="message" required></textarea>
      </p>
      <p>
        <input type="submit" value="Envoyer le message" />
      </p>
    </form>
  );
}
```

Le composant ci-dessus retourne un formulaire ordinaire. J'ai enfermé chaque paire label-input et label-textarea dans sa propre balise `p`.

Il n'y a rien de spécial dans la balise `p`. Vous pouvez utiliser `div` si vous le souhaitez. Je l'ai simplement utilisée parce que je veux appliquer un espacement entre les paires label-input successives sans utiliser de CSS.

Vous pouvez importer le composant `Form` et le rendre dans `App`. Pour nettoyer `App.js`, vous pouvez également supprimer certains éléments qui viennent avec `create-react-app`, afin qu'il ressemble à ceci :

```js
import "./App.css";
import Form from "./Form";

function App() {
  return (
    <div className="App">
      <h1> Contactez-nous </h1>
      <Form />
    </div>
  );
}

export default App;
```

Vous pouvez également nettoyer `App.css` pour qu'il ne contienne que le CSS suivant :

```css
.App {
  padding: 1em;
}
```

Lorsque vous vérifiez votre formulaire dans le navigateur, il devrait ressembler à l'image ci-dessous.

![Screenshot-from-2021-04-17-14-30-11](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-from-2021-04-17-14-30-11.png align="left")

Pour l'instant, déployer cette application sur Netlify ne nous permettra pas de capturer les soumissions de formulaires des clients. Pour cela, nous devons ajouter des informations nécessaires à notre application afin que les robots de Netlify puissent détecter notre formulaire.

Dans l'étape suivante, nous allons ajouter toutes les informations nécessaires pour rendre le formulaire JSX dans React détectable par Netlify.

## Étape 6 : Ajouter les informations nécessaires pour rendre le `formulaire` détectable par les robots de Netlify

Dans cette étape, vous allez ajouter certaines informations à votre application afin que Netlify puisse détecter la configuration de votre formulaire. Si votre formulaire est déployé en HTML simple, le processus pour le rendre détectable est assez simple. Vous pouvez en lire plus dans la [documentation](https://docs.netlify.com/forms/setup/?_ga=2.214149207.1369394306.1618461268-796209470.1617367540).

Mais si vous traitez avec un formulaire JSX dans React comme dans cette application simple que nous construisons, alors vous devrez faire un peu plus de travail. Vous pouvez suivre les étapes décrites ci-dessous.

### Ajouter la version HTML du formulaire au fichier `index.html`

Copiez et collez votre formulaire JSX dans le fichier `index.html` juste après la balise d'ouverture `body`. Cela garantira que Netlify détecte notre formulaire car les robots de construction analysent directement les fichiers HTML au moment du déploiement. Le formulaire JSX ne peut pas être analysé par les robots.

Vous pouvez supprimer les éléments `label` et l'élément `submit` car nous allons ajouter un attribut `hidden` au `form` afin qu'il ne soit pas visible pour les utilisateurs et les lecteurs d'écran.

Vous pouvez ne laisser que les attributs `type` et `name` sur les éléments `input` et l'attribut `name` sur `textarea` afin de garder le formulaire minimal.

Cela est illustré dans le code ci-dessous :

```HTML
<form name="contact" netlify netlify-honeypot="bot-field" hidden>
     <input type="text"  name="name">
     <input type="email" name="email">
     <textarea name="message"></textarea>
</form>
```

Comme vous pouvez le voir dans l'extrait de code ci-dessus, il y a des attributs supplémentaires `netlify` et `netlify-honeypot` sur le `form`. Les robots de Netlify les utiliseront lors de l'analyse de votre HTML, alors assurez-vous de les ajouter.

N'oubliez pas d'ajouter l'attribut `hidden`, car ce formulaire doit être caché aux utilisateurs de votre site web. Il est également important de noter que les attributs de nom dans le formulaire HTML doivent être exactement les mêmes que ceux dans le formulaire JSX correspondant.

### Ajouter un élément `input` caché dans votre formulaire JSX

Vous devez également ajouter un élément `input` caché dans votre formulaire JSX avec les attributs `name` et `value` comme illustré dans le code ci-dessous :

```HTML
<input type="hidden" name="form-name" value="contact" />
```

La valeur de l'attribut `name` doit toujours être `"form-name"` et la valeur de l'attribut `value` doit être le nom du formulaire HTML, qui dans notre cas est `contact`.

Votre fichier `Form.js` devrait maintenant ressembler à ceci :

```js
import React from "react";

export default function Form() {
  return (
    <form name="contact" method="post">
      <input type="hidden" name="form-name" value="contact" />
      <p>
        <label htmlFor="name">Nom</label> <br />
        <input type="text" id="name" name="name" required />
      </p>
      <p>
        <label htmlFor="email">Email</label> <br />
        <input type="email" id="email" name="email" required />
      </p>
      <p>
        <label htmlFor="message">Message</label> <br />
        <textarea id="message" name="message" required></textarea>
      </p>
      <p>
        <input type="submit" value="Envoyer le message" />
      </p>
    </form>
  );
}
```

Si vous vérifiez l'application dans le navigateur, vous devriez pouvoir voir le formulaire – mais vous ne pourrez pas le soumettre depuis votre configuration locale. Vous ne pouvez soumettre des formulaires qu'après avoir déployé votre application sur Netlify.

Alors faisons cela maintenant.

## Étape 7 : Déployer l'application sur Netlify

Dans cette étape, vous allez déployer notre application sur Netlify afin de pouvoir tester si les clients peuvent soumettre des formulaires.

Il existe plusieurs façons de déployer votre application sur Netlify. Une méthode consiste à construire l'application localement et à la déployer depuis la ligne de commande, ou en glissant-déposant la version de production sur Netlify. La deuxième méthode consiste à configurer le déploiement automatique via GitHub, BitBucket ou GitLab.

Dans cette application, vous allez construire l'application localement et utiliser la méthode la plus simple de glisser-déposer. Cette étape nécessite que vous vous connectiez à votre compte Netlify. Si vous n'avez pas de compte, vous pouvez vous inscrire pour en obtenir un.

Exécutez la commande `npm run build` dans le terminal. Cela construira l'application pour la production dans le dossier `build`. Cela prendra un peu de temps. Vous devriez pouvoir voir le répertoire `build` après avoir exécuté la commande avec succès.

Connectez-vous à votre compte Netlify. Sur le tableau de bord de Netlify, cliquez sur l'élément de menu `Sites`. En bas de la page, il y a une zone où vous pouvez glisser-déposer la version de production de votre application. Après avoir glissé-déposé le dossier `build`, le processus de construction commence.

Après que le site soit construit avec succès, vous pouvez vérifier le tableau de bord du projet pour savoir si Netlify détecte votre formulaire. Si le formulaire est détecté, vous verrez généralement un message à cet effet dans la section des formulaires en bas à gauche.

Il ne vous reste plus qu'à remplir le formulaire et à le soumettre. Après la soumission, vous devriez pouvoir voir les informations soumises.

![Screenshot-from-2021-04-17-14-03-26](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-from-2021-04-17-14-03-26.png align="left")

Ensuite, nous apprendrons comment configurer des alertes par email pour être notifié chaque fois qu'un utilisateur soumet un formulaire.

## Étape 8 : Configurer les mises à jour par email chaque fois qu'un utilisateur soumet un formulaire

Dans cette section, vous allez configurer votre application pour envoyer des notifications par email à une adresse email chaque fois qu'un formulaire est soumis.

Pour ce faire, naviguez vers les paramètres du site. À gauche, vous verrez une liste d'éléments de menu. Cliquez sur l'option `formulaires`.

Sous `notifications sortantes`, cliquez sur `Ajouter une notification` et sélectionnez l'option `Notification par email`. Vous allez ensuite configurer vos préférences en conséquence.

![Screenshot-from-2021-04-17-14-11-20](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-from-2021-04-17-14-11-20.png align="left")

C'est tout ce que vous devez faire pour utiliser la fonctionnalité de formulaire intégrée de Netlify avec CRA. Vous n'avez pas besoin de code côté serveur pour obtenir des retours de vos clients.

Si vous avez réussi à suivre les étapes ci-dessus, félicitations ! Vous pouvez maintenant explorer d'autres fonctionnalités.

Si vous rencontrez des erreurs ou des problèmes liés aux formulaires Netlify en suivant ce tutoriel, n'hésitez pas à consulter [ce conseil de débogage des erreurs de formulaire Netlify](https://answers.netlify.com/t/support-guide-form-problems-form-debugging-404-when-submitting/92).

Vous pouvez également lire la [documentation sur les formulaires Netlify](https://docs.netlify.com/forms/setup/).

Si vous ne trouvez pas de solution après avoir utilisé les ressources ci-dessus, vous pouvez poser une question dans le [forum Netlify](https://answers.netlify.com/). Il y a un certain nombre de personnes amicales dans cette communauté qui pourraient vous aider.

## Conclusion

Dans cet article, nous avons examiné :

* Comment créer une application React en utilisant `create-react-app`

* Comment ajouter un formulaire JSX à votre application React

* Comment ajouter les informations nécessaires pour que votre formulaire puisse être détecté par les robots de Netlify

* Comment déployer une version de production sur Netlify

* Comment configurer des notifications par email chaque fois qu'un client soumet un formulaire

### Références

* [Documentation sur les formulaires Netlify](https://docs.netlify.com/forms/setup/)

* [Documentation sur create-react-app](https://create-react-app.dev/)

* [Documentation React](https://reactjs.org/docs/getting-started.html)

* [Débogage des erreurs de formulaire Netlify](https://answers.netlify.com/t/support-guide-form-problems-form-debugging-404-when-submitting/92)