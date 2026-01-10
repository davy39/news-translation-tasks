---
title: Vérifier la température de votre CPU en utilisant Python (et autres astuces
  sympas)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-03T17:12:17.000Z'
originalURL: https://freecodecamp.org/news/using-psutil-in-python-8623d9fac8dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gx9zzO6SmaEn8btnqGxhGw.png
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Vérifier la température de votre CPU en utilisant Python (et autres astuces
  sympas)
seo_desc: 'By Ori Roza

  Python’s psutil module provides an interface with all the PC resources and processes.

  This module is very helpful whether we want to get some data on a specific resource
  or manage a resource according to its state.

  In this article, I will...'
---

Par Ori Roza

Le module [psutil](https://psutil.readthedocs.io/en/latest/) de Python fournit une interface avec toutes les ressources et processus du PC.

Ce module est très utile que ce soit pour obtenir des données sur une ressource spécifique ou pour gérer une ressource en fonction de son état.

Dans cet article, je vais vous montrer les principales fonctionnalités de ce module et comment les utiliser.

### **Obtenir des informations sur les ressources du PC**

Voyons comment nous pouvons obtenir des informations sur l'état actuel du système de notre PC.

Nous pouvons obtenir des informations sur le CPU depuis le démarrage, y compris le nombre d'[appels système](https://www.geeksforgeeks.org/operating-system-introduction-system-call/) et de [changements de contexte](http://www.linfo.org/context_switch.html) qu'il a effectués :

```
In [1]: psutil.cpu_stats()Out[1]: scpustats(ctx_switches=437905181,interrupts=2222556355L,soft_interrupts=0,syscalls=109468308)
```

Nous pouvons obtenir des informations sur l'état du disque et de la mémoire :

```
In [1]: psutil.disk_usage("c:")Out[1]: sdiskusage(total=127950385152L,                   used=116934914048L,                   free=11015471104L,                   percent=91.4)
```

```
In [2]: psutil.virtual_memory()Out[2]: svmem(total=8488030208L,              available=3647520768L,              percent=57.0,              used=4840509440L,              free=3647520768L)
```

Nous pouvons même obtenir des informations physiques comme le nombre de secondes de batterie restantes ou la température actuelle du CPU :

```
In [1]: psutil.sensors_battery()Out[1]: sbattery(percent=77, secsleft=18305, power_plugged=False)
```

```
In [2]: psutil.sensors_temperatures() # En CelsiusOut[2]: {'ACPI\\ThermalZone\\THM0_0':         [shwtemp(label='',          current=49.05000000000001,          high=127.05000000000001,          critical=127.05000000000001)]}
```

### **Obtenir des informations sur les processus**

L'une des fonctionnalités les plus puissantes que ce module nous offre est la classe "Process". Nous pouvons accéder aux ressources et statistiques de chaque processus et réagir en conséquence.

(Certains processus nécessitent des privilèges admin ou système, donc après avoir tenté d'accéder à leur instance, cela échouera avec une erreur "AccessDenied".)

Vérifions cette fonctionnalité.

Tout d'abord, nous créons une instance en donnant l'ID du processus souhaité :

```
In [1]: p = psutil.Process(9800)
```

Ensuite, nous pouvons accéder à toutes les informations et statistiques du processus :

```
In [1]: p.exe()Out[1]: 'C:\\Windows\\System32\\dllhost.exe'
```

```
In [2]: p.cpu_percent()Out[2]: 0.0
```

```
In [3]: p.cwd()Out[3]: 'C:\\WINDOWS\\system32'
```

Créons une fonction qui lie les ports de connexion ouverts aux processus.

Tout d'abord, nous devons itérer sur toutes les connexions ouvertes. `ps.net_connections` est exactement ce dont nous avons besoin !

```
In [1]: ps.net_connections?Signature: ps.net_connections(kind='inet')Docstring:Return system-wide socket connections as a list of(fd, family, type, laddr, raddr, status, pid) namedtuples.In case of limited privileges 'fd' and 'pid' may be set to -1and None respectively.The *kind* parameter filters for connections that fit thefollowing criteria:
```

```
+------------+----------------------------------------------------+| Kind Value | Connections using                                  |+------------+----------------------------------------------------+| inet       | IPv4 et IPv6                                      || inet4      | IPv4                                               || inet6      | IPv6                                               || tcp        | TCP                                                || tcp4       | TCP sur IPv4                                      || tcp6       | TCP sur IPv6                                      || udp        | UDP                                                || udp4       | UDP sur IPv4                                      || udp6       | UDP sur IPv6                                      || unix       | Socket UNIX (protocoles UDP et TCP)               || all        | la somme de toutes les familles et protocoles possibles |+------------+----------------------------------------------------+
```

Nous pouvons voir que l'un des attributs que net_connections retourne est "pid".

Nous pouvons lier cela à un nom de processus :

```
In [1]: def link_connection_to_process():    ...:     for connection in ps.net_connections():    ...:         try:    ...:             yield [ps.Process(pid=connection.pid).name(),    ...:                   connection]    ...:         except ps.AccessDenied:    ...:             continue # Continuer si nous n'avons pas accès
```

Nous devons nous souvenir que, sauf si nous avons des privilèges root, nous ne pouvons pas accéder à certains processus. Par conséquent, nous devons l'envelopper dans un bloc try-catch pour gérer une erreur "AccessDenied".

Vérifions la sortie.

Cela va sortir beaucoup de données, alors imprimons le premier membre :

```
In [1]: for proc_to_con in ps.net_connections():    ...:     print proc_to_con    ...:     raw_input("...")    ...:['ManagementServer.exe', sconn(fd=-1, family=2, type=1, laddr=addr(ip='127.0.0.1', port=5905), raddr=addr(ip='127.0.0.1', port=49728), status='ESTABLISHED', pid=5224)]...
```

Comme nous pouvons le voir, le premier membre est le nom du processus et le second est les données de connexion : adresse IP, port, statut, etc.

Cette fonction est très utile pour explorer quels ports sont utilisés par chaque processus.

Nous avons tous déjà eu l'erreur "Cette adresse est déjà utilisée", n'est-ce pas ?

### Conclusion

Le module psutil est une excellente bibliothèque pour la gestion du système. Il est utile pour gérer les ressources dans le cadre d'un flux de code.

J'espère que cet article vous a appris quelque chose de nouveau, et j'attends avec impatience vos retours. Veuillez me dire — était-ce utile pour vous ?