---
title: Comment envoyer une newsletter par e-mail avec l'API SendGrid
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2020-12-14T18:07:58.000Z'
originalURL: https://freecodecamp.org/news/send-email-newsletter-with-the-sendgrid-api
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd3a6ebe6787e098393da0c.jpg
tags:
- name: email
  slug: email
- name: node js
  slug: node-js
- name: sendgrid
  slug: sendgrid
- name: TypeScript
  slug: typescript
seo_title: Comment envoyer une newsletter par e-mail avec l'API SendGrid
seo_desc: "For years, Quincy Larson sent a weekly email newsletter through freeCodeCamp's\
  \ Mail for Good platform, which is powered by Amazon SES. \nHe recently migrated\
  \ this process to SendGrid. In this article, I will show you how I built a tool\
  \ to accomplish t..."
---

Pendant des années, Quincy Larson a envoyé une newsletter hebdomadaire par e-mail via la plateforme [Mail for Good](https://github.com/freeCodeCamp/mail-for-good) de freeCodeCamp, qui est alimentée par Amazon SES. 

Il a récemment migré ce processus vers [SendGrid](https://sendgrid.com). Dans cet article, je vais vous montrer comment j'ai construit un outil pour accomplir cela.

## Comment configurer un compte SendGrid

La première étape consiste à [s'inscrire à SendGrid](https://signup.sendgrid.com/) et à configurer votre compte. Pour les besoins de ce tutoriel, le niveau gratuit devrait suffire.

À mesure que vous développez votre application, vous devrez peut-être augmenter vos limites d'e-mails disponibles via la plateforme.

## Comment configurer une adresse IP dédiée sur SendGrid

Par défaut, SendGrid utilise des adresses IP partagées pour envoyer des e-mails. Cela peut être acceptable pour des applications d'e-mails à plus petite échelle, mais à mesure que vous augmentez vos taux d'envoi, vous devrez configurer une adresse IP dédiée. 

C'est une bonne idée, car votre "réputation d'expéditeur" (la métrique que SendGrid utilise pour évaluer votre position auprès des fournisseurs de services de messagerie) ne sera pas négativement impactée par les actions d'autres utilisateurs qui partagent la même IP.

Pour configurer votre propre IP dédiée, sélectionnez l'option "Paramètres" dans le menu de navigation latéral, puis sélectionnez "Adresses IP". Juste une petite note, cependant : cette option n'est pas disponible sur le niveau gratuit. 

Selon votre plan payant, vous avez peut-être déjà une adresse IP dédiée configurée. Si vous n'en avez pas, ou si vous choisissez d'en ajouter plus, vous pouvez sélectionner le bouton "Ajouter une adresse IP" pour configurer une nouvelle IP.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-87.png)
_Menu de paramétrage pour les adresses IP_

## Comment autoriser un expéditeur d'e-mail dans SendGrid

_NOTE : vous pouvez ignorer cette section si vous utilisez un domaine personnalisé pour vos e-mails._

Pour envoyer des e-mails depuis votre adresse e-mail personnelle, vous devrez vérifier que l'adresse e-mail vous appartient.

Dans le menu de gauche, sélectionnez "Paramètres", puis "Authentification de l'expéditeur". Choisissez "Vérifier un expéditeur unique" pour suivre le processus d'ajout de votre adresse e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-98.png)
_Option Expéditeur unique_

## Comment authentifier votre domaine personnalisé dans SendGrid

_NOTE : vous pouvez ignorer cette section si vous n'utilisez PAS de domaine personnalisé pour vos e-mails._

Afin d'envoyer des e-mails depuis votre domaine de messagerie personnalisé, vous devrez authentifier ce domaine avec SendGrid. Pour accéder à cet écran, sélectionnez à nouveau le menu Paramètres, puis sélectionnez "Authentification de l'expéditeur".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-88.png)
_Menu de paramétrage pour l'authentification de l'expéditeur_

Vous devriez alors voir un écran avec une option pour "Authentification de domaine". Sélectionnez l'option "Authentifier votre domaine" et SendGrid vous guidera tout au long du processus de configuration de vos enregistrements DNS (avec des instructions spécifiques basées sur votre fournisseur DNS). 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-91.png)
_Page des paramètres d'authentification de l'expéditeur_

## Comment configurer le DNS inverse dans SendGrid

_NOTE : vous pouvez ignorer cette section si vous n'utilisez pas de domaine personnalisé pour vos e-mails._

Le DNS inverse (Domain Name System) est utilisé par les fournisseurs de messagerie pour rechercher le propriétaire d'une adresse IP donnée. La configuration de cela permettra aux fournisseurs de messagerie de vérifier que l'adresse IP à partir de laquelle vous envoyez un e-mail est connectée à votre domaine personnalisé.

Dans le même écran d'authentification de l'expéditeur que ci-dessus, vous verrez une section "DNS inverse". Il y aura une option pour configurer le DNS inverse pour chaque IP dédiée que vous avez sur votre compte - comme pour l'authentification de domaine, la plateforme de SendGrid vous guidera tout au long de la configuration.

## Comment configurer l'authentification des e-mails dans SendGrid

_NOTE : vous pouvez ignorer cette section si vous n'utilisez pas de domaine personnalisé pour vos e-mails._

Les principaux fournisseurs de messagerie (tels que Gmail, Yahoo et Outlook) utilisent plusieurs méthodes pour authentifier l'expéditeur d'un e-mail : SPF, DKIM et DMARC.

* **SPF** (Sender Policy Framework) valide que l'adresse IP envoyant un courrier depuis votre domaine est autorisée à le faire.
* **DKIM** (DomainKeys Identified Mail) utilise des chaînes de clés publiques pour authentifier qu'une adresse e-mail `from` est exacte et non usurpée/falsifiée.
* **DMARC** (Domain-based Message Authentication, Reporting, and Conformance) est un ensemble d'instructions qui indiquent aux fournisseurs de messagerie comment réagir lorsqu'un e-mail échoue aux validations SPF ou DKIM.

Le flux d'authentification de SendGrid vous guidera tout au long de la configuration de SPF et DKIM dans le cadre du processus d'authentification de domaine, mais vous devrez configurer votre DMARC manuellement. 

Visitez votre fournisseur d'hébergement DNS et accédez aux paramètres de gestion DNS. À partir de là, ajoutez un nouvel enregistrement `TXT` avec un nom de `_dmarc.votredomaine.com` (en remplaçant `votredomaine.com` par votre domaine personnalisé). 

Notez que certains fournisseurs, comme GoDaddy, ajouteront automatiquement votre domaine à l'enregistrement - dans ce cas, le nom doit être `_dmarc`. 

La _valeur_ de cet enregistrement doit prendre une structure similaire à :

```text
"v=DMARC1; p=none; pct=100; rua=mailto:dmarc@votredomaine.com"
```

* `v=DMARC` indique la version des règles DMARC à utiliser (actuellement seule la Version 1 est disponible).
* `p=none` indique l'action qu'un fournisseur de messagerie doit prendre lorsqu'un e-mail échoue à DKIM ou SPF. Ce paramètre doit commencer par `none`, pour éviter d'impacter la délivrabilité de vos e-mails. Une fois que vous avez confirmé que votre DKIM et SPF sont configurés correctement, vous pouvez mettre à jour cette valeur à `quarantine` pour que les fournisseurs routent automatiquement les e-mails échoués vers le dossier spam, ou `reject` pour que les fournisseurs rejettent/renvoient les e-mails échoués.
* `pct=100` indique le pourcentage d'e-mails échoués auxquels l'action doit être appliquée.
* `rua=mailto:dmarc@votredomaine.com` est l'adresse e-mail à laquelle envoyer les rapports agrégés. Ces rapports contiennent des informations sur tous les e-mails de vos IP qui ont été reçus par un fournisseur donné. Remplacez `dmarc@votredomaine.com` par l'adresse e-mail à laquelle vous souhaitez recevoir ces rapports.

## Comment créer un modèle dynamique dans SendGrid

L'outil que nous allons construire aujourd'hui utilise la fonction de modèle dynamique de SendGrid pour définir le sujet et le texte du corps d'un e-mail. Pour configurer cela, sélectionnez l'option "Email API" dans le menu de navigation latéral, puis choisissez "Dynamic Templates".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-92.png)
_Menu de paramétrage pour les modèles dynamiques_

Vous verrez un écran avec une invite pour créer votre premier modèle dynamique. Sélectionnez l'option "Créer un modèle dynamique". 

Donnez un nom à votre nouveau modèle : "Tutoriel SendGrid freeCodeCamp". SendGrid ajoutera ce modèle à une liste de modèles disponibles. Sélectionnez le modèle pour voir l'`ID de modèle` (notez cela, car nous en aurons besoin pour l'outil plus tard) et cliquez sur le bouton "Ajouter une version".

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-93.png)
_Aperçu du modèle nouvellement ajouté_

Sélectionnez "Modèle vide" sur l'écran qui apparaît, puis choisissez "Éditeur de code". Vous devriez maintenant voir la vue de l'éditeur. L'éditeur de SendGrid utilise HTML pour construire le corps de l'e-mail - cependant, lorsque nous construirons notre outil, nous enverrons la version en texte brut. 

Pour l'instant, remplacez le contenu de l'éditeur par le code suivant :

```html
<p>Ceci est un e-mail de test utilisé avec le tutoriel SendGrid de freeCodeCamp</p>
<p>Se désabonner : {{{unsubscribeId}}}</p>
```

Vous remarquerez que nous avons ajouté `{{{unsubscribeId}}}`. Le modèle de SendGrid utilise Handlebars pour remplacer dynamiquement les valeurs - nous utiliserons cette fonctionnalité lorsque nous construirons l'outil. 

Maintenant, sélectionnez l'option des paramètres en haut à gauche - vous pouvez éventuellement donner un nom à votre version de modèle, mais le champ "Sujet" est ce que nous voulons modifier. Définissez cette valeur à `{{{subject}}}` pour charger dynamiquement la valeur du sujet depuis notre outil.

Pour tester le modèle dynamique, sélectionnez l'option "Données de test" dans le menu supérieur. Insérez ces données JSON dans l'éditeur :

```json
{
    "unsubscribeId": "1",
    "subject": "Test des e-mails !"
}
```

Vous devriez maintenant voir l'aperçu sur le côté droit de l'écran refléter ces valeurs dans le modèle. N'oubliez pas de cliquer sur le bouton `Enregistrer` pour sauvegarder vos modifications !

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-94.png)
_Écran de l'éditeur et de l'aperçu montrant le chargement dynamique des valeurs du modèle_

## Comment générer une clé API dans SendGrid

La dernière étape de la configuration de votre compte SendGrid consiste à générer une clé API pour que notre outil l'utilise. 

Cliquez sur la flèche de retour en haut à gauche pour revenir à la page principale de SendGrid. Ensuite, sélectionnez "Paramètres" et "Clés API". Choisissez "Créer une clé API" pour générer une nouvelle clé. Vous pouvez éventuellement accorder un "Accès complet" à votre clé, mais pour les besoins de ce tutoriel, vous n'aurez besoin que de l'accès "Envoi de mail". 

Assurez-vous de donner à votre clé un nom descriptif afin de vous souvenir de son but si vous accédez à nouveau à cet écran. Une fois vos permissions configurées, sélectionnez "Créer et afficher" pour générer la clé - **sauvegardez-la quelque part en sécurité car vous ne pourrez plus la consulter**.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-95.png)
_Écran de création de l'API avec la permission d'envoi de mail activée_

## Comment construire l'outil d'e-mail

Il est maintenant temps d'écrire le code pour envoyer réellement des e-mails. Vous pouvez [voir le code de notre application en direct](https://github.com/nhcarrigan/sendgrid-email-blast), mais pour les besoins de ce tutoriel, nous allons construire une [version légèrement réduite](https://github.com/nhcarrigan/fcc-sendgrid-tutorial) pour nous concentrer principalement sur l'utilisation de l'API SendGrid.

### Logiciel requis pour un script de campagne e-mail personnalisé

Vous devrez avoir les outils suivants installés pour travailler sur ce projet :

* [Node.js](https://nodejs.org/en/) - la version LTS est recommandée
* Un IDE, tel que [VSCode](https://code.visualstudio.com) ou [Atom](https://atom.io/)

Vous pouvez également optionnellement vouloir `git` pour le contrôle de version. 

Notre outil en direct utilise un cluster MongoDB Atlas, mais notre exemple de tutoriel ne le fera pas. Si vous n'êtes pas familier avec MongoDB, le programme de freeCodeCamp comprend [une excellente section sur la configuration et l'utilisation de MongoDB](https://www.freecodecamp.org/learn/apis-and-microservices/mongodb-and-mongoose/).

### Comment initialiser le projet

Créez un répertoire (dossier) dans lequel travailler sur ce projet. Ensuite, ouvrez ce dossier avec votre éditeur et terminal de choix.

Pour commencer, nous devons configurer cela comme un projet Node. Le moyen le plus rapide de le faire est avec `npm init` dans votre terminal. Cela vous guidera tout au long de la création d'un `package.json` qui est le fichier central d'une application Node. 

Les valeurs par défaut fonctionneront bien pour notre application, mais nous voudrons modifier la section `scripts` :

```json
  "scripts": {
    "build": "tsc",
    "send": "node ./prod/send.js"
  },
```

Le script `build` sera utilisé pour compiler notre TypeScript en JavaScript, et le script `send` exécutera notre application.

Ensuite, nous installerons et configurerons [TypeScript](https://www.typescriptlang.org/). Si vous n'êtes pas familier avec TypeScript, il s'agit essentiellement d'un sur-ensemble de JavaScript avec des définitions de types plus fortes et une vérification des erreurs à la compilation. 

Pour installer TypeScript sur votre projet, exécutez `npm install --save-dev typescript` dans votre terminal. (Le drapeau `--save-dev` l'enregistre comme une dépendance de développement - TypeScript n'est pas requis à l'exécution et peut donc être nettoyé dans un environnement de production). 

TypeScript nécessite son propre fichier de configuration pour définir les règles qu'il doit suivre lors de la génération des fichiers JavaScript. Créez un fichier dans le répertoire racine de votre projet appelé `tsconfig.json` et insérez ce qui suit :

```json
{
    "compilerOptions": {
      "target": "es5",
      "module": "commonjs",
      "strict": true,
      "esModuleInterop": true,
      "skipLibCheck": true,
      "forceConsistentCasingInFileNames": true,
      "outDir": "./prod",
      "rootDir": "./src"
    }
  }
```

Pour des raisons de brièveté, nous n'entrerons pas dans ces paramètres de configuration. Si vous souhaitez des informations supplémentaires, TypeScript dispose d'une [documentation très approfondie](https://www.typescriptlang.org/docs/).

Si vous utilisez `git` pour le contrôle de version et que vous téléchargez cela vers un dépôt (tel que GitHub), vous voudrez créer un fichier `.gitignore` dans le répertoire racine de votre projet. Ce fichier doit contenir :

```txt
/node_modules/
.env
/prod/
```

* `/node_modules/` ignorera les packages installés. Cela est considéré comme une bonne pratique lors de l'utilisation du contrôle de version.
* `.env` ignorera notre fichier de variables d'environnement. Cela est très important car vous ne voulez _jamais_ commettre vos secrets dans un dépôt.
* `/prod/` ignorera nos fichiers JavaScript compilés. Nous utiliserons également ce dossier pour nos listes d'e-mails, il est donc important d'éviter de commettre accidentellement ces informations identifiables privées.

Créez un fichier `.env` dans le répertoire racine de votre projet. Nous chargerons les variables d'environnement suivantes via ce fichier :

```txt
SENDGRID_API_KEY=
SENDGRID_FROM=
SENDGRID_TEMPLATE_ID=

MAIL_SUBJECT=
```

* `SENDGRID_API_KEY` doit être la clé API que vous avez générée dans les étapes précédentes.
* `SENDGRID_FROM` doit être votre adresse e-mail (c'est l'adresse utilisée pour le champ `from`).
* `SENDGRID_TEMPLATE_ID` doit être la chaîne `id` pour le modèle dynamique que vous avez créé précédemment.
* `MAIL_SUBJECT` sera la ligne d'objet pour les e-mails que vous envoyez. Pour l'instant, définissez cela comme "Email du tutoriel fCC".

Enfin, créez un dossier `src` dans le répertoire racine de votre projet, et créez un fichier `send.ts` dans ce dossier.

### Comment installer vos dépendances

Tout d'abord, nous devons installer le package `sendgrid` Node.js. Ce package sert de wrapper pour l'API SendGrid et simplifiera notre processus de réalisation d'appels API pour envoyer des e-mails. Exécutez `npm install @sendgrid/mail` pour installer ce package.

Ensuite, nous avons besoin de quelques dépendances de développement. Exécutez `npm install --save-dev dotenv @types/node`.

* `dotenv` nous permettra de charger les variables d'environnement depuis le fichier `.env` localement.
* `@types/node` fournit des définitions de type pour Node.js - TypeScript s'appuie sur ces définitions pour comprendre la structure des méthodes et fonctions intégrées.

### Comment écrire la logique

Maintenant, nous allons travailler dans notre fichier `/src/send.ts` - c'est là que nous construisons la majeure partie de la logique de notre application. Nous commencerons par importer les valeurs requises depuis nos packages.

Tout d'abord, nous voulons charger le package `dotenv` et analyser nos variables d'environnement.

```ts
import dotenv from "dotenv";
dotenv.config();
```

L'appel `dotenv.config()` lit notre fichier `.env` et charge les valeurs dans l'objet Node `process.env`.

Ensuite, nous importons les modules requis depuis le package SendGrid :

```ts
import sgMail, { MailDataRequired } from "@sendgrid/mail";
```

`sgMail` est le wrapper principal de l'API, et `MailDataRequired` est une définition de type dont nous aurons besoin.

Enfin, nous importons certaines fonctionnalités intégrées de Node pour gérer nos fichiers :

```ts
import path from "path";
import { createWriteStream, readFile } from "fs";
```

* `path` sera utilisé pour localiser nos fichiers de liste d'e-mails avec des chemins relatifs
* `fs` sera utilisé pour lire et écrire dans ces fichiers

Il est temps de commencer à construire la logique ! Notre application repose sur certaines valeurs essentielles définies dans le fichier `.env`, nous devons donc commencer par valider que ces variables sont correctement définies. Si certaines sont manquantes, nous voulons que notre application se termine tôt pour éviter de générer des erreurs lorsque nous envoyons les e-mails.

```ts
// Ici, nous vérifions la présence d'une clé API valide
const apiKey = process.env.SENDGRID_API_KEY;
if (!apiKey) {
  console.error("Clé SendGrid manquante");
  process.exit(1);
}

// Ici, nous vérifions la présence d'une adresse d'expéditeur valide
const fromAddress = process.env.SENDGRID_FROM;
if (!fromAddress) {
  console.error("Adresse e-mail de l'expéditeur manquante !");
  process.exit(1);
}

// Ici, nous vérifions la présence d'un ID de modèle dynamique
const sgTemplate = process.env.SENDGRID_TEMPLATE_ID;
if (!sgTemplate) {
  console.error("ID de modèle SendGrid manquant");
  process.exit(1);
}

// Ici, nous vérifions la présence de l'objet du mail, mais s'il est manquant
// nous n'avons pas besoin de quitter. Au lieu de cela, nous utilisons une valeur de repli.
const subjectValue = process.env.MAIL_SUBJECT || "Valeur de repli - vérifiez votre env !";
```

L'appel `process.exit(1)` que vous voyez dans chaque vérification de condition indique à Node de terminer le processus (notre application) avec un code de sortie de `1`. Cela indique que notre application a planté en raison de l'échec de l'une de ces vérifications.

SendGrid nous oblige à définir la clé API. Sous votre logique de variable d'environnement, ajoutez l'appel de fonction pour définir la clé.

```ts
// Ici, nous définissons la clé API SendGrid
sgMail.setApiKey(apiKey);
```

Avant de continuer, allez-y et exécutez `npm run build` dans votre terminal - cela créera un dossier `prod` contenant notre JavaScript compilé. Vous devriez maintenant voir la structure de fichier suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-96.png)
_Arborescence des fichiers à ce stade du tutoriel_

**À ce stade, si vous utilisez `git`, vous devez être _très sûr_ que le dossier `prod` ne sera pas commis dans votre dépôt.** 

Dans le dossier `prod`, créez un fichier `validEmails.csv`. Notre application utilisera ce fichier pour lire la liste des e-mails. Initialisez le fichier avec le contenu suivant (remplacez `votre@email.com` par votre véritable adresse e-mail) :

```csv
email,unsubscribeId
votre@email.com,1
iama@fake.email,2
```

Maintenant, nous pouvons écrire le code pour analyser cela dans une liste d'e-mails ! Dans votre fichier `src/send.ts`, ajoutez ce code :

```
// Ici, nous concaténons notre chemin de fichier pour le fichier d'e-mails valides
const filePath = path.join(__dirname + "/../validEmails.csv");

// C'est ici que nous commençons à lire le fichier !
readFile(filePath, "utf8", (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data)
});
```

Maintenant, si vous exécutez `npm run build` et `npm run send`, vous devriez voir le contenu de notre fichier `validEmail.csv` dans le terminal. Si vous le souhaitez, vous pouvez [voir notre progression actuelle jusqu'à ce point](https://github.com/naomis-archive/fcc-sendgrid-tutorial/blob/main/tutorial-steps/step-1.ts). 

Super ! Maintenant, nous devons analyser cette chaîne en un tableau d'objets afin de pouvoir itérer à travers et construire nos messages électroniques. Mettons à jour notre fonction de rappel :

```
// C'est ici que nous commençons à lire le fichier !
readFile(filePath, "utf8", (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
  // Ici, nous analysons les données en un tableau d'objets
  const emailList = data
    .split("\n")
    .slice(1)
    .map((el) => {
      const [email, unsubscribeId] = el.split(",");
      return { email, unsubscribeId };
    });
});
```

* `.split("\n")` divise la chaîne par les sauts de ligne. **NOTE** : Si vous êtes sous Windows, vous devrez peut-être changer le paramètre de fin de ligne pour votre `validEmails.csv` de `CRLF` à `LF` (Windows insère des caractères de saut de ligne supplémentaires qui affecteront notre gestion des données)
* `.slice(1)` supprime le premier élément de ce tableau (notre ligne `email,unsubscribeId`).
* Notre fonction `map` convertira chaque chaîne `email,unsubscribeId` en un objet `{email, unsubscribeId}`.

Le résultat final de cette fonction d'analyse sera un tableau d'objets avec les propriétés `email` et `unsubscribeId` - beaucoup plus facile à utiliser qu'une chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-97.png)
_Exemple de sortie de la fonction d'analyse_

Il est maintenant temps d'envoyer quelques e-mails. Sous votre fonction d'analyse (mais toujours dans le rappel `readFile`), ajoutez la structure de notre méthode d'itération. Comme nous voulons accéder à chaque valeur dans le tableau, nous utiliserons l'approche `.forEach`.

```ts
  // Ici, nous itérons à travers le tableau emailList
  emailList.forEach((user) => {});
```

Dans le rappel pour le `.forEach`, nous pouvons construire l'objet message que l'API SendGrid attend. 

```ts
  // Ici, nous itérons à travers le tableau emailList
  emailList.forEach((user) => {

    // Ceci est l'objet message dont SendGrid a besoin
    const message: MailDataRequired = {
        to: user.email,
        from: fromAddress,
        subject: subjectValue,
        text: "Ceci disparaît !",
        templateId: sgTemplate,
        dynamicTemplateData: {
            subject: subjectValue,
            unsubscribeId: user.unsubscribeId
        }
    }
    
  });
```

Avant de continuer, examinons de plus près cet objet message. Le `MailDataRequired` que nous avons importé précédemment est utilisé comme définition de type ici, donc TypeScript peut nous alerter si nous manquons une propriété requise. Heureusement, nous avons toutes les propriétés requises. Mais que signifient-elles ?

* `to:` L'adresse e-mail à laquelle envoyer le message. Ce sera l'`email` de chaque ligne de notre fichier `validEmails.csv`
* `from:` L'adresse e-mail à partir de laquelle envoyer le message. Cela est défini dans notre `.env` précédemment (ce devrait être _votre_ adresse e-mail).
* `subject:` Ce champ n'est pas requis, mais nous donne une valeur de repli au cas où le modèle dynamique ne parse pas correctement notre sujet.
* `text:` Cette valeur de texte est écrasée par le modèle. Cependant, il est toujours important de l'utiliser. SendGrid peut envoyer des e-mails en `texte brut` ou en `html` - en utilisant la propriété `text` au lieu de la propriété `html`, nous nous assurons que notre modèle est envoyé en `texte brut`. Les fournisseurs de messagerie sont _plus susceptibles_ de marquer les messages HTML comme spam, donc cela aide à augmenter notre taux de délivrabilité.
* `templateId:` Il s'agit de l'ID du modèle dynamique que SendGrid doit utiliser dans l'e-mail.
* `dynamicTemplateData:` Ce sont les valeurs qui correspondent à nos chaînes Handlebars que nous avons définies dans le modèle dynamique précédemment. 

Super ! Notre prochaine étape consiste à prendre ce message construit et à l'envoyer. Sous l'objet message (mais toujours dans le rappel `.forEach`), ajoutons notre appel d'envoi :

```ts
    // Ici, nous envoyons le message que nous venons de construire !
    sgMail.send(message);
```

Cela enverra le message à chacun des e-mails de notre `validEmails.csv`. Malheureusement, notre code s'exécutera silencieusement et nous ne saurons pas si chaque envoi a réussi ou non. Ajoutons une gestion des erreurs. 

L'appel `.send()` retourne une Promesse, donc nous pouvons utiliser `.then().catch()` pour gérer le retour.

```ts
    // Ici, nous envoyons le message que nous venons de construire !
    sgMail.send(message)
        .then(() => {
            // Ici, nous enregistrons les demandes d'envoi réussies
            console.info(`Envoi du message réussi : ${user.email}`)
        }).catch((err) => {
            // Ici, nous enregistrons les demandes d'envoi en erreur
            console.error(err);
            console.error(`Échec de l'envoi du message : ${user.email}`)
        });
```

Maintenant, si vous exécutez `npm run build` et `npm run send`, vous devriez voir un bel e-mail dans votre boîte de réception !

À ce stade, vous avez maintenant une application fonctionnelle d'envoi d'e-mails. Félicitations ! Vous pouvez [voir notre progression jusqu'à ce point](https://github.com/naomis-archive/fcc-sendgrid-tutorial/blob/main/tutorial-steps/step-2.ts) si vous le souhaitez. 

Lisez la suite pour voir comment gérer les e-mails rejetés et la logique supplémentaire pour les échecs d'envoi, ce que nous discuterons ensuite.

### Comment gérer les e-mails rejetés dans SendGrid

Vous avez peut-être remarqué que `iama@fake.email` n'est pas du tout une adresse e-mail réelle. SendGrid générera des rapports de rejet quotidiens pour votre activité de la veille. 

Chaque e-mail rejeté nuit à votre réputation SendGrid et peut amener les fournisseurs de messagerie à marquer votre courrier comme spam. Nous devons donc ajouter une logique pour éviter d'envoyer des messages à des adresses connues pour être rejetées.

Commencez par créer un fichier `bouncedEmails.csv` dans votre dossier `prod` (il doit être à côté de votre `validEmails.csv`). Nous n'avons pas besoin de valeurs `unsubscribeId` ici, donc initialisez-le avec :

```csv
email
iama@fake.email
```

Retour à notre fichier `send.ts`. À la ligne 38, juste en dessous de notre déclaration de `filePath` existante, configurez le chemin pour le nouveau fichier `bouncedEmails.csv`.

```
// Ici, nous concaténons nos chemins de fichiers pour les fichiers CSV
const filePath = path.join(__dirname + "/validEmails.csv");
const bouncePath = path.join(__dirname + "/bouncedEmails.csv");
```

Super ! Maintenant, nous devons lire ce fichier. Immédiatement en dessous de ces déclarations de chemin de fichier (avant notre appel `readFile` existant), ajoutez la logique pour lire les fichiers rejetés.

```
// Lire la liste des rejets, analyser en tableau
readFile(bouncePath, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  bounceList = data.split("\n").slice(1);

```

`readFile` est asynchrone - nous devons donc envelopper la fonction de rappel autour de _toute notre logique d'envoi existante_. Assurez-vous que votre `})` de fermeture pour ce rappel est déplacé à la toute fin de notre fichier.

Nous lisons le fichier `bouncedEmails.csv`, le divisons à la nouvelle ligne (n'oubliez pas que vous devrez vous assurer que vos fins de ligne sont `LF`), et supprimons la ligne `email`. Enfin, nous continuons avec notre logique d'envoi existante.

Retour à notre logique d'envoi. Dans notre fonction `.forEach`, ajoutez une logique pour ignorer les e-mails bloqués (nous ajouterons cela avant de construire l'objet message pour éviter de créer des variables inutiles).

```ts
  // Ici, nous itérons à travers le tableau emailList
  emailList.forEach((user) => {
    // Ici, nous vérifions si l'e-mail a été rejeté
    if (bounceList.length && bounceList.includes(user.email)) {
        console.info(`Envoi du message ignoré : ${user.email}`);
        return;
    }
    
```

En utilisant une instruction `return` précoce, nous mettons fin à cette itération particulière de `.forEach` lorsque la `bounceList` inclut cet e-mail. Cela nous empêche d'essayer d'envoyer des e-mails à des adresses qui ont déjà été rejetées. Maintenant, si vous exécutez `npm run build` et `npm run start`, vous devriez voir cette sortie dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-99.png)
_Exemple de sortie de la console pour un e-mail ignoré et un e-mail réussi_

[Voir notre progression jusqu'à ce point](https://github.com/naomis-archive/fcc-sendgrid-tutorial/blob/main/tutorial-steps/step-3.ts).

### Comment capturer les e-mails échoués dans SendGrid

Actuellement, notre application enregistrera une erreur si un e-mail échoue à être envoyé. Cela peut fonctionner pour des cas d'utilisation plus petits, mais à mesure que vous développez votre application, vous trouverez de plus en plus difficile d'identifier ces échecs et de tenter de renvoyer. 

Mais au lieu de cela, nous pouvons faire en sorte que notre application sauvegarde ces e-mails dans un nouveau fichier.

Créez un fichier `failedEmails.csv` dans votre dossier `prod`. Ce fichier peut être vide. Nous allons écrire le code pour ajouter la ligne d'en-tête.

Retour à notre fichier `send.ts`, rendez-vous à nos déclarations de chemin à la ligne 38. Ajoutons-en un de plus pour notre nouveau `failedEmails.csv` :

```ts
// Ici, nous concaténons nos chemins de fichiers pour les fichiers CSV
const filePath = path.join(__dirname + "/validEmails.csv");
const bouncePath = path.join(__dirname + "/bouncedEmails.csv");
const failedPath = path.join(__dirname + "/failedEmails.csv");
```

Contrairement à nos autres chemins, ce chemin sera utilisé pour une opération d'`écriture`. Comme nous voulons écrire en continu à mesure que les e-mails sont traités, nous devons créer un flux pour le faire. Juste en dessous de ces déclarations de chemin, créons ce flux et ajoutons notre ligne d'en-tête initiale.

```ts
// Ici, nous créons notre flux d'écriture pour les e-mails échoués
const failedStream = createWriteStream(failedPath);

// Ici, nous ajoutons la ligne d'en-tête
failedStream.write("email,unsubscribeId\n")
```

Il est temps d'améliorer notre logique de gestion des erreurs pour incorporer ce nouveau flux. Nous devons ajouter une autre opération d'`écriture` à notre gestion des erreurs dans l'appel `send`.

```ts
    // Ici, nous envoyons le message que nous venons de construire !
    sgMail
      .send(message)
      .then(() => {
        // Ici, nous enregistrons les demandes d'envoi réussies
        console.info(`Envoi du message réussi : ${user.email}`);
      })
      .catch((err) => {
        // Ici, nous enregistrons les demandes d'envoi en erreur
        console.error(err);
        console.error(`Échec de l'envoi du message : ${user.email}`);
        // Et ici, nous ajoutons cet e-mail à failedEmails.csv
        failedStream.write(`${user.email},${user.unsubscribeId}\n`)
      });
```

Cela écrira l'`email` et `unsubscribeId` dans notre nouveau `failedEmails.csv` dans le format approprié - nous permettant de copier ces données dans le `validEmails.csv` pour faire une autre tentative d'envoi.

Félicitations ! Vous avez maintenant construit un outil réussi et entièrement fonctionnel pour envoyer des e-mails en masse. Vous pouvez [voir le code complet](https://github.com/naomis-archive/fcc-sendgrid-tutorial/blob/main/tutorial-steps/step-4.ts) si vous voulez confirmer votre travail. Mais continuez à lire pour quelques fonctionnalités optionnelles, "agréables à avoir".

## Fonctionnalités optionnelles pour votre outil d'e-mail

Parce que notre outil est basé sur CLI (ce qui signifie qu'il est utilisé dans l'interface de ligne de commande, ou terminal), il n'y a pas beaucoup de retour utilisateur. Nous pouvons utiliser certaines fonctions de console supplémentaires pour fournir plus d'informations sur la progression du script.

Commençons par ajouter quelques "points de contrôle". Avant notre validation des variables d'environnement, imprimons un message indiquant que le script a démarré et vérifie les variables :

```ts
console.info('Script démarré. Validation des variables d'environnement...')
```

Ensuite, après notre validation, nous pouvons imprimer un message de succès.

```ts
// Ici, nous définissons la clé API SendGrid
sgMail.setApiKey(apiKey);

console.info('Variables confirmées !')
```

Dans notre fonction pour lire le fichier des e-mails rejetés, nous pouvons ajouter quelques messages pour le début, l'échec et le succès.

```ts
console.info('Lecture de la liste des e-mails rejetés...')

// Lire la liste des rejets, analyser en tableau
readFile(bouncePath, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    console.error('Échec de la lecture des e-mails rejetés !')
    process.exit(1);
  }
  bounceList = data.split("\n").slice(1);

console.info('E-mails rejetés lus !')
```

Et de même pour notre liste d'e-mails valides :

```ts
console.info('Lecture de la liste d'envoi...')
// C'est ici que nous commençons à lire le fichier !
readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    console.error('Échec de la lecture de la liste d'envoi !')
    return;
  }
```

Maintenant, il serait très agréable d'avoir un message qui s'affiche lorsque l'opération est terminée. Cependant, si nous ajoutons un `console.info` après notre boucle `.forEach`, il s'affichera en réalité _avant_ que les e-mails n'aient fini d'être envoyés !

Cela est dû au fait que la méthode `.send` crée un appel réseau et retourne une Promesse, et cette Promesse peut ne pas avoir été résolue/rejetée avant que notre itération ne soit terminée. 

Nous pouvons donc créer un compteur pour suivre le nombre d'e-mails que nous avons envoyés par rapport au nombre total d'e-mails. Juste avant notre boucle `.forEach`, ajoutez ces variables :

```ts
    // Ici, nous créons des variables pour le comptage
    const emailTotal = emailList.length;
    let emailCount = 0;
```

Nous voulons compter les e-mails rejetés comme traités, même si nous les ignorons.

```ts
  // Ici, nous itérons à travers le tableau emailList
  emailList.forEach((user) => {
    // Ici, nous vérifions si l'e-mail a été rejeté
    if (bounceList.includes(user.email)) {
      console.info(`Envoi du message ignoré : ${user.email}`);
      emailCount++;
      if (emailCount === emailTotal) {
        console.info(
          `Envoi terminé ! ${emailTotal} e-mails envoyés. Bonne journée !`
        );
        return;
      }
    }
```

Enfin, nous devons ajouter une logique pour voir si l'e-mail que nous avons envoyé est le dernier e-mail. Cette logique va dans nos gestionnaires de succès et d'erreurs pour l'appel d'envoi :

```ts
    // Ici, nous envoyons le message que nous venons de construire !
    sgMail
      .send(message)
      .then(() => {
        // Ici, nous enregistrons les demandes d'envoi réussies
        console.info(`Envoi du message réussi : ${user.email}`);
        // Ici, nous gérons le comptage des e-mails
        emailCount++;
        if (emailCount === emailTotal) {
          console.info(
            `Envoi terminé ! ${emailTotal} e-mails envoyés. Bonne journée !`
          );
        }
      })
      .catch((err) => {
        // Ici, nous enregistrons les demandes d'envoi en erreur
        console.error(err);
        console.error(`Échec de l'envoi du message : ${user.email}`);
        // Et ici, nous ajoutons cet e-mail à failedEmails.csv
        failedStream.write(`${user.email},${user.unsubscribeId}\n`);
        // Ici, nous gérons le comptage des e-mails
        emailCount++;
        if (emailCount === emailTotal) {
          console.info(
            `Envoi terminé ! ${emailTotal} e-mails envoyés. Bonne journée !`
          );
        }
      });
```

Et avec cela, notre application est entièrement complète ! Si vous exécutez les scripts `npm run build` et `npm run send`, vous devriez voir cette sortie dans votre terminal :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-100.png)
_Exemple de sortie de la console pour l'application terminée._

Et vous devriez avoir reçu quelques e-mails qui ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-101.png)
_Image d'exemple du résultat de l'e-mail de test_

Vous pouvez [voir notre code final ici](https://github.com/nhcarrigan/fcc-sendgrid-tutorial/blob/main/tutorial-steps/step-5.ts), ou vous pouvez [voir la version étendue](https://github.com/freecodecamp/sendgrid-email-blast) construite pour freeCodeCamp.