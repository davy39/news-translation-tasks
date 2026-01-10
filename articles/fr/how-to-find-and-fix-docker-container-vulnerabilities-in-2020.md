---
title: Comment trouver et corriger les vulnérabilités des conteneurs Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-20T16:20:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-and-fix-docker-container-vulnerabilities-in-2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/New-Project--1-.jpg
tags:
- name: Docker
  slug: docker
- name: Security
  slug: security
seo_title: Comment trouver et corriger les vulnérabilités des conteneurs Docker
seo_desc: 'By Dipto Karmakar

  Containerization allows engineering teams to create a sandbox environment in which
  to run and test applications. Containers are mostly made up of open-source images
  pulled in from docker hub or other public image repositories.

  But t...'
---

Par Dipto Karmakar

La conteneurisation permet aux équipes d'ingénierie de créer un environnement sandbox dans lequel exécuter et tester des applications. Les conteneurs sont principalement composés d'images open-source tirées de Docker Hub ou d'autres dépôts publics d'images.

Mais ces images open-source peuvent parfois contenir des vulnérabilités qui peuvent compromettre la sécurité des conteneurs et, par conséquent, celle de leur machine/serveur hôte.

Étant donné que ces conteneurs s'exécutent sur une machine hôte, il est possible de détourner des conteneurs en production s'ils sont laissés sans protection.

Un bon exemple d'une telle attaque est [l'attaque de cryptojacking de Tesla](https://cointelegraph.com/news/tesla-cryptojacked-hackers-use-passwordless-system-to-mine-crypto) sur un cluster Kubernetes non protégé. Lors de cette attaque, les attaquants ont pu télécharger et exécuter un script malveillant pour miner des cryptomonnaies en utilisant les GPU fournis par le cluster K8s (Kubernetes) de Tesla. Ils ont pu garder cette attaque sous le radar en maintenant l'utilisation du CPU à un minimum et en exécutant le script à des intervalles de temps spécifiques.

Au cours de cet article, nous examinerons les vulnérabilités courantes des conteneurs et les moyens possibles de les corriger.

## Vulnérabilités courantes des conteneurs et comment les corriger

Les conteneurs sont utilisés par les ingénieurs ops pour packager et déployer un logiciel/application dans un environnement fermé et contrôlé.

Dans le but d'éviter de réinventer la roue et d'accélérer le temps de mise sur le marché, des images open-source déjà existantes sont tirées pour satisfaire les dépendances nécessaires à l'exécution du logiciel. Ces images contiennent souvent certaines vulnérabilités qui rendent l'ensemble du conteneur et son hôte vulnérables aux attaques malveillantes.

Voici quelques vulnérabilités et expositions courantes des conteneurs ainsi que la manière de les atténuer.

### Cryptojacking

Le cryptojacking est un type d'attaque où un script malveillant est utilisé pour voler les ressources computationnelles d'un appareil afin de miner des cryptomonnaies.

Récemment, une vulnérabilité a été découverte sur Docker avec l'entrée de dictionnaire [CVE-2018-15664](https://nvd.nist.gov/vuln/detail/CVE-2018-15664). Cette vulnérabilité permet aux attaquants d'obtenir un accès root à une machine hôte.

Outre le fait de pouvoir utiliser les ressources CPU et GPU de la machine hôte pour miner des cryptomonnaies, les attaquants peuvent également voler des informations d'identification sensibles, mener des attaques DoS, lancer des campagnes de phishing, et plus encore.

Les conteneurs peuvent être sensibles au cryptojacking s'ils contiennent des images malveillantes qui donnent aux attaquants un accès root à l'ensemble du conteneur. Ils sont également vulnérables si les points de terminaison de l'API du conteneur Docker sont accessibles publiquement sur Internet sans mots de passe ou pare-feux de sécurité, comme dans le cas de Tesla.

%[https://twitter.com/bad_packets/status/1199087675833085959?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fpaperusercontent.com%2Fintegrations%2Fembed%2Fiframe%2Ftweet%3Fid%3D1199087675833085959] 

### Images open-source malveillantes

Une vulnérabilité qui permet de remplacer le binaire runc de l'hôte donne aux attaquants la possibilité d'exécuter des commandes avec un accès root. Les moteurs Docker antérieurs à la version 18.09.2 rendent les conteneurs avec des images contrôlées par l'attaquant vulnérables à la vulnérabilité [CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736).

Il est conseillé aux ingénieurs, autant que possible, d'utiliser les images Docker officielles fournies par Docker. Après tout, il existe même une équipe sponsorisée par Docker qui travaille en étroite collaboration avec les mainteneurs/éditeurs de logiciels et les experts en sécurité pour garantir la sécurité des images Docker officielles.

### Dockerfiles statiques

L'un des principes des conteneurs est qu'une image est immuable. Cela signifie que lorsque l'image est construite, son contenu est inchangable. Cela donne lieu à des vulnérabilités qui résultent de packages/bibliothèques/images obsolètes contenus dans une image.

Par conséquent, il est judicieux d'incorporer des scanners de vulnérabilités dans les processus CI/CD afin d'identifier les images de conteneurs vulnérables. Puisque les images sont immuables, le déploiement d'un nouveau conteneur avec des dépendances mises à jour aidera à limiter les vulnérabilités de sécurité, car le [correctif de conteneur](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-how-containers-enable-passive-patching-and-a-better-model-for-supply-chain-security) est déconseillé.

## Comment trouver les vulnérabilités des conteneurs

Dans la section précédente, nous avons examiné les différentes manières dont les vulnérabilités peuvent s'introduire dans les conteneurs Docker.

Trouver les vulnérabilités dans nos conteneurs avant qu'ils n'atteignent la production aidera à éviter les éventuelles failles de sécurité et à tenir les attaquants malveillants à distance.

> Comme on dit - mieux vaut prévenir que guérir.

Dans cette section, nous examinerons les différentes manières dont vous pouvez rester en avance sur les vulnérabilités des conteneurs.

### Utilisation de Docker Bench pour la sécurité

[Docker Bench](https://github.com/docker/docker-bench-security) pour la sécurité est un script qui teste tous les conteneurs Docker sur l'ordinateur/serveur hôte pour les meilleures pratiques de déploiement des conteneurs en production. Ces tests sont basés sur le [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker/).

Pour un test, vous pouvez tirer l'image `docker/docker-bench-security` et tester les conteneurs existants sur votre machine locale comme suit :

```bash
docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /etc:/etc:ro \
    -v /usr/bin/docker-containerd:/usr/bin/docker-containerd:ro \
    -v /usr/bin/docker-runc:/usr/bin/docker-runc:ro \
    -v /usr/lib/systemd:/usr/lib/systemd:ro \
    -v /var/lib:/var/lib:ro \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    --label docker_bench_security \
    docker/docker-bench-security
```

**Note** : cette commande ne fonctionne pas bien sous OSX. Voir ce [problème GitHub](https://github.com/docker/docker-bench-security/issues/158) pour plus de détails.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview.png align="left")

### Analyse des vulnérabilités dans GCR

Les dépôts d'images Docker (par exemple, [GCR](https://cloud.google.com/container-registry)) permettent aux ingénieurs d'exécuter des analyses de vulnérabilités pour les images dans le registre de conteneurs.

Pour activer l'analyse des vulnérabilités dans GCR (Google Container Registry), rendez-vous dans les [paramètres du registre de conteneurs](https://console.cloud.google.com/gcr/settings) sur la console cloud Google et cliquez sur "activer l'analyse des vulnérabilités" comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--1-.png align="left")

Lorsque l'analyse des vulnérabilités est terminée, vous verrez un résultat comme dans l'image ci-dessous si des vulnérabilités existent :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--2-.png align="left")

### Utilisation de solutions de niveau entreprise

Il existe des suites de sécurité de conteneurisation de niveau entreprise qui gèrent les vulnérabilités et appliquent les politiques de déploiement tout au long du cycle de vie d'un conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image_preview--3-.png align="left")

En outre, cette suite de produits s'intègre également de manière transparente avec les outils CI/CD populaires et les registres de conteneurs. Cela lui permet de fournir des déploiements sans risque ainsi qu'une gestion de conteneurs de bout en bout, du déploiement à la production.

## Conclusion

Les conteneurs permettent aux équipes d'ingénierie de déployer des logiciels de manière transparente. Cependant, cette facilité a un coût en termes de sécurité.

Il existe plusieurs CVEs (Common Vulnerability Exposures) dans les conteneurs Docker enregistrées ces dernières années. Certaines d'entre elles ont été résolues dans les mises à jour récentes du moteur Docker, le reste étant promis dans les futures [versions de correctifs](https://docs.docker.com/engine/release-notes/).

Les équipes d'ingénierie doivent avoir la sécurité à l'esprit lors de la construction et du déploiement de conteneurs. Elles doivent également appliquer des politiques de sécurité des conteneurs dans leurs cycles de vie DevOps.