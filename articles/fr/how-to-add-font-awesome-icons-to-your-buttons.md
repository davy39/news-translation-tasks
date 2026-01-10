---
title: Comment ajouter des icônes Font Awesome à vos boutons
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T19:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-font-awesome-icons-to-your-buttons
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2b740569d1a4ca3bbb.jpg
tags:
- name: Design
  slug: design
- name: fonts
  slug: fonts
seo_title: Comment ajouter des icônes Font Awesome à vos boutons
seo_desc: 'Font Awesome is a convenient library of icons. These icons can be vector
  graphics stored in the .svg file format or web fonts.

  These icons are treated just like fonts. You can specify their size using pixels,
  and they will assume the font size of the...'
---

Font Awesome est une bibliothèque pratique d'icônes. Ces icônes peuvent être des graphiques vectoriels stockés au format de fichier `.svg` ou des polices web.

Ces icônes sont traitées comme des polices. Vous pouvez spécifier leur taille en utilisant des pixels, et elles prendront la taille de police de leurs éléments HTML parents.

## Utilisation de base

Pour inclure Font Awesome dans votre application ou page, ajoutez simplement le code suivant à l'élément `<head>` en haut de votre HTML :

```html
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
```

L'élément `i` était à l'origine utilisé pour mettre d'autres éléments en italique, mais il est maintenant couramment utilisé pour les icônes. Vous pouvez ajouter les classes Font Awesome à l'élément `i` pour le transformer en icône, par exemple :

```html
<i class="fas fa-info-circle"></i>
```

Notez que l'élément `span` est également acceptable pour une utilisation avec les icônes.

Voici comment ajouter une icône :

```html
<i class="fas fa-thumbs-up"></i>
```

Cela produira une simple icône de pouce levé :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/thumbs-up.jpg)

Et voici comment insérer cette icône sur un bouton :

```html
<button>
  <i class="fas fa-thumbs-up"></i> J'aime
</button>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/thumbs-up-btn.jpg)

Remarquez qu'il y a deux parties pour utiliser une icône, le _préfixe de style_ et le _nom de l'icône_. Dans l'exemple ci-dessus, le préfixe de style et le nom de l'icône sont respectivement `fas` et `fa-thumbs-up`.

Font Awesome offre les préfixes de style suivants :

| Style  | Préfixe de style | Type de plan |
| --- | --- | --- |
| Solid | `fas` | Gratuit |
| Regular | `far` | Pro |
| Light | `fal` | Pro |
| Duotone | `fad` | Pro |
| Brands | `fab` | Gratuit |

Les icônes de marque sont souvent soumises par l'entreprise elle-même et sont utiles pour construire des éléments comme des boutons pour l'authentification sociale ou le paiement. Ces icônes incluent Twitter, Facebook, Spotify, Apple et même freeCodeCamp :

```html
<i class="fab fa-free-code-camp"></i>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/fcc-fa-icon.jpg)

Bien que vous n'ayez accès qu'aux icônes solides et de marque dans le plan gratuit, il existe de nombreuses façons de les styliser.

## Stylisation des icônes Font Awesome

Pour des applications simples, vous pourriez utiliser des styles en ligne :

```html
<span style="font-size: 3em; color: Tomato;">
  <i class="fas fa-thumbs-up"></i>
</span>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/styled-thumbs-up.jpg)

Pour le dimensionnement, vous pourriez également utiliser les mots-clés intégrés de Font Awesome :

```html
<i class="fas fa-thumbs-up fa-xs"></i>
<i class="fas fa-thumbs-up fa-sm"></i>
<i class="fas fa-thumbs-up fa-lg"></i>
<i class="fas fa-thumbs-up fa-2x"></i>
<i class="fas fa-thumbs-up fa-3x"></i>
<i class="fas fa-thumbs-up fa-5x"></i>
<i class="fas fa-thumbs-up fa-7x"></i>
<i class="fas fa-thumbs-up fa-10x"></i>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sizing-keywords.jpg)

Une chose importante à retenir est que les icônes FA héritent de la `font-size` du conteneur parent. Cela signifie que les icônes s'adaptent à tout texte qui pourrait être utilisé avec elles, ce qui maintient la conception cohérente.

Par exemple, disons que vous souhaitez créer plusieurs boutons. La taille par défaut des boutons est assez petite, vous écrivez donc un peu de CSS pour augmenter la taille des boutons, ainsi que le texte et les icônes qu'ils contiennent :

```html
<button>
  <i class="fas fa-thumbs-up"></i> J'aime
</button>

<button>
  <i class="fas fa-thumbs-down"></i> Je n'aime pas
</button>

<button>
  <i class="fas fa-share"></i> Partager
</button>
```

```css
button {
  font-size: 1.5em;
  margin: 5px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/buttons-ex.jpg)

Vous pouvez également ajuster la taille d'une icône directement en ciblant l'icône elle-même et en ajustant sa `font-size`.

Font Awesome est, eh bien, génial ! En tant que bibliothèque d'icônes la plus populaire, il est facile à inclure et à utiliser dans tous vos projets. Maintenant, allez ajouter des icônes à tout.

### Plus d'informations

* [Documentation Font Awesome](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use)
* [Toutes les icônes Font Awesome disponibles](https://fontawesome.com/icons)