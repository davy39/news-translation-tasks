---
title: Lien HTML – Comment insérer un lien vers un site web avec le code HREF
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T18:22:00.000Z'
originalURL: https://freecodecamp.org/news/html-link-code-how-to-insert-a-link-to-a-website-with-href-3
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd76c26e6787e098393e8a7.jpg
tags:
- name: HTML
  slug: html
- name: Website design
  slug: website-design
seo_title: Lien HTML – Comment insérer un lien vers un site web avec le code HREF
seo_desc: "By Dillion Megida\nA website is made up of of various pieces of information\
  \ that live in different sections and on different pages within the site itself.\
  \ \nYou can also find information relating to that site on pages that are on different\
  \ websites. \nA..."
---

Par Dillion Megida

Un site web est composé de diverses informations qui résident dans différentes sections et sur différentes pages au sein du site lui-même. 

Vous pouvez également trouver des informations relatives à ce site sur des pages qui se trouvent sur d'autres sites web. 

Toutes ces sections et pages sont liées ensemble en HTML en utilisant l'attribut `href`.

Dans cet article, nous examinerons le terme *Hyperlien*. Ensuite, nous apprendrons les différentes façons de créer des hyperliens, ce que fait `href`, et comment utiliser correctement l'attribut `href` pour lier des sections et des pages.

## Qu'est-ce que les hyperliens ?

En HTML, il existe diverses formes de liens. Dans les images, il y a l'attribut `src` pour "lier" la source d'une image. 

Pour les feuilles de style, il y a la balise `link` avec l'attribut `href` pour "lier" la source d'une feuille de style. 

Pour les balises d'ancrage, il y a l'attribut `href` pour "lier" la section ou la page référencée. Les liens d'ancrage sont également appelés hyperliens.

Lorsque l'utilisateur suit un hyperlien, il navigue vers cette page. Les hyperliens sont des éléments qui référencent un autre document, de sorte que lorsque l'utilisateur clique sur cet élément, il est dirigé vers le nouveau document.

## Quand utiliser les hyperliens

Comme indiqué ci-dessus, vous pouvez vouloir lier diverses pages (au sein de votre site web ou externement) ou des sections sur votre site web. 

Dans cet article, je vais mettre en évidence trois façons de créer des hyperliens. Ces différentes façons sont importantes à connaître car elles déterminent les valeurs de l'attribut `href`. 

D'accord, regardons maintenant ces trois différentes façons.

### 1. Lorsque vous voulez lier des sections d'une page

Vous pourriez utiliser cette méthode, par exemple, lorsque vous créez une page avec une table des matières.

Dans ce cas, vous ne voulez peut-être pas que vos lecteurs aient à faire défiler jusqu'à la dernière section. Il serait agréable qu'ils puissent simplement cliquer dessus dans la table des matières et que le navigateur les y emmène directement. 

Ce type de liaison se produit dans le même document et emmène simplement le lecteur vers différentes sections. Nous apprendrons comment créer un hyperlien pour ce cas d'utilisation lorsque nous apprendrons l'attribut `href`.

### 2. Lorsque vous voulez lier une autre page au sein d'un site web

Sur votre site, vous pouvez avoir une page d'accueil, une page à propos, une page de services et d'autres types de pages. Cette méthode aide les utilisateurs à naviguer d'une page à l'autre.

### 3. Lorsque vous voulez lier des pages externes

Parfois, votre site web peut ne pas contenir certaines informations et un autre site web peut les avoir. Dans de tels cas, vous pouvez vouloir référencer l'autre site web. 

Pour ce faire, vous créeriez un hyperlien externe qui dirige l'utilisateur vers l'autre site web.

Ce sont les trois principales façons de lier des pages. Voyons maintenant comment l'attribut `href` peut vous aider à les activer.

## Comment utiliser l'attribut `href`

L'attribut `href` est utilisé pour référencer un autre document. Vous pouvez le trouver sur les balises `link` et `anchor`.

L'attribut `href` est utilisé sur les balises d'ancrage (`a`) pour créer des hyperliens dans les sites web. La valeur de l'attribut contient l'URL vers laquelle pointe l'hyperlien. Vous pouvez l'utiliser comme ceci :

```html
<a href="URL">Hyperlien</a>
```

Cependant, les valeurs d'URL peuvent être différentes selon ce que vous pointez. Pour les trois façons que nous avons examinées précédemment, voyons comment vous pouvez utiliser `href`.

### 1. Comment utiliser `href` pour lier des sections au sein d'un document

Dans ce cas, la valeur sera l'`id` de l'élément qui commence la section. Cela signifie que nous aurons quelque chose comme ceci :

```html
<a href="#second-section">Aller à la deuxième section</a>
<!--
  Quelques éléments ici
 -->
<section id="second-section">
	<h2>Deuxième section</h2>
</section>
```

Lorsque l'hyperlien "Aller à la deuxième section" est cliqué, le navigateur fait défiler jusqu'à la section avec l'`id` associé. De plus, l'URL dans la barre d'URL du navigateur change. 

Par exemple, si l'URL précédente était `mysite.com`, la nouvelle URL sera `mysite.com#second-section`.

### 2. Comment utiliser `href` pour lier des pages au sein d'un site web

Pour utiliser `href` de cette manière, vous devez comprendre ce que sont les URL relatives et les URL absolues.

Les URL relatives sont des URL courtes qui pointent vers un document sur le même site web. C'est un peu comme, depuis l'endroit où vous êtes, comment arrivez-vous à cet autre endroit sur le même site web ? 

Cela contraste avec les URL absolues. Pour celles-ci, vous ne vous souciez pas de l'endroit où vous vous trouvez actuellement – vous fournissez les détails complets pour arriver à un autre endroit comme si vous partiez du début.

Pour les navigations entre les pages qui résident sur un site web, vous pouvez utiliser l'une de ces URL, mais les URL relatives sont couramment utilisées.

Supposons que vous êtes sur la page d'accueil et que vous voulez référencer la page à propos. Voici comment utiliser l'attribut `href` pour le faire :

```html
<a href='/a-propos' >Page à propos</a>
```

Depuis la page d'accueil (disons `mysite.com`), le lien ci-dessus naviguera vers `mysite.com/a-propos`.

Il y a quelque chose à noter concernant la barre oblique (`/`) avant le lien. Le `/` indique au navigateur d'ajouter le lien à la racine du site (qui est le domaine). Donc la racine est `mysite.com` et le lien est ajouté comme suit : `mysite.com/a-propos`.

Si la barre oblique était absente (`<a href='a-propos'>`), le navigateur remplacerait le chemin actuel par `/a-propos`.

Par exemple, si nous étions actuellement sur `mysite.com/projets/generateur`, et que nous avions les liens suivants :

```html
<a href='a-propos'>À propos 1</a>
<a href='/a-propos'>À propos 2</a>
```

"À propos 1" naviguerait vers `mysite.com/projets/a-propos` (en remplaçant le chemin actuel `/generateur`) et "À propos 2" naviguerait vers `mysite.com/a-propos`.

### 3. Comment utiliser `href` pour lier des pages sur un autre site web

Puisqu'il s'agit d'un autre site web, il n'y a aucun moyen d'utiliser des URL relatives. Pour cela, nous devons spécifier la source absolue du document que nous référençons.

Par exemple, supposons que nous sommes sur `mysite.com`, et que nous voulons référencer `google.com`, voici comment nous le ferions avec `href` :

```html
<a href='https://google.com'>Google</a>
```

Si nous avions seulement écrit `google.com`, le navigateur l'aurait traité comme une page au sein d'un site web, l'ajoutant ainsi à `mysite.com`.

## Conclusion

Dans cet article, nous avons vu comment l'attribut `href` nous permet de créer différents types de liens. Ces divers liens montrent les différentes façons dont les documents/pages peuvent être référencés au sein d'un site web.