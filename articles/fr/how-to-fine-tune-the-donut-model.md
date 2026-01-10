---
title: Comment affiner le modèle Donut – Avec un cas d'utilisation exemple
subtitle: ''
author: Eivind Kjosbakken
co_authors: []
series: null
date: '2023-09-12T17:59:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-fine-tune-the-donut-model
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/undraw_Dashboard_re_3b76-4.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment affiner le modèle Donut – Avec un cas d'utilisation exemple
seo_desc: "The Donut model in Python is a model you can use to extract text from a\
  \ given image. This can be useful in various scenarios, like scanning receipts,\
  \ for example. \nYou can easily download the Donut model from GitHub. But as is\
  \ common with AI models, ..."
---

Le modèle Donut en Python est un modèle que vous pouvez utiliser pour extraire du texte d'une image donnée. Cela peut être utile dans divers scénarios, comme la numérisation de reçus, par exemple. 

Vous pouvez facilement télécharger le [modèle Donut depuis GitHub](https://github.com/clovaai/donut). Mais comme c'est courant avec les modèles d'IA, vous devriez affiner le modèle pour vos besoins spécifiques. 

J'ai écrit ce tutoriel parce que je n'ai pas trouvé de ressources me montrant exactement comment affiner le modèle Donut avec mon jeu de données. J'ai donc dû apprendre cela à partir d'autres tutoriels (que je partagerai tout au long de ce guide) et résoudre les problèmes moi-même. 

Ces problèmes étaient particulièrement fréquents car je n'avais pas de GPU sur mon ordinateur local. Pour simplifier le processus pour les autres, j'ai créé ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img1.png)
_Extraire des informations à partir de reçus. L'image a été prise depuis [ce fichier Google Colab](https://colab.research.google.com/drive/1NMSqoIZ_l39wyRD7yVjw2FIuU2aglzJi?usp=sharing#scrollTo=f7RoSOEXUa6i" rel="noopener) en utilisant une photo prise par moi_

### Voici ce que nous allons couvrir :

* Comment trouver un jeu de données pour l'affinage
* Affinage avec Google Colab
* Comment changer les paramètres
* Affinage localement

## Comment trouver un jeu de données pour l'affinage

### Trouver un jeu de données en ligne

Pour affiner le modèle, nous avons besoin d'un jeu de données avec lequel nous allons affiner. Si vous voulez une solution simple, vous pouvez trouver un jeu de données préparé dans [ce dossier sur Google Drive](https://drive.google.com/drive/folders/1orOj76DW2o-w3Dnati2CKAlXauH8STpT?usp=sharing). 

Vous devriez ensuite copier ce jeu de données dans votre propre Google Drive. Notez que cela a été pris depuis [ce tutoriel](https://towardsdatascience.com/ocr-free-document-understanding-with-donut-1acfbdf099be) sous le titre "Downloading and parsing SROIE". Le tutoriel est une excellente lecture qui a inspiré cet article, car je voulais créer un tutoriel plus approfondi pour l'affinage du modèle Donut dans Google Colab. Donc, si vous voulez un regard plus approfondi sur la génération du jeu de données, je recommande de lire le tutoriel ci-dessus.

Le jeu de données lié ci-dessus n'est pas nécessairement pour votre usage spécifique. Si vous voulez affiner un modèle pour vos besoins spécifiques, vous devez soit trouver un jeu de données adapté en ligne, soit créer un jeu de données vous-même.

### Annoter votre propre jeu de données

C'est une autre option si vous ne pouvez pas ou ne voulez pas trouver un jeu de données en ligne (donc si vous l'avez fait, vous pouvez ignorer cette sous-section). 

Annoter votre propre jeu de données est un moyen sûr de créer un jeu de données qui correspond parfaitement à vos besoins. 

Il existe de nombreux outils d'annotation en ligne, mais un outil gratuit que je recommande est l'[outil d'annotation de données Sparrow UI](https://github.com/katanaml/sparrow). Ici, vous pouvez télécharger votre image, placer des boîtes englobantes sur l'image et étiqueter chaque boîte englobante. Vous pouvez ensuite extraire les données étiquetées au format JSON et les utiliser en suivant le reste du tutoriel. 

Assurez-vous que votre jeu de données est au même format que le [jeu de données que j'ai fourni précédemment](https://drive.google.com/drive/folders/1orOj76DW2o-w3Dnati2CKAlXauH8STpT). Pour plus de détails sur l'annotation des données avec Sparrow UI, vous pouvez consulter [mon article sur l'utilisation du modèle Donut pour les données auto-annotées](https://medium.com/python-in-plain-english/empower-your-donut-model-for-receipts-with-self-annotated-data-51fc882b7229). Notez que cet article suppose que vous êtes déjà capable d'affiner le modèle Donut (ce que vous apprendrez dans cet article).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img2.png)
_Annotation d'un reçu avec l'outil d'annotation de données Sparrow UI_

## Affinage avec Google Colab

Pour rendre le processus d'affinage aussi simple que possible, j'ai fourni un [fichier Google Colab que vous pouvez utiliser ici](https://colab.research.google.com/drive/1-qfztYjDrFecOWdqyANtI23HV06xhDRE?usp=sharing). (Certains codes sont tirés de [cette page GitHub](https://github.com/NielsRogge/Transformers-Tutorials)). 

Notez que les versions des packages doivent être exactement celles fournies dans le Drive, car les mauvaises versions des packages étaient à l'origine de nombreux problèmes que j'ai rencontrés en affinant le modèle Donut moi-même.

Avant d'affiner en utilisant le fichier Google Colab, il y a 2 choses que vous devez faire :

### Télécharger les données sur votre Google Drive.

Téléchargez le [jeu de données que j'ai fourni précédemment](https://drive.google.com/file/d/1WsWLVZhKLb8A0uCJ7Jpk8F5pCNDNsGbH/view?usp=sharing) sur votre Google Drive dans un dossier parent appelé _preparedFinetuneData_ (voir la structure de fichier dans l'image ci-dessous). 

Assurez-vous d'ajouter le dossier parent dans le dossier racine de votre Google Drive. De plus, téléchargez [ce fichier de configuration](https://drive.google.com/file/d/1WsWLVZhKLb8A0uCJ7Jpk8F5pCNDNsGbH/view?usp=sharing) et ajoutez-le au dossier racine de votre Google Drive.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img.png)
_Comment votre jeu de données devrait apparaître dans le dossier racine de Google Drive_

### Lier votre Google Drive à votre Google Colab.

Lorsque vous exécutez la cellule qui monte le Google Drive, vous pourriez obtenir une invite, auquel cas vous pouvez simplement l'accepter et ignorer le reste de ce paragraphe. 

Si vous n'obtenez pas d'invite, appuyez sur l'icône des fichiers (en rouge dans l'image ci-dessous), puis sur l'icône Monter le Drive (en bleu dans l'image ci-dessous). Vous obtiendrez alors un extrait de code que vous pouvez exécuter, et maintenant votre Google Drive est connecté. 

Notez que si vous n'avez pas connecté Google Colab à Google Drive auparavant, vous devez vous connecter à votre Google Drive après avoir appuyé sur l'icône du Drive, et donner la permission à Colab d'accéder au Drive (les invites pour cela devraient apparaître automatiquement lorsque vous essayez de lier le Drive).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img3.png)
_Icône des fichiers (rouge). Monter Google Drive (bleu)_

Enfin, **redémarrez votre runtime**. Après avoir modifié des fichiers sur Google Colab, vous devez toujours redémarrer votre runtime pour voir les dernières mises à jour.

## Comment changer les paramètres

Super ! Maintenant, vous pouvez exécuter les cellules dans le notebook, et vous devriez recevoir un modèle affiné. N'oubliez pas que vous pouvez également changer les paramètres de configuration pour, par exemple, entraîner plus longtemps, utiliser plus de workers, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img6.png)
_Exemple de paramètres de configuration que vous pouvez changer._

Notez que je travaille avec le modèle Donut affiné sur le [jeu de données CORD](https://github.com/clovaai/cord), car je veux être capable de lire des reçus. Vous pouvez également trouver d'autres modèles Donut [ici](https://github.com/clovaai/donut), les autres options étant l'analyse de documents, la classification de documents, ou la réponse visuelle aux questions sur les documents (DocVQA).

## Affinage localement

L'affinage peut également être exécuté localement, ce qui sera surtout pertinent pour vous si vous avez un GPU, car l'entraînement sur CPU prendra beaucoup de temps. 

Pour exécuter localement, vous devez :

1. D'abord, cloner [ce dépôt GitHub](https://github.com/clovaai/donut)
2. Ajouter le jeu de données préparé pour l'affinage au dossier racine.
3. Si vous voulez sauvegarder le modèle affiné, ajoutez la ligne ci-dessous à train.py ligne 164, juste en dessous de _trainer.fit()_

```py
#...
trainer.save_checkpoint(f"{Path(config.result_path)}/{config.exp_name}/{config.exp_version}/model_checkpoint.ckpt")
#...
```

4. Vous devez ensuite commenter les processus GPU dans le PyTorch Lightning Trainer, et ajouter la ligne : _accelerator="cpu"_ :

```py
#train.py file
#... 
trainer = pl.Trainer(
        #Comment out the lines above
        # num_nodes=config.get("num_nodes", 1),
        # devices=torch.cuda.device_count(),
        # strategy="dp",
        # accelerator="gpu",
        accelerator="cpu", #TODO add this line
        plugins=custom_ckpt,
        max_epochs=config.max_epochs,
        max_steps=config.max_steps,
        val_check_interval=config.val_check_interval,
        check_val_every_n_epoch=config.check_val_every_n_epoch,
        gradient_clip_val=config.gradient_clip_val,
        precision=16,
        num_sanity_val_steps=0,
        logger=logger,
        callbacks=[lr_callback, checkpoint_callback, bar],
    )
#...
```

5. Assurez-vous que le paramètre max_epochs dans votre fichier Config est défini sur -1 (sinon vous obtiendrez une erreur de division par 0). Vous pouvez décider du temps d'entraînement en définissant le paramètre _max_steps_.

6. Vous pouvez ensuite exécuter l'affinage avec la commande suivante dans le terminal :

```bash
python train.py --config config/train_cord.yaml
```

Où _train_cord.yaml_ est le fichier de configuration que vous souhaitez utiliser.

### Exécution sur CPU

Si vous exécutez sur CPU après tout, vous rencontrerez quelques problèmes à moins de faire quelques changements :

1. donut/train.py, changez le paramètre _accelerator_ en "cpu" (au lieu de "gpu"), et supprimez les paramètres : _num_nodes_, _devices_, et _strategy_).
2. Ensuite, dans votre fichier Config (par exemple _train_cord.yaml_), définissez _max_epochs_ sur -1, puis spécifiez le paramètre _max_steps_. Cela est dû au fait que vous rencontrerez une erreur de division par 0 si vous avez _max_epoch_ supérieur à 0

Après ces changements, l'exécution sur un CPU devrait également fonctionner.

## Conclusion

Dans cet article, je vous ai montré comment affiner facilement le modèle Donut en utilisant vos propres données, ce qui, je l'espère, entraînera une amélioration de la précision pour votre modèle Donut affiné. 

Les applicabilités du modèle Donut sont nombreuses, et ceci n'est qu'une façon de l'utiliser, que j'espère utile.

Si vous êtes intéressé et souhaitez en savoir plus sur des sujets similaires, vous pouvez me trouver sur :

* [ Medium](https://medium.com/@oieivind)
* [](https://twitter.com/Ravenspike21) [Twitter](https://twitter.com/Ravenspike21)