---
title: Comment j'ai construit un reconnaisseur d'écriture manuscrite et l'ai publié
  sur l'App Store
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T21:33:11.000Z'
originalURL: https://freecodecamp.org/news/build-a-handwriting-recognizer-ship-it-to-app-store-fcce24205b4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pZ12Pa-cCEs64Mf44ubmog.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: iOS
  slug: ios
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit un reconnaisseur d'écriture manuscrite et l'ai publié
  sur l'App Store
seo_desc: 'By Melody Yang

  From constructing a Convolutional Neural Network to deploying an OCR to iOS

  The Motivation for the Project ✍️ ??

  While I was learning how to create deep learning models for the MNIST dataset a
  few months ago, I ended up making an iOS a...'
---

Par Melody Yang

#### De la construction d'un réseau de neurones convolutionnel au déploiement d'un OCR sur iOS

### La motivation pour le projet ✍️ ??

Alors que j'apprenais à créer des modèles de deep learning pour le [jeu de données MNIST](https://en.wikipedia.org/wiki/MNIST_database) il y a quelques mois, j'ai fini par créer une application iOS qui reconnaissait les caractères manuscrits.

Mon ami Kaichi Momose développait une application d'apprentissage de la langue japonaise, [Nukon](http://bit.ly/nukon-app). Il voulait par hasard une fonctionnalité similaire. Nous avons ensuite collaboré pour construire quelque chose de plus sophistiqué qu'un reconnaisseur de chiffres : un [OCR (Optical Character Recognition/Reader)](https://en.wikipedia.org/wiki/Optical_character_recognition) pour les caractères japonais ([Hiragana](https://en.wikipedia.org/wiki/Hiragana) et [Katakana](https://en.wikipedia.org/wiki/Katakana)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Iy1B42dQjgAaYwweyrUA-g.gif)
_[Hiragana & Katakana de base](http://www.kanjipower.com/jws/hiragana.php" rel="noopener" target="_blank" title=")_

Pendant le développement de Nukon, il n'y avait pas d'API disponible pour la reconnaissance de l'écriture manuscrite en japonais. Nous n'avions pas d'autre choix que de construire notre propre OCR. Le plus grand avantage que nous avons obtenu en construisant un OCR à partir de zéro est que le nôtre fonctionne hors ligne. Les utilisateurs peuvent être profondément dans les montagnes sans internet et toujours ouvrir Nukon pour maintenir leur routine quotidienne d'apprentissage du japonais. Nous avons beaucoup appris tout au long du processus, mais plus important encore, nous étions ravis de livrer un meilleur produit pour nos utilisateurs.

Cet article décomposera le processus de construction d'un OCR japonais pour les applications iOS. Pour ceux qui souhaitent en construire un pour d'autres langues/symboles, n'hésitez pas à le personnaliser en changeant le jeu de données.

Sans plus attendre, voyons ce qui sera couvert :

**Partie 1️⃣ : Obtenir le jeu de données et pré-traiter les images**  
**Partie 2️⃣ : Construire & entraîner le CNN (Convolutional Neural Network)**  
**Partie 3️⃣ : Intégrer le modèle entraîné dans iOS**

![Image](https://cdn-media-1.freecodecamp.org/images/1*TZHSfqQ9CUAuBR_o2AhdZA.png)
_À quoi pourrait ressembler l'application finale (démo provient de [Recogmize](http://bit.ly/recogmize" rel="noopener" target="_blank" title="))_

### Obtenir le jeu de données & Pré-traiter les images ?

Le jeu de données provient de la [base de données de caractères ETL](http://etlcdb.db.aist.go.jp), qui contient neuf ensembles d'images de caractères et de symboles manuscrits. Puisque nous allons construire un OCR pour Hiragana, [ETL8](http://etlcdb.db.aist.go.jp/?page_id=2461) est le jeu de données que nous allons utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pZ12Pa-cCEs64Mf44ubmog.png)
_Images du caractère manuscrit « あ » produites par 160 écrivains (de ETL8)_

Pour obtenir les images de la base de données, nous avons besoin de quelques fonctions auxiliaires qui lisent et stockent les images au format `.npz`.

```py
import struct
import numpy as np
from PIL import Image

sz_record = 8199

def read_record_ETL8G(f):
    s = f.read(sz_record)
    r = struct.unpack('>2H8sI4B4H2B30x8128s11x', s)
    iF = Image.frombytes('F', (128, 127), r[14], 'bit', 4)
    iL = iF.convert('L')
    return r + (iL,)
  
def read_hiragana():
    # Type de caractères = 70, personne = 160, y = 127, x = 128
    ary = np.zeros([71, 160, 127, 128], dtype=np.uint8)

    for j in range(1, 33):
        filename = '../../ETL8G/ETL8G_{:02d}'.format(j)
        with open(filename, 'rb') as f:
            for id_dataset in range(5):
                moji = 0
                for i in range(956):
                    r = read_record_ETL8G(f)
                    if b'.HIRA' in r[2] or b'.WO.' in r[2]:
                        if not b'KAI' in r[2] and not b'HEI' in r[2]:
                            ary[moji, (j - 1) * 5 + id_dataset] = np.array(r[-1])
                            moji += 1
    np.savez_compressed("hiragana.npz", ary)
```

Une fois que nous avons sauvegardé `hiragana.npz`, commençons à traiter les images en chargeant le fichier et en **redimensionnant les dimensions des images à 32x32 pixels**. Nous ajouterons également une augmentation de données pour générer des images supplémentaires qui sont tournées et zoomées. Lorsque notre modèle est entraîné sur des images de caractères sous divers angles, notre modèle peut mieux s'adapter à l'écriture manuscrite des gens.

```py
import scipy.misc
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

# 71 caractères
nb_classes = 71
# dimensions de l'image d'entrée
img_rows, img_cols = 32, 32

ary = np.load("hiragana.npz")['arr_0'].reshape([-1, 127, 128]).astype(np.float32) / 15
X_train = np.zeros([nb_classes * 160, img_rows, img_cols], dtype=np.float32)
for i in range(nb_classes * 160):
    X_train[i] = scipy.misc.imresize(ary[i], (img_rows, img_cols), mode='F')
 
y_train = np.repeat(np.arange(nb_classes), 160)

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

# convertir les vecteurs de classe en matrices catégorielles
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)

# augmentation des données
datagen = ImageDataGenerator(rotation_range=15, zoom_range=0.20)
datagen.fit(X_train)
```

### Construire et entraîner le CNN ?

Voici la partie amusante ! Nous allons utiliser Keras pour construire un CNN (Convolutional Neural Network) pour notre modèle. Lorsque j'ai construit le modèle pour la première fois, j'ai expérimenté avec des hyper-paramètres et les ai ajustés plusieurs fois. La combinaison ci-dessous m'a donné la plus haute précision — 98,77 %. N'hésitez pas à jouer avec différents paramètres vous-même.

```py
model = Sequential()

def model_6_layers():
    model.add(Conv2D(32, 3, 3, input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Conv2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(Conv2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))

model_6_layers()

model.compile(loss='categorical_crossentropy', 
              optimizer='adam', metrics=['accuracy'])
model.fit_generator(datagen.flow(X_train, y_train, batch_size=16), 
                    samples_per_epoch=X_train.shape[0],
                    nb_epoch=30, validation_data=(X_test, y_test))
```

Voici quelques conseils si vous trouvez **les performances du modèle insatisfaisantes** lors de l'étape d'entraînement :

#### Le modèle est en _surcharge_ (overfitting)

Cela signifie que le modèle n'est pas bien généralisé. Consultez cet [article](https://elitedatascience.com/overfitting-in-machine-learning#overfitting-vs-underfitting) pour des explications intuitives.

**Comment détecter le surapprentissage** : `acc` (précision) continue d'augmenter, mais `val_acc` (précision de validation) fait le contraire lors du processus d'entraînement.

**Quelques solutions pour le surapprentissage** : régularisation (ex. abandon), augmentation des données, amélioration de la qualité du jeu de données

#### Comment savoir si le modèle est en train d'« apprendre »

Le modèle n'apprend pas si `val_loss` (perte de validation) augmente ou ne diminue pas au fur et à mesure que l'entraînement avance.

Utilisez [TensorBoard](https://keras.io/callbacks/#tensorboard) — il fournit des visualisations des performances du modèle au fil du temps. Il élimine la tâche fastidieuse de regarder chaque époque et de comparer constamment les valeurs.

Alors que nous sommes satisfaits de notre précision, nous supprimons les couches d'abandon avant de sauvegarder les poids et la configuration du modèle dans un fichier.

```py
for k in model.layers:
    if type(k) is keras.layers.Dropout:
        model.layers.remove(k)
        
model.save('hiraganaModel.h5')
```

La seule tâche restante avant de passer à la partie iOS est de convertir `hiraganaModel.h5` en un modèle CoreML.

```py
import coremltools

output_labels = [
'あ', 'い', 'う', 'え', 'お',
'か', 'き', 'く', 'け', 'こ',
'さ', 'し', 'す', 'せ', 'そ',
'た', 'ち', 'つ', 'て', 'と',
'な', 'に', 'ぬ', 'ね', 'の',
'は', 'ひ', 'ふ', 'へ', 'ほ',
'ま', 'み', 'む', 'め', 'も',
'や', 'ゆ', 'よ', 'ら', 'り',
'る', 'れ', 'ろ', 'わ', 'が',
'ぎ', 'ぐ', 'げ', 'ご', 'ざ',
'じ', 'ず', 'ぜ', 'ぞ', 'だ',
'ぢ', 'づ', 'で', 'ど', 'ば',
'び', 'ぶ', 'べ', 'ぼ', 'ぱ',
'ぴ', 'ぷ', 'ぺ', 'ぽ', 'を',
'ん', 'ゔ', 'ゕ', 'ゖ']

scale = 1/255.

coreml_model = coremltools.converters.keras.convert('./hiraganaModel.h5',
                                                    input_names='image',
                                                    image_input_names='image',
                                                    output_names='output',
                                                    class_labels= output_labels,
                                                    image_scale=scale)
coreml_model.author = 'Votre Nom'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Détecter un caractère hiragana à partir de l'écriture manuscrite'
coreml_model.input_description['image'] = 'Image en niveaux de gris contenant un caractère manuscrit'
coreml_model.output_description['output'] = 'Sortie d'un caractère en hiragana'
coreml_model.save('hiraganaModel.mlmodel')
```

Les `output_labels` sont toutes les sorties possibles que nous verrons plus tard dans iOS.

Fait amusant : si vous comprenez le japonais, vous savez peut-être que l'ordre des caractères de sortie ne correspond pas à l'ordre « alphabétique » du Hiragana. Il nous a fallu un certain temps pour réaliser que les images dans ETL8 n'étaient pas dans l'ordre « alphabétique » (merci à Kaichi de l'avoir réalisé). Le jeu de données a été compilé par une université japonaise, cependant...

### Intégrer le modèle entraîné dans iOS ?

Nous mettons enfin tout ensemble ! Glissez-déposez `hiraganaModel.mlmodel` dans un projet Xcode. Vous verrez alors quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*axV4LC7bbb-QfvWtdwYnjA.png)
_Détails du mlmodel dans l'espace de travail Xcode_

**Note** : Xcode créera un espace de travail lors de la copie du modèle. Nous devons basculer notre environnement de codage vers l'**espace de travail**, sinon le modèle ML ne fonctionnera pas !

L'objectif final est d'avoir notre modèle Hiragana prédire un caractère en passant une image. Pour y parvenir, nous allons créer une interface utilisateur simple pour que l'utilisateur puisse écrire, et nous allons stocker l'écriture de l'utilisateur dans un format d'image. Enfin, nous récupérons les valeurs de pixels de l'image et les transmettons à notre modèle.

Faisons cela étape par étape :

1. « Dessiner » des caractères sur `UIView` avec `UIBezierPath`

```swift
import UIKit

class viewController: UIViewController {

    @IBOutlet weak var canvas: UIView!
    var path = UIBezierPath()
    var startPoint = CGPoint()
    var touchPoint = CGPoint()
  
    override func viewDidLoad() {
        super.viewDidLoad()
        canvas.clipsToBounds = true
        canvas.isMultipleTouchEnabled = true
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        if let point = touch?.location(in: canvas) {
            startPoint = point
        }
    }
  
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        if let point = touch?.location(in: canvas) {
            touchPoint = point
        }
        
        path.move(to: startPoint)
        path.addLine(to: touchPoint)
        startPoint = touchPoint
        draw()
    }
    
    func draw() {
        let strokeLayer = CAShapeLayer()
        strokeLayer.fillColor = nil
        strokeLayer.lineWidth = 8
        strokeLayer.strokeColor = UIColor.orange.cgColor
        strokeLayer.path = path.cgPath
        canvas.layer.addSublayer(strokeLayer)
    }
    
    // effacer le dessin dans la vue
    @IBAction func clearPressed(_ sender: UIButton) {
        path.removeAllPoints()
        canvas.layer.sublayers = nil
        canvas.setNeedsDisplay()
    }
}
```

La couleur `strokeLayer.strokeColor` peut être n'importe quelle couleur. Cependant, la couleur de fond de `canvas` doit être **noire**. Bien que nos images d'entraînement aient un fond blanc et des traits noirs, le modèle ML ne réagit pas bien à une image d'entrée avec ce style.

2. Transformer `UIView` en `UIImage` et récupérer les valeurs de pixels avec [CVPixelBuffer](https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e)

Dans l'extension, il y a deux fonctions auxiliaires. Ensemble, elles traduisent les images en un tampon de pixels, ce qui est équivalent aux valeurs de pixels. Les dimensions `width` et `height` doivent toutes deux être **32** puisque **les dimensions d'entrée de notre modèle sont de 32 par 32 pixels.**

Dès que nous avons le `pixelBuffer`, nous pouvons appeler `model.prediction()` et passer `pixelBuffer`. Et voilà ! Nous pouvons obtenir une sortie de `classLabel` !

```swift
@IBAction func recognizePressed(_ sender: UIButton) {
        // Transformer la vue en une image
        let resultImage = UIImage.init(view: canvas)
        let pixelBuffer = resultImage.pixelBufferGray(width: 32, height: 32)
        let model = hiraganaModel3()
        // sortie d'un caractère Hiragana
        let output = try? model.prediction(image: pixelBuffer!)
        print(output?.classLabel)
}

extension UIImage {
    // Redimensionne l'image à width x height et la convertit en un CVPixelBuffer en niveaux de gris
    func pixelBufferGray(width: Int, height: Int) -> CVPixelBuffer? {
        return _pixelBuffer(width: width, height: height,
                           pixelFormatType: kCVPixelFormatType_OneComponent8,
                           colorSpace: CGColorSpaceCreateDeviceGray(),
                           alphaInfo: .none)
    }
    
    func _pixelBuffer(width: Int, height: Int, pixelFormatType: OSType,
                     colorSpace: CGColorSpace, alphaInfo: CGImageAlphaInfo) -> CVPixelBuffer? {
        var maybePixelBuffer: CVPixelBuffer?
        let attrs = [kCVPixelBufferCGImageCompatibilityKey: kCFBooleanTrue,
                     kCVPixelBufferCGBitmapContextCompatibilityKey: kCFBooleanTrue]
        let status = CVPixelBufferCreate(kCFAllocatorDefault,
                                         width,
                                         height,
                                         pixelFormatType,
                                         attrs as CFDictionary,
                                         &maybePixelBuffer)
        
        guard status == kCVReturnSuccess, let pixelBuffer = maybePixelBuffer else {
            return nil
        }
        
        CVPixelBufferLockBaseAddress(pixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
        let pixelData = CVPixelBufferGetBaseAddress(pixelBuffer)
        
        guard let context = CGContext(data: pixelData,
                                      width: width,
                                      height: height,
                                      bitsPerComponent: 8,
                                      bytesPerRow: CVPixelBufferGetBytesPerRow(pixelBuffer),
                                      space: colorSpace,
                                      bitmapInfo: alphaInfo.rawValue)
            else {
                return nil
        }
        
        UIGraphicsPushContext(context)
        context.translateBy(x: 0, y: CGFloat(height))
        context.scaleBy(x: 1, y: -1)
        self.draw(in: CGRect(x: 0, y: 0, width: width, height: height))
        UIGraphicsPopContext()
        
        CVPixelBufferUnlockBaseAddress(pixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
        return pixelBuffer
    }
}

```

3. Afficher la sortie avec `UIAlertController`

Cette étape est totalement optionnelle. Comme montré dans le GIF au début, j'ai ajouté un contrôleur d'alerte pour informer du résultat.

```swift
func informResultPopUp(message: String) {
        let alertController = UIAlertController(title: message, 
                                                message: nil, 
                                                preferredStyle: .alert)
        let ok = UIAlertAction(title: "Ok", style: .default, handler: { action in
            self.dismiss(animated: true, completion: nil)
        })
        alertController.addAction(ok)
        self.present(alertController, animated: true) { () in
        }
}
```

Et voilà ! Nous venons de construire un OCR prêt pour une démonstration (et prêt pour l'App Store) ! ??

### Conclusion ?

Construire un OCR n'est pas si difficile. Comme vous l'avez vu, cet article se compose d'étapes et de problèmes auxquels j'ai été confrontée lors de la construction de ce projet. J'ai apprécié le processus de transformation d'un ensemble de code Python en une démonstration en le connectant avec iOS, et j'ai l'intention de continuer à le faire.

J'espère que cet article fournit des informations utiles à ceux qui veulent construire un OCR mais ne savent pas par où commencer.

Vous pouvez trouver le **code source** [ici](https://github.com/melodyfs/Build_OCR)_._

**Bonus** : si vous êtes intéressé par l'expérimentation avec des algorithmes peu profonds, continuez à lire !

### [Optionnel] Entraînement avec des algorithmes peu profonds ?

Avant d'implémenter le CNN, Kaichi et moi avons testé d'autres algorithmes d'apprentissage automatique pour voir s'ils pouvaient faire le travail (et nous faire économiser quelques coûts de calcul !). Nous avons choisi KNN et Random Forest.

Pour évaluer leurs performances, nous avons défini notre précision de base à 1/71 = 0,014.

Nous avons supposé qu'une personne sans aucune connaissance de la langue japonaise pourrait avoir 1,4 % de chances de deviner correctement un caractère.

Ainsi, le modèle se porterait bien si sa précision pouvait dépasser 1,4 %. Voyons si c'était le cas. ?

#### KNN

![Image](https://cdn-media-1.freecodecamp.org/images/1*FVM7oO8WGGDrCY-fBsU8Qw.png)
_Entraîné avec KNN_

La précision finale que nous avons obtenue était de 54,84 %. Bien plus élevée que 1,4 % déjà !

#### Random Forest

![Image](https://cdn-media-1.freecodecamp.org/images/1*B8NjOqzuBj9dOqob5hI3Rg.png)
_Entraîné avec Random Forest_

Une précision de 79,23 %, donc Random Forest a dépassé nos attentes. En ajustant les hyper-paramètres, nous avons obtenu de meilleurs résultats en augmentant le nombre d'estimateurs et la profondeur des arbres. Nous avons pensé que le fait d'avoir plus d'arbres (estimateurs) dans la forêt signifiait que plus de caractéristiques de l'image étaient apprises. De plus, plus l'arbre est profond, plus il apprend de détails à partir des caractéristiques.

Si vous êtes intéressé à en apprendre davantage, j'ai trouvé cet [article](http://www.cs.huji.ac.il/~daphna/course/CoursePapers/bosch07a.pdf) qui discute de la classification d'images avec Random Forest.

_Merci d'avoir lu. Toutes les pensées et retours sont les bienvenus !_