---
title: Comment créer un Hook React personnalisé et le publier sur npm
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-04-14T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-custom-react-hook-and-publish-it-to-npm
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Custom-React-Hooks-Book-Cover--1-.png
tags:
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: hooks
  slug: hooks
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: npm scripts
  slug: npm-scripts
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: Yarn
  slug: yarn
seo_title: Comment créer un Hook React personnalisé et le publier sur npm
seo_desc: 'Hooks are a handy addition to the React API that allow us to organize some
  of our logic and state in function components. How can we build a custom hook and
  share it with the rest of the world?


  What are hooks?

  Why are custom hooks cool?

  What are we ...'
---

Les Hooks sont un ajout pratique à l'API React qui nous permet d'organiser une partie de notre logique et de notre état dans des composants fonctionnels. Comment pouvons-nous créer un Hook personnalisé et le partager avec le reste du monde ?

* [Qu'est-ce que les Hooks ?](#heading-questce-que-les-hooks)
* [Pourquoi les Hooks personnalisés sont-ils cool ?](#heading-pourquoi-les-hooks-personnalises-sont-ils-cool)
* [Que allons-nous créer ?](#heading-que-allons-nous-creer)
* [Étape 0 : Nommer votre Hook](#heading-etape-0-nommer-votre-hook)
* [Étape 1 : Configurer votre projet](#heading-etape-1-configurer-votre-projet)
* [Étape 2 : Écrire votre nouveau Hook React](#heading-etape-2-ecrire-votre-nouveau-hook-react)
* [Étape 3 : Utiliser votre Hook React dans un exemple](#heading-etape-3-utiliser-votre-hook-react-dans-un-exemple)
* [Étape 4 : Compiler votre Hook React et l'exemple](#heading-etape-4-compiler-votre-hook-react-et-lexemple)
* [Étape 5 : Publier votre Hook React sur npm](#heading-etape-5-publier-votre-hook-react-sur-npm)
* [Plus de ressources sur les Hooks](#heading-plus-de-ressources-sur-les-hooks)

%[https://www.youtube.com/watch?v=Q0xVnRanXVk]

## Qu'est-ce que les Hooks ?

Les [Hooks](https://reactjs.org/docs/hooks-intro.html) React, en termes simples, sont des fonctions. Lorsque vous les incluez dans votre composant ou dans un autre Hook, ils vous permettent d'utiliser les fonctionnalités internes de React et des parties du cycle de vie de React avec des Hooks natifs comme `useState` et `useEffect`.

Je ne prévois pas de faire une plongée profonde sur les Hooks, mais vous pouvez [consulter une introduction rapide](https://www.freecodecamp.org/news/how-to-destructure-the-fundamentals-of-react-hooks-d13ff6ea6871/) avec un exemple de `useState` ainsi que [l'introduction de l'équipe React](https://reactjs.org/docs/hooks-intro.html).

## Pourquoi les Hooks personnalisés sont-ils cool ?

Ce qui est génial avec la création de Hooks personnalisés, c'est qu'ils vous permettent d'abstraire la logique pour vos composants, ce qui facilite la réutilisation dans plusieurs composants de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/hook-example-use-counter-1.jpg)
_Exemple de diagramme de Hook pour useCounter_

Par exemple, si vous souhaitez créer un simple compteur où vous utilisez l'état de React pour gérer le compte actuel. Au lieu d'avoir le même Hook `useState` dans chaque fichier de composant, vous pouvez créer cette logique une fois dans un Hook `useCounter`, ce qui facilite la maintenance, l'extension et la correction des bugs s'ils surviennent.

## Que allons-nous créer ?

Pour les besoins de cet article, nous allons garder les choses simples avec un Hook de base. Typiquement, vous pourriez utiliser un Hook parce que, plutôt qu'une fonction typique, vous utilisez d'autres Hooks natifs qui doivent être utilisés dans les composants fonctionnels React. Nous allons nous en tenir à une entrée et une sortie de base pour garder les choses simples.

Nous allons recréer ce Hook personnalisé [Placecage](https://github.com/colbyfayock/use-placecage) que j'ai créé, qui vous permet de générer facilement des URLs d'images que vous pouvez utiliser comme images de remplissage.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/nic-cage-excited.gif)
_Nic Cage excité_

Si vous n'êtes pas familier, [Placecage](https://www.placecage.com/) est une API qui vous permet de générer des images de Nic Cage comme images de remplissage pour votre site web. Ridicule ? Oui. Amusant ? Absolument !

Mais si vous n'êtes pas fan du travail de Nic, vous pouvez tout aussi facilement remplacer l'URL par [Fill Murray](https://placeholder.com/) qui utilise des images de Bill Murray ou [placeholder.com](https://placeholder.com/) qui génère un fond de couleur unie simple avec du texte indiquant la taille de l'image.

## Étape 0 : Nommer votre Hook

Avant de plonger dans notre code réel, notre objectif ultime est de publier ce Hook. Si ce n'est pas votre objectif, vous pouvez sauter cette étape, mais pour la publication, nous voudrons créer un nom pour notre Hook.

Dans notre cas, le nom de notre Hook sera `usePlaceCage`. Maintenant, avec cela en tête, nous avons 2 formats pour notre nom — un en format camelCase et un en format snake-case.

* **camelCase** : usePlaceCage
* **snake-case** : use-placecage

Le format camelCase sera utilisé pour la fonction du Hook elle-même, tandis que le nom en snake-case sera utilisé pour le nom du package et certains dossiers. Lors de la création du nom, gardez à l'esprit que le nom du package doit être unique. Si un package avec le même nom existe déjà sur [npmjs.com](https://www.npmjs.com/), vous ne pourrez pas l'utiliser.

Si vous n'avez pas encore de nom, ce n'est pas grave ! Vous pouvez simplement utiliser votre propre nom ou quelque chose que vous pouvez imaginer, cela n'a pas vraiment d'importance car nous essayons simplement d'apprendre comment faire cela. Si c'était moi, par exemple, j'utiliserais :

* **camelCase** : useColbysCoolHook
* **snake-case** : use-colbyscoolhook

Mais juste pour clarifier, pour le reste de notre exemple, nous allons nous en tenir à `usePlaceCage` et `use-placecage`.

## Étape 1 : Configurer votre projet

Bien que vous puissiez configurer votre projet comme vous le souhaitez, nous allons passer en revue la création d'un nouveau Hook à partir de [ce modèle](https://github.com/colbyfayock/use-custom-hook) que j'ai créé.

L'espoir ici est que nous puissions éliminer certaines des parties pénibles du processus et devenir immédiatement productifs avec notre Hook personnalisé. Ne vous inquiétez pas, je vais expliquer ce qui se passe en cours de route.

Les exigences ici sont [git](https://git-scm.com/) et [yarn](https://yarnpkg.com/) car cela aide à fournir des outils qui facilitent l'échafaudage de ce modèle, comme l'utilisation de la fonctionnalité workspaces pour permettre des scripts npm faciles à gérer le code à partir de la racine du projet. Si l'un de ceux-ci est un problème, vous pouvez essayer de télécharger le dépôt via le lien de téléchargement et le mettre à jour selon vos besoins.

### Cloner le modèle de Hook depuis git

Pour commencer, clonons le dépôt depuis Github. Dans la commande ci-dessous, vous devez remplacer `use-my-custom-hook` par le nom de votre Hook, comme `use-cookies` ou `use-mooncake`.

```shell
git clone https://github.com/colbyfayock/use-custom-hook use-my-custom-hook
cd use-my-custom-hook

```

Une fois que vous avez cloné et navigué vers ce dossier, vous devriez maintenant voir 2 répertoires — un répertoire `example` et un répertoire `use-custom-hook`.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/cloning-use-custom-hook-1.jpg)
_Clonage de use-custom-hook_

Cela vous donnera quelques éléments pour commencer :

* Un répertoire de Hook qui inclura la source de notre Hook
* Des scripts de construction qui compilent notre Hook avec [babel](https://babeljs.io/)
* Une page d'exemple qui importe notre Hook et crée une simple page de démonstration avec [next.js](https://nextjs.org/)

### Exécuter les scripts de configuration du Hook

Après avoir cloné le dépôt avec succès, nous voulons exécuter les scripts de configuration qui installent les dépendances et mettent à jour le Hook avec le nom que nous voulons.

```shell
yarn install && yarn setup

```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/setting-up-new-hook-template.jpg)
_Configuration d'un nouveau Hook à partir du modèle use-custom-hook_

Lorsque le script de configuration s'exécute, il fait quelques choses :

* Il vous demande votre nom — cela est utilisé pour mettre à jour la LICENCE et le nom de l'auteur du package
* Il vous demande le nom de votre Hook dans 2 variations — camelCase et snake-case — cela sera utilisé pour mettre à jour le nom du Hook dans tout le modèle et déplacer les fichiers avec ce nom à l'emplacement correct
* Il réinitialise git — il supprime d'abord le dossier local .git, qui contient l'historique de mon modèle et réinitialise git avec un nouveau commit pour commencer votre nouvel historique
* Enfin, il supprime le répertoire du script de configuration et supprime les dépendances du package qui étaient uniquement utilisées par ces scripts

### Démarrer le serveur de développement

Une fois que les scripts de configuration ont fini de s'exécuter, vous voudrez exécuter :

```shell
yarn develop

```

Cela exécute un processus de surveillance sur la source du Hook, construisant le Hook localement chaque fois qu'un fichier source est modifié, et exécutant le serveur de l'application d'exemple, où vous pouvez tester le Hook et apporter des modifications aux pages d'exemple.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/custom-hook-development-server.jpg)
_Démarrage du serveur de développement use-custom-hook_

Avec tout cela prêt, nous pouvons commencer !

[Suivez le commit !](https://github.com/colbyfayock/use-my-custom-hook/commits/master)

## Étape 2 : Écrire votre nouveau Hook React

À ce stade, vous devriez maintenant avoir un nouveau Hook personnalisé où vous pouvez le faire faire ce que vous voulez. Mais puisque nous allons passer en revue la reconstruction du Hook [usePlaceCage](https://github.com/colbyfayock/use-placecage), commençons par là.

Le Hook usePlaceCage fait une chose simple à haut niveau — il prend un objet de configuration et retourne un certain nombre d'URLs d'images que vous pouvez ensuite utiliser pour votre application.

Juste pour rappel, chaque fois que je mentionne `usePlaceCage` ou `use-placecage`, vous devez utiliser le nom du Hook que vous avez configuré précédemment.

### Un peu sur placecage.com

Placecage.com est un service d'images de remplissage qui fait une chose. Il prend une URL avec une configuration simple et retourne une image... de Nic Cage.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/placecage-website.jpg)
_placecage.com_

De l'utilisation la plus simple, le service utilise un modèle d'URL comme suit :

```
https://www.placecage.com/200/300

```

Cela retournerait une image avec une largeur de 200 et une hauteur de 300.

Optionnellement, vous pouvez passer un paramètre d'URL supplémentaire qui définit le type d'image :

```
https://www.placecage.com/gif/200/300

```

Dans ce cas particulier, notre type est `gif`, donc nous recevrons un gif.

Les différents types disponibles à utiliser sont :

* Rien : calme
* `g` : gris
* `c` : fou
* `gif` : gif

Nous allons utiliser cela pour définir comment nous configurons notre Hook.

### Définir notre fonction génératrice principale

Pour commencer, nous allons copier une fonction en bas de notre fichier `use-placecage/src/usePlaceCage.js`, qui nous permet de générer une URL d'image, ainsi que quelques définitions de constantes que nous utiliserons dans cette fonction.

Tout d'abord, copions nos constantes en haut de notre fichier `usePlaceCage.js` :

```js
const PLACECAGE_HOST = 'https://www.placecage.com/';
const TYPES = {
  calm: null,
  gray: 'g',
  crazy: 'c',
  gif: 'gif'
};
const DEFAULT_TYPE = 'calm';
const ERROR_BASE = 'Failed to place Nick';

```

Ici nous :

* Définissons un hôte, qui est l'URL de base de notre service d'images.
* Définissons les types disponibles, que nous utiliserons dans l'API de configuration. Nous définissons `calm` à `null`, car c'est la valeur par défaut que vous obtenez en ne l'incluant pas du tout
* Notre type par défaut sera `calm`
* Et nous définissons une base d'erreur qui est un message cohérent lors du lancement d'une erreur

Ensuite, pour notre fonction, copions ceci en bas de notre fichier `usePlaceCage.js` :

```js
function generateCage(settings) {
  const { type = DEFAULT_TYPE, width = 200, height = 200, count = 1 } = settings;
  const config = [];
    
  if ( type !== DEFAULT_TYPE && TYPES[type] ) {
    config.push(TYPES[type]);
  }
    
  config.push(width, height);
    
  if ( isNaN(count) ) {
    throw new Error(`${ERROR_BASE}: Invalid count ${count}`);
  }
    
  return [...new Array(count)].map(() => `${PLACECAGE_HOST}${config.join('/')}`);
}

```

En parcourant ce code :

* Nous définissons une fonction `generateCage` que nous utiliserons pour générer notre URL d'image
* Nous prenons un objet de paramètres comme argument, qui définit la configuration de notre URL d'image. Nous utiliserons les mêmes paramètres que nous avons vus dans notre URL placecage.com
* Nous déstructurons ces paramètres pour les rendre disponibles pour nous
* Nous avons quelques valeurs par défaut ici juste pour faciliter les choses. Notre `type` par défaut sera défini par `DEFAULT_TYPE` ainsi qu'une largeur, une hauteur et un nombre de résultats par défaut que nous voulons retourner
* Nous créons un tableau `config`. Nous allons utiliser cela pour ajouter tous les différents objets de configuration dans notre URL et enfin les joindre ensemble avec un `/` en faisant essentiellement une URL
* Avant de pousser notre config dans ce tableau, nous vérifions si c'est un argument valide, en utilisant l'objet `TYPES` pour vérifier contre lui. Si c'est valide, nous le poussons dans notre tableau de config
* Nous poussons ensuite notre largeur et notre hauteur
* Nous faisons un peu de vérification de type, si nous n'avons pas un nombre valide comme `count`, nous lançons une erreur, sinon nous obtiendrons des résultats incorrects
* Enfin, nous retournons un nouveau tableau avec le nombre de résultats demandés, mappé à un créateur d'URL, qui utilise `PLACECAGE_HOST` comme notre URL de base définie, et avec notre tableau de config joint par `/`

Et si nous devions tester cette fonction, cela ressemblerait à ceci :

```js
const cage = generateCage({
  type: 'gif',
  width: 500,
  height: 500,
  count: 2
});

console.log(cage); // ['https://www.placecage.com/gif/500/500', 'https://www.placecage.com/gif/500/500']
```

### Utiliser notre fonction dans le Hook

Maintenant que nous avons notre fonction génératrice, utilisons-la dans notre Hook !

À l'intérieur de la fonction `usePlaceCage` dans le fichier `use-placecage/src/usePlaceCage.js`, nous pouvons ajouter :

```js
export default function usePlaceCage (settings = {}) {
  return generateCage(settings);
}

```

Ce que cela fait, c'est utiliser notre fonction génératrice, prendre les paramètres qui ont été passés au Hook, et retourner cette valeur depuis le Hook.

Similaire à notre exemple d'utilisation précédent, si nous devions utiliser notre Hook, cela ressemblerait à ceci :

```js
const cage = usePlaceCage({
  type: 'gif',
  width: 500,
  height: 500,
  count: 2
});

console.log(cage); // ['https://www.placecage.com/gif/500/500', 'https://www.placecage.com/gif/500/500']

```

À ce stade, cela fait la même chose !

Nous avons donc notre Hook, il sert de fonction pour générer des URLs d'images pour le service placecage.com. Comment pouvons-nous l'utiliser réellement ?

[Suivez le commit !](https://github.com/colbyfayock/use-my-custom-hook/commit/a4d4d3c3565759031c29d00faf731ac4c236a1fd)

## Étape 3 : Utiliser votre Hook React dans un exemple

La bonne nouvelle concernant notre modèle, c'est qu'il inclut déjà une application d'exemple que nous pouvons mettre à jour pour utiliser facilement notre Hook afin de le tester et de fournir une documentation pour ceux qui veulent l'utiliser.

### Configurer le Hook

Pour commencer, ouvrons notre fichier `example/pages/index.js`. À l'intérieur de ce fichier, vous verrez ce qui suit :

```js
const hookSettings = {
  message: 'Hello, custom hook!'
}

const { message } = usePlaceCage(hookSettings);

```

Ce snippet était utilisé par défaut dans le modèle juste pour une preuve de concept, alors mettons-le à jour. Nous allons utiliser la même configuration exacte que nous avons utilisée dans l'Étape 2 :

```js
const hookSettings = {
  type: 'gif',
  width: 500,
  height: 500,
  count: 2
}

const cage = usePlaceCage(hookSettings);

```

Encore une fois, nous configurons notre objet de paramètres avec la configuration pour notre Hook et invoquons notre Hook et définissons la valeur à la constante `cage`.

Si nous affichons maintenant cette valeur dans nos outils de développement, nous pouvons voir qu'elle fonctionne !

```js
console.log('cage', cage);

```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/console-log-cage-array.jpg)
_Utilisation de console.log pour afficher la valeur de cage_

_Note : Si vous obtenez une erreur ici concernant `message`, vous pouvez commenter cela ou le supprimer sous la section Exemples._

### Mettre à jour l'exemple avec notre nouvelle configuration de Hook

Si vous faites défiler jusqu'à la section Exemples, vous remarquerez que nous avons les mêmes `hookSettings` par défaut que ci-dessus, alors mettons cela à jour à nouveau pour nous assurer que notre exemple est précis.

```jsx
{`const hookSettings = {
  type: 'gif',
  width: 500,
  height: 500,
  count: 2
}

const cage = usePlaceCage(hookSettings);`}

```

Vous remarquerez également que nous n'utilisons plus la variable `message`. Si vous ne l'avez pas supprimée à l'étape précédente, nous pouvons maintenant la remplacer sous l'en-tête Output avec :

```jsx
<p>
  { JSON.stringify(cage) }
</p>
<p>
  { cage.map((img, i) => <img key={`img-${i}`} width={200} src={img} />)}
</p>

```

Nous faisons 2 choses ici :

* Au lieu d'afficher la variable elle-même, nous l'enveloppons avec `JSON.stringify` afin de pouvoir afficher le contenu du tableau
* Nous utilisons également la fonction `map` pour parcourir nos URLs d'images dans la constante `cage` et créer un nouvel élément image pour chacune. Cela nous permet de prévisualiser la sortie au lieu de simplement voir les valeurs

Et une fois que vous avez enregistré et ouvert votre navigateur, vous devriez maintenant voir vos exemples et votre sortie mis à jour !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/custom-hook-example-page.jpg)
_Page d'exemple de Hook personnalisé_

### Autres choses que vous pouvez faire sur cette page

Avant de continuer, vous pouvez également mettre à jour quelques autres choses qui seront importantes pour la page de vos Hooks :

* Mettre à jour la section **Comment utiliser** avec des instructions
* Ajouter des exemples supplémentaires pour faciliter la compréhension des utilisateurs

Quelques éléments sont également automatiquement extraits du fichier `use-placecage/package.json`. Vous pouvez soit les mettre à jour là pour faciliter la maintenance, soit les remplacer dans la page d'exemple :

* `name` : Utilisé comme `<h1>` de la page
* `description` : Utilisé comme description sous le `<h1>`
* `repository.url` : Utilisé pour inclure un lien vers le dépôt
* `author` : Le `name` et `url` sont utilisés pour inclure un lien en bas de la page

[Suivez le commit !](https://github.com/colbyfayock/use-my-custom-hook/commit/71ae57b562ad814d0ce862c22e247aa8c450b6cf)

## Étape 4 : Compiler votre Hook React et l'exemple

La manière dont nous pouvons faire fonctionner notre Hook facilement en tant que module npm est de le compiler pour que d'autres puissent l'utiliser. Nous utilisons babel pour cela.

Bien que le processus de publication le fasse déjà automatiquement pour nous avec le script `prepublishOnly` dans `use-placecage/package.json`, nous pouvons compiler manuellement notre Hook en utilisant la commande `yarn build` depuis la racine du projet.

En plus de compiler le Hook, l'exécution de `yarn build` compilera également la page d'exemple, vous permettant de la télécharger où vous le souhaitez. Après avoir exécuté cette commande, vous devriez voir une sortie de fichiers HTML statiques dans le répertoire `example/out`.

Si vous cherchez une recommandation, [Netlify](https://www.netlify.com/) facilite la connexion de votre compte [Github](https://github.com/) et le déploiement du site statique.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/netlify-deployment-setup.jpg)
_Configuration du déploiement dans Netlify_

[Voir le site de démonstration déployé sur Netlify !](https://use-my-custom-hook.netlify.com/)

## Étape 5 : Publier votre Hook React sur npm

Enfin, si vous êtes satisfait de votre Hook, il est temps de le publier !

npm rend cette partie vraiment facile. Le seul prérequis est d'avoir un compte npm. Avec ce compte, connectons-nous :

```shell
npm login

```

Ce qui vous demandera vos identifiants de connexion.

Ensuite, naviguons vers le répertoire de notre Hook, car notre configuration de package s'y trouve sous `use-placecage/package.json` :

```shell
cd use-placecage

```

Ensuite, nous pouvons simplement publier !

```shell
npm publish

```

Gardez à l'esprit que chaque nom de package doit être unique. Si vous avez utilisé `use-placecage`, il est déjà pris... par moi. ?

Mais si vous réussissez, npm devrait construire votre Hook et le télécharger sur le registre des packages !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/publishing-npm-package.jpg)
_Publication d'un package npm_

Il sera alors disponible sur npm avec le modèle suivant :

```
https://www.npmjs.com/package/[package-name]

```

Donc pour `use-placeage`, il est disponible ici : [https://www.npmjs.com/package/use-placecage](https://www.npmjs.com/package/use-placecage)

## Nous avons maintenant un Hook personnalisé !

Yay ? si vous avez suivi, vous devriez maintenant avoir créé un Hook personnalisé et l'avoir publié sur npm.

Bien que ce soit un exemple amusant utilisant placecage.com, cela nous donne une bonne idée de la manière dont nous pouvons facilement configurer cela.

Vous remarquerez également que cet exemple spécifique n'était pas le meilleur cas d'utilisation pour des Hooks, où nous aurions pu simplement utiliser une fonction. Typiquement, nous voudrons utiliser des Hooks personnalisés pour envelopper des fonctionnalités qui ne peuvent vivre qu'à l'intérieur d'un composant React, comme `useState`. Pour en savoir plus à ce sujet, vous pouvez lire un de mes autres [articles sur les Hooks personnalisés](https://www.freecodecamp.org/news/how-to-destructure-the-fundamentals-of-react-hooks-d13ff6ea6871/).

Cependant, cela nous a donné une bonne base pour discuter de la création et de la configuration de notre nouveau Hook !

## Plus de ressources sur les Hooks

* [Comment déstructurer les fondamentaux des Hooks React](https://www.freecodecamp.org/news/how-to-destructure-the-fundamentals-of-react-hooks-d13ff6ea6871/) (freecodecamp.org)
* [Introduction aux Hooks](https://reactjs.org/docs/hooks-intro.html) (reactjs.org)
* [Référence de l'API des Hooks](https://reactjs.org/docs/hooks-reference.html) (reactjs.org)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>