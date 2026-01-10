---
title: How to Move a Single Fly Machine and Volume to a New Region with flyctl
subtitle: ''
author: Clarence Bakosi
co_authors: []
series: null
date: '2024-07-18T13:19:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-move-a-fly-application-to-a-new-region
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Cover-1.png
tags:
- name: Cloud
  slug: cloud
- name: deployment
  slug: deployment
seo_title: null
seo_desc: 'Fly.io allows users to deploy their applications to virtual machines in
  regions where their applications are mostly used. A Fly application can also be
  deployed to multiple regions.

  You may want to move your Fly application to a new region if you exp...'
---

Fly.io allows users to deploy their applications to virtual machines in regions where their applications are mostly used. A Fly application can also be deployed to multiple regions.

You may want to move your Fly application to a new region if you experience performance issues, high latency, or data residency compliance problems. Placing your application closer to your users can reduce latency and improve response time.

Additionally, aligning your data storage with regional compliance requirements can prevent legal issues. Overall, these changes enhance the user experience with your application.

This article will cover how to smoothly move a Fly application that includes a single [Fly Machine](https://fly.io/docs/machines/overview/) and an attached [Fly Volume](https://fly.io/docs/volumes/overview/), from one [Fly region](https://fly.io/docs/reference/regions/) to another using [flyctl](https://fly.io/docs/flyctl/) commands.

## **Prerequisites**

* [Fly.io account](https://fly.io/dashboard)
* `flyctl` installed
* Command line Interface (CLI)

## **Getting Started**

To get started, you will have to verify if you already have `flyctl` installed and also get it authenticated.

### How to Verify `flyctl` Installation

You can verify that you have `flyctl` installed using the command below. If not, use this [guide](https://fly.io/docs/flyctl/install/) to install it.

```bash
fly version
```

![fly version](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.43.16.png)
_Output of fly version_

This shows the version you have installed.

### How to Authenticate `flyctl`

Connect the terminal to your account via the CLI using:

```bash
fly auth login
```

When the browser opens up, login if you aren't already logged in and proceed to authenticate your CLI.

After authenticating your account, return to the CLI.

## **How to Confirm the Region of the Application**

Navigate to the root folder of your project and run the following to determine the current region of your application:

```bash
fly status
```

![fly status](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.44.26.png)
_Output of fly status_

The application's current region is `lhr`, the command shows additional information about the application, including the app name, owner, hostname, image, and machine details.

## **How to Verify the Number of Volumes Available**

Run the following command to list all volumes:

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-19.45.05.png)
_Output of fly volumes list_

There should be only one volume that exists and it should be already attached to a machine. You can use this [guide](https://fly.io/docs/apps/volume-storage/#launch-a-new-app-with-a-fly-volume) to create an application with a single machine with an attached volume.

## **How to Verify that the Volume is Attached to a Machine**

To ensure the volume is attached to a machine, run:

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.14.04.png)
_Output of fly machine list_

From the output, you can determine if there is a volume attached to the machine.

## **List of Fly Regions**

To determine the new region you want to move the Machine and volume to, use the following command to view the list of available regions:

```bash
fly platform regions
```

![fly platform regions](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.15.13.png)
_Output of fly platform regions_

For this article, the machine and volume will be moved to the `syd` region.

## **Fork the Available Volume to a New Region**

You can create a copy of an existing volume and place it into a new region by forking it using the current volume ID to create a fork:

```bash
fly volumes fork vol_4yj0k93z118j9x14 --region syd
```

Result:

![fly volumes fork](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.16.00.png)
_Output of fly volumes fork_

This shows information about the newly created volume.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.18.52.png)
_Output of fly volumes list_

The current state of the new forked volume in a new region will be in a `hydrating` state for a couple of minutes before it is changed to `created`.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.19.11.png)
_Output of fly volumes list_

The image above shows current state after `hydrating` is complete.

You have successfully created a new volume in another region containing data from the volume existing in the old region.

## **How to Clone the Existing Machine**

Fly possesses the clone feature to replicate a machine and you can make use of this by getting the ID of the existing machine.

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.19.43.png)
_Output of fly machine list_

After retrieving the ID of the machine, use the command below to clone the machine and attach the new volume using the same region as the newly created volume:

For example:

```bash
fly machine clone <machine id> --region <region code> --attach-volume <volume id>:<destination_mount_path>
```

It's important to note that the `destination_mount_path` has to be a different path other than `/` which is the root directory of the application. It should be a unique path `/zata`.

```bash
fly machine clone 5683977a624218 --region syd --attach-volume vol_vzkd2l6yxnk72p9v:/zata
```

![fly machine clone](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.20.06.png)
_Output of fly machine clone_

You have successfully created a clone of the existing machine and attached the forked volume.

## **How to Verify the Volume Attachment**

To check if the volume has been successfully attached:

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.20.37.png)
_Output of fly volumes list_

The volume is now attached to a machine.

To check if the machine has been successfully attached:

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.21.08.png)
_Output of fly machine list_

The machine now has a volume attached.

You have successfully moved the machine and volume to a new region.

## **How to View the Application Available Regions**

Currently, the application exists in two different regions and you can view this using the following command:

```bash
fly scale show
```

![fly scale show](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.21.30.png)
_Output of fly scale show_

The application is now running in `lhr` and `syd`.

## **How to Update the Remote fly.toml**

Add the new region to the **fly.toml** file `primary_region = 'syd'`, update the volume destination to `destination = '/zata'`, and deploy the changes.

```bash
fly deploy
```

![fly deploy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.22.37.png)
_Output of fly deploy_

Once this is successful, the changes to the **fly.toml** file will be on the remote configuration.

## **How to Destroy the Old Machine**

You have successfully moved your machine and attached volume to a new region and since we no longer need the machine in the old region `lhr`, you will have to clean it up. The first approach is to stop the machine using the ID.

### Stop the Old Machine

```bash
fly machine stop <old_machine_id>
```

![fly machine stop](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.23.39.png)
_Output of fly machine stop_

To confirm if it was successful, use:

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.11.png)
_Output of fly machine list_

The state of the machine has been updated to `stopped`

### Destroy the Old Machine

```bash
fly machine destroy <old_machine_id>
```

![fly machine destroy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.35.png)
_Output of fly machine destroy_

Run the below command to verify if the machine still exists.

```bash
fly machine list
```

![fly machine list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.24.59.png)
_Output of fly machine list_

The machine in the old region has been successfully deleted.

## **How to Destroy the Unattached Volume**

After successfully destroying the Machine, the volume attached to it is now unattached and can also be destroyed.

```bash
fly volumes list
```

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.25.24.png)
_Output of fly volumes list_

Use the ID of the unattached volume and run the below command:

```bash
fly volumes destroy <old_volume_id>
```

![fly volumes destroy](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.26.04.png)
_Output of fly volumes destroy_

The unattached volume has now been destroyed.

![fly volumes list](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-15-at-20.26.27.png)
_Output of fly volumes list_

Only one volume exists and is attached to a machine in the new region.

## **How to Check the State of the Instance**

Check the logs to see the state of the instance:

```bash
fly logs
```

The logs show the application is running without any issues.

## **Conclusion**

Moving a Fly.io application to a new region involves forking the existing volume, cloning the existing machine with the forked volume to a new region, updating **fly.toml**, deploying the changes, and removing the old machine and volume. 

Following these guidelines ensures a smooth and successful transition with minimal disruption.

 If you have any questions you can always find me on [X (formerly Twitter)](https://x.com/X8inez)

## **Resources**:

* [Fly Docs](https://fly.io/docs)
* [Flyctl](https://fly.io/docs/flyctl)
* [Fly Machines](https://fly.io/docs/machines/overview/)
* [Fly Volumes](https://fly.io/docs/volumes/overview/)
* [Fly regions](https://fly.io/docs/reference/regions/)

