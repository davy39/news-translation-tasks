---
title: Comment utiliser la propriété CSS text-wrap pour créer des mises en page de
  texte équilibrées sur vos sites web
subtitle: ''
author: Azubuike Duru
co_authors: []
series: null
date: '2025-04-14T13:57:22.508Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-text-wrap-property
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744638131989/38357168-abda-4f7b-8c4f-568f64b586df.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Responsive Web Design
  slug: responsive-web-design
seo_title: Comment utiliser la propriété CSS text-wrap pour créer des mises en page
  de texte équilibrées sur vos sites web
seo_desc: An inconsistent text layout can really ruin the look of your website’s design.
  Maybe a heading has an extra word that wraps to another line, or in a paragraph
  some lines are longer than others. This can leave the whole thing looking messy
  and hard to...
---

Une mise en page de texte incohérente peut vraiment ruiner l'apparence de la conception de votre site web. Peut-être qu'un titre a un mot supplémentaire qui se wrappe sur une autre ligne, ou dans un paragraphe, certaines lignes sont plus longues que d'autres. Cela peut laisser l'ensemble paraître désordonné et difficile à lire.

Auparavant, les développeurs utilisaient des balises comme `<br>` ou `<span>` pour ajuster manuellement l'espacement des mots. Mais que se passe-t-il dans les cas où vous devez également prendre en compte la réactivité du site web ? Eh bien, la nouvelle propriété `text-wrap: balance` en CSS peut maintenant calculer et diviser automatiquement les lignes de manière à ce que chaque mot paraisse organisé et uniforme. Comme ceci :

![Titre avant et après l'application de 'text-wrap: balance' pour un wrapping amélioré.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743742346617_Desktop+-+1-3.png align="left")

Dans cet article, vous apprendrez comment fonctionne la propriété `text-wrap` et comment l'utiliser dans votre code. Vous verrez également quelques exemples en cours de route.

Sans perdre de temps, passons directement à cela.

### Table des matières

* [Comprendre les problèmes](#heading-comprendre-les-problemes)
    
* [Présentation de text-wrap](#heading-presentation-de-text-wrap)
    
    * [Qu'est-ce que text-wrap ?](#heading-quest-ce-que-text-wrap)
        
    * [Syntaxe de base de text-wrap](#heading-syntaxe-de-base-de-text-wrap)
        
* [text-wrap vs. max-width : Quand utiliser chacun](#heading-text-wrap-vs-max-width-quand-utiliser-chacun)
    
    * [Quand utiliser max-width vs text-wrap](#heading-quand-utiliser-max-width-vs-text-wrap)
        
    * [Support des navigateurs et considérations](#heading-support-des-navigateurs-et-considerations)
        
* [Implémentation pratique : Guide étape par étape](#heading-implementation-pratique-guide-etape-par-etape)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre les problèmes

En plus de rendre les mots plus difficiles à lire lorsque votre texte est affiché de manière inégale, il y a d'autres problèmes que peut causer un texte mal affiché ou inégal sur votre site web dans son ensemble. Certains de ces problèmes sont :

* **Conception réactive** : Nous n'aurions aucun problème si nous pouvions concevoir manuellement pour chaque taille d'écran et placer et espacer soigneusement les lignes de notre texte exactement comme nous voulons que les utilisateurs les lisent. Malheureusement, nous ne pouvons pas faire cela, c'est pourquoi il est toujours crucial de rendre les conceptions réactives. Lorsque le texte s'ajuste d'une taille d'écran à une autre, les lignes se brisent, et ce qui semble bien sur un bureau peut sembler terrible sur une vue de tablette.
    
* **Titres et paragraphes courts** : Comme les paragraphes et les petits blocs de texte contiennent de nombreux mots, il y a une forte probabilité que les mots se terminent de manière très déséquilibrée. Souvent, nous voyons une ligne de titre se terminant par un seul mot, formant une forme maladroite dans la conception globale.
    
* **Contenu dynamique** : Si votre site web contient du contenu dynamique (comme des cartes de différentes tailles, des descriptions de produits ou des articles de blog), ne pas avoir de `text-wrap` peut faire en sorte que votre mise en page se brise ou semble imprévisible.
    

## Présentation de `text-wrap`

Dans la dernière section, nous avons examiné les problèmes attribués à la distribution inégale du texte. Dans cette section, vous verrez comment `text-wrap` est un changement de jeu dans la manière dont vous organisez votre texte.

Avant `text-wrap`, les développeurs dépendaient fortement de `max-width`, `text-align`, ou `<br>` pour contrôler les lignes de texte. La nouvelle propriété CSS `text-wrap` a été créée pour aider à briser le texte naturellement à travers les lignes sans le faire paraître déplacé, évitant ainsi le besoin d'essais et d'erreurs pour vérifier si le texte s'adapte.

### Qu'est-ce que `text-wrap` ?

`text-wrap` est une propriété CSS qui peut vous aider à ajuster et à espacer le texte automatiquement, à briser les lignes de manière uniforme sans utiliser la balise rigide `<br>`, et à ne pas avoir à dépendre de `text-align`, qui ne fonctionnait pas sur toutes les tailles d'écran.

Avec `text-wrap`, vos titres et paragraphes sont sûrs de bien paraître. Au lieu d'avoir certaines lignes qui semblent plus longues que d'autres, `text-wrap` organise tout proprement pour apparaître visuellement attrayant.

### Syntaxe de base de `text-wrap`

Il y a deux façons principales d'appliquer text-wrap à votre texte. Ces valeurs sont :

`text-wrap: balance`**: (L'équilibreur de titres intelligent)**

C'est la manière intelligente de dire au navigateur d'ajuster le texte de manière uniforme, quelle que soit la taille de l'écran.

Extrait de code :

```css
h1 {
  text-wrap: balance;
}
```

Dans ce code, les lignes de texte du titre se diviseront naturellement sans aucune ligne courte étrange.

`text-wrap: pretty;` **(L'équilibreur de paragraphes intelligent)**

Tout comme `text-wrap: balance` fonctionne mieux pour les titres, `text-wrap: pretty` est le meilleur pour styliser les longs paragraphes.

Extrait de code :

```css
p{
  text-wrap: pretty;
}
```

Le `p` dans ce code garantira que les paragraphes maintiennent une lisibilité naturelle.

**Autres valeurs incluent :**

| **Valeur** | **Description** |
| --- | --- |
| `wrap` | État par défaut |
| `nowrap` | Empêche le texte de se wrapper à la ligne suivante |
| `stable` | Assure que les choses sont maintenues en place jusqu'à ce que le contenu change lui-même |

## `text-wrap` vs. `max-width` : Quand utiliser chacun

`max-width` était toujours l'option privilégiée par les développeurs dans le passé. Bien que cette méthode fonctionne dans la plupart des cas, elle n'empêchera pas la distribution inégale du texte. Comparons-la avec la nouvelle propriété CSS `text-wrap` afin que vous sachiez quand utiliser chacune.

**Utilisation de** `max-width`:

```css
h1 {
  max-width: 400px;
}
```

Le `max-width` ici force le titre à ne pas dépasser une largeur de 400px. Cela peut être bon pour contrôler les courts paragraphes du corps mais peut causer des inégalités pour les titres lorsqu'on traite avec plusieurs tailles d'écran.

**Utilisation de** `text-wrap`:

```css
h1 {
  text-wrap: balance;
}
```

Ici, le navigateur brise dynamiquement le texte du titre de manière équilibrée, empêchant toute ligne unique de paraître étrange.

### Quand utiliser `max-width` vs `text-wrap`

Utilisez `text-wrap: balance` lorsque vous voulez une lecture de texte plus naturelle sans aucune rupture de ligne étrange.

Utilisez `max-width` lorsque vous devez contrôler la largeur du texte et ne vous souciez pas nécessairement de la manière dont les lignes se brisent.

Utilisez les deux si vous voulez une lecture plus naturelle dans une limite de largeur confinée.

```css
h1 {
  max-width: 500px;
  text-wrap: balance;
}
```

Cela garantit que le titre reste dans une limite de 500px tout en maintenant une distribution de texte uniforme.

### Support des navigateurs et considérations

Actuellement, Chrome et Edge sont les seuls navigateurs principaux qui supportent la nouvelle propriété `text-wrap`. Si vous construisez un projet qui doit fonctionner sur des navigateurs comme Safari et Firefox, vous devrez utiliser des méthodes traditionnelles de formatage de texte comme `text-align`, `<br>`, ou `max-width` à la place.

Extrait de repli :

```css
@supports (text-wrap: balance) {
  h1 {
    text-wrap: balance;
  }
}
```

Le `@support` est un conseil pro pour appliquer ce style uniquement aux navigateurs supportés.

## Implémentation pratique : Guide étape par étape

Maintenant que vous avez vu à quel point `text-wrap` peut être important et comment l'utiliser, mettons cette connaissance en pratique et voyons des exemples réels, comparons les écrans avant et après son utilisation (et non), et vérifions comment il réagit dans les conceptions réactives également.

### 1. Application de `text-wrap: balance` aux titres

Dans cette section, nous verrons comment les lignes de titre dans le sujet **"Comment utiliser l'équilibre du texte CSS : Un truc simple pour des conceptions plus fluides et plus propres"** se briseront sur différentes tailles et comment cela apparaît lorsque `text-wrap: balance` est appliqué.

**Sans** `text-wrap: balance`:

HTML

```html
<h1 class="title">Comment utiliser l'équilibre du texte CSS : Un truc simple pour des conceptions plus fluides et plus propres</h1>
```

CSS

```css
.title {
  font-size: 2.5rem;
  font-weight: bold;
}
```

Sans aucune application spéciale aux titres, il s'ajustera simplement librement.

Résultat :

![Titre sans 'text-wrap: balance', montrant un wrapping inégal.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743740541468_Screenshot+2025-04-04+at+5.21.36AM+1.png align="left")

**Avec** `text-wrap: balance`:

CSS

```css
.title {
  font-size: 2.5rem;
  font-weight: bold;
  text-wrap: balance;
}
```

Maintenant, le navigateur ajuste automatiquement les sauts de ligne pour assurer une distribution plus uniforme.

Résultat :

![Titre avec 'text-wrap: balance', montrant un comportement lisible intelligent et un wrapping](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743740708025_Screenshot+2025-04-04+at+5.24.26AM.png align="left")

### 2. Utilisation de `text-wrap: pretty` sur des paragraphes courts

Vous avez maintenant vu comment `text-wrap: balance` gère les titres, alors regardons aussi comment il brise les lignes de manière uniforme dans vos paragraphes de texte. Comme je l'ai mentionné ci-dessus, la valeur `pretty` est principalement utilisée pour les paragraphes ou les courts blocs de mots. Voici comment cela fonctionne et apparaît sur un bloc de texte.

**Sans** `text-wrap: pretty`:

HTML

```html
<p class="subText"> Savez-vous que la mise en page de texte incohérente peut ruiner l'apparence de la conception de votre site web ? Peut-être qu'un titre a un mot supplémentaire qui prend une autre ligne ou dans un paragraphe, certaines lignes sont plus longues que d'autres, laissant ainsi l'ensemble paraître désordonné et difficile à lire.</p>
```

CSS

```css
.subText {
  font-size: 1.2rem;
  line-height: 1.5;
}
```

Dans ce code, l'ajustement du texte se comportera normalement sans aucune contrainte intelligente.

Résultat :

![Paragraphe sans 'text-wrap: pretty', montrant un wrapping inégal.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743739991569_Screenshot+2025-04-04+at+5.11.08AM.png align="left")

**Avec** `text-wrap: pretty`:

CSS

```css
.subText {
  font-size: 1.2rem;
  line-height: 1.5;
  text-wrap: pretty;
}
```

Le code ci-dessus fait en sorte que les sauts de ligne soient uniformes de manière à ce qu'il soit plus facile pour quelqu'un de lire.

Résultat :

![Paragraphe avec 'text-wrap: pretty', montrant un comportement lisible intelligent et un wrapping](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743739834917_Screenshot+2025-04-04+at+5.09.49AM.png align="left")

### Comment `text-wrap` fonctionne dans la conception réactive

Lorsque vous utilisez `text-wrap` sur votre texte, vous n'avez pas à vous soucier de la manière dont il va apparaître sur diverses tailles d'écran. La vidéo ci-dessous vous montre ce que je veux dire par là :

![Un gif montrant comment 'text-wrap' s'ajuste en douceur sur un écran réactif](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743738297774_ScreenRecording2025-04-04at4.37.18AM-ezgif.com-video-to-gif-converter.gif align="left")

### Utilisation des requêtes média pour un contrôle supplémentaire

Combinez `media-queries` et `text-wrap` pour avoir un contrôle spécial sur la manière dont votre texte apparaît sur divers écrans.

```css
h1 {
  font-size: 2.5rem;
  text-wrap: balance;
}

/* Sur les petits écrans, réduisez la taille de la police et appliquez l'équilibrage du texte */
@media (max-width: 600px) {
  h1 {
    font-size: 2rem;
    text-wrap: balance;
  }
}
```

Ce code garantit que le texte de votre titre s'adapte et reste propre sur plusieurs tailles d'appareils.

## Conclusion

La manière dont le texte s'affiche est quelque chose à laquelle tout bon développeur devrait prêter attention. Cela joue un grand rôle dans l'expérience utilisateur. En utilisant `text-wrap`, vous pouvez vous assurer que les mises en page de votre site web ne paraissent pas désordonnées ou difficiles à lire.

L'une des meilleures choses concernant l'utilisation de `text-wrap` dans votre formatage de texte est qu'il fonctionne simplement à chaque fois. Vous n'avez pas besoin de vous soucier des balises `<br>`, d'ajuster `max-width`, ou de lutter avec l'alignement du texte.

Même s'il n'est pas encore supporté par tous les navigateurs, l'ajouter à votre prochain projet rendra votre conception à l'épreuve du temps afin qu'elle soit toujours intacte et belle.