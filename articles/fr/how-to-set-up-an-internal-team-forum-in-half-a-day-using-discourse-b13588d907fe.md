---
title: Comment configurer un forum d'équipe interne en une demi-journée avec Discourse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-12T15:34:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-an-internal-team-forum-in-half-a-day-using-discourse-b13588d907fe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*chgxuE38EYBS5anj2E49LQ.png
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment configurer un forum d'équipe interne en une demi-journée avec Discourse
seo_desc: 'By Ben Cheng

  TL;DR: I’ve deployed Discourse on Kubernetes (K8s) for my company’s internal discussion
  platform. Because I couldn’t find a simple tutorial, I documented my steps to help
  other developers do it too.

  Why would I want to deploy Discourse o...'
---

Par Ben Cheng

**TL;DR :** J'ai déployé [Discourse](https://www.discourse.org/) sur [Kubernetes (K8s)](https://kubernetes.io/) pour la plateforme de discussion interne de [mon entreprise](http://oursky.com). Comme je n'ai pas trouvé de tutoriel simple, j'ai documenté mes étapes pour aider d'autres développeurs à le faire aussi.

### Pourquoi voudrais-je déployer Discourse sur Kubernetes ?

1. Notre entreprise a déjà un cluster Kubernetes pour des outils aléatoires et des déploiements de staging, donc il est moins cher de déployer sur le cluster existant pour une utilisation interne de Discourse.
2. En tant que fondateur, je n'ai plus beaucoup d'occasions de coder. Je voulais apprendre à utiliser Kubernetes car mon équipe l'a beaucoup utilisé récemment.

### Un aperçu rapide de ce tutoriel

Le tutoriel et la configuration d'exemple ci-dessous **montrent comment déployer un seul serveur web Discourse**. Ce serveur doit se connecter à un serveur **PostgreSQL** et **Redis**. Nous utilisons **Google Cloud Registry** et `[gcePersistentDisk](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)` pour le stockage.  
   
Alors commençons :

#### Créer une image Docker de l'application Discourse

Nous allons "détourner" le lanceur fourni par `discourse_docker` pour créer l'image Docker pour le serveur web Discourse. Et par "détourner", je veux dire que nous avons surutilisé le script de lanceur pour créer des images Docker pour une utilisation en production.

1. Clonez depuis [https://github.com/discourse/discourse_docker](https://github.com/discourse/discourse_docker) vers votre environnement local.

2. Configurez un serveur [Redis](https://redis.io/topics/quickstart) temporaire et une base de données [PostgresSQL](https://www.postgresql.org/download/) dans l'environnement local.

3. Créez un fichier `containers/web_only.yml` (comme montré ci-dessous)

* La variable d'environnement n'est pas pertinente pour K8s. Elle est juste pour construire l'image locale, alors remplissez avec quelque chose qui fonctionne pour votre environnement local.
* Déterminez les plugins que vous voulez installer avec votre configuration Discourse ici.

4. **Astuce** : Les instances locales de Redis peuvent être en mode protégé et n'autoriseront pas un invité Docker à héberger la connexion. Dans ce cas, vous devriez démarrer votre serveur Redis avec le mode protégé désactivé : `redis-server --protected-mode no`

5. Créez les images Docker et téléchargez les images vers votre registre Docker K8s. Dans ce cas, nous utilisons Google Cloud Registry :

* Créez une image Docker avec le lanceur de Discourse : `./launcher bootstrap web_only`
* Vérifiez que l'image est créée : `docker images`. Vous devriez voir l'image Discourse dans la liste si c'est un succès.
* Téléchargez l'image vers le registre avec cette commande :

Configuration d'exemple dans `web_only.yml` :

#### Maintenant, nous sommes prêts à déployer sur K8s

**1. Préparer un volume persistant**

Nous aurons besoin d'un volume persistant comme base de données pour stocker les informations utilisateur et les éléments de discussion. Nous utilisons [GCEPersistentDisk](https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk) pour le disque persistant sur le cluster K8s. Maintenant, créons deux disques de 10 Go pour l'application et la base de données respectivement. Vous pouvez ajuster la taille du disque en fonction de votre utilisation de Discourse.

**2. Déployer sur Kubernetes**

Ensuite, nous allons configurer les paramètres de déploiement du cloud K8s. Personnalisez le fichier K8s d'exemple. Voici quelques variables que vous voudrez probablement ajuster :

`volumes.yaml`

* Pour les deux volumes persistants :   
- metadata.name   
- spec.capacity.storage   
- spec.gcePersistentDisk.pdName (pour le nom du disque persistant ci-dessus)   
- spec.claimRef.namespace (pour le namespace que vous utilisez dans K8s)
* Le fichier d'exemple ici suppose que vous utilisez `gcePersistentDisk`. volumes.yaml doit être fortement modifié en fonction du type de disque persistant que vous prévoyez d'utiliser.

`redis.yaml`

* Déploiement Redis :  
- spec.template.spec.containers.resources.* (ressources CPU et mémoire pour le serveur cache)

`pgsql.yaml`

* PersistentVolumeClaim (`pgsql-pv-claim`) :  
- `spec.resources.requests.storage` (stockage du serveur de base de données)

`discourse.yaml`

* PersistentVolumeClaim (`discourse-pv-claim`)  
- spec.resources.requests.storage (stockage du disque du serveur web pour les logs et les sauvegardes)
* Déploiement (`web-server`)  
-`spec.template.spec.containers.image` (Définissez l'URL pour pointer vers votre image Docker)   
-`spec.template.spec.containers.env`

> `DISCOURSE_DEVELOPER_EMAILS`  
> `DISCOURSE_HOSTNAME`  
> `DISCOURSE_SMTP_ADDRESS`  
> `DISCOURSE_SMTP_PORT`

- spec.template.spec.containers.resources.* (ressources CPU et mémoire pour votre serveur web)

`ingress.yaml`

* `spec.rules.host`
* `spec.tls.hosts`

**Recommandé :** À partir de là, vous pourriez vouloir créer votre propre namespace pour le déploiement. Supposez également que vous avez défini le bon contexte pour exécuter la commande `kubectl` dans le namespace. (Pour plus de détails, lisez la [documentation Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/namespaces-walkthrough/)). Sinon, vous devriez renommer la plupart des noms dans les fichiers de configuration ci-dessus avec des noms uniques et ajouter des labels.  
   
Appliquez les secrets. `dbUsername` et `dbPassword` peuvent être ce que vous voulez. Veuillez définir le bon `smtpUsername` et `smtpPassword` pour les services de livraison de mail que vous utilisez.  
   
Une autre note sur HTTPS pour Ingress : vous devriez lire [ce document](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls) et les contrôleurs Ingress spécifiques à votre cluster et mettre à jour `ingress.yaml` en conséquence.

Appliquez tous les fichiers de configuration :

Avant de démarrer l'application, exécutez ce qui suit sur l'instance PostgreSQL pour initialiser correctement la base de données. Vous pouvez trouver le nom de votre pod en exécutant `kubectl get pods`.

Créez le déploiement Discourse et Ingress avec ces commandes :

À partir de là, votre instance Discourse devrait être opérationnelle. Voici quelques commandes utiles au cas où les choses ne fonctionneraient pas et nécessiteraient un débogage :

#### Configurer la sauvegarde S3 et le téléchargement de fichiers

Discourse peut utiliser AWS S3 pour la sauvegarde et le téléchargement de fichiers. Voici les étapes pour l'activer :

1. Créez deux buckets S3 : un pour la sauvegarde et un pour le téléchargement de fichiers. Définissez-les comme privés.

2. Créez un utilisateur IAM avec un accès API uniquement et attachez la politique en ligne AWS ci-dessous :

3. Remplissez la clé d'accès et l'ID de clé dans **Paramètres Discourse**.

Ensuite, Discourse peut télécharger des fichiers vers le bucket S3 que vous avez spécifié, afin que vous puissiez joindre des images et des pièces jointes dans chaque publication.

### C'est tout !

J'espère que cet article vous sera utile pour configurer votre propre plateforme Discourse. C'est aussi un exercice pratique pour moi pour essayer de déployer une application sur K8s.

### Améliorations potentielles et mise à l'échelle :

* Il est possible d'exécuter plusieurs répliques pour le serveur web Discourse pour la mise à l'échelle. Cela devrait fonctionner, mais je ne l'ai pas encore essayé.
* Nous pourrions également déployer PostgreSQL Primary-Replica pour la mise à l'échelle. Nous utilisons l'image Docker PostgreSQL de [Bitnami](https://bitnami.com/) et vous pouvez lire les instructions pertinentes [ici](https://github.com/bitnami/bitnami-docker-postgresql).

_Construisez une application ? Nos [outils pour développeurs gratuits](https://oursky.com/products/) et notre [backend open source](http://skygear.io) faciliteront votre travail._