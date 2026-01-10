---
title: Qu'est-ce que Tailwind CSS ? Un guide pour débutants
subtitle: ''
author: Soham De Roy
co_authors: []
series: null
date: '2022-09-12T15:38:34.000Z'
originalURL: https://freecodecamp.org/news/what-is-tailwind-css-a-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Group-69.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: tailwind
  slug: tailwind
- name: Web Design
  slug: web-design
seo_title: Qu'est-ce que Tailwind CSS ? Un guide pour débutants
seo_desc: "Writing CSS can be really difficult. Period. And I get it – it can be frustrating\
  \ to nail down your own ideas or the designs you get from your design team. \nI'm\
  \ sure many of you have gone through the same pain at least a few times in your\
  \ development..."
---

Écrire du CSS peut être vraiment difficile. Point. Et je comprends – il peut être frustrant de concrétiser vos propres idées ou les designs que vous recevez de votre équipe de design. 

Je suis sûr que beaucoup d'entre vous ont vécu la même douleur au moins quelques fois dans votre carrière de développeur. 

Eh bien, c'est terminé. Parce qu'il est temps d'apprendre un outil intéressant qui nous enlève beaucoup de ce fardeau. Et non, ce n'est pas Bootstrap – cela s'appelle Tailwind CSS. 

Bien que Tailwind existe depuis un certain temps, vous n'avez peut-être pas encore rencontré ce framework. Peut-être que vous n'en avez tout simplement pas entendu parler, ou vous ne savez pas vraiment si apprendre une nouvelle technologie liée au CSS rendra vraiment votre vie plus facile. 

Et en effet, il existe de nombreuses façons d'écrire du CSS – comme le CSS3 Vanilla, LESS, SCSS, Bootstrap, styled-components, Windi CSS, et plus encore...ouf. Une liste assez longue, n'est-ce pas ?


![spongebob-long-list](https://www.freecodecamp.org/news/content/images/2022/08/spongebob-long-list.gif)

J'espère que ce court guide vous aidera à comprendre Tailwind CSS et ses avantages afin que vous puissiez dire "C'est ça. C'est celui-là".

Assez de bavardages. Plongeons directement dans le vif du sujet.

## Qu'est-ce que le CSS Atomique ?

Avant de plonger dans Tailwind CSS, comprenons ce qu'est le CSS Atomique. Selon [CSS Tricks](https://css-tricks.com/lets-define-exactly-atomic-css/) 

> "Le CSS Atomique est l'approche de l'architecture CSS qui privilégie les petites classes à usage unique avec des noms basés sur la fonction visuelle." 

C'est un peu comme créer des classes qui sont censées remplir un seul objectif. Par exemple, créons une classe `bg-blue` avec le CSS suivant :

```css
.bg-blue {
  background-color: rgb(81, 191, 255);
}

``` 

Maintenant, si nous ajoutons cette classe à une balise `<h1>`, elle obtiendra un fond bleu avec la couleur `rgb(81, 191, 255)` comme vous pouvez le voir dans le code ci-dessus.

Et voici le HTML :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div><h1 class="bg-blue">Hello world!</h1></div>
  </body>
</html>
``` 

Donc ce HTML donnera quelque chose comme ceci :

![img2-1](https://www.freecodecamp.org/news/content/images/2022/08/img2-1.PNG)


Maintenant, imaginez écrire de telles règles CSS **à usage unique** et les conserver toutes dans un **fichier CSS global**. Je sais que c'est un investissement ponctuel, mais réfléchissez à ceci – vous pouvez maintenant utiliser ces classes d'assistance à usage unique où vous le souhaitez. 

Vous avez juste besoin que votre fichier HTML utilise ce fichier CSS global, et c'est tout. Vous pouvez également utiliser des combinaisons de ces classes d'assistance dans une seule balise HTML. 

Regardons un autre exemple, voulez-vous ?

Créons un fichier CSS avec les règles suivantes :

```css
.bg-blue {
  background-color: rgb(81, 191, 255);
}
.bg-green {
  background-color: rgb(81, 255, 90);
}
.text-underline {
  text-decoration: underline;
}
.text-center {
  text-align: center;
}
.font-weight-400 {
  font-weight: 400;
}
``` 

et ensuite l'utiliser dans notre fichier HTML comme suit :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div><h1 class="bg-blue">Hello world 1</h1></div>
    <div><h1 class="text-underline">Hello world 2</h1></div>
    <div class="text-center">
      <h1 class="bg-green font-weight-400 text-underline">Hello world 3</h1>
    </div>
  </body>
</html>
``` 

Eh bien, cela générera le résultat suivant :

![img3-1](https://www.freecodecamp.org/news/content/images/2022/08/img3-1.PNG)


### 📌 Points à noter ici :

- **Combinaison de plusieurs classes d'assistance** : Regardez comment j'ai combiné plusieurs classes d'assistance à la ligne 14 dans la balise `<h1>`, à savoir `bg-green`, `font-weight-400` et `text-underline`. Tout cela a pris effet dans mon texte **Hello world 3**.
- **Réutilisabilité des classes d'assistance** : Dans l'exemple ci-dessus, regardez comment la classe d'assistance `text-underline` est utilisée plusieurs fois aux lignes 12 et 14.

Voyez comment nous avons pu ajouter différents styles sans même quitter la page HTML. Eh bien, vous pourriez dire, "Hey, nous avons dû écrire ces classes d'assistance ou utilitaires dans le fichier CSS global... qu'en est-il ?" Eh bien, je comprends. C'était définitivement l'investissement initial que nous avons dû faire pour commencer. 

Et bien sûr, qui sait combien de ces classes d'assistance ou utilitaires à usage unique nous devrions créer si nous voulions suivre cette architecture *CSS Atomique*. 

Et c'est là que Tailwind CSS intervient. Le concept de CSS Atomique n'est pas nouveau, mais Tailwind CSS le porte à un autre niveau.


## Tailwind CSS – Un Framework CSS Utility-First

Tailwind CSS, selon leur propre [site web](https://tailwindcss.com/), est un "framework CSS utility-first" qui fournit plusieurs de ces classes utilitaires **opinionnées** et **à usage unique** que vous pouvez utiliser directement dans votre balisage pour concevoir un élément. 

Certaines des classes utilitaires que j'utilise fréquemment ces jours-ci sont :

- **flex** : Utilisé pour appliquer Flexbox à une `<div>`
- **items-center** : pour appliquer la propriété CSS `align-items: center;` à une `<div>`
- **rounded-full** : pour rendre une image circulaire, et ainsi de suite 

Sérieusement, il n'est pas possible pour moi de toutes les lister car il y en a tellement. Mais le meilleur, c'est que nous n'avons pas à écrire nous-mêmes ces classes utilitaires et à les conserver dans un fichier CSS global. Nous les obtenons directement de Tailwind. 

Vous pouvez obtenir une liste de toutes les classes utilitaires que Tailwind propose sur la [page de documentation](https://tailwindcss.com/docs/installation). De plus, si vous travaillez dans VS Code, vous pouvez installer une extension appelée [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) et elle vous donnera des suggestions automatiques au fur et à mesure que vous tapez les classes utilitaires, comme montré dans l'image ci-dessous.

![img4-1](https://www.freecodecamp.org/news/content/images/2022/08/img4-1.PNG)


### Comment Installer Tailwind CSS

Il existe plusieurs façons d'installer Tailwind CSS dans votre projet, toutes mentionnées dans leur [documentation](https://tailwindcss.com/docs/installation). 

Tailwind CSS fonctionne parfaitement avec une multitude de frameworks comme Next, React, Angular, et plus encore – et même notre bon vieux HTML. 

Pour la démonstration pratique ci-dessous, j'utilise **Tailwind CSS avec une application Next**. Pour configurer une application Next avec Tailwind CSS directement, utilisez la commande suivante :

Avec `npx`
```shell
npx create-next-app --example with-tailwindcss with-tailwindcss-app
``` 
ou avec `yarn`

```shell
yarn create next-app --example with-tailwindcss with-tailwindcss-app
``` 
Une fois le projet configuré, vous pouvez passer à l'étape suivante pour créer un composant de carte de base 

### Démo Pratique

Construisons un composant de carte dans un projet Next.

```jsx
// Fichier Card.js
// à rendre dans index.js

import React from "react";

const Card = () => {
  return (
    <div className="relative w-96 m-3 cursor-pointer border-2 shadow-lg rounded-xl items-center">
      {/* Image */}
      <div className="flex h-28 bg-blue-700 rounded-xl items-center justify-center">
        <h1 className="absolute mx-auto text-center right text-2xl text-white">
          L'image va ici
        </h1>
      </div>

      {/* Description */}
      <div className="p-2 border-b-2">
        <h6>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis
          beatae nulla, atque et sunt ad voluptatum quidem impedit numquam quia?
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis
          beatae nulla, atque et sunt ad voluptatum quidem impedit numquam quia?
        </h6>
      </div>

      {/* Pile technologique utilisée */}
      <div className="flex flex-wrap items-center m-2">
        <span className=" border border-blue-300 rounded-2xl px-2 my-1 mx-1">
          #React
        </span>
        <span className=" border border-blue-300 rounded-2xl px-2 my-1 mx-1">
          #Redux
        </span>
        <span className=" border border-blue-300 rounded-2xl px-2 my-1 mx-1">
          #Javascript
        </span>
      </div>

      {/* Liens */}
      <div className="flex flex-wrap items-center rounded-b-xl border-t-2 bg-white">
        <button className="border rounded-2xl bg-blue-600 text-white shadow-sm p-1 px-2 m-2">
          Aller au Projet
        </button>
        <button className="border-2 border-blue-600 rounded-2xl text-blue-600 shadow-sm p-1 px-2 m-2">
          Github
        </button>
      </div>
    </div>
  );
};

export default Card;
``` 
Cela donne la carte suivante qui est rendue dans l'UI :

![img5-1](https://www.freecodecamp.org/news/content/images/2022/08/img5-1.PNG)

Regardez comment je peux facilement styliser le composant de carte sans même quitter le fichier Card.js. Pas besoin d'écrire des fichiers CSS supplémentaires. 

L'utilisation de `flex` avec une `<div>` applique la règle CSS `display: flex;` à celle-ci. Vous voulez ajouter `position: relative;` à une `<div>` ? Il suffit d'ajouter `relative` dans le `className` et c'est fait.  

Nous pouvons également ajouter différents modificateurs comme `hover`, `active`, `focus` et ainsi de suite pour rendre conditionnellement les classes utilitaires. Il est possible d'appliquer des règles CSS complexes comme ceci :

```css
.some-class-name {
          --tw-space-x-reverse: 0;
          margin-right: calc(0.5rem * var(--tw-space-x-reverse));
          margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse)));
}
``` 

en mentionnant simplement `space-x-2` dans la balise `<div>`. Propre, n'est-ce pas ?

Et devons-nous mentionner explicitement ces styles quelque part dans un fichier CSS global ? Absolument pas ! Tailwind le fait automatiquement pour nous. C'est la beauté de Tailwind.

Nous n'avons pas encore terminé... il y a beaucoup d'autres avantages. Regardons-les maintenant.

### Avantages de Tailwind CSS

#### Le mode Just-In-Time (JIT) offre des temps de construction ultra-rapides
Avant Tailwind v3, il parcourait tous les styles pour supprimer les styles inutilisés, afin que la version de production reste aussi petite que possible. 

Selon Tailwind, la version de production était comprise entre 5 et 10 ko. Mais c'est l'histoire en production. Dans un environnement de développement, le CSS peut devenir très volumineux, surtout si nous utilisons beaucoup de configuration personnalisée.

Avec la version 3 et supérieure, Tailwind a sorti une nouvelle fonctionnalité appelée le **compilateur Just-in-Time**. Le compilateur JIT évite de compiler tout le CSS d'emblée et ne compile que le CSS au fur et à mesure que nous en avons besoin. 

Cela se traduit par des temps de construction ultra-rapides dans tous les environnements. Et comme les styles sont générés au fur et à mesure que nous en avons besoin, il n'est pas nécessaire de supprimer les styles inutilisés. Cela signifie que le CSS dans tous les environnements sera le même. Cela nous aide à nous débarrasser de la crainte que du CSS important soit supprimé en production.

%[https://www.youtube.com/watch?v=3O_3X7InOw8]

#### Il est à la fois opinionné et flexible

Tailwind CSS est opinionné. Il spécifie certaines contraintes en matière de style, et si vous me demandez, c'est bien car cela nous aide à laisser la partie design à ceux qui la comprennent vraiment. 

Regardez simplement l'une des classes utilitaires pour ajouter une `box-shadow` à votre `<div>` ([source](tailwindcss.com/docs/box-shadow)) :

![img6-1](https://www.freecodecamp.org/news/content/images/2022/08/img6-1.PNG)

Comme vous pouvez le voir, il n'y a que 8 variantes d'ombre que Tailwind propose. Il y a des valeurs prédéfinies pour le décalage vertical et horizontal, le flou, l'étalement, la couleur et l'opacité. C'est pourquoi Tailwind est opinionné. 

Il essaie de donner un avis sur les valeurs de propriété à choisir parmi presque toutes les propriétés de style disponibles. Et croyez-moi, dans la plupart des cas, ces 8 variantes (pour `box-shadow`) seront plus que suffisantes pour créer une excellente UI. 

Par exemple, dans l'exemple pratique ci-dessus, j'ai utilisé `shadow-lg` dans la `<div>` parent principale pour obtenir cette belle ombre extérieure. 

L'utilisation de la même variante d'une classe utilitaire particulière dans différentes zones de l'UI assure également l'uniformité dans toute l'application et se traduit par une meilleure UX.

Mais au cas où vous auriez besoin d'une valeur vraiment personnalisée pour un style particulier, vous pouvez l'obtenir en ajoutant un thème personnalisé dans le `tailwind.config.js`. Par exemple, pour obtenir un `shadow-3xl` (Tailwind ne fournit pas `shadow-3xl` par défaut), vous pouvez ajouter les lignes suivantes dans le `module.exports` dans `tailwind.config.js` :

```js
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        '3xl': '0 35px 60px -15px rgba(0, 0, 0, 0.3)',
      }
    }
  }
}
``` 

Et maintenant, avec l'arrivée du JIT, vous pouvez également utiliser une valeur arbitraire à l'intérieur de crochets `[]` comme suit :

```jsx
<div class="shadow-[0_35px_60px_-15px_rgba(0,0,0,0.3)]">
  // Le reste de votre code va ici
</div>
``` 

L'utilisation de valeurs arbitraires peut être utile lorsque vous avez besoin d'un style spécifique à seulement quelques endroits. Et dans ce cas, créer un thème pour cela dans le `tailwind.config.js` peut sembler inutile.

## Mes Réflexions

J'espère vraiment avoir réussi à vous faire comprendre ce qu'est Tailwind CSS et ce que vous pouvez faire avec. 

Tailwind est un framework CSS qui nous fournit des **classes utilitaires à usage unique** qui sont **opinionnées** pour la plupart, et qui nous aident à concevoir nos pages web directement depuis notre balisage ou nos fichiers .js/.jsx/.ts/.tsx. 

À mon avis, Tailwind est simple et facile à comprendre. Il est vrai qu'il peut prendre un certain temps pour s'habituer à tous les noms de classes utilitaires, mais ne vous inquiétez pas – vous pouvez vous référer à leur documentation chaque fois que vous êtes bloqué. 

Et à tous les débutants qui commencent leur parcours dans le développement web, il est très important de savoir ce qu'est le CSS3 avant même d'explorer Tailwind (ou d'ailleurs tout autre framework CSS comme Bootstrap, Windi CSS, etc.). 


## Conclusion

Merci d'avoir lu ! J'espère vraiment que vous avez apprécié lire cet article sur Tailwind CSS et que vous l'avez trouvé utile. 

N'hésitez pas à le partager avec vos amis, j'apprécierais vraiment cela. Suivez-moi sur LinkedIn et Twitter (voir ci-dessous) et restez à l'écoute pour plus de contenu passionnant. À plus ! 🖖

## Liens Sociaux

- [LinkedIn](https://www.linkedin.com/feed/)
- [Site Web](https://www.sohamderoy.dev/)
- [Autres Blogs de moi](https://blogs.sohamderoy.dev)
- [Twitter](https://twitter.com/_sohamderoy)