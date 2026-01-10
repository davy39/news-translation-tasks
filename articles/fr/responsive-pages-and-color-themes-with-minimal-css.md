---
title: Comment créer des pages réactives et des thèmes de couleurs avec un minimum
  de CSS
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-12-16T17:51:58.000Z'
originalURL: https://freecodecamp.org/news/responsive-pages-and-color-themes-with-minimal-css
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/root.jpeg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Comment créer des pages réactives et des thèmes de couleurs avec un minimum
  de CSS
seo_desc: 'Want to build a responsive website with color themes? Start at the root.

  If you happen to drop by my website, you may notice I’ve spruced it up a bit. Victoria.dev
  can now better respond to your devices and preferences.

  Most modern devices and web br...'
---

Vous souhaitez créer un site web réactif avec des thèmes de couleurs ? Commencez par la racine.

Si vous passez par mon site web, vous remarquerez peut-être que je l'ai un peu rafraîchi. [Victoria.dev](https://victoria.dev/) peut maintenant mieux répondre à vos appareils et préférences.

La plupart des appareils modernes et des navigateurs web permettent aux utilisateurs de choisir un thème clair ou foncé pour l'interface utilisateur. Avec les [requêtes média CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries), vous pouvez faire en sorte que les styles de votre propre site web changent pour correspondre à ce paramètre utilisateur !

Les requêtes média sont également un moyen courant de faire en sorte que les éléments des pages web changent pour s'adapter à différentes tailles d'écran. Cet outil est particulièrement puissant lorsqu'il est combiné avec des [propriétés personnalisées](https://developer.mozilla.org/en-US/docs/Web/CSS/--*) définies sur l'[élément racine](https://developer.mozilla.org/en-US/docs/Web/CSS/:root).

Voici comment utiliser les requêtes média CSS et les propriétés personnalisées pour améliorer l'expérience de navigation de vos visiteurs avec seulement quelques lignes de CSS.

## Comment répondre aux préférences de couleur des gens

La fonctionnalité média [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) peut être interrogée pour servir le schéma de couleur de choix de votre utilisateur. L'option `light` est la version par défaut si aucune préférence active n'est définie, et elle a [un bon support sur les navigateurs modernes](https://caniuse.com/mdn-css_at-rules_media_prefers-color-scheme).

De plus, les utilisateurs lisant sur certains appareils peuvent également définir des thèmes de couleur clair et foncé en fonction d'un calendrier. Par exemple, mon téléphone utilise des couleurs claires dans son interface utilisateur pendant la journée, et des couleurs sombres la nuit. Vous pouvez faire en sorte que votre site web suive cette tendance.

Évitez de répéter beaucoup de CSS en définissant des propriétés personnalisées pour vos thèmes de couleur sur votre pseudo-classe `:root`. Créez une version pour chaque thème que vous souhaitez supporter. Voici un exemple rapide sur lequel vous pouvez construire :

```css
:root {
    color-scheme: light dark;
}

@media (prefers-color-scheme: light) {
    :root {
        --text-primary: #24292e;
        --background: white;
        --shadow: rgba(0, 0, 0, 0.15) 0px 2px 5px 0px;
    }
}

@media (prefers-color-scheme: dark) {
    :root {
        --text-primary: white;
        --background: #24292e;
        --shadow: rgba(0, 0, 0, 0.35) 0px 2px 5px 0px;
    }
}

```

Comme vous pouvez le voir, vous pouvez utiliser des propriétés personnalisées pour définir toutes sortes de valeurs. Pour utiliser celles-ci comme variables avec d'autres éléments CSS, utilisez la [fonction](https://developer.mozilla.org/en-US/docs/Web/CSS/var()) [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/var()) :

```css
header {
    color: var(--text-primary);
    background-color: var(--background);
    box-shadow: var(--shadow);
}

```

Dans cet exemple rapide, l'élément `header` affichera maintenant les couleurs préférées de votre utilisateur selon les paramètres de son navigateur.

Les schémas de couleur préférés sont définis par l'utilisateur de différentes manières, selon le navigateur. Voici quelques exemples.

### Mode clair et sombre dans Firefox

Vous pouvez tester les modes `light` et `dark` dans Firefox en tapant `about:config` dans la barre d'adresse. Acceptez l'avertissement s'il apparaît, puis tapez `ui.systemUsesDarkTheme` dans la recherche.

Choisissez une valeur `Number` pour le paramètre, puis entrez `1` pour sombre ou `0` pour clair.

![Une capture d'écran de la configuration du thème de couleur dans Firefox](https://victoria.dev/blog/responsive-pages-and-color-themes-with-minimal-css/firefox-theme-setting.png)

### Mode clair et sombre dans Brave

Si vous utilisez Brave, trouvez les paramètres de thème de couleur dans **Paramètres** > **Apparence** > **Couleurs Brave**.

![Une capture d'écran de la configuration du thème de couleur dans Brave](https://victoria.dev/blog/responsive-pages-and-color-themes-with-minimal-css/brave-settings.png)

## Comment utiliser la mise à l'échelle variable

Vous pouvez également utiliser une propriété personnalisée pour ajuster facilement la taille du texte ou d'autres éléments en fonction de la taille de l'écran de votre utilisateur. La [fonctionnalité média `width`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/width) teste la largeur de la fenêtre d'affichage. 

Alors que `width: _px` correspondra à une taille exacte, vous pouvez également utiliser `min` et `max` pour créer des plages.

Interrogez avec `min-width: _px` pour correspondre à tout ce qui dépasse `_` pixels, et `max-width: _px` pour correspondre à tout ce qui va jusqu'à `_` pixels.

Utilisez ces requêtes pour définir une propriété personnalisée sur le `:root` afin de créer un ratio :

```css
@media (min-width: 360px) {
    :root {
        --scale: 0.8;
    }
}

@media (min-width: 768px) {
    :root {
        --scale: 1;
    }
}

@media (min-width: 1024px) {
    :root {
        --scale: 1.2;
    }
}

```

Ensuite, rendez un élément réactif en utilisant la [fonction](https://developer.mozilla.org/en-US/docs/Web/CSS/calc()) [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/calc()). Voici quelques exemples :

```css
h1 {
    font-size: calc(42px * var(--scale));
}

h2 {
    font-size: calc(26px * var(--scale));
}

img {
    width: calc(200px * var(--scale));
}

```

Dans cet exemple, multiplier une valeur initiale par votre propriété personnalisée `--scale` permet à la taille des titres et des images de s'ajuster automatiquement à la largeur de l'appareil de votre utilisateur.

L'unité relative `rem` aura un effet similaire. Vous pouvez l'utiliser pour définir des tailles pour les éléments par rapport à la taille de police déclarée à l'élément racine.

```css
h1 {
    font-size: calc(5rem * var(--scale));
}

h2 {
    font-size: calc(1.5rem * var(--scale));
}

p {
    font-size: calc(1rem * var(--scale));
}

```

Bien sûr, vous pouvez également multiplier deux propriétés personnalisées. Par exemple, définir `--max-img` comme une propriété personnalisée sur le `:root` peut vous faire gagner du temps plus tard en n'ayant pas à mettre à jour une valeur de pixel à plusieurs endroits :

```css
img {
    max-width: calc(var(--max-img) * var(--scale));
}

```

## Élevez votre jeu de réactivité

Essayez ces gains faciles pour un site web qui répond aux appareils et préférences de vos visiteurs. Je les ai mis à bonne utilisation maintenant sur [victoria.dev](https://victoria.dev/). Je vous invite à [me faire savoir ce que vous en pensez !](https://victoria.dev/contact)

Si vous avez aimé cet article, il y en a beaucoup plus d'où il vient. Abonnez-vous sur [victoria.dev](https://victoria.dev) pour voir les nouveaux articles en premier.