---
title: Le manuel HTML – Apprendre le HTML pour les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-07-23T10:22:00.000Z'
originalURL: https://freecodecamp.org/news/the-html-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-21-at-11.20.52-1.png
tags:
- name: handbook
  slug: handbook
- name: HTML
  slug: html
seo_title: Le manuel HTML – Apprendre le HTML pour les débutants
seo_desc: 'Introduction

  Welcome! I wrote this book to help you quickly learn HTML and get familiar with
  the advanced HTML topics.

  HTML, a shorthand for Hyper Text Markup Language, is one of the most fundamental
  building blocks of the Web.

  HTML was officially bo...'
---

# Introduction

Bienvenue ! J'ai écrit ce livre pour vous aider à apprendre rapidement le HTML et à vous familiariser avec les sujets avancés du HTML.

HTML, une abréviation pour Hyper Text Markup Language, est l'un des blocs de construction les plus fondamentaux du Web.

HTML est officiellement né en 1993 et depuis lors, il a évolué vers son état actuel, passant de simples documents textuels à l'alimentation d'applications Web riches.

Ce manuel s'adresse à un large public.

Tout d'abord, le débutant. J'explique le HTML à partir de zéro de manière succincte mais complète, afin que vous puissiez utiliser ce livre pour apprendre le HTML depuis les bases.

Ensuite, le professionnel. Le HTML est souvent considéré comme une chose secondaire à apprendre. Il peut être tenu pour acquis.

Pourtant, beaucoup de choses sont obscures pour beaucoup de gens. Moi y compris. J'ai écrit ce manuel pour aider ma compréhension du sujet, car lorsque j'ai besoin d'expliquer quelque chose, je m'assure mieux de d'abord connaître la chose de fond en comble.

Même si vous n'écrivez pas de HTML dans votre travail quotidien, savoir comment fonctionne le HTML peut vous aider à éviter quelques maux de tête lorsque vous devez le comprendre de temps en temps, par exemple en modifiant une page web.

Vous pouvez me rejoindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).

Mon site web est [flaviocopes.com](https://flaviocopes.com/).

[Note : vous pouvez télécharger une version PDF / ePub / Mobi de ce livre afin de pouvoir le lire hors ligne.](https://flaviocopes.com/page/html-handbook/)

## **Index du livre**

* [Préface](#heading-preface)
* [Bases du HTML](#heading-bases-du-html)
* [L'en-tête du document](#heading-lentete-du-document)
* [Le corps du document](#heading-le-corps-du-document)
* [Balises qui interagissent avec le texte](#heading-balises-qui-interagissent-avec-le-texte)
* [Liens](#heading-liens)
* [Balises conteneurs et structure de page HTML](#heading-balises-conteneurs-et-structure-de-page-html)
* [Formulaires](#heading-formulaires)
* [Tableaux](#heading-tableaux)
* [Balises multimédias : audio et vidéo](#heading-balises-multimedias-audio-et-video)
* [Iframes](#heading-iframes)
* [Images](#heading-images)
* [Accessibilité](#heading-accessibilite)

# PRÉFACE

HTML est la fondation de la merveille appelée le Web.

Il y a un pouvoir incroyable sous cet ensemble de règles plutôt simple et limité, qui nous permet -- développeurs, créateurs, designers, écrivains et bricoleurs -- de créer des documents, des applications et des expériences pour les gens du monde entier.

Mon premier livre sur HTML est sorti en 1997 et s'appelait "HTML Unleashed". Un gros livre, avec beaucoup de pages, un long tome.

Plus de 20 ans ont passé, et HTML est toujours la fondation du Web, avec des changements minimes depuis cette époque.

Bien sûr, nous avons obtenu plus de balises sémantiques, le HTML de présentation n'est plus une chose, et le CSS s'est occupé du design des choses.

Le succès d'HTML repose sur une chose : la **simplicité**.

Il a résisté à être détourné en un dialecte XML via XHTML, lorsque finalement les gens ont réalisé que cette chose était bien, bien trop complexe.

Il l'a fait grâce à une autre caractéristique qu'il nous offre : le **pardon**. Il y a _certaines_ règles, oui, mais une fois que vous les avez apprises, vous avez beaucoup de liberté.

Les navigateurs ont appris à être résilients et à toujours essayer de faire de leur mieux lors de l'analyse et de la présentation du HTML aux utilisateurs.

Et toute la plateforme Web a fait une chose correctement : elle n'a jamais rompu la compatibilité ascendante. Assez incroyablement, nous pouvons revenir aux documents HTML écrits en 1991, et ils ont à peu près la même apparence qu'à l'époque.

Nous savons même quelle était la première page web. C'est celle-ci : [http://info.cern.ch/hypertext/WWW/TheProject.html](http://info.cern.ch/hypertext/WWW/TheProject.html)

Et vous pouvez voir la source de la page, grâce à une autre grande caractéristique du Web et du HTML : **nous pouvons inspecter le HTML de n'importe quelle page web**.

Ne tenez pas cela pour acquis. Je ne connais aucune autre plateforme qui nous donne cette capacité.

Les outils de développement exceptionnels intégrés dans n'importe quel navigateur nous permettent d'inspecter et de nous inspirer du HTML écrit par n'importe qui dans le monde.

Si vous êtes nouveau dans le HTML, ce livre vise à vous aider à commencer. Si vous êtes un développeur Web expérimenté, ce livre améliorera vos connaissances.

J'ai tant appris en l'écrivant, même si je travaille avec le Web depuis plus de 20 ans, et je suis sûr que vous trouverez aussi quelque chose de nouveau.

Ou vous réapprendrez quelque chose d'ancien que vous aviez oublié.

Dans tous les cas, le but du livre est de vous être utile, et j'espère qu'il y parviendra.

## BASES DU HTML

HTML est une norme définie par le **WHATWG**, un acronyme pour Web Hypertext Application Technology Working Group, une organisation formée par des personnes travaillant sur les navigateurs web les plus populaires. Cela signifie qu'il est essentiellement contrôlé par Google, Mozilla, Apple et Microsoft.

Dans le passé, le **W3C** (World Wide Web Consortium) était l'organisation responsable de la création de la norme HTML.

Le contrôle a informellement passé du W3C au WHATWG lorsqu'il est devenu clair que la poussée du W3C vers XHTML n'était pas une bonne idée.

Si vous n'avez jamais entendu parler de XHTML, voici une courte histoire. Au début des années 2000, nous croyions tous que l'avenir du Web était XML (sérieusement). Ainsi, HTML est passé d'un langage d'auteur basé sur SGML à un langage de balisage XML.

C'était un grand changement. Nous devions connaître et respecter plus de règles. Des règles plus strictes.

Finalement, les éditeurs de navigateurs ont réalisé que ce n'était pas la bonne voie pour le Web, et ils ont résisté, créant ce qui est maintenant connu sous le nom de HTML5.

Le W3C n'était pas vraiment d'accord pour abandonner le contrôle de HTML, et pendant des années nous avons eu 2 normes concurrentes, chacune visant à être la version officielle. Finalement, le 28 mai 2019, il a été officiellement annoncé par le W3C que la version "vraie" de HTML était celle publiée par le WHATWG.

J'ai mentionné HTML5. Laissez-moi expliquer cette petite histoire. Je sais, c'est un peu confus jusqu'à présent, comme beaucoup de choses dans la vie lorsque de nombreux acteurs sont impliqués, mais c'est aussi fascinant.

Nous avions la **version 1 de HTML** en 1993. [Voici la RFC originale](https://tools.ietf.org/html/rfc1983).

**HTML 2** a suivi en 1995.

Nous avons obtenu **HTML 3** en janvier 1997, et **HTML 4** en décembre 1997.

Des temps occupés !

Plus de 20 ans se sont écoulés, nous avons eu toute cette histoire XHTML, et finalement nous en sommes arrivés à cette "chose" HTML5, qui n'est plus vraiment _juste du HTML_.

HTML5 est un terme qui définit désormais un ensemble de technologies, qui inclut HTML mais ajoute beaucoup d'API et de normes comme WebGL, SVG et plus encore.

La chose clé à comprendre ici est la suivante : il n'existe plus de version HTML à proprement parler. C'est une norme vivante. Comme CSS, qui est appelé "3", mais en réalité est un ensemble de modules indépendants développés séparément. Comme JavaScript, où nous avons une nouvelle édition chaque année, mais de nos jours, la seule chose qui compte est quelles fonctionnalités individuelles sont implémentées par le moteur.

Oui, nous l'appelons HTML5, mais HTML4 date de 1997. C'est une longue période pour quoi que ce soit, et encore plus pour le web.

C'est là que la norme "vit" maintenant : [https://html.spec.whatwg.org/multipage](https://html.spec.whatwg.org/multipage).

HTML est le langage de balisage que nous utilisons pour structurer le contenu que nous consommons sur le Web.

HTML est servi au navigateur de différentes manières.

* Il peut être généré par une application côté serveur qui le construit en fonction de la requête ou des données de session, par exemple une application Rails, Laravel ou Django.
* Il peut être généré par une application JavaScript côté client qui génère du HTML à la volée.
* Dans le cas le plus simple, il peut être stocké dans un fichier et servi au navigateur par un serveur Web.

Plongeons dans ce dernier cas. Bien que dans la pratique, ce soit probablement le moyen le moins populaire de générer du HTML, il est toujours essentiel de connaître les blocs de construction de base.

Par convention, un fichier HTML est enregistré avec une extension `.html` ou `.htm`.

À l'intérieur de ce fichier, nous organisons le contenu en utilisant des **balises**.

Les balises enveloppent le contenu, et chaque balise donne un sens spécial au texte qu'elle enveloppe.

Faisons quelques exemples.

Ce fragment HTML crée un paragraphe en utilisant la balise `p` :

```html
<p>Un paragraphe de texte</p>
```

Ce fragment HTML crée une liste d'éléments en utilisant la balise `ul`, qui signifie _liste non ordonnée_, et les balises `li`, qui signifient _élément de liste_ :

```html
<ul>
  <li>Premier élément</li>
  <li>Deuxième élément</li>
  <li>Troisième élément</li>
</ul>
```

Lorsque qu'une page HTML est servie par le navigateur, les balises sont interprétées, et le navigateur rend les éléments selon les règles qui définissent leur apparence visuelle.

Certaines de ces règles sont intégrées, comme la façon dont une liste est rendue ou comment un lien est souligné en bleu.

D'autres règles sont définies par vous avec CSS.

HTML n'est pas présentatif. Il ne se préoccupe pas de l'apparence des choses. Au lieu de cela, il se préoccupe de ce que les choses _signifient_.

C'est au navigateur de déterminer l'apparence des choses, avec les directives définies par celui qui construit la page, avec le langage CSS.

Maintenant, ces deux exemples que j'ai faits sont des extraits HTML pris en dehors du contexte d'une page.

### **Structure de la page HTML**

Faisons un exemple d'une page HTML correcte.

Les choses commencent avec la déclaration de type de document (aka _doctype_), une manière de dire au navigateur qu'il s'agit d'une page HTML, et quelle version de HTML nous utilisons.

Le HTML moderne utilise ce doctype :

```html
<!DOCTYPE html>
```

Ensuite, nous avons l'élément `html`, qui a une balise d'ouverture et de fermeture :

```html
<!DOCTYPE html>
<html>
...
</html>
```

La plupart des balises viennent par paires avec une balise d'ouverture et une balise de fermeture. La balise de fermeture est écrite de la même manière que la balise d'ouverture, mais avec un `/` :

```html
<sometag>some content</sometag>
```

Il existe quelques balises auto-fermantes, ce qui signifie qu'elles n'ont pas besoin d'une balise de fermeture séparée car elles ne contiennent rien _en elles_.

La balise de début `html` est utilisée au début du document, juste après la déclaration de type de document.

La balise de fin `html` est la dernière chose présente dans un document HTML.

À l'intérieur de l'élément `html`, nous avons 2 éléments : `head` et `body` :

```html
<!DOCTYPE html>
<html>
    <head>
    ...
    </head>
    <body>
    ...
    </body>
</html>
```

À l'intérieur de `head`, nous aurons des balises qui sont essentielles à la création d'une page web, comme le titre, les métadonnées, et le CSS et JavaScript internes ou externes. Principalement des choses qui n'apparaissent pas directement sur la page, mais aident seulement le navigateur (ou les robots comme le robot de recherche Google) à l'afficher correctement.

À l'intérieur de `body`, nous aurons le contenu de la page. Le **contenu visible**.

### **Balises vs éléments**

J'ai mentionné les balises et les éléments. Quelle est la différence ?

Les éléments ont une balise de début et une balise de fermeture. Dans cet exemple, nous utilisons les balises de début et de fermeture `p` pour créer un élément `p` :

```html
<p>Un paragraphe de texte</p>
```

Ainsi, un élément constitue le package complet :

* balise de début
* contenu textuel (et éventuellement d'autres éléments)
* balise de fermeture

Si un élément n'a pas de balise de fermeture, il n'est écrit qu'avec la balise de début et ne peut contenir aucun contenu textuel.

Cela dit, je pourrais utiliser le terme balise ou élément dans le livre signifiant la même chose, sauf si je mentionne explicitement la balise de début ou la balise de fin.

### **Attributs**

La balise de début d'un élément peut avoir des extraits spéciaux d'informations que nous pouvons attacher, appelés **attributs**.

Les attributs ont la syntaxe `clé="valeur"` :

```html
<p class="une-classe">Un paragraphe de texte</p>
```

Vous pouvez également utiliser des guillemets simples, mais utiliser des guillemets doubles en HTML est une belle convention.

Nous pouvons en avoir plusieurs :

```html
<p class="une-classe" id="un-id">Un paragraphe de texte</p>
```

et certains attributs sont booléens, ce qui signifie que vous n'avez besoin que de la clé :

```html
<script defer src="fichier.js"></script>
```

Les attributs `class` et `id` sont deux des plus courants que vous trouverez utilisés.

Ils ont une signification spéciale et sont utiles à la fois en CSS et en JavaScript.

La différence entre les deux est qu'un `id` est unique dans le contexte d'une page web ; il ne peut pas être dupliqué.

Les classes, en revanche, peuvent apparaître plusieurs fois sur plusieurs éléments.

De plus, un `id` est juste une valeur. `class` peut contenir plusieurs valeurs, séparées par un espace :

```html
<p class="une-classe une-autre-classe">Un paragraphe de texte</p>
```

Il est courant d'utiliser le tiret `-` pour séparer les mots dans une valeur de classe, mais ce n'est qu'une convention.

Ce ne sont là que deux des attributs possibles que vous pouvez avoir. Certains attributs ne sont utilisés que pour une seule balise. Ils sont très spécialisés.

D'autres attributs peuvent être utilisés de manière plus générale. Vous venez de voir `id` et `class`, mais nous en avons d'autres aussi, comme `style` qui peut être utilisé pour insérer des règles CSS en ligne sur un élément.

### **Insensible à la casse**

HTML est insensible à la casse. Les balises peuvent être écrites en majuscules ou en minuscules. Dans les premiers jours, les majuscules étaient la norme. Aujourd'hui, les minuscules sont la norme. C'est une convention.

Vous écrivez généralement comme ceci :

```html
<p>Un paragraphe de texte</p>
```

pas comme ceci :

```html
<P>Un paragraphe de texte</P>
```

### **Espace blanc**

Assez important. En HTML, même si vous ajoutez plusieurs espaces blancs dans une ligne, ils sont réduits par le moteur CSS du navigateur.

Par exemple, le rendu de ce paragraphe :

```html
<p>Un paragraphe de texte</p>
```

est le même que celui-ci :

```html
<p>        Un paragraphe de texte</p>
```

et le même que celui-ci :

```html
<p>Un paragraphe

de
           texte          </p>
```

> _En utilisant la [propriété CSS white-space](https://developer.mozilla.org/fr/docs/Web/CSS/white-space), vous pouvez changer le comportement des choses. Vous pouvez trouver plus d'informations sur la façon dont CSS traite les espaces blancs dans la [Spécification CSS](https://www.w3.org/TR/CSS2/text.html#white-space-model)_

Je privilégie généralement

```html
<p>Un paragraphe de texte</p>
```

ou

```html
<p>
    Un paragraphe de texte
</p>
```

Les balises imbriquées doivent être indentées avec 2 ou 4 caractères, selon votre préférence :

```html
<body>
    <p>
        Un paragraphe de texte
    </p>
    <ul>
        <li>Un élément de liste</li>
    </ul>
</body>
```

Note : cette fonctionnalité "l'espace blanc n'est pas pertinent" signifie que si vous souhaitez ajouter un espace supplémentaire, cela peut vous rendre assez fou. Je vous suggère d'utiliser CSS pour créer plus d'espace lorsque cela est nécessaire.

Note : dans des cas particuliers, vous pouvez utiliser l'entité HTML `&nbsp;` (un acronyme qui signifie _espace insécable_) - plus sur les entités HTML plus tard. Je pense que cela ne devrait pas être abusé. CSS est toujours préféré pour modifier la présentation visuelle.

## L'EN-TÊTE DU DOCUMENT

La balise `head` contient des balises spéciales qui définissent les propriétés du document.

Elle est toujours écrite avant la balise `body`, juste après la balise d'ouverture `html` :

```html
<!DOCTYPE html>
<html>
    <head>
        ...
    </head>
    ...
</html>
```

Nous n'utilisons jamais d'attributs sur cette balise. Et nous n'écrivons pas de contenu dedans.

C'est juste un conteneur pour d'autres balises. À l'intérieur, nous pouvons avoir une grande variété de balises, selon ce que vous devez faire :

* `title`
* `script`
* `noscript`
* `link`
* `style`
* `base`
* `meta`

### **La balise `title`**

La balise `title` détermine le titre de la page. Le titre est affiché dans le navigateur, et il est particulièrement important car c'est l'un des facteurs clés pour le référencement (SEO).

### **La balise `script`**

Cette balise est utilisée pour ajouter du JavaScript dans la page.

Vous pouvez l'inclure en ligne, en utilisant une balise d'ouverture, le code JavaScript et ensuite la balise de fermeture :

```html
<script>
..du JS
</script>
```

Ou vous pouvez charger un fichier JavaScript externe en utilisant l'attribut `src` :

```html
<script src="fichier.js"></script>
```

L'attribut `type` est par défaut défini sur `text/javascript`, donc il est complètement optionnel.

Il y a quelque chose de très important à savoir sur cette balise.

Parfois, cette balise est utilisée en bas de la page, juste avant la balise de fermeture `</body>`. Pourquoi ? Pour des raisons de performance.

Le chargement des scripts bloque par défaut le rendu de la page jusqu'à ce que le script soit analysé et chargé.

En le plaçant en bas de la page, le script est chargé et exécuté après que toute la page est déjà analysée et chargée, offrant une meilleure expérience à l'utilisateur par rapport à le garder dans la balise `head`.

Mon avis est que cela est maintenant une mauvaise pratique. Laissez `script` vivre dans la balise `head`.

Dans le JavaScript moderne, nous avons une alternative plus performante que de garder le script en bas de la page -- l'attribut `defer`. Voici un exemple qui charge un fichier `fichier.js`, relatif à l'URL actuelle :

```html
<script defer src="fichier.js"></script>
```

C'est le scénario qui déclenche le chemin le plus rapide vers une page à chargement rapide, et un JavaScript à chargement rapide.

Note : l'attribut `async` est similaire, mais à mon avis une option pire que `defer`. Je décris pourquoi, plus en détail, sur la page [https://flaviocopes.com/javascript-async-defer/](https://flaviocopes.com/javascript-async-defer/)

### **La balise `noscript`**

Cette balise est utilisée pour détecter lorsque les scripts sont désactivés dans le navigateur.

Note : les utilisateurs peuvent choisir de désactiver les scripts JavaScript dans les paramètres du navigateur. Ou le navigateur peut ne pas les supporter par défaut.

Elle est utilisée différemment selon qu'elle est placée dans l'en-tête du document ou dans le corps du document.

Nous parlons de l'en-tête du document maintenant, alors introduisons d'abord cette utilisation.

Dans ce cas, la balise `noscript` ne peut contenir que d'autres balises :

* balises `link`
* balises `style`
* balises `meta`

pour modifier les ressources servies par la page, ou les informations `meta`, si les scripts sont désactivés.

Dans cet exemple, je définis un élément avec la classe `no-script-alert` pour s'afficher si les scripts sont désactivés, car il était `display: none` par défaut :

```html
<!DOCTYPE html>
<html>
    <head>
        ...
        <noscript>
            <style>
                .no-script-alert {
                    display: block;
                }
            </style>
        </noscript>

        ...
    </head>
    ...
</html>
```

Résolvons l'autre cas : si elle est placée dans le corps, elle peut contenir du contenu, comme des paragraphes et d'autres balises, qui sont rendus dans l'interface utilisateur.

### **La balise `link`**

La balise `link` est utilisée pour établir des relations entre un document et d'autres ressources.

Elle est principalement utilisée pour lier un fichier CSS externe à charger.

Cet élément n'a pas de balise de fermeture.

Utilisation :

```html
<!DOCTYPE html>
<html>
    <head>
        ...
        <link href="fichier.css" rel="stylesheet">
        ...
    </head>
    ...
</html>
```

L'attribut `media` permet le chargement de différentes feuilles de style en fonction des capacités de l'appareil :

```html
<link href="fichier.css" media="screen" rel="stylesheet">
<link href="print.css" media="print" rel="stylesheet">
```

Nous pouvons également lier des ressources autres que des feuilles de style.

Par exemple, nous pouvons associer un flux RSS en utilisant

```html
<link rel="alternate" type="application/rss+xml" href="/index.xml">
```

Ou nous pouvons associer un favicon en utilisant :

```html
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">

<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">

<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16x16.png">
```

Cette balise _était_ également utilisée pour le contenu multi-pages, pour indiquer la page précédente et suivante en utilisant `rel="prev"` et `rel="next"`. Principalement pour Google. En 2019, [Google a annoncé qu'il n'utilisait plus cette balise](https://twitter.com/googlewmc/status/1108726443251519489) car il peut trouver la structure correcte de la page sans elle.

### **La balise `style`**

Cette balise peut être utilisée pour ajouter des styles dans le document, plutôt que de charger une feuille de style externe.

Utilisation :

```html
<style>
.du-css {}
</style>
```

Comme avec la balise `link`, vous pouvez utiliser l'attribut `media` pour utiliser ce CSS uniquement sur le support spécifié :

```html
<style media="print">
.du-css {}
</style>
```

### **La balise `base`**

Cette balise est utilisée pour définir une URL de base pour toutes les URL relatives contenues dans la page.

```html
<!DOCTYPE html>
<html>
    <head>
        ...
        <base href="https://flaviocopes.com/">
        ...
    </head>
    ...
</html>
```

### **La balise `meta`**

Les balises meta effectuent une variété de tâches et elles sont très, très importantes.

Surtout pour le SEO.

Les éléments `meta` n'ont que la balise de début.

La plus basique est la balise meta `description` :

```html
<meta name="description" content="Une belle page">
```

Cela _peut_ être utilisé par Google pour générer la description de la page dans ses pages de résultats, s'il trouve qu'elle décrit mieux la page que le contenu de la page (ne me demandez pas comment).

La balise meta `charset` est utilisée pour définir l'encodage des caractères de la page. `utf-8` dans la plupart des cas :

```html
<meta charset="utf-8">
```

La balise meta `robots` indique aux robots des moteurs de recherche s'ils doivent indexer une page ou non :

```html
<meta name="robots" content="noindex">
```

Ou s'ils doivent suivre les liens ou non :

```html
<meta name="robots" content="nofollow">
```

Vous pouvez définir nofollow sur des liens individuels, aussi. Voici comment vous pouvez définir `nofollow` globalement.

Vous pouvez les combiner :

```html
<meta name="robots" content="noindex, nofollow">
```

Le comportement par défaut est `index, follow`.

Vous pouvez utiliser d'autres propriétés, y compris `nosnippet`, `noarchive`, `noimageindex` et plus encore.

Vous pouvez aussi simplement dire à Google au lieu de cibler _tous_ les moteurs de recherche :

```html
<meta name="googlebot" content="noindex, nofollow">
```

Et d'autres moteurs de recherche peuvent avoir leur propre balise meta, aussi.

À ce propos, nous pouvons dire à Google de désactiver certaines fonctionnalités. Cela empêche la fonctionnalité de traduction dans les résultats du moteur de recherche :

```html
<meta name="google" content="notranslate">
```

La balise meta `viewport` est utilisée pour dire au navigateur de définir la largeur de la page en fonction de la largeur de l'appareil.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

[En savoir plus sur cette balise](https://developer.mozilla.org/fr/docs/Mozilla/Mobile/Viewport_meta_tag).

Une autre balise meta plutôt populaire est `http-equiv="refresh"`. Cette ligne indique au navigateur d'attendre 3 secondes, puis de rediriger vers cette autre page :

```html
<meta http-equiv="refresh" content="3;url=http://flaviocopes.com/another-page">
```

Utiliser 0 au lieu de 3 redirigera dès que possible.

Ce n'est pas une référence complète ; d'autres balises meta moins utilisées existent.

Après cette introduction à l'en-tête du document, nous pouvons commencer à plonger dans le corps du document.

## LE CORPS DU DOCUMENT

Après la balise de fermeture de l'en-tête, nous ne pouvons avoir qu'une seule chose dans un document HTML : l'élément `body`.

```html
<!DOCTYPE html>
<html>
    <head>
        ...
    </head>
    <body>
        ...
    </body>
</html>
```

Tout comme les balises `head` et `html`, nous ne pouvons avoir qu'une seule balise `body` dans une page.

À l'intérieur de la balise `body`, nous avons toutes les balises qui définissent le contenu de la page.

Techniquement, les balises de début et de fin sont facultatives. Mais je considère qu'il est bon de les ajouter. Juste pour la clarté.

Dans les prochains chapitres, nous définirons la variété de balises que vous pouvez utiliser à l'intérieur du corps de la page.

Mais avant, nous devons introduire une différence entre les éléments de bloc et les éléments en ligne.

## **Éléments de bloc vs éléments en ligne**

Les éléments visuels, ceux définis dans le corps de la page, peuvent être généralement classés en 2 catégories :

* éléments de bloc (`p`, `div`, éléments de titre, listes et éléments de liste, ...)
* éléments en ligne (`a`, `span`, `img`, ...)

Quelle est la différence ?

Les éléments de bloc, lorsqu'ils sont positionnés dans la page, ne permettent pas d'autres éléments à côté d'eux. À gauche, ou à droite.

Les éléments en ligne, en revanche, peuvent se situer à côté d'autres éléments en ligne.

La différence réside également dans les propriétés visuelles que nous pouvons modifier en utilisant CSS. Nous pouvons altérer la largeur/hauteur, la marge, le remplissage et la bordure des éléments de bloc. Nous ne pouvons pas faire cela pour les éléments en ligne.

Notez que l'utilisation de CSS nous permet de changer le comportement par défaut de chaque élément, en définissant une balise `p` pour qu'elle soit en ligne, par exemple, ou une balise `span` pour qu'elle soit un élément de bloc.

Une autre différence est que les éléments en ligne peuvent être contenus dans des éléments de bloc. L'inverse n'est pas vrai.

Certains éléments de bloc peuvent contenir d'autres éléments de bloc, mais cela dépend. La balise `p`, par exemple, ne permet pas une telle option.

# **BALISES QUI INTERAGISSENT AVEC LE TEXTE**

## **La balise `p`**

Cette balise définit un paragraphe de texte.

```html
<p>Du texte</p>
```

C'est un élément de bloc.

À l'intérieur, nous pouvons ajouter n'importe quel élément en ligne que nous aimons, comme `span` ou `a`.

Nous ne pouvons pas ajouter d'éléments de bloc.

Nous ne pouvons pas imbriquer un élément `p` dans un autre.

Par défaut, les navigateurs stylisent un paragraphe avec une marge en haut et en bas. `16px` dans Chrome, mais la valeur exacte peut varier entre les navigateurs.

Cela provoque l'espacement de deux paragraphes consécutifs, reproduisant ce que nous considérons comme un "paragraphe" dans le texte imprimé.

## **La balise `span`**

Il s'agit d'une balise en ligne qui peut être utilisée pour créer une section dans un paragraphe qui peut être ciblée à l'aide de CSS :

```html
<p>Une partie du texte <span>et ici une autre partie</span></p>
```

## **La balise `br`**

Cette balise représente un saut de ligne. C'est un élément en ligne et ne nécessite pas de balise de fermeture.

Nous l'utilisons pour créer une nouvelle ligne à l'intérieur d'une balise `p`, sans créer un nouveau paragraphe.

Et comparé à la création d'un nouveau paragraphe, il n'ajoute pas d'espacement supplémentaire.

```html
<p>Du texte<br>Une nouvelle ligne</p>
```

## **Les balises de titre**

HTML nous fournit 6 balises de titre. De la plus importante à la moins importante, nous avons `h1`, `h2`, `h3`, `h4`, `h5`, `h6`.

Typiquement, une page aura un élément `h1`, qui est le titre de la page. Ensuite, vous pouvez avoir un ou plusieurs éléments `h2` selon le contenu de la page.

Les titres, en particulier l'organisation des titres, sont également essentiels pour le SEO, et les moteurs de recherche les utilisent de diverses manières.

Le navigateur, par défaut, rendra la balise `h1` plus grande et réduira la taille des éléments à mesure que le nombre près de `h` augmente :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-11-at-19.46.57.png)

Tous les titres sont des éléments de bloc. Ils ne peuvent pas contenir d'autres éléments, juste du texte.

## **La balise `strong`**

Cette balise est utilisée pour marquer le texte à l'intérieur comme _important_. Cela est assez important, ce n'est pas un indice visuel, mais un indice sémantique. Selon le support utilisé, son interprétation variera.

Les navigateurs rendent par défaut le texte dans cette balise en **gras**.

## **La balise `em`**

Cette balise est utilisée pour marquer le texte à l'intérieur comme _emphasé_. Comme avec `strong`, ce n'est pas un indice visuel mais un indice sémantique.

Les navigateurs rendent par défaut le texte dans cette balise en *italique*.

## **Citations**

La balise HTML `blockquote` est utile pour insérer des citations dans le texte.

Les navigateurs appliquent par défaut une marge à l'élément `blockquote`. Chrome applique une marge de 40px à gauche et à droite, et une marge de 10px en haut et en bas.

La balise HTML `q` est utilisée pour les citations en ligne.

## **Ligne horizontale**

Pas vraiment basé sur le texte, mais la balise `hr` est souvent utilisée à l'intérieur d'une page. Elle signifie `règle horizontale`, et elle ajoute une ligne horizontale dans la page.

Utile pour séparer les sections dans la page.

## **Blocs de code**

La balise `code` est particulièrement utile pour afficher du code, car les navigateurs lui donnent une police à espacement fixe.

C'est généralement la seule chose que font les navigateurs. Voici le CSS appliqué par Chrome :

```css
code {
    font-family: monospace;
}
```

Cette balise est généralement enveloppée dans une balise `pre`, car l'élément `code` ignore les espaces blancs et les sauts de ligne. Comme la balise `p`.

Chrome donne à `pre` ce style par défaut :

```css
pre {
    display: block;
    font-family: monospace;
    white-space: pre;
    margin: 1em 0px;
}
```

ce qui empêche l'effondrement des espaces blancs et en fait un élément de bloc.

## **Listes**

Nous avons 3 types de listes :

* listes non ordonnées
* listes ordonnées
* listes de définition

Les listes non ordonnées sont créées en utilisant la balise `ul`. Chaque élément de la liste est créé avec la balise `li` :

```html
<ul>
    <li>Premier</li>
    <li>Deuxième</li>
</ul>
```

Les listes ordonnées sont similaires, mais créées avec la balise `ol` :

```html
<ol>
    <li>Premier</li>
    <li>Deuxième</li>
</ol>
```

La différence entre les deux est que les listes ordonnées ont un numéro avant chaque élément :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-12-at-09.35.05.png)

Les listes de définition sont un peu différentes. Vous avez un terme, et sa définition :

```html
<dl>
    <dt>Flavio</dt>
    <dd>Le prénom</dd>
    <dt>Copes</dt>
    <dd>Le nom</dd>
</dl>
```

Voici comment les navigateurs les rendent généralement :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-12-at-09.45.21.png)

Je dois dire que vous les voyez rarement dans la nature, certainement pas autant que `ul` et `ol`, mais parfois elles peuvent être utiles.

## **Autres balises de texte**

Il existe un certain nombre de balises à des fins de présentation :

* la balise `mark`
* la balise `ins`
* la balise `del`
* la balise `sup`
* la balise `sub`
* la balise `small`
* la balise `i`
* la balise `b`

Voici un exemple du rendu visuel qui est appliqué par défaut par les navigateurs :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-12-at-08.43.55.png)

Vous pourriez vous demander, comment `b` est différent de `strong` ? Et comment `i` est différent de `em` ?

La différence réside dans la signification sémantique. Alors que `b` et `i` sont un indice direct pour le navigateur de rendre un morceau de texte en gras ou en italique, `strong` et `em` donnent au texte une signification spéciale, et c'est au navigateur de donner le style. Ce qui se trouve être exactement le même que `b` et `i`, par défaut. Bien que vous puissiez changer cela en utilisant CSS.

Il existe un certain nombre d'autres balises, moins utilisées, liées au texte. Je viens de mentionner celles que je vois le plus utilisées.

# LIENS

Les liens sont définis en utilisant la balise `a`. La destination du lien est définie via son attribut `href`.

Exemple :

```html
<a href="https://flaviocopes.com">cliquez ici</a>
```

Entre la balise d'ouverture et la balise de fermeture, nous avons le texte du lien.

L'exemple ci-dessus est une URL absolue. Les liens fonctionnent également avec des URL relatives :

```html
<a href="/test">cliquez ici</a>
```

Dans ce cas, lorsque vous cliquez sur le lien, l'utilisateur est redirigé vers l'URL `/test` sur l'origine actuelle.

Faites attention au caractère `/`. S'il est omis, au lieu de commencer à partir de l'origine, le navigateur ajoutera simplement la chaîne `test` à l'URL actuelle.

Exemple, je suis sur la page `https://flaviocopes.com/axios/` et j'ai ces liens :

* `/test` une fois cliqué m'amène à `https://flaviocopes.com/test`
* `test` une fois cliqué m'amène à `https://flaviocopes.com/axios/test`

Les balises de lien peuvent inclure d'autres choses à l'intérieur, pas seulement du texte. Par exemple, des images :

```html
<a href="https://flaviocopes.com">
    <img src="test.jpg">
</a>
```

ou tout autre élément, sauf d'autres balises `<a>`.

Si vous souhaitez ouvrir le lien dans un nouvel onglet, vous pouvez utiliser l'attribut `target` :

```html
<a href="https://flaviocopes.com" target="_blank">ouvrir dans un nouvel onglet</a>
```

# **BALISES CONTENANT ET STRUCTURE DE PAGE HTML**

## **Balises conteneur**

HTML fournit un ensemble de balises conteneur. Ces balises peuvent contenir un ensemble non spécifié d'autres balises.

Nous avons :

* `article`
* `section`
* `div`

et il peut être déroutant de comprendre la différence entre elles.

Voyons quand utiliser chacune d'entre elles.

### **`article`**

La balise article identifie une _chose_ qui peut être indépendante des autres _choses_ dans une page.

Par exemple, une liste de billets de blog dans la page d'accueil.

Ou une liste de liens.

```html
<div>
    <article>
        <h2>Un billet de blog</h2>
        <a ...>Lire la suite</a>
    </article>
    <article>
        <h2>Un autre billet de blog</h2>
        <a ...>Lire la suite</a>
    </article>
</div>
```

Nous ne sommes pas limités aux listes : un article peut être l'élément principal dans une page.

```html
<article>
    <h2>Un billet de blog</h2>
    <p>Voici le contenu...</p>
</article>
```

À l'intérieur d'une balise `article`, nous devrions avoir un titre (`h1`-`h6`) et

### **`section`**

Représente une section d'un document. Chaque section a une balise de titre (`h1`-`h6`), puis le _corps_ de la section.

Exemple :

```html
<section>
    <h2>Une section de la page</h2>
    <p>...</p>
    <img ...>
</section>
```

C'est utile pour diviser un long article en différentes **sections**.

Ne devrait pas être utilisé comme un élément conteneur générique. `div` est fait pour cela.

### **`div`**

`div` est l'élément conteneur générique :

```html
<div>
    ...
</div>
```

Vous ajoutez souvent un attribut `class` ou `id` à cet élément, pour permettre de le styliser en utilisant CSS.

Nous utilisons `div` à tout endroit où nous avons besoin d'un conteneur mais où les balises existantes ne sont pas adaptées.

## **Balises liées à la page**

### **`nav`**

Cette balise est utilisée pour créer le balisage qui définit la navigation de la page. À l'intérieur, nous ajoutons généralement une liste `ul` ou `ol` :

```html
<nav>
    <ol>
        <li><a href="/">Accueil</a></li>
        <li><a href="/blog">Blog</a></li>
    </ol>
</nav>
```

### **`aside`**

La balise `aside` est utilisée pour ajouter un morceau de contenu qui est lié au contenu principal.

Une boîte où ajouter une citation, par exemple. Ou une barre latérale.

Exemple :

```html
<div>
  <p>du texte..</p>
  <aside>
    <p>Une citation..</p>
  </aside>
  <p>autre texte...</p>
</div>
```

Utiliser `aside` est un signal que les choses qu'il contient ne font pas partie du flux régulier de la section dans laquelle il se trouve.

### **`header`**

La balise `header` représente une partie de la page qui est l'introduction. Elle peut contenir, par exemple, un ou plusieurs titres (`h1`-`h6`), le slogan de l'article, une image.

```html
<article>
  <header>
      <h1>Titre de l'article</h1>
  </header>
  ...
</div>
```

### **`main`**

La balise `main` représente la partie principale d'une page :

```html
<body>
  ....
  <main>
    <p>....</p>
  </main>
</body>
```

### **`footer`**

La balise `footer` est utilisée pour déterminer le pied de page d'un article, ou le pied de page de la page :

```html
<article>
 ....
  <footer>
    <p>Notes de pied de page..</p>
  </footer>
</div>
```

# **FORMULAIRES**

Les formulaires sont le moyen par lequel vous pouvez interagir avec une page, ou une application, construite avec des technologies Web.

Vous avez un ensemble de contrôles, et lorsque vous soumettez le formulaire, soit avec un clic sur un bouton "soumettre" ou par programmation, le navigateur enverra les données au serveur.

Par défaut, cette transmission de données provoque le rechargement de la page après l'envoi des données, mais en utilisant JavaScript, vous pouvez altérer ce comportement (je ne vais pas expliquer comment dans ce livre).

Un formulaire est créé en utilisant la balise `form` :

```html
<form>
    ...
</form>
```

Par défaut, les formulaires sont soumis en utilisant la méthode HTTP GET. Ce qui a ses inconvénients, et généralement vous voulez utiliser POST.

Vous pouvez définir le formulaire pour utiliser POST lorsqu'il est soumis en utilisant l'attribut `method` :

```html
<form method="POST">
    ...
</form>
```

Le formulaire est soumis, soit en utilisant GET ou POST, à la même URL où il réside.

Donc si le formulaire est dans la page `https://flaviocopes.com/contacts`, appuyer sur le bouton "soumettre" fera une requête à cette même URL.

Ce qui pourrait ne rien faire.

Vous avez besoin de quelque chose côté serveur pour gérer la requête, et généralement vous "écoutez" ces événements de soumission de formulaire sur une URL dédiée.

Vous pouvez spécifier l'URL via le paramètre `action` :

```html
<form action="/new-contact" method="POST">
    ...
</form>
```

Cela fera que le navigateur soumet les données du formulaire en utilisant POST à l'URL `/new-contact` sur la même origine.

Si l'origine (protocole + domaine + port) est `https://flaviocopes.com` (le port 80 est celui par défaut), cela signifie que les données du formulaire seront envoyées à `https://flaviocopes.com/new-contact`.

J'ai parlé de données. Quelles données ?

Les données sont fournies par les utilisateurs via l'ensemble de contrôles disponibles sur la plateforme Web :

* zones de saisie (texte sur une seule ligne)
* zones de texte (texte multiligne)
* cases de sélection (choisir une option dans un menu déroulant)
* boutons radio (choisir une option dans une liste toujours visible)
* cases à cocher (choisir zéro, une ou plusieurs options)
* téléchargements de fichiers
* et plus encore !

Introduisons chacun d'entre eux dans l'aperçu des champs de formulaire suivant.

## **La balise `input`**

Le champ `input` est l'un des éléments de formulaire les plus largement utilisés. C'est aussi un élément très polyvalent, et il peut changer complètement de comportement en fonction de l'attribut `type`.

Le comportement par défaut est d'être un contrôle de saisie de texte sur une seule ligne :

```html
<input>
```

Équivalent à utiliser :

```html
<input type="text">
```

Comme pour tous les autres champs qui suivent, vous devez donner un nom au champ afin que son contenu soit envoyé au serveur lorsque le formulaire est soumis :

```html
<input type="text" name="username">
```

L'attribut `placeholder` est utilisé pour afficher un texte, en gris clair, lorsque le champ est vide. Utile pour ajouter un indice à l'utilisateur sur ce qu'il doit taper :

```html
<input type="text" name="username" placeholder="Votre nom d'utilisateur">
```

### **Email**

L'utilisation de `type="email"` validera côté client (dans le navigateur) un email pour sa correction (correction sémantique, sans garantir que l'adresse email existe) avant la soumission.

```html
<input type="email" name="email" placeholder="Votre email">
```

### **Mot de passe**

L'utilisation de `type="password"` fera apparaître chaque touche saisie comme un astérisque (*) ou un point, utile pour les champs qui hébergent un mot de passe.

```html
<input type="password" name="password" placeholder="Votre mot de passe">
```

### **Nombres**

Vous pouvez avoir un élément de saisie qui n'accepte que des nombres :

```html
<input type="number" name="age" placeholder="Votre âge">
```

Vous pouvez spécifier une valeur minimale et maximale acceptée :

```html
<input type="number" name="age" placeholder="Votre âge" min="18" max="110">
```

L'attribut `step` aide à identifier les étapes entre différentes valeurs. Par exemple, cela accepte une valeur entre 10 et 50, par étapes de 5 :

```html
<input type="number" name="a-number"  min="10" max="50" step="5">
```

### **Champ caché**

Les champs peuvent être cachés de l'utilisateur. Ils seront toujours envoyés au serveur lors de la soumission du formulaire :

```html
<input type="hidden" name="some-hidden-field" value="some-value">
```

Cela est couramment utilisé pour stocker des valeurs comme un jeton CSRF, utilisé pour la sécurité et l'identification de l'utilisateur, ou même pour détecter les robots envoyant du spam, en utilisant des techniques spéciales.

Il peut également être utilisé simplement pour identifier un formulaire et son action.

### **Définir une valeur par défaut**

Tous ces champs acceptent une valeur prédéfinie. Si l'utilisateur ne la modifie pas, ce sera la valeur envoyée au serveur :

```html
<input type="number" name="age" value="18">
```

Si vous définissez un placeholder, cette valeur apparaîtra si l'utilisateur efface la valeur du champ de saisie :

```html
<input type="number" name="age" placeholder="Votre âge" value="18">
```

## **Soumission du formulaire**

Le champ `type="submit"` est un bouton qui, une fois pressé par l'utilisateur, soumet le formulaire :

```html
<input type="submit">
```

L'attribut `value` définit le texte sur le bouton, qui, s'il est manquant, affiche le texte "Submit" :

```html
<input type="submit" value="Cliquez ici">
```

## **Validation du formulaire**

Les navigateurs fournissent une fonctionnalité de validation côté client pour les formulaires.

Vous pouvez définir des champs comme obligatoires, en vous assurant qu'ils sont remplis, et imposer un format spécifique pour la saisie de chaque champ.

Voyons les deux options.

### **Définir les champs comme obligatoires**

L'attribut `required` vous aide avec la validation. Si le champ n'est pas défini, la validation côté client échoue et le navigateur ne soumet pas le formulaire :

```html
<input type="text" name="username" required>
```

### **Imposer un format spécifique**

J'ai décrit le champ `type="email"` ci-dessus. Il valide automatiquement l'adresse email selon un format défini dans la spécification.

Dans le champ `type="number"`, j'ai mentionné les attributs `min` et `max` pour limiter les valeurs saisies à un intervalle.

Vous pouvez faire plus.

Vous pouvez imposer un format spécifique à n'importe quel champ.

L'attribut `pattern` vous donne la possibilité de définir une expression régulière pour valider la valeur.

Je vous recommande de lire mon Guide des Expressions Régulières à l'adresse [flaviocopes.com/javascript-regular-expressions/](https://flaviocopes.com/javascript-regular-expressions/).

pattern="[https://.*](https://.%2A/)"

```html
<input type="text" name="username" pattern="[a-zA-Z]{8}">
```

## **Autres champs**

### **Téléchargements de fichiers**

Vous pouvez charger des fichiers depuis votre ordinateur local et les envoyer au serveur en utilisant un élément d'entrée `type="file"` :

```html
<input type="file" name="secret-documents">
```

Vous pouvez attacher plusieurs fichiers :

```html
<input type="file" name="secret-documents" multiple>
```

Vous pouvez spécifier un ou plusieurs types de fichiers autorisés en utilisant l'attribut `accept`. Cela accepte les images :

```html
<input type="file" name="secret-documents" accept="image/*">
```

Vous pouvez utiliser un type MIME spécifique, comme `application/json` ou définir une extension de fichier comme `.pdf`. Ou définir plusieurs extensions de fichiers, comme ceci :

```html
<input type="file" name="secret-documents" accept=".jpg, .jpeg, .png">
```

### **Boutons**

Les champs d'entrée `type="button"` peuvent être utilisés pour ajouter des boutons supplémentaires au formulaire, qui ne sont pas des boutons de soumission :

```html
<input type="button" value="Cliquez ici">
```

Ils sont utilisés pour faire quelque chose de manière programmatique, en utilisant JavaScript.

Il existe un champ spécial rendu comme un bouton, dont l'action spéciale est d'effacer l'ensemble du formulaire et de ramener l'état des champs à l'état initial :

```html
<input type="reset">
```

### **Boutons radio**

Les boutons radio sont utilisés pour créer un ensemble de choix, dont un est pressé et tous les autres sont désactivés.

Le nom vient des anciennes radios de voiture qui avaient ce type d'interface.

Vous définissez un ensemble d'entrées `type="radio"`, toutes avec le même attribut `name`, et un attribut `value` différent :

```html
<input type="radio" name="color" value="yellow">
<input type="radio" name="color" value="red">
<input type="radio" name="color" value="blue">
```

Une fois le formulaire soumis, la propriété de données `color` aura une seule valeur.

Il y a toujours un élément coché. Le premier élément est celui coché par défaut.

Vous pouvez définir la valeur qui est présélectionnée en utilisant l'attribut `checked`. Vous ne pouvez l'utiliser qu'une seule fois par groupe d'entrées radio.

### **Cases à cocher**

Similaires aux boutons radio, mais ils permettent de choisir plusieurs valeurs, ou aucune.

Vous définissez un ensemble d'entrées `type="checkbox"`, toutes avec le même attribut `name`, et un attribut `value` différent :

```html
<input type="checkbox" name="color" value="yellow">
<input type="checkbox" name="color" value="red">
<input type="checkbox" name="color" value="blue">
```

Toutes ces cases à cocher seront décochées par défaut. Utilisez l'attribut `checked` pour les activer au chargement de la page.

Puisque ce champ d'entrée permet plusieurs valeurs, lors de la soumission du formulaire, la ou les valeurs seront envoyées au serveur sous forme de tableau.

### **Date et heure**

Nous avons quelques types d'entrée pour accepter des valeurs de date.

Le champ d'entrée `type="date"` permet à l'utilisateur de saisir une date et affiche un sélecteur de date si nécessaire :

```html
<input type="date" name="birthday">
```

Le champ d'entrée `type="time"` permet à l'utilisateur de saisir une heure et affiche un sélecteur d'heure si nécessaire :

```html
<input type="time" name="time-to-pickup">
```

Le champ d'entrée `type="month"` permet à l'utilisateur de saisir un mois et une année :

```html
<input type="month" name="choose-release-month">
```

Le champ d'entrée `type="week"` permet à l'utilisateur de saisir une semaine et une année :

```html
<input type="week" name="choose-week">
```

Tous ces champs permettent de limiter la plage et le pas entre chaque valeur. Je recommande de vérifier MDN pour les petits détails sur leur utilisation.

Le champ `type="datetime-local"` vous permet de choisir une date et une heure.

```html
<input type="datetime-local" name="date-and-time">
```

Voici une page pour les tester tous : [https://codepen.io/flaviocopes/pen/ZdWQPm](https://codepen.io/flaviocopes/pen/ZdWQPm)

### **Sélecteur de couleur**

Vous pouvez laisser les utilisateurs choisir une couleur en utilisant l'élément `type="color"` :

```html
<input type="color" name="car-color">
```

Vous définissez une valeur par défaut en utilisant l'attribut `value` :

```html
<input type="color" name="car-color" value="#000000">
```

Le navigateur se chargera d'afficher un sélecteur de couleur à l'utilisateur.

### **Plage**

Cet élément d'entrée affiche un élément curseur. Les gens peuvent l'utiliser pour passer d'une valeur de départ à une valeur de fin :

```html
<input type="range" name="age" min="0" max="100" value="30">
```

Vous pouvez fournir un pas optionnel :

```html
<input type="range" name="age" min="0" max="100" value="30" step="10">
```

### **Téléphone**

Le champ d'entrée `type="tel"` est utilisé pour saisir un numéro de téléphone :

```html
<input type="tel" name="telephone-number">
```

Le principal argument de vente pour utiliser `tel` plutôt que `text` est sur mobile, où l'appareil peut choisir d'afficher un clavier numérique.

Spécifiez un attribut `pattern` pour une validation supplémentaire :

```html
<input type="tel" pattern="[0-9]{3}-[0-9]{8}" name="telephone-number">
```

### **URL**

Le champ `type="url"` est utilisé pour saisir une URL.

```html
<input type="url" name="website">
```

Vous pouvez le valider en utilisant l'attribut `pattern` :

```html
<input type="url" name="website"  pattern="https://.*">
```

## **La balise `textarea`**

L'élément `textarea` permet aux utilisateurs de saisir du texte sur plusieurs lignes. Comparé à `input`, il nécessite une balise de fermeture :

```html
<textarea></textarea>
```

Vous pouvez définir les dimensions en utilisant CSS, mais aussi en utilisant les attributs `rows` et `cols` :

```html
<textarea rows="20" cols="10"></textarea>
```

Comme avec les autres balises de formulaire, l'attribut `name` détermine le nom dans les données envoyées au serveur :

```html
<textarea name="article"></textarea>
```

## **La balise `select`**

Cette balise est utilisée pour créer un menu déroulant.

L'utilisateur peut choisir l'une des options disponibles.

Chaque option est créée en utilisant la balise `option`. Vous ajoutez un nom à la sélection, et une valeur à chaque option :

```html
<select name="color">
    <option value="red">Rouge</option>
    <option value="yellow">Jaune</option>
</select>
```

Vous pouvez définir une option désactivée :

```html
<select name="color">
    <option value="red" disabled>Rouge</option>
    <option value="yellow">Jaune</option>
</select>
```

Vous pouvez avoir une option vide :

```html
<select name="color">
    <option value="">Aucun</option>
    <option value="red">Rouge</option>
    <option value="yellow">Jaune</option>
</select>
```

Les options peuvent être regroupées en utilisant la balise `optgroup`. Chaque groupe d'options a un attribut `label` :

```html
<select name="color">
    <optgroup label="Primaire">
        <option value="red">Rouge</option>
        <option value="yellow">Jaune</option>
        <option value="blue">Bleu</option>
    </optgroup>
    <optgroup label="Autres">
        <option value="green">Vert</option>
        <option value="pink">Rose</option>
    </optgroup>
</select>
```

# **TABLEAUX**

Dans les premiers jours du web, les tableaux étaient une partie très importante de la construction des mises en page.

Plus tard, ils ont été remplacés par CSS et ses capacités de mise en page, et aujourd'hui nous avons des outils puissants comme CSS Flexbox et CSS Grid pour construire des mises en page. Les tableaux sont maintenant utilisés juste pour, devinez quoi, construire des tableaux !

### **La balise `table`**

Vous définissez un tableau en utilisant la balise `table` :

```html
<table>

</table>
```

À l'intérieur du tableau, nous définirons les données. Nous raisonnons en termes de lignes, ce qui signifie que nous ajoutons des lignes dans un tableau (pas des colonnes). Nous définirons les colonnes à l'intérieur d'une ligne.

### **Lignes**

Une ligne est ajoutée en utilisant la balise `tr`, et c'est la seule chose que nous pouvons ajouter dans un élément `table` :

```html
<table>
  <tr></tr>
  <tr></tr>
  <tr></tr>
</table>
```

C'est un tableau avec 3 lignes.

La première ligne _peut_ jouer le rôle de l'en-tête.

### **En-têtes de colonne**

L'en-tête du tableau contient le nom d'une colonne, généralement en police grasse.

Pensez à un document Excel / Google Sheets. L'en-tête supérieur `A-B-C-D...`.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.18.17.png)

Nous définissons l'en-tête en utilisant la balise `th` :

```html
<table>
  <tr>
    <th>Colonne 1</th>
    <th>Colonne 2</th>
    <th>Colonne 3</th>
  </tr>
  <tr></tr>
  <tr></tr>
</table>
```

### **Le contenu du tableau**

Le contenu du tableau est défini en utilisant des balises `td`, à l'intérieur des autres éléments `tr` :

```html
<table>
  <tr>
    <th>Colonne 1</th>
    <th>Colonne 2</th>
    <th>Colonne 3</th>
  </tr>
  <tr>
    <td>Ligne 1 Colonne 1</td>
    <td>Ligne 1 Colonne 2</td>
    <td>Ligne 1 Colonne 3</td>
  </tr>
  <tr>
    <td>Ligne 2 Colonne 1</td>
    <td>Ligne 2 Colonne 2</td>
    <td>Ligne 2 Colonne 3</td>
  </tr>
</table>
```

Voici comment les navigateurs le rendent, si vous n'ajoutez aucun style CSS :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.24.08.png)

En ajoutant ce CSS :

```css
th, td {
  padding: 10px;
  border: 1px solid #333;
}
```

fait en sorte que le tableau ressemble davantage à un tableau correct :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.26.15.png)

### **Fusionner des colonnes et des lignes**

Une ligne peut décider de s'étendre sur 2 colonnes ou plus, en utilisant l'attribut `colspan` :

```html
<table>
  <tr>
    <th>Colonne 1</th>
    <th>Colonne 2</th>
    <th>Colonne 3</th>
  </tr>
  <tr>
    <td colspan="2">Ligne 1 Colonnes 1-2</td>
    <td>Ligne 1 Colonne 3</td>
  </tr>
  <tr>
    <td colspan="3">Ligne 2 Colonnes 1-3</td>
  </tr>
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.27.59.png)

Ou elle peut s'étendre sur 2 lignes ou plus, en utilisant l'attribut `rowspan` :

```html
<table>
  <tr>
    <th>Colonne 1</th>
    <th>Colonne 2</th>
    <th>Colonne 3</th>
  </tr>
  <tr>
    <td colspan="2" rowspan="2">Lignes 1-2 Colonnes 1-2</td>
    <td>Ligne 1 Colonne 3</td>
  </tr>
  <tr>
    <td>Ligne 2 Colonne 3</td>
  </tr>
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.29.37.png)

### **En-têtes de ligne**

Auparavant, j'ai expliqué comment vous pouvez avoir des en-têtes de colonne, en utilisant la balise `th` à l'intérieur de la première balise `tr` du tableau.

Vous pouvez ajouter une balise `th` comme premier élément à l'intérieur d'une balise `tr` qui n'est pas la première balise `tr` du tableau, pour avoir des en-têtes de ligne :

```html
<table>
  <tr>
    <th></th>
    <th>Colonne 2</th>
    <th>Colonne 3</th>
  </tr>
  <tr>
    <th>Ligne 1</th>
    <td>Col 2</td>
    <td>Col 3</td>
  </tr>
  <tr>
    <th>Ligne 2</th>
    <td>Col 2</td>
    <td>Col 3</td>
  </tr>
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.49.16.png)

### **Plus de balises pour organiser le tableau**

Vous pouvez ajouter 3 balises supplémentaires dans un tableau, pour l'organiser davantage.

Cela est idéal pour les grands tableaux. Et pour définir correctement un en-tête et un pied de page.

Ces balises sont

* `thead`
* `tbody`
* `tfoot`

Elles enveloppent les balises `tr` pour définir clairement les différentes sections du tableau. Voici un exemple :

```html
<table>
  <thead>
    <tr>
      <th></th>
      <th>Colonne 2</th>
      <th>Colonne 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ligne 1</th>
      <td>Col 2</td>
      <td>Col 3</td>
    </tr>
    <tr>
      <th>Ligne 2</th>
      <td>Col 2</td>
      <td>Col 3</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td></td>
      <td>Pied de page de Col 1</td>
      <td>Pied de page de Col 2</td>
    </tr>
  </tfoot>
</table>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-06-20-at-10.52.41.png)

## **Légende du tableau**

Un tableau doit avoir une balise `caption` qui décrit son contenu. Cette balise doit être placée immédiatement après la balise d'ouverture `table` :

```html
<table>
  <caption>Âge des chiens</caption>
  <tr>
    <th>Chien</th>
    <th>Âge</th>
  </tr>
  <tr>
    <td>Roger</td>
    <td>7</td>
  </tr>
</table>
```

# **BALISES MULTIMÉDIA : `AUDIO` ET `VIDEO`**

Dans cette section, je veux vous montrer les balises `audio` et `video`.

## **La balise `audio`**

Cette balise vous permet d'intégrer du contenu audio dans vos pages HTML.

Cet élément peut diffuser de l'audio, peut-être en utilisant un microphone via `getUserMedia()`, ou il peut lire une source audio que vous référencez en utilisant l'attribut `src` :

```html
<audio src="fichier.mp3">
```

Par défaut, le navigateur n'affiche aucun contrôle pour cet élément. Ce qui signifie que l'audio ne sera joué que s'il est défini en lecture automatique (plus d'informations à ce sujet plus tard) et l'utilisateur ne peut pas voir comment l'arrêter ou contrôler le volume ou se déplacer dans la piste.

Pour afficher les contrôles intégrés, vous pouvez ajouter l'attribut `controls` :

```html
<audio src="fichier.mp3" controls>
```

Les contrôles peuvent avoir une apparence personnalisée.

Vous pouvez spécifier le type MIME du fichier audio en utilisant l'attribut `type`. Si non défini, le navigateur essaiera de le déterminer automatiquement :

```html
<audio src="fichier.mp3" controls type="audio/mpeg">
```

Un fichier audio ne se lit pas automatiquement par défaut. Ajoutez l'attribut `autoplay` pour lire l'audio automatiquement :

```html
<audio src="fichier.mp3" controls autoplay>
```

Note : les navigateurs mobiles n'autorisent pas la lecture automatique

L'attribut `loop` redémarre la lecture de l'audio à 0:00 s'il est défini ; sinon, si absent, l'audio s'arrête à la fin du fichier :

```html
<audio src="fichier.mp3" controls autoplay loop>
```

Vous pouvez également lire un fichier audio en mode muet en utilisant l'attribut `muted` (je ne suis pas vraiment sûr de l'utilité de cela) :

```html
<audio src="fichier.mp3" controls autoplay loop muted>
```

En utilisant JavaScript, vous pouvez écouter divers événements se produisant sur un élément `audio`, les plus basiques étant :

* `play` lorsque le fichier commence à être lu
* `pause` lorsque la lecture audio a été mise en pause
* `playing` lorsque l'audio est repris après une pause
* `ended` lorsque la fin du fichier audio a été atteinte

## **La balise `video`**

Cette balise vous permet d'intégrer du contenu vidéo dans vos pages HTML.

Cet élément peut diffuser de la vidéo, en utilisant une webcam via `getUserMedia()` ou **WebRTC**, ou il peut lire une source vidéo que vous référencez en utilisant l'attribut `src` :

```html
<video src="fichier.mp4">
```

Par défaut, le navigateur n'affiche aucun contrôle pour cet élément, juste la vidéo.

Ce qui signifie que la vidéo ne sera lue que si elle est définie en lecture automatique (plus d'informations à ce sujet plus tard) et l'utilisateur ne peut pas voir comment l'arrêter, la mettre en pause, contrôler le volume ou sauter à une position spécifique dans la vidéo.

Pour afficher les contrôles intégrés, vous pouvez ajouter l'attribut `controls` :

```html
<video src="fichier.mp4" controls>
```

Les contrôles peuvent avoir une apparence personnalisée.

Vous pouvez spécifier le type MIME du fichier vidéo en utilisant l'attribut `type`. Si non défini, le navigateur essaiera de le déterminer automatiquement :

```html
<video src="fichier.mp4" controls type="video/mp4">
```

Un fichier vidéo ne se lit pas automatiquement par défaut. Ajoutez l'attribut `autoplay` pour lire la vidéo automatiquement :

```html
<video src="fichier.mp4" controls autoplay>
```

Certains navigateurs nécessitent également l'attribut `muted` pour la lecture automatique. La vidéo se lit automatiquement uniquement si elle est en mode muet :

```html
<audio src="fichier.mp3" controls autoplay muted>
```

L'attribut `loop` redémarre la lecture de la vidéo à 0:00 s'il est défini ; sinon, si absent, la vidéo s'arrête à la fin du fichier :

```html
<video src="fichier.mp4" controls autoplay loop>
```

Vous pouvez définir une image à utiliser comme image de poster :

```html
<video src="fichier.mp4" poster="image.png">
```

Si elle n'est pas présente, le navigateur affichera la première image de la vidéo dès qu'elle sera disponible.

Vous pouvez définir les attributs `width` et `height` pour définir l'espace que l'élément occupera afin que le navigateur puisse en tenir compte et qu'il ne change pas la mise en page lorsqu'il est finalement chargé. Il prend une valeur numérique, exprimée en pixels.

En utilisant JavaScript, vous pouvez écouter divers événements se produisant sur un élément `video`, les plus basiques étant :

* `play` lorsque le fichier commence à être lu
* `pause` lorsque la vidéo a été mise en pause
* `playing` lorsque la vidéo est reprise après une pause
* `ended` lorsque la fin du fichier vidéo a été atteinte

# **IFRAMES**

La balise `iframe` nous permet d'intégrer du contenu provenant d'autres origines (d'autres sites) dans notre page web.

Techniquement, un iframe crée un nouveau contexte de navigation imbriqué. Cela signifie que tout ce qui se trouve dans l'iframe n'interfère pas avec la page parente, et vice versa. JavaScript et CSS ne "fuient" pas vers/depuis les iframes.

De nombreux sites utilisent des iframes pour effectuer diverses choses. Vous êtes peut-être familier avec Codepen, Glitch ou d'autres sites qui vous permettent de coder dans une partie de la page, et vous voyez le résultat dans une boîte. C'est un iframe.

Vous en créez un de cette manière :

```html
<iframe src="page.html"></iframe>
```

Vous pouvez charger une URL absolue, aussi :

```html
<iframe src="https://site.com/page.html"></iframe>
```

Vous pouvez définir un ensemble de paramètres de largeur et de hauteur (ou les définir en utilisant CSS) sinon l'iframe utilisera les valeurs par défaut, une boîte de 300x150 pixels :

```html
<iframe src="page.html" width="800" height="400"></iframe>
```

## **Srcdoc**

L'attribut `srcdoc` vous permet de spécifier un HTML en ligne à afficher. C'est une alternative à `src`, mais récente et non supportée dans Edge 18 et versions antérieures, et dans IE :

```html
<iframe srcdoc="<p>Mon chien est un bon chien</p>"></iframe>
```

## **Sandbox**

L'attribut `sandbox` nous permet de limiter les opérations autorisées dans les iframes.

Si nous l'omettons, tout est autorisé :

```html
<iframe src="page.html"></iframe>
```

Si nous le définissons à "", rien n'est autorisé :

```html
<iframe src="page.html" sandbox=""></iframe>
```

Nous pouvons sélectionner ce qu'il faut autoriser en ajoutant des options dans l'attribut `sandbox`. Vous pouvez en autoriser plusieurs en ajoutant un espace entre elles. Voici une liste incomplète des options que vous pouvez utiliser :

* `allow-forms` : autoriser la soumission de formulaires
* `allow-modals` : autoriser l'ouverture de fenêtres modales, y compris l'appel de `alert()` en JavaScript
* `allow-orientation-lock` : autoriser le verrouillage de l'orientation de l'écran
* `allow-popups` : autoriser les popups, en utilisant `window.open()` et les liens `target="_blank"`
* `allow-same-origin` : traiter la ressource en cours de chargement comme ayant la même origine
* `allow-scripts` : permet à l'iframe chargé d'exécuter des scripts (mais pas de créer des popups).
* `allow-top-navigation` : donne accès à l'iframe au contexte de navigation de niveau supérieur

## **Allow**

Actuellement expérimental et uniquement supporté par les navigateurs basés sur Chromium, c'est l'avenir du partage de ressources entre la fenêtre parente et l'iframe.

C'est similaire à l'attribut `sandbox`, mais nous permet d'autoriser des fonctionnalités spécifiques, y compris :

* `accelerometer` donne accès à l'interface Accelerometer de l'API Sensors
* `ambient-light-sensor` donne accès à l'interface AmbientLightSensor de l'API Sensors
* `autoplay` permet de lire automatiquement les fichiers vidéo et audio
* `camera` permet d'accéder à la caméra depuis l'API getUserMedia
* `display-capture` permet d'accéder au contenu de l'écran en utilisant l'API getDisplayMedia
* `fullscreen` permet d'accéder au mode plein écran
* `geolocation` permet d'accéder à l'API Geolocation
* `gyroscope` donne accès à l'interface Gyroscope de l'API Sensors
* `magnetometer` donne accès à l'interface Magnetometer de l'API Sensors
* `microphone` donne accès au microphone de l'appareil en utilisant l'API getUserMedia
* `midi` permet l'accès à l'API Web MIDI
* `payment` donne accès à l'API Payment Request
* `speaker` permet l'accès à la lecture audio via les haut-parleurs de l'appareil
* `usb` donne accès à l'API WebUSB.
* `vibrate` donne accès à l'API Vibration
* `vr` donne accès à l'API WebVR

## **Referrer**

Lors du chargement d'un iframe, le navigateur envoie des informations importantes sur qui le charge dans l'en-tête `Referer` (remarquez le `r` unique, une faute de frappe avec laquelle nous devons vivre).

La mauvaise orthographe de referrer provient de la proposition originale du scientifique informatique Phillip Hallam-Baker d'incorporer le champ dans la spécification HTTP. La mauvaise orthographe a été gravée dans le marbre au moment de son incorporation dans le document de demande de commentaires RFC 1945.

L'attribut `referrerpolicy` nous permet de définir le référent à envoyer à l'iframe lors de son chargement. Le référent est un en-tête HTTP qui permet à la page de savoir qui la charge. Voici les valeurs autorisées :

* `no-referrer-when-downgrade` c'est la valeur par défaut, et n'envoie pas le référent lorsque la page actuelle est chargée via HTTPS et que l'iframe se charge sur le protocole HTTP
* `no-referrer` n'envoie pas l'en-tête de référent
* `origin` le référent est envoyé, et ne contient que l'origine (port, protocole, domaine), et non l'origine + le chemin qui est la valeur par défaut
* `origin-when-cross-origin` lors du chargement depuis la même origine (port, protocole, domaine) dans l'iframe, le référent est envoyé dans sa forme complète (origine + chemin). Sinon, seule l'origine est envoyée
* `same-origin` le référent est envoyé uniquement lors du chargement depuis la même origine (port, protocole, domaine) dans l'iframe
* `strict-origin` envoie l'origine comme référent si la page actuelle est chargée via HTTPS et que l'iframe se charge également sur le protocole HTTPS. N'envoie rien si l'iframe est chargée via HTTP
* `strict-origin-when-cross-origin` envoie l'origine + le chemin comme référent lors du travail sur la même origine. Envoie l'origine comme référent si la page actuelle est chargée via HTTPS et que l'iframe se charge également sur le protocole HTTPS. N'envoie rien si l'iframe est chargée via HTTP
* `unsafe-url` : envoie l'origine + le chemin comme référent même lors du chargement de ressources depuis HTTP et que la page actuelle est chargée via HTTPS

# **IMAGES**

Les images peuvent être affichées en utilisant la balise `img`.

Cette balise accepte un attribut `src`, que nous utilisons pour définir la source de l'image :

```html
<img src="image.png">
```

Nous pouvons utiliser un large éventail d'images. Les plus courantes sont PNG, JPEG, GIF, SVG et plus récemment WebP.

La norme HTML exige qu'un attribut `alt` soit présent, pour décrire l'image. Cela est utilisé par les lecteurs d'écran et également par les robots des moteurs de recherche :

```html
<img src="chien.png" alt="Une photo d'un chien">
```

Vous pouvez définir les attributs `width` et `height` pour définir l'espace que l'élément occupera, afin que le navigateur puisse en tenir compte et qu'il ne change pas la mise en page lorsqu'il est entièrement chargé. Il prend une valeur numérique, exprimée en pixels.

```html
<img src="chien.png" alt="Une photo d'un chien" width="300" height="200">
```

## **La balise `figure`**

La balise `figure` est souvent utilisée avec la balise `img`.

`figure` est une balise sémantique souvent utilisée lorsque vous souhaitez afficher une image avec une légende. Vous l'utilisez comme ceci :

```html
<figure>
    <img src="chien.png"
         alt="Un beau chien">
    <figcaption>Un beau chien</figcaption>
</figure>
```

La balise `figcaption` enveloppe le texte de la légende.

## **Images réactives utilisant `srcset`**

L'attribut `srcset` vous permet de définir des images réactives que le navigateur peut utiliser en fonction de la densité de pixels ou de la largeur de la fenêtre, selon vos préférences. Ainsi, il ne télécharge que les ressources dont il a besoin pour rendre la page, sans télécharger une image plus grande si elle est sur un appareil mobile, par exemple.

Voici un exemple, où nous donnons 4 images supplémentaires pour 4 tailles d'écran différentes :

```html
<img src="chien.png"
    alt="Une photo d'un chien"
    srcset="chien-500.png 500w,
               chien-800.png 800w,
             chien-1000.png 1000w,
             chien-1400.png 1400w">
```

Dans le `srcset`, nous utilisons la mesure `w` pour indiquer la largeur de la fenêtre.

Puisque nous le faisons, nous devons également utiliser l'attribut `sizes` :

```html
<img src="chien.png"
    alt="Une photo d'un chien"
    sizes="(max-width: 500px) 100vw, (max-width: 900px) 50vw, 800px"
    srcset="chien-500.png 500w,
               chien-800.png 800w,
             chien-1000.png 1000w,
             chien-1400.png 1400w">
```

Dans cet exemple, la chaîne `(max-width: 500px) 100vw, (max-width: 900px) 50vw, 800px` dans l'attribut `sizes` décrit la taille de l'image en relation avec la fenêtre d'affichage, avec plusieurs conditions séparées par un point-virgule.

La condition de média `max-width: 500px` définit la taille de l'image en corrélation avec la largeur de la fenêtre. En bref, si la taille de la fenêtre est < 500px, elle rend l'image à 100% de la taille de la fenêtre.

Si la taille de la fenêtre est plus grande mais < `900px`, elle rend l'image à 50% de la taille de la fenêtre.

Et si elle est encore plus grande, elle rend l'image à 800px.

L'unité de mesure `vw` peut être nouvelle pour vous, et en bref, nous pouvons dire que 1 `vw` est 1% de la largeur de la fenêtre, donc `100vw` est 100% de la largeur de la fenêtre.

Un site web utile pour générer le `srcset` et des images progressivement plus petites est [https://responsivebreakpoints.com/](https://responsivebreakpoints.com/).

## **La balise `picture`**

HTML nous donne également la balise `picture`, qui fait un travail très similaire à `srcset`, et les différences sont très subtiles.

Vous utilisez `picture` lorsque, au lieu de simplement servir une version plus petite d'un fichier, vous souhaitez complètement le changer. Ou servir un format d'image différent.

Le meilleur cas d'utilisation que j'ai trouvé est lorsque vous servez une image WebP, qui est un format encore peu supporté. Dans la balise `picture`, vous spécifiez une liste d'images, et elles seront utilisées dans l'ordre, donc dans l'exemple suivant, les navigateurs qui supportent WebP utiliseront la première image, et basculeront vers JPG si ce n'est pas le cas :

```html
<picture>
  <source type="image/webp" srcset="image.webp">
  <img src="image.jpg" alt="Une image">
</picture>
```

La balise `source` définit un (ou plusieurs) formats pour les images. La balise `img` est le recours en cas de navigateur très ancien qui ne supporte pas la balise `picture`.

Dans la balise `source` à l'intérieur de `picture`, vous pouvez ajouter un attribut `media` pour définir des requêtes média.

L'exemple qui suit fonctionne un peu comme l'exemple ci-dessus avec `srcset` :

```html
<picture>
  <source media="(min-width: 500w)" srcset="chien-500.png" sizes="100vw">
  <source media="(min-width: 800w)" srcset="chien-800.png" sizes="100vw">
  <source media="(min-width: 1000w)" srcset="chien-1000.png"    sizes="800px">
  <source media="(min-width: 1400w)" srcset="chien-1400.png"    sizes="800px">
  <img src="chien.png" alt="Une image de chien">
</picture>
```

Mais ce n'est pas son cas d'utilisation, car comme vous pouvez le voir, c'est beaucoup plus verbeux.

La balise `picture` est récente mais est maintenant [supportée](https://caniuse.com/#search=picture) par tous les principaux navigateurs sauf Opera Mini et IE (toutes versions).

# **ACCESSIBILITÉ**

Il est important que nous concevions notre HTML en gardant à l'esprit l'accessibilité.

Avoir un HTML accessible signifie que les personnes handicapées peuvent utiliser le Web. Il y a des utilisateurs totalement aveugles ou malvoyants, des personnes ayant des problèmes de perte auditive et une multitude d'autres handicaps différents.

Malheureusement, ce sujet ne reçoit pas l'importance qu'il mérite, et il ne semble pas aussi cool que d'autres.

Et si une personne ne peut pas _voir_ votre page, mais souhaite toujours consulter son contenu ? Tout d'abord, comment fait-elle cela ? Elle ne peut pas utiliser la souris, elle utilise quelque chose appelé un **lecteur d'écran**. Vous n'avez pas besoin de l'imaginer. Vous pouvez en essayer un maintenant : Google fournit l'extension gratuite [ChromeVox Chrome Extension](https://chrome.google.com/webstore/detail/chromevox/kgejglhpjiefppelpmljglcjbhoiplfn/). L'accessibilité doit également prendre soin de permettre aux outils de sélectionner facilement des éléments ou de naviguer à travers les pages.

Les pages Web et les applications Web ne sont pas toujours construites avec l'accessibilité comme l'un de leurs premiers objectifs, et peut-être que la version 1 est publiée non accessible mais il est possible de rendre une page Web accessible après coup. Plus tôt c'est mieux, mais il n'est jamais trop tard.

C'est important et dans mon pays, les sites Web construits par le gouvernement ou d'autres organisations publiques doivent être accessibles.

Que signifie rendre un HTML accessible ? Laissez-moi illustrer les principales choses auxquelles vous devez penser.

Note : il y a plusieurs autres choses à prendre en compte, qui peuvent relever du sujet CSS, comme les couleurs, le contraste et les polices. Ou [comment rendre les images SVG accessibles](https://css-tricks.com/accessible-svgs/). Je n'en parle pas ici.

## **Utiliser le HTML sémantique**

Le HTML sémantique est très important et c'est l'une des principales choses dont vous devez prendre soin. Laissez-moi illustrer quelques scénarios courants.

Il est important d'utiliser la structure correcte pour les balises de titre. La plus importante est `h1`, et vous utilisez des nombres plus élevés pour les moins importantes, mais tous les titres de même niveau doivent avoir la même signification (pensez à cela comme une structure d'arbre)

```js
h1
    h2
        h3
    h2
    h2
        h3
            h4
```

Utilisez `strong` et `em` au lieu de `b` et `i`. Visuellement, ils ont la même apparence, mais les deux premiers ont plus de signification associée. `b` et `i` sont plus des éléments visuels.

Les listes sont importantes. Un lecteur d'écran peut détecter une liste et fournir un aperçu, puis laisser l'utilisateur choisir d'entrer dans la liste ou non.

Un tableau doit avoir une balise `caption` qui décrit son contenu :

```html
<table>
  <caption>Âge des chiens</caption>
  <tr>
    <th>Chien</th>
    <th>Âge</th>
  </tr>
  <tr>
    <td>Roger</td>
    <td>7</td>
  </tr>
</table>
```

## **Utiliser les attributs `alt` pour les images**

Toutes les images doivent avoir une balise `alt` décrivant le contenu de l'image. Ce n'est pas seulement une bonne pratique, c'est requis par la norme HTML et votre HTML sans cela n'est pas validé.

```html
<img src="chien.png" alt="photo de mon chien">
```

C'est aussi bon pour les moteurs de recherche, si c'est un incitatif pour vous de l'ajouter.

## **Utiliser l'attribut `role`**

L'attribut `role` vous permet d'assigner des rôles spécifiques aux divers éléments de votre page.

Vous pouvez assigner de nombreux rôles différents : complémentaire, liste, élément de liste, principal, navigation, région, onglet, alerte, application, article, bannière, bouton, cellule, case à cocher, info de contenu, dialogue, document, flux, figure, formulaire, grille, cellule de grille, titre, image, boîte de liste, ligne, groupe de lignes, recherche, interrupteur, tableau, panneau d'onglet, zone de texte, minuteur.

Il y en a beaucoup et pour la référence complète de chacun d'eux, je vous donne [ce lien MDN](https://developer.mozilla.org/fr/docs/Web/Accessibility/ARIA/Roles). Mais vous n'avez pas besoin d'assigner un rôle à chaque élément de la page. Les lecteurs d'écran peuvent déduire à partir de la balise HTML dans la plupart des cas. Par exemple, vous n'avez pas besoin d'ajouter une balise de rôle aux balises sémantiques comme `nav`, `button`, `form`.

Prenons l'exemple de la balise `nav`. Vous pouvez l'utiliser pour définir la navigation de la page comme ceci :

```html
<nav>
  <ul>
    <li><a href="/">Accueil</a></li>
    <li><a href="/blog">Blog</a></li>
  </ul>
</nav>
```

Si vous étiez _obligé_ d'utiliser une balise `div` au lieu de `nav`, vous utiliseriez le rôle `navigation` :

```html
<div role="navigation">
  <ul>
    <li><a href="/">Accueil</a></li>
    <li><a href="/blog">Blog</a></li>
  </ul>
</div>
```

Ainsi, vous avez un exemple pratique : `role` est utilisé pour assigner une valeur significative lorsque la balise ne véhicule pas déjà le sens.

## **Utiliser l'attribut `tabindex`**

L'attribut `tabindex` vous permet de changer l'ordre de sélection des éléments "sélectionnables" en appuyant sur la touche Tab. Par défaut, seuls les liens et les éléments de formulaire sont "sélectionnables" par navigation en utilisant la touche Tab (et vous n'avez pas besoin de définir `tabindex` sur eux).

Ajouter `tabindex="0"` rend un élément sélectionnable :

```html
<div tabindex="0">
...
</div>
```

Utiliser `tabindex="-1"` retire un élément de cette navigation basée sur les tabulations, et cela peut être très utile.

## **Utiliser les attributs `aria`**

ARIA est un acronyme qui signifie Accessible Rich Internet Applications et définit des sémantiques qui peuvent être appliquées aux éléments.

### **`aria-label`**

Cet attribut est utilisé pour ajouter une chaîne de caractères pour décrire un élément.

Exemple :

```html
<p aria-label="La description du produit">...</p>
```

J'utilise cet attribut sur la barre latérale de mon blog, où j'ai une boîte de recherche sans étiquette explicite, car elle a un attribut placeholder.

### **`aria-labelledby`**

Cet attribut établit une corrélation entre l'élément actuel et celui qui le libelle.

Si vous savez comment un élément `input` peut être associé à un élément `label`, c'est similaire.

Nous passons l'ID de l'élément qui décrit l'élément actuel.

Exemple :

```html
<h3 id="description">La description du produit</h3>

<p aria-labelledby="description">
...
</p>
```

### **`aria-describedby`**

Cet attribut nous permet d'associer un élément à un autre élément qui sert de description.

Exemple :

```html
<button aria-describedby="payNowDescription" >Payer maintenant</button>

<div id="payNowDescription">Cliquer sur le bouton vous enverra à notre formulaire Stripe !</div>
```

### **Utiliser aria-hidden pour masquer le contenu**

J'aime un design minimaliste dans mes sites. Mon blog, par exemple, est principalement du contenu, avec quelques liens dans la barre latérale. Mais certaines choses dans la barre latérale sont juste des éléments visuels qui n'ajoutent rien à l'expérience d'une personne qui ne peut pas voir la page. Comme mon image de logo, ou le sélecteur de thème sombre/clair.

Ajouter l'attribut `aria-hidden="true"` indiquera aux lecteurs d'écran d'ignorer cet élément.

## **Où apprendre plus**

Ce n'est qu'une introduction au sujet. Pour en savoir plus, je recommande ces ressources :

* [https://www.w3.org/TR/WCAG20/](https://www.w3.org/TR/WCAG20/)
* [https://webaim.org](https://webaim.org/)
* [https://developers.google.com/web/fundamentals/accessibility/](https://developers.google.com/web/fundamentals/accessibility/)

---

Vous avez atteint la fin du Manuel HTML.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1563876708.png)

**[Cliquez ici pour obtenir une version PDF / ePub / Mobi de ce](https://flaviocopes.com/page/html-handbook/) livre **à lire hors ligne**!**