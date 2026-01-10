---
title: Comment calculer le changement de pourcentage dans Excel – Trouver l'augmentation
  et la diminution en pourcentage
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-07-19T15:25:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-percent-change-in-excel-find-increase-and-decrease-percentage
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/uide-to-writting-a-good-readme-file--1-.png
tags:
- name: excel
  slug: excel
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Comment calculer le changement de pourcentage dans Excel – Trouver l'augmentation
  et la diminution en pourcentage
seo_desc: 'In this article, you''ll learn how to use Excel to calculate percentage
  change, and also how to find the increase and decrease in percentage values.

  Microsoft''s Excel is the most used software when it come performing calculations.
  Various departments ...'
---

Dans cet article, vous apprendrez à utiliser Excel pour calculer le changement de pourcentage, et aussi comment trouver l'augmentation et la diminution des valeurs en pourcentage.

**Excel** de Microsoft est le logiciel le plus utilisé lorsqu'il s'agit d'effectuer des calculs. Divers départements dans de nombreuses entreprises l'utilisent, comme la comptabilité, le suivi des stocks, l'enregistrement du temps, et plus encore.

Il dispose de nombreuses fonctionnalités intégrées utiles comme des formules et il vous aide à effectuer des calculs précis.

Dans cet article, nous allons voir comment utiliser Excel pour calculer le changement de pourcentage, et aussi comment trouver l'augmentation et la diminution des valeurs en pourcentage.

Commençons.

## Qu'est-ce que le changement de pourcentage ?
Le changement de pourcentage est un concept en mathématiques qui représente les changements qui se sont produits au fil du temps. Il est principalement applicable dans le domaine de la comptabilité pour comparer les anciens changements aux nouveaux.

Pour calculer le changement de pourcentage dans Excel, vous devrez utiliser une formule. C'est la formule qui suit les différentes figures sur lesquelles on travaille, comme les bilans, les prix des produits, et autres.

**Syntaxe de la formule**
```excel
changement de pourcentage = (NOUVEAU - ORIGINAL) / ORIGINAL
```

## Comment calculer le pourcentage dans Excel
Prenons un exemple pour comprendre le fonctionnement de la formule.

__Exemple 1__
Si vos gains sont de 1 250 $ en mai et de 1 750 $ en juin, quel est le changement de pourcentage ?

__Solution__
Ce que nous essayons de trouver dans cette question est le changement qui a été fait sur les gains du mois de mai à juin.

En utilisant notre formule :
```
changement de pourcentage = (NOUVEAU - ORIGINAL) / ORIGINAL

donc :
(1 750 - 1 250) / 1 250 = 0,4 ou 40 %
```

__Exemple 2__
Maintenant, voyons comment faire cela dans Excel avec quelques entrées de données pour mieux comprendre comment fonctionnent les fonctions d'Excel :

*ÉTAPE 1 : Saisie des données*.
Ci-dessous, nous avons un espace de travail Excel avec quelques données, nous devons calculer le changement de pourcentage comme indiqué dans la colonne `D`.
![changement de pourcentage](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-07_47_10.png)

*ÉTAPE 2 : La formule*.
Dans ce cas, nous allons poser **A = Prix réel** et **B = Prix budgétaire**, donc notre formule sera : **A/B-1**. Cette formule sera entrée dans la cellule **D2**.
![formule](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-07_56_07.png)

Pour exécuter la formule, il suffit de presser *Entrée*. Nous obtiendrons notre changement de pourcentage en valeurs décimales comme ci-dessous :

> Si le nombre que vous obtenez est positif, comme **0,2**, alors le pourcentage a augmenté. Si le nombre est négatif, comme **-0,2**, alors le pourcentage a diminué.

![changement de pourcentage](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-08_00_58.png)

*ÉTAPE 3 : Attribution du %*.
Pour attribuer le signe `%` à nos valeurs, nous avons plusieurs options. Nous pouvons soit :
* Faire un clic droit sur les valeurs et sélectionner `%`, puis faire glisser le curseur vers le bas pour appliquer les changements aux autres valeurs. Ou
* Surbriller toute la colonne `% Changement` et sélectionner le signe `%` dans le menu Accueil, sous les nombres dans la feuille de travail.
![application %](https://www.freecodecamp.org/news/content/images/2022/01/screenshot-nimbus-capture-2021.07.17-08_07_28.png)

Lors du calcul du changement de pourcentage dans Excel, nous avons deux options à travailler, c'est-à-dire que nous calculons soit l'augmentation en pourcentage, soit la diminution. Voyons comment travailler sur cela :

## Comment calculer l'augmentation en pourcentage
Pour calculer l'augmentation en pourcentage, vous devrez déterminer la différence entre les deux nombres que vous comparez, ce qui signifie que vous aurez besoin des détails originaux et des nouveaux.

Dans ce cas, notre formule sera divisée en deux étapes :
```
augmentation = (NOUVEAU - ORIGINAL)
```
L'étape suivante consistera à diviser l'augmentation par le nombre original et à la multiplier par 100 pour obtenir la valeur en pourcentage.
```
augmentation en pourcentage = Augmentation ÷ Nombre Original × 100.
```

Si le nombre que vous obtenez est négatif, comme **-0,10**, alors le pourcentage a en réalité diminué plutôt qu'augmenté.

__Exemple__
Votre facture de ménage était de 100 $ en septembre, mais a augmenté à 125 $ en octobre. Quel est le pourcentage d'augmentation de septembre à octobre ?

__Solution__
En référence à notre formule ci-dessus, nous devons d'abord obtenir la valeur augmentée, puis la convertir en pourcentage.
```
augmentation = (NOUVEAU - ORIGINAL)

donc :
augmentation = (125 - 100 = 25)

puis :
augmentation en pourcentage = Augmentation ÷ Nombre Original × 100.
% augmentation = 25 ÷ 100 × 100
    = 25 %
```

Comme décrit précédemment lors du calcul du changement de pourcentage dans Excel, les mêmes étapes seront suivies dans le cas du changement de pourcentage.

## Comment calculer la diminution en pourcentage
La même procédure que nous avons appliquée lors du calcul de l'augmentation en pourcentage sera appliquée ici, la seule différence sera que cette fois-ci, nous soustrayons la valeur originale de la nouvelle.

__Formule__
```
Diminution = Nombre Original - Nouveau Nombre
```
L'étape suivante consiste à diviser la valeur que vous avez obtenue comme diminution par le nombre original et à multiplier par 100 pour obtenir la valeur en %.
```
Diminution en pourcentage = Diminution ÷ Nombre Original × 100
```

Si le nombre que vous obtenez est négatif, comme **-0,10**, alors le pourcentage a en réalité augmenté plutôt que diminué.

__Exemple__
L'année précédente, vos dépenses étaient de 500 000 $. Cette année, vos dépenses étaient de 400 000 $. Quelle est la diminution en pourcentage de vos dépenses cette année par rapport à l'année dernière ?

__Solution__
La première étape consiste à obtenir la valeur diminuée, ce qui nous guidera facilement pour obtenir la valeur en pourcentage de celle-ci.

```
Diminution = Nombre Original - Nouveau Nombre

donc :
Diminution = (500 000 - 400 000)
             = 100 000

donc :
Diminution en pourcentage = Diminution ÷ Nombre Original × 100
% Diminution = 100 000 ÷ 500 000 × 100
             = 20 %
```

Peut-être vous demandez-vous comment faire de même sur une feuille de calcul Excel ? Voici une représentation picturale et le fonctionnement de celle-ci :
![diminution en pourcentage](https://www.freecodecamp.org/news/content/images/2022/01/Untitled-design-1.png)

Vous avez maintenant les méthodes illustrées ci-dessus qui fonctionnent quelle que soit la quantité de données que vous avez en main.

Maintenant, lorsque vous travaillez avec des logiciels, vous n'êtes pas toujours garanti de succès, vous êtes susceptible de rencontrer certaines erreurs. Voici quelques-unes des plus courantes que vous êtes susceptible de rencontrer et comment les résoudre.

## Erreurs courantes d'Excel lors de l'utilisation de formules
* **#DIV/0!** : Se produit si vous essayez de diviser un nombre par zéro. Pour résoudre ce problème, changez le diviseur en un nombre qui n'est pas zéro.
* **#VALEUR** : Se produit lorsque les cellules sont laissées vides, ou lorsqu'une fonction attend un nombre mais que vous passez du texte à la place.
* **NUM!** : Se produit lorsqu'une formule contient des valeurs numériques invalides.
* **####** : Se produit lorsque les valeurs sont trop nombreuses pour être affichées dans la colonne assignée. La solution est d'élargir la colonne respective.
* **#NOM?** : Si vous tapez de mauvaises valeurs dans la formule, comme une faute d'orthographe dans une fonction. Pour la corriger, écrivez les noms de formule corrects.
* **#REF!** : Se produit lorsque vous référencez des cellules qui ne sont pas valides ou supprimez des cellules qui ont été référencées dans une formule. Pour corriger cela, référencez les cellules correctement.

## Conclusion
Maintenant, avec cette connaissance, vous devriez être capable de vous débrouiller avec les calculs de changement de pourcentage. Avez-vous quelqu'un en tête qui pourrait bénéficier des connaissances capturées ici, partagez l'article avec eux.

Voici un rapide récapitulatif de ce que nous avons discuté :
* Dans les calculs de changement de pourcentage, nous avons besoin d'au moins deux valeurs.
* Le changement de pourcentage peut être soit un nombre positif, soit un nombre négatif.
* Si le nombre que vous obtenez dans la diminution en % est négatif, alors le pourcentage a en réalité augmenté plutôt que diminué.
* Si le nombre que vous obtenez dans l'augmentation en % est négatif, alors le pourcentage a en réalité diminué plutôt qu'augmenté.

Voici quelques ressources pour vous aider à mieux comprendre le travail avec Excel.
* [Tutoriel Microsoft Excel pour débutants - Cours complet](https://www.youtube.com/watch?v=Vl0H-qTclOg) (*Tutoriel vidéo*)
* [Questions pratiques sur le changement de pourcentage](https://corbettmaths.com/wp-content/uploads/2013/02/percentage-change-pdf.pdf)

Bon codage ❤