---
title: Comment construire un outil d'analyse statique C++ basé sur l'AST de Clang
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-11-30T19:01:21.000Z'
originalURL: https://freecodecamp.org/news/clang-ast-based-static-analysis-tools
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/ClangCover-2.jpg
tags:
- name: C++
  slug: c-2
- name: compilers
  slug: compilers
seo_title: Comment construire un outil d'analyse statique C++ basé sur l'AST de Clang
seo_desc: 'Clang is a set of tools and projects that provides infrastructure for languages
  in the C family like C, C++, OpenCL, and CUDA. It is a part of the LLVM project.

  This article will show you how to use Clang''s front end libraries to build a simple
  stati...'
---

Clang est un ensemble d'outils et de projets qui fournit une infrastructure pour les langues de la famille C comme C, C++, OpenCL et CUDA. Il fait partie du projet [LLVM](https://www.llvm.org/).

Cet article vous montrera comment utiliser les bibliothèques frontales de Clang pour construire un outil d'analyse statique simple qui fonctionnera sur des fichiers source / d'en-tête C++. Il utilisera la puissance de la traversée de l'AST (Abstract Syntax Tree).

Un arbre de syntaxe abstraite est une structure arborescente représentant la structure syntaxique du code. [Ici](https://en.wikipedia.org/wiki/Abstract_syntax_tree) se trouve une bonne explication de son fonctionnement, et [ici](https://astexplorer.net/) un outil pour vous aider à explorer l'AST pour un morceau de code donné.

Ici, je vais vous apprendre comment utiliser l'AST de Clang pour trouver des informations sur le code qui lui est donné afin de vous montrer à quel point il est puissant.

Cet article passe en revue tout cela étape par étape, et j'expliquerai brièvement la terminologie que j'utilise à chaque étape.

Dans la première section, vous apprendrez comment obtenir le projet open source Clang. Ensuite, nous explorerons comment vous pouvez construire un outil d'analyse statique avec un objectif simple : vérifier si chaque `Class` définie dans un fichier source / d'en-tête commence par un caractère majuscule. Nous ferons cela en utilisant les bibliothèques frontales de Clang qui analyseront l'AST source C++.

Alors, allez-y et prenez votre boisson de codage préférée, installez-vous confortablement et continuez votre lecture !

Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
* [Comment obtenir le projet Clang et accéder aux bibliothèques frontales](#comment-obtenir-le-projet-clang-et-acceder-aux-bibliothèques-frontales)
* [Comment créer l'échafaudage pour l'outil d'analyse statique](#heading-comment-creer-lechafaudage-pour-loutil-danalyse-statique)
* [Mettre le tout ensemble dans le code](#heading-mettre-le-tout-ensemble-dans-le-code)
* [Résumé](#heading-resume)

## Prérequis

Avant de commencer, il serait bénéfique d'avoir une compréhension de base des éléments suivants :

* Compilateurs : [cette](https://en.wikipedia.org/wiki/Compiler#:~:text=In%20computing%2C%20a%20compiler%20is,language%20(the%20target%20language).) page est une bonne introduction pour les débutants.
* C++ : Pour les lecteurs non familiers avec C++, [Apprendre la programmation C++ pour débutants – Cours gratuit de 31 heures](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) est une ressource utile.
* Git : [Git Best Practices – Un guide de contrôle de version pour débutants](https://www.freecodecamp.org/news/how-to-use-git-best-practices-for-beginners/) est un excellent point de départ.

## Comment obtenir le projet Clang et accéder aux bibliothèques frontales

Puisque `clang` et `llvm` sont des projets open source, ils disposent d'une documentation très complète sur la manière de commencer à obtenir le code et à construire des outils en les utilisant.

Vous pouvez consulter la page [Getting Started](https://llvm.org/docs/GettingStarted.html) du projet `llvm` pour obtenir plus d'informations à ce sujet. Je m'y suis également référé dans cet article.

### 1. Obtenir le projet Clang

Sur un terminal de type UNIX, clonez le projet Git `llvm` dans votre propre répertoire. Je l'appellerai `ast-analyzer`.


1. `mkdir -p  ~/ast-analyzer; cd ~/ast-analyzer`
2. `git clone https://github.com/llvm/llvm-project.git` # Clone le code source du projet llvm


### 2. Obtenir le système de construction CMake et l'outil de construction Ninja

[CMake](https://cmake.org/) et [ninja](https://ninja-build.org/) fonctionnent ensemble pour former un système de construction. `CMake` génère des fichiers `build.ninja`, qui contiennent des commandes indiquant à `ninja` comment générer des cibles de sortie. Nous approfondirons cela un peu plus tard.

#### 2.1 Obtenir et installer Ninja


Voici les étapes que vous pouvez suivre pour installer Ninja :

1. `cd ~/ast-analyzer`
2. Clonez le projet source ninja avec cette commande : `git clone https://github.com/martine/ninja.git` 
3. `cd ninja`
4. Passez à la branche release - c'est la branche stable - avec cette commande : `git checkout release`
5. `python3 configure.py –bootstrap` Cela prépare et crée un binaire Ninja (`configure.py –help` vous donnera plus d'informations).
6. Installez ninja avec cette commande : `sudo cp ninja /usr/local/bin`. Après cette étape, en tant que vérification de validité de base, faites `which ninja` pour vous assurer qu'il indique /usr/local/bin/ninja.

#### 2.2. Obtenir et installer CMake

Voici les étapes que vous pouvez suivre pour installer cmake :

1. `cd ~/ast-analyzer`
2. Clonez le code source du projet cmake : `git clone git://cmake.org/stage/cmake.git`
3. `cd cmake`
4. Passez à la branche release - c'est la branche stable - avec cette commande : `git checkout release`.
5. Exécutez le script bootstrap : `./bootstrap`. Cela prépare cmake à être construit et installé sur votre machine hôte.
6. Construisez cmake à partir de la source avec cette commande : `make`.
7. Enfin, installez cmake : `sudo make install`.



Une fois que nous avons obtenu Clang, nous allons le construire et le configurer afin de pouvoir également construire des outils basés sur Clang.

### 3. Construire Clang et le configurer

Créez un répertoire 'build'. C'est là que nos fichiers build.ninja/ binaires de sortie et ainsi de suite seront créés :

```
cd ~/ast-analyzer; mkdir -p build; cd build
```

Maintenant, nous devons générer le fichier `build.ninja` afin de construire Clang ainsi que les outils dans le répertoire du projet cloné précédemment (`llvm/clang-tools-extra`). Vous pouvez faire cela en utilisant `CMake` comme ceci :

```
cmake -G Ninja ../llvm-project/llvm -DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra" # Activez les projets clang-tools dans notre build également
```

Cela devrait générer un fichier build.ninja, que je vous encourage à ouvrir et à consulter le contenu. Vous verrez qu'il contient une liste de cibles suivie de dépendances. Par exemple, l'une des cibles peut ressembler à ceci :

```
#############################################
# Commande utilitaire pour install-llvm-headers

build install-llvm-headers: phony CMakeFiles/install-llvm-headers llvm-headers
```

Nous ferons également cela pour l'outil d'analyse statique personnalisé que nous construirons dans les prochaines étapes.

### 4. Construire et installer toutes les cibles spécifiées dans le fichier build.ninja

`   ninja; ninja install`

D'accord, l'installation est terminée et maintenant nous arrivons à la partie amusante !

## Comment créer l'échafaudage pour l'outil d'analyse statique

Nous allons construire notre outil dans le cadre du répertoire `clang-tools-extra` dans `llvm-project/clang-tools-extra`. Allons-y et créons ce répertoire. Nous appellerons notre outil `class-analyzer`.

```
mkdir ~/ast-analyzer/llvm-project/clang-tools-extra/class-analyzer
cd ~/ast-analyzer/llvm-project/clang-tools-extra/class-analyzer
```

Maintenant, nous devons créer un `CMakeLists.txt`. Il s'agit essentiellement d'un fichier qui indique au système de construction `CMake` d'ajouter les fichiers source de cet outil au fichier `build.ninja` qu'il générera. Cela permet à `ninja` de savoir comment construire notre outil.

Notre fichier `CMakeLists.txt` ressemblera à ceci :

CMakeLists.txt

```
set(LLVM_LINK_COMPONENTS support)
set(CMAKE_CXX_COMPILER /usr/bin/clang++)  


add_clang_executable(class-analyzer
  ClassAnalzyer.cpp
  MyFrontendActionFactory.cpp
  MyFrontendAction.cpp
  MyASTConsumer.cpp
  )
target_link_libraries(class-analyzer
  PRIVATE
  clangAST
  clangFrontend
  clangTooling
  )
```

Les premières lignes indiquent au système de construction que le compilateur doit être `/usr/local/bin/clang++` (celui qui vient d'être construit dans les étapes précédentes).

La section suivante `add_clang_executable` indique au système de construction quels fichiers source construire dans le cadre de notre exécutable. Nous entrerons plus dans les détails de ce que fait chaque fichier source bientôt. Elle définit également le nom de l'exécutable pour le système de construction. Ici, il est appelé `class-analyzer` puisqu'il analyse les noms de classe.

La section `target_link_libraries` informe le système de construction des bibliothèques frontales Clang que nous devons lier. Ce sont les bibliothèques qui exposent vraiment la puissance de l'AST de Clang à l'outil que nous construirons.

La documentation de l'API de Clang est un bon point de départ pour chercher des indices sur la manière dont nous devons commencer à écrire l'outil `class-analyzer`. Un autre bon point de départ est de scanner le code source du projet Clang que nous avons cloné précédemment, pour d'autres outils ! `[clang-tools-extra](https://github.com/llvm/llvm-project/tree/main/clang-tools-extra)` contient plusieurs exemples - ceux-ci ont été une source d'inspiration pour le code écrit ici.

Alors maintenant, commençons par le code de notre tout premier fichier source. Ce fichier contient la fonction `main()` de l'exécutable. Il ressemble à ceci :

```cpp

#include "clang/Tooling/CommonOptionsParser.h"
#include "clang/Tooling/Tooling.h"

#include "MyFrontendActionFactory.h"

#include <memory>

using namespace clang::tooling;
using namespace llvm;

static llvm::cl::OptionCategory toolCategory("class-analyzer <options>");

int main(int argc, const char** argv)
{
    // Utiliser l'infrastructure d'analyse d'arguments de clang
    // Cela est utilisé pour donner à l'outil clang le chemin
    // vers les fichiers source passés à l'outil.
    // Il obtient également la base de données de compilation - une collection
    // des options du compilateur utilisées dans l'invocation de l'outil
    auto argsParser = CommonOptionsParser::create(
        argc, argv, toolCategory);
    if (!expectedArgsParser) {
        llvm::errs() << argsParser.takeError();
        return -1;
    }
    CommonOptionsParser& optionsParser
        = argsParser.get();
    ClangTool tool(optionsParser.getCompilations(),
                   optionsParser.getSourcePathList());
    auto myActionFactory
        = std::make_unique<MyFrontendActionFactory>();
   
    return tool.run(myActionFactory.get());
} 

```

Ce fichier source crée essentiellement un outil qui exécute une `clang` [`FrontendActionFactory`](https://clang.llvm.org/doxygen/classclang_1_1tooling_1_1FrontendActionFactory.html). Maintenant, pour comprendre ce que fait `FrontendActionFactory`, examinons la documentation de Clang à ce sujet.

Nous voyons qu'il a une méthode virtuelle pure,

```cpp
virtual std::unique_ptr<FrontendAction> create () = 0;
```

qui retourne un [`std::unique_ptr`](https://en.cppreference.com/w/cpp/memory/unique_ptr) vers un objet `[FrontendAction](https://clang.llvm.org/doxygen/classclang_1_1FrontendAction.html)`. `FrontendAction` est, en essence, une classe qui permet aux appelants d'effectuer des actions personnalisées lorsque Clang analyse l'AST d'une unité de traduction qui lui est donnée. Une [unité de traduction](https://en.wikipedia.org/wiki/Translation_unit_(programming)) en termes simples est le code combiné donné au compilateur pour créer un fichier objet. Il contient le code inclus à travers tous les fichiers d'en-tête + le code dans un fichier source C / C++

Cela deviendra plus clair au fur et à mesure que nous avancerons dans l'article.

Maintenant, nous en venons à l'écriture de notre propre `FrontendActionFactory` que vous pouvez appeler `MyFrontendActionFactory`. Il s'agit d'une classe très simple qui remplace simplement la méthode virtuelle `create()`. Elle ressemble à ceci :

```cpp
// Fichier d'en-tête MyFrontendActionFactory.h
#pragma once

include<clang/Tooling/Tooling.h>


class MyFrontendActionFactory : public clang::tooling::FrontendActionFactory{
    public:
    MyFrontendActionFactory();
    std::unique_ptr<clang::FrontendAction> create() override;
};                                                         

// Fichier source MyFrontendActionFactory.cpp

#include "MyFrontendActionFactory.h"
#include "MyFrontendAction.h"

MyFrontendActionFactory::MyFrontendActionFactory() {

}

std::unique_ptr<clang::FrontendAction> MyFrontendActionFactory::create() {
    return std::make_unique<MyFrontendAction>();
}

```

Puisque `MyFrontendActionFactory::create()` doit retourner un `std::unique_ptr` vers `clang::FrontendAction`, nous devons créer un objet `clang::FrontendAction`.

Si nous regardons la documentation de Clang pour [`FrontendAction`](https://clang.llvm.org/doxygen/classclang_1_1FrontendAction.html), nous serons particulièrement intéressés par ce que nous pouvons faire avec l'AST (Abstract Syntax Tree) de la source.

Nous pourrions repérer la méthode suivante :

```cpp
virtual std::unique_ptr< ASTConsumer >
CreateASTConsumer (CompilerInstance &CI, StringRef InFile) = 0;
```

Il s'agit d'une méthode virtuelle qu'une classe héritant de FrontendAction peut implémenter. Elle retourne un [`ASTConsumer`](https://clang.llvm.org/doxygen/classclang_1_1ASTConsumer.html#details) qui, selon la documentation,

> "...est une interface abstraite qui doit être implémentée par les clients qui lisent les AST."

Cette méthode semble donc très prometteuse si nous voulons créer quelque chose qui nous permettra de lire l'AST généré par Clang !

Si nous regardons à nouveau la documentation de `FrontendAction`, elle nous montre que `ASTFrontend` est une classe qui hérite de `FrontendAction`. Nous apprenons également que c'est :

> "La classe de base abstraite à utiliser pour les actions frontales basées sur les consommateurs AST."

Elle n'a qu'une seule méthode virtuelle pure : `CreateASTConsumer()`. Cela semble prometteur, puisque... nous pourrions être en mesure de créer notre propre objet `ASTConsumer`.

Nous commençons donc par lire la [documentation](https://clang.llvm.org/doxygen/classclang_1_1ASTConsumer.html) de `ASTConsumer`. Nous voyons qu'il a une méthode virtuelle

```cpp
virtual void
clang::ASTConsumer::HandleTranslationUnit(ASTContext &Ctx)
```

où la documentation indique :

> "`HandleTranslationUnit` - Cette méthode est appelée lorsque les AST pour toute l'unité de traduction ont été analysés".

C'est exactement ce que nous voulons. Nous pouvons remplacer cette méthode pour faire des choses intéressantes avec l'AST analysé.

Vous vous demandez peut-être maintenant - comment pouvons-nous utiliser exactement le paramètre passé à cette fonction `ASTContext` pour parcourir réellement l'AST ?

Il existe une classe dans l'API frontale de Clang qui peut nous aider ici : [`RecursiveASTVisitor`](https://clang.llvm.org/doxygen/classclang_1_1RecursiveASTVisitor.html). Il s'agit d'une classe qui effectue un parcours en profondeur de l'AST de Clang et visite chaque nœud. Elle dispose de méthodes telles que `VisitDecl()`, `VisitStmt()`, etc., qui peuvent nous aider à parcourir pratiquement tout l'AST du fichier source.

Elle dispose également d'une méthode particulièrement intéressante : [`TraverseDecl()`](https://clang.llvm.org/doxygen/classclang_1_1RecursiveASTVisitor.html#a99a9e941a07a015bc18d3613c5aa0914). Cette méthode parcourt récursivement toutes les déclarations à partir de la déclaration racine qui lui est donnée.

## Mettre le tout ensemble dans le code

Donc, maintenant, ce que nous devons faire est de donner à `TraverseDecl()` la déclaration racine de notre unité de traduction et il parcourra l'intégralité de celle-ci. Nous pouvons définir des 'hooks' spéciaux qui seront appelés lors de ce parcours. Un tel hook est :

```cpp
bool VisitRecordDecl(const clang::RecordDecl *record);
```

Cela est appelé chaque fois que le `RecursiveASTVisitor` parcourt un `CXXRecordDecl` - qui est le terme Clang pour une classe C++. Nous allons surcharger cette méthode avec notre propre version pour faire quelque chose d'intéressant : obtenir le nom de la classe C++ et voir si elle commence par un caractère majuscule.

En mettant tout cela ensemble, voici ce que nous obtenons :

```cpp
// Fichier d'en-tête MyFrontendAction.h
#pragma once

#include <clang/Frontend/FrontendAction.h>

class MyFrontendAction : public clang::ASTFrontendAction {
    protected:
        std::unique_ptr<clang::ASTConsumer> CreateASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) override;
};    

// Fichier source MyFrontendAction.cpp
#include "MyFrontendAction.h"
#include "MyASTConsumer.h"

std::unique_ptr<clang::ASTConsumer> MyFrontendAction::CreateASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) {
    return std::make_unique<MyASTConsumer>(ci, file);
}
```

```cpp

// Fichier d'en-tête MyASTConsumer.h

#pragma once

#include<clang/AST/ASTConsumer.h>
#include<clang/Frontend/CompilerInstance.h>

class MyASTConsumer : public clang::ASTConsumer {

public:
    MyASTConsumer(clang::CompilerInstance &ci, llvm::StringRef file) {}
    void HandleTranslationUnit(clang::ASTContext &context) override;
};

// Fichier source MyASTConsumer.cpp

#include <clang/AST/RecursiveASTVisitor.h>
#include "MyASTConsumer.h"

#include <iostream>

static bool isFirstLetterUpperCase(const std::string &str) {
    return str.size() != 0 && std::isupper(str[0]);
}
class MyASTVisitor : public clang::RecursiveASTVisitor<MyASTVisitor> {
    public:
    bool VisitCXXRecordDecl(const clang::RecordDecl *record) {
        std::string name = record->getNameAsString();

        if (!isFirstLetterUpperCase(name)) {
            std::cout << "Record Decl : " << name
                      <<" doesn't start with uppercase! \n";
        }

        return true;
    }
    bool TraverseDecl(clang::Decl *decl)  {
        return
           clang::RecursiveASTVisitor<MyASTVisitor>::TraverseDecl(decl);
    }
};

void MyASTConsumer::HandleTranslationUnit(clang::ASTContext &ctx) {
    clang::TranslationUnitDecl *tuDecl = ctx.getTranslationUnitDecl();
    MyASTVisitor visitor;
    visitor.TraverseDecl(tuDecl);
}

```

Maintenant, pour construire, nous faisons simplement :

`cd ~/ast-analyzer/build/;  ninja class-analyzer`

Cela construit l'exécutable `class-analyzer` dans le répertoire `build/bin`.

Maintenant, pour tester l'analyseur, nous créons un fichier source test.cpp :

```cpp
// test.cpp
class Test {
public:
 int a;
};

class testLower {
public:
 int b;
};

int main() {
        return 0;
}
```

Exécutez `class-analyzer` sur celui-ci :

```
bin/class-analyzer test.cpp
```

La sortie de cette commande est :

```
Record Decl : testLower doesn't start with uppercase!
```

Nous pouvons utiliser une multitude de méthodes `Visit*` telles que `VisitEnumDecl`, `VisitFunctionDecl`, `VisitVarDecl`, etc., pour obtenir des informations précieuses sur le fichier source et créer nos propres outils. Il suffit de penser à n'importe quel outil qui s'exécute et effectue des actions sur le code ou donne des suggestions à l'utilisateur.

Vous pourriez penser que cela semble être beaucoup de travail pour une petite tâche. Mais pensez au potentiel. Par exemple, vous pourriez écrire un outil qui donne automatiquement des suggestions à un utilisateur pour améliorer son style de code. Ou vous pourriez créer un outil qui analyse le code C++ et trouve des lignes de code où il pourrait y avoir des vulnérabilités de sécurité.

Les possibilités sont infinies. Les bibliothèques frontales de Clang sont extrêmement puissantes et vous pouvez construire de nombreux projets et outils intéressants avec elles.

## Résumé

Dans cet article, vous avez appris comment obtenir et utiliser la riche collection de bibliothèques frontales de Clang pour analyser un AST source C++. Vous pouvez utiliser ces bibliothèques pour écrire des outils intéressants d'analyse de code statique.

Comme cet article l'a montré, l'une des parties les plus importantes du voyage d'exploration des bibliothèques de Clang est l'art de lire la documentation de l'API et de l'appliquer aux problèmes que vos outils visent à résoudre. J'espère que vous avez apprécié l'article !