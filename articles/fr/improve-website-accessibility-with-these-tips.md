---
title: Comment améliorer l'accessibilité d'un site web – 7 conseils utiles
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2022-10-26T18:09:18.000Z'
originalURL: https://freecodecamp.org/news/improve-website-accessibility-with-these-tips
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/website_accessibility-1.png
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment améliorer l'accessibilité d'un site web – 7 conseils utiles
seo_desc: "An accessible website is designed in such a way that anyone can use it\
  \ without difficulty. \nDuring the website development process, you want to make\
  \ sure that the end user has the best user experience. And that includes people\
  \ with disabilities or th..."
---

Un site web accessible est conçu de manière à ce que tout le monde puisse l'utiliser sans difficulté.

Lors du processus de développement d'un site web, vous souhaitez vous assurer que l'utilisateur final ait la meilleure expérience possible. Et cela inclut les personnes handicapées ou celles qui rencontrent des difficultés lors de l'utilisation d'un site web.

Malheureusement, il existe encore des sites web qui n'utilisent pas les meilleures pratiques en matière d'accessibilité. Mais vous pouvez vous assurer que le vôtre le fait.

Si vous gardez à l'esprit quelques éléments pendant le processus de développement web, vous pouvez améliorer l'expérience utilisateur pour tous les utilisateurs, y compris les utilisateurs [differently abled](https://dictionary.cambridge.org/dictionary/english/differently-abled).
Voici quelques conseils utiles que vous pouvez utiliser pour améliorer l'accessibilité d'un site web.

## Ajouter un texte alternatif aux images

Vous avez peut-être entendu parler de l'importance d'ajouter un texte alternatif aux balises d'image en HTML5. Alors, comment les utiliser ? Fournissez-vous un texte alternatif pour chaque image sur votre page web ?

Le texte alternatif des images facilite la compréhension du contenu d'une page web pour les personnes ayant des déficiences visuelles. Mais vous devez inclure le texte alternatif uniquement pour les images informatives qui aident à la compréhension du contenu.

Les images décoratives doivent avoir un texte alternatif vide. Cela indique aux lecteurs d'écran que l'information fournie par l'image n'est pas importante et pourrait en fait nuire à l'expérience utilisateur.

Les images **informatives** sont des images qui transmettent des informations importantes liées au contenu. Vous devriez être en mesure de décrire ce qu'elles montrent en quelques mots de texte alternatif.

Supposons que nous tenons un blog sur le fitness et que nous travaillons sur la création d'un article sur la façon de faire une séance d'entraînement à la maison et que nous utilisons l'image suivante dans notre article.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/jonathan-borba-lrQPTQs7nQQ-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/ja/@jonathanborba?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Jonathan Borba</a> sur <a href="https://unsplash.com/s/photos/workout?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Cette image est censée transmettre un message aux lecteurs du blog sur les choses dont vous avez besoin pour un exercice de crunch. Le texte alternatif pour cette image pourrait être quelque chose comme ceci :

```html
<img src="crunch_exercise.png" alt="Vous devez avoir un tapis d'exercice de bonne qualité et des vêtements de sport pour éviter les blessures au dos et les allergies cutanées">

```

Le texte alternatif que nous avons fourni pour notre image indique clairement aux utilisateurs malvoyants le message que notre image transmet.

Les images **décoratives**, en revanche, servent uniquement à décorer la page web – peut-être qu'elles ne font que rompre le contenu ou compléter les descriptions générales dans le texte.

Les images utilisées comme icônes sont un excellent exemple d'images décoratives. La page d'accueil d'Airbnb comporte une barre de navigation avec plusieurs icônes (comme celle dans le cercle rouge) indiquant différents types d'espaces de vie disponibles chez Airbnb. Les icônes utilisées dans la barre de navigation sont à des fins de décoration et nous pouvons laisser leur texte alternatif vide.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/decorative_image.png)
_Page d'accueil d'Airbnb_

```html
<!-- Exemple d'image décorative -->
<img src="decorative_img.png" alt="">
```

## Maintenir la hiérarchie des titres

Si vous n'utilisez pas les titres dans la bonne hiérarchie (de <h1> – le plus grand – à <h6> – le plus petit), les lecteurs d'écran pourraient supposer qu'il manque du contenu.

Pour cette raison, il est préférable d'utiliser <h1> uniquement pour le titre principal, <h2> pour les titres qui suivent le titre, h3 pour les sous-titres, et ainsi de suite.

Considérez l'exemple ci-dessous : nous avons une page web avec quelques titres. <h1> est utilisé pour le titre du document, <h2> pour le titre de deuxième niveau du document, <h3> pour les sous-titres et <h4> pour les mini-titres (titres qui suivent <h3>).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/heading_hierarchy.png)
_Exemple de hiérarchie des titres_

Ci-dessous se trouve le code de cette page web. Remarquez les différentes balises de titre qu'il contient :

```html
<h1>Faits sur les chiens</h1>
<img src="dog.png" alt="un chien mignon se reposant sous le soleil">
<h2>Qu'est-ce qui fait du chien le meilleur animal de compagnie ?</h2>
<p>Les chiens sont les préférés de tout le monde et il y a de nombreuses raisons scientifiques pour cela, mentionnées ci-dessous</p>
<h3>Les chiens peuvent sentir un mensonge</h3>
<p>Oui ! Vous avez bien lu ! Les chiens sont assez intelligents pour dire quand un éloge est sincère. Ils ont un esprit assez vif.</p>
<h3>Les chiens ont un excellent odorat</h3>
<p>Les chiens ont un odorat 40 fois meilleur que le nôtre et cette qualité joue un rôle important dans la création d'un lien plus fort entre un humain et un chien. Les raisons en sont données ci-dessous</p>
<h4>1. Ils peuvent sentir un étranger s'infiltrer dans votre garage</h4>
<p>Les chiens peuvent repérer un étranger grâce à leur odorat puissant et vous sauver du vol.</p>
<h4>2. Ils peuvent vous dire chaque fois que vous oubliez de mettre la viande dans le réfrigérateur après une course</h4>
<p>Les chiens peuvent vous faire donner la moitié de la viande que vous avez achetée au supermarché, mais ils peuvent aussi vous aider à sauver l'autre moitié. Grâce à leur odorat !</p>
```

## Utiliser la propriété Aria ou la balise Label pour les champs de saisie

Les étiquettes Aria ou les balises <label> indiquent aux lecteurs d'écran quel type d'information un champ de saisie attend. Sans elles, les lecteurs d'écran ne connaîtront pas le but d'un champ de saisie, ce qui fournirait une mauvaise expérience utilisateur aux utilisateurs malvoyants.

```html
<!-- Exemple d'étiquette Aria -->
<input type="text" placeholder="Entrez votre nom" aria-label="Entrez votre nom">

<!-- Exemple de balise Label -->
<label>Nom complet : <input type="text" placeholder="Entrez votre nom"></label>

```

Le premier exemple utilise la propriété aria pour que les lecteurs d'écran lisent ce que l'utilisateur est censé entrer dans le champ de saisie du nom.

Le deuxième exemple utilise la balise <label> avec le texte Nom complet qui est lisible par les lecteurs d'écran.

## Fournir une fonctionnalité clavier

Tous les utilisateurs ne peuvent pas utiliser un dispositif de pointage (souris), mais beaucoup de sites web ne fournissent pas de fonctionnalité clavier aux utilisateurs. Cela décourage les utilisateurs qui n'utilisent que le clavier de revenir sur votre site web.

Un exemple simple de cela est l'ajout d'un écouteur d'événement de clic au bouton de soumission d'un formulaire au lieu d'utiliser l'événement onsubmit (qui nécessite qu'un utilisateur clique pour soumettre un formulaire). Jetez un coup d'œil à l'exemple ci-dessous :

```html
<!-- Exemple un -->
<form>
	<label>Nom complet : <input type="text" value=""></label>
    <label>Email : <input type="email" value=""></label>
    <button onclick="handleSubmit">Soumettre</button>
</form>

<!-- Exemple deux -->
<form>
	<label>Nom complet : <input type="text" value=""></label>
    <label>Email : <input type="email" value=""></label>
    <button>Soumettre</button>
</form>
```

Le premier exemple utilise un écouteur d'événement de clic sur le bouton de soumission. Cela signifie que l'appui sur la touche Entrée d'un clavier ne soumettrait pas le formulaire.

Le deuxième exemple utilise l'événement onsubmit et attribue une fonction JavaScript à cet événement. Ainsi, un clic ou un appui sur la touche Entrée exécutent tous deux la fonction handleSubmit.

## Utiliser une palette de couleurs accessible

Les mauvais contrastes de couleurs gâchent l'expérience globale pour les personnes sans handicap ainsi que pour celles avec des handicaps. Il est donc important d'obtenir le contraste et les couleurs complémentaires corrects lors de la conception de votre site.

Il existe des outils comme [contrast checker](https://webaim.org/resources/contrastchecker/) qui vous aident à comprendre si vos couleurs contrastent suffisamment pour être correctement visibles. Le contraste de couleurs accessible aide les personnes handicapées à distinguer les éléments sur une page web. Voir ci-dessous les exemples de bonnes et de mauvaises combinaisons de couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/color_combination.png)
_Exemple de bonne et de mauvaise combinaison de couleurs_

La première boîte a un fond bleu foncé qui rend le blanc plus facile à lire. En revanche, la deuxième boîte a un fond vert avec un texte rose qui n'est pas facile à lire et cause une fatigue oculaire.

## Fournir des alternatives pour le contenu audio et vidéo

Les utilisateurs qui ne peuvent pas bien entendre ou voir peuvent trouver difficile d'accéder au contenu audio et vidéo d'un site web.

Pour leur offrir une meilleure expérience, fournissez des transcriptions pour tout audio que vous utilisez, et ajoutez des sous-titres faciles à lire sur votre contenu vidéo.

## Assurez-vous que le contenu est facile à comprendre

Un contenu facile à comprendre est exempt de jargon inexpliqué et de phrases techniques.

Supposons que vous dirigez une entreprise d'analyse et que vous êtes un expert dans le domaine de la science des données. Mais vos utilisateurs peuvent inclure des clients actuels ou potentiels et des chercheurs d'emploi. Ces personnes peuvent ne pas avoir assez de connaissances techniques pour comprendre un contenu rempli de jargon.

> Nous sommes une équipe d'experts en analyse qui sommes maîtres dans l'agrégation de données de tous les entrepôts disponibles, la détection d'anomalies, l'exécution de traitements par lots sur de grands volumes de données, et l'application d'algorithmes robustes pour résoudre vos besoins commerciaux.

Le texte ci-dessus est rempli de jargon analytique que tout le monde ne peut pas comprendre. Cela vous fait perdre vos visiteurs – car pourquoi investiraient-ils dans vous s'ils ne comprennent pas ce que vous faites ?

Consultez la version simplifiée ci-dessous du même texte qui utilise des termes plus accessibles que tout le monde peut comprendre :

> Nous sommes une équipe d'experts qui nous spécialisons dans la collecte de données de toutes les sources disponibles, l'identification d'erreurs dans ces données, le traitement de grands volumes de données en moins de temps avec une plus grande précision, et la réalisation de prédictions pour résoudre vos besoins commerciaux.

Assurez-vous que votre contenu livre son but dans un langage que tout le monde peut facilement comprendre.

## Conclusion

Les sites web accessibles sont cruciaux pour une bonne expérience utilisateur. Un site web accessible peut non seulement attirer de nouveaux utilisateurs, mais il peut également encourager les anciens utilisateurs à revenir encore et encore.

Il y a beaucoup plus que vous pouvez faire en matière d'accessibilité des sites web. Mais avec ces conseils et astuces, vous pouvez améliorer considérablement l'UX de votre site ou application.

J'espère que ces conseils vous aideront à offrir une meilleure expérience utilisateur dans vos projets à venir.

Développez des sites web accessibles et faites d'Internet un meilleur endroit pour tout le monde !

Intéressé à se connecter sur LinkedIn ? Contactez-moi à [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/)