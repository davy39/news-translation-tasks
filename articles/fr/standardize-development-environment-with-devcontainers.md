---
title: Comment standardiser votre environnement de développement avec devcontainer.json
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-04T14:45:34.000Z'
originalURL: https://freecodecamp.org/news/standardize-development-environment-with-devcontainers
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/image--9-.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Comment standardiser votre environnement de développement avec devcontainer.json
seo_desc: "By Hrittik Roy\nModern software development workflows are complicated,\
  \ involving many tools and dependencies. \nWhen working in a team, it's not uncommon\
  \ to use several different software programs, each with its own dependencies. This\
  \ can quickly becom..."
---

Par Hrittik Roy

Les flux de travail modernes de développement logiciel sont complexes, impliquant de nombreux outils et dépendances. 

Lorsqu'on travaille en équipe, il n'est pas rare d'utiliser plusieurs programmes différents, chacun avec ses propres dépendances. Cela peut rapidement devenir confus, chaque logiciel nécessitant des configurations et une gestion différentes. 

Une solution consiste à utiliser des environnements virtuels pour isoler les dépendances. Cela peut encore nécessiter d'installer et de gérer l'installation et la configuration. 

Mais il existe une autre option meilleure : tout empaqueter – y compris la base de données et la version du langage de codage – dans un seul conteneur que vous pouvez utiliser chaque fois que vous en avez besoin. En fait, la plupart des entreprises déploient leur logique et leurs applications dans des conteneurs de production.

Pour le développement, vous pouvez utiliser un conteneur Docker comme environnement de développement complet. Il est similaire à votre environnement de production, mais avec tous les compilateurs, débogueurs, outils de construction, SDK, outils de productivité, et autres. Ce serait votre conteneur de développement ou dev container.

Ici, `devcontainer.json` intervient comme la norme qui rationalise et standardise votre environnement de développement. Il vous permet de vous concentrer sur la livraison des changements plutôt que de vous soucier des dépendances et des installations. 

Dans ce tutoriel, vous apprendrez à propos de la norme devcontainer.json, son but, comment la configurer et comment l'adopter pour un usage personnel ou professionnel. Cela vous aidera à augmenter votre productivité en tant qu'ingénieur.

## Qu'est-ce qu'un Dev Container ?

Les dev containers, également connus sous le nom de conteneurs de développement, fournissent un environnement de développement complet empaqueté dans un conteneur qui peut être facilement accessible via votre IDE préféré via Secured Shell (SSH). Cette configuration élimine tous les obstacles qui entravent votre flux de travail, allant des performances faibles à la faible bande passante.

Votre conteneur peut fonctionner sur diverses infrastructures, y compris des clouds privés et publics, des clusters ou des machines locales, et vous pouvez exploiter le matériel qui serait difficile à reproduire par vous-même.

L'aspect isolation garantit également que vos dépendances ne se chevauchent pas et ne perturbent pas votre environnement local. Toute la configuration du conteneur est stockée dans un fichier standard `.devcontainer.json`, de Microsoft, qui sert d'instructions d'empaquetage pour votre environnement. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-2.png)
_Structure du Dev Container. De : [containers.dev](https://containers.dev/overview)_

Le fichier utilise un format de métadonnées JSON structuré avec commentaires (jsonc) que vous pouvez adapter à vos besoins spécifiques. Par exemple, vous pouvez ajouter des outils de développement comme git, un débogueur, et d'autres configurations comme diverses extensions.

### Où pouvez-vous l'utiliser ? 

La configuration la plus simple peut être de créer un environnement de conteneur de base avec un langage pour expérimenter différentes fonctionnalités. Par exemple, si vous souhaitez tester une nouvelle édition d'un langage de programmation, vous pouvez utiliser l'image de base de ce langage particulier et générer un nouvel environnement de développement avec facilité.

Il existe également quelques cas d'utilisation pour des configurations compliquées. Par exemple, l'une des tâches les plus difficiles est souvent de créer et de configurer une base de données pour qu'elle fonctionne de manière transparente avec votre projet tout en configurant votre environnement de développement.

En créant un fichier Docker compose, vous pouvez facilement configurer la création de la base de données et exposer des variables d'environnement pour créer un environnement autonome. Ces configurations multi-conteneurs orchestrés (avec à la fois la base de données et le langage de programmation) sont installées dans une relation parent-enfant et peuvent servir des cas d'utilisation complexes.

Regardez la configuration ci-dessous comme exemple qui utilise Compose pour connecter l'espace de construction :

```json
{
"name": "Python 3 & PostgreSQL",
"dockerComposeFile": "docker-compose.yml",
"service": "app",
"workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}"
}
```

Dans cet exemple, votre Dev Container utilise un fichier Docker Compose et référence les instructions pour construire un espace de travail intégré Python et PostgreSQL. La structure peut aider à développer des applications CRUD sans essayer de configurer votre base de données et votre configuration système pour la supporter sur chaque développeur.

## Les problèmes que les Dev Containers résolvent

Maintenant, avec des fonctionnalités comme celles-ci, les dev containers gagnent en popularité dans les contextes personnels et professionnels car ils offrent la reproductibilité et l'isolation. Examinons tous les avantages :

### Résolution des problèmes de configuration de l'installation

Maintenir et gérer des environnements locaux peut être beaucoup de travail. Cela implique souvent l'utilisation de divers outils et configurations, rendant le processus fastidieux. Avoir quelque chose qui standardise ce processus peut faire gagner beaucoup de temps.

### Standardisation des instructions de construction du projet

Écrire de la documentation pour les mises à jour et les changements de dépendances peut être difficile. Une meilleure approche serait d'utiliser du code pour simplifier le processus, permettant à chacun de livrer sans être ralentis par la documentation ou "ça marche sur ma machine".

### Assurer l'isolation des environnements de développement

Un développeur logiciel peut travailler simultanément sur différents projets avec de nombreuses parties mobiles. Et si vous pouvez isoler les environnements, empêchant les conflits avec d'autres logiciels sur le système hôte et fournissant un environnement propre et contrôlé pour le développement ? C'est maintenant possible :)

### Permettre la cohérence entre les équipes de développement

Atteindre la portabilité entre plusieurs équipes et individus est compliqué avec des technologies et configurations variées. Un environnement de développement standardisé peut garantir que tous les membres de l'équipe ont une configuration uniforme tout en réduisant les incohérences causées par les variations individuelles des machines.

### Simplifier les processus d'intégration et de formation

Apprendre de nouvelles choses est important, mais peut être difficile. Alors, quelle meilleure façon d'apprendre qu'en pratiquant un nouveau langage ou framework ? Lancer des environnements rapidement en isolation peut aider à garder les machines propres. 

Cela est particulièrement vrai lors de la présentation de conférences ou de l'exécution d'ateliers. En commençant avec une ardoise propre, tout le monde peut suivre sans être ralenti par des outils manquants ou une confusion à mi-parcours.

## Comment créer votre premier Devcontainer

Maintenant que vous connaissez tous les avantages, je vais vous aider à créer votre premier conteneur de développement. Comme il s'agit d'un tutoriel d'introduction, vous apprendrez à le faire pour un environnement Go de base.

Une fois que vous aurez compris les bases, vous pourrez étendre votre configuration pour inclure des configurations plus complexes impliquant des bases de données, des outils de développement supplémentaires et des personnalisations. Commençons par en créer un !

### Prérequis 

Voici les prérequis pour créer le modèle : 

1. Outils pour exécuter Dev Container : [Docker](https://www.docker.com/) ou tout autre moteur de conteneur
2. Outils pour créer des modèles et se connecter à Dev Container : [Visual Studio Code](https://code.visualstudio.com/)
3. Outils pour gérer la connexion et la logique de création : [Extension Visual Studio Code Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Note : Après avoir créé le modèle, vous pouvez passer à votre IDE préféré avec différents backends, comme nous le verrons dans les sections à venir. Considérez simplement le fichier `.devcontainer.json` comme une source de vérité pour l'environnement et qui peut être facilement partagé.

### Comment construire un simple dev container

Vous pouvez soit créer le dev container à partir de zéro, soit utiliser l'utilitaire VSCode. Commencer avec l'utilitaire est simple. Pour configurer votre dev container, utilisez simplement l'option `Dev Containers: Add Dev Container Configuration Files…` depuis la Palette de Commandes `(Ctrl+Shift+P)` :

![Image](https://lh3.googleusercontent.com/KcLU2UhZfNoxHiKs9wdUBeEVrJGvOviHYrNXlWgqdSq8D1afGSzr_TCnrmwsuTgH4Zm58e_MomNp3i_4LRKnxC6ppJ4v-p2A_mvokmVnk1JSJg_f7hsuZY9cTpn-UjY2gHjdWxA696Fy-bgFnlWheOg)
_Configuration d'exemple pour les Dev Containers depuis la Palette de Commandes VSCode_

Maintenant, passons à l'étape suivante, qui consiste à sélectionner l'image de base. Vous pouvez choisir n'importe quelle image de base que vous souhaitez. Dans ce cas, nous utilisons l'image de base Go.

![Image](https://lh5.googleusercontent.com/sgFvvnhlbN_nt8eQpk19ZGlWxZ5Dk3TK-nAXAZAdGw314fHKKEz5RkG8WXyxCKRO5x9VHyjtuyNH_-q7Vev2Ue4bszdKm8uACtAnFPFDPZmJiM0zMYZAQazLzvJJaRN4u1A8ItAnwODEOYwaCwjONa4)
_Configuration de base du Dev Container_

Cependant, il peut y avoir de nombreuses versions de Go – donc l'étape suivante consiste à choisir celle que vous voulez. La dernière version disponible est `1.21`, donc je recommande d'utiliser celle-ci. Mais si vous préférez, vous pouvez également construire une image à partir de zéro ou même sélectionner parmi des versions plus anciennes.

Faites simplement défiler et choisissez.

![Image](https://lh5.googleusercontent.com/Hkg2vqYKxnuBn6A31LrVvETkND4_S0JUsIHqStVzZaKZz-1LtVnKZEAAdtA_BfX2CvHIW6e9-P8PPQObb3B1b2C3SrYjmSWw_st8Wm2ihbuU0efRfHMLy9ynjbnaulrY0aEsNAHw1Fb21NS_lhKzEWk)
_Version du fichier de configuration de base sélectionné_

L'étape suivante consiste à importer des "Fonctionnalités", qui sont des unités autonomes de code d'installation qui aident à induire des outils ou des conteneurs spécifiques dans votre configuration de dev container. Ces fonctionnalités peuvent aller de nouveaux outils à des personnalisations spécifiques que vous pouvez découvrir [ici](https://containers.dev/features). 

Mais pour un environnement Go simple et basique, nous allons sauter cette étape.

![Image](https://lh4.googleusercontent.com/YXO8ZA_kH95z7OMTkrYmLz8VMenqCdlyUFpDl2uoRfJdrtvSLFtH-QouD1gToeLrye8MDRFGzGDaQy3yhXujAiC43LKb-TvctMmxWbLqaSwde2U-XlVSdYgexohqkp5Ho_ft7UgkqkPBvvrDx6eN8Fg)
_Fonctionnalités complémentaires qui peuvent booster votre espace de travail_

Cliquez sur `Ok` pour générer un fichier `.devcontainer.json` Go basique dans le répertoire `.devcontainer` : 

```bash
~/Code/devcontainer-new main +4 !4 \u276f tree -a
.
\u251c\u2500\u2500 .devcontainer
\u2502   \u2514\u2500\u2500 devcontainer.json
```

Félicitations ! Vous avez maintenant un environnement qui est isolé et peut être partagé avec n'importe qui. 

### Comment utiliser VSCode pour la configuration du dev container

Pour exécuter cette configuration, vous pouvez cliquer sur `Reopen in Container` comme méthode la plus simple comme vu ci-dessous :

![Image](https://lh5.googleusercontent.com/Ndj5FXh3EE09Ab_srEQH7lSQ35yDfQwLWBeJPQQMmx_JDZPVnQOZsCH-jZdTJ_ZXOfTRyc95fzhBPmPSZefUs7O3pT19xi3-FRcxlvtSBsMx5JHNN3hR6jCwPHAz_2BTr-oTzqjp9E4YvHiRAehVlUg)
_Un exemple de fichier Dev Container avec Go 1.21_

L'extension va récupérer l'image "_mcr.microsoft.com/devcontainers/go:1-1.21-bullseye_" puis créer un serveur SSH dedans. 

![Image](https://lh5.googleusercontent.com/NKkI-1yuc-HjQ53zmc2EfxT4zPbjSRf9r7uXSt3IVm2w7WeCLT5v9wwUJPdzIPO_0VT4tluONMOJowZeeQCa2iEZudAPJ_e2H9rchPVfFI5LkspnfT4uTAhU2LwcAangC1EXF0ff1mli5c4nYQyFMYk)
_Démarrage du Dev Container_

Après avoir construit avec succès la version Go, vous pouvez vous connecter en toute confiance à l'environnement et exécuter vos opérations. Vous verrez que la version Go est la même que celle que vous avez construite et que la connexion provient de votre Dev Container, ce qui rend la connexion réussie : 

![Image](https://lh4.googleusercontent.com/wbxcN6fkTVxkVkn0UftnN2IsdZK79NJ32vSiLTCSlcJrX2woQjZvSjiIYl1Ynoxuil1GDPZ7SZkxYrjzEYWYCZG-Wcq6rEt7rbtB0oJujz8IZJcc5WwYYhGEZtZsXJz4gNEeJVFV8bx0MRKfzE5DP7g)
_Dev Container en cours d'exécution localement_

### Dev Container CLI 

[Devcontainers CLI](https://github.com/devcontainers/cli) est une interface de ligne de commande qui vous aide à exécuter, construire et lancer le conteneur à partir de votre configuration devcontainer.  

Avec l'aide de cet outil, vous pouvez configurer un environnement sans utiliser VSCode et vous y connecter manuellement via SSH, vous offrant plus de liberté.

Bien que l'outil soit intéressant, de nombreuses fonctionnalités n'ont pas encore été lancées comme listé ici : 

![Image](https://lh4.googleusercontent.com/YT7slbodThp_21lmmxyzafvWP7atDEn_6lrGTotxdWsF9idTfob0nnu_517dLHizjv9tEeehkzASWF1pPrQehYPf05tSDNDZONUajVhsEGsV93vofapIhZFG9V-v3afR1Qb6Oa-Axk8ZZk6wC1CErx0)
_Feature Roadmap_

## Comment utiliser les Dev Containers à leur plein potentiel 

Une fois que vous distribuez le `devcontainer.json` à vos coéquipiers, ils peuvent facilement l'utiliser pour lancer des environnements locaux avec les avantages discutés. Mais que faire si vous devez les aider à lancer l'environnement sur le Cloud pour exploiter son matériel puissant ?

Il existe quelques options qui peuvent vous aider. La première est [GitHub Codespaces](https://github.com/codespaces), qui vous aide à lancer sur une infrastructure gérée par GitHub sur Azure. 

Mais il peut y avoir une exigence d'utiliser du matériel dédié depuis votre cluster Kubernetes, ou un cloud privé ou public. Comment faire ? Vous pouvez utiliser des outils open source côté client comme [DevPod](https://devpod.sh/), qui vous aide à déployer sur l'infrastructure souhaitée.

![Image](https://lh5.googleusercontent.com/_nKg6h4V7em9ZORxwFUVuWpgWxAmRLSfv2lWWm6JpSoJBDXDw56bjNfBhmxWtnpb8kGAgbvkZTn4kOo4oouV2vU7ypm-m5H1H9OROlaWESPtJ4SskfXwxSz3n9rO0LA7DgU98EvKaJ0H0CZ4wooSPww)
_Interface utilisateur de DevPod_

Actuellement, l'outil a plus de [4.4k étoiles](https://www.freecodecamp.org/news/p/43b21e57-00ca-4850-9a0f-95ebce575227/(%E2%80%8B%E2%80%8Bhttps://github.com/loft-sh/devpod) et se développe rapidement avec plus d'adhésions chaque jour avec une devise de `_Donner le pouvoir à l'utilisateur. N'importe quelle infra, n'importe quel IDE, et sans opinion_` :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-4.png)
_Historique de croissance GitHub - DevPod_

L'outil est sans opinion, ce qui signifie que vous pouvez l'utiliser de manière transparente sur diverses infrastructures, IDE et langages de programmation. 

Par exemple, si vous voulez un backend spécifique sur un fournisseur de cloud, vous pouvez le faire avec des fournisseurs déjà disponibles, ou vous pouvez [créer le vôtre comme les 7 fournisseurs communautaires](https://devpod.sh/docs/developing-providers/quickstart) :

![Image](https://lh3.googleusercontent.com/4WvTAJUH_qOmcuGSyDQnGKf4ZDpjQ7um2SwhUAfhaFTPSK5SMwUY0TV1JuSrYXKyyUl7fQvOONHbem1puJ6ohxYn2n_1tCnrHobieQRjlkZ_FupqBobTnD8s3z0nPaVuh2CWsWHygqO27Aatas25R_c)
_Fournisseurs DevPod_

L'outil permet également un environnement de développement cohérent qui peut être utilisé de manière répétée où vous le souhaitez et connecté à n'importe quel éditeur de code/IDE allant de JetBrains, Jupyter, ou VSCode. 

## Comment lancer votre environnement de développement en utilisant DevPod

Cet outil offre à la fois une version desktop et CLI, vous pouvez donc utiliser celle qui vous convient le mieux. Lorsque vous utilisez DevPod Desktop pour créer un environnement, le processus est le suivant :

Étape 1 : Installez DevPod à partir des [instructions officielles](https://devpod.sh/docs/getting-started/install). 

Étape 2 : Ajoutez un fournisseur via 'Providers' > '+ Add'. Sélectionnez un fournisseur et cliquez sur 'Continue'.

![Image](https://lh4.googleusercontent.com/CfrbpPmbH6X4H3SWDLVbc0ujGBakXbGKIauhv-YJ7nNQY6ISnhpU9cJqDzVjR6ylwBvaQ88bbUQSLMKaDG1KKu1B9Ezz_1-nUiZ6fGfqDRuy4X0ju9NTK_gbZvwUgdF3GUEJBgz6pdbiKx9lXzOxfuk)
_Fournisseur AWS DevPod_

Étape 3 : `Enter Workspace Source` avec votre chemin `devcontainer.json` qui peut être un dépôt distant ou local ou l'exemple :

![Image](https://lh4.googleusercontent.com/B-ovwU1mYLxJu5_ANnbP_-dHKUOgMBa4hFiHUt2QEt6suJYGKV-I5M2YJ5wX714AFYNhzib0UOsMesL1t0XJzoordevJ4En91iVpDDzNcIRcHZrsme7qWwB7BzemNzMyPzppy6I0iRGlOn-9YY8ZYgI)
_Sélection de l'IDE et du fournisseur_

Étape 4 : Sélectionnez votre IDE par défaut et cliquez sur `Create Workspace` :

![Image](https://lh3.googleusercontent.com/-etuLcx-G3VOHAwbNoPdcO9PWPiNu-KF3Z6NR0qq3vji5o7FCeDoJqywprmKo7yOmAlv4FV-JrRbopfXEjmK_CqyF0EmPT1zo8xZkfGmj7b0wz-chmyZgACh7Tz2qLxe1TJ2lcs6FJ1wAV0Jpih976s)
_Créer un espace de travail_

Maintenant, vous pouvez construire et configurer votre application sur votre instance en cours d'exécution :

![Image](https://lh3.googleusercontent.com/FWJpNnACbxTFA3BDD162oIploPPdBUQgYuaNu6dvoqAJEadvdUf5Ep5v_dMBEShFfj6lll085xLxVPpH-bte5tHLX8q2av42JDol9K_i3fnel5LuNR8GVYqHocHIsfFOMtPs1td_XvcWQJksiycanNA)
_Dev Container en cours d'exécution sur votre machine locale_

Félicitations ! Vous avez configuré avec succès votre premier Dev Container \ud83c\udf89

Si vous vous sentez aventureux et souhaitez explorer la CLI, vous pouvez en savoir plus sur son utilisation [ici](https://devpod.sh/docs/developing-in-workspaces/connect-to-a-workspace).

## Réflexions finales

Les normes comme les dev containers vous aident à améliorer votre productivité et votre écosystème de développement global. Cela réduit les coûts pour les entreprises car le matériel le plus récent peut être provisionné sans nécessiter que toute l'équipe mette à niveau leurs machines locales tous les deux ans.

Cela vous aide également à intégrer sans effort de nouveaux membres d'équipe et à maintenir une expérience utilisateur cohérente. 

Les outils de conteneurs de développement comme DevPod peuvent améliorer la sécurité et la personnalisation pour répondre à divers besoins sur toute infrastructure que vous souhaitez tout en maintenant une expérience [DevEx](https://loft.sh/blog/why-every-software-team-should-have-a-developer-experience-owner-dxo/) cohérente. Cela permet une construction et des tests plus rapides en utilisant le matériel le plus récent et remplace le temps d'intégration par du temps de codage.

Vous pouvez rejoindre le [Slack](https://slack.loft.sh/) de DevPod pour en savoir plus.