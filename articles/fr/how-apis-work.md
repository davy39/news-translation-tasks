---
title: Qu'est-ce qu'une API et comment fonctionne-t-elle ? Les APIs pour les débutants
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2022-12-05T22:56:35.000Z'
originalURL: https://freecodecamp.org/news/how-apis-work
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/api-article.png
tags:
- name: api
  slug: api
- name: beginner
  slug: beginner
seo_title: Qu'est-ce qu'une API et comment fonctionne-t-elle ? Les APIs pour les débutants
seo_desc: "When I started learning to code, the term API would always haunt me. I\
  \ couldn't make sense of what it actually meant because I would hear people talking\
  \ about APIs in different contexts. \nThe biggest challenge was that I couldn't\
  \ find resources to le..."
---

Lorsque j'ai commencé à apprendre à coder, le terme API me hantait toujours. Je ne parvenais pas à comprendre ce que cela signifiait réellement parce que j'entendais les gens parler des APIs dans différents contextes. 

Le plus grand défi était que je ne trouvais pas de ressources pour apprendre les APIs en termes simples. 

Maintenant que je sais comment fonctionnent les APIs, j'ai décidé d'écrire ce guide pour tous les nouveaux venus qui ont du mal à comprendre ce sujet pas si compliqué mais encore confus dans le développement web et l'ingénierie logicielle.

## Qu'est-ce qu'une API ?

API signifie Application Programming Interface. L'application peut être n'importe quel logiciel qui effectue une tâche spécifique et l'interface est un point où deux applications communiquent. 

Une application agit comme un client et l'autre comme un serveur. Un client demande une ressource, par exemple une photo, et le serveur envoie cette photo au client. 

Le client ici peut être votre téléphone mobile, votre ordinateur de bureau ou portable, ou tout appareil que vous utilisez pour surfer sur l'internet. Et le serveur est un ordinateur plus grand qui stocke les données que vous voulez (une photo dans notre cas).

![Exemple de recherche Unsplash](https://www.freecodecamp.org/news/content/images/2022/12/unsplash-1.png)

Supposons que je veux une photographie de nature à télécharger sur mon blog de voyage. Je pourrais aller sur le site web d'Unsplash, taper "nature" dans la barre de recherche, et il retournerait un grand nombre de photographies de nature. 

C'est une API qui travaille en coulisses pour faire la conversation entre Unsplash et moi.

## Comment fonctionnent les APIs ?

Les ordinateurs suivent un protocole pour communiquer entre eux. Un protocole n'est rien d'autre qu'un ensemble de règles que les ordinateurs suivent pour communiquer. Tout ordinateur qui ne suit pas le protocole rompt le fil de communication. 

Vous avez peut-être utilisé le Bluetooth pour partager des données autrefois. Le Bluetooth n'est rien d'autre qu'un protocole pour que les appareils mobiles communiquent entre eux à courte distance. 

Lorsque vous demandez à votre ami de vous envoyer des photos de leur dernier voyage, votre appareil agit comme un client, et l'appareil de votre ami (celui qui envoie les photos) est le serveur. 

Ce n'est qu'un exemple de protocole. Nous avons un grand nombre de protocoles dans le monde de l'informatique - un pour presque tout.

Sur le web, nous utilisons le protocole HTTP (qui signifie Hyper Text Transfer Protocol). Les APIs disponibles sur le web utilisent le protocole HTTP pour un certain nombre de raisons - il est facile à utiliser et il est populaire, par exemple. 

Les communications qui ont lieu via le **protocole HTTP** sont également connues sous le nom de cycle demande-réponse car c'est exactement ainsi que fonctionne le protocole. Le client envoie une demande au serveur et le serveur répond au client concernant cette demande. 

Contrairement aux humains, les ordinateurs doivent être rigides pour communiquer entre eux ou ils rompent la communication. Pour cette raison, un client (ordinateur/appareil demandeur) a besoin d'un ensemble d'informations à envoyer avec la demande afin que le serveur réponde en conséquence. Ces informations incluent :

1. URL - une adresse web où vous souhaitez faire une demande
2. Méthode - si vous voulez des données déjà stockées quelque part ou si vous voulez sauvegarder de nouvelles données dans une base de données
3. En-tête - toutes les informations pertinentes sur votre demande, y compris le format dans lequel l'appareil client s'attend à recevoir les données
4. Corps - le corps contient les données de la demande réelle

Dans notre exemple Unsplash, l'URL est [https://unsplash.com/s/photos/nature](https://unsplash.com/s/photos/england). La méthode est GET parce que nous voulons que le serveur obtienne des images de nature en retour. L'en-tête inclut des informations comme le format que notre ordinateur s'attend à recevoir et à accepter - comme la signification de la langue, la langue de l'appareil, notre système d'exploitation, et ainsi de suite. Le corps inclut les données que nous devons envoyer au serveur, le mot-clé nature par exemple.

Il existe quatre types de méthodes pour les demandes HTTP que nous aborderons dans un instant. Pour l'instant, sachez simplement qu'une méthode indique ce que vous voulez faire avec les données disponibles sur le serveur. Par exemple, si vous voulez ces données sous forme de documents ou si vous voulez sauvegarder une nouvelle entrée dans les données sauvegardées quelque part.

Lorsque un client fait une demande, le serveur répond à cette demande. La réponse peut être les données que le client a demandées ou une erreur. 

Tout comme une réponse, une demande a une structure incluant une URL, un code de statut, un en-tête et un corps. Dans une demande, nous avons une méthode, qui a quatre types. Et dans la réponse, nous avons un code de statut qui indique si une demande a été acceptée ou refusée. 

### Méthodes HTTP

Il existe quatre méthodes HTTP disponibles, et chacune a sa propre fonctionnalité.

1. GET : comme déjà discuté, cela indique que le client demande des données à envoyer depuis le serveur.
2. POST : cette méthode indique au serveur que le client souhaite créer une nouvelle entrée dans une base de données. Par exemple, sauvegarder un nouveau billet de blog dans une base de données de tous les blogs précédents.
3. DELETE : comme le nom l'indique, le client souhaite supprimer un enregistrement de données d'une base de données.
4. PUT : cette méthode est utilisée lorsque un client souhaite mettre à jour ou modifier un enregistrement de données. Par exemple, changer votre mot de passe Facebook.

### Codes de statut HTTP

Il existe une longue liste de codes de statut HTTP, mais examinons quelques-uns des plus courants :

1. 200 OK : cela indique que la demande a été remplie avec succès par le serveur
2. 201 CREATED : l'entrée de données que vous avez demandée à créer a été créée
3. 404 NOT FOUND : cela indique que la ressource que vous avez demandée n'a pas été trouvée par le serveur
4. 500 INTERNAL SERVER ERROR : cela signifie qu'une erreur s'est produite du côté du serveur et qu'il n'a pas pu remplir votre demande

Il n'est pas nécessaire de mémoriser ces codes de statut, car la liste est longue et vous les apprendrez subconsciemment au fur et à mesure que vous les rencontrerez dans votre parcours de développement.

Néanmoins, il existe une gamme de codes de statut qui indiquent une réponse générique, comme vous pouvez le voir ici :

1. 100s : Réponses informationnelles, indiquant la progression de la demande
2. 200s : Succès, indiquant le succès de la demande
3. 300s : Redirection, indiquant que la demande a dû être redirigée ailleurs
4. 400s : Erreurs client, indiquant les erreurs qui se sont produites du côté du client
5. 500s : Erreurs serveur, lorsque le serveur échoue à répondre à une demande valide du client

## Types d'APIs

Vous souvenez-vous comment je vous ai dit que je me sentais confus lorsque les gens parlaient des APIs dans différents contextes ? C'est parce que nous avons également différents types d'APIs disponibles. 

Celles dont nous avons parlé dans cet article sont les APIs web qui utilisent le protocole HTTP. Les développeurs peuvent les utiliser pour créer une meilleure expérience utilisateur pour leurs utilisateurs. 

D'autres types incluent les APIs internes qui sont cachées aux utilisateurs externes et qui sont utilisées uniquement au sein d'une entreprise. 

Il existe également des APIs ouvertes qui sont disponibles pour être utilisées par n'importe qui gratuitement (comme l'API open weather map). Vous pouvez avoir des APIs partenaires qui sont partagées uniquement entre partenaires commerciaux pour effectuer leurs tâches commerciales, et des APIs composites qui combinent séquentiellement plusieurs demandes d'API en un seul appel d'API pour réduire la charge du serveur et créer une expérience plus rapide.

### Ressources pour en savoir plus sur les APIs :

Si vous souhaitez en savoir plus sur la conception des APIs, [voici un livre complet pour vous aider à démarrer](https://www.freecodecamp.org/news/rest-api-design-best-practices-build-a-rest-api/).

Et vous pouvez en savoir plus sur [les types d'APIs, les outils de test et la documentation ici](https://www.freecodecamp.org/news/what-is-an-api-and-how-to-test-it/).

Voici un tutoriel qui vous [apprendra tout sur les APIs REST](https://www.freecodecamp.org/news/rest-api-tutorial-rest-client-rest-service-and-api-calls-explained-with-code-examples/).

Et voici une [feuille de triche Fetch API](https://www.freecodecamp.org/news/fetch-api-cheatsheet/) pour vous aider à commencer à apprendre Fetch.

## Conclusion

Une API est une interface pour que deux ordinateurs communiquent afin d'effectuer des tâches sur l'internet. 

Les APIs suivent le protocole HTTP pour communiquer, qui a une structure de demande et de réponse spécifique. 

Différentes méthodes existent pour effectuer différentes tâches et de nombreux codes de statut sont disponibles qui indiquent si la demande est réussie, refusée ou en attente. 

Intéressé à se connecter sur LinkedIn ? Contactez-moi à [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/).