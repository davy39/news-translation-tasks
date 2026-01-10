---
title: Comment construire un grand modèle de langage à partir de zéro en utilisant
  Python
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-25T15:32:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-large-language-model-from-scratch-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/llmscratch.png
tags:
- name: 'LLM''s '
  slug: llms
- name: youtube
  slug: youtube
seo_title: Comment construire un grand modèle de langage à partir de zéro en utilisant
  Python
seo_desc: 'Have you ever been fascinated by the capabilities of large language models
  like GPT-4 but wondered how they are actually work?

  If you want to uncover the mysteries behind these powerful models, our latest video
  course on the freeCodeCamp.org YouTube ...'
---

Avez-vous déjà été fasciné par les capacités des grands modèles de langage comme GPT-4, mais vous êtes-vous demandé comment ils fonctionnent réellement ?

Si vous souhaitez découvrir les mystères derrière ces modèles puissants, notre dernier cours vidéo sur la chaîne YouTube de freeCodeCamp.org est parfait pour vous. Dans ce cours complet, vous apprendrez à créer votre propre grand modèle de langage à partir de zéro en utilisant Python.

Elliot Arledge a créé ce cours. Il vous enseignera la gestion des données, les concepts mathématiques et les architectures de transformateurs qui alimentent ces géants linguistiques. Elliot s'est inspiré d'un cours sur la création d'un GPT à partir de zéro développé par le cofondateur d'OpenAI, Andrej Karpathy.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-181.png)
_Vous utiliserez Jupyter Notebook pour développer le LLM._

Le cours commence par une introduction complète, posant les bases du cours. Après avoir configuré votre environnement, vous apprendrez la tokenisation au niveau des caractères et la puissance des tenseurs par rapport aux tableaux.

Ensuite, le cours passe à la création de modèles. Vous apprendrez les divisions d'entraînement et de validation, le modèle bigramme et le concept critique des entrées et des cibles. Avec des informations sur les hyperparamètres de taille de lot et un aperçu complet du framework PyTorch, vous basculerez entre le traitement CPU et GPU pour des performances optimales. Des concepts tels que les vecteurs d'embedding, les produits scalaires et la multiplication de matrices posent les bases de sujets plus avancés.

La section principale du cours offre une exploration approfondie des architectures de transformateurs. Vous parcourrez les intrications des mécanismes d'auto-attention, vous plongerez dans l'architecture du modèle GPT et acquerrez une expérience pratique dans la construction et l'entraînement de votre propre modèle GPT. Enfin, vous acquerrez de l'expérience dans des applications réelles, de l'entraînement sur le jeu de données OpenWebText à l'optimisation de l'utilisation de la mémoire et à la compréhension des nuances du chargement et de l'enregistrement de modèles.

En créant votre propre grand modèle de langage, vous obtiendrez une compréhension approfondie de leur fonctionnement. Cela vous sera bénéfique lorsque vous travaillerez avec ces modèles à l'avenir. Vous pouvez regarder [le cours complet sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/UU1WVnMk4E8) (6 heures de visionnage).

%[https://youtu.be/UU1WVnMk4E8]

Voici toutes les sections du cours :

* Introduction
* Installer les bibliothèques
* Outils de construction Pylzma
* Jupyter Notebook
* Télécharger le magicien d'Oz
* Expérimentation avec un fichier texte
* Tokeniseur au niveau des caractères
* Types de tokeniseurs
* Tenseurs au lieu de tableaux
* Rappel d'algèbre linéaire
* Divisions d'entraînement et de validation
* Prémisse du modèle Bigram
* Entrées et cibles
* Implémentation des entrées et des cibles
* Hyperparamètre de taille de lot
* Passage du CPU à CUDA
* Aperçu de PyTorch
* Performance CPU vs GPU dans PyTorch
* Plus de fonctions PyTorch
* Vecteurs d'embedding
* Implémentation d'embedding
* Produit scalaire et multiplication de matrices
* Implémentation de Matmul
* Int vs Float
* Récapitulatif et get_batch
* Sous-classe nnModule
* Descente de gradient
* Logits et remodelage
* Fonction de génération et donner un contexte au modèle
* Dimensionnalité des logits
* Boucle d'entraînement + Optimiseur + Explication de Zerograd
* Aperçu des optimiseurs
* Applications des optimiseurs
* Rapport de perte + Mode d'entraînement vs Évaluation
* Aperçu de la normalisation
* Activations ReLU, Sigmoid, Tanh
* Transformateur et auto-attention
* Architecture du transformateur
* Construction d'un GPT, pas de modèle de transformateur
* Plongée profonde dans l'auto-attention
* Architecture GPT
* Passage à Macbook
* Implémentation de l'encodage positionnel
* Initialisation de GPTLanguageModel
* Passe avant de GPTLanguageModel
* Écart type pour les paramètres du modèle
* Blocs de transformateur
* Réseau FeedForward
* Attention multi-têtes
* Attention par produit scalaire
* Pourquoi nous mettons à l'échelle par 1/sqrt(dk)
* Traitement séquentiel vs ModuleList
* Aperçu des hyperparamètres
* Correction des erreurs, affinement
* Début de l'entraînement
* Téléchargement d'OpenWebText et étude des LLMs
* Comment le chargeur de données/l'obtention de lots devra changer
* Extraire le corpus avec winrar
* Extracteur de données Python
* Ajustement pour les divisions d'entraînement et de validation
* Ajout du chargeur de données
* Entraînement sur OpenWebText
* L'entraînement fonctionne bien, chargement/enregistrement du modèle
* Pickling
* Correction des erreurs + Mémoire GPU dans le gestionnaire de tâches
* Analyse des arguments de la ligne de commande
* Portage du code vers un script
* Fonctionnalité de complétion de prompt + plus d'erreurs
* Héritage de nnModule + rognage de génération
* Pré-entraînement vs Affinage
* Pointeurs R&D
* Outro