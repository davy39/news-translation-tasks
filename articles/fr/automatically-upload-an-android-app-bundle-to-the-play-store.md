---
title: Comment télécharger automatiquement un Android App Bundle vers le Play Store
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-06T21:08:39.000Z'
originalURL: https://freecodecamp.org/news/automatically-upload-an-android-app-bundle-to-the-play-store
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-lisa-1092644.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: automation
  slug: automation
seo_title: Comment télécharger automatiquement un Android App Bundle vers le Play
  Store
seo_desc: "By Zaid Humayun\nIn this article, I'm going to explain how to automatically\
  \ upload an Android App Bundle (.aab file) to the Play Store's beta track. We'll\
  \ use Android Studio and AWS as a cloud infrastructure provider. \nOnce we've uploaded\
  \ the app bund..."
---

Par Zaid Humayun

Dans cet article, je vais expliquer comment télécharger automatiquement un Android App Bundle (fichier .aab) vers la piste bêta du Play Store. Nous utiliserons Android Studio et AWS comme fournisseur d'infrastructure cloud. 

Une fois que nous aurons téléchargé l'app bundle, nous déclencherons une notification Slack.

C'est une utilisation précieuse de votre temps pour plusieurs raisons, comme la création d'observabilité et la priorisation des processus.

## Technologies que nous utiliserons

Voici les ressources que nous allons utiliser pour ce tutoriel :

1. Android Studio
2. AWS CodeBuild
3. AWS Lambda
4. S3
5. Slack

## Aperçu général du projet

![beta_track_upload_flow-1](https://www.freecodecamp.org/news/content/images/2021/07/beta_track_upload_flow-1.jpg)

L'image ci-dessus vous montre un aperçu général de la manière dont nous structurerons l'ensemble.

Essentiellement, il faut configurer un Code Pipeline sur AWS pour votre dépôt Android. Ce Code Pipeline aura Code Build comme l'une de ses étapes.

Pousser vers la branche master de votre dépôt d'application Android déclenchera Code Build. Le projet Code Build signera l'application Android depuis la ligne de commande et téléchargera l'artefact vers un bucket S3.

Le téléchargement du bundle vers S3 déclenchera un Lambda, qui téléchargera le bundle et le téléchargera vers le Play Store en utilisant l'API Google Publishing. Une fois qu'il reçoit une réponse 200, le Lambda déclenchera alors une notification Slack.

## Comment obtenir votre clé de compte de service Google Play

Pour pouvoir utiliser l'API Google Play Publisher, vous aurez besoin d'une clé de compte de service Google Play.

Un compte de service est un compte qui peut agir en votre nom lorsque les serveurs communiquent entre eux. Vous pouvez en savoir plus sur la manière dont Google utilise OAuth2.0 pour la communication serveur à serveur [ici](https://developers.google.com/identity/protocols/oauth2/service-account).

Pour savoir comment créer un compte de service et lui donner accès à l'API Google Play Publisher, consultez [ici](https://developers.google.com/identity/protocols/oauth2/service-account).

Une fois que vous avez créé votre compte de service et lui avez donné les autorisations appropriées, assurez-vous de télécharger la clé du compte de service et de la garder en sécurité. Vous allez bientôt télécharger cela vers un bucket S3.

## Comment signer le bundle Android

La principale chose à comprendre est comment signer l'Android App Bundle. Google a une documentation assez décente à ce sujet que vous pouvez trouver [ici](https://developer.android.com/studio/build/building-cmdline#sign_cmdline).

Je vais résumer les liens ci-dessous.

Générez une clé privée en utilisant `keytool` comme ceci :

```bash
keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
```

Vous pouvez appeler votre clé comme vous le souhaitez. Ici, je l'ai appelée `my-release-key.jks`. Vous pouvez également choisir l'alias que vous voulez. Tout au long de ce tutoriel, assurez-vous d'utiliser le nom et l'alias corrects pour votre clé.

Ouvrez `build.gradle` dans votre répertoire `app` dans Android Studio et ajoutez le bloc de code suivant :

```bash
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            // Vous devez spécifier soit un chemin absolu, soit inclure le
            // fichier keystore dans le même répertoire que le fichier build.gradle.
            storeFile file("my-release-key.jks")
            storePassword "password"
            keyAlias "my-alias"
            keyPassword "password"
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            ...
        }
    }
}
```

Si vous avez changé le nom de votre clé de release en autre chose que par défaut, assurez-vous de spécifier le nouveau nom. Même chose pour l'alias.

Votre mot de passe de magasin sera celui que vous avez généré lorsque vous avez téléchargé votre application pour la première fois sur le Play Store.

Maintenant, lorsque vous exécutez la commande `./gradlew :app:bundleRelease` depuis la ligne de commande dans Android Studio, vous remarquerez qu'elle génère un App Bundle signé.

## Comment nettoyer les informations de signature

Commettre du code avec les informations de signature disponibles en texte brut dans le fichier `build.gradle` est un risque de sécurité et pourrait être un vecteur d'attaque.

Google a une documentation à ce sujet que vous pouvez trouver [ici](https://developer.android.com/studio/publish/app-signing#secure-shared-keystore).

Tout d'abord, créez un fichier `keystore.properties` à la racine de votre répertoire de projet.

Le contenu du fichier doit être comme suit :

```text
storePassword=myStorePassword
keyPassword=myKeyPassword
keyAlias=myKeyAlias
storeFile=myStoreFileLocation
```

Votre mot de passe de magasin et votre mot de passe de clé seront le mot de passe que vous avez utilisé lorsque vous avez téléchargé votre bundle d'application vers l'App Store pour la première fois.

Votre `keyAlias` et `storeFile` seront l'alias que vous avez assigné lors de la création de votre clé privée et l'emplacement de la clé privée que vous avez créée, respectivement.

Maintenant, nous devons charger ce fichier dans `build.gradle`. Cela m'a surpris au début, mais Gradle fonctionne en réalité comme un DSL. Cela facilite donc l'écriture de la configuration en utilisant Gradle.

```gradle
//  Charger les propriétés depuis keystore.properties
def keystorePropertiesFile = rootProject.file("keystore.properties")

//  Créer un nouvel objet Properties()
def keystoreProperties = new Properties()

//  Si keystorePropertiesFile existe, lire depuis celui-ci, sinon définir depuis l'environnement de build
if (keystorePropertiesFile.exists()) {
    //  Charger le fichier keystoreProperties
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
} else {
    //  Lire toutes les variables d'environnement depuis l'environnement de build
    keystoreProperties.setProperty("storeFile", "${System.getenv('STORE_FILE')}")
    keystoreProperties.setProperty("keyAlias", "${System.getenv('KEY_ALIAS')}")
    keystoreProperties.setProperty("keyPassword", "${System.getenv('KEY_PASSWORD')}")
    keystoreProperties.setProperty("storePassword", "${System.getenv('STORE_PASSWORD')}")
}
```

Vous remarquerez la condition if dans ce code – ne vous en souciez pas pour l'instant. Elle est là spécifiquement pour tenir compte de Code Build plus tard.

Une fois que vous avez fait cela, changez votre section `signingConfigs` dans `build.gradle` pour qu'elle ressemble à ceci :

```gradle
signingConfigs {
        release {
            storeFile file(keystoreProperties['storeFile'])
            keyAlias keystoreProperties['keyAlias']
            keyPassword keystoreProperties['keyPassword']
            storePassword keystoreProperties['storePassword']
        }
    }
```

## Comment configurer AWS Code Pipeline

Je ne vais pas entrer dans trop de détails sur celui-ci car c'est relativement simple.

Configurez un AWS Code Pipeline avec les trois étapes suivantes :

1. Étape de source connectée à la branche `master` de votre dépôt GitHub
2. Étape de build connectée à AWS Code Build
3. Étape de déploiement qui déploiera vers un bucket S3.

Vous pouvez trouver plus de documentation sur la configuration d'un Code Pipeline [ici](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html).

## Comment configurer AWS S3

Tout d'abord, assurez-vous d'avoir un Code Pipeline configuré avec Code Build comme l'une des étapes. Ensuite, configurez deux buckets S3 :

1. Un bucket pour stocker votre clé de release. J'appelle ce bucket `release-key.jks`
2. Un bucket dans lequel vous stockerez votre clé privée de compte de service Google Play. (Vous devriez avoir téléchargé cette clé lors de la création de votre compte de service.)

Vous devrez autoriser l'accès à ces buckets depuis votre rôle de service Code Build. Votre rôle de service Code Build devrait avoir été créé lorsque vous avez configuré votre Code Pipeline.

Rendez-vous sur la console IAM et trouvez votre rôle de service Code Build et récupérez l'ARN.

Ensuite, utilisez la console pour accéder à l'onglet Autorisations pour le bucket `release-key.jks` et ajoutez la politique suivante :

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789:role/service-role/codebuild-service-role-dummy",
                ]
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::release-key-bucket/*"
        }
    ]
}
```

Cette politique permettra l'accès au bucket S3 depuis la machine où votre projet CodeBuild sera exécuté.

Vous devrez remplacer les ARN mentionnés ci-dessus par les ARN de votre compte. Assurez-vous de spécifier l'ARN correct pour le rôle de service Code Build lorsque vous mettez à jour la politique.

Vous n'avez pas besoin de changer la politique des autorisations pour le deuxième bucket. Nous ajouterons les autorisations pertinentes au rôle AWS Lambda pour lui permettre d'accéder au bucket.

## Comment configurer AWS CodeBuild

Ensuite, créez un fichier `buildspec.yml` dans le dossier racine de votre projet.

```yaml
version: 0.2

phases:
  build:
    commands:
      - aws s3api get-object --bucket release-key.jks --key release-key.jks ./releaseKey.jks
      - cp ./releaseKey.jks ${CODEBUILD_SRC_DIR}/app/releaseKey.jks
      - export STORE_FILE=releaseKey.jks
      - export KEY_ALIAS=$keyAlias
      - export KEY_PASSWORD=$keyPassword
      - export STORE_PASSWORD=$storePassword
      - ./gradlew :app:bundleRelease

artifacts:
  files:
    - app/build/outputs/bundle/release/app-release.aab
```

Ce fichier est assez simple. Il récupère la clé de release depuis le bucket spécifié et l'enregistre dans un fichier local sur le serveur Code Build à l'emplacement spécifié.

Ensuite, exportez toutes les variables requises pour que la configuration `build.gradle` fonctionne correctement. Enfin, exécutez la commande de release de Gradle depuis la ligne de commande.

Avant de pouvoir exécuter ce script dans Code Build, vous devrez ajouter les variables à l'environnement Code Build. Pour ce faire, allez d'abord sur la console AWS Code Build et choisissez votre projet de build pour votre application Android.

Ensuite, sélectionnez Modifier > Environnement comme dans la capture d'écran ci-dessous :

![](https://www.freecodecamp.org/news/assets/img/aws_code_build_menu_screenshot.png)

Sur l'écran qui s'affiche une fois que vous avez fait cela, sélectionnez le menu déroulant Configuration supplémentaire. Vous y verrez une option pour ajouter des variables d'environnement via des paires clé-valeur.

Maintenant, lorsque Code Build exécute le fichier `buildspec.yml`, il pourra exporter les variables spécifiées.

En l'état actuel des choses, lorsque votre pipeline s'exécute, Code Build pourra télécharger la clé privée pour signer et construire votre application Android et télécharger le bundle signé vers un bucket S3.

## Comment configurer l'application Slack

L'observabilité est une caractéristique de l'automatisation. Vous voulez savoir quand votre automatisation s'exécute, si elle réussit ou échoue, et si elle échoue, la raison de l'échec.

La manière dont AWS gère généralement l'observabilité est via CloudWatch. Mais je pense qu'une intégration Slack remplit tout aussi bien le but.

La manière la plus simple d'intégrer Slack dans vos flux de travail d'automatisation est de configurer une application Slack et d'envoyer une notification à cette application depuis votre flux de travail d'automatisation.

Pour apprendre comment configurer une application Slack, consultez la documentation [ici](https://api.slack.com/start/overview). Le processus est super facile et vous devriez avoir une application opérationnelle en quelques minutes. 

Une fois que vous avez créé l'application, vous obtiendrez une URL de WebHook que vous pourrez utiliser pour appeler l'application et publier dans le canal pertinent. Gardez une trace de cette URL de WebHook car nous l'utiliserons avec la fonction AWS Lambda.

## Comment configurer AWS Lambda

Jusqu'à présent, nous avons un Android App Bundle qui est signé, construit et téléchargé vers un bucket S3. Ensuite, nous devons comprendre comment télécharger le bundle vers la piste bêta du Play Store.

La manière de faire cela est de configurer un AWS Lambda qui sera déclenché lorsque le bundle est téléchargé vers le bucket S3. Lorsque ce déclencheur se produit, le Lambda s'exécutera, téléchargera le bundle, récupérera la clé du compte de service et téléchargera le bundle vers la piste bêta du Play Store.

Une fois que vous avez créé un Lambda et ajouté un déclencheur pour l'exécuter lorsqu'un fichier est téléchargé vers le bucket, regardez le code ci-dessous :

```python
"""Ce script Python3 est utilisé pour télécharger un nouveau bundle .aab vers le play store. L'exécution de ce script Python
    se fait via un AWS Lambda qui est invoqué lorsqu'un nouveau fichier est téléchargé vers les buckets S3 pertinents"""

import json
import boto3
import os
from urllib import request, parse
from google.oauth2 import service_account
import googleapiclient.discovery

#   Définir la portée de la demande d'autorisation
SCOPES = ['https://www.googleapis.com/auth/androidpublisher']

#   Nom du package pour l'application
package_name = 'com.app.name'

#   Définir l'URL du webhook Slack
slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

def send_slack_message(message):
    data = json.dumps({ 'text': message })
    post_data = data.encode('utf-8')
    req = request.Request(slack_webhook_url, data=post_data, headers={ 'Content-Type': 'application/json' })
    request.urlopen(req)

#   C'est la fonction principale de gestion
def lambda_handler(event, context):
    #   Créer un nouveau client S3 et télécharger le bon fichier depuis le bucket
    s3 = boto3.client('s3')
    s3.download_file('service-account-bucket-key', 'service-account-bucket-key.json', '/tmp/service-account-key.json')
    SERVICE_ACCOUNT_FILE = '/tmp/service-account-key.json'

    #   Télécharger le fichier app-release.aab qui a déclenché le Lambda
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    s3.download_file(bucket_name, file_key, '/tmp/app-release.aab')
    APP_BUNDLE = '/tmp/app-release.aab'

    print(f"Un bundle téléchargé vers {bucket_name} a déclenché le Lambda")

    #   Créer un objet d'identifiants et créer un objet de service en utilisant l'objet d'identifiants
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = googleapiclient.discovery.build('androidpublisher', 'v3', credentials=credentials, cache_discovery=False)
    
    #   Créer une demande de modification en utilisant l'objet de service et obtenir l'editId
    edit_request = service.edits().insert(body={}, packageName=package_name)
    result = edit_request.execute()
    edit_id = result['id']

    #   Créer une demande pour télécharger le bundle de l'application
    try:
        bundle_response = service.edits().bundles().upload(
            editId=edit_id,
            packageName=package_name,
            media_body=APP_BUNDLE,
            media_mime_type="application/octet-stream"
        ).execute()
    except Exception as err:
        message = f"Il y a eu une erreur lors du téléchargement d'une nouvelle version de {package_name}"
        send_slack_message(message)
        raise err

    print(f"Le code de version {bundle_response['versionCode']} a été téléchargé")

    #   Créer une demande de piste pour télécharger le bundle vers la piste bêta
    track_response = service.edits().tracks().update(
        editId=edit_id,
        track='beta',
        packageName=package_name,
        body={u'releases': [{
            u'versionCodes': [str(bundle_response['versionCode'])],
            u'status': u'completed',
        }]}
    ).execute()

    print("Le bundle a été commis vers la piste bêta")

    #   Créer une demande de commit pour commiter la modification vers la piste BETA
    commit_request = service.edits().commit(
        editId=edit_id,
        packageName=package_name
    ).execute()

    print(f"La modification {commit_request['id']} a été commise")

    message = f"Le code de version {bundle_response['versionCode']} a été téléchargé depuis le bucket {bucket_name}.\nLa modification {commit_request['id']} a été commise"
    send_slack_message(message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Exécution réussie de la publication du bundle de l'application vers la bêta')
    }
```

Le Lambda ci-dessus utilisera la bibliothèque `googleapiclient` et son module de découverte pour construire l'URL de l'API de publication de Google Play. 

Ensuite, le Lambda téléchargera la clé du compte de service depuis le bucket que vous avez configuré précédemment. Vous devrez vous assurer de spécifier les noms de bucket corrects.

Selon que le téléchargement réussit ou échoue, nous voulons qu'un message Slack soit envoyé. Ajoutez l'URL du WebHook Slack de la section précédente dans les variables d'environnement pour le Lambda. La fonction ci-dessus utilise le module `os` de Python pour accéder à la variable d'environnement et publier le message sur Slack.

Si votre Lambda échoue, cela peut être dû au fait que votre Lambda n'a pas les autorisations pour accéder au bucket S3 où la clé de votre compte de service Google Play est stockée. Dans ce cas, vous verrez un message d'erreur indiquant cela. 

Pour corriger cela, vous devez simplement ajouter les autorisations pertinentes à votre rôle Lambda.

Voici la politique que vous devrez ajouter :

```json
{
    "Version": "2012-10-07",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObjectVersion",
                "s3:GetBucketVersioning",
                "s3:GetBucketAcl",
                "s3:GetObject",
                "s3:GetBucketTagging",
                "s3:GetBucketLocation",
                "s3:GetObjectVersionAcl"
            ],
            "Resource": [
                "arn:aws:s3:::arn:aws:s3:::your-bucket-name-with-service-account-key"
            ]
        }
    ]
}
```

Remplacez l'ARN du bucket par celui pertinent pour votre compte et vous devriez être prêt à partir.

## Conclusion

Donc, voilà. Ce n'était définitivement pas facile et il y a beaucoup de pièces mobiles, mais c'est une automatisation qui vous fera gagner beaucoup de temps et d'efforts. 

Si vous faites partie d'une équipe qui publie fréquemment de nouvelles mises à jour d'applications, vous ne voulez pas être entravé par l'absence d'une personne dont le travail est de publier la mise à jour.

Construire ce type d'automatisation rend votre flux de travail CI/CD beaucoup plus fluide et plus robuste.

Si vous êtes intéressé par des blogs comme celui-ci, vous pouvez en lire plus sur https://redixhumayun.github.io ou me suivre sur Twitter.