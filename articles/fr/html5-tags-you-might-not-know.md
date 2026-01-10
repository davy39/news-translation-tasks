---
title: Balises HTML5 utiles que vous ne connaissez peut-être pas
subtitle: ''
author: Bhavesh Rawat
co_authors: []
series: null
date: '2022-08-31T21:47:30.000Z'
originalURL: https://freecodecamp.org/news/html5-tags-you-might-not-know
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/five-html-tags-1.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Web Development
  slug: web-development
seo_title: Balises HTML5 utiles que vous ne connaissez peut-être pas
seo_desc: 'One of the key factors that differentiates HTML 5 from its predecessors
  is the introduction of semantic tags.

  Semantic tags add real meaning to the webpage and make it easy for humans, and search
  engines, to differentiate between different parts of t...'
---

L'un des facteurs clés qui différencient HTML 5 de ses prédécesseurs est l'introduction des balises sémantiques.

Les balises sémantiques ajoutent une réelle signification à la page web et facilitent la différenciation entre les différentes parties du site pour les humains et les moteurs de recherche.

Dans une certaine mesure, cela affecte également le SEO d'une page web.

Pour en tirer les avantages, vous devez connaître les balises HTML5 que vous pouvez utiliser pour améliorer votre site web.

Il existe également des balises HTML5 très utiles mais peu connues qui peuvent s'avérer pratiques. Elles donnent une signification sémantique à votre page web, apportent plus d'accessibilité et facilitent votre travail.

Voici ma liste de 5 balises HTML utiles que vous pourriez vouloir essayer.

## La balise `<abbr>`

Vous utilisez cette balise lorsque vous souhaitez afficher la forme complète d'une abréviation que vous avez utilisée dans votre blog.

Par exemple, si vous écrivez un article sur un produit pour maison intelligente qui possède également des fonctionnalités d'IA que vous souhaitez discuter. Maintenant, il pourrait y avoir des lecteurs occasionnels qui ne sont peut-être pas familiers avec l'IA. L'utilisation de cette balise `abbr` couplée avec l'attribut 'title' affichera aux lecteurs une info-bulle avec le contenu écrit dans la balise title de l'abréviation. Lorsque l'utilisateur survole l'abréviation, cela peut l'aider à apprendre ce que signifie "IA".

Pensez à la quantité de tracas que cela vous épargnerait si vous souhaitez un jour ajouter ce type de fonctionnalité à votre blog. Au lieu de bidouiller avec CSS, tout ce que vous avez à faire est d'insérer cette balise.

### Comment fonctionne la balise `<abbr>`

En supposant que vous écriviez un blog et que vous ayez accès à la vue HTML. Vous devez envelopper le mot abrégé avec `<abbr>` avec un attribut title qui contiendra la définition ou la forme complète du mot abrégé. Lorsque cela est fait correctement, l'info-bulle apparaîtra lorsque l'utilisateur survolera l'abréviation, montrant le contenu que l'attribut 'title' contient.

```html
<p style="font-family: sans-serif;"> Can <abbr title="Artificial Intelligence">AI</abbr> be taught how to reciprocate human emotions?
</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-300.png align="left")

## La balise `<details>`

Vous utilisez cette balise pour créer une boîte conteneur interactive qui peut s'étendre et se réduire lorsque l'utilisateur clique, tout en contenant tout le contenu. En s'étendant, elle montre le contenu à l'intérieur, et se ferme en se réduisant.

Je l'utilise chaque fois que j'ai quelque chose comme des 'FAQ' ou une 'Table des matières' en tête. Cela vous donne le support natif d'un accordéon sans une seule ligne de JS.

Je l'ai utilisé récemment en travaillant sur l'un de mes sites. J'ai construit la section 'Table des matières' en l'utilisant. (Vous pourrez la voir ci-dessous)

### Comment fonctionne la balise `<details>`

Tout d'abord, nous déclarons la balise `<details>` qui enveloppe la balise `<summary>` et votre contenu habituel que vous voulez que l'utilisateur voie lorsqu'il en a besoin. Cela peut être n'importe quoi - un formulaire, un tableau, un paragraphe ou une image.

```html
<details>
	<summary>Table des matières</summary>
    <ul>
    	<li>
        	<a href="#web-dev">Développement Web</a>
        </li>
        <ul>
            <li><a href="#web-dev-html">HTML</a></li>
            <li><a href="#web-dev-css">CSS</a></li>
        </ul>
       </ul>
 </details>
```

Maintenant, j'ai mentionné la balise `<summary>` plus tôt : cette balise est utilisée avec la balise `<details>` et spécifie un en-tête pour le contenu.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/details.gif align="left")

*Crédit Image : Capture d'écran de* [*Freemium Stuff*](https://freemiumstuffings.blogspot.com/2022/05/a-beefy-curated-list-of-valuable-twitter-threads.html)

**Astuce** : Supposons que vous créez une section FAQ avec cette balise, et que vous souhaitez que le conteneur s'ouvre au chargement de la page pour, par exemple, 'La question la plus posée'. Vous pouvez le faire en donnant simplement un attribut 'open' à cet accordéon particulier. Comme ceci :

```html
<details open>
	<summary>Comment faire enregistrer mon produit ?</summary>
    <p>Vous pouvez faire enregistrer votre produit...</p>
</details>
```

## La balise `<optgroup>`

Cette balise vous permettra de catégoriser les options de la liste déroulante dans les formulaires que vous construisez.

Lorsque vous voulez quelque chose comme une liste déroulante à partir de laquelle les utilisateurs peuvent choisir, utilisez la balise `<select>`. Mais souvent, cela peut devenir très long et fastidieux pour les utilisateurs de parcourir toute la liste pour trouver les options correctes.

Grouper les options peut vraiment aider, et vos utilisateurs apprécieront cela car ils n'auront pas à parcourir chaque option. Au lieu de cela, ils peuvent simplement naviguer jusqu'à la catégorie dont ils ont besoin. Cela offre une meilleure expérience utilisateur.

### Comment fonctionne la balise `<optgroup>`

Juste avant de disposer toutes les options, déclarez la balise `<optgroup>` et enveloppez toutes les options similaires dans celle-ci, comme dans l'exemple ci-dessous. Vous pouvez le faire pour autant de groupes que vous le souhaitez.

```html
<label for="cars">Voitures</label>
    <select name="Cars" id="cars">
        <optgroup label="SUV">
            <option value="">Porsche Cayenne</option>
            <option value="">Lincoln Nautilus</option>
            <option value="">Mercedes-Benz GLB 2022</option>
            <option value="">BMW X3 2022</option>
            <option value="">Genesis GV80 2022</option> 
            <option value="">Mercedes-Benz GLS 2022</option>
        </optgroup>
        <optgroup label="Voiture de sport">
            <option value="">Ford Mustang</option>
            <option value="">Toyota GR Supra</option>
            <option value="">McLaren 7205</option>
            <option value="">Porsche 911</option>
            <option value="">Audi R8 V10</option>
            <option value="">Chevrolet Corvette Z06</option>
        </optgroup>
    </select>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-302.png align="left")

*Crédit Image : Auteur*

## La balise `<base>`

Cette balise vous permettra de changer l'URL de base pour toutes les URLs relatives dans ce fichier HTML. Vous devez l'inclure dans la balise `<head>`. Elle vous permet d'avoir la commodité des URLs relatives tout en ayant la flexibilité de changer l'URL de base.

### Comment fonctionne la balise `<base>`

L'utilisateur doit simplement déclarer cette balise à l'intérieur de la balise head, et maintenant toutes les URLs relatives dans le document obtiendront la nouvelle URL comme base.

```html
<head>
	<base href="https://bhaveshrawat.pages.dev/assets/">
</head>
<body>
    <figure style="max-width: 480px;">
        <img style="width: 100%;" src="netflix-planform.webp">
        <figcaption>Netflix Planform fait avec Grid. </figcaption>
    </figure>
    <figure style="max-width: 480px;">
        <img style="width: 100%;" src="hamburger-menu.gif">	
        <figcaption>Barre de menu de la balise &lt;input&gt;</figcaption>
    </figure>
</body>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-305.png align="left")

### Le piège avec la balise `<base>`

Il y a un piège avec l'utilisation de cette balise, cependant. Elle ne fonctionne pas bien avec les balises d'ancrage dans la page, comme `<a href="#home">`. Ces types de liens sont assez utiles d'un point de vue navigation. Donc, à moins que vous ne fassiez du JS pour compenser les balises d'ancrage dans la page, cette balise pourrait ne pas être idéale.

## La balise `<map>`

Si vous avez déjà voulu associer une seule image avec plusieurs liens et les mapper selon l'image, cette balise vous permettra de faire exactement cela.

Cette balise vous permet de spécifier les zones sur une image - il peut s'agir d'un rectangle, d'un cercle ou d'un poly (basiquement n'importe quelle forme irrégulière) - et de les mapper à différents liens.

### Comment fonctionne la balise `<map>`

Tout d'abord, nous spécifions une balise `<img>` avec l'attribut 'usemap' qui contient la même valeur que l'attribut name de la balise `<map>`. Il doit être le même car cela sera responsable de la liaison des coordonnées de la carte à l'image.

La balise `<map>` sera déclarée après cela avec l'attribut 'name' qui contient la même valeur que l'attribut 'usemap'.

La balise `<map>` enveloppe également les balises `<area>` avec les attributs 'shape', 'coords', 'alt' et 'href'. L'attribut shape spécifie la forme de la zone de la carte, coords définit les coordonnées de la zone de la carte à des fins de mappage, alt est pour le texte alternatif, et href contient les liens pour les zones respectives.

```html
<img src="frame.png" width="430" height="194" usemap="#map" />
    <map name="map">
        <area shape="circle" coords="51,51,31" alt="Twitter" href="https://twitter.com/" />
        <area shape="circle" coords="161,52, 33" alt="Github" href="https://github.com/" />
        <area shape="circle" coords="271,51,31" alt="LinkedIn" href="https://linkedin.com/" />
        <area shape="circle" coords="379,51,31" alt="Medium" href="https://medium.com/" />
        <area shape="circle" coords="187, 143, 31" alt="Contra" href="https://contra.com/" />
        <area shape="circle" coords="215, 143, 31" alt="Instagram" href="https://www.instagram.com/" />
        <area shape="circle" coords="323,143,31" alt="Codepen" href="https://codepen.io" />
    </map>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/APNG-1.gif align="left")

### Une chose de plus...

Ce n'est pas une balise, mais plutôt un attribut qui peut vous aider à construire un menu contextuel personnalisé pour votre application. Je parle de l'attribut 'oncontextmenu'.

Le menu contextuel est essentiellement une barre de menu qui apparaît lorsque l'utilisateur fait un clic droit sur le navigateur et est servi avec des options comme 'Inspecter', 'Voir la source de la page' pour n'en nommer que quelques-unes.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/7ecce6cb9af145cb11c57bc6ccb47e1a2c0c5eac.png align="left")

Lors de la construction d'une application web, vous pourriez vouloir servir votre utilisateur avec un menu contextuel personnalisé avec un ensemble d'options et de fonctionnalités spéciales, comme le fait Spotify.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-313.png align="left")

*Crédit Image : Capture d'écran de Spotify*

### Comment fonctionne l'attribut `oncontextmenu`

La valeur de cet attribut est vraie par défaut. Cela vous permet d'accéder au menu contextuel qui apparaît lorsque vous faites un clic droit. Mais, lorsqu'on lui donne une valeur fausse, le menu contextuel n'apparaîtra pas.

Ainsi, vous désactivez le menu contextuel natif car vos utilisateurs n'en auront pas besoin. De plus, il n'interférera pas avec la fonctionnalité de votre application web.

Vous ne voulez pas que votre menu personnalisé soit chevauché/interféré par le menu contextuel natif, n'est-ce pas ? Donc, cet exercice pourrait vous éviter cette horrible expérience.

```html
<body oncontextmenu="return false"></body>
```

Note : L'attribut est applicable à tous les éléments HTML. Cela signifie que si vous ne voulez pas qu'un utilisateur ait la fonctionnalité du menu contextuel sur une certaine section uniquement, vous pouvez le faire aussi. Il suffit d'utiliser l'attribut sur l'élément parent, comme ceci

```html
<body>
    <section oncontextmenu="return false"></section>
</body>
```

## Conclusion

Donc, voici les balises HTML que je voulais partager avec vous tous ! J'espère que cet article valait votre temps et que vous y avez appris quelque chose.

Si l'une de ces balises a piqué votre intérêt, vous pouvez en apprendre plus sur elles sur MDN.

Bonne journée !

Si vous apprenez Git ou commencez à l'utiliser, je voudrais vous recommander un e-Book que j'ai écrit lorsque j'apprenais Git. Il est disponible en format PDF et E-PUB, vous pouvez l'obtenir gratuitement sur [Gumroad](https://bhaveshrawat.gumroad.com/l/lets-git-it-beginners-guide-to-git-bash-commands). J'espère que vous apprécierez l'e-Book.