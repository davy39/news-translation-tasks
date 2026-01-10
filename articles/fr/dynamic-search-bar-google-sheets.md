---
title: Google Sheets – Comment créer une barre de recherche dynamique
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-06-02T13:31:11.000Z'
originalURL: https://freecodecamp.org/news/dynamic-search-bar-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Google-Sheets-Dynamic-Search-Bar-with-profile.png
tags:
- name: google sheets
  slug: google-sheets
- name: search
  slug: search
- name: spreadsheets
  slug: spreadsheets
seo_title: Google Sheets – Comment créer une barre de recherche dynamique
seo_desc: 'This tutorial is for when CTRL + F is not enough. 🔥

  I bet I''ve used the CTRL + F shortcut more than any other keyboard shortcut in
  my life. CTRL + Z probably comes close, but I use CTRL + F to find things...

  💥ALL 💥

  💥💥THE 💥💥

  💥💥💥TIME 💥💥💥


  ...'
---

Ce tutoriel est pour quand CTRL + F ne suffit pas. 

Je parie que j'ai utilisé le raccourci CTRL + F plus que tout autre raccourci clavier dans ma vie. CTRL + Z arrive probablement en deuxième position, mais j'utilise CTRL + F pour trouver des choses...

**TOUTES** 

**LES** 

**FOIS** 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/more2.gif)
_gif d'un homme disant nous avons besoin de plus_

Et oui, cela fonctionnera très bien dans une feuille Google pour trouver des informations.

Mais parfois, je veux afficher une gamme de résultats basée sur un mot que je recherche. Pour cela, nous allons créer une barre de recherche dynamique dans notre feuille Google.

Vous pouvez également suivre ce tutoriel vidéo :

%[https://youtu.be/5xgwvokDhT0]

## La barre de recherche

Notre barre de recherche n'est rien de plus qu'une cellule ou une plage de cellules. Dans l'exemple ci-dessous, elle commence en J2.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/google-sheets-search-bar.png)
_Capture d'écran d'une barre de recherche sur Google Sheets_

En ajoutant une fonction `=QUERY()` en J5, nous pouvons regarder ce qui est tapé dans `J2` (le cercle rouge) et afficher les résultats de la recherche en dessous (le rectangle bleu).

Dans mon exemple, je recherche parmi un ensemble de transactions financières personnelles (avec des montants aléatoires ) qui se trouvent dans les colonnes `A:F`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/google-sheets-finance-data.png)
_Capture d'écran des données financières sur Google Sheets_

## La fonction Query

La fonction `=QUERY()` recherche dans la plage Transactions (qui est cette plage `A3:F` où se trouvent toutes les transactions).

Et elle récupère toutes les informations dans la colonne B ou la colonne D qui `CONTIENT` ce que nous tapons dans `J2`.

Ainsi, elle recherche dans toutes nos descriptions de transactions de la colonne B et les catégories de la colonne D ce que nous tapons dans `J2`. La commande `LOWER` transforme les informations de B et D en minuscules. Cela facilite la recherche car la commande `CONTAINS` est sensible à la casse.

```javascript
=QUERY(Transactions, 
       "SELECT A,B,C,D,E WHERE LOWER(B) CONTAINS '"&J2&"' OR LOWER(D) CONTAINS '"&J2&"'")
```

* le seul bémol est que si vous tapez en majuscules dans la barre de recherche, cela ne fonctionnera pas correctement.

## La fonction Filter

En utilisant la fonction `=FILTER()` en combinaison avec la fonction `=SEARCH()`, nous pouvons faire la même chose avec une formule un peu plus courte et sans avoir à nous soucier de la sensibilité à la casse.

```xls
=IF(ISBLANK(J2),"",FILTER(Transactions,SEARCH(J2,B3:B225)))
```

Le compromis ici est que lorsque nous voulons ajouter plusieurs conditions comme nous l'avons fait dans l'instruction `=QUERY()`, cela ne fonctionne pas. Ni `=FIND()` ni `=SEARCH()` n'ont fonctionné correctement lorsque nous avons essayé de les utiliser plus d'une fois à l'intérieur de `=FILTER()`.

J'ai pu trouver une solution en utilisant l'opérateur plus et en construisant la formule de cette manière :

```xls
=IF(ISBLANK(J2),"",FILTER(Transactions,(B3:B225=J2)+(D3:D225=J2)))
```

Malheureusement, lorsque vous filtrez de cette manière, les correspondances partielles ne sont pas incluses dans les résultats de la recherche.

Dans le cas de Query, les réponses partielles sont toujours retournées.

Ainsi, lorsque nous entrons "hom", toutes les lignes contenant "home" seraient retournées. En utilisant plusieurs conditions avec filter, rien ne serait retourné à moins que vous n'entriez le mot entier "home".

## Et XLOOKUP ?

Le problème avec XLOOKUP est double. Premièrement, il ne gère pas bien les correspondances partielles sauf si vous ajoutez des caractères génériques :

```xls
=XLOOKUP("*"&J2&"*",B3:B225,A3:F225,,2)
```

Cela augmente la complexité mais fonctionne toujours.

La différence plus importante est qu'il ne retournera qu'un seul résultat, donc cela ne fonctionnera pas du tout pour nous pour ce cas d'utilisation.

## Le gagnant est Query

Query remporte la palme simplement parce qu'il n'a pas besoin de manipulation supplémentaire pour ajouter plusieurs conditions, et il retournera toutes les valeurs qui répondent à nos critères de recherche.

Il peut vous falloir une minute pour comprendre la syntaxe, mais elle est tout aussi puissante et plus polyvalente que Filter à long terme.

La seule chose à bien retenir est la sensibilité à la casse. Si vous utilisez la commande `LOWER` dans votre requête, n'utilisez pas de lettres de recherche en majuscules.

## Rendre cela propre

Dans la formule complète, j'ai ajouté une fonction `=IF()` au début pour gérer la barre de recherche vide. Nous voulons ne rien retourner dans ce cas :

```xls
=IF(ISBLANK(J2),"", QUERY(Transactions "SELECT A,B,C,D,E WHERE LOWER(B) CONTAINS '"&J2&"' OR LOWER(D) CONTAINS '"&J2&"'")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-30.png)
_Capture d'écran d'une barre de recherche vide dans Google Sheets_

## Suivez-moi

Venez [me suivre sur YouTube](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) alors que je crée des tutoriels chaque semaine.

[Inscrivez-vous ici](https://got-sheet.beehiiv.com/subscribe) pour recevoir ma newsletter dans votre boîte mail chaque semaine.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Beehiivp.jpg)
_Eamonn's Sheets | Coding | Education logo_