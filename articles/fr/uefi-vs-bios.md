---
title: 'UEFI vs BIOS : Quelles sont les différences ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-10T20:11:31.000Z'
originalURL: https://freecodecamp.org/news/uefi-vs-bios
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/AMIBIOS_ROM-Chip_1992.jfif.jpg
tags:
- name: Computer Science
  slug: computer-science
seo_title: 'UEFI vs BIOS : Quelles sont les différences ?'
seo_desc: "By Vaibhav Kandwal\nSo you might have heard the acronyms BIOS and UEFI\
  \ thrown around, especially when trying to switch Operating Systems or messing around\
  \ with overclocking. \nAnd you might know what these acronyms stand for (Unified\
  \ Extensible Firmwar..."
---

Par Vaibhav Kandwal

Vous avez peut-être entendu les acronymes BIOS et UEFI, surtout lorsque vous essayez de changer de système d'exploitation ou de vous amuser avec l'overclocking. 

Et vous savez peut-être ce que signifient ces acronymes (Unified Extensible Firmware Interface et Basic Input/Output System, respectivement). Mais vous êtes-vous déjà demandé comment ils sont utilisés dans un système informatique ? 

Démystifions ces termes et leurs significations maintenant.

## Procédure de démarrage

Commençons par le commencement – je sais que nous nous écartons du sujet, mais je vous promets que cela vous aidera avec certains concepts plus tard.

Alors, comment un ordinateur démarre-t-il ? Allons-y étape par étape :

1. Vous appuyez sur le bouton d'alimentation de votre ordinateur portable/ordinateur de bureau.
2. Le CPU démarre, mais a besoin de quelques instructions pour fonctionner (rappelons que le CPU doit toujours faire quelque chose). Comme la mémoire principale est vide à ce stade, le CPU reporte le chargement des instructions à partir de la puce du firmware sur la carte mère et commence à exécuter les instructions.
3. Le code du firmware effectue un Power On Self Test (POST), initialise le matériel restant, détecte les périphériques connectés (souris, clavier, clé USB, etc.) et vérifie si tous les appareils connectés sont en bon état. Vous vous en souvenez peut-être comme d'un "bip" que les ordinateurs de bureau faisaient après un POST réussi.
4. Enfin, le code du firmware parcourt tous les périphériques de stockage et recherche un chargeur de démarrage (généralement situé dans le premier secteur d'un disque). Si le chargeur de démarrage est trouvé, le firmware lui transfère le contrôle de l'ordinateur.

Nous n'avons pas besoin d'en savoir plus sur ce sujet pour les besoins de cet article. Mais si vous êtes intéressé, alors continuez à lire (sinon, vous pouvez passer à la section suivante).

5. Maintenant que le chargeur de démarrage est chargé, son travail est de charger le reste du système d'exploitation. GRUB est un tel chargeur de démarrage capable de charger des systèmes d'exploitation de type Unix et est également capable de charger en chaîne le système d'exploitation Windows. Le chargeur de démarrage n'est disponible que dans le premier secteur d'un disque, qui fait 512 octets. Étant donné la complexité des systèmes d'exploitation modernes, certains de ces chargeurs de démarrage tendent à faire un chargement en plusieurs étapes, où le chargeur de démarrage principal charge le chargeur de démarrage de deuxième étape dans un environnement qui n'est pas limité à 512 octets.

6. Le chargeur de démarrage charge ensuite le [noyau](https://en.wikipedia.org/wiki/Kernel_(operating_system)) en mémoire. Les systèmes d'exploitation de type Unix exécutent ensuite le processus `init` (le processus maître, à partir duquel d'autres processus sont forkés/exécutés) et initialisent enfin les [niveaux d'exécution](https://en.wikipedia.org/wiki/Runlevel). 

7. Dans Windows, `wininit.exe` est chargé avec d'autres processus comme `services.exe` pour le contrôle des services, `lsass.exe` pour la sécurité locale et l'autorité (similaire aux niveaux d'exécution) et `lsm.exe` pour la gestion des sessions locales.

8. Après tout cela, et après que certains autres pilotes sont initialisés, l'interface utilisateur graphique (GUI) est chargée et vous êtes présenté avec l'écran de connexion.

C'était un aperçu très général du processus de démarrage. Si vous êtes intéressé par les systèmes d'exploitation, je vous recommande de lire davantage sur [osdev.net](https://wiki.osdev.org/Expanded_Main_Page). 

Revenons maintenant à notre sujet initial.

## BIOS :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Bios-configuracion-orden-arranque.png)

BIOS signifie Basic Input/Output System, le firmware dont nous avons parlé dans la procédure de démarrage ci-dessus. 

Il est stocké sur une EPROM (Erasable Programmable Read-Only Memory), permettant au fabricant de publier facilement des mises à jour. 

Il fournit de nombreuses fonctions d'assistance qui permettent de lire les secteurs de démarrage des stockages attachés et d'imprimer des choses à l'écran. Vous pouvez accéder au BIOS pendant les phases initiales de la procédure de démarrage en appuyant sur `del`, `F2` ou `F10`.

## UEFI :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/uefi_1270.png)
_ASUS UEFI_

UEFI signifie Unified Extensible Firmware Interface. Il fait le même travail qu'un BIOS, mais avec une différence fondamentale : il stocke toutes les données concernant l'initialisation et le démarrage dans un fichier .efi, au lieu de les stocker sur le firmware. 

Ce fichier .efi est stocké sur une partition spéciale appelée EFI System Partition (ESP) sur le disque dur. Cette partition ESP contient également le chargeur de démarrage.

UEFI a été conçu pour surmonter de nombreuses limitations de l'ancien BIOS, notamment :

1. UEFI supporte des tailles de disque jusqu'à 9 zettaoctets, tandis que le BIOS ne supporte que 2,2 téraoctets.
2. UEFI offre un temps de démarrage plus rapide.
3. UEFI dispose d'un support de pilotes discret, tandis que le BIOS a un support de pilotes stocké dans sa ROM, donc la mise à jour du firmware BIOS est un peu difficile.
4. UEFI offre une sécurité comme "Secure Boot", qui empêche l'ordinateur de démarrer à partir d'applications non autorisées/non signées. Cela aide à prévenir les rootkits, mais entrave également le dual-boot, car il traite les autres systèmes d'exploitation comme des applications non signées. Actuellement, seuls Windows et Ubuntu sont des systèmes d'exploitation signés (faites-moi savoir si je me trompe).
5. UEFI fonctionne en mode 32 bits ou 64 bits, tandis que le BIOS fonctionne en mode 16 bits. Ainsi, l'UEFI est capable de fournir une interface graphique (navigation avec la souris) contrairement au BIOS qui permet la navigation uniquement avec le clavier.

## Vous n'avez peut-être pas besoin de l'UEFI

Bien que tous les ordinateurs modernes soient équipés de l'UEFI par défaut, voici quelques raisons pour lesquelles vous pourriez choisir le BIOS plutôt que l'UEFI :

1. Si vous êtes débutant et que vous ne voulez pas vous soucier de manipuler un quelconque firmware, le BIOS est fait pour vous.
2. Si vous avez moins de 2 To par disque dur ou partition, vous pouvez opter pour le BIOS.
3. Le BIOS permet d'exécuter plusieurs systèmes d'exploitation sans changer de paramètres. Cela peut poser un problème de sécurité d'un point de vue moderne, mais bon, pas de tracas pour l'utilisateur.
4. Le BIOS fournit des informations système au système d'exploitation. Ainsi, si votre système d'exploitation fonctionne en mode 16 bits, il n'est pas nécessaire d'écrire du code pour interagir avec le matériel. Il peut directement utiliser les méthodes fournies par le BIOS. Sinon, si le système d'exploitation passe en mode 32 bits ou 64 bits, il doit alors fournir ses propres sous-routines pour interagir avec le matériel.
5. Si vous êtes quelqu'un qui préfère une interface utilisateur basée sur le clavier et le texte plutôt que la navigation avec une souris et une interface graphique, alors le BIOS est fait pour vous.

L'UEFI prend ces limitations en compte et fournit un mode Legacy. Dans ce mode, vous pouvez tout exécuter comme si vous aviez un firmware BIOS. Mais gardez à l'esprit qu'Intel a annoncé qu'il ne supportera plus le BIOS traditionnel à partir de 2020.

## Conclusion

Cet article vous a donné un aperçu des différences entre le BIOS et l'UEFI. Il vous conseille également sur le moment de choisir l'un ou l'autre et sur leurs différences. 

Si vous avez des questions, je serai toujours disponible sur Twitter. Merci pour votre temps.