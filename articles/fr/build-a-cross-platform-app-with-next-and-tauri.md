---
title: Comment créer une application multiplateforme avec Next.js et Tauri
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-10-18T16:38:44.000Z'
originalURL: https://freecodecamp.org/news/build-a-cross-platform-app-with-next-and-tauri
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Tauri-and-nextjs--1-.png
tags:
- name: Linux
  slug: linux
- name: macOS
  slug: macos
- name: Next.js
  slug: nextjs
- name: node
  slug: node
- name: Rust
  slug: rust
- name: Windows
  slug: windows
seo_title: Comment créer une application multiplateforme avec Next.js et Tauri
seo_desc: "Tauri is a new Rust-based framework that builds an x86_64 cross-platform\
  \ application for Windows, macOS, and Linux. \nIn this tutorial, we'll use Tauri\
  \ and Next.js to build a desktop-based cross-platform application and publish it\
  \ to the Snap store an..."
---

Tauri est un nouveau framework basé sur Rust qui construit une application x86_64 multiplateforme pour Windows, macOS et Linux. 

Dans ce tutoriel, nous allons utiliser Tauri et Next.js pour créer une application de bureau multiplateforme et la publier sur le Snap store et AppImage.

Alors, pourquoi est-il important de nos jours de créer une application multiplateforme, qui fonctionne sur Windows, Mac et Linux ? Eh bien, cela aide les entreprises à cibler un public plus large et à augmenter leurs revenus, sans avoir à construire trois applications séparées.

De nombreuses entreprises et développeurs utilisent Next.js comme front-end lors de la création d'un site web. Dans ce tutoriel, nous allons utiliser Next et Tauri pour créer une application de bureau multiplateforme qui sera disponible sur Windows, macOS et Linux. 

### Démo du projet

Pour construire cette application multiplateforme, vous avez besoin de [Tauri](https://tauri.app/), [markdown](https://en.wikipedia.org/wiki/Markdown), [Contentlayer](https://www.npmjs.com/package/contentlayer), [pnpm](http://pnpm.io/), et [Next.js](https://nextjs.org/). Si vous vérifiez comment mon application ressemble, vous pouvez installer l'application avec [snap-cli](https://snapcraft.io/docs/snap-tutorials), [AppImage](https://appimage.org/), ou télécharger l'application via le lien et l'installer.

Voyons ce que font ces outils :

* nous utiliserons Next.js pour construire la partie front-end du site web 
* le package npm markdown aide à convertir les fichiers markdown en HTML 
* le package npm Contentlayer nous aide à gérer les fichiers markdown dans le projet.
* nous utiliserons Tauri pour construire le binaire de l'application multiplateforme
* et enfin, nous utiliserons pnpm comme gestionnaire de packages Node.

```
// Installer avec snap
snap install static-blog-app

ou

// installer avec AppImage
https://github.com/officialrajdeepsingh/static-blog-app/releases/download/v0.0.2/static-blog-app_0.0.2_amd64.AppImage

ou

// Installer sur macOS
https://github.com/officialrajdeepsingh/static-blog-app/releases/download/v0.0.2/static-blog-app_0.0.2_x64.dmg

ou

// Installer sur Windows
https://github.com/officialrajdeepsingh/static-blog-app/releases/download/v0.0.2/static-blog-app_0.0.2_x64_en-US.msi

```

## Table des matières :

* [Qu'est-ce que Next.js ?](#heading-questce-que-nextjs)
* [Qu'est-ce que Tauri ?](#heading-questce-que-tauri)
* [Architecture informatique](#heading-architecture-informatique)
* [Comment créer un nouveau projet avec Next.js et Tauri](#heading-comment-creer-un-nouveau-projet-avec-nextjs-et-tauri)
* [Comment construire une application avec Tauri](#heading-comment-construire-une-application-avec-tauri)
* [Comment construire une application pour le Snap Store ou Snapcraft](#heading-comment-construire-une-application-pour-le-snap-store-ou-snapcraft)
* [Comment construire une application multiplateforme avec GitHub Actions](#heading-comment-construire-une-application-multiplateforme-avec-github-actions)
* [Comment publier l'application](#heading-comment-publier-lapplication)
* [FAQ](#heading-faq)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que Next.js ?

[Next](https://nextjs.org/) est un framework basé sur React. Il possède de nombreuses fonctionnalités qui vous permettent de construire un site web et d'améliorer l'expérience utilisateur.

Pour en savoir plus sur Next, vous pouvez [lire ce tutoriel utile que j'ai trouvé](https://www.freecodecamp.org/news/nextjs-tutorial/) sur freeCodeCamp écrit par Reed Barger.

## Qu'est-ce que Tauri ?

[Tauri](https://tauri.app/) est un nouveau framework qui vous aide à construire des applications de bureau multiplateformes. Tauri est construit sur la base du langage Rust. Rust est plus rapide, plus sécurisé et a moins de problèmes de mémoire que d'autres langages.

Tauri a de nombreuses fonctionnalités, mais je vais mentionner certaines des plus importantes pour un développeur front-end.

1. Tauri supporte HTML, CSS et JavaScript.
2. Tauri supporte de nombreux frameworks et bibliothèques front-end, par exemple, React.js, Next.js, Vite et Svelte kit.
3. Avec Tauri, vous n'avez pas besoin d'apprendre GTK, GJS et les commandes de construction d'applications ou le constructeur AppImage.
4. Tauri fournit une prise en charge de l'API JavaScript. Vous pouvez l'utiliser facilement à l'intérieur de JS. Par exemple, l'API window aide toutes les tâches liées à la fenêtre. 
5. Vous pouvez rapidement construire une taille de bundler d'application croisée avec une seule commande.
6. Tauri fournit un gestionnaire de mise à jour pour mettre à jour les anciennes versions de Tauri vers les plus récentes. Vous n'avez pas besoin d'utiliser d'autres services et bibliothèques pour obtenir la fonctionnalité de mise à jour automatique.
7. Dans Tauri, vous appelez des fonctions Rust à l'intérieur de JavaScript.

Tauri améliore l'expérience de développement en fournissant un outil CLI JavaScript, npm et Rust intégré, des plugins et le flux de travail GitHub tauri-action. 

Tous ces outils vous aident à écrire du code plus rapidement et à créer une application prête pour la production en moins de temps. Mais la grande chose que Tauri fournit est une documentation facile à comprendre et prête pour les débutants. 

[GTK](https://www.gtk.org/) est un kit d'outils de widgets multiplateforme gratuit et open-source pour créer des interfaces utilisateur graphiques pour les applications.

[GJS](https://gjs.guide/) est une bibliothèque JavaScript pour Gnome pour construire des interfaces d'application. GJS est construit sur le moteur JavaScript [SpiderMonkey](https://spidermonkey.dev/).

## Architecture informatique

Chaque système d'exploitation vient avec une architecture différente. Construire des applications multiplateformes ou effectuer une [compilation croisée](https://rust-lang.github.io/rustup/cross-compilation.html#cross-compilation) n'est pas facile. En fonction de l'architecture, vous pouvez comprendre où l'application est exécutée. En d'autres termes, quelle architecture nécessite l'exécution de nos applications comme i386, ARM ou x86_64 ?

Les architectures les plus courantes dans le monde de l'informatique sont [ARM](https://en.wikipedia.org/wiki/ARM_architecture_family), [i386](https://en.wikipedia.org/wiki/I386), et [AMD (x86_64)](https://en.wikipedia.org/wiki/X86-64). Les utilisateurs moins techniques peuvent le connaître sous le nom d'architecture 64 ou 32 bits.

Rust utilise différents types d'architecture pour s'installer. Dans mon cas, mon matériel de portable supporte x86_64 et j'ai Ubuntu installé. Sur Ubuntu x86_64, la toolchain Rust `stable-x86_64-unknown-linux-gnu` par défaut est utilisée pour construire des applications Tauri. 

La toolchain Rust construit des applications [AMD (x86_64)](https://en.wikipedia.org/wiki/X86-64). C'est pourquoi Tauri construit des applications multiplateformes (pour Windows, macOs et les distributions Linux) mais ne construit pas des applications multi-architectures (construit des applications pour toutes les architectures ARM, i386 et x86_67). 

### Comment vérifier votre architecture sous Linux par commande :

```bash
cat /etc/debian_version

	ou 
    
dpkg --print-architecture

	ou
    
uname -m

	ou
    
arch
```

### Comment vérifier quelle toolchain Tauri utilise :

La toolchain est un utilitaire fourni par Rust lui-même. Vous pouvez installer différentes toolchains avec la commande `rustup`.

Vous pouvez utiliser différents types de toolchains Rust selon l'architecture de votre ordinateur. Vous pouvez facilement vérifier quelle toolchain est installée dans votre système d'exploitation avec la commande `tauri npm`, `yarn` ou `pnpm`. 

Dans mon projet, j'utilise pnpm pour créer un nouveau projet, donc j'utilise la commande `pnpm`. Encore une fois, en fonction de la toolchain, nous construisons des applications pour différentes architectures. 

L'Ubuntu par défaut (x86_64) est basé sur la toolchain `stable-x86_64-unknown-linux-gnu`. La toolchain Rust `stable-x86_64-unknown-linux-gnu` ne construit que des applications basées sur AMD. 

La toolchain Rust est différente selon le système d'exploitation et la distribution que vous utilisez. La toolchain Rust par défaut est installée lorsque vous installez Rust sur votre ordinateur.

Voici les commandes pour vérifier votre architecture :

```
pnpm tauri info

ou

yarn tauri info

ou

npm run tauri info
```

![pnpm tauri info command output](https://www.freecodecamp.org/news/content/images/2022/10/pnpm-tauri-info.png)
_sortie de la commande pnpm tauri info_

Tauri supporte officiellement macOS, Windows et les distributions Linux et vous ne pouvez pas construire d'applications mobiles avec Tauri (vous rencontrerez beaucoup de problèmes, et après les avoir tous résolus, vous finirez par construire votre application mobile directement).

J'ai trouvé un [excellent tutoriel sur la toolchain Rust ainsi que sur la compilation croisée](https://www.youtube.com/watch?v=wp6s2sm_7VE). Le tutoriel vous guide et vous fournit une compréhension plus approfondie de la toolchain Rust.

Vous pouvez utiliser la commande `rustup` pour installer un type différent de toolchain si vous le souhaitez. Pour en savoir plus sur la toolchain Rust et la commande `rustup`, je vous suggère de commencer par la [documentation de la toolchain Rust](https://rust-lang.github.io/rustup/concepts/toolchains.html).

## Comment créer un nouveau projet avec Next.js et Tauri

Vous pouvez créer une application Tauri avec bash, cargo, PowerShell npm, yarn ou pnpm. Nous allons utiliser pnpm pour créer une nouvelle configuration Tauri dans ce tutoriel. pnpm est le nouveau gestionnaire de packages pour Node.js.

### Créer le modèle d'interface utilisateur dans Tauri

Vous pouvez utiliser différents types de frameworks front-end pour l'application Tauri, par exemple, Vue, React, Svelte, Solid, Next.js, Preact, Angular et Svelte. J'ai choisi d'utiliser Nextjs comme modèle d'interface utilisateur pour notre application Tauri dans ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-11-12-44-05.png)
_pnpm - choisissez votre modèle d'interface utilisateur_

### Créer une nouvelle application avec pnpm

Vous pouvez utiliser tout autre gestionnaire de packages node pour créer une nouvelle application comme yarn ou npm. J'ai choisi le gestionnaire de packages node pnpm, car pnpm est rapide par rapport à yarn et npm.  

```bash
pnpm create tauri-app
```

![create tauri-app with nextjs](https://www.freecodecamp.org/news/content/images/2022/10/create-tauri-app.png)
_Créer tauri-app avec nextjs_

Maintenant, Tauri a créé l'application my-demo avec succès. Vous pouvez directement changer le répertoire (dossier) `cd my-demo` avec la commande de changement de répertoire (cd). Ensuite, vous pouvez exécuter la commande `pnpm install` pour installer toutes les dépendances nécessaires au projet. Enfin, exécutez la commande `tauri dev` pour lancer une nouvelle fenêtre d'application Tauri.

![Run local development server in tauri](https://www.freecodecamp.org/news/content/images/2022/10/tauri-dev.png)
_Lancer le serveur de développement local dans tauri_

Après avoir téléchargé et compilé le code, vous pouvez voir une nouvelle fenêtre s'ouvrir dans votre système en utilisant la commande `pnpm tauri dev`.

![Open a new window by tauri](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-11-14-03-45.png)
_Ouvrir une nouvelle fenêtre avec tauri_

La structure de dossier Tauri par défaut vient avec `pnpm create tauri-app`:

![Tauri default folder structure](https://www.freecodecamp.org/news/content/images/2022/10/tauri-folder-struture.png)
_Structure de dossier Tauri par défaut_

1. Vous utilisez le fichier `next.config.js` pour la configuration de Next.js.
2. Le fichier `next-env.d.ts` est généré automatiquement pour TypeScript
3. Le fichier `package.json` contient toutes les informations pour npm, yarn et pnpm.
4. Le fichier `pnpm-lock.yaml` est créé par pnpm pour stocker toutes les informations de package avec la version.
5. Le fichier `README.MD` contient toutes les informations sur le projet.
6. Le dossier `src` contient tout le code Next.js avec les pages, les composants et les fichiers CSS.
7. Vous utilisez le dossier `src-tauri` pour Rust et la configuration Rust.
8. `src-tauri/icons` contient toutes les icônes pour l'application.
9. `src-tauri/Cargo.lock` généré par cargo pour stocker toutes les informations de package.
10. `src-tauri/Cargo.toml` généré par cargo et stocke tous les packages et la confirmation pour le projet.
11. `src-tauri/src` utilisé pour écrire le code Rust.
12. `src-tauri/target` généré par la commande `pnpm tauri dev`. Il contient tous les binaires pour le projet.
13. Le fichier `tauri.config.json` est utilisé pour la configuration de Tauri.  

### Créer l'interface utilisateur pour l'application avec Next.js

J'utilise mon [ancien site statique Next.js](https://github.com/officialrajdeepsingh/contentlayer) et je vais le convertir en une application de bureau. Le code du site web statique Next est disponible sur [GitHub afin que vous puissiez facilement le télécharger](https://github.com/officialrajdeepsingh/contentlayer).

Tout d'abord, je dois copier mes anciens articles ainsi que les dossiers public, components et pages et les coller dans le nouveau projet Tauri. Ensuite, je vais supprimer le CSS bootstrap et utiliser Tailwind CSS pour concevoir la mise en page de l'application. 

J'ai déjà expliqué le processus étape par étape sur [comment installer TailwindCSS avec Next dans cet article](https://medium.com/nextjs/install-tailwind-css-in-next-js-37a56bd64fa7). Vous pouvez lire et suivre la même configuration pour installer Tailwind si vous ne l'avez pas déjà installé.

### Générer une icône pour l'application

L'icône est importante pour l'application. L'utilisateur cliquera sur l'icône pour ouvrir votre application sous Windows, macOS et Linux.

![Serach your application in ubuntu](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-from-2022-10-11-17-57-45.png)
_Icône static-blog-app Ubuntu_

Générer des icônes pour les applications avec divers types et tailles peut être compliqué. Vous avez besoin d'icônes pour Windows, macOS et Linux. Chaque système d'exploitation a ses propres directives pour les icônes.

Tauri vient avec un outil CLI qui génère des icônes multi-systèmes d'exploitation pour les applications basées sur la configuration des icônes dans Tauri. Voici la commande pour générer les icônes :

```bash
pnpm tauri icon path-of-image
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/create-icon-for-app.png)
_Génération d'icônes_

Vous pouvez utiliser un site web en ligne pour générer des icônes pour Tauri, puis ajouter toutes les icônes dans le dossier `tauri-app/src-tauri/icons`.

Vous pouvez changer la configuration de l'icône dans le fichier `tauri-app/src-tauri/tauri.conf.json` :

```json
"icon": [
        "icons/32x32.png",
        "icons/128x128.png",
        "icons/128x128@2x.png",
        "icons/icon.icns",
        "icons/icon.ico"
],
```

## Comment construire une application avec Tauri

Pour construire l'application dans Tauri, vous devez exécuter une seule commande dans le terminal. Tauri génère automatiquement les applications de construction. 

La première application est pour la distribution basée sur Debian `.deb` et la deuxième application est AppImage. Le fichier de construction de l'application change d'un système d'exploitation à l'autre.

[AppImage](https://appimage.org/) est une distribution d'application universelle pour les distributions Linux croisées. Vous créez donc une AppImage et exécutez votre application sur n'importe quelle distribution. 

```bash
pnpm tauri build
```

La première fois que vous exécutez la commande `tauri build`, vous pouvez rencontrer une erreur d'identifiant de bundle dans le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/_bundle-identifier-error-in-tauri.png)
_Erreur d'identifiant de bundle_

Pour résoudre l'erreur d'identifiant de bundle, ouvrez d'abord le fichier `my-demo/src-tauri/tauri.conf.json` et trouvez `identifier`. Ensuite, changez la valeur `"identifier": "com.tauri.dev"` selon votre application. Assurez-vous que la valeur `identifier` est unique dans l'application.

```json
"identifier": "com.officialrajdeepsingh.blog",

```

Après avoir changé l'`identifier` dans le fichier `tauri.conf.json`, **réexécutez** la commande `pnpm tauri build`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/tauri-building-application.png)
_Exécuter la commande tauri build_

Après avoir exécuté avec succès la commande `tauri build`, Tauri génère deux fichiers :

1. my-demo_0.0.0_amd64.deb
2. my-demo_0.0.0_amd64.AppImage

Le fichier binaire bot fonctionne uniquement pour l'architecture **amd64** et ne fonctionne pas sur les architectures **arm** et **i386**.

L'extension de fichier nous indique où nous l'utilisons.

1. L'extension de fichier `.deb` est utilisée pour Debian.
2. L'extension de fichier `.AppImage` est utilisée pour toutes les distributions Linux pour installer l'application.
3. L'extension de fichier `.dmg` est utilisée pour macOS.
4. L'extension de fichier `.msi` est utilisée pour Windows.
5. L'extension de fichier `.snap` est utilisée pour la distribution Linux.

### Installer `.deb` et `.AppImage` localement

Pour tester les deux binaires `my-demo_0.0.0_amd64.deb` et `my-demo_0.0.0_amd64.AppImage`, installez-les d'abord localement et vérifiez que tout fonctionne correctement.

**Fichier `.deb`**

```bash
 276f dpkg -i static-blog-app_0.0.2_amd64
```

**Fichier `.AppImage`**

Tout d'abord, ajoutez la permission de fichier pour l'exécution, puis exécutez le fichier.

**Étape 1** : exécutez `chmod +x my-demo_0.0.0_amd64.AppImage`

**Étape 2** : exécutez `./my-demo_0.0.0_amd64.AppImage` appuyez sur entrer pour exécuter le binaire basé sur `AppImage`.

Tauri génère automatiquement les fichiers `.deb` et `.AppImage` avec leurs propres noms de fichiers.

Les deux fichiers utilisent la même syntaxe de conversion de nom partout dans le monde. Cette conversion de nom de fichier n'est pas pour Tauri. Le constructeur Flatpak et Snapcraft utilisent également le même type de syntaxe de nom de fichier.

```bash
Syntaxe

<nom-de-lapplication> <version> <architecture> <Extension de fichier>

Exemple
1. my-demo_0.0.0_amd64.deb
2. my-demo_0.0.0_amd64.AppImage
```

## Comment construire une application pour le Snap Store ou Snapcraft

Snapcraft ou le Snap store est une distribution d'applications Linux. Il aide à distribuer vos applications sur les distributions Linux. Les utilisateurs peuvent installer votre application avec un clic et l'utilisation d'une ligne de commande (Terminal).

Snapcraft est maintenu et construit par Canonical (Ubuntu). Canonical fournit toutes les distributions d'applications Linux et ne fonctionne pas pour macOS et Windows.

Avant de construire un snap, vous devez d'abord installer [Snapcraft](https://snapcraft.io/docs/snapcraft-overview).

```bash
sudo apt-get update
sudo snap install snapcraft --classic
```

### Comment construire une application pour le Snap store

Je vais vous guider avec une méthode simple pour générer le fichier snap pour Snapcraft. Le fichier snap est un fichier binaire, similaire au fichier `.deb`. Le Snap store utilise une extension spéciale `.snap` pour le fichier. Cela indique qu'il s'agit d'une application snap installée sur une distribution linux.

Vous pouvez également développer rapidement votre première application snap si vous êtes débutant – suivez simplement ces étapes (nous les passerons en revue une par une) :

1. Installez le package npm [tauri-snap-packager](https://www.npmjs.com/package/tauri-snap-packager)
2. Ajoutez la configuration dans le fichier `package.json`
3. Construisez le snap
4. Gérez les erreurs
5. Comment corriger l'erreur tauri-snap-packager prend trop de temps

### Installez le package npm tauri-snap-packager

Tout d'abord, installez le package npm [tauri-snap-packager](https://www.npmjs.com/package/tauri-snap-packager) dans votre projet. Le package npm [tauri-snap-packager](https://www.npmjs.com/package/tauri-snap-packager) vous aide à créer un fichier de configuration snapcraft.

```bash
npm install --save-dev tauri-snap-packager

# Ou avec yarn

yarn add --dev tauri-snap-packager

# Ou avec pnpm

pnpm add tauri-snap-packager
```

### Ajoutez la configuration dans le fichier package.json

Après l'installation, complétez le package npm tauri-snap-package. Maintenant, configurez le script `"tauri-snap": "tauri-snap-packager"` tauri-snap-package dans le fichier `package.json`.

```json
"scripts": {
    "dev": "next dev -p 1420",
    "build": "next build && next export -o dist",
    "tauri": "tauri",
    "lint": "next lint",
    
    "tauri-snap": "tauri-snap-packager"
    
  },
```

### Construisez le snap

Maintenant, vous exécutez la commande `pnpm tauri-snap` dans votre dossier de projet. `tauri-snap` crée automatiquement un dossier snap dans `src-tauri/target`. À l'intérieur du dossier snap, `pnpm tauri-snap` crée un nouveau fichier `snapcraft.yaml` avec toutes les configurations. Toutes les configurations sont basées sur votre configuration Tauri.

```src-tauri/target/snap/snapcraft.yaml
name: static-blog-app
base: core18
version: 0.0.2
summary: Tauri app.
description: Awesome Tauri app.
grade: devel
confinement: strict
source-code: https://github.com/officialrajdeepsingh/static-blog-app
apps:
  static-blog-app:
    command: static-blog-app
    extensions:
      - gnome-3-34
    desktop: static-blog-app.desktop
parts:
  dump-binary:
    plugin: dump
    source: ./target/release
    source-type: local
    stage:
      - lib
      - icons
      - static-blog-app
      - static-blog-app.desktop
    prime:
      - lib
      - icons
      - static-blog-app
      - static-blog-app.desktop
    stage-packages:
      - libc6

```

### Comment corriger les erreurs 

Vous obtiendrez une erreur lors de la validation de `snapcraft.yaml` avec la commande `pnpm tauri-snap`.

![Problèmes lors de la validation de snapcraft.yaml](https://www.freecodecamp.org/news/content/images/2022/10/Issues-while-validating-snapcraft.yaml--1-.png)
_Problèmes lors de la validation de snapcraft.yaml_

Le nom de votre application peut contenir certains mots qui ne sont pas autorisés, comme des espaces, des chiffres, des lettres majuscules, etc. Par exemple, Static-blog-website ne vous permet pas d'utiliser votre nom avec une lettre majuscule. Utilisez simplement un mot en minuscules pour un nom comme static-blog-website.

Vous pourriez également voir une erreur `you need 'multipass' set-up to build snaps` lors de l'exécution de la commande `pnpm tauri-snap --trace-warnings`.

Le flag Node.js `--trace-warnings` aide à déboguer ou à tracer l'erreur.

![Vous avez besoin de 'multipass' configuré pour construire des snaps](https://www.freecodecamp.org/news/content/images/2022/10/You-need-multipass-.png)
_Erreur : Vous avez besoin d'une configuration multipass pour construire des snaps._

Pour résoudre l'erreur, vous devez installer le [package multipass](https://multipass.run/) dans Ubuntu. Le tauri-snap-package utilise la commande Snapcraft en arrière-plan pour construire un fichier snap. Donc Snapcraft nécessite multipass pour construire un package snap.

```
sudo snap install multipass
```

![Installer multipass dans ubuntu](https://www.freecodecamp.org/news/content/images/2022/10/install-multipass.png)
_Installer multipass dans ubuntu_

### Tauri-snap-packager prend trop de temps.

Si le [tauri-snap-packager](https://www.npmjs.com/package/tauri-snap-packager) prend trop de temps pour construire le binaire snap ou si vous avez l'impression que votre application est bloquée et ne montre aucune sortie dans le terminal, arrêtez simplement la commande. Le tauri-snap-packager ne fonctionne pas pour vous, vous pouvez donc utiliser la commande `snapcraft`.

![Créer une configuration snap avec Tauri-snap-packager ](https://www.freecodecamp.org/news/content/images/2022/10/build-snap-by-tauri-snap.png)
_Créer une configuration snap avec Tauri-snap-packager_

Cette erreur signifie que la commande `pnpm tauri-snap` ne fonctionne pas et qu'elle prend trop de temps. Il est probable que le package npm tauri-snap-package ne fonctionne pas correctement. 

Pour résoudre ce problème, **exécutez la commande snapcraft dans le même dossier où votre dossier snap a été créé**. Avant d'exécuter la commande snapcraft, installez d'abord l'outil de commande snapd. Snapd est un démon d'API REST pour gérer les packages snap. Pour en savoir plus sur snapd, j'ai [trouvé un excellent article](https://codeburst.io/how-to-install-and-use-snap-on-ubuntu-18-04-9fcb6e3b34f9) écrit par Oyetoke Tobi Emmanuel.

```
snap install --channel stable snapd
```

Après l'installation, exécutez la commande `snapcraft` dans le dossier `tauri-app/src-tauri/target`. Le dossier `target` est généré par la commande `pnpm tauri dev`. 

![Rencontrez une erreur courante avec la commande snapcraft.](https://www.freecodecamp.org/news/content/images/2022/10/snap-_core18_-has-no-updates-available.png)
_Rencontrez une erreur courante avec la commande snapcraft_

Vous pouvez obtenir une erreur snap "core18" n'a pas de mises à jour disponibles avec Snapcraft. **Mais le core18 n'est pas un gros problème.** Mettez simplement à jour votre package de distribution avec la commande `sudo apt-get update && sudo apt-get upgrade`, puis redémarrez votre terminal ou votre ordinateur portable. [Voici un tutoriel youtube](https://www.youtube.com/watch?v=PNii2y97D0s&ab_channel=BassoniaTv) qui peut vous aider à résoudre votre problème d'erreur core18.

"Snapd n'a pas enregistré" signifie que vous devez d'abord vous connecter à votre [compte snapcraft](https://snapcraft.io/). Pour vous connecter, exécutez `snapcraft login`.

Après avoir résolu le problème core 18, exécutez à nouveau la commande `snapcraft` et construisez votre fichier binaire snap.

![Construire un nouveau binaire avec snapcraft](https://www.freecodecamp.org/news/content/images/2022/10/snapcraft.png)
_Créer un binaire avec snapcraft_

Snapcraft crée un nouveau binaire `static-blog-app_0.0.0_amd64.snap`. Maintenant, le fichier `static-blog-app_0.0.0_amd64.snap` est prêt à être publié sur le site web Snapcraft ou le snap store.

### Comment installer static-blog-app_0.0.0_amd64.snap localement dans le système

Si vous installez le fichier `static-blog-app_0.0.0_amd64.snap` localement avec la commande suivante, vous pourriez rencontrer l'erreur de métadonnées de signatures.

```bash
sudo snap install ./static-blog-app_0.0.0_amd64.snap

```

**Voici l'erreur :**

![impossible de trouver l'erreur de métadonnées de signatures pour snap](https://www.freecodecamp.org/news/content/images/2022/10/install-locally-snap-file.png)
_impossible de trouver l'erreur de métadonnées de signatures pour snap_

Pour résoudre cette erreur, vous devez exécuter la commande snap avec le flag `--dangerous`.

![Installer le package snap localement](https://www.freecodecamp.org/news/content/images/2022/10/install-snap-locally-package-with-snap.png)
_Installer le package snap localement_

## Comment construire une application multiplateforme avec GitHub Actions

GitHub Actions est une plateforme ou un pipeline **d'intégration continue et de livraison continue (CI/CD)** qui vous permet d'automatiser des tâches comme la construction, les tests et le déploiement. 

Vous pouvez trier les actions GitHub sur certains événements comme quelqu'un poussant un nouveau code dans le dépôt GitHub et exécutant des tests sur le code. Si le test passe, le code est ajouté à la branche principale ou master. 

Si vous souhaitez construire des applications multiplateformes pour Windows, macOS et Linux, le moyen le plus simple est d'utiliser le flux de travail GitHub actions. Ce flux de travail s'exécute sur un événement spécifique comme push, pull, etc.

Pour essayer cela, vous devrez créer une nouvelle action dans votre projet. Tout d'abord, créez un nouveau dossier `.github/workflows`. Ensuite, dans `workflows`, créez un fichier avec n'importe quel nom avec une extension `.yml`.

L'application Tauri fournit une [configuration d'action GitHub](https://github.com/tauri-apps/tauri-action). Avec les actions Tauri, vous pouvez rapidement construire des applications multiplateformes pour Windows, macOS et les distributions Linux avec le flux de travail GitHub.

```my-demo/.github/workflows/build.yml
name: Build application
on:
  push:
    branches:
      - 'main'
  workflow_dispatch:

jobs:
  release:
    strategy:
      fail-fast: false
      matrix:
        platform: [macos-latest, ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.platform }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16

      - uses: pnpm/action-setup@v2.0.1
        name: Install pnpm
        id: pnpm-install
        with:
          version: 7.13.1
          run_install: false

      - name: Get pnpm store directory
        id: pnpm-cache
        run: |
          echo "::set-output name=pnpm_cache_dir::$(pnpm store path)"

      - uses: actions/cache@v3
        name: Setup pnpm cache
        with:
          path: ${{ steps.pnpm-cache.outputs.pnpm_cache_dir }}
          key: ${{ runner.os }}-pnpm-store-${{ hashFiles('**/pnpm-lock.yaml') }}
          restore-keys: |
            ${{ runner.os }}-pnpm-store-

      - name: Rust setup
        uses: actions-rs/toolchain@v1
        with:
          toolchain: stable

      - name: Install dependencies (ubuntu only)
        if: matrix.platform == 'ubuntu-latest'
        run: |
          sudo apt-get update
          sudo apt-get install -y libgtk-3-dev webkit2gtk-4.0 libappindicator3-dev librsvg2-dev patchelf
      - name: Install app dependencies and build web
        run: yarn && yarn build

      - name: Build the app
        uses: tauri-apps/tauri-action@v0
        env:
          GITHUB_TOKEN: ${{ secrets.STATIC_BLOG_APP }}
        with:
          tagName: v__VERSION__ # tauri-action remplace \_\_VERSION\_\_ avec la version de l'application
          releaseName: 'v__VERSION__'
          releaseBody: 'Voir les actifs pour télécharger cette version et l'installer.'
          releaseDraft: true
          prerelease: false
```

En suivant l'action GitHub, vous pouvez construire votre application à chaque push après avoir construit avec succès l'application et afficher tous les fichiers dans la section des actifs de la version GitHub. 

![Afficher toutes les applications dans la section des actifs](https://www.freecodecamp.org/news/content/images/2022/10/asset-folder.png)
_Afficher toutes les applications dans la section des actifs._

## Comment publier l'application 

La publication du package est le cœur de cet article. Beaucoup de gens construisent leurs propres applications Linux. Mais ensuite, ils ne savent pas comment soumettre l'application sur diverses distributions comme Snapcraft, AppImage et Homebrew.

Alors maintenant, je vais montrer comment soumettre une application static-blog-app à Snapcraft et AppImage. 

### Comment publier l'application dans le snap store ou snapcraft

Pour publier un nouveau package sur le snap store, assurez-vous d'avoir un binaire `.snap` disponible. Sinon, construisez d'abord le binaire `.snap` pour l'application (ce que nous avons déjà couvert ci-dessus).

Allez dans le dossier `target` ou celui où vous avez créé le binaire `.snp`. Ensuite, exécutez la commande `snapcraft`. Assurez-vous de vous connecter d'abord avec votre compte Snapcraft. Pour vous connecter, exécutez `snapcraft login`. Ensuite, exécutez la commande suivante avec l'argument que j'ai mentionné :

Syntaxe :

```
snapcraft upload <Opation> name-of-file
```

![Publier un nouveau package sur snapcraft](https://www.freecodecamp.org/news/content/images/2022/10/devel-in-snap.png)
_Publier un nouveau package sur snap en version devel_

Après vous être connecté avec succès à votre compte, vous pouvez ajouter ou modifier les informations concernant l'icône, le nom de votre package, etc.

```bash
snapcraft upload --release=stable ./static-blog-app_0.0.0_amd64.snap
```

En mode `devel`, vous verrez un message sur la page d'installation de l'application. `devel` signifie mode développement.

![Application en mode développement](https://www.freecodecamp.org/news/content/images/2022/10/static-app-in-devmode.png)
_Application en mode développement_

Par défaut, votre package publie toutes les informations collectées par `src-tauri/target/snap/snapcraft.yaml` dans la version edge. Pour comprendre davantage le système de publication de Snapcraft, vous pouvez lire la [documentation sur la publication](https://snapcraft.io/docs/release-management).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/staticblogappforlinux.png)
_Allez dans le tableau de bord et ajoutez ou mettez à jour toutes les informations concernant l'application._

Assurez-vous d'utiliser une image de bannière avec une taille de 720 x 240 pour le snap.

### Comment publier votre application sur Snapcraft

Lorsque vous téléchargez votre application sur votre compte Snapcraft, votre application est privée. Pour changer la manière dont elle est publiée, faites glisser votre version disponible dans l'un des canaux de publication. 

Allez dans le tableau de bord> my snap> sélectionnez votre snap> releases, et selon vos exigences, ajoutez votre application à l'une des versions fournies. La version par défaut est edge release. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/releases-in-snap.png)

### Comment ajouter une application à une version stable

Pour changer l'application en une version stable, allez dans la configuration snap `src-tauri/target/snap/snapcraft.yaml` et mettez à jour votre `grade: devel` en `grade: stable` :

```yaml
....

grade: stable

....

```

Maintenant, votre application passe en version stable ou en canal et réupload votre application.

![Publier une image snap en version stable](https://www.freecodecamp.org/news/content/images/2022/10/publish-in-snap-1.png)
_L'application passe automatiquement en version stable si vous ne mentionnez pas les tags de version._

Maintenant, vous avez publié avec succès votre application dans une version stable. 

### Comment mettre à jour votre application snap

Pour mettre à jour l'application snap, vous devez apporter des modifications dans le fichier `tauri/target/snap/snapcraft.yaml` dans la section version.

```snapcraft.yaml
...

version: 0.0.1

ou 
version: 1.0.0

ou

version: 0.1.0

...

```

Maintenant, reconstruisez votre application avec la commande `snapcraft`.

![Reconstruire votre application](https://www.freecodecamp.org/news/content/images/2022/10/update-application.png)
_Reconstruire votre application_

Après avoir construit avec succès votre application, réupload votre dernière version, et votre application sera mise à jour sur le site web du snap store. 

![Mettre à jour votre application dans snapcraft](https://www.freecodecamp.org/news/content/images/2022/10/upload-latest-v-ersion-of-snap.png)
_Mettre à jour votre application dans snapcraft_

### Comment publier des applications dans AppImage

AppImage vous aide à distribuer votre application sur les distributions Linux. Vous n'avez pas besoin d'installer AppImage pour qu'il fonctionne dans votre système.

La publication de l'application sur AppImage est un processus simple. Tout d'abord, vous avez besoin d'une URL AppImage et d'un compte GitHub.

Tout d'abord, allez dans le [dépôt GitHub appimage](https://github.com/AppImage/appimage.github.io) et cliquez sur ce lien.  

![Soumettre une application dans appimage](https://www.freecodecamp.org/news/content/images/2022/10/appimagesubmit.png)
_Cliquez sur ce lien_

Après cela, une nouvelle page s'ouvre dans le navigateur :

![Soumettre une pull request dans appimage](https://www.freecodecamp.org/news/content/images/2022/10/submit-app.png)
_Soumettre une pull request dans AppImage_

1. Ajoutez le nom de votre application.
2. Collez votre URL d'image 
3. Ajoutez un commentaire
4. Cliquez sur le nouveau bouton de proposition de fichier. 
5. Téléchargez le dépôt appimage.github.io dans votre compte GitHub
6. Créez une nouvelle pull request dans le dépôt appimage.github.io.

![Créer une pull request dans appimage.github.io](https://www.freecodecamp.org/news/content/images/2022/10/create-a-new-pull-request.png)
_Créer une pull request dans appimage.github.io_

7. Ajoutez le commentaire et cliquez sur le bouton de création de pull request.

![Créer une pull request dans appimage.github.io](https://www.freecodecamp.org/news/content/images/2022/10/create-pull-request-to-appimage.png)
_Ajoutez un commentaire et créez une pull request dans appimage.github.io_

Maintenant, votre application est soumise avec succès au dépôt appimage.github.io. Le appimage.github.io exécute des actions GitHub basées sur votre application. Votre application doit passer tous les tests exécutés par AppImage. Après cela, votre image doit être listée avec succès sur AppImage afin que tout le monde puisse télécharger votre application.

Si vous soumettez une application sur AppImage avec une pull request, votre test d'action GitHub échouera. Vous verrez l'erreur GLIBC_2.29' not found.

J'ai essayé de nombreuses façons de résoudre ce problème, mais je n'ai pas trouvé de solution. Si je le fais, je mettrai à jour mon dépôt ainsi que cet article.

![GLIBC_2.29 n'est pas trouvé dans ubuntu](https://www.freecodecamp.org/news/content/images/2022/10/GLIBC_2.29--not-found.png)
_GLIBC_2.29 n'est pas trouvé_

## FAQ

### Si vous construisez l'application avec Tauri, devez-vous coder en Rust ?

Non, vous pouvez construire une application sans écrire une seule ligne de code en Rust. Au lieu de cela, Tauri fournit une prise en charge de l'API JavaScript et TypeScript pour le développement front-end afin de gérer de nombreuses choses comme le presse-papiers, la boîte de dialogue, l'événement, HTTP, la notification, etc.

### Comment construisez-vous une architecture multiplateforme (compilation croisée) avec Tauri ?

Vous pouvez construire une application multi-architecture (compilation croisée) avec Rust. La toolchain Rust vous aide à construire des [applications de compilation croisée](https://rust-lang.github.io/rustup/cross-compilation.html).

### Qu'est-ce que la toolchain dans Tauri ?

La toolchain Rust vous aide à construire une application sur une architecture différente. Dans Rust, il existe 86 toolchains disponibles pour différentes architectures.

```bash
 276f rustup target list
```

### Pouvez-vous utiliser Tauri pour construire une application Android ou iOS ?

Non, vous ne pouvez pas utiliser Tauri pour construire des applications pour Android et iOS. Mais il existe une bibliothèque qui vous aide à construire des applications pour les téléphones mobiles – je ne l'ai pas encore testée. Vous pouvez construire des applications avec une toolchain. Je vais bientôt écrire un article à ce sujet sur [mon site web.](https://officialrajdeepsingh.dev/)

### Quelles sont les API JavaScript et TypeScript de Tauri ?

Tauri fournit différents types d'API qui aident à améliorer l'expérience utilisateur et développeur. Vous pouvez utiliser l'API pour gérer les notifications, les boîtes de dialogue, les événements, HTTP, etc.

## Conclusion

Il est relativement facile de construire des applications multiplateformes avec Tauri. Vous pouvez utiliser n'importe quel framework front-end pour l'application.

Mais les autres frameworks ne vous permettent pas de construire diverses applications multi-architecture et multi-système d'exploitation, par exemple, Windows, macOS et les distributions Linux.

Tauri vient avec un support de langage backend solide. Avec Rust, vous pouvez faire tout ce que vous pouvez faire avec un langage de bas niveau. De plus, Rust fournit une sécurité mémoire, pas de ramasse-miettes, etc.

Lors de la construction de l'application Tauri avec Flatpak, je n'ai pas trouvé de solution de développement et de distribution. Cependant, à l'avenir, je l'ajouterai au fichier readme GitHub.

Je n'ai pas couvert comment distribuer des applications sur Windows et macOS. Je suis un utilisateur Linux et je ne teste pas les applications sur Windows et macOS. Mais il existe de nombreux articles et vidéos sur Internet que vous pouvez consulter pour apprendre comment faire cela.

MacOS dispose d'une plateforme de distribution populaire appelée homebrew. Le système de distribution [homebrew](https://docs.brew.sh/How-to-Build-Software-Outside-Homebrew-with-Homebrew-keg-only-Dependencies) est similaire à [appimage.org](https://appimage.org/). Si vous soumettez une nouvelle pull request pour votre application et passez tous les tests, votre application apparaîtra sur homebrew.

Si vous avez des questions ou des suggestions concernant le développement et la distribution d'une application Tauri, vous pouvez demander de l'aide sur les [discussions GitHub de Tauri](https://github.com/tauri-apps/tauri/discussions/).