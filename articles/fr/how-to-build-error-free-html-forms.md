---
title: Comment créer des formulaires HTML sans erreur
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-07-17T18:47:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-error-free-html-forms
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/FCC-Blog-Cover-4.png
tags:
- name: error
  slug: error
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: Comment créer des formulaires HTML sans erreur
seo_desc: "After taking some coding courses, I decided that it was time to put my\
  \ knowledge to good use and do a coding project. \nLike most newbies, I went to\
  \ Google to find some inspiration. As I scrolled through the internet, I stumbled\
  \ upon Skillcrush’s list..."
---

Après avoir suivi quelques cours de codage, j'ai décidé qu'il était temps de mettre mes connaissances à profit et de réaliser un projet de codage. 

Comme la plupart des débutants, je suis allé sur Google pour trouver de l'inspiration. En parcourant Internet, je suis tombé sur [la liste de projets HTML et CSS pour débutants de Skillcrush](https://skillcrush.com/blog/html-css-projects/). 

Le numéro 5 a piqué ma curiosité, alors j'ai cherché des images sur l'apparence des formulaires HTML. Je me suis dit : « Oh, je peux faire ça. Cela semble facile ! » Mais ce projet s'est avéré un peu plus difficile que je ne le pensais. 

Dans cet article, je vais vous montrer trois choses que j'ai apprises pour survivre, je veux dire pour créer des formulaires HTML sans erreur. Commençons ! 600

## Astuce n°1 : Assurez-vous que les étiquettes et les champs correspondent.

Lorsque j'ai commencé à créer des formulaires HTML, j'utilisais souvent les méthodes suivantes pour créer des champs de saisie d'email :

```html
<label id="text"> Votre Email</label>
<input type="text" id="text" name="text"> 
```

J'utilisais souvent `text` comme étiquette et attribut d'id car je pensais que c'était la méthode correcte. 

Tout a changé lorsque j'ai commencé à utiliser [le vérificateur d'accessibilité WAVE](https://wave.webaim.org/extension/) pour apprendre à rendre mon code plus accessible. Lorsque j'ai passé mon formulaire dans le vérificateur, il a souligné que le champ de saisie d'email n'avait pas d'étiquette correctement associée, ce qui peut causer des difficultés aux lecteurs d'écran pour le présenter aux utilisateurs handicapés.

Alors, j'ai cherché quelques sources et trouvé [« HTML Inputs and Labels: A Love Story » par Amber Wilson](https://css-tricks.com/html-inputs-and-labels-a-love-story/). En lisant cet article, j'ai appris qu'il est préférable d'utiliser des noms spécifiques dans l'attribut `id`. 

Avec un nouveau sentiment de confiance, j'ai commencé à utiliser cette approche. Voici un exemple :

%[https://codepen.io/CB_ID2/pen/MWPPmBG]

Dans l'extrait de code ci-dessus, j'ai utilisé `email` comme étiquette et attribut `id` du champ de saisie. Lorsque je l'ai passé dans le vérificateur d'accessibilité, il n'y avait pas de X rouges. 

Bien que cette victoire ait été douce, je voulais apprendre d'autres façons de m'assurer que les étiquettes et les champs étaient accessibles. Alors je suis allé sur Google et j'ai trouvé cet [article sur les attributs des formulaires HTML](https://www.w3schools.com/html/html_forms_attributes.asp). En le lisant, j'ai appris que vous pouvez ajouter d'autres attributs comme `placeholder`, qui montre comment l'utilisateur doit présenter ses informations de contact. 

À travers ces expériences, j'ai réalisé que créer des étiquettes et des champs harmonieux pour un formulaire est comme construire un sandwich. Vous voulez vous assurer que vos saveurs fonctionnent bien ensemble et utiliser les meilleures fonctionnalités de votre four (ou de l'appareil que vous utilisez) pour rendre votre sandwich bien grillé. 

Maintenant, avant de commencer à avoir faim, passons à mon prochain conseil. :)

## **Astuce n°2 : Soyez plus sémantique lors de la création d'un bouton**

Formater les boutons de votre formulaire est crucial pour l'efficacité de votre formulaire HTML. Les boutons sont le principal moyen par lequel les informations de l'utilisateur sont envoyées à la destination souhaitée. 

Lorsque j'ai commencé à créer des formulaires HTML, je créais des boutons comme ceci :

```html
<input type="submit">
```

Comme pour les étiquettes et les champs, j'obtenais un X rouge sur le vérificateur d'accessibilité WAVE. Dans les résultats, il était mentionné qu'un attribut `value` était manquant, ce qui rend difficile pour le lecteur d'écran de détecter le bouton. 

Avec cela en tête, j'ai décidé de faire ce que la plupart des débutants font lors de la création de cette fonctionnalité :

```html
<button> Soumettre</button>
```

Lorsque j'ai exécuté le code dans le vérificateur d'accessibilité WAVE à nouveau, il a passé quelques tests. Mais quelque chose en moi me disait que ma solution précédente était également correcte et que je devais simplement trouver un moyen d'ajouter un attribut `value`. 

Avec une nouvelle soif de connaissances, je suis allé sur Google et j'ai trouvé cet [article sur la création de composants de formulaire accessibles](https://www.w3.org/WAI/tutorials/forms/labels/#labeling-buttons). Dans la section sur les boutons, ils recommandent d'utiliser les méthodes suivantes pour rendre cet élément sémantique :

```html
<input type="Submit" value="Submit">
<button type="Submit">Submit</button>
```

Lorsque j'ai exécuté le premier extrait dans le vérificateur d'accessibilité, je n'ai reçu aucun X rouge. Le même résultat s'est produit lorsque j'ai exécuté le deuxième extrait de code dans le vérificateur d'accessibilité. 

Au début, je ne savais pas lequel choisir car les deux approches rendaient le formulaire accessible. Mais quelque chose en moi m'a dit de choisir ce que je voulais vraiment. Alors, j'ai pris une profonde inspiration et choisi la ligne de code suivante :

%[https://codepen.io/CB_ID2/pen/Rwedeme]

J'ai décidé d'opter pour le deuxième extrait de code car il est plus explicitement étiqueté, ce qui facilite la lecture par les lecteurs d'écran. C'est aussi plus facile à retenir, et c'est la méthode que j'utilise souvent pour créer des boutons. 

Pensez-y comme si vous décidiez d'utiliser la marque de pain que vous avez toujours utilisée pour vos sandwichs au lieu d'en choisir une différente. Aussi cliché que cela puisse paraître, parfois la simplicité est la meilleure. 

Avant de commencer à avoir faim à nouveau, il ne reste qu'une dernière suggestion pour rendre vos formulaires HTML sans erreur.

## **Astuce n°3 : Choisissez le meilleur Framework CSS en fonction de vos besoins**

Lorsque j'ai commencé à créer le style de mes formulaires, je me forçais à utiliser des frameworks CSS comme Flexbox. À l'époque, mes sentiments de syndrome de l'imposteur étaient à leur comble en voyant d'autres personnes créer de superbes formulaires avec ces frameworks. Je pensais que si je commençais à les utiliser aussi, j'obtiendrais les mêmes designs. 

Au début, j'étais heureux d'utiliser Flexbox car cela rendait des choses comme le centrage du contenu plus facile, comme le montre l'extrait ci-dessous :

%[https://codepen.io/CB_ID2/pen/mdzoQrg]

Malheureusement, je n'étais toujours pas satisfait à la fin. J'ai trouvé que le design ne correspondait pas à ce que j'avais imaginé. 

Pour combattre ce sentiment, je suis allé sur Google pour trouver quelque chose pour m'aider à résoudre mon dilemme. Lorsque j'étais sur le point d'abandonner, je suis tombé sur l'article, [« How to style forms with CSS: A beginner’s guide » par Supun Kavinda](https://blog.logrocket.com/how-to-style-forms-with-css-a-beginners-guide/).

Mon cœur a bondi de joie lorsqu'il a été souligné que vous pouvez utiliser du CSS vanilla pour créer de beaux designs. Par exemple, pour rendre les champs de saisie de texte plus présentables, je pourrais faire ceci :

```css
input[type=text]{
padding: 10px;
} 
```

Avec une confiance nouvelle, j'ai donné une autre chance au CSS vanilla, et je peux honnêtement dire que j'étais si heureux de cette décision. Voici le résultat final :

%[https://codepen.io/CB_ID2/pen/NWOOQXQ]

Je voulais garder mon design simple, alors j'ai utilisé des éléments de base comme la propriété `text-align` pour centrer le contenu de mon formulaire. 

Si je devais choisir quelque chose qui exemplifie cette expérience, ce serait comme un sandwich coupé en deux parts triangulaires. Simple mais efficace. 

Dans l'ensemble, parfois, il est préférable de revenir aux bases avant de passer à quelque chose de plus difficile. 

## **Conclusion**

Voilà, mes trois conseils pour rendre vos formulaires HTML sans erreur. 

Je sais que créer des formulaires HTML peut être effrayant au début. Mais avec ces conseils, de la confiance et un peu d'imagination, vous pouvez créer des formulaires HTML qui impressionnent vos spectateurs. Maintenant, allez de l'avant et soyez génial ! :)