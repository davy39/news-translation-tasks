---
title: An Overview of Android Storage
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-08-25T16:05:00.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-android-storage
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0aa740569d1a4ca4a11.jpg
tags:
- name: Android
  slug: android
- name: coding
  slug: coding
- name: development
  slug: development
- name: storage
  slug: storage
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: Storage is this thing we are all aware of, but always take for granted.
  Not long ago, every leap in storage capacity was incremental and appeared to be
  impossible. Nowadays, we don’t give a second thought when contemplating how much
  of it our devices...
---

Storage is this thing we are all aware of, but always take for granted. Not long ago, every leap in storage capacity was incremental and appeared to be impossible. Nowadays, we don’t give a second thought when contemplating how much of it our devices have (and couldn't care less about the differences).

A bigger point would be to look at the evolution of what is stored in memory. Before smartphones, we saved the occasional photo or two, some games and a ton of text messages. But now, any standard phone will have a concoction of applications, documents, photos, videos, music files, and more. Let’s find out how we can utilize a devices's storage space for our applications.

What we’re going to cover in this article is:

1. The different types of storage on Android phones
2. Differences between the types of storage
3. How to use storage in your application

Each application has access to two different types of storage: **_internal_** and **_external_**. There are major differences between these two types of storage, and knowing them will help you when designing your next application.

Before we begin, one thing must be said about storage and cache. Storage is meant for things you want to save persistently, while cache is there to save things temporarily.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-227.png)
_Photo by [Unsplash](https://unsplash.com/@erdaest?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Erda Estremera</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Internal Storage

When each application is run on the operating system, it has its own internal storage. This storage is private and only for the use of the application. Meaning, other applications cannot access it, nor can the user. Another thing to keep in mind when using internal storage is the availability of it. Unlike external storage, internal storage is always available for your application. 

Using this storage has its drawbacks, though. If the user removes the application, all the data stored in your app's internal storage is removed as well. Imagine what would happen if you installed a game on your phone and somewhere down the road decided to remove it. You would like to have your game progress saved, if by any chance you would install the game again.

So, how do we save a file to internal storage?

```java
public void saveFileInternalStorage() {
   
        String FILENAME = "hello_world_file";
        String inputToFile = "Hello From Internal Storage!";
   
        try {
            FileOutputStream fileOutputStream = openFileOutput(FILENAME, Context.MODE_PRIVATE);
            fileOutputStream.write(inputToFile.getBytes());
            fileOutputStream.close();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has been saved successfully",
                    Toast.LENGTH_SHORT).show();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has not been saved successfully due to an exception " + e.getLocalizedMessage(),
                    Toast.LENGTH_SHORT).show();
        } catch (IOException e) {
            e.printStackTrace();
            Toast.makeText(getApplicationContext(),
                    "File " + FILENAME + " has not been saved successfully due to an exception " + e.getLocalizedMessage(),
                    Toast.LENGTH_SHORT).show();
        }
 }
```

As you can see in the code example, we are saving a file called **_hello_world_file_** that contains the text, **_“Hello From Internal Storage!”_**. I have created two catch clauses just to demonstrate the exceptions that may occur when trying to do this, but you can minimize them to one catch clause with the general Exception object.

Pay attention that the method **_openFileOutput_** will open the file if it already exists, but if not, will create it. The second parameter to this method is the file mode. This parameter designates the scope of the file and access to it. The default value is MODE_PRIVATE, which makes the file accessible to your application only. 

The other two values for this parameter are MODE_WORLD_READABLE and MODE_WORLD_WRITEABLE, but they have been deprecated since API 17. Sharing private files with other applications uses a different set of logic that you can read more about [here](https://developer.android.com/training/secure-file-sharing). Finally, when writing to the file, we convert our string to bytes and we make sure to close the file at the end.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-228.png)
_Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Spiske</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## External Storage

Contrary to what the name implies, this is storage that is defined by the fact that it is not always accessible. This may mean that it can be an external SD card (secondary external storage), but it can also be storage found on the device (primary external storage). 

To bring the fact home, external storage is storage that can be accessed when you connect your device to a computer via a USB cable. As you may have guessed, anything stored in this type of storage is accessible to other applications on your device, but will be kept if you uninstall the application.

Before we can demonstrate how to save files to the external storage, we need to do two things:

1. Make sure there is enough space there to save the file
2. Ask for permission during runtime

Making sure there is enough storage space requires the following lines of code:

```java
//Check if you can read/write to external storage
public boolean isExternalStorageWritable() {
    String state = Environment.getExternalStorageState();
    if (Environment.MEDIA_MOUNTED.equals(state)) {
        return true;
    }
    return false;
}
```

To get access to the external storage, we need to add the following permission to our AndroidManifest.xml:

```java
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

Furthermore, since API 23, dangerous permissions aren’t authorized during install time, but during runtime. Writing to external storage is categorized as one, so we need to add logic to allow the user to decide whether to grant the application permission or not.

```java
public void saveFileExternalStorage(View view) {
        if (isExternalStorageWritable()) {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) ==
                PackageManager.PERMISSION_GRANTED) {
                    writeFileToExternalStorage();
                } else{
                    ActivityCompat.requestPermissions(this,
                            new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 0);
                }
            }
        }

        @Override
        public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
            switch (requestCode) {
                case 0:
                {
                    writeFileToExternalStorage();
                    break;
                }
            }
        }
```

Our **_writeFileToExternalStorage_** looks like this:

```java
public void writeFileToExternalStorage() {
            String root = Environment.getExternalStorageDirectory().toString();
            File myDir = new File(root + "/saved_files");
            if (!myDir.exists()) {
                myDir.mkdirs();
            }
            try {
                File file = new File(myDir, "myfile.txt");
                FileOutputStream out = new FileOutputStream(file);
                out.write(inputToFile.getBytes());
                out.close();
                Toast.makeText(getApplicationContext(),
                        "File myfile.txt" + " has been saved successfully to external storage",
                        Toast.LENGTH_SHORT).show();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
```

If you want to see an example of all the code presented here, you can head over to this [GitHub repository](https://github.com/TomerPacific/MediumArticles/tree/master/AndroidStorage).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-229.png)
_Photo by [Unsplash](https://unsplash.com/@steve_j?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Steve Johnson</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Good To Know

Above were just two simple examples of how to work with the different types of storage for your application. Since we are dealing with a resource that the system manages, we should also be aware of the behaviors associated with it.

By default, your application will be installed to internal storage (**_see internalOnly explanation_**), but from API level 8, you can add an attribute, **_installLocation_**, to your manifest that lets your application be installed to external storage. One reason for doing so is if your application is very large, and you would prefer the user to install it on the device’s external storage since there is more space there. 

There are three values for this attribute:

* **_auto_** - means that you don’t have a specific preference where the application will be installed. The application will try to be installed to internal storage, but if it is full, it will install it inside external storage
* **_internalOnly_** - the application will only be installed to internal storage, and if there isn’t enough space there, it will not be installed
* **_preferExternal_** - means that you want your application to be installed to external storage, but if there is not enough room there, it will be installed internally

For both the auto and the preferExternal options, the user has the option of moving the application from external storage to internal, and vice versa.

Keep in mind that once a user connects their device to a computer and enables it to share data or unmounts an SD card, all applications running from the external storage are destroyed. If your application uses one of the following features, you should not install it to external storage:

> _Various services (alarm service_s _in particular), Input Method Engines, Live Wallpapers, Application Widgets, Account Managers, Sync Adapters, Device Administrators and Broadcast receivers listening for boot completed._

