---
title: Comment ajouter une table des matières à votre article sur Ghost
subtitle: ''
author: Ayu Adiati
co_authors: []
series: null
date: '2023-12-01T19:47:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-table-of-contents-to-your-article-on-ghost
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/How-to-Add-a-Table-of-Contents-to-Your-Article-on-Ghost-1.png
tags:
- name: Ghost
  slug: ghost-tag
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: Comment ajouter une table des matières à votre article sur Ghost
seo_desc: 'A table of contents (or TOC) is a list of chapters or section titles in
  an article. You''ll usually find it at the beginning of an article, right after
  the introduction.

  When you write a long blog post or an article with independent sections, consider...'
---

Une table des matières (ou TOC) est une liste de chapitres ou de titres de sections dans un article. Vous la trouverez généralement au début d'un article, juste après l'introduction.

Lorsque vous écrivez un long article de blog ou un article avec des sections indépendantes, envisagez d'ajouter une table des matières. Cela peut aider vos lecteurs à comprendre le contenu de votre article et à savoir ce qui va suivre. Fournir des hyperliens vers chaque titre dans la table des matières aide les lecteurs à naviguer entre les sections qu'ils souhaitent consulter.

Avoir une table des matières dans vos articles vous bénéficie également en tant qu'auteur. Tout d'abord, vous pouvez facilement voir le flux de votre article. Un autre avantage est qu'elle peut augmenter le trafic de votre blog. Si vos lecteurs ont une excellente expérience de lecture de votre article, ils seront susceptibles de le marquer et d'y revenir.

Certaines publications utilisent [Ghost](https://ghost.org/) pour écrire et publier des articles sur leur site web, et freeCodeCamp en fait partie. Dans cet article, je vais vous guider à travers les étapes pour ajouter une table des matières cliquable à votre article sur Ghost.

## Table des matières

<ul>
    <li><a href="#comprendre-les-titres">Comprendre les titres</a></li>
    <li><a href="#comment-ajouter-une-table-des-matieres">Comment ajouter une table des matières</a>
        <ul>
            <li><a href="#etape-1-creer-une-liste-de-titres">Étape #1 - Créer une liste de titres</a>
                <ul>
                    <li><a href="#creer-une-liste-de-titres-de-niveau-un">Créer une liste de titres de niveau un</a></li>
                    <li><a href="#creer-une-liste-avec-des-sous-titres">Créer une liste avec des sous-titres</a></li>
                </ul>
            </li>
            <li><a href="#etape-2-inspecter-un-titre-et-trouver-lid">Étape #2 - Inspecter un titre et trouver l'<code>id</code></a></li>
            <li><a href="#etape-3-ajouter-le-lien">Étape #3 - Ajouter le lien</a>
                <ul>
                    <li><a href="#ajouter-un-lien-vers-un-titre">Ajouter un lien vers un titre</a></li>
                    <li><a href="#ajouter-un-lien-vers-un-titre-en-html">Ajouter un lien vers un titre en HTML</a></li>
                    <li><a href="#pourquoi-le-lien-ne-fonctionne-t-il-pas">Pourquoi le lien ne fonctionne-t-il pas ?</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li><a href="#mots-de-la-fin">Mots de la fin</a></li>
</ul>

## Comprendre les titres

Avant de plonger dans la manière d'ajouter une table des matières, prenons un moment pour comprendre les "titres" car j'utiliserai ce terme par la suite.

> Les titres sont les titres des sections et sous-sections qui sont affichés sur un site web.

Il existe six niveaux de titres basés sur l'importance de la section.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/h1-h6.png)
_Niveaux de titres – H1 - H6_

Suivant les meilleures pratiques, une page sur un site web ne devrait avoir qu'un seul `niveau de titre 1` (connu sous le nom de `h1`). C'est le titre principal de la page. Dans votre cas, ce sera le titre principal de votre article. (Dans cet article, c'est "Comment ajouter une table des matières à votre article sur Ghost".)

Ainsi, écrire un article sur Ghost (ou toute autre plateforme de publication) vous laisse avec `h2` à `h6` pour vos titres de sections et sous-sections. Et vous pouvez en utiliser autant que vous en avez besoin en fonction de la hiérarchie et de l'organisation de votre contenu.

## Comment ajouter une table des matières

Vous pouvez créer votre table des matières à tout moment – avant d'écrire, pendant le processus, ou après avoir terminé la rédaction de votre article.

Mais vous ne pouvez ajouter le lien à chaque chapitre ou titre de section qu'après avoir écrit votre article. Cela est dû au fait que vous devez savoir exactement comment le texte des titres apparaîtra afin de les lier correctement, comme vous le verrez ci-dessous.

Dans ce guide, je vais vous montrer comment construire une table des matières en HTML, ce qui vous permet d'ajouter des sous-titres en plus des titres principaux/titres de section.

### Étape #1 - Créer une liste de titres

Vous pouvez créer une table des matières avec une [liste de titres de niveau un](#heading-creer-une-liste-de-titres-de-niveau-un) (`h2`) ou [inclure les sous-titres](#heading-creer-une-liste-avec-des-sous-titres) (`h3` à `h6`) si vous le souhaitez.

Vous pouvez également choisir comment vous souhaitez formater votre liste :

* **Liste non ordonnée** : Une liste avec des puces.
* **Liste ordonnée** : Une liste avec des nombres.

#### Créer une liste de titres de niveau un

Suivez ces étapes pour créer une liste de titres de niveau un :

1. Insérez une nouvelle ligne.
2. Tapez un tiret (`-`) ou un astérisque (`*`) pour la liste non ordonnée. Ou, tapez un nombre et ajoutez un point — par exemple, `1.` — pour la liste ordonnée.
3. Appuyez sur la barre d'espace.
4. Ajoutez le titre.
5. Cliquez sur entrer pour ajouter un nouvel élément dans la liste.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/add-list-ghost.gif)
_Ajouter une liste non ordonnée et une liste ordonnée._

**Note** : Vous pouvez sauter la section suivante et aller directement à "[Étape #2 - Inspecter un titre et trouver l'`id`](#heading-etape-2-inspecter-un-titre-et-trouver-lid)" si vous le souhaitez.

#### Créer une liste avec des sous-titres

Si vous souhaitez créer une liste avec des sous-titres (liste imbriquée), vous devez utiliser HTML pour la formater manuellement, car Ghost n'a pas d'options de liste imbriquée intégrées dans l'éditeur.

Tout d'abord, vous devez ajouter la carte HTML :

1. Commencez sur une nouvelle ligne.
2. Lorsque votre curseur est sur la nouvelle ligne, vous verrez un bouton d'icône plus (`+`) dans le cercle à gauche. Cliquez sur ce bouton.
3. Cliquez sur l'option "HTML".

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ghost-primary-option-1.png)
_Un signe plus et une option "HTML" sur Ghost._

Ensuite, vous verrez la carte HTML, comme montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ghost----html-card.png)
_Carte HTML sur Ghost._

Maintenant, commençons à ajouter la liste de vos titres et sous-titres.

Ajoutez une liste non ordonnée HTML (`<ul></ul>`) ou une liste ordonnée (`<ol></ol>`) élément.

```html
<ul></ul>

ou

<ol></ol>
```

Pour ajouter la liste de vos titres, ajoutez un espace entre les balises `ul` ou `ol`. Placez le curseur entre les balises et appuyez sur entrer deux fois.

```html
<ul>

</ul>
```

Ensuite, ajoutez des éléments de liste (`<li></li>`) dans la ligne vide entre les balises d'ouverture et de fermeture `ul` ou `ol`. Ajoutez ces éléments de liste en fonction du nombre de vos titres de section.

```html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

Ensuite, placez chacun des titres entre les balises `li`.

```html
<ul>
    <li>Titre 2 - Partie 1</li>
    <li>Titre 2 - Partie 2</li>
    <li>Titre 2 - Partie 3</li>
</ul>
```

Pour ajouter des sous-titres, répétez toutes les étapes. Mais maintenant, vous devez placer l'élément `ul` ou `ol` à l'intérieur de l'élément `li` qui contient le titre de la section. Voici comment faire :

1. Placez votre curseur entre la fin du titre de la section et la balise `</li>`, puis cliquez sur entrer.
2. Cliquez à nouveau sur entrer pour ajouter un espace et ajouter un élément `ul` ou `ol` pour les sous-titres.
3. Ajoutez un élément `ul` ou `ol` dans la nouvelle ligne, placez le curseur entre les balises, et appuyez sur entrer deux fois pour ajouter un espace.
4. Ajoutez des éléments `li` dans la nouvelle ligne entre les balises `ul` ou `ol`.
5. Placez le titre de la sous-section entre les balises `li`.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/walkthrough-nested-list.gif)
_Création d'une liste imbriquée en HTML._

Voici un exemple de table des matières avec des sous-titres en HTML.

```html
<ul>
    <li>Titre 2 - Partie 1
        <ul>
            <li>Titre 3</li>
            <li>Titre 3</li>
        </ul>
    </li>
    <li>Titre 2 - Partie 2
        <ul>
            <li>Titre 3
                <ul>
                    <li>Titre 4</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Titre 2 - Partie 3</li>
</ul>


```

Et le résultat ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ghost----HTML-result.png)
_Une liste de titres de sections et de sous-sections._

### Étape #2 - Inspecter un titre et trouver l'`id`

Après avoir créé la liste, il est temps d'ajouter les liens aux titres dans votre table des matières.

Mais d'abord, vous devez trouver l'attribut `id` de votre titre en utilisant le mode aperçu en inspectant le titre avec les outils de développement de votre navigateur (Chrome ou Firefox).

Alors, ouvrons votre mode aperçu :

1. Cliquez sur l'icône d'engrenage en haut à droite de votre éditeur Ghost.
2. Cliquez sur le lien "Aperçu" à côté de l'entrée "URL de l'article".

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ghost-preview-link.png)
_Le lien "Aperçu" se trouve dans les "Paramètres de l'article" sur Ghost._

Maintenant que vous êtes en mode aperçu, faites un clic droit avec votre souris. Vous verrez quelques options. Cliquez sur l'option "Inspecter" pour ouvrir les outils de développement.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/developer-tools-1.png)
_Option "Inspecter" sur Chrome._

Dans les outils de développement, cliquons sur le bouton avec une icône de boîte et de flèche en haut à gauche pour sélectionner un élément de titre sur la page et l'inspecter.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/select-element-tool.png)
_Bouton "Sélectionner un élément dans la page pour l'inspecter" dans les outils de développement sur Chrome._

Survolez un titre et cliquez dessus. Cela mettra en surbrillance l'élément que vous souhaitez inspecter dans les outils de développement. À l'intérieur de l'élément de titre (`h2` à `h6`), vous verrez un `id` (indiqué par une ligne rouge dans l'image ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/inspect-elelemet-devtool.png)
_Inspecter un titre avec les outils de développement sur Chrome._

Double-cliquez sur la valeur à l'intérieur des guillemets de l'`id` et copiez-la. Vous l'utiliserez pour ajouter le lien au titre dans la table des matières.

**Note** :

* Si vous avez [créé une liste de titres de niveau un](#heading-creer-une-liste-de-titres-de-niveau-un), rendez-vous à la section "[Ajouter un lien vers un titre](#heading-ajouter-un-lien-vers-un-titre)".
* Si vous avez [créé une liste avec des sous-titres](#heading-creer-une-liste-avec-des-sous-titres), allez à la section "[Ajouter un lien vers un titre en HTML](#heading-ajouter-un-lien-vers-un-titre-en-html)".

### Étape #3 - Ajouter le lien

#### Ajouter un lien vers un titre

Pour ajouter le lien, retournez à votre table des matières dans l'éditeur Ghost. Ensuite, suivez ces étapes :

1. Surlignez le titre auquel vous souhaitez ajouter le lien.
2. Cliquez sur l'icône de chaîne.
3. Tapez un crochet (`#`) dans le champ de saisie et collez votre valeur `id` copiée.

Ainsi, cela ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/ghost-highlight-title.png)
_Surligner une liste et une icône de chaîne sur Ghost._

```markdown
#comprendre-les-titres
```

Après avoir actualisé la page d'aperçu, vérifiez si le lien fonctionne. Il devrait vous emmener à la section cible lorsque vous cliquez sur le lien du titre. Si ce n'est pas le cas, lisez la section "[Pourquoi le lien ne fonctionne-t-il pas ?](#heading-pourquoi-le-lien-ne-fonctionne-t-il-pas)".

#### Ajouter un lien vers un titre en HTML

Tout d'abord, retournons à votre éditeur Ghost et allez à l'élément `li` qui contient le titre dans la table des matières.

Ensuite, enveloppez le titre à l'intérieur d'un élément d'ancrage (`<a></a>`) et ajoutez l'attribut `href=""` dans la balise d'ouverture.

```html
<ul>
    <li><a href="">Comprendre les titres</a></li>
</ul>
```

L'élément d'ancrage crée un hyperlien, et l'attribut `href` est le placeholder pour la destination du lien.

Maintenant, vous allez ajouter la destination du lien. Tapez un crochet (`#`) et collez la valeur `id` que vous avez copiée à l'intérieur des guillemets de l'`href`.

```html
<ul>
    <li><a href="#comprendre-les-titres">Comprendre les titres</a></li>
</ul>
```

Répétez toutes les étapes pour ajouter un lien pour chaque titre.

Voici un exemple de titres de sections et de sous-sections avec des liens en HTML :

```html
<ul>
    <li><a href="#comprendre-les-titres">Comprendre les titres</a></li>
    <li><a href="#ajouter-une-table-des-matieres">Ajouter une table des matières</a>
        <ul>
            <li><a href="#etape-1-creer-une-liste-de-titres">Étape #1 - Créer une liste de titres</a></li>
        </ul>
    </li>
</ul>
```

Après avoir actualisé la page d'aperçu, vous pouvez maintenant vérifier si le lien fonctionne en cliquant dessus. Si cela ne fonctionne pas, lisez la section suivante.

#### Pourquoi le lien ne fonctionne-t-il pas ?

Si vous cliquez sur un lien dans votre table des matières et qu'il ne mène nulle part ou vous redirige vers une "Page 404 non trouvée", retournez à la page d'aperçu. Actualisez-la et essayez de cliquer à nouveau sur le lien.

Si cela fait toujours la même chose, vous devez vérifier le lien dans l'éditeur Ghost.

Parfois, cela peut être une faute de frappe où vous changez le titre mais vous devez encore mettre à jour le lien. Ou il manque un crochet (`#`) dans le lien.

## **Mots de la fin**

Si vous avez aimé cet article et l'avez trouvé utile, veuillez le partager avec d'autres. Vous pouvez trouver d'autres travaux sur mon [blog](https://adiati.com/). Restons en contact sur [X (anciennement Twitter)](https://twitter.com/@AdiatiAyu) ou [LinkedIn](https://www.linkedin.com/in/adiatiayu/).