---
title: Image de fond CSS – Avec exemple de code HTML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-21T15:20:18.000Z'
originalURL: https://freecodecamp.org/news/css-background-image-with-html-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/kobu-agency-ipARHaxETRk-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Image de fond CSS – Avec exemple de code HTML
seo_desc: "What a user sees on a website will impact how good their user experience\
  \ is. It will also affect how easily they can use the whole site in general. \n\
  Adding images to the background of certain parts of a website is often more visually\
  \ appealing and in..."
---

Ce que voit un utilisateur sur un site web impacte la qualité de son expérience utilisateur. Cela affecte également la facilité avec laquelle il peut utiliser l'ensemble du site en général.

Ajouter des images en arrière-plan de certaines parties d'un site web est souvent plus attrayant et intéressant que de simplement changer la couleur de fond.

Les navigateurs modernes supportent divers types de fichiers image comme `.jpg`, `.png`, `.gif`, et `.svg`.

Cet article explique comment ajouter des images à votre code HTML et comment les ajuster pour qu'elles aient meilleure apparence.

## Syntaxe de l'image de fond

La première étape consiste à créer un répertoire (dossier) d'assets pour stocker les images que vous souhaitez utiliser dans votre projet.

Par exemple, nous pouvons créer un dossier `images` dans le projet sur lequel nous travaillons et ajouter une image appelée `sunset.png` que nous voulons utiliser.

La propriété CSS `background-image` vous permet ensuite de placer l'image derrière n'importe quel élément HTML que vous souhaitez.

Cela peut être soit toute la page (en utilisant le sélecteur `body` en CSS qui cible l'élément `<body>` dans notre HTML), soit juste une partie spécifique de la page comme un élément `section` comme dans l'exemple ci-dessous.

Pour ajouter une `background-image` à une balise section dans votre fichier `.css`, écrivez le code suivant :

```css
section {
     background-image: url("images/sunset.png");
        }
```

Analysons en détail ce qui se passe ici :

- `section` spécifie la balise à laquelle vous souhaitez ajouter l'image.
- `url()` est utilisé pour indiquer à CSS où se trouve notre image.
- À l'intérieur des parenthèses, `"images/sunset.png"` est le chemin vers l'image. Cela permet au navigateur de savoir quelle URL récupérer.
- Le chemin dans cet exemple est appelé un chemin `relatif`, ce qui signifie qu'il s'agit d'un fichier local, relatif à notre projet et à notre répertoire de travail actuel, et non d'une adresse web. Pour ajouter des images, nous pouvons également utiliser un chemin `absolu`, qui est une adresse web complète et commence par une URL de domaine (`http://www.`).
- L'utilisation de guillemets est une bonne habitude, mais nous pouvons les omettre, donc `background-image: url(images/sunset.png)` fonctionne de la même manière.
- N'oubliez pas le point-virgule !





## Comment empêcher la répétition de l'arrière-plan

Lorsque vous appliquez une image de fond à un élément, par défaut, elle se répétera.

Si l'image est plus petite que la balise dont elle est l'arrière-plan, elle se répétera afin de remplir la balise.

Comment empêcher cela ?

La propriété `background-repeat` prend 4 valeurs et nous pouvons changer la direction dans laquelle l'image se répète, ou empêcher l'image de se répéter.

```css
section {
    background-repeat: repeat;
        }
```

C'est la valeur par défaut si nous ne donnons pas de valeur à la propriété `background-repeat`. Dans ce cas, l'image est répétée **à la fois horizontalement et verticalement**, donc dans **les deux directions x et y** respectivement jusqu'à ce qu'elle remplisse l'espace.

![Screenshot-2021-07-20-at-9.10.06-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-20-at-9.10.06-PM.png)



```css
section {
    background-repeat: no-repeat;
        }
```

![Screenshot-2021-07-20-at-9.11.39-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-20-at-9.11.39-PM.png)



La valeur `no-repeat` empêche l'image de se répéter dans toutes les directions. L'image n'est affichée qu'une seule fois.

```css
section {
    background-repeat: repeat-y;
        }
```

Cette valeur répète l'image *uniquement* horizontalement sur la page. L'image est répétée sur la page, dans la `direction x`. La `direction x` en mathématiques va de gauche à droite.

```css
section {
    background-repeat: repeat-y;
        }
```

Cette valeur répète l'image *uniquement* verticalement sur la page. L'image est répétée vers le bas de la page, dans la `direction y`. La `direction y` en mathématiques va de haut en bas.

## Comment définir la position de l'arrière-plan

Après avoir ajouté une image de fond et l'avoir empêchée de se répéter, nous pouvons contrôler davantage son apparence dans l'arrière-plan de la balise en améliorant sa position.

Nous utiliserons la propriété `background-position` pour cela.

Le sélecteur prend deux valeurs. La première est pour la position horizontale, ou direction x (distance par rapport à la balise). La seconde est pour la position verticale, ou direction y (distance vers le bas de la balise).

Les valeurs peuvent être des unités, comme une **paire de pixels** :

```css
section {
    background-position: 20px 30px;
        }
```

Cela déplacera l'image de 20px à droite et de 30px vers le bas de la balise conteneur.


Au lieu de pixels, nous pouvons utiliser un ensemble de mots-clés comme **right, left, top, down, ou center** pour placer l'image à droite, à gauche, en haut, en bas, ou au centre de la balise.

```css
section {
    background-position: right center;
        }
```

Cela place l'image à droite du centre de la balise.

![Screenshot-2021-07-21-at-9.02.55-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-21-at-9.02.55-AM.png)


Si nous voulions la centrer à la fois horizontalement et verticalement, nous ferions ce qui suit :

```css
section {
    background-position: center center;
        }
```

![Screenshot-2021-07-21-at-9.07.41-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-21-at-9.07.41-AM.png)

Pour positionner une image avec plus de précision, il est utile de mentionner que nous pouvons utiliser des pourcentages.

```css
section {
    background-position: 20% 40%;
        }
```

Cela positionne l'image à 20% de la largeur de la balise et à 40% de la hauteur de la balise.

Jusqu'à présent, nous avons vu des valeurs utilisées en combinaison, mais nous pouvons également spécifier une seule valeur comme `background-position: 20px;` ou `background-position: center;` ou `background-position: 20%;`, qui s'applique aux deux directions.


## Comment redimensionner une image de fond

Pour contrôler la taille de l'image de fond, nous pouvons utiliser la propriété background-size.

Encore une fois, comme les propriétés précédentes mentionnées, elle prend deux valeurs. Une pour la taille horizontale (x) et une pour la taille verticale (y).

Nous pouvons utiliser des pixels, comme ceci :

```css
section {
    background-size: 20px 40px;
    /* redimensionne l'image à 20px de large et 40px de haut sur la page */
        }
```

Si nous ne connaissons pas la largeur exacte du conteneur dans lequel nous stockons l'image, il existe un ensemble de valeurs spécifiques que nous pouvons donner à la propriété.

- `background-size: cover;` redimensionne l'image de fond de sorte qu'elle couvre tout l'espace de fond de la balise, quelle que soit la largeur de la balise. Si l'image est trop grande et a un rapport plus grand que la balise dans laquelle elle se trouve, cela signifie que l'image sera étirée et donc rognée à ses bords.
- `background-size: contain;` *contient* l'image, comme le suggère le nom. Il s'assurera que toute l'image est affichée en arrière-plan sans en rogner aucune partie. Si l'image est beaucoup plus petite que la balise, il y aura de l'espace laissé vide, ce qui la fera se répéter pour le remplir, nous pouvons donc utiliser la règle `background-repeat: no-repeat;` que nous avons mentionnée précédemment.


La règle `background-size:cover;` dans ce cas rognera des parties de l'image
![Screenshot-2021-07-21-at-9.18.15-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-21-at-9.18.15-AM.png)

Lorsque nous la changeons en `background-size:contain;` nous voyons que l'image se rétrécit pour s'adapter à la balise section.

![Screenshot-2021-07-21-at-9.18.49-AM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-21-at-9.18.49-AM.png)

## Comment utiliser la propriété Background Attachment

Avec la propriété `background-attachment`, nous pouvons contrôler où l'image de fond est attachée, ce qui signifie si l'image est fixe ou non par rapport au navigateur.

La valeur par défaut est `background-attachment: scroll;`, où l'image de fond reste avec sa balise et suit le flux naturel de la page en faisant défiler vers le haut et vers le bas lorsque nous faisons défiler la page.

La deuxième valeur que la propriété peut avoir est `background-attachement: fixed;`.
Cela fait en sorte que l'image de fond reste dans la même position, fixe sur la page et fixe sur le viewport du navigateur. Cela crée un effet de parallaxe que vous pouvez voir un exemple ici :


<p class="codepen" data-height="300" data-default-tab="result" data-slug-hash="ZEKyRpp" data-user="deniselemonaki" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/deniselemonaki/pen/ZEKyRpp">
  </a> by Dionysia Lemonaki (<a href="https://codepen.io/deniselemonaki">@deniselemonaki</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

## Dégradés de fond

Un cas d'utilisation différent pour la propriété `background-image` est d'indiquer au navigateur de créer un dégradé.

Dans ce cas, `background-image` n'a pas d'URL, mais un dégradé linéaire à la place.

La manière la plus simple de faire cela est de spécifier l'angle. Cela contrôle la direction du dégradé et la manière dont les couleurs se mélangeront. Enfin, ajoutez deux couleurs que vous souhaitez mélanger ensemble dans un dégradé pour l'arrière-plan de la balise.

Un dégradé qui va du haut vers le bas et du noir au blanc est :
 
 ```css
 section {
     background-image: linear-gradient(black,white);
         }
 ```
 
Les degrés les plus couramment utilisés pour les dégradés sont :
 
 - `0deg` de haut en bas
 - `90deg` de gauche à droite
 - `180deg` de bas en haut
 - `270deg` de droite à gauche
 
 
Les degrés ci-dessus correspondent respectivement à `to top`, `to right`, `to bottom` et `to left`.

```css
section{
  background-image: linear-gradient(to left,pink,orange);
        }
```

<p class="codepen" data-height="300" data-default-tab="result" data-slug-hash="poPrPjo" data-user="deniselemonaki" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/deniselemonaki/pen/poPrPjo">
  </a> by Dionysia Lemonaki (<a href="https://codepen.io/deniselemonaki">@deniselemonaki</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

Au lieu de couleurs en mots-clés, nous pouvons utiliser des couleurs hexadécimales pour être plus précis et avoir une plus grande gamme d'options :

```css
section{
  background-image: linear-gradient(to left,#42275a, #734b6d)
      }
```



<p class="codepen" data-height="300" data-default-tab="result" data-slug-hash="LYyjWwL" data-user="deniselemonaki" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/deniselemonaki/pen/LYyjWwL">
  </a> by Dionysia Lemonaki (<a href="https://codepen.io/deniselemonaki">@deniselemonaki</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>

Nous pouvons également inclure plus de deux couleurs dans un dégradé, créant ainsi différents effets et schémas de couleurs.

## Conclusion

Cela marque la fin de notre introduction à la syntaxe de base de la propriété `background-image`.

À partir de là, les possibilités sont infinies et laissent place à beaucoup d'expression créative. Ces effets aident l'utilisateur à avoir une expérience agréable lors de la visite de votre site web.

J'espère que cela a été utile, et merci d'avoir lu.

Amusez-vous avec vos designs et bon codage !