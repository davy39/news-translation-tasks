---
title: Listes HTML – Exemples de listes ordonnées, non ordonnées et de définition
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-10-04T16:01:18.000Z'
originalURL: https://freecodecamp.org/news/html-lists-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Blue-And-White-Modern-Effective-Leadership-In-Business-Presentation.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Listes HTML – Exemples de listes ordonnées, non ordonnées et de définition
seo_desc: "Imagine you're creating an article with a list of recommendations or a\
  \ web page with a menu of options. How do you structure this information to make\
  \ it visually appealing and easy to navigate? \nThis is where HTML lists come to\
  \ the rescue. In this ar..."
---

Imaginez que vous créez un article avec une liste de recommandations ou une page web avec un menu d'options. Comment structurez-vous ces informations pour les rendre visuellement attrayantes et faciles à naviguer ?

C'est là que les listes HTML viennent à la rescousse. Dans cet article, nous allons plonger dans le monde des listes HTML et explorer comment elles peuvent vous aider à organiser et présenter votre contenu de manière efficace.

## Les bases des listes HTML

Les listes HTML se déclinent en trois catégories principales : les **listes non ordonnées**, les **listes ordonnées** et les **listes de définition**. Chaque type sert un objectif spécifique et peut être personnalisé pour s'adapter à vos besoins de design et de contenu.

### Comment créer des listes non ordonnées

Les listes non ordonnées sont parfaites pour présenter des éléments qui n'ont pas de séquence ou d'ordre particulier. Elles sont généralement affichées avec des puces, ce qui les distingue visuellement des listes ordonnées. Un exemple pourrait être une liste de courses.

Pour créer une liste non ordonnée, vous pouvez utiliser l'élément `<ul>` (unordered list) et imbriquer les éléments individuels de la liste dans des éléments `<li>` (list item) :

```html
<ul>
  <li>Élément 1</li>
  <li>Élément 2</li>
  <li>Élément 3</li>
</ul>
```

Ce code générera une simple liste non ordonnée comme ceci :

* Élément 1
* Élément 2
* Élément 3

Vous pouvez personnaliser davantage l'apparence des puces en utilisant CSS pour correspondre au style de votre site web.

### Comment créer des listes ordonnées

Les listes ordonnées, comme leur nom l'indique, sont utiles lorsque vous souhaitez présenter des éléments dans une séquence ou un ordre spécifique. Elles sont affichées avec des nombres ou des lettres par défaut, mais vous pouvez personnaliser le style de numérotation en utilisant CSS. Un exemple pourrait être une liste classée de vos films préférés.

Pour créer une liste ordonnée, utilisez l'élément `<ol>` (ordered list) et imbriquez les éléments de la liste dans des éléments `<li>` :

```html
<ol>
  <li>Premier élément</li>
  <li>Deuxième élément</li>
  <li>Troisième élément</li>
</ol>
```

Ce code produira une liste ordonnée comme ceci :

1. Premier élément
2. Deuxième élément
3. Troisième élément

Les listes ordonnées sont utiles pour créer des instructions étape par étape, classer des éléments, ou toute situation où un ordre spécifique compte.

### Comment créer des listes de définition

Les listes de définition sont conçues pour présenter des termes et leurs définitions correspondantes. Elles consistent en une liste de termes enfermés dans des éléments `<dt>` (definition term) et leurs définitions associées enfermées dans des éléments `<dd>` (definition description). Voici un exemple :

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language, utilisé pour structurer le contenu sur le web.</dd>
  
  <dt>CSS</dt>
  <dd>Cascading Style Sheets, utilisé pour styliser les documents web.</dd>
  
  <dt>JavaScript</dt>
  <dd>Un langage de programmation utilisé pour ajouter de l'interactivité aux pages web.</dd>
</dl>
```

Ce code créera une liste de définition comme ceci :

**HTML**  
HyperText Markup Language, utilisé pour structurer le contenu sur le web.

**CSS**  
Cascading Style Sheets, utilisé pour styliser les documents web.

**JavaScript**  
Un langage de programmation utilisé pour ajouter de l'interactivité aux pages web.

Les listes de définition sont particulièrement pratiques pour les glossaires et les dictionnaires, où vous devez associer des termes à leurs significations.

## Comment personnaliser les listes avec CSS

HTML fournit la structure de base pour les listes, mais pour les rendre visuellement attrayantes et adaptées au design de votre site web, vous pouvez appliquer des styles CSS. Voici quelques propriétés CSS courantes que vous pouvez utiliser pour personnaliser les listes :

### Changer le style des puces ou des nombres

Pour changer le style des puces dans les listes non ordonnées ou le style de numérotation dans les listes ordonnées, vous pouvez utiliser la propriété `list-style-type`. Par exemple, pour utiliser des puces carrées dans une liste non ordonnée, vous pouvez ajouter la règle CSS suivante :

```css
ul {
  list-style-type: square;
}
```

Avec ce CSS appliqué, la liste non ordonnée ressemblera à ceci :

<ul style="list-style: none;">
  <li>■ Élément 1</li>
  <li>■ Élément 2</li>
  <li>■ Élément 3</li>
</ul>

### Ajouter des marges et des espacements

Vous pouvez contrôler l'espacement autour des éléments de la liste en ajustant les propriétés `margin` et `padding`. Par exemple, vous pouvez ajouter de l'espace entre les éléments de la liste comme ceci :

```css
li {
  margin-bottom: 10px;
}
```

Avec cette règle CSS, les éléments de la liste auront un espace supplémentaire entre eux, rendant la liste plus lisible.

### Styliser les éléments de la liste

Vous pouvez styliser les éléments individuels de la liste différemment en les ciblant directement avec CSS. Par exemple, vous pouvez changer la couleur des éléments de la liste lorsque les utilisateurs les survolent :

```css
li:hover {
  color: blue;
}
```

Avec ce CSS, les éléments de la liste changeront de couleur en bleu lorsque l'utilisateur les survolera, fournissant un retour visuel.

### Créer des icônes personnalisées

Si vous souhaitez utiliser des icônes personnalisées au lieu des puces par défaut pour les listes non ordonnées, vous pouvez y parvenir avec CSS en utilisant le pseudo-élément `::before`. Cela vous permet d'ajouter du contenu personnalisé avant chaque élément de la liste. Voici un exemple de la façon dont vous pouvez utiliser une icône de coche personnalisée :

```css
ul {
  list-style: none; /* Supprimer les puces par défaut */
}

li::before {
  content: "\2714"; /* Symbole de coche Unicode */
  margin-right: 5px; /* Ajouter un espacement entre l'icône et le texte */
}
```

Avec ce CSS appliqué, la liste non ordonnée aura des icônes de coche personnalisées avant chaque élément, comme ceci :

✓ Élément 1  
✓ Élément 2  
✓ Élément 3

## Comment rendre les listes plus accessibles

Il est essentiel de prendre en compte l'accessibilité lors de la conception de listes. Une sémantique HTML appropriée et CSS peuvent rendre les listes plus accessibles aux lecteurs d'écran et autres technologies d'assistance.

### Éléments sémantiques :

Vous voudrez vous assurer d'utiliser correctement les éléments sémantiques pour fournir un contexte aux utilisateurs qui dépendent des lecteurs d'écran. Par exemple :

```html
<ol>
  <li><strong>Étape 1 :</strong> Préparez vos ingrédients</li>
  <li><strong>Étape 2 :</strong> Préchauffez le four à 350°F</li>
  <li><strong>Étape 3 :</strong> Mélangez les ingrédients secs</li>
</ol>
```

Dans cette liste ordonnée, les éléments `<strong>` sont utilisés dans les éléments de la liste pour mettre en évidence les étapes importantes. Cela non seulement rend la liste plus visuellement attrayante, mais améliore également la compréhension du contenu pour les lecteurs d'écran.

### Rôles et étiquettes ARIA :

Pour des listes plus complexes ou lorsque des informations d'accessibilité supplémentaires sont nécessaires, vous pouvez utiliser les attributs ARIA (Accessible Rich Internet Applications). Par exemple :

```html
<ul role="list" aria-label="Fonctionnalités">
  <li role="listitem">Design réactif</li>
  <li role="listitem">Accessibilité</li>
  <li role="listitem">Compatibilité multi-navigateurs</li>
</ul>
```

Dans cette liste non ordonnée, l'attribut `role` est défini sur "list" pour indiquer qu'il s'agit d'une liste, et l'attribut `aria-label` fournit une étiquette pour la liste. Ces attributs aident les lecteurs d'écran à interpréter et à transmettre correctement le but et le contenu de la liste.

## Conclusion

Intégrer des listes HTML dans votre contenu web est un moyen puissant d'organiser les informations, de créer des interfaces engageantes et d'améliorer les expériences utilisateur.

En comprenant les différents types de listes – listes non ordonnées, ordonnées et de définition – et en sachant comment les styliser avec CSS, vous avez les outils pour rendre votre contenu plus visuellement attrayant et convivial.

Incorporez des listes dans vos documents HTML de manière judicieuse, en tenant compte à la fois du design et de l'accessibilité. Utilisez CSS pour affiner leur apparence afin de les aligner sur le style de votre site web, et assurez-vous que tout le monde, quelles que soient ses capacités, peut naviguer dans votre contenu sans effort.

N'oubliez pas, les listes sont plus que de simples puces ou nombres. Elles sont une pierre angulaire de la conception web efficace et de la communication.

## Passez à la pratique

Maintenant que vous avez appris à propos des listes HTML, pourquoi ne pas essayer de créer vos propres listes dans un document HTML ? Expérimentez avec différents styles et voyez comment CSS peut transformer l'apparence de vos listes. La pratique est la clé pour maîtriser cette compétence essentielle en développement web.