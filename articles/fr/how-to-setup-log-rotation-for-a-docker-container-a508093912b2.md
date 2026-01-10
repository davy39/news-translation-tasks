---
title: Comment configurer la rotation des logs pour un conteneur Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T22:50:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-log-rotation-for-a-docker-container-a508093912b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_q2gpmanaKPIhoScKtgt1Q.png
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment configurer la rotation des logs pour un conteneur Docker
seo_desc: 'By Ying Kit Yuen

  We all need logs!

  Sometimes working with Docker makes me feel like I’m working with a black box. Especially
  when I’m playing with Docker images from the community, and it doesn’t go the way
  I expected. In many cases, reading logs tak...'
---

Par Ying Kit Yuen

#### Nous avons tous besoin de logs !

Parfois, travailler avec [Docker](https://www.docker.com/) me donne l'impression de travailler avec une boîte noire. Surtout lorsque je manipule des images Docker de la communauté, et que cela ne se passe pas comme prévu. Dans de nombreux cas, la lecture des logs prend une grande partie du temps lors du débogage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PdclvVxyj07MQ_Fn8nJPYw.jpeg)

Cet article traite de la configuration de la rotation des logs pour les conteneurs Docker.

### Le pilote de journalisation par défaut

Nous pouvons configurer différents pilotes de journalisation pour les conteneurs. Par défaut, les flux **stdout** et **stderr** du conteneur sont écrits dans un fichier JSON situé dans _/var/lib/docker/containers/[container-id]/[container-id]-json.log_. Si vous le laissez sans surveillance, il peut occuper une grande quantité d'espace disque, comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2e9iGLyDCm5_WNfxl0_KAQ.jpeg)
_Un grand fichier de log au format json_

#### Purger le log manuellement

Si ce fichier de log JSON occupe une partie importante du disque, nous pouvons le purger en utilisant la commande suivante.

Nous pourrions configurer un cronjob pour purger régulièrement ces fichiers de log JSON. Mais à long terme, il serait préférable de configurer la rotation des logs.

### Configurer la rotation des logs

#### Configurer le pilote de journalisation par défaut

Cela peut être fait en ajoutant les valeurs suivantes dans _/etc/docker/daemon.json_. Créez ce fichier s'il n'existe pas.

Le pilote de journalisation _json-file_ a quelques options supplémentaires, et nous pouvons même changer pour d'autres pilotes de journalisation tels que _syslog_. Pour plus d'informations, veuillez consulter la [Documentation Docker — Configurer les pilotes de journalisation](https://docs.docker.com/config/containers/logging/configure/).

Exécutez les commandes suivantes pour recharger le fichier _daemon.json_ mis à jour. La nouvelle configuration s'appliquera à tous les nouveaux conteneurs créés après le redémarrage.

#### Configurer le pilote de journalisation pour un conteneur

La configuration peut également être effectuée au niveau du conteneur si vous ne souhaitez pas l'appliquer globalement.

**La commande docker run**

Nous pouvons spécifier le pilote de journalisation et les options dans la commande _docker run_. Par exemple :

**Utilisation de docker-compose**

Le pilote de journalisation et les options peuvent également être configurés en utilisant docker-compose. Par exemple :

Vérifiez si la configuration fonctionne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Pl6ERkWFB4HBZ9fVNvtsw.jpeg)
_Les logs sont divisés en fichiers de 1k_

### Résumé

Bien que les paramètres par défaut fonctionnent bien, on ne sait jamais quand les logs du conteneur occupent tout l'espace disque. Cela peut être évité par les quelques étapes discutées ci-dessus. Autre que cela, les logs sont un actif important. Ils ne sont pas seulement utiles lorsque quelque chose ne va pas, mais ils contiennent également beaucoup de valeur cachée. Alors, ne laissez jamais les logs s'échapper.

Si vous cherchez une **solution SAAS de gestion des logs**, envisagez d'utiliser [Boatswain](https://boatswain.io/). Nous vous aiderons à gérer tous les logs et à surveiller vos serveurs [Docker](https://www.docker.com/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*wU51pWBThLTG2ngSYcE7lA.jpeg)
_Des faits insuffisants invitent toujours le danger_

— Originalement publié sur [Boatswain Blog](https://blog.boatswain.io/post/docker-container-log-rotation/).