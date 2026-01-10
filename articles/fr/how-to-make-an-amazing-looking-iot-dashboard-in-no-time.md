---
title: Comment créer un tableau de bord IoT magnifique en un rien de temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-03T21:17:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-amazing-looking-iot-dashboard-in-no-time
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Dashboard-3.png
tags:
- name: iot
  slug: iot
- name: Iot Portal
  slug: iot-portal
seo_title: Comment créer un tableau de bord IoT magnifique en un rien de temps
seo_desc: "By Jared Wolff\nThis post is originally from www.jaredwolff.com\nIn this\
  \ post, I’m going to show you how to get started with Grafana and InfluxDB. All\
  \ of this running docker container on Digital Ocean. \nThat way you can have pretty\
  \ graphs like these:\n\n..."
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-make-an-amazing-looking-iot-dashboard-in-no-time/)**

Dans cet article, je vais vous montrer comment commencer avec Grafana et InfluxDB. Tout cela fonctionne dans un conteneur Docker sur Digital Ocean.

Ainsi, vous pouvez avoir de jolis graphiques comme ceux-ci :

![Tableau de bord IoT](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-05_at_12.55.10_PM.png)

Le coût ?

**5 $ par mois**

Commençons.

## Étapes
1. Connectez-vous à Digital Ocean. Si vous n'avez pas de compte Digital Ocean et que vous souhaitez soutenir ce blog, cliquez [ici](https://m.do.co/c/9574d3846a29) pour créer un compte.
2. Allez dans `Paramètres du compte` -> `Sécurité` et assurez-vous d'avoir une clé SSH configurée.
![Screen_Shot_2019-05-07_at_9.14.07_AM](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-07_at_9.14.07_AM.png)
3. Créez une nouvelle droplet en utilisant leur [image docker](https://marketplace.digitalocean.com/apps/docker)
4. Assurez-vous de sélectionner le forfait à 5 $ par mois. Pour les installations simples, c'est plus que suffisant !
5. Connectez-vous en SSH une fois terminé : `ssh root@<votre_ip_serveur>`
6. Configurez InfluxDB

      ```
      docker run --rm -e INFLUXDB_HTTP_AUTH_ENABLED=true -e INFLUXDB_DB=particle -e INFLUXDB_ADMIN_ENABLED=true -e INFLUXDB_ADMIN_USER=admin -e INFLUXDB_USER=grafana -v influxdb:/var/lib/influxdb influxdb /init-influxdb.sh
      ```

      Observez la sortie de cette commande. Elle générera des mots de passe pour les utilisateurs `admin` et `grafana`. Sauvegardez-les dans un endroit sûr !

7. Démarrez influx
      ```
      docker run -d -p 8086:8086 \
            -v influxdb:/var/lib/influxdb \
            -e INFLUXDB_HTTP_AUTH_ENABLED=true \
            influxdb
      ```

8. Ajoutez une règle de pare-feu

      ```
      ufw allow 8086
      ```

      Cela permet au monde extérieur d'accéder à votre instance InfluxDB.

9. Configurez curl depuis Particle

      Exemple d'appel équivalent :
      ```
      curl -i -XPOST 'http://<IP DOCKER ICI>:8086/write?db=particle' --data-binary 'temperature,id=<ID ICI> value=22.1'
      ```

      La version à mettre dans la **requête personnalisée** serait :

      ```
      temperature,id={{{PARTICLE_DEVICE_ID}}} value={{{temperature}}}
      ```

      ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-04_at_9.19.59_PM.png)

      **Note :** sous `PARAMÈTRES DE REQUÊTE`, `db` pointe vers `particle`. Cela doit pointer vers ce que vous avez défini pour `INFLUXDB_DB` à l'étape 6.

      **Deuxième note :** assurez-vous que le nom d'utilisateur et le mot de passe sont ceux que vous avez configurés à l'étape 6. Dans cet exemple, le nom d'utilisateur est `grafana`.

      ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-04_at_9.19.54_PM.png)

      Voici une version plus complexe :

      ```
      temperature,id={{{PARTICLE_DEVICE_ID}}} value={{{temperature}}}
      humidity,id={{{PARTICLE_DEVICE_ID}}} value={{{humidity}}}
      tvoc,id={{{PARTICLE_DEVICE_ID}}} value={{{tvoc}}}
      c02,id={{{PARTICLE_DEVICE_ID}}} value={{{c02}}}
      {{#pm25}}pm25,id={{{PARTICLE_DEVICE_ID}}} value={{{pm25}}}{{/pm25}}
      {{#pm10}}pm10,id={{{PARTICLE_DEVICE_ID}}} value={{{pm10}}}{{/pm10}}
      {{#sgp30_tvoc}}sgp30_tvoc,id={{{PARTICLE_DEVICE_ID}}} value={{{sgp30_tvoc}}}{{/sgp30_tvoc}}
      {{#sgp30_c02}}sgp30_c02,id={{{PARTICLE_DEVICE_ID}}} value={{{sgp30_c02}}}{{/sgp30_c02}}
      {{#bme680_pres}}bme680_pres,id={{{PARTICLE_DEVICE_ID}}} value={{{bme680_pres}}}{{/bme680_pres}}
      {{#bme680_iaq}}bme680_iaq,id={{{PARTICLE_DEVICE_ID}}} value={{{bme680_iaq}}}{{/bme680_iaq}}
      {{#bme680_temp_calc}}bme680_temp_calc,id={{{PARTICLE_DEVICE_ID}}} value={{{bme680_temp_calc}}}{{/bme680_temp_calc}}
      {{#bme680_hum_calc}}bme680_hum_calc,id={{{PARTICLE_DEVICE_ID}}} value={{{bme680_hum_calc}}}{{/bme680_hum_calc}}
      ```

      Pour les données conditionnelles, vous pouvez envelopper toute la ligne dans la variable qui peut être présente ou non :

      ```
      {{#bme680_pres}}<insérez des éléments liés à bme680_pres>{{/bme680_pres}}
      ```

10. Ensuite ! Installez Grafana avec stockage persistant

      ```
      # créez un volume persistant pour vos données dans /var/lib/grafana (base de données et plugins)
      docker volume create grafana-storage

      # démarrez grafana
      docker run \
        -d \
        -p 3000:3000 \
        --name=grafana \
        -v grafana-storage:/var/lib/grafana \
        grafana/grafana
      ```

11. Ajoutez une règle de pare-feu pour Grafana

        ```
        ufw allow 3000
        ```

12. Connectez-vous. Cela devrait être l'IP de votre droplet Digital Ocean + :3000 ajouté. Exemple : `123.456.789.101:3000` (Le nom d'utilisateur et le mot de passe par défaut sont **admin** et **admin**)

13. Connectez Grafana à Influx (cela devrait être l'une des premières options sur une nouvelle installation de Grafana)

    ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-04_at_9.24.02_PM_copy.png)

    ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-04_at_9.25.39_PM_copy.png)

    **Note** sous utilisateur, vous devrez mettre le nom d'utilisateur `grafana` et le mot de passe généré à l'étape 6. De plus, le nom de la base de données a été défini comme `particle` à la même étape.

14. Testez votre connexion en cliquant sur `Enregistrer et tester`. Cela devrait revenir rapidement en indiquant si une connexion a été réussie ou non.
15. Démarrez votre appareil, si ce n'est pas déjà fait, et faites-le publier dans votre base de données InfluxDB.

    (Besoin de données ? [Ce projet devrait vous en fournir !](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/))

16. Créez des graphiques !

    Enfin, la raison pour laquelle vous êtes venu sur cette page : **de jolis graphiques**

    Cliquez sur l'icône **+** à gauche et créez un **nouveau tableau de bord**

    ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-07_at_9.32.49_AM.png)

17. Sélectionnez `Ajouter une requête`

    ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-07_at_9.33.58_AM.png)

18. Descendez et cliquez sur `sélectionner une mesure`. Si votre appareil a publié dans votre base de données, vous devriez voir des options pour les valeurs.

    ![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-07_at_9.34.32_AM.png)

19. Sous `fill(null)`, changez cela en `fill(none)`. Cela devrait vous donner une belle ligne entre les points de données.
20. Vous devriez voir le graphique apparaître !
![](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-05-07_at_9.36.36_AM.png)
19. Cliquez sur le bouton de retour en arrière, puis cliquez sur le bouton d'enregistrement.
20. Vous venez de créer un graphique simple à partir des données directement de votre appareil ! Je vous recommande de jouer avec l'interface Grafana. Elle est assez intuitive et ne prend que quelques minutes pour s'y habituer !

## HTTPS/SSL

L'installation de HTTPS/SSL est assez simple. Suivez les étapes ci-dessous :

1. Arrêtez l'instance Grafana si ce n'est pas déjà fait
2. Démarrez un nouveau conteneur avec `nginx-proxy`
   ```
   docker run --detach \
       --name nginx-proxy \
       --publish 80:80 \
       --publish 443:443 \
       --volume /etc/nginx/certs \
       --volume /etc/nginx/vhost.d \
       --volume /usr/share/nginx/html \
       --volume /var/run/docker.sock:/tmp/docker.sock:ro \
       jwilder/nginx-proxy
   ```

3. Exécutez le `letsencrypt-nginx-proxy-companion`

   ```
   docker run --detach \
       --name nginx-proxy-letsencrypt \
       --volumes-from nginx-proxy \
       --volume /var/run/docker.sock:/var/run/docker.sock:ro \
       jrcs/letsencrypt-nginx-proxy-companion
   ```

4. Redémarrez le conteneur Grafana

   ```
   docker run \
     -d \
     --env "VIRTUAL_HOST=<VOTRE_ADRESSE_SOUS_DOMAINE>" \
     --env "VIRTUAL_PORT=3000" \
     --env "LETSENCRYPT_HOST=<VOTRE_ADRESSE_SOUS_DOMAINE>" \
     --env "LETSENCRYPT_EMAIL=<VOTRE_ADRESSE_EMAIL>" \
     --name=grafana \
     -v grafana-storage:/var/lib/grafana \
     grafana/grafana
   ```

   **Note :** assurez-vous de remplacer `<VOTRE_ADRESSE_SOUS_DOMAINE>` et `<VOTRE_ADRESSE_EMAIL>` ci-dessus par vos propres informations.

Le compagnon proxy générera un certificat SSL pour l'hôte virtuel que vous avez fourni au conteneur Grafana. Le proxy est utilisé pour rediriger tout le trafic HTTP/HTTPS vers votre conteneur Grafana. C'est propre, c'est simple et c'est sécurisé !

**Note** InfluxDB est un peu plus difficile. Vous devez soit créer un sous-domaine séparé, soit configurer HTTPS pour partager les certificats entre Grafana et Influx. Ce [script Docker Compose](https://www.grzegorowski.com/grafana-with-lets-encrypt-ssl-on-docker/) fait tout cela si vous n'avez pas encore tout installé. Vous pouvez suivre les mêmes étapes ci-dessus si vous souhaitez l'exécuter sur un sous-domaine séparé.

## Liens utiles
Voici quelques liens utiles que j'ai trouvés pour commencer avec Grafana + InfluxDB

* [influxdb | Documentation Docker](https://docs.docker.com/samples/library/influxdb/)
* [Prise en main | Documentation Grafana](https://grafana.com/docs/guides/getting_started/)
* [Installation avec Docker | Documentation Grafana](https://grafana.com/docs/installation/docker/)
* [Let's Encrypt Nginx Proxy Companion](https://hub.docker.com/r/jrcs/letsencrypt-nginx-proxy-companion/)
* [Très utile pour configurer HTTPS pour Grafana et Influx](https://www.grzegorowski.com/grafana-with-lets-encrypt-ssl-on-docker/)

## Conclusion

Vous l'avez fait. Profitez de votre nouvelle installation Grafana + InfluxDB !

Si vous avez aimé ce tutoriel, partagez-le avec vos amis et vos ennemis. De plus, si vous en voulez plus, [découvrez comment construire votre propre capteur de qualité de l'air en utilisant seulement quelques pièces.](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/)