---
title: Comment affiner EasyOCR avec un ensemble de données synthétique
subtitle: ''
author: Eivind Kjosbakken
co_authors: []
series: null
date: '2024-01-05T17:48:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-fine-tune-easyocr-with-a-synthetic-dataset
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/image-53.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
seo_title: Comment affiner EasyOCR avec un ensemble de données synthétique
seo_desc: "OCR is a valuable tool that you can use to extract text from images. But\
  \ the OCR you are using may not work as intended for your specific needs. In such\
  \ situations, fine-tuning your OCR engine is the way to go. \nIn this tutorial,\
  \ I will show you how ..."
---

L'OCR est un outil précieux que vous pouvez utiliser pour extraire du texte à partir d'images. Mais l'OCR que vous utilisez peut ne pas fonctionner comme prévu pour vos besoins spécifiques. Dans de telles situations, l'ajustement fin de votre moteur OCR est la solution à adopter.

Dans ce tutoriel, je vais vous montrer comment affiner EasyOCR, un moteur OCR gratuit et open-source que vous pouvez utiliser avec Python.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Comment installer les packages requis](#heading-how-to-install-required-packages)
* [Comment cloner le dépôt Git](#heading-how-to-clone-the-git-repository)
* [Comment obtenir un ensemble de données](#how-get-a-dataset)
* [Comment générer votre ensemble de données synthétique](#heading-how-to-generate-your-synthetic-dataset)
* [Convertir l'ensemble de données au format lmdb](#convert-the-dataset-to-lmdb-format)
* [Comment récupérer un modèle OCR pré-entraîné](#heading-how-to-retrieve-a-pre-trained-ocr-model)
* [Comment exécuter l'ajustement fin](#heading-how-to-run-the-fine-tuning)
* [Comment exécuter l'inférence avec votre modèle affiné](#heading-how-to-run-inference-with-your-fine-tuned-model)
* [Un test qualitatif de performance](#heading-a-qualitative-test-of-performance)
* [Test quantitatif de performance](#heading-quantitative-test-of-performance)
* [Conclusion](#heading-conclusion)

## Prérequis

* Connaissance de base de Python.
* Connaissance de base de l'utilisation du terminal

## Comment installer les packages requis

Tout d'abord, installons les packages `pip` requis. Je recommande de créer un environnement virtuel pour cela, bien que ce ne soit pas obligatoire.

Exécutez les commandes ci-dessous, une ligne à la fois :

```bash
pip install fire
pip install lmdb
pip install opencv-python
pip install natsort
pip install nltk
```

Vous devez également installer PyTorch depuis [ce site web](https://pytorch.org/get-started/locally/) (choisissez vos spécifications et copiez la commande pip install. La commande ci-dessous est pour mes spécifications). Vous pouvez choisir soit la version GPU soit la version CPU. La différence est que l'exécution du processus d'ajustement fin sera plus lente sur le CPU.

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Comment cloner le dépôt Git

Vous aurez besoin d'un dépôt Git qui vous aidera à exécuter l'ajustement fin. Clonez [ce dépôt Git](https://github.com/clovaai/deep-text-recognition-benchmark) avec la commande ci-dessous :

```bash
git clone https://github.com/clovaai/deep-text-recognition-benchmark
```

Le [dépôt GitHub deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) nous fournira certains fichiers utiles pour l'ajustement fin du modèle EasyOCR. Notez que certaines des commandes de terminal utilisées dans cet article ont été prises du dépôt et ensuite adaptées à mes besoins, donc le dépôt vaut la peine d'être lu.

J'aimerais ajouter une note ici que [Clova AI sur Git](https://github.com/clovaai) a beaucoup de bons dépôts qui m'ont été d'une immense aide, alors n'hésitez pas à vérifier d'autres dépôts intéressants qu'ils ont.

Un autre dépôt intéressant qu'ils ont est le [dépôt du modèle Donut](https://github.com/clovaai/donut), et j'ai écrit un [article sur l'ajustement fin du modèle Donut](https://python.plainenglish.io/empower-your-donut-model-for-receipts-with-self-annotated-data-51fc882b7229) que vous devriez consulter.

## Comment obtenir un ensemble de données

Avant de pouvoir affiner votre OCR, vous aurez besoin d'un ensemble de données. Vous pouvez soit télécharger un ensemble de données, soit en créer un vous-même.

Puisque je veux que mon OCR soit particulièrement bon pour scanner les tickets de caisse de supermarché, je vais créer un ensemble de données d'articles que vous pouvez trouver dans le supermarché, mais n'hésitez pas à créer un ensemble de données à partir de toute donnée dont vous avez besoin que votre OCR soit bon. Pour cette section, j'ai utilisé [cette page GitHub](https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md).

Si vous voulez apprendre à générer votre propre ensemble de données, vous pouvez passer à la section suivante tout de suite, mais si vous voulez une solution plus simple, vous pouvez utiliser l'une des options ci-dessous :

### Option 1 – Utiliser mon ensemble de données factice :

Si vous voulez que cette étape soit aussi simple que possible (recommandé si vous testez simplement), vous pouvez télécharger un ensemble de données factice. J'en ai créé et téléchargé un sur [ce Google Drive](https://drive.google.com/drive/folders/1rS-WFRqN9zkD3vetwcYYFmOzg_cMv9su?usp=sharing) (téléchargez le dossier entier).

### Option 2 – Télécharger un ensemble de données

Si vous voulez un ensemble de données plus grand, vous pouvez télécharger un ensemble de données depuis [cette page Dropbox](https://www.dropbox.com/sh/i39abvnefllx2si/AAAbAYRvxzRp3cIE5HzqUw3ra?dl=0) en téléchargeant le fichier data_lmdb_release.zip (notez qu'il fait un peu plus de 18 Go).

## Comment générer votre ensemble de données synthétique

Si vous voulez une approche plus intéressante pour créer votre propre ensemble de données, vous pouvez suivre cette section. J'en ai initialement parlé dans [cet article Medium](https://blog.devgenius.io/generating-a-fine-tuning-dataset-for-an-ocr-engine-3509167bc8a1).

Pour cette section, vous devriez utiliser un fichier Python séparé.

L'avantage d'un ensemble de données synthétique est que vous n'avez pas besoin d'étiquetage intensif en main-d'œuvre, car vous créez les images en fonction des descriptions textuelles fournies. Cela signifie que vous avez à la fois l'entrée du modèle (l'image) et l'étiquette (le texte des images), les deux composants nécessaires pour affiner un modèle d'IA.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-61.png)
_Créez des images synthétiques comme celle-ci en suivant cette section_

### Cloner le dépôt de génération synthétique

Tout d'abord, vous devez cloner [ce dépôt de génération de données synthétiques](https://github.com/Belval/TextRecognitionDataGenerator) pour pouvoir créer des données synthétiques. Pour le cloner, ouvrez un nouveau dossier et exécutez cette commande :

```bash
git clone https://github.com/Belval/TextRecognitionDataGenerator.git
```

Ce dépôt vous permet de créer des images à partir d'une description textuelle donnée. Vous aurez alors l'ensemble de données dont vous avez besoin : des images et un fichier txt indiquant le texte sur les images (l'étiquette).

### Créer un fichier pour générer les données synthétiques

Maintenant, créez un nouveau fichier appelé `generate_synth_data.py`, et ajoutez le code ci-dessous pour importer les packages utiles :

```py
from trdg.generators import (
    GeneratorFromStrings,
)
from tqdm.auto import tqdm
import os
import pandas as pd
import numpy as np
import random
```

Pour les exécuter, vous avez besoin de ces installations `pip` (exécutez une ligne à la fois dans le terminal). Notez qu'une version spécifique de `Pillow` est nécessaire (vous obtiendrez une erreur si vous avez la dernière version de Pillow) :

```bash
pip install trdg
pip install pandas
pip install Pillow==9.5.0
```

Ensuite, définissez quelques hyperparamètres (donnez-leur les valeurs que vous préférez) :

```py
NUM_IMAGES_TO_SAVE = 10
NUM_PRICES_TO_GENERATE = 10000
```

Maintenant, vous avez besoin d'un grand ensemble de données avec des mots que vous voulez avoir sur les images que vous créez. Puisque je veux que mon OCR soit bon pour lire les tickets de caisse de supermarché, j'ai utilisé [Openfoodfacts](https://no.openfoodfacts.org/), qui est un site web contenant de nombreux articles de supermarché.

Pour simplifier au maximum, vous pouvez utiliser le fichier CSV sur [cette page Google Drive](https://drive.google.com/file/d/1DZhRBVGpf9smuiom3JdL0QW0HEgKIqtQ/view?usp=sharing) (téléchargez-le simplement et placez-le dans votre dossier).

Notez que vous pouvez utiliser n'importe quelle autre donnée au lieu d'utiliser la mienne. Si vous voulez utiliser vos propres données, tout ce dont vous avez besoin est une liste de chaînes de caractères, que vous pouvez alimenter dans le générateur pour créer des images.

Voici comment vous pouvez lire le fichier CSV contenant les articles de supermarché :

```py
# helper funcs and data to generate images
df = pd.read_csv("openfoodfacts_export_csv.csv", on_bad_lines='skip', sep='\t', low_memory=True)
df[["product_name_nb", "generic_name_nb", "brands"]]
all_words = df[["product_name_nb", "generic_name_nb", "brands"]].to_numpy().flatten()
```

Ici, je charge mes propres données, mais le code sera différent si vous utilisez vos propres données.

Voici comment vous pouvez filtrer les données :

```py
# ignore np nan 
num_before = len(all_words)
all_words = [x for x in all_words if str(x) != 'nan']
after_nan_filter = len(all_words)
print("removed: ", num_before - after_nan_filter, "words because of nan values")
all_words = list(set(all_words))
print("Removed", len(all_words), "duplicates")
print("Current number of words: ", len(all_words))
```

Notez que j'imprime toujours le nombre de mots supprimés lors du processus de filtrage. C'est une bonne pratique, car cela vous permet d'avoir une meilleure vue d'ensemble de la taille et de la qualité de votre ensemble de données.

Je veux également avoir un prix sur les images, donc je génère aléatoirement quelques prix avec le code ci-dessous :

```py
#randomly generate 2 digits between 0-99
number_strings = []
for i in range(len(all_words)*9//10): #90 percent of all words
 digits = np.random.randint(1, 100, 4)
 before_comma = f"{str(digits[0])}" #before comma is just given as 1 digit if 0-9
 after_comma = f"{str(digits[1])}" if len(str(digits[1])) == 2 else f"0{str(digits[1])}"
 number_string = f"{before_comma},{after_comma}"
 number_strings.append(number_string)

#then create 10 percent of the words with price between 100-999
for i in range(len(all_words)*1//10): #90 percent of all words
 before_comma = np.random.randint(100, 999, 1)
 after_comma = np.random.randint(1, 99, 1)
 after_comma = f"{str(after_comma[0])}" if len(str(after_comma[0])) == 2 else f"0{str(after_comma[0])}"
 number_string = f"{str(before_comma[0])},{str(after_comma)}"
 number_strings.append(number_string)
```

Le code ci-dessous combine aléatoirement les articles de supermarché avec les prix :

```py
#now given word list and number list, get all combinations
all_combinations = []
for word in tqdm(all_words):
 for number in random.sample(number_strings, 20): #only need 20 prices per product for example
  for num_tabs in [1]:
   combined_string = word + "    "*num_tabs + number
   all_combinations.append(combined_string)
```

Utilisez le dépôt que vous avez cloné précédemment pour créer les images à partir de la liste de chaînes que nous avons créée :

```py
#generate the images
generator = GeneratorFromStrings(
    random.sample(all_combinations, 10000),

    # uncomment the lines below for some image augmentation options
    # blur=6,
    # random_blur=True,
    # random_skew=True,
    # skewing_angle=20,
    # background_type=1,
    # text_color="red",
)
```

Il existe de nombreuses options pour générer les données, que vous pouvez lire plus en détail [ici](https://github.com/Belval/TextRecognitionDataGenerator). Certains exemples sont : changer l'arrière-plan, ajouter du flou et ajouter du skewing. Vous pouvez essayer cela en décommentant certaines des lignes dans l'extrait de code ci-dessus.

Ensuite, enregistrez les images du générateur dans un format spécifique :

```py
# save images from generator
# if output folder doesnt exist, create it
if not os.path.exists('output'):
    os.makedirs('output')
#if labels.txt doesnt exist, create it
if not os.path.exists('output/labels.txt'):
    f = open("output/labels.txt", "w")
    f.close()

#open txt file
current_index = len(os.listdir('output')) - 1 #all images minus the labels file
f = open("output/labels.txt", "a")

for counter, (img, lbl) in tqdm(enumerate(generator), total = NUM_IMAGES_TO_SAVE):
    if (counter >= NUM_IMAGES_TO_SAVE):
        break
    # img.show()
    #save pillow image
    img.save(f'output/image{current_index}.png')
    f.write(f'image{current_index}.png {lbl}\n')
    current_index += 1
    # Do something with the pillow images here.
f.close()
```

### Générer les données synthétiques

Vous pouvez exécuter le fichier `generate_synth_data.py` que vous avez créé avec cette commande dans le terminal :

```bash
python generate_synth_data.py
```

Vous devriez voir une image similaire à celle ci-dessous (vous pouvez avoir un texte différent, dans votre dossier de sortie) :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-62.png)
_Cette image a été générée synthétiquement_

Vos images seront organisées dans l'ordre de l'image ci-dessous, où les fichiers `.png` sont vos images, et le fichier `labels.txt` contient le texte de chaque image. Cela vous permet d'utiliser l'ensemble de données pour l'ajustement fin.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-63.png)
_La structure du dossier de sortie après l'exécution du code ci-dessus._

Félicitations, vous pouvez maintenant créer votre propre ensemble de données synthétique. Puisque vous avez maintenant à la fois une image et le texte de cette image dans un fichier `labels.txt`, vous pouvez utiliser cela pour affiner un moteur OCR, dont je parlerai plus en détail ci-dessous.

## Comment convertir l'ensemble de données au format LMDB

LMDB signifie [Lightning Memory-Mapped Database Manager](http://www.lmdb.tech/doc/) et est essentiellement un encodage que vous pouvez utiliser pour votre ensemble de données afin d'entraîner des modèles d'IA.

Vous pouvez en lire plus sur la [documentation LMDB](https://lmdb.readthedocs.io/en/release/). Après avoir créé votre ensemble de données, vous devriez avoir un dossier avec vos images, et les étiquettes pour toutes les images (le texte dans les images) dans un fichier `labels.txt`.

Votre dossier devrait ressembler à l'image ci-dessous, et devrait être à l'intérieur du dossier **deep-text-recognition** :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-54.png)
_Comment le dossier de votre ensemble de données devrait ressembler avant la conversion au format LMDB_

**NOTE** : Assurez-vous d'avoir au moins 10 images dans votre dossier. Vous pourriez obtenir une erreur lors de l'exécution du script d'entraînement plus tard dans le tutoriel si vous avez moins d'images.

Vous devez apporter quelques modifications au fichier `create_lmdb_dataset.py` dans le dossier **deep-text-recognition-benchmark** :

Définissez la variable `map_size` à une valeur plus basse — j'obtenais une erreur de mémoire disque avec la valeur précédente. J'ai défini la nouvelle valeur pour `map_size` à 1073741824, comme on peut le voir ci-dessous :

```py
# OLD LINE
# ...
env = lmdb.open(outputPath, map_size=1099511627776)
# ...

# NEW LINE 
# ...
env = lmdb.open(outputPath, map_size=1073741824) 
# ...
```

J'ai également obtenu une erreur avec l'encodage utf, donc j'ai supprimé l'encodage utf-8 lors de l'ouverture du `gtFile`. La nouvelle ligne ressemble alors à ceci :

```py
# OLD LINE
# ...
with open(gtFile, 'r', encoding='utf-8') as data:
# ...

# NEW LINE
# ...
with open(gtFile, 'r') as data:
# ...
```

Enfin, j'ai changé la façon dont `imagePath` était lu :

```py
# OLD LINE
# ...
imagePath, label = datalist[i].strip('\n').split('\t')
# ...

# NEW LINES
# ...
imagePath, label = datalist[i].strip('\n').split('.png')
imagePath += '.png'
# ...
```

Le fichier `create_lmdb_dataset.py` devrait ressembler à ceci (code du [dépôt Git](https://github.com/clovaai/deep-text-recognition-benchmark), avec les changements ci-dessus appliqués) :

```py
import fire
import os
import lmdb
import cv2

import numpy as np


def checkImageIsValid(imageBin):
    if imageBin is None:
        return False
    imageBuf = np.frombuffer(imageBin, dtype=np.uint8)
    img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
    imgH, imgW = img.shape[0], img.shape[1]
    if imgH * imgW == 0:
        return False
    return True


def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            txn.put(k, v)


def createDataset(inputPath, gtFile, outputPath, checkValid=True):
    """
    Create LMDB dataset for training and evaluation.
    ARGS:
        inputPath  : input folder path where starts imagePath
        outputPath : LMDB output path
        gtFile     : list of image path and label
        checkValid : if true, check the validity of every image
    """
    os.makedirs(outputPath, exist_ok=True)
    env = lmdb.open(outputPath, map_size=1073741824) #TODO Changed map size
    cache = {}
    cnt = 1

    with open(gtFile, 'r') as data: #TODO removed utf-8 encoding here since I have norwegian letters
        datalist = data.readlines()

    nSamples = len(datalist)
    print(nSamples)
    for i in range(nSamples):
        #TODO changed the way imagePath is found as well to match my usecase
        imagePath, label = datalist[i].strip('\n').split('.png')
        imagePath += '.png'

        # imagePath, label = datalist[i].strip('\n').split('\t')
        imagePath = os.path.join(inputPath, imagePath)

        # # only use alphanumeric data
        # if re.search('[^a-zA-Z0-9]', label):
        #     continue

        if not os.path.exists(imagePath):
            print('%s does not exist' % imagePath)
            continue
        with open(imagePath, 'rb') as f:
            imageBin = f.read()
        if checkValid:
            try:
                if not checkImageIsValid(imageBin):
                    print('%s is not a valid image' % imagePath)
                    continue
            except:
                print('error occured', i)
                with open(outputPath + '/error_image_log.txt', 'a') as log:
                    log.write('%s-th image data occured error\n' % str(i))
                continue

        imageKey = 'image-%09d'.encode() % cnt
        labelKey = 'label-%09d'.encode() % cnt
        cache[imageKey] = imageBin
        cache[labelKey] = label.encode()

        if cnt % 1000 == 0:
            writeCache(env, cache)
            cache = {}
            print('Written %d / %d' % (cnt, nSamples))
        cnt += 1
    nSamples = cnt-1
    cache['num-samples'.encode()] = str(nSamples).encode()
    writeCache(env, cache)
    print('Created dataset with %d samples' % nSamples)


if __name__ == '__main__':
    fire.Fire(createDataset)
```

Ensuite, déplacez le dossier vers le dossier **deep-text-recognition-benchmark** (le dépôt Git que vous avez cloné). Ensuite, exécutez la commande suivante dans le terminal :

```bash
python .\create_lmdb_dataset.py <data folder name> <path to labels.txt in data folder> <output folder for your lmdb dataset>
```

Où :

* `<data folder name>` est le nom de votre dossier avec les images et `labels.txt` (`output` dans mon cas)
* `<path to labels.txt>` est le `<data folder name>` + le `labels.txt` (donc `.\output\labels.txt` dans mon cas)
* `<output folder for your lmdb dataset>` est le nom d'un dossier qui sera créé pour votre ensemble de données converti au format LMDB (je l'ai appelé `.\lmbd_output`)

Pour moi, c'était la commande (assurez-vous d'exécuter cette commande à l'intérieur du dossier **deep-text-recognition-benchmark**) :

```bash
python .\create_lmdb_dataset.py .\output .\output\labels.txt .\lmbd_output
```

Maintenant, vous devriez avoir un nouveau dossier, comme dans l'image ci-dessous, dans votre dossier **deep-text-recognition-benchmark**.



![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-55.png)
_Comment le dossier de vos données converties en lmdb devrait ressembler_

**NOTE** : L'exécution de la commande sur un dossier existant ne remplace pas le dossier existant. Assurez-vous de supprimer un dossier ou de donner un nouveau nom à **lmdb_output** (c'est quelque chose avec lequel j'ai eu du mal pendant un moment, donc espérons que cela vous aidera à éviter cette erreur).

## Comment récupérer un modèle OCR pré-entraîné

Ensuite, vous avez besoin d'un modèle OCR pré-entraîné que vous pouvez affiner avec votre ensemble de données. Pour cela, vous pouvez aller sur [ce site Dropbox](https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW) et télécharger le modèle `TPS-ResNet-BiLSTM-Attn.pth`.

Placez le modèle dans votre dossier **deep-text-recognition-benchmark** (je sais que cela semble un peu douteux, mais c'est la partie des instructions dans le dépôt deep-text-recognition-benchmark. Le Dropbox n'est pas à moi, et je le lie ici parce qu'il est lié dans le dépôt Git _text-recognition-benchmark_)

## Comment exécuter l'ajustement fin

Si vous exécutez sur CPU (ceci peut être ignoré si vous utilisez GPU), vous obtiendrez probablement une erreur qui dit : "RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False".

Cela peut être corrigé en modifiant les lignes 85 et 87 dans le fichier `train.py` :

```py
# OLD LINES
# ...
if opt.FT:
    model.load_state_dict(torch.load(opt.saved_model), strict=False)
else:
    model.load_state_dict(torch.load(opt.saved_model))
# ...


# NEW LINES (change to this if you are using CPU)
#
if opt.FT:
    model.load_state_dict(torch.load(opt.saved_model,map_location='cpu'), strict=False)
else:
    model.load_state_dict(torch.load(opt.saved_model,map_location='cpu'))
# ...
```

Enfin, vous pouvez alors exécuter l'ajustement fin. Pour cela, vous pouvez utiliser la commande ci-dessous dans le terminal :

```bash
python train.py --train_data lmdb_output --valid_data lmdb_output --select_data "/" --batch_ratio 1.0 --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --batch_size 2 --data_filtering_off --workers 0 --batch_max_length 80 --num_iter 10 --valInterval 5 --saved_model TPS-ResNet-BiLSTM-Attn.pth
```

Quelques notes sur la commande :

* `data_filtering_off` est défini sur `True` (vous devez simplement utiliser le drapeau, pas lui donner une variable). Je n'ai pas utilisé `data_filtering` car je n'aurais aucun échantillon à entraîner si le filtrage était activé.
* Les workers ont été définis sur 0 pour éviter les erreurs. Je pense que cela a quelque chose à voir avec les paramètres multi-GPU, et cela est également mentionné dans le fichier `train.py` dans le dossier **deep-text-recognition-benchmark**.
* `batch_max_length` est la longueur maximale de tout texte dans l'ensemble de données d'entraînement. Si vous utilisez un ensemble de données différent, n'hésitez pas à changer cette variable. Assurez-vous que cette variable est aussi grande que la chaîne la plus longue que vous utilisez dans votre ensemble de données, ou vous obtiendrez une erreur.
* Pour ce tutoriel, j'utilise `train_data` et `valid_data` pour faire référence au même dossier. En pratique, je créerais un dossier avec un ensemble de données d'entraînement, et un pour un ensemble de données de validation et je ferais référence à ceux-ci à la place.
* J'ai défini `num_iter` à 10 pour que vous puissiez vous assurer que cela fonctionne. Naturellement, cette variable doit être définie beaucoup plus haut lors de l'exécution de l'ajustement fin réel d'un modèle.
* `saved_model` est un paramètre facultatif. Si vous ne le définissez pas, vous entraînez un modèle à partir de zéro. Vous ne voulez probablement pas cela (car cela nécessitera beaucoup d'entraînement), donc définissez le drapeau `saved_model` sur le modèle existant que vous avez [téléchargé depuis Dropbox](https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW).

## Comment exécuter l'inférence avec votre modèle affiné

Après avoir affiné votre modèle, vous voudrez exécuter l'inférence avec celui-ci. Pour cela, vous pouvez utiliser la commande ci-dessous :

```bash
python demo.py --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --image_folder <path to images to test on> --saved_model <path to model to use>
```

Où :

* `<path to images to test on>` est un dossier contenant des images PNG sur lesquelles vous voulez tester. Pour moi, c'était **output**
* `<path to model to use>` est le chemin vers le modèle enregistré de votre ajustement fin. Pour moi, c'était **.\saved_models\TPS-ResNet-BiLSTM-Attn-Seed1111\best_accuracy.pth** (l'ajustement fin enregistre le modèle affiné dans un dossier `saved_models`)

Voici la commande que j'ai utilisée :

```bash
python demo.py --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --image_folder output --saved_model .\saved_models\TPS-ResNet-BiLSTM-Attn-Seed1111\best_accuracy.pth
```

La commande produit simplement la prédiction du modèle et le score de confiance pour chaque image dans le dossier `<path to images to test on>`, afin que vous puissiez vérifier les performances du modèle en regardant les images vous-même pour voir si le modèle a fait la bonne prédiction. Il s'agit d'un test qualitatif des performances du modèle.

## Un test qualitatif de performance

Pour voir si l'ajustement fin a fonctionné, je vais effectuer un test qualitatif des performances en testant le modèle original par rapport à mon modèle affiné sur 10 mots et chiffres spécifiques.

Les mots que j'ai testés sont montrés ci-dessous (fusionnés verticalement en une seule image). J'ai dû rendre cela un peu difficile pour le modèle en ajoutant des textes inclinés et flous.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-56.png)
_Images auto-créées fusionnées avec [https://products.aspose.app/pdf/merger/png-to-png](https://products.aspose.app/pdf/merger/png-to-png" rel="noopener ugc nofollow). Les mots de haut en bas sont : vanskeligheter, uvanligheter, skrekkeksempel, rosenborg_

Considérant que je veux que mon OCR lise les tickets de caisse norvégiens, j'ai ajouté quelques mots norvégiens (les mots sont tirés de [http://openfoodfacts.com/](http://openfoodfacts.com/), vous pouvez en lire plus à ce sujet dans [cet article](https://medium.com/dev-genius/generating-a-fine-tuning-dataset-for-an-ocr-engine-3509167bc8a1)).

Espérons que mon modèle affiné devrait mieux performer sur ces mots, car le modèle OCR original n'est pas habitué à voir des mots norvégiens. Mon modèle affiné a été entraîné sur certains mots norvégiens.

Les textes dans chaque image sont :

* image0 -> vanskeligheter
* image1 -> uvanligheter
* image2 -> skrekkeksempel
* image3 -> rosenborg

Résultats pour le modèle original (non affiné) :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-57.png)
_Résultats pour le modèle original (non affiné) sur un test qualitatif. Vous pouvez voir que le modèle a du mal_

Résultats pour le modèle affiné :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-58.png)
_Résultats pour le modèle affiné. Vous pouvez voir que le modèle atteint une précision parfaite grâce à l'ajustement fin._

Comme vous pouvez le voir, l'ajustement fin a fonctionné, et le modèle affiné atteint des résultats parfaits dans cet exemple qualitatif.

Pour interpréter vos résultats qualitativement, vous devriez prendre un échantillon de documents représentatifs de l'ensemble de données complet et comparer manuellement la sortie de l'OCR et la vérité terrain. Cela vous donnera une idée de la performance du modèle, car vous pouvez voir à quelle fréquence il commet des erreurs.

Vous devez noter que vous ne pouvez souvent pas vous attendre à des résultats parfaits de la part du moteur OCR affiné, et vous pouvez donc utiliser l'analyse qualitative pour déterminer les erreurs spécifiques que le modèle commet.

Cela pourrait, par exemple, être le modèle ayant des difficultés à reconnaître certains caractères. Si c'est le cas, vous pouvez entraîner le modèle sur plus d'exemples de ces caractères pour augmenter davantage les performances de votre modèle.

## Test quantitatif de performance

Si vous voulez un test plus quantitatif, vous pouvez soit regarder les résultats de validation qui apparaissent pendant l'ajustement fin, soit utiliser la commande ci-dessous :

```bash
python test.py --eval_data <path to test data set in lmdb format> --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --saved_model <path to model to test> --batch_max_length 70 --workers 0 --batch_size 2 --data_filtering_off
```

Où :

* `<path to test data set in lmdb format>` est le chemin vers le dossier contenant les données de test au format LMDB. Pour moi, c'était : `lmdb_norwegian_data_test`
* `<path to model to test>` est le chemin vers le modèle dont vous voulez tester les performances. Pour moi, c'était : `saved_models/TPS-ResNet-BiLSTM-Attn-Seed1111/best_accuracy.pth`.

La commande que j'ai utilisée était donc :

```bash
python test.py --eval_data lmdb_norwegian_data_test --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --saved_model saved_models/TPS-ResNet-BiLSTM-Attn-Seed1111/best_accuracy.pth --batch_max_length 70 --workers 0 --batch_size 2 --data_filtering_off
```

Cela produira une précision en pourcentage, donc un nombre entre 0 et 100, qui est la précision que le modèle OCR atteint sur votre ensemble de données de test.

Dans mon expérience, le modèle que vous avez téléchargé depuis Dropbox a besoin d'un peu d'entraînement. Au début, le modèle fera des prédictions inexactes, mais si vous le laissez s'entraîner pendant 30 minutes environ, vous devriez commencer à voir quelques améliorations.

J'ai ensuite exécuté le `test.py` sur les 4 images que j'ai montrées ci-dessus et obtenu les résultats dans les images ci-dessous : avec l'ancien modèle (non affiné) en haut et le nouveau modèle affiné en bas.

Résultats de l'ancien modèle :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-59.png)
_Résultat pour l'ancien modèle, qui atteint une précision de 50%._

Résultats du modèle affiné :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-60.png)
_Résultat pour le nouveau modèle affiné qui atteint une précision de 100%, ce qui indique que l'ajustement fin a fonctionné_

Vous pouvez voir que le nouveau modèle affiné performe mieux avec une précision de 100 pour cent.

## Conclusion

Félicitations, vous pouvez maintenant affiner votre modèle OCR. Pour avoir un impact significatif sur un modèle plus grand et le généraliser, vous devez probablement créer un ensemble de données plus grand. Vous pouvez en apprendre davantage à ce sujet dans [ce tutoriel](https://medium.com/dev-genius/generating-a-fine-tuning-dataset-for-an-ocr-engine-3509167bc8a1), puis laisser le modèle s'entraîner pendant un certain temps.

En fin de compte, le modèle OCR fonctionnera, espérons-le, mieux pour votre cas d'utilisation spécifique.

Ce tutoriel a été initialement écrit partie par partie sur mon Medium, vous pouvez consulter chaque partie ici :

* [Générer un ensemble de données synthétique pour l'ajustement fin d'un moteur OCR](https://blog.devgenius.io/generating-a-fine-tuning-dataset-for-an-ocr-engine-3509167bc8a1)
* [Comment affiner EasyOCR pour obtenir de meilleures performances OCR](https://pub.towardsai.net/how-to-fine-tune-easyocr-to-achieve-better-ocr-performance-1540f5076428)

Si vous êtes intéressé et souhaitez en savoir plus sur des sujets similaires, vous pouvez me trouver sur :

* [[1;32m✓[0m Medium](https://medium.com/@oieivind)
* [[1;32m✓[0m](https://twitter.com/Ravenspike21) [Twitter](https://twitter.com/Ravenspike21)
* [1;32m✓[0m[LinkedIn](https://www.linkedin.com/in/eivind-kjosbakken/)

Image de couverture : Utilisez l'OCR pour lire des documents. Image réalisée avec DALL-E. OpenAI. (2023). ChatGPT (Grand modèle de langage) [https://chat.openai.com](https://chat.openai.com/).