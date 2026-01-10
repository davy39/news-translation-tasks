---
title: Comment exécuter et lancer du code Java depuis le terminal
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-10T19:20:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-execute-and-run-java-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Run-Java-Using-The-Terminal
seo_title: Comment exécuter et lancer du code Java depuis le terminal
---

freeCodeCamp-Cover-image.jpg
tags:
- name: Java
  slug: java
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "Si vous travaillez avec Java, vous avez probablement utilisé l'un des éditeurs de texte bien connus comme Sublime Text, VS Code, Brackets, Atom et Notepad++, ainsi que des IDE comme Apache NetBeans et IntelliJ IDEA. \nExécuter du code dans votre IDE est simple, mais vous ne voyez pas souvent comment il s'exécute..."
---

Si vous travaillez avec Java, vous avez probablement utilisé l'un des éditeurs de texte bien connus comme Sublime Text, VS Code, Brackets, Atom et Notepad++, ainsi que des IDE comme Apache NetBeans et IntelliJ IDEA.

Exécuter du code dans votre IDE est simple, mais vous n'avez pas souvent l'occasion de voir comment il exécute votre code (même si vous pouvez bien sûr vérifier la commande dans le terminal !).

Cependant, c'est une bonne pratique de savoir comment votre code s'exécute réellement et fournit le résultat qu'il vous donne.

Beaucoup d'entre vous ont peut-être entendu dire que les programmeurs professionnels expérimentés utilisent également le terminal pour exécuter les programmes. Cela leur donne une meilleure clarté et les aide à comprendre comment le code fonctionne, où il renvoie la valeur souhaitée, où pourrait se trouver le bug, et ainsi de suite.

Quel que soit votre objectif, exécuter du code Java directement depuis le terminal est une tâche très facile.

Dans cet article, je vais vous montrer comment vous pouvez exécuter Java directement depuis votre fenêtre de terminal préférée. N'ayez crainte ! La procédure est assez simple, et après avoir lu l'article en entier, vous devriez être capable de lancer votre propre code Java dans le terminal.

## Comment exécuter du code Java dans le terminal

Le processus que je vais vous montrer dans cet article est applicable à n'importe quel système d'exploitation, qu'il s'agisse de Windows, MacOS ou Linux.

J'utiliserai le code Java suivant dans l'étape suivante.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

## 📦 Étape 1 – Allez dans le répertoire où se trouve votre code source

Si vous avez déjà écrit votre code Java dans un éditeur, allez simplement dans ce répertoire. Vous pouvez vous rendre directement dans le répertoire via votre gestionnaire de fichiers si vous le souhaitez.

### Comment aller dans le répertoire où se trouve le code source : pour Windows 🪟

Supposons que j'ai le code source ( `Main.java` ) dans le dossier `Ce PC` > `Documents`. Je peux simplement m'y rendre via mon explorateur de fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Untitled.png)

Ou, si je le souhaite, je peux aussi m'y rendre en utilisant mon terminal. Je dois utiliser `cd` pour indiquer que je veux **changer de répertoire** (change directory).

Dans ce cas, je peux utiliser `cd "C:\Users\Md. Fahim Bin Amin\Documents"`. Comme mon nom d'utilisateur contient des espaces, j'ai utilisé des guillemets `"` `"` pour les encadrer.

Ensuite, si je vérifie tous les fichiers de ce répertoire, j'obtiendrai également le fichier `Main.java`.

Cette fois, j'ai placé le fichier `Main.java` sur mon lecteur **D**. Je me suis donc rendu dans ce répertoire en utilisant la commande `cd`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-022040.png)

J'obtiens également mon fichier Java dans le terminal.

### Comment aller dans le répertoire où se trouve le code source : pour Linux 🐧

Vous pouvez aller dans le répertoire où vous avez conservé votre code source soit en suivant la méthode classique via l'interface graphique (GUI), soit depuis le terminal en utilisant également la commande `cd`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124200.png)
_en utilisant l'interface graphique classique_

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124317.png)
_en utilisant la commande cd_

## 🧑‍💻 Comment compiler le code Java

Avant de lancer notre code Java, nous devons d'abord le compiler. Pour compiler un code/programme Java, nous générons le fichier class. Ensuite, nous devons exécuter/lancer ce fichier class.

### Comment compiler du code Java en utilisant le terminal

Nous devons utiliser la commande `javac nom_du_fichier_avec_extension`. Par exemple, comme je veux compiler mon `Main.java`, j'utiliserai la commande `javac Main.java`. Le `c` dans `javac` signifie compiler (compile).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122312.png)

Si le processus de compilation réussit, nous n'obtiendrons aucune erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122345.png)

Cela créera le fichier class dont nous avons besoin dans le même répertoire.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-122628.png)

Gardez à l'esprit que nous lançons le fichier **class**, et non le fichier `.java`.

Le même processus est applicable à tous les systèmes d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-124951.png)
_sous Linux_

## 🖥️ Comment exécuter le code Java

Nous lançons le fichier `.class` pour exécuter les programmes Java. Pour cela, nous utilisons la commande `java nom_du_fichier_class_sans_extension`. Par exemple, comme notre fichier `.class` pour ceci est `Main.class`, notre commande sera `java Main`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-125223.png)

Le programme Java a été exécuté avec succès !

La procédure est exactement la même pour les autres systèmes d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-125317.png)
_sous Linux_

## 🏆 Bonus : Comment exécuter un programme Java avec des packages

Un package signifie essentiellement un dossier. Précédemment, je vous ai montré comment utiliser n'importe quel code Java classique via le terminal. Là, je n'ai utilisé aucun package à l'intérieur du code Java.

Maintenant, je vais vous montrer comment vous pouvez lancer n'importe quel code Java dans lequel des packages sont déclarés. Cette fois, j'utiliserai le code Java suivant.

```java
package myJavaProgram.Source;
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

Dans la première ligne, j'ai écrit le package sous la forme `package myJavaProgram.Source`. Cela indique que je veux créer un dossier nommé `myJavaProgram`. Ensuite, je veux créer un autre dossier à l'intérieur nommé `Source`. Enfin, je veux créer le fichier class de mon code Java à l'intérieur du dossier `Source`.

L'arborescence du répertoire ressemble à ceci : **myJavaProgram > Source.**

Pour compiler ce type de code Java avec des packages, nous utilisons la commande `javac -d . nom_du_fichier_avec_extension`.

Pour l'instant, j'utilise le fichier `Main.java`, donc j'appliquerai la commande `javac -d . Main.java`. Cela créera un dossier nommé **myJavaProgram**, puis un autre dossier nommé **Source** sous le dossier **myJavaProgram**, dans le répertoire où se trouve actuellement mon fichier source.

- Le_Répertoire_Où_J'ai_Gardé_Mon_Code_Source
	- dossier `myJavaProgram` 
		- dossier `Source` 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134626.png)

Cela crée instantanément le dossier **myJavaProgram**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134710.png)

À l'intérieur de ce dossier, il crée le dossier **Source**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134806.png)

À l'intérieur du dossier Source, il crée notre fichier `.class`. Nous avons besoin de ce fichier pour lancer le programme Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-134853.png)

Maintenant, si nous voulons lancer le fichier `.class`, nous devons modifier un peu la commande, car nous devons fournir le répertoire du fichier `.class` dans la fenêtre du terminal.

Nous utilisons la commande suivante pour lancer le programme Java avec des packages : `java repertoire_du_fichier_class.nom_du_fichier_class_sans_extension`.

Comme j'utilise `Main.java` et que je dois lancer le fichier `Main.class`, ma commande sera `java myJavaProgram.Source.Main`. Cela lancera le code Java comme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-135226.png)

Si vous vous demandez pourquoi nous changeons la commande maintenant, c'est parce qu'auparavant, nous n'avions déclaré aucun package. Le compilateur Java avait donc créé le fichier `.class` dans le répertoire où se trouvait notre code source. Nous pouvions donc obtenir le fichier `.class` directement là et l'exécuter également.

Mais si nous déclarons des packages à l'intérieur du code source comme ceci, nous disons au compilateur de créer le fichier `.class` à un autre endroit (pas dans le répertoire où se trouve actuellement notre code source). Cela signifie que nous n'obtenons pas le fichier class directement sur place.

Comme nous voulons lancer le fichier class, nous devons dire explicitement au compilateur où se trouve actuellement le fichier class afin qu'il puisse le récupérer et l'exécuter.

Si vous avez peur de vous tromper à cette étape, vous pouvez copier le répertoire directement depuis votre code Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-135404.png)

À la ligne 1, nous avons déclaré le répertoire du package (où nous voulons que le fichier class soit généré). Donc, si nous copions simplement le répertoire et ajoutons le nom du fichier `.class` sans l'extension ( `.class` ) plus tard avec un point ( `.` ), cela satisfait la condition pour exécuter n'importe quel code Java ayant des packages déclarés dans le code source.

Le même processus est également applicable pour les autres systèmes d'exploitation. Je fournis ici des captures d'écran d'un système Linux :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-10-140017.png)
_Exécution de codes Java avec des packages sur une machine Linux_

Beau travail ! 👏 Vous pouvez maintenant exécuter n'importe quel code/programme Java directement en utilisant un terminal. 🥳

J'ai également créé une vidéo où j'ai montré tous les processus mentionnés ci-dessus. Vous pouvez la consulter [ici](https://www.youtube.com/watch?v=e_lmKSCH9YE). 😁

## 💁‍♂️ Conclusion

J'espère que cet article vous aidera à exécuter vos programmes Java en utilisant simplement le terminal.

➡️ Si vous voulez savoir comment installer un compilateur Java pour votre système d'exploitation Windows, [vous pouvez consulter cet article](https://www.freecodecamp.org/news/how-to-install-java-on-windows/).

➡️ Si vous voulez savoir comment installer des compilateurs C et C++ pour votre système d'exploitation Windows, [vous pouvez consulter cet article](https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/).

➡️ Si vous voulez savoir comment installer Python sur votre système Windows, [vous pouvez consulter cet article](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/).

Merci d'avoir lu l'article en entier. S'il vous a aidé, vous pouvez également consulter mes autres articles sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez me contacter, vous pouvez le faire via [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/) et [GitHub](https://github.com/FahimFBA).

Vous pouvez également vous [ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre régulièrement divers langages de programmation avec de nombreux exemples pratiques.

Si vous voulez voir mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce sur quoi je travaille.

Merci beaucoup !"