---
title: Comment obtenir une carte de la mémoire de votre système à l'aide des interruptions
  du BIOS
subtitle: ''
author: Nikolaos Panagopoulos
co_authors: []
series: null
date: '2024-09-23T14:14:25.667Z'
originalURL: https://freecodecamp.org/news/how-to-get-a-memory-map-of-your-system-using-bios-interrupts
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/iar-afB0QQw/upload/7b7f724f7260216b7427408112d5f8c4.jpeg
tags:
- name: Kernel
  slug: kernel
- name: memory-management
  slug: memory-management
- name: Linux
  slug: linux
seo_title: Comment obtenir une carte de la mémoire de votre système à l'aide des interruptions
  du BIOS
seo_desc: 'When you are developing a kernel, one of the most important things is memory.
  The kernel must know how much memory is available and where it''s located to avoid
  overwriting crucial system resources.

  But not all memory is freely available for use. Some...'
---

Lorsque vous développez un noyau (kernel), l'un des aspects les plus importants est la mémoire. Le noyau doit savoir quelle quantité de mémoire est disponible et où elle se situe pour éviter d'écraser des ressources système cruciales.

Cependant, toute la mémoire n'est pas librement utilisable. Certaines sections de mémoire sont réservées aux fonctions système et d'autres peuvent être occupées par des périphériques matériels. C’est pourquoi il est très important d'obtenir la carte de la mémoire (memory map) du système.

### Qu'est-ce qu'une carte de la mémoire ?

Mais qu'est-ce qu'une carte de la mémoire ? Une carte de la mémoire est une représentation (pensez-y comme à un tableau) qui montre comment la mémoire physique est organisée dans votre système. Elle indique l'adresse de chaque région mémoire, sa longueur et son type.

Le type 1 signifie que la région est disponible pour une utilisation libre et le type 2 signifie qu'elle est réservée par votre système. Le type 3 signifie que la région est réservée à l'interface avancée de configuration et d'énergie (ACPI 3.x). Bien qu'une région de type 3 puisse ne pas être utilisée par le système, elle peut être récupérée plus tard.

L'utilisation d'une carte de la mémoire vous permettra de gérer les ressources mémoire avec succès sans rencontrer de problèmes tels que des plantages ou une instabilité du système.

Il existe plusieurs façons de détecter la mémoire disponible de votre système. L'une d'elles consiste à utiliser le BIOS et l'interruption 15h. Une autre consiste à effectuer un sondage de la mémoire (memory probing).

Dans cet article, vous apprendrez quels outils sont disponibles pour vous aider à obtenir une carte de la mémoire de votre système, lesquels vous devriez utiliser, et lesquels vous devriez éviter et pourquoi. Enfin, vous verrez du code assembleur que vous pourrez utiliser dans votre propre chargeur d'amorçage (bootloader) / noyau.

### Prérequis

Si vous souhaitez suivre le code présenté dans cet article, vous aurez besoin de :

* Un système d'exploitation Linux
    
* Quelques connaissances en langage assembleur
    
* Un éditeur de texte de votre choix
    
* Un émulateur installé. Pour cet exemple, j'utilise QEMU.
    
* L'assembleur FASM installé
    
* Git pour pouvoir cloner le dépôt ([https://github.com/nikolaospanagopoulos/memoryMapBoot](https://github.com/nikolaospanagopoulos/memoryMapBoot))
    

### Quelques mots sur l'int 15h du BIOS

En mode Réel (Real mode), le BIOS propose de nombreuses interruptions qui interagissent avec le matériel et peuvent vous donner des informations.

Il existe certaines interruptions qui peuvent aider à obtenir une carte de la mémoire, mais la plus puissante est l'int 15h avec la fonction E820h (nombres hexadécimaux ! très important à retenir. Les nombres décimaux ne fonctionneront pas). Cette méthode offre une carte de la mémoire détaillée que vous pouvez utiliser pour déterminer en toute sécurité quelles zones de mémoire peuvent être utilisées pour des tâches vitales comme la configuration de la pagination, l'allocation de mémoire, et plus encore.

Dans cet article, vous verrez comment utiliser cette interruption pour obtenir une carte de la mémoire détaillée de votre système.

Maintenant, avant d'aller plus loin, j'aimerais ajouter quelques points sur le sondage de la mémoire et pourquoi vous devriez l'éviter.

### Le sondage de la mémoire et pourquoi vous devriez l'éviter

Le sondage de la mémoire (memory probing) est le processus consistant à accéder manuellement à la mémoire physique pour déterminer si elle est disponible ou non. Le problème est que toute la mémoire n'est pas conçue pour être accédée directement.

L'accès à des parties de la mémoire que vous ne devriez pas toucher peut provoquer des comportements imprévisibles tels que :

* **Plantages du système :** certaines zones de mémoire sont réservées aux structures du BIOS, aux périphériques matériels, etc. L'accès à ces zones peut entraîner des plantages ou une instabilité du système.
    
* **Corruption de la mémoire :** l'accès à des zones de mémoire réservées peut entraîner la corruption de ces zones. Cela peut à nouveau provoquer des plantages, de l'instabilité, des dysfonctionnements, etc.
    

Ainsi, vous devriez éviter le sondage de la mémoire car c'est un risque inutile pour votre processus de développement de noyau.

## Le Code

### Étape 1 : Préparer l'appel à l'int 15h

Dans cette partie, vous allez essentiellement configurer l'environnement nécessaire pour invoquer l'int 15h. Les registres à usage général doivent être sauvegardés afin qu'aucune donnée importante ne soit perdue lors de l'invocation de l'interruption. Ensuite, les registres `bp`, `ebx` sont effacés afin qu'ils puissent être initialisés à leurs valeurs de départ.

La valeur « SMAP » est stockée dans le registre `edx` pour garantir le format correct que le BIOS retournera. Enfin, nous configurons la fonction `0xe820` et demandons les données de la carte de la mémoire.

```plaintext
pusha
mov di, 0x0504        ; Définit le registre DI pour le stockage mémoire
xor ebx, ebx          ; EBX doit être à 0
xor bp, bp            ; BP doit être à 0 (pour compter les entrées)
mov edx, 0x534D4150   ; Place "SMAP" dans edx | La signature "SMAP" garantit que le BIOS fournit le format de carte mémoire correct
mov eax, 0xe820       ; Fonction 0xE820 pour obtenir la carte mémoire
mov dword [es:di + 20], 1 ; force une entrée ACPI 3.X valide | permet d'obtenir des informations supplémentaires (attributs étendus)
mov ecx, 24           ; Demande 24 octets de données
```

* La commande `pusha` a poussé tous les registres à usage général sur la pile pour sauvegarder leurs valeurs pendant l'appel d'interruption. Ils peuvent être restaurés après l'appel pour éviter la corruption d'autres zones.
    
* L'instruction `mov di, 0x0504` définit le registre di sur 0x0504 (où les entrées de la carte mémoire seront stockées).
    
* `xor ebx, ebx` : l'instruction xor utilise l'opérateur xor pour effacer le registre ebx. Il doit être mis à 0 pour commencer à récupérer les entrées.
    
* `xor bp, bp` : utilisation du même opérateur xor ici pour mettre bp à 0. Cela permettra de suivre vos entrées mémoire.
    
* `mov edx, 0x534D4150` : cette instruction stockera `0x534D4150` (chaîne ASCII « SMAP ») dans le registre edx. Elle garantit que le BIOS renverra le format correct pour votre carte mémoire.
    
* `mov eax, 0xe820` : cette instruction définit la fonction 0xe280 qui permettra d'obtenir la carte mémoire avec l'int 15h.
    
* `mov dword [es:di + 20], 1` : cette instruction force une entrée ACPI (Advanced Configuration and Power Interface) 3.x valide. De cette façon, le BIOS fournit des informations supplémentaires sous forme d'attributs étendus.
    
* `mov ecx, 24` : cette instruction demande au BIOS 24 octets de données mémoire. C'est la taille nécessaire pour que les entrées ACPI 3.x incluent des informations supplémentaires.
    

### Étape 2 : Appeler l'int 15h

Ici, vous pouvez enfin invoquer l'interruption pour récupérer la carte mémoire. Vous devez vérifier que la fonction est supportée par le BIOS et que des données valides sont récupérées. Vous devez également vous assurer que le format correct est récupéré en réglant à nouveau « SMAP » dans le registre `edx`.

```plaintext
    int 0x15                 ; utilisation de l'interruption
    jc short .failed         ; retenue (carry) activée au premier appel signifie "fonction non supportée"
    mov edx, 0x534D4150      ; Certains BIOS semblent corrompre ce registre ? réglons-le à nouveau
    cmp eax, edx             ; en cas de succès, eax doit avoir été réinitialisé à "SMAP"
    jne short .failed
    test ebx, ebx            ; ebx = 0 implique que la liste ne contient qu'une seule entrée (inutile)
    je short .failed
```

* `int 0x15` : cette instruction invoque l'interruption 0x15.
    
* `jc short .failed` : si le drapeau de retenue (carry flag) est activé, cela signifie que la fonction n'est pas supportée et que l'appel a échoué. Cela saute vers notre gestionnaire d'erreurs.
    
* `mov edx, 0x534D4150` : règle à nouveau « SMAP » car certains BIOS corrompent ce registre après l'appel.
    
* `cmp eax, edx` : si l'appel réussit, le BIOS renverra la valeur « SMAP » dans eax.
    
* `jne short .failed` : si ce n'est pas le cas, cela signifie que l'appel a échoué et cela saute vers notre étiquette de gestion des erreurs.
    
* `test ebx, ebx` : cette instruction vérifie si ebx est à 0 après le premier appel. Cela signifie que la carte mémoire ne contient qu'une seule entrée. Cette entrée est probablement invalide, donc elle saute vers l'étiquette de gestion des erreurs.
    

### Étape 3 : Parcourir les entrées de mémoire

Après une première invocation réussie, vous devez parcourir chaque entrée de la carte mémoire.

Dans la boucle, vous invoquerez à nouveau l'int 15h pour obtenir toutes les entrées de mémoire suivantes tout en vérifiant la longueur et les autres attributs de chaque entrée. Si elle répond aux critères, vous incrémentez le compteur et vous stockez l'entrée. Cela continue jusqu'à ce qu'il ne reste plus d'entrées à traiter.

```plaintext
    jmp short .jmpin
.e820lp:
    mov eax, 0xe820          ; eax, ecx sont corrompus à chaque appel int 0x15
    mov dword [es:di + 20], 1 ; force une entrée ACPI 3.X valide
    mov ecx, 24              ; demande à nouveau 24 octets
    int 0x15
    jc short .e820f          ; retenue activée signifie "fin de liste déjà atteinte"
    mov edx, 0x534D4150      ; répare le registre potentiellement corrompu
.jmpin:
    jcxz .skipent            ; ignore toute entrée de longueur 0 (si ecx est nul, ignore l'entrée)
    cmp cl, 20               ; réponse ACPI 3.X de 24 octets obtenue ?
    jbe short .notext
    test byte [es:di + 20], 1 ; si le bit 0 est vide, l'entrée doit être ignorée
    je short .skipent         ; saut si le bit 0 est vide 
.notext:
    mov eax, [es:di + 8]     ; obtient les 32 bits inférieurs de la longueur de la région mémoire
    or eax, [es:di + 12]     ; effectue un "or" avec les 32 bits supérieurs pour tester le zéro (little endian)
    jz .skipent              ; si la longueur totale est 0, ignore l'entrée
    inc bp                   ; entrée valide obtenue : ++compteur, passage à l'emplacement suivant
    add di, 24               ; déplace la prochaine entrée dans le tampon
.skipent:
    test ebx, ebx            ; si ebx revient à 0, la liste est complète
    jne short .e820lp
```

* `.e820lp` est une étiquette pour boucler à travers chaque entrée de la carte mémoire.
    

Les lignes suivantes sont utilisées pour appeler l'int 15h afin d'obtenir l'entrée de mémoire suivante :

* `jc short .e820f` : si le drapeau de retenue est activé, cela signifie que nous avons atteint la fin de la liste.
    
* `jcxz .skipent` : si le registre ecx est à 0, cela signifie que la longueur de l'entrée mémoire est invalide. Le code l'ignore donc.
    
* `cmp cl, 20` : vérifie si l'entrée mémoire est une entrée ACPI 3.x valide (elle ferait 24 octets de long). Si ce n'est pas le cas, le code saute vers `.notext`.
    
* `test byte [es:di + 20], 1` : vérifie si le bit 0 est défini dans les attributs étendus de l'entrée mémoire, indiquant une entrée valide. S'il est vide, l'entrée est ignorée.
    
* `mov eax, [es:di + 8]` : récupère les 32 bits inférieurs de la longueur de la région mémoire, puis nous les combinons avec l'opérateur or avec les 32 bits supérieurs. Si la longueur totale est 0, alors l'entrée est ignorée.
    
* `inc bp` : incrémente le nombre d'entrées.
    
* `add di, 24` : déplace le pointeur di vers l'entrée mémoire suivante. Chaque entrée fait 24 octets de long.
    

### Étape 4 : Gestion de la fin des entrées de mémoire

Enfin, vous pouvez stocker le nombre d'entrées. Et en utilisant l'instruction `popa`, vous restaurerez tous les registres à usage général à leurs valeurs précédentes. Si une erreur survient pendant le processus, le code saute vers l'étiquette `.failed` qui est notre fonction de gestion des erreurs.

```plaintext
.e820f:
    mov [mmap_ent], bp       ; stocke le nombre d'entrées
    clc                      ; il y a un "jc" en fin de liste vers ce point, donc la retenue doit être effacée

    popa
    ret
.failed:
    stc                      ; sortie en cas d'erreur "fonction non supportée"
    ret
```

* `mov [mmap_ent], bp` : stocke le nombre d'entrées.
    
* `clc` : efface le drapeau de retenue car il est déjà activé.
    
* `popa` : restaure tous les registres à usage général depuis la pile.
    
* `.failed` : nous utilisons cette étiquette pour la gestion des erreurs.
    

Voici une vidéo de ma chaîne YouTube où j'implémente et explique le code ci-dessus :

%[https://www.youtube.com/watch?v=WW3pduHMWkc&t=37s] 

### Épilogue

Dans le développement d'un noyau, l'une des tâches les plus importantes est la gestion de la mémoire. La méthode ci-dessus est un moyen fiable de détecter les informations de configuration de la mémoire de votre système. Cela signifie que vous pouvez prendre des décisions sûres lors de l'allocation des ressources, de l'implémentation de la pagination, etc.

Cela peut paraître complexe, et ça l'est peut-être, mais si vous suivez le code ligne par ligne, vous serez en mesure de le comprendre. Ces techniques vous permettront de construire un noyau robuste capable de fonctionner sur différentes configurations matérielles.

Continuez à coder !