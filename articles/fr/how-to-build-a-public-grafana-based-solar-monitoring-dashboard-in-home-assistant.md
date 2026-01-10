---
title: Comment créer un tableau de bord public de surveillance solaire basé sur Grafana
  dans Home Assistant
subtitle: ''
author: Daniel Anomfueme
co_authors: []
series: null
date: '2025-04-17T14:10:50.221Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-public-grafana-based-solar-monitoring-dashboard-in-home-assistant
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744899028552/8ad3f3c4-9b25-473d-b539-14dcb2f2b241.png
tags:
- name: iot
  slug: iot
- name: Home Assistant
  slug: home-assistant
- name: Grafana
  slug: grafana
- name: InfluxDB
  slug: influxdb
- name: solar energy
  slug: solar-energy
seo_title: Comment créer un tableau de bord public de surveillance solaire basé sur
  Grafana dans Home Assistant
seo_desc: If you have a solar inverter setup, one thing you would agree on with me
  is that data from your solar inverter setup is really important. Another thing that
  is also important is having a way to show what your energy generation, consumption,
  and so on...
---

Si vous avez une installation d'onduleur solaire, une chose sur laquelle vous serez d'accord avec moi est que les données de votre installation d'onduleur solaire sont vraiment importantes. Une autre chose qui est également importante est d'avoir un moyen de montrer ce que votre génération d'énergie, votre consommation, etc., ressemble publiquement.

Le problème est que la plupart des marques d'onduleurs solaires disposent d'une forme de plateforme de surveillance de données à distance, de [Victrons VRM](https://www.victronenergy.com/panel-systems-remote-monitoring/vrm) à [Growatts ShineServe](https://en.growatt.com/products/growatt-monitoring-platform) en passant par [Deyes Cloud](https://www.deyeinverter.com/product/accessory-monitoring-1/smart-pv-management-platform.html), entre autres. Mais je suis un adepte de l'auto-hébergement et du contrôle local des données. C'est l'une des meilleures façons de visualiser et de présenter toutes ces belles données que vous avez publiquement à d'autres bricoleurs, utilisateurs d'onduleurs solaires et au grand public sans dépendre de la solution de journalisation des données cloud de l'entreprise.

Dans cet article, nous allons utiliser les données disponibles dans notre installation Home Assistant, les envoyer à [InfluxDB](https://www.influxdata.com/products/influxdb/) et créer un tableau de bord [Grafana](https://grafana.com/oss/grafana/) à partir de celles-ci. Il existe un bon nombre de façons de connecter votre onduleur à Home Assistant, selon le fabricant. J'utilise un onduleur Growatt SPF ES 6000, et j'ai partagé un guide sur la façon de créer un enregistreur de données local pour celui-ci qui fonctionne avec Home Assistant [ici](https://hackernoon.com/turn-your-dumb-solar-inverter-into-a-smart-one-with-this-home-assistant-hack).

### Table des matières

* [Prérequis](#heading-prerequisites)
    
* [Comment installer et configurer InfluxDB](#heading-installation-et-configuration-influxdb)
    
* [Comment installer et configurer Grafana](#heading-installation-et-configuration-grafana)
    
* [Comment créer le tableau de bord solaire Grafana](#comment-creer-le-tableau-de-bord-solaire-grafana)
    
* [Comment créer un nouvel utilisateur administrateur et supprimer l'utilisateur administrateur par défaut](#comment-creer-un-nouvel-utilisateur-administrateur-et-supprimer-lutilisateur-administrateur-par-defaut)
    
* [Comment activer l'accès à distance au tableau de bord solaire](#comment-activer-lacces-a-distance-au-tableau-de-bord-solaire)
    
* [Conclusion](#heading-conclusion)
    

### **Prérequis**

* Home Assistant OS
    
* Un nom de domaine
    
* Un onduleur connecté à votre instance Home Assistant
    

## Comment installer et configurer InfluxDB

Nous allons commencer par configurer InfluxDB. InfluxDB est une base de données de séries temporelles open-source, qui diffère de la base de données que [Home Assistant utilise par défaut](https://www.home-assistant.io/docs/backend/database/#:~:text=The%20default%20database%20used%20is,other%20databases%20can%20be%20used.), SQLite. Nous allons utiliser InfluxDB v1, car il est beaucoup plus facile à configurer.

Allez dans votre tableau de bord Home Assistant et allez dans Paramètres > Modules complémentaires et cliquez sur le Magasin de modules complémentaires.

![Une capture d'écran des modules complémentaires Home Assistant](https://cdn.hashnode.com/res/hashnode/image/upload/v1744463486874/9dda1fca-24a9-4c30-a486-3b723e8535fe.png align="center")

Dans le Magasin de modules complémentaires, recherchez "InfluxDB" et cliquez sur le module complémentaire. Vous devriez voir l'écran ci-dessous, puis installez.

![Une capture d'écran des modules complémentaires Home Assistant, montrant la page du module complémentaire InfluxDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1744463639772/75f66c35-e7b3-4c20-96ea-9e9154829ac5.png align="center")

Activez le "Watchdog", car cela permet au module complémentaire de redémarrer s'il plante. Activez également "show in sidebar", ce qui vous permet de voir le module complémentaire dans la barre latérale de Home Assistant.

![Une capture d'écran du module complémentaire InfluxDB installé et certaines configurations activées](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465515531/0c9e9475-08c2-4bc3-afe5-baa4fdbae164.png align="center")

Démarrez le module complémentaire et consultez les logs pour vous assurer qu'il fonctionne. Le "Starting NGINX" est un indicateur qu'il fonctionne.

![Une capture d'écran des logs du module complémentaire InfluxDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1744465746577/f3adbd52-14cd-4e78-b2d7-789ad2c22b31.png align="center")

Ensuite, allez dans la barre latérale de Home Assistant et cliquez sur InfluxDB. Vous devez créer une nouvelle base de données pour stocker vos données et également créer un nouvel utilisateur qui a des privilèges d'administrateur pour lire et écrire des données. Allez dans l'onglet Admin d'InfluxDB.

![Une capture d'écran des paramètres d'admin du module complémentaire InfluxDB montrant la base de données disponible](https://cdn.hashnode.com/res/hashnode/image/upload/v1744466323654/78f21741-e6ca-4094-8fc3-adc563b3dfc1.png align="center")

Cliquez sur Create Database - et vous pouvez nommer la base de données comme vous le souhaitez. Je vais nommer la mienne **homeassistant**.

Par défaut, la politique de conservation pour une base de données créée est infinie (ce qui est pour toujours), mais vous pouvez configurer cela pour être n'importe quel intervalle de temps que vous souhaitez. La politique de conservation fait référence à l'intervalle de temps des données que la base de données peut contenir. Je préfère rester avec l'infini car je veux garder autant de données que possible et j'ai assez de stockage dans mon matériel Home Assistant pour cela.

![Une capture d'écran des paramètres d'admin du module complémentaire InfluxDB montrant la nouvelle base de données créée disponible](https://cdn.hashnode.com/res/hashnode/image/upload/v1744466625066/c2ae2012-44d8-4acb-91ae-25ad35fb18ff.png align="center")

Une fois la base de données créée, allez dans l'onglet Users pour que vous puissiez créer le nouvel utilisateur administrateur. Saisissez un nom d'utilisateur et un mot de passe pour cet utilisateur et cliquez sur Grant Admin, afin que le niveau de permission puisse être défini sur tout. J'ai créé un nouvel utilisateur appelé **root**.

![Une capture d'écran des paramètres d'admin du module complémentaire InfluxDB montrant les utilisateurs disponibles](https://cdn.hashnode.com/res/hashnode/image/upload/v1744467230710/6c025cb7-123a-4552-8090-6a9550e64ecf.png align="center")

À ce stade, ce qui reste à faire du côté InfluxDB est de dire à Home Assistant de commencer à envoyer les données des capteurs à InfluxDB. Vous pouvez faire cela en allant dans votre fichier **configuration.yaml** de Home Assistant et en ajoutant cette configuration ci-dessous. Votre hôte est l'IP de votre Home Assistant, le port est le port par défaut pour le module complémentaire InfluxDB, et les valeurs restantes sont basées sur les valeurs que vous avez utilisées pendant la configuration.

```yaml
influxdb:
  host: 192.168.8.12
  port: 8086
  database: homeassistant
  username: root
  password: password
  max_retries: 3
  default_measurement: state
```

Redémarrez votre Home Assistant et allez dans InfluxDB. Cliquez sur l'onglet Explore, et vérifiez si vous avez un fichier **database.autogen** là-bas. Cliquez dessus, et si vous voyez certaines valeurs sous Measurements & Tags, vous êtes prêt à partir.

![Une capture d'écran de l'onglet Explore du module complémentaire InfluxDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1744468647521/3082e165-04d9-4b7d-bfd7-8de0662c11a9.png align="center")

## Comment installer et configurer Grafana

Ensuite à notre agenda, nous allons installer et configurer Grafana. Le but est d'avoir Grafana interroger InfluxDB et créer des tableaux de bord basés sur les données interrogées.

Allez dans le magasin de modules complémentaires, recherchez Grafana, et installez-le. N'oubliez pas d'activer ces paramètres importants, puis démarrez le module complémentaire.

![Une capture d'écran de la page du module complémentaire Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744470196074/b3d69925-9ccc-45b9-8078-905866222d15.png align="center")

Une fois qu'il a démarré, cliquez sur Grafana dans la barre latérale. Vous arriverez à la page d'accueil de Grafana où vous pouvez créer ces tableaux de bord.

![Une capture d'écran de la page d'accueil du module complémentaire Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744470431232/0e4541a5-344f-4f46-bd85-44f4d92ea53c.png align="center")

Mais avant de faire cela, vous devez connecter InfluxDB à Grafana. Naviguez vers l'onglet de Grafana >> Connexions. Vous devriez voir une page "Add new connection". Recherchez InfluxDB et choisissez-le. Ensuite, cliquez sur le bouton add new datasource.

![Une capture d'écran de la page des paramètres de connexion du module complémentaire Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744470636092/8dcb8f2b-7fcd-49d3-80d8-abce4f83ea07.png align="center")

Sous HTTP, modifiez l'URL et utilisez **http://ha\_ip\_address:8086** - n'omettez pas le `http://` ou n'essayez pas d'utiliser `localhost` avec celui-ci. Faites défiler vers le bas jusqu'aux détails d'InfluxDB et remplissez les données que vous avez utilisées lors de la configuration d'InfluxDB. Ensuite, cliquez sur Save & Test. Si la configuration est correcte, vous devriez voir une coche verte et un texte disant "datasource is working...measurements found."

![Une capture d'écran de la configuration de connexion du module complémentaire Grafana pour InfluxDB](https://cdn.hashnode.com/res/hashnode/image/upload/v1744471708830/5b0d0306-8b74-4c02-9163-cc23a7c3425c.png align="center")

## Comment créer le tableau de bord solaire Grafana

Avec cela, vous devriez avoir InfluxDB en cours d'exécution et connecté à Grafana. Commençons à créer de beaux tableaux de bord à partir de toutes les données générées. Cette partie est subjective, donc vous pouvez vous sentir libre de modifier et de personnaliser le design à votre goût. Nous allons utiliser ce tableau de bord [ici](https://helio.openculture.org.ng/public-dashboards/cf813bfa739044129e125bdd65db7a65?ref=blog.openculture.org.ng) comme inspiration pour notre design.

![Une capture d'écran d'un tableau de bord que nous voulons recréer](https://cdn.hashnode.com/res/hashnode/image/upload/v1744548823070/811cb6b1-d3f6-4880-b665-8af999d4c703.png align="center")

Alors maintenant, allez dans votre Grafana dans Home Assistant, cliquez sur l'icône + et créez un nouveau tableau de bord.

![Une capture d'écran de la page d'accueil de Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744544792278/0bbc6140-1335-4597-a972-80a5ddee1744.png align="center")

Vous devez savoir qu'un tableau de bord dans Grafana fait référence à l'espace complet et chaque élément placé sur le tableau de bord est un panneau. Chaque visualisation sur le tableau de bord est un panneau.

Créons un nouveau panneau. Choisissez InfluxDB comme source de données, et à la ligne **FROM**, choisissez W qui est l'unité à partir de laquelle nous voulons créer une visualisation. **WHERE** est entity\_id::tag, car c'est la façon de trier les valeurs par nom d'entité de capteur Home Assistant. Ensuite, choisissez l'ID d'entité de votre panneau - le mien est **growatt\_pv1\_charge\_power.** Vous pouvez changer le titre du panneau, changer la visualisation en stat, et ajouter le watt comme unité et la couleur de base en jaune.

La requête brute ressemble à ceci :

```sql
SELECT mean("value") FROM "W" WHERE ("entity_id"::tag = 'growatt_pv1_charge_power') AND $timeFilter GROUP BY time($__interval) fill(null)
```

La page d'édition de Grafana ressemble à ceci :

![Une capture d'écran de la vue d'édition du panneau Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744550024020/bb50d494-c6bc-45f2-8ff0-17173e7255bc.png align="center")

À ce stade, vous devriez être en mesure de recréer les parties restantes du tableau de bord. Mais je l'ai fait manuellement, donc vous n'avez pas à tout faire vous-même si vous ne le souhaitez pas.

[Voici](https://github.com/LifeofDan-EL/Grafana-Solar-Dashboard) le lien vers un dépôt GitHub qui contient le fichier JSON de ce tableau de bord. Lorsque vous allez créer un tableau de bord, vous verrez une option pour importer à partir d'un fichier JSON. Vous pouvez choisir de copier et coller ou de télécharger le fichier, selon ce qui fonctionne pour vous.

Après l'importation, vous n'avez besoin que de modifier chaque panneau via l'interface graphique pour utiliser votre propre balise d'ID d'entité dans Home Assistant et également l'UID de votre base de données InfluxDB.

Voici une image de mon résultat final :

![Une capture d'écran du produit final du tableau de bord que j'ai construit](https://cdn.hashnode.com/res/hashnode/image/upload/v1744559385614/57b58bfe-7fc2-4fa7-a0d2-19485558899a.png align="center")

## Comment créer un nouvel utilisateur administrateur et supprimer l'utilisateur administrateur par défaut

Par défaut, le module complémentaire Grafana dans Home Assistant utilise un proxy d'authentification et crée un utilisateur par défaut (`admin`) avec un mot de passe (`hassio`) qui est synchronisé avec votre session de connexion HA. Cela empêche les changements de mot de passe ou d'utilisateur via l'interface utilisateur.

Pour contexte, un proxy d'authentification, ou proxy d'authentification, agit comme un intermédiaire entre un client et une ressource cible, gérant l'authentification et l'autorisation au nom du client.

Comme mesure de sécurité, nous devons créer un nouvel utilisateur pour le module complémentaire Grafana et modifier ses permissions pour avoir des privilèges d'administrateur, puis supprimer l'utilisateur administrateur par défaut. Cela est dû au fait que vous ne pouvez pas changer le mot de passe de l'utilisateur administrateur par défaut sur le module complémentaire.

Allez dans le menu de Grafana > Administration > Users et accès > Users. Ensuite, créez un nouvel utilisateur.

![Une capture d'écran de la page des paramètres des utilisateurs de Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744571233206/daf2c674-4501-4774-89d9-76992227b531.png align="center")

Ensuite, donnez-lui des privilèges d'administrateur. Modifiez Grafana Admin pour qu'il soit oui et assurez-vous que le rôle de l'organisation est défini sur admin, puis enregistrez.

![Une capture d'écran du paramètre utilisateur de Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744749794592/21e85eab-99ca-4c7d-9d18-19e9f31ea1da.png align="center")

Retournez à l'onglet Configuration du module complémentaire. Faites défiler jusqu'au paramètre Réseau et ajoutez un port pour exposer le module complémentaire. J'utiliserai le port 3000. Enregistrez et redémarrez le module complémentaire. Si vous avez activé SSL et qu'il n'est pas configuré, le module complémentaire ne démarrera pas. Vous pouvez le désactiver car nous allons laisser Cloudflare gérer cela.

![Une capture d'écran de l'onglet Configuration du module complémentaire Grafana](https://cdn.hashnode.com/res/hashnode/image/upload/v1744750541094/326aa725-7b81-4407-82ef-e6589a153b9c.png align="center")

Pour confirmer que le port a été exposé correctement, allez à `http://ha_ip:3000/` et confirmez que vous voyez cet écran de connexion Grafana. Assurez-vous qu'il s'agit de http et non de https.

![Une capture d'écran de la page d'accueil de Grafana accessible depuis l'URL externe de Home Assistant](https://cdn.hashnode.com/res/hashnode/image/upload/v1744563139292/e17d2691-3b77-4faf-997d-95a0b3141066.png align="center")

Connectez-vous en tant que nouvel utilisateur que vous avez créé. Ensuite, allez dans votre liste d'utilisateurs et supprimez l'utilisateur administrateur par défaut.

![Une capture d'écran de l'édition de l'utilisateur administrateur par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1744750661705/1d98e960-e325-4a5c-9746-64ff1819a573.png align="center")

Après cela, retournez à l'onglet Configuration du module complémentaire Grafana. Cliquez sur les 3 points de la ligne Options et choisissez Edit in YAML. Ensuite, ajoutez cette ligne ci-dessous à votre fichier de configuration et enregistrez.

```yaml
grafana_ingress_user: usernameofnewuser
```

## Comment activer l'accès à distance au tableau de bord solaire

À ce stade, nous avons le tableau de bord solaire prêt et nous pouvons y accéder dans Home Assistant depuis notre réseau domestique. Mais nous ne voulons pas qu'il soit accessible uniquement de cette manière. Nous voulons que n'importe qui puisse visiter le lien sans avoir accès à notre réseau domestique.

Je vais mettre en œuvre cette partie à l'aide d'un module complémentaire Home Assistant Cloudflared qui utilise Cloudflare Tunnel. Voici le [dépôt GitHub](https://github.com/brenner-tobias/addon-cloudflared) - l'installation est simple et sans stress.

Après avoir effectué la configuration et avoir un accès à distance à votre réseau Home Assistant (n'oubliez pas d'activer la 2FA), allez dans l'onglet de configuration du module complémentaire Cloudflared et modifiez la partie Additional Hosts.

```yaml
- hostname: subdomain_you_want.your_domain.xyz
  service: http://ha_ip:3000
  disableChunkedEncoding: true
```

Enregistrez et redémarrez le module complémentaire et consultez les logs. Vous devriez voir qu'il crée une entrée DNS pour le nom d'hôte que vous avez ajouté.

Comme autre mesure de sécurité, allez dans l'onglet Configuration du module complémentaire Grafana. Ajoutez ces valeurs aux variables d'environnement.

```yaml
- name: GF_AUTH_ANONYMOUS_ENABLED
  value: "true"
- name: GF_AUTH_ANONYMOUS_ORG_ROLE
  value: "Viewer"
- name: GF_AUTH_DISABLE_LOGIN_FORM
  value: "true"
```

* `GF_AUTH_ANONYMOUS_ENABLED` : Toute personne qui visite Grafana sans se connecter sera toujours autorisée.
    
* `GF_AUTH_ANONYMOUS_ORG_ROLE` : Cela définit la permission par défaut pour les utilisateurs anonymes. Dans ce cas, les utilisateurs anonymes auront le rôle de visualisateur.
    
* `GF_AUTH_DISABLE_LOGIN_FORM` : Désactive le formulaire de connexion sur la page de connexion de Grafana. Assurez-vous d'être déjà connecté sur le nom d'hôte distant. Mais vous pouvez toujours modifier cela dans l'onglet Configuration du module complémentaire si vous êtes bloqué.
    

## Conclusion

Enfin, allez à l'hôte distant pour votre Grafana et vous devriez voir la page d'accueil de Grafana. Ensuite, allez dans vos tableaux de bord et cliquez sur le tableau de bord solaire créé. Partagez-le et choisissez publiquement. Maintenant, vous pouvez partager ce lien (l'URL de cette page et non l'URL copiée réelle du bouton de partage) avec n'importe qui et ils pourront voir votre beau tableau de bord.

Cette méthode sert de moyen tout-en-un pour tout faire, via votre machine Home Assistant. J'espère que vous vous êtes amusé à bricoler, à la prochaine fois.