---
title: Un guide sur les extraits de code de Sublime Text
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T17:49:42.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-preserving-your-wrists-with-sublime-text-snippets-7541662a53f2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m0_LP6bcNEN_ZPBad6ekfA.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Snippet
  slug: snippet
- name: Web Development
  slug: web-development
seo_title: Un guide sur les extraits de code de Sublime Text
seo_desc: 'By Jimmy Zhang

  I recently switched jobs, which involves a lot of acclimation: new coworkers to
  befriend, new terms to learn, a new development environment to internalize. But
  most of all, the switch came with a change in programming languages, away f...'
---

Par Jimmy Zhang

J'ai récemment changé de travail, ce qui implique beaucoup d'acclimatation : de nouveaux collègues à se lier d'amitié, de nouveaux termes à apprendre, un nouvel environnement de développement à assimiler. Mais surtout, ce changement s'est accompagné d'un changement de langages de programmation, loin de l'esthétique soignée de Python, et directement dans le monde anguleux et courbé de JavaScript.

Alors que je continuais à mal placer les crochets et à omettre les parenthèses, j'ai cherché quelque chose qui m'aiderait à naviguer dans ce territoire inconnu. Heureusement, j'ai découvert les extraits de code de Sublime Text.

J'adore les extraits de code de Sublime Text parce qu'ils réduisent les définitions fastidieuses à quelques touches, comme ceci :

### Aperçu

Les extraits de code de Sublime Text accélèrent l'acte d'écrire du code en fournissant un moyen rapide d'insérer des blocs de texte qui apparaissent répétitivement dans un projet. Ils sont à la fois faciles à comprendre et simples à écrire, ce qui en fait un excellent outil pour gagner du temps et éliminer les erreurs pendant le développement.

Un extrait de code associe un mot déclencheur à un bloc de texte prédéfini, les deux étant définis par vous. Pour invoquer l'extrait de code, tapez le mot déclencheur et appuyez sur `tab`. Cette action simple développe le mot déclencheur en bloc de texte mappé — avec autant de crochets, parenthèses et points-virgules que nécessaire, toujours appariés et dans le bon ordre.

**Note :** Les exemples donnés ci-dessous s'appliquent principalement à JavaScript et React, mais les informations sur les extraits de code peuvent être appliquées à n'importe quel langage de programmation ou framework.

### Création d'extraits de code

Pour créer un nouvel extrait de code dans Sublime Text 3, allez à :

```
Outils -> Développeur -> Nouveau snippet...
```

Cela ouvre une nouvelle fenêtre contenant un nouveau modèle de snippet, qui ressemble à ceci :

Il y a quatre parties à un extrait de code. Bien qu'une seule partie soit requise, il est recommandé de définir les quatre.

#### **1) Le Contenu (Ligne 3) : Requis**

```
<content><![CDATA[  Bonjour, ${1:ceci} est un ${2:snippet}.]]></content>
```

Définissez le bloc de texte à développer par l'extrait de code en modifiant la ou les lignes entre les balises `<![CDATA[` et `]]>`. (Désormais, le bloc de texte qui est développé après l'invocation de l'extrait de code sera appelé le _contenu_ de l'extrait de code).

Vous remarquerez la présence de mots entourés d'un signe dollar, d'accolades, de chiffres et précédés d'un chiffre. Ce balisage optionnel spécifie un **marqueur de champ**, qui contrôle la position du curseur après l'invocation de l'extrait de code.

Après le développement du contenu, le curseur se déplace automatiquement vers le premier marqueur de champ (`${1:ceci}` ci-dessus). Appuyer à nouveau sur tab déplace le curseur vers le marqueur de champ numéroté suivant, ou à la fin du contenu de l'extrait de code s'il n'y a plus de champs (voir **astuce pro** ci-dessous).

Le texte après le deux-points dans un marqueur de champ est optionnel. S'il est spécifié, il est automatiquement sélectionné dans le cadre du déplacement du curseur, ce qui signifie qu'il peut être supprimé en un seul geste. Cela rend le texte après le deux-points idéal pour les valeurs "placeholder" qui fournissent des indications sur ce qui doit être rempli, ou pour les valeurs par défaut optionnelles, comme le champ `isRequired` dans l'exemple ci-dessous.

**Astuce pro**
Utilisez le marqueur de champ `$0` (le marqueur de sortie) pour définir explicitement où le curseur sortira après que tous les marqueurs de champ aient été parcourus. Cela est utile si vous souhaitez réassigner la touche `tab` à la complétion automatique après l'invocation de l'extrait de code. Pour ce faire, placez le marqueur de sortie immédiatement après le premier marqueur de champ, comme ceci : `${1:exemple}$0`

#### **2 : Le Mot Déclencheur (Ligne 6) : Optionnel**

```
<tabTrigger>bonjour</tabTrigger>
```

Les mots déclencheurs courts et mnémoniques fonctionnent le mieux. Par exemple, le paquet [Babel React Snippet](https://github.com/babel/babel-sublime-snippets) associe `cwm` à `componentWillMount` et `cwr` à `componentWillReceiveProps`.

Les mots déclencheurs sont optionnels car il existe une autre façon d'invoquer les extraits de code, que nous aborderons dans la section Utilisation avancée.

#### **3 : Un Contexte (Ligne 8) : Optionnel**

```
<scope> source: python </scope>
```

Les contextes limitent où votre extrait de code peut être invoqué, améliorant la précision et évitant les collisions. Par exemple, avec les contextes, le même mot déclencheur peut avoir des significations différentes pour différents langages de programmation.

Ce [gist](https://gist.github.com/J2TeaM/a54bafb082f90c0f20c9) liste comment définir des contextes pour une longue liste de langages de programmation, mais les contextes sont capables de beaucoup plus. Nous aborderons les contextes plus en détail dans la section Utilisation avancée.

#### **4 : Une Description (Ligne 10) : Optionnel**

```
<description> description de démonstration </description>
```

Pour une raison quelconque, la balise de description n'apparaît pas dans le modèle de création de snippet. Cependant, en fournir une sera utile.

Les extraits de code apparaissent dans le menu de complétion automatique de Sublime Text, avec une phrase descriptive. Sans description, cette phrase est par défaut le nom de fichier de l'extrait de code, ce qui n'est pas garanti d'avoir suffisamment de contexte lorsque plusieurs extraits de code partagent le même préfixe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6kQO9TXQwXs0NcSqqFx1sw.png)
_Les descriptions m'aident à démêler mes extraits de code d'importation_

**Astuce pro**
Créez un raccourci clavier pour créer rapidement un nouvel extrait de code. Allez dans `Préférences -> Raccourcis clavier` et ajoutez la ligne suivante au fichier de configuration "Utilisateur" (bien sûr, remplacez cmd+alt+n par la combinaison qui vous convient le mieux) :

```
{ "keys": ["cmd+alt+n"], "command": "new_snippet" }
```

### Enregistrement des extraits de code

Après avoir créé votre extrait de code, assurez-vous de l'enregistrer dans un fichier se terminant par `sublime-snippet`. Sur Mac, les extraits de code créés par l'utilisateur sont enregistrés à l'emplacement suivant :

```
~/Library/Application Support/Sublime Text 3/Packages/User
```

La création d'un nouvel extrait de code via l'élément de menu ou le raccourci clavier invite automatiquement cet emplacement lors de l'enregistrement.

### Utilisation avancée

#### Variables d'environnement

Nous avons couvert les quatre aspects de la création d'un extrait de code statique. Cependant, il est possible de créer des extraits de code dynamiques grâce à l'utilisation de variables d'environnement, qui contiennent des références au contexte dans lequel un extrait de code a été invoqué.

Le contexte est un terme vague, alors consultez la [Documentation des extraits de code de Sublime Text](http://docs.sublimetext.info/en/latest/extensibility/snippets.html#environment-variables) pour un tableau des variables d'environnement et leurs significations exactes.

Pour un exemple de l'utilisation des variables d'environnement, mon équipe suit une convention où la feuille de style d'un composant est enregistrée sous le même nom de fichier que le composant, et reçoit une extension `.scss`.

Le fichier du composant peut alors tirer parti de cette convention avec un extrait de code utilisant la variable d'environnement `$TM_FILENAME`.

```
<content><![CDATA[  import styles from './$TM_FILENAME${1:}scss']]></content>
```

La variable d'environnement `$TM_SELECTED_TEXT` ou `$SELECTION` sert un but plus général. Vous souvenez-vous lorsque j'ai mentionné qu'il y avait une autre façon d'invoquer les extraits de code ? Au lieu de taper le mot déclencheur et d'appuyer sur `tab`, vous pouvez également invoquer les extraits de code via la Palette de commandes.

Sur Mac, appuyez sur `cmd+shift+p` pour faire apparaître la Palette, tapez 'Snippet' et sélectionnez l'extrait de code souhaité dans le menu déroulant. Cette approche détournée présente un avantage majeur — il est possible d'invoquer un extrait de code avec un bloc de texte sélectionné, et pour que ce texte soit inclus dans le contenu de l'extrait de code. Cela vous permet de créer des extraits de code "d'enveloppement", qui enveloppent le texte sélectionné avec une clause if, par exemple.

**Astuce pro**
Les [raccourcis d'extension de sélection](http://docs.sublimetext.info/en/latest/editing/editing.html?highlight=selection#other-ways-of-selecting-text) sont excellents pour sélectionner rapidement du texte à envelopper avec des extraits de code comme celui ci-dessus.

#### Contextes avancés

Nous avons parlé de limiter les extraits de code à certains fichiers de code source, mais les extraits de code ont souvent des contextes plus granulaires dans lesquels ils sont valides. Par exemple, une méthode telle que `componentWillUpdate` a généralement du sens uniquement dans une définition de composant (classe), ce que la définition suivante de l'extrait de code rend explicite :

L'inclusion de `meta.class.js` à la ligne 8 signifie que l'extrait de code n'est valide que dans les situations où le fichier de code source en cours d'édition est un fichier JavaScript, _et_ le curseur est "dans" une définition de classe. Si vous essayiez d'invoquer l'extrait de code dans un fichier JavaScript vide, rien ne se passerait.

Pour tirer pleinement parti de la puissance des contextes, vous devez avoir une petite compréhension de la syntaxe, des contextes et des sélecteurs de contexte. Ce sont des sujets nuancés qui méritent leur propre article, donc je les expliquerai à un niveau très élevé, avec des liens vers la documentation pour combler les lacunes :

* une [syntaxe](http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html) de langage définit comment le code source est divisé en contextes.
* les [contextes](http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html#scopes) sont des régions étiquetées de texte qui correspondent aux "unités" d'un langage de programmation, telles que les définitions de classe ou de fonction. Chaque position dans un fichier de code source a un contexte associé. Les contextes [Meta](https://www.sublimetext.com/docs/3/scope_naming.html#meta) sont les plus pertinents pour les extraits de code.
* les [sélecteurs de contexte](https://manual.macromates.com/en/scope_selectors) "interrogent" les contextes. Les sélecteurs de contexte sont liés à des actions (telles que les extraits de code ou les raccourcis clavier), et sont utilisés pour déterminer si l'action est appropriée étant donné le contexte actuel.

**Astuce pro**
La meilleure façon d'apprendre les contextes est de jouer avec eux. Déplacez votre curseur à différentes positions dans un fichier, et utilisez le raccourci clavier `cmd+shift+p` pour faire apparaître un menu contextuel affichant le contexte associé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7uR3g9cWm3U_CYShUZQtKw.png)

Les extraits de code ne prennent que quelques secondes à créer. Pourtant, ils en économisent beaucoup plus en effort, et pas seulement en réduisant ce que vous devez taper. En fournissant un moyen rapide et reproductible de développer du contenu, les extraits de code réduisent les erreurs. Ils abstraient également les détails difficiles à retenir, tels que les noms de méthodes et leurs signatures. Tout cela libère vos doigts — et votre cerveau — pour se concentrer sur ce qu'ils veulent faire le plus : écrire du bon code.