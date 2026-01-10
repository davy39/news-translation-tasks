---
title: Le manuel de programmation C pour débutants
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-08-29T20:38:16.000Z'
originalURL: https://freecodecamp.org/news/the-c-programming-handbook-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726039032547/73b9df27-a4f7-4ee2-81c0-d1e3db521cdb.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: c programming
  slug: c-programming
- name: handbook
  slug: handbook
seo_title: Le manuel de programmation C pour débutants
seo_desc: 'C is one of the oldest, most widely known, and most influential programming
  languages.

  It is used in many industries because it is a highly flexible and powerful language.

  Learning C is a worthwhile endeavor – no matter your starting point or aspirat...'
---

C est l'un des plus anciens, des plus connus et des plus influents langages de programmation.

Il est utilisé dans de nombreuses industries car c'est un langage hautement flexible et puissant.

Apprendre C est une entreprise qui en vaut la peine – peu importe votre point de départ ou vos aspirations – car il construit une base solide dans les compétences dont vous aurez besoin pour le reste de votre carrière en programmation.

Il vous aide à comprendre comment un ordinateur fonctionne sous le capot, comme la façon dont il stocke et récupère les informations et à quoi ressemble l'architecture interne.

Cela dit, C peut être un langage difficile à apprendre, surtout pour les débutants, car il peut être cryptique.

Ce manuel vise à vous enseigner les fondamentaux de la programmation C et est écrit en pensant au programmeur débutant.

Il n'y a pas de prérequis, et aucune connaissance préalable de concepts de programmation n'est supposée.

Si vous n'avez jamais programmé auparavant et que vous êtes un débutant complet, vous êtes au bon endroit.

Voici ce que vous allez apprendre dans ce manuel :

* [Chapitre 1 : Introduction à la programmation C](#chapter-1)
    
* [Chapitre 2 : Variables et types de données en C](#chapter-2)
    
* [Chapitre 3 : Opérateurs en C](#chapter-3)
    
* [Chapitre 4 : Instructions conditionnelles en C](#chapter-4)
    
* [Chapitre 5 : Boucles en C](#chapter-5)
    
* [Chapitre 6 : Tableaux en C](#chapter-6)
    
* [Chapitre 7 : Chaînes de caractères en C](#chapter-7)
    
* [Apprentissage supplémentaire : Sujets avancés en C](#further-learning)
    

Sans plus tarder, commençons à apprendre C !

## Chapitre 1 : Introduction à la programmation C

Dans ce chapitre introductif, vous apprendrez les principales caractéristiques et cas d'utilisation du langage de programmation C.

Vous apprendrez également les bases de la syntaxe C et vous familiariserez avec la structure générale de tous les programmes C.

À la fin du chapitre, vous aurez configuré un environnement de développement pour la programmation C afin de pouvoir suivre les exemples de code de ce livre sur votre machine locale.

Vous aurez écrit, compilé et exécuté avec succès votre premier programme C simple qui imprime le texte "Hello, world!" à l'écran.

Vous aurez également appris certaines fonctionnalités fondamentales du langage C, telles que les commentaires pour documenter et expliquer votre code et les séquences d'échappement pour représenter les caractères non imprimables dans le texte.

### Qu'est-ce que la programmation ?

Les ordinateurs ne sont pas si intelligents.

Même s'ils peuvent traiter des données sans relâche et effectuer des opérations à très haute vitesse, ils ne peuvent pas penser par eux-mêmes. Ils ont besoin de quelqu'un pour leur dire quoi faire ensuite.

Les humains disent aux ordinateurs quoi faire et exactement comment le faire en leur donnant des instructions détaillées et étape par étape à suivre.

Une collection d'instructions détaillées est connue sous le nom de programme.

La programmation est le processus d'écriture de la collection d'instructions qu'un ordinateur peut comprendre et exécuter pour effectuer une tâche spécifique et résoudre un problème particulier.

Un langage de programmation est utilisé pour écrire les instructions.

Et les humains qui écrivent les instructions et les fournissent à l'ordinateur sont connus sous le nom de programmeurs.

#### Langages de programmation de bas niveau VS de haut niveau VS de niveau intermédiaire – Quelle est la différence ?

Il existe trois types de langages de programmation : les langages de bas niveau, les langages de haut niveau et les langages de niveau intermédiaire.

Les langages de bas niveau incluent le langage machine (également connu sous le nom de binaire) et le langage d'assemblage.

Les deux langages fournissent peu ou pas d'abstraction par rapport au matériel de l'ordinateur. Les instructions du langage sont étroitement liées ou correspondent directement à des instructions machine spécifiques.

Cette "proximité avec la machine" permet la vitesse, l'efficacité, une moindre consommation de mémoire et un contrôle fin sur le matériel de l'ordinateur.

Le langage machine est le niveau le plus bas des langages de programmation.

Les instructions consistent en des séries de `0` et de `1` qui correspondent directement aux instructions et aux emplacements mémoire d'un ordinateur particulier.

Les instructions sont également directement exécutées par le processeur de l'ordinateur.

Même si le langage machine était le langage de choix pour écrire des programmes dans les premiers jours de l'informatique, ce n'est pas un langage lisible par l'homme et il est chronophage à écrire.

Le langage d'assemblage permet au programmeur de travailler en étroite collaboration avec la machine à un niveau légèrement supérieur.

Il utilise des mnémoniques et des symboles qui correspondent directement à l'ensemble d'instructions d'une machine particulière au lieu d'utiliser des séquences de `0` et de `1`.

Ensuite, les langages de haut niveau, comme Python et JavaScript, sont éloignés de l'ensemble d'instructions d'une architecture machine particulière.

Leur syntaxe ressemble à la langue anglaise, ce qui les rend plus faciles à utiliser et à comprendre.

Les programmes écrits dans des langages de haut niveau sont également portables et indépendants de la machine. C'est-à-dire qu'un programme peut s'exécuter sur n'importe quel système qui supporte ce langage.

Cela dit, ils tendent à être plus lents, à consommer plus de mémoire et à rendre plus difficile le travail avec le matériel et les systèmes de bas niveau en raison de leur niveau d'abstraction.

Enfin, les langages de niveau intermédiaire, comme C et C++, servent de pont entre les langages de programmation de bas niveau et de haut niveau.

Ils permettent une proximité et un niveau de contrôle sur le matériel informatique. En même temps, ils offrent également un niveau d'abstraction avec des instructions plus lisibles et compréhensibles pour les programmeurs.

### Qu'est-ce que le langage de programmation C ?

C est un langage de programmation généraliste et procédural.

Un langage procédural est un type de langage de programmation qui suit une approche étape par étape pour résoudre un problème.

Il utilise une série d'instructions, également connues sous le nom de procédures ou de fonctions, qui sont exécutées dans un ordre spécifique pour effectuer des tâches et atteindre des objectifs. Ces instructions disent à l'ordinateur étape par étape quoi faire et dans quel ordre.

Ainsi, les programmes C sont divisés en fonctions plus petites et plus spécifiques qui accomplissent une certaine tâche et sont exécutées séquentiellement, l'une après l'autre, suivant une approche de haut en bas.

Cela favorise la lisibilité et la maintenabilité du code.

#### Une brève histoire du langage de programmation C

C a été développé au début des années 1970 par Dennis Ritchie aux laboratoires Bell d'AT&T.

Le développement de C était étroitement lié au développement du système d'exploitation Unix aux laboratoires Bell.

Historiquement, les systèmes d'exploitation étaient généralement écrits en langage d'assemblage et sans portabilité à l'esprit.

Lors du développement d'Unix, il y avait un besoin pour un langage de programmation plus efficace et portable pour écrire des systèmes d'exploitation.

Dennis Ritchie a créé un langage appelé B, qui était une évolution d'un langage précédent appelé BCPL (Basic Combined Programming Language).

Il visait à combler le fossé entre les capacités de bas niveau de l'assemblage et les langages de haut niveau utilisés à l'époque, tels que Fortran.

B n'était pas assez puissant pour supporter le développement d'Unix, donc Dennis Ritchie a développé un nouveau langage qui s'inspirait de B et BCPL et avait quelques fonctionnalités supplémentaires. Il a nommé ce langage C.

La conception simple de C, sa vitesse, son efficacité, ses performances et sa relation étroite avec le matériel informatique en ont fait un choix attrayant pour la programmation système. Cela a conduit à la réécriture du système d'exploitation Unix en C.

#### Caractéristiques et cas d'utilisation du langage C

Malgré le fait que C soit un langage relativement ancien (par rapport à d'autres langages de programmation plus modernes utilisés aujourd'hui), il a résisté à l'épreuve du temps et reste toujours populaire.

Selon l'[index TIOBE](https://www.tiobe.com/tiobe-index/), qui mesure la popularité des langages de programmation chaque mois, C est le deuxième langage de programmation le plus populaire en août 2023.

Cela est dû au fait que C est considéré comme la "mère des langages de programmation" et est l'un des langages les plus fondamentaux de l'informatique.

La plupart des langages modernes et populaires utilisés aujourd'hui utilisent soit C sous le capot, soit s'en inspirent.

Par exemple, l'implémentation par défaut de Python et son interpréteur, CPython, sont écrits en C. Et des langages tels que C++ et C# sont des extensions de C et fournissent des fonctionnalités supplémentaires.

Même si C a été initialement conçu en pensant à la programmation système, il est largement utilisé dans de nombreux autres domaines de l'informatique.

Les programmes C sont portables et faciles à implémenter, ce qui signifie qu'ils peuvent être exécutés sur différentes plateformes avec des modifications minimales.

C permet également une manipulation et une gestion efficaces et directes de la mémoire, ce qui en fait un langage idéal pour les applications critiques en termes de performance.

Et C fournit des abstractions de haut niveau ainsi que des capacités de bas niveau, ce qui permet aux programmeurs d'avoir un contrôle fin sur les ressources matérielles lorsqu'ils en ont besoin.

Ces caractéristiques font de C un langage idéal pour créer des systèmes d'exploitation, des systèmes embarqués, des utilitaires système, des appareils de l'Internet des objets (IoT), des systèmes de bases de données et diverses autres applications.

C est utilisé pratiquement partout aujourd'hui.

### Comment configurer un environnement de développement pour la programmation C sur votre machine locale

Pour commencer à écrire des programmes C sur votre machine locale, vous aurez besoin des éléments suivants :

* Un compilateur C
    
* Un environnement de développement intégré (IDE)
    

C est un langage de programmation compilé, comme Go, Java, Swift et Rust.

Les langages compilés sont différents des langages interprétés, tels que PHP, Ruby, Python et JavaScript.

La différence entre les langages compilés et interprétés est qu'un langage compilé est directement traduit en code machine en une seule fois.

Ce processus est effectué par un programme spécial appelé compilateur.

Le compilateur lit l'ensemble du code source, vérifie les erreurs et traduit ensuite l'ensemble du programme en code machine. Il s'agit d'un langage que l'ordinateur peut comprendre et qui est directement associé aux instructions particulières de l'ordinateur.

Ce processus crée un fichier binaire exécutable autonome contenant des séquences de `0` et de `1` qui est une forme plus adaptée à l'ordinateur du code source initial. Ce fichier contient des instructions que l'ordinateur peut comprendre et exécuter directement.

Un langage interprété, en revanche, n'est pas traduit en code machine en une seule fois et ne produit pas de fichier exécutable binaire.

Au lieu de cela, un interpréteur lit et exécute le code source instruction par instruction, ligne par ligne. L'interpréteur lit chaque ligne, la traduit en code machine, puis l'exécute immédiatement.

Si vous utilisez un système Unix ou un système de type Unix tel que macOS ou Linux, vous avez probablement déjà installé la populaire [GNU Compiler Collection (GCC)](https://gcc.gnu.org/) sur votre machine.

Si vous utilisez l'un de ces systèmes d'exploitation, ouvrez l'application terminal et tapez la commande suivante :

```plaintext
gcc --version
```

Si vous utilisez macOS et que vous n'avez pas installé les outils de développement en ligne de commande, une boîte de dialogue s'ouvrira vous demandant de les installer – donc si vous voyez cela, allez-y et faites-le.

Si vous avez déjà installé les outils en ligne de commande, vous verrez une sortie avec la version du compilateur, qui ressemblera à ce qui suit :

```plaintext
Apple clang version 14.0.0 (clang-1400.0.29.202)
```

Si vous utilisez Windows, vous pouvez consulter [Code::Blocks](https://www.codeblocks.org/) ou envisager d'installer [Linux sur Windows avec WSL](https://learn.microsoft.com/en-us/windows/wsl/install). N'hésitez pas à choisir l'environnement de programmation qui vous convient le mieux.

Un IDE est l'endroit où vous écrivez, éditez, enregistrez, exécutez et déboguez vos programmes C. Vous pouvez le considérer comme un traitement de texte mais pour écrire du code.

[Visual Studio Code](https://code.visualstudio.com/) est un excellent éditeur pour écrire du code et offre de nombreuses fonctionnalités similaires à celles d'un IDE.

Il est gratuit, open-source, supporte de nombreux langages de programmation et est disponible pour tous les systèmes d'exploitation.

Une fois que vous avez téléchargé Visual Studio Code, installez l'[extension C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools).

Il est également judicieux d'activer l'enregistrement automatique en sélectionnant : "Fichier" -> "Enregistrement automatique".

Si vous souhaitez en savoir plus, vous pouvez consulter la [documentation de Visual Studio Code pour C/C++](https://code.visualstudio.com/docs/languages/cpp).

Avec votre machine locale entièrement configurée, vous êtes prêt à écrire votre premier programme C !

### Comment écrire votre premier programme C

Pour commencer, ouvrez Visual Studio Code et créez un nouveau dossier pour votre programme C en naviguant vers "Fichier" -> "Ouvrir" -> "Nouveau dossier".

Donnez un nom à ce dossier, par exemple, `c-practice`, puis sélectionnez "Créer" -> "Ouvrir".

Vous devriez maintenant avoir le dossier `c-practice` ouvert dans Visual Studio Code.

À l'intérieur du dossier que vous venez de créer, créez un nouveau fichier C.

Maintenez la touche `Commande` enfoncée et appuyez sur `N` sur macOS ou maintenez la touche `Contrôle` enfoncée et appuyez sur `N` pour Windows/Linux pour créer un fichier `Sans-titre-1`.

Maintenez la touche `Commande` enfoncée et appuyez sur `S` sur macOS ou maintenez la touche `Contrôle` enfoncée et appuyez sur `S` pour Windows/Linux, et enregistrez le fichier sous le nom `main.c`.

Enfin, cliquez sur "Enregistrer".

Assurez-vous d'enregistrer le fichier que vous avez créé avec une extension `.c`, sinon il ne sera pas un fichier C valide.

Vous devriez maintenant avoir le fichier `main.c` que vous venez de créer ouvert dans Visual Studio Code.

Ensuite, ajoutez le code suivant :

```c
#include <stdio.h>

int main(void) {

  // affiche 'Hello, world!' sur la console

  printf("Hello, world!\n");
}
```

Passons en revue chaque ligne et expliquons ce qui se passe dans le programme.

#### Qu'est-ce que les fichiers d'en-tête en C ?

Commençons par la première ligne, `#include <stdio.h>`.

La partie `#include` de `#include <stdio.h>` est une commande de préprocesseur qui indique au compilateur C d'inclure un fichier.

Plus précisément, elle indique au compilateur d'inclure le fichier d'en-tête `stdio.h`.

Les fichiers d'en-tête sont des bibliothèques externes.

Cela signifie que certains développeurs ont écrit des fonctionnalités et des caractéristiques qui ne sont pas incluses dans le noyau du langage C.

En ajoutant des fichiers d'en-tête à votre code, vous obtenez des fonctionnalités supplémentaires que vous pouvez utiliser dans vos programmes sans avoir à écrire le code à partir de zéro.

Le fichier d'en-tête `stdio.h` signifie entrée-sortie standard.

Il contient des définitions de fonctions pour les opérations d'entrée et de sortie, telles que des fonctions pour recueillir des données utilisateur et imprimer des données sur la console.

Plus précisément, il fournit des fonctions telles que `printf()` et `scanf()`.

Ainsi, cette ligne est nécessaire pour que la fonction que nous avons plus loin dans notre programme, `printf()`, fonctionne.

Si vous n'incluez pas le fichier `stdio.h` en haut de votre code, le compilateur ne comprendra pas ce qu'est la fonction `printf()`.

#### Qu'est-ce que la fonction `main()` en C ?

Ensuite, `int main(void) {}` est la fonction principale et le point de départ de chaque programme C.

C'est la première chose qui est appelée lorsque le programme est exécuté.

Chaque programme C doit inclure une fonction `main()`.

Le mot-clé `int` dans `int main(void) {}` indique la valeur de retour de la fonction `main()`.

Dans ce cas, la fonction retournera un nombre entier.

Et le mot-clé `void` à l'intérieur de la fonction `main()` indique que la fonction ne reçoit aucun argument.

Tout ce qui se trouve entre les accolades, `{}`, est considéré comme le corps de la fonction – c'est ici que vous incluez le code que vous souhaitez écrire. Tout code écrit ici s'exécutera toujours en premier.

Cette ligne sert de modèle et de point de départ pour tous les programmes C. Elle permet à l'ordinateur de savoir où commencer à lire le code lorsqu'il exécute vos programmes.

#### Qu'est-ce que les commentaires en C ?

En programmation C, les commentaires sont des lignes de texte qui sont ignorées par le compilateur.

Écrire des commentaires est un moyen de fournir des informations supplémentaires et de décrire la logique, le but et la fonctionnalité de votre code.

Les commentaires fournissent un moyen de documenter votre code et de le rendre plus lisible et compréhensible pour quiconque le lira et travaillera avec.

Avoir des commentaires dans votre code source est également utile pour vous-même à l'avenir. Ainsi, lorsque vous reviendrez au code dans quelques mois et que vous ne vous souviendrez plus de son fonctionnement, ces commentaires pourront vous aider.

Les commentaires sont également utiles pour le débogage et le dépannage. Vous pouvez temporairement commenter des lignes de code pour isoler les problèmes.

Cela vous permettra d'ignorer une section de code et de vous concentrer sur la partie du code que vous testez et sur laquelle vous travaillez sans avoir à supprimer quoi que ce soit.

Il existe deux types de commentaires en C :

* Commentaires sur une seule ligne
    
* Commentaires sur plusieurs lignes
    

Les commentaires sur une seule ligne commencent par deux barres obliques, `//`, et continuent jusqu'à la fin de la ligne.

Voici la syntaxe pour créer un commentaire sur une seule ligne en C :

```c
// Je suis un commentaire sur une seule ligne
```

Tout texte écrit après les barres obliques et sur la même ligne est ignoré par le compilateur.

Les commentaires sur plusieurs lignes commencent par une barre oblique, `/`, suivie d'un astérisque, `*`, et se terminent par un astérisque, suivi d'une barre oblique.

Comme leur nom l'indique, ils s'étendent sur plusieurs lignes.

Ils offrent un moyen d'écrire des explications ou des notes légèrement plus longues dans votre code et d'expliquer plus en détail son fonctionnement.

Voici la syntaxe pour créer un commentaire sur plusieurs lignes en C :

```c
/*
Ceci est
un commentaire
sur plusieurs lignes
*/
```

### Qu'est-ce que la fonction `printf()` en C ?

À l'intérieur du corps de la fonction, la ligne `printf("Hello, World!\n");` imprime le texte `Hello, World!` sur la console (ce texte est également connu sous le nom de chaîne de caractères).

Chaque fois que vous souhaitez afficher quelque chose, utilisez la fonction `printf()`.

Entourez le texte que vous souhaitez afficher de guillemets doubles, `""`, et assurez-vous qu'il se trouve à l'intérieur des parenthèses de la fonction `printf()`.

Le point-virgule, `;`, termine l'instruction. Toutes les instructions doivent se terminer par un point-virgule en C, car il identifie la fin de l'instruction.

Vous pouvez considérer un point-virgule de la même manière qu'un point final/met fin à une phrase.

### Qu'est-ce que les séquences d'échappement en C ?

Avez-vous remarqué le `\n` à la fin de `printf("Hello, World!\n");` ?

C'est ce qu'on appelle une séquence d'échappement, ce qui signifie qu'il s'agit d'un caractère qui crée une nouvelle ligne et indique au curseur de passer à la ligne suivante lorsqu'il le voit.

En programmation, une séquence d'échappement est une combinaison de caractères qui représente un caractère spécial dans une chaîne.

Ils fournissent un moyen d'inclure des caractères spéciaux qui sont difficiles à représenter directement dans une chaîne.

Ils consistent en une barre oblique inverse, `\`, également connue sous le nom de caractère d'échappement, suivie d'un ou plusieurs caractères supplémentaires.

La séquence d'échappement pour un caractère de nouvelle ligne est `\n`.

Une autre séquence d'échappement est `\t`. Le `\t` représente un caractère de tabulation et insérera un espace dans une chaîne.

### Comment compiler et exécuter votre premier programme C

Dans la section précédente, vous avez écrit votre premier programme C :

```c
#include <stdio.h>

int main(void) {

  // affiche 'Hello, world!' sur la console

  printf("Hello, world!\n");
}
```

Tout code que vous écrivez dans le langage de programmation C est appelé code source.

Votre ordinateur ne comprend aucun des énoncés C que vous avez écrits, donc ce code source doit être traduit dans un format différent que l'ordinateur peut comprendre. C'est là que le compilateur que vous avez installé précédemment entre en jeu.

Le compilateur lira le programme et le traduira dans un format plus proche du langage natif de l'ordinateur et rendra votre programme adapté à l'exécution.

Vous pourrez voir la sortie de votre programme, qui devrait être `Hello, world!`.

La compilation d'un programme C se compose de quatre étapes : le prétraitement, la compilation, l'assemblage et l'édition des liens.

La première étape est le prétraitement.

Le préprocesseur parcourt le code source pour trouver les directives de préprocesseur, qui sont toutes les lignes commençant par un symbole `#`, comme `#include`.

Une fois que le préprocesseur trouve ces lignes, il les remplace par autre chose.

Par exemple, lorsque le préprocesseur trouve la ligne `#include <stdio.h>`, le `#include` indique au préprocesseur d'inclure tout le code du fichier d'en-tête `stdio.h`.

Ainsi, il remplace la ligne `#include <stdio.h>` par le contenu réel du fichier `stdio.h`.

Le résultat de cette phase est une version modifiée du code source.

Après le prétraitement, l'étape suivante est la phase de compilation, où le code source modifié est traduit en code d'assemblage correspondant.

S'il y a des erreurs, la compilation échouera et vous devrez corriger les erreurs pour continuer.

L'étape suivante est la phase d'assemblage, où l'assembleur convertit les instructions de code d'assemblage générées en instructions de code machine.

Le résultat de cette phase est un fichier objet, qui contient les instructions de code machine.

La dernière étape est la phase d'édition des liens.

L'édition des liens est le processus de combinaison du fichier objet généré à partir de la phase d'assemblage avec les bibliothèques nécessaires pour créer le fichier binaire exécutable final.

Maintenant, passons en revue les commandes que vous devez entrer pour compiler votre fichier `main.c`.

Dans Visual Studio Code, ouvrez le terminal intégré en sélectionnant "Terminal" -> "Nouveau Terminal".

À l'intérieur du terminal, entrez la commande suivante :

```plaintext
gcc main.c
```

La partie `gcc` de la commande fait référence au compilateur C, et `main.c` est le fichier qui contient le code C que vous souhaitez compiler.

Ensuite, entrez la commande suivante :

```plaintext
ls
```

La commande `ls` liste le contenu du répertoire courant.

```plaintext
a.out  main.c
```

Le résultat de cette commande montre un fichier `a.out` – il s'agit du fichier exécutable contenant les instructions du code source dans leurs instructions binaires correspondantes.

Le `a.out` est le nom par défaut du fichier exécutable créé lors du processus de compilation.

Pour exécuter ce fichier, entrez la commande suivante :

```plaintext
./a.out
```

Cette commande indique à l'ordinateur de chercher dans le répertoire courant, `./`, un fichier nommé `a.out`.

La commande ci-dessus génère la sortie suivante :

```plaintext
Hello, world!
```

Vous avez également la possibilité de nommer le fichier exécutable au lieu de le laisser avec le nom par défaut `a.out`.

Supposons que vous souhaitiez nommer le fichier exécutable `helloWorld`.

Si vous souhaitiez faire cela, vous devriez entrer la commande suivante :

```plaintext
gcc -o helloWorld main.c
```

Cette commande avec l'option `-o` (qui signifie output) indique au compilateur `gcc` de créer un fichier exécutable nommé `helloWorld`.

Pour exécuter le nouveau fichier exécutable que vous venez de créer, entrez la commande suivante :

```plaintext
./helloWorld
```

C'est le résultat de la commande ci-dessus :

```plaintext
Hello, world!
```

Notez que chaque fois que vous apportez une modification à votre fichier de code source, vous devez répéter le processus de compilation et d'exécution de votre programme à partir du début pour voir les modifications que vous avez apportées.

## Chapitre 2 : Variables et types de données

Dans ce chapitre, vous apprendrez les bases des variables et des types de données – les unités de stockage fondamentales qui vous permettent de préserver et de manipuler des données dans vos programmes.

À la fin de ce chapitre, vous saurez comment déclarer et initialiser des variables.

Vous aurez également appris les différents types de données disponibles en C, tels que les entiers, les nombres à virgule flottante et les caractères, qui dictent comment les informations sont traitées et stockées dans la mémoire d'un programme.

Enfin, vous aurez appris comment recevoir l'entrée de l'utilisateur dans vos programmes et comment utiliser des constantes pour stocker des valeurs que vous ne souhaitez pas voir modifiées.

### Qu'est-ce qu'une variable en C ?

Les variables stockent différents types de données dans la mémoire de l'ordinateur et occupent une certaine quantité d'espace.

En stockant des informations dans une variable, vous pouvez les récupérer et les manipuler, effectuer divers calculs ou même les utiliser pour prendre des décisions dans votre programme.

Les données stockées reçoivent un nom, et c'est ainsi que vous pouvez y accéder lorsque vous en avez besoin.

### Comment déclarer des variables en C

Avant de pouvoir utiliser une variable, vous devez la déclarer – cette étape permet au compilateur de savoir qu'il doit allouer de la mémoire pour elle.

C est un langage fortement typé, donc pour déclarer une variable en C, vous devez d'abord spécifier le type de données que la variable contiendra, comme un entier pour stocker un nombre entier, un nombre à virgule flottante pour les nombres avec des décimales, ou un char pour un seul caractère.

Ainsi, lors de la compilation, le compilateur sait si la variable est capable d'effectuer les actions pour lesquelles elle a été conçue.

Une fois que vous avez spécifié le type de données, vous donnez un nom à la variable.

La syntaxe générale pour déclarer des variables ressemble à ceci :

```plaintext
type_de_donnees nom_variable;
```

Prenons l'exemple suivant :

```c
#include <stdio.h>

int main(void) {

    int age;
}
```

Dans l'exemple ci-dessus, j'ai déclaré une variable nommée `age` qui contiendra des valeurs entières.

#### Quelles sont les conventions de nommage pour les variables en C ?

En ce qui concerne les noms de variables, ils doivent commencer soit par une lettre, soit par un trait de soulignement.

Par exemple, `age` et `_age` sont des noms de variables valides.

De plus, ils peuvent contenir n'importe quelle lettre majuscule ou minuscule, des chiffres ou un caractère de soulignement. Il ne peut y avoir aucun autre symbole spécial à part un trait de soulignement.

Enfin, les noms de variables sont sensibles à la casse. Par exemple, `age` est différent de `Age`.

### Comment initialiser des variables en C

Une fois que vous avez déclaré une variable, il est bon de l'initialiser, ce qui implique d'assigner une valeur initiale à la variable.

La syntaxe générale pour initialiser une variable ressemble à ceci :

```plaintext
type_de_donnees nom_variable = valeur;
```

L'opérateur d'assignation, `=`, est utilisé pour assigner la `valeur` au `nom_variable`.

Prenons l'exemple précédent et assignons à `age` une valeur :

```c
#include <stdio.h>

int main(void) {

    int age;

    age = 29;
}
```

J'ai initialisé la variable `age` en lui assignant une valeur entière de `29`.

Cela dit, vous pouvez combiner les étapes d'initialisation et de déclaration au lieu de les effectuer séparément :

```c
#include <stdio.h>

int main(void) {

    // déclaration + initialisation
    int age = 29;
}
```

### Comment mettre à jour les valeurs des variables en C

Les valeurs des variables peuvent changer.

Par exemple, vous pouvez changer la valeur de `age` sans avoir à spécifier son type à nouveau.

Voici comment vous changeriez sa valeur de `29` à `30` :

```c
#include <stdio.h>

int main(void) {

    // la variable age avec sa valeur originale
    int age = 29;

    // changement de la valeur de age
    // la nouvelle valeur sera 30
    age = 30;
}
```

Notez que le type de données de la nouvelle valeur assignée doit correspondre au type de données déclaré de la variable.

Si ce n'est pas le cas, le programme ne s'exécutera pas comme prévu. Le compilateur générera une erreur lors de la compilation.

```c
#include <stdio.h>

int main(void) {

    int age = 29;
    
    /*
    tentative d'assigner une valeur à virgule flottante
    à une variable de type int
    provoquera une erreur dans votre programme
    */
    age = 29.5;
}
```

### Quels sont les types de données de base en C ?

Les types de données spécifient la forme que l'information peut prendre dans les programmes C. Et ils déterminent quel type d'opérations peuvent être effectuées sur cette information.

Il existe divers types de données intégrés en C tels que `char`, `int` et `float`.

Chacun des types de données nécessite une allocation de mémoire différente.

Avant d'explorer chacun d'eux plus en détail, passons d'abord en revue la différence entre les types de données signés et non signés en C.

Les types de données signés peuvent représenter à la fois des valeurs positives et négatives.

D'autre part, les types de données non signés ne peuvent représenter que des valeurs non négatives (zéro et valeurs positives).

Vous vous demandez quand utiliser les types de données signés et quand utiliser les types de données non signés ?

Utilisez les types de données signés lorsque vous devez représenter à la fois des valeurs positives et négatives, comme lorsque vous travaillez avec des nombres qui peuvent avoir des variations positives et négatives.

Et utilisez les types de données non signés lorsque vous voulez vous assurer qu'une variable ne peut contenir que des valeurs non négatives, comme lorsque vous traitez des quantités.

Maintenant, examinons les types de données C plus en détail.

#### Qu'est-ce que le type de données `char` en C ?

Le type de données le plus basique en C est `char`.

Il signifie "caractère" et c'est l'un des types de données les plus simples et les plus fondamentaux du langage de programmation C.

Vous l'utilisez pour stocker un seul caractère individuel tel qu'une lettre majuscule et minuscule du tableau ASCII (American Standard Code for Information Interchange).

Quelques exemples de `char` sont `'a'` et `'Z'`.

Il peut également stocker des symboles tels que `'!'`, et des chiffres tels que `'7'`.

Voici un exemple de la façon de créer une variable qui contiendra une valeur `char` :

```c
#include <stdio.h>

int main(void) {

    char initial = 'D';

 }
```

Remarquez comment j'ai utilisé des guillemets simples autour du caractère unique.

C'est parce que vous ne pouvez pas utiliser de guillemets doubles lorsque vous travaillez avec des `char`.

Les guillemets doubles sont utilisés pour les chaînes de caractères.

En ce qui concerne l'allocation de mémoire, un `char` signé vous permet de stocker des nombres allant de `[-128 à 127`\], et utilise au moins 1 octet (ou 8 bits) de mémoire.

Un char non signé stocke des nombres allant de `[0 à 255]`.

#### Qu'est-ce que le type de données `int` en C ?

Un `int` est un entier, qui est également connu sous le nom de nombre entier.

Il peut contenir une valeur positive ou négative ou `0`, mais il ne peut pas contenir de nombres qui contiennent des points décimaux (comme `3.5`).

Quelques exemples d'entiers sont `0`, `-3`, et `9`.

Voici comment vous créez une variable qui contiendra une valeur `int` :

```c
#include <stdio.h>

int main(void) {

    int age = 29;
 }
```

Lorsque vous déclarez un `int`, l'ordinateur alloue au moins 2 octets (ou 16 bits) de mémoire.

Cela dit, sur la plupart des systèmes modernes, un `int` alloue généralement 4 octets (ou 32 bits) de mémoire.

La plage de nombres disponibles pour un `int` signé est `[-32,768 à 32,767]` lorsqu'il occupe 2 octets et `[-2,147,483,648 à 2,147,483,647]` lorsqu'il occupe 4 octets de mémoire.

La plage de nombres pour un `int` non signé n'inclut aucun des nombres négatifs de la plage mentionnée pour les `int` signés.

Ainsi, la plage de nombres pour les `int` non signés qui occupent 2 octets de mémoire est `[0 à 65,535]` et la plage est `[0 à 4,294,967,295]` pour ceux qui occupent 4 octets.

Pour représenter des nombres plus petits, vous pouvez utiliser un autre type de données – le `short int`. Il occupe généralement 2 octets (ou 16 bits) de mémoire.

Un `short int` signé permet des nombres dans une plage de `[-32,768 à 32,767]`.

Un `short int` non signé permet des nombres dans une plage de `[0 à 65,535]`.

Utilisez un `short` lorsque vous souhaitez travailler avec des entiers plus petits, ou lorsque l'optimisation de la mémoire est d'une importance cruciale.

Si vous devez travailler avec des entiers plus grands, vous pouvez également utiliser d'autres types de données comme `long int` ou `long long int`, qui offrent une plage plus large et une précision plus élevée.

Un `long int` occupe généralement au moins 4 octets de mémoire (ou 32 bits).

Les valeurs pour un `long int` signé vont de `[-2,147,483,648 à 2,147,483,647]`.

Et les valeurs pour un `long int` non signé vont de `[0 à 4,294,967,295]`.

Le type de données `long long int` est capable d'utiliser des nombres encore plus grands qu'un `long int`. Il utilise généralement 8 octets (ou 64 bits) de mémoire.

Un `long long int` signé permet une plage de `[-9,223,372,036,854,775,808 à 9,223,372,036,854,775,807]`

Et un `long long int` non signé a une plage de nombres de `[0 à 18,446,744,073,709,551,615]`.

#### Qu'est-ce que le type de données `float` en C ?

Le type de données `float` est utilisé pour contenir des nombres avec une valeur décimale (qui sont également connus sous le nom de nombres réels).

Il occupe 4 octets (ou 32 bits) de mémoire et il s'agit d'un type à virgule flottante de précision simple.

Voici comment vous créez une variable qui contiendra une valeur `float` :

```c
#include <stdio.h>

int main(void) {

   float temperature = 68.5;
 }
```

Un `double` est une valeur à virgule flottante et est le type de données à virgule flottante le plus couramment utilisé en C.

Il occupe 8 octets (ou 64 bits) de mémoire, et il s'agit d'un type à virgule flottante de double précision.

Voici comment vous créez une variable qui contiendra une valeur `double` :

```c
#include <stdio.h>

int main(void) {

	double number = 3.14159;
 }
```

Lors du choix du type de données à virgule flottante à utiliser, tenez compte du compromis entre l'utilisation de la mémoire et la précision.

Un `float` a moins de précision qu'un `double` mais consomme moins de mémoire.

Utilisez un `float` lorsque l'utilisation de la mémoire est une préoccupation (comme lorsque vous travaillez avec un système aux ressources limitées) ou lorsque vous devez effectuer des calculs où une haute précision n'est pas cruciale.

Si vous nécessitez une précision et une exactitude plus élevées pour vos calculs et que l'utilisation de la mémoire n'est pas cruciale, vous pouvez utiliser un `double`.

### Qu'est-ce que les codes de format en C ?

Les codes de format sont utilisés dans les fonctions d'entrée et de sortie, telles que `scanf()` et `printf()`, respectivement.

Ils agissent comme des espaces réservés et des substituts pour les variables.

Plus précisément, ils spécifient le format attendu de l'entrée et de la sortie.

Ils indiquent au programme comment formater ou interpréter les données transmises ou lues par les fonctions `scanf()` et `printf()`.

La syntaxe des codes de format est le caractère `%` et le spécificateur de format pour le type de données de la variable.

Prenons l'exemple suivant :

```c
#include<stdio.h>

int main(void)
{
	int age = 29;

	printf("My age is %i\n", age);  // Mon âge est 29
}
```

Dans l'exemple ci-dessus, `age` est la variable dans le programme. Elle est de type `int`.

Le code de format – ou espace réservé – pour les valeurs entières est `%i`. Cela indique qu'un entier doit être imprimé.

Dans la sortie du programme, `%i` est remplacé par la valeur de `age`, qui est `29`.

Voici un tableau avec les spécificateurs de format pour chaque type de données :

| SPÉCIFICATEUR DE FORMAT | TYPE DE DONNÉES |
| --- | --- |
| %c | char |
| %c | unsigned char |
| %i, &d | int |
| %u | unsigned int |
| %hi, %hd | short int |
| %hu | unsigned short int |
| %li ou %ld | long int |
| %lu | unsigned long int |
| %lli ou %lld | long long int |
| %llu | unsigned long long int |
| %f | float |
| %lf | double |
| %Lf | long double |

### Comment recevoir l'entrée de l'utilisateur en utilisant la fonction `scanf()`

Plus tôt, vous avez vu comment imprimer quelque chose sur la console en utilisant la fonction `printf()`.

Mais que se passe-t-il lorsque vous souhaitez recevoir l'entrée de l'utilisateur ? C'est là que la fonction `scanf()` entre en jeu.

La fonction `scanf()` lit l'entrée de l'utilisateur, qui est généralement saisie via un clavier.

L'utilisateur entre une valeur, appuie sur la touche Entrée, et la valeur est enregistrée dans une variable.

La syntaxe générale pour utiliser `scanf()` ressemble à quelque chose de similaire à ce qui suit :

```c
scanf("format_string", &variable);
```

Décomposons cela :

* `format_string` est la chaîne qui permet à l'ordinateur de savoir à quoi s'attendre. Elle spécifie le format attendu de l'entrée. Par exemple, s'agit-il d'un mot, d'un nombre ou de quelque chose d'autre ?
    
* `&variable` est le pointeur vers la variable où vous souhaitez stocker la valeur recueillie à partir de l'entrée de l'utilisateur.
    

Regardons un exemple de `scanf()` en action :

```c
#include <stdio.h>

int main(void) {
  
  int number;

  printf("Please enter your age: ");
  
  scanf("%i", &number);

  printf("Your age is %i\n", number);
}
```

Dans l'exemple ci-dessus, je dois d'abord inclure le fichier d'en-tête `stdio.h`, qui fournit des fonctions d'entrée et de sortie en C.

Ensuite, dans la fonction `main()`, je déclare une variable nommée `number` qui contiendra des valeurs entières. Cette variable stockera l'entrée de l'utilisateur.

Ensuite, je demande à l'utilisateur d'entrer un nombre en utilisant la fonction `printf()`.

Ensuite, j'utilise `scanf()` pour lire et enregistrer la valeur que l'utilisateur entre.

Le spécificateur de format `%i` permet à l'ordinateur de savoir qu'il doit s'attendre à une entrée entière.

Remarquez également le symbole `&` avant le nom de la variable. Oublier de l'ajouter provoquera une erreur.

Enfin, après avoir reçu l'entrée, j'affiche la valeur reçue sur la console en utilisant une autre fonction `printf()`.

### Qu'est-ce que les constantes en C ?

Comme vous l'avez vu précédemment, les valeurs des variables peuvent être modifiées tout au long de la vie d'un programme.

Cela dit, il peut y avoir des moments où vous ne souhaitez pas qu'une valeur soit modifiée. C'est là que les constantes sont utiles.

En C, une constante est une variable avec une valeur qui ne peut pas être modifiée après la déclaration et pendant l'exécution du programme.

Vous pouvez créer une constante de manière similaire à la création de variables.

Les différences entre les constantes et les variables sont que, avec les constantes, vous devez utiliser le mot-clé `const` avant de mentionner le type de données.

Et lorsque vous travaillez avec des constantes, vous devez toujours spécifier une valeur.

La syntaxe générale pour déclarer des constantes en C ressemble à ceci :

```plaintext
const type_de_donnees nom_constante = valeur;
```

Ici, `type_de_donnees` représente le type de données de la constante, `nom_constante` est le nom que vous choisissez pour la constante, et `valeur` est la valeur de la constante.

Il est également une bonne pratique d'utiliser des lettres majuscules pour le nom d'une constante.

Voyons un exemple de la façon de créer une constante en C :

```c
#include <stdio.h>

int main(void) {

    const int LUCKY_NUM = 7;

    printf("My lucky number is: %i\n", LUCKY_NUM);
}
```

Dans cet exemple, `LUCKY_NUM` est défini comme une constante avec une valeur de `7`.

Le nom de la constante, `LUCKY_NUM`, est en lettres majuscules, car c'est une bonne pratique et une convention qui améliore la lisibilité de votre code et distingue les constantes des variables.

Une fois défini, il ne peut pas être modifié dans le programme.

Si vous essayez de changer sa valeur, le compilateur C générera une erreur indiquant que vous tentez de modifier une constante.

```c
#include <stdio.h>

int main(void) {

    const int LUCKY_NUM = 7;

    printf("My lucky number is: %i\n", LUCKY_NUM);

    LUCKY_NUM = 13; // cela provoquera une erreur

}
```

## Chapitre 3 : Opérateurs

Les opérateurs sont des éléments essentiels dans tous les langages de programmation.

Ils vous permettent d'effectuer diverses opérations sur des variables et des valeurs en utilisant des symboles.

Et ils vous permettent de comparer des variables et des valeurs entre elles pour des calculs de prise de décision.

Dans ce chapitre, vous apprendrez les opérateurs les plus courants en programmation C.

Vous apprendrez d'abord les opérateurs arithmétiques, qui vous permettent d'effectuer des calculs mathématiques de base.

Vous apprendrez ensuite les opérateurs relationnels (également connus sous le nom d'opérateurs de comparaison), qui vous aident à comparer des valeurs.

Et vous apprendrez les opérateurs logiques, qui vous permettent de prendre des décisions en fonction de conditions.

Après avoir compris ces opérateurs fondamentaux, vous apprendrez quelques opérateurs supplémentaires, tels que les opérateurs d'affectation, et les opérateurs d'incrémentation et de décrémentation.

À la fin de ce chapitre, vous aurez une bonne compréhension de l'utilisation des différents opérateurs pour manipuler des données.

### Quels sont les opérateurs arithmétiques en C ?

Les opérateurs arithmétiques sont utilisés pour effectuer des opérations arithmétiques de base sur des types de données numériques.

Les opérations incluent l'addition, la soustraction, la multiplication, la division et le calcul du reste après division.

Ce sont les principaux opérateurs arithmétiques en C :

| Opérateur | Opération |
| --- | --- |
| + | Addition |
| \- | Soustraction |
| \* | Multiplication |
| / | Division |
| % | Reste après division (modulo) |

Regardons des exemples de chacun en action.

#### Comment utiliser l'opérateur d'addition (`+`)

L'opérateur d'addition additionne deux opérandes et retourne leur somme.

```c
#include <stdio.h>

int main(void) {

    int a = 5;

    int b = 3;

    int sum = a + b;

    printf("Sum: %i\n", sum); // Output: Sum: 8
}
```

#### Comment utiliser l'opérateur de soustraction (`-`)

L'opérateur de soustraction soustrait le deuxième opérande du premier opérande et retourne leur différence.

```c
#include <stdio.h>

int main(void) {

    int a = 10; 

    int b = 5;

    int difference = a - b;

    printf("Difference: %i\n", difference); // Output: Difference: 5
}
```

#### Comment utiliser l'opérateur de multiplication (`*`)

L'opérateur de multiplication multiplie deux opérandes et retourne leur produit.

```c
#include <stdio.h>

int main(void) {

    int a = 4;
    
    int b = 3;

    int product = a * b;

    printf("Product: %i\n", product); // Output: Product: 12
}
```

#### Comment utiliser l'opérateur de division (`/`)

L'opérateur de division divise le premier opérande par le deuxième opérande et retourne leur quotient.

```c
#include <stdio.h>

int main(void) {

    int a = 10;
    
    int b = 2;

    int quotient = a / b;

    printf("Quotient: %i\n", quotient); // Output: Quotient: 5
}
```

#### Comment utiliser l'opérateur modulo (`%`)

L'opérateur modulo retourne le reste du premier opérande lorsqu'il est divisé par le deuxième opérande.

```c
#include <stdio.h>

int main(void) {

    int a = 10;
    
    int b = 3;

    int remainder = a % b;

    printf("Remainder: %i\n", remainder); // Output: Remainder: 1
}
```

L'opérateur modulo est couramment utilisé pour déterminer si un entier est pair ou impair.

Si le reste de l'opération est `1`, alors l'entier est impair. Si le reste est nul, alors l'entier est pair.

### Quels sont les opérateurs relationnels en C ?

Les opérateurs relationnels sont utilisés pour comparer des valeurs et retourner un résultat.

Le résultat est une valeur booléenne. Une valeur booléenne est soit `true` (représentée par `1`) soit `false` (représentée par `0`).

Ces opérateurs sont couramment utilisés dans les instructions de prise de décision telles que les instructions `if` et les boucles `while`.

Ce sont les opérateurs relationnels en C :

| Opérateur | Nom de l'opérateur |
| --- | --- |
| \== | Égal à |
| != | Différent de |
| \&gt; | Supérieur à |
| &lt; | Inférieur à |
| \&gt;= | Supérieur ou égal à |
| &lt;= | Inférieur ou égal à |

Regardons un exemple de chacun en action.

#### Comment utiliser l'opérateur égal à (`==`)

L'opérateur égal à vérifie si deux valeurs sont égales.

Il pose essentiellement la question, "Ces deux valeurs sont-elles égales ?"

Notez que vous utilisez l'opérateur de comparaison (deux signes égaux – `==`) et non l'opérateur d'assignation (`=`) qui est utilisé pour assigner une valeur à une variable.

```c
#include <stdio.h>

int main(void) {

    int a = 5;

    int b = 5;
    
    int result = (a == b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

Le résultat est `1` (vrai), car `a` et `b` sont égaux.

#### Comment utiliser l'opérateur différent de (`!=`)

L'opérateur différent de vérifie si deux valeurs ne sont PAS égales.

```c
#include <stdio.h>

int main(void) {

    int a = 5; 

    int b = 3;

    int result = (a != b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

Le résultat est `1` (vrai), car `a` et `b` ne sont pas égaux.

#### Comment utiliser l'opérateur supérieur à (`>`)

Cet opérateur compare deux valeurs pour vérifier si l'une est supérieure à l'autre.

```c
#include <stdio.h>

int main(void) {

    int a = 10;

    int  b = 5;

    int result = (a > b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

Le résultat est `1` (vrai), car `a` est supérieur à `b`.

#### Comment utiliser l'opérateur inférieur à (`<`)

Cet opérateur compare deux valeurs pour vérifier si l'une est inférieure à l'autre.

```c
#include <stdio.h>

int main(void) {

    int a = 10;

    int b = 5;

    int result = (a < b);

    printf("Result: %i\n", result); // Output: Result: 0
}
```

Le résultat est `0` (faux), car `a` n'est pas inférieur à `b`.

#### Comment utiliser l'opérateur supérieur ou égal à (`>=`)

Cet opérateur compare deux valeurs pour vérifier si l'une est supérieure ou égale à l'autre.

```c
#include <stdio.h>

int main(void) {

    int a = 5;
    
    int  b = 5;

    int result = (a >= b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

Le résultat est `1` (vrai), car `a` est égal à `b`.

#### Comment utiliser l'opérateur inférieur ou égal à (`<=`)

Cet opérateur compare deux valeurs pour vérifier si l'une est inférieure ou égale à l'autre.

```c
#include <stdio.h>

int main(void) {

    int a = 1;

    int b = 5;

    int result = (a <= b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

Le résultat est `1` (vrai), car `a` est inférieur à `b`.

### Opérateurs logiques

Les opérateurs logiques opèrent sur des valeurs booléennes et retournent une valeur booléenne.

Voici les opérateurs logiques utilisés en C :

| Opérateur | Nom de l'opérateur |
| --- | --- |
| `&&` | ET logique |
| \` |  |
| `!` | NON logique |

Examinons plus en détail chacun d'eux dans les sections suivantes.

#### Comment utiliser l'opérateur ET (`&&`)

L'opérateur logique ET (`&&`) vérifie si tous les opérandes sont `true`.

Le résultat est `true` uniquement lorsque tous les opérandes sont `true`.

Voici la table de vérité pour l'opérateur ET (`&&`) lorsque vous travaillez avec deux opérandes :

| PREMIER OPÉRANDE | DEUXIÈME OPÉRANDE | RÉSULTAT |
| --- | --- | --- |
| vrai | vrai | vrai |
| vrai | faux | faux |
| faux | vrai | faux |
| faux | faux | faux |

Prenons l'exemple suivant :

Le résultat de `(10 == 10) && (20 == 20)` est `true` car les deux opérandes sont `true`.

Regardons un autre exemple :

Le résultat de `(10 == 20) && (20 == 20)` est `false` car l'un des opérandes est `false`.

Lorsque le premier opérande est `false`, le deuxième opérande n'est pas évalué (puisqu'il n'y a pas de point - il est déjà déterminé que le premier opérande est faux, donc le résultat ne peut être que `false`).

#### Comment utiliser l'opérateur OU (`||`)

L'opérateur logique OU (`||`) vérifie si au moins l'un des opérandes est `true`.

Le résultat est `true` uniquement lorsque au moins l'un des opérandes est `true`.

Voici la table de vérité pour l'opérateur OU (`||`) lorsque vous travaillez avec deux opérandes :

| PREMIER OPÉRANDE | DEUXIÈME OPÉRANDE | RÉSULTAT |
| --- | --- | --- |
| vrai | vrai | vrai |
| vrai | faux | vrai |
| faux | vrai | vrai |
| faux | faux | faux |

Regardons un exemple :

Le résultat de `(10 == 20) || (20 == 20)` est `true` car l'un des opérandes est `true`.

Regardons un autre exemple :

Le résultat de `(20 == 20) || (10 == 20)` est `true` car l'un des opérandes est `true`

Si le premier opérande est `true`, alors le deuxième opérateur n'est pas évalué.

### Comment utiliser l'opérateur NON (`!`)

L'opérateur logique NON (`!`) nie l'opérande.

Si l'opérande est `true`, il retourne `false`.

Et si c'est `false`, il retourne `true`.

Vous pouvez vouloir utiliser l'opérateur NON lorsque vous souhaitez inverser la valeur d'une condition et retourner l'opposé de ce que la condition évalue.

Voici la table de vérité pour l'opérateur NON (`!`) :

| OPÉRANDE | RÉSULTAT |
| --- | --- |
| vrai | faux |
| faux | vrai |

Regardons un exemple :

Le résultat de `!(10 == 10)` est `false`.

La condition `10 == 10` est `true`, mais l'opérateur `!` la nie donc le résultat est `false`.

Et regardons un autre exemple :

Le résultat de `!(10 == 20)` est `true`.

La condition `10 == 20` est fausse, mais l'opérateur `!` la nie.

### Qu'est-ce que l'opérateur d'affectation en C ?

L'opérateur d'affectation est utilisé pour affecter une valeur à une variable.

```c
#include <stdio.h>

int main(void) {

    // déclarer une variable entière nommée num
    int num;
		
    // affecter la valeur 10 à num
    num = 10;

    printf("num: %i\n", num); // Output: num: 10

}
```

Dans l'exemple ci-dessus, la valeur `10` est affectée à la variable `num` en utilisant l'opérateur d'affectation.

L'opérateur d'affectation fonctionne en évaluant l'expression du côté droit puis en stockant son résultat dans la variable du côté gauche.

Le type de données affecté doit correspondre au type de données de la variable.

#### Comment utiliser les opérateurs d'affectation composés

Les opérateurs d'affectation composés sont des notations abrégées.

Ils vous permettent de modifier une variable en effectuant une opération sur celle-ci puis en stockant le résultat de l'opération dans la même variable en une seule étape.

Cela peut rendre votre code plus concis et plus facile à lire.

Certains opérateurs d'affectation composés courants en C incluent :

* `+=`: Addition et affectation
    
* `=`: Soustraction et affectation
    
* `=`: Multiplication et affectation
    
* `/=`: Division et affectation
    
* `%=`: Modulo et affectation
    

Regardons un exemple de la façon dont l'opérateur `+=` fonctionne :

```c
#include <stdio.h>

int main(void) {

  int num = 10;

  num += 5; 
 
  printf("Num: %i\n", num); // Num: 15
}
```

Dans l'exemple ci-dessus, j'ai créé une variable nommée `num` et je lui ai assigné une valeur initiale de `10`.

J'ai ensuite voulu incrémenter la variable de `5`. Pour ce faire, j'ai utilisé l'opérateur composé `+=`.

La ligne `num += 5` incrémente la valeur de `num` de 5, et le résultat (15) est stocké dans `num` en une seule étape.

Notez que la ligne `num += 5;` fonctionne exactement de la même manière que `num = num + 5`, ce qui signifierait `num = 10 + 5`, mais avec moins de lignes de code.

### Quels sont les opérateurs d'incrémentation et de décrémentation en C ?

Les opérateurs d'incrémentation `++` et de décrémentation `--` incrémentent et décrémentent une variable de un, respectivement.

Regardons un exemple de la façon d'utiliser l'opérateur `++` :

```c
#include <stdio.h>

int main(void) {
  
  int num = 10;
  num++;

  printf("Num: %i\n", num); // Num: 11

}
```

La valeur initiale de la variable `num` est `10`.

En utilisant l'opérateur d'incrémentation `++`, la valeur de `num` est définie à `11`.

C'est comme effectuer `num = num + 1` mais avec moins de code.

Le raccourci pour décrémenter une variable de un est `--`.

Si vous souhaitiez décrémenter `num` de un, vous feriez ce qui suit :

```c
#include <stdio.h>

int main(void) {
  
  int num = 10;
  num--;

  printf("Num: %i\n", num); // Num: 9

}
```

La valeur initiale de la variable `num` est `10`.

En utilisant l'opérateur de décrémentation `--`, la valeur de `num` est maintenant définie à `9`.  
C'est comme effectuer `num = num - 1`.

## Chapitre 4 : Instructions conditionnelles

Les exemples que vous avez vus jusqu'à présent s'exécutent tous ligne par ligne, de haut en bas.

Ils ne sont pas flexibles et dynamiques et ne s'adaptent pas en fonction du comportement de l'utilisateur ou de situations spécifiques.

Dans ce chapitre, vous apprendrez à prendre des décisions et à contrôler le flux d'un programme.

Vous définissez les règles sur ce qui se passe ensuite dans vos programmes en établissant des conditions à l'aide d'instructions conditionnelles.

Les instructions conditionnelles effectuent une action spécifique en fonction du résultat d'une comparaison qui a lieu.

Le programme décidera des prochaines étapes en fonction de la satisfaction ou non des conditions.

Certaines parties du programme peuvent ne pas s'exécuter en fonction des résultats ou de certaines entrées de l'utilisateur. L'utilisateur peut emprunter différents chemins en fonction des diverses bifurcations qui se présentent pendant la vie d'un programme.

Tout d'abord, vous apprendrez l'instruction `if` – le bloc de construction fondamental de la prise de décision en C.

Vous apprendrez également les instructions `else if` et `else` qui sont ajoutées à l'instruction `if` pour fournir une flexibilité supplémentaire au programme.

Vous apprendrez ensuite l'opérateur ternaire qui vous permet de condenser la logique de prise de décision en une seule ligne de code et d'améliorer la lisibilité de votre programme.

### Comment créer une instruction `if` en C

L'instruction conditionnelle la plus basique en C est l'instruction `if`.

Elle prend une décision basée sur une condition.

Si la condition donnée évalue à `true`, alors le code à l'intérieur du bloc `if` est exécuté.

Si la condition donnée évalue à `false`, le code à l'intérieur du bloc `if` est ignoré et sauté.

La syntaxe générale pour une instruction `if` en C est la suivante :

```c
if (condition) {
  // exécuter ce code si la condition est vraie
}
```

Regardons un exemple :

```c
#include <stdio.h>

int main(void) {

    // variable age
   int age;

   // demander à l'utilisateur d'entrer son âge
   printf("Please enter your age: ");

   // stocker la réponse de l'utilisateur dans la variable
   scanf("%i", &age);

    // vérifier si l'âge est inférieur à 18
    // si c'est le cas, alors et seulement alors, imprimer un message sur la console

   if (age < 18) {
       printf("You need to be over 18 years old to continue\\n");
   }
}
```

Dans le code ci-dessus, j'ai créé une variable nommée `age` qui contient une valeur entière.

J'ai ensuite demandé à l'utilisateur d'entrer son âge et j'ai stocké la réponse dans la variable `age`.

Ensuite, j'ai créé une condition qui vérifie si la valeur contenue dans la variable `age` est inférieure à 18.

Si c'est le cas, je veux qu'un message soit imprimé sur la console pour informer l'utilisateur que pour continuer, l'utilisateur doit avoir au moins 18 ans.

Lorsque l'on me demande mon âge et que j'entre `16`, j'obtiens la sortie suivante :

```plaintext
#output

Please enter your age: 16
You need to be over 18 years old to continue
```

La condition (`age < 18`) évalue à `true` donc le code dans le bloc `if` s'exécute.

Ensuite, je recompile et réexécute le programme.

Cette fois, lorsque l'on me demande mon âge, disons que j'entre `28`, mais je n'obtiens aucune sortie :

```plaintext
#output

Please enter your age: 28
```

C'est parce que la condition évalue à `false` et donc le corps du bloc `if` est ignoré.

Je n'ai également pas spécifié ce qui devrait se passer dans le cas où l'âge de l'utilisateur est supérieur à 18.

Pour spécifier ce qui se passe si l'âge de l'utilisateur est supérieur à 18, je peux utiliser une instruction `if else`.

### Comment créer une instruction `if else` en C

Vous pouvez ajouter une clause `else` à une instruction `if` pour fournir un code qui s'exécutera uniquement lorsque l'instruction `if` évalue à `false`.

L'instruction `if else` signifie essentiellement que "`si` cette condition est vraie, faites ce qui suit, `sinon` faites cela à la place".

Si la condition à l'intérieur des parenthèses évalue à `true`, le code à l'intérieur du bloc `if` s'exécutera.

Mais si cette condition évalue à `false`, le code à l'intérieur du bloc `else` s'exécutera.

Le mot-clé `else` est la solution lorsque la condition `if` est fausse et que le code à l'intérieur du bloc `if` ne s'exécute pas. Il fournit une alternative.

La syntaxe générale ressemble à ceci :

```c
if (condition) {
  // exécuter ce code si la condition est vraie
} else {
  // si la condition ci-dessus est fausse, exécuter ce code
}
```

Maintenant, revisitons l'exemple de la section précédente, et spécifions ce qui devrait se passer si l'âge de l'utilisateur est supérieur à 18 :

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

 
    // si la condition entre parenthèses est vraie, le code à l'intérieur des accolades s'exécutera
    // sinon, il est ignoré
    // et le code dans le bloc else s'exécutera
    
   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   } else {
      printf("You are over 18 so you can continue \n");
  }
  
   }
```

Si la condition est `true`, le code dans le bloc `if` s'exécute :

```plaintext
#output

Please enter your age: 14
You need to be over 18 years old to continue
```

Si la condition est `false`, le code dans le bloc `if` est ignoré et le code dans le bloc `else` s'exécute à la place :

```plaintext
#output

Please enter your age: 45
You are over 18 so you can continue
```

### Comment créer une instruction `else if` en C

Mais que se passe-t-il lorsque vous souhaitez avoir plus d'une condition parmi lesquelles choisir ?

Si vous souhaitez choisir parmi plus d'une option, vous pouvez introduire une instruction `else if`.

Une instruction `else if` signifie essentiellement que "Si cette condition est vraie, faites ce qui suit. Si ce n'est pas le cas, faites cela à la place. Cependant, si aucune des conditions ci-dessus n'est vraie et que tout le reste échoue, faites enfin cela."

La syntaxe générale ressemble à quelque chose comme ce qui suit :

```plaintext
if (condition) {
   // si la condition est vraie, exécutez ce code
} else if(another_condition) {
   // si la condition ci-dessus était fausse et que cette condition est vraie,
   // exécutez le code dans ce bloc
} else {
   // si les deux conditions ci-dessus sont fausses, exécutez ce code
}
```

Voyons comment fonctionne une instruction `else if`.

Supposons que vous ayez l'exemple suivant :

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }  else if (age < 21) {
       printf("You need to be over 21\n");
   } else {
      printf("You are over 18 and older than 21 so you can continue \n");
  }
  
   }
```

Si la première instruction `if` est vraie, le reste du bloc ne s'exécutera pas :

```plaintext
#output

Please enter your age: 17
You need to be over 18 years old to continue
```

Si la première instruction `if` est fausse, alors le programme passe à la condition suivante.

Si celle-ci est vraie, le code à l'intérieur du bloc `else if` s'exécute et le reste du bloc ne s'exécute pas :

```plaintext
#output

Please enter your age: 20
You are need to be over 21
```

Si les deux conditions précédentes sont toutes fausses, alors le dernier recours est le bloc `else` qui est celui à exécuter :

```plaintext
#output

Please enter your age: 22
You are over 18 and older than 21 so you can continue
```

### Comment utiliser l'opérateur ternaire en C

L'opérateur ternaire (également connu sous le nom d'opérateur conditionnel) vous permet d'écrire une instruction `if else` avec moins de lignes de code.

Il peut fournir un moyen d'écrire un code plus lisible et concis et s'avère utile lors de l'écriture d'expressions conditionnelles simples.

Vous pourriez vouloir l'utiliser lorsque vous prenez des décisions simples et souhaitez garder votre code concis et sur une seule ligne.

Cependant, il est préférable de s'en tenir à une instruction `if-else` régulière lorsque vous traitez des décisions plus complexes, car l'opérateur ternaire pourrait rendre votre code difficile à lire.

La syntaxe générale de l'opérateur ternaire ressemble à quelque chose de similaire à ce qui suit :

```plaintext
condition ? expression_si_vrai : expression_si_faux;
```

Décomposons cela :

* `condition` est la condition que vous souhaitez évaluer. Cette condition évaluera soit `true` soit `false`
    
* `?` sépare la condition des deux expressions possibles
    
* `expression_si_vrai` est exécutée si la `condition` évalue à `true`
    
* `:` sépare l'`expression_si_vrai` de l'`expression_si_faux`
    
* `expression_si_faux` est exécutée si la `condition` évalue à `false`.
    

Regardons un exemple :

```c
#include <stdio.h>

int main(void) {
  
    int x = 10;
    
    int y = (x > 5) ? 100 : 200;
    
    printf("x: %i\n", x); // x: 10
    
    printf("y: %i\n", y);  // y: 100
   }
```

Dans l'exemple ci-dessus, la condition est `(x > 5)`.

Si `x` est supérieur à 5, la condition évalue à `true`. Et lorsque la condition est `true`, la valeur assignée à `y` sera `100`.

Si la condition évalue à `false`, la valeur assignée à `y` sera `200`.

Ainsi, puisque `x` est supérieur à 5 (`x = 10`), `y` se voit assigner la valeur `100`.

## Chapitre 5 : Boucles

Dans ce chapitre, vous apprendrez les boucles, qui sont essentielles pour automatiser les tâches répétitives sans avoir à écrire le même code plusieurs fois.

Les boucles vous permettent d'exécuter un bloc spécifique d'instructions de code de manière répétée encore et encore jusqu'à ce qu'une certaine condition soit remplie.

Vous apprendrez les différents types de boucles, telles que les boucles `for`, `while` et `do-while`, et comprendrez leur syntaxe et quand vous devez utiliser chacune d'elles.

Vous apprendrez également l'instruction `break`, qui vous permet de contrôler le flux d'exécution au sein des boucles de manière spécifique.

### Comment créer une boucle `for` en C

Une boucle `for` vous permet d'exécuter un bloc de code de manière répétée en fonction d'une condition spécifiée.

Elle est utile lorsque vous savez combien de fois vous souhaitez répéter une certaine action.

La syntaxe générale d'une boucle `for` ressemble à ceci :

```plaintext
for (initialisation; condition; incrément/décrément) {
    // Code à exécuter à chaque itération
}
```

Décomposons cela :

* `initialisation` est l'étape où vous initialisez une variable de contrôle de boucle. Elle est généralement utilisée pour définir le point de départ de votre boucle.
    
* `condition` est la condition qui est évaluée avant chaque itération. Si la condition est `true`, la boucle continue. Si elle est `false`, la boucle se termine. La boucle s'exécutera tant que la condition reste vraie.
    
* `incrément/décrément` est la partie responsable de la modification de la variable de contrôle de boucle après chaque itération. Il peut s'agir d'un incrément (`++`), d'un décrément (`--`), ou de toute autre modification.
    
* `Code à exécuter à chaque itération` est le bloc de code à l'intérieur du corps de la boucle `for` qui est exécuté à chaque itération si la condition est `true`.
    

Regardons un exemple de fonctionnement d'une boucle `for`.

Supposons que vous souhaitiez imprimer les nombres de 1 à 5 sur la console :

```c
#include <stdio.h>

int main() {

    for (int i = 1; i <= 5; i++) {
        printf("Iteration %i\n", i);
    }
    
}
```

Sortie :

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

Dans l'exemple ci-dessus, j'ai d'abord initialisé la variable de contrôle de boucle `i` avec une valeur de `1`.

La condition `i <= 5` est vraie, donc le corps de la boucle est exécuté et `"Iteration 1"` est imprimé.

Après chaque itération, la valeur de `i` est incrémentée de `1`. Ainsi, `i` est incrémenté à `2`.

La condition est toujours `true`, donc `"Iteration 2"` est imprimé.

La boucle continuera tant que `i` est inférieur ou égal à `5`.

Lorsque `i` devient `6`, la condition évalue à `false` et la boucle se termine.

### Comment créer une boucle `while` en C

Comme vous l'avez vu dans la section précédente, une boucle `for` est utilisée lorsque vous connaissez le nombre exact d'itérations que vous souhaitez que la boucle effectue.

La boucle `while` est utile lorsque vous souhaitez répéter une action en fonction d'une condition mais que vous ne connaissez pas le nombre exact d'itérations à l'avance.

Voici la syntaxe générale d'une boucle `while` :

```plaintext
while (condition) {
    // Code à exécuter à chaque itération
}
```

Avec une boucle `while`, la condition est évaluée avant chaque itération. Si la condition est `true`, la boucle continue. Si elle est `false`, la boucle se termine.

La boucle `while` continuera tant que la condition évalue à `true`.

Une chose à noter avec les boucles `while` est que le code dans le corps de la boucle n'est pas garanti de s'exécuter même au moins une fois si une condition n'est pas remplie.

Regardons un exemple de fonctionnement d'une boucle `while` :

```c
#include <stdio.h>

int main() {

    int count = 1;
    
    while (count <= 5) {
    
        printf("Iteration %i\n", count);
        
        count++;
    }
    
}
```

Sortie :

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

Dans l'exemple ci-dessus, j'ai d'abord initialisé une variable `count` avec une valeur de `1`.

Avant d'exécuter un code, la boucle `while` vérifie une condition.

La condition `count <= 5` est `true` car count est initialement `1`. Ainsi, le corps de la boucle est exécuté et `"Iteration 1"` est imprimé.

Ensuite, `count` est incrémenté à `2`.

La condition est toujours `true`, donc `"Iteration 2"` est imprimé.

La boucle continuera tant que count est inférieur ou égal à 5.

Ce processus continue jusqu'à ce que count devienne `6`, moment auquel la condition devient `false`, et la boucle se termine.

Une chose à laquelle il faut faire attention lors de l'utilisation des boucles `while` est de créer accidentellement une boucle infinie :

```c
#include <stdio.h> 

int main(void)
{

	while(true)
	{
		printf("Hello world");
	}
}
```

Dans ce cas, la condition évalue toujours à `true`.

Après avoir imprimé la ligne de code à l'intérieur des accolades, elle vérifie en continu si elle doit exécuter le code à nouveau.

Comme la réponse est toujours oui (puisque la condition à vérifier est toujours vraie à chaque fois), elle exécute le code encore et encore.

Le moyen d'arrêter le programme et de sortir de la boucle sans fin est d'exécuter `Ctrl C` dans le terminal.

### Comment créer une boucle `do-while` en C

Comme mentionné dans la section précédente, le code dans le corps de la boucle `while` n'est pas garanti de s'exécuter même au moins une fois si la condition n'est pas remplie.

Une boucle `do-while` exécute un bloc de code de manière répétée tant qu'une condition reste `true`.

Cependant, contrairement à une boucle `while`, elle est garantie de s'exécuter au moins une fois, indépendamment du fait que la condition soit `true` ou `false` dès le début.

Ainsi, la boucle `do-while` est utile lorsque vous souhaitez vous assurer que le corps de la boucle est exécuté au moins une fois avant que la condition ne soit vérifiée.

La syntaxe générale d'une boucle `do-while` ressemble à ceci :

```plaintext
do {
    // Code à exécuter à chaque itération
} while (condition);
```

Regardons un exemple qui démontre comment fonctionne une boucle `do-while` :

```c
#include <stdio.h>

int main() {

    int count = 1;
    
    do {
        printf("Iteration %i\n", count);
        
        count++;
        
    } while (count <= 5);

}
```

Sortie :

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

Dans l'exemple ci-dessus, j'initialise une variable `count` avec une valeur de `1`.

Une boucle `do-while` fait d'abord quelque chose puis vérifie une condition.

Ainsi, le bloc de code à l'intérieur de la boucle est exécuté au moins une fois.

La chaîne `"Iteration 1"` est imprimée puis `count` est incrémenté à `2`.

La condition `count <= 5` est ensuite vérifiée et elle évalue à `true`, donc la boucle continue.

La boucle continuera tant que `count` est inférieur ou égal à 5.

Après l'itération où `count` est `6`, la condition devient `false`, et la boucle se termine.

### Comment utiliser l'instruction `break` en C

L'instruction `break` est utilisée pour sortir immédiatement d'une boucle et terminer son exécution.

C'est une instruction de contrôle de flux qui vous permet d'interrompre l'exécution normale de la boucle et de passer au code après la boucle.

L'instruction `break` est particulièrement utile lorsque vous souhaitez sortir d'une boucle dans des conditions spécifiques, même si la condition de terminaison de la boucle n'a pas été remplie.

Vous pourriez l'utiliser lorsque vous rencontrez une certaine valeur, ou lorsqu'une condition spécifique est remplie.

Voici comment utiliser une instruction `break` dans une boucle :

```c
#include <stdio.h>

int main() {
    int target = 5;
    
    for (int i = 1; i <= 10; i++) {
        printf("Current value: %i\n", i);
        
        if (i == target) {
            printf("Target value reached. Exiting loop.\n");
            break; // Sortir de la boucle
        }
    }
    
}
```

Sortie :

```plaintext
Current value: 1
Current value: 2
Current value: 3
Current value: 4
Current value: 5
Target value reached. Exiting loop.
```

Dans l'exemple ci-dessus, une boucle `for` est définie pour itérer de `1` à `10`.

À l'intérieur de la boucle, la valeur actuelle de `i` est imprimée à chaque itération.

Il y a également une instruction `if` qui vérifie si la valeur actuelle de `i` correspond à la valeur cible, qui est définie à `5`.

Si `i` correspond à la valeur cible, l'instruction `if` est déclenchée et un message est imprimé.

En conséquence, l'instruction `break` sort de la boucle actuelle immédiatement et prématurément.

Le programme continuera à exécuter le code qui se trouve après la boucle.

## Chapitre 6 : Tableaux

Les tableaux offrent une manière polyvalente et organisée de stocker plusieurs éléments de données apparentées qui sont disposés dans une séquence ordonnée.

Ils vous permettent de stocker plusieurs valeurs du même type de données sous un seul identifiant et d'effectuer des tâches répétitives sur chaque élément.

Dans ce chapitre, vous apprendrez à déclarer et initialiser des tableaux. Vous apprendrez également à accéder aux éléments individuels d'un tableau en utilisant la notation d'index et à les modifier.

De plus, vous apprendrez à utiliser des boucles pour parcourir les éléments d'un tableau et effectuer des opérations sur chaque élément.

### Comment déclarer et initialiser un tableau en C

Pour déclarer un tableau en C, vous spécifiez d'abord le type de données des éléments que le tableau stockera.

Cela signifie que vous pouvez créer des tableaux de type `int`, `float`, `char`, et ainsi de suite.

Vous spécifiez ensuite le nom du tableau, suivi de la taille du tableau entre crochets.

La taille du tableau est le nombre d'éléments qu'il peut contenir. Ce nombre doit être un entier positif.

Gardez à l'esprit que les tableaux ont une taille fixe, et une fois déclarés, vous ne pouvez pas la modifier par la suite.

Voici la syntaxe générale pour déclarer un tableau :

```c
type_de_donnees nom_tableau[taille_tableau];
```

Voici comment déclarer un tableau d'entiers :

```c
#include <stdio.h>

int main() {

   int grades[5];
}
```

Dans l'exemple ci-dessus, j'ai créé un tableau nommé `grades` qui peut stocker `5` nombres `int`.

Après avoir déclaré un tableau, vous pouvez l'initialiser avec des valeurs initiales.

Pour ce faire, utilisez l'opérateur d'assignation, `=`, suivi d'accolades, `{}`.

Les accolades contiendront les valeurs, et chaque valeur doit être séparée par une virgule.

Voici comment initialiser le tableau `grades` :

```c
#include <stdio.h>

int main() {

   int grades[5] = {50, 75, 100, 67, 90};
}
```

Gardez à l'esprit que le nombre de valeurs doit correspondre à la taille du tableau, sinon vous rencontrerez des erreurs.

Une chose à noter ici est que vous pouvez également initialiser partiellement le tableau :

```c
#include <stdio.h>

int main() {

   int grades[5] = {50, 75, 100};
}
```

Dans ce cas, les deux éléments restants seront définis à `0`.

Une autre façon d'initialiser les tableaux est d'omettre la longueur du tableau à l'intérieur des crochets et de n'assigner que les valeurs initiales, comme ceci :

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
}
```

Dans cet exemple, la taille du tableau est `5` car je lui ai assigné `5` valeurs.

#### Comment trouver la longueur d'un tableau en C en utilisant l'opérateur `sizeof()`

L'opérateur `sizeof` est utile lorsque vous devez calculer la taille d'un tableau.

Regardons un exemple de l'opérateur `sizeof` en action :

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};

    // calculer la taille du tableau
    int array_size = sizeof(grades);

    printf("Size of array: %i bytes\n", array_size);
}
```

Sortie :

```plaintext
Size of array: 20 bytes
```

Dans l'exemple ci-dessus, `sizeof(grades)` calcule la taille totale du tableau en octets.

Dans ce cas, le tableau contient cinq entiers.

Comme mentionné dans un chapitre précédent, sur la plupart des systèmes modernes, un `int` occupe généralement 4 octets de mémoire. Par conséquent, la taille totale est de `5 x 4 = 20` octets de mémoire pour l'ensemble du tableau.

Voici comment vous pouvez vérifier combien de mémoire chaque `int` occupe en utilisant l'opérateur `sizeof` :

```c
#include <stdio.h>

int main() {
    
    int grades[] = {50, 75, 100, 67, 90};
    
    // calculer la taille d'un seul élément du tableau
    int element_size = sizeof(grades[0]);
    
    printf("Size of a single element: %i bytes\n", element_size);

}
```

Sortie :

```plaintext
Size of a single element: 4 bytes
```

Le `sizeof(grades[0])` calcule la taille d'un seul élément en octets.

En divisant la taille totale du tableau par la taille d'un seul élément, vous pouvez calculer le nombre d'éléments dans le tableau, ce qui est égal à la longueur du tableau :

```c
#include <stdio.h>

int main() {
    
    int grades[] = {50, 75, 100, 67, 90};
    
     int array_size = sizeof(grades);
     
     int element_size = sizeof(grades[0]);
    
     // calculer la longueur du tableau
     int length = array_size / element_size;

    printf("Length of the array: %i elements\n", length);

}
```

Sortie :

```plaintext
Length of the array: 5 elements
```

### Comment accéder aux éléments d'un tableau en C

Vous pouvez accéder à chaque élément d'un tableau en spécifiant son index ou sa position dans le tableau.

Notez qu'en C, l'indexation commence à `0` au lieu de `1`.

Ainsi, l'index du premier élément est `0`, l'index du deuxième élément est `1`, et ainsi de suite.

Le dernier élément d'un tableau a un index de `taille_tableau - 1`.

Pour accéder aux éléments individuels du tableau, vous spécifiez le nom du tableau suivi du numéro d'index de l'élément entre crochets (`[]`).

```plaintext
nom_tableau[index];
```

Regardons l'exemple suivant :

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};

   // Accéder à chaque élément du tableau en utilisant la notation d'index
    
   printf("Element at index 0: %i\n", grades[0]);  
    
   printf("Element at index 1: %i\n", grades[1]);  

   printf("Element at index 2: %i\n", grades[2]); 

   printf("Element at index 3: %i\n", grades[3]); 
    
   printf("Element at index 4: %i\n", grades[4]); 
}
```

Sortie :

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

Dans l'exemple ci-dessus, pour accéder à chaque élément du tableau d'entiers `grades`, je dois spécifier le nom du tableau ainsi que la position de l'élément dans le tableau entre crochets.

Rappelez-vous que l'index commence à `0`, donc `grades[0]` vous donne le premier élément, `grades[1]` vous donne le deuxième élément, et ainsi de suite.

Notez que si vous essayez d'accéder à un élément avec un numéro d'index supérieur à `taille_tableau - 1`, le compilateur retournera un nombre aléatoire :

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};

    
    printf("Element at index 5: %d\n", grades[5]);  

}
```

Sortie :

```plaintext
Element at index 5: 220312136
```

### Comment modifier les éléments d'un tableau en C

Une fois que vous savez comment accéder aux éléments d'un tableau, vous pouvez ensuite les modifier.

La syntaxe générale pour modifier un élément de tableau ressemble à ceci :

```plaintext
nom_tableau[index] = nouvelle_valeur;
```

Vous pouvez changer la valeur d'un élément en lui assignant une nouvelle valeur en utilisant son index.

Prenons le tableau `grades` de plus tôt :

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
}
```

Voici comment vous changeriez la valeur `75` en `85` :

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
   
   grades[1] = 85; // changement de la valeur à l'index 1 en 85
   
   printf("Element at index 1: %i\n", grades[1]); 
}
```

Sortie :

```plaintext
Element at index 1: 85
```

Lors de la modification des tableaux, gardez à l'esprit que la nouvelle valeur doit correspondre au type de données déclaré du tableau.

### Comment parcourir un tableau en C

En parcourant un tableau, vous pouvez accéder et effectuer des opérations sur chaque élément séquentiellement.

La boucle `for` est couramment utilisée pour parcourir les tableaux.

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    for (int i = 0; i < 5; i++) {
        printf("Element at index %i: %i\n", i, grades[i]);
    }
}
```

Sortie :

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

Lorsque vous utilisez une boucle `for` pour parcourir un tableau, vous devez spécifier l'index comme variable de boucle, puis utiliser l'index pour accéder à chaque élément du tableau.

Les espaces réservés `%i` sont remplacés par l'index actuel `i` et la valeur à cet index dans le tableau des notes, respectivement.

Vous pouvez également utiliser une boucle `while` pour parcourir un tableau :

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    int i = 0;
    
    while (i < 5) {
    
        printf("Element at index %i: %i\n", i, grades[i]);
        i++;
    }
}
```

Sortie :

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

Lorsque vous utilisez une boucle `while` pour parcourir un tableau, vous aurez besoin d'une variable d'index, `int i = 0`, pour suivre la position actuelle dans le tableau.

La boucle vérifie la condition `(i < 5)` et imprime l'index de la note ainsi que la valeur réelle de la note.

Après que chaque note est affichée, la variable `i` est augmentée de un, et la boucle continue jusqu'à ce qu'elle ait affiché toutes les notes de la liste.

Une boucle `do-while` fonctionne de manière similaire à la boucle `while`, mais elle est utile lorsque vous souhaitez vous assurer que le corps de la boucle est exécuté au moins une fois avant de vérifier la condition :

```c
#include <stdio.h>

int main() {

     int grades[] = {50, 75, 100, 67, 90};

    int i = 0;
    
    do {
        printf("Element at index %i: %i\n", i, grades[i]);
        
        i++;
    } while (i < 5);
}
```

Vous pouvez également utiliser l'opérateur `sizeof` pour parcourir un tableau.

Cette méthode est particulièrement utile pour vous assurer que votre boucle ne dépasse pas la longueur du tableau :

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    int length = sizeof(grades) / sizeof(grades[0]);

    for (int i = 0; i < length; i++) {
        printf("Element at index %i: %i\n", i, grades[i]);
    }

}
```

La ligne `int length = sizeof(grades) / sizeof(grades[0]);` calcule la longueur du tableau `grades`.

La longueur est calculée en divisant la taille totale (en octets) du tableau par la taille d'un seul élément `grades[0]`. Le résultat est stocké dans la variable `length`.

La boucle parcourt ensuite le tableau en utilisant cette valeur `length`.

Pour chaque itération, elle imprime l'index `i` et la valeur de la note à cet index `grades[i]`.

## Chapitre 7 : Chaînes de caractères

Dans le chapitre précédent, vous avez appris les bases des tableaux en C.

Maintenant, il est temps d'apprendre les chaînes de caractères – un type spécial de tableau.

Les chaînes de caractères sont partout en programmation. Elles sont utilisées pour représenter des noms, des messages, des mots de passe, et plus encore.

Dans ce chapitre, vous apprendrez les chaînes de caractères en C et comment elles sont stockées sous forme de tableaux de caractères.

Vous apprendrez également les bases de la manipulation de chaînes de caractères.

Plus précisément, vous apprendrez à trouver la longueur d'une chaîne de caractères et à copier, concaténer et comparer des chaînes de caractères en C.

### Qu'est-ce que les chaînes de caractères en C ?

Une chaîne de caractères est une séquence de caractères, comme des lettres, des chiffres ou des symboles, qui sont utilisés pour représenter du texte.

En C, les chaînes de caractères sont en fait des tableaux de caractères. Et chaque caractère de la chaîne a une position spécifique dans le tableau.

Une autre caractéristique unique des chaînes de caractères en C est qu'à la fin de chacune d'elles, il y a un caractère caché `\0` appelé le 'terminateur nul'.

Ce terminateur permet à l'ordinateur de savoir où la chaîne se termine.

Ainsi, la chaîne '`Hello`' en C est stockée comme '`Hello\0`' en mémoire.

### Comment créer des chaînes de caractères en C

Une façon de créer une chaîne de caractères en C est d'initialiser un tableau de caractères.

Le tableau contiendra les caractères qui composent la chaîne.

Voici comment vous initialiseriez un tableau pour créer la chaîne 'Hello' :

```c
#include <stdio.h>

int main() {
  char word[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

}
```

Remarquez comment j'ai spécifié que le tableau doit stocker `6` caractères malgré le fait que `Hello` ne fasse que `5` caractères de long. Cela est dû à l'opérateur nul.

Assurez-vous d'inclure le terminateur nul, `\0`, comme dernier caractère pour signifier la fin de la chaîne.

Regardons comment vous créeriez la chaîne 'Hello world' :

```c
#include <stdio.h>

int main() {
  char phrase[12] = {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\0'};
}
```

Dans cet exemple, il y a un espace entre le mot 'Hello' et le mot 'world'.

Ainsi, le tableau doit inclure un caractère d'espace vide.

Pour imprimer la chaîne, vous utilisez la fonction `printf()`, le code de format `%s` et le nom du tableau :

```c
#include <stdio.h>

int main() {
  char phrase[] = {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\0'};

  printf("%s\n", phrase);

}
```

Une autre façon de créer une chaîne de caractères en C est d'utiliser une chaîne littérale.

Dans ce cas, vous créez un tableau de caractères puis vous attribuez la chaîne en l'enfermant dans des guillemets doubles :

```c
#include <stdio.h>

int main() {
  char word[] = "Hello";

}
```

Avec les littéraux de chaîne, le terminateur nul (`\0`) est implicite.

La création de chaînes avec des littéraux de chaîne est plus facile, car vous n'avez pas besoin d'ajouter le terminateur nul à la fin. Cette méthode est également beaucoup plus lisible et nécessite moins de code.

Cependant, vous pouvez vouloir utiliser des tableaux de caractères lorsque vous souhaitez modifier le contenu de la chaîne. Les littéraux de chaîne sont en lecture seule, ce qui signifie que le contenu est fixe.

### Comment manipuler des chaînes de caractères en C

C fournit des fonctions qui vous permettent d'effectuer des opérations sur des chaînes de caractères, telles que la copie, la concaténation et la comparaison, pour n'en nommer que quelques-unes.

Pour utiliser ces fonctions, vous devez d'abord inclure le fichier d'en-tête `string.h` en ajoutant la ligne `#include <string.h>` en haut de votre fichier.

#### Comment trouver la longueur d'une chaîne de caractères en C

Pour calculer la longueur d'une chaîne de caractères, utilisez la fonction `strlen()` :

```c
#include <stdio.h>
#include <string.h>

int main() {
  char phrase[] = "Hello";

  int length = strlen(phrase);

  printf("String length: %i\n", length);

}
```

Sortie :

```plaintext
String length: 5
```

La fonction `strlen()` retournera le nombre de caractères qui composent la chaîne.

Notez que le résultat n'inclut pas le terminateur nul, `\0`.

#### Comment copier une chaîne de caractères en C

Pour copier une chaîne de caractères dans une autre, vous pouvez utiliser la fonction `strcpy()`.

Vous pouvez vouloir copier une chaîne de caractères en C lorsque vous devez apporter des modifications sans la modifier. Cela s'avère utile lorsque vous devez conserver le contenu de la chaîne originale intact.

La syntaxe générale de la fonction `strcpy()` ressemble à ceci :

```plaintext
strcpy(destination_string, original_string);
```

La fonction `strcpy()` copie `original_string` dans `destination_string`, y compris le terminateur nul (`'\0'`).

Une chose à noter ici est que vous devez vous assurer que le tableau de destination a assez d'espace pour la chaîne originale :

```c
#include <stdio.h>
#include <string.h>

int main() {
  
    char original[] = "Hello";
  
    char destination[20]; // Assurez-vous que ce tableau est assez grand

    strcpy(destination, original);

    printf("Copied string: %s\n", destination);
}
```

Sortie :

```plaintext
Copied string: Hello
```

La fonction `strcpy()` copie la chaîne originale dans un tableau vide et retourne la chaîne copiée, qui inclut également le caractère de terminateur nul (`'\0'`).

#### Comment concaténer des chaînes de caractères en C

Vous pouvez concaténer (ajouter) deux chaînes de caractères ensemble en utilisant la fonction `strcat()`.

La syntaxe générale de la fonction `strcat()` ressemble à quelque chose comme ce qui suit :

```plaintext
strcat(destination_string, original_string);
```

La fonction `strcat()` prend la chaîne `original` et l'ajoute à la fin de la chaîne `destination`.

Assurez-vous que la `destination_string` a assez de mémoire pour la `original_string`.

Une chose à noter ici est que `strcat()` ne crée pas une nouvelle chaîne.

Au lieu de cela, elle modifie la `destination_string` originale, en incluant la `original_string` à la fin.

Regardons un exemple de fonctionnement de `strcat()` :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    
  char greeting[50] = "Hello, ";
  
  char name[] = "Dionysia";

  strcat(greeting, name);

  printf("Message: %s\n", greeting);
  
}
```

Sortie :

```plaintext
Message: Hello, Dionysia
```

#### Comment comparer des chaînes de caractères en C

Pour comparer deux chaînes de caractères pour vérifier leur égalité, vous pouvez utiliser la fonction `strcmp()`.

La syntaxe générale de la fonction `strcmp()` ressemble à ceci :

```plaintext
strcmp(string1, string2);
```

La fonction `strcmp()` compare `string1` avec `string2` et retourne un entier.

Si la valeur de retour de `strcmp()` est `0`, cela signifie que les deux chaînes sont identiques :

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "apples";
  char word2[] = "apples";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Résultat : 0

}
```

Si la valeur de retour de `strcmp()` est inférieure à `0`, cela signifie que le premier mot vient avant le second :

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "apples";
  char word2[] = "bananas";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Résultat : -1

}
```

Et si la valeur de retour de `strcmp()` est supérieure à `0`, cela signifie que le premier mot vient après le second :

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "bananas";
  char word2[] = "apples";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Résultat : 1

}
```

## Apprentissage supplémentaire : Sujets avancés en C

Bien que ce manuel ait couvert un large éventail de sujets, il reste encore tant à apprendre, car la programmation est si vaste.

Une fois que vous avez construit une base solide avec les bases de la programmation C, vous pouvez vouloir explorer des concepts plus avancés.

Vous pouvez vouloir passer à l'apprentissage des fonctions, par exemple. Elles vous permettent d'écrire des instructions pour une tâche spécifique et de réutiliser ce code dans tout votre programme.

Vous pouvez également vouloir apprendre les pointeurs. Les pointeurs en C sont comme des flèches qui vous montrent où une information spécifique est stockée dans la mémoire de l'ordinateur.

Ensuite, vous pouvez vouloir passer à l'apprentissage des structures. Ce sont comme des conteneurs de données personnalisés qui vous permettent de regrouper différents types d'informations sous un seul nom.

Enfin, vous pouvez vouloir apprendre à travailler avec des fichiers. Travailler avec des fichiers en C vous permet de lire et d'écrire dans des fichiers. Cela est utile pour des tâches comme sauvegarder des données utilisateur, lire des paramètres de configuration ou partager des données entre différents programmes.

Ces suggestions ne sont pas un guide définitif – juste quelques idées pour continuer votre apprentissage de la programmation C.

Si vous êtes intéressé à en apprendre davantage, vous pouvez consulter les ressources suivantes de freeCodeCamp :

* [Tutoriel de programmation C pour débutants](https://www.youtube.com/watch?v=KJgsSFOSQv0&t=12372s)
    
* [Apprendre la programmation C en utilisant le livre classique de Kernighan et Ritchie](https://www.freecodecamp.org/news/learn-c-programming-classic-book-dr-chuck/)
    
* [Découvrir les mystères des pointeurs en C](https://www.freecodecamp.org/news/finally-understand-pointers-in-c/)
    

## Conclusion

Cela marque la fin de cette introduction au langage de programmation C.

Merci beaucoup d'avoir persévéré et d'être arrivé jusqu'à la fin.

Vous avez appris à travailler avec des variables, divers types de données et des opérateurs.

Vous avez également appris à écrire des instructions conditionnelles et des boucles. Et vous avez appris les bases de la manipulation des tableaux et des chaînes de caractères.

Espérons que vous avez acquis une bonne compréhension de certains des fondamentaux de la programmation C, que vous avez obtenu quelques idées sur ce qu'il faut apprendre ensuite et que vous êtes enthousiaste à l'idée de continuer votre parcours en programmation.

Bon codage !