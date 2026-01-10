---
title: Comment automatiser les tâches avec Azure WebJobs
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2021-12-21T16:33:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-tasks-with-azure-webjobs
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/cover.jpg
tags:
- name: automation
  slug: automation
- name: Azure
  slug: azure
- name: Productivity
  slug: productivity
seo_title: Comment automatiser les tâches avec Azure WebJobs
seo_desc: "When you work in IT operations, automation is a key part of your job. \n\
  You'll have various repetitive tasks you have to deal with, and you don’t want to\
  \ waste your time doing something that can be done by a script. \nHere are some\
  \ great reasons to aut..."
---

Lorsque vous travaillez dans les opérations informatiques, l'automatisation est une partie clé de votre travail. 

Vous aurez diverses tâches répétitives à gérer, et vous ne voulez pas perdre votre temps à faire quelque chose qui peut être fait par un script. 

Voici quelques bonnes raisons d'automatiser les tâches répétitives :

* effectuer des tâches répétitives n'aide pas votre carrière ni ne développe votre ensemble de compétences
* il y a beaucoup de place pour les erreurs
* comme je l'ai dit avant, vous avez l'impression de perdre votre temps. Et si vous demandiez à quelqu'un d'autre de faire ces tâches, il en serait de même. 

## Quand est-il temps d'automatiser une tâche ?

Eh bien, plus vous avancez dans votre parcours professionnel, plus vous comprendrez quand vous pouvez essayer d'automatiser un processus. 

Sur la base de mon expérience personnelle, vous devez être en mesure de répondre à ces trois questions :

### 1. À quelle fréquence effectuez-vous cette tâche ?

Gardez une trace du nombre de fois où vous avez effectué la tâche au cours du dernier mois. Si elle doit être faite chaque semaine ou moins, vous devriez essayer de l'automatiser.

### 2. Combien de temps prend ce processus ?

Essayez d'estimer le temps moyen dont vous avez besoin pour compléter la tâche. Si elle est égale ou supérieure à 30 minutes, je pense qu'il vaut la peine de réfléchir à la manière de l'automatiser. 

Juste pour vous donner une idée, disons que vous effectuez la tâche tous les jours et qu'elle prend 30 minutes. Cela représente 2,5 heures par semaine et 10 heures par mois. En supposant que vous travaillez huit heures par jour, vous passez plus d'une journée par mois à gérer cette tâche. En termes de budget, cela représente beaucoup d'argent.

### 3. Quel est le coût de l'automatisation ?

Vous avez besoin d'une estimation des coûts : combien d'heures avez-vous besoin pour développer le script ? Avez-vous besoin d'utiliser des services tiers tels que des bibliothèques, des services cloud, etc. ? 

Si vous décidez que le développement est rapide et peu coûteux, vous pouvez envisager de passer à l'implémentation.

## Comment automatiser les tâches

D'accord, voyons maintenant comment vous pouvez automatiser une tâche simple mais fréquente. 

Lorsque vous travaillez dans les opérations informatiques, vous devrez souvent générer des rapports ou des fichiers avec des informations mises à jour pour d'autres départements. Disons que vous êtes invité à générer un fichier avec certaines informations sur un profil GitHub spécifique.

GitHub offre des API où vous pouvez obtenir des informations sur un seul profil :

[https://api.github.com/users](https://api.github.com/users)/<USERNAME>

Nous pouvons écrire un script rapide avec Node.js et Axios pour appeler l'endpoint, obtenir les informations dont nous avons besoin et créer un fichier texte pour les stocker dans un répertoire spécifique.

Voici notre script :

```javascript
const axios = require('axios');
const fs = require('fs');

axios.get('https://api.github.com/users/<USERNAME>')
  .then(response => {
    const file_text = response.data.login + " " + response.data.name
    const nome = Date.now()
    console.log(response.data.login);
    console.log(response.data.name);
    fs.writeFile('./fileCreated/' + nome + '.txt', file_text, err => {
      if (err) {
        console.error(err)
        return
      }
    })
    
  })
  .catch(error => {
    console.log(error);
  });
```

Comme vous pouvez le voir, une fois que nous appelons l'endpoint, nous enregistrons le nom d'utilisateur et le nom dans la console. Ensuite, nous imprimons ces informations dans un fichier texte nommé par le timestamp, et nous les enregistrons dans un répertoire appelé "fileCreated".

### Comment exécuter le script périodiquement

Il existe de nombreux outils qui vous aident à exécuter un script à tout moment donné. Pour ce tutoriel, j'ai décidé d'utiliser Azure WebJobs. 

C'est un service inclus dans la solution Pass d'Azure, "Web App", et il vous permet d'exécuter des scripts, manuellement ou périodiquement, écrits avec les langages les plus populaires au monde tels que Java, Python, .NET, et, bien sûr, NodeJs. 

Vous pouvez trouver la liste complète [ici](https://docs.microsoft.com/en-us/azure/app-service/webjobs-create).

### Comment utiliser Azure WebJobs

Je suppose que vous avez déjà créé votre Web App. Juste pour information, au moment où j'écris ce tutoriel, les WebJobs sont disponibles uniquement sur les Web Apps Windows. 

Si vous avez besoin d'aide pour commencer, je vous suggère de consulter ce [tutoriel](https://azure.microsoft.com/en-us/get-started/web-app/) de Microsoft.

Dans le menu WebApp (barre latérale gauche), j'ai filtré les options en tapant "WebJobs" et en cliquant dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/0.png)

Une fois sur le panneau WebJobs, j'ai cliqué sur "Add" pour ajouter mon script (j'ai zippé mon fichier avec toutes ses dépendances et je l'ai appelé "axiosexample"). Ensuite,

* J'ai entré le nom
* J'ai téléchargé le fichier zippé
* J'ai choisi "triggered" puisque je ne veux pas que cette tâche soit effectuée en continu

Dans l'option "Triggers", j'ai choisi "Manual" parce que je voulais l'exécuter maintenant pour vous montrer le résultat pour ce tutoriel. Mais vous pouvez planifier les WebJobs en choisissant "Scheduled" et en spécifiant l'expression CRON. Consultez ce [tutoriel](https://docs.microsoft.com/en-us/azure/app-service/webjobs-create#CreateScheduledCRON) de Microsoft pour voir comment écrire une expression CRON. 

Si vous voulez en savoir plus sur les expressions CRON, Internet regorge de littérature à ce sujet. Vous pouvez simplement commencer par la page [Wikipedia](https://en.wikipedia.org/wiki/Cron), consulter ce [tutoriel sur freeCodeCamp](https://www.freecodecamp.org/news/cron-jobs-in-linux/), et continuer avec d'autres contenus utiles tels que [Cronitor](https://crontab.guru/).

Ensuite, cliquez sur "Ok".

![Image](https://www.freecodecamp.org/news/content/images/2021/12/2.png)

Une fois enregistré, cliquez sur "Run" pour exécuter la tâche immédiatement. Ensuite, cliquez sur "Logs" pour voir les résultats de nos WebJobs.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/4.png)

Une fois sur la page "Logs", cliquez sur webjobs pour obtenir plus de détails :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/5.png)

Ensuite, définissons le "Timing" de nos WebJobs :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/6.png)

Et nous voyons les messages de journal, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/7.png)

Maintenant, en utilisant le service "Kudu" disponible dans notre Web App, allez dans le répertoire où vous avez enregistré votre fichier via Powershell. 

"Kudu" est un service très utile disponible sur les Web Apps d'Azure qui vous permet d'obtenir beaucoup d'informations sur la Web App elle-même, telles que les paramètres de l'application, les commandes d'exécution, et bien plus encore. Vous pouvez voir la liste complète [ici](https://docs.microsoft.com/en-us/azure/app-service/resources-kudu).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/8.png)

Vous atteindrez le répertoire que vous avez créé. Le chemin est :

```cmd
\home\site\wwwroot\App_Data\jobs\triggered\webjob\axiosexample\fileCreated
```

![Image](https://www.freecodecamp.org/news/content/images/2021/12/9.png)

Une fois que vous atteignez le fichier, ouvrez-le simplement et voici ce que vous devriez voir :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/10.png)

## Conclusion

Donc, voici un exemple rapide de la manière dont vous pouvez simplement automatiser une tâche avec quelques lignes de JavaScript et Azure WebJobs. 

Regardez simplement autour de vous et voyez ce que vous trouvez répétitif et chronophage. Ensuite, réfléchissez à la manière dont vous pourriez mettre ces actions dans un script et c'est tout ! 

L'automatisation est tout autour de vous ! 😀 N'oubliez pas : plus vous automatisez, plus vous avez de temps pour penser à plus d'automatisations... N'hésitez pas à jeter un coup d'œil à mon [dépôt](https://github.com/mventuri/How-to-Automate-Tasks-with-Azure-Webjobs) sur GitHub.