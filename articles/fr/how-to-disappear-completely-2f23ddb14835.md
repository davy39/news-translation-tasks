---
title: Comment faire disparaître complètement le HTML
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-10-12T23:03:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-disappear-completely-2f23ddb14835
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VcnMqhkSm-S1cMhlKmg1Aw.jpeg
tags:
- name: Design
  slug: design
- name: halloween
  slug: halloween
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment faire disparaître complètement le HTML
seo_desc: 'We all want to disappear sometimes. HTML elements are no different. Sometimes
  they want to hide out for a while. Not cease to exist completely — just keep things
  on the down-low.

  Thankfully, when it comes to making HTML elements disappear, CSS offers...'
---

Nous voulons tous disparaître parfois. Les éléments HTML ne font pas exception. Parfois, ils veulent se cacher un moment. Pas cesser d'exister complètement — juste garder les choses discrètes.

Heureusement, lorsqu'il s'agit de faire disparaître des éléments HTML, CSS offre une variété d'options.

### Le CSS de l'invisibilité

Prenons un élément HTML avec la classe « ghost » et cachons-le.

```
//index.html
```

```
<div class="ghost">  <p>Je suis amical !</p></div>
```

```
//style.css
```

```
.ghost {
```

```
}
```

### Pixels morts

Par défaut, les éléments HTML sont visibles. Leur propriété CSS **visibility** par défaut est **visible**, mais vous pouvez changer cela et utiliser :

```
.ghost {
```

```
  visibility: hidden;
```

```
}
```

Maintenant, le fantôme est caché, mais il occupera toujours de l'espace sur la page.

### Sans laisser de trace

Si vous voulez rendre quelque chose invisible et qu'il n'occupe aucun espace, vous pouvez également utiliser la propriété CSS **display**.

Les développeurs utilisent généralement la propriété display pour déterminer si un élément HTML doit être affiché comme un élément de bloc ou un élément en ligne, mais elle peut également cacher complètement l'élément :

```
.ghost {
```

```
  display: none;
```

```
}
```

Et contrairement à **visibility: hidden**, un élément caché avec **display: none** n'occupera aucun espace sur la page.

### Âmes transparentes

![Image](https://cdn-media-1.freecodecamp.org/images/VvKVYtHZxvI6TxafCK-PM5JCKLfElNM0y6Oj)
_En train de partir, parti._

Vous pouvez également rendre un élément si transparent qu'il devient invisible en utilisant la propriété CSS **opacity**.

```
.ghost {
```

```
  opacity: 0.0;
```

```
}
```

Comme **visibility: hidden**, **opacity: 0.0** laissera un espace vide là où se trouve l'élément HTML. N'oubliez pas qu'avec toutes ces techniques, l'élément reste une partie du DOM — il n'est simplement pas visible pour les utilisateurs normaux dans leurs navigateurs.

### Fuyez ! Fuyez loin, très loin !

Une dernière façon de cacher un élément consiste simplement à le déplacer si loin de la page que vous devrez zoomer énormément pour le voir.

Pour ce faire, utilisez d'abord la propriété CSS **position** pour donner à l'élément une position **absolute** sur la page (par opposition à **relative** par rapport à d'autres éléments HTML).

Ensuite, vous pouvez déplacer l'élément hors de la page d'un nombre arbitrairement grand de pixels :

```
.ghost {  position: absolute;  left: -999999px;}
```

Pourquoi faire cela ? Eh bien, c'est bon pour l'accessibilité de votre contenu. Les lecteurs d'écran — que les personnes malvoyantes utilisent pour naviguer sur Internet — peuvent capter ce contenu, et tout le monde ne saura pas que le contenu est là.

Pour de meilleurs résultats, positionnez ces éléments invisibles à gauche plutôt qu'en haut ou en bas, ce qui peut confondre les lecteurs d'écran.

### Être un fantôme pour Halloween

Lorsque vous combinez ces 4 techniques, vous obtenez un costume d'Halloween plutôt cool et peu coûteux :

![Image](https://cdn-media-1.freecodecamp.org/images/x7PSUq8ODURrsTF8jjGqHc1qU7XnXtgtY2hG)

J'ai créé cela avec l'aide d'Austin, designer et campeur Wes Searan.

Vous pouvez [vous en procurer un](https://www.freecodecamp.com/shop) jusqu'à la fin de ce week-end — en tailles pour hommes et femmes ajustées.

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**