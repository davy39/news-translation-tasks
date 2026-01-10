---
title: Causes courantes de la syntaxe HTML invalide – et comment les corriger
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-04-18T16:51:50.000Z'
originalURL: https://freecodecamp.org/news/invalid-html-syntax-examples-and-fixes
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Blog-post-cover-for-FCC
seo_title: Causes courantes de la syntaxe HTML invalide – et comment les corriger
---

2-Revised-.png
tags:
- name: coding
  slug: coding
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Vous souvenez-vous de ces cabanes dans les arbres que nous avions enfants et comment le bois s'usait, se déchirait et finissait par s'effondrer parce que nous ne pouvions pas arrêter de sauter à l'intérieur ?  \nEh bien, c'est un peu comme le HTML. Ce langage de balisage est comme le bois de votre projet de codage. S'il est invalide, votre solution s'effondrera. "
---

Vous souvenez-vous de ces cabanes dans les arbres que nous avions enfants et comment le bois s'usait, se déchirait et finissait par s'effondrer parce que nous ne pouvions pas arrêter de sauter à l'intérieur ?  

Eh bien, c'est un peu comme le HTML. Ce langage de balisage est comme le bois de votre projet de codage. S'il est invalide, votre solution s'effondrera. 

Maintenant, ne vous inquiétez pas. Dans cet article, je vais vous donner quelques conseils pour vous aider à vous assurer que votre HTML est sans erreur pendant que vous construisez votre solution de codage.

![Dwight de The Office est prêt à coder ](https://www.freecodecamp.org/news/content/images/2023/04/dwight.gif)
_Vous avez entendu Dwight. Faisons cela ! :)_

## Causes courantes de la syntaxe HTML invalide

Avant de vous lancer dans l'investigation de code non propre comme Sherlock Holmes (la version [Benedict Cumberbatch](https://www.imdb.com/title/tt1475582/) pour être exact 609), rencontrons brièvement quelques exemples de syntaxe qui peuvent ruiner votre fichier HTML :

1. Imbrication incorrecte des éléments HTML

![Capture d'écran d'un extrait de code zoomant sur la ligne <b></b> ](https://www.freecodecamp.org/news/content/images/2023/04/example-of-improper-nesting-tag.jpeg)
_"HEIN ?" en effet_

2. Balises HTML obsolètes 

![Capture d'écran pointant vers la balise <center>, un élément HTML obsolète du code de recherche Google. ](https://www.freecodecamp.org/news/content/images/2023/04/deprecated-HTML.jpg)
_Choix intéressant 60F_

3. Balises manquantes 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/missing-html-tag.png)
_Oh balise de fermeture, où es-tu ?_

Maintenant que vous avez rencontré les coupables, découvrons comment les attraper avant qu'ils ne ruinent votre fichier HTML et ne détruisent votre projet de codage.   


![Jeune Alfred de "Gotham" disant "Faisons cela"](https://www.freecodecamp.org/news/content/images/2023/04/alfred-3.gif)
_Oui monsieur !_

###   
Imbrication incorrecte des éléments HTML 

Pour une brève révision, l'imbrication se produit lorsqu'un élément HTML est à l'intérieur d'un autre élément HTML.

```html
<p>Codé par <a class="profile-link" href="<https://github.com/CBID2>" target="_blank"><em>Christine Belzie</em></a></p>

```

Maintenant, un élément imbriqué devient malveillant – je veux dire incorrectement imbriqué – lorsque vous placez un élément HTML à l'intérieur de la mauvaise zone de l'autre élément, comme ceci :

```html
<a class="profile-link" href="<https://github.com/CBID2>" target="_blank"><em>Christine Belzie<p>Codé par </p></em></a>

```

Le code ci-dessus serait considéré comme invalide car la balise <p> n'est pas liée à la balise <a> et la balise <p> n'est pas liée à la balise <em>. En conséquence, vous obtenez un paragraphe désorganisé.

%[https://codepen.io/CB_ID2/pen/WNawGVw]

Pour remplacer l'élément incorrectement imbriqué, je recommande vivement de faire ce que j'aime appeler le Modèle Sandwich. Il consiste à empiler les balises d'ouverture et de fermeture des éléments HTML de style à l'intérieur des balises principales, un peu comme la façon dont vous empilez toutes vos garnitures et remplissages entre deux tranches de votre pain préféré.

```html
<bread> <topping> </topping> <filling> </filling> </bread>
```

Maintenant, si vous pensez que les balises incorrectement imbriquées étaient malveillantes, attendez de voir le prochain méchant.

![Fille de "Bob's Burgers" rit de manière malveillante tandis que des flammes éclatent en arrière-plan](https://www.freecodecamp.org/news/content/images/2023/04/evil-laugh.gif)
_Muahaha ! 608_

### Balises HTML obsolètes

En termes simples, les balises HTML obsolètes sont essentiellement lorsque vous utilisez des éléments HTML que l'industrie technologique a décidé de ne plus utiliser. Voici un exemple :

```html
<center>
  <figcaption id="img-caption">Rihanna se produit sur scène au stade San Siro pour l'Anti World Tour 2016. </figcaption>
</center>

```

Dans l'extrait de code ci-dessus, j'ai utilisé la balise <center>. Maintenant, l'extrait de code ci-dessus remplira-t-il sa tâche ? Bien sûr. Voir le résultat ci-dessous :

%[https://codepen.io/CB_ID2/pen/LYgZXOE]

Mais il est considéré comme invalide puisqu'il n'est [plus utilisé](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center), ce qui peut empêcher votre projet de fonctionner de la meilleure façon possible. 

C'est comme porter des chaussures à plateforme des années 70 alors que tout le monde porte des Yeezy, des Sketchers ou des Converse.

![Chaussures à plateforme jaunes descendant les escaliers](https://www.freecodecamp.org/news/content/images/2023/04/platform-shoes.gif)
_Pour citer Pauly D de "Jersey Shore", "Qu'est-ce que c'est que ça ?!"_

La meilleure façon de corriger les balises HTML obsolètes est de se référer à des sites web, des blogs et d'autres sources pour rester à jour sur les dernières versions du code. Donnons un coup de jeune à l'extrait que j'ai mentionné :

```html
<figcaption id="img-caption">Rihanna se produit sur scène au stade San Siro pour l'Anti World Tour 2016. </figcaption>

```

```css
figcaption{
	max-width:100%;
	  height: auto;
	display:flex;
	justify-content: center;
	 font-family: 'Montserrat', sans-serif;
	
  }

```

Pour centrer l'élément <figcaption>, j'ai utilisé la méthode CSS Flexbox : "justify-content" et voilà :

%[https://codepen.io/CB_ID2/pen/jOerQzK]

Vous voyez à quel point l'extrait est joli maintenant ? Lorsque votre code est beau, votre projet fonctionne bien aussi. Pour rester à jour sur HTML, [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), à mon avis, est une excellente source car ils informent toujours les lecteurs lorsque certaines balises sont obsolètes.

Maintenant, ne vous réjouissez pas trop vite, nous ne sommes pas encore sortis des bois, il reste encore une syntaxe invalide que nous devons rencontrer.

![Ren de "Ren et Stimpy" transpire de peur](https://www.freecodecamp.org/news/content/images/2023/04/nervous.gif)
_N'ayez pas peur...pas encore ! 608_

### Balises de fermeture manquantes 

Vous savez comment vous aviez l'habitude de ricaner et de lever les yeux au ciel chaque fois que votre instructeur de rédaction vous enlevait des points pour votre essai à cause de quelques mots mal orthographiés ou d'un point manquant ? Eh bien, ils avaient raison – car la même idée s'applique à votre fichier HTML. 

Un problème courant auquel vous pourriez être confronté est celui des balises de fermeture manquantes. Voyons à quoi cela ressemble.

```html
<div class="user-info">
<h3 id="user-name">Victor Crest<span class="age">26</span></h3>


```

Si l'une de vos lignes de code ressemble à l'extrait de code ci-dessus, votre fichier HTML se cassera, ce qui fera que votre projet ne sera pas aussi beau que dans le résultat ci-dessous :

%[https://codepen.io/CB_ID2/pen/qBJNQQO]

Imaginez cela comme un pneu manquant dans votre voiture (ou tout autre véhicule que vous utilisez pour vous transporter). Sans lui, vous conduiriez comme ceci :

![Kramer de "Seinfeld" conduit un camion incontrôlable.](https://www.freecodecamp.org/news/content/images/2023/04/crazy-driving.gif)
_Tiens bon, mon ami !_

Pour corriger cette erreur, je recommande vivement d'utiliser la méthode du sandwich que j'ai mentionnée précédemment. 

```html
<div class="user-info">
<h3 id="user-name">Victor Crest<span class="age">26</span></h3>
</div>

```

Comme vous pouvez le voir dans le code ci-dessus, nous avons ajouté notre balise de fermeture `</div>`, ce qui fait que l'extrait ressemble maintenant à ceci :

%[https://codepen.io/CB_ID2/pen/jOerQXv]

Vous voyez à quel point le code est amélioré maintenant ? Souvenez-vous, pensez à une ligne de code comme à un sandwich. Lorsque une tranche de pain (ou dans ce cas, une balise de fermeture) est manquante, votre chef-d'œuvre s'effondre, vous laissant en colère, triste et parfois affamé. 

![Un manchot se frotte le ventre avec tristesse en disant "J'AI TELLEMENT FAIM"](https://www.freecodecamp.org/news/content/images/2023/04/penguin.gif)
_Désolé pour toi, manchot !_

## Conclusion

Vous l'avez ! Trois types courants de syntaxe invalide à surveiller dans votre fichier HTML. 

Souvenez-vous, ce fichier est la fondation de vos projets de codage, donc un fichier HTML heureux = un projet heureux ! 60A

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-131.png)
_Heureux de savoir que nous sommes d'accord l'un avec l'autre._

### Crédits

* Ben Mckenzie Fox GIF par [Gotham](https://giphy.com/gifs/gotham-fox-3o7abuqxszgO6pFb3i)
* Can't Touch This High Heels GIF par [BrownSugarApp](https://giphy.com/gifs/brownsugarapp-fashion-get-l3vR1JnogyxKm0SGs)
* Image de la balise de fermeture de l'article "How to Easily Find Missing Closing Tags in HTML (with Coda 2)" sur [Clicks Nathan](https://clicknathan.com/web-design/easily-find-missing-closing-html-tag/)
* Dwight Office Tv GIF par [The Office](https://giphy.com/gifs/BpGWitbFZflfSUYuZ9)
* Driving Michael Richards GIF par [Seinfield GIFs](https://giphy.com/gifs/crazy-seinfeld-9NTfxeLPpgRUI)
* Fox Tv Fire GIF par [Bob's Burgers](https://giphy.com/gifs/bobs-burgers-fox-bobs-burgers-tv-3o72FfM5HJydzafgUE)
* Oh Yeah Yes GIF par [Mauro Gatti](https://giphy.com/gifs/cool-ok-sure-l41lUjUgLLwWrz20w)
* Ren And Stimpy Reaction GIF par [Giphy](https://giphy.com/gifs/scared-nervous-ren-and-stimpy-y9X0F8VgTkmU8)
* Sad Nft GIF par [Pudgy Penguins](https://media.giphy.com/media/MSqUXNDStq8V3Qc9OM/giphy.gif)
* Capture d'écran de Google du forum de discussion "Why does Google use the deprecated HTML tag still?" sur [Reddit](https://twitter.com/davedbase/status/1647012417841365001?s=46)
* Capture d'écran de la balise imbriquée incorrecte de l'article "How is the DOM Affected by Improperly Nested HTML Elements?" par Louis Lazrus sur [Impressive Webs](https://www.impressivewebs.com/dom-improperly-nested/)