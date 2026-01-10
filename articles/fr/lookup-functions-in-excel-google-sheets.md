---
title: Fonctions de RECHERCHE dans Google Sheets et Excel – RECHERCHEV, RECHERCHEX
  et plus
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-02-07T20:47:26.000Z'
originalURL: https://freecodecamp.org/news/lookup-functions-in-excel-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/lookupFCC.jpg
tags:
- name: excel
  slug: excel
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Fonctions de RECHERCHE dans Google Sheets et Excel – RECHERCHEV, RECHERCHEX
  et plus
seo_desc: "There are several ways to lookup data in a spreadsheet. If you're building\
  \ a dashboard, you'll find this very useful. \nThe =XLOOKUP() function is my new\
  \ favorite way to lookup data. It's discussed in the last section \U0001F447.\n\
  We'll look at four of the bui..."
---

Il existe plusieurs façons de rechercher des données dans une feuille de calcul. Si vous construisez un tableau de bord, vous trouverez cela très utile. 

La fonction =RECHERCHEX() est ma nouvelle façon préférée de rechercher des données. Elle est discutée dans la dernière section 👋.

Nous allons examiner quatre des fonctions de recherche intégrées dans Excel et Google Sheets :

1. `=RECHERCHE()`
2. `=RECHERCHEV()`
3. `=RECHERCHEH()`
4. `=RECHERCHEX()`

Maintenant, si vous avez passé du temps dans des feuilles de calcul, vous avez probablement entendu parler ou utilisez déjà `=RECHERCHEV()`. C'est l'une des fonctions les plus populaires, mais elle est aussi un peu mystérieuse si vous ne l'utilisez pas régulièrement.

🏆 Je vais vous guider à travers chacune de ces fonctions pour vous donner une compréhension complète de la manière de les utiliser correctement. Et je mettrai en avant ma nouvelle préférée, `=RECHERCHEX()`, que Microsoft a publiée en 2019 et que Google Sheets a ajoutée en 2022.

✋ J'ai également créé une feuille Google Sheets sur le thème du café que vous pouvez ouvrir et suivre. [La voici.](https://docs.google.com/spreadsheets/d/1rNAJKwGQzdq8F2zMrAwHMQvY_z3FlBs9BIy_4MIOXn4/edit?usp=sharing)

📽️ Et, je vous ai couvert... à la fin de l'article, il y a aussi une vidéo de présentation. 🎥

![Image](https://www.freecodecamp.org/news/content/images/2023/02/igotyou.gif)
_Gif d'un athlète pointant et disant, Je vous tiens !_

## Données sur le café

Dans notre feuille de calcul sur les données de café, j'ai créé deux feuilles avec les mêmes données. L'une, l'onglet `coffee-data`, est pour `RECHERCHE` et `RECHERCHEV`. L'onglet `horizontal-data` est pour `RECHERCHEH`.

Voici à quoi ressemble l'onglet `coffee-data`. Il y a des colonnes pour le nom du café, le prix, la popularité, le niveau de torréfaction et le goût.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-40.png)
_Capture d'écran de la feuille de calcul des données de café_

Voici à quoi ressemble l'onglet `horizontal-data`. Les mêmes informations, simplement transposées pour que nous puissions passer en revue la fonction `RECHERCHEH` dans un instant. 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-41.png)
_Capture d'écran de la feuille de calcul horizontale des données de café_

Et puis nous avons notre onglet principal, `lookup-functions`, où nous allons examiner les différentes fonctions ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-42.png)

Si vous n'avez pas encore ouvert la feuille Google Sheets, allez-y pour que vous puissiez suivre : [https://docs.google.com/spreadsheets/d/1rNAJKwGQzdq8F2zMrAwHMQvY_z3FlBs9BIy_4MIOXn4/edit#gid=1137792422](https://docs.google.com/spreadsheets/d/1rNAJKwGQzdq8F2zMrAwHMQvY_z3FlBs9BIy_4MIOXn4/edit#gid=1137792422)

Tout fonctionne de la même manière dans Excel, mais il est très facile de partager des feuilles Google Sheets. Vous pouvez faire votre propre copie pour travailler en cliquant sur Fichier -> Créer une copie.

J'ai créé plusieurs plages nommées dans cette feuille pour la rendre plus facile à utiliser lorsque nous remplissons les fonctions. Vous pouvez les examiner en cliquant sur Données -> Plages nommées. Je vais les référencer dans les définitions des fonctions ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/named-ranges.png)
_Capture d'écran des plages nommées dans Google Sheets_

## Comment utiliser la fonction RECHERCHE

Pas de surprise ici – `=RECHERCHE()` vous permet de rechercher une valeur dans vos données. Comme tout le reste ici.

**Voici notre fonction RECHERCHE pour retourner le goût : `=RECHERCHE(A2,coffees,taste)`.** 

Nous utilisons des plages nommées (coffees & taste) qui définissent la colonne des cafés et la colonne des notes de dégustation dans notre `coffee-data`.

Si vous ouvrez la feuille Google Sheets exemple, vous verrez que nous donnons à RECHERCHE trois arguments : la `clé_de_recherche`, `plage_de_recherche|tableau_de_résultat_de_recherche`, et la `[plage_de_résultat]` optionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-28.png)
_Capture d'écran de la fonction Recherche_

La `clé_de_recherche` est la chose que nous recherchons. Dans notre exemple, c'est le nom du café dont nous voulons des informations. Toutes les fonctions ont un argument `clé_de_recherche`.

La `plage_de_recherche|tableau_de_résultat_de_recherche` est la plage où `=RECHERCHE()` doit trouver la `clé_de_recherche`. Elle peut être utilisée à la fois comme plage de recherche et de résultat.

Supposons que vous avez des clés de recherche dans votre colonne de café (A) et que le résultat que vous souhaitez afficher est la colonne de goût (E). Si vous spécifiez A:E comme `plage_de_recherche|tableau_de_résultat_de_recherche`, vous obtiendrez les notes de dégustation sur le café que vous recherchez.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/col.png)
_Capture d'écran d'un tableau de données_

Lorsque vous faites cela, la valeur de la plage de résultat proviendra de la **dernière colonne (ou ligne) de la plage**.

L'alternative est de simplement spécifier la colonne `plage_de_recherche` sur la colonne de café et puis entrer une autre plage pour la `plage_de_résultat`.

C'est ce que j'ai fait dans notre feuille de calcul exemple puisque je voulais extraire des données de chacune des colonnes sur le café.

Inconvénients de `=RECHERCHE()` :

* Les données doivent être triées. Cela ne fonctionnera pas correctement si ce n'est pas le cas.
* Vous devez spécifier la colonne ou la ligne de retour unique pour le résultat.

## Comment utiliser la fonction RECHERCHEV

C'est une fonction très populaire car elle vous permet de rechercher des données avec un peu plus de puissance que la fonction `RECHERCHE` régulière.

**Voici notre fonction RECHERCHEV pour retourner le goût : `=RECHERCHEV(E2,All,5,FAUX)`.**

Nous utilisons une autre plage nommée. Cette fois, une seule est nécessaire. Nous avons `All` qui est l'ensemble du tableau de `coffee-data`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/range-vlookup.jpg)
_Capture d'écran d'un tableau de données_

Avec `=RECHERCHEV()`, nous entrons la `clé_de_recherche` comme avant, puis nous lui donnons une `plage` à rechercher. La première colonne de la `plage` sera utilisée pour trouver la `clé_de_recherche`. Ensuite, nous lui donnons un `index` qui indique combien de colonnes à droite nous voulons chercher pour notre valeur retournée.

Nous tapons ensuite `FAUX` pour indiquer que nos données ne sont pas triées. (Cela est en fait inutile ici puisque nous les avons triées pour que la fonction `RECHERCHE` régulière fonctionne correctement).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-27.png)
_Capture d'écran de la fonction Recherchev_

Inconvénients de `=RECHERCHEV()` :

* Doit rechercher des données de gauche à droite.
* Doit spécifier un nombre pour l'index. Si vous ajoutez ou déplacez des colonnes dans vos données, vous risquez de casser la formule.
* Par défaut, les données sont triées. Dans de nombreux cas, vous devrez définir cet argument comme `FAUX` pour que la fonction fonctionne correctement.

## Comment utiliser la fonction RECHERCHEH

RECHERCHEH fonctionne essentiellement de la même manière que RECHERCHEV, sauf qu'au lieu de rechercher à travers des colonnes, elle recherche à travers des lignes.

**Voici notre fonction RECHERCHEH pour retourner le goût : `=RECHERCHEH(I2,hAll,5,FAUX)`**

![Image](https://www.freecodecamp.org/news/content/images/2023/02/range-hlookup-1.jpg)
_Capture d'écran d'un tableau de données horizontales_

Consultez l'onglet `horizontal-data` pour voir que j'ai transposé le même ensemble de données afin que notre `clé_de_recherche` soit maintenant répartie sur une ligne au lieu de descendre une colonne. Ensuite, lorsque nous donnons une valeur `index`, elle retourne cette valeur en comptant de haut en bas :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-34.png)
_Capture d'écran de la fonction Rechercheh_

Ainsi, si nous voulions le prix, nous aurions un `index` de 2 puisque c'est la deuxième ligne vers le bas. Et dans notre exemple, nous retournons `taste` avec un `index` de 5.

Les inconvénients sont les mêmes que pour `RECHERCHEV`.

## Comment utiliser la fonction RECHERCHEX

Entrez : `=RECHERCHEX()` ! Microsoft l'a publiée comme successeur de RECHERCHEV et RECHERCHEH en 2019, et Google Sheets l'a enfin ajoutée en août 2022. 

Qu'est-ce qui est différent ? 

Eh bien, pour commencer, vous pouvez l'utiliser verticalement ou horizontalement. Vous n'avez pas à spécifier l'un ou l'autre tant que vous avez les plages appropriées comme arguments.

Consultez les deux blocs `RECHERCHEX` sur la feuille de calcul exemple. L'un l'utilise comme une recherche verticale et le second comme une recherche horizontale. Tout ce qui est nécessaire, c'est que les plages soient correctes : La `clé_de_recherche` doit être une seule ligne ou colonne, et la `plage_de_recherche` doit être de la même taille en fonction de celle utilisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-38.png)
_Capture d'écran de la fonction Recherchex utilisée verticalement_

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-36.png)
_Capture d'écran de la fonction Recherchex utilisée horizontalement_

Quelques fonctionnalités/avantages supplémentaires :

* `=RECHERCHEX()` utilise par défaut une correspondance exacte, vous n'avez donc pas à spécifier un `mode_de_correspondance` si c'est ce que vous recherchez.
* Vous êtes en mesure de définir une chaîne personnalisée à afficher comme `valeur_manquante` au lieu de `#N/A` dans le cas où rien n'est retourné.
* Vous êtes en mesure de définir `mode_de_recherche` pour rechercher de la dernière entrée à la première si vous le souhaitez. Dans `RECHERCHEV` et `RECHERCHEH`, il n'est possible d'aller que de la première à la dernière.
* Au lieu de déclarer de nouvelles fonctions pour chaque valeur souhaitée (`price`, `popularity`, `roast level`, et `taste`), `=RECHERCHEX()` retournera chaque valeur dans la `plage_de_recherche` donnée. 

Si vous ne voulez pas que toutes les valeurs soient retournées, vous devrez réduire la taille de la plage. 

Dans l'exemple de feuille de calcul, j'ai défini mes plages `All` et `hAll` pour inclure toutes les colonnes et lignes, respectivement. Si je voulais exclure le goût, par exemple, nous devrions exclure cette colonne/ligne de la `plage_de_recherche`.

`=RECHERCHEX()` a été introduite pour être le successeur de `=RECHERCHEV()` et `=RECHERCHEH()`. Je pense que je vais l'utiliser à l'avenir, et vous ?

## Conclusion

Comme pour la plupart des choses en programmation informatique et en feuilles de calcul, il existe de nombreuses façons de résoudre le même problème. 

Nous avons exploré quatre façons de rechercher des données dans une feuille de calcul : `=RECHERCHE()`, `=RECHERCHEV()`, `=RECHERCHEH()` et `=RECHERCHEX()`. Chacune est puissante, mais `=RECHERCHEX()`, la fonction la plus récente, est particulièrement utile en combinant et en développant de nombreuses fonctionnalités de ses prédécesseurs.

Voici une vidéo de présentation de tout ce que nous avons discuté :

%[https://youtu.be/3TO80uky0Xg]

Merci 🙏 pour la lecture et le visionnage !

Abonnez-vous 🔔 à ma chaîne YouTube ici : [https://www.youtube.com/@EamonnCottrell/](https://www.youtube.com/@EamonnCottrell/)

Et dites bonjour 👋 sur LinkedIn ici : [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)