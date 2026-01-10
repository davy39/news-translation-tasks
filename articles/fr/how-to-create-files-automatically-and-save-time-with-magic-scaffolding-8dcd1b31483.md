---
title: Comment créer des fichiers automatiquement et gagner du temps avec l'échafaudage
  magique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T19:47:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-files-automatically-and-save-time-with-magic-scaffolding-8dcd1b31483
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4xIsUwu1lTMXm0IZ
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment créer des fichiers automatiquement et gagner du temps avec l'échafaudage
  magique
seo_desc: 'By Jonathan Wood

  Before we begin: This article uses JavaScript / Node.js example code, but you can
  port these concepts to any language using the right tools.

  An exciting intro

  Do you ever find yourself creating the same files over and over again in y...'
---

Par Jonathan Wood

**Avant de commencer :** Cet article utilise des exemples de code JavaScript / Node.js, mais vous pouvez porter ces concepts dans n'importe quel langage en utilisant les bons outils.

### Une introduction excitante

**Créez-vous souvent les mêmes fichiers encore et encore dans vos projets ?**

Moi aussi.

#### Mes doigts me font mal !

Je ne suis pas surpris. Vous prenez le travail des robots.

Créer les mêmes fichiers répétitivement est ennuyeux et inutile.

#### TLDR ? Je vous ai compris — Voici une démonstration

![Image](https://cdn-media-1.freecodecamp.org/images/1*DVXreOfKQqtyY4CfLxiJ8w.gif)
_Automation magique — comme promis._

#### Montrez-moi le code

Je respecte votre sens de l'urgence — je vais aller droit au but.

### Le Code

Nous voulons automatiser la création de fichiers — c'est pour cela que vous êtes tous là aujourd'hui. D'abord, nous devons identifier les fichiers que nous voulons créer.

J'ai créé beaucoup de composants React récemment, donc ma configuration tourne autour de cela — mais vous pouvez ajuster cela pour littéralement n'importe quoi.

J'ai divisé cela en quatre étapes. Je vous le dis maintenant pour que vous puissiez gérer vos attentes. Si vous ne pouvez pas gérer plus de trois étapes, alors nous sommes dans le pétrin...

#### Étape 1 : Modèles

Configurez-les une fois et profitez-en.

Nous avons besoin de modèles. J'ai utilisé les [Template Literals](https://developers.google.com/web/updates/2015/01/ES6-Template-Strings), mais faites-le de la manière qui vous semble logique — soyez créatif.

Ce sont les fichiers que je crée chaque fois que je fais un composant React :

1. **index.jsx**
2. **{Component}.test.js**
3. **{Component}.sass**

**Note :** {Component} implique une [interpolation de chaîne](https://en.wikipedia.org/wiki/String_interpolation#Examples).

Je teste avec [Jest](https://jestjs.io/docs/en/tutorial-react), et j'utilise le modèle [create-react-app](https://github.com/facebook/create-react-app). Je sais que beaucoup de gens préfèrent [CSS-in-JS](https://alligator.io/react/css-in-js-roundup-styling-react-components/) ces jours-ci — mais bon. Faites-moi savoir dans les commentaires ce que vous utilisez.

En tout cas — C'est parti :

```js
const templates = {
  
  index: name => `// @flow
import React from 'react';
import './${name}.css';
// TODO: écrire le reste du composant ${name}
const ${name} = () => (
  <div className="${name.toLowerCase()}">
    <span>reste du composant</span>
  </div>
);
export default ${name};`,
  
  test: name => `// TODO: TDD
import { shallow, render } from 'enzyme';
import renderer from 'react-test-renderer';
import React from 'react';
import ${name} from '.';
const component = <${name} />;
describe('Le composant ${name}', () => {
  it('rend correctement', () => {
    const wrapper = render(component);
    expect(wrapper.hasClass('${name.toLowerCase()}')).toBeTruthy();
    const tree = renderer.create(component).toJSON();
    expect(tree).toMatchSnapshot();
  });
});`,
  
  sass: name => `.${name.toLowerCase()}
  background: initial`,
};
```

C'est le morceau de code le plus désordonné que vous verrez ici — promis.

Donc, nous avons un objet avec trois propriétés : index, test, et sass. Chacune héberge une fonction qui prend un nom et retourne un modèle avec ce nom interpolé. Cela semble légitime.

#### Étape 2 : Créons quelques fonctions !

Nous utilisons le [module fs](https://nodejs.org/api/fs.html#fs_file_system) fourni avec Node. Il est fabuleux. Il fait beaucoup de choses.

Nous allons utiliser quelques [fonctions fléchées](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) et un peu de [programmation fonctionnelle](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/). Ne soyez pas effrayé — suivez simplement.

La syntaxe de la double fonction fléchée s'appelle [currying](https://stackoverflow.com/questions/32782922/what-do-multiple-arrow-functions-mean-in-javascript). Ce n'est pas grave si cela semble bizarre. J'ai été effrayé quand je l'ai vu pour la première fois, mais cela permet de [super choses cool](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch04.html#cant-live-if-livin-is-without-you). En fait, voici une rapide démonstration :

```js
const fs = require('fs');

const fileExists = path => file => fs.existsSync(`${path}/${file}`);

const fileExistsInSrc = fileExists('/src'); // file => fs.existsSync(`${path}/${file}`)

fileExistsInSrc('index.js') // true || false
```

Donc, c'est du [currying](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/ch04.html#cant-live-if-livin-is-without-you) avec une [application partielle](https://stackoverflow.com/questions/218025/what-is-the-difference-between-currying-and-partial-application) — c'est aussi une [fermeture](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

**À part :** Espérons que personne ne me critique ici sur une quelconque technicité, mais n'hésitez pas à me harceler dans les commentaires si vous en ressentez le besoin.

Continuons :

```js
const fs = require('fs');

const fileExists = path => file => fs.existsSync(`${path}/${file}`);

const writeToPath = path => (file, content) => {
  const filePath = `${path}/${file}`;

  fs.writeFile(filePath, content, err => {
    if (err) throw err;
    console.log("Fichier créé : ", filePath);
    return true;
  });
};
```

D'abord, nous avons besoin de [**fs**](https://nodejs.org/api/fs.html#fs_file_system). Nous en avons besoin dans notre vie.

Ensuite, nous déclarons **fileExists** comme une [expression de fonction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function).

Enfin, nous avons une autre [expression de fonction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function) appelée **writeToPath.** Elle prend le **path** et retourne une autre fonction qui accepte une chaîne **file** et le **content** de ce fichier. Elle écrit ensuite le fichier ou lance une erreur (pire scénario).

Vous comprenez, n'est-ce pas ? Nous créons quelques fichiers.

#### **Étape 3 : Rencontrez Chokidar**

Fait amusant : C'est un [mot Hindi](https://en.wiktionary.org/wiki/chowkidar#English).

> **Chowkidar** — (_Inde_) gardien, gardien, portier ; celui qui habite un « chowki », poste de police ou maison de garde.

Nous parlons du [package npm](https://github.com/paulmillr/chokidar) cependant. Il est basé sur notre nouvel ami [fs](https://nodejs.org/api/fs.html#fs_class_fs_fswatcher) et vous pourriez l'utiliser pour tant de choses délicieuses.

Il surveille nos fichiers pour nous [comme un faucon](https://idioms.thefreedictionary.com/watch+like+a+hawk).

Eh bien, pas exactement comme un faucon.

Ce n'est pas un oiseau.

Pas du tout.

En tout cas, voici le code...

```js
const chokidar = require("chokidar");

const watcher = chokidar
  .watch("src/components/**", { ignored: /node_modules/ })
  .on("addDir", (path, event) => {
    const name = path.replace(/.*\/components\//, "");
    const goodToGo = /^[^\/_]*$/.test(name);
    if (goodToGo) createFiles(path, name);
  });
```

D'abord, nous l'importons.

Ensuite, nous définissons ce que nous voulons surveiller. Je surveille le répertoire **src/components**, mais vous pouvez surveiller n'importe quel ensemble de chemins. Vous pouvez même passer un [tableau de chemins](https://github.com/paulmillr/chokidar#api). Si vous ne reconnaissez pas la partie ****** dans **src/components/**** — c'est appelé un [motif glob](https://en.wikipedia.org/wiki/Glob_%28programming%29).

Après cela, nous définissons les événements que nous voulons écouter. Je n'écoute que l'ajout d'un répertoire avec **.on("addDir")** mais vous pouvez écouter [d'autres événements](https://github.com/paulmillr/chokidar#methods--events) aussi.

Ensuite, extrayons le nom du composant en remplaçant tout ce qui précède le nom du composant :

```
src/components/Header/components/Title
```

devient

```
Title
```

Enfin, nous vérifierons que le nom du composant passe cette regex :

```
/^[^\/_]*$/
```

Donc, tant qu'il n'a pas de barre oblique ou de trait de soulignement — c'est bon à aller. Cela évite de polluer les dossiers __tests__ ou les répertoires imbriqués par erreur.

#### Étape 4 : Il est temps de créer quelques fichiers !

Vous avez atteint la dernière étape. Félicitations ! C'était plutôt génial.

Cette prochaine fonction s'appelle à juste titre **createFiles**.

C'est un peu désordonné — cela pourrait être refactorisé.

Je m'excuse à l'avance si le code ci-dessous vous offense.

Plongeons-nous :

```js
function createFiles(path, name) {
  const files = {
    index: "index.jsx",
    test: `${name}.test.js`,
    sass: `${name}.sass`
  };

  if (name !== "components") {
    const writeFile = writeToPath(path);
    const toFileMissingBool = file => !fileExists(path)(file);
    const checkAllMissing = (acc, cur) => acc && cur;

    const noneExist = Object.values(files)
      .map(toFileMissingBool)
      .reduce(checkAllMissing);

    if (noneExist) {
      console.log(`Nouveau composant détecté : ${name}, ${path}`);
      Object.entries(files).forEach(([type, fileName]) => {
        writeFile(fileName, templates[type](name));
      });
    }
  }
}
```

Donc, en haut, nous déclarons l'objet **files** — c'est une liste de chaînes de noms de fichiers dans lesquelles nous injectons le paramètre **name**. Vous avez peut-être remarqué qu'il a les mêmes clés que l'objet **templates**. C'est important.

L'instruction **if** est très spécifique à ma configuration. Je ne veux pas créer mes fichiers **si** le nouveau dossier s'appelle components. Je ne crée des composants qu'**à l'intérieur** d'un sous-dossier components.

* **writeFile** est notre fonction **writeToPath** [partiellement appliquée](https://stackoverflow.com/questions/218025/what-is-the-difference-between-currying-and-partial-application). C'est une fonction qui crée un fichier dans le chemin donné lorsqu'elle est appelée avec un nom de fichier et un contenu.
* **toFileMissingBool** prend un nom de fichier et retourne vrai si ce fichier n'existe pas dans le chemin donné. Je sais que les noms de fonction sont bizarres, mais je promets que cela a un peu plus de sens dans quelques lignes.
* **checkAllMissing** est une fonction que nous allons passer à [**reduce**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce). Elle prend deux booléens et retourne vrai si les deux sont vrais. C'est de [l'algèbre booléenne](https://benmccormick.org/2018/03/27/cs-basics-boolean/). Nous utilisons également la méthode [**reduce**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce) de **Array**. Ne craignez pas reduce. C'est super cool et vraiment utile dans ce genre de situation.

Parlons de la variable **noneExist**. Si elle est vraie, alors aucun des fichiers que nous voulons créer n'existe dans le nouveau dossier. L'idée est que vous ne touchez pas à un dossier juste parce qu'il n'a pas de fichier de test ou de fichier sass. Peut-être que ce dossier n'en a pas besoin.

```js
const noneExist = Object.values(files)
  .map(toFileMissingBool)      
  .reduce(checkAllMissing);
```

C'est pourquoi j'ai créé ces fonctions aux noms étranges ci-dessus.

Nous **mappons** les valeurs dans **files** à un **booléen** qui représente si ce fichier est manquant ou non. Ensuite, nous prenons ce **tableau de booléens** et nous les **réduisons** à une seule valeur **booléenne** qui représente si tous les fichiers existent ou non.

Donc, s'ils sont tous **vrais**, alors **noneExist** est aussi **vrai**. Mais si même un est **faux**, alors **noneExist** sera **faux**.

J'espère que vous avez tout compris. C'est [un peu long à dire](https://www.ldoceonline.com/dictionary/a-bit-of-a-mouthful).

Dernier morceau de code :

```js
Object.entries(files).forEach(([type, fileName]) => {
  writeFile(fileName, templates[type](name)); 
});
```

Nous prenons la clé (**type)** et la valeur **(fileName)** et écrivons un fichier dans le chemin donné avec le contenu du modèle pertinent.

#### [Fin.](https://www.quora.com/What-does-fin-mean-at-the-end-of-a-film-or-story?share=1)

![Image](https://cdn-media-1.freecodecamp.org/images/0*rv8KkV_Kvdfj941i)
_Grosse tortue de mer nageant à travers l'océan à Kaputas Beach par [Unsplash](https://unsplash.com/@ruizra?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Randall Ruiz</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Cette image d'une tortue de mer représente à quel point vous devez vous sentir libre maintenant que vous avez tout automatisé.

Si vous voulez tout le code pour créer automatiquement des composants React, [il est ici](https://gist.github.com/Bamblehorse/6ad136c83e6fd2ea62375fa92d843a14).

Faites-moi savoir ce que vous en pensez — Restons en contact.

Dites-moi si vous trouvez des erreurs.

Suivez-moi sur [Twitter](https://twitter.com/Bamblehorse), [Medium](https://medium.com/@Bamblehorse) ou [Github](https://github.com/Bamblehorse).