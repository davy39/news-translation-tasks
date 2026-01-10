---
title: Comment commencer avec l'architecture Serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-18T01:09:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-serverless-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/serverless-cover-1.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: serverless
  slug: serverless
seo_title: Comment commencer avec l'architecture Serverless
seo_desc: 'By Anirban Das

  Traditionally, when you wanted to build a web app or API, you’d usually have to
  spend significant time and effort managing servers and ensuring your app scales
  up to handle large request volumes. Serverless is a cloud computing model w...'
---

Par Anirban Das

Traditionnellement, lorsque vous souhaitiez créer une application web ou une API, vous deviez généralement passer beaucoup de temps et d'efforts à gérer des serveurs et à vous assurer que votre application pouvait monter en charge pour gérer de grands volumes de requêtes. Le Serverless est un modèle de cloud computing qui vous permet d'exécuter des applications sans avoir à vous soucier de la gestion et de la mise à l'échelle des serveurs.

Tout ce que vous avez à faire est de télécharger votre code vers le service d'un fournisseur cloud, et ils provisionnent automatiquement un environnement éphémère. Contrairement aux architectures traditionnelles, il peut monter en charge pour gérer des milliers de requêtes en un instant, et vous ne payez que pour la durée pendant laquelle votre code s'exécute.

Dans cet article, nous allons créer un simple formulaire de contact alimenté par l'offre serverless d'AWS (Amazon Web Services), Lambda. Cependant, le serverless convient aux applications de toute complexité ou taille. Par exemple, nous avons construit [myCompiler](https://www.mycompiler.io/) — un terrain de jeu de programmation qui supporte 20 langages — et il est largement alimenté par le serverless.

Avant de commencer, nous allons examiner de plus près comment fonctionnent le serverless et Lambda, ainsi que l'architecture que nous allons mettre en place pour notre formulaire de contact. De plus, à la fin de cet article, nous examinerons quelques outils qui sont destinés à aider à la construction et au déploiement de grandes applications serverless.

Vous aurez besoin d'un compte AWS pour suivre ce guide, et [vous pouvez vous inscrire ici](https://portal.aws.amazon.com/billing/signup). Notre utilisation d'AWS pour ce guide sera entièrement couverte par le niveau gratuit.

## Comment fonctionne AWS Lambda ?

Dans cette section, nous allons comprendre le flux de travail avec Lambda et une brève compréhension de son fonctionnement. Cependant, ces concepts s'appliquent également aux offres serverless de la plupart des autres fournisseurs cloud.

Avec Lambda, vous téléchargez votre code vers AWS, qui est généralement un script écrit en Python, Node.js ou Ruby. Dans le cas d'un langage tel que Go, Java ou C#, il s'agit d'un exécutable Linux ou d'un package au format du langage (comme les fichiers jar pour Java).

Après avoir téléchargé votre code, vous pouvez ensuite l'"invoquer" manuellement ou utiliser un autre service AWS à cette fin (nous verrons cela en détail dans un instant). Lorsque vous invoquez votre code, Lambda crée un environnement Linux sécurisé et éphémère appelé "conteneur" sur l'un de leurs serveurs, et toutes les données que vous avez passées dans le cadre de l'invocation sont transmises à votre fonction.

Une fois que la fonction a terminé son exécution, le service Lambda retourne les résultats du code à son appelant. Le conteneur peut ensuite être réutilisé pour servir une autre exécution, ou si la fonction n'a pas été invoquée depuis longtemps, le conteneur est détruit.

Lorsque vous effectuez des invocations parallèles, Lambda crée un conteneur pour servir chaque invocation. Parce que chaque invocation est dédiée à un seul conteneur, chaque invocation obtient des ressources amples pour l'exécution. Vous pouvez attribuer de 128 Mo à 3 Go de mémoire à chaque invocation, ainsi que des CPU qui augmentent avec la mémoire. Combinez cela avec le fait qu'il peut servir jusqu'à 1000 invocations parallèles (ceci peut être augmenté en contactant AWS), vous pouvez gérer des charges de travail lourdes sans avoir à vous soucier de la mise à l'échelle.

Alors, avec les préoccupations de mise à l'échelle écartées, combien coûte l'exécution d'AWS Lambda ? L'utilisation de Lambda est mesurée en utilisant les paramètres suivants : le nombre de requêtes, la mémoire allouée et le nombre de millisecondes que vos fonctions prennent pour s'exécuter.

Si vous choisissez la plus petite taille de mémoire (128 Mo), et que vos fonctions prennent 1 seconde pour s'exécuter lorsque vous les invoquez, vous pouvez invoquer votre fonction jusqu'à un million de fois gratuitement. Après cela, chaque million d'invocations peut coûter jusqu'à 2,30 $. Une taille de mémoire de 128 Mo peut sembler minuscule, mais elle est certainement suffisante pour gérer de nombreux types de charges de travail.

## API Gateway — Servir des requêtes HTTP avec Lambda

Comme nous l'avons mentionné précédemment, une fois que vous avez téléchargé votre code, vous devez l'invoquer manuellement. Pour créer une application web, vous auriez besoin d'un serveur qui écoute les requêtes HTTP, invoque votre fonction avec les détails de la requête, et traduit les données retournées par votre fonction en une réponse HTTP.

AWS dispose d'un autre service qui vous permet de faire exactement cela — API Gateway. Tout comme Lambda, il s'agit d'un autre service géré par AWS qui peut automatiquement monter en charge pour gérer des volumes de requêtes extrêmement élevés.

Une fois que vous avez créé une API Gateway, vous obtiendrez une URL de base qui ressemble à ceci :
`https://abcdefgh.execute-api.us-east-1.amazonaws.com/`

Sous cette URL de base, vous pouvez mapper des chemins et des méthodes de requête (comme GET ou POST) à vos fonctions. Vous avez également la possibilité de créer votre propre domaine si vous souhaitez utiliser autre chose que le domaine par défaut, mais nous n'aborderons pas cela dans ce guide.

De plus, tout comme Lambda, le prix de l'API Gateway est également intéressant — vous pouvez servir jusqu'à un million de requêtes gratuitement, et après cela, chaque million de requêtes vous coûte 1 $.

## Création d'un formulaire de contact

Nous allons créer un simple formulaire de contact qui nous envoie un email contenant les détails que notre utilisateur remplit. Voici comment nous allons construire les différentes parties du formulaire de contact :

1. Tout d'abord, nous allons configurer SES (Simple Email Service), l'offre d'email d'AWS. Cela nous aidera à envoyer des emails pour le formulaire de contact.
2. Ensuite, nous allons configurer un "rôle" pour Lambda, puis créer une fonction Lambda qui reçoit la requête HTTP et nous envoie un email.
3. Nous allons configurer API Gateway et le mapper à la fonction que nous avons créée à l'étape 2.
4. Nous allons ensuite configurer une page web qui interagit avec le point de terminaison API Gateway et soumet les détails remplis par l'utilisateur.

À la fin de ce guide, vous aurez configuré quelque chose qui fonctionne comme ceci :

![Application Serverless](https://www.freecodecamp.org/news/content/images/2020/03/serverless-app.png)

Pour commencer, visitez la [console de gestion AWS](http://console.aws.amazon.com/) (ou simplement, la "console") et connectez-vous avec les détails que vous avez utilisés pour vous inscrire. Une fois connecté, vous pouvez utiliser le menu déroulant "Services" dans la barre de navigation pour basculer entre les différents services que nous allons utiliser.

![Console de gestion AWS](https://www.freecodecamp.org/news/content/images/2020/03/AWS-management-console.png)

## Configuration de SES pour l'envoi d'emails

Commencez par visiter la section SES (Simple Email Service) de la console via le menu déroulant "Services", ou en utilisant ce [lien direct](https://console.aws.amazon.com/ses/home). Ensuite, cliquez sur la section "Adresses email" à gauche. Vous serez accueilli avec cette page :

![AWS SES](https://www.freecodecamp.org/news/content/images/2020/03/AWS-SES.png)

Cliquez sur le bouton "Vérifier une nouvelle adresse email" puis entrez votre adresse email, et cliquez sur "Vérifier cette adresse email". Vous recevrez un email avec un lien de vérification. Ouvrez-le pour vérifier l'adresse, puis actualisez la page de la console SES. Vous verrez que l'adresse email a été vérifiée :

![AWS SES vérifier l'adresse email](https://www.freecodecamp.org/news/content/images/2020/03/AWS-SES-verify-email-address.png)

À ce stade, vous pourrez envoyer des emails pour votre adresse email en utilisant SES.

## Configuration d'un rôle pour la fonction Lambda

Dans AWS, la plupart des choses commencent sans aucune permission pour interagir avec d'autres ressources ou services dans votre compte AWS, sauf si vous leur donnez des permissions explicites pour le faire.

Cela signifie que notre fonction Lambda ne pourra pas communiquer avec des services tels que SES pour envoyer des emails. Lambda utilise quelque chose appelé un "rôle" pour définir le niveau d'accès qu'il a aux autres services. Donc, dans cette section, nous allons configurer un rôle pour notre fonction avec accès à SES et [CloudWatch](https://aws.amazon.com/cloudwatch/). CloudWatch est un service qui stocke les journaux et les métriques, et Lambda l'utilise pour stocker les erreurs et les journaux d'exécution de vos fonctions.

Pour configurer le rôle, allez dans la section IAM (Identity and Access Management) de la console, ou utilisez ce [lien direct](https://console.aws.amazon.com/iam/home), et cliquez sur "Rôles" à gauche. Vous verrez une page comme celle ci-dessous :

![AWS IAM](https://www.freecodecamp.org/news/content/images/2020/03/AWS-IAM.png)

Nous devons créer un nouveau rôle, alors cliquez sur "Créer un rôle". Vous verrez une page avec une liste de services AWS. Puisque nous configurons cela pour Lambda, sélectionnez "Lambda" et cliquez sur le bouton "Suivant : Permissions".

![Entité de confiance du rôle AWS](https://www.freecodecamp.org/news/content/images/2020/03/AWS-role-trusted-entity.png)

Maintenant, sur la page des permissions, vous aurez l'option d'attacher des politiques. Tout d'abord, nous allons accorder les permissions "SES" — et vous pouvez le faire en recherchant "SES" et en sélectionnant la politique "AmazonSESFullAccess".

![Politiques de permissions AWS](https://www.freecodecamp.org/news/content/images/2020/03/AWS-permission-policies.png)

De même, vous pouvez accorder l'accès à CloudWatch en recherchant "CloudWatchFullAccess" puis en sélectionnant la politique qui apparaît :

![politique cloudwatch](https://www.freecodecamp.org/news/content/images/2020/03/cloudwatch-policy.png)

Après avoir sélectionné ces politiques, cliquez sur "Suivant : Balises" puis sur le bouton "Suivant : Examen". Dans la zone de texte "Nom du rôle", entrez un nom de rôle de votre choix, tel que "ContactFormRole". Ensuite, cliquez sur le bouton "Créer un rôle".

![Rôle AWS](https://www.freecodecamp.org/news/content/images/2020/03/AWS-role.png)

Maintenant, nous avons un rôle prêt à être utilisé avec notre fonction Lambda.

## Création de la fonction Lambda

À ce stade, nous pouvons créer la fonction Lambda qui reçoit les détails de l'API Gateway et nous envoie un email.

Pour créer la fonction, allez dans la section Lambda de la console, ou utilisez ce [lien direct](https://console.aws.amazon.com/lambda/home). Cliquez sur "Fonctions" dans le côté gauche. Sur cette page, cliquez sur le bouton "Créer une fonction".

![créer une fonction lambda](https://www.freecodecamp.org/news/content/images/2020/03/create-lambda-function.png)

Sur la page de création de fonction, vous serez invité à entrer le nom de la fonction et le langage que vous souhaitez utiliser. Nous nommerons notre fonction "ContactFormFunction", et nous utiliserons Python 3.8 comme langage.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-1.png)

Ensuite, nous attacherons le rôle que nous avons créé dans la section précédente. Cliquez sur "Choisir ou créer un rôle d'exécution" sous la section "Permissions", et sélectionnez "Utiliser un rôle existant" puis sélectionnez le rôle que nous avons créé précédemment, "ContactFormRole". Une fois que vous avez entré les détails, cliquez sur le bouton "Créer une fonction".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-2.png)

Cela vous amènera à une page montrant les détails de votre fonction. Faites défiler un peu vers le bas pour voir l'éditeur de code, qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-3.png)

Dans le panneau de droite, collez le code suivant et remplacez `your_email_address_here` par votre adresse email.

```python
import boto3
from base64 import b64decode
from urllib.parse import parse_qs

# Remplacez votre adresse email ici
send_to = 'your_email_address_here'

def lambda_handler(event, context):
    # Nous recevons nos données via des requêtes POST. API Gateway
    # envoie les données POST sous forme de chaîne encodée en Base64 dans
    # event['body'], donc nous devons la décoder.
    data = parse_qs(b64decode(event['body']).decode())

    subject = 'Vous avez un message de %s' % data['email'][0]
    text = '\n'.join([
        'Nom : %s' % data['name'][0],
        'Email : %s' % data['email'][0],
        'Message %s' % data['message'][0]
    ])

    # Envoyer un email via SES avec l'API SendEmail
    client = boto3.client('ses', region_name='us-east-1')
    client.send_email(
        Source=send_to,
        Destination={'ToAddresses': [send_to]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': text}}
        },
        ReplyToAddresses=[data['email'][0]]
    )

    # Il s'agit de la réponse qui sera envoyée via
    # l'API Gateway au navigateur.
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': '"Succès"' # jquery attend une réponse JSON
    }
```

Ensuite, cliquez sur le bouton "Enregistrer" en haut à droite pour enregistrer votre code. Cela fait, nous allons créer une API Gateway et la mapper avec la fonction Lambda.

## Gestion des requêtes HTTP avec API Gateway

Pour ajouter une API Gateway et la mapper à votre fonction, faites défiler vers le haut dans la page de la fonction Lambda jusqu'à ce que vous voyiez la section "Designer", et cliquez sur le bouton "Ajouter un déclencheur" comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-4.png)

Cela ouvrira la page de configuration du "Déclencheur". Les déclencheurs sont des éléments qui peuvent invoquer votre fonction Lambda, et puisque nous avons besoin d'une API Gateway, choisissez-la dans le menu déroulant :

![déclencheur lambda](https://www.freecodecamp.org/news/content/images/2020/03/lambda-trigger.png)

Cela fera apparaître diverses options pour configurer l'API Gateway. Assurez-vous d'avoir configuré "API" sur "Créer une nouvelle API" et "Choisir un modèle" sur "API HTTP" :

![API Gateway créer une API](https://www.freecodecamp.org/news/content/images/2020/03/api-gateway-create-api.png)

Faites défiler vers le bas et cliquez sur le bouton "Ajouter" pour configurer l'API Gateway. Cela prend quelques secondes à compléter, et une fois terminé, vous serez redirigé vers la vue du designer. Cliquez sur le bouton "API Gateway" à gauche pour voir l'URL à travers laquelle vous pouvez déclencher la fonction Lambda :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/lambda-5.png)

Maintenant, avant de créer la page du formulaire de contact, nous allons tester que notre configuration fonctionne correctement jusqu'à présent. Si vous êtes sur MacOS, Linux, ou une version récente de Windows 10, vous pouvez copier l'URL de l'API Gateway affichée ci-dessus et exécuter la commande suivante dans votre terminal. Assurez-vous de remplacer `your_api_gateway_url` par l'URL réelle !

```
curl -i your_api_gateway_url --data-urlencode "name=John" --data-urlencode "email=john@example.com" --data-urlencode "message=bonjour"
```

Si tout s'est bien passé, vous pouvez voir une réponse 200 OK avec un message "Succès", comme ceci :

![requête curl](https://www.freecodecamp.org/news/content/images/2020/03/curl-request.png)

Vous devriez également recevoir un email dans votre boîte de réception intitulé "Vous avez un message de john@example.com" avec les détails qui ont été saisis dans le formulaire.

Cependant, cela peut parfois être capricieux. L'email peut être livré dans votre dossier de spam, ou parfois même être rejeté sans que vous ne voyiez jamais cet email. Cela est dû au fait que des fournisseurs comme Gmail et Yahoo bloquent les tiers (comme SES) d'envoyer des emails en utilisant leur nom de domaine.

Si vous avez votre propre nom de domaine, vous pouvez contourner cela en configurant un [enregistrement SPF](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-authentication-spf.html). Cependant, nous n'en discuterons pas dans ce guide, car nous voulons que vous puissiez suivre même sans un domaine.

Ensuite, nous allons compléter ce guide en construisant la page du formulaire de contact.

## Construction du formulaire de contact

Ouvrez votre éditeur de texte préféré et enregistrez le code suivant sous forme de fichier HTML. N'oubliez pas de remplacer `your_api_gateway_url` par l'URL complète que vous avez obtenue précédemment.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Formulaire de contact</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <style>
    body {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Formulaire de contact</h2>
    <hr>
    <form id="form">
      <div class="form-group">
        <label for="name">Votre nom</label>
        <input type="text" class="form-control" id="name" placeholder="Votre nom">
      </div>
      <div class="form-group">
        <label for="email">Votre adresse email</label>
        <input type="email" class="form-control" id="email" placeholder="Votre adresse email">
      </div>
      <div class="form-group">
        <label for="message">Votre message</label>
        <textarea class="form-control" id="message" rows="3"></textarea>
      </div>
      <div id="alert" class="alert d-none">
      </div>
      <button type="submit" class="btn btn-primary">
        Soumettre
      </button>
    </form>
  </div>
  <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
  <script>
    function showMessage(msg, type) {
      $('#alert').attr('class', `alert alert-${type}`).text(msg)
    }

    function hideMessage(msg) {
      $('#alert').attr('class', 'd-none')
    }

    $('#form').submit(event => {
      event.preventDefault()
      hideMessage()

      let name = $('#name').val().trim()
      let email = $('#email').val().trim()
      let message = $('#message').val().trim()

      if (!(name && email && message)) {
        showMessage('Vous devez remplir tous les champs avant de soumettre le formulaire', 'danger')
        return
      }

      $.post('your_api_gateway_url', {name, email, message}).done(_ => {
        showMessage("Merci de nous avoir contactés. Nous vous répondrons bientôt.", 'success')
      }).fail(_ => {
        showMessage('Quelque chose s\'est mal passé lors de la soumission du message', 'danger')
      })
    })
  </script>
</body>
</html>
```

Une fois que vous avez enregistré le fichier, ouvrez-le dans votre navigateur, remplissez les détails et cliquez sur "Soumettre". Vous pourrez voir un message de succès, comme ceci :

![formulaire de contact](https://www.freecodecamp.org/news/content/images/2020/03/contact-form.png)

Cliquer sur le bouton soumet les détails sous forme de requête POST à l'API Gateway, qui déclenche ensuite la fonction Lambda, qui à son tour nous envoie un email via SES. Cependant, comme nous l'avons discuté dans la section précédente ("Gestion des requêtes HTTP avec API Gateway"), vous ne recevrez peut-être pas d'email dans certaines circonstances.

Maintenant que nous avons un formulaire de contact qui déplace la plupart de sa logique vers le serverless, vous avez cette page web statique que vous devez héberger quelque part.

Alors, avez-vous besoin d'un serveur pour héberger cette page ? Pas du tout ! AWS propose un service de stockage nommé S3 (Simple Storage Service), et vous pouvez l'utiliser pour héberger des sites web statiques. Cela nécessite un nom de domaine, donc si vous en possédez un, vous pouvez utiliser [cet article](https://medium.com/@kyle.galbraith/how-to-host-a-website-on-s3-without-getting-lost-in-the-sea-e2b82aa6cd38) pour héberger la page web.

## Où aller ensuite ?

Maintenant que nous avons construit un simple formulaire de contact en utilisant le serverless, comment construire des applications plus grandes ? Cliquer sur diverses options dans la console est un bon moyen d'apprendre AWS et le serverless, mais ce n'est pas une option lorsque vous essayez de construire quelque chose de grand avec beaucoup de parties mobiles.

Heureusement, il existe divers outils qui peuvent vous aider à construire et à déployer des applications serverless sur AWS, tels que le [Framework Serverless](https://serverless.com/) ou [AWS Chalice](https://chalice.readthedocs.io/en/latest/). [CloudFormation](https://aws.amazon.com/cloudformation/), un service AWS gratuit, peut également vous aider à construire des applications en automatisant le processus de déploiement via des modèles écrits en JSON ou YAML, bien qu'il soit un peu plus difficile à utiliser que les autres options.