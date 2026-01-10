---
title: Qu'est-ce qu'une attaque par débordement de tampon – et comment l'arrêter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-05T13:48:00.000Z'
originalURL: https://freecodecamp.org/news/buffer-overflow-attacks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fff3d7b98be260817e495c3.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Qu'est-ce qu'une attaque par débordement de tampon – et comment l'arrêter
seo_desc: 'By Megan Kaczanowski

  A buffer overflow occurs when the size of information written to a memory location
  exceeds what it was allocated. This can cause data corruption, program crashes,
  or even the execution of malicious code.

  While C, C++, and Objecti...'
---

Par Megan Kaczanowski

Un débordement de tampon se produit lorsque la taille des informations écrites dans un emplacement mémoire dépasse ce qui lui a été alloué. Cela peut provoquer une corruption des données, des plantages de programmes ou même l'exécution de code malveillant.

Bien que C, C++ et Objective-C soient les principaux langages présentant des vulnérabilités de débordement de tampon (car ils gèrent plus directement la mémoire que de nombreux langages interprétés), ils constituent la base d'une grande partie d'Internet. 

Même si le code est écrit dans un langage 'sûr' (comme Python), s'il appelle des bibliothèques écrites en C, C++ ou Objective-C, il pourrait toujours être vulnérable aux débordements de tampon.

## Allocation de mémoire

Pour comprendre les débordements de tampon, il est important de comprendre un peu comment les programmes allouent la mémoire. Dans un programme C, vous pouvez allouer de la mémoire sur la pile, au moment de la compilation, ou sur le tas, à l'exécution. 

Pour déclarer une variable sur la pile : `int numberPoints = 10;`

Ou, sur le tas : `int* ptr = malloc (10 * sizeof(int));`

Les débordements de tampon peuvent se produire sur la pile (débordement de pile) ou sur le tas (débordement de tas).

En général, les débordements de pile sont plus couramment exploités que les débordements de tas. Cela est dû au fait que les piles contiennent une séquence de fonctions imbriquées, chacune retournant l'adresse de la fonction appelante à laquelle la pile doit revenir après que la fonction a fini de s'exécuter. Cette adresse de retour peut être remplacée par l'instruction d'exécuter plutôt un morceau de code malveillant. 

Comme les tas stockent moins couramment ces adresses de retour, il est beaucoup plus difficile de lancer une exploitation (bien que ce ne soit pas impossible). La mémoire sur le tas contient généralement des données de programme et est allouée dynamiquement au fur et à mesure que le programme s'exécute. Cela signifie qu'un débordement de tas devrait probablement écraser un pointeur de fonction – plus difficile et moins efficace qu'un débordement de pile.

Comme les débordements de pile sont le type de débordement de tampon le plus couramment exploité, nous allons brièvement examiner exactement comment ils fonctionnent.

## Débordements de pile

Lorsqu'un exécutable est lancé, il s'exécute dans un processus, et chaque processus a sa propre pile. Au fur et à mesure que le processus exécute la fonction principale, il trouvera à la fois de nouvelles variables locales (qui seront poussées au sommet de la pile) et des appels à d'autres fonctions (qui créeront un nouveau cadre de pile).

Un diagramme de pile, pour plus de clarté :

![Image](https://megankaczanowski.com/content/images/2021/01/Screen-Shot-2021-01-05-at-12.31.23-PM.png)
_https://en.wikipedia.org/wiki/Stack_(abstract_data_type)_

### Alors, qu'est-ce qu'un cadre de pile ?

Tout d'abord, une pile d'appels est essentiellement le code assembleur pour un programme particulier. C'est une pile de variables et de cadres de pile qui indiquent à l'ordinateur dans quel ordre exécuter les instructions. Il y aura un cadre de pile pour chaque fonction qui n'a pas encore fini de s'exécuter, la fonction qui s'exécute actuellement étant au sommet de la pile.

Pour suivre cela, un ordinateur conserve plusieurs pointeurs en mémoire :

* **Pointeur de pile** : Pointe vers le sommet de la pile d'appels du processus (ou le dernier élément poussé sur la pile).
* **Pointeur d'instruction** : Pointe vers l'adresse de la prochaine instruction CPU à exécuter.
* **Pointeur de base (BP)** : (également connu sous le nom de pointeur de cadre) Pointe vers la base du cadre de pile actuel. Il reste constant tant que le programme exécute le cadre de pile actuel (bien que le pointeur de pile changera).

Par exemple, étant donné le programme suivant :

```c
int main() {
    int j = firstFunction(5);
    return 0;
}
    
int firstFunction(int z) {
    int x = 1 + z;
    return x;
}
```

La pile d'appels ressemblerait à ceci, juste après que firstFunction a été appelée et que l'instruction `int x = 1+z` a été exécutée :

![Image](https://megankaczanowski.com/content/images/2021/04/Screen-Shot-2021-04-03-at-12.04.52-PM.png)

Ici, `main` a appelé `firstFunction` (qui s'exécute actuellement), donc elle est au sommet de la pile d'appels. L'adresse de retour est l'adresse mémoire de la fonction qui l'a appelée (celle-ci est détenue par le pointeur d'instruction lorsque le cadre de pile est créé). Les variables locales qui sont encore dans la portée sont également sur la pile d'appels. Au fur et à mesure qu'elles sont exécutées et sortent de la portée, elles sont 'retirées' du sommet de la pile.

Ainsi, l'ordinateur est capable de suivre quelle instruction doit être exécutée, et dans quel ordre. Un débordement de pile est conçu pour écraser l'une de ces adresses de retour enregistrées avec sa propre adresse malveillante.

**Exemple de vulnérabilité de débordement de tampon (C) :** 

```c
int main() {
    bufferOverflow();
 }
 
 bufferOverflow() {
    char textLine[10];
    printf("Enter your line of text: ");
    gets(textLine);
    printf("You entered: ", textLine);
    return 0;
 }
```

Cet exemple simple lit une quantité arbitraire de données (gets lira jusqu'à la fin du fichier ou le caractère de nouvelle ligne). En pensant à la pile d'appels que nous avons parcourue ci-dessus, vous pouvez voir pourquoi cela est dangereux. Si l'utilisateur entre plus de données que la quantité assignée à la variable, la chaîne entrée par l'utilisateur écrasera les emplacements mémoire suivants sur la pile d'appels. Si elle est suffisamment longue, elle pourrait même écraser l'adresse de retour de la fonction appelante.

La manière dont l'ordinateur réagira à cela dépend de la façon dont les piles sont implémentées et de la manière dont la mémoire est allouée dans un système particulier. La réponse à un débordement de tampon peut être assez imprévisible, allant des défauts de programme, aux plantages, à l'exécution de code malveillant.

## Pourquoi les débordements de tampon se produisent-ils ?

La raison pour laquelle les débordements de tampon sont devenus un problème si important est que de nombreuses fonctions de manipulation de mémoire en C et C++ n'effectuent aucune vérification des limites. Bien que les débordements de tampon soient assez bien connus maintenant, ils sont également très couramment exploités (par exemple, [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) a exploité un débordement de tampon). 

Les débordements de tampon sont plus courants lorsque le code dépend de données d'entrée externes, est trop complexe pour qu'un programmeur comprenne facilement son comportement, ou lorsqu'il a des dépendances en dehors du champ d'application direct du code. 

Les serveurs web, les serveurs d'applications et les environnements d'applications web sont tous sensibles aux débordements de tampon. 

L'exception concerne les environnements écrits dans des langages interprétés, bien que les interpréteurs eux-mêmes puissent être sensibles aux débordements.

## Comment atténuer les débordements de tampon

* **Utilisez un langage interprété** qui n'est pas sensible à ces problèmes.
* **Évitez d'utiliser des fonctions qui n'effectuent pas de vérifications de tampon** (par exemple, en C, au lieu de gets(), utilisez fgets()).
* **Utilisez des compilateurs qui peuvent aider à identifier les fonctions non sûres ou les erreurs.**
* **[Utilisez](https://ritcsec.wordpress.com/2017/05/18/buffer-overflows-aslr-and-stack-canaries/) [des Canaries](http://www.cbi.umn.edu/securitywiki/CBI_ComputerSecurity/MechanismCanary.html),** une 'valeur de garde' qui peut aider à prévenir les débordements de tampon. Elles sont insérées avant une adresse de retour dans la pile et sont vérifiées avant que l'adresse de retour ne soit accédée. Si le programme détecte un changement dans la valeur du canari, il interrompra le processus, empêchant l'attaquant de réussir. La valeur du canari est soit aléatoire (donc, très difficile à deviner pour un attaquant) soit une chaîne de caractères qui, pour des raisons techniques, est impossible à écraser. 
* **Réorganisation des variables locales** de sorte que les variables scalaires (objets de données de taille fixe individuels) soient au-dessus des variables de tableau (contenant plusieurs valeurs). Cela signifie que si les variables de tableau débordent, elles n'affecteront pas les variables scalaires. Cette technique, combinée avec des valeurs de canari, peut aider à empêcher les attaques par débordement de tampon de réussir.
* **Rendre une pile non exécutable** en définissant le bit NX (No-eXecute), empêchant l'attaquant d'insérer du shellcode directement dans la pile et de l'exécuter là. Ce n'est pas une solution parfaite, car même les piles non exécutables peuvent être victimes d'attaques par débordement de tampon telles que l'attaque return-to-libc. Cette attaque se produit lorsque l'adresse de retour d'un cadre de pile est remplacée par l'adresse d'une bibliothèque déjà dans l'espace d'adressage du processus. De plus, tous les CPU ne permettent pas de définir le bit NX.
* **[ASLR (randomisation de la disposition de l'espace d'adressage)](https://en.wikipedia.org/wiki/Address_space_layout_randomization)**, peut servir de défense générale (ainsi que de défense spécifique contre les attaques return-to-libc). Cela signifie que chaque fois qu'un fichier de bibliothèque ou une autre fonction est appelé par un processus en cours d'exécution, son adresse est décalée d'un nombre aléatoire. Cela rend presque impossible l'association d'une adresse mémoire de processus fixe avec des fonctions, ce qui signifie qu'il peut être difficile, voire impossible, pour un attaquant de savoir d'où appeler des fonctions spécifiques. ASLR est activé par défaut dans de nombreuses versions de Linux, OS X et Android (ce qui peut être désactivé dans la ligne de commande).

### Note sur le débordement de pile par le bas :

Il est également possible d'avoir une vulnérabilité de débordement de tampon par le bas, lorsque deux parties du même programme traitent le même bloc de mémoire différemment. Par exemple, si vous allouez un tableau de taille X, mais que vous le remplissez avec un tableau de taille x < X, et que vous tentez ensuite de récupérer tous les octets X, vous risquez d'obtenir des données inutiles pour X - x octets. 

Essentiellement, vous avez peut-être récupéré des données qui restent de l'utilisation précédente de cette mémoire. Le meilleur des cas est que ce soit des données inutiles qui ne signifient rien, tandis que le pire des cas est que ce soit des données sensibles qu'un attaquant pourrait être en mesure de détourner.

### Sources/Lectures complémentaires :

* [Cours sur la sécurité des ordinateurs et des réseaux, Avinash Kak](https://engineering.purdue.edu/kak/compsec/)
* [Débordements de tampon OWASP](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)
* [Pile vs Tas](https://gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html)