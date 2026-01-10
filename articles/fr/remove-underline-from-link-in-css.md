---
title: Comment supprimer le soulignement d'un lien en CSS – Guide de style HTML
date: '2022-06-23T15:41:01.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/remove-underline-from-link-in-css
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/writing-326357_1280.jpg
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_desc: 'If you''re a web developer, you''ve probably wanted to get rid of the default
  underline that appears when you add a link to a page.

  Fortunately, just like other elements on a web page, you can style the anchor tags
  responsible for displaying a link.

  In...'
---


Si vous êtes un développeur web, vous avez probablement déjà voulu supprimer le soulignement par défaut qui apparaît lorsque vous ajoutez un lien à une page.

<!-- more -->

Heureusement, tout comme les autres éléments d'une page web, vous pouvez styliser les balises d'ancrage responsables de l'affichage d'un lien.

Dans cet article, je vais vous montrer comment supprimer le soulignement d'un lien avec CSS. Je vous présenterai également les quatre états dans lesquels un lien peut se trouver, et comment supprimer le soulignement pour chacun d'eux.

## Comment supprimer le soulignement d'un lien en CSS

Par défaut, voici comment la balise de lien apparaît dans le navigateur : ![ss1-4](https://www.freecodecamp.org/news/content/images/2022/06/ss1-4.png)

Premièrement, il est important de savoir que la balise de lien (balise d'ancrage) peut se trouver dans 4 états différents appelés pseudo-classes :

-   `a:link` : l'état normal du lien lorsqu'il n'est pas actif, visité ou survolé
-   `a:visited` : lorsque le lien a été cliqué par l'utilisateur, c'est-à-dire visité
-   `a:hover` : lorsque l'utilisateur survole le lien
-   `a:active` : lorsque l'utilisateur clique sur le lien

**N.B. :** Les états (pseudo-classes) doivent apparaître dans l'ordre listé ci-dessus en raison de la nature en cascade du CSS.

Pour enfin **supprimer le soulignement par défaut** du lien, vous pouvez cibler toutes les pseudo-classes et leur assigner une propriété `text-decoration` avec la valeur `none`.

```
<p>This is a <a href="#">link</a></p>
```

```
 a:link {
      text-decoration: none;
}

a:visited {
      text-decoration: none;
}

a:hover {
      text-decoration: none;
}

a:active {
      text-decoration: none;
}
```

![ss2-4](https://www.freecodecamp.org/news/content/images/2022/06/ss2-4.png)

Vous pouvez également supprimer le soulignement par défaut en une seule fois avec le sélecteur d'élément d'ancrage :

```
 a {
       text-decoration: none;
}
```

![ss3-5](https://www.freecodecamp.org/news/content/images/2022/06/ss3-5.png)

Vous pouvez manipuler les 4 pseudo-classes de la balise de lien avec ce Pen :

<iframe width="100%" height="350" src="https://codepen.io/koladechris/embed/bGLPzXr" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="CodePen embed" scrolling="no" allowtransparency="true" allowfullscreen="true" loading="lazy"></iframe>

## Conclusion

J'espère que cet article vous aidera à apprendre comment supprimer le soulignement par défaut des liens en CSS.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Merci de votre lecture.