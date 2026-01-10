---
title: 'Un cours accéléré en design web : d''un non-designer à un autre'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T18:42:38.000Z'
originalURL: https://freecodecamp.org/news/a-web-design-crash-course-from-one-non-designer-to-another-a6f8da0e6aa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hUO_8TtnehSqpj_NPESE8Q.jpeg
tags:
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Design
  slug: web-design
seo_title: 'Un cours accéléré en design web : d''un non-designer à un autre'
seo_desc: 'By Ali Spittel

  I will preface this by saying that I’m not a professional designer. That being said,
  I like building pretty things and have had some success with that. A lot of developers
  seem overwhelmed by design. I wanted to do a quick write-up wit...'
---

Par Ali Spittel

Je commencerai par dire que je ne suis pas une designer professionnelle. Cela dit, j'aime créer de belles choses et j'ai eu un certain succès dans ce domaine. Beaucoup de développeurs semblent submergés par le design. Je voulais faire un rapide article avec des exemples visuels et des conseils rapides sur la façon d'améliorer les visuels de votre site. Les règles sont faites pour être enfreintes. Si vous voulez créer un site web génial aussi facilement que possible, voici quelques bonnes règles à suivre !

### Couleur

J'aime vraiment jouer avec les couleurs sur mes sites web, mais il faut un équilibre et une harmonie de couleurs pour que le site paraisse cohérent et professionnel. Il est essentiel que ces couleurs ne se heurtent pas, qu'elles aient un niveau de contraste raisonnable et qu'elles soient cohérentes.

#### Cohérence

Voici ma palette de couleurs pour [The Zen of Programming](https://the-zen-of-programming.com/) :

![Image](https://cdn-media-1.freecodecamp.org/images/b8l2lxE2xFdpdc7RPaLjfStSd8TEPsElZf48)

J'utilise les mêmes codes hexadécimaux pour le vert, le rose et le gris pour mes arrière-plans, mes en-têtes, mon texte et mes boutons.

Vous pouvez utiliser des variables CSS pour vous assurer que vos couleurs sont les mêmes dans tout votre code.

```
body {   --pink: #CF92B7;   --green: #59876B;   --grey: #4A4A4A; } 
```

```
h1 {   color: var(--pink); }
```

Si vous utilisez SCSS ou un autre préprocesseur CSS, c'est encore plus facile !

En ce qui concerne le nombre de couleurs impliquées dans votre thème, quatre est généralement un bon choix. Peut-être faire deux de ces couleurs neutres (comme le noir, le blanc ou le gris) et deux couleurs plus vives. Les schémas de couleurs monochromatiques qui utilisent des nuances d'une seule couleur peuvent définitivement fonctionner également !

Lorsque je travaille avec des schémas de couleurs arc-en-ciel, je traite l'arc-en-ciel comme une seule couleur et j'utilise ensuite deux neutres pour tout le reste. Par exemple, sur [alispit.tel](https://alispit.tel/), j'utilise un gris foncé pour certains textes, du blanc pour l'arrière-plan, et ensuite les couleurs de l'arc-en-ciel pour les lettres et les formes aléatoires.

![Image](https://cdn-media-1.freecodecamp.org/images/SJFZZv8mvlvHuBLKyHDrrN8BhpX3NJEllHAC)

#### Couleurs qui se heurtent

Il est important de s'assurer que vos couleurs s'harmonisent bien et ne se heurtent pas. Habituellement, les couleurs opposées sur la roue chromatique se heurtent. Bien sûr, vous pouvez créer d'excellents sites web qui utilisent des couleurs qui se heurtent, mais c'est plus difficile et peut être mieux laissé aux designers. Certains exemples seraient le rouge et le vert ou l'orange et le violet.

De plus, gardez à l'esprit les tons des couleurs — si vous utilisez un rose à tons froids, un vert à tons froids peut être bon à associer avec lui plutôt qu'un vert à tons chauds. Les couleurs à tons chauds ont des sous-tons plus rouges, et les couleurs à tons froids sont plus bleutées.

#### Contraste

Assurez-vous qu'il y a un niveau de contraste raisonnable entre les couleurs sur votre site web. Si ce n'est pas le cas, il sera beaucoup plus difficile de lire votre contenu. [Voici](https://marijohannessen.github.io/color-contrast-checker/) un site génial qui vérifiera le contraste pour vous. Les tests Lighthouse le vérifieront également pour vous ! En général, placez des couleurs claires sur des couleurs foncées, et des couleurs foncées sur des couleurs claires !

![Image](https://cdn-media-1.freecodecamp.org/images/E0zc87iuUHaF-DnjTZmCWnXA9C95a3AMEmoT)

#### Signification des couleurs

Si vous travaillez sur un site web pour une marque, différentes couleurs ont différentes [significations implicites](https://graf1x.com/color-psychology-emotion-meaning-poster/) pour les lecteurs. Elles peuvent transmettre différentes humeurs, il peut donc être utile de les garder à l'esprit.

#### Conseils pour choisir les couleurs

Il existe de nombreux sites web géniaux qui facilitent le choix de bonnes palettes de couleurs qui s'harmonisent bien.

J'utilise parfois le générateur [Coolors](https://coolors.co/) lorsque je construis un nouveau site. Je suis également [ce compte](https://www.instagram.com/colours.cafe/) sur Instagram, et j'enregistre les palettes de couleurs que j'aime lorsque je les vois. Enfin, si je veux simplement voir un tas de couleurs et choisir entre elles, j'utilise la page [color](https://materializecss.com/color.html) sur Materialize — j'aime leurs couleurs !

### Texte

Sur la plupart des sites, le texte sera la partie la plus critique. Vous devez le rendre facile à lire et mettre en évidence le contenu le plus important.

Voici un exemple de texte vraiment difficile à lire :

![Image](https://cdn-media-1.freecodecamp.org/images/gz-FtBuGU50NKtqfFHT3VJje8czLSrxdZ3ST)

Améliorons sa lisibilité !

#### Espacement

Ajoutez de l'espacement à votre contenu textuel. Il existe quelques types d'espacement qui peuvent rendre votre contenu plus lisible. Le premier consiste à ajouter un remplissage sur les côtés de votre page.

**Sur les côtés de votre contenu :**

Sur de nombreux sites web — le texte ne s'étendra pas sur toute la largeur de la page, il sera à l'intérieur d'un conteneur qui n'occupe qu'une partie de la page. Cela rend le contenu plus confortable à lire puisque vos yeux ont moins à bouger, et la page aura meilleure apparence. Le [W3C](https://www.w3.org/TR/2008/REC-WCAG20-20081211/#visual-audio-contrast-visual-presentation) recommande moins de 80 caractères par ligne.

```
<style> .container {   width: 80%; margin: 0 auto; } <;/style> 
```

```
<div class="container">   <p>   Lorem ipsum dolor amet master cleanse cloud bread brunch pug PBR&B  actually. Thundercats marfa art party man bun gluten-free  sriracha. DIY tofu cred blue bottle etsy. Retro listicle normcore  glossier next level etsy lumbersexual polaroid pour-over 90's  slow-carb health goth banjo. Unicorn chicharrones 8-bit poke   glossier.   </p> </div>
```

**Hauteur de ligne :**

Nous pouvons ajouter une hauteur de ligne pour ajouter plus d'espace entre les lignes de texte. Le système d'exploitation Android le plus récent a ajouté une hauteur de ligne plus substantielle aux notifications. Cela les rend plus faciles à lire d'un coup d'œil.

De plus, il est préférable pour des raisons d'accessibilité d'ajouter plus de hauteur de ligne — la recommandation du W3C est de 1,5 à 2,0. Vous souvenez-vous d'avoir dû doubler l'espacement des essais au lycée ? Nous faisons la même chose ici, juste en ligne cette fois-ci !

```
p {   font-size: 18px;   line-height: 2.0; }
```

Cela transformera le texte de gauche en texte de droite dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/PCFI7cZKfJyewSUCFQ3H-Ee-uZirNyg3tpU1)

**Remplissage des paragraphes :**

Je m'assurerais également d'ajouter un remplissage entre vos paragraphes afin qu'il soit facile de les différencier.

```
p {   padding-bottom: 27px; }
```

![Image](https://cdn-media-1.freecodecamp.org/images/QCot3EmTYiqhR9j5Y4xLe54J9EG4n1T2nPyY)

**Espacement des mots :**

Si vous utilisez des majuscules pour un en-tête, vous pouvez ajouter plus d'espacement entre les mots pour qu'il soit plus facile de les différencier.

Voici l'en-tête de mon blog avec un espacement de mots supplémentaire :

![Image](https://cdn-media-1.freecodecamp.org/images/SaB6uZ9Wj1a2xBIgLItirhluTN8e90EO9-Rg)

Et voici sans :

![Image](https://cdn-media-1.freecodecamp.org/images/wo5jJb6Yan7R0WSRBDYmUDcRlVlPSd2kFJ3O)

```
h1 {   word-spacing: 9px; }
```

Le premier est beaucoup plus facile à lire !

#### Alignement

Il est plus facile de lire le contenu s'il est aligné à gauche et non justifié pour l'anglais et d'autres langues de haut en bas à droite. Votre contenu sera ainsi par défaut ! Assurez-vous simplement que vous n'avez pas un `text-align: center;` dessus ! N'hésitez pas à centrer vos en-têtes ou le conteneur de votre texte, mais alignez les longs blocs de contenu à gauche.

#### Polices lisibles

Certaines polices sont plus faciles à lire que d'autres. Pour le contenu sur le web, il est généralement plus facile de lire les polices sans empattement. Les empattements sont les petits points qui sortent des extrémités des lettres dans certaines polices — vous pouvez voir un empattement dans le cercle vert dans le diagramme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/258KOJDtqv4mOTY2MZWImL0hytLWMRwQTlvs)

Ma règle générale est d'utiliser une police décorative (pensez à l'écriture cursive ou non traditionnelle) ou une police avec empattement pour les en-têtes et une police sans empattement pour le contenu par site web.

#### Quelques-unes de mes polices préférées :

**Avec empattement et décoratives**

* [Pacifico](https://fonts.google.com/specimen/Pacifico)
* [Righteous](https://fonts.google.com/specimen/Righteous)
* [Fira Sans](https://fonts.google.com/specimen/Fira+Sans)

**Sans empattement**

* [Roboto](https://fonts.google.com/specimen/Roboto)
* [Lato](https://fonts.google.com/specimen/Lato)
* [Montserrat](https://fonts.google.com/specimen/Montserrat)
* Arial — celle-ci est déjà sur votre ordinateur

#### Couleur

Le texte noir sur un fond blanc peut causer une fatigue oculaire en raison d'un contraste trop élevé. J'utilise des gris foncés pour mon contenu. Ensuite, il y a encore beaucoup de contraste, mais pas autant qu'avec du texte noir.

Il en va de même pour les arrière-plans — un noir pur n'est souvent pas le meilleur choix — un bleu marine foncé ou un gris rendra votre contenu plus facile à lire.

#### Taille

Il existe différentes opinions sur la taille que devrait avoir votre contenu et quelle unité de mesure vous devriez utiliser (em vs. px par exemple). Le consensus penche vers 16–18 pixels et avoir cette échelle pour les personnes qui zooment ou dézooment sur votre site.

Les en-têtes de différents types devraient être plus grands que votre contenu. De plus, utilisez différentes épaisseurs de police pour différencier le texte.

![Image](https://cdn-media-1.freecodecamp.org/images/cwYX7xWUHvuzp3pwoHru6Ocb0vA1tF3ozaQH)

#### Une fois ces changements apportés...

Notre contenu devient beaucoup plus facile à lire !

![Image](https://cdn-media-1.freecodecamp.org/images/-dRyZ4r15URJo4ov2Dwc-lMvMGQTzVfKW0-M)

### Arrière-plans

Rendre les images d'arrière-plan belles, surtout avec du texte par-dessus, est vraiment difficile. J'éviterais les images d'arrière-plan sauf si elles sont essentielles au site. Je vais donner quelques alternatives et solutions pour faire fonctionner les images d'arrière-plan si vous décidez toujours d'en utiliser une !

Sur l'image ci-dessous, le texte est difficile à lire.

![Image](https://cdn-media-1.freecodecamp.org/images/22EzCEej-9B869OCC6er9fcJE3tZmVCZdT8D)

#### Diviser la page

Si vous voulez garder l'image, vous pouvez diviser la page pour que l'image s'affiche sur une moitié et le texte sur l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/JVVDYYIpytq45Om2cGrDNxfmQDxihTO2QuN4)

```
<style>   .container {     display: grid;     grid-template-columns: 1fr 1fr;   } &lt;/style>
```

```
<div class="container">   <div class="text">My Text</div>  <img src="path/to/img"> </div>
```

#### Utiliser une image moins chargée

Si vous voulez garder l'image d'arrière-plan en pleine page, si possible, utilisez une image simple sans trop de choses. Dans celle que j'utilise ci-dessus, il y a beaucoup de couleurs et de gros textes que l'utilisateur peut encore lire. Utiliser une image de paysage ou un motif sera moins distrayant.

#### Ajouter une ombre au texte

Vous pouvez également ajouter une ombre au texte sous votre texte pour le rendre plus lisible.

```
.text {   text-shadow: #4A4A4A 1px 1px 8px; }
```

Avec les modifications ci-dessus en place et une taille de police augmentée, la police sur une image d'arrière-plan devient beaucoup plus facile à lire !

![Image](https://cdn-media-1.freecodecamp.org/images/BaFBx3kizuvmCKpCQlY5ciiKrhVIurt0Q0HC)

#### Couleurs d'arrière-plan

Je n'utiliserais pas une couleur super vive pour votre arrière-plan. Pratiquement n'importe quelle couleur sera difficile à lire par-dessus, et cela peut fatiguer les yeux des gens pour lire.

### Appels à l'action

Lorsque vous construisez un site web, il y a généralement quelque chose que vous voulez que l'utilisateur fasse. Sur les sites de commerce électronique, vous voulez que l'utilisateur achète quelque chose. Sur un portfolio, vous voulez probablement que le spectateur vous contacte. Sur un blog, vous voulez que l'utilisateur s'abonne. Lorsque vous concevez un site, gardez cette action à l'esprit. Vous pouvez vouloir utiliser une couleur vive, un texte plus grand, ou mettre en avant cet "appel à l'action" à plusieurs endroits sur votre site. Vous pouvez également vouloir vous assurer qu'il est visible partout sur le site.

Par exemple, mon formulaire d'abonnement pour mon blog est toujours dans la barre latérale, et il a une couleur pour attirer l'attention du lecteur. Sur mon portfolio, j'ai des liens vers mes comptes de réseaux sociaux sur les pages d'accueil, à propos et de contact.

Mettre en évidence le contenu important sera différent sur chaque site. Il est important de garder à l'esprit l'action que vous voulez que l'utilisateur entreprenne avec chaque choix de design que vous faites.

#### Plus de lectures

* [Smashing Magazine](https://www.smashingmagazine.com/articles/) — beaucoup d'articles sur le design ici
* [Designing with Sketch](https://dev.to/aspittel/designing-with-sketch-42jp) — un article que j'ai écrit sur la façon d'utiliser le logiciel de design Sketch, que j'utilise pour concevoir tout. Beaucoup des étapes s'appliqueront également à d'autres logiciels de design.
* [Hello Web Design](https://hellowebbooks.com/learn-design/) — C'est un livre génial qui discute du design web destiné aux débutants.
* [The Little Details of UI Design](https://speakerdeck.com/sschoger/the-little-details-of-ui-design) — Un excellent diaporama qui passe en revue une refonte de LinkedIn — celui-ci est un peu plus avancé.

### Frameworks UI

Vous ne voulez peut-être pas commencer de zéro lorsque vous concevez un site, donc l'utilisation d'un Framework UI peut être utile. Certains d'entre eux incluent :

* [Bootstrap](https://v4-alpha.getbootstrap.com/), que je m'assurerais de personnaliser car il est largement utilisé
* [Materialize](https://materializecss.com/), qui suit la philosophie de design Material de Google, et
* [Grommet](http://grommet.io/), mon préféré esthétiquement — il met également l'accent sur l'accessibilité.

### Liste de contrôle de design

Puisque cet article est assez long avec beaucoup de conseils, je voulais distiller les informations les plus importantes dans une liste de contrôle. Elle est écrite en markdown GitHub, donc vous pouvez la copier et la coller sur un problème ou dans un fichier markdown. Ensuite, vous pouvez soit cocher la case, soit remplacer l'espace par un `x` pour chaque élément d'action.

```
## Couleur - [ ] Utilise des couleurs cohérentes partout - [ ] Utilise des couleurs non conflictuelles - [ ] Le choix des couleurs est pertinent pour le but commercial du site 
```

```
## Texte - [ ] Le texte a un remplissage des deux côtés. - [ ] La hauteur de ligne est de 1,5-2,0 - [ ] Il y a un remplissage entre les paragraphes - [ ] Si vos titres sont en majuscules, il y a un espacement accru entre les mots - [ ] Les blocs de texte ne sont pas justifiés - [ ] Les blocs de texte sont alignés à gauche - [ ] Les polices sans empattement sont utilisées pour le texte du corps - [ ] Un maximum de deux polices sont utilisées - une décorative ou avec empattement et une sans empattement - [ ] Le texte du corps n'est pas noir pur sur blanc - [ ] Le texte du corps est de 16-18px et est redimensionnable 
```

```
## Arrière-plans - [ ] Utiliser un motif ou une image simple - [ ] Une ombre de texte est utilisée pour rendre les titres lisibles - [ ] L'arrière-plan n'est pas trop brillant 
```

```
## Appels à l'action - [ ] Les informations importantes sont mises en évidence afin d'attirer l'interaction de l'utilisateur
```

### Restez en contact

Si vous avez aimé cet article et que vous voulez en lire plus, j'ai une [newsletter hebdomadaire](https://tinyletter.com/ali_writes_code) avec mes liens préférés de la semaine et mes derniers articles. De plus, [tweetez](https://twitter.com/aspittel) vos conseils de design préférés ! J'en ai beaucoup plus que je n'aurais pu en discuter dans cet article comme la réactivité, l'espace blanc et l'alignement. Si vous voulez voir plus de publications comme celle-ci, faites-le moi savoir !

_Publié à l'origine sur [zen-of-programming.com](https://zen-of-programming.com/design)._