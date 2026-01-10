---
title: Comment visualiser ce que vous avez tweeté
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T15:46:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualize-what-you-have-been-tweeting-81c75f00546d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c4JfsP1tnptisFAUvMMVJg.png
tags:
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment visualiser ce que vous avez tweeté
seo_desc: 'By Deepal Dsilva

  A wordcloud experiment in R


  Have you ever wondered what you tweet about the most? Or you’re attending your favorite
  conference, and you want to know what’s the buzz around it?Or perhaps you want to
  know what’s the talk about the lat...'
---

Par Deepal Dsilva

#### Une expérience de nuage de mots en R

![Image](https://cdn-media-1.freecodecamp.org/images/M4fM-FrOINbwdMvYqE8Sr3EBh9d-vgCU9S5L)

Vous êtes-vous déjà demandé ce que vous tweetez le plus souvent ? Ou vous assistez à votre conférence préférée et vous voulez savoir ce qui s'y passe ?  
Ou peut-être voulez-vous savoir de quoi on parle concernant le dernier film sorti ?

Eh bien, les nuages de mots sont ce que vous devriez utiliser. Ils sont simples à configurer, offrent des visualisations époustouflantes et sont facilement personnalisables.

### **Attendez ! Mais d'abord, qu'est-ce qu'un nuage de mots ?**

C'est une image composée de mots utilisés dans un texte ou un sujet particulier, dans laquelle la taille de chaque mot indique sa fréquence ou son importance.

Maintenant que vous connaissez les bases, commençons en R.

#### **Chargez les bibliothèques requises**

```
library(twitteR)
library(ROAuth)
library(stringr)
library(tm)
library(wordcloud2)
library(tidytext)
```

#### **Configuration de l'application Twitter**

Nous allons utiliser les données de Twitter pour construire notre nuage de mots, alors obtenez un compte Twitter si vous n'en avez pas. Je vous attends...

Ensuite, nous allons avoir besoin d'une application Twitter. C'est une configuration unique.

Vous devez vous authentifier sur Twitter afin de pouvoir envoyer une demande de tweets et afin que Twitter puisse vous les renvoyer.

Je ne vais pas entrer dans les détails des étapes. Vous pouvez utiliser [ce tutoriel](https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/) pour le configurer.

Ensuite, nous transmettons le jeton à la fonction setup_twitter_oauth pour nous authentifier.

```
consumer_key <- "xxxx"      #Votre Consumer Key (API Key)
consumer_secret <- "xxxx"   #Votre Consumer Secret (API Secret)
access_token <- "xxxx"      #Votre Access Token
access_secret <- "xxxx"     #Votre Access Token Secret
setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
```

#### **Extraction des données Twitter**

Vous pouvez extraire des tweets basés sur le profil d'un utilisateur ou sur des mots-clés/hashtags. Voici les deux exemples.

```
#Interroger un hashtag
tweets <- searchTwitter("#rstats",n=3000,lang="en", resultType = "popular")
```

```
#OU
```

```
#Interroger un utilisateur que vous suivez ou vous-même
tweets <- userTimeline("dsilvadeepal",n=3200,includeRts = FALSE)
```

#### **Fouille de texte de vos tweets**

Nous devons maintenant extraire le texte des tweets vers un vecteur.

Et nous allons d'abord supprimer les paramètres graphiques. Cela supprime les caractères visibles (tout sauf les espaces et les caractères de contrôle) pour éviter les erreurs d'entrée.

```
tweets.txt <- sapply(tweets, function(t)t$getText())
tweets.txt <- str_replace_all(tweets.txt,"[^[:graph:]]", " ")
```

Maintenant, créons une fonction pour nettoyer les tweets. Ici, nous allons supprimer les chiffres, la ponctuation, les espaces, les liens HTTP et les retweets (RTs). Vous pouvez personnaliser cette fonction en fonction des données que vous traitez.

```
clean.text = function(x){
    x = tolower(x)                   # tolower
    x = gsub("rt", "", x)            # supprimer rt
    x = gsub("@\\w+", "", x)         # supprimer at
    x = gsub("[[:punct:]]", "", x)   # supprimer ponctuation
    x = gsub("[[:digit:]]", "", x)   # supprimer nombres
    x = gsub("http\\w+", "", x)      # supprimer liens http
    x = gsub("[ |\t]{2,}", "", x)    # supprimer tabulations
    x = gsub("^ ", "", x)            # supprimer espaces vides en début
    x = gsub(" $", "", x)            # supprimer espaces vides en fin
    return(x)}
```

```
clean_tweet <- clean.text(tweets.txt)
```

Ensuite, nous construisons un Corpus. Un Corpus est une collection de documents textuels et le VectorSource pointe vers le vecteur où les tweets sont stockés.

Nous allons également créer un vecteur pour supprimer les mots vides en anglais et tout autre mot qui est irrelevant (nous identifierons ces mots dans une étape ultérieure). Certains mots vides courants en anglais sont « the », « I » et « he ».

```
tweets <- Corpus(VectorSource(clean_tweet))
wordsToRemove <- c(stopwords('en'), 'tco', 'https')
clean_tweet <- tm_map(tweets, removeWords, wordsToRemove)
```

Nous créons maintenant une Matrice de Termes Documents (TDM) qui nous indique le nombre de fois où chaque mot du corpus est trouvé.

```
dtm <- TermDocumentMatrix(clean_tweet, control = list(wordLengths = c(1, Inf)))
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 10)   #inspecter notre liste de mots et supprimer tout mot irrelevant
              #dans l'étape des mots vides ci-dessus
```

Enfin, la partie amusante !

#### **Création de notre nuage de mots**

Ici, nous allons utiliser le package WordCloud2 — c'est un package plus récent que le package WordCloud, et il offre beaucoup plus de personnalisation.

```
wordcloud2(d, shape = "triangle", color="random-light", backgroundColor = "white", minRotation = -pi/4, maxRotation = -pi/4, size = 0.5)
```

![Image](https://cdn-media-1.freecodecamp.org/images/M67dhbljBs8VnU5nWSxM6YzFXSJKc9uYISh4)

Et voilà ! Voici un lien vers le [code](https://github.com/dsilvadeepal/Data-Science/blob/master/Projects/Wordclouds/Twitter%20Wordcloud.Rmd) sur Github.

Merci d'avoir lu !

_Note : L'API Twitter limite le nombre de tweets qu'un utilisateur peut obtenir à partir d'une timeline particulière à 3200._