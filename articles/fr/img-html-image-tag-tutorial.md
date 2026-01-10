---
title: <img> HTML – Balise Image Tutoriel
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-11T15:28:58.000Z'
originalURL: https://freecodecamp.org/news/img-html-image-tag-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/imgTag.png
tags:
- name: HTML
  slug: html
- name: image
  slug: image
- name: Web Development
  slug: web-development
seo_title: <img> HTML – Balise Image Tutoriel
seo_desc: 'In HTML, you use the <img> tag to add images to websites. It is an inline
  and empty element, which means that it doesn''t start on a new line and doesn''t
  take a closing tag (unlike the paragraph (<p>) tag, for instance).

  The <img> tag takes several at...'
---

En HTML, vous utilisez la balise `<img>` pour ajouter des images aux sites web. C'est un élément en ligne et vide, ce qui signifie qu'il ne commence pas sur une nouvelle ligne et ne prend pas de balise de fermeture (contrairement à la balise de paragraphe (`<p>`), par exemple).

La balise `<img>` prend plusieurs attributs, dont `src`, `height`, `width` et `alt` sont les plus importants.

Connaître les tenants et aboutissants ainsi que certaines bonnes pratiques de la balise `<img>` est crucial car les images peuvent affecter négativement le temps de chargement de votre site et le SEO.

Donc, dans ce tutoriel, nous allons voir comment ajouter des images aux sites web en utilisant la balise `<img>`, comment utiliser ses attributs, quelques bonnes pratiques et des approches modernes pour utiliser `<img>`.

## Syntaxe de base de la balise HTML `<img>`

Voici la syntaxe de base pour ajouter une balise `<img>` à votre HTML :

```html
<img 
    src="assets/images/ring-tailed-lemurs.webp" 
    alt="Un groupe de lémuriens à queue annelée" 
/>
```

Maintenant, parlons de ses attributs et de leur fonctionnement.

## Attributs de la balise HTML `<img>`

### L'attribut `src`

L'attribut `src` indique la source de l'image. Sans lui, la balise elle-même ne serait pas fonctionnelle dans le monde réel.

Il indique au navigateur où trouver l'image. Il prend donc un chemin relatif si l'image est hébergée localement, ou une URL absolue si l'image est hébergée en ligne.

### L'attribut `alt`

L'attribut `alt` spécifie un texte alternatif pour l'image. Cela pourrait être le texte qui s'affiche en cas de défaillance du réseau, par exemple. Ou il pourrait afficher quelque chose lorsque la source de l'image est mal spécifiée, afin que les utilisateurs sachent de quoi il s'agit.

Dans l'extrait de code ci-dessous, la source de l'image est mal spécifiée, vous montrant le rôle que joue l'attribut `alt` :

```html
<img
     src="assets/images/ring-tailed-lemur.webp"
     alt="Un groupe de lémuriens à queue annelée"
/>
```

Voici le CSS qui centre l'image horizontalement et verticalement :

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   flex-direction: column;
   height: 100vh;
  }
```

Et cela ressemble à ceci :
![alt-text-1](https://www.freecodecamp.org/news/content/images/2021/08/alt-text-1.png)

L'attribut `alt` est très important pour 2 autres raisons :

- SEO : il indique aux robots d'indexation de quoi il s'agit
- Accessibilité : il aide les lecteurs d'écran à savoir de quoi il s'agit afin qu'ils puissent le signaler aux personnes malvoyantes. De plus, il permet aux utilisateurs avec une faible bande passante de savoir de quoi il s'agit.

### Les attributs `width` et `height`

Vous pouvez utiliser ces attributs pour spécifier une certaine largeur et hauteur pour vos images. Avec ces attributs, vous pouvez redimensionner l'image vers le bas ou vers le haut.

Idéalement, cependant, vous ne devriez pas redimensionner une image avec ces attributs. Nous aborderons cela plus en détail dans les bonnes pratiques.

## Bonnes pratiques pour la balise HTML `<img>`

### Ne pas redimensionner une image avec les attributs width et height.

C'est une mauvaise pratique car cela peut rendre l'image déformée et affecter la qualité.

Au lieu de cela, vous pouvez optimiser l'image à vos dimensions souhaitées avec un logiciel de retouche photo tel que Photoshop.

Dans l'extrait de code ci-dessous, je spécifie une largeur et une hauteur pour l'image – une mauvaise pratique :

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      height="440px"
      width="440px"
      alt="Un groupe de lémuriens à queue annelée"
/>
```

L'image ressemble à ceci :
![wrong-width-height-usage-1](https://www.freecodecamp.org/news/content/images/2021/08/wrong-width-height-usage-1.png)

Sans utiliser les attributs width et height, l'image ressemble à ceci :
![no-width-height-1](https://www.freecodecamp.org/news/content/images/2021/08/no-width-height-1.png)

C'est mieux ? Oui !

### Nommer vos images de manière appropriée

Nommer les images de manière appropriée peut aider les moteurs de recherche à comprendre de quoi il s'agit. Par exemple, nommez une image `ring-tailed-lemurs.webp` au lieu de `photo-1580855733764-084b90737008.webp`. Ce dernier n'est pas suffisant pour l'optimisation des moteurs de recherche (SEO).

### Réduire la taille du fichier image

La taille du fichier image est cruciale en ce qui concerne la vitesse de la page. Une taille d'image plus petite (qui préserve la qualité de l'image) réduit le temps de chargement tandis que les images plus grandes prennent une éternité à charger.

Il existe plusieurs outils et divers logiciels qui peuvent vous aider à faire cela. Certains exemples sont imageOptim, jStrip et PNGGauntet. Et si vous êtes préoccupé par le SEO, vous voudrez vous pencher sur ces outils – car la vitesse de la page est un facteur de classement important.

### Héberger les images avec un CDN

Imaginez si un site web est hébergé aux États-Unis mais qu'un utilisateur en Afrique souhaite y accéder. Les ressources telles que les images et les icônes devraient voyager des États-Unis à l'Afrique, ce qui ralentit le temps de téléchargement.

L'utilisation d'un CDN (Content Delivery Network) permettra aux images du site web d'être mises en cache dans plusieurs endroits à travers le monde. Le CDN peut ensuite les servir à partir des emplacements les plus proches de l'utilisateur, améliorant le temps de chargement et offrant une meilleure expérience utilisateur.

Cloudflare est un CDN populaire que de nombreux développeurs utilisent pour héberger leurs images.

### Utiliser un texte alternatif descriptif

L'utilisation d'un texte alternatif descriptif aide les moteurs de recherche à comprendre de quoi il s'agit. Mais cela ne s'arrête pas là – le texte alternatif doit également être pertinent par rapport à l'image.

Par exemple, utilisez ceci :

```html
<img
   src="assets/images/ring-tailed-lemurs.webp"
   alt="Un groupe de lémuriens à queue annelée"
/>
```

Au lieu de ceci :

```html
<img src="assets/images/ring-tailed-lemurs.webp" alt="Lemurs" />
```

### Utiliser l'attribut `title` pour afficher des infobulles

Tout comme l'attribut `alt`, vous pouvez utiliser l'attribut `title` pour afficher des informations supplémentaires sur l'image. Les navigateurs affichent cela sous forme d'infobulle lorsque l'utilisateur survole l'image.

```html
<img
    src="assets/images/ring-tailed-lemurs.webp"
    alt="Un groupe de lémuriens à queue annelée"
    title="Les lémuriens à queue annelée sont dirigés par des femelles"
/>
```

![tooltip-1](https://www.freecodecamp.org/news/content/images/2021/08/tooltip-1.png)

## Approches modernes de la balise `<img>`

Il existe diverses façons d'utiliser la balise `<img>` qui sont un peu plus à jour et modernes. Examinons-en quelques-unes maintenant.

### Chargement paresseux des images

Le chargement paresseux est un concept relativement nouveau de "charger ce qui est nécessaire". Avec le chargement paresseux, l'image est chargée uniquement lorsque l'utilisateur fait défiler jusqu'à son viewport.

Cela contraste avec le chargement impatient, qui charge chaque image immédiatement après que la page est rendue par le navigateur.

Pour appliquer le chargement paresseux, ajoutez l'attribut `loading` à la balise `<img>` et définissez la valeur sur "lazy".

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      alt="Un groupe de lémuriens à queue annelée"
      title="Les lémuriens à queue annelée sont dirigés par des femelles"
      loading="lazy"
/>
```

Les images sont souvent de très haute qualité et grandes de nos jours, mais cela peut avoir un impact négatif sur l'expérience utilisateur et le SEO – d'où l'introduction du chargement paresseux.

### Utiliser les balises `<figure>` et `<figcaption>`

Souvent, vous pourriez avoir besoin de spécifier à l'utilisateur la légende d'une image. Beaucoup de développeurs le font en plaçant une balise `<p>` juste après la balise `<img>`.

Cela pourrait ne pas être incorrect, mais cela va à l'encontre des bonnes pratiques et n'associe pas la légende à l'image, donc les moteurs de recherche ne comprendront pas ce que c'est.

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      alt="Un groupe de lémuriens à queue annelée"
      title="Les lémuriens à queue annelée sont dirigés par des femelles"
      loading="lazy"
/>
<p>Les lémuriens à queue annelée sont des animaux sociaux</p>
```

![wrong-captioning-1](https://www.freecodecamp.org/news/content/images/2021/08/wrong-captioning-1.png)

Il est clair qu'il n'y a pas d'association entre l'image et la légende dans l'exemple ci-dessus.

HTML5 a introduit les éléments `<figure>` et `<figcaption>` pour aider avec cela. Vous enveloppez la balise `<img>` à l'intérieur d'un élément `<figure>`, et vous spécifiez une légende dans l'élément `<figcaption>`.

Cela aide les moteurs de recherche à associer la légende à l'image, conduisant à de meilleures performances et SEO.

Les extraits de code ci-dessous et les captures d'écran vous montrent une image avec et sans les éléments `<figure>` et `<figcaption>` :

```html
<figure>
   <img
     src="assets/images/ring-tailed-lemurs.webp"
     alt="Un groupe de lémuriens à queue annelée"
     title="Les lémuriens à queue annelée sont dirigés par des femelles"
     loading="lazy"
   />
<figcaption>Les lémuriens à queue annelée sont des animaux sociaux</figcaption>
</figure>
```

![right-captioning](https://www.freecodecamp.org/news/content/images/2021/08/right-captioning.png)

Vous pouvez voir maintenant que l'image et la légende sont magnifiquement associées.

### Utiliser le format d'image .webP

.webP est un format d'image créé par Google. Selon le créateur, c'est un format d'image plus petit en taille que ses homologues - JPG, JPEG, PNG, mais avec la même qualité.

Ce format est de plus en plus largement accepté et est considéré comme le format d'image de nouvelle génération pour le web.

## Conclusion

J'espère que cet article vous aide à comprendre comment fonctionne la balise `<img>` en HTML afin que vous puissiez l'utiliser correctement dans vos projets. Si vous le faites, cela aidera à améliorer votre expérience utilisateur et votre SEO.

Merci beaucoup d'avoir lu, et continuez à coder.