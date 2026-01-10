---
title: 'AWS Step Functions : comment implémenter des sémaphores pour les machines
  à états'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-21T20:06:11.000Z'
originalURL: https://freecodecamp.org/news/aws-step-functions-how-to-implement-semaphores-for-state-machines-8075650ceb86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sjet9qSO4O8fX2-FXvxflw.jpeg
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'AWS Step Functions : comment implémenter des sémaphores pour les machines
  à états'
seo_desc: 'By Yan Cui

  Here at DAZN, we are migrat­ing from our lega­cy plat­form into the brave new world
  of microfron­tends and microser­vices. Along the way, we also dis­cov­ered the delights
  that AWS Step Func­tions have to offer. For exam­ple…


  flex­i­ble e...'
---

Par Yan Cui

Ici chez [DAZN](https://engineering.dazn.com/), nous migrons de notre plateforme héritée vers le nouveau monde des [microfrontends](https://micro-frontends.org/) et des microservices. En cours de route, nous avons également découvert les avantages que les AWS Step Functions ont à offrir. Par exemple...

* gestion flexible des erreurs et nouvelle tentative
* la capacité sous-estimée d'attendre entre les tâches
* la capacité de mélanger des étapes automatisées avec des [activités](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html) nécessitant une intervention humaine

Dans certains cas, nous devons contrôler le nombre d'exécutions concurrentes de machines à états qui peuvent accéder à une ressource partagée. Cela peut être une exigence commerciale. Ou cela peut être dû à des préoccupations de scalabilité pour la ressource partagée. Cela peut également être le résultat de la conception de notre machine à états qui la rend difficile à paralléliser.

Nous avons trouvé quelques solutions qui se divisent en deux catégories générales :

1. Contrôler le nombre d'exécutions que vous pouvez démarrer
2. Permettre aux exécutions concurrentes de démarrer, mais bloquer une exécution d'entrer dans le chemin critique jusqu'à ce qu'elle puisse acquérir un [sémaphore](https://en.wikipedia.org/wiki/Semaphore_%28programming%29) (c'est-à-dire, un signal pour continuer)

### Contrôler le nombre d'exécutions concurrentes

Vous pouvez contrôler le nombre MAX d'exécutions concurrentes en introduisant une file d'attente SQS. Un calendrier CloudWatch déclenchera une fonction Lambda pour :

1. vérifier combien d'exécutions concurrentes il y a
2. si il y a N exécutions, alors nous pouvons démarrer MAX-N exécutions
3. interroger SQS pour MAX-N messages, et démarrer une nouvelle exécution pour chacun

![Image](https://cdn-media-1.freecodecamp.org/images/HEltXnpPctxNoQlmZPgqWmqFKAExcaRJMBst)

Nous n'utilisons pas le nouveau [déclencheur SQS pour Lambda](https://aws.amazon.com/blogs/aws/aws-lambda-adds-amazon-simple-queue-service-to-supported-event-sources/) ici, car le but est de **ralentir** la création de nouvelles exécutions. Alors que le déclencheur SQS pousserait les tâches vers notre fonction Lambda avec empressement.

De plus, vous devriez utiliser une file FIFO afin que les tâches soient traitées dans le même ordre où elles sont ajoutées à la file.

### Bloquer l'exécution en utilisant des sémaphores

Vous pouvez utiliser l'API [ListExecutions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html) pour découvrir combien d'exécutions sont dans l'état RUNNING. Vous pouvez ensuite les trier par [startDate](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionListItem.html#StepFunctions-Type-ExecutionListItem-startDate) et ne permettre qu'aux exécutions les plus anciennes de passer à des états qui accèdent à la ressource partagée.

![Image](https://cdn-media-1.freecodecamp.org/images/fJaX03lK7RvYFecLc9CeJn0hZ5dj3Kpt4BMc)

Prenons par exemple la machine à états suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/35CfjuZqHsXqiEx5fXvkAeYBov9zvyDMA3ol)

L'état **OnlyOneShallRunAtOneTime** invoque la fonction Lambda `one-shall-pass` et retourne un indicateur `proceed`. L'état **Shall Pass?** branche ensuite le flux de cette exécution en fonction de l'indicateur `proceed`.

```
OnlyOneShallRunAtOneTime:
  Type: Task
  Resource: arn:aws:lambda:us-east-1:xxx:function:one-shall-pass
  Next: Shall Pass?

Shall Pass?:
  Type: Choice
  Choices:
    - Variable: $.proceed
      # vérifier si cette exécution doit continuer
      BooleanEquals: true
      Next: SetWriteThroughputDeltaForScaleUp
    Default: WaitToProceed
      # sinon attendre et réessayer plus tard

WaitToProceed:
  Type: Wait
  Seconds: 60
  Next: OnlyOneShallRunAtOneTime
```

Le point délicat ici est comment associer l'invocation Lambda avec l'exécution correspondante de Step Functions. Malheureusement, Step Functions ne passe pas l'ARN d'exécution à la fonction Lambda. Au lieu de cela, nous devons passer le nom de l'exécution dans l'entrée lorsque nous démarrons l'exécution.

```
const name = uuid().replace(/-/g, '_')
const input = JSON.stringify({ name, bucketName, fileName, mode })
  const req = { stateMachineArn, name, input }
const resp = await SFN.startExecution(req).promise()
```

Lorsque la fonction `one_shall_pass` s'exécute, elle peut utiliser le `name` de l'exécution à partir de l'entrée. Elle est alors capable de faire correspondre l'invocation avec les exécutions retournées par [ListExecutions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html).

Dans ce cas particulier, seule l'exécution la plus ancienne peut continuer. Toutes les autres exécutions passeraient à l'état **WaitToProceed**.

```
module.exports.handler = async (input, context) => {
  const executions = await listRunningExecutions()
  Log.info(`found ${executions.length} RUNNING executions`)
```

```
const oldest = _.sortBy(executions, x => x.startDate.getTime())[0]
      Log.info(`the oldest execution is [${oldest.name}]`)
```

```
if (oldest.name === input.name) {
    return { ...input, proceed: true }
  } else {
    return { ...input, proceed: false }
  }
}
```

### Comparaison des approches

Comparons les deux approches selon les critères suivants :

* **Scalabilité**. Comment l'approche gère-t-elle l'augmentation du nombre d'exécutions concurrentes ?
* **Simplicité**. Combien de pièces mobiles l'approche ajoute-t-elle ?
* **Coût**. Quel est le coût supplémentaire de l'approche ?

#### Scalabilité

L'approche 2 (bloquer les exécutions) présente deux problèmes lorsque vous avez un grand nombre d'exécutions concurrentes.

Premièrement, vous pouvez atteindre la limite de throttling régionale sur l'appel API `ListExecutions`.

![Image](https://cdn-media-1.freecodecamp.org/images/WeuQ0JcWEx5FoUQlIkfuj1pYh3fcHkfXn9x2)

Deuxièmement, si vous avez configuré un timeout sur votre machine à états (et vous devriez !), ils peuvent également expirer. Cela crée une contre-pression sur le système.

![Image](https://cdn-media-1.freecodecamp.org/images/c69Jh5yX3TpcLhmDBfHfwzmUn8d8nMsx1k56)

L'approche 1 (avec SQS) est beaucoup plus scalable en comparaison. Les tâches en file d'attente ne sont pas démarrées tant qu'elles ne sont pas autorisées à démarrer, donc pas de contre-pression. Seule la fonction Lambda cron doit lister les exécutions, donc vous êtes également peu susceptible d'atteindre les limites de l'API.

#### Simplicité

L'approche 1 introduit de nouvelles pièces à l'infrastructure — SQS, le calendrier CloudWatch et Lambda. De plus, elle force les producteurs à changer également.

Avec l'approche 2, une nouvelle fonction Lambda est nécessaire pour l'étape supplémentaire, mais elle fait partie de la machine à états.

#### Coût

L'approche 1 introduit un coût de base minimal même lorsqu'il n'y a pas d'exécutions. Cependant, nous parlons de quelques centimes ici...

L'approche 2 introduit des transitions d'état supplémentaires, ce qui coûte environ 25 $ par million. Voir la page de [tarification des Step Functions](https://aws.amazon.com/step-functions/pricing/) pour plus de détails. Puisque chaque exécution entraînera 3 transitions par minute pendant qu'elle est bloquée, le coût de ces transitions peut s'accumuler rapidement.

### Conclusions

Étant donné les deux approches que nous avons considérées ici, l'utilisation de SQS est de loin la plus scalable. Elle est également plus rentable à mesure que le nombre d'exécutions concurrentes augmente.

Cependant, vous devez gérer une infrastructure supplémentaire et forcer les systèmes en amont à changer. Cela peut impacter d'autres équipes, et affecter finalement votre capacité à livrer à temps.

Si vous ne prévoyez pas un grand nombre d'exécutions, alors vous pourriez être mieux lotis avec la deuxième approche.