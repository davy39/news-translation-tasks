---
title: Nous avons besoin d'un nouveau langage de balisage de documents — voici pourquoi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T16:39:47.000Z'
originalURL: https://freecodecamp.org/news/we-need-a-new-document-markup-language-c22e0ec44e15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ge4Z5bQFJwk5AUA8DjHgNQ.png
tags:
- name: documentation
  slug: documentation
- name: markup
  slug: markup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: writing
  slug: writing
seo_title: Nous avons besoin d'un nouveau langage de balisage de documents — voici
  pourquoi
seo_desc: 'By Christian Neumanns

  Introduction: What’s the Problem?

  There are many document markup languages available already. Wikipedia lists over
  70 variations in its List of document markup languages — among them HTML, Markdown,
  Docbook, Asciidoctor, reStruc...'
---

Par Christian Neumanns

### Introduction : Quel est le problème ?

Il existe déjà de nombreux langages de balisage de documents. Wikipedia répertorie plus de 70 variations dans sa [Liste des langages de balisage de documents](https://en.wikipedia.org/wiki/List_of_document_markup_languages) — parmi eux HTML, Markdown, Docbook, Asciidoctor, reStructuredText, etc.

Pourquoi, alors, le titre de cet article suggère-t-il que nous avons besoin d'_un autre_ ???

Quel est le problème ?

Il existe deux problèmes fondamentaux avec les langages de balisage de documents existants : soit ils ne sont pas faciles à utiliser, soit ils ne sont pas bien adaptés pour écrire des documents complexes, tels que des articles techniques, des manuels utilisateurs ou des livres. Un exemple de « non facile à utiliser, mais adapté pour des documents complexes » serait Docbook. Un exemple de « facile à utiliser, mais non adapté pour des documents complexes » serait Markdown.

Bien sûr, la catégorisation ci-dessus est simpliste. Mais elle devrait servir de bon point de départ pour saisir l'essentiel de cet article qui vise à délimiter le type de problèmes qui se posent en pratique. Vous verrez de nombreux exemples représentatifs de code de balisage qui illustrent ce qui ne va pas, complétés par des liens vers plus d'informations.

Vous découvrirez également un _nouveau_ langage de balisage. De nombreux exemples démontreront comment une nouvelle syntaxe peut conduire à un langage qui est « facile à utiliser et adapté pour des documents complexes ». Une implémentation de _preuve de concept_ est déjà disponible. Plus d'informations à ce sujet plus tard.

### Remarques préliminaires

Veuillez noter :

* Cet article traite des langages de balisage de documents utilisés pour écrire des _documents textuels_, tels que des livres et des articles publiés sur le net. Il existe d'autres langages de balisage utilisés pour décrire des données spécifiques, telles que des formules mathématiques, des images et des informations géographiques, mais ceux-ci sont hors du champ de cet article. Cependant, certaines idées présentées dans cet article pourraient être appliquées à d'autres types de langages de balisage également.
* Cet article se concentre uniquement sur la _syntaxe_ des langages de balisage. Nous ne discuterons pas d'autres aspects qui sont également importants dans le choix d'un langage de balisage approprié, tels que : le support sur votre OS, la facilité d'installation et les dépendances, la chaîne d'outils disponible pour créer des documents finaux, la qualité de la documentation, le prix, le support client/utilisateur, etc.
* Les lecteurs de cet article devraient avoir une certaine expérience de base avec un langage de balisage comme HTML, Markdown, Asciidoctor, ou similaire.
* Les lecteurs qui ne connaissent pas les _nombreux_ avantages des langages de balisage de documents pourraient d'abord vouloir lire :
[Avantages des langages de balisage de documents vs éditeurs WYSIWYG](https://medium.freecodecamp.org/the-advantages-of-document-markup-languages-vs-wysiwyg-editors-829dc8362219) (traitement de texte)

### Inconvénients / Partie 1

Examinons d'abord certains langages de balisage bien connus et jetons un coup d'œil à quelques inconvénients.

#### HTML

HTML est le langage du web. Alors, pourquoi ne pas tout écrire en HTML ? Les raisons de rejeter cette option sont bien connues. Récapitulons-les rapidement.

HTML est fastidieux à écrire. Personne ne veut écrire du code XML à la main, bien que des éditeurs avec support HTML/XML puissent aider.

Certaines tâches d'écriture fréquentes nécessitent un code HTML non trivial.

Supposons que nous voulons afficher une image centrée horizontalement avec une simple bordure noire et un lien. Le code HTML qu'un utilisateur inexpérimenté s'attendrait à fonctionner pourrait ressembler à ceci :

```html
<img src="ball.png" align="center" border="yes" link="http://www.example.com/ball">
```

Mais le code qu'il ou elle doit réellement écrire est fastidieux et il existe différentes façons de le faire. Voici une façon :

```html
<div style="text-align: center">
    <a href="http://www.example.com/ball">
        <img src="ball.png" style="border:1px solid black;">
    </a>
</div>
```

HTML manque de « fonctionnalités de productivité pour les écrivains », telles que :

* Génération automatique d'une table des matières, d'un index, d'un glossaire, etc.
* Variables utilisées pour contenir des valeurs récurrentes
* Division d'un document en différents fichiers

D'autres inconvénients seront montrés plus tard.

#### Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) est un langage de balisage très populaire et léger. Il est facile à apprendre et à utiliser, et bien adapté pour des textes courts et simples, tels que des commentaires dans des forums, des fichiers readme, etc.

Cependant, il souffre des problèmes suivants qui le rendent inadapté pour des documents complexes ou volumineux (par exemple, des articles techniques, des manuels utilisateurs et des livres) :

* Le Markdown original défini par John Gruber manque de nombreuses fonctionnalités attendues par les écrivains, telles que les tableaux (seuls les tableaux HTML intégrés sont supportés), la génération automatique de la table des matières, la coloration syntaxique, la division de fichiers, etc.
* Il n'existe pas de spécification unique et non ambiguë pour Markdown. De nombreuses variantes de Markdown existent, avec des règles différentes et des fonctionnalités différentes supportées. Cela conduit à des problèmes d'incompatibilité lorsque le code de balisage est partagé. [CommonMark](https://commonmark.org/) est une tentative de résoudre ce problème. Cependant, la spécification est énorme et n'est pas encore terminée (au moment de l'écriture, en avril 2019, la version 0.28, datée du 2017-08-01, est la dernière).
* Markdown a des problèmes et des limitations similaires à ceux montrés plus tard dans le chapitre « Inconvénients / Partie 2 ». Ces défauts peuvent rapidement devenir une nuisance lorsque vous utilisez Markdown pour autre chose que des textes courts et simples.

Voici une liste d'articles avec plus d'informations sur les lacunes de Markdown :

* [Pourquoi vous ne devriez pas utiliser « Markdown » pour la documentation](http://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/)
* [Le déclin de Markdown ?](https://www.red-gate.com/simple-talk/blogs/sundown-on-markdown/)
* [Pourquoi Markdown n'est pas mon langage préféré](http://www.wilfred.me.uk/blog/2012/07/30/why-markdown-is-not-my-favourite-language/)

#### Docbook

[Docbook](https://docbook.org/) est un langage de balisage basé sur XML qui utilise des balises sémantiques pour décrire des documents.

Il possède probablement l'ensemble de fonctionnalités le plus complet parmi tous les langages de balisage. Il a été utilisé par de nombreux auteurs, est préinstallé sur certaines distributions Linux, et est supporté par de nombreuses organisations et éditeurs. Docbook a été utilisé avec succès pour créer, publier et imprimer de nombreux documents volumineux de toutes sortes.

Mais il présente les inconvénients suivants :

Il utilise XML et une syntaxe verbeuse. Regardez l'exemple suivant, emprunté à [Wikipedia](https://en.wikipedia.org/wiki/DocBook) :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<book xml:id="simple_book" xmlns="http://docbook.org/ns/docbook" version="5.0">
    <title>Very simple book</title>
    <chapter xml:id="chapter_1">
        <title>Chapter 1</title>
        <para>Hello world!</para>
        <para>I hope that your day is proceeding <emphasis>splendidly</emphasis>!</para>
    </chapter>
    <chapter xml:id="chapter_2">
        <title>Chapter 2</title>
        <para>Hello again, world!</para>
    </chapter>
</book>
```

Aimeriez-vous écrire et maintenir un tel code ?

Comparez maintenant le code ci-dessus avec le suivant, écrit dans un langage de balisage moderne comme Asciidoctor :

```
= Very simple book

== Chapter 1

Hello world!

I hope that your day is proceeding _splendidly_!

== Chapter 2

Hello again, world!
```

Docbook est également complexe, et donc difficile à apprendre et à utiliser.

Le rendu produit par Docbook, en particulier HTML, semble dépassé (voir les exemples sur son site web). Bien sûr, la présentation peut être personnalisée, mais ce n'est pas une tâche facile.

#### LaTeX

[LaTeX](https://en.wikipedia.org/wiki/LaTeX) est un système de composition de haute qualité. Il est largement utilisé dans le milieu universitaire pour créer des documents scientifiques. Il est considéré comme la meilleure option pour écrire des documents PDF contenant de nombreuses formules et équations mathématiques.

Je n'ai jamais utilisé LaTeX moi-même, car je n'écris pas de documents scientifiques — juste des articles et des livres à publier sur le web. Par conséquent, je ne veux pas trop commenter à ce sujet. Cependant, il est important de le mentionner en raison de sa popularité dans le milieu universitaire.

La syntaxe unique de LaTeX me semble verbeuse et un peu complexe. Voici un exemple abrégé de [Wikipedia](https://en.wikipedia.org/wiki/LaTeX#Example) :

```latex
\documentclass{article}
\usepackage{amsmath}
\title{\LaTeX}

\begin{document}
    \maketitle
    \LaTeX{} is a document preparation system ...
    
    % This is a comment
    \begin{align}
        E_0 &= mc^2 \\
        E &= \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}
    \end{align}  
\end{document}
```

L'article [Conversion de (La)TeX vers HTML](https://texfaq.org/FAQ-LaTeX2HTML) indique que la conversion de LaTeX math en HTML est « un défi ».

Certains langages de balisage permettent d'intégrer des extraits LaTeX dans leur code de balisage, ce qui peut être très utile si vous avez besoin de la puissance de LaTeX pour les mathématiques. Il existe d'autres options pour afficher des mathématiques sur le web, telles que [Mathjax](https://www.mathjax.org/) ou [MathML](https://en.wikipedia.org/wiki/MathML) (une norme ISO et partie de HTML5).

### Populaires pour les grands documents

Un nombre impressionnant de langages de balisage ont émergé. Beaucoup d'entre eux utilisent une syntaxe similaire à Markup, et sont donc faciles à apprendre et à utiliser. Certains ont plus de fonctionnalités que Markdown et sont même extensibles. Cependant, dès que nous commençons à écrire des documents complexes, les cas particuliers et les limites diminuent la joie initiale de les utiliser.

Deux langages de balisage populaires utilisés pour les grands documents sont Asciidoctor (une version améliorée de [Asciidoc](https://en.wikipedia.org/wiki/AsciiDoc)), et [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) (une version améliorée de StructuredText). Nous allons les examiner bientôt.

### Langage de balisage pratique (PML)

Avant de passer à la partie la plus intéressante de cet article, permettez-moi de présenter brièvement le nouveau langage de balisage que j'ai déjà mentionné dans l'introduction.

Le langage s'appelle **_Practical_** _Markup Language (PML)_.

> « adapté aux besoins d'une situation particulière de manière utile ; aidant à résoudre un problème ou une difficulté ; efficace ou approprié »

> — définition de « practical » dans le dictionnaire Cambridge

J'ai commencé le [projet PML](http://www.practical-programming.org/pml/index.html) il y a quelques mois parce que je n'ai pas pu trouver un langage de balisage qui soit facile à utiliser _et_ bien adapté pour les grands documents complexes, tels qu'un manuel utilisateur.

Dans la section suivante, nous examinerons des exemples de code de balisage écrits en PML, comparés à du code écrit dans d'autres langages. Commençons donc par mentionner deux règles de syntaxe PML de base nécessaires pour comprendre les exemples à venir.

Un document PML est un arbre de nœuds (similaire à un document XML/XHTML). Chaque nœud commence par un `{`, suivi d'un nom de balise. Chaque nœud se termine par un `}`. Un nœud peut contenir du texte ou des nœuds enfants.

Par exemple, voici un nœud contenant du texte qui sera rendu en italique :

```
{i bright}
```

Ce nœud commence par `{i`, et se termine par `}`. `i` est le nom de la balise. Dans ce cas, `i` est une abréviation pour `italic`, ce qui signifie que le contenu du nœud sera rendu en _italique_. Le contenu de ce nœud est le texte `bright`. Le code de balisage PML ci-dessus sera rendu comme :  
 _bright_

Certains nœuds ont des attributs, utilisés pour spécifier des propriétés supplémentaires du nœud (en plus de son nom de balise).

Par exemple, le titre d'un chapitre est défini avec l'attribut `title`, comme suit :

```
{chapter title=A Nice Surprise
    Once upon a time ...
}
```

Il n'y a pas grand-chose à dire de plus sur le concept de base de la syntaxe PML. Pour plus d'informations et une description des fonctionnalités non utilisées dans cet article, veuillez consulter le [Manuel de l'utilisateur PML](http://www.practical-programming.org/pml/docs/User_Manual/PML_User_Manual.html).

Vous pouvez télécharger et essayer une implémentation gratuite de PML. Mais veuillez noter : PML est un _travail en cours_. Il manque des fonctionnalités, vous pourriez rencontrer des bugs, et la compatibilité ascendante n'est actuellement pas garantie.

J'utilise PML moi-même pour écrire tous mes documents web, comme cet article. Pour des liens vers plus d'exemples concrets, veuillez visiter la [FAQ](http://www.practical-programming.org/pml/about/faq.html#examples).

### Inconvénients / Partie 2

Dans cette section, nous examinerons des exemples qui révèlent _certains_ problèmes rencontrés avec les langages de balisage. Ce n'est en aucun cas une énumération exhaustive de tous les problèmes et cas particuliers. Le but est simplement de montrer quelques exemples qui démontrent le type d'inconvénients et de limites rencontrés dans le monde réel.

Pour chaque exemple, le code de balisage sera montré en [HTML](https://www.w3.org/TR/html/), [Asciidoctor](https://asciidoctor.org/), [reStructuredText](http://docutils.sourceforge.net/rst.html), et [PML](http://www.practical-programming.org/pml/).

Si vous souhaitez essayer du code, vous pouvez utiliser les testeurs en ligne suivants (pas besoin d'installer quoi que ce soit sur votre PC) :

* [HTML](https://www.w3schools.com/tryit/)
* [Asciidoctor](https://asciidoclive.com)
* [reStructuredText](http://rst.ninjs.org)

Un testeur en ligne pour PML n'est pas encore disponible. Vous devez installer PML sur un PC Windows si vous souhaitez l'essayer.

### Styles de police

Les styles de police (_italique_, **gras**, `monospace`, etc.) sont souvent utilisés dans tous types de documents, donc un bon support est essentiel.

Mais comme nous allons le voir, des surprises et des limites peuvent émerger dès que nous devons traiter des cas non triviaux. Examinons _certains_ exemples pour illustrer cela.

### Partie d'une phrase en italique

Supposons que nous voulons écrire :  
 Ils l'ont appelé _Harmonic States_, un bon nom.

C'est un cas trivial, et tous les langages le supportent.

**HTML** :

```
They called it <i>Harmonic States</i>, a good name.
```

**Asciidoctor** :

```
They called it _Harmonic States_, a good name.
```

**reStructuredText** :

```
They called it *Harmonic States*, a good name.
```

**PML** :

```
They called it {i Harmonic States}, a good name.
```

### Partie d'un mot en italique

Nous voulons écrire :  
 Elle a _dé_ballé le défi en premier.

**HTML** :

```
She <i>un</i>wrapped the challenge first.
```

**Asciidoctor** :

```
She __un__wrapped the challenge first.
```

Notez que nous devons utiliser deux underscores. L'utilisation d'un seul underscore (comme dans le premier exemple) donnerait :  
 Elle _un_wrapped le défi en premier.

**reStructuredText** :

```
She *un*\wrapped the challenge first.
```

Notez que la lettre w doit être échappée (précédée d'un backslash) pour des raisons expliquées [ici](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#character-level-inline-markup). Si la lettre n'est pas échappée, un avertissement est affiché et le résultat est :  
 Elle *un*wrapped le défi en premier.

**PML** :

```
She {i un}wrapped the challenge first.
```

### Texte en gras et italique

Nous voulons écrire :  
 Ils étaient tous **_totalement stupéfaits_**.

**HTML** :

```
They were all <b><i>totally flabbergasted</i></b>.
```

**Asciidoctor** :

```
They were all *_totally flabbergasted_*.
```

**reStructuredText** :

La combinaison de gras et d'italique n'est pas supportée dans reStructuredText, mais il existe quelques [solutions de contournement compliquées](https://stackoverflow.com/questions/11984652/bold-italic-in-restructuredtext).

**PML** :

```
They were all {b {i totally flabbergasted}}.
```

### Exemple réel

Voici un exemple inspiré d'un utilisateur d'Asciidoctor qui a [demandé](https://github.com/asciidoctor/asciidoctor/issues/2020) comment afficher :  
 **_id** _optionnel_.

Rendons l'exercice un peu plus intéressant en affichant également :  
 __id_ **optionnel**.

**HTML** :

```
<b>_id</b> <i>optional</i>
<i>_id</i> <b>optional</b>
```

Aucune surprise ici. Cela fonctionne simplement comme prévu.

**Asciidoctor** :

Tentative intuitive :

```
*_id* _optional_
__id_ *optional*
```

La première ligne ne fonctionne pas, elle produit :  
 **_id_** __optionnel_

Cependant, la deuxième ligne fonctionne, ce qui est un peu contre-intuitif.

Si le texte normal inclut un caractère qui est également utilisé pour le balisage (dans notre cas le `_` précédant `id`), alors le caractère doit être échappé. C'est une règle fondamentale dans presque tous les langages de balisage. Par exemple, en HTML, un `&`lt; doit être échappé avec `&`lt;. De nombreux langages (y compris Asciidoctor et PML) utilisent un préfixe backslash (par exemple, \r) pour échapper. Donc, réécrivons le code :

```
*\_id* _optional_
_\_id_ *optional*
```

Cela ne fonctionne pas dans Asciidoctor. Cela produit  
 **_id** _optionnel_  
et  
\_id **optionnel**

Voici une version correcte, comme suggéré dans une réponse à la question de l'utilisateur :

```
*pass:[_]id* _optional_
_pass:[_]id_ *optional*
```

Une autre réponse suggère cette solution :

```
*_id* __optional__
___id__ *optional*
```

Plus de cas particuliers sont documentés dans les chapitres [Unconstrained formatting edge cases](https://asciidoctor.org/docs/user-manual/#unconstrained-formatting-edge-cases) et [Escaping unconstrained quotes](https://asciidoctor.org/docs/user-manual/#escaping-unconstrained-quotes) du manuel de l'utilisateur Asciidoctor.

**reStructuredText** :

```
**_id** *optional*
*_id* **optional**
```

Il n'y a pas de problème ici, car le caractère `_` n'est pas utilisé dans reStructuredText pour définir le balisage.

Cependant, supposons que nous voulions écrire :  
 _*id*_ ***optionnel***.

Voici le code :

```
*\*id\** ***optional***
```

Notez que les `*` dans `id` doivent être échappés, mais les `*` dans `optional` n'ont pas besoin de l'être.

**PML** :

```
{b _id} {i optional}
{i _id} {b optional}
```

### Styles de police imbriqués

Les styles de police imbriqués de même type (par exemple, `<i>...<i>..`.</i>...</i>) se produisent rarement dans les textes écrits par des humains, mais ils pourraient être plus ou moins fréquents dans le code de balisage généré automatiquement. S'ils ne sont pas supportés, l'outil qui génère le code de balisage devient plus compliqué à implémenter, car il doit suivre les styles de police qui sont déjà actifs, afin d'éviter de les imbriquer.

Alors, comment cela est-il supporté dans les différents langages ?

**HTML** :

```
<i>This is <i>excellent</i>, isn't it?</i>
```

Aucun problème, cela produit  
_This is excellent, isn't it?_

**Asciidoctor** :

```
_This is _excellent_, isn't it?_
```

Le code ci-dessus est évidemment ambigu : les italiques sont-ils imbriqués ou voulons-nous mettre en italique « This is » et «, isn't it? ». Lorsque je l'ai testé, le résultat n'était ni l'un ni l'autre :  
_This is _excellent_, isn't it?_

Pour autant que je sache, Asciidoctor ne supporte pas les styles de police imbriqués de même type.

**reStructuredText** :

La spécification reStructuredText [indique](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#inline-markup) : « Le balisage en ligne ne peut pas être imbriqué. » Cependant, aucun message d'erreur n'est affiché si le balisage est imbriqué, et le résultat est non spécifié.

**PML** :

```
{i This is {i excellent}, isn't it?}
```

Les styles de police de même type peuvent être imbriqués dans PML. Le code ci-dessus donne :  
_This is excellent, isn't it?_

### Chapitres imbriqués

Supposons que nous écrivons un article intitulé « New Awesome Product » qui contient quatre chapitres. La structure est la suivante :

```
New Awesome Product
    Introduction
    More features
    Faster
    Less resources
```

Plus tard, nous décidons d'insérer le chapitre « Advantages » comme parent des trois derniers chapitres. La structure devient maintenant :

```
New Awesome Product
    Introduction
    Advantages
        More features
        Faster
        Less resources
```

Quels sont les _changements_ nécessaires dans le code de balisage pour passer de la version 1 à la version 2 ? Pouvez-vous simplement insérer le code pour un nouveau chapitre ? Voyons cela.

**HTML** :

![Image](https://cdn-media-1.freecodecamp.org/images/PoEYqgtazrmE2KEXHHEdSVyBd1XCISQurRxT)

Remarque : Les _changements_ de code sont affichés en gras.

Comme montré ci-dessus, en plus d'insérer le nouveau chapitre, nous devons changer le balisage pour les trois chapitres enfants : `h2` doit être changé en `h3`.

**Asciidoctor** :

![Image](https://cdn-media-1.freecodecamp.org/images/h6RYuEiJ5YHGqr6yjJ7UKEivRxOfhNKbc9Fs)

Encore une fois, nous devons changer le balisage pour les trois chapitres enfants : `==` doit être changé en `===`

Remarque : Les lignes vides entre les chapitres sont requises, sinon le document n'est pas rendu correctement.

**reStructuredText** :

![Image](https://cdn-media-1.freecodecamp.org/images/iLno1NIDCRQW-AtE7E1R-Bp6lToSFfbQETlj)

Le balisage pour les trois chapitres enfants doit être changé : toutes les occurrences de `=` doivent être changées en `-`

Les règles non triviales pour les sections de reStructuredText peuvent être consultées [ici](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections).

**PML** :

![Image](https://cdn-media-1.freecodecamp.org/images/-z7E6Sv0f4-ZPQlj9ldRKMTiFLdzBjbjNCTF)

Dans PML, il n'est pas nécessaire de changer le code des trois chapitres enfants.

**Conclusion** :

Dans tous les langages, sauf PML, le code de balisage de tous les chapitres enfants doit être adapté si un chapitre parent est inséré.

Ce n'est pas un problème récurrent dans le cas d'articles courts avec peu de chapitres. Mais imaginez que vous écrivez votre prochain grand article ou livre avec de nombreux chapitres et des changements fréquents. Maintenant, la nécessité de mettre à jour manuellement les chapitres enfants peut rapidement devenir une tâche fastidieuse, ennuyeuse et sujette aux erreurs.

Remarque : Asciidoctor fournit une variable `leveloffset` qui peut être utilisée pour changer le niveau des chapitres. Cela peut être utile dans certains cas, mais cela crée également une complexité supplémentaire inutile, comme on peut le voir [ici](https://github.com/asciidoctor/asciidoctor/issues/530) et [ici](https://github.com/asciidoctor/asciidoctor/issues/1616).

Un type de problème plus sérieux peut survenir dans la situation suivante : imaginez un ensemble de différents documents qui partagent certains chapitres communs. Pour éviter la duplication de code, les chapitres communs sont stockés dans différents fichiers, et une directive `insert file` est utilisée dans les documents principaux. Cela fonctionne bien tant que les niveaux de tous les chapitres communs sont les mêmes dans tous les documents. Mais des problèmes émergent si ce n'est pas le cas.

Il est également utile de mentionner que HTML, Asciidoctor et reStructuredText ne nous protègent pas contre les mauvaises hiérarchies de chapitres. Par exemple, vous n'obtenez pas d'avertissement ou d'erreur si un chapitre de niveau 2 contient un chapitre enfant direct de niveau 4.

Dans un langage comme PML, les problèmes ci-dessus n'existent tout simplement pas, car le niveau n'est pas spécifié dans le code de balisage. Tous les chapitres (de n'importe quel niveau) sont définis avec la même syntaxe unique. La structure arborescente des chapitres (c'est-à-dire le niveau de chaque chapitre) est automatiquement définie par l'analyseur. Et les mauvaises hiérarchies dans le code de balisage, telles qu'un `}` manquant pour fermer un chapitre, sont signalées par un message d'erreur.

### Listes

Dans Asciidoctor, le type de problèmes que nous avons vus avec les hiérarchies de chapitres peut également survenir avec les hiérarchies de listes (par exemple, des listes qui contiennent des listes). La raison est la même que pour les chapitres : les [listes Asciidoctor](https://asciidoctor.org/docs/user-manual/#nested) utilisent un code de balisage différent pour spécifier explicitement le niveau des éléments de liste (`*` pour le niveau 1, `**` pour le niveau 2, etc.). De plus, il existe un certain nombre de complications dont vous devez être conscient lorsque vous travaillez avec un [contenu de liste complexe](https://asciidoctor.org/docs/user-manual/#complex-list-content).

Dans reStructuredText, les [listes imbriquées](https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext) sont créées en utilisant l'indentation et les lignes vides. Cela fonctionne bien pour les listes imbriquées simples, mais crée d'autres problèmes dans des cas plus complexes (non discutés ici). L'utilisation d'espaces blancs (par exemple, des lignes vides et de l'indentation) pour définir la structure dans le code de balisage est une mauvaise idée, comme nous le verrons bientôt.

Dans HTML et PML, les problèmes ci-dessus n'existent pas avec les listes car la syntaxe pour les nœuds parents et enfants est la même.

### Espaces blancs et indentation

À première vue, utiliser des espaces blancs pour définir la structure semble être une bonne idée. Regardez l'exemple suivant :

```
parent
    child 1
    child 2
```

La structure est très facile à lire _et_ à écrire. Aucun caractère spécial de balisage bruyant n'est nécessaire.

Il est donc tentant pour les concepteurs de langages de balisage d'utiliser les espaces blancs comme un moyen simple de définir la structure. Malheureusement, cela fonctionne bien seulement pour les structures simples, et présente d'autres inconvénients que nous verrons bientôt.

Par conséquent, une règle simple mais importante doit être appliquée dans les langages de balisage conçus pour bien fonctionner avec du contenu complexe :

> « Les espaces blancs ne changent pas la structure ou la sémantique du document. »  
>   
> — règle des espaces blancs non significatifs

Que signifie cela ?

Tout d'abord, définissons les _espaces blancs_ : les espaces blancs sont tout ensemble d'un ou plusieurs espaces consécutifs, tabulations, nouvelles lignes et autres caractères Unicode qui représentent de l'espace.

Dans notre contexte, la règle ci-dessus signifie que :

À l'intérieur du texte, un ensemble de _plusieurs_ (c'est-à-dire plus d'un) caractères d'espace blanc est traité de la même manière qu'un _seul_ caractère d'espace.

Par exemple, ce code :

```
a beautiful
    flower
```

… est identique à celui-ci :

```
a beautiful flower
```

Entre les éléments structurels, un ensemble de caractères d'espace blanc est insignifiant.

Par exemple, ce code :

```
<table>

    <tr>
```

… est identique à celui-ci :

```
<table><tr>
```

Un cas spécial d'espace blanc est l'_indentation_ (espace blanc en début de ligne). La règle ci-dessus implique que l'indentation est également insignifiante. L'indentation ne change pas le résultat du document final.

Appliquer la règle des _espaces blancs non significatifs_ est important, car cela conduit à des avantages significatifs :

* Il n'est pas nécessaire d'apprendre, d'appliquer et de s'inquiéter des règles complexes d'espaces blancs (voir les exemples ci-dessous).  
Violer la règle des _espaces blancs non significatifs_ dans une spécification de balisage ajoute une complexité inutile et peut conduire à un code de balisage laid, sujet aux erreurs et difficile à maintenir, en particulier dans le cas des listes imbriquées.
* Les espaces blancs peuvent être librement utilisés par les auteurs pour formater le code de balisage de manière plus compréhensible, présentable et attrayante (pretty printing). Par exemple, les listes (et les listes de listes) peuvent être indentées pour afficher leur structure de manière visuellement claire et maintenable, sans le risque de changer la structure sous-jacente.
* Les blocs de texte peuvent être copiés/collés sans avoir besoin d'adapter les espaces blancs.
* Si des blocs de texte partagés (stockés dans différents fichiers) sont importés dans plusieurs documents avec différentes structures, il n'y a pas de risque de changer ou de casser la structure.
* Il n'y a pas de comportement inattendu ou obscur si les espaces blancs ne sont pas visibles pour les lecteurs humains. Quelques exemples :  
- un mélange de caractères d'espace blanc, tels que des espaces et des tabulations, en particulier lorsqu'ils sont utilisés pour indenter du code  
- des espaces blancs à la fin d'une ligne  
- des espaces blancs dans les lignes vides  
- les personnes malvoyantes (aveugles) qui ne peuvent pas lire les espaces blancs  
Remarque : Pour atténuer la douleur, certains éditeurs fournissent un mode _affichage des espaces blancs_.
* Les outils qui génèrent du code de balisage, ainsi que les analyseurs de balisage, sont généralement plus faciles à créer.
* Dans certaines situations, il est utile de réduire les espaces blancs au minimum (par exemple, pas de nouvelles lignes), afin d'économiser de l'espace de stockage et d'améliorer les performances.

Si vous voulez quelques exemples démontrant le type de problèmes techniques qui surviennent si les espaces blancs sont significatifs, vous pouvez lire :

* [Quels sont les inconvénients de l'indentation par espaces blancs plutôt que l'utilisation d'accolades ?](https://www.quora.com/What-are-the-downsides-to-whitespace-indentation-rather-than-requiring-curly-braces)
* [Syntaxe F# : indentation et verbosité](https://fsharpforfunandprofit.com/posts/fsharp-syntax/)
* [Problème dans nodeca/js-yaml](https://github.com/nodeca/js-yaml/issues/80)

Alors, comment les espaces blancs sont-ils gérés dans les langages que nous discutons dans cet article ?

**HTML** :

HTML applique la règle des _espaces blancs non significatifs_.

Pour une explication approfondie, consultez cet excellent article écrit par Patrick Brosset : [Quand les espaces blancs comptent-ils en HTML ?](https://medium.com/@patrickbrosset/when-does-white-space-matter-in-html-b90e8a7cdd33).

**Asciidoctor** :

Dans Asciidoctor, les espaces blancs sont significatifs dans certains cas.

Cela peut conduire à des comportements surprenants et à des problèmes sans solution facile ou satisfaisante. Certains exemples peuvent être vus [ici](https://github.com/asciidoctor/asciidoctor/issues/686) et [ici](https://github.com/asciidoctor/asciidoctor/issues/623).

**reStructuredText** :

reStructuredText a des règles d'espaces blancs qui sont « un peu surprenantes ».

Par exemple, écrire `*very*` donne _very_ (texte en italique, comme prévu). Cependant, `* very*` donne * very* (pas d'italique !), à cause de l'espace blanc précédant « very ». Pour comprendre pourquoi, la réponse peut être trouvée dans le chapitre [Whitespace](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#whitespace) de la spécification.

**PML** :

Similaire à HTML, PML applique la règle des _espaces blancs non significatifs_.

Il y a une exception : pour des raisons pratiques, une ligne vide entre deux blocs de texte entraîne une rupture de paragraphe. Cela signifie qu'au lieu d'écrire :

```
{p text of paragraph 1}
{p text of paragraph 2}
```

… nous pouvons simplement écrire :

```
text of paragraph 1

text of paragraph 2
```

Remarque : Parfois, les espaces blancs _sont_ significatifs dans le texte. Par exemple, les espaces blancs doivent être préservés dans les exemples de code source. Ou, dans le texte brut, plusieurs espaces consécutifs ou nouvelles lignes doivent être préservés dans le document final. Tous les langages supportent cela. Cependant, dans reStructuredText, il n'est pas toujours évident de le faire, comme le montre [ici](https://stackoverflow.com/questions/51198270/how-do-i-create-a-new-line-with-restructuredtext).

### Autres inconvénients

Comme nous l'avons déjà vu, certains langages de balisage utilisent systématiquement des balises d'ouverture et de fermeture. Un exemple serait `<i>` et `</i>` en HTML. Tous les langages basés sur XML, ainsi que PML, appartiennent à cette classe de langages.

Sans entrer dans les détails, voici quelques inconvénients qui peuvent survenir dans les langages qui n'utilisent _pas_ (ou pas toujours) des paires de balises d'ouverture/fermeture distinctes (par exemple, Markdown, Asciidoctor et reStructuredText) :

**Support de l'éditeur**  
Créer un bon support d'éditeur fiable est plus difficile à développer. Des exemples de fonctionnalités utiles de l'éditeur sont :

* la coloration syntaxique pour le code de balisage
* la complétion du code de balisage
* la visualisation des paires de marques de début/fin de bloc (par exemple, `{` et son `}` correspondant)
* le repliement/déploiement de bloc  
Dans le cas des langages qui utilisent des balises d'ouverture/fermeture distinctes, les deux dernières fonctionnalités fonctionnent directement dans certains éditeurs. Par exemple, PML utilise `{` et `}` pour les limites des nœuds. Cela est également utilisé dans de nombreux langages de programmation (C, Java, Javascript, etc.) et donc les fonctionnalités de bloc implémentées pour les langages de programmation fonctionneront également pour PML.

**Validation du document**  
Moins d'erreurs de syntaxe et de structure peuvent être détectées automatiquement. Cela peut conduire à plus de temps passé à déboguer des documents. Ou, pire encore, il pourrait y avoir des erreurs silencieusement ignorées qui se retrouvent dans une sortie incorrecte (Ai-je vraiment manqué le bloc d'avertissement sur la page 267 de mon livre de 310 pages ?).

**Analyseurs**  
Il est plus difficile de créer des analyseurs (c'est-à-dire des programmes qui lisent le code de balisage) qui fonctionnent bien dans tous les cas. Si différents analyseurs lisent le même code de balisage, il y a un risque accru d'obtenir des résultats différents pour les cas particuliers.

**Code de balisage généré automatiquement**  
Les outils qui génèrent du code de balisage de manière programmatique sont plus difficiles à créer. Par exemple, si les espaces blancs sont significatifs, ou si les styles de police ne peuvent pas être imbriqués, alors un état supplémentaire doit être mis à jour et suivi, afin de respecter ces règles.

### Mon expérience personnelle

Lorsque j'ai commencé à écrire des documents techniques il y a quelques années, j'utilisais Docbook. Il m'a fallu un certain temps pour l'apprendre, mais après cela, je n'ai jamais buté sur quelque chose que je ne pouvais pas faire. Docbook est puissant. Cependant, je n'aimais pas taper du code XML verbeux. J'ai essayé quelques éditeurs XML, mais j'ai abandonné. Finalement, j'ai simplement écrit des blocs de texte complets non formatés dans Notepad++, puis j'ai orné le texte avec le code de balisage nécessaire. C'était frustrant et chronophage. De plus, je n'ai pas pu trouver une feuille de style qui produisait de beaux documents web, et je n'avais pas la patience, la motivation et l'expérience pour bidouiller de gros fichiers CSS complexes et les adapter.

Plus tard, j'ai découvert Asciidoctor. Quel soulagement. Tout était tellement plus simple et les documents web étaient magnifiques, prêts à l'emploi. La documentation d'Asciidoctor est excellente, et je pense que la communauté est utile et active. Cependant, lorsque j'ai commencé à écrire des documents plus complexes et plus volumineux, j'ai dû faire face à des problèmes similaires à ceux décrits dans les sections précédentes. À un moment donné, j'ai dû développer un pré- et post-processeur spécifique pour résoudre un problème pour lequel je n'ai pas pu trouver de solution dans Asciidoctor/Gitbook.

Une question intrigante a émergé : « Pourquoi ces problèmes n'existent-ils pas dans Docbook ? ».

Pour faire court, j'ai conclu que nous avions besoin d'une nouvelle syntaxe de balisage. Les points clés du succès seraient :

* facile à apprendre : peu de règles, simples, cohérentes et prévisibles (pas d'exceptions)
* facile à écrire et à lire
* documents bien structurés sans ambiguïtés
* suffisamment puissant pour créer de grands documents complexes sans avoir besoin de « règles spéciales, astuces ou solutions de contournement »

Après une période d'investigation, de réflexion, de programmation, de test et d'amélioration, le [Practical Markup Language (PML)](http://www.practical-programming.org/pml/index.html) est né. Depuis lors, je n'ai plus jamais regardé en arrière. Aujourd'hui, j'écris tous mes documents web en PML (y compris cet article).

Bien sûr, lorsque j'ai commencé à créer PML, c'était pour couvrir mes propres besoins. Je suis donc probablement partial. Espérons que cet article contient suffisamment d'exemples factuels, mais je vous encourage à laisser un commentaire si vous voyez quelque chose de faux, d'injuste ou de manquant. J'apprécie les retours constructifs de toute sorte, et je mettrai à jour l'article si nécessaire.

### Conclusion

Comme démontré dans cet article, un bon nombre de problèmes rencontrés avec les langages de balisage de documents existants disparaissent avec la syntaxe PML.

Maintenant, nous devrions nous réunir pour améliorer PML et le rendre plus puissant, afin qu'il couvre plus de cas d'utilisation et que plus de personnes puissent en bénéficier.

Veuillez aider à faire connaître PML. Ou essayez PML et envoyez des retours, afin que nous sachions ce qui doit être affiné. Votre voix compte !

La vision est de créer le meilleur langage de balisage de documents possible et tous les outils nécessaires, afin que les écrivains puissent se concentrer sur l'écriture et profiter de la création de beaux documents en un minimum de temps — sans se soucier de la complexité inutile.