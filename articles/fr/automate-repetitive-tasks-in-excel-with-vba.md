---
title: Tutoriel Visual Basic Excel – Comment automatiser les tâches répétitives dans
  une feuille de calcul
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-29T15:35:00.000Z'
originalURL: https://freecodecamp.org/news/automate-repetitive-tasks-in-excel-with-vba
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Thumbnail2.png
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: visual basic
  slug: visual-basic
seo_title: Tutoriel Visual Basic Excel – Comment automatiser les tâches répétitives
  dans une feuille de calcul
seo_desc: "By Sander Vreeken\nI use VBA, or Visual Basic for Applications, to automate\
  \ my repetitive tasks. This saves me quite a lot of time in my day-to-day life.\
  \ \nBased on the fact that you're reading this tutorial, I assume that you would\
  \ like to be able to ..."
---

Par Sander Vreeken

J'utilise VBA, ou Visual Basic pour Applications, pour automatiser mes tâches répétitives. Cela me fait gagner beaucoup de temps dans ma vie quotidienne. 

Étant donné que vous lisez ce tutoriel, je suppose que vous aimeriez pouvoir faire de même.

Je vais donc vous guider à travers les bases de VBA, comme l'utilisation de variables, de boucles, de structures if-else, de tableaux et de dictionnaires.

## Introduction à VBA et aperçu du projet

Bien que VBA ait été déclaré obsolète en 2008, cette implémentation de Visual Basic peut vous aider à automatiser les tâches répétitives de votre vie quotidienne.

Le langage est orienté objet, il est écrit en C++, et il inclut toutes les fonctionnalités que vous attendez d'un langage de programmation de nos jours.

Dans ce tutoriel, nous allons écrire une macro qui prépare un modèle pour noter les températures dans plusieurs villes européennes – Amsterdam, Barcelone, Berlin, Bruxelles, Londres et Rome. 

Le modèle sera automatiquement créé par une macro que nous construirons ensemble en fonction des villes et de la date que nous utiliserons comme paramètres. 

Enfin, nous apprendrons également comment importer les données depuis un autre fichier dans notre modèle.

Pour suivre ce tutoriel, je m'attends à ce que vous ayez une compréhension de base d'Excel. Mais vous n'avez besoin d'aucune expérience avec VBA (bien que cela puisse vous aider à comprendre les différents concepts que je vais introduire).

J'ai téléchargé [plusieurs fichiers Excel de données](https://www.meteoblue.com/) qui sont libres d'utilisation. Vous pouvez également [les trouver sur mon GitHub](https://github.com/SanderVreeken/FreeCodeCamp-VBA-Automation) avec le résultat final.

## Définissons nos paramètres

Tout d'abord, nous allons définir les différentes villes que nous utiliserons pour ce tutoriel. Si nous devions faire cela manuellement, augmenter le nombre de villes signifierait conséquemment plus de travail. 

Mais dans notre cas, puisque la macro fera le travail pour nous, nous pouvons ajouter autant de villes que nous le souhaitons. Ensuite, nous exécuterons simplement la macro et irons faire autre chose.

Pour définir les villes, nous pouvons faire l'une des deux choses suivantes. Soit nous pouvons inclure les villes dans un tableau dans le code, soit nous pouvons les définir dans une feuille de calcul séparée dans notre modèle. 

Pour ce tutoriel, nous allons faire cette dernière option, ce qui facilite l'ajout de villes par d'autres personnes sans aucune connaissance de VBA.

### Comment configurer le classeur Excel

Ouvrez un nouveau fichier Excel, enregistrez-le en tant que Classeur Excel avec macros (extension .xlsm), et nommez-le comme vous le souhaitez. 

Renommez la première feuille de calcul en Villes et ajoutez les six villes en tapant leurs noms dans la première colonne avec une ville sur chaque ligne, comme montré ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-83.png)
_Figure 01 : Feuille de calcul Villes_

Pour définir la date, nous allons créer une autre feuille de calcul appelée Date où l'utilisateur peut définir le mois pour lequel il souhaite que le modèle soit créé. 

Puisque toutes les années et tous les mois ne sont pas identiques (par exemple, nombre différent de jours, nombre différent de jours de semaine), le modèle pour vos données doit être ajusté chaque mois afin d'afficher correctement ces différences. 

J'ai également ajouté une validation des données pour m'assurer que nous ne pouvons entrer qu'une date et pour m'assurer qu'elle ne dépasse pas la date d'aujourd'hui (mais cela est complètement facultatif). Tant que vous avez une cellule avec une date, de préférence la cellule B1, cela suffit.

Pour ce tutoriel, nous n'aurons besoin que du mois et de l'année, j'ai donc choisi un format de date différent comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-89.png)
_Figure 02 : Feuille de calcul Date_

## Comment créer une macro avec Visual Basic pour Applications

Maintenant que nous avons défini les paramètres, nous pouvons passer à la création de la macro.

Si c'est la première fois que vous utilisez VBA, vous devrez peut-être personnaliser votre ruban pour obtenir les fonctions nécessaires.

Pour ce faire, assurez-vous que la case Développeur est cochée (comme montré dans la Figure 3 ci-dessous) et que les options Développeur sont disponibles dans votre ruban après avoir enregistré vos modifications.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-85.png)
_Figure 03 : Paramètres Excel_

Vous devriez maintenant pouvoir ouvrir Visual Basic depuis l'onglet Développeur dans Excel, ce qui devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-86.png)
_Figure 04 : Visual Basic_

C'est l'éditeur fourni par Excel où vous pourrez créer, ajuster et supprimer vos fonctions et macros. Je ne vais pas entrer dans trop de détails pour l'instant, mais je vais expliquer certains des éléments au fur et à mesure.

Maintenant, mettons les mains dans le cambouis et écrivons notre première macro.   
  
Vous pourriez choisir d'écrire des macros pour une seule feuille de calcul, ou choisir de les avoir disponibles dans tout le classeur. 

Comme les deux feuilles de calcul que nous avons créées précédemment ne maintiennent que les paramètres, j'ai choisi d'écrire les macros pour tout le classeur en double-cliquant sur l'option "ThisWorkbook" dans la barre latérale de notre projet. 

_Ne vous inquiétez pas pour le PERSONAL.xlsb dans ma capture d'écran pour l'instant – c'est un fichier contenant des fonctions que je peux utiliser dans tous mes fichiers et qui sera traité dans un futur tutoriel._

### Comment créer notre première macro

Après avoir sélectionné le classeur, vous êtes prêt à commencer votre premier programme.

Les macros en VBA commencent par le mot-clé Sub, abréviation de subroutine, suivi de leur nom et de deux parenthèses. Bien que l'éditeur ne soit rien comparé à un IDE comme Visual Studio Code, il complétera le code avec End Sub lorsque vous appuierez sur Entrée après les deux parenthèses. 

Pour l'instant, j'ai créé une macro vide appelée `CreateTemplate` qui ressemble à ceci :

```vba
Sub CreateTemplate()

End Sub
```

Il est un peu triste que la fonction ne fasse rien pour l'instant, alors ajoutons le code suivant et voyons ce qu'il fait :

```vba
Sub CreateTemplate()

    'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur, à côté de la feuille de calcul actuellement sélectionnée.
    Sheets.Add.Name = "NewSheet"
    
End Sub
```

Si nous exécutions ce code maintenant, la fonction créerait une nouvelle feuille de calcul dans notre classeur Excel appelée NewSheet. 

Notez que j'ai inclus un commentaire dans le code en commençant la ligne par une apostrophe. Cela ne sera pas exécuté, mais est seulement là pour vous aider, vous et moi, à comprendre le code. 

Nous pouvons exécuter ce code en plaçant notre curseur quelque part dans la fonction et en appuyant sur l'icône verte 'play' en haut de l'éditeur, qui dit Run Sub lorsque vous passez la souris dessus. 

Après avoir appuyé sur ce bouton, vous verrez qu'une nouvelle feuille de calcul appelée NewSheet a été créée dans notre classeur et a également été ajoutée dans la barre latérale, à côté des feuilles que nous avions déjà.

Personnellement, je n'aime pas le fait que la feuille soit créée à côté de la feuille que nous avions (peut-être intentionnellement, peut-être pas) sélectionnée. Par conséquent, je vais ajouter un paramètre à la méthode add pour définir son emplacement :

```vba
Sub CreateTemplate()
    
    'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur, à côté de la feuille de calcul Date.
    Sheets.Add(After:=Sheets("Date")).Name = "NewSheet"
    
End Sub
```

Supprimez la feuille nouvellement créée, car nous allons maintenant créer les feuilles de calcul pour chaque ville que nous avons définie précédemment. Comme le nombre de villes entrées peut différer, nous voulons savoir combien de lignes sont réellement utilisées dans notre feuille de calcul Villes.

```vba
Sub CreateTemplate()

    Debug.Print Worksheets("Cities").UsedRange.Rows.Count
    
End Sub
```

Pour tester si nous sommes capables d'extraire la date du fichier, nous utilisons `Debug.Print` (similaire à print en Python ou console.log en JavaScript) pour imprimer le nombre de lignes, que Excel calculera pour nous en fonction du code que nous avons fourni.

Assurez-vous d'ouvrir votre Fenêtre Immédiate (dans Visual Basic, en sélectionnant Affichage > Fenêtre Immédiate) et exécutez la macro ci-dessus. Elle imprimera six, comme nous nous y attendons, après avoir défini le même nombre de villes dans notre feuille de calcul Villes plus tôt dans ce tutoriel.

## Comment stocker des valeurs en tant que variables dans VBA

Plutôt que d'imprimer cette valeur, je veux la stocker en tant que variable. Pour ce faire, ajoutez le code suivant :

```vba
Sub CreateTemplate()
    'Variable qui contiendra le nombre de villes.
    Dim NumberOfCities As Integer
    
    NumberOfCities = Worksheets("Cities").UsedRange.Rows.Count
    Debug.Print NumberOfCities
    
End Sub
```

Nous utilisons le mot-clé Dim en VBA pour déclarer une variable, qui doit toujours inclure le type (par exemple String, Integer, Double). 

Après avoir déclaré notre variable, nous pouvons assigner le nombre de lignes utilisées, comme imprimé précédemment, à cette variable et imprimer le nombre pour tester que nous obtenons le même résultat. Vous pouvez voir cela dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-90.png)
_Figure 05 : Impression dans la Fenêtre Immédiate_

Nous pouvons maintenant utiliser ce nombre pour définir une boucle qui créera une feuille pour chaque ville.

```vba
Sub CreateTemplate()
    'Variable qui contiendra le nom de la ville utilisé pour nommer une feuille.
    Dim CityName As String
    'Variable qui contiendra le nombre de villes.
    Dim NumberOfCities As Integer
    'Variable qui sera utilisée pour suivre l'index de la boucle pour créer des feuilles de calcul.
    Dim SheetIndex As Integer
    
    NumberOfCities = Worksheets("Cities").UsedRange.Rows.Count
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur en dernier pour assurer l'ordre alphabétique.
        Sheets.Add(After:=Sheets(Sheets.Count)).Name = CityName
    Next SheetIndex
    
End Sub
```

## Comment travailler avec des boucles en VBA

Permettez-moi d'expliquer comment tout cela fonctionne. Dans l'exemple ci-dessus, j'ai déclaré deux variables supplémentaires, à savoir `CityName` et `SheetIndex`, qui contiendront le nom de la ville (que nous utiliserons pour le titre de la feuille) et maintiendront l'index de la boucle.

La boucle elle-même commence par le mot-clé `For`. Par la suite, nous définissons le début de l'index (un dans ce cas) et parcourons jusqu'à ce que le nombre de villes soit atteint. 

Pour chaque itération, la ville a été stockée dans la variable `CityName`, que nous utilisons ensuite pour créer une nouvelle feuille de calcul. Exécutez la fonction et vous verrez les feuilles de calcul être créées avec le titre tel que défini dans notre feuille de calcul Villes. C'est magique, je sais !

Maintenant que les feuilles de calcul sont là, nous pouvons ajouter les dates individuelles pour le mois. Plus tôt, nous avons déjà défini le mois que nous voulons utiliser dans la feuille de calcul Date. Cela peut maintenant nous aider à créer une autre boucle afin que tous les jours du mois soient représentés.

## Comment utiliser des fonctions en VBA

Mais d'abord, nous devons obtenir le nombre de jours du mois que l'utilisateur a entré dans l'onglet Date. Nous pouvons faire cela en utilisant une fonction en VBA. Plutôt que les sous-routines que nous avons utilisées précédemment, nous pouvons également utiliser une fonction qui retourne quelque chose. 

La fonction que nous utilisons maintenant ressemble beaucoup à la fonction que vous pourriez utiliser dans Excel lorsque vous définissez le nombre de jours dans un mois (mais vous utiliseriez `Date` au lieu de `DateSerial`) :

```vba
Function DaysInMonth(DateInput As Date)
    DaysInMonth = Day(DateSerial(Year(DateInput), Month(DateInput) + 1, 1) - 1)
End Function
```

Vous pouvez entrer cette fonction soit au-dessus, soit en dessous de la sous-routine que nous avons définie précédemment, car VBA est un langage compilé plutôt qu'interprété.

_Note – bien que je ne collerai pas la fonction à nouveau, elle sera là pour le reste de ce tutoriel._

Nous pouvons maintenant utiliser cette fonction dans notre sous-routine. Cela facilite beaucoup notre vie, car nous pouvons maintenant utiliser ces superpouvoirs sans polluer notre sous-routine. 

```
Sub CreateTemplate()
    'Variable qui contiendra le nom de la ville utilisé pour nommer une feuille.
    Dim CityName As String
    Dim MonthNum As Integer
    'Variable qui contiendra le nombre de villes.
    Dim NumberOfCities As Integer
    'Variable qui contiendra la date entrée dans la feuille de calcul Date.
    Dim ReportDate As Date
    'Variable qui sera utilisée pour suivre l'index de la boucle pour créer des feuilles de calcul.
    Dim SheetIndex As Integer
    
    NumberOfCities = Worksheets("Cities").UsedRange.Rows.Count
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur en dernier pour assurer l'ordre alphabétique.
        Sheets.Add(After:=Sheets(Sheets.Count)).Name = CityName
    Next SheetIndex
    
    ReportDate = Worksheets("Date").Cells(1, 2)
    Debug.Print DaysInMonth(ReportDate)
    
End Sub
```

Pour l'instant, supprimez les feuilles de calcul avec les noms de villes si vous les aviez créées et exécutez la macro (à nouveau) pour vous assurer que vous avez obtenu le nombre correct de jours imprimé dans la Fenêtre Immédiate pour le mois que vous avez défini précédemment dans la feuille de calcul Date.

Nous pouvons ensuite stocker le nombre de jours en tant qu'entier dans une autre variable (appelée `NumberOfDays`) pour une autre boucle. 

```
Sub CreateTemplate()
    'Variable qui contiendra le nom de la ville utilisé pour nommer une feuille.
    Dim CityName As String
    'Variable qui sera utilisée pour suivre l'index de la boucle pour ajouter les dates individuelles pour le mois.
    Dim DateIndex As Integer
    'Variable qui contiendra le nombre de villes.
    Dim NumberOfCities As Integer
    'Variable qui contiendra le nombre de jours dans le mois choisi
    Dim NumberOfDays As Integer
    'Variable qui contiendra la date entrée dans la feuille de calcul Date.
    Dim ReportDate As Date
    'Variable qui sera utilisée pour suivre l'index de la boucle pour créer des feuilles de calcul.
    Dim SheetIndex As Integer
    
    NumberOfCities = Worksheets("Cities").UsedRange.Rows.Count
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur en dernier pour assurer l'ordre alphabétique.
        Sheets.Add(After:=Sheets(Sheets.Count)).Name = CityName
    Next SheetIndex
    
    ReportDate = Worksheets("Date").Cells(1, 2)
    NumberOfDays = DaysInMonth(ReportDate)
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        
        For DateIndex = 1 To NumberOfDays
            Worksheets(CityName).Cells(DateIndex + 1, 1) = DateSerial(Year(ReportDate), Month(ReportDate), DateIndex)
        Next DateIndex
    Next SheetIndex
    
End Sub
```

Ce sera une boucle dans une boucle pour pimenter un peu ! 🔥 

Je vais vous dire ce que nous faisons ici. Encore une fois, nous parcourons les villes. Mais au lieu de créer une autre feuille de calcul, nous allons maintenant faire autre chose avec la variable `Cityname`.

Dans la boucle à l'intérieur de la boucle (vous voyez toujours où je suis maintenant ?) nous imprimons la date sur la feuille, où, comme plus tôt dans ce tutoriel, nous avons utilisé la fonction `DateSerial`.

Assurez-vous de supprimer les feuilles avec un nom de ville de votre classeur, exécutez la macro à nouveau, et vous devriez voir les feuilles de calcul incluant les dates pour le mois.

Notez que les dates seront imprimées à partir de la deuxième ligne, car j'ai inclus +1 pour ma colonne de cellule dans mon code précédent. Pourquoi, pourriez-vous vous demander ? Eh bien, parce que je veux ajouter certains titres sur la première ligne à la place, que nous allons ajouter à la même boucle tout de suite.

Plutôt que de définir les cellules en utilisant la propriété Cells suivie du numéro de ligne et de colonne en tant qu'entier, nous pouvons utiliser `Range` suivi de l'emplacement d'une cellule (ou de plusieurs cellules) pour cibler sa valeur et d'autres propriétés.

```vba
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        
        For DateIndex = 1 To NumberOfDays
            Worksheets(CityName).Cells(DateIndex + 1, 1) = DateSerial(Year(ReportDate), Month(ReportDate), DateIndex)
        Next DateIndex
        
        Worksheets(CityName).Range("B1") = "Minimum"
        Worksheets(CityName).Range("C1") = "Moyenne"
        Worksheets(CityName).Range("D1") = "Maximum"
    Next SheetIndex
```

Dans l'exemple ci-dessus, j'ai ajouté les en-têtes pour notre tableau, qui seront maintenant imprimés sur chaque feuille de calcul grâce à notre boucle. 

## Comment utiliser des tableaux en VBA

Vous avez déjà entendu parler de DRY ? Ne vous répétez pas ! Malheureusement, c'est exactement ce que nous faisons ici. 

Une alternative pourrait être de stocker les trois en-têtes dans un tableau et de les parcourir pour obtenir le même résultat. Est-ce vraiment nécessaire pour trois éléments ? C'est discutable, pour être honnête. Mais ci-dessous, vous trouverez mon exemple de code tel que décrit :

```
Sub CreateTemplate()
    'Variable qui contiendra le nom de la ville utilisé pour nommer une feuille.
    Dim CityName As String
    'Variable qui sera utilisée pour suivre l'index de la boucle pour ajouter les dates individuelles pour le mois.
    Dim DateIndex As Integer
    'Variable qui sera utilisée pour suivre l'index de la boucle pour insérer les en-têtes.
    Dim HeaderIndex As Integer
    'Variant qui stockera les en-têtes utilisés dans chaque feuille de calcul.
    Dim Headers(2) As Variant
    'Variable qui contiendra le nombre de villes.
    Dim NumberOfCities As Integer
    'Variable qui contiendra le nombre de jours dans le mois choisi
    Dim NumberOfDays As Integer
    'Variable qui contiendra la date entrée dans la feuille de calcul Date.
    Dim ReportDate As Date
    'Variable qui sera utilisée pour suivre l'index de la boucle pour créer des feuilles de calcul.
    Dim SheetIndex As Integer
    
    Headers(0) = "Minimum"
    Headers(1) = "Moyenne"
    Headers(2) = "Maximum"
    
    NumberOfCities = Worksheets("Cities").UsedRange.Rows.Count
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        'Ajout d'une nouvelle feuille de calcul appelée NewSheet au classeur en dernier pour assurer l'ordre alphabétique.
        Sheets.Add(After:=Sheets(Sheets.Count)).Name = CityName
    Next SheetIndex
    
    ReportDate = Worksheets("Date").Cells(1, 2)
    NumberOfDays = DaysInMonth(ReportDate)
    
    For SheetIndex = 1 To NumberOfCities
        'Définition de la variable cityname basée sur l'index.
        CityName = Worksheets("Cities").Cells(SheetIndex, 1)
        
        For DateIndex = 1 To NumberOfDays
            Worksheets(CityName).Cells(DateIndex + 1, 1) = DateSerial(Year(ReportDate), Month(ReportDate), DateIndex)
        Next DateIndex
        
        For HeaderIndex = 0 To UBound(Headers) - LBound(Headers)
            Worksheets(CityName).Cells(1, HeaderIndex + 2) = Headers(HeaderIndex)
        Next HeaderIndex
        
    Next SheetIndex
    
End Sub
```

Le variant est utilisé comme un tableau, qui est déclaré là où vous vous y attendez et les titres sont insérés plus tard par index directement après la déclaration de la variable. 

Au lieu de fournir les emplacements de cellules individuels, j'ai utilisé une boucle qui s'exécute de zéro au nombre d'éléments (moins un, car les tableaux en VBA commencent également à zéro). Le titre est ensuite imprimé sur la feuille, comme dans la situation précédente. 

Vous devrez peut-être ajouter un autre en-tête plus tard, auquel cas la dernière solution est plus facile. Mais si vous êtes sûr à cent pour cent de rester avec trois seulement, choisissez ce qui est le plus pratique pour vous. Il est préférable de connaître les deux méthodes après tout. 

_Cela n'a pas d'importance laquelle des deux options vous choisissez pour le reste de ce tutoriel, tant que vous avez imprimé les en-têtes._

## Comment importer des données en utilisant VBA

À ce stade, nous avons créé le modèle réel, donc nous pouvons entrer des villes et une date dans le classeur. Ensuite, la macro fera le reste pour nous. 

J'aimerais aller plus loin dans ce tutoriel et vous montrer comment déclencher une fenêtre d'explorateur où vous pouvez choisir un fichier et importer les données de ce fichier.

Assurez-vous d'avoir terminé les étapes ci-dessus et d'avoir obtenu les feuilles de calcul pour toutes les villes. Commençons une nouvelle sous-routine et définissons les variables suivantes en haut :

```
Sub ImportData()
    Dim FileLocation As String
    Dim WorksheetTitle As String
    
    WorksheetTitle = ActiveSheet.Name
End Sub
```

Nous avons besoin de la première variable pour stocker l'emplacement du fichier où nous allons importer les données sur votre appareil. Nous utilisons la seconde pour stocker le titre de la feuille actuellement sélectionnée par l'utilisateur.

Ajoutez le code suivant à la macro, juste en dessous de la ligne où nous définissons `WorksheetTitle` égal au nom de la feuille (mais toujours avant End Sub) :

```
FileLocation = Application.GetOpenFilename
If FileLocation = "False" Then
    Beep
    Exit Sub
End If

Application.ScreenUpdating = False
Set ImportWorkbook = Workbooks.Open(Filename:=FileLocation)

Debug.Print ImportWorkbook.Worksheets(1).Range("B1")

ImportWorkbook.Close
Application.ScreenUpdating = True
```

Cela peut sembler un peu cryptique au premier abord, mais ne devrait pas être trop difficile à comprendre. La fonction `Application.GetOpenFilename` est ce qui déclenche une fenêtre d'explorateur de fichiers et retourne un emplacement, qui est ensuite stocké dans la variable définie précédemment.

Si vous décidez de ne pas sélectionner de fichier, ce qui signifie que si `FileLocation` = "False", vous entendrez le son iconique du bip (oui, Excel vient aussi avec des sons géniaux !😍) et la macro se terminera ici.

Si c'est vrai, nous continuerons avec la macro, qui met d'abord fin aux mises à jour de l'écran d'Excel. Cela aide à s'assurer que tout se déroulera sans accroc. 

Pour cette macro, vous ne remarquerez peut-être pas la différence sans cette ligne, mais avec des calculs plus complexes, vous le ferez. Croyez-moi.

## Comment travailler avec des objets en VBA

Après cela, les données incluses dans le fichier situé où la variable FileLocation est stockée dans la constante `ImportWorkbook`. 

Notez que nous utilisons le mot-clé `Set` qui est principalement utilisé pour les objets, comme une importation d'un classeur. 

Pour tester si nous sommes capables d'extraire la date du fichier, nous utilisons à nouveau `Debug.Print` pour imprimer la ville, qui est située dans la cellule B1 des fichiers disponibles via le lien mentionné au début de ce tutoriel.

Si vous importez le fichier `Data_Amsterdam`, vous devriez voir Amsterdam imprimé dans votre Fenêtre Immédiate. Après la fermeture du fichier, Excel se comportera normalement à nouveau. Nous pouvons facilement coller le nom de la ville (juste imprimé) dans notre propre modèle en remplaçant le `Debug.Print` par ce qui suit :

```vba
ThisWorkbook.Worksheets(WorksheetTitle).Range("A1") = ImportWorkbook.Worksheets(1).Range("B1")

'Équivalent à ce qui suit.
ThisWorkbook.Worksheets(WorksheetTitle).Cells(1, 1) = ImportWorkbook.Worksheets(1).Range(1, 2)
```

Notez que nous pouvons maintenant utiliser notre variable `ImportWorkbook` pour obtenir les données du classeur importé. Mais nous pouvons également utiliser `ThisWorkbook` (nom de mot-clé protégé par VBA) pour obtenir les propriétés de notre propre modèle à la place. 

Si nous exécutons maintenant cette macro et importons `Data_Amsterdam`, la ville devrait maintenant être imprimée dans le coin supérieur gauche de votre feuille de calcul Amsterdam.

## Comment utiliser des dictionnaires en VBA

Comme promis, il est maintenant temps d'obtenir les températures réelles. Vous pouvez utiliser une boucle et insérer les nombres comme démontré ci-dessus, mais je me sens fantaisiste aujourd'hui et j'aimerais vous montrer comment nous pouvons faire cela en utilisant un dictionnaire.

Encore une fois, comme le tableau plus tôt dans ce tutoriel, cette approche peut être un peu redondante pour cette situation. Mais si vous devez travailler avec de grandes quantités de données, cela sera utile.

La première chose que nous devons faire est de définir plusieurs nouvelles variables ici :

```
Dim DataIndex As Integer
Dim DaysIndex As Integer
Dim FileLocation As String
Dim Headers(2) As Variant
Dim WorksheetTitle As String
Set TemperaturesDict = CreateObject("Scripting.Dictionary")

Headers(0) = "Maximum"
Headers(1) = "Minimum"
Headers(2) = "Moyenne"
```

Les deux index en haut suivront l'index des boucles que nous utiliserons plus tard. J'ai copié la déclaration des en-têtes et des variables de notre macro précédente. 

_Oui, nous aurions pu les définir comme une variable globale, mais c'est un autre sujet pour un autre jour._ 

Notez que j'ai changé l'ordre, car c'est ainsi qu'ils sont affichés dans le fichier importé.

Un dictionnaire est également un objet, que nous déclarerons donc en utilisant le mot-clé `Set` directement en dessous de nos variables.

Mais avant de pouvoir utiliser un dictionnaire de cette manière, assurez-vous que vous avez coché Microsoft Scripting Runtime (comme vous pouvez le voir dans la Figure 6 ci-dessus), que vous pouvez trouver sous Outils puis Références dans votre éditeur.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-91.png)
_Figure 06 : Références Visual Basic_

Auparavant, je vous ai montré comment copier une valeur d'une seule cellule d'un classeur à un second. Maintenant, plutôt que de copier des valeurs individuelles, je veux les stocker toutes ensemble dans un dictionnaire avant de continuer et de les coller.

```vba
    For DaysIndex = 11 To ImportWorkbook.Worksheets(1).UsedRange.Rows.Count
        Set DataDict = CreateObject("Scripting.Dictionary")
        For DataIndex = 0 To 2
            DataDict.Add Headers(DataIndex), ImportWorkbook.Worksheets(1).Cells(DaysIndex, DataIndex + 2)
        Next DataIndex
        TemperaturesDict.Add DaysIndex, DataDict
    Next DaysIndex
```

Cela pourrait être la partie la plus difficile du tutoriel, que je vais essayer d'expliquer aussi clairement que possible. 

Nous commençons par une boucle comme nous l'avons utilisée de nombreuses fois auparavant dans ce tutoriel – jusqu'à présent, tout va bien. La boucle commence à onze et se termine lorsque le nombre de lignes utilisées dans le classeur importé est atteint.

Ensuite, je définis un nouveau dictionnaire. Pourquoi ? Dans la plupart des autres langages, il est possible d'ajouter de nouvelles paires clé-valeur en utilisant la notation par points – mais pas en VBA. Afin de soi-disant imbriquer (ajouter un dictionnaire dans un dictionnaire), vous devrez créer un nouveau dictionnaire (interne) puis l'ajouter à votre autre dictionnaire (externe).

Ce dictionnaire dans la boucle sera donc d'abord peuplé avec les différentes températures disponibles, à savoir minimum, moyenne et maximum. 

Pour ce faire, j'utiliserai le tableau d'en-têtes comme discuté ci-dessus et je parcourrai ces valeurs. Vous ajoutez une paire clé-valeur en utilisant le nom du dictionnaire suivi de l'appel de la méthode `.Add`, la clé que vous souhaitez utiliser, une virgule, puis sa valeur :

```vba
DictName.Add Key, Value
```

C'est ce qui sera entré après la première itération lorsque vous importez le fichier `Data_Amsterdam` :

```
Maximum: 22.105547
Minimum: 14.385546	
Moyenne: 18.25388	

```

Ce dictionnaire est ensuite ajouté au dictionnaire 'principal' appelé `TemperaturesDict` – ce qui signifie que nous aurons maintenant quelque chose comme ceci :

```
10: 
    Maximum: 22.105547
    Minimum: 14.385546	
    Moyenne: 18.25388	

```

Nous faisons de même pour tous les autres jours et types de températures, jusqu'à ce que le fichier soit complètement extrait et que nous soyons prêts à insérer ces informations dans notre modèle. Mais alors quoi ?

```vba
    Headers(0) = "Minimum"
    Headers(1) = "Moyenne"
    Headers(2) = "Maximum"
    
    For DaysIndex = 2 To ThisWorkbook.Worksheets(WorksheetTitle).UsedRange.Rows.Count
        If TemperaturesDict.Exists(DaysIndex - 1) Then
            For DataIndex = 0 To 2
                ThisWorkbook.Worksheets(WorksheetTitle).Cells(DaysIndex, DataIndex + 2) = TemperaturesDict(DaysIndex - 1)(Headers(DataIndex))
            Next DataIndex
        End If
    Next DaysIndex
```

Comme discuté ci-dessus, le fichier importé a un autre ordre. Mais puisque nous utilisons un dictionnaire, nous pouvons maintenant facilement réorganiser le tableau des en-têtes et l'afficher comme nous l'avions initialement prévu dans notre modèle, car il recherchera la clé (#winning).

Nous utilisons ensuite une boucle à l'ancienne pour parcourir tous les jours que nous avons dans notre modèle. La boucle commence à deux, car nous avons défini nos en-têtes sur la première ligne. Commencer à l'index un les écrasera, ce que nous ne voulons pas. La boucle se termine après que nous avons eu toutes les lignes (c'est-à-dire, tous les jours).

Puisque seul un nombre limité de jours sont inclus dans le fichier importé, nous devons vérifier si le jour égal à l'index existe réellement dans notre dictionnaire. 

Nous faisons cela avec une instruction if, que vous pourriez reconnaître d'autres langages de programmation. Il y a un moins un puisque notre boucle commence à deux, bien que les jours du mois commencent toujours à un. Il en va de même pour le moins un utilisé plus tard dans ce bloc de code.

Si les données existent réellement dans notre tableau, nous les insérerons dans notre modèle. Ensuite, la ligne est définie par l'index de la boucle et la colonne provient de `DataIndex`. 

Finalement, nous obtenons le code suivant pour notre deuxième macro :

```
Sub ImportData()
    Dim DataIndex As Integer
    Dim DaysIndex As Integer
    Dim FileLocation As String
    'Variant qui stockera les en-têtes utilisés dans chaque feuille de calcul.
    Dim Headers(2) As Variant
    Dim WorksheetTitle As String
    Set TemperaturesDict = CreateObject("Scripting.Dictionary")
    
    Headers(0) = "Maximum"
    Headers(1) = "Minimum"
    Headers(2) = "Moyenne"
    
    WorksheetTitle = ActiveSheet.Name
    
    FileLocation = Application.GetOpenFilename
    If FileLocation = "False" Then
        Beep
        Exit Sub
    End If
    
    Application.ScreenUpdating = False
    Set ImportWorkbook = Workbooks.Open(Filename:=FileLocation)
    
    For DaysIndex = 11 To ImportWorkbook.Worksheets(1).UsedRange.Rows.Count
        Set DataDict = CreateObject("Scripting.Dictionary")
        For DataIndex = 0 To 2
            DataDict.Add Headers(DataIndex), ImportWorkbook.Worksheets(1).Cells(DaysIndex, DataIndex + 2)
        Next DataIndex
        TemperaturesDict.Add DaysIndex, DataDict
    Next DaysIndex
    
    Headers(0) = "Minimum"
    Headers(1) = "Moyenne"
    Headers(2) = "Maximum"
    
    For DaysIndex = 2 To ThisWorkbook.Worksheets(WorksheetTitle).UsedRange.Rows.Count
        If TemperaturesDict.Exists(DaysIndex - 1) Then
            For DataIndex = 0 To 2
                ThisWorkbook.Worksheets(WorksheetTitle).Cells(DaysIndex, DataIndex + 2) = TemperaturesDict(DaysIndex - 1)(Headers(DataIndex))
            Next DataIndex
        End If
    Next DaysIndex
    
    ImportWorkbook.Close
    Application.ScreenUpdating = True

End Sub
```

Lorsque vous exécutez maintenant ce code, vous devriez voir les températures être importées du fichier de données vers le modèle. 

Notez que nous avons également changé l'ordre dans lequel elles viennent à l'origine – commençant maintenant par le minimum et se terminant par le maximum. 

## Conclusion

Félicitations ! Vous avez maintenant créé un modèle que vous pouvez facilement remplir avec des données, tout en utilisant des macros.

Merci d'avoir lu :) Si vous avez des questions sur ce tutoriel ou une autre implémentation VBA, n'hésitez pas à m'envoyer un message direct sur Twitter afin que je puisse vous aider.