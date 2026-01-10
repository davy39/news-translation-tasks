---
title: Guide RGB - HTML et CSS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-19T19:00:35.000Z'
originalURL: https://freecodecamp.org/news/rgb-color-html-and-css-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/alice-dietrich-FwF_fKj5tBo-unsplash.jpg
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Guide RGB - HTML et CSS
seo_desc: 'Choosing the right color for your web design project is a serious endeavour.
  A color scheme can often make or break a site''s overall appearance.

  Different colors create a different feel for your designs. The right choice of colors
  can make your desig...'
---

Choisir la bonne couleur pour votre projet de design web est une tâche sérieuse. Une palette de couleurs peut souvent faire ou défaire l'apparence générale d'un site.

Différentes couleurs créent une ambiance différente pour vos designs. Le bon choix de couleurs peut rendre vos designs et créations propres, esthétiquement plaisants et modernes. Mais les mauvaises couleurs peuvent rendre un projet criard, difficile pour les yeux et compliquer l'interaction des utilisateurs.

La couleur de la bordure (`border`), de l'arrière-plan (`background-color`), ou du premier plan (`color`) – le texte et les décorations de texte sur la page – ont un énorme impact, vous devriez donc faire un effort pour les choisir correctement.


![Image](https://www.freecodecamp.org/news/content/images/2021/07/rhondak-native-florida-folk-artist-_Yc7OtfFn-0-unsplash.jpg)
_Image de [Unsplash](https://unsplash.com/)_

CSS vous permet d'utiliser une grande variété de couleurs et de systèmes de couleurs. Ils vont des couleurs nommées, aux couleurs hexadécimales, aux couleurs rgb(), aux couleurs hsl et plus encore.

## Comment utiliser les couleurs en HTML

La manière la plus simple d'appliquer des couleurs à vos éléments HTML est d'écrire votre HTML dans un fichier `.html`. Ensuite, dans ce fichier, vous liez simplement votre feuille de style `.css` avec toutes les couleurs et styles que vous spécifiez.

Cela rend votre code plus facile à lire et *sépare les préoccupations*, ce qui est considéré comme une meilleure pratique.

Nous pouvons avoir un fichier, `about.html`, avec un peu de code HTML comme ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- lien vers nos styles css -->
    <link rel="stylesheet" href="style.css">
    <title>À propos de moi</title>
</head>
<body>
     <section class="intro">
     <h2>À propos de moi</h2>
     </section>
</body>
</html>
```

Ensuite, dans notre `style.css`, nous pouvons ajouter ce qui suit :

```css

.intro {
 /* change la couleur de l'arrière-plan */
  background-color: rgb(232, 206, 191);
  max-width: 620px;
  height: 100px;
  padding: 5px;
  margin: 70px auto;
}

h2 {
/* change la couleur du texte   */
  color: rgb(79, 72, 70);
  text-align:center;
}
```

Ces styles ressemblent à ceci lorsque nous les chargeons dans le navigateur :

![Screenshot-2021-07-19-at-3.36.33-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-3.36.33-PM.png)

Dans cet exemple, nous avons utilisé des valeurs de couleur `rgb` pour changer les couleurs de la page.

Cet article couvre principalement le modèle de couleur `rgb()`. Il fait quelques comparaisons avec les `couleurs nommées` et les `couleurs hexadécimales`, pesant les avantages et les inconvénients de chacun, et discute de certaines différences et similitudes entre ces différents systèmes de couleurs.

## Quelles sont les couleurs nommées en CSS ?

Les couleurs nommées sont des mots anglais, connus sous le nom de *couleurs par mot-clé*. Et elles sont assez simples à utiliser.

Dans votre fichier CSS, vous déclarez la propriété que vous souhaitez cibler et modifier. Vous utilisez ensuite l'un des noms de couleurs définis et spécifiés.

```css

h2 {
    color: cyan;
    }
```

Le code ci-dessus donnera à chaque élément `h2` dans votre HTML une couleur de texte `cyan`.

Il y a environ 140 couleurs nommées que les navigateurs modernes supportent. Vos choix sont donc relativement limités et il n'y a pas beaucoup de variété disponible.

Avec les couleurs nommées, nous ne pouvons pas exploiter tout le pouvoir de CSS. Alors, examinons d'autres options.

## Systèmes de couleurs numériquement nommés

Dans ce cas, les couleurs sont décrites avec un système numérique. Cela vous permet de tirer le meilleur parti de tout le spectre des couleurs disponibles.

La plupart des écrans d'ordinateur utilisent un mélange de couleurs rouge, verte et bleue combinées ensemble.

Les `couleurs hexadécimales` et les `couleurs rgb()` utilisent une combinaison de rouge, vert et bleu pour créer différentes teintes. Elles fonctionnent de la même manière – les seules différences sont les systèmes numériques qu'elles utilisent et leur syntaxe.

Alors, examinons chaque système un peu plus en profondeur.

## Quelles sont les couleurs hexadécimales en CSS ?

Les ordinateurs comptent dans le système de comptage hexadécimal, contrairement à nous, les humains, qui utilisons le système de comptage décimal.

Ce système est composé de valeurs alphanumériques qui incluent ces caractères : `0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f`.

Une couleur hexadécimale commence par un `#` pour indiquer qu'il s'agit bien d'une couleur hexadécimale, puis est suivie par `6` des caractères mentionnés ci-dessus.

Ces chiffres et lettres représentent la quantité de `rouge, vert et bleu` dans la couleur.

Convertir la couleur par mot-clé, `cyan`, de l'exemple précédent en sa valeur de couleur hexadécimale équivalente serait :

```css

h2 {
    #00ffff;
    }
```

La première paire (`00`) représente la quantité de rouge. La paire suivante (`ff`) représente la quantité de vert. Et la dernière (`ff`) représente la quantité de bleu.

La valeur minimale que les couleurs hexadécimales peuvent utiliser est `00`, qui est complètement éteinte, et la valeur maximale est `ff`, qui est complètement allumée.

La couleur blanche en hexadécimal est `#FFFFFF` ou `FFF` pour sa notation abrégée, et la couleur noire est `#000000` ou `#000`.

## Qu'est-ce que le modèle de couleur RGB ?

Généralement, les couleurs `hexadécimales` et les couleurs `rgb` sont identiques – elles utilisent simplement un système numérique et une syntaxe différents (mais les couleurs sont exactement les mêmes).

Cela revient vraiment à une préférence personnelle quant à celle que vous choisissez d'utiliser.

`RGB` est un acronyme qui signifie `Rouge Vert Bleu`.

Au lieu d'utiliser six caractères hexadécimaux comme nous l'avons fait pour les valeurs de couleur hexadécimales, avec le RGB, chaque paire de paramètres définit l'intensité et la luminosité de chaque couleur (rouge, vert et bleu), avec un nombre entier allant de `0-255` ou un pourcentage allant de (0% - 100%).

Il exprime les couleurs en termes de quantité de rouge, vert et bleu dont elles sont composées et utilise un système de comptage humain par comparaison aux couleurs hexadécimales qui parlent le langage informatique.

Le nombre est un code pour représenter à quel point la couleur est sombre ou lumineuse.

La valeur minimale de `0` représente qu'aucune de la couleur n'est affichée, elle est donc à son plus sombre. D'un autre côté, la valeur maximale de `255` représente que la quantité totale de couleur et l'intensité totale sont affichées.


### Syntaxe des couleurs RGB

L'apparence générale d'une déclaration `rgb` est `rgb(rouge,vert,bleu);`

RGB a la syntaxe suivante :

* le mot-clé `rgb` suivi d'une paire de parenthèses `()`
* trois valeurs décimales numériques séparées par des virgules à l'intérieur des parenthèses (qui représentent les trois couleurs),
* et enfin, elle se termine par un point-virgule.

Assurez-vous de ne laisser aucun espace entre quoi que ce soit.

Prenons à nouveau l'exemple `cyan`, le code `rgb` équivalent est :

```css

h2 {
    color:  rgb(0,255,255);
    }
```
 
La couleur rouge n'est pas affichée tandis que le vert et le bleu sont à leur plus lumineux et à leur maximum.

- Le blanc est `rgb(255,255,255)`
- Le noir est `rgb(0,0,0)`
- Le rouge est `rgb(255,0,0)`
- Le vert est `rgb(0,255,0)`
- Le bleu est `rgb(0,0,255)`

### Beaucoup d'options avec le RGB

Avec le RGB, chaque valeur est mélangée avec le reste et ensemble elles créent une large gamme de teintes. Vous pouvez même créer de nouvelles combinaisons de couleurs, ce qui en fait le rêve du designer.

Dans le système de couleur `rgb`, il y a trois valeurs que vous pouvez utiliser, et chaque valeur peut être l'une des 256 valeurs possibles.

Cela fait 256 * 256 * 256 = 16 777 216 options de couleurs au total à choisir !

### Opacité RGB

Par défaut, toutes les couleurs `rgb` sont complètement opaques.

Nous avons la possibilité de rendre les couleurs plus transparentes en changeant l'opacité avec le sélecteur `rgba()`.

La partie `rgb` reste la même, mais la quatrième valeur, `a`, signifie `alpha`.

Nous pouvons donner à `a` un nombre qui est soit `0` soit `1` pour décrire à quel point nous voulons que notre couleur soit opaque. `0` est totalement transparent et `1` est totalement opaque.

Nous utiliserons à nouveau l'exemple `cyan`, mais cette fois nous lui donnerons une opacité de moitié.

```css

h2 {
    color:  rgba(0,255,255,0.5);
    }
```


En CSS, il y a aussi le sélecteur `opacity`.

Nous utiliserons le HTML précédent et ajouterons le sélecteur `opacity` à notre élément `section` avec une classe `.intro` dans notre CSS :

```css
.intro {
    background-color: rgb(232, 206, 191);
    max-width: 620px;
    height: 100px;
    padding: 5px;
    margin: 70px auto;
    opacity: 0.3;
    }
```

Remarquez que cela rend toute la balise transparente, y compris l'arrière-plan, le titre, l'arrière-plan du titre – tout.

![Screenshot-2021-07-19-at-4.21.54-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-4.21.54-PM.png)

La puissance de `rgba()` est qu'il nous permet de rendre uniquement l'arrière-plan transparent, par exemple, ou nous pouvons rendre uniquement le titre transparent. Cela n'affectera pas toute la balise et tout le contenu à l'intérieur.

Maintenant, si nous supprimons la ligne ci-dessus et mettons à jour le sélecteur `background-color` en `background-color: rgb(232, 206, 191,0.3);`, nous voyons que cela n'affecte pas le titre :

![Screenshot-2021-07-19-at-4.25.18-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-4.25.18-PM.png)

## Conclusion

J'espère que cela vous a donné un bon aperçu du modèle de couleur RGB, de sa syntaxe et de son fonctionnement. Nous l'avons également brièvement comparé à d'autres modèles de couleurs en CSS.

J'espère que vous avez trouvé cela utile et je vous remercie de votre lecture.

Bon codage !