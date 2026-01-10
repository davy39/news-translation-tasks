---
title: 'Comment les agents IA se souviennent des choses : Le rôle des bases de données
  vectorielles dans la mémoire des LLM'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-07-17T14:08:19.791Z'
originalURL: https://freecodecamp.org/news/how-ai-agents-remember-things-vector-stores-in-llm-memory
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747753163050/26574896-6da9-4a30-af4f-1d0b7f38f43b.png
tags:
- name: AI
  slug: ai
- name: Machine Learning
  slug: machine-learning
- name: llm
  slug: llm
- name: memory-management
  slug: memory-management
- name: technology
  slug: technology
seo_title: 'Comment les agents IA se souviennent des choses : Le rôle des bases de
  données vectorielles dans la mémoire des LLM'
seo_desc: 'When you talk to an AI assistant, it can feel like it remembers what you
  said before.

  But large language models (LLMs) don’t actually have memory on their own. They don’t
  remember conversations unless that information is given to them again.

  So, how ...'
---

Lorsque vous parlez à un assistant IA, cela peut donner l'impression qu'il se souvient de ce que vous avez dit auparavant.

Mais les grands modèles de langage (LLM) n'ont pas réellement de mémoire par eux-mêmes. Ils ne se souviennent pas des conversations à moins que ces informations ne leur soient à nouveau fournies.

Alors, comment semblent-ils se rappeler des choses ?

La réponse réside dans quelque chose appelé une base de données vectorielle – et c'est ce que vous apprendrez dans cet article.

## **Table des matières**

* [Qu'est-ce qu'une base de données vectorielle ?](#heading-qu-est-ce-qu-une-base-de-données-vectorielle)
    
* [Comment fonctionnent les embeddings](#heading-comment-fonctionnent-les-embeddings)
    
* [Pourquoi les bases de données vectorielles sont cruciales pour la mémoire](#heading-pourquoi-les-bases-de-données-vectorielles-sont-cruciales-pour-la-mémoire)
    
* [Bases de données vectorielles populaires](#heading-bases-de-données-vectorielles-populaires)
    
    * [FAISS (Facebook AI Similarity Search)](#heading-faiss-facebook-ai-similarity-searchhttpsaimetacomtoolsfaiss)
        
    * [Pinecone](#heading-pineconehttpswwwpineconeio)
        
* [Rendre l'IA intelligente avec la génération augmentée par récupération](#heading-rendre-l-ia-intelligente-avec-la-génération-augmentée-par-récupération)
    
* [Les limites de la mémoire basée sur les vecteurs](#heading-les-limites-de-la-mémoire-basée-sur-les-vecteurs)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce qu'une base de données vectorielle ?**

Une base de données vectorielle est un type spécial de base de données. Au lieu de stocker du texte ou des nombres comme une base de données classique, elle stocke des vecteurs.

Un vecteur est une liste de nombres qui représente le sens d'un morceau de texte. Vous obtenez ces vecteurs en utilisant un processus appelé embedding.

Le modèle prend une phrase et la transforme en un point de haute dimension dans l'espace. Dans cet espace, les significations similaires sont proches les unes des autres.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746419405154/214a0566-8dc6-4402-a0f1-e30f8d81003c.png align="center")

Par exemple, si j'embedding "J'adore les sushis", cela pourrait être proche de "Les sushis sont ma nourriture préférée" dans l'espace vectoriel. Ces embeddings aident un agent IA à trouver des pensées liées même si les mots exacts diffèrent.

## **Comment fonctionnent les embeddings**

Supposons qu'un utilisateur dise à un assistant :

```plaintext
"Je vis à Austin, au Texas."
```

Le modèle transforme cette phrase en un vecteur :

```plaintext
[0.23, -0.41, 0.77, ..., 0.08]
```

Ce vecteur ne signifie pas grand-chose pour nous, mais pour l'IA, c'est un moyen de capturer le sens de la phrase. Ce vecteur est stocké dans une base de données vectorielle, avec quelques informations supplémentaires – peut-être un horodatage ou une note indiquant qu'il provient de cet utilisateur.

Plus tard, si l'utilisateur dit :

```plaintext
"Réservez un vol pour ma ville natale."
```

Le modèle transforme cette nouvelle phrase en un nouveau vecteur. Il recherche ensuite dans la base de données vectorielle les vecteurs stockés les plus similaires.

La correspondance la plus proche pourrait être "Je vis à Austin, au Texas." Maintenant, l'IA sait ce que vous vouliez probablement dire par "ma ville natale".

Cette capacité à rechercher des entrées passées liées en fonction du sens – et non pas seulement des mots-clés correspondants – est ce qui donne aux LLM une forme de mémoire.

## **Pourquoi les bases de données vectorielles sont cruciales pour la mémoire**

Les LLM traitent le langage en utilisant une fenêtre de contexte. C'est la quantité de texte qu'ils peuvent "voir" à la fois.

Pour GPT-4-turbo, la fenêtre peut gérer jusqu'à 128 000 tokens, ce qui semble énorme – mais même cela se remplit rapidement. Vous ne pouvez pas garder toute la conversation là pour toujours.

Au lieu de cela, vous utilisez une base de données vectorielle comme mémoire à long terme. Vous embedding et sauvegardez les informations utiles.

Ensuite, lorsque nécessaire, vous interrogez la base de données vectorielle, récupérez les éléments les plus pertinents et les réinjectez dans le LLM. De cette façon, le modèle se souvient juste assez pour agir de manière intelligente – sans tout garder dans sa mémoire à court terme.

## **Bases de données vectorielles populaires**

Il existe plusieurs bases de données vectorielles populaires en usage. Chacune a ses forces.

### [FAISS (Facebook AI Similarity Search)](https://ai.meta.com/tools/faiss)

FAISS est une bibliothèque open-source développée par Meta. Elle est rapide et fonctionne bien pour les applications locales ou sur site.

FAISS est idéale si vous voulez un contrôle total et n'avez pas besoin d'hébergement cloud. Elle supporte des millions de vecteurs et fournit des outils pour l'indexation et la recherche avec des performances élevées.

Voici comment vous pouvez utiliser FAISS :

```plaintext
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
```

```plaintext
# Charger un modèle de transformation de phrases pré-entraîné qui convertit les phrases en vecteurs numériques (embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Définir la phrase d'entrée que nous voulons stocker en mémoire
sentence = "L'utilisateur vit à Austin, au Texas"

# Convertir la phrase en un vecteur dense (embedding)
embedding = model.encode(sentence)

# Obtenir la dimensionnalité du vecteur d'embedding (nécessaire pour créer l'index FAISS)
dimension = embedding.shape[0]

# Créer un index FAISS pour la recherche de similarité L2 (Euclidienne) en utilisant la dimension de l'embedding
index = faiss.IndexFlatL2(dimension)

# Ajouter l'embedding de la phrase à l'index FAISS (c'est notre "mémoire")
index.add(np.array([embedding]))

# Encoder une nouvelle phrase de requête que nous voulons faire correspondre à la mémoire stockée
query = model.encode("D'où vient l'utilisateur ?")

# Rechercher dans l'index FAISS le vecteur le plus similaire à la requête
D, I = index.search(np.array([query]), k=1)

# Imprimer l'index de la mémoire la plus pertinente (dans ce cas, un seul élément dans l'index)
print("Index de la mémoire la plus pertinente :", I[0][0])
```

Ce code utilise un modèle pré-entraîné pour transformer une phrase comme "L'utilisateur vit à Austin, au Texas" en un embedding.

Il stocke cet embedding dans un index FAISS. Lorsque vous posez une question comme "D'où vient l'utilisateur ?", le code convertit cette question en un autre embedding et recherche dans l'index pour trouver la phrase stockée qui est la plus similaire en sens.

Enfin, il imprime la position (index) de la phrase la plus pertinente dans la mémoire.

FAISS est efficace, mais il n'est pas hébergé. Cela signifie que vous devez gérer votre propre infrastructure.

### [Pinecone](https://www.pinecone.io)

Pinecone est une base de données vectorielle native cloud. Elle est gérée pour vous, ce qui la rend idéale pour les systèmes de production.

Vous n'avez pas à vous soucier de la mise à l'échelle ou de la maintenance des serveurs. Pinecone gère des milliards de vecteurs et offre des fonctionnalités de filtrage, de support de métadonnées et des requêtes rapides. Il s'intègre bien avec des outils comme LangChain et OpenAI.

Voici comment fonctionne une configuration de base de Pinecone :

```plaintext
import pinecone
from sentence_transformers import SentenceTransformer
```

```plaintext
# Initialiser Pinecone avec votre clé API et votre environnement
pinecone.init(api_key="votre-clé-api", environment="us-west1-gcp")

# Se connecter à ou créer un index Pinecone nommé "memory-store"
index = pinecone.Index("memory-store")

# Charger un modèle de transformation de phrases pré-entraîné pour convertir le texte en embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convertir un fait/une phrase en un embedding numérique (vecteur)
embedding = model.encode("L'utilisateur préfère la nourriture végétarienne")

# Stocker (upsert) l'embedding dans Pinecone avec un ID unique
index.upsert([("user-pref-001", embedding.tolist())])

# Encoder la phrase de requête en un embedding
query = model.encode("Quel type de nourriture l'utilisateur aime-t-il ?")

# Rechercher dans Pinecone l'embedding stocké le plus pertinent pour la requête
results = index.query(queries=[query.tolist()], top_k=1)

# Imprimer l'ID de la mémoire la plus correspondante
print("ID de la meilleure correspondance :", results['matches'][0]['id'])
```

Pinecone est idéal si vous voulez une scalabilité et une facilité d'utilisation sans gérer le matériel.

D'autres bases de données vectorielles populaires incluent :

* [**Weaviate**](https://weaviate.io) – Combine la recherche vectorielle avec des graphes de connaissances. Offre une recherche sémantique forte avec un support hybride de mots-clés.
    
* [**Chroma**](https://www.trychroma.com) – Simple à utiliser et bon pour le prototypage. Souvent utilisé dans les applications personnelles ou les démonstrations.
    
* [**Qdrant**](https://qdrant.tech) – Open-source et conçu pour la recherche vectorielle haute performance avec filtrage.
    

Chacune de ces solutions a sa place en fonction de vos besoins en termes de vitesse, d'échelle, de simplicité ou de fonctionnalités spéciales.

## **Rendre l'IA intelligente avec la génération augmentée par récupération**

Ce système entier – embedding des entrées utilisateur, les stocker dans une base de données vectorielle et les récupérer plus tard – est appelé [génération augmentée par récupération (RAG)](https://www.freecodecamp.org/news/retrieval-augmented-generation-rag-handbook/).

L'IA n'a toujours pas de cerveau, mais elle peut agir comme si elle en avait un. Vous choisissez ce dont vous voulez vous souvenir, quand le rappeler et comment le réinjecter dans la conversation.

Si l'IA aide un utilisateur à suivre les mises à jour de projet, vous pouvez stocker chaque détail de projet sous forme de vecteur. Lorsque l'utilisateur demande plus tard, "Quel est l'état de la phase de conception ?", vous recherchez dans votre base de données de mémoire, récupérez les notes les plus pertinentes et laissez le LLM les assembler en une réponse utile.

## **Les limites de la mémoire basée sur les vecteurs**

Bien que les bases de données vectorielles donnent aux agents IA un moyen puissant de simuler la mémoire, cette approche présente certaines limites importantes.

La recherche vectorielle est basée sur la similarité, et non sur une véritable compréhension. Cela signifie que l'embedding stocké le plus similaire peut ne pas toujours être le plus pertinent ou utile dans le contexte. Par exemple, deux phrases peuvent être mathématiquement proches dans l'espace vectoriel mais porter des significations très différentes. En conséquence, l'IA peut parfois produire des résultats confus ou hors sujet, surtout lorsque la nuance ou le ton émotionnel est impliqué.

Un autre défi est que les embeddings sont des instantanés statiques. Une fois stockés, ils n'évoluent ni ne s'adaptent à moins d'être explicitement mis à jour. Si un utilisateur change d'avis ou fournit de nouvelles informations, le système ne "apprendra" pas à moins que le vecteur original ne soit supprimé ou remplacé. Contrairement à la mémoire humaine, qui s'adapte et se raffine avec le temps, la mémoire basée sur les vecteurs est figée à moins que les développeurs ne la gèrent activement.

Il existe quelques moyens de mitiger ces défis.

L'un consiste à inclure plus de contexte dans le processus de récupération, comme le filtrage des résultats par métadonnées telles que les horodatages, les sujets ou l'intention de l'utilisateur. Cela aide à réduire les résultats à ce qui est vraiment pertinent à ce moment-là.

Une autre approche consiste à retraiter ou à ré-embedding les anciennes mémoires périodiquement, en s'assurant que les informations reflètent la compréhension la plus récente des besoins ou des préférences de l'utilisateur.

Au-delà des limites techniques, les bases de données vectorielles soulèvent également des préoccupations en matière de confidentialité et d'éthique. Les questions clés sont : Qui décide de ce qui est sauvegardé ? Combien de temps cette mémoire doit-elle persister ? Et l'utilisateur a-t-il le contrôle sur ce qui est retenu ou oublié ?

Idéalement, ces décisions ne doivent pas être prises uniquement par le développeur ou le système. Une approche plus réfléchie consiste à rendre la mémoire explicite. Laissez les utilisateurs choisir ce qui est retenu. Par exemple, en marquant certaines entrées comme "importantes", cela ajoute une couche de consentement et de transparence. De même, la rétention de la mémoire doit être limitée dans le temps lorsque cela est approprié, avec des politiques d'expiration basées sur la durée pendant laquelle l'information reste utile.

Tout aussi important est la capacité pour les utilisateurs de visualiser, gérer ou supprimer leurs données stockées. Que ce soit par le biais d'une interface simple ou d'une API programmatique, les outils de gestion de la mémoire sont essentiels pour la confiance. À mesure que l'utilisation des bases de données vectorielles se développe, l'attente que les systèmes d'IA respectent l'agence et la confidentialité des utilisateurs augmente également.

La communauté IA plus large façonne encore les meilleures pratiques autour de ces questions. Mais une chose est claire : la mémoire simulée doit être conçue non seulement pour la précision et la performance, mais aussi pour la responsabilité. En combinant des paramètres forts avec le contrôle de l'utilisateur, les développeurs peuvent s'assurer que les systèmes de mémoire basés sur les vecteurs sont à la fois intelligents et responsables.

## **Conclusion**

Les bases de données vectorielles donnent aux agents IA un moyen de simuler la mémoire – et ils le font bien. En embedding du texte en vecteurs et en utilisant des outils comme FAISS ou Pinecone, nous donnons aux modèles le pouvoir de rappeler ce qui compte. Ce n'est pas une vraie mémoire. Mais cela rend les systèmes d'IA plus personnels, plus utiles et plus humains.

À mesure que ces outils deviennent plus avancés, l'illusion grandit également. Mais derrière chaque IA intelligente se cache un système simple de vecteurs et de similarité. Si vous pouvez maîtriser cela, vous pouvez construire des assistants qui se souviennent, apprennent et s'améliorent avec le temps.

J'espère que vous avez apprécié cet article. [**Connectez-vous avec moi sur LinkedIn**.](https://www.linkedin.com/in/manishmshiva/)