---
title: Comment j'ai résolu un défi CrackMe simple avec Ghidra de la NSA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T15:30:50.000Z'
originalURL: https://freecodecamp.org/news/how-i-solved-a-simple-crackme-challenge-with-the-nsas-ghidra-d7e793c5acd2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9N3SURf2cF4fISICAH7tGA.png
tags:
- name: hacking
  slug: hacking
- name: General Programming
  slug: programming
- name: reverse engineering
  slug: reverse-engineering
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: Comment j'ai résolu un défi CrackMe simple avec Ghidra de la NSA
seo_desc: 'By Denis Nuțiu

  Hello!

  I’ve been playing recently a bit with Ghidra, which is a reverse engineering tool
  that was recently open sourced by the NSA. The official website describes the tool
  as:


  A software reverse engineering (SRE) suite of tools develo...'
---

Par Denis Nuțiu

Bonjour !

J'ai récemment joué un peu avec [Ghidra](https://ghidra-sre.org/), qui est un outil d'ingénierie inverse récemment open source par la NSA. Le site officiel décrit l'outil comme :

> _Une suite d'outils d'ingénierie inverse de logiciels (SRE) développée par la Direction de la Recherche de la NSA pour soutenir la mission de cybersécurité._

Je suis au début de ma carrière en ingénierie inverse, donc je n'ai rien fait d'avancé. Je ne sais pas quelles fonctionnalités attendre d'un outil professionnel comme celui-ci, si vous cherchez à lire sur les fonctionnalités avancées de Ghidra, cet article n'est probablement pas pour vous.

Dans cet article, je vais essayer de résoudre un défi CrackMe simple que j'ai trouvé sur le site [root-me](https://www.root-me.org/). Le défi que je résous s'appelle [ELF - CrackPass](https://www.root-me.org/en/Challenges/Cracking/ELF-CrackPass). Si vous voulez essayer par vous-même, alors vous devriez éviter de lire cet article car il va gâcher le défi pour vous.

Commençons ! J'ouvre Ghidra et crée un nouveau projet que j'appelle RootMe.

![Image](https://cdn-media-1.freecodecamp.org/images/t6VRANxq75gcBUE7GDwEho2IqpOJ6DC4NGt0)

Ensuite, j'importe le fichier du défi en le glissant dans le dossier du projet. Je vais avec les paramètres par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/y2KMPmw-nfQlH9gn9ZJxP2Zqk5XZgrTD1lGF)

Après avoir été présenté avec quelques informations sur le fichier binaire, j'appuie sur OK, je sélectionne le fichier et je double-clique dessus. Cela ouvre l'utilitaire de navigation de code de Ghidra et demande si je veux analyser le fichier, puis j'appuie sur Oui et je continue avec les paramètres par défaut.

Après avoir importé le fichier, nous obtenons quelques informations sur le fichier binaire. Si nous appuyons sur OK et fermons cette fenêtre, puis double-cliquons sur le fichier que nous avons importé, cela ouvre l'utilitaire de navigation de code de Ghidra. Je sélectionne Oui lorsque je suis invité à analyser le binaire et je continue avec les paramètres par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/zBOQtrTVrg3SebAl14mSBlRknf4qJrM2VBKY)

Le navigateur de code est assez pratique. Dans le panneau de gauche, nous voyons la vue de désassemblage et dans le panneau de droite, la vue de décompilation.

Ghidra nous montre directement les informations d'en-tête ELF et le point d'entrée du binaire. Après avoir double-cliqué sur le point d'entrée, la vue de désassemblage saute à la fonction d'entrée.

Maintenant, nous pouvons identifier avec succès la fonction principale, que je renomme en main. Il serait bien que l'outil tente de détecter automatiquement la fonction principale et de la renommer en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/7Ng0waaxWM2LhOlomKpuNfPmJudV8uido7WJ)

Avant d'analyser la fonction principale, je voulais changer sa signature. J'ai changé le type de retour en int et corrigé le type et le nom des paramètres. Ce changement a pris effet dans la vue de décompilation, ce qui est cool ! 💡

Mettre en surbrillance une ligne dans la vue de décompilation la met également en surbrillance dans la vue d'assemblage.

![Image](https://cdn-media-1.freecodecamp.org/images/2HOWsHwRO1EjjGH7Kwv4Dmvu-KVrMSkNL0yj)

Explorons la fonction FUN_080485a5, que je renommerai en CheckPassword.

Le contenu de la fonction CheckPassword peut être trouvé ci-dessous. J'ai copié le code directement depuis la vue de décompilation de Ghidra, ce qui est une fonctionnalité pratique que de nombreux outils de ce type n'ont pas ! Pouvoir copier l'assemblage et le code est une fonctionnalité agréable à avoir.

```
void CheckPassword(char *param_1) {   ushort **ppuVar1;   int iVar2;   char *pcVar3;   char cVar4;   char local_108c [128];   char local_100c [4096];   cVar4 = param_1;       if (cVar4 != 0) {          ppuVar1 = __ctype_b_loc();           pcVar3 = param_1;           do {               if (((byte )(ppuVar1 + (int)cVar4) & 8) == 0) {         puts("Bad password !");                     /* WARNING: Subroutine does not return */         abort();       }       cVar4 = pcVar3[1];       pcVar3 = pcVar3 + 1;     } while (cVar4 != 0);   }   FUN_080484f4(local_100c,param_1);   FUN_0804851c(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar2 = strcmp(local_108c,local_100c);   if (iVar2 == 0) {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   else {     puts("Is not the good password !");   }   return; }
```

Après avoir jeté un coup d'œil au code, je suis arrivé aux conclusions suivantes. Le bloc avec le `if` vérifie si l'utilisateur a fourni un mot de passe et inspecte le mot de passe fourni pour vérifier s'il s'agit d'un caractère valide ou autre chose. Je ne suis pas exactement sûr de ce qu'il vérifie, mais voici ce que dit la documentation de __ctype_b_loc() :

> _La fonction __ctype_b_loc() doit retourner un pointeur vers un tableau de caractères dans la locale actuelle qui contient des caractéristiques pour chaque caractère dans le jeu de caractères actuel. Le tableau doit contenir un total de 384 caractères, et peut être indexé avec n'importe quel char signé ou non signé (c'est-à-dire avec une valeur d'index comprise entre 128 et 255). Si l'application est multithread, le tableau doit être local au thread actuel._

Quoi qu'il en soit, ce bloc de code ne vaut pas vraiment la peine, car il ne modifie pas notre mot de passe de quelque manière que ce soit, il le vérifie simplement. Nous pouvons donc sauter ce type de vérification.

La fonction suivante appelée est FUN_080484f4. En regardant son code, nous pouvons dire qu'il s'agit simplement d'une implémentation personnalisée de memcopy. Au lieu de copier le code C depuis la vue de décompilation, j'ai copié le code assembleur — oui, c'est amusant.

```
*************************************************************                     *                           FUNCTION                                               *************************************************************                     undefined  FUN_080484f4 (undefined4  param_1 , undefined4  p     undefined         AL:1           <RETURN>     undefined4        Stack[0x4]:4   param_1                                 XREF[1]:     080484f8 (R)        undefined4        Stack[0x8]:4   param_2                                 XREF[1]:     080484fb (R)                        FUN_080484f4                                    XREF[1]:     CheckPassword:080485f5 (c)    080484f4 55              PUSH       EBP 080484f5 89  e5           MOV        EBP ,ESP 080484f7 53              PUSH       EBX 080484f8 8b  5d  08       MOV        EBX ,dword ptr [EBP  + param_1 ] 080484fb 8b  4d  0c       MOV        ECX ,dword ptr [EBP  + param_2 ] 080484fe 0f  b6  11       MOVZX      EDX ,byte ptr [ECX ] 08048501 84  d2           TEST       DL,DL 08048503 74  14           JZ         LAB_08048519 08048505 b8  00  00       MOV        EAX ,0x0             00  00                         LAB_0804850a                                    XREF[1]:     08048517 (j)    0804850a 88  14  03       MOV        byte ptr [EBX  + EAX *0x1 ],DL 0804850d 0f  b6  54       MOVZX      EDX ,byte ptr [ECX  + EAX *0x1  + 0x1 ]             01  01 08048512 83  c0  01       ADD        EAX ,0x1 08048515 84  d2           TEST       DL,DL 08048517 75  f1           JNZ        LAB_0804850a                         LAB_08048519                                    XREF[1]:     08048503 (j)    08048519 5b              POP        EBX 0804851a 5d              POP        EBP 0804851b c3              RETComment: param_1 est dest, param_2 est src. 08048501 vérifie si src est null et si c'est le cas, il retourne, sinon il initialise EAX (index, current_character) avec 0. Les instructions suivantes déplacent les octets dans EBX (dest) depuis EDX (src). La boucle s'arrête lorsque EDX est null.
```

Et l'autre fonction FUN_0804851c génère le mot de passe à partir de la chaîne "THEPASSWORDISEASYTOCRACK". En regardant la vue décompilée, nous pouvons voir grossièrement comment cette fonction fonctionne. Si nous n'avions pas cela, nous devrions analyser manuellement chaque instruction d'assemblage de la fonction pour comprendre ce qu'elle fait.

Ensuite, nous comparons le mot de passe généré précédemment avec le mot de passe que nous avons obtenu de l'utilisateur (le premier argument, argv[1]). Si cela correspond, le programme dit bon travail et l'imprime, sinon il imprime un message d'erreur.

À partir de cette analyse de base, nous pouvons conclure que si nous patchons le programme à divers endroits, nous pouvons le faire cracher le mot de passe sans avoir besoin de reverse aucune fonction C et d'écrire du code. Patcher le programme signifie changer certaines de ses instructions.

Voyons ce que nous devons patcher :

À l'adresse 0x0804868c, nous patchons l'instruction JNS en JMP. Et voilà, le changement est reflété dans la vue de décompilation. La vérification du résultat de ptrace est contournée.

```
{   ptrace(PTRACE_TRACEME,0,1,0);   if (argc != 2) {     puts("You must give a password for use this program !");                     /* WARNING: Subroutine does not return */     abort();   }   CheckPassword(argv[1]);   return 0;}
```

À l'adresse 0x080485b8, nous patchons l'instruction JZ en JMP. Nous contournons ce bloc de vérification de mot de passe que nous avons vu plus tôt.

```
void CheckPassword(undefined4 param_1) {   int iVar1;   char local_108c [128];   char local_100c [4096];   CustomCopy(local_100c,param_1);      GeneratePassword(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar1 = strcmp(local_108c,local_100c);   if (iVar1 == 0) {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   else {     puts("Is not the good password !");   }   return; }
```

À l'adresse 0x0804861e, nous patchons JNZ en JZ. Cela inverse la condition if/else. Puisque nous ne connaissons pas le mot de passe, nous allons soumettre un mot de passe aléatoire qui n'est pas égal à celui généré, exécutant ainsi le printf dans le bloc else.

```
void CheckPassword(undefined4 param_1) {   int iVar1;   char local_108c [128];   char local_100c [4096];   CustomCopy(local_100c,param_1);   // construit le mot de passe à partir des chaînes et le stocke dans   // local_108c    GeneratePassword(s_THEPASSWORDISEASYTOCRACK_08049960,local_108c);   iVar1 = strcmp(local_108c,local_100c);   if (iVar1 == 0) { // les mots de passe sont égaux     puts("Is not the good password !");   }   else {     printf("Good work, the password is : \n\n%s\n",local_108c);   }   return; }
```

C'est tout !

Maintenant, nous exécutons le programme. Dans d'autres outils, nous sauvegardons simplement le fichier et cela fonctionne, mais dans Ghidra, il semble que nous devons l'exporter.

Pour exporter le programme, nous allons dans Fichier -> Exporter le programme (O). Nous changeons le format en binaire et cliquons sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/nQiTkhZ4S8BIG22V66wHKDDcovdTOugk1E3J)

J'obtiens le programme exporté sur mon bureau mais il ne fonctionne pas — je n'ai pas réussi à exécuter le programme exporté. Après avoir essayé de lire son en-tête avec le programme readelf -h, j'obtiens la sortie suivante :

```
root@DESKTOP:/mnt/c/users/denis/Desktop# readelf -h Crack.bin ELF Header:   Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00   Class:                             ELF32   Data:                              2's complement, little endian   Version:                           1 (current)   OS/ABI:                            UNIX - System V   ABI Version:                       0   Type:                              EXEC (Executable file)   Machine:                           Intel 80386   Version:                           0x1   Entry point address:               0x8048440   Start of program headers:          52 (bytes into file)   Start of section headers:          2848 (bytes into file)   Flags:                             0x0   Size of this header:               52 (bytes)   Size of program headers:           32 (bytes)   Number of program headers:         7   Size of section headers:           40 (bytes)   Number of section headers:         27   Section header string table index: 26 readelf: Error: Reading 1080 bytes extends past end of file for section headers
```

Dommage. Il semble que Ghidra ait corrompu l'[en-tête de fichier](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#File_header)... et, pour l'instant, je n'ai pas envie de corriger manuellement les en-têtes. J'ai donc lancé un autre outil et appliqué les mêmes patchs au fichier, je l'ai sauvegardé, je l'ai exécuté avec un argument aléatoire et j'ai validé le flag.

#### Conclusions

Ghidra est un bel outil avec beaucoup de potentiel. Dans son état actuel, ce n'est pas génial mais cela fonctionne. J'ai également rencontré un bug de défilement étrange en l'exécutant sur mon ordinateur portable.

Les alternatives seraient de payer $$ pour d'autres outils de ce type, de créer vos propres outils ou de travailler avec des outils gratuits mais moins conviviaux.

Espérons qu'une fois le code publié, la communauté commencera à faire des corrections et à améliorer Ghidra.

Merci d'avoir lu !