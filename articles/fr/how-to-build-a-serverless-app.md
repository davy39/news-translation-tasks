---
title: Comment construire une application serverless entièrement fonctionnelle en
  moins de deux heures
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2021-04-09T19:02:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Create-Your-Own-Link-Shortener.png
tags:
- name: MongoDB
  slug: mongodb
- name: React
  slug: react
- name: serverless
  slug: serverless
- name: TypeScript
  slug: typescript
seo_title: Comment construire une application serverless entièrement fonctionnelle
  en moins de deux heures
seo_desc: 'If you want to dive deep into serverless full-stack apps, you''ve come
  to the right place.

  This post will guide you through the process of building your own link shortener.
  We are going to use TypeScript, React, Next.JS, and MongoDB. And to take advan...'
---

Si vous souhaitez plonger profondément dans les applications full-stack serverless, vous êtes au bon endroit.

Cet article vous guidera à travers le processus de création de votre propre raccourcisseur de liens. Nous allons utiliser TypeScript, React, Next.JS et MongoDB. Et pour tirer parti du traitement serverless, nous allons le déployer sur Vercel.

Vous pouvez trouver le **code** et la **vidéo** dans le résumé à la fin.

## Ce que vous apprendrez dans cet article

Ce n'est pas un autre article qui montre simplement comment démarrer une application Next.JS et ajouter deux pages simples. Je vais vous montrer comment construire une application propre.

Ce sera un raccourcisseur de liens entièrement fonctionnel - vous pouvez l'utiliser vous-même et même le partager avec vos amis, afin qu'ils puissent également raccourcir leurs liens.

L'application stockera les liens dans la base de données et suivra les redirections vers des sites web externes. Cela signifie que vous apprendrez toutes les pièces nécessaires pour construire d'autres applications serverless à l'avenir.

Il vous faudra probablement une heure ou deux pour compléter ce tutoriel, selon votre expérience et vos connaissances préalables. J'ai enregistré un [tutoriel YouTube (9 vidéos - 7-10 minutes chacune)](https://www.youtube.com/watch?v=IkATIunl_wE&list=PLbI79WtxN-IpgA_HaJ5j1jR1Zt_EAVasZ), c'est donc de là que vient mon estimation.

C'est à vous de décider comment vous abordez le processus. Si vous voulez aller vite, vous pouvez trouver le code sur mon GitHub - il suffit de le fork et de le déployer sur Vercel. Cela ne devrait pas prendre plus de 15 minutes.

Le résultat final ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-22-at-23.32.08-copy.png)

Vous pouvez [l'essayer ici](https://yals.vercel.app/).

## Prérequis

Ce tutoriel nécessite quelques bases de Node, juste les bases. Vous devriez également savoir comment utiliser Git et GitHub avant de suivre les instructions de cet article.

J'ai sauté la partie sur la création d'un dépôt Git et le push du code, car c'est une connaissance commune. Si vous ne savez pas comment faire, ce n'est pas grave - consultez simplement les tutoriels ci-dessous sur freeCodeCamp (ils sont gratuits !) avant de commencer à suivre les instructions de cet article :

* [Git et Github pour débutants](https://www.youtube.com/watch?v=RGOj5yH7evk).
* [Apprendre Node.js - Tutoriel complet pour débutants](https://www.youtube.com/watch?v=RLtyhwFtXQA).

## Commençons !

Nous devons créer un nouveau projet Next.JS, et nous pouvons le faire en tapant la commande suivante dans le terminal :

```bash
$ npx create-next-app yals
```

Vous pouvez remplacer l'acronyme YALS par votre propre nom. J'ai décidé d'appeler mon projet ainsi. L'acronyme signifie _Yet Another Link Shortener_.

Maintenant, nous allons configurer notre projet pour supporter TypeScript. Bien sûr, vous pouvez utiliser Next.JS sans TypeScript, mais je préfère l'utiliser chaque fois que possible.

TypeScript ajoute une vérification de type au code JavaScript, et cela m'a ouvert un nouveau monde. Ma vitesse de développement a augmenté car je n'avais plus besoin de vérifier les types de chaque variable. Je fais moins d'erreurs et économise beaucoup de temps que je passais auparavant à déboguer.

La configuration est simple : nous devons créer un fichier `tsconfig.json`, installer TypeScript et lancer le serveur de développement :

```bash
$ cd yals
$ touch tsconfig.json
$ npm install --save-dev typescript @types/react @types/node
$ npm run dev
```

Vous devriez voir la notification indiquant que Next.JS a détecté TypeScript et l'a configuré pour nous :

```bash
> yals@0.1.0 dev
> next dev

ready - started server on 0.0.0.0:3000, url: http://localhost:3000
We detected TypeScript in your project and created a tsconfig.json file for you.
```

Malheureusement, Next.JS ne convertira pas les fichiers JavaScript existants en TypeScript, nous devons donc les changer nous-mêmes.

Pas de soucis, il n'y a que trois fichiers. Nous devons changer les extensions de tous les fichiers React en `.tsx`, et tous les autres fichiers en `.ts` :

```bash
$ mv pages/index.js pages/index.tsx
$ mv pages/_app.js pages/_app.tsx
$ mv pages/api/hello.js pages/api/hello.ts
```

Voici à quoi ressemble l'arborescence de notre projet après les changements :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/file-name-change.png)

## Installer la bibliothèque d'interface utilisateur React avec Design System

L'un des plus grands avantages de React est sa grande communauté. La communauté crée des tonnes de bibliothèques open source utiles.

Lorsque je commence un nouveau projet React, je veux avancer rapidement et me concentrer uniquement sur la construction de fonctionnalités spécifiques au projet plutôt que de créer du code boilerplate. J'essaie d'utiliser autant de bibliothèques existantes que possible plutôt que de réinventer la roue.

Et je préfère toujours utiliser une bibliothèque de composants existante plutôt que de construire mes propres composants à partir de zéro - au moins pour la phase de prototypage.

Si votre entreprise a de nombreux produits, vous pourriez envisager d'engager un designer pour créer votre propre système de design. Sinon, vous pourriez utiliser un système existant et personnaliser son thème.

Les meilleures bibliothèques vous permettent de modifier l'apparence et le comportement de leurs composants, comme changer la palette de couleurs, les icônes, les polices, etc.

Dans ce tutoriel, j'ai décidé d'utiliser une bibliothèque d'interface utilisateur gratuite construite par Alibaba appelée [Ant Design](https://ant.design/components/overview/). Les composants sont faciles à utiliser et flexibles, nous pouvons donc facilement les adapter à nos besoins. Je l'utilise également pour le travail, donc l'apprendre n'a pas été une perte de temps.

Pour installer Ant Design, vous pouvez utiliser npm ou yarn. J'utilise npm dans ce tutoriel :

```
$ npm install --save antd
```

Maintenant, nous pouvons importer un nouveau système de design dans notre fichier de style principal en remplaçant le contenu par le code suivant :

```styles/global.css
# file: https://github.com/mateuszsokola/yals/blob/main/styles/globals.css

@import '~antd/dist/antd.css';
```

Vous avez peut-être remarqué que votre application a changé de style et utilise une autre police :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/theme-change.png)

Nous devons également installer `axios`. C'est un client HTTP un peu plus avancé que `fetch`. Il supporte la gestion des erreurs et les types dès la sortie de la boîte. Nous n'avons pas besoin de l'implémenter nous-mêmes, nous pouvons donc passer directement aux affaires.

```
$ npm install --save axios
```

## Comment styliser notre application web

Notre application est prête pour le développement. Nous allons commencer par créer le front-end React. J'ai coupé quelques coins ici, car je veux me concentrer davantage sur la construction d'un back-end serverless plutôt que sur la création d'un autre tutoriel React.

Je vais garder les instructions sur la partie front-end au strict minimum. Après tout, ce tutoriel ne concerne pas l'utilisation d'Ant Design dans React.

Ouvrons le fichier `pages/index.tsx` et collons le code suivant :

```pages/index.tsx
import Head from 'next/head'
import { useState } from 'react';
import axios, { AxiosError } from 'axios';
import { Alert, Button, Form, Input, Layout, Typography } from 'antd'
import styles from '../styles/Home.module.css'

const { Header, Content, Footer } = Layout;
const { Title } = Typography;

type ShortenLinkResponse = {
  short_link: string;
}

type ShortenLinkError = {
  error: string;
  error_description: string;
}

type FormValues = {
  link: string;
}

export default function Home() {
  const [status, setStatus] = useState<'initial' | 'error' | 'success'>('initial');
  const [message, setMessage] = useState('');
  const [form] = Form.useForm();

  const onFinish = async ({ link }: FormValues) => {
    try {
      const response = await axios.post<ShortenLinkResponse>('/api/shorten_link', { link });
      setStatus('success');
      setMessage(response.data?.short_link);
    }
    catch(e) {
      const error = e as AxiosError<ShortenLinkError>;
      setStatus('error');
      setMessage(error.response?.data?.error_description || 'Something went wrong!');
    }
  }

  const onFinishedFailed = () => {
    setStatus('error');
    const error = form.getFieldError('link').join(' ');
    setMessage(error);
  }

  return (
    <Layout>
      <Head>
        <title>Yet Another Link Shortner</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header>
        <div className={styles.logo} />
      </Header>
      <Content className={styles.content}>
        <div className={styles.shortner}>
          <Title level={5}>Copy &amp; Paste your lengthy link</Title>
          <Form
            form={form}
            onFinish={onFinish}
            onFinishFailed={onFinishedFailed}
          >
            <div className={styles.linkField}>
              <div className={styles.linkFieldInput}>
                <Form.Item name="link" noStyle rules={[{
                  required: true,
                  message: 'Please paste a correct link',
                  type: 'url',
                }]}>
                  <Input placeholder="https://my-super-long-link.com/blah-blah-blah-blah-blah-blah-blah-blah-blah-blah-blah-blah" size="large"/>
                </Form.Item>
              </div>
              <div className={styles.linkFieldButton}>
                <Form.Item>
                  <Button type="primary" htmlType="submit" style={{ width: '100%' }} size="large">
                    Shorten!
                  </Button>
                </Form.Item>
              </div>
            </div>
          </Form>
          {['error', 'success'].includes(status) && (<Alert showIcon message={message} type={status as 'error' | 'success'} />)}
        </div>
      </Content>
      <Footer className={styles.footer}>
        Yet Another Link Shortener (YALS) &copy; 2021
      </Footer>
    </Layout>
  )
}
```

Regardons ce qu'il y a sous le capot du code. L'application a trois états :

* `initial` - lorsque l'application est chargée et que l'utilisateur n'a encore pris aucune action.
* `success` - lorsque l'utilisateur a copié-collé le lien, cliqué sur "_Shorten_" et que notre système a généré un lien pour lui. L'application affichera un lien sous le formulaire.
* `error` - si quelque chose s'est mal passé, l'application affichera une erreur sous le formulaire. Par exemple, si l'utilisateur a entré un lien incorrect.

Nous avons exposé deux méthodes responsables de la gestion des formulaires. La première, `onFinish`, fait une requête à notre API pour générer un lien. La seconde, `onFinishedFailed`, est responsable de l'affichage des erreurs de validation du formulaire.

Nous n'avons pas besoin d'implémenter la validation du formulaire nous-mêmes. Ant Design est livré avec un composant Form avancé qui le gère pour nous.

L'apparence de notre application web peut encore être améliorée, ajoutons-y quelques styles. Nous devons créer un fichier CSS dans le répertoire `styles`. Je vais l'appeler `Home.modules.css`. Vous pouvez créer un fichier vous-même dans votre IDE ou en tapant cette commande :

```bash
$ touch styles/Home.module.css
```

Maintenant, nous devons ajouter quelques styles :

```styles/home.module.css
// @file: https://github.com/mateuszsokola/yals/blob/main/styles/Home.module.css
.logo {
  float: left;
  width: 120px;
  height: 30px;
  margin: 16px 24px 16px 0;
  background: rgba(255,255,255,.3);
}

.content {
  display: flex;
  align-items:  center;
  padding: 0 50px;
  min-height: calc(100vh - 64px - 70px);
}

.shortner {
  width: 100%;
  background: #fff;
  padding: 24px 20px;
}

.linkField {
  display: flex;
  width: 100%;
}

.linkFieldInput {
  flex: 100%;
  margin-right: 5px;
}

.linkFieldButton {
  width: 120px;
}

.footer {
  text-align: center;
}
```

Et voici à quoi votre application web devrait ressembler maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/layout.png)

D'accord, la vue de notre application est terminée. Maintenant, nous pouvons nous concentrer sur la logique métier derrière elle.

## Comment créer une base de données MongoDB

Nous sommes prêts à commencer le développement de notre back-end, mais nous devons décider comment nous allons stocker les liens.

Nous ne pouvons pas les stocker en mémoire car les applications serverless sont arrêtées après leur exécution. Cela signifie que nos liens disparaîtront immédiatement après leur création.

L'une des options est d'utiliser un service de base de données cloud. Dans ce tutoriel, nous allons utiliser MongoDB car il ne génère pas de surcharge du côté du développeur. Nous devons créer une base de données et immédiatement nous pouvons y stocker des données. Pas besoin de définir des schémas de table et des configurations sophistiquées.

J'ai décidé d'héberger notre base de données sur MongoDB Atlas car ils nous offrent notre première base de données gratuitement.

Le processus de création de votre compte est très intuitif, donc j'ai sauté cette partie. Les instructions commencent après vous être connecté à votre compte et que vous pouvez voir un tableau de bord de base de données vide. Il est censé ressembler à ce qui suit, et vous devez cliquer sur le bouton "_Build a Cluster_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-1.png)

Et nous allons créer un cluster partagé gratuit :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-2.png)

Nous allons héberger notre application web sur Vercel. J'ai fait quelques recherches rapides et j'ai découvert que Vercel héberge mes autres applications gratuites en Californie. J'ai donc dû trouver le cluster le plus proche de cet emplacement. Et j'ai découvert qu'ils ont un cluster hébergé chez Microsoft Azure en Californie.

C'est la principale raison pour laquelle je les ai choisis, car il est important de réduire la latence. Si vous souhaitez l'héberger ailleurs, vous devriez choisir l'emplacement de cluster le plus proche de votre hébergement.

Maintenant, vous devez cliquer sur les trois boutons. Veuillez suivre le même ordre que ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-3.png)

Il faudra jusqu'à trois minutes pour créer votre cluster. Pendant ce temps, créons un utilisateur de base de données. Il suffit de cliquer sur le lien "_Database Access_" sur le côté droit :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-3b.png)

Maintenant, nous devons cliquer sur le bouton "_Add New Database User_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-3aa.png)

Nous devons remplir le formulaire simple. Choisissons "_Password_" comme méthode d'authentification. Remplissez votre nom d'utilisateur, mot de passe (nous en aurons besoin plus tard, alors notez-le quelque part). Une fois que vous avez terminé le formulaire, cliquez sur le bouton "_Add User_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-3aaaa.png)

Maintenant, nous pouvons copier la chaîne de connexion à notre base de données. Nous devons cliquer sur le bouton "_Connect_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-4.png)

Sélectionnez "_Connect your application_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-5.png)

Et maintenant, nous pouvons copier notre chaîne de connexion :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/cluster-7.png)

Vous avez la chaîne de connexion dans votre presse-papiers, alors maintenant nous devons créer le fichier `.env` dans votre projet. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```
$ touch .env
$ touch .env.local
```

Maintenant, nous devons ajouter une nouvelle variable :

```.env
# file: https://github.com/mateuszsokola/yals/blob/main/.env

MONGODB_URI=""
```

Et nous devons mettre un contenu similaire dans `.env.local` avec une différence. Cette fois, nous allons coller notre chaîne de connexion là. **N'oubliez pas de remplir le nom d'utilisateur et le mot de passe** que vous avez créés auparavant.

```.env.local
# file: THIS FILE WILL NOT BE PUSHED INTO THE GITHUB REPOSITORY

MONGODB_URI="mongodb+srv://<username>:<password>@cluster0.v56ul.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
```

J'ai créé deux fichiers (`.env` et `.env.local`) au cas où vous souhaiteriez pousser le code dans un dépôt GitHub public. Le `.env.local` est ignoré, il ne sera donc pas poussé là-bas. Cela signifie que nous ne divulguons pas votre nom d'utilisateur et votre mot de passe au public. Veuillez en tenir compte et ne les ajoutez jamais dans le fichier `.env` !

Redémarrons le serveur de développement pour vérifier si Next.JS détecte les nouvelles variables.

```bash
Ctrl + C
$ npm run dev
```

Si vous voyez des logs vous indiquant que deux fichiers avec des variables ont été chargés, cela fonctionne :

```bash
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
info  - Loaded env from /Users/msokola/code/own/yals/.env.local
info  - Loaded env from /Users/msokola/code/own/yals/.env
event - compiled successfully
```

Maintenant, nous devons installer un adaptateur MongoDB afin de pouvoir exécuter des commandes sur la base de données. Installons deux nouveaux packages :

```
$ npm install --save mongodb
$ npm install --save-dev @types/mongodb
```

Nous avons résolu toutes les dépendances et nous pouvons connecter l'application à MongoDB. Créons un fichier `_connector.ts` dans le répertoire `pages/api` :

```bash
$ touch pages/api/_connector.ts
```

Et maintenant, nous devons écrire le code suivant :

```pages/api/_connector.ts
import { MongoClient } from 'mongodb';

let cachedDb;

export async function connectToDatabase() {
  if (cachedDb) {
    return cachedDb;
  }
  const client = new MongoClient(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });

  cachedDb = client;
  return await client.connect();
}
```

Regardons ce que fait le code. Il vérifie si la connexion à la base de données existe, et si ce n'est pas le cas, le code l'établit.

Faites attention à la variable `MONGODB_URI`. Sa valeur provient du fichier `.env.local` que vous avez créé précédemment. Grâce aux variables d'environnement, nous évitons de garder la configuration dans le code.

Next.JS crée une API d'exemple appelée `hello`. Nous allons y connecter notre connecteur pour vérifier si nous pouvons établir une connexion à la base de données.

Ouvrons `pages/api/hello.ts` et appelons `connectToDatabase` à l'intérieur du callback. Le résultat final devrait ressembler à ceci :

```
import { connectToDatabase } from "./_connector";

export default async (req, res) => {
  await connectToDatabase();

  res.status(200).json({ name: 'John Doe' })
}

```

Maintenant, vous pouvez démarrer votre serveur de développement et ouvrir cette URL dans votre navigateur : [http://localhost:3000/api/hello](http://localhost:3000/api/hello). Vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/api-test-1.png)

Si vous voyez une `Internal Server Error` au lieu de l'écran ci-dessus, cela signifie que votre application n'a pas pu se connecter à la base de données. Vous pouvez trouver plus d'informations dans votre terminal. Probablement, vous avez mal tapé votre nom d'utilisateur ou votre mot de passe.

## Comment créer la première API

Notre connexion à la base de données est prête, nous pouvons donc travailler sur notre back-end. Chaque raccourcisseur de liens a deux comportements : raccourcir les liens et les rediriger vers leurs URLs complètes. Cela signifie que nous devrons créer deux points de terminaison API, `shorten_link` et `redirect`. Commençons par le premier.

Nous devons créer un fichier `shorten_link.ts` dans le répertoire `pages/api`.

```
$ touch pages/api/shorten_link.ts
```

Et maintenant, nous devons ajouter le code suivant :

```pages/api/shorten_link.ts
import { connectToDatabase } from "./_connector";

export default async (req, res) => {
  const db = await connectToDatabase();

  if (req.body !== '' && req.body.link !== undefined && req.body.link !== '') {
    const entry = await db.db('links_db').collection('links_collection').insertOne({ link: req.body.link });

    res.statusCode = 201;
    return res.json({ short_link: `${process.env.VERCEL_URL}/r/${entry.insertedId}` });
  }

  res.statusCode = 409;
  res.json({ error: 'no_link_found', error_description: 'No link found'})
}
```

Ici, nous avons déclaré une API pour raccourcir les liens. Si le lien a été fourni, le système créera un nouveau lien dans la base de données. Sinon, il retournera le code `409` (Conflit) indiquant qu'il n'a trouvé aucun lien à raccourcir.

Maintenant, je vais essayer notre nouvelle API avec Postman. Si vous ne savez pas comment utiliser Postman et que vous souhaitez l'apprendre, vous pouvez [regarder ce tutoriel de freeCodeCamp](https://www.freecodecamp.org/news/learn-how-to-use-postman-to-test-apis/). Sinon, vous pouvez sauter cette section et passer à l'API suivante. Ce n'est pas nécessaire.

Nous devons sélectionner la méthode `POST` (1), entrer l'URL (2), cliquer sur l'onglet _Body_ (3), passer le `link` (4) et appuyer sur le bouton _Send_ (5). Nous devrions obtenir la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/postman-1.png)

Vous avez peut-être remarqué que j'ai marqué avec le trait rouge la partie `undefined` dans la propriété `short_link`. Comme vous pouvez le voir dans le code, nous avons utilisé le snippet suivant pour générer le lien court :

```javascript
{ short_link: `${process.env.VERCEL_URL}/r/${entry.insertedId}` }
```

La variable `VERCEL_URL` est une variable d'environnement disponible uniquement sur Vercel. Cela signifie que nous devons déployer notre application sur Vercel, et ensuite elle remplacera la bonne valeur. Next.JS ne la reconnaît pas par défaut, donc nous voyons `undefined` dans la réponse de l'API. C'est attendu pour le moment.

Vous pouvez également essayer le front-end de notre application - cela fonctionnera également :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/website-1.png)

## Comment implémenter les redirections

Puisque nous avons déjà créé le premier lien court, préparons les redirections des liens courts vers les URLs complètes.

Nous devons créer un fichier `redirect.ts` dans le répertoire `pages/api`, et nous devons y coller le code suivant :

```
import { ObjectID } from 'mongodb';
import { connectToDatabase } from "./_connector";

export default async (req, res) => {
  const db = await connectToDatabase();

  const entry = await db.db('links_db').collection('links_collection').findOne({ _id: new ObjectID(req.query.id as string) });

    if (entry !== null) {
        return res.redirect(301, entry.link);
    }

    return res.redirect(301, '/');
}
```

Comme vous pouvez le voir, nous essayons de trouver un lien par son id dans notre base de données. Si nous le trouvons, nous redirigeons l'utilisateur vers le bon emplacement. Si le système échoue à le trouver, nous redirigerons l'utilisateur vers la page principale.

J'ai essayé de tester ce point de terminaison avec Postman. Malheureusement, la réponse ne semble pas bonne - je pouvais voir le code HTML du site web plutôt que la redirection, donc j'ai décidé de sauter cette partie. Nous allons le déployer bientôt de toute façon, donc nous pouvons le tester dans l'environnement approprié.

## Comment réécrire nos URLs

Avant de pouvoir déployer notre application sur Vercel, nous devons faire quelque chose avec notre lien de redirection. Actuellement, si nous voulons rediriger vers le lien complet, nos utilisateurs doivent coller le lien suivant :

```
localhost:3000/api/redirect?id=606f512cbb6d7306eb5df189
```

Cela ne semble pas bon et c'est plus long que la plupart des liens que nos utilisateurs aimeraient raccourcir. Je pense que nous devrions suivre ce modèle :

```
localhost:3000/r/606f512cbb6d7306eb5df189
```

C'est plus court et un peu plus propre. Ce n'est toujours pas parfait mais assez bon pour notre exemple. Si vous le souhaitez, vous pouvez modifier le code pour supporter des alias ou une autre façon de générer les liens courts.

Nous devons créer un fichier `vercel.json` et y coller la définition suivante :

```vercel.json
{
    "rewrites": [{ "source": "/r/:id", "destination": "/api/redirect?id=:id" }]
}
```

Cette configuration indique à notre fournisseur d'hébergement que le serveur doit réécrire toutes les URLs commençant par `/r` en `/api/redirect?id=`.

Maintenant, le code et la configuration de notre application sont terminés. Si vous souhaitez la déployer sur Vercel, vous devez la pousser dans le dépôt GitHub. Comme je l'ai mentionné au début de l'article, j'ai sauté cette section ici - assurez-vous simplement de le faire avant de continuer.

## Comment déployer l'application sur Vercel

Une fois notre application prête, nous devons la publier afin que les utilisateurs puissent raccourcir leurs liens en utilisant notre service. Nous allons [déployer notre application sur Vercel](https://vercel.com/), car ils offrent un hébergement gratuit pour les applications serverless, et leur expérience développeur est tout simplement incroyable.

Comme d'habitude, je vais sauter le processus de création d'un nouveau compte. Vous pouvez en créer un en un clic en utilisant votre compte GitHub ou Google.

Une fois que vous vous êtes inscrit, vous devriez voir cet écran. Cliquez sur le bouton "_New Project_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-1.png)

Maintenant, vous devez sélectionner le dépôt GitHub que vous souhaitez importer. Dans mon cas, c'est "_yals_", mais vous avez peut-être appelé cela autrement. Si vous ne voyez pas votre dépôt, vous devez cliquer sur "_Adjust GitHub App Permission_" (le lien ci-dessous marqué avec le rectangle rouge) :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-2.png)

À l'étape suivante, nous devons sélectionner si nous utilisons un dépôt d'équipe ou un compte individuel. Dans notre cas, il s'agit d'un compte individuel :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-3.png)

Maintenant, nous devons configurer le projet. Ouvrons "_Environment Variables_", collez votre chaîne de connexion dans `MONGODB_URI`, cliquez sur le bouton "_Add_" et appuyez sur "_Deploy_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-4.png)

Notre application est en cours de déploiement. Vous devriez voir l'écran suivant une fois terminé. Il suffit de cliquer sur le bouton "_Visit_" :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-5.png)

Testons l'application en collant n'importe quel lien long dans le formulaire. J'ai utilisé un lien vers l'article que j'ai écrit pour freeCodeCamp il y a quelque temps, et voici ce que j'ai reçu :

* Avant : [`https://www.freecodecamp.org/news/how-to-deploy-react-apps-to-production/`](https://www.freecodecamp.org/news/how-to-deploy-react-apps-to-production/).
* Après : `https://yals.vercel.app/r/606f6723622f2c0008b64dc4`.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/vercel-6.png)

## Résumé

Félicitations ! Vous avez construit une application serverless entièrement fonctionnelle et vous êtes prêt à la partager avec vos amis.

Je comprends que les alias de liens ne sont pas les plus courts et les plus lisibles. Donc, comme toujours, vous pouvez améliorer le projet vous-même et nous montrer une autre façon de le faire. Vous pouvez le partager sur le forum freeCodeCamp ou dans la section des commentaires des vidéos YouTube ci-dessous.

J'ai créé un tutoriel YouTube où vous pouvez me regarder écrire chaque ligne de code. Il faut environ 90 minutes pour le regarder.

Gardez à l'esprit que c'est mon tout premier tutoriel YouTube et qu'il n'est pas parfait. Je n'ai pas d'expérience de travail avec la caméra ou d'enregistrement d'un screencast. J'ai essayé de rendre chaque vidéo meilleure que la précédente.

Si vous trouvez ces vidéos utiles, j'apprécierais que vous cliquiez sur le bouton like et que vous vous abonniez. Je vais publier quelques vidéos sur la façon de garder votre code JavaScript propre.

%[https://youtu.be/IkATIunl_wE]

Tous les épisodes :

1. [Configurer Next.JS + React + TypeScript.](https://youtu.be/IkATIunl_wE)
2. [Préparer une mise en page pour l'application React en utilisant Ant Design.](https://youtu.be/9oE7XwVv1Zo)
3. [Styliser le formulaire.](https://youtu.be/F3TePtPLPqs)
4. [Validation de formulaire avec les composants Ant React.](https://youtu.be/YB4OVbqFs-8)
5. [Codons la première API.](https://youtu.be/hrZ_IbE0GFs)
6. [Stocker des données dans MongoDB en utilisant Next.JS.](https://youtu.be/hrZ_IbE0GFs)
7. [Connecter l'API avec l'application React.](https://youtu.be/ILNpFkT0YNw)
8. [Redirections avec Next.JS.](https://youtu.be/maPmxCJT9Jo)
9. [Déployer une application serverless sur Vercel](https://youtu.be/0pS9VWy-YXI).

**Vous pouvez trouver tout le code dans ce dépôt GitHub** : [https://github.com/mateuszsokola/react-to-aws](https://github.com/mateuszsokola/react-to-aws)

Vous pouvez me DM sur Twitter : [@msokola](https://twitter.com/msokola)

C'est tout pour aujourd'hui ! J'espère que vous avez aimé et que vous passez une excellente journée :)