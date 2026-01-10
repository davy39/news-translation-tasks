---
title: How to get started with augmented reality in Swift, the easy way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T22:09:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-ar-in-swift-the-easy-way-7399fe1c82f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gf3uExB7i8IDfN-s3_tcLw.png
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ranadhir Dey

  If you look around, this is the golden era of technology. Every keynote adds something
  new to the existing stack of technologies. It’s exciting to see how these emerging
  technologies have enhanced the boundaries of our imagination. As...'
---

By Ranadhir Dey

If you look around, this is the golden era of technology. Every keynote adds something new to the existing stack of technologies. It’s exciting to see how these emerging technologies have enhanced the boundaries of our imagination. As a developer, we must be proud that we are the firsthand users of these technologies.

But every new technology comes with quite a steep learning curve. You just can’t watch a keynote or a video on Youtube and start developing an app. But the good news is that, with AR in Swift, it’s remarkably easy to work with basic AR apps. Apple has done most of the heavy lifting for you. Follow along and you’ll see how easy it can be.

### **Let’s dig in…**

In this tutorial, we will learn the necessary tools and techniques of AR in Swift that will allow us to create an app that decorates your floor with some cool floor tiles and wooden textures. The finished app will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/vO7XUgbwu9-jNCpzzBts8M-Q4ObnFsVmSCBB)

Let’s start by creating a **single view** application in Xcode and name it Home Decor.

![Image](https://cdn-media-1.freecodecamp.org/images/vcKpo7OKMJJrjoVC4NUEaj3CK0ZTDVn1B9kc)

### **Adding camera permissions**

Now the very first thing we will do is to navigate to the info.plist file and enable camera usage. Camera capability is the first thing you need for an AR app. Find the Camera Usage Description key, like the below image, and give it a suitable message. This message will show up in the very first launch of the app while asking for the camera permissions from the user.

![Image](https://cdn-media-1.freecodecamp.org/images/nXNhGVVjq4c-CAFVSXuDotT1p4OI44-GWugJ)

### **Adding ARKit Capabilities to the app**

Go to Main.storyboard. Drag and drop an ARKit SceneKit View on the ViewController and pin the ARSCNView to the edges of the ViewController.

![Image](https://cdn-media-1.freecodecamp.org/images/mw2nLyGFYWFvXMOtDFrZqCHentFfkfQu2LFu)

Create a IBOutlet to the ViewController class, and name it sceneView. As soon as you do that, an error stating **undeclared ARSCNView**_,_ will popup, as our view controller doesn’t recognise anything of type ARSCNView. To resolve this, and to use other ARKit features, we need to import ARKit into the view controller.

![Image](https://cdn-media-1.freecodecamp.org/images/vqFrntUcNDJ0ySI-E9hIWjLttHQ3bv24PPRU)

Now move from storyboard to the view controller.swift file. Declare a property of type ARWorldTrackingConfiguration before the viewDidLoad() method and name it config. And our view controller will look like this (I’ve removed the didReceiveMemoryWarning method):

```
import UIKitimport ARKit
```

```
class ViewController: UIViewController {
```

```
@IBOutlet weak var sceneView: ARSCNView!let config = ARWorldTrackingConfiguration()
```

```
override func viewDidLoad() {super.viewDidLoad()}
```

### **Allow debugging**

This config variable will determine the configurations of the scene session. We will see it’s usage later in the section. Now, in the viewDidLoad method after super.viewDidLoad(), add the following:

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

Here we are enabling debug options for our sceneView, which is nothing but the camera view with the capabilities of AR framework. ARSCNDebugOptions.showWorldOrigin will display world origin on the screen. This will help us find the reference point of all other positions. ARSCNDebugOptions.showFeaturePoints will display all the points on the screen which the AR camera has recognised in the surroundings.

Now to start the AR session, we need to run a session in our sceneView with the configurations mentioned in the config variable. Just below sceneView.debugOptions line, write:

```
sceneView.session.run(config)
```

Now run the app on your device (not on a simulator, as it doesn’t have the camera). The alert asking for camera permissiosn with the message you wrote will show up, and you need allow it. Wait for a bit while it loads the world origin.

![Image](https://cdn-media-1.freecodecamp.org/images/nfQfMj9tFFxVpQ02jfMQpFttyDtiWLo-HAJV)

If you are here, you have already have an AR app running. Congratulations!

### **How AR Axes work**

The red bar or X axis is used to position objects left or right of the world origin. The green bar or Y axis is used to position objects to the top or bottom of the world origin. And the blue bar or Z axis is used to determine how close or far an object will be placed from the world origin.

A positive value of X will position an object to the right of the world origin, and negative will place it on the left. Positive for Y will place it on top and negative will place it on the bottom of the world origin. Positive for Z will place it nearer, and negative will place it farther from the world origin.

### **Adding a virtual object**

Let’s add some virtual objects to the scene. 3D capsule would be a good choice. Declare a capsuleNode of type [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode?changes=_8) and give it a geometry of [capsule](https://developer.apple.com/documentation/scenekit/scncapsule?changes=_5). Give it a height of 0.1 meter, and radius of 0.03 meters.

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1
```

Now position it 0.1 meter left of the world origin, 0.1 meter above the world origin, and 0.1 meter away from the world origin:

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

Now, add the node to scene:

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

The sceneView contains a scene which is responsible for holding all the 3D objects in SCNNode format that will form the 3D scene. We are adding the capsule to the root node of the scene. Root node’s position is exactly aligned to the position of the world origin. That means its position is (0,0,0).

Currently, our viewDidLoad method looks like this:

```
override func viewDidLoad() {
```

```
super.viewDidLoad()
```

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

```
sceneView.session.run(config)
```

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1))
```

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

```
}
```

Now run the app.

![Image](https://cdn-media-1.freecodecamp.org/images/oWdSpOkroOQI7EuYJZ8-HAix6Xdg2tim75NN)

Cool! We have just positioned a virtual object in the real world. You can play with different positions and different [geometries](https://developer.apple.com/documentation/scenekit/scngeometry) to explore more. Now let’s rotate the capsule 90 degree around the Z axis so that it lies flat on the X axis and changes its colour to blue.

### **Euler Angles**

Euler Angles are responsible for a SCNNode’s display angle. We will see how to use it to rotate the capsule.

Every SCNGeometry can have materials added to it, which defines the appearance of the geometry. Materials have a diffuse property which, when set, spreads its content all over the geometry.

In viewDidLoad, add the below lines after you set the position of the capsule.

```
capsuleNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue //1capsuleNode.eulerAngles = SCNVector3(0,0,Double.pi/2)//2
```

Here, in the first line, we are setting the blue colour to the very first material of the node which will spread across the capsule and will make it look blue. In line 2, we are setting the Z Euler angle to 90 degree radians. Finally, our view loads and looks like this:

```
override func viewDidLoad() {
```

```
super.viewDidLoad()
```

```
sceneView.debugOptions = [ARSCNDebugOptions.showFeaturePoints, ARSCNDebugOptions.showWorldOrigin]
```

```
sceneView.session.run(config)
```

```
let capsuleNode = SCNNode(geometry: SCNCapsule(capRadius: 0.03, height: 0.1))
```

```
capsuleNode.position = SCNVector3(0.1, 0.1, -0.1)
```

```
capsuleNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue //1
```

```
capsuleNode.eulerAngles = SCNVector3(0,0,Double.pi/2)//2
```

```
sceneView.scene.rootNode.addChildNode(capsuleNode)
```

```
}
```

Now run the app.

![Image](https://cdn-media-1.freecodecamp.org/images/KRIWB1PKTsTUtgcALCZrbEIKFxyFAsOOJr3M)

Great! A blue coloured sleeping capsule on the wall! You can even add textures as diffuse contents to make an object look more realistic. We will use that in the next section when we place the tiles’ textures on the floor.

Now that we have successfully placed virtual objects on the real world, it’s time to decorate our real floor with virtual floor-tiles. To achieve the floor effect, we will use a [SCNPlane](https://developer.apple.com/documentation/scenekit/scnplane) geometry. SCNPlane doesn’t have any depth like other 3D geometries, which makes it a perfect fit for our app.

### **ARSCENEView Delegates**

Before starting the floor detection, we will explore some delegate methods of our sceneView to understand what capabilities we are equipped with to interact with an ongoing AR session.

```
func renderer(SCNSceneRenderer, didAdd: SCNNode, for: ARAnchor)
```

Whenever we move or tilt our device with an AR session on in it, the ARKit tries to find different ARAnchors in the surroundings. An [ARAnchor](https://developer.apple.com/documentation/arkit/aranchor) contains information about a real world position and orientation that can be used to place an object.

Once a different anchor is found, a new node gets added to the scene with the same information to accommodate this newly found anchor. This delegate method will inform us about that. We will be using it to find all the positions on the floor to place the tiles.

```
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor)
```

Most of the time, all the nodes that get added from the anchors belong to the same object. Let’s say you are moving around the floor and the device finds a number of anchors at different positions. It tries to add all the nodes for those anchors, as it thinks that all these anchors belong to different objects.

But ARKit eventually recognises that all of them belong to the same floor, so it updates the very first floor node by appending dimensions of other duplicate nodes. This delegate method will inform us about that.

```
func renderer(SCNSceneRenderer, didRemove: SCNNode, for: ARAnchor)
```

After updating the first unique node with dimensions of all other duplicate nodes, ARKit removes all the duplicate nodes and the delegate method notifies us. We will be using all of the above delegate methods in our app (and their purpose will become clearer).

### **Plane detection**

Presently, our scene is trying to gather all anchors that it comes across, as that is the default behaviour. But since a floor is a horizontal surface, we are only interested in anchors that are on horizontal planes. So, go back to our viewDidLoad method and write the below code **before** running the session (that is before sceneView.session.run(config)) line.

```
config.planeDetection = .horizontal
```

In the viewDidLoad method, you can remove everything after sceneView.session.run(config) as that was for placing the capsule on screen and we don’t need that anymore. Since we will be using all the above mentioned delegate methods, we need to make our viewController a delegate of the sceneView. Before the closing brace of viewDidLoad() method, add the below line.

```
sceneView.delegate = self
```

You should get an error now, as our view controller still is not conforming the sceneView delegate. To implement this, let’s create an extension of the view controller at the end of the ViewController.swift file.

```
extension ViewController:ARSCNViewDelegate{}
```

The didAdd SCNNode delegate method will get fired every time a part of the floor is discovered and a new node gets added to the scene based on the anchor. Within this method, we will create a floor node and will add it as a child of the recently added node in the position of the anchor.

[ARArchor](https://developer.apple.com/documentation/arkit/aranchor) can be of four different types to solve four different purposes. Here we are only interested in ARPlaneAnchor which detects the horizontal or vertical planes.

### **Creating AR floor nodes**

Let’s create a function that would receive an ARPlaneAnchor as a parameter, create a floor node at the anchor’s position, and return it.

```
func createFloorNode(anchor:ARPlaneAnchor) ->SCNNode{
```

```
let floorNode = SCNNode(geometry: SCNPlane(width: CGFloat(anchor.extent.x), height: CGFloat(anchor.extent.z))) //1
```

```
floorNode.position=SCNVector3(anchor.center.x,0,anchor.center.z)                                               //2
```

```
floorNode.geometry?.firstMaterial?.diffuse.contents = UIColor.blue                                             //3
```

```
floorNode.geometry?.firstMaterial?.isDoubleSided = true                                                        //4
```

```
floorNode.eulerAngles = SCNVector3(Double.pi/2,0,0)                                                    //5
```

```
return floorNode                                                                                               //6
```

```
}
```

Let’s go through the function line by line and discuss it in more detail. Please follow each line’s description, as it’s the trickiest part.

1. We are creating a node with a geometry of SCNPlane which has the size of the anchor. ARPlaneAnchor’s extent holds the position information. The fact that the extent.z has been used as height and not extent.y, might be a little confusing. If you visualise that a 3D cube is placed on a floor and you want to make it flat along a 2D surface, you would change the y to zero and it would go flat. Now, to get the length of this 2D surface, you would consider the z, wouldn’t you? Our floor is flat, so we need a flat node not a cube.

2. We are setting the position of the node. As we don’t need any elevation, we make y zero.

3. Set the floor colour to blue.

4. The material colour will be displayed only on one side unless we specifically mention it is double-sided.

5. By default, the plane will be placed vertically. To make it horizontal, we need to rotate it by 90 degrees.

### **Implementing the delegate methods**

Now, let’s implement the didAdd SCNNode delegate method.

```
func renderer(_ renderer: SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor) {
```

```
guard let planeAnchor = anchor as? ARPlaneAnchor else {return} //1
```

```
let planeNode = createFloorNode(anchor: planeAnchor) //2
```

```
node.addChildNode(planeNode) //3
```

```
}
```

In line 1, we are checking if the anchor is a ARPlaneAnchor, since we would only deal with this type of anchor.

In line 2, a new node is getting created based on the anchor. In line 3, it’s getting added to the node.

Now in the didUpdate SCNNode delegate, we will delete all our floor nodes. We’ll do this because the dimensions of the current node have been changed and the old floor nodes won’t match. Then we will again add a fresh floor node to this updated node.

```
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {
```

```
guard let planeAnchor = anchor as? ARPlaneAnchor else {return}
```

```
node.enumerateChildNodes { (node, _) in
```

```
node.removeFromParentNode()
```

```
}
```

```
let planeNode = createFloorNode(anchor: planeAnchor)
```

```
node.addChildNode(planeNode)
```

```
}
```

In didRemove SCNNode delegate method, we want to clean out all our junk nodes in a civilized manner.

```
func renderer(_ renderer: SCNSceneRenderer, didRemove node: SCNNode, for anchor: ARAnchor) {
```

```
guard let _ = anchor as? ARPlaneAnchor else {return}
```

```
node.enumerateChildNodes { (node, _) in
```

```
node.removeFromParentNode()
```

```
}
```

```
}
```

Phew! Thats it! Run the app.

![Image](https://cdn-media-1.freecodecamp.org/images/3wVNiLmgzrS3Hjqr7lyE4wQJIssiklvQKZOk)

### **Adding the tile effect**

Wait, what? A blue floor? No, we are not completely done yet. Just a small change and we will have a stunning floor!

To change the blue floor to tiles, we need a texture. Let’s google for a floor tile texture. I searched for “wooden floor texture” and found some beautiful texture images. Save any of them on your Mac and drag it to the Assets.xcassets.

![Image](https://cdn-media-1.freecodecamp.org/images/k9pct70eqbORC5u5WnCgSPOb5cYSmN9hoKmC)

I named it WoodenFloorTile. You can name it whatever you want. Back to the ViewController.swift file again. In the createFloorNode function, instead of setting UIColor.blue as diffuse content, make it an UIImage with the name you have given to the image in the asset folder.

```
floorNode.geometry?.firstMaterial?.diffuse.contents = UIImage(named: "WoodenFloorTile")
```

Now run the app, and wait until the world origin loads. Once the floor is detected, move around to update the node information.

![Image](https://cdn-media-1.freecodecamp.org/images/aO7-9zVFW65MANwJfIgAmwT0OaX6xXIIYEEx)

Wow, You really have a gorgeous floor! You can download multiple textures and place them in a listView. This allows you to change the floor based on selected texture, as it was shown in the first part.

[Download the complete project from GitHub here.](https://github.com/ranadhirdey/Home-Decor)

Now that you have a nice floor, you must be missing some nice furnitures to give your room a great look! We will work on that later on.

