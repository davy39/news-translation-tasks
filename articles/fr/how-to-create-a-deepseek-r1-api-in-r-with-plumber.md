---
title: Comment créer une API DeepSeek R1 en R avec Plumber
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2025-02-20T23:22:01.999Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-deepseek-r1-api-in-r-with-plumber
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740093558918/453118b9-3c93-4e57-a1ad-7471e1046ef1.png
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Deep Learning
  slug: deep-learning
- name: APIs
  slug: apis
seo_title: Comment créer une API DeepSeek R1 en R avec Plumber
seo_desc: 'To create an AI chatbot and integrate it with another platform, you have
  to communicate with large language model using an API. This API receives prompts
  from the client and sends them to the model to generate answers.

  In this tutorial, you will lear...'
---

Pour créer un chatbot IA et l'intégrer avec une autre plateforme, vous devez communiquer avec un grand modèle de langage en utilisant une API. Cette API reçoit des prompts du client et les envoie au modèle pour générer des réponses.

Dans ce tutoriel, vous apprendrez à créer une telle API en utilisant le grand modèle de langage DeepSeek R1 afin que des applications externes puissent l'appeler. Nous utiliserons le [modèle DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1), disponible sur HuggingFace, et le package R Plumber pour le déployer en tant qu'API.

HuggingFace est une plateforme open source pour construire, entraîner et déployer des modèles de machine learning, tandis que Plumber est un package R qui expose le code R en tant qu'API RESTful accessibles à d'autres applications via des requêtes HTTP.

Avec cette API, vous pouvez :

* Construire des applications IA

* Vous connecter à des données externes et extraire des informations significatives

* Vous intégrer dans des applications existantes pour fournir un support client, créer des documentations, etc.

## Qu'est-ce que le modèle DeepSeek R1 ?

DeepSeek R1 est le dernier grand modèle de langage de l'entreprise chinoise [DeepSeek](https://www.deepseek.com/). Il a été conçu pour améliorer les capacités de résolution de problèmes et d'analyse des systèmes IA.

DeepSeek-R1 utilise l'apprentissage par renforcement et le fine-tuning supervisé pour gérer des tâches de raisonnement complexes. Contrairement aux modèles propriétaires, DeepSeek R1 est open-source et gratuit à utiliser.

## Prérequis

* Inscrivez-vous pour un [compte HuggingFace](https://huggingface.co/) si vous n'en avez pas déjà un

* Installez [R et R Studio](https://posit.co/download/rstudio-desktop/).

* Installez le package R [`plumber`](https://www.rplumber.io/) pour construire le point de terminaison de l'API

* Installez le package R [`httr2`](https://httr2.r-lib.org/) pour travailler avec les requêtes HTTP et interagir avec l'API Hugging Face

## Étape 1 : Créez votre dépôt de projet

Vous devez créer un projet R pour créer une application API en R. Cela garantit que tous les fichiers nécessaires pour maintenir votre API en fonctionnement sont conservés ensemble sous le même répertoire. R Studio dispose déjà d'un modèle fourni pour les projets API, vous pouvez donc suivre les étapes ci-dessous pour créer le vôtre.

Dans votre IDE R Studio, cliquez sur le menu Fichier et allez dans Nouveau Projet pour ouvrir l'Assistant Nouveau Projet. Une fois dans l'assistant, sélectionnez Nouveau Répertoire, puis cliquez sur Nouveau Projet API Plumber. Dans le champ nom du répertoire, donnez-lui un nom (par exemple `DeepSeek-R1 API`), puis cliquez sur Créer le Projet.

Vous verrez un fichier appelé `plumber.R` avec un modèle d'API d'exemple. C'est là que vous écrirez le code pour vous connecter au modèle DeepSeek R1 sur HuggingFace. Assurez-vous de vider ce modèle avant de continuer.

![GIF montrant comment créer un nouveau projet Plumber dans R](https://cdn.hashnode.com/res/hashnode/image/upload/v1738503866976/60b959cd-b564-486d-8b65-c9ca0278e239.gif align="center")

Ensuite, allez dans votre terminal et créez un fichier `.env`. C'est là que vous stockerez la clé API Hugging Face.

```plaintext
touch .env
```

![Image montrant comment créer une variable .env sur le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504109388/6ce9bda3-305a-4f2e-87b8-adbe4c245861.png align="center")

Créez un fichier `.gitignore` et ajoutez le fichier `.env` à celui-ci. Cela garantit que les informations sensibles comme les jetons d'accès et les clés API ne sont pas poussées vers votre dépôt Git.

![Image montrant le fichier .env dans le fichier .gitignore](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504889229/0d433bcb-2a7d-4379-a0c7-e09fb53e288f.png align="center")

## Étape 2 : Créez un jeton d'accès Hugging Face

Nous devons créer un jeton d'accès pour nous connecter aux modèles Hugging Face. Allez dans votre profil, cliquez sur Paramètres, puis cliquez sur Créer un nouveau jeton pour créer votre jeton d'accès pour le dépôt Hugging Face.

![Image montrant la page des jetons d'accès, avec des options pour créer un nouveau jeton](https://cdn.hashnode.com/res/hashnode/image/upload/v1738504360986/077a2778-d790-4ff9-94e1-c2c372b2efef.png align="center")

Copiez le jeton d'accès et collez-le dans votre fichier `.env`, et donnez-lui le nom `HUGGINGFACE_ACCESS_TOKEN`.

```plaintext
HUGGINGFACE_ACCESS_TOKEN="<votre-jeton-d-acces>"
```

Ensuite, installez le package `dotenv`, et collez le code suivant en haut de votre fichier `plumber.R` :

```r
# Charge les variables d'environnement depuis .env
dotenv::load_dot_env()
```

`dotenv::load_dot_env()` charge toutes les variables d'environnement dans le fichier `.env`, les rendant disponibles pour le script `plumber.R`.

## Étape 3 : Construisez le point de terminaison de l'API DeepSeek

Maintenant que nous avons notre environnement de projet configuré et notre jeton API prêt, nous allons écrire le code pour construire l'application API en nous connectant au modèle DeepSeek R1 sur HuggingFace.

Allez dans le fichier `plumber.R` et chargez les bibliothèques suivantes :

```r
library(plumber)
library(httr2)
```

Copiez et collez le code suivant dans `plumber.R` :

```r

api_key <- Sys.getenv("HUGGINGFACE_ACCESS_TOKEN")



#* @post /deepseek_chat
function(prompt) {
  url <- "https://huggingface.co/api/inference-proxy/together/v1/chat/completions"

  # Crée un objet de requête
  req <- request(url) |>
    req_auth_bearer_token(api_key) |>
    req_body_json(list(
      model = "deepseek-ai/DeepSeek-R1",
      messages = list(
        list(role = "user", content = prompt)
      ),
      max_tokens = 500,
      stream = FALSE
    ))

  # Exécute la requête et capture la réponse
  res <- req_perform(req)

  # Analyse la réponse JSON
  parsed_data <- res |>
    resp_body_json()

  # Extrait le contenu de la réponse
  content <- parsed_data$choices
  return(content)
}
```

Voici ce qui se passe dans le code ci-dessus :

* `Sys.getenv` obtient le jeton d'accès HuggingFace et le stocke dans la variable `access_token`.

* La variable `url` contient le lien API pour accéder au modèle DeepSeek sur HuggingFace. Vous pouvez obtenir cela en recherchant le nom du modèle `deepseek-ai/DeepSeek-R1` sur HuggingFace. Allez sur le bouton **View Code**, et sous l'onglet **cURL**, copiez l'URL de l'API

![GIF montrant comment copier l'URL de l'API que vous allez utiliser dans votre code d'API plumber](https://cdn.hashnode.com/res/hashnode/image/upload/v1739177037117/0781bce2-7bf8-411d-ad71-cb2bf11fe1bb.gif align="left")

* `#* @post /deepseek_chat` signifie que le point de terminaison fait une requête POST via le chemin `/deepseek_chat`.

* Ce point de terminaison prend un argument `prompt`, un texte, ou une question qu'un utilisateur est censé donner.

* L'objet `req` est une chaîne de diverses opérations, qui fait une `request()` à l'`url`, puis prend la `api_key` à l'intérieur de la fonction `req_auth_bearer_token()`. Les propriétés du modèle telles que le nom du `model`, `role`, `prompt`, et `max_tokens` sont passées à l'objet `req` via la fonction `req_body_json`.

* La variable `headers` contient l'autorisation requise pour faire une requête à l'API HuggingFace.

* La requête est exécutée et capturée dans un objet de réponse `res` en utilisant la fonction `req_perform()`.

* L'objet `res` retourne un objet JSON, qui est maintenant analysé en R en utilisant la fonction `resp_body_json()`.

* Le `content` de `parsed_data` est maintenant retourné afin que vous puissiez extraire les informations dont vous avez besoin de l'application pour laquelle vous souhaitez utiliser l'API.

## Étape 4 : Testez le point de terminaison de l'API

Exécutons le point de terminaison de l'API pour voir comment l'application se comporte. Cliquez sur Run API. Cela ouvrira automatiquement le point de terminaison de l'API dans votre navigateur à l'URL [`http://127.0.0.1:8634/docs/`](http://127.0.0.1:8634/docs/).

![Image montrant le bouton Run API](https://cdn.hashnode.com/res/hashnode/image/upload/v1739282692303/82a029ea-31f5-4088-9e72-2fe1b69d0f7d.png align="center")

Cliquez sur le menu déroulant du point de terminaison de l'API, fournissez un prompt, et cliquez sur le bouton Execute. Vous devriez recevoir une réponse en quelques minutes.

![Image montrant comment le point de terminaison de l'API retourne une réponse lorsqu'un prompt est donné](https://cdn.hashnode.com/res/hashnode/image/upload/v1739282620577/b1a52679-b397-4d82-af56-0f81ebc5888e.gif align="center")

## Conclusion

Avec votre API, vous pouvez faire des inférences vers le modèle Hugging Face et construire des applications IA en R ou dans d'autres langages de programmation. Vous devez héberger votre API pour la rendre accessible aux clients en ligne. Il existe diverses [façons d'héberger une application R Plumber](https://www.rplumber.io/articles/hosting.html) : vous pouvez utiliser Docker ou l'héberger sur DigitalOcean en utilisant le package R plumberDeploy. Cependant, la manière la plus simple et la plus facile est d'utiliser [Posit Connect](https://posit.co/products/enterprise/connect/).

Vous pouvez utiliser la même approche utilisée dans ce tutoriel pour essayer d'autres modèles HuggingFace, construire une API pour générer des images ou traduire différentes langues. R Plumber est facile à utiliser, et la documentation fournit de nombreuses ressources.

Si vous êtes intéressé par le déploiement de modèles en utilisant R Plumber, vous pouvez consulter [cet article](https://learndata.xyz/posts/forecasting%20time%20series%20data%20with%20facebook%20prophet/) sur la façon de déployer un modèle de séries temporelles construit sur Prophet en utilisant R Plumber.

Si vous trouvez cet article intéressant, veuillez consulter mes autres articles sur [learndata.xyz](https://learndata.xyz/blog).