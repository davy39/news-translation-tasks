---
title: Comment créer un dépôt de modèle GitHub pour l'échafaudage avec React, Vite
  et TailwindCSS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-01-09T18:04:08.000Z'
originalURL: https://freecodecamp.org/news/create-a-github-template-repository-with-react-vite-and-tailwindcss
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/github-template-vite-react-tailwind.png
tags:
- name: GitHub
  slug: github
- name: React
  slug: react
- name: tailwind
  slug: tailwind
- name: vite
  slug: vite
seo_title: Comment créer un dépôt de modèle GitHub pour l'échafaudage avec React,
  Vite et TailwindCSS
seo_desc: 'Developers love productivity. When it comes to coding, we want to do things
  fast and we look out for opportunities to re-use things as much as possible.

  Say, you are getting started with a ReactJS project and want to use TailwindCSS
  for the same. The...'
---

Les développeurs adorent la productivité. Lorsqu'il s'agit de coder, nous voulons faire les choses rapidement et nous cherchons des opportunités pour réutiliser les choses autant que possible.

Disons que vous commencez un projet `ReactJS` et que vous souhaitez utiliser `TailwindCSS` pour celui-ci. La première fois, il serait normal pour vous de créer un projet en utilisant l'outil `ViteJS`, puis de configurer TailwindCSS par-dessus.

Mais la prochaine fois (et les nombreuses fois suivantes), si vous souhaitez démarrer un nouveau projet React, aimeriez-vous répéter ces mêmes étapes encore et encore ? Un développeur astucieux ne ferait pas cela. Au lieu de cela, il créerait un "modèle" et l'utiliserait chaque fois qu'il aurait besoin de quelque chose de similaire à l'avenir.

Dans cet article, nous allons apprendre comment créer un dépôt de modèle `GitHub` pour l'échafaudage d'un nouveau projet React avec Vite et TailwindCSS. Les étapes expliquées dans cet article vous aideront également à configurer React en utilisant Vite, et à configurer TailwindCSS avec celui-ci, même si vous avez des raisons de ne pas créer le dépôt de modèle. Alors, continuez votre lecture.

Si vous aimez apprendre à partir de contenu vidéo également, cet article est également disponible sous forme de tutoriel vidéo ici : 👂

%[https://www.youtube.com/watch?v=Zk2YJUvfsOA]

## Qu'est-ce que Vite ?

[Vite (aka ViteJS)](https://vitejs.dev/) est un système de outils frontend de nouvelle génération qui aide les développeurs à commencer le développement local rapidement et facilement. Il prend en charge le remplacement de modules à chaud (HMR) super rapide afin qu'il n'y ait pratiquement aucun décalage entre la modification du code source et sa visualisation dans le navigateur.

Vite est beaucoup plus rapide pour démarrer le serveur de développement que ses prédécesseurs comme create-react-app (CRA) qui était une option privilégiée pour l'échafaudage des applications React. Vite prend en charge JSX, TypeScript et CSS dès la sortie de la boîte. Il crée des builds optimisés et gère les dépendances de manière efficace.

Vite est livré avec des modèles disponibles pour toutes les technologies web modernes comme JavaScript/TypeScript vanilla, React, Vue, Preact, Lit, Svelte, Solid et Qwik.

À ce moment, Vite est le système de outils le plus viable disponible pour commencer le développement React.

## Comment configurer un projet React avec Vite

Pour commencer, assurez-vous d'avoir `Node.js` version 18+ installée. Vous pouvez vérifier cela en exécutant la commande suivante à partir de votre invite de commande (terminal) :

```bash
node -v
```

Cela imprimera la version de Node.js que vous avez installée. Si vous n'avez pas Node.js installé ou si vous avez une version inférieure à v18, allez-y et téléchargez-le et installez-le depuis [ici](https://nodejs.org/en).

Vous pouvez utiliser l'option `--template` de la bibliothèque `vite` pour créer un projet React en utilisant le modèle. Il suffit de copier-coller la commande suivante dans votre terminal et d'appuyer sur entrée pour l'exécuter :

```bash
npm create vite@latest votre_nom_dapp -- --template react
```

Notez que vous devez remplacer `votre_nom_dapp` par le nom de votre projet/application. L'outil `vite` créera un répertoire avec le même nom contenant le code source généré.

Ensuite, changez de répertoire pour votre projet :

```bash
cd votre_nom_dapp
```

Maintenant, installez les dépendances en utilisant cette commande :

```bash
npm install
```

Une fois terminé avec succès, exécutez l'application localement en utilisant la commande suivante :

```bash
npm run dev
```

Vite exécutera l'application localement sur l'URL `http://localhost:5173` par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-16.png)
_Vite exécutant l'application localement à `http://localhost:5173`_

Vous pouvez maintenant ouvrir un onglet de navigateur et essayer l'URL pour voir votre application React en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-17.png)
_Application React en cours d'exécution_

Félicitations ! Vous avez maintenant configuré avec succès une application React avec Vite. N'hésitez pas à apporter des modifications au fichier de code source `src/App.jsx` pour voir les changements reflétés instantanément dans le navigateur.

## Comment configurer TailwindCSS avec Vite

[TailwindCSS](https://tailwindcss.com/) est un framework CSS basé sur les utilitaires qui peut vous aider à être plus productif avec son cycle de développement rapide. Il fournit des classes d'utilitaires que vous pouvez utiliser pour traduire n'importe quel design en balisage sans effort.

Tailwind fonctionne assez bien avec React, et les deux sont devenus une combinaison moderne pour construire des sites web et des applications web rapides.

### Installer TailwindCSS

Nous allons maintenant installer et configurer TailwindCSS avec l'application React que nous avons créée jusqu'à présent avec Vite. Vous pouvez maintenant arrêter le serveur Vite s'il est en cours d'exécution localement pour vous.

Tout d'abord, installons `tailwindcss`, `postcss` et `autoprefixer` en tant que dépendances de développement du projet :

```bash
npm install -D tailwindcss postcss autoprefixer
```

Quelques points à mentionner concernant `postcss` et `autoprefixer` ici :

* Le framework `tailwindcss` ne nous fournit pas les styles CSS que le navigateur comprend directement. Il nous fournit les classes d'utilitaires qu'un outil doit traduire en CSS régulier que le navigateur comprend.
* De plus, le CSS produit à partir des classes d'utilitaires doit fonctionner sur tous les navigateurs (Edge, Chrome, Firefox, Safari, etc.).

Nous devons donc avoir PostCSS et Autoprefixer avec TailwindCSS pour configurer la sortie CSS attendue à la phase de construction.

### Configurer TailwindCSS

Maintenant, créez le fichier de configuration pour Tailwind et PostCSS en utilisant cette commande :

```bash
npx tailwindcss init -p
```

Il créera deux fichiers pour vous :

* `tailwind.config.js` : le fichier de configuration pour TailwindCSS. Nous devrons modifier ce fichier pour fournir une configuration de base pour commencer. Le même fichier doit être édité avec des paramètres supplémentaires lorsque vous souhaitez étendre TailwindCSS pour des cas d'utilisation avancés.
* `postcss.config.js` : le fichier de configuration pour PostCSS. Dans la plupart des cas, vous n'avez pas besoin de changer quoi que ce soit dans ce fichier.

Ouvrez le fichier `tailwind.config.js` et remplacez le contenu existant par le suivant :

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Notez que nous avons ajouté quelques entrées à la valeur du tableau `content` pour indiquer à TailwindCSS ce qu'il doit considérer pour que ses classes d'utilitaires fonctionnent. Dans notre cas, il doit s'agir du fichier `index.html` et de tout fichier `.js` | `.ts` ou `.jsx` | `.tsx` sous le répertoire `src/`.

Maintenant, ouvrez le fichier `./src/index.css` et ajoutez les directives `@tailwind` pour chacune des couches de Tailwind :

```js
@tailwind base;
@tailwind components;
@tailwind utilities;
```

C'est tout. Nous avons effectué toute la configuration requise pour que TailwindCSS fonctionne avec une application Vite.

## Exécutons les choses ensemble

Il est temps d'exécuter les choses ensemble. Démarrez le serveur Vite localement en utilisant la commande :

```bash
npm run dev
```

Maintenant, modifiez le fichier `src/App.jsx` pour remplacer son contenu par le fragment de code suivant :

```js


function App() {

  return (
    <>
      <h1
        className="text-3xl text-center text-red-700"
      >Bienvenue à Vite avec TailwindCSS et React</h1>
    </>
  )
}

export default App
```

Ici, le JSX du composant App retourne une balise d'en-tête (h1) avec un texte de bienvenue. Remarquez les noms de classe utilisés avec la balise `<h1>`. Ce sont toutes des classes d'utilitaires du framework TailwindCSS. Vous pouvez même les lire comme de l'anglais simple. Nous avons demandé à TailwindCSS de rendre un texte plus grand (3XL), qui doit être centré et dans une nuance de rouge.

Maintenant, accédez à l'application comme avant en utilisant l'URL `http://localhost:5173`. Vous devriez voir le résultat comme prévu :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-18.png)
_Écran de bienvenue dans votre application React/Vite_

Félicitations, encore une fois ! Vous avez maintenant configuré React et TailwindCSS avec Vite et tout fonctionne comme prévu.

## Comment créer le dépôt de modèle sur GitHub

Tout le travail difficile est terminé. Maintenant, nous voulons sauvegarder ce travail quelque part afin que vous puissiez l'utiliser comme un modèle chaque fois que vous souhaitez démarrer un projet React avec TailwindCSS. Il n'y a pas de meilleur endroit que GitHub pour stocker et gérer le code source.

Connectez-vous à votre compte GitHub et créez un nouveau dépôt en cliquant sur le bouton `New` de l'onglet `repositories`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-19.png)
_Création d'un nouveau dépôt sur GitHub_

Maintenant, fournissez un nom de dépôt et une description et créez le dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-20.png)
_Entrez les détails de votre dépôt et cliquez sur "créer un dépôt"_

Ensuite, commitez et poussez l'ensemble du code du projet vers ce dépôt. Après avoir poussé le code du projet, allez dans les `Paramètres` du dépôt. Sous les paramètres généraux, vous trouverez une case à cocher avec l'étiquette `Template repository`. Cochez cette case pour faire de ce dépôt un dépôt de modèle.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-21.png)
_Faites de ce dépôt un dépôt de modèle en cochant la case à cocher_

Super ! Vous avez maintenant créé un dépôt de modèle qui vous permettra de créer un projet React et TailwindCSS en un seul clic à l'avenir.

Maintenant, vous trouverez un nouveau bouton appelé `Use this template` en haut à droite de votre dépôt. Vous pouvez cliquer dessus pour créer un nouveau dépôt de projet à partir de ce modèle. Si votre dépôt de modèle est public, n'importe qui d'autre de la communauté des développeurs peut l'utiliser pour créer son dépôt de projet. Amazing, n'est-ce pas ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-22.png)

J'ai créé un dépôt de modèle en utilisant les mêmes étapes que nous avons discutées dans cet article. N'hésitez pas à le consulter et si vous aimez le travail, donnez une étoile  2b50 au dépôt.

[https://github.com/atapas/vite-tailwind-react](https://github.com/atapas/vite-tailwind-react)

## Conclusion

C'est tout pour le moment. J'espère que vous avez trouvé cet article informatif et perspicace. Je publie régulièrement des articles significatifs sur mon [GreenRoots Blog](https://blog.greenroots.info/), et je pense que vous les trouverez utiles également.

Restez en contact.

* Je suis un éducateur sur ma chaîne YouTube, `tapaScript`. Veuillez vous [ABONNER](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à la chaîne si vous souhaitez apprendre JavaScript, ReactJS, Next.js, Node.js, Git et tout sur le développement web de manière fondamentale.
* [Suivez-moi sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils en développement web et en programmation.
* Retrouvez toutes mes conférences publiques [ici](https://www.tapasadhikary.com/talks).
* Consultez et suivez mon travail Open Source sur [GitHub](https://github.com/atapas).

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.