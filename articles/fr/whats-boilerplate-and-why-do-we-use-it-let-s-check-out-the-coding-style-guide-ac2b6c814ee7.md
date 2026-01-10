---
title: Qu'est-ce qu'un boilerplate et pourquoi l'utilisons-nous ? Nécessité d'un guide
  de style de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T16:14:41.000Z'
originalURL: https://freecodecamp.org/news/whats-boilerplate-and-why-do-we-use-it-let-s-check-out-the-coding-style-guide-ac2b6c814ee7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hrjnxp5fCjg2Hxv8IrImcg.png
tags:
- name: boilerplate
  slug: boilerplate
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'un boilerplate et pourquoi l'utilisons-nous ? Nécessité d'un
  guide de style de codage
seo_desc: 'By Meet Zaveri

  In Information Technology, a boilerplate is a unit of writing that can be reused
  over and over without change. By extension, the idea is sometimes applied to reusable
  programming, as in “boilerplate code.”

  Legal agreements, including s...'
---

Par Meet Zaveri

En technologie de l'information, un boilerplate est une unité de rédaction qui peut être réutilisée encore et encore sans changement. Par extension, l'idée est parfois appliquée à la programmation réutilisable, comme dans le « boilerplate code ».

Les accords légaux, y compris les termes et conditions des logiciels et du matériel, font un usage abondant des boilerplates.

Par exemple, un avocat peut vous donner un contrat de cinq pages à signer, mais la plupart du contrat est du boilerplate — ce qui signifie qu'il est le même pour tout le monde qui reçoit ce contrat, avec seulement quelques lignes changées ici et là.

En programmation informatique, le **boilerplate code** ou **boilerplate** fait référence à des sections de code qui doivent être incluses en de nombreux endroits avec peu ou pas d'altération. Il est souvent utilisé lorsqu'on parle de langages considérés comme _verbux_, c'est-à-dire que le programmeur doit écrire beaucoup de code pour effectuer des tâches minimales.

Par exemple, en développement web, un simple boilerplate pour HTML ressemblerait à ceci :

```
<!DOCTYPE html>                       <html class="no-js" lang="">                           <head>                                 <meta charset="utf-8">                                 <meta http-equiv="x-ua-compatible" content="ie=edge">         <title></title>                                 <meta name="description" content="">                           <meta name="viewport" content="width=device-width, initial- scale=1, shrink-to-fit=no"> <link rel="stylesheet" href="css/main.css"></head>                           <body>                                 <p>Hello world! This is HTML5 Boilerplate.</p>               <script src="js/vendor/modernizr-{{MODERNIZR_VERSION}}.min.js>     </script>
```

```
 </body></html>
```

Vous pouvez consulter l'ensemble du dépôt ici :

[**h5bp/html5-boilerplate**](https://github.com/h5bp/html5-boilerplate)  
[_html5-boilerplate - Un modèle frontal professionnel pour construire des applications ou sites web rapides, robustes et adaptables._github.com](https://github.com/h5bp/html5-boilerplate)

Dans les années 1890, le boilerplate était en fait coulé ou estampé en métal prêt pour la presse à imprimer et distribué aux presses de journaux et aux entreprises à travers les États-Unis. Jusqu'aux années 1950, des milliers de journaux recevaient et utilisaient ce type de boilerplate du plus grand fournisseur du pays, la Western Newspaper Union. Certaines entreprises envoyaient également des communiqués de presse sous forme de boilerplate afin qu'ils soient imprimés tels quels.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQnxLRyGkTqHamqONvrftA.png)

La plupart des développeurs web professionnels ont créé une collection d'actifs et de fragments de code qu'ils réutilisent sur des projets pour accélérer le développement. Il existe certains modèles universels ou presque universels que tous les sites web ont en commun. Plutôt que de les reconstruire continuellement, la plupart des développeurs commencent par copier le code qu'ils ont utilisé pour un projet similaire, puis commencent à le modifier.

Certains développeurs reconnaissent la valeur de ces modèles de démarrage boilerplate et prennent le temps de rendre le boilerplate plus générique et de les partager en ligne pour que d'autres puissent les utiliser.

Cela ne se limite pas au développement web. Il est utilisé au-delà dans l'IA/ML car il existe de plus en plus de frameworks et de bibliothèques.

#### Caractéristiques nécessaires du boilerplate pour les grands projets (prêts pour la production)

* Bonne et lisible documentation ?
* Structure de code avec un niveau d'abstraction plus profond
* Suit les normes de codage appropriées
* Dispose d'un outil CLI (pour le prototypage rapide et la configuration)
* Évolutif ?
* Outils de test faciles
* Modules API nécessaires
* Support pour l'internationalisation et la localisation ?
* Fractionnement de code
* Code serveur et client pour la configuration
* Structure de navigation et de routage appropriée ?

Après toutes ces spécifications minimales, vous devriez commencer à éditer et à modifier le code afin de construire votre projet.

Il existe certaines grandes entreprises technologiques qui construisent même leur propre boilerplate. Elles l'utilisent pour des projets respectifs et similaires au fil du temps.

Un exemple parfait pour cela serait le boilerplate de react.js :

[**react-boilerplate/react-boilerplate**](https://github.com/react-boilerplate/react-boilerplate)  
[_react-boilerplate - :fire: Une fondation hautement évolutive, hors ligne, avec la meilleure expérience développeur et un focus_github.com](https://github.com/react-boilerplate/react-boilerplate)

#### Boilerplate pour les petits projets (Scaffolding)

Ces types de boilerplates sont généralement des « Kits de démarrage » ou, en termes professionnels, on les appelle « Scaffolding ». Leurs principaux utilisateurs cibles sont les développeurs novices ou les nouveaux adopteurs précoces.

Il se concentre sur le prototypage rapide en créant les éléments nécessaires uniquement pour les nouveaux projets. Ceux-ci nécessitent moins de fonctionnalités et ne sont pas évolutifs au fil du temps et du projet.

Leur structure de code n'est pas très étendue et n'implique pas de couche d'abstraction plus profonde, car les utilisateurs n'ont besoin de construire que les fonctionnalités principales. Cela élimine le besoin d'utilitaires supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lfaRa-3SmkzcN2cuy3MCYw.png)
_Structure de code_

L'exemple le plus simple est le boilerplate create-react-app de Facebook :

[**facebookincubator/create-react-app**](https://github.com/facebookincubator/create-react-app)  
[_create-react-app - Créez des applications React sans configuration de build._github.com](https://github.com/facebookincubator/create-react-app)

### Quelle est la différence entre un boilerplate et un template ?

Comme [Joachim Pense](https://www.quora.com/profile/Joachim-Pense) l'explique clairement, le **boilerplate** est quelque chose que vous copiez et collez et que vous ajoutez simplement à un document. Il apparaît le plus souvent dans les contrats où le langage est utilisé et réutilisé, détaillant des choses comme les conditions et les mises en garde.

Les écrivains utilisent les **templates comme modèles**, parfois avec des effets négatifs. En termes généraux, un template est un modèle ou un motif utilisé pour créer de nouveaux objets. En écriture, c'est une **forme standardisée de quelque chose comme un CV** que les écrivains peuvent utiliser pour développer leurs propres versions.

Contrairement aux boilerplates, les templates sont adaptés pour un usage particulier. Le problème s'est posé pour moi lorsque les étudiants utilisaient des templates Word pour leurs CV, et ils finissaient tous par se ressembler.

Les templates et les boilerplates peuvent rendre l'écriture commerciale guindée et artificielle s'ils sont utilisés à mauvais escient.

### Guide de style pour l'écriture de code

Quoi qu'il en soit, que vous utilisiez un boilerplate ou non, il existe certaines normes suivies par les entreprises pour l'écriture de code. L'une d'entre elles est le **Guide de style**. Il tente d'expliquer les styles et modèles de base utilisés dans diverses entreprises ou organisations. Il est généralement obligatoire que les employés adoptent le guide de style de codage de leur entreprise.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHZwgapkhk1bMWHilZa6vw.png)

Le Guide de style décrit des tonnes de règles pour l'écriture de code, comme l'indentation des tabulations et des espaces, la nomination des variables et des fonctions, l'écriture de commentaires nécessaires, la mise en forme, les structures de fichiers sources, l'utilisation de méthodes appropriées de structures de données, l'évitement du hoisting, la portée, les instructions de contrôle et bien plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hxP11Dbe9ksYpK5c8_nU3g.png)

Les styles de programmation traitent généralement de l'apparence visuelle du code source dans le but de lisibilité. Des logiciels sont disponibles depuis longtemps pour formater automatiquement le code source, laissant les codeurs se concentrer sur la nomination, la logique et les techniques supérieures.

En tant que point pratique, l'utilisation d'un ordinateur pour formater le code source fait gagner du temps, et il est possible d'appliquer ensuite des normes à l'échelle de l'entreprise sans [débats](https://en.wikipedia.org/wiki/Flaming_(Internet)#Holy_Wars). (Source — Wiki).

Voici quelques débats courants comme : **Tabs v Spaces Holy war**, **choisir le Code IDE parfait**, et ainsi de suite. Le plus intéressant est que vous pouvez participer à ces débats qui se déroulent principalement sur [**Reddit**](https://www.reddit.com/r/programming/comments/2ban9r/the_great_white_space_debate/)**.** Vous pouvez également participer à certaines des Q&A de [**stackoverflow**](https://stackoverflow.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjETUMQ62xAZegCSAglE6Q.png)
_source — [https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/" rel="noopener" target="_blank" title=")_

Pour les développeurs web, le guide de style le plus courant pour JS est le **guide de style javascript d'Airbnb**. Il est open source et tout le monde peut contribuer.

[**airbnb/javascript**](https://github.com/airbnb/javascript)  
[_javascript - Guide de style JavaScript_github.com](https://github.com/airbnb/javascript)

Si quelqu'un doute de la nécessité d'un guide de style pour JavaScript, alors lisez la deuxième réponse de cette question par [Harrison Shoff](https://twitter.com/hshoff), qui est programmeur chez **Airbnb**.

[**Pourquoi JavaScript a-t-il besoin d'un guide de style ? · Question #102 · airbnb/javascript**](https://github.com/airbnb/javascript/issues/102)  
[_L'une de mes parties préférées de la communauté JavaScript est que les gens choisissent de l'écrire de tant de manières différentes_github.com](https://github.com/airbnb/javascript/issues/102)

Voici quelques guides de style pour certains des langages les plus populaires d'aujourd'hui :

[**DotNet Code Formatter**](https://github.com/dotnet/codeformatter)

[**Java : Google-Java-Format**](https://github.com/google/google-java-format)

[**Javascript Standard Style**](https://standardjs.com) **(différent du javascript d'Airbnb)**

[**PHP Coding Standards Fixer**](http://cs.sensiolabs.org)

[**Python : YAPF de Google**](https://github.com/google/yapf/)

[**Ruby : Rubocop**](http://rubocop.readthedocs.io/en/latest/)

#### Plus sur le Boilerplate : Concept pour la POO

Dans les [programmes orientés objet](https://en.wikipedia.org/wiki/Object-oriented_programming), les classes sont souvent fournies avec des méthodes pour [obtenir et définir](https://en.wikipedia.org/wiki/Mutator_method) des variables d'instance. Les définitions de ces méthodes peuvent fréquemment être considérées comme du boilerplate.

Bien que le code variera d'une classe à l'autre, il est suffisamment stéréotypé en structure pour qu'il soit mieux généré automatiquement que écrit à la main.

Par exemple, dans la classe [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) suivante représentant un animal de compagnie, presque tout le code est du boilerplate sauf pour les [déclarations](https://en.wikipedia.org/wiki/Declaration_(computer_science)) de _Pet_, _name_, et _owner_ :

```
public class Pet {    private String name;    private Person owner;
```

```
public Pet(String name, Person owner) {        this.name = name;        this.owner = owner;    }
```

```
public String getName() {        return name;    }
```

```
public void setName(String name) {        this.name = name;    }
```

```
public Person getOwner() {        return owner;    }
```

```
public void setOwner(Person owner) {        this.owner = owner;    }}
```

La définition du boilerplate devient de plus en plus globale dans de nombreux autres langages de programmation de nos jours. Il provient de la POO et des langages hybrides qui étaient autrefois procéduraux mais sont devenus POO. Ils ont maintenant le même objectif de répéter le code que vous construisez avec un modèle/template/classe/objet, donc ils adoptent ce terme. Vous faites un template, et les seules choses que vous faites pour chaque instance d'un template sont les paramètres individuels.

Cette partie est ce que nous appelons le boilerplate. Vous réutilisez simplement le code que vous avez fait en template, mais avec différents paramètres.

#### Boilerplate en tant qu'API

Puisque vous réutilisez simplement le code du template avec différents paramètres, cela implique que nous pourrions construire des API réutilisables qui n'ont besoin que d'un changement d'entrées et de sorties.

### Conclusion

Le « boilerplate code » est tout code apparemment répétitif qui apparaît encore et encore afin d'obtenir un résultat qui semble devoir être beaucoup plus simple.

J'ai écrit cet article parce que j'ai récemment été instruit par un Team Lead d'apprendre les nombreuses variétés de boilerplate qui pourraient convenir à notre projet. J'ai donc dû partir à la recherche du boilerplate parfait.

Tout type de feedback sera apprécié ! Hustle On!