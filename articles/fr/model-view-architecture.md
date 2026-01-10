---
title: Comment fonctionne l'architecture Modèle-Vue-Contrôleur – Explication du MVC
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-04T20:51:41.000Z'
originalURL: https://freecodecamp.org/news/model-view-architecture
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--15--1.png
tags:
- name: software architecture
  slug: software-architecture
seo_title: Comment fonctionne l'architecture Modèle-Vue-Contrôleur – Explication du
  MVC
seo_desc: "By Nishant Kumar\nOver the last 20 years, websites have changed from simple\
  \ pages with a little CSS to become much more complex and powerful applications.\
  \ \nTo make these applications easier to develop, programmers use different patterns\
  \ and software a..."
---

Par Nishant Kumar

Au cours des 20 dernières années, les sites web sont passés de simples pages avec un peu de CSS à des applications beaucoup plus complexes et puissantes.

Pour faciliter le développement de ces applications, les programmeurs utilisent différents modèles et architectures logicielles pour rendre le code moins compliqué.

## Mais d'abord, qu'est-ce que l'architecture logicielle ?

Une architecture est une manière systématique de décrire un logiciel. Elle fait également référence à sa relation avec d'autres logiciels, et à la manière dont ils interagissent entre eux.

L'architecture logicielle inclut également d'autres facteurs tels que la stratégie commerciale, les attributs de qualité, la dynamique humaine, la conception et l'environnement informatique.

En d'autres termes, une architecture sert de **plan pour un système**.

## Architecture Modèle-Vue-Contrôleur (MVC)

L'architecture logicielle la plus populaire, de loin, est le Modèle-Vue-Contrôleur, ou MVC.

MVC divise toute application complexe en trois parties :

1. Le Modèle
2. La Vue
3. Le Contrôleur

Chacun de ces composants est conçu pour gérer un aspect spécifique d'une application et a des objectifs différents.

### Le Modèle

Le modèle contient toute la logique liée aux données avec lesquelles l'utilisateur travaille, comme les schémas et les interfaces d'un projet, les bases de données et leurs champs.

Par exemple, un objet client récupérera les informations du client dans la base de données, manipulera ou mettra à jour son enregistrement dans la base de données, ou l'utilisera pour rendre les données.

### La Vue

La vue contient l'interface utilisateur et la présentation d'une application.

Par exemple, la vue client inclura tous les composants de l'interface utilisateur tels que les zones de texte, les listes déroulantes et autres éléments avec lesquels l'utilisateur interagit.

### Le Contrôleur

Et enfin, le contrôleur contient toute la logique liée aux règles de gestion et gère les requêtes entrantes. Il est l'interface entre le Modèle et la Vue.

Par exemple, le contrôleur client gérera toutes les interactions et les entrées de la vue client et mettra à jour la base de données en utilisant le modèle client. Le même contrôleur sera utilisé pour afficher les données du client.

Voici un diagramme pour aider à visualiser l'architecture MVC et comment tout fonctionne ensemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--15-.png)
_Diagramme de flux du Modèle-Vue-Contrôleur_

## Comment fonctionne l'architecture MVC

Tout d'abord, le navigateur envoie une requête au Contrôleur. Ensuite, le Contrôleur interagit avec le Modèle pour envoyer et recevoir des données.

Le Contrôleur interagit ensuite avec la Vue pour rendre les données. La Vue ne se préoccupe que de la manière de présenter les informations et non de la présentation finale. Il s'agira d'un fichier HTML dynamique qui rend les données en fonction de ce que le Contrôleur lui envoie.

Enfin, la Vue envoie sa présentation finale au Contrôleur et le Contrôleur envoie ces données finales à la sortie utilisateur.

L'important est que la Vue et le Modèle n'interagissent jamais directement. La seule interaction qui a lieu entre eux passe par le Contrôleur.

Cela signifie que la logique de l'application et l'interface n'interagissent jamais entre elles, ce qui facilite l'écriture d'applications complexes.

Examinons un exemple simple :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--16-.png)

Voyons ce qui se passe ici. Tout d'abord, un utilisateur indique qu'il souhaite une liste de films via un navigateur web ou une application mobile.

Le navigateur envoie ensuite la requête au Contrôleur pour obtenir la liste des films.

Ensuite, le Contrôleur demande au Modèle de trouver la liste des films dans la base de données.

```express
router.get('/',ensureAuth, async (req,res)=>{ 
	try{ 
		const movies = await Movies.find() (*) 
		res.render('movies/index',{ movies }) 
    } 
    
	catch(err){ console.error(err) 
		res.render('error/500') } })     
```

Ensuite, le Modèle recherche dans la base de données et retourne la liste des films au Contrôleur.

```express
const mongoose = require('mongoose') 
const MovieSchema = new mongoose.Schema
({ 
	name:{ 
        type:String, 
        required:true 
    }, 
	description:{ 
    	type:String 
    } 
}) 

module.exports = mongoose.model('Movies',MovieSchema)
```

Si le Contrôleur obtient la liste des films du Modèle, le Contrôleur demande à la Vue de présenter la liste des films.

```express
router.get('/',ensureAuth, async (req,res)=>{ 
	try{ const movies = await Movies.find() 
		res.render('movies/index', { movies (*) }) } 

	catch(err){ 
    console.error(err) res.render('error/500') } 
})
```

Ensuite, la Vue reçoit la requête et retourne la liste rendue des films au Contrôleur en HTML.

```html
<div class="col" style="margin-top:20px;padding-bottom:20px">
    <div class="ui fluid card"> 
        <div class="content"> 
        <div class="header">{{movie.title}}</div> 
        	</div> <div class="extra content"> 
            <a href="/movies/{{movie._id}}" class="ui blue button"> Plus de {{movie.description}} </a> 
        </div> 
    </div>
</div>
```

Enfin, le Contrôleur prend ce HTML et le retourne à l'utilisateur, obtenant ainsi la liste des films comme sortie.

## Conclusion

Il existe de nombreuses architectures logicielles, mais Modèle-Vue-Contrôleur est la plus populaire et la plus largement utilisée. Elle réduit la complexité du code et rend le logiciel facilement compréhensible.

Maintenant, vous connaissez les concepts derrière le Modèle-Vue-Contrôleur.

> C'est tout pour aujourd'hui ! Bon apprentissage !