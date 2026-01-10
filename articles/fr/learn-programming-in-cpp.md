---
title: Une Introduction Animée à la Programmation en C++
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-03-26T23:21:35.536Z'
originalURL: https://freecodecamp.org/news/learn-programming-in-cpp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743028744653/12f33ee5-4ef4-47da-b50d-060a9ee327ce.png
tags:
- name: C++
  slug: cpp
- name: Beginner Developers
  slug: beginners
seo_title: Une Introduction Animée à la Programmation en C++
seo_desc: 'In this tutorial, I’ll give you a comprehensive introduction to programming
  in C++. You don''t need to have any previous programming experience in order to
  begin.

  Along the way, you will learn about the flow of control, variables, conditional
  statemen...'
---

Dans ce tutoriel, je vais vous donner une introduction complète à la programmation en C++. Vous n'avez pas besoin d'avoir une expérience préalable en programmation pour commencer.

Au cours de ce tutoriel, vous apprendrez le flux de contrôle, les variables, les instructions conditionnelles, les boucles, les tableaux, les fonctions, les données structurées, les pointeurs et la mémoire dynamique, les classes, les structures de données courantes et le travail avec les bases de données.

Les environnements de développement intégrés (IDE) sont des outils qui vous permettent d'écrire, d'exécuter et de déboguer des programmes C++. Il existe de excellents IDE C++ gratuits.

Si vous possédez un ordinateur Windows, je recommande d'utiliser [Visual Studio Community Edition](https://visualstudio.microsoft.com/vs/community). Si vous possédez un Mac, je recommande d'utiliser [Xcode](https://developer.apple.com/xcode). Ces outils offrent des fonctionnalités robustes et un excellent support pour le développement C++. Si vous cherchez une installation légère sur n'importe quelle plateforme, [CLion](https://www.jetbrains.com/clion/download) est un excellent choix.

Pour ceux qui préfèrent ne pas installer de logiciel ou qui ne peuvent pas le faire, [replit](https://replit.com) est un IDE basé sur le web qui vous permet de commencer à coder immédiatement.

Il y a des problèmes de pratique dans chaque section afin que vous puissiez pratiquer tout en apprenant le contenu. Ceux-ci se trouvent dans la partie '**Pratique Pratique**' de chaque section. Vous utiliserez votre IDE pour écrire et exécuter ces programmes de pratique.

## **Lectures de Code**

Ce n'est pas un tutoriel en ligne traditionnel ou une série de vidéos. Chaque section contiendra des liens vers des '**lectures de code**' interactives qui animent visuellement les changements apportés à un programme de manière étape par étape.

Une lecture de code montre comment un programme évolue en rejouant toutes les étapes de son développement. Elle comprend un récit fourni par l'auteur, des captures d'écran, des dessins de style tableau blanc et des questions à choix multiples auto-évaluées pour rendre le processus d'apprentissage plus dynamique et interactif. Il suffit de cliquer sur les commentaires numérotés du côté gauche de l'écran pour faire avancer la lecture.

![Capture d'écran montrant à quoi ressemblent les lectures](https://cdn.hashnode.com/res/hashnode/image/upload/v1742956414812/64ed10ba-5f80-442b-b469-9d6462521578.png align="center")

Regardez cette courte [vidéo YouTube](https://youtu.be/uYbHqCNjVDM) qui explique comment visualiser une lecture de code plus en détail.

## **Playback Press**

[Playback Press](https://playbackpress.com/books) est une plateforme pour partager des lectures de code. Le site contient des collections de lectures de code regroupées par langage/technologie dans différents 'livres'. Si vous souhaitez voir le livre complet sur C++, vous pouvez aller ici : [Une Introduction Animée à la Programmation en C++](https://playbackpress.com/books/cppbook).

Les lectures de code sur la plateforme incluent un tutorat IA, des mini-quizzes et des fonctionnalités de synthèse vocale.

[Storyteller](https://markm208.github.io/) est l'outil gratuit et open-source qui alimente les lectures de code.

## **Tuteur IA**

Lors de la visualisation d'une lecture de code, vous pouvez poser des questions à un tuteur IA sur le code. Il répond aux questions de manière claire et patiente, ce qui en fait une ressource utile pour les apprenants. Vous pouvez également demander au tuteur IA de générer de nouvelles questions à choix multiples auto-évaluées pour tester vos connaissances sur ce que vous apprenez.

Pour accéder au tuteur IA et générer de nouvelles questions à choix multiples, il suffit de créer un compte gratuit sur Playback Press et d'ajouter le [livre](https://playbackpress.com/books/cppbook) à votre bibliothèque. C'est toujours gratuit, mais vous devez vous inscrire pour accéder aux fonctionnalités IA.

## **Table des Matières**

* [Partie 1 : Variables](#heading-partie-1-variables)
    
* [Partie 2 : Sélection](#heading-partie-2-selection)
    
* [Partie 3 : Boucles](#heading-partie-3-boucles)
    
* [Partie 4 : Tableaux](#heading-partie-4-tableaux)
    
* [Partie 5 : Fonctions](#heading-partie-5-fonctions)
    
* [Partie 6 : Vecteurs](#heading-partie-6-vecteurs)
    
* [Partie 7 : Données Structurées](#heading-partie-7-donnees-structurees)
    
* [Partie 8 : Pointeurs](#heading-partie-8-pointeurs)
    
* [Partie 9 : Programmation Orientée Objet](#heading-partie-9-programmation-orientee-objet)
    
* [Partie 10 : Structures de Données](#heading-partie-10-structures-de-donnees)
    
* [Partie 11 : Bases de Données SQLite](#heading-partie-11-bases-de-donnees-sqlite)
    
* [Commentaires et Retours](#heading-commentaires-et-retours)
    

### Aperçu de C++

C++ est un langage de programmation puissant et performant largement utilisé dans divers domaines tels que le développement système, le développement de jeux, les simulations en temps réel et les applications haute performance. Il s'agit d'une extension du langage de programmation C, ajoutant des fonctionnalités orientées objet, ce qui le rend adapté aux projets d'ingénierie logicielle à grande échelle.

C++ offre un contrôle fin sur les ressources système et la gestion de la mémoire, ce qui peut conduire à un code hautement optimisé et efficace. C++ reste un choix populaire en raison de sa polyvalence, de ses performances et du vaste écosystème de bibliothèques et d'outils disponibles.

## **Partie 1 : Variables**

Regarder un artiste expérimenté peindre ne suffit pas pour dire que vous avez appris à devenir peintre. Regarder un artiste expérimenté fait partie importante du processus d'apprentissage, mais vous ne pouvez vous appeler peintre qu'après avoir lutté pour faire vos propres peintures.

Il y a beaucoup de similitudes entre apprendre à peindre et apprendre à programmer. La seule façon d'apprendre vraiment la programmation est par la pratique !

Alors, commençons. Suivez les lectures de code ci-dessous. Cliquez sur les liens ci-dessous pour charger chaque lecture de code (il peut être utile de les ouvrir dans un nouvel onglet). Cliquez sur les commentaires de lecture du côté gauche de l'écran de lecture pour parcourir le développement du code.

### **Flux de Contrôle**

La lecture suivante explique le **flux de contrôle** dans un programme en décrivant comment imprimer à l'écran à partir de celui-ci :

* [1.1 Programme d'impression de nom](https://playbackpress.com/books/cppbook/chapter/1/1)
    

### **Variables et Types**

Ce groupe de programmes suivant décrit la déclaration de variables pour stocker des données dans un programme. Toutes les variables ont un **type** qui spécifie ce qui peut être stocké dans celles-ci et quelles opérations peuvent être effectuées sur elles.

* [1.2 Formule de distance](https://playbackpress.com/books/cppbook/chapter/1/2)
    
* [1.3 Types de base en C++](https://playbackpress.com/books/cppbook/chapter/1/3)
    
* [1.4 Types de nombres](https://playbackpress.com/books/cppbook/chapter/1/4)
    
* [1.5 Caractères et chaînes](https://playbackpress.com/books/cppbook/chapter/1/5)
    

### **Lecture à partir du Clavier**

Ce dernier groupe de programmes s'appuie sur les concepts précédents et montre comment demander à l'utilisateur de saisir des données.

* [1.6 Calculateur de salaire hebdomadaire](https://playbackpress.com/books/cppbook/chapter/1/6)
    
* [1.7 Formule de distance revisitée](https://playbackpress.com/books/cppbook/chapter/1/7)
    
* [1.8 Consommation de carburant](https://playbackpress.com/books/cppbook/chapter/1/8)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez un programme qui demande à l'utilisateur trois entiers : un représentant une heure, un représentant une minute et un représentant une seconde. Ensuite, calculez le nombre de secondes jusqu'à minuit en fonction de l'heure qui a été saisie. Affichez le nombre de secondes jusqu'à minuit à l'écran.

Ensuite, demandez à l'utilisateur un seul entier représentant le nombre de secondes jusqu'à minuit. À partir de cette valeur, effectuez le calcul inverse pour trouver l'heure, la minute et la seconde de cette heure. Affichez-la à l'écran au format HH:MM:SS.

## **Partie 2 : Sélection**

Cette section traite de la modification du flux de contrôle avec les instructions `if/else`. Ces instructions demandent à l'ordinateur d'évaluer si une condition est `vraie` ou `fausse` et modifient le flux de contrôle en fonction de la réponse. Elle explique également le type de données `bool`, qui peut contenir soit vrai soit faux, et montre quelques exemples de l'utilisation de la sélection avec les instructions `if`, `if/else`, `if/else if/else` et `switch`.

* [2.1 Booléens](https://playbackpress.com/books/cppbook/chapter/2/1)
    
* [2.2 Calculateur pair/impair](https://playbackpress.com/books/cppbook/chapter/2/2)
    
* [2.3 Paie des heures supplémentaires avec un if/else](https://playbackpress.com/books/cppbook/chapter/2/3)
    
* [2.4 Température de l'eau](https://playbackpress.com/books/cppbook/chapter/2/4)
    
* [2.5 Switch](https://playbackpress.com/books/cppbook/chapter/2/5)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, essayez d'écrire quelques programmes :

#### **Problème 1**

Le problème 1 vous demande d'écrire un programme pour déterminer si une date vient après une autre. Le programme demandera deux ensembles de dates. Ensuite, le programme déterminera si la première date vient avant, est égale à, ou vient après.

```plaintext
Saisissez le premier mois : 2
Saisissez le premier jour : 21
Saisissez la première année : 2012
 
Saisissez le deuxième mois : 2
Saisissez le deuxième jour : 22
Saisissez la deuxième année : 2011
 
La première date vient après la deuxième.
```

#### **Problème 2**

Le problème 2 vous demande d'écrire un programme qui demande à l'utilisateur une date et détermine si cette date est valide. Par exemple, 9/19/2017 est une date valide, mais celles-ci ne sont pas des dates valides :

* 4/31/2006 (seulement 30 jours en avril)
    
* 2/29/2005 (pas une année bissextile)
    
* 16/1/2010 (mois invalide)
    
* 4/59/2013 (jour invalide)
    

Si la date est correcte, affichez-la. Si elle est incorrecte, affichez un message d'erreur expliquant pourquoi la date n'est pas correcte.

#### **Problème 3**

Le problème 3 vous demande d'écrire un programme qui calculera la monnaie pour un achat de vente. Votre programme doit demander un prix de vente. Validez que les données saisies sont un nombre supérieur à 0. Si les données saisies sont incorrectes, affichez un message d'erreur et terminez le programme.

Ensuite, demandez à l'utilisateur le montant que le client paiera au caissier. Validez que cette valeur est supérieure ou égale au prix de vente. Si ce n'est pas le cas, affichez un message d'erreur et terminez le programme.

Si l'entrée est correcte, votre programme doit calculer le montant de la monnaie à rendre à l'utilisateur. Ensuite, calculez les billets et pièces que le caissier doit rendre au client. Le nombre minimal de billets et pièces doit être rendu. Vous pouvez rendre la monnaie de nombreuses manières différentes, mais la seule implémentation correcte est celle qui rend le moins de billets et pièces.

Affichez le nombre de chacun des billets et pièces. Voici un exemple d'exécution du programme :

```plaintext
Saisissez un montant de vente : 20,38 $
Saisissez le montant que le client paie : 30,00 $

La monnaie due est de 9,62 $

Vous devez donner au client cette monnaie :
0 billets de 100 $
0 billets de 50 $
0 billets de 20 $
0 billets de 10 $
1 billet de 5 $
4 billets de 1 $
1 demi-dollar
0 quarters
1 dime
0 nickels
2 pennies
```

En raison du fonctionnement de l'arithmétique avec les variables float, le stockage des valeurs monétaires en tant que floats peut poser certains problèmes.

Par exemple, si vous aviez une variable float qui contenait 1,29 pour représenter 1,29 $ et que vous soustrayiez 0,05 (pour représenter le fait de rendre un nickel), vous penseriez que vous seriez laissé avec exactement 1,24. Malheureusement, l'ordinateur pourrait stocker cette valeur ou pourrait stocker 1,2399999 ou 1,2400001 au lieu de exactement 1,24.

Ces très petites incohérences peuvent poser un problème pour calculer le nombre de pennies à rendre. Envisagez de convertir les montants en ints pour résoudre ce problème.

## **Partie 3 : Boucles**

Ce groupe de lectures traite de l'exécution répétée du même code encore et encore dans une boucle. Ils montrent comment créer des boucles contrôlées par compteur et des boucles contrôlées par événement avec le mot-clé `while`, des boucles imbriquées, une boucle `for`, et comment quitter une boucle avec `break` et `continue`.

* [3.1 Une boucle simple](https://playbackpress.com/books/cppbook/chapter/3/1)
    
* [3.2 Plus de boucles](https://playbackpress.com/books/cppbook/chapter/3/2)
    
* [3.3 Sommation](https://playbackpress.com/books/cppbook/chapter/3/3)
    
* [3.4 Boucle imbriquée](https://playbackpress.com/books/cppbook/chapter/3/4)
    
* [3.5 Boucle `for`](https://playbackpress.com/books/cppbook/chapter/3/5)
    
* [3.6 Mise en majuscules](https://playbackpress.com/books/cppbook/chapter/3/6)
    
* [3.7 `break` et `continue`](https://playbackpress.com/books/cppbook/chapter/3/7)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez quelques programmes :

#### **Problème 1**

Le problème 1 vous demande d'écrire un programme qui calculera la somme des carrés de 1 jusqu'à et y compris ce nombre. Par exemple, si l'utilisateur entre la valeur 5, alors la somme des carrés pour les nombres de un à cinq serait (1 + 4 + 9 + 16 + 25) = 55.

Votre programme doit calculer cette valeur de manière répétée jusqu'à ce que l'utilisateur entre une valeur de -99. Il s'agit de la valeur sentinelle que le programme utilise pour déterminer quand quitter.

```plaintext
Entrez un nombre entier (ex. 10), -99 pour quitter : 5
La somme des carrés jusqu'à 5 est 55
 
Entrez un nombre entier (ex. 10), -99 pour quitter : 4
La somme des carrés jusqu'à 4 est 30
 
Entrez un nombre entier (ex. 10), -99 pour quitter : -99
Bonne journée !
```

#### **Problème 2**

Le problème 2 vous demande d'écrire un programme qui déterminera si un nombre est premier ou non. Un nombre premier est un nombre qui est divisible uniquement par le nombre un et lui-même.

7 est premier car les seuls nombres qui le divisent sans reste sont 1 et 7.

12 n'est pas premier car les nombres qui le divisent sans reste sont 1, 2, 3, 4, 6 et 12.

Votre programme demandera un nombre puis affichera si le nombre est premier ou non. Le nombre saisi doit être un nombre positif. Demandez un nombre de manière répétée jusqu'à ce qu'un nombre positif soit saisi.

#### **Problème 3**

Le problème 3 vous demande de calculer un calendrier d'hypothèque pour quelqu'un qui envisage d'acheter une nouvelle maison. Les entrées pour déterminer un calendrier mensuel sont le montant du prêt principal et le taux d'intérêt annuel. Supposons qu'il s'agit d'un prêt conventionnel de 30 ans.

Votre programme doit demander ces entrées et trouver un paiement mensuel en utilisant ce calcul :

```plaintext
                                   taux d'intérêt mensuel                                              
paiement mensuel =  ------------------------------------------------- * principal
                   1 - (1 + taux d'intérêt mensuel)^-nombre de mois
```

Remarquez que vous devrez calculer le taux d'intérêt mensuel (le taux d'intérêt annuel divisé par 12,0) et le nombre de mois (360 pour un prêt de 30 ans). Le ^ dans cette formule signifie élever un nombre à une puissance. Il existe une fonction appelée `pow()` qui élève un nombre à une autre puissance et retourne le résultat. Par exemple, si vous vouliez élever 2 à la puissance -3, vous feriez ceci :

```cpp
float result = pow(2.0, -3.0);
```

Après avoir calculé le paiement mensuel, créez un résumé des caractéristiques du prêt. Affichez le montant du prêt, le taux d'intérêt, le paiement mensuel, le montant total payé pour le prêt, le montant total des intérêts payés et le ratio du montant payé sur le principal.

Après avoir imprimé le résumé, vous pouvez commencer à faire le calendrier. Demandez à l'utilisateur le mois de fin à afficher dans le calendrier. Le calendrier doit afficher le numéro du mois, le paiement mensuel, le montant payé en principal ce mois-là, le montant payé en intérêts ce mois-là et le montant restant du principal (le montant payé en principal chaque mois est déduit du principal restant). Le montant des intérêts d'un mois est égal au taux d'intérêt mensuel multiplié par le principal restant. Le principal mensuel est la différence entre le paiement mensuel et les intérêts mensuels payés. N'oubliez pas de mettre à jour le principal restant après chaque mois.

Après chaque année du calendrier imprimée, affichez un message avec le numéro de l'année.

## **Partie 4 : Tableaux**

Ce lot de programmes montre comment utiliser les tableaux en C/C++. Un tableau est une collection de variables (toutes du même type) qui ont un seul nom et se trouvent les unes à côté des autres en mémoire. Les boucles sont presque toujours utilisées pour parcourir les éléments d'un tableau. Ils montrent comment créer des tableaux à deux et trois dimensions et utiliser le générateur de nombres aléatoires en C/C++.

* [4.1 Tableaux](https://playbackpress.com/books/cppbook/chapter/4/1)
    
* [4.2 Moyenne et écart-type d'un tableau de valeurs](https://playbackpress.com/books/cppbook/chapter/4/2)
    
* [4.3 Problèmes avec les tableaux](https://playbackpress.com/books/cppbook/chapter/4/3)
    
* [4.4 Lancer de pièces](https://playbackpress.com/books/cppbook/chapter/4/4)
    
* [4.5 Tableaux multidimensionnels](https://playbackpress.com/books/cppbook/chapter/4/5)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez quelques programmes :

#### **Problème 1**

Le problème 1 vous demande d'écrire un programme qui affiche un menu avec trois options.

La première option permet à l'utilisateur de saisir un numéro de mois (entre 1-12) et un numéro de jour dans ce mois (1-31) et calcule le numéro de jour dans l'année. Le 1er janvier est le jour 1. Le 31 janvier est le jour 31. Le 1er février est le jour 32. Le 28 février est le jour 59. Le 31 décembre est le jour 365 (ne vous inquiétez pas des années bissextiles). Si l'utilisateur saisit une combinaison invalide (comme le 31 février), le programme doit demander continuellement à l'utilisateur de saisir une nouvelle valeur jusqu'à ce qu'il saisisse une date valide.

La deuxième option de menu permet à l'utilisateur de saisir un numéro de jour (1-365) et imprime le nom du mois et le numéro de jour de ce mois. Si l'utilisateur saisit 59, le programme doit imprimer :

```plaintext
Le jour 59 est le 28 février
```

Si l'utilisateur saisit un numéro de jour invalide, le programme doit demander continuellement à l'utilisateur de saisir une nouvelle valeur jusqu'à ce qu'elle soit dans la plage correcte.

La dernière option de menu permet à l'utilisateur de quitter le programme. Le menu doit être affiché de manière répétée jusqu'à ce que l'utilisateur choisisse de quitter le programme.

Utilisez un tableau d'entiers pour stocker le nombre de jours dans chacun des mois. Utilisez le tableau pour garder une somme cumulative pour aider à vos calculs de jours. Vous pouvez également vouloir créer un tableau de chaînes avec les noms des mois.

```cpp
int numDaysInMonths[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
```

Voici un exemple d'exécution du programme :

```plaintext
1. Saisir un mois et un jour
2. Saisir un numéro de jour
3. Quitter
Saisir une option de menu : 1
 
Saisir un numéro de mois : 2
Saisir un numéro de jour : 1
 
Le 1er février est le jour 32
 
1. Saisir un mois et un jour
2. Saisir un numéro de jour
3. Quitter
Saisir une option de menu : 2
 
Saisir un numéro de jour : 59
Le jour 59 est le 28 février
 
1. Saisir un mois et un jour
2. Saisir un numéro de jour
3. Quitter
Saisir une option de menu : 3
```

#### **Problème 2**

Le problème 2 vous demande de créer un programme qui trouvera le nombre de jours entre deux dates.

Par exemple, supposons qu'un utilisateur souhaite savoir combien de jours il y a entre deux dates (1/1/2000) et (3/19/2030). Le programme doit trouver combien de jours entiers il y a entre ces deux dates (inclure la date de début et la date de fin).

Si les deux dates sont dans la même année, alors l'algorithme pour trouver le nombre de jours peut être différent de celui où les dates sont dans des années différentes. Votre programme doit gérer chaque cas.

Voici un exemple d'exécution du programme :

```plaintext
Saisir un mois de début : 1
Saisir un jour de début : 1
Saisir une année de début : 2000

Saisir un mois de fin : 3
Saisir un jour de fin : 19
Saisir une année de fin : 2030

Il y a 11035 jours entre le 1/1/2000 et le 3/19/2030
```

## **Partie 5 : Fonctions**

Ce groupe de lectures décrit un autre mécanisme de modification du flux de contrôle appelé fonctions. Une fonction est un bloc de code nommé qui peut être *appelé* et le flux de contrôle sautera vers celui-ci.

Lors de l'appel d'une fonction, certaines données peuvent être passées (appelées paramètres) et la fonction peut retourner une donnée lorsqu'elle est terminée (appelée valeur de retour). Ces lectures discutent du passage de données 'par valeur' versus 'par référence'. Elles montrent que chaque variable a une durée de vie limitée pendant laquelle elle se trouve en mémoire, ou portée.

* [5.1 Fonctions](https://playbackpress.com/books/cppbook/chapter/5/1)
    
* [5.2 Fonctions retournant une valeur](https://playbackpress.com/books/cppbook/chapter/5/2)
    
* [5.3 Fonctions avec paramètres](https://playbackpress.com/books/cppbook/chapter/5/3)
    
* [5.4 Passage de paramètres par référence](https://playbackpress.com/books/cppbook/chapter/5/4)
    
* [5.5 La portée des variables](https://playbackpress.com/books/cppbook/chapter/5/5)
    
* [5.6 Fonction de nombre premier](https://playbackpress.com/books/cppbook/chapter/5/6)
    
* [5.7 Passage de tableaux à des fonctions](https://playbackpress.com/books/cppbook/chapter/5/7)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez quelques programmes :

#### **Problème 1**

Le problème 1 vous demande d'étendre le problème des nombres premiers d'une section précédente. Écrivez un programme qui inclut une fonction qui imprimera tous les nombres premiers dans une plage. Le programme demandera une borne inférieure et une borne supérieure et imprimera tous les nombres premiers dans cette plage.

#### **Problème 2**

Le problème 2 vous demande d'écrire une fonction qui prend un numéro d'année entier et retourne un `bool` indiquant si cette année est une année bissextile ou non. Le calcul pour une année bissextile est le suivant :

* la plupart des années divisibles par quatre sont des années bissextiles
    
* si une année est divisible par quatre et est une année de siècle, comme 1800 ou 1900, alors ce n'est PAS une année bissextile
    
* si une année de siècle est également divisible par 400, comme 2000 ou 2400, alors c'est une année bissextile
    

La fonction devrait ressembler à ceci :

```cpp
bool isLeapYear(int year)
{
    //calculer si c'est une année bissextile ou non et retourner vrai ou faux
}
```

#### **Problème 3**

Le problème 3 vous demande d'écrire un programme qui imprimera un calendrier pour une année entière étant donné le jour où tombe le 1er janvier. Votre programme demandera le jour où tombe le 1er janvier et l'année. Vous devez imprimer le calendrier pour les 12 mois de cette année. Les options pour le premier jour de l'année seront saisies avec les trois premières lettres de chacun des sept jours de la semaine du dimanche ('sun') au samedi ('sat').

L'année n'a pas besoin d'être validée, mais le jour de la semaine oui. Vous ne devez pas permettre à l'utilisateur de saisir une valeur autre que 'sun', 'mon', 'tue', 'wed', 'thu', 'fri' ou 'sat'.

Le format de votre calendrier doit être très similaire à l'exemple ci-dessous. Vous devez utiliser au moins une fonction en plus de la fonction principale. Passez des données entre les fonctions, n'utilisez pas de variables globales.

La dernière exigence est que votre programme ne doit afficher qu'un mois à la fois, puis attendre une entrée de l'utilisateur avant de continuer.

Il est très important que vous élaboriez un plan pour résoudre ce programme avant de commencer à coder (comme pour chaque programme). Réfléchissez à la manière dont vous imprimeriez le calendrier d'un seul mois étant donné le jour du mois où il commence.

Sortie d'exemple :

```plaintext
Pour quelle année souhaitez-vous le calendrier ?
2003

Quel jour de la semaine tombe le 1er janvier (sun pour dimanche, mon pour lundi, etc.) ?
s
Entrée invalide - veuillez entrer les trois premières lettres du jour
 
Quel jour de la semaine tombe le 1er janvier (sun pour dimanche, mon pour lundi, etc.) ?
wed

    Janvier 2003
 D  L  M  M  J  V  S
---------------------
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

Souhaitez-vous continuer ? y

   Février 2003
 D  L  M  M  J  V  S
---------------------
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28

Souhaitez-vous continuer ? y
...
...
```

## **Partie 6 : Vecteurs**

C++ est livré avec la Standard Template Library (STL) qui est une collection de différents conteneurs. Cette section couvrira les vecteurs. Un `vector` est un conteneur basé sur un tableau qui contient des données de manière très similaire à un tableau, mais il est *plus intelligent*. Il sait combien d'éléments il contient et il peut croître à mesure que le programme s'exécute. Il montre également comment lire et écrire des données à partir d'un fichier, rechercher efficacement dans un conteneur basé sur un tableau, trier des valeurs, et plus encore.

* [6.1 `vector`](https://playbackpress.com/books/cppbook/chapter/6/1)
    
* [6.2 Passage d'un `vector` à une fonction](https://playbackpress.com/books/cppbook/chapter/6/2)
    
* [6.3 Fonctionnalités avancées des `vector`s](https://playbackpress.com/books/cppbook/chapter/6/3)
    
* [6.4 Lecture à partir d'un fichier et stockage dans un `vector`](https://playbackpress.com/books/cppbook/chapter/6/4)
    
* [6.5 Recherche linéaire et recherche binaire](https://playbackpress.com/books/cppbook/chapter/6/5)
    
* [6.6 Tri à bulles](https://playbackpress.com/books/cppbook/chapter/6/6)
    
* [6.7 Écriture dans un fichier](https://playbackpress.com/books/cppbook/chapter/6/7)
    
* [6.8 `vector`s à deux dimensions](https://playbackpress.com/books/cppbook/chapter/6/8)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez un programme pour lire des mots entiers à partir d'un fichier et les stocker dans un vecteur de chaînes. Créez un simple fichier texte (.txt) en utilisant votre éditeur de code. Ajoutez ensuite quelques phrases de texte. Supprimez les marques de ponctuation des mots et mettez-les tous en minuscules. Ne stockez un mot dans le vecteur que s'il n'est pas déjà présent.

## **Partie 7 : Données Structurées**

Cette section décrit comment utiliser les types de données structurés. Les types de données structurés vous permettent de regrouper des données liées ensemble afin qu'elles puissent être transmises facilement.

* [7.1 `struct` simple](https://playbackpress.com/books/cppbook/chapter/7/1)
    
* [7.2 `struct`s hiérarchiques](https://playbackpress.com/books/cppbook/chapter/7/2)
    
* [7.3 `vector`s en tant que membres de `struct`s](https://playbackpress.com/books/cppbook/chapter/7/3)
    
* [7.4 `struct`s avec un `vector` d'objets](https://playbackpress.com/books/cppbook/chapter/7/4)
    
* [7.5 Calcul avec `struct`s](https://playbackpress.com/books/cppbook/chapter/7/5)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez un programme qui a une structure pour représenter un téléphone portable. Chaque téléphone portable a un nom de modèle et un fabricant ainsi qu'un appareil photo avec une résolution en mégapixels. Par exemple, un utilisateur peut vouloir stocker des informations sur un Apple IPhone X avec un appareil photo de 12 MP ou un Google Pixel 4 avec un appareil photo de 16 MP.

Votre programme créera trois objets de téléphone portable, les remplira, puis les ajoutera à un vecteur. Enfin, imprimez les informations sur chaque téléphone portable à l'écran.

Écrivez une fonction qui prend un objet de téléphone portable par référence et demande à l'utilisateur de saisir le modèle, le fabricant et la résolution de l'appareil photo. Écrivez une autre fonction qui imprime les informations sur un téléphone portable. Écrivez une fonction qui prend un vecteur de téléphones portables et imprime chacun.

## **Partie 8 : Pointeurs**

Cette section décrit les pointeurs en C/C++. Un pointeur est une variable qui contient l'adresse d'une autre variable. Les pointeurs sont importants car ils nous permettent d'utiliser une section spéciale de la mémoire appelée le 'tas'. Cette section traite des différents types de mémoire qui peuvent être utilisés dans un programme (globale, locale et dynamique).

* [8.1 Pointeurs simples](https://playbackpress.com/books/cppbook/chapter/8/1)
    
* [8.2 Pointeur vers un objet](https://playbackpress.com/books/cppbook/chapter/8/2)
    
* [8.3 Vecteurs de pointeurs](https://playbackpress.com/books/cppbook/chapter/8/3)
    
* [8.4 Les tableaux sont des pointeurs](https://playbackpress.com/books/cppbook/chapter/8/4)
    
* [8.5 Passage de données aux fonctions avec des pointeurs](https://playbackpress.com/books/cppbook/chapter/8/5)
    
* [8.6 Comparaison de pointeurs](https://playbackpress.com/books/cppbook/chapter/8/6)
    
* [8.7 Trois types de variables - globale, locale et dynamique](https://playbackpress.com/books/cppbook/chapter/8/7)
    
* [8.8 Exemple de variables dynamiques](https://playbackpress.com/books/cppbook/chapter/8/8)
    
* [8.9 Pointeurs pendants et pointeurs nuls](https://playbackpress.com/books/cppbook/chapter/8/9)
    
* [8.10 Tableau dynamique d'étudiants](https://playbackpress.com/books/cppbook/chapter/8/10)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez un programme qui lira une séquence de mots à partir du clavier et les stockera dans un tableau dynamique de chaînes. Utilisez le mot 'quit' comme le mot qui termine la saisie. Imprimez les mots à l'écran dans l'ordre où ils ont été saisis, chacun sur sa propre ligne. Ne stockez pas le même mot deux fois.

Jusqu'à présent, la taille d'un tableau était déterminée au moment de la compilation. Maintenant que vous connaissez les pointeurs et le mot-clé `new`, écrivez un programme qui n'est pas limité à la sélection d'une borne supérieure au moment de la compilation pour le nombre de mots qui peuvent être lus.

Une façon de faire cela est d'utiliser `new` pour créer des tableaux de chaînes à la volée. Chaque fois qu'un tableau est rempli, créez dynamiquement un tableau qui est deux fois plus grand, copiez le contenu du tableau existant vers le nouveau tableau et continuez (n'oubliez pas de `delete` le tableau original). Commencez avec un tableau de 5 éléments.

Voici un exemple de la sortie :

```plaintext
Entrez du texte et terminez par le mot quit :
Ce labo vous demande d'écrire un programme qui lira une séquence de mots à partir du clavier et les stockera dans un tableau dynamique de chaînes. Utilisez le mot 'quit' comme le mot qui termine la saisie. Imprimez les mots à l'écran dans l'ordre où ils ont été saisis chacun sur sa propre ligne. Ne stockez pas le même mot deux fois. quit

Doublement du tableau de 5 à 10
Doublement du tableau de 10 à 20
Doublement du tableau de 20 à 40
Doublement du tableau de 40 à 80
1. Ce
2. labo
3. vous
4. demande
5. d'écrire
6. un
7. programme
8. qui
9. lira
10. une
11. séquence
12. de
13. mots
14. à
15. partir
16. du
17. clavier
18. et
19. les
20. stockera
21. dans
22. un
23. tableau
24. dynamique
25. de
26. chaînes.
27. Utilisez
28. le
29. mot
30. 'quit'
31. comme
32. le
33. mot
34. qui
35. termine
36. la
37. saisie.
38. Imprimez
39. les
40. mots
41. à
42. l'écran
43. dans
44. l'ordre
45. où
46. ils
47. ont
48. été
49. saisis
50. chacun
51. sur
52. sa
53. propre
54. ligne.
55. Ne
56. stockez
57. pas
58. le
59. même
60. mot
61. deux
62. fois.
Appuyez sur une touche pour continuer . . .
```

## **Partie 9 : Programmation Orientée Objet**

Cette section traite de la programmation orientée objet en utilisant des classes en C++. Une classe est comme une `struct`, sauf qu'en plus de collecter des données, elle collecte également des méthodes qui travaillent sur ces données. Cela s'appelle l'encapsulation. Elle traite également de l'héritage et du polymorphisme qui facilitent la réutilisation du code.

* [9.1 Classe simple](https://playbackpress.com/books/cppbook/chapter/9/1)
    
* [9.2 Une classe avec des membres de données](https://playbackpress.com/books/cppbook/chapter/9/2)
    
* [9.3 Une classe avec des objets pour membres de données](https://playbackpress.com/books/cppbook/chapter/9/3)
    
* [9.4 Analyse de mots courants](https://playbackpress.com/books/cppbook/chapter/9/4)
    
* [9.5 Système d'inscription des étudiants et des cours](https://playbackpress.com/books/cppbook/chapter/9/5)
    
* [9.6 Héritage et polymorphisme](https://playbackpress.com/books/cppbook/chapter/9/6)
    
* [9.7 Hiérarchie d'héritage des formes](https://playbackpress.com/books/cppbook/chapter/9/7)
    
* [9.8 Héritage et polymorphisme en C++](https://playbackpress.com/books/cppbook/chapter/9/8)
    
* [9.9 Exemple de constructeur de copie](https://playbackpress.com/books/cppbook/chapter/9/9)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez quelques programmes :

#### **Problème 1**

Le problème 1 vous demande de créer une classe Date pour représenter une date.

Il doit y avoir un int pour le numéro du jour, le numéro du mois et le numéro de l'année déclarés dans la section privée. Au lieu d'avoir un setter pour chacun de ceux-ci, avez une méthode appelée setDate(int m, int d, int y) qui définit la date. Vous pouvez avoir une méthode getter pour chaque morceau de données.

Ajoutez deux constructeurs : un qui ne prend aucune donnée et définit la date à 1/1/2000, et un autre qui prend trois ints pour définir la date.

Incluez une méthode print() qui imprimera la date dans ce format : MM/JJ/AAAA et une méthode appelée printLong() qui imprime dans ce format : `NomDuMois Jour, Année`. Par exemple, le premier jour du 21e siècle doit imprimer `1er janvier 2000`.

Incluez une méthode pour ajouter un certain nombre de jours, de mois et d'années à une Date :

```cpp
void addDays(int d)
void addMonths(int m)
void addYears(int y)
```

#### **Problème 2**

Le problème 2 vous demande de créer quelques classes liées pour jouer à des jeux de cartes. Les données nécessaires pour être stockées pour une carte sont une valeur numérique et une couleur. Une carte est responsable de pouvoir s'afficher elle-même. Par exemple, lorsque nous voulons afficher un deux de cœur, un dix de carreau, un valet de trèfle ou un as de pique, la sortie ressemblerait à ceci :

```plaintext
2 de Cœur
10 de Carreau
V de Trèfle
A de Pique
```

Ensuite, créez une classe de jeu. Un jeu est une collection de cinquante-deux cartes. Chaque carte est unique. Il doit y avoir une carte avec une valeur numérique de deux à l'as dans chacune des quatre couleurs. Les responsabilités de la classe de jeu sont qu'elle doit pouvoir se mélanger et distribuer un certain nombre de cartes du jeu. Pour mélanger le jeu, vous devrez déplacer aléatoirement les cartes dans le jeu. Vous pouvez générer un nombre aléatoire en C++ en utilisant la fonction rand().

Lors de la distribution des cartes, l'utilisateur demandera au jeu un certain nombre de cartes. S'il y a assez de cartes dans le jeu, il doit distribuer ces cartes. Une fois qu'une carte est distribuée du jeu, elle ne peut pas être redistribuée à partir du même jeu. L'utilisateur passera un vecteur de cartes et le jeu le remplira avec le nombre de cartes demandé. S'il n'y a pas assez de cartes dans le jeu, imprimez un message d'erreur puis terminez le programme avec un exit(0).

Lors de la création d'une classe, vous devez toujours réfléchir aux données nécessaires pour la classe et aux responsabilités de la classe. Les données de la classe doivent être privées et une interface pour la classe doit être fournie.

Réfléchissez à la manière dont chaque carte et jeu doit être construit. Écrivez au moins un constructeur pour chaque classe. Écrivez d'abord la classe de carte et testez-la dans un programme pilote. Ensuite, travaillez sur la classe de jeu.

Pour tester le jeu, créez un objet de jeu, demandez 52 cartes et imprimez chacune de ces cartes à l'écran.

Ensuite, modifiez le programme pour qu'il permette à une personne d'évaluer les probabilités d'obtenir certaines mains de poker. Le poker est un jeu de cartes joué avec un jeu de 52 cartes. Dans ce programme, vous n'avez besoin de gérer que la variété de poker à cinq cartes. Le programme obtiendra de manière répétée des groupes de cinq cartes du jeu et comptera combien de fois chaque main se produit.

Dans la plupart des variantes du poker, la précédence des mains est la suivante :

```plaintext
Quinte Flush Royale - 5 cartes qui sont une quinte (5 cartes en ordre numérique) et une couleur (5 cartes de la même couleur) du 10 à l'As.
Quinte Flush - 5 cartes qui sont une quinte (5 cartes en ordre numérique) et une couleur (5 cartes de la même couleur).
Carré - n'importe quelles 4 cartes avec le même numéro.
Full - un brelan (3 cartes avec le même numéro) et une paire (deux cartes avec le même numéro).
Couleur - n'importe quelles 5 cartes de la même couleur.
Quinte - n'importe quelles 5 cartes en ordre numérique.
Brelan - n'importe quelles 3 cartes avec le même numéro.
Deux Paires - 2 ensembles de paires.
Paire - n'importe quelles 2 cartes avec le même numéro.
Carte Haute dans votre Main - si vous n'avez aucune des mains ci-dessus, votre carte haute est la meilleure main.
```

Vous devrez créer des classes supplémentaires avec plus de responsabilités que les classes Deck et Card.

Votre programme a besoin d'un 'évaluateur' qui peut examiner une collection de cartes et déterminer la meilleure main qui peut être faite à partir de ces cartes. Afin de déterminer les probabilités, distribuez un grand nombre de mains et gardez une trace du nombre de fois que chaque main apparaît.

En d'autres termes, votre programme pourrait créer 100 000 collections de cinq cartes à évaluer. L'évaluateur comptera combien de fois une quinte flush royale apparaît, combien de fois une quinte flush apparaît, et ainsi de suite. Votre programme montrera les probabilités en pourcentages de la probabilité d'obtenir chaque main.

Ci-dessous se trouve un pilote pour illustrer comment utiliser l'évaluateur :

```cpp
int main()
{
    //évaluateur de cinq cartes
    //créer un évaluateur de poker pour le poker à cinq cartes
    PokerEvaluator fiveCardPokerEvaluator;

    //définir le nombre de mains à jouer - cent mille cette fois
    fiveCardPokerEvaluator.setNumberOfHandsToPlay(100000);

    //jouer toutes les mains et suivre les statistiques, puis imprimer les résultats à l'écran
    fiveCardPokerEvaluator.playAndDisplay();

    return 0;
}
```

## **Partie 10 : Structures de Données**

Cette section décrit comment construire quelques structures de données courantes : une table de hachage, un arbre de recherche binaire et un graphe. Elle décrit également comment utiliser la classe `unordered_map` de la STL.

* [10.1 Liste chaînée simple](https://playbackpress.com/books/cppbook/chapter/10/1)
    
* [10.2 Table de hachage simple](https://playbackpress.com/books/cppbook/chapter/10/2)
    
* [10.3 Table de hachage plus complexe](https://playbackpress.com/books/cppbook/chapter/10/3)
    
* [10.4 `unordered_map` de la STL](https://playbackpress.com/books/cppbook/chapter/10/4)
    
* [10.5 Arbre de recherche binaire](https://playbackpress.com/books/cppbook/chapter/10/5)
    
* [10.6 Matrice d'adjacence de graphe](https://playbackpress.com/books/cppbook/chapter/10/6)
    

### **Pratique Pratique**

Maintenant que vous avez passé en revue les parcours de code guidés, écrivez un programme qui inclut une classe équivalente au `vector` appelée SafeArray. SafeArray a une méthode appelée `at` qui retourne l'élément à la position spécifiée.

Un SafeArray maintient un pointeur vers un tableau sur le tas. Utilisez le pointeur pour faire croître et réduire le tableau avec des appels à `push_back` et `pop_back`.

Le SafeArray aura une méthode appelée `size` qui retourne le nombre d'éléments qu'il contient. Incluez un constructeur par défaut qui définit la taille initiale du tableau sous-jacent pour contenir 10 éléments. Incluez un destructeur pour `delete` le tableau lorsque le SafeArray sort de la portée.

## **Partie 11 : Bases de Données SQLite**

Cette section décrit le travail avec une base de données SQLite. SQLite est mon système de gestion de bases de données (SGBD) préféré, car il est puissant et facile à ajouter à n'importe quel programme. Cette section suppose que vous êtes familiarisé avec la conception de bases de données relationnelles et SQL.

Le premier programme montre comment utiliser l'API pour écrire et exécuter des requêtes SQL dans un programme C++. Dans le second, une partie du code répétitif est abstraite dans une classe séparée. Dans le troisième, les transactions dans SQLite sont expliquées et il montre qu'elles peuvent être utilisées pour garantir les propriétés ACID d'une base de données :

* [11.1 L'API C++ SQLite](https://playbackpress.com/books/cppbook/chapter/11/1)
    
* [11.2 Un Programme d'Enchères Orienté Objet](https://playbackpress.com/books/cppbook/chapter/11/2)
    
* [11.3 Transactions SQLite](https://playbackpress.com/books/cppbook/chapter/11/3)
    

### **Pratique Pratique**

Étendez le programme d'enchères du deuxième playback pour inclure une méthode qui imprime les noms et adresses e-mail de tous les utilisateurs qui ont remporté une enchère. Ensuite, écrivez une méthode qui imprime un article suivi des noms et adresses e-mail de toute personne ayant fait une offre sur l'article.

## **Commentaires et Retours**

Vous pouvez trouver toutes ces lectures de code dans mon livre gratuit, [Une Introduction Animée à la Programmation en C++](https://playbackpress.com/books/cppbook/). Il y a d'autres livres gratuits ici :

* [Une Introduction Animée à la Programmation avec Python](https://playbackpress.com/books/pybook)
    
* [Conception de Base de Données et SQL pour Débutants](https://playbackpress.com/books/sqlbook)
    
* [Exemples SQL Travaillés](https://playbackpress.com/books/workedsqlbook)
    
* [Programmation avec SQLite](https://playbackpress.com/books/sqlitebook)
    
* [Une Introduction au Développement Web de l'Arrière à l'Avant](https://playbackpress.com/books/webdevbook)
    
* [Une Introduction Animée à Clojure](https://playbackpress.com/books/cljbook)
    
* [Une Introduction Animée à Elixir](https://playbackpress.com/books/exbook)
    
* [Une Brève Introduction à Ruby](https://playbackpress.com/books/rubybook)
    
* [Développement d'Applications Mobiles avec Dart et Flutter](https://playbackpress.com/books/flutterbook)
    
* [Modèles de Conception OO avec Java](https://playbackpress.com/books/patternsbook)
    
* [Comment je l'ai construit : Word Zearch](https://playbackpress.com/books/wordzearchbook)
    
Les commentaires et retours sont les bienvenus par e-mail : [mark@playbackpress.com](mailto:mark@playbackpress.com).

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don en utilisant [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !