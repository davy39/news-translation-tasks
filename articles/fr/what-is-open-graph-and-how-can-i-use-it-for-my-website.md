---
title: Qu'est-ce que l'Open Graph et comment l'utiliser pour mon site web ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-03-26T14:51:33.000Z'
originalURL: https://freecodecamp.org/news/what-is-open-graph-and-how-can-i-use-it-for-my-website
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/open-graph.jpg
tags:
- name: '#content marketing'
  slug: content-marketing
- name: 'Digital Marketing '
  slug: digital-marketing
- name: HTML
  slug: html
- name: marketing
  slug: marketing
- name: open graph
  slug: open-graph
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que l'Open Graph et comment l'utiliser pour mon site web ?
seo_desc: 'It can take a lot of time to build content and maintain a website. How
  can we make sure our content stands out when getting shared on social feeds around
  the internet?


  What is Open Graph?

  Why do I need it?

  What happens if I don’t have it?

  Starting w...'
---

Cela peut prendre beaucoup de temps pour créer du contenu et maintenir un site web. Comment pouvons-nous nous assurer que notre contenu se démarque lorsqu'il est partagé sur les fils d'actualité sociaux autour d'Internet ?

* [Qu'est-ce que l'Open Graph ?](#heading-quest-ce-que-lopen-graph)
* [Pourquoi en ai-je besoin ?](#heading-pourquoi-en-ai-je-besoin)
* [Que se passe-t-il si je ne l'ai pas ?](#heading-que-se-passe-t-il-si-je-ne-lai-pas)
* [Commencer avec les bases de l'Open Graph](#heading-commencer-avec-les-bases-de-lopen-graph)
* [Type de site web Open Graph](#heading-type-de-site-web-open-graph)
* [Quelques autres balises Open Graph qui valent la peine d'être ajoutées](#heading-quelques-autres-balises-open-graph-qui-valent-la-peine-detre-ajoutees)
* [Twitter et autres réseaux sociaux utilisant l'Open Graph](#heading-twitter-et-autres-reseaux-sociaux-utilisant-lopen-graph)
* [Images dans l'Open Graph](#heading-images-dans-lopen-graph)
* [Tester vos balises Open Graph](#heading-tester-vos-balises-open-graph)
* [Puis-je avoir un exemple ?](#heading-puis-je-avoir-un-exemple)

%[https://www.youtube.com/watch?v=QwEQKM4YRnU]

## Qu'est-ce que l'Open Graph ?

[Open Graph](https://ogp.me/) est un protocole internet qui a été créé à l'origine par [Facebook](http://fbdevwiki.com/wiki/Open_Graph_protocol) pour standardiser l'utilisation des métadonnées dans une page web afin de représenter le contenu d'une page.

Dans celui-ci, vous pouvez fournir des détails aussi simples que le titre d'une page ou aussi spécifiques que la durée d'une vidéo. Ces éléments s'assemblent tous pour former une représentation de chaque page individuelle de l'internet.

## Pourquoi en ai-je besoin ?

Le contenu sur l'internet est généralement créé avec au moins un objectif en tête -- le partager avec d'autres. Cela peut ne pas avoir d'importance si vous l'envoyez simplement à un ami, mais si vous voulez le partager ou voulez qu'il soit partagé sur un réseau social ou une application qui utilise des aperçus riches, vous voudrez que cet aperçu soit aussi efficace que possible.

%[https://twitter.com/colbyfayock/status/1237455806230077441]

Cela aidera à encourager les gens à consulter votre contenu et, inévitablement, à cliquer sur votre contenu.

## Que se passe-t-il si je ne l'ai pas ?

La plupart des réseaux sociaux essaieront par défaut de faire de leur mieux pour créer un aperçu de votre contenu. Cela ne se passe souvent pas très bien.

Prenons par exemple mon site web [colbyfayock.com](https://colbyfayock.com).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/simple-twitter-card.jpg)
_Exemple d'une simple carte Twitter_

Il récupère correctement le titre de ma page et la description, mais ce n'est pas le tweet le plus attrayant dans un fil d'actualité.

Contrastez cela avec l'aperçu d'un seul article et nous voyons une histoire différente.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/large-image-twitter-card.jpg)
_Exemple d'une carte Twitter avec une grande image_

Alors, que se passe-t-il si vous n'avez pas de balises Open Graph ? Rien de mal ne se passera, mais vous ne profiterez pas de certaines des fonctionnalités qui aident à faire ressortir votre contenu parmi les nombreuses autres contenus publiés sur l'internet.

## Commencer avec les bases de l'Open Graph

Les quatre balises Open Graph de base requises pour chaque page sont `og:title`, `og:type`, `og:image` et `og:url`. Ces balises doivent être uniques pour chaque page que vous servez, ce qui signifie que les balises de votre page d'accueil doivent toutes être différentes de celles de votre page d'article de blog.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/open-graph-twitter-card.jpg)
_Anatomie d'une carte Twitter utilisant les balises Open Graph_

Bien que cela devrait être assez simple, voici une explication de ce que signifie chaque balise :

* `og:title` : Le titre de votre page. Cela est généralement le même que la balise `<title>` de votre page web, sauf si vous souhaitez le présenter différemment.
* `og:type` : Le "type" de site web que vous avez. J'expliquerai plus en détail dans la section suivante, bien qu'un type "générique" soit "website".
* `og:image` : Cela devrait être un lien vers une image que vous souhaitez utiliser pour représenter votre contenu. Il devrait s'agir d'une image haute résolution que les réseaux sociaux utiliseront dans leurs fils d'actualité.
* `og:url` : Cela devrait être l'URL de la page actuelle.

Lorsque vous placez une balise sur votre site web, vous devez la placer dans la section `<head>` avec les autres métadonnées. La balise utilisée sera une balise `<meta>` et devrait ressembler à ce modèle :

```
<meta property="[NAME]" content="[VALUE]" />

```

Ainsi, si je devais créer un ensemble de quatre balises Open Graph de base pour mon site web, [colbyfayock.com](https://colbyfayock.com), cela pourrait ressembler à :

```html
<meta property="og:title" content="Colby Fayock - Un blog de designer UX et développeur front-end" />
<meta property="og:type" content="website" />
<meta property="og:image" content="/static/website-social-card-44070c4a901df708aa1563ac4bbe595a.jpg" />
<meta property="og:url" content="https://www.colbyfayock.com" />

```

## Type de site web Open Graph

Le protocole Open Graph propose quelques variations du "type" de site web qu'il prend en charge. Cela inclut des types comme website, article ou video.

Lorsque vous configurez vos balises Open Graph, vous voudrez avoir une idée du type qui conviendra le mieux à votre site web. Si votre page est axée sur une seule vidéo, il est probablement judicieux d'utiliser le type "video". Si c'est un site web général sans verticale spécifique, vous voudrez probablement utiliser le type "website".

Similaire aux autres, cela est unique pour chaque page. Ainsi, si votre page d'accueil est "website", vous pouvez toujours avoir une autre page de type "video".

Ainsi, si je devais créer un type Open Graph pour mon site web, cela pourrait ressembler à ce qui suit sur ma page d'accueil :

```html
<!-- colbyfayock.com -->
<meta property="og:type" content="profile" />

```

Lorsque vous naviguez vers un article de blog, cela ressemblerait à :

```html
<!-- https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping/ -->
<meta property="og:type" content="article" />

```

Vous pouvez trouver les types de sites web Open Graph les plus courants sur la page web Open Graph : [https://ogp.me/#types](https://ogp.me/#types)

## Quelques autres balises Open Graph qui valent la peine d'être ajoutées

Bien que vous devriez généralement être satisfait avec les bases, voici quelques autres balises qui valent la peine d'être ajoutées :

* `og:description` : Une description de votre page. Similaire à `og:title`, cela peut être la même chose que la balise `<meta type="description">` de votre site web, sauf si vous souhaitez la présenter différemment.
* `og:locale` : Si vous souhaitez localiser vos balises, il serait probablement judicieux d'inclure la locale. Le format est `language_TERRITORY`, où le défaut est `en_US`.
* `og:site_name` : Le nom du site web global sur lequel se trouve votre contenu. Si vous êtes sur une page d'article de blog, vous pourriez avoir un `title` utilisant le titre de cet article de blog, où le `site_name` serait le nom de votre blog.
* `og:video` : Vous avez une vidéo qui soutient votre contenu ? Voici une chance de l'inclure. Ajoutez un lien vers votre vidéo en utilisant cette balise.

Ces balises seront ajoutées selon le même modèle que précédemment :

```html
<meta property="[NAME]" content="[VALUE]" />

```

## Twitter et autres réseaux sociaux utilisant l'Open Graph

La plupart des réseaux sociaux adhèrent aux bases des normes Open Graph, mais certains d'entre eux incluent également leur propre extension pour aider à personnaliser l'apparence dans leur écosystème.

Twitter, par exemple, vous permet de spécifier `twitter:card`, qui est le type de "carte" que vous pouvez utiliser lorsqu'ils affichent votre site web. À l'heure actuelle, leurs types de cartes incluent :

* summary
* summary_large_image
* app
* player

Cela vous aidera à choisir comment vos liens sont utilisés dans leur fil d'actualité. Si vous choisissez `summary_large_image`, par exemple, Twitter affichera vos liens avec de grandes images haute résolution tant que vous les fournissez dans la balise `og:image`.

Voici quelques références rapides à la documentation sur la façon d'utiliser les balises Open Graph avec certains des sites de réseaux sociaux :

* Twitter : [https://developer.twitter.com/en/docs/tweets/optimize-with-cards/guides/getting-started](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/guides/getting-started)
* Facebook : [https://developers.facebook.com/docs/sharing/webmasters/](https://developers.facebook.com/docs/sharing/webmasters/)
* Pinterest : [https://developers.pinterest.com/docs/rich-pins/overview/](https://developers.pinterest.com/docs/rich-pins/overview/)
* LinkedIn : [https://www.linkedin.com/help/linkedin/answer/46687/making-your-website-shareable-on-linkedin?lang=en](https://www.linkedin.com/help/linkedin/answer/46687/making-your-website-shareable-on-linkedin?lang=en)

## Images dans l'Open Graph

Bien que l'ajout de votre image en tant que `og:image` devrait souvent suffire, il peut parfois être difficile de faire apparaître votre image correctement. Si vous semblez rencontrer des problèmes, le standard Open Graph inclut quelques balises d'image telles que `og:image:url` vs `og:image:secure_url` ainsi que `og:image:width` et `og:image:height`.

Essayez de vous assurer que vous suivez toutes les [notes et exemples dans la documentation Open Graph](https://ogp.me/#structured). De plus, certains des réseaux sociaux ont des exigences d'image. [Twitter, par exemple, exige](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary-card-with-large-image) un ratio de 2:1 avec une taille minimale de 300x157 et une taille maximale de 4096x4096 qui est inférieure à 5 Mo et au format JPG, PNG, WEBP ou GIF.

Si vous êtes bloqué, testez vos balises en utilisant les outils du réseau social pour voir si vous pouvez trouver le problème.

## Tester vos balises Open Graph

Heureusement, nos réseaux sociaux préférés fournissent également des outils pour nous aider à déboguer nos balises. Une fois que vous vous êtes assuré que vos balises apparaissent réellement dans le code source de votre site web, vous pourrez prévisualiser l'apparence de votre site web dans le fil d'actualité.

* Twitter : [https://cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator)
* Facebook : [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)
* Pinterest : [https://developers.pinterest.com/tools/url-debugger/](https://developers.pinterest.com/tools/url-debugger/)

## Approfondir les balises Open Graph

Bien que la plupart de celles-ci devraient couvrir un site web de base, il existe quelques autres balises qui pourraient vous aider, vous et votre entreprise, à être découverts sur les réseaux sociaux.

Si vous êtes intéressé à approfondir, [la documentation](https://ogp.me/) fait un excellent travail en fournissant une liste de toutes les balises disponibles pour vous d'utiliser.

[https://ogp.me/](https://ogp.me/)

## Puis-je avoir un exemple ?

Si vous cherchez simplement un exemple pour commencer, voici ce que vous devriez obtenir lorsque vous configurez vos balises pour [un article de blog](https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping/) :

```html
<meta property="og:site_name" content="Colby Fayock" />
<meta property="og:title" content="Anyone Can Map! Inspiration and an introduction to the world of mapping - Colby Fayock" />
<meta property="og:description" content="Chef Gusteau was a visionary who created food experiences for the world to enjoy. How can we take his lessons and apply them to the world of…" />
<meta property="og:url" content="https://www.colbyfayock.com/2020/03/anyone-can-map-inspiration-and-an-introduction-to-the-world-of-mapping/" />
<meta property="og:type" content="article" />
<meta property="article:publisher" content="https://www.colbyfayock.com" />
<meta property="article:section" content="Coding" />
<meta property="article:tag" content="Coding" />
<meta property="og:image" content="https://res.cloudinary.com/fay/image/upload/w_1280,h_640,c_fill,q_auto,f_auto/w_860,c_fit,co_rgb:232129,g_west,x_80,y_-60,l_text:Source%20Sans%20Pro_70_line_spacing_-10_semibold:Anyone%20Can%20Map!%20Inspiration%20and%20an%20introduction%20to%20the%20world%20of%20mapping/blog-social-card-1.1" />
<meta property="og:image:secure_url" content="https://res.cloudinary.com/fay/image/upload/w_1280,h_640,c_fill,q_auto,f_auto/w_860,c_fit,co_rgb:232129,g_west,x_80,y_-60,l_text:Source%20Sans%20Pro_70_line_spacing_-10_semibold:Anyone%20Can%20Map!%20Inspiration%20and%20an%20introduction%20to%20the%20world%20of%20mapping/blog-social-card-1.1" />
<meta property="og:image:width" content="1280" />
<meta property="og:image:height" content="640" />
<meta property="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content="https://res.cloudinary.com/fay/image/upload/w_1280,h_640,c_fill,q_auto,f_auto/w_860,c_fit,co_rgb:232129,g_west,x_80,y_-60,l_text:Source%20Sans%20Pro_70_line_spacing_-10_semibold:Anyone%20Can%20Map!%20Inspiration%20and%20an%20introduction%20to%20the%20world%20of%20mapping/blog-social-card-1.1" />
<meta property="twitter:site" content="@colbyfayock" />

```

## Vous cherchez d'autres moyens d'optimiser et d'analyser votre contenu ?

* [Comment ajouter une image de réseau social à votre dépôt de projet Github](https://www.freecodecamp.org/news/how-to-add-a-social-media-image-to-your-github-project/)
* [Comment comprendre Google Analytics et le trafic vers votre site web](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/)
* [Comment configurer et suivre les performances de votre chaîne YouTube avec Google Analytics](https://www.freecodecamp.org/news/how-to-set-up-and-track-youtube-channel-performance-with-google-analytics/)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f60a Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f60a Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>