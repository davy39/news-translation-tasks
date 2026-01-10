---
title: 'The Ultimate How-to: Build a Bluetooth Swift App With Hardware in 20 Minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T14:15:00.000Z'
originalURL: https://freecodecamp.org/news/ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/main.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: iOS
  slug: ios
- name: particle
  slug: particle
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: null
seo_desc: 'By Jared Wolff

  In a previous tutorial, you learned how to add Bluetooth to a Particle Xenon application.
  That way you could control the onboard RGB LED from a test app like nRF Connect
  or Light Blue Explorer.

  In this post, we''re going to take it one ...'
---

By Jared Wolff

In a [previous tutorial](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/), you learned how to add Bluetooth to a Particle Xenon application. That way you could control the onboard RGB LED from a test app like nRF Connect or Light Blue Explorer.

In this post, we're going to take it one step further. We're going to develop a Swift app to control a Particle Mesh RGB led. If all goes well, you should have a working app in about 20 minutes!

Let's get started.

### Don't have time right now to read the full article?

[Download the PDF version here.](https://www.jaredwolff.com/files/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/)

## Getting set up

* Install Xcode. [You can download it from the App store here.](https://developer.apple.com/xcode/resources/)
* You'll also need an Apple login. I use my iCloud email. You can create a new account within Xcode if you don't have one yet.
* Install the [RGB example code](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/#final-code) on a Particle Mesh board.

## Create the project

Once everything is installed, let's get to the fun stuff!

Open Xcode and go to **File → New Project.**

![Xcode New Project](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-7ef4de80-050c-4fc3-9cf2-8581e16ffe18.10.57_PM.png)

Select **Single View App.**

![New Project Info](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-ef953954-312b-4320-be30-5da186d0902e.11.14_PM.png)

Then update the **Project Name** to be to your liking. I've also changed my organization identifier to `com.jaredwolff`. Modify it as you see fit!

Select a location to save it.

Next find your **Info.plist.**

![Info.plist in Xcocde](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-27439ca7-68c5-4890-902d-6c2ee7f31829.13.26_PM.png)

Update `info.plist` by adding `Privacy - Bluetooth Peripheral Usage Description`

The description I ended up using was `App uses Bluetooth to connect to the Particle Xenon RGB Example`

This allows you to use Bluetooth in your app if you ever want to release it.

Now, let's get everything minimally functional!

## Minimally functional

![New section image](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Copy_of_Flow-5e62bf38-b399-4bca-9b5b-c63f9716af33.jpg)

Next, we'll get a minimally functional app to connect and do a services discovery. Most of the action will happen in the `ViewController.swift`.

Lets first import `CoreBluetooth`

```swift
    import CoreBluetooth

```

This allows us to control the Bluetooth Low Energy functionality in iOS. Then let's add both the `CBPeripheralDelegate` and `CBCentralManagerDelegate` to the `ViewController` class.

```swift
    class ViewController: UIViewController, CBPeripheralDelegate, CBCentralManagerDelegate {

```

Let's now create local private variables to store the actual central manager and peripheral. We'll set them up further momentarily.

```swift
    // Properties
    private var centralManager: CBCentralManager!
    private var peripheral: CBPeripheral!

```

In your `viewDidLoad` function, let's init the `centralManager`

```swift
    centralManager = CBCentralManager(delegate: self, queue: nil)

```

Setting `delegate: self` is important. Otherwise the central state never changes on startup.

Before we get further, let's create a separate file and call it `ParticlePeripheral.swift`. It can be placed anywhere but I placed it in a separate 'group' called **Models** for later.

Inside we'll create some public variables which contain the UUIDs for our Particle Board. They should look familiar!

```swift
    import UIKit
    import CoreBluetooth

    class ParticlePeripheral: NSObject {

        /// MARK: - Particle LED services and charcteristics Identifiers

        public static let particleLEDServiceUUID     = CBUUID.init(string: "b4250400-fb4b-4746-b2b0-93f0e61122c6")
        public static let redLEDCharacteristicUUID   = CBUUID.init(string: "b4250401-fb4b-4746-b2b0-93f0e61122c6")
        public static let greenLEDCharacteristicUUID = CBUUID.init(string: "b4250402-fb4b-4746-b2b0-93f0e61122c6")
        public static let blueLEDCharacteristicUUID  = CBUUID.init(string: "b4250403-fb4b-4746-b2b0-93f0e61122c6")

    }

```

Back in `ViewController.swift` let's piece together the Bluetooth bits.

### Bluetooth bits

![Flow diagram for Bluetooth Swift in iOS](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-3cb1d250-f9d5-4757-a244-be29bed9dcf6.jpg)

Everything to do with Bluetooth is event based. We'll be defining several functions that handle these events. Here are the important ones:

`centralManagerDidUpdateState` updates when the Bluetooth Peripheral is switched on or off. It will fire when an app first starts so you know the state of Bluetooth. We also start scanning here.

The `centralManager` `didDiscover` event occurs when you receive scan results. We'll use this to start a connection.

The `centralManager` `didConnect` event fires once the device is connected. We'll start the device discovery here. **Note:** Device discovery is the way we determine what services and characteristics are available. This is a good way to confirm what type of device we're connected to.

The `peripheral` `didDiscoverServices` event first once all the services have been discovered. Notice that we've switched from `centralManager` to `peripheral` now that we're connected. We'll start the characteristic discovery here. We'll be using the RGB service UUID as the target.

The `peripheral` `didDiscoverCharacteristicsFor` event will provide all the characteristics using the provided service UUID. This is the last step in the chain of doing a full device discovery. It's hairy but it only has to be done once during the connection phase!

### Defining all the Bluetooth functions.

Now that we know what the functions events that get triggered. We'll define them in the logical order that they happen during a connection cycle.

First, we'll define `centralManagerDidUpdateState` to start scanning for a device with our Particle RGB LED Service. If Bluetooth is not enabled, it will not do anything.

```swift
    // If we're powered on, start scanning
        func centralManagerDidUpdateState(_ central: CBCentralManager) {
            print("Central state update")
            if central.state != .poweredOn {
                print("Central is not powered on")
            } else {
                print("Central scanning for", ParticlePeripheral.particleLEDServiceUUID);
                centralManager.scanForPeripherals(withServices: [ParticlePeripheral.particleLEDServiceUUID],
                                                  options: [CBCentralManagerScanOptionAllowDuplicatesKey : true])
            }
        }

```

Defining the `centralManager` `didDiscover` is our next step in the process. We know we've found a device if this event has occurred.

```swift
    // Handles the result of the scan
        func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {

            // We've found it so stop scan
            self.centralManager.stopScan()

            // Copy the peripheral instance
            self.peripheral = peripheral
            self.peripheral.delegate = self

            // Connect!
            self.centralManager.connect(self.peripheral, options: nil)

        }

```

So, we stop scanning using `self.centralManager.stopScan()`. We set the `peripheral` so it persists through the app. Then we connect to that device using `self.centralManager.connect`

Once connected, we need to double check if we're working with the right device.

```swift
    // The handler if we do connect succesfully
        func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
            if peripheral == self.peripheral {
                print("Connected to your Particle Board")
                peripheral.discoverServices([ParticlePeripheral.particleLEDServiceUUID])
            }
        }

```

By comparing the two peripherals we'll know its the device we found earlier. We'll kick off a services discovery using `peripheral.discoverService`. We can use `ParticlePeripheral.particleLEDServiceUUID` as a parameter. That way we don't pick up any services we don't care about.

Once we finish the discovering services, we'll get a `didDiscoverServices` event. We iterate through all the "available" services. (Though there will only be one!)

```swift
    // Handles discovery event
        func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
            if let services = peripheral.services {
                for service in services {
                    if service.uuid == ParticlePeripheral.particleLEDServiceUUID {
                        print("LED service found")
                        //Now kick off discovery of characteristics
                        peripheral.discoverCharacteristics([ParticlePeripheral.redLEDCharacteristicUUID,
                                                                 ParticlePeripheral.greenLEDCharacteristicUUID,
                                                                 ParticlePeripheral.blueLEDCharacteristicUUID], for: service)
                        return
                    }
                }
            }
        }

```

By this point this is the third time we're checking to make sure we have the correct service. This becomes more handy later when there are many characteristics and many services.

We call `peripheral.discoverCharacteristics` with an array of UUIDs for the characteristics we're looking for. They're all the UUIDs that we defined in `ParticlePeripheral.swift`.

Finally, we handle the `didDiscoverCharacteriscsFor` event. We iterate through all the available characteristics. As we iterate we compare with the ones we're looking for.

```swift
    // Handling discovery of characteristics
        func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
            if let characteristics = service.characteristics {
                for characteristic in characteristics {
                    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
                        print("Red LED characteristic found")
                    } else if characteristic.uuid == ParticlePeripheral.greenLEDCharacteristicUUID {
                        print("Green LED characteristic found")
                    } else if characteristic.uuid == ParticlePeripheral.blueLEDCharacteristicUUID {
                        print("Blue LED characteristic found");
                    }
                }
            }
        }

```

At this point we're ready to do a full device discovery of our Particle Mesh device. In the next section we'll test what we have to make sure things are working ok.

## Testing our minimal example

![Section image about testing](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-6-744bf855-fd7c-403b-b07f-dfc0c191b6af.jpg)

Before we get started, if you run into trouble I've put some troubleshooting steps in the [footnotes](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/#troubleshooting).

**To test, you'll have to have an iPhone with Bluetooth Low Energy.** Most modern iPhones have it. The last iPhone not to have it I believe was either the iPhone 4 or 3Gs. (so you're likely good)

First, plug it into your computer.

Go to the top by the play and stop buttons. Select your target device. In my case I chose my phone (**Jared's iPhone**). You can also use an iPad.

![Select device type](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-09_at_4-d04de709-6000-4161-bd12-7347a70d6e1e.37.27_PM.png)

Then you can hit **Command + R** or hit that **Play button** to load the app to your phone.

Make sure you have your log tab open. Enable it by clicking the bottom pane button in the top right corner.

![Bottom pane in Xcode for logs](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-09_at_4-8b83ea0a-274f-4a41-a5ff-e80717b41977.38.57_PM.png)

Make sure you have a mesh device setup and running the example code. You can go to [this post](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/#final-code) to get it. Remember your Particle Mesh board needs to be running device OS 1.3.0 or greater for Bluetooth to work!

Once both the firmware and app is loaded, let's check the log output.

It should look something like this:

```
View loaded
Central state update
Central scanning for B4250400-FB4B-4746-B2B0-93F0E61122C6
Connected to your Particle Board
LED service found
Red LED characteristic found
Green LED characteristic found
Blue LED characteristic found

```

This means that your Phone has connected, found the LED service! The characteristics also being discovered is important here. Without those we wouldn't be able to send data to the mesh device.

Next step is to create some sliders so we can update the RGB values on the fly.

## Slide to the left. Slide to the right.

Next we're going to add some elements to our `Main.storyboard`. Open `Main.storyboard` and click on the **View** underneath **View Controller.**

![Updating view in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-7919e3c2-cb72-4297-b9e0-06139a064fec.57.37_PM.png)

Then click on the **Library** button. (It looks like the old art Apple used for the home button)

![Library button in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-895d247a-6706-4c39-be04-0bda41195ca6.58.02_PM.png)

You'll get a pop-up with all the choices that you can insert into your app.

![Library pane in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-8b531053-621e-4c14-8086-2ac0ef6e52de.58.31_PM.png)

Drag three **Labels** and copy three **Sliders** to your view.

![Dragging Labels to Xcode View](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-9c8c6167-2279-4cb7-a37b-c24b8cdd275d.59.39_PM.png)

You can double click on the labels and rename them as you go.

![Dragging Slider to Xcode View](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-72573a66-1201-4d08-902d-ea905c91b2bb.59.57_PM.png)

If you click and hold, some handy alignment tools will popup. They'll even snap to center!

![Alignment tools in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-4c7b1627-c55e-4eba-b29a-32915ba41867.00.17_PM.png)

You can also select them all and move them together. We'll align them vertically and horizontally.

In order for them to stay in the middle, let's remove the autoresizing property. Click the **Ruler icon** on the top right. Then click each of the **red bars**. This will ensure that your labels and sliders stay on the screen!

![Ruler pane in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-f207fae8-7292-4e38-9985-c97444ab4e55.09.39_PM.png)

Next let's click the **Show Assistant Editor** button. (Looks like a Venn diagram)

![Show Assistant Editor button in Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-c52c52b8-70b3-426b-9cbe-9df1042f5fb1.00.59_PM.png)

**Note:** make sure that **ViewController.swift** is open in your Assistant Editor.

![Automatic option in Assistant Editor](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-655a4468-4da8-4841-a2dc-1cf8706592e7.17.35_PM.png)

Then underneath the `/properties` section, **Control-click and drag** **the Red Slider** into your code.

![Drag slider to code](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-39480e58-fd92-4ec7-a2db-9e8524019755.01.43_PM.png)

Repeat with all the other ones. Make sure you name them something different. Your code should look like this when you're done:

```swift
        // Properties
        private var centralManager: CBCentralManager!
        private var peripheral: CBPeripheral!

        // Sliders
        @IBOutlet weak var redSlider: UISlider!
        @IBOutlet weak var greenSlider: UISlider!
        @IBOutlet weak var blueSlider: UISlider!

```

This allow us to access the value of the sliders.

Next, let's attach the **Value Changed** event to each of the sliders. **Right click** on the **Red Slider in the folder view.**

![Drag value changed event to code](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-b2ffe0a6-709e-433d-9d4c-0f8028bd096c.03.44_PM.png)

It should give you some options for events. Click and drag the **Value Changed** event to your code. Make sure you name it something that makes sense. I used **RedSliderChanged** for the Red Slider.

Repeat two more times. Your code should look like this at the end of this step:

```swift
        @IBAction func RedSliderChanged(_ sender: Any) {
        }

        @IBAction func GreenSliderChanged(_ sender: Any) {
        }

        @IBAction func BlueSliderChanged(_ sender: Any) {
        }

```

I've also selected each of the sliders to and **un-checked Enabled**. That way you can't move them. We'll enable them later on in code.

![Disable slider by default](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-e7e0aca9-224c-4bfb-b482-1d9e58b37947.21.21_PM.png)

Also, this is a great time to change the **maximum value to 255**. Also set the default **value from 0.5 to 0.**

![Set default value and max value of slider](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-9bf5618b-f6ac-4aea-9888-7f93a8c75414.55.38_PM.png)

Back at the top of the file. Let's create some local variables for each of the characteristics. We'll use these so we can write the slider variables to the Particle Mesh board.

```swift
        // Characteristics
        private var redChar: CBCharacteristic?
        private var greenChar: CBCharacteristic?
        private var blueChar: CBCharacteristic?

```

Now, let's tie everything together!

In the `didDiscoverCharacteristicsFor` callback function. Let's assign those characteristics. For example

```swift
    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
        print("Red LED characteristic found")
        redChar = characteristic

```

As we find each characteristic, we can also enable each of the sliders in the same spot.

```swift
    		// Unmask red slider
    		redSlider.isEnabled = true

```

In the end your `didDiscoverCharacteristicsFor` should look like:

```swift
    // Handling discovery of characteristics
        func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
            if let characteristics = service.characteristics {
                for characteristic in characteristics {
                    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
                        print("Red LED characteristic found")

                        redChar = characteristic
                        redSlider.isEnabled = true
                    } else if characteristic.uuid == ParticlePeripheral.greenLEDCharacteristicUUID {
                        print("Green LED characteristic found")

                        greenChar = characteristic
                        greenSlider.isEnabled = true
                    } else if characteristic.uuid == ParticlePeripheral.blueLEDCharacteristicUUID {
                        print("Blue LED characteristic found");

                        blueChar = characteristic
                        blueSlider.isEnabled = true
                    }
                }
            }
        }

```

Now, let's update the `RedSliderChanged` `GreenSliderChanged` and `BlueSliderChanged` functions. What we want to do here is update the characteristic associated with the `Changed` function. I created a separate function called `writeLEDValueToChar`. We'll pass in the characteristic and the data.

```swift
    private func writeLEDValueToChar( withCharacteristic characteristic: CBCharacteristic, withValue value: Data) {

            // Check if it has the write property
            if characteristic.properties.contains(.writeWithoutResponse) && peripheral != nil {

                peripheral.writeValue(value, for: characteristic, type: .withoutResponse)

            }

        }

```

Now add a call to `writeLEDValueToChar` to each of the `Changed` functions. You will have to cast the value to a `Uint8`. (The Particle Mesh device expects an unsigned 8-bit number.)

```swift
    		@IBAction func RedSliderChanged(_ sender: Any) {
            print("red:",redSlider.value);
            let slider:UInt8 = UInt8(redSlider.value)
            writeLEDValueToChar( withCharacteristic: redChar!, withValue: Data([slider]))

        }

```

Repeat this for `GreenSliderChanged` and `BlueSliderChanged`. Make sure you changed `red` to `green` and `blue` for each!

Finally, to keep things clean, i've also added a function that handles Bluetooth disconnects.

```swift
    func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error: Error?) {

```

Inside, we should reset the state of the sliders to 0 and disable them.

```swift
            if peripheral == self.peripheral {
                print("Disconnected")

                redSlider.isEnabled = false
                greenSlider.isEnabled = false
                blueSlider.isEnabled = false

                redSlider.value = 0
                greenSlider.value = 0
                blueSlider.value = 0

```

It's a good idea to reset `self.peripheral` to nil that way we're not ever trying to write to a phantom device.

```swift
                self.peripheral = nil

```

Finally, because we've disconnected, start scanning again!

```swift
                // Start scanning again
                print("Central scanning for", ParticlePeripheral.particleLEDServiceUUID);
                centralManager.scanForPeripherals(withServices: [ParticlePeripheral.particleLEDServiceUUID],
                                                  options: [CBCentralManagerScanOptionAllowDuplicatesKey : true])
            }

```

Alright! We just about ready to test. Let's move on to the next (and final) step.

## Test the sliders.

![Next section test!](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-5-3af7db2e-8bf7-4561-98c2-a1b7ab0c685b.jpg)

The hard work is done. Now it's time to play!

The easiest way to test everything is to **click the Play button** in the top left or the **Command + R** keyboard shortcut. Xcode will load the app to your phone. You should see a white screen proceeded by a screen with your sliders!

The sliders should stay greyed out until connected to your Particle Mesh board. You can check your log output if the connection has been established.

```
View loaded
Central state update
Central scanning for B4250400-FB4B-4746-B2B0-93F0E61122C6
Connected to your Particle Board
LED service found
Red LED characteristic found
Green LED characteristic found
Blue LED characteristic found

```

(Look familiar? We're connected!)

If you followed everything perfectly, you should be able to move the sliders. Better yet, the RGB LED on the Particle Mesh board should change color.

![Final test results](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/DSC01556-1fda5018-f1f5-4855-8705-f7d344ce3d78.jpeg)

## Conclusion

In this article you've learned how to connect your Particle Mesh board and iOS device over Bluetooth. We've learned how to connect to each of the available characteristics. Plus, on top of it all, make a clean interface to do it all in.

As you can imagine, you can go down the rabbit hole with Bluetooth on iOS. There's more coming in my upcoming guide: **The Ultimate Guide to Particle Mesh.** Subscribers to my list get access to pre-launch content and a discount when it comes out! [Click here to get signed up.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/)

## Code

The full source code is available on [Github.](https://github.com/jaredwolff/swift-bluetooth-particle-rgb) If you find it useful, hit the star button. ⭐️

