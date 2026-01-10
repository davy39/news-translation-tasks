---
title: Comment créer des applications de bureau natives avec JavaScript (Proton Native)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T22:17:48.000Z'
originalURL: https://freecodecamp.org/news/build-native-desktop-apps-with-javascript-a49ede90d8e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XyeRix8Z-yOcpRlpubtyuA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer des applications de bureau natives avec JavaScript (Proton
  Native)
seo_desc: 'By Mohammed Salman

  When I was writing this article, Atwood’s Law came to mind:


  Any application that can be written in JavaScript, will eventually be written in
  JavaScript. - Jeff Atwood



  don’t worry about it

  Originally posted on my blog!

  Today we a...'
---

Par Mohammed Salman

Lorsque j'écrivais cet article, la loi d'Atwood m'est venue à l'esprit :

> Toute application qui peut être écrite en JavaScript finira par être écrite en JavaScript. - [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XyeRix8Z-yOcpRlpubtyuA.png)
_ne vous en faites pas_

[Originalement publié sur mon blog !](https://code.nimrey.me/how-to-build-native-desktop-apps-with-js/)

Aujourd'hui, nous allons examiner [Proton Native](https://proton-native.js.org) et créer une application simple avec.

Contrairement aux applications **Electron**, les applications construites avec **Proton Native** sont réellement **natives** (d'où le nom) et non basées sur le web via Chromium.

**Proton Native** est comme **React Native** mais pour le bureau. Il compile en code natif de la plateforme, donc il a l'apparence et les performances d'une application native.

Alors, commençons.

#### Windows

Installez les outils de construction en exécutant :

```
npm install --global --production windows-build-tools
```

#### Linux

Vous aurez besoin de ces bibliothèques :

* libgtk-3-dev
* build-essential

#### Mac

Vous n'avez besoin de rien.

Maintenant, exécutez ce qui suit :

```
npm install -g create-proton-app
```

et

```
create-proton-app my-app
```

pour créer un nouveau projet.

Ouvrez le répertoire du projet avec votre éditeur de code préféré. Le répertoire devrait ressembler à ceci :

```
 [34m[1m[4mnode_modules[0m
 [34m[1m.babelrc[0m
 [34m[1mindex.js[0m
 [34m[1mpackage.json[0m
 [34m[1mpackage-lock.json[0m
```

`index.js` devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BUgjpvWtCCZNPJ__qrQxig.png)
_Comme vous pouvez le voir, cela ressemble à un fichier React/React Native_

Comme pour tout projet React ou React Native, nous importons la bibliothèque React et créons un composant de classe.

L'élément `App` est simplement un conteneur qui contient `Window` et `Menu`, et `Window` a trois props : `title` (le titre de la fenêtre), `size` (prend un objet qui contient la largeur et la hauteur de la fenêtre), et `menuBar` (défini sur false car nous ne voulons pas de barre de menu).

Avant de commencer à coder, installons `crypto` en utilisant `npm` :

```
npm i crypto
```

Nous allons utiliser `crypto` pour hacher le texte avec l'algorithme MD5.

### index.js

```js
import React, { Component } from "react";
import { render, Window, App, Box, Text, TextInput } from "proton-native";
import crypto from "crypto";

class Example extends Component {
  state = { text: "", md5: "" };

  hash = text => {
    this.setState({ text });
    
    let md5 = crypto
      .createHash("md5")
      .update(text, "utf8")
      .digest("hex");

    this.setState({ md5 });
  };
  render() {
    return (
      <App>
        <Window
          title="Proton Native Rocks!"
          size={{ w: 300, h: 300 }}
          menuBar={false}
        >
          <Box>
            <TextInput onChange={text => this.hash(text)} />
            <Text>{this.state.md5}</Text>
          </Box>
        </Window>
      </App>
    );
  }
}

render(<Example />);
```

J'ai d'abord importé `Text` et `TextInput` pour pouvoir les utiliser plus tard. Ensuite, dans la `class`, après avoir défini `text` et `md5` comme des chaînes vides dans l'objet `state`, j'ai créé une fonction `hash` qui prend un argument `text`.

Dans la fonction `hash`, nous définissons l'état sur `text` et déclarons `md5` pour stocker le texte chiffré (comme ci-dessous)

```js
this.setState({ text });
let md5 = crypto.createHash("md5")
  .update(text, "utf8").digest("hex");
```

et définissons l'objet state sur le `md5` mis à jour.

```js
this.setState({ md5 });
```

La méthode `render` retourne un élément `jsx`. L'élément `Box` est comme `div` dans React, ou `View` dans React Native, qui contient `TextInput` et `Text`. Cela est dû au fait que l'élément parent window ne permet pas d'avoir plus d'un enfant.

`TextInput` a une prop `onChange` qui sera appelée chaque fois que le texte change. Par conséquent, nous la définissons sur une fonction fléchée qui prend un argument `text` et retourne la fonction `hash` que nous avons déclarée précédemment.

Ainsi, chaque fois que le texte change, `text` est haché et défini sur `md5`.

Maintenant, si nous l'exécutons avec

```
npm run start
```

cette fenêtre devrait apparaître :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D_fBTxyGSpUbIVPcyt3Kzw.png)

Et si nous entrons du texte, il est haché en md5 comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*azNLC0SBkJs85SK-fj15fw.png)

Vous pourriez dire « Cela a l'air moche — ajoutons un peu de style. » Eh bien, au moment de l'écriture de cet article, Proton Native en est encore à ses débuts. Il est très bogué et ne supporte pas encore le style, mais c'est un projet amusant avec lequel jouer.

Si vous souhaitez contribuer au projet, consultez le [dépôt](https://github.com/kusti8/proton-native).

Si vous avez des questions ou des suggestions, n'hésitez pas à commenter ou à me contacter sur Twitter [@4msal4](https://twitter.com/4msal4) et n'oubliez pas de cliquer sur ce bouton d'applaudissements :)

👋 Consultez mon histoire précédente 👋

[Comment créer une application d'actualités avec React Native](https://medium.freecodecamp.org/create-a-news-app-using-react-native-ced249263627).