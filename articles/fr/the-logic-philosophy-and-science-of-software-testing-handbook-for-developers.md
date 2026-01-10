---
title: La logique, la philosophie et la science des tests logiciels – Un manuel pour
  les développeurs
date: '2025-06-17T18:43:38.266Z'
author: Han Qi
authorURL: https://www.freecodecamp.org/news/author/gitgithan/
originalURL: https://freecodecamp.org/news/the-logic-philosophy-and-science-of-software-testing-handbook-for-developers
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750176539544/965a99ef-8aad-467c-ae6b-4a144e2d1117.png
tags:
- name: Testing
  slug: testing
- name: debugging
  slug: debugging
- name: logic
  slug: logic
- name: Software Engineering
  slug: software-engineering
- name: 'Science '
  slug: science
- name: handbook
  slug: handbook
seo_desc: 'In an age of information overload, AI assistance, and rapid technological
  change, the ability to think clearly and reason soundly has never been more valuable.

  This handbook takes you on a journey from fundamental logical principles to their
  practica...'
---


À une époque de surcharge d'informations, d'assistance par l'IA et de changements technologiques rapides, la capacité à penser clairement et à raisonner sainement n'a jamais eu autant de valeur.

<!-- more -->

Ce manuel vous emmène dans un voyage allant des principes logiques fondamentaux à leurs applications pratiques dans le développement de logiciels, le raisonnement scientifique et la pensée critique.

Que vous soyez un lycéen apprenant à structurer sa pensée, un professionnel déboguant des systèmes complexes, ou simplement quelqu'un de curieux de comprendre le fonctionnement d'un raisonnement solide, ce manuel fournit des outils pour une réflexion plus aiguisée et plus fiable.

## Ce que nous allons aborder :

### **Partie I : Théorie fondamentale**

Nous commençons par le socle de la logique formelle – comprendre les implications, les tables de vérité et les règles fondamentales du raisonnement.

Vous apprendrez l'échafaudage de tout ce qui suit :

-   Comment fonctionnent réellement les énoncés "si-alors" (spoiler : ce n'est pas toujours intuitif !)
    
-   Le pouvoir des tables de vérité pour cartographier tous les scénarios possibles
    
-   Pourquoi certains arguments sont valides alors que d'autres sont des sophismes logiques
    
-   La relation élégante entre le **Modus Ponens, le Modus Tollens et les Contraposées**
    

### **Partie II : Applications pratiques**

C'est ici que la logique prend vie de manière concrète :

**Dans le développement logiciel :**

-   Comment le débogage reflète le raisonnement logique, et pourquoi vos tests pourraient vous mentir
    
-   La logique derrière le Test-Driven Development (TDD) et les tests de mutation
    

**Dans la pensée scientifique :**

-   Le principe de falsification de Karl Popper et pourquoi il est important au-delà du monde académique
    
-   Comment les **tests d'hypothèse** ne sont que des statistiques rencontrant le **Modus Tollens**
    

**Dans le raisonnement quotidien :**

-   Repérer les sophismes logiques dans les arguments, les médias et votre propre pensée
    
-   L'art d'envisager de multiples chemins causaux au lieu de sauter aux conclusions
    

### **Partie III : Profondeurs philosophiques**

La section finale confronte la belle complexité de l'application de la logique pure à un monde impur :

-   Pourquoi les relations parfaites de "**si et seulement si**" sont l'objectif mais sont rarement atteignables
    
-   Comment les systèmes logiciels modernes cachent leur complexité
    
-   L'effet papillon des bugs et pourquoi l'analyse des causes racines est souvent plus difficile qu'il n'y paraît
    
-   Outils de vérification formelle : de **Prolog** à **Coq** en passant par **TLA+**
    

## Ce que vous allez y gagner

### **Pour les étudiants :**

-   **Super-pouvoirs de pensée critique** : Apprenez à repérer les raisonnements fallacieux dans les arguments, les réseaux sociaux et les actualités
    
-   **Avantage académique** : Ces concepts apparaissent dans les débats, la philosophie, l'informatique, les mathématiques et les statistiques
    

### **Pour les ingénieurs logiciels :**

-   **Maîtrise du débogage** : Le _Modus Tollens_ pour le débogage : "Si la sortie est incorrecte, qu'est-ce qui pourrait en être la cause ?"
    
-   **Philosophie des tests** : Passez du "faire réussir les tests" à "prouver que le code est correct"
    
-   **Analyse de problèmes** : Évitez de sauter sur des solutions avant de comprendre le problème réel
    
-   **Conception de systèmes** : Pensez plus rigoureusement aux modes de défaillance et aux cas limites, évaluez les relations de cause à effet dans les systèmes complexes
    
-   **Communication et évolution de carrière** : Présentez des arguments de manière plus claire et persuasive, acquérez des compétences de pensée logique qui distinguent les ingénieurs seniors des juniors
    

### **Pour les scientifiques :**

-   **Conception expérimentale** : Renforcez votre compréhension des tests d'hypothèse et de la falsifiabilité
    
-   **Revue par les pairs** : Mieux évaluer la solidité logique des affirmations de recherche
    
-   **Rédaction de demandes de subvention** : Structurez vos arguments de manière plus persuasive en utilisant des fondements logiques solides
    

## Prérequis

J'introduirai des échantillons de code à partir de la seconde moitié de l'article, donc la connaissance d'un langage de programmation sera utile. Les concepts de cet article sont agnostiques au langage, mais j'ai utilisé Python partout pour la lisibilité.

Aucun bagage préalable en logique formelle ou en philosophie n'est strictement nécessaire, mais les éléments suivants vous permettront de tirer le meilleur parti de cet article :

-   Expérience en tests et débogage lors du développement de logiciels.
    
-   Savoir ce qu'est un REPL (Read-Evaluate-Print-Loop) si vous voulez essayer les assistants de preuve.
    
-   Connaissance des opérateurs logiques (NOT, AND, OR) et du fait qu'ils prennent 1 ou 2 valeurs booléennes en entrée et renvoient une seule valeur booléenne en sortie.
    
-   Pensée algébrique de base : représenter des énoncés par des variables (P, Q), le concept de NOT (¬) comme inversion d'énoncés, et le concept selon lequel différentes combinaisons d'entrées peuvent atteindre la même sortie.
    
-   Exposition au raisonnement déductif, où les inférences sont faites sur la base de faits, et aux sophismes, qui sont des manières dont les arguments peuvent être défaillants.
    
-   Volonté de s'engager dans un va-et-vient conceptuel entre des exemples concrets en français et des symboles logiques abstraits.
    
-   Accepter de détenir des idées potentiellement conflictuelles entre le monde logique idéal et le monde réel impur.
    
-   Ouverture à remettre en question l'intuition et à suivre les règles logiques avant d'appliquer votre expérience du monde réel.
    

## Table des matières

1.  [Une introduction à la logique](#heading-une-introduction-a-la-logique)
    
2.  [Tables de vérité : cartographier toutes les possibilités](#heading-tables-de-verite-cartographier-toutes-les-possibilites)
    
3.  [Contraposées, Modus Ponens, Modus Tollens](#heading-contraposees-modus-ponens-modus-tollens)
    
4.  [L'origine de P⟹Q : Science et réalité](#heading-lorigine-de-p-q-science-et-realite)
    
5.  [Retour sur les formes d'arguments : inférences valides et sophismes courants](#heading-retour-sur-les-formes-darguments-inferences-valides-et-sophismes-courants)
    
6.  [Nier l'antécédent : un exemple de base de données](#heading-nier-lantecedent-un-exemple-de-base-de-donnees)
    
7.  [Assigner des significations concrètes à la logique](#heading-assigner-des-significations-concretes-a-la-logique)
    
8.  [Appliquer la logique aux tests logiciels](#heading-appliquer-la-logique-aux-tests-logiciels)
    
9.  [Un regard plus attentif sur les tests](#heading-un-regard-plus-attentif-sur-les-tests)
    
10.  [Retour sur les quatre énoncés pour le code](#heading-retour-sur-les-quatre-enonces-pour-le-code)
    
11.  [L'ingrédient manquant - Si et seulement si](#heading-lingredient-manquant-si-et-seulement-si)
    
12.  [Tests de mutation : tester les tests](#heading-tests-de-mutation-tester-les-tests)
    
13.  [Vers une confiance en "si et seulement si"](#heading-vers-une-confiance-en-si-et-seulement-si)
    
14.  [Les défis du monde réel](#heading-les-defis-du-monde-reel)
    
15.  [Lueurs d'espoir : outils et pratiques pour la clarté](#heading-lueurs-despoir-outils-et-pratiques-pour-la-clarte)
    
16.  [Le pouvoir de la falsification dans les tests](#heading-le-pouvoir-de-la-falsification-dans-les-tests)
    
17.  [Assistants de preuve](#heading-assistants-de-preuve)
    
18.  [Matière à réflexion](#heading-matiere-a-reflexion)
    
19.  [Q.E.D. : Le pouvoir durable de la logique dans un monde incertain](#heading-qed-le-pouvoir-durable-de-la-logique-dans-un-monde-incertain)
    
20.  [Ressources](#heading-ressources)
    
21.  [Glossaire](#heading-glossaire)
    

![homme debout au bord d'un lac regardant au loin](https://cdn.hashnode.com/res/hashnode/image/upload/v1749064487021/b0404a1e-3257-4815-bc42-517b2ea955d0.jpeg)

## Une introduction à la logique

Imaginez que l'énoncé suivant soit Vrai :

**Si vous êtes un instructeur de code, alors vous avez un emploi.**

Maintenant, est-ce que ceci a du sens ?

1.  Vous n'avez pas d'emploi, donc vous n'êtes pas un instructeur de code.
    
2.  Vous avez un emploi, donc vous êtes un instructeur de code.
    
3.  Vous n'êtes pas un instructeur de code, donc vous n'avez pas d'emploi.
    

### Interprétations

Basé sur la logique :

-   L'énoncé 1 est correct.
    
-   L'énoncé 2 est faux car vous pouvez avoir d'autres emplois sans être un instructeur de code.
    
-   L'énoncé 3 est faux car vous pouvez ou non avoir un emploi, et comme précédemment, vous pouvez avoir d'autres emplois sans être un instructeur de code.
    

### Complexité croissante

Ces énoncés deviennent de plus en plus complexes en raison de :

-   Le passage de 2 énoncés valides à 2 conclusions invalides.
    
-   Le passage d'un statut d'emploi clair (1, 2) à une incertitude sur l'existence ou le type d'emploi (3).
    

Familiarisons-nous avec certaines notations avant de voir comment les **tables de vérité** aident à gérer cette complexité.

### Notations

| Notation | Signification | Exemple (si P="Il pleut", Q="Le sol est mouillé") |
| --- | --- | --- |
| **P, Q** | Propositions | P, Q |
| **⟹** | Implique / Si...alors... | P⟹Q ("S'il pleut, alors le sol est mouillé") |
| **¬** | Non | ¬P ("Il ne pleut pas") |
| **∧** | Et (conjonction) | P∧Q ("Il pleut et le sol est mouillé") |
| **∨** | Ou (disjonction) | P∨Q ("Il pleut ou le sol est mouillé") |
| **⟺** | Si et seulement si (biconditionnel) | P⟺Q ("Il pleut si et seulement si le sol est mouillé") |
| ∴ | Donc | P ⟹ Q : S'il pleut, le sol est mouillé ; P : Il pleut ; ∴ Q : **Donc**, le sol est mouillé |

## Tables de vérité : cartographier toutes les possibilités

### **Qu'est-ce qu'une table de vérité ?**

Une table de vérité est un outil puissant en logique qui nous aide à déterminer la vérité ou la fausseté globale d'un énoncé logique composé. Elle le fait en listant systématiquement **toutes les combinaisons possibles** de valeurs de vérité (Vrai ou Faux) pour ses propositions composantes individuelles.

Pour chaque façon dont les "entrées" (nos propositions comme P et Q) peuvent être vraies ou fausses, la table de vérité vous montre la "sortie" précise (la valeur de vérité de l'énoncé logique complet, tel que P⟹Q).

### **Pourquoi les tables de vérité sont-elles utiles ?**

Les tables de vérité offrent des avantages critiques pour une pensée claire :

-   **Clarté et précision :** Elles éliminent l'ambiguïté en montrant explicitement le résultat pour chaque scénario.
    
-   **Analyse systématique :** Elles garantissent qu'aucune combinaison possible n'est oubliée, ce qui est vital pour un raisonnement sain.
    
-   **Fondation pour la compréhension :** Elles définissent comment fonctionnent les règles logiques, formant le socle de l'analyse d'arguments plus complexes dans n'importe quel domaine.
    

### **Comment lire notre première table de vérité :**

Examinons la table de vérité pour l'implication P⟹Q ("Si P alors Q").

Chaque ligne représente un scénario unique, combinant les valeurs de vérité de P et Q pour montrer la valeur de vérité résultante de P⟹Q.

| P | Q | P⟹Q (Si P alors Q) | Utilisé dans |
| --- | --- | --- | --- |
| Vrai | Vrai | Vrai | Modus Ponens ✅ |
| Vrai | Faux | Faux | Falsifiabilité 🚨 |
| Faux | Vrai | Vrai | Aucune inférence |
| Faux | Faux | Vrai | Modus Tollens ✅ |

Analysons chaque ligne :

-   **Colonnes P et Q :** Elles montrent les valeurs de vérité d'entrée (Vrai ou Faux) pour nos deux propositions. Comme chacune peut avoir l'une des deux valeurs, nous avons 2×2 = 4 combinaisons uniques, remplissant les quatre lignes.
    
-   **Colonne P ⟹ Q :** C'est la valeur de vérité de sortie de l'énoncé "Si P alors Q" pour chaque combinaison d'entrées P et Q.
    
    -   **Ligne 1 : P est Vrai, Q est Vrai.**
        
        -   Si P est vrai (**vous êtes un instructeur de code**) et Q est aussi vrai (**vous avez un emploi**), alors l'implication P⟹Q est **Vraie**. (L'énoncé "Si...alors..." tient).
            
        -   Cette ligne est clé pour le **Modus Ponens**.
            
    -   **Ligne 2 : P est Vrai, Q est Faux**
        
        -   Si P est vrai (**vous êtes un instructeur de code**) mais Q est faux (**vous n'avez pas d'emploi**), alors l'implication P⟹Q est **Fausse**. C'est le seul scénario qui invalide un énoncé "si-alors".
            
        -   Cette ligne est clé pour la **Falsifiabilité**.
            
    -   **Ligne 3 : P est Faux, Q est Vrai.**
        
        -   Si P est Faux (**vous n'êtes pas un instructeur de code**) mais Q est Vrai (**vous avez un emploi**), alors l'implication P⟹Q est toujours considérée comme **Vraie**. Cela peut sembler contre-intuitif.
            
        -   La raison est que l'énoncé d'implication affirme _seulement_ ce qui se passe quand P est vrai. Si P est faux, l'affirmation de l'implication n'est pas testée, elle est donc considérée comme [vacueusement vraie][22].
            
    -   **Ligne 4 : P est Faux, Q est Faux.**
        
        -   Si P est Faux (**vous n'êtes pas un instructeur de code**) et Q est Faux (**vous n'avez pas d'emploi**), alors l'implication P⟹Q est également considérée comme **Vraie**.
            
        -   Comme pour la ligne 3, puisque la condition initiale (P) était fausse, la valeur de vérité de l'implication reste Vraie, car elle n'a pas été réfutée.
            
        -   Cette ligne est clé pour le **Modus Tollens**.
            

La colonne "Utilisé dans" sert d'aperçu des arguments logiques ou concepts spécifiques qui reposent sur le comportement de chaque ligne, que nous explorerons en détail plus tard.

### Approfondir la compréhension de l'implication (P⟹Q)

La plupart des programmeurs connaissent les tables de vérité via les opérateurs logiques comme **AND (∧)**, **OR (∨)** et **NOT (¬)**, où elles définissent la sortie basée sur les combinaisons d'entrées.

L'implication (P⟹Q) fonctionne de manière similaire, sa sortie est définie par les règles de la logique propositionnelle, et non par une relation causale du monde réel ou votre "bon sens". Pour toute paire d'entrées P et Q, le résultat de P⟹Q est fixe.

Si cela semble contre-intuitif, considérez que la logique mathématique, comme tout système formel, est construite sur des **axiomes** convenus. Ces vérités de base acceptées nous permettent de construire des systèmes d'idées complexes. S'ils sont plus tard jugés inefficaces ou contradictoires, ces axiomes peuvent être redéfinis, ou un nouveau système peut être développé.

En logique formelle, cette implication est également définie comme étant logiquement équivalente à **"NON P OU Q" (¬P∨Q)**.

C'est la règle logique fondamentale qui dicte pourquoi, **si P est Faux, P⟹Q est toujours Vrai, quelle que soit la valeur de vérité de Q**. Vous pouvez également comprendre cela en utilisant la forme **NON P OU Q**.

-   Si P est Faux, cela signifie que NON P est Vrai.
    
-   En utilisant les règles de l'opération logique :
    
    -   Vrai (NON P) OU Vrai (Q) est Vrai (**NON P OU Q**)
        
    -   Vrai (NON P) OU Faux (Q) est Vrai (**NON P OU Q**)
        
    -   **NON P OU Q** est Vrai indépendamment de ce qu'est Q.
        

Ce qui précède explique les lignes 3 et 4 de la table de vérité à partir de la forme **NON P OU Q**. À titre d'exercice, vous pouvez appliquer les entrées (P, Q) des deux premières lignes de la table de vérité à NON P OU Q pour arriver aux mêmes résultats définis dans la colonne P⟹Q.

Cette définition formelle nous permet d'utiliser l'implication pour raisonner de manières puissantes, non seulement dans le sens "direct" (P⟹Q, menant au Modus Ponens), mais aussi dans un sens "inverse" crucial.

Cette forme inverse (**Contraposée**) consiste à échanger et à nier les propositions (¬Q⟹¬P).

Par exemple, si "Si vous êtes un instructeur de code, alors vous avez un emploi" est vrai, alors il doit aussi être vrai que "Si vous n'avez pas d'emploi (¬Q), alors vous n'êtes pas un instructeur de code (¬P)".

Cette manière de raisonner "à l'envers", qui sous-tend le Modus Tollens, est un outil puissant pour inférer des conclusions à partir de résultats observés.

Nous explorerons la **Contraposée** et deux formes d'arguments (**Modus Ponens, Modus Tollens**) en détail par la suite.

## Contraposées, Modus Ponens, Modus Tollens

Nous avons exploré l'implication fondamentale (P⟹Q) et comment les tables de vérité révèlent son comportement.

Maintenant, nous explorons des outils de raisonnement qui s'appuient sur ce fondement : le **Modus Ponens**, le **Modus Tollens** et le concept de **Contraposée**. Ce sont des principes de base de l'argumentation valide et de la pensée logique efficace.

### Qu'est-ce que l'équivalence logique ?

Avant de plonger dans ces concepts spécifiques, clarifions ce que signifie l'**équivalence logique**. Deux énoncés sont **logiquement équivalents** s'ils ont toujours la même valeur de vérité dans toutes les circonstances possibles. En termes plus simples, si un énoncé est vrai, l'autre est _toujours_ vrai. Si l'un est faux, l'autre est _toujours_ faux. Ils sont, par essence, des manières différentes de dire la même chose sur le plan logique.

Comprendre l'équivalence logique est incroyablement utile. Cela permet de :

-   **Simplifier la logique :** Cela nous permet de substituer un énoncé par un autre sans changer la vérité d'un argument, ce qui simplifie les preuves et le raisonnement complexes.
    
-   **Réduire la complexité :** Dans des domaines comme la conception de circuits, cela peut conduire à utiliser moins de portes physiques.
    
-   **Maintenir la correction logicielle :** En programmation, cela aide à maintenir la justesse du code lors du refactoring et du débogage, en particulier lors de la simplification des structures conditionnelles, en garantissant que le code transformé se comporte toujours de manière identique à l'original dans toutes les conditions.
    

### La contraposée : une implication équivalente

L'une des équivalences logiques les plus importantes concerne la **contraposée** d'une implication. La contraposée d'un énoncé "Si P alors Q" (P⟹Q) est **"Si non Q, alors non P"** (¬Q⟹¬P).

Vous pourriez intuitivement vous demander comment "**Si P alors Q**" pourrait être logiquement identique à "**Si non Q alors non P**". Démontrons-le à l'aide d'une table de vérité.

Nous commencerons par nos colonnes familières P et Q et l'implication P⟹Q. Ensuite, nous ajouterons des colonnes pour ¬P (Non P) et ¬Q (Non Q), et enfin, l'implication pour la contraposée, ¬Q⟹¬P.

Voyons comment la table de vérité montre explicitement cette équivalence :

![Table de vérité des colonnes P, Q, P->Q, non P, non Q, non Q -> non P](https://cdn.hashnode.com/res/hashnode/image/upload/v1747584857181/2732a798-da1d-48d9-aa92-c1ca3459b169.png)

### Explication du tableau

1.  **P, Q, P ⟹ Q (Colonnes 1-3) :** Ce sont nos propositions standard et l'implication que nous avons déjà définie.
    
2.  **¬P (Colonne 4) :** Cette colonne montre simplement la négation (valeur de vérité opposée) de la colonne P. Si P est Vrai, ¬P est Faux, et vice-versa.
    
3.  **¬Q (Colonne 5) :** De même, cette colonne montre la négation de la colonne Q.
    
4.  **¬Q ⟹ ¬P (Colonne 6) :** C'est la contraposée. Nous appliquons les mêmes règles d'implication apprises précédemment, mais en utilisant ¬Q comme partie "si" et ¬P comme partie "alors". Par exemple, à la ligne 2, ¬Q est Vrai et ¬P est Faux. Selon la règle d'implication (Vrai ⟹ Faux donne Faux), le résultat pour ¬Q⟹¬P est Faux.
    
5.  **La preuve d'équivalence :** Maintenant, comparez la **colonne 3 (P⟹Q)** avec la **colonne 6 (¬Q⟹¬P)**. Vous remarquerez que pour chaque ligne, leurs valeurs de vérité sont identiques ! Quand P⟹Q est Vrai, ¬Q⟹¬P est aussi Vrai. Quand P⟹Q est Faux, ¬Q⟹¬P est aussi Faux. Cela illustre parfaitement pourquoi ils sont **logiquement équivalents**.
    

Ainsi, "Si vous êtes un instructeur de code, alors vous avez un emploi" (P⟹Q) est logiquement la même chose que de dire "Si vous n'avez pas d'emploi, alors vous n'êtes pas un instructeur de code" (¬Q⟹¬P). Ils transmettent la même information sur la relation entre être un instructeur de code et avoir un emploi.

### Comment le Modus Ponens et le Modus Tollens se rapportent à l'implication

Ayant défini l'équivalence logique et la contraposée, nous pouvons maintenant comprendre précisément deux des formes les plus fondamentales et valides d'argument déductif : le **Modus Ponens** et le **Modus Tollens**. Ces deux formes d'argument reposent sur une prémisse centrale selon laquelle une implication (P⟹Q) est vraie, puis utilisent une information supplémentaire pour tirer une conclusion valide.

1.  **Modus Ponens (Affirmation de l'antécédent) :** C'est souvent considéré comme la forme d'inférence logique la plus intuitive et directe. Il fonctionne dans le sens "direct" de l'implication.
    
    -   **Prémisse 1 :** On nous donne que l'implication est vraie : Si P, alors Q (P⟹Q).
        
    -   **Prémisse 2 :** On nous donne aussi que la partie "si", l'antécédent, est vraie : P est vrai.
        
    -   **Conclusion :** Par conséquent, nous pouvons validement inférer que la partie "alors", le conséquent, doit aussi être vraie : Q est vrai.
        

_Exemple :_

-   Prémisse 1 : S'il pleut (P), alors le sol est mouillé (Q).
    
-   Prémisse 2 : Il pleut (P).
    
-   Conclusion : Par conséquent, le sol est mouillé (Q).
    

Cela correspond directement à la **Ligne 1 (Vrai, Vrai)** de notre table de vérité pour P⟹Q.

2.  **Modus Tollens (Négation du conséquent) :** Cette forme d'argument fonctionne dans le sens "inverse" et repose directement sur l'équivalence logique d'une implication et de sa contraposée.
    
    -   **Prémisse 1 :** On nous donne que l'implication est vraie : Si P, alors Q (P⟹Q).
        
    -   **Prémisse 2** : On nous donne aussi que la partie "alors", le conséquent, est fausse : Non Q (¬Q).
        
    -   **Conclusion** : Par conséquent, nous pouvons validement inférer que la partie "si", l'antécédent, doit aussi être fausse : Non P (¬P).
        

_Exemple :_

-   Prémisse 1 : S'il pleut (P), alors le sol est mouillé (Q).
    
-   Prémisse 2 : Le sol n'est **pas** mouillé (¬Q).
    
-   Conclusion : Par conséquent, il ne pleut **pas** (¬P).
    

Le Modus Tollens est valide car si P⟹Q est vrai, sa contraposée (¬Q⟹¬P) doit aussi être vraie. Appliquer le Modus Ponens à cette contraposée (avec ¬Q comme seconde prémisse) mène directement à la conclusion ¬P. Cela correspond à la **Ligne 4 (Faux, Faux)** de notre table de vérité originale pour P⟹Q, où P et Q sont tous deux faux mais l'implication est toujours vraie.

Ces deux formes d'argument sont centrales au raisonnement déductif rigoureux, nous permettant de tirer des conclusions certaines basées sur la vérité des implications et des faits associés.

![Page de titre du livre de Charles Darwin : L'Origine des espèces](https://cdn.hashnode.com/res/hashnode/image/upload/v1749063972374/e3eaf8a6-8eb1-4fa2-9e97-703b547a81bd.jpeg)

## L'origine de P⟹Q : Science et réalité

En science, les hypothèses prennent souvent la forme "**Si P, alors Q**" où P est une cause et Q est son effet prédit – par exemple, "Si un médicament est administré (P), alors les symptômes s'améliorent (Q)."

Idéalement, P est contrôlable, comme dans les études expérimentales, mais même dans les études observationnelles, P doit être clairement défini et mesurable.

Chaque expérience donne une observation, reflétant l'une des quatre combinaisons possibles de valeurs de vérité de P et Q.

### Le cas falsificateur en science et en logique

Chaque expérience produit une seule observation – l'une des quatre combinaisons possibles de P et Q.

-   Si P=Vrai, Q=Faux est observé (ligne 2 de la table de vérité), l'hypothèse est **falsifiée**.
    
-   Dans tous les autres cas, l'hypothèse n'est **pas falsifiée** (pour l'instant).
    

Ainsi :

-   Si toutes les observations tombent dans les 3 lignes préservant la vérité, l'hypothèse reste viable.
    
-   Si au moins une expérience donne P=Vrai, Q=Faux, soit :
    
    -   Nous concluons à la falsification, soit
        
    -   Nous réexaminons l'expérience et tentons une réplication avant d'accepter la falsification.
        

### Le pouvoir du cas falsificateur

#### Dans le monde logique

Le cas falsificateur n'est pas utile pour l'inférence avec le Modus Ponens ou le Modus Tollens car ces deux formes d'argument nécessitent de partir de **P⟹Q = Vrai**. J'expliquerai les deux arguments en détail plus tard.

Mais le cas falsificateur est utile pour montrer des contre-exemples afin d'infirmer l'implication, ou pour la preuve par contradiction.

#### Dans le monde scientifique réel

Le cas falsificateur incarne la **Falsifiabilité** – un concept crucial en science.

> Dans la mesure où un énoncé scientifique parle de la réalité, il doit être falsifiable : et dans la mesure où il n'est pas falsifiable, il ne parle pas de la réalité.
> 
> **— Karl R. Popper, La Logique de la découverte scientifique**

Les théories scientifiques naissent d'hypothèses qui sont continuellement testées et survivent aux tentatives de falsification.

### Falsification poppérienne et tests d'hypothèse

Ces deux approches, l'une philosophique et l'autre statistique, sont distinctes mais complémentaires dans la méthode scientifique.

-   La **falsification poppérienne** commence par une hypothèse scientifique (par exemple, "P a un effet sur Q"). Son objectif central est de rechercher activement des preuves qui infirmeraient cette hypothèse. Si de telles preuves sont trouvées, l'hypothèse est falsifiée.
    
-   Le **test d'hypothèse statistique** commence par une hypothèse nulle (H0) (par exemple, "P n'a aucun effet sur Q"). Son but est de déterminer si les données collectées fournissent des preuves suffisamment extrêmes pour rejeter cette hypothèse nulle.
    

Si l'hypothèse nulle est rejetée, cela fournit un soutien statistique à l'hypothèse alternative (que P _a_ effectivement un effet sur Q). Cette hypothèse statistiquement soutenue devient alors une candidate plus forte, continuellement soumise à d'autres tentatives poppériennes de falsification par de nouvelles expériences et observations.

### La nuance : l'implication n'est pas la causalité

P⟹Q n'implique **pas** intrinsèquement que P cause Q.

Considérez ces exemples :

-   "Si l'alarme incendie sonne, alors il y a de la fumée." L'alarme ne _cause_ pas la fumée.
    
-   "Si un collègue hurle pendant une revue de code, alors le code est mauvais." Le hurlement _cause_-t-il le mauvais code, ou le révèle-t-il simplement ? (Peut-être parfois les deux ! 😰)
    

La **causalité** est un concept du monde réel crucial pour prendre des décisions éclairées, prédire des résultats et inférer les raisons sous-jacentes des événements.

Elle est souvent centrale dans la modélisation prédictive et l'apprentissage supervisé en science des données, où la variable cible est l'effet et les prédicteurs sont les causes proposées. Un piège courant ici est la **fuite de données** (data leakage), où les prédicteurs sont par inadvertance influencés par (ou sont eux-mêmes des effets de) la cible, violant l'hypothèse causale.

La logique, cependant, ne modélise pas le temps, les mécanismes ou les interventions. Elle ne se soucie que des **valeurs de vérité et de la structure formelle**. La logique définit ce qui est vrai sur la base de prémisses, et non ce qui _rend_ quelque chose vrai au sens causal.

## Retour sur les formes d'arguments : inférences valides et sophismes courants

Nous avons maintenant établi les règles de l'implication, compris l'équivalence logique et appris deux formes d'arguments valides et puissantes : le **Modus Ponens** et le **Modus Tollens**. Mais quand nous essayons de raisonner à l'aide d'énoncés "si-alors", il est facile de tomber dans des pièges logiques courants.

Dans cette section, nous allons revisiter systématiquement les quatre manières courantes dont nous pourrions essayer de tirer des conclusions d'une implication **P⟹Q (Si vous êtes un instructeur de code, alors vous avez un emploi)** introduite au début du manuel.

Deux sont des arguments valides (Modus Ponens et Modus Tollens), et deux sont des sophismes logiques courants. Comprendre les différences est crucial pour un raisonnement sain.

D'abord, définissons rapidement les parties d'une condition "si-alors" :

-   **Antécédent :** La partie "si" de la condition (P).
    
-   **Conséquent :** La partie "alors" de la condition (Q).
    

Maintenant, examinons ces quatre formes d'arguments, en utilisant notre connaissance des tables de vérité et l'exemple de l'instructeur de code.

### Affirmation de l'antécédent (Modus Ponens)

C'est la première forme d'argument valide dont nous avons discuté. On l'appelle "affirmation de l'antécédent" car elle affirme la vérité de la partie "si" (l'antécédent, P) pour conclure la vérité de la partie "alors" (le conséquent, Q).

-   **Forme de l'argument :**
    
    1.  Si P, alors Q (P⟹Q)
        
    2.  P est vrai.
        
    3.  Par conséquent, Q est vrai.
        
-   **Exemples :**
    
    -   Vous êtes un instructeur de code (P), donc vous avez un emploi (Q).
        
    -   Vous avez fourni des données d'entrée invalides (P), donc le code affichera une erreur (Q).
        
-   **Interprétation :** Cet argument s'aligne directement sur la **Ligne 1 (P=Vrai, Q=Vrai)** de notre table de vérité, où l'implication est vraie. C'est souvent la forme la plus intuitive de déduction logique. En programmation, il est naturel de s'attendre à ce qu'une mauvaise entrée mène à des messages d'erreur si le code est conçu correctement.
    

### Négation du conséquent (Modus Tollens)

C'est la deuxième forme d'argument valide. On l'appelle "négation du conséquent" car elle affirme la fausseté de la partie "alors" (le conséquent, ¬Q) pour conclure la fausseté de la partie "si" (l'antécédent, ¬P). Comme nous l'avons appris, le Modus Tollens tire sa validité de l'équivalence logique de P⟹Q et de sa contraposée (¬Q⟹¬P).

-   **Forme de l'argument :**
    
    1.  Si P, alors Q (P⟹Q)
        
    2.  Non Q est vrai (¬Q).
        
    3.  Par conséquent, Non P est vrai (¬P).
        
-   **Exemples :**
    
    -   Vous n'avez pas d'emploi (¬Q), donc vous n'êtes pas un instructeur de code (¬P).
        
    -   Il n'y a pas de messages d'erreur (¬Q), donc les données d'entrée sont valides (¬P).
        
-   **Interprétation :** Cet argument correspond à la **Ligne 4 (P=Faux, Q=Faux)** de notre table de vérité, où P⟹Q est vrai, et P et Q sont tous deux faux. Cette forme de raisonnement est critique pour un débogage habile, vous permettant d'inférer des conclusions raisonnablement vraies sur la cause (P) à partir d'observations du résultat (Q), en supposant que la logique de votre programme (P⟹Q) tient.
    

### Affirmation du conséquent (Sophisme)

Nous passons maintenant aux pièges courants. C'est une **forme d'argument invalide** où nous tentons de conclure que l'antécédent (P) est vrai simplement parce que le conséquent (Q) est vrai. C'est un sophisme car la vérité de Q ne garantit pas la vérité de P, car Q pourrait avoir été causé par autre chose que P.

-   **Forme de l'argument (Invalide) :**
    
    1.  Si P, alors Q (P⟹Q)
        
    2.  Q est vrai.
        
    3.  Par conséquent, P est vrai. (\*\*Inférence incorrecte !\*\*🚨)
        
-   **Exemples :**
    
    -   Vous avez un emploi (Q), donc vous êtes un instructeur de code (P).
        
        -   Incorrect : Vous pourriez avoir beaucoup d'autres emplois.
    -   Le code a affiché une erreur (Q), donc vous avez fourni des données invalides (P).
        
        -   Incorrect : D'autres choses que des données invalides peuvent causer des erreurs.
-   **Interprétation :** Ce sophisme souligne la différence entre une relation un-à-un et une relation un-à-plusieurs. En regardant notre table de vérité, quand P⟹Q est Vrai et Q est Vrai, P pourrait être **Vrai (Ligne 1)** ou **Faux (Ligne 3)**. L'argument conclut à tort que P doit toujours être Vrai. L'incertitude vient du fait que l'observation de Q comme Vrai n'indique pas de manière unique P comme cause – il pourrait y avoir beaucoup d'autres raisons ou chemins menant à Q.
    
    -   Imaginez que vous marchez sur un sentier forestier, ignorant qu'un autre sentier a rejoint le vôtre derrière vous. En revenant sur vos pas, vous rencontrez une bifurcation (Q) à cette jonction et vous vous sentez désorienté, ne sachant pas quel chemin mène à votre point de départ (P). Tout comme plusieurs chemins peuvent converger vers le même point, plusieurs causes peuvent produire le même résultat.

### Négation de l'antécédent (Sophisme)

C'est une autre **forme d'argument invalide**. Ici, nous tentons de conclure que le conséquent (Q) est faux simplement parce que l'antécédent (P) est faux. C'est un sophisme car le fait que P soit faux ne garantit pas que Q sera également faux. Q pourrait toujours être vrai pour d'autres raisons, ou l'implication pourrait ne pas couvrir tous les scénarios où Q se produit.

-   **Forme de l'argument (Invalide) :**
    
    1.  Si P, alors Q (P⟹Q)
        
    2.  Non P est vrai (¬P).
        
    3.  Par conséquent, Non Q est vrai (¬Q). (\*\*Inférence incorrecte !\*\*🚨)
        
-   **Exemples :**
    
    -   Vous n'êtes pas un instructeur de code (¬P), donc vous n'avez pas d'emploi (¬Q).
        
        -   Incorrect : Vous pourriez avoir un emploi différent.
    -   Vous avez fourni des données valides (¬P), donc vous n'avez pas d'erreur (¬Q).
        
        -   Incorrect : Des données valides ne garantissent pas l'absence d'erreur. D'autres facteurs comme des problèmes réseau, des fuites de mémoire ou des opérations non idempotentes peuvent toujours causer des erreurs.
-   **Interprétation :** Similaire à l'affirmation du conséquent, ce sophisme provient de l'hypothèse incorrecte d'une relation unique. D'après notre table de vérité, quand P⟹Q est Vrai et P est Faux, Q pourrait être **Vrai (Ligne 3)** ou **Faux (Ligne 4)**. L'argument conclut à tort que Q doit toujours être Faux.
    

Ces deux sophismes (**Affirmation du conséquent** et **Négation de l'antécédent**) s'immiscent dans notre pensée lorsque nous supposons prématurément une cause unique pour un effet. Dans les systèmes complexes du monde réel, de nombreux facteurs peuvent mener à un résultat, et restreindre votre pensée trop tôt peut vous faire manquer des bugs ou vous mener à des conclusions erronées.

### Sophismes et implication : un prérequis

L'affirmation du conséquent et la négation de l'antécédent supposent toutes deux que l'implication sous-jacente (P⟹Q) est vraie.

Si cette implication est fausse dès le départ, il n'y a pas d'argument logique à construire, et donc, pas de sophisme à proprement parler.

### Exercice : Identifier une forme d'argument

Laquelle des 4 formes d'argument est-ce ?

-   **Les pingouins ne savent pas voler. Je ne sais pas voler. Donc, je suis un pingouin.**

_Indice : Reformulez la première phrase sous une forme si-alors._

## Nier l'antécédent : un exemple de base de données

Nous venons de voir que nier l'antécédent est un sophisme logique, ce qui signifie que même si l'implication initiale (P⟹Q) est vraie, conclure ¬Q à partir de ¬P n'est pas une inférence valide. Pour rendre ce concept abstrait concret, et pour illustrer pourquoi ce sophisme peut être particulièrement dangereux dans des systèmes réels comme les logiciels, explorons un exemple pratique impliquant une base de données.

L'implication : **Si la base de données est hors service (P), nous verrons une erreur de timeout de connexion (Q).**

Maintenant, en appliquant le sophisme de la négation de l'antécédent, nous pourrions conclure incorrectement : **Si la base de données n'est pas hors service (¬P), nous ne verrons pas d'erreur de timeout de connexion (¬Q). ❌**

Mais même si la base de données elle-même est parfaitement opérationnelle et "pas hors service", vous pourriez toujours rencontrer une erreur de timeout. Cela pourrait arriver pour diverses autres raisons indépendantes, telles que :

-   Des problèmes réseau
    
-   Des règles de pare-feu
    
-   La base de données est active mais extrêmement lente
    
-   Le moteur de requête est bloqué
    

Cet exemple spécifique de causes potentielles multiples pour un "timeout" met en évidence une compétence plus large et critique dans le développement de logiciels : **l'analyse exhaustive des cas**.

C'est précisément pourquoi les évaluations techniques, en particulier dans des domaines comme les algorithmes et la conception de systèmes, exigent fréquemment que vous considériez toutes les possibilités. Par exemple, on vous demande souvent de gérer les **cas de base et récursifs en programmation dynamique**, ou de garantir une **couverture mutuellement exclusive et collectivement exhaustive lors du regroupement de plusieurs scénarios dans des problèmes comme la fusion d'intervalles.**

Une telle analyse de cas rigoureuse est vitale pour minimiser les bugs et cultiver une approche ouverte d'esprit permettant d'envisager de multiples chemins causaux, guidée par l'expérience, la curiosité et le dévouement à l'artisanat.

Mais même une analyse de cas parfaite ne garantit pas une implémentation correcte. Une faible maîtrise du langage ou des hypothèses erronées peuvent toujours mener à des erreurs, faisant des tests une dernière ligne de défense cruciale.

Avant de passer à l'application de la logique aux tests logiciels, pratiquons notre agilité à basculer conceptuellement entre les concepts du monde réel en français et les symboles logiques.

![chaton devant un écran d'ordinateur rempli de code](https://cdn.hashnode.com/res/hashnode/image/upload/v1750012280729/731cd405-1a5c-45c1-8d16-9e6b28837979.jpeg)

## Assigner des significations concrètes à la logique

Nous devons définir ce à quoi P, Q et P⟹Q se réfèrent lorsque nous appliquons la théorie logique à des concepts du monde réel.

La manière dont nous définissons ces variables affecte nos tables de vérité.

Par exemple :

-   Si **P signifie "entrée valide"**, alors ¬P signifie "entrée invalide".
    
-   Si **P signifie "entrée invalide"**, alors ¬P signifie "entrée valide".
    

Imaginez que nous définissions **P = "Bonne entrée"** et **Q = "Pas d'erreur"**.

-   Lors du test du **happy path**, nous vérifions que l'implication **P⟹Q (Si l'entrée est bonne, alors pas d'erreur)** est vraie.
    
-   Lors du test du **unhappy path** (tests de mutation, plus de détails plus tard), nous vérifions que **¬P⟹¬Q (Si l'entrée n'est pas bonne, alors une erreur survient)** est vraie.
    

Dans n'importe quel test, un échec indique que l'implication testée est fausse. Cela justifie une enquête pour savoir si le problème réside dans l'interprétation des spécifications, l'implémentation, ou même le test lui-même.

## Appliquer la logique aux tests logiciels

Le développement de logiciels repose sur la construction de systèmes qui se comportent de manière prévisible. Les **tests logiciels** sont notre outil principal pour valider ces comportements. À la base, le test est un processus profondément ancré dans les implications logiques, où nous proposons une hypothèse sur notre code et exécutons ensuite une expérience (le test) pour vérifier sa véracité.

Un cas de test est soigneusement conçu pour évaluer une partie spécifique du code. Cela implique :

1.  **Mise en place des préconditions et des entrées :** Avant d'exécuter le code testé, nous établissons méticuleusement un environnement spécifique et fournissons des entrées particulières. Cela inclut :
    
    -   **Arguments de fonction/méthode :** Les valeurs précises transmises au code testé.
        
    -   **État du système :** Configuration des données pertinentes dans une base de données, préparation du contenu d'un système de fichiers, configuration des variables d'instance d'un objet, ou dictée des réponses des services externes (souvent via des "mocks" ou des "stubs").
        
    -   **Facteurs environnementaux :** Contrôle d'éléments comme l'heure actuelle, des conditions réseau spécifiques ou des permissions utilisateur pertinentes pour l'exécution du code. Cette configuration précise garantit que le code s'exécute dans des conditions définies, nous permettant d'évaluer son comportement de manière cohérente.
        

Une fois la configuration terminée, le code testé est exécuté, et sa sortie ou son comportement est observé. Cette observation est ensuite comparée à un **résultat attendu**.

Pour analyser précisément les résultats des tests, établissons notre mapping logique spécifique :

-   **P : Le code testé est correct pour le scénario spécifique défini par le test.** Cela se réfère à l'_état réel et objectif_ de la logique interne et de l'implémentation du code lorsqu'il est confronté aux préconditions et entrées du test. Si P est Vrai, le code est sans défaut pour ce cas. Si P est Faux, il y a un bug ou un écart.
    
-   **Q : Le test réussit.** Cela signifie que la sortie ou le comportement réel observé du code correspond précisément au résultat attendu défini dans notre cas de test. S'ils ne correspondent pas, le test échoue.
    
-   **P⟹Q : Si le code testé est correct pour ce scénario spécifique, alors le test réussira.** En logique propositionnelle pure, la valeur de vérité de P⟹Q est effectivement définie par les valeurs de vérité de P et Q. Mais dans le contexte des tests logiciels, P⟹Q représente notre **hypothèse ou spécification souhaitée** sur la manière dont le code _devrait_ se comporter. Nous ne "connaissons" pas directement la valeur de vérité de P à l'avance. Au lieu de cela, l'exécution du test fournit des données empiriques (le Q réel) qui nous permettent d'**évaluer si cette hypothèse tient en pratique**, et d'en inférer l'état réel de P.
    

Comprendre ce mapping est vital pour interpréter les résultats des tests. Examinons les différents résultats d'une exécution de test, en nous référant à la table de vérité pour P⟹Q :

| P | Q | P⟹Q | Interprétation dans les tests |
| --- | --- | --- | --- |
| Vrai | Vrai | Vrai | **Succès du test / Confirmation de la correction :** Le code est correct pour le scénario, et le test réussit comme prévu. Cela renforce notre confiance dans le fait que le code et le test sont tous deux corrects. |
| Vrai | Faux | Faux | **Contradiction logique / Falsification de l'hypothèse :** Le code _est_ correct pour le scénario, et pourtant le test échoue. Cette ligne signifie que notre hypothèse globale "P⟹Q" est _fausse_ pour cette instance spécifique. Cela nécessite une enquête : soit notre hypothèse initiale que P _était_ Vrai (signifiant que le code était correct) est fausse (c'est-à-dire qu'il y a un bug réel, donc P est en fait Faux), soit le test lui-même est défaillant (ses entrées/attentes sont incorrectes), soit la spécification est erronée. C'est ici que la "remise en question" de l'hypothèse P⟹Q elle-même a lieu. |
| Faux | Vrai | Vrai | **Faux positif / Test inadéquat :** Le comportement du code pour le scénario donné est _incorrect_, et pourtant le test réussit. C'est un scénario problématique. Il implique que le test n'est pas assez robuste pour détecter le défaut dans le code, ou que l'attente du test est erronée. Bien que P⟹Q reste vrai (vacueusement), ce résultat est trompeur et signifie que le test ne vérifie pas efficacement la correction du code. |
| Faux | Faux | Vrai | **Bug trouvé / Confirmation de l'incorrection :** Le comportement du code pour le scénario donné est _incorrect_, et le test échoue correctement. C'est un résultat bénéfique, car le test a identifié avec succès un défaut. Quand P est réellement Faux, P⟹Q est vacueusement vrai. Cette ligne peut représenter soit un état "P est Faux" connu et intentionnel (par exemple, la phase Red du TDD), soit l'_état réel découvert_ via déduction (**expliqué ci-dessous dans le Scénario 1**). |

![bc300c03-ce17-456d-9a7e-47c8e649cfd6](https://cdn.hashnode.com/res/hashnode/image/upload/v1750280931102/bc300c03-ce17-456d-9a7e-47c8e649cfd6.png)

### **Note sur cette table de vérité contextualisée et sa nature probabiliste**

Cette table de vérité diffère d'une table de vérité logique purement abstraite en étant explicitement contextualisée pour les tests logiciels.

-   **Définitions spécifiques :** Contrairement à un P et Q génériques, ils ont ici des significations précises dans le domaine de la correction du code et des résultats des tests.
    
-   **Colonne "Interprétation dans les tests" :** C'est la caractéristique distinctive clé. Elle traduit les résultats logiques bruts (P, Q et P⟹Q) en informations exploitables et en scénarios de débogage/développement courants pour les ingénieurs logiciels. Elle explique _ce que cela signifie_ lorsqu'une ligne particulière est observée dans le contexte des tests.
    
-   **Confiance probabiliste :** Alors que la logique formelle opère en binaire (Vrai/Faux), les tests logiciels du monde réel impliquent souvent une **confiance probabiliste**. Un test ne fournit pas une preuve logique absolue de correction (par exemple, un test réussi ne garantit pas que P est 100 % Vrai en raison de la possibilité de bugs non découverts ou de faux positifs). Au lieu de cela, les résultats des tests _augmentent notre confiance_ dans le fait que le code est correct, ou _fournissent des preuves solides_ qu'il est incorrect. Le test consiste fondamentalement à réduire l'incertitude et à augmenter la probabilité que notre code fonctionne comme prévu.
    

Explorons maintenant comment ces résultats logiques sont interprétés dans deux scénarios de test courants :

### Scénario 1 : Débogage d'un défaut inattendu (Application du Modus Tollens)

Ce scénario se produit lorsqu'un test qui réussissait auparavant, ou un nouveau test en lequel nous avons une grande confiance en tant que spécification précise et correcte, échoue de manière inattendue. Dans ce contexte, nous supposons la validité de l'implication P⟹Q pour ce cas de test spécifique, en la traitant comme une règle inviolable sur la manière dont un code correct _devrait_ se comporter.

1.  **Notre prémisse centrale (Spécification de confiance) :** Nous opérons sous l'hypothèse que l'implication "P⟹Q" ("Si le code est correct pour ce scénario, alors le test réussit") est **Vraie** pour ce test spécifique. Notre confiance provient de la conception méticuleuse du test, de son historique de succès ou de son rôle dans une suite de non-régression bien établie.
    
2.  **Exécution du test et observation :** Nous lançons le test, avec ses préconditions et ses entrées configurées.
    
    -   **Si le test échoue (Q est Faux) :** C'est l'observation clé. Puisque nous **faisons confiance à notre prémisse selon laquelle P⟹Q est Vrai**, et que nous observons ¬Q (le test échoue), nous sommes logiquement contraints de déduire que notre croyance initiale sur P (le code étant correct pour ce scénario) doit être fausse.
        
        -   **Application du Modus Tollens :**
            
            -   Prémisse 1 : Si le code est correct pour ce scénario (P), alors le test réussit (Q). (P⟹Q, supposé vrai en tant que spécification de confiance).
                
            -   Prémisse 2 : Le test n'a pas réussi (¬Q).
                
            -   Conclusion : Par conséquent, le **code n'est pas correct pour ce scénario (¬P).**
                
        -   **Résultat :** Cette inférence nous pointe directement vers un défaut dans le code. L'échec du test, compte tenu de sa nature fiable, _révèle_ que l'état réel du code pour ce scénario est **P est Faux**. Cela place effectivement le scénario dans la **Ligne 4 (P Faux, Q Faux)** de notre table de vérité, confirmant la présence d'un bug qui doit être corrigé. C'est typique des **tests de régression**, où une fonctionnalité précédemment correcte se casse soudainement.
            

### Scénario 2 : Validation/Affinage de la spécification (Falsification de P⟹Q ou confirmation d'une incorrection connue)

Ce scénario survient lorsqu'un test échoue, et que notre objectif principal n'est pas immédiatement de déboguer le code comme s'il s'agissait d'une régression. Au lieu de cela, il s'agit de comprendre _pourquoi_ la relation P⟹Q (notre hypothèse pour ce comportement spécifique) ne tient pas, ou simplement de confirmer un échec attendu. Cela peut impliquer de remettre en question le test lui-même, les exigences sous-jacentes, ou de confirmer un état délibérément incorrect du code.

1.  **Notre hypothèse (remise en question ou confirmée) :** Soit nous évaluons activement la validité de l'implication "P⟹Q" pour un comportement spécifique, soit nous exécutons un test contre un code que nous savons incomplet ou incorrect.
    
2.  **Exécution du test et observation :** Nous lançons le test avec ses préconditions et entrées définies.
    
3.  **Si le test échoue (Q est Faux) :** L'interprétation ici dépend de notre connaissance préalable ou de notre intention concernant l'état du code (P) :
    
    -   **Sous-scénario 2A : Falsification de P⟹Q et remise en question de la spécification (Correspond à la Ligne 2 : P Vrai, Q Faux) :**
        
        -   Nous observons que Q est Faux (le test échoue).
            
        -   Si nous examinons ensuite le code et les exigences, et que nous concluons que le code _aurait dû_ être correct pour ce scénario (signifiant que notre attente/croyance était que P est Vrai), alors le résultat du test signifie que **l'instance spécifique de notre hypothèse "P⟹Q" est FAUSSE.**
            
        -   Cette falsification directe révèle une contradiction. Nous devons alors enquêter :
            
            -   Notre croyance initiale que P était Vrai est-elle erronée (c'est-à-dire, y a-t-il un bug authentique dans le code qui rend P réellement Faux, déplaçant cela vers un scénario de Ligne 4) ?
                
            -   Ou bien, le test lui-même est-il incorrect (ses entrées ou sa sortie attendue sont fausses), ce qui signifie que notre prémisse P⟹Q doit être réévaluée et corrigée ?
                
            -   Ou encore, les exigences sous-jacentes ont-elles changé ou été mal comprises ?
                
        -   **Résultat :** Ce résultat critique nous incite à "repenser" – soit le code doit être corrigé, soit le test doit être ajusté, soit la spécification doit être clarifiée. C'est courant dans les **tests exploratoires** ou lors du travail sur de nouvelles fonctionnalités en évolution où le comportement exact est encore en cours de définition.
            
    -   **Sous-scénario 2B : Confirmation d'une incorrection connue (Correspond à la Ligne 4 : P Faux, Q Faux) :**
        
        -   Nous observons que Q est Faux (le test échoue).
            
        -   Nous _savons déjà ou avons intentionnellement conçu_ le code pour qu'il soit incorrect pour ce scénario (c'est-à-dire que nous développons activement une fonctionnalité et n'avons pas encore écrit tout le code, ou nous exécutons un test contre un bug connu non corrigé, donc notre attente est que P soit Faux).
            
        -   Le résultat du test **confirme simplement notre connaissance préalable que P est Faux**. Le test met correctement en évidence le comportement manquant ou incorrect. Dans ce cas, l'implication P⟹Q est vacueusement vraie, et le test a efficacement rempli son rôle en montrant le défaut existant.
            
        -   **Résultat :** C'est typique du Test-Driven Development (TDD) dans la phase Red, où un test échoué pour une fonctionnalité pas encore implémentée confirme l'état "P est Faux", guidant le développement pour rendre P Vrai. Cela s'applique également lors de la vérification qu'une correction de bug fonctionne réellement : le test échoue initialement (confirmant le bug), puis réussit après la correction (confirmant que P est maintenant Vrai).
            

![fille regardant dans un microscope](https://cdn.hashnode.com/res/hashnode/image/upload/v1749063701013/bc574591-90ec-4439-9b47-f0737d5a5384.jpeg)

## Un regard plus attentif sur les tests

### L'illusion de la correction : Affirmation du conséquent

Considérez un scénario courant où un test réussit, semblant valider notre code :

```python
def get_user_role(user_id):
    if user_id == 42:
        return "admin"
    return "guest"

# test
assert get_user_role(42) == "admin"
```

Ici, notre affirmation implicite (la spécification) est : **Si le code est correct (P), alors la sortie correspondra à l'attente (Q).**

Dans cet exemple, le test réussit – la sortie est "admin" **(Q)**, mais pouvons-nous conclure définitivement que la fonction est correcte **(P)** ? Pas nécessairement.

Ce scénario illustre souvent le sophisme logique de l'**affirmation du conséquent**. Nous voyons le résultat souhaité (Q) et supposons par erreur que notre cause spécifique prévue (P, la correction de _notre chemin d'implémentation spécifique_) en était la raison.

**Le problème :** Et si la condition réelle pour un rôle "admin" devait être la vérification d'une base de données, mais que nous avons temporairement codé la valeur en dur pour le test ? Le test réussirait, mais la correction est illusoire. Si nous considérons P comme faux parce que le code n'a pas implémenté le comportement de la spécification complète, cela correspond à la Ligne 3 (P Faux, Q Vrai : Faux positif) dans notre table de vérité.

Comme je l'ai mentionné plus tôt, implémenter délibérément ¬P fonctionne bien si ¬Q est observé, mais est inutile, voire erroné, si Q est observé.

Même sans codage en dur, la sortie pourrait correspondre par coïncidence, ou à cause de facteurs extérieurs à la logique directe que nous avions l'intention de tester. Cela peut arriver à cause de :

-   **Comportement par défaut :** Un défaut système plus large pourrait produire la sortie attendue.
    
-   **Mise en cache :** Une opération réussie précédente pourrait avoir mis le résultat en cache, contournant la logique réelle.
    
-   **Logique de repli (fallback) :** Un mécanisme de repli involontaire produit la sortie correcte malgré une erreur dans le chemin principal.
    
-   **Bugs dans le harnais de test :** Des failles dans la configuration du test lui-même pourraient masquer des problèmes réels.
    

### Le rôle et les risques des doublures de test

Les défis soulignés ci-dessus sont particulièrement pertinents lors de l'utilisation de **doublures de test** (test doubles), tels que les Stubs et les Mocks. Ce sont des composants artificiels qui remplacent les dépendances réelles (par exemple, bases de données, API externes, opérations sensibles au temps) pendant les tests.

-   Les **Stubs** se concentrent sur l'**état** : ils fournissent de fausses données préprogrammées ou des valeurs de retour pour que le reste du code testé fonctionne de manière prévisible, comme dans l'exemple `get_user_role`.
    
-   Les **Mocks** se concentrent sur le **comportement** : ils vous permettent de vérifier les interactions, comme le nombre d'appels faits à une certaine API, ou comment le flux de contrôle passe par des parties spécifiques du système.
    

Les deux suppriment les dépendances externes, vous permettant d'isoler et de vous concentrer sur la logique interne du code sans bruit ni effets secondaires. Mais les utiliser sans comprendre leurs limites peut mener à une **fausse confiance**.

Si une doublure de test simule une réponse "correcte", mais que la dépendance réelle qu'elle remplace a un bug, ou que la manière dont le code principal interagit avec cette dépendance est défaillante, le test réussira (Q est Vrai) – et pourtant P (la correction globale du code dans un environnement réel) pourrait être Faux, menant à un dangereux faux positif.

Le fait de rencontrer de tels sophismes logiques dans vos tests dépend précisément du comportement ou de l'état que vous tentez de vérifier, et de votre éventuelle surinterprétation des résultats des tests.

### Portée des tests et interprétation

Le choix de la portée des tests – des tests unitaires ciblés aux tests d'intégration plus larges, tests système, tests d'acceptation utilisateur (UAT), et même tests en production – représente un continuum. Sur ce spectre, divers compromis sont impliqués, notamment concernant le rapport effort-récompense. Cet effort est influencé par des facteurs tels que la compétence individuelle du développeur, les pratiques d'ingénierie de l'entreprise (par exemple, la répartition des responsabilités entre le développeur de fonctionnalités et le testeur dédié) et les réglementations de l'industrie.

Généralement :

-   **Les tests à portée réduite** (par exemple, les tests unitaires) comportent moins d'hypothèses intégrées et une chaîne d'implications logiques plus courte. Cela se traduit par moins de risques de commettre des sophismes tant dans l'implémentation du test que dans l'interprétation de ses résultats. Ils sont excellents pour vérifier rapidement des unités de code isolées.
    
-   **Les tests à portée plus large** (par exemple, les tests d'intégration de bout en bout) intègrent davantage de complexités et de dépendances du monde réel. Tout en offrant une plus grande confiance dans le comportement global du système, ils augmentent intrinsèquement le potentiel de facteurs de confusion pouvant mener à des faux positifs ou rendre le débogage plus difficile.
    

Être extrêmement conscient des hypothèses implicites dans chaque test, à chaque niveau de portée, est primordial. Faire réussir des tests pour les mauvaises raisons causera inévitablement des problèmes plus tard.

### Débogage, observabilité et modèles mentaux

Les tests qui échouent ne sont pas des échecs du processus de test mais sont, en fait, des moments d'apprentissage incroyablement précieux. Ils représentent des opportunités pour :

-   Exécuter des expériences de débogage ciblées pour identifier la cause exacte de l'échec.
    
-   Affiner votre **modèle mental du lien code-résultat (P⟹Q)**. Un test qui échoue (où Q est Faux) vous indique que votre compréhension actuelle de P, ou de la relation P⟹Q, est défaillante. Utilisez ce feedback pour mettre à jour votre compréhension du comportement réel du code.
    
-   Améliorer à la fois le code et les tests eux-mêmes.
    

Améliorez l'**observabilité** du système pour mieux détecter et confirmer les résultats (Q). Plus nous pouvons observer Q clairement, sous plusieurs angles et par diverses méthodes (par exemple, logs, métriques, tracing, inspection de sortie), plus nous pouvons être confiants dans ses causes et, par extension, dans l'état réel de P.

Surtout, évitez de corriger aveuglément les tests juste pour les faire réussir. Assurez-vous toujours de bien comprendre pourquoi un test a échoué et mettez à jour votre modèle P⟹Q en conséquence. L'objectif ultime n'est pas seulement de corriger les bugs actuels, mais de les prévenir à l'avenir en renforçant continuellement à la fois la correction du code et la vérifiabilité de son comportement.

### Les tests falsifiables révèlent les régressions

Au-delà de l'évitement des faux positifs (où le code est incorrect mais le test réussit), un bon test doit également être **falsifiable**. Cela signifie que le test doit être réellement capable d'échouer dans certaines conditions (incorrectes). Un test non falsifiable est un test cassé – il ne peut pas remplir son rôle de révéler des régressions ou de confirmer la présence de bugs.

Bien que nous nous efforcions de faire en sorte que l'implication P⟹Q soit vraie pour tous les scénarios qui nous importent, elle peut ne pas être vraie pour tous les cas en raison d'hypothèses imprévues ou erronées, ou simplement parce que le code est incorrect. La capacité du test à démontrer cette incorrection en échouant dans des conditions spécifiques et bien définies le rend profondément précieux.

Voici quelques coupables courants de tests non falsifiables ou "mauvais" :

-   **Spécifications vagues ou non testables :** Des affirmations comme "Le système doit bien se comporter dans la plupart des conditions", "Il ne devrait pas planter de manière aléatoire" ou "L'algorithme est robuste" manquent de critères clairs et mesurables. Il est impossible de concevoir un test qui réussit ou échoue définitivement par rapport à de telles affirmations, ce qui les rend effectivement non falsifiables.
    
-   **Implémentations défectueuses de la suite de tests :** Le code de test lui-même peut être défaillant, peut-être à cause d'erreurs logiques ou de problèmes de flux de contrôle qui empêchent les assertions d'être jamais atteintes ou correctement évaluées, empruntant par inadvertance le même chemin de succès quel que soit le code testé.
    
-   **Données de test ou cas limites insuffisants :** Si les tests ne couvrent que les scénarios du "happy path" et omettent d'inclure des entrées difficiles ou des conditions aux limites, ils pourraient réussir pour un code incorrect qui ne se casse que dans des circonstances spécifiques non testées.
    

Une spécification robuste définit clairement ce qui constitue un succès et un échec. En correspondance, une bonne suite de tests implémente correctement cette spécification, rendant ses tests à la fois précis et véritablement falsifiables.

### Prendre du recul

Les penseurs critiques pourraient observer que l'application des quatre formes d'arguments logiques fondamentaux aux scénarios de codage, telle qu'elle a été présentée initialement, pourrait être trompeuse face aux complexités des logiciels du monde réel.

La section suivante montre certaines nuances qui surviennent lorsque nous passons des règles tranchées de la logique formelle à la réalité souvent désordonnée du développement logiciel.

Plus précisément :

-   Les deux premiers points ci-dessous montrent pourquoi les arguments apparemment valides du Modus Ponens et du Modus Tollens peuvent ne pas toujours mener à des conclusions fiables lorsqu'ils sont appliqués à des scénarios de codage.
    
-   Les deux derniers points ci-dessous montrent pourquoi les deux sophismes logiques courants, l'affirmation du conséquent et la négation de l'antécédent, peuvent en fait fournir des informations correctes dans des conditions de codage réelles spécifiques.
    

## Retour sur les quatre énoncés pour le code

Voici les quatre arguments et leurs exemples de codage associés :

1.  **Modus Ponens :** Si vous fournissez des données d'entrée invalides (P), le code affichera une erreur (Q).
    
2.  **Modus Tollens :** Il n'y a pas de messages d'erreur (¬Q), donc les données d'entrée sont valides (¬P).
    
3.  **Affirmation du conséquent (Sophisme) :** Le code a affiché une erreur (Q), donc vous avez fourni des données invalides (P).
    
4.  **Négation de l'antécédent (Sophisme) :** Vous avez fourni des données valides (¬P), donc vous n'avez pas d'erreur (¬Q).
    

Maintenant, plongeons dans les nuances de chacun :

### Modus Ponens

-   **Notre exemple de codage :** Si vous fournissez des données d'entrée invalides (P), alors le code affichera une erreur (Q).
    
-   **Pourquoi il peut ne pas toujours tenir :** Cette application du Modus Ponens suppose que soit votre code, soit tout code tiers sur lequel il repose, détectera _toujours_ correctement et lèvera explicitement des exceptions ou affichera des erreurs sur des données erronées. En réalité, les systèmes peuvent corriger ou assainir (sanitize) automatiquement les mauvaises entrées, passer les erreurs sous silence, ou simplement continuer avec un comportement inattendu sans signaler explicitement d'erreur, menant à un état de succès (ou de non-échec) (¬Q) même quand P (entrée invalide) était vrai.
    

### Modus Tollens

-   **Notre exemple de codage :** Il n'y a pas de messages d'erreur (¬Q), donc les données d'entrée sont valides (¬P).
    
-   **Pourquoi il peut ne pas toujours tenir :** Cette application du Modus Tollens suppose qu'il n'y a pas de mécanismes automatiques dans le système pour corriger ou passer sous silence les mauvaises entrées _avant_ que les erreurs ne soient typiquement affichées. Si une telle "correction silencieuse" ou "suppression d'erreur" se produit, vous pourriez n'observer aucun message d'erreur (¬Q), mais les données d'entrée pourraient toujours être invalides (P), rendant la conclusion (¬P) fausse malgré la prémisse (¬Q) vraie. Cela souligne les dangers d'une observabilité incomplète.
    

### Affirmation du conséquent (Sophisme)

-   **Notre exemple de codage :** Le code a affiché une erreur (Q), donc vous avez fourni des données invalides (P).
    
-   **Pourquoi il peut en fait être correct :** Bien que logiquement ce soit un sophisme, dans des conditions réelles spécifiques et hautement contraintes, cette inférence peut acquérir une validité pratique. Si le message d'erreur est défini de manière si unique et spécifique qu'il ne peut être causé _que_ par des données d'entrée invalides (P) et aucun autre facteur connu, alors cet énoncé peut devenir fiable. C'est rare et cela nécessite généralement une conception méticuleuse de la gestion des erreurs où chaque message d'erreur correspond sans ambiguïté à une seule cause racine.
    

### Négation de l'antécédent (Sophisme)

-   **Notre exemple de codage :** Vous avez fourni des données valides (¬P), donc vous n'avez pas d'erreur (¬Q).
    
-   **Pourquoi il peut en fait être correct :** Bien qu'il s'agisse d'un sophisme en logique générale, cette inférence peut détenir un haut degré de confiance pratique sous certains paradigmes de programmation (**Programmation Fonctionnelle**). Si le code est suffisamment simple, purement fonctionnel (signifiant que les sorties dépendent _uniquement_ des entrées et n'ont pas d'effets secondaires) et n'a pas de dépendances externes (comme des interactions réseau ou base de données), alors l'absence de données invalides (¬P) peut effectivement nous rendre raisonnablement confiants qu'il n'y aura pas d'erreurs (¬Q). L'absence de variables externes et d'état interne rend le comportement du code hautement prévisible et directement lié à ses entrées.
    

![chien avec la tête penchée](https://cdn.hashnode.com/res/hashnode/image/upload/v1749061917858/db44dba5-2184-427a-8e28-27fc59904c49.jpeg)

Vous vous demandez peut-être maintenant : quel est l'intérêt d'étudier la logique si elle comporte autant de failles et de cas particuliers lorsqu'elle est appliquée au code ?

## L'ingrédient manquant - Si et seulement si

Dans notre exploration des implications logiques, nous nous sommes concentrés principalement sur la **relation unidirectionnelle** P⟹Q ("Si P, alors Q"). Cet énoncé nous dit ce qui se passe _si_ P est vrai, mais il reste muet sur le fait de savoir si Q se produit _uniquement_ quand P est vrai. C'est comme dire : "S'il pleut, le sol devient mouillé." C'est vrai, mais le sol peut aussi devenir mouillé si un arroseur est allumé, même s'il ne pleut pas.

Mais dans de nombreux contextes critiques, en particulier dans les théories scientifiques rigoureuses et les systèmes logiciels robustes, nous recherchons souvent une relation beaucoup plus forte : une relation où la vérité de Q _dépend_ absolument de la vérité de P, et vice versa. Cette puissante **relation bidirectionnelle** est capturée par l'expression "**Si et seulement si**" (P⟺Q).

### Ce que signifie "Si et seulement si" : un énoncé plus fort

Lorsque nous affirmons "P⟺Q", nous faisons deux affirmations distinctes simultanément :

1.  **Si P, alors Q** (P⟹Q) : P est une condition suffisante pour Q. Chaque fois que P est vrai, Q doit aussi être vrai.
    
2.  **Si Q, alors P** (Q⟹P) : P est aussi une condition nécessaire pour Q. Chaque fois que Q est vrai, P doit aussi être vrai. En d'autres termes, Q ne peut pas être vrai sans que P ne soit vrai.
    

Remarquez l'**augmentation significative de la force** de l'énoncé. "Si P, alors Q" énonce simplement une conséquence. "P⟺Q" déclare une **équivalence définitive**, où P et Q sont inextricablement liés. Ils s'élèvent et tombent ensemble – l'un ne peut être vrai sans que l'autre ne le soit, et l'un ne peut être faux sans que l'autre ne le soit.

### Table de vérité bidirectionnelle : des relations sans ambiguïté

Construisons la table de vérité pour P⟺Q pour voir clairement cette relation forte.

P⟺Q est logiquement équivalent à (P⟹Q)∧(Q⟹P).

![Table de vérité avec les colonnes P, Q, P->Q, Q->P, P<->Q](https://cdn.hashnode.com/res/hashnode/image/upload/v1747678444501/8d498249-eec2-46ca-a5c1-85801eb1b350.png)

#### Création de la table (les colonnes 4 et 5 sont nouvelles) :

-   **Q⟹P (Colonne 4) :** Nous appliquons les règles d'implication standard, mais avec Q comme "si" et P comme "alors". Par exemple, à la ligne 3, Q est Vrai et P est Faux, donc Q⟹P est Faux.
    
-   **P⟺Q (Colonne 5) :** C'est le **ET** logique des colonnes P⟹Q et Q⟹P. Pour que P⟺Q soit Vrai, les deux implications composantes doivent être Vraies, ce qui explique pourquoi vous voyez moins de "Vrai" dans l'implication bidirectionnelle par rapport à n'importe laquelle des implications unidirectionnelles.
    

### Implications pour les deux sophismes courants

La clarté fournie par le "Si et seulement si" est particulièrement puissante pour prévenir les sophismes logiques dont nous avons discuté précédemment : l'affirmation du conséquent et la négation de l'antécédent. Ces sophismes proviennent de l'hypothèse incorrecte qu'un énoncé "si-alors" implique une relation "si et seulement si".

Revisitons-les sous l'angle de **P⟺Q Si et seulement si vous avez fourni des données invalides (P), alors le code affichera une erreur (Q)** :

#### Affirmation du conséquent : plus d'ambiguïté

-   **Le sophisme (en supposant P⟹Q unidirectionnel) :**
    
    -   Si le code a affiché une erreur (Q), alors vous avez fourni des données invalides (P).
        
    -   Auparavant, quand P⟹Q était Vrai et Q était Vrai, P pouvait être Vrai (Ligne 1) ou Faux (Ligne 3). Cette ambiguïté menait au sophisme.
        
-   **Avec P⟺Q :**
    
    -   Maintenant, regardez la colonne P⟺Q dans le tableau. Quand P⟺Q est Vrai et Q est Vrai (Ligne 1), P est **sans ambiguïté Vrai**. La confusion de la ligne 3 a disparu car si Q était Vrai alors que P était Faux, P⟺Q serait Faux (car Q⟹P serait Faux), rendant cette ligne non pertinente pour une inférence modus ponens valide sous la prémisse P⟺Q.
        
    -   Dans un système conçu avec P⟺Q à l'esprit, savoir que Q est Vrai (observer une erreur) **forcerait** la conclusion que P est Vrai (les données invalides sont la cause), en supposant que la relation "si et seulement si" tient pour cette conception de système spécifique.
        

#### Négation de l'antécédent : conséquences indéniables

-   **Le sophisme (en supposant P⟹Q unidirectionnel) :**
    
    -   Vous avez fourni des données valides (¬P), donc vous n'avez pas d'erreur (¬Q).
        
    -   Auparavant, quand P⟹Q était Vrai et P était Faux, Q pouvait être Vrai (Ligne 3) ou Faux (Ligne 4). Cette ambiguïté menait au sophisme.
        
-   **Avec P⟺Q :**
    
    -   Maintenant, quand P⟺Q est Vrai et P est Faux (Ligne 4), Q est **sans ambiguïté Faux**. Le scénario problématique de la ligne 3 (où P était Faux mais Q était Vrai) est ici non pertinent car P⟺Q serait Faux dans ce cas (plus précisément, Q⟹P serait Faux).
        
    -   Si votre système adhère véritablement à "P⟺Q", alors savoir que P est Faux (données valides fournies) **garantit** que Q est Faux (pas de messages d'erreur).
        

### Atténuation pratique dans le code

Les enseignements du "Si et seulement si" sont plus que théoriques. Pratiquement, les deux sophismes (affirmation du conséquent et négation de l'antécédent) peuvent être atténués en s'efforçant d'établir des conditions qui se rapprochent d'une relation "si et seulement si" dans votre code et vos tests.

#### Tests unitaires ciblés

Concevez des tests unitaires si granulaires et isolés qu'ils visent effectivement à établir un scénario "si et seulement si" pour une minuscule partie de la logique. En utilisant des mocks ou en contrôlant rigoureusement toutes les dépendances externes et les facteurs environnementaux, vous réduisez l'impact des "autres causes".

Si votre test pour une entrée spécifique réussit, vous voulez être aussi confiant que possible qu'il a réussi _uniquement_ parce que le code a géré cette entrée spécifique correctement, et non à cause d'un effet secondaire non pertinent. De même, s'il échoue, vous voulez être sûr que l'échec pointe directement vers le chemin logique prévu.

#### Gestion des exceptions et spécificité

Au lieu de capturer des types `Exception` larges, capturez et gérez des exceptions spécifiques. Cela aide à différencier les diverses "causes" (P1, P2, …) qui pourraient mener à une "erreur" générique (Q). Plus votre gestion des erreurs est précise, plus vous vous rapprochez d'un scénario où "Si erreur X, alors cause spécifique Y", tendant vers une compréhension bidirectionnelle des conditions d'erreur.

#### Test-Driven Development (TDD) et tests de mutation

Ces méthodologies poussent intrinsèquement vers une pensée P⟺Q. Le TDD encourage l'écriture d'un test échoué _d'abord_ (¬Q), ce qui nécessite _ensuite_ un changement de code spécifique (P) pour le faire réussir.

Les tests de mutation, que nous explorerons plus loin, vont encore plus loin en garantissant que vos tests sont assez robustes pour _échouer_ quand le code est subtilement altéré (c'est-à-dire en prouvant que ¬P mène à ¬Q, et donc que le P original était bien nécessaire pour Q).

En visant consciemment des relations "si et seulement si" dans la conception de votre code et vos stratégies de test, vous pouvez construire des systèmes qui sont non seulement prévisibles mais aussi beaucoup plus faciles à déboguer et à analyser, passant de la simple corrélation à une compréhension profonde de la cause et de l'effet.

### Rappel sur les tests de mutation

Dans la section précédente sur l'**Assignation de significations concrètes à la logique**, nous avons discuté :

> Lors du test du **happy path**, nous vérifions que l'implication **P**⟹**Q (Si l'entrée est bonne, alors pas d'erreur)** est vraie.
> 
> Lors du test du **unhappy path (tests de mutation)**, nous vérifions que **¬P**⟹**¬Q (Si l'entrée n'est pas bonne, alors une erreur survient)** est vraie.

Cette double vision est la clé pour comprendre comment les tests de mutation contribuent à la justesse du logiciel.

![représentation artistique de structures moléculaires](https://cdn.hashnode.com/res/hashnode/image/upload/v1749063165908/e1e3736c-75dd-4f1f-81bb-fd7d4f4f7837.jpeg)

## Tests de mutation : tester les tests

Les tests de mutation introduisent délibérément de petits défauts (mutations) dans le code et vérifient si la suite de tests les détecte en échouant. Ce processus évalue non pas le _code_, mais les _tests eux-mêmes_.

Dans une suite de tests robuste, nous visons deux conditions idéales :

-   Toutes les implémentations **correctes** doivent **réussir** les tests.
    
-   Toutes les implémentations **incorrectes** doivent **échouer** aux tests.
    

Si une version mutée (erronée) du code est introduite et ne provoque aucun échec de test, cela va à l'encontre de l'objectif fondamental du test. Cela signifie que vos tests ne sont pas assez sensibles pour détecter un écart par rapport à la correction. Les mutations révèlent des hypothèses cachées ou des lacunes dans votre couverture de tests, agissant comme une sonde de sensibilité pour votre suite de tests.

**Exemples de mutations de code :**

-   Changer un opérateur arithmétique (`+` en `-`, `>` en `>=`).
    
-   Inverser une condition booléenne (`true` en `false`).
    
-   Supprimer ou dupliquer une instruction.
    
-   Modifier une valeur constante.
    

**Outils de tests de mutation Python courants :**

-   **mutmut** utilise le module `ast` intégré de Python.
    
-   **cosmic-ray** utilise `parso`, qui fournit un AST plus complet.
    

Ces outils s'appuient sur les arbres de syntaxe abstraite (AST) pour muter chirurgicalement le code.

Vous pouvez même échanger les bibliothèques AST sous-jacentes pour une précision ou une exhaustivité différente : [https://github.com/boxed/mutmut/issues/281][23]

### Logique derrière les tests de mutation

Formalisons le mapping logique des tests de mutation, en rappelant nos définitions :

-   Soit P : Le code est correct.
    
-   Soit Q : Les tests réussissent.
    

Le **test standard du happy path** vérifie principalement que P⟹Q – "si le code est correct, alors les tests réussissent".

Les **tests de mutation** se concentrent sur l'autre face de la pièce : nous rendons intentionnellement ¬P vrai (en introduisant un défaut), puis nous attendons ¬Q (les tests doivent échouer). Ce processus vérifie rigoureusement si l'implication ¬P⟹¬Q ("si le code n'est _pas_ correct, alors les tests _échouent_") est vraie pour votre suite de tests.

Mais il y a une implication logique plus profonde et plus puissante ici :

Comme nous l'avons appris plus tôt, l'énoncé ¬P⟹¬Q est **logiquement équivalent** à sa **contraposée**, Q⟹P.

Ainsi, en vérifiant avec succès que l'introduction d'un défaut (¬P) mène à un échec de test (¬Q), nous validons simultanément la contraposée : `si les tests réussissent (Q), alors le code doit être correct (P)`.

C'est incroyablement significatif ! Cela nous rapproche beaucoup de l'établissement d'une **garantie bidirectionnelle** entre notre code et nos tests : P⟺Q (la correction du code est étroitement couplée au succès des tests). Les tests de mutation nous aident à éliminer avec confiance les faux positifs dans la suite de tests – des situations où Q est vrai (le test réussit) mais P est faux (le code est en fait incorrect).

Dans un monde où les LLM nous aident à écrire et à refactoriser le code rapidement, avoir cette confiance en "si et seulement si" dans notre suite de tests est inestimable pour garantir que le code généré ou refactorisé répond véritablement aux attentes.

### **Clarification sur les types d'échecs**

En informatique, nous catégorisons généralement les erreurs en trois types principaux :

-   **Erreurs de syntaxe :** Violations des règles grammaticales du langage (par exemple, deux-points manquants, mot-clé invalide). Celles-ci empêchent le code de s'exécuter.
    
-   **Erreurs d'exécution (runtime) :** Erreurs qui surviennent pendant l'exécution du programme, souvent dues à des conditions inattendues (par exemple, `TypeError`, `AttributeError`, `ZeroDivisionError`).
    
-   **Erreurs de logique :** Le programme s'exécute sans planter, mais il produit un résultat incorrect ou se comporte d'une manière qui ne correspond pas à la spécification prévue (par exemple, mauvais algorithme, mauvaise valeur de retour).
    

Les tests de mutation se concentrent sur les **erreurs de logique** – des défaillances où le programme s'exécute, mais produit des résultats incorrects. Celles-ci sont généralement capturées via `AssertionError` dans la phase "Assert" du pattern de test Arrange–Act–Assert (AAA).

On pourrait arguer de manière pédante que `AssertionError` est une erreur d'exécution, mais dans les tests, nous la traitons comme un **signal de défaillance logique** :

> _"La fonction s'est exécutée, mais la sortie ne correspondait pas au comportement attendu."_

Les tests de mutation supposent que les erreurs de syntaxe et d'exécution sont déjà gérées. Leur but est de valider si la suite de tests capture de manière fiable les mauvais comportements logiques.

### Une perspective de falsification plus profonde

Maintenant, connectons les tests de mutation au **principe de falsification de Karl Popper**, que nous avons introduit plus tôt dans le contexte du raisonnement scientifique. Rappelez-vous que Popper soutenait que les théories scientifiques gagnent en force non pas en étant "prouvées", mais en _survivant à des tentatives rigoureuses de réfutation_. L'idée centrale de la logique de falsification est que pour infirmer une implication comme P⟹Q, il suffit de trouver une seule instance où P est Vrai et Q est Faux.

Les tests de mutation appliquent ce même principe puissant à l'efficacité de notre suite de tests :

Au lieu d'essayer de _prouver_ directement que nos tests sont parfaits, les tests de mutation adoptent une approche de falsification de l'implication **¬P⟹¬Q ("Si le code est incorrect, alors les tests échouent").** Ils tentent activement de **falsifier** cette relation cruciale.

Si nous introduisons une mutation (rendant ¬P vrai, c'est-à-dire que le code est maintenant incorrect) mais que la suite de tests existante _réussit toujours_ (signifiant que Q est vrai), alors nous avons trouvé une instance où :

1.  ¬P est Vrai (le code est incorrect à cause de la mutation).
    
2.  Q est Vrai (le test réussit toujours).
    

Dans ce scénario, l'implication **¬P⟹¬Q est falsifiée** car nous avons un antécédent Vrai (¬P) menant à un conséquent Faux (¬Q est faux, car Q est vrai).

Et, de manière critique, si ¬P⟹¬Q est falsifiée, alors sa contraposée logiquement équivalente, Q⟹P ("Si les tests réussissent, alors le code est correct"), est _également_ falsifiée. Cela signifie que nous ne pouvons plus avoir confiance dans le fait qu'une suite de tests réussie indique de manière fiable un code correct. Notre relation P⟺Q souhaitée est rompue – **la suite de tests n'est plus pleinement efficace** pour garantir la justesse.

En poussant pour zéro mutant survivant, les tests de mutation nous forcent à minimiser la surface de ces "hypothèses cachées" dans notre suite de tests. Ils exigent des tests hautement sensibles et spécifiques capables de détecter même des failles logiques subtiles, nous rapprochant ainsi de la construction de systèmes véritablement résilients.

### Comparaison entre le TDD (Phase Red) et les tests de mutation

Les deux méthodologies, bien que par des moyens différents et à des étapes différentes du cycle de développement, visent à établir la confiance dans la relation **¬P ⟹ ¬Q**.

**Résumé des différences clés :**

| Caractéristique | TDD (Phase Red) | Tests de mutation |
| --- | --- | --- |
| **Objectif principal** | Piloter le développement de nouveau code. Confirmer un bug/une fonctionnalité. | Évaluer la qualité/l'exhaustivité des tests existants. |
| **État du code** | Le code de production est incomplet ou buggé. | Le code de production est (supposé) correct. |
| **État du test** | Le _nouveau_ test est censé échouer. | Les tests _existants_ sont censés échouer (à cause des mutants). |
| **Initiateur** | Développeur voulant ajouter une fonctionnalité/corriger un bug. | Outil qui insère des bugs artificiels dans le code. |
| **"Bugs"** | Bugs réels, intentionnels ou fonctionnalités manquantes. | Changements artificiels et subtils dans le code. |

## Vers une confiance en "si et seulement si"

En fin de compte, l'objectif du développement logiciel est d'établir des relations "si et seulement si" chaque fois que possible, tant dans l'implémentation du code que, surtout, dans la sensibilité de la suite de tests au code testé.

Cela signifie que **si une certaine condition (P) est vraie, alors un résultat spécifique (Q) _doit_ se produire, et si Q se produit, alors P _doit_ en avoir été la cause**. Atteindre ce niveau de clarté provient de :

-   Une compréhension approfondie du problème.
    
-   Des attentes alignées lors du recueil des exigences.
    
-   L'analyse logique et l'interprétation d'expériences bien conçues.
    
-   Le respect du Principe de Responsabilité Unique (SRP) dans SOLID.
    
-   Des tests rigoureux avec une couverture significative.
    

Cela nous permet de comprendre comment le **flux de contrôle** et le **flux de données** fonctionnent avec plus de profondeur et de confiance, menant à de meilleures inférences tout au long du cycle de vie du développement logiciel.

![Papillon Monarque posé sur une fleur de buddléia](https://cdn.hashnode.com/res/hashnode/image/upload/v1749062596293/9bfb566a-5e3c-4fec-ac42-326aa22532c8.jpeg)

## Les défis du monde réel

Bien que la recherche de relations parfaites "si et seulement si" fournisse un idéal logique puissant, la réalité désordonnée du développement logiciel moderne présente des obstacles importants. Les caractéristiques mêmes qui rendent les grands systèmes puissants et évolutifs – leurs interconnexions complexes et leur dynamisme inhérent – obscurcissent simultanément les relations claires de cause à effet, faisant du raisonnement logique précis et du débogage une bataille permanente.

### Un réseau de complexité

#### Fan-In, Fan-Out : La nature des systèmes modernes

Tout système logiciel d'une taille raisonnable fonctionne rarement par des flux de contrôle et de données purement linéaires. Les patterns de fan-out et fan-in – où de nombreux composants sont appelés puis leurs résultats fusionnés – sont inévitables.

Par exemple :

-   Dans les **pipelines ETL**, les données peuvent être ingérées à partir de multiples sources (API externes, CSV) et journalisées vers de multiples destinations (fichiers, bases de données).
    
-   Dans la **programmation concurrente**, le `ProcessPoolExecutor` de Python divise les données en morceaux traités en parallèle, puis recombine les résultats.
    

#### Le SRP rencontre les frontières du monde réel

Tout comme la programmation fonctionnelle doit éventuellement effectuer des E/S, le **Principe de Responsabilité Unique (SRP)** se heurte à des frontières réelles, qu'elles soient conceptuelles ou infrastructurelles. À un moment donné, quelque chose doit lier ces unités isolées.

La logique d'orchestration peut résider dans une seule fonction, s'étendre sur plusieurs fichiers, ou même être distribuée sur des microservices et des machines communiquant via des réseaux. Bien que cette décomposition améliore la modularité, elle augmente également la surface d'exposition aux bugs impliquant :

-   **Effets secondaires :** Changements involontaires de l'état du système en dehors des sorties explicites d'un composant.
    
-   **Dépendances circulaires :** Composants s'appuyant les uns sur les autres en boucle, menant à des comportements difficiles à tracer.
    
-   **Dérive d'interface :** Changements dans les attentes d'entrée/sortie d'un composant non répercutés correctement ailleurs.
    
-   **Conditions de concurrence (race conditions) :** Bugs dépendant du timing dans les opérations concurrentes.
    
-   **Problèmes de sérialisation :** Problèmes de traduction des données entre différents formats ou systèmes.
    
-   **Manque de fiabilité du réseau :** Latence imprévisible, perte de paquets ou déconnexions dans les systèmes distribués.
    

#### L'épée à double tranchant de l'abstraction

Ce réseau de dépendances est le prix du progrès, rendu gérable uniquement grâce à de meilleurs outils et abstractions.

-   Si les frontières sont **bien conçues, observables et testables**, elles permettent une collaboration asynchrone, améliorent la maintenabilité à long terme et augmentent la confiance des développeurs. (Voir le GitHub Playbook dans les Références).
    
-   Si les systèmes **manquent de cohérence architecturale** ou sont dépassés par l'évolution des besoins, ils se calcifient en une dette technique qui démoralise même les équipes les plus motivées.
    

#### Le code propre est contextuel

Bien que les abstractions et l'orchestration aident à gérer la complexité, l'utilisation excessive de design patterns ou la création de couches de classes inutiles peut introduire une indirection superflue. C'est un contre-argument courant au purisme architectural.

En fin de compte, ce qui compte comme "code propre" dépend du contexte. Cela varie selon les compétences du programmeur, les outils à disposition (linters, tests, Copilot), et si le projet est un script jetable ou un investissement d'infrastructure sur plusieurs années. Les pratiques architecturales comme le SRP devraient évoluer parallèlement à ces contraintes.

### L'effet papillon des bugs

#### Du SRP aux chaînes de raisonnement

Auparavant, nous nous sommes concentrés sur une logique de cause à effet simple et directe (P ⟹ Q), mais les systèmes du monde réel sont plus désordonnés.

Plus nous adhérons au SRP via de petites fonctions ciblées, plus nous créons de longues chaînes de logique. Cela améliore la séparation des préoccupations mais prolonge également le raisonnement requis pour déboguer un comportement.

#### Déboguer dans un brouillard causal

Un déclencheur apparemment mineur (O) peut cascader à travers une chaîne comme O⟹P⟹Q⟹R, que nous pourrions ne pas comprendre pleinement en raison des silos de connaissances, de l'évolution des exigences ou du dynamisme au moment de l'exécution.

Même quand nous comprenons les composants, identifier précisément "P" est difficile, tout comme la redéfinition d'une question de recherche déplace la population statistique étudiée. Dans les systèmes complexes avec des **boucles de rétroaction** (moteurs de recommandation), il se peut qu'il n'y ait pas du tout de "cause racine" unique.

#### Triage à court terme vs vision à long terme

Trouver l'origine réelle d'un bug exige souvent de l'expérimentation, de la télémétrie et une vision globale du système. Ces investigations produisent des corrections robustes et pérennes, mais prennent du temps.

Dans les scénarios d'astreinte, cependant, l'urgence redéfinit les priorités. Les atténuations rapides et une communication claire prennent souvent le pas sur un diagnostic approfondi.

### Masqué par la conception et la dette

À mesure que les systèmes se développent, la défaillance ne ressemble plus à un crash. Au lieu de cela, elle se manifeste par un pic de tentatives (retries), une dérive lente des métriques ou un comportement de repli silencieux.

Les systèmes modernes tolérants aux pannes, construits avec des retries, des basculements (failovers), des coupe-circuits (circuit breakers) et de l'autoscaling, sont conçus pour récupérer rapidement. Cette résilience masque souvent des problèmes plus profonds, retardant la détection pendant des semaines et rendant l'analyse des causes racines plus difficile.

Opérer dans des **environnements non déterministes** avec des réseaux capricieux, des conditions de concurrence ou un routage dynamique ajoute une ambiguïté supplémentaire. Les petits symptômes deviennent plus difficiles à relier à des causes spécifiques.

Pour couronner le tout, la **dette technique** alimentée par un leadership technique faible, des priorités changeantes ou la pression du temps affaiblit l'observabilité du système et sa couverture de tests. Les équipes héritent d'un code fragile et mal compris, ce qui rend difficile le tracé de lignes claires entre cause et effet.

Même les meilleurs ingénieurs luttent dans de telles conditions. Lorsqu'un système résiste à la clarté, il ne bloque pas seulement le débogage. Il érode la confiance, ralentit l'apprentissage et alimente l'épuisement professionnel à long terme.

## Lueurs d'espoir : outils et pratiques pour la clarté

Malgré ces défis, plusieurs stratégies et pratiques offrent une voie vers des logiciels plus robustes et compréhensibles.

### Tirer parti des Design Patterns

Les design patterns offrent un vocabulaire partagé et des stratégies éprouvées pour structurer les systèmes. Lorsqu'ils sont bien appliqués, ils domptent la complexité, réduisent la dette technique et rendent le comportement plus prévisible.

Ils ont également tendance à concentrer des modes de défaillance similaires. Le même bug peut apparaître dans différentes entreprises ou industries, créant une richesse de connaissances préalables et de guides de solutions. La familiarité avec les patterns peut accélérer le débogage et approfondir la compréhension partagée au sein des équipes.

### Favoriser le mentorat expert

Promouvoir des mentors sur la base d'un impact technique réel plutôt que sur l'ancienneté permet de bâtir des équipes plus fortes et d'éviter le **Principe de Peter** (les gens dans une hiérarchie ont tendance à s'élever jusqu'à un niveau d'incompétence respective).

Les grands mentors enseignent plus que des compétences – ils modélisent la falsifiabilité, la pensée indépendante et la capacité à raisonner dans l'incertitude.

Ils aident les autres à remettre en question les hypothèses, à naviguer dans les compromis et à grandir tant sur le plan technique qu'interpersonnel. Dans les systèmes où les causes racines sont floues, ce type de leadership est essentiel.

L'une des techniques les plus puissantes qui s'étend du mentorat au code est la **falsification** : la recherche disciplinée de contre-exemples. Qu'elle soit appliquée dans les revues de conception, les sessions de débogage ou les tests automatisés, cet état d'esprit ancre le raisonnement dans la réalité.

## Le pouvoir de la falsification dans les tests

La recherche délibérée de contre-exemples est au cœur de la construction de systèmes fiables.

-   Dans la conception d'algorithmes, tester les cas limites n'est que de la falsification déguisée : trouver où votre logique se brise.
    
-   Dans le code, le **fuzz testing** (Atheris) envoie des entrées diverses aux fonctions pour exposer des exemples falsificateurs.
    
-   Le **property-based testing** (Hypothesis) va plus loin en générant des entrées qui satisfont certaines règles, puis réduit les échecs à leur forme minimale. Cela améliore considérablement la reproductibilité et aide à tester les problèmes de concurrence.
    

Plus nous tentons rigoureusement de falsifier nos hypothèses, plus nous pouvons raisonner avec confiance sur le comportement en utilisant des outils comme le Modus Ponens et le Modus Tollens.

Les hypothèses sont toujours présentes dans les logiciels pour simplifier la complexité. La question est de savoir si elles sont **explicitement codifiées dans les tests** ou **laissées cachées et fragiles**.

Bien sûr, aucun test n'est jamais infaillible : nos hypothèses pourraient être erronées, ou le monde pourrait changer. C'est pourquoi la pensée critique, le discernement entre "ce qui devrait être" et "ce qui est", reste essentiel alors que les nouvelles générations s'appuient de plus en plus sur des outils d'IA comme les grands modèles de langage (LLM).

Cette approche délibérée, **axée sur la falsification**, est primordiale pour construire des logiciels fiables. Elle sous-tend des techniques de test sophistiquées conçues pour exposer les hypothèses cachées et briser nos chaînes logiques.

Bien que les tests nous aident à découvrir où notre raisonnement pourrait faiblir, certains domaines exigent un degré de certitude encore plus élevé. Pour ces systèmes critiques, nous nous tournons vers les outils ultimes de la rigueur logique : les **Assistants de preuve**.

![rangée de dominos](https://cdn.hashnode.com/res/hashnode/image/upload/v1749062895395/f92ed2e7-f1fd-4351-a9d3-12c436c989f1.jpeg)

## Assistants de preuve

Alors que les tests traditionnels et le fuzzing sont puissants pour trouver des bugs, ils ne peuvent fondamentalement pas garantir la justesse pour toutes les entrées ou tous les scénarios possibles. Ils ne peuvent prouver que la _présence_ de bugs, pas leur _absence_.

Pour obtenir des preuves formelles et mathématiquement vérifiées du comportement d'un programme – fournissant les garanties les plus solides possibles – nous nous tournons vers les **assistants de preuve**. Ces outils nous permettent de construire des preuves logiques étape par étape, garantissant qu'un programme ou une conception de système adhère à sa spécification avec une rigueur absolue.

### **Prolog**

Prolog offre un point d'entrée relativement simple dans le monde de la programmation logique et de la démonstration de théorèmes. **SWI-Prolog** est un interpréteur courant (un **REPL**, ou Read-Eval-Print Loop) pour Prolog.

Vous interagissez avec Prolog en lui fournissant une base de connaissances composée de `faits` (facts) et de `règles` (rules) (qui sont un type de clause logique appelée **clauses de Horn**). Vous posez ensuite des `requêtes` (queries).

#### Installation de SWI-Prolog

Vous pouvez télécharger SWI-Prolog sur son site officiel : [https://www.swi-prolog.org/download/stable][24]  
Suivez les instructions pour votre système d'exploitation (Windows, macOS ou Linux).

Sur Ubuntu/Debian, vous pouvez généralement l'installer via :

```bash
sudo apt update
sudo apt install swi-prolog
```

#### Utilisation de Prolog : REPL vs Fichier

-   Le **REPL (**`swipl`) est idéal pour : Des tests rapides et interactifs de faits ou de règles uniques, et pour poser des requêtes à une base de connaissances _déjà chargée_.
    
-   **Un fichier (**extension `.pl`) est idéal pour : Définir votre **base de connaissances entière** (plusieurs faits et règles) et stocker votre programme pour qu'il soit réutilisable. C'est la manière standard de travailler avec Prolog pour tout ce qui dépasse quelques lignes.
    

#### Exemple : Une base de connaissances simple

Définissons une base de connaissances pour représenter qui a un emploi et qui est un instructeur de code.

**1. Créez un fichier** nommé `knowledge.pl` avec le contenu suivant :

```prolog
% knowledge.pl
% Ce fichier définit une petite base de connaissances en Prolog.
% En Prolog, toutes les déclarations (faits et règles) sur le même prédicat
% (identifié par son nom ET son nombre d'arguments, par ex., 'has_job' avec 1 argument est 'has_job/1')
% doivent être écrites consécutivement sans autres définitions de prédicats entre les deux.

% --- Définitions pour le prédicat 'has_job' (prend 1 argument) ---

% Fait : Alice a un emploi.
has_job(alice).

% Fait : Bob a un emploi.
has_job(bob).

% Règle : Quiconque (représenté par la variable X) a un emploi S'IL est un instructeur de code.
% ':-' signifie 'si'. 'X' est une variable (commence par une majuscule).
has_job(X) :- is_coding_instructor(X).

% --- Définitions pour le prédicat 'is_coding_instructor' (prend 1 argument) ---

% Fait : Alice est un instructeur de code.
is_coding_instructor(alice).
```

**Ce que fait chaque ligne :**

-   Lignes commençant par `%` : Ce sont des commentaires pour la lisibilité humaine, ignorés par Prolog. Ils expliquent le but du fichier et les règles clés comme le regroupement des prédicats.
    
-   `has_job(alice).` / `has_job(bob).` : Ce sont des faits. Ils affirment des vérités simples, comme "Alice a un emploi". Le `.` à la fin est obligatoire pour chaque instruction.
    
-   `has_job(X) :- is_coding_instructor(X).` : C'est une règle. Elle énonce une vérité conditionnelle : "Pour tout `X`, `X` a un emploi _si_ `X` est un instructeur de code." `X` est une variable (commence toujours par une majuscule), et `:-` signifie "si". Cette règle permet à Prolog de déduire de nouvelles informations.
    
-   `is_coding_instructor(alice).` : Un autre fait, affirmant "Alice est un instructeur de code". Il est placé après toutes les clauses `has_job/1` pour satisfaire la règle de regroupement de Prolog.
    

**2. Charger et interroger dans le REPL :**

Ouvrez votre terminal et tapez `swipl`. Une fois à l'invite `?-`, chargez le fichier puis posez vos requêtes :

```prolog
$ swipl
?- [knowledge].   % Charge le fichier 'knowledge.pl' (omettre .pl, utiliser des crochets et un point)
% Appuyez sur Entrée. Prolog confirmera qu'il a chargé le fichier, par ex., '% knowledge.pl compiled...'
True.

?- has_job(alice). % Requête : Est-ce qu'Alice a un emploi ?
% Appuyez sur Entrée. Prolog vous donne une solution, puis attend.
True.              % Sortie : Oui, parce que c'est un fait.
% Après 'True.', vous verrez à nouveau l'invite '?- ', indiquant que Prolog est prêt pour votre prochaine requête.
% S'il y avait plusieurs façons de prouver 'True.', Prolog présenterait le premier 'True.' puis attendrait que vous appuyiez sur ';' pour les alternatives, puis Entrée pour confirmer le 'True.' ou 'False.' final.

?- has_job(carol). % Requête : Est-ce que Carol a un emploi ?
% Appuyez sur Entrée.
False.             % Sortie : Non, Prolog ne peut pas le prouver à partir de ses connaissances.

?- has_job(X).     % Requête : Qui a un emploi ? (Trouver les valeurs pour X)
% Appuyez sur Entrée
X = alice ;        % Prolog trouve Alice comme première solution. Tapez ';' et Entrée pour demander la solution suivante.
X = bob ;          % Il trouve Bob. Tapez ';' et Entrée pour la solution suivante.
X = alice          % Il trouve à nouveau Alice (cette fois déduit via la règle et is_coding_instructor(alice)).
% Appuyez sur Entrée. Cela accepte l'ensemble actuel de solutions et arrête la recherche.
False.             % Sortie : Indique qu'aucune autre solution n'a été trouvée après le dernier 'Entrée' (ou si vous avez explicitement choisi de ne pas chercher plus loin).

?- halt.           % Tapez 'halt.' pour quitter proprement le REPL Prolog.
% Alternativement, vous pouvez souvent utiliser Ctrl+D pour quitter la plupart des REPL.
```

**L'exemple Prolog démontre clairement :**

-   **"Est-ce que P(X) est vrai pour un X spécifique ?"** : Montré par `?- has_job(alice).` (renvoie `True.`) et `?- has_job(carol).` (renvoie `False.`).
    
-   **"Existe-t-il un X pour lequel P(X) est vrai ?"** : Montré par `?- has_job(X).` (fournit des solutions comme `X = alice`, `X = bob`).
    

#### Limitations de Prolog

Les limitations de Prolog deviennent évidentes lorsqu'on tente de raisonner sur la fausseté ou la non-existence. **Vous ne pouvez pas demander directement "Existe-t-il un X pour lequel P(X) est faux ?"**

Au lieu de cela, Prolog fonctionne sur le principe de la négation par l'échec (negation as failure). Cela signifie que si Prolog ne peut pas prouver un énoncé, il considère cet énoncé comme faux.

Par exemple, si vous demandez `?- \+ has_job(carol).` (signifiant "N'est-il pas vrai que Carol a un emploi ?"), Prolog dira True, car il ne peut tout simplement trouver aucune preuve que Carol a un emploi dans sa base de connaissances.

C'est une distinction importante : cela ne signifie pas que Carol n'a définitivement pas d'emploi, et Prolog ne fournit pas non plus de contre-exemple formel. Cela reflète simplement un manque d'informations prouvables.

Cette contrainte fondamentale signifie que Prolog, bien que puissant pour la programmation logique, n'est pas un assistant de preuve complet pour une vérification formelle exhaustive.

### **Coq**

Après avoir expérimenté Prolog et vu ses limites, vous pouvez passer à un assistant de preuve plus puissant comme **Coq**. Coq est employé dans des **domaines critiques pour la sécurité** où une certitude mathématique absolue est primordiale. `coqtop` est le REPL standard pour Coq.

Une différence fondamentale avec Prolog est l'absence d'**Hypothèse du Monde Clos** (Closed World Assumption) dans Coq. Dans Coq, tout ce qui n'est pas explicitement prouvé est simplement **inconnu**, pas automatiquement faux.

Contrairement à Prolog, le but premier de Coq n'est pas de résoudre des problèmes de calcul en cherchant dans une base de connaissances. Sa véritable force réside dans sa capacité à **construire et vérifier des preuves mathématiques formelles et des programmes avec une rigueur absolue**. Son interaction implique la gestion d'un **état de preuve** (vos objectifs restants) et l'application de **tactiques** (étapes d'inférence logique) jusqu'à ce que la preuve soit complète.

#### Installation de Coq

Coq peut être installé de plusieurs manières, souvent via des gestionnaires de paquets ou un outil appelé `opam` (le gestionnaire de paquets OCaml, car Coq est écrit en OCaml).

-   **Téléchargements officiels :** Visitez le site de Coq pour des instructions détaillées selon votre OS : [https://coq.inria.fr/download][25]
    
-   **Utilisation d'un gestionnaire de paquets système (par ex., Ubuntu/Debian) :**
    
    ```bash
      sudo apt update
      sudo apt install coq
    ```
    

#### Utilisation de Coq : REPL vs Fichier

-   Le **REPL (**`coqtop`) est idéal pour : Essayer des tactiques uniques, inspecter l'état actuel de la preuve, ou apprendre la syntaxe de base pour des commandes très courtes.
    
-   **Un fichier (**extension `.v`) est idéal pour : **Presque tout le développement Coq et la construction de preuves.** C'est ainsi que les preuves complexes et les programmes vérifiés sont structurés et gérés.
    

#### La réponse complète aux questions de Coq

Contrairement à Prolog, Coq peut répondre directement aux trois types de questions logiques dont nous avons discuté, en fournissant des réponses robustes étayées par une preuve formelle :

-   **"Est-ce que P(X) est vrai pour un X spécifique ?"** : Coq vous permet de définir un énoncé précis (un **théorème**) comme "Alice a un emploi". Vous construisez ensuite une **preuve** logique étape par étape qui confirme formellement si cet énoncé est vrai sur la base de vos définitions. Si la preuve réussit, Coq la vérifie formellement ; si elle échoue, Coq montre clairement où votre logique flanche.
    
-   **"Existe-t-il un X pour lequel P(X) est vrai ?"** : Coq gère les questions d'existence. Si vous demandez : "Est-ce que quelqu'un a un emploi ?", vous pouvez construire une preuve en fournissant explicitement un exemple (comme "Alice") puis en prouvant que l'exemple choisi satisfait effectivement la condition ("Alice a un emploi").
    
-   **"Existe-t-il un X pour lequel P(X) est faux ?"** : C'est une capacité clé où Coq surpasse Prolog. Coq vous permet de prouver formellement qu'un énoncé est faux, ou qu'un contre-exemple existe. Par exemple, vous pourriez prouver "Carol n'a pas d'emploi" en montrant que cela contredit la définition, ou prouver qu'"il existe quelqu'un qui n'a pas d'emploi" en identifiant explicitement une telle personne et en prouvant qu'elle n'a effectivement pas d'emploi. Cette capacité directe à raisonner sur la négation et à fournir des contre-exemples formels (ou à prouver leur non-existence) est ce qui fait de Coq un **assistant de preuve complet**.
    

Bien que le cœur de Coq ne génère pas automatiquement de contre-exemples lorsqu'une preuve échoue, des plugins comme QuickChick peuvent être intégrés pour effectuer des tests basés sur les propriétés afin de trouver des exemples falsificateurs.

C'est une bibliothèque Coq qui vous permet de spécifier des propriétés sur vos définitions Coq et de **générer aléatoirement des entrées** pour essayer de trouver un contre-exemple qui falsifie votre propriété.

C'est un moyen puissant de _trouver les bugs tôt_ dans votre formalisation avant d'investir beaucoup de temps à essayer de prouver un théorème faux.

### TLA+, Isabelle et Lean : un spectre de vérification formelle

Au-delà de Prolog et Coq, d'autres assistants de preuve puissants et langages de spécification formelle répondent à des besoins et des paradigmes différents :

-   **TLA+ :** Il s'agit d'un **langage de spécification** formelle développé par Leslie Lamport. Il se concentre sur la modélisation et la vérification des **conceptions de systèmes** (en particulier les systèmes concurrents et distribués) en utilisant la **logique temporelle**, plutôt que de prouver du code de bas niveau. Il aide à garantir des propriétés critiques comme la sûreté (rien de mal n'arrive jamais) et la vivacité (quelque chose de bien finit par arriver). Sa praticité et son accessibilité le rendent populaire dans l'industrie, notamment chez Amazon et Microsoft pour la conception de systèmes robustes.
    
-   **Isabelle et Lean :** Ce sont des assistants de preuve modernes et hautement avancés.
    
    -   **Isabelle**, basé sur la logique d'ordre supérieur, est largement utilisé par les chercheurs et les institutions (par exemple, dans des projets comme le micro-noyau vérifié seL4) pour la démonstration formelle de théorèmes et la vérification de logiciels dans des **domaines critiques pour la sécurité** exigeant une rigueur extrême.
        
    -   **Lean**, basé sur la théorie des types dépendants, est privilégié par les mathématiciens pour la **formalisation des preuves en mathématiques pures** (par exemple, théorie des nombres, algèbre). Il est connu pour sa puissante automatisation et sa communauté active.
        

Ces outils représentent le summum de l'application de la logique formelle pour garantir la justesse et la fiabilité des théories mathématiques et des systèmes logiciels complexes.

Maintenant que vous avez une bonne vision d'ensemble de la théorie et de la pratique, voici quelques expériences de pensée pour enrichir votre apprentissage.

![noix sur une table, comme des amandes, des noix de cajou](https://cdn.hashnode.com/res/hashnode/image/upload/v1749063042362/b94ec237-0aca-46d8-8921-80dfe1f5f051.jpeg)

## Matière à réflexion

Le voyage dans la logique formelle et son intersection avec des domaines pratiques comme le logiciel et la science offre de nombreuses pistes d'exploration plus approfondie.

### Tests d'hypothèse en science et table de vérité de l'implication

Les tests d'hypothèse statistique utilisent une forme probabiliste de Modus Tollens. Nous commençons par une **hypothèse nulle (H0) : "Si H0 est vraie, alors l'observation de ces données (ou de données plus extrêmes) est probable."** Nous observons ensuite des données qui sont hautement improbables/inattendues si H0 était vraie (c'est-à-dire une petite p-value). Cela sert de **"non Q" probabiliste**. Par conséquent, nous concluons que H0 n'est probablement pas vraie (nous rejetons H0). C'est notre **"∴¬P" probabiliste**.

Ici, la **"vérité" de P⟹Q est testée**, plutôt que d'être simplement supposée vraie pour développer des arguments, comme dans le Modus Ponens ou le Modus Tollens. Il n'y a pas de vérité absolue ou quoi que ce soit à "prouver" définitivement.

Les inférences sont tirées d'expériences antérieures (qui informent la distribution des données de test) et de configurations d'expériences spécifiques au contexte (qui définissent le niveau de signification α), définissant ensemble le seuil (valeur critique) pour ce qui est considéré comme une observation improbable de Q.

Le résultat de l'expérience est un rejet (ou non) de H0, pas une preuve définitive que H0 est vraie.

### Relation du raisonnement inductif avec les arguments déductifs

-   L'**induction** génère des règles générales (par exemple, "P est toujours suivi de Q") à partir d'observations ou de cas spécifiques.
    
-   La **déduction** teste ou applique ensuite ces règles générales dans de nouvelles situations.
    

Si la déduction mène à de mauvaises prédictions (c'est-à-dire qu'une règle est falsifiée), l'induction peut avoir besoin de réviser la règle originale, ce qui forme une **boucle de rétroaction** continue qui affine notre compréhension.

### Nécessité et suffisance dans l'implication

L'implication **P⟹Q ("Si vous avez franchi la frontière, vous deviez avoir un passeport")** se décompose en deux concepts logiques fondamentaux :

-   **P est suffisant pour Q :** Franchir la frontière **garantit** que vous aviez un passeport. (P seul suffit pour Q.)
    
-   **Q est nécessaire pour P :** Si vous **n'aviez pas de passeport (¬Q), vous ne pouviez pas avoir franchi la frontière (¬P)**. (Q est requis pour que P se produise.)
    

## Q.E.D. : Le pouvoir durable de la logique dans un monde incertain

Tout au long de ce manuel, nous avons voyagé des concepts fondamentaux de la logique propositionnelle et des tables de vérité aux puissantes formes d'arguments que sont le Modus Ponens et le Modus Tollens. Nous avons exploré comment ces outils permettent des déductions valides et identifié des sophismes logiques courants comme l'affirmation du conséquent et la négation de l'antécédent, comprenant pourquoi ils mènent à des inférences incorrectes lorsqu'une relation "si-alors" n'est pas un "si et seulement si" strict. Nous avons appris l'importance profonde de la falsifiabilité – la capacité pour un énoncé ou une hypothèse d'être infirmé – une pierre angulaire de l'enquête scientifique et des tests logiciels robustes.

Nous avons ensuite approfondi l'application pratique de ces principes logiques dans le développement de logiciels, en faisant correspondre la justesse du code aux résultats des tests. Nous avons découvert comment un test échoué, lorsqu'il est fiable, devient une application puissante du Modus Tollens, identifiant les défauts. Nous avons également affronté l'"illusion de la correction" qui découle du sophisme de l'affirmation du conséquent lorsque les tests réussissent pour les mauvaises raisons, en particulier lors de l'utilisation de doublures de test.

De manière cruciale, nous avons introduit la relation "Si et seulement si" (P⟺Q), soulignant son pouvoir inégalé pour établir des connexions sans ambiguïté entre la cause et l'effet. Cette garantie bidirectionnelle est l'idéal que nous recherchons pour la qualité des suites de tests, passant de la simple corrélation à une compréhension plus profonde de la causalité. Nous avons vu comment les tests de mutation nous poussent rigoureusement vers cette confiance en "si et seulement si" en essayant activement de falsifier l'hypothèse selon laquelle "un code incorrect mène à des tests échoués", renforçant ainsi l'inverse : "des tests réussis garantissent un code correct".

Nous avons également reconnu la "réalité désordonnée" des logiciels modernes. Les grands systèmes sont des réseaux de complexité, avec des patterns de fan-in/fan-out, des effets secondaires et des interactions imprévues qui peuvent obscurcir les chaînes logiques claires. La dette technique et l'épée à double tranchant de l'abstraction masquent souvent les origines réelles des bugs, transformant le débogage en un "brouillard causal".

### La logique comme boussole

Malgré ces défis formidables, les principes logiques que nous avons explorés restent vos outils les plus vitaux. Ils fournissent le cadre mental pour naviguer dans l'incertitude.

Face à un bug, votre capacité à raisonner logiquement vous permet de formuler des hypothèses, de concevoir des expériences ciblées (vos tests) et d'interpréter leurs résultats avec précision. Que vous déboguiez un microservice complexe ou que vous raisonniez sur une fonction simple, l'application du Modus Tollens à un test échoué ou la conception de tests visant la clarté P⟺Q vous aide à percer le bruit.

Nous avons également abordé des outils avancés comme les assistants de preuve (Prolog, Coq, TLA+, Isabelle, Lean), qui représentent le summum de l'application de la logique formelle pour garantir la justesse du système – un témoignage du pouvoir durable de la rigueur logique dans les domaines critiques.

Dans la danse complexe entre théorie et pratique, les principes de la logique constituent un fondement inébranlable. Ils sont les "pierres" sur lesquelles vous pouvez méticuleusement construire votre compréhension et vos systèmes. Plus vous appliquez systématiquement cette pensée critique, guidée par la curiosité et un engagement envers une validation rigoureuse, plus votre chemin devient clair.

Cette clarté ne consiste pas seulement à corriger les bugs d'aujourd'hui, il s'agit d'affiner continuellement vos modèles mentaux, de favoriser la confiance dans votre base de code et de vous équiper pour construire des systèmes de plus en plus robustes et prévisibles dans un paysage technologique en constante évolution.

Si vous aimez la résolution de problèmes, la pensée critique, ou si vous avez des expériences sur la façon dont vous avez résolu un problème qui semblait différent de ce qu'il paraissait initialement, n'hésitez pas à me contacter sur [https://linkedin.com/in/hanqi91][26].

![homme faisant du kayak et se préparant à descendre une cascade](https://cdn.hashnode.com/res/hashnode/image/upload/v1749064755840/c7646f6a-a8ba-4cf5-9647-0488e24705aa.jpeg)

## Ressources

1.  Article ayant motivé ce manuel : [Classical Reasoning and Debugging][27]
    
2.  3 preuves formelles du modus tollens : [https://en.wikipedia.org/wiki/Modus\_tollens][28]
    
3.  Tableau de 24 syllogismes : [https://en.wikipedia.org/wiki/Syllogism][29]
    
4.  Remise en question des hypothèses : [Falsehoods software teams believe about user feedback][30]
    
5.  Comment les hypothèses et les logiciels évoluent hors de votre contrôle : [https://www.tdda.info/why-code-rusts][31]
    
6.  Relation avec les tests d'hypothèse : [https://sites.google.com/view/reasonedwriting/home/FRAMEWORK\_FOR\_SCIENTIFIC\_PAPERS/HYPOTHESES/HOW\_TO\_TEST\_HYPOTHESES/MODUS\_TOLLENS][32]
    
7.  L'état d'esprit du dépannage : [https://www.autodidacts.io/troubleshooting/][33]
    
8.  Diagrammes causaux du livre The Effect : [https://theeffectbook.net/ch-CausalDiagrams.html][34]
    
9.  Un guide systématique des mentalités et pratiques du débogage : [https://www.amazon.sg/Debug-Find-Repair-Prevent-Bugs/dp/193435628X][35]
    
10.  Construire P de manière à garantir la justesse du logiciel : [https://www.hillelwayne.com/post/constructive/][36]
    
11.  Fail Fast en représentant explicitement les hypothèses comme des assertions : [https://www.martinfowler.com/ieeeSoftware/failFast.pdf][37]
    
12.  Tests de simulation déterministes pour aborder les systèmes complexes : [https://pierrezemb.fr/posts/learn-about-dst/][38]
    
13.  Engineering System Success Playbook (ESSP) de GitHub - Qualité, Vélocité, Bonheur des développeurs sur les résultats commerciaux : [https://assets.ctfassets.net/wfutmusr1t3h/us6AUuwawrtNGTlwlT9Ac/f0fce86712054fc87f10db28b20f303b/GitHub-ESSP.pdf][39]
    
14.  Hypothèse du monde clos : [https://en.wikipedia.org/wiki/Closed-world\_assumption][40]
    

## Glossaire

-   **Axiome :** Une vérité ou règle fondamentale acceptée comme point de départ d'un système logique ou mathématique, sans nécessiter de preuve.
    
-   **Contraposée :** Une forme logiquement équivalente d'un énoncé "si-alors" (P⟹Q), qui est ¬Q⟹¬P ("Si non Q, alors non P").
    
-   **Raisonnement déductif :** Un type de raisonnement logique où une conclusion est nécessairement vraie si ses prémisses sont vraies.
    
-   **Falsification :** Le principe, particulièrement en science (selon Karl Popper), selon lequel une hypothèse ou une théorie doit pouvoir être prouvée fausse par l'observation empirique ou l'expérience.
    
-   **Logique formelle :** L'étude des systèmes abstraits de raisonnement et d'arguments basés sur leur structure, indépendamment du contenu.
    
-   **Test d'hypothèse :** Une méthode statistique pour tirer des inférences sur une population à partir de données d'échantillon, généralement en testant une hypothèse nulle (par ex., "P n'a aucun effet sur Q") contre une hypothèse alternative.
    
-   **Sophisme logique :** Un défaut dans la structure ou le contenu d'un argument qui le rend non fondé ou invalide, même si sa conclusion peut sembler plausible.
    
    -   **Affirmation du conséquent (Sophisme) :** Une forme d'argument invalide qui suppose par erreur que si P⟹Q est vrai, et que Q est vrai, alors P doit être vrai.
        
    -   **Négation de l'antécédent (Sophisme) :** Une forme d'argument invalide qui suppose par erreur que si P⟹Q est vrai, et que P est faux, alors Q doit être faux.
        
-   **Modus Ponens :** Une forme d'argument valide : Si P⟹Q est vrai et que P est vrai, alors Q doit être vrai.
    
-   **Modus Tollens :** Une forme d'argument valide : Si P⟹Q est vrai et que ¬Q est vrai, alors ¬P doit être vrai.
    
-   **Tests de mutation :** Une technique de test logiciel qui consiste à introduire délibérément de petits défauts ponctuels (mutations) dans le code pour évaluer l'efficacité et la couverture d'une suite de tests.
    
-   **Logique propositionnelle :** Une branche de la logique qui traite des propositions et de leurs relations en utilisant des opérateurs logiques.
    
-   **Test-Driven Development (TDD) :** Une méthodologie de développement logiciel où les tests sont écrits _avant_ le code, guidant le processus de développement et garantissant la justesse.
    
-   **Table de vérité :** Un tableau qui liste systématiquement toutes les valeurs de vérité possibles pour un ensemble de propositions et montre la valeur de vérité résultante d'un énoncé logique complexe.
    
-   **Vacueusement vrai :** Décrit une implication (P⟹Q) qui est considérée comme vraie simplement parce que son antécédent (P) est faux.
    

[1]: #heading-une-introduction-a-la-logique
[2]: #heading-tables-de-verite-cartographier-toutes-les-possibilites
[3]: #heading-contraposees-modus-ponens-modus-tollens
[4]: #heading-lorigine-de-p-q-science-et-realite
[5]: #heading-retour-sur-les-formes-darguments-inferences-valides-et-sophismes-courants
[6]: #heading-nier-lantecedent-un-exemple-de-base-de-donnees
[7]: #heading-assigner-des-significations-concretes-a-la-logique
[8]: #heading-appliquer-la-logique-aux-tests-logiciels
[9]: #heading-un-regard-plus-attentif-sur-les-tests
[10]: #heading-retour-sur-les-quatre-enonces-pour-le-code
[11]: #heading-lingredient-manquant-si-et-seulement-si
[12]: #heading-tests-de-mutation-tester-les-tests
[13]: #heading-vers-une-confiance-en-si-et-seulement-si
[14]: #heading-les-defis-du-monde-reel
[15]: #heading-lueurs-despoir-outils-et-pratiques-pour-la-clarte
[16]: #heading-le-pouvoir-de-la-falsification-dans-les-tests
[17]: #heading-assistants-de-preuve
[18]: #heading-matiere-a-reflexion
[19]: #heading-qed-le-pouvoir-durable-de-la-logique-dans-un-monde-incertain
[20]: #heading-ressources
[21]: #heading-glossaire
[22]: https://fr.wikipedia.org/wiki/V%C3%A9rit%C3%A9_vacueuse
[23]: https://github.com/boxed/mutmut/issues/281
[24]: https://www.swi-prolog.org/download/stable
[25]: https://coq.inria.fr/download
[26]: https://linkedin.com/in/hanqi91
[27]: https://thoughtbot.com/blog/classical-reasoning-and-debugging
[28]: https://en.wikipedia.org/wiki/Modus_tollens
[29]: https://en.wikipedia.org/wiki/Syllogism
[30]: https://thoughtbot.com/blog/falsehoods-software-teams-believe-about-user-feedback
[31]: https://www.tdda.info/why-code-rusts
[32]: https://sites.google.com/view/reasonedwriting/home/FRAMEWORK_FOR_SCIENTIFIC_PAPERS/HYPOTHESES/HOW_TO_TEST_HYPOTHESES/MODUS_TOLLENS
[33]: https://www.autodidacts.io/troubleshooting/
[34]: https://theeffectbook.net/ch-CausalDiagrams.html
[35]: https://www.amazon.sg/Debug-Find-Repair-Prevent-Bugs/dp/193435628X
[36]: https://www.hillelwayne.com/post/constructive/
[37]: https://www.martinfowler.com/ieeeSoftware/failFast.pdf
[38]: https://pierrezemb.fr/posts/learn-about-dst/
[39]: https://assets.ctfassets.net/wfutmusr1t3h/us6AUuwawrtNGTlwlT9Ac/f0fce86712054fc87f10db28b20f303b/GitHub-ESSP.pdf
[40]: https://en.wikipedia.org/wiki/Closed-world_assumption