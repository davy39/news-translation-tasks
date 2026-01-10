---
title: Comment créer votre propre boîte de commentaires gratuite et sans serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T18:42:38.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-build-your-own-free-serverless-comment-box-dc9d4f366d12
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GyItksCXjWpt1FvrlsOUEQ.png
tags:
- name: Blogging
  slug: blogging
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Comment créer votre propre boîte de commentaires gratuite et sans serveur
seo_desc: 'By Shaun Persad

  Contentful’s flexible content modeling goes far beyond blog posts. Here’s how you
  can leverage Contentful and Netlify to create a nested commenting system that’s
  easy to moderate and deploy.

  The motivation

  I find most commenting syste...'
---

Par Shaun Persad

La modélisation flexible du contenu de Contentful va bien au-delà des articles de blog. Voici comment vous pouvez utiliser Contentful et Netlify pour créer un système de commentaires imbriqués facile à modérer et à déployer.

### La motivation

Je trouve que la plupart des systèmes de commentaires disponibles sont... insuffisants. Disqus peut souvent être lent à s'afficher, et leur comportement de suivi des utilisateurs n'a pas la meilleure réputation. Pendant ce temps, le plugin de commentaires de Facebook est assez bien, mais bien sûr, il est limité aux utilisateurs de Facebook.

Ce que je voulais vraiment, c'était la vitesse native et l'approche des commentaires imbriqués et de la modération adoptées par des sites comme Hacker News et Indie Hackers, mais j'avais besoin d'une solution portable pour plusieurs projets.

Il ne semblait tout simplement pas y avoir de solution idéale, alors j'ai décidé de créer la mienne, avec ma liste de fonctionnalités souhaitées :

* **Gratuit**
* **Faible barrière à l'entrée** — étapes minimales requises pour soumettre un commentaire
* **Faible maintenance** — sans serveur, pour ne pas avoir à se soucier de l'hébergement ou de la mise à l'échelle
* **Modération facile** — utiliser un tableau de bord pour effectuer des opérations _CRUD_ sur les commentaires
* **Performant** — super rapide à apparaître sur la page
* **Flexible** — les utilisateurs doivent pouvoir se connecter via plusieurs plateformes
* **Puissant** — les commentaires doivent avoir des fonctionnalités de formatage intelligentes
* **Haute qualité des commentaires** — les utilisateurs peuvent voter pour ou contre les commentaires
* **Abonnements** — les utilisateurs peuvent recevoir des notifications lorsque leurs commentaires reçoivent une réponse

Au cours de cette série, nous allons développer un système de commentaires qui intègre chacun des aspects ci-dessus.

### Le plan

Notre stack inclura initialement :

* [Contentful](https://www.contentful.com/) comme base de données et tableau de bord de modération
* AWS Lambda via [Netlify](https://www.netlify.com/) comme notre back-end
* [React](https://reactjs.org/) sur le front-end

Nous allons créer un composant React pour servir de boîte de commentaires, et lui fournir la capacité de faire un appel API à Contentful pour récupérer les commentaires si nécessaire. Il pourra également faire un appel API à notre fonction Lambda pour poster un commentaire sur Contentful.

En termes de projet, notre fonction Lambda vivra aux côtés de notre code front-end. Le front-end et le back-end seront configurés pour être déployés en continu via Netlify.

Au fait, la stack ci-dessus est entièrement gratuite ! Enfin, presque. À moins que vous ne prévoyiez de faire plus de 10 000 commentaires, c'est gratuit. De plus, je ne suis affilié à aucune de ces entreprises... J'aime juste leurs produits :)

### Contentful en 10 secondes

Si vous n'êtes pas déjà familier avec Contentful et [son fonctionnement](https://www.contentful.com/r/knowledgebase/contentful-101/), c'est un CMS "headless" (piloté par API). Vous pouvez modéliser votre contenu avec différents champs et types de champs, puis créer du contenu basé sur ces modèles. Vous pouvez construire votre front-end comme vous le souhaitez, et interroger vos données en utilisant leur API. C'est super flexible, et leur tableau de bord est assez agréable à utiliser. C'est essentiellement la meilleure chose qui soit arrivée aux CMS depuis, eh bien, toujours ?

J'utilisais déjà Contentful pour mes articles de blog, alors je me suis demandé, pourrait-il être viable d'héberger des commentaires également ? Je suis heureux de rapporter que la réponse est oui ! Cependant, quelques éléments de ma liste de souhaits ne fonctionnent pas tout à fait en utilisant uniquement Contentful. Mais ne vous inquiétez pas, nous y arriverons... dans les prochains articles de cette série.

Nous utiliserons Contentful parce que :

* modélisation flexible des données
* API pratique
* modération via un tableau de bord
* vous l'utilisez peut-être déjà pour votre site web/blog qui a besoin de commentaires

### Netlify en 10 secondes

Je pense que Netlify offre de loin l'expérience de déploiement la plus agréable pour les applications front-end. Il se connecte à votre dépôt GitHub et vous permet de déployer en continu un site statique sur un hébergement soutenu par CDN. Ils ont également [Netlify Functions](https://www.netlify.com/docs/functions/), qui vous permettent de déployer sur AWS Lambda sans aucune des complications de manipuler AWS.

Vous pouvez commencer avec [leur documentation](https://www.netlify.com/docs/#getting-started), mais honnêtement, leur tableau de bord est si facile à utiliser et à comprendre, je recommande simplement de [vous connecter](https://app.netlify.com/) et de regarder autour de vous.

Nous utiliserons Netlify parce que :

* intégration sans douleur avec AWS Lambda
* vous l'utilisez peut-être déjà pour votre site web/blog qui a besoin de commentaires
* Si vous ne l'utilisez pas déjà, vous pouvez toujours déployer les fonctions Lambda que nous créons sur AWS lui-même

### Attendez, pas de "React en 10 secondes" ?

Je ne sais pas si 10 secondes suffisent pour rendre justice à React. Si vous ne l'avez pas encore appris, vous devriez ! Mais sautez les trucs Redux et Flux. Les chances sont que vous n'avez besoin d'aucun de cela (mais c'est un autre sujet pour une autre fois).

### Modélisation du contenu dans Contentful

Maintenant, passons aux choses sérieuses.

Il y a deux approches différentes que nous pourrions prendre concernant la manière dont nous gérons nos utilisateurs : les commentaires **sans authentification** et **avec authentification** :

* Sans authentification — n'importe qui peut laisser un commentaire simplement en fournissant son nom
* Avec authentification — seuls les utilisateurs authentifiés dans un système d'authentification peuvent commenter

Je préfère les commentaires avec authentification, car selon moi, les conversations tendent à être plus civilisées. De plus, vous évitez généralement le spam. En revanche, la barrière pour créer un commentaire est légèrement plus élevée.

Cependant, nous commencerons par les commentaires sans authentification, car c'est plus simple à implémenter. Une fois que nous aurons les pieds mouillés, nous passerons aux commentaires avec authentification dans la partie 2.

Quoi qu'il en soit, nous allons d'abord avoir besoin de [créer un modèle de contenu](https://www.contentful.com/r/knowledgebase/content-modelling-basics/) pour représenter nos commentaires.

Pour les approches avec et sans authentification, notre modèle de contenu Commentaire restera principalement le même, bien qu'il y aura quelques changements ultérieurs au champ **Auteur**, comme indiqué ci-dessous.

### Le modèle de contenu Commentaire

C'est le modèle au cœur de notre système de commentaires. Les commentaires doivent avoir quatre champs :

![Image](https://cdn-media-1.freecodecamp.org/images/tp1JYhltz8FSFApiR5aS1XrwgQ-w1MSIZKbF)
_Le tableau de bord de Contentful_

**Corps**

* Le corps réel du commentaire
* Marquez celui-ci comme le titre de l'entrée
* N'hésitez pas à définir également une valeur maximale et/ou minimale pour sa longueur

**Auteur**

* Un identifiant unique représentant l'utilisateur qui a posté ce commentaire.
* Pour les commentaires sans authentification, vous utiliserez un texte court et remplirez le nom de l'auteur dans ce champ
* Pour les commentaires avec authentification, ce champ deviendra une référence au modèle CommentAuthor à venir

**Sujet**

* L'ID unique de l'article de blog (ou équivalent) auquel ces commentaires appartiennent
* Il peut également s'agir de l'URL de la page
* Pour une flexibilité maximale, j'ai choisi de ne pas supposer que vous stockez vos articles de blog dans Contentful, sinon ce serait un champ de référence au lieu de texte court

**CommentaireParent**

* Si ce commentaire est une réponse à un autre commentaire, nous référencerons ce commentaire ici
* Ce champ est ce qui nous permet de créer des commentaires imbriqués

### Implémentation des commentaires sans authentification

Pour cette implémentation, nous voulons que l'utilisateur entre son nom avant de pouvoir poster un commentaire. Je recommande de faire une première lecture des étapes suivantes, puis de consulter le projet de démonstration final à la fin pour voir comment tout cela s'assemble.

### Front-end

Maintenant que notre modèle Commentaire est terminé, il est temps de créer notre boîte de commentaires. La bonne nouvelle est que j'ai déjà créé un composant React "boîte de commentaires" générique. Il est conçu comme un composant **de bas niveau**, où vous enveloppez un composant **de haut niveau** autour de lui pour gérer la récupération et la création de commentaires Contentful, et d'autres logiques métiers spécifiques à l'application.

Vous pouvez l'installer ainsi que les autres packages requis via npm :

```
npm install react-commentbox contentful contentful-management --save
```

Le [dépôt GitHub](https://github.com/shaunpersad/react-commentbox) contient une liste de toutes les props que vous pouvez lui passer, mais au minimum, nous implémenterons et passerons celles-ci :

* `getComments` : une fonction qui retourne une promesse qui se résout en un tableau de commentaires, ordonnés du plus ancien au plus récent
* `normalizeComment` : une fonction qui mappe votre tableau de commentaires en objets que le composant comprend
* `comment` : une fonction qui fait un appel API pour créer un commentaire, et retourne une promesse
* `disabled` : défini sur true lorsque les commentaires doivent être désactivés
* `disabledComponent` : le composant à afficher lorsque les commentaires sont désactivés

Créons notre composant de haut niveau :

```
import React from 'react';import CommentBox from 'react-commentbox';
```

```
class MyCommentBox extends React.Component {
```

```
    state = { authorName: '', authorNameIsSet: false };
```

```
    onChangeAuthorName = (e) => this.setState({         authorName: e.currentTarget.value     });
```

```
    onSubmitAuthorName = (e) => {
```

```
        e.preventDefault();        this.setState({ authorNameIsSet: true });    };}
```

Remarquez que le composant est responsable de la définition du nom de l'auteur.

Au fait, nous utilisons le plugin Babel [transform-class-properties](https://babeljs.io/docs/plugins/transform-class-properties/) pour éviter une configuration fastidieuse du constructeur et des liaisons de fonctions. Vous n'avez pas besoin de l'utiliser, mais c'est assez pratique.

Maintenant, nous devons implémenter les props de logique métier dont `react-commentbox` a besoin.

Nous commencerons par récupérer les commentaires de Contentful, et les normaliser :

```
// récupérer nos commentaires de ContentfulgetComments = () => {
```

```
    return this.props.contentfulClient.getEntries({        'order': 'sys.createdAt',        'content_type': 'comment',        'fields.subject': this.props.subjectId,    }).then( response => {
```

```
        return response.items;
```

```
    }).catch(console.error);};
```

```
// transformer les entrées Contentful en objets que react-commentbox attend.normalizeComment = (comment) => {
```

```
    const { id, createdAt } = comment.sys;    const { body, author, parentComment } = comment.fields;
```

```
    return {        id,        bodyDisplay: body,        userNameDisplay: author,        timestampDisplay: createdAt.split('T')[0],        belongsToAuthor: false,        parentCommentId: parentComment ? parentComment.sys.id : null    };};
```

Ensuite, nous devons faire l'appel API pour créer des commentaires :

```
// faire un appel API pour poster un commentairecomment = (body, parentCommentId = null) => {
```

```
    return this.props.postData('/create-comment', {        body,        parentCommentId,        authorName: this.state.authorName,        subjectId: this.props.subjectId    });};
```

Nous devons également demander à l'utilisateur son nom avant qu'il puisse commenter :

```
// sera affiché lorsque la boîte de commentaires est initialement désactivéedisabledComponent = (props) => {
```

```
    return (        <form             className="author-name"             onSubmit{ this.onSubmitAuthorName }        >            <input                type="text"                placeholder="Entrez votre nom pour poster un commentaire"                value={ this.state.authorName }                onChange={ this.onChangeAuthorName }            />            <button type="submit">Soumettre</button>        </form>    );};
```

Ensuite, rassemblez le tout dans `render`, en passant les props appropriées à `react-commentbox` :

```
render() {
```

```
    return (        <div>            <h4>Commentaires</h4>            <CommentBox                disabled={ !this.state.authorNameIsSet }                getComments={ this.getComments }                normalizeComment={ this.normalizeComment }                comment={ this.comment }                disabledComponent={ this.disabledComponent }            />        </div>    );};
```

Nous avons également défini la prop `disabled` sur `true` tant que le nom de l'auteur n'est pas défini. Cela désactive la `textarea`, et affiche le formulaire `disabledComponent` que nous avons créé pour obtenir le nom de l'auteur.

Vous pouvez consulter le composant complet [ici](https://github.com/shaunpersad/authless-comments-example/blob/master/src/components/MyCommentBox.jsx).

Vous avez peut-être remarqué que notre `MyCommentBox` nouvellement créé attend également quelques props : `subjectId`, `postData`, et `contentfulClient`.

Le `subjectId` est simplement un identifiant unique ou une URL de l'article de blog (ou entité équivalente) auquel ces commentaires sont destinés.

`postData` est une fonction qui fait des appels ajax POST. En utilisant `fetch`, cela pourrait ressembler à ceci :

```
function postData(url, data) {
```

```
    return fetch(`.netlify/functions${url}`, {        body: JSON.stringify(data),        headers: {            'content-type': 'application/json'        },        method: 'POST',        mode: 'cors' // si vos endpoints sont sur un domaine différent    }).then(response => response.json());}
```

`contentfulClient` est une instance du client que vous obtenez lorsque vous utilisez le package npm [contentful](https://www.npmjs.com/package/contentful) (donc assurez-vous de l'avoir installé) :

```
import { createClient } from 'contentful';const contentfulClient = createClient({    space: 'my-space-id',    accessToken: 'my-access-token'});
```

Vous pouvez obtenir votre identifiant d'espace dans le tableau de bord de Contentful sous "Paramètres de l'espace" > "Paramètres généraux".

Vous pouvez obtenir votre jeton d'accès depuis "Paramètres de l'espace" > "Clés API" > "Jeton de livraison/prévisualisation du contenu" > "Ajouter une clé API".

Vous pouvez ensuite passer vos props lors de la création de `MyCommentBox`, comme montré [ici](https://github.com/shaunpersad/authless-comments-example/blob/master/src/components/App.jsx).

### Back-end

Nous allons implémenter notre endpoint `/create-comment` en tant que fonction AWS Lambda.

#### Prérequis

Pour pouvoir construire, prévisualiser et finalement déployer ces fonctions, nous allons utiliser le package npm pratique [netlify-lambda](https://www.npmjs.com/package/netlify-lambda). Il vous permet d'écrire vos fonctions Lambda en tant que fonctions ES6 régulières dans un répertoire source particulier, puis il les construit de manière compatible avec Lambda et les place dans un répertoire de destination, prêtes pour le déploiement. Mieux encore, il nous permet également de prévisualiser ces fonctions en les déployant localement.

Ainsi, vous devrez créer un répertoire source particulier pour stocker votre fonction (par exemple, `src/lambda`), puis créer un fichier `netlify.toml` dans votre répertoire racine. Minimalement, ce fichier devrait ressembler à ceci :

```
[build] Functions = "lambda"
```

Ce qui précède indique à `netlify-lambda` dans quel répertoire placer vos fonctions construites, ce qui signifie qu'il construira les fonctions dans `src/lambda` et les stockera dans `./lambda`. De plus, lorsqu'il sera temps de déployer, Netlify cherchera dans le répertoire `./lambda` pour déployer sur AWS.

Pour exécuter vos fonctions Lambda localement, utilisez la commande suivante :

```
netlify-lambda serve <source directory>
```

Cela vous permettra d'exécuter vos fonctions sur `[http://localhost:9000/{function-name}](http://localhost:9000/{function-name}.)`[.](http://localhost:9000/{function-name}.)

C'est le comportement par défaut, mais il ne correspond pas tout à fait à ce qui se passera en production, car il exécute nos fonctions sur un domaine différent de notre front-end. En production, nos fonctions seront disponibles sur le même domaine que notre front-end, via l'URL `{domain}/.netlify/functions/{function-name}`.

Pour reproduire ce comportement localement, nous devons proxyfier les appels front-end de `/.netlify/functions/{function-name}` vers `[http://localhost:9000/{function-name}](http://localhost:9000/{function-name}.)`[.](http://localhost:9000/{function-name}.)

La réalisation de cela diffère en fonction de la configuration de votre projet. Je vais couvrir deux configurations populaires :

Pour les projets [create-react-app](https://github.com/facebook/create-react-app), ajoutez ce qui suit à votre `package.json` :

```
"proxy": {        "/.netlify/functions": {        "target": "http://localhost:9000",        "pathRewrite": {            "^/\\.netlify/functions": ""        }    }}
```

Pour les projets [Gatsby.js](https://www.gatsbyjs.com/), ajoutez ce qui suit à votre `gatsby-config.js` :

```
const proxy = require('http-proxy-middleware');...developMiddleware: app => {    app.use(        '/.netlify/functions/',        proxy({            target: 'http://lambda:9000',            pathRewrite: {                '/.netlify/functions/': '',            }        })    );},
```

Pour la plupart des autres projets, vous pouvez utiliser le serveur de développement de webpack, qui dispose d'un [support de proxy](https://webpack.js.org/configuration/dev-server/#devserver-proxy).

#### Écriture de notre fonction

Avant de nous lancer dans l'écriture de code spécifique à Lambda, nous allons d'abord créer une fonction générique pour gérer la plupart de notre logique. De cette façon, notre code reste portable au-delà de Lambda.

Créons une fonction `createComment` :

```
const contentful = require('contentful-management');const client = contentful.createClient({    accessToken: process.env.CONTENTFUL_CONTENT_MANAGEMENT_ACCESS_TOKEN});
```

```
module.exports = function createComment(    body,     authorName,     subjectId,     parentCommentId = null) {
```

```
    return client.getSpace('my-space-id')        .then(space => space.getEnvironment('master'))        .then(environment => environment.createEntry('comment', {            fields: {                body: {                    'en-US': body                },                author: {                    'en-US': authorName                },                subject: {                    'en-US': subjectId                },                parentComment: {                    'en-US': {                        sys: {                            type: 'Link',                            linkType: 'Entry',                            id: parentCommentId                        }                    }                }            }        }))        .then(entry => entry.publish());};
```

Vous pouvez placer la fonction ci-dessus dans un répertoire comme `utils`. Elle utilise le package npm `[contentful-management](https://www.npmjs.com/package/contentful-management)` pour créer et publier une nouvelle entrée de commentaire, et retourne une promesse. Remarquez que nous avons spécifié notre clé API de gestion comme variable d'environnement. Vous ne voulez définitivement pas la coder en dur. Lorsque vous déployez sur Netlify ou ailleurs, assurez-vous que vos variables d'environnement sont définies.

Vous pouvez obtenir votre jeton d'accès de gestion depuis le tableau de bord de Contentful à "Paramètres de l'espace" > "Clés API" > "Jeton de gestion de contenu" > "Générer un jeton personnel".

Maintenant, créons notre fonction spécifique à Lambda :

```
const createComment = require('../utils/createComment');
```

```
exports.handler = function (event, context, callback) {
```

```
    const { body, authorName, subjectId, parentCommentId } = JSON.parse(event.body);
```

```
    createComment(body, authorName, subjectId, parentCommentId)        .then(entry => callback(null, {            headers: {                'Content-Type': 'application/json'            },            statusCode: 200,            body: JSON.stringify({ message: 'OK' })        }))        .catch(callback);};
```

Placez cette fonction dans votre répertoire source Lambda, et nommez le fichier avec le chemin que vous souhaitez pour l'URL, par exemple `create-comment.js`. Cela rendra votre fonction disponible à l'URL `/.netlify/functions/create-comment`.

### Le tableau d'ensemble

Pour illustrer notre configuration complète du front-end et du back-end jusqu'à présent, j'ai créé [un projet create-react-app](https://github.com/shaunpersad/authless-comments-example) qui fonctionne comme un exemple prêt à être déployé et entièrement fonctionnel.

Remarquez que dans le fichier `netlify.toml` du projet d'exemple, il y a quelques lignes supplémentaires que vous devriez ajouter à votre propre fichier. `Command` indique à Netlify quelles commandes exécuter pour construire le projet. `Publish` indique à Netlify où trouver les actifs statiques prêts pour le déploiement une fois la construction terminée. Vous pouvez en lire plus sur ce fichier dans la [documentation de Netlify](https://www.netlify.com/docs/netlify-toml-reference/).

Le projet d'exemple est également facilement clonable et déployable sur votre propre compte Netlify via le bouton de déploiement pratique dans le README.

Si vous avez été en train de l'implémenter dans votre propre projet, rendez-vous sur [le tableau de bord de Netlify](https://app.netlify.com/) et suivez leurs instructions simples pour configurer votre dépôt à déployer.

Une fois qu'il est opérationnel, vous pourrez commencer à commenter comme un chef.

(Note : ceci n'est qu'une capture d'écran, donc n'essayez pas de cliquer dessus ^_^)

![Image](https://cdn-media-1.freecodecamp.org/images/iIM89R0mRNjlfbmT1JIbnLTaJ-vnOliNirFf)

### Jusqu'à la prochaine fois

Dans la partie 2, nous aborderons l'implémentation des commentaires avec authentification, ainsi que l'ajout de fonctionnalités de formatage de texte super cool à notre boîte de commentaires.

Merci pour la lecture ! — Shaun

_Publié à l'origine sur [shaunasaservice.com](https://shaunasaservice.com/blog/build-your-own-free-serverless-comment-box-part-1-contentful-and-netlify/)._