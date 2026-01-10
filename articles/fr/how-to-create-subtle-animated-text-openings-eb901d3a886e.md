---
title: Comment Créer des Ouvertures de Texte Animées Subtiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T08:41:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-subtle-animated-text-openings-eb901d3a886e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Seg0OuKEcq61DduMsmJh4Q.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment Créer des Ouvertures de Texte Animées Subtiles
seo_desc: 'By Emmanuel Ohans

  Have you ever seen subtle text openings and wondered how they came about?

  There’s so many of those out there, and it’s practically impossible to explain how
  they all work.

  However, let’s pick an example and let me show you how to re...'
---

Par Emmanuel Ohans

Avez-vous déjà vu des ouvertures de texte subtiles et vous êtes demandé comment elles étaient réalisées ?

Il en existe tant, et il est pratiquement impossible d'expliquer comment elles fonctionnent toutes.

Cependant, choisissons un exemple et laissez-moi vous montrer comment le recréer.

J'ai déjà fait mon choix, et voici ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/FOFdXz3y3MYBQM7vP2hUk1NY78dHfwX9a8j0)
_[La Démo](https://codepen.io/ohansemmanuel/full/QmjxJr/" rel="noopener" target="_blank" title=")_

C'est une ouverture de texte pour une agence créative fictive. Vous pouvez [voir les résultats](https://codepen.io/ohansemmanuel/full/QmjxJr/) ici.

Vous voyez le flash, n'est-ce pas ? Vous voyez aussi comment l'animation est décalée — au lieu d'animer tout le texte en une fois, chaque mot dans le texte est temporisé différemment ?

Je vais vous montrer comment recréer ces effets.

Mettez un sourire. Vous allez adorer !

### Introduction

Personne n'aime le balisage laid. En fait, nous n'écrireons pas beaucoup de balisage. Contentons-nous de recréer cette animation.

Tout d'abord, attrapez votre sweat à capuche (si vous en avez un) et mettez votre chapeau de développeur (vous devez en avoir un).

Maintenant, laissez-moi vous guider à travers le processus étape par étape. Ce n'est pas difficile, pour être honnête.

#### 1. Introduisez le balisage simple requis.

```
<section class="opening">  <h1 class="opening-text">    We are a creative agency  </h1></section>
```

![Image](https://cdn-media-1.freecodecamp.org/images/2SQawUW3As3NPhLnHML1AUqeFQlwdjBI9rvl)

#### 2. Ajoutez une belle image de fond.

```
.opening {  background-image: url('https://preview.ibb.co/cBVBf7/fantasy_3146946_1280.jpg')  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/OI9ZHoWdw5BckRO3X842MxaG-mDfwPt7R3In)

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/2XqScjEr75qscBxx0kubqwp-dNzjFGQaZiKq)
_Nous sommes partis de rien. Nous y voilà !_

Le résultat semble bizarre, car l'image de fond est répétée.

#### 3. Arrêtez la répétition et rendez l'image de fond plus belle.

```
.opening {  height: 100vh;  background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.9)), url('https://preview.ibb.co/hkXMDS/fantasy_3146946_1920.jpg') no-repeat 50% 0%/cover;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/DHuZ57bFKOGOGv5kvqNR8oTsSrKsIRu1WOY6)
_Cela semble encombré :(_

Si vous ne comprenez pas le code ci-dessus, il repose sur le principe que **plusieurs arrière-plans peuvent être ajoutés à un élément via CSS**. Ces arrière-plans doivent être séparés par une virgule. Dans l'exemple ci-dessus, le `linear-gradient` représente un arrière-plan, et le `url(..)` l'autre. L'un ajoute un dégradé linéaire, l'autre, une image.

Jetez un coup d'œil à l'illustration ci-dessus. Cela devrait avoir plus de sens maintenant.

Toujours confus ? Posez-moi vos questions dans la section des commentaires au fur et à mesure.

![Image](https://cdn-media-1.freecodecamp.org/images/jOPP-niRSksv16eptLDRa-PL9kp18XbSRg9V)
_Voici le résultat ! => L'image de fond est maintenant superposée avec un dégradé subtil. Plutôt cool, non ?_

#### 4. Positionnez le contenu du texte au centre.

Utilisez Flexbox !

```
.opening {  ...  display: flex;  justify-content: center;  align-items: center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/KQgGegIrFbxhLixaORQ5RqLBfbR1xmD7F8Rp)
_J'ai copié cette image d'un autre article de moi, au cas où vous ne sauriez pas [comment fonctionne Flexbox](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af" rel="noopener" target="_blank" title="). Prenez la partie nécessaire._

![Image](https://cdn-media-1.freecodecamp.org/images/plI1Nlc3XHCm4fs0Ue-aSUjJucOgtzU2W0Jm)
_Le texte est maintenant parfaitement centré. Hourra !_

#### 5. Juste avant d'animer, rendez le texte joli.

```
.opening-text {  margin: 0;  color: rgba(255,255,255,0.6);  text-transform: uppercase;  font-size: 3.6rem;  text-align: center;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZDHspwHmPX66WNtl1Qpu5vlWgysR9qhcna6L)
_Vous avez compris !_

![Image](https://cdn-media-1.freecodecamp.org/images/sBdFA96mIu-lGjmvvuKFyrBXta2MlM1jW5Nc)
_Hé ! Nous progressons. Cela a l'air bien ?_

#### 6. Préparez-vous à animer !

Si vous regardez le résultat final, vous remarquerez que chaque mot de la phrase est animé dans la scène. Nous avons besoin d'un moyen de séparer les mots en éléments individuels.

Occupons-nous de cela avec JavaScript.

En résumé, voici une représentation graphique de ce que nous voulons faire.

![Image](https://cdn-media-1.freecodecamp.org/images/PoAq4uC0vCRA23ELwt8Sdp20SZ2OHBI4-GvZ)
_Nous devons envelopper chaque mot dans un élément <span>._

Maintenant, vous comprenez la tâche à accomplir.

Et voici le code pour cela. J'espère que vous êtes à l'aise avec un peu de JavaScript car je vais vous en lancer.

```
const textNode = document.querySelector('.opening-text');const splitTextArr = textNode.innerText.split(" ");
```

```
let finalMarkup = "";splitTextArr.forEach(buildMarkup);function buildMarkup(text, index) {  let spanText;
```

```
  (index === 2) ?   spanText = "<span>" + text + "</span><br />" :   spanText = "<span>" + text + "</span> ";    return finalMarkup += spanText;}/** Substituez le contenu précédent par le nouveau balisage avec des éléments span */textNode.innerHTML = finalMarkup;
```

Ce n'est pas trop difficile à comprendre, mais j'ai illustré ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/06lqH-ZIXHxwaKby7cEFqYNLqXtfXY6rNpE9)
_Cela a un peu plus de sens maintenant ?_

NB : Dans la fonction `buildMarkup`, j'ai ajouté une balise `<br />` après le troisième mot. Cela garantira que le texte se casse au lieu de rester sur une seule ligne.

#### 7. Écrivez les Keyframes

```
@keyframes hide {    from { opacity: 1; }    to { opacity: 0; }}@keyframes glow {    from { text-shadow: 0 0 14rem white; }    to { text-shadow: 0 0 0 white; }}
```

Il y a deux animations différentes dont nous avons besoin pour l'effet final. L'une, l'animation `hide`, et l'autre, l'animation `glow`.

![Image](https://cdn-media-1.freecodecamp.org/images/cmeqklfx575gwke24yifzPXbOe9CjTVY0SZz)

Si vous n'êtes pas familier avec le fonctionnement des animations CSS, obtenir mon [Cours Avancé de CSS](https://www.educative.io/collection/5191711974227968/5641332169113600) est une évidence. En résumé, les animations sont largement alimentées par les `keyframes`.

Dans un bloc de keyframes, vous définissez le changement des propriétés d'un élément au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/HyHSpQLnuuEbQZDJNIQ6Hb9U4ySsYICfrWgL)

Voyez le code ci-dessus. Même si vous ne connaissez pas bien les animations CSS, je suis sûr que vous pouvez en comprendre un peu.

#### 8. Appliquez les animations aux éléments

```
.opening-text span {  opacity: 0;  animation:     hide 8s ease-in-out infinite,     glow 8s ease-in-out infinite;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/f8Gjpf8V3gd61-JBoxaoH9zQkLed9SR-UvBG)

![Image](https://cdn-media-1.freecodecamp.org/images/zCzQJ6XHd5FolHNEWuWSZdp3BXNzxCy0oBG8)
_Nous y voilà !_

Cela a l'air bien ?

Voici une petite explication.

La propriété CSS `text-shadow` est utilisée pour créer l'effet de flash sur le texte. Si vous ne savez pas comment fonctionne `text-shadow`, consultez la référence [codrops](https://tympanus.net/codrops/css_reference/text-shadow/). Même si j'écris du CSS depuis des années, je l'ai regardé pour un rafraîchissement, aussi.

Nous sommes dans ce cas ensemble !

#### 9. Enfin, décalez les animations pour un effet de décalage subtil.

```
.opening-text span:nth-child(6n) {    animation-delay: 900ms; }.opening-text span:nth-child(6n-1) {    animation-delay: 700ms; }.opening-text span:nth-child(6n-3) {    animation-delay: 600ms; }.opening-text span:nth-child(6n-4) {    animation-delay: 300ms; }.opening-text span:nth-child(6n-5) {    animation-delay: 0s; }
```

Après avoir enveloppé chaque mot dans un élément `span`, `.opening-text` contient maintenant six éléments. Chacun est ciblé en utilisant le sélecteur `nth-child`. Substituez `n = 1` dans les sélecteurs ci-dessus. Vous comprendrez le principe.

![Image](https://cdn-media-1.freecodecamp.org/images/EtnyKhMxDTNp9NNsnL0BTXWsqxCSvjRS42J0)

J'ai été paresseux, mais je suis sûr que si vous passez un peu plus de temps à ajuster les valeurs, vous aurez une animation plus belle.

Oui, nous l'avons fait ?

#### Bloqué quelque part ?

Faites-le-moi savoir dans les commentaires, et je serai heureux de vous aider.

### Prêt à devenir Pro ?

J'ai créé un guide CSS gratuit pour faire décoller vos compétences en CSS, immédiatement. [Obtenez l'ebook gratuit](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/Gg2sddawCgEIDygcY3rnjnZ1uaS4G172lEwG)
_Sept secrets CSS que vous ne connaissiez pas_