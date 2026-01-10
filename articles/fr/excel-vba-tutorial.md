---
title: Tutoriel Excel VBA – Comment écrire du code dans une feuille de calcul en utilisant
  Visual Basic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/excel-vba-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/excel-1771393_1920.jpg
tags:
- name: excel
  slug: excel
- name: VBA
  slug: vba
- name: visual basic
  slug: visual-basic
seo_title: Tutoriel Excel VBA – Comment écrire du code dans une feuille de calcul
  en utilisant Visual Basic
seo_desc: 'By Chloe Tucker

  Introduction

  This is a tutorial about writing code in Excel spreadsheets using Visual Basic for
  Applications (VBA).

  Excel is one of Microsoft’s most popular products. In 2016, the CEO of Microsoft
  said  "Think about a world without Ex...'
---

Par Chloe Tucker

# Introduction

Ce tutoriel explique comment écrire du code dans des feuilles de calcul Excel en utilisant Visual Basic pour Applications (VBA).

Excel est l'un des produits les plus populaires de Microsoft. En 2016, le PDG de Microsoft a déclaré : "Imaginez un monde sans Excel. C'est juste impossible pour moi." Eh bien, peut-être que le monde ne peut pas se passer d'Excel.

* En 1996, il y avait plus de 30 millions d'utilisateurs de Microsoft Excel ([source](https://news.microsoft.com/1996/05/20/more-than-30-million-users-make-microsoft-excel-the-worlds-most-popular-spreadsheet-program/)).
* Aujourd'hui, on estime à 750 millions le nombre d'utilisateurs de Microsoft Excel. C'est un peu plus que la population de l'Europe et 25 fois plus d'utilisateurs qu'en 1996.

Nous sommes une grande famille heureuse !

Dans ce tutoriel, vous apprendrez à utiliser VBA et à écrire du code dans une feuille de calcul Excel en utilisant Visual Basic.

### Prérequis

Vous n'avez besoin d'aucune expérience préalable en programmation pour comprendre ce tutoriel. Cependant, vous aurez besoin de :

* Une familiarité basique à intermédiaire avec Microsoft Excel
* Si vous souhaitez suivre les exemples VBA de cet article, vous aurez besoin d'un accès à Microsoft Excel, de préférence la dernière version (2019), mais Excel 2016 et Excel 2013 fonctionneront très bien.
* Une volonté d'essayer de nouvelles choses

### Objectifs d'apprentissage

Au cours de cet article, vous apprendrez :

1. Ce qu'est VBA
2. Pourquoi utiliser VBA
3. Comment se configurer dans Excel pour écrire en VBA
4. Comment résoudre certains problèmes réels avec VBA

### Concepts importants

Voici quelques concepts importants avec lesquels vous devriez être familier pour comprendre pleinement ce tutoriel.

**Objets** : Excel est orienté objet, ce qui signifie que tout est un objet - la fenêtre Excel, le classeur, une feuille, un graphique, une cellule. VBA permet aux utilisateurs de manipuler et d'effectuer des actions avec des objets dans Excel.

Si vous n'avez aucune expérience avec la programmation orientée objet et que ce concept est nouveau pour vous, prenez un moment pour le comprendre !

**Procédures** : une procédure est un ensemble de code VBA, écrit dans l'éditeur Visual Basic, qui accomplit une tâche. Parfois, cela est également appelé une macro (plus sur les macros ci-dessous). Il existe deux types de procédures :

* Subroutines : un groupe d'instructions VBA qui effectue une ou plusieurs actions
* Fonctions : un groupe d'instructions VBA qui effectue une ou plusieurs actions et <ins>retourne une ou plusieurs valeurs</ins>

Note : vous pouvez avoir des fonctions qui opèrent à l'intérieur de subroutines. Vous verrez cela plus tard.

**Macros** : Si vous avez passé du temps à apprendre des fonctionnalités avancées d'Excel, vous avez probablement rencontré le concept de "macro". Les utilisateurs d'Excel peuvent enregistrer des macros, composées de commandes/utilisateur/frappes/clics, et les rejouer à une vitesse fulgurante pour accomplir des tâches répétitives. Les macros enregistrées génèrent du code VBA, que vous pouvez ensuite examiner. C'est en fait assez amusant d'enregistrer une macro simple et de regarder le code VBA.

Veuillez garder à l'esprit qu'il peut parfois être plus facile et plus rapide d'enregistrer une macro plutôt que de coder manuellement une procédure VBA.

Par exemple, peut-être que vous travaillez dans la gestion de projet. Une fois par semaine, vous devez transformer un rapport exporté brut de votre système de gestion de projet en un rapport propre et bien formaté pour la direction. Vous devez formater les noms des projets dépassant le budget en texte rouge gras. Vous pourriez enregistrer les modifications de formatage en tant que macro et l'exécuter chaque fois que vous devez apporter la modification.

# Qu'est-ce que VBA ?

Visual Basic pour Applications est un langage de programmation développé par Microsoft. Chaque programme logiciel de la suite Microsoft Office est livré avec le langage VBA sans frais supplémentaires. VBA permet aux utilisateurs de Microsoft Office de créer de petits programmes qui fonctionnent dans les programmes logiciels de Microsoft Office.

Pensez à VBA comme à un four à pizza dans un restaurant. Excel est le restaurant. La cuisine est équipée d'appareils commerciaux standard, comme de grands réfrigérateurs, des cuisinières et des fours ordinaires - ce sont toutes les fonctionnalités standard d'Excel.

Mais que faire si vous voulez faire de la <ins>pizza cuite au feu de bois</ins> ? Vous ne pouvez pas faire cela dans un four de cuisson commercial standard. VBA est le four à pizza.

![Pizza dans un four à pizza](https://www.freecodecamp.org/news/content/images/2021/11/1-Pizza.jpeg)

Miam.

# Pourquoi utiliser VBA dans Excel ?

Parce que la pizza cuite au feu de bois est la meilleure !

Mais sérieusement.

Beaucoup de gens passent _beaucoup_ de temps dans Excel dans le cadre de leur travail. Le temps dans Excel passe différemment aussi. Selon les circonstances, 10 minutes dans Excel peuvent sembler une éternité si vous ne pouvez pas faire ce dont vous avez besoin, ou 10 heures peuvent passer très rapidement si tout se passe bien. C'est à ce moment-là que vous devriez vous demander, **pourquoi diable est-ce que je passe 10 heures dans Excel ?**

Parfois, ces journées sont inévitables. Mais si vous passez 8 à 10 heures chaque jour dans Excel à faire des tâches répétitives, à répéter beaucoup des mêmes processus, à essayer de nettoyer après d'autres utilisateurs du fichier, ou même à mettre à jour d'autres fichiers après des modifications apportées au fichier Excel, une procédure VBA pourrait bien être la solution pour vous.

Vous devriez envisager d'utiliser VBA si vous avez besoin de :

* Automatiser des tâches répétitives
* Créer des moyens faciles pour les utilisateurs d'interagir avec vos feuilles de calcul
* Manipuler de grandes quantités de données

# Configuration pour écrire du VBA dans Excel

## Onglet Développeur

Pour écrire du VBA, vous devrez ajouter l'onglet Développeur au ruban, afin que vous voyiez le ruban comme ceci.

![Onglet développeur VBA](https://www.freecodecamp.org/news/content/images/2021/11/2-Developer-Tab.png)

Pour ajouter l'onglet Développeur au ruban :

1. Dans l'onglet Fichier, allez dans Options > Personnaliser le ruban.
2. Sous Personnaliser le ruban et sous Onglets principaux, sélectionnez la case à cocher Développeur.

Après avoir affiché l'onglet, l'onglet Développeur reste visible, sauf si vous décochez la case ou devez réinstaller Excel. [Pour plus d'informations, voir la documentation d'aide de Microsoft.](https://support.office.com/en-us/article/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45)

## Éditeur VBA

Accédez à l'onglet Développeur et cliquez sur le bouton Visual Basic. Une nouvelle fenêtre s'ouvrira - c'est l'éditeur Visual Basic. Pour les besoins de ce tutoriel, vous devez simplement être familier avec le volet Explorateur de projets et le volet Propriétés.

![Éditeur VBA](https://www.freecodecamp.org/news/content/images/2020/06/VBA-Editor.png)

# Exemples de VBA Excel

Tout d'abord, créons un fichier pour nous amuser.

1. Ouvrez un nouveau fichier Excel
2. Enregistrez-le en tant que classeur avec macros (.xlsm)
3. Sélectionnez l'onglet Développeur
4. Ouvrez l'éditeur VBA

Commençons avec quelques exemples faciles pour vous faire écrire du code dans une feuille de calcul en utilisant Visual Basic.

## Exemple #1 : Afficher un message lorsque les utilisateurs ouvrent le classeur Excel

Dans l'éditeur VBA, sélectionnez Insertion -> Nouveau Module

Écrivez ce code dans la fenêtre du Module (ne collez pas !) :

Sub Auto_Open()
  MsgBox ("Bienvenue dans le classeur XYZ.")
End Sub

Enregistrez, fermez le classeur et rouvrez le classeur. Ce dialogue devrait s'afficher.

![Message de bienvenue dans le classeur XYZ](https://www.freecodecamp.org/news/content/images/2021/11/3-Welcome-to-XYZ-Notebook.png)

Et voilà !

### Comment cela fonctionne-t-il ?

Selon votre familiarité avec la programmation, vous pouvez avoir quelques idées. Ce n'est pas particulièrement complexe, mais il se passe beaucoup de choses :

* Sub (abréviation de "Subroutine") : rappelez-vous du début, "un groupe d'instructions VBA qui effectue une ou plusieurs actions."
* Auto_Open : c'est la subroutine spécifique. Elle exécute automatiquement votre code lorsque le fichier Excel s'ouvre - c'est l'événement qui déclenche la procédure. Auto_Open ne s'exécutera que lorsque le classeur est ouvert manuellement ; il ne s'exécutera pas si le classeur est ouvert via du code à partir d'un autre classeur (Workbook_Open le fera, [en savoir plus sur la différence entre les deux](https://www.pcreview.co.uk/threads/auto_open-vs-workbook_open.953960/)).
* Par défaut, l'accès à une subroutine est public. Cela signifie que tout autre module peut utiliser cette subroutine. Tous les exemples de ce tutoriel seront des subroutines publiques. Si nécessaire, vous pouvez déclarer des subroutines comme privées. Cela peut être nécessaire dans certaines situations. [En savoir plus sur les modificateurs d'accès des subroutines.](https://www.thespreadsheetguru.com/blog/2014/3/5/explaining-private-vs-public-declarations)
* msgBox : c'est une fonction - un groupe d'instructions VBA qui effectue une ou plusieurs actions et retourne une valeur. La valeur retournée est le message "Bienvenue dans le classeur XYZ."

En bref, c'est une subroutine simple qui contient une fonction.

### Quand pourrais-je utiliser cela ?

Peut-être avez-vous un fichier très important qui est rarement consulté (par exemple, une fois par trimestre), mais automatiquement mis à jour quotidiennement par une autre procédure VBA. Lorsqu'il est consulté, c'est par de nombreuses personnes dans plusieurs départements, dans toute l'entreprise.

* Problème : La plupart du temps, lorsque les utilisateurs consultent le fichier, ils sont confus quant à l'objectif de ce fichier (pourquoi il existe), comment il est mis à jour si souvent, qui le maintient et comment ils doivent interagir avec lui. Les nouveaux employés ont toujours beaucoup de questions, et vous devez répondre à ces questions encore et encore.
* Solution : créer un message utilisateur qui contient une réponse concise à chacune de ces questions fréquemment posées.

### Exemples réels

* Utilisez la fonction MsgBox pour afficher un message lors de tout événement : l'utilisateur ferme un classeur Excel, l'utilisateur imprime, une nouvelle feuille est ajoutée au classeur, etc.
* Utilisez la fonction MsgBox pour afficher un message lorsque l'utilisateur doit remplir une condition avant de fermer un classeur Excel
* Utilisez la fonction InputBox pour obtenir des informations de l'utilisateur

## Exemple #2 : Permettre à l'utilisateur d'exécuter une autre procédure

Dans l'éditeur VBA, sélectionnez Insertion -> Nouveau Module

Écrivez ce code dans la fenêtre du Module (ne collez pas !) :

Sub UserReportQuery()
Dim UserInput As Long
Dim Answer As Integer
UserInput = vbYesNo
Answer = MsgBox("Traiter le rapport XYZ ?", UserInput)
If Answer = vbYes Then ProcessReport
End Sub

Sub ProcessReport()
MsgBox ("Merci d'avoir traité le rapport XYZ.")
End Sub

Enregistrez et revenez à l'onglet Développeur d'Excel et sélectionnez l'option "Bouton". Cliquez sur une cellule et attribuez la macro UserReportQuery au bouton.

Cliquez maintenant sur le bouton. Ce message devrait s'afficher :

![Message de traitement du rapport XYZ](https://www.freecodecamp.org/news/content/images/2021/11/4-Process-the-Report.png)

Cliquez sur "oui" ou appuyez sur Entrée.

![Message de remerciement pour le traitement du rapport XYZ](https://www.freecodecamp.org/news/content/images/2021/11/5-Thanks-for-Processing-the-Report.png)

Encore une fois, et voilà !

Veuillez noter que la subroutine secondaire, ProcessReport, pourrait être _n'importe quoi_. Je démontrerai plus de possibilités dans l'exemple #3. Mais d'abord...

### Comment cela fonctionne-t-il ?

Cet exemple s'appuie sur l'exemple précédent et comporte plusieurs nouveaux éléments. Passons en revue les nouvelles fonctionnalités :

* Dim UserInput As Long : Dim est l'abréviation de "dimension" et vous permet de déclarer des noms de variables. Dans ce cas, UserInput est le nom de la variable et Long est le type de données. En anglais simple, cette ligne signifie "Voici une variable appelée 'UserInput', et c'est un type de variable Long."
* Dim Answer As Integer : déclare une autre variable appelée "Answer", avec un type de données Integer. [En savoir plus sur les types de données ici.](https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/data-types/)
* UserInput = vbYesNo : attribue une valeur à la variable. Dans ce cas, vbYesNo, qui affiche les boutons Oui et Non. Il existe _de nombreux_ types de boutons, [en savoir plus ici](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/msgbox-function).
* Answer = MsgBox("Traiter le rapport XYZ ?", UserInput) : attribue la valeur de la variable Answer pour qu'elle soit une fonction MsgBox et la variable UserInput. Oui, une variable dans une variable.
* If Answer = vbYes Then ProcessReport : il s'agit d'une "instruction If", une instruction conditionnelle, qui nous permet de dire si x est vrai, alors faites y. Dans ce cas, si l'utilisateur a sélectionné "Oui", alors exécutez la subroutine ProcessReport.

### Quand pourrais-je utiliser cela ?

Cela pourrait être utilisé de nombreuses manières. La valeur et la polyvalence de cette fonctionnalité sont davantage définies par ce que fait la subroutine secondaire.

Par exemple, peut-être avez-vous un fichier utilisé pour générer 3 rapports hebdomadaires différents. Ces rapports sont formatés de manières très différentes.

* Problème : Chaque fois que l'un de ces rapports doit être généré, un utilisateur ouvre le fichier et modifie le formatage et les graphiques ; et ainsi de suite. Ce fichier est modifié de manière extensive au moins 3 fois par semaine, et cela prend au moins 30 minutes chaque fois qu'il est modifié.
* Solution : créez 1 bouton par type de rapport, qui reformate automatiquement les composants nécessaires des rapports et génère les graphiques nécessaires.

### Exemples réels

* Créez une boîte de dialogue pour que l'utilisateur puisse remplir automatiquement certaines informations sur plusieurs feuilles
* Utilisez la fonction InputBox pour obtenir des informations de l'utilisateur, qui sont ensuite remplies sur plusieurs feuilles

## Exemple #3 : Ajouter des nombres à une plage avec une boucle For-Next

Les boucles For sont très utiles si vous devez effectuer des tâches répétitives sur une plage spécifique de valeurs - des tableaux ou des plages de cellules. En anglais simple, une boucle dit "pour chaque x, faites y."

Dans l'éditeur VBA, sélectionnez Insertion -> Nouveau Module

Écrivez ce code dans la fenêtre du Module (ne collez pas !) :

Sub LoopExample()
Dim X As Integer
For X = 1 To 100
    Range("A" & X).Value = X
Next X
End Sub

Enregistrez et revenez à l'onglet Développeur d'Excel et sélectionnez le bouton Macros. Exécutez la macro LoopExample.

Cela devrait se produire :

![Résultats de la boucle For-Next](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-01-at-2.53.02-PM.png)

Et ainsi de suite, jusqu'à la 100ème ligne.

### Comment cela fonctionne-t-il ?

* Dim X As Integer : déclare la variable X comme un type de données Integer.
* For X = 1 To 100 : c'est le début de la boucle For. Simplement, cela indique à la boucle de continuer à se répéter jusqu'à ce que X = 100. X est le _compteur_. La boucle continuera à s'exécuter jusqu'à ce que X = 100, s'exécute une dernière fois, puis s'arrête.
* Range("A" & X).Value = X : cela déclare la plage de la boucle et ce qu'il faut mettre dans cette plage. Puisque X = 1 initialement, la première cellule sera A1, moment auquel la boucle mettra X dans cette cellule.
* Next X : cela indique à la boucle de s'exécuter à nouveau

### Quand pourrais-je utiliser cela ?

La boucle For-Next est l'une des fonctionnalités les plus puissantes de VBA ; il existe de nombreux cas d'utilisation potentiels. Il s'agit d'un exemple plus complexe qui nécessiterait plusieurs couches de logique, mais il communique le monde des possibilités dans les boucles For-Next.

Peut-être avez-vous une liste de tous les produits vendus dans votre boulangerie dans la colonne A, le type de produit dans la colonne B (gâteaux, beignets ou muffins), le coût des ingrédients dans la colonne C, et le coût moyen du marché de chaque type de produit dans une autre feuille.

Vous devez déterminer quel devrait être le prix de détail de chaque produit. Vous pensez qu'il devrait être le coût des ingrédients plus 20 %, mais aussi 1,2 % en dessous de la moyenne du marché si possible. Une boucle For-Next vous permettrait de faire ce type de calcul.

### Exemples réels

* Utilisez une boucle avec une instruction if imbriquée pour ajouter des valeurs spécifiques à un tableau séparé uniquement si elles répondent à certaines conditions
* Effectuez des calculs mathématiques sur chaque valeur d'une plage, par exemple, calculez des frais supplémentaires et ajoutez-les à la valeur
* Parcourez chaque caractère d'une chaîne et extrayez tous les nombres
* Sélectionnez aléatoirement un certain nombre de valeurs dans un tableau

# Conclusion

Maintenant que nous avons parlé de pizza et de muffins et oh-oui, comment écrire du code VBA dans des feuilles de calcul Excel, faisons un contrôle d'apprentissage. Voyez si vous pouvez répondre à ces questions.

* Qu'est-ce que VBA ?
* Comment me configurer pour commencer à utiliser VBA dans Excel ?
* Pourquoi et quand utiliseriez-vous VBA ?
* Quels sont certains problèmes que je pourrais résoudre avec VBA ?

Si vous avez une idée assez claire de la manière de répondre à ces questions, alors ce tutoriel a été un succès.

Que vous soyez un utilisateur occasionnel ou un utilisateur avancé, j'espère que ce tutoriel a fourni des informations utiles sur ce qui peut être accompli avec un peu de code dans vos feuilles de calcul Excel.

Bon codage !

## Ressources d'apprentissage

* Programmation Excel VBA pour les Nuls, John Walkenbach
* [Commencer avec VBA, Documentation Microsoft](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office)
* [Apprendre VBA dans Excel, Lynda](https://www.lynda.com/Excel-tutorials/Learning-VBA-Excel/802840-2.html?srchtrk=index%3a5%0alinktypeid%3a2%0aq%3avba%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2)

## Un peu à propos de moi

Je suis Chloe Tucker, une artiste et développeuse à Portland, Oregon. En tant qu'ancienne éducatrice, je recherche continuellement l'intersection de l'apprentissage et de l'enseignement, ou de la technologie et de l'art. Contactez-moi sur Twitter [@_chloetucker](https://twitter.com/_chloetucker) et consultez mon site web à l'adresse [chloe.dev](https://chloe.dev/).