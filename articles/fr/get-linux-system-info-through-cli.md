---
title: Comment obtenir des informations sur votre système Linux via la ligne de commande
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2025-06-11T10:15:20.560Z'
originalURL: https://freecodecamp.org/news/get-linux-system-info-through-cli
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749636399891/4b457f71-2d18-463a-b98a-e19ff5a6b769.png
tags:
- name: Linux
  slug: linux
- name: handbook
  slug: handbook
- name: cli
  slug: cli
seo_title: Comment obtenir des informations sur votre système Linux via la ligne de
  commande
seo_desc: 'Whether you’ve just gained access to a new Linux system, ethically hacked
  into one as part of a security test, or you’re just curious to know more about your
  current machine, this article will guide you through the process.

  You’ll learn how you can g...'
---

Que vous veniez d'obtenir l'accès à un nouveau système Linux, que vous ayez piraté un système de manière éthique dans le cadre d'un test de sécurité, ou que vous soyez simplement curieux d'en savoir plus sur votre machine actuelle, cet article vous guidera à travers le processus.

Vous apprendrez comment obtenir des informations liées à votre système d'exploitation (OS), noyau, CPU, mémoire, processus, disques, réseaux et logiciels installés. Vous explorerez les commandes et leurs sorties en détail.

## Table des matières

* [Pourquoi il est important de comprendre votre système Linux](#heading-pourquoi-il-est-important-de-comprendre-votre-systeme-linux)
    
* [Comment obtenir des informations sur votre OS et noyau sous Linux](#heading-comment-obtenir-des-informations-sur-votre-os-et-noyau-sous-linux)
    
* [Comment obtenir des informations sur votre CPU sous Linux](#heading-comment-obtenir-des-informations-sur-votre-cpu-sous-linux)
    
* [Comment obtenir des informations sur votre mémoire sous Linux](#heading-comment-obtenir-des-informations-sur-votre-memoire-sous-linux)
    
* [Comment obtenir des informations sur vos disques et systèmes de fichiers sous Linux](#heading-comment-obtenir-des-informations-sur-vos-disques-et-systemes-de-fichiers-sous-linux)
    
* [Comment obtenir des informations sur votre matériel sous Linux](#heading-comment-obtenir-des-informations-sur-votre-materiel-sous-linux)
    
* [Comment obtenir des informations sur vos interfaces réseau et leur statut sous Linux](#heading-comment-obtenir-des-informations-sur-vos-interfaces-reseau-et-leur-statut-sous-linux)
    
* [Comment obtenir des informations sur vos logiciels et services sous Linux](#heading-comment-obtenir-des-informations-sur-vos-logiciels-et-services-sous-linux)
    
* [Comment obtenir des informations sur vos logs et dmesg sous Linux](#heading-comment-obtenir-des-informations-sur-vos-logs-et-dmesg-sous-linux)
    
* [Comment obtenir des informations d'audit de sécurité/utilisateur sous Linux](#heading-comment-obtenir-des-informations-daudit-de-securiteutilisateur-sous-linux)
    
* [Commandes visuellement attrayantes](#heading-commandes-visuellement-attrayantes)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi il est important de comprendre votre système Linux

### Administration système

Les administrateurs système doivent avoir une compréhension du système afin de pouvoir :

* Gérer les utilisateurs, les groupes et les permissions de manière efficace.
    
* Configurer des services comme les serveurs web, les bases de données, etc.
    
* Automatiser les tâches répétitives avec des scripts et des cron jobs.
    

### Dépannage

Lorsque le système est dans un état problématique, une solide compréhension de la spécification et de la configuration du système vous aide à :

* Identifier et résoudre rapidement les erreurs système.
    
* Analyser les logs système et surveiller les performances.
    
* Diagnostiquer les problèmes réseau et matériel.
    

### Audit de sécurité

Si vous occupez un rôle lié à la sécurité, connaître votre système en profondeur vous aide à :

* Surveiller les logs pour détecter les accès non autorisés.
    
* Configurer les pare-feu et les politiques de sécurité.
    
* Détecter et supprimer les processus ou logiciels malveillants.
    

### Optimisation des performances

Si vous savez comment recueillir des informations liées aux ressources système, vous pouvez les mesurer et créer une projection pour une utilisation future. Vous pouvez également :

* Ajuster les paramètres système pour une meilleure efficacité.
    
* Surveiller l'utilisation des ressources (CPU, mémoire, disque, I/O).
    
* Éliminer les goulots d'étranglement et optimiser les charges de travail.
    

### Maintenance proactive

Il est bon de pouvoir prévenir les problèmes avant qu'ils ne surviennent. Une fois que vous connaissez bien votre système, vous pouvez :

* Planifier des mises à jour et des sauvegardes régulières.
    
* Assurer la fiabilité et le temps de fonctionnement du système.
    

Comprendre votre système Linux vous donne un meilleur contrôle, améliore la stabilité du système et augmente votre efficacité globale en tant qu'administrateur système ou utilisateur avancé.

Dans la section suivante, nous discuterons de quelques commandes essentielles pour recueillir des informations système.

## Comment obtenir des informations sur votre OS et noyau sous Linux

### Commande `uname -a`

`uname -a` fournit des informations complètes sur le noyau :

```bash
uname -a
Linux ip-172-31-90-178 6.8.0-1024-aws #26-Ubuntu SMP Tue Feb 18 17:22:37 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```

Voici ce que signifie chaque partie dans la commande ci-dessus :

* `Linux` : Le nom du noyau.
    
* `ip-172-31-90-178` : Le nom d'hôte réseau du système.
    
* `6.8.0-1024-aws` : La version du noyau et la build spécifique à AWS.
    
* `#26-Ubuntu` : Le numéro de build du noyau.
    
* `SMP` : Symmetric Multi-Processing, indiquant que le noyau est compilé pour plusieurs processeurs.
    
* `Tue Feb 18 17:22:37 UTC 2025` : La date et l'heure de compilation du noyau.
    
* `x86_64 x86_64 x86_64` : Le nom du matériel de la machine (architecture), le type de processeur et le type de plateforme, tous indiquant une architecture x86 64 bits.
    
* `GNU/Linux` : Le nom du système d'exploitation.
    

D'après cette sortie, j'exécute une instance AWS EC2 avec une distribution Ubuntu Linux 64 bits utilisant un noyau spécifiquement construit pour l'infrastructure AWS.

### Commandes `uname -r` et `uname -s`

Les commandes `uname -r` et `uname -s` spécifient les informations sur la version du noyau et le type de système d'exploitation :

```bash
uname -r
6.11.0-25-generic

uname -s
Linux
```

### Commande `cat /etc/os-release`

La commande `cat /etc/os-release` fournit des informations sur la distribution :

```bash
cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.2 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
```

Voici ce que signifie chaque partie dans la commande ci-dessus :

* `PRETTY_NAME="Ubuntu 24.04.2 LTS"` : Le nom convivial de la distribution incluant la version et la désignation LTS (Long Term Support).
    
* `NAME="Ubuntu"` : Le nom de la distribution Linux.
    
* `VERSION_ID="24.04"` : Le numéro de version de la sortie Ubuntu (format Année/Mois).
    
* `VERSION="24.04.2 LTS (Noble Numbat)"` : Les informations de version complètes incluant :
    
    • `24.04` : Version majeure (sortie en avril 2024)
    
    • `.2` : Numéro de version ponctuelle
    
    • `LTS` : Long Term Support
    
    • `Noble Numbat` : Le nom de code de la version
    
* `VERSION_CODENAME=noble` : Le nom de code de cette version Ubuntu ("Noble").
    
* `ID=ubuntu` : Le nom lisible par machine du système d'exploitation.
    
* `ID_LIKE=debian` : Indique qu'Ubuntu est basé sur Debian Linux.
    
* `HOME_URL`, `SUPPORT_URL`, `BUG_REPORT_URL`, `PRIVACY_POLICY_URL` : Diverses URL officielles pour les ressources Ubuntu.
    
* `UBUNTU_CODENAME=noble` : Répète le nom de code de cette version Ubuntu.
    
* `LOGO=ubuntu-logo` : Spécifie l'identifiant du logo pour la distribution.
    

Cette sortie montre que j'exécute Ubuntu 24.04.2 LTS (nom de code "Noble Numbat"), qui est une version Long Term Support d'Ubuntu. Étant une version LTS, elle recevra des mises à jour de sécurité et un support pour une période prolongée (généralement 5 ans pour les versions LTS d'Ubuntu).

### Commande `hostnamectl`

`hostnamectl` affiche le nom d'hôte, les informations sur le système d'exploitation et le noyau :

```bash
hostnamectl
 Static hostname: ip-172-31-90-178
       Icon name: computer-vm
         Chassis: vm 🖥
      Machine ID: ec272830b6dca2da0d11e41b292cfc99
         Boot ID: dd12f48ff01b44a796991d99ce1bcfde
  Virtualization: xen
Operating System: Ubuntu 24.04.2 LTS              
          Kernel: Linux 6.8.0-1024-aws
    Architecture: x86-64
 Hardware Vendor: Xen
  Hardware Model: HVM domU
Firmware Version: 4.11.amazon
   Firmware Date: Thu 2006-08-24
    Firmware Age: 18y 9month 1w 2d
```

Dans la commande ci-dessus, voici ce que signifie chaque partie :

* `Static hostname: "ip-172-31-90-178"` : Il s'agit du nom d'hôte permanent du système, stocké dans `/etc/hostname`.
    
* `Icon name: "computer-vm"` : Un identifiant d'icône symbolique pour le système, utilisé par certains environnements de bureau.
    
* `Chassis: "vm"` : Indique que cela s'exécute dans un environnement de machine virtuelle.
    
* `Machine ID: "ec272830b6dca2da0d11e41b292cfc99"` : Un identifiant unique pour ce système, stocké dans `/etc/machine-id`.
    
* `Boot ID: "dd12f48ff01b44a796991d99ce1bcfde"` : Un identifiant unique qui change à chaque démarrage du système.
    
* `Virtualization: "xen"` : Montre que ce système s'exécute sur la virtualisation Xen (courant pour les instances AWS).
    
* `Operating System: "Ubuntu 24.04.2 LTS"` : La distribution et la version actuelles du système d'exploitation.
    
* `Kernel: "Linux 6.8.0-1024-aws"` : La version actuelle du noyau Linux, spécifiquement un noyau optimisé pour AWS.
    
* `Architecture: "x86-64"` : L'architecture CPU du système.
    
* `Hardware Vendor: "Xen" Hardware Model: "HVM domU"` : Indique qu'il s'agit d'une instance utilisateur de domaine HVM (Hardware Virtual Machine) Xen.
    
* Détails du micrologiciel :
    
    * `Version: 4.11.amazon` : Il s'agit de la version du micrologiciel/BIOS spécifiquement personnalisée pour les environnements AWS.
        
    * `Date: Thu 2006-08-24` : Il s'agit de la date de sortie du micrologiciel. La date peut sembler ancienne (2006) mais cela est normal pour les instances AWS.
        
    * `Age: 18y 9month 1w` : Cela montre l'ancienneté du micrologiciel par rapport à la date actuelle calculée à partir de la date du micrologiciel (2006) jusqu'à aujourd'hui (2025). Bien que le micrologiciel semble ancien, il est toujours maintenu et sécurisé.
        

Cette sortie globale montre que j'exécute Ubuntu 24.04.2 LTS sur une instance AWS EC2 utilisant la virtualisation Xen. Le système utilise un noyau optimisé pour AWS et est configuré en tant qu'instance HVM (Hardware Virtual Machine).

## Comment obtenir des informations sur votre CPU sous Linux

### Commande `lscpu`

`lscpu` affiche l'architecture du CPU, les cœurs, les threads et les informations de virtualisation :

```bash
lscpu
Architecture:             x86_64
  CPU op-mode(s):         32-bit, 64-bit
  Address sizes:          46 bits physical, 48 bits virtual
  Byte Order:             Little Endian
CPU(s):                   1
  On-line CPU(s) list:    0
Vendor ID:                GenuineIntel
  Model name:             Intel(R) Xeon(R) CPU E5-2686 v4 @ 2
                          .30GHz
    CPU family:           6
    Model:                79
    Thread(s) per core:   1
    Core(s) per socket:   1
    Socket(s):            1
    Stepping:             1
    BogoMIPS:             4599.99
    Flags:                fpu vme de pse tsc msr pae mce cx8 
                          apic sep mtrr pge mca cmov pat pse3
                          6 clflush mmx fxsr sse sse2 ht sysc
                          all nx rdtscp lm constant_tsc rep_g
                          ood nopl xtopology cpuid tsc_known_
                          freq pni pclmulqdq ssse3 fma cx16 p
                          cid sse4_1 sse4_2 x2apic movbe popc
                          nt tsc_deadline_timer aes xsave avx
                           f16c rdrand hypervisor lahf_lm abm
                           pti fsgsbase bmi1 avx2 smep bmi2 e
                          rms invpcid xsaveopt
Virtualization features:  
  Hypervisor vendor:      Xen
  Virtualization type:    full
Caches (sum of all):      
  L1d:                    32 KiB (1 instance)
  L1i:                    32 KiB (1 instance)
  L2:                     256 KiB (1 instance)
  L3:                     45 MiB (1 instance)
NUMA:                     
  NUMA node(s):           1
  NUMA node0 CPU(s):      0
Vulnerabilities:          
  Gather data sampling:   Not affected
  Itlb multihit:          KVM: Mitigation: VMX unsupported
  L1tf:                   Mitigation; PTE Inversion
  Mds:                    Vulnerable: Clear CPU buffers attem
                          pted, no microcode; SMT Host state 
                          unknown
  Meltdown:               Mitigation; PTI
  Mmio stale data:        Vulnerable: Clear CPU buffers attem
                          pted, no microcode; SMT Host state 
                          unknown
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Vulnerable
  Spectre v1:             Mitigation; usercopy/swapgs barrier
                          s and __user pointer sanitization
  Spectre v2:             Mitigation; Retpolines; STIBP disab
                          led; RSB filling; PBRSB-eIBRS Not a
                          ffected; BHI Retpoline
  Srbds:                  Not affected
  Tsx async abort:        Not affected
```

Voici une brève explication de la sortie ci-dessus :

1. Informations de base sur le CPU

* Architecture : `x86_64` (64 bits)
    
* Modèle de CPU : Intel Xeon E5-2686 v4 (2,3 GHz)
    
* Cœurs/Threads : 1 cœur, 1 thread (pas d'Hyper-Threading)
    
* CPU physique (Socket) : 1
    

2. Performance et fonctionnalités

* Tailles du cache :
    
    * L1 : 32 KiB (données) + 32 KiB (instructions)
        
    * L2 : 256 KiB
        
    * L3 : 45 MiB (grand, typique pour Xeon)
        
* Flags : Prend en charge AVX, AES, SSE4.1/4.2 (utile pour le chiffrement/opérations vectorielles).
    

3. Virtualisation

* Hyperviseur : Fonctionne sur Xen (virtualisation complète).
    
* Prise en charge de la virtualisation : Oui (Intel VT-x).
    

4. Sécurité (Vulnérabilités)

* Meltdown/Spectre : Principalement atténuées (PTI, Retpolines).
    
* MDS/MMIO : Vulnérable (pas de correctifs de microcode).
    
* Spec Store Bypass : Vulnérable (pas d'atténuation).
    

5. NUMA (Mémoire)

* Nœud NUMA unique (pas de complexité multi-processeur).
    

La sortie montre que ma machine est un Intel Xeon monocœur (dans un environnement virtualisé/nuage) avec un grand cache L3 mais présente certaines vulnérabilités de CPU non corrigées.

### Commande `cat /proc/cpuinfo`

`cat /proc/cpuinfo` fournit des détails plus approfondis sur le CPU :

```bash
cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 79
model name	: Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz
stepping	: 1
microcode	: 0xd000404
cpu MHz		: 2299.998
cache size	: 46080 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm pti fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit mmio_stale_data bhi
bogomips	: 4599.99
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:
```

### Commande `nproc`

`nproc` affiche le nombre de cœurs :

```bash
nproc
1
```

La sortie de la commande ci-dessus montre qu'il y a un processeur disponible.

## Comment obtenir des informations sur votre mémoire sous Linux

### Commande `free -h`

Vous pouvez utiliser la commande `free -h` pour connaître la mémoire RAM totale/utilisée/libre :

```bash
free -h
               total        used        free      shared  buff/cache   available
Mem:           957Mi       406Mi       218Mi       920Ki       522Mi       551Mi
Swap:             0B          0B          0B
```

Voici une ventilation de la sortie partagée ci-dessus :

* `total` : La quantité totale de mémoire physique (RAM) ou d'espace de swap disponible sur le système.
    
* `used` : La quantité de mémoire actuellement utilisée par les applications et le système. Calculée comme : `total - free - buffers - cache`.
    
* `free` : La quantité de mémoire qui est complètement inutilisée.
    
* `shared` : Mémoire qui peut être simultanément accessible par plusieurs programmes.
    
* `buff/cache` : Combine deux types de mémoire :
    
    * Buffers : Mémoire utilisée pour la mise en mémoire tampon des E/S de périphériques de bloc.
        
    * Cache : Mémoire utilisée pour le cache de pages du système de fichiers - Cette mémoire peut être récupérée lorsque les applications en ont besoin.
        
    * `available` : Il inclut la mémoire 'free' plus la mémoire qui peut être récupérée à partir de `buff/cache`. Il s'agit de la colonne la plus importante pour déterminer si vous avez suffisamment de mémoire.
        

### Commande **vmstat**

`vmstat` signifie Virtual Memory Statistics, un outil pour surveiller les performances du système. Il fournit des informations sur l'utilisation de la mémoire, l'activité du CPU, les processus, les E/S de disque et l'utilisation du swap.

Vous pouvez également utiliser `vmstat` pour extraire des informations en temps réel. Voici comment procéder :

```bash
vmstat 1 5
procs -----------memory---------- ---swap-- -----io---- -system-- -------cpu-------
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st gu
 1  0      0 238264  46120 489056    0    0     3     8   23    0  0  0 82  0 18  0
 0  0      0 238264  46120 489060    0    0     0     0  240  120  0  1 98  0  1  0
 0  0      0 238264  46120 489060    0    0     0     0  239  124  0  0 98  0  2  0
 0  0      0 238264  46120 489060    0    0     0     0  199  101  0  0 95  0  5  0
 0  0      0 238264  46120 489060    0    0     0     0   36   25  0  0 78  0 22  0
```

Voici ce que fait la commande ci-dessus :

1. Capture 5 instantanés des performances du système.
    
2. Chaque instantané est pris à 1 seconde d'intervalle, donnant des informations presque en temps réel.
    
3. Affiche les métriques clés concernant :
    
    * L'utilisation de la mémoire (libre, mise en mémoire tampon, mise en cache).
        
    * L'activité du CPU (utilisateur, système, inactif, en attente).
        
    * Les processus (en cours d'exécution, bloqués).
        
    * Les E/S de disque (blocs lus/écrits).
        
    * L'utilisation du swap (si le swapping est en cours).
        

Notez que vous pouvez remplacer l'intervalle et le nombre d'instantanés en conséquence.

Voici une ventilation détaillée de la sortie ci-dessus :

* `Procs` :
    
    * `r` : Nombre de processus en attente de temps d'exécution.
        
    * `b` : Nombre de processus en sommeil ininterruptible
        
* `Memory` (en Ko) :
    
    * `swpd` : Quantité de mémoire virtuelle utilisée
        
    * `free` : Quantité de mémoire inactive
        
    * `buff` : Mémoire utilisée comme tampons
        
    * `cache` : Mémoire utilisée comme cache
        
* `Swap` :
    
    * `si` : Mémoire échangée depuis le disque (Ko/s)
        
    * `so` : Mémoire échangée vers le disque (Ko/s)
        
* `IO` :
    
    * `bi` : Blocs reçus depuis un périphérique de bloc (blocs/s)
        
    * `bo` : Blocs envoyés vers un périphérique de bloc (blocs/s)
        
* `System` :
    
    * `in` : Nombre d'interruptions par seconde
        
    * `cs` : Nombre de changements de contexte par seconde
        
* `CPU` (pourcentages) :
    
    1. `us` : Temps passé à exécuter du code utilisateur
        
    2. `sy` : Temps passé à exécuter du code système
        
    3. `id` : Temps passé inactif
        
    4. `wa` : Temps passé à attendre les E/S
        
    5. `st` : Temps volé à une machine virtuelle
        
    6. `gu` : Temps d'exécution du code invité (CPU virtuel)
        

D'après la sortie, on peut voir que mon système :

* A une utilisation CPU très faible (pourcentage élevé d'inactivité)
    
* N'a pas de swap utilisé (`swpd = 0`)
    
* A environ `99 Mo` de mémoire libre
    
* Montre une activité IO minimale
    
* S'exécute dans un environnement virtualisé (remarquez que la colonne `st` (volé) a une valeur non nulle
    

La première ligne montre les moyennes depuis le dernier redémarrage, tandis que les lignes suivantes montrent les statistiques en temps réel pour chaque seconde.

### Commande `cat /proc/meminfo`

`cat /proc/meminfo` affiche les statistiques détaillées de la mémoire :

```bash
cat /proc/meminfo
MemTotal:         980384 kB
MemFree:          245100 kB
MemAvailable:     585896 kB
Buffers:           46184 kB
Cached:           393672 kB
SwapCached:            0 kB
Active:           141404 kB
Inactive:         356376 kB
Active(anon):      47672 kB
Inactive(anon):    29300 kB
Active(file):      93732 kB
Inactive(file):   327076 kB
Unevictable:       36528 kB
Mlocked:           27152 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Zswap:                 0 kB
Zswapped:              0 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:         94488 kB
Mapped:            97936 kB
Shmem:               920 kB
KReclaimable:      95396 kB
Slab:             148672 kB
SReclaimable:      95396 kB
SUnreclaim:        53276 kB
KernelStack:        2444 kB
PageTables:         3224 kB
SecPageTables:         0 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:      490192 kB
Committed_AS:     508912 kB
VmallocTotal:   34359738367 kB
VmallocUsed:        9988 kB
VmallocChunk:          0 kB
Percpu:            14848 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
Unaccepted:            0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
DirectMap4k:       71680 kB
DirectMap2M:      976896 kB
```

Voici une ventilation détaillée de la sortie partagée ci-dessus :

* Mémoire totale et mémoire disponible :
    
    * `MemTotal` : Mémoire physique RAM totale disponible.
        
    * `MemFree` : Mémoire complètement inutilisée.
        
    * `MemAvailable` : Mémoire disponible pour les nouvelles applications.
        
* Caches et tampons de mémoire :
    
    * `Buffers` : Mémoire utilisée pour la mise en mémoire tampon des E/S de périphériques de bloc.
        
    * `Cached` : Mémoire utilisée pour le cache du système de fichiers.
        
    * `SwapCached` : Pages de mémoire stockées à la fois en RAM et en swap.
        
* Mémoire active vs inactive :
    
    * `Active` : Mémoire récemment utilisée.
        
    * `Inactive` : Mémoire moins récemment utilisée.
        
    * `Active(anon)` : Mémoire anonyme récemment utilisée.
        
    * `Active(file)` : Mémoire basée sur des fichiers récemment utilisée.
        
* Informations sur le swap :
    
    * `SwapTotal` : Espace de swap configuré.
        
    * `SwapFree` : Espace de swap disponible.
        
    * `Zswap` : Swap compressé en RAM.
        
* Autres métriques importantes :
    
    * `Dirty` : Mémoire en attente d'être écrite sur le disque.
        
    * `Mapped` : Fichiers mappés en mémoire.
        
    * `Slab` : Cache des structures de données du noyau.
        
    * `CommitLimit` : Mémoire totale disponible pour l'allocation.
        
    * `Committed_AS` : Mémoire totale actuellement allouée.
        

Une utilisation saine de la mémoire est indiquée par une bonne quantité de mémoire disponible, des mécanismes de mise en cache actifs en place et aucune pression sur la mémoire (pas besoin d'utiliser le swap).

## Comment obtenir des informations sur vos disques et systèmes de fichiers sous Linux

### Commande `tree -d -L 1`

`tree -d -L 1` affiche les détails du système de fichiers à partir du dossier dans lequel elle est exécutée. Pour obtenir les détails complets du système de fichiers, exécutez-la à partir du dossier racine `/` :

```bash
tree -d -L 1
.
├── bin -> usr/bin
├── bin.usr-is-merged
├── boot
├── dev
├── etc
├── home
├── lib -> usr/lib
├── lib.usr-is-merged
├── lib64 -> usr/lib64
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── sbin.usr-is-merged
├── snap
├── srv
├── sys
├── tmp
├── usr
└── var

25 directories
```

La sortie de la commande `tree -d -L 1` montre une structure d'arborescence de répertoires avec les options suivantes :

* `-d` : Affiche uniquement les répertoires (ignore les fichiers)
    
* `-L 1` : Limite la profondeur de l'arborescence à un niveau (n'affiche que les sous-répertoires immédiats)
    
* `df -h` : systèmes de fichiers montés et utilisation :
    
    ```bash
    df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/root        29G  2.6G   26G   9% /
    tmpfs           479M     0  479M   0% /dev/shm
    tmpfs           192M  908K  191M   1% /run
    tmpfs           5.0M     0  5.0M   0% /run/lock
    /dev/xvda16     881M  144M  676M  18% /boot
    /dev/xvda15     105M  6.1M   99M   6% /boot/efi
    tmpfs            96M   12K   96M   1% /run/user/1000
    ```
    
    La sortie ci-dessus de la commande `df -h` montre les informations suivantes sur l'utilisation de l'espace disque :
    
    * `Filesystem` : Le nom du système de fichiers/périphérique monté.
        
    * `Size` : Taille totale du système de fichiers.
        
    * `Used` : Quantité d'espace utilisé.
        
    * `Avail` : Quantité d'espace disponible.
        
    * `Use%` : Pourcentage d'espace utilisé.
        
    * `Mounted on` : Le point de montage où le système de fichiers est attaché
        

### Commande `lsblk`

`lsblk` signifie 'list block devices' et affiche des informations sur tous les périphériques de bloc disponibles comme les disques durs, les SSD, etc.

```bash
lsblk
NAME     MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0      7:0    0 26.3M  1 loop /snap/amazon-ssm-agent/9881
loop1      7:1    0 73.9M  1 loop /snap/core22/1748
loop2      7:2    0 44.4M  1 loop /snap/snapd/23545
loop3      7:3    0 50.9M  1 loop /snap/snapd/24505
loop4      7:4    0 73.9M  1 loop /snap/core22/1963
loop5      7:5    0 27.2M  1 loop /snap/amazon-ssm-agent/11320
xvda     202:0    0   30G  0 disk 
├─xvda1  202:1    0   29G  0 part /
├─xvda14 202:14   0    4M  0 part 
├─xvda15 202:15   0  106M  0 part /boot/efi
└─xvda16 259:0    0  913M  0 part /boot
```

La sortie ci-dessus montre les détails suivants :

* `NAME` : Nom du périphérique.
    
* `MAJ:MIN` : Numéros de périphérique majeur et mineur.
    
* `RM` : Indicateur de périphérique amovible (1 pour amovible, 0 pour fixe).
    
* `SIZE` : Taille du périphérique.
    
* `RO` : Indicateur de lecture seule (1 pour lecture seule, 0 pour lecture-écriture).
    
* `TYPE` : Type de périphérique (disque, part pour partition, loop pour périphérique loop).
    
* `MOUNTPOINTS` : Où le périphérique est monté.
    

### Commande `fdisk -l`

`fdisk -l` affiche tous les périphériques de disque et leurs partitions sur votre système :

```bash
Disk /dev/xvda: 30 GiB, 32212254720 bytes, 62914560 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: E3478E01-32E3-4FC2-8E79-1BCCDE89C2D7

Device        Start      End  Sectors  Size Type
/dev/xvda1  2099200 62914526 60815327   29G Linux filesystem
/dev/xvda14    2048    10239     8192    4M BIOS boot
/dev/xvda15   10240   227327   217088  106M EFI System
/dev/xvda16  227328  2097152  1869825  913M Linux extended boot
```

La sortie ci-dessus montre les informations de partition pour le disque principal du système (`/dev/xvda`) qui fait 30 GiB de taille et a quatre partitions :

* `/dev/xvda1` : `29G` système de fichiers Linux (partition principale du système).
    
* `/dev/xvda14` : `4M` partition de démarrage BIOS.
    
* `/dev/xvda15` : `106M` partition de système EFI (pour le démarrage UEFI).
    
* `/dev/xvda16` : `913M` partition de démarrage étendue Linux.
    

### Commande `mount`

`mount` affiche tous les systèmes de fichiers actuellement montés au format : `device/source "on" mount_point "type" filesystem_type (mount_options)`, affichant où et comment chaque système de fichiers est attaché à l'arborescence des répertoires de votre système.

Voici un exemple de ligne de la sortie de `mount` :

```bash
/dev/xvda1 on / type ext4 (rw,relatime,discard,errors=remount-ro,commit=30)
```

Quelques options de montage courantes que vous verrez sont :

* `rw` : Accès en lecture-écriture.
    
* `ro` : Accès en lecture seule.
    
* `nosuid` : Désactiver les bits SUID/SGID.
    
* `nodev` : Empêcher l'interprétation des fichiers de périphérique.
    
* `noexec` : Empêcher l'exécution des binaires.
    
* `relatime` : Mettre à jour les temps d'accès de manière relative.
    

### Commande `du -sh *`

`du -sh *` fournit un résumé de l'utilisation du disque pour chaque fichier et répertoire dans le répertoire courant (bon pour trouver les gros consommateurs de disque) :

```bash
du -sh *
4.0K    file1.txt
8.0K    file2.txt
12K     directory1
20K     directory2
```

## Comment obtenir des informations sur votre matériel sous Linux

### Commande `lshw`

La commande `lshw` fournit des informations détaillées sur la configuration matérielle de l'ordinateur. Elle peut rapporter :

* Configuration de la mémoire.
    
* Version du micrologiciel.
    
* Configuration de la carte mère.
    
* Version et vitesse du CPU.
    
* Configuration du cache.
    
* Vitesse du bus et plus.
    

Elle est particulièrement utile pour les administrateurs système et les utilisateurs qui doivent recueillir des informations matérielles détaillées. La commande peut sortir des informations dans divers formats, y compris HTML, XML, JSON ou texte brut.

Voici une partie de la sortie de `lshw` :

```bash
*-pci
          description: Host bridge
          product: 440FX - 82441FX PMC [Natoma]
          vendor: Intel Corporation
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 02
          width: 32 bits
          clock: 33MHz
        *-isa
             description: ISA bridge
             product: 82371SB PIIX3 ISA [Natoma/Triton II]
             vendor: Intel Corporation
             physical id: 1
             bus info: pci@0000:00:01.0
             version: 00
             width: 32 bits
             clock: 33MHz
             capabilities: isa bus_master
             configuration: latency=0
```

### Commande `lspci`

`lspci` affiche des informations sur tous les bus PCI (Peripheral Component Interconnect) et les périphériques connectés à votre système.

```bash
lspci
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]
00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 01)
00:02.0 VGA compatible controller: Cirrus Logic GD 5446
00:03.0 Unassigned class [ff80]: XenSource, Inc. Xen Platform Device (rev 01)
```

D'après la sortie, nous pouvons voir que :

* Chaque ligne commence par une adresse `bus:device.function` (comme "`00:00.0`")
    
* Suivant l'adresse se trouve la classe de périphérique et les détails spécifiques du matériel :
    
    * Un pont hôte (`Intel 440FX`), qui gère les communications entre le CPU et les autres composants.
        
    * Un pont ISA (`Intel PIIX3`), pour la prise en charge des périphériques hérités.
        
    * Une interface IDE pour les périphériques de stockage.
        
    * Un pont ACPI pour la gestion de l'alimentation.
        
    * Un contrôleur graphique VGA (Cirrus Logic).
        
    * Un périphérique de plateforme Xen (ce qui suggère que vous exécutez dans un environnement virtualisé Xen).
        

La commande est particulièrement utile pour :

* Dépanner les problèmes matériels
    
* Vérifier la détection du matériel
    
* Trouver les détails du matériel pour l'installation des pilotes
    
* Vérifier la configuration du système
    

## Comment obtenir des informations sur vos interfaces réseau et leur statut sous Linux

### Commande `ip a`

`ip a` affiche des informations sur toutes les interfaces réseau de votre système :

```bash
ip -a
1: lo: <LOOPBACK,UP,LOWER_UP>
- Il s'agit de l'interface de boucle locale (localhost)
- MTU (Unité de Transmission Maximale) est de 65536 octets
- Adresse IP : 127.0.0.1/8 (IPv4)
- Adresse IPv6 : ::1/128

2. Interface Réseau (enX0) :
enX0: <BROADCAST,MULTICAST,UP,LOWER_UP>
- Il s'agit de votre interface réseau principale
- MTU est de 9001 octets
- Adresse MAC (ether) : 12:16:a6:d3:b3:61
- Adresse IPv4 : 172.31.90.178/20
- Adresse IPv6 : fe80::1016:a6ff:fed3:b361/64 (Liaison locale)
```

Voici les éléments clés de la sortie :

* État de l'interface (UP/DOWN).
    
* Adresse MAC (ether).
    
* Adresses IPv4 et IPv6.
    
* Portée du réseau (hôte, global, liaison).
    
* Durée de validité de l'adresse (valid_lft).
    
* Adresse de diffusion (brd).
    

### Commande `ip r`

`ip r` affiche la table de routage du système :

```bash
ip r
default via 172.31.80.1 dev enX0 proto dhcp src 172.31.90.178 metric 100 
172.31.0.2 via 172.31.80.1 dev enX0 proto dhcp src 172.31.90.178 metric 100 
172.31.80.0/20 dev enX0 proto kernel scope link src 172.31.90.178 metric 100 
172.31.80.1 dev enX0 proto dhcp scope link src 172.31.90.178 metric 100 
```

La sortie `ip r` ci-dessus montre la table de routage de mon système avec les routes suivantes :

* Route par défaut (Passerelle) :
    
    * Default via `172.31.80.1` : Tout le trafic ne correspondant pas aux autres règles passe par cette passerelle.
        
    * Utilisation de l'interface `enX0`.
        
    * Configuré via DHCP.
        
    * Adresse IP source : `172.31.90.178`.
        
* Réseau local :
    
    * `172.31.80.0/20` : Sous-réseau local (couvre les IP de `172.31.80.0` à `172.31.95.255`)
        
    * Directement connecté à l'interface `enX0`
        
    * Route gérée par le noyau (proto kernel)
        
    * Pour les paquets provenant de `172.31.90.178`
        
* Route DHCP :
    
    * Route directe vers le serveur DHCP (`172.31.80.1`)
        
    * Via l'interface `enX0`
        

Toutes les routes ont une métrique de 100, qui détermine la priorité des routes (les valeurs les plus basses sont préférées).

`netstat -tuln` affiche les ports d'écoute actifs :

```bash
netstat -tuln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
udp        0      0 127.0.0.54:53           0.0.0.0:*                          
udp        0      0 127.0.0.53:53           0.0.0.0:*                          
udp        0      0 172.31.90.178:68        0.0.0.0:*                          
udp        0      0 127.0.0.1:323           0.0.0.0:*                          
udp6       0      0 ::1:323                 :::*                               
```

## Comment obtenir des informations sur vos logiciels et services sous Linux

### Paquets installés

Vous pouvez vérifier les paquets installés avec `dpkg -l`, `apt list --installed` (Debian/Ubuntu). Voici un extrait de la sortie :

```bash
vim-common/noble-updates,noble-security,now 2:9.1.0016-1ubuntu7.8 all [installed,automatic]
vim-runtime/noble-updates,noble-security,now 2:9.1.0016-1ubuntu7.8 all [installed,automatic]
vim-tiny/noble-updates,noble-security,now 2:9.1.0016-1ubuntu7.8 amd64 [installed,automatic]
vim/noble-updates,noble-security,now 2:9.1.0016-1ubuntu7.8 amd64 [installed,automatic]
```

### Statut du service

`systemctl list-units --type=service` liste les services. Vous pouvez également utiliser `systemctl status <service>` et remplacer `<service>` par celui que vous souhaitez.

Voici la sortie pour `cron.service` :

```bash
systemctl status cron.service
● cron.service - Regular background program processing daemon
     Loaded: loaded (/usr/lib/systemd/system/cron.service; enabled; preset: enabled)
     Active: active (running) since Wed 2025-05-14 19:46:58 UTC; 2 weeks 5 days ago
       Docs: man:cron(8)
   Main PID: 625 (cron)
      Tasks: 1 (limit: 1129)
     Memory: 1.7M (peak: 4.7M)
        CPU: 20.890s
     CGroup: /system.slice/cron.service
             └─625 /usr/sbin/cron -f -P

Jun 03 09:25:01 ip-172-31-90-178 CRON[121748]: pam_unix(cron:session): session closed for user root
Jun 03 09:35:01 ip-172-31-90-178 CRON[121817]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
Jun 03 09:35:01 ip-172-31-90-178 CRON[121818]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Jun 03 09:35:01 ip-172-31-90-178 CRON[121817]: pam_unix(cron:session): session closed for user root
Jun 03 09:45:01 ip-172-31-90-178 CRON[122050]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
Jun 03 09:45:01 ip-172-31-90-178 CRON[122051]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Jun 03 09:45:01 ip-172-31-90-178 CRON[122050]: pam_unix(cron:session): session closed for user root
Jun 03 09:55:01 ip-172-31-90-178 CRON[122318]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
Jun 03 09:55:01 ip-172-31-90-178 CRON[122319]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
Jun 03 09:55:01 ip-172-31-90-178 CRON[122318]: pam_unix(cron:session): session closed for user root
lines 5-21/21 (END)
```

### **Processus**

`ps aux` affiche tous les processus avec leur statut respectif :

```bash
ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.4  22556 13952 ?        Ss   May14   0:35 /usr/lib/systemd/systemd --system --deserialize=63
root           2  0.0  0.0      0     0 ?        S    May14   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    May14   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   May14   0:00 [kworker/R-rcu_g]
root           5  0.0  0.0      0     0 ?        I<   May14   0:00 [kworker/R-rcu_p]
root           6  0.0  0.0      0     0 ?        I<   May14   0:00 [kworker/R-slub_]
.
.
.
```

Voici une explication de chaque colonne dans la sortie `ps aux` :

* `USER` : Le propriétaire du processus
    
* `PID` : Numéro d'identification du processus
    
* `%CPU` : Pourcentage d'utilisation du CPU
    
* `%MEM` : Pourcentage d'utilisation de la mémoire
    
* `VSZ` : Taille de la mémoire virtuelle en kilooctets (taille totale du programme)
    
* `RSS` : Taille de l'ensemble résident en kilooctets (mémoire réellement utilisée)
    
* `TTY` : Terminal associé au processus ('?' signifie pas de terminal)
    
* `STAT` : Code d'état du processus :
    
    * `S` : En sommeil
        
    * `R` : En cours d'exécution
        
    * `I` : Inactif
        
    * `Z` : Zombie
        
    * `T` : Arrêté
        
    * `s` : Leader de session
        
    * `<` : Priorité élevée
        
    * `N` : Priorité faible
        
* `START` : Heure à laquelle le processus a démarré
    
* `TIME` : Temps CPU cumulé utilisé
    
* `COMMAND` : La commande avec tous ses arguments
    

### Commandes `top` et `htop`

`top` ou `htop` peuvent être utilisés pour un aperçu de l'utilisation en temps réel, et pour afficher une vue dynamique des performances du système et des processus en cours d'exécution. Voici ce qu'ils affichent :

* Aperçu du système :
    
    * Temps de fonctionnement du système et nombre d'utilisateurs connectés.
        
    * Valeurs de charge moyenne pour les dernières 1, 5 et 15 minutes.
        
    * Nombre total de processus et leurs états (en cours d'exécution, en sommeil, arrêté, zombie)
        
* Utilisation des ressources :
    
    * Répartition de l'utilisation du CPU (utilisateur, système, inactif, etc.).
        
    * Utilisation de la mémoire (totale, libre, utilisée, mise en cache).
        
    * Utilisation de l'espace de swap
        
    * Liste des processus : Affiche une liste triée des processus en cours d'exécution (par défaut triés par utilisation du CPU) Pour chaque processus, affiche :
        
        * Identifiant de processus (PID).
            
        * Utilisateur propriétaire du processus.
            
        * Utilisation du CPU et de la mémoire.
            
        * Priorité du processus et valeur nice.
            
        * Détails de l'utilisation de la mémoire (virtuelle, résidente, partagée).
            
        * Statut du processus.
            
        * Temps d'exécution.
            
        * Nom de la commande.
            
    
    ```bash
    top - 10:04:25 up 19 days, 14:17,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks: 104 total,   1 running, 103 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.0 sy,  0.0 ni, 88.0 id,  0.0 wa,  0.0 hi,  0.0 si, 12.0 st 
    MiB Mem :    957.4 total,    247.3 free,    366.1 used,    533.7 buff/cache     
    MiB Swap:      0.0 total,      0.0 free,      0.0 used.    591.3 avail Mem 
    
        PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                              
          1 root      20   0   22556  13952   9728 S   0.0   1.4   0:35.08 systemd                                              
          2 root      20   0       0      0      0 S   0.0   0.0   0:00.16 kthreadd                                             
          3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_workqueue_release                               
          4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-rcu_g                                      
          5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-rcu_p                                      
          6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-slub_                                      
          7 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-netns                                      
         10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-events_highpri                          
         12 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-mm_pe                                      
         13 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_rude_kthread                               
         14 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_trace_kthread                              
    ```
    
    La commande top met à jour ces informations régulièrement (par défaut toutes les 3 secondes) et est couramment utilisée pour :
    
* Surveiller les performances du système
    
* Identifier les processus gourmands en ressources
    
* Résoudre les ralentissements du système
    
* Obtenir un aperçu rapide de l'état de santé du système
    
    Vous pouvez également interagir avec top pendant son exécution en utilisant diverses commandes clavier (comme 'k' pour tuer un processus, '1' pour voir les cœurs du CPU, etc.).
    

## Comment obtenir des informations sur vos logs et dmesg sous Linux

En fonction de la configuration du système, un certain nombre de logs sont générés. Il peut s'agir de logs d'audit, de logs système, de logs cron, etc. Ils contiennent tous des informations utiles. Voici quelques commandes que vous pouvez utiliser pour afficher les logs :

* `dmesg | less` : Tampon circulaire du noyau (problèmes matériels, messages de démarrage)
    
* `journalctl -xe` : Logs critiques récents (systèmes systemd)
    
* `/var/log/syslog` ou `/var/log/messages` : Logs généraux du système
    

## Comment obtenir des informations d'audit de sécurité/utilisateur sous Linux

`whoami` affiche le nom d'utilisateur de l'utilisateur actuel.

```bash
whoami
ubuntu
```

`id` affiche des informations détaillées sur l'identité d'un utilisateur sur le système.

```bash
id
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),24(cdrom),27(sudo),30(dip),105(lxd)
```

Décomposons la sortie :

* Identifiant utilisateur (uid) : `uid=1000(ubuntu)` signifie que l'identifiant utilisateur est 1000, avec le nom d'utilisateur "ubuntu"
    
* Identifiant du groupe principal (gid) : `gid=1000(ubuntu)` signifie que l'identifiant du groupe principal est 1000, nommé "ubuntu"
    
* Groupes supplémentaires (groups) : L'utilisateur appartient aux groupes suivants :
    
    * `ubuntu (1000)` : Votre groupe principal.
        
    * `adm (4)` : Pour les tâches de surveillance du système.
        
    * `cdrom (24)` : Pour accéder aux périphériques CD-ROM.
        
    * `sudo (27)` : Permet d'exécuter des commandes avec des privilèges superutilisateur.
        
    * `dip (30)` : Pour gérer les connexions dial-up.
        
    * `lxd (105)` : Pour gérer les conteneurs LXD.
        

La commande `id` est utile pour vérifier les identifiants utilisateur et groupe, vérifier les appartenances aux groupes, résoudre les problèmes de permissions et confirmer l'accès sudo.

`who` affiche des informations sur les utilisateurs actuellement connectés au système :

```bash
who
ubuntu   pts/0        2025-06-03 08:45 (39.43.159.5)
```

La décomposition de la sortie est présentée ci-dessous :

* Nom d'utilisateur : "`ubuntu`"
    
* Terminal : "`pts/0`" (pseudo-terminal)
    
* Heure de connexion : "`2025-06-03 08:45"`
    
* Hôte distant : "`(39.43.159.5)`" - l'adresse IP à partir de laquelle la connexion a été établie
    
* `w` - affiche qui est connecté et ce qu'ils font :
    

```bash
w
 10:21:46 up 19 days, 14:35,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
ubuntu   pts/0    39.43.159.5      08:45   44:56   0.00s  0.02s sshd: ubuntu [priv]
```

Voici la décomposition du résultat :

Première ligne :

* `10:21:46` : Heure actuelle du système
    
* `up 19 days, 14:35` : Temps de fonctionnement du système (combien de temps le système a été en cours d'exécution)
    
* `1 user` : Nombre d'utilisateurs actuellement connectés
    
* `load average: 0.24, 0.05, 0.02` : Moyennes de charge du système pour les dernières 1, 5 et 15 minutes
    
    * Les nombres inférieurs à 1.0 indiquent une faible charge du système
        
    * Les nombres plus élevés indiquent une charge/stress plus importante du système
        

La deuxième ligne montre les en-têtes de colonne pour les informations utilisateur ci-dessous :

* `USER` : Nom d'utilisateur.
    
* `TTY` : Périphérique terminal utilisé.
    
* `FROM` : Hôte distant à partir duquel l'utilisateur est connecté.
    
* `LOGIN@` : Heure à laquelle l'utilisateur s'est connecté.
    
* `IDLE` : Temps écoulé depuis la dernière activité de l'utilisateur.
    
* `JCPU` : Temps CPU utilisé par tous les processus attachés au tty.
    
* `PCPU` : Temps CPU utilisé par le processus actuel.
    
* `WHAT` : Processus/commande actuel en cours d'exécution.
    

`last` affiche un historique des connexions utilisateur et des redémarrages du système :

```bash
last
ubuntu   pts/1        39.43.159.5      Tue Jun  3 10:15 - 10:17  (00:02)
ubuntu   pts/0        39.43.159.5      Tue Jun  3 08:45   still logged in
ubuntu   pts/0        39.43.159.5      Tue Jun  3 05:23 - 08:29  (03:06)
ubuntu   pts/0        39.43.159.5      Sun Jun  1 06:32 - 12:24  (05:52)
ubuntu   pts/0        39.43.159.5      Thu May 22 05:39 - 05:58  (00:18)
ubuntu   pts/0        139.135.32.93    Wed May 21 14:45 - 14:47  (00:01)
ubuntu   pts/0        139.135.32.93    Wed May 21 11:58 - 13:49  (01:51)
ubuntu   pts/0        39.43.159.5      Wed May 21 05:05 - 05:12  (00:06)
ubuntu   pts/0        39.43.159.5      Tue May 20 18:41 - 21:45  (03:04)
ubuntu   pts/0        39.43.159.5      Thu May 15 06:12 - 06:12  (00:00)
ubuntu   pts/0        39.43.159.5      Thu May 15 06:05 - 06:12  (00:07)
ubuntu   pts/0        18.206.107.27    Wed May 14 20:06 - 20:08  (00:01)
ubuntu   pts/0        182.185.185.39   Wed May 14 19:48 - 19:50  (00:01)
reboot   system boot  6.8.0-1024-aws   Wed May 14 19:46   still running

wtmp begins Wed May 14 19:46:47 2025
```

Chaque ligne montre :

* Nom d'utilisateur (dans ce cas, toutes les connexions proviennent de l'utilisateur 'ubuntu').
    
* Périphérique terminal (`pts/0` indique un pseudo-terminal, généralement utilisé pour les connexions SSH).
    
* Adresse IP de l'hôte distant (d'où provient la connexion).
    
* Heure et date de connexion.
    
* Heure de déconnexion ou statut.
    
* Durée de la session entre parenthèses.
    

`sudo -l` montre ce que l'utilisateur actuel peut faire avec sudo.

```bash
sudo -l
Matching Defaults entries for ubuntu on ip-172-31-90-178:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User ubuntu may run the following commands on ip-172-31-90-178:
    (ALL : ALL) ALL
    (ALL) NOPASSWD: ALL
```

Cette sortie indique que l'utilisateur 'ubuntu' a :

* Un accès sudo complet (peut exécuter n'importe quelle commande)
    
* Aucune exigence de mot de passe pour les commandes sudo
    
* Des privilèges administratifs complets sur le système
    

## Commandes visuellement attrayantes

Dans cette section, vous apprendrez deux commandes qui affichent les informations que nous avons vues précédemment sous une forme présentable et esthétique.

`neofetch` - affiche les informations du système ainsi que le logo de la distribution :

![Sortie du terminal de la commande neofetch affichant les informations du système Ubuntu, y compris le système d'exploitation, le noyau, le temps de fonctionnement, le CPU, le GPU, la mémoire et un logo ASCII coloré](https://cdn.hashnode.com/res/hashnode/image/upload/v1748945743174/9cef1af7-fce8-4657-ad26-7d75b5755dd1.png align="center")

`btop` affiche des statistiques dynamiques avec différents modes :

![Une capture d'écran en temps réel du moniteur système btop montrant l'utilisation en temps réel du CPU, de la mémoire, du disque et du réseau dans un terminal. Des graphiques colorés affichent les métriques de performance pour les processus, les températures et le temps de fonctionnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1748945510465/8c8c200c-bb1a-4123-8db7-c30bb6a1c9bf.gif align="center")

## Conclusion

Merci d'avoir lu l'article jusqu'à la fin. Si vous l'avez trouvé utile, envisagez de le partager avec d'autres.

**Restez connecté et continuez votre parcours d'apprentissage !**

Je lis chaque message, venez dire bonjour 👋

1. **Connectez-vous avec moi sur** :
    
    * [LinkedIn](https://www.linkedin.com/in/zaira-hira/) : Je partage du contenu lié à Linux, la cybersécurité et DevOps. Laissez une recommandation sur LinkedIn et endossez-moi sur des compétences pertinentes.
        
    * [Discord](https://discord.gg/9zfbjEDs) communauté : Traînez avec d'autres développeurs ou partagez vos accomplissements.
        
    * [X](https://twitter.com/hira_zaira) : Je partage des mises à jour pré-lancement et quelques coulisses.
        
2. **Accédez à du contenu exclusif** : Pour une aide individuelle et du contenu exclusif, allez [ici](https://buymeacoffee.com/zairah/extras).
    

Mes [articles](https://www.freecodecamp.org/news/author/zaira/) font partie de ma mission pour augmenter l'accessibilité à du contenu de qualité pour tous. Chaque article prend beaucoup de temps et d'efforts à écrire. Cet article sera gratuit, pour toujours. Si vous avez apprécié mon travail et souhaitez me motiver, envisagez de [m'offrir un café](https://buymeacoffee.com/zairah).

Merci encore une fois et bon apprentissage !