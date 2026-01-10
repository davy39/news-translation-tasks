---
title: Comment commencer avec CentOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T16:13:42.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-centos-15eac7215c99
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bIzsWHmJ6nun5bayHe3LKg.png
tags:
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: System administration
  slug: system-administration
- name: 'tech '
  slug: tech
seo_title: Comment commencer avec CentOS
seo_desc: 'By Krasimir Vatchinsky

  You can download CentOS versions here.

  CentOS or Community Enterprise OS is an open source distribution based on RHEL or
  Red Hat Enterprise Linux. This is available only if you’ve bought the support package.
  Moreover, all RHEL ...'
---

Par Krasimir Vatchinsky

Vous pouvez télécharger les versions de CentOS [_ici_](https://wiki.centos.org/Download).

CentOS ou Community Enterprise OS est une distribution open source basée sur RHEL ou Red Hat Enterprise Linux. Cela n'est disponible que si vous avez acheté le package de support. De plus, tous les packages RHEL sont entièrement compatibles avec CentOS, offrant une plateforme robuste, stable et facile à gérer, garantissant le plus haut niveau de sécurité opérationnelle gratuitement.

CentOS est compatible binaire avec RHEL dès la sortie de la boîte et est la plateforme préférée pour les installations de serveurs. L'une des parties les plus précieuses de CentOS est le long cycle de support. Alors que les cycles de support de publication pour Fedora, par exemple, durent jusqu'à 13 mois, les versions de CentOS fournissent un support jusqu'à 7 ans. Cela le rend extrêmement fiable et fiable.

De plus, le projet communautaire CentOS étend sa disponibilité sur une large gamme de plateformes comme Google, Amazon AWS et d'autres. Il est également disponible dans des images génériques activées par cloud-init.

Pour en savoir plus sur CentOS, visitez [le projet CentOS ici](https://www.centos.org/).

#### Versions

![Image](https://cdn-media-1.freecodecamp.org/images/FexWtcAsU02omlWN2zMjEBD-S9O4KYaNDnv2)

#### Exemples

Passons en revue quelques instructions détaillées pour obtenir l'installation de CentOS 7 et la configuration de base.

1. Téléchargez la dernière version [CentOS .ISO](https://www.centos.org/download/)
2. Après avoir téléchargé la dernière version de CentOS en utilisant les liens ci-dessus ou en utilisant la page de téléchargement officielle de CentOS, gravez-la sur un DVD ou créez une clé USB bootable en utilisant LiveUSB Creator appelé [Unetbootin](https://unetbootin.github.io/).
3. Après avoir créé le support d'installation bootable, placez votre DVD/USB dans le lecteur approprié de votre système, démarrez l'ordinateur, sélectionnez votre unité bootable, et la première invite CentOS 7 devrait apparaître. À l'invite, choisissez Installer CentOS 7 et appuyez sur la touche [Entrée].

![Image](https://cdn-media-1.freecodecamp.org/images/rk-uJQssZewGXgFP9sIRmUHGpHjUEIpz0ee2)

4. Le système commencera à charger l'installateur de média et un écran de bienvenue devrait apparaître. Sélectionnez la langue de votre processus d'installation — cela vous assistera tout au long de la procédure d'installation — et cliquez sur Continuer.

![Image](https://cdn-media-1.freecodecamp.org/images/21CN30c3nOpSCAb9XSlWJncObEl5fyqAIQEr)

![Image](https://cdn-media-1.freecodecamp.org/images/IIAp4gYwhWdcRvg0KP8de6Y7ivhgiZJ4SXvH)

5. À l'étape suivante, l'invite de l'écran actuel est le Résumé de l'installation. Il contient de nombreuses options pour personnaliser complètement votre système. La première chose que vous souhaitez configurer est vos paramètres de temps. Cliquez sur Date & Heure et sélectionnez l'emplacement physique de votre serveur à partir de la carte fournie, puis appuyez sur le bouton Terminé en haut pour appliquer cette configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/zPoewuybibFqlg79nqCcDjEtKE1lxAi8RqXj)

![Image](https://cdn-media-1.freecodecamp.org/images/udVF8vI0FuFqP8uFY-fXGeXIHcyVUYZcEmQg)

6. Ensuite, choisissez votre support de langue et vos paramètres de clavier. Choisissez votre langue principale et supplémentaire pour votre système, et lorsque vous avez terminé, appuyez sur Terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/GNUOD3cBf0HukL0AdEFSaslfAXDfihcOeJxt)

![Image](https://cdn-media-1.freecodecamp.org/images/0SOMnkOxnmkG4DSwnogamdTSlEOC45QFi23m)

7. De la même manière, choisissez votre disposition de clavier en appuyant sur le bouton plus et testez votre configuration de clavier en utilisant le champ de saisie de droite. Après avoir terminé la configuration de votre clavier, vous pouvez utiliser n'importe quelle combinaison de touches pour basculer entre les claviers. Dans mon cas, j'utilise Alt+Ctrl. Après avoir sélectionné votre combinaison de touches souhaitée, appuyez à nouveau sur Terminé pour appliquer les modifications et revenir à l'écran principal du Résumé de l'installation.

![Image](https://cdn-media-1.freecodecamp.org/images/YI7FkWgL8h9QTXALMgCCvqxrKgZarWNFh5gn)

![Image](https://cdn-media-1.freecodecamp.org/images/r0NDr-cIq3UyaXoa0y3qgmE7EhiMLj8DZRS4)

![Image](https://cdn-media-1.freecodecamp.org/images/yPi-j4-sjLXe4ShqPpR-bnKWwY2wO-keP5mv)

![Image](https://cdn-media-1.freecodecamp.org/images/aXcgQKMdphnhNTLzTcWWWt7B-3bduQ3b4AXm)

8. Maintenant, nous pouvons ajouter le SUPPORT DE LANGUE si vous ne souhaitez pas utiliser l'anglais. Cliquez sur « SUPPORT DE LANGUE » pour ouvrir la boîte de dialogue.

![Image](https://cdn-media-1.freecodecamp.org/images/caxBvCvaLqNJYHbuqCEnWz4SlzHcnjJWbSHN)

9. Par défaut, CentOS est livré avec la langue anglaise préinstallée, mais nous pouvons ajouter plus de langues facilement. Dans mon cas, j'ajoute l'allemand Deutsch avec Deutsch (Deutschland) comme langue supplémentaire. Appuyez sur Terminé après votre sélection.

![Image](https://cdn-media-1.freecodecamp.org/images/p69eRIErcsIn7g1AMpUQskZ2gCN2hnpzxAI5)

10. À l'étape suivante, vous pouvez personnaliser votre installation en utilisant d'autres sources d'installation que votre média local DVD/USB, telles que des emplacements réseau utilisant les protocoles HTTP, HTTPS, FTP ou NFS. Vous pouvez même ajouter des dépôts supplémentaires, mais utilisez cette méthode uniquement si vous savez ce que vous faites. Laissez donc le média d'installation auto-détecté par défaut et appuyez sur Terminé pour continuer.

![Image](https://cdn-media-1.freecodecamp.org/images/TOxIxWtUUaU6dck4gKzc2d5VPzbFaWbH7XP0)

![Image](https://cdn-media-1.freecodecamp.org/images/5SagBXBx6G402fzVKdcQgKJXJ3vRqFv9j3Rr)

11. Ensuite, vous pouvez choisir le logiciel d'installation de votre système. À cette étape, CentOS offre de nombreux environnements de plateforme serveur et bureau parmi lesquels vous pouvez choisir. Mais si vous souhaitez un haut degré de personnalisation, surtout si vous allez utiliser CentOS 7 pour fonctionner comme une plateforme serveur, alors je suggère une installation minimale avec des bibliothèques de compatibilité comme add-ons. Cela installera un logiciel système de base minimal et plus tard vous pourrez ajouter d'autres packages selon vos besoins en utilisant :

![Image](https://cdn-media-1.freecodecamp.org/images/aiPGfy0I85i73SC5EYBucyDGslreAYyBUvai)

![Image](https://cdn-media-1.freecodecamp.org/images/9VBciZwESM-gjiXOUsLz-88I7H9fLs1GghwC)

![Image](https://cdn-media-1.freecodecamp.org/images/w4QVnApDtJTm1jcMIFnQ8z-Z7ZW68jdjXMxB)

12. Il est maintenant temps de partitionner votre disque dur. Cliquez sur le menu Destination de l'installation, sélectionnez votre disque et choisissez celui que vous souhaitez. Je vais configurer le partitionnement. Lisez plus sur le partitionnement à choisir [ici](https://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-diskpartitioning-x86.html).

![Image](https://cdn-media-1.freecodecamp.org/images/enMF4gpceUHqdwSWDhP6-n0Zvyb0122RP8NQ)

![Image](https://cdn-media-1.freecodecamp.org/images/7nKmF4m-peDAaJT-pJz7F4EvKAzW1fYbHIQX)

13. À l'écran suivant, choisissez LVM (Logical Volume Manager) comme disposition de partition, puis cliquez sur Cliquez ici pour les créer automatiquement. Cette option créera trois partitions système en utilisant le système de fichiers XFS, redistribuant automatiquement l'espace de votre disque dur et regroupant tous les LVS en un grand groupe de volumes nommé « centos ». 11.

* /boot — Non LVM
* /(root) — LVM
* Swap — LVM

![Image](https://cdn-media-1.freecodecamp.org/images/N-pKNTOCYDUvsQjB7N5O8H2JV02iw08ODO93)

![Image](https://cdn-media-1.freecodecamp.org/images/U7obhodVkpI38y4oV19VUrC4WU59fYo65s2H)

14. Si vous n'êtes pas satisfait de la disposition de partition par défaut créée automatiquement par l'installateur, vous pouvez ajouter, modifier ou redimensionner complètement votre schéma de partition. Lorsque vous avez terminé, appuyez sur le bouton Terminé et Accepter les modifications dans l'invite Résumé des modifications.

![Image](https://cdn-media-1.freecodecamp.org/images/fyZ3sVKHOs8pN77NHqcRDfwpYpuyyF4xlzsJ)

NOTE : Pour les utilisateurs qui ont des disques durs de plus de 2 To, l'installateur convertira automatiquement la table de partition en GPT. Mais si vous souhaitez utiliser la table GPT sur des disques plus petits que 2 To, vous devez utiliser l'argument inst.gpt dans la ligne de commande de démarrage de l'installateur afin de changer le comportement par défaut.

15. L'étape suivante consiste à définir le nom d'hôte de votre système et à activer la mise en réseau. Cliquez sur l'étiquette Réseau & Nom d'hôte et tapez le FQDN (Nom de domaine complet) de votre système dans le champ Nom d'hôte, puis activez votre interface réseau en basculant le bouton Ethernet supérieur sur ON. Si vous avez un serveur DHCP fonctionnel sur votre réseau, il configurera automatiquement tous vos paramètres réseau pour la NIC activée, qui devrait apparaître sous votre interface active.

![Image](https://cdn-media-1.freecodecamp.org/images/aJaSFWrR0OhcclQfctFmPeShvAb4CrK-yJfO)

![Image](https://cdn-media-1.freecodecamp.org/images/6JGzTjzo0weuiVyPoGWOYzRRsh1Rl6C5GcHF)

16. Si votre système est un serveur, il est préférable de définir une configuration réseau statique sur la NIC Ethernet en cliquant sur le bouton Configurer et en ajoutant tous vos paramètres d'interface statique comme dans la capture d'écran ci-dessous. Lorsque vous avez terminé, appuyez sur Enregistrer, désactivez et activez la carte Ethernet en basculant le bouton sur OFF et ON, puis appuyez sur Terminé pour appliquer les paramètres et revenir au menu principal.

Sinon :

![Image](https://cdn-media-1.freecodecamp.org/images/LSvNkE3Tc2i7Fa2q1DDT6YCtJ3C0WQpEam8G)

![Image](https://cdn-media-1.freecodecamp.org/images/j44d6AGcV6OTDbjZOMx8MY8eFGVt4c5QDYOp)

![Image](https://cdn-media-1.freecodecamp.org/images/xNSaSz1Fe3lQ9dZHBqTha5Y4kciBIxVDs7R2)

17. Ajoutez les entrées pour l'adresse, le masque de réseau et la passerelle selon votre environnement IP statique. Dans mon cas, j'utilise l'adresse 192.168.1.100, le masque de réseau 255.255.255.0, la passerelle 192.168.1.1 et les serveurs DNS 8.8.8.8 8.8.4.4. Ces valeurs peuvent varier selon votre environnement réseau. Après cela, appuyez sur Enregistrer.

IMPORTANT : Si vous n'avez pas de connexion Internet IPv6, définissez IPv6 de auto à ignorer dans l'onglet IPv6. Sinon, vous ne pourrez pas atteindre Internet depuis ce serveur en IPv4, car CentOS semble ignorer la configuration IPv4 correcte et utilise IPv6 à la place, ce qui échoue.

![Image](https://cdn-media-1.freecodecamp.org/images/zIVn34DFeRZBICltiKeJ6ZoLae4c2pN45Xdp)

18. Ensuite, nous devons activer la connexion comme montré dans la capture d'écran ci-dessous. Après, appuyez sur Terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/ZnGNcnOiXpdvvpMya2dRhJ4CaOY8pSRYLnaJ)

19. Il est maintenant temps de commencer le processus d'installation en choisissant Débuter l'installation et en définissant un mot de passe fort pour le compte root.

![Image](https://cdn-media-1.freecodecamp.org/images/ea3kScov6z01BRxr4jOLM4NRJccCxUS3EDqN)

20. Le processus d'installation va maintenant commencer et vous obtiendrez une petite barre de progression bleue dans les fenêtres suivantes. Maintenant, nous devons définir le MOT DE PASSE ROOT et ajouter un nouvel utilisateur non-root dans l'option CRÉATION D'UTILISATEUR. Je vais d'abord opter pour le mot de passe root.

![Image](https://cdn-media-1.freecodecamp.org/images/c5h9dW9aqyasoNX9aDwfInjkU5xnPGq4QAu2)

21. Entrez un mot de passe sécurisé de votre choix et appuyez sur Terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/2Ky7QzNMLccBT5QPLSqGbav50VsK3cH4JmBI)

22. Ensuite, nous allons procéder à la CRÉATION D'UTILISATEUR.

![Image](https://cdn-media-1.freecodecamp.org/images/GeveORGJo-scuJeD1Z25sxVDSeNNeAN7Npr-)

23. Ensuite, je vais créer un utilisateur. Dans mon cas, j'ai utilisé le nom complet « Administrateur » et le nom d'utilisateur « administrateur ». Cochez l'option Exiger le mot de passe pour utiliser ce compte, puis appuyez sur Terminé. Bien sûr, vous pouvez utiliser n'importe quelle valeur selon votre choix.

![Image](https://cdn-media-1.freecodecamp.org/images/3sGgDLaj28eqO4yvWYHgANUkwZn-kXz10LmY)

24. Appuyez sur Terminer. Ayez de la patience et attendez la fin de la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/n8Qxnk5BdvJRkM6sntmR62uC4eV8GiNK7dFk)

25. Après la fin de l'installation, il vous demandera de redémarrer le serveur, appuyez simplement sur Terminer la configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/rTWWi5rPGgTBBjTN8vI6uInYwTqD9nhcb2Yy)

26. Le serveur redémarre et demandera votre nom d'utilisateur et votre mot de passe par la suite.

![Image](https://cdn-media-1.freecodecamp.org/images/yQwZNdAYh2gDJ3cxbDzEiVFGQYnzz412Q3j8)

Félicitations ! Vous avez maintenant installé la dernière version de CentOS sur votre nouvelle machine. Retirez tout support d'installation et redémarrez votre ordinateur afin de pouvoir vous connecter à votre nouvel environnement CentOS 7 minimal et effectuer d'autres tâches système, telles que la mise à jour de votre système et l'installation d'autres logiciels utiles nécessaires pour exécuter les tâches quotidiennes.

Nous sommes maintenant prêts à nous connecter avec l'utilisateur que nous venons de créer ci-dessus ou nous pouvons utiliser les identifiants root.

Première connexion sur CentOS. Connectez-vous en tant qu'utilisateur root au serveur afin que nous puissions effectuer quelques étapes d'installation finales.

La première consiste à installer toutes les mises à jour disponibles avec yum.

![Image](https://cdn-media-1.freecodecamp.org/images/yjaMZ33oDpbtjB21GtAnE-yh3GHkhHuZsEOp)

Confirmez avec « y » pour procéder à l'installation des mises à jour. Je vais installer deux éditeurs de ligne de commande pour pouvoir éditer les fichiers de configuration sur le shell :

![Image](https://cdn-media-1.freecodecamp.org/images/eRLKdk7Ha3KRU3fgjZF847V9wIiHhxTpXqnO)

#### Configuration réseau

CentOS 7.2 minimal n'est pas livré avec la commande ifconfig préinstallée, nous allons donc l'installer comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/slhBMQEUoqGJkgEDUQOW-3rxa3WZCA7PD-V3)

Si vous souhaitez modifier ou voir le fichier de configuration réseau, éditez simplement le fichier :

![Image](https://cdn-media-1.freecodecamp.org/images/OliVYcSJvGNYWk9mDB5zqtMExcggQG5SqzbM)

Il sera comme ceci lorsque vous aurez configuré une adresse IP statique :

![Image](https://cdn-media-1.freecodecamp.org/images/pofxOfE9lJnMwr4nIKs0AOyORp4k-r1eUMBI)

![Image](https://cdn-media-1.freecodecamp.org/images/CNjWloceJVc8vHVn9BaiqeZ5c1hEhoYw7WuN)

Modifiez les valeurs si nécessaire.

Note : Le nom de l'appareil ci-dessus peut varier, veuillez donc vérifier le fichier équivalent dans le répertoire /etc/sysconfig/network-scripts.

#### Ajuster /etc/hosts

Ajustez le fichier /etc/hosts comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/9f52fds4U3nqAdcQtDp5tv98MDuQ6nm09m3q)

Faites en sorte que les valeurs soient comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/4G8Ve0NTRP1Jx6fVcVNx6a7HGIGRiAVK02Hm)

Félicitations ! Nous avons maintenant une configuration de serveur CentOS 7 de base minimale.

Vous préférerez peut-être utiliser une interface graphique, voici une variété de saveurs parmi lesquelles vous pouvez choisir :

#### Installation de GNOME-Desktop :

Installez l'environnement de bureau GNOME en entrant ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/8xrxZk0240pPvx-yslBxJXZih9jrhfOPaksU)

Pour démarrer l'interface graphique, entrez après avoir terminé l'installation :

![Image](https://cdn-media-1.freecodecamp.org/images/cZPdsALzVpA5DYKoToQ2lgMG7FDBftKHJgGY)

![Image](https://cdn-media-1.freecodecamp.org/images/8O5W1tTbW4-caJbSU9qQxqIM5RaUfugFt6BJ)

#### Comment utiliser GNOME Shell

Le bureau GNOME par défaut de CentOS 7 démarre en mode classique, mais si vous souhaitez utiliser GNOME Shell, définissez-le comme suit :

Option A : Si vous démarrez GNOME avec **startx**, définissez-le comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/UGFEuBeOA5TeYZZlPE-E2iOZBJmXvjjrfFYn)

Option B : définissez le système de connexion graphique systemctl set-default graphical.target et redémarrez le système. Après le démarrage du système :

1. Cliquez sur le bouton qui est situé à côté du bouton « Sign In ».
2. Sélectionnez « GNOME » dans la liste. (Le défaut est GNOME Classic)
3. Cliquez sur « Sign In » et connectez-vous avec GNOME Shell.

![Image](https://cdn-media-1.freecodecamp.org/images/N2icRiFgBxnYEXUUu8cHdfVTGPo-yGzHhlAU)

GNOME shell démarre comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/oiqDsqZuANvGUG2XEpJU8M9LJbaEhfBTcrAV)

#### Installation de KDE-Desktop :

Installez l'environnement de bureau KDE en entrant

![Image](https://cdn-media-1.freecodecamp.org/images/8EKvkfyxykrD7ESdx-NTZqLn1-XoAHUxqB0t)

Entrez une commande comme ci-dessous après avoir terminé l'installation :

![Image](https://cdn-media-1.freecodecamp.org/images/BM7BB8s7TzICeeeYJyhw9H2XeBU5BmXcEAfb)

L'environnement de bureau KDE démarre comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vLim8XR1-vl7DP2Nzbk7GPe34X7PNLjx4KcR)

#### Installation de l'environnement de bureau MATE :

Installez l'environnement de bureau MATE en entrant ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/KQGWjK2f5QL-ESkHT71foneUyytOZgC76THw)

Entrez une commande comme ci-dessous après avoir terminé l'installation :

![Image](https://cdn-media-1.freecodecamp.org/images/S-9RT00AC-D0EyVaqdsQMYbH9G1CMKf5imSZ)

L'environnement de bureau MATE démarre :

![Image](https://cdn-media-1.freecodecamp.org/images/6bLYOa7ktDIkJ5-nJ7BK9mQifjizzOZK47ir)

#### Installation de l'environnement de bureau Xfce :

Installez l'environnement de bureau Xfce en entrant ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/eajRi-cVLawzVkihC8nTDZNGXKjdEISEnn6Y)

Entrez une commande comme ci-dessous après avoir terminé l'installation :

![Image](https://cdn-media-1.freecodecamp.org/images/nvqLmB2PqwYamPW3KOfIRf4mIKvohyGzwbgv)

L'environnement de bureau Xfce démarre comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/3916tM9oz0pGpYNGX5H1EfjvA93F4aSQ33qf)

#### AUTRE FAÇON DE LE FAIRE :

Plutôt que d'utiliser le piratage d'une commande startx dans un fichier .xinitrc, il est probablement préférable de dire à Systemd que vous souhaitez démarrer dans une interface graphique GUI plutôt que dans le terminal.

Pour accomplir cela, faites simplement ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/clCHZwiwW12IxLg8F-1eV8MMpwww250wx8Fn)

Ensuite, redémarrez simplement.

La dernière partie associera le niveau d'exécution 5 comme cible par défaut par rapport à Systemd.

#### Le faire avec Systemd

Vous pouvez également utiliser Systemd pour accomplir cela. C'est probablement la meilleure méthode, puisque vous gérez l'état du système directement via Systemd et ses CLIs.

Vous pouvez voir quelle est votre cible par défaut actuelle :

![Image](https://cdn-media-1.freecodecamp.org/images/GAMQwC7zZTIyvWWjnOwCxOBII0f9ZJFo6NpV)

Puis changez-la en graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/MRK-LDaeKfDAPHrq1UiP3aG6USYtZYMp0c8Z)

![Image](https://cdn-media-1.freecodecamp.org/images/Q3WkBqFK0D7pAQCU0Kzure2BqDw5cSoA24tC)

#### Cibles

Dans Systemd, les cibles runlevel5.target et graphical.target sont identiques. Il en va de même pour runlevel2.target et multi-user.target.

![Image](https://cdn-media-1.freecodecamp.org/images/04fnoUaIaChUTVk1gI5bpdWueeHe9j6Z4AZx)

#### RHEL / CentOS Linux Install Core Development Tools Automake, Gcc (C/C++), Perl, Python & Debuggers

Q. Comment installer tous les outils de développement tels que les compilateurs GNU GCC C/C++, make et autres, après avoir installé CentOS ou RHEL ou Fedora Linux à partir d'une invite de shell ?

Vous devez installer le groupe 'Development Tools' sur RHEL/CentOS/Fedora/Scientific/Red Hat Enterprise Linux. Ces outils incluent les outils de développement de base tels que automake, gcc, perl, python et les débogueurs qui sont nécessaires pour compiler des logiciels et construire de nouveaux rpms :

1. flex
2. gcc c/c++ compiler
3. redhat-rpm-config
4. strace
5. rpm-build
6. make
7. pkgconfig
8. gettext
9. automake
10. strace64
11. gdb
12. bison
13. libtool
14. autoconf
15. gcc-c++ compiler
16. binutils et toutes les dépendances.

#### Installation :

Ouvrez le terminal ou connectez-vous via une session ssh et tapez la commande suivante en tant qu'utilisateur root :

![Image](https://cdn-media-1.freecodecamp.org/images/FBV3oXITAW4NDKmUlCSnqKRHkrpFxOsywEOa)

Exemples de sorties qui suivent :

![Image](https://cdn-media-1.freecodecamp.org/images/eJlL3KG2asfbT7-KjJODLskpBeLTsgNbcCRt)

Maintenant, vous pouvez compiler et utiliser n'importe quelle application sur votre système.

#### **Vérification de l'installation**

Pour afficher la version du compilateur Gnu gcc/c/c++, tapez :

![Image](https://cdn-media-1.freecodecamp.org/images/gCh9plzh1fFHqRAxIN41R2Z024dgm-3uUICK)

Exemples de sorties :

![Image](https://cdn-media-1.freecodecamp.org/images/f3COT3u-Xb8zvgnrNGVvH-7rpiPqZenBdivq)

#### Comment lister tous les services en cours d'exécution sur un serveur Fedora / RHEL / CentOS Linux ?

Il existe diverses façons et outils pour trouver et lister tous les services en cours d'exécution sous les systèmes Fedora / RHEL / CentOS Linux.

![Image](https://cdn-media-1.freecodecamp.org/images/sR1j7IEftLUJcf3l8eA09lFf4QuW31Na3dbE)

La syntaxe est la suivante pour CentOS/RHEL 6.x et versions antérieures (pré-systemd) :

![Image](https://cdn-media-1.freecodecamp.org/images/34duN-gDwYU8Voox68o0OWpyO0lcROokMeN6)

Imprimer le statut de n'importe quel service. Pour imprimer le statut du service apache (httpd) :

![Image](https://cdn-media-1.freecodecamp.org/images/hrg5zAjTRW789CRAM0kLPpoEdJi4VCqdf2re)

Lister tous les services connus (configurés via SysV) :

![Image](https://cdn-media-1.freecodecamp.org/images/zdMHiLpBgWw-7wcHU4rtNePnTWydgPGwNVSY)

Lister les services et leurs ports ouverts :

![Image](https://cdn-media-1.freecodecamp.org/images/ONlXfdtpMuQThom-1TXCwogvZLW-CxvJsZSu)

Activer/désactiver le service :

![Image](https://cdn-media-1.freecodecamp.org/images/9zwxQTHcBo1W4-bYkTdLRYkRqlxbgiwH30Fo)

**ntsysv** est une interface simple pour configurer les services de niveau d'exécution qui sont également configurables via **chkconfig**. Par défaut, il configure le niveau d'exécution actuel. Il suffit de taper **ntsysv** et de sélectionner le service que vous souhaitez exécuter.

#### Une note sur RHEL/CentOS 7.x avec systemd

Si vous utilisez une distribution basée sur systemd telle que Fedora Linux v22/23/24 ou RHEL/CentOS Linux 7.x+, essayez la commande suivante pour lister les services en cours d'exécution en utilisant la commande systemctl. Elle contrôle le système systemd et le gestionnaire de services.

Pour lister les services systemd sur CentOS/RHEL 7.x+, utilisez ce qui suit.

La syntaxe est :

![Image](https://cdn-media-1.freecodecamp.org/images/HMgfPY4TiCQZt5VqkAeVnOA6wzKA0tHb7fnM)

Pour lister tous les services :

![Image](https://cdn-media-1.freecodecamp.org/images/4X-Q7tJMtViVrTXOg1118N4RQSxK8fIIsG8q)

Exemples de sorties :

![Image](https://cdn-media-1.freecodecamp.org/images/8HHdKMxQvr1tP9gfoT3K602qrD3FkQ-RpAU2)

L'image ci-dessus montre la liste de toutes les unités installées sur le système CentOS/RHEL 7 basé sur systemd, ainsi que leurs états actuels.

Pour afficher les processus associés à un service particulier (cgroup), vous pouvez utiliser la commande systemd-cgtop. Comme la commande top, systemd-cgtop liste les processus en cours d'exécution en fonction de leurs services :

![Image](https://cdn-media-1.freecodecamp.org/images/cnQkMU558eEjH4IQ7NY546voU0Q079Aj5iOp)

Exemples de sorties :

![Image](https://cdn-media-1.freecodecamp.org/images/vOiJ6B9pCEt3sT5CrOGbkiIGf5UoSdQ7xv42)

Pour lister uniquement les services SysV sur CentOS/RHEL 7.x+ (n'inclut pas les services systemd natifs) :

![Image](https://cdn-media-1.freecodecamp.org/images/C6mSxcdwt6RdEjfLwbP0XmdjJBv7UrKEjr33)

Exemples de sorties :

![Image](https://cdn-media-1.freecodecamp.org/images/psYt44SaI963eoYVsBCFSCEFGyERv4H3V2nC)

#### CONFIGURATION DU PARE-FEU :

Apprenez à configurer le pare-feu [ici](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-oncentos-7).

**Références**

* [Documentation CentOS](https://wiki.centos.org/Documentation)
* [Notes de version de CentOS](https://wiki.centos.org/Manuals/ReleaseNotes/CentOS7)
* [Installer Gnome GUI sur CentOS 7 / RHEL 7](https://linuxconfig.org/how-to-install-gui-gnome-on-centos-7-linux-system)
* [Travailler avec les cibles SYSTEMD](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-targets)

**Guide de documentation pour CentOS**

[Version 7 de CentOS](https://docs.centos.org/en-US/docs/)

CentOS 7 est entièrement basé sur la documentation détaillée de RedHat. Des exemples et des guides d'administration système sont disponibles ici : [Documentation complète de CentOS 7](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/)

[_Publié à l'origine par Krasimir Vatchinsky dans la documentation archivée de Stack Overflow — RIP Tutorial_](https://riptutorial.com/centos/topic/7640/getting-started-with-centos)