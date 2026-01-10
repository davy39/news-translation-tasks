---
title: Qu'est-ce que les modules Terraform et comment fonctionnent-ils ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-09T00:18:25.000Z'
originalURL: https://freecodecamp.org/news/terraform-modules-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/tf-modules.jpeg
tags:
- name: Devops
  slug: devops
- name: Terraform
  slug: terraform
seo_title: Qu'est-ce que les modules Terraform et comment fonctionnent-ils ?
seo_desc: 'By Serhii Vasylenko

  Surprisingly, a lot of beginners skip over Terraform modules for the sake of simplicity,
  or so they think.

  Later, they find themselves going through hundreds of lines of configuration code.

  I assume you already know some of the ba...'
---

Par Serhii Vasylenko

Étonnamment, beaucoup de débutants ignorent les modules Terraform pour des raisons de simplicité, ou du moins le pensent-ils.

Plus tard, ils se retrouvent à parcourir des centaines de lignes de code de configuration.

Je suppose que vous connaissez déjà quelques bases sur Terraform et que vous l'avez même essayé auparavant. Si ce n'est pas le cas, consultez cet [aperçu sur Terraform](https://serhii.vasylenko.info/2020/05/02/Terraform-explained-for-managers.html) et ce [tutoriel vidéo](https://www.freecodecamp.org/news/how-to-use-terraform-to-automate-your-aws-cloud-infrastructure-tutorial/) avant de continuer votre lecture.

Veuillez noter : Je n'utilise pas intentionnellement d'exemples de code réels avec un fournisseur spécifique comme AWS ou Google, simplement pour des raisons de simplicité.

## Modules Terraform

### Vous écrivez déjà des modules

Même lorsque vous ne créez pas intentionnellement un module, si vous utilisez Terraform, vous écrivez déjà un module – un module dit "racine".

Tout fichier de configuration Terraform (`.tf`) dans un répertoire, même un seul, forme un module.

### Que fait un module ?

Un module Terraform vous permet de créer une abstraction logique au-dessus d'un ensemble de ressources. En d'autres termes, un module vous permet de regrouper des ressources ensemble et de réutiliser ce groupe plus tard, éventuellement plusieurs fois.

Supposons que nous avons un serveur virtuel avec certaines fonctionnalités hébergées dans le cloud. Quel ensemble de ressources pourrait décrire ce serveur ? Par exemple :

* la machine virtuelle elle-même, créée à partir d'une image
* un périphérique de bloc attaché d'une taille spécifiée pour un stockage supplémentaire
* une IP publique statique mappée à l'interface réseau virtuelle du serveur
* un ensemble de règles de pare-feu à attacher au serveur
* d'autres choses comme un autre périphérique de bloc, une interface réseau supplémentaire, etc.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-10.png)

Maintenant, supposons que vous devez créer ce serveur avec un ensemble de ressources plusieurs fois. C'est là que les modules sont vraiment utiles – vous ne voulez pas répéter le même code de configuration encore et encore, n'est-ce pas ?

Voici un exemple qui illustre comment notre module "server" pourrait être appelé. "Appeler un module" signifie l'utiliser dans le fichier de configuration.

Ici, nous créons 5 instances du "server" en utilisant un seul ensemble de configurations (dans le module) :

```hcl
module "server" {
    
    count         = 5
    
    source        = "./module_server"
    some_variable = some_value
}
```

### Organisation des modules : enfant et racine

Bien sûr, vous voudrez probablement créer plus d'un module. Voici quelques exemples courants :

* un réseau comme un cloud privé virtuel (VPC)
* l'hébergement de contenu statique (c'est-à-dire des buckets)
* un équilibreur de charge et ses ressources associées
* une configuration de journalisation
* ou toute autre chose que vous considérez comme un composant logique distinct de l'infrastructure

Disons que nous avons deux modules différents : un module "server" et un module "network". Le module appelé "network" est celui où nous définissons et configurons notre réseau virtuel et y plaçons des serveurs :

```
module "server" {
    source        = "./module_server"
    some_variable = some_value
}

module "network" {  
    source              = "./module_network"
    some_other_variable = some_other_value
}
```

Une fois que nous avons quelques modules personnalisés, nous pouvons nous référer à eux comme des modules "enfants". Et le fichier de configuration où nous appelons les modules enfants se rapporte au module racine.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-11.png)

Un module enfant peut être sourcé à partir de plusieurs endroits :

* chemins locaux
* le registre officiel Terraform – si vous êtes familier avec d'autres registres comme le Docker Registry, vous comprenez déjà l'idée
* un dépôt Git (personnalisé ou GitHub/BitBucket)
* une URL HTTP vers une archive .zip contenant le module

Mais comment pouvez-vous transmettre les détails des ressources entre les modules ?

Dans notre exemple, les serveurs doivent être créés dans un réseau. Alors, comment pouvons-nous dire au module "server" de créer des VM dans un réseau qui a été créé dans un module appelé "network" ?

C'est là que l'**encapsulation** entre en jeu.

## Encapsulation des modules

L'encapsulation dans Terraform se compose de deux concepts de base : la portée du module et l'exposition explicite des ressources.

### Portée du module

Toutes les instances de ressources, les noms et, par conséquent, la visibilité des ressources, sont isolés dans la portée d'un module. Par exemple, le module "A" ne peut pas voir et ne connaît pas les ressources du module "B" par défaut.

La visibilité des ressources, parfois appelée isolation des ressources, garantit que les ressources auront des noms uniques dans l'espace de noms d'un module. Par exemple, avec nos 5 instances du module "server" :

```
module.server[0].resource_type.resource_name
module.server[1].resource_type.resource_name
module.server[2].resource_type.resource_name
...
```

D'autre part, nous pourrions créer deux instances du même module avec des noms différents :

```
module "server-alpha" {    
    source        = "./module_server"
    some_variable = some_value
}
module "server-beta" {
    source        = "./module_server"
    some_variable = some_value
}
```

Dans ce cas, la dénomination ou l'adresse des ressources serait la suivante :

```
module.server-alpha.resource_type.resource_name

module.server-beta.resource_type.resource_name
```

### Exposition explicite des ressources

Si vous souhaitez accéder à certains détails des ressources dans un autre module, vous devrez configurer cela explicitement.

Par défaut, notre module "server" ne connaît pas le réseau qui a été créé dans le module "network".

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-08-24-0025-13.png)

Nous devons donc déclarer une valeur de `output` dans le module "network" pour exporter sa ressource, ou un attribut de la ressource, vers d'autres modules.

Le module "server" doit déclarer une `variable` pour être utilisée plus tard comme entrée :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Untitled-2020-09-01-2021-4.png)
*Les noms `output` et `variable` peuvent différer, mais je suggère d'utiliser les mêmes noms pour plus de clarté.*

Cette déclaration explicite de la sortie est le moyen d'exposer une ressource (ou des informations à son sujet) à l'extérieur — à la portée du module 'racine', et donc de la rendre disponible pour d'autres modules.

Ensuite, lorsque nous appelons le module enfant "server" dans le module racine, nous devons assigner la sortie du module "network" à la variable du module "server" :

```
network_id = module.network.network_id
```

Voici à quoi ressemblera le code final pour appeler nos modules enfants :

```
module "server" {
    count         = 5
    source        = "./module_server"
    some_variable = some_value
    network_id    = module.network.network_id
}

module "network" {  
    source              = "./module_network"
    some_other_variable = some_other_value
}
```

Cette configuration d'exemple créerait 5 instances du même serveur, avec toutes les ressources nécessaires, dans le réseau que nous avons créé en tant que module séparé.

## Conclusion

Maintenant, vous devriez comprendre ce que sont les modules et ce qu'ils font.

Si vous êtes au début de votre parcours avec Terraform, voici quelques suggestions pour les prochaines étapes.

Je vous encourage à suivre ce court tutoriel de HashiCorp, les créateurs de Terraform, sur les modules : "[Organiser la configuration](https://learn.hashicorp.com/collections/terraform/modules)".

De plus, il existe un excellent guide d'étude complet qui couvre tout, des concepts de débutant aux concepts avancés sur Terraform : "[Guide d'étude - Certification Terraform Associate](https://learn.hashicorp.com/tutorials/terraform/associate-study?in=terraform/certification)".

La structure de code modulaire rend votre configuration plus flexible et pourtant facile à comprendre par les autres. Ce dernier point est particulièrement utile pour une équipe.

Si vous avez aimé l'article, suivez-moi sur Twitter ([@vasylenko](https://twitter.com/vasylenko)) où je partage occasionnellement mes découvertes et conseils sur Terraform, AWS, Ansible et d'autres technologies liées au DevOps.