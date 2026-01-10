---
title: Comment apprendre le langage de programmation C++
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-04-11T17:10:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-the-c-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/How-to-Learn-the-C
seo_title: Comment apprendre le langage de programmation C++
---

Programming-Language.png
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "Dans les premiers jours de la programmation informatique, les programmeurs devaient écrire des instructions individuelles en langage d'assemblage une par une. \nPlus tard, des langages de programmation \n  comme FORTRAN et COBOL ont été créés. Le problème avec ces langages était qu'ils étaient ..."
---

Dans les premiers jours de la programmation informatique, les programmeurs devaient écrire des instructions individuelles en langage d'assemblage une par une. 

Plus tard, des langages de programmation comme FORTRAN et COBOL ont été créés. Le problème avec ces langages était qu'ils étaient ciblés pour un certain groupe de personnes – FORTRAN pour les ingénieurs et les scientifiques et COBOL pour les hommes d'affaires.

Puis, dans les années 60, un nouveau langage appelé Simula a émergé et a introduit le concept de classe, qui permettait à peu près à n'importe qui de créer des logiciels pour leurs domaines spéciaux.

Après cela, dans les années 80, Bjarne Stroustrup a eu l'idée de combiner l'abstraction générale de Simula avec les fonctionnalités de bas niveau de C, qui était à l'époque le meilleur langage pour le travail. 

Ainsi, "C with Classes" est né, qui est ensuite devenu connu sous le nom de langage de programmation C++.

Le langage de programmation C++ est un langage de programmation statiquement typé, compilé, multi-paradigme, à usage général, notoire pour sa courbe d'apprentissage abrupte. Il est largement utilisé dans le développement de jeux vidéo, de logiciels de bureau et de systèmes embarqués. 

C++ est quelque peu complexe et extrêmement puissant – et pour être honnête, si vous planifiez correctement votre feuille de route d'apprentissage, C++ n'est pas aussi mauvais que beaucoup de gens pourraient vous le faire croire.

Dans cet article, je vais commencer par vous montrer les bases du langage de programmation C++. 

Si vous avez déjà programmé, cette introduction devrait être assez simple pour vous. Mais si vous apprenez C++ comme premier langage de programmation, vous pourriez trouver cela assez difficile en raison de la quantité de concepts que vous devrez comprendre.

Une fois que j'aurai terminé l'introduction, je vous donnerai une liste de ressources d'apprentissage de haute qualité ainsi que des recommandations sur la manière d'en tirer le meilleur parti.

Alors sans plus attendre, plongeons-nous.

## Table des matières

- [Aperçu de haut niveau de C++](#heading-apercu-de-haut-niveau-de-c)
    - [Hello World](#heading-hello-world)
    - [Comprendre un programme C++](#heading-comprendre-un-programme-c)
    - [Types de données courants et tableaux](#heading-types-de-donnees-courants-et-tableaux)
    - [Contrôle de flux](#heading-controle-de-flux)
    - [Fonctions](#heading-fonctions)
- [Ressources d'apprentissage de C++](#heading-ressources-dapprentissage-de-c)
    - [Apprendre C++ en 31 heures](#heading-apprendre-c-en-31-heures)
    - [Apprendre C++ en 4 heures](#heading-apprendre-c-en-4-heures)
    - [Programmation Orientée Objet (POO) en C++](#heading-programmation-orientee-objet-poo-en-c)
    - [Cours accéléré sur OpenGL](#heading-cours-accelere-sur-opengl)
    - [Unreal Engine en 5 heures](#heading-unreal-engine-en-5-heures)
- [Conclusion](#heading-conclusion)

## Aperçu de haut niveau de C++

Avant de plonger dans la feuille de route d'apprentissage et la section des ressources, je voudrais vous présenter le langage de programmation C++ lui-même. De cette façon, vous ne vous sentirez pas submergé une fois que vous commencerez à plonger dans les ressources mentionnées ci-dessous. 

Gardez à l'esprit que cette section suppose que vous avez de l'expérience dans l'utilisation d'un autre langage de programmation tel que Python ou JavaScript.

### Hello World

Comme je l'ai déjà mentionné, C++ est un langage de programmation statiquement typé et compilé, et il existe un certain nombre de compilateurs disponibles. 

Le GCC ou GNU Compiler Collection est l'un des compilateurs les plus populaires pour C++ et mon collègue auteur de freeCodeCamp [Md. Fahim Bin Amin](https://www.freecodecamp.org/news/author/fahimbinamin/) a écrit un excellent guide sur [Comment installer les compilateurs C et C++ sur Windows](https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/). 

Selon votre distribution Linux, l'une des commandes suivantes devrait installer GCC pour vous :

```bash
# Debian/Ubuntu
sudo apt install build-essential

# Fedora
sudo dnf install make automake gcc gcc-c++

# Arch Linux
sudo pacman -S base-devel
```

Sur un Mac, vous pouvez soit installer GCC en utilisant [Homebrew](https://brew.sh/), soit suivre le guide écrit par un autre auteur de freeCodeCamp [Daniel Kehoe](https://www.freecodecamp.org/news/author/danielkehoe/) sur [Comment installer les outils de ligne de commande Xcode sur un Mac](https://www.freecodecamp.org/news/install-xcode-command-line-tools/).

Outre GCC, il y a aussi MSVC ou Microsoft Visual C++ compiler sur Windows. Pour installer MSVC, rendez-vous sur [https://visualstudio.com/](https://visualstudio.com/), téléchargez le dernier installateur et installez la charge de travail "Développement de bureau avec C++" :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-120.png)

Une fois que vous avez fait cela, vous devriez être en mesure d'écrire et de compiler des programmes C++ sur votre ordinateur. Pour ce faire, créez un fichier `hello-world.cpp` n'importe où sur votre ordinateur et mettez le code suivant dedans :

```cpp
#include <iostream>

int main() {
	std::cout << "Hello World!" << std::endl;
    
    return 0;
}
```

Maintenant, si vous utilisez GCC, ouvrez une fenêtre de terminal dans le même répertoire où se trouve le fichier `hello-world.cpp` et exécutez la commande suivante :

```
g++ -o hello-world hello-world.cpp
```

Cette commande compilera le fichier `hello-world.cpp` dans le fichier indiqué dans l'option `-o`. Vous devriez voir un nouveau fichier binaire nommé `hello-world` dans le même dossier. Exécutez le fichier à partir du terminal comme suit :

```bash
./hello-world

# Hello World!
```

Si vous utilisez MSVC, ouvrez le menu Démarrer et recherchez "Developer PowerShell" et ouvrez le programme approprié selon votre version de Visual Studio :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/developer-powershell.png)

Maintenant, accédez au répertoire où vous avez enregistré votre fichier `hello-world.cpp` et exécutez la commande suivante :

```bash
cl -o hello-world hello-world.cpp
```

Comme la commande `g++`, cela compilera votre fichier `hello-world.cpp` en un binaire exécutable `hello-world.exe`. Exécutez le fichier en utilisant la commande suivante :

```bash
.\hello-world.exe

# Hello World!
```

### Comprendre un programme C++

Maintenant que vous avez écrit votre premier programme C++, il est temps de comprendre ce que vous venez de faire. Regardons à nouveau le code source :

```cpp
#include <iostream>

int main() {
	std::cout << "Hello World!" << std::endl;
    
    return 0;
}
```

Le fichier source contient quatre lignes de code au total. La première ligne est `#include <iostream>` et elle fait exactement ce qu'elle semble faire. Elle inclut le contenu du fichier d'en-tête `iostream` dans le fichier `hello-world.cpp`. 

Les fichiers d'en-tête contiennent des déclarations de choses comme les objets `std::cout` et `std::endl`. Le fichier d'en-tête `iostream` traite des flux d'entrée et de sortie.

Après l'instruction `#include`, les lignes `int main(){}` déclarent et définissent une nouvelle fonction. Cette fonction `main()` sera appelée par le système d'exploitation lorsque vous exécuterez votre programme et chaque programme exécutable C++ doit avoir une fonction `main()`.

Tout ce que vous écrivez entre les accolades fera partie de cette fonction. Dans le code mentionné ci-dessus, l'objet `std::cout` imprime toute chaîne qui vient après le signe `<<`. L'objet `std::endl` ajoute un caractère de nouvelle ligne à la fin de la ligne. Vous pouvez enchaîner plusieurs choses à sortir dans un seul appel `std::cout` comme suit :

```cpp
#include <iostream>

int main() {
	std::cout << "Hello World!" << " " << "C++ est génial!" << std::endl;
    
    return 0;
}
```

Si vous compilez et exécutez ce programme, vous obtiendrez la sortie suivante :

```bash
Hello World! C++ est génial!
```

Le mot `int` dans la déclaration de la fonction signifie simplement que cette fonction retourne un entier. Retourner `0` à la fin d'un programme signifie qu'il s'est exécuté avec succès. Une valeur de retour non nulle indique généralement une sorte d'échec, mais ce sujet est hors du cadre de cet article.

### Types de données courants et tableaux

C++ a sept types de données fondamentaux. Ils sont les suivants :

| Type de donnée | Signification               |
| -------------- | --------------------------- |
| `int`          | Entier                      |
| `float`        | Nombre à virgule flottante  |
| `double`       | Double précision flottante  |
| `char`         | Caractère                   |
| `w_char`       | Caractère large             |
| `bool`         | Booléen                     |
| `void`         | Vide                        |

Il existe des modificateurs tels que `short`, `long`, `signed`, et `unsigned`, mais je ne les aborderai pas dans cet aperçu de haut niveau. 

Pour déclarer une variable d'un certain type de donnée, vous pouvez faire quelque chose comme ceci :

```cpp
#include<iostream>

int main() {
	int number = 25;

	std::cout << "Le nombre est " << number << std::endl;
    
    return 0;
}
```

Si vous compilez et exécutez ce programme, la sortie sera :

```
Le nombre est 25
```

Il y a aussi des tableaux qui sont capables de stocker plusieurs valeurs du même type. Donc si vous voulez déclarer un tableau de type `int`, vous pouvez le faire comme suit :

```cpp
#include<iostream>

int main() {
	int numbers[] = { 1, 2, 3, 4, 5 };

	std::cout << "Le nombre est " << numbers[0] << std::endl;

	return 0;
}
```

Vous pouvez accéder à n'importe quel élément du tableau en suivant la syntaxe `array_name[element_index]`. Les index des tableaux sont basés sur zéro, donc pour accéder au premier élément, vous devrez écrire `numbers[0]`, et la sortie du code ci-dessus sera :

```
Le nombre est 1
```

Vous pouvez également créer des chaînes de caractères en utilisant des tableaux de type `char` comme suit :

```cpp
#include<iostream>

int main() {
	char name[] = "Farhan";

	std::cout << "Mon nom est " << name << std::endl;

	return 0;
}
```

La sortie de ce programme sera :

```
Mon nom est Farhan
```

Il y a aussi `std::string`, mais je ne l'aborderai pas ici. Vous pouvez [en lire plus ici](https://www.freecodecamp.org/news/c-string-std-string-example-in-cpp/).

### Contrôle de flux

En C++, il y a les méthodes courantes de contrôle du flux de votre programme telles que les instructions if-else, les instructions switch, les boucles, les breaks, etc. 

Dans cette section, je vais vous montrer un exemple d'instruction if-else, d'une boucle for et d'une instruction break. 

Jetez un coup d'œil au programme suivant :

```cpp
#include<iostream>

int main() {
	int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

	for (int i = 0; i < 10; i++) {
		if (numbers[i] == 5) {
			std::cout << numbers[i] << std::endl;

			break;
		}
	}

	return 0;
}
```

C'est un programme simple qui parcourt un tableau d'entiers et vérifie si l'élément actuel est 5 ou non. Si c'est le cas, le programme imprimera le nombre et sortira de la boucle. Cela peut également être fait en utilisant une boucle for basée sur une plage comme suit :

```cpp
#include<iostream>

int main() {
	int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

	for (auto number : numbers) {
		if (number == 5) {
			std::cout << number << std::endl;

			break;
		}
	}

	return 0;
}
```

Le mot-clé `auto` déduira automatiquement le type de la variable. Cette syntaxe est à nouveau hors du cadre de cet article, mais je voulais simplement vous montrer ce que vous pouvez faire en C++.

### Fonctions

Comme tout autre langage de programmation, C++ a également des fonctions. Vous pouvez en créer une comme suit :

```cpp
#include<iostream>

int add(int a, int b) {
	return a + b;
}

int main() {
	std::cout << "La somme est " << add(8, 2) << std::endl;

	return 0;
}
```

Dans cet exemple, j'ai créé une fonction nommée `add()` qui retourne un `int` et prend `int a` et `int b` comme paramètres. 

Lorsque vous appelez cette fonction et lui passez deux entiers, la fonction additionnera simplement les deux nombres et retournera la somme. C'est probablement la forme la plus simple de fonction en C++. En réalité, les fonctions peuvent devenir beaucoup plus complexes que cela.

Maintenant que vous avez une idée très brève de la façon dont le langage de programmation C++ fonctionne, je vais vous présenter quelques ressources d'apprentissage de très haute qualité sur YouTube que vous pouvez utiliser pour apprendre C++.

## Ressources d'apprentissage de C++

Dans cette section, je vais vous donner une liste de vidéos gratuites et géniales sur C++. Commençons par la première.

### Apprendre C++ en 31 heures

%[https://youtu.be/8jLOx1hD3_o]

C'est la dernière vidéo sur C++ de la chaîne YouTube de freeCodeCamp. Elle dure 31 heures et aborde chaque concept important de C++. C'est aussi la vidéo la plus à jour de la liste. 

L'instructeur **Daniel Gakwaya** est un développeur logiciel expérimenté et sait ce qu'il fait. Si vous commencez avec C++ en 2022, c'est la vidéo à suivre.

Mais il y a quelques choses à garder à l'esprit lorsque vous regardez cette vidéo. Je l'ai regardée moi-même pour rafraîchir mes compétences en C++ et je peux dire par expérience que vous pourriez vous sentir submergé au moment où vous atteignez le milieu de la vidéo.

Ne vous inquiétez pas, c'est tout à fait normal. Ce que je vous suggère de faire, c'est de ne pas essayer de regarder toute la vidéo d'une traite. De cette façon, vous ne vous souviendrez de rien.

Commencez par le **Chapitre 1** et regardez la vidéo jusqu'au **Chapitre 7**. Assurez-vous de faire des pauses après chaque chapitre et de pratiquer ce que vous avez appris. 

Une fois que vous avez atteint le Chapitre 7, vous devriez être capable de résoudre n'importe quel problème de programmation de base en utilisant C++. Alors trouvez une plateforme de résolution de problèmes de programmation qui vous convient et commencez à résoudre des problèmes en utilisant C++. 

Une fois que vous vous sentez confiant dans ce que vous avez déjà appris, revenez à la vidéo et continuez à la regarder.

Ensuite, je vous suggère de regarder un chapitre par jour à partir du Chapitre 8. Parce que ce sont tous des sujets intermédiaires à avancés et prendront du temps pour être correctement compris. Ne vous précipitez pas, prenez votre temps.

### Apprendre C++ en 4 heures

%[https://youtu.be/vLnPwxZdW4Y]

Si vous pensez que 31 heures est un peu trop pour vous, alors je vous suggère celle-ci. C'est l'une des vidéos les plus anciennes de la chaîne et enseigne la plupart des concepts fondamentaux de C++ assez bien. 

L'instructeur **Mike** de **Giraffe Academy** a créé plusieurs cours sur la chaîne freeCodeCamp et est bien connu pour ses tutoriels longs et agréables.

L'instructeur construira quelques projets simples comme une calculatrice et un jeu de mad libs pendant la vidéo. Assurez-vous de comprendre ce qu'il fait et essayez d'implémenter ces projets par vous-même. De cette façon, vous apprendrez bien mieux qu'en copiant simplement ce qu'il fait dans la vidéo.

### Programmation Orientée Objet (POO) en C++

%[https://youtu.be/wN0x9eZLix4]

Cette vidéo est un peu différente des précédentes. Supposons que vous connaissez C++ mais que vous n'êtes pas confiant dans votre compréhension de la programmation orientée objet. Dans ce cas, cette vidéo vous aidera énormément. C'est une vidéo de 1,5 heure entièrement dédiée à la programmation orientée objet en C++. 

L'instructeur **Saldina Nurak** alias **CodeBeauty** est une développeuse logicielle et dirige [une chaîne entière dédiée à C++](https://www.youtube.com/c/CodeBeauty/). N'hésitez pas à consulter son contenu.

### Cours accéléré sur OpenGL

%[https://youtu.be/45MIykWJ-C4]

Supposons que vous avez maîtrisé C++ en suivant l'une des vidéos précédentes et que vous voulez maintenant faire quelque chose de fun. Eh bien, l'une des choses les plus courantes que vous pouvez faire avec C++ est de travailler avec des graphiques. 

Dans ce cours vidéo d'environ 2 heures par **Victor Gordan**, vous n'apprendrez pas seulement à appliquer vos compétences en C++ pour rendre de jolis graphiques à l'écran, mais vous obtiendrez également une bonne compréhension de la façon dont les graphiques informatiques fonctionnent en général.

La vidéo nécessite une compréhension de la POO en C++ et quelques compétences en mathématiques. Même si vous n'êtes pas confiant en mathématiques, essayez la vidéo. Vous pourriez la trouver amusante. 

Si vous aimez celle-ci et que vous voulez en apprendre plus, le même instructeur a une autre vidéo sur les parties avancées d'OpenGL

%[https://youtu.be/GJFHqK_-ARA]

Dans celle-ci, vous apprendrez beaucoup plus de choses avancées sur OpenGL et vous aurez besoin d'une compréhension des sujets couverts dans les vidéos précédentes.

Il y a un autre instructeur **Etay Meiri** qui a créé un cours vraiment cool sur OpenGL sur la chaîne YouTube de freeCodeCamp.

%[https://youtu.be/GZQkwx10p-8]

Dans celle-ci, l'instructeur fait un travail génial en vous apprenant à implémenter des animations squelettiques en utilisant OpenGL. 

Mais cette vidéo aborde quelques concepts vraiment avancés, alors assurez-vous d'avoir une bonne maîtrise de C++ et une tasse de café à proximité.

### Unreal Engine en 5 heures

%[https://youtu.be/LsNW4FPHuZE]

Si vous pensez que le rendu graphique manuel à l'écran n'est pas votre truc et que vous voulez utiliser vos nouvelles compétences en C++ d'une autre manière, alors cette vidéo vous intéressera sûrement.

Dans ce cours vidéo de 5 heures d'Awesome Tuts, vous créerez trois jeux complets à partir de zéro en utilisant Unreal Engine et C++. Bien que la vidéo utilise Unreal Engine 4 et non 5, vous devriez être en mesure de transférer vos connaissances de cette vidéo à UE5 assez facilement.

Si vous aimez celle-ci et que vous voulez plus de vidéos sur UE et C++, il y en a deux autres du même instructeur.

%[https://youtu.be/SOjZTmOMGcY]

Dans celle-ci, vous apprendrez à créer un jeu de course sans fin comme Subway Surfer ou Temple Run en utilisant Unreal Engine 4 et C++.

%[https://youtu.be/4HoJIgyclZ4]

Si vous n'êtes pas fan des jeux de course sans fin et que vous voulez créer un jeu de tir à la première personne, l'instructeur a également une vidéo sur cela.

## Conclusion

Je voudrais vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article. J'espère que vous avez appris des choses précieuses dans cet article et n'oubliez jamais :

> "La seule façon d'apprendre un nouveau langage de programmation est d'écrire des programmes avec." -- Dennis Ritchie

Alors continuez à appliquer ce que vous apprenez sur C++, créez des projets fantastiques, partagez-les sur GitHub, et vous deviendrez un magicien de C++ en un rien de temps. 

J'ai également un blog personnel où j'écris sur des sujets technologiques aléatoires, alors si vous êtes intéressé par quelque chose comme ça, consultez [https://farhan.dev](https://farhan.dev). Si vous avez des questions ou si vous êtes confus à propos de quelque chose – ou si vous voulez simplement entrer en contact – je suis disponible sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/).