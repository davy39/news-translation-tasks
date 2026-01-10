---
title: Comment utiliser les variables d'environnement dans VanillaJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-02T22:54:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-environment-variables-in-vanillajs
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/nguy-n-phuc-6ZO3rE6OLew-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Vanilla
  slug: vanilla
seo_title: Comment utiliser les variables d'environnement dans VanillaJS
seo_desc: 'By Caleb Olojo

  In this article, you will learn about environment variables in Vanilla JavaScript.
  You''ll also learn how to serve API keys to your application through the Netlify
  build command.

  What are JavaScript environment variables?

  Environment va...'
---

Par Caleb Olojo

Dans cet article, vous apprendrez à utiliser les variables d'environnement en JavaScript Vanilla. Vous apprendrez également comment servir des clés API à votre application via la commande de build de Netlify.

## Qu'est-ce que les variables d'environnement JavaScript ?

Les variables d'environnement sont très courantes lorsque vous utilisez des frameworks JavaScript comme React ou Vue pour créer des interfaces utilisateur frontend ou NodeJS côté serveur. 

L'idée principale (ou du moins, la façon dont je la comprends) des variables d'environnement est qu'elles vous offrent la flexibilité de définir des conditions pour le comportement de votre application ou logiciel dans différents modes – développement et production.

Vous créez ces conditions lorsque l'UI/frontend du logiciel interagit avec une API ou un serveur backend nécessitant une méthode d'authentification avant de fournir les résultats de l'action (comme un appel API). La méthode la plus courante implique la fourniture d'une clé API avant de pouvoir compléter une requête.

Si vous avez déjà essayé d'obtenir des données à partir d'une API, vous devez fournir cette clé API pour que la requête de données soit réussie. Cela implique l'ajout d'un en-tête `Authorization` à l'appel API.

Jetez un œil à une requête fetch typique et son en-tête d'autorisation ci-dessous.

```js
const apiCall = () => {
    fetch(url, {
    	headers: {
            Authorization: `bearer ${private_api_key}`
        }
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => JSON.stingify(err))
}
```

Les variables d'environnement stockent des variables, comme leur nom l'indique. Les valeurs ou éléments assignés à ces variables peuvent être des clés API nécessaires pour effectuer certaines requêtes ou opérations. 

Pour créer une variable d'environnement, il vous suffit de créer un nouveau fichier appelé .env dans le dossier racine du projet sur lequel vous travaillez. Ensuite, vous pouvez commencer à ajouter toutes les variables que vous ne souhaitez pas révéler à quiconque. 

Le fichier `.gitignore` contient la liste des fichiers que Git ne doit pas suivre, et le fichier `.env` sera dans ce fichier.

## Comment utiliser les fichiers .env dans VanillaJS

Vous utilisez des variables d'environnement dans le backend d'une application. Maintenant, vous vous dites probablement "mais je peux créer un fichier `.env` dans une application React". 

La vérité est que vous avez tout à fait raison – mais React a été initialisé de manière à inclure Node.js. Cela signifie que vous devez utiliser le gestionnaire de paquets Node pour effectuer certaines opérations.

Vous pouvez également créer un fichier .env lorsque vous utilisez VanillaJS, mais vous ne pourrez pas accéder à la variable globale process.env que Node fournit à l'exécution. Node traite le fichier `.env` comme un objet, donc il a la capacité de faire ceci : `process.env.env_variable`.

```js
const env = {
    env_variable: "bgrtyaqQtyfadV0F08BHGvfsgskl",
    topic_id: "F08BHGvfsgsklgrtyaqQtyfadV0F08"
}

console.log(process.env.env_variable)

// affiche bgrtyaqQtyfadV0F08BHGvfsgskl dans la console
```

Vous utilisez VanillaJS côté client, il n'est donc pas vraiment possible de créer un `.env` et d'utiliser des variables d'environnement. Cela est dû au fait que vous ne pouvez pas utiliser la variable globale process.env fournie par Node (pour accéder aux variables créées dans le fichier `.env`) dans le navigateur. 

Alors, comment pouvez-vous réellement utiliser des variables d'environnement ? Hmm...surtout puisque vous ne pouvez pas utiliser de variables d'environnement en écrivant du JavaScript côté client (je veux dire VanillaJS). 

Le package npm appelé [dotenv](https://npmjs.org/dotenv) offre une solution car il a accès à la variable globale Node `process.env`.

Une fois le package installé, un dossier `node_modules` sera automatiquement créé avec deux fichiers, `package.json` et `package-lock.json`. Ces fichiers contiennent les détails de l'application. 

Mais dès que vous l'utilisez, JavaScript génère une erreur indiquant que `require` n'est pas défini :

```js
require("dotenv").config()

const apiCall = () => {
    fetch(url, {
    	headers: {
            Authorization: `bearer ${process.env.env_variable}`
        }
    })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => JSON.stingify(err))
}
```

Cette erreur se produit car `require` n'est pas dans le `node_module` ou la liste des packages qui permettraient au package `dotenv` de fonctionner. 

En résumé, `dotenv` a besoin de `require` pour fonctionner. Vous pouvez obtenir `require` à partir de [RequireJS](https://requirejs.org/), mais cela représente une autre complication. Vous devriez lire la documentation pour savoir comment appliquer les scripts qui rendraient la variable globale de Node disponible côté client.

## Pourquoi passer par toutes ces complications ?

Vraiment. Pourquoi ?

Les gens utilisent généralement des API publiques soit pour un projet personnel, soit pour expérimenter certains concepts qu'ils n'ont pas encore maîtrisés. 

La plupart du temps, ces API ne nécessitent pas l'utilisation de clés (API) privées pour une authentification ou une autre. Cela est courant lorsque vous traitez avec des endpoints qui permettent uniquement la méthode `GET` pour récupérer des données.

Des API comme celles de GitHub ou Twitter nécessitent l'utilisation de clés API pour authentifier l'utilisateur avant d'autoriser la requête. L'API GitHub GraphQL, par exemple, nécessite un jeton d'accès pour un appel API réussi. Mais le jeton d'accès a quelques particularités, dont la capacité à effectuer 5000 requêtes en une heure. 

Vous ne pouvez jamais commiter ce jeton d'accès dans le flux de travail Git de votre projet. Si vous le commitez, GitHub le supprimera pour des raisons de sécurité. C'est là que cela devient un problème que VanillaJS ne peut pas contenir de variables d'environnement. 

Le jeton d'accès fourni par GitHub (qui est finalement supprimé une fois qu'il est commité dans le flux de travail) ne permettra pas à l'application de fonctionner en mode `production`. Il fonctionnera parfaitement en mode `développement` – mais une fois supprimé, et le dépôt/projet déployé sur Netlify, alors Netlify ne pourra plus accéder aux clés.

## Comment résoudre ce problème ?

Netlify dispose d'un onglet "build and deploy". Cela vous permet de modifier la manière dont le processus de déploiement continu se déroule avec vos projets ou dépôts sur GitHub. 

Vous pouvez décider d'arrêter toutes les builds automatiques concurrentes dès que Netlify détecte un push sur la branche `master` ou `main`, désactiver toutes les builds jusqu'à ce que le projet soit complètement terminé en mode développement, et bien d'autres fonctionnalités que je ne peux pas me rappeler.

Mais ce n'est pas le sujet de cet article. Ce qui nous intéresse, c'est comment utiliser le jeton d'accès GitHub localement (en veillant à ce qu'il ne soit pas inclus dans l'historique des commits) et ensuite permettre à Netlify d'y accéder en `production`.

L'image ci-dessous montre l'onglet "build and deploy" sur Netlify.  
 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-from-2021-05-31-10-39-42.png)

Remarquez le champ de saisie de la commande de build ? En utilisant l'extrait de code ci-dessous :

```bash
cd js && echo -e "const TOKEN = 'api-token';\n\nexport default TOKEN;" > config.js
```

la commande ci-dessus injectera simplement un nouveau fichier appelé `config.js` dans le dossier `js` pendant le processus de build. Cela donne à Netlify accès à votre clé API (jeton d'accès). 

Si vous n'avez pas de dossier `js` dans votre projet, c'est-à-dire que tous les fichiers sont dans le dossier racine du projet, vous pouvez simplement ajouter `echo -e "const TOKEN = 'api-token';\n\nexport default TOKEN;" > config.js` comme commande de build.

```js
const TOKEN = 'api-token';

export default TOKEN;
```

Pour vous assurer de pouvoir utiliser l'instruction ES6 `import` dans le fichier JavaScript, vous devez ajouter l'attribut `type="module"` dans la balise script.

```html
<script src="./index.js" type="module"></script>
```

## Conclusion

Cela peut ne pas sembler être la meilleure pratique ou méthode pour utiliser les variables d'environnement. Cela est dû au fait que votre clé API pourrait encore être visible par quiconque visite votre application sur Internet lorsqu'il ouvre les outils de développement dans son navigateur préféré. 

Mais cela m'a aidé à contourner le problème de GitHub supprimant ces clés, ce qui empêcherait l'application de fonctionner en `production`. 

Vous ne devriez envisager cette méthode que lorsque vous utilisez une API qui, si votre clé API est révélée, ne causera pas beaucoup de dommages si elle est utilisée par un tiers.

Merci d'avoir lu cet article. J'espère qu'il vous sera utile. ;)