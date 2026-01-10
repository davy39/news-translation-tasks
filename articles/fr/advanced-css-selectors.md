---
title: Sélecteurs CSS avancés – Comment et quand les utiliser
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-02-26T17:12:11.000Z'
originalURL: https://freecodecamp.org/news/advanced-css-selectors
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Advanced-CSS.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Sélecteurs CSS avancés – Comment et quand les utiliser
seo_desc: Writing CSS is often painful for a lot of developers, because many of us
  lose our curiosity very early in the learning journey. For instance, as soon as
  we learn basic CSS selectors, we settle into a pattern of using only those, thinking
  they're all ...
---

Écrire du CSS est souvent douloureux pour beaucoup de développeurs, car beaucoup d'entre nous perdons notre curiosité très tôt dans le parcours d'apprentissage. Par exemple, dès que nous apprenons les sélecteurs CSS de base, nous nous installons dans un schéma d'utilisation uniquement de ceux-ci, pensant qu'ils sont tout ce dont nous avons besoin. Mais et s'il y avait plus ?

Dans cet article, vous apprendrez quelques sélecteurs et combinateurs CSS avancés essentiels comme les `combinateurs enfants et frères`, les `pseudo-classes`, les `pseudo-classes structurelles`, les `pseudo-éléments` et les `sélecteurs d'attributs` en construisant une section FAQ interactive. Si vous souhaitez avancer pour voir ce que nous allons construire, [consultez-la](#construction-dune-section-faq-interactive).

## Table des matières :

* [Qu'est-ce que les sélecteurs CSS avancés ?](#heading-questce-que-les-selecteurs-css-avances)
* [Pourquoi utiliser les sélecteurs CSS avancés](#heading-pourquoi-utiliser-les-selecteurs-css-avances)
* [Comment construire une section FAQ interactive](#heading-comment-construire-une-section-faq-interactive)
* [Code complet du projet](#heading-code-complet-du-projet)
* [Conclusion](#heading-conclusion)

# **Qu'est-ce que les sélecteurs CSS avancés ?**

Au cœur, le CSS consiste à sélectionner des éléments du DOM (Document Object Model) pour leur appliquer des styles.

Bien que les sélecteurs de base comme les classes, les ID et les sélecteurs d'éléments fassent une grande partie du travail quotidien, les sélecteurs CSS avancés offrent un niveau de spécificité et de contrôle plus profond. Ils vous permettent de cibler exactement les éléments que vous souhaitez styliser, en fonction des attributs, des états et de leurs relations les uns avec les autres.

Par exemple, vous pouvez habiller les liens qui ont été visités (`:visited`), styliser le premier paragraphe dans un article (`article p:first-of-type`), ou cibler les éléments vides (`:empty`), ce qui vous évite d'encombrer votre code HTML avec des classes ou des ID supplémentaires, conduisant finalement à un code plus propre et plus efficace.

# Pourquoi utiliser les sélecteurs CSS avancés

Voici trois des nombreuses raisons d'envisager de donner une chance aux sélecteurs CSS avancés :

1. **Stylisation interactive** : Avec des pseudo-classes comme `:hover` et `:focus`, vous pouvez créer des éléments interactifs qui répondent aux actions de l'utilisateur, directement dans le CSS. C'est un gagnant-gagnant, car cela minimise le besoin de JavaScript pour les effets visuels et maintient vos scripts légers tout en améliorant l'expérience utilisateur et l'interactivité.
2. **Accessibilité et SEO** : L'utilisation de sélecteurs avancés peut aider à garder le HTML sémantique, car les styles sont appliqués en fonction de la structure naturelle de votre document et des attributs des éléments. Cela rend votre code plus facile à lire et à maintenir, mais surtout améliore l'accessibilité et le SEO.
3. **Pertinence future** : À mesure que les normes du web évoluent, le CSS évolue également. Cela signifie qu'en adoptant les sélecteurs avancés aujourd'hui, vous alignez vos feuilles de style sur l'avenir du développement web. Cela garantit que vos designs restent résilients et adaptables, peu importe les changements qui surviennent sur le web.

# Comment construire une section FAQ interactive

Pour apprendre les sélecteurs CSS avancés, nous allons construire une section FAQ interactive pour révéler les réponses aux questions lorsqu'elles sont cliquées. Nous mettrons également en œuvre différents styles pour les FAQ en fonction de leur état ou de leur contenu.

Cette approche pratique consolidera votre compréhension lorsque vous verrez leur application dans des scénarios réels.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/finalproject.gif)
_Un GIF montrant la section FAQ que nous allons construire dans cet article_

Consultez-le sur CodePen [ici](https://codepen.io/ophyboamah/full/WNmWRvd).

## Prérequis

* Connaissance de base du HTML et du CSS
* Un IDE
* Un navigateur web

## Code HTML

La structure HTML de notre projet se compose d'une série d'éléments FAQ, chacun contenu dans un `div` et présentant une question cliquable (`label` ou `button`) qui contrôle la visibilité de la réponse (`div`). Chaque élément FAQ a une case à cocher pour gérer son état ouvert/fermé, en utilisant le CSS pour basculer visuellement la visibilité de la réponse sans JavaScript.

```html
<body>
  <section class="faq-section">
  <div class="container">
    <div class="faq-heading">
      <h1>Foire aux questions</h1>
    <p>Voici quelques questions générales sur le CSS et leurs réponses, espérons qu'elles servent de rappel.</p>
    </div>
    <div class="faq-container">
      <!-- Élément FAQ 1 -->
      <div class="faq-item">
        <input type="checkbox" id="faq1" class="faq-toggle" hidden>
        <label for="faq1" class="faq-question">Quelle est la différence entre px, em et rem ?</label>
        <div class="faq-answer">
          <p>px est une taille fixe, em change de taille en fonction de la taille de police de l'élément parent, et rem est toujours relatif à la taille de police racine du document, rendant les mises en page plus flexibles.</p>
        </div>
      </div>
      <!-- Élément FAQ 2 -->
      <div class="faq-item">
        <input type="checkbox" id="faq2" class="faq-toggle" hidden>
        <label for="faq2" class="faq-question">Pourquoi utiliser les pseudo-classes :hover et :focus ?</label>
        <div class="faq-answer">
          <p>Elles vous permettent de styliser les éléments lorsque les utilisateurs interagissent avec eux, comme changer la couleur d'un bouton lorsqu'il est survolé, rendant les sites web plus interactifs.</p>
        </div>
      </div>
    </div>
  </div>
</section>
</body>
```

## Code CSS de base

Le code ci-dessous applique un style de base à notre code HTML ci-dessus. Cela est fourni afin que vous puissiez vous concentrer sur l'apprentissage du fonctionnement des sélecteurs CSS avancés.

```css
body {
  background-color: #00ad8f;
}

.faq-section {
  margin-top: 5em; 
}

.faq-section h1 {
  font-size: 2.5em; 
}

.faq-heading {
  text-align: center; 
  margin-bottom: 2em; 
  color: #fff;
}

.container {
  max-width: 800px;
  margin: auto;
  padding: 1em;
}

.faq-item {
  background-color: #fff;
  border-radius: 0.3em;
  border: 1px solid #333;
  margin-bottom: 0.5em;
}

.faq-toggle {
  display: none; /* Masquer la case à cocher */
}

.faq-question {
  background-color: #efefef;
  padding: 1em;
  margin: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  border: none;
  position: relative; /* Nécessaire pour positionner le contenu ::before */
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  border-top: 1px solid #333;
  transition: transform 0.3s ease, padding 0.3s ease;
  padding: 0 1em;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/beforeadvCSS.png)
_Une capture d'écran de notre section FAQ avant l'ajout des sélecteurs CSS avancés_

## Combinateurs enfants et frères (`+` , `~`, `>`) :

Les combinateurs enfants et frères, bien que moins populaires que les sélecteurs d'ID et de classe, sont puissants pour styliser les éléments en relation les uns avec les autres.

Le combinateur enfant (**`>`**) est essentiel pour cibler les enfants directs d'un élément, comme le stylisme des éléments de menu dans une barre de navigation sans affecter les menus déroulants imbriqués.

Pendant ce temps, le sélecteur de frère adjacent (**`+`**) cible uniquement le frère qui suit immédiatement un élément pour des tâches comme faire ressortir le premier paragraphe après un titre.

Et le sélecteur de frère général (**`~`**) cible n'importe quel frère qui suit un élément, comme la mise en surbrillance des éléments de liste suivant une case à cocher cochée.

Dans notre projet, comme on peut le voir dans le code ci-dessous, lorsqu'une question est cliquée (c'est-à-dire que sa case à cocher associée est cochée), le sélecteur de frère adjacent (`+`) affiche un symbole "-" pour indiquer un état ouvert, signifiant qu'une FAQ est ouverte. De plus, il contrôle la hauteur maximale de la réponse pour la révéler en douceur.

```css
.faq-toggle:checked + .faq-question::after {
  content: '-'; /* Change le plus en moins sur la question FAQ lorsque le toggle est coché */
}

.faq-toggle:checked + .faq-question + .faq-answer {
  max-height: 1000px; /* Révèle la réponse lorsque le toggle est coché */
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/childandsib.png)
_Une capture d'écran de notre section FAQ ajoutant le symbole - sur les questions ouvertes_

## Pseudo-classes (`:nth-child()`, `:nth-of-type()`, `:not()`, `:focus`, `:hover`) :

Les pseudo-classes permettent de styliser des éléments en fonction de leur état ou de leurs caractéristiques sans changer la structure HTML.

Elles sont idéales pour les éléments interactifs, comme changer la couleur de fond des boutons au survol en utilisant `:hover` et `:nth-of-type()` pour mettre en évidence chaque troisième image dans une galerie pour un effet en motif. Ou styliser chaque ligne d'un tableau pour améliorer la lisibilité avec `:nth-child()` et `:not()` pour appliquer des styles à tous les boutons sauf ceux désactivés.

Dans notre projet, comme on peut le voir dans le code ci-dessous, nous utilisons la pseudo-classe `:nth-of-type()` pour différencier les questions paires et impaires en leur attribuant différentes couleurs de fond, et `:hover` pour améliorer l'interactivité, rendant la section FAQ plus facile à naviguer visuellement.

```css
.faq-item:nth-of-type(odd) .faq-question{
 background-color: #fff; /* Pour les éléments impairs */
} 

.faq-item:nth-of-type(even) .faq-question{
 background-color: #caffee; /* Pour les éléments pairs */
}

.faq-item:nth-of-type(odd) .faq-question:hover {
  background-color: #dfdfdf; 
}

.faq-item:nth-of-type(even) .faq-question:hover {
  background-color: #9debd2; 
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/candsibselectors-1.gif)
_Un GIF montrant différentes couleurs de survol pour les questions FAQ paires et impaires_

## Pseudo-classes structurelles (`:first-child`, `:last-child`, `:empty`, `:only-child`) :

Les pseudo-classes structurelles brillent lorsqu'il s'agit de styliser des éléments en fonction de leur position dans leur conteneur parent. C'est pourquoi elles aident à des tâches comme la mise en évidence du premier ou du dernier élément dans une liste avec `:first-child` pour attirer l'attention ou `:last-child` pour ajouter une bordure spéciale pour l'emphase.

Elles excellent également dans les scénarios où la structure du document influence le style, comme l'utilisation de `:empty` pour masquer ou styliser différemment les divs vides pour la cohérence de la mise en page, ou `:only-child` pour centrer le contenu dans une div pour un look propre.

```css
.faq-item:first-of-type .faq-question {
  border-top: 2px solid #007BFF; 
}

.faq-item:last-of-type .faq-question {
  border-bottom: 2px solid #007BFF; 
}

```

Dans notre projet et dans le code ci-dessus, les sélecteurs `:first-of-type` et `:last-of-type` sont utilisés pour distinguer visuellement les premier et dernier éléments FAQ en ajoutant respectivement une bordure supérieure et inférieure.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/structural.png)
_Une capture d'écran de notre section FAQ avec des bordures bleues_

## Pseudo-éléments (`::before`, `::after`, `:first-letter`, `::first-line`) :

Les pseudo-éléments ont la capacité de créer des éléments virtuels qui peuvent être stylisés séparément. Ils nous permettent de styliser des parties spécifiques d'un élément, comme ajouter du contenu avant ou après le contenu d'un élément, ou styliser la première lettre ou ligne de texte.

Vous pouvez également utiliser `::before` et `::after` pour ajouter des guillemets décoratifs autour des citations en bloc sans altérer le HTML, ou `::first-letter` pour agrandir la première lettre de chaque article similaire à ce qui est fait dans les magazines. Enfin, `::first-line` change la couleur de la première ligne d'un paragraphe pour attirer l'attention.

```css
/* ::after utilisé pour afficher le symbole "+" */
.faq-question::after {
  content: '+';
  color: #00ad8f;
  font-size: 1.4em;
}
```

Dans notre projet et dans le code ci-dessus, le pseudo-élément `::after` ajoute un signe "+" à chaque question dans leurs états par défaut. Cela complète le symbole "-" que nous avons ajouté ci-dessus sur les questions ouvertes. Ensemble, ceux-ci fournissent des indices visuels à l'utilisateur sur l'état de l'élément FAQ.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/aftersymbol.png)
_Une capture d'écran de notre section FAQ ajoutant le symbole + sur les questions fermées_

## Sélecteurs d'attributs (`[attr^="value"]`, `[attr$="value"]`, `[attr*="value"]`) :

Les sélecteurs d'attributs fournissent un moyen de styliser les éléments en fonction de la présence, de l'absence ou de la valeur des attributs. Ils sont la solution pour styliser les éléments avec des attributs de données spécifiques, comme différencier les liens externes avec `[attr^="value"]` en ciblant les URL qui commencent par "http" ou utiliser `[attr$="value"]` pour appliquer des icônes aux liens de téléchargement.

Tous ceux-ci soulignent le rôle des sélecteurs d'attributs dans la création de styles précis et basés sur des conditions, offrant un haut niveau de spécificité et de flexibilité.

```css

.faq-item[data-category^="important"] .faq-question {
  color: #E91E63; 
}
```

Dans notre projet et dans le code ci-dessus, nous utilisons un sélecteur d'attribut `[attr^="value"]` pour appliquer un style distinct (rouge) aux questions marquées avec un `data-category` comme important. Cela les fait ressortir dans la section FAQ.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/dataattribute.png)
_Une capture d'écran de notre section FAQ avec la question importante différemment colorée_

# Code complet du projet

Voici le code HTML :

```html
<body>
  <section class="faq-section">
  <div class="container">
    <div class="faq-heading">
      <h1>Foire aux questions</h1>
    <p>Voici quelques questions générales sur le CSS et leurs réponses, espérons qu'elles servent de rappel.</p>
    </div>
    <div class="faq-container">
      <!-- Élément FAQ 1 -->
      <div class="faq-item">
        <input type="checkbox" id="faq1" class="faq-toggle" hidden>
        <label for="faq1" class="faq-question">Quelle est la différence entre px, em et rem ?</label>
        <div class="faq-answer">
          <p>px est une taille fixe, em change de taille en fonction de la taille de police de l'élément parent, et rem est toujours relatif à la taille de police racine du document, rendant les mises en page plus flexibles.</p>
        </div>
      </div>
      <!-- Élément FAQ 2 -->
      <div class="faq-item">
        <input type="checkbox" id="faq2" class="faq-toggle" hidden>
        <label for="faq2" class="faq-question">Pourquoi utiliser les pseudo-classes :hover et :focus ?</label>
        <div class="faq-answer">
          <p>Elles vous permettent de styliser les éléments lorsque les utilisateurs interagissent avec eux, comme changer la couleur d'un bouton lorsqu'il est survolé, rendant les sites web plus interactifs.</p>
        </div>
      </div>
      <!-- Élément FAQ 3 -->
      <div class="faq-item" data-category="important">
        <input type="checkbox" id="faq3" class="faq-toggle" hidden>
        <label for="faq3" class="faq-question">Qu'est-ce que le modèle de boîte CSS ?</label>
        <div class="faq-answer">
          <p>C'est un concept qui inclut les marges, les bordures, le remplissage et la zone de contenu réelle, vous aidant à contrôler l'espacement et la mise en page autour des éléments.</p>
        </div>
      </div>
      <!-- Élément FAQ 4 -->
      <div class="faq-item">
        <input type="checkbox" id="faq4" class="faq-toggle" hidden>
        <label for="faq4" class="faq-question">Comment fonctionne z-index ?</label>
        <div class="faq-answer">
          <p>z-index décide quels éléments apparaissent au-dessus des autres sur la page. Les valeurs plus élevées sont plus proches de l'avant, utiles pour les superpositions ou les menus déroulants.</p>
        </div>
      </div>
      <!-- Élément FAQ 5 -->
      <div class="faq-item">
        <input type="checkbox" id="faq5" class="faq-toggle" hidden>
        <label for="faq5" class="faq-question">Pourquoi utiliser les variables CSS ?</label>
        <div class="faq-answer">
          <p>Elles facilitent la mise à jour des valeurs comme les couleurs ou les polices sur votre site en les changeant en un seul endroit, gardant vos styles cohérents et plus faciles à gérer.</p>
        </div>
      </div>
    </div>
  </div>
</section>

</body>
```

Voici le code CSS :

```css
body {
  background-color: #00ad8f;
}

.faq-section {
  margin-top: 5em; 
}

.faq-section h1 {
  font-size: 2.5em; 
}

.faq-heading {
  text-align: center; 
  margin-bottom: 2em; 
  color: #fff;
}

.container {
  max-width: 800px;
  margin: auto;
  padding: 1em;
}

.faq-item {
  background-color: #fff;
  border-radius: 0.3em;
  border: 1px solid #333;
  margin-bottom: 0.5em;
}

.faq-toggle {
  display: none; /* Masquer la case à cocher */
}

.faq-question {
  background-color: #efefef;
  padding: 1em;
  margin: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  border: none;
  position: relative; /* Nécessaire pour positionner le contenu ::before */
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  border-top: 1px solid #333;
  transition: transform 0.3s ease, padding 0.3s ease;
  padding: 0 1em;
}

.faq-toggle:checked + .faq-question::after {
  content: '-'; /* Change le plus en moins sur la question FAQ lorsque le toggle est coché */
}

.faq-toggle:checked + .faq-question + .faq-answer {
  max-height: 1000px; /* Révèle la réponse lorsque le toggle est coché */
}

 /* nth-of-type pour styliser les questions paires et impaires différemment */
.faq-item:nth-of-type(odd) .faq-question{
 background-color: #fff; /* Pour les éléments impairs */
} 

.faq-item:nth-of-type(even) .faq-question{
 background-color: #caffee; /* Pour les éléments pairs */
}

.faq-item:nth-of-type(odd) .faq-question:hover {
  background-color: #dfdfdf; /* Éclaircit le fond de la question au survol pour un retour visuel */ 
}

.faq-item:nth-of-type(even) .faq-question:hover {
  background-color: #9debd2; /* Éclaircit le fond de la question au survol pour un retour visuel */ 
}

/* First-of-type et last-of-type pour styliser le premier et le dernier élément de manière unique */
.faq-item:first-of-type .faq-question {
  border-top: 2px solid #007BFF;
}

.faq-item:last-of-type .faq-question {
  border-bottom: 2px solid #007BFF;
}

/* ::after utilisé pour afficher le symbole "+" */
.faq-question::after {
  content: '+';
  color: #00ad8f;
  font-size: 1.4em;
}

.faq-item[data-category^="important"] .faq-question {
  color: #E91E63; /* Style les questions importantes différemment */
}
```

# Conclusion

Nous venons de plonger dans le monde des sélecteurs CSS avancés en construisant une section FAQ interactive. Ces sélecteurs avancés vous permettent d'écrire moins de code tout en faisant plus, en gardant votre HTML propre et vos styles nets.

Alors que nous concluons, j'espère que la prochaine fois que vous serez confronté à une décision sur la manière d'aborder le style d'une mise en page complexe ou d'un élément interactif, vous vous souviendrez de la puissance et de la flexibilité que ces sélecteurs CSS avancés offrent et choisirez de les essayer.

* [Google Web Dev sur les sélecteurs CSS](https://web.dev/learn/css/selectors)
* [MDN Web Docs sur les sélecteurs CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)