---
title: Comment utiliser les éléments HTML – Exemple de balises d'en-tête, de paragraphes
  et de mise en forme de texte
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-09-26T18:02:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-elements
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Pink-Minimalist-Digital-Marketing-Presentation.png
tags:
- name: beginner
  slug: beginner
- name: HTML
  slug: html
seo_title: Comment utiliser les éléments HTML – Exemple de balises d'en-tête, de paragraphes
  et de mise en forme de texte
seo_desc: HTML, which stands for HyperText Markup Language, is the standard markup
  language used to create webpages. HTML provides a structured way to organize content
  on a webpage, allowing web developers to present text and media in a clear and meaningful
  wa...
---

HTML, qui signifie HyperText Markup Language, est le langage de balisage standard utilisé pour créer des pages web. HTML offre une manière structurée d'organiser le contenu sur une page web, permettant aux développeurs web de présenter du texte et des médias de manière claire et significative.

Dans cet article, nous explorerons trois éléments fondamentaux de HTML : les en-têtes, les paragraphes et les éléments de mise en forme de texte, et nous apprendrons comment ils jouent un rôle crucial dans la présentation du contenu web.

## Comment utiliser les éléments HTML

Comprendre les éléments HTML est fondamental pour toute personne intéressée par le développement web. HTML repose sur des éléments comme blocs de construction des pages web. Chaque élément a un but et une structure spécifiques, contribuant à la mise en page et à la fonctionnalité globale d'une page web.

Les éléments peuvent aller de composants de base comme les en-têtes, les paragraphes et les éléments de mise en forme de texte, à des éléments plus complexes tels que les liens, les formulaires, les tableaux et les intégrations multimédias.

Apprendre à utiliser ces éléments, leurs attributs, et le bon imbrication et hiérarchie est essentiel pour créer un contenu web bien structuré, accessible et visuellement attrayant. Continuons et discutons de certains éléments HTML plus en détail.

### Comment structurer le contenu avec les en-têtes en HTML

Les en-têtes en HTML servent à structurer le contenu. Ils jouent un rôle vital dans l'organisation et la catégorisation de l'information, la rendant plus compréhensible pour les utilisateurs humains et les algorithmes des moteurs de recherche.

HTML offre un total de six niveaux hiérarchiques d'en-têtes, allant de `<h1>` à `<h6>`, chacun ayant une signification unique. `<h1>` est le niveau le plus élevé, généralement utilisé pour le titre principal ou la section primaire d'une page web, tandis que `<h6>` représente le niveau le plus bas, généralement réservé aux sous-sous-sections ou aux détails mineurs dans le contenu.

En utilisant ces balises d'en-tête de manière réfléchie et hiérarchique, les développeurs web peuvent créer une hiérarchie visuelle et structurelle qui guide les lecteurs à travers le flux et l'importance du contenu, facilitant une meilleure compréhension et navigation. Des en-têtes correctement structurés améliorent également l'accessibilité du contenu web, car ils fournissent aux lecteurs d'écran des indices vitaux sur la structure et la hiérarchie du contenu.

Voici un exemple de l'utilisation des en-têtes :

```html
<!DOCTYPE html>
<html>
<head>
    <title>En-têtes HTML</title>
</head>
<body>
    <h1>En-tête principal</h1>
    <p>Ceci est du contenu sous l'en-tête principal.</p>
    
    <h2>Sous-titre</h2>
    <p>Plus de contenu sous le sous-titre.</p>
</body>
</html>
```

Dans cet exemple, nous avons un `<h1>` pour l'en-tête principal et un `<h2>` pour le sous-titre. Cette hiérarchie aide les moteurs de recherche et les lecteurs d'écran à comprendre la structure du contenu, le rendant plus accessible et optimisé pour le référencement.

### Conseils et bonnes pratiques pour utiliser les en-têtes en HTML

Voici quelques conseils à garder à l'esprit lors de l'utilisation des en-têtes en HTML :

**Utilisez les en-têtes de manière séquentielle** : Il est essentiel d'utiliser les en-têtes dans l'ordre séquentiel. Commencez par un `<h1>` pour le titre principal ou la section, suivi de `<h2>` pour les sous-sections, `<h3>` pour les sous-sous-sections, et ainsi de suite. Cela aide à maintenir une structure logique et organisée.

**Évitez de sauter des niveaux** : Ne sautez pas de niveaux d'en-têtes. Par exemple, n'utilisez pas `<h1>` suivi de `<h3>` sans un `<h2>` entre les deux. Sauter des niveaux peut confondre les utilisateurs et les moteurs de recherche.

**Ne surutilisez pas `<h1>`** : Bien que `<h1>` soit l'en-tête de niveau le plus élevé et doive représenter le sujet principal de la page, évitez de l'utiliser plusieurs fois sur une seule page. Il est préférable de l'utiliser une seule fois pour le titre principal.

**Utilisez des en-têtes sémantiques** : Choisissez des en-têtes qui représentent sémantiquement le contenu qu'ils englobent. Par exemple, utilisez `<h3>` pour les sous-titres qui sont moins importants que le sujet principal mais plus importants que les sous-sections.

**Pensez à l'accessibilité** : Assurez-vous que vos en-têtes sont significatifs pour les utilisateurs qui dépendent des lecteurs d'écran. Ils doivent fournir un aperçu clair de la structure du contenu. Évitez d'utiliser les en-têtes uniquement à des fins de style.

**Testez la réactivité** : Vérifiez comment vos en-têtes apparaissent sur différents appareils et tailles d'écran. Assurez-vous qu'ils restent lisibles et maintiennent la structure souhaitée.

### Comment organiser le texte avec les paragraphes en HTML

Les paragraphes en HTML, représentés par l'élément `<p>`, servent de moyen fondamental pour organiser le contenu textuel sur les pages web. Ils sont utilisés pour regrouper du texte lié. En enveloppant le texte dans des balises `<p>`, vous indiquez que ce contenu forme une unité cohésive.

Ces balises jouent un rôle crucial dans l'amélioration de la lisibilité et de la compréhension des informations présentées. En encapsulant le texte dans des balises `<p>`, les développeurs web signalent aux navigateurs et aux lecteurs que le contenu enfermé est une unité d'information cohérente et autonome.

Cette approche structurée non seulement sépare les différentes idées ou sujets, mais fournit également un espacement naturel et des sauts de ligne avant et après chaque paragraphe, assurant une mise en page propre et visuellement attrayante.

Que vous rédigez des articles, des descriptions ou des explications, l'utilisation des éléments `<p>` aide à maintenir un flux de texte logique et organisé. Cela contribue finalement à une expérience web plus conviviale et accessible. Les paragraphes ajoutent automatiquement un espacement avant et après le texte qu'ils contiennent, rendant chacun visuellement distinguable du contenu environnant.

Voici un exemple de l'utilisation des paragraphes :

```html
<p>Ceci est un paragraphe de texte. Il peut contenir plusieurs phrases.</p>
<p>Un autre paragraphe ici, gardant le contenu organisé.</p>
```

_Résultat :_

<p>Ceci est un paragraphe de texte. Il peut contenir plusieurs phrases.</p>
<p>Un autre paragraphe ici, gardant le contenu organisé.</p>

### Conseils et bonnes pratiques pour utiliser les paragraphes en HTML

**Utilisez pour le contenu textuel** : Utilisez les éléments `<p>` pour le contenu textuel, y compris le texte brut, les articles, les descriptions, et plus encore. Cela aide à maintenir la lisibilité et sépare les différentes idées ou sujets.

**Évitez les sauts de ligne excessifs** : N'utilisez pas plusieurs éléments `<p>` avec seulement quelques mots chacun. Si le texte appartient logiquement ensemble, gardez-le dans un seul paragraphe.

**Maintenez une mise en forme cohérente** : Gardez la mise en forme des paragraphes cohérente sur tout votre site web. Cela inclut un espacement de ligne cohérent, une taille de police et un alignement de texte.

**Évitez d'utiliser `<p>` pour les en-têtes** : Bien que les éléments `<p>` soient pour le contenu textuel, évitez de les utiliser pour simuler des en-têtes. Utilisez les balises d'en-tête `<h1>` à `<h6>` pour les en-têtes à la place.

**Utilisez un balisage sémantique** : Lorsque vous utilisez des paragraphes, assurez-vous qu'ils transmettent le sens voulu du contenu. Par exemple, utilisez des paragraphes pour le texte d'introduction, les explications ou le contenu principal.

**Vérifiez la lisibilité sur mobile** : Assurez-vous que les paragraphes sont lisibles sur les appareils mobiles sans défilement horizontal excessif ou zoom.

### Comment améliorer la lisibilité avec les éléments de mise en forme de texte en HTML

HTML fournit divers éléments pour la mise en forme de texte afin d'améliorer la lisibilité et l'attrait visuel de votre contenu. Ces éléments de mise en forme fournissent à la fois des améliorations esthétiques et une signification sémantique à votre texte, le rendant plus engageant et accessible à votre audience.

Voici quelques-uns des éléments de mise en forme en HTML :

#### Comment utiliser les éléments de mise en forme en gras et en italique

Vous pouvez mettre du texte en **gras** en utilisant l'élément `<b>` ou en _italique_ en utilisant l'élément `<em>`.

```html
<p>Ce texte est en <b>gras</b>, et ce texte est en <em>italique</em>.</p>
```

Résultat :

<p>Ce texte est en <b>gras</b>, et ce texte est en <em>italique</em>.</p>

Cependant, il est essentiel de noter que lorsque vous mettez en emphase du texte pour des raisons sémantiques, il est généralement préférable d'utiliser l'élément `<strong>` pour fournir à la fois un style visuel et une signification sémantique. Utilisez `<b>` lorsque le but principal est simplement de mettre le texte en gras pour des raisons stylistiques.

#### Comment utiliser les éléments de mise en forme en souligné et en barré

Le texte peut également être souligné en utilisant l'élément `<u>`, et vous pouvez barrer le texte en utilisant l'élément `<s>` ou `<strike>` (obsolète en HTML5 mais toujours largement supporté).

```html
<p>Ce texte est <u>souligné</u>, et ce texte est <s>barré</s>.</p>
```

Résultat :

<p>Ce texte est <u>souligné</u>, et ce texte est <s>barré</s>.</p>

#### Comment utiliser les éléments de mise en forme en exposant et en indice

Le texte en exposant et en indice peut être réalisé avec les éléments `<sup>` et `<sub>`, respectivement.

```html
<p>L'eau est H<sub>2</sub>O, et E=mc<sup>2</sup>.</p>
```

Résultat :

<p>L'eau est H<sub>2</sub>O, et E=mc<sup>2</sup>.</p>

#### Comment utiliser les éléments de code et de saisie clavier

Pour afficher du code ou des entrées clavier, vous pouvez utiliser les éléments `<code>` et `<kbd>`.

```html
<p>Pour ouvrir un fichier dans le terminal, tapez <code>cd dossier</code>. Pour enregistrer, appuyez sur <kbd>Ctrl + S</kbd>.</p>
```

<p>Pour ouvrir un fichier dans le terminal, tapez <code>cd dossier</code>. Pour enregistrer, appuyez sur <kbd>Ctrl + S</kbd>.</p>

### Conseils et bonnes pratiques pour utiliser les éléments de mise en forme de texte en HTML

**Utilisez la mise en forme avec parcimonie** : Bien que la mise en forme de texte puisse rendre le contenu visuellement attrayant, ne faites pas de l'excès. Une utilisation excessive de gras, d'italique ou d'autres éléments de mise en forme peut rendre la page encombrée et distraire les lecteurs du message prévu.

**Maintenez la lisibilité** : L'objectif principal de la mise en forme de texte est d'améliorer la lisibilité. Assurez-vous que le texte mis en forme reste lisible et ne fatigue pas les yeux du lecteur.

**Combinez les mises en forme** : Combinez différents éléments de mise en forme lorsque nécessaire. Par exemple, vous pouvez utiliser `<strong>` pour l'emphase dans un paragraphe qui est déjà en italique en utilisant `<em>`.

**Signification sémantique** : Utilisez les éléments de mise en forme pour transmettre une signification sémantique. Par exemple, utilisez `<em>` pour mettre en emphase du texte et `<strong>` pour indiquer une forte importance.

**Utilisez CSS pour le style** : Bien que HTML fournisse une mise en forme de texte de base, CSS (Cascading Style Sheets) est la méthode préférée pour styliser le contenu web. CSS vous donne plus de contrôle sur les polices, les couleurs et l'espacement.

Ces éléments de mise en forme de texte fournissent non seulement une amélioration visuelle, mais aussi une signification sémantique à votre contenu, ce qui peut être important pour les lecteurs d'écran et l'optimisation pour les moteurs de recherche.

## Conclusion

Les éléments HTML comme les en-têtes, les paragraphes et les balises de mise en forme de texte sont des outils essentiels pour structurer et présenter le contenu sur le web. Ils fournissent clarté, hiérarchie et lisibilité à vos pages web, les rendant accessibles aux humains et aux machines.

Alors que vous plongez plus profondément dans le développement web, maîtriser ces éléments fondamentaux sera crucial pour créer des sites web bien structurés et conviviaux. N'oubliez pas de suivre les bonnes pratiques pour vous assurer que votre contenu HTML est non seulement fonctionnel, mais aussi visuellement attrayant et accessible à un large éventail d'utilisateurs.

### Ressources d'apprentissage recommandées

[La certification Responsive Web Design de freeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/)

[Le manuel HTML pour débutants](https://www.freecodecamp.org/news/the-html-handbook/)

[Introduction à HTML et au codage – Cours vidéo pour débutants](https://www.freecodecamp.org/news/html-coding-introduction-course-for-beginners/)