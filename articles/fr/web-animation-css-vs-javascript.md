---
title: Techniques d'animation Web – CSS vs JavaScript
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-19T14:54:50.000Z'
originalURL: https://freecodecamp.org/news/web-animation-css-vs-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Addition-and-Subtraction-Word-Problems-Math-Presentation-Orange-in-Pink-and-Purple-Groovy-Style.png
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: Techniques d'animation Web – CSS vs JavaScript
seo_desc: "Animations play a vital role in enhancing user experience on web pages.\
  \ They add interactivity, visual appeal, and engagement to websites and web applications.\
  \ \nTwo popular methods for creating web animations are Cascading Style Sheets (CSS)\
  \ and Java..."
---

Les animations jouent un rôle vital dans l'amélioration de l'expérience utilisateur sur les pages web. Elles ajoutent de l'interactivité, de l'attrait visuel et de l'engagement aux sites web et aux applications web.

Deux méthodes populaires pour créer des animations web sont les feuilles de style en cascade (CSS) et JavaScript. Chacune de ces techniques a ses forces et ses cas d'utilisation, et comprendre quand utiliser l'une plutôt que l'autre est crucial pour les développeurs web.

Dans cet article, nous allons explorer les différences clés entre les animations CSS et JavaScript, fournir des exemples de code et vous guider sur quand choisir l'une plutôt que l'autre.

## Animations CSS

CSS (Cascading Style Sheets) est couramment utilisé pour styliser les pages web. Mais il offre également un moyen puissant et simple de créer des animations.

Les animations CSS sont principalement utilisées pour des animations simples et déclaratives comme les transitions, les keyframes et les transformations.

### Exemple de transition CSS

Tout d'abord, examinons un exemple de transition CSS simple :

```css
.button {
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #3498db;
}
```

<html>
<head>
  <style> 
      .button {
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #3498db;
}
    </style>
</head>
<body>
  <button class="button">Survolez-moi</button>
</body>
</html>

Dans l'exemple ci-dessus, la couleur de fond du bouton passera en douceur à une nouvelle couleur lorsque l'utilisateur le survolera. Cela est réalisé en utilisant la propriété `transition`.

Apprenons un peu plus sur le fonctionnement de la propriété `transition` :

* `background-color` : Il s'agit de la propriété CSS animée. Dans ce cas, il s'agit de la couleur de fond du bouton.
* `0.3s` : Il s'agit de la durée de l'animation. Elle spécifie combien de temps la transition prend pour se terminer (0,3 seconde dans cet exemple).
* `ease-in-out` : Il s'agit de la fonction de temporisation qui contrôle la courbe de vitesse de l'animation. Elle commence lentement, accélère au milieu et ralentit à la fin.
* `0s` : Il s'agit du délai avant le début de l'animation (dans ce cas, il n'y a pas de délai).

### Exemple de Keyframes

Les keyframes sont un autre type d'animation CSS que vous pouvez utiliser pour styliser vos éléments. Voici un exemple en action :

```css
@keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }

        .element {
            width: 100px;
            height: 100px;
            background-color: #3498db;
            animation: pulse 2s ease-in-out infinite;
        }
```

Résultat :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animation Pulse</title>
    <style>
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }

        .element {
            width: 100px;
            height: 100px;
            background-color: #3498db;
            animation: pulse 2s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <div class="element"></div>
</body>
</html>

Dans cet exemple :

* Nous définissons une règle `@keyframes` nommée "pulse" qui spécifie trois keyframes à 0%, 50% et 100% de la durée de l'animation. Elle utilise la propriété `transform` pour mettre à l'échelle l'élément.
* La classe CSS `.element` définit la couleur de fond initiale et applique l'animation "pulse" avec une durée de 2 secondes, une fonction de temporisation "ease-in-out" et la valeur "infinite", ce qui signifie que l'animation se répétera indéfiniment.
* À l'intérieur du `<body>`, il y a un élément `<div>` avec la classe "element" qui subira l'animation "pulse" lorsque la page se chargera.

Lorsque vous ouvrez ce fichier HTML dans un navigateur web, l'élément pulsera ou "respirera" en mettant à l'échelle en douceur la taille, créant une animation simple mais accrocheuse.

### Autres techniques d'animation CSS :

Il existe d'autres techniques d'animation CSS, notamment :

* **Transformations** : CSS peut être utilisé pour effectuer des transformations 2D et 3D comme la mise à l'échelle, la rotation et la translation des éléments.
* **Keyframes** : Comme montré dans l'exemple ci-dessus, les keyframes vous permettent de créer des animations plus complexes en spécifiant plusieurs étapes ou keyframes dans une séquence d'animation.
* **Autres types de transitions CSS** : En plus des transitions basées sur les propriétés, vous pouvez également utiliser des transitions pour plusieurs propriétés, vous permettant de créer des animations plus complexes.

### Avantages des animations CSS

* **Facile à utiliser** : Les animations CSS sont relativement simples à implémenter, surtout pour les animations de base comme les transitions et les fondu.
* **Performance** : Elles sont accélérées par le matériel et offrent généralement de bonnes performances, assurant une expérience utilisateur fluide.
* **Design réactif** : Les animations CSS sont intrinsèquement réactives et s'adaptent à différentes tailles d'écran et appareils.
* **Faible surcharge JavaScript** : L'utilisation de CSS pour les animations peut réduire la charge sur JavaScript, rendant votre application web plus efficace.
* **Compatibilité des navigateurs** : Les animations CSS sont largement supportées dans les navigateurs modernes. Mais il est important de noter qu'il peut y avoir des problèmes de compatibilité avec les versions plus anciennes d'Internet Explorer (IE) et certains navigateurs mobiles. Dans de tels cas, il peut être nécessaire de fournir une dégradation élégante ou des designs alternatifs pour les utilisateurs sur les anciens navigateurs.

## Animations JavaScript

JavaScript est un langage de programmation polyvalent utilisé pour une large gamme de tâches, y compris la création d'animations complexes. Les animations JavaScript sont généralement plus flexibles et capables de gérer des animations complexes et basées sur des données.

### Animations JS utilisant la méthode `requestAnimationFrame`

```javascript
     const box = document.getElementById('animated-box');
        let isAnimating = false;

        box.addEventListener('click', () => {
            if (!isAnimating) {
                isAnimating = true;
                box.style.transform = 'translateX(200px)';
                
                setTimeout(() => {
                    isAnimating = false;
                    box.style.transform = 'translateX(0)';
                }, 1000);
            }
        });
```

Résultat :

<!DOCTYPE html>
<html>
<head>
    <style>
        #animated-box {
            width: 100px;
            height: 100px;
            background-color: #FF5733;
            position: relative;
            transition: transform 1s ease;
        }
    </style>
</head>
<body>
    <div id="animated-box">Cliquez-moi</div>

    <script>
        const box = document.getElementById('animated-box');
        let isAnimating = false;

        box.addEventListener('click', () => {
            if (!isAnimating) {
                isAnimating = true;
                box.style.transform = 'translateX(200px)';
                
                setTimeout(() => {
                    isAnimating = false;
                    box.style.transform = 'translateX(0)';
                }, 1000);
            }
        });
    </script>
</body>
</html>

Dans l'exemple d'animation JavaScript, la méthode `requestAnimationFrame` est utilisée pour créer une animation simple où une boîte se déplace horizontalement lorsqu'elle est cliquée. Cette méthode est souvent utilisée pour des animations plus fluides et plus complexes.

Dans cet exemple,

* Nous utilisons `document.getElementById('animated-box')` pour sélectionner l'élément HTML avec l'ID "animated-box" et l'assigner à la variable `box`.
* Nous déclarons également une variable booléenne `isAnimating` pour suivre si une animation est actuellement en cours.
* Nous ajoutons un écouteur d'événement à l'élément `box` qui écoute un événement de clic.
* Lorsque la boîte est cliquée, l'écouteur d'événement déclenche une fonction anonyme qui vérifie si une animation est déjà en cours (`isAnimating`). Si ce n'est pas le cas, elle définit `isAnimating` sur `true`.
* Elle modifie ensuite la propriété `transform` de la boîte en `translateX(200px)`. Cela déplace la boîte de 200 pixels vers la droite, créant un effet d'animation horizontale.
* Après un délai d'une seconde (spécifié par `setTimeout`), elle définit `isAnimating` sur `false` et réinitialise la propriété `transform` à son état d'origine (`translateX(0)`), ramenant la boîte à sa position initiale.

Ce code crée une animation simple où cliquer sur la boîte la déplace horizontalement vers la droite puis la ramène à sa position d'origine, le tout en une durée d'une seconde. La propriété CSS `transition` garantit que le mouvement est fluide et visuellement attrayant.

### Autres méthodes courantes d'animation JavaScript

* **jQuery** : jQuery est une bibliothèque JavaScript populaire qui simplifie les tâches d'animation, facilitant la création d'animations avec moins de code.
* **GreenSock Animation Platform (GSAP)** : GSAP est une bibliothèque d'animation robuste pour JavaScript qui offre des capacités d'animation avancées et un contrôle précis sur les animations.
* **Animation Canvas** : Le canvas HTML5 peut être utilisé pour créer des animations personnalisées, notamment pour les jeux et les visualisations.
* **Web Animation API** : Cette API native du navigateur fournit une interface JavaScript pour contrôler les animations sur les pages web, permettant un meilleur contrôle des animations par rapport à CSS.
* **Animations SVG** : Vous pouvez créer des animations complexes dans les graphiques vectoriels scalables (SVG) en utilisant JavaScript pour manipuler les éléments SVG.

### Avantages des animations JavaScript

* **Animations complexes** : JavaScript offre une plus grande flexibilité, ce qui le rend adapté aux animations complexes avec un comportement dynamique.
* **Interactivité** : Vous pouvez facilement ajouter des interactions utilisateur, telles que la fonctionnalité de glisser-déposer, grâce aux animations JavaScript.
* **Animations basées sur les données** : JavaScript vous permet de créer des animations basées sur des données, ce qui le rend idéal pour visualiser du contenu dynamique.
* **Mises à jour en temps réel** : Les animations JavaScript peuvent être utilisées pour des mises à jour en temps réel et des animations synchronisées avec d'autres parties de l'application web.
* **Implications de performance** : Les animations JavaScript peuvent parfois être intensives en ressources, en particulier sur les appareils mobiles ou le matériel moins puissant. Les développeurs doivent être prudents lors de la mise en œuvre d'animations JavaScript complexes sur ces plateformes pour garantir une expérience utilisateur fluide.

## Quand utiliser CSS vs JavaScript pour les animations

### Quand utiliser CSS pour les animations :

CSS est souvent le meilleur choix pour les animations de base comme les effets de survol, les transitions et les petites animations non interactives.

Les animations CSS sont généralement plus fluides et plus efficaces, ce qui les rend idéales pour les scénarios critiques en termes de performance.

Et lorsque vous concevez des sites web réactifs, les animations CSS s'adaptent à différentes tailles d'écran de manière transparente.

### Quand utiliser JavaScript pour les animations :

En revanche, lorsque vous devez créer des animations complexes avec des éléments dynamiques, JavaScript offre la flexibilité et le contrôle nécessaires.

De plus, si vos animations doivent répondre aux interactions de l'utilisateur, les animations JavaScript doivent être votre option de prédilection.

JavaScript est également essentiel pour créer des graphiques et des diagrammes interactifs pour les animations basées sur les données.

Et enfin, lorsque vous avez besoin de mises à jour en temps réel ou d'animations synchronisées, JavaScript est le meilleur choix pour le contenu dynamique.

## Comment combiner les animations CSS et JavaScript

Dans certains scénarios, une approche hybride utilisant à la fois les animations CSS et JavaScript peut offrir le meilleur des deux mondes.

Par exemple, vous pourriez utiliser CSS pour les animations initiales et les transitions qui se produisent lorsque la page se charge, puis employer JavaScript pour les interactions utilisateur, les mises à jour en temps réel ou les animations basées sur les données. Cette combinaison peut offrir les avantages d'efficacité et de performance de CSS avec l'interactivité et les capacités dynamiques de JavaScript.

Consultez le Codepen suivant pour un exemple :

%[https://codepen.io/joanayebola/pen/wvRLKbQ]

## Conclusion

Les animations web sont un élément crucial du développement web moderne, améliorant l'expérience utilisateur et l'engagement.

Le choix entre CSS et JavaScript pour les animations dépend de la complexité de votre projet, du niveau d'interactivité requis et de vos besoins en termes de performance.

Pour les animations simples et critiques en termes de performance, CSS est souvent le meilleur choix, tandis que JavaScript est l'option privilégiée pour les animations complexes, interactives et basées sur les données.

N'oubliez pas que dans de nombreux cas, une combinaison de CSS et de JavaScript peut être l'approche la plus efficace. En comprenant les forces de chaque technique et quand les appliquer, vous pouvez créer des animations web qui captivent votre audience et élèvent vos projets de développement web.