---
title: Comment compiler votre code C++ dans Visual Studio Code
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-10-07T05:14:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/banner-1.png
tags:
- name: C++
  slug: c-2
- name: compilers
  slug: compilers
- name: Visual Studio Code
  slug: vscode
seo_title: Comment compiler votre code C++ dans Visual Studio Code
seo_desc: 'C++ is a statically-typed, free-form, (usually) compiled, multi-paradigm,
  intermediate-level general-purpose middle-level programming language.

  In simple terms, C++ is a sophisticated, efficient, general-purpose programming
  language based on C.

  It wa...'
---

Le C++ est un langage de programmation généraliste, de niveau intermédiaire, multi-paradigme, (généralement) compilé, à typage statique et à forme libre.

En termes simples, le C++ est un langage de programmation sophistiqué, efficace et généraliste basé sur le C.

Il a été développé par [Bjarne Stroustrup](http://www.stroustrup.com/) en 1979.

L'une des principales caractéristiques du C++ est le compilateur. Celui-ci est utilisé pour compiler et exécuter du code C++.

> Un compilateur est un programme spécial qui traite les instructions écrites dans un langage de programmation particulier comme le C++ et les transforme en langage machine ou en "code" que le processeur d'un ordinateur utilise. ([Source](https://en.wikipedia.org/wiki/Compiler))

J'ai en fait écrit cet article parce que j'avais un devoir en C++ qui nécessitait l'utilisation d'un compilateur. Comme d'habitude, tout le monde utilisait l'IDE [CodeBlocks](http://www.codeblocks.org/) et l'IDE [Visual Studio](https://visualstudio.microsoft.com/). Mais j'étais déjà habitué à Visual Studio Code pour toutes mes activités de programmation.

J'ai alors cherché un moyen de compiler du C++ directement dans mon éditeur VsCode, d'où cet article :).

Dans cet article, je vais vous montrer comment configurer votre compilateur dans VsCode et vous donner quelques liens vers certaines des meilleures ressources C++.

![Image](https://media0.giphy.com/media/3o7TKUM3IgJBX2as9O/giphy.gif align="left")

# Prérequis

* Connaissances préalables en C++
    (Je suppose que vous apprenez le C++, que vous êtes sur le point de commencer à l'apprendre, ou que vous lisez simplement cela pour le plaisir. Cet article n'est pas un tutoriel C++ 101 – une certaine compréhension du C++ est nécessaire.)
    
* Éditeur Visual Studio Code
    Téléchargez [ici](https://code.visualstudio.com/#alt-downloads) et lisez la documentation d'installation pour [Windows](https://code.visualstudio.com/docs/?dv=win), [Linux](https://code.visualstudio.com/docs/?dv=linux64_deb) et [Mac](https://code.visualstudio.com/docs/?dv=osx)
    
* **Connexion Internet (!important)**
    

### **Avertissement !**

J'utiliserai un système d'exploitation Windows tout au long de cet article, mais je fournirai des liens vers des ressources qui aideront ceux qui utilisent d'autres systèmes d'exploitation.

Maintenant, commençons !

# Télécharger et installer un compilateur C++

* Rendez-vous sur www.mingw.org et cliquez sur le lien "Download/Installer" pour télécharger le fichier d'installation de MinGW, ou cliquez [ici](https://osdn.net/projects/mingw/downloads/68260/mingw-get-setup.exe/) pour Windows, [ici](http://www.mingw.org/wiki/LinuxCrossMinGW) pour Linux, et [ici](https://brewinstall.org/Install-mingw-w64-on-Mac-with-Brew/) pour Mac
    

> MinGW, une contraction de "Minimalist GNU for Windows", est un environnement de développement minimaliste pour les applications natives Microsoft Windows. ([Source](https://mingw.osdn.io/))

* Après le téléchargement, installez MinGW et attendez que le "MinGW Installation Manager" apparaisse.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture1.png align="left")

* Lorsque le "MinGW Installation Manager" apparaît, cliquez sur `mingw32-gcc-g++` puis sélectionnez "Mark for Installation"
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture2.png align="left")

* Dans le menu en haut à gauche, cliquez sur "Installation > Apply Changes"
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture3.png align="left")

* Attendez et permettez l'installation complète. Assurez-vous d'avoir une connexion Internet stable pendant ce processus.
    

# Modifier votre variable d'environnement PATH pour inclure le répertoire où se trouve le compilateur C++

> PATH est une variable d'environnement sur les systèmes d'exploitation de type Unix, DOS, OS/2 et Microsoft Windows, spécifiant un ensemble de répertoires où se trouvent les programmes exécutables. En général, chaque processus en cours d'exécution ou session utilisateur a son propre paramètre PATH. - [Wikipedia](https://en.wikipedia.org/wiki/PATH_(variable))

Après avoir installé MinGW, il peut être trouvé dans `C:\MinGW\bin`. Vous devez maintenant inclure ce répertoire dans votre variable d'environnement PATH. Si vous utilisez des ordinateurs depuis un certain temps, vous devriez déjà savoir comment faire cela, mais si ce n'est pas le cas, voici quelques ressources :

* Cliquez [ici](https://www.computerhope.com/issues/ch000549.htm) pour un guide Windows OS
    
* Cliquez [ici](https://www.cyberciti.biz/faq/unix-linux-adding-path/) pour Linux
    
* Cliquez [ici](https://hathaway.cc/2008/06/how-to-edit-your-path-environment-variables-on-mac/) pour un guide Mac OS
    

# Installer l'extension Code Runner dans VS Code

Maintenant que notre compilateur est configuré, installons Code Runner

Code Runner vous permet d'exécuter des extraits de code ou des fichiers de code pour plusieurs langages :

> C, C++, Java, JavaScript, PHP, Python, Perl, Perl 6, Ruby, Go, Lua, Groovy, PowerShell, BAT/CMD, BASH/SH, F# Script, F# (.NET Core), C# Script, C# (.NET Core), VBScript, TypeScript, CoffeeScript, Scala, Swift, Julia, Crystal, OCaml Script, R, AppleScript, Elixir, Visual Basic .NET, Clojure, Haxe, Objective-C, Rust, Racket, AutoHotkey, AutoIt, Kotlin, Dart, Free Pascal, Haskell, Nim, D, Lisp, Kit, et commande personnalisée.

* Cliquez [ici](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) pour télécharger
    
* Ou recherchez dans l'onglet marketplace de VsCode
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture4.png align="left")

* Après l'installation, redémarrez VsCode
    
* Ouvrez votre fichier C++ dans Vscode. Voici un programme hello world de base ci-dessous :
    

```c++
#include <iostream>
using namespace std;
int main() 
{
    cout << "Hello world!";
    return 0;
}
```

Enregistrez ce fichier sous `test.cpp`

# Exécuter votre code en utilisant Code Runner

* Utilisez le raccourci `Ctrl+Alt+N`
    
* Ou appuyez sur F1 puis sélectionnez/tapez Run Code
    
* Ou cliquez avec le bouton droit sur l'éditeur de texte puis cliquez sur Run Code dans le menu contextuel de l'éditeur
    

Le code s'exécutera et le résultat sera affiché dans la fenêtre de sortie. Ouvrez la fenêtre de sortie avec le raccourci `Ctrl+`.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Capture5.png align="left")

# Pour arrêter le code en cours d'exécution

* Utilisez le raccourci `Ctrl+Alt+M`
    
* Ou appuyez sur F1 puis sélectionnez/tapez Stop Code Run
    
* Ou cliquez avec le bouton droit sur le canal de sortie puis cliquez sur Stop Code Run dans le menu contextuel
    

Hourra, vous venez de configurer avec succès votre environnement C++ dans VsCode !

# Conclusion

Voici un petit conseil : Par défaut, le terminal de sortie de VsCode est en lecture seule. Si vous exécutez du code qui nécessite une entrée utilisateur comme :

```c++
#include <iostream>
using namespace std;

const double pi = 3.14159; 

void calculate()
{
  double area; 
  double radius;

  cout<<"Enter Radius: "<<endl; 
  cin>>radius;

  area = pi * radius * radius; 

  cout<<"area is: "<<area<<endl;
 }
 
int main()
{
  calculate(); 
  return 0;
}
```

vous ne pourrez pas taper dans le terminal, `Cannot edit in read-only terminal`.
Pour corriger cela, vous devez activer manuellement la lecture-écriture.

* Dans VsCode, allez dans Fichier > Préférence > Paramètres.
    
* Dans l'onglet Utilisateur sur le panneau de gauche, trouvez la section extensions
    
* Faites défiler et trouvez 'Run Code Configuration'
    
* Faites défiler et trouvez une case à cocher `Run in Terminal` (Exécuter le code dans le terminal intégré) Cochez la case.
    

OU

* Dans votre fichier `setting.json`, ajoutez :
    

```python
"code-runner.runInTerminal": true
```

Hourra, vous avez terminé et prêt à partir :).

# Ressources C++

Voici quelques ressources C++ que vous pouvez utiliser pour commencer à apprendre le C++

* [https://www.learncpp.com/](https://www.learncpp.com/)
    
* [https://www.codecademy.com/learn/learn-c-plus-plus](https://www.codecademy.com/learn/learn-c-plus-plus)
    
* [https://www.udemy.com/free-learn-c-tutorial-beginners/](https://www.udemy.com/free-learn-c-tutorial-beginners/)
    
* [https://www.sololearn.com/Course/CPlusPlus/](https://www.sololearn.com/Course/CPlusPlus/)
    
* [https://www.youtube.com/watch?v=vLnPwxZdW4Y](https://www.youtube.com/watch?v=vLnPwxZdW4Y)
    
* [https://www.tutorialspoint.com/cplusplus/cpp_useful_resources.htm](https://www.tutorialspoint.com/cplusplus/cpp_useful_resources.htm)
    
* [https://makeawebsitehub.com/learning-c/](https://www.tutorialspoint.com/cplusplus/cpp_useful_resources.htm)
    

# Crédits

* [Projet MinGW](http://www.mingw.org/)
    
* [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) par [Jun Han](https://marketplace.visualstudio.com/publishers/formulahendry)
    

Merci d'avoir lu !