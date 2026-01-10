---
title: Expérimentation avec l'API HTTP d'Apache Mesos pour le plaisir et le profit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-27T21:59:44.000Z'
originalURL: https://freecodecamp.org/news/experimenting-with-the-apache-mesos-http-api-for-fun-and-profit-part-1-of-3-cf5736e84f85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YWIt5Ajh2lAk4e2yj4jO8Q.jpeg
tags:
- name: Mesos
  slug: mesos
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Expérimentation avec l'API HTTP d'Apache Mesos pour le plaisir et le profit
seo_desc: 'By Marco Massenzio

  Apache Mesos is a tool used in production at large-scale services like Twitter and
  Airbnb. Here’s its textbook description:


  The Mesos kernel runs on every machine and provides applications (e.g., Hadoop,
  Spark, Kafka, Elasticsearc...'
---

Par Marco Massenzio

Apache Mesos est un outil utilisé en production dans des services à grande échelle comme Twitter et Airbnb. Voici sa description théorique :

> Le noyau Mesos s'exécute sur chaque machine et fournit aux applications (par exemple, Hadoop, Spark, Kafka, Elasticsearch) des API pour la gestion des ressources et la planification dans des environnements de centres de données et de cloud entier. — du site du projet [Apache Mesos](https://mesos.apache.org).

Il s'agit du premier d'une série de trois articles qui montrent comment configurer un environnement de test/développement Apache Mesos basé sur Vagrant sur votre ordinateur portable, comment exécuter un notebook Python contre l'API HTTP, et comment lancer des conteneurs Docker sur la VM Agent en cours d'exécution.

Cette série est une version étendue (et mise à jour) de la [conférence](https://youtu.be/G7xfEs0lX5U) que j'ai donnée à **MesosCon Europe 2015**, mise à jour pour Apache Mesos 1.0.0, qui vient d'être publiée (août 2016) — vous pouvez également trouver les [diapositives](http://events.linuxfoundation.org/sites/events/files/slides/MesosCon%20EU%20-%20HTTP%20API%20Framework.pdf) là-bas.

Cet article est assez chargé et nécessitera que vous soyez familier avec certains concepts autour des conteneurs, des VM et de Mesos. Mais je prendrai le temps de montrer toutes les étapes intermédiaires (d'où les 3 parties). Il devrait être facile à suivre, même si vous n'avez jamais utilisé Vagrant, Mesos, ou même les notebooks Jupyter auparavant.

Je vous recommande d'abord d'avoir une familiarité de base avec Python et la gestion des requêtes et réponses HTTP, car nous n'aborderons pas ces détails ici.

Tout le code est disponible [sur le dépôt git zk-mesos](https://github.com/massenz/zk-mesos) :

```
git clone git@github.com:massenz/zk-mesos.git
```

Et vous pouvez également consulter le [README](https://github.com/massenz/zk-mesos).

### Mise en route

Pour suivre, vous devrez cloner le dépôt (comme montré ci-dessus) et installer [Virtualbox](http://virtualbox.org) et [Vagrant](https://www.vagrantup.com/docs). Suivez les instructions sur leurs sites respectifs et vous serez opérationnel en un rien de temps.

Je recommande également de parcourir rapidement la documentation de Vagrant. Une connaissance de Vagrant au-delà de `_vagrant up` n'est pas vraiment nécessaire pour tirer le meilleur parti de cette série, mais cela peut aider si vous êtes bloqué (ou si vous souhaitez expérimenter et améliorer notre _Vagrantfile_).

Si vous n'êtes pas familier avec [Apache Mesos](https://mesos.apache.org), je recommande de consulter le site du projet. Je recommande de lire [Mesos in Action](http://amzn.to/2citsRx) (notez que j'étais l'un des relecteurs du manuscrit).

Nous ne construirons **pas** Mesos à partir des sources ici, mais utiliserons plutôt les [paquets Mesosphere](http://open.mesosphere.com/downloads/mesos/). Vous n'avez pas besoin de les télécharger. Le _Vagrantfile_ les téléchargera et les installera automatiquement sur les VM.

Pour exécuter le notebook Python, nous profiterons des paquets [Jupyter](http://jupyter.org) et utiliserons un _virtualenv_ pour exécuter tout notre code. Virtualenv n'est pas strictement nécessaire, mais empêchera de désorganiser votre Python système.

Si vous n'avez jamais utilisé [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) auparavant :

```
$ sudo pip install virtualenv
```

Puis créez et exécutez un _virtualenv_ :

```
$ cd zk-mesos
$ virtualenv mesos-demo
$ source mesos-demo/bin/activate
$ pip install -r requirements.txt
```

Enfin, vérifiez que vous pouvez exécuter et charger le notebook Jupyter :

```
$ jupyter notebook
```

Cela devrait automatiquement ouvrir votre navigateur et le pointer vers [http://localhost:8888](http://localhost:8888). À partir de là, vous pouvez sélectionner le fichier _notebooks/Demo-API.ipynb_. Ne l'exécutez pas tout de suite, mais s'il s'affiche, cela confirmera que votre configuration Python est correcte.

### Construction et installation d'Apache Mesos

C'est là que la beauté de Vagrant brille de tout son éclat. L'installation d'Apache Mesos Master et Agent ne sont pas des tâches triviales, mais dans notre cas, il suffit de :

```
$ cd vagrant
$ vagrant up
```

Assurez-vous d'être dans le même répertoire que le _Vagrantfile_ lorsque vous émettez l'une des commandes Vagrant, sinon il se plaindra.

Il est à noter que nous construisons **deux** boxes Vagrant, donc toute commande opérera sur **les deux** sauf si spécifié. Pour éviter cela, vous pouvez spécifier le nom de la VM après la commande. Par exemple, pour se connecter en SSH à l'Agent :

```
$ vagrant ssh agent
```

Cela devrait vous connecter à cette box. À partir de là, vous pouvez explorer, expérimenter et diagnostiquer tout problème.

La commande _vagrant up_ prendra un certain temps à s'exécuter, mais elle devrait finalement amener votre Virtualbox à avoir deux VM, nommées respectivement _mesos-master_ et _mesos-agent_. Accessoirement, vous ne devriez jamais avoir besoin d'utiliser VirtualBox pour les gérer. Toutes les tâches peuvent être entreprises via les commandes Vagrant. Mais vous pouvez les gérer manuellement si nécessaire ou souhaité.

Une fois vos VM construites, assurez-vous de pouvoir accéder à l'interface utilisateur HTTP de Mesos à l'adresse :

```
http://192.168.33.10:5050
```

![Image](https://cdn-media-1.freecodecamp.org/images/uzGS7oJkLwPeUpQvw8H3eoHEVZeq3Nurmg0O)
_Interface web du Master Mesos — accessible à http://192.168.33.10:5050_

Vous devriez également voir un agent en cours d'exécution, accessible soit via l'interface utilisateur du Master.

![Image](https://cdn-media-1.freecodecamp.org/images/crYwNv0fIdcZmmrQiHPotFET2aviNHr3etEO)
_Vue des Agents sur l'interface web du Master Mesos_

Ou directement à l'adresse :

```
http://192.168.33.11:5051/state
```

![Image](https://cdn-media-1.freecodecamp.org/images/TjtQITaW3MEkyObTyLMGbQSDnqqpsOP4tVnd)
_Réponse JSON de l'Agent, lors de l'accès au point de terminaison /state_

Notez que l'Agent s'exécute non seulement sur une adresse IP différente de celle du Master, mais également sur un port différent (5051 au lieu de 5050).

Consultez vagrant/run-agent.sh pour voir quelques-uns des indicateurs de ligne de commande que nous utilisons pour exécuter l'Agent (et dans run-master.sh pour le Master).

### Zookeeper

Il est à noter que nous exécutons également une instance de Zookeeper (pour l'élection du Leader et la coordination Master/Agent) sur la VM _mesos-master_, à l'intérieur d'un conteneur Docker : en partie parce que nous pouvons le faire, mais aussi pour montrer à quel point il est facile de le faire en utilisant des conteneurs.

Cette ligne unique (dans _run-master.sh_) vous donnera une instance ZK parfaitement fonctionnelle (bien que catastrophiquement peu fiable dans un environnement de production, où vous souhaiteriez exécuter au moins 3 à 5 nœuds, au moins, sur des machines/racks physiquement séparés) :

```
docker run -d --name zookeeper -p 2181:2181 -p 2888:2888 \
    -p 3888:3888 jplock/zookeeper:3.4.8
```

Et parce que nous exposons les ports (en particulier, 2181) à la VM hôte, nous pouvons nous y connecter via l'utilitaire CLI Zookeeper (_zkCli.sh_) et l'explorer. À partir de votre machine de développement (vous devrez d'abord télécharger Zookeeper), vous pouvez utiliser :

```
$ zkCli.sh -server 192.168.33.10:2181
...
[zk: 192.168.33.10:2181(CONNECTED) 4] get /mesos/vagrant/json.info_0000000000
```

```
# Formaté pour une meilleure lisibilité :
{
  "address":  {
    "hostname": "mesos-master",
    "ip":"192.168.33.10",
    "port":5050
  },
  "hostname":"mesos-master",
  "id":"7eb34f10-b07c-4921-aece-bbaece09dfd1",
  "ip":169978048,
  "pid":"master@192.168.33.10:5050",
  "port":5050,
  "version":"1.0.0"
}
```

```
cZxid = 0xbctime = Sat Aug 27 14:00:44 PDT 2016
...
```

C'est ainsi que les Agents obtiennent des informations sur la manière de se connecter au nœud Master.

Le suffixe __000000_ est incrémenté chaque fois qu'un nouveau Leader est élu, donc selon la durée d'exécution de l'instance ZK et si le Master a été redémarré, il peut devenir quelque chose comme __0000005. Il s'agit d'un « nœud éphémère » dans le jargon de Zookeeper.

Dans cet enregistrement ci-dessus, il est à noter que « pid » est l'identifiant unique de _libprocess_ et « ip » est une représentation compressée en 4 octets d'un quadruple d'octets IPv4. Ces champs hérités peuvent éventuellement être supprimés.

#### Conclusion

Vous êtes maintenant le fier propriétaire d'un déploiement Apache Mesos à 2 nœuds Master/Agent. Bienvenue dans la même ligue que les sorciers de production de Twitter et Airbnb.

Dans la partie 2, nous exécuterons notre notebook Python contre l'API Master et accepterons les offres de l'Agent pour lancer un conteneur Docker.

Si vous avez le temps, plongeons-nous et apprenons [comment se connecter au Master Mesos et accepter les offres de ressources](https://medium.com/@massenz/a-python-notebook-to-experiment-with-the-apache-mesos-http-api-part-2-of-3-7f97fbe32e80#heading-installation).

_Publié à l'origine sur [codetrips.com](https://codetrips.com/2016/08/27/a-python-notebook-to-experiment-with-the-apache-mesos-http-api-part-1-of-3/) le 27 août 2016._