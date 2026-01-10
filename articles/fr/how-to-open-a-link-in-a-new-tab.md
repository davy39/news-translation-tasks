---
title: Comment ouvrir un lien dans un nouvel onglet – L'attribut HTML target blank
  expliqué
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-05-31T14:53:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-open-a-link-in-a-new-tab
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/markus-spiske-4qbS830djfs-unsplash.jpg
tags:
- name: freeCodeCamp Curriculum Guide
  slug: freecodecamp-curriculum-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment ouvrir un lien dans un nouvel onglet – L'attribut HTML target blank
  expliqué
seo_desc: 'There will be times where you will want your user to click on a website
  link and have it open in a new browser tab. But how do you do that in HTML?

  In this article, I will show you how to use the target="_blank" attribute through
  code examples. I wil...'
---

Il y aura des moments où vous voudrez que votre utilisateur clique sur un lien de site web et qu'il s'ouvre dans un nouvel onglet du navigateur. Mais comment faire cela en HTML ?

Dans cet article, je vais vous montrer comment utiliser l'attribut `target="_blank"` à travers des exemples de code. Je vais également parler des cas où vous devriez envisager d'utiliser cet attribut.

## Comment ouvrir un nouvel onglet de navigateur en utilisant `target="_blank"`

L'attribut `target="_blank"` est utilisé à l'intérieur de la balise d'ancrage d'ouverture comme ceci :

```html
<a href="website-link-goes-here" target="_blank">
```

Lorsque l'utilisateur clique sur le lien, un nouvel onglet du navigateur s'ouvrira automatiquement sur cette page.

Dans cet exemple, j'ai nesté un lien à l'intérieur d'une paire de balises de paragraphe pour diriger les gens vers freeCodeCamp.

```html
<p>Pour apprendre à coder gratuitement, veuillez visiter <a href="https://www.freecodecamp.org/learn" target="_blank">freeCodeCamp.org</a></p>
```

Lorsque vous cliquez sur le lien freeCodeCamp, un nouvel onglet du navigateur s'ouvrira pour vous.

%[https://codepen.io/jessica-wilkins/pen/zYRRdmQ?editors=1000]

Si j'omets l'attribut `target="_blank"`, alors le comportement par défaut serait de quitter la page web actuelle et d'aller directement au lien sans ouvrir un nouvel onglet du navigateur.

## Qu'est-ce que le mot-clé `noopener` ?

Le mot-clé `noopener` dans l'attribut `rel` est utilisé principalement pour des raisons de sécurité afin d'empêcher les utilisateurs malveillants de manipuler la page web originale via la propriété `[Window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)`. Si l'utilisateur malveillant accédait à votre objet window, il pourrait rediriger votre page vers une URL malveillante.

Vous pouvez utiliser le mot-clé `noopener` comme moyen d'aider à prévenir ce problème de sécurité. Voici comment le mot-clé `noopener` est utilisé :

```html
<a target="_blank" rel="noopener" href="https://devdocs.io/html/element/heading_elements">Documentation DevDocs</a>
```

Si vous souhaitez en savoir plus sur les préoccupations de sécurité que `rel=noopener` a aidé à résoudre, veuillez lire [cet article utile](https://mathiasbynens.github.io/rel-noopener/).

### Mises à jour du mot-clé `noopener`

En 2021, une mise à jour a été faite où les navigateurs modernes définissent désormais `rel=noopener` pour tout lien utilisant l'attribut `target=_blank`. Comme vous pouvez le voir dans ce [tableau Can I use](https://caniuse.com/rel-noopener), le mot-clé `noopener` est supporté par la plupart des navigateurs sauf Internet Explorer 11.

Même avec cette mise à jour, de nombreux développeurs utiliseront toujours `rel=noopener` pour les liens utilisant l'attribut `target=_blank`.

## Devriez-vous utiliser l'attribut `target="_blank"` tout le temps ?

Lorsque les utilisateurs cliquent sur un lien, le comportement par défaut est que ce lien s'ouvre sur la page actuelle sur laquelle ils se trouvent sans ouvrir un nouvel onglet du navigateur. Dans de nombreux cas, vous ne voulez pas changer ce comportement par défaut car les utilisateurs s'y sont habitués.

Vous devez réfléchir attentivement à quand il serait bon d'utiliser l'attribut `target="_blank"`. Un bon exemple serait si un utilisateur travaille sur une page et ne veut pas quitter cette page s'il clique sur un lien.

Dans cet exemple, nous créons un lien vers la [documentation DevDocs](https://devdocs.io/), afin que l'utilisateur puisse rester sur sa page actuelle et consulter une référence dans un nouvel onglet.

%[https://codepen.io/jessica-wilkins/pen/qBxxPdb?editors=1000]

## Conclusion

Vous pouvez utiliser l'attribut `target="_blank"` si vous voulez que vos utilisateurs cliquent sur un lien qui ouvre un nouvel onglet du navigateur.

L'attribut `target="_blank"` est utilisé à l'intérieur de la balise d'ancrage d'ouverture comme ceci.

```html
<a href="website-link-goes-here" target="_blank">
```

Le mot-clé `noopener` dans l'attribut `rel` est ajouté pour empêcher les utilisateurs malveillants de manipuler la page web originale via la propriété `[Window.opener](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)`.

```html
<a target="_blank" rel="noopener" href="link-goes-here">
```

Vous devez réfléchir attentivement à quand il serait bon d'utiliser l'attribut `target="_blank"` car vous ne voulez pas toujours changer le comportement par défaut des liens.

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours de programmation.