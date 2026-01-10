---
title: Table des matières
date: '2022-02-07T15:56:18.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/css-button-style-hover-color-and-background
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/moises-de-paula-HPZZHJ-LuDI-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_desc: 'In this article you''ll see how to style a button using CSS.

  My goal here is mostly to showcase how different CSS rules and styles are applied
  and used. We won''t see much design inspiration nor will we discuss ideas for styling.

  Instead, this will be ...'
---


Dans cet article, vous verrez comment styliser un bouton à l'aide de CSS.

<!-- more -->

Mon objectif ici est principalement de montrer comment différentes règles et styles CSS sont appliqués et utilisés. Nous ne verrons pas beaucoup d'inspiration en matière de design et nous ne discuterons pas d'idées de stylisation.

Au lieu de cela, il s'agira plutôt d'un aperçu du fonctionnement des styles eux-mêmes, des propriétés couramment utilisées et de la manière dont elles peuvent être combinées.

Vous verrez d'abord comment créer un bouton en HTML. Ensuite, vous apprendrez comment surcharger les styles par défaut des boutons. Enfin, vous aurez un aperçu de la manière de styliser les boutons pour leurs trois états différents.

### Voici un Scrim interactif sur le style des boutons CSS

<iframe src="https://scrimba.com/scrim/co3524355bcd2543752fa537c?pl=pBe55fP&amp;embed=freecodecamp,mini-header" width="100%" height="420" title="Embedded content" loading="lazy"></iframe>

# Table des matières

1.  [Créer un bouton en HTML][1]
2.  [Modifier le style par défaut des boutons][2]
    1.  [Modifier la couleur d'arrière-plan][3]
    2.  [Modifier la couleur du texte][4]
    3.  [Modifier le style de bordure][5]
    4.  [Modifier la taille][6]
3.  [Styliser les états des boutons][7]
    1.  [Styliser l'état hover][8]
    2.  [Styliser l'état focus][9]
    3.  [Styliser l'état active][10]
4.  [Conclusion][11]

C'est parti !

## Comment créer un bouton en HTML

Pour créer un bouton, utilisez l'élément `<button>`.

C'est une option plus accessible et sémantique que l'utilisation d'un conteneur générique créé avec l'élément `<div>`.

Dans le fichier `index.html` ci-dessous, j'ai créé la structure de base d'une page web et ajouté un seul bouton :

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>CSS Button Style</title>
</head>
<body>
    <button type="button" class="button">Click me!</button>
</body>
</html>
```

Analysons la ligne `<button type="button" class="button">Click me!</button>` :

-   Vous ajoutez d'abord l'élément bouton, qui se compose d'une balise ouvrante `<button>` et d'une balise fermante `</button>`.
-   L'attribut `type="button"` dans la balise ouvrante `<button>` crée explicitement un bouton cliquable. Comme ce bouton particulier n'est pas utilisé pour soumettre un formulaire, il est utile pour des raisons sémantiques de l'ajouter afin de rendre le code plus clair et de ne déclencher aucune action indésirable.
-   L'attribut `class="button"` sera utilisé pour styliser le bouton dans un fichier CSS séparé. La valeur `button` pourrait être n'importe quel autre nom de votre choix. Par exemple, vous auriez pu utiliser `class="btn"`.
-   Le texte `Click me!` est le texte visible à l'intérieur du bouton.

Tous les styles qui seront appliqués au bouton iront dans un fichier `style.css` séparé.

Vous pouvez appliquer les styles au contenu HTML en reliant les deux fichiers ensemble. Vous le faites avec la balise `<link rel="stylesheet" href="style.css">` qui a été utilisée dans `index.html`.

Dans le fichier `style.css`, j'ai ajouté un style qui centre uniquement le bouton au milieu de la fenêtre du navigateur.

Notez que la `class="button"` est utilisée avec le sélecteur `.button`. C'est une façon d'appliquer des styles directement au bouton.

```
* {
    box-sizing: border-box;
} 

body {
    display:flex;
    justify-content: center;
    align-items: center;
    margin:50px auto;
}

.button {
    position: absolute;
    top:50%
}
```

Le code ci-dessus donnera le résultat suivant :

![Screenshot-2022-02-06-at-10.29.02-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.29.02-PM.png)

Le style par défaut des boutons variera en fonction du navigateur que vous utilisez.

Ceci est un exemple de l'apparence des styles natifs pour les boutons sur le navigateur Google Chrome.

## Comment modifier le style par défaut des boutons

### Comment modifier la couleur d'arrière-plan des boutons

Pour modifier la couleur d'arrière-plan du bouton, utilisez la propriété CSS `background-color` et donnez-lui la valeur d'une couleur de votre choix.

Dans le sélecteur `.button`, vous utilisez `background-color:#0a0a23;` pour changer la couleur d'arrière-plan du bouton.

```
.button {
    position: absolute;
    top:50%;
    background-color:#0a0a23;
}
```

![Screenshot-2022-02-06-at-10.28.30-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.28.30-PM.png)

### Comment modifier la couleur du texte des boutons

La couleur par défaut du texte est le noir, donc lorsque vous ajoutez une couleur d'arrière-plan sombre, vous remarquerez que le texte a disparu.

Une autre chose à vérifier est qu'il y a suffisamment de contraste entre la couleur d'arrière-plan du bouton et la couleur du texte. Cela aide à rendre le texte plus lisible et agréable à l'œil.

Ensuite, utilisez la propriété `color` pour changer la couleur du texte :

```
.button {
    position: absolute;
    top:50%;
    background-color:#0a0a23;
    color: #fff;
}
```

![Screenshot-2022-02-06-at-10.28.03-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.28.03-PM.png)

### Comment modifier le style de bordure des boutons

Remarquez le gris sur les bords du bouton ? C'est la couleur par défaut des bordures du bouton.

Une façon de corriger cela est d'utiliser la propriété `border-color`. Vous définissez la valeur pour qu'elle soit la même que celle de `background-color`. Cela garantit que les bordures ont la même couleur que l'arrière-plan du bouton.

Une autre façon serait de supprimer entièrement la bordure autour du bouton en utilisant `border:none;`.

```
.button {
  position: absolute;
  top:50%;
  background-color:#0a0a23;
  color: #fff;
  border:none;
}
```

![Screenshot-2022-02-06-at-10.27.33-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.27.33-PM.png)

Ensuite, vous pouvez également arrondir les bords du bouton en utilisant la propriété `border-radius`, comme ceci :

```
.button {
    position: absolute;
    top:50%;
    background-color:#0a0a23;
    color: #fff;
    border:none;
    border-radius:10px;
  }
```

![Screenshot-2022-02-06-at-10.26.57-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.26.57-PM.png)

Vous pourriez également ajouter un léger effet d'ombre portée autour du bouton en utilisant la propriété `box-shadow` :

```
 position: absolute;
    top:50%;
    background-color:#0a0a23;
    color: #fff;
    border:none;
    border-radius:10px;
    box-shadow: 0px 0px 2px 2px rgb(0,0,0);
```

![Screenshot-2022-02-06-at-10.25.55-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.25.55-PM.png)

### Comment modifier la taille des boutons

La façon de créer plus d'espace à l'intérieur des bordures du bouton est d'augmenter le `padding` du bouton.

Ci-dessous, j'ai ajouté une valeur de 15px pour le padding supérieur, inférieur, droit et gauche du bouton.

J'ai également défini une hauteur et une largeur minimales, avec les propriétés `min-height` et `min-width` respectivement. Les boutons doivent être suffisamment grands pour tous les différents types d'appareils.

```
.button {
    position: absolute;
    top:50%;
    background-color:#0a0a23;
    color: #fff;
    border:none; 
    border-radius:10px; 
    padding:15px;
    min-height:30px; 
    min-width: 120px;
  }
```

![Screenshot-2022-02-06-at-10.42.58-PM](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-06-at-10.42.58-PM.png)

## Comment styliser les états des boutons

Les boutons ont trois états différents :

-   `:hover`
-   `:focus`
-   `:active`

Il est préférable que les trois états soient stylisés différemment et ne partagent pas les mêmes styles.

Dans les sections suivantes, je donnerai une brève explication sur la signification de chacun de ces états et ce qui les déclenche. Vous verrez également quelques façons de styliser le bouton pour chaque état distinct.

### Voici un scrim interactif sur la stylisation des états de boutons :

<iframe src="https://scrimba.com/scrim/coa4a454f9e83e63fbe1a80ed?pl=pBe55fP&amp;embed=freecodecamp,mini-header" width="100%" height="420" title="Embedded content" loading="lazy"></iframe>

### Comment styliser l'état `:hover`

L'état `:hover` devient présent lorsqu'un utilisateur survole un bouton, en plaçant sa souris ou son trackpad dessus, sans le sélectionner ni cliquer dessus.

Pour modifier les styles du bouton lors du survol, utilisez le sélecteur de pseudo-classe CSS `:hover`.

Un changement courant à effectuer avec `:hover` est de basculer la couleur d'arrière-plan du bouton.

Pour rendre le changement moins brusque, associez `:hover` à la propriété `transition`.

La propriété `transition` aidera à rendre la _transition_ de l'absence d'état à l'état `:hover` beaucoup plus fluide.

Le changement de couleur d'arrière-plan se produira un peu plus lentement qu'il ne le ferait sans la propriété `transition`. Cela aidera également à rendre le résultat final moins déroutant pour l'utilisateur.

```
.button:hover {
      background-color:#002ead;
      transition: 0.7s;
  }
```

Dans l'exemple ci-dessus, j'ai utilisé une valeur de code couleur Hex pour rendre la couleur d'arrière-plan d'une nuance plus claire lors du survol du bouton.

À l'aide de la propriété `transition`, j'ai également provoqué un délai de `0.7s` lors de la transition de l'absence d'état à l'état `:hover`. Cela a entraîné une transition plus lente de la couleur d'arrière-plan originale `#0a0a23` vers la couleur d'arrière-plan `#002ead`.

![hover](https://www.freecodecamp.org/news/content/images/2022/02/hover-2.gif)

Gardez à l'esprit que la pseudo-classe `:hover` ne fonctionne pas pour les écrans d'appareils mobiles et les applications mobiles. Choisissez d'utiliser des effets de survol uniquement pour les applications web de bureau et non pour les écrans tactiles.

### Comment styliser l'état `:focus`

L'état `:focus` prend effet pour les utilisateurs de clavier - plus précisément, il s'activera lorsque vous mettrez le focus sur un bouton en appuyant sur la touche `Tab` (`⇥`).

Si vous suivez l'exemple, lorsque vous mettrez le focus sur le bouton après avoir appuyé sur la touche `Tab`, vous verrez ce qui suit :

![focus-5](https://www.freecodecamp.org/news/content/images/2022/02/focus-5.gif)

Remarquez le léger contour bleu clair autour du bouton lorsqu'il a obtenu le focus ?

Les navigateurs ont un style par défaut pour la pseudo-classe `:focus`, à des fins d'accessibilité pour la navigation au clavier. Ce n'est pas une bonne idée de supprimer complètement cet `outline`.

Vous pouvez cependant créer des styles personnalisés pour celui-ci et le rendre facilement détectable.

Une façon de le faire est de définir d'abord la couleur du contour sur `transparent`.

Ensuite, vous pouvez maintenir l'`outline-style` sur `solid`. Enfin, en utilisant la propriété `box-shadow`, vous pouvez ajouter une couleur de votre choix pour le moment où l'élément a le focus :

```
 .button:focus {
    outline-color: transparent;
    outline-style:solid;
    box-shadow: 0 0 0 4px #5a01a7;
}
```

![focusend](https://www.freecodecamp.org/news/content/images/2022/02/focusend.gif)

Vous pouvez également à nouveau associer ces styles à la propriété `transition`, selon l'effet que vous souhaitez obtenir :

```
  .button:focus {
    outline-color: transparent;
    outline-style:solid;
    box-shadow: 0 0 0 4px #5a01a7;
    transition: 0.7s;
}
```

![focusend1](https://www.freecodecamp.org/news/content/images/2022/02/focusend1.gif)

### Comment styliser l'état `:active`

L'état `:active` s'active lorsque vous cliquez sur le bouton, soit en cliquant avec la souris de l'ordinateur, soit en appuyant sur le trackpad de l'ordinateur portable.

Ceci étant dit, regardez ce qui se passe lorsque je clique sur le bouton après avoir appliqué et conservé les styles pour les états `:hover` et `:focus` :

![active-1](https://www.freecodecamp.org/news/content/images/2022/02/active-1.gif)

Les styles de l'état `:hover` sont appliqués avant de cliquer lorsque je survole le bouton.

Les styles de l'état `:focus` sont également appliqués, car lorsqu'un bouton est cliqué, il gagne également un état `:focus` en plus d'un état `:active`.

Cependant, gardez à l'esprit qu'ils ne sont _pas_ la même chose.

L'état `:focus` est lorsqu'un élément est ciblé et `:active` est lorsqu'un utilisateur `clique` sur un élément en le maintenant enfoncé.

Pour changer le style lorsqu'un utilisateur clique sur un bouton, appliquez des styles au pseudo-sélecteur CSS `:active`.

Dans ce cas, j'ai changé la couleur d'arrière-plan du bouton lorsqu'un utilisateur clique dessus :

```
.button:active {
    background-color: #ffbf00;
}
```

![activefinal](https://www.freecodecamp.org/news/content/images/2022/02/activefinal.gif)

## Conclusion

Et voilà ! Vous connaissez maintenant les bases de la stylisation d'un bouton avec CSS.

Nous avons vu comment changer la couleur d'arrière-plan et la couleur du texte des boutons, ainsi que comment styliser les boutons pour leurs différents états.

Pour en savoir plus sur le design web, consultez la [Certification Responsive Web Design][12] de freeCodeCamp. Dans les leçons interactives, vous apprendrez le HTML et le CSS en construisant 15 projets pratiques et 5 projets de certification.

Notez que la certification ci-dessus est encore en version bêta - si vous voulez la dernière version stable, [regardez ici][13].

Merci de m'avoir lu et bon codage !

[1]: #heading-comment-creer-un-bouton-en-html
[2]: #heading-comment-modifier-le-style-par-defaut-des-boutons
[3]: #heading-comment-modifier-la-couleur-darriere-plan-des-boutons
[4]: #heading-comment-modifier-la-couleur-du-texte-des-boutons
[5]: #heading-comment-modifier-le-style-de-bordure-des-boutons
[6]: #heading-comment-modifier-la-taille-des-boutons
[7]: #heading-comment-styliser-les-etats-des-boutons
[8]: #heading-comment-styliser-letat-hover
[9]: #heading-comment-styliser-letat-focus
[10]: #heading-comment-styliser-letat-active
[11]: #heading-conclusion
[12]: https://www.freecodecamp.org/learn/2022/responsive-web-design/
[13]: https://www.freecodecamp.org/learn/responsive-web-design