---
title: Gestion des fichiers en C — Comment ouvrir, fermer et écrire dans des fichiers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/file-handling-in-c-how-to-open-close-and-write-to-files
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d31740569d1a4ca3667.jpg
tags:
- name: C
  slug: c-3
- name: toothbrush
  slug: toothbrush
seo_title: Gestion des fichiers en C — Comment ouvrir, fermer et écrire dans des fichiers
seo_desc: "If you’ve written the C helloworld program before, you already know basic\
  \ file I/O in C:\n/* A simple hello world in C. */\n#include <stdlib.h>\n\n// Import\
  \ IO functions.\n#include <stdio.h>\n\nint main() {\n    // This printf is where\
  \ all the file IO magic ..."
---

Si vous avez déjà écrit le programme C `helloworld`, vous connaissez déjà les bases de l'I/O de fichiers en C :

```c
/* Un simple hello world en C. */
#include <stdlib.h>

// Importer les fonctions d'I/O.
#include <stdio.h>

int main() {
    // Ce printf est l'endroit où toute la magie de l'I/O de fichiers se produit !
    // Comme c'est excitant !
    printf("Hello, world!\n");
    return EXIT_SUCCESS;
}
```

La gestion des fichiers est l'une des parties les plus importantes de la programmation. En C, nous utilisons un pointeur de structure de type fichier pour déclarer un fichier :

```c
FILE *fp;
```

C fournit un certain nombre de fonctions intégrées pour effectuer des opérations de base sur les fichiers :

* `fopen()` - créer un nouveau fichier ou ouvrir un fichier existant
* `fclose()` - fermer un fichier
* `getc()` - lit un caractère depuis un fichier
* `putc()` - écrit un caractère dans un fichier
* `fscanf()` - lit un ensemble de données depuis un fichier
* `fprintf()` - écrit un ensemble de données dans un fichier
* `getw()` - lit un entier depuis un fichier
* `putw()` - écrit un entier dans un fichier
* `fseek()` - définit la position à un point désiré
* `ftell()` - donne la position actuelle dans le fichier
* `rewind()` - définit la position au point de début

### **Ouvrir un fichier**

La fonction `fopen()` est utilisée pour créer un fichier ou ouvrir un fichier existant :

```c
fp = fopen(const char filename, const char mode);
```

Il existe de nombreux modes pour ouvrir un fichier :

* `r` - ouvre un fichier en mode lecture
* `w` - ouvre ou crée un fichier texte en mode écriture
* `a` - ouvre un fichier en mode ajout
* `r+` - ouvre un fichier en mode lecture et écriture
* `a+` - ouvre un fichier en mode lecture et écriture
* `w+` - ouvre un fichier en mode lecture et écriture

Voici un exemple de lecture de données depuis un fichier et d'écriture dans celui-ci :

```c
#include<stdio.h>
#include<conio.h>
main()
{
FILE *fp;
char ch;
fp = fopen("hello.txt", "w");
printf("Enter data");
while( (ch = getchar()) != EOF) {
  putc(ch,fp);
}
fclose(fp);
fp = fopen("hello.txt", "r");

while( (ch = getc(fp)) != EOF)
  printf("%c",ch);
  
fclose(fp);
}
```

Maintenant, vous pourriez penser : "Cela imprime simplement du texte à l'écran. En quoi est-ce de l'I/O de fichier ?"

La réponse n'est pas évidente au premier abord et nécessite une certaine compréhension du système UNIX. Dans un système UNIX, tout est traité comme un fichier, ce qui signifie que vous pouvez lire et écrire dedans.

Cela signifie que votre imprimante peut être abstraite comme un fichier puisque tout ce que vous faites avec une imprimante est d'écrire avec elle. Il est également utile de penser à ces fichiers comme des flux, car, comme vous le verrez plus tard, vous pouvez les rediriger avec le shell.

Alors, comment cela se rapporte-t-il à `helloworld` et à l'I/O de fichier ?

Lorsque vous appelez `printf`, vous écrivez en réalité simplement dans un fichier spécial appelé `stdout`, abréviation de **sortie standard**. `stdout` représente la sortie standard telle que décidée par votre shell, qui est généralement le terminal. Cela explique pourquoi il a été imprimé à votre écran.

Il existe deux autres flux (c'est-à-dire fichiers) qui sont disponibles pour vous avec effort, `stdin` et `stderr`. `stdin` représente l'**entrée standard**, que votre shell attache généralement au clavier. `stderr` représente la sortie d'**erreur standard**, que votre shell attache généralement au terminal.

### **I/O de fichier rudimentaire, ou Comment j'ai appris à poser des tuyaux**

Assez de théorie, passons aux choses sérieuses en écrivant du code ! La manière la plus simple d'écrire dans un fichier est de rediriger le flux de sortie en utilisant l'outil de redirection de sortie, `>`.

Si vous voulez ajouter, vous pouvez utiliser `>>` :

```bash
# Cela affichera à l'écran...
./helloworld
# ...mais cela écrira dans un fichier !
./helloworld > hello.txt
```

Le contenu de `hello.txt` sera, sans surprise,

```text
Hello, world!
```

Supposons que nous avons un autre programme appelé `greet`, similaire à `helloworld`, qui vous salue avec un `name` donné :

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Initialiser un tableau pour contenir le nom.
    char name[20];
    // Lire une chaîne et l'enregistrer dans name.
    scanf("%s", name);
    // Imprimer le message de salutation.
    printf("Hello, %s!", name);
    return EXIT_SUCCESS;
}
```

Au lieu de lire depuis le clavier, nous pouvons rediriger `stdin` pour lire depuis un fichier en utilisant l'outil `<` :

```bash
# Écrire un fichier contenant un nom.
echo Kamala > name.txt
# Cela lira le nom depuis le fichier et imprimera la salutation à l'écran.
./greet < name.txt
# ==> Hello, Kamala!
# Si vous vouliez également écrire la salutation dans un fichier, vous pourriez le faire en utilisant ">".
```

Note : ces opérateurs de redirection sont dans `bash` et les shells similaires.

### **Le vrai truc**

Les méthodes ci-dessus ne fonctionnaient que pour les cas les plus basiques. Si vous vouliez faire des choses plus grandes et meilleures, vous voudrez probablement travailler avec des fichiers depuis l'intérieur de C plutôt que via le shell.

Pour y parvenir, vous utiliserez une fonction appelée `fopen`. Cette fonction prend deux paramètres de chaîne, le premier étant le nom du fichier et le second étant le mode.

Les modes sont essentiellement des permissions, donc `r` pour la lecture, `w` pour l'écriture, `a` pour l'ajout. Vous pouvez également les combiner, donc `rw` signifierait que vous pourriez lire et écrire dans le fichier. Il existe d'autres modes, mais ceux-ci sont les plus couramment utilisés.

Une fois que vous avez un pointeur `FILE`, vous pouvez utiliser essentiellement les mêmes commandes d'I/O que vous auriez utilisées, sauf que vous devez les préfixer avec `f` et le premier argument sera le pointeur de fichier. Par exemple, la version fichier de `printf` est `fprintf`.

Voici un programme appelé `greetings` qui lit depuis un fichier contenant une liste de noms et écrit les salutations dans un autre fichier :

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Créer des pointeurs de fichier.
    FILE *names = fopen("names.txt", "r");
    FILE *greet = fopen("greet.txt", "w");

    // Vérifier que tout est OK.
    if (!names || !greet) {
        fprintf(stderr, "L'ouverture du fichier a échoué !\n");
        return EXIT_FAILURE;
    }

    // C'est l'heure des salutations !
    char name[20];
    // Basiquement, continuer à lire jusqu'à ce qu'il n'y ait plus rien.
    while (fscanf(names, "%s\n", name) > 0) {
        fprintf(greet, "Hello, %s!\n", name);
    }

    // Lorsque la fin est atteinte, imprimer un message dans le terminal pour informer l'utilisateur.
    if (feof(names)) {
        printf("Les salutations sont terminées !\n");
    }

    return EXIT_SUCCESS;
}
```

Supposons que `names.txt` contient ce qui suit :

```text
Kamala
Logan
Carol
```

Alors, après avoir exécuté `greetings`, le fichier `greet.txt` contiendra :

```text
Hello, Kamala!
Hello, Logan!
Hello, Carol!
```