---
title: Une Introduction Plus Douce à la Programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-12T22:29:53.000Z'
originalURL: https://freecodecamp.org/news/a-gentler-introduction-to-programming-1f57383a1b2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*94q4HJ10s6rtvhLcQQuMRw.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une Introduction Plus Douce à la Programmation
seo_desc: 'By Matt Adesanya

  This write-up captures what I teach when I get coaching requests. I won’t jump into
  the code or a setup of any sort. I will teach concepts.

  If you work in a software development company as a non-programmer, you may wonder
  what the pr...'
---

Par Matt Adesanya

Cet article capture ce que j'enseigne lorsque je reçois des demandes de coaching. Je ne vais pas sauter dans le code ou une installation de quelque sorte. Je vais enseigner des concepts.

Si vous travaillez dans une entreprise de développement de logiciels en tant que non-programmeur, vous vous demandez peut-être ce que font les programmeurs. Et vous entendez de nouveaux mots à la mode tous les jours. Cet article a été écrit en pensant à vous. Que vous soyez une personne dans les ventes, un médecin, un avocat, un responsable commercial ou un comptable, si vous avez déjà eu l'idée d'apprendre à coder, c'est un bon endroit pour commencer.

### Comment cet article est organisé

Cet article est divisé en 4 parties. Après avoir lu chaque partie, vous trouverez une section quiz pour vous aider à mieux vous rappeler ce que vous avez lu. Ensuite, vous trouverez une section "aller de l'avant" et les réponses au quiz.

Notez que chaque mot à la mode introduit dans cette série est en **gras**, comme **algorithme**.

![Image](https://cdn-media-1.freecodecamp.org/images/DK7wB4Z7ruYntQ2XWjpBwlbHm4B9fuSNhoN0)
_Illustration par [John Adesanya](https://www.facebook.com/adesanya.john.52" rel="noopener" target="_blank" title=")_

### Partie 1 — Qu'est-ce que la Programmation ?

Une réponse simple serait : « La programmation est l'acte d'instruire les ordinateurs pour qu'ils exécutent des tâches. » On l'appelle souvent **codage**.

Alors, qu'est-ce qu'un **programme informatique** ? Un programme informatique est une séquence d'instructions que l'ordinateur exécute.

L'ordinateur dans la définition ci-dessus est tout appareil capable de traiter du code. Cela pourrait être des smartphones, des guichets automatiques, le Raspberry Pi, des serveurs, pour n'en nommer que quelques-uns.

#### Une Bonne Analogie pour la Programmation

Tout d'abord, il y a des schémas dans notre vie quotidienne. L'univers fonctionne de manière quelque peu prévisible ; par exemple, le jour et la nuit, les saisons, le lever et le coucher du soleil. Les gens suivent des routines comme se lever le matin, aller à l'école ou au travail. Nous recevons des instructions d'autres personnes comme nos supérieurs au travail. La façon dont nous cuisinons certaines recettes peut être expliquée en étapes finies.

Deuxièmement, chaque fois que nous utilisons des appareils intelligents, du code s'exécute en arrière-plan. Déplacer un pointeur de souris d'une partie de l'écran de votre ordinateur à une autre peut sembler une tâche simple, mais en réalité, tant de lignes de code viennent de s'exécuter. Un acte aussi simple que de taper des lettres dans Google Docs conduit à l'exécution de lignes de code en arrière-plan. C'est du code partout.

> Les programmes informatiques sont également appelés **code**. **Ne pas utiliser le mot 'codes'** (le code doit être utilisé comme un nom non comptable). D'accord, ce n'est pas un cours d'anglais, revenons aux affaires.

#### Le Langage Naturel de l'Ordinateur

Les machines ont leur langage naturel comme les humains. Les ordinateurs ne comprennent pas le langage humain. Le langage naturel des ordinateurs est le code binaire — 1 et 0. Ceux-ci représentent deux états : **allumé (1)** et **éteint (0)**.

C'est le langage naturel des équipements électroniques. Il serait fastidieux pour nous, en tant qu'êtres humains, de communiquer avec l'ordinateur en binaire.

#### Entrée des Langages de Programmation

Pour communiquer avec des machines qui parlent binaire, nous le faisons dans un langage qui est plus proche de notre propre langage naturel. Comme l'anglais, le français, le swahili ou l'arabe. Les langages de programmation sont proches de nos langages naturels. Mais ils sont plus structurés et doivent être appris à fond.

Ils peuvent être des langages de haut niveau ou de bas niveau. Les langages de programmation de haut niveau sont plus éloignés du langage machine que les langages de bas niveau. Cet "éloignement" est généralement appelé une **abstraction**, mais nous n'aborderons pas cela dans cette série. Ne nous laissons pas distraire :)

L'ordinateur a besoin d'un moyen de comprendre notre langage humain. Pour ce faire, nous aurons besoin d'un traducteur.

#### Qu'est-ce que les Traducteurs

Le code source fait référence au code écrit dans un langage de programmation particulier. Plus à ce sujet dans la Partie 2.

Les traducteurs ont la responsabilité de convertir votre code source en langage machine. Cela est également connu sous le nom de **binaire**. Souvenez-vous des uns et des zéros. Nous pouvons désigner les binaires comme **Code Objet**, le Programme ou un mot commun aujourd'hui : **App**.

![Image](https://cdn-media-1.freecodecamp.org/images/4NAINQiVOx5JSNH9XOrmaLpIvJPcxqvofFgd)

Les traducteurs peuvent être l'un des suivants :

* Interpréteurs
* Compilateurs
* Un hybride d'Interpréteurs et de Compilateurs
* Assembleurs

#### Interpréteurs

Certains langages sont interprétés. Le traducteur traite le code source ligne par ligne et exécute chaque ligne dans le programme ou l'application final. Cela signifie que le code source interprété commence à s'exécuter jusqu'à ce qu'il rencontre une erreur. Ensuite, l'interpréteur s'arrête pour signaler de telles erreurs. Plus de détails à ce sujet dans la Partie 3.

Python est un bon exemple de langage de programmation interprété.

#### Compilateurs

Les compilateurs fonctionnent différemment. Ils convertissent le code source dans son intégralité via un processus de compilation en binaire. Le binaire est ensuite exécuté. Si des erreurs étaient présentes dans le code source, elles sont détectées pendant le temps de compilation et signalées. Cela interrompt le processus de compilation, et aucun binaire n'est généré.

Les interpréteurs traduisent ligne par ligne et exécutent la ligne avant de passer à la ligne suivante. Les compilateurs traduisent toutes les lignes d'un programme en un fichier (binaire) et exécutent le fichier entier.

Souvenez-vous de la définition du programme informatique ? C'est une séquence d'instructions qui est exécutée par un ordinateur.

Un programme en cours d'exécution est généralement appelé un processus. De tels programmes utilisent certaines ressources sur le système informatique ou le smartphone, comme la mémoire, l'espace disque et le système de fichiers. Un programme en cours d'exécution peut également être dit **en cours d'exécution**.

Nous utilisons le mot 'run' lorsque nous exécutons un programme informatique. Le temps qu'il faut pour exécuter de tels programmes est connu sous le nom de **run-time** du programme.

Il est courant de voir des programmes appelés Apps. Nous associons également les programmes aux plateformes ou environnements dans lesquels ils s'exécutent, ou sont conçus pour. Il y a des applications web, qui s'exécutent sur des navigateurs web, comme Google Spreadsheet. Il y a des applications mobiles, qui s'exécutent sur des smartphones comme CandyCrush. Il y a aussi des applications de bureau comme l'application de bureau Evernote.

Encore une fois, le code source interprété est exécuté directement à partir du fichier source. Le code source compilé est converti en un fichier binaire. Le fichier binaire est ensuite exécuté. Le code source compilé peut échouer pendant le run-time même après une compilation réussie. Voir Partie 3.

#### Traducteurs Hybrides

Un traducteur hybride est une combinaison de l'Interpréteur et du Compilateur. Un langage de programmation hybride populaire est **Java**. Java compile d'abord votre code source en un format intermédiaire connu sous le nom de **Bytecode**.

Le Bytecode est ensuite interprété et exécuté par un moteur d'exécution également connu sous le nom de Machine Virtuelle. Cela permet aux traducteurs hybrides d'exécuter le bytecode sur divers systèmes d'exploitation.

#### Assembleurs

Il y a aussi l'Assembleur pour traduire le langage d'assemblage de bas niveau en binaire.

Pour cette série, nous nous concentrerons uniquement sur les langages de haut niveau.

Une bonne façon de voir les Traducteurs est de les considérer comme un programme en eux-mêmes. Vous devez les télécharger ou les obtenir, les installer sur votre système informatique et comprendre leur fonctionnement de base.

#### Une Question Souvent Posée

Voici une question que les débutants posent généralement.

> Quel langage dois-je apprendre en premier ?

Il existe des centaines de langages de programmation. Ils sont classés par popularité, communauté, support à long terme, pédagogie, utilisation commerciale. Ils peuvent également être classés par technicité, comme s'ils sont fonctionnels, impératifs, statiques, forts, ou faiblement typés.

Certains langages sont plus pédagogiques que d'autres. Certains langages sont à des fins éducatives et non pour un usage commercial. Il existe des langages écrits, par exemple, pour que les enfants apprennent à coder.

Il existe des langages très puissants qui sont faciles à installer et à apprendre. **Python** est un tel langage de programmation. Je le recommande généralement aux débutants.

![Image](https://cdn-media-1.freecodecamp.org/images/P62XnEB9KpX8GJ4AttJ29WDuuUeOs0lt-bbe)

Si vous êtes intéressé à explorer plus d'options pour votre "premier langage", [voici](https://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext) une bonne recherche de Philip Guo.

Lorsque vous voulez apprendre un nouveau langage, vous savez maintenant que vous aurez besoin de ce **traducteur de langage**. C'est un programme que vous installez et configurez sur votre système informatique.

Je vous recommande de commencer à apprendre à utiliser un **CLI** (Command Line Interface). Le CLI est le terminal ou la console. Considérez le terminal comme une alternative à une GUI (Graphical User Interface).

Dans les GUI, vous interagissez avec l'ordinateur via le pointeur de la souris. Vous dépendez également des rendus visuels des répertoires, et de presque tout ce que vous faites.

Mais, lorsque vous utilisez un CLI, vous interagissez avec l'ordinateur en utilisant des commandes que vous tapez à l'invite ou un curseur **clignotant**

```
$_
```

Dans Windows, le terminal intégré est l'invite de commande. Pour les utilisateurs de Mac et Linux, vous avez déjà un terminal Bash par défaut. Pour obtenir la même expérience sur Windows, installez [Git Bash](https://git-scm.com/) OU [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/powershell-scripting?view=powershell-5.1).

#### Aller de l'Avant

Maintenant que vous avez été légèrement introduit à ce qu'est la programmation. Vous devez vous préparer pour votre première ligne de code :)

Pour commencer, vous aurez besoin des éléments suivants :

* Un système informatique  
À ce stade, vous n'avez pas besoin d'un système sophistiqué ou très coûteux, vous avez seulement besoin d'un ordinateur qui fonctionne bien.
* Installer le CLI  
Je recommande [ce cours accéléré](https://learnpythonthehardway.org/book/appendixa.html) pour vous lancer sur l'utilisation du CLI.
* Installer un éditeur de texte  
Nous reviendrons sur ce point dans la Partie 2
* Apprendre un langage de programmation  
Dans cette série, vous apprendrez les éléments de base qui constituent les connaissances fondamentales de la plupart des langages de programmation.

#### Quiz

* Quels outils de base avez-vous besoin pour commencer à programmer ?
* Quelle commande utiliseriez-vous pour les actions suivantes dans bash (CLI) ?
* Vérifier votre répertoire actuel
* Changer pour un répertoire nommé 'bin' (bin est dans votre répertoire actuel)
* créer un nouveau répertoire appelé 'lib'
* créer un nouveau fichier appelé 'book.py'
* lister tout le contenu du répertoire actuel

#### Résumé

Nous avons passé en revue les bases de la programmation, avec une introduction aux Traducteurs. Le mot « code source » ne vous est plus étranger. Nous examinerons ce qu'est un code source en détail dans la partie suivante.

#### Réponses au Quiz

Quels outils de base avez-vous besoin pour commencer à programmer ?  
Un ordinateur, un éditeur de texte, le shell (terminal), et un compilateur/interpréteur

Quelle commande utiliseriez-vous pour les actions suivantes dans bash (CLI) ?

* Vérifier votre répertoire actuel : `pwd`
* Changer pour un répertoire nommé 'bin' : `cd bin`
* créer un nouveau répertoire appelé 'lib' : `mkdir lib`
* créer un nouveau fichier appelé 'book.py' : `touch book.py`
* lister tout le contenu du répertoire actuel : `ls`

![Image](https://cdn-media-1.freecodecamp.org/images/v7gKv7gZ0PMNZ0MXUGEGOKAs2ykSWt5ywi9r)
_De Wikimedia Commons, le dépôt de médias libres_

### Partie 2 — Code Source

Maintenant que vous comprenez le concept de la programmation, nous allons examiner le code source.

Un code source est essentiellement un fichier, tout comme un fichier Microsoft (.doc), mais légèrement différent. C'est un fichier texte brut, écrit sur des éditeurs très simples, comme le Bloc-notes de Windows. Vous vous souviendrez de la section précédente que vous avez besoin d'interpréteurs ou de compilateurs pour convertir votre code source en binaire. Le code source doit être enregistré dans un fichier, qui est passé en entrée au traducteur.

Selon le langage que vous écrivez, il existe des extensions désignées pour enregistrer votre fichier de code source. L'extension de Python est '.py'. Java est '.java'. Php est '.php' et PERL est '.pl' pour n'en nommer que quelques-uns.

Lorsque vous avez terminé d'écrire votre code source, vous devez l'exécuter via le traducteur. Par exemple, voici comment exécuter votre code source Python en utilisant la commande `python`.

#### Pour Commencer : Votre Premier Programme

* Suivez les instructions [ici](https://realpython.com/learn/python-first-steps/) pour configurer Python sur votre système informatique.
* Installez un éditeur simple pour taper votre code source. Vous pouvez utiliser l'éditeur de texte [sublime](https://www.sublimetext.com/3) pour commencer.
* Ouvrez un nouveau fichier dans votre éditeur et tapez ce qui suit :

```
print 'Hello Python!'
```

* N'oubliez pas d'enregistrer le fichier sous main.py
* Trouvez le chemin du fichier sur votre CLI et tapez la commande suivante :

```
$ python main.py
```

Le résultat devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Hz0MuuL5PGDJQnx0iJl06iJQt0F8SVRulj-P)

#### L'Anatomie d'un Code Source Typique

Nous allons maintenant examiner le contenu d'un fichier de code source typique. Voici les composants réguliers :

#### Mots-clés

Mots courts, lisibles par l'homme, généralement connus sous le nom de **mots-clés**. Ils sont propres au langage que vous apprenez, et ils sont spéciaux. Nous y reviendrons dans un instant. Vous devez apprendre certains des mots-clés par cœur. Voici l'ensemble des [mots-clés](https://www.programiz.com/python-programming/keyword-list) reconnus et utilisés en Python.

![Image](https://cdn-media-1.freecodecamp.org/images/CmdM7Tw8hsew5PmsStcHrpmjhJoYok0EgbxU)

[_https://www.programiz.com/python-programming/keyword-list_](https://www.programiz.com/python-programming/keyword-list)

#### Identifiants

Mots inventés par Vous — Oui Vous, le programmeur. Ces mots sont généralement appelés **Identifiants**. Ils peuvent être créés par vous ou d'autres programmeurs. Ils sont conditionnés sous forme de plugins, mieux connus sous le nom de **Bibliothèques**.

Un exemple de bibliothèque est la bibliothèque Math. Elle vous permet d'accéder à des fonctions comme la racine carrée (Math.sqrt), utilisée en Javascript.

De nombreux langages de programmation sont livrés avec de nombreuses bibliothèques. Celles-ci sont généralement appelées leurs **SDK** (Software Development Kits). Vous les téléchargerez avec le compilateur pour commencer à construire des technologies, des applications et des projets. En plus de ceux-ci, il y a des **frameworks**, conçus pour aider à construire sur une plateforme particulière comme le web ou le mobile.

Certains identifiants sont regroupés avec un langage que vous utilisez et ne peuvent pas être utilisés comme identifiant nommé par l'utilisateur. Un exemple est le mot **string** en java. De tels identifiants, avec les mots-clés, sont connus sous le nom de **Mots Réservés**. Ils ne sont pas des mots-clés, mais comme les mots-clés, ils sont également spéciaux.

Tous les mots-clés sont des mots réservés, l'inverse n'est pas vrai.

Les mots que vous choisissez doivent être significatifs pour quiconque les voit au premier coup d'œil.

Une utilisation courante des identifiants est dans la nomination des **variables**, nous allons examiner cela dans un instant.

#### Types de Données de Base

Vous trouverez également des données de différents types dans un code source, des **nombres** (3, 5.7, -100, 3.142) et des **caractères** (M, A). Dans certains langages de programmation, les nombres sont encore divisés en leurs propres types tels que les **entiers**.

Les entiers peuvent être **Signés** ou **Non Signés**, **grands** entiers, et **petits** entiers. Grand ou petit dépend en fait de la quantité d'espace mémoire réservé pour de tels nombres. Il y a des nombres avec des parties décimales, généralement appelés **double** et **float**, selon le langage que vous apprenez.

Nous avons également des types de données booléens qui évaluent à vrai ou faux.

#### Types de Données Complexes

Les types de données expliqués ci-dessus sont connus sous le nom de types de données élémentaires, primaires ou de base. Nous pouvons construire des types de données plus complexes à partir de ces types de données de base.

Un **Tableau** est la forme la plus simple du type de données complexe. Une **Chaîne** est un Tableau de **caractères**. Nous ne pouvons pas nous en passer et nous les utilisons souvent lorsque nous écrivons notre code source.

Une combinaison de caractères est une chaîne. Pour utiliser une analogie, une chaîne est pour un ordinateur ce qu'un mot est pour un être humain. Le mot 'Thermomètre' est composé de 11 caractères — nous l'appelons simplement une chaîne de caractères. Le traitement des chaînes est un sujet vaste en soi à apprendre, et doit être étudié par tout programmeur en herbe.

Les types de données complexes sont livrés avec la plupart des langages de programmation que vous utilisez. Il y en a d'autres que nous construisons nous-mêmes en tant que programmeurs, comme les systèmes de Classes. Ceux-ci sont également connus sous le nom de (**OOP**) Programmation Orientée Objet.

#### Variables

Les variables sont simplement des emplacements mémoire nommés. Nous voulons parfois conserver des données dans notre code source dans un endroit où nous pouvons rappeler les données, pour les utiliser à nouveau. Il s'agit généralement d'un emplacement mémoire que notre compilateur/interpréteur réserve pour nous. Nous devons nommer ces emplacements mémoire pour les rappeler plus tard. Considérez l'extrait de code Python ci-dessous :

```
pet_name = 'Hippo'print pet_name
```

`pet_name` est un exemple de variable. Parce que le type de données stocké dans `pet_name` est une chaîne. Il est connu comme une variable de chaîne. Il existe également des variables numériques. Les variables sont catégorisées par leurs types de données.

#### Constantes

Les constantes sont des valeurs qui ne changent pas tout au long de la durée de vie du programme. Nous utilisons des lettres majuscules pour imposer que certaines valeurs soient des valeurs constantes. Certains langages fournissent un moyen de créer des valeurs constantes, tandis que d'autres ne le font pas.

Certains langages offrent le luxe de déclarer les types que les variables doivent être. Nous appelons souvent ceux-ci des langages **fortement typés**. Java est un bon exemple.

D'autres ne fournissent pas ces fonctionnalités. Ils sont **faiblement typés** ou **langages de programmation dynamiques**. Python est un bon exemple.

Voici comment déclarer des valeurs constantes en JavaScript.

```
const petName = 'Hippo'
```

#### Littéraux

Dans chaque code source, il y a des types de données que vous utilisez partout dans votre code et qui ne changeront que si vous les modifiez vous-même. Nous appelons ceux-ci des littéraux, qui ne doivent pas être confondus avec des variables ou des constantes. Les littéraux peuvent être vus dès que vous parcourez le code source. Ils peuvent être des chaînes, des nombres, des décimales ou d'autres types de données.

Dans l'extrait de code source ci-dessus, le mot 'Hippo' est un littéral — un littéral de chaîne. Il sera toujours 'Hippo' jusqu'à ce que vous modifiez le code source. En apprenant à coder, vous apprendrez à gérer les littéraux dans votre code source de manière à ce qu'il soit facile à maintenir sans changer beaucoup de votre code source.

#### Ponctuations/Symboles

Dans la plupart des codes sources, vous trouverez généralement différents signes de ponctuation selon le langage de programmation. Java a plus de signes de ponctuation, par exemple que Python.

Les signes de ponctuation courants incluent la virgule (`,`), le point-virgule (`;`), les deux-points (`:`), les accolades (`{}`), les parenthèses (`()`), les crochets (`[]`), les guillemets (`" "`), le pipe (`|`), la barre oblique (`\`), le point (`.`), le point d'interrogation (`?`), le circonflexe (`^`) et le pourcentage (`%`).

Bienvenue dans le monde de la programmation, où les signes de ponctuation sont vos meilleurs amis. Vous vous retrouverez à les taper beaucoup.

#### Opérateurs

Les chances que vous écriviez du code pour effectuer une opération sont très élevées. De la manière la plus simple, vous effectuerez une opération d'affectation dans votre code source. Nous sommes présentés avec un grand nombre d'opérateurs par les langages de programmation que nous utilisons. Les exemples incluent l'addition (`+`), la division (`/`), la multiplication (`*`), la soustraction (`-`) et supérieur à (`&`gt;).

Les opérateurs peuvent généralement être classés comme suit :

* Opérateurs d'Affectation  
Cela est parfois confondu avec égal à. Égal à est utilisé pour comparer deux valeurs. L'opérateur d'affectation place une valeur dans une variable, comme `pet_name = 'Hippo'`
* Opérateurs Arithmétiques  
Comprend les opérateurs pour effectuer des tâches arithmétiques telles que l'addition et la soustraction. Certains langages fournissent certains opérateurs arithmétiques que d'autres peuvent ne pas avoir. Par exemple, l'opérateur modulo (`%`) retourne la valeur du reste dans les opérations de division.
* Opérateurs Relationnels  
sont utilisés pour comparer des valeurs. Ils incluent supérieur à, inférieur à, égal à, non égal à. Leur représentation varie également selon le langage de programmation que vous apprenez. `&l`t;> n'est pas égal à dans certains langages, tandis que dans d'autres, `i`ts `!= o`r !==.
* Opérateurs Logiques  
sont utilisés pour calculer des opérations logiques. Les opérateurs logiques couramment utilisés sont and, or, not. Certains langages représentent ces opérateurs avec des symboles tels que `&&` pour and, `||` pour or, et `!` pour not. Les valeurs des opérations logiques évaluent généralement à des valeurs booléennes `true` ou `false`.

#### Commentaires

La documentation sera un aspect important de vos activités de codage. C'est ainsi que vous expliquez votre code à d'autres programmeurs. Cela se fait via des commentaires qui sont occasionnellement ajoutés à des parties de votre code. Grâce aux commentaires, vous pouvez guider d'autres programmeurs à travers le type de données avec lequel votre code fonctionne et le type de sortie qu'il génère.

Généralement, le compilateur ignore les lignes de code qui sont des commentaires.

Les commentaires varient selon les langages. Le `#` est utilisé pour introduire des commentaires en Python.

Voici un exemple de commentaire en Python.

```
# extrait de programme pour calculer la suite de fibonacci de N nombres
```

En Java, C et C++, il y a des commentaires pour une seule ligne comme le `#` en Python, mais le symbole `//` est utilisé à la place. Il y a aussi des commentaires multi-lignes `/*` … `*/`. Vous pouvez lire plus sur les commentaires dans le langage que vous avez choisi d'apprendre.

#### Espaces et Tabulations

Ce sont des espaces créés entre le code que vous écrivez. Cela se fait lorsque vous appuyez sur la barre d'espace ou la touche de tabulation sur votre clavier.

#### Aller de l'Avant

Assurez-vous de configurer correctement Python sur votre système informatique et d'exécuter votre premier programme.

#### Quiz

Voici un simple quiz pour vous.   
Identifiez les différents éléments que nous avons étudiés jusqu'à présent dans l'extrait de code source Java ci-dessous :

```
// une implémentation récursive de Factorielleimport java.util.Scanner;class RecursiveFactorial {  public static void main(String[] args) {    Scanner input=new Scanner(System.in);    System.out.print("Find the Factorial of: ");    int num=input.nextInt();    System.out.println("Factorial of "+num+" = "+fact(num));  }
```

```
 static long fact(int n) {  if(n<2) return 1;  return n*fact(n-1); }}
```

#### Résumé

Vous avez été introduit à ce qu'est un code source, et avez examiné le contenu d'un code source typique.

Compilé ou traduit, votre code peut éventuellement échouer à s'exécuter pour un certain nombre de raisons. Ces raisons sont généralement liées à des erreurs dans votre code source. Ces erreurs sont connues sous le nom de bugs.

L'acte de trouver et de supprimer ces bugs est appelé débogage et est une compétence que vous devez apprendre en tant que programmeur. Nous examinerons ce que sont les bugs dans la partie suivante.

#### Réponses au Quiz

Identifiez les différents éléments que nous avons étudiés jusqu'à présent dans l'extrait de code source Java ci-dessous :

Mots-clés :  
import, class, public, static, void, new, int, long, if, return

Identifiants :  
java, util, Scanner, RecursiveFactorial, main, String, args, input, System, in, out, print, println, num, nextInt, fact, n

Littéraux :  
Littéraux de Chaîne — "Factorial of " = "Find the Factorial of: "  
Littéraux Entiers — 2, 1

Opérateurs :  
Opérateur d'Affectation `=`  
Concaténateur `+` (pour joindre des chaînes ensemble)  
inférieur à `&`lt;  
multipl`l`y *  
soustra`c`t -

Ponctuation et Symboles  
`{ } [] ( ) ; .`

Commentaire  
`//`une implémentation récursive de Factorielle

![Image](https://cdn-media-1.freecodecamp.org/images/CRBCrOTDE8OtiY5W7Jb6cvLznp9d4HfRTKii)

### Partie 3 — Débogage

Une fois que vous commencez à essayer des extraits de code ou que vous essayez de résoudre des problèmes réels avec du code, vous réaliserez bientôt qu'il y aura des moments où votre programme se brise, est interrompu et cesse de fonctionner.

Cela est souvent causé par des erreurs, connues sous le nom de **bugs** ou **exceptions** en temps d'exécution. L'acte de trouver et de supprimer les bugs de notre code est le **débogage**. Vous devenez meilleur dans le débogage du code à mesure que vous le pratiquez davantage. Nous ne déboguons pas seulement notre propre code, nous pouvons également déboguer le code écrit par d'autres programmeurs.

Pour commencer, nous devons identifier les bugs courants susceptibles de se manifester dans notre code source.

#### Erreurs de Syntaxe

Ces erreurs ne permettront pas à votre code source de compiler dans les langages de programmation compilés. Elles sont détectées au moment de la compilation ou pendant l'interprétation de votre code source. Elles peuvent également être facilement détectées par des linters. Nous en apprendrons un peu plus sur les **linters** plus tard.

Elles sont principalement causées lorsque vous rompez la forme ou la structure attendue du langage dans lequel vous codez. Un exemple est l'oubli d'une parenthèse fermante dans une équation.

#### Erreurs Sémantiques

Les erreurs sémantiques, également connues sous le nom d'erreurs logiques, sont les plus problématiques de toutes les erreurs. Elles ne peuvent pas être facilement détectées. Un signe qu'il y a une erreur sémantique est lorsque le programme s'exécute avec succès mais ne produit pas la sortie souhaitée.

Considérez cet exemple :

```
3 + 5 * 6
```

Selon l'ordre de priorité, populairement appelé BODMAS en mathématiques, nous nous attendons à ce que la partie multiplication soit évaluée en premier, puis le résultat final sera 33. Si le programmeur voulait que l'addition soit évaluée en premier, cela donnerait une sortie différente de celle souhaitée. Des erreurs comme celle-ci sont des erreurs sémantiques, ayant plus à voir avec la signification qu'avec la structure (syntaxe).

Des parenthèses autour de `3 + 5` donneront la sortie souhaitée de 48 à la place.

```
(3 + 5) * 6
```

#### Erreurs d'Exécution

Comme les erreurs sémantiques, les erreurs d'exécution ne sont jamais détectées au moment de la compilation. Contrairement aux erreurs sémantiques, les erreurs d'exécution interrompent le programme et l'empêchent de s'exécuter davantage. Elles sont généralement causées par un résultat inattendu de certains calculs dans le code source.

Voici un bon exemple :

```
input = 25x = 0.8/(Math.sqrt(input) - 5)
```

L'extrait de code ci-dessus se compilera avec succès, mais une entrée de `25` entraînera une `ZeroDivisionError`. Il s'agit d'une erreur d'exécution. Un autre exemple populaire est le `StackOverflowError` ou `IndexOutofBoundError`. Ce qui est vraiment important, c'est que vous identifiiez ces erreurs et appreniez à les gérer.

Il existe des erreurs causées par la manière dont votre code source utilise la mémoire et l'espace sur la plateforme ou l'environnement dans lequel il est exécuté. Ce sont également des erreurs d'exécution. Des erreurs telles que `OutOfMemoryError` et `HeapError` sont généralement causées par la manière dont votre code source utilise les ressources. Une bonne connaissance des **algorithmes** vous aidera à écrire du code qui utilise mieux les ressources.

Le processus de réécriture de votre code pour de meilleures performances est appelé **optimisation**, et un mot pas vraiment lié est **refactoring**. À mesure que vous passez plus de temps à coder, vous devez également garder ces concepts à l'esprit.

#### Débogage

Voici quelques conseils sur la manière de procéder au débogage de votre code :

* **Utiliser des Linters**  
Les linters sont des outils qui aident à **lire votre code source** pour vérifier s'ils se conformen à la norme attendue dans le langage que vous utilisez. Il existe des linters pour de nombreux langages de programmation. Assurez-vous d'en obtenir un pour le langage que vous apprenez.
* **IDEs plutôt que des éditeurs simples**  
Vous pourriez opter pour un **IDE** conçu pour le langage que vous apprenez. IDE signifie Integrated Development Environment. Ce sont des logiciels conçus pour écrire, déboguer, compiler et exécuter du code. Ils sont généralement livrés avec des kits de débogage puissants, pour surveiller ou parcourir votre code.   
Jetbrains crée de grands IDE comme Webstorm et IntelliJ. Il y a NetBeans, Komodo, Qt editor, Android Studio, XCode (fournis avec Mac) pour n'en nommer que quelques-uns.
* **Lire votre code à voix haute**  
Cela est généralement utile lorsque vous cherchez une erreur sémantique. En lisant votre code à voix haute, il y a de fortes chances que vous lisiez également l'erreur. Cela pourrait vous sauter aux yeux comme ce qui était probablement faux.
* **Lire les journaux d'erreurs**  
Lorsque le compilateur signale une erreur, assurez-vous de regarder le numéro de ligne ou la partie de votre code signalée.

#### Aller de l'Avant

En tant que débutant, vous apprendrez à coder à partir de livres, de tutoriels en ligne ou de vidéos. Vous taperez souvent du code tel que vous le voyez.

Voici quelque chose que vous devriez faire, lorsque vous avez terminé d'écrire ou d'exécuter un tel code, **apprenez à les casser**. Comment faites-vous cela ?

Changez quelque chose pour voir comment le code se comporte. Faites cela pour ne pas faire d'hypothèses sur quoi que ce soit et pour être sûr de comprendre ce qui se passe.

#### Quiz

1. Quel est le bug probable dans l'extrait de code Python ci-dessous :

```
items = [0,1,2,3,4,5]print items[8]
```

```
//indice : items ici est un Array, avec 6 items. Pour récupérer le 4ème item par exemple, vous utiliserez items[3]. Nous commençons à compter à partir de 0.
```

2. Quel est le bug probable dans l'extrait de code Python ci-dessous :

```
input = Hippo'if input == 'Hippo':  print 'Hello, Hippo'
```

#### Résumé de la Section

Félicitations ! Le mot bug ne vous est plus étranger, et repérer les bugs ne devrait plus l'être non plus. Ensuite, nous examinerons le flux commun du code que nous écrivons tous les jours.

#### Réponses au Quiz

Quel est le bug probable dans l'extrait de code Python ci-dessous :  
(1) Erreur d'Exécution : Erreur d'Index Hors Limites  
(2) Erreur de Syntaxe : Guillemet d'ouverture manquant à la ligne 1

![Image](https://cdn-media-1.freecodecamp.org/images/wyv7WKjSRkKdfaLB6xgtI0EGnOJtrxZ392eF)
_[http://www.publicdomainpictures.net/](http://www.publicdomainpictures.net/" rel="noopener" target="_blank" title=")_

### Partie 4 — Flux de Codage de Base

#### Ligne de Code, Expressions et Instructions

L'unité de tout code source est la **LOC (Ligne de Code)**. Le programme le plus simple est une ligne de Code. Une LOC pourrait être un mot-clé, un symbole ou une instruction. C'est une Ligne de Code tant qu'elle est sur une ligne séparée.

Considérons une simple ligne de code :

`area = 0.5 * base * height`

`0.5 * base * height` est une expression. **Une expression** est une combinaison d'opérateurs et d'opérandes. Dans l'exemple donné ici, les opérandes sont `0.5`, `base`, `height`. Vous vous souviendrez que `0.5` est un littéral à virgule flottante, `base` et `height` sont des variables. L'opérateur est le `*` (multiplication).

Les expressions peuvent ne pas être significatives en restant seules comme une LOC. Lorsque nous attribuons la valeur d'une expression à une autre variable, dans le cas ci-dessus `area`, ce que nous avons s'appelle une instruction. C'est encore une instruction lorsque nous attachons des expressions à des mots-clés, exemple : `return 0.5 * base * height`

Pour le reste de cette section, nous représenterons une instruction par le symbole **S**. La n-ième instruction sera **Sn** parmi une séquence (ou un ensemble) d'instructions

Pour saisir rapidement la programmation, un bon point de départ est de comprendre les flux de codage de base. Les flux de base sont également appelés **flux de contrôle**. Une fois que vous comprenez ces flux, vous les trouverez dans beaucoup des langages de programmation que vous apprenez.

Notez que les exemples donnés dans cet article sont purement basiques. Vous devez vous référer au langage que vous apprenez pour obtenir une connaissance approfondie des mots-clés qu'il fournit.

De plus, les flux de base introduits ici sont différents des **modèles de conception** en programmation. Comprenez d'abord ces flux de base. Vous rattraperez plus tard les modèles de conception courants en programmation à mesure que vous apprendrez davantage.

Voici les flux de programmation de base :

* Séquentiel
* Conditionnel/Branchement
* Itération/Répétition/Boucles

#### Séquentiel

C'est le flux le plus basique, où une instruction est exécutée après l'autre. En réalité, tous les autres flux se résolvent en un flux séquentiel (plus à ce sujet plus tard).

```
S1S2S3...Sn
```

Dans certains langages de programmation comme JavaScript, il est possible que S3 s'exécute avant S1. Cela se produit si S1 est bloqué par certaines tâches qui peuvent prendre plus de temps comme les opérations de base de données ou de fichiers, connues sous le nom de **tâches asynchrones**. Il existe des moyens de contourner des cas comme celui-ci. Ne vous inquiétez pas, ce sera un jeu d'enfant à apprendre lorsque vous choisirez le langage de programmation à apprendre.

#### Conditionnel/Branchement

L'instruction qui s'exécute est déterminée par des conditions. Le mot-clé clé ici est le mot-clé `if`. C'est l'un des flux de codage les plus utilisés.

Voici le modèle conditionnel le plus simple :

```
if (condition) then:   S1
```

Dans l'exemple ci-dessus, soit `S1` s'exécute, soit rien ne se passe. `S1` est exécuté uniquement si la condition donnée est vraie.

Voici un autre modèle conditionnel :

```
if (condition) then:  S1  S2else:  S3  S4
```

Cela peut être lu comme l'exécution de `S1`-`S2` ou `S3`-`S4` en fonction de la condition donnée. Si la condition est vraie, `S1` et `S2` seront traités. Sinon, les instructions `S3` et `S4` seront traitées. Cela, en réalité, est un flux séquentiel :

```
S1S2
```

Nous avons également le style multi-conditionnel :

```
if (condition1) then:  S1else if (condition2) then:   S2else:  S3
```

Ici, si `condition1` est vraie, alors `S1` est traité. Sinon, `condition2` est testée, et si elle est vraie, `S2` est traité. Cela peut continuer ainsi.

Pour le style multi-conditionnel, de nombreux langages de programmation fournissent l'instruction `switch`. Voici le modèle pour l'instruction switch :

```
switch value:  case condition1:    S1    break    case condition2:    S2    break
```

```
default:    S3
```

Les `condition1` et `condition2` sont comparées avec la valeur dans l'instruction switch. Si l'une d'elles est vraie par rapport à la valeur, alors l'instruction dans le bloc de cas est exécutée.

Il existe d'autres choix pour le flux conditionnel. Certains sont spécifiques au langage que vous décidez d'apprendre, comme l'opérateur conditionnel (`: ?`), et d'autres mots-clés qui facilitent le branchement, comme `cycle` et `break`. Assurez-vous de passer du temps à comprendre le flux conditionnel/branchement.

#### Itération/Répétition/Boucles

Le flux d'itération/répétition maintient l'exécution des instructions tant que certaines conditions sont remplies, et arrête l'exécution des instructions une fois que la condition n'est plus vraie.

Voici le modèle :

```
while (condition):  S1  S2
```

Dans l'exemple ci-dessus, les instructions `S1` et `S2` peuvent s'exécuter une fois, plusieurs fois, ou ne pas s'exécuter du tout. Si la condition donnée est vraie la première fois que l'instruction `while` est rencontrée, alors `S1` et `S2` seront traités. La condition `while` est vérifiée à nouveau, et `S1` et `S2` seront exécutés tant que la condition est vraie.

Le moment où la condition devient **fausse**, l'exécution de `S1` et `S2` s'arrête.

Le résultat de l'instruction ci-dessus si la condition est vraie trois fois sera :

```
S1S2S1S2S1S2
```

Quel est ce flux de codage ? Si vous avez répondu séquentiel, vous avez tout à fait raison. Comme nous pouvons le voir, les autres flux se résolvent en flux séquentiel.

Voici un autre modèle d'itération :

```
do:  S1  S2while (condition)
```

Dans cet exemple, `S1` et `S2` s'exécuteront au moins une fois ou plusieurs fois. Cela est dû au fait qu'ils s'exécuteront avant que la condition ne soit testée.

Dans de nombreux langages de programmation, des mots-clés comme `do` et `while` sont fournis pour implémenter le flux de répétition. Un autre mot-clé courant est le mot-clé `for`. Voici le modèle courant pour l'instruction `for`.

```
for (initialvalue; condition; decrement/increment initialvalue):  S1  S2
```

De nombreux langages ont `foreach` utilisé pour travailler à travers chaque élément dans un objet complexe tel qu'un tableau ou une structure.

#### Quiz

Identifiez les flux de codage dans l'extrait de code Python suivant :

```
numlist=[]cnt=0while cnt >= 0:  m=int(raw_input())  if m < 0:    break  numlist.append(m)  cnt=cnt+1
```

#### Résumé

Les flux couverts ici sont les flux de base. Il existe un moyen de regrouper un ensemble de code et de leur donner un nom. De cette façon, vous pouvez appeler cet ensemble de code chaque fois que vous en avez besoin en une seule fois. Cela est appelé une procédure. Dans le cas où l'ensemble de code effectue une opération et retourne une valeur, vous avez une fonction.

La manière dont les procédures et les fonctions sont implémentées varie selon les différents langages. Vous ne pouvez pas sauter celles-ci pour obtenir les bases de n'importe quel langage. Elles sont très importantes pour organiser votre code. En fait, c'est là que commencent les blocs de construction de votre code, également connu sous le nom de **programmation modulaire**.

Il existe d'autres flux que vous apprendrez dès que vous comprendrez les fonctions, celui qui me vient à l'esprit est la **récursivité**.

Pourtant, vous constaterez que dans les procédures et les fonctions se trouvent toujours les flux de codage impressionnants que nous avons couverts ici — séquentiel, conditionnel et flux itératif/boucles.

### Aller de l'Avant

Maintenant que vous avez appris les concepts les plus basiques de la programmation de votre ordinateur. Si vous souhaitez en apprendre davantage, ou faire carrière dans le développement de logiciels, alors tout ce que vous avez à faire est de plonger plus profondément dans les eaux plus profondes. Il existe de nombreuses ressources pour vous aider à apprendre. Savoir lesquelles choisir en fonction de votre niveau d'expérience compte beaucoup.

Essayez de ne pas vous laisser submerger par les nouveaux termes que vous entendez de la part des programmeurs plus expérimentés dans votre cercle d'amis. Vous pourriez garder un bloc-notes pour noter ces termes, mais ne soyez pas sous pression pour découvrir ce qu'ils signifient. Vous rattraperez votre retard en apprenant et en pratiquant.

Voici quelques ressources pour aider à lancer votre carrière de codeur, et pour vous aider à construire sur la fondation que vous avez obtenue ici :

* [https://www.codecademy.com/](https://www.codecademy.com/)   
Choisissez le cours Python
* [https://app.pluralsight.com/library/courses/what-is-programming/table-of-contents](https://app.pluralsight.com/library/courses/what-is-programming/table-of-contents)  
Cours Gratuit sur Pluralsight

NOTE : Je ne recommande pas de trop lire sur le même sujet. Je crois en agissant sur le peu que vous avez appris, c'est-à-dire en pratiquant. C'est pourquoi je ne déverse pas trop de liens ici pour votre apprentissage. N'hésitez pas à chercher sur Google ou à en trouver d'autres en fonction de ce que vous savez déjà si vous n'êtes pas un débutant.

#### Défi Final

Je vous lance le défi de :  
Relever l'un de ces défis :

* Trouver une application simple en ligne et la reproduire dans le langage de programmation que vous avez appris

OU

* Pensez à une idée même si elle est aussi simple qu'une application de liste de tâches  
construisez une application autour de cette idée.

Je recommande cet [article](https://www.codementor.io/codementorteam/how-to-build-app-from-scratch-beginner-programmer-7z0atq56w) de [codementor](http://codementor.io/) pour vous lancer sur ce sujet.

#### Réponses au Quiz

Identifiez les flux de codage dans les extraits de code Python suivants.

* Flux séquentiel
* Itération   
l'instruction `while`
* Conditionnel  
l'instruction `if`

Un grand merci à [Maya Neria](https://www.linkedin.com/in/maya-neria-5bb18763/?ppe=1), [Joshua Ugba](https://www.linkedin.com/in/joshua-ugba-o-0a193936/) et [Mohini Ufeli](http://medium.com/@mohiniufeli) pour avoir révisé cet article, [Surajudeen Akande](https://www.linkedin.com/in/sirolad/) pour m'avoir incité à le publier, l'équipe éditoriale d'Andela pour les révisions, [John Adesanya](https://www.facebook.com/adesanya.john.52) pour les illustrations et à 'Kunmi — ces leçons ont commencé avec son désir d'apprendre à coder.

_Si vous avez aimé cela, cliquez sur l'icône d'applaudissements pour que d'autres personnes voient cela ici sur medium. De plus, si vous avez des questions ou des observations, utilisez la section des commentaires pour partager vos pensées._