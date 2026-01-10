---
title: Tout ce que vous devez savoir sur l'accessibilité web
date: '2025-03-18T17:16:08.825Z'
author: Kunal Nalawade
authorURL: https://www.freecodecamp.org/news/author/KunalN25/
originalURL: https://freecodecamp.org/news/the-web-accessibility-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742318086251/103cec5f-3330-4559-8554-4ec76b16ec76.png
tags:
- name: Accessibility
  slug: accessibility
- name: a11y
  slug: a11y
- name: handbook
  slug: handbook
- name: Web Development
  slug: web-development
- name: Web Design
  slug: web-design
seo_desc: 'The web is a great place to access information and connect with people.
  It has opened up countless opportunities, making life more convenient in many ways.

  But not everyone experiences the web in the same way. Websites are difficult to
  use for people...'
---


Le web est un endroit formidable pour accéder à l'information et se connecter avec les gens. Il a ouvert d'innombrables opportunités, rendant la vie plus pratique à bien des égards.

<!-- more -->

Mais tout le monde ne vit pas le web de la même manière. Les sites web sont difficiles à utiliser pour les personnes présentant des déficiences visuelles, auditives ou motrices. Ces barrières rendent la navigation dans le contenu plus complexe et, dans certains cas, rendent le web complètement inaccessible.

Ce guide vous aidera à comprendre l'accessibilité et comment la mettre en œuvre. Que vous soyez un développeur débutant ou intermédiaire, vous apprendrez les pratiques de base de l'accessibilité ainsi que certaines techniques avancées. Cela vous aidera à rendre votre site web plus inclusif.

C'est parti.

## Table des matières

-   [Qu'est-ce que l'accessibilité ?][1]
    
-   [Pratiques d'accessibilité de base][2]
    
    -   [HTML sémantique et non sémantique][3]
        
    -   [Contenu textuel][4]
        
    -   [Mises en page][5]
        
    -   [Éléments interactifs][6]
        
    -   [Accessibilité au clavier][7]
        
    -   [Étiquettes de formulaire][8]
        
    -   [Liens][9]
        
    -   [Accessibilité des tableaux][10]
        
-   [Pratiques CSS et JavaScript supplémentaires][11]
    
    -   [Styliser les éléments de formulaire][12]
        
    -   [Contraste des couleurs][13]
        
    -   [Pratiques JavaScript][14]
        
-   [Pratiques d'accessibilité avancées : WAI-ARIA][15]
    
    -   [L'attribut role][16]
        
    -   [Attribut aria-*][17]
        
    -   [Attributs de contenu dynamique][18]
        
    -   [Validation de formulaire et erreurs][19]
        
    -   [Utiliser des éléments non sémantiques comme boutons][20]
        
-   [Accessibilité multimédia][21]
    
-   [Accessibilité mobile][22]
    

## Qu'est-ce que l'accessibilité ?

L'accessibilité (A11y) est une pratique importante du développement web qui vise à rendre le site web utilisable (accessible) par tous. Cela inclut les personnes ayant des handicaps qui rendent l'utilisation des sites web difficile. En rendant un site web accessible à tous, y compris aux personnes handicapées, nous garantissons qu'elles disposent des mêmes opportunités que nous. Nous contribuons également à faire du web un espace plus inclusif de manière générale.

Quels types de handicaps devrions-nous prendre en compte ? De manière générale :

-   Déficiences visuelles : cécité, vision floue et daltonisme
    
-   Déficiences auditives : audition faible ou nulle
    
-   Déficiences motrices : difficulté de mouvement physique
    
-   Déficiences cognitives : comme la dyslexie et le TDAH
    

Les personnes ayant des déficiences visuelles utilisent couramment des appareils comme les [lecteurs d'écran][23] pour visualiser et comprendre le contenu d'un site web, par exemple. Une grande partie de l'accessibilité web consiste donc à concevoir un site web qui puisse être facilement consulté par un lecteur d'écran.

Il existe diverses pratiques que vous pouvez suivre en tant que développeur pour rendre un site web accessible, que je vais aborder dans ce guide.

## Pratiques d'accessibilité de base

L'accessibilité n'est pas seulement une fonctionnalité ajoutée par-dessus un site web que vous avez déjà développé. C'est une pratique qui doit être suivie tout au long du processus de développement. Chaque fois que vous créez du contenu sur une page web, demandez-vous s'il est réellement accessible.

Un autre point important est que l'accessibilité n'est pas réservée aux personnes handicapées. Elle profite à tout le monde en rendant un site web plus facile à utiliser, améliorant ainsi l'expérience utilisateur globale.

Comment obtenir une bonne accessibilité ? Eh bien, il existe certaines pratiques que vous devriez suivre lors de l'écriture de votre code HTML, CSS et JavaScript. Nous allons discuter de quelques pratiques de base dans cette section.

Avant d'entrer dans le vif du sujet, commençons par comprendre ce que sont les balises HTML sémantiques et non sémantiques :

### HTML sémantique et non sémantique

Les balises HTML non sémantiques ne transmettent pas de signification ou de but spécifique. Elles peuvent être utilisées pour n'importe quoi, en fonction du style CSS et des fonctionnalités JavaScript. Des exemples de balises non sémantiques sont : `<div>` et `<span>`. Ces balises sont principalement utilisées comme conteneurs pour envelopper d'autres éléments.

Les balises HTML sémantiques décrivent clairement leur but au navigateur et aux développeurs grâce à leur nom. Elles améliorent la lisibilité du code et aident également au [SEO (Search Engine Optimisation)][24]. Des exemples de balises sémantiques incluent : `<button>`, `<a>`, `<header>`, `<footer>`.

Vous pouvez trouver une liste de tous les éléments sémantiques [ici][25].

#### Importance de l'utilisation du HTML sémantique

Une partie essentielle de l'accessibilité consiste à utiliser l'élément HTML correct pour l'usage prévu. Cela signifie, par exemple, utiliser une balise `<button>` lorsque vous souhaitez afficher un bouton.

Mais pourquoi utiliser des éléments sémantiques ? Après tout, vous pouvez utiliser du CSS pour faire ressembler un `<div>` à un bouton. C'est vrai, mais l'utilisation d'éléments sémantiques est importante pour les raisons suivantes :

-   Les éléments sémantiques possèdent des styles et des fonctionnalités intégrés que vous devriez autrement ajouter via CSS et JavaScript. Cela les rend plus faciles à utiliser.
    
-   Ils rendent le code plus facile à lire et à maintenir, car vous pouvez réellement voir les éléments utilisés au lieu de voir une multitude de divs partout.
    
-   Les lecteurs d'écran peuvent facilement lire et interpréter les éléments sémantiques, ce qui aide les personnes ayant des déficiences visuelles.
    

Dans les sections suivantes, nous comprendrons les pratiques d'accessibilité de base pour chaque type de contenu que vous affichez en HTML. Nous explorerons comment utiliser les bonnes balises HTML pour chaque situation, vous aidant à voir comment le choix de la bonne balise améliore l'accessibilité.

N'hésitez pas à tester chaque exemple avec un lecteur d'écran. Sur Mac, utilisez ⌘+F5 pour activer VoiceOver, le lecteur d'écran intégré de Mac. Pour Windows, vous pouvez utiliser le lecteur d'écran intégré appelé Narrator en appuyant sur Ctrl + Touche Windows + Entrée.

### Contenu textuel

Lors de la rédaction de contenu textuel, il est important d'utiliser les éléments corrects pour les titres, les paragraphes et les listes. Comprenons cela avec les exemples suivants.

Supposons que vous écriviez des titres et des paragraphes de la manière suivante :

```
<span id="heading1">Titre 1</span>
<br />
<br />
<span id="heading2">Titre 2</span>
<br />
<br />
Ceci est un paragraphe
<br />
<br />
Ceci est un autre paragraphe
```

Cette approche présente les problèmes suivants :

-   Le lecteur d'écran ne pourra pas distinguer les titres des paragraphes – il lira simplement le contenu d'un trait, déroutant ainsi les personnes qui dépendent des lecteurs d'écran.
    
-   Il est difficile de styliser des paragraphes individuels, car il n'y a pas de sélecteurs. Même si vous ajoutez un `<span>` à chacun, cela nécessite un style CSS supplémentaire.
    
-   Le code contient également des sauts de ligne inutiles qui pourraient être évités en utilisant les bons éléments.
    

Le code ci-dessus est un exemple de mauvaise sémantique. Voici ce que vous devriez faire à la place :

```
<h1>Titre 1</h1>
<h2>Titre 2</h2>
<p>Ceci est un paragraphe</p>
<p>Ceci est un autre paragraphe</p>
```

Ici, nous avons utilisé les bons éléments sémantiques pour le contenu textuel, ce qui présente les avantages suivants :

-   Un lecteur d'écran est capable de distinguer les titres du texte du paragraphe en annonçant le niveau du titre avant de lire le texte.
    
-   `h1`, `h2` et `p` possèdent des styles intégrés et s'affichent chacun sur une nouvelle ligne. Cela élimine le besoin d'utiliser des sauts de ligne.
    
-   Le code est plus propre et beaucoup plus lisible.
    

#### Listes

Pour afficher une liste d'éléments, nous avons les approches suivantes. L'approche non sémantique regroupe simplement un tas de divs et leur applique des styles CSS.

```
<h2>Liste de tâches</h2>
<div id="mylist">
  <div>Préparer le petit-déjeuner</div>
  <div>Faire la lessive</div>
  <div>Terminer l'article de blog</div>
</div>
```

Encore une fois, cela permet d'obtenir le résultat visuel souhaité, mais il est difficile pour les lecteurs d'écran d'identifier ce contenu comme une liste d'éléments. Utilisez plutôt des éléments sémantiques :

```
<h2>Liste de tâches</h2>
<ul id="mylist">
  <li>Préparer le petit-déjeuner</li>
  <li>Faire la lessive</li>
  <li>Terminer l'article de blog</li>
</ul>
```

Cela aide les lecteurs d'écran à identifier l'élément comme une liste non ordonnée et à lire chaque élément. `<ul>` vient également avec des styles par défaut et des puces pour chaque élément de la liste. Vous pouvez également utiliser `<ol/>` pour les listes numérotées, où le lecteur d'écran lit le numéro de chaque élément.

Vous pouvez tester les exemples ci-dessus avec VoiceOver de Mac pour voir la différence.

#### Texte accentué

Le texte accentué fait référence au texte mis en évidence qui donne de l'importance à certains mots ou phrases dans un contenu. Lors de l'ajout de texte accentué, il est important d'utiliser les bons éléments sémantiques comme [`<strong>`][26] et [`<em>`][27].

```
<p>Pour de meilleurs résultats, utilisez des <em>ingrédients frais</em> lors de la cuisson.</p>

<p>Le processus de transformation de l'eau en gaz s'appelle l'<strong>évaporation</strong>.</p>
```

Ces éléments ajoutent des styles intégrés au texte comme le **gras** et l'*italique*. De plus, si vous testez avec VoiceOver, vous remarquerez qu'il met une certaine emphase sur le texte à l'intérieur de ces éléments. Cela aide les personnes utilisant des lecteurs d'écran à identifier le texte accentué.

Vous pouvez également ajouter de la couleur au texte accentué. Mais il n'est pas nécessaire d'ajouter trop de styles, sinon cela pourrait prêter à confusion. Consultez la [Documentation MDN - Emphase et importance][28] pour en savoir plus sur l'accentuation du texte en HTML.

#### Abréviations

Ensuite, lors de l'écriture d'abréviations (ou d'acronymes), c'est une bonne pratique de les rendre visuellement différentes et d'inclure également le développement complet de l'acronyme. Vous pouvez également ajouter un style simple à l'abréviation. En savoir plus sur les abréviations dans la [Documentation MDN - Abréviations][29].

#### Autres bonnes pratiques

En dehors de ce qui précède, voici quelques autres pratiques qu'il est bon de suivre :

-   Utilisez un langage clair, autant que possible. Par exemple, développez les abréviations : au lieu de Jan., écrivez Janvier.
    
-   Lors de l'écriture de plages, évitez d'utiliser des tirets si possible, écrivez "1 à 5" au lieu de "1-5".
    
-   Évitez d'utiliser des caractères qui pourraient dérouter les utilisateurs lorsqu'un lecteur d'écran les lit, par exemple `~` ou `*`.
    
-   Évitez les exclamations excessives et les emojis.
    

De plus, lors de l'écriture du CSS pour le contenu textuel, n'oubliez pas ces pratiques :

-   Lorsque vous utilisez des styles tels que la taille de la police, la hauteur de ligne et l'espacement des lettres, assurez-vous que le texte est confortable à lire.
    
-   Vos titres doivent se démarquer du reste du texte si vous utilisez des styles CSS. Généralement, cela est réalisé simplement en utilisant les bonnes balises de titre.
    
-   La couleur du texte doit avoir un contraste de 4,5:1 avec l'arrière-plan. Voir la section [Contraste des couleurs][30] pour plus de détails.
    

Si vous voulez plus de conseils sur le style du texte, consultez la [Documentation MDN - Style du texte CSS][31].

### Mises en page

La mise en page concerne la façon dont le contenu est disposé sur l'écran. Lorsque vous commencez à concevoir une page web, votre première pensée est de savoir comment votre contenu doit être positionné.

Typiquement, une page web se compose d'un en-tête, d'une barre de navigation, d'un pied de page, d'un contenu principal et d'une barre latérale. À l'"époque sombre" (expression empruntée à la doc, désolé), les développeurs utilisaient des tableaux pour créer des mises en page composées de ces éléments.

Mais les tableaux rendaient les mises en page incroyablement complexes et difficiles à maintenir. Les mises en page par tableaux sont également difficiles à lire pour les lecteurs d'écran, ce qui affecte l'accessibilité.

Aujourd'hui, il existe de bien meilleures façons d'écrire des mises en page. Si vous incluez un en-tête, une barre de navigation et un pied de page avec le contenu principal, vous pouvez utiliser les éléments sémantiques suivants :

```
<header>
  <h1>En-tête</h1>
  <nav>
    <!-- navigation principale ici -->
  </nav>
</header>

<!-- Voici le contenu principal de notre page -->
<main>
  <!-- Contenu principal ici -->
</main>

<footer>
  <!-- contenu du pied de page ici -->
</footer>
```

Comprenons chaque balise utilisée ci-dessus (passez si vous le savez déjà) :

-   `<header>` : Représente la section d'introduction d'une page web, contenant généralement des titres, des logos ou des liens de navigation.
    
-   `<nav>` : Définit une section de navigation qui contient des liens vers d'autres parties du site web ou de la page, offrant un accès facile aux sections importantes.
    
-   `<main>` : Représente la zone de contenu principal qui se concentre sur le but premier de la page ou du site web, à l'exclusion des éléments communs comme l'en-tête, le pied de page ou la barre latérale (peut inclure la barre latérale selon le site).
    
-   `<footer>` : Représente la section du bas de la page web, contenant généralement des métadonnées, des informations de copyright ou des liens vers des ressources connexes.
    

Ces éléments sont appelés [éléments de sectionnement][32]. Voici les avantages de l'utilisation de ces éléments :

-   La mise en page est claire, chaque élément décrivant précisément son but, ce qui rend le code lisible et maintenable.
    
-   L'utilisation des bons éléments sémantiques permet aux lecteurs d'écran d'identifier chaque partie de la mise en page, aidant ainsi les utilisateurs malvoyants à comprendre la structure du site web.
    

Bien sûr, vous pouvez écrire les mises en page ci-dessus en utilisant des divs, mais les éléments de sectionnement offrent une bonne sémantique et aident les utilisateurs à comprendre le type de contenu dans lequel ils naviguent.

### Éléments interactifs

Il s'agit des éléments par lesquels un utilisateur interagit avec la page web. Ces éléments incluent les boutons, les champs de formulaire, les liens, etc.

#### Accessibilité au clavier

Chaque élément interactif d'une page web doit être navigable via le clavier. Cela donne de la flexibilité à l'utilisateur lors de la navigation sur votre site. L'accessibilité au clavier est réellement utile pour les personnes ayant des déficiences motrices qui pourraient avoir du mal à utiliser une souris.

Par exemple, visitez [cette][33] page et essayez de naviguer vers chaque élément interactif en appuyant sur Tab sur votre clavier. Vous pouvez également appuyer sur Entrée/Espace pour cliquer sur un bouton ou un lien. Cela devrait vous donner une idée de ce à quoi ressemble un site web accessible au clavier.

Pour la plupart, l'utilisation des bons éléments sémantiques devrait garantir l'accessibilité au clavier, car ils possèdent des fonctionnalités intégrées. Regardez l'exemple suivant :

```
<p>
  Visitez mon blog sur 
  <a href="https://www.freecodecamp.org/news/author/KunalN25/">freecodecamp.org</a>
</p>

<button>Cliquez-moi</button>
<button>Cliquez-moi encore</button>

<div>
  <input type="text" placeholder="Entrez votre nom" />
</div>
```

Ici, nous avons utilisé les bons éléments sémantiques pour le lien hypertexte, le bouton et l'élément de saisie. Tous ces éléments sont accessibles via Tab et interactifs via Entrée/Espace. Consultez les autres éléments liés aux formulaires dans cette [liste][34].

Certaines personnes utilisent un `div` ou un `span` et les font ressembler à une balise d'ancrage ou à un bouton avec du style CSS. Mais c'est mauvais pour l'accessibilité pour deux raisons :

-   `div` et `span` ne sont pas "tabulables" par défaut. Ainsi, même si vous faites ressembler un `div` à un bouton, l'utilisateur ne peut pas y naviguer au clavier.
    
-   Les lecteurs d'écran ne pourront pas les identifier comme des boutons, alors que dans le cas des éléments sémantiques, ils lisent ces éléments comme des boutons ou des liens.
    

Mais si vous devez absolument utiliser un `div` pour créer un élément cliquable, incluez les attributs suivants :

```
<div id="customButton" role="button" tabindex="0">Cliquez-moi</div>
```

Ici, nous avons ajouté deux attributs, `tabindex` et `role`. Nous comprendrons l'attribut `role` dans une section ultérieure.

L'attribut [`tabindex`][35] prend un entier qui spécifie l'ordre de tabulation des éléments, au lieu de l'ordre par défaut de haut en bas. Un entier positif signifie que l'élément reçoit le focus dans l'ordre spécifié par la valeur de l'attribut.

Cependant, l'utilisation de tabindex pour modifier l'ordre de tabulation par défaut n'est pas recommandée, car cela peut prêter à confusion pour les navigateurs au clavier et affecter l'accessibilité. Et franchement, ce n'est pas nécessaire.

Vous ne devriez utiliser que les deux valeurs suivantes :

-   `tabindex="0"` rend un élément tabulable, ce qui signifie qu'il est accessible via le clavier dans l'ordre naturel de tabulation.
    
-   `tabindex="-1"` signifie que l'élément n'est pas atteignable via la navigation au clavier.
    

Ces attributs font que le `div` se comporte comme un bouton, mais il reste un petit morceau de code JS à ajouter pour rendre le bouton cliquable via Entrée/Retour :

```
document.getElementById("customButton").addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    document.activeElement.click();
  }
});
```

Ici, nous avons ajouté un écouteur d'événement à l'élément qui écoute l'événement keydown. Si la touche pressée est Entrée, il appelle la méthode `onclick` de l'élément.

Si vous utilisez un élément non sémantique comme bouton, vous devez ajouter ce code supplémentaire pour qu'il fonctionne comme un bouton. Donc, ne l'utilisez que si c'est absolument nécessaire. Sinon, il est toujours préférable d'utiliser l'élément sémantique correct dès le départ.

L'accessibilité au clavier est également importante pour les commandes audio et vidéo. Nous en discuterons dans la section [Accessibilité multimédia][36].

### Étiquettes de formulaire

Une étiquette de formulaire est un texte qui décrit ce que vous devez saisir dans un champ de formulaire. L'ajout d'étiquettes aux champs de formulaire est une pratique nécessaire car elle permet à l'utilisateur de savoir comment remplir le formulaire. Mais l'utilisation des bons éléments sémantiques est cruciale.

Vous pourriez faire ce qui suit et obtenir le résultat visuel souhaité :

```
Entrez votre nom : <input type="text" id="name" name="name" />
```

Ce n'est pas bon pour les utilisateurs de lecteurs d'écran, car cela n'indique pas à quoi sert le champ de saisie. Même s'il lit "Entrez votre nom", l'utilisateur peut ne pas l'associer au champ de saisie. Utilisez plutôt l'élément `<label>` pour les étiquettes de formulaire.

```
<div>
      <label for="name">Entrez votre nom :</label>
      <input type="text" id="nameField" name="name" />
    </div>
```

L'attribut `for` associe l'étiquette au champ de saisie. Ainsi, lorsque le focus du lecteur d'écran est sur le champ de saisie, il lit l'étiquette, suivie de "champ d'édition" pour faire savoir à l'utilisateur qu'il doit entrer son nom dans le champ.

Consultez le [formulaire avec étiquette][37] et le [formulaire sans étiquette][38] dans ces exemples pour plus de clarté. Utilisez Voiceover de Mac (⌘+F5) ou Narrator de Windows (Ctrl+Windows+Entrée) pour voir comment il lit les éléments du formulaire.

L'utilisation de `<label>` offre d'autres avantages :

-   En liant un `<label>` à un champ de saisie avec l'attribut `for` (association cliquable), cliquer sur l'étiquette donne le focus au champ de saisie.
    
-   L'association cliquable avec le champ de saisie aide les utilisateurs à sélectionner de petites entrées comme les [cases à cocher][39] ou les [boutons radio][40].
    
-   Cela respecte le HTML sémantique et spécifie que le texte est utilisé comme étiquette de formulaire.
    

Enfin, n'oubliez pas que le texte de l'étiquette doit décrire clairement ce que l'utilisateur doit saisir dans le champ. Par exemple, "Entrez votre nom" ou "Entrez votre e-mail".

Cela s'applique également aux boutons. Assurez-vous que le texte du bouton est suffisamment descriptif pour indiquer à l'utilisateur sur quoi il clique. Des textes vagues comme "Cliquez-moi !" ou "Cliquez ici !" ne sont pas utiles. Des exemples de textes descriptifs sont "Envoyer le formulaire" ou "Télécharger le rapport", qui donnent aux utilisateurs une idée claire de l'action du bouton.

Parallèlement à cela, les liens font également partie des éléments interactifs. Mais comme il existe de nombreux exemples pour les liens, je vais les aborder dans leur propre section maintenant.

### Liens

Les liens sont un élément clé des pages web car ils permettent à l'utilisateur de naviguer sur le site. Les liens servent à différents buts : aller vers une autre page du même site, aller vers un site externe ou télécharger quelque chose. Dans cette section, vous découvrirez plusieurs pratiques concernant les liens qui contribuent à l'accessibilité.

#### Lien vers des sites web externes

Lorsque vous ajoutez un lien qui permet aux utilisateurs d'ouvrir un site externe, l'inclusion de l'attribut `target=_blank` ouvre le lien dans un nouvel onglet.

```
<a href="https://www.wikipedia.org/" target="_blank"> Wikipedia </a>
```

C'est utile pour les utilisateurs car ils n'ont pas besoin de quitter le site actuel, leur évitant ainsi de devoir revenir en arrière.

De plus, si votre lien s'ouvre dans un nouvel onglet, c'est une bonne idée de le mentionner pour que les lecteurs d'écran puissent le lire et aider les utilisateurs malvoyants.

```
<a href="https://www.wikipedia.org/" target="_blank" >
Wikipedia (s'ouvre dans un nouvel onglet)
</a>
```

De même, si votre lien ouvre un fichier non HTML, comme un PDF ou un DOCX, vous devriez le mentionner :

```
<a target="_blank" href="fiche-paie-janvier.pdf">
Fiche de paie - Janvier (PDF)
</a>
```

Alternativement, vous pouvez utiliser une icône pour indiquer qu'un lien s'ouvre dans un nouvel onglet.

```
<a href="https://www.wikipedia.org/" target="_blank">
  Wikipedia
  <img src="new-tab-icon.png" alt="S'ouvre dans un nouvel onglet" style="width:16px; height:16px; margin-left:5px;">
</a>
```

Lorsque vous utilisez une icône, assurez-vous d'inclure l'attribut alt avec une description de l'image. Nous comprendrons son but dans la section [Accessibilité multimédia][41].

#### Liens d'évitement

Un lien d'évitement (skip link) est un élément de lien placé en haut d'une page qui mène directement au contenu principal. Cela permet aux utilisateurs de sauter les en-têtes et tous les menus de navigation pour arriver directement au contenu principal de la page. C'est utile sur les sites où il y a beaucoup de contenu répétitif en haut, comme des menus ou des bannières.

Les liens d'évitement sont particulièrement utiles pour les personnes malvoyantes qui utilisent des lecteurs d'écran. Ces liens offrent un moyen de contourner les menus de navigation répétitifs. Cela aide également les navigateurs au clavier, faisant gagner du temps et améliorant l'expérience utilisateur.

Pour ajouter un lien d'évitement, ajoutez une balise d'ancrage tout en haut, juste sous la balise body, et liez-la au contenu principal.

```
<body>
 <a href="#main">Passer au contenu principal</a>
    <header>
      <h1>Titre de la page</h1>
      <nav>
        <ul id="nav-links">
          <li><a href="/">Accueil</a></li>
          <li><a href="/about">À propos</a></li>
          <li><a href="/blog">Blog</a></li>
          <!-- autres liens de navigation -->
        </ul>
      </nav>
    </header>
    <main id="main">
      <!-- Contenu principal -->
    </main>
</body>
```

Le lien d'évitement est accessible au clavier et est également lu par le lecteur d'écran. Cliquer dessus vous amène directement au contenu principal. Visitez [WebAIM][42] et appuyez sur Tab sur votre clavier pour voir les liens d'évitement en action.

#### Stylisation des liens

Par défaut, les liens créés avec la balise d'ancrage sont visuellement différents du texte normal. C'est parce que la balise d'ancrage possède des styles intégrés comme la couleur, la [text-decoration][43], l'anneau de focus (qui s'affiche lorsque vous tabulez sur le lien avec le clavier) et des effets de survol.

Les liens doivent avoir un aspect différent du reste du texte pour être facilement identifiables. Comme vous l'avez vu plus haut, le navigateur s'en occupe pour vous, vous n'avez donc pas grand-chose à faire. Mais si vous ajoutez des styles personnalisés au lien pour qu'il s'intègre mieux à votre thème, vous devez suivre certaines bonnes pratiques :

-   Les liens doivent avoir des couleurs différentes pour les états par défaut, [visité][44], [focus][45] et [survol][46].
    
-   La couleur du texte du lien doit être différente du texte normal et doit avoir un style distinct.
    
-   La couleur du texte du lien doit avoir un contraste de 3:1 avec le reste du texte et un contraste de 4,5:1 avec la couleur d'arrière-plan. Voir la section [Contraste des couleurs][47] pour plus de détails.
    

Un exemple de style personnalisé pour les liens est présenté ci-dessous (tiré de la doc) :

```
a {
  color: #ff0000;
}

a:hover,
a:visited,
a:focus {
  color: #a60000;
  text-decoration: none;
}

a:active {
  color: #000000;
  background-color: #a60000;
}
```

À l'aide des [pseudo-classes][48], cela ajoute différents styles lorsque le lien est survolé, déjà visité, focalisé (avec le clavier) ou actif (pendant le clic).

Vous pouvez expérimenter avec différentes couleurs et styles, mais ne supprimez pas les propriétés `cursor: pointer` ou `outline`. Les deux sont importantes pour les personnes utilisant la navigation au clavier.

Rappelez-vous, les liens ont déjà des styles intégrés pour tous les états. N'ajoutez les vôtres que si vous voulez quelque chose en accord avec le thème de votre site.

#### Éviter d'utiliser des gestionnaires onclick

Les liens sont utilisés pour naviguer vers une autre page web sur le même site ou vers un site externe. Spécifier le lien dans l'attribut [href][49] s'en occupe pour vous sans qu'il soit nécessaire d'ajouter du code JavaScript.

Cependant, certaines personnes ajoutent un attribut `onclick` aux éléments d'ancrage pour les faire se comporter comme des boutons et définissent `href="#"` ou `href="javascript:void(0)"` pour éviter le rafraîchissement de la page. Cela provoque un comportement inattendu et peut entraîner les problèmes suivants :

-   Copier ou faire glisser ce lien ajoute un `#` ou `void(0)` inutile à l'URL, ce qui n'a aucun sens.
    
-   Cliquer sur le lien fait immédiatement défiler la page vers le haut, ce qui peut faire perdre à l'utilisateur le fil de sa lecture.
    
-   Si le JavaScript est encore en cours de téléchargement, cliquer sur le lien ne fait rien et la page web semble ne pas répondre.
    

C'est également mauvais pour la sémantique et l'accessibilité, car les personnes utilisant des lecteurs d'écran peuvent être confuses. Si vous souhaitez ajouter une fonctionnalité JavaScript au clic d'un élément, utilisez simplement un `<button>`. N'utilisez des liens que pour naviguer vers une véritable URL.

#### Texte de lien explicite

Tout comme pour les boutons, lors de la rédaction du texte d'un lien, gardez-le explicite et descriptif, et évitez d'utiliser "Cliquez ici" ou "Cliquez sur ceci".

```
<p>
  Pour plus d'informations sur l'accessibilité,
  <a href="https://developer.mozilla.org/en-US/docs/Web/Accessibility">
    cliquez ici
  </a>
</p>
```

Au lieu de ce qui précède, faites ceci :

```
<p>
  Pour plus d'informations sur l'accessibilité, consultez la
  <a href="https://developer.mozilla.org/en-US/docs/Web/Accessibility">
    Documentation MDN - Accessibilité
  </a>
</p>
```

Consultez les exemples de [Bons Liens][50] et de [Mauvais Liens][51] de la doc. Vous pouvez également les tester avec VoiceOver (⌘+F5).

#### Proximité des liens

Si votre page web contient de nombreux éléments interactifs comme des liens et des boutons, assurez-vous qu'ils sont correctement espacés pour éviter les clics accidentels. Cela aide les personnes ayant des [problèmes de contrôle moteur][52] qui pourraient cliquer sur le mauvais lien.

L'utilisation de la propriété [`margin`][53] devrait suffire à garantir l'espacement.

### Accessibilité des tableaux

Dans la section sur les mises en page, nous avons vu que l'utilisation de tableaux pour créer des mises en page est une pratique obsolète. Cependant, les tableaux peuvent toujours être utilisés si vous souhaitez afficher une grande quantité de données sous forme tabulaire. L'intégration de l'accessibilité dans les tableaux aide les lecteurs d'écran à les interpréter et aide les utilisateurs malvoyants.

Consultez la [Documentation MDN - Accessibilité des tableaux][54] pour comprendre les meilleures pratiques.

## Pratiques CSS et JS supplémentaires

La plupart de vos objectifs d'accessibilité devraient être atteints avec le HTML seul. Mais il y a certaines choses à garder à l'esprit lors de l'écriture du CSS et du JavaScript pour s'assurer de ne pas dégrader l'accessibilité.

### Styliser les éléments de formulaire

Lors du stylisme des éléments de formulaire, n'oubliez pas ce qui suit :

-   Ne supprimez pas les styles par défaut pour les contours de focus (focus outlines), le survol et l'état désactivé dans les éléments de formulaire. Vous pouvez les modifier selon le design de votre site, mais ils doivent rester visibles.
    
-   Assurez-vous que vos étiquettes et textes d'espace réservé (placeholders) sont visuellement clairs. Suivez les pratiques de contraste des couleurs (section suivante).
    
-   Pour les zones cliquables comme les boutons et les entrées, assurez-vous qu'elles sont assez grandes pour que l'utilisateur puisse cliquer confortablement.
    
-   Les messages de succès et d'erreur doivent être physiquement distinguables des étiquettes et des autres contenus textuels.
    

### Contraste des couleurs

Lorsque vous choisissez les couleurs de votre site web, votre texte et votre couleur d'arrière-plan doivent avoir un bon contraste. Un bon contraste de couleurs garantit que le texte est facilement lisible par tous les utilisateurs (et cela aide particulièrement les personnes atteintes de daltonisme).

Les WCAG (Web Content Accessibility Guidelines) recommandent les ratios de contraste suivants :

![Ratios de contraste de couleurs recommandés](https://cdn.hashnode.com/res/hashnode/image/upload/v1736175276741/40ee7fe4-110c-4dd1-95f3-4cb7620de032.png)

Comprenons les niveaux de contraste de couleurs :

-   Le niveau AA correspond au ratio minimum que votre contraste de couleurs doit atteindre pour que le contenu du site soit lisible. Comme vous pouvez le voir dans le tableau ci-dessus, cela nécessite un ratio minimum de 4,5:1 pour le corps du texte, un ratio de 3:1 pour le texte à grande échelle, et un ratio de 3:1 pour les composants d'interface utilisateur actifs et les objets graphiques.
    
-   Le niveau AAA est la norme idéale pour l'accessibilité qui garantit un contraste élevé pour votre site web. Cela nécessite un ratio de 7:1 pour le corps du texte, un ratio de 4,5:1 pour le texte à grande échelle, et n'est pas défini pour les composants d'interface utilisateur/objets graphiques.
    

Choisissez un ratio de contraste qui s'aligne bien avec votre design, mais essayez de maintenir au moins le niveau AA. Pour vérifier le ratio de contraste entre deux couleurs, vous pouvez utiliser les outils suivants :

-   [Color Contrast Checker][55]
    
-   [Outils de développement Chrome][56] - Identifie le texte de votre site ne respectant pas les niveaux AA et AAA.
    

### Pratiques JavaScript

#### Événements spécifiques à la souris

Lorsque vous avez des fonctionnalités déclenchées par des événements comme [mouse-over][57] et [mouse-out][58], elles ne sont pas accessibles aux personnes dépendant de la navigation au clavier. Ainsi, pour rendre la fonctionnalité accessible au clavier, vous devez ajouter les mêmes gestionnaires d'événements aux événements comme [focus][59] et [blur][60].

#### Validations de formulaire côté client

Lorsque vous soumettez des données via un formulaire, les données sont validées pour vérifier si vous avez saisi des informations valides. Souvent, lorsque les données sont envoyées au serveur, celui-ci les valide et informe l'interface utilisateur si la validation a échoué.

Pour rendre le site web convivial, il est utile d'ajouter des validations de formulaire côté client, afin que les utilisateurs reçoivent un retour instantané s'ils ont saisi des données incorrectes, car le mécanisme côté serveur peut prendre du temps. C'est une petite étape vers l'amélioration de l'expérience utilisateur.

Consultez l'exemple de [Validation de formulaire][61] pour en savoir plus.

En dehors de ce qui précède, une chose dont vous devez vous souvenir est de ne pas utiliser JavaScript pour tout et n'importe quoi. JavaScript peut être utilisé pour générer n'importe quelle forme de HTML et appliquer dynamiquement des styles CSS. C'est très utile si vous avez du contenu dynamique sur votre site.

Mais si vous avez trop de HTML généré par JavaScript, il devient difficile pour les lecteurs d'écran de suivre les changements dynamiques. Cela rend le site difficile à lire pour les utilisateurs handicapés. Assurez-vous donc de ne pas abuser de JavaScript quand un simple HTML suffirait.

L'accessibilité pour les mises à jour de contenu dynamique est abordée dans la section suivante.

## Pratiques d'accessibilité avancées : WAI-ARIA

À mesure que les applications commençaient à devenir plus grandes et plus complexes, les développeurs ont eu besoin d'un nouvel ensemble de fonctionnalités d'accessibilité. Les éléments sémantiques seuls ne suffisaient plus, surtout pour les éléments complexes comme les sélecteurs de date et les widgets personnalisés.

Se fier uniquement au HTML sémantique n'aide pas lorsque le contenu est mis à jour dynamiquement sur la page web. De nos jours, tous les sites web construits avec JavaScript ont du contenu qui n'est pas chargé initialement, mais mis à jour dynamiquement en fonction des interactions de l'utilisateur.

WAI-ARIA (Web Accessibility Initiative - Accessible Rich Internet Applications) a été introduit pour ajouter plus de fonctionnalités d'accessibilité là où c'était nécessaire. Il définit un ensemble d'attributs HTML que vous pouvez utiliser pour fournir une sémantique supplémentaire à votre site web et améliorer l'accessibilité.

Dans les sections suivantes, vous apprendrez quels attributs ont été introduits et comment vous pouvez les utiliser pour améliorer l'accessibilité.

### L'attribut `role`

L'attribut `role` aide à ajouter des informations sémantiques aux éléments non sémantiques en définissant leur "rôle" sur la page web. Avec les rôles, les lecteurs d'écran peuvent lire avec précision les éléments non sémantiques et aider à les identifier pour les personnes handicapées.

Le W3C définit plusieurs rôles que vous pouvez utiliser, selon leur but. Mais gardez à l'esprit que vous ne devriez utiliser `role` que lorsque c'est nécessaire. Dans la plupart des cas, il est préférable d'utiliser les bons éléments sémantiques comme `<button>`, `<nav>`, `<header>`, etc.

Cependant, lorsque les éléments sémantiques ne remplissent pas votre objectif, les rôles peuvent aider. Voyons comment les utiliser avec quelques exemples :

Si vous voulez créer un bouton avec un `div` personnalisé, l'ajout de l'attribut `role` spécifie que cet élément est utilisé comme un bouton.

```
<div role="button" tabindex="0">Cliquez-moi</div>
```

Lorsque vous testez cela avec VoiceOver de Mac (⌘+F5), il lit l'élément comme un bouton. Comme discuté précédemment, incluez toujours l'attribut `tabindex`.

Mais si vous voulez utiliser un `div` au lieu d'un bouton, vous devez toujours ajouter la fonctionnalité JavaScript, comme expliqué dans la section [Accessibilité au clavier][62].

Un autre exemple est si vous écrivez un lien personnalisé. Vous pouvez utiliser le rôle suivant, afin que le lecteur d'écran interprète cela comme un lien :

```
<div role="link">Visitez notre site web</div>
```

En dehors des éléments interactifs, l'attribut `role` peut également être utilisé pour définir des éléments comme des menus de navigation, des barres latérales, des bannières, etc. Si vous utilisez des éléments non sémantiques à ces fins, incluez toujours un rôle, comme ceci :

```
<div role="navigation">
    <!-- Éléments du menu de navigation -->
</div>
```

Dans ce cas, le lecteur d'écran annonce cela comme une zone de navigation.

De plus, si vous avez un élément qui sert d'alerte pour l'utilisateur, l'inclusion du rôle suivant fait que le lecteur d'écran l'annonce dès qu'il apparaît à l'écran, même s'il n'a pas le focus :

```
<div role="alert">
  Veuillez répondre à cette alerte
</div>
```

Vous pouvez trouver la liste complète des rôles disponibles dans la [Documentation MDN : Rôles WAI-ARIA][63].

### Attributs aria-*

En plus de `role`, ARIA (Accessible Rich Internet Applications) définit des attributs supplémentaires pour améliorer l'accessibilité des applications web. Ces attributs donnent aux lecteurs d'écran plus d'informations sur les éléments, aidant les personnes handicapées à mieux les comprendre.

Si les éléments sémantiques natifs ou l'attribut `role` seul ne suffisent pas, les attributs aria-* peuvent fournir un contexte supplémentaire. Vous pouvez trouver une liste complète de ces attributs dans la [Documentation MDN - ARIA][64].

Dans les sections suivantes, nous verrons comment les attributs role et aria-* peuvent améliorer l'accessibilité. Nous ne couvrirons pas tous les attributs ici, mais nous nous concentrerons sur les plus couramment utilisés.

### Mises à jour de contenu dynamique

Lorsqu'une page web se charge pour la première fois, son contenu est lu par le lecteur d'écran. Mais les lecteurs d'écran ne peuvent pas capturer le contenu dynamique, c'est-à-dire le contenu qui est ajouté ou supprimé par la suite.

Par exemple, lorsqu'une page web affiche des mises à jour sportives en direct, elle est mise à jour presque chaque minute. Les lecteurs d'écran ne liront que le contenu affiché lors du premier rendu de la page, mais ne montreront pas les mises à jour dynamiques.

Ce n'est pas vraiment un problème pour beaucoup d'utilisateurs, mais pour les personnes malvoyantes, les lecteurs d'écran peuvent ne pas être capables de lire les changements sur la page. La plupart des sites web modernes étant de nature dynamique, il est important de considérer l'accessibilité des mises à jour de contenu dynamique.

Consultez l'exemple [aria-no-live][65] de la documentation MDN. Il charge une nouvelle citation toutes les 10 secondes, ce que vous pouvez voir clairement en tant qu'utilisateur sans déficience visuelle. Mais le lecteur d'écran ne lit que le contenu initial de la page et n'annonce pas les mises à jour. Ce n'est pas bon pour l'accessibilité.

Pour corriger cela, WAI-ARIA fournit l'attribut [`aria-live`][66] qui permet au lecteur d'écran de lire le contenu mis à jour. Vous pouvez ajouter cet attribut à l'élément qui contient le contenu dynamique.

Il prend les trois valeurs suivantes :

-   `aria-live="off"` : Valeur par défaut qui signifie qu'aucun contenu n'est lu.
    
-   `aria-live="polite"` : Les mises à jour ne sont annoncées que lorsque l'utilisateur est inactif.
    
-   `aria-live="assertive"` : Le contenu est lu dès qu'il est mis à jour.
    

Selon l'importance de la mise à jour, vous pouvez décider quelle valeur utiliser.

```
<div aria-live="polite">
    <!-- Contenu dynamique ici -->
</div>
```

Dans ce cas, le lecteur d'écran attend que l'utilisateur ait terminé sa tâche actuelle avant d'annoncer la mise à jour.

Vous pouvez ajouter plus de détails ici. Avec l'attribut ci-dessus, seul le texte mis à jour est lu. Cependant, les utilisateurs de lecteurs d'écran peuvent être confus quant à la partie de la page qui est lue. Il est donc utile que l'élément entier soit lu.

```
<div aria-live="assertive" aria-atomic="true">
    <!-- Contenu dynamique ici -->
</div>
```

L'attribut [`aria-atomic`][67] indique aux lecteurs d'écran de lire l'élément entier comme une seule unité atomique. Cela évite toute confusion pour les utilisateurs malvoyants. Consultez l'exemple [aria-live][68] de la documentation MDN avec VoiceOver de Mac (⌘+F5). Il lit l'élément entier lorsque le contenu est mis à jour.

### Validation de formulaire et erreurs

Supposons que vous ayez ajouté une validation à votre formulaire via JavaScript. Lorsque la validation échoue, un message d'erreur s'affiche à l'écran. Par exemple, un message de champ obligatoire apparaît si vous avez oublié un champ.

L'implémentation de la gestion des erreurs implique la création d'un élément contenant un message d'erreur ou une liste d'erreurs qui s'affichent sous certaines conditions, selon le code JavaScript. Comme nous l'avons vu dans la section précédente, le lecteur d'écran ne lit pas les nouvelles mises à jour de contenu.

Nous devrions donc nous assurer que le lecteur d'écran lit le message d'erreur dès qu'il apparaît, afin de faire savoir aux utilisateurs malvoyants qu'une erreur a été générée. Nous pouvons utiliser les attributs suivants à cette fin :

```
<div class="errors" role="alert" aria-relevant="all">
  <ul></ul>
</div>
```

Le rôle [`alert`][69] fait deux choses. Il identifie sémantiquement cet élément comme une information importante. Deuxièmement, ce rôle transforme l'élément en une région [live][70], ce qui signifie que le lecteur d'écran est immédiatement averti s'il y a des changements.

L'attribut [`aria-relevant`][71] décrit quels changements doivent être annoncés dans une région live. L'attribut prend une liste de valeurs séparées par des espaces parmi les suivantes :

-   `additions` : Annonce le nouveau contenu ajouté à la région live.
    
-   `removals` : Le contenu supprimé de la région live est lu.
    
-   `text` : Annonce toute modification du texte existant.
    

Il prend également la valeur `all` qui est un raccourci pour `additions removals text`, signifiant que les trois types de changements sont lus.

Vous pouvez consulter l'[exemple de validation de formulaire][72] de la documentation MDN.

Ensuite, voyons ce qu'il faut faire si nous voulons marquer certains champs comme obligatoires. Normalement, nous ajouterions des indices visuels comme un `*` et le message suivant en haut du formulaire :

```
<p>Les champs marqués d'un astérisque (*) sont obligatoires.</p>
```

C'est utile pour les utilisateurs ordinaires, mais les utilisateurs malvoyants peuvent être confus quant aux champs qui sont obligatoires. Pour leur faciliter la tâche, nous pouvons utiliser l'attribut [`aria-required`][73].

```
<input type="text" name="name" id="name" aria-required="true" />
```

Avec cet attribut, le lecteur d'écran mentionne ce champ comme "obligatoire" lors de sa lecture.

Lorsque vous créez des champs de saisie, il est important d'inclure une étiquette, car certains lecteurs d'écran ne lisent pas le texte de l'espace réservé (placeholder). Si vous ne souhaitez pas inclure de champ d'étiquette visible, voici les alternatives suivantes :

Vous pouvez utiliser l'attribut `aria-label` pour ajouter des étiquettes aux champs de saisie qui n'ont pas d'étiquette associée.

```
<input type="email" name="email" aria-label="Entrez votre e-mail" />
```

Cet attribut fournit un texte à lire par un lecteur d'écran pour décrire le champ de saisie.

Vous pouvez aller plus loin et utiliser l'attribut `aria-labelledby` qui utilise un autre élément pour servir d'étiquette au champ de saisie. Par exemple :

```
<div>
  <span id="emailLabel">Entrez votre e-mail</span>
  <input type="email" name="email" aria-labelledby="emailLabel" />
</div>
```

Le lecteur d'écran lit le texte à l'intérieur de l'élément `<span>` pour décrire l'élément de saisie. C'est similaire à l'utilisation d'un `<label>` avec un attribut `for`. Vous pouvez également utiliser cet attribut pour référencer d'autres éléments interactifs comme `<button>` ou `<a>` qui n'ont pas de champ d'étiquette pour les référencer.

Gardez à l'esprit que l'attribut `aria-labelledby` ne définit qu'un nom accessible pour l'élément – il ne fournit pas d'autres fonctionnalités comme le clic sur l'étiquette pour donner le focus à l'élément de saisie. Il est préférable d'utiliser `<label>` avec un attribut `for`.

Nous avons déjà discuté des étiquettes de formulaire dans la section [Éléments interactifs][74].

Vous avez maintenant vu certains des différents attributs offerts par WAI-ARIA et comment ils améliorent l'accessibilité. Vous pouvez consulter la [Documentation MDN : WAI-ARIA][75] pour vérifier les détails supplémentaires que j'aurais pu omettre.

Avant de passer à la suite, rappelez-vous une chose : _n'utilisez WAI-ARIA que lorsque c'est nécessaire_. Habituellement, les éléments sémantiques suffisent à atteindre la majorité de vos objectifs d'accessibilité. N'abusez pas de WAI-ARIA car cela pourrait finir par compliquer votre code.

## Accessibilité multimédia

Le contenu d'un site web ne se limite pas au texte. Il se compose aussi souvent de contenus multimédias comme des images, de l'audio et de la vidéo. Dans de nombreux cas, le contenu multimédia est plus facile à comprendre que le texte. Bien que cela soit vrai pour beaucoup d'utilisateurs, cela pose des défis aux utilisateurs handicapés.

Les personnes malvoyantes ne peuvent pas voir les images et les personnes sourdes ou malentendantes ne peuvent pas facilement interpréter le contenu audio. En tant que développeurs, c'est donc notre travail de rendre ce type de contenu accessible à tous. Voyons comment rendre cela possible :

### Images

Comme les personnes malvoyantes ne peuvent pas voir les images, elles dépendent d'un lecteur d'écran pour décrire l'image. Écrire simplement une balise `img` avec un attribut `src` n'aide pas.

```
<img src="temple.jpg" />
```

Par défaut, le lecteur d'écran lit le chemin du fichier ou l'URL de l'image. Un nom de fichier peut donner une idée de l'image, mais ne la décrit pas réellement.

Il est donc utile d'ajouter un attribut `alt` à une `img`. L'attribut `alt` fournit un texte alternatif pour l'image, et son but est de décrire l'image.

```
<img
  src="temple.jpg"
  alt="Le temple de Meenakshi, situé à Madurai, une ville du sud de l'Inde, est dédié à la déesse Meenakshi, une forme de Parvati"
/>
```

Ici, au lieu de lire le chemin du fichier, le lecteur d'écran lit le texte alternatif – c'est-à-dire la valeur de l'attribut `alt`. Le texte alternatif doit fournir une description de l'image pour aider les utilisateurs à comprendre ce qu'elle transmet. Ainsi, au lieu de dire simplement "Temple", l'utilisateur sait quel temple est représenté sur l'image.

Vous pouvez également ajouter un contexte supplémentaire à l'image avec l'attribut `title`.

```
<img
  src="temple.jpg"
  alt="Le temple de Meenakshi, situé à Madurai, une ville du sud de l'Inde, est dédié à la déesse Meenakshi, une forme de Parvati"
  title="Le temple de Meenakshi"
/>
```

Lorsqu'il est focalisé sur l'image, le lecteur d'écran lit le texte `alt` et le titre.

Prenons un autre exemple qui utilise une alternative à l'attribut `alt` :

```
<img src="temple.jpg" aria-labelledby="temple-label" />
<p id="temple-label">
  Le temple de Meenakshi, situé à Madurai, une ville du sud de l'Inde, est dédié à la
  déesse Meenakshi, une forme de Parvati
</p>
```

Ici, au lieu d'utiliser l'attribut `alt`, nous avons utilisé l'attribut `aria-labelledby` pour lier l'élément paragraphe à l'image. Le texte à l'intérieur de `p` agit comme un texte alternatif pour l'image. C'est utile si vous devez utiliser le même texte comme texte alternatif pour différentes images.

Parfois, nous utilisons des images comme icônes pour les en-têtes et les menus de navigation, simplement pour la décoration. Habituellement, ces images ne sont pas pertinentes pour comprendre le contenu de la page. Dans ces cas, vous ajoutez un attribut `alt` vide.

```
<h3>
  <img src="page-icon.png" alt="" />
  Histoire du temple de Meenakshi 
</h3>
```

Si vous omettez l'attribut `alt`, le lecteur d'écran lit l'URL complète de l'image. Pour éviter cela, utilisez un attribut `alt` vide, afin que le lecteur d'écran l'annonce simplement comme une image et passe à la suite, évitant ainsi des distractions inutiles pour les utilisateurs.

Vous pouvez également utiliser `role="presentation"` pour ignorer la lecture du chemin de l'image ou du texte alternatif.

### Audio et vidéo

Lors de l'utilisation des éléments [<audio>][76] et [<video>][77], n'oubliez pas d'inclure plusieurs sources – c'est-à-dire de fournir l'audio et la vidéo dans différents formats. Pour les navigateurs qui ne supportent pas les formats mentionnés, incluez un lien de téléchargement de secours afin qu'ils puissent accéder à la ressource.

```
<audio controls>
  <source src="audio.mp3" type="audio/mpeg" />
  <source src="audio.ogg" type="audio/ogg" />
  <p>
    Votre navigateur ne supporte pas l'audio HTML. Voici un
    <a href="audio.mp3">lien vers l'audio</a> à la place.
  </p>
</audio>
<video controls>
  <source src="video.mp4" type="video/mp4" />
  <source src="video.webm" type="video/webm" />
  <p>
    Votre navigateur ne supporte pas la vidéo HTML5. Voici un
    <a href="video.mp4">lien vers la vidéo</a> à la place.
  </p>
</video>
```

Ensuite, comprenons les lacunes de l'utilisation des contrôles HTML natifs pour l'audio et la vidéo.

-   Ils ne peuvent pas être stylisés avec CSS, ils peuvent donc ne pas s'aligner sur le thème de votre site.
    
-   Les boutons lecture/pause ne sont pas accessibles au clavier.
    
-   Ils n'ont pas de fonctionnalité pour avancer ou reculer dans la vidéo.
    

Pour surmonter ces limitations, nous allons créer notre propre lecteur vidéo personnalisé dans les étapes suivantes. Pour commencer, créons un conteneur pour le contenu vidéo :

```
<div class="controls">
  <button class="play-pause">Lecture</button>
  <button class="stop">Réinitialiser la vidéo</button>
</div>
```

Ceux-ci fonctionneront comme boutons de lecture/pause et de réinitialisation. Ensuite, supprimons l'attribut `controls` de la balise `<video>` pour les remplacer par nos contrôles personnalisés.

```
const videoPlayer = document.querySelector("video");
videoPlayer.removeAttribute("controls");
```

Pourquoi le supprimer au moment de l'exécution ? Supposons que le JavaScript ne se charge pas en raison d'un problème. Dans ce cas, l'utilisateur peut toujours utiliser les contrôles natifs. Ensuite, ajoutons quelques fonctionnalités à nos boutons :

```
const playPauseBtn = document.querySelector(".play-pause");
const resetBtn = document.querySelector(".reset");

playPauseBtn.onclick = () => {
  if (videoPlayer.paused) {
    videoPlayer.play();
    playPauseBtn.textContent = "Pause";
  } else {
    videoPlayer.pause();
    playPauseBtn.textContent = "Lecture";
  }
};

resetBtn.onclick = () => {
  videoPlayer.pause();
  videoPlayer.currentTime = 0;
  playPauseBtn.textContent = "Lecture";
};
```

-   L'objet lecteur vidéo est de type [`HTMLMediaElement`][78], qui contient plusieurs méthodes que vous pouvez utiliser pour contrôler la vidéo.
    
-   Pour le bouton lecture/pause, nous ajoutons une fonctionnalité de bascule avec les méthodes `play()` et `pause()`.
    
-   Pour réinitialiser la vidéo, nous la mettons en pause et définissons le temps actuel à 0.
    

Désormais, notre lecteur vidéo personnalisé est accessible au clavier et peut être stylisé avec CSS. Vous pouvez également ajouter des fonctionnalités supplémentaires comme l'avance/retour rapide, une minuterie et une barre de progression. Les étapes sont similaires pour un lecteur audio personnalisé.

Consultez la [Documentation MDN][79] pour plus de détails sur cette fonctionnalité.

#### Transcriptions audio

Les personnes sourdes ou malentendantes ne peuvent pas facilement accéder au contenu audio. Pour le rendre accessible, vous devez donc ajouter des transcriptions sous tout contenu de type audio ou vidéo.

Si vous dirigez une entreprise, vous pourriez payer un professionnel pour réaliser les transcriptions. Consultez la [doc][80] pour les options. Pour afficher la transcription sur l'interface utilisateur, vous pourriez utiliser un panneau afficher/masquer. En vous référant à la doc, voyez l'[interface utilisateur de transcription audio][81] ([code source][82]) pour un exemple.

Si l'audio est l'enregistrement d'une présentation, vous devriez joindre des liens vers tous les documents ou supports de présentation. Incluez également une description pour tout contenu visuel référencé.

#### Sous-titres codés et sous-titres vidéo

Tout d'abord, comprenons la différence entre les sous-titres codés (captions) et les sous-titres (subtitles). Ils sont implémentés de manière similaire et visuellement, ils se ressemblent – mais leurs buts sont différents.

Les sous-titres codés indiquent qui parle et décrivent d'autres effets sonores dans la vidéo. Ils sont principalement ajoutés pour les personnes sourdes ou malentendantes. Les sous-titres aident les personnes qui ne comprennent pas la langue parlée dans la vidéo, en la traduisant dans un texte utilisant la langue de leur choix.

Voyons comment ajouter des sous-titres à vos vidéos. Nous écrivons les sous-titres en WebVTT, un format qui contient du texte accompagné de plages d'horodatage indiquant quel texte vous voulez à chaque partie de la vidéo. Voici un exemple de fichier de sous-titres :

```
WEBVTT

1
00:00:01.230 --> 00:00:02.606
Ceci est le premier sous-titre.

2
00:00:04.739 --> 00:00:06.074
Ceci est le deuxième.
```

Enregistrez ce fichier avec une extension `.vtt`. Pour lier ce fichier à votre vidéo, incluez-le dans un élément [`<track>`][83] :

```
<video controls>
  <source src="video.mp4" type="video/mp4" />
  <track
    src="captions.vtt"
    kind="subtitles"
    srclang="fr"
    label="Français"
    default
  />
</video>
```

Vous devez inclure l'élément `<track>` à l'intérieur de l'élément `<video>` et le placer après toutes les sources. Il possède les attributs suivants :

-   `kind` mentionne le type de fichier référencé.
    
-   `srclang` indique la langue des sous-titres.
    
-   `label` indique le texte affiché pendant que l'utilisateur sélectionne une langue.
    
-   `src` est le chemin ou l'URL du fichier de sous-titres, c'est-à-dire le fichier `.vtt` que nous avons créé précédemment.
    

Cela affichera les sous-titres pour les horodatages spécifiés. Cela aidera non seulement les personnes malentendantes, mais sera également utile pour les personnes qui ne comprennent pas la langue, ou celles qui travaillent dans un environnement bruyant.

Pour les personnes malvoyantes, vous pourriez également inclure du texte décrivant certains visuels dans des parties de la vidéo. Ce texte serait lu par le lecteur d'écran.

Vous pouvez également ajouter un style personnalisé au menu des sous-titres et au texte des sous-titres. Consultez [Documentation MDN - Ajouter des sous-titres codés et des sous-titres à une vidéo HTML][84] pour l'implémentation.

## Accessibilité mobile

Nous avons couvert de nombreuses pratiques clés d'accessibilité jusqu'à présent, et elles devraient également bien fonctionner sur les téléphones mobiles. Mais il existe des considérations supplémentaires que vous pouvez suivre pour les utilisateurs mobiles.

Tout d'abord, parlons des événements spécifiques à la souris. Nous avons déjà vu comment rendre les événements spécifiques à la souris accessibles dans la section [Pratiques JavaScript][85]. Les événements comme [mousedown][86] ou [mouseup][87] sont souvent utilisés pour les fonctionnalités de glisser-déposer.

Mais ceux-ci ne sont pas accessibles aux utilisateurs d'écrans tactiles, vous devriez donc ajouter la même fonctionnalité aux événements spécifiques au toucher comme [touchstart][88] et [touchend][89]. L'exemple suivant est dans le contexte du glisser-déposer :

```
source.ontouchstart = (e) => {
  // initier le glissement
};

dest.ontouchend = (e) => {
   // déposer
};
```

Ensuite, vous devez vous assurer de suivre le design responsive lors de la conception de vos pages web. Le design responsive garantit que le site web a une belle apparence tant sur ordinateur que sur téléphone mobile. J'ai écrit un guide détaillé sur le [design responsive][90], n'hésitez pas à le consulter si vous êtes intéressé.

Quelques autres pratiques d'accessibilité mobile qu'il est bon de connaître :

-   Ne désactivez pas le zoom sur votre site web. Les utilisateurs voyants comme ceux ayant des déficiences visuelles peuvent avoir besoin de zoomer pour lire le contenu du site sur de plus petits écrans.
    
-   Lors de la rédaction de menus de navigation, vous les cacherez normalement et fournirez une icône hamburger pour les ouvrir, car l'écran est beaucoup plus court/petit sur un téléphone mobile. Dans ces cas, le menu hamburger doit être facilement accessible. Consultez l'exemple d'un [bon menu hamburger][91] de la doc, en vue mobile.
    
-   Lors de la création de formulaires, essayez de minimiser la quantité de saisie que l'utilisateur doit faire, car cela peut devenir agaçant pour les utilisateurs mobiles. C'est particulièrement important si votre site est principalement conçu pour les utilisateurs mobiles. Consultez la [doc][92] pour des exemples.
    

Visitez la [Documentation MDN - Accessibilité mobile][93] si vous voulez en savoir plus.

## Tester l'accessibilité avec des outils

Il existe plusieurs outils que vous pouvez utiliser pour tester l'accessibilité de votre page. [Lighthouse][94] dans les outils de développement Chrome est un outil open source qui analyse une page web pour la performance, l'accessibilité, le SEO, et plus encore. Il génère un rapport sur la façon dont une page se comporte dans ces domaines.

Voyons comment il aide à analyser l'accessibilité d'une page :

Ouvrez les outils de développement Chrome et accédez à l'onglet Lighthouse. Cliquez sur "Analyser le chargement de la page" et attendez quelques secondes. Il affichera un rapport contenant des informations sur le score d'accessibilité de votre page web et d'autres mesures. Il listera tous les problèmes d'accessibilité que vous pourriez avoir.

Prenons l'exemple suivant :

```
<h1>Bienvenue</h1>
<img src="image.jpg" />
<button tabindex="2">Cliquez ici</button>
<div onclick="alert('Cliqué !')" class="button">Cliquez-moi</div>
<form>
  <input type="text" />
</form>
```

Lorsqu'il est testé avec l'audit Lighthouse, il donne les résultats suivants :

![Audit Lighthouse avec des problèmes d'accessibilité](https://cdn.hashnode.com/res/hashnode/image/upload/v1739631885589/c886f304-aba2-44ac-8d75-88fac2f60c55.png)

Comme vous pouvez le voir, il a obtenu un score de 74 en accessibilité, ce qui signifie qu'il y a une marge d'amélioration. Il a également montré les problèmes d'accessibilité dans votre code HTML, comme vous l'auriez deviné en regardant le code :

-   Les éléments d'image n'ont pas d'attribut `alt`
    
-   Le champ de formulaire n'a pas d'étiquette
    
-   La valeur de `tabindex` est supérieure à 0.
    

Corrigeons ces problèmes et relançons le test :

![Audit Lighthouse avec une bonne accessibilité](https://cdn.hashnode.com/res/hashnode/image/upload/v1739632090527/2db4798a-53d3-4010-9756-83de8b0f208a.png)

Cette fois, il a obtenu 100 en accessibilité puisque nous avons suivi toutes les pratiques de base.

Comme vous pouvez le voir, il s'agit d'une page HTML très simple, et il est beaucoup plus difficile d'atteindre un score de 100 pour de grands sites web. Cependant, vous devriez viser un score aussi élevé que possible. Cela ne devrait pas être trop difficile si vous intégrez l'accessibilité à votre processus de développement.

Le score d'accessibilité seul ne signifie pas que votre site web est entièrement accessible. Vous devez également tester les points suivants :

-   Tests manuels avec un lecteur d'écran (VoiceOver sur Mac ou Narrator sur Windows).
    
-   Accessibilité au clavier – testez si chaque partie de votre site web est accessible au clavier.
    
-   Simuler votre site web avec différents contrastes de couleurs pour différentes déficiences visuelles.
    

Pour la simulation, les outils de développement Chrome fournissent un outil de rendu (Rendering) pour émuler votre site web selon différentes préférences, comme le mode clair/sombre, un contraste de couleurs élevé/faible, un mouvement réduit et diverses déficiences visuelles.

Pour y accéder, ouvrez les outils de développement, faites ⌘+maj+P (Ctrl+Maj+P sur Windows) et tapez "Rendering". Cela ouvrira la fenêtre suivante :

![Outil de rendu](https://cdn.hashnode.com/res/hashnode/image/upload/v1741959781294/36f6c233-9326-4acb-a551-e95a56a87d8a.png)

Si vous avez ajouté des media queries comme celle-ci, vous pouvez sélectionner ces préférences et tester si votre site web se comporte en conséquence :

```
@media (prefers-reduced-motion) {
    * {
        animation: none;
    }
}
```

Ainsi, lorsque vous sélectionnez `prefers-reduced-motion`, vous pouvez tester si toutes les animations ont été désactivées et comment votre site web fonctionne.

En dehors des outils de développement, il existe un plugin NPM appelé [eslint-plugin-jsx-a11y][95] qui évalue le code React JSX pour les problèmes d'accessibilité.

Vous pouvez trouver tous les extraits de code sur [GitHub][96].

## Conclusion

L'accessibilité n'est pas seulement une fonctionnalité ajoutée par-dessus votre code – elle doit faire partie intégrante du processus de développement. Lorsque vous rendez un site web accessible à tous, cela augmente non seulement votre base d'utilisateurs, mais favorise également l'inclusivité.

Même si les principaux bénéficiaires de l'accessibilité sont les personnes handicapées, elle profite également aux autres utilisateurs en rendant le site web plus facile à utiliser de manière générale. De nombreuses pratiques mentionnées dans l'article, comme l'utilisation d'éléments sémantiques, l'ajout des bons attributs, etc., sont très faciles à suivre et contribuent grandement à garantir l'accessibilité.

Si vous êtes débutant, vous avez déjà fait un excellent travail en apprenant l'accessibilité. Commencez à inclure des pratiques simples d'accessibilité dans vos projets. Avec le temps, inclure ces pratiques deviendra une habitude naturelle.

J'espère que ce guide deviendra votre ressource de référence pour tout ce qui concerne l'accessibilité. Si vous pensez que j'ai oublié quelque chose ou si vous avez besoin de clarifications sur certains concepts, n'hésitez pas à me contacter sur Twitter. Pour plus de contenu sur le développement web, consultez mon profil.

### Références

-   [Documentation MDN - Accessibilité][97]
    
-   [Web Dev Simplified - Guide sur l'accessibilité][98]
    

[1]: #heading-qu-est-ce-que-l-accessibilite
[2]: #heading-pratiques-d-accessibilite-de-base
[3]: #heading-html-semantique-et-non-semantique
[4]: #heading-contenu-textuel
[5]: #heading-mises-en-page
[6]: #heading-elements-interactifs
[7]: #heading-accessibilite-au-clavier
[8]: #heading-etiquettes-de-formulaire
[9]: #heading-liens
[10]: #heading-accessibilite-des-tableaux
[11]: #heading-pratiques-css-et-javascript-supplementaires
[12]: #heading-styliser-les-elements-de-formulaire
[13]: #heading-contraste-des-couleurs
[14]: #heading-pratiques-javascript
[15]: #heading-pratiques-d-accessibilite-avancees-wai-aria
[16]: #heading-l-attribut-role
[17]: #heading-attribut-aria-
[18]: #heading-mises-a-jour-de-contenu-dynamique
[19]: #heading-validation-de-formulaire-et-erreurs
[20]: #heading-utiliser-des-elements-non-semantiques-comme-boutons
[21]: #heading-accessibilite-multimedia
[22]: #heading-accessibilite-mobile
[23]: https://axesslab.com/what-is-a-screen-reader/
[24]: https://seo.co/semantic-html/
[25]: https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantic_elements
[26]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong
[27]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em
[28]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Emphasis_and_importance
[29]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Advanced_text_features#abbreviations
[30]: #heading-contraste-des-couleurs
[31]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling
[32]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element#content_sectioning
[33]: https://mdn.github.io/learning-area/tools-testing/cross-browser-testing/accessibility/native-keyboard-accessibility.html
[34]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element#forms
[35]: https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex
[36]: #heading-accessibilite-multimedia
[37]: https://mdn.github.io/learning-area/accessibility/html/good-form.html
[38]: https://mdn.github.io/learning-area/accessibility/html/bad-form.html
[39]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox
[40]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio
[41]: #heading-accessibilite-multimedia
[42]: https://webaim.org/
[43]: https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration
[44]: https://developer.mozilla.org/en-US/docs/Web/CSS/:visited
[45]: https://developer.mozilla.org/en-US/docs/Web/CSS/:focus
[46]: https://developer.mozilla.org/en-US/docs/Web/CSS/:hover
[47]: #heading-contraste-des-couleurs
[48]: https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes
[49]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#href
[50]: https://mdn.github.io/learning-area/accessibility/html/good-links.html
[51]: https://mdn.github.io/learning-area/accessibility/html/bad-links.html
[52]: https://axesslab.com/hand-tremors/
[53]: https://developer.mozilla.org/en-US/docs/Web/CSS/margin
[54]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Table_accessibility
[55]: https://webaim.org/resources/contrastchecker/
[56]: https://developer.chrome.com/docs/devtools/accessibility/contrast
[57]: https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event
[58]: https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event
[59]: https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event
[60]: https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event
[61]: https://mdn.github.io/learning-area/accessibility/css/form-validation.html
[62]: #heading-accessibilite-au-clavier
[63]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles
[64]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes
[65]: https://mdn.github.io/learning-area/accessibility/aria/aria-no-live.html
[66]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-live
[67]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-atomic
[68]: https://mdn.github.io/learning-area/accessibility/aria/aria-live.html
[69]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/alert_role
[70]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/ARIA_Live_Regions
[71]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-relevant
[72]: https://mdn.github.io/learning-area/accessibility/css/form-validation.html
[73]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-required
[74]: #heading-elements-interactifs
[75]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics#accessibility_of_non-semantic_controls_2
[76]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio
[77]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
[78]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement
[79]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Multimedia#creating_custom_audio_and_video_controls
[80]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Multimedia#audio_transcripts
[81]: https://mdn.github.io/learning-area/accessibility/multimedia/audio-transcript-ui/
[82]: https://github.com/mdn/learning-area/tree/main/accessibility/multimedia/audio-transcript-ui
[83]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track
[84]: https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video
[85]: #heading-pratiques-javascript
[86]: https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event
[87]: https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event
[88]: https://developer.mozilla.org/en-US/docs/Web/API/Element/touchstart_event
[89]: https://developer.mozilla.org/en-US/docs/Web/API/Element/touchend_event
[90]: https://medium.com/gitconnected/read-this-to-make-your-website-responsive-35af4ab7992b
[91]: https://fritz-weisshart.de/meg_men/
[92]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Mobile#user_input
[93]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Mobile
[94]: https://developer.chrome.com/docs/lighthouse/overview
[95]: https://www.npmjs.com/package/eslint-plugin-jsx-a11y
[96]: https://github.com/KunalN25/accessibilityguide
[97]: https://developer.mozilla.org/en-US/docs/Web/Accessibility
[98]: https://www.youtube.com/watch?v=2oiBKSjOOFE