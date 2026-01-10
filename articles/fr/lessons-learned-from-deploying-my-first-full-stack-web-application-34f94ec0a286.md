---
title: Leçons tirées du déploiement de ma première application web full-stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T09:38:32.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/edu-lauton-TyQ-0lPp6e4-unsplash.jpg
tags:
- name: learning
  slug: learning
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Leçons tirées du déploiement de ma première application web full-stack
seo_desc: 'By Will Abramson

  I recently achieved one of my long-term goals: deploying my first full-stack web
  application.

  In this post, I’ll be sharing the lessons I learned from a beginner’s perspective,
  along with some useful tutorials I followed, key roadblo...'
---

Par Will Abramson

J'ai récemment atteint l'un de mes objectifs à long terme : déployer ma première application web full-stack.

Dans cet article, je vais partager les leçons que j'ai apprises du point de vue d'un débutant, ainsi que quelques tutoriels utiles que j'ai suivis, les principaux obstacles que j'ai dû surmonter et les erreurs que j'ai commises en cours de route. Je veux aider d'autres développeurs à comprendre ce qui est impliqué dans le déploiement d'une application web.

Après avoir passé plus de six semaines à chercher sur Google, à essayer, à échouer et à réessayer, j'ai finalement réussi à déployer mon application web. Elle était composée d'un backend Node.js ainsi que d'un frontend React sur une machine virtuelle Amazon Web Services (AWS) EC2.

C'était un vrai défi, mais c'était vraiment satisfaisant, car à la fin, l'application a été déployée avec succès et est maintenant accessible via un nom de domaine public.

![Image](https://cdn-media-1.freecodecamp.org/images/7lX00uJHwR2qavL7Wm7oV-W-6LcApDtK1aP3)
_Saut de la victoire ! - Après avoir déployé votre application web_

La plus grande difficulté pour moi a été de trouver les informations. Je ne comprenais pas ce qui était impliqué dans le déploiement. J'ai donc eu du mal à trouver des réponses efficaces sur le web. Je n'ai pas réussi à trouver un seul guide pour l'ensemble du processus.

Espérons que je puisse simplifier la courbe d'apprentissage du déploiement pour la prochaine personne en rassemblant toutes les informations que j'ai apprises en un seul endroit.

Alors, c'est parti...

### Que signifie déployer une application ?

Une application web est divisée en deux parties.

* **Code côté client :** Il s'agit de votre code d'interface utilisateur frontend. Ce sont des fichiers statiques qui ne changent pas tout au long de la vie de votre application. Les fichiers statiques doivent exister **quelque part** afin que vos utilisateurs puissent les télécharger et les exécuter dans leur navigateur côté client. Je vais entrer dans plus de détails sur l'endroit où ce quelque part pourrait être plus tard.
* **Code côté serveur :** Cela traite toute la logique de votre application. Il doit être exécuté sur un serveur (machine), communément une machine virtuelle comme une instance EC2, tout comme vous l'exécutez lors du développement local.

Pour exécuter votre code local, le serveur doit en avoir une copie. J'ai simplement cloné mon dépôt Github sur le serveur à partir de l'interface de ligne de commande du serveur.

Vous devez également configurer votre serveur. Cela inclut :

* configurer la machine pour qu'elle puisse accéder à Internet et exécuter votre code
* exposer les ports corrects
* écouter les requêtes HTTP (requêtes Internet)
* pointer un nom de domaine personnalisé vers le serveur où votre application est exécutée

Vous saurez qu'il fonctionne lorsque vous pourrez accéder à votre application en utilisant votre nom de domaine personnalisé depuis n'importe quelle machine sur Internet et que toutes les fonctionnalités de votre application fonctionnent comme prévu.

Donc, c'est un aperçu. Mais, comment faisons-nous cela en réalité ?

### Pour commencer

Vous devriez diviser votre application et décomposer le problème. Vous déployez deux choses différentes : des fichiers statiques côté client et du code côté serveur.

Ma première erreur a été de penser à mon application comme un tout, plutôt que comme deux applications séparées qui communiquent entre elles.

Cela a ajouté à la complexité et a rendu les recherches sur Google inutiles. Cela m'a laissé submergé.

J'ai décomposé le problème en ces étapes. Bien que chaque problème puisse toujours être décomposé davantage.

* Configuration de votre VM et déploiement de votre Backend
* Déploiement de votre Frontend
* Faire communiquer les deux applications
* Pointer votre nom de domaine

Dans la figure ci-dessous, j'ai tenté de mettre le processus complet dans un diagramme.

![Image](https://cdn-media-1.freecodecamp.org/images/eBec3M2S8ovEMvyboray1w2JoZn1kp3uueXY)
_Le processus de déploiement. Créé avec [draw.io](https://www.draw.io/" rel="noopener" target="_blank" title=") - un outil de diagramme gratuit génial._

### Configuration de votre VM et déploiement de votre Backend

Dans mon cas, il s'agissait d'un serveur Express.js déployé sur une machine virtuelle Amazon EC2. J'aurais expliqué comment le faire, mais le tutoriel « [Création et gestion d'un serveur Node.js sur AWS - Partie 1](https://hackernoon.com/tutorial-creating-and-managing-a-node-js-server-on-aws-part-1-d67367ac5171) » fait un bien meilleur travail.

C'est le meilleur tutoriel que j'ai trouvé dans ce domaine et il couvre :

* Démarrer une machine virtuelle AWS
* Obtenir les groupes de sécurité corrects pour les ports
* Tirer le code de GitHub sur la machine virtuelle
* Exécuter votre serveur
* Utiliser Nginx, un serveur HTTP, pour transférer les requêtes du port 80
* Utiliser PM2 pour persister le processus d'exécution de votre serveur

C'était un sauveur, et sans lui, je serais probablement encore bloqué. Donc merci, [Robert Tod](https://www.freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286/undefined).

Vous pouvez facilement tester que votre serveur est en cours d'exécution en utilisant [Postman](https://www.getpostman.com/) pour envoyer une requête à l'un de vos points de terminaison Backend.

### Déploiement de votre Frontend

Maintenant que vous avez un serveur avec votre backend en cours d'exécution (je l'espère), vous devez faire fonctionner votre Frontend. C'est vraiment facile lorsque vous comprenez le processus.

Malheureusement, je ne l'ai pas compris pendant longtemps. Par exemple, au début, j'ai essayé d'exécuter mon Frontend en utilisant npm start.

Npm start crée un serveur de développement local, servant les fichiers de sorte qu'ils ne soient accessibles qu'en utilisant `localhost`, ce qui n'est pas ce que nous voulons.

Pour déployer le code Frontend, vous devez stocker tous les fichiers sur votre machine virtuelle dans un emplacement connu de votre serveur web. Le serveur web permet à un client de télécharger le code et de l'exécuter dans son navigateur.

[Apache](https://httpd.apache.org/) et [Nginx](https://www.nginx.com/) sont des exemples de serveurs web.

Un serveur web écoute certains ports, le port 80 ou plus communément le port 443 (sécurisé), et sert soit des fichiers statiques (votre code Frontend) soit transmet la requête à un port différent. Par exemple, nous avons vu une requête au Backend dans le tutoriel Node.js ci-dessus.

Comme le code Frontend est simplement une collection de fichiers stockés sur un serveur web, nous voulons rendre ces fichiers aussi petits et optimisés que possible. Cela garantit que le client peut les télécharger et les exécuter aussi rapidement que possible.

Des temps de chargement de page plus rapides égalent des utilisateurs heureux.

Tous vos fichiers JavaScript Frontend peuvent être regroupés en un seul fichier JavaScript. Cela se fait généralement en exécutant npm run build, en supposant que vous avez ce script défini dans votre package.json.

Vous pouvez en lire plus sur le regroupement de code [ici](https://medium.com/@andrejsabrickis/modern-approach-of-javascript-bundling-with-webpack-3b7b3e5f4e7).

En gros, le regroupement de votre application supprime tout ce qui n'est pas essentiel. Cela inclut le raccourcissement des noms et le placement de tout le code JavaScript dans un seul fichier. Il compilera également votre code dans la bonne version JavaScript. Cela permet à tous les navigateurs web de le comprendre et de l'exécuter (par exemple, convertir TypeScript en JavaScript).

Lorsque votre code est regroupé, vous devez simplement copier les fichiers dans votre serveur web. Ensuite, configurez votre serveur web pour servir les fichiers stockés à cet emplacement.

Voici un bon [article](https://medium.com/@jgefroh/a-guide-to-using-nginx-for-static-websites-d96a9d034940) sur le déploiement de fichiers statiques sur un serveur web Nginx.

Espérons que, si tout se passe bien (ce qui n'est jamais le cas), votre code Frontend fonctionne maintenant.

Visitez le DNS public de la machine virtuelle pour vérifier que les informations statiques du site se chargent.

### Faire communiquer les deux applications

J'avais donc mes deux applications en cours d'exécution individuellement, mais quelque chose n'allait pas. Je ne pouvais pas me débarrasser d'une erreur de requête réseau.

C'était le point le plus frustrant pour moi. J'étais si proche, mais j'ai rencontré quelques revers qui ont fini par prendre des semaines à résoudre.

Le partage des ressources cross-origin (CORS) est un mécanisme qui permet la communication entre différentes adresses IP ou ports. Vous voulez que votre Backend soit autorisé à envoyer des données à votre Frontend.

Pour activer cela, votre Frontend doit inclure les en-têtes corrects lors de la demande de ressources. Cela peut être fait de deux manières :

* Les en-têtes peuvent être ajoutés dans Nginx, bien que cela nécessite quelques recherches. Vous pouvez commencer [ici](http://oskarhane.com/avoid-cors-with-nginx-proxy_pass/).
* Vous pouvez [utiliser le module cors npm](https://www.npmjs.com/package/cors) pour inclure les en-têtes.

Un excellent moyen de tester si cela fonctionne est de regarder dans l'onglet réseau des outils de développement de votre navigateur. Cela montre toutes les requêtes que votre application effectue. Si vous sélectionnez une requête, vous pouvez voir où la requête est allée et quels en-têtes elle incluait.

![Image](https://cdn-media-1.freecodecamp.org/images/y1rlso3aqjosHHJaBZpKCwdOugXiYNOLLHQW)

Une fois que vous avez les bons en-têtes de requête envoyés avec votre requête, vous devez vous assurer que les requêtes vont au bon endroit. Cela devrait être l'adresse et le port de votre serveur Backend EC2 et **pas** l'adresse et le port de votre serveur Backend **local** comme c'était le cas pour le mien.

Votre Frontend communique avec votre Backend en utilisant des requêtes HTTP. Quelque part dans votre code Frontend, vous lui direz où se trouve votre Backend.

```js
const networkInterface = createNetworkInterface({
 uri: 'http://0.0.0.0:5000/graphql',
});
```

Le mien ressemblait à ceci, ce qui n'allait clairement pas être correct pour mon serveur de production.

De manière ennuyeuse, cela faisait sembler que mon application fonctionnait lorsque je naviguais dessus sur ma machine locale, car mon serveur local était en cours d'exécution et pouvait retourner les informations requises.

Pour corriger cela, vous pouvez simplement changer l'URI défini, mais cela signifie devoir le changer à chaque fois que vous faites un développement supplémentaire, ce qui n'est **pas** la meilleure approche (je le sais parce que je l'ai fait).

Une solution plus sophistiquée consiste à inclure les deux URI et à utiliser des variables d'environnement pour sélectionner celui qui est approprié.

```js
const networkInterface = createNetworkInterface({   
   uri: process.env.NODE_ENV === 'production' ?      
                     'http://thecommunitymind.com/graphql' : 
                     'http://0.0.0.0:5000/graphql',
});
```

Simple mais efficace. Assurez-vous simplement de définir votre NODE_ENV sur production lorsque vous l'utilisez pour votre serveur de production.

Nous y sommes presque. En fait, votre déploiement pourrait fonctionner maintenant.

Mais j'avais un dernier problème à surmonter.

Même si ma configuration CORS était correcte, les en-têtes requis n'étaient pas inclus de manière cohérente et n'étaient ajoutés que parfois. Pour certaines requêtes POST, les en-têtes CORS n'étaient pas toujours présents. Très étrange !

Cette erreur m'a conduit à une chasse à l'oie frustrante en essayant de corriger ma configuration CORS dans Nginx, alors qu'en réalité cela n'avait rien à voir avec CORS.

En fait, je n'avais même pas besoin de faire quoi que ce soit avec CORS dans Nginx, car j'utilisais le module CORS npm.

L'erreur était due à deux autres problèmes :

* Ma base de données était incluse en tant que fichier sqlite dans le Backend et
* Mon gestionnaire de processus, [PM2](http://pm2.keymetrics.io/), surveillait les changements de fichiers

Ainsi, l'écriture dans le fichier de la base de données lors d'une requête POST provoquait le redémarrage du serveur par PM2. Cela conduisait à ce que les en-têtes corrects ne soient pas pris en compte, ce qui entraînait des erreurs trompeuses.

Un excellent conseil et que j'aurais aimé connaître plus tôt est de vérifier les journaux de votre serveur sur votre instance EC2. Que vous utilisiez PM2 ou autre chose, il y aura toujours un moyen de vérifier vos journaux. Il suffit de le rechercher sur Google !

Ces journaux ont fourni la clé pour résoudre mon problème.

J'ai simplement dû désactiver la capacité de surveillance de PM2. Bingo. Et enfin, cela a fonctionné.

### Pointer votre nom de domaine

C'est la cerise sur le gâteau. Vous voulez une URL propre et agréable pour votre application nouvellement déployée.

J'ai acheté mon nom de domaine via Amazon et j'ai utilisé Route 53 pour le pointer vers la bonne instance EC2. Ce fut une expérience surprenamment indolore.

Le [tutoriel](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html) d'Amazon était tout à fait suffisant.

![Image](https://cdn-media-1.freecodecamp.org/images/gi7iwvOLcVgcWyejOR2SDpnnV3hImGJPBpG5)
_Grand diagramme - Source : [WPBeginner](http://www.wpbeginner.com/beginners-guide/beginners-guide-what-is-a-domain-name-and-how-do-domains-work/" rel="noopener" target="_blank" title=")_

### Résumé

J'espère que cet article vous a aidé à comprendre le processus de déploiement d'une application web et, en fin de compte, à mettre votre projet incroyable en ligne — quel qu'il soit.

Au moins, vous devriez avoir une meilleure idée de ce qu'il faut rechercher sur Google !

Bonne chance.