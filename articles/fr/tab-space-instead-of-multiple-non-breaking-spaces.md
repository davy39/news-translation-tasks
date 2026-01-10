---
title: Pourquoi vous devriez utiliser l'espace de tabulation au lieu de plusieurs
  espaces insécables (nbsp) en HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T18:19:00.000Z'
originalURL: https://freecodecamp.org/news/tab-space-instead-of-multiple-non-breaking-spaces
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dbb740569d1a4ca3959.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Pourquoi vous devriez utiliser l'espace de tabulation au lieu de plusieurs
  espaces insécables (nbsp) en HTML
seo_desc: 'There are a number of ways to insert spaces in HTML. The easiest way is
  by simply adding spaces or multiple &nbsp; character entities before and after the
  target text. Of course, that isn''t the DRYest method.

  Instead, to keep your code easy to mainta...'
---

Il existe plusieurs façons d'insérer des espaces en HTML. La méthode la plus simple consiste à ajouter des espaces ou plusieurs entités de caractères `&nbsp;` avant et après le texte cible. Bien sûr, ce n'est pas la méthode la plus DRY.

Au lieu de cela, pour garder votre code facile à maintenir et réduire la répétition, vous pouvez utiliser les éléments `<span>` et `<pre>`, ainsi qu'un peu de CSS :

## **Utilisation de l'élément `<span>`**

Un exemple de la façon d'utiliser `<span>` pour contrôler l'espacement entre le texte peut être vu ci-dessous :

```html
<p>Bonjour mon nom est <span class="tab"> James</p>
```

Notez que les balises `<span>` sont auto-fermantes, ce qui signifie qu'elles n'ont pas besoin de `/>`.

Ensuite, vous pouvez utiliser un style externe ou interne pour donner à la classe `tab` certaines propriétés. Par exemple, le code suivant fonctionnera dans une feuille de style externe :

```css
.tab {
  padding-left: 2px;
}
```

Vous pouvez également donner à `<span>` certaines propriétés de style en ligne, comme montré ci-dessous.

Alternativement, vous pouvez donner à `<span>` les mêmes propriétés que les styles en ligne comme montré ci-dessous :

```html
<p>Bonjour mon nom est <span style="padding-left: 2px;"> James</p>
```

## Utilisation de l'élément `<pre>`

Pour une façon facile d'ajouter un espace de tabulation, il suffit d'envelopper votre texte dans des balises `<pre>`. Par exemple :

L'élément `<pre>` représente simplement du texte _préformaté_. En d'autres termes, tous les espaces ou tabulations dans le texte interne seront rendus. Par exemple :

```html
<pre>
function greeting() {
  console.log('Hello world!');
}
</pre>
```

Gardez simplement à l'esprit que tous les caractères de tabulation réels (et non un tas d'espaces qui ressemblent à des tabulations) que vous utilisez avec cette méthode peuvent apparaître ridiculement larges. Cela est dû au fait que la propriété `tab-size` pour l'élément `<pre>` est définie à 8 espaces par défaut.

Vous pouvez changer cela avec un peu de CSS :

```css
pre {
  tab-width: 2;
}
```

## Plus d'informations sur HTML :

Le langage de balisage hypertexte (HTML) est un langage de balisage utilisé pour construire des documents en ligne et est la base de la plupart des sites web aujourd'hui.

Un langage de balisage comme HTML nous permet de

* créer des liens vers d'autres documents,
* structurer le contenu de notre document, et
* attribuer du contexte et du sens au contenu de notre document.

Un document HTML a deux aspects. Il contient des informations structurées (balisage) et des liens texte (hypertexte) vers d'autres documents.

Nous structurons nos pages en utilisant des [éléments HTML](https://guide.freecodecamp.org/html#). Ce sont des constructions du langage fournissant une [structure](https://guide.freecodecamp.org/html#) et un [sens](https://guide.freecodecamp.org/html#) dans notre document pour le navigateur et les liens d'éléments vers d'autres documents à travers l'internet.

L'internet a été créé à l'origine pour stocker et présenter des documents statiques (inchangés). Les aspects de HTML discutés ci-dessus étaient parfaitement visibles dans ces documents qui manquaient de tout design et style. Ils présentaient des informations structurées contenant des liens vers d'autres documents.

HTML5 est la dernière version, ou spécification, de HTML. Le World Wide Web Consortium (W3C) est l'organisation qui développe les normes pour le World Wide Web, y compris celles pour HTML. À mesure que les pages web et les applications web deviennent plus complexes, le W3C met à jour les normes de HTML.

HTML5 introduit un ensemble de nouveaux éléments sémantiques. Bien que HTML aide à fournir du sens à notre document, ce n'est qu'avec l'introduction des [éléments sémantiques](https://guide.freecodecamp.org/html#) avec HTML5 que son potentiel a été pleinement connu.

## **Un exemple simple d'un document HTML**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Titre de la page</title>
</head>
<body>

  <h1>Mon premier titre</h1>
  <p>Mon premier paragraphe.</p>

</body>
</html>
```

!DOCTYPE html : Définit ce document comme étant HTML5

html : L'élément racine d'une page HTML

head : L'élément contient des méta-informations sur le document

title : L'élément spécifie un titre pour le document

body : L'élément contient le contenu visible de la page

h1 : L'élément définit un grand titre

p : L'élément définit un paragraphe

## Versions de HTML

Depuis les premiers jours du web, il y a eu de nombreuses versions de HTML

* HTML1991
* HTML 2.01995
* HTML 3.21997
* HTML 4.011999X
* HTML2000
* HTML52014

#### **Autres ressources**

* [Éléments HTML](https://guide.freecodecamp.org/html/elements)
* [HTML sémantique](https://guide.freecodecamp.org/html/html5-semantic-elements)
* [Attributs HTML](https://guide.freecodecamp.org/html/attributes)