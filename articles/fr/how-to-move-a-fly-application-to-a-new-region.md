---
title: Comment déplacer une seule machine Fly et un volume vers une nouvelle région
  avec flyctl
subtitle: ''
author: Clarence Bakosi
co_authors: []
series: null
date: '2024-07-18T13:19:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-move-a-fly-application-to-a-new-region
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Cover-1.png
tags:
- name: Cloud
  slug: cloud
- name: deployment
  slug: deployment
seo_title: Comment déplacer une seule machine Fly et un volume vers une nouvelle région
  avec flyctl
seo_desc: 'Fly.io allows users to deploy their applications to virtual machines in
  regions where their applications are mostly used. A Fly application can also be
  deployed to multiple regions.

  You may want to move your Fly application to a new region if you exp...'
---

Fly.io permet aux utilisateurs de déployer leurs applications sur des machines virtuelles dans des régions où leurs applications sont principalement utilisées. Une application Fly peut également être déployée dans plusieurs régions.

Vous pouvez souhaiter déplacer votre application Fly vers une nouvelle région si vous rencontrez des problèmes de performance, une latence élevée ou des problèmes de conformité de résidence des données. Placer votre application plus près de vos utilisateurs peut réduire la latence et améliorer le temps de réponse.

De plus, aligner votre stockage de données avec les exigences de conformité régionales peut prévenir les problèmes juridiques. Globalement, ces changements améliorent l'expérience utilisateur avec votre application.

Cet article expliquera comment déplacer en douceur une application Fly qui inclut une seule [Fly Machine](https://fly.io/docs/machines/overview/) et un [Fly Volume](https://fly.io/docs/volumes/overview/) attaché, d'une [région Fly](https://fly.io/docs/reference/regions/) à une autre en utilisant les commandes [flyctl](https://fly.io/docs/flyctl/).

## **Prérequis**

* [Compte Fly.io](https://fly.io/dashboard)
* `flyctl` installé
* Interface de ligne de commande (CLI)

## **Pour commencer**

Pour commencer, vous devrez vérifier si vous avez déjà `flyctl` installé et également l'authentifier.

### Comment vérifier l'installation de `flyctl`

Vous pouvez vérifier que vous avez `flyctl` installé en utilisant la commande ci-dessous. Si ce n'est pas le cas, utilisez ce [guide](https://fly.io/docs/flyctl/install/) pour l'installer.

```bash
fly version
```

![fly version](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.43.16.png)
_Sortie de fly version_

Cela montre la version que vous avez installée.

### Comment authentifier `flyctl`

Connectez le terminal à votre compte via le CLI en utilisant :

```bash
fly auth login
```

Lorsque le navigateur s'ouvre, connectez-vous si vous n'êtes pas déjà connecté et procédez à l'authentification de votre CLI.

Après avoir authentifié votre compte, retournez au CLI.

## **Comment confirmer la région de l'application**

Accédez au dossier racine de votre projet et exécutez la commande suivante pour déterminer la région actuelle de votre application :

```bash
fly status
```

![fly status](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.44.26.png)
_Sortie de fly status_

La région actuelle de l'application est `lhr`, la commande montre des informations supplémentaires sur l'application, y compris le nom de l'application, le propriétaire, le nom d'hôte, l'image et les détails de la machine.

## **Comment vérifier le nombre de volumes disponibles**

Exécutez la commande suivante pour lister tous les volumes :

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.45.05.png)
_Sortie de fly volumes list_

Il devrait y avoir un seul volume qui existe et il devrait déjà être attaché à une machine. Vous pouvez utiliser ce [guide](https://fly.io/docs/apps/volume-storage/#launch-a-new-app-with-a-fly-volume) pour créer une application avec une seule machine avec un volume attaché.

## **Comment vérifier que le volume est attaché à une machine**

Pour vous assurer que le volume est attaché à une machine, exécutez :

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.14.04.png)
_Sortie de fly machine list_

À partir de la sortie, vous pouvez déterminer s'il y a un volume attaché à la machine.

## **Liste des régions Fly**

Pour déterminer la nouvelle région vers laquelle vous souhaitez déplacer la machine et le volume, utilisez la commande suivante pour afficher la liste des régions disponibles :

```bash
fly platform regions
```

![fly platform regions](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.15.13.png)
_Sortie de fly platform regions_

Pour cet article, la machine et le volume seront déplacés vers la région `syd`.

## **Forker le volume disponible vers une nouvelle région**

Vous pouvez créer une copie d'un volume existant et le placer dans une nouvelle région en le forkant en utilisant l'ID de volume actuel pour créer un fork :

```bash
fly volumes fork vol_4yj0k93z118j9x14 --region syd
```

Résultat :

![fly volumes fork](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.16.00.png)
_Sortie de fly volumes fork_

Cela montre des informations sur le nouveau volume créé.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.18.52.png)
_Sortie de fly volumes list_

L'état actuel du nouveau volume forké dans une nouvelle région sera dans un état `hydrating` pendant quelques minutes avant de passer à `created`.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.19.11.png)
_Sortie de fly volumes list_

L'image ci-dessus montre l'état actuel après la fin de `hydrating`.

Vous avez réussi à créer un nouveau volume dans une autre région contenant des données du volume existant dans l'ancienne région.

## **Comment cloner la machine existante**

Fly possède la fonctionnalité de clonage pour répliquer une machine et vous pouvez l'utiliser en obtenant l'ID de la machine existante.

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.19.43.png)
_Sortie de fly machine list_

Après avoir récupéré l'ID de la machine, utilisez la commande ci-dessous pour cloner la machine et attacher le nouveau volume en utilisant la même région que le nouveau volume créé :

Par exemple :

```bash
fly machine clone <machine id> --region <region code> --attach-volume <volume id>:<destination_mount_path>
```

Il est important de noter que le `destination_mount_path` doit être un chemin différent de `/` qui est le répertoire racine de l'application. Il doit être un chemin unique `/zata`.

```bash
fly machine clone 5683977a624218 --region syd --attach-volume vol_vzkd2l6yxnk72p9v:/zata
```

![fly machine clone](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.20.06.png)
_Sortie de fly machine clone_

Vous avez réussi à créer un clone de la machine existante et à attacher le volume forké.

## **Comment vérifier l'attachement du volume**

Pour vérifier si le volume a été attaché avec succès :

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.20.37.png)
_Sortie de fly volumes list_

Le volume est maintenant attaché à une machine.

Pour vérifier si la machine a été attachée avec succès :

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.21.08.png)
_Sortie de fly machine list_

La machine a maintenant un volume attaché.

Vous avez réussi à déplacer la machine et le volume vers une nouvelle région.

## **Comment afficher les régions disponibles de l'application**

Actuellement, l'application existe dans deux régions différentes et vous pouvez voir cela en utilisant la commande suivante :

```bash
fly scale show
```

![fly scale show](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.21.30.png)
_Sortie de fly scale show_

L'application fonctionne maintenant dans `lhr` et `syd`.

## **Comment mettre à jour le fichier fly.toml distant**

Ajoutez la nouvelle région au fichier **fly.toml** `primary_region = 'syd'`, mettez à jour la destination du volume à `destination = '/zata'`, et déployez les changements.

```bash
fly deploy
```

![fly deploy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.22.37.png)
_Sortie de fly deploy_

Une fois cela réussi, les changements apportés au fichier **fly.toml** seront dans la configuration distante.

## **Comment détruire l'ancienne machine**

Vous avez réussi à déplacer votre machine et le volume attaché vers une nouvelle région et puisque nous n'avons plus besoin de la machine dans l'ancienne région `lhr`, vous devrez la nettoyer. La première approche consiste à arrêter la machine en utilisant l'ID.

### Arrêter l'ancienne machine

```bash
fly machine stop <old_machine_id>
```

![fly machine stop](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.23.39.png)
_Sortie de fly machine stop_

Pour confirmer si cela a réussi, utilisez :

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.11.png)
_Sortie de fly machine list_

L'état de la machine a été mis à jour à `stopped`

### Détruire l'ancienne machine

```bash
fly machine destroy <old_machine_id>
```

![fly machine destroy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.35.png)
_Sortie de fly machine destroy_

Exécutez la commande ci-dessous pour vérifier si la machine existe toujours.

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.59.png)
_Sortie de fly machine list_

La machine dans l'ancienne région a été supprimée avec succès.

## **Comment détruire le volume non attaché**

Après avoir détruit la machine avec succès, le volume qui lui était attaché est maintenant non attaché et peut également être détruit.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.25.24.png)
_Sortie de fly volumes list_

Utilisez l'ID du volume non attaché et exécutez la commande ci-dessous :

```bash
fly volumes destroy <old_volume_id>
```

![fly volumes destroy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.26.04.png)
_Sortie de fly volumes destroy_

Le volume non attaché a maintenant été détruit.

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.26.27.png)
_Sortie de fly volumes list_

Un seul volume existe et est attaché à une machine dans la nouvelle région.

## **Comment vérifier l'état de l'instance**

Vérifiez les logs pour voir l'état de l'instance :

```bash
fly logs
```

Les logs montrent que l'application fonctionne sans aucun problème.

## **Conclusion**

Déplacer une application Fly.io vers une nouvelle région implique de forker le volume existant, de cloner la machine existante avec le volume forké vers une nouvelle région, de mettre à jour **fly.toml**, de déployer les changements et de supprimer l'ancienne machine et le volume.

En suivant ces directives, vous assurez une transition fluide et réussie avec une perturbation minimale.

Si vous avez des questions, vous pouvez toujours me trouver sur [X (anciennement Twitter)](https://x.com/X8inez)

## **Ressources** :

* [Fly Docs](https://fly.io/docs)
* [Flyctl](https://fly.io/docs/flyctl)
* [Fly Machines](https://fly.io/docs/machines/overview/)
* [Fly Volumes](https://fly.io/docs/volumes/overview/)
* [Régions Fly](https://fly.io/docs/reference/regions/)