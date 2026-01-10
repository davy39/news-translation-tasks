---
title: Comment résoudre les problèmes Project Euler en Rust
subtitle: ''
author: Shaun Hamilton
co_authors: []
series: null
date: '2022-03-03T17:09:14.000Z'
originalURL: https://freecodecamp.org/news/project-euler-problems-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-9-1.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Rust
  slug: rust
seo_title: Comment résoudre les problèmes Project Euler en Rust
seo_desc: "You can now solve the classic Project Euler programming problems using\
  \ the Rust language. Each of these problems comes with a user-friendly test suite.\
  \ \nHere's the full Project Euler Rust GitHub repository.\nIf you do not know Rust,\
  \ and want to learn ..."
---

Vous pouvez maintenant résoudre les problèmes de programmation classiques de Project Euler en utilisant le langage Rust. Chaque problème est accompagné d'une suite de tests conviviale. 

Voici le dépôt GitHub complet [Project Euler Rust](https://github.com/freeCodeCamp/euler-rust).

Si vous ne connaissez pas Rust et souhaitez l'apprendre, vous pouvez commencer par le [cours interactif Rust de freeCodeCamp](https://www.freecodecamp.org/news/rust-in-replit/).

Très bien. Voyons comment commencer à travailler sur Project Euler en Rust.

## Comment exécuter les problèmes Project Euler localement dans VSCode

Tout d'abord, vous devrez télécharger et installer l'[extension freeCodeCamp Courses pour VSCode](https://marketplace.visualstudio.com/items?itemName=freeCodeCamp.freecodecamp-courses).

Assurez-vous également d'avoir l'extension Microsoft [Dev Containers pour VSCode](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

Ensuite, dans un espace de travail vide, ouvrez la palette de commandes VSCode avec `Ctrl/Cmd + Shift + P`.

![euler-rust-local-ext-1](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-1.png)

Sélectionnez la commande `freeCodeCamp: Open Course`.

![euler-rust-local-ext-2](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-2.png)

Ensuite, choisissez l'option `Project Euler: Rust`.

![euler-rust-local-ext-3](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-3.png)

Une fois le cours cloné, ouvrez à nouveau la palette de commandes et sélectionnez `Dev Containers: Rebuild and Reopen in Container`.

![euler-rust-local-ext-4](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-4.png)

![euler-rust-local-ext-5](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-5.png)

![euler-rust-local-ext-6](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-6.png)

![euler-rust-gitpod](https://www.freecodecamp.org/news/content/images/2024/02/euler-rust-gitpod.png)

## Comment exécuter les problèmes Project Euler localement sans l'extension

Si vous préférez exécuter ces problèmes sans l'extension VS Code, vous devrez fork le dépôt :

![euler-rust-fork](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-fork.png)

Ensuite, clonez votre fork sur votre machine locale.

```bash
git clone https://github.com/<your_username>/euler-rust.git
cd euler-rust
```

Construisez et ouvrez le conteneur Docker comme suit :

```bash
docker build -f Dockerfile -t euler-rust .
```

Puis démarrez le cours :

```bash
npm i && npm run start
```

Optionnellement, vous pouvez également cloner et construire le conteneur avec Docker comme suit :

```bash
docker build github.com/<your_username>/euler-rust
```

## Comment exécuter les problèmes Project Euler en utilisant Gitpod

GitPod est un outil populaire pour exécuter une machine virtuelle dans votre navigateur, et c'est une autre façon de résoudre ces problèmes Project Euler. Tout d'abord, fork le dépôt :

![euler-rust-fork](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-fork.png)

Ensuite, ouvrez votre fork dans Gitpod : `https://gitpod.io/#https://github.com/<your_user_name>/euler-rust`

Optionnellement, si vous avez installé l'extension de navigateur Gitpod, vous pouvez cliquer sur le bouton `Gitpod` qu'elle ajoute à GitHub :

![euler-rust-gitpod-button](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-gitpod-button.png)

![euler-rust-gitpod-setup](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-gitpod-setup.png)

![euler-rust-gitpod](https://www.freecodecamp.org/news/content/images/2024/02/euler-rust-gitpod.png)

## Informations utiles

_NOTE :_ Si vous utilisez l'une des méthodes ci-dessus avec Docker, vous devrez avoir Docker installé sur votre machine et le démon en cours d'exécution.

Vous ne devriez avoir besoin de modifier que le fichier `src/lib.rs` dans chaque répertoire `project-euler-problems-...`, et vous pouvez suivre l'exemple de code pour commencer.

Pour compiler votre code avant d'exécuter les tests, exécutez :

```bash
wasm-pack build
```

Si à un moment donné vous êtes bloqué, je vous recommande de consulter plus d'informations sur [Rust avec WASM](https://www.rust-lang.org/what/wasm). Sinon, n'hésitez pas à ouvrir un nouveau sujet sur le [forum freeCodeCamp](https://forum.freecodecamp.org/).

## Comment le projet fonctionne

Tout d'abord, en prenant votre code Rust dans `src/lib.rs` :

```rust
use wasm_bindgen::prelude::*;

// Format d'exemple pour écrire des fonctions :
#[wasm_bindgen(js_name = camelCaseName)] // js_name doit être égal au nom de la fonction testée sur le client
pub fn snake_case_name(num: i32) -> i32 { // La fonction doit être publique
    // Tous les nombres en JS sont en 32 bits
    num
}
```

Le Rust est transpilé en code JavaScript en utilisant `wasm-pack` :

```javascript
import * as wasm from "./curriculum_bg.wasm";

/**
 * @param {number} n
 * @returns {number}
 */
export function camelCaseName(num) {
  var ret = wasm.camelCaseName(num);
  return ret;
}
```

## Questions fréquemment posées (FAQ)

> Ces problèmes Project Euler seront-ils disponibles dans d'autres langages de programmation ?

Nous accueillons toutes les contributions bien intentionnées pour la communauté freeCodeCamp. Donc, si vous êtes intéressé à développer sur un fork du dépôt, n'hésitez pas à le faire !

> Puis-je sauvegarder ma progression sur mon compte freeCodeCamp.org ?

Pas encore, mais c'est quelque chose que nous pouvons explorer plus en détail.

> L'étape Docker prend tellement de temps. Existe-t-il un moyen plus rapide de commencer ?

Eh bien, à condition d'avoir la ténacité d'installer tous les outils nécessaires sur votre machine locale, vous pouvez simplement exécuter les commandes suivantes dans le projet :

```bash
npm ci
npm run start
```

```bash
cd project-euler-problems-1-to-100
wasm-pack build
```

Maintenant, vous devriez pouvoir ouvrir un navigateur et naviguer vers `http://localhost:8080/`, et commencer.