---
title: Tests A/B avec NGINX en moins de 40 lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-14T20:26:42.000Z'
originalURL: https://freecodecamp.org/news/a-b-testing-with-nginx-in-40-lines-of-code-d4f94397130a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vW7X8V-kG0TVtdIwmHw7hQ.png
tags:
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Tests A/B avec NGINX en moins de 40 lignes de code
seo_desc: 'By Nitish Phanse

  A/B Testing, has enabled designers and product managers to get a deep insight into
  user behavioral patterns.

  On the one hand, it has allowed product managers more flexibility while conceptualizing
  user journeys. But on the other, it’...'
---

Par Nitish Phanse

Les tests A/B ont permis aux designers et aux chefs de produit d'obtenir une compréhension approfondie des schémas comportementaux des utilisateurs.

D'une part, cela a offert plus de flexibilité aux chefs de produit lors de la conceptualisation des parcours utilisateurs. Mais d'autre part, c'est devenu un cauchemar pour les développeurs, qui doivent créer deux versions du même composant.

> « Le concept général derrière les [tests A/B](https://en.wikipedia.org/wiki/A/B_testing) est de créer une expérience avec un groupe témoin et un ou plusieurs groupes expérimentaux (appelés « cellules » chez Netflix) qui reçoivent des traitements alternatifs. Chaque membre appartient exclusivement à une cellule au sein d'une expérience donnée, l'une des cellules étant toujours désignée comme la « cellule par défaut ». Cette cellule représente le groupe témoin, qui reçoit la même expérience que tous les membres Netflix non inclus dans le test. »

> - Blog Netflix

#### Que propose l'écosystème actuel ?

De nombreuses entreprises comme Mixpanel, VWO et Optimisely fournissent des SDK clients (code JavaScript) qui doivent être ajoutés dans la balise `head` du HTML de la page. Les tests peuvent ensuite être créés via un tableau de bord.

Bien que les méthodes ci-dessus offrent de nombreuses options en matière de couleurs de boutons, de hauteur de composants et d'autres attributs CSS, elles ne permettent pas vraiment de créer deux flux distincts.

De plus, certaines bibliothèques externes peuvent vraiment nuire aux temps de chargement de votre page et créer une expérience saccadée ou lente pour les utilisateurs.

### Présentation de NGINX

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lqqzohxt5sznYqtnrAh09w.png)

[Nginx](https://nginx.org/en/) est un serveur web léger qui offre une multitude de fonctionnalités comme l'équilibrage de charge, le proxy inverse et la compression HTML. Il est facile à installer et offre beaucoup de contrôle aux développeurs.

NGINX est un outil formidable pour distribuer le trafic pour les tests fractionnés.

Il est stable, extrêmement rapide, et les configurations pour les cas d'utilisation typiques sont courantes en ligne. Des configurations plus complexes peuvent être réalisées après seulement quelques heures d'exploration de la documentation. Les petites entreprises peuvent ne pas avoir les ressources pour investir dans des logiciels payants pour les tests A/B, mais NGINX offre une option pour effectuer une forme de test A/B.

Par exemple, disons que vous souhaitez voir lequel des formulaires ci-dessous aura une meilleure conversion :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny7aOxNtdXE88Ax8Q7B8eA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*I6fuPkJm2zwhYcYDE-4f1w.png)
_Version A et Version B respectivement_

Votre hypothèse pourrait être que moins de champs de formulaire impliquent moins de données à saisir par l'utilisateur, conduisant ainsi à plus de conversions.

Nous pouvons donc définir deux groupes : Version A et Version B. La première est le groupe témoin, qui est montré à 80 % du trafic. La seconde est le groupe test, qui forme les 20 % restants du trafic.

Le port 7770 hébergera un groupe de code, tandis que le port 7777 hébergera le second groupe de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pficodfp_HU6MW87VL3N6g.jpeg)

### Code

Votre fichier nginx.conf peut être modifié comme montré ci-dessous.

```
http {    # ...    # version de l'application 1a    upstream version_a {        server server 127.0.0.1:7770; ## Peut être une ip externe aussi    }
```

```
    # version de l'application 1b    upstream version_b {        server server 127.0.0.1:7777; ## Peut être une ip externe aussi    }
```

```
    split_clients "app${remote_addr}${http_user_agent}${date_gmt}"   $appversion {        80%     version_1a;        *       version_1b;    }
```

```
server {        # ...        listen 80;        location / {            proxy_set_header Host $host;            proxy_pass http://$appversion;        }    }}
```

Créez deux upstreams, un pour chaque groupe.

La directive `split_client` nous aide à rediriger le trafic selon le poids spécifié vers un upstream particulier.

Le `app${remote_addr}${http_user_agent}${date_gmt}appversion` crée un hachage basé sur les paramètres ci-dessus et est utilisé par nginx pour logger une requête faite à l'un ou l'autre groupe. De préférence, ces paramètres sont ceux qui concernent uniquement un utilisateur, comme `user_agent`, `remote addr`.

Ok — donc cela fonctionnera, mais cela ne donne pas à l'utilisateur une expérience persistante.

Si je rafraîchis ma page, il y a une chance que je bascule entre les groupes, et cela peut être une expérience utilisateur horrible.

Prenons le cas ci-dessus : imaginez essayer de remplir un formulaire de six champs, puis soudain, en rafraîchissant, voir un formulaire de deux champs. Confusant !

### Une approche différente

1. Transmettre la requête proxy à l'un ou l'autre groupe
2. Définir un cookie avec une durée d'expiration égale à la durée du test.
3. Vérifier l'existence du cookie et transmettre le proxy au bon groupe pour garantir une expérience utilisateur uniforme.

Nous utiliserons la directive `map` de NGINX et mapperons la variable `$cookie_name` à différents groupes que nous avons créés.

```
http {    # ...    # version de l'application a    upstream version_a {        server server 127.0.0.1:7770; ## Peut être une ip externe aussi    }
```

```
   # version de l'application b    upstream version_b {        server server 127.0.0.1:7777; ## Peut être une ip externe aussi    }    split_clients "app${remote_addr}${http_user_agent}${date_gmt}"     $appversion {        80%     version_a;        *       version_b;    }
```

```
    map $cookie_split_test_version $upstream_group {        default $appversion;        "version_a" "version_a";        "version_b" "version_b";    }
```

```
server {        # ...        listen 80;        location / {            add_header Set-Cookie "split_test_version=$upstream_group;Path=/;Max-Age=518400;";
```

```
            proxy_set_header Host $host;
```

```
            if ($upstream_group = "version_a") {                proxy_pass http://127.0.0.1:7777;                break;            }
```

```
          if ($upstream_group = "version_b") {                proxy_pass http://127.0.0.1:7770;                break;            }
```

```
          proxy_pass http://$appversion;        }    }}
```

Comme il est un peu difficile de formater le code ci-dessus...

![Image](https://cdn-media-1.freecodecamp.org/images/1*LekfEbjABlUcQ05aDIoAug.png)

### Conclusion

1. NGINX offre une API très simple pour créer un environnement de test A/B.
2. Permet de créer plusieurs groupes. L'exemple ci-dessus montre deux groupes, mais nous pouvons diviser le trafic et créer plus de groupes.
3. Comme le même code est hébergé sur deux ports, le déploiement peut devenir délicat (actuellement, j'ai deux branches : une master et une branche de test), qu'il soit fait à partir d'une branche différente ou de la même.
4. Effectuer plus d'un test A/B peut devenir délicat. Oui, vous pouvez utiliser la directive `location` et définir différents cookies en fonction des tests requis, mais avoir deux tests (_Test 1, Contrôle : 80, Test 20 & Test 2 Contrôle : 50, Test 50_) est impossible. Cela dit, vous ne devriez pas avoir plus d'un test A/B à la fois par page. Sinon, vous finirez par avoir 2^n versions de votre page, où n est le nombre de tests, et le suivi des conversions sera un enfer.
5. Le suivi peut maintenant être fait à un niveau très granulaire car les bases de code sont effectivement séparées.

N'hésitez pas à me faire savoir si j'ai fait une erreur dans ce qui précède. Heureux de corriger et d'apprendre. J'espère que vous avez aimé l'article.

**PS : Quelqu'un a-t-il remarqué qu'il y a moins de 40 lignes de code ?!**