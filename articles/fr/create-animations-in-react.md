---
title: Comment créer des animations dans React 18
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-08T23:51:27.000Z'
originalURL: https://freecodecamp.org/news/create-animations-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Animations-splash--1-.png
tags:
- name: animations
  slug: animations
- name: React
  slug: react
seo_title: Comment créer des animations dans React 18
seo_desc: "We are surrounded by gorgeous web applications. Sometimes I catch myself\
  \ admiring visual effects on some website and wondering how they were made. \nWell\
  \ today I'll show you how you can create awesome CSS animations in React 18.\nAs\
  \ always, we'll work ..."
---

Nous sommes entourés d'applications web magnifiques. Parfois, je me surprends à admirer les effets visuels d'un site web et à me demander comment ils ont été créés. 

Aujourd'hui, je vais vous montrer comment créer des animations CSS incroyables dans React 18.

Comme toujours, nous travaillerons sur un exemple concret, mais nous nous concentrerons uniquement sur les animations pour éviter toute confusion. Si vous souhaitez voir les résultats finaux appliqués à une application complète, ne vous inquiétez pas. J'ai joint le code source d'un projet personnel, alors n'hésitez pas à [jouer avec](https://mateuszsokola.github.io/2048-in-react/). 

Avant de commencer, je dois vous donner un peu de contexte : j'ai conçu ces animations pour mon jeu 2048 en React. Ce jeu fait partie de mon [cours en ligne sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106), mais je vous en parlerai plus en détail à la fin de cet article.  
  
Vous pouvez trouver le [code source sur GitHub](https://github.com/mateuszsokola/2048-in-react/). Voici le résultat final de ce que nous allons créer :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/all-animations.gif)
_Toutes les animations de 2048-in-react_

## **🛠E0F P**rérequis****

Avant de commencer, assurez-vous de connaître les bases de React et de CSS. Ce serait bien si vous êtes familier avec les transitions CSS, mais ce n'est pas nécessaire. En fait, j'espère que cet article vous encouragera à explorer ce sujet par vous-même. Croyez-moi, rien n'est plus gratifiant que de voir les utilisateurs admirer votre travail. 

De plus, vous n'avez besoin d'aucun outil, mais si vous souhaitez exécuter le projet d'exemple sur votre ordinateur, vous devrez d'abord installer [Node.js](https://nodejs.org/en).

## 🕹E0F **Introduction rapide**

Si vous n'êtes pas familier avec le jeu 2048, voici l'essentiel : le joueur doit combiner des tuiles contenant les mêmes nombres jusqu'à atteindre le nombre 2048. Les tuiles ne peuvent contenir que des nombres représentant une puissance de deux à partir de 2, ce qui signifie 2, 4, 8, 16, 32, et ainsi de suite. Le plateau a une dimension de 4 x 4 tuiles, de sorte qu'il peut contenir jusqu'à 16 tuiles.

Permettez-moi de vous montrer brièvement les animations que j'ai préparées pour les utilisateurs du jeu :

La première animation est censée visualiser le mouvement des tuiles.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/slide.gif)
_L'animation de "glissement des tuiles"_

Le jeu aurait l'air saccadé si les tuiles disparaissaient et réapparaissaient à différents endroits. Les transitions CSS aident à rendre le mouvement fluide pour les utilisateurs.

La deuxième animation met en évidence la création des tuiles et leurs fusions.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/hightlight-1.gif)
_L'animation de "mise en surbrillance des tuiles"_

Cette animation aide les utilisateurs à repérer les tuiles qui ont été modifiées après le mouvement.

Je pense que c'est tout ce que je dois vous dire sur le projet. Mettons-nous au travail !

## 🌟 Comment créer l'animation de surbrillance

Nous commencerons par l'animation responsable de la mise en évidence des changements. Je dois admettre que j'ai eu du mal à trouver une manière "belle" de la visualiser. L'objectif principal était d'attirer l'attention de l'utilisateur sur les tuiles qui ont changé de valeur ou qui ont été créées. J'ai décidé de redimensionner ces tuiles car je ne voulais pas que l'animation soit trop "intrusive".

Alors, comment cela va-t-il fonctionner ? Tout d'abord, nous allons augmenter la taille de la tuile à 110 %. Une fois que la tuile atteint 110 % de sa taille d'origine, nous allons la redimensionner à 100 %. L'animation complète durera 0,2 s (0,1 s pour l'agrandissement, 0,1 s pour la réduction). Je pense que c'est suffisant pour montrer les éléments mis à jour à l'utilisateur.

Nous pouvons accomplir cette animation en utilisant les transitions CSS suivantes :

```css
.tile {
  // ...
  transition-property: transform;
  transition-duration: 100ms;
  transform: scale(1);
}
```

Brève explication de ces propriétés CSS :

* `transition-property` – définit la propriété sur laquelle la transition sera appliquée. Dans notre cas, nous voulons animer la transformation – le changement de la taille de l'élément. 
* `transition-duration` – définit la durée de la transition. Dans notre cas – 0,1 s.
* `transform` – cette propriété nous permet de faire pivoter, redimensionner, incliner ou translater un élément. Note de bas de page : `scale(1)` signifie 100 %, et nous l'utiliserons comme valeur par défaut.

La transition CSS est prête. Maintenant, nous devons implémenter le redimensionnement dans React. 

```js
export default function Tile({ value }) {
  const [scale, setScale] = useState(1);

  const previousValue = usePreviousProps(value);
  const hasChanged = previousValue !== value;

  useEffect(() => {
    if (hasChanged) {
      setScale(1.1);
      setTimeout(
          () => setScale(1), 
          100 /* 100ms == 0.1s */
      );
    }
  }, [hasChanged, setScale]);

  const style = {
    transform: `scale(${scale})`
  };

  return (
    <div className="tile" style={style}>
      {value}
    </div>
  );
};
```

Permettez-moi de vous expliquer brièvement ce code :

1. Il définit l'échelle initiale en utilisant le hook `useState`. Par défaut, elle est de `1` pour refléter 100 % de la taille de la tuile.
2. Nous utilisons le hook `usePreviousProps` pour récupérer la valeur précédente de la tuile. Si la tuile vient d'être créée, la valeur précédente sera `undefined`.
3. Le hook `useEffect` joue un rôle clé dans notre animation – il vérifie si la valeur de la tuile a changé. Si oui, il l'agrandira à 110 % et après 0,1 s, il la ramènera à 100 %.
4. La constante `style` est utilisée pour injecter des attributs CSS en ligne dans l'élément `div`. 

Et le résultat est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/hightlight.gif)
_Création de tuile (aka "mise en surbrillance")_

## 🗝 Comment créer l'animation de glissement

La deuxième animation est responsable du mouvement des tuiles. J'espère que vous êtes d'accord avec moi pour dire que les utilisateurs pourraient être confus s'ils ne peuvent pas suivre les tuiles se déplaçant sur le plateau. Après chaque mouvement, ils devraient réanalyser tout le plateau. Ce serait une mauvaise expérience utilisateur.

Réfléchissons à la manière dont nous pouvons y remédier. Nous pourrions certainement tirer parti des propriétés CSS responsables du positionnement, telles que `left` et `top`. Si nous suivons cette approche, nous devons ajouter quelques transitions CSS supplémentaires. Faisons-le.

```css
.tile {
  position: absolute;
  // ...
  transition-property: left, top, transform;  // ajouté : left, top
  transition-duration: 250ms, 250ms, 100ms; // ajouté : 250ms, 250ms
  transform: scale(1);
}
```

Une fois que nous avons déclaré les transitions, nous pouvons implémenter la logique responsable du mouvement des tuiles.

```js
export default function Tile({ value, position }) {
  // ...
  const boardWidthInPixels = 464; 
  const tileCount = 4;
  
  const positionToPixels = (position) => {
    return (position / tileCount) * boardWidthInPixels;
  };    
    
  const style = {
    top: positionToPixels(position[0]),
    left: positionToPixels(position[1]),      
    transform: `scale(${scale})`
  };

  // ...
};
```

Comme vous pouvez le voir, l'équation dans la fonction `positionToPixels` doit connaître la position de la tuile, le nombre total de tuiles par ligne et colonne, et la longueur totale du plateau en pixels (largeur ou hauteur – c'est la même chose, c'est un carré). La valeur calculée est transmise à la constante `style` que nous avons transmise à l'élément div dans l'étape précédente.

Le résultat est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/slide-1.gif)
_Animation pour le mouvement des tuiles_

## **🏁 Résumé**

Ajouter des transitions CSS à votre projet React peut sembler intimidant au premier abord, mais ce n'est vraiment pas le cas. Comme vous pouvez le voir, quelques lignes de code ont considérablement amélioré l'expérience utilisateur de mon jeu. 

Gardez à l'esprit que si les animations peuvent effectivement améliorer l'expérience utilisateur, elles peuvent aussi la ruiner. Essayez toujours de trouver le bon équilibre lorsque vous les appliquez. Cela demande un peu de pratique, et c'est pourquoi j'espère que cet article vous a encouragé à expérimenter par vous-même.

La meilleure façon d'apprendre est de pratiquer et d'apprendre des autres. C'est pourquoi vous devriez consulter le [code source de mon jeu 2048 sur GitHub](https://github.com/mateuszsokola/2048-in-react/). N'oubliez pas de lui donner une étoile 🌟. C'est le moyen le plus simple de le marquer dans votre profil pour ne jamais le perdre. 

Si cet article vous a aidé, veuillez le partager sur vos réseaux sociaux ou me donner un [coup de pouce sur Twitter](https://twitter.com/msokola). Merci !

## 🏫 **Souhaitez-vous créer votre propre jeu 2048 ?**

Comme je vous l'ai dit au début, j'ai créé un cours en ligne sur Udemy où j'enseigne comment créer un jeu 2048 entièrement fonctionnel dans React 18. Je propose une réduction de 50 % pour les lecteurs de freeCodeCamp. Il suffit d'utiliser le code **50DISCOUNT** pour s'inscrire.

### **🧑🎓 Rejoignez mon [cours React 18 sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106)**

  
Ce que vous apprendrez :

* Comment construire un jeu 2048 avec React 18 et Next.js.
* Les hooks essentiels de React tels que useState, useRef, useCallback, useEffect, et bien d'autres.
* Gérer l'état en utilisant Reducer et React Context.
* Comment créer des applications mobiles réactives qui supportent les événements tactiles (comme le balayage mobile). 
* Intégrer TypeScript dans vos projets React.
* Tester les applications React.

J'ai créé ce cours parce que je crois que la programmation devrait être amusante et libérer la créativité. Plutôt que de créer une autre liste de tâches ou un panier d'achat, créons quelque chose que vous pouvez montrer à vos amis ou peut-être même à un responsable de recrutement !