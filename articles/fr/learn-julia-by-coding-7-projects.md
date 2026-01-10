---
title: Apprendre Julia en codant 7 projets – Tutoriel de programmation pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-28T23:54:26.000Z'
originalURL: https://freecodecamp.org/news/learn-julia-by-coding-7-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/7-projects-1.png
tags:
- name: Julia
  slug: julia
- name: Julialang
  slug: julialang
- name: projects
  slug: projects
seo_title: Apprendre Julia en codant 7 projets – Tutoriel de programmation pratique
seo_desc: "By Logan Kilpatrick\nThe Julia programming language is used for a lot of\
  \ really impactful and interesting challenges like Machine Learning and Data Science.\
  \ \nBut before you can get to the complex stuff, it is worth exploring the basics\
  \ to develop a so..."
---

Par Logan Kilpatrick

Le langage de programmation Julia est utilisé pour de nombreux défis très impactants et intéressants comme le Machine Learning et la Data Science. 

Mais avant de pouvoir aborder les choses complexes, il vaut la peine d'explorer les bases pour développer une solide fondation. 

Dans ce tutoriel, nous allons passer en revue certaines bases de Julia en construisant 7 petits projets Julia :

* Mad Libs ✍️
* Jeu de devinette de nombre 🔊
* Devinette de nombre par l'ordinateur 🤖
* Pierre 🪨, Papier 📄, Ciseaux ✂️
* Générateur de mots de passe 🎬
* Simulateur de lancer de dés 🎲
* Minuterie de compte à rebours ⏳

Si vous n'avez pas encore téléchargé Julia, rendez-vous sur : [https://julialang.org/downloads/](https://julialang.org/downloads/) ou regardez cette vidéo :

%[https://www.youtube.com/watch?v=t67TGcf4SmM]

Il est également utile de noter que si vous êtes totalement nouveau dans Julia et que vous souhaitez une introduction complète au langage, vous pouvez [consulter cet article de freeCodeCamp](https://www.freecodecamp.org/news/learn-julia-programming-language/).

## Projets Julia pour débutants

### Comment créer Mad Libs en Julia ✍️

Dans Mad Libs, l'utilisateur est invité à entrer différents types de mots. Les mots aléatoires que l'utilisateur entre sont ensuite insérés dans une phrase. Cela conduit à des résultats assez farfelus et drôles. Essayons de programmer une version simple de cela en utilisant Julia.

Au cœur de ce problème, nous voulons concaténer (ou ajouter ensemble) plusieurs chaînes de caractères afin de passer d'une phrase avec des espaces réservés à une phrase avec l'entrée de l'utilisateur. 

La manière la plus simple d'y parvenir en Julia est avec l'interpolation de chaînes :

```julia
julia> name = "Logan"
"Logan"

julia> new_string = "Hello, my name is $name"
"Hello, my name is Logan"
```

Ici, nous pouvons voir que nous pouvons insérer la variable name que nous avons définie dans la chaîne en utilisant la syntaxe `$name`.

Il existe de nombreuses autres façons de faire cela, comme utiliser la fonction `string` :

```julia
julia> new_string = string("Hello, my name is ", name)
"Hello, my name is Logan"

```

mais l'interpolation de chaînes semble être la plus directe et lisible dans ce cas.

Maintenant que nous savons comment nous allons configurer les chaînes, nous devons demander à l'utilisateur son entrée. 

Pour cela, nous pouvons utiliser la fonction `readline` comme suit :

```julia
julia> my_name = readline()
Logan
"Logan"
```

La fonction `readline` prend une seule ligne d'entrée de l'utilisateur. C'est exactement ce que nous voulons utiliser. Mettons tout cela ensemble dans un exemple simple :

```julia
function play_mad_libs()

    print("Entrez un verbe (action) : ")
    verb1 = readline()

    print("Entrez un adjectif (mot descriptif) : ")
    adj1 = readline()

    print("Entrez un nom (personne, lieu ou chose) : ")
    noun1 = readline()

    print("Entrez un autre nom (personne, lieu ou chose) : ")
    noun2 = readline()

    print("Entrez une phrase d'accroche (quelque chose comme 'hands up!') : ")
    phrase1 = readline()
    
    base_sentence = "John $verb1 dans la rue une nuit, jouant avec son $adj1 $noun1. Quand tout à coup, un $noun2 a surgi devant lui et a dit $phrase1"
    
    print("\n\n", base_sentence)
end

# Lien vers le code source : https://github.com/logankilpatrick/Julia-Projects-for-Beginners/blob/main/madlibs.jl
```

Dans cet exemple, nous avons appris à travailler avec des chaînes de caractères, à définir une fonction, à utiliser des instructions print, et plus encore ! 

Comme mentionné précédemment, il existe de nombreuses autres façons de faire les mêmes choses que nous avons faites ci-dessus. Donc, si vous voulez en savoir plus sur le travail avec les chaînes de caractères, [consultez la documentation Julia ici](https://docs.julialang.org/en/v1/manual/strings/).

### Comment créer un jeu de devinette de nombre en Julia 🔊

Dans ce jeu, nous devons générer un nombre aléatoire puis essayer de deviner ce que c'est. 

Pour commencer, nous devons générer un nombre aléatoire. Comme toujours, il existe de nombreuses façons de faire quelque chose comme cela, mais l'approche la plus directe est de faire ce qui suit :

```julia
julia> rand(1:10)
4
```

La fonction `rand` prend en entrée la plage de nombres que vous souhaitez utiliser comme limites pour le nombre que vous allez générer. Dans ce cas, nous définissons la plage comme `1-10`, inclusivement.

L'autre nouveau sujet que nous devons aborder pour que cet exemple fonctionne est les boucles while. La structure de base d'une boucle while est :

```julia
while some_condition is true
   do something
end
```

Cette boucle continuera à itérer jusqu'à ce que la condition de la boucle while ne soit plus remplie. Vous verrez bientôt comment nous utilisons cela pour continuer à demander à l'utilisateur d'entrer un nombre jusqu'à ce qu'il le devine correctement.

Enfin, pour nous faciliter un peu la tâche, nous allons ajouter une instruction if qui nous indique si nous devinons un nombre proche du nombre cible. La structure d'une instruction if en Julia est :

```julia
if some_condition is true
   do something
end
```

La grande différence est que l'instruction if est vérifiée une fois et ensuite c'est terminé. La condition initiale n'est pas revérifiée sauf si l'instruction if est dans une boucle.

Maintenant que nous avons les idées de base, voyons le code réel pour construire le devin de nombre. Assurez-vous d'essayer cela par vous-même avant de vérifier la solution ci-dessous. Bon codage ! 🎉

```julia
# Jeu de devinette de nombre en Julia
# Source : https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners

function play_number_guess_human()

    total_numbers = 25 # 

    # Générer un nombre aléatoire dans une certaine plage
    target_number = rand(1:total_numbers)
    guess = 0

    # Tant que le nombre n'a pas été deviné, continuer à demander des devinettes
    while guess != target_number
        print("Veuillez deviner un nombre entre 1 et $total_numbers : ")
        guess = parse(Int64, readline())
        # Convertir la valeur d'entrée de chaîne en nombre

        # Si nous sommes à +/-2 du nombre cible, donner un indice
        if abs(target_number - guess) <= 2 && target_number != guess
            print("\nVous vous rapprochez !\n")
        end
    end

    print("Bon travail, vous l'avez trouvé !")
end
```

### Comment créer un devin de nombre par ordinateur en Julia 🤖

Maintenant que nous avons vu à quoi cela ressemble lorsque nous essayons de deviner ce que l'ordinateur a généré aléatoirement, voyons si l'ordinateur peut faire mieux. 

Dans ce jeu, nous allons sélectionner un nombre puis voir combien de temps il faut à l'ordinateur pour deviner ce nombre. Pour cela, nous allons introduire de nouveaux concepts comme le module Random et les boucles for.

Nous commencerons par réfléchir à la manière dont nous pouvons faire en sorte que l'ordinateur devine des nombres aléatoires sans répétition. 

Une solution simple est d'utiliser la fonction `rand`, mais le problème est qu'il n'y a pas de moyen intégré pour s'assurer que l'ordinateur ne devine pas le même nombre plus d'une fois – après tout, c'est aléatoire !

Nous pouvons résoudre ce problème en combinant la fonction `collect` et la fonction `shuffle`. Nous commençons par définir une graine aléatoire :

```julia
julia> rng = MersenneTwister(1234);
```

Les graines aléatoires font en sorte que les générateurs de nombres aléatoires produisent des résultats reproductibles. Ensuite, nous devons définir toutes les devinettes possibles :

```julia
julia> a = collect(1:50)
50-element Vector{Int64}:
1
2
3
⋮
```

Nous devons maintenant utiliser la fonction `shuffle` pour rendre les devinettes aléatoires :

```julia
julia> using Random
julia> shuffle(rng, a)
50-element Vector{Int64}:
41
23
13
49
⋮
```

Maintenant que nous avons configuré les devinettes aléatoires, il est temps de les parcourir une par une et de voir si le nombre est égal à la cible entrée par l'utilisateur. 

Encore une fois, essayez cela avant de vérifier la solution ci-dessous :

```julia
# Jeu de devinette de nombre par ordinateur en Julia
# Source : https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners

using Random

function play_number_guess_computer()

    print("Veuillez entrer un nombre entre 1 et 50 pour que l'ordinateur essaie de le deviner : ")
    
    # Prendre l'entrée de l'utilisateur et la convertir en nombre
    target_number = parse(Int64, readline())
    
    # Créer un tableau de 50 nombres
    guess_order = collect(1:50)
    
    # Définir notre graine aléatoire
    rng = MersenneTwister(1234)

    # Mélanger le tableau aléatoirement selon notre graine
    shuffled_guess = shuffle(rng, guess_order)

    # Parcourir chaque devinette et voir si elle est correcte
    for guess in shuffled_guess

        if guess == target_number
            print("\nL'ordinateur a craqué le code et l'a deviné correctement !")
            break # Arrêter la boucle for si nous l'avons correctement
        end
        
        print("\nL'ordinateur a deviné : $guess")
    end
end
```

### Comment créer Pierre 🪨, Papier 📄, Ciseaux ✂️ en Julia

Si vous n'avez jamais joué à pierre, papier, ciseaux, vous passez à côté de quelque chose ! L'idée de base est que vous essayez de battre votre adversaire avec soit pierre, papier ou ciseaux. 

Dans ce jeu, la pierre bat les ciseaux, les ciseaux battent le papier, et le papier bat la pierre. Si deux personnes font la même chose, vous recommencez.

Dans cet exemple, nous allons jouer à pierre, papier, ciseaux contre l'ordinateur. Nous allons également utiliser la fonction `sleep` pour introduire un court délai comme si quelqu'un disait les mots à voix haute (ce que vous feriez si vous jouiez en personne).

La fonction sleep prend un nombre qui représente la durée (en secondes) pendant laquelle vous voulez suspendre l'exécution. Nous pouvons utiliser cela avec une fonction ou une boucle pour ralentir les choses comme vous le verrez dans ce jeu.

```julia
sleep(1) # Suspendre l'exécution pendant 1 seconde

```

Explorons également une fonction que j'ai découverte en écrivant ce tutoriel, `Base.prompt`, qui nous aide à faire ce que nous faisions précédemment avec `readline`. 

Dans ce cas, cependant, `prompt` ajoute automatiquement un `:` à la fin de la ligne et nous permet d'éviter d'avoir deux lignes séparées pour l'impression et l'entrée utilisateur :

```julia
human_move = Base.prompt("Veuillez entrer 🪨, 📄, ou ✂️")

```

Nous aurons également besoin d'utiliser un `elseif` pour faire fonctionner ce jeu d'exemple. Nous pouvons enchaîner `if`, `elseif` et `else` ensemble pour plus de complétude. Essayez de mettre ensemble les conditionnelles if, les prompts et les sleeps pour obtenir le comportement souhaité, puis consultez le code ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/1-406j3f0e3nN-VxRJUUtK7A.gif)
_Gif de jouer à Pierre Papier Ciseaux dans le REPL Julia_

```julia
# Jeu Pierre 🪨, Papier 📄, Ciseaux ✂️ en Julia

function play_rock_paper_scissors()
    moves = ["🪨", "📄", "✂️"]
    computer_move = moves[rand(1:3)]

    # Base.prompt est similaire à readline que nous avons utilisé avant
    human_move = Base.prompt("Veuillez entrer 🪨, 📄, ou ✂️")
    # Ajoute un ": " à la fin de la ligne par défaut

    print("Pierre...")
    sleep(0.8)

    print("Papier...")
    sleep(0.8)

    print("Ciseaux...")
    sleep(0.8)
    
    print("Feu !\n")

    if computer_move == human_move
        print("Vous avez fait match nul, veuillez réessayer")
    elseif computer_move == "🪨" && human_move == "✂️"
        print("Vous perdez, l'ordinateur a gagné avec 🪨, veuillez réessayer")
    elseif computer_move == "📄" && human_move == "🪨"
        print("Vous perdez, l'ordinateur a gagné avec 📄, veuillez réessayer")
    elseif computer_move == "✂️" && human_move == "📄"
        print("Vous perdez, l'ordinateur a gagné avec ✂️, veuillez réessayer")
    else
        print("Vous avez gagné, l'ordinateur a perdu avec $computer_move, bon travail !")
    end

end
```

### Comment créer un générateur de mots de passe en Julia 🎬

**AVERTISSEMENT : Ne pas utiliser ce code pour générer de vrais mots de passe !**

À l'ère des violations de données sans fin et des personnes utilisant le même mot de passe pour chaque site web, avoir un mot de passe sécurisé est important. Dans cet exemple, nous allons générer un nombre arbitraire de mots de passe avec une longueur variable. 

Étant donné que cela pourrait prendre beaucoup de temps, nous allons également ajouter un package externe, [ProgressBars.jl](https://github.com/cloud-oak/ProgressBars.jl), pour montrer visuellement la progression de notre boucle for. Si vous n'avez jamais ajouté de package externe auparavant, envisagez de [consulter ce tutoriel robuste](https://blog.devgenius.io/the-most-underrated-feature-of-the-julia-programming-language-the-package-manager-652065f45a3a) sur pourquoi le gestionnaire de packages est la fonctionnalité la plus sous-estimée du langage de programmation Julia.

Pour ajouter un package Julia, ouvrez le REPL et tapez `]` suivi de `add ProgressBars`. Après cela, comme nous l'avons fait avec le module Random (notez que nous n'avons pas eu besoin de l'ajouter puisqu'il fait partie de la base de Julia), nous pouvons dire `using ProgressBars` pour le charger.

La principale nouvelle idée que nous allons introduire ici est les vecteurs / tableaux. En Julia, nous pouvons mettre n'importe quel type dans un tableau. Pour créer un tableau vide, nous faisons :

```julia
password_holder = []
```

et ensuite pour ajouter quelque chose, nous utilisons la fonction `push!` comme vous le verrez dans l'exemple ci-dessous. 

Comme mentionné précédemment, nous allons utiliser le package ProgressBars pour montrer la progression à l'écran. Notez que Julia est si rapide qu'il ne montrera probablement pas l'écran de chargement sauf si vous ralentissez manuellement les choses avec un appel de fonction sleep ou un grand nombre de mots de passe. Consultez le README pour un exemple d'utilisation de cela en pratique. 

Comme pour l'autre exemple, essayez de mettre ensemble du code avant de disséquer l'exemple ci-dessous :

```julia
# Générer des mots de passe en Julia
# Source : https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners
using ProgressBars
using Random

# AVERTISSEMENT : Ne pas utiliser ce code pour générer des mots de passe réels !
function generate_passwords()
    num_passwords = parse(Int64, Base.prompt("Combien de mots de passe voulez-vous générer ?"))
    password_length = parse(Int64, Base.prompt("Quelle doit être la longueur de chaque mot de passe ?"))

    # Créer un vecteur / tableau vide
    password_holder = []

    # Générer une barre de progression pour montrer à quel point nous sommes proches de la fin
    for i in ProgressBar(1:num_passwords)
        # Ajouter le nouveau mot de passe dans le porte-mots de passe
        push!(password_holder, randstring(password_length))
        sleep(0.2) # Ralentir manuellement la génération de mots de passe
    end
    
    # Ne montrer les mots de passe que s'il y en a moins de 100
    if length(password_holder) <= 100
        # Parcourir chaque mot de passe un par un
        for password in password_holder
            print("\n", password)
        end
    end
end
```

### Comment créer un simulateur de lancer de dés en Julia 🎲

Les dés sont un moyen amusant d'explorer et de jouer avec l'aléatoire ainsi qu'avec les caractères unicode. 

Julia a un excellent support pour l'unicode, et si vous voulez voir tous les caractères qu'il supporte, [rendez-vous sur la documentation Julia](https://docs.julialang.org/en/v1/manual/unicode-input/). 

Commençons par définir un tableau de faces de dés. Pour accéder aux caractères unicode, nous pouvons utiliser le REPL Julia pour faire une complétion par tabulation en tapant ce qui suit :

```julia
julia> \dicei
```

suivi de la touche tabulation. Cela créera `🀀` qui est "Face de dé-1". Si nous faisons cela pour les 6 côtés d'un dé à 6 faces, nous obtenons :

```julia
dice_faces = ["🎲", "🎲", "🎲", "🎲", "🎲", "🎲"]
```

Pour ce jeu, nous voulons demander continuellement à l'utilisateur s'il veut lancer les dés. S'il le fait, nous générons un nombre aléatoire entre 1 et 6 puis affichons la face du dé à partir du tableau que nous avons créé ci-dessus. 

Tout comme nous l'avons fait dans les projets précédents, nous voudrons utiliser la fonction `rand` comme suit :

```julia
rand(1:num_sides_dice)
```

Essayez cela avant de vérifier une solution possible qui est mise en évidence ci-dessous et gardez à l'esprit comment nous pourrions étendre cela ou utiliser ce code pour programmer un jeu beaucoup plus grand comme Monopoly. 

```julia
# Code de https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function rolling_dice()
    
    # Nombre de faces pour les dés
    num_sides_dice = 6

    # Tant que l'utilisateur veut lancer un dé, continuer à générer un nombre entre 1 et le nombre de faces
    dice_faces = ["🎲", "🎲", "🎲", "🎲", "🎲", "🎲"]
    
    while true
        print("Voulez-vous lancer un dé ? (1=Oui/0=Non) : ")
        guess = parse(Int64, readline())
        # Convertir la valeur d'entrée de chaîne en nombre

        if guess == 1
            println("Lancer de dé")
            current_side = rand(1:num_sides_dice)
            println("Le dé a le nombre $(dice_faces[current_side])")
        elseif guess == 0
            println("Sortie")
            break # Arrêter la boucle while si l'utilisateur décide de le faire
        else
            println("Entrée invalide, veuillez réessayer")
        end 
    end

end 
```

### Comment créer une minuterie de compte à rebours en Julia ⏳

Les comptes à rebours, pour le meilleur ou pour le pire, font partie intégrante de la vie. Du réveillon du Nouvel An à un parent frustré essayant de convaincre un enfant d'obéir à une règle, nous voyons et participons régulièrement à des minuteries de compte à rebours. 

Maintenant, nous allons avoir l'occasion d'en programmer une (youpi). Au cœur, nous allons à nouveau utiliser la fonction `sleep` que nous avons eu l'occasion d'explorer dans l'exemple pierre papier ciseaux.

Pour rappel rapide, `sleep` prend en argument le nombre de secondes pendant lesquelles nous voulons que le programme s'arrête. 

Pour cet exemple, nous allons essayer de faire un peu de nesting de boucles while en utilisant des fonctions. Nous voulons avoir une boucle qui continue à demander à l'utilisateur s'il veut définir une minuterie, et ensuite, s'il le fait, nous appelons une fonction appelée `run_timer`. La fonction `run_timer` doit demander à l'utilisateur d'entrer combien de temps il veut que la minuterie fonctionne. 

Le hic ici est que nous voulons également imprimer combien de temps il reste pour la minuterie à chaque itération. Donc si l'utilisateur entre 5, nous ne pouvons pas simplement faire `sleep(5)` puisque l'utilisateur ne pourra pas voir quoi que ce soit se passer pendant ces 5 secondes. 

Ci-dessous se trouve la fonction principale qui vous est donnée pour commencer. N'hésitez pas à modifier cela comme vous le souhaitez. Utilisez ce code de départ et définissez ensuite la fonction `run_timer` selon la spécification ci-dessus. 

Rappelez-vous, il y a beaucoup de façons possibles d'aborder cela et la solution que nous incluons en bas n'est qu'une approche possible.

```julia
# Code de : https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function run_timer()
	# TODO
end

# Appeler la fonction run_timer dans une boucle jusqu'à ce que l'utilisateur la quitte
function countdown_timer()

    # Tant que l'utilisateur choisit d'exécuter la minuterie de compte à rebours
    while true
        print("Voulez-vous définir une minuterie de compte à rebours ? (1=Oui/0=Non) : ")
        answer = parse(Int64, readline())
        # Convertir la valeur d'entrée de chaîne en nombre

        if answer == 1
            # Exécuter la minuterie
            run_timer()
        elseif answer == 0
            println("Sortie...")
            break # Arrêter la minuterie de compte à rebours
        else
            println("Entrée invalide, veuillez réessayer")
        end 
    end

end
countdown_timer()
```

Essayez et rappelez-vous que vous devrez utiliser les fonctions `parse`, `readline`, `sleep` et `println` pour faire fonctionner cette fonction. 

```julia
# Code de : https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function run_timer()
    print("Entrez le nombre de secondes : ")
    seconds = parse(Int64, readline())
    
    println("Le compte à rebours commence maintenant avec $seconds secondes restantes.")
    current_seconds = seconds

    # Tant que la minuterie de compte à rebours n'est pas terminée
    while current_seconds != 0

        # Imprimer le compte à rebours actuel
        if current_seconds != seconds
            println("Secondes restantes : $current_seconds")
        end

        # Attendre une seconde
        sleep(1)
        current_seconds = current_seconds - 1
    end
    println("Le compte à rebours est terminé !")
end

# Appeler la fonction run_timer dans une boucle jusqu'à ce que l'utilisateur la quitte
function countdown_timer()

    # Tant que l'utilisateur choisit d'exécuter la minuterie de compte à rebours
    while true
        print("Voulez-vous définir une minuterie de compte à rebours ? (1=Oui/0=Non) : ")
        answer = parse(Int64, readline())
        # Convertir la valeur d'entrée de chaîne en nombre

        if answer == 1
            # Exécuter la minuterie
            run_timer()
        elseif answer == 0
            println("Sortie...")
            break # Arrêter la minuterie de compte à rebours
        else
            println("Entrée invalide, veuillez réessayer")
        end 
    end

end

countdown_timer()
```

## Conclusion 🎁

J'espère que vous vous êtes autant amusé à travailler et à lire sur ces projets que j'ai eu à les créer. 

Si vous voulez faire votre propre version de cet article et créer de petits projets Julia et les partager avec le monde, n'hésitez pas et ouvrez une PR ici : [https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners](https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners). 

Je peux facilement changer le nom du dépôt pour accueillir un afflux de petits projets.

Je noterai également qu'un exercice comme celui-ci est également un excellent moyen de contribuer potentiellement à Julia. Pendant que je travaillais sur cet article, j'ai pu ouvrir 2 PR à la base Julia que je pense aideront à améliorer l'expérience des développeurs :

* [https://github.com/JuliaLang/julia/pull/43635](https://github.com/JuliaLang/julia/pull/43635) et
* [https://github.com/JuliaLang/julia/pull/43640](https://github.com/JuliaLang/julia/pull/43640).

Si vous avez aimé ce tutoriel, [connectons-nous sur Twitter](https://twitter.com/OfficialLoganK).