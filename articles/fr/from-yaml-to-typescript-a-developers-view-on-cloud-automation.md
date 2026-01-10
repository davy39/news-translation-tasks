---
title: 'Du YAML à TypeScript : le point de vue d''un développeur sur l''automatisation
  du cloud'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T21:44:23.000Z'
originalURL: https://freecodecamp.org/news/from-yaml-to-typescript-a-developers-view-on-cloud-automation
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CRXQDOXGvKBpB-N6Fv74lw.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: 'Du YAML à TypeScript : le point de vue d''un développeur sur l''automatisation
  du cloud'
seo_desc: 'By Mikhail Shilkov

  The rise of managed cloud services, cloud-native, and serverless applications brings
  both new possibilities and challenges. More and more practices from software development
  processes like version control, code review, continuous i...'
---

Par Mikhail Shilkov

L'essor des services cloud gérés, des applications natives du cloud (cloud-native) et du serverless apporte à la fois de nouvelles possibilités et de nouveaux défis. De plus en plus de pratiques issues des processus de développement logiciel, telles que le contrôle de version, la revue de code, l'intégration continue et les tests automatisés, sont appliquées à l'automatisation de l'infrastructure cloud.

La plupart des outils existants suggèrent de définir l'infrastructure dans des formats de balisage textuels, le YAML étant le favori. Dans cet article, je plaide pour l'utilisation de véritables langages de programmation comme TypeScript à la place. Un tel changement rend encore plus de pratiques de développement logiciel applicables au domaine de l'infrastructure.

### Exemple d'application

Il est plus facile de plaider une cause à l'aide d'un exemple spécifique. Pour cet article, nous allons construire une application de raccourcissement d'URL, un clone basique de tinyurl.com ou bit.ly. Il existe une page d'administration où nous pouvons définir des alias courts pour des URL longues :

![Image](https://cdn-media-1.freecodecamp.org/images/0*vUDdeSIDFoGp2UDE.png)
_Exemple d'application de raccourcissement d'URL_

Désormais, chaque fois qu'un visiteur se rend sur l'URL de base de l'application + un alias existant, il est redirigé vers l'URL complète.

Cette application est simple à décrire mais implique suffisamment de pièces mobiles pour être représentative de certains problèmes du monde réel. En prime, il existe de nombreuses implémentations existantes sur le web avec lesquelles comparer.

### Raccourcisseur d'URL Serverless

Je suis un grand partisan de l'architecture serverless : ce style d'applications cloud combinant des fonctions sans serveur et des services cloud gérés. Elles sont rapides à développer, faciles à exploiter et ne coûtent que quelques centimes, à moins que l'application ne reçoive énormément d'utilisateurs. Cependant, même les applications serverless doivent gérer l'infrastructure, comme les bases de données, les files d'attente et d'autres sources d'événements et destinations de données.

Mes exemples utiliseront AWS d'Amazon, mais cela pourrait tout aussi bien être Microsoft Azure ou Google Cloud Platform.

L'idée est donc de stocker les URL avec des noms courts sous forme de paires clé-valeur dans Amazon DynamoDB et d'utiliser des AWS Lambdas pour exécuter le code de l'application. Voici le schéma initial :

![Image](https://cdn-media-1.freecodecamp.org/images/0*IHX7dL1m1H8uvcF4.png)
_Raccourcisseur d'URL avec AWS Lambda et DynamoDB_

La Lambda en haut reçoit un événement lorsque quelqu'un décide d'ajouter une nouvelle URL. Elle extrait le nom et l'URL de la requête et les enregistre en tant qu'élément dans la table DynamoDB.

La Lambda en bas est appelée chaque fois qu'un utilisateur navigue vers une URL courte. Le code lit l'URL complète en fonction du chemin demandé et renvoie une réponse 301 avec l'emplacement correspondant.

Voici l'implémentation de la Lambda `Open URL` en JavaScript :

```ts
const aws = require('aws-sdk');
const table = new aws.DynamoDB.DocumentClient(); 
exports.handler = async (event) => { 
  const name = event.path.substring(1); 
  const params = { TableName: "urls", Key: { "name": name } }; 
  const value = await table.get(params).promise(); 
  const url = value && value.Item && value.Item.url; 
  return url 
    ? { statusCode: 301, body: "", headers: { "Location": url } } 
    : { statusCode: 404, body: name + " not found" }; 
};
```

Cela représente 11 lignes de code. Je passerai sur l'implémentation de la fonction `Add URL` car elle est très similaire. En considérant une troisième fonction pour lister les URL existantes pour l'interface utilisateur, nous pourrions aboutir à 30-40 lignes de JavaScript au total.

Alors, comment déployons-nous l'application ?

Eh bien, avant de faire cela, nous devrions réaliser que l'image ci-dessus était une simplification excessive :

* AWS Lambda ne peut pas gérer directement les requêtes HTTP, nous devons donc ajouter AWS API Gateway devant.
* Nous devons également servir des fichiers statiques pour l'interface utilisateur, que nous placerons dans AWS S3 et proxifierons avec la même API Gateway.

Voici le diagramme mis à jour :

![Image](https://cdn-media-1.freecodecamp.org/images/0*2ezVdcpK_Wt9HdhM.png)
_API Gateway, Lambda, DynamoDB et S3_

C'est une conception viable, mais les détails sont encore plus complexes :

* API Gateway est une bête complexe qui nécessite des étapes (Stages), des déploiements et des points de terminaison REST configurés de manière appropriée.
* Les permissions et les politiques (Policies) doivent être définies pour qu'API Gateway puisse appeler Lambda et que Lambda puisse accéder à DynamoDB.
* Les fichiers statiques doivent aller dans des objets de compartiment (Bucket) S3.

Ainsi, la configuration réelle implique une vingtaine d'objets à configurer dans AWS :

![Image](https://cdn-media-1.freecodecamp.org/images/0*8vOMSf1GN9eHgrKw.png)
_Toutes les ressources cloud à provisionner_

Comment abordons-nous cette tâche ?

### Options pour provisionner l'infrastructure

Il existe de nombreuses options pour provisionner une application cloud, et chacune a ses compromis. Passons rapidement en revue la liste des possibilités pour comprendre le paysage.

#### Console Web AWS

AWS, comme tout autre cloud, dispose d'une [interface utilisateur web](https://console.aws.amazon.com/) pour configurer ses ressources :

![Image](https://cdn-media-1.freecodecamp.org/images/0*RzAUosMerv055fWr.png)
_Console Web AWS_

C'est un bon point de départ — idéal pour expérimenter, découvrir les options disponibles, suivre les tutoriels, c'est-à-dire pour l'exploration.

Cependant, cela ne convient pas particulièrement bien aux applications à longue durée de vie et en constante évolution développées en équipe. Un déploiement effectué manuellement par clics est assez difficile à reproduire de manière exacte, ce qui devient très vite un problème de maintenabilité.

#### Interface de ligne de commande AWS (CLI)

L'[interface de ligne de commande AWS](https://aws.amazon.com/cli/) (CLI) est un outil unifié pour gérer tous les services AWS à partir d'une invite de commande. Vous écrivez les appels comme ceci :

```
aws apigateway create-rest-api --name 'My First API' --description 'This is my first API' 

aws apigateway create-stage --rest-api-id 1234123412 --stage-name 'dev' --description 'Development stage' --deployment-id a1b2c3
```

L'expérience initiale n'est peut-être pas aussi fluide que de cliquer sur des boutons dans le navigateur, mais l'énorme avantage est que vous pouvez _réutiliser_ des commandes que vous avez écrites une fois. Vous pouvez créer des scripts en combinant de nombreuses commandes dans des scénarios cohérents. Ainsi, votre collègue peut bénéficier du même script que vous avez créé. Vous pouvez provisionner plusieurs environnements en paramétrant les scripts.

Franchement, je ne l'ai jamais fait pour plusieurs raisons :

* Les scripts CLI me semblent trop impératifs. Je dois décrire « comment » faire les choses, et non « ce que » je veux obtenir à la fin.
* Il ne semble pas y avoir de bonne solution pour mettre à jour les ressources existantes. Dois-je écrire de petits scripts delta pour chaque modification ? Dois-je les conserver éternellement et exécuter toute la suite chaque fois que j'ai besoin d'un nouvel environnement ?
* Si une défaillance survient à mi-chemin du script, je dois réparer manuellement tout pour revenir à un état cohérent. Cela devient vite désordonné, et je n'ai aucune envie de pratiquer ce processus, surtout en production.

Pour surmonter ces limitations, la notion de **Configuration de l'état souhaité** (Desired State Configuration - DSC) a été inventée. Sous ce paradigme, nous décrivons la disposition souhaitée de l'infrastructure, puis l'outillage se charge soit de la provisionner de zéro, soit d'appliquer les modifications requises à un environnement existant.

Quel outil fournit un modèle DSC pour AWS ? Ils sont légion.

#### AWS CloudFormation

[AWS CloudFormation](https://aws.amazon.com/cloudformation/) est l'outil de premier niveau pour la gestion de la configuration de l'état souhaité d'Amazon. Les modèles CloudFormation utilisent YAML pour décrire toutes les ressources d'infrastructure d'AWS.

Voici un extrait d'un [exemple de raccourcisseur d'URL privé](https://aws.amazon.com/blogs/compute/build-a-serverless-private-url-shortener/) aimablement fourni sur le blog AWS :

```
Resources:
  S3BucketForURLs:
  Type: "AWS::S3::Bucket"
  DeletionPolicy: Delete
  Properties:
    BucketName: !If ["CreateNewBucket", !Ref "AWS::NoValue", !Ref S3BucketName ]
    WebsiteConfiguration:
      IndexDocument: "index.html"
    LifecycleConfiguration:
      Rules:
        -
          Id: DisposeShortUrls
          ExpirationInDays: !Ref URLExpiration
          Prefix: "u"
         Status: Enabled
```

Ceci n'est qu'un très court fragment : l'exemple complet se compose de 317 lignes de YAML. C'est un ordre de grandeur de plus que le code JavaScript réel que nous avons dans l'application !

CloudFormation est un outil puissant, mais il demande un certain apprentissage pour être maîtrisé. De plus, il est spécifique à AWS : vous ne pourrez pas transférer cette compétence à d'autres fournisseurs de cloud.

Ne serait-ce pas formidable s'il existait un format DSC universel ? Voici Terraform.

#### Terraform

[HashiCorp Terraform](https://www.terraform.io/) est un outil open source permettant de définir l'infrastructure dans des fichiers de configuration déclaratifs. Il possède une architecture enfichable, de sorte que l'outil prend en charge tous les principaux clouds et même les scénarios hybrides.

Le format textuel personnalisé Terraform `.tf` est utilisé pour définir les configurations. Le langage de template est assez puissant et, une fois appris, vous pouvez l'utiliser pour différents fournisseurs de cloud.

Voici un extrait de l'exemple [AWS Lambda Short URL Generator](https://github.com/jamesridgway/aws-lambda-short-url) :

```
resource "aws_api_gateway_rest_api" "short_urls_api_gateway" {
  name        = "Short URLs API"
  description = "API for managing short URLs."
}
resource "aws_api_gateway_usage_plan" "short_urls_api_usage_plan" {
  name         = "Short URLs admin API key usage plan"
  description  = "Usage plan for the admin API key for Short URLS."
  api_stages {
    api_id = "${aws_api_rest_api.short_urls_gateway.id}"
    stage  = "${aws_api_deployment.short_url_deployment.stage_name}"
  }
}
```

Cette fois, l'exemple complet fait environ 450 lignes de templates textuels. Existe-t-il des moyens de réduire la taille de la définition de l'infrastructure ?

Oui, en élevant le niveau d'abstraction. C'est possible avec les modules de Terraform, ou en utilisant d'autres outils plus spécialisés.

#### Serverless Framework et SAM

[Le Serverless Framework](https://serverless.com/) est un outil de gestion d'infrastructure axé sur les applications serverless. Il fonctionne sur plusieurs fournisseurs de cloud (bien que le support AWS soit le plus solide) et n'expose que les fonctionnalités liées à la création d'applications avec des fonctions cloud.

L'avantage est qu'il est beaucoup plus concis. Une fois de plus, l'outil utilise YAML pour définir les modèles, voici un extrait de l'exemple [Serverless URL Shortener](https://github.com/danielireson/serverless-url-shortener) :

```
functions:
  store:
    handler: api/store.handle
    events:
      - http:
          path: /
          method: post
          cors: true
```

Le langage spécifique au domaine permet une définition plus courte : cet exemple comporte 45 lignes de YAML + 123 lignes de fonctions JavaScript.

Cependant, la concision a un revers : dès que vous vous écartez du chemin doré assez « mince » — les fonctions cloud et une liste incomplète de sources d'événements — vous devez vous rabattre sur des outils plus génériques comme CloudFormation. Dès que votre paysage inclut des travaux d'infrastructure de plus bas niveau ou des composants basés sur des conteneurs, vous vous retrouvez à nouveau à utiliser plusieurs langages et outils de configuration.

L'[AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/index.html) (SAM) d'Amazon ressemble beaucoup au Serverless Framework mais est conçu pour être spécifique à AWS.

Est-ce la fin de l'histoire ? Je ne le pense pas.

### Propriétés souhaitées d'un outil de définition d'infrastructure

Qu'avons-nous appris en parcourant le paysage actuel ? Les outils d'infrastructure parfaits devraient :

* Fournir des résultats de déploiement **reproductibles**
* Être **scriptables**, c'est-à-dire ne nécessiter aucune intervention humaine une fois la définition terminée
* Définir l'**état souhaité** plutôt que les étapes exactes pour y parvenir
* Prendre en charge **plusieurs fournisseurs de cloud** et les scénarios hybrides
* Être **universels** au sens où l'on utilise le même outil pour définir n'importe quel type de ressource
* Être **succincts** et **concis** pour rester lisibles et gérables
* ~~Utiliser un format basé sur YAML~~

Non, j'ai barré le dernier point. Le YAML semble être le langage le plus populaire parmi cette classe d'outils (et je n'ai même pas encore abordé Kubernetes !), mais je ne suis pas convaincu qu'il fonctionne bien pour moi. [Le YAML a de nombreux défauts, et je ne veux tout simplement pas l'utiliser](https://noyaml.com/).

Avez-vous remarqué que je n'ai pas mentionné une seule fois l'**Infrastructure as Code** (IaC) jusqu'à présent ? Eh bien, nous y voilà (selon [Wikipedia](https://en.wikipedia.org/wiki/Infrastructure_as_code)) :

> _L'infrastructure en tant que code (IaC) est le processus de gestion et de provisionnement des centres de données informatiques par le biais de fichiers de définition lisibles par machine, plutôt que par une configuration matérielle physique ou des outils de configuration interactifs._

Ne devrait-on pas l'appeler « Infrastructure en tant que fichiers de définition » ou « Infrastructure en tant que YAML » ?

En tant que développeur logiciel, ce que je veux vraiment, c'est « l'infrastructure en tant que véritable code, vous savez, le truc de programmation ». Je veux utiliser **le même langage** que je connais déjà. Je veux rester dans le même éditeur. Je veux bénéficier de l'**auto-complétion** IntelliSense quand je tape. Je veux voir les **erreurs de compilation** quand ce que j'ai tapé n'est pas syntaxiquement correct. Je veux réutiliser les **compétences de développeur** que j'ai déjà. Je veux concevoir des **abstractions** pour généraliser mon code et créer des **composants réutilisables**. Je veux **tirer parti de la communauté open-source** qui créerait de bien meilleurs composants que je ne pourrais jamais le faire. Je veux **combiner le code et l'infrastructure** dans un seul projet de code.

Si vous êtes d'accord avec moi sur ce point, continuez à lire. Vous obtenez tout cela avec Pulumi.

### Pulumi

[Pulumi](https://pulumi.io/) est un outil permettant de créer des logiciels basés sur le cloud en utilisant de véritables langages de programmation. Ils prennent en charge tous les principaux fournisseurs de cloud, ainsi que Kubernetes.

Le modèle de programmation de Pulumi prend également en charge Go et Python, mais je vais utiliser TypeScript pour le reste de l'article.

Tout en prototypant un raccourcisseur d'URL, j'explique le mode de fonctionnement fondamental et j'illustre les avantages et certains compromis. Si vous voulez suivre, [installez Pulumi](https://pulumi.io/quickstart/install.html).

### Comment fonctionne Pulumi

Commençons à définir notre application de raccourcissement d'URL en TypeScript. J'ai installé les modules NPM `@pulumi/pulumi` et `@pulumi/aws` pour pouvoir démarrer le programme. La première ressource à créer est une table DynamoDB :

```ts
import * as aws from "@pulumi/aws";

// Une table DynamoDB avec une seule clé primaire
let counterTable = new aws.dynamodb.Table("urls", {
    name: "urls",
    attributes: [
        { name: "name", type: "S" },
    ],
    hashKey: "name",
    readCapacity: 1,
    writeCapacity: 1
});
```

J'utilise la CLI `pulumi` pour exécuter ce programme afin de provisionner la ressource réelle dans AWS :

```
> pulumi up 
Previewing update (urlshortener): 
   Type                  Name           Plan 
+  pulumi:pulumi:Stack   urlshortener   create 
+    aws:dynamodb:Table  urls           create 
Resources: 
    + 2 to create 
Do you want to perform this update? yes 
Updating (urlshortener): 
   Type                  Name           Status 
+  pulumi:pulumi:Stack   urlshortener   created 
+    aws:dynamodb:Table  urls           created 
Resources: 
    + 2 created
```

La CLI affiche d'abord l'aperçu des modifications à apporter, et lorsque je confirme, elle crée la ressource. Elle crée également une **pile** (stack) — un conteneur pour toutes les ressources de l'application.

Ce code peut ressembler à une commande impérative pour créer une table DynamoDB, mais ce n'est pas le cas. Si je modifie `readCapacity` à `2` puis que je relance `pulumi up`, cela produit un résultat différent :

```
> pulumi up
Previewing update (urlshortener):
   Type                  Name           Plan
   pulumi:pulumi:Stack   urlshortener 
~    aws:dynamodb:Table  urls           update [diff: ~readCapacity]
Resources: 
    ~ 1 to update 1 unchanged
```

Il détecte le changement exact que j'ai effectué et suggère une mise à jour. L'image suivante illustre le fonctionnement de Pulumi :

![Image](https://cdn-media-1.freecodecamp.org/images/0*viskl_7ZYjUekaYZ.png)
_Comment fonctionne Pulumi_

`index.ts` dans le carré rouge est mon programme. L'hôte de langage de Pulumi comprend TypeScript et traduit le code en commandes pour le moteur interne. En conséquence, le moteur construit un arbre des ressources à provisionner, l'état souhaité de l'infrastructure.

L'état final du dernier déploiement est conservé dans le stockage (peut être dans le backend pulumi.com ou un fichier sur disque). Le moteur compare ensuite l'état actuel du système avec l'état souhaité du programme et calcule le delta en termes de commandes de création-mise à jour-suppression vers le fournisseur de cloud.

### L'aide des types

Je peux maintenant passer au code qui définit une fonction Lambda :

```ts
// Créer un rôle donnant accès à notre Lambda.
let policy: aws.iam.PolicyDocument = { /* Masqué pour plus de brièveté */ };
let role = new aws.iam.Role("lambda-role", {
    assumeRolePolicy: JSON.stringify(policy),
});
let fullAccess = new aws.iam.RolePolicyAttachment("lambda-access", {
    role: role,
    policyArn: aws.iam.AWSLambdaFullAccess,
});

// Créer une fonction Lambda, en utilisant le code du dossier `./app`.
let lambda = new aws.lambda.Function("lambda-get", {
    runtime: aws.lambda.NodeJS8d10Runtime,
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive("./app"),
    }),
    timeout: 300,
    handler: "read.handler",
    role: role.arn,
    environment: { 
        variables: {
            "COUNTER_TABLE": counterTable.name
        }
    },
}, { dependsOn: [fullAccess] });
```

Vous pouvez voir que la complexité s'est installée et que la taille du code augmente. Cependant, je commence maintenant à tirer de réels avantages de l'utilisation d'un langage de programmation typé :

* J'utilise des objets dans les définitions des paramètres d'autres objets. Si je fais une faute d'orthographe dans leur nom, je n'obtiens pas une erreur à l'exécution mais un message d'erreur immédiat de l'éditeur.
* Si je ne sais pas quelles options je dois fournir, je peux aller à la définition du type et la consulter (ou utiliser IntelliSense).
* Si j'oublie de spécifier une option obligatoire, j'obtiens une erreur claire.
* Si le type du paramètre d'entrée ne correspond pas au type de l'objet que je passe, j'obtiens à nouveau une erreur.
* Je peux utiliser des fonctionnalités du langage comme `JSON.stringify` directement dans mon programme. En fait, je peux référencer et utiliser n'importe quel module NPM.

Vous pouvez voir le code pour API Gateway [ici](https://github.com/mikhailshilkov/fosdem2019/blob/master/samples/1-raw/index.ts#L60-L118). Il semble trop verbeux, n'est-ce pas ? De plus, je n'en suis qu'à la moitié avec une seule fonction Lambda définie.

### Composants réutilisables

Nous pouvons faire mieux que cela. Voici la définition améliorée de la même fonction Lambda :

```ts
import { Lambda } from "./lambda";

const func = new Lambda("lambda-get", {
    path: "./app",
    file: "read",
    environment: { 
       "COUNTER_TABLE": counterTable.name
    },
});
```

N'est-ce pas magnifique ? Seules les options essentielles subsistent, tandis que toute la machinerie a disparu. Enfin, elle n'a pas complètement disparu, elle a été cachée derrière une _abstraction_.

J'ai défini un **composant personnalisé** appelé `Lambda` :

```ts
export interface LambdaOptions {
    readonly path: string;
    readonly file: string;
    
    readonly environment?:  pulumi.Input<{
        [key: string]: pulumi.Input<string>;
    }>;    
}

export class Lambda extends pulumi.ComponentResource {
    public readonly lambda: aws.lambda.Function;

    constructor(name: string,
        options: LambdaOptions,
        opts?: pulumi.ResourceOptions) {
        
        super("my:Lambda", name, opts);

        const role = //... Rôle tel que défini dans l'extrait précédent
        const fullAccess = //... RolePolicyAttachment tel que défini dans l'extrait précédent
        
        this.lambda = new aws.lambda.Function(`${name}-func`, {
            runtime: aws.lambda.NodeJS8d10Runtime,
            code: new pulumi.asset.AssetArchive({
                ".": new pulumi.asset.FileArchive(options.path),
            }),
            timeout: 300,
            handler: `${options.file}.handler`,
            role: role.arn,
            environment: {
                variables: options.environment
            }
        }, { dependsOn: [fullAccess], parent: this });
    }
}
```

L'interface `LambdaOptions` définit les options qui sont importantes pour mon abstraction. La classe `Lambda` dérive de `pulumi.ComponentResource` et crée toutes les ressources enfants dans son constructeur.

Un effet sympathique est que l'on peut voir la structure dans l'aperçu `pulumi` :

```
> pulumi up
Previewing update (urlshortener):
   Type                              Name               Plan 
+  pulumi:pulumi:Stack               urlshortener       create 
+    my:Lambda                       lambda-get         create 
+      aws:iam:Role                  lambda-get-role    create
+      aws:iam:RolePolicyAttachment  lambda-get-access  create 
+      aws:lambda:Function           lambda-get-func    create 
+    aws:dynamodb:Table              urls               create
```

Le composant `Endpoint` simplifie la définition d'API Gateway (voir [la source](https://github.com/mikhailshilkov/fosdem2019/blob/master/samples/2-components/endpoint.ts)) :

```ts
const api = new Endpoint("urlapi", {
    path: "/{proxy+}",
    lambda: func.lambda
});
```

Le composant cache la complexité aux clients — si l'abstraction a été correctement sélectionnée, bien sûr. La classe du composant peut être réutilisée à plusieurs endroits, dans plusieurs projets, entre équipes, etc.

### Bibliothèque de composants standard

En fait, l'équipe Pulumi a conçu de nombreux composants de haut niveau qui construisent des abstractions par-dessus les ressources brutes. Les composants du package `@pulumi/cloud-aws` sont particulièrement utiles pour les applications serverless.

Voici l'application complète de raccourcissement d'URL avec la table DynamoDB, les Lambdas, l'API Gateway et les fichiers statiques basés sur S3 :

```ts
import * as aws from "@pulumi/cloud-aws";

// Créer une table `urls`, avec `name` comme clé primaire.
let urlTable = new aws.Table("urls", "name");

// Créer un serveur web.
let endpoint = new aws.API("urlshortener");

// Servir tous les fichiers du répertoire www à la racine.
endpoint.static("/", "www");

// GET /url/{name} redirige vers l'URL cible en fonction d'un nom court.
endpoint.get("/url/{name}", async (req, res) => {
    let name = req.params["name"];
    let value = await urlTable.get({name});
    let url = value && value.url;

    // Si nous avons trouvé une entrée, redirection 301 ; sinon, 404.
    if (url) {
        res.setHeader("Location", url);
        res.status(301);
        res.end("");
    }
    else {
        res.status(404);
        res.end("");
    }
});

// POST /url enregistre une nouvelle URL avec un nom court donné.
endpoint.post("/url", async (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];
    await urlTable.insert({ name, url });
    res.json({ shortenedURLName: name });
});

export let endpointUrl = endpoint.publish().url;
```

La chose la plus cool ici est que le *code d'implémentation* réel des AWS Lambdas est [entrelacé](https://blog.pulumi.com/lambdas-as-lambdas-the-magic-of-simple-serverless-functions) avec la *définition des ressources*. Le code ressemble beaucoup à une application Express. Les AWS Lambdas sont définies comme des lambdas TypeScript. Tout est fortement typé et vérifié à la compilation.

Il convient de noter qu'à l'heure actuelle, de tels composants de haut niveau n'existent qu'en TypeScript. On pourrait créer ses propres composants personnalisés en Python ou Go, mais il n'y a pas de bibliothèque standard disponible. L'équipe Pulumi [essaie activement de trouver un moyen de combler cette lacune](https://github.com/pulumi/pulumi/issues/2430).

### Éviter le verrouillage fournisseur (Vendor Lock-in) ?

Si vous regardez de près le bloc de code précédent, vous remarquerez qu'une seule ligne est spécifique à AWS : l'instruction `import`. Le reste n'est que du nommage.

Nous pouvons nous débarrasser de celle-là aussi : il suffit de changer l'importation en `import * as cloud from "@pulumi/cloud";` et de remplacer `aws.` par `cloud.` partout. Ensuite, nous devrions aller dans le fichier de configuration de la pile et y spécifier le fournisseur de cloud :

```
config: 
  cloud:provider: aws
```

Ce qui est suffisant pour faire fonctionner l'application à nouveau !

Le verrouillage fournisseur semble être une grande préoccupation pour beaucoup de gens lorsqu'il s'agit d'architectures cloud s'appuyant fortement sur des services cloud gérés, y compris les applications serverless. Bien que je ne partage pas nécessairement ces préoccupations et que je ne sois pas sûr que les abstractions génériques soient la bonne voie à suivre, la bibliothèque Pulumi Cloud peut être une direction pour l'exploration.

L'image suivante illustre le choix du niveau d'abstraction fourni par Pulumi :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tyZNF_k6q7gNWHwsjLFb5w.png)
_Couches d'abstraction Pulumi_

En travaillant au-dessus de l'API du fournisseur de cloud et du fournisseur de ressources interne, vous pouvez choisir de travailler avec des composants bruts avec une flexibilité maximale, ou opter pour des abstractions de plus haut niveau. Le mélange des deux dans le même programme est également possible.

### L'infrastructure en tant que véritable code

Concevoir des applications pour le cloud moderne signifie utiliser plusieurs services cloud qui doivent être configurés pour fonctionner harmonieusement ensemble. L'approche Infrastructure as Code est presque une exigence pour maintenir la gestion de telles applications de manière fiable en équipe et sur une période prolongée.

Le code de l'application et l'infrastructure de support deviennent de plus en plus fusionnés, il est donc naturel que les développeurs de logiciels prennent la responsabilité de définir les deux. La prochaine étape logique consiste à utiliser le même ensemble de langages, d'outils et de pratiques pour le logiciel et l'infrastructure.

Pulumi expose les ressources cloud sous forme d'API dans plusieurs langages de programmation polyvalents populaires. Les développeurs peuvent directement transférer leurs compétences et leur expérience pour définir, construire, composer et déployer des applications modernes natives du cloud et serverless plus efficacement que jamais.

_Publié initialement sur [mikhail.io](https://mikhail.io/2019/02/from-yaml-to-typescript-developers-view-on-cloud-automation/)._