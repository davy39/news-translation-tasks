---
title: Comment récupérer les informations système en utilisant l'instruction CPUID
subtitle: ''
author: Nikolaos Panagopoulos
co_authors: []
series: null
date: '2024-10-03T10:13:02.208Z'
originalURL: https://freecodecamp.org/news/retrieve-system-information-using-cpuid
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/JMwCe3w7qKk/upload/bb94515f8210b64d35039199912a3b6c.jpeg
tags:
- name: Kernel
  slug: kernel
- name: operating system
  slug: operating-system
- name: cpu
  slug: cpu
seo_title: Comment récupérer les informations système en utilisant l'instruction CPUID
seo_desc: 'When developing a bootloader/kernel, understanding the underlying architecture
  is crucial for optimizing performance and compatibility between software and hardware.

  One important yet sometimes overlooked tool available to engineers for querying
  and ...'
---

Lorsque vous développez un chargeur de démarrage/noyau, comprendre l'architecture sous-jacente est crucial pour optimiser les performances et la compatibilité entre le logiciel et le matériel.

Un outil important mais parfois négligé disponible pour les ingénieurs afin d'interroger et de récupérer des informations système est l'instruction CPUID.

### Qu'est-ce que l'instruction CPUID ?

L'instruction CPUID est une instruction de bas niveau, au cœur de chaque processeur x86 et x86-64 moderne, qui permet au logiciel d'interroger le CPU pour obtenir des informations sur le processeur et ses fonctionnalités prises en charge.

En invoquant cette instruction, vous pouvez recueillir des informations telles que le modèle du processeur, sa famille, les tailles de cache interne et les fonctionnalités prises en charge comme le [SIMD](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) ou la virtualisation matérielle. Cela peut vous aider à optimiser les performances et à activer ou désactiver dynamiquement les fonctionnalités prises en charge.

Pour les développeurs de chargeurs de démarrage ou de noyaux, comprendre les fonctionnalités prises en charge par un processeur—telles que la virtualisation matérielle, les tailles de cache ou les instructions SIMD—peut garantir que le système fonctionne efficacement et que le code que vous écrivez est compatible avec différents CPU. En utilisant l'instruction CPUID, vous pouvez ajuster dynamiquement le comportement de votre noyau en fonction du processeur spécifique sur lequel il s'exécute.

Dans cet article, vous apprendrez comment vérifier si l'instruction CPUID est disponible pour votre système, comment elle fonctionne et quelles informations vous pouvez obtenir en l'utilisant.

### Prérequis

* Certaines connaissances en langage d'assemblage (pour cet exemple, j'utilise FASM)

* Certaines connaissances des systèmes d'exploitation/noyaux

* Accès à des outils de débogage de bas niveau (par exemple, GDB) ou à des émulateurs matériels comme QEMU pour tester votre chargeur de démarrage/noyau sur diverses plateformes.

## Étape 1 : Vérifier la disponibilité de CPUID

Avant d'exécuter l'instruction CPUID, il est important de déterminer si le processeur la prend en charge, car tous les CPU ne sont pas garantis d'avoir cette fonctionnalité. Le code suivant vérifie la disponibilité de l'instruction CPUID en modifiant et en testant le bit ID (bit 21) dans le registre EFLAGS.

Voici une image de [wiki.osdev.org](https://wiki.osdev.org/Expanded_Main_Page) qui montre chaque bit du registre EFLAGS :

[![](https://cdn.hashnode.com/res/hashnode/image/upload/v1727637307676/82ad4bf5-3906-49a3-a12a-6cb83cc852db.png align="center")](https://wiki.osdev.org/CPU_Registers_x86)

Si le processeur permet de basculer ce bit, CPUID est pris en charge ; sinon, ce n'est pas le cas. Voici comment fonctionne le processus de détection :

(la plupart des gens pensent qu'en mode réel, les registres 32 bits ne sont pas accessibles. Ce n'est pas vrai. Tous les registres 32 bits sont utilisables)

```plaintext
cpuid_check:
    pusha                                ; sauvegarder l'état
    pushfd                               ; Sauvegarder EFLAGS
    pushfd                               ; Stocker EFLAGS
    xor dword [esp],0x00200000           ; Inverser le bit ID dans EFLAGS stocké
    popfd                                ; Charger EFLAGS stocké (avec le bit ID inversé)
    pushfd                               ; Stocker EFLAGS à nouveau (le bit ID peut être inversé ou non)
    pop eax                              ; eax = EFLAGS modifié (le bit ID peut être inversé ou non)
    xor eax,[esp]                        ; eax = quels bits ont été changés
    popfd                                ; Restaurer EFLAGS original
    and eax,0x00200000                   ; eax = zéro si le bit ID ne peut pas être changé, sinon non-zéro
    cmp eax,0x00
    je .cpuid_instruction_not_is_available
.cpuid_instruction_is_available:
    ; gérer l'existence de CPUID
.cpuid_instruction_not_is_available:
    ; gérer le fait que CPUID n'est pas pris en charge
.cpuid_check_end:
    popa                                  ; restaurer l'état
    ret
```

`pusha` : Sauvegarde tous les registres à usage général pour s'assurer que l'état original peut être restauré à la fin.

`pushfd` : Sauvegarde le registre EFLAGS actuel.

`pushfd` : Stocke une copie des EFLAGS.

`xor dword [esp], 0x00200000` : Le code inverse le bit ID (21) des EFLAGS en utilisant l'opérateur XOR.

`popfd` : Restaure les EFLAGS modifiés avec le bit ID inversé.

`pushfd` : Pousse les EFLAGS modifiés vers la pile.

`pop eax` : Place les EFLAGS modifiés (le bit ID peut être inversé ou non) dans le registre EAX.

`xor eax, [esp]` : Après l'opération XOR, EAX contiendra les bits qui ont été changés.

`popfd` : Restaure les EFLAGS originaux.

`and eax, 0x00200000` : L'opération `and` isole le 21ème bit (bit ID) en masquant tous les autres bits. Après cette opération, le registre EAX contiendra soit 0x00200000 (si le bit 21 a été changé, ce qui signifie que CPUID est pris en charge) soit 0×00 (le bit 21 n'a pas changé, CPUID non pris en charge).

`cmp eax, 0x00` : L'instruction CMP vérifie le résultat de l'opération précédente. Si EAX est égal à 0×00, cela signifie que le bit ID ne peut pas être modifié et que le processeur ne prend pas en charge l'instruction CPUID. Si ce n'est pas zéro, cela signifie que le bit ID a été inversé et que votre processeur prend en charge l'instruction CPUID.

## Étape 2 : Comment utiliser l'instruction CPUID

### Obtenir les fonctionnalités du CPU

L'instruction CPUID retournera différentes informations avec différentes valeurs dans le registre EAX.

```plaintext
mov eax, 0x1
cpuid
```

Avec EAX défini sur 1, CPUID retournera un champ de bits dans EDX, qui contiendra les valeurs suivantes. Différentes marques peuvent donner des significations différentes à celles-ci (source [https://wiki.osdev.org/CPUID](https://wiki.osdev.org/CPUID))

```c
enum {
    CPUID_FEAT_ECX_SSE3         = 1 << 0,
    CPUID_FEAT_ECX_PCLMUL       = 1 << 1,
    CPUID_FEAT_ECX_DTES64       = 1 << 2,
    CPUID_FEAT_ECX_MONITOR      = 1 << 3,
    CPUID_FEAT_ECX_DS_CPL       = 1 << 4,
    CPUID_FEAT_ECX_VMX          = 1 << 5,
    CPUID_FEAT_ECX_SMX          = 1 << 6,
    CPUID_FEAT_ECX_EST          = 1 << 7,
    CPUID_FEAT_ECX_TM2          = 1 << 8,
    CPUID_FEAT_ECX_SSSE3        = 1 << 9,
    CPUID_FEAT_ECX_CID          = 1 << 10,
    CPUID_FEAT_ECX_SDBG         = 1 << 11,
    CPUID_FEAT_ECX_FMA          = 1 << 12,
    CPUID_FEAT_ECX_CX16         = 1 << 13,
    CPUID_FEAT_ECX_XTPR         = 1 << 14,
    CPUID_FEAT_ECX_PDCM         = 1 << 15,
    CPUID_FEAT_ECX_PCID         = 1 << 17,
    CPUID_FEAT_ECX_DCA          = 1 << 18,
    CPUID_FEAT_ECX_SSE4_1       = 1 << 19,
    CPUID_FEAT_ECX_SSE4_2       = 1 << 20,
    CPUID_FEAT_ECX_X2APIC       = 1 << 21,
    CPUID_FEAT_ECX_MOVBE        = 1 << 22,
    CPUID_FEAT_ECX_POPCNT       = 1 << 23,
    CPUID_FEAT_ECX_TSC          = 1 << 24,
    CPUID_FEAT_ECX_AES          = 1 << 25,
    CPUID_FEAT_ECX_XSAVE        = 1 << 26,
    CPUID_FEAT_ECX_OSXSAVE      = 1 << 27,
    CPUID_FEAT_ECX_AVX          = 1 << 28,
    CPUID_FEAT_ECX_F16C         = 1 << 29,
    CPUID_FEAT_ECX_RDRAND       = 1 << 30,
    CPUID_FEAT_ECX_HYPERVISOR   = 1 << 31,

    CPUID_FEAT_EDX_FPU          = 1 << 0,
    CPUID_FEAT_EDX_VME          = 1 << 1,
    CPUID_FEAT_EDX_DE           = 1 << 2,
    CPUID_FEAT_EDX_PSE          = 1 << 3,
    CPUID_FEAT_EDX_TSC          = 1 << 4,
    CPUID_FEAT_EDX_MSR          = 1 << 5,
    CPUID_FEAT_EDX_PAE          = 1 << 6,
    CPUID_FEAT_EDX_MCE          = 1 << 7,
    CPUID_FEAT_EDX_CX8          = 1 << 8,
    CPUID_FEAT_EDX_APIC         = 1 << 9,
    CPUID_FEAT_EDX_SEP          = 1 << 11,
    CPUID_FEAT_EDX_MTRR         = 1 << 12,
    CPUID_FEAT_EDX_PGE          = 1 << 13,
    CPUID_FEAT_EDX_MCA          = 1 << 14,
    CPUID_FEAT_EDX_CMOV         = 1 << 15,
    CPUID_FEAT_EDX_PAT          = 1 << 16,
    CPUID_FEAT_EDX_PSE36        = 1 << 17,
    CPUID_FEAT_EDX_PSN          = 1 << 18,
    CPUID_FEAT_EDX_CLFLUSH      = 1 << 19,
    CPUID_FEAT_EDX_DS           = 1 << 21,
    CPUID_FEAT_EDX_ACPI         = 1 << 22,
    CPUID_FEAT_EDX_MMX          = 1 << 23,
    CPUID_FEAT_EDX_FXSR         = 1 << 24,
    CPUID_FEAT_EDX_SSE          = 1 << 25,
    CPUID_FEAT_EDX_SSE2         = 1 << 26,
    CPUID_FEAT_EDX_SS           = 1 << 27,
    CPUID_FEAT_EDX_HTT          = 1 << 28,
    CPUID_FEAT_EDX_TM           = 1 << 29,
    CPUID_FEAT_EDX_IA64         = 1 << 30,
    CPUID_FEAT_EDX_PBE          = 1 << 31
};
```

Une brève explication des fonctionnalités du CPU ci-dessus :

* `PCLMUL, AES` : Jeux d'instructions cryptographiques pour un chiffrement et un déchiffrement rapides.

* `VMX, SMX` : Prise en charge de la virtualisation pour l'exécution de machines virtuelles.

* `SSE3, SSSE3, SSE4.1, SSE4.2, AVX` : Jeux d'instructions SIMD pour un traitement multimédia, mathématique et vectoriel plus rapide.

* `FMA` : Fused Multiply-Add, améliore les performances dans les calculs en virgule flottante.

* `RDRAND` : Générateur de nombres aléatoires.

* `X2APIC` : Gestion avancée des interruptions dans les systèmes multiprocesseurs.

* `PCID` : Optimise la gestion de la mémoire lors des changements de contexte.

* `FPU` : Unité matérielle de calcul en virgule flottante pour des opérations mathématiques plus rapides.

* `PAE` : Extension d'adresse physique, permet d'adresser plus de 4 Go de mémoire.

* `HTT` : Permet à un seul cœur de CPU de gérer plusieurs threads.

* `PAT, PGE` : Fonctionnalités de gestion de la mémoire pour contrôler la mise en cache et le mappage des pages.

* `MMX, SSE, SSE2` : Anciens jeux d'instructions SIMD pour le traitement multimédia.

### Obtenir la chaîne du fournisseur du CPU

Si vous souhaitez obtenir la chaîne du fournisseur du CPU, EAX doit être défini sur 0×0 avant d'invoquer l'instruction CPUID.

```plaintext
mov eax, 0x0
cpuid
```

La chaîne du fournisseur est un identifiant unique utilisé par les fournisseurs de CPU comme AMD et Intel. Des exemples sont : GenuineIntel (pour les processeurs Intel) ou AuthenticAMD (pour les processeurs AMD). Elle spécifie essentiellement le fabricant du CPU.

La chaîne du fournisseur permet au noyau d'identifier le fabricant du CPU, ce qui est très utile car différents fabricants implémentent certaines fonctionnalités différemment. De plus, les logiciels ou les pilotes peuvent interagir différemment en fonction du fabricant du CPU pour garantir la compatibilité.

Lorsque vous l'utilisez de cette manière, la chaîne d'identification du fournisseur sera retournée dans les registres EBX, EDX, ECX. Vous pouvez les écrire dans un tampon et obtenir la chaîne complète de 12 caractères.

Exemple de code :

### Étape 1 : Le tampon

Créez un tampon qui peut contenir 12 octets :

```plaintext
buffer: db 12 dup(0), 0xA, 0xD, 0
```

### Étape 2 : Imprimer le tampon

Nous commençons par créer une fonction d'impression de chaîne.

Ce code d'assemblage lit une chaîne caractère par caractère et l'imprime à l'écran en utilisant l'interruption BIOS 0x10. La fonction `print` parcourt la chaîne et utilise l'instruction `lodsb` pour charger chaque caractère dans le registre `al`.

Ensuite, la fonction `print_char` utilise l'interruption 0×10 pour l'imprimer à l'écran. Lorsque le code atteint la fin de la chaîne (terminateur nul), la boucle se termine.

```plaintext
print_string:
	call print
	ret
print:
.loop:  
	lodsb   ; lire le caractère dans al puis incrémenter
	cmp al ,0 ; vérifier si nous avons atteint la fin
	je .done  ; nous avons atteint le terminateur nul, terminer
	call print_char ; imprimer le caractère
	jmp .loop   ; sauter en arrière dans la boucle
.done:
	ret
print_char:
	mov ah, 0eh
	int 0x10
	ret
```

### Étape 3 : Remplir le tampon et l'imprimer

Ici, après avoir sauvegardé l'état actuel en utilisant l'instruction `pusha` et appelé `cpuid` avec 0×0 passé dans le registre EAX, nous pouvons stocker le contenu de `ebx`, `edx`, `ecx` dans le tampon. Ensuite, nous appelons `print_string` pour l'imprimer.

```plaintext
get_cpu_vendor:
    pusha
    mov eax, 0x0
    cpuid
    mov [buffer], ebx
    mov [buffer + 4], edx
    mov [buffer + 8], ecx
    mov si, buffer 
    call print_string
    popa
    ret
```

Une vidéo de ma chaîne YouTube où j'implémente et explique le code ci-dessus en détail

%[https://www.youtube.com/watch?v=K0Rxq2AIMmo]

Plus d'informations sur les informations que l'instruction CPUID peut vous donner selon la valeur passée dans le registre EAX peuvent être trouvées ici : [https://gitlab.com/x86-cpuid.org/x86-cpuid-db](https://gitlab.com/x86-cpuid.org/x86-cpuid-db)

### Épilogue

En comprenant et en utilisant l'instruction CPUID, vous pouvez rendre votre chargeur de démarrage/noyau plus adaptable à une large gamme de processeurs. Savoir comment détecter la disponibilité de l'instruction et récupérer des informations système cruciales—telles que les fonctionnalités du CPU, les tailles de cache et les technologies prises en charge—peut considérablement améliorer les performances et la compatibilité.

Après avoir lu cet article, vous devriez avoir les outils et les connaissances pour commencer à explorer l'instruction CPUID et comment vous pouvez l'utiliser dans votre propre projet !

Bon codage !