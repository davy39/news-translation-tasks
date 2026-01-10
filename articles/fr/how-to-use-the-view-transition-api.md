---
title: Comment utiliser l'API View Transition pour de meilleures transitions Web
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-07-01T15:51:33.660Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-view-transition-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751324398272/d2f05e29-6925-43da-8c41-14b1c18a4898.png
tags:
- name: view transitions
  slug: view-transitions
- name: CSS Animation
  slug: css-animation
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'API View Transition pour de meilleures transitions Web
seo_desc: If you want to add some amazing and visually appealing animations to your
  web page, the View Transition API is a great animation tool. It lets you create
  Cross-Document Transitions when navigating between pages. And not just in classic
  multi-page app...
---

Si vous souhaitez ajouter des animations visuellement attrayantes à votre page web, l'**API View Transition** (https://developer.mozilla.org/fr/docs/Web/API/View_Transition_API) est un excellent outil d'animation. Elle vous permet de créer des transitions entre documents lors de la navigation entre les pages. Et pas seulement dans les applications multi-pages classiques – vous pouvez également l'utiliser pour créer des transitions accrocheuses dans les applications monopages.

Dans cet article, vous apprendrez à :

* Activer les transitions entre documents avec une seule ligne de CSS

* Animer des éléments individuels comme les titres et les images

* Déboguer et affiner vos transitions

* Appliquer la même API aux interactions dynamiques dans les applications monopages en utilisant JavaScript

* Avoir une idée de son fonctionnement dans un environnement [React](https://react.dev/) ou [Next.js](https://nextjs.org/).

## Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)

* [Configuration de l'exemple](#heading-installation)

* [Activation des transitions entre documents](#heading-activation-des-transitions-entre-documents)

  * [Déboguer la transition](#heading-deboguer-la-transition)

  * [Première transition de vue](#heading-premiere-transition-de-vue)

  * [Comprendre les mécanismes internes des transitions de vue](#heading-comprendre-les-mecanismes-internes-des-transitions-de-vue)

  * [Animer les images entre les pages](#heading-animer-les-images-entre-les-pages)

  * [Opportunités d'animation infinies](#heading-opportunites-danimation-infinies)

* [Expérience monopage](#heading-experience-monopage)

  * [Configurer l'écouteur d'événements](#heading-configurer-lecouteur-devenements)

  * [La fonction addStoryCard()](#heading-la-fonction-addstorycard)

  * [Appliquer l'animation](#heading-appliquer-lanimation)

* [Transition de vue dans React.js](#heading-transition-de-vue-dans-reactjs)

* [Transition de vue dans Next.js](#heading-transition-de-vue-dans-nextjs)

* [Support des navigateurs](#heading-support-des-navigateurs)

* [Conclusion](#heading-conclusion)

* [Résumé](#heading-resume)

## Prérequis

Pour suivre ce guide et en tirer le meilleur parti, vous devez avoir :

1. **HTML et CSS de base** : Vous devez comprendre comment structurer une page web en utilisant HTML et appliquer des styles en utilisant CSS.

2. **Fondamentaux de JavaScript** : La familiarité avec la manipulation du DOM JavaScript, la gestion des événements et les fonctions de base vous aidera à suivre les exemples dynamiques.

3. **Environnement de navigateur moderne** : L'API View Transition est actuellement prise en charge dans les navigateurs basés sur Chromium comme Chrome et Edge. Assurez-vous d'utiliser un navigateur compatible.

4. **Bases de React et Next.js (optionnel)** : Vers la fin de l'article, nous explorons comment intégrer les transitions de vue dans React et Next.js. Une connaissance de base de la structure des composants et du routage dans ces frameworks sera utile, bien que non strictement nécessaire pour les concepts de base.

Si vous êtes nouveau dans l'un de ces sujets, vous pouvez toujours suivre et revenir à l'article plus tard avec une pratique concrète.

J'ai également créé une vidéo pour accompagner cet article. Si vous êtes du genre à aimer apprendre à partir de vidéos ainsi que de textes, vous pouvez la consulter ici :

%[https://youtu.be/Fb-RNqiDoiw]

## Configuration de l'exemple

Pour votre démonstration, vous avez deux pages HTML simples – `from.html` et `to.html` – qui partagent la même feuille de style (`style.css`). La page `from.html` affiche une grille de cartes d'histoires. Lorsque vous cliquez sur une carte de la première page, son image s'agrandit et se déplace vers la page `to.html`.

![Démonstration de la transition de vue](https://cdn.hashnode.com/res/hashnode/image/upload/v1750879534660/6fb3252f-aef2-42f9-8e64-3e106369c0a5.gif align="center")

```xml
<!-- from.html -->
<link rel="stylesheet" href="style.css">

<div class="stories-container">
    <div class="story-card">
        <img
            src="./assets/image-3.jpg"
            alt="World in the Glass"
            id="story-image"
        />
        <a href="./to.html">
            <div class="story-overlay">
                <div class="story-content">
                    <div class="story-tag" id="story-tag">
                        Sci-Fi
                    </div>
                    <h2 class="story-title">World in the Glass</h2>
                    <p class="story-description">
                        A cyberpunk adventure in a dystopian future
                        where reality and virtual worlds collide.
                    </p>
                </div>
            </div>
        </a>
    </div>
    <!-- plus de cartes d'histoires... -->
</div>
```

```xml
<!-- to.html -->
<link rel="stylesheet" href="style.css">

<section class="story-hero">
    <img id="hero-image" src="./assets/image-3.jpg" />
    <div class="story-hero-overlay" id="overlay">
        <div class="breadcrumb" id="breadcrumb">
            <a href="from.html">My Stories</a>
            <span class="breadcrumb-separator">/</span>
            <a href="#">World in the Glass</a>
        </div>
        <div class="story-tag" id="story-tag">Sci-Fi</div>
        <h1 class="story-title">World in the Glass</h1>
        <div class="story-meta" id="story-meta">
            <div class="story-meta-item">
                <span>Created: June 1, 2025</span>
            </div>
            <!-- balisage supplémentaire... -->
        </div>
    </div>
</section>

<section class="story-content-wrapper">
    <div class="story-content">
        <div class="story-main">
            <div class="story-chapter">
                <h2 class="chapter-title" id="title">
                    Chapter 1: The Discovery
                </h2>
                <!-- balisage supplémentaire... -->
            </div>
        </div>
    </div>
</section>
```

Au lieu de montrer tout le balisage HTML ici, j'ai inclus uniquement le fragment clé pour vous aider à comprendre l'idée. Vous trouverez le code complet dans le dépôt GitHub à la fin de l'article.

Vous verrez que la plupart de notre travail se fait dans `style.css`, car bien que l'API View Transition soit une API JavaScript, vous la contrôlez fortement avec CSS.

## Activation des transitions entre documents

Pour activer les transitions entre documents, ajoutez simplement cette ligne à votre CSS :

```css
@view-transition {
    navigation: auto;
}
```

Maintenant, lorsque vous naviguez entre deux pages – même en utilisant les boutons "Retour" et "Avant" du navigateur – vous verrez un fondu enchaîné fluide par défaut.

### Déboguer la transition

Si l'animation semble trop rapide, vous pouvez utiliser les outils de développement dans le navigateur Google Chrome pour la ralentir. Cela vous aide non seulement à suivre l'animation plus clairement, mais vous donne également une chance d'apprendre à déboguer les animations en utilisant les DevTools de Chrome. Suivez simplement les étapes ci-dessous :

* Ouvrez DevTools dans votre navigateur Chrome

* Cliquez sur l'icône des trois points en haut à droite (vous pouvez suivre le diagramme ci-dessous)

* Cliquez sur "Plus d'outils" → Animations

![Débogage de l'animation avec les DevTools de Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1750877041736/c8aa8b70-eb85-490a-9668-fc8791de7194.jpeg align="center")

* Ensuite, ralentissez la vitesse de l'animation (par exemple à 10 %) pour pouvoir la regarder en détail.

![Contrôle de la vitesse de l'animation avec DevTools](https://cdn.hashnode.com/res/hashnode/image/upload/v1750877234236/9fe44c73-ec28-4216-a40f-d13fe3bd5854.jpeg align="center")

### Première transition de vue

Par défaut, tout le document s'estompe, ce qui est assez ennuyeux. Pour animer un élément spécifique – comme le "titre de la page" – donnez-lui un `view-transition-name` :

```css
#title {
    view-transition-name: title;
}
```

Les deux pages utilisent le même `id="title"`, donc l'API sait qu'il faut les traiter comme un seul élément. Maintenant, lorsque vous cliquez sur une carte, le titre se déplace élégamment de sa position sur la première page à son emplacement sur la page de détail – en avant et en arrière. Avec ces trois lignes de code, vous obtenez une transition morphing assez décente ! N'est-ce pas intéressant ?

### Comprendre les mécanismes internes des transitions de vue

Pour voir comment l'API fonctionne sous le capot :

1. Ouvrez DevTools et mettez l'animation en pause.

2. Naviguez entre les pages. Vous remarquerez un nouvel overlay dans le panneau Éléments. Cet overlay est composé avec le pseudo-élément CSS `::view-transition`

   ![Découverte de ::view-transition](https://cdn.hashnode.com/res/hashnode/image/upload/v1750878635416/e58425ae-99a9-4a83-b16b-52b8fdf4f50f.jpeg align="center")

3. À l'intérieur, vous trouverez deux groupes de pseudo-éléments :

   * `::view-transition-group-root` (le fondu enchaîné par défaut)

   * `::view-transition-group-title` (pour l'élément nommé `title`)

     ![Groupes de pseudo-éléments de transition de vue](https://cdn.hashnode.com/res/hashnode/image/upload/v1750878743737/c84cd13d-0110-4f72-b635-6a31c08b2a11.jpeg align="center")

Vous pouvez cibler ces groupes en CSS. Par exemple, pour contrôler la durée de toutes les transitions :

```css
::view-transition-group(*) {
    animation-duration: 0.5s;
}
```

Ou pour désactiver le fondu enchaîné `root` par défaut tout en conservant votre animation `title` :

```css
::view-transition-group(root) {
    animation: none;
}
```

### Animer les images entre les pages

Animons l'image de l'histoire de la galerie vers l'image héroïque plus grande sur la page de détail. Ici, les ID diffèrent – `#story-image` sur `from.html` et `#hero-image` sur `to.html` – donc vous sélectionnez les deux et nommez la transition `picture` :

```css
#story-image,
#hero-image {
    view-transition-name: picture;
}
```

#### Animation par défaut

Par défaut, vous verrez deux instantanés en fondu enchaîné ("ancien" et "nouveau"). Mais cette animation n'est pas parfaite pour nous. Pour comprendre cela, vous allez un peu plus loin. Ouvrez DevTools à nouveau et mettez l'animation en pause. Ensuite, cliquez sur la carte d'histoire dans la page `from.html`. Maintenant, vous pouvez faire glisser le curseur de lecture en avant et en arrière dans le panneau Animations pour comprendre le problème et ajuster le chevauchement.

![Trouver le problème de chevauchement de l'animation par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1750933857022/7edf89cf-9cb3-4692-9f86-d1124700827d.gif align="center")

#### Approfondir le problème pour mieux le comprendre

En regardant, vous pouvez déjà voir le problème. Pendant que l'animation se joue, l'état de la page `from.html` (vous pouvez penser à cet état comme l'instantané de l'ancien état) chevauche l'état entrant ou l'instantané de la page `to.html`. Ils se mélangent l'un à l'autre d'une manière qui n'est pas visuellement agréable. Vous pouvez vérifier les instantanés de l'ancien et du nouvel état des transitions dans le panneau des éléments dans les DevTools.

![Problème de chevauchement identifié](https://cdn.hashnode.com/res/hashnode/image/upload/v1750938129914/eb9cb31f-2aaf-49e8-b46d-9b8edeb43cf5.jpeg align="center")

Là, vous remarquerez un nouveau groupe de pseudo-éléments `::view-transition-group(picture)`. Si vous le développez, un autre groupe apparaît : `::view-transition-image-pair(picture)`.

À l'intérieur, vous trouverez deux autres pseudo-éléments : `::view-transition-old(picture)` et `::view-transition-new(picture)`. La nomenclature est assez explicite. L'"image pair" reflète mon analogie précédente de traiter les états avant et après comme des instantanés – vous en avez un pour l'ancien état et un pour le nouvel état. Cela a du sens maintenant ?

#### Améliorer l'animation

Maintenant que vous comprenez le concept et avez identifié le problème, ajustons le CSS pour améliorer l'animation. Vous avez remarqué que le nouvel instantané apparaît au-dessus de l'ancien. L'ancien instantané couvre la hauteur complète de l'élément parent `::view-transition-image-pair(picture)`, tandis que le nouveau est plus petit. Ils s'estompent l'un sur l'autre, ce qui n'est pas génial.

Pour corriger cela, vous pouvez cibler à la fois les instantanés "ancien" et "nouveau" et définir leur `height` à 100 %. Puisque le fondu enchaîné par défaut semble un peu terne, vous désactiverez également l'animation intégrée et définirez leur propriété `mix-blend-mode` à `normal` pour qu'ils ne se chevauchent pas visuellement de manière étrange. Enfin, vous vous assurerez que les deux instantanés ont le même `border-radius` pour que la transition entre les deux semble fluide et cohérente.

```css
::view-transition-old(picture),
::view-transition-new(picture) {
    animation: none;
    mix-blend-mode: normal;
    height: 100%;
    border-radius: 0 0 30px 30px;
}
```

#### Approfondir pour découvrir les problèmes cachés

Maintenant, si vous répétez le processus de débogage et regardez de plus près, vous verrez que le problème de chevauchement est résolu. Mais il reste un problème : l'élément `::view-transition-new(picture)` en haut apparaît déformé. Vous pouvez corriger cela en définissant sa propriété `object-fit` à `cover` et en masquant tout `overflow`. Cela garantira que l'image s'adapte correctement sans s'étirer et reste bien dans son conteneur.

```css
#to::view-transition-new(picture) {
    object-fit: cover;
    overflow: hidden;
}
```

Ici, j'ai spécifiquement ciblé le pseudo-élément `::view-transition-new(picture)` de la page `to` en utilisant l'identifiant `#to` – car j'ai ajouté des ID uniques aux éléments de `from.html` et `to.html`.

```xml
<!-- from.html -->
<html lang="en" id="from">
    <!-- code ici -->
</html>

<!-- to.html -->
<html lang="en" id="to">
    <!-- code ici -->
</html>
```

Maintenant, si vous vérifiez l'animation de près, vous remarquerez que la transition de `from.html` à `to.html` semble parfaite.

Ensuite, traitons la navigation "retour" – la transition de `to.html` à `from.html`. Si vous déboguez cette transition inverse, vous verrez que l'ancien instantané `::view-transition-new(picture)` apparaît complètement déformé pendant l'animation.

![Problème de distorsion de la navigation retour](https://cdn.hashnode.com/res/hashnode/image/upload/v1750939152019/65b715c6-0e2b-4997-a9d1-795a5daab922.jpeg align="center")

Pour corriger cela, vous pouvez cibler le nouvel instantané sur la page `from` et définir son `object-fit` à `cover`.

```css
#from::view-transition-new(picture) {
    object-fit: contain;
}
```

Maintenant, si vous déboguez et inspectez à nouveau, la distorsion a disparu ! Mais si vous suivez attentivement l'animation, vous remarquerez un autre problème – l'instantané inférieur (qui est `::view-transition-old(picture)` sur la page `from.html`) – se chevauche de manière gênante, comme illustré dans le diagramme ci-dessous :

![Nouvel instantané chevauchant l'ancien](https://cdn.hashnode.com/res/hashnode/image/upload/v1750939706428/6f084418-c14e-4eb7-af50-aaca93d30d40.jpeg align="center")

Pour corriger cette dernière partie, vous pouvez cibler le pseudo-élément `::view-transition-old(picture)` sur la page `from`. Ensuite, vous appliquez `object-fit: cover`, masquez tout `overflow` et faites correspondre le `border-radius` à `20px` – tout comme l'instantané de destination – pour une transition fluide et visuellement cohérente.

```css
#from::view-transition-old(picture) {
    object-fit: cover;
    overflow: hidden;
    border-radius: 20px;
}
```

#### Affinage supplémentaire pour la perfection

Après avoir apporté ces modifications, l'animation de l'image semble enfin parfaite ! Comme vous pouvez le voir, l'API View Transition est à la fois simple et puissante. Tout ce qu'il faut vraiment, c'est cibler les bons pseudo-éléments et appliquer les compétences CSS que vous avez déjà pour affiner la transition.

Cela peut sembler un peu fastidieux au début – mais c'est la nature du travail d'animation, qu'il s'agisse de développement web ou de montage vidéo.

Ces petits ajustements détaillés sont ce qui rend vos animations plus fluides et votre expérience utilisateur vraiment agréable. Plus vous déboguez, plus vous découvrez d'opportunités d'amélioration. Alors plongeons un peu plus profondément et voyons s'il y a autre chose que vous pouvez affiner.

Si vous mettez l'animation en pause et naviguez de la page `from.html` à la page `to.html`, vous remarquerez que l'instantané du titre de la page entrante chevauche l'ancien – comme montré dans le diagramme ci-dessous.

![Problème de chevauchement du titre de la page](https://cdn.hashnode.com/res/hashnode/image/upload/v1750961028146/c1946f2d-f659-4ffb-a597-93ec176d6dce.jpeg align="center")

Vous pouvez résoudre cela facilement. Lorsque vos titres se chevauchent pendant la transition, masquez l'ancien titre au bon moment :

```css
::view-transition-old(title) {
    opacity: 0;
}
```

Maintenant, si vous vérifiez à nouveau, vous verrez que le titre ne chevauche plus – et l'animation semble enfin parfaite !

### **Opportunités d'animation infinies**

L'API View Transition n'est pas limitée à cibler uniquement des pseudo-éléments ou à s'appuyer sur des animations par défaut. Vous pouvez utiliser toutes vos compétences en animation et transition CSS pour créer des animations personnalisées époustouflantes et accrocheuses. Regardons un autre exemple pour mieux comprendre ce qui est possible.

#### Trouver l'opportunité

Lorsque vous passez de la page `from.html` à la page `to.html`, l'image s'anime en douceur. Mais il y a un problème : un calque plus sombre apparaît soudainement au-dessus de l'image, ainsi que le contenu textuel à l'intérieur. Le calque et le texte apparaissent brusquement, ce qui n'est pas génial. Alors corrigeons cela.

Si vous inspectez les éléments dans DevTools, vous verrez que j'ai intentionnellement donné au calque un ID de `#overlay`. Tout le contenu textuel de la page `to.html` se trouve à l'intérieur de cet élément.

Idéalement, lorsque vous passez de `from.html` à `to.html`, le calque devrait également apparaître avec une animation fluide. Remarquez que la page `from.html` n'a pas du tout ce calque. Jusqu'à présent, tout ce que vous avez fait a impliqué la transition entre des éléments qui existent sur les deux pages – des éléments qui ont des homologues. Mais dans ce cas, vous voulez passer de "rien" à "quelque chose". Et oui, c'est aussi possible avec l'API View Transition.

#### Implémenter l'idée

Sans rien dire de plus, allons-y et ciblons d'abord l'élément `#overlay` et attribuons-lui un nom de transition personnalisé "overlay". Cela nous donne la flexibilité de contrôler son animation séparément des autres éléments.

```css
#overlay {
    view-transition-name: overlay;
}
```

Maintenant que vous avez configuré cela, voyons ce qui se passe réellement. Si vous mettez l'animation en pause et la déboguez, comme avant, vous remarquerez un nouvel pseudo-élément `::view-transition-group(overlay)`. À l'intérieur de ce groupe, dans la paire d'images, vous trouverez uniquement `::view-transition-new(overlay)` – il n'y a pas de `::view-transition-old(overlay)`.

Pourquoi cela ? C'est simple : sur la page précédente (`from.html`), il n'y a pas d'élément avec l'ID `overlay`. Puisqu'il n'y a rien à capturer, le navigateur ne crée pas de `::view-transition-old(overlay)`.

De même, lors de la navigation de `to.html` à `from.html`, il n'y aura qu'un `::view-transition-old(overlay)` – et pas de `::view-transition-new(overlay)` – car le calque n'existe que sur la page que vous quittez.

Ce que vous voulez faire maintenant, c'est animer cet élément de manière agréable. Puisque vous passez de "rien" à "quelque chose", vous pouvez définir une animation CSS personnalisée. Un effet simple et élégant pourrait être un fondu depuis le bas.

#### Définir des images clés personnalisées

Pour y parvenir, vous pouvez définir une animation d'images clés personnalisée appelée `fade-in`. Dans cette animation, vous commencez par `opacity: 0` et positionnez l'élément légèrement plus bas – par exemple, `translateY(50px)` – puis vous l'animez vers le haut tout en le faisant apparaître.

```css
@keyframes fade-in {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
}
```

Pour l'inverse (fondu sortant), vous pouvez simplement faire revenir l'`opacity` à `0`.

```css
@keyframes fade-out {
    to {
        opacity: 0;
    }
}
```

#### Utiliser les animations d'images clés

Maintenant que vous avez défini vos animations d'images clés, vous pouvez cibler l'élément `::view-transition-new(overlay)` et lui appliquer l'animation `fade-in`. Vous ajouterez également un léger délai d'animation – disons `0.5` secondes. Ce délai garantit que notre animation personnalisée commence après que l'animation de fondu enchaîné par défaut soit terminée. Puisque vous avez précédemment défini un délai de `0.5` seconde pour la transition, ce timing aide tout à s'écouler en douceur, sans animations qui se chevauchent.

```css
::view-transition-new(overlay) {
    animation: 250ms cubic-bezier(0, 0, 0.3, 1) both fade-in;
    animation-delay: 0.5s;
}
```

Et dans le cas de l'état "ancien" (c'est-à-dire lorsque vous naviguez en arrière), vous ciblez simplement l'élément `::view-transition-old(overlay)` et lui appliquez l'animation `fade-out`.

```css
::view-transition-old(overlay) {
    animation: 50ms cubic-bezier(0.3, 0, 1, 1) both fade-out;
}
```

#### Affinage pour la perfection

Maintenant, faisons une pause et vérifions si un affinage est nécessaire. Cette étape est essentielle lors du travail avec les transitions de vue, c'est pourquoi je continue à l'insister.

Si vous regardez de près pendant les animations de fondu entrant et sortant, vous remarquerez un problème de débordement : une zone noire subtile apparaît brièvement sous le calque.

![Problème de calque noir en dessous](https://cdn.hashnode.com/res/hashnode/image/upload/v1750972763490/73f112e5-3fc1-4115-bbe1-0f23eee66577.jpeg align="center")

Pour corriger cela, vous pouvez simplement sélectionner tout le `::view-transition-group(overlay)` et masquer son `overflow`. Cela devrait régler le problème immédiatement.

```css
::view-transition-group(overlay) {
    overflow: hidden;
}
```

Maintenant, si vous vérifiez à nouveau, vous verrez que l'animation semble parfaite !

## Expérience monopage

Jusqu'à présent, vous avez exploré comment l'API View Transition fonctionne dans le contexte des applications multi-documents ou multi-pages – quelque chose qui n'était pas nativement possible auparavant.

Mais maintenant, changeons notre focus vers les applications monopages (SPA). Dans la plupart des SPA, les animations ont toujours fait partie de l'expérience, même avant l'introduction de l'API View Transition. Les développeurs ont longtemps utilisé divers trucs JavaScript pour créer des transitions fluides au sein des SPA. Mais avec l'API View Transition, vous pouvez maintenant implémenter ces transitions de manière native et beaucoup plus facilement. Jetons un rapide coup d'œil à son fonctionnement.

Parlons de l'interaction sur laquelle nous nous concentrons. Lorsque vous cliquez sur le bouton "Nouvelle histoire", une nouvelle carte d'histoire devrait apparaître. Ensuite, nous allons animer cette interaction en utilisant l'API View Transition.

Mais d'abord, laissez-moi vous montrer rapidement comment cela fonctionne sous le capot. C'est une simple opération DOM (Document Object Model). J'ai spécifiquement ciblé le bouton et ajouté un écouteur d'événements à son événement `onclick`. Alors, que fait cet écouteur ? Il crée un nouvel élément de carte et l'injecte directement dans le DOM. Décomposons comment ce code crée une nouvelle carte d'histoire en utilisant JavaScript.

### Configurer l'écouteur d'événements

Vous pouvez configurer l'écouteur d'événements en cinq étapes simples :

#### Étape 1 : Sélectionner le bouton

Vous commencez par sélectionner le bouton que l'utilisateur cliquera pour créer une nouvelle carte d'histoire. Cette ligne utilise `document.querySelector()` pour récupérer le premier élément de la page avec le nom de classe `.new-story-btn` et le stocke dans la variable `newStoryButton`.

```javascript
const newStoryButton = document.querySelector(".new-story-btn");
```

#### Étape 2 : Configurer l'écouteur d'événements de clic

Ensuite, ajoutez un écouteur d'événements de clic à ce bouton. Cela signifie que lorsque l'utilisateur clique sur le bouton "Nouvelle histoire", la fonction que vous définissez à l'intérieur de cet écouteur d'événements s'exécutera. La fonction est marquée `async` au cas où vous souhaiteriez utiliser `await` à l'intérieur – par exemple, si vous récupérez des données ou exécutez des animations qui doivent attendre.

```javascript
newStoryButton.addEventListener("click", async () => {
    // vous écrirez le code de l'écouteur ici
});
```

#### Étape 3 : Sélectionner le conteneur pour les cartes d'histoire

Maintenant que le bouton a été cliqué, vous récupérez le conteneur où nos cartes d'histoire sont affichées. Il s'agit de l'élément avec la classe `.stories-container`, et c'est là que vous ajouterez la nouvelle carte dans les étapes suivantes.

```javascript
// sélectionner le conteneur pour les cartes d'histoire
const container = document.querySelector(".stories-container");
```

#### Étape 4 : Créer une nouvelle carte d'histoire

Vous appellerez une fonction auxiliaire nommée `addStoryCard()` – probablement une fonction personnalisée qui retourne un élément DOM prêt à l'emploi représentant une carte d'histoire. Nous lui passons les détails de l'histoire : tag, titre, description et un chemin d'image. Cette fonction gère probablement la création de la structure HTML, le style et peut-être même les animations pour la carte.

```javascript
const newCard = addStoryCard({
    tag: "Fantasy",
    title: "Sky Kingdoms",
    description:
        "A tale of floating islands and the heroes who defend them.",
    image: "./assets/image-5.jpg",
});
```

#### Étape 5 : Ajouter la carte à la page

Enfin, la carte nouvellement créée est ajoutée au `.stories-container`, la rendant visible sur la page. À ce stade, l'utilisateur verra la carte d'histoire "Sky Kingdoms" apparaître dans la liste des histoires.

```javascript
container.appendChild(newCard);
```

C'est tout. Voici la fonction complète de l'écouteur d'événements :

```javascript
newStoryButton.addEventListener("click", async () => {
    const container = document.querySelector(".stories-container");

    const newCard = addStoryCard({
        tag: "Fantasy",
        title: "Sky Kingdoms",
        description:
            "A tale of floating islands and the heroes who defend them.",
        image: "./assets/image-5.jpg",
    });

    container.appendChild(newCard);
});
```

### La fonction `addStoryCard()`

Examinons de plus près la fonction auxiliaire `addStoryCard()`, qui est responsable de la génération d'une toute nouvelle carte d'histoire en utilisant une structure prédéfinie et en y insérant du contenu personnalisé.

#### Étape 1 : Trouver la carte de modèle

Vous commencez par sélectionner l'élément `.story-card` existant dans le DOM. Cet élément sert de modèle – un design prêt à l'emploi que vous pouvez cloner pour créer de nouvelles cartes. Vous ajoutez également une simple vérification de sécurité : si pour une raison quelconque le modèle n'existe pas sur la page, la fonction se termine immédiatement en retournant undefined.

```javascript
function addStoryCard(data) {
    const templateCard = document.querySelector(".story-card");
    if (!templateCard) return;
}
```

#### Étape 2 : Cloner le modèle

Une fois que vous avez le modèle, vous créez un clone profond de celui-ci en utilisant `cloneNode(true)`. Cela signifie qu'il copie l'élément et tous ses éléments enfants imbriqués – en préservant la structure complète de la carte. À ce stade, vous avez un nouvel élément de carte en mémoire qui ressemble exactement à l'original.

```javascript
const newCard = templateCard.cloneNode(true);
```

#### Étape 3 : Mettre à jour l'image (si disponible)

Si une image est fournie dans l'objet de données, vous trouvez la balise `img` à l'intérieur de la nouvelle carte et mettez à jour son attribut `img`.

```javascript
if (data.image) {
    const currentImage = newCard.querySelector("img");
    currentImage.setAttribute("img", `url('${data.image}')`);
}
```

#### Étape 4 : Mettre à jour le contenu textuel

Maintenant, vous personnalisez le texte de la carte :

* Vous cherchez les éléments `.story-tag`, `.story-title` et `.story-description` à l'intérieur de la carte.

* S'ils existent, vous définissez leur contenu textuel en fonction de l'objet de données qui a été passé. C'est là que l'histoire obtient son contenu réel – comme le tag ("Fantasy"), le titre ("Sky Kingdoms") et la description.

```javascript
const tag = newCard.querySelector(".story-tag");
const title = newCard.querySelector(".story-title");
const desc = newCard.querySelector(".story-description");
if (tag) tag.textContent = data.tag;
if (title) title.textContent = data.title;
if (desc) desc.textContent = data.description;
```

#### Étape 5 : Retourner la carte finale

Enfin, vous retournez la carte d'histoire entièrement préparée pour qu'elle puisse être ajoutée à la page où nécessaire.

```javascript
return newCard;
```

Voici donc la fonction complète `addStoryCard` :

```javascript
function addStoryCard(data) {
    const templateCard = document.querySelector(".story-card");
    if (!templateCard) return;

    // Cloner la carte
    const newCard = templateCard.cloneNode(true);

    // Mettre à jour l'image si fournie
    if (data.image) {
        const currentImage = newCard.querySelector("img");
        currentImage.setAttribute("img", `url('${data.image}')`);
    }

    // Mettre à jour le contenu
    const tag = newCard.querySelector(".story-tag");
    const title = newCard.querySelector(".story-title");
    const desc = newCard.querySelector(".story-description");
    if (tag) tag.textContent = data.tag;
    if (title) title.textContent = data.title;
    if (desc) desc.textContent = data.description;

    return newCard;
}
```

Maintenant, si vous cliquez sur le bouton "Nouvelle histoire", une nouvelle carte d'histoire apparaît dynamiquement – grâce aux simples opérations DOM que vous avez déjà écrites ci-dessus. Mais vous pouvez la rendre plus engageante. Au lieu que la carte apparaisse simplement, vous voulez ajouter une transition fluide et accrocheuse lorsqu'elle est ajoutée au conteneur.

Pouvez-vous faire cela avec du CSS simple ? Malheureusement, non – car la carte est ajoutée dynamiquement via JavaScript, le CSS seul ne capturera pas ce changement et ne l'animera pas. C'est là que l'API View Transition en JavaScript intervient. Avec juste un peu de code supplémentaire, vous pouvez donner vie à cette interaction avec un effet de transition fluide et poli.

### Appliquer l'animation

Dans votre fonction d'écouteur d'événements, après avoir créé le nœud DOM de la carte, vous l'avez simplement ajouté au conteneur en utilisant le code ci-dessous :

```javascript
container.appendChild(newCard);
```

Cette ligne – `container.appendChild(newCard)` – est l'opération principale que vous souhaitez animer.

Alors, comment faire en sorte que cette transition se produise en douceur ? Vous ne pouvez pas utiliser le CSS seul ici, car le nouvel élément est inséré dynamiquement en utilisant JavaScript. Mais ce n'est pas un problème, car JavaScript vous donne un contrôle total sur la manipulation du DOM, y compris la capacité d'appliquer des styles à la volée.

Pour activer l'API View Transition pour votre `newCard`, vous devez simplement lui attribuer un `viewTransitionName`. Vous pouvez le faire en définissant la propriété `style.viewTransitionName` sur l'élément `newCard`. Vous donnerez à la transition un nom `targeted-card`, tout comme vous l'avez fait dans l'exemple basé sur CSS précédemment.

```javascript
newCard.style.viewTransitionName = "targeted-card";
```

Cela indique au navigateur : "Suivez cet élément pendant la transition et animez-le." Et avec cette seule ligne, votre élément ajouté dynamiquement fait partie d'une animation d'interface utilisateur fluide et native.

Et maintenant, vous pouvez démarrer la transition en utilisant l'API JavaScript View Transition comme ci-dessous :

```javascript
const transition = document.startViewTransition(async () => {
    container.appendChild(newCard);
});
```

Ici, vous utilisez la méthode `startViewTransition()` fournie par le navigateur. Il s'agit d'une API moderne qui vous aide à animer les changements entre deux états visuels de la page – avant et après les mises à jour du DOM. À l'intérieur de `startViewTransition()`, vous passez une fonction de rappel asynchrone, dans ce cas :

```javascript
() => {
    container.appendChild(newCard);
}
```

Il s'agit de la modification du DOM que vous souhaitez animer : l'ajout de la `newCard` dans le `.stories-container`. Normalement, l'ajout d'un nouvel élément DOM apparaîtrait instantanément sur la page. Mais avec cette API, vous dites au navigateur :

> Hé, je vais modifier le DOM. Veuillez capturer l'état visuel avant la modification, appliquer ma mise à jour du DOM, puis animer la transition entre l'ancien et le nouvel état.

Maintenant, vous devez faire une pause ici et attendre que l'animation soit entièrement terminée, car il s'agit d'une tâche asynchrone. Vous pouvez le faire comme ci-dessous :

```javascript
await transition.finished;
```

Maintenant que l'animation est terminée, vous supprimez ce nom en le définissant sur `null`. Cette étape est importante pour éviter les animations non intentionnelles si la carte est mise à jour ou déplacée à nouveau. Considérez cela comme un nettoyage après la fin de l'animation.

```javascript
newCard.style.viewTransitionName = null;
```

Voici donc le code complet en une seule fois, combinant tout ce que nous venons de discuter.

```javascript
// nommer la transition
newCard.style.viewTransitionName = "targeted-card";

// démarrer la transition
const transition = document.startViewTransition(async () => {
    container.appendChild(newCard);
});

// attendre la fin de la transition
await transition.finished;

// enfin nettoyer la transition une fois terminée
newCard.style.viewTransitionName = null;
```

Maintenant, si vous rechargez la page et l'essayez, vous verrez une transition fluide et belle lorsqu'une nouvelle carte est créée. C'est une touche subtile, mais elle rend l'interaction beaucoup plus polie et dynamique.

Et c'est ainsi que vous pouvez exploiter la puissance de JavaScript pour ajouter n'importe quelle animation que vous souhaitez – tout comme vous l'avez fait avec CSS, mais en définissant les propriétés de style dynamiquement. Les possibilités sont infinies lorsque vous combinez vos compétences CSS avec la flexibilité de JavaScript et l'API View Transition.

![Transition de vue dans SPA](https://cdn.hashnode.com/res/hashnode/image/upload/v1751052383696/5f166113-6ca7-4f4c-b5dd-8fde64972523.gif align="center")

## Transition de vue dans React.js

Si vous êtes un développeur React, vous pouvez jouer avec le composant React expérimental `<ViewTransition>` pour utiliser cette API.

```javascript
import {unstable_ViewTransition as ViewTransition} from 'react';

<ViewTransition>
  <div>...</div>
</ViewTransition>
```

Veuillez noter que cette API est expérimentale et n'est pas encore disponible dans une version stable de React. Vous pouvez l'essayer en mettant à niveau les packages React vers la version expérimentale la plus récente.

* react@experimental

* react-dom@experimental

* eslint-plugin-react-hooks@experimental

Vous pouvez consulter les détails dans la [documentation officielle de React.js](https://react.dev/reference/react/ViewTransition).

## Transition de vue dans Next.js

Si vous êtes un développeur Next.js, tout comme React vanilla, vous pouvez essayer l'API View Transition.

Pour activer cette fonctionnalité, vous devez définir la propriété `viewTransition` sur true dans votre fichier `next.config.js`.

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
}
 
module.exports = nextConfig
```

Veuillez noter que `viewTransition` est un drapeau expérimental qui active la nouvelle API expérimentale View Transitions dans React. Veuillez consulter les détails dans la [documentation officielle de Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition).

## Support des navigateurs

Le support des navigateurs varie (Firefox ne le supporte pas encore), alors assurez-vous de consulter le [tableau de compatibilité](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API#browser_compatibility) avant de déployer en production.

## Conclusion

L'API View Transition vous permet de :

* Activer les transitions entre documents avec une ligne de CSS

* Animer des éléments individuels en les nommant

* Déboguer les transitions dans DevTools et affiner le timing et l'assouplissement

* Appliquer la même approche aux applications monopages en utilisant JavaScript

Pour plus de détails, consultez la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) sur les transitions de vue. Profitez de la création d'animations fluides et natives dans vos projets web !

Vous pouvez trouver tout le code source de ce guide dans [ce dépôt GitHub](https://github.com/logicbaselabs/view-transition-api-tutorial). Si cela vous a aidé d'une manière ou d'une autre, envisagez de lui donner une étoile pour montrer votre soutien !

De plus, si vous avez trouvé le guide précieux, n'hésitez pas à le partager avec d'autres qui pourraient en bénéficier. J'apprécierais vraiment vos commentaires – mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen), regardez mes [tutoriels de codage](https://youtube.com/@logicBaseLabs), ou connectez-vous simplement avec moi sur [LinkedIn](https://www.linkedin.com/in/sumitanalyzen/).