---
title: Déployer une application NUXT sur S3 en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T02:42:01.000Z'
originalURL: https://freecodecamp.org/news/deploy-a-nuxt-app-to-s3-in-5-minutes-515a161eb74f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xw6OooWmB0S-uAM6VpqyIA.png
tags:
- name: AWS
  slug: aws
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Déployer une application NUXT sur S3 en 5 minutes
seo_desc: 'By Gareth Fuller

  Step by step guide to deploy a NUXT app with Vue.js to an AWS S3 bucket with a custom
  domain and everything! ?

  To start with, I’m assuming that you are somewhat familiar with Vue.js, NUXT and
  Amazon AWS S3 buckets.

  We’ve only got 5 m...'
---

Par Gareth Fuller

Guide étape par étape pour déployer une application NUXT avec Vue.js sur un bucket AWS S3 avec un domaine personnalisé et tout le reste ! 💡

Pour commencer, je suppose que vous êtes quelque peu familier avec [Vue.js](https://vuejs.org/), [NUXT](https://nuxtjs.org/) et les buckets Amazon AWS S3.

Nous n'avons que 5 minutes, alors commençons.

#### 1. Installer le Vue CLI

Sur la ligne de commande :

```
npm install -g @vue/cli
```

puis

```
npm install -g @vue/cli-init
```

#### 2. Créer votre application NUXT

Sur la ligne de commande :

```
vue init nuxt-community/starter-template exampleapp-frontend
```

puis

```
cd exampleapp-frontend
```

#### 3. Tester l'environnement de développement

Sur la ligne de commande :

```
npm install
```

puis

```
npm run dev
```

Si vous naviguez vers [localhost:3000](http://localhost:3000) dans votre navigateur, vous devriez voir la page d'accueil par défaut de NUXT.

#### 4. Générer votre application NUXT

Sur la ligne de commande :

```
npm run generate
```

Cela génère un dossier `/dist` avec la version de production de votre application NUXT. C'est ce dossier que nous allons déployer sur S3.

#### 5. Installer l'AWS CLI

Nous avons besoin de l'AWS CLI pour pouvoir créer et manipuler notre bucket S3 rapidement depuis la ligne de commande.

```
pip install awscli --upgrade --user
```

#### 6. Configurer votre AWS CLI

Cette étape est nécessaire pour avoir l'autorisation de créer un bucket S3 dans votre compte AWS depuis la ligne de commande.

```
aws configure
```

Il vous demandera ensuite certaines informations d'identification :

```
AWS Access Key ID: [ENTREZ VOTRE CLÉ D'ACCÈS]
AWS Secret Access Key: [ENTREZ VOTRE CLÉ SECRÈTE D'ACCÈS]
Default region name: [ENTREZ VOTRE RÉGION PRÉFÉRÉE]
Default output format: json
```

Pour votre « Default region name », choisissez celle qui vous convient le mieux. Voici une liste des [régions disponibles](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) pour le service S3.

#### 7. Créer votre bucket S3

Sur la ligne de commande :

```
aws s3api create-bucket --bucket votredomaine.com --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
```

Notez que nous avons nommé le bucket d'après le nom de domaine que nous souhaitons utiliser. Remplacez « votredomaine.com » par le domaine que vous souhaitez utiliser pour votre application. Remplacez également « eu-west-1 » par votre région préférée.

#### 8. Activer l'hébergement de site web statique sur le bucket S3

Sur la ligne de commande :

```
aws s3 website s3://votredomaine.com/ --index-document index.html --error-document index.html
```

Notez que nous définissons également les documents d'index et d'erreur de notre bucket d'hébergement statique S3. Dans cet exemple, nous les avons tous deux définis sur la page d'index NUXT (index.html), mais à l'avenir, vous pourriez vouloir changer le `--error-document` en une véritable page d'erreur.

#### 9. Activer la versioning du bucket S3

Sur la ligne de commande :

```
aws s3api put-bucket-versioning --bucket votredomaine.com --versioning-configuration Status=Enabled
```

#### 10. Créer une politique S3 pour téléverser vers le bucket S3

Cela permet à votre bucket S3 d'être accessible via une URL publique.

Dans votre répertoire local, créez un fichier JSON appelé `policy.json` et ajoutez ce qui suit :

```json
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::votredomaine.com/*"
    }
  ]
}
```

Puis ajoutez la politique à votre bucket depuis la ligne de commande :

```
aws s3api put-bucket-policy --bucket votredomaine.com --policy file://policy.json
```

#### 11. Déployer votre application NUXT sur S3

Sur la ligne de commande :

```
aws s3 cp dist s3://votredomaine.com --recursive
```

Ici, nous téléversons essentiellement le contenu de notre dossier `/dist` vers le bucket S3 que nous venons de créer.

#### 12. Pointer votre URL personnalisée vers votre nouvelle application

Obtenez l'URL de votre bucket S3 depuis la section « Properties » de votre bucket S3 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xw6OooWmB0S-uAM6VpqyIA.png)

Définissez l'enregistrement CNAME racine de votre domaine personnalisé pour pointer vers cet endpoint. Si vous utilisez Cloudflare pour le DNS, vous le configureriez comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*i3kV5BUyqmcOYqUF-CuO_g.png)

Remarque : vous devrez peut-être également supprimer les enregistrements DNS A actuellement associés à votre domaine.

Et c'est tout !

Si vous naviguez vers le domaine que vous avez spécifié (dans notre cas votredomaine.com), vous devriez pouvoir voir la page par défaut de l'application NUXT.

Vous ne croyez pas que cela peut être fait en 5 minutes ? J'ai suivi mon propre article, je l'ai enregistré dans une vidéo et je l'ai fait en **exactement 5 minutes** !

Un pur hasard en fait.

Voici la vidéo :

%[https://www.youtube.com/watch?v=peumMBGExFc]