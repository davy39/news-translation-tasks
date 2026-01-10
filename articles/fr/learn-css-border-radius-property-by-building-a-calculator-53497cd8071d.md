---
title: Apprenez la propriété CSS border-radius en construisant une calculatrice
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T14:01:49.000Z'
originalURL: https://freecodecamp.org/news/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lqgg0-J8JroKUWsmL8-S1w.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Apprenez la propriété CSS border-radius en construisant une calculatrice
seo_desc: 'By Jennifer Bland

  Have you ever seen a button on a web page that has rounded edges? Have you ever
  seen an image that fits within a circle? If so, you have seen the impact of using
  the CSS border-radius property.

  You can give any element “rounded corn...'
---

Par Jennifer Bland

Avez-vous déjà vu un bouton sur une page web avec des bords arrondis ? Avez-vous déjà vu une image qui s'inscrit dans un cercle ? Si oui, vous avez vu l'impact de l'utilisation de la propriété CSS border-radius.

Vous pouvez donner à n'importe quel élément des "coins arrondis" en appliquant un border-radius via CSS.

### Syntaxe de border-radius

Comme pour de nombreuses propriétés CSS relatives aux marges, au remplissage et aux bordures, il existe quatre propriétés individuelles — une pour chaque coin d'un élément de type boîte — et une propriété raccourcie. Chacun des attributs de coin acceptera une ou deux valeurs.

La propriété border-radius est acceptée dans tous les principaux navigateurs, mais ils ont des attributs spécifiques au navigateur. Voici les attributs CSS et spécifiques au navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/qnkEgNX3r6axXCWRrTIowIIYhuB9hddlmaQE)

Chacune des propriétés CSS3 individuelles pour les coins prend une ou deux valeurs de longueur (généralement des valeurs 'px' ou 'em'). Si une seule valeur est fournie, elle devient le rayon d'un coin arrondi. Si deux valeurs sont fournies, elles deviennent les rayons horizontal et vertical pour un coin elliptique.

La propriété border-radius elle-même accepte une ou deux valeurs et les utilise pour styliser les quatre coins, créant une forme symétrique.

### Doit-on encore utiliser les préfixes de bordure ?

Maintenant que je vous ai montré les préfixes de bordure spécifiques au navigateur, la question est : devez-vous vraiment les utiliser, ou pouvez-vous vous en passer en utilisant uniquement les propriétés CSS3 ?

La réponse simple à cette question dépend de la version des navigateurs que votre site web supporte.

Firefox 3.6 nécessite l'utilisation du préfixe `-moz-`. À partir de la version 4, l'utilisation des propriétés CSS3 est acceptable.

Safari 4 a besoin du préfixe `-webkit-`. Safari 5 et versions supérieures acceptent les propriétés CSS3.

iOS3 a besoin du préfixe `-webkit-`. Cela s'applique uniquement à un iPhone 3GS ou un iPad 1 qui n'ont jamais été mis à jour.

### **Démonstration de base de la propriété border-radius**

Voici deux démonstrations du border-radius. La valeur fournie pour la propriété peut être en px, rem, em ou %.

```
div {    width: 100px;    height: 100px;    background-color: #7db9e8;}#demo-one {    border-radius: 20px;}#demo-two {    border-radius: 50%;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/58inFWiFV2nf3gY0np2En3eiv-yT4v6me2TN)
_#demo-one image à gauche et #demo-two image à droite_

Pour la première div, un coin arrondi de 8px est appliqué à chaque coin de la div. Dans le deuxième exemple, chaque coin a un coin arrondi de 50% appliqué, ce qui crée un cercle.

Avec une seule valeur, le border-radius sera le même sur les quatre coins d'un élément comme montré ci-dessus. Vous avez la possibilité de spécifier une valeur différente pour chaque coin.

Lorsque vous spécifiez des valeurs individuelles, elles sont appliquées dans cet ordre : haut gauche, haut droit, bas droit, bas gauche. Voici un exemple :

```
#demo-three {    border-radius: 10em 20em 10em 20em;}#demo-four {    border-radius: 40px 5px;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/BGucle-f9GeDKujT0Lvpkd6NHoCU3hhEbDBW)
_#demo-three image à gauche et #demo-four image à droite_

### Bords elliptiques

Les bords n'ont pas besoin d'être circulaires, mais peuvent aussi être elliptiques. Pour créer un bord elliptique, vous placez une barre oblique (« / ») entre deux valeurs. Voici un exemple :

```
#demo-five {    border-radius: 10% / 50%;}#demo-six {    border-radius: 50% / 10%;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/98A58SmtXz8co6JdO13FcOcJ1bBWuBGEBq7u)
_#demo-five image à gauche et #demo-six image à droite_

### Création de notre calculatrice

Nous allons appliquer ce que nous venons d'apprendre sur le border-radius pour créer cette calculatrice :

![Image](https://cdn-media-1.freecodecamp.org/images/XfZMe9RBd87B6-whvzUyAAhyoC3Odc3iLufy)
_Image de la calculatrice que nous allons créer_

#### Cadre de la calculatrice

Tout d'abord, nous devons créer le cadre de notre calculatrice. Le haut de la calculatrice aura une arche et le bas aura des bords arrondis. Pour créer ce design, nous allons spécifier une valeur pour chaque coin individuel comme ceci :

```
.calc-frame {    display: flex;    flex-direction: column;    align-items: center;    max-height: 650px;    max-width: 400px;    width: 90%;    padding: 20px;    border: solid 5px #41403E;    border-top-left-radius: 270px 100px;    border-top-right-radius: 270px 100px;    border-bottom-right-radius: 35px;    border-bottom-left-radius: 35px;    background: #b1b1b1;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/158kfBelpvY3-QDnxL0KRwdc10d8IZyuAE7g)
_Image du cadre de la calculatrice créé avec le CSS ci-dessus_

#### Cadre du résultat de la calculatrice

Le haut de la calculatrice contient le total qui a été calculé (le résultat). Il est composé de deux parties : le cadre extérieur et la zone d'entrée qui contient le total. Le cadre extérieur utilise exactement le même border-radius que le cadre pour avoir la même arche. Voici le style pour ces deux éléments :

```
.calc-result-frame {    background: #fefefe;    border: solid 5px #41403E;    width: 100%;    height: 150px;    border-top-left-radius: 270px 100px;    border-top-right-radius: 270px 100px;    border-bottom-right-radius: 10px;    border-bottom-left-radius: 10px;    display: flex;    justify-content: center;    align-items: flex-end;}.calc-result-input {    width: 85%;    height: 70px;    text-align: right;    color: #41403E;    overflow: hidden;    font-size: 2rem;
```

![Image](https://cdn-media-1.freecodecamp.org/images/GQIskucMzloAzKnvRCVjgqsyXBXou7pGNTlY)
_Image du cadre du résultat de la calculatrice créé avec le CSS ci-dessus_

#### Logo et bouton d'alimentation de la calculatrice

Les prochains éléments à ajouter à notre calculatrice sont le logo, « BLAND INSTRUMENTS », et le bouton d'alimentation. Nous allons utiliser le code dans #demo-four pour le logo et le code dans #demo-two pour le bouton d'alimentation. Voici à quoi cela ressemble :

```
.calc-logo {    background: #41403e;    color: #e8eff0;    border: solid px #41403E;    border-radius: 40px 5px;    width: 250px;    height: 50px;    line-height: 50px;    font-weight: bold;    text-align: center;}.calc-on {    border-radius: 50%;    border: none;    background: #bb0f29;    color: #fefefe;    width: 50px;    height: 50px;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/xdYe0M5nEFA5-cuoK6lnZAQC-oOXanmmzlPG)
_Image montrant notre logo de calculatrice et le bouton d'alimentation du CSS ci-dessus_

#### Boutons de la calculatrice

Ensuite, nous allons créer un style pour chaque bouton de la calculatrice. Nous allons spécifier un style pour chaque coin individuel, puis fournir deux valeurs pour chaque coin. Cela produit un aspect fait à la main pour les boutons. Voici le code :

```
.calc-btn {    background: transparent;    color: #41403E;    font-size: 2rem;    width: 75px;    height: 75px;    outline: none;    border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;    border: solid 7px #41403E;    flex: 1;    transition: all .5s ease;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/zowOBlwKqRf1NKRRYRpEBPdc9DB-jUIgEI4h)
_Image montrant les boutons de la calculatrice utilisant le CSS ci-dessus_

#### Bouton Entrer

La dernière chose que nous devons ajouter à notre calculatrice est le bouton `ENTER`. Nous allons utiliser le code de #demo-one pour ce bouton. Voici le code :

```
.calc-enter {    background: #bb0f29;    color: #fefefe;    border-radius: 20px;    border: none;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/aWVrEsCdtTGBtWohqfF5qjGiGsd6MlJt143q)
_Image montrant les boutons Entrer de la calculatrice du CSS ci-dessus_

#### Animation des boutons

La dernière chose que nous allons ajouter à notre calculatrice est une animation pour chaque bouton lorsque l'utilisateur survole le bouton. Cela simule l'action du bouton étant réellement pressé.

Pour y parvenir, nous allons ajouter une ombre portée à nos boutons. C'est l'ombre qui sera affichée pour tous les boutons, et donne aux boutons l'apparence d'être légèrement surélevés par rapport au cadre de la calculatrice.

Pour fournir l'animation, nous allons ajouter une transition au bouton. Ensuite, nous fournirons une ombre portée différente pour les boutons lorsque l'utilisateur les survole. Voici le code :

```
.calc-btn {    background: transparent;    color: #41403E;    font-size: 2rem;    width: 75px;    height: 75px;    outline: none;    border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;    border: solid 7px #41403E;    flex: 1;    box-shadow: 20px 38px 34px -26px hsla(0,0%,0%,.2);    transition: all .5s ease;}.calc-btn:hover {    box-shadow:2px 8px 4px -6px hsla(0,0%,0%,.3);}
```

Et voici notre calculatrice terminée :

![Image](https://cdn-media-1.freecodecamp.org/images/CwnpB7nIh11k5CkmnjjjAGZqZveSnB3jCYXX)
_Image montrant l'animation des boutons de la calculatrice du CSS ci-dessus_

### Obtenez le code

Si vous souhaitez voir le code complet de la calculatrice, vous pouvez l'obtenir depuis mon [dépôt GitHub ici](https://github.com/ratracegrad/border-radius). Veuillez mettre une étoile à mon dépôt lorsque vous obtenez le code !

Le code utilise Flexbox pour la mise en page de la calculatrice. Si vous n'êtes pas familier avec Flexbox ou souhaitez le réviser, vous pouvez consulter mon cours de formation gratuit sur Flexbox sur [in5days.tech](https://www.in5days.tech/).

### Merci d'avoir lu

Merci d'avoir lu mon article. Si vous l'aimez, veuillez cliquer sur l'icône d'applaudissements ci-dessous afin que d'autres trouvent cet article.

Voici d'autres articles que vous pourriez trouver intéressants :

[Voici 5 mises en page que vous pouvez faire avec FlexBox](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)
[Pensez hors de la boîte avec la propriété CSS shape-outside](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)
[Pourquoi la culture d'entreprise est importante pour votre carrière en tant qu'ingénieur logiciel](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)