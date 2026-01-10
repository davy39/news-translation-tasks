---
title: Comment utiliser votre plateforme API-first pour rendre votre prototype prêt
  pour la production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-07T16:41:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-api-first-platforms-to-build-your-websites-faster-part-2-68085d7cdf36
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LEexgp77Nph6PDWZAh2vnA.jpeg
tags:
- name: api
  slug: api
- name: Design
  slug: design
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser votre plateforme API-first pour rendre votre prototype
  prêt pour la production
seo_desc: 'By Mike Sedzielewski

  In the first part of this article, we laid out a way to build static-yet-dynamic
  websites using API-first platforms. This is one of many approaches you can use to
  quickly construct business application prototypes.

  In this article...'
---

Par Mike Sedzielewski

Dans la [première partie](https://medium.freecodecamp.org/how-to-use-api-first-platforms-to-build-your-websites-faster-e917e8318ee) de cet article, nous avons présenté une méthode pour construire des sites web statiques mais dynamiques en utilisant des plateformes API-first. Cela fait partie des nombreuses approches que vous pouvez utiliser pour construire rapidement des prototypes d'applications commerciales.

Dans cet article, nous allons passer au niveau supérieur. Nous voulons renforcer le prototype pour qu'il soit prêt à être déployé dans un environnement de production.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LEexgp77Nph6PDWZAh2vnA.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/1ow9zrlldJU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Patrick Hendry</a> sur <a href="https://unsplash.com/search/photos/mountain-bike?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Mais pour ce faire, nous devons surmonter certaines préoccupations de sécurité qui ne sont tout simplement pas présentes dans les sites web statiques. Comment connecter les quatre différents blocs de construction de notre application pour automatiser le processus commercial ? Comment pouvons-nous y parvenir sans sacrifier la vitesse d'itération que nous avons actuellement ? Rencontrez Zapier.

### Mais d'abord — que avons-nous construit jusqu'à présent

Au cas où vous ne vous en souviendriez pas, nous avons créé un squelette fonctionnel de [nostalgia.io](http://nostalgia.glitch.me) — un marché pour les experts en technologies du passé. Il s'agit d'un site web statique assemblé avec une légère interface utilisateur et fonctionnalité, construit sur quatre plateformes API-first (Contentful, Algolia, Timekit et Voucherify).

En résumé, l'application permet de parcourir les technologies, de rechercher des experts (en texte intégral), de trouver et de réserver un créneau de consultation dans leur calendrier, et enfin de faire en sorte que la page de paiement valide et accepte des codes de coupon uniques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E9BauUTpJhZtutx7p72VDw.png)

Le parcours heureux — lorsque n'importe quel Tom, Dick ou Harry entre sur le marché avec son code promo et se retrouve avec une réservation confirmée à prix réduit — fonctionne assez bien. N'oubliez pas que vous pouvez le voir en action et jouer avec le code source sur ce [dépôt glitch](https://glitch.com/edit/#!/nostalgia).

Mais nous avons encore de nombreux parcours malheureux. L'un des plus douloureux est l'ajout d'un nouvel expert. Pour l'instant, cela implique plusieurs étapes manuelles :

* Ajouter une entité expert à Contentful
* La propager à la recherche Algolia
* Assigner une ressource de calendrier dans Timekit
* Marquer un coupon comme utilisé pour qu'il ne soit plus valide

Et le problème est que vous ne pouvez pas automatiser ces opérations en utilisant notre approche actuelle de "site web statique". Cela est dû au fait que nos fournisseurs d'API ne permettent pas (heureusement) ce type de gestion des données en utilisant des clés API publiques. Chaque plateforme SaaS offre deux types de modes d'autorisation :

* Côté client : ensemble limité de fonctionnalités à utiliser sur les applications web et mobiles (la clé API peut être vue par tout le monde)
* Secret : accès complet au contrôle à utiliser uniquement dans la couche backend

Puisque nous n'avons pas encore de backend, nous devons trouver comment contourner ces limitations sans la nécessité de configurer des frameworks backend et une infrastructure de serveur web.

### Rencontrez Zapier

> _"Zapier est un outil qui vous permet de connecter les applications que vous utilisez tous les jours pour automatiser les tâches et gagner du temps." — Tutoriel de démarrage de Zapier_

En fait, vous avez peut-être déjà trempé un orteil dans le [monde merveilleux des Zaps](https://zapier.com/apps/integrations) lorsque vous vouliez automatiser certaines opérations personnelles comme "stocker les memes que j'approuve dans mon dossier Dropbox". Pourtant, vous avez peut-être manqué que, aujourd'hui, Zapier est bien plus que cela. Il a parcouru un long chemin depuis leur début en 2011.

Ils ont mis beaucoup d'efforts pour fournir une plateforme de niveau entreprise qui donne les blocs de construction pour coller diverses parties de vos plateformes logicielles de manière scalable.

Les littéralement milliers de plugins que vous pouvez trouver dans leur marketplace font de Zapier un outil puissant. En une heure, vous pouvez rapidement connecter la myriade de fournisseurs de logiciels populaires, différents départements, et éventuellement des entreprises dans leur ensemble. Dans la section suivante, nous allons vous montrer comment exploiter la puissance des zaps en rendant le marché Nostalgia plus robuste et sécurisé.

### Ajout de nouveaux experts à Contentful et Algolia

La première chose est de créer automatiquement une nouvelle entité. Pour ce faire, nous avons besoin d'un formulaire en ligne. Nous pouvons construire et héberger une simple application web qui connecte un formulaire HTML avec Contentful, mais pouvons-nous l'obtenir plus rapidement d'une manière ou d'une autre ? Frappons aux portes du répertoire Zapier. Après avoir tapé "formulaires", la première place sur la liste est occupée par Typeform. Nous vérifions la description, il a tout ce dont nous avons besoin, alors essayons-le.

#### Comment fonctionne Zapier en un mot ?

En coulisses, il s'agit d'appeler des requêtes HTTP et de capturer des webhooks. Ce que Zapier fournit est une couche d'authentification et une interface utilisateur intuitive pour mapper un format de données dans un autre. Le processus de mappage revient à invoquer une série de connecteurs (Zaps) qui récupèrent, convertissent et poussent les données dans le pipeline. Chaque pipeline commence par un soi-disant déclencheur qui est activé par un webhook. Construisons-en un.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4DWmwip1_Yldtj3JxLP0_g.png)
_Éditeur Typeform_

### Le premier petit obstacle

Maintenant, nous avions prévu de montrer comment Typeform collecte les données nécessaires pour créer un Expert, mais nous ne le ferons pas. La raison en est étrange. Le webhook atteint Zapier correctement, mais le format des données est d'une manière ou d'une autre corrompu.

Bien que les entrées de texte aient été traitées correctement, nous avons été bloqués avec l'entrée multi-sélection des technologies. Les valeurs que nous avons mises dans le formulaire n'apparaissaient tout simplement pas lorsque la charge utile de la requête est apparue dans Zapier. Le même problème s'est produit lorsque nous avons changé de la multi-sélection à un ensemble de trois booléens.

Nous avons donc décidé de changer de fournisseur pour SurveyMonkey — pour apprendre que l'envoi du contenu du formulaire à Zapier est disponible dans le plan Premium annuel. Finalement, nous avons donné une chance aux formulaires WuFoo, et ils ont très bien fonctionné.

Bien que cela nous ait pris un certain temps pour localiser le problème, il était encore plus rapide d'obtenir le formulaire fonctionnel que de construire une application web à partir de zéro. En tant que conseil général, nous suggérons d'être plus prudent lorsque vous prévoyez d'utiliser des Zaps officiels maintenant — même de fournisseurs reconnaissables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*snRRXlSsX-9vGTWj1dsn8Q.png)
_Un traitement réussi de l'envoi du formulaire WuFoo_

### Le principal obstacle...

Après avoir passé en revue la configuration du Zap WuFoo, nous avons fait en sorte que notre configuration écoute l'événement d'envoi du formulaire expert. Transformons les données pour qu'elles correspondent au modèle Contentful.

En utilisant le Zap officiel Contentful, la conversion est assez simple : vous prenez un champ du formulaire et le mappez dans un champ d'entité correspondant, comme dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tut_QxJViuN_NZRanu82JA.png)

Jusqu'à ce que nous voulions mapper les technologies. Comme vous vous en souvenez peut-être, chaque expert peut maîtriser de nombreuses technologies. Pour mapper cette relation un-à-plusieurs correctement, nous devrions fournir l'ID de l'entité Contentful de la technologie dans une structure d'objet spécifique, quelque chose comme :

```js
{ sys: { type: "Link", linkType: "Entry", id: "7Dtej0GnXqw6cSIMmA6Cko"}}
```

au lieu de simplement des noms qui proviennent des formulaires WuFoo. On pourrait suggérer que nous pourrions mapper la technologie dans un objet JSON, mais malheureusement, ce n'est pas possible. Le Zap Contentful envoie chaque champ sous forme de chaîne. Donc, la charge utile qui atteint réellement l'API Contentful ressemble à :

```json
{
  "fields": {
    "technologies": {
      "en-US": ["   { \n     \"sys\": {\n        \"type\": \"Link\",\n        \"linkType\": \"Entry\",\n        \"id\": \"5oKmKwfdjGO2cCaCkwamKW\"\n      }\n    }"]
    },
    "name": {
      "en-US": "Test Testowicz"
    }
  }
}
```

Et provoque une erreur 422 du côté de Contentful.

### ...et comment le surmonter

À ce moment-là, nous avons décidé de vérifier le Zap suivant dans le pipeline pour découvrir s'il y avait d'autres obstacles que nous n'avions pas prévus. Il s'est avéré que le connecteur Algolia n'est pas très mature. Comme l'entreprise pousse à la livraison du prototype, nous en sommes arrivés à la conclusion que nous ne voulons pas perdre plus de temps à tester ces zaps. Nous avons décidé de passer en mode manuel.

Heureusement, Zapier propose le [Code](https://zapier.com/help/code/) zap. [Introduit](https://zapier.com/blog/zapier-code/) il y a 2 ans, il est destiné à effectuer des opérations non standard en utilisant **du code personnalisé en JavaScript et Python** — y compris l'appel d'API tierces !

Cela est parfait pour notre approche "itération rapide". Nous obtenons une bonne vieille capacité de scripting et nous n'avons toujours pas à configurer le backend. Voyons comment cela peut nous aider avec le problème Contentful.

### Le Code Zap en action

Supprimons le Zap Contentful et mettons le Code à la place. Après avoir choisi JavaScript, vous devriez vous retrouver dans la vue "Edit Template". Maintenant, nous devons faire trois choses :

* Mapper les données de l'étape précédente du pipeline de données (WuFoo zap) dans des variables que vous pouvez utiliser directement dans le code
* Utiliser les variables pour préparer la charge utile dans le format approprié
* Envoyer la charge utile à Contentful avec un appel HTTP

La première chose est super facile car le gestionnaire de données d'entrée suggère magiquement les champs correspondants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*m1C3t-ZElZI5vqP_Vo8CsA.png)

Une fois que nous avons les entrées, rien ne peut nous empêcher d'envoyer la requête manuellement. Un rapide coup d'œil à la [référence de l'API](https://www.contentful.com/developers/docs/references/content-management-api/) de Contentful et nous y sommes :

```js
var technologies = [];

if (inputData.gwt) {
  technologies.push({
    sys: {
      type: "Link",
      linkType: "Entry",
      id: "7Dtej0GnXqw6cSIMmA6Cko"
    }
  });
}

if (inputData.symfony) {
  technologies.push({
    sys: {
      type: "Link",
      linkType: "Entry",
      id: "5S2iYV7inK6KyokCkwu4ss"
    }
  });
}

if (inputData.struts) {
  technologies.push({
    sys: {
      type: "Link",
      linkType: "Entry",
      id: "5oKmKwfdjGO2cCaCkwamKW"
    }
  });
}

fetch('https://api.contentful.com/spaces/n763nxcwuf4y/entries',{
  method: 'post',
  headers: {
    "Authorization": "Bearer <hidden>",
    "Content-Type": "application/vnd.contentful.management.v1+json",
    "X-Contentful-Content-Type": "expert"
  },
  body: JSON.stringify({
    fields: {
      name: {
        'en-US': inputData.name
      },
      price: {
        'en-US': parseInt(inputData.price)
      },
      projects: {
        'en-US': parseInt(inputData.projects)
      },
      description: {
        'en-US': inputData.profile
      },
      technologies: {
        'en-US': technologies
      }
    }
  })
})
.then(function(res) {
  return res.json();
})
.then(function(json) {
  var output = { expert: json } 
  callback(null, output);
})
.catch(callback);
```

Trois choses à surveiller :

* Zapier supporte fetch, mais c'est la seule fonctionnalité JS moderne. Sous le capot, il exécute Node v4
* Vous devez appeler `callback`, sinon Zapier ne sait pas quand le processus asynchrone est terminé
* Il y a une limite de timeout de 1s

Maintenant, vous pouvez lancer le test pour voir si l'entité est persistée dans Contentful.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AeVUal5H7ApV0BDN7nOEsA.png)

### Téléchargement d'une photo d'expert vers Contentful

Jusqu'à présent, nous avons réussi à ajouter une entité expert et à l'assigner aux technologies respectives. Une chose importante manque — la photo.

Contentful stocke les photos (et autres fichiers) dans une abstraction séparée appelée Assets. Le problème avec cela est que vous ne pouvez pas simplement télécharger une photo lors de la création d'une entité (comme nous l'avons fait dans l'étape précédente). Le processus de téléchargement ressemble à ceci :

* Créer un objet asset en fournissant le lien vers la ressource
* Déclencher le traitement de la ressource (dans le cas des images, il télécharge simplement le fichier)
* Assigner l'asset à une entité expert

Malheureusement, bien que le Zap officiel semble avoir cette option, elle n'est pas utilisable dans notre cas. La raison en est que le Zap ne retourne pas l'ID de l'asset ou un lien quelconque après son téléchargement. En conséquence, nous ne savons pas comment lier un expert à un asset. Que faire maintenant ? Le Code zap frappe encore !

En fait, nous devons l'utiliser deux fois :

* La première requête pour créer un asset

```js
fetch('https://api.contentful.com/spaces/n763nxcwuf4y/assets',{
  method: 'post',
  headers: {
    "Authorization": "Bearer <hidden>",
    "Content-Type": "application/vnd.contentful.management.v1+json"
  },
  body: JSON.stringify({
    fields: {
      title: {
        'en-US': inputData.name
      },
      file: {
        'en-US': {
          "fileName": inputData.name+".jpg",
          "upload": inputData.pictureLink,
          "contentType": "image/jpeg"
        }
      }
    }
  })
})
.then(function(res) {
  return res.json();
})
.then(function(json) {
  callback(null, json)
})
.catch(callback);
```

* La seconde pour télécharger l'image

```js
var assetURL = "https://api.contentful.com/spaces/n763nxcwuf4y/assets/" + inputData.assetId + "/files/en-US/process";

fetch(assetURL, {
  method: 'put',
  headers: {
    "Authorization": "Bearer <hidden>",
    "X-Contentful-Version": "1"
  }
})
.then(function(res) {
  callback(null, []);
})
.catch(callback);
```

Après avoir testé ces requêtes séparément, vous pouvez enfin les coller en utilisant InputData et les placer devant le Zap créant une entité et après le WuFoo zap. En fin de compte, nous obtenons le pipeline suivant :

_Wufoo > Code (création d'un asset) > Code (traitement de l'asset) > Code (création d'une entité)_

Vous avez peut-être remarqué que le code dans chaque zap suit le schéma copier & coller & modifier. Il est facile de changer les détails de la requête et de mélanger l'ordre d'invocation. Ce n'est pas la puissance à laquelle vous êtes habitué, mais c'est suffisant pour l'étape de prototype.

### Création de calendriers Timekit

Le moment d'implémenter les réservations est enfin arrivé. Comme Timekit ne fournit aucun Zap officiel, nous sommes obligés d'inviter à nouveau notre bon vieux ami. Vous vous souvenez peut-être que pour obtenir le calendrier d'un expert, vous devez créer une ressource dans Timekit puis obtenir l'instance de calendrier qui lui est assignée. Devinez quoi, l'API Timekit est si conviviale pour les développeurs qu'elle vous permet de l'atteindre avec une seule requête :

```js
var email = inputData.email;

fetch('https://api.timekit.io/v2/resources?include=calendars', // notice the include param
{
  method: 'post',
  headers: {
    "Authorization" : "Basic <hidden>",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    name: email,
    timezone: 'Europe/Warsaw'
  })
})
.then(function(res) {
  return res.json();
})
.then(function(resource) {
  callback(null, resource);
})
.catch(callback);
```

Maintenant, vous avez probablement compris l'idée de ce qui suit. Nous devons simplement placer le zap dans le bon ordre pour garantir que le processus commercial est couvert. Comme nous voulons stocker les liens Timekit dans une entité expert, nous devons placer ce Zap comme dans le pipeline ci-dessous :

_Wufoo > Code (création d'un asset) > Code (traitement de l'asset) > Code (création d'un calendrier) > Code (création d'une entité)_

### Peuplement de la recherche en texte intégral

La dernière partie de l'automatisation de cette étape est de rendre les experts recherchables. Si vous ne vous souvenez pas comment nous avons abordé cela avec l'aide d'Algolia, allez à la [première partie](https://medium.freecodecamp.org/how-to-use-api-first-platforms-to-build-your-websites-faster-e917e8318ee) pour rafraîchir votre mémoire. Ensuite, vous pouvez sauter directement au code :

```js
var objects = {
	requests: []
};

if (inputData.gwt) {
	objects.requests.push({
		action: "addObject",
		body: {
			name: inputData.name,
			description: inputData.description,
			projects: inputData.projects,
			price: inputData.price,
			contentfulID: inputData.contentfulID,
			technologies: { name: "Google Web Toolkit" }
		}
	});	
}

if (inputData.struts) {
	objects.requests.push({
		action: "addObject",
		body: {
			name: inputData.name,
			description: inputData.description,
			projects: inputData.projects,
			price: inputData.price,
			contentfulID: inputData.contentfulID,
			technologies: { name: "Apache Struts 1" }
		}
	});	
}

if (inputData.symfony) {
	objects.requests.push({
		action: "addObject",
		body: {
			name: inputData.name,
			description: inputData.description,
			projects: inputData.projects,
			price: inputData.price,
			contentfulID: inputData.contentfulID,
			technologies: { name: "Symfony 1.x" }
		}
	});	
}

fetch('https://N675AF3ESI.algolia.net/1/indexes/experts/batch',{
  method: 'post',
  headers: {
    "X-Algolia-API-Key" : "<hidden>",
    "X-Algolia-Application-Id" : "N675AF3ESI"
  },
  body: JSON.stringify(objects)
})
.then(function(res) {
  return res.json();
})
.then(function(resource) {
  callback(null, resource)
})
.catch(callback);
```

Lorsque vous configurez cette étape, vous aurez tout le processus couvert :

* Quelqu'un ajoute un expert via le formulaire
* Notre "logiciel" crée un calendrier correspondant dans Timekit
* L'entité expert est stockée dans Contentful (avec la photo)
* L'expert devient recherchable en étant ajouté à l'index Algolia

C'est tout pour la partie interne du processus Nostalgia. Maintenant, donnons à nos coupons une chance de faire leur travail et d'attirer des clients vers nous !

### Remboursement des coupons

Commençons par rappeler comment fonctionnent les coupons Nostalgia. L'équipe marketing a imaginé 2 campagnes différentes avec des milliers de codes de coupon uniques :

* 25 % de réduction — exemples : nstlg-CCAMIDFf, nstlg-wZK4CoLs, nstlg-V8eV9A3p
* 5 $ de réduction — exemples : uub-nstlg, afl-nstlg, yeq-nstlg

Maintenant, lorsque vous en mettez un dans la case de coupon, le code est validé par rapport à l'API Voucherify et la réduction correspondante est appliquée. Lorsque vous sélectionnez enfin le créneau horaire et envoyez la demande de réservation à Timekit, sous le capot, le code est envoyé avec la charge utile et est persisté dans une entité Timekit.

Pour empêcher l'utilisation à nouveau du code unique, nous devons le marquer comme remboursé dans Voucherify. Nous aurions pu y parvenir en utilisant le widget Voucherify (il suffit de remplacer la méthode [validate](https://docs.voucherify.io/reference#vouchers-validate) par [redeem](https://docs.voucherify.io/reference#redeem-voucher-client-side)), mais nous voulons le marquer comme utilisé **uniquement si** la réservation a été confirmée par l'équipe des opérations (effectuée dans le tableau de bord Timekit). Comme l'entreprise souhaite passer de la confirmation automatique à la confirmation manuelle, nous sommes obligés de quitter l'environnement de site web statique et de nous tourner à nouveau vers Zapier.

### Capture des webhooks

Comme mentionné précédemment, vous chercherez Timekit dans le répertoire de Zap en vain. Nous devons trouver un autre moyen d'être informé d'une confirmation de réservation. Heureusement, le Zap Webhook tend une main secourable ici.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5wZ76HK3v346MiPMJasiUg.png)

Lorsque vous passez par le flux de configuration en 5 étapes, vous obtenez une URL de point de terminaison unique qui peut être utilisée pour envoyer des notifications via des requêtes HTTP. Votre prochaine tâche consiste à la mettre dans un appel de webhook dans Timekit sous un événement spécifique — dans notre cas, il s'agit d'une confirmation de réservation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4l3cQGN2CbBaPY53y5jeQw.png)

### La touche finale — gestion du remboursement

La toute dernière étape consiste à invoquer la méthode de remboursement pour marquer le coupon comme utilisé. Pour ce faire, nous pouvons utiliser le [Voucherify Zap officiel](https://zapier.com/developer/invite/62387/cdcdf9275d825dff01c4da836b4c445f/). Tout ce que vous avez à faire est d'autoriser Zapier à invoquer le remboursement et de mapper les détails du client capturés par le zap de webhook dans la structure appropriée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DNp2gEE3qNW1XKUrG6CRRA.png)

Après avoir effectué quelques tests, nous pouvons voir que Voucherify suit les remboursements de coupons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4rM5iC2w4nt47WYkhYN7hA.png)

Maintenant que les remboursements sont gérés correctement, le marketing peut lancer de nouvelles campagnes du jour au lendemain, et l'implication des développeurs n'est pas nécessaire pour générer, distribuer et accepter de nouveaux codes de coupon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QyqQSmNd01mivX7WEGHcKQ.png)

### Rapide et sale

Félicitations ! Avec seulement ces deux pipelines Zapier, nous avons construit quatre blocs de construction de manière sécurisée et prête pour la production. Nous admettons que la solution semble rapide et sale, mais elle fonctionne, et elle a été livrée dans un délai raisonnable.

Bien sûr, nous aurions pu améliorer le code en supprimant les doublons et ainsi de suite. Mais c'est un prototype de toute façon, et il va être réécrit lorsque l'entreprise décidera que la direction qu'ils veulent prendre avec les premiers clients a du sens.

Lorsque vous allez pour la première fois dans le répertoire des plugins Zapier, tout semble brillant et reluisant. Mais le diable, comme on dit, est dans les détails. Pour être honnête, avant de nous lancer dans cet article, nous étions super optimistes quant à la configuration de Zapier. Mais en nous plongeant de plus en plus dans les détails, nous avons été confrontés à des problèmes avec les zaps que nous avions prévu d'utiliser. Nous les avons mis en évidence afin que vous puissiez les éviter sur votre chemin. Et nous avons, espérons-le, appris comment exploiter les fonctionnalités moins connues de Zapier pour combler les lacunes.

S'il vous plaît, s'il vous plaît, s'il vous plaît, rappelez-vous que le tandem "plateformes API-first <> Zapier" n'est pas un marteau brillant que vous pouvez utiliser pour frapper chaque clou possible. Ce que nous voulons souligner, c'est que parfois il existe des moyens plus rapides et tout aussi fiables de livrer un résultat commercial que d'écrire du code à partir de zéro.

—

Si vous aimez ces idées et que vous souhaitez apprendre à utiliser le monde merveilleux des API pour livrer des applications commerciales réelles et testées, vous pourriez être intéressé par notre [**série récente**](https://hackernoon.com/building-an-online-marketplace-from-scratch-introduction-738839e4e76).

![Image](https://cdn-media-1.freecodecamp.org/images/1*b_7EFJ3zfoM9Xl17VTgteg.png)