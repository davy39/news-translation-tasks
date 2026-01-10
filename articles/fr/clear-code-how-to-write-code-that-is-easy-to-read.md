---
title: Code Clair - Comment Écrire du Code Facile à Lire
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2022-11-28T12:26:28.000Z'
originalURL: https://freecodecamp.org/news/clear-code-how-to-write-code-that-is-easy-to-read
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cafe-gc5d844b68_1280.jpg
tags: []
seo_title: Code Clair - Comment Écrire du Code Facile à Lire
seo_desc: 'This article is a follow up to a tweet I made on how I deal with my poor
  ability to remember code. It may seem funny to you, but I do actually tend to forget
  what I write shortly after writing it.

  https://twitter.com/wiseAss301/status/159118167805122...'
---

Cet article est une suite à un tweet que j'ai publié sur la manière dont je gère ma mauvaise capacité à me souvenir du code. Cela peut vous sembler drôle, mais j'ai effectivement tendance à oublier ce que j'écris peu de temps après l'avoir écrit.

%[https://twitter.com/wiseAss301/status/1591181678051229696?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1591181678051229696%7Ctwgr%5E0c73a629a6c4b95546c3202d41070cd1ff69b172%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttps3A%2F%2Ftwitter.com%2Fwiseass301%2Fstatus%2F1591181678051229696image%3Dhttps3A%2F%2Fi.embed.ly%2F1%2Fimage3Furl3Dhttps253A252F252Fabs.twimg.com252Ferrors252Flogo46x38.png26key3Da19fcc184b9711e1b4764040d3dc5c07]

Tout d'abord, nous allons discuter de pourquoi vous pourriez vouloir écrire du code plus lisible plutôt que du code court et concis. Ensuite, nous examinerons les stratégies suivantes sur la manière de le faire avec :

* Le nommage des variables, valeurs, références, classes, objets et fonctions

* Les fonctions d'assistance

* Les commentaires de code

* Les énumérations/dictionnaires/classes scellées/etc.

* L'organisation et le nommage des packages

Une connaissance de base de la lecture de code est recommandée pour tirer le meilleur parti de cet article. Cependant, j'ai essayé de le rendre accessible aux débutants lorsque cela était possible.

![Image](https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE1Mnx8cmVhZGluZ3xlbnwwfHx8fDE2Njg4MTYyMjQ&ixlib=rb-4.0.3&q=80&w=2000 align="left")

*Photo par [Unsplash](https://unsplash.com/@jamie452?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit"&gt;Jamie Street / &lt;a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)*

## L'Efficacité Vient-Elle de Moins de Frappes de Clavier ?

Je me souviens, en tant que développeur junior, que je pensais que les noms courts ou abrégés pour les identifiants - essentiellement toute structure de code que nous, développeurs, sommes autorisés à nommer - étaient plus efficaces.

Ma logique était simple : Si cela me prend moins de temps à l'écrire, alors je peux faire le travail plus rapidement.

Cette logique aurait du sens si les choses suivantes étaient vraies :

* Moi, ou quelqu'un d'autre, n'aurions jamais à lire ou à corriger ce que j'ai écrit dans le passé

* Je n'oubliais pas souvent ce qu'était une variable, ou plusieurs variables, en lisant une fonction

* Je n'avais pas occasionnellement à écrire du code qui était vraiment complexe et obscur

* Je pouvais renommer des fonctions, classes ou propriétés de bibliothèques externes ridicules ou obscures en quelque chose de plus sensé

Le point est que, pour moi, **je trouve peu de situations où être concis économise réellement du temps**. De plus, les IDE modernes ont cette fonctionnalité utile appelée complétion de code qui économise la plupart des frappes de toute façon.

Vous ne vous sentez peut-être pas de la même manière, et c'est parfaitement acceptable ! Prenez ce qui fonctionne pour vous dans cet article et jetez le reste.

## Comment Nommer les Classes, Variables et Fonctions

Je vais maintenant partager ce que je fais pour rendre mon code plus facile à lire pour moi-même et pour les autres. Les exemples de code que j'utilise seront en Kotlin, mais les points que je soulève devraient être applicables à la plupart des plateformes et des langages.

Il y a deux choses importantes à savoir lorsque l'on apprend à nommer les entités logicielles. Avant d'en arriver là, le terme entités logicielles fait référence à l'un des éléments suivants :

* Classes, structs, objets

* Variables, valeurs, références, pointeurs

* Fonctions, méthodes, algorithmes, commandes

* Interfaces, protocoles, abstractions

Essentiellement, tout ce qu'un programmeur doit nommer lors de l'écriture d'un programme.

### À Quel Point les Noms Doivent-Être Descriptifs

Mon objectif pour le nommage des entités logicielles est le suivant : Le nom doit **réduire toute confusion sur ce qu'une entité logicielle fait, ou est.**

Les détails sur la manière dont elle fait quelque chose ne sont généralement pas nécessaires.

Le contexte, ou tout ce qui entoure une entité logicielle, est important lors du choix d'un nom. Quelque chose peut nécessiter plus ou moins de détails en fonction de son contexte.

Considérons trois exemples :

1. `getFormattedDate(date: String) : String`

2. `getYYYYMMDDFormattedDate(date: String) : String`

3. `getYYYYMMDDFormattedDateFromIso8601Format(date: String) : String`

L'application de production sur laquelle je travaille actuellement nécessite fréquemment de transformer des dates vers et depuis différents formats.

Dans ce contexte, j'utilise absolument des noms comme l'exemple 3, qui est beaucoup plus clair que l'exemple 1.

Une autre option pourrait être de changer le nom du paramètre dans l'exemple 2 en quelque chose comme `iso8601Date`.

Bien que je vous suggère d'être cohérent dans votre approche dans une base de code donnée, n'hésitez pas à expérimenter ce qui fonctionne pour vous. L'idée est d'ajouter autant d'informations que nécessaire pour clarifier toute ambiguïté.

Si j'écrivais un programme ponctuel qui ne convertit qu'un seul format en un autre, alors l'exemple 1 est bien. **Ajouter plus d'informations que nécessaire n'est pas ce que je préconise ici.**

### Plus Quelque Chose Fait de Choses, Plus C'est Difficile à Nommer

Si vous avez du mal à nommer quelque chose, c'est le plus souvent (bien que pas toujours) parce qu'il fait trop de choses qui ne sont pas conceptuellement liées.

Le degré auquel les entités logicielles sont conceptuellement liées est connu sous le nom de [cohésion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)).

**En regardant quelles parties d'un programme sont cohésives ou non**, vous pouvez commencer à comprendre ce qui doit être séparé ou regroupé.

Ce processus peut être fait à partir de diverses perspectives, que je vais essayer d'expliquer par l'exemple.

Supposons que vous avez quatre entités logicielles :

1. `StoreUserInCloud`

2. `StoreUserOnDisk`

3. `StoreMessage`

4. `EditUserUI`

La première perspective que nous pouvons considérer est l'information du monde réel avec laquelle ces entités sont concernées. De ce point de vue, nous pouvons voir que `StoreUserInCloud`, `StoreUserOnDisk`, et `EditUserUI` utilisent le même modèle d'information : un utilisateur.

Cependant, il y a une autre perspective que nous devons garder à l'esprit, en particulier lors de la conception de programmes d'interface graphique (GUI).

Tout programme GUI peut être décomposé en trois couches principales :

* Interface utilisateur (communément appelée "View")

* Logique (faisant généralement référence à des choses comme les contrôleurs et les présentateurs)

* Modèle (stockage et accès aux données, ou l'état lui-même selon votre définition)

Cela ne signifie pas que vous devez toujours voir un programme comme ayant ces trois couches ! L'approche en trois couches est une généralisation qui est **fréquemment insuffisante**.

Dans tous les cas, de ce point de vue, `StoreMessage` a plus en commun avec les autres entités de stockage que `EditUserUI`.

Pouvoir regarder vos programmes sous plusieurs perspectives est quelque chose qui viendra avec la construction de programmes plus complexes.

Le point clé à retenir est que la séparation de votre base de code en parties cohésives et liées rendra généralement les entités logicielles plus faciles à nommer.

## Comment Utiliser les Fonctions d'Assistance

Les fonctions d'assistance, en particulier lorsqu'elles sont combinées avec de bonnes pratiques de nommage des fonctions, peuvent grandement améliorer la lisibilité de votre code.

Les fonctions d'assistance sont également une opportunité d'appliquer un principe fondamental de l'architecture logicielle : la séparation des préoccupations.

### Comment Créer des Puzzles Sudoku avec des Fonctions d'Assistance

Nous allons maintenant examiner un exemple pratique pour démontrer l'utilisation intensive des fonctions d'assistance. Essayez d'imaginer à quel point ce code serait plus difficile à suivre si tout était dans une seule fonction géante !

Dans le passé, j'ai travaillé sur une grande mais cohésive partie d'un programme : un générateur de [Sudoku](https://en.wikipedia.org/wiki/Sudoku) qui utilise des structures de données et des algorithmes de graphe. Même si vous n'êtes pas familier avec le Sudoku ou les graphes DSA, je crois que vous pourrez toujours suivre le point principal.

Vous pouvez trouver le code source complet [ici](https://github.com/BracketCove/GraphSudokuOpen/tree/master/app/src/main/java/com/bracketcove/graphsudoku/computationlogic).

Nous pouvons diviser le processus de génération d'un puzzle Sudoku jouable en cinq étapes :

* Créer les nœuds du puzzle (représentant les tuiles)

* Créer les arêtes du puzzle (les arêtes dans ce cas sont un autre mot pour les relations/références entre les tuiles : soit ligne, colonne ou sous-grille)

* Ensemencer (ajouter) certaines valeurs à la structure de données pour en faciliter la résolution

* Résoudre le puzzle

* Désoudre un certain nombre de tuiles afin que le jeu soit effectivement jouable par un utilisateur

J'ai utilisé quelque chose de similaire au modèle de construction pour représenter ces étapes dans la fonction que j'appelle pour créer le puzzle :

```kotlin
internal fun buildNewSudoku(
    boundary: Int,
    difficulty: Difficulty
): SudokuPuzzle = buildNodes(boundary, difficulty)
        .buildEdges()
        .seedColors()
        .solve()
        .unsolve()
```

Bien que l'idée de "nœuds" et "arêtes" soient des définitions techniques dans la [théorie des graphes](https://en.wikipedia.org/wiki/Graph_theory), ce code reflète clairement les cinq étapes que j'avais décidées.

Nous ne regarderons pas toute la base de code, mais je veux souligner comment les fonctions d'assistance continuent de décomposer la logique et favorisent la lisibilité :

```kotlin
internal fun SudokuPuzzle.buildEdges(): SudokuPuzzle {
    this.graph.forEach {
        val x = it.value.first.x
        val y = it.value.first.y

        it.value.mergeWithoutRepeats(
                getNodesByColumn(this.graph, x)
        )

        it.value.mergeWithoutRepeats(
                getNodesByRow(this.graph, y)
        )

        it.value.mergeWithoutRepeats(
                getNodesBySubgrid(this.graph, x, y, boundary)
        )

    }
    return this
}

internal fun LinkedList<SudokuNode>.mergeWithoutRepeats(new: List<SudokuNode>) {
    val hashes: MutableList<Int> = this.map { it.hashCode() }.toMutableList()
    new.forEach {
        if (!hashes.contains(it.hashCode())) {
            this.add(it)
            hashes.add(it.hashCode())
        }
    }
}

internal fun getNodesByColumn(graph: LinkedHashMap<Int,
        LinkedList<SudokuNode>>, x: Int): List<SudokuNode> {
    val edgeList = mutableListOf<SudokuNode>()
    graph.values.filter {
        it.first.x == x
    }.forEach {
        edgeList.add(it.first)
    }
    return edgeList
}
//...
```

Pour résumer ce processus, les fonctions d'assistance offrent deux avantages :

* Elles servent de substitut à un bloc de code qui fait quelque chose

* Ce bloc de code peut être donné un nom descriptif

Ces deux avantages peuvent conduire à une plus grande lisibilité, car le code devient moins encombré et plus descriptif.

Si vous vous demandez ce qui devrait et ne devrait pas être une fonction d'assistance, je vous suggère de pratiquer différentes approches pour voir ce qui fonctionne pour vous.

## Comment Utiliser les Commentaires de Code

Ma préférence personnelle pour les commentaires de code est qu'ils ont deux usages principaux : Premièrement, les commentaires aident à décrire les fonctions complexes en détail.

Deuxièmement, pour clarifier toute confusion concernant une ligne ou un bloc de code.

### Comment Utiliser les Commentaires pour Concevoir de Nouvelles Fonctions

Lorsque je rencontre des fonctions que je m'attends à être difficiles à écrire, je décris ce que la fonction fait en utilisant soit un langage simple soit du pseudocode.

La manière dont je fais cela a changé au fil des années, alors je vous encourage à essayer différentes approches.

Dans les exemples de la section précédente, j'avais omis les commentaires de code :

```kotlin
/**
 * 1. Générer une Map qui contient n*n nœuds.
 * 2. pour chaque nœud adjacent (selon les règles du Sudoku), ajouter une Arête à l'ensemble de hachage
 *  - Par colonne
 *  - Par ligne
 *  - Par sous-grille de taille n
 *
 *  LinkedHashMap : J'ai choisi d'utiliser une LinkedHashMap car elle préserve l'ordre des
 *  éléments placés dans la Map, mais permet également les recherches par code de hachage, qui sont
 *  générés par les valeurs x et y.
 *
 *  En ce qui concerne la LinkedList dans chaque bucket (élément) de la map, supposez que le premier élément
 *  est le nœud à hashCode(x, y), et les éléments suivants sont les arêtes de cet élément.
 *  À part l'ordre du premier élément en tant que Head de la LinkedList, le reste des
 *  éléments n'a pas besoin d'être ordonné de manière particulière.
 *
 *
 *  */
internal fun buildNodes(n: Int, difficulty: Difficulty): SudokuPuzzle {
    val newMap = LinkedHashMap<Int, LinkedList<SudokuNode>>()

    (1..n).forEach { xIndex ->
        (1..n).forEach { yIndex ->
            val newNode = SudokuNode(
                    xIndex,
                    yIndex,
                    0
            )

            val newList = LinkedList<SudokuNode>()
            newList.add(newNode)
            newMap.put(
                    newNode.hashCode(),
                    newList
            )
        }
    }
    return SudokuPuzzle(n, difficulty, newMap)
}
```

La quantité de détails que j'ajoute à ces commentaires dépend du contexte. Si je travaille en équipe, j'essaie généralement de garder cela beaucoup plus court que ce que vous voyez ci-dessus, et j'inclus uniquement les informations que je juge nécessaires.

L'exemple ci-dessus était un projet d'apprentissage personnel que je prévoyais de partager avec d'autres. C'est pourquoi j'ai même inclus mon processus de prise de décision sur les types utilisés pour représenter un puzzle Sudoku.

Pour les fans de développement piloté par les tests, vous pourriez essayer d'écrire les étapes de pseudocode d'un algorithme avant d'écrire le test :

```kotlin
/**
     * Lors du processus de liaison, appelé par la vue dans onCreate. Vérifier l'état actuel de l'utilisateur, écrire ce résultat dans
     * vModel, afficher le graphique de chargement, effectuer une initialisation
     *
     * a. L'utilisateur est anonyme
     * b. L'utilisateur est enregistré
     *
     * a:
     * 1. Afficher la vue de chargement
     * 2. Vérifier la présence d'un utilisateur connecté à partir de l'authentification : null
     * 3. écrire null dans l'état de l'utilisateur vModel
     * 4. appeler le processus de démarrage
     */
    @Test
    fun `Lors de la liaison, l'utilisateur est anonyme`() = runBlocking {

        //...
    }
```

Cela vous permet de concevoir l'unité à un **niveau d'abstraction plus élevé** avant d'écrire l'implémentation. Le temps que vous passez à concevoir à des niveaux d'abstraction plus élevés peut vous faire économiser du temps à long terme.

### Comment Utiliser Efficacement les Commentaires de Code Inline

Il y a deux situations principales où j'écrirai un commentaire de code inline :

* Lorsque je sens que le but d'une ligne ou d'un bloc de code ne sera pas clair pour moi-même ou pour toute autre personne le lisant plus tard

* Lorsque je dois appeler une fonction de bibliothèque mal nommée qui a un nom confus ou trompeur

De loin, l'algorithme Sudoku le plus complexe dans mon programme est l'[algorithme de résolution](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/computationlogic/SolveSudoku.kt). En fait, il est si long que je ne vais poster qu'un extrait ici :

```kotlin
internal fun SudokuPuzzle.solve()
        : SudokuPuzzle {
    // nœuds qui ont été assignés (non inclus les nœuds ensemencés à partir de seedColors()
    val assignments = LinkedList<SudokuNode>()

    // suivre les tentatives d'assignation échouées pour surveiller les boucles infinies
    var assignmentAttempts = 0
    // Deux étapes de retour en arrière, partiel est la moitié du jeu de données, complet est un redémarrage complet
    var partialBacktrack = false

    var fullbacktrackCounter = 0

    // de 0 à boundary, représente à quel point l'algorithme est "exigeant" pour l'assignation de nouvelles valeurs
    var niceValue: Int = (boundary / 2)

    // pour éviter d'être trop exigeant trop tôt
    var niceCounter = 0

    // travailler avec une copie
    var newGraph = LinkedHashMap(this.graph)
    // tous les nœuds qui sont de valeur 0 (non colorés)
    val uncoloredNodes = LinkedList<SudokuNode>()
    newGraph.values.filter { it.first.color == 0 }.forEach { uncoloredNodes.add(it.first) }

    while (uncoloredNodes.size > 0) {
    //...
    }
//...
}
```

Dans ce cas, les commentaires inline étaient nécessaires car j'oubliais fréquemment ce que certaines de ces variables étaient en lisant cet algorithme géant.

Un autre cas où j'ajouterai un commentaire inline est lorsque je dois expliquer ou me rappeler du code sur lequel je n'ai pas de contrôle.

Par exemple, l'infâme [API Java Calendar](https://docs.oracle.com/javase/7/docs/api/java/util/Calendar.html#MONTH) utilise un indexage basé sur zéro pour les mois. Cela est arguablement vraiment stupide, car je ne connais aucun standard qui représente janvier avec 0, et je ne me souviens pas s'il en existe un !

Je ne peux pas partager le code avec vous car il est propriétaire, mais il suffit de dire que j'ai des commentaires dans la base de code de mon équipe actuelle qui expliquent les déclarations aléatoires `- 1` pour se conformer à l'API Calendar.

## Comment Utiliser les Énumérations et les Dictionnaires

Il existe d'autres noms pour ces types de structures de code, mais ce sont les deux avec lesquels je suis familier. Supposons que vous avez un ensemble restreint, ou limité, de valeurs que vous utilisez pour représenter quelque chose.

Par exemple, j'avais besoin d'un moyen de limiter le nombre de tuiles incluses dans un nouveau puzzle Sudoku, basé sur :

* La taille du puzzle (4, 9 ou 16 tuiles par colonne/ligne/sous-grille)

* La difficulté du puzzle (facile, moyen ou difficile)

À travers des tests approfondis, je suis arrivé aux valeurs suivantes comme modificateurs :

```kotlin
enum class Difficulty(val modifier:Double) {
    EASY(0.50),
    MEDIUM(0.44),
    HARD(0.38)
}

data class SudokuPuzzle(
        val boundary: Int,
        val difficulty: Difficulty,
        val graph: LinkedHashMap<Int, LinkedList<SudokuNode>>
        = buildNewSudoku(boundary, difficulty).graph,
        var elapsedTime: Long = 0L
)//...
```

Ces valeurs sont utilisées à divers endroits où la logique doit changer en fonction de la difficulté.

Parfois, vous n'avez même pas besoin d'avoir des valeurs associées à des noms lisibles par l'homme. J'ai utilisé une énumération différente pour représenter différentes stratégies de résolution afin de garantir qu'un puzzle est jouable par rapport à la difficulté sélectionnée :

```kotlin
enum class SolvingStrategy {
    BASIC,
    ADVANCED,
    UNSOLVABLE
}

internal fun determineDifficulty(
    puzzle: SudokuPuzzle
): SolvingStrategy {
    val basicSolve = isBasic(
        puzzle
    )
    val advancedSolve = isAdvanced(
        puzzle
    )

    // si le puzzle n'est plus soluble, nous retournons la stratégie actuelle
    if (basicSolve) return SolvingStrategy.BASIC
    else if (advancedSolve) return SolvingStrategy.ADVANCED
    else {
        puzzle.print()
        return SolvingStrategy.UNSOLVABLE
    }
}
```

Un bon principe dans la conception de tout système est le suivant : **Moins de pièces mobiles ont généralement moins de choses qui peuvent mal tourner.**

Placer des restrictions sur les valeurs et les types, et leur donner de bons noms, non seulement rend votre code plus facile à lire, **mais peut également le protéger contre les erreurs.**

## Comment Organiser et Nommer les Packages, Dossiers et Répertoires

Aucun guide sur la lisibilité du code ne serait complet sans une discussion sur les packages. Si la plateforme et le langage de votre préférence n'utilisent pas ce terme, supposez que je veux dire dossier ou répertoire à la place.

C'est quelque chose sur lequel j'ai changé d'avis à plusieurs reprises, et cela se reflète dans mes anciens projets.

Deux approches courantes pour l'organisation des packages sont :

* Package par couche architecturale

* Package par fonctionnalité

### Comment Faire un Package par Couche

Le package par couche est le premier et le pire système que j'ai jamais utilisé. L'idée est généralement de construire votre structure de packages autour d'un modèle architectural comme MVC, MVP, MVVM, et ainsi de suite.

Pour prendre MVC comme exemple, votre structure de packages de premier niveau ressemblerait à ceci :

* modèle

* vue

* contrôleur

Le premier problème avec cette approche est qu'elle suppose que chaque classe ou fonction s'intègre confortablement dans l'une de ces couches. Ce n'est rarement le cas en pratique.

Je trouve également cette approche comme étant la moins lisible, car le niveau supérieur ne vous donne que les détails les plus généraux sur ce à quoi vous attendre à l'intérieur de chaque package.

Cette approche peut généralement être améliorée en ajoutant plus de "couches" pour être plus spécifique :

* ui

* modèle

* api

* buildlogic/di

* repository

* domaine

* commun

Cela peut fonctionner raisonnablement bien dans les bases de code plus petites où tous les développeurs sont familiers avec le modèle général et le style utilisé.

### Comment Faire un Package par Fonctionnalité

Le package par fonctionnalité a ses propres défauts, mais est généralement plus facile à lire et à naviguer. Cela suppose que vous donniez aux packages de bons noms.

Le terme fonctionnalité est difficile à décrire, mais je le définirais généralement comme ceci : Un écran/page, ou un ensemble d'écrans/pages qui définissent une **pièce principale de fonctionnalité** pour les utilisateurs ou les clients.

Pour une application de médias sociaux, nous pourrions voir une structure telle que :

* timeline

* friends

* userprofile

* messages

* messagedetail

Le problème central avec le package par fonctionnalité est l'inverse du package par couche : Il y aura presque toujours des entités logicielles qui sont utilisées dans plusieurs fonctionnalités.

Il existe deux solutions à ce problème. La première serait d'avoir du code dupliqué dans chaque fonctionnalité.

Cela peut sembler étrange, mais dupliquer des entités logicielles **peut être incroyablement utile dans les environnements d'entreprise** dans des situations spécifiques.

Cependant, ce n'est pas quelque chose que je recommanderais comme règle générale.

### Comment Faire une Structure de Package Hybride

La solution que je recommande généralement aux développeurs est ce que j'aime appeler l'approche hybride. Elle est très simple, flexible et devrait couvrir la plupart de vos exigences :

* timeline

* friends

* messages

* allmessages

* conversation

* messagedetail

* api

* timeline

* user

* message

* uicomponents

Veuillez ne pas prendre cet exemple trop au sérieux ; j'essaie de transmettre l'idée générale : Tout ce qui est spécifique à une fonctionnalité va dans ce package de fonctionnalité. Tout ce qui est partagé entre les fonctionnalités va dans un package séparé imbriqué au même niveau ou à un niveau supérieur.

Encore une fois, ce qui définit une couche était un concept vague dès le départ, alors ne suivez pas simplement une convention aveuglément. **Pensez de manière critique à ce qui est clair, en particulier pour quelqu'un qui n'est pas familier avec le projet.**

## Réflexions Finales

La plupart de mes préférences en matière de lisibilité et de style de code sont venues d'une grande quantité d'essais de différentes approches. Parfois, il s'agissait d'approches que j'ai vues d'autres utiliser et certaines sont venues naturellement.

Si vous êtes capable de vous mettre à la place de quelqu'un de moins familier avec le code ou le programme que vous regardez, vous aurez plus de facilité à faire en sorte que votre code se lise comme un livre.

### Avant de partir...

Si vous avez aimé cet article et souhaitez plus d'informations sur ces principes et structures de code, consultez mon cours gratuit et complet sur les [fondamentaux de la programmation](https://youtu.be/FL2SMZxNQlc). Il inclut des sous-titres professionnels en anglais, birman et arabe.