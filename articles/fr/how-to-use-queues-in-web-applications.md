---
title: Comment utiliser les files d'attente dans les applications web – Tutoriel Node.js
  et Redis
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-07-06T16:23:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-queues-in-web-applications
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/businessmen02.jpg
tags:
- name: Node.js
  slug: nodejs
- name: queue
  slug: queue
- name: Redis
  slug: redis
seo_title: Comment utiliser les files d'attente dans les applications web – Tutoriel
  Node.js et Redis
seo_desc: 'When you''re building large scale web applications, speed is a major priority.
  Users don''t want to wait long for responses anymore, and they shouldn''t have to.
  But some processes take time, and they cannot be made any faster or eliminated.

  Message que...'
---

Lorsque vous construisez des applications web à grande échelle, la vitesse est une priorité majeure. Les utilisateurs ne veulent plus attendre longtemps pour les réponses, et ils ne devraient pas avoir à le faire. Mais certains processus prennent du temps, et ils ne peuvent pas être accélérés ou éliminés.

Les files d'attente de messages aident à résoudre ce problème en fournissant une branche supplémentaire au parcours habituel de requête-réponse. Cette branche supplémentaire aide à s'assurer que les utilisateurs peuvent obtenir des réponses immédiates, et les processus chronophages peuvent être effectués en parallèle. Tout le monde rentre chez soi heureux.

Cet article se concentrera sur l'explication de ce que sont les files d'attente de messages et comment commencer à les utiliser en construisant une application très simple. Vous devriez être familier avec les bases de Node.js, et vous devriez avoir Redis installé soit localement soit sur une instance cloud. Apprenez comment installer Redis [ici](https://redis.io/docs/getting-started/installation/).

## Qu'est-ce qu'une file d'attente ?

Une file d'attente est une structure de données qui permet de stocker des entités dans un ordre. Les files d'attente utilisent un principe premier entré, premier sorti (FIFO).

Le concept des files d'attente en informatique est le même que le concept des files d'attente dans la vie quotidienne où les gens font la queue pour obtenir des choses. Vous rejoignez une file d'attente par l'arrière, attendez jusqu'à ce que ce soit votre tour, puis quittez la file d'attente par l'avant après avoir été servi.

En informatique, lorsqu'un processus comme une requête API est en cours d'exécution, et que vous devez retirer une certaine tâche (comme l'envoi d'un email) du flux actuel, vous la poussez dans une file d'attente et continuez le processus.

Le diagramme ci-dessous illustre le cycle de vie d'une file d'attente :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/job-lifecycle.png)
_Cycle de vie de la file d'attente | https://optimalbits.github.io/bull/_

## Qu'est-ce qu'un Job ?

Un job est toute pièce de données utilisée dans une file d'attente, généralement un objet de type JSON.

Comme démontré dans l'image de couverture de cet article, vous pouvez penser à un job comme chaque personne dans une file d'attente à un aéroport. Chaque personne tient une mallette contenant des données spécifiques, et d'autres instructions (passeports et peut-être des papiers médicaux si nécessaire) qui aideront lorsqu'il sera leur tour d'être servis.

Les nouvelles personnes rejoignant cette file d'attente entreront par l'arrière (comme la dernière personne), et les personnes seront servies par l'avant. C'est ainsi que les jobs sont également traités, chaque job contient des données qui seront utilisées pour son traitement. Les nouveaux jobs sont ajoutés par l'arrière tandis que les jobs sont retirés par l'avant.

### Qu'est-ce qu'un Producteur de Jobs ?

Un producteur de jobs est toute pièce de code qui ajoute un job à une file d'attente. Dans la vie réelle, ce serait l'agent de sécurité à l'aéroport qui donne des directions aux gens, leur disant quelle file d'attente rejoindre pour différents buts.

Un producteur de jobs peut exister indépendamment d'un consommateur de jobs. Cela signifie que dans une configuration de microservices, un service particulier pourrait simplement être concerné par l'ajout de jobs à une file d'attente, mais pas par la manière dont ils sont traités après.

### Qu'est-ce qu'un Worker (Consommateur de Jobs) ?

Un worker, ou consommateur de jobs, est un processus, ou une fonction, qui peut exécuter un job. Pensez à un worker comme à un caissier de banque qui sert les gens dans une file d'attente à la banque. Lorsque la première personne arrive, elle rejoint la file d'attente comme la seule personne dans la file d'attente. Le caissier l'appelle ensuite et la file d'attente est vidée.

Le caissier demande des détails spécifiques à utiliser pour traiter la transaction à la personne. Pendant que le caissier sert ce client, quatre autres clients pourraient s'être alignés. Ils resteront dans la file d'attente jusqu'à ce que le caissier ait terminé avec le premier client avant d'appeler le suivant. C'est le même processus avec les workers de file d'attente — ils prennent le premier job dans la file d'attente, et le traitent.

### Qu'est-ce que les Jobs Échoués ?

Souvent, certains jobs peuvent échouer pendant le traitement.

Voici quelques raisons pour lesquelles un job pourrait échouer :

* Données d'entrée invalides ou manquantes : Lorsque les données requises pour qu'un job soit traité sont manquantes, le job échouera. Par exemple, un job pour envoyer un email échouera sans l'adresse email du destinataire.
* Timeout : Un job pourrait être échoué par le mécanisme de file d'attente s'il prend plus de temps que d'habitude. Cela pourrait être dû à un problème sur une dépendance du job ou autre chose, mais généralement vous ne voulez pas qu'un seul job s'exécute indéfiniment.
* Problèmes de réseau ou d'infrastructure : Ces problèmes sont presque hors de votre contrôle, mais ils arrivent. Une erreur de connexion à la base de données, par exemple, échouerait un job.
* Problèmes de dépendance : Parfois, un job dépend de certaines ressources externes pour fonctionner correctement. Chaque fois que ces autres ressources sont indisponibles ou sans succès, le job échouera.

Lorsque les jobs échouent, vous pouvez configurer votre mécanisme de file d'attente pour les réessayer. Vous pouvez soit réessayer le job immédiatement, soit après un temps calculé. Vous pouvez définir un nombre maximum de tentatives, ce qui est recommandé. Sinon, vous finissez par exécuter un job qui échouera toujours indéfiniment.

## Pourquoi Utiliser les Files d'Attente ?

Les files d'attente sont utiles pour créer des canaux de communication robustes entre les microservices. Plusieurs services peuvent utiliser la même file d'attente. Différents services pourraient être chargés de différents problèmes. Lorsqu'un service termine sa tâche, il peut pousser un job vers un autre service qui a des workers en attente de ce job. Ce service le prendra et fera ce qui est nécessaire avec les données.

Les files d'attente sont également utiles pour déleser les tâches lourdes d'un processus. Comme vous le verrez dans cet article, une tâche chronophage comme l'envoi d'un email peut être mise dans une file d'attente pour éviter de ralentir le temps de réponse.

Les files d'attente aident à éviter les points de défaillance uniques. Un processus qui a la capacité d'échouer et peut être réessayé est mieux traité en utilisant une file d'attente où il peut être réessayé après un certain temps.

## Comment Construire une Application Simple qui Utilise les Files d'Attente

Dans cet article, nous allons construire un projet simple en utilisant Node.js et [Redis](https://redis.io/). Nous allons utiliser la bibliothèque [Bull](https://optimalbits.github.io/bull/) car elle simplifie beaucoup des complexités impliquées dans la construction d'un système de file d'attente. Le projet aura un seul endpoint pour envoyer des emails.

### Créer un Nouveau Projet Node.js

```shell
mkdir nodejs-queue-project
cd nodejs-queue-project
npm init -y
```

Les commandes ci-dessus créeront un nouveau dossier nommé `nodejs-queue-project` et un fichier `package.json` dedans. Le fichier `package.json` devrait ressembler à ceci :

```json
{
  "name": "nodejs-queue-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}

```

### Installer les Dépendances Requises

```shell
npm i express @types/express @types/node body-parser ts-node ts-lint typescript nodemon nodemailer @types/nodemailer
```

Les commandes ci-dessus installeront les différents packages et dépendances requis pour le projet.

Après l'installation, vous pouvez mettre à jour la section `scripts` de votre `package.json` pour avoir une commande `dev`. Votre fichier `package.json` complet devrait maintenant ressembler à ceci :

```json
{
  "name": "nodejs-queue-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "nodemon src/app.ts"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@types/express": "^4.17.17",
    "@types/node": "^20.3.3",
    "@types/nodemailer": "^6.4.8",
    "body-parser": "^1.20.2",
    "express": "^4.18.2",
    "nodemailer": "^6.9.3",
    "nodemon": "^2.0.22",
    "ts-lint": "^4.5.1",
    "ts-node": "^10.9.1",
    "typescript": "^5.1.6"
  }
}

```

Le fichier ci-dessus montre toutes vos dépendances installées. La commande `npm run dev` s'exécutera lorsque vous utiliserez le script `dev`.

## Comment Construire l'Endpoint

La première chose à faire est de créer un nouveau dossier nommé `src`. Ce dossier contiendra tous vos fichiers de code. Le premier fichier qu'il contiendra est le fichier racine de l'application — le fichier `app.ts` comme défini dans le fichier `package.json`.

Nous utiliserons le fichier `app.ts` pour importer les packages requis et créer un serveur simple avec un seul endpoint pour envoyer un email comme vu ci-dessous :

```ts
import express from "express";
import bodyParser from "body-parser";
import nodemailer from "nodemailer";

const app = express();

app.use(bodyParser.json());

app.post("/send-email", async (req, res) => {
  const { from, to, subject, text } = req.body;

  // Utiliser un compte de test car ceci est un tutoriel
  const testAccount = await nodemailer.createTestAccount();

  const transporter = nodemailer.createTransport({
    host: "smtp.ethereal.email",
    port: 587,
    secure: false,
    auth: {
      user: testAccount.user,
      pass: testAccount.pass,
    },
    tls: {
      rejectUnauthorized: false,
    },
  });

  console.log("Envoi de mail à %s", to);

  let info = await transporter.sendMail({
    from,
    to,
    subject,
    text,
    html: `<strong>${text}</strong>`,
  });

  console.log("Message envoyé : %s", info.messageId);
  console.log("URL de prévisualisation : %s", nodemailer.getTestMessageUrl(info));

  res.json({
    message: "Email envoyé",
  });
});

app.listen(4300, () => {
  console.log("Serveur démarré à http://localhost:4300");
});

```

Maintenant, vous pouvez démarrer votre serveur en exécutant `npm run dev` dans votre terminal. Vous devriez voir un message disant `Serveur démarré à [http://localhost:4300](http://localhost:4300)` dans votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-17.41.33.png)
_message npm run dev_

Vous pouvez maintenant tester l'endpoint en utilisant un outil comme Postman :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-17.30.33.png)
_Test de l'endpoint sur Postman_

La requête a pris presque 4 secondes comme montré dans la capture d'écran. C'est très lent pour un endpoint. Si vous regardez votre terminal, vous devriez également voir une URL où vous pouvez prévisualiser l'email qui a été envoyé.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-17.43.01.png)

Ouvrir le lien vous permet de voir à quoi ressemble l'email.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-17.43.47.png)
_Contenu de l'email_

## Comment Créer la File d'Attente

Pour rendre le processus encore plus rapide, l'email peut être mis en file d'attente pour être envoyé plus tard et une réponse envoyée à l'utilisateur immédiatement.

Pour ce faire, installez la bibliothèque `bull` et sa bibliothèque `@types` car nous l'utiliserons pour créer une file d'attente. C'est-à-dire :

```shell
npm i bull @types/bull
```

Créer une nouvelle file d'attente en utilisant `bull` est aussi simple que d'instancier un nouvel objet `Bull` avec un nom pour la file d'attente :

```ts
// Cela va en haut de votre fichier
import Bull from 'bull';

const emailQueue = new Bull("email");

```

Lorsque la file d'attente est créée avec juste le nom de la file d'attente, elle essaie d'utiliser l'URL de connexion Redis par défaut : `localhost:6379`. Si vous préférez utiliser une URL différente, passez simplement un deuxième objet à la classe `Bull` en tant qu'objet d'options :

```ts
const emailQueue = new Bull("email", {
  redis: "localhost:6379",
});
```

À ce stade, vous pouvez créer une fonction simple pour servir de producteur de jobs et ajouter un job à la file d'attente chaque fois qu'une requête arrive.

```ts
type EmailType = {
  from: string;
  to: string;
  subject: string;
  text: string;
};

const sendNewEmail = async (email: EmailType) => {
  emailQueue.add({ ...email });
};
```

Cette fonction nouvellement créée, `sendNewEmail`, accepte un objet contenant les détails du nouvel email à envoyer de type `EmailType`. Il y a l'adresse email de l'expéditeur (`from`), l'adresse email du destinataire (`to`), le `sujet` de l'email, et le contenu de l'email (`text`). Ensuite, elle pousse un nouveau job dans la file d'attente.

Vous pouvez utiliser cette fonction au lieu d'envoyer l'email pendant la requête maintenant. Modifiez l'endpoint pour faire ceci :

```ts
app.post("/send-email", async (req, res) => {
  const { from, to, subject, text } = req.body;

  await sendNewEmail({ from, to, subject, text });

  console.log("Ajouté à la file d'attente");

  res.json({
    message: "Email envoyé",
  });
});
```

À ce stade, le code est plus simple et le processus est plus rapide. La requête ne prend qu'environ 40 ms — environ 100 fois plus rapide qu'avant.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-18.25.40.png)
_Test de l'endpoint avec Postman_

À ce stade, l'email est ajouté à une file d'attente. Il restera dans la file d'attente jusqu'à ce qu'il soit traité. Le job peut être traité par la même application ou un autre service (si dans une [configuration de microservices](https://www.freecodecamp.org/news/microservices-architecture-for-humans/)).

## Comment Traiter les Jobs

Le cycle est incomplet et inutile si les emails ne quittent jamais la file d'attente. Nous allons créer un consommateur de jobs pour traiter les jobs et vider la file d'attente.

Nous pouvons faire cela en créant la logique pour une fonction qui accepte un objet `Job` et envoie l'email :

```ts
const processEmailQueue = async (job: Job) => {
  // Utiliser un compte de test car ceci est un tutoriel
  const testAccount = await nodemailer.createTestAccount();

  const transporter = nodemailer.createTransport({
    host: "smtp.ethereal.email",
    port: 587,
    secure: false,
    auth: {
      user: testAccount.user,
      pass: testAccount.pass,
    },
    tls: {
      rejectUnauthorized: false,
    },
  });

  const { from, to, subject, text } = job.data;

  console.log("Envoi de mail à %s", to);

  let info = await transporter.sendMail({
    from,
    to,
    subject,
    text,
    html: `<strong>${text}</strong>`,
  });

  console.log("Message envoyé : %s", info.messageId);
  console.log("URL de prévisualisation : %s", nodemailer.getTestMessageUrl(info));
  
  return nodemailer.getTestMessageUrl(info);
};
```

La fonction ci-dessus accepte un objet `Job`. L'objet a des propriétés utiles qui montrent le statut et les données d'un job. Ici, nous utilisons la propriété `data`.

À ce stade, tout ce que nous avons est une fonction. Elle ne récupère pas les jobs automatiquement car elle ne sait pas avec quelle file d'attente travailler.

Avant de la connecter à la file d'attente, vous pouvez continuer à ajouter quelques jobs à la file d'attente en envoyant quelques requêtes. Vous pouvez vérifier les jobs d'email actuellement en file d'attente en exécutant cette commande dans votre `redis-cli` :

```shell
LRANGE bull:email:wait 0 -1
```

Cela vérifie la liste d'attente des emails, et retourne les `ids` des jobs en attente.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-18.47.35.png)
_Redis CLI_

J'ai créé quelques jobs juste pour montrer comment les workers fonctionnent réellement.

Maintenant, connectez le worker à la file d'attente en ajoutant cette ligne de code :

```ts
emailQueue.process(processEmailQueue);
```

Voici à quoi votre fichier `app.ts` devrait maintenant ressembler après cela :

```ts
import express from "express";
import bodyParser from "body-parser";
import nodemailer from "nodemailer";
import Bull, { Job } from "bull";

const app = express();

app.use(bodyParser.json());

const emailQueue = new Bull("email", {
  redis: "localhost:6379",
});

type EmailType = {
  from: string;
  to: string;
  subject: string;
  text: string;
};

const sendNewEmail = async (email: EmailType) => {
  emailQueue.add({ ...email });
};

const processEmailQueue = async (job: Job) => {
  // Utiliser un compte de test car ceci est un tutoriel
  const testAccount = await nodemailer.createTestAccount();

  const transporter = nodemailer.createTransport({
    host: "smtp.ethereal.email",
    port: 587,
    secure: false,
    auth: {
      user: testAccount.user,
      pass: testAccount.pass,
    },
    tls: {
      rejectUnauthorized: false,
    },
  });

  const { from, to, subject, text } = job.data;

  console.log("Envoi de mail à %s", to);

  let info = await transporter.sendMail({
    from,
    to,
    subject,
    text,
    html: `<strong>${text}</strong>`,
  });

  console.log("Message envoyé : %s", info.messageId);
  console.log("URL de prévisualisation : %s", nodemailer.getTestMessageUrl(info));
};

emailQueue.process(processEmailQueue);

app.post("/send-email", async (req, res) => {
  const { from, to, subject, text } = req.body;

  await sendNewEmail({ from, to, subject, text });

  console.log("Ajouté à la file d'attente");

  res.json({
    message: "Email envoyé",
  });
});

app.listen(4300, () => {
  console.log("Serveur démarré à http://localhost:4300");
});

```

Une fois que vous avez sauvegardé, vous remarquerez que le serveur redémarre et commence immédiatement à envoyer des emails. Cela est dû au fait que le worker voit la file d'attente et commence à la traiter immédiatement.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-01-at-18.51.14.png)
_Serveur envoyant les emails en file d'attente_

Maintenant, le producteur et le worker sont tous deux actifs. Chaque nouvelle requête API sera poussée dans la file d'attente, et le worker la traitera immédiatement sauf s'il y a déjà des jobs en attente.

## **Résumé**

J'espère que cet article vous a aidé à comprendre ce qu'est une file d'attente de messages, comment ajouter des jobs et créer des processus pour les exécuter, et comment vous pouvez les utiliser pour construire de meilleures applications web. Vous pouvez trouver les fichiers de code utilisés dans cet article sur [GitHub](https://github.com/Zubs/php-redis).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me connecter sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), et [Github](https://github.com/Zubs). C'est rapide, c'est facile, et c'est gratuit !