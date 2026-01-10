---
title: Comment passer au serverless avec Rust et API Gateway
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-23T22:37:17.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-rust-and-api-gateway-aa5d1502c32e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X2YaTL1Nfk3bHkw7k8Y30w.jpeg
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: Rust
  slug: rust
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Comment passer au serverless avec Rust et API Gateway
seo_desc: 'By Michael Habib

  Before this year’s AWS re:Invent, there was no supported way to write AWS Lambda
  functions with Rust. I often come across the use of the Go runtime as a wrapper
  for the underlying Rust code. At re:Invent, AWS announced that its lambd...'
---

Par Michael Habib

Avant l'AWS re:Invent de cette année, il n'existait aucun moyen pris en charge pour écrire des fonctions AWS Lambda avec Rust. Je rencontre souvent l'utilisation du runtime Go comme wrapper pour le code Rust sous-jacent. Lors de re:Invent, AWS a annoncé que ses fonctions lambda pourront désormais prendre en charge n'importe quel langage. Les utilisateurs pourront en profiter en utilisant la nouvelle API runtime. Parallèlement à cette annonce, AWS a également open sourcé un [runtime Rust](https://github.com/awslabs/aws-lambda-rust-runtime) et publié un guide rapide [ici](https://aws.amazon.com/blogs/opensource/rust-runtime-for-aws-lambda/).

L'objectif de cet article est de fournir suffisamment d'informations pour démarrer avec API Gateway et Rust. Nous allons créer une simple fonction AWS Lambda qui servira une seule ressource API Gateway. Un exemple plus intermédiaire utilisant DynamoDB sera publié sur YouTube en mars. Si vous êtes intéressé à être notifié lorsque cela sera publié, suivez-moi sur [Twitter](https://twitter.com/_itshabib). Bien que toujours en cours, le code utilisé dans cette vidéo se trouve sur la branche `intermediate` du dépôt.

#### Prérequis

1. [Docker](https://docs.docker.com/install/)
2. Git
3. [Compte AWS](https://aws.amazon.com/console/)
4. [AWS CLI (optionnel)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
5. [Rust (optionnel)](https://www.rust-lang.org/tools/install)
6. [Terraform (optionnel)](https://www.terraform.io/)

**Clonez et forkez le dépôt depuis [ici](https://github.com/itsHabib/api-gateway-rust). Les instructions de configuration AWS peuvent être trouvées [ici](https://github.com/itsHabib/api-gateway-rust/blob/master/AWS_SETUP.md).**

### Gestion des requêtes

Pour commencer, exécutez `git checkout scratch` et modifiez le `Cargo.toml` dans le dossier users.

La section `[[bin]]` en bas du fichier indique à cargo de générer un exécutable avec ce nom. Cela est nécessaire car les packages de déploiement AWS Lambda attendent un fichier bootstrap. Concentrons-nous maintenant sur le code réel qui gérera les requêtes entrantes de l'API Gateway. Modifiez `users/src/main.rs` pour qu'il corresponde au fichier ci-dessous.

Nous commençons par déclarer une structure User qui sera utilisée pour nos réponses. Nous définissons ensuite un routeur qui correspond à la méthode de requête. Les trois fonctions responsables de la création des réponses sont `not_allowed`, `add_user` et `get_users`. Chaque fonction construit une réponse, gère une éventuelle erreur et envoie enfin la réponse.

Le crate `lambda_http` nous permet commodément de transformer des valeurs JSON de serveur en une réponse avec `into_response()`. Cela est fait dans `add_user` et `get_users` lorsque nous passons d'un utilisateur à une valeur JSON puis enfin à une réponse.

Gardez à l'esprit que aucune des requêtes POST n'ajoutera réellement d'utilisateurs à une base de données. Tout ce que fait la méthode `add_user` ici est de désérialiser le corps et de le renvoyer.

### Opérations — Build & Deploy

Bundler votre code et ses dépendances pour lambda peut parfois être délicat. Au moment de la rédaction de cet article, [SAM](https://aws.amazon.com/serverless/sam/) ne dispose pas d'une commande de build pour bundler les projets cargo. Au lieu de SAM, nous allons utiliser Docker et Terraform pour créer ces packages de déploiement et plus encore. Ajoutez un `Dockerfile` au dossier users avec le contenu suivant.

Une image de build lambci est utilisée comme image de base car elles fournissent un processus de build assez transparent. Le Dockerfile ci-dessus peut être divisé en cinq parties principales :

1. Installation de l'édition nightly de Rust
2. Ajout des fichiers du projet
3. Compilation du projet
4. Compression de l'exécutable
5. Création du plan Terraform

Nous avons également besoin d'un Dockerfile qui sera spécifiquement utilisé pour déployer nos ressources API Gateway. Créez un fichier appelé `Dockerfile.api` avec le contenu suivant.

Créons maintenant un script de build qui pilotera le processus de création et d'application de nos plans Terraform. Un plan Terraform est simplement une proposition des ressources qu'il souhaite créer. Ajoutez le contenu suivant à un `build.sh` et `deploy.sh`.

Les scripts de build et de déploiement utilisent Docker et Terraform pour créer ou mettre à jour nos ressources AWS. En résumé, le plan Terraform pour provisionner les ressources est créé lorsque `build.sh` est exécuté et ce plan est ensuite appliqué lors de l'exécution de `deploy.sh`. Terraform est hors du scope de cet article, mais vous pouvez consulter tout le code dans `users/terraform`. Pour build et déployer nos ressources lambda, exécutez `./build.sh && ./deploy.sh`.

Si tout s'est bien passé, vous devriez voir la fin de votre sortie comme celle ci-dessous. Gardez à l'esprit que les Dockerfiles supposent que les identifiants AWS_* sont définis comme variables d'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hE05hJTsK5ty9EYYPieHEQ.png)
_`./build.sh && ./deploy.sh`_

Pour déployer nos ressources API Gateway, exécutez `./build.sh --api && ./deploy.sh --api`. Comme la commande ci-dessus, si tout s'est bien passé, vous devriez voir la fin de votre sortie comme celle ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*atksjHls4NE50d2zkQth1Q.png)
_`./build.sh --api && ./deploy.sh --api`_

Assurez-vous de noter le `base_url` qui est affiché après le déploiement. Pour tester l'API, nous devons envoyer une requête GET et POST à `<base_url>`/users. Vous pouvez utiliser un programme comme Postman ou la ligne de commande comme dans la capture d'écran ci-dessous. Les deux commandes montrées dans l'image supposent que jq est installé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BOoHfuJ3csHtCSW1JZuPaA.png)

Pour détruire toutes les ressources créées dans cet article, exécutez `./destroy.sh && ./destroy.sh --state`.

J'espère que vous avez trouvé cet article utile pour démarrer avec API Gateway et Rust. N'hésitez pas à commenter, poser des questions ou suggérer un sujet que je pourrais aborder ensuite.

**_P.S. Suivez-moi sur [Twitter](https://twitter.com/_itsHabib)_**