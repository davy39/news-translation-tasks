---
title: Comment valider les Pull Requests dans AWS et faciliter les revues de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-23T15:59:03.000Z'
originalURL: https://freecodecamp.org/news/validate-pull-requests-in-aws
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9893740569d1a4ca1ad3.jpg
tags:
- name: AWS
  slug: aws
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
seo_title: Comment valider les Pull Requests dans AWS et faciliter les revues de code
seo_desc: "By Aagam Vadecha\nWhen a project grows, and developers are pushing code\
  \ frequently, there is always a chance that working pull requests might break somewhere.\
  \ \nIt could be because one PR was merged before another, or the destination branch\
  \ moved a few..."
---

Par Aagam Vadecha

Lorsque qu'un projet grandit et que les développeurs poussent du code fréquemment, il y a toujours un risque que les pull requests en cours de travail puissent échouer quelque part. 

Cela pourrait être dû au fait qu'une PR a été fusionnée avant une autre, ou que la branche de destination a avancé de quelques commits, provoquant des conflits. 

Ou peut-être parce qu'un développeur n'a pas exécuté les tests avant de pousser et a involontairement introduit un bug dans une autre partie du produit. Et la liste continue.

Mais cela ne devrait pas être un problème. Chaque organisation a un workflow pour les revues de code, n'est-ce pas ? Mais cela prend encore beaucoup de temps. Surtout pour ces PR qui échouent et ne sont même pas prêtes pour la revue. 

Nous pouvons construire et tester manuellement notre code chaque fois avant une revue de code appropriée, sans aucun doute. Mais après un certain point, il semble préférable de l'automatiser. 

Imaginez une organisation de taille moyenne avec 100 à 150 PR chaque semaine. Le temps passé à valider répétitivement celles-ci pourrait donner à cette entreprise un ensemble complet de nouvelles fonctionnalités. Eh bien alors, allons chercher ces fonctionnalités !

## Prérequis

Vous devriez avoir une certaine familiarité avec les services AWS. 

Je suppose que vous savez comment créer et gérer des fonctions Lambda, des projets CodeBuild, des événements CloudWatch, des rôles IAM, et que vous utilisez CodeCommit pour versionner votre base de code.

## Architecture

Comprenons, à un niveau élevé, comment nous allons aborder ce projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/ValidatePR-Architecture-Flowchart.png)
_Uh huh, Qu'est-ce que c'est ?_

Étape par étape, comprenons mieux notre workflow.

1. Disons qu'une nouvelle PR est créée / une PR existante est mise à jour.
2. Un événement CloudWatch qui surveille notre dépôt sera activé et enverra les données pertinentes à une fonction lambda.
3. Cette fonction fera deux choses  
  Trigger CodeBuild Project pour construire notre dernier commit et exécuter les tests.   
  Commenter tout message personnalisé que nous voulons sur notre PR.
4. Après que CodeBuild ait fini d'exécuter la construction, un autre événement CloudWatch enverra ces résultats de construction à une fonction lambda.
5. Cette fonction commentera les résultats de la construction sur notre PR.

Très bien alors, commençons !

## Configuration de notre application

Pour simplifier, j'ai créé une application Node.js simple. Elle est écrite en TypeScript et toute la phase de construction consiste à compiler 'app.ts' en 'app.js'.

[Voici](https://github.com/aagam29/ValidatePR) le lien vers le dépôt - clonez-le et utilisez-le si vous voulez suivre.   
Tout le code pertinent utilisé dans cet article peut être trouvé là.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/simple-express-app-screenshots.jpg)
_Une application Express simple_

La commande `build` ici est un simple `tsc app.ts`, mais vous pouvez la changer pour la commande de construction de votre projet.

Aussi pour garder cela simple, je n'ai pas inclus de cas de test. Vous pouvez les lier à `test` dans la section script de `package.json` et suivre.

## Projet CodeBuild

Tout d'abord, vous voudrez configurer un projet CodeBuild de base pour votre dépôt. 

**Pour ce faire, procédez comme suit :**

* Configurez la source comme votre dépôt CodeCommit
* Le type de référence doit être une branche
* L'environnement doit être conforme aux exigences du projet
* Vous devez utiliser un fichier buildspec
* Le reste doit être les valeurs par défaut.

Assurez-vous d'avoir un fichier `buildspec.yml` dans le dossier racine de votre dépôt.

Note : cela peut différer si vous travaillez avec un MonoRepo. Dans ce cas, vous pourriez avoir des fichiers buildspec.yml séparés pour chaque application et devrez transmettre sélectivement le chemin du fichier buildspec comme variable d'environnement en fonction des fichiers modifiés dans le commit. 

Nous avons une configuration similaire dans notre organisation, et nous adorons les résultats pour l'instant !

```yml
version: 0.2
phases:
  install:
    commands:
     - n 12.12
     - curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
     - echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
     - apt update
     - apt install yarn
     - yarn install
#   pre_build:
#     commands:
#     - yarn test
  build:
    commands:
     - yarn build
```

Que fait ce buildspec.yml ? Eh bien, il transmet des commandes d'exécution pour chaque construction à notre projet CodeBuild.

Et puis, que fait-il ? ?

* Installe node 12.12.0
* Installe yarn
* Installe les dépendances de notre projet.
* yarn test (Il exécute nos cas de test. Il n'y en a aucun ici, mais vous pouvez décommenter cette section si vous en avez besoin.)
* yarn build (Construire notre projet.)

## Fonctions Lambda

Configurons deux fonctions comme discuté dans la section architecture ci-dessus.

La fonction **TriggerCodebuildStart** recevra un événement CloudWatch (que nous configurerons dans un instant) et déclenchera notre projet CodeBuild pour démarrer une nouvelle construction.

Elle publiera également un commentaire "Build Started" avec l'horodatage et un lien vers les logs de construction dans la section des commentaires de notre PR.

La fonction **TriggerCodebuildResult** recevra un événement CloudWatch de notre projet CodeBuild qui contiendra les résultats de la construction. 

Elle publiera également le commentaire "Codebuild Results" avec l'horodatage et un lien vers les logs de construction dans la section des commentaires de notre PR.

Voici le code. C'est ce que vous attendiez, n'est-ce pas ! ? 

```js
const AWS = require('aws-sdk');
const codecommit = new AWS.CodeCommit();
const codebuild = new AWS.CodeBuild();

exports.handler = async (event) => {
    try {
        console.log('Received Event: ', event);
        const { destinationCommit } = event.detail;
        const { sourceCommit } = event.detail;
        const { pullRequestId } = event.detail;
        const pullRequestName = event.detail.title;
        const sourceBranch = event.detail.sourceReference.split('/').pop();
        const triggerCodeBuildParameters = {
            sourceBranch, sourceCommit, destinationCommit, pullRequestId, pullRequestName
        };
        const codeBuildResult = await triggerCodebuild(triggerCodeBuildParameters);
        
        const buildId = codeBuildResult.build.id;
        const postBuildStartedCommentOnPRParameters = {
            sourceCommit, destinationCommit, pullRequestId, buildId
        }
        
        await postBuildStartedCommentOnPR(postBuildStartedCommentOnPRParameters);
        
        return {
            statusCode: 200
        };
    }
    catch (error) {
        console.log('An Error Occured', error);
        return { 
            error
        };
    }
};

async function postBuildStartedCommentOnPR(postBuildStartedCommentOnPRParameters) {
    const { sourceCommit, destinationCommit, pullRequestId, buildId } = postBuildStartedCommentOnPRParameters;
    const logLink = `https://${process.env.REGION}.console.aws.amazon.com/codesuite/codebuild/projects/ValidatePullRequest/build/${buildId}`;
    const parameters = {
        afterCommitId: sourceCommit,
        beforeCommitId: destinationCommit,
        content: `Build For Validating The Pull Request has been started.   
        Timestamp: **${Date.now()}**   
        Check [CodeBuild Logs](${logLink})`,
        pullRequestId,
        repositoryName: process.env.REPOSITORY_NAME
    };

    const request = await codecommit.postCommentForPullRequest(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Commenting To Pull Request', error);
            throw new Error(error);
        }
    );
}

async function triggerCodebuild(triggerCodeBuildParameters) {
    const { sourceBranch, sourceCommit, destinationCommit, pullRequestId, pullRequestName } = triggerCodeBuildParameters;
    console.log(`Triggering Codebuild, Branch: ${sourceBranch}`);
    const parameters = {
        projectName: process.env.CODEBUILD_PROJECT,
        sourceVersion: `refs/heads/${sourceBranch}^{${sourceCommit}}`,
        environmentVariablesOverride: [
            {
                name: 'pullRequestId',
                value: pullRequestId,
                type: 'PLAINTEXT'
            },
            {
                name: 'sourceCommit',
                value: sourceCommit,
                type: 'PLAINTEXT'
            },
            {
                name: 'destinationCommit',
                value: destinationCommit,
                type: 'PLAINTEXT'
            },
            {
                name: 'pullRequestName',
                value: pullRequestName,
                type: 'PLAINTEXT'
            }
        ]
    };
    const request = await codebuild.startBuild(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Starting Codebuild', error);
            throw new Error(error);
        }
    );
}
```

```js
const AWS = require('aws-sdk');
const codecommit = new AWS.CodeCommit();
exports.handler = async (event) => {
    try {
        console.log('Event', event);
        const parameters = await getParameters(event);
        console.log('Parameters For Comment:', parameters);
        await commentCodeBuildResultOnPR(parameters);
        return { statusCode: 200 };
    }
    catch (error) {
        console.log('An Error Occured', error);
        return { error };
    }
};

async function getParameters(event) {
    try {
        const buildId = event.detail['build-id'].split('/')[1];
        const buildStatus = event.detail['build-status'];
        const environmentVariableList = event.detail['additional-information'].environment['environment-variables'];
        let afterCommitId, beforeCommitId, content, pullRequestId;
        for (element of environmentVariableList) {
            if (element.name === 'pullRequestId') pullRequestId = element.value;
            if (element.name === 'sourceCommit') afterCommitId = element.value;
            if (element.name === 'destinationCommit') beforeCommitId = element.value;
            if (element.name === 'pullRequestName') pullRequestName = element.value;
        }

        const logLink = `https://${process.env.REGION}.console.aws.amazon.com/codesuite/codebuild/projects/ValidatePullRequest/build/${buildId}`;
        content = `Build Result: **${buildStatus}**   
        Timestamp: **${Date.now()}**   
        Check [CodeBuild Logs](${logLink})`;

        return {
            afterCommitId,
            beforeCommitId,
            content,
            pullRequestId,
            repositoryName: process.env.REPOSITORY_NAME
        };
    } catch (error) {
        throw error;
    }
}

async function commentCodeBuildResultOnPR(parameters) {
    const request = await codecommit.postCommentForPullRequest(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Commenting To Pull Request', error);
            throw new Error(error);
        }
    );
}
```

Vous devrez remplir les variables d'environnement appropriées avant d'utiliser ces fonctions. Lisez le code une fois et vous saurez quoi faire.

Au cas où vous auriez besoin de vous référer à la documentation, allez simplement [ici](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CodeBuild.html#startBuild-property) et [là](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CodeCommit.html#postCommentForPullRequest-property). ? 

## Configurer les événements CloudWatch

D'accord, maintenant pour tout relier, configurons nos événements CloudWatch.

Nous créerons deux événements : l'un recevra les nouvelles données de commit de notre dépôt, et l'autre recevra les résultats de CodeBuild. Les cibles de ces événements seront nos fonctions lambda.  
  
J'inclus ici des captures d'écran en pleine page. Cela vous aidera à comprendre les références.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/CloudWatch-Events.png)
_Concentrez-vous sur les verts._

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Start--CloudWatch-Event-1.png)
_Remplacez par l'ARN de votre projet CodeBuild._

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Result---Cloudwatch-Event.png)
_Presque là !_

J'ai choisi de déclencher la fonction lambda sur les événements FAILED et SUCCEEDED. Mais vous pouvez également sélectionner All Events et l'adapter à vos besoins.

## Et, Action !

D'accord, vous êtes super cool si vous êtes arrivé à ce point. ? Après tant de travail, voyons ce que nous avons accompli. 

Faisons deux pull requests, une qui fonctionne bien et une autre qui contient une erreur de construction intentionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/New-Working-PR.png)
_PR sans erreur_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Successfull-build.png)
_Génial !_

Maintenant, créons une PR avec des bugs. Voyez ici, au lieu de **app.get**, il y a **ap.get**. C'est intentionnel et stupide. Mais cela fera l'affaire pour l'instant.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Faulty-PR.png)
_PR défectueuse_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Failed-build.png)
_Message de construction échouée, revues heureuses. N'ont pas eu à vérifier la branche et à tester !_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Failed-Logs.png)
_Développeurs, comme d'habitude, nous avons des logs pour vous !_

## Conclusion

Pour aller plus loin, vous pourriez déclencher un appel API à votre URL de webhook Slack pour notifier immédiatement dans un canal en cas d'échec de construction. Génial, n'est-ce pas ?

De plus, il s'agit d'une configuration très simple et les projets du monde réel pourraient être plus complexes.   
Par exemple, les MonoRepos pourraient avoir plusieurs applications et constructions, et les tests pour chacune de ces applications sont différents. 

Déclencher tous ces tests à chaque fois serait inutile, plus coûteux et créerait de la confusion. Vous devrez peut-être déclencher sélectivement ces constructions en fonction des fichiers commis et des applications affectées.

Cependant, cet article devrait vous fournir une base décente. Et vous pouvez définitivement l'étendre. Après tout, vous êtes aussi génial. :)

**Merci d'avoir lu !** Si vous avez besoin d'aide à ce sujet, n'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/aagamvadecha/). J'ai hâte de vous aider comme je le peux.