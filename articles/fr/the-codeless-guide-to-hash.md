---
title: Le Guide Sans Code des Tables de Hachage et du Hachage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-06T16:47:50.000Z'
originalURL: https://freecodecamp.org/news/the-codeless-guide-to-hash
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c45740569d1a4ca3116.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Hash tables
  slug: hash-tables
seo_title: Le Guide Sans Code des Tables de Hachage et du Hachage
seo_desc: 'By Armstrong Subero

  If you have programmed before, you are sure to have come across hashing and hash
  tables. Many developers have used hash tables in one form or another, and beginner
  developers must learn this fundamental data structure. There is ju...'
---

Par Armstrong Subero

Si vous avez déjà programmé, vous avez sûrement rencontré le hachage et les tables de hachage. De nombreux développeurs ont utilisé des tables de hachage sous une forme ou une autre, et les développeurs débutants doivent apprendre cette structure de données fondamentale. Il y a juste un problème :

**Tous les tutoriels que vous rencontrez sont sûrs de discuter du hachage et des tables de hachage en JavaScript, Python, ou dans un autre langage de programmation.**

Cela signifie que vous pouvez comprendre un peu comment le hachage fonctionne et comment utiliser une table de hachage dans [insérer le langage ici], mais vous pouvez manquer les principes de son fonctionnement.

Ne serait-ce pas génial si nous pouvions apprendre le hachage sans connaître un langage particulier ? Si vous savez comment le hachage fonctionne et ce qu'est une table de hachage, le langage ne devrait pas importer.

C'est l'approche sans code, et dans cet article, je vais vous enseigner tout sur le hachage et les tables de hachage, quel que soit le langage de programmation que vous utilisez actuellement. Que vous soyez un développeur junior ou senior, tout le monde apprendra quelque chose de cet article.

## Alors, qu'est-ce qu'une Fonction de Hachage ?

Avant de nous lancer dans toutes les choses sophistiquées, laissez-moi vous dire ce qu'est le hachage. Pour simplifier, imaginons que nous avons une boîte noire :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image.png)
_Je suis une Boîte Noire_

Cette boîte noire est spéciale. Elle est appelée une boîte de fonction. Nous l'appellerons une boîte de fonction parce que cette boîte va mapper une variable indépendante en entrée à une variable dépendante en sortie (cela semble mathématique, mais restez avec moi).

Notre boîte de fonction fonctionne comme ceci : si nous mettons une lettre dans la boîte, nous obtenons un nombre en sortie. Puisque notre boîte est une boîte de fonction, il ne peut y avoir qu'une seule sortie pour chaque entrée dans la boîte.

Notre boîte de fonction prendra une lettre de A à J en entrée et sortira un nombre correspondant de 0 à 9 en sortie. Donc si nous entrons C, nous obtiendrons 2 en sortie.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-3.png)
_Boîte de Fonction_

Cela forme les bases de ce qu'est une fonction de hachage. La fonction de hachage, cependant, va plus loin. Nous allons mapper des données en entrée à une valeur numérique en sortie, généralement une séquence hexadécimale.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-4.png)
_Fonction de Hachage_

Donc, essentiellement, tout ce que fait le hachage, c'est utiliser une fonction pour mapper des données à une valeur numérique ou alphanumérique représentative. Pour la fonction de hachage, quelle que soit la taille de l'entrée, la sortie restera toujours la même.

## Qu'en est-il des Tables de Hachage ?

À ce stade, vous vous demandez peut-être ce qu'est une table de hachage. Les tables de hachage utilisent le hachage pour former une structure de données.

Les tables de hachage utilisent une méthode associative pour stocker des données en utilisant ce que l'on appelle un système de recherche par clé-valeur. Tout cela signifie que, dans une table de hachage, les clés sont mappées à des valeurs uniques.

Ce système d'organisation des données permet de trouver des données de manière très rapide et efficace. Cela est dû au fait que chaque clé est mappée à une valeur unique - une fois que nous connaissons une clé, nous pouvons trouver la valeur associée instantanément.

Les tables de hachage sont extrêmement rapides, avec une complexité temporelle de l'ordre de O(1).

Confus ? Jetez un coup d'œil à ce diagramme, où nous avons plusieurs boîtes de fonction générant des valeurs de hachage.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-5.png)
_Multiples Boîtes de Fonction_

Dans ce scénario, chaque caractère en entrée (chacun est une clé) a une fonction de hachage appliquée, et la fonction de hachage dans la boîte de fonction génère la valeur de hachage. Cette valeur résultante est ensuite mappée à un index dans la liste chaînée ou le tableau sous-jacent utilisé pour implémenter la table de hachage.

La structure résultante ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/hashtable.png)
_Table de Hachage_

## Collisions de Hachage

C'est le bon moment pour parler des collisions dans les fonctions de hachage et les tables de hachage.

Une fonction en mathématiques est idéale en ce sens qu'un élément en entrée est mappé à exactement un élément en sortie.

Dans une fonction de hachage, cependant, ce n'est pas toujours le cas. Parfois, des valeurs de hachage différentes en entrée peuvent produire la même valeur de hachage en sortie. Lorsque cela se produit, vous obtenez ce que l'on appelle une collision de hachage.

Les collisions de hachage ne sont pas très courantes dans la plupart des cas d'utilisation, car un petit changement dans l'entrée peut produire une sortie radicalement différente. Mais plus vous avez de données à entrer dans la fonction de hachage, plus une collision est susceptible de se produire.

Dans l'exemple de table de hachage que nous avons fourni précédemment, nous avons supposé qu'un tableau était utilisé pour implémenter la table de hachage. Bien que cela soit bon pour les tables de hachage simples, en pratique, celles-ci ne sont pas très bonnes pour gérer les collisions.

Ainsi, une méthode connue sous le nom de chaînage est utilisée. Dans le chaînage, si la table de hachage retourne la même valeur de hachage pour plusieurs éléments, nous "chaînons" simplement les éléments ensemble avec les mêmes valeurs de hachage au même index dans la table de hachage.

De cette façon, au lieu d'être implémentée comme un tableau avec un index, nous implémentons la table de hachage en utilisant une liste chaînée où chaque élément est une liste plutôt que d'avoir une seule valeur assignée.

Mais à mesure que la longueur de la chaîne augmente, la complexité temporelle de la table de hachage peut empirer. Une méthode connue sous le nom d'adressage ouvert est également utilisée. Dans celle-ci, des emplacements alternatifs dans la structure de données sous-jacente implémentant la table de hachage sont trouvés. Gardez simplement à l'esprit que cette méthode réduira l'efficacité de la table de hachage et a une complexité temporelle pire.

## Le Hachage est-il la Même Chose que le Chiffrement ou l'Encodage ?

Beaucoup de gens tendent à associer le hachage au chiffrement ou à l'encodage. Alors, le hachage est-il du chiffrement ? Est-ce la même chose que l'encodage ?

Vous voyez, dans le chiffrement, nous brouillons les données de sorte que seule une personne ayant la clé nécessaire pour déchiffrer les données y aura accès. Lorsque nous utilisons un chiffre de chiffrement, nous ne rendons pas seulement les données chiffrées, mais nous voulons aussi déchiffrer les données à un moment donné. Dans le chiffrement, nous voulons récupérer les données originales.

Le hachage, en revanche, prend des données et produit une sortie dans le but de confirmer l'intégrité des données. Dans le hachage, nous n'avons pas l'intention de récupérer les données originales.

L'encodage diffère du chiffrement et du hachage en ce que le but de l'encodage n'est pas d'obscurcir les données à des fins de sécurité, mais simplement de convertir les données dans un format qu'un autre système peut utiliser.

## Que Puis-je Faire avec le Hachage ?

Les hachages et les tables de hachage ont de nombreuses utilisations ! Celles-ci incluent :

1. Cryptosystèmes
2. Vérifications de Redondance Cyclique
3. Moteurs de Recherche
4. Bases de Données
5. Compilateurs

Ou tout système ayant un processus de recherche complexe.

## Conclusion

Dans cet article, nous avons couvert les bases du hachage, tout cela sans écrire une seule ligne de code ! C'était facile, n'est-ce pas ? L'approche sans code est une manière beaucoup plus facile d'apprendre ces sujets fondamentaux.

Nous avons appris que les fonctions de hachage peuvent être utilisées pour convertir des objets en une sortie alphanumérique de longueur fixe. Nous avons également appris que les tables de hachage sont des systèmes de recherche par clé-valeur et, bien qu'elles fonctionnent bien, ne sont pas parfaites et souffrent parfois de collisions.

À la fin de cet article, vous devriez connaître la différence entre le hachage, le chiffrement et l'encodage, et avoir également une idée de l'endroit où les hachages peuvent être utilisés.

Avez-vous aimé l'approche sans code ? Voulez-vous aller plus loin ?

Apprenez-en davantage sur les tables de hachage et d'autres structures de données et algorithmes dans le livre "Codeless Data Structures and Algorithms". Vous obtiendrez une expansion de ce qui a été couvert dans cet article et apprendrez de nombreux autres sujets, tout cela sans écrire une seule ligne de code !

%[https://www.apress.com/gp/book/9781484257241]