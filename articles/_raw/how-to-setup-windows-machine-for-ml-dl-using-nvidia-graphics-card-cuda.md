---
title: How to Setup a Windows Machine for Machine Learning/Deep Learning Using an
  Nvidia Graphics Card (CUDA)
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-05-30T14:58:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-windows-machine-for-ml-dl-using-nvidia-graphics-card-cuda
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/arseny-togulev-MECKPoKJYjM-unsplash.jpg
tags:
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Windows
  slug: windows
- name: WSL
  slug: wsl
seo_title: null
seo_desc: "If you are learning machine learning / deep learning, you may be using\
  \ the free Google Colab. But you might wonder if the free version is adequate. \n\
  If you can afford a good Nvidia Graphics Card (with a decent amount of CUDA cores)\
  \ then you can easil..."
---

If you are learning machine learning / deep learning, you may be using the free [Google Colab](https://colab.research.google.com/). But you might wonder if the free version is adequate. 

If you can afford a good Nvidia Graphics Card (with a decent amount of CUDA cores) then you can easily use your graphics card for this type of intensive work. 

A lot of developers use Linux for this. But, I do not like Linux as a desktop operating system (do not get offended, as it is my personal preference. And yes, Linux is the best for server-related stuff). 

Also, if you own the latest Nvidia GPU, then you're probably already familiar with the hassle regarding the graphics driver and so on.

For all these reasons, I was thinking about trying something different: utilizing the new Windows 11 operating system to use the CUDA cores from my Graphics Card. 

I followed a lot of videos but couldn't implement it after trying many times, unfortunately. There was some gap in the latest version of PyTorch with the Windows 11 kernel in CUDA. Still, after researching a lot, I have found out that WSL2 should work just fine.

After trying for more than a few days, I have successfully managed to set up everything necessary and can use my graphics card's CUDA cores in my Windows machine! An interesting thing is, in this process, you do not need to download or use Microsoft Visual Studio 2022 and download huge 30/35GB files just to install the recommended compilers and so on.

Because of this, I wrote a complete handbook on my GitHub (here's the repo: [CUDA-WSL2-Ubuntu](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu), and here's the website: [fahimfba.github.io/CUDA-WSL2-Ubuntu](https://fahimfba.github.io/CUDA-WSL2-Ubuntu)).

I am writing the same handbook here as well. So, here we go! 🎉

## My Computer Specification

For this guide, I have used my Desktop workstation. If you are also interested in the current specification that I used for this task, here you go:

* Processor: Ryzen 5 3500X 6 Core and 6 Threads
* RAM: 32GB DDR4 3200MHz (16 GB + 8 GB + 8 GB)
* GPU: Zotac Nvidia GeForce RTX 3050 8GB GDDR6
* Motherboard: Gigabyte B450M Aorus Elite
* Storage: Gigabyte 240GB SATA SSD
* Monitor: MSI Optix G24 Gaming Curved 75Hz

I will be using Windows 11 Pro (Version 22H2) and WSL2 (of course!).

## Step 1: Make Sure You Have Solid Internet and Electricity

This whole process can take a lot of time. So make sure you're properly connected to the internet and have consistent electricity. For me, it took almost 7 hours in total. You will also need to download some pretty huge packages along the way. 

Also, make sure that you have installed the latest Nvidia driver after downloading the official driver from [the official website of Nvidia](https://www.nvidia.com/download/index.aspx). Make sure that you have installed all the updates of your Windows 11.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/win_update.png)
_windows update_

## St**ep 2: Download Latest PowerShell**

I will be using the latest PowerShell. You can download that from the Microsoft store, but I will download it from the official website as the store might create some problems later. 

Go to [the official website](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows). This normally redirects you to the latest version of PowerShell available at that moment. For me, the latest version is 7.3 (24 May 2023). For you, it might be the updated version. Don't worry about that. Simply download the latest stable version.

1. Click on the **Download PowerShell** button.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/1-1.png)
_Download Powershell button_

2.  Find the latest PowerShell of `win-x64.msi`. Download that.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/2-3.png)
_latest PowerShell msi file_

3.  The installation process is pretty straightforward. But I will be guiding you throughout the entire process. Double click on the downloaded file. Then click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/3-2.png)
_msi software_

4.  Keep everything as it is and click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/4-3.png)
_Next step_

5.  I still prefer to keep everything as it is and simply click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/5-4.png)
_Next step_

6.  I still prefer to keep everything as it is and simply click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/6-1.png)
_Next step_

7.  Click `Install`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/7-2.png)
_Install_

8.  Now click `Finish`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/8-3.png)
_Finish_

## Step 3: Check Your Windows Terminal

I really like the Windows Terminal, as I can simply switch to any other WSL OSes (Ubuntu, Kali, Git Bash, and so on) whenever I want. But before proceeding further, I have to make sure that my current Windows Terminal is the updated one.

1. Open the **Microsoft Store** and search for `Windows Terminal`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/9-2.png)
_Windows Terminal on Microsoft Store_

2.  Click on `Update` if it needs an update.

3.  Make sure that you are on the latest updated Windows Terminal already.

4.  Now open the Windows Terminal, because we have to change some settings first. Click on `Open Settings`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/10-2.png)
_Windows Terminal Settings Customization_

5.  If you do not see the `Open Settings` prompt, then simply click the drop-down arrow, and click on `Settings`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/11-2.png)
_Settings_

6.  From `Startup`, make sure that the **Default profile** is set on `PowerShell` (the new PowerShell we installed in Step 2). The `Default terminal application` should be set on `Windows Terminal`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/12-1.png)
_Default startup config_

7.  Then click `Save` and exit the terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/13-2.png)
_Save_

## Step 4: Hardware Virtualization

In order to use WSL, we have to make sure that our CPU virtualization is enabled. You can check the status through your task manager. If it is disabled, then make sure to enable the virtualization through BIOS. 

You will find a lot of YouTube videos about this, but make sure that you are following the correct one that matches your motherboard brand and model.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/14-2.png)
_Virtualization_

## Step 5: Install WSL and Ubuntu LTS

Now we need to install the WSL2 and Ubuntu LTS.

1. Open the Windows Terminal as an **Administrator**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/15-2.png)
_Open terminal as an administrator_

2.  For installing **WSL**, use the command `wsl --install`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/16-3.png)
_VMP install_

3.  Then, it would automatically install the latest LTS version of Ubuntu.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/18-2.png)
_Ubuntu install_

4.  After the tasks get finished, it will prompt you for rebooting your PC. Save other work and simply restart your computer.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/19-3.png)
_Reboot PC_

5.  After restarting the PC, it would automatically open the terminal and ask you for the username and password for your Linux OS.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/20-1.png)
_After rebooting PC_

6.  Give the Username and Password. Make sure to use the same Password on Retype Password!

![Image](https://www.freecodecamp.org/news/content/images/2023/05/21-1.png)
_username and password_

7.  After a while, it will install the necessary components.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/22-1.png)
_Complete Ubuntu_

8.  Now, make sure that **WSL2** becomes the default WSL in this terminal. Apply the command, `wsl --set-default-version 2`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/23-1.png)
_WSL 2 default_

9.  If you want to check the WSL OSes status (how many OSes are available, how many of them are running or stopped), use the command, `wsl --list --verbose`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/24-1.png)
_OSes status_

Here, it is telling me that I have **Ubuntu** installed on my WSL version 2 and it is currently stopped.

10.  However, after working on a WSL OS, if you want to shut down the OS, then you can use the command `wsl -t distro_name`. For me, it is Ubuntu, so I used `wsl -t Ubuntu`. `t` represents the **termination** command here.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/25-2.png)
_Terminate command_

11.  If you have multiple OSes in WSL, and if you want to run any specific distribution, then use the command `wsl --distribution distribution_name`. For example, if I want to run Ubuntu specifically, the command would be `wsl --distribution Ubuntu`. If you only have one distribution, then you do not necessarily need to worry about this at all.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/26-1.png)
_run specific distro_

12.  You can simply use `exit` to exit a distro from the terminal. It might not necessarily shut down the distribution. You can specifically use the termination command for that. But some regularly used commands are here.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/27-1.png)
_regularly used command_

13.  After installing a distribution, you would also be able to see and go there by using the drop-down menu from the Windows Terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/28-1.png)
_the drop-down menu for other distributions_

## Step 6: Configure Ubuntu LTS

We need to update and install some apps now.

1. Open Ubuntu by using any method inside the Windows Terminal. You can obviously use the dedicated **Ubuntu App**. But I always prefer the Terminal as I can use multiple different distributions and command line applications here altogether.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/29.png)
_start Ubuntu_

2.  Update the system by using the command `sudo apt update`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/30.png)
_update_

3.  If you get errors in updating/upgrading saying it can't reach the server then change the nameserver with the command `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null`.

4.  After updating, upgrade the system using `sudo apt upgrade`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/31.png)
_Upgrade_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/32.png)
_Upgrade system_

You can clear the terminal by using the `clear` command.

5.  CUDA works with C. So we need to install the gcc compiler first. Use the command `sudo apt install gcc --fix-missing`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/33.png)
_gcc_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/34.png)
_gcc installing_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/35.png)
_finishing installation_

## Step 7: Install CUDA

Now it is time to install CUDA from the [official website of Nvidia](https://developer.nvidia.com/cuda-downloads).

Make sure to select the following:

* **Operating System**: Linux <br>
* **Architecture**: x86_64 <br>
* **Distribution**: WSL-Ubuntu <br>
* **Version**: 2.0 <br>
* **Installer Type**: deb(local) <br> 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/36.png)
_Nvidia - CUDA_

This will provide the necessary commands.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/37.png)
_commands CUDA_

Now your task is to apply each command serially in the WSL Ubuntu terminal. Make sure to use the first command twice. It normally resolves the problem of keyring later.

Also, keep in mind that these commands might get changed later. So always follow the official website. For this guideline, I will be using the exact command I used to set up the CUDA in my machine.

1. `wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/38.png)
_1st command_

I used the same command again after finishing the previous transactions.

2.  `wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/39.png)
_1st command_

3.  `sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/40.png)
_2nd Command_

4.  `wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/41.png)
_3rd command_

This normally takes a lot of time as it downloads a large file (above 2GB file size).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/42.png)
_large file_

5.  `sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/43.png)
_4th command_

6.  `sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/44.png)
_5th command_

7.  Then update the system using `sudo apt-get update`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/45.png)
_update system_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/46.png)
_updating_

8.  `sudo apt-get -y install cuda`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/47.png)
_install CUDA_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/48.png)
_finish CUDA installation_

## Step 8: Post Installation

The [official CUDA installation guide from Nvidia](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) tells us to add `export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}` to the **PATH** variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/49.png)
_path_

I have changed the CUDA version `cuda-12.1` according to my installed CUDA version. Make sure to do the same for your updated CUDA version.

Do the following to do that:

1. Open Ubuntu in the Windows Terminal.
2. Go to the root directory using `cd ~`. Then open the `bashrc` in nano using `nano .bashrc`

![Image](https://www.freecodecamp.org/news/content/images/2023/05/50.png)
_root_

3.  Go to the end of the file and copy-paste the path there. For me, the path is `export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/51.png)
_path_

Then use `Ctrl` + `X` to close. Make sure to use `Y` to save in the same file.

4.  To apply the changes, use `source ~/.bashrc`. You can check the path using `echo $PATH`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/52.png)
_path check_

## Step 9: Nvidia CUDA Toolkit

Install the Nvidia Cuda Toolkit using `sudo apt install nvidia-cuda-toolkit`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/53.png)
_toolkit 1_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/54.png)
_toolkit 2_

You can check the Driver and CUDA versions using `nvidia-smi`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/55.png)
_smi_

Also, make sure to check whether the Nvidia Cuda Compiler Driver has been installed or not by using `nvcc -V`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/56.png)
_nvcc_

## Step 9: Confirm that Python is Installed

Now, make sure that you have Python 3 installed in your system. You can check the version using `python3 --version`. If that says that "python3 is not found" or something like that, then install Python.

Install **PIP** using `sudo apt-get install python3-pip`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/57.png)
_pip install_

## Step 10: Install PyTorch

For installing PyTorch, go to [the official website of PyTorch](https://pytorch.org/get-started/locally/). Then make sure to select the relevant sections. After that, it will provide you with a command. You have to use the command in your Ubuntu terminal.

For me, the selections were:

* PyTorch Build: Stable (2.0.1) - Make sure to select the latest stable version always
* Your OS: Linux
* Package: Pip
* Language: Python
* Computer Platform: CUDA 11.8 - Make sure to select the latest available CUDA version

After that, I got the command `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/58.png)
_PyTorch command_

I simply used that exact command in my Ubuntu terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/59.png)
_PyTorch command_

It also downloads a large file that can take a lot of time if you have a slower internet connection like I do!

![Image](https://www.freecodecamp.org/news/content/images/2023/05/60.png)
_PyTorch download_

## Step 11: CUDA Availability

You can directly check whether your CUDA has been installed or not by running two lines of Python code in the terminal.

* Run Python in the terminal using `python3`.
* Import torch using `import torch`.
* Check the CUDA availability using `torch.cuda.is_available()`.

If it returns `True`, then you have successfully finished installing CUDA on your system!

![Image](https://www.freecodecamp.org/news/content/images/2023/05/61.png)
_cuda yes_

## Step 12: Nvidia Developer Settings

You have to enable the Nvidia Developer Settings for using CUDA via WSL. Simply follow this process:

1. Open the **Nvidia Control Panel**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/62.png)
_Nvidia control panel_

2.  Click "Agree and Continue".

![Image](https://www.freecodecamp.org/news/content/images/2023/05/63.png)
_agree_

3.  In the Nvidia Control Panel, Click Desktop > Enable Developer Settings. If the "Enable Developer Settings" does not have any check mark, then click on that to enable that feature.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/64.png)
_not check mark_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/65.png)
_check mark_

4.  The **Developer** section will be visible. Click on **Manage GPU Performance Counters**.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/66.png)
_GPU counters_

5.  Check the radio button on "Allow access to the GPU performance counters to all users".

![Image](https://www.freecodecamp.org/news/content/images/2023/05/67.png)
_check_

6.  Click "Apply" and "Yes" to approve the changes permanently.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/68.png)
_approve changes_

7.  At the end, it should look like this. 

![Image](https://www.freecodecamp.org/news/content/images/2023/05/69.png)
_final_

8.  You can again check the CUDA availability like earlier.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/70.png)
_cuda availability_

## Step 12: Install Jupyter Notebook

I normally prefer the Jupyter Notebook. You can install it in various ways, like `pip install notebook`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/71.png)
_notebook 1_

![Image](https://www.freecodecamp.org/news/content/images/2023/05/72.png)
_notebook 2_

But I prefer the command `pip install jupyter notebook`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/73.png)
_jupyter notebook_

To open a Jypyter Notebook, you can simply use `jupyter notebook` in the terminal.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/74.png)
_notebook cli_

The notebook will open instantly and you can use the given URL to open that in your web browser:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/75.png)
_open the notebook in the browser_

## Step 13: Run Some Tests

I ran two codes to check the performance of my CUDA.

1. Open a Python3 script in the notebook.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/76.png)
_open script_

2.  I used the following code to check whether it is using my CPU or CUDA from my GPU:

```python
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print("using", device, "device") 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/77.png)
_cuda_

3.  For the performance comparison between my CPU and GPU (CUDA), I used the following code:

```python
import time

matrix_size = 32*512

x = torch.randn(matrix_size, matrix_size)
y = torch.randn(matrix_size, matrix_size)

print("************* CPU SPEED *******************")
start = time.time()
result = torch.matmul(x, y)
print(time.time() - start)
print("verify device:", result.device)

x_gpu = x.to(device)
y_gpu = y.to(device)
torch.cuda.synchronize()

for i in range(3):
    print("************* GPU SPEED *******************")
    start = time.time()
    result_gpu = torch.matmul(x_gpu, y_gpu)
    torch.cuda.synchronize()
    print(time.time() - start)
    print("verify device:", result_gpu.device)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/78.png)
_CPU vs GPU_

I also made side by side comparisons between the [Google Colab](https://colab.research.google.com/) and my computer. You can check them as well.

| Try | Google Colab                                                                               | My Computer                                                                               |
| --- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| 1   | [Google Colab](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/GoogleCollab1.ipynb) | [My PC](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/CUDA%20_TEST_Fahim1.ipynb) |
| 2   | [Google Colab](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/GoogleCollab2.ipynb) | [My PC](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu/blob/main/CUDA%20_TEST_Fahim2.ipynb) |


The result already states that my PC is working better than the Google Colab.

## Step 14: Remove the CUDA Deb File

If you think that you do not need the CUDA deb file anymore, then you can remove that using the following command:

```bash
rm filename
```

For me it was this:

```bash
rm cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb
```

It does not remove the CUDA from your system. It just removes the deb file from your system.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/79.png)
_remove deb_

## Conclusion

I hope that you have successfully installed CUDA on your Windows 11 system using WSL2. If you have any questions, feel free to reach out to me using [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Also, make sure to follow me on [GitHub](https://github.com/FahimFBA) and star (⭐) the [repository](https://github.com/FahimFBA/CUDA-WSL2-Ubuntu)!

You can also [subscribe to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) for more helpful video content.

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

Thank you for reading the entire article till now. Have a great day! 😊

Cover image: Photo by [Arseny Togulev](https://unsplash.com/@tetrakiss?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/MECKPoKJYjM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

