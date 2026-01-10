---
title: Comment construire un classificateur d'images avec une précision supérieure
  à 97%
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-28T18:03:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-the-best-image-classifier-3c72010b3d55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NRIFYyKmm8XJvQSZNZbaxQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire un classificateur d'images avec une précision supérieure
  à 97%
seo_desc: 'By Anne Bonner

  A clear and complete blueprint for success


  How do you teach a computer to look at an image and correctly identify it as a flower?
  How do you teach a computer to see an image of a flower and then tell you exactly
  what species of flower...'
---

Par Anne Bonner

#### Un plan clair et complet pour réussir

![Image](https://cdn-media-1.freecodecamp.org/images/oQM93I4HcELwQ5DI5fkcCqzPDQdDU1GxP-dx)

Comment enseigner à un ordinateur à regarder une image et à l'identifier correctement comme une fleur ? **Comment enseigner à un ordinateur à voir une image de fleur et à vous dire exactement de quelle espèce de fleur il s'agit lorsque même _vous_ ne savez pas de quelle espèce il s'agit ?**

Laissez-moi vous montrer !

Cet article vous guidera à travers les bases de la création d'un classificateur d'images avec PyTorch. Vous pouvez imaginer utiliser quelque chose comme cela dans une application mobile qui vous donne le nom de la fleur que votre caméra regarde. Vous pourriez, si vous le souhaitez, entraîner ce classificateur et ensuite l'exporter pour l'utiliser dans une application qui vous est propre.

**Ce que vous faites à partir de là dépend entièrement de vous et de votre imagination.**

J'ai rassemblé cet article pour toute personne qui est nouvelle dans tout cela et qui cherche un point de départ. C'est à vous de prendre ces informations, de les améliorer et de vous les approprier !

[Si vous souhaitez consulter le notebook, vous pouvez le trouver ici.](https://github.com/bonn0062/image_classifier_pytorch)

_Pourquoi ce classificateur d'images PyTorch a été construit comme projet final pour un programme Udacity, le code s'inspire du code d'Udacity qui, à son tour, s'inspire de la documentation officielle de PyTorch. Udacity a également fourni un fichier JSON pour le mappage des étiquettes. [Ce fichier peut être trouvé dans ce dépôt GitHub](https://github.com/bonn0062/image_classifier_pytorch)._

[_Les informations sur l'ensemble de données de fleurs peuvent être trouvées ici._](http://www.robots.ox.ac.uk/~vgg/data/flowers/102/) _L'ensemble de données inclut un dossier séparé pour chacune des 102 classes de fleurs. Chaque fleur est étiquetée comme un nombre et chacun des répertoires numérotés contient un certain nombre de fichiers .jpg._

### Commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/7lY8LqdhRvffqUDnmStexLyx-GyNGn9uIDOF)
_Photo par [Unsplash](https://unsplash.com/@anniespratt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Annie Spratt</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Étant donné que c'est un réseau de neurones utilisant un ensemble de données plus grand que ce que mon CPU pourrait gérer en un temps raisonnable, j'ai décidé de configurer mon classificateur d'images dans [Google Colab](https://colab.research.google.com/). Colab est vraiment génial car il fournit un **GPU gratuit**. (Si vous êtes nouveau dans Colab, [consultez cet article pour commencer avec Google Colab](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c) !)

Parce que j'utilisais Colab, j'ai dû commencer par importer PyTorch. Vous n'avez pas besoin de faire cela si vous n'utilisez pas Colab.

***** MISE À JOUR ! (01/29) *** Colab prend désormais en charge PyTorch natif !!! Vous ne devriez pas avoir besoin d'exécuter le code ci-dessous, mais je le laisse au cas où quelqu'un aurait des problèmes !**

```py
# Importer PyTorch si vous utilisez Google Colab
# http://pytorch.org/
from os.path import exists
from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag
platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(), get_abi_tag())
cuda_output = !ldconfig -p|grep cudart.so|sed -e 's/.*\.\([0-9]*\)\.\([0-9]*\)$/cu\1\2/'
accelerator = cuda_output[0] if exists('/dev/nvidia0') else 'cpu'

!pip install -q http://download.pytorch.org/whl/{accelerator}/torch-0.4.1-{platform}-linux_x86_64.whl torchvision
import torch
```

Ensuite, après avoir eu des problèmes avec Pillow (il est bogué dans Colab !), j'ai simplement exécuté ceci :

```py
import PIL
print(PIL.PILLOW_VERSION)
```

Si vous obtenez une version inférieure à 5.3.0, utilisez le menu déroulant sous « Runtime » pour « Redémarrer le runtime » et exécutez cette cellule à nouveau. Vous devriez être prêt à partir !

Vous voudrez utiliser le GPU pour ce projet, ce qui est incroyablement simple à configurer sur Colab. Vous allez simplement dans le menu déroulant « runtime », sélectionnez « changer le type de runtime » et ensuite sélectionnez « GPU » dans le menu déroulant de l'accélérateur matériel !

![Image](https://cdn-media-1.freecodecamp.org/images/BLEUCgK-smvUhkH3UKLXTChyqkclSOAaGHBu)

Ensuite, j'aime exécuter

```py
train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
    print('Dommage ! Entraînement sur CPU ...')
else:
    print('Vous êtes prêt à partir ! Entraînement sur GPU ...')
```

juste pour m'assurer que cela fonctionne. Ensuite, exécutez

```py
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
```

pour définir l'appareil.

Après cela, importez les fichiers. Il existe de nombreuses façons de le faire, y compris le montage de votre Google Drive si vous avez votre ensemble de données stocké là-bas, ce qui est en fait très simple. Même si je n'ai pas trouvé que ce soit la solution la plus utile, je l'inclus ci-dessous, juste parce que c'est si facile et utile.

```py
from google.colab import drive
drive.mount('/content/gdrive')
```

Ensuite, vous verrez un lien, cliquez dessus, autorisez l'accès, copiez le code qui apparaît, collez-le dans la boîte, appuyez sur Entrée, et vous êtes prêt à partir ! Si vous ne voyez pas votre lecteur dans la boîte latérale à gauche, cliquez simplement sur « actualiser » et il devrait apparaître.

(Exécutez la cellule, cliquez sur le lien, copiez le code sur la page, collez-le dans la boîte, appuyez sur Entrée, et vous verrez ceci lorsque vous aurez monté votre lecteur avec succès) :

![Image](https://cdn-media-1.freecodecamp.org/images/nQ9zSmXowwXJDMsxyMu1VGQtuO-iUDP48Ctc)

C'est en fait super facile !

Cependant, si vous préférez télécharger un lien de fichier zip partagé (ce qui s'est avéré plus facile et plus rapide pour ce projet), vous pouvez utiliser :

```
!wget
!unzip
```

Par exemple :

```bash
!wget -cq https://s3.amazonaws.com/content.udacity-data.com/courses/nd188/flower_data.zip
!unzip -qq flower_data.zip
```

Cela vous donnera l'ensemble de données de fleurs d'Udacity en quelques secondes !

(Si vous téléchargez de petits fichiers, vous pouvez simplement les télécharger directement avec un peu de code simple. Cependant, si vous le souhaitez, vous pouvez également aller sur le côté gauche de l'écran et cliquer sur « télécharger des fichiers » si vous n'avez pas envie d'exécuter un peu de code pour récupérer un fichier local.)

![Image](https://cdn-media-1.freecodecamp.org/images/Ge2FEjP46A5IuDJqSh8uPMdG4mWv-OA4-bFJ)

Après avoir chargé les données, j'ai importé les bibliothèques que je voulais utiliser :

```py
%matplotlib inline
%config InlineBackend.figure_format = 'retina'

import time
import json
import copy

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import PIL

from PIL import Image
from collections import OrderedDict

import torch
from torch import nn, optim
from torch.optim import lr_scheduler
from torch.autograd import Variable
import torchvision
from torchvision import datasets, models, transforms
from torch.utils.data.sampler import SubsetRandomSampler
import torch.nn as nn
import torch.nn.functional as F
```

Viennent ensuite les transformations de données ! Vous voulez vous assurer d'utiliser plusieurs types de transformations différents sur votre ensemble d'entraînement afin d'aider votre programme à apprendre autant que possible. Vous pouvez créer un modèle plus robuste en l'entraînant sur des images retournées, tournées et recadrées.

Les moyennes et les écarts types sont fournis pour normaliser les valeurs des images avant de les passer à notre réseau, mais ils peuvent également être trouvés en regardant les valeurs moyennes et les écarts types des différentes dimensions des tenseurs d'images. [La documentation officielle](https://pytorch.org/docs/stable/torchvision/transforms.html) est incroyablement utile ici !

Pour mon classificateur d'images, je l'ai gardé simple avec :

```py
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ]),
    'valid': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ])
}

# Charger les ensembles de données avec ImageFolder
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'valid']}
# Utiliser les ensembles de données d'images et les transformations pour définir les chargeurs de données
batch_size = 64
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size,
                                             shuffle=True, num_workers=4)
              for x in ['train', 'valid']}
              
class_names = image_datasets['train'].classes

dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
class_names = image_datasets['train'].classes
```

Comme vous pouvez le voir ci-dessus, j'ai également défini la taille du lot, les chargeurs de données et les noms de classe dans le code ci-dessus.

Pour jeter un très rapide coup d'œil aux données et vérifier mon appareil, j'ai exécuté :

```py
print(dataset_sizes)
print(device)

{'train': 6552, 'valid': 818}
cuda:0
```

Ensuite, nous devons faire un peu de mappage du numéro d'étiquette au nom réel de la fleur. Udacity a fourni un fichier JSON pour que ce mappage soit fait simplement.

```py
with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)
```

Afin de tester le chargeur de données, exécutez :

```py
images, labels = next(iter(dataloaders['train']))
rand_idx = np.random.randint(len(images))
# Print(rand_idx)
print("label: {}, class: {}, name: {}".format(labels[rand_idx].item(),
                                               class_names[labels[rand_idx].item()],
                                               cat_to_name[class_names[labels[rand_idx].item()]]))
```

Maintenant, cela commence à devenir encore plus excitant ! Un certain nombre de modèles au cours des dernières années ont été créés par des personnes bien plus qualifiées que la plupart d'entre nous pour être réutilisés dans des problèmes de vision par ordinateur. [PyTorch facilite le chargement de modèles pré-entraînés et la construction sur ceux-ci](https://pytorch.org/docs/stable/torchvision/models.html), ce qui est exactement ce que nous allons faire pour ce projet. Le choix du modèle dépend entièrement de vous !

Certains des modèles pré-entraînés les plus populaires, comme ResNet, AlexNet et VGG, proviennent du ImageNet Challenge. Ces modèles pré-entraînés permettent à d'autres d'obtenir rapidement des résultats de pointe en vision par ordinateur sans avoir besoin de telles quantités de puissance informatique, de patience et de temps. J'ai en fait obtenu d'excellents résultats avec DenseNet et j'ai décidé d'utiliser DenseNet161, qui m'a donné de très bons résultats relativement rapidement.

Vous pouvez rapidement configurer cela en exécutant

```py
model = models.densenet161(pretrained=True)
```

mais il pourrait être plus intéressant de vous donner un choix de modèle, d'optimiseur et de planificateur. Afin de configurer un choix d'architecture, exécutez

```py
model_name = 'densenet' #vgg
if model_name == 'densenet':
    model = models.densenet161(pretrained=True)
    num_in_features = 2208
    print(model)
elif model_name == 'vgg':
    model = models.vgg19(pretrained=True)
    num_in_features = 25088
    print(model.classifier)
else:
    print("Modèle inconnu, veuillez choisir 'densenet' ou 'vgg'")
```

ce qui vous permet de configurer rapidement un modèle alternatif.

Après cela, vous pouvez commencer à construire votre classificateur, en utilisant les paramètres qui fonctionnent le mieux pour vous. J'ai construit

```py
for param in model.parameters():
    param.requires_grad = False
def build_classifier(num_in_features, hidden_layers, num_out_features):
   
    classifier = nn.Sequential()
    if hidden_layers == None:
        classifier.add_module('fc0', nn.Linear(num_in_features, 102))
    else:
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        classifier.add_module('fc0', nn.Linear(num_in_features, hidden_layers[0]))
        classifier.add_module('relu0', nn.ReLU())
        classifier.add_module('drop0', nn.Dropout(.6))
        classifier.add_module('relu1', nn.ReLU())
        classifier.add_module('drop1', nn.Dropout(.5))
        for i, (h1, h2) in enumerate(layer_sizes):
            classifier.add_module('fc'+str(i+1), nn.Linear(h1, h2))
            classifier.add_module('relu'+str(i+1), nn.ReLU())
            classifier.add_module('drop'+str(i+1), nn.Dropout(.5))
        classifier.add_module('output', nn.Linear(hidden_layers[-1], num_out_features))
        
    return classifier
```

ce qui permet de changer facilement le nombre de couches cachées que j'utilise, ainsi que d'ajuster rapidement le taux de dropout. Vous pouvez décider d'ajouter des couches ReLU et dropout supplémentaires afin d'affiner plus précisément votre modèle.

Ensuite, travaillez sur l'entraînement des paramètres de votre classificateur. J'ai décidé de m'assurer que je n'entraînais que les paramètres du classificateur ici tout en ayant les paramètres des caractéristiques gelés. Vous pouvez être aussi créatif que vous le souhaitez avec votre optimiseur, votre critère et votre planificateur. Le critère est la méthode utilisée pour évaluer l'ajustement du modèle, l'optimiseur est la méthode d'optimisation utilisée pour mettre à jour les poids, et le planificateur fournit différentes méthodes pour ajuster le taux d'apprentissage et la taille de pas utilisés pendant l'optimisation.

Essayez autant d'options et de combinaisons que possible pour voir ce qui vous donne le meilleur résultat. [Vous pouvez voir toute la documentation officielle ici.](https://pytorch.org/docs/stable/optim.html) Je vous recommande de la consulter et de prendre vos propres décisions sur ce que vous voulez utiliser. Vous n'avez pas littéralement un nombre infini d'options ici, mais cela y ressemble une fois que vous commencez à jouer avec !

```py
hidden_layers = None

classifier = build_classifier(num_in_features, hidden_layers, 102)
print(classifier)

# N'entraîner que les paramètres du classificateur, les paramètres des caractéristiques sont gelés
if model_name == 'densenet':
    model.classifier = classifier
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adadelta(model.parameters())
    sched = optim.lr_scheduler.StepLR(optimizer, step_size=4)
elif model_name == 'vgg':
    model.classifier = classifier
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=0.0001)
    sched = lr_scheduler.StepLR(optimizer, step_size=4, gamma=0.1)
else:
    pass
```

Maintenant, il est temps d'entraîner votre modèle.

```py
# Adapté de https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

def train_model(model, criterion, optimizer, sched, num_epochs=5):
    since = time.time()
    
best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    
for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch+1, num_epochs))
        print('-' * 10)
        
# Chaque époque a une phase d'entraînement et une phase de validation
        for phase in ['train', 'valid']:
            if phase == 'train':
                model.train()  # Mettre le modèle en mode entraînement
            else:
                model.eval()   # Mettre le modèle en mode évaluation
                
running_loss = 0.0
            running_corrects = 0
            
# Itérer sur les données.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)
                
# Mettre à zéro les gradients des paramètres
                optimizer.zero_grad()
                
# Avant
                # suivre l'historique uniquement en entraînement
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)
                    
# Rétropropagation + optimisation uniquement si en phase d'entraînement
                    if phase == 'train':
                        #sched.step()
                        loss.backward()
                        
                        optimizer.step()
                        
# Statistiques
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
                
epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]
            
print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))
                
# Copie profonde du modèle
            if phase == 'valid' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
                
print()

time_elapsed = time.time() - since
    print('Entraînement terminé en {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Meilleure précision de validation : {:4f}'.format(best_acc))
    
# Charger les meilleurs poids du modèle
    model.load_state_dict(best_model_wts)
    
    return model
    
epochs = 30
model.to(device)
model = train_model(model, criterion, optimizer, sched, epochs)
```

Je voulais pouvoir surveiller mes époques facilement et également garder une trace du temps écoulé pendant que mon modèle fonctionnait. Le code ci-dessus inclut les deux, et les résultats sont assez bons ! Vous pouvez voir que le modèle apprend rapidement et que la précision sur l'ensemble de validation a rapidement atteint plus de 95 % à l'époque 7 !

```
Epoch 1/30
----------
train Loss: 2.4793 Acc: 0.4791
valid Loss: 0.9688 Acc: 0.8191

Epoch 2/30
----------
train Loss: 0.8288 Acc: 0.8378
valid Loss: 0.4714 Acc: 0.9010

Epoch 3/30
----------
train Loss: 0.5191 Acc: 0.8890
valid Loss: 0.3197 Acc: 0.9181

Epoch 4/30
----------
train Loss: 0.4064 Acc: 0.9095
valid Loss: 0.2975 Acc: 0.9169

Epoch 5/30
----------
train Loss: 0.3401 Acc: 0.9214
valid Loss: 0.2486 Acc: 0.9401

Epoch 6/30
----------
train Loss: 0.3111 Acc: 0.9303
valid Loss: 0.2153 Acc: 0.9487

Epoch 7/30
----------
train Loss: 0.2987 Acc: 0.9298
valid Loss: 0.1969 Acc: 0.9584

...

Entraînement terminé en 67m 43s
Meilleure précision de validation : 0.973105
```

Vous pouvez voir que l'exécution de ce code sur Google Colab avec GPU a pris un peu plus d'une heure.

Maintenant, il est temps pour l'évaluation

```py
model.eval()

accuracy = 0

for inputs, labels in dataloaders['valid']:
    inputs, labels = inputs.to(device), labels.to(device)
    outputs = model(inputs)
    
    # Classe avec la probabilité la plus élevée est notre classe prédite
    equality = (labels.data == outputs.max(1)[1])

# Précision = nombre de prédictions correctes divisé par toutes les prédictions
    accuracy += equality.type_as(torch.FloatTensor()).mean()
    
print("Précision du test : {:.3f}".format(accuracy/len(dataloaders['valid'])))

Précision du test : 0.973
```

Il est important de sauvegarder votre point de contrôle

```py
model.class_to_idx = image_datasets['train'].class_to_idx

checkpoint = {'input_size': 2208,
              'output_size': 102,
              'epochs': epochs,
              'batch_size': 64,
              'model': models.densenet161(pretrained=True),
              'classifier': classifier,
              'scheduler': sched,
              'optimizer': optimizer.state_dict(),
              'state_dict': model.state_dict(),
              'class_to_idx': model.class_to_idx
             }
   

torch.save(checkpoint, 'checkpoint.pth')
```

Vous n'avez pas à sauvegarder tous les paramètres, mais je les inclue ici à titre d'exemple. Ce point de contrôle sauvegarde spécifiquement le modèle avec une architecture densenet161 pré-entraînée, mais si vous souhaitez sauvegarder votre point de contrôle avec l'option à deux choix, vous pouvez absolument le faire. Il suffit d'ajuster la taille d'entrée et le modèle.

Maintenant, vous êtes en mesure de charger votre point de contrôle. Si vous soumettez votre projet dans l'espace de travail Udacity, les choses peuvent devenir un peu délicates. [Voici de l'aide pour le dépannage de votre chargement de point de contrôle](https://towardsdatascience.com/load-that-checkpoint-51142d44fb5d).

Vous pouvez vérifier vos clés en exécutant

```py
ckpt = torch.load('checkpoint.pth')
ckpt.keys()
```

Ensuite, chargez et reconstruisez votre modèle !

```py
def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = checkpoint['model']
    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    optimizer = checkpoint['optimizer']
    epochs = checkpoint['epochs']
    
    for param in model.parameters():
        param.requires_grad = False
        
    return model, checkpoint['class_to_idx']
    
model, class_to_idx = load_checkpoint('checkpoint.pth')
```

Voulez-vous continuer ? C'est une bonne idée de faire un peu de prétraitement d'image et d'inférence pour la classification. Allez-y et définissez votre chemin d'image et ouvrez une image :

```py
image_path = 'flower_data/valid/102/image_08006.jpg'
img = Image.open(image_path)
```

Traitez votre image et jetez un coup d'œil à une image traitée :

```py
def process_image(image):
    ''' Redimensionne, recadre et normalise une image PIL pour un modèle PyTorch,
        retourne un tableau Numpy
    '''
    # Traiter une image PIL pour une utilisation dans un modèle PyTorch
    # tensor.numpy().transpose(1, 2, 0)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                             std=[0.229, 0.224, 0.225])
    ])
    image = preprocess(image)
    return image
def imshow(image, ax=None, title=None):
    """Imshow pour Tensor."""
    if ax is None:
        fig, ax = plt.subplots()
    
    # Les tenseurs PyTorch supposent que le canal de couleur est la première dimension
    # mais matplotlib suppose que c'est la troisième dimension
    image = image.numpy().transpose((1, 2, 0))
    
    # Annuler le prétraitement
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    image = std * image + mean
    
    # L'image doit être rognée entre 0 et 1 ou elle ressemble à du bruit lorsqu'elle est affichée
    image = np.clip(image, 0, 1)
    
    ax.imshow(image)
    
    return ax
with Image.open('flower_data/valid/102/image_08006.jpg') as image:
    plt.imshow(image)
    
model.class_to_idx = image_datasets['train'].class_to_idx
```

![Image](https://cdn-media-1.freecodecamp.org/images/IBg2uwerD1Iap7RxV3h0k1LWvci-yMrHyVhN)

Créez une fonction pour la prédiction :

```py
def predict2(image_path, model, topk=5):
    ''' Prédire la classe (ou les classes) d'une image en utilisant un modèle d'apprentissage profond entraîné.
    '''
    
    # Implémenter le code pour prédire la classe à partir d'un fichier image
    img = Image.open(image_path)
    img = process_image(img)
    
    # Convertir l'image 2D en vecteur 1D
    img = np.expand_dims(img, 0)
    
    
    img = torch.from_numpy(img)
    
    model.eval()
    inputs = Variable(img).to(device)
    logits = model.forward(inputs)
    
    ps = F.softmax(logits,dim=1)
    topk = ps.cpu().topk(topk)
    
    return (e.data.numpy().squeeze().tolist() for e in topk)
```

Une fois les images dans le bon format, vous pouvez écrire une fonction pour faire des prédictions avec votre modèle. Une pratique courante consiste à prédire les 5 classes les plus probables (généralement appelées top-KK). Vous voudrez calculer les probabilités de classe puis trouver les KK valeurs les plus grandes.

Pour obtenir les KK valeurs les plus grandes dans un tenseur, utilisez k.topk(). Cette méthode retourne à la fois les k probabilités les plus élevées et les indices de ces probabilités correspondant aux classes. Vous devez convertir ces indices en étiquettes de classe réelles en utilisant class_to_idx, que vous avez ajouté au modèle ou à partir du dossier d'images que vous avez utilisé pour charger les données. Assurez-vous d'inverser le dictionnaire afin d'obtenir un mappage de l'index à la classe également.

Cette méthode doit prendre un chemin vers une image et un point de contrôle de modèle, puis retourner les probabilités et les classes.

```py
img_path = 'flower_data/valid/18/image_04252.jpg'
probs, classes = predict2(img_path, model.to(device))
print(probs)
print(classes)
flower_names = [cat_to_name[class_names[e]] for e in classes]
print(flower_names)
```

J'étais assez satisfaite des performances de mon modèle !

```
[0.9999195337295532, 1.4087702766119037e-05, 1.3897360986447893e-05, 1.1400215043977369e-05, 6.098791800468462e-06]
[12, 86, 7, 88, 40]
['lis peruvien', 'rose du désert', 'king protea', 'magnolia', 'lis épée']
```

En gros, il est presque certain à 100 % que l'image que j'ai spécifiée est un Lis Péruvien. Vous voulez jeter un coup d'œil ? Essayez d'utiliser matplotlib pour tracer les probabilités des cinq classes principales dans un graphique à barres ainsi que l'image d'entrée :

```py
def view_classify(img_path, prob, classes, mapping):
    ''' Fonction pour visualiser une image et ses classes prédites.
    '''
    image = Image.open(img_path)
fig, (ax1, ax2) = plt.subplots(figsize=(6,10), ncols=1, nrows=2)
    flower_name = mapping[img_path.split('/')[-2]]
    ax1.set_title(flower_name)
    ax1.imshow(image)
    ax1.axis('off')
    
    y_pos = np.arange(len(prob))
    ax2.barh(y_pos, prob, align='center')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(flower_names)
    ax2.invert_yaxis()  # les étiquettes se lisent de haut en bas
    ax2.set_title('Probabilité de classe')
    
view_classify(img_path, probs, classes, cat_to_name)
```

Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/-j60QPFXGBWQNDpGY1Du94iqMVcAH4rrmJR1)

Je dois dire que je suis assez satisfaite de cela ! Je recommande de tester quelques autres images pour voir à quel point vos prédictions sont proches sur une variété d'images.

![Image](https://cdn-media-1.freecodecamp.org/images/Ax7ffcJVq0xFPUzTs7Mek33N5BmtKJ3VcPiK)

Maintenant, il est temps de créer un modèle qui vous est propre et de me faire savoir comment cela se passe dans les réponses ci-dessous !

![Image](https://cdn-media-1.freecodecamp.org/images/Cf2-EYuEAv9bjmmRUXJxKRO6c6Pe6dXfEqZR)
_Photo par [Unsplash](https://unsplash.com/@pezgonzalez?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Pez Gonz e1lez</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Avez-vous terminé votre modèle d'apprentissage profond ou de machine learning, mais vous ne savez pas quoi en faire ensuite ? Pourquoi ne pas le déployer sur Internet ?

**Mettez votre modèle en ligne pour que tout le monde puisse le voir !**

[Consultez cet article pour apprendre comment déployer votre modèle de machine learning avec Flask](https://heartbeat.fritz.ai/brilliant-beginners-guide-to-model-deployment-133e158f6717) !