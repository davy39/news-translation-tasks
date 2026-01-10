---
title: 'Le manuel CSS : un guide pratique de CSS pour les développeurs'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-04-24T15:51:53.000Z'
originalURL: https://freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aeXtrs9UI4WniMd1miDIDw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: 'Le manuel CSS : un guide pratique de CSS pour les développeurs'
seo_desc: 'I wrote this article to help you quickly learn CSS and get familiar with
  the advanced CSS topics.

  CSS is often quickly dismissed as an easy thing to learn by developers, or one thing
  you just pick up when you need to quickly style a page or app. Due ...'
---

J'ai écrit cet article pour vous aider à apprendre rapidement CSS et à vous familiariser avec les sujets avancés de CSS.

CSS est souvent rapidement écarté comme une chose facile à apprendre par les développeurs, ou une chose que vous apprenez simplement lorsque vous devez rapidement styliser une page ou une application. Pour cette raison, il est souvent appris à la volée, ou nous apprenons des choses de manière isolée au moment où nous devons les utiliser. Cela peut être une source énorme de frustration lorsque nous découvrons que l'outil ne fait pas simplement ce que nous voulons.

Cet article vous aidera à vous mettre à niveau avec CSS et à obtenir un aperçu des principales fonctionnalités modernes que vous pouvez utiliser pour styliser vos pages et applications.

J'espère vous aider à vous sentir à l'aise avec CSS et à vous mettre rapidement à niveau avec l'utilisation de cet outil génial qui vous permet de créer des designs époustouflants sur le Web.

**[Cliquez ici pour obtenir une version PDF / ePub / Mobi de cet article à lire hors ligne](https://flaviocopes.com/page/css-handbook)**

CSS, une abréviation de Cascading Style Sheets, est l'un des principaux éléments de construction du Web. Son histoire remonte aux années 90, et avec HTML, il a beaucoup changé depuis ses modestes débuts.

Comme je crée des sites web depuis avant que CSS n'existe, j'ai vu son évolution.

CSS est un outil incroyable, et ces dernières années, il a beaucoup évolué, introduisant de nombreuses fonctionnalités fantastiques comme CSS Grid, Flexbox et les propriétés personnalisées CSS.

Ce manuel s'adresse à un large public.

Tout d'abord, le débutant. J'explique CSS à partir de zéro de manière succincte mais complète, afin que vous puissiez utiliser ce livre pour apprendre CSS à partir des bases.

Ensuite, le professionnel. CSS est souvent considéré comme une chose secondaire à apprendre, surtout par les développeurs JavaScript. Ils savent que CSS n'est pas un vrai langage de programmation, ils sont programmeurs et donc ils ne devraient pas se soucier d'apprendre CSS de la bonne manière. J'ai écrit ce livre pour vous aussi.

Ensuite, la personne qui connaît CSS depuis quelques années mais n'a pas eu l'occasion d'apprendre les nouvelles choses qu'il contient. Nous parlerons longuement des nouvelles fonctionnalités de CSS, celles qui vont construire le web de la prochaine décennie.

CSS s'est beaucoup amélioré ces dernières années et il évolue rapidement.

Même si vous n'écrivez pas de CSS pour gagner votre vie, savoir comment fonctionne CSS peut vous aider à éviter quelques maux de tête lorsque vous devez le comprendre de temps en temps, par exemple lors de la modification d'une page web.

Merci d'avoir obtenu cet ebook. Mon objectif avec celui-ci est de vous donner un aperçu rapide mais complet de CSS.

Flavio

Vous pouvez me contacter par email à l'adresse [flavio@flaviocopes.com](mailto:flavio@flaviocopes.com), sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).

Mon site web est [flaviocopes.com](https://flaviocopes.com/).

## Table des matières

* [INTRODUCTION À CSS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#introduction-a-css)
* [UN BREF HISTORIQUE DE CSS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#un-bref-historique-de-css)
* [AJOUTER CSS À UNE PAGE HTML](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#ajouter-css-a-une-page-html)
* [SÉLECTEURS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#selecteurs)
* [CASCADE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#cascade)
* [SPÉCIFICITÉ](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#specificite)
* [HÉRITAGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#heritage)
* [IMPORT](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#import)
* [SÉLECTEURS D'ATTRIBUTS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#selecteurs-dattributs)
* [PSEUDO-CLASSES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#pseudo-classes)
* [PSEUDO-ÉLÉMENTS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#pseudo-elements)
* [COULEURS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#couleurs)
* [UNITÉS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#unites)
* [URL](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#url)
* [CALC](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#calc)
* [ARRIÈRE-PLANS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#arriere-plans)
* [COMMENTAIRES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#commentaires)
* [PROPRIÉTÉS PERSONNALISÉES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#proprietes-personnalisees)
* [POLICES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#polices)
* [TYPOGRAPHIE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#typographie)
* [MODÈLE DE BOÎTE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#modele-de-boite)
* [BORDURE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#bordure)
* [REMPLISSAGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#remplissage)
* [MARGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#marge)
* [DIMENSIONNEMENT DE BOÎTE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#dimensionnement-de-boite)
* [AFFICHAGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#affichage)
* [POSITIONNEMENT](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#positionnement)
* [FLOTTANT ET NETTOYAGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#flottant-et-nettoyage)
* [Z-INDEX](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#z-index)
* [GRID CSS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#css-grid)
* [FLEXBOX](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#flexbox)
* [TABLEAUX](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#tableaux)
* [CENTRAGE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#centrage)
* [LISTES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#listes)
* [REQUÊTES MÉDIA ET DESIGN RESPONSIVE](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#media-queries-et-responsive-design)
* [REQUÊTES DE FONCTIONNALITÉS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#feature-queries)
* [FILTRES](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#filtres)
* [TRANSFORMATIONS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#transformations)
* [TRANSITIONS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#transitions)
* [ANIMATIONS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#animations)
* [NORMALISATION CSS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#normalisation-css)
* [GESTION DES ERREURS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#gestion-des-erreurs)
* [PRÉFIXES DE FOURNISSEURS](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#prefixes-de-fournisseurs)
* [CSS POUR L'IMPRESSION](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#css-pour-limpression)
* [CONCLUSION](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/#conclusion)

### INTRODUCTION À CSS

**CSS** (une abréviation de **Cascading Style Sheets**) est le langage que nous utilisons pour styliser un fichier HTML, et dire au navigateur comment il doit rendre les éléments sur la page.

> _Dans ce livre, je parle exclusivement de la mise en style de documents HTML, bien que CSS puisse être utilisé pour styliser d'autres choses également._

Un fichier CSS contient plusieurs règles CSS.

Chaque règle est composée de 2 parties :

* le **sélecteur**
* le **bloc de déclaration**

Le sélecteur est une chaîne qui identifie un ou plusieurs éléments sur la page, suivant une syntaxe spéciale dont nous parlerons bientôt en détail.

Le bloc de déclaration contient une ou plusieurs **déclarations**, composées à leur tour d'une paire **propriété** et **valeur**.

Ce sont toutes les choses que nous avons en CSS.

Organiser soigneusement les propriétés, leur associer des valeurs, et attacher celles-ci à des éléments spécifiques de la page en utilisant un sélecteur est l'argument principal de cet ebook.

#### À quoi ressemble CSS

Un ensemble de règles CSS a une partie appelée **sélecteur**, et l'autre partie appelée **déclaration**. La déclaration contient diverses **règles**, chacune composée d'une **propriété**, et d'une **valeur**.

Dans cet exemple, `p` est le sélecteur, et applique une règle qui définit la valeur `20px` pour la propriété `font-size` :

```css
p {
  font-size: 20px;
}
```

Plusieurs règles sont empilées les unes après les autres :

```css
p {
  font-size: 20px;
}

a {
  color: blue;
}
```

Un sélecteur peut cibler un ou plusieurs éléments :

```css
p, a {
  font-size: 20px;
}
```

et il peut cibler des balises HTML, comme ci-dessus, ou des éléments HTML qui contiennent un certain attribut de classe avec `.my-class`, ou des éléments HTML qui ont un attribut `id` spécifique avec `#my-id`.

Des sélecteurs plus avancés vous permettent de choisir des éléments dont l'attribut correspond à une valeur spécifique, ou également des éléments qui répondent à des pseudo-classes (plus d'informations à ce sujet plus tard)

#### Points-virgules

Chaque règle CSS se termine par un point-virgule. Les points-virgules ne sont **pas** optionnels, sauf après la dernière règle. Mais je suggère de toujours les utiliser pour la cohérence et pour éviter les erreurs si vous ajoutez une autre propriété et oubliez d'ajouter le point-virgule sur la ligne précédente.

#### Formatage et indentation

Il n'y a pas de règle fixe pour le formatage. Ce CSS est valide :

```css
p
      {
  font-size:           20px   ;
                      }
                      
a{color:blue;}
```

mais c'est une douleur à voir. Respectez certaines conventions, comme celles que vous voyez dans les exemples ci-dessus : collez les sélecteurs et les accolades fermantes à gauche, indentiez de 2 espaces pour chaque règle, placez l'accolade ouvrante sur la même ligne que le sélecteur, séparée par un espace.

Une utilisation correcte et cohérente de l'espacement et de l'indentation est une aide visuelle pour comprendre votre code.

### UN BREF HISTORIQUE DE CSS

Avant de continuer, je veux vous donner un bref rappel de l'histoire de CSS.

CSS est né de la nécessité de styliser les pages web. Avant l'introduction de CSS, les gens voulaient un moyen de styliser leurs pages web, qui avaient toutes un aspect très similaire et « académique » à l'époque. Vous ne pouviez pas faire grand-chose en termes de personnalisation.

HTML 3.2 a introduit l'option de définir des couleurs en ligne en tant qu'attributs d'éléments HTML, et des balises de présentation comme `center` et `font`, mais cela a rapidement dégénéré en une situation loin d'être idéale.

CSS nous a permis de déplacer tout ce qui est lié à la présentation de l'HTML vers le CSS, afin que l'HTML puisse redevenir le format qui définit la structure du document, plutôt que la manière dont les choses devraient apparaître dans le navigateur.

CSS évolue continuellement, et le CSS que vous utilisiez il y a 5 ans pourrait bien être obsolète, car de nouvelles techniques CSS idiomatiques ont émergé et les navigateurs ont changé.

Il est difficile d'imaginer les temps où CSS est né et à quel point le web était différent.

À l'époque, nous avions plusieurs navigateurs concurrents, les principaux étant Internet Explorer ou Netscape Navigator.

Les pages étaient stylisées en utilisant HTML, avec des balises de présentation spéciales comme `bold` et des attributs spéciaux, dont la plupart sont maintenant obsolètes.

Cela signifiait que vous aviez un nombre limité d'opportunités de personnalisation.

La majorité des décisions de style étaient laissées au navigateur.

De plus, vous construisiez un site spécifiquement pour l'un d'eux, car chacun introduisait différentes balises non standard pour donner plus de puissance et d'opportunités.

Bientôt, les gens ont réalisé le besoin d'un moyen de styliser les pages, d'une manière qui fonctionnerait sur tous les navigateurs.

Après l'idée initiale proposée en 1994, CSS a obtenu sa première version en 1996, lorsque la recommandation CSS Level 1 (« CSS 1 ») a été publiée.

CSS Level 2 (« CSS 2 ») a été publié en 1998.

Depuis lors, le travail a commencé sur CSS Level 3. Le groupe de travail CSS a décidé de diviser chaque fonctionnalité et de travailler dessus séparément, en modules.

Les navigateurs n'étaient pas particulièrement rapides à implémenter CSS. Nous avons dû attendre jusqu'en 2002 pour avoir le premier navigateur implémenter la spécification CSS complète : IE pour Mac, comme décrit dans cet article de CSS Tricks : [https://css-tricks.com/look-back-history-css/](https://css-tricks.com/look-back-history-css/)

Internet Explorer a implémenté le modèle de boîte incorrectement dès le départ, ce qui a conduit à des années de douleur en essayant d'avoir le même style appliqué de manière cohérente sur tous les navigateurs. Nous avons dû utiliser divers trucs et astuces pour faire en sorte que les navigateurs rendent les choses comme nous le voulions.

Aujourd'hui, les choses sont beaucoup, beaucoup mieux. Nous pouvons simplement utiliser les standards CSS sans penser aux particularités, la plupart du temps, et CSS n'a jamais été aussi puissant.

Nous n'avons plus de numéros de version officiels pour CSS maintenant, mais le groupe de travail CSS publie un « instantané » des modules qui sont actuellement considérés comme stables et prêts à être inclus dans les navigateurs. Voici le dernier instantané, de 2018 : [https://www.w3.org/TR/css-2018/](https://www.w3.org/TR/css-2018/)

CSS Level 2 est toujours la base du CSS que nous écrivons aujourd'hui, et nous avons beaucoup plus de fonctionnalités construites par-dessus.

### AJOUTER CSS À UNE PAGE HTML

CSS est attaché à une page HTML de différentes manières.

#### 1 : Utilisation de la balise `link`

La balise `link` est le moyen d'inclure un fichier CSS. C'est la manière préférée d'utiliser CSS comme il est censé être utilisé : un fichier CSS est inclus par toutes les pages de votre site, et changer une ligne dans ce fichier affecte la présentation de toutes les pages du site.

Pour utiliser cette méthode, vous ajoutez une balise `link` avec l'attribut `href` pointant vers le fichier CSS que vous souhaitez inclure. Vous l'ajoutez à l'intérieur de la balise `head` du site (pas à l'intérieur de la balise `body`) :

```html
<link rel="stylesheet" type="text/css" href="myfile.css">
```

Les attributs `rel` et `type` sont également requis, car ils indiquent au navigateur quel type de fichier nous sommes en train de lier.

#### 2 : utiliser la balise `style`

Au lieu d'utiliser la balise `link` pour pointer vers une feuille de style séparée contenant notre CSS, nous pouvons ajouter le CSS directement à l'intérieur d'une balise `style`. Voici la syntaxe :

```html
<style>
...notre CSS...
</style>
```

En utilisant cette méthode, nous pouvons éviter de créer un fichier CSS séparé. Je trouve que c'est une bonne façon d'expérimenter avant de « formaliser » le CSS dans un fichier séparé, ou d'ajouter une ligne spéciale de CSS juste pour un fichier.

#### 3 : styles en ligne

Les styles en ligne sont la troisième façon d'ajouter du CSS à une page. Nous pouvons ajouter un attribut `style` à n'importe quelle balise HTML, et ajouter du CSS à l'intérieur.

```
<div style="">...</div>
```

Exemple :

```html
<div style="background-color: yellow">...</div>
```

### SÉLECTEURS

Un sélecteur nous permet d'associer une ou plusieurs déclarations à un ou plusieurs éléments sur la page.

#### Sélecteurs de base

Supposons que nous avons un élément `p` sur la page, et nous voulons afficher les mots à l'intérieur en utilisant la couleur jaune.

Nous pouvons **cibler** cet élément en utilisant ce sélecteur `p`, qui cible tous les éléments utilisant la balise `p` dans la page. Une simple règle CSS pour atteindre ce que nous voulons est :

```css
p {
  color: yellow;
}
```

Chaque balise HTML a un sélecteur correspondant, par exemple : `div`, `span`, `img`.

Si un sélecteur correspond à plusieurs éléments, tous les éléments de la page seront affectés par le changement.

Les éléments HTML ont 2 attributs qui sont très couramment utilisés dans CSS pour associer un style à un élément spécifique sur la page : `class` et `id`.

Il y a une grande différence entre ces deux attributs : à l'intérieur d'un document HTML, vous pouvez répéter la même valeur de `class` sur plusieurs éléments, mais vous ne pouvez utiliser un `id` qu'une seule fois. Par conséquent, en utilisant des classes, vous pouvez sélectionner un élément avec 2 noms de classe spécifiques ou plus, ce qui n'est pas possible en utilisant des ids.

Les classes sont identifiées en utilisant le symbole `.`, tandis que les ids utilisent le symbole `#`.

Exemple utilisant une classe :

```css
<p class="dog-name">
  Roger
</p>

.dog-name {
  color: yellow;
}
```

Exemple utilisant un id :

```css
<p id="dog-name">
  Roger
</p>

#dog-name {
  color: yellow;
}
```

#### Combinaison de sélecteurs

Jusqu'à présent, nous avons vu comment cibler un élément, une classe ou un id. Introduisons des sélecteurs plus puissants.

#### Cibler un élément avec une classe ou un id

Vous pouvez cibler un élément spécifique qui a une classe ou un id attaché.

Exemple utilisant une classe :

```css
<p class="dog-name">
  Roger
</p>

p.dog-name {
  color: yellow;
}
```

Exemple utilisant un id :

```css
<p id="dog-name">
  Roger
</p>

p#dog-name {
  color: yellow;
}
```

Pourquoi voudriez-vous faire cela, si la classe ou l'id fournit déjà un moyen de cibler cet élément ? Vous pourriez avoir à le faire pour avoir plus de spécificité. Nous verrons ce que cela signifie plus tard.

#### Cibler plusieurs classes

Vous pouvez cibler un élément avec une classe spécifique en utilisant `.class-name`, comme vous l'avez vu précédemment. Vous pouvez cibler un élément avec 2 (ou plus) classes en combinant les noms de classe séparés par un point, sans espaces.

Exemple :

```css
<p class="dog-name roger">
  Roger
</p>

.dog-name.roger {
  color: yellow;
}
```

#### Combinaison de classes et d'ids

De la même manière, vous pouvez combiner une classe et un id.

Exemple :

```css
<p class="dog-name" id="roger">
  Roger
</p>

.dog-name#roger {
  color: yellow;
}
```

#### Regroupement de sélecteurs

Vous pouvez combiner des sélecteurs pour appliquer les mêmes déclarations à plusieurs sélecteurs. Pour ce faire, vous les séparez par une virgule.

Exemple :

```css
<p>
  Le nom de mon chien est :
</p>
<span class="dog-name">
  Roger
</span>

p, .dog-name {
  color: yellow;
}
```

Vous pouvez ajouter des espaces dans ces déclarations pour les rendre plus claires :

```css
p,
.dog-name {
  color: yellow;
}
```

#### Suivre l'arborescence du document avec les sélecteurs

Nous avons vu comment cibler un élément dans la page en utilisant un nom de balise, une classe ou un id.

Vous pouvez créer un sélecteur plus spécifique en combinant plusieurs éléments pour suivre la structure de l'arborescence du document. Par exemple, si vous avez une balise `span` imbriquée dans une balise `p`, vous pouvez cibler celle-ci sans appliquer le style à une balise `span` non incluse dans une balise `p` :

```css
<span>
  Bonjour !
</span>
<p>
  Le nom de mon chien est :
  <span class="dog-name">
    Roger
  </span>
</p>

p span {
  color: yellow;
}
```

Voyez comment nous avons utilisé un espace entre les deux jetons `p` et `span`.

Cela fonctionne même si l'élément de droite est à plusieurs niveaux de profondeur.

Pour rendre la dépendance stricte au premier niveau, vous pouvez utiliser le symbole `>` entre les deux jetons :

```css
p > span {
  color: yellow;
}
```

Dans ce cas, si un `span` n'est pas un premier enfant de l'élément `p`, il ne va pas avoir la nouvelle couleur appliquée.

Les enfants directs auront le style appliqué :

```html
<p>
  <span>
    Ceci est jaune
  </span>
  <strong>
    <span>
      Ceci n'est pas jaune
    </span>
  </strong>
</p>
```

Les sélecteurs de frères adjacents nous permettent de styliser un élément uniquement s'il est précédé par un élément spécifique. Nous le faisons en utilisant l'opérateur `+` :

Exemple :

```css
p + span {
  color: yellow;
}
```

Cela assignera la couleur jaune à tous les éléments span précédés par un élément `p` :

```html
<p>Ceci est un paragraphe</p>
<span>Ceci est un span jaune</span>
```

Nous avons beaucoup plus de sélecteurs que nous pouvons utiliser :

* sélecteurs d'attributs
* sélecteurs de pseudo-classe
* sélecteurs de pseudo-élément

Nous trouverons tout à leur sujet dans les prochaines sections.

### CASCADE

La cascade est un concept fondamental de CSS. Après tout, elle est dans le nom lui-même, le premier C de CSS — Cascading Style Sheets — elle doit être une chose importante.

Que signifie-t-elle ?

La cascade est le processus, ou l'algorithme, qui détermine les propriétés appliquées à chaque élément sur la page. En essayant de converger à partir d'une liste de règles CSS qui sont définies à divers endroits.

Elle le fait en prenant en considération :

* la spécificité
* l'importance
* l'héritage
* l'ordre dans le fichier

Elle prend également soin de résoudre les conflits.

Deux règles CSS concurrentes ou plus pour la même propriété appliquée au même élément doivent être élaborées selon la spécification CSS, pour déterminer laquelle doit être appliquée.

Même si vous n'avez qu'un seul fichier CSS chargé par votre page, il y a d'autres CSS qui vont faire partie du processus. Nous avons le CSS de l'agent utilisateur (navigateur). Les navigateurs viennent avec un ensemble de règles par défaut, toutes différentes entre les navigateurs.

Ensuite, votre CSS entre en jeu.

Ensuite, le navigateur applique toute feuille de style utilisateur, qui peut également être appliquée par des extensions de navigateur.

Toutes ces règles entrent en jeu lors du rendu de la page.

Nous allons maintenant voir les concepts de spécificité et d'héritage.

### SPÉCIFICITÉ

Que se passe-t-il lorsqu'un élément est ciblé par plusieurs règles, avec différents sélecteurs, qui affectent la même propriété ?

Par exemple, parlons de cet élément :

```html
<p class="dog-name">
  Roger
</p>
```

Nous pouvons avoir

```css
.dog-name {
  color: yellow;
}
```

et une autre règle qui cible `p`, qui définit la couleur à une autre valeur :

```css
p {
  color: red;
}
```

Et une autre règle qui cible `p.dog-name`. Quelle règle va prendre le pas sur les autres, et pourquoi ?

Entrez la spécificité. **La règle la plus spécifique gagnera**. Si deux règles ou plus ont la **même spécificité, celle qui apparaît en dernier gagne**.

Parfois, ce qui est plus spécifique en pratique est un peu déroutant pour les débutants. Je dirais que c'est aussi déroutant pour les experts qui ne regardent pas souvent ces règles, ou qui les négligent simplement.

#### Comment calculer la spécificité

La spécificité est calculée en utilisant une convention.

Nous avons 4 emplacements, et chacun d'eux commence à 0 : `0 0 0 0`. L'emplacement à gauche est le plus important, et celui le plus à droite est le moins important.

Comme cela fonctionne pour les nombres dans le système décimal : `1 0 0 0` est supérieur à `0 1 0 0`.

#### Emplacement 1

Le premier emplacement, celui le plus à droite, est le moins important.

Nous augmentons cette valeur lorsque nous avons un **sélecteur d'élément**. Un élément est un nom de balise. Si vous avez plus d'un sélecteur d'élément dans la règle, vous incrémentez en conséquence la valeur stockée dans cet emplacement.

Exemples :

```css
p {}                    /* 0 0 0 1 */
span {}                 /* 0 0 0 1 */
p span {}               /* 0 0 0 2 */
p > span {}             /* 0 0 0 2 */
div p > span {}         /* 0 0 0 3 */
```

#### Emplacement 2

Le deuxième emplacement est incrémenté par 3 choses :

* sélecteurs de classe
* sélecteurs de pseudo-classe
* sélecteurs d'attribut

Chaque fois qu'une règle rencontre l'un de ceux-ci, nous incrémentons la valeur de la deuxième colonne à partir de la droite.

Exemples :

```css
.name {}                 /* 0 0 1 0 */
.users .name {}          /* 0 0 2 0 */
[href$='.pdf'] {}        /* 0 0 1 0 */
:hover {}                /* 0 0 1 0 */
```

Bien sûr, les sélecteurs de l'emplacement 2 peuvent être combinés avec les sélecteurs de l'emplacement 1 :

```css
div .name {}             /* 0 0 1 1 */
a[href$='.pdf'] {}       /* 0 0 1 1 */
.pictures img:hover {}   /* 0 0 2 1 */
```

Un bon truc avec les classes est que vous pouvez répéter la même classe et augmenter la spécificité. Par exemple :

```css
.name {}              /* 0 0 1 0 */
.name.name {}         /* 0 0 2 0 */
.name.name.name {}    /* 0 0 3 0 */
```

#### Emplacement 3

L'emplacement 3 contient la chose la plus importante qui peut affecter votre spécificité CSS dans un fichier CSS : l'`id`.

Chaque élément peut avoir un attribut `id` assigné, et nous pouvons utiliser cela dans notre feuille de style pour cibler l'élément.

Exemples :

```css
#name {}                    /* 0 1 0 0 */
.user #name {}              /* 0 1 1 0 */
#name span {}               /* 0 1 0 1 */
```

#### Emplacement 4

L'emplacement 4 est affecté par les styles en ligne. Tout style en ligne aura la priorité sur toute règle définie dans un fichier CSS externe, ou à l'intérieur de la balise `style` dans l'en-tête de la page.

Exemple :

```html
<p style="color: red">Test</p> /* 1 0 0 0 */
```

Même si une autre règle dans le CSS définit la couleur, cette règle de style en ligne va être appliquée. Sauf dans un cas — si `!important` est utilisé, ce qui remplit l'emplacement 5.

#### Importance

La spécificité n'a pas d'importance si une règle se termine par `!important` :

```css
p {
  font-size: 20px!important;
}
```

Cette règle aura la priorité sur toute règle avec plus de spécificité

Ajouter `!important` dans une règle CSS rendra cette règle plus importante que toute autre règle, selon les règles de spécificité. La seule façon pour une autre règle de prendre le dessus est d'avoir également `!important`, et d'avoir une spécificité plus élevée dans les autres emplacements moins importants.

#### Conseils

En général, vous devriez utiliser la quantité de spécificité dont vous avez besoin, mais pas plus. De cette façon, vous pouvez créer d'autres sélecteurs pour écraser les règles définies par les règles précédentes sans devenir fou.

`!important` est un outil très débattu que CSS nous offre. De nombreux experts CSS s'opposent à son utilisation. Je me surprends à l'utiliser surtout lorsque j'essaie un style et qu'une règle CSS a tellement de spécificité que j'ai besoin d'utiliser `!important` pour faire appliquer mon nouveau CSS par le navigateur.

Mais généralement, `!important` ne devrait pas avoir sa place dans vos fichiers CSS.

Utiliser l'attribut `id` pour styliser CSS est également beaucoup débattu, car il a une spécificité très élevée. Une bonne alternative est d'utiliser des classes à la place, qui ont moins de spécificité, et sont donc plus faciles à travailler, et plus puissantes (vous pouvez avoir plusieurs classes pour un élément, et une classe peut être réutilisée plusieurs fois).

#### Outils pour calculer la spécificité

Vous pouvez utiliser le site [https://specificity.keegan.st/](https://specificity.keegan.st/) pour effectuer le calcul de spécificité automatiquement pour vous.

C'est utile surtout si vous essayez de comprendre les choses, car cela peut être un bon outil de retour d'information.

### HÉRITAGE

Lorsque vous définissez certaines propriétés sur un sélecteur en CSS, elles sont héritées par tous les enfants de ce sélecteur.

J'ai dit _certaines_, car toutes les propriétés ne présentent pas ce comportement.

Cela se produit parce que certaines propriétés ont du sens à être héritées. Cela nous aide à écrire du CSS beaucoup plus concis, puisque nous n'avons pas à définir explicitement cette propriété à nouveau sur chaque enfant.

D'autres propriétés ont plus de sens à _ne pas_ être héritées.

Pensez aux polices : vous n'avez pas besoin d'appliquer le `font-family` à chaque balise de votre page. Vous définissez la police de la balise `body`, et chaque enfant l'hérite, ainsi que d'autres propriétés.

La propriété `background-color`, en revanche, a peu de sens à être héritée.

#### Propriétés qui héritent

Voici une liste des propriétés qui héritent. La liste n'est pas exhaustive, mais ces règles sont simplement les plus populaires que vous utiliserez probablement :

* border-collapse
* border-spacing
* caption-side
* color
* cursor
* direction
* empty-cells
* font-family
* font-size
* font-style
* font-variant
* font-weight
* font-size-adjust
* font-stretch
* font
* letter-spacing
* line-height
* list-style-image
* list-style-position
* list-style-type
* list-style
* orphans
* quotes
* tab-size
* text-align
* text-align-last
* text-decoration-color
* text-indent
* text-justify
* text-shadow
* text-transform
* visibility
* white-space
* widows
* word-break
* word-spacing

Je l'ai obtenu à partir de cet [article de Sitepoint](https://www.sitepoint.com/css-inheritance-introduction/) sur l'héritage CSS.

#### Forcer les propriétés à hériter

Que se passe-t-il si vous avez une propriété qui n'est pas héritée par défaut, et que vous voulez qu'elle le soit, dans un enfant ?

Dans les enfants, vous définissez la valeur de la propriété sur le mot-clé spécial `inherit`.

Exemple :

```css
body {
    background-color: yellow;
}

p {
  background-color: inherit;
}
```

#### Forcer les propriétés à NE PAS hériter

Au contraire, vous pourriez avoir une propriété héritée et vous voulez l'éviter.

Vous pouvez utiliser le mot-clé `revert` pour la réinitialiser. Dans ce cas, la valeur est réinitialisée à la valeur originale que le navigateur lui a donnée dans sa feuille de style par défaut.

En pratique, cela est rarement utilisé, et la plupart du temps vous définirez simplement une autre valeur pour la propriété afin de remplacer cette valeur héritée.

#### Autres valeurs spéciales

En plus des mots-clés spéciaux `inherit` et `revert` que nous venons de voir, vous pouvez également définir n'importe quelle propriété sur :

* `initial` : utilise la feuille de style par défaut du navigateur si disponible. Si ce n'est pas le cas, et si la propriété hérite par défaut, hérite de la valeur. Sinon, ne fait rien.
* `unset` : si la propriété hérite par défaut, hérite. Sinon, ne fait rien.

### IMPORT

À partir de n'importe quel fichier CSS, vous pouvez importer un autre fichier CSS en utilisant la directive `@import`.

Voici comment l'utiliser :

```css
@import url(myfile.css)
```

url() peut gérer des URL absolues ou relatives.

Une chose importante que vous devez savoir est que les directives `@import` doivent être placées avant tout autre CSS dans le fichier, sinon elles seront ignorées.

Vous pouvez utiliser des descripteurs de média pour ne charger un fichier CSS que sur le média spécifique :

```css
@import url(myfile.css) all;
@import url(myfile-screen.css) screen;
@import url(myfile-print.css) print;
```

### SÉLECTEURS D'ATTRIBUTS

Nous avons déjà introduit plusieurs des sélecteurs CSS de base : utiliser des sélecteurs d'éléments, de classe, d'id, comment les combiner, comment cibler plusieurs classes, comment styliser plusieurs sélecteurs dans la même règle, comment suivre la hiérarchie de la page avec les sélecteurs d'enfants et d'enfants directs, et les frères adjacents.

Dans cette section, nous allons analyser les sélecteurs d'attributs, et nous parlerons des sélecteurs de pseudo-classe et de pseudo-élément dans les 2 sections suivantes.

#### Sélecteurs de présence d'attribut

Le premier type de sélecteur est le sélecteur de présence d'attribut.

Nous pouvons vérifier si un élément **a** un attribut en utilisant la syntaxe `[]`. `p[id]` sélectionnera toutes les balises `p` dans la page qui ont un attribut `id`, quelle que soit sa valeur :

```css
p[id] {
  /* ... */
}
```

#### Sélecteurs de valeur exacte d'attribut

À l'intérieur des crochets, vous pouvez vérifier la valeur de l'attribut en utilisant `=`, et le CSS sera appliqué uniquement si l'attribut correspond à la valeur exacte spécifiée :

```css
p[id="my-id"] {
  /* ... */
}
```

#### Correspondre à une partie de la valeur de l'attribut

Alors que `=` nous permet de vérifier la valeur exacte, nous avons d'autres opérateurs :

* `*=` vérifie si l'attribut contient la partie
* `^=` vérifie si l'attribut commence par la partie
* `$=` vérifie si l'attribut se termine par la partie
* `|=` vérifie si l'attribut commence par la partie et est suivi d'un tiret (commun dans les classes, par exemple), ou contient simplement la partie
* `~=` vérifie si la partie est contenue dans l'attribut, mais séparée par des espaces du reste

Toutes les vérifications que nous avons mentionnées sont **sensibles à la casse**.

Si vous ajoutez un `i` juste avant le crochet fermant, la vérification sera insensible à la casse. Cela est pris en charge dans de nombreux navigateurs mais pas dans tous, vérifiez [https://caniuse.com/#feat=css-case-insensitive](https://caniuse.com/#feat=css-case-insensitive).

### PSEUDO-CLASSES

Les pseudo-classes sont des mots-clés prédéfinis qui sont utilisés pour sélectionner un élément en fonction de son **état**, ou pour cibler un enfant spécifique.

Elles commencent par un **double deux-points** `::`.

Elles peuvent être utilisées comme partie d'un sélecteur, et elles sont très utiles pour styliser des liens actifs ou visités, par exemple, changer le style au survol, au focus, ou cibler le premier enfant, ou les lignes impaires. Très pratique dans de nombreux cas.

Ce sont les pseudo-classes les plus populaires que vous utiliserez probablement :

![Image](https://cdn-media-1.freecodecamp.org/images/ACo1IxL9QFOQvDYkMigh3FXw717fjM2ChP3w)

Faisons un exemple. Un exemple courant, en fait. Vous voulez styliser un lien, alors vous créez une règle CSS pour cibler l'élément `a` :

```css
a {
  color: yellow;
}
```

Les choses semblent fonctionner correctement, jusqu'à ce que vous cliquiez sur un lien. Le lien revient à la couleur prédéfinie (bleu) lorsque vous cliquez dessus. Ensuite, lorsque vous ouvrez le lien et revenez à la page, le lien est maintenant bleu.

Pourquoi cela se produit-il ?

Parce que le lien, lorsqu'il est cliqué, change d'état et passe à l'état `:active`. Et lorsqu'il a été visité, il est dans l'état `:visited`. Pour toujours, jusqu'à ce que l'utilisateur efface l'historique de navigation.

Ainsi, pour faire en sorte que le lien soit jaune dans tous les états, vous devez écrire

```css
a,
a:visited,
a:active {
  color: yellow;
}
```

`:nth-child()` mérite une mention spéciale. Il peut être utilisé pour cibler les enfants impairs ou pairs avec `:nth-child(odd)` et `:nth-child(even)`.

Il est couramment utilisé dans les listes pour colorer les lignes impaires différemment des lignes paires :

```css
ul:nth-child(odd) {
  color: white;
    background-color: black;
}
```

Vous pouvez également l'utiliser pour cibler les 3 premiers enfants d'un élément avec `:nth-child(-n+3)`. Ou vous pouvez styliser 1 élément sur 5 avec `:nth-child(5n)`.

Certaines pseudo-classes ne sont utilisées que pour l'impression, comme `:first`, `:left`, `:right`, afin que vous puissiez cibler la première page, toutes les pages de gauche, et toutes les pages de droite, qui sont généralement stylisées légèrement différemment.

### PSEUDO-ÉLÉMENTS

#### Les pseudo-éléments sont utilisés pour styliser une partie spécifique d'un élément.

Ils commencent par un double deux-points `::`.

> _Parfois, vous les verrez dans la nature avec un seul deux-points, mais ce n'est qu'une syntaxe prise en charge pour des raisons de compatibilité ascendante. Vous devriez utiliser deux deux-points pour les distinguer des pseudo-classes._

`::before` et `::after` sont probablement les pseudo-éléments les plus utilisés. Ils sont utilisés pour ajouter du contenu avant ou après un élément, comme des icônes par exemple.

Voici la liste des pseudo-éléments :

![Image](https://cdn-media-1.freecodecamp.org/images/9FIuV0uCcudGyplaJcgQAEqK7sTSwhRCIZYd)

Faisons un exemple. Supposons que vous voulez rendre la première ligne d'un paragraphe légèrement plus grande en taille de police, une chose courante en typographie :

```css
p::first-line {
  font-size: 2rem;
}
```

Ou peut-être voulez-vous que la première lettre soit plus grasse :

```css
p::first-letter {
  font-weight: bolder;
}
```

`::after` et `::before` sont un peu moins intuitifs. Je me souviens les avoir utilisés lorsque je devais ajouter des icônes en utilisant CSS.

Vous spécifiez la propriété `content` pour insérer n'importe quel type de contenu après ou avant un élément :

```css
p::before {
  content: url(/myimage.png);
}

.myElement::before {
    content: "Hey Hey!";
}
```

### COULEURS

Par défaut, une page HTML est rendue par les navigateurs web de manière assez triste en termes de couleurs utilisées.

Nous avons un fond blanc, une couleur noire et des liens bleus. C'est tout.

Heureusement, CSS nous donne la possibilité d'ajouter des couleurs à nos designs.

Nous avons ces propriétés :

* `color`
* `background-color`
* `border-color`

Elles acceptent toutes une **valeur de couleur**, qui peut être sous différentes formes.

#### Couleurs nommées

Tout d'abord, nous avons des mots-clés CSS qui définissent des couleurs. CSS a commencé avec 16, mais aujourd'hui il y a un grand nombre de noms de couleurs :

* `aliceblue`
* `antiquewhite`
* `aqua`
* `aquamarine`
* `azure`
* `beige`
* `bisque`
* `black`
* `blanchedalmond`
* `blue`
* `blueviolet`
* `brown`
* `burlywood`
* `cadetblue`
* `chartreuse`
* `chocolate`
* `coral`
* `cornflowerblue`
* `cornsilk`
* `crimson`
* `cyan`
* `darkblue`
* `darkcyan`
* `darkgoldenrod`
* `darkgray`
* `darkgreen`
* `darkgrey`
* `darkkhaki`
* `darkmagenta`
* `darkolivegreen`
* `darkorange`
* `darkorchid`
* `darkred`
* `darksalmon`
* `darkseagreen`
* `darkslateblue`
* `darkslategray`
* `darkslategrey`
* `darkturquoise`
* `darkviolet`
* `deeppink`
* `deepskyblue`
* `dimgray`
* `dimgrey`
* `dodgerblue`
* `firebrick`
* `floralwhite`
* `forestgreen`
* `fuchsia`
* `gainsboro`
* `ghostwhite`
* `gold`
* `goldenrod`
* `gray`
* `green`
* `greenyellow`
* `grey`
* `honeydew`
* `hotpink`
* `indianred`
* `indigo`
* `ivory`
* `khaki`
* `lavender`
* `lavenderblush`
* `lawngreen`
* `lemonchiffon`
* `lightblue`
* `lightcoral`
* `lightcyan`
* `lightgoldenrodyellow`
* `lightgray`
* `lightgreen`
* `lightgrey`
* `lightpink`
* `lightsalmon`
* `lightseagreen`
* `lightskyblue`
* `lightslategray`
* `lightslategrey`
* `lightsteelblue`
* `lightyellow`
* `lime`
* `limegreen`
* `linen`
* `magenta`
* `maroon`
* `mediumaquamarine`
* `mediumblue`
* `mediumorchid`
* `mediumpurple`
* `mediumseagreen`
* `mediumslateblue`
* `mediumspringgreen`
* `mediumturquoise`
* `mediumvioletred`
* `midnightblue`
* `mintcream`
* `mistyrose`
* `moccasin`
* `navajowhite`
* `navy`
* `oldlace`
* `olive`
* `olivedrab`
* `orange`
* `orangered`
* `orchid`
* `palegoldenrod`
* `palegreen`
* `paleturquoise`
* `palevioletred`
* `papayawhip`
* `peachpuff`
* `peru`
* `pink`
* `plum`
* `powderblue`
* `purple`
* `rebeccapurple`
* `red`
* `rosybrown`
* `royalblue`
* `saddlebrown`
* `salmon`
* `sandybrown`
* `seagreen`
* `seashell`
* `sienna`
* `silver`
* `skyblue`
* `slateblue`
* `slategray`
* `slategrey`
* `snow`
* `springgreen`
* `steelblue`
* `tan`
* `teal`
* `thistle`
* `tomato`
* `turquoise`
* `violet`
* `wheat`
* `white`
* `whitesmoke`
* `yellow`
* `yellowgreen`

plus `transparent`, et `currentColor` qui pointe vers la propriété `color`, par exemple, il est utile pour faire hériter le `border-color` de celle-ci.

Ils sont définis dans le [Module de Couleur CSS, Niveau 4](https://www.w3.org/TR/css-color-4/). Ils sont insensibles à la casse.

Wikipedia a un [tableau pratique](https://en.wikipedia.org/wiki/Web_colors) qui vous permet de choisir la couleur parfaite par son nom.

Les couleurs nommées ne sont pas la seule option.

### RGB et RGBa

Vous pouvez utiliser la fonction `rgb()` pour calculer une couleur à partir de sa notation RGB, qui définit la couleur en fonction de ses parties rouge-vert-bleu. De 0 à 255 :

```css
p {
  color: rgb(255, 255, 255); /* blanc */
    background-color: rgb(0, 0, 0); /* noir */
}
```

`rgba()` vous permet d'ajouter le canal alpha pour entrer une partie transparente. Cela peut être un nombre de 0 à 1 :

```css
p {
    background-color: rgb(0, 0, 0, 0.5);
}
```

#### Notation hexadécimale

Une autre option est d'exprimer les parties RGB des couleurs en notation hexadécimale, qui est composée de 3 blocs.

Le noir, qui est `rgb(0,0,0)` est exprimé comme `#000000` ou `#000` (nous pouvons raccourcir les 2 chiffres à 1 s'ils sont égaux).

Le blanc, `rgb(255,255,255)` peut être exprimé comme `#ffffff` ou `#fff`.

La notation hexadécimale nous permet d'exprimer un nombre de 0 à 255 en seulement 2 chiffres, puisque ils peuvent aller de 0 à "15" (f).

Nous pouvons ajouter le canal alpha en ajoutant 1 ou 2 chiffres de plus à la fin, par exemple `#00000033`. Tous les navigateurs ne supportent pas la notation raccourcie, donc utilisez tous les 6 chiffres pour exprimer la partie RGB.

#### HSL et HSLa

C'est une addition plus récente à CSS.

HSL = Teinte Saturation Luminosité.

Dans cette notation, le noir est `hsl(0, 0%, 0%)` et le blanc est `hsl(0, 0%, 100%)`.

Si vous êtes plus familier avec HSL qu'avec RGB grâce à vos connaissances passées, vous pouvez définitivement utiliser cela.

Vous avez également `hsla()` qui ajoute le canal alpha au mélange, encore une fois un nombre de 0 à 1 : `hsl(0, 0%, 0%, 0.5)`

### UNITÉS

L'une des choses que vous utiliserez tous les jours en CSS sont les unités. Elles sont utilisées pour définir les longueurs, les remplissages, les marges, aligner les éléments et ainsi de suite.

Des choses comme `px`, `em`, `rem`, ou des pourcentages.

Elles sont partout. Il y en a aussi des obscures. Nous allons passer en revue chacune d'elles dans cette section.

#### Pixels

L'unité de mesure la plus largement utilisée. Un pixel ne correspond pas réellement à un pixel physique sur votre écran, car cela varie, beaucoup, selon l'appareil (pensez aux appareils à haute DPI par rapport aux appareils non rétina).

Il existe une convention qui fait fonctionner cette unité de manière cohérente sur tous les appareils.

#### Pourcentages

Une autre mesure très utile, les pourcentages vous permettent de spécifier des valeurs en pourcentages de la propriété correspondante de l'élément parent.

Exemple :

```css
.parent {
  width: 400px;
}

.child {
  width: 50%; /* = 200px */
}
```

#### Unités de mesure du monde réel

Nous avons ces unités de mesure qui sont traduites du monde extérieur. Principalement inutiles à l'écran, elles peuvent être utiles pour les feuilles de style d'impression. Elles sont :

* `cm` un centimètre (correspond à 37,8 pixels)
* `mm` un millimètre (0,1 cm)
* `q` un quart de millimètre
* `in` un pouce (correspond à 96 pixels)
* `pt` un point (1 pouce = 72 points)
* `pc` un pica (1 pica = 12 points)

#### Unités relatives

* `em` est la valeur assignée à la `font-size` de cet élément, donc sa valeur exacte change entre les éléments. Elle ne change pas en fonction de la police utilisée, seulement en fonction de la taille de la police. En typographie, cela mesure la largeur de la lettre `m`.
* `rem` est similaire à `em`, mais au lieu de varier en fonction de la taille de la police de l'élément actuel, il utilise la taille de la police de l'élément racine (`html`). Vous définissez cette taille de police une fois, et `rem` sera une mesure cohérente sur toute la page.
* `ex` est comme `em`, mais au lieu de mesurer la largeur de `m`, il mesure la hauteur de la lettre `x`. Il peut changer en fonction de la police utilisée, et de la taille de la police.
* `ch` est comme `ex` mais au lieu de mesurer la hauteur de `x`, il mesure la largeur de `0` (zéro).

#### Unités de viewport

* `vw` l'**unité de largeur de viewport** représente un pourcentage de la largeur de viewport. `50vw` signifie 50 % de la largeur de viewport.
* `vh` l'**unité de hauteur de viewport** représente un pourcentage de la hauteur de viewport. `50vh` signifie 50 % de la hauteur de viewport.
* `vmin` l'**unité de minimum de viewport** représente le minimum entre la hauteur ou la largeur en termes de pourcentage. `30vmin` est 30 % de la largeur ou de la hauteur actuelle, selon celle qui est la plus petite.
* `vmax` l'**unité de maximum de viewport** représente le maximum entre la hauteur ou la largeur en termes de pourcentage. `30vmax` est 30 % de la largeur ou de la hauteur actuelle, selon celle qui est la plus grande.

#### Unités de fraction

`fr` sont des unités de fraction, et elles sont utilisées dans CSS Grid pour diviser l'espace en fractions.

Nous en parlerons dans le contexte de CSS Grid plus tard.

### URL

Lorsque nous parlons d'images de fond, `@import`, et plus encore, nous utilisons la fonction `url()` pour charger une ressource :

```css
div {
  background-image: url(test.png);
}
```

Dans ce cas, j'ai utilisé une URL relative, qui recherche le fichier dans le dossier où le fichier CSS est défini.

Je pourrais remonter d'un niveau

```css
div {
  background-image: url(../test.png);
}
```

ou aller dans un dossier

```css
div {
  background-image: url(subfolder/test.png);
}
```

Ou je pourrais charger un fichier à partir de la racine du domaine où le CSS est hébergé :

```css
div {
  background-image: url(/test.png);
}
```

Ou je pourrais utiliser une URL absolue pour charger une ressource externe :

```css
div {
  background-image: url(https://mysite.com/test.png);
}
```

### CALC

La fonction `calc()` vous permet d'effectuer des opérations mathématiques de base sur des valeurs, et elle est particulièrement utile lorsque vous devez ajouter ou soustraire une valeur de longueur à un pourcentage.

Voici comment cela fonctionne :

```css
div {
    max-width: calc(80% - 100px)
}
```

Elle retourne une valeur de longueur, donc elle peut être utilisée partout où vous attendez une valeur en pixels.

Vous pouvez effectuer

* des additions en utilisant `+`
* des soustractions en utilisant `-`
* des multiplications en utilisant `*`
* des divisions en utilisant `/`

> _Un avertissement : avec l'addition et la soustraction, l'espace autour de l'opérateur est obligatoire, sinon cela ne fonctionne pas comme prévu._

Exemples :

```css
div {
    max-width: calc(50% / 3)
}

div {
    max-width: calc(50% + 3px)
}
```

### ARRIÈRE-PLANS

L'arrière-plan d'un élément peut être modifié en utilisant plusieurs propriétés CSS :

* `background-color`
* `background-image`
* `background-clip`
* `background-position`
* `background-origin`
* `background-repeat`
* `background-attachment`
* `background-size`

et la propriété raccourcie `background`, qui nous permet de raccourcir les définitions et de les regrouper sur une seule ligne.

`background-color` accepte une valeur de couleur, qui peut être l'un des mots-clés de couleur, ou une valeur `rgb` ou `hsl` :

```css
p {
  background-color: yellow;
}

div {
  background-color: #333;
}
```

Au lieu d'utiliser une couleur, vous pouvez utiliser une image comme arrière-plan d'un élément, en spécifiant l'URL de l'emplacement de l'image :

```css
div {
  background-image: url(image.png);
}
```

`background-clip` vous permet de déterminer la zone utilisée par l'image ou la couleur d'arrière-plan. La valeur par défaut est `border-box`, qui s'étend jusqu'au bord extérieur de la bordure.

D'autres valeurs sont

* `padding-box` pour étendre l'arrière-plan jusqu'au bord du remplissage, sans la bordure
* `content-box` pour étendre l'arrière-plan jusqu'au bord du contenu, sans le remplissage
* `inherit` pour appliquer la valeur du parent

Lorsque vous utilisez une image comme arrière-plan, vous voudrez définir la position du placement de l'image en utilisant la propriété `background-position` : `left`, `right`, `center` sont toutes des valeurs valides pour l'axe X, et `top`, `bottom` pour l'axe Y :

```css
div {
  background-position: top right;
}
```

Si l'image est plus petite que l'arrière-plan, vous devez définir le comportement en utilisant `background-repeat`. Doit-elle se répéter sur l'axe `x`, `y` ou sur tous les axes ? Cette dernière est la valeur par défaut. Une autre valeur est `no-repeat`.

`background-origin` vous permet de choisir où l'arrière-plan doit être appliqué : à l'élément entier y compris le remplissage (par défaut) en utilisant `padding-box`, à l'élément entier y compris la bordure en utilisant `border-box`, à l'élément sans le remplissage en utilisant `content-box`.

Avec `background-attachment`, nous pouvons attacher l'arrière-plan au viewport, de sorte que le défilement n'affectera pas l'arrière-plan :

```css
div {
  background-attachment: fixed;
}
```

Par défaut, la valeur est `scroll`. Il y a une autre valeur, `local`. La meilleure façon de visualiser leur comportement est [ce Codepen](https://codepen.io/BernLeech/pen/mMNKJV).

La dernière propriété d'arrière-plan est `background-size`. Nous pouvons utiliser 3 mots-clés : `auto`, `cover` et `contain`. `auto` est la valeur par défaut.

`cover` étend l'image jusqu'à ce que l'élément entier soit couvert par l'arrière-plan.

`contain` arrête l'extension de l'image d'arrière-plan lorsqu'une dimension (x ou y) couvre le bord le plus petit de l'image, de sorte qu'elle soit entièrement contenue dans l'élément.

Vous pouvez également spécifier une valeur de longueur, et si vous le faites, elle définit la largeur de l'image d'arrière-plan (et la hauteur est automatiquement définie) :

```css
div {
  background-size: 100%;
}
```

Si vous spécifiez 2 valeurs, l'une est la largeur et la seconde est la hauteur :

```css
div {
  background-size: 800px 600px;
}
```

La propriété raccourcie `background` permet de raccourcir les définitions et de les regrouper sur une seule ligne.

Voici un exemple :

```css
div {
  background: url(bg.png) top left no-repeat;
}
```

Si vous utilisez une image, et que l'image ne peut pas être chargée, vous pouvez définir une couleur de repli :

```css
div {
  background: url(image.png) yellow;
}
```

Vous pouvez également définir un dégradé comme arrière-plan :

```css
div {
  background: linear-gradient(#fff, #333);
}
```

### COMMENTAIRES

CSS vous donne la possibilité d'écrire des commentaires dans un fichier CSS, ou dans la balise `style` dans l'en-tête de la page

Le format est le commentaire de style C `/* ceci est un commentaire */` (ou de style JavaScript, si vous préférez).

Ceci est un commentaire sur plusieurs lignes. Jusqu'à ce que vous ajoutiez le jeton de fermeture `*/`, toutes les lignes trouvées après l'ouverture sont commentées.

Exemple :

```css
#name { display: block; } /* Belle règle ! */

/* #name { display: block; } */

#name {
    display: block; /*
    color: red;
    */
}
```

CSS n'a pas de commentaires en ligne, comme `//` en C ou JavaScript.

Faites attention cependant — si vous ajoutez `//` avant une règle, la règle ne sera pas appliquée, comme si le commentaire avait fonctionné. En réalité, CSS a détecté une erreur de syntaxe et, en raison de son fonctionnement, il a ignoré la ligne avec l'erreur et est passé directement à la ligne suivante.

Connaître cette approche vous permet d'écrire intentionnellement des commentaires en ligne, bien que vous deviez être prudent car vous ne pouvez pas ajouter de texte aléatoire comme vous pouvez le faire dans un commentaire de bloc.

Par exemple :

```css
// Belle règle !
#name { display: block; }
```

Dans ce cas, en raison du fonctionnement de CSS, la règle `#name` est en réalité commentée. Vous pouvez trouver plus de détails [ici](https://www.xanthir.com/b4U10) si vous trouvez cela intéressant. Pour éviter de vous tirer une balle dans le pied, évitez simplement d'utiliser des commentaires en ligne et reposez-vous sur des commentaires de bloc.

### PROPRIÉTÉS PERSONNALISÉES

Ces dernières années, les préprocesseurs CSS ont connu un grand succès. Il était très courant pour les projets greenfield de commencer avec Less ou Sass. Et c'est toujours une technologie très populaire.

Les principaux avantages de ces technologies sont, à mon avis :

* Ils permettent d'imbriquer des sélecteurs
* Ils fournissent une fonctionnalité d'importation facile
* Ils offrent des variables

Le CSS moderne dispose d'une nouvelle fonctionnalité puissante appelée **Propriétés Personnalisées CSS**, également communément connues sous le nom de **Variables CSS**.

CSS n'est pas un langage de programmation comme [JavaScript](https://flaviocopes.com/javascript/), Python, PHP, Ruby ou Go où les variables sont essentielles pour faire quelque chose d'utile. CSS est très limité dans ce qu'il peut faire, et c'est principalement une syntaxe déclarative pour dire aux navigateurs comment ils doivent afficher une page HTML.

Mais une variable est une variable : un nom qui fait référence à une valeur, et les variables en CSS aident à réduire la répétition et les incohérences dans votre CSS, en centralisant la définition des valeurs.

Et cela introduit une fonctionnalité unique que les préprocesseurs CSS n'auront jamais : **vous pouvez accéder et modifier la valeur d'une Variable CSS de manière programmatique en utilisant JavaScript**.

#### Les bases de l'utilisation des variables

Une Variable CSS est définie avec une syntaxe spéciale, en préfixant **deux tirets** à un nom (`--variable-name`), puis un deux-points et une valeur. Comme ceci :

```css
:root {
  --primary-color: yellow;
}
```

(plus d'informations sur `:root` plus tard)

Vous pouvez accéder à la valeur de la variable en utilisant `var()` :

```css
p {
  color: var(--primary-color)
}
```

La valeur de la variable peut être n'importe quelle valeur CSS valide, par exemple :

```css
:root {
  --default-padding: 30px 30px 20px 20px;
  --default-color: red;
  --default-background: #fff;
}
```

#### Créer des variables à l'intérieur de n'importe quel élément

Les Variables CSS peuvent être définies à l'intérieur de n'importe quel élément. Voici quelques exemples :

```css
:root {
  --default-color: red;
}

body {
  --default-color: red;
}

main {
  --default-color: red;
}

p {
  --default-color: red;
}

span {
  --default-color: red;
}

a:hover {
  --default-color: red;
}
```

Ce qui change dans ces différents exemples, c'est la **portée**.

#### Portée des variables

L'ajout de variables à un sélecteur les rend disponibles pour tous les enfants de celui-ci.

Dans l'exemple ci-dessus, vous avez vu l'utilisation de `:root` lors de la définition d'une variable CSS :

```css
:root {
  --primary-color: yellow;
}
```

`:root` est une pseudo-classe CSS qui identifie l'élément racine d'un arbre.

Dans le contexte d'un document HTML, l'utilisation du sélecteur `:root` pointe vers l'élément `html`, sauf que `:root` a une spécificité plus élevée (prend la priorité).

Dans le contexte d'une image SVG, `:root` pointe vers la balise `svg`.

L'ajout d'une propriété personnalisée CSS à `:root` la rend disponible pour tous les éléments de la page.

Si vous ajoutez une variable à l'intérieur d'un sélecteur `.container`, elle ne sera disponible que pour les enfants de `.container` :

```css
.container {
  --secondary-color: yellow;
}
```

et l'utiliser en dehors de cet élément ne fonctionnera pas.

Les variables peuvent être **réassignées** :

```css
:root {
  --primary-color: yellow;
}

.container {
  --primary-color: blue;
}
```

En dehors de `.container`, `--primary-color` sera _jaune_, mais à l'intérieur, il sera _bleu_.

Vous pouvez également assigner ou écraser une variable à l'intérieur du HTML en utilisant **des styles en ligne** :

```html
<main style="--primary-color: orange;">
  <!-- ... -->
</main>
```

> _Les Variables CSS suivent les règles normales de cascade CSS, avec la priorité définie selon la spécificité._

#### Interagir avec une valeur de Variable CSS en utilisant JavaScript

La chose la plus cool avec les Variables CSS est la capacité à accéder et à les modifier en utilisant JavaScript.

Voici comment définir une valeur de variable en utilisant JavaScript simple :

```js
const element = document.getElementById('my-element')
element.style.setProperty('--variable-name', 'a-value')
```

Ce code ci-dessous peut être utilisé pour accéder à une valeur de variable à la place, au cas où la variable est définie sur `:root` :

```js
const styles = getComputedStyle(document.documentElement)
const value = String(styles.getPropertyValue('--variable-name')).trim()
```

Ou, pour obtenir le style appliqué à un élément spécifique, dans le cas de variables définies avec une portée différente :

```js
const element = document.getElementById('my-element')
const styles = getComputedStyle(element)
const value = String(styles.getPropertyValue('--variable-name')).trim()
```

#### Gestion des valeurs invalides

Si une variable est assignée à une propriété qui n'accepte pas la valeur de la variable, elle est considérée comme invalide.

Par exemple, vous pourriez passer une valeur de pixel à une propriété `position`, ou une valeur rem à une propriété de couleur.

Dans ce cas, la ligne est considérée comme invalide et est ignorée.

#### Support des navigateurs

Le support des navigateurs pour les Variables CSS est **très bon**, [selon Can I Use](https://www.caniuse.com/#feat=css-variables).

Les Variables CSS sont là pour rester, et vous pouvez les utiliser aujourd'hui si vous n'avez pas besoin de supporter Internet Explorer et les anciennes versions des autres navigateurs.

Si vous devez supporter des navigateurs plus anciens, vous pouvez utiliser des bibliothèques comme [PostCSS](https://flaviocopes.com/postcss/) ou [Myth](http://www.myth.io/), mais vous perdrez la capacité d'interagir avec les variables via JavaScript ou les Outils de Développement du Navigateur, car elles sont transpilées en bon vieux CSS sans variables (et donc, vous perdez la plupart de la puissance des Variables CSS).

#### Les Variables CSS sont sensibles à la casse

Cette variable :

```css
--width: 100px;
```

est différente de celle-ci :

```css
--Width: 100px;
```

#### Mathématiques dans les Variables CSS

Pour faire des mathématiques dans les Variables CSS, vous devez utiliser `calc()`, par exemple :

```css
:root {
  --default-left-padding: calc(10px * 2);
}
```

#### Requêtes média avec Variables CSS

Rien de spécial ici. Les Variables CSS s'appliquent normalement aux requêtes média :

```css
body {
  --width: 500px;
}

@media screen and (max-width: 1000px) and (min-width: 700px) {
  --width: 800px;
}

.container {
  width: var(--width);
}
```

#### Définir une valeur de repli pour var()

`var()` accepte un deuxième paramètre, qui est la valeur de repli par défaut lorsque la valeur de la variable n'est pas définie :

```css
.container {
  margin: var(--default-margin, 30px);
}
```

### POLICES

À l'aube du web, vous n'aviez qu'une poignée de polices parmi lesquelles choisir.

Heureusement, aujourd'hui vous pouvez charger n'importe quel type de police sur vos pages.

CSS a gagné de nombreuses capacités intéressantes au fil des ans en ce qui concerne les polices.

La propriété `font` est le raccourci pour un certain nombre de propriétés :

* `font-family`
* `font-weight`
* `font-stretch`
* `font-style`
* `font-size`

Voyons chacune d'elles et ensuite nous couvrirons `font`.

Ensuite, nous parlerons de la façon de charger des polices personnalisées, en utilisant `@import` ou `@font-face`, ou en chargeant une feuille de style de police.

#### `font-family`

Définit la _famille_ de polices que l'élément utilisera.

Pourquoi « famille » ? Parce que ce que nous connaissons comme une police est en fait composée de plusieurs sous-polices qui fournissent tous les styles (gras, italique, léger, etc.) dont nous avons besoin.

Voici un exemple de l'application Font Book de mon Mac — la famille de polices Fira Code héberge plusieurs polices dédiées en dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/3eSWEQuM-orkdVa7xATJ5p9sH2Te-clkilVI)

Cette propriété vous permet de sélectionner une police spécifique, par exemple :

```css
body {
  font-family: Helvetica;
}
```

Vous pouvez définir plusieurs valeurs, afin que la deuxième option soit utilisée si la première ne peut pas être utilisée pour une raison quelconque (si elle n'est pas trouvée sur la machine, ou si la connexion réseau pour télécharger la police a échoué, par exemple) :

```css
body {
  font-family: Helvetica, Arial;
}
```

J'ai utilisé certaines polices spécifiques jusqu'à présent, que nous appelons **Polices Sûres pour le Web**, car elles sont préinstallées sur différents systèmes d'exploitation.

Nous les divisons en polices Serif, Sans-Serif et Monospace. Voici une liste de certaines des plus populaires :

**Serif**

* Georgia
* Palatino
* Times New Roman
* Times

**Sans-Serif**

* Arial
* Helvetica
* Verdana
* Geneva
* Tahoma
* Lucida Grande
* Impact
* Trebuchet MS
* Arial Black

**Monospace**

* Courier New
* Courier
* Lucida Console
* Monaco

Vous pouvez utiliser toutes celles-ci comme propriétés `font-family`, mais elles ne sont pas garanties d'être présentes pour chaque système. D'autres existent également, avec un niveau de support variable.

Vous pouvez également utiliser des noms génériques :

* `sans-serif` une police sans ligatures
* `serif` une police avec ligatures
* `monospace` une police particulièrement adaptée au code
* `cursive` utilisée pour simuler des pièces manuscrites
* `fantasy` le nom dit tout

Celles-ci sont généralement utilisées à la fin d'une définition `font-family`, pour fournir une valeur de repli au cas où rien d'autre ne peut être appliqué :

```css
body {
  font-family: Helvetica, Arial, sans-serif;
}
```

#### `font-weight`

Cette propriété définit la largeur d'une police. Vous pouvez utiliser ces valeurs prédéfinies :

* normal
* bold
* bolder (relatif à l'élément parent)
* lighter (relatif à l'élément parent)

Ou en utilisant les mots-clés numériques

* 100
* 200
* 300
* 400, mappé à `normal`
* 500
* 600
* 700 mappé à `bold`
* 800
* 900

où 100 est la police la plus légère, et 900 est la plus grasse.

Certaines de ces valeurs numériques peuvent ne pas correspondre à une police, car celle-ci doit être fournie dans la famille de polices. Lorsqu'une valeur est manquante, CSS fait en sorte que ce nombre soit au moins aussi gras que le précédent, donc vous pouvez avoir des nombres qui pointent vers la même police.

#### `font-stretch`

Permet de choisir une face étroite ou large de la police, si disponible.

C'est important : la police doit être équipée de différentes faces.

Les valeurs autorisées sont, de la plus étroite à la plus large :

* `ultra-condensed`
* `extra-condensed`
* `condensed`
* `semi-condensed`
* `normal`
* `semi-expanded`
* `expanded`
* `extra-expanded`
* `ultra-expanded`

#### `font-style`

Permet d'appliquer un style italique à une police :

```css
p {
  font-style: italic;
}
```

Cette propriété permet également les valeurs `oblique` et `normal`. Il y a très peu, voire aucune, différence entre l'utilisation de `italic` et `oblique`. Le premier est plus facile pour moi, car HTML offre déjà un élément `i` qui signifie italique.

#### `font-size`

Cette propriété est utilisée pour déterminer la taille des polices.

Vous pouvez passer 2 types de valeurs :

1. une valeur de longueur, comme `px`, `em`, `rem` etc, ou un pourcentage
2. un mot-clé de valeur prédéfinie

Dans le second cas, les valeurs que vous pouvez utiliser sont :

* xx-small
* x-small
* small
* medium
* large
* x-large
* xx-large
* smaller (relatif à l'élément parent)
* larger (relatif à l'élément parent)

Utilisation :

```css
p {
  font-size: 20px;
}

li {
  font-size: medium;
}
```

#### `font-variant`

Cette propriété était à l'origine utilisée pour changer le texte en petites capitales, et elle n'avait que 3 valeurs valides :

* `normal`
* `inherit`
* `small-caps`

Les petites capitales signifient que le texte est rendu en « capitales plus petites » à côté de ses lettres majuscules.

#### `font`

La propriété `font` vous permet d'appliquer différentes propriétés de police en une seule, réduisant ainsi l'encombrement.

Nous devons au moins définir 2 propriétés, `font-size` et `font-family`, les autres sont facultatives :

```css
body {
  font: 20px Helvetica;
}
```

Si nous ajoutons d'autres propriétés, elles doivent être placées dans le bon ordre.

Voici l'ordre :

```css
font: <font-stretch> <font-style> <font-variant> <font-weight> <font-size> <line-height> <font-family>;
```

Exemple :

```css
body {
  font: italic bold 20px Helvetica;
}

section {
  font: small-caps bold 20px Helvetica;
}
```

#### Chargement de polices personnalisées avec `@font-face`

`@font-face` vous permet d'ajouter un nouveau nom de famille de polices, et de le mapper à un fichier qui contient une police.

Cette police sera téléchargée par le navigateur et utilisée dans la page, et cela a été un changement fondamental pour la typographie sur le web — nous pouvons maintenant utiliser n'importe quelle police que nous voulons.

Nous pouvons ajouter des déclarations `@font-face` directement dans notre CSS, ou lier à un CSS dédié à l'importation de la police.

Dans notre fichier CSS, nous pouvons également utiliser `@import` pour charger ce fichier CSS.

Une déclaration `@font-face` contient plusieurs propriétés que nous utilisons pour définir la police, y compris `src`, l'URI (un ou plusieurs URI) vers la police. Cela suit la politique de même origine, ce qui signifie que les polices ne peuvent être téléchargées que depuis l'origine actuelle (domaine + port + protocole).

Les polices sont généralement dans les formats

* `woff` (Web Open Font Format)
* `woff2` (Web Open Font Format 2.0)
* `eot` (Embedded Open Type)
* `otf` (OpenType Font)
* `ttf` (TrueType Font)

Les propriétés suivantes nous permettent de définir les propriétés de la police que nous allons charger, comme nous l'avons vu ci-dessus :

* `font-family`
* `font-weight`
* `font-style`
* `font-stretch`

#### Une note sur la performance

Bien sûr, le chargement d'une police a des implications sur les performances que vous devez prendre en compte lors de la création du design de votre page.

### TYPOGRAPHIE

Nous avons déjà parlé des polices, mais il y a plus à dire sur la mise en forme du texte.

Dans cette section, nous parlerons des propriétés suivantes :

* `text-transform`
* `text-decoration`
* `text-align`
* `vertical-align`
* `line-height`
* `text-indent`
* `text-align-last`
* `word-spacing`
* `letter-spacing`
* `text-shadow`
* `white-space`
* `tab-size`
* `writing-mode`
* `hyphens`
* `text-orientation`
* `direction`
* `line-break`
* `word-break`
* `overflow-wrap`

#### `text-transform`

Cette propriété peut transformer la casse d'un élément.

Il y a 4 valeurs valides :

* `capitalize` pour mettre en majuscule la première lettre de chaque mot
* `uppercase` pour mettre en majuscule tout le texte
* `lowercase` pour mettre en minuscule tout le texte
* `none` pour désactiver la transformation du texte, utilisé pour éviter d'hériter de la propriété

Exemple :

```css
p {
  text-transform: uppercase;
}
```

#### `text-decoration`

Cette propriété ajoute des décorations au texte, y compris

* `underline`
* `overline`
* `line-through`
* `blink`
* `none`

Exemple :

```css
p {
  text-decoration: underline;
}
```

Vous pouvez également définir le style de la décoration, et la couleur.

Exemple :

```css
p {
  text-decoration: underline dashed yellow;
}
```

Les valeurs de style valides sont `solid`, `double`, `dotted`, `dashed`, `wavy`.

Vous pouvez tout faire en une seule ligne, ou utiliser les propriétés spécifiques :

* `text-decoration-line`
* `text-decoration-color`
* `text-decoration-style`

Exemple :

```css
p {
  text-decoration-line: underline;
  text-decoration-color: yellow;
  text-decoration-style: dashed;
}
```

#### `text-align`

Par défaut, l'alignement du texte a la valeur `start`, ce qui signifie que le texte commence au « début », à l'origine 0, 0 de la boîte qui le contient. Cela signifie en haut à gauche dans les langues de gauche à droite, et en haut à droite dans les langues de droite à gauche.

Les valeurs possibles sont `start`, `end`, `left`, `right`, `center`, `justify` (bien d'avoir un espacement cohérent aux extrémités de la ligne) :

```css
p {
  text-align: right;
}
```

#### `vertical-align`

Détermine comment les éléments en ligne sont alignés verticalement.

Nous avons plusieurs valeurs pour cette propriété. Tout d'abord, nous pouvons assigner une valeur de longueur ou de pourcentage. Celles-ci sont utilisées pour aligner le texte dans une position plus haute ou plus basse (en utilisant des valeurs négatives) que la ligne de base de l'élément parent.

Ensuite, nous avons les mots-clés :

* `baseline` (par défaut), aligne la ligne de base à la ligne de base de l'élément parent
* `sub` rend un élément en indice, simulant le résultat de l'élément HTML `sub`
* `super` rend un élément en exposant, simulant le résultat de l'élément HTML `sup`
* `top` aligne le haut de l'élément au haut de la ligne
* `text-top` aligne le haut de l'élément au haut de la police de l'élément parent
* `middle` aligne le milieu de l'élément au milieu de la ligne de l'élément parent
* `bottom` aligne le bas de l'élément au bas de la ligne
* `text-bottom` aligne le bas de l'élément au bas de la police de l'élément parent

#### `line-height`

Cela vous permet de changer la hauteur d'une ligne. Chaque ligne de texte a une certaine hauteur de police, mais il y a un espacement vertical supplémentaire entre les lignes. C'est la hauteur de ligne :

```css
p {
  line-height: 0.9rem;
}
```

#### `text-indent`

Indente la première ligne d'un paragraphe d'une longueur définie, ou d'un pourcentage de la largeur du paragraphe :

```css
p {
  text-indent: -10px;
}
```

#### `text-align-last`

Par défaut, la dernière ligne d'un paragraphe est alignée en suivant la valeur de `text-align`. Utilisez cette propriété pour changer ce comportement :

```css
p {
  text-align-last: right;
}
```

#### `word-spacing`

Modifie l'espacement entre chaque mot.

Vous pouvez utiliser le mot-clé `normal`, pour réinitialiser les valeurs héritées, ou utiliser une valeur de longueur :

```css
p {
  word-spacing: 2px;
}

span {
  word-spacing: -0.2em;
}
```

#### `letter-spacing`

Modifie l'espacement entre chaque lettre.

Vous pouvez utiliser le mot-clé `normal`, pour réinitialiser les valeurs héritées, ou utiliser une valeur de longueur :

```css
p {
  letter-spacing: 0.2px;
}

span {
  letter-spacing: -0.2em;
}
```

#### `text-shadow`

Applique une ombre au texte. Par défaut, le texte n'a pas d'ombre.

Cette propriété accepte une couleur facultative, et un ensemble de valeurs qui définissent

* le décalage X de l'ombre par rapport au texte
* le décalage Y de l'ombre par rapport au texte
* le rayon de flou

Si la couleur n'est pas spécifiée, l'ombre utilisera la couleur du texte.

Exemples :

```css
p {
  text-shadow: 0.2px 2px;
}

span {
  text-shadow: yellow 0.2px 2px 3px;
}
```

#### `white-space`

Détermine comment CSS gère les espaces blancs, les nouvelles lignes et les tabulations à l'intérieur d'un élément.

Les valeurs valides qui réduisent les espaces blancs sont :

* `normal` réduit les espaces blancs. Ajoute de nouvelles lignes lorsque nécessaire lorsque le texte atteint la fin du conteneur
* `nowrap` réduit les espaces blancs. N'ajoute pas de nouvelle ligne lorsque le texte atteint la fin du conteneur, et supprime tout saut de ligne ajouté au texte
* `pre-line` réduit les espaces blancs. Ajoute de nouvelles lignes lorsque nécessaire lorsque le texte atteint la fin du conteneur

Les valeurs valides qui préservent les espaces blancs sont :

* `pre` préserve les espaces blancs. N'ajoute pas de nouvelle ligne lorsque le texte atteint la fin du conteneur, mais préserve les sauts de ligne ajoutés au texte
* `pre-wrap` préserve les espaces blancs. Ajoute de nouvelles lignes lorsque nécessaire lorsque le texte atteint la fin du conteneur

#### `tab-size`

Détermine la largeur du caractère de tabulation. Par défaut, elle est de 8, et vous pouvez définir une valeur entière qui définit le nombre de caractères qu'elle prend, ou une valeur de longueur :

```css
p {
  tab-size: 2;
}

span {
  tab-size: 4px;
}
```

#### `writing-mode`

Détermine si les lignes de texte sont disposées horizontalement ou verticalement, et la direction dans laquelle les blocs progressent.

Les valeurs que vous pouvez utiliser sont

* `horizontal-tb` (par défaut)
* `vertical-rl` le contenu est disposé verticalement. Les nouvelles lignes sont placées à gauche de la précédente
* `vertical-lr` le contenu est disposé verticalement. Les nouvelles lignes sont placées à droite de la précédente

#### `hyphens`

Détermine si des traits d'union doivent être ajoutés automatiquement lors du passage à une nouvelle ligne.

Les valeurs valides sont

* `none` (par défaut)
* `manual` ajoute un trait d'union uniquement lorsqu'il y a déjà un trait d'union visible ou un trait d'union caché (un caractère spécial)
* `auto` ajoute des traits d'union lorsqu'il est déterminé que le texte peut avoir un trait d'union.

#### `text-orientation`

Lorsque `writing-mode` est en mode vertical, détermine l'orientation du texte.

Les valeurs valides sont

* `mixed` est le mode par défaut, et si une langue est verticale (comme le japonais), elle préserve cette orientation, tout en faisant pivoter le texte écrit dans les langues occidentales
* `upright` fait en sorte que tout le texte soit orienté verticalement
* `sideways` fait en sorte que tout le texte soit orienté horizontalement

#### `direction`

Détermine la direction du texte. Les valeurs valides sont `ltr` et `rtl` :

```css
p {
  direction: rtl;
}
```

#### `word-break`

Cette propriété spécifie comment casser les lignes à l'intérieur des mots.

* `normal` (par défaut) signifie que le texte n'est cassé qu'entre les mots, pas à l'intérieur d'un mot
* `break-all` le navigateur peut casser un mot (mais aucun trait d'union n'est ajouté)
* `keep-all` supprime le retour à la ligne automatique. Principalement utilisé pour le texte CJK (Chinois/Japonais/Coréen).

En parlant de texte CJK, la propriété `line-break` est utilisée pour déterminer comment les lignes de texte se cassent. Je ne suis pas un expert de ces langues, donc je vais éviter de les couvrir.

#### `overflow-wrap`

Si un mot est trop long pour tenir sur une ligne, il peut déborder à l'extérieur du conteneur.

> _Cette propriété est également connue sous le nom de `word-wrap`, bien que ce soit non standard (mais fonctionne toujours comme un alias)_

C'est le comportement par défaut (`overflow-wrap: normal;`).

Nous pouvons utiliser :

```css
p {
  overflow-wrap: break-word;
}
```

pour le casser à la longueur exacte de la ligne, ou

```css
p {
  overflow-wrap: anywhere;
}
```

si le navigateur voit qu'il y a une opportunité de retour à la ligne quelque part plus tôt. Aucun trait d'union n'est ajouté, dans tous les cas.

Cette propriété est très similaire à `word-break`. Nous pourrions vouloir choisir celle-ci pour les langues occidentales, tandis que `word-break` a un traitement spécial pour les langues non occidentales.

### MODÈLE DE BOÎTE

Chaque élément CSS est essentiellement une boîte. Chaque élément est une boîte générique.

Le modèle de boîte explique le dimensionnement des éléments en fonction de quelques propriétés CSS.

De l'intérieur vers l'extérieur, nous avons :

* la zone de contenu
* le remplissage
* la bordure
* la marge

La meilleure façon de visualiser le modèle de boîte est d'ouvrir les outils de développement du navigateur et de vérifier comment il est affiché :

![Image](https://cdn-media-1.freecodecamp.org/images/xj9Q5XeqWTDKdl2roL0mkiHGXxRfGnAs4MhI)

Ici, vous pouvez voir comment Firefox me montre les propriétés d'un élément `span` que j'ai mis en surbrillance. J'ai fait un clic droit dessus, appuyé sur Inspecter l'élément, et je suis allé dans le panneau Layout des DevTools.

Voyez, l'espace bleu clair est la zone de contenu. Autour de celle-ci se trouve le remplissage, puis la bordure et enfin la marge.

Par défaut, si vous définissez une largeur (ou une hauteur) sur l'élément, celle-ci sera appliquée à la **zone de contenu**. Tous les calculs de remplissage, de bordure et de marge sont effectués en dehors de la valeur, vous devez donc garder cela à l'esprit lorsque vous faites vos calculs.

Plus tard, vous verrez comment vous pouvez changer ce comportement en utilisant le dimensionnement de boîte.

### BORDURE

La bordure est une fine couche entre le remplissage et la marge. En modifiant la bordure, vous pouvez faire en sorte que les éléments dessinent leur périmètre à l'écran.

Vous pouvez travailler sur les bordures en utilisant ces propriétés :

* `border-style`
* `border-color`
* `border-width`

La propriété `border` peut être utilisée comme un raccourci pour toutes ces propriétés.

`border-radius` est utilisé pour créer des coins arrondis.

Vous avez également la possibilité d'utiliser des images comme bordures, une capacité offerte par `border-image` et ses propriétés spécifiques séparées :

* `border-image-source`
* `border-image-slice`
* `border-image-width`
* `border-image-outset`
* `border-image-repeat`

Commençons par `border-style`.

#### Le style de bordure

La propriété `border-style` vous permet de choisir le style de la bordure. Les options que vous pouvez utiliser sont :

* `dotted`
* `dashed`
* `solid`
* `double`
* `groove`
* `ridge`
* `inset`
* `outset`
* `none`
* `hidden`

![Image](https://cdn-media-1.freecodecamp.org/images/lCWsi0wfQU30QoiDD6GsvfRrWx-4DurGOMeX)

Consultez [ce Codepen](https://codepen.io/flaviocopes/pen/yraaxq) pour un exemple en direct.

Le style par défaut est `none`, donc pour faire apparaître la bordure, vous devez la changer en autre chose. `solid` est un bon choix la plupart du temps.

Vous pouvez définir un style différent pour chaque bord en utilisant les propriétés

* `border-top-style`
* `border-right-style`
* `border-bottom-style`
* `border-left-style`

ou vous pouvez utiliser `border-style` avec plusieurs valeurs pour les définir, en utilisant l'ordre habituel Haut-Droite-Bas-Gauche :

```
p {
  border-style: solid dotted solid dotted;
}
```

#### La largeur de la bordure

`border-width` est utilisé pour définir la largeur de la bordure.

Vous pouvez utiliser l'une des valeurs prédéfinies :

* `thin`
* `medium` (la valeur par défaut)
* `thick`

ou exprimer une valeur en pixels, em ou rem ou toute autre valeur de longueur valide.

Exemple :

```css
p {
  border-width: 2px;
}
```

Vous pouvez définir la largeur de chaque bord (Haut-Droite-Bas-Gauche) séparément en utilisant 4 valeurs :

```css
p {
  border-width: 2px 1px 2px 1px;
}
```

ou vous pouvez utiliser les propriétés spécifiques de bord `border-top-width`, `border-right-width`, `border-bottom-width`, `border-left-width`.

#### La couleur de la bordure

`border-color` est utilisé pour définir la couleur de la bordure.

Si vous ne définissez pas de couleur, la bordure est par défaut colorée en utilisant la couleur du texte dans l'élément.

Vous pouvez passer n'importe quelle valeur de couleur valide à `border-color`.

Exemple :

```css
p {
  border-color: yellow;
}
```

Vous pouvez définir la couleur de chaque bord (Haut-Droite-Bas-Gauche) séparément en utilisant 4 valeurs :

```css
p {
  border-color: black red yellow blue;
}
```

ou vous pouvez utiliser les propriétés spécifiques de bord `border-top-color`, `border-right-color`, `border-bottom-color`, `border-left-color`.

#### La propriété raccourcie de bordure

Ces 3 propriétés mentionnées, `border-width`, `border-style` et `border-color` peuvent être définies en utilisant la propriété raccourcie `border`.

Exemple :

```css
p {
  border: 2px black solid;
}
```

Vous pouvez également utiliser les propriétés spécifiques de bord `border-top`, `border-right`, `border-bottom`, `border-left`.

Exemple :

```css
p {
  border-left: 2px black solid;
  border-right: 3px red dashed;
}
```

#### Le rayon de bordure

`border-radius` est utilisé pour définir des coins arrondis à la bordure. Vous devez passer une valeur qui sera utilisée comme le rayon du cercle qui sera utilisé pour arrondir la bordure.

Utilisation :

```css
p {
  border-radius: 3px;
}
```

Vous pouvez également utiliser les propriétés spécifiques de bord `border-top-left-radius`, `border-top-right-radius`, `border-bottom-left-radius`, `border-bottom-right-radius`.

#### Utilisation d'images comme bordures

Une chose très intéressante avec les bordures est la possibilité d'utiliser des images pour les styliser. Cela vous permet d'être très créatif avec les bordures.

Nous avons 5 propriétés :

* `border-image-source`
* `border-image-slice`
* `border-image-width`
* `border-image-outset`
* `border-image-repeat`

et le raccourci `border-image`. Je ne vais pas entrer dans les détails ici car les images comme bordures nécessiteraient une couverture plus approfondie que ce que je peux faire dans ce petit chapitre. Je recommande de lire l'entrée de l'almanach CSS Tricks sur border-image [https://css-tricks.com/almanac/properties/b/border-image/](https://css-tricks.com/almanac/properties/b/border-image/) pour plus d'informations.

### REMPLISSAGE

La propriété CSS `padding` est couramment utilisée en CSS pour ajouter de l'espace à l'intérieur d'un élément.

Rappelez-vous :

* `margin` ajoute de l'espace à l'extérieur de la bordure d'un élément
* `padding` ajoute de l'espace à l'intérieur de la bordure d'un élément

#### Propriétés de remplissage spécifiques

`padding` a 4 propriétés associées qui modifient le remplissage d'un seul bord à la fois :

* `padding-top`
* `padding-right`
* `padding-bottom`
* `padding-left`

L'utilisation de celles-ci est très simple et ne peut pas être confondue, par exemple :

```css
padding-left: 30px;
padding-right: 3em;
```

#### Utilisation du raccourci `padding`

`padding` est un raccourci pour spécifier plusieurs valeurs de remplissage en même temps, et selon le nombre de valeurs entrées, il se comporte différemment.

#### 1 valeur

L'utilisation d'une seule valeur applique celle-ci à **tous** les remplissages : haut, droite, bas, gauche.

```css
padding: 20px;
```

#### 2 valeurs

L'utilisation de 2 valeurs applique la première à **bas & haut**, et la seconde à **gauche & droite**.

```css
padding: 20px 10px;
```

#### 3 valeurs

L'utilisation de 3 valeurs applique la première à **haut**, la seconde à **gauche & droite**, la troisième à **bas**.

```css
padding: 20px 10px 30px;
```

#### 4 valeurs

L'utilisation de 4 valeurs applique la première à **haut**, la seconde à **droite**, la troisième à **bas**, la quatrième à **gauche**.

```css
padding: 20px 10px 5px 0px;
```

Ainsi, l'ordre est _haut-droite-bas-gauche_.

#### Valeurs acceptées

`padding` accepte les valeurs exprimées dans n'importe quel type d'unité de longueur, les plus courantes sont px, em, rem, mais [beaucoup d'autres existent](https://developer.mozilla.org/en-US/docs/Web/CSS/length).

### MARGE

La propriété CSS `margin` est couramment utilisée en CSS pour ajouter de l'espace autour d'un élément.

Rappelez-vous :

* `margin` ajoute de l'espace à l'extérieur de la bordure d'un élément
* `padding` ajoute de l'espace à l'intérieur de la bordure d'un élément

#### Propriétés de marge spécifiques

`margin` a 4 propriétés associées qui modifient la marge d'un seul bord à la fois :

* `margin-top`
* `margin-right`
* `margin-bottom`
* `margin-left`

L'utilisation de celles-ci est très simple et ne peut pas être confondue, par exemple :

```css
margin-left: 30px;
margin-right: 3em;
```

#### Utilisation du raccourci `margin`

`margin` est un raccourci pour spécifier plusieurs marges en même temps, et selon le nombre de valeurs entrées, il se comporte différemment.

#### 1 valeur

L'utilisation d'une seule valeur applique celle-ci à **toutes** les marges : haut, droite, bas, gauche.

```css
margin: 20px;
```

#### 2 valeurs

L'utilisation de 2 valeurs applique la première à **bas & haut**, et la seconde à **gauche & droite**.

```css
margin: 20px 10px;
```

#### 3 valeurs

L'utilisation de 3 valeurs applique la première à **haut**, la seconde à **gauche & droite**, la troisième à **bas**.

```css
margin: 20px 10px 30px;
```

#### 4 valeurs

L'utilisation de 4 valeurs applique la première à **haut**, la seconde à **droite**, la troisième à **bas**, la quatrième à **gauche**.

```css
margin: 20px 10px 5px 0px;
```

Ainsi, l'ordre est _haut-droite-bas-gauche_.

#### Valeurs acceptées

`margin` accepte les valeurs exprimées dans n'importe quel type d'unité de longueur, les plus courantes sont px, em, rem, mais [beaucoup d'autres existent](https://developer.mozilla.org/en-US/docs/Web/CSS/length).

Il accepte également les valeurs en pourcentage, et la valeur spéciale `auto`.

#### Utilisation de `auto` pour centrer les éléments

`auto` peut être utilisé pour dire au navigateur de sélectionner automatiquement une marge, et il est le plus couramment utilisé pour centrer un élément de cette manière :

```css
margin: 0 auto;
```

Comme dit ci-dessus, l'utilisation de 2 valeurs applique la première à **bas & haut**, et la seconde à **gauche & droite**.

La manière moderne de centrer les éléments est d'utiliser [Flexbox](https://flaviocopes.com/flexbox/), et sa directive `justify-content: center;`.

Les anciens navigateurs, bien sûr, n'implémentent pas Flexbox, et si vous devez les supporter, `margin: 0 auto;` est toujours un bon choix.

#### Utilisation d'une marge négative

`margin` est la seule propriété liée au dimensionnement qui peut avoir une valeur négative. C'est extrêmement utile, aussi. Définir une marge supérieure négative fait bouger un élément par-dessus les éléments qui le précèdent, et avec une valeur négative suffisante, il sortira de la page.

Une marge inférieure négative fait monter les éléments qui le suivent.

Une marge droite négative fait en sorte que le contenu de l'élément s'étende au-delà de sa taille de contenu autorisée.

Une marge gauche négative fait bouger l'élément vers la gauche par-dessus les éléments qui le précèdent, et avec une valeur négative suffisante, il sortira de la page.

### DIMENSIONNEMENT DE BOÎTE

Le comportement par défaut des navigateurs lors du calcul de la largeur d'un élément est d'appliquer la largeur et la hauteur calculées à la **zone de contenu**, sans prendre en compte le remplissage, la bordure et la marge.

Cette approche s'est avérée assez compliquée à utiliser.

Vous pouvez changer ce comportement en définissant la propriété `box-sizing`.

La propriété `box-sizing` est une grande aide. Elle a 2 valeurs :

* `border-box`
* `content-box`

`content-box` est la valeur par défaut, celle que nous avions depuis des années avant que `box-sizing` ne devienne une chose.

`border-box` est la nouvelle et grande chose que nous recherchons. Si vous définissez cela sur un élément :

```css
.my-div {
  box-sizing: border-box;
}
```

le calcul de la largeur et de la hauteur inclut le remplissage et la bordure. Seule la marge est laissée de côté, ce qui est raisonnable puisque dans notre esprit, nous la voyons également typiquement comme une chose séparée : la marge est à l'extérieur de la boîte.

Cette propriété est un petit changement mais a un grand impact. CSS Tricks a même déclaré un [jour international de sensibilisation à la boîte de dimensionnement](https://css-tricks.com/international-box-sizing-awareness-day/), juste pour dire, et il est recommandé de l'appliquer à chaque élément de la page, dès le départ, avec ceci :

```css
*, *:before, *:after {
  box-sizing: border-box;
}
```

### AFFICHAGE

La propriété `display` d'un objet détermine comment il est rendu par le navigateur.

C'est une propriété très importante, et probablement celle avec le plus grand nombre de valeurs que vous pouvez utiliser.

Ces valeurs incluent :

* `block`
* `inline`
* `none`
* `contents`
* `flow`
* `flow-root`
* `table` (et toutes les `table-*`)
* `flex`
* `grid`
* `list-item`
* `inline-block`
* `inline-table`
* `inline-flex`
* `inline-grid`
* `inline-list-item`

plus d'autres que vous n'utiliserez probablement pas, comme `ruby`.

Choisir l'une de celles-ci modifiera considérablement le comportement du navigateur avec l'élément et ses enfants.

Dans cette section, nous allons analyser les plus importantes non couvertes ailleurs :

* `block`
* `inline`
* `inline-block`
* `none`

Nous verrons certaines des autres dans les chapitres suivants, y compris la couverture de `table`, `flex` et `grid`.

#### `inline`

Inline est la valeur d'affichage par défaut pour chaque élément en CSS.

Toutes les balises HTML sont affichées en ligne par défaut sauf certains éléments comme `div`, `p` et `section`, qui sont définis comme `block` par l'agent utilisateur (le navigateur).

Les éléments en ligne n'ont aucune marge ou remplissage appliqué.

Idem pour la hauteur et la largeur.

Vous _pouvez_ les ajouter, mais l'apparence dans la page ne changera pas — ils sont calculés et appliqués automatiquement par le navigateur.

#### `inline-block`

Similaire à `inline`, mais avec `inline-block`, `width` et `height` sont appliqués comme vous le spécifiez.

#### `block`

Comme mentionné, normalement les éléments sont affichés en ligne, à l'exception de certains éléments, y compris

* `div`
* `p`
* `section`
* `ul`

qui sont définis comme `block` par le navigateur.

Avec `display: block`, les éléments sont empilés les uns après les autres, verticalement, et chaque élément occupe 100 % de la page.

Les valeurs assignées aux propriétés `width` et `height` sont respectées, si vous les définissez, ainsi que `margin` et `padding`.

#### `none`

L'utilisation de `display: none` fait disparaître un élément. Il est toujours là dans le HTML, mais simplement non visible dans le navigateur.

### POSITIONNEMENT

Le positionnement est ce qui nous permet de déterminer où les éléments apparaissent à l'écran, et comment ils apparaissent.

Vous pouvez déplacer des éléments, et les positionner exactement où vous le souhaitez.

Dans cette section, nous verrons également comment les choses changent sur une page en fonction de la manière dont les éléments avec différents `position` interagissent les uns avec les autres.

Nous avons une principale propriété CSS : `position`.

Elle peut avoir ces 5 valeurs :

* `static`
* `relative`
* `absolute`
* `fixed`
* `sticky`

#### Positionnement statique

C'est la valeur par défaut pour un élément. Les éléments positionnés de manière statique sont affichés dans le flux normal de la page.

#### Positionnement relatif

Si vous définissez `position: relative` sur un élément, vous pouvez maintenant le positionner avec un décalage, en utilisant les propriétés

* top
* right
* bottom
* left

qui sont appelées **propriétés de décalage**. Elles acceptent une valeur de longueur ou un pourcentage.

Prenez [cet exemple que j'ai fait sur Codepen](https://codepen.io/flaviocopes/pen/WWGgrR). Je crée un conteneur parent, un conteneur enfant, et une boîte intérieure avec du texte :

```html
<div class="parent">
  <div class="child">
    <div class="box">
      <p>Test</p>
    </div>
  </div>
</div>
```

avec un peu de CSS pour donner des couleurs et du remplissage, mais cela n'affecte pas le positionnement :

```css
.parent {
  background-color: #af47ff;
  padding: 30px;
  width: 300px;
}

.child {
  background-color: #ff4797;
  padding: 30px;
}

.box {
  background-color: #f3ff47;
  padding: 30px;
  border: 2px solid #333;
  border-style: dotted;
  font-family: courier;
  text-align: center;
  font-size: 2rem;
}
```

voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/gtXUfjyrczqxDqdfrjJyec58o9ru6CqGGCFD)

Vous pouvez essayer d'ajouter l'une des propriétés que j'ai mentionnées précédemment (`top`, `right`, `bottom`, `left`) à `.box`, et rien ne se passera. La position est `static`.

Maintenant, si nous définissons `position: relative` sur la boîte, au premier abord, apparemment rien ne change. Mais l'élément peut maintenant se déplacer en utilisant les propriétés `top`, `right`, `bottom`, `left`, et vous pouvez maintenant modifier sa position par rapport à l'élément qui le contient.

Par exemple :

```css
.box {
  /* ... */
  position: relative;
  top: -60px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/aYTcDVhCB9-CazlQrWrPyfxMpr3TThT0V-ho)

Une valeur négative pour `top` fera monter la boîte par rapport à son conteneur.

Ou

```css
.box {
  /* ... */
  position: relative;
  top: -60px;
  left: 180px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/5ePc6ALKZV0fubpagz0OzfPBCzctqPAJY81p)

Remarquez comment l'espace occupé par la boîte reste préservé dans le conteneur, comme s'il était encore à sa place.

Une autre propriété qui fonctionnera maintenant est `z-index` pour modifier le placement sur l'axe z. Nous en parlerons plus tard.

#### Positionnement absolu

Définir `position: absolute` sur un élément le retirera du flux du document.

Souvenez-vous du positionnement relatif où nous avons remarqué que l'espace occupé à l'origine par un élément était préservé même s'il était déplacé ?

Avec le positionnement absolu, dès que nous définissons `position: absolute` sur `.box`, son espace d'origine est maintenant réduit, et seules les coordonnées d'origine (x, y) restent les mêmes.

```css
.box {
  /* ... */
  position: absolute;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/B4aFUpYab0eSO-LUQKAu2Vmbi-wnFA8qFOHm)

Nous pouvons maintenant déplacer la boîte comme nous le souhaitons, en utilisant les propriétés `top`, `right`, `bottom`, `left` :

```css
.box {
  /* ... */
  position: absolute;
  top: 0px;
  left: 0px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/NHw-ZkR2lzBsPyb9gSYTyuYGreSvedNPsJ7J)

ou

```css
.box {
  /* ... */
  position: absolute;
  top: 140px;
  left: 50px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/QOYrWkDjiNv7ODZ9WtYCBVEnJf5oZwGfombH)

Les coordonnées sont relatives au conteneur le plus proche qui n'est pas `static`.

Cela signifie que si nous ajoutons `position: relative` à l'élément `.child`, et que nous définissons `top` et `left` à 0, la boîte ne sera pas positionnée en haut à gauche de la _fenêtre_, mais plutôt elle sera positionnée aux coordonnées 0, 0 de `.child` :

```css
.child {
  /* ... */
  position: relative;
}

.box {
  /* ... */
  position: absolute;
  top: 0px;
  left: 0px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1FB8qKtiZgmxtp7xjd6UU7CW573XRxTrZlNc)

Voici comment nous avons déjà vu que `.child` est statique (par défaut) :

```css
.child {
  /* ... */
  position: static;
}

.box {
  /* ... */
  position: absolute;
  top: 0px;
  left: 0px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/eF4yC5dRIkcyezTcVUCbG36sfxOVurQX2L38)

Comme pour le positionnement relatif, vous pouvez utiliser `z-index` pour modifier le placement sur l'axe z.

#### Positionnement fixe

Comme avec le positionnement absolu, lorsqu'un élément est assigné `position: fixed`, il est retiré du flux de la page.

La différence avec le positionnement absolu est la suivante : les éléments sont maintenant toujours positionnés par rapport à la fenêtre, au lieu du premier conteneur non statique.

```css
.box {
  /* ... */
  position: fixed;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Ium4uJdPRXPpp-gAVsMMWveviu6HY-g0nUYA)

```css
.box {
  /* ... */
  position: fixed;
  top: 0;
  left: 0;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/k3-LecCC6WXUjssKdQ9u9w70EZSh3hzK3iFY)

Une autre grande différence est que les éléments ne sont pas affectés par le défilement. Une fois que vous placez un élément fixe quelque part, le défilement de la page ne le retire pas de la partie visible de la page.

#### Positionnement collant

Alors que les valeurs ci-dessus existent depuis très longtemps, celle-ci a été introduite récemment et elle est encore relativement non supportée ([voir caniuse.com](https://caniuse.com/#feat=css-sticky))

Le composant UITableView iOS est la chose qui me vient à l'esprit lorsque je pense à `position: sticky`. Vous savez, lorsque vous faites défiler dans la liste des contacts et que la première lettre reste collée en haut, pour vous indiquer que vous consultez les contacts de cette lettre particulière ?

Nous utilisions JavaScript pour émuler cela, mais c'est l'approche adoptée par CSS pour le permettre de manière native.

### FLOTTANT ET NETTOYAGE

Le flottement a été un sujet très important dans le passé.

Il était utilisé dans de nombreux hacks et usages créatifs car c'était l'une des rares façons, avec les tableaux, dont nous pouvions vraiment implémenter certains layouts. Dans le passé, nous avions l'habitude de faire flotter la barre latérale à gauche, par exemple, pour l'afficher sur le côté gauche de l'écran et ajouter une marge au contenu principal.

Heureusement, les temps ont changé et aujourd'hui nous avons Flexbox et Grid pour nous aider avec la mise en page, et le flottement est revenu à son champ d'application initial : placer le contenu d'un côté de l'élément conteneur, et faire en sorte que ses frères et sœurs apparaissent autour de lui.

La propriété `float` supporte 3 valeurs :

* `left`
* `right`
* `none` (par défaut)

Supposons que nous avons une boîte qui contient un paragraphe avec du texte, et le paragraphe contient également une image.

Voici un peu de code :

```css
<div class="parent">
  <div class="child">
    <div class="box">
      <p>Ceci est un paragraphe aléatoire et une image. <img src="https://via.placeholder.com/100x100" /> L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte.
      </p>
    </div>
  </div>
</div>

.parent {
  background-color: #af47ff;
  padding: 30px;
  width: 500px;
}

.child {
  background-color: #ff4797;
  padding: 30px;
}

.box {
  background-color: #f3ff47;
  padding: 30px;
  border: 2px solid #333;
  border-style: dotted;
  font-family: courier;
  text-align: justify;
  font-size: 1rem;
}
```

et l'apparence visuelle :

![Image](https://cdn-media-1.freecodecamp.org/images/fx5ZaCoCalyWSNeIkNi6044e5uEPPlQVupJD)

Comme vous pouvez le voir, le flux normal par défaut considère l'image en ligne, et fait de la place pour elle dans la ligne elle-même.

Si nous ajoutons `float: left` à l'image, et un peu de remplissage :

```css
img {
  float: left;
  padding: 20px 20px 0px 0px;
}
```

voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/Yftt6zI7UBrNYY30BapoEr3BAtiVCx80M4Eq)

et voici ce que nous obtenons en appliquant un flottement à droite, en ajustant le remplissage en conséquence :

```css
img {
  float: right;
  padding: 20px 0px 20px 20px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/WORQNScMck67c42LH0cfbiZJmzNnGzWde1Au)

Un élément flottant est retiré du flux normal de la page, et l'autre contenu s'écoule autour de lui.

[Voir l'exemple sur Codepen](https://codepen.io/flaviocopes/pen/WWGqPr?editors=1100)

Vous n'êtes pas limité à faire flotter des images, non plus. Ici, nous remplaçons l'image par un élément `span` :

```css
<div class="parent">
  <div class="child">
    <div class="box">
      <p>Ceci est un paragraphe aléatoire et une image. <span>Du texte à faire flotter</span> L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte. L'image est au milieu du texte.
      </p>
    </div>
  </div>
</div>

span {
  float: right;
  margin: 20px 0px 20px 20px;
  padding: 10px;
  border: 1px solid black
}
```

et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/Pe0oVfgmeHF7Rheb4hPwXTaq5AZ1939rMeBy)

#### Nettoyage

Que se passe-t-il lorsque vous faites flotter plus d'un élément ?

Si, lorsqu'ils flottent, ils trouvent une autre image flottante, par défaut, ils sont empilés les uns à côté des autres, horizontalement. Jusqu'à ce qu'il n'y ait plus de place, et ils commenceront à être empilés sur une nouvelle ligne.

Supposons que nous avions 3 images en ligne à l'intérieur d'une balise `p` :

![Image](https://cdn-media-1.freecodecamp.org/images/15-LCn0BOSVAVMraLSiNzWpP-oWBiEKIGULW)

Si nous ajoutons `float: left` à ces images :

```css
img {
  float: left;
  padding: 20px 20px 0px 0px;
}
```

voici ce que nous aurons :

![Image](https://cdn-media-1.freecodecamp.org/images/JGZ7LTxKux1nKWIISdzIPgb2jzxcqpifbxIx)

si vous ajoutez `clear: left` aux images, celles-ci seront empilées verticalement plutôt qu'horizontalement :

![Image](https://cdn-media-1.freecodecamp.org/images/9J-ggQAlJFZ4C1hUbnpD74FcjuKpS960LABv)

J'ai utilisé la valeur `left` pour `clear`. Elle permet

* `left` pour effacer les flottements à gauche
* `right` pour effacer les flottements à droite
* `both` pour effacer les flottements à gauche et à droite
* `none` (par défaut) désactive l'effacement

### Z-INDEX

Lorsque nous avons parlé de positionnement, j'ai mentionné que vous pouvez utiliser la propriété `z-index` pour contrôler le positionnement des éléments sur l'axe Z.

C'est très utile lorsque vous avez plusieurs éléments qui se chevauchent, et que vous devez décider lequel est visible, comme étant plus proche de l'utilisateur, et lequel (lesquels) doit être caché derrière.

Cette propriété prend un nombre (sans décimales) et utilise ce nombre pour calculer quels éléments apparaissent plus proches de l'utilisateur, sur l'axe Z.

Plus la valeur de z-index est élevée, plus un élément est positionné près de l'utilisateur.

Lors de la décision de quel élément doit être visible et lequel doit être positionné derrière, le navigateur effectue un calcul sur la valeur de z-index.

La valeur par défaut est `auto`, un mot-clé spécial. En utilisant `auto`, l'ordre de l'axe Z est déterminé par la position de l'élément HTML dans la page - le dernier frère apparaît en premier, car il est défini en dernier.

Par défaut, les éléments ont la valeur `static` pour la propriété `position`. Dans ce cas, la propriété `z-index` ne fait aucune différence - elle doit être définie sur `absolute`, `relative` ou `fixed` pour fonctionner.

Exemple :

```css
.my-first-div {
    position: absolute;
    top: 0;
    left: 0;
    width: 600px;
    height: 600px;
    z-index: 10;
}

.my-second-div {
    position: absolute;
    top: 0;
    left: 0;
    width: 500px;
    height: 500px;
    z-index: 20;
}
```

L'élément avec la classe `.my-second-div` sera affiché, et derrière lui `.my-first-div`.

Ici, nous avons utilisé 10 et 20, mais vous pouvez utiliser n'importe quel nombre. Même des nombres négatifs. Il est courant de choisir des nombres non consécutifs, afin de pouvoir positionner des éléments au milieu. Si vous utilisez des nombres consécutifs à la place, vous devrez recalculer le z-index de chaque élément impliqué dans le positionnement.

### CSS GRID

CSS Grid est le nouveau venu dans le monde CSS, et bien qu'il ne soit pas encore entièrement supporté par tous les navigateurs, il sera le futur système pour les mises en page.

CSS Grid est une approche fondamentalement nouvelle pour construire des mises en page en utilisant CSS.

Surveillez la page CSS Grid Layout sur caniuse.com ([https://caniuse.com/#feat=css-grid](https://caniuse.com/#feat=css-grid)) pour savoir quels navigateurs le supportent actuellement. Au moment de la rédaction, en avril 2019, tous les principaux navigateurs (sauf IE, qui n'aura jamais de support pour celui-ci) supportent déjà cette technologie, couvrant 92% de tous les utilisateurs.

CSS Grid n'est pas un concurrent de Flexbox. Ils interopèrent et collaborent sur des mises en page complexes, car CSS Grid fonctionne sur 2 dimensions (lignes ET colonnes) tandis que Flexbox fonctionne sur une seule dimension (lignes OU colonnes).

Construire des mises en page pour le web a traditionnellement été un sujet compliqué.

Je ne vais pas creuser les raisons de cette complexité, qui est un sujet complexe en soi. Mais vous pouvez vous considérer comme un humain très chanceux car de nos jours vous avez 2 outils très puissants et bien supportés à votre disposition :

* **CSS Flexbox**
* **CSS Grid**

Ces 2 outils sont ceux pour construire les mises en page Web de l'avenir.

Sauf si vous devez supporter des anciens navigateurs comme IE8 et IE9, il n'y a aucune raison de s'embêter avec des choses comme :

* Les mises en page de tableaux
* Les flottants
* Les hacks de clearfix
* Les hacks `display: table`

Dans ce guide, il y a tout ce que vous devez savoir pour passer d'une connaissance nulle de CSS Grid à être un utilisateur compétent.

#### Les bases

La mise en page CSS Grid est activée sur un élément conteneur (qui peut être un `div` ou toute autre balise) en définissant `display: grid`.

Comme avec flexbox, vous pouvez définir certaines propriétés sur le conteneur, et certaines propriétés sur chaque élément individuel de la grille.

Ces propriétés combinées détermineront l'apparence finale de la grille.

Les propriétés de conteneur les plus basiques sont `grid-template-columns` et `grid-template-rows`.

#### grid-template-columns et grid-template-rows

Ces propriétés définissent le nombre de colonnes et de lignes dans la grille, et elles définissent également la largeur de chaque colonne/ligne.

L'extrait suivant définit une grille avec 4 colonnes de 200px de large chacune, et 2 lignes de 300px de haut chacune.

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/LgbgchKoiffQNAqLtBYVbPsLJMKiWB3XWvCP)

Voici un autre exemple de grille avec 2 colonnes et 2 lignes :

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px;
  grid-template-rows: 100px 100px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/sdVnLwfTJmY1alewU41wNxRMZ827XK07quWq)

#### Dimensions automatiques

De nombreuses fois, vous pourriez avoir une taille d'en-tête fixe, une taille de pied de page fixe, et le contenu principal qui est flexible en hauteur, en fonction de sa longueur. Dans ce cas, vous pouvez utiliser le mot-clé auto :

```css
.container {
  display: grid;
  grid-template-rows: 100px auto 100px;
}
```

#### Différentes dimensions de colonnes et de lignes

Dans les exemples ci-dessus, nous avons créé des grilles régulières en utilisant les mêmes valeurs pour les lignes et les mêmes valeurs pour les colonnes.

Vous pouvez spécifier n'importe quelle valeur pour chaque ligne/colonne, pour créer de nombreux designs différents :

```css
.container {
  display: grid;
  grid-template-columns: 100px 200px;
  grid-template-rows: 100px 50px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/h5vifpz6IUZQbWCzX4YvJjOhLojgzgP2F-AN)

Un autre exemple :

```css
.container {
  display: grid;
  grid-template-columns: 10px 100px;
  grid-template-rows: 100px 10px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/GGCFboj9Z6YQz8jvB69KmslqKz00sLuca843)

#### Ajout d'espace entre les cellules

Sauf indication contraire, il n'y a pas d'espace entre les cellules.

Vous pouvez ajouter de l'espacement en utilisant ces propriétés :

* `grid-column-gap`
* `grid-row-gap`

ou la syntaxe raccourcie `grid-gap`.

Exemple :

```css
.container {
  display: grid;
  grid-template-columns: 100px 200px;
  grid-template-rows: 100px 50px;
  grid-column-gap: 25px;
  grid-row-gap: 25px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ivVtIubdZG3BpFfoASpFy4EMJG1kXeiCx3zP)

La même mise en page en utilisant le raccourci :

```css
.container {
  display: grid;
  grid-template-columns: 100px 200px;
  grid-template-rows: 100px 50px;
  grid-gap: 25px;
}
```

#### Étendre les éléments sur plusieurs colonnes et/ou lignes

Chaque élément de cellule a la possibilité d'occuper plus d'une seule case dans la ligne, et de s'étendre horizontalement ou verticalement pour obtenir plus d'espace, tout en respectant les proportions de la grille définies dans le conteneur.

Ce sont les propriétés que nous utiliserons pour cela :

* `grid-column-start`
* `grid-column-end`
* `grid-row-start`
* `grid-row-end`

Exemple :

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
}

.item1 {
  grid-column-start: 2;
  grid-column-end: 4;
}

.item6 {
  grid-column-start: 3;
  grid-column-end: 5;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/JrzZm5o6SkpvGiKZo6v8XmRDAfpajBt6mym4)

Les nombres correspondent à la ligne verticale qui sépare chaque colonne, en commençant par 1 :

![Image](https://cdn-media-1.freecodecamp.org/images/JdCCwzrGzvd1O68dBAqIHSWh4hMbM6ttuJ8Z)

Le même principe s'applique à `grid-row-start` et `grid-row-end`, sauf que cette fois, au lieu de prendre plus de colonnes, une cellule prend plus de lignes.

#### Syntaxe raccourcie

Ces propriétés ont une syntaxe raccourcie fournie par :

* `grid-column`
* `grid-row`

L'utilisation est simple, voici comment reproduire la mise en page ci-dessus :

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
}

.item1 {
  grid-column: 2 / 4;
}

.item6 {
  grid-column: 3 / 5;
}
```

Une autre approche consiste à définir la colonne/ligne de départ, et à définir combien elle doit occuper en utilisant `span` :

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
}

.item1 {
  grid-column: 2 / span 2;
}

.item6 {
  grid-column: 3 / span 2;
}
```

### Plus de configuration de grille

#### Utilisation de fractions

Spécifier la largeur exacte de chaque colonne ou ligne n'est pas idéal dans tous les cas.

Une fraction est une unité d'espace.

L'exemple suivant divise une grille en 3 colonnes de même largeur, chacune occupant 1/3 de l'espace disponible.

```css
.container {
  grid-template-columns: 1fr 1fr 1fr;
}
```

#### Utilisation de pourcentages et rem

Vous pouvez également utiliser des pourcentages, et mélanger et assortir des fractions, des pixels, des rem et des pourcentages :

```css
.container {
  grid-template-columns: 3rem 15% 1fr 2fr
}
```

#### Utilisation de `repeat()`

`repeat()` est une fonction spéciale qui prend un nombre indiquant le nombre de fois qu'une ligne/colonne sera répétée, et la longueur de chacune.

Si chaque colonne a la même largeur, vous pouvez spécifier la mise en page en utilisant cette syntaxe :

```css
.container {
  grid-template-columns: repeat(4, 100px);
}
```

Cela crée 4 colonnes de même largeur.

Ou en utilisant des fractions :

```css
.container {
  grid-template-columns: repeat(4, 1fr);
}
```

#### Spécifier une largeur minimale pour une ligne

Cas d'utilisation courant : Avoir une barre latérale qui ne se réduit jamais en dessous d'une certaine quantité de pixels lorsque vous redimensionnez la fenêtre.

Voici un exemple où la barre latérale prend 1/4 de l'écran et ne prend jamais moins de 200px :

```css
.container {
  grid-template-columns: minmax(200px, 3fr) 9fr;
}
```

Vous pouvez également définir uniquement une valeur maximale en utilisant le mot-clé `auto` :

```css
.container {
  grid-template-columns: minmax(auto, 50%) 9fr;
}
```

ou uniquement une valeur minimale :

```css
.container {
  grid-template-columns: minmax(100px, auto) 9fr;
}
```

#### Positionnement des éléments en utilisant `grid-template-areas`

Par défaut, les éléments sont positionnés dans la grille en utilisant leur ordre dans la structure HTML.

En utilisant `grid-template-areas`, vous pouvez définir des zones de modèle pour les déplacer dans la grille, et également étendre un élément sur plusieurs lignes / colonnes au lieu d'utiliser `grid-column`.

Voici un exemple :

```css
<div class="container">
  <main>
    ...
  </main>
  <aside>
    ...
  </aside>
  <header>
    ...
  </header>
  <footer>
    ...
  </footer>
</div>

.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
  grid-template-areas:
    "header header header header"
    "sidebar main main main"
    "footer footer footer footer";
}
main {
  grid-area: main;
}
aside {
  grid-area: sidebar;
}
header {
  grid-area: header;
}
footer {
  grid-area: footer;
}
```

Malgré leur ordre original, les éléments sont placés où `grid-template-areas` les définit, en fonction de la propriété `grid-area` qui leur est associée.

#### Ajout de cellules vides dans les zones de modèle

Vous pouvez définir une cellule vide en utilisant le point `.` au lieu d'un nom de zone dans `grid-template-areas` :

```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px 200px;
  grid-template-rows: 300px 300px;
  grid-template-areas:
    ". header header ."
    "sidebar . main main"
    ". footer footer .";
}
```

#### Remplir une page avec une grille

Vous pouvez faire en sorte qu'une grille s'étende pour remplir la page en utilisant `fr` :

```css
.container {
  display: grid;
  height: 100vh;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
}
```

#### Un exemple : en-tête, barre latérale, contenu et pied de page

Voici un exemple simple d'utilisation de CSS Grid pour créer une mise en page de site qui fournit un en-tête en haut, une partie principale avec une barre latérale à gauche et du contenu à droite, et un pied de page ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/M8qvpAE1DS6BoPXyfpb2VWAEbz2C8U4W587t)

Voici le balisage :

```html
<div class="wrapper">
  <header>Header</header>
  <article>
    <h1>Welcome</h1>
    <p>Hi!</p>
  </article>
  <aside><ul><li>Sidebar</li></ul></aside>
  <footer>Footer</footer>
</div>
```

et voici le CSS :

```css
header {
  grid-area: header;
  background-color: #fed330;
  padding: 20px;
}
article {
  grid-area: content;
  background-color: #20bf6b;
  padding: 20px;
}
aside {
  grid-area: sidebar;
  background-color: #45aaf2;
}
footer {
  padding: 20px;
  grid-area: footer;
  background-color: #fd9644;
}
.wrapper {
  display: grid;
  grid-gap: 20px;
  grid-template-columns: 1fr 3fr;
  grid-template-areas:
    "header  header"
    "sidebar content"
    "footer  footer";
}
```

J'ai ajouté quelques couleurs pour le rendre plus joli, mais en gros, cela assigne à chaque balise différente un nom de `grid-area`, qui est utilisé dans la propriété `grid-template-areas` dans `.wrapper`.

Lorsque la mise en page est plus petite, nous pouvons mettre la barre latérale sous le contenu en utilisant une requête média :

```css
@media (max-width: 500px) {
  .wrapper {
    grid-template-columns: 4fr;
    grid-template-areas:
      "header"
      "content"
      "sidebar"
      "footer";
  }
}
```

[Voir sur CodePen](https://codepen.io/flaviocopes/pen/JZWOEK)

Ce sont les bases de CSS Grid. Il y a beaucoup de choses que je n'ai pas incluses dans cette introduction, mais je voulais la rendre très simple, afin que vous puissiez commencer à utiliser ce nouveau système de mise en page sans que cela ne semble écrasant.

### FLEXBOX

Flexbox, également appelé Flexible Box Module, est l'un des deux systèmes de mise en page modernes, avec CSS Grid.

Comparé à CSS Grid (qui est bidimensionnel), flexbox est un **modèle de mise en page unidimensionnel**. Il contrôlera la mise en page en fonction d'une ligne ou d'une colonne, mais pas les deux en même temps.

Le principal objectif de flexbox est de permettre aux éléments de remplir tout l'espace offert par leur conteneur, en fonction de certaines règles que vous définissez.

Sauf si vous devez supporter des anciens navigateurs comme IE8 et IE9, Flexbox est l'outil qui vous permet d'oublier l'utilisation de

* Mises en page de tableaux
* Flottants
* Hacks de clearfix
* Hacks `display: table`

Plongeons dans flexbox et devenons un maître en très peu de temps.

### Support des navigateurs

Au moment de la rédaction (février 2018), il est supporté par 97,66 % des utilisateurs. Tous les navigateurs les plus importants l'ont implémenté depuis des années, donc même les anciens navigateurs (y compris IE10+) sont couverts :

![Image](https://cdn-media-1.freecodecamp.org/images/pAsJcNUmJljKeifKY7DSA8-LQasyo2vsgOoW)

Alors que nous devons attendre quelques années pour que les utilisateurs rattrapent CSS Grid, Flexbox est une technologie plus ancienne et peut être utilisée dès maintenant.

### Activer Flexbox

Une mise en page flexbox est appliquée à un conteneur, en définissant

```css
display: flex;
```

ou

```css
display: inline-flex;
```

Le contenu **à l'intérieur du conteneur** sera aligné en utilisant flexbox.

#### Propriétés du conteneur

Certaines propriétés flexbox s'appliquent au conteneur, qui définit les règles générales pour ses éléments. Elles sont

* `flex-direction`
* `justify-content`
* `align-items`
* `flex-wrap`
* `flex-flow`

#### Aligner les lignes ou les colonnes

La première propriété que nous voyons, `**flex-direction**`, détermine si le conteneur doit aligner ses éléments en tant que lignes, ou en tant que colonnes :

* `flex-direction: row` place les éléments en tant que **ligne**, dans la direction du texte (de gauche à droite pour les pays occidentaux)
* `flex-direction: row-reverse` place les éléments comme `row` mais dans la direction opposée
* `flex-direction: column` place les éléments dans une **colonne**, en ordonnant de haut en bas
* `flex-direction: column-reverse` place les éléments dans une colonne, comme `column` mais dans la direction opposée

![Image](https://cdn-media-1.freecodecamp.org/images/o26IgBk91Cjdfe8h-uAl-NAULk6k5fUjTI8o)

#### Alignement vertical et horizontal

Par défaut, les éléments commencent à gauche si `flex-direction` est row, et en haut si `flex-direction` est column.

![Image](https://cdn-media-1.freecodecamp.org/images/lgTI1ZtxbWha-5GyAWbTNrmOhe03ikkpo-Gx)

Vous pouvez changer ce comportement en utilisant `justify-content` pour changer l'alignement horizontal, et `align-items` pour changer l'alignement vertical.

#### Changer l'alignement horizontal

`**justify-content**` a 5 valeurs possibles :

* `flex-start` : aligne à gauche du conteneur.
* `flex-end` : aligne à droite du conteneur.
* `center` : aligne au centre du conteneur.
* `space-between` : affiche avec un espacement égal entre eux.
* `space-around` : affiche avec un espacement égal autour d'eux

![Image](https://cdn-media-1.freecodecamp.org/images/3eA5Rgtjp0xnyWoQ5v5e1aWIbgmS8YgWzgdm)

#### Changer l'alignement vertical

`**align-items**` a 5 valeurs possibles :

* `flex-start` : aligne en haut du conteneur.
* `flex-end` : aligne en bas du conteneur.
* `center` : aligne au centre vertical du conteneur.
* `baseline` : affiche à la ligne de base du conteneur.
* `stretch` : les éléments sont étirés pour s'adapter au conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/1pQRvAAzAtBRjO8UI8-zpoa8rL51uKkKklZR)

Une note sur `baseline` :

`baseline` semble similaire à `flex-start` dans cet exemple, en raison de mes boîtes étant trop simples. Consultez [ce Codepen](https://codepen.io/flaviocopes/pen/oExoJR) pour avoir un exemple plus utile, que j'ai forké d'un Pen créé à l'origine par [Martin Michálek](https://twitter.com/machal). Comme vous pouvez le voir là, les dimensions des éléments sont alignées.

#### Enveloppement

Par défaut, les éléments dans un conteneur flexbox sont maintenus sur une seule ligne, en les réduisant pour qu'ils s'adaptent au conteneur.

Pour forcer les éléments à se répartir sur plusieurs lignes, utilisez `flex-wrap: wrap`. Cela distribuera les éléments selon l'ordre défini dans `flex-direction`. Utilisez `flex-wrap: wrap-reverse` pour inverser cet ordre.

Une propriété raccourcie appelée `flex-flow` vous permet de spécifier `flex-direction` et `flex-wrap` en une seule ligne, en ajoutant la valeur `flex-direction` en premier, suivie de la valeur `flex-wrap`, par exemple : `flex-flow: row wrap`.

#### Propriétés qui s'appliquent à chaque élément individuel

Jusqu'à présent, nous avons vu les propriétés que vous pouvez appliquer au conteneur.

Les éléments individuels peuvent avoir une certaine indépendance et flexibilité, et vous pouvez modifier leur apparence en utilisant ces propriétés :

* `order`
* `align-self`
* `flex-grow`
* `flex-shrink`
* `flex-basis`
* `flex`

Voyons-les en détail.

#### Déplacer les éléments avant / après un autre en utilisant l'ordre

Les éléments sont ordonnés en fonction de l'ordre qui leur est assigné. Par défaut, chaque élément a l'ordre `0` et l'apparence dans le HTML détermine l'ordre final.

Vous pouvez remplacer cette propriété en utilisant `order` sur chaque élément séparé. C'est une propriété que vous définissez sur l'élément, pas sur le conteneur. Vous pouvez faire en sorte qu'un élément apparaisse avant tous les autres en définissant une valeur négative.

![Image](https://cdn-media-1.freecodecamp.org/images/B1sZQ2N0Faporf-B6QSoT9qlksFM0ul6Ova2)

#### Alignement vertical en utilisant align-self

Un élément peut choisir de **remplacer** le paramètre `align-items` du conteneur, en utilisant `**align-self**`, qui a les mêmes 5 valeurs possibles que `align-items` :

* `flex-start` : aligne en haut du conteneur.
* `flex-end` : aligne en bas du conteneur.
* `center` : aligne au centre vertical du conteneur.
* `baseline` : affiche à la ligne de base du conteneur.
* `stretch` : les éléments sont étirés pour s'adapter au conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/Vgk2OOS4KMX-ABecwTGMZGxu5HNOUsSCguNv)

#### Agrandir ou réduire un élément si nécessaire

**flex-grow**

La valeur par défaut pour tout élément est 0.

Si tous les éléments sont définis comme 1 et qu'un est défini comme 2, l'élément le plus grand prendra la place de deux éléments "1".

**flex-shrink**

La valeur par défaut pour tout élément est 1.

Si tous les éléments sont définis comme 1 et qu'un est défini comme 3, l'élément le plus grand se réduira 3x plus que les autres. Lorsqu'il y a moins d'espace disponible, il prendra 3x moins d'espace.

**flex-basis**

Si défini sur `auto`, il dimensionne un élément en fonction de sa largeur ou de sa hauteur, et ajoute de l'espace supplémentaire en fonction de la propriété `flex-grow`.

Si défini sur 0, il n'ajoute aucun espace supplémentaire pour l'élément lors du calcul de la mise en page.

Si vous spécifiez une valeur de pixel numérique, elle utilisera cette valeur comme valeur de longueur (la largeur ou la hauteur dépend de si c'est un élément de ligne ou de colonne)

**flex**

Cette propriété combine les 3 propriétés ci-dessus :

* `flex-grow`
* `flex-shrink`
* `flex-basis`

et fournit une syntaxe raccourcie : `flex: 0 1 auto`

### TABLEAUX

Les tableaux ont été grandement surutilisés dans le passé en CSS, car ils étaient l'un des seuls moyens dont nous disposions pour créer une mise en page de page élégante.

Aujourd'hui, avec Grid et Flexbox, nous pouvons ramener les tableaux à leur travail initial : styliser les tableaux.

Commençons par le HTML. Voici un tableau de base :

```html
<table>
  <thead>
    <tr>
      <th scope="col">Nom</th>
      <th scope="col">Âge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Flavio</th>
      <td>36</td>
    </tr>
    <tr>
      <th scope="row">Roger</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
```

Par défaut, il n'est pas très attrayant. Le navigateur fournit quelques styles standard, et c'est tout :

![Image](https://cdn-media-1.freecodecamp.org/images/cSv50H4eDfA17z4XhwXhlwgDCzfrtAkth840)

Nous pouvons utiliser CSS pour styliser tous les éléments du tableau, bien sûr.

Commençons par la bordure. Une belle bordure peut faire beaucoup.

Nous pouvons l'appliquer sur l'élément `table`, et sur les éléments intérieurs aussi, comme `th` et `td` :

```css
table, th, td {
  border: 1px solid #333;
}
```

Si nous l'associons à une marge, nous obtenons un beau résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/77EZWjHTyPL1-2BHjB6PtNKGxoefvaH8Ou0N)

Une chose courante avec les tableaux est la possibilité d'ajouter une couleur à une ligne, et une couleur différente à une autre ligne. Cela est possible en utilisant le sélecteur `:nth-child(odd)` ou `:nth-child(even)` :

```css
tbody tr:nth-child(odd) {
  background-color: #af47ff;
}
```

Cela nous donne :

![Image](https://cdn-media-1.freecodecamp.org/images/bgYEzQ0jzePRY8Z1QsjS8Wr33gzw8Hm2R0-o)

Si vous ajoutez `border-collapse: collapse;` à l'élément table, toutes les bordures sont fusionnées en une seule :

![Image](https://cdn-media-1.freecodecamp.org/images/YBEKBLgWtAy6VbpdnQCbpIzfWJYKvGPesyGA)

### CENTRAGE

Centrer les choses en CSS est une tâche très différente selon que vous devez centrer horizontalement ou verticalement.

Dans cet article, j'explique les scénarios les plus courants et comment les résoudre. Si une nouvelle solution est fournie par [Flexbox](https://flaviocopes.com/flexbox/), j'ignore les anciennes techniques car nous devons avancer, et Flexbox est supporté par les navigateurs depuis des années, y compris IE10.

### Centrer horizontalement

#### Texte

Le texte est très simple à centrer horizontalement en utilisant la propriété `text-align` définie sur `center` :

```css
p {
  text-align: center;
}
```

#### Blocs

La manière moderne de centrer n'importe quoi qui n'est pas du texte est d'utiliser Flexbox :

```css
#mysection {
  display: flex;
  justify-content: center;
}
```

n'importe quel élément à l'intérieur de `#mysection` sera centré horizontalement.

![Image](https://cdn-media-1.freecodecamp.org/images/poUby5NpYUt0D8ADmTgP6wWXhjj2PMjWuK4p)

Voici l'approche alternative si vous ne voulez pas utiliser Flexbox.

Tout ce qui n'est pas du texte peut être centré en appliquant une marge automatique à gauche et à droite, et en définissant la largeur de l'élément :

```css
section {
  margin: 0 auto;
  width: 50%;
}
```

le `margin: 0 auto;` ci-dessus est un raccourci pour :

```css
section {
  margin-top: 0;
  margin-bottom: 0;
  margin-left: auto;
  margin-right: auto;
}
```

N'oubliez pas de définir l'élément sur `display: block` s'il s'agit d'un élément en ligne.

### Centrer verticalement

Traditionnellement, cela a toujours été une tâche difficile. Flexbox nous offre maintenant un excellent moyen de le faire de la manière la plus simple possible :

```css
#mysection {
  display: flex;
  align-items: center;
}
```

n'importe quel élément à l'intérieur de `#mysection` sera centré verticalement.

![Image](https://cdn-media-1.freecodecamp.org/images/XOIWKiWU2zPe3VNje1LpiaHur6lJu4db8Cyp)

### Centrer à la fois verticalement et horizontalement

Les techniques Flexbox pour centrer verticalement et horizontalement peuvent être combinées pour centrer complètement un élément dans la page.

```css
#mysection {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/OtQEQ-F5AsSU0b49Oo5cGwoyLafxN05qmoLQ)

La même chose peut être faite en utilisant [CSS Grid](https://flaviocopes.com/css-grid/) :

```css
body {
  display: grid;
  place-items: center;
  height: 100vh;
}
```

### LISTES

Les listes sont une partie très importante de nombreuses pages web.

CSS peut les styliser en utilisant plusieurs propriétés.

`list-style-type` est utilisé pour définir un marqueur prédéfini à utiliser par la liste :

```css
li {
  list-style-type: square;
}
```

Nous avons beaucoup de valeurs possibles, que vous pouvez voir ici [https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type) avec des exemples de leur apparence. Certaines des plus populaires sont `disc`, `circle`, `square` et `none`.

`list-style-image` est utilisé pour utiliser un marqueur personnalisé lorsqu'un marqueur prédéfini n'est pas approprié :

```css
li {
  list-style-image: url(list-image.png);
}
```

`list-style-position` vous permet d'ajouter le marqueur `outside` (par défaut) ou `inside` du contenu de la liste, dans le flux de la page plutôt qu'à l'extérieur de celle-ci

```css
li {
  list-style-position: inside;
}
```

La propriété raccourcie `list-style` nous permet de spécifier toutes ces propriétés sur la même ligne :

```css
li {
  list-style: url(list-image.png) inside;
}
```

### REQUÊTES MÉDIA ET DESIGN RESPONSIVE

Dans cette section, nous allons d'abord introduire les types de médias et les descripteurs de fonctionnalités de médias, puis nous expliquerons les requêtes de médias.

#### Types de médias

Utilisés dans les requêtes de médias et les déclarations @import, les types de médias nous permettent de déterminer sur quel média un fichier CSS, ou un morceau de CSS, est chargé.

Nous avons les **types de médias** suivants

* `all` signifie tous les médias
* `print` utilisé lors de l'impression
* `screen` utilisé lorsque la page est présentée sur un écran
* `speech` utilisé pour les lecteurs d'écran

`screen` est le type par défaut.

Dans le passé, nous en avions plus, mais la plupart sont obsolètes car ils se sont avérés être des moyens inefficaces de déterminer les besoins des appareils.

Nous pouvons les utiliser dans les instructions @import comme ceci :

```css
@import url(myfile.css) screen;
@import url(myfile-print.css) print;
```

Nous pouvons charger un fichier CSS sur plusieurs types de médias en séparant chacun par une virgule :

```css
@import url(myfile.css) screen, print;
```

Le même principe s'applique à la balise `link` en HTML :

```html
<link rel="stylesheet" type="text/css" href="myfile.css" media="screen" />
<link rel="stylesheet" type="text/css" href="another.css" media="screen, print" />
```

Nous ne sommes pas limités à n'utiliser que les types de médias dans l'attribut `media` et dans la déclaration `@import`. Il y a plus.

#### Descripteurs de fonctionnalités de médias

Tout d'abord, introduisons les **descripteurs de fonctionnalités de médias**. Ce sont des mots-clés supplémentaires que nous pouvons ajouter à l'attribut `media` de `link` ou à la déclaration `@import`, pour exprimer plus de conditions sur le chargement du CSS.

Voici la liste de ceux-ci :

* `width`
* `height`
* `device-width`
* `device-height`
* `aspect-ratio`
* `device-aspect-ratio`
* `color`
* `color-index`
* `monochrome`
* `resolution`
* `orientation`
* `scan`
* `grid`

Chacun d'eux a un `min-` et `max-` correspondant, par exemple :

* `min-width`, `max-width`
* `min-device-width`, `max-device-width`

et ainsi de suite.

Certains d'entre eux acceptent une valeur de longueur qui peut être exprimée en `px` ou `rem` ou toute valeur de longueur. C'est le cas de `width`, `height`, `device-width`, `device-height`.

Par exemple :

```css
@import url(myfile.css) screen and (max-width: 800px);
```

Remarquez que nous enveloppons chaque bloc utilisant des descripteurs de fonctionnalités de médias entre parenthèses.

Certains acceptent une valeur fixe. `orientation`, utilisé pour détecter l'orientation de l'appareil, accepte `portrait` ou `landscape`.

Exemple :

```html
<link rel="stylesheet" type="text/css" href="myfile.css" media="screen and (orientation: portrait)" />
```

`scan`, utilisé pour déterminer le type d'écran, accepte `progressive` (pour les écrans modernes) ou `interlace` (pour les anciens appareils CRT).

D'autres veulent un entier.

Comme `color` qui inspecte le nombre de bits par composante de couleur utilisés par l'appareil. Très bas niveau, mais vous devez juste savoir qu'il est là pour votre usage (comme `grid`, `color-index`, `monochrome`).

`aspect-ratio` et `device-aspect-ratio` acceptent une valeur de ratio représentant le ratio largeur/hauteur du viewport, qui est exprimé comme une fraction.

Exemple :

```
@import url(myfile.css) screen and (aspect-ratio: 4/3);
```

`resolution` représente la densité de pixels de l'appareil, exprimée dans un [type de données de résolution](https://developer.mozilla.org/en-US/docs/Web/CSS/resolution) comme `dpi`.

Exemple :

```css
@import url(myfile.css) screen and (min-resolution: 100dpi);
```

#### Opérateurs logiques

Nous pouvons combiner des règles en utilisant `and` :

```html
<link rel="stylesheet" type="text/css" href="myfile.css" media="screen and (max-width: 800px)" />
```

Nous pouvons effectuer une opération logique de type "ou" en utilisant des virgules, qui combine plusieurs requêtes de médias :

```css
@import url(myfile.css) screen, print;
```

Nous pouvons utiliser `not` pour nier une requête de médias :

```css
@import url(myfile.css) not screen;
```

> _Important : `not` ne peut être utilisé que pour nier une requête de médias entière, donc il doit être placé au début de celle-ci (ou après une virgule)._

#### Requêtes de médias

Toutes ces règles que nous avons vues appliquées à @import ou à la balise `link` HTML peuvent également être appliquées à l'intérieur du CSS.

Vous devez les envelopper dans une structure `@media () {}`.

Exemple :

```css
@media screen and (max-width: 800px) {
  /* entrer un peu de CSS */
}
```

et c'est la base du **design responsive**.

Les requêtes de médias peuvent être assez complexes. Cet exemple applique le CSS uniquement s'il s'agit d'un appareil d'écran, la largeur est comprise entre 600 et 800 pixels, et l'orientation est paysage :

```css
@media screen and (max-width: 800px) and (min-width: 600px) and (orientation: landscape) {
  /* entrer un peu de CSS */
}
```

### REQUÊTES DE FONCTIONNALITÉS

Les requêtes de fonctionnalités sont une capacité récente et relativement inconnue de CSS, mais une capacité [bien supportée](https://caniuse.com/#feat=css-featurequeries).

Nous pouvons l'utiliser pour vérifier si une fonctionnalité est supportée par le navigateur en utilisant le mot-clé `@supports`.

Je pense que cela est particulièrement utile, au moment de la rédaction, pour vérifier si un navigateur supporte CSS grid, par exemple, ce qui peut être fait en utilisant :

```css
@supports (display: grid) {
  /* appliquer ce CSS */
}
```

Nous vérifions si le navigateur supporte la valeur `grid` pour la propriété `display`.

Nous pouvons utiliser `@supports` pour n'importe quelle propriété CSS, pour vérifier n'importe quelle valeur.

Nous pouvons également utiliser les opérateurs logiques `and`, `or` et `not` pour construire des requêtes de fonctionnalités complexes :

```css
@supports (display: grid) and (display: flex) {
  /* appliquer ce CSS */
}
```

### FILTRES

Les filtres permettent d'effectuer des opérations sur les éléments.

Des choses que vous faites normalement avec Photoshop ou d'autres logiciels de retouche photo, comme changer l'opacité ou la luminosité, et plus encore.

Vous utilisez la propriété `filter`. Voici un exemple appliqué sur une image, mais cette propriété peut être utilisée sur _n'importe quel_ élément :

```css
img {
  filter: <quelque chose>;
}
```

Vous pouvez utiliser diverses valeurs ici :

* `blur()`
* `brightness()`
* `contrast()`
* `drop-shadow()`
* `grayscale()`
* `hue-rotate()`
* `invert()`
* `opacity()`
* `sepia()`
* `saturate()`
* `url()`

Remarquez les parenthèses après chaque option, car elles nécessitent toutes un paramètre.

Par exemple :

```css
img {
  filter: opacity(0.5);
}
```

signifie que l'image sera 50 % transparente, car `opacity()` prend une valeur de 0 à 1, ou un pourcentage.

Vous pouvez également appliquer plusieurs filtres à la fois :

```css
img {
  filter: opacity(0.5) blur(2px);
}
```

Parlons maintenant de chaque filtre en détail.

#### `blur()`

Floute le contenu d'un élément. Vous lui passez une valeur, exprimée en `px` ou `em` ou `rem` qui sera utilisée pour déterminer le rayon de flou.

Exemple :

```css
img {
  filter: blur(4px);
}
```

#### `opacity()`

`opacity()` prend une valeur de 0 à 1, ou un pourcentage, et détermine la transparence de l'image en fonction de celle-ci.

`0`, ou `0%`, signifie totalement transparent. `1`, ou `100%`, ou plus, signifie totalement visible.

Exemple :

```css
img {
  filter: opacity(0.5);
}
```

CSS a également une propriété `opacity`. Cependant, `filter` peut être accéléré par le matériel, selon l'implémentation, donc ce devrait être la méthode préférée.

#### `drop-shadow()`

`drop-shadow()` affiche une ombre derrière l'élément, qui suit le canal alpha. Cela signifie que si vous avez une image transparente, vous obtenez une ombre appliquée à la forme de l'image, et non à la boîte de l'image. Si l'image n'a pas de canal alpha, l'ombre sera appliquée à toute la boîte de l'image.

Il accepte un minimum de 2 paramètres, jusqu'à 5 :

* _offset-x_ définit le décalage horizontal. Peut être négatif.
* _offset-y_ définit le décalage vertical. Peut être négatif.
* _blur-radius_, optionnel, définit le rayon de flou pour l'ombre. Il est par défaut à 0, pas de flou.
* _spread-radius_, optionnel, définit le rayon de propagation. Exprimé en `px`, `rem` ou `em`
* _color_, optionnel, définit la couleur de l'ombre.

Vous pouvez définir la couleur sans définir le rayon de propagation ou le rayon de flou. CSS comprend que la valeur est une couleur et non une valeur de longueur.

Exemple :

```css
img {
  filter: drop-shadow(10px 10px 5px orange);
}

img {
  filter: drop-shadow(10px 10px orange);
}

img {
  filter: drop-shadow(10px 10px 5px 5px #333);
}
```

#### `grayscale()`

Rend l'élément de couleur grise.

Vous passez une valeur de 0 à 1, ou de 0% à 100%, où 1 et 100% signifient complètement gris, et 0 ou 0% signifient que l'image n'est pas modifiée, et les couleurs d'origine restent.

Exemple :

```css
img {
  filter: grayscale(50%);
}
```

#### `sepia()`

Rend l'élément de couleur sépia.

Vous passez une valeur de 0 à 1, ou de 0% à 100%, où 1 et 100% signifient complètement sépia, et 0 ou 0% signifient que l'image n'est pas modifiée, et les couleurs d'origine restent.

Exemple :

```css
img {
  filter: sepia(50%);
}
```

#### `invert()`

Inverse les couleurs d'un élément. Inverser une couleur signifie chercher l'opposé d'une couleur dans la roue chromatique HSL. Cherchez simplement "roue chromatique" sur Google si vous n'avez aucune idée de ce que cela signifie. Par exemple, l'opposé du jaune est le bleu, l'opposé du rouge est le cyan. Chaque couleur a un opposé.

Vous passez un nombre, de 0 à 1 ou de 0% à 100%, qui détermine la quantité d'inversion. 1 ou 100% signifie une inversion totale, 0 ou 0% signifie aucune inversion.

0.5 ou 50% donnera toujours une couleur grise à 50%, car vous finissez toujours au milieu de la roue.

Exemple :

```css
img {
  filter: invert(50%);
}
```

#### `hue-rotate()`

La roue chromatique HSL est représentée en degrés. En utilisant `hue-rotate()`, vous pouvez faire tourner la couleur en utilisant une rotation positive ou négative.

La fonction accepte une valeur `deg`.

Exemple :

```css
img {
  filter: hue-rotate(90deg);
}
```

#### `brightness()`

Modifie la luminosité d'un élément.

0 ou 0% donne un élément totalement noir. 1 ou 100% donne une image inchangée.

Les valeurs supérieures à 1 ou 100% rendent l'image plus lumineuse jusqu'à atteindre un élément totalement blanc.

Exemple :

```css
img {
  filter: brightness(50%);
}
```

### `contrast()`

Modifie le contraste d'un élément.

0 ou 0% donne un élément totalement gris. 1 ou 100% donne une image inchangée.

Les valeurs supérieures à 1 ou 100% donnent plus de contraste.

Exemple :

```css
img {
  filter: contrast(150%);
}
```

#### `saturate()`

Modifie la saturation d'un élément.

0 ou 0% donne un élément totalement en niveaux de gris (avec moins de saturation). 1 ou 100% donne une image inchangée.

Les valeurs supérieures à 1 ou 100% donnent plus de saturation.

Exemple :

```css
img {
  filter: saturate();
}
```

#### `url()`

Ce filtre permet d'appliquer un filtre défini dans un fichier SVG. Vous pointez vers l'emplacement du fichier SVG.

Exemple :

```css
img {
  filter: url(filter.svg);
}
```

Les filtres SVG sont hors du cadre de cet article, mais vous pouvez en lire plus dans cet article de Smashing Magazine : [https://www.smashingmagazine.com/2015/05/why-the-svg-filter-is-awesome/](https://www.smashingmagazine.com/2015/05/why-the-svg-filter-is-awesome/)

### TRANSFORMATIONS

Les transformations permettent de translater, faire tourner, mettre à l'échelle et incliner les éléments, dans l'espace 2D ou 3D. Elles sont une fonctionnalité CSS très intéressante, surtout lorsqu'elles sont combinées avec des animations.

#### Transformations 2D

La propriété `transform` accepte ces fonctions :

* `translate()` pour déplacer les éléments
* `rotate()` pour faire tourner les éléments
* `scale()` pour mettre à l'échelle les éléments en taille
* `skew()` pour tordre ou incliner un élément
* `matrix()` une façon d'effectuer l'une des opérations ci-dessus en utilisant une matrice de 6 éléments, une syntaxe moins conviviale mais moins verbeuse

Nous avons également des fonctions spécifiques à l'axe :

* `translateX()` pour déplacer les éléments sur l'axe X
* `translateY()` pour déplacer les éléments sur l'axe Y
* `scaleX()` pour mettre à l'échelle les éléments en taille sur l'axe X
* `scaleY()` pour mettre à l'échelle les éléments en taille sur l'axe Y
* `skewX()` pour tordre ou incliner un élément sur l'axe X
* `skewY()` pour tordre ou incliner un élément sur l'axe Y

Voici un exemple de transformation qui modifie la largeur de l'élément `.box` par 2 (la duplique) et la hauteur par 0,5 (la réduit de moitié) :

```css
.box {
    transform: scale(2, 0.5);
}
```

`[transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin)` nous permet de définir l'origine (les coordonnées `(0, 0)`) pour la transformation, nous permettant de changer le centre de rotation.

#### Combinaison de plusieurs transformations

Vous pouvez combiner plusieurs transformations en séparant chaque fonction par un espace.

Par exemple :

```css
transform: rotateY(20deg) scaleX(3) translateY(100px);
```

#### Transformations 3D

Nous pouvons aller plus loin et déplacer nos éléments dans un espace 3D au lieu d'un espace 2D. Avec le 3D, nous ajoutons un autre axe, Z, qui ajoute de la profondeur à nos visuels.

En utilisant la propriété `perspective`, vous pouvez spécifier à quelle distance l'objet 3D se trouve de l'observateur.

Exemple :

```css
.3Delement {
  perspective: 100px;
}
```

`perspective-origin` détermine l'apparence de la position de l'observateur, comment nous regardons l'objet sur les axes X et Y.

Maintenant, nous pouvons utiliser des fonctions supplémentaires qui contrôlent l'axe Z, et qui s'ajoutent aux autres transformations des axes X et Y :

* `translateZ()`
* `rotateZ()`
* `scaleZ()`

et les raccourcis correspondants `translate3d()`, `rotate3d()` et `scale3d()` comme raccourcis pour utiliser les fonctions `translateX()`, `translateY()` et `translateZ()` et ainsi de suite.

Les transformations 3D sont un peu trop avancées pour ce manuel, mais sont un excellent sujet à explorer par vous-même.

### TRANSITIONS

Les transitions CSS sont le moyen le plus simple de créer une animation en CSS.

Dans une transition, vous changez la valeur d'une propriété, et vous dites à CSS de la changer lentement selon certains paramètres, vers un état final.

Les transitions CSS sont définies par ces propriétés :

![Image](https://cdn-media-1.freecodecamp.org/images/-84q2WYZR7Ojj24SC1gD4k8ZIRNGq2pXDfSo)

La propriété `transition` est un raccourci pratique :

```css
.container {
  transition: property
              duration
              timing-function
              delay;
}
```

#### Exemple d'une transition CSS

Ce code implémente une transition CSS :

```css
.one,
.three {
  background: rgba(142, 92, 205, .75);
  transition: background 1s ease-in;
}

.two,
.four {
  background: rgba(236, 252, 100, .75);
}

.circle:hover {
  background: rgba(142, 92, 205, .25); /* plus clair */
}
```

Voir l'exemple sur Glitch [https://flavio-css-transitions-example.glitch.me](https://flavio-css-transitions-example.glitch.me/)

Lorsque vous survolez les éléments `.one` et `.three`, les cercles violets, il y a une animation de transition qui facilite le changement de fond, tandis que les cercles jaunes ne le font pas, car ils n'ont pas la propriété `transition` définie.

#### Valeurs de la fonction de temporisation de la transition

`transition-timing-function` vous permet de spécifier la courbe d'accélération de la transition.

Il y a quelques valeurs simples que vous pouvez utiliser :

* `linear`
* `ease`
* `ease-in`
* `ease-out`
* `ease-in-out`

[Ce Glitch](https://flavio-css-transitions-easings.glitch.me/) montre comment celles-ci fonctionnent en pratique.

Vous pouvez créer une fonction de temporisation complètement personnalisée en utilisant [des courbes de Bézier cubiques](https://developer.mozilla.org/en-US/docs/Web/CSS/single-transition-timing-function). Cela est plutôt avancé, mais en gros, chacune de ces fonctions ci-dessus est construite en utilisant des courbes de Bézier. Nous avons des noms pratiques car ce sont des courbes courantes.

#### Transitions CSS dans les outils de développement du navigateur

Les outils de développement du navigateur offrent un excellent moyen de visualiser les transitions.

Ceci est Chrome :

![Image](https://cdn-media-1.freecodecamp.org/images/l6svCI9t6bLTsuniRuxjgwOnD9i1YSseno-f)

Ceci est Firefox :

![Image](https://cdn-media-1.freecodecamp.org/images/JYAWK9J6xuzeP2WVytUt8k64RUUCHl3UJmXC)

À partir de ces panneaux, vous pouvez éditer en direct la transition et expérimenter directement dans la page sans recharger votre code.

#### Quelles propriétés vous pouvez animer en utilisant les transitions CSS

Beaucoup ! Elles sont les mêmes que vous pouvez animer en utilisant les animations CSS, aussi.

Voici la liste complète :

* `background`
* `background-color`
* `background-position`
* `background-size`
* `border`
* `border-color`
* `border-width`
* `border-bottom`
* `border-bottom-color`
* `border-bottom-left-radius`
* `border-bottom-right-radius`
* `border-bottom-width`
* `border-left`
* `border-left-color`
* `border-left-width`
* `border-radius`
* `border-right`
* `border-right-color`
* `border-right-width`
* `border-spacing`
* `border-top`
* `border-top-color`
* `border-top-left-radius`
* `border-top-right-radius`
* `border-top-width`
* `bottom`
* `box-shadow`
* `caret-color`
* `clip`
* `color`
* `column-count`
* `column-gap`
* `column-rule`
* `column-rule-color`
* `column-rule-width`
* `column-width`
* `columns`
* `content`
* `filter`
* `flex`
* `flex-basis`
* `flex-grow`
* `flex-shrink`
* `font`
* `font-size`
* `font-size-adjust`
* `font-stretch`
* `font-weight`
* `grid-area`
* `grid-auto-columns`
* `grid-auto-flow`
* `grid-auto-rows`
* `grid-column-end`
* `grid-column-gap`
* `grid-column-start`
* `grid-column`
* `grid-gap`
* `grid-row-end`
* `grid-row-gap`
* `grid-row-start`
* `grid-row`
* `grid-template-areas`
* `grid-template-columns`
* `grid-template-rows`
* `grid-template`
* `grid`
* `height`
* `left`
* `letter-spacing`
* `line-height`
* `margin`
* `margin-bottom`
* `margin-left`
* `margin-right`
* `margin-top`
* `max-height`
* `max-width`
* `min-height`
* `min-width`
* `opacity`
* `order`
* `outline`
* `outline-color`
* `outline-offset`
* `outline-width`
* `padding`
* `padding-bottom`
* `padding-left`
* `padding-right`
* `padding-top`
* `perspective`
* `perspective-origin`
* `quotes`
* `right`
* `tab-size`
* `text-decoration`
* `text-decoration-color`
* `text-indent`
* `text-shadow`
* `top`
* `transform.`
* `vertical-align`
* `visibility`
* `width`
* `word-spacing`
* `z-index`

### ANIMATIONS

Les animations CSS sont un excellent moyen de créer des animations visuelles, non limitées à un seul mouvement comme les transitions CSS, mais beaucoup plus articulées.

Une animation est appliquée à un élément en utilisant la propriété `animation`.

```css
.container {
  animation: spin 10s linear infinite;
}
```

`spin` est le nom de l'animation, que nous devons définir séparément. Nous disons également à CSS de faire durer l'animation 10 secondes, de l'exécuter de manière linéaire (sans accélération ou différence de vitesse) et de la répéter indéfiniment.

Vous devez **définir comment votre animation fonctionne** en utilisant des **keyframes**. Exemple d'une animation qui fait tourner un élément :

```css
@keyframes spin {
  0% {
    transform: rotateZ(0);
  }
  100% {
    transform: rotateZ(360deg);
  }
}
```

À l'intérieur de la définition `@keyframes`, vous pouvez avoir autant de points de passage intermédiaires que vous le souhaitez.

Dans ce cas, nous instruisons CSS de faire en sorte que la propriété transform fasse tourner l'axe Z de 0 à 360 degrés, complétant ainsi la boucle complète.

Vous pouvez utiliser n'importe quelle transformation CSS ici.

Remarquez comment cela ne dicte rien sur l'intervalle temporel que l'animation doit prendre. Cela est défini lorsque vous l'utilisez via `animation`.

#### Un exemple d'animations CSS

Je veux dessiner quatre cercles, tous avec un point de départ en commun, tous à 90 degrés de distance les uns des autres.

```css
<div class="container">
  <div class="circle one"></div>
  <div class="circle two"></div>
  <div class="circle three"></div>
  <div class="circle four"></div>
</div>

body {
  display: grid;
  place-items: center;
  height: 100vh;
}

.circle {
  border-radius: 50%;
  left: calc(50% - 6.25em);
  top: calc(50% - 12.5em);
  transform-origin: 50% 12.5em;
  width: 12.5em;
  height: 12.5em;
  position: absolute;
  box-shadow: 0 1em 2em rgba(0, 0, 0, .5);
}

.one,
.three {
  background: rgba(142, 92, 205, .75);
}

.two,
.four {
  background: rgba(236, 252, 100, .75);
}

.one {
  transform: rotateZ(0);
}

.two {
  transform: rotateZ(90deg);
}

.three {
  transform: rotateZ(180deg);
}

.four {
  transform: rotateZ(-90deg);
}
```

Vous pouvez les voir dans ce Glitch : [https://flavio-css-circles.glitch.me](https://flavio-css-circles.glitch.me/)

Faisons tourner cette structure (tous les cercles ensemble). Pour ce faire, nous appliquons une animation sur le conteneur, et nous définissons cette animation comme une rotation de 360 degrés :

```css
@keyframes spin {
  0% {
    transform: rotateZ(0);
  }
  100% {
    transform: rotateZ(360deg);
  }
}

.container {
  animation: spin 10s linear infinite;
}
```

Voir sur [https://flavio-css-animations-tutorial.glitch.me](https://flavio-css-animations-tutorial.glitch.me/)

Vous pouvez ajouter plus de keyframes pour avoir des animations plus amusantes :

```css
@keyframes spin {
  0% {
    transform: rotateZ(0);
  }
  25% {
    transform: rotateZ(30deg);
  }
  50% {
    transform: rotateZ(270deg);
  }
  75% {
    transform: rotateZ(180deg);
  }
  100% {
    transform: rotateZ(360deg);
  }
}
```

Voir l'exemple sur [https://flavio-css-animations-four-steps.glitch.me](https://flavio-css-animations-four-steps.glitch.me/)

#### Les propriétés des animations CSS

Les animations CSS offrent de nombreux paramètres différents que vous pouvez ajuster :

![Image](https://cdn-media-1.freecodecamp.org/images/AurqyVJOCys9sUi4S6DtBlaxKGi6evJQhsbB)

La propriété `animation` est un raccourci pour toutes ces propriétés, dans cet ordre :

```css
.container {
  animation: name
             duration
             timing-function
             delay
             iteration-count
             direction
             fill-mode
             play-state;
}
```

Voici l'exemple que nous avons utilisé ci-dessus :

```css
.container {
  animation: spin 10s linear infinite;
}
```

#### Événements JavaScript pour les animations CSS

En utilisant JavaScript, vous pouvez écouter les événements suivants :

* `animationstart`
* `animationend`
* `animationiteration`

Faites attention avec `animationstart`, car si l'animation commence au chargement de la page, votre code JavaScript est toujours exécuté après que le CSS a été traité, donc l'animation est déjà démarrée et vous ne pouvez pas intercepter l'événement.

```js
const container = document.querySelector('.container')

container.addEventListener('animationstart', (e) => {
  //faire quelque chose
}, false)

container.addEventListener('animationend', (e) => {
  //faire quelque chose
}, false)

container.addEventListener('animationiteration', (e) => {
  //faire quelque chose
}, false)
```

#### Quelles propriétés vous pouvez animer en utilisant les animations CSS

Beaucoup ! Elles sont les mêmes que vous pouvez animer en utilisant les transitions CSS, aussi.

Voici la liste complète :

* `background`
* `background-color`
* `background-position`
* `background-size`
* `border`
* `border-color`
* `border-width`
* `border-bottom`
* `border-bottom-color`
* `border-bottom-left-radius`
* `border-bottom-right-radius`
* `border-bottom-width`
* `border-left`
* `border-left-color`
* `border-left-width`
* `border-radius`
* `border-right`
* `border-right-color`
* `border-right-width`
* `border-spacing`
* `border-top`
* `border-top-color`
* `border-top-left-radius`
* `border-top-right-radius`
* `border-top-width`
* `bottom`
* `box-shadow`
* `caret-color`
* `clip`
* `color`
* `column-count`
* `column-gap`
* `column-rule`
* `column-rule-color`
* `column-rule-width`
* `column-width`
* `columns`
* `content`
* `filter`
* `flex`
* `flex-basis`
* `flex-grow`
* `flex-shrink`
* `font`
* `font-size`
* `font-size-adjust`
* `font-stretch`
* `font-weight`
* `grid-area`
* `grid-auto-columns`
* `grid-auto-flow`
* `grid-auto-rows`
* `grid-column-end`
* `grid-column-gap`
* `grid-column-start`
* `grid-column`
* `grid-gap`
* `grid-row-end`
* `grid-row-gap`
* `grid-row-start`
* `grid-row`
* `grid-template-areas`
* `grid-template-columns`
* `grid-template-rows`
* `grid-template`
* `grid`
* `height`
* `left`
* `letter-spacing`
* `line-height`
* `margin`
* `margin-bottom`
* `margin-left`
* `margin-right`
* `margin-top`
* `max-height`
* `max-width`
* `min-height`
* `min-width`
* `opacity`
* `order`
* `outline`
* `outline-color`
* `outline-offset`
* `outline-width`
* `padding`
* `padding-bottom`
* `padding-left`
* `padding-right`
* `padding-top`
* `perspective`
* `perspective-origin`
* `quotes`
* `right`
* `tab-size`
* `text-decoration`
* `text-decoration-color`
* `text-indent`
* `text-shadow`
* `top`
* `transform.`
* `vertical-align`
* `visibility`
* `width`
* `word-spacing`
* `z-index`

### NORMALISATION CSS

La feuille de style par défaut du navigateur est l'ensemble des règles que les navigateurs doivent appliquer pour donner un style minimal aux éléments.

La plupart du temps, ces styles sont très utiles.

Puisque chaque navigateur a son propre ensemble, il est courant de trouver un terrain d'entente.

Plutôt que de supprimer tous les styles par défaut, comme le fait l'une des approches de **réinitialisation CSS**, le processus de normalisation supprime les incohérences entre les navigateurs, tout en conservant un ensemble de règles de base sur lequel vous pouvez compter.

Normalize.css [http://necolas.github.io/normalize.css](http://necolas.github.io/normalize.css) est la solution la plus couramment utilisée pour ce problème.

Vous devez charger le fichier CSS de normalisation avant tout autre CSS.

### GESTION DES ERREURS

CSS est résilient. Lorsqu'il trouve une erreur, il n'agit pas comme JavaScript qui fait ses valises et s'en va complètement, mettant fin à toutes les exécutions de script après avoir trouvé l'erreur.

CSS fait de son mieux pour faire ce que vous voulez.

Si une ligne contient une erreur, il la saute et passe à la ligne suivante sans aucune erreur.

Si vous oubliez le point-virgule sur une ligne :

```css
p {
  font-size: 20px
  color: black;
  border: 1px solid black;
}
```

la ligne avec l'erreur ET la suivante ne **seront pas** appliquées, mais la troisième règle sera appliquée avec succès sur la page. En gros, il analyse tout jusqu'à ce qu'il trouve un point-virgule, mais lorsqu'il l'atteint, la règle est maintenant `font-size: 20px color: black;`, qui est invalide, donc il la saute.

Parfois, il est difficile de réaliser qu'il y a une erreur quelque part, et où se trouve cette erreur, car le navigateur ne nous le dira pas.

C'est pourquoi des outils comme [CSS Lint](http://csslint.net/) existent.

### PRÉFIXES DE FOURNISSEURS

Les préfixes de fournisseurs sont l'un des moyens utilisés par les navigateurs pour donner aux développeurs CSS l'accès à des fonctionnalités plus récentes non encore considérées comme stables.

Avant de continuer, gardez à l'esprit que cette approche est en déclin de popularité. Les gens préfèrent maintenant utiliser des **drapeaux expérimentaux**, qui doivent être activés explicitement dans le navigateur de l'utilisateur.

Pourquoi ? Parce que les développeurs, au lieu de considérer les préfixes de fournisseurs comme un moyen de prévisualiser les fonctionnalités, les expédient parfois en production — une pratique considérée comme nuisible par le groupe de travail CSS.

Surtout parce qu'une fois que vous ajoutez un drapeau et que les développeurs commencent à l'utiliser en production, les navigateurs sont dans une mauvaise position s'ils réalisent que quelque chose doit changer. Avec les drapeaux, vous ne pouvez pas expédier une fonctionnalité à moins de pouvoir pousser tous vos visiteurs à activer ce drapeau dans leur navigateur (je plaisante, n'essayez pas).

Cela dit, voyons ce que sont les préfixes de fournisseurs.

Je me souviens spécifiquement d'eux pour avoir travaillé avec les transitions CSS dans le passé. Au lieu d'utiliser simplement la propriété `transition`, vous deviez faire ceci :

```css
.myClass {
    -webkit-transition: all 1s linear;
    -moz-transition: all 1s linear;
    -ms-transition: all 1s linear;
    -o-transition: all 1s linear;
    transition: all 1s linear;
}
```

Maintenant, vous utilisez simplement

```css
.myClass {
    transition: all 1s linear;
}
```

puisque la propriété est maintenant bien supportée par tous les navigateurs modernes.

Les préfixes utilisés sont :

* `-webkit-` (Chrome, Safari, iOS Safari / iOS WebView, Android)
* `-moz-` (Safari)
* `-ms-` (Edge, Internet Explorer)
* `-o-` (Opera, Opera Mini)

Puisque Opera est basé sur Chromium et que Edge le sera bientôt aussi, `-o-` et `-ms-` vont probablement bientôt tomber en désuétude. Mais comme nous l'avons dit, les préfixes de fournisseurs dans leur ensemble sont également en train de tomber en désuétude.

Écrire des préfixes est difficile, principalement à cause de l'incertitude. Avez-vous vraiment besoin d'un préfixe pour une propriété ? Plusieurs ressources en ligne sont également obsolètes, ce qui rend encore plus difficile de faire les choses correctement. Des projets comme [Autoprefixer](https://github.com/postcss/autoprefixer) peuvent automatiser le processus dans son intégralité sans que nous ayons besoin de découvrir si un préfixe est encore nécessaire, ou si la fonctionnalité est maintenant stable et le préfixe doit être abandonné. Il utilise les données de caniuse.com, un très bon site de référence pour tout ce qui concerne le support des navigateurs.

Si vous utilisez React ou Vue, des projets comme `create-react-app` et Vue CLI, deux façons courantes de commencer à construire une application, utilisent `autoprefixer` dès le départ, donc vous n'avez même pas à vous en soucier.

### CSS POUR L'IMPRESSION

Même si nous regardons de plus en plus nos écrans, l'impression est toujours une chose.

Même avec les articles de blog. Je me souviens d'une fois en 2009 où j'ai rencontré une personne qui m'a dit qu'elle faisait imprimer chaque article de blog que je publiais par son assistant personnel (oui, j'ai regardé fixement pendant un petit moment). Définitivement inattendu.

Mon cas d'utilisation principal pour l'impression est généralement l'impression en PDF. Je peux créer quelque chose dans le navigateur, et je veux le rendre disponible en PDF.

Les navigateurs rendent cela très facile, Chrome par défaut sur "Enregistrer" lors de l'impression d'un document et une imprimante n'est pas disponible, et Safari a un bouton dédié dans la barre de menu :

![Image](https://cdn-media-1.freecodecamp.org/images/bgA5gq1sJ4vzRx7inVg4skJLVgDggyhDjhmF)

#### CSS pour l'impression

Certaines choses courantes que vous pourriez vouloir faire lors de l'impression sont de masquer certaines parties du document, peut-être le pied de page, quelque chose dans l'en-tête, la barre latérale.

Peut-être voulez-vous utiliser une police différente pour l'impression, ce qui est tout à fait légitime.

Si vous avez un grand CSS pour l'impression, vous feriez mieux d'utiliser un fichier séparé pour celui-ci. Les navigateurs ne le téléchargeront que lors de l'impression :

```html
<link rel="stylesheet"
      src="print.css"
      type="text/css"
      media="print" />
```

#### CSS @media print

Une alternative à l'approche précédente est les requêtes de médias. Tout ce que vous ajoutez à l'intérieur de ce bloc :

```css
@media print {
  /* ... */
}
```

sera appliqué uniquement aux documents imprimés.

#### Liens

HTML est génial grâce aux liens. Il est appelé HyperText pour une bonne raison. Lors de l'impression, nous pouvons perdre beaucoup d'informations, selon le contenu.

CSS offre un excellent moyen de résoudre ce problème en modifiant le contenu, en ajoutant le lien après le texte de la balise `<a>`, en utilisant :

```css
@media print {
    a[href*='//']:after {
        content:" (" attr(href) ") ";
        color: $primary;
    }
}
```

Je cible `a[href*='//']` pour ne faire cela que pour les liens externes. Je peux avoir des liens internes à des fins de navigation et d'indexation interne, qui seraient inutiles dans la plupart de mes cas d'utilisation. Si vous voulez également que les liens internes soient imprimés, faites simplement :

```css
@media print {
    a:after {
        content:" (" attr(href) ") ";
        color: $primary;
    }
}
```

#### Marges de page

Vous pouvez ajouter des marges à chaque page. `cm` ou `in` est une bonne unité pour l'impression sur papier.

```css
@page {
    margin-top: 2cm;
    margin-bottom: 2cm;
    margin-left: 2cm;
    margin-right: 2cm;
}
```

`@page` peut également être utilisé pour cibler uniquement la première page, en utilisant `@page :first`, ou uniquement les pages de gauche et de droite en utilisant `@page :left` et `@page: right`.

#### Sauts de page

Vous pourriez vouloir ajouter un saut de page après certains éléments, ou avant eux. Utilisez `page-break-after` et `page-break-before` :

```css
.book-date {
    page-break-after: always;
}

.post-content {
    page-break-before: always;
}
```

Ces propriétés [acceptent une grande variété de valeurs](https://developer.mozilla.org/en-US/docs/Web/CSS/page-break-after).

#### Éviter de couper les images en deux

J'ai expérimenté cela avec Firefox : les images sont par défaut coupées en deux, et continuent sur la page suivante. Cela peut aussi arriver au texte.

Utilisez

```css
p {
  page-break-inside: avoid;
}
```

et enveloppez vos images dans une balise `p`. Cibler `img` directement n'a pas fonctionné dans mes tests.

Cela s'applique également à d'autres contenus, pas seulement aux images. Si vous remarquez que quelque chose est coupé lorsque vous ne le souhaitez pas, utilisez cette propriété.

#### Déboguer la présentation d'impression

Les outils de développement de Chrome offrent des moyens d'émuler la mise en page d'impression :

![Image](https://cdn-media-1.freecodecamp.org/images/-uiIs0O58DxJGuPKuMjjzg356Nq2On7GH7QI)

Une fois le panneau ouvert, changez l'émulation de rendu en `print` :

![Image](https://cdn-media-1.freecodecamp.org/images/XO5KBdEIBUtWLlIXwISJMN3GaehM9Gfd22K7)

### CONCLUSION

J'espère que cet article vous a aidé à vous mettre à niveau avec CSS et à obtenir un aperçu des principales fonctionnalités que vous pouvez utiliser pour styliser vos pages et applications. Je l'ai écrit pour vous aider à vous sentir à l'aise avec CSS et à vous mettre rapidement à niveau avec l'utilisation de cet outil génial qui vous permet de créer des designs époustouflants sur le Web, et j'espère avoir atteint cet objectif.

**[Cliquez ici pour obtenir une version PDF / ePub / Mobi de cet article à lire hors ligne](https://flaviocopes.com/page/css-handbook/)**

Flavio