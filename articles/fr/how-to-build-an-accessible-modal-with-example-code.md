---
title: Comment construire une modale accessible – avec exemple de code
subtitle: ''
author: Elizabeth Lola
co_authors: []
series: null
date: '2024-08-27T15:10:54.560Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-accessible-modal-with-example-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724337698676/aa23c219-2ffb-4424-bb34-3195a905d973.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: frontend
  slug: frontend
- name: HTML5
  slug: html5
seo_title: Comment construire une modale accessible – avec exemple de code
seo_desc: We often use modals or popups to display important information or prompt
  users to take action. Unlike regular pop-ups that can be opened in new windows or
  tabs, these dialogues keep the user on the same page by overlaying the existing
  content. This e...
---

Nous utilisons souvent des modales ou des popups pour afficher des informations importantes ou inciter les utilisateurs à agir. Contrairement aux fenêtres surgissantes classiques qui peuvent s'ouvrir dans de nouvelles fenêtres ou onglets, ces dialogues maintiennent l'utilisateur sur la même page en se superposant au contenu existant. Cela garantit que les utilisateurs restent concentrés sur la tâche en cours.

Les modales sont courantes et parfois nécessaires. Cependant, si elles ne sont pas implémentées correctement, elles peuvent constituer une barrière significative. S'assurer que les modales sont accessibles signifie qu'elles sont utilisables par tous, y compris par les personnes qui dépendent des technologies d'assistance.

Dans cet article, nous allons **construire une modale** en suivant les directives pour la rendre accessible.

## **Prerequisites**

Pour suivre ce tutoriel, vous devriez avoir :

1. **Des connaissances de base en HTML :** Comprendre le fonctionnement des éléments et des attributs HTML.
    
2. **Des connaissances de base en JavaScript :** Une familiarité avec les concepts de base de JavaScript comme les fonctions, la gestion des événements et la manipulation du DOM est utile.
    
3. **Une compréhension d'ARIA :** Bien que le tutoriel explique les rôles et attributs ARIA, avoir une compréhension de base des concepts d'accessibilité peut être bénéfique.
    

## Quand devriez-vous utiliser une modale ?

L'utilisation efficace des modales nécessite une réflexion approfondie sur l'expérience utilisateur. Voici quelques directives pour vous aider à décider si vous devez utiliser une modale ou non :

* Vous devriez utiliser des modales lorsque l'utilisateur doit prendre une décision critique, comme confirmer une action potentiellement destructrice (par exemple, supprimer un élément) ou accepter des conditions générales.
    
* Vous pouvez utiliser une modale lorsqu'une tâche nécessite toute l'attention de l'utilisateur et ne repose pas sur les informations du reste de la page (par exemple, remplir un formulaire ou finaliser un processus de paiement).
    
* Vous pouvez utiliser une modale pour afficher des informations temporaires ou transitoires qui n'ont pas besoin d'être visibles en permanence sur la page (par exemple, des alertes, des notifications ou des messages brefs).
    
* Vous devriez éviter d'utiliser des modales pour des tâches nécessitant une interaction ou une saisie importante, comme des formulaires longs ou des flux de travail complexes. Ceux-ci peuvent être frustrants dans une modale en raison de l'espace limité et des contraintes de navigation.
    
* Vous devriez éviter d'utiliser des modales pour des actions qu'un utilisateur devra effectuer fréquemment, car cela peut devenir répétitif et agaçant. Des options intégrées (inline) ou des info-bulles (tooltips) pourraient être préférables pour les actions répétitives.
    
* Vous ne devriez pas utiliser de modales si elles interrompent le flux naturel de l'utilisateur sur le site, surtout si le contenu ou l'action dans la modale n'est pas urgent ou important.
    

## Directives d'accessibilité des modales

Voici quelques conseils pour vous aider à construire des modales utiles et accessibles :

* Fournissez un attribut `aria-labelledby` descriptif qui pointe vers le titre ou l'en-tête de la modale. S'il n'y a pas de titre, utilisez `aria-label` pour fournir un libellé court et descriptif.
    

* Incluez toujours un bouton de fermeture visible et facilement accessible dans la modale, généralement dans le coin supérieur droit. Étiquetez ce bouton clairement, par exemple avec le texte "Fermer" ou une icône avec `aria-label="Fermer"`.
    
* Lorsque la modale s'ouvre, déplacez le focus du clavier vers le premier élément interactif de la modale (généralement un bouton de fermeture). Lorsque la modale se ferme, ramenez le focus sur l'élément qui a déclenché l'ouverture de la modale.
    
* Maintenez le focus du clavier à l'intérieur de la modale tant qu'elle est ouverte.
    
* Permettez aux utilisateurs de fermer la modale en appuyant sur la touche `Echap`.
    

En suivant ces directives, construisons une modale.

Je préfère utiliser les bonnes balises HTML pour construire des composants, et dans ce cas, c'est exactement ce que je vais faire en utilisant la balise `dialog`.

## Comment construire une modale en utilisant la balise `dialog`

Au cas où vous ne seriez pas familier avec la balise `dialog`, elle a été introduite en HTML5. Vous l'utilisez pour créer des boîtes de dialogue comme des popups, des alertes et des modales. Elle offre des méthodes et des attributs intégrés qui facilitent la gestion du comportement des dialogues sans avoir besoin de beaucoup de JavaScript. Les méthodes JavaScript intégrées sont `show()`, `showModal()` et `close()`.

### `show()` et `showModal()`

La méthode `show()` est utile pour un dialogue non bloquant. Cela signifie que le dialogue apparaît par-dessus le contenu actuel, mais que les utilisateurs peuvent toujours interagir avec d'autres parties de la page Web (cliquer sur des boutons, des liens, etc.) pendant que le dialogue est ouvert.

C'est utile dans les situations où le dialogue fournit des informations qui ne nécessitent pas l'attention immédiate de l'utilisateur. Voici un exemple :

```xml
<!-- Contenu précédent ici -->
<dialog id="dialog-box">
<!-- Plus de contenu ici -->
</dialog>

<script>
    const dialog = document.getElementById('dialog-box');
    dialog.show();
</script>
```

Résultat :

![un dialogue non modal](https://cdn.hashnode.com/res/hashnode/image/upload/v1723822375653/a592c09a-747c-4248-84e2-9cd76c8f6498.png align="center")

La méthode `showModal()` ouvre le dialogue en mode modal. Cela signifie que le dialogue prend le focus et que l'interaction avec le reste de la page Web est bloquée jusqu'à ce que le dialogue soit fermé. L'utilisateur ne peut cliquer sur aucune autre partie de la page, ni interagir avec elle.

Selon le navigateur, un arrière-plan semi-transparent (backdrop) apparaît derrière le dialogue, indiquant visuellement que le reste de la page n'est pas interactif.

Lorsqu'un dialogue est ouvert avec `showModal()`, le focus est automatiquement piégé à l'intérieur du dialogue. L'utilisateur ne peut naviguer qu'entre les éléments à l'intérieur du dialogue à l'aide de la touche tabulation, et le focus bouclera dans le contenu du dialogue jusqu'à sa fermeture. Voici un exemple :

```xml
<dialog id="dialog-box">
<!-- Plus de contenu ici -->
</dialog>

<script>
    const dialog = document.getElementById('dialog-box');
    dialog.showModal();
</script>
```

Résultat :

![une boîte de dialogue modale](https://cdn.hashnode.com/res/hashnode/image/upload/v1723823970852/1ca30713-199d-4b94-b12a-ad1a27a9063f.png align="center")

L'élément `<dialog>` possède des styles par défaut mais peut être personnalisé via CSS pour correspondre à votre design. Vous pouvez styliser la boîte de dialogue, ajouter des animations ou modifier l'arrière-plan. L'arrière-plan peut être stylisé à l'aide du sélecteur `::backdrop`. Par exemple :

```css
dialog::backdrop {
    background: rgba(0, 0, 0, 0.7);
}
```

Le dialogue est également doté de fonctionnalités d'accessibilité intégrées telles que la gestion du focus, l'arrière-plan, l'annonce automatique à l'ouverture, et l'appui sur la touche `ECHAP` fermera le dialogue.

You pouvez ajouter l'attribut `autofocus` au premier élément interactif de la modale, comme le premier champ d'un formulaire ou le bouton de fermeture. Alternativement, vous pouvez compter sur la gestion native du focus de l'élément `<dialog>`.

Évitez d'utiliser `tabindex` sur l'élément `<dialog>`, car ce n'est pas un élément interactif comme un bouton ou un lien. Le `<dialog>` sert de conteneur pour le contenu interactif et n'est pas destiné à recevoir directement le focus de l'utilisateur.

L'élément `<dialog>` offre un moyen natif de créer des modales. Si vous construisez une modale personnalisée, assurez-vous que ses fonctionnalités d'accessibilité correspondent à celles de l'élément `<dialog>` natif.

En résumé :

```xml
<style>
    dialog::backdrop {
        background: rgba(0, 0, 0, 0.7);
    }
</style>
<body>
    <button id="open-dialog">Ouvrir le dialogue</button>
    <dialog id="dialog-box">
        <h2>Titre de la modale</h2>
        <div>
          <!-- Plus de contenu ici -->
          <button id="close-dialog" autofocus>Fermer</button>
        </div>
    </dialog>

<script>
    const dialog = document.getElementById("dialog-box");
    const openButton = document.getElementById("open-dialog");
    const closeButton = document.getElementById("close-dialog");

    openButton.addEventListener("click", () => {
      dialog.showModal();
    });
    closeButton.addEventListener("click", () => {
      dialog.close();
    });
</script>
</body>
```

Vous remarquerez que je n'ai pas utilisé l'attribut `aria-label` sur le dialogue comme je l'avais listé dans les directives. Eh bien, c'est parce que l'élément dialog, s'il est bien structuré, n'en a pas forcément besoin. Dans ce cas, il y a une étiquette visible dans l'élément dialog (l'élément `h2`).

S'il n'y a pas d'étiquettes visibles présentes, vous devez en ajouter une. Comme dans cet exemple :

```xml
<dialog id="confimation-dialog" aria-label="Dialogue de confirmation">
    <p>Êtes-vous sûr de vouloir continuer ?</p>
    <button id="close-dialog" autofocus>Fermer</button>
</dialog>
```

## Qu'est-ce que l'attribut `inert` ?

Lorsqu'une modale est ouverte, un lecteur d'écran peut toujours naviguer vers le contenu situé à l'extérieur de la modale. Vous souhaiterez généralement que le focus de l'utilisateur soit limité à la modale elle-même, ou empêcher l'utilisateur de cliquer accidentellement sur des éléments en dehors de la modale pour éviter toute confusion et erreur. Dans ces cas, vous aurez besoin de l'attribut `inert`.

L'attribut `inert` rend un élément et tous ses descendants non interactifs et inaccessibles aux technologies d'assistance. Lorsqu'une modale est ouverte, l'utilisation de l'attribut `inert` sur le reste du contenu de la page garantira que seul le contenu de la modale est accessible, rendant l'expérience du dialogue plus claire.

### Comment utiliser l'attribut `inert` ?

Lorsqu'une modale est ouverte, vous pouvez appliquer l'attribut `inert` au reste du contenu de la page (généralement l'élément `<main>`). Lorsque la modale est fermée, vous supprimez l'attribut `inert`.

Voici un exemple montrant comment utiliser `inert` avec un dialogue modal :

```xml
<body>
    <header>En-tête du site</header>
    <main id="main-content">
        <button id="open-dialog">Ouvrir la modale</button>
        <p>Ceci est le contenu principal de la page.</p>
        <!-- Plus de contenu ici -->
        
    </main>
    <!-- Déplacer le dialogue à l'extérieur de l'élément main -->
    <dialog id="dialog">
        <h2>Titre de la modale</h2>
        <p>Ceci est le contenu à l'intérieur de la modale.</p>
        <button id="close-dialog" autofocus>Fermer</button>
    </dialog>

    <script>
        const dialog = document.getElementById('dialog');
        const mainContent = document.getElementById('main-content');
        const openButton = document.getElementById('open-dialog');
        const closeButton = document.getElementById('close-dialog');

        openButton.addEventListener("click", () => {
           mainContent.setAttribute('inert', '');
          dialog.showModal();
        });
        
        closeButton.addEventListener("click", () => {
           dialog.close();
        });
        
        // l'élément dialog possède un événement close, qui est appelé lorsqu'un utilisateur appelle la méthode close() ou appuie sur la touche echap
        dialog.addEventListener("close", (event) => {
           mainContent.removeAttribute("inert");
        });
    </script>
</body>
```

## Comment animer les états d'ouverture et de fermeture

Lorsqu'une modale apparaît (état ouvert) ou disparaît (état fermé), cela peut être brusque pour les utilisateurs si cette transition se produit soudainement. Animer ces états peut créer une expérience utilisateur plus fluide en introduisant ou en retirant progressivement la modale, la rendant plus naturelle.

#### Pourquoi animer les états d'ouverture et de fermeture ?

Animer les états d'ouverture et de fermeture d'une modale peut :

* **Améliorer l'expérience utilisateur** : Une animation fluide peut rendre la transition moins abrupte et plus engageante.
    
* **Attirer l'attention** : Des animations subtiles peuvent aider à guider le focus de l'utilisateur vers le contenu de la modale lorsqu'elle apparaît.
    
* **Maintenir la cohérence** : Des animations cohérentes dans votre interface utilisateur peuvent créer une impression de cohésion et de professionnalisme.
    

Par défaut, le dialogue est défini sur `display:none` lorsqu'il est fermé et `display:block` lorsqu'il est ouvert. Vous ne pouvez pas effectuer de transition de `none` à `block` en CSS, mais vous pouvez combiner les propriétés d'affichage avec `transform` ou `opacity`. La propriété `transform` peut être utilisée pour redimensionner ou déplacer la modale, tandis que `opacity` contrôle sa transparence.

Voici un exemple de la façon dont vous pourriez animer une modale :

```css
dialog {
  animation: zoom-out 0.5s ease-out;
}

/* un attribut open est ajouté au dialogue lorsqu'il est ouvert */
dialog[open] {
    animation: zoom-in 0.5s ease-out;
}

/* La propriété display dans les keyframes est critique 
parce qu'elle bascule la visibilité de la modale. */
@keyframes zoom-in {
    0% {
      opacity: 0;
      transform: scale(0.1);
      display:  none;
    }
    100% {
      opacity: 1;
      transform: scale(1);
      display: block;
    }
}

@keyframes zoom-out {
    0% {
      opacity: 1;
      transform: scale(1);
      display: block;
    }
    100% {
      opacity: 0;
      transform: scale(0);
      display: none;
    }
}
```

Résultat final :

%[https://codepen.io/leezee/embed/preview/XWLVBgp?default-tab=result&editable=true] 

## Conclusion

L'élément `<dialog>` est le moyen natif de créer des modales. Il fournit des fonctionnalités d'accessibilité intégrées pour les utilisateurs de clavier et de lecteurs d'écran.

L'élément `<dialog>` est de deux types : modal et non-modal. Vous pouvez créer un dialogue non-modal en utilisant la méthode `show()`, et la méthode `showModal()` créera un dialogue modal.

Lorsque vous n'utilisez pas l'élément de dialogue natif, assurez-vous que votre modale personnalisée correspond au dialogue natif en termes d'accessibilité afin de garantir une expérience uniforme pour tous les utilisateurs.

Vous devriez également toujours vous rappeler de mettre le focus automatiquement sur l'élément interactif le plus immédiat ; le dialogue peut le faire par défaut.

Enfin, vous pouvez utiliser l'attribut `inert` sur d'autres éléments pour empêcher l'accès à ces éléments lorsque la modale est ouverte.

### Ressources :

* [Rôle W3c Dialog](https://w3c.github.io/aria/#dialog)
    
* [MDN : L'élément Dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
    

Merci beaucoup d'avoir lu cet article. Si vous l'avez trouvé utile, n'hésitez pas à le partager. Bon codage !

Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/elizabeth-meshioye/).