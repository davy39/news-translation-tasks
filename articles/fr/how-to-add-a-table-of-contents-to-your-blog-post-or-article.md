---
title: Comment ajouter une table des matières à votre article de blog
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-02-12T15:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-table-of-contents-to-your-blog-post-or-article
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/table-of-contents.jpg
tags:
- name: blog
  slug: blog
- name: Blogger
  slug: blogger
- name: Blogging
  slug: blogging
- name: publishing
  slug: publishing
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: Comment ajouter une table des matières à votre article de blog
seo_desc: 'Providing a table of contents helps preview and prioritize content when
  writing lengthier articles. But not every platform makes it easy to add one. How
  can we implement one when we lack first class tooling?

  Want to skip ahead of the “what” and “why”...'
---

Fournir une [table des matières](https://en.wikipedia.org/wiki/Table_of_contents) aide à prévisualiser et à prioriser le contenu lors de la rédaction d'articles plus longs. Mais toutes les plateformes ne facilitent pas son ajout. Comment pouvons-nous en implémenter une lorsque nous manquons d'outils de première classe ?

Vous voulez passer directement au "comment" ? [Passez à la section "comment"](#heading-comment-ajouter-une-table-des-matieres) !

<figure class="kg-card kg-embed-card"><div class="fluid-width-video-container"><div class="fluid-width-video-wrapper" style="padding-top: 55%;"><iframe src="https://www.youtube.com/embed/MsrNdjp0aKI?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" name="fitvid0"></iframe></div></div></figure>

## Ce que nous allons créer

![Image](https://www.freecodecamp.org/news/content/images/2020/02/table-of-contents-example.jpg)
_Table des matières d'un article de blog_

Pour les besoins de cet article, nous allons utiliser le gestionnaire de contenu de freeCodeCamp.org à des fins visuelles et de démonstration. freeCodeCamp/news utilise la plateforme de blogging [Ghost](https://ghost.org/) au moment de la rédaction de cet article, mais cette méthode peut vraiment s'appliquer à n'importe quel article que vous écrivez.

## Pourquoi est-ce utile ?

Fournir une table des matières aide à améliorer l'expérience des personnes lisant votre article.

### Cela donne aux lecteurs un aperçu de l'article

Se lancer dans un article, au moins un long, peut être un grand engagement de temps. Personne ne veut passer 20 minutes de sa matinée pour se rendre compte qu'un article dans lequel il s'est plongé n'a pas réellement répondu à ses questions. Ou que c'est un réchauffé de quelque chose dont il est déjà un expert (bien que des perspectives différentes peuvent encore être utiles).

En fournissant cet aperçu, vous pouvez aider les gens à se faire une idée de ce à quoi s'attendre lorsqu'ils commencent à lire. Cela leur permet de prioriser leur temps avec l'autre liste d'articles qu'ils doivent lire.

### Cela fournit des points d'ancrage pour sauter vers un contenu spécifique

Similaire à la fourniture d'un aperçu, peut-être que quelqu'un veut lire une partie spécifique de la page. Peut-être est-ce parce qu'il peut sauter les premiers morceaux d'un tutoriel ou qu'il arrive d'un lien qu'un collègue a partagé dans [Slack](https://slack.com/).

Le point est, les gens peuvent utiliser la table des matières pour sauter vers les parties qui sont plus importantes pour eux.

### Bonus : cela vous aide en tant qu'auteur

Fournir une table des matières peut ne pas aider pour de nombreuses raisons pratiques, mais c'est un outil supplémentaire pour vous aider à prioriser et à comprendre le contenu de votre article. Cela sert de plan de haut niveau auquel vous pouvez vous référer lorsque vous vous assurez que le flux de votre histoire a réellement du sens.

## Ce qu'elle ne fait pas

Malheureusement, ce processus est manuel. Cette table des matières ne va pas se mettre à jour magiquement chaque fois que vous modifiez votre contenu. Assurez-vous donc d'être vigilant pendant le processus d'édition et de mettre à jour les liens brisés ou d'ajouter et de supprimer les modifications avant de publier.

## Comment pouvons-nous ajouter une table des matières ?

### En-têtes de contenu et liens d'ancrage

La clé de cette solution est d'utiliser les attributs `id` intégrés appliqués aux en-têtes de contenu dans le HTML lors de la création d'une page d'article. L'utilisation de ces attributs nous permet de créer un [lien d'ancrage](https://www.w3.org/TR/REC-html40/struct/links.html#h-12.2.3) qui fera défiler la position de défilement du navigateur jusqu'à l'emplacement de l'élément avec cet `id`.

Un exemple de base du HTML ressemble à ceci :

```html
<ul>
  <li><a href="#my-id">Lien vers Mon ID</a></li>
</ul>
<article>
  <p>Contenu très long</p>
  <h2 id="my-id">Chose Importante</h2>
  <p>Contenu important</p>
</article>

```

Dans l'exemple ci-dessus, nous pouvons voir que notre `article` contient du contenu de base (imaginez qu'il est beaucoup plus long que ci-dessus) avec un `h2` qui suit avec notre contenu important.

En fournissant à notre `h2` l'attribut `id`, nous pouvons maintenant créer un lien en définissant le `href` selon le modèle `#[id]` qui saura vers cet élément dans la page.

Maintenant, lors de la création de cela dans notre plateforme de blogging, nous n'avons pas nécessairement besoin de nous soucier d'écrire ce HTML. Mais nous devons comprendre comment trouver l'`id` afin de créer nos liens.

### Trouver notre ID d'en-tête

Nous pouvons utiliser les outils de développement de notre navigateur ([Chrome](https://developers.google.com/web/tools/chrome-devtools), [Firefox](https://developer.mozilla.org/en-US/docs/Tools)) pour trouver assez facilement nos précieux attributs `id` afin de créer nos liens.

En utilisant votre navigateur préféré, trouvez le titre que vous souhaitez utiliser, faites un clic droit sur le texte, puis sélectionnez "Inspecter" (ou "Inspecter l'élément") en bas du menu contextuel.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/browser-inspect-element-developer-tools.jpg)
_Utilisation de Chrome pour inspecter le HTML d'une page_

À partir de là, vous remarquerez qu'un panneau apparaît soit en bas de la page, soit sur le côté. Le placement de ce panneau n'a pas trop d'importance - c'est juste un [paramètre utilisateur](https://developers.google.com/web/tools/chrome-devtools/customize/placement). Mais nous pouvons maintenant voir le HTML de la page que nous regardons avec notre élément d'en-tête mis en évidence.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/developer-tools-highlight-element.jpg)
_Prévisualisation du HTML d'une page à l'aide des outils de développement de Chrome_

Après avoir trouvé notre en-tête dans le HTML, trouvez l'attribut `id`. Double-cliquez sur son contenu et copiez la valeur que nous utiliserons dans un instant.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/developer-tools-select-id.jpg)
_Sélection de l'attribut id à l'aide des outils de développement de Chrome_

### Création d'un lien vers notre en-tête

Puisque nous allons créer une table des matières, ouvrons la page d'édition de notre article et faisons défiler jusqu'en haut de la page.

La première chose que nous voulons faire est de commencer une liste, ce que nous pouvons faire en tapant un astérisque `*` suivi d'un espace lorsque nous commençons une nouvelle section de contenu.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/post-editor-add-list-ghost.gif)
_Ajout d'une nouvelle liste en utilisant Markdown dans Ghost_

Ensuite, écrivez ce que vous voulez que votre lien dise. Le plus souvent dans les tables des matières, le lien est exactement le même texte que l'en-tête lui-même.

Après avoir écrit ce que vous voulez, surlignez toute la ligne, et un petit menu contextuel apparaîtra au-dessus de votre sélection.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/post-rich-text-formatting-editing.jpg)
_Ouverture du menu de formatage de texte enrichi_

Sélectionnez la petite icône de lien et le menu contextuel se transformera en un champ de texte. Tapez dans le champ de texte un hashtag `#` suivi du contenu de l'attribut `id` que vous avez trouvé sur votre en-tête ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/post-edit-add-link.jpg)
_Ajout ou édition d'un lien_

Appuyez sur la touche Entrée et succès ! Nous avons un lien.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/post-list-with-link.jpg)
_Liste avec lien_

Répétez les étapes ci-dessus et créez 1 lien pour chaque en-tête de premier niveau auquel vous souhaitez lier.

Ne vous sentez pas obligé d'en faire trop, cependant. Typiquement, vous verrez des articles de blog inclure uniquement les en-têtes de premier niveau de la page, donc ne vous sentez pas obligé d'inclure chaque sous-en-tête. En fin de compte - faites ce avec quoi vous êtes à l'aise.

## Test et prévisualisation de votre table des matières

Une fois que nous avons terminé l'ajout de tous nos liens, nous pouvons prévisualiser ou afficher notre article et tester que nos liens fonctionnent.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/preview-post-freecodecamp-ghost.jpg)
_Prévisualisation ou affichage de l'article dans Ghost sur freecodecamp.org/news_

Après avoir ouvert votre prévisualisation ou votre page, faites défiler jusqu'à votre table des matières ou votre lien et cliquez dessus pour tester.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/table-of-contents-clicking-link.gif)
_Utilisation d'une table des matières_

Succès !

## Plus d'outils pour les auteurs

Une table des matières n'est qu'une façon d'aider les lecteurs à apprécier votre travail acharné. Quels autres outils utilisez-vous qui sont importants pour votre flux de travail ? Y en a-t-il d'autres que vous avez vus mais dont vous n'êtes peut-être pas sûr de la manière de les implémenter vous-même ?

Partagez avec nous sur Twitter à [@colbyfayock](https://twitter.com/colbyfayock) et [@freecodecamp](https://twitter.com/freecodecamp) !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? 0000fe0f Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 00002709 0000fe0f Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>