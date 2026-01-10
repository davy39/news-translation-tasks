---
title: Comment convertir de l'audio en texte en utilisant OpenAI Whisper
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-03-05T13:02:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-turn-audio-to-text-using-openai-whisper
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Untitled-design-26-1068x601.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: openai
  slug: openai
seo_title: Comment convertir de l'audio en texte en utilisant OpenAI Whisper
seo_desc: 'Do you know what OpenAI Whisper is? It’s the latest AI model from OpenAI
  that helps you to automatically convert speech to text.

  Transforming audio into text is now simpler and more accurate, thanks to OpenAI’s
  Whisper.

  This article will guide you th...'
---

Savez-vous ce qu'est OpenAI Whisper ? Il s'agit du dernier modèle d'IA d'OpenAI qui vous aide à convertir automatiquement la parole en texte.

Transformer l'audio en texte est désormais plus simple et plus précis, grâce à Whisper d'OpenAI.

Cet article vous guidera à travers l'utilisation de Whisper pour convertir des mots parlés en forme écrite, offrant une approche simple pour toute personne souhaitant utiliser l'IA pour une transcription efficace.

# Introduction à OpenAI Whisper

[OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text) est un modèle d'IA conçu pour comprendre et transcrire le langage parlé. Il s'agit d'un système de reconnaissance automatique de la parole (ASR) conçu pour convertir le langage parlé en texte écrit.

Ses capacités ont ouvert un large éventail de cas d'utilisation dans divers secteurs. Que vous soyez un développeur, un créateur de contenu ou simplement quelqu'un fasciné par l'IA, Whisper a quelque chose pour vous.

Passons en revue certaines de ses principales caractéristiques :

**1. Services de transcription :** Whisper peut transcrire du contenu audio et vidéo en temps réel ou à partir d'enregistrements, ce qui le rend utile pour générer des comptes rendus de réunion précis, des interviews, des conférences et tout contenu parlé qui doit être documenté sous forme de texte.

**2. Sous-titrage et sous-titres codés :** Il peut générer automatiquement des sous-titres et des sous-titres codés pour les vidéos, améliorant l'accessibilité pour les personnes sourdes et malentendantes, ainsi que pour les spectateurs qui préfèrent regarder des vidéos avec du texte.

**3. Apprentissage des langues et traduction :** La capacité de Whisper à transcrire dans plusieurs langues soutient les applications d'apprentissage des langues, où il peut aider à la pratique de la prononciation et à la compréhension orale. Combiné à des modèles de traduction, il peut également faciliter la communication interlinguistique en temps réel.

**4. Outils d'accessibilité :** Au-delà du sous-titrage, Whisper peut être intégré dans des technologies d'assistance pour aider les personnes ayant des troubles de la parole ou celles qui dépendent de la communication basée sur le texte. Il peut convertir des commandes ou des requêtes vocales en texte pour un traitement ultérieur, améliorant l'utilisabilité des appareils et des logiciels pour tous.

**5. Recherche de contenu :** En transcriant le contenu audio et vidéo en texte, Whisper permet de rechercher dans de vastes quantités de données multimédias. Cette capacité est cruciale pour les entreprises de médias, les institutions éducatives et les professionnels du droit qui doivent trouver des informations spécifiques de manière efficace.

**6. Applications contrôlées par la voix :** Whisper peut servir de base au développement d'applications et d'appareils contrôlés par la voix. Il permet aux utilisateurs d'interagir avec la technologie par le biais de la parole naturelle. Cela inclut tout, des appareils domestiques intelligents aux machines industrielles complexes.

**7. Automatisation du support client :** Dans le service client, Whisper peut transcrire les appels en temps réel. Il permet une analyse et une réponse immédiates des systèmes automatisés. Cela peut améliorer les temps de réponse, la précision dans le traitement des requêtes et la satisfaction globale des clients.

**8. Podcasting et journalisme :** Pour les podcasteurs et les journalistes, Whisper offre un moyen rapide de transcrire des interviews et du contenu audio pour des articles, des blogs et des publications sur les réseaux sociaux, rationalisant la création de contenu et le rendant accessible à un public plus large.

OpenAI's Whisper représente une avancée significative dans la technologie de reconnaissance vocale.

Avec ses cas d'utilisation s'étendant à l'amélioration de l'accessibilité, à la rationalisation des flux de travail et à la promotion d'applications innovantes dans la technologie, c'est un outil puissant pour construire des applications modernes.

## Comment travailler avec Whisper

Maintenant, examinons un exemple de code simple pour convertir un fichier audio en texte en utilisant Whisper d'OpenAI. Je recommande d'utiliser un [Google Collab notebook](https://colab.research.google.com/).

Avant de plonger dans le code, vous avez besoin de deux choses :

1. [Clé API OpenAI](https://platform.openai.com/api-keys)
2. [Fichier audio d'exemple](https://audio-samples.github.io/)

Tout d'abord, installez la bibliothèque OpenAI (Utilisez `!` uniquement si vous l'installez sur le notebook) :

```
!pip install openai
```

Maintenant, écrivons le code pour transcrire un fichier de parole d'exemple en texte :

```
# Importer la bibliothèque openai
from openai import OpenAI

# Créer un client api
client = OpenAI(api_key="VOTRE_CLE_ICI")

# Charger le fichier audio
audio_file = open("CHEMIN_FICHIER_AUDIO", "rb")

# Transcrire
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# Imprimer le texte transcrit
print(transcription.text)
```

Ce script montre une manière simple d'utiliser OpenAI Whisper pour transcrire des fichiers audio. En exécutant ce script avec Python, vous verrez la transcription de votre fichier audio spécifié imprimée dans la console.

N'hésitez pas à expérimenter avec différents fichiers audio et à explorer les options supplémentaires fournies par la [Bibliothèque Whisper](https://platform.openai.com/docs/guides/speech-to-text) pour personnaliser le processus de transcription selon vos besoins.

## Conseils pour de meilleures transcriptions

Whisper est puissant, mais il existe des moyens d'obtenir encore de meilleurs résultats. Voici quelques conseils :

1. **Audio clair :** Plus votre fichier audio est clair, meilleure est la transcription. Essayez d'utiliser des fichiers avec un minimum de bruit de fond.
2. **Sélection de la langue :** Whisper prend en charge plusieurs langues. Si votre audio n'est pas en anglais, assurez-vous de spécifier la langue pour une meilleure précision.
3. **Personnalisation de la sortie :** Whisper offre des options pour personnaliser la sortie. Vous pouvez lui demander d'inclure des horodatages, des scores de confiance, et plus encore. Explorez la documentation pour voir ce qui est possible.

## Fonctionnalités avancées

Whisper n'est pas seulement pour les transcriptions simples. Il possède des fonctionnalités qui répondent à des besoins plus avancés :

1. **Transcription en temps réel :** Vous pouvez configurer Whisper pour transcrire l'audio en temps réel. Cela est idéal pour les événements en direct ou le streaming.
2. **Support multilingue :** Whisper peut gérer plusieurs langues dans le même fichier audio. Il est parfait pour les réunions ou les interviews multilingues.
3. **Ajustement fin :** Si vous avez des besoins spécifiques, vous pouvez ajuster finement les modèles de Whisper pour mieux les adapter à votre audio. Cela nécessite plus de compétences techniques mais peut améliorer considérablement les résultats.

## Conclusion

Travailler avec OpenAI Whisper ouvre un monde de possibilités. Il ne s'agit pas seulement de transcrire de l'audio, mais de rendre l'information plus accessible et les processus plus efficaces.

Que vous transcribiez des interviews pour un projet de recherche, que vous rendiez votre podcast plus accessible avec des transcriptions, ou que vous exploriez de nouvelles façons d'interagir avec la technologie, Whisper vous couvre.

J'espère que vous avez apprécié cet article. [Visitez turingtalks.ai](https://www.turingtalks.ai/) pour des tutoriels quotidiens sur l'IA en petits morceaux.