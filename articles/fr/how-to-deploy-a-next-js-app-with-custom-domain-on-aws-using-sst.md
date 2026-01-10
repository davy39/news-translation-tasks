---
title: Comment déployer une application Next.js avec un domaine personnalisé sur AWS
  en utilisant SST
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-07-24T07:18:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-next-js-app-with-custom-domain-on-aws-using-sst
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/AWS
seo_title: Comment déployer une application Next.js avec un domaine personnalisé sur
  AWS en utilisant SST
---

SST---Banner.png
tags:
- name: AWS
  slug: aws
- name: Next.js
  slug: nextjs
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'Les architectures serverless ont transformé la manière dont nous construisons et déployons des applications dans le cloud, apportant plus d\'efficience et de scalabilité.

Dans cet article, nous allons plonger dans le Serverless Stack Toolkit (SST), un framework pour construire des applications serverless. Nous allons déployer une application Next.js et configurer un domaine personnalisé, tout cela sans visiter la console AWS. 

Commençons ce voyage !

## Que signifie Serverless ?

Le terme "serverless" fait référence à un modèle de cloud computing où les développeurs peuvent construire et déployer des applications sans avoir besoin de gérer des serveurs. Dans une architecture serverless, le fournisseur de cloud gère l\'approvisionnement, la mise à l\'échelle et la maintenance des serveurs. Cela permet aux développeurs de se concentrer uniquement sur l\'écriture de code pour leurs applications.

Avec le serverless, les développeurs sont facturés en fonction de l\'utilisation réelle plutôt que des coûts fixes de serveur, ce qui en fait une solution rentable et scalable. Il offre une flexibilité et une agilité accrues, car les ressources sont automatiquement allouées et libérées en fonction de la demande. Cela élimine le besoin pour les développeurs de s\'inquiéter de la gestion de l\'infrastructure.

Maintenant que nous avons une bonne idée de ce que signifie serverless, voyons ce qu\'est le Serverless Stack Toolkit (SST).

## Comprendre le Serverless Stack Toolkit (SST)

Le Serverless Stack Toolkit, ou SST en abrégé, est un framework flexible et open-source conçu pour permettre un développement plus rapide et un déploiement fiable des applications serverless sur AWS.

Il vise à faciliter la définition de l\'infrastructure de l\'application par les développeurs en utilisant AWS CDK (Cloud Development Kit).

Vous pouvez l\'utiliser pour tester des applications en temps réel avec le développement Live Lambda, déboguer du code dans Visual Studio Code, gérer des applications via un tableau de bord basé sur le web, et déployer vers plusieurs environnements et régions de manière transparente.

## Avantages de l\'utilisation de SST

Voici quelques avantages de l\'utilisation de la pile SST :

### Infrastructure en tant que Code

Avec SST, les développeurs peuvent définir l\'infrastructure de leur application de manière programmatique en utilisant AWS CDK. Cela améliore le contrôle de version et la collaboration entre les membres de l\'équipe.

### Tests et Débogage Efficaces

SST permet le développement live Lambda, ce qui facilite les tests et le débogage des applications serverless localement avant le déploiement sur AWS. Cela réduit les problèmes potentiels et assure un déploiement plus fluide.

### Déploiement Simplifié

SST simplifie le processus de déploiement, permettant aux développeurs de déployer des applications vers plusieurs environnements et régions sans effort.

### Flexibilité des Langages

SST supporte plusieurs langages de programmation, dont JavaScript, TypeScript, Go, Python, C# et F#, offrant aux développeurs la flexibilité d\'utiliser leur langage préféré pour construire des applications serverless.

Maintenant que nous avons compris ce qu\'est SST et certains de ses avantages, voyons la puissance de SST en action.

## Comment Configurer AWS

Avant d\'ajouter SST, nous devons configurer certaines informations d\'identification AWS. Pour cela, tapez la commande suivante dans votre terminal :

```
aws configure
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-from-2023-07-18-02-29-05.png)
_AWS Configure_

Vous devrez entrer votre AWS Access Key ID, Secret Access Key, le nom de la région et le format de sortie. Si vous n\'avez pas ces clés, veuillez [créer un utilisateur IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) et entrer les informations d\'identification.

## Comment Ajouter SST à Votre Application Next.js

Nous pouvons utiliser SST dans une application Next.js existante en _[mode drop-in](https://docs.sst.dev/what-is-sst#drop-in-mode)_ ou dans une application monorepo en _[mode standalone](https://docs.sst.dev/what-is-sst#standalone-mode)_.

Dans cet article, nous allons créer un nouveau projet Next.js et ajouter SST qui suit l\'installation en mode drop-in en utilisant les commandes suivantes :

```
yarn create next-app
cd my-app
yarn create sst
yarn install
```

**Note** : Vous devez vous assurer que vous avez le fichier `index.tsx` à l\'intérieur du dossier `/pages`. Sans ce fichier, vous obtiendrez des erreurs lors du déploiement de votre application avec SST. Vous n\'avez pas besoin d\'apporter de modifications à ce fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-100.png)
_Structure du dossier_

Une fois que vous avez exécuté les commandes ci-dessus, SST créera deux nouveaux fichiers — `sst.config.ts` et `sst-env.d.ts`

Nous devons définir toute notre infrastructure et nos piles dans le fichier `sst.config.ts`.

Vous pouvez utiliser ces commandes pour exécuter l\'application localement :

```
# Démarrer SST localement
yarn sst dev

# Démarrer Next.js localement
yarn dev
```

En exécutant la commande `yarn sst dev`, vous serez invité à entrer le nom de l\'étape. Veuillez entrer le nom de votre environnement. J\'utiliserai `dev` pour le nom de l\'étape de ce projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-96.png)
_Démarrer SST localement_

Asseyez-vous et regardez. Il créera automatiquement les rôles IAM nécessaires, les permissions et les piles CloudFormation.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-97.png)
_SST - Création des rôles IAM nécessaires, des permissions et de la pile_

Remarquez dans l\'image ci-dessus que vous pouvez voir l\'URL de la console, `https://console.sst.dev/sst-demo/dev`. Avec l\'URL de la console, vous pouvez voir les logs en temps réel, invoquer des fonctions, rejouer des invocations, faire des requêtes, exécuter des migrations, voir les fichiers téléchargés, interroger vos API GraphQL, et plus encore !

Plutôt génial, non ? Je vous recommande de visiter la [documentation officielle](https://docs.sst.dev/console) pour en savoir plus sur les services qu\'ils offrent.

Ensuite, démarrez le site Next.js en exécutant `yarn dev`. Vous devriez voir la page par défaut après cela.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-98.png)
_Page par défaut de Next.js_

Notre application Next.js est maintenant prête à être déployée sur AWS ! Il suffit d\'exécuter la commande suivante et de voir la magie.

```
yarn sst deploy --stage prod
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-99.png)
_OpenNext construisant l\'application Next.js_

Il commencera automatiquement à construire l\'application en utilisant [OpenNext](https://open-next.js.org/), à la déployer sur AWS en utilisant [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html), et à sortir l\'URL CloudFront. Cliquez sur le lien et vous devriez pouvoir voir votre application en cours d\'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-102.png)
_SST - Déploiement des changements et sortie de l\'URL CloudFront_

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-101.png)
_L\'application Next.js en cours d\'exécution_

## Comment Créer une Infrastructure en utilisant SST

Pour créer une infrastructure, nous devons simplement éditer `sst.config.ts` et importer des services AWS comme S3 bucket, RDS, API Gateway, et ainsi de suite depuis `sst/constructs`

Ajoutons une simple fonctionnalité de téléchargement de fichiers S3. Ouvrez le fichier `sst.config.ts` et ajoutez le code ci-dessous :

```
import { SSTConfig } from "sst";
import {Bucket, NextjsSite } from "sst/constructs";

export default {
  config(_input) {
    return {
      name: "sst-tutorial",
      region: "us-east-1",
    };
  },
  stacks(app) {
    app.stack(function Site({ stack }) {
      const bucket = new Bucket(stack, "public");
      const site = new NextjsSite(stack, "site",{
        bind:[bucket],
      });
      stack.addOutputs({
        SiteUrl: site.url,
      });
    });
  },
} satisfies SSTConfig;
```

Ici, nous créons un nouveau bucket S3 public et le lions avec notre `NextjsSite`. 

Éditons notre page d\'index pour ajouter la fonctionnalité de téléchargement de fichiers.

### Comment Télécharger des Fichiers vers S3 en utilisant SST

Pour télécharger un fichier vers S3, nous devons générer une URL pré-signée. Pour cela, nous devons ajouter ce package `@aws-sdk/s3-request-presigner` dans notre dépôt.

```
yarn add @aws-sdk/s3-request-presigner
```

Ouvrez le fichier `index.tsx` et créez une fonction appelée `getServerSideProps` au-dessus de la fonction Home, comme montré dans l\'extrait de code ci-dessous.

```
...
import { Bucket } from "sst/node/bucket";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
...
export async function getServerSideProps() {
  const command = new PutObjectCommand({
    ACL: "public-read",
    Key: crypto.randomUUID(),
    Bucket: Bucket.public.bucketName,
  });
  const url = await getSignedUrl(new S3Client({}), command);
  const bucketName = Bucket.public.bucketName
  console.log(bucketName)
  return { props: { url } };
}
```

Mettez à jour la fonction `Home()` avec le code suivant.

```
import styles from "@/styles/Home.module.css";
export default function Home({ url }: { url: string }) {
  return (
    <main className={styles.main}>
     <div className={styles.center}>
        <a
          href="https://5minslearn.gogosoon.com/?ref=github_sst_app"
          className={styles.card}
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2 className={inter.className}>
            5minslearn <span>-&gt;</span>
          </h2>
          <p className={inter.className}>Apprendre la tech en 5 mins</p>
        </a>
      </div>
      <form
        className={styles.form}
        onSubmit={async (e) => {
          e.preventDefault();

          const file = (e.target as HTMLFormElement).file.files?.[0]!;

          const image = await fetch(url, {
            body: file,
            method: "PUT",
            headers: {
              "Content-Type": file.type,
              "Content-Disposition": `attachment; filename="${file.name}"`,
            },
          });

          window.location.href = image.url.split("?")[0];
        }}
      >
        <input name="file" type="file" accept="image/png, image/jpeg" />
        <button type="submit" className={inter.className}>
          Télécharger
        </button>
      </form>
    </main>
  );
}
```

J\'ai ajouté une entrée avec un type de fichier `file` et un bouton pour soumettre le formulaire. L\'image sélectionnée sera téléchargée vers S3 lorsque le formulaire sera soumis. Il est temps de déployer les changements.

Pour déployer les changements, exécutez la commande `yarn sst deploy`.

Une fois déployé, vous verrez une page comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-103.png)
_Next.js en cours d\'exécution avec les changements mis à jour_

Maintenant, vous pouvez télécharger n\'importe quelle image et vérifier votre S3. Le fichier sélectionné sera téléchargé vers votre bucket S3.

Super, nous avons déployé avec succès les changements. Mais nous avons toujours l\'URL aléatoire générée par CloudFront qui peut être difficile à mémoriser pour les humains. Configurons un domaine personnalisé.

## Comment Configurer des Domaines Personnalisés

Pour configurer des domaines personnalisés, nous avons besoin d\'un domaine ou sous-domaine valide. Vous pouvez en créer un en utilisant Route 53 ou votre fournisseur de domaine préféré comme GoDaddy, Namecheap, etc.

Si vous avez un domaine sur un fournisseur DNS externe, vous devrez créer un certificat SSL sur AWS Certificate Manager (ACM).

J\'ai mon domaine sur Cloudflare. Si vous avez le vôtre avec d\'autres fournisseurs comme Namecheap ou GoDaddy, alors les étapes ci-dessous devraient toujours fonctionner pour vous. 

### Comment Pointer le CNAME vers CloudFront

1. Connectez-vous à votre fournisseur DNS.
2. Ajoutez un CNAME. Dans mon cas, j\'ai utilisé `aws` comme nom car mon domaine est `aws.gogosoon.com`, et la cible comme l\'URL CloudFront sans `https`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-104.png)

Nous avons réussi à pointer notre CNAME vers CloudFront. Maintenant, créons un certificat SSL pour notre domaine.

### Comment Créer un Certificat ACM

Les certificats ACM sont des certificats SSL/TLS gérés qui peuvent être utilisés avec une variété de services AWS, y compris CloudFront.

Cependant, il y a une exigence spécifique pour l\'utilisation des certificats ACM avec CloudFront : le certificat doit être créé dans la **région US East (N. Virginia) (us-east-1)**. La raison en est que CloudFront a toute son infrastructure d\'approvisionnement/administrative basée dans **us-east-1**. 

Citant leur [documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html#https-requirements-aws-region) :

> Pour utiliser un certificat dans AWS Certificate Manager (ACM) pour exiger HTTPS entre les viewers et CloudFront, assurez-vous de demander (ou d\'importer) le certificat dans la région US East (N. Virginia) (us-east-1).

Voici les étapes à suivre pour créer un ACM :

1. Connectez-vous à la console AWS.
2. Recherchez le gestionnaire de certificats, basculez vers **us-east-1** et cliquez sur "Demander un certificat" dans la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-105.png)
_AWS ACM - Demander un certificat_

3. Entrez le nom de domaine que vous avez pointé dans la configuration de votre fournisseur DNS. Sous "Méthode de validation", sélectionnez "Validation par email" et cliquez sur suivant.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-114.png)
_AWS ACM - Demander un certificat_

4. Un certificat avec le statut "Validation en attente" sera créé. Vous recevrez un email d\'AWS avec un lien pour valider la demande.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-106.png)
_Certificat ACM avec statut en attente_

5. Une fois que vous avez cliqué sur le lien dans l\'email, le statut du certificat passera à "Émis". Copiez l\'ARN – nous en aurons besoin dans les étapes suivantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-111.png)
_Certificat AWS ACM émis_

Maintenant que nous avons créé le certificat avec succès, créons le domaine alternatif pour CloudFront.

### Comment Créer un Domaine Alternatif pour la Distribution CloudFront

1. Connectez-vous à la console AWS et recherchez CloudFront.
2. Cliquez sur la distribution créée par SST.
3. Dans l\'onglet "Général", cliquez sur le bouton "Modifier".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-115.png)
_Modifier la distribution CloudFront_

4. Entrez le nom de domaine alternatif et sélectionnez le certificat que nous avons créé. Laissez toutes les autres options par défaut et cliquez sur le bouton "Enregistrer les modifications".

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-108.png)
_Ajouter un domaine alternatif pour la distribution CloudFront_

Tout est prêt ! Modifions notre application pour déployer les changements sur notre domaine personnalisé.

### Comment Configurer un Domaine Personnalisé Externe en utilisant SST

Mettez à jour le fichier `sst.config.ts` avec le code suivant. Collez l\'ARN que vous avez copié lors de la création du certificat comme valeur pour la variable `certArn`. Remplacez le `domainName` par votre domaine :

```
import { SSTConfig } from "sst";
import {Bucket, NextjsSite } from "sst/constructs";
import { Certificate } from "aws-cdk-lib/aws-certificatemanager";


export default {
  config(_input) {
    return {
      name: "sst-tutorial",
      region: "us-east-1",
    };
  },
  stacks(app) {
    app.stack(function Site({ stack }) {
      const bucket = new Bucket(stack, "public");
      const certArn = 'Collez l\'arn du certificat'
      const site = new NextjsSite(stack, "site",{
        bind:[bucket],
        customDomain: {
          isExternalDomain: true,
          domainName: "aws.gogosoon.com",
          cdk: {
            certificate: Certificate.fromCertificateArn(stack, "MyCert", certArn),
          },
        },
      });
      stack.addOutputs({
        SiteUrl: site.customDomainUrl || site.url,
      });
    });
  },
} satisfies SSTConfig;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-110.png)
_sst.config.ts - Modifications du fichier_

Exécutez `yarn sst deploy` pour déployer les changements sur un domaine personnalisé. Une fois déployé, vous devriez avoir l\'application en cours d\'exécution sur l\'URL personnalisée. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-113.png)
_Next.js déployé avec un domaine personnalisé en utilisant SST_

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-112.png)
_L\'application Next.js en cours d\'exécution avec un domaine personnalisé_

## Conclusion

Voilà ! Notre application Next.js est maintenant déployée sur AWS, et nous l\'avons connectée avec notre domaine personnalisé. Veuillez consulter le code source [ici](https://github.com/5minslearn/sst-demo).

Le framework SST fournit un excellent ensemble d\'outils pour déployer des applications serverless, contribuant considérablement à la vitesse de développement, à la scalabilité et à la gestion des erreurs.

N\'hésitez pas à explorer davantage sur [SST](https://docs.sst.dev/) et son potentiel pour transformer votre expérience de développement cloud. Bon codage !

Si vous souhaitez en savoir plus sur les services AWS, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_aws_sst_nextjs_deploy) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_aws_sst_nextjs_deploy)) et suivez-moi sur les réseaux sociaux.