---
title: Comment utiliser les attributs HTML pour rendre vos sites web et applications
  plus accessibles
subtitle: ''
author: Elizabeth Lola
co_authors: []
series: null
date: '2024-09-06T20:04:11.283Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-attributes-to-make-your-websites-and-apps-more-accessible
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725281991044/7edb0d70-c31e-4a41-bc24-232c75d0fae3.jpeg
tags:
- name: HTML
  slug: html
- name: a11y
  slug: a11y
- name: aria
  slug: aria
- name: Accessibility
  slug: accessibility
seo_title: Comment utiliser les attributs HTML pour rendre vos sites web et applications
  plus accessibles
seo_desc: 'Have you ever used an attribute in HTML without fully understanding its
  purpose? You''re not alone! Over time, I''ve dug into the meaning behind many HTML
  attributes, especially those that are crucial for accessibility.

  In this in-depth tutorial, I''ll ...'
---

Avez-vous déjà utilisé un attribut en HTML sans comprendre pleinement son but ? Vous n'êtes pas seul ! Au fil du temps, j'ai creusé la signification de nombreux attributs HTML, en particulier ceux qui sont cruciaux pour l'accessibilité.

Dans ce tutoriel approfondi, je vais décortiquer certains attributs HTML clés qui améliorent l'accessibilité, en expliquant ce qu'ils font et quand les utiliser efficacement.

## Prérequis

Pour suivre ce tutoriel, vous devriez avoir une compréhension de base du HTML et un peu de connaissances en JavaScript également.

## Table des matières

1. [Que sont les attributs ARIA ?](#heading-que-sont-les-attributs-aria)
    
2. [L'attribut `alt`](#heading-lattribut-alt)
    
3. [L'attribut `aria-label`](#heading-lattribut-aria-label)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-label`](#heading-bonnes-pratiques-pour-lutilisation-daria-label)
        
4. [L'attribut `aria-labelledby`](#heading-lattribut-aria-labelledby)
    
    * [En quoi `aria-label` est-il différent de `aria-labelledby` ?](#heading-en-quoi-aria-label-est-il-different-de-aria-labelledby)
        
    * [Bonnes pratiques pour l'utilisation d' `aria-labelledby`](#heading-bonnes-pratiques-pour-lutilisation-daria-labelledby)
        
5. [L'attribut `aria-describedby`](#heading-lattribut-aria-describedby)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-describedby`](#heading-bonnes-pratiques-pour-lutilisation-daria-describedby)
        
6. [L'attribut `role`](#heading-lattribut-role)
    
    * [Valeurs de `role` courantes](#heading-valeurs-de-role-courantes)
        
    * [Bonnes pratiques pour l'utilisation de l'attribut `role`](#heading-bonnes-pratiques-pour-lutilisation-de-lattribut-role)
        
7. [L'attribut `aria-controls`](#heading-lattribut-aria-controls)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-controls`](#heading-bonnes-pratiques-pour-lutilisation-daria-controls)
        
8. [L'attribut `aria-selected`](#heading-lattribut-aria-selected)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-selected`](#heading-bonnes-pratiques-pour-lutilisation-daria-selected)
        
9. [L'attribut `tabindex`](#heading-lattribut-tabindex)
    
    * [Valeurs possibles de `tabindex`](#heading-valeurs-possibles-de-tabindex)
        
    * [Bonnes pratiques pour l'utilisation de `tabindex`](#heading-bonnes-pratiques-pour-lutilisation-de-tabindex)
        
10. [L'attribut `title`](#heading-lattribut-title)
    
    * [Problèmes d'accessibilité liés à `title`](#heading-problemes-daccessibilite-lies-a-lattribut-title)
        
    * [Bonnes pratiques pour l'utilisation de l'attribut `title`](#heading-bonnes-pratiques-pour-lutilisation-de-lattribut-title)
        
11. [Utiliser l'attribut `for` dans `label`](#heading-utilisation-de-lattribut-for-dans-label)
    
    * [Bonnes pratiques pour l'utilisation de l'attribut `for`](#heading-bonnes-pratiques-pour-lutilisation-de-lattribut-for)
        
12. [L'attribut `scope`](#heading-lattribut-scope)
    
    * [Valeurs possibles de `scope`](#heading-valeurs-possibles-de-scope)
        
    * [Bonnes pratiques pour l'utilisation de `scope`](#heading-bonnes-pratiques-pour-lutilisation-de-lattribut-scope)
        
13. [L'attribut `aria-hidden`](#heading-lattribut-aria-hidden)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-hidden`](#heading-bonnes-pratiques-pour-lutilisation-daria-hidden)
        
14. [L'attribut `inert`](#heading-lattribut-inert)
    
    * [Bonnes pratiques pour l'utilisation d' `inert`](#heading-bonnes-pratiques-pour-lutilisation-de-lattribut-inert)
        
15. [L'attribut `aria-live`](#heading-lattribut-aria-live)
    
    * [Valeurs possibles pour `aria-live`](#heading-valeurs-possibles-pour-aria-live)
        
    * [Bonnes pratiques pour l'utilisation d' `aria-live`](#heading-bonnes-pratiques-pour-lutilisation-daria-live)
        
16. [L'attribut `aria-roledescription`](#heading-lattribut-aria-roledescription)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-roledescription`](#heading-bonnes-pratiques-pour-lutilisation-daria-roledescription)
        
17. [L'attribut `aria-atomic`](#heading-lattribut-aria-atomic)
    
    * [Bonnes pratiques pour l'utilisation d' `aria-atomic`](#heading-bonnes-pratiques-pour-lutilisation-daria-atomic)
        
18. [Conclusion](#heading-conclusion)
    

## Que Sont les Attributs ARIA ?

La plupart des attributs listés dans cet article sont des attributs ARIA. ARIA, qui signifie **Accessible Rich Internet Applications**, est un ensemble d'attributs définis par le W3C (World Wide Web Consortium) pour améliorer l'accessibilité des applications web.

Les attributs ARIA fournissent des informations supplémentaires aux technologies d'assistance comme les lecteurs d'écran. Les utiliser correctement peut rendre les applications web complexes plus accessibles aux personnes souffrant de déficiences visuelles, auditives ou motrices.

L'un des principes clés de l'utilisation d'ARIA est que, parfois, il est préférable de ne pas l'utiliser. Bien que cela puisse paraître contradictoire, vous ne devriez utiliser les attributs ARIA que lorsque cela est nécessaire. L'utilisation excessive d'ARIA peut perturber l'expérience des utilisateurs s'appuyant sur des technologies d'assistance. Bien que les utilisateurs voyants puissent ne remarquer aucun problème, une utilisation excessive ou incorrecte d'ARIA peut avoir un impact négatif sur l'accessibilité.

## L'attribut `alt`

L'attribut `alt` ne vous est probablement pas nouveau si vous avez déjà utilisé des images HTML. Vous l'utilisez pour fournir un texte *alternatif* qui s'affiche lorsqu'une image n'est pas correctement affichée à l'écran.

Mais l'utilisation la plus importante de l'attribut `alt` concerne l'accessibilité. Si l'attribut `alt` n'est pas présent dans un élément d'image, un lecteur d'écran peut annoncer le nom du fichier image ou l'URL de l'image au lieu d'expliquer ce qu'elle montre. Cela peut être inutile et nous voulons éviter cela.

Le contenu de l'attribut `alt` doit être concis car son but principal est de décrire brièvement une image pour ceux qui ne peuvent pas la voir. Cela inclut les utilisateurs qui comptent sur les lecteurs d'écran, les moteurs de recherche et les utilisateurs ayant des connexions internet lentes où les images peuvent ne pas charger. Si le texte `alt` est trop long, il peut inclure des détails inutiles qui n'apportent pas de valeur à la compréhension de l'utilisateur.

L'attribut `alt` est différent d'une légende d'image. Les légendes sont visibles et peuvent fournir plus de contexte ou d'informations supplémentaires sur une image. Utiliser une légende comme texte `alt` peut le rendre trop long et redondant.

Si l'image est purement décorative, alors l'attribut alt doit être laissé vide. Si une image a un attribut alt vide, un outil d'assistance l'ignorera. C'est important pour aider les utilisateurs à rester concentrés sur le contenu et à ne pas les distraire avec des informations inutiles.

Voici un exemple d'utilisation de l'attribut alt :

```xml
<p>Les lions sont remarquables pour leurs rugissements puissants, 
qui peuvent être entendus jusqu'à huit kilomètres. 
Ces rugissements sont utilisés pour communiquer avec les autres 
membres de la troupe, ainsi que pour éloigner les lions rivaux et les intrus. 
Bien que les lions soient souvent associés à la savane africaine, 
une petite population de lions d'Asie existe encore dans la forêt de Gir en Inde, 
en faisant l'un des grands félins les plus menacés au monde.</p>

<img src="lion.jpg" alt="un lion" /> <!-- bref et donne du contexte au paragraphe -->

<img src="background-stars.png" alt="" /> <!-- Cette image est purement pour 
la décoration donc elle est laissée vide -->
```

## L'attribut `aria-label`

L'attribut `aria-label` est utilisé pour fournir un nom accessible à un élément qui pourrait ne pas avoir de texte visible. Un exemple courant est un bouton qui contient une image ou un SVG.

Beaucoup d'éléments ont un nom accessible – le nom accessible est le contenu à l'intérieur de l'élément. Le nom accessible pour le titre dans cet exemple est "Foire Aux Questions"

```xml
<h1>Foire Aux Questions</h1>
```

Tout le monde, y compris les personnes utilisant une technologie d'assistance, comprendrait clairement la signification de l'exemple ci-dessus car il contient un contenu visible.

Mais dans l'exemple ci-dessous, un utilisateur s'appuyant sur un lecteur d'écran pourrait manquer le contenu du bouton s'il n'a pas d' `aria-label`. C'est parce que le contenu du bouton est un SVG et que le SVG ne contient aucun contenu visible :

```xml
<button aria-label="Rechercher">
    <svg
      fill="#000000" 
      height="20px"
      width="20px"
      xmlns="http://www.w3.org/2000/svg" 
      viewBox="0 0 488.4 488.4">
        <g stroke-width="0"></g>
        <g stroke-linecap="round" stroke-linejoin="round"></g>
        <g><g>
        <g>
          <path d="M0,203.25c0,112.1,91.2,203.2,203.2,203.2c51.6,0,98.8-19.4,134.7-51.2l129.5,129.5c2.4,2.4,5.5,3.6,8.7,3.6 s6.3-1.2,8.7-3.6c4.8-4.8,4.8-12.5,0-17.3l-129.6-129.5c31.8-35.9,51.2-83,51.2-134.7c0-112.1-91.2-203.2-203.2-203.2 S0,91.15,0,203.25z M381.9,203.25c0,98.5-80.2,178.7-178.7,178.7s-178.7-80.2-178.7-178.7s80.2-178.7,178.7-178.7 S381.9,104.65,381.9,203.25z" />
        </g> 
        </g></g>
    </svg>
</button>
```

N'utilisez pas l' `aria-label` de manière excessive. Tout le contenu n'a pas besoin d'un `aria-label` – par exemple, si vous avez un bouton qui contient une image avec un `alt`, ou un SVG avec un `title`, alors ces attributs agissent comme le nom accessible pour cet élément.

```xml
<button>
    <img src="search-icon.png" alt="Rechercher" /> <!-- pas besoin d'aria-label -->
</button>

<!-- Autre exemple -->

<button>
  <svg
    fill="#000000"
    height="20px"
    width="20px"
    role="image"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 488.4 488.4">
        <title>Icône de recherche</title> <!-- Nom accessible -->
        <g stroke-width="0"></g>
        <g stroke-linecap="round" stroke-linejoin="round"></g>
        <g><g>
        <g>
         <path d="M0,203.25c0,112.1,91.2,203.2,203.2,203.2c51.6,0,98.8-19.4,134.7-51.2l129.5,129.5c2.4,2.4,5.5,3.6,8.7,3.6 s6.3-1.2,8.7-3.6c4.8-4.8,4.8-12.5,0-17.3l-129.6-129.5c31.8-35.9,51.2-83,51.2-134.7c0-112.1-91.2-203.2-203.2-203.2 S0,91.15,0,203.25z M381.9,203.25c0,98.5-80.2,178.7-178.7,178.7s-178.7-80.2-178.7-178.7s80.2-178.7,178.7-178.7 S381.9,104.65,381.9,203.25z" />
        </g> 
        <g><g>
  </svg>
</button>
```

Vous devriez utiliser l' `aria-label` avec parcimonie et de manière appropriée. L'utilisation excessive de l'attribut peut entraîner plusieurs problèmes :

* Le contenu de l' `aria-label` n'est pas visible pour les utilisateurs voyants. Si un utilisateur ayant un handicap cognitif utilise un lecteur d'écran pour se faire aider, il pourrait ne pas comprendre pourquoi il entend des informations différentes de ce qu'il voit à l'écran.
    
* Utiliser l' `aria-label` de manière intensive dans une large base de code peut rendre le HTML plus difficile à maintenir. Vous pourriez avoir du mal à suivre d'où proviennent les étiquettes, surtout si elles sont définies par programmation ou à plusieurs endroits.
    

### Best practices for Using `aria-label`

* Chaque fois que possible, utilisez des étiquettes textuelles visibles. Elles sont plus faciles à comprendre et à maintenir, et elles garantissent des expériences cohérentes pour tous les utilisateurs.
    
* Quand c'est possible : S'il y a déjà une étiquette visible sur la page, utilisez `aria-labelledby` pour lier l'élément au texte existant au lieu de créer une nouvelle étiquette avec `aria-label` (nous en parlerons ci-dessous).
    
* Si vous utilisez `aria-label`, gardez le texte court et direct. Il doit décrire le but de l'élément en aussi peu de mots que possible.
    

## L'attribut `aria-labelledby`

L'attribut `aria-labelledby` est utilisé pour associer un élément à un autre élément qui lui sert d'étiquette. Il lie l'élément cible à un ou plusieurs autres éléments de la page qui contiennent le texte devant être utilisé comme étiquette.

Vous pouvez utiliser cet attribut lorsqu'il existe déjà une étiquette textuelle visible ou lorsque l'étiquette doit être composée de plusieurs éléments textuels.

Par exemple, vous pouvez utiliser `aria-labelledby` dans un élément `<section>` pour l'associer à un titre ou à un autre texte qui sert d'étiquette pour toute la section.

```xml
<h2 id="about-heading">À propos de nous</h2> 
<section aria-labelledby="about-heading"> <!-- utiliser l'id du h2 -->
    <p>Nous sommes une entreprise dédiée à fournir un excellent service...</p>
</section>

<h2 id="services-heading">Nos Services</h2>
<section aria-labelledby="services-heading">
    <p>Nous offrons une large gamme de services incluant...</p>
</section>
```

Parfois, vous voudrez peut-être combiner plusieurs morceaux de texte pour l'étiquette. Vous pouvez le faire en listant plusieurs IDs dans l'attribut `aria-labelledby` :

```xml
<h1 id="dialog-title">Confirmation requise</h1>
<p id="dialog-description">Êtes-vous sûr de vouloir supprimer cet élément ?</p>
<button aria-labelledby="dialog-title dialog-description">Oui</button>
```

L' `aria-labelledby` est similaire à l' `aria-label` dans la mesure où son but est de fournir un élément accessible.

### En quoi `aria-label` est-il différent de `aria-labelledby` ?

`aria-label` assigne directement une chaîne de texte comme étiquette pour un élément. Ce texte n'est pas visible à l'écran mais est annoncé par les technologies d'assistance comme les lecteurs d'écran. Il est généralement utilisé lorsqu'il n'y a pas d'étiquette textuelle visible.

`aria-labelledby` pointe vers un ou plusieurs éléments existants sur la page (en utilisant leurs attributs `id`) qui doivent être utilisés comme étiquette pour l'élément. Le texte de l'étiquette est visible pour tous les utilisateurs car il fait partie du contenu d'un autre élément.

### Bonnes pratiques pour l'utilisation d' `aria-labelledby`

* Préférez `aria-labelledby` à `aria-label` lorsqu'il y a déjà du texte sur la page pouvant servir d'étiquette. Cela réduit la redondance et garantit que les utilisateurs voyants et les utilisateurs de lecteurs d'écran voient le même contenu.
    
* Les attributs `id` référencés par `aria-labelledby` doivent être uniques sur la page et pointer correctement vers des éléments existants. Si l'ID est manquant ou incorrect, l'étiquette ne fonctionnera pas, entraînant des problèmes d'accessibilité.
    
* Lors de la combinaison de plusieurs étiquettes, assurez-vous que l'étiquette résultante a du sens lorsqu'elle est lue ensemble. L'ordre des IDs dans `aria-labelledby` est important, car les lecteurs d'écran liront les étiquettes dans l'ordre où elles sont listées.
    
* Comme pour `aria-label`, évitez de surutiliser `aria-labelledby` dans des situations où une approche plus simple (comme l'utilisation directe d'un élément `label` visible) suffirait. Cela aide à maintenir le code et réduit la charge cognitive pour les utilisateurs.
    

## L'attribut `aria-describedby`

L'attribut `aria-describedby` est utilisé pour associer un élément à un ou plusieurs éléments qui fournissent des informations descriptives supplémentaires à son sujet. L'attribut `aria-describedby` est utilisé pour fournir un contexte supplémentaire ou des instructions à un élément.

Contrairement à `aria-labelledby`, qui est destiné à fournir une étiquette ou un nom, `aria-describedby` est destiné à donner aux utilisateurs des informations plus détaillées ou un contexte sur un élément, souvent pour compléter ce qu'ils savent déjà par l'étiquette.

```xml
<label id="full-name">Nom complet</label>
<input type="text" aria-labelledby="full-name" aria-describedby="info">
<span id="info">Entrez votre nom complet.</span>
```

Lorsque `aria-labelledby` et `aria-describedby` sont tous deux utilisés sur le même élément, les lecteurs d'écran annonceront d'abord l'étiquette (de `aria-labelledby`), puis le rôle de l'élément (par exemple, "bouton"), et enfin la description (de `aria-describedby`).

### Bonnes pratiques pour l'utilisation d' `aria-describedby`

* Appliquez `aria-describedby` lorsque vous devez fournir aux utilisateurs un contexte supplémentaire ou des instructions qui vont au-delà de l'étiquette. C'est particulièrement utile pour les formulaires, les contrôles complexes ou tout élément pouvant nécessiter des éclaircissements.
    
* Bien que `aria-describedby` soit destiné à des descriptions plus détaillées, évitez les textes excessivement longs. Gardez la description concentrée sur ce que l'utilisateur doit savoir pour interagir efficacement avec l'élément.
    
* Tout comme avec `aria-labelledby`, assurez-vous que les éléments référencés par `aria-describedby` ont des attributs `id` uniques et pertinents. Le contenu de ces éléments doit être directement lié à l'élément qu'ils décrivent.
    

## L'attribut `role`

L'attribut role est utilisé pour spécifier le rôle d'un élément. Vous pouvez l'utiliser pour surcharger le rôle par défaut d'un élément sémantique. Il aide les technologies d'assistance à comprendre comment un élément doit être interprété ou comment interagir avec lui.

Lors de l'utilisation d'éléments non sémantiques (comme `<div>` ou `<span>`) pour créer des contrôles interactifs (boutons, boîtes de dialogue, onglets, etc.), l'attribut `role` informe les technologies d'assistance du comportement attendu de l'élément. Vous pouvez également utiliser le rôle pour définir des rôles de repère (landmarks) qui aident à la navigation, tels que `banner` ou `complementary`, qui définissent la structure de la page pour les utilisateurs de lecteurs d'écran.

### Valeurs de `role` courantes

Rôles pour les régions de repère (Landmarks) :

* `banner` : Représente l'en-tête du site.
    
* `navigation` : Définit une section de navigation de la page, souvent pour les liens de navigation du site ou de la page.
    
* `main` : Marque le contenu principal d'un document, distinct des barres latérales, des pieds de page, etc.
    
* `contentinfo` : Représente les informations du pied de page.
    

Cet exemple ci-dessous est uniquement à des fins de démonstration – vous devriez utiliser le bon élément sémantique quand c'est possible :

```xml
<div role="banner">
    <h1>Mon site Web</h1>
</div>

<div role="navigation">
    <ul>
        <li><a href="#home">Accueil</a></li>
        <li><a href="#about">À propos</a></li>
    </ul>
</div>

<div role="main">
    <h2>Bienvenue sur mon site Web</h2>
    <p>Voici le contenu principal...</p>
</div>

<div role="contentinfo">
    <p>&copy; 2024 Mon site Web</p>
</div>
```

Rôles pour les widgets et éléments interactifs :

* `button` : Représente un élément de bouton, sur lequel les utilisateurs peuvent cliquer pour déclencher une action.
    
* `dialog` : Marque une boîte de dialogue ou une modale qui nécessite une interaction de l'utilisateur.
    
* `alert` : Identifie un élément comme un message important ou une alerte qui nécessite l'attention de l'utilisateur.
    
* `tablist`, `tab`, `tabpanel` : Utilisés pour les interfaces à onglets, où `tablist` contient les onglets, et chaque `tab` contrôle la visibilité de son `tabpanel` correspondant.
    

```xml
<div role="button" tabindex="0" onclick="submitForm()">Envoyer</div>

<div role="dialog" aria-labelledby="dialog-title" aria-modal="true">
    <h2 id="dialog-title">Confirmation</h2>
    <p>Êtes-vous sûr de vouloir continuer ?</p>
    <button onclick="closeDialog()">Fermer</button>
</div>
```

Exemple de panneau à onglets :

```xml
<div role="tablist" aria-label="Exemple d'onglets">
    <button role="tab" id="tab-1" aria-controls="panel-1" aria-selected="true" tabindex="0">Onglet 1</button>
    <button role="tab" id="tab-2" aria-controls="panel-2" aria-selected="false" tabindex="-1">Onglet 2</button>
    <button role="tab" id="tab-3" aria-controls="panel-3" aria-selected="false" tabindex="-1">Onglet 3</button>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
    <h2>Contenu pour l'onglet 1</h2>
    <p>Ceci est le contenu du premier onglet.</p>
</div>

<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
    <h2>Contenu pour l'onglet 2</h2>
    <p>Ceci est le contenu du deuxième onglet.</p>
</div>

<div role="tabpanel" id="panel-3" aria-labelledby="tab-3" hidden>
    <h2>Contenu pour l'onglet 3</h2>
    <p>Ceci est le contenu du troisième onglet.</p>
</div>
```

### Bonnes pratiques pour l'utilisation de l'attribut `role`

* Préférez toujours utiliser des éléments HTML natifs qui ont déjà le rôle approprié (par exemple, `<button>`, `<header>`, `<nav>`, `<main>`). Cela offre un meilleur support d'accessibilité sur une plus large gamme de navigateurs et d'appareils.
    
* N'utilisez pas de manière **excessive** ou **incorrecte** l'attribut `role` car cela peut entraîner de la confusion et une accessibilité réduite. Utilisez `role` pour améliorer ou clarifier si nécessaire, pas pour remplacer le HTML sémantique.
    
* Comprenez les rôles implicites. De nombreux éléments HTML ont des rôles implicites. Par exemple, un élément `<a>` avec un attribut `href` possède automatiquement le rôle `link`. Évitez d'ajouter des attributs `role` redondants à ces éléments.
    

## L'attribut `aria-controls`

L'attribut `aria-controls` informe un lecteur d'écran que l'élément est contrôlé ou affecté par un autre élément. Il est couramment utilisé pour indiquer qu'un composant (comme un bouton ou un onglet) contrôle ou interagit avec une autre partie de la page (comme un panneau ou un menu). Il est également utilisé dans les composants interactifs tels que les onglets, les accordéons et les curseurs pour décrire quelles parties de la page sont affectées lorsque l'utilisateur interagit avec le composant.

Par exemple, vous pouvez utiliser `aria-controls` sur un bouton d'onglet pour indiquer quel panneau chaque bouton contrôle :

```xml
<!-- Boutons d'onglets -->
<button id="tab1" aria-controls="panel1">Onglet 1</button>
<button id="tab2" aria-controls="panel2">Onglet 2</button>

<!-- Panneaux de contenu -->
<div id="panel1" role="tabpanel">Contenu pour l'onglet 1</div>
<div id="panel2" role="tabpanel">Contenu pour l'onglet 2</div>
```

### Bonnes pratiques pour l'utilisation d' `aria-controls`

* Assurez-vous que l'ID utilisé dans `aria-controls` correspond exactement à l' `id` de l'élément contrôlé.
    
* Utilisez `aria-controls` conjointement avec des attributs de rôle et d'état comme `aria-selected` ou `role="tabpanel"` pour fournir des informations plus complètes sur les éléments contrôlés et leurs états.
    
* Appliquez `aria-controls` aux éléments interactifs tels que les boutons ou les liens qui ont un effet direct sur d'autres éléments. Il n'est pas typiquement utilisé pour le contenu non interactif.
    

## L'attribut `aria-selected`

L'attribut `aria-selected` est utilisé pour indiquer l'état de sélection actuel d'un élément au sein d'un groupe d'éléments sélectionnables. Un élément sélectionnable pourrait être une option dans un menu, un onglet dans un panneau à onglets ou un élément dans une zone de liste.

Voici un exemple de l'état de sélection dans une zone de liste (listbox). `aria-selected="true"` dans l'option 1 indique que l'Option 1 est actuellement sélectionnée.

```xml
<!-- Listbox -->
<ul role="listbox">
  <li role="option" aria-selected="true">Option 1</li>
  <li role="option" aria-selected="false">Option 2</li>
  <li role="option" aria-selected="false">Option 3</li>
</ul>
```

### Bonnes pratiques pour l'utilisation d' `aria-selected`

* Utilisez `aria-selected="true"` pour l'élément sélectionné et `aria-selected="false"` pour les éléments non sélectionnés. La valeur doit être une chaîne de caractères, pas un booléen.
    
* Assurez-vous que l'état visuel de l'élément (par exemple, onglet actif ou option sélectionnée) correspond à la valeur `aria-selected`. Des états incohérents peuvent prêter à confusion pour les utilisateurs de technologies d'assistance.
    
* Utilisez `aria-selected` conjointement avec les attributs `role` appropriés (par exemple, `role="option"` pour les éléments de zone de liste) pour fournir un contexte complet.
    
* Assurez-vous qu' `aria-selected` est mis à jour dynamiquement à mesure que les utilisateurs interagissent avec l'interface. Par exemple, lorsqu'un utilisateur sélectionne une nouvelle option, mettez à jour l'attribut `aria-selected` en conséquence.
    

## L'attribut `tabindex`

L'attribut `tabindex` est utilisé pour contrôler la navigation au clavier d'un élément. Vous pouvez l'utiliser pour activer le focus pour des éléments non interactifs comme `div`, `p` ou `span` ou désactiver le focus pour des éléments interactifs comme `button`, `a`, `input`. Vous pouvez également l'utiliser pour contrôler l'ordre du focus sur une page.

### Valeurs possibles de `tabindex`

**Valeurs positives :** Les éléments avec des valeurs positives deviennent focalisables et sont inclus dans l'ordre de tabulation, leurs numéros déterminant l'ordre dans lequel ils reçoivent le focus. Les éléments avec des numéros plus bas reçoivent le focus avant les éléments avec des numéros plus élevés.

```xml
<button tabindex="2">Annuler</button> <!-- Ceci recevra le focus en dernier -->
<button tabindex="1">Envoyer</button> <!-- Ceci recevra le focus en premier -->
```

Les éléments ayant les mêmes valeurs seront parcourus dans l'ordre où ils apparaissent.

**Note :** L'utilisation de valeurs `tabindex` positives peut entraîner un ordre de tabulation confus et non intuitif. Il est généralement préférable d'utiliser `tabindex="0"` pour les éléments qui doivent faire partie de l'ordre de tabulation naturel.

**Zéro :** Vous utilisez ceci pour rendre un élément focalisable et l'inclure dans l'ordre de tabulation naturel basé sur sa position dans le document. C'est utile pour rendre focalisables des éléments qui ne le sont pas normalement (comme `<div>` ou `<span>`).

```xml
<div role="button" tabindex="0">Envoyer</div> 
<!-- L'élément devient focalisable en utilisant le clavier -->
```

**Valeurs négatives :** Vous utilisez ceci pour retirer un élément de l'ordre de tabulation, ce qui signifie qu'il ne peut pas recevoir le focus à l'aide de la touche `Tab`. Mais il peut toujours recevoir le focus par programmation (via JavaScript). C'est utile pour les éléments qui ne devraient pas être focalisables par défaut mais qui pourraient avoir besoin de l'être dans certaines conditions.

```xml
<input type="text" name="name">
<input type="text" name="other-names" tabindex="-1">
<input type="text" placeholder="email">

<!-- other-names sera sauté lors de la tabulation à travers les champs ; 
seuls name et email recevront le focus -->
```

### Bonnes pratiques pour l'utilisation de `tabindex`

* Reposez-vous sur l'ordre de tabulation naturel autant que possible. Utilisez `tabindex="0"` pour inclure des éléments dans l'ordre de tabulation et évitez d'utiliser des valeurs positives à moins que cela ne soit absolument nécessaire.
    
* L'utilisation de valeurs `tabindex` positives peut créer un ordre de tabulation imprévisible et rendre la navigation plus difficile pour les utilisateurs. Il vaut mieux utiliser le flux par défaut et `tabindex="0"`.
    
* Utilisez `tabindex="-1"` pour les éléments qui n'ont pas vocation à recevoir le focus.
    
* Assurez-vous que l'ordre du focus suit une séquence logique et intuitive, correspondant à la disposition visuelle et au flux d'interaction de la page.
    
* Testez avec le clavier et les technologies d'assistance.
    
* Lors de l'ajout ou du retrait dynamique d'éléments focalisables (par exemple, via JavaScript), assurez-vous que la gestion du focus est traitée correctement pour maintenir une expérience fluide.
    

## L'attribut `title`

L'attribut `title` en HTML est utilisé pour fournir des informations supplémentaires sur un élément. Le contenu de l'attribut s'affiche dans une info-bulle (tooltip) lorsqu'un utilisateur survole l'élément contenant le titre. Il peut être appliqué à la plupart des éléments HTML, y compris les liens, les images et les champs de formulaire.

Vous pouvez utiliser l'attribut title pour fournir une brève explication ou une description du contenu d'un élément. Par exemple, vous pouvez l'utiliser pour clarifier la signification d'abréviations ou d'acronymes lorsqu'il est utilisé avec la balise `<abbr>`.

```xml
<abbr title="World Wide Web">WWW</abbr>
<!-- Le survol de "WWW" affiche l'info-bulle "World Wide Web", 
expliquant l'abréviation. -->

<img src="logo.png" 
alt="Logo de l'entreprise" 
title="Ceci est le logo de notre entreprise">
<!-- Les utilisateurs verront "Ceci est le logo de notre entreprise" 
lors du survol de l'image. -->
```

### Problèmes d'accessibilité liés à l'attribut `title`

L'attribut title peut être utile, mais il s'accompagne de certains problèmes d'accessibilité :

* Les lecteurs d'écran n'annoncent pas systématiquement l'attribut `title`, surtout lorsqu'il y a aussi un attribut `alt` – ou ils peuvent l'ignorer complètement. Les utilisateurs de technologies d'assistance peuvent passer à côté des informations fournies par l'attribut `title`, surtout s'ils s'appuient uniquement sur les lecteurs d'écran.
    
* L'info-bulle générée par l'attribut `title` n'apparaît généralement qu'au survol avec une souris ou un pavé tactile. Les utilisateurs qui naviguent avec un clavier ou un écran tactile peuvent ne pas avoir accès à ces informations.
    
* Le contenu de l'attribut `title` est masqué par défaut et n'est révélé qu'au survol. Cela le rend moins accessible aux utilisateurs qui ne savent pas qu'ils doivent survoler pour obtenir des informations supplémentaires.
    
* Les info-bulles peuvent être difficiles à lire car elles disparaissent souvent rapidement, et leur contenu peut être tronqué ou trop long pour tenir dans la fenêtre de l'info-bulle.
    

### Bonnes pratiques pour l'utilisation de l'attribut `title`

* Évitez de vous fier uniquement à l'attribut `title`. Assurez-vous que les informations critiques sont disponibles de manière plus accessible, comme du texte visible ou des attributs ARIA.
    
* Utilisez l'attribut `title` pour des informations supplémentaires et non essentielles qui améliorent l'expérience utilisateur mais ne sont pas critiques pour la compréhension du contenu.
    
* Pour les entrées de formulaire, utilisez l'attribut `aria-describedby` pour associer des instructions supplémentaires à un élément de formulaire. Utilisez des étiquettes ou des descriptions visibles à la place ou en complément de l'attribut `title` pour garantir que tous les utilisateurs ont accès à l'information.
    
* Si vous utilisez l'attribut `title`, gardez le texte bref et direct. Les info-bulles longues peuvent être difficiles à lire et risquent d'être tronquées.
    

## Utiliser l'attribut `for` dans `label`

L'attribut `for`, lorsqu'il est utilisé dans `<label>`, sert à connecter une étiquette à son contrôle de formulaire correspondant – c'est-à-dire `<input>`, `<select>` ou `<textarea>`. Les lecteurs d'écran annonceront l'étiquette lorsque l'entrée assignée reçoit le focus. Lorsqu'il est utilisé correctement, cliquer sur l'étiquette mettra le focus sur l'entrée correspondante.

La valeur de l'attribut `for` doit correspondre à l' `id` de l'entrée avec laquelle il est associé :

```xml
<label for="fullname">Nom complet</label>
<input type="text" id="fullname">
<!-- Lorsque l'utilisateur clique sur l'étiquette "Nom complet", 
le curseur se placera sur le champ de saisie correspondant. -->
```

### Bonnes pratiques pour l'utilisation de l'attribut `for`

* Assurez-vous que chaque contrôle de formulaire possède un attribut `id` unique afin que l'attribut `for` puisse le référencer correctement. Évitez d'utiliser des valeurs d' `id` en double sur la même page.
    
* Évitez les attributs `for` vides. S'il n'y a pas de contrôle de formulaire associé, cela peut troubler les utilisateurs de technologies d'assistance.
    
* Placez les étiquettes à proximité de leurs contrôles de formulaire associés. Typiquement, les étiquettes doivent être placées au-dessus ou à gauche des contrôles de formulaire pour une lisibilité et une utilisabilité optimales.
    

## L'attribut `scope`

L'attribut `scope` est utilisé dans les tableaux HTML pour définir la relation entre les en-têtes de tableau et les cellules qu'ils décrivent. Cet attribut est particulièrement important pour l'accessibilité car il aide les lecteurs d'écran et autres technologies d'assistance à comprendre la structure du tableau et à transmettre les informations correctes aux utilisateurs.

L'attribut `scope` est appliqué aux éléments `<th>` (en-tête de tableau) pour spécifier si l'en-tête s'applique à une ligne, une colonne ou un groupe de lignes ou colonnes.

### Valeurs possibles de `scope`

* `row` : Indique que l'élément `<th>` est un en-tête pour une ligne. Dans l'exemple ci-dessous, `scope="row"` est utilisé pour le premier élément `<th>` de chaque ligne, indiquant que l'en-tête s'applique à toute la ligne.
    

```xml
<table>
    <tbody>
        <tr>
            <th scope="row">Produit A</th>
            <td>$1000</td>
            <td>$1200</td>
            <td>$1100</td>
        </tr>
        <tr>
            <th scope="row">Produit B</th>
            <td>$900</td>
            <td>$950</td>
            <td>$1000</td>
        </tr>
    </tbody>
</table>
```

* `col` : Indique que l'élément `<th>` est un en-tête pour une colonne.
    

```xml
<table>
    <thead>
        <tr>
            <th scope="col">Nom</th>
            <th scope="col">Âge</th>
            <th scope="col">Profession</th>
        </tr>
<!-- L'attribut scope="col" indique que chaque élément <th> 
sert d'en-tête pour la colonne correspondante située en dessous. -->
    </thead>
    <tbody>
        <tr>
            <td>Jane</td>
            <td>30</td>
            <td>Ingénieure</td>
        </tr>
        <tr>
            <td>Tobe</td>
            <td>25</td>
            <td>Designer</td>
        </tr>
    </tbody>
</table>
```

* `rowgroup` : Indique que l'élément `<th>` est un en-tête pour un groupe de lignes. Dans l'exemple ci-dessous, les lignes "Département Marketing" et "Département Ventes" ont l'attribut `scope="rowgroup"` pour indiquer que ces lignes agissent comme en-têtes pour les groupes de lignes qui suivent :
    

```xml
<table>
  <thead>
    <tr>
      <th scope="col">Département</th>
      <th scope="col">Nom de l'employé</th>
      <th scope="col">Poste</th>
      <th scope="col">Salaire</th>
    </tr>
  </thead>
  <tbody>
    <!-- Groupe de lignes pour le département Marketing -->
    <tr>
      <th scope="rowgroup" colspan="4">Département Marketing</th>
    </tr>
    <tr>
      <th scope="row">Amari Pere</th>
      <td>Responsable Marketing</td>
      <td>$75,000</td>
    </tr>
    <tr>
      <th scope="row">Uyati Hope</th>
      <td>Spécialiste SEO</td>
      <td>$65,000</td>
    </tr>

    <!-- Groupe de lignes pour le département Ventes -->
    <tr>
      <th scope="rowgroup" colspan="4">Département Ventes</th>
    </tr>
    <tr>
      <th scope="row">Timini Prosper</th>
      <td>Responsable des Ventes</td>
      <td>$80,000</td>
    </tr>
    <tr>
      <th scope="row">Delilu Pink</th>
      <td>Chargé de compte</td>
      <td>$70,000</td>
    </tr>
  </tbody>
</table>
```

* `colgroup` : Indique que l'élément `<th>` est un en-tête pour un groupe de colonnes. Dans l'exemple ci-dessous, `scope="colgroup"` est utilisé pour indiquer que la première ligne d'en-têtes s'applique à des groupes de colonnes (Q1 et Q2), tandis que `scope="col"` et `scope="row"` sont utilisés pour les colonnes et lignes individuelles.
    

```xml
<table>
    <thead>
        <tr>
            <th scope="colgroup">Région</th>
            <th scope="colgroup">T1</th>
            <th scope="colgroup">T2</th>
        </tr>
        <tr>
            <th scope="col">Ventes</th>
            <th scope="col">Profit</th>
            <th scope="col">Ventes</th>
            <th scope="col">Profit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">Nord</th>
            <td>$2000</td>
            <td>$400</td>
            <td>$2500</td>
            <td>$500</td>
        </tr>
        <tr>
            <th scope="row">Sud</th>
            <td>$1500</td>
            <td>$300</td>
            <td>$1800</td>
            <td>$350</td>
        </tr>
    </tbody>
</table>
```

### Bonnes pratiques pour l'utilisation de l'attribut `scope`

* Définissez toujours `scope` pour les tableaux complexes afin de clarifier la relation entre les en-têtes et les cellules de données.
    
* Simplifiez les structures de tableaux quand c'est possible. Bien que l'attribut `scope` aide à l'accessibilité, envisagez de simplifier les structures de tableaux là où c'est possible. Si un tableau est trop complexe, il peut être difficile à comprendre pour tous les utilisateurs, même avec un balisage approprié.
    
* Pour les tableaux particulièrement complexes, envisagez d'utiliser des attributs ARIA comme `aria-labelledby` ou `aria-describedby` pour fournir un contexte supplémentaire et garantir que tous les utilisateurs peuvent naviguer efficacement dans le tableau.
    
* Après avoir appliqué l'attribut `scope`, testez le tableau avec des lecteurs d'écran pour vous assurer que les relations entre les en-têtes et les cellules de données sont annoncées correctement.
    
* N'utilisez pas `scope` dans des situations où c'est inutile. Pour les tableaux simples où chaque en-tête est clairement associé à une seule ligne ou colonne, le comportement par défaut de l'HTML est généralement suffisant.
    

## L'attribut `aria-hidden`

L'attribut aria-hidden est utilisé pour contrôler la visibilité d'un élément pour les technologies d'assistance alors qu'il est toujours visible à l'écran. Vous pouvez l'utiliser pour masquer des éléments purement décoratifs, comme des icônes ou des images, qui n'ajoutent pas d'informations significatives au contenu. Cela aide à éviter que les lecteurs d'écran ne lisent des informations inutiles.

```xml
<button>
    <span aria-hidden="true">🔍</span>
    Rechercher
</button>
```

Vous pouvez également l'utiliser pour masquer du contenu qui a déjà été annoncé afin d'éviter la redondance dans ce que les lecteurs d'écran annoncent. Pour le contenu dont l'affichage est basculé (comme les modales ou les sections extensibles), vous pouvez utiliser `aria-hidden` pour masquer le contenu inactif des lecteurs d'écran, garantissant qu'ils n'interagissent qu'avec le contenu visible et actif.

```xml
<button>
    <span aria-hidden="true">✉</span> <!-- masquer l'icône décorative -->
    <span>Messages</span>
</button>
```

Vous pouvez aussi utiliser `aria-hidden` lors de la création de widgets complexes (comme des carrousels ou des interfaces à onglets) pour masquer les panneaux ou diapositives inactifs des technologies d'assistance, concentrant leur attention sur la partie active du widget.

```xml
<div id="menu" aria-hidden="true">
    <!-- Contenu du menu ici -->
</div>

<button onclick="toggleMenu()">Basculer le menu</button>

<script>
    const toggleMenu = () => {
        const menu = document.getElementById('menu');
        const isHidden = menu.getAttribute('aria-hidden') === 'true';

        menu.setAttribute('aria-hidden', !isHidden);
    }
</script>
```

### Bonnes pratiques pour l'utilisation d' `aria-hidden`

* N'utilisez `aria-hidden` que lorsque vous avez besoin de masquer du contenu aux lecteurs d'écran pour éviter de submerger les utilisateurs d'informations redondantes ou non pertinentes.
    
* Ne l'utilisez pas sur des éléments avec lesquels les utilisateurs doivent interagir, comme les boutons ou les liens.
    
* Assurez-vous que `aria-hidden` reflète fidèlement la visibilité des éléments à l'écran. Si un élément devient visible ou masqué via JavaScript ou CSS, mettez à jour `aria-hidden` en conséquence pour maintenir l'accessibilité.
    
* Dans un environnement d'équipe, documentez pourquoi et où `aria-hidden` est utilisé dans votre base de code, afin que les autres membres de l'équipe comprennent son but et puissent le maintenir correctement.
    

## L'attribut `inert`

L'attribut `inert` empêche un élément et tous ses descendants d'être focalisables, interactifs ou perceptibles par les technologies d'assistance. Lorsqu'un élément possède l'attribut `inert`, il ne peut pas recevoir le focus, être cliqué ou faire l'objet d'une interaction d'aucune sorte. Il est également masqué des technologies d'assistance comme les lecteurs d'écran.

Contrairement à `aria-hidden`, qui n'affecte que l'accessibilité, `inert` s'applique à toutes les interactions utilisateur. L'attribut inert peut être utilisé pour désactiver des sections d'une page qui sont temporairement non pertinentes, comme lors d'erreurs de validation de formulaire, pendant le chargement de données, ou lorsqu'une certaine section est masquée mais toujours présente dans le DOM. Il peut également être utilisé dans des interfaces utilisateur complexes comme les formulaires multi-étapes ou les assistants pour garantir que les utilisateurs n'interagissent qu'avec l'étape ou la section actuelle.

L'utilisation la plus courante d'inert, cependant, se trouve dans une modale, où vous voulez empêcher les utilisateurs d'interagir avec le contenu en arrière-plan pendant que la modale est ouverte.

Comme dans l'exemple ci-dessous, lorsque la modale est ouverte, l'attribut `inert` est ajouté au contenu principal, le rendant non interactif et masqué pour les lecteurs d'écran. Lorsque la modale est fermée, l'attribut `inert` est supprimé, et le contenu principal redevient interactif.

```xml
<div id="main-content" inert>
    <p>Ceci est le contenu principal de la page. Il sera inactif lorsque la modale est ouverte.</p>
</div>

<div id="modal" role="dialog" aria-modal="true">
    <h2>Titre de la modale</h2>
    <p>Ceci est le contenu à l'intérieur de la modale.</p>
    <button onclick="closeModal()">Fermer la modale</button>
</div>

<script>
function openModal() {
    document.getElementById('main-content').setAttribute('inert', '');
    document.getElementById('modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('main-content').removeAttribute('inert');
    document.getElementById('modal').style.display = 'none';
}
</script>
```

### Bonnes pratiques pour l'utilisation de l'attribut `inert`

* Assurez-vous que lorsque vous utilisez `inert`, l'état visuellement inactif ou désactivé des éléments est clair pour les utilisateurs voyants. Par exemple, assombrir ou flouter le contenu en arrière-plan lorsqu'une modale est ouverte peut compléter l'attribut `inert`.
    
* Ne surutilisez pas `inert`, car cela pourrait involontairement rendre des portions importantes de votre page non interactives et inaccessibles. Utilisez-le judicieusement pour gérer le focus et l'interaction de l'utilisateur uniquement lorsque c'est nécessaire.
    
* Lors de l'ajout et du retrait dynamique de l'attribut `inert`, assurez-vous qu'il est correctement supprimé lorsqu'il n'est plus nécessaire afin que les utilisateurs puissent retrouver l'accès au contenu précédemment désactivé.
    

## L'attribut `aria-live`

Vous pouvez utiliser l'attribut `aria-live` pour informer les technologies d'assistance des changements de contenu dynamiques sur une page web. Lorsqu' `aria-live` est appliqué à un élément, les lecteurs d'écran sont alertés quand le contenu à l'intérieur de cet élément est mis à jour, garantissant que les utilisateurs sont informés des changements importants qui surviennent après le chargement initial de la page.

Cet attribut peut être utile pour le contenu qui se met à jour dynamiquement, comme les notifications, les alertes, les messages de chat ou les cours de la bourse. Il garantit que les utilisateurs sont conscients des changements qui pourraient autrement passer inaperçus.

### Valeurs possibles pour `aria-live`

Il existe trois valeurs principales : `off`, `polite` et `assertive`.

* `off` : Valeur par défaut, les mises à jour de l'élément ne seront pas annoncées par les lecteurs d'écran.
    
* `polite` : Les mises à jour seront annoncées par le lecteur d'écran, mais seulement après que l'utilisateur a fini d'interagir avec la tâche actuelle ou de lire d'autres contenus. Cela garantit que la mise à jour n'interrompt pas l'activité en cours de l'utilisateur.
    

Dans l'exemple ci-dessous, chaque nouveau message est ajouté au conteneur `#messages`, qui a `aria-live="polite"`. Le lecteur d'écran annoncera le nouveau message seulement après que l'utilisateur aura terminé son activité actuelle.

```xml
<div id="chat-window">
    <div id="messages" aria-live="polite">
        <!-- Les messages existants sont ici -->
        <div>Jean : Bonjour !</div>
        <div>Vous : Salut !</div>
    </div>
</div>

<button onclick="addMessage()">Envoyer le message</button>

<script>
function addMessage() {
    const newMessage = document.createElement('div');
    newMessage.textContent = 'Alice : Comment vas-tu ?';
    document.getElementById('messages').appendChild(newMessage);
}
</script>
```

* `assertive` : Les mises à jour seront annoncées immédiatement, interrompant tout ce que le lecteur d'écran est en train d'annoncer. Utilisez ceci pour des informations urgentes ou critiques qui nécessitent l'attention immédiate de l'utilisateur.
    

Dans l'exemple ci-dessous, les mises à jour des cours de la bourse sont placées dans un conteneur qui possède `aria-live="assertive"`.

```xml
<div id="stock-ticker" aria-live="assertive">
    <!-- Cours de bourse initiaux -->
    <div id="stock1">Action A : $100</div>
    <div id="stock2">Action B : $150</div>
</div>

<button onclick="updateStockPrices()">Mettre à jour les prix</button>

<script>
function updateStockPrices() {
    document.getElementById('stock1').textContent = 'Action A : $95';
    document.getElementById('stock2').textContent = 'Action B : $155';
}
</script>
```

### Bonnes pratiques pour l'utilisation d' `aria-live`

* Utilisez `aria-live="polite"` pour les mises à jour non critiques afin d'éviter de perturber l'expérience de l'utilisateur. Réservez `aria-live="assertive"` pour les mises à jour urgentes qui nécessitent une attention immédiate, telles que des erreurs critiques ou des avertissements de sécurité.
    
* Soyez attentif à la fréquence d'utilisation des éléments `aria-live` sur une page. En abuser peut entraîner une expérience surstimulante pour les utilisateurs qui comptent sur les lecteurs d'écran, car ils peuvent être submergés par des annonces fréquentes.
    
* N'utilisez pas `aria-live` sur du contenu qui n'a pas besoin d'être annoncé, ou sur du contenu qui est déjà communiqué à l'utilisateur d'une autre manière.
    
* `aria-live` est particulièrement utile pour le contenu mis à jour dynamiquement, comme les scores sportifs en direct, les actualités de dernière minute ou les applications de chat. Assurez-vous que l'utilisateur est tenu informé des mises à jour importantes au fur et à mesure qu'elles se produisent.
    

## L'attribut `aria-roledescription`

Vous pouvez utiliser `aria-roledescription` pour fournir une description lisible par l'homme et localisée pour le rôle d'un élément. Il surcharge la valeur `role` implicite ou explicite pour les lecteurs d'écran, et permet aux développeurs de créer des descriptions plus intuitives et spécifiques au contexte pour des composants d'interface utilisateur complexes ou non conventionnels qui pourraient ne pas avoir de nom de rôle standard.

Vous pouvez l'utiliser pour fournir une explication plus claire de l'objectif ou de la fonctionnalité de l'élément.

Dans l'exemple ci-dessous, les lecteurs d'écran l'annonceront comme "Bouton de favoris" au lieu de simplement "Bouton".

```xml
<button role="button" aria-roledescription="Bouton de favoris">
    <span aria-hidden="true">⭐</span> Enregistrer cette page
</button>
```

Vous pouvez également l'utiliser pour soutenir l'internationalisation, comme fournir des descriptions de rôles dans différentes langues.

```xml
<button role="button" aria-roledescription="Search Button" lang="en">
    <span aria-hidden="true">🔍</span> Search
</button>

<button role="button" aria-roledescription="Botón de busqueda" lang="es">
    <span aria-hidden="true">🔍</span> Buscar
</button>

<button role="button" aria-roledescription="Bouton de recherche" lang="fr">
    <span aria-hidden="true">🔍</span> Recherche
</button>
```

### Bonnes pratiques pour l'utilisation d' `aria-roledescription`

* N'utilisez `aria-roledescription` que lorsque le rôle standard ne décrit pas suffisamment l'objectif de l'élément.
    
* La description doit être courte, claire et directement liée à la fonction de l'élément. Évitez d'utiliser du jargon ou un langage trop technique.
    
* `aria-roledescription` doit être utilisé aux côtés d'un rôle ARIA approprié, et non comme un remplacement. Le `role` fournit le contexte fondamental (comme `"button"` ou `"listbox"`), tandis que la description ajoute de la clarté.
    
* Si votre application prend en charge plusieurs langues, assurez-vous que les valeurs d' `aria-roledescription` sont localisées pour correspondre aux préférences linguistiques de l'utilisateur. Cela aide à fournir une expérience cohérente et compréhensible.
    
* Assurez-vous que l' `aria-roledescription` ne répète pas ou n'entre pas en conflit avec d'autres attributs ARIA ou étiquettes d'éléments. Il doit compléter, et non dupliquer, les informations déjà fournies.
    

## L'attribut `aria-atomic`

Vous pouvez utiliser l'attribut `aria-atomic` pour contrôler la manière dont les mises à jour d'un élément sont annoncées par les technologies d'assistance. Lorsqu' `aria-atomic` est défini sur `true`, cela indique que lorsque des changements surviennent au sein de l'élément, l'intégralité du contenu de l'élément doit être traitée comme une seule unité et annoncée en totalité par le lecteur d'écran (plutôt que d'annoncer seulement les parties modifiées).

Dans les cas où les mises à jour d'une partie d'un élément pourraient rendre le contexte global flou, `aria-atomic` aide en fournissant une annonce complète du contenu de l'élément, donnant aux utilisateurs une compréhension totale du contexte.

Il est souvent utilisé conjointement avec `aria-live`. Alors qu' `aria-live` détermine comment les mises à jour sont annoncées (poliment ou de manière assertive), `aria-atomic` contrôle si tout le contenu est lu ou seulement les changements.

```xml
<div id="news-ticker" role="region" aria-live="polite" aria-atomic="true">
  Actualité : Une tempête majeure est attendue ce week-end.
</div>
<button onclick="updateHeadline()">Mettre à jour le titre</button>
<script>
function updateHeadline() {
    document.getElementById('news-ticker').innerText = 'Actualité : Le marché boursier atteint un record historique !';
}
</script>
```

### Bonnes pratiques pour l'utilisation d' `aria-atomic`

* Appliquez `aria-atomic="true"` uniquement aux éléments où une annonce complète des mises à jour est essentielle pour comprendre le contexte.
    
* Lors de l'utilisation d' `aria-atomic="true"`, assurez-vous que le contenu à l'intérieur de l'élément fournit un contexte cohérent et complet aux utilisateurs.
    
* Utilisez `aria-atomic` en combinaison avec `aria-live` pour spécifier comment les mises à jour doivent être annoncées. Cela garantit que les mises à jour sont annoncées de la manière appropriée et avec tout leur contexte.
    

## Conclusion

Comprendre et utiliser efficacement les attributs HTML pour l'accessibilité est crucial pour créer des expériences web inclusives. En comprenant et en utilisant ces attributs de manière appropriée, vous pouvez vous assurer que votre application offre une excellente expérience utilisateur à tous les visiteurs.

### Ressources

* [Fournir des noms et des descriptions accessibles](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)
    
* [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
    
* [Pas d'ARIA vaut mieux qu'une mauvaise ARIA](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/)
    
* [Exemples ARIA par propriétés et états](https://www.w3.org/WAI/ARIA/apg/example-index/#examples_by_props_label)
    

Merci beaucoup de m'avoir lu, j'espère que ce guide vous aidera à créer du contenu web plus accessible. Si vous l'avez trouvé utile, n'hésitez pas à le partager.

Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/elizabeth-meshioye/).