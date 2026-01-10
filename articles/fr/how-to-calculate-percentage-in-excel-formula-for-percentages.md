---
title: Comment calculer un pourcentage dans Excel – Formule pour les pourcentages
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-08-18T17:44:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-percentage-in-excel-formula-for-percentages
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/victoria-strukovskaya-OhL_qEqpef4-unsplash-1.jpg
tags:
- name: excel
  slug: excel
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: MathJax
  slug: mathjax
seo_title: Comment calculer un pourcentage dans Excel – Formule pour les pourcentages
seo_desc: 'A percentage is a kind of fraction saying how many parts over 100 something
  is. In this article you will see in detail what a percentage is, and how to calculate
  a percentage in Excel.

  First, before diving into how it works in Excel, let''s take a loo...'
---

Un pourcentage est une sorte de fraction indiquant combien de parties sur 100 quelque chose représente. Dans cet article, vous verrez en détail ce qu'est un pourcentage et comment calculer un pourcentage dans Excel.

Tout d'abord, avant de plonger dans le fonctionnement dans Excel, examinons les mathématiques.

Si vous souhaitez passer directement à la partie Excel et éviter la partie mathématique, veuillez vous rendre à la section [Comment travailler avec les pourcentages dans Excel](#heading-comment-travailler-avec-les-pourcentages-dans-excel).

## Quelle est la formule pour calculer un pourcentage ?

Les pourcentages de 0 % à 100 % sont équivalents à des valeurs décimales de 0 à 1. Cela signifie que vous pouvez convertir un pourcentage en un nombre décimal. Voyons comment.

### Comment convertir un nombre décimal en pourcentage

Vous pouvez convertir un nombre décimal en pourcentage de la manière suivante :

* prenez le nombre décimal, \(d\),
* multipliez-le par \(100\),
* puis ajoutez le symbole de pourcentage \(\%\),

En bref, si vous voulez obtenir un pourcentage à partir d'un nombre \(d\) vous pouvez faire ceci :

$$ ( d \cdot 100 ) \% $$

### Comment convertir un pourcentage en nombre décimal

Si vous voulez convertir un pourcentage en nombre, vous pouvez :

* prendre le pourcentage \(P\%\),
* supprimer le symbole de pourcentage, \(P\)
* puis diviser le nombre par \(100\) : \(\frac{P}{100}\)

En bref, pour convertir un pourcentage \(P\%\) en nombre décimal :

$$ \frac{P\xcancel{\%}}{100} $$

### Comment calculer le pourcentage d'un nombre

Il existe trois cas dans lesquels vous pourriez vouloir calculer le pourcentage d'un nombre :

* pour ajouter un pourcentage au nombre (comme pour calculer combien vous devez payer en incluant la TVA)
* pour obtenir simplement le pourcentage du nombre
* pour soustraire un pourcentage du nombre (comme pour une vente)

#### Comment ajouter un pourcentage à un nombre

Utilisons d'abord un cas spécifique, puis généralisons.

Vous êtes allé faire des courses, et le total que vous devez payer est de 185 $ + TVA. Disons que la TVA dans ce cas est de 17 %.

Vous devriez donc calculer 17 % de 185 $ puis l'ajouter à 185 $.

$$ \$185  \cdot 17 \% + \$185 $$

Vous pouvez en faire une seule opération si, à la place, vous multipliez par \( 117 \% \).

$$ \$185 \cdot ( 100\% + 17\% ) = \$185 \cdot 117\% $$

Si vous avez une calculatrice simple qui n'a pas d'opérateur de pourcentage, vous pouvez convertir le pourcentage en nombre décimal comme nous l'avons discuté ci-dessus. Voici à quoi cela ressemblerait :

$$ \$185 \cdot 117\% = \$185 \cdot \frac{117 \xcancel{ \% }}{ 100 } = \$185 \cdot 1.17 $$

Donc, en général, si vous voulez ajouter un pourcentage \( P \% \) à un nombre \( n \) vous pouvez faire ceci :

$$ n \cdot ( 100\% + P\%) $$

Ou si, à la place, vous avez le pourcentage sous forme de nombre décimal \( d \) vous pouvez faire ceci :

$$ n \cdot (1 + d) $$

#### Comment calculer le pourcentage d'un nombre

Si vous voulez acheter une maison, vous devez payer un acompte sur la maison. Disons que c'est 15 % de la valeur totale de la maison.

Si le prix de la maison est de 200 000 $, comment pouvez-vous le calculer ?

Vous pouvez multiplier le prix par le nombre de pourcentages pour obtenir le pourcentage.

$$ \$200,000 \cdot 15 \% = \$30,000 $$

Donc, si vous voulez savoir quel est le pourcentage \(P\%\) ou la fraction \(d\) d'un nombre \(m\), vous pouvez multiplier ce nombre par le pourcentage ou la fraction.

$$ m \cdot P\% \newline \, \\ m \cdot d $$

#### Comment soustraire un pourcentage d'un nombre

Ce cas est courant pour calculer le prix d'un article en solde. Par exemple, si quelque chose a un prix original de 999 $ et qu'il est en solde à 20 % de réduction, vous pouvez calculer le prix final en déterminant ce que représente 20 % de 999 $. Eh bien, c'est 199,80 $, donc vous soustrayez simplement cette valeur de 999 $.

Le prix final de l'article en solde est de 799,20 $.

Vous pouvez le calculer en une seule étape si vous multipliez le prix original par \((100\% - 20\%)\) ou \(80\%\) :

$$ \$999 \cdot (100\% - 20\%) = \$999 \cdot 80\% = \$779.20 $$

Donc, la formule générale pour soustraire un pourcentage \(P\%\) d'un nombre \(b\) est :

$$ b \cdot (100\% - P\%) $$

Ou sous forme décimale :

$$ b \cdot (1 - d) $$

### Comment calculer le pourcentage d'un nombre par rapport à un autre nombre

Un gâteau pèse 11 livres, et vous mangez 3 parts pour un total de 21 oz. Comment pouvez-vous savoir quel pourcentage de gâteau vous avez mangé ?

Il est important de faire des calculs de ce type avec tout dans les mêmes unités. Donc, d'abord, convertissons le poids du gâteau en onces.

$$ 11~\mathrm{lb} \cdot \frac{16~\mathrm{oz}}{\mathrm{lb}} = 176~\mathrm{oz} $$

Maintenant, il est possible de voir le pourcentage du gâteau que vous avez mangé : vous devez diviser la partie (dans ce cas, les 21 oz de gâteau que vous avez mangées) par le tout (les 176 oz du gâteau entier) :

$$ \frac{11~\mathrm{oz}}{176~\mathrm{oz}} = 0.0625 $$

Comme vu dans le paragraphe sur la conversion d'un décimal en nombre, vous pouvez convertir ceci en pourcentage avec \( 0.0625 \cdot 100 \% = 6.25\%\).

Dans cet exemple, vous avez mangé 6,25 % du gâteau entier.

### Comment combinez-vous deux pourcentages ?

Supposons que certains articles dans une boutique en ligne sont soldés à 20 %, puis il y a une offre pour une réduction de 10 % sur tout ce qui se trouve dans votre panier au moment du paiement.

Si vous obtenez une réduction de 20 % puis une autre réduction de 10 % en plus... combien fait la réduction ?

Ce n'est pas 30 %, car la deuxième réduction est appliquée à un moment différent de la première réduction.

Une réduction de 20 % signifie que vous payez 80 % (\(100\% - 20\%\)) du prix original, et une réduction de 10 % signifie que vous payez 90 % (\(100\% - 10\%\)) du prix original. Combiner les deux réductions signifie multiplier ensemble les deux pourcentages, comme ceci :

$$ 80\% \cdot 90\% = 72\% $$

Ou sous forme décimale :

$$ 0.80 \cdot 0.90 = 0.72 $$

Donc, vous payez 72 % du prix original, ou avez une réduction de 28 %.

## Pourquoi un décimal et un pourcentage sont-ils équivalents ?

Le pourcentage vient de "per cent", ou "sur cent". Le symbole de pourcentage représente la fraction de ligne avec 100 au dénominateur.

$$ 0.20 = \frac{20}{100} = 20\% $$

Le pourcentage est un moyen simple de décrire combien de centièmes d'un tout quelque chose est.

## Comment travailler avec les pourcentages dans Excel

Maintenant, il est temps de commencer à travailler avec Excel. Commençons par quelque chose de assez important. Comment écrivez-vous les pourcentages dans Excel ?

### Comment écrire des pourcentages dans Excel

Dans Excel, vous pouvez écrire des pourcentages de deux manières :

* Vous pouvez écrire un nombre décimal puis formater la cellule en pourcentage à partir du menu déroulant de format ou du bouton Style Pourcentage :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-86.png)
_Sur la première image, le bouton Style Pourcentage est encerclé en rouge, et un nombre décimal est écrit dans la cellule. Sur la deuxième image, la cellule a été formatée en pourcentage, et le nombre est converti en pourcentage._

* Vous pouvez écrire un pourcentage dans la cellule, et la cellule prendra automatiquement le formatage de pourcentage :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-87.png)
_Sur la première image, vous pouvez voir que la cellule vide a le formatage "Général", sur la deuxième image vous pouvez voir un pourcentage écrit dans la cellule, et sur la troisième image vous pouvez voir que la cellule a pris le formatage de pourcentage._

Le format par défaut est pour un pourcentage entier. Vous pouvez changer le nombre de décimales affichées avec les boutons "Augmenter la décimale" et "Diminuer la décimale".

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-112.png)
_Les deux boutons "Augmenter la décimale" et "Diminuer la décimale" encerclés en rouge._

Disons que vous avez une forme décimale de 0,12345. Le formater en pourcentage affichera \( 12\% \). Vous pouvez utiliser les boutons pour afficher les décimales.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-113.png)
_Sur la première image, la valeur 12% apparaît dans la cellule K1. Sur la deuxième image, après avoir utilisé le bouton "Augmenter la décimale" deux fois, la valeur 12,35% apparaît dans la cellule K1. Sur la troisième image, après avoir utilisé le bouton "Diminuer la décimale" une fois, la valeur 12,3% apparaît dans la cellule K1._

### Comment calculer le pourcentage d'un nombre dans Excel

En mathématiques, le pourcentage d'un nombre est calculé en multipliant ce nombre par le pourcentage : \( 87\% \cdot 824 = 716.88 \).

Dans Excel, disons que vous avez le nombre dans la cellule A1 et le pourcentage dans la cellule B1. Pour calculer le résultat, vous pouvez écrire dans la cellule C1 `=A1*B1` :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-110.png)
_Sur la première image, vous pouvez voir la formule pour calculer le pourcentage d'un nombre, puis son résultat sur la deuxième image._

### Comment calculer le pourcentage d'un nombre par rapport à un autre dans Excel

En mathématiques, vous pouvez calculer le pourcentage d'un nombre par rapport à un autre nombre en prenant le rapport des deux nombres puis en le convertissant en pourcentage.

Si vous voulez savoir quel pourcentage 75 représente par rapport à 142, vous pouvez faire \( \frac{75}{142} = 0.528 = 52.8\% \).

Écrivons 75 dans la cellule G1, et 142 dans la cellule H1. Pour obtenir le pourcentage de 75 par rapport à 142, vous pouvez écrire dans la cellule I1 `=G1/H1`. La cellule aura le résultat au format décimal, mais vous pouvez le formater en pourcentage en utilisant le bouton Style Pourcentage. Ensuite, vous pouvez ajuster le nombre de décimales avec les boutons Augmenter la décimale et Diminuer la décimale.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-111.png)
_Sur la première image, vous pouvez voir la formule pour effectuer le calcul. Sur la deuxième image, cela donne un nombre décimal. Sur la troisième image, il a été converti en pourcentage, puis sur la quatrième, le nombre de chiffres après le séparateur décimal a été changé._

### Comment calculer un pourcentage de plusieurs pourcentages dans Excel

Prenons l'exemple utilisé ci-dessus.

Une boutique en ligne a une promotion sur certains articles à 20 % de réduction. Ensuite, il y a une autre promotion de 10 % de réduction sur tout ce qui se trouve dans le panier au moment du paiement.

La première réduction signifie que vous payez 80 % du prix original de l'article. Et ensuite, vous payez 90 % de ce qui se trouve dans le panier.

Combien fait la réduction ?

Vous obtenez le résultat en multipliant les deux pourcentages. \( 90\% \cdot 80\%\).

Dans Excel, si vous avez le premier pourcentage dans I2 et le second dans J2, vous pouvez écrire `=I2*J2` pour calculer le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-120.png)
_Sur la première image, vous pouvez voir la formule pour calculer le pourcentage à partir de plusieurs pourcentages, puis son résultat sur la deuxième image._

## Conclusion

Les pourcentages sont un outil mathématique que nous utilisons dans la vie de tous les jours. Dans ce tutoriel, vous avez appris comment ils fonctionnent mathématiquement et comment les utiliser dans Excel.

J'espère que cet article vous a été utile.