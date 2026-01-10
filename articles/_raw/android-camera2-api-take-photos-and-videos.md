---
title: Android Camera2 – How to Use the Camera2 API to Take Photos and Videos
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
seo_title: null
seo_desc: "We all use the camera on our phones and we use it a l-o-t. There are even\
  \ some applications that have integrated the camera as a feature. \nOn one end,\
  \ there is a standard way of interacting with the camera. On the other, there is\
  \ a way to customize y..."
---

We all use the camera on our phones and we use it a l-o-t. There are even some applications that have integrated the camera as a feature. 

On one end, there is a standard way of interacting with the camera. On the other, there is a way to customize your interaction with the camera. This distinction is an important one to make. And that’s where Camera2 comes in.

## What is Camera2?

While it has been available since API level 21, the Camera2 API has got to be one of the more complex pieces of architecture developers have to deal with. 

This API and its predecessor were put in place so developers could harness the power of interacting with the camera inside of their applications. 

Similar to how there is a way to interact with the microphone or the volume of the device, the Camera2 API gives you the tools to interact with the device's camera. 

In general, if you want to user the Camera2 API, it would probably be for more than just taking a picture or recording a video. This is because the API lets you have in depth control of the camera by exposing various classes that will need to be configured per specific device.

Even if you've dealt with the camera previously, it is such a drastic change from the former camera API, that you might as well forget all that you know. 

There are a ton of resources out there that try to showcase how to use this API directly, but some of them may be outdated and some don’t present the whole picture. 

So, instead of trying to fill in the missing pieces by yourself, this article will (hopefully) be your one stop shop for interacting with the Camera2 API.

## Camera2 Use Cases

Before we dive into anything, it is important to understand that if you only want to use the camera to take a picture or to record a video, you do not need to bother yourself with the Camera2 API. 

The primary reason to use the Camera2 API is if your application requires some custom interaction with the camera or its functionality. 

If you are interested in doing the former instead of the latter, I'll suggest that you visit the following documentation from Google:

1. [Take Photos](https://developer.android.com/training/camera/photobasics)
2. [Capture Video](https://developer.android.com/training/camera/videobasics)

There you will find all the necessary steps you need to take to capture great photos and videos with your camera. But in this article, the main focus will be on how to use Camera2.

Now, there are some things we need to add to our manifest file:

Camera permissions:

```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Camera feature:

```xml
<uses-feature android:name="android.hardware.camera" />
```

You will have to deal with checking if the camera permission has been granted or not, but since this topic has been covered widely, we won’t be dealing with that in this article.

## How to Set up the Camera2 API Components 

The Camera2 API introduces several new interfaces and classes. Let’s break down each of them so we can better understand how to use them.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/1_nPqyLhTqxaqRytV8lV41VA.png)
_Look at all those components_

First off, we’ll start with the [TextureView](https://developer.android.com/reference/android/view/TextureView).

### Camera2 TextureView Component

A TextureView is a UI component that you use to display a content stream (think video). We need to use a TextureView to display the feed from the camera, whether it's a preview or before taking the picture/video. 

Two properties that are important to use regarding the TextureView are:

* The SurfaceTexture field
* The SurfaceTextureListener interface

The first is where the content will get displayed, and the second has four callbacks:

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

The first callback is crucial when using the camera. This is because we want to be notified when the SurfaceTexture is available so we can start displaying the feed on it. 

Be aware that only once the TextureView is attached to a window does it become available.

Interacting with the camera has changed since the previous API. Now, we have the [CameraManager](https://developer.android.com/reference/android/hardware/camera2/CameraManager). This is a system service that allows us to interact with [CameraDevice](https://developer.android.com/reference/android/hardware/camera2/CameraDevice) objects. 

The methods you want to pay close attention to are:

* [openCamera](https://developer.android.com/reference/android/hardware/camera2/CameraManager#openCamera%28java.lang.String,%20android.hardware.camera2.CameraDevice.StateCallback,%20android.os.Handler%29)
* [getCameraCharacteristics](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics%28java.lang.String%29)
* [getCameraIdList](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraIdList%28%29)

After we know that the TextureView is available and ready, we need to call openCamera to open a connection to the camera. This method takes in three arguments:

1. CameraId - String
2. CameraDevice.StateCallback
3. A Handler

The CameraId argument signifies which camera we want to connect to. On your phone, there are mainly two cameras, the front and the back. Each has its own unique id. Usually, it is either a zero or a one. 

How do we get the camera id? We use the CameraManager’s getCamerasIdList method. It will return an array of string type of all the camera ids identified from the device.

```kotlin
val cameraManager: CameraManager = getSystemService(Context.CAMERA_SERVICE) as CameraManager
val cameraIds: Array<String> = cameraManager.cameraIdList
var cameraId: String = ""
for (id in cameraIds) {
    val cameraCharacteristics = cameraManager.getCameraCharacteristics(id)
    //If we want to choose the rear facing camera instead of the front facing one
    if (cameraCharacteristics.get(CameraCharacteristics.LENS_FACING) == CameraCharacteristics.LENS_FACING_FRONT) 
      continue
    }
    
    val previewSize = cameraCharacteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!.getOutputSizes(ImageFormat.JPEG).maxByOrNull { it.height * it.width }!!
    val imageReader = ImageReader.newInstance(previewSize.width, previewSize.height, ImageFormat.JPEG, 1)
    imageReader.setOnImageAvailableListener(onImageAvailableListener, backgroundHandler)
    cameraId = id
}
```

The next arguments are callbacks to the camera state after we try to open it. If you think about it, there can only be several outcomes for this action:

* The camera manages to open successfully
* The camera disconnects
* Some error occurs

And that’s what you will find inside the CameraDevice.StateCallback:

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

The third argument deals with where this work will happen. Since we don’t want to occupy the main thread, it is better to do this work in the background. 

That’s why we need to pass a Handler to it. It would be wise to have this handler instance instantiated with a thread of our choosing so we can delegate work to it.

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

With everything that we have done, we can now call openCamera:

```kotlin
cameraManager.openCamera(cameraId, cameraStateCallback,backgroundHandler)
```

Then in the **onOpened** callback, we can start to deal with the logic on how to present the camera feed to the user via the TextureView.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/0_hW39WzgV8lm87Ql0.jpg)
_Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Markus Spiske</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

### How to Show a Preview of the Feed 

We've got our camera (cameraDevice) and our TextureView to show the feed. But we need to connect them to each other so we can show a preview of the feed. 

To do that, we will be using the SurfaceTexture property of TextureView and we will be building a CaptureRequest.

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

In the code above, first we get the surfaceTexture from our TextureView. Then we use the cameraCharacteristics object to get the list of all output sizes. To get the desired size, we set it for the surfaceTexture.

Next, we create a captureRequest where we pass in **TEMPLATE_PREVIEW**. We add our input surface to the captureRequest.

Finally, we start a captureSession with our input and output surfaces, captureStateCallback, and pass in null for the handler

So what is this captureStateCallback? If you remember the diagram from the beginning of this article, it is part of the CameraCaptureSession which we are starting. This object tracks the progress of the captureRequest with the following callbacks:

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

When the **cameraCaptureSession** is configured successfully, we set a repeating request for the session to allow us to show the preview continuously. 

To do that, we use the session object we get in the callback:

```kotlin
 session.setRepeatingRequest(captureRequestBuilder.build(), null, backgroundHandler)
```

You will recognize our captureRequestBuilder object that we created earlier as the first argument for this method. We enact the build method so the final parameter passed in is a CaptureRequest. 

The second argument is a CameraCaptureSession.captureCallback listener, but since we don’t want to do anything with the captured images (since this is a preview), we pass in null. 

The third argument is a handler, and here we use our own backgroundHandler. This is also why we passed in null in the previous section, since the repeating request will run on the background thread.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/dicky-jiang-ovUgpiDrbrc-unsplash.jpg)
_Photo by [Unsplash](https://unsplash.com/@dicky_juwono?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Dicky Jiang</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

## How to Take a Picture

Having a live preview of the camera is awesome, but most users will probably want to do something with it. Some of the logic that we will write to take a picture will be similar to what we did in the previous section.

1. We will create a captureRequest
2. We will use an ImageReader and its listener to gather the photo taken
3. Using our cameraCaptureSession, we will invoke the capture method

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

But what is this [ImageReader](https://developer.android.com/reference/android/media/ImageReader)? Well, an ImageReader provides access to image data that is rendered onto a surface. In our case, it is the surface of the TextureView. 

If you look at the code snippet from the previous section, you will notice we have already defined an ImageReader there.

```kotlin
val cameraManager: CameraManager = getSystemService(Context.CAMERA_SERVICE) as CameraManager
val cameraIds: Array<String> = cameraManager.cameraIdList
var cameraId: String = ""
for (id in cameraIds) {
    val cameraCharacteristics = cameraManager.getCameraCharacteristics(id)
    //If we want to choose the rear facing camera instead of the front facing one
    if (cameraCharacteristics.get(CameraCharacteristics.LENS_FACING) == CameraCharacteristics.LENS_FACING_FRONT) 
      continue
    }
    
    val previewSize = cameraCharacteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP)!!.getOutputSizes(ImageFormat.JPEG).maxByOrNull { it.height * it.width }!!
    val imageReader = ImageReader.newInstance(previewSize.width, previewSize.height, ImageFormat.JPEG, 1)
    imageReader.setOnImageAvailableListener(onImageAvailableListener, backgroundHandler)
    cameraId = id
}
```

As you can see above, we instantiate an ImageReader by passing in a width and height, the image format we would like our image to be in and the number of images that it can capture.

A property the ImageReader class has is a listener called onImageAvailableListener. This listener will get triggered once a photo is taken (since we passed in its surface as the output source for our capture request).

```kotlin
val onImageAvailableListener = object: ImageReader.OnImageAvailableListener{
        override fun onImageAvailable(reader: ImageReader) {
            val image: Image = reader.acquireLatestImage()
        }
    }
```

⚠️ **Make sure to close the image after processing it or else you will not be able to take another photo.**

![Image](https://www.freecodecamp.org/news/content/images/2021/07/jakob-owens-CiUR8zISX60-unsplash.jpg)
_Photo by [Unsplash](https://unsplash.com/@jakobowens1?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener">Jakob Owens</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener)_

## How to Record a Video

To record a video, we need to interact with a new object called [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder). The media recorder object is in charge of recording audio and video and we will be using it do just that.

Before we do anything, we need to setup the media recorder. There are various configurations to deal with and **they must be in the correct order or else exceptions will be thrown**. 

Below is an example of a selection of configurations that will allow us to capture video (without audio).

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

Pay attention to the **setOutputFile** method as it expects a path to the file which will store our video. At the end of setting all these configurations we need to call prepare.

Note that the mediaRecorder also has a start method and we must call prepare before calling it.

After setting up our mediaRecoder, we need to create a capture request and a capture session.

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

Similar to setting up the preview or taking a photograph, we have to define our input and output surfaces. 

Here we are creating a Surface object from the surfaceTexture of the TextureView and also taking the surface from the media recorder. We are passing in the **TEMPLATE_RECORD** value when creating a capture request. 

Our captureStateVideoCallback is of the same type we used for the still photo, but inside the onConfigured callback we call media recorder’s start method.

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

Now we are recording a video, but how do we stop recording? For that, we will be using the stop and reset methods on the mediaRecorder object:

```kotlin
mediaRecorder.stop()
mediaRecorder.reset()
```

## Conclusion

That was a lot to process. So if you made it here, congratulations! There is no way around it – only by getting your hands dirty with the code will you start to understand how everything connects together. 

You are more than encouraged to look at all the code featured in this article below :

%[https://github.com/TomerPacific/MediumArticles/tree/master/Camrea2API]

Bear in mind that this is just the tip of the iceberg when it comes to the Camera2 API. There are a lot of other things you can do, like capturing a slow motion video, switching between the front and back cameras, controlling the focus, and much more.

