---
title: Extension Géniale Pour Sites Statiques Qui Vous Fera Danser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T12:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-worry-free-blog-comments-in-20-simple-steps
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Copy-of-Static-Site-Docker-Recipes-2.jpg
tags:
- name: blog
  slug: blog
- name: Docker compose
  slug: docker-compose
- name: nginx
  slug: nginx
- name: oauth
  slug: oauth
- name: Static Site Generators
  slug: static-site-generators
seo_title: Extension Géniale Pour Sites Statiques Qui Vous Fera Danser
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  Privacy.

  Performance.

  Brilliant looks.

  Can you have all three?

  (Of course!)

  Having a statically generated blog is great. Many folks use services like Disqus
  and Google Analytics to make t...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/)**

Vie privée.

Performance.

Apparence géniale.

Pouvez-vous avoir les trois ?

(Bien sûr !)

Avoir un blog généré statiquement est génial. De nombreuses personnes utilisent des services comme Disqus et Google Analytics pour les améliorer encore. Pas surprenant si vous en faisiez partie ! Les préoccupations concernant la vie privée sont au premier plan de l'attention de tous. Alors, plutôt que de maintenir le statu quo, il est temps de faire quelque chose à ce sujet !

**Si vous cherchez à protéger la vie privée des visiteurs de votre site et à améliorer les performances, cet article est fait pour vous.**

Dans cet article, nous utiliserons le droplet Docker de DigitalOcean. Il vous permet d'héberger plusieurs applications/services différents sur une seule machine (virtuelle). À la fin, vous saurez comment exécuter votre propre serveur de commentaires en utilisant Commento. De plus, je partagerai quelques astuces que j'ai apprises en cours de route pour vous faciliter la tâche.

C'est parti !

## Proxy Inverse

L'un des aspects les plus importants de cette installation est le proxy inverse. Un proxy inverse agit comme un routeur. Les requêtes arrivent pour un certain domaine. Cette requête est ensuite routée vers le service associé à ce domaine.

Voici un diagramme de la documentation Nginx Reverse Proxy + Let's Encrypt Helper. Il aidera à illustrer l'idée.

![Nginx Reverse Proxy avec Let's Encrypt](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/webproxy-1f1c7540-4b86-4478-bb3e-f05043d671a5.jpg)

Un autre avantage est qu'il y a une couche supplémentaire de protection contre le monde extérieur. Vos sites web fonctionnent dans un réseau privé et le seul accès se fait via le proxy inverse Nginx. Pointez votre DNS vers le serveur et Nginx gère toute la magie.

Voici comment le configurer :

1. Allez-y et configurez votre Digital Ocean Droplet. [Toutes les informations dont vous avez besoin sont ici](https://marketplace.digitalocean.com/apps/docker). La version à 5 $ est plus que suffisante.
2. [Allez ici pour cloner le dépôt.](https://github.com/evertramos/docker-compose-letsencrypt-nginx-proxy-companion) Vous pouvez également exécuter cela dans votre terminal. Assurez-vous de vous connecter en SSH à votre droplet Digital Ocean d'abord !

        git clone git@github.com:evertramos/docker-compose-letsencrypt-nginx-proxy-companion.git

3. Changez de répertoire pour le dépôt cloné.
4. Copiez `.env.sample` en `.env` et mettez à jour les valeurs à l'intérieur. J'ai dû changer la valeur `IP` par l'IP de mon Digital Ocean Droplet. J'ai laissé toutes les autres telles quelles.
5. Exécutez `docker-compose up -d` pour tout démarrer. (vous pouvez exécuter sans l'option `-d` pour vous assurer que tout démarre correctement. Ou vous pouvez attacher la sortie du journal en utilisant `docker container logs -f <container name`

Lorsque vous pointez vos sous-domaines vers ce serveur, assurez-vous d'utiliser un enregistrement A. Voici un exemple du mien :

![Configuration de l'enregistrement A NS1](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-9c0432cd-4d40-4c89-88f3-24037d915eaf.52.32_PM.png)

Selon votre fournisseur DNS, vous devrez déterminer comment configurer un enregistrement A. Cela dépasse le cadre de cet article !

## Configuration de Commento avec Docker Compose

![Logo Commento avec Logo Docker](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Compose-1c868832-6819-43e2-8696-ab698a10dbee.jpg)

Voici le fichier docker compose actuel que j'utilise pour Commento. Il inclut quelques variables d'environnement supplémentaires pour configurer Github, Gitlab et Google. Il inclut également les variables d'environnement pour définir les paramètres SMTP. Ces paramètres sont importants. Sinon, vous ne pouvez pas recevoir d'e-mails de réinitialisation de mot de passe ou de modération !

    version: '3'

    services:
      commento:
        image: registry.gitlab.com/commento/commento
        container_name: commento
        restart: always
        environment:
          COMMENTO_ORIGIN: https://${COMMENTS_URL}
          COMMENTO_PORT: 8080
          COMMENTO_POSTGRES: postgres://postgres:postgres@postgres:5432/commento?sslmode=disable
          COMMENTO_SMTP_HOST: ${SMTP_HOST}
          COMMENTO_SMTP_PORT: ${SMTP_PORT}
          COMMENTO_SMTP_USERNAME: ${SMTP_USERNAME}
          COMMENTO_SMTP_PASSWORD: ${SMTP_PASSWORD}
          COMMENTO_SMTP_FROM_ADDRESS: ${SMTP_FROM_ADDRESS}
          COMMENTO_GITHUB_KEY: ${COMMENTO_GITHUB_KEY}
          COMMENTO_GITHUB_SECRET: ${COMMENTO_GITHUB_SECRET}
          COMMENTO_GITLAB_KEY: ${COMMENTO_GITLAB_KEY}
          COMMENTO_GITLAB_SECRET: ${COMMENTO_GITLAB_SECRET}
          COMMENTO_GOOGLE_KEY: ${COMMENTO_GOOGLE_KEY}
          COMMENTO_GOOGLE_SECRET: ${COMMENTO_GOOGLE_SECRET}
          COMMENTO_TWITTER_KEY: ${COMMENTO_TWITTER_KEY}
          COMMENTO_TWITTER_SECRET: ${COMMENTO_TWITTER_SECRET}
          VIRTUAL_HOST: ${COMMENTS_URL}
          VIRTUAL_PORT: 8080
          LETSENCRYPT_HOST: ${COMMENTS_URL}
          LETSENCRYPT_EMAIL: ${EMAIL}
        depends_on:
          - postgres
        networks:
          - db_network
          - webproxy

      postgres:
        image: postgres
        container_name: postgres
        environment:
          POSTGRES_DB: commento
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        networks:
          - db_network
        volumes:
          - postgres_data_volume:/var/lib/postgresql/data

    networks:
      db_network:
      webproxy:
        external: true

    volumes:
      postgres_data_volume:

Pour définir les variables d'environnement, placez-les dans un fichier `.env`. Assurez-vous que le fichier `.env` se trouve dans le même répertoire que `docker-compose.yml`. Lorsque vous exécutez `docker-compose up`, il appliquera les variables définies dans le fichier `.env`. Rien n'est défini si elles sont laissées vides.

Définissez les variables requises `COMMENTS_URL` et `EMAIL` ou vous pourriez rencontrer des problèmes. La meilleure façon de les définir est de les placer dans le fichier `.env`. Voici un exemple :

    COMMENTS_URL=comments.votre.url
    EMAIL=vous@votre.url

## Obtenir la clé et le secret OAuth

Commento fonctionne avec la plupart des fournisseurs OAuth populaires. Ainsi, les visiteurs peuvent laisser des commentaires sans créer de compte.

Les instructions sont similaires pour chacun. J'ai décrit les étapes pour tous ci-dessous.

### Twitter

1. Connectez-vous à [Twitter.com](http://twitter.com) et demandez un compte développeur : [https://developer.twitter.com/en/application/use-case](https://developer.twitter.com/en/application/use-case)

    ![Accès à l'API Twitter](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-4171cdf7-6c2b-408b-bb64-57822ede91cb.26.08_PM.png)

2. Décrivez comment vous utiliserez l'API. Vous pouvez utiliser ce que j'ai écrit.

    ![Comment allez-vous utiliser l'API ?](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-4c0aecf2-c020-4005-bd5f-81e3b4ac6b8f.28.43_PM.png)

3. Vérifiez votre entrée et cliquez sur **Cela a l'air bien !**

    ![Tout est-il correct ?](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-ade63510-86d3-48a4-a121-221f6e14cd96.28.50_PM.png)

4. Acceptez les conditions de service.

    ![Accepter l'accord de développeur](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-2e8e3089-bd51-4d27-8573-6987aafc663e.28.59_PM.png)

    ![Vous l'avez fait !](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-145b1bfd-9fc7-4ea6-ba5f-032e59d7fe8d.41.47_PM.png)

5. Ils vous diront de vérifier votre email pour une confirmation. Confirmez votre email et vous devriez pouvoir créer votre première application !
6. Une fois approuvé, cliquez sur **Commencer** puis sur **Créer une application**.

    ![Créer une application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-640686b8-15c6-4af0-b9df-65ce15ae0fe7.29.22_PM.png)

7. Sur l'écran suivant, cliquez à nouveau sur **Créer une application**

    ![Créer une application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-de2b85d5-8bb7-428f-bfd1-2a23d0b7d4e0.29.26_PM.png)

8. Entrez tous les détails appropriés. Pour l'URL de rappel, utilisez [`https://<votre URL>/api/oauth/github/callback`](https://comments.jaredwolff.com/api/oauth/google/callback) où [`<votre URL>`](https://comments.jaredwolff.com/api/oauth/google/callback) est votre sous-domaine Commento.

    ![Détails de l'application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-91acb343-9dee-4917-be77-9704fe439722.32.44_PM.png)

9. Enfin, une fois que vous avez terminé de remplir les informations, allez dans la section **Clés et jetons**. Sauvegardez à la fois la clé et le jeton. Entrez-les dans le fichier `.env`. Vous pouvez utiliser `COMMENTO_TWITTER_KEY` et `COMMENTO_TWITTER_SECRET`

    ![Obtenir la clé et le secret oauth](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_6-b910e9ff-dc34-45e8-94df-affb06702617.33.07_PM.png)

### Gitlab

1. Connectez-vous à [Gitlab.com](http://gitlab.com) et allez en haut à droite et cliquez sur **Paramètres**
2. Ensuite, cliquez sur **Applications**

    ![Profil Gitlab](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-c6da9d02-2052-4fa4-89de-d5212b8f49ca.56.47_PM.png)

3. Entrez un nom pour votre application. J'ai mis **Commento**.
4. Définissez l'URI de redirection sur [`https://<votre URL>/api/oauth/gitlab/callback`](https://comments.jaredwolff.com/api/oauth/google/callback)
5. Sélectionnez la portée **read_user**.

    ![Ajouter une application Gitlab](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-e616c338-6144-4704-93c6-914db6fad5f6.59.15_PM.png)

6. Cliquez sur le bouton vert **Enregistrer l'application**
7. Copiez l'**ID de l'application** et le **Secret** et placez-les dans votre fichier `.env` en utilisant `COMMENTO_GITLAB_KEY` et `COMMENTO_GITLAB_SECRET`

    ![Clé et secret de l'application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_1-a4f4ab4a-9fd6-423f-821c-6ff2f174e589.04.10_PM.png)

### Github

1. Pour obtenir votre clé et votre secret OAuth, vous devrez vous rendre à cette URL : [https://github.com/settings/developers](https://github.com/settings/developers)
2. Une fois là-bas, cliquez sur **Nouvelle application OAuth**

    ![Ajouter une application OAuth](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-18bf8f23-916f-476b-8c25-3377de931fe3.15.33_AM.png)

3. Entrez vos détails. Pour l'URL de rappel, utilisez [`https://<votre URL>/api/oauth/github/callback`](https://comments.jaredwolff.com/api/oauth/google/callback) où [`<votre URL>`](https://comments.jaredwolff.com/api/oauth/google/callback) est votre sous-domaine Commento.

    ![Enregistrer une nouvelle application OAuth](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-6e616334-7123-4de4-a4fd-f2fe319b1971.28.24_AM.png)

    *Remarque : Assurez-vous d'inclure `https` dans vos URLs.*

4. Récupérez l'**ID client** et le **secret client** et placez-les dans votre fichier `.env` en utilisant `COMMENTO_GITHUB_KEY` et `COMMENTO_GITHUB_SECRET`

    ![Application créée avec succès](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_9-7505a3ef-386a-4b75-a7dc-1dd3e22d0baf.29.28_AM.png)

### Google

La configuration de Google est presque aussi fastidieuse que celle de Twitter. Malgré la façon dont je viens de le décrire, c'est tout à fait réalisable. Voici les étapes.

1. Allez à cette URL : [Console des développeurs Google](https://console.developers.google.com/cloud-resource-manager?previousPage=%2Fapi)
2. Créez un nouveau projet

    ![Créer un nouveau projet](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-f3793926-cc54-4345-b81c-5ec0f4631a35.42.48_AM.png)

3. Cliquez sur le **logo GoogleAPIs** dans le coin supérieur gauche pour revenir en arrière une fois que vous avez un projet. (Assurez-vous que la liste déroulante à côté du **logo GoogleAPIs** est la même que votre nouveau projet !)
4. Ensuite, cliquez sur **Identifiants** sur le côté gauche.
5. Mettez à jour le **Nom de l'application** et les **Domaines autorisés** dans l'**écran de consentement OAuth**

    ![Configurer l'application](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-d839a5c9-3368-4f18-b674-73b6e4e7c17c.47.15_AM.png)

6. Cliquez sur **Créer des identifiants** puis sur **ID client OAuth**

    ![Configurer les identifiants](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-201545f9-4d47-4e0c-ae9a-b40efdc35a4b.44.36_AM.png)

7. Sur **Créer un ID client OAuth**, entrez le sous-domaine associé à Commento dans **Origines JavaScript autorisées**. Ensuite, entrez l'URL de rappel complète. Par exemple [`https://comments.jaredwolff.com/api/oauth/google/callback`](https://comments.jaredwolff.com/api/oauth/google/callback). Remplacez `comments.jaredwolff.com` par votre URL.

    ![Créer un ID client OAuth](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-fdba3491-d562-41f3-acff-2857ea816cec.52.15_AM.png)

    Une fois entré, cliquez sur le bouton **créer**.

8. Récupérez l'**ID client** et le **secret client**

    ![Identifiants OAuth](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-04_at_8-0c3f2895-0cb9-4b3a-a154-a3d80fd9716a.57.40_AM.png)

9. Mettez à jour votre fichier `.env` en utilisant `COMMENTO_GOOGLE_KEY` et `COMMENTO_GOOGLE_SECRET`

## Installer votre application

Vous avez entré vos identifiants OAuth, votre email, votre domaine et vos identifiants SMTP. Il est temps de conclure ce spectacle !

1. Une fois que vous avez terminé de modifier votre fichier `.env`, exécutez `docker-compose up` (Pour les fichiers non nommés `docker-compose.yml`, utilisez le drapeau `-f`. Exemple : `docker-compose -f commento.yml up`
2. Surveillez la sortie pour les erreurs. Si tout semble bon, vous pouvez vouloir l'arrêter (**CTRL+C**) et l'exécuter avec le drapeau `-d`
3. Au premier démarrage, Commento vous invitera avec un écran de connexion.

    ![Connexion Commento](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-d5a1ca53-93b3-49c5-a3a7-e8b728259e2d.11.29_PM.png)

4. Créez un nouveau compte en cliquant sur **Vous n'avez pas encore de compte ? Inscrivez-vous.**
5. Entrez vos informations et cliquez sur **S'inscrire**
6. Vérifiez votre email et cliquez sur le lien inclus :

    ![Email de validation avec lien](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-e263aa4f-201b-42ac-986c-b28c5f003f38.12.48_PM.png)

7. Connectez-vous avec votre compte nouvellement créé.
8. Ensuite, cliquez sur **Ajouter un nouveau domaine.**

    ![Ajouter un nouveau domaine](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-46acfe9c-f3f4-4d3e-b8fb-97fbff643a86.10.47_PM.png)

9. Une fois créé, allez dans **Guide d'installation**. Copiez le snippet et placez-le où vous voulez que vos commentaires apparaissent. Dans mon cas, j'ai placé le snippet dans une zone juste après ma balise `<article>`.

    ![Snippet de code](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-f78f36c5-f3f7-45ec-971d-9bf0bf7b7d1f.36.35_PM.png)

10. Recompilez votre site et vérifiez le succès !

    ![Section des commentaires du blog avec des cochet](https://www.jaredwolff.com/how-to-setup-worry-free-blog-comments-in-less-than-20-simple-steps/images/Screen_Shot_2019-07-05_at_12-8f7ffbdc-c49f-49bc-95bb-1f53a926f361.30.27_PM.png)

    Cochet ! Enfin, je vous recommande d'essayer de vous connecter avec chaque configuration OAuth individuelle. Ainsi, vous savez qu'elle fonctionne pour les visiteurs de votre site web. ?

## Alternatives

J'ai passé un bon moment à jouer avec certaines des alternatives. Ce n'est en aucun cas un guide définitif sur ce qui fonctionnera le mieux pour votre site. Voici quelques-unes des meilleures à ce jour :

[https://utteranc.es/#configuration](https://utteranc.es/#configuration)

[https://github.com/netlify/gotell](https://github.com/netlify/gotell)

[https://github.com/eduardoboucas/staticman](https://github.com/eduardoboucas/staticman)

[https://posativ.org/isso/](https://posativ.org/isso/)

[https://www.remarkbox.com](https://www.remarkbox.com/)

[https://www.vis4.net/blog/2017/10/hello-schnack/](https://www.vis4.net/blog/2017/10/hello-schnack/)

[https://github.com/gka/schnack](https://github.com/gka/schnack)

Il y a aussi un énorme fil de discussion sur le blog Hugo qui contient beaucoup plus de liens et de ressources également :

[https://discourse.gohugo.io/t/alternative-to-disqus-needed-more-than-ever/5516](https://discourse.gohugo.io/t/alternative-to-disqus-needed-more-than-ever/5516)

## Conclusion

Félicitations ! Vous hébergez maintenant votre propre serveur de commentaires ! ?

Dans cet article, vous avez appris à exploiter la puissance de Docker et d'un proxy inverse Nginx. En prime, vous savez comment configurer les identifiants OAuth ! Ainsi, la configuration future sera facile.

D'ailleurs, ce n'est que la partie émergée de l'iceberg. Vous pouvez configurer le même serveur pour l'analyse, la collecte de données et plus encore. [Tout le code exemple, y compris le code pour d'autres applications, peut être trouvé ici.](https://www.jaredwolff.com/files/host-your-comments/)

Enfin, si vous cherchez à payer pour Commento, rendez-vous sur [www.commento.io](http://www.commento.io) et inscrivez-vous au service. Vous soutiendrez un logiciel open source génial !

Si vous avez des commentaires et des questions, faisons-les entendre. Commencez la conversation ci-dessous. ???