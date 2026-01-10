---
title: Je voulais que le Twitter de freeCodeCamp Toronto tweete des citations, alors
  j'ai créé un bot gratuit pour le faire.
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2018-03-09T00:45:56.000Z'
originalURL: https://freecodecamp.org/news/running-a-free-twitter-bot-on-aws-lambda-66160eb4de4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BRRO1djJpCPe-Z92aBt62Q.png
tags:
- name: bots
  slug: bots
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
seo_title: Je voulais que le Twitter de freeCodeCamp Toronto tweete des citations,
  alors j'ai créé un bot gratuit pour le faire.
seo_desc: If you read About time, you’ll know that I’m a big believer in spending
  time now on building things that save time in the future. To this end, I built a
  simple Twitter bot in Go that would occasionally post links to my articles and keep
  my account in...
---

Si vous lisez [À propos du temps](https://victoria.dev/verbose/about-time/), vous savez que je suis une grande croyante dans le fait de passer du temps maintenant à construire des choses qui font gagner du temps à l'avenir. À cette fin, j'ai construit un simple bot Twitter en Go qui publiait occasionnellement des liens vers mes articles et gardait mon compte intéressant même lorsque je suis trop occupée pour l'utiliser. Les tweets aident à générer du trafic vers mes sites, et je n'ai pas à lever le petit doigt.

J'ai exécuté le bot sur une instance Amazon EC2 pendant environ un mois. Mon utilisation d'AWS a historiquement été assez peu coûteuse (moins que le prix d'un café dans la plupart de l'Amérique du Nord), alors j'ai été surprise lorsque la petite instance que j'utilisais a accumulé une facture 90 % plus élevée que le mois précédent. Je ne pense pas qu'AWS soit cher, pour être claire, mais quand même... Je suis économe. Je veux mon bot Twitter, et je le veux pour moins cher.

J'avais l'intention d'explorer AWS Lambda, et j'ai pensé que c'était une bonne opportunité. Contrairement à une instance EC2 qui tourne constamment (et vous facture pour cela), Lambda vous facture par requête et selon la durée de l'exécution de votre fonction. Il y a aussi un niveau gratuit, et les premières 1 million de requêtes, plus une certaine quantité de temps de calcul, sont gratuites.

En gros, si vous exécutez un bot Twitter qui publie pour vous, disons, deux fois par jour, votre coût mensuel pour utiliser Lambda serait de... carry the one... rien. J'exécute ma fonction Lambda depuis quelques semaines maintenant, complètement gratuitement.

Lorsque récemment, il a été temps pour moi de prendre les rênes du Twitter [@freeCodeCampTO](https://twitter.com/freeCodeCampTO), j'ai décidé d'employer une stratégie similaire. J'ai également utilisé cette opportunité pour documenter le processus pour vous, cher lecteur.

Donc, si vous utilisez actuellement une instance en fonctionnement à temps plein pour une tâche qui pourrait être servie par un cron job, cet article est pour vous. Je vais couvrir comment écrire votre fonction pour Lambda, et comment la configurer pour qu'elle s'exécute automatiquement. Et, en bonus, j'inclurai un script bash pratique qui met à jour votre fonction à partir de la ligne de commande chaque fois que vous devez apporter une modification. C'est parti !

### Lambda est-il fait pour vous ?

Lorsque j'ai écrit le code pour mon bot Twitter en Go, j'avais l'intention de le faire fonctionner sur une instance AWS et je me suis largement inspirée de [l'épisode génial Just for Func de Francesc](https://github.com/campoy/justforfunc/tree/master/14-twitterbot). Quelque temps plus tard, je l'ai modifié pour qu'il choisisse aléatoirement un article parmi mes flux RSS et tweete le lien, deux fois par jour. Je voulais faire quelque chose de similaire pour le bot @freeCodeCampTO, et lui faire tweeter une citation inspirante sur la programmation chaque matin.

C'est un bon cas d'utilisation pour Lambda parce que :

* Le programme doit s'exécuter une fois
* Il s'exécute selon un calendrier régulier, en utilisant le temps comme déclencheur
* Il n'a pas besoin de s'exécuter constamment

L'important à garder à l'esprit est que Lambda exécute une fonction une fois en réponse à un événement que vous définissez. Le déclencheur le plus largement applicable est une simple expression cron, mais il existe de nombreux autres événements déclencheurs que vous pouvez configurer. Vous pouvez obtenir un aperçu [ici](https://aws.amazon.com/lambda/).

### Écrire une fonction Lambda

J'ai trouvé cela très simple à faire en Go. Tout d'abord, récupérez la bibliothèque [aws-lambda-go](https://github.com/aws/aws-lambda-go) :

```
go get github.com/aws/aws-lambda-go/lambda
```

Ensuite, faites de ceci votre `func main()` :

```js
func main() { 
       lambda.Start(tweetFeed) 
}
```

où `tweetFeed` est le nom de la fonction qui fait tout fonctionner. Bien que je ne vais pas entrer dans l'écriture de tout le bot Twitter ici, vous pouvez consulter mon [code sur GitHub](https://gist.github.com/victoriadrake/7859dab68df87e28f40d6715d08383c7).

### Configurer AWS Lambda

Je suppose que vous avez déjà un compte AWS. Si ce n'est pas le cas, première chose à faire ici : [https://aws.amazon.com/free](https://aws.amazon.com/free)

### 1. Créer votre fonction

Trouvez AWS Lambda dans la liste des services, puis cherchez ce bouton brillant :

![Image](https://cdn-media-1.freecodecamp.org/images/qIm1TxAXfJKEGAFbnbqES24MR65doEaTekrW)

Nous allons créer une fonction à partir de zéro. Nommez votre fonction, puis sous **Runtime** choisissez « Go 1.x ».

Sous **Role name** écrivez n'importe quel nom que vous aimez. C'est un champ obligatoire, mais sans importance pour ce cas d'utilisation.

Cliquez sur **Create function**.

![Image](https://cdn-media-1.freecodecamp.org/images/Q05OinPHTS5NY-XOFLXE5sGaSsU-qESrDVWy)

### 2. Configurer votre fonction

Vous verrez un écran pour configurer votre nouvelle fonction. Sous **Handler** entrez le nom de votre programme Go.

![Image](https://cdn-media-1.freecodecamp.org/images/B9QTTbx0JTqtsumeH0Jf387oW1PLpMe7U7Fu)

Si vous faites défiler vers le bas, vous verrez un endroit pour entrer les variables d'environnement. C'est un bon endroit pour entrer les jetons et secrets de l'API Twitter, en utilisant les noms de variables que votre programme attend. La fonction AWS Lambda créera l'environnement pour vous en utilisant les variables que vous fournissez ici.

![Image](https://cdn-media-1.freecodecamp.org/images/6g09YtNJPhHQYNwS1flNHOg4TgjXY0AwFYB3)

Aucun autre paramètre n'est nécessaire pour ce cas d'utilisation. Cliquez sur **Save** en haut de la page.

### 3. Télécharger votre code

Vous pouvez télécharger le code de votre fonction sous forme de fichier zip sur l'écran de configuration. Puisque nous utilisons Go, vous voudrez d'abord faire `go build`, puis zipper l'exécutable résultant avant de le télécharger sur Lambda.

... Bien sûr, je ne vais pas faire cela manuellement chaque fois que je veux modifier ma fonction. C'est à cela que servent `awscli` et ce script bash !

`update.sh`

```
go build && \ 
zip fcc-tweet.zip fcc-tweet && \ 
rm fcc-tweet && \ 
aws lambda update-function-code --function-name fcc-tweet --zip-file fileb://fcc-tweet.zip && \ 
rm fcc-tweet.zip
```

Maintenant, chaque fois que je fais une modification, je lance simplement `bash update.sh`.

Si vous n'utilisez pas déjà [AWS Command Line Interface](https://aws.amazon.com/cli/), faites `pip install awscli` et remerciez-moi plus tard. Trouvez des instructions pour vous configurer et vous lancer en quelques minutes [ici](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) sous **Quick Configuration**.

### 4. Tester votre fonction

Vous voulez voir ça fonctionner ? Bien sûr que oui ! Cliquez sur « Configure test events » dans le menu déroulant en haut.

![Image](https://cdn-media-1.freecodecamp.org/images/JWXu1kePtQwT0sMHRSuGblbMqTnn5rFMigV2)

Puisque vous utiliserez un déclencheur basé sur le temps pour cette fonction, vous n'avez pas besoin d'entrer de code pour définir des événements de test dans la fenêtre pop-up. Écrivez simplement n'importe quel nom sous **Event name** et videz le JSON dans le champ ci-dessous. Ensuite, cliquez sur **Create**.

![Image](https://cdn-media-1.freecodecamp.org/images/fLckVqobjQUiH32AMTkhbaMdyQeiyu64KVFU)

Cliquez sur **Test** en haut de la page, et si tout fonctionne correctement, vous devriez voir...

![Image](https://cdn-media-1.freecodecamp.org/images/tqJRKThljxHyeBe0EUULpDbIUz6NFKi5Dk9Z)

### 5. Configurer les événements CloudWatch

Pour exécuter notre fonction comme nous le ferions avec un cron job — comme un événement planifié régulier basé sur le temps — nous utiliserons CloudWatch. Cliquez sur **CloudWatch Events** dans la barre latérale **Designer**.

![Image](https://cdn-media-1.freecodecamp.org/images/RT2ZUJs1FniR6coBW4HBiM1zlvtfDDvyBt2w)

Sous **Configure triggers**, vous créerez une nouvelle règle. Choisissez un nom descriptif pour votre règle sans espaces ni ponctuation, et assurez-vous que **Schedule expression** est sélectionné. Ensuite, entrez l'heure à laquelle vous voulez que votre programme s'exécute sous forme d'expression de taux, ou d'expression cron.

Une expression cron ressemble à ceci : `cron(0 12 * * ? *)`

Les éléments entre crochets représentent, dans l'ordre : minutes, heures, jour du mois, mois, jour de la semaine et année. En français, cela signifie : Exécuter à midi (UTC) tous les jours.

Pour en savoir plus sur la façon d'écrire vos expressions cron, lisez [ceci](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html).

Pour savoir quelle est l'heure actuelle en UTC, cliquez [ici](https://codepen.io/victoriadrake/full/OQabar).

Si vous voulez que votre programme s'exécute deux fois par jour, disons une fois à 10h et une autre à 15h, vous devrez configurer deux déclencheurs d'événements CloudWatch séparés et deux règles d'expression cron.

Cliquez sur **Add**.

![Image](https://cdn-media-1.freecodecamp.org/images/h5qitsKU9RfEayGeKITs32sWemUvD2KYMioV)

### Regardez-le fonctionner

C'est tout ce dont vous avez besoin pour lancer votre fonction Lambda ! Maintenant, vous pouvez vous asseoir, vous détendre et faire des choses plus importantes que de partager vos liens RSS sur Twitter.