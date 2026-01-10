---
title: Nettoyer Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T17:31:37.000Z'
originalURL: https://freecodecamp.org/news/cleaning-up-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_C6BkVKRpoVK_Pq1TLqlSkQ-3.png
tags:
- name: command line
  slug: command-line
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: Tutorial
  slug: tutorial
seo_title: Nettoyer Docker
seo_desc: 'By Faizan Bashir

  With the passage of time running Docker in development, we tend to accumulate a
  lot of unused images. Sometimes for testing, research or just trying out fun new
  stuff. It''s always cool to run new software in containers, lights up new...'
---

Par Faizan Bashir

Avec le temps, en utilisant Docker dans le développement, nous avons tendance à accumuler beaucoup d'images inutilisées. Parfois pour des tests, des recherches ou simplement pour essayer de nouvelles choses amusantes. C'est toujours génial d'exécuter de nouveaux logiciels dans des conteneurs, cela ouvre de nouvelles possibilités pour ceux d'entre nous qui sont intéressés à apprendre constamment de nouvelles technologies. L'inconvénient est qu'une grande partie de la mémoire SSD précieuse est occupée par des images rarement utilisées ou inutilisées, et le pire, c'est que nous le remarquons à peine. Mais les gars chez Docker Inc. ont fait un excellent travail en gardant une trace de toutes les choses Docker.

Dites bonjour à la commande `system`, qui fait partie des commandes de gestion de Docker et qui est tout simplement géniale. La commande `system` fournit des informations allant de l'utilisation du disque à des informations système, n'est-ce pas génial ?

### **Utilisation du disque avec la commande** `df`

```
$ docker system df
```

Retourne quelque chose comme ceci,

```
TYPE              TOTAL     ACTIVE     SIZE         RECLAIMABLE
Images            35        6          8.332GB      7.364GB (88%)
Containers        12        12         417.6MB      0B (0%)
Local Volumes     67        2          2.828GB      2.828GB (100%)
Build Cache                            0B           0B
```

Remarquez le `Reclaimable`, c'est la taille que vous pouvez récupérer, elle est calculée en soustrayant la taille des images actives de la taille des images totales.

---

**Événements en temps réel avec la commande** `events`

```
$ docker system events
```

Retourne la liste des événements en temps réel depuis le serveur, basés sur les types d'objets Docker.

Formater la sortie

```
--format 'Type={{.Type}}  Status={{.Status}}  ID={{.ID}}'
```

ou simplement formater la sortie en JSON

```
$ docker system events --format '{{json .}}'
```

---

**Informations système avec la commande** `info`

Une autre commande géniale pour obtenir toutes les informations liées au système est la commande `info`. Vous serez surpris de voir la quantité d'informations que vous pouvez obtenir.

```
$ docker system info
```

---

**Supprimer les données inutilisées avec la commande** `prune`

Maintenant que nous avons toutes les informations dont nous avons besoin, c'est l'heure du nettoyage, mais attention à ne pas utiliser cette commande à moitié endormi.

```
$ docker system prune
WARNING! This will remove:        
	- all stopped containers        
        - all networks not used by at least one container        
        - all dangling images        
        - all build cache
Are you sure you want to continue? [y/N]
```

De plus, nous pouvons supprimer exactement ce que nous voulons, en utilisant l'une des commandes suivantes, régalez-vous mesdames et messieurs.

```
$ docker system prune -a --volumes
$ docker image prune
$ docker container prune
$ docker volume prune
$ docker network prune
```

Toutes les commandes ci-dessus demanderont une confirmation, alors lavez-vous le visage avec de l'eau froide ou prenez un shot d'Espresso avant d'exécuter l'une de ces commandes ;).