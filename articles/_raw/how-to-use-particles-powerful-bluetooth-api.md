---
title: How to Use Particle's Powerful Bluetooth API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T12:39:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-particles-powerful-bluetooth-api
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Particle-Bluetooth.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: hardware
  slug: hardware
- name: particle
  slug: particle
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  I was defeated.

  I had spent the whole night trying to get a Bluetooth Low Energy project working.
  It was painful. It was frustrating. I was ready to give up.

  That was during the early day...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/)**

I was defeated.

I had spent the whole night trying to get a Bluetooth Low Energy project working. It was painful. It was frustrating. I was ready to give up.

That was during the early days of Bluetooth Low Energy. Since then it's gotten easier and easier to develop. The Particle Mesh Bluetooth Library is no exception.

In this walkthrough, i'll show you how to use Particle's Bluetooth API. We'll configure some LEDs and watch them change over all devices in the Mesh network. We'll be using an Argon and Xenon board.

Ready? Let's get started!

P.S. this post is lengthy. If you want something to download, [click here for a beautifully formatted PDF.](https://www.jaredwolff.com/files/how-to-use-particles-powerful-bluetooth-api-pdf)

## Stage 1: Setting Up Bluetooth

1. [Download/Install Particle Workbench](https://www.particle.io/workbench/)
2. Create a new Project. I picked a suitable location and then named it `ble_mesh`

    ![Create a new Project in Particle Workbench](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_5-4348ea15-e220-4138-8d28-a8c5de99e9fe.32.11_PM.png)

3. Go to your `/src/` direcory and open your `<your project name>.ino` file
4. Then make sure you change the version of your deviceOS to  > **1.3.0**

    ![Select DeviceOS Version](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_5-9d20c90b-e27c-4609-9917-2ec1bb849727.40.15_PM.png)

### Write the Code

We want to set up a service with 3 characteristics. The characteristics relate to the intensity of the RGB LEDs respectively. Here's how to get your Bluetooth Set Up:

1. In your `Setup()` function enable app control of your LED

    ```
    RGB.control(true);
    ```

2. Set up your UUIDs at the top of your `.ino` file

        const char* serviceUuid = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* red         = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* green       = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* blue        = "6E400004-B5A3-F393-E0A9-E50E24DCCA9E";

    UUIDs are unique identifiers or addresses. They're used to differentiate different services and characteristics on a device.

    The above UUIDs are used in previous Particle examples. If you want to create your own you can use  `uuidgen` on the OSX command line. You can also go to a website like **[Online GUID Generator](https://www.guidgenerator.com/online-guid-generator.aspx).**

    ![Online GUID Generator](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-14_at_11-343e1df6-69e8-4560-98b9-f2f54caeb7d3.28.46_AM.png)

    Use the above settings to get your own UUID. You can then create your service and characteristic UUIDS from this generated one:

        const char* serviceUuid = "b425040**0**-fb4b-4746-b2b0-93f0e61122c6"; //service
        const char* red         = "b4250401-fb4b-4746-b2b0-93f0e61122c6"; //red char
        const char* green       = "b4250402-fb4b-4746-b2b0-93f0e61122c6"; //green char
        const char* blue        = "b4250403-fb4b-4746-b2b0-93f0e61122c6"; //blue char

    There's no right or wrong way to do this. But you have to be careful you're not using the UUIDs reserved by the Bluetooth SIG. This is highly unlikely. If you do want to double check you can go [here](https://www.bluetooth.com/specifications/gatt/characteristics/) and [here](https://www.bluetooth.com/specifications/gatt/services/).

    For now, we'll stick with the first set of UUIDs.

3. In `Setup()`, initialize your service.

        // Set the RGB BLE service
        BleUuid rgbService(serviceUuid);

    This is the first step of "registering' your service. More on this below.

4. Initialize each characteristic in `Setup()`

        BleCharacteristic redCharacteristic("red", BleCharacteristicProperty::WRITE_WO_RSP, red, serviceUuid, onDataReceived, (void*)red);
        BleCharacteristic greenCharacteristic("green", BleCharacteristicProperty::WRITE_WO_RSP, green, serviceUuid, onDataReceived, (void*)green);
        BleCharacteristic blueCharacteristic("blue", BleCharacteristicProperty::WRITE_WO_RSP, blue, serviceUuid, onDataReceived, (void*)blue);

    For this setup, we're going to use the `WRITE_WO_RSP` property. This allows us to write the data and expect no response.
    I've referenced the UUIDs as the next two parameters. The first being the characteristic UUID. The second being the service UUID.

    The next parameter is the callback function. When data is written to this callback, this function will fire.

    Finally the last parameter is the context. What does this mean exactly? We're using the same callback for all three characteristics. The only way we can know which characteristic was written to (in deviceOS at least) is by setting a context. In this case we're going to use the already available UUIDs.

5. Right after defining the characteristics, let's add them so they show up:

        // Add the characteristics
        BLE.addCharacteristic(redCharacteristic);
        BLE.addCharacteristic(greenCharacteristic);
        BLE.addCharacteristic(blueCharacteristic);

6. Set up the callback function.

        // Static function for handling Bluetooth Low Energy callbacks
        static void onDataReceived(const uint8_t* data, size_t len, const BlePeerDevice& peer, void* context) {

        }

    You can do this at the top of the file (above `Setup()`) We will define this more later.

7. Finally, in order for your device to be connectable, we have to set up advertising. Place this code at the end of your `Setup()` function

        // Advertising data
        BleAdvertisingData advData;

        // Add the RGB LED service
        advData.appendServiceUUID(rgbService);

        // Start advertising!
        BLE.advertise(&advData);

    First we create a `BleAdvertisingData` object. We add the `rgbService` from Step 3. Finally, we can start advertising so our service and characteristics are discoverable!

### Time to test

At this point we have a minimally viable program. Let's compile it and program it to our Particle hardware. This should work with any Mesh enabled device. (Xenon, Argon, Boron)

1. Before we start testing, temporarily add `SYSTEM_MODE(MANUAL);` to the top of your file. This will prevent the device connecting to the mesh network. If the device is blinking blue on startup, you'll have to set it up with the [Particle App](https://apps.apple.com/ru/app/particle-iot/id991459054?l=en) before continuing.
2. [Download the 1.3.0-rc.1 image here.](https://github.com/particle-iot/device-os/releases/tag/v1.3.0-rc.1) For Xenon, you'll need **xenon-system-part1@1.3.0-rc.1.bin.** For others look for **boron-system-part1@1.3.0-rc.1.bin** and **argon-system-part1@1.3.0-rc.1.bin.** The files are at the bottom of the page under **Assets**

    ![Assets location on DeviceOS Release Page](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-14_at_11-df9b46f4-e230-484e-b69e-828526f5566e.39.39_AM.png)

3. Put your device into DFU mode. Hold the **Mode Button** and momentarily click the **Reset** **Button.** Continue holding the **Mode Button** until the LED blinks yellow.
4. In a command line window, change directories to where you stored the file you downloaded. In my case the command is `cd ~/Downloads/`
5. Then run:

        particle flash --usb xenon-system-part1@1.3.0-rc.1.bin

    This will install the latest OS to your Xenon. Once it's done it will continue to rapidly blink yellow. Again if you have a different Particle Mesh device, change the filename to match.

6. In Visual Code, use the **Command + Shift + P** key combination to pop up the command menu. Select **Particle: Compile application (local)**

    ![Compile application (local) choice](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-8cb8dda2-73ae-4b0d-af5b-33892d66752e.52.19_PM.png)

7. Fix any errors that may pop up.
8. Then, open the same menu and select **Flash application (local)**

    ![Flash application (local) choice](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-4ff7bc95-58f1-497f-9edf-9eadb69e3abb.51.59_PM.png)

9. When programming is complete, pull out your phone.  Then, open your favorite Bluetooth Low Energy app. The best ones are **[NRF Connect](https://apps.apple.com/cn/app/nrf-connect/id1054362403?l=en)** and **[Light Blue Explorer.](https://apps.apple.com/ru/app/lightblue-explorer/id557428110?l=en)** I'm going to use Light Blue Explorer for this example.
10. Check if a device named **"Xenon-<ID>"** is advertising. Insert **<ID>** with the unique ID for your device.

    ![Light Blue Explorer Scan Results](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2187-aa8b88cc-f423-4b5a-8bb0-e1f75c3b7dd9.png)

11. Find your device and click the name.
12. Look at the list of services & characteristics. Does it include the service and characteristic UUID's that we have set so far? For instance, does the service UUID show up as **6E400001-B5A3-F393-E0A9-E50E24DCCA9E**?

    ![Confirm Light Blue Explorer has new characteristic UUIDs](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2188-d7759af0-964e-4067-9ca2-d78edd190410.png)

    If everything shows up as you expect, you're in a good place. If not go through the earlier instructions to make sure everything matches.

## Stage 2: Handling Data

The next stage of our project is to process write events. We'll be updating our `onDataReceived` function.

### Write the Code

1. First, let's create a struct that will keep the state of the LEDs. This can be done at the top of the file.

        // Variables for keeping state
        typedef struct {
          uint8_t red;
          uint8_t green;
          uint8_t blue;
        } led_level_t;

2. The second half of that is to create a static variable using this data type

        // Static level tracking
        static led_level_t m_led_level;

    The first two steps allows us to use one single variable to represent the three values of the RGB LED.

3. Next, let's check for basic errors inside the `onDataReceive` function For instance we want to make sure that we're receiving only one byte.

        // We're only looking for one byte
          if( len != 1 ) {
            return;
        	}

4. Next, we want to see which characteristic this event came from. We can use the `context` variable to determine this.

        // Sets the global level
          if( context == red ) {
            m_led_level.red = data[0];
          } else if ( context == green ) {
            m_led_level.green = data[0];
          } else if ( context == blue ) {
            m_led_level.blue = data[0];
          }

    Remember, in this case context will be equal to the pointer of either the red, green, or blue UUID string. You can also notice we're setting `m_led_level`. That way we can update the RGB led even if only one value has changed.

5. Finally, once set, you can write to the `RGB` object

        // Set RGB color
        	RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

### Test the Code

Let's go through the same procedure as before to flash the device.

1. Put your device into DFU mode. Hold the **Mode Button** and click the **Reset** **Button.** Continue holding the **Mode Button** until the LED blinks yellow.
2. Then, open the same menu and select **Flash application (local)**

    ![Flash application (local) choice](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-4ff7bc95-58f1-497f-9edf-9eadb69e3abb.51.59_PM.png)

3. Once it's done programming, connect to the device using **Light Blue Explorer**.
4. Tap on the characteristic that applies to the red LED.
5. **Write FF**. The red LED should turn on.

    ![Write new value choice](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2191-b8ad0693-f4f8-4828-ae99-b0a0e204cc50.jpg)

    ![Write the hex value of 0xff](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2190-2c799875-22e5-44bc-9edc-c647cf8669f6.png)

6. **Write 00**. The red LED should turn off.
7. Do the same for the other two characteristics. We now have full control of the RGB LED over Bluetooth Low Energy!

## Stage 3: Sharing Via Mesh

Finally, now that we're successfully receiving BLE message, it's time to forward them on to our mesh network.

### Write the Code

1. First let's remove MANUAL mode. Comment out `SYSTEM_MODE(MANUAL);`
2. At the top of the file let's add a variable we'll used to track if we need to publish

        // Tracks when to publish to Mesh
        static bool m_publish;

3. Then initialize it in `Setup()`

        // Set to false at first
        m_publish = false;

4. Then, after setting the RGB led in the `onDataReceived` callback, let's set it true:

        // Set RGB color
        RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

        // Set to publish
        m_publish = true;

5. Let's add a conditional in the `loop()` function. This will cause us to publish the LED status to the Mesh network:

        if( m_publish ) {
        	// Reset flag
        	m_publish = false;

        	// Publish to Mesh
          Mesh.publish("red", String::format("%d", m_led_level.red));
          Mesh.publish("green", String::format("%d", m_led_level.green));
          Mesh.publish("blue", String::format("%d", m_led_level.blue));
        }

    `Mesh.publish` requires a string for both inputs. Thus, we're using `String::format` to create a string with our red, green and blue values.

6. Then let's subscribe to the same variables in `Setup()`. That way another device can cause the LED on this device to update as well.

        Mesh.subscribe("red", meshHandler);
        Mesh.subscribe("green", meshHandler);
        Mesh.subscribe("blue", meshHandler);

7. Toward the top of the file we want to create `meshHandler`

        // Mesh event handler
        static void meshHandler(const char *event, const char *data)
        {
        }

8. In this application, we need the `event` parameter and `data` parameter. In order use them, we have to change them to a `String` type. That way we can use the built in conversion and comparison functions. So, inside the `meshHandler` function add:

          // Convert to String for useful conversion and comparison functions
          String eventString = String(event);
          String dataString = String(data);

9. Finally we do some comparisons. We first check if the event name matches. Then we set the value of the `dataString` to the corresponding led level.

          // Determine which event we recieved
          if( eventString.equals("red") ) {
            m_led_level.red = dataString.toInt();
          } else if ( eventString.equals("green") ) {
            m_led_level.green = dataString.toInt();
          } else if ( eventString.equals("blue") ) {
            m_led_level.blue = dataString.toInt();
          } else {
        		return;
        	}

          // Set RGB color
          RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

    Then at the end we set the new RGB color. Notice how I handle an unknown state by adding a `return` statement in the `else` section. It's always good to filter out error conditions before they wreak havoc!

### Test the Code

1. Open the Particle App on your phone
2. Let's set up the Argon first. **If it's not blinking blue, hold the mode button until it's blinking blue.**

    ![Particle Argon with Blue LED](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_1216-f78725ab-a9f5-4270-b389-73d6dddb1f62.jpg)

    Note: if you've already programmed the app, the LED will be off by default. **Hold the mode button for 5 seconds and then continue.**

3. Go through the pairing process. The app walks you though all the steps. **Make sure you remember the Admin password for your mesh network.**

    ![Particle Setup App Board Choice](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2194-2482aa12-082c-4786-8883-860b50b4cd53.png)

    ![Scan the sticker](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2195-2d030603-e59f-4e76-9d1a-9d4f2c078a4e.png)

    ![Pairing with your Argon](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2198-80bb83d8-818b-4cd8-a583-9262da9b5121.png)

    ![Enter wifi password](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2199-e3c107dd-2704-4aa3-9781-550ad14ea7fc.png)

4. Program an Argon with the latest firmware (1.3.0) (see **Stage 1 - Time to Test - Step 2** for a reminder on how to do this)
5. Once rapidly blinking yellow, program the Argon with the Tinker app. You can download it at the [release page](https://github.com/particle-iot/device-os/releases/tag/v1.3.0-rc.1).
6. Once we have a nice solid Cyan LED (connected to the Particle Cloud) we'll program the app. Use the **Cloud Flash** option in the drop down menu.

    ![Cloud Flash option](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_9-a50458b1-ade1-4d4d-818b-ef214f3fec5d.55.19_AM.png)

    As far as I can tell, Particle forces any device flashed locally into safe mode when connecting to the cloud. It may be my setup. Your mileage may vary here. Best to use  **Cloud Flash**.

    Make sure you select the correct deviceOS version (**1.3.0-rc1**), device type (**Argon**) and device name (**What you named it during setup**)

7. Connect to the Xenon using the **phone app**
8. Connect the Xenon to your Mesh network using the phone app
9. Flash your Xenon using **Cloud Flash**. Use the name that you gave it during the phone app setup. As long as the device is connected to Particle Cloud or in safe mode (Purple LED), it should program.

    ![Confirm board type, deviceOS version and device name](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_10-2f76843b-3cee-4818-adfb-7ece4173df2d.06.32_AM.png)

    ![Cloud flash option](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_10-8e140009-440c-480d-838e-b83c782a8c96.08.47_AM.png)

10. Once connected, let's get to the fun part. Open up **Light Blue Explorer.** Connect to either the **Argon** or the **Xenon**.

    ![Select either the Argon or Xenon](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2200-e1c513ba-6689-4652-b442-e5c6f916d619.png)

11. Select one of the LED characteristics and change the value.

    ![Argon and Xenon with red LEDs on](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_0627-2db8ab26-99e1-46a2-9583-97126fbe2594.jpg)

    The LED should change on all devices!

## Final Code

Here's the final code with all the pieces put together. You can use this to make sure you put them in the right place!!

    /*
     * Project ble_mesh
     * Description: Bluetooth Low Energy + Mesh Example
     * Author: Jared Wolff
     * Date: 7/13/2019
     */

    //SYSTEM_MODE(MANUAL);

    // UUIDs for service + characteristics
    const char* serviceUuid = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* red         = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* green       = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* blue        = "6E400004-B5A3-F393-E0A9-E50E24DCCA9E";

    // Set the RGB BLE service
    BleUuid rgbService(serviceUuid);

    // Variables for keeping state
    typedef struct {
      uint8_t red;
      uint8_t green;
      uint8_t blue;
    } led_level_t;

    // Static level tracking
    static led_level_t m_led_level;

    // Tracks when to publish to Mesh
    static bool m_publish;

    // Mesh event handler
    static void meshHandler(const char *event, const char *data)
    {

      // Convert to String for useful conversion and comparison functions
      String eventString = String(event);
      String dataString = String(data);

      // Determine which event we recieved
      if( eventString.equals("red") ) {
        m_led_level.red = dataString.toInt();
      } else if ( eventString.equals("green") ) {
        m_led_level.green = dataString.toInt();
      } else if ( eventString.equals("blue") ) {
        m_led_level.blue = dataString.toInt();
      } else {
    		return;
    	}

      // Set RGB color
      RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

    }

    // Static function for handling Bluetooth Low Energy callbacks
    static void onDataReceived(const uint8_t* data, size_t len, const BlePeerDevice& peer, void* context) {

      // We're only looking for one byte
      if( len != 1 ) {
        return;
      }

      // Sets the global level
      if( context == red ) {
        m_led_level.red = data[0];
      } else if ( context == green ) {
        m_led_level.green = data[0];
      } else if ( context == blue ) {
        m_led_level.blue = data[0];
      }

      // Set RGB color
      RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

      // Set to publish
      m_publish = true;

    }

    // setup() runs once, when the device is first turned on.
    void setup() {

      // Enable app control of LED
      RGB.control(true);

      // Init default level
      m_led_level.red = 0;
      m_led_level.green = 0;
      m_led_level.blue = 0;

      // Set to false at first
      m_publish = false;

      // Set the subscription for Mesh updates
      Mesh.subscribe("red",meshHandler);
      Mesh.subscribe("green",meshHandler);
      Mesh.subscribe("blue",meshHandler);

      // Set up characteristics
      BleCharacteristic redCharacteristic("red", BleCharacteristicProperty::WRITE_WO_RSP, red, serviceUuid, onDataReceived, (void*)red);
      BleCharacteristic greenCharacteristic("green", BleCharacteristicProperty::WRITE_WO_RSP, green, serviceUuid, onDataReceived, (void*)green);
      BleCharacteristic blueCharacteristic("blue", BleCharacteristicProperty::WRITE_WO_RSP, blue, serviceUuid, onDataReceived, (void*)blue);

      // Add the characteristics
      BLE.addCharacteristic(redCharacteristic);
      BLE.addCharacteristic(greenCharacteristic);
      BLE.addCharacteristic(blueCharacteristic);

      // Advertising data
      BleAdvertisingData advData;

      // Add the RGB LED service
      advData.appendServiceUUID(rgbService);

      // Start advertising!
      BLE.advertise(&advData);
    }

    // loop() runs over and over again, as quickly as it can execute.
    void loop() {

      // Checks the publish flag,
      // Publishes to a variable called "red" "green" and "blue"
      if( m_publish ) {

        // Reset flag
        m_publish = false;

        // Publish to Mesh
        Mesh.publish("red", String::format("%d", m_led_level.red));
        Mesh.publish("green", String::format("%d", m_led_level.green));
        Mesh.publish("blue", String::format("%d", m_led_level.blue));
      }

    }

## Conclusion

In this tutorial you learned how to add Bluetooth to a Particle Mesh project. As you can imagine, the possibilities are endless. For instance you can add user/administrative apps into the experience. *Now that's awesome.* ?

You can expect more content like this in my upcoming book: ***The Ultimate Guide to Particle Mesh***. Subscribe to my list for updates and insider content. Plus all early subscribers get a discount when it's released! [Click here to sign up.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh)


