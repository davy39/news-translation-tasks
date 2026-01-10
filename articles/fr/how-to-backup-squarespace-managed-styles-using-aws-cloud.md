---
title: Comment sauvegarder les styles gérés par Squarespace en utilisant AWS Cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-14T19:19:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-backup-squarespace-managed-styles-using-aws-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/backup-with-aws-cloud.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
seo_title: Comment sauvegarder les styles gérés par Squarespace en utilisant AWS Cloud
seo_desc: 'By Adham El Banhawy

  A while ago, I was doing side gig for a client who had a website hosted on Squarespace.
  They asked me to implement an advanced design for a page that wasn''t possible with
  the site''s current DIY tools.

  For an experienced and battle...'
---

Par Adham El Banhawy

Il y a quelque temps, je faisais un travail à côté pour un client qui avait un site web hébergé sur Squarespace. Ils m'ont demandé de mettre en œuvre un design avancé pour une page qui n'était pas possible avec les outils DIY actuels du site.

Pour un développeur web expérimenté et aguerri comme moi, c'était une tâche simple même si je n'avais jamais travaillé avec des outils de création de sites web auparavant. Tout ce que j'avais à faire était d'écrire mon CSS et JavaScript personnalisés et de les injecter dans le site tout en référençant la documentation des développeurs de Squarespace.

Mais malgré mon expérience, j'ai rencontré un problème qui m'a mis à genoux et m'a fait douter de moi en tant que développeur (oh salut syndrome de l'imposteur – longtemps sans te voir !). Voici l'histoire de comment j'ai rencontré ce problème, comment je l'ai débogué et finalement comment je l'ai résolu en utilisant le cloud AWS.

## Où sont passés les styles du site ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-132.png)
_Un site cassé === Un cœur brisé_

Je me souviens avoir simplement changé la marge d'une classe dans l'éditeur CSS du site en utilisant une variable. Lorsque j'ai cliqué sur sauvegarder dans l'éditeur de styles du site admin, j'ai vu l'aperçu en direct devenir blanc. J'ai ouvert le site en direct dans un nouvel onglet, et j'ai été accueilli par un site web cassé sur toutes les routes.

Bizarre... ce simple changement n'aurait pas dû casser le site. Peut-être que leur éditeur de styles ne supporte pas les variables ? J'ai supprimé la variable CSS que j'avais créée et utilisé des pixels normaux. Le site était toujours cassé. La console ne montre aucune erreur.

Bon ! J'ai supprimé tout mon CSS personnalisé de l'éditeur de styles. Même problème. À ce moment-là, je commence à paniquer. Comment ai-je cassé le site ? Pourquoi le site refusait-il de charger QUELCONQUE style ?

Attendez. Je viens de poser la bonne question. Pourquoi le site ne **chargeait-il** pas mes styles ? J'ai réalisé que je ne savais pas si tous mes CSS personnalisés et ceux de Squarespace étaient intégrés dans le HTML ou s'ils étaient livrés via le réseau.

J'ai inspecté le HTML pour trouver des feuilles de style liées, et j'ai trouvé un suspect dans l'en-tête appelé _site.css_

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-133.png)
_Une feuille de style liée en externe_

J'ai confirmé le coupable lorsque je suis passé à l'onglet Réseau pour voir si la requête vers ce fichier CSS particulier était réussie.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-134.png)

Ce n'était pas le cas. Il retournait une erreur 5xx. Dans la capture d'écran, j'ai manuellement bloqué la requête pour répliquer le problème, donc le statut est différent de l'original, mais l'effet est le même : notre site demande la feuille de style principale de Squarespace et cette requête a échoué, ce qui a cassé le style du site.

Ouf ! J'ai arrêté de paniquer et j'ai retrouvé ma confiance. Ce n'était pas mon erreur, c'était celle de Squarespace.

Pour confirmer, j'ai consulté et visité la page de statut de Squarespace. En effet, leur page de statut indiquait qu'ils rencontraient des problèmes sur leurs serveurs qui, entre autres, empêchaient les styles de se charger pour de nombreux utilisateurs. Je ne pouvais rien faire de plus. J'ai simplement attendu que le problème soit résolu.

Il a fallu 15 **minutes** à Squarespace pour résoudre le problème. J'ai pensé que c'était peut-être un problème rare, et j'ai eu de la chance que cela se produise à une heure très tardive après minuit. J'avais tout faux...

## Nous avions besoin d'une solution

Quelques jours plus tard, mon client a essayé et échoué à me joindre pour m'alerter que le site était, vous l'avez deviné, CASSÉ. Au moment où nous avons pris contact plus tard dans la journée, j'ai découvert que le même problème s'était reproduit. Et cela s'est produit en plein milieu de la journée pendant une période plus longue, proche de **30 minutes.**

Le client a naturellement paniqué et a supprimé tout le CSS personnalisé (heureusement, j'avais une copie locale), et a prié pour le meilleur (tout en pensant probablement que j'avais cassé leur site web et disparu).

Avec le recul, j'aurais dû mieux communiquer et les informer de ce problème lorsque je l'ai rencontré pour la première fois. Ce n'était pas la faute de Squarespace cette fois (même si c'était totalement le cas), c'était la mienne de ne pas avoir trouvé de solution lorsque je l'ai rencontré.

Le problème ici, comme je le voyais, était que nos feuilles de style étaient hébergées sur un serveur qui n'était pas sous notre contrôle. Comment supprimer cette dépendance externe du site web ?

Pour répondre à cette question, je me suis tourné vers le cloud...

## Ma solution initiale AWS

Dans mon développement initial, je mettais mon code CSS personnalisé dans l'éditeur CSS personnalisé de Squarespace. L'éditeur de site acceptait SASS, donc j'ai écrit mes styles en SASS, et j'ai toujours stocké une copie dans un dossier Git local sur ma machine pour avoir une sorte de versioning.

Comme je l'ai mentionné précédemment, les feuilles de style sont hébergées sur les serveurs de Squarespace, donc j'avais besoin de ma propre méthode sans tracas pour héberger ces feuilles de style. J'ai donc imaginé la solution suivante.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-135.png)

Dans ce scénario, moi, le développeur de site web, écrivais mon code sur l'éditeur CSS personnalisé de Squarespace, puis je copiais/collais le SASS sur ma machine locale. Le flux suivant avait alors lieu :

* Je pousse mon code vers CodeCommit
* L'événement de poussée déclenche une fonction Lambda
* La fonction Lambda récupère le dernier fichier SASS et le convertit en une feuille de style CSS.
* La fonction Lambda stocke la feuille de style CSS dans un bucket S3 accessible au public
* Un script en ligne personnalisé sur le site web vérifie si la feuille de style attendue de Squarespace est chargée. Si ce n'est pas le cas, il demande la feuille de style de secours depuis le bucket S3 et l'injecte dans la page.

Et ainsi, j'ai mis en œuvre cette solution aussi rapidement que possible avant que le site ne se casse à nouveau. Le lendemain, le nouveau flux était configuré et fonctionnait comme prévu.

### Comment configurer le déclencheur CodeCommit

Après avoir poussé le code vers mon dépôt CodeCommit, je suis allé dans les paramètres du dépôt, puis dans l'onglet Déclencheurs, et j'ai cliqué sur le bouton "Créer un déclencheur".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-136.png)

J'ai nommé le déclencheur, sélectionné "Push to existing branch" comme type d'événement, et master comme ma branche à écouter. Ensuite, j'ai sélectionné AWS Lambda comme service à utiliser, et j'ai pointé vers ma fonction Lambda, puis j'ai créé le déclencheur.

Cette Lambda s'exécute maintenant juste après que du code est poussé vers la branche master sur CodeCommit.

### Logique Lambda

Voici le code JS pour la lambda invoquée :

```js
const {
    S3,
    CodeCommit,
} = require('aws-sdk')
const sass = require('node-sass');

const getFileFromCodeCommit = (filePath) => new Promise((resolve, reject) => {
    const ccClient = new CodeCommit({ region: "us-east-1" })
    const ccParams = {
        filePath,
        repositoryName: 'mebbels-assets'
    }

    ccClient.getFile(ccParams, (err, data) => {
        if (err) reject(err)
        console.log(data)
        let stringData = new TextDecoder().decode(data.fileContent);
        resolve(stringData)
    })

})

const sendStylesheetToS3 = (fileData, fileName) => new Promise((resolve, reject) => {
    const s3Client = new S3({ region: "eu-south-1" })
    let putObjectBody = {
        Bucket: 'mebbels-assets',
        Key: fileName,
        ACL: 'public-read',
        Body: fileData,
        ContentType: 'text/css'
    }
    s3Client.putObject(putObjectBody, (err, data) => {
        if (err) reject(err)
        resolve(data)
    })
})

const processSASS = (fileData) => new Promise((resolve, reject) => {
    sass.render({
        data: fileData
    }, (err, data) => {
        if (err) reject(err)
        resolve(data)
    })
})
exports.handler = async (event) => {
    const sassFile = await getFileFromCodeCommit('mebbels-sass.scss')
    const processedSass = await processSASS(sassFile)
    await sendStylesheetToS3(processedSass.css, 'fallbackStyles.css')
    const response = {
        statusCode: 200,
        body: JSON.stringify("Done"),
    };

    return response;
};

```

En bref, il récupère la feuille de style SASS (mebbels-sass.scss), la convertit en CSS en utilisant le package node-sass, puis place le fichier CSS de sortie dans un bucket S3 public.

Bien sûr, pour que cette lambda s'exécute sans problèmes liés à l'accès à nos ressources sur CodeCommit et S3, elle a besoin des bonnes permissions.

Voici la politique de rôle IAM attachée à la fonction :

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "codecommit:GitPull",
                "s3:PutObjectAcl",
                "codecommit:GetFile"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::mebbels-assets",
                "arn:aws:codecommit:us-east-1:6653912857032:mebbels-assets"
            ]
        }
    ]
}

```

### Comment configurer le bucket S3 :

Le bucket S3 cible qui stockera les feuilles de style CSS de secours doit être public. Je me suis assuré qu'il l'était lors de la création du bucket, et j'ai vérifié une deuxième fois dans l'onglet "Permissions" de mon bucket S3 dans la section Bloquer l'accès public :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-137.png)

Le bucket doit également avoir le [CORS activé](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/cors.html) et configuré, car nous allons le demander depuis un domaine différent, à savoir [mebbels.com](http://mebbels.com).

Dans le même onglet "Permissions", sous la section Partage de ressources cross-origin (CORS), j'ai ajouté la configuration CORS suivante :

```json
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "https://www.mebbels.com"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]

```

## Script du site

Et enfin, voici le petit script en ligne dans l'en-tête du site qui vérifie l'état de chargement de la feuille de style demandée à Squarespace. Si elle n'est pas chargée après 20 millisecondes, le script injecte un lien dans l'en-tête de notre site vers notre style de secours hébergé dans notre bucket S3.

```js
var isSiteCssLoaded = false;
var siteCssLink = document.querySelector("link[href*='/site.css']")
siteCssLink.addEventListener('load', () => {
    console.log('site.css loaded')
    isSiteCssLoaded = true;
})

const fallBackIfNeeded = () => {
    if (!isSiteCssLoaded) {
        console.log('site.css not loaded')
        var headID = document.getElementsByTagName('head')[0];
        var link = document.createElement('link');
        link.type = 'text/css';
        link.rel = 'stylesheet';
        link.href = '<https://mebbels-assets.s3.eu-south-1.amazonaws.com/fallbackStyles.css>'
        headID.appendChild(link);
		console.log('fallback styles loaded')
    }
}
setTimeout(fallBackIfNeeded, 20)

```

## Comment tester cette solution

Eh bien, je ne pouvais pas attendre que les serveurs de Squarespace se détraquent à nouveau pour tester ma solution. Voici comment je l'ai testée.

Comme je l'ai suggéré au début de l'article, je peux simuler une requête échouée pour récupérer la feuille de style de notre site depuis Squarespace en allant dans l'onglet Réseau du navigateur (en m'assurant de désactiver le cache pour éviter les feuilles de style en cache), puis en bloquant l'URL de la requête CSS :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-138.png)

Après avoir cliqué sur "Bloquer l'URL de la requête" et rafraîchi la page, nous devrions voir mon script se déclencher après 20 millisecondes. Et il devrait afficher "site.css not loaded" et "fallback styles loaded" dans la console, puis ajouter notre feuille de style de secours depuis S3. Et le site devrait fonctionner sans se casser !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-140.png)

## Une meilleure solution

Franchement, j'étais assez fier de cette solution rapide et la voir fonctionner était un plaisir. C'est une option peu coûteuse et sans serveur qui n'est pas trop compliquée.

Mais cette solution _est_ plus compliquée qu'elle ne devrait l'être. Et elle n'est pas sans ses inconvénients.

L'inconvénient de cette solution est que le style de secours dépend toujours du développeur web pour maintenir les styles de secours dans le dépôt CodeCommit à jour en permanence.

De plus, il y a d'autres utilisateurs administrateurs du site (comme les designers) qui modifient parfois eux-mêmes les styles personnalisés du site. Donc cette solution repose sur une communication parfaite entre les membres de l'équipe pour informer le développeur ayant accès à AWS des changements personnalisés afin qu'il puisse mettre à jour le dépôt.

Alors que je lisais davantage sur les services AWS disponibles, je suis tombé sur un service génial appelé [CloudWatch Events](https://docs.amazonaws.cn/en_us/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html). Ce service vous permet de déclencher des flux de travail dans votre compte AWS en fonction de métriques surveillées OU sur une base planifiée.

J'ai donc décidé d'utiliser CloudWatch Events comme un cronjob sans serveur qui déclenche une fonction Lambda qui scrape la feuille de style de notre site web quotidiennement et la stocke dans le bucket S3.

La solution modifiée ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-142.png)

Dans ce flux modifié, nous avons supprimé la dépendance au développeur web pour mettre à jour manuellement la feuille de style et pousser vers CodeCommit pour que les styles de secours soient créés.

Dans ce cas, nous avons un événement CloudWatch planifié quotidiennement qui déclenche une fonction Lambda.

Notre fonction Lambda scrape ensuite notre site web pour les feuilles de style liées en externe, les fusionne en un seul fichier CSS de secours et le stocke dans le bucket S3 accessible au public. Le script du site web reste le même car il vérifie les feuilles de style par défaut et les demande depuis notre bucket S3 si elles ne sont pas trouvées.

### Code Lambda

Commençons par la nouvelle fonction lambda.

```python
import sys, os
import urllib.request as req
from bs4 import BeautifulSoup
import logging
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    fallback_css_filename = 'fallbackStyles.css'
    fallback_css_path = '/tmp/' + fallback_css_filename
    url = '<https://www.mebbels.com>'
    
    html = req.urlopen(url) # request the initial page
    soup = BeautifulSoup(html, 'html.parser') 
    fallback_styles = open(fallback_css_path, 'ab')
    
    for link in soup.find_all('link', type='text/css'): # get links to external style sheets
        address = link['href'] # the address of the stylesheet
        if address.startswith('/'): # relative link
            address = url + address
        css_file_name, headers = req.urlretrieve(address) # make a request to download the stylesheet from the address, returns bytes
        css = open(css_file_name, 'rb')
        fallback_styles.write(css.read())
        css.close()
    
    try:
        s3_client.upload_file(
            fallback_css_path,
            'mebbels-assets',
            fallback_css_filename,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': 'text/css'
                }
        )
        return True
    except ClientError as e:
        logging.error(e)
        return False

```

Dans cette lambda, j'utilise la bibliothèque BeautifulSoup pour scraper notre site web. Je télécharge chaque feuille de style liée en externe et je les écris dans un fichier dans le dossier temporaire (AWS Lambdas vous permet de stocker des fichiers temporairement dans un dossier appelé 'tmp' pendant l'exécution).

Après avoir écrit tous les styles dans un seul fichier fallbackStyles.css, je l'ai téléchargé dans notre bucket S3 en utilisant le SDK AWS comme avant.

Mais contrairement à avant, j'ai maintenant sauvegardé TOUTE feuille de style liée en externe, donc je pourrais sauvegarder une feuille de style Google Fonts liée en externe ou un CDN CSS Bootstrap, par exemple.

## Comment utiliser les événements CloudWatch planifiés

C'était un nouveau service pour moi que j'étais très excité d'essayer dans un cas d'utilisation pratique comme celui-ci. C'est incroyable à quel point il est simple et facile à utiliser, avec seulement deux étapes.

Dans la console AWS, sous CloudWatch > Events > Rules, j'ai créé une nouvelle règle et défini mes paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-143.png)

Dans la section Source de l'événement, j'ai choisi l'option "Schedule" et choisi une période de 6 heures. Cela signifiait que cet événement serait déclenché automatiquement et de manière cohérente toutes les six heures. Il y a même une option pour une expression cron personnalisée si vous voulez un intervalle personnalisé très spécifique.

Mais que fait cet événement ? Nous devons lui dire cela dans la section Cibles. J'ai choisi "Lambda function" dans la liste déroulante et sélectionné ma fonction Lambda disponible. Ensuite, j'ai cliqué sur "Configure details" pour avancer.

Dans l'étape suivante et dernière, j'ai simplement entré le nom et la description de la règle d'événement que j'ai créée.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-144.png)

Heureusement, cet écran a répondu à une question brûlante que j'avais sur les permissions : "Cet événement sera-t-il autorisé à déclencher ma fonction Lambda ? Ou devrais-je lui attribuer un rôle IAM ?"

Et, comme le montre la capture d'écran, CloudWatch gère complètement l'attribution de la permission requise pour que l'événement fonctionne sur sa cible, donc je n'ai pas eu à m'inquiéter du travail supplémentaire et des tests.

# Mots finaux

J'espère que cet article vous a été utile d'une manière ou d'une autre, que vous soyez intéressé par le développement cloud, les créateurs de sites web, ou simplement la programmation en général.

Si vous possédez et gérez un site web Squarespace (ou tout autre créateur de sites web) qui s'est mystérieusement cassé et que vous lisez ceci en mode panique, je vous conseille de visiter leur page de statut pour les mises à jour. Les pannes comme celles-ci sont généralement résolues en moins d'une heure.

Je prévois de construire une application web native cloud qui mettra en œuvre et automatisera cette solution afin de pouvoir l'offrir à mes futurs et actuels clients. Vous pouvez me suivre pour les mises à jour alors que je la construis en public. 👨‍💻

Pour plus de conseils et d'informations sur le cloud et le développement web, suivez-moi sur Twitter [@adham_benhawy](https://twitter.com/adham_benhawy).