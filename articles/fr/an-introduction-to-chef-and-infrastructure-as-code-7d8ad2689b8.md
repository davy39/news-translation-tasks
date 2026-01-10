---
title: Un guide complet pour les débutants sur Chef et l'infrastructure en tant que
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-01T19:15:24.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-chef-and-infrastructure-as-code-7d8ad2689b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QRU5eVJ3ahrSuyfnf7rlKg.jpeg
tags:
- name: coding
  slug: coding
- name: Devops
  slug: devops
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide complet pour les débutants sur Chef et l'infrastructure en tant
  que code
seo_desc: 'By Mohak Puri

  For the past few weeks, I have been digging a lot into Chef. Although the documentation
  is good, there have been a lot of times when I was stuck with no clue whatsoever.
  So I will be giving an in-depth introduction to Chef. If you haven...'
---

Par Mohak Puri

Depuis quelques semaines, j'ai beaucoup exploré Chef. Bien que la documentation soit bonne, il y a eu de nombreuses fois où j'étais bloqué sans aucun indice. Je vais donc donner une introduction approfondie à Chef. Si vous n'avez jamais entendu parler de Chef (comme moi il y a quelques mois), ne vous inquiétez pas, je vais tout expliquer.

![Image](https://cdn-media-1.freecodecamp.org/images/oQ7inoIArobhPDgvYq0gHbbDAniehpLLB-cH)
_credits: Google_

### Qu'est-ce que Chef et pourquoi l'utiliser ?

> Chef est une plateforme d'automatisation puissante qui transforme l'infrastructure en code. Chef automatise la configuration, le déploiement et la gestion de l'infrastructure sur votre réseau, quelle que soit sa taille.

Mais que signifie l'infrastructure en tant que code ? Supposons que vous avez une application Java qui doit être déployée sur une seule machine. Vous n'avez pas besoin d'automatisation pour cela — vous pouvez le faire manuellement.

Mais que se passe-t-il lorsqu'une seule machine ne peut pas gérer la charge et que vous devez déployer votre application sur 10, 50 ou 100 machines supplémentaires ? C'est là que Chef intervient. Plutôt que de déployer manuellement votre application sur chaque machine, vous pouvez écrire du code qui le fait pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/9K-qK4H21c2G7Ba3WvjV6nc5SZqQqv3hMW7e)
_Chef_

#### Terminologie

1. Workstation — votre machine locale, alias votre ordinateur portable. C'est ici que vous écrivez votre code qui est ensuite **poussé** vers votre serveur Chef.
2. Chef Server — C'est ici que réside tout votre code. Il contient également toutes les informations sur les nœuds.
3. Nœuds, alias Chef Client — Les machines sur lesquelles votre code doit s'exécuter. Vous pouvez utiliser quelque chose comme Vagrant à des fins d'apprentissage et AWS/GCP en production. Vos nœuds **tirent** le dernier code de votre serveur Chef.

#### Bien démarrer avec Chef

Pour commencer, nous devons d'abord installer **ChefDK** sur notre workstation. ChefDK est le kit de développement Chef qui contient tous les outils nécessaires pour commencer à utiliser Chef. Vous pouvez installer ChefDK depuis [ici](https://docs.chef.io/install_dk.html).

Une fois que vous avez installé ChefDK, exécutez la commande suivante :

```
chef generate cookbook testingCheftree testingChef
```

![Image](https://cdn-media-1.freecodecamp.org/images/x7X2-vOKvD7gzPFjueY1cdvPOelCRQhYIJZv)
_Output_

C'est la structure générée par la commande _chef generate cookbook_. Passons en revue chaque fichier pour voir ce qu'ils font.

#### Cookbooks

Un cookbook est l'unité fondamentale de configuration qui vise à atteindre un état souhaité avec l'aide d'autres composants comme les recettes, les modèles, les fichiers, etc. Par défaut, lorsque vous générez un cookbook, vous obtenez uniquement un dossier de recettes. Cependant, vous pouvez créer des dossiers pour les modèles et autres composants si vous prévoyez de les utiliser (nous en parlerons plus tard).

Supposons que vous souhaitez exécuter une application Java sur une machine. Deux choses sont nécessaires pour cela :

1. Votre machine doit avoir Java installé.
2. Elle doit avoir l'application à exécuter.

Ensuite, vous pouvez exécuter l'application.

Vous créez donc un cookbook qui, lorsqu'il est exécuté sur un nœud, installe Java sur ce nœud, récupère l'application que vous devez exécuter et exécute cette application.

#### Ressources Chef

Une ressource est un bloc Ruby avec quatre composants : un type, un nom, une (ou plusieurs) propriétés (avec des valeurs) et une (ou plusieurs) actions. La syntaxe pour une ressource est la suivante :

```
type 'name' do   attribute 'value'   action :type_of_actionend
```

Supposons que vous souhaitez installer OpenJDK 7 sur votre nœud. Pour ce faire, vous pouvez utiliser la ressource _package_ disponible dans Chef.

```
package 'java-1.7.0-openjdk' do action :installend
```

L'action _action :install_ est l'action par défaut pour la ressource package, vous pouvez donc l'omettre si vous le souhaitez.

```
package 'java-1.7.0-openjdk'
```

Pour exécuter un cronJob sur votre nœud, vous pouvez utiliser la ressource _cron_.

```
cron 'reporting' do  action :create  minute '0'  hour '0'  weekday '1'  command "/srv/app/scripts/daily_report" # Chemin du script à exécuterend
```

Selon ce que vous souhaitez accomplir, il existe de nombreuses ressources Chef intégrées que vous pouvez utiliser. Vous pouvez en lire plus à ce sujet [ici](https://docs.chef.io/resource_reference.html).

#### Recettes

Une recette est une collection de ressources qui tend à rapprocher votre nœud d'un état souhaité. Les recettes sont écrites en Ruby.

Pour exécuter une recette, nous utilisons la commande suivante :

```
chef-client -z pathToRecipe
```

Le drapeau `-z` implique que le chef-client doit s'exécuter en mode local puisque nous ne sommes pas connectés à un serveur chef. Si vos nœuds sont connectés au serveur, vous n'avez pas besoin d'utiliser le drapeau `-z`.

```
************************** default.rb ****************************
```

```
/* Il s'agit d'une recette d'exemple pour installer httpd (programme serveur Apache HyperText Transfer Protocol (HTTP)), crée un fichier sur le nœud à /var/www/html/index.html (chemin par défaut pour servir des pages web sur un serveur apache) et démarre le service sur une machine basée sur centOS */
```

```
package 'httpd'
```

```
file '/var/www/html/index.html' do  content '<html>This is a placeholder for the home page.<;/html>'end
```

```
service 'httpd' do  action [:enable, :start]end
```

#### Métadonnées et Berksfile

Lorsque vous travaillez sur un cookbook, vous n'avez pas besoin de commencer depuis la toute première étape, car il est probable que quelqu'un ait déjà construit quelque chose de similaire et que vous puissiez simplement étendre leur travail.

C'est là que le [Chef Supermarket](https://supermarket.chef.io/) intervient. Il contient des cookbooks communautaires que vous pouvez utiliser comme _dépendances_ dans votre propre cookbook. Ces dépendances sont listées dans le fichier metadata.rb ou même dans votre Berksfile. Mais alors la question se pose : comment sont-ils différents ?

```
************************* Berksfile ********************************source 'https://supermarket.chef.io' # Récupérer les dépendances depuis ici
```

```
metadata
```

Lorsque vous téléchargez votre cookbook sur le serveur chef, vous devez également télécharger les dépendances de votre cookbook. C'est là que Berks aide. Vous devez simplement exécuter deux commandes simples :

```
berks install berks upload
```

qui téléchargent toutes les dépendances de vos cookbooks et les téléchargent toutes sur le serveur chef. Les cookbooks de dépendance sont présents à

```
~/.berkshelf/cookbooks/
```

Au cas où vous auriez mis à jour votre cookbook et souhaitez le re-télécharger sur le serveur chef, vous devez alors mettre à jour la version dans le fichier de métadonnées. Sinon, lorsque vous utilisez la commande _berks upload_, la nouvelle recette ne sera pas téléchargée sauf si vous forcez un téléchargement.

```
**************************** metadata.rb ***************************name 'testingChef'maintainer 'The Authors'maintainer_email 'you@example.com'license 'All Rights Reserved'description 'Installs/Configures testingChef'long_description 'Installs/Configures testingChef'version '0.1.0' # Mettre à jour après les modifications apportées au cookbookchef_version '>= 12.14' if respond_to?(:chef_version)
```

```
depends 'haproxy', '~> 6.2.6'
```

#### Chefignore

Placez les fichiers/répertoires qui doivent être ignorés dans ce fichier lors du téléchargement 
ou du partage de cookbooks sur le site communautaire.

#### Ohai

Lorsque nous installons ChefDK, nous obtenons également ohai avec lui. Chaque fois que vous exécutez chef-client sur votre nœud, chef exécute ohai avant cela. Ohai collecte beaucoup d'informations système. Les types d'attributs que Ohai collecte incluent, mais ne sont pas limités à :

* Système d'exploitation
* Réseau
* Mémoire
* Disque
* CPU

Lorsque vous exécutez ohai, vous obtenez beaucoup de sortie, alors soyez attentif à ce que vous voulez et écrivez vos commandes en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/jQ0fmMqFKw0pvKIPMyDjeQokBu-3cdZBkOpp)
_Exécution explicite de ohai_

![Image](https://cdn-media-1.freecodecamp.org/images/wlf3dkk7zxpgvjw3eRk9kyclvHymsImFvLI7)
_Obtention d'informations sur l'hôte à partir de ohai_

![Image](https://cdn-media-1.freecodecamp.org/images/V2hW5WBSjMbJGNAoNje9x9VUl0eCX9tIUZc3)
_Obtention d'informations liées au CPU à partir de ohai_

Maintenant, si nous le souhaitons, nous pouvons utiliser toutes ces informations dans nos recettes. Tout ce que nous avons à faire est de nous référer à une propriété particulière du nœud.

```
if node['hostname'] == "Some hostname" do  // faire quelque chose seulement si le nom d'hôte du nœud correspondend
```

**Knife**

Knife est un outil que vous utilisez pour communiquer avec le serveur chef. Si vous voulez savoir quoi que ce soit sur vos nœuds ou si vous voulez mettre à jour quoi que ce soit comme leurs recettes, knife est la solution. Il existe plus d'une douzaine de commandes knife. En voici quelques-unes

1. **knife bootstrap** — Cette commande est utilisée pour créer un nouveau nœud et l'attacher à votre serveur chef. Lors du bootstrapping d'un nœud, chef installe tout comme ohai, chef-client sur le nœud et il exécute également chef-client automatiquement. Pour toute modification ultérieure apportée à ce nœud, vous devez exécuter chef-client manuellement pour mettre à jour votre nœud.
2. **knife node show ${nodeName}** — Cette commande est utilisée pour obtenir des informations sur votre nœud qui incluent les recettes, l'environnement, la plateforme, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/kpeCW0f54ohVZbv9jWt-kUe3laGTQ0P83txP)
_Obtention d'informations sur votre nœud à l'aide de Knife_

3. **knife cookbook list ${nodeName}** — Cette commande est utilisée pour obtenir tous les cookbooks associés à votre nœud

![Image](https://cdn-media-1.freecodecamp.org/images/2LofigMRsrGKLX-VRs3hiz8AQH7JKfzke2EN)

C'est à peu près tout ! Merci d'avoir lu, et j'espère que vous avez apprécié l'article.

Vous pouvez me suivre sur [Medium](https://medium.com/@mohak1712) et [Github](https://github.com/mohak1712) :)