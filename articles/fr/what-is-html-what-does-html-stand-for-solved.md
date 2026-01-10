---
title: Qu'est-ce que le HTML ? Que signifie HTML ? [Résolu]
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-04-12T01:27:51.000Z'
originalURL: https://freecodecamp.org/news/what-is-html-what-does-html-stand-for-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-270404.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le HTML ? Que signifie HTML ? [Résolu]
seo_desc: 'HTML is one of the fundamental technologies you can learn when starting
  out in web development. HTML code is present in every single webpage online.

  Once you have a good grasp of the fundamental concepts of the language, you will
  be well equipped to ...'
---

Le HTML est l'une des technologies fondamentales que vous pouvez apprendre lorsque vous débutez dans le développement web. Le code HTML est présent dans chaque page web en ligne.

Une fois que vous aurez bien compris les concepts fondamentaux du langage, vous serez bien équipé pour passer aux deux autres technologies présentes dans presque tous les sites web - CSS et JavaScript.

Dans cet article, vous apprendrez les bases du HTML. 

Vous commencerez par apprendre ce que signifie l'acronyme. Ensuite, vous comprendrez son but en parcourant un bref historique de l'évolution du langage au fil des ans.

Vous apprendrez également certaines des balises les plus couramment utilisées et certaines des meilleures pratiques modernes à suivre.

Voici ce que nous allons couvrir dans cet article :

1. [Introduction au HTML pour les débutants](#introduction)
    1. [Un bref historique du HTML](#historique)
2. [Un aperçu de la syntaxe HTML](#syntaxe)
    1. [Comment créer un modèle HTML5](#modele)
3. [Un aperçu des éléments HTML](#elements) 
    - [Créer des commentaires de code](#commentaires)
    - [Créer des titres](#titres)
    - [Créer des listes](#listes)
    - [Créer des paragraphes](#paragraphes)
    - [Créer des liens](#liens)
    - [Créer des conteneurs](#conteneurs)
    - [Créer des images](#images)
4. [Qu'est-ce que le HTML sémantique et pourquoi est-il important](#semantique)

## Que signifie HTML et à quoi sert-il ? Une introduction au HTML <a name="introduction"></a>

Les documents de tout type, qu'ils soient imprimés ou numériques, ont besoin de structure.

La structure permet aux utilisateurs de naviguer facilement dans le document et de manière non confuse.

En haut de la plupart des documents, il y a généralement un grand titre. 

Ce titre de niveau supérieur transmet le message général de la page, explique de quoi parle le contenu et donne le ton pour ce qui suit. 

Ensuite, il y a un texte introductif et d'autres titres plus petits. 

Les différents niveaux de titres créent une structure hiérarchique pour l'information.

Généralement, quelques paragraphes de texte suivent chaque titre.

En ce qui concerne les documents web, des images, des vidéos et des hyperliens (ou liens) accompagnent le contenu textuel. Les liens aident les utilisateurs à naviguer vers une section différente de la page ou vers une page web différente. Ces éléments apportent plus de vie au document. 

Il peut également y avoir des formulaires pour que les utilisateurs saisissent des données, des cases à cocher ou même des boutons radio pour sélectionner une option parmi un groupe d'éléments.

Pour créer une structure, formater le contenu et l'afficher dans les navigateurs web, vous devez utiliser le HTML.

HTML est l'abréviation de **HyperText Markup Language**, et c'est le langage du World Wide Web.

Depuis sa création, il a subi de nombreuses révisions, changements et développements.

Dans la section suivante, vous verrez comment le HTML est apparu, ainsi que les changements qu'il a subis jusqu'à ce qu'il se développe en la version la plus récente et standardisée, HTML5, qui est la version que nous utilisons aujourd'hui.

### Un bref historique du HTML <a name="historique"></a>

En 1989, un scientifique britannique nommé Sir Tim Berners Lee travaillait au CERN (le Conseil européen pour la recherche nucléaire) à Genève, en Suisse.

En tant que chercheur, il a eu l'idée de créer un système interconnecté et distribué. Avec un tel système en place, le partage et l'organisation de l'information pourraient être réalisés à un rythme plus rapide et de manière beaucoup plus facile et pratique.

Des scientifiques et des universitaires du monde entier pourraient échanger des ressources et des résultats de recherche les uns avec les autres. 

L'objectif était de cliquer d'un document de référence à un autre et de permettre aux utilisateurs de naviguer facilement d'une page à une autre en fournissant ces liens.

De cette idée, le World Wide Web est né.

En 1990, il a développé le HTTP (un acronyme pour HyperText Transfer Protocol), un protocole de communication qui définit comment les ressources sont échangées et transférées. 

Il a également développé le HTML, un serveur et un navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-06-at-2.08.29-PM.png)
_[Image du CERN PhotoLab](http://cds.cern.ch/record/39437#31)_

Le SGML (abréviation de Standard Generalized Markup Language) existait déjà et était la base du HTML. Mais il était beaucoup plus simple. 

Au lieu de créer le HTML à partir de zéro, Berners-Lee a adopté certains concepts préétablis du SGML.  

L'une de ces caractéristiques du SGML incorporées dans le HTML est les éléments structurels, autrement connus sous le nom de **balises**. 

Les balises dans le SGML allaient par paires (avec une balise d'ouverture et une balise de fermeture). 

Une autre caractéristique adoptée était la notation des chevrons pour les balises. 

Sir Tim Berners Lee a inclus certaines des paires de balises qui existaient déjà dans le SGML. Par exemple, il a inclus la balise de titre (`<h1>`, `</h1>`) et la balise de paragraphe (`<p>`, `</p>`) et a incorporé une balise de référence hypertexte de sa propre invention (`<a>`, `</a>`).

En 1991, il a publié la première proposition pour le HTML.

Cependant, la première version officielle du HTML était le HTML 2.0, développé par l'IETF (abréviation de Internet Engineering Task Force), avec de nombreuses fonctionnalités supplémentaires incorporées. 

L'une d'entre elles, en particulier, était la capacité d'incorporer des images dans les documents en utilisant la balise `<img>`. 

Mosaic, le navigateur leader de l'époque, a initialement inclus cette capacité, et l'IETF en a fait une norme.

À cette époque, les soi-disant guerres des navigateurs battaient leur plein.

Les entreprises de navigateurs, comme Netscape Communications Corporation avec le navigateur Netscape Navigator, manipulaient le HTML et créaient une version propriétaire spécifique au navigateur des balises HTML.

D'autres navigateurs ont tenté de les reproduire mais sans succès - les pages web avaient l'air bien sur un navigateur mais n'étaient pas utilisables sur un autre. 

Le W3C (abréviation de World Wide Web Consortium) a été fondé, qui a pris en charge la création de normes tant nécessaires.

Le W3C a repris la tâche de poursuivre le développement du HTML.

Au cours du reste des années 90, différentes versions du HTML ont été publiées, telles que le HTML 3.0 et le HTML 3.2.

La norme successive recommandée par le W3C était le HTML 4, qui se concentrait sur l'internationalisation. 

Les documents pouvaient désormais être écrits dans n'importe quelle autre langue du monde, et pas seulement en anglais. 

En 1999, il y a eu plus de mises à jour pour le HTML, avec la nouvelle version du HTML 4.01.

Suite à la publication du HTML 4.01, le développement du HTML a pris un tournant et est allé dans une direction différente.

Le W3C a créé le XHTML 1.0, une branche du HTML qui incorporait le XML (abréviation de eXtensible Markup Language). Cette fois, il y avait des règles de codage plus strictes et moins de liberté pour que le code puisse fonctionner dans un navigateur. 

La version suivante du XHTML 1.0, le XHTML 1.1, ressemblait encore plus au XML au point où Internet Explorer, le navigateur le plus populaire à l'époque, ne supportait pas les documents.

Le W3C se concentrait sur le XML, donc ils ont commencé à travailler sur la création du XHTML 2.0. Mais il n'y a eu aucun progrès, et ils se sont rendu compte qu'ils ne suivaient pas la bonne voie. Le W3C a abandonné le projet.

Pendant que le W3C travaillait sur le développement du XHTML 2.0, un autre groupe de travail s'est formé appelé le WHATWG (abréviation de Web Hypertext Application Technology Working Group). 

Le WHATWG était composé de représentants de différentes entreprises, comme Mozilla et Apple, qui travaillaient sur la création d'une nouvelle version du HTML orientée vers les applications web.

En 2006, Sir Tim Berners Lee a annoncé la collaboration des deux groupes, le W3C et le WHATWG, pour travailler ensemble sur la nouvelle version du HTML - le HTML5.

Le HTML5 est la version standard recommandée du HTML utilisée jusqu'à ce jour.

## Un aperçu de la syntaxe HTML <a name="syntaxe"></a>

Examinons de plus près le HTML, spécifiquement les balises HTML, et découvrons la syntaxe de base. 

Comme vous l'avez vu dans la section précédente, les balises sont une structure syntaxique héritée du SGML.

Prenons l'exemple de code HTML suivant :

```html
<a> freeCodeCamp </a>
```

Décomposons cela :

- Il existe *deux* types de balises. Une balise **d'ouverture** (`<a>`) et une balise **de fermeture** (`</a>`)
- Une balise se compose d'un chevron gauche, d'un chevron droit et d'un caractère entre eux. 
- Les balises de fermeture ont une barre oblique (`/`) après le chevron gauche et avant le caractère.
- Le caractère dans la balise nous permet d'en savoir plus sur le contenu entre les balises. Dans ce cas, le caractère `a`, qui signifie `ancre`, indique qu'il s'agit d'un lien vers un endroit sur le web nommé `freeCodeCamp`.
- Entre les balises d'ouverture et de fermeture, il y a du contenu - dans ce cas, il s'agit du texte `freeCodeCamp`.
- Ensemble, la **balise d'ouverture, le contenu et la balise de fermeture** constituent un **élément** HTML.

Il est utile de mentionner que, dans l'exemple ci-dessus, vous avez vu un élément qui se compose à la fois d'une balise d'ouverture et d'une balise de fermeture. 

Cela dit, certains éléments se composent uniquement d'une balise **auto-fermante**, comme la balise `<img>`. Dans de tels cas, la barre oblique (comme `<img />`) est entièrement facultative. 

Dans l'exemple ci-dessus, il y a quelque chose qui ne va pas avec l'élément HTML. 

Il est censé pointer vers une ressource, d'où le caractère `a`, mais il n'y a aucune indication d'une ressource liée disponible quelque part.

Pour cela, vous devez utiliser un **attribut** HTML. Les attributs fournissent des informations supplémentaires sur l'élément.

Donc, corrigeons le code :

```html
<a href="https://www.freecodecamp.org/"> freeCodeCamp </a>
```

Maintenant, décomposons cela :

- `href="https://www.freecodecamp.org/"` est l'attribut qui accompagne l'élément. La plupart du temps, des éléments spécifiques acceptent et sont associés à certains attributs.
- Les attributs sont placés *uniquement* sur la balise d'ouverture, avant le chevron droit. Notez l'espace juste après le caractère.
- Les attributs sont constitués de paires **nom** et **valeur**. Avec `href="https://www.freecodecamp.org/"`, le `nom` est `href` et la `valeur` est `https://www.freecodecamp.org/`. 
- La paire nom-valeur est séparée par l'opérateur d'assignation `=` .
- La valeur est toujours entourée de guillemets doubles `""`.

Maintenant que vous avez appris les bases des éléments HTML, comment configurez-vous un document HTML pour votre projet ?

Dans la section suivante, vous apprendrez comment créer un modèle HTML5. Un modèle sert de formule pour tous vos projets HTML.

### Comment créer un modèle HTML5 <a name="modele"></a>

Lorsque vous configurez de nouveaux projets HTML, vous constaterez que vous devez inclure les mêmes éléments à chaque fois.

Ces éléments sont essentiels et vous en aurez besoin pour faire fonctionner correctement votre site HTML, en suivant les meilleures pratiques et les normes.

Certains éditeurs de code offrent des raccourcis pour remplir et entrer automatiquement les éléments utilisés dans chaque nouveau projet HTML, ce qui vous fait gagner un temps considérable.

Cela est autrement connu sous le nom de modèle HTML. 

Un modèle est un squelette de base et une structure fondamentale dont chaque nouveau document HTML a besoin.

Pour créer un modèle, suivez les étapes suivantes :

- Tout d'abord, assurez-vous d'installer l'éditeur [Visual Studio Code](https://code.visualstudio.com/download).
- Créez un fichier avec une extension `.html`. Les fichiers contenant du code HTML doivent se terminer par cette extension.
- À l'intérieur du fichier vide, tapez un point d'exclamation, `!`.    

![Screenshot-2022-04-09-at-7.20.40-PM](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot-2022-04-09-at-7.20.40-PM.png)

Appuyez sur Entrée, ou cliquez sur le point d'exclamation qui mentionne qu'il s'agit d'une abréviation Emmet. Emmet est un plugin pour les éditeurs de code qui est intégré par défaut dans Visual Studio Code, et il vous aide à optimiser votre flux de travail HTML. 

Vous verrez alors le code suivant :

```html
<!DOCTYPE html>
<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Document</title>
	</head>
    
	<body>
        
	</body>
</html>
```

Décomposons cela :

- `<!DOCTYPE html>` est la première ligne de code qui doit être présente en haut de tous les documents HTML modernes. Vous pouvez remarquer qu'elle a une couleur différente du reste du code. Cela est dû au fait qu'il ne s'agit pas d'un élément HTML mais d'une *déclaration de type de document*. Elle indique aux navigateurs quel document attendre. Elle leur indique également la version de HTML utilisée. Dans ce cas, cette déclaration informe les navigateurs que le document contient du code HTML5.
- L'élément `<html>` est le premier élément de chaque document HTML et est considéré comme l'élément *racine*. Le `<html>` d'ouverture indique le début de tout le code HTML, et le `</html>` de fermeture la fin de tout le code HTML. L'attribut `lang` désigne la langue du document. À l'intérieur de `html`, il y a toujours *deux* éléments imbriqués : les éléments `head` et `body`.
- L'élément `<head>` contient des métadonnées et des configurations. Les métadonnées sont des informations sur la page. Ces informations sont cachées aux utilisateurs et ne sont pas visibles dans le navigateur. La seule information visible est le contenu de l'élément `title`, qui est le titre de la page. Le titre apparaît dans l'onglet du navigateur, en haut de la fenêtre du navigateur.
- L'élément `<body>` contient tout le contenu qui sera visible dans la fenêtre du navigateur. C'est ici que vous ajouterez votre code HTML pour votre projet.

## Un aperçu des éléments HTML de base <a name="elements"></a>

### Comment créer des commentaires de code <a name="commentaires"></a>

Les commentaires aident à clarifier votre code et la logique qui le sous-tend. Considérez-les comme des notes pour vous-même ou pour vos collègues.

Voici la syntaxe pour créer des commentaires :

```html
<!-- Je suis un commentaire -->
```

Tout ce qui se trouve entre `<!--` et `-->` n'apparaîtra pas sur votre page web car il est ignoré par les navigateurs.

### Comment créer des titres <a name="titres"></a>

Il existe six niveaux de titres en HTML :

```html
<h1>Niveau 1</h1>
<h2>Niveau 2</h2>
<h3>Niveau 3</h3>
<h4>Niveau 4</h4>
<h5>Niveau 5</h5>
<h6>Niveau 6</h6>
```

À mesure que le nombre contenu dans la balise augmente, le niveau d'importance diminue. Un titre `<h1>` a plus d'importance qu'un titre `<h6>`.

### Comment créer des listes <a name="listes"></a>

Il existe deux types de listes en HTML :

```html
<!-- liste non ordonnée (ou à puces) -->
<ul>
    <li> Un élément </li>
    <li> Un autre élément </li>
</ul>

<!-- liste ordonnée (ou numérotée) -->
<ol>
    <li> Élément 1 </li>
    <li> Élément 2 </li>
</ol>
```

Remarquez que dans les listes non ordonnées et ordonnées, la façon de créer des éléments de liste est d'utiliser l'élément `<li>`.

### Comment créer des paragraphes <a name="paragraphes"></a>

Pour créer un bloc de texte, utilisez l'élément `<p>` :

```html
<p> Je suis un paragraphe </p>
```

### Comment créer des liens <a name="liens"></a>

Vous avez vu l'élément `<a>` dans une section précédente. 

```html
<a href="https://www.freecodecamp.org/"> freeCodeCamp </a>
```

Typiquement, il y aura un soulignement sous le texte entre les balises d'ouverture et de fermeture `<a>`. Le curseur change également lorsque vous passez dessus. Ce texte indique la page ou la ressource liée.

L'attribut `href` est la destination, puisqu'il contient l'adresse du lien.

Une autre chose à garder à l'esprit est que vous pouvez imbriquer certains éléments à l'intérieur d'autres.

Par exemple, vous pouvez créer un lien à partir de certains textes dans un paragraphe, comme ceci :

```html
<p>Apprenez à coder gratuitement avec <a href="https://www.freecodecamp.org/"> freeCodeCamp </a> !</p>
```

Assurez-vous de fermer d'abord la balise imbriquée. Par exemple, évitez de faire cette erreur courante de débutant :

```html
<!-- ne faites pas cela ! -->

<p>Apprenez à coder gratuitement avec <a href="https://www.freecodecamp.org/"> freeCodeCamp </p> !</a>
```

Vous pouvez également lier différentes sections au sein de la même page.

Tout d'abord, vous devez inclure l'attribut `id` à la section que vous souhaitez lier, et lui attribuer une valeur.

Supposons que vous souhaitiez lier un paragraphe :

```html
<p id="ressource"> J'ai un contenu qui vaut la peine d'être lu et lié. Je suis dans une autre partie de la page ! </p>
```

Lorsque vous créez un lien (de la même manière que vous l'avez vu précédemment), incluez le signe dièse (`#`) devant la valeur attribuée à l'attribut `id` :

```html
<a href="#ressource">Lisez plus sur le sujet dans cette partie différente de la même page</a>
```

### Comment créer un conteneur <a name="conteneurs"></a>

L'élément `<div>` crée un conteneur générique pour contenir du contenu.

Il est couramment utilisé avec CSS pour obtenir différentes mises en page sur la page.

```html
<div></div>
```

### Comment créer des images <a name="images"></a>

Pour créer une image, utilisez l'élément `<img>`. Vous avez vu cet élément dans une section précédente. Pour rappel, il s'agit d'un élément auto-fermant.

Utilisez l'attribut `src`, qui spécifie la source de l'image (qui est soit une URL, soit un chemin vers l'image), et l'attribut `alt`. L'attribut `alt` est un texte qui s'affichera si l'image ne parvient pas à se charger pour une raison quelconque.

Il est également important de toujours inclure un attribut `alt` pour des raisons d'accessibilité, car les lecteurs d'écran liront le contenu à voix haute pour les utilisateurs malvoyants.

```html
<img src="chemin-vers-image" alt="Texte décrivant l'image">
```

### Comment créer des formulaires

Les formulaires sont un aspect nécessaire de presque toutes les pages web. C'est ainsi que les utilisateurs peuvent soumettre des informations et que vous pouvez collecter ces données.

Vous créez un formulaire en utilisant l'élément `<form>` :

```html
<form></form>
```

Cela dit, de nombreux attributs sont impliqués lors de la création d'un formulaire.

Lisez les ressources suivantes pour commencer avec les formulaires HTML :

- [Votre premier formulaire - MDN Docs](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form)
- [Un guide étape par étape pour commencer avec les formulaires HTML](https://www.freecodecamp.org/news/a-step-by-step-guide-to-getting-started-with-html-forms-7f77ae4522b5/)
- [Zone de texte en HTML - La balise de champ de saisie HTML](https://www.freecodecamp.org/news/text-box-in-html-the-input-field-html-tag/)

## Qu'est-ce que le HTML sémantique et pourquoi est-il important <a name="semantique"></a>

Le HTML sémantique est l'une des fonctionnalités les plus importantes du HTML5.

Le mot *sémantique* fait référence aux éléments HTML décrivant le contenu qu'ils contiennent, plutôt que d'être simplement des conteneurs génériques sans signification.

Au lieu d'utiliser des éléments `<div>` qui sont des conteneurs vides et génériques sans signification sémantique et qui sont simplement utilisés pour stocker du contenu, vous pouvez utiliser des éléments HTML5 sémantiques.

Le HTML sémantique consiste également à créer une meilleure structure pour le site.

Par exemple, vous pouvez utiliser l'élément `<header>` pour les informations situées en haut de la page. Ici, vous pouvez inclure un logo et un titre de niveau supérieur pour la page. À l'intérieur de `<header>`, vous pouvez imbriquer un autre élément sémantique, `<nav>`, pour créer une barre de navigation avec des liens vers différentes pages.

Pour le contenu principal de la page, vous pouvez utiliser l'élément `<main>`.

Vous pouvez stocker des informations en bas de la page dans un élément `<footer>`. Cela inclut généralement un plan du site, des liens vers les réseaux sociaux, des réponses aux questions courantes que les utilisateurs peuvent avoir, ou des informations de contact.

Le HTML sémantique ne se concentre pas sur l'apparence du contenu.

Par exemple, il existe deux éléments HTML, `<b>` et `<i>`, pour rendre le texte **gras** et *italique*, respectivement.

Cependant, ces éléments se concentrent sur la présentation et l'apparence du contenu - cela devrait être le rôle du CSS (Cascading Style Sheets) et non du HTML.

Utilisez `<strong>` pour signaler qu'un morceau de texte est d'une grande importance. Les navigateurs rendront le texte en gras. 

Et utilisez `<em>` pour signaler que le texte a besoin d'emphase. Les navigateurs rendront le texte en italique. 

Ces éléments ne se concentrent pas sur l'apparence du texte mais fournissent plutôt plus d'informations sur le type de texte qu'ils contiennent.

Comme vous l'avez vu jusqu'à présent, tous les éléments mentionnés fournissent des informations sur le balisage et le type de contenu qu'ils contiennent et créent ainsi des pages plus significatives et une meilleure structure.

Pourquoi écrire du HTML sémantique ? Pour quelques raisons :

- Il améliore l'accessibilité. Lorsque vous concevez et développez des sites web, vous devez garder à l'esprit que vous créez des sites web pour tout le monde. Les personnes malvoyantes dépendent des technologies d'assistance telles que les lecteurs d'écran pour lire le contenu à voix haute. Les personnes ayant d'autres handicaps peuvent dépendre de la navigation au clavier uniquement. Ainsi, apprendre à écrire du HTML accessible vous conduira à créer des pages web plus conviviales.
- Il améliore le SEO (Search Engine Optimisation). L'utilisation d'éléments qui décrivent correctement le contenu aidera votre site web à mieux se classer dans les recherches Google, car le but de votre site web sera plus clair. Les moteurs de recherche aideront votre site à atteindre son public cible qui recherche ce contenu spécifique.

Pour en savoir plus sur le HTML sémantique, consultez les ressources suivantes :

- [Guide du HTML sémantique - 10 alternatives à l'utilisation de divs](https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/)
- [Éléments HTML5 sémantiques expliqués](https://www.freecodecamp.org/news/semantic-html5-elements/)

## Conclusion

Cela marque la fin de notre introduction au HTML. J'espère que vous avez trouvé cet aperçu utile.

Le meilleur endroit pour commencer à apprendre le HTML (et le CSS !) est avec la [Certification de Conception Web Réactive](https://www.freecodecamp.org/learn/2022/responsive-web-design/) de freeCodeCamp.

C'est un programme interactif gratuit, structuré et bien conçu. Vous apprenez de manière pratique en construisant 20 projets. Vous apprendrez le HTML et les techniques modernes de CSS ainsi que les meilleures pratiques d'accessibilité.

Merci d'avoir lu !