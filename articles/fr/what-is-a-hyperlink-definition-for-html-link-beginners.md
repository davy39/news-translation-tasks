---
title: Qu'est-ce qu'un hyperlien ? Définition pour les débutants en liens HTML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-30T22:07:57.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hyperlink-definition-for-html-link-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/bas-van-den-eijkhof-aJfOuWeNzko-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
seo_title: Qu'est-ce qu'un hyperlien ? Définition pour les débutants en liens HTML
seo_desc: 'Links are a defining featute of the Web and you''ll find them everywhere.

  As their name suggests, they create links, or connections, between pages. This allows
  us to navigate quickly and easily from one webpage to another.

  You''ll find many types of li...'
---

Les liens sont une caractéristique définissante du Web et vous les trouverez partout.

Comme leur nom l'indique, ils créent des liens, ou des connexions, entre les pages. Cela nous permet de naviguer rapidement et facilement d'une page web à une autre.

Vous trouverez de nombreux types de liens sur le Web.

Il y a des liens qui vont d'un site web à un autre. Il y a des liens qui vont d'une page d'un site à une autre page du même site. Et il y a des liens qui vont d'une section d'un site à une autre section au sein du même site.

Cet article passe en revue la définition d'un hyperlien et comment créer une variété de liens différents en HTML.


## Qu'est-ce qu'un hyperlien ?

Un hyperlien, également appelé lien ou lien web, contient une adresse pour une destination et agit comme une référence à des données. Un utilisateur peut facilement suivre, sauter et être dirigé vers la destination en cliquant, en tapant ou en survolant le lien.

Un hyperlien peut être un morceau de texte, une image, une icône ou un graphique qui, lorsque vous cliquez dessus, pointe vers et vous naviguer vers une page web ou un document différent. Il peut également pointer vers une section ou un élément spécifique au sein de la même page web ou du même document.

En gros, les hyperliens sont des pointeurs cliquables vers une ressource.

Par exemple, [ce lien vers la page d'accueil de freeCodeCamp](https://www.freecodecamp.org/) est un hyperlien. Lorsque vous cliquez sur le texte souligné, le navigateur quitte cette page actuelle et vous redirige là-bas.

Chaque résultat de recherche Google est un hyperlien. Lorsque vous cliquez sur l'un d'eux, vous quittez la page de recherche et allez au résultat.

Sans hyperliens, vous devriez connaître chaque URL (Uniform Resource Locator) de chaque page web sur Internet afin de les visiter.

## Hyperliens et HTML

Un hyperlien est un élément dans un document HTML.

L'hypertexte est du texte avec des hyperliens. Le texte lié (la référence aux données) est appelé **texte d'ancrage**.

Vous utilisez des **balises d'ancrage** pour créer des hyperliens vers d'autres pages web. Ils créent des liens : un texte ou une image cliquable qui, lorsqu'on clique dessus, nous emmène à une nouvelle page ou à une partie différente de la même page.

Le HTML est constitué d'hyperliens. Ils sont une caractéristique essentielle et définissante du World Wide Web, et c'est ce qui a rendu le Web si réussi. Ils ont permis l'idée même de la navigation.

Ils nous donnent la capacité de connecter un document à un autre document à travers différents ordinateurs et réseaux.

L'idée a initialement pris naissance à partir des références savantes et des notes de bas de page dans les documents scientifiques, mais cela a conduit à la découvrabilité des sites web d'autres personnes au fil du temps.

Les utilisateurs pouvaient cliquer entre les pages non seulement du site web d'un auteur, mais aussi à travers les sites web d'autres auteurs et passer d'une page web à une autre. Tout pouvait être lié à autre chose, rendant la navigation vers différents endroits sur le Web facile. Et cela a fourni aux utilisateurs un accès plus large à l'information.

Le World Wide Web est composé de billions d'hyperliens reliant des billions de pages web les unes aux autres, créant quelque chose qui pourrait ressembler à une très grande toile d'araignée.


## Comment créer un lien HTML

Vous créez des liens avec l'élément en ligne `<a>`, où "a" signifie *ancre*.

Voici un exemple de balise de lien HTML :

```html
<a href="https://www.freecodecamp.org/">Page d'accueil de freeCodeCamp</a>
```

Décomposons cela :

- L'élément de lien a une balise d'ouverture `<a>` et une balise de fermeture `</a>`.
- Le texte que les utilisateurs voient et peuvent cliquer est entre les balises d'ouverture et de fermeture `a` – dans ce cas, `Page d'accueil de freeCodeCamp`. Il est appelé *texte de lien* et doit être descriptif de l'endroit où le lien mène.
- Sur la balise d'ouverture, `<a>`, un attribut `href` est ajouté, qui est l'abréviation de `hypertext reference`. La valeur de l'attribut `href` spécifie l'URL souhaitée à laquelle vous voulez que le lien emmène les utilisateurs lorsque le texte du lien est cliqué.
- N'oubliez pas le signe égal `=` et les guillemets `""` qui accompagnent l'attribut `href`.

Par défaut, les hyperliens ont un aspect différent de celui du texte brut ordinaire. Cela est fait à des fins d'utilisabilité et pour informer les utilisateurs que cela est effectivement un lien.

Par défaut, le texte aura une couleur bleue avec un soulignement. Vous pouvez cependant changer cela en ajoutant différents styles CSS.

Sur un ordinateur, lorsque vous survolez un lien, le pointeur change d'une flèche en une main pour indiquer que quelque chose est cliquable.

Ce type d'hyperlien dans l'exemple ci-dessus lie à d'autres sites. Il s'agit d'un lien externe, utilisé pour connecter deux pages de deux sites web complètement différents.

Dans ce cas, la valeur de `href` est une URL **absolue** – c'est-à-dire une adresse web complète du site avec son nom de domaine.

## Comment lier à une page différente au sein d'un site

Les liens internes sont des liens qui dirigent l'utilisateur vers différentes pages du même site. Ils ne pointent pas vers des sites externes.

Dans de tels cas, l'attribut `href` a une URL **relative**.

Par exemple :

```html
<nav>
    <ul>
        <li><a href="about.html">À propos</a></li>
        <li><a href="posts.html">Articles de blog</a></li>
        <li><a href="projects.html">Mes projets</a></li>
        <li><a href="contact.html">Contactez-moi</a></li>
    </ul>
</nav>
```

Dans l'exemple ci-dessus, nous avons créé une navigation qui contient des liens vers différentes pages du même site. Ils pointent vers la page "À propos", la page "Articles de blog", la page "Mes projets" et la page "Contactez-moi", respectivement.

Nous n'avons pas besoin de spécifier le nom de domaine et l'URL complète dans l'attribut `href` dans ce cas, car ces fichiers sont *relatifs* à notre projet et au répertoire de travail actuel.

Dans ce cas, tous les fichiers sont dans le même dossier et ont la même structure hiérarchique, donc écrire simplement le nom du fichier suffit.

## Comment créer un lien vers une section spécifique d'un site

Et si nous voulons qu'un lien saute à une partie spécifique de la page ?

Peut-être avez-vous mentionné un sujet et souhaitez-vous référer les lecteurs à une section plus loin dans la page où vous en parlez plus en détail.

Nous pouvons créer des liens qui connectent le contenu sur la même page.

Tout d'abord, allez à la section où vous voulez que le lien mène, et dans la balise d'ouverture, ajoutez un attribut `id`.

Par exemple, peut-être avons-nous un paragraphe que nous voulons référencer :

```html
<p id="extra-info">Meilleures villes à visiter</p>
```

Ensuite, dans votre lien, ajoutez un `#` et la valeur que vous avez donnée à l'attribut `id`, dans ce cas `extra-info` :

```html
<a href="#extra-info">Lisez plus d'informations sur les villes à visiter ici</a>
```

## Comment ouvrir un lien dans un nouvel onglet

Lorsque un lien pointe vers un site externe, il est bon de le faire ouvrir dans un onglet séparé. Nous ne voulons pas perdre les visiteurs de notre site.

Par défaut, le navigateur ouvre les liens dans le même onglet.

Nous pouvons changer ce lien :

```html
<a href="https://www.freecodecamp.org/">Page d'accueil de freeCodeCamp</a>
```

En celui-ci :

```html
<a href="https://www.freecodecamp.org/" target="_blank">Page d'accueil de freeCodeCamp</a>
```

Vous ajoutez l'attribut `target` à la balise d'ouverture `<a>`, et lui donnez la valeur `_blank` qui ouvre les liens dans un nouvel onglet.


## Comment créer des liens email

Les liens peuvent effectuer d'autres actions en plus de simplement lier à une autre page ou site web.

Par exemple, il y a des liens qui font apparaître et ouvrent le programme de messagerie par défaut et commencent un nouvel email à une adresse spécifiée.

```html
<a href="mailto:hellothere@gmail.com">Envoyez-moi un email !</a>
```

Cette fois, l'attribut `href` commence par `mailto:` puis l'adresse email à laquelle vous voulez envoyer un message.

Le lien par défaut ne semble pas différent des autres liens dont nous avons parlé ici. Mais lorsqu'il est cliqué, il commence automatiquement à composer un nouvel email avec le client email par défaut de l'utilisateur.

Lorsque cela se produit, le champ `à` est déjà rempli avec l'adresse email où vous voulez l'envoyer.

## Conclusion

Dans cet article, nous avons passé en revue la définition d'un hyperlien et pourquoi ils sont une partie si importante du Web.

Nous avons également appris comment créer différents types de liens en HTML.

Merci d'avoir lu et bon codage !