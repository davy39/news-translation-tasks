---
title: Comment créer une application Web de journalisation avec Server-Sent Events,
  RxJS et Express
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-09T18:06:54.000Z'
originalURL: https://freecodecamp.org/news/build-a-logging-web-app-with-server-sent-events-rxjs-and-express
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/Frame-11.png
tags:
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: logging
  slug: logging
- name: node
  slug: node
- name: TypeScript
  slug: typescript
seo_title: Comment créer une application Web de journalisation avec Server-Sent Events,
  RxJS et Express
seo_desc: "By Shayan\nSay you're working on your new great idea – a web or mobile\
  \ app, and a back end server. Nothing too complicated so far. Until you realize\
  \ that you need to stream data from your server to these clients. \nUsually, when\
  \ working on this, the fi..."
---

Par Shayan

Disons que vous travaillez sur votre nouvelle grande idée – une application web ou mobile, et un serveur back-end. Rien de trop compliqué jusqu'à présent. Jusqu'à ce que vous réalisiez que vous devez diffuser des données depuis votre serveur vers ces clients. 

Habituellement, lorsque vous travaillez sur cela, la première chose qui vient à l'esprit est d'utiliser l'un des outils à la mode, comme WebSockets, SocketIO, ou même un service payant qui s'en occupe pour vous. 

Mais il existe une autre méthode qui est généralement laissée de côté, et que vous n'avez peut-être pas encore entendue. Elle s'appelle SSE, abréviation de Server-Sent Events. 

SSE a une place spéciale dans mon cœur en raison de sa simplicité. Il est léger, efficace et très puissant. 

Pour expliquer SSE en détail et comment je l'utilise, je vais passer en revue un petit projet secondaire que j'ai réalisé et que je pense être une excellente vitrine pour SSE. J'utiliserai Typescript, Express et RxJS, alors préparez votre environnement et attachez vos ceintures car nous allons plonger dans du code.

Avant de commencer, il y a quelque chose que vous devez savoir sur SSE. Comme son nom l'indique, Server-Sent Events est unidirectionnel, du serveur vers le client. Cela peut être un point bloquant si votre client doit diffuser des données en retour vers le serveur. Mais ce n'est pas le cas dans de nombreux scénarios, et nous pouvons simplement nous appuyer sur REST pour envoyer des données au serveur.

## Quel est le projet ?

L'idée de ce projet est simple : j'ai un ensemble de scripts qui tournent sur des Raspberry Pis, des droplets sur Digital Ocean, et d'autres endroits qui ne sont pas facilement accessibles pour moi. Je veux donc un moyen d'imprimer les logs et de les consulter depuis n'importe où.

En tant que solution, je souhaite une application web de base pour pousser mes logs et avoir un lien direct vers ma session que je peux ouvrir sur n'importe quel appareil ou même partager avec d'autres.

Il y a quelques points à garder à l'esprit avant de continuer. 

Premièrement, les logs provenant de mes scripts ne sont pas très fréquents, et le surcoût de l'utilisation de HTTP est négligeable pour mon cas d'utilisation. Pour cette raison, j'ai décidé de publier mes logs via une API REST de base et d'utiliser SSE côté client pour souscrire aux logs entrants.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Frame-8-1.png)
_Exemple de journalisation_

Deuxièmement, cet outil est principalement destiné à déboguer rapidement les choses sur lesquelles je travaille. Il existe de nombreux outils prêts pour la production et pour les entreprises que je pourrais utiliser à la place. Mais je voulais quelque chose de très léger et facile à utiliser.

## Écrivons du code côté serveur

La configuration côté serveur est simple. Commençons donc par un diagramme pour vous donner une idée de la configuration avant d'expliquer tout en détail.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Frame-10-1.png)
_Diagramme du serveur_

Si nous considérons notre serveur back-end comme un pipeline, à une extrémité nous avons une série de publishers – dans notre cas, les scripts publiant des logs. À l'autre extrémité, nous avons des clients qui s'abonnent à ces logs.

Pour connecter ces deux extrémités, j'utiliserai un Subject RxJS. Il me permettra de publier n'importe quoi depuis les publishers via REST, puis de m'abonner à ces événements et de transférer les messages aux clients via SSE.

Pour commencer, définissons notre interface Log. Pour garder les choses simples, je ne définirai qu'un champ content qui contiendra nos informations de log.

```ts
interface Log {
  content: string;
}
```

### Comment configurer RxJS

Importons RxJS, créons un nouveau Subject pour nos Logs et définissons une fonction pour publier nos logs vers ce Subject. 

Bien sûr, nous pourrions exporter notre Subject et l'appeler directement depuis notre routeur, mais je préfère abstraire l'implémentation et ne fournir que la fonction emit au reste de mon code.

```ts
import { Subject } from 'rxjs';

// Log Subject
const NewLog$ = new Subject<Log>();

/**
 * Émettre un nouveau log vers le sujet RxJS
 * @param log
 */
export function emitNewLog(log: Log): void {
    NewLog$.next(log);
}
```

Enfin, définissons une nouvelle route sur notre serveur Express qui acceptera les nouveaux logs de notre client et les publiera vers la méthode emitNewLog que nous venons de créer.

```ts
app.post('/', (req: Request, res: Response) => {
  const content = req.body.content;
  const log: Log = { content: content };
  emitNewLog(log);
  return res.status(200).json({ ok: true });
});
```

Nous avons maintenant terminé avec le côté publication. Il reste à définir notre route SSE, à nous abonner au Subject RxJS et à livrer les logs à notre client.

### Comment configurer la route SSE

Définissons une nouvelle route pour notre connexion SSE. Pour activer SSE, nous devons envoyer quelques en-têtes à notre client. 

Nous voulons que **'Connection'** soit défini sur **'keep-alive'**, **'Cache-Control'** sur **'no-cache'**, et **'Content-Type'** sur **'text/event-stream'**. Ainsi, notre client comprendra que c'est une route SSE.

En outre, j'ai ajouté **'Access-Control-Allow-Origin'** pour CORS et **'X-Accel-Buffering'** défini sur **'no'** pour empêcher [Nginx](https://www.nginx.com/) de modifier cette route. Enfin, nous pouvons envoyer les en-têtes à notre client pour démarrer le flux d'événements.

```ts
app.get('/', (req: Request, res: Response) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('X-Accel-Buffering', 'no');
  res.flushHeaders();
});
```

Nous pouvons maintenant commencer à diffuser des données en écrivant quelque chose dans notre réponse. 

SSE fournit un protocole basé sur du texte que nous pouvons utiliser pour aider nos clients à différencier les types d'événements. Chacun de nos événements doit ressembler à ce qui suit :

```ts
event: ${event name}\n
data: ${event data}\n\n
```

Pour me faciliter la vie, j'ai créé une fonction helper pour prendre en charge la sérialisation pour nous.

```ts
/**
 * Sérialiseur de messages SSE
 * @param event: Nom de l'événement
 * @param data: Données de l'événement
 */
function serializeEvent(event: string, data: any): string {
  const jsonString = JSON.stringify(data);
  return `event: ${event}\ndata: ${jsonString}\n\n`;
}
```

Nous pouvons maintenant nous abonner au Subject RxJS que nous avons créé précédemment, sérialiser chaque nouveau log et l'écrire en tant qu'événement **NEW_LOG** à notre connexion.

```ts
app.get('/', (req: Request, res: Response) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('X-Accel-Buffering', 'no');
  res.flushHeaders();

  NewLog$.subscribe((log: Log) => {
    res.write(serializeEvent('NEW_LOG', log));
  });

}
```

Enfin, nous devons nous assurer de nous désabonner de notre observateur lorsque la connexion SSE est fermée. En mettant tout cela ensemble, nous devrions avoir quelque chose comme ceci :

```ts
app.get('/', (req: Request, res: Response) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('X-Accel-Buffering', 'no');
  res.flushHeaders();

  const stream$ = NewLog$.subscribe((log: Log) => {
    res.write(serializeEvent('NEW_LOG', log));
  });

  req.on('close', () => {
    stream$.unsubscribe();
  });
});
```

C'est tout ! Nous avons terminé avec notre serveur back-end et il est temps de passer au code front-end.

## Écrire le code client

S'abonner à notre route SSE dans le navigateur est très simple. D'abord, passons à notre code client et créons une nouvelle instance de l'interface **EventSource** et passons notre endpoint au constructeur.

```js
const eventSource = new EventSource("/");
```

Ensuite, nous pouvons ajouter des écouteurs d'événements pour les événements auxquels nous voulons nous abonner (dans notre cas, **NEW_LOG**) et définir une méthode de rappel pour gérer notre log.

```js
eventSource.addEventListener(
   "NEW_LOG", (event) => {
       const log = JSON.parse(event.data);
       // utiliser les données pour mettre à jour l'UI
    }, false
);
```

Et enfin, nous pouvons fermer la connexion lorsque nous avons terminé d'écouter ces événements.

```js
eventSource.close();
```

## Conclusion

Comme vous pouvez le voir, les Server-Sent Events rendent très facile la diffusion de contenu du serveur vers le client. Ils sont particulièrement utiles car nous obtenons une interface intégrée dans la plupart des navigateurs modernes, et nous pouvons facilement utiliser un polyfill pour ceux qui ne fournissent pas l'interface. 

De plus, SSE gère automatiquement la reconnexion pour nous au cas où le client perd la connexion avec le serveur. Par conséquent, c'est une alternative valable à SocketIO et WebSockets dans divers scénarios où nous avons besoin d'un flux d'événements unidirectionnel depuis le serveur.

Si vous êtes intéressé par ce projet, j'ai ajouté quelques fonctionnalités supplémentaires au code que nous venons de passer en revue et une interface web GUI que vous pouvez consulter ici : [LogSnag Console](https://logsnag.com/console).

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Frame-9-1.png)
_Démo de la console_