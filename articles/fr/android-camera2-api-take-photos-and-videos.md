---
title: Android Camera2 – Comment utiliser l'API Camera2 pour prendre des photos et
  des vidéos
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-07-29T22:36:44.000Z'
originalURL: https://freecodecamp.org/news/android-camera2-api-take-photos-and-videos
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/0_0d3MvPnozsSTafWk.jpg
tags:
- name: Android
  slug: android
- name: Photography
  slug: photography
- name: video
  slug: video
seo_title: Android Camera2 – Comment utiliser l'API Camera2 pour prendre des photos
  et des vidéos
seo_desc: "We all use the camera on our phones and we use it a l-o-t. There are even\
  \ some applications that have integrated the camera as a feature. \nOn one end,\
  \ there is a standard way of interacting with the camera. On the other, there is\
  \ a way to customize y..."
---

Nous utilisons tous la caméra de nos téléphones et nous l'utilisons b-e-a-u-c-o-u-p. Il existe même certaines applications qui ont intégré la caméra comme fonctionnalité. 

D'une part, il existe une manière standard d'interagir avec la caméra. D'autre part, il existe un moyen de personnaliser votre interaction avec la caméra. Cette distinction est importante à faire. Et c'est là que Camera2 intervient.

## Qu'est-ce que Camera2 ?

Bien qu'elle soit disponible depuis le niveau d'API 21, l'API Camera2 est l'une des architectures les plus complexes que les développeurs doivent gérer. 

Cette API et son prédécesseur ont été mis en place pour que les développeurs puissent exploiter la puissance de l'interaction avec la caméra à l'intérieur de leurs applications. 

De la même manière qu'il existe un moyen d'interagir avec le microphone ou le volume de l'appareil, l'API Camera2 vous donne les outils pour interagir avec la caméra de l'appareil. 

En général, si vous souhaitez utiliser l'API Camera2, ce serait probablement pour plus que simplement prendre une photo ou enregistrer une vidéo. Cela est dû au fait que l'API vous permet d'avoir un contrôle approfondi de la caméra en exposant diverses classes qui devront être configurées par appareil spécifique.

Même si vous avez déjà traité avec la caméra auparavant, c'est un changement si drastique par rapport à l'ancienne API de la caméra que vous pouvez tout aussi bien oublier tout ce que vous savez. 

Il existe une tonne de ressources qui tentent de montrer comment utiliser cette API directement, mais certaines peuvent être obsolètes et d'autres ne présentent pas l'ensemble du tableau. 

Ainsi, au lieu d'essayer de combler les pièces manquantes par vous-même, cet article sera (espérons-le) votre guichet unique pour interagir avec l'API Camera2.

## Cas d'utilisation de Camera2

Avant de plonger dans quoi que ce soit, il est important de comprendre que si vous souhaitez uniquement utiliser la caméra pour prendre une photo ou pour enregistrer une vidéo, vous n'avez pas besoin de vous embêter avec l'API Camera2. 

La raison principale d'utiliser l'API Camera2 est si votre application nécessite une interaction personnalisée avec la caméra ou ses fonctionnalités. 

Si vous êtes intéressé par faire ce qui précède plutôt que ce qui suit, je vous suggère de visiter la documentation suivante de Google :

1. [Prendre des photos](https://developer.android.com/training/camera/photobasics)
2. [Capturer une vidéo](https://developer.android.com/training/camera/videobasics)

Là, vous trouverez toutes les étapes nécessaires à suivre pour capturer de superbes photos et vidéos avec votre caméra. Mais dans cet article, l'accent principal sera mis sur comment utiliser Camera2.

Maintenant, il y a certaines choses que nous devons ajouter à notre fichier manifest :

Permissions de la caméra :

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Fonctionnalité de la caméra :

```xml
<uses-feature android:name="android.hardware.camera" />
```

Vous devrez gérer la vérification si la permission de la caméra a été accordée ou non, mais comme ce sujet a été largement couvert, nous ne traiterons pas de cela dans cet article.

## Comment configurer les composants de l'API Camera2

L'API Camera2 introduit plusieurs nouvelles interfaces et classes. Décomposons chacune d'entre elles pour mieux comprendre comment les utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/1_nPqyLhTqxaqRytV8lV41VA.png)
_Regardez tous ces composants_

Tout d'abord, nous commencerons avec le [TextureView](https://developer.android.com/reference/android/view/TextureView).

### Composant TextureView de Camera2

Un TextureView est un composant d'interface utilisateur que vous utilisez pour afficher un flux de contenu (pensez à une vidéo). Nous devons utiliser un TextureView pour afficher le flux de la caméra, qu'il s'agisse d'un aperçu ou avant de prendre la photo/la vidéo. 

Deux propriétés importantes à utiliser concernant le TextureView sont :

* Le champ SurfaceTexture
* L'interface SurfaceTextureListener

Le premier est l'endroit où le contenu sera affiché, et le second a quatre rappels :

1. [onSurfaceTextureAvailable](https://developer.android.com/reference/android/view/TextureView.SurfaceTextureListener#onSurfaceTextureAvailable%28android.graphics.SurfaceTexture,%20int,%20int%29)
2. [onSurfaceTextureSizeChanged](https://developer.android.com/reference/android/view/TextureView.SurfaceTextureListener#onSurfaceTextureSizeChanged%28android.graphics.SurfaceTexture,%20int,%20int%29)
3. [onSurfaceTextureUpdated](https://developer.android.com/reference/android/view/TextureView.SurfaceTextureListener#onSurfaceTextureUpdated%28android.graphics.SurfaceTexture%29)
4. [onSurfaceTextureDestroyed](https://developer.android.com/reference/android/view/TextureView.SurfaceTextureListener#onSurfaceTextureDestroyed%28android.graphics.SurfaceTexture%29)

```kotlin
private val surfaceTextureListener = object : TextureView.SurfaceTextureListener {
        override fun onSurfaceTextureAvailable(texture: SurfaceTexture, width: Int, height: Int) {

        }
        override fun onSurfaceTextureSizeChanged(texture: SurfaceTexture, width: Int, height: Int) {
        
        }
        
        override fun onSurfaceTextureDestroyed(texture: SurfaceTexture) {
           
        }
        override fun onSurfaceTextureUpdated(texture: SurfaceTexture) {
          
        }
}
```

Le premier rappel est crucial lors de l'utilisation de la caméra. Cela est dû au fait que nous voulons être informés lorsque la SurfaceTexture est disponible afin que nous puissions commencer à afficher le flux dessus. 

Soyez conscient que ce n'est que lorsque le TextureView est attaché à une fenêtre qu'il devient disponible.

L'interaction avec la caméra a changé depuis l'API précédente. Maintenant, nous avons le [CameraManager](https://developer.android.com/reference/android/hardware/camera2/CameraManager). Il s'agit d'un service système qui nous permet d'interagir avec les objets [CameraDevice](https://developer.android.com/reference/android/hardware/camera2/CameraDevice). 

Les méthodes auxquelles vous devez prêter une attention particulière sont :

* [openCamera](https://developer.android.com/reference/android/hardware/camera2/CameraManager#openCamera%28java.lang.String,%20android.hardware.camera2.CameraDevice.StateCallback,%20android.os.Handler%29)
* [getCameraCharacteristics](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics%28java.lang.String%29)
* [getCameraIdList](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraIdList%28%29)

Après avoir su que le TextureView est disponible et prêt, nous devons appeler openCamera pour ouvrir une connexion à la caméra. Cette méthode prend trois arguments :

1. CameraId - String
2. CameraDevice.StateCallback
3. Un Handler

L'argument CameraId indique à quelle caméra nous voulons nous connecter. Sur votre téléphone, il y a principalement deux caméras, l'avant et l'arrière. Chacune a son propre identifiant unique. Habituellement, il s'agit soit d'un zéro, soit d'un un. 

Comment obtenons-nous l'identifiant de la caméra ? Nous utilisons la méthode getCamerasIdList du CameraManager. Elle retournera un tableau de type chaîne de tous les identifiants de caméra identifiés à partir de l'appareil.

```kotlin
val cameraManager: CameraManager = getSystemService(Context.CAMERA_SERVICE) as CameraManager
val cameraIds: Array<String> = cameraManager.cameraIdList
var cameraId: String = ""
for (id in cameraIds) {
    val cameraCharacteristics = cameraManager.getCameraCharacteristics(id)
    //Si nous voulons choisir la caméra avant au lieu de la caméra arrière
    if (cameraCharacteristics.get(CameraCharacteristics.LENS_FACING) == CameraCharacteristics.LENS_FACING_FRONT) 
      continue
    }
    
    val previewSize = cameraCharacteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!.getOutputSizes(ImageFormat.JPEG).maxByOrNull { it.height * it.width }!!
    val imageReader = ImageReader.newInstance(previewSize.width, previewSize.height, ImageFormat.JPEG, 1)
    imageReader.setOnImageAvailableListener(onImageAvailableListener, backgroundHandler)
    cameraId = id
}
```

Les arguments suivants sont des rappels à l'état de la caméra après avoir essayé de l'ouvrir. Si vous y réfléchissez, il ne peut y avoir que plusieurs résultats pour cette action :

* La caméra parvient à s'ouvrir avec succès
* La caméra se déconnecte
* Une erreur se produit

Et c'est ce que vous trouverez à l'intérieur du CameraDevice.StateCallback :

```kotlin
 private val cameraStateCallback = object : CameraDevice.StateCallback() {
        override fun onOpened(camera: CameraDevice) {
           
        }

        override fun onDisconnected(cameraDevice: CameraDevice) {
           
        }

        override fun onError(cameraDevice: CameraDevice, error: Int) {
            val errorMsg = when(error) {
                ERROR_CAMERA_DEVICE -> "Fatal (device)"
                ERROR_CAMERA_DISABLED -> "Device policy"
                ERROR_CAMERA_IN_USE -> "Camera in use"
                ERROR_CAMERA_SERVICE -> "Fatal (service)"
                ERROR_MAX_CAMERAS_IN_USE -> "Maximum cameras in use"
                else -> "Unknown"
            }
            Log.e(TAG, "Error when trying to connect camera $errorMsg")
        }
    }
```

Le troisième argument traite de l'endroit où ce travail se fera. Puisque nous ne voulons pas occuper le thread principal, il est préférable de faire ce travail en arrière-plan. 

C'est pourquoi nous devons lui passer un Handler. Il serait judicieux d'avoir cette instance de handler instanciée avec un thread de notre choix afin que nous puissions déléguer le travail à celui-ci.

```kotlin
private lateinit var backgroundHandlerThread: HandlerThread
private lateinit var backgroundHandler: Handler

 private fun startBackgroundThread() {
    backgroundHandlerThread = HandlerThread("CameraVideoThread")
    backgroundHandlerThread.start()
    backgroundHandler = Handler(
        backgroundHandlerThread.looper)
}

private fun stopBackgroundThread() {
    backgroundHandlerThread.quitSafely()
    backgroundHandlerThread.join()
}
```

Avec tout ce que nous avons fait, nous pouvons maintenant appeler openCamera :

```kotlin
cameraManager.openCamera(cameraId, cameraStateCallback,backgroundHandler)
```

Ensuite, dans le rappel **onOpened**, nous pouvons commencer à traiter la logique sur la manière de présenter le flux de la caméra à l'utilisateur via le TextureView.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/0_hW39WzgV8lm87Ql0.jpg)
_Photo par [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Markus Spiske</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

### Comment afficher un aperçu du flux

Nous avons notre caméra (cameraDevice) et notre TextureView pour afficher le flux. Mais nous devons les connecter l'un à l'autre afin de pouvoir afficher un aperçu du flux. 

Pour ce faire, nous utiliserons la propriété SurfaceTexture de TextureView et nous construirons une CaptureRequest.

```kotlin
val surfaceTexture : SurfaceTexture? = textureView.surfaceTexture // 1

val cameraCharacteristics = cameraManager.getCameraCharacteristics(cameraId) //2
val previewSize = cameraCharacteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!
  .getOutputSizes(ImageFormat.JPEG).maxByOrNull { it.height * it.width }!!

surfaceTexture?.setDefaultBufferSize(previewSize.width, previewSize.height) //3

val previewSurface: Surface = Surface(surfaceTexture)

captureRequestBuilder = cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW) //4
captureRequestBuilder.addTarget(previewSurface) //5

cameraDevice.createCaptureSession(listOf(previewSurface, imageReader.surface), captureStateCallback, null) //6
```

Dans le code ci-dessus, nous obtenons d'abord la surfaceTexture de notre TextureView. Ensuite, nous utilisons l'objet cameraCharacteristics pour obtenir la liste de toutes les tailles de sortie. Pour obtenir la taille souhaitée, nous la définissons pour la surfaceTexture.

Ensuite, nous créons une captureRequest où nous passons **TEMPLATE_PREVIEW**. Nous ajoutons notre surface d'entrée à la captureRequest.

Enfin, nous démarrons une captureSession avec nos surfaces d'entrée et de sortie, captureStateCallback, et nous passons null pour le handler.

Alors, qu'est-ce que ce captureStateCallback ? Si vous vous souvenez du diagramme du début de cet article, il fait partie de la CameraCaptureSession que nous démarrons. Cet objet suit la progression de la captureRequest avec les rappels suivants :

* onConfigured
* onConfigureFailed

```kotlin
private val captureStateCallback = object : CameraCaptureSession.StateCallback() {
        override fun onConfigureFailed(session: CameraCaptureSession) {
            
        }
        override fun onConfigured(session: CameraCaptureSession) {
         
        }
}
```

Lorsque la **cameraCaptureSession** est configurée avec succès, nous définissons une demande répétée pour la session afin de nous permettre d'afficher l'aperçu en continu. 

Pour ce faire, nous utilisons l'objet session que nous obtenons dans le rappel :

```kotlin
 session.setRepeatingRequest(captureRequestBuilder.build(), null, backgroundHandler)
```

Vous reconnaîtrez notre objet captureRequestBuilder que nous avons créé précédemment comme premier argument de cette méthode. Nous appliquons la méthode build afin que le paramètre final passé soit un CaptureRequest. 

Le deuxième argument est un écouteur CameraCaptureSession.captureCallback, mais comme nous ne voulons rien faire avec les images capturées (puisqu'il s'agit d'un aperçu), nous passons null. 

Le troisième argument est un handler, et ici nous utilisons notre propre backgroundHandler. C'est aussi pourquoi nous avons passé null dans la section précédente, puisque la demande répétée s'exécutera sur le thread d'arrière-plan.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/dicky-jiang-ovUgpiDrbrc-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@dicky_juwono?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Dicky Jiang</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

## Comment prendre une photo

Avoir un aperçu en direct de la caméra est génial, mais la plupart des utilisateurs voudront probablement faire quelque chose avec. Une partie de la logique que nous allons écrire pour prendre une photo sera similaire à ce que nous avons fait dans la section précédente.

1. Nous allons créer une captureRequest
2. Nous allons utiliser un ImageReader et son écouteur pour récupérer la photo prise
3. En utilisant notre cameraCaptureSession, nous allons invoquer la méthode capture

```kotlin
val orientations : SparseIntArray = SparseIntArray(4).apply {
    append(Surface.ROTATION_0, 0)
    append(Surface.ROTATION_90, 90)
    append(Surface.ROTATION_180, 180)
    append(Surface.ROTATION_270, 270)
}

val captureRequestBuilder = cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_STILL_CAPTURE)
captureRequestBuilder.addTarget(imageReader.surface)

val rotation = windowManager.defaultDisplay.rotation
captureRequestBuilder.set(CaptureRequest.JPEG_ORIENTATION, orientations.get(rotation))
cameraCaptureSession.capture(captureRequestBuilder.build(), captureCallback, null)
```

Mais qu'est-ce que ce [ImageReader](https://developer.android.com/reference/android/media/ImageReader) ? Eh bien, un ImageReader fournit un accès aux données d'image qui sont rendues sur une surface. Dans notre cas, il s'agit de la surface du TextureView. 

Si vous regardez l'extrait de code de la section précédente, vous remarquerez que nous avons déjà défini un ImageReader là.

```kotlin
val cameraManager: CameraManager = getSystemService(Context.CAMERA_SERVICE) as CameraManager
val cameraIds: Array<String> = cameraManager.cameraIdList
var cameraId: String = ""
for (id in cameraIds) {
    val cameraCharacteristics = cameraManager.getCameraCharacteristics(id)
    //Si nous voulons choisir la caméra arrière au lieu de la caméra avant
    if (cameraCharacteristics.get(CameraCharacteristics.LENS_FACING) == CameraCharacteristics.LENS_FACING_FRONT) 
      continue
    }
    
    val previewSize = cameraCharacteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!.getOutputSizes(ImageFormat.JPEG).maxByOrNull { it.height * it.width }!!
    val imageReader = ImageReader.newInstance(previewSize.width, previewSize.height, ImageFormat.JPEG, 1)
    imageReader.setOnImageAvailableListener(onImageAvailableListener, backgroundHandler)
    cameraId = id
}
```

Comme vous pouvez le voir ci-dessus, nous instancions un ImageReader en passant une largeur et une hauteur, le format d'image que nous aimerions pour notre image et le nombre d'images qu'il peut capturer.

Une propriété que la classe ImageReader possède est un écouteur appelé onImageAvailableListener. Cet écouteur sera déclenché une fois qu'une photo est prise (puisque nous avons passé sa surface comme source de sortie pour notre demande de capture).

```kotlin
val onImageAvailableListener = object: ImageReader.OnImageAvailableListener{
        override fun onImageAvailable(reader: ImageReader) {
            val image: Image = reader.acquireLatestImage()
        }
    }
```

⚠️ **Assurez-vous de fermer l'image après l'avoir traitée, sinon vous ne pourrez pas prendre une autre photo.**

![Image](https://www.freecodecamp.org/news/content/images/2021/07/jakob-owens-CiUR8zISX60-unsplash.jpg)
_Photo par [Unsplash](https://unsplash.com/@jakobowens1?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Jakob Owens</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

## Comment enregistrer une vidéo

Pour enregistrer une vidéo, nous devons interagir avec un nouvel objet appelé [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder). L'objet media recorder est responsable de l'enregistrement audio et vidéo et nous allons l'utiliser pour faire exactement cela.

Avant de faire quoi que ce soit, nous devons configurer le media recorder. Il y a diverses configurations à gérer et **elles doivent être dans le bon ordre, sinon des exceptions seront levées**. 

Ci-dessous un exemple d'une sélection de configurations qui nous permettront de capturer une vidéo (sans audio).

```kotlin
fun setupMediaRecorder(width: Int, height: Int) {
  val mediaRecorder: MediaRecorder = MediaRecorder()
  mediaRecorder.setVideoSource(MediaRecorder.VideoSource.SURFACE)
  mediaRecorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
  mediaRecorder.setVideoEncoder(MediaRecorder.VideoEncoder.H264)
  mediaRecorder.setVideoSize(videoSize.width, videoSize.height)
  mediaRecorder.setVideoFrameRate(30)
  mediaRecorder.setOutputFile(PATH_TO_FILE)
  mediaRecorder.setVideoEncodingBitRate(10_000_000)
  mediaRecorder.prepare()
}
```

Faites attention à la méthode **setOutputFile** car elle attend un chemin vers le fichier qui stockera notre vidéo. À la fin de la définition de toutes ces configurations, nous devons appeler prepare.

Notez que le mediaRecorder a également une méthode start et nous devons appeler prepare avant de l'appeler.

Après avoir configuré notre mediaRecoder, nous devons créer une demande de capture et une session de capture.

```kotlin
fun startRecording() {
        val surfaceTexture : SurfaceTexture? = textureView.surfaceTexture
        surfaceTexture?.setDefaultBufferSize(previewSize.width, previewSize.height)
        val previewSurface: Surface = Surface(surfaceTexture)
        val recordingSurface = mediaRecorder.surface
        captureRequestBuilder = cameraDevice.createCaptureRequest(CameraDevice.TEMPLATE_RECORD)
        captureRequestBuilder.addTarget(previewSurface)
        captureRequestBuilder.addTarget(recordingSurface)

        cameraDevice.createCaptureSession(listOf(previewSurface, recordingSurface), captureStateVideoCallback, backgroundHandler)
    }
```

De manière similaire à la configuration de l'aperçu ou à la prise d'une photographie, nous devons définir nos surfaces d'entrée et de sortie. 

Ici, nous créons un objet Surface à partir de la surfaceTexture du TextureView et nous prenons également la surface du media recorder. Nous passons la valeur **TEMPLATE_RECORD** lors de la création d'une demande de capture. 

Notre captureStateVideoCallback est du même type que celui que nous avons utilisé pour la photo fixe, mais à l'intérieur du rappel onConfigured, nous appelons la méthode start du media recorder.

```kotlin
val captureStateVideoCallback = object : CameraCaptureSession.StateCallback() {
      override fun onConfigureFailed(session: CameraCaptureSession) {
         
      }
      
      override fun onConfigured(session: CameraCaptureSession) {
          session.setRepeatingRequest(captureRequestBuilder.build(), null, backgroundHandler)
          mediaRecorder.start()
      }
  }
```

Maintenant, nous enregistrons une vidéo, mais comment arrêter l'enregistrement ? Pour cela, nous utiliserons les méthodes stop et reset sur l'objet mediaRecorder :

```kotlin
mediaRecorder.stop()
mediaRecorder.reset()
```

## Conclusion

C'était beaucoup à assimiler. Donc si vous êtes arrivé jusqu'ici, félicitations ! Il n'y a pas moyen de contourner cela – seulement en mettant les mains dans le cambouis avec le code que vous commencerez à comprendre comment tout se connecte ensemble. 

Vous êtes plus que encouragé à regarder tout le code présenté dans cet article ci-dessous :

%[https://github.com/TomerPacific/MediumArticles/tree/master/Camrea2API]

Gardez à l'esprit que ce n'est que la partie émergée de l'iceberg en ce qui concerne l'API Camera2. Il y a beaucoup d'autres choses que vous pouvez faire, comme capturer une vidéo au ralenti, basculer entre les caméras avant et arrière, contrôler la mise au point, et bien plus encore.