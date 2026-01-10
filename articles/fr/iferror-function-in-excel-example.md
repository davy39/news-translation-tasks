---
title: Fonction IFERROR dans Excel
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-09T15:21:52.000Z'
originalURL: https://freecodecamp.org/news/iferror-function-in-excel-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/rubaitul-azad-GauA0hiEwDk-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: excel
  slug: excel
seo_title: Fonction IFERROR dans Excel
seo_desc: "You can use the IFERROR function to catch errors in Excel. Using the function's\
  \ parameters, you can return a custom value when specific errors occur. \nIn this\
  \ article, you'll learn how to use the IFERROR function to evaluate and handle errors\
  \ in Exce..."
---

Vous pouvez utiliser la fonction `IFERROR` pour capturer les erreurs dans Excel. En utilisant les paramètres de la fonction, vous pouvez retourner une valeur personnalisée lorsque des erreurs spécifiques se produisent. 

Dans cet article, vous apprendrez à utiliser la fonction `IFERROR` pour évaluer et gérer les erreurs dans Excel. Vous pouvez utiliser la fonction `IFERROR` pour gérer les erreurs `#N/A`, `#VALUE!`, `#REF!`, `#DIV/0!`, `#NUM!`, `#NAME?` ou `#NULL!`.

## Syntaxe de la fonction IFERROR dans Excel

Voici à quoi ressemble la syntaxe de la fonction `IFERROR`:

```txt
IFERROR(valeur, valeur_si_erreur)
```

Comme vous pouvez le voir ci-dessus, la fonction `IFERROR` a deux paramètres : `valeur` et `valeur_si_erreur`. 

* `valeur` désigne la valeur à vérifier pour une erreur.
* `valeur_si_erreur` est retournée si la valeur vérifiée génère une erreur. 

Les paramètres ci-dessus seront plus clairs avec les exemples qui suivent. 

## Comment utiliser la fonction `IFERROR` dans Excel

Dans cette section, vous verrez une application pratique de la fonction `IFERROR`. 

Voici le tableau avec lequel nous allons travailler : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror-1.PNG)

Dans le tableau ci-dessus, nous avons trois colonnes : **Donnée 1**, **Donnée 2** et **Quotient**. 

L'idée ici est de remplir la troisième colonne (**Quotient**) avec le résultat obtenu en divisant **Donnée 1** par **Donnée 2**. 

C'est-à-dire :

Pour la première ligne : 80/192  
Pour la deuxième ligne : 75/180. Et ainsi de suite. 

Mais si vous regardez de près, certaines lignes ont des valeurs qui entraîneront des erreurs mathématiques — ligne 4 et ligne 6. 

Nous ne pouvons pas diviser 60 par 0 à la ligne 4, ni diviser 65 par NIL à la ligne 6. 

Voici à quoi ressemblera le tableau après les divisions : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror1.PNG)

Le quotient pour la colonne 4 et 6 est respectivement `#DIV/0!` et `#VALUE!`. Cela est dû au fait que l'opération effectuée conduit à une erreur mathématique. 

Nous ne pouvons pas corriger cela mathématiquement, mais nous pouvons capturer ces erreurs et retourner une valeur personnalisée pour elles. Voici comment utiliser la fonction `IFERROR` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror3.PNG)

J'ai supprimé toutes les valeurs de la colonne **Quotient**. Ensuite, nous utiliserons la fonction `IFERROR`. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror4.PNG)

Dans la première ligne **Quotient**, nous avons écrit la fonction `IFERROR` : `=IFERROR(A2/B2, 0)`. Les deux paramètres sont **A2/B2** et **0**.

Le premier paramètre **A2/B2** désigne **A2** (80) divisé par la ligne **B2** (192). Si la division est possible, le quotient sera retourné. 

Si la division n'est pas possible, le deuxième paramètre (**0**) sera retourné. 

Ainsi, notre tableau ressemblera à ceci après l'application de la fonction `IFERROR` dans chaque ligne : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror5.PNG)

Maintenant, la ligne 4 et 6 ont 0 comme quotient au lieu de `#DIV/0!` et `#VALUE!`, respectivement. 

Notez que vous pouvez également utiliser un message personnalisé au lieu de 0. C'est-à-dire : `=IFERROR(A2/B2, "Division non possible")`. Vous devez encadrer le texte entre guillemets. Nous aurons un tableau comme ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/iferror6.PNG)

Il vous appartient donc de personnaliser ce qui sera retourné en cas d'erreur. 

## Résumé

Dans cet article, nous avons parlé de la fonction `IFERROR` dans Excel. Elle peut être utilisée pour gérer les erreurs `#N/A`, `#VALUE!`, `#REF!`, `#DIV/0!`, `#NUM!`, `#NAME?` ou `#NULL!`. 

Nous avons vu la syntaxe pour utiliser la fonction `IFERROR` et la signification de ses paramètres. 

Nous avons également vu des exemples qui montraient comment utiliser la fonction `IFERROR` dans un tableau Excel. 

Merci d'avoir lu !