---
title: Comment créer un beau petit package npm et le publier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T15:50:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-beautiful-tiny-npm-package-and-publish-it-2881d4307f78
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7m8mTkj_Fp916sdm
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer un beau petit package npm et le publier
seo_desc: 'By Jonathan Wood

  You won’t believe how easy it is!

  If you’ve created lots of npm modules, you can skip ahead. Otherwise, we’ll go through
  a quick intro.

  TL;DR

  An npm module only requires a package.json file with name and version properties.

  Hey!

  Ther...'
---

Par Jonathan Wood

Vous ne croirez pas à quel point c'est facile !

Si vous avez déjà créé beaucoup de modules npm, vous pouvez passer à la suite. Sinon, nous allons faire un rapide tour d'horizon.

#### TL;DR

Un module npm **nécessite uniquement** un fichier package.json avec les propriétés **name** et **version**.

### Hé !

Te voilà.

Juste un petit éléphant avec toute la vie devant toi.

Tu n'es pas expert en création de packages npm, mais tu aimerais apprendre comment faire.

Tous les grands éléphants piétinent avec leurs gros pieds, créant package après package, et toi tu es là comme :

> « Je ne peux pas rivaliser avec ça. »

Eh bien, je suis là pour te dire que tu peux !

Plus de doutes sur toi-même.

Commençons !

#### Tu n'es pas un éléphant

Je parlais [métaphoriquement](https://www.merriam-webster.com/dictionary/metaphorical).

Tu t'es déjà demandé comment on appelait les bébés éléphants ?

_Bien sûr que oui._ Un bébé éléphant s'appelle un [veau](https://www.reference.com/pets-animals/baby-elephant-called-a3893188e0a63095).

#### Je crois en toi

Le [doute de soi](https://en.wikipedia.org/wiki/Impostor_syndrome) est réel.

C'est pourquoi personne ne fait jamais rien de cool.

Tu penses que tu ne réussiras pas, alors au lieu de cela, tu ne fais rien. Mais ensuite, tu glorifies les personnes qui font toutes ces choses géniales.

Super ironique.

C'est pourquoi je vais te montrer le plus petit module npm possible.

Bientôt, tu auras des hordes de modules npm qui sortiront de tes doigts. Du code réutilisable à perte de vue. Pas de trucs — pas d'instructions complexes.

### Les instructions complexes

J'avais promis que je ne le ferais pas...

...mais je l'ai totalement fait.

Elles ne sont pas si mauvaises. Tu me pardonneras un jour.

#### **Étape 1 : compte npm**

Tu en as besoin. C'est juste partie du deal.

[Inscription ici](https://www.npmjs.com/signup).

#### Étape 2 : connexion

As-tu créé un compte npm ?

Oui, tu l'as fait.

Cool.

Je suppose aussi que tu sais utiliser la [ligne de commande / console](https://www.davidbaumgold.com/tutorials/command-line/) etc. Je vais l'appeler le terminal à partir de maintenant. Il y a une différence [apparemment](https://superuser.com/questions/144666/what-is-the-difference-between-shell-console-and-terminal).

Va dans ton terminal et tape :

```bash
npm adduser
```

Tu peux aussi utiliser la commande :

```bash
npm login
```

Choisis la commande qui te convient le mieux.

Tu auras une invite pour ton **nom d'utilisateur**, **mot de passe** et **email**. Mets-les là-dedans !

Tu devrais recevoir un message similaire à celui-ci :

```
Connecté en tant que bamblehorse au scope @username sur https://registry.npmjs.org/.
```

Bien !

### Créons un package

D'abord, nous avons besoin d'un dossier pour contenir notre code. Crée-en un de la manière qui te convient. J'appelle mon package **tiny** parce qu'il est vraiment très petit. J'ai ajouté quelques commandes de terminal pour ceux qui ne sont pas familiers avec elles.

```bash
md tiny
```

Dans ce dossier, nous avons besoin d'un fichier [**package.json**](https://docs.npmjs.com/files/package.json). Si tu utilises déjà [Node.js](https://en.wikipedia.org/wiki/Node.js) — tu as déjà rencontré ce fichier. C'est un fichier [JSON](https://en.wikipedia.org/wiki/JSON) qui inclut des informations sur ton projet et qui a une pléthore d'options différentes. Dans ce tutoriel, nous allons nous concentrer uniquement sur deux d'entre elles.

```bash
cd tiny && touch package.json
```

#### À quel point peut-il être petit, vraiment ?

Très petit.

Tous les tutoriels sur la création d'un package npm, y compris la documentation officielle, te disent d'entrer certains champs dans ton package.json. Nous allons essayer de publier notre package avec le moins possible jusqu'à ce que cela fonctionne. C'est une sorte de [TDD](https://en.wikipedia.org/wiki/Test-driven_development) pour un package npm minimal.

**Veuillez noter :** Je te montre cela pour démontrer que la création d'un package npm n'a pas à être compliquée. Pour être utile à la communauté en général, un package a besoin de quelques extras, et nous en parlerons plus tard dans l'article.

#### Publication : Première tentative

Pour publier ton package npm, tu exécutes la commande bien nommée : **npm publish.**

Nous avons donc un package.json vide dans notre dossier et nous allons essayer :

```bash
npm publish
```

Oups !

Nous avons obtenu une erreur :

```
npm ERR! file package.json
npm ERR! code EJSONPARSE
npm ERR! Failed to parse json
npm ERR! Unexpected end of JSON input while parsing near ''
npm ERR! File: package.json
npm ERR! Failed to parse package.json data.
npm ERR! package.json must be actual JSON, not just JavaScript.
npm ERR!
npm ERR! Tell the package author to fix their package.json file. JSON.parse
```

npm n'aime pas beaucoup cela.

C'est compréhensible.

#### Publication : Deuxième essai

Donnons un nom à notre package dans le fichier package.json :

```json
{
"name": "@bamlehorse/tiny"
}
```

Tu as peut-être remarqué que j'ai ajouté mon nom d'utilisateur npm au début.

De quoi s'agit-il ?

En utilisant le nom **@bamblehorse/tiny** au lieu de simplement **tiny**, nous créons un package sous le **scope** de notre nom d'utilisateur. C'est ce qu'on appelle un [**package scopé**](https://docs.npmjs.com/misc/scope). Cela nous permet d'utiliser des noms courts qui pourraient déjà être pris, par exemple le package [**tiny**](https://www.npmjs.com/package/tiny) existe déjà dans npm.

Tu as peut-être vu cela avec des bibliothèques populaires comme le [Framework Angular](https://angular.io/) de Google. Ils ont quelques packages scopés comme [@angular/core](https://www.npmjs.com/package/@angular/core) et [@angular/http](https://www.npmjs.com/package/@angular/http).

Plutôt cool, non ?

Nous allons essayer de publier une deuxième fois :

```bash
npm publish
```

L'erreur est plus petite cette fois-ci — progrès.

```
npm ERR! package.json requires a valid "version" field
```

Chaque package npm a besoin d'une version pour que les développeurs sachent s'ils peuvent mettre à jour en toute sécurité vers une nouvelle version de ton package sans casser le reste de leur code. Le système de versionnage utilisé par npm s'appelle [**SemVer**](https://semver.org/), qui signifie **Semantic Versioning**.

Ne t'inquiète pas trop de comprendre les noms de version plus complexes, mais voici leur résumé de la manière dont les versions de base fonctionnent :

> Étant donné un numéro de version MAJOR.MINOR.PATCH, incrémente le :

> 1. MAJOR version lorsque tu fais des changements incompatibles dans l'API,

> 2. MINOR version lorsque tu ajoutes des fonctionnalités de manière rétrocompatible, et

> 3. PATCH version lorsque tu fais des corrections de bugs rétrocompatibles.

> Des étiquettes supplémentaires pour les pré-versions et les métadonnées de build sont disponibles en tant qu'extensions au format MAJOR.MINOR.PATCH.

> [https://semver.org](https://semver.org)

#### **Publication : Troisième essai**

Nous allons donner à notre package.json la version : **1.0.0** — la première version majeure.

```json
{
"name": "@bamblehorse/tiny",
"version": "1.0.0"
}
```

Publions !

```bash
npm publish
```

Oh zut.

```
npm ERR! publish Failed PUT 402npm ERR! code E402npm ERR! You must sign up for private packages : @bamblehorse/tiny
```

Permets-moi de t'expliquer.

Les packages scopés sont automatiquement publiés en privé car, en plus d'être utiles pour des utilisateurs individuels comme nous, ils sont également utilisés par des entreprises pour partager du code entre projets. Si nous avions publié un package normal, alors notre voyage se terminerait ici.

Tout ce que nous devons changer, c'est de dire à npm que nous voulons en réalité que tout le monde utilise ce module — et non le garder enfermé dans leurs coffres. Donc, au lieu de cela, nous exécutons :

```bash
npm publish --access=public
```

Boom !

```
+ @bamblehorse/tiny@1.0.0
```

Nous recevons un signe plus, le nom de notre package et la version.

Nous l'avons fait — nous sommes dans le club npm.

Je suis excité.

_Tu dois être excité._

![Image](https://cdn-media-1.freecodecamp.org/images/1*oBaHFxAXy-BWtzyAKeMGBQ.png)
_redacted in a friendly blue_

#### As-tu saisi cela ?

> npm t'aime

Mignon !

La [version un](https://www.npmjs.com/package/@bamblehorse/tiny/v/1.0.0) est sortie !

### Faisons le point

Si nous voulons être pris au sérieux en tant que développeur, et si nous voulons que notre package soit utilisé, nous devons montrer le code aux gens et leur dire comment l'utiliser. Généralement, nous le faisons en mettant notre code quelque part en public et en ajoutant un fichier readme.

Nous avons aussi besoin de code.

Sérieusement.

Nous n'avons encore aucun code.

GitHub est un excellent endroit pour mettre ton code. Créons un [nouveau dépôt](https://github.com/new).

![Image](https://cdn-media-1.freecodecamp.org/images/1*NGHjzcMgnzBtmSFfQuqVow.png)

#### README !

Je me suis habitué à taper **README** au lieu de **readme.**

Tu n'as plus à faire cela.

C'est une convention amusante.

Nous allons ajouter quelques badges funky de [shields.io](https://shields.io/) pour que les gens sachent que nous sommes super cool et professionnels.

En voici un qui permet aux gens de connaître la version actuelle de notre package :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZbzgGAfTeBlqNH2gtLy-GQ.png)
_npm (scoped)_

Ce badge suivant est intéressant. Il a échoué parce que nous n'avons en réalité aucun code.

Nous devrions vraiment écrire du code...

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxZkgckYLK16mhkRte1Bqw.png)
_npm bundle size (minified)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*gY_-15Q4rLU129dXLg5ibQ.png)
_Notre petit readme_

#### Licence pour coder

Ce titre est définitivement une [référence à James Bond](https://www.imdb.com/title/tt0097742/).

J'ai en fait oublié d'ajouter une licence.

Une licence informe simplement les gens dans quelles situations ils peuvent utiliser ton code. Il en existe [beaucoup de différentes](https://choosealicense.com/).

Il y a une page cool appelée insights dans chaque dépôt GitHub où tu peux vérifier diverses statistiques — y compris les normes de la communauté pour un projet. Je vais ajouter ma licence à partir de là.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hkUyteXGLLTDt0WwKEpZ6A.png)
_Recommandations de la communauté_

Ensuite, tu arrives sur cette page :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZWgFtTjkB8RpBDfRsCsLUQ.png)
_GitHub te donne un résumé utile de chaque licence_

#### Le Code

Nous n'avons toujours aucun code. C'est légèrement embarrassant.

Ajoutons-en maintenant avant de perdre toute crédibilité.

```js
module.exports = function tiny(string) {
  if (typeof string !== "string") throw new TypeError("Tiny veut une chaîne de caractères !");
  return string.replace(/\s/g, "");
};
```

Le voilà.

Une fonction **tiny** qui supprime tous les espaces d'une chaîne de caractères.

Donc tout ce dont un package npm a besoin, c'est d'un fichier **index.js**. C'est le point d'entrée de ton package. Tu peux le faire de différentes manières à mesure que ton package devient plus complexe.

Mais pour l'instant, c'est tout ce dont nous avons besoin.

### **Y sommes-nous presque ?**

Nous sommes si proches.

Nous devrions probablement mettre à jour notre **package.json** minimal et ajouter quelques instructions à notre **readme.md**.

Sinon, personne ne saura comment utiliser notre beau code.

#### package.json

```json
{
  "name": "@bamblehorse/tiny",
  "version": "1.0.0",
  "description": "Supprime tous les espaces d'une chaîne de caractères",
  "license": "MIT",
  "repository": "bamblehorse/tiny",
  "main": "index.js",
  "keywords": [
    "tiny",
    "npm",
    "package",
    "bamblehorse"
  ]
}
```

Nous avons ajouté :

* [description](https://docs.npmjs.com/files/package.json#description-1) : une courte description du package
* [repository](https://docs.npmjs.com/files/package.json#repository) : compatible GitHub — donc tu peux écrire **username/repo**
* [license](https://docs.npmjs.com/files/package.json#license) : MIT dans ce cas
* [main](https://docs.npmjs.com/files/package.json#main) : le point d'entrée de ton package, relatif à la racine du dossier
* [keywords](https://docs.npmjs.com/files/package.json#keywords) : une liste de mots-clés utilisés pour découvrir ton package dans la recherche npm

#### readme.md

<script src="https://gist.github.com/Bamblehorse/4fc0c46138a738b29141209c8fd7197d.js"></script>

Nous avons ajouté des instructions sur la façon d'installer et d'utiliser le package. Bien !

Si tu veux un bon modèle pour ton readme, regarde simplement les packages populaires dans la communauté open source et utilise leur format pour te lancer.

### Terminé

Publions notre package spectaculaire.

#### Version

D'abord, nous allons mettre à jour la version avec la commande [npm version](https://docs.npmjs.com/cli/version).

C'est une version majeure, donc nous tapons :

```bash
npm version major
```

Ce qui donne :

```
v2.0.0
```

#### Publions !

Exécutons notre nouvelle commande préférée :

```bash
npm publish
```

C'est fait :

```
+ @bamblehorse/tiny@2.0.0
```

### Trucs cool

[Package Phobia](https://packagephobia.now.sh/result?p=%40bamblehorse%2Ftiny) te donne un excellent résumé de ton package npm. Tu peux aussi vérifier chaque fichier sur des sites comme [Unpkg](https://unpkg.com/@bamblehorse/tiny@2.0.0/).

### Merci

Ce fut un merveilleux voyage que nous venons de faire. J'espère que tu l'as apprécié autant que moi.

Fais-moi savoir ce que tu en as pensé !

Étoile le package que nous venons de créer ici :

#### **⭐ [Github.com/Bamblehorse/tiny](https://github.com/Bamblehorse/tiny) ⭐**

![Image](https://cdn-media-1.freecodecamp.org/images/0*qmkE3zw9beF6fP_0)
_« Un éléphant partiellement submergé dans l'eau. » par [Unsplash](https://unsplash.com/@jakobowens1?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jakob Owens</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Suis-moi sur [Twitter](https://twitter.com/Bamblehorse), [Medium](https://medium.com/@Bamblehorse) ou [GitHub](https://github.com/Bamblehorse)