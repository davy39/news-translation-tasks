---
title: Comment construire un chatbot RAG avec Agent Cloud et Google Sheets
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-06-26T14:43:10.000Z'
originalURL: https://freecodecamp.org/news/build-a-rag-chatbot-agent-cloud-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Orange
seo_title: Comment construire un chatbot RAG avec Agent Cloud et Google Sheets
---

Yellow-Gradient-Make-Design-Blog-Banner--73-.png
tags:
- name: Intelligence Artificielle
  slug: intelligence-artificielle
- name: '#chatbots'
  slug: chatbots
- name: 'LLM''s '
  slug: llms
seo_title: null
seo_desc: 'Les entreprises d''aujourd''hui sont des usines à données. Chaque interaction, transaction,
  et processus interne génère un flux constant d''informations.

  Ces données ont une immense valeur, promettant d''améliorer la prise de décision, de rationaliser
  les opérations et de déverrouiller des informations profondes sur les clients...'
---

Les entreprises d'aujourd'hui sont des usines à données. Chaque interaction, transaction et processus interne génère un flux constant d'informations.

Ces données ont une immense valeur, promettant d'améliorer la prise de décision, de rationaliser les opérations et de déverrouiller des informations profondes sur les clients.

Mais les données restent souvent cloisonnées et inaccessibles. Elles peuvent être réparties dans différents départements et systèmes, et il peut être difficile de les comprendre et de les utiliser efficacement.

C'est là qu'intervient la technologie de génération augmentée par récupération ([RAG](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)). En combinant la puissance des techniques basées sur la récupération et des outils modernes d'IA générative, vous pouvez construire des applications de chat de génération augmentée par récupération (RAG) qui vous permettent d'interagir avec vos données en utilisant une simple interface de chat.

![Flux conceptuel de l'utilisation de RAG avec les LLM.](https://www.freecodecamp.org/news/content/images/2024/05/image-57.png)
_Qu'est-ce que la génération augmentée par récupération (RAG) ?_

Mais avant de pouvoir discuter de vos données, beaucoup de "travail préparatoire" est nécessaire. La mise en place de l'infrastructure - le pipeline, la base de données vectorielle, le courtier de messages et la récupération des connaissances - est un processus complexe et chronophage. C'est là qu'intervient l'outil open source [Agent Cloud](https://theankurtyagi.com/what-is-agent-cloud/).

Dans ce guide, vous apprendrez tout sur Agent Cloud et ce qu'il peut faire. Nous commencerons par examiner quelques informations de base et les problèmes actuels que nous traitons. Ensuite, nous verrons comment Agent Cloud peut aider à les résoudre.

## Comment j'ai commencé à travailler avec Agent Cloud

Je suis passionné par les nouvelles technologies et les [outils pour développeurs](https://theankurtyagi.com/blog/), et je me situe quelque part entre le marketing produit, la croissance et la défense des développeurs. Je me spécialise dans la création de contenu écrit technique de haute qualité à des fins éducatives.

Je suis impliqué dans le web depuis ~14 ans, les 4 dernières années ayant été documentées en détail sur mon [site web](https://theankurtyagi.com/).

J'aimais être ingénieur logiciel, mais ce que j'aime vraiment faire, c'est coder, concevoir, développer et puis écrire.

Plus tôt cette année, j'ai rencontré [Andrew](https://www.linkedin.com/in/andrewnada/) (fondateur d'Agent Cloud) dans un groupe Slack privé. Il cherchait quelqu'un qui pouvait non seulement écrire sur le produit, mais aussi discuter et enseigner aux gens ce qu'ils construisent. Je l'ai contacté, et après deux rounds de discussions, nous avons commencé à travailler ensemble.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-35.png)

J'ai commencé par construire quelques chatbots RAG sympas en local et j'ai ensuite écrit un couple de guides complets sur "[Comment construire un chatbot RAG avec Agent Cloud](https://www.agentcloud.dev/blog)".

Dans cet article, je vais vous apprendre à construire une application de chat RAG en utilisant Agent Cloud pour discuter de manière privée et sécurisée avec vos données Google Sheets. Je vais également parler de pourquoi je pense qu'Agent Cloud est un bon outil de développement open source.

## Table des matières :

* [Qu'est-ce qu'Agent Cloud](#heading-questce-que-agent-cloud) ?
* [Qu'est-ce que RAG](#heading-questce-que-la-retrieval-augmented-generation) ?
* [Défis de la construction d'un chatbot RAG sans Agent Cloud](#heading-defis-de-la-construction-dun-chatbot-rag-sans-agent-cloud)
* [Prérequis](#heading-prerequis)
* [Comment installer Agent Cloud via Docker](#heading-comment-installer-agent-cloud-via-docker)
* [Comment ajouter des modèles dans Agent Cloud](#heading-comment-ajouter-des-modeles-dans-agent-cloud)
* [Comment créer votre clé de compte de service GCP](#heading-comment-creer-votre-cle-de-compte-de-service-gcp)
* [Comment activer l'API Google Sheets](#heading-comment-activer-lapi-google-sheets)
* [Comment configurer vos sources de données](#heading-comment-configurer-vos-sources-de-donnees)
* [Comment configurer les outils](#heading-comment-configurer-les-outils)
* [Comment configurer un agent](#heading-comment-configurer-un-agent)
* [Comment créer une tâche](#heading-comment-creer-une-tache)
* [Comment configurer votre application](#heading-comment-configurer-votre-application)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'Agent Cloud ?

[Agent Cloud](https://www.agentcloud.dev) est une plateforme open-source qui vous permet de construire des applications de chat privées et sécurisées alimentées par de grands modèles de langage (pensez à ChatGPT).

Elle rationalise ce processus en fournissant une offre "RAG en tant que service" et un pipeline intégré qui vous permet de diviser, de segmenter et d'intégrer des données provenant de plus de 300 sources (y compris [Google Sheets](https://www.agentcloud.dev/integrations/google-sheets), Salesforce, Atlassian Confluence, [BigQuery](https://dev.to/agentcloud/how-to-build-a-rag-chat-app-with-agent-cloud-and-bigquery-15b), [MongoDB](https://dev.to/agentcloud/how-to-build-a-rag-chatbot-with-agentcloud-and-mongodb-4la7), [Postgres Data](https://dev.to/agentcloud/how-to-build-a-chat-app-with-your-postgres-data-using-agent-cloud-33hk), SharePoint et OneDrive).

![Liste des sources de données prises en charge par agentcloud](https://lh7-us.googleusercontent.com/mCVaA9lJyTTTLY7YNebA8AyR5Tj_iQ3werHlAERD9-NgHPQ6BXUo42NMIm9HwnIXni-iWaTrjVtROtmx8XhY7RXF_wh2LnYAifRDnP7GYFl9EAvP83EuEtoHa7BM4OZBjCokVzYwBF-4Nrd8TlG-JvQ)
_Sources de données_

## Qu'est-ce que la génération augmentée par récupération ?

RAG est un processus pour améliorer la précision des grands modèles de langage. Il le fait grâce à la récupération à la demande de données externes et en injectant du contexte dans le prompt, au moment de l'exécution.

Ces données peuvent provenir de diverses sources, telles que la documentation ou les pages web de vos clients (par grattage), et les données ou documents de dizaines (sinon de centaines) d'applications tierces comme leurs bases de données, Google BigQuery, HubSpot, Google Ads, Google Analytics 4 (GA4) et ainsi de suite.

Pour ceux qui souhaitent approfondir la génération augmentée par récupération et comprendre ses applications et son importance plus larges, je recommande vivement de lire ce blog complet de [NVIDIA](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/). Il offre des informations et un contexte précieux qui complètent les aspects pratiques abordés dans cet article.

## Défis de la construction d'un chatbot RAG sans Agent Cloud

Si vous travaillez avec ces outils d'IA au quotidien, il devient facile de comprendre la valeur qu'ils apportent et de réaliser l'importance d'Agent Cloud dans la simplification du processus de développement de chatbots.

Mais pour apprécier pleinement ses avantages, vous devez comprendre comment le développement de chatbots était géré avant que de tels outils ne soient disponibles.

Avant des outils comme Agent Cloud, créer un chatbot RAG (Retrieval-Augmented Generation) était une tâche ardue et gourmande en ressources. Vous deviez intégrer manuellement divers composants, ce qui nécessitait une expertise significative dans plusieurs domaines.

Voici quelques défis rencontrés et les solutions que l'équipe d'Agent Cloud a dû concevoir :

### Récupération et gestion des données :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-36.png)
_Liste des sources de données_

* **Problème :** Garantir que le chatbot pouvait récupérer et gérer efficacement les données provenant de sources comme Google Sheets, les bases de données, etc.
* **Sans Agent Cloud :** Les développeurs devaient écrire des scripts personnalisés pour la récupération des données, souvent en utilisant des API pour récupérer les données de Google Sheets. Cela impliquait de gérer la mise en forme des données, la vérification des erreurs et les mises à jour en temps réel manuellement. C'était un processus chronophage sujet aux erreurs.
* **Solution d'Agent Cloud :** Automatise la récupération et la gestion des données, garantissant une intégration fluide et précise avec une intervention manuelle minimale.

### Traitement du langage naturel (NLP) :

* **Problème :** Implémenter le NLP pour comprendre les requêtes des utilisateurs et générer des réponses humaines.
* **Sans Agent Cloud :** Les développeurs devaient intégrer des moteurs NLP autonomes tels que TensorFlow. Cela nécessitait de former des modèles sur de vastes ensembles de données, de les affiner pour la précision et de les mettre à jour constamment pour gérer efficacement les nouvelles requêtes.
* **Solution d'Agent Cloud :** Offre des capacités NLP intégrées, réduisant considérablement le temps de configuration et fournissant une compréhension linguistique de haute qualité dès la sortie de la boîte.

### Évolutivité et maintenance :

* **Problème :** Garantir que le chatbot pouvait gérer des charges de données croissantes et des interactions utilisateur.
* **Sans Agent Cloud :** Construire une architecture évolutive signifiait investir dans une infrastructure serveur robuste, écrire du code efficace et surveiller et maintenir continuellement le système pour gérer la croissance.
* **Solution d'Agent Cloud :** Conçu pour évoluer sans effort, permettant aux développeurs de se concentrer sur l'amélioration de la fonctionnalité plutôt que sur la gestion de l'infrastructure.

### Interaction et expérience utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-37.png)
_Interface utilisateur de l'application Agent Cloud_

* **Problème :** Créer une interface engageante et conviviale.
* **Sans Agent Cloud :** Les développeurs devaient construire des interfaces personnalisées, souvent à partir de zéro, ce qui nécessitait des ressources supplémentaires de conception et de développement. Garantir des interactions fluides et une réactivité était un défi majeur.
* **Solution d'Agent Cloud :** Fournit des modèles préconstruits et des options d'intégration faciles, améliorant l'expérience utilisateur avec un effort minimal.

En comprenant ces défis, vous pouvez voir comment un outil comme Agent Cloud aide le processus de construction de chatbots RAG. Il aborde les points de douleur de la gestion manuelle des données, de l'intégration complexe du NLP, des problèmes d'évolutivité et de la conception de l'interface utilisateur, fournissant une solution tout-en-un qui économise du temps et des ressources.

## Prérequis

Vous n'avez besoin d'aucune connaissance préalable des applications de chat RAG ou de Google Sheets pour suivre ce guide, car Agent Cloud gère la division, l'encodage, le stockage et la synchronisation des données. Cela vous permet de vous concentrer sur la discussion avec vos données et l'interprétation des résultats.

## Comment installer Agent Cloud via Docker

Tout d'abord, vous devrez installer Docker sur votre système si vous ne l'avez pas déjà. [Docker](https://docs.docker.com/get-docker/) est une plateforme pour exécuter des applications conteneurisées.

Ouvrez votre terminal et exécutez la commande suivante pour cloner le dépôt Agent Cloud depuis GitHub :

```bash
git clone https://github.com/rnadigital/agentcloud.git
```

Utilisez la commande suivante pour vous déplacer dans le répertoire `agentcloud` nouvellement cloné :

```bash
cd agentcloud
```

Pour exécuter Agent Cloud localement, exécutez cette commande :

```bash
chmod +x install.sh && ./install.sh
```

Cette commande accordera les permissions d'exécution au script install.sh et l'exécutera. Le script téléchargera les images Docker nécessaires et démarrera les conteneurs Agent Cloud dans votre environnement Docker.

![Image](https://lh7-us.googleusercontent.com/IJP_WeswIONKA5EsL87jVisv0mZRsk__P5BajAlXZU3fQW8Fif6mdjqW0t-NTCkU_ZNHAk6PJ4U5UthUmDFOsOQhnmQyY6HwMxHEDIxfqy-VfZODKOq7jFv9OpAlXkR1AszdYK0gkn0RDEut3Y7U7K4)
_Configuration de développement local - Agent Cloud_

Une fois le script d'installation terminé avec succès, vous pouvez voir les conteneurs Agent Cloud en cours d'exécution dans l'application Docker.

![Image](https://lh7-us.googleusercontent.com/oZ4mwbfNiCtFcv4scaILguo5QYVR_cwU5mpJqEzDzq-2gMHtyrD-XbZJnMiloPDFmVcFaUc6KQLyBWw6SnnSlVrTU-IcBIspkIELSZaGJ3M-9bRaq7H9NX94tdug39a98p0XQfa3RNmCYsxiSlTQDUA)
_Services Docker locaux_

Une fois que tout est opérationnel, vous pouvez accéder à l'interface utilisateur d'Agent Cloud dans votre navigateur web.

Accédez à l'URL :

```
http://localhost:3000/register
```

Cela ouvrira généralement la page d'inscription où vous pouvez créer un compte pour utiliser Agent Cloud.

![Image](https://lh7-us.googleusercontent.com/-o54n5I5Z_6RByvP6IaDXyDC5hlLgkRMFCEHlvJukZ5RWMV31G0ty2NZC09xA-O2-wslq_BUWCxGMcWRX1RT-ed5D75MFqOvNZR5-qA1Dg_lDChV-BGnrdNgq4epGxGGWmgSfT0qLvxq8J80tgAG64Q)
_Page d'inscription - Agent Cloud_

Vous pouvez maintenant vous connecter en utilisant les identifiants que vous avez créés lors de l'inscription.

Une fois que vous vous êtes inscrit et connecté avec succès, vous serez accueilli par l'interface utilisateur d'Agent Cloud. Cette interface fournit un hub central pour gérer vos sources de données, agents, tâches, modèles, applications, identifiants, etc.

![Image](https://lh7-us.googleusercontent.com/zEAo52ay_80MFLRDZPeRUgMCgx0VtPhOzX_68BSkO0Bkh9-66sAtrVYRTig15imqVFTAHs6OZ0fijXYrZxUMgeExMkRFyTEI9OvKijZWBZKzaQcYrBl0dfJ-MH5E5_5G-IpcTs-312lIdq77INYDk00)
_Écran d'accueil - Agent Cloud_

Félicitations ! Vous avez installé Agent Cloud avec succès. Passons maintenant à l'étape suivante et construisons notre application de chat RAG en utilisant Google Sheets comme source de données.

## Comment ajouter des modèles dans Agent Cloud

Allez dans l'onglet Modèles dans Agent Cloud. Cliquez sur le bouton Ajouter des Modèles pour ajouter deux types de modèles.

* Un modèle d'intégration rapide est un modèle léger qui s'exécute localement sur votre machine. Il divise et segmente vos données avant de les intégrer.
* OpenAI est un fournisseur populaire de LLM basé sur le cloud.

![Image](https://lh7-us.googleusercontent.com/SlXyhi9xFjz8o1dsMnNApxNDJ8G-NEppj6jfP1TkyaNjU3X6Ewt5NuKQ4mj9SKYxsQOMJ650ErJVvJWR9w4WbNfPRtb26pXnjzoUEsOX6jN7foDbiaM_U6jUJE9HSKqQpSDK54QKjLyI_T9yr2xTGDs)
_Écran des modèles - Agent Cloud_

## Comment créer votre clé de compte de service GCP

Agent Cloud offre deux méthodes d'authentification pour accéder à vos données Google Sheets :

* Google (Auth) - Cette méthode implique l'autorisation directe d'Agent Cloud via votre compte Google.
* Compte de clé de service - Cette approche utilise une clé de service, une identité spécifiquement créée pour l'accès des applications aux services de la plateforme Google Cloud (GCP), y compris Google Sheets.

Pour ce guide, je me concentrerai sur la méthode du compte de clé de service, qui est généralement considérée comme une approche plus sécurisée et rationalisée pour la communication entre applications.

**Voici ce dont vous aurez besoin :**

* Un projet Google Cloud Platform (GCP) avec l'API Google Sheets activée.
* Une clé de compte de service créée dans votre projet GCP. Cette clé sera utilisée pour authentifier Agent Cloud.

Je vais vous guider à travers la création d'une clé de compte de service dans votre projet GCP et la configuration d'Agent Cloud pour l'utiliser afin d'accéder à vos données Google Sheets.

Tout d'abord, créez un compte Google Cloud Platform. Ensuite, créez un nouveau projet. Vous pouvez donner à votre projet n'importe quel nom que vous préférez.

![Image](https://lh7-us.googleusercontent.com/s1m6tovJn9Hv7NsWNat4-0AKU_PzwiO6oujqSFwG0Yj-lEyVFbwBMrNIWd-h6ill46ZbHqmdrBH8_xTxXWRP-I6G33n2qB9jhYqCNvtQiYqmc15rSJ7jgP9Qw4y4CfaWDkHfNVl_cb4qHa5HhfyTnns)
_Comment créer un compte GCP_

Accédez à la section "IAM & Admin" et sélectionnez "Comptes de service".

![Image](https://lh7-us.googleusercontent.com/jObPCuwTVS1B9-z5yy4rX4Xi775Ur2AGz8B8k-dISs92F-0Ww5Nk4i3m77VzwvKT5w8pjtpHvEBqfvPlKQf6HC_hF4ghh6mQmeAj_BQm7qH3DJeF_tUFZU2lrDvZ5jB3taEpmQu5kn4cWM_W8mWbA_M)
_Écran IAM et Admin_

Cliquez sur "Créer un compte de service" et fournissez un nom et une description.

![Image](https://lh7-us.googleusercontent.com/un89_I_sIaEsLrROHvoZF10CYb0KeOrRjhzcm_kregQD-4v7-7Tg0xkhVOqqTNwPcaE0xvio_SL9OD4JFxxwql_T_YIbazfAUADcwh-tkM8FZ8YNwiDiEgTqA-zELb4kIILxFYGDw6t4Vc8qYD7UFPI)
_Comment ajouter un compte de service_

Entrez le nom de votre compte de service et l'ID de service unique, puis cliquez sur **Terminé**.

![Image](https://lh7-us.googleusercontent.com/pKIZ1n1-dTCXB0Lzqb5unx-ChrghpEVp8z_zC0Cv6N5PhN2oaHKtgBjsutM_YvynvtSO17cq89uIB6koyktx0W-vxGy_xIyr_nOlwDe_jcvU4ZtU1fGKDG7lMxPvgMZgjkgMO6odWV56gR3BAKWq53I)
_Comment créer un compte de service dans GCP_

Sous l'onglet actions, cliquez sur l'option gérer les clés.

![Image](https://lh7-us.googleusercontent.com/ju2mGTR2qMExBbW1vt8budeR1MeA9uNZddtx-IJhFAUaV-bw0GlVJUny9kdXJWndgWA4VXpl70DtYMpXCKQj7-zLus_3iJkl430EoIIcNtBfe2FThCFwQirwlCb0YJwJHb5z54HVKbuw4WlC8PY-HyE)
_Projet_

Cliquez sur le bouton **AJOUTER UNE CLÉ** et sélectionnez l'option Créer une clé.

Sélectionnez JSON comme type de clé, puis cliquez sur Créer une nouvelle clé.

![Image](https://lh7-us.googleusercontent.com/cynXfWX4n8ngRB-mB_CTLvUC1xA4ZqmSnaYtv6K3haSgJyAGlTk-l__J2LXZhupGJpJcZ9LW6NDlw6l05YlKev6sYVsXC9vMjCD3LgPGcCX9O405L-Ixn-LV8jmJbiRcd97y2TfL3zvezgZMi4eNYKw)
_Ajouter des clés dans GCP_

Sélectionnez JSON comme type de clé, puis cliquez sur Créer. Votre clé JSON de compte de service ou votre clé JSON sera automatiquement téléchargée.

![Image](https://lh7-us.googleusercontent.com/RmAJh50XGOSlSbK-hqWveHc4GozeFZSTsB3oU7y7d4nJ-tiEbfdcyQDdrUOfJonS-8w2GAw30vF1AlII8SOEPHSGz7Ip2Xdc60ypSi_gfljQJa_w84UoyfakUM_U-DcbcOlujk4uN0rrFDXG19aW0Rc)
_Créer une clé privée dans GCP_

Conservez ce fichier en sécurité, nous l'utiliserons plus tard pour l'authentification.

## Comment activer l'API Google Sheets

Vous devrez également activer l'API Google Sheets dans votre projet Google Cloud.

Ouvrez le menu de navigation de gauche et accédez à "APIs & Services" puis "Bibliothèque".

![Image](https://lh7-us.googleusercontent.com/1wVRoIvsYl6cYlaxeck2Ob2EviXaktCRdI68xVMjwSbXfABsYWTAkCHNEW7kwc2Ww2MoBop8-3-vS9s_1FIGuM7lq1E5cmp02dZ4ApPdbasZ6SneopXV5PGaiGF5AnVUVV9LVTdMQW8qSpOCzzfMs40)
_APIs et Services dans GCP_

Tapez "Google Sheets API" dans la barre de recherche et appuyez sur Entrée.

L'API Google Sheets apparaîtra dans les résultats de recherche. Cliquez dessus.

![Image](https://lh7-us.googleusercontent.com/TUq6HeWJfhZkZaAHQRst9cZKKlG3zbQkU8NBfl5tEZ43pgBbyYPDiLpHUt9yu1xF1-e8XWUp2isXS7zRcYonVlOwoEj2KJn2PZbK65UmA1KWv2y9AcoCxIaTuCaq5pJ2rrCo1wiZbwL1nDnBhsjPzec)
_API Google Sheets_

Sur la page des détails de l'API, cliquez sur le bouton "**ACTIVER**".

![Image](https://lh7-us.googleusercontent.com/Rh0qrd79Yqlw1YF5JZ_CSJwvO8ZpnytUs0392Y3OBEmmpLar1JyuOggQo-qms4qWtv9ZPLS69uiNmn4Hi4fSneAQZRIR-eRxWtbagqwNrf0q5qNGIxKJNAnjNk1uDziRLlzny4ZWZL0zeljWkmFT-7E)
_Activer l'API Google Sheets_

## Comment configurer vos sources de données

Agent Cloud vous permet de traiter des données provenant d'une large gamme de sources.

Dans ce guide, j'utiliserai Google Sheets comme source de données. Sheets est une application de feuille de calcul basée sur le web populaire incluse dans Google Workspace. Google Sheets vous permet de créer, modifier et collaborer sur des feuilles de calcul en temps réel.

Pour cet exemple, je travaillerai avec un ensemble de données de plaintes de consommateurs financiers stocké dans une feuille Google Sheets.

Cet ensemble de données contient plusieurs colonnes représentant les étapes clés des ventes et les détails, potentiellement incluant :

* ID de plainte
* Soumis via
* Date de soumission
* Date de réception
* État
* Produit
* Sous-produit
* Problème
* Sous-problème
* Société
* Réponse publique
* Réponse de la société au consommateur
* Réponse en temps opportun ?

Voici comment connecter vos données Google Sheets :

Accédez à l'onglet Sources de données dans l'interface Agent Cloud.

Cliquez sur le bouton étiqueté **Nouvelle Connexion**. Cela initiéra le processus d'ajout d'une nouvelle source de données.

![Image](https://lh7-us.googleusercontent.com/Tr8WlGVlJTmef0xrTvAxjLeTHCpLua_VDxZ9jamnlXQDY8wKsPf0skYQ_b1PFE0d9K13ndHS-piLpDKu16ikxLL9-AUb4lpgFw2pA6-TOI0lRwLQR5KBPbus5FDqJNkbKQYXdf2s4daLRHP4gPci0Ec)
_Écran des sources de données - Agent Cloud_

Recherchez et sélectionnez "Google Sheets" comme source de données.

![Image](https://lh7-us.googleusercontent.com/aNI6G2gH3HNF4XqibSxNOHjXWwW7X_jgtyK79B0k46LJUL1j_1G9vgYOtUdgT__6mjet3AMXEosqRLsrXZHZsf2rW3UhKPKdpAO2v6RFl8acpdINe6l6-1Y4ZGP52oP4xQVrm1XBlpHVuZVYLfx6-M0)
_Créer une source de données_

J'ai nommé notre source de données **Plaintes des consommateurs financiers**, que vous pouvez nommer comme vous le souhaitez. Ajoutez une description claire et concise. La synchronisation des données sera manuelle. Cela signifie que vous devrez initier le processus de rafraîchissement des données chaque fois que vous souhaitez que les dernières informations de vos feuilles Google Sheets soient reflétées dans Agent Cloud.

Entrez la taille de lot de lignes appropriée. La taille de lot de lignes signifie combien de lignes sont traitées depuis la feuille Google. Par exemple, la valeur par défaut 200 traiterait les lignes 1-201, puis 201-401, et ainsi de suite.

Choisissez la méthode d'authentification comme "**Authentification par clé de compte de service**".

Entrez la clé JSON **que nous avons téléchargée plus tôt ci-dessus** sous le champ Informations du compte de service.

Entrez le lien vers la feuille de calcul Google que vous souhaitez synchroniser. Pour copier le lien, cliquez sur le bouton 'Partager' dans le coin supérieur droit de la feuille de calcul, puis cliquez sur 'Copier le lien'.

![Image](https://lh7-us.googleusercontent.com/L9rtuBctsZISgx997WPk-zW25t46yJEvTMg7-wOCE7yBYPrd6l58BkPRFSWIErEf-1QR8v_6QHWQMtOlMyjOVfPPUUiE6yTOSg5BV5DexE3Jw_fANfmPSQRQqueAYJ3ODS3HRFzmA19PN8JYtOTXbi4)
_Ajout de détails sous la source de données_

Cliquez sur le bouton soumettre.

Sélectionnez la collection et les champs que vous souhaitez synchroniser avec la base de données vectorielle et entrez leurs descriptions.

![Image](https://lh7-us.googleusercontent.com/oPDKJbdi5uWh4q0staVJA4gTUytt_EVxCPBeIhV8VUGBsShtYeH9OJ_1R1uvN6HJYcgBvX64DHKt4qxNggdV6bx0filBtMdsuDo_xyhJjmipgIO52dzNmy-ABAtOwi-x-l7hCJoo6lFITMOpSDz83eo)
_Fenêtre contextuelle du modèle_

Cliquez sur continuer et choisissez le champ que vous souhaitez intégrer, puis choisissez le modèle.

![Image](https://lh7-us.googleusercontent.com/fa8oHY4rDm9SHQ4La-FM5c8BuWq1eWOsTzAhyq-IgMBaGIXR5crLog7gQ3Ziq0X_cngVy5J9yCF6Ld8u-Py6ByQI_S72jB4a5An8BHES6lng2675hjQeyP-ai0_zBY5pmTmX1LgRDI1qLPGsQ3Ws0QA)
_Sources de données_

La connexion à votre feuille Google Sheets est maintenant établie.

Lors de la première exécution, Agent Cloud traitera les données de votre feuille de calcul et les convertira dans un format adapté à une récupération efficace. Ces données traitées seront ensuite stockées dans le magasin vectoriel d'Agent Cloud.

![Image](https://lh7-us.googleusercontent.com/DWPrunB5TnUXQg7E0gV_XwoETIGO-Qo7cBpN8oYUl9Up--j3_roKiNS6--3CZZADnSeQWfjtO-j3r9RfQsVxQBsZ_NZvhq5Ahnkik2fGPaz0B6bDDVUJRq5rVXDxEkZ0fIIxMxRjqRdxZOIAM3SXiug)
_Nouvel écran de source de données_

Si vous êtes à l'aise avec les détails techniques, vous pouvez vérifier la présence des données dans le magasin vectoriel Qdrant en cours d'exécution localement sur le port 6333.

Cela peut être accessible via : http://localhost:6333/dashboard#/collections.

Recherchez une nouvelle collection correspondant à vos données Google Sheets.

![Image](https://lh7-us.googleusercontent.com/gEdkROWowqm1Xr8Q0ixb65CVZB-UNrzLnNh6KPXkPhAZaP5vHIOSJMeK28nyXye2I846SbMhfo9qG9I2qp67r6BNJLHJDM_z9kYc-KSoN0bUpfUS0CIoQBV_qQcVeXm5mqbIxclnM4VCN4pmc_w1u1k)
_Écran des collections_

Vous pouvez cliquer sur la collection pour afficher les charges utiles et les champs peuplés dans la collection.

![Image](https://lh7-us.googleusercontent.com/kQtXRqdF1VR_4UmJUqYGcNMcoVrx9kj1Ncrkgvgb3nzEX7s8UvHscOkYEx18P1qxYy6U04UjLDz-SqjVtTsvjHjxajx5qwsAsVkRPXy1nFBAtjELcht8cSL1vE4jVl49J39KHZuIohiNkAFscO9H4m0)
_Charge utile_

## Comment configurer les outils

Les outils jouent un rôle crucial dans la facilitation de l'interaction efficace entre l'agent IA et son environnement, permettant un traitement fluide des informations et l'exécution d'actions alignées sur ses objectifs.

Ces outils peuvent inclure des fonctions, des API, des sources de données et des ressources adaptées pour permettre à l'agent d'entreprendre diverses tâches de manière autonome et efficace. Bien que vous ayez la flexibilité de créer vos propres outils selon vos besoins, Agent Cloud rationalise également le processus en générant automatiquement un outil lors de l'ajout d'une nouvelle source de données.

Cliquez sur l'onglet Outils pour passer à la page Outils et cliquez sur le bouton **Nouveau**.

Entrez les noms des outils et ajoutez une description. Une description détaillée et détaillée aide les agents à mieux comprendre quand utiliser chaque outil.

Choisissez la source de données et cliquez sur le bouton Enregistrer.

![Image](https://lh7-us.googleusercontent.com/URmNamQ6ccOn5FbABAaBo7tfSjAmxZZgT_sN5W8aNrzdfFPbMCMcRwUk6X5YNL_CKTctP-cQxUURBwCADnGQyALwEUmmoQgBBUAsdtEDUWkWxH9oRp15pKHFcnObNpCkjw_eEdSiGnZbdVZodNraQ5Y)
_Écran d'édition de l'outil_

## Comment configurer un agent

Les agents IA sont des systèmes intelligents qui excellent dans la gestion des tâches routinières ou répétitives en percevant leur environnement, en collectant des données et en utilisant ces données pour prendre des décisions.

Cliquez sur l'onglet Agents puis sur le bouton Nouveau Agent.

![Image](https://lh7-us.googleusercontent.com/5JrsomIfl-WKZ2hOLW-MZ34xhRpJdhx9hzKwAz2Ab0kDtCVTnZy_rsgjoreGuS533ZCgq125n11M9siNy_AlFHTuMXOHhCSkFGzbE6gNSCQ7YMxw4-Sut1f_-ydDeKchOJjeAtcKxUVoSBmattKAiIg)
_Nouvel écran d'agent_

Définissez le **Nom**, le **Rôle**, le **But** et le **Contexte** d'un agent comme indiqué ci-dessous.

Dans la section "Modèle", choisissez le moteur IA pour alimenter les capacités de raisonnement de votre agent. Pour cet exemple, nous avons sélectionné "OpenAI GPT-4" comme Modèle et Modèle d'appel de fonction.

Choisissez l'outil que nous avons configuré précédemment sous Outils (Optionnel).

![Image](https://lh7-us.googleusercontent.com/d_NajepTkSjuk-tkpiuWcdupeY02HU5nYatqyfjMgj6WXXvBJTgYuStRoSgCFAqNpU4WK8MIarqLJY5MvytjkuQWI4CFyBvTvDsylYEAWgKS8p9f-EbO6LvHYnRFwBd5yQjDvt6XGlriuEfGkicVi-g)
_Ajout de détails dans l'écran de l'agent_

Si "OpenAI GPT-4" n'est pas déjà configuré dans Agent Cloud, vous pouvez facilement l'ajouter. Cliquez sur le champ "Modèle" et sélectionnez "Ajouter un nouveau modèle". Une nouvelle fenêtre apparaîtra, vous permettant de définir le nom du modèle, le type, les identifiants (votre clé API OpenAI) et le modèle LLM spécifique.

![Image](https://lh7-us.googleusercontent.com/0M9gkgwNfR-2VPGdgVN75Aqh-_aZuotKjasIVbiuOEaV6Wf8O-rQZo3bwk8-ZdHv8tfgRywXnlSy57An1rndCfzmfExx4K7nZ_UXpqDOJ_x1q0IUEnYaMRWqI6EzoEWcDzwx4CsFeWncc2bIiI82uOA)
_Fenêtre contextuelle du modèle_

Cliquez sur le bouton Enregistrer. Une fois que vous avez enregistré ces informations, "GPT-4" sera disponible pour la création future d'agents.

![Image](https://lh7-us.googleusercontent.com/3qE96774xn2RHAecevtTlCQ4GUv_WcC6r3sFZFdPNGUNCafENkdQ5SaONMSLzwwIsFyjIgLyp-XlVU-ZijHBybv_ay2KCICrxcR71w7GgqCuklvXK5znfIoRtM03Wd9pSdXFUEWVKnrYnjaGv__l8kk)
_Écran des agents_

## Comment créer une tâche

Les tâches sont des actions spécifiques assignées aux agents pour être complétées. Pour créer une nouvelle tâche, accédez à l'onglet Tâches et cliquez sur le bouton "Ajouter une tâche".

![Image](https://lh7-us.googleusercontent.com/wN1Wy93IPaxiU6NdElwizuJ4e6meqz4-jMiibnKN02WZqNikxMPWOZKsWDNVSlGU-X7IpY1cqPPAlF13aVKSVBGyw-ImPGKYXH2XH-1Yjg3FjI66mBrU-_hrPfbTntKJ1JZ4keZ5X06jnK06-ikwNdE)
_Écran de création de tâches_

Entrez les détails suivants dans la fenêtre contextuelle ci-dessous.

* **Nom de la tâche** : Donnez à votre tâche un titre clair et concis qui reflète son objectif.
* **Description détaillée** de ce que la tâche implique.
* Choisissez l'outil que nous avons créé précédemment, qui est "**Plainte des consommateurs financiers**" dans mon cas.
* Sélectionnez l'agent préféré que nous avons créé précédemment, que nous avons nommé "**Agent des plaintes des clients**".

![Image](https://lh7-us.googleusercontent.com/RujrqL0gjUYk31aJSYKQYyY55T_nIy-PdSdm8uhcodHGcs8lsHyctuJLnkI4COAL34tXHFjnsjRvypzRaThbIkVEhlTU2quvmaA5cxihN_MHGfg6QaB1i7oBgtXx2Bwa5hEQLbdtEM8Za70JgLRuONI)
_Ajout de détails dans l'écran des tâches_

Cliquez sur le bouton **Enregistrer** pour enregistrer la tâche.

## Comment configurer votre application

Maintenant, attachez vos ceintures car nous allons nous lancer dans la partie excitante : créer une application conversationnelle. Cette application transformera notre source de données en un partenaire de chat, vous permettant d'avoir des conversations interactives et de découvrir des informations grâce au langage naturel.

Jusqu'à présent, nous avons posé les bases de notre application. Nous avons créé :

* Une source de données.
* Un outil de récupération de données.
* Un agent.
* Des tâches.

Cliquez sur l'onglet Applications puis sur le bouton **Nouvelle Application**, puis entrez les détails ci-dessous :

![Image](https://lh7-us.googleusercontent.com/jBOcimMYi1-HQGbpUXJYFLho-5LGKGKVJJ5E9OnNpy83PzSX0RINP0DN6oK_9p9LztvSm5yQdMSDqmLqY_fvmC_3pREpO2f9h_zRmPGwaYdr9TwLmcWzWhZSRPMlWDK15x9cEdMz6gNwyL4uYnB0Pyc)
_Nouvel écran d'application_

* Nom de l'application - Entrez le nom que vous souhaitez donner à votre application.
* Entrez une description de ce que fait notre application.
* Sélectionnez une tâche.
* Sélectionnez un agent.
* Choisissez un modèle de gestion de chat - Choisissez le modèle Open AI que nous avons configuré précédemment.

![Image](https://lh7-us.googleusercontent.com/1SMFU6auHKUZgxZGUQ9yJQzKuqDwtU4KbZBJGweDPaJBW_Oc6plMrcror2o2dWindixOWu6bGyYNGg6eUB5TS2iYYmOzP9FHFIvacZTle32ZqL7Gylxxy1XlZLR9YivE3KDHBXxJ1_dvO-aVHWbc2Mo)
_Écran de l'application_

Maintenant, testons notre application.

En cliquant sur le bouton de lecture, une fenêtre de chat s'ouvrira pour nous où nous pourrons avoir une conversation.

![Image](https://lh7-us.googleusercontent.com/ju-0a5CRhaHgVEqFZkDhdlPkCBqtwOM0Mjnsaz2D7ftl5Hsfku49pkBFYyY9DBr41Rzbwqm90vf8pirBzz2hsUBnsM6YOwjPoCmGhzkm6OQefP_jNNIdOGKx9geEibQLQv_ZzGsaN8AhuXIBl-F9P64)
_Bouton de lecture dans l'écran de l'application_

Une fenêtre d'interface de chat devrait s'ouvrir pour nous où nous pouvons discuter avec nos données. Par exemple, avec les données que j'ai utilisées, je peux demander à l'application de résumer certains des problèmes soulevés par les clients liés au produit Hypothèque.

![Image](https://lh7-us.googleusercontent.com/tfEGreNRfDRwyiJs0ZomrjfRmSQajuMSYzqL-uxa8tULoso0d56mwE-JiNpLEiv0-x0dnN9XgpajdiwW9aa-dvfnF47dmhW4daQkJ21JYYmC25svAfd3PBXdm9HrmC6tVFAlZ04-H0PLf1B5GfOsqHc)
_Chat en direct avec les données_

Ou je peux lui demander de résumer les réponses des entreprises liées à différents problèmes.

![Image](https://lh7-us.googleusercontent.com/KpGoDKLffAOcUzFdN7_tJwMved1uDklnP5XQAkaLbwhn1hTlnOgI7Br8QmaPfGUgaK8hLvW958KIyZfDI577PB2aTHgSEHQjBFRN7TeOAgQA0cYjds4R5evGbuMfNXBJOl5x-7Uur0akvOsWgNjI4V4)
_Écran de réponse_

## Conclusion

Dans ce tutoriel, nous avons exploré la construction d'une application de chat RAG en utilisant Agent Cloud et Google Sheets.

Nous avons couvert la configuration de Google Sheets comme source de données, l'intégration des données pour une récupération efficace et leur stockage dans un magasin vectoriel comme Qdrant. Nous avons également appris comment créer des outils pour les agents (composants de chatbot) et construire une interface de chat d'application où les utilisateurs peuvent interagir avec les données sans écrire une seule ligne de code.

Si vous souhaitez lire plus d'articles intéressants sur les outils pour développeurs, React, Next.js, l'IA et plus encore, je vous encourage à consulter mon [blog](https://theankurtyagi.com/).

Certains des articles récents que j'ai écrits cette année.

* [Comment je construis un blog avec Next.js et Firebase](https://theankurtyagi.com/how-to-create-blog-with-nextjs-and-firebase/)
* [Comment je construis une application de gestion de tâches avec React et Appwrite](https://theankurtyagi.com/appwrite/)
* [Comment je construis une application de notes en utilisant React et Supabase - Le guide complet](https://theankurtyagi.com/notes-app-react-supabase/)
* [Comment je construis une application de chat RAG avec Agent Cloud et BigQuery](https://dev.to/agentcloud/how-to-build-a-rag-chat-app-with-agent-cloud-and-bigquery-15b)

Vous pouvez me contacter si vous avez des questions ou des corrections. Je les attends.

Et si vous avez trouvé ce tutoriel utile, veuillez le partager avec vos amis et collègues qui pourraient en bénéficier également. Votre soutien me permet de continuer à produire du contenu utile pour la communauté tech.

Maintenant, il est temps de passer à l'étape suivante en vous abonnant à ma **[newsletter](https://bytesizedbets.com/)** et en me suivant sur [**Twitter**](https://twitter.com/theankurtyagi).