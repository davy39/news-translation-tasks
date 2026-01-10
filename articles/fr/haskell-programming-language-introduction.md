---
title: Langage de programmation Haskell – Comment installer et utiliser Haskell
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-04T19:57:55.000Z'
originalURL: https://freecodecamp.org/news/haskell-programming-language-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/haskell_freecodecamp.png
tags:
- name: Haskell
  slug: haskell
- name: programming languages
  slug: programming-languages
seo_title: Langage de programmation Haskell – Comment installer et utiliser Haskell
seo_desc: 'By MacBobby Chibuzor

  What is Haskell? What is it used for? Why are there relatively few Haskell programmers?
  How can I get started with Haskell?

  If you''re asking yourself these questions, then this article is for you. In it,
  I''ll answer your question...'
---

Par MacBobby Chibuzor

Qu'est-ce que Haskell ? À quoi sert-il ? Pourquoi y a-t-il relativement peu de programmeurs Haskell ? Comment puis-je commencer avec Haskell ?

Si vous vous posez ces questions, alors cet article est fait pour vous. Dans cet article, je répondrai à vos questions sur le langage de programmation Haskell et le démystifierai pour vous. 

Vous apprendrez à connaître l'écosystème Haskell et comment le configurer pour le développement. Vous découvrirez également la beauté de Haskell et où le langage peut être appliqué pour résoudre des problèmes réels.

Étant donné la complexité de Haskell, vous devriez connaître les bases de la programmation avant de vous plonger dans Haskell. Il sera également utile d'être très à l'aise avec un autre langage de programmation fonctionnelle pour mieux comprendre la syntaxe de Haskell.

# Ce que nous allons couvrir

* Haskell — Une introduction appropriée
* Programmation fonctionnelle
* Programmation fortement typée statiquement
* L'écosystème Haskell
* Comment configurer l'environnement de développement Haskell
* L'éditeur de code
* Découvrir la beauté de Haskell
* Le compilateur `ghci`
* Python vs Haskell — le plus facile vs le plus difficile
* Principaux cas d'utilisation de Haskell
* Développement web : Backend avec Spock, Frontend avec Elm
* Développement de la blockchain Cardano avec Plutus

# Haskell — Une introduction appropriée

Haskell est un langage de programmation entièrement fonctionnel qui prend en charge l'évaluation paresseuse et les classes de types. 

Haskell oblige le développeur à écrire un code très correct, ce qui est la nature quintessentielle du langage.

## Programmation fonctionnelle

Le monde de la programmation informatique permet différents styles de programmation : fonctionnel, impératif, orienté objet. 

Le style de programmation fonctionnelle traite les fonctions comme des citoyens de première classe — les parties les plus importantes d'un programme. 

Dans les langages de programmation fonctionnelle, les fonctions peuvent être passées comme des valeurs ou des types de données. Les fonctions peuvent être passées comme arguments à d'autres fonctions, retournées comme résultats de fonctions et assignées à des variables. Cela favorise la réutilisation du code dans une seule base de code.

Haskell est un langage de programmation fonctionnelle et il prend en charge ces propriétés. Les langages modernes comme Java, C++, Go et C# sont tous liés au style de programmation fonctionnelle.

## Langage fortement typé statiquement

Les langages de programmation peuvent avoir un système de typage dynamique ou statique. Dans le typage dynamique, les valeurs sont étiquetées avec des types de données pendant l'exécution. Cela est courant parmi les langages comme Python et JavaScript qui permettent la conversion implicite entre les types de données. 

Dans le typage statique, l'étiquetage est effectué pendant la compilation et est courant parmi les langages de bas niveau. Dans les langages à typage statique, les programmes sont évalués par le compilateur avant d'être compilés en code machine ou en bytecode et exécutés.

Haskell est à typage statique car ses programmes doivent être vérifiés avant la compilation et l'exécution. Contrairement à Java et C#, le compilateur Haskell ne fait la vérification de type qu'une seule fois, ce qui améliore les performances. 

De plus, le système de typage de Haskell est appelé fort en raison de la sécurité des erreurs au moment de la compilation. Ainsi, une phrase courante parmi les développeurs Haskell est : « Une fois qu'il compile, il fonctionne. »

# L'écosystème Haskell

L'aspect le plus difficile pour commencer avec un nouveau langage est de configurer parfaitement l'environnement de développement. 

Pour installer et configurer Haskell, vous devez obtenir l'ensemble de l'écosystème Haskell. L'écosystème Haskell contient :

* Le compilateur appelé Glasgow Haskell Compiler (GHC)
* L'interpréteur appelé Glasgow Haskell Interpreter (GHCi)
* L'outil Stack pour gérer les projets Haskell
* Autres packages Haskell

Vous pouvez obtenir le package logiciel tout-en-un depuis [www.haskell.org/downloads#platform](http://www.haskell.org/downloads#platform). Haskell, comme tout autre langage de programmation largement adopté, dispose d'une base de données pour ses bibliothèques, appelée [Hackage](http://hackage.haskell.org/).

## Comment configurer l'environnement de développement Haskell

### Environnement Linux

Si vous utilisez une machine Linux, il est plus facile d'exécuter une commande shell. La commande ci-dessous installera la plateforme Haskell sur votre machine.

```bash
$ sudo apt-get install haskell-platform

```

Ensuite, tapez `ghc` sur la ligne de commande Linux et appuyez sur **Entrée**. Cela devrait vous demander si vous souhaitez installer l'interpréteur GHCi ou non. Tapez Y et appuyez sur `Entrée`. Vous devriez également installer l'outil de construction Cabal en exécutant cette chaîne de commandes :

```bash
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:hvr/ghc
$ sudo apt install cabal-install

```

Après l'installation, vous devriez voir la sortie suivante lorsque vous ré-exécutez `ghci` sur le shell :

```bash
$ ghci
GHCi, version 8.8.4: <https://www.haskell.org/ghc/>  :? pour l'aide
Prelude>

```

Exécutez une simple arithmétique pour confirmer que `ghci` fonctionne correctement.

### Windows et Mac OS

La plateforme Haskell peut être obtenue depuis la page de téléchargement officielle pour Windows et macOS. 

Vous pouvez installer l'outil de bibliothèques Cabal sur Windows depuis [ici](https://downloads.haskell.org/~cabal/cabal-install-3.6.2.0/cabal-install-3.6.2.0-x86_64-windows.zip). Vous pouvez l'installer pour macOS [ici](https://downloads.haskell.org/~cabal/cabal-install-3.6.2.0/cabal-install-3.6.2.0-x86_64-darwin.tar.xz).

## L'éditeur de code

Haskell n'a pas d'éditeur de code spécialement adapté pour écrire ses programmes. Vous pouvez écrire du code Haskell dans l'un de ces éditeurs de code :

* [IntelliJ IDEA](https://www.jetbrains.com/idea/download/download-thanks.html?platform=linux&code=IIC) avec le [plugin Haskell](https://plugins.jetbrains.com/plugin/8258-intellij-haskell) installé
* Visual Studio Code avec les plugins Haskell installés
* Emacs en mode Haskell
* Neovim

Alternativement, vous pouvez également écrire du code Haskell sur un éditeur de code « basique » comme Notepad++ et Sublime Text, puis compiler avec le GHC. 

Ce que fait Haskell, c'est vous conditionner à écrire des codes en morceaux ou modules, en les répétant pour vous assurer que chaque module est correct et parfait pour la production. Ainsi, un éditeur de code intelligent ou basique a un impact minimal sur le code final.

N'hésitez pas à vérifier les extensions dans les places de marché des éditeurs de code qui faciliteront l'écriture des fichiers sources Haskell, comme Haskero ou [Haskell Runner pour VSCode](https://github.com/Meowcolm024/has-go).

# Découvrir la beauté de Haskell

La beauté de Haskell réside dans :

* La logique
* La facilité de lecture du code Haskell comme des expressions mathématiques
* Vous pouvez spécifier la sortie probable pour un programme et le langage fait le reste
* Sa nature auto-documentée
* Le magnifique compilateur GHCi
* Le concept de pureté

## Le compilateur `ghci`

Contrairement à d'autres langages de programmation, le compilateur `ghci` vous permet d'utiliser le compilateur de manière interactive.

De plus, le codage multi-ligne, qui n'est pas autorisé dans d'autres compilateurs, est autorisé dans `ghci`. Par exemple, si vous souhaitez écrire un script complet dans Python IDLE, vous devriez l'écrire étape par étape, chaque ligne étant complète. Mais le compilateur de Haskell permet de faire du codage multi-ligne comme ceci :

```haskell
$ ghci
GHCi, version 8.8.4: <https://www.haskell.org/ghc/>  :? pour l'aide
Prelude> :{
Prelude| 60 +
Prelude| 30
Prelude| :}
90
Prelude>

```

## Python vs Haskell — le plus facile vs le plus difficile

Haskell est considéré comme un langage très difficile à apprendre et à maîtriser. D'un autre côté, Python est considéré comme le langage de programmation le plus facile et le plus utile à utiliser.

Étant donné que de nombreux programmeurs sont à l'aise avec la programmation Python, il est logique d'expliquer Haskell en termes de Python :

1. Haskell est un langage fonctionnel, comme mentionné précédemment, tandis que Python est un mélange de styles de programmation procédurale, orientée objet et fonctionnelle. Haskell prend en charge la programmation procédurale, mais les effets secondaires dans le langage ne la rendent pas facile.
2. Python et Haskell ont un système de typage fort, ce qui signifie que des conversions explicites doivent être effectuées. Cependant, tandis que Python est à typage dynamique, Haskell est à typage statique.
3. Python est beaucoup plus lent que Haskell.
4. Comme mentionné précédemment, Python est plus facile à apprendre que Haskell. La courbe d'apprentissage de Haskell est raide, surtout pour ceux qui n'ont aucune expérience préalable en programmation fonctionnelle.
5. En termes de support de bibliothèque, Python a plus de bibliothèques et de cas d'utilisation que Haskell.

# Principaux cas d'utilisation de Haskell

Les principales utilisations du langage Haskell aujourd'hui incluent le développement web et le développement de la blockchain Cardano.

## Haskell pour le développement web

Vous pouvez utiliser Haskell pour le développement web. Tout comme Python a Flask et Django, Go a Gin, Echo et Bevel, Haskell a Scotty, Servant et Yesod, tous construits sur Wai.

Wai est le package Haskell pour gérer les requêtes/réponses HTTP. Parmi les trois frameworks Haskell populaires, Yesod est plus un framework web complet que les autres.

Haskell a également le package `blaze-html` utilisé pour construire des fichiers HTML, similaire à `gohtml`.

## **Haskell pour le développement de la blockchain Cardano**

Cardano est une nouvelle plateforme de blockchain qui adopte l'algorithme de consensus Proof-of-Stake. C'est la première à permettre la recherche par les pairs et elle a été créée pour répondre aux inconvénients de Bitcoin et Ethereum.

La cryptomonnaie Cardano, ADA, est une monnaie populaire au Japon, et ils ont des distributeurs automatiques ADA installés à Tokyo. 

Le système de blockchain Cardano est écrit en Plutus, un langage de programmation basé sur Haskell et Turing-complet. 

Plutus utilise plusieurs outils pour construire des contrats intelligents sur la blockchain Cardano. Il dispose du backend d'application Plutus qui fournit l'environnement et les outils utilisés pour interagir avec les contrats intelligents. Plutus fournit également un estimateur de frais pour les calculs de coûts internes.

Vous pouvez prévisualiser et exécuter du code Plutus sur le [Plutus Playground](https://playground.plutus.iohkdev.io/).

Puisque Haskell est un langage à haute assurance construit pour les utilisateurs de l'industrie financière, il résout le problème des échecs d'échange de transactions dus à un mauvais code, et des échecs multi-signatures qui permettent aux pirates de voler de l'argent numérique.

# Mots finaux

Merci d'avoir lu cette introduction à Haskell, son écosystème et ses principales utilisations. J'espère que vous êtes inspiré pour commencer à en apprendre davantage.

Dans mes futurs articles, vous pourrez apprendre les bases de la programmation Haskell, ainsi que plus sur ses principales utilisations.