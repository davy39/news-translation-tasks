---
title: 'Comment automatiser les configurations spécifiques aux branches de Netlify
  avec un script Bash : Un guide étape par étape'
subtitle: ''
author: Francis Ihejirika
co_authors: []
series: null
date: '2024-12-16T17:51:07.621Z'
originalURL: https://freecodecamp.org/news/how-to-automate-branch-specific-netlify-configurations-with-a-bash-script
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733871988108/cde4ea9b-705c-40e0-9730-09dbeebdfbae.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Netlify
  slug: netlify
- name: Web Development
  slug: web-development
- name: automation
  slug: automation
- name: Bash
  slug: bash
seo_title: 'Comment automatiser les configurations spécifiques aux branches de Netlify
  avec un script Bash : Un guide étape par étape'
seo_desc: 'When you’re working on a project with multiple environments – like staging
  and production – for your backend APIs and frontend deployments, you’ll want to
  make sure you have the correct configuration and commands for each branch in your
  repository.

  T...'
---

Lorsque vous travaillez sur un projet avec plusieurs environnements  comme la préproduction et la production  pour vos API backend et vos déploiements frontend, vous voudrez vous assurer d'avoir la configuration et les commandes correctes pour chaque branche dans votre dépôt.

Cela peut être intimidant dans des situations où plusieurs développeurs travaillent activement sur une base de code, apportant des modifications à différentes branches, ou gérant plusieurs configurations spécifiques aux branches.

Comme avec chaque pull request ou changement poussé vers une branche, vous devrez examiner chaque ligne de code qui a été modifiée, ajoutée ou supprimée avant de décider ce qui est fusionné ou non. Les fichiers de configuration dans les bases de code ne sont pas exempts de cela, ce qui les rend sujettes aux erreurs, car un simple changement peut affecter votre intégration continue.

Lorsque des changements sont apportés à la branche de préproduction ou de production et qu'un build est déclenché, vous voudrez vous assurer que les bonnes ressources attachées à une branche sont maintenues. Dans certains cas, vous devrez peut-être définir différentes règles de redirection pour chaque client respectif, des commandes de build personnalisées, ou d'autres paramètres pour chaque branche.

Dans cet article, je vais vous montrer comment gérer les configurations spécifiques aux branches, y compris les redirections pour plusieurs branches automatiquement, en utilisant un simple script bash. Je vais également vous montrer comment fusionner en toute sécurité les règles spécifiques au contexte pour vos branches de préproduction et de production sur Netlify.

## Ce que nous allons couvrir :

* [Structure du projet et scénario](#heading-structure-du-projet-et-scenario)
    
* [Qu'est-ce que les redirections/réécritures ?](#heading-quest-ce-que-les-redirectionsreecritures)
    
* [Comment Netlify traite les redirections](#heading-comment-netlify-traite-les-redirections)
    
    * [Utilisation de la syntaxe du fichier _redirects](#heading-utilisation-de-la-syntaxe-du-fichier-redirects)
        
    * [Utilisation de la syntaxe du fichier de configuration netlify.toml](#heading-utilisation-de-la-syntaxe-du-fichier-de-configuration-netlifytoml)
        
* [Le problème : Gérer plusieurs fichiers netlify.toml pour différentes branches](#heading-le-probleme-gerer-plusieurs-fichiers-netlifytoml-pour-differentes-branches)
    
* [Comment écrire le script pour créer automatiquement notre(s) fichier(s) de configuration](#heading-comment-ecrire-le-script-pour-creer-automatiquement-notre-s-fichier-s-de-configuration)
    
    * [Exemple de fichier Netlify.toml](#heading-exemple-de-fichier-netlifytoml)
        
    * [Étape 1 : Créer le dossier de script et ajouter le fichier de script](#heading-etape-1-creer-le-dossier-de-script-et-ajouter-le-fichier-de-script)
        
    * [Étape 2 : Modifier package.json pour inclure la commande de script](#heading-etape-2-modifier-packagejson-pour-inclure-la-commande-de-script)
        
* [Comment déployer notre client sur Netlify](#heading-comment-deployer-notre-client-sur-netlify)
    
    * [Premier déploiement de votre projet sur Netlify](#heading-premier-deploiement-de-votre-projet-sur-netlify)
        
    * [Déploiements ultérieurs / Comment configurer les déploiements de branches](#heading-deploiements-ulterieurs-comment-configurer-les-deploiements-de-branches)
        
        * [Étape 1 : Configurer les variables d'environnement dans Netlify pour chaque contexte de branche  production, préproduction, etc.](#heading-etape-1-configurer-les-variables-denvironnement-dans-netlify-pour-chaque-contexte-de-branche-production-preproduction-etc)
            
        * [Étape 2 : Déclencher un nouveau déploiement](#heading-etape-2-declencher-un-nouveau-deploiement)
            
* [Inspecter vos déploiements](#heading-inspecter-vos-deploiements)
    
* [Conclusion](#heading-conclusion)
    

## Structure du projet et scénario

Considérez une situation où vous avez deux serveurs séparés déployés pour un projet : un pour servir les requêtes à un environnement de préproduction (déployé sur Render), et un autre pour l'environnement de production (déployé sur Google Cloud Run).

Vous avez également deux déploiements clients séparés sur Netlify, chacun avec leurs URL de base d'API respectives, qui sont servis par leurs serveurs respectifs comme illustré ci-dessous :

![Illustration montrant les branches d'un dépôt de projet - développement, préproduction et production - chacune avec son propre serveur et client](https://cdn-images-1.medium.com/max/1200/1*Zat3jiq5BCucEzDHKp8yuA.png align="left")

L'image ci-dessous est un dépôt `sample-project`, avec des dossiers/dossiers `api` et `client` à l'intérieur. Voici un aperçu de la structure dans chacune des branches décrites ci-dessus. Chaque répertoire contient son propre fichier `package.json`, est traité comme un composant indépendant et peut être déployé sur deux services séparés.

![Une structure de projet pour un projet exemple, incluant des répertoires et fichiers pour le backend et le frontend.](https://cdn-images-1.medium.com/max/800/1*Vkh8EyIA5qamhoJOz2ksSg.png align="left")

Dans votre déploiement frontend pour chacun des clients, toutes vos requêtes faites aux endpoints qui commencent par `/api/v1/` sont routées vers le serveur. Les autres routes restent dans le frontend pour vous diriger vers les pages à l'intérieur du client. Vous devez donc écrire les règles correctes pour guider votre client sur la manière de traiter ces requêtes. Ce sont ce qu'on appelle les règles de redirection ou de réécriture.

## Qu'est-ce que les redirections/réécritures ?

Les redirections, ou réécritures, sont des règles que vous pouvez créer pour que certaines URL soient automatiquement redirigées vers un nouvel emplacement n'importe où sur Internet (source : [WPengine](https://wpengine.com/)). Ce sont également des règles généralement connues sous le nom de **redirection d'URL** et vous pouvez les utiliser n'importe où  sur des sites web entiers, des sections d'un site web, ou une application web entière.

Dans les applications web, les redirections sont souvent utilisées pour déterminer comment traiter les requêtes. Les plateformes d'hébergement web telles que Netlify et Vercel les utilisent également, donnant aux développeurs l'option de déterminer comment leurs applications web traitent les requêtes.

## Comment Netlify traite les redirections

Netlify propose deux façons possibles de spécifier les règles de redirection. Vous pouvez le faire en utilisant la syntaxe du fichier `_redirects` ou en utilisant la syntaxe du fichier de configuration `netlify.toml`. Elles atteignent le même objectif, mais la syntaxe `netlify.toml` vous offre plus d'options et de capacités.

### Utilisation de la syntaxe du fichier `_redirects`

Si vous optez pour l'utilisation de la syntaxe de redirection, vous devez simplement créer un fichier `_redirects` dans le dossier public de votre application client, et spécifier les règles de redirection à l'intérieur. C'est aussi simple que cela. Voici un exemple de règle de redirection dans le fichier :

![Exemple de fichier _redirects de Netlify montrant la syntaxe d'utilisation et les règles de redirection](https://cdn.hashnode.com/res/hashnode/image/upload/v1733944577546/2f21a9b9-6843-4900-a6fe-5573a087b3d9.png align="center")

La règle ci-dessus peut être interprétée comme suit :

1. Envoyez toutes mes requêtes qui correspondent à `/api/v1` vers l'URL de l'API spécifiée, et retournez un code de statut de succès 200. Les astérisques (\*) après `/api/v1/` comme vu dans `/api/v1/*` lui indiquent d'ajouter toute autre extension de l'URL originale à l'URL de l'API indiquée. Par exemple, si vous avez une route `/api/v1/users` dans votre frontend, cette requête sera redirigée vers `https://your-api-base-url.com/api/v1/users`. Le `:splat` vu dans l'URL de l'API est simplement un espace réservé.
    
2. Servez toutes les autres routes par défaut via le fichier index.html. Cela est nécessaire pour garantir que vous ne rencontrez pas de pages cassées lorsque vous naviguez vers d'autres pages et essayez de visiter la page précédente en utilisant le bouton "retour".
    

### Utilisation de la syntaxe du fichier de configuration `netlify.toml`

Le fichier de configuration `netlify.toml` vous offre beaucoup plus de flexibilité lors de la spécification des règles de redirection, y compris, mais sans s'y limiter, la correspondance avec la route de requête originale, la destination requise, la réponse de code de statut préférée, les règles d'en-tête, les signatures, les restrictions de pays, les rôles et plus encore.

Voici un exemple de fichier `netlify.toml` provenant de la [documentation de Netlify](https://docs.netlify.com/routing/redirects/#syntax-for-the-netlify-configuration-file) :

![Exemple de fichier netlify.toml montrant la configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1733947216566/f64670b4-9d28-4c50-a753-1deb27dfc646.png align="center")

**Note rapide :** utiliser le fichier de redirections pour rediriger certaines requêtes vers notre API est parfaitement acceptable. Mais cela peut être considéré comme un risque de sécurité si l'URL de base de l'API est supposée être privée. Cela est dû au fait que tout fichier dans le dossier public est ce qu'il semble être  public  et n'importe qui peut y accéder.

Si les emplacements directs que vous souhaitez avoir dans votre application sont des URL publiques, alors n'hésitez pas à utiliser la syntaxe du fichier `_redirects`. Mais si vous préférez avoir une ou plusieurs URL privées, l'utilisation d'un fichier de configuration `netlify.toml` en combinaison avec les variables d'environnement est généralement une meilleure idée.

## Le problème : Gérer plusieurs fichiers `netlify.toml` pour différentes branches

Lorsque vous utilisez le fichier `netlify.toml` pour définir vos commandes de build et vos paramètres spécifiques à l'environnement, et que vous apportez des modifications qui sont poussées vers votre dépôt et ouvrent des pull requests, vous devez manuellement ignorer ou modifier chaque `netlify.toml` dans chaque branche. Cela devient finalement très stressant et sujet aux erreurs.

En plus de cela, nous voulons éviter d'avoir nos URL d'API codées en dur dans notre fichier `_redirects` ou `netlify.toml` au sein de notre base de code de projet pour des raisons de sécurité. Nous utiliserons les variables d'environnement fournies dans notre interface utilisateur Netlify pour les contextes de production et de préproduction.

Pour éviter les problèmes ci-dessus, nous utiliserons un petit script dans notre base de code pour générer dynamiquement les fichiers `netlify.toml` corrects pour chaque branche. Cette approche élimine les conflits et supprime le besoin d'intervention manuelle lors du changement de branches ou de la gestion des pull requests.

## Comment écrire le script pour créer automatiquement notre(s) fichier(s) de configuration

### Exemple de fichier `Netlify.toml`

Ci-dessous se trouve une capture d'écran d'un exemple de fichier `netlify.toml` que nous essayons d'obtenir pour chaque build. Vous pouvez voir que toutes nos requêtes qui correspondent à `api/v1/` dans notre base de code seront routées vers notre API.

Vous pourriez avoir vos requêtes d'endpoint d'API structurées différemment, par exemple `/api/your-endpoint`  assurez-vous simplement d'ajuster le script en conséquence. Dans ce projet exemple, nous utilisons `api/v1/your-endpoint` comme structure.

![Fichier de configuration Netlify montrant les commandes de build et les règles de redirection](https://cdn-images-1.medium.com/max/800/1*oj_oJDA7lnC9we2zuQHm4w.png align="left")

### Étape 1 : Créer le dossier de script et ajouter le fichier de script

Dans le répertoire `client`, créez un répertoire `scripts/` et un fichier de script [`configure-netlify.sh`](http://configure-netlify.sh). Vous devez faire cela pour chaque branche dans votre dépôt. Le contenu reste le même.

Ouvrez le fichier de script [`configure-netlify.sh`](http://configure-netlify.sh) et collez le contenu suivant à l'intérieur :

```bash
#!/bin/bash

# Vérifiez que API_BASE_URL est définie
if [ -z "$API_BASE_URL" ]; then
  echo "Erreur : La variable d'environnement API_BASE_URL n'est pas définie."
  exit 1  # Quittez le script pour arrêter le déploiement
fi

echo "Utilisation du point de terminaison de l'API : $API_BASE_URL"

# Définissez la configuration Netlify souhaitée
NETLIFY_CONFIG="
[build]
  command = \"npm install && npm run build\"
  base = \"client\"
  publish = \"dist\"

[[redirects]]
  from = \"/api/v1/*\"
  to = \"$API_BASE_URL/:splat\"
  status = 200
  force = true

[[redirects]]
  from = \"/*\"
  to = \"/index.html\"
  status = 200
"

# Créez ou mettez à jour le fichier netlify.toml
if [ ! -f "netlify.toml" ]; then
  echo "Création du fichier netlify.toml..."
else
  echo "Mise à jour du fichier netlify.toml existant..."
fi

echo "$NETLIFY_CONFIG" > netlify.toml

# Confirmez la configuration réussie
echo "Le fichier netlify.toml a été configuré avec succès !"
```

Le script fait ce qui suit :

1. Il vérifie les variables d'environnement pour s'assurer que `API_BASE_URL` est définie. Si ce n'est pas le cas, il quitte le build et le fait échouer. Nous avons fait cela pour nous assurer que vous ne créez pas par erreur un déploiement réussi mais avec des URL invalides en production.
    
2. Il crée ensuite le contenu du fichier `netlify.toml` comme montré dans l'exemple ci-dessus. Si vos endpoints d'API utilisent une structure différente de `api/v1/your-endpoint`, vous pouvez ajuster le script pour qu'il corresponde à votre structure souhaitée.
    
3. Il vérifie s'il existe déjà un fichier `netlify.toml`. S'il n'existe pas, il en crée un et écrit le contenu à l'intérieur. S'il existe, il le met à jour avec le contenu correct pendant le build, en utilisant le `API_BASE_URL` défini dans les variables d'environnement.
    

### Étape 2 : Modifier `package.json` pour inclure la commande de script

Pour intégrer ce script à votre processus de build, nous allons ajouter une commande de script au fichier `package.json` pour appeler ce script avant d'exécuter le build réel.

Ajoutez la commande `configure-netlify` comme suit : `"configure-netlify": "bash scripts/`[`configure-netlify.sh"`](http://configure-netlify.sh) dans les scripts de votre fichier `package.json`.

Mettez à jour votre commande de build pour exécuter le script avant d'exécuter le build réel : `"build": "npm run configure-netlify && vite build"`.

![Image montrant le fichier package.json mis à jour avec la commande personnalisée configure-netlify et la commande de build mise à jour](https://cdn-images-1.medium.com/max/800/1*Sds0AS4Poe80pc9D9YkBvQ.png align="left")

N'oubliez pas de sauvegarder ces modifications et de les pousser vers votre dépôt distant.

## Comment déployer notre client sur Netlify

Lorsque nous déployons notre client sur Netlify, nous avons trois options :

1. importer un projet existant (c'est-à-dire un projet qui existe sur un service de dépôt git tel que GitHub et GitLab),
    
2. importer à partir d'un modèle, ou
    
3. déployer manuellement un site statique en utilisant l'interface de dépôt de Netlify (glisser-déposer).
    

Pour que la configuration dans notre dépôt fonctionne comme prévu pendant notre processus de build, vous devrez utiliser l'option qui nécessite l'importation à partir d'un projet existant tel que GitHub. L'utilisation de l'interface glisser-déposer ne fonctionnera pas. Si vous devez utiliser cela, alors optez pour l'option de syntaxe du fichier `_redirects` pour définir vos redirections.

### Premier déploiement de votre projet sur Netlify

Lorsque vous déployez votre projet pour la première fois, vous avez la possibilité de déployer uniquement une branche initialement. Vous ne pouvez ajouter et spécifier d'autres options, telles que d'autres branches, que dans les déploiements ultérieurs.

Pour déployer votre projet, suivez les étapes suivantes :

1. Connectez-vous à Netlify &gt; [netlify.com](http://netlify.com)
    
2. Cliquez sur "Ajouter un nouveau site" &gt; "Importer un projet existant" &gt; "Déployer avec GitHub"
    
3. Cliquez sur "Configurer Netlify sur GitHub" &gt; Recherchez votre dépôt &gt; Sélectionnez-le
    
4. Entrez un nom de site unique pour votre projet
    
5. Configurez les paramètres de déploiement. Ici, vous devez sélectionner la branche préférée à déployer. Pour le déploiement initial, nous allons déployer la branche `main` que nous utilisons comme branche de production.
    
    * Branche : main/master
        
    * Commande de build : `npm run build`
        
    * Répertoire de publication : `dist` (Sélectionnez le répertoire où se trouvent vos fichiers statiques. Dans ce projet exemple, il est exporté dans le répertoire `dist`. Certains outils exportent dans `build`)
        
6. Entrez les variables d'environnement pour votre projet. N'oubliez pas d'entrer votre `API_BASE_URL` depuis votre serveur. Cela est une exigence essentielle selon le script bash.
    
7. Cliquez sur "Déployer le site"
    

![Écran de déploiement Netlify montrant les paramètres de build optionnels du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1733951997499/f329f2e6-b977-4b1f-a6ea-6b20610dc0d2.png align="center")

Votre projet devrait se déployer correctement, et vous pourrez voir la configuration `netlify.toml` générée par le script en inspectant les détails du déploiement en bas de la page de déploiement réussi.

Vous pouvez télécharger ce fichier sur votre machine locale pour voir la configuration générée. Elle devrait correspondre à l'exemple de fichier `netlify.toml` ci-dessus. Vous pouvez également tester qu'elle fonctionne en utilisant le lien de votre site généré.

![Écran Netlify montrant le journal de déploiement et les fichiers statiques après un déploiement réussi](https://cdn.hashnode.com/res/hashnode/image/upload/v1733952720930/97ccee2f-e93b-4205-94fa-a8ab32dd37c2.png align="center")

## Déploiements ultérieurs / Comment configurer les déploiements de branches

### Étape 1 : Configurer les variables d'environnement dans Netlify pour chaque contexte de branche  production, préproduction, etc.

Lorsque votre projet a été déployé avec succès, vous pouvez configurer les déploiements pour votre branche de préproduction. Pour modifier les configurations, vous devrez :

1. Naviguer vers la liste de vos sites
    
2. Sélectionner votre site déployé avec succès
    
3. Cliquer sur "configuration du site" dans le menu de gauche
    
4. Sélectionner "variables d'environnement" &gt; cliquer sur le bouton "Ajouter une variable".
    

![Page de configuration du site Netlify du site déployé avec succès, montrant les variables d'environnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1733953093253/26948920-70a7-47bc-8f53-4cb19a9d8543.png align="center")

Vous aurez la possibilité d'ajouter des variables individuellement ou d'importer un fichier `.env` entier. Vous pouvez choisir l'une ou l'autre option. Dans l'image ci-dessous, j'ai sélectionné "Importer à partir d'un fichier `.env`".

![Écran des variables d'environnement montrant les options disponibles pour ajouter une variable - en utilisant une entrée de variable unique ou plusieurs entrées à partir d'un fichier .env](https://cdn.hashnode.com/res/hashnode/image/upload/v1734124727631/1bb20e6b-1232-4a79-bc18-2df2440cb641.png align="center")

Voyant que notre site de production, déployé à partir de la branche `main` (avec les variables d'environnement de production), a déjà été déployé, vous devrez :

1. Désélectionner la branche de production (pour éviter de remplacer la branche principale initialement déployée. Faites attention à ne pas mélanger vos variables d'environnement pour différentes branches)
    
2. Sélectionner "déploiements de branche"
    
3. Copier et coller le contenu de votre fichier .env dans la section d'entrée
    
4. N'oubliez pas d'ajouter la variable d'environnement `API_BASE_URL` pour votre environnement de préproduction
    

Notez qu'en sélectionnant les déploiements de branche, les variables d'environnement importées ici affecteront tous les déploiements de branche, à l'exception de la branche de production. Vous pouvez personnaliser davantage vos contextes en sélectionnant une branche personnalisée, mais c'est une approche entièrement différente qui peut nécessiter de personnaliser davantage votre fichier de configuration `netlify.toml` ou le script bash.

![Écran des variables d'environnement avec les contextes disponibles pour le déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1733953419262/2f62d3d6-2549-4a75-aa0b-7a02225bd630.png align="center")

Si vous décidez d'importer chaque variable d'environnement individuellement, vous avez une option similaire à celle vue ci-dessous. Assurez-vous de sélectionner le contexte correct pour chaque branche.

N'UTILISEZ PAS LES MÊMES VALEURS POUR TOUS LES CONTEXTES. Comme vu dans l'image ci-dessous, la sélection de "*valeur différente pour chaque contexte de déploiement*" vous permettra de définir les valeurs pour chacun. Dans ce cas, nous définissons les valeurs pour les déploiements de branche. Votre variable de production initialement utilisée devrait déjà exister.

![Écran d'insertion de variable d'environnement pour une seule variable, montrant les options de valeur pour différents contextes](https://cdn-images-1.medium.com/max/800/1*699HAdcahAzATFCDYlbqpw.png align="left")

Lorsque toutes les variables ont été importées, vous pouvez les inspecter pour confirmer qu'elles ont été correctement importées en sélectionnant le menu déroulant à droite à côté de chaque variable et en inspectant leurs valeurs.

![Variables environnementales définies pour l'application web déployée](https://cdn.hashnode.com/res/hashnode/image/upload/v1733954618431/66e90f42-4e3d-4c5b-95ec-a6ae03207498.png align="center")

### Étape 2 : Déclencher un nouveau déploiement

Lorsque toutes vos variables d'environnement ont été importées pour les différents contextes  production et préproduction dans ce cas  naviguez vers "déploiements" dans le panneau de gauche de votre écran. Ensuite, appuyez sur le bouton "Déclencher le déploiement", effacez le cache et lancez un nouveau déploiement.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733954838853/79685cf6-54a5-4495-8777-914fcc46950f.png align="center")

## Inspecter vos déploiements

Vous pouvez confirmer que votre script fonctionne comme prévu en sélectionnant l'un des déploiements et en sélectionnant le menu déroulant de construction dans le "Journal de déploiement". Vous verrez la commande exécutée, ainsi que votre sortie et l'URL de l'API pour ce déploiement, comme défini par votre contexte.

![Journal de déploiement pour une application web déployée avec succès, montrant les valeurs enregistrées par le script d'automatisation pendant le build](https://cdn.hashnode.com/res/hashnode/image/upload/v1733955355311/8268c1f3-c9cb-4b98-8094-59b7dd2d5b13.png align="center")

## Conclusion

En suivant les étapes de ce guide et en utilisant votre script et les commandes mises à jour dans chaque branche de votre dépôt, lorsque vous pousserez des modifications, Netlify générera ou mettra à jour automatiquement le fichier `netlify.toml` dans chaque branche. Cela garantit que les configurations et variables d'environnement correctes pour chaque environnement sont utilisées au moment du build.

Votre script reste le même dans toutes les branches. Cela vous permet de vous concentrer sur d'autres modifications de code tandis que votre script gère la configuration correcte pour vous de manière sûre et facile.

Poussez des modifications vers n'importe quelle branche pour voir cela en action.

N'hésitez pas à me contacter sur [Twitter](https://x.com/@francisihej) (@francisihej) ou [LinkedIn](https://linkedin.com/in/francis-ihejirika) !