---
title: 'Tables HTML : Tout ce qu''il faut savoir sur elles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T16:21:36.000Z'
originalURL: https://freecodecamp.org/news/html-tables-all-there-is-to-know-about-them-d1245980ef96
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UFIlBVRuLEGCGfliYgNwsA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Tables HTML : Tout ce qu''il faut savoir sur elles'
seo_desc: 'By Alexander Gilmanov

  Judging by the fact that we created wpDataTables, it’s no secret that we like tables.
  So much that we wrote this lengthy article about them to help out those of you who
  are beginners and want to learn about HTML tables.

  HTML tab...'
---

Par Alexander Gilmanov

À en juger par le fait que nous avons créé [wpDataTables](https://wpdatatables.com/), il n'est un secret pour personne que nous aimons les tables. Tellement que nous avons écrit cet article détaillé à leur sujet pour aider ceux d'entre vous qui sont débutants et qui veulent apprendre à propos des tables HTML.

Les tables HTML sont utilisées pour afficher des données qui ont du sens dans un logiciel de tableur. Elles se composent de lignes et de colonnes et sont souvent utilisées sur les sites web pour l'affichage efficace de données tabulaires.

Alors, comment faire une table en HTML ? Quand et pourquoi l'utiliser ? Quels sont les bons exemples de tables HTML ? Aujourd'hui, nous allons répondre à ces questions et plus encore pour vous aider à comprendre tout ce qu'il y a à savoir sur les tables HTML.

### Table des matières

* Introduction aux tables
* Style des tables
* Questions fréquemment posées sur les tables HTML
* Outils de génération de tables HTML

### Introduction aux tables

La table HTML est utilisée pour organiser des données (comme du texte, des images, des liens, etc.) dans une conception tabulaire — essentiellement, des lignes et des colonnes.

#### Quand utiliser les tables

Une table en HTML a beaucoup de sens lorsque vous souhaitez organiser des données qui seraient mieux présentées dans un tableur. Une table HTML est un excellent moyen d'afficher des choses comme des données financières, des calendriers, des tarifs, des comparaisons de fonctionnalités, le panneau d'informations nutritionnelles, les scores de bowling et bien d'autres données tabulaires.

Il y a une chance que vous ayez entendu dire que les tables étaient non sémantiques. Cependant, ce n'est pas du tout vrai. Les tables indiquent sémantiquement des données tabulaires et elles sont le meilleur choix pour afficher des données de ce type.

#### Quand NE PAS utiliser les tables

Bien que certaines données soient bien présentées dans des tables, il y a des choses qui ne devraient pas être organisées de cette manière simplement parce que cela n'aurait aucun sens. Il y a aussi certaines autres utilisations inappropriées des tables CSS qui devraient être évitées si possible.

Par exemple, **vous ne devriez jamais utiliser de tables pour la mise en page**. Le problème est que les éléments de table décrivent sémantiquement des données tabulaires et les utiliser à d'autres fins est une violation du devoir sémantique.

La règle générale est que les sites web doivent être accessibles. Une partie de l'accessibilité est constituée des lecteurs d'écran qui lisent les tables de haut en bas, de gauche à droite. Avec les tables en HTML, l'ordre de présentation du site est déterminé par des choix visuels plutôt que par des choix d'accessibilité. Dans des cas comme celui-ci, les lecteurs d'écran ne fonctionnent pas toujours comme vous le souhaitez.

### Éléments de table

Les tables HTML sont généralement accompagnées d'une courte description de leur objectif. Parfois, une description plus détaillée est fournie via l'attribut summary pour le bénéfice des personnes utilisant des agents utilisateurs basés sur la parole ou le Braille.

Les lignes de table peuvent être regroupées en sections d'en-tête, de pied et de corps, (via les éléments **THEAD**, **TFOOT** et **TBODY**). Les agents utilisateurs peuvent exploiter la division en-tête/corps/pied pour supporter le défilement des sections de corps indépendamment des sections d'en-tête et de pied. Lorsque nous imprimons de longues tables HTML, les informations d'en-tête et de pied sont généralement affichées sur chaque page contenant la table.

Si vous souhaitez fournir plus d'informations structurelles, vous pouvez également regrouper les colonnes. En plus de cela, les propriétés des colonnes peuvent être déclarées au début de la définition de la table en utilisant les éléments **COLGROUP** et **COL**.

Les cellules de table contiennent les informations d'en-tête et/ou les données et elles peuvent s'étendre sur plusieurs colonnes et lignes. Lorsque vous étiquetez chaque cellule avec le mode table HTML 4, les agents utilisateurs non visuels peuvent communiquer les informations à l'utilisateur plus facilement. Non seulement cela est utile pour les utilisateurs handicapés, mais cela permet également aux navigateurs sans fil modaux avec des capacités d'affichage limitées de gérer les tables HTML.

Nous avons déjà mentionné que les tables HTML ne doivent pas être utilisées pour la mise en page. Au lieu de cela, vous devriez utiliser des feuilles de style chaque fois que nécessaire pour obtenir de meilleurs résultats et une meilleure accessibilité.

#### En-tête et corps

Examinons un exemple de base de style de table HTML :

Imaginez regarder une ligne (horizontale) pour voir une seule personne et des informations pertinentes à son sujet. Lorsque vous regardez de haut en bas une colonne (verticale), vous obtiendrez un aperçu de la variété ou du motif des données.

La première ligne est l'en-tête de la table et elle ne contient aucune donnée — juste les titres des colonnes. Vous pouvez indiquer sémantiquement que c'est le cas avec l'élément **<thead>**, qui envelopperait le premier **<tr>** (il pourrait envelopper autant de lignes que nécessaire qui sont toutes des informations d'en-tête).

Lorsque vous utilisez **<thead>**, il doit y avoir **aucun <tr>** qui soit un enfant direct de **<table>**. Toutes les lignes doivent être **à l'intérieur** soit de **<thead>**, **<tbody>**, ou **<tfoot>**.

#### Pied de table

Avec **<thead>** et **<tbody>**, il y a **<tfoot>** pour envelopper les lignes de table qui indiquent le pied de la table. Comme **<thead>**, c'est le meilleur moyen d'indiquer sémantiquement que celles-ci ne sont pas des lignes de données mais des informations auxiliaires.

Le placement de **<tfoot>** est unique en HTML car il vient **après <thead>** et **avant <tbody>** ! Donc, même si cela pourrait sembler logique de le trouver à la fin de **<table>**, ce n'est en fait pas le cas. Puisque le pied de table contient des informations nécessaires pour comprendre la table, il est placé avant les données dans l'ordre source pour une meilleure accessibilité.

Le pied de table peut être utilisé dans les longues tables HTML pour répéter l'en-tête, par exemple. Cependant, il peut être utilisé à d'autres fins également, par exemple, avec une mise en page où la position des éléments saute de bas en haut en fonction des besoins.

### Éléments de table et leurs attributs

#### Balise HTML <tfoot>

L'élément **<tfoot>** identifie un ou plusieurs éléments **<tr>** comme contenant le contenu récapitulatif des colonnes d'une table. L'élément **<tfoot>** doit être le descendant direct d'un élément **<table>**.

En HTML5, **<tfoot>** peut être placé soit avant soit après **<tbody>** et les éléments **<tr>**, mais doit apparaître après tout élément **<caption>**, **<colgroup>**, et **<thead>**.

#### Balise HTML <tbody>

L'élément **<tbody>** doit être un descendant direct d'un élément **<table>** et est utilisé pour identifier les éléments **<tr>** qui composent le corps de la table. L'élément **<tbody>** doit toujours venir après un élément **<thead>** et peut venir avant ou après un élément **<tfoot>**.

#### Balise HTML <tr>

**Attributs**

* <tr align="">
* <tr valign="">
* <tr bgcolor="">
* <tr background="">
* <tr bordercolor="">

L'élément **<tr>** est utilisé pour regrouper ensemble les valeurs **<th>** ou **<td>** en une seule ligne d'en-tête de table ou de valeurs de données. L'élément **<tr>** peut être un enfant direct d'un élément **<table>** ou imbriqué dans un élément parent **<thead>**, **<tfoot>**, ou **<tbody>**.

#### Balise HTML <thead>

**Attributs**

L'élément **<caption>** est utilisé pour ajouter une légende à une table HTML. Un **<caption>** doit apparaître dans un document HTML comme le premier descendant d'un parent **<table>**, mais il peut être positionné visuellement en bas de la table avec CSS.

#### col

**Attributs**

L'élément **<col>**, généralement implémenté comme un élément enfant d'un parent **<colgroup>**, peut être utilisé pour cibler une colonne dans une table HTML.

#### colgroup

**Attributs**

L'élément **<colgroup>** est utilisé comme un conteneur parent pour un ou plusieurs éléments **<col>** qui sont utilisés pour cibler des colonnes dans une table HTML.

### Style de base

Distinguer les différentes parties de la table est facile si la table a des couleurs et des lignes différentes. La bordure de la table CSS est un autre élément courant. Par défaut, toutes les cellules de la table sont espacées de 2px les unes des autres. Entre la première ligne et le reste, vous remarquerez un léger écart supplémentaire causé par l'espacement des bordures par défaut appliqué à **<thead>** et **<tbody>** qui les pousse un peu plus.

Vous pouvez contrôler l'espacement :

`table {border-spacing: 0.5rem;}`

Ou vous pouvez simplement supprimer cet espace :

`table {border-collapse: collapse;}`

Le remplissage des tables HTML, l'en-tête des tables HTML, les bordures et l'alignement à gauche des éléments **<th>** sont des moyens simples mais efficaces de styliser vos tables HTML.

### Règles de style importantes pour les tables

Les tables CSS et leurs propriétés fonctionnent très bien si vous les utilisez correctement. Il y a cependant quelques détails à garder à l'esprit. Par exemple, si vous appliquez une certaine police à la table, mais ensuite une autre à la cellule — la cellule gagne car c'est l'élément réel avec le texte à l'intérieur.

Ces propriétés sont soit uniques aux éléments de table, soit elles se comportent de manière unique sur les éléments de table.

#### vertical-align

**Valeurs possibles** : baseline, sub, super, text-top, text-bottom, middle, top, bottom, %, length

Aligne le contenu à l'intérieur d'une cellule. Fonctionne particulièrement bien dans les tables, bien que seuls le haut/bas/milieu aient beaucoup de sens dans ce contexte.

#### white-space

**Valeurs possibles** : normal, pre, nowrap, pre-wrap, pre-line

Contrôle la façon dont le texte s'enroule dans une cellule. Certaines données peuvent avoir besoin d'être toutes sur une seule ligne pour avoir du sens.

#### border-collapse

**Valeurs possibles** : collapse, separate

Appliqué à la table pour déterminer si les bordures s'effondrent en elles-mêmes (un peu comme l'effondrement des marges mais bidirectionnel) ou non. Et si deux bordures qui s'effondrent l'une dans l'autre ont des styles conflictuels (comme la couleur) ? Les styles appliqués à ces types d'éléments « gagneront », dans l'ordre de « force » : cellule, ligne, groupe de lignes, colonne, groupe de colonnes, table.

#### border-spacing

**Valeurs possibles** : length

Si border-collapse est séparé, vous pouvez spécifier à quelle distance les cellules doivent être espacées les unes des autres. La version moderne de l'attribut cellspacing. Et en parlant de cela, le padding est la version moderne de l'attribut cellpadding.

#### width

**Valeurs possibles** : length

La largeur fonctionne sur les cellules de table presque comme vous le pensez, sauf en cas de conflit.

Par exemple, si vous dites à la table elle-même d'être large de 400px puis à la première cellule d'une ligne de trois cellules d'être large de 100px et laissez les autres tranquilles, cette première cellule sera large de 100px et les deux autres se partageront l'espace restant.

Mais si vous dites à toutes les trois d'être larges de 20000px, la table sera toujours de 400px et elle donnera simplement à chacune un tiers de l'espace. Cela suppose que white-space ou des éléments comme une image n'entrent pas en jeu.

#### border

**Valeurs possibles** : length

La bordure fonctionne sur n'importe lequel des éléments de table et presque comme vous vous y attendez. Les particularités apparaissent lorsque vous effondrez les bordures.

Dans ce cas, toutes les cellules de la table n'auront qu'une seule largeur de bordure entre elles, plutôt que les deux auxquelles vous vous attendez (border-right sur la première cellule et border-left sur la cellule suivante).

Pour supprimer une bordure dans un environnement effondré, les deux cellules doivent « être d'accord » pour la supprimer. Comme ceci :

```
td:nth-child(2) { border-right: 0; } td:nth-child(3) { border-left: 0; }
```

Sinon, l'ordre source/spécificité détermine quelle bordure est affichée sur quel bord.

#### table-layout

**Valeurs possibles** : auto, fixed

auto est la valeur par défaut. La largeur de la table et de ses cellules dépend du contenu à l'intérieur.

Si vous changez cela pour fixed, les largeurs de la table et des colonnes sont définies par les largeurs des éléments table et col ou par la largeur de la première ligne de cellules.

Les cellules des lignes suivantes n'affectent pas les largeurs des colonnes, ce qui peut accélérer le rendu. Si le contenu des cellules suivantes ne peut pas s'adapter, la propriété overflow détermine ce qui se passe.

#### Bordure de table

La bordure de table CSS facilite la visualisation de la table et c'est aussi la meilleure méthode pour afficher les bordures. Ajoutez des styles, dans les balises **<style></style>** situées dans l'élément head, pour montrer la bordure de la table, des éléments th et td dans votre document HTML.

#### Connexion des cellules

Pour comprendre comment fonctionnent les cellules connectées, nous devons expliquer les deux attributs qui peuvent être placés sur n'importe quel élément de cellule de table : HTML rowspan et HTML colspan. Si un td a un colspan de 2 (c'est-à-dire **<td colspan="2">**) occupera l'espace de deux cellules dans une ligne horizontalement même s'il s'agit toujours d'une seule cellule. Il en va de même pour rowspan, mais verticalement.

Rowspan est un peu plus difficile à comprendre simplement parce que les colonnes sont regroupées différemment des lignes. Par exemple, avec colspan, vous obtenez la valeur finale en additionnant simplement les valeurs de chaque cellule de table dans la ligne. Avec rowspan, en revanche, la ligne en dessous obtient +1 à son compte de cellules de table et a besoin d'une cellule de table de moins pour compléter la ligne.

#### Imbrication des tables

« Imbriquer des tables » signifie simplement placer une table à l'intérieur d'une autre table, ce qui est possible, mais vous devez inclure la structure complète avec l'élément **<table>**. Cependant, ce n'est peut-être pas la meilleure idée en raison du balisage confus et de la moins bonne accessibilité.

Cependant, il y a des situations où cela est absolument nécessaire et oui, c'est possible. Donc, par exemple, si vous devez importer du contenu d'autres sources, vous pouvez importer une table et la placer à l'intérieur de votre table.

#### Tables à rayures zebra

Les couleurs sont très utiles pour les utilisateurs afin de repérer facilement ce qu'ils recherchent dans la table. Vous pouvez soit définir une couleur de fond pour les éléments de cellule de table, soit les définir sur les lignes de table elles-mêmes.

Voici l'exemple le plus basique :

`tbody tr:nth-child(odd) {background: #eee; }`

L'utilisation de tbody est utile si vous ne voulez pas rayurer les lignes d'en-tête et de pied de page. Si vous ne voulez pas laisser ce qui est en dessous apparaître, vous pouvez également définir les lignes paires.

Si vous devez supporter des navigateurs qui ne comprennent pas : nth-child() (très anciens), vous pourriez utiliser jQuery pour le faire.

#### Mise en évidence des lignes et des colonnes

La mise en évidence des lignes est assez facile ; il suffit d'ajouter un nom de classe à une ligne.

La mise en évidence des colonnes, en revanche, demande un peu plus d'efforts. Vous pouvez utiliser l'élément **<col>**, qui vous permettra de définir des styles pour les cellules qui apparaissent dans la colonne sélectionnée. Par exemple, une table avec 4 colonnes dans chaque ligne devrait avoir 4 éléments **<col>**.

#### Comment centrer une table HTML

Comment centrer une table en HTML ? Cette question est assez courante parmi les personnes concevant leurs premières tables HTML. Le problème est que text-align:center ne centre pas une table dans son ensemble — il centre simplement le texte à l'intérieur des cellules.

Centrer toute la table nécessite que les marges gauche et droite soient définies sur _auto_, et les marges haute et basse définies sur les valeurs dont vous avez besoin.

Supposons que vous souhaitiez que les marges haute et basse de votre table soient d'une ligne vide (1em). Le code CSS dans la balise **<table>** est simplement :

`<table style="margin:1em auto;">`

Si vous souhaitez envelopper du texte à côté d'une table, utilisez _float:left_ pour faire flotter la table à gauche du texte suivant. Pour mettre un peu d'espace entre la table et le texte, vous pouvez également mettre la marge droite sur la table, comme ceci :

`<table style="float:left; margin-right:10px;">`

Si vous voulez que la table soit à droite du texte voisin, utilisez _float:right_ à la place. Vous pouvez également définir la marge gauche :

`<table style="float:right; margin-left:10px;">`

Une chose à garder à l'esprit : Assurez-vous de placer le texte qui doit être à côté de la table après la balise de fermeture **</table>** de la table. Les flottants flottent à côté du contenu suivant dans le code, et non du contenu qui précède le flottant.

### Questions fréquemment posées sur les tables HTML

![Image](https://cdn-media-1.freecodecamp.org/images/1*IlTpsqI9LEC4vNclDhbuNQ.jpeg)

#### Puis-je imbriquer des tables dans des tables ?

Oui, vous pouvez placer une table existante à l'intérieur de la cellule d'une autre table. Il y a un exemple mentionné plus tôt dans cet article.

Gardez à l'esprit que les anciens navigateurs ont des problèmes avec les tables imbriquées si vous ne fermez pas explicitement vos éléments **TR**, **TD**, et **TH**. Pour éviter ces problèmes, incluez chaque balise **</tr>**, **</td>**, et **</th>**, même si les spécifications HTML ne les exigent pas.

De plus, essayez de ne pas imbriquer les tables plus de quelques lignes en profondeur dans la table car les anciennes versions de navigateurs ont souvent des problèmes avec cela. Vous pouvez utiliser les attributs **ROWSPAN** et **COLSPAN** pour minimiser l'imbrication des tables.

Enfin, assurez-vous particulièrement de valider votre balisage chaque fois que vous utilisez des tables imbriquées.

#### Comment puis-je utiliser des tables pour structurer des formulaires ?

À l'intérieur d'un élément **TD** dans une table, il peut y avoir de petits formulaires placés si vous voulez positionner un formulaire par rapport à l'autre contenu. Cependant, si vous voulez positionner les éléments liés au formulaire les uns par rapport aux autres, cela n'aide pas vraiment.

Si vous voulez faire cela, toute la table doit être à l'intérieur du formulaire. Vous ne pouvez pas commencer un formulaire dans un élément **TH** ou **TD** et le terminer dans un autre. Vous ne pouvez pas placer le formulaire à l'intérieur de la table sans le placer à l'intérieur d'un élément **TH** ou **TD**. Vous pouvez mettre la table à l'intérieur du formulaire, puis utiliser la table pour positionner les éléments **INPUT**, **TEXTAREA**, **SELECT**, et autres éléments liés au formulaire, comme le montre l'exemple suivant.

#### Puis-je utiliser des valeurs en pourcentage pour <TD WIDTH=…> ?

Les spécifications HTML 3.2 et HTML 4.0 permettent uniquement des valeurs entières (représentant un nombre de pixels) pour l'attribut WIDTH de l'élément TD. La DTD HTML 4.0, en revanche, permet des valeurs non entières (comme des pourcentages), donc un validateur HTML ne se plaindra pas de <TD WIDTH="xx%">.

Gardez à l'esprit que les navigateurs de Netscape et Microsoft interprètent différemment les valeurs en pourcentage pour <TD WIDTH=…>. D'autre part, leurs interprétations (et celles d'autres navigateurs compatibles avec les tables) correspondent lorsqu'elles sont combinées avec <TABLE WIDTH="100%">. Dans des cas comme celui-ci, les valeurs en pourcentage peuvent être utilisées en toute sécurité, même si elles sont interdites par les spécifications publiques.

#### Pourquoi <TABLE WIDTH="100%"> n'utilise-t-il pas la largeur complète du navigateur ?

La marge entre le contenu et le bord de la zone d'affichage est assez étroite avec les navigateurs graphiques. Navigator laisse toujours de la place pour une barre de défilement à droite. Cependant, lorsque le document n'est pas assez long pour nécessiter un défilement, la barre de défilement n'apparaît pas et cela vous laisse avec la marge à droite qui ne peut pas être supprimée.

#### Pourquoi y a-t-il un espace supplémentaire avant ou après ma table ?

Une syntaxe HTML invalide peut causer un espace supplémentaire avant et après les tables HTML. La cause la plus courante est le contenu libre dans la table (c'est-à-dire, le contenu qui n'est pas à l'intérieur d'un élément **TD** ou **TH**).

En ce qui concerne le contenu libre, il n'y a pas de manière standard de le gérer. Certains navigateurs l'affichent avant ou après la table. Lorsque le contenu libre ne contient que des sauts de ligne multiples ou des paragraphes vides, tout cet espace vide sera affiché avant ou après la table elle-même.

La solution est de corriger les erreurs de syntaxe HTML. Tout le contenu dans une table doit être à l'intérieur d'un élément **TD** ou **TH**.

#### Y a-t-il des problèmes à utiliser des tables pour la mise en page ?

La réponse courte serait — **oui**.

Pour que les navigateurs affichent la table, les attributs de table HTML, en particulier les attributs **HEIGHT** ou **WIDTH**, doivent être connus. Le problème est que toute la table doit être téléchargée avec les dimensions connues avant d'être rendue. Si les attributs mentionnés ci-dessus ne sont pas connus, le processus de rendu peut être retardé.

En plus de cela, si l'un des contenus de la table est trop large pour la zone d'affichage disponible, la table doit s'étirer pour afficher le contenu surdimensionné. Le reste du contenu s'ajuste alors pour s'adapter à la table surdimensionnée plutôt que de s'adapter à la zone d'affichage disponible. En conséquence, les utilisateurs doivent faire défiler horizontalement pour pouvoir lire le contenu. Les versions imprimées peuvent également finir par être rognées.

Si le contenu est affiché sur un écran plus étroit que prévu, les tables de largeur fixe causent les mêmes problèmes que les autres tables surdimensionnées. Si les écrans sont plus larges que prévu, une grande partie de l'écran sera gaspillée avec des marges extrêmement larges. Si les lecteurs nécessitent des polices plus grandes, le contenu sera affiché avec seulement quelques mots par ligne.

L'une des choses les plus importantes à garder à l'esprit est la syntaxe correcte. Les navigateurs ne gèrent pas bien la syntaxe invalide. Les tables imbriquées peuvent ne pas s'afficher correctement avec une syntaxe correcte dans les anciennes versions de Netscape Navigator.

Ensuite, il y a aussi certains navigateurs qui ignorent complètement les tables, ce qui signifie qu'ils ignoreraient également la mise en page créée avec les tables HTML. En plus de cela, les moteurs de recherche les ignorent également. Ce que vous voyez normalement dans les résultats de recherche est généralement le texte au début d'un document. En conséquence, si une table est utilisée pour la mise en page, au lieu du contenu réel, des liens de navigation apparaissent dans la recherche.

Certaines versions de Navigator ont des problèmes de lien vers des ancres nommées lorsqu'elles sont à l'intérieur d'une table qui utilise l'attribut **ALIGN**. Ils associent l'ancre nommée avec le haut de la table, au lieu du contenu de l'ancre. Si vous n'utilisez pas l'attribut **ALIGN** sur vos tables, ce problème peut être entièrement évité.

Tout cela étant dit, si vous insistez pour utiliser des tables HTML pour la mise en page, un balisage soigné peut vous aider à minimiser les problèmes associés. Évitez de placer du contenu large à l'intérieur des tables comme des images larges, des éléments **PRE** avec des lignes longues, des URLs longues, et similaires.

Utilisez plusieurs tables indépendantes plutôt qu'une seule mise en page pleine page. Par exemple, vous pourriez utiliser une table pour disposer une barre de navigation en haut ou en bas de la page, et laisser le contenu principal complètement en dehors de toute table de mise en page.

#### Comment ajouter une légende à votre table avec <caption> ?

Vous ajoutez une légende à votre table en la plaçant à l'intérieur d'un élément [<caption>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption) et en l'imbriquant à l'intérieur de l'élément **<table>**. Vous devriez la placer juste en dessous de la balise d'ouverture **<table>**.

```
<table> <caption>Votre légende devrait être ici</caption> ... </table>
```

Le but de la légende est de contenir une description du contenu de la table. Cela donne aux lecteurs une idée rapide de savoir si la table contient le contenu qu'ils recherchent. Cependant, elle est particulièrement utile pour les utilisateurs malvoyants qui peuvent éviter de faire lire au lecteur d'écran une grande partie du contenu de la table avant de réaliser de quoi parle la table.

Une légende est placée directement sous la balise **<table>**.

Note : L'attribut summary peut également être utilisé sur l'élément **<table>** pour fournir une description — cela est également lu par les lecteurs d'écran. Nous recommandons d'utiliser l'élément **<caption>** à la place car le summary est obsolète selon la spécification des tables HTML5, et n'apparaît pas sur la page.

### Meilleurs outils de génération de tables HTML

Si vous ne voulez pas vous occuper d'un tas de code de table HTML, utiliser un bon outil de génération de table pourrait être vraiment utile. Créer une table en HTML avec un outil comme celui-ci ne nécessite aucune connaissance des langages de développement et c'est assez rapide et simple.

En plus de cela, la majorité des meilleurs outils de ce type sont complètement gratuits et tout le monde peut les utiliser. Basiquement, tout ce que vous avez à faire est d'importer les données, et de personnaliser la table (par exemple, le style de bordure de la table HTML, la mise en forme de la table HTML, la largeur de la table CSS, la couleur de fond de la table CSS, cellspacing, cellpadding, etc.).

Une fois que vous avez terminé, le générateur vous donnera votre code HTML de table que vous copierez et collerez simplement sur votre site web. Facile comme bonjour.

#### Pourquoi devriez-vous utiliser des outils de génération de tables HTML

Concevoir une table à partir de zéro n'est pas une tâche facile. La rendre parfaitement fonctionnelle est un combat difficile et cela prend beaucoup de temps et d'efforts — sans parler du fait que les résultats finissent souvent par être moins que parfaits.

Au lieu d'écrire des lignes et des lignes de code avec votre bloc-notes, vous pouvez vous épargner beaucoup de temps et d'ennuis avec le bon outil de génération de tables HTML. Non seulement c'est plus facile, mais les résultats sont souvent meilleurs que lorsque vous essayez de construire tout vous-même. Sans parler du temps que cela vous fera économiser, et nous savons tous que le temps, c'est de l'argent.

### Outils de génération de tables HTML

#### [Générateur de tables](http://www.tablesgenerator.com/html_tables)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_EHfuyYjdmcl3NN4BkAcJQ.jpeg)

Un outil de génération de tables HTML très utile. Facile à utiliser et il vous permet de choisir le thème que vous préférez. Vous pouvez en savoir plus à ce sujet sur le site officiel.

#### [Quackit](http://www.quackit.com/html/html_table_generator.cfm)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GD-6r6smQraAI_El5jk58g.jpeg)

Un outil simple et facile à utiliser qui est également gratuit.

#### [Truben](http://truben.no/latex/table/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C4G_v1UPRcQCsY60avTwAg.jpeg)

Truben vous permet de créer toutes sortes de tables HTML rapidement et facilement.

#### [Html-tables](http://html-tables.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*xk9W4CUlPP3aXKWwCz-Zwg.jpeg)

Un outil pratique qui fonctionne de manière similaire aux traitements de texte. Il vous permet de créer de belles tables gratuitement.

#### [Générateur de tables CSS](http://www.csstablegenerator.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bwDVOj6xgPOOhsgeDdLHjA.jpeg)

Un excellent outil pour créer des tables stylées sans utiliser d'images.

#### [Tablestyler](http://tablestyler.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ke1T1TXqDO-0w67w2E4w6A.jpeg)

Utilisez des éléments CSS de table et créez de superbes tables HTML avec cet outil en ligne.

#### [Textfixer](http://www.textfixer.com/html/html-table-generator.php)

![Image](https://cdn-media-1.freecodecamp.org/images/1*FBGbuZ-IHehw5esqSTKSwQ.jpeg)

Un outil simple pour créer votre style de table préféré.

#### [Accessify](http://accessify.com/tools-and-wizards/accessibility-tools/table-builder/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BYzMYV3bC9hwhTvwfsZsvA.jpeg)

L'un des outils les plus simples ; parfait pour les personnes ayant peu de connaissances techniques et/ou une connexion internet lente.

#### [RapidTables](https://www.rapidtables.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*u0Iqq-tKoNWD9cow5kOrLg.jpeg)

Cet outil offre une variété d'options de génération et la création de superbes tables HTML en fait partie.

#### [Tableizer](http://tableizer.journalistopia.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zwb6_Tv214beAfvZs_vtIA.jpeg)

Un générateur utile pour concevoir des tables HTML à partir de données de tableur.

### Réflexions finales sur l'apprentissage des tables HTML

Créer des tables HTML belles et fonctionnelles n'est pas une tâche facile. Si vous voulez les construire à partir de zéro, vous devez avoir une certaine quantité de connaissances en codage et d'expérience en développement car il y a beaucoup de choses à considérer si vous voulez que la table affiche le contenu correctement.

Si, en revanche, vous cherchez une solution rapide qui ne nécessite aucune expérience en codage, vous pourriez toujours envisager d'utiliser l'un des nombreux outils pratiques de génération de tables. Non seulement ils vous feront économiser beaucoup de temps et d'ennuis, mais les résultats seront également incroyables.

Si vous avez aimé lire cet article sur les tables HTML, vous devriez également lire ceux-ci :

* [Tables CSS et leur code que vous pouvez utiliser](https://wpdatatables.com/css-tables/)
* [Création de tables réactives avec CSS & HTML ou WordPress](https://wpdatatables.com/responsive-tables/)
* [Plugins de table jQuery que vous devriez vérifier](https://wpdatatables.com/jquery-table-plugins/)

_Publié à l'origine sur [wpdatatables.com](https://wpdatatables.com/html-tables/) le 31 octobre 2018._