---
title: Comment créer un effet de carte inclinée 3D dans React Native
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-02-22T16:35:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-3d-tilting-card-in-react-native
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--14--1.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Comment créer un effet de carte inclinée 3D dans React Native
seo_desc: "Recently, I came across a tutorial about how to create a 3D tilting card\
  \ effect (with mouse tracking functionality) on Kevin Powell's YouTube channel.\n\
  https://youtu.be/Z-3tPXf9a7M\n \nKevin used HTML, CSS, and JavaScript to create\
  \ the markup, style the..."
---

Récemment, je suis tombé sur un tutoriel expliquant comment créer un effet de carte inclinée 3D (avec fonctionnalité de suivi de la souris) sur la chaîne YouTube de Kevin Powell.

%[https://youtu.be/Z-3tPXf9a7M]

Kevin a utilisé HTML, CSS et JavaScript pour créer le balisage, styliser la carte et implémenter la fonctionnalité de suivi de la souris, respectivement.

Dans ce tutoriel, nous allons voir comment reproduire le même projet dans React Native. Nous allons écrire du balisage HTML pur et utiliser la bibliothèque [react-native-render-html](https://www.npmjs.com/package/react-native-render-html) pour tout rendre dans des vues natives à 100 %.

Voici à quoi ressembleront nos cartes inclinées à la fin de ce tutoriel :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--20-.png align="left")

Vous êtes enthousiaste ? Commençons !

## **Prérequis**

Pour suivre ce tutoriel, vous devez avoir une bonne compréhension de HTML. La connaissance de JavaScript et React Native est utile mais pas nécessaire.

Pour suivre ce tutoriel localement, sur votre ordinateur, vous devez avoir installé ce qui suit :

* [Node.js v10 ou supérieur](https://nodejs.org/en/download/)

* [Xcode](https://developer.apple.com/xcode/) ou [Android Studio](https://developer.android.com/studio) (configuré pour exécuter l'émulateur)

* React Native CLI

Pour des instructions étape par étape sur la configuration de votre environnement de développement React Native, vous pouvez lire la [documentation officielle](https://reactnative.dev/docs/environment-setup).

Alternativement, si vous n'avez pas le temps ou les ressources pour le configurer à partir de zéro, utilisez [Expo Snack](https://snack.expo.dev/). Il s'agit d'un environnement basé sur un navigateur qui vous permet de créer des projets React Native sans avoir besoin d'installer quoi que ce soit.

Passez la section **Configuration du projet** si vous suivez ce tutoriel à partir d'Expo Snack. Sinon, continuez.

## Configuration du projet

Exécutez cette commande pour installer l'outil React Native CLI en utilisant npm :

```c
npm install -g react-native-cli
```

Initialisez un nouveau projet :

```c
react-native init my-app
```

Démarrez votre émulateur :

```c
cd my-app && npx react-native run-ios // Démarrer le simulateur iOS

// OU

cd my-app && npx react-native run-android // Démarrer l'émulateur Android
```

Ces commandes devraient faire apparaître le simulateur sur l'écran comme ceci :

![Image](https://paper-attachments.dropboxusercontent.com/s_8DBD080458BC82C38C5265C10E1A2396B6E318C95FC96C295C6A241E0096B1AD_1675941462527_emulator.png align="left")

Ensuite, accédez à votre dossier d'application dans le terminal et exécutez la commande suivante pour installer [React Native HTML Renderer](https://www.npmjs.com/package/react-native-render-html) :

```c
npm i react-native-render-html
```

C'est tout pour les installations. Commençons avec le code.

## Comment configurer l'application

Dans cette section, nous allons importer React, `useWindowDimensions` et `RenderHtml`, que nous utiliserons pour créer la mise en page de notre application.

Ouvrez le fichier App.js dans votre projet et effacez le contenu du fichier. Ensuite, commencez par importer ce qui suit :

```c
import * as React from 'react';
import { useWindowDimensions } from 'react-native';
import RenderHtml from 'react-native-render-html';
```

Le hook `useWindowDimensions` nous permet d'accéder aux dimensions de la fenêtre, ce qui est la manière dont nous allons rendre le contenu réactif sur toutes les tailles d'écran. Nous utiliserons `RenderHtml` pour rendre le balisage HTML pur dans des vues natives dans notre application React Native.

Si vous suivez ce tutoriel sur Expo Snack, vous serez invité à ajouter le package `react-native-render-html` en cliquant sur le lien **Add dependency** en bas de la page. Cliquez dessus.

Ensuite, incluez le code suivant sous les imports :

```c
const source = {
  html: `
<pre class="language-css" tabindex="0"><code class="language-css"><span class="token selector">.awesome-layouts</span> <span class="token punctuation">{</span>
  <span class="token property">display:</span></span> <span>grid;</span>
<span class="token punctuation">}</span></code></pre>`
};
```

En tant que valeur de la propriété `html`, nous passons le balisage HTML pour le bloc de code. Il s'agit d'un contenu préformaté, donc ne formatez pas le code (ou il se cassera). Copiez simplement le code tel quel et collez-le dans votre fichier.

Ensuite, créez `App()` en tant que composant fonctionnel et une feuille de style de base pour l'application. Retournez `<RenderHTML />` et passez le code préformaté et la feuille de style à `source` et `baseStyles`, respectivement :

```c
export default function App() {  
  const { height, width } = useWindowDimensions();

  const base = {
    height: height,
    width: width,
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'hsl(224, 32%, 12%)', 
    color: 'white'
  }

  return (  
      <RenderHtml      
      contentWidth={width}
      source={source}      
      baseStyle={base}      
      />
  );
}
```

À la ligne 2, nous accédons à la hauteur et à la largeur de l'appareil de visualisation à partir de l'appel `useWindowsDimensions()`. Nous définissons ensuite la hauteur et la largeur de l'élément racine à celle de l'écran, aligneons le contenu au centre, définissons la couleur de fond en bleu foncé et la couleur du texte en blanc.

Enregistrez le fichier. Vous devriez trouver une interface utilisateur qui ressemble à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--15-.png align="left")

Prochaine étape : styliser le bloc de code.

## Comment styliser le code `<pre>`

Dans cette section, nous allons placer le code préformaté à l'intérieur d'une carte, incliner la carte et appliquer différentes couleurs au code pour qu'il ressemble à du vrai code CSS.

### 1. Comment mettre le code dans une carte

Toutes les feuilles de style pour notre balisage HTML iront à l'intérieur de l'objet `htmlStyles`. La première propriété de `htmlStyles` est la feuille de style pour l'élément `<pre>` :

```c
const htmlStyles = { 
  pre: {
    fontSize: '18px',
    fontWeight: 'bold',
    backgroundColor: 'hsl(222, 45%, 7%)',
    padding: '10px',
    borderRadius: '5px',    
    transform: [
      { perspective: 5000 },
      { rotateX: '8deg'},
      { rotateY: '20deg'},
      { skewX: '8deg'},
    ],
  },  
}
```

Cela ajoute un fond bleu foncé autour du code, arrondit les bords de la boîte, augmente la taille et le poids de la police du code, et ajoute un peu de remplissage entre la boîte et le code.

Avec `transform`, nous faisons tourner la carte de 8 degrés autour de l'axe x et de 20 degrés le long de l'axe y, inclinant légèrement la carte.

Nous définissons également la perspective à 5000 pour établir une distance significative entre l'utilisateur et la carte (ce qui la rend plus réaliste).

Pour voir cela en action, vous devez ajouter la propriété `tagsStyles` à `<RenderHTML />` et passer `htmlStyles` comme valeur, comme ceci :

```c
<RenderHtml      
  contentWidth={width}
  source={source}      
  baseStyle={base}
  tagsStyles={htmlStyles}      
/>
```

Enregistrez le fichier et allez sur votre appareil/émulateur pour voir l'effet :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--16-.png align="left")

Ensuite, nous stylisons le texte en ajoutant différentes couleurs.

### 2. Comment styliser le code

Nous ne voulons pas que tout le code soit blanc. Au lieu de cela, nous voulons que le `.selector` soit rose, le `.property` bleu-vert et le reste blanc. Nous allons ajouter un peu de CSS supplémentaire pour obtenir ces couleurs.

Rappelons que chaque élément `<span>` dans `<pre>` avait un nom de classe soit `.selector`, `.property` ou `.punctuation`. Avec react-native-render-html, nous ne pouvons pas utiliser le sélecteur de classe pour cibler les éléments, donc cela ne fonctionnera pas :

```c
.selector {
	color: 'hsl(338, 70%, 65%)'
}
```

Nous devrons définir le code CSS directement sur les balises HTML respectives avec la propriété `style` en ligne. Donc pour l'élément `<span>` avec le nom de classe `selector`, appliquez la couleur rose comme ceci :

```c
style="color: hsl(338, 70%, 65%);
```

Quant à l'élément `<span>` avec le nom de classe `property`, appliquez une couleur bleu-vert :

```c
style="color: hsl(183, 70%, 62%);
```

Ensuite, nous allons ajouter une lueur au texte. Pour ce faire, nous allons utiliser les versions React Native de la propriété `text-shadow` et nous allons l'appliquer aux éléments `<span>` (ajoutez à l'intérieur de l'objet `htmlStyles`) :

```c
 span: {
    textShadowColor: 'currentColor',
    textShadowOffset: {width: -0.5, height: 0.5},
    textShadowRadius: 4
  },
```

En définissant `textShadowColor` sur `currentColor`, nous disons à React Native d'utiliser la même couleur de chaque texte comme couleur d'ombre, donc le sélecteur aura une lueur rose et la propriété aura une lueur bleu-vert.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--17-.png align="left")

Maintenant, nous avons terminé avec le style du code. Dans la section suivante, nous allons transformer la carte en un élément 3D.

## Comment rendre la carte 3D et ajouter différentes couches

Dans cette section, nous allons ajouter une deuxième couche à la carte et transformer la carte en un objet 3D. La deuxième boîte sera un dégradé d'image contenant les couleurs bleu et rouge.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/angryimg.png align="left")

Dans l'objet `source`, sous la balise `<pre />`, créez un élément `<img>` et pointez son `src` vers l'image ci-dessus (téléchargez l'image à un endroit comme Dropbox et obtenez l'URL) :

```c
<img src="put-the-url-to-your-image-here"/>
```

Ensuite, ajoutez la feuille de style suivante à l'objet `htmlStyles` :

```c
  img: {    
    top: -95,
    right: 7, 
    zIndex: -10,   
    height: 95,
    width: 216,    
    borderRadius: '5px', 
    overflow: 'hidden',   
   transform: [
      { perspective: 5000 },
      { rotateX: '8deg'},
      { rotateY: '20deg'},
      { skewX: '8deg'},
    ],
  }
```

La feuille de style ci-dessus superpose essentiellement l'image avec le bloc de code (haut et droite), place l'image derrière le bloc de code (z-index), rend l'image de la même taille que le bloc de code (hauteur et largeur) et de la même forme également (transform).

Voici l'apparence finale de notre application :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--18-.png align="left")

Pour redresser le bouton, il vous suffit de réinitialiser la valeur de `rotateX` et `rotateY` à 0 pour les éléments `<img>` et `<pre>` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Untitled-design--19-.png align="left")

Récupérez le code source complet [ici](https://snack.expo.dev/@ubahthebuilder/69e153).

## Conclusion

Dans ce tutoriel, nous avons pris une carte 3D inclinée réalisée avec HTML et CSS et l'avons reproduite dans React Native.

Pour y parvenir, nous avons utilisé react-native-html-renderer pour rendre HTML en éléments React Native, et des propriétés spécifiques à React Native pour styliser les éléments.

J'espère que vous avez apprécié suivre ce tutoriel autant que j'ai apprécié le créer. Vous pouvez donner votre avis sur cet article ou discuter des opportunités avec moi sur [Twitter](https://twitter.com/kingchuuks).