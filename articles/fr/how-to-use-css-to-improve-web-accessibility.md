---
title: Comment utiliser le CSS pour améliorer l'accessibilité web
subtitle: ''
author: Elizabeth Lola
co_authors: []
series: null
date: '2024-09-18T17:13:12.444Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-to-improve-web-accessibility
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726577970240/02631676-6492-4b83-a057-b9c2048709ee.jpeg
tags:
- name: CSS
  slug: css
- name: frontend
  slug: frontend
- name: a11y
  slug: a11y
- name: webdev
  slug: webdev
- name: Design
  slug: design
seo_title: Comment utiliser le CSS pour améliorer l'accessibilité web
seo_desc: 'Did you know that CSS can play a significant role in web accessibility?
  While CSS primarily handles the visual presentation of a webpage, when you use it
  properly it can enhance the user’s experience and improve accessibility.

  In this article, I''ll s...'
---

Saviez-vous que le CSS peut jouer un rôle important dans l'accessibilité web ? Bien que le CSS gère principalement la présentation visuelle d'une page web, lorsqu'il est utilisé correctement, il peut enrichir l'expérience de l'utilisateur et améliorer l'accessibilité.

Dans cet article, je partagerai quelques façons dont le CSS peut soutenir l'accessibilité afin que vous puissiez commencer à utiliser ces techniques dans vos propres projets.

## Prérequis

Pour suivre ce tutoriel, vous devez avoir une compréhension de base du HTML, du CSS et un peu de JavaScript.

## Mettre à jour les styles de focus

Le navigateur fournit des styles de focus par défaut pour les éléments interactifs comme les boutons ou les champs de saisie. Mais parfois, ces styles de focus par défaut peuvent ne pas être idéaux pour votre système de design – surtout si les couleurs utilisées dans votre design sont trop proches des couleurs par défaut. Cela peut rendre le focus difficile à remarquer.

De plus, différents navigateurs ont des styles de focus par défaut différents et vous pourriez vouloir standardiser les styles de focus pour assurer l'uniformité.

Vous pouvez modifier le style de focus par défaut d'un élément en CSS en utilisant la pseudo-classe `:focus`. Par exemple, le style de focus par défaut pour un élément `input` est un contour bleu dans Chrome et un contour bleu avec un décalage (outline offset) dans Firefox. Pour mettre à jour les styles de focus par défaut d'un élément `input`, vous pouvez faire ceci :

```css
input:focus {
  outline: 2px solid #007BFF;
  outline-offset: 2px;
  border-radius: 1rem;
}
```

## Éviter les décalages de contenu

Les décalages de contenu peuvent se produire lors du chargement différé (lazy loading) d'images, où les images se chargent progressivement à mesure que l'utilisateur fait défiler la page. Parfois, l'image pousse le contenu environnant vers le bas, déplaçant le texte que vous lisez.

Les décalages de contenu peuvent également se produire lors de la récupération de contenu dynamique, en particulier lorsque de nouveaux contenus comme du texte, des images ou des publicités sont ajoutés à la page sans réserver d'espace à l'avance.

Les décalages de contenu peuvent être frustrants, en particulier pour les utilisateurs :

* Ayant des handicaps cognitifs qui peuvent perdre le fil de leur lecture dans le contenu.
    
* Utilisant des loupes d'écran, où le décalage peut leur faire perdre leur focus agrandi.
    
* Naviguant avec un clavier, car cela peut perturber l'ordre naturel des tabulations et rendre la navigation confuse.
    

Vous pouvez pré-allouer de l'espace pour le contenu afin d'éviter les décalages en utilisant les propriétés `min-height` ou `aspect-ratio`. Voici comment vous pouvez allouer de l'espace pour une image afin d'empêcher le décalage de contenu avant que l'image ne soit complètement chargée.

```css
img {
    width: 100%;
    height: auto;
    aspect-ratio: 16/9;
    object-fit: cover; /* Garantit que l'image s'adapte bien à l'espace alloué */
}
```

Vous pouvez également utiliser des animations ou des transitions lors du chargement dynamique de contenu pour ajouter des transitions fluides aux nouveaux éléments. Ainsi, au lieu d'un décalage soudain, le contenu glisse gracieusement, réduisant la perception de perturbation.

```css
.new-content {
    transition: margin 0.3s ease-in-out, opacity 0.3s ease-in-out;
}
```

## Réduire le mouvement

Les animations rapides ou les transitions très complexes peuvent être déroutantes pour les utilisateurs sensibles au mouvement, ce qui pourrait entraîner des inconforts tels que des maux de tête, des étourdissements ou des vertiges (pour les utilisateurs souffrant de troubles vestibulaires).

Vous pouvez utiliser la media query CSS `prefers-reduced-motion` pour réduire ou désactiver les animations pour les utilisateurs.

Personnellement, au lieu de désactiver complètement les animations, je remplace les animations complexes et distrayantes par des animations plus subtiles pour maintenir la fonctionnalité tout en respectant les préférences de l'utilisateur.

Voici comment utiliser `prefers-reduced-motion` pour créer une animation plus simple :

```css
/* Animation par défaut */
@keyframes complexAnimation {
    0% { transform: translateX(0); opacity: 0; }
    50% { transform: translateX(100px); opacity: 0.5; }
    100% { transform: translateX(0); opacity: 1; }
}

.element {
    animation: complexAnimation 2s ease-in-out;
}

/* Animation plus simple pour la préférence de mouvement réduit */
@media (prefers-reduced-motion: reduce) {
    @keyframes simpleAnimation {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .element {
        animation: simpleAnimation 1s ease-in-out;
    }
}
```

Voici un exemple tiré du code ci-dessus. Si vous avez activé le mouvement réduit, vous verrez une balle qui s'estompe au lieu d'une balle en mouvement :

%[https://codepen.io/leezee/embed/preview/PorrrQW?default-tab=result&editable=true] 

**Note** : Si vous souhaitez voir le mouvement réduit en action, vous pouvez l'activer dans l'onglet [rendering de Google Chrome](https://developer.chrome.com/docs/devtools/rendering).

## Focus-within pour les éléments imbriqués

Vous pouvez mettre en évidence ou styliser un élément parent lorsque l'un de ses éléments enfants reçoit le focus, afin de clarifier quel groupe (comme des champs de formulaire ou des menus déroulants) est actuellement l'objet d'une interaction.

Pour ce faire, vous pouvez utiliser la pseudo-classe CSS `:focus-within` qui sert à styliser un élément lorsqu'un de ses descendants reçoit le focus, que ce soit par la navigation au clavier ou par l'interaction de l'utilisateur.

Par exemple, pour mettre en évidence un `fieldset` lorsque n'importe quel élément du groupe a le focus dans un contrôle groupé, vous pouvez faire ceci :

```xml
<style>
 fieldset {
   padding: 10px;
   border: 1px solid #ccc;
 }

 fieldset:focus-within {
   border-color: #007BFF; /* met en évidence le fieldset lorsqu'un utilisateur active le focus sur n'importe quel input */
 }
</style>

<fieldset>
  <legend>Choisissez une couleur :</legend>
  <label><input type="radio" name="color" value="red"> Rouge</label>
  <label><input type="radio" name="color" value="green"> Vert</label>
  <label><input type="radio" name="color" value="blue"> Bleu</label>
</fieldset>
```

## Personnaliser les options de contraste

Parfois, vous travaillez sur un design qui utilise beaucoup de couleurs et qui pourrait ne pas maintenir un contraste élevé entre le texte et l'arrière-plan pour s'adapter à une esthétique. Ou peut-être travaillez-vous sur un design avec beaucoup de couleurs vives. Dans ces cas, vous devriez considérer la manière dont votre application s'affiche pour différents utilisateurs.

Certains utilisateurs malvoyants ou ayant certains types de daltonisme peuvent avoir besoin d'un mode de contraste élevé pour différencier plus clairement le texte de l'arrière-plan. D'autres utilisateurs sensibles aux couleurs vives pourraient préférer une expérience visuelle plus douce et moins agressive.

Certains de ces utilisateurs peuvent avoir réglé leur système sur un contraste élevé ou faible pour améliorer leur expérience. Pour personnaliser leur expérience, vous pouvez utiliser la media query CSS `prefers-contrast`.

La media query `prefers-contrast` vous permet d'adapter le contraste de votre site web ou de votre application en fonction des paramètres système de l'utilisateur.

Voici un exemple d'utilisation de `prefers-contrast` :

```css
/* préférence de style par défaut */
body {
    background-color: white;
    color: black;
}

/* préférence de contraste élevé */
@media (prefers-contrast: more) {
    body {
        background-color: black;
        color: white;
    }
    a {
        color: yellow;
    }
}
/* préférence de contraste faible */

@media (prefers-contrast: less) {
    body {
        background-color: #f0f0f0;
        color: #333;
    }
    a {
        color: #555;
    }
}
```

%[https://codepen.io/leezee/embed/preview/dyBBxgV?default-tab=result&editable=true] 

Dans l'exemple ci-dessus, l'option `prefers-contrast: more` garantit que lorsqu'un utilisateur préfère un contraste élevé, l'arrière-plan est noir et le texte est blanc, avec des liens jaunes pour une meilleure visibilité.

L'option `prefers-contrast: less` ajuste le schéma de couleurs vers une couleur plus douce pour les utilisateurs qui préfèrent moins de contraste. Le style par défaut est utilisé si l'utilisateur n'a pas de préférence de contraste spécifique ou si sa préférence n'est pas détectée.

**Note** : Si votre design utilise peu de couleurs et maintient un contraste élevé entre le texte et l'arrière-plan, ou si vous travaillez sur un design où le texte est minimal et où l'accent est mis sur le contenu visuel (comme des galeries d'images ou des lecteurs vidéo), vous n'aurez peut-être pas autant besoin de `prefers-contrast`. Mais c'est toujours une bonne pratique de prendre en compte les contrastes.

## Activer le mode sombre

Vous pouvez utiliser le CSS pour répondre aux préférences des utilisateurs en matière de mode sombre ou clair. Vous pouvez y parvenir grâce à la media query CSS `prefers-color-scheme`. Le navigateur peut détecter la préférence de couleur de l'utilisateur et appliquer le style s'il est fourni dans le CSS.

Voici un exemple de la façon dont vous pouvez ajouter un style de mode sombre à votre site en utilisant des variables CSS :

```css
:root {
  --background-color: #ffffff;
  --text-color: #000000;
}

@media (prefers-color-scheme: dark) {
  :root {
    --background-color: #000000;
    --text-color: #ffffff;
  }
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
}
```

Dans l'exemple ci-dessus, les variables sont mises à jour si le navigateur détecte une préférence pour un schéma de couleurs sombres.

Si vous souhaitez permettre aux utilisateurs de basculer manuellement entre les modes, vous pouvez utiliser JavaScript pour cela :

```xml
<style>
 /* Styles du mode clair par défaut */
  body {
   background-color: #ffffff;
   color: #000000;
  }
 /* Styles du mode sombre */
  body.dark-mode {
   background-color: #000000;
   color: #ffffff;
  }
</style>

<button id="toggle-theme">Changer de thème</button>

<script>
  const toggleButton = document.getElementById('toggle-theme');
  toggleButton.addEventListener('click', () => {
   document.body.classList.toggle('dark-mode');
  });
</script>
```

## Utiliser les unités `rem` pour une typographie responsive

L'utilisation des unités `rem` pour une typographie responsive peut aider à améliorer l'accessibilité en s'adaptant de manière plus dynamique aux préférences d'un utilisateur. Étant donné que `rem` est relatif à la taille de police racine (généralement définie par le navigateur ou l'utilisateur), il s'ajuste aux changements de la taille de police de base. Cela permet de garantir que le texte reste lisible sans casser les mises en page.

Les utilisateurs peuvent définir une taille de police préférée dans leur navigateur ou leur système d'exploitation pour une meilleure lisibilité. Lorsque vous utilisez `rem`, le contenu du site web s'adapte selon ce réglage, ce qui garantit que le texte n'est ni trop petit ni trop grand pour les utilisateurs (ce qui peut arriver lors de l'utilisation d'unités fixes comme `px`).

Lorsque les utilisateurs zooment via les paramètres du navigateur ou augmentent leur taille de texte préférée, le texte basé sur `rem` s'ajustera de manière appropriée.

La taille de police racine par défaut (généralement 16px) est normalement héritée du navigateur, mais vous pouvez la définir explicitement si nécessaire :

```css
html {
  font-size: 100%; /* 16px par défaut */
}
```

Après avoir défini la taille de police racine, vous pouvez utiliser l'unité `rem` pour le reste de votre contenu. Par exemple :

```css
h1 {
  font-size: 2.5rem; /* Équivalent à 40px si la racine est à 16px */
}

p {
  font-size: 1rem; /* Équivalent à 16px */
}
```

## Utiliser les animations pour améliorer l'UX

Les animations CSS peuvent améliorer l'accessibilité lorsqu'elles sont utilisées avec discernement. Elles peuvent aider à créer une expérience attrayante et compréhensible pour les utilisateurs.

Voici quelques façons dont les animations peuvent aider à améliorer l'accessibilité :

* Vous pouvez utiliser des animations pour indiquer un état de chargement afin de communiquer visuellement aux utilisateurs que le système travaille sur une tâche.
    
* L'utilisation d'effets de texte animés, comme des fondus ou des mises à l'échelle sur les titres ou les sections importantes, peut aider à guider le regard des utilisateurs vers le contenu important. Cela peut être utile pour les personnes ayant des handicaps cognitifs qui bénéficient de hiérarchies visuelles claires.
    
* Des transitions subtiles pour les changements d'état au lieu de changements brusques (comme une fenêtre modale apparaissant instantanément) peuvent créer des transitions plus fluides entre les différents états de l'interface.
    
* L'utilisation de mises en évidence animées ou d'effets de tremblement sur les champs de formulaire peut fournir un retour visuel aux utilisateurs concernant les erreurs de saisie. Vous devriez coupler ces animations avec des libellés ou des attributs ARIA pour clarifier ce que l'utilisateur doit corriger.
    
* Les animations peuvent aider les utilisateurs à suivre le focus, en particulier les utilisateurs au clavier ou ceux ayant des déficiences visuelles. Les transitions CSS qui mettent en évidence les éléments focalisés (par exemple en agrandissant les boutons ou en changeant la bordure) aident les utilisateurs à comprendre où ils se trouvent dans la page.
    

### Bonnes pratiques :

* Assurez-vous que les animations sont utilisées à bon escient, et pas seulement pour des raisons esthétiques.
    
* Évitez les animations trop longues ou continues qui peuvent distraire ou agacer les utilisateurs.
    
* Combinez les animations avec d'autres fonctionnalités d'accessibilité, telles que les annonces de lecteurs d'écran, pour garantir que tous les utilisateurs comprennent les changements de contenu.
    

## Conclusion

Lorsque l'on considère l'accessibilité, un HTML bien structuré constitue la base d'une page accessible – mais le CSS joue également un rôle vital dans l'amélioration de cette structure.

Le CSS seul ne peut pas corriger un HTML mal structuré. Mais lorsqu'il est appliqué de manière réfléchie sur une base solide, il garantit une expérience plus inclusive et engageante en améliorant la hiérarchie visuelle, la lisibilité et l'interaction pour les utilisateurs de toutes capacités.

Combiner un HTML accessible avec du CSS améliore non seulement l'interface utilisateur, mais fournit également un soutien pour les technologies d'assistance.

Merci beaucoup d'avoir lu cet article. Si vous l'avez trouvé utile, n'hésitez pas à le partager. Bon codage !

Vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/elizabeth-meshioye/).