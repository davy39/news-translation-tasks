---
title: Suivez ces étapes pour devenir une superstar CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T15:42:16.000Z'
originalURL: https://freecodecamp.org/news/follow-these-steps-to-become-a-css-superstar-837cd6cb9b1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H0IBb9kvGI3eIuL1sGmWug.jpeg
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Suivez ces étapes pour devenir une superstar CSS
seo_desc: 'By Preetish HS

  CSS (Cascading Style Sheets) is one of the core technologies used for building webpages.
  Since it is the ONLY style sheet language that browsers can understand, it''s important
  to learn CSS in depth to master web development.

  It’s very ...'
---

Par Preetish HS

CSS (Cascading Style Sheets) est l'une des technologies principales utilisées pour construire des pages web. Puisqu'il s'agit du SEUL langage de feuille de style que les navigateurs peuvent comprendre, il est important d'apprendre CSS en profondeur pour maîtriser le développement web.

Il est très facile de commencer avec CSS. Avec seulement quelques heures de formation, vous pouvez facilement styliser des textes, des éléments et des mises en page. Cependant, cela devient progressivement difficile et bientôt vous vous retrouverez dans une situation où votre code commence à devenir assez désordonné. Les composants qui fonctionnaient avant commencent à se casser, et vous cherchez sur Google et trouvez la solution qui corrige votre élément mais en casse 5 autres, car la solution que vous avez trouvée sur Google a changé le `display` ou `position` ?

### **Pourquoi apprendre CSS de la bonne manière est important**

Si vous n'avez pas une compréhension approfondie des bases, CSS devient plus une méthode d'**essais et d'erreurs**. Vous essaierez différentes valeurs pour différentes propriétés et garderez finalement celle qui fonctionne à peu près comme vous le vouliez sans vraiment comprendre comment cela fonctionne.

Vous commencerez à chercher sur Google des choses basiques comme **"comment centrer deux divs"** ou **"comment aligner un div et un texte verticalement"** et copierez-collerez le code de StackOverflow ou CodePen à chaque fois. À l'époque, lorsque **flexbox** n'était pas si populaire, **"comment aligner un div à la fois verticalement et horizontalement dans une page ?"** était une question classique d'entretien sur CSS. De nombreux débutants pouvaient réussir la partie horizontale, mais seuls quelques-uns réussissaient aussi la partie verticale.

### La feuille de route ??

#### **1. Les bases ?**

Si vous commencez tout juste le développement web, apprenez quelques bases de [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) avant de commencer CSS. En CSS, lisez d'abord la théorie sur ce qu'est CSS, comment il fonctionne dans le navigateur, et sa syntaxe et utilisation de base.

Apprenez les différents types de feuilles de style disponibles, leurs différences, les sélecteurs et le style de base tel que `font-size`, `width`, `height`, etc.

Vous pouvez commencer en suivant les tutoriels sur [MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS).

#### **2. Le modèle de boîte CSS ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*HnuCN_p4MiCMtOp7ziLpnA.png)
_crédit : [https://developer.mozilla.org](https://developer.mozilla.org" rel="noopener" target="_blank" title=")_

Comprenez les bases du [modèle de boîte CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Box_model) et les propriétés qui y sont associées, telles que `margin`, `border`, `padding`, etc.

#### **3. Images et arrière-plan ?**

Les images donnent vie à la page web. Il existe de nombreuses façons d'ajouter une image, comme les balises d'image, l'ajout de couleurs/gradients d'arrière-plan et d'images d'arrière-plan à diverses autres balises. Vous pouvez également appliquer ce que vous avez appris précédemment, comme définir des bordures pour les images ou utiliser plusieurs images et développer une galerie simple.

```
<img src="../images/wallpaper.jpg" ><div class="image" > </div>
```

```
.image {   background-image: url(../images/wallpaper.jpg);}
```

#### **4. Affichage et position ?**

Ces deux propriétés sont parmi les plus importantes en CSS, où vous devez prêter attention pour les comprendre correctement. Connaître ces deux propriétés peut rendre votre parcours CSS beaucoup plus fluide.

```
 display: block | inline | inline-block | table | etc
```

Comprenez comment chacune de ces propriétés `display` est utilisée. Vous commencerez à remarquer que certains éléments HTML tels que `<div>`, `<p>` ou `<h1>` se comportent comme `display: block` et que certains éléments comme `<img>`, `<span>` se comportent comme `display: inline`.

```
position: static | absolute | relative | fixed | sticky
```

Il s'agit de l'une des propriétés où même les programmeurs expérimentés font des erreurs. Apprenez comment chacune d'elles fonctionne, comment la position d'un élément affecte ses frères et sœurs ou son parent, dans quelles situations vous les utilisez, etc.

**_Cette étape est si importante que vous pouvez la répéter encore et encore jusqu'à ce que vous compreniez !_**

```
float: left | right
```

Bien que les mises en page flottantes soient un peu dépassées maintenant, il existe de nombreux anciens sites web qui utilisent encore des mises en page flottantes.

#### **5. Couleurs, polices, listes et tableaux ✓**

Comprenez les différents formats de couleurs tels que le code `HEX`, `rgb`, `rgba`, `hsl`, `hsla`, `transparent`, etc.

```
color: white;color: #fff;color: rgb(255, 255, 255);color: rgba(255, 255, 255, 1);color: hsl(0, 100%, 100%);color: hsla(0, 100%, 100%, 1);color: transparent;
```

Apprenez à utiliser différentes polices. Certaines polices ne sont pas disponibles sur tous les navigateurs, vous devrez donc apprendre à ajouter des polices manuellement avec des fichiers `woff` ou `ttf` ou en important des polices Google.

CSS peut transformer une liste non ordonnée de base `<ul>` en une belle barre de navigation ! Il y a des années, les tableaux étaient utilisés pour créer des mises en page d'écran, heureusement, nous ne faisons plus cela ! ?

#### **6. Pseudo-classes et combinateurs ➕**

Une **pseudo-classe** CSS est un mot-clé ajouté à un sélecteur qui spécifie un état spécial de l'élément ou des éléments sélectionnés. Une pseudo-classe peut être aussi simple que `:hover` ou `:visited` ou quelque chose de complexe comme `:nth-last-of-type(odd)`.

Les **combinateurs** nous aident à appliquer des styles aux éléments enfants ou aux frères et sœurs facilement sans avoir à créer de nouvelles classes pour chacun d'eux.

```
/* tous les éléments de paragraphe à l'intérieur du conteneur auront la couleur rouge */
```

```
.container > p {  color: yellow;}
```

#### **7. Débogage et outils de développement ?**

CSS ne génère aucune erreur. Il casse silencieusement l'interface utilisateur si vous n'obtenez pas les styles corrects ? donc apprendre à utiliser les outils de développement est très important.

Les outils de développement Chrome sont un outil incroyable pour les développeurs web. Ils sont remplis de nombreuses fonctionnalités pour déboguer votre site web en temps réel et disposent également d'outils de vérification des performances comme [**lighthouse**](https://developers.google.com/web/tools/lighthouse/) intégrés.

#### **8. Pratique, pratique, pratique ?**

![Image](https://cdn-media-1.freecodecamp.org/images/0*RapmXy8eJSyb2OX6)
_Photo par [Unsplash](https://unsplash.com/@rangel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">David Rangel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Le contenu que vous avez appris ci-dessus est suffisant pour développer un site web de base, donc à ce stade, vous devriez commencer à pratiquer en développant de petits sites web. Vous rencontrerez divers défis lorsque vous construirez une application réelle. Pour votre pratique, vous pouvez développer un site web simple pour un resort, ou construire une galerie d'images, ou un blog, ou vous pouvez également construire quelques fonctionnalités de base de votre réseau social préféré comme Facebook ou Instagram.

#### **9. Conception Web Responsive ??**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ScNanqYCmVsKnRaPWosYIw.png)
_crédit : Wikipedia_

**Après avoir appris le développement web pour le bureau, il existe de nombreux autres appareils à travers lesquels les sites web sont accessibles. Prendre en charge ces appareils est tout aussi important. Avant que la conception Responsive ne devienne populaire, les développeurs concevaient un site web séparé pour les mobiles, un site web séparé pour les appareils tactiles, etc. vous souvenez-vous de _m.facebook.com_ et _touch.facebook.com_ ?**

**Il y a 3 choses importantes dans la conception web Responsive :**

**Mises en page fluides :**

**La largeur définie avec `px` ne s'adapte pas en fonction de la fenêtre du navigateur. Pour que les éléments s'adaptent en fonction de la taille du navigateur, nous devons créer des mises en page fluides en définissant les tailles en `%` ou en unités `rem`.**

**Requêtes média :**

**Une requête média est une technique pour inclure un bloc de propriétés CSS uniquement si une certaine condition est vraie. Nous définissons des points d'arrêt en fonction de notre conception et changeons le CSS en fonction de la largeur du navigateur.**

**`@media only screen and (max-width: 600px) {`**  
  **`body {`**  
    **`background-color: lightblue;`**  
  **`}`**  
**`}`**

**Images responsives :**

**Les images s'adaptent à la baisse lorsque la largeur de la fenêtre du navigateur diminue ou si le site web est consulté sur des appareils mobiles. Parfois, il serait difficile de se concentrer sur les détails importants d'une image particulière, donc nous aurions besoin d'utiliser différentes images pour différents écrans.**

#### **10. Flexbox et Grid ⬜ ⬡ ?**

**Cela fait environ 10 ans (!) que Flexbox a été introduit pour la première fois, mais il n'a été incorporé que récemment en 2015. — [source](http://annairish.github.io/historicizing/history)**

**Flexbox et Grid sont les styles utilisés pour créer des mises en page flexibles, et ils rendent notre vie tellement plus facile ! C'est l'une des meilleures choses qui soit arrivée à CSS. ?**

**La mise en page montrée ci-dessous aurait pris plus de 300 lignes de code CSS sans Flexbox ou Grid.**

#### **11. Transformations, transitions et animations ?**

**Apprendre les transformations et transitions de base sera utile si vous souhaitez créer une page web interactive avec des parties mobiles sur des événements de souris ou de clavier tels que le survol ou le clic.**

**Avant CSS3, les animations étaient principalement réalisées en utilisant jQuery — une bibliothèque JavaScript. Maintenant, CSS est devenu si puissant que nous pouvons faire des animations complexes sans aucun JavaScript.**

#### **12. Préprocesseurs ✝️**

Les **préprocesseurs CSS** sont des langages de script qui étendent les capacités par défaut de CSS. Ils nous permettent d'utiliser la logique dans notre code CSS, comme des variables, l'imbrication, l'héritage, les mixins, les fonctions et les opérations mathématiques. Certains des plus populaires sont [SASS](http://sass-lang.com/), [LESS](http://lesscss.org/), [STYLUS](http://stylus-lang.com/) et [POSTCSS](http://postcss.org/).

**Le format **SCSS** de SASS est plus largement utilisé, il est donc bon de commencer avec SASS pour le développement.**

**Le plugin `autoprefixer` de POSTCSS rend vos règles CSS compatibles avec divers navigateurs en ajoutant des règles supplémentaires telles que `-moz-` et `-webkit-`.**

#### **13. Frameworks** ?

**Apprendre des frameworks tels que [Bootstrap](http://getbootstrap.com/), [Semantic-UI](http://semantic-ui.com/) ou [Materialize](http://materializecss.com/) est optionnel mais très utile pour un développement plus rapide, car ils fournissent de nombreux styles et mises en page prêts à l'emploi.**

**Ces frameworks sont testés sur divers navigateurs, donc leur utilisation évitera certains problèmes de compatibilité. La plupart des frameworks suivent le modèle de conception responsive et de nombreux templates tiers gratuits sont disponibles pour commencer rapidement.**

#### **14. Spécificité** ?

**"_essaie de modifier un style de bouton de bootstrap mais échoue, cherche une solution sur Google, utilise `!important`, s'enthousiasme en pensant que c'est la bonne solution pour tous les problèmes !_" Et c'est ainsi que vous avez condamné votre projet ! ? Si vous comprenez correctement le concept de **spécificité**, les problèmes concernant les règles chevauchantes dans plusieurs feuilles de style seront considérablement réduits.**

**La spécificité est un poids qui est appliqué à une déclaration CSS donnée, déterminé par le nombre de chaque type de sélecteur dans le sélecteur correspondant. Chaque sélecteur a un poids différent, et l'utilisation de plusieurs sélecteurs peut changer la spécificité. Si les spécificités globales sont égales, l'ordre est alors considéré. Voir l'exemple ci-dessous :**

**`<style>div.wrapper p.paragraph {`**  
   **`color: pink;`**  
**`}#container p{`**  
   **`color: violet;`**  
**`}p {`**  
  **`color: green;`**  
**`}.paragraph {`**  
  **`color: yellow;`**  
**`}`**  
**`</style><div class="wrapper" id="container">`**  
   **`<p class="paragraph"> This is a dummy text </p>`**  
**`</div>`**

**Selon vous, quelle serait la couleur du paragraphe ? ?**

#### **15. Architecture CSS ?**

**Écrire du code CSS est facile, mais écrire du code CSS maintenable est difficile. Une structure et une méthode appropriées doivent être suivies pour écrire du bon code CSS. Suivre simplement les meilleures pratiques ne suffit pas pour écrire du CSS maintenable.**

**Certains des modèles d'architecture pour CSS sont [BEM](http://getbem.com/introduction/), [OOCSS](http://oocss.org/), [SMACSS](https://smacss.com/) etc. Vous pouvez parcourir la documentation et choisir le modèle qui correspond à vos goûts et à votre projet.**

### **Voilà ! ?**

**Maîtriser CSS demande de la patience et beaucoup de pratique. En commençant à pratiquer, vous découvrirez l'incroyable puissance de CSS. Les 15 grandes étapes peuvent sembler intimidantes au début, mais elles ne le sont pas vraiment. J'ai aimé chaque étape, et mon expérience s'est améliorée à chaque fois. ?**

**Merci d'avoir lu mon article. J'espère que vous l'avez trouvé utile. Si c'est le cas, n'oubliez pas de laisser beaucoup d'applaudissements ! ? (Vous pouvez laisser jusqu'à 50 ?)**

#### **Vous souhaitez m'engager pour votre prochain projet ? Envoyez-moi un email à contact@preetish.in ?**