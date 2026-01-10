---
title: Compte de mots dans Excel – Comment vérifier le nombre de mots
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-09T23:51:24.000Z'
originalURL: https://freecodecamp.org/news/word-count-in-excel-how-to-check-the-number-of-words
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603d3e41a675540a2292502b.jpg
tags:
- name: business
  slug: business
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
seo_title: Compte de mots dans Excel – Comment vérifier le nombre de mots
seo_desc: "Excel does not have its own tool that lets you simply look at the number\
  \ of words in a document (like Word does). But is it possible to find out anyway?\
  \ \nYes it is – but it's a bit convoluted, and it also only works on one cell at\
  \ a time. Don't worry..."
---

Excel ne dispose pas de son propre outil qui permet de simplement voir le nombre de mots dans un document (comme Word le fait). Mais est-il possible de le découvrir autrement ?

Oui, c'est possible – mais c'est un peu compliqué, et cela ne fonctionne également qu'une cellule à la fois. Ne vous inquiétez pas, cependant – nous verrons à la fin comment le faire fonctionner sur un groupe de cellules. Explorons comment compter les mots dans Excel.

# Les fonctions Excel que nous utiliserons pour compter les caractères

Nous devons apprendre trois fonctions Excel, `LEN()`, `TRIM()` et `SUBSTITUTE()`, avant de pouvoir les utiliser dans la formule.

## Comment utiliser la fonction `LEN()` dans Excel

La fonction `LEN()` prend une cellule avec un contenu textuel et renvoie le nombre de caractères dans cette cellule.

Par exemple, si nous écrivons `The horse under the three` dans une cellule, et que nous utilisons la fonction `LEN()` pour calculer le nombre de caractères dans cette phrase dans une autre cellule, nous obtiendrons `25`. Vous pouvez voir comment cela fonctionne ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/len.png)

En spécifiant que nous voulons la `LEN()` de la cellule B1 (`LEN(B1)`, dans la cellule B2 ci-dessus), Excel effectue ce calcul pour nous.

Note : J'expliquerai pourquoi j'ai inclus l'erreur d'orthographe ("three" au lieu de "tree") ci-dessous.

## Comment utiliser la fonction `TRIM()` dans Excel

La fonction `TRIM()` prend une cellule avec un contenu textuel et renvoie le même texte sans aucun espace blanc au début ou à la fin.

Par exemple, disons que nous avons une cellule qui ressemble à ceci :       `The horse under the three`   (avec 7 espaces avant le texte et 2 à la fin. Elle a une longueur totale de 34 caractères, y compris les espaces.

La fonction `TRIM()` nous renverra `The horse under the three` (avec seulement les 25 caractères originaux) sans les espaces au début ou à la fin. Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/trim.png)

Vous pouvez voir que, similaire à l'exemple ci-dessus avec `LEN()`, lorsque nous mettons les instructions `TRIM()` dans la cellule B4, Excel calcule la valeur correcte dans la cellule B5.

## Comment utiliser la fonction `SUBSTITUTE()` dans Excel

La fonction `SUBSTITUTE()` remplacera une partie du texte par une autre partie de texte. Par exemple, dans le texte que nous avons utilisé, il y a une erreur d'orthographe (au lieu de `tree`, nous avons `three`). Nous pouvons la corriger en utilisant la fonction `SUBSTITUTE()`.

La syntaxe est `SUBSTITUTE(text, old_text, new_text, [instance_num])`, avec `text` étant le texte que nous allons changer. Dans ce cas, nous aurons le texte que nous voulons changer, et le `old_text` et la partie que nous voulons changer (`three`) qui sera remplacée par le `new_text` (`tree`).

La formule complète est `SUBSTITUTE(B4, "three", "tree")`. Notez que le texte dans une formule doit toujours être mis entre guillemets. Voici comment cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/substitute.png)

Au cas où vous auriez besoin de le savoir, `instance_num` est un paramètre optionnel que vous utilisez au cas où il y aurait plusieurs instances de `old_text` dans le texte et que vous souhaitez en changer une seule. Mais nous ne l'utilisons pas ici.

# Comment compter les mots dans Excel

Nous avons appris à utiliser les fonctions individuelles ci-dessus, et maintenant nous devons les utiliser ensemble de manière un peu compliquée.

Avant de les rassembler, essayons de comprendre comment nous les utilisons, puis nous construirons ensemble la formule complète.

## Comment fonctionne le compte de mots dans Excel

Excel ne dispose pas d'un outil ou d'une formule de compte de mots approprié, mais il y a une chose que nous pouvons compter, et c'est les caractères, comme nous l'avons appris ci-dessus. Plus précisément, nous allons compter le nombre d'espaces à l'intérieur de la chaîne. Et à partir de cela, nous allons dériver le nombre de mots en ajoutant simplement 1 au nombre d'espaces.

Lorsque nous regardons notre exemple, nous pouvons voir que la chaîne `The horse under the tree` a quatre espaces. Si nous ajoutons un, nous obtenons cinq, le nombre total de mots dans la phrase.

Compter les espaces n'est pas non plus une tâche triviale. Puisqu'il n'y a pas d'outil ou de formule spécifique qui peut compter uniquement les espaces, nous devons être un peu créatifs.

Ce que nous allons faire, c'est compter le nombre de caractères dans la chaîne, puis compter le nombre de caractères dans la chaîne lorsque les espaces ont été supprimés (nous pouvons utiliser `SUBSTITUTE(text, " ", "")` pour cela). Ensuite, nous prendrons la différence entre les deux.

`The horse under the tree` a 24 caractères, tandis que `Thehorseunderthetree` a 20 caractères. La différence est de 4, ce qui est le nombre d'espaces dans la chaîne originale. Si nous ajoutons 1, nous obtenons 5, le nombre de mots.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/count-words.png)

## Mise en pratique

Maintenant, nous devons mettre dans une seule formule ce que nous avons vu dans le dernier paragraphe. Cette formule a trois composants :

* la longueur de la phrase avec les espaces au début ou à la fin de la phrase supprimés (nous voulons compter uniquement les espaces entre les mots), donc nous utiliserons `LEN(TRIM(text))`
* la longueur de la chaîne sans espaces, dans ce cas, nous n'avons pas besoin d'utiliser `TRIM()` car nous supprimons tous les espaces, donc `LEN(SUBSTITUTE(text, " ", ""))`
* Ensuite, nous ajoutons simplement `1`.

La formule complète est : `LEN(TRIM(text)) - LEN(SUBSTITUTE(text, " ", "")) + 1`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/single-formula.png)

# Comment créer une fonction personnalisée pour compter les mots dans Excel

Nous avons appris à compter les mots dans une cellule, mais peut-être ne voulons-nous pas taper tout cela chaque fois que nous devons compter le nombre de mots.

Heureusement, nous pouvons résoudre ce problème en créant une fonction personnalisée pour compter les mots. Nous pouvons également avoir une fonction personnalisée pour compter le nombre total de mots dans plusieurs cellules.

## Comment créer une fonction personnalisée avec Visual Basic pour Applications

Nous pouvons ouvrir l'éditeur VBA avec `Alt + F11` (`FN + Alt + F11` pour Mac). Ensuite, nous pouvons aller dans **Insertion > Module**, et nous sommes prêts à écrire notre fonction.

Nous pouvons utiliser ce que nous avons déjà écrit comme point de départ, mais nous devons remplacer `SUBSTITUTE`, car cela n'existe pas en Visual Basic, par la fonction `REPLACE`. Nous avons donc maintenant `LEN(TRIM(text)) - LEN(REPLACE(text, " ", "")) + 1`.

Donnons un nom à la nouvelle fonction que nous voulons créer. J'ai choisi le nom `WORDCOUNT`, mais vous pouvez utiliser n'importe quel nom que vous voulez. Remplacez-le simplement dans les deux endroits où il est écrit par le nom de votre choix.

```
Function WORDCOUNT(text)
   WORDCOUNT = LEN(TRIM(text)) - LEN(REPLACE(text, " ", "")) + 1
End Function
```

Une fois que vous avez ajouté ce code dans l'éditeur, vous avez créé la fonction. Maintenant, vous pouvez fermer l'éditeur et profiter de votre nouvelle fonction ! Mais gardez à l'esprit qu'elle ne fonctionne que pour ce classeur.

Maintenant, faisons en sorte que la fonction fonctionne avec plus d'une cellule, puis nous pourrons également l'ajouter de manière permanente à Excel.

## Comment créer une fonction Excel personnalisée pour compter le nombre total de mots dans un groupe de cellules

Nous allons maintenant mettre à jour la fonction pour qu'elle fonctionne avec une plage de cellules afin de la rendre un peu plus utile. Nous prenons le même code que ci-dessus, et nous l'appliquons à chaque cellule dans une plage, en additionnant le nombre de mots dans chaque cellule.

Remplacez le code que nous avons écrit précédemment par le suivant :

```
Function WORDCOUNT(rng As Range)
    Count = 0
    For Each cl In rng
        thisCount = LEN(TRIM(cl.Value)) - LEN(REPLACE(cl.Value, " ", "")) + 1
        Count = Count + thisCount
    Next
    WORDCOUNT = Count
End Function
```

Note : cette version fonctionne avec une seule plage de cellules, et toutes les cellules sélectionnées doivent contenir du texte. Vous pourriez essayer de créer votre propre version plus polyvalente si vous le souhaitez, explorez simplement VBA par vous-même !

Enfin, nous voulons nous assurer que notre fonction est disponible dans chaque classeur Excel. Pour cela, nous devons fermer l'éditeur VBA et enregistrer le classeur sur lequel nous travaillons en tant que `*.xlam`, le type de fichier de complément Excel.

Pour cela, nous pouvons aller dans **Fichier > Enregistrer sous**, donner un nom au fichier qui nous permettra de le reconnaître, comme "WordCount", choisir le format "Complément Excel (*.xlam)" dans le menu déroulant. Ne changez pas le dossier dans lequel vous enregistrez le fichier, car il est défini automatiquement sur un dossier **AddIns**. 

Maintenant que nous avons créé le fichier, nous devons l'importer dans Excel. Pour cela, nous allons dans **Fichier > Options > Compléments**. En bas de la fenêtre, sélectionnez "Compléments Excel" dans le menu déroulant, et cliquez sur **Atteindre...**. Dans la nouvelle fenêtre, utilisez le bouton **Parcourir...**, et là, il devrait ouvrir le dossier **AddIns** dans lequel nous avons enregistré le fichier. Sélectionnez-le et appuyez sur **Ok**, puis **Ok** à nouveau. Maintenant, la fonction `WORDCOUNT()` sera disponible chaque fois que vous utiliserez Excel.

# Conclusion

Dans cet article, nous avons appris à compter les mots dans une chaîne dans Excel.

Et même si Excel ne dispose pas d'un outil prêt à l'emploi pour compter les mots, nous avons appris à créer notre propre fonction personnalisée pour éviter d'avoir à écrire chaque formule chaque fois que nous voulons obtenir le nombre de mots dans une chaîne.

Enfin, nous avons également appris à étendre notre fonction pour qu'elle fonctionne avec n'importe quel nombre de cellules.