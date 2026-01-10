---
title: How to Fine-Tune the Donut Model – With Example Use Case
subtitle: ''
author: Eivind Kjosbakken
co_authors: []
series: null
date: '2023-09-12T17:59:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-fine-tune-the-donut-model
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/undraw_Dashboard_re_3b76-4.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: null
seo_desc: "The Donut model in Python is a model you can use to extract text from a\
  \ given image. This can be useful in various scenarios, like scanning receipts,\
  \ for example. \nYou can easily download the Donut model from GitHub. But as is\
  \ common with AI models, ..."
---

The Donut model in Python is a model you can use to extract text from a given image. This can be useful in various scenarios, like scanning receipts, for example. 

You can easily download the [Donut model from GitHub](https://github.com/clovaai/donut). But as is common with AI models, you should fine-tune the model for your specific needs. 

I wrote this tutorial because I did not find any resources showing me exactly how to fine-tune the Donut model with my dataset. So I had to learn this from other tutorials (which I'll share throughout this guide) and figure out issues myself. 

These issues were especially prevalent as I did not have a GPU on my local computer So to simplify the process for others, I made this tutorial.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img1.png)
_Extract information from receipts. The picture was taken from [this Google Colab file](https://colab.research.google.com/drive/1NMSqoIZ_l39wyRD7yVjw2FIuU2aglzJi?usp=sharing#scrollTo=f7RoSOEXUa6i" rel="noopener) using a photo taken by me_

### Here's what we'll cover:

* How to find a dataset to fine-tune with
* Fine-tuning with Google Colab
* How to change parameters
* Fine-tuning locally

## How to Find a Dataset to Fine-tune with

### Finding a dataset online

To fine-tune the model, we need a dataset we will fine-tune with. If you want a simple solution, you can find a prepared dataset in [this folder on Google Drive.](https://drive.google.com/drive/folders/1orOj76DW2o-w3Dnati2CKAlXauH8STpT?usp=sharing) 

You should then copy this dataset over to your own Google Drive. Note that this was taken from [this tutorial](https://towardsdatascience.com/ocr-free-document-understanding-with-donut-1acfbdf099be) under the “Downloading and parsing SROIE” headline. The tutorial is a great read which inspired this article, as I wanted to create a more in-depth tutorial for fine-tuning the Donut model in Google Colab. So if you want a more in-depth look at generating the dataset, I recommend reading the tutorial above.

The dataset linked above may not necessarily be for your specific purpose. If you want to fine-tune a model to your specific needs, you either need to find a fitting dataset online, or create a dataset yourself.

### Annotating your own dataset

This is another option if you can't or don't want to find a dataset online (so if you did that, you can ignore this subsection). 

Annotating your own dataset is a surefire way to create a dataset that perfectly fits your needs. 

There are many annotating tools online, but a free one I recommend is the [Sparrow UI data annotation tool](https://github.com/katanaml/sparrow). Here you can upload your image, put bounding boxes on the image, and label each bounding box. You can then extract the labeled data in JSON format, and use it following the rest of the tutorial. 

Make sure your dataset is in the same format as the [dataset I provided earlier](https://drive.google.com/drive/folders/1orOj76DW2o-w3Dnati2CKAlXauH8STpT). For more details on annotating data with the Sparrow UI, you can check out [my article on using the Donut model for self-annotated data](https://medium.com/python-in-plain-english/empower-your-donut-model-for-receipts-with-self-annotated-data-51fc882b7229). Note that this article assumes you are already able to finetune the Donut model (which you will learn in this article).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img2.png)
_Annotating a receipt with the Sparrow UI data annotation tool_

## Fine-Tuning with Google Colab

To make the fine-tuning process as simple as possible, I provided a [Google Colab file you can use here](https://colab.research.google.com/drive/1-qfztYjDrFecOWdqyANtI23HV06xhDRE?usp=sharing). (Some code is taken from [this GitHub page](https://github.com/NielsRogge/Transformers-Tutorials)). 

Note that package versions need to be exactly as provided in the Drive, as wrong package versions were the root of a lot of the problems I faced fine-tuning the Donut model myself.

Before fine-tuning using the Google Colab file, there are 2 things you need to do:

### Upload data to your Google Drive.

Upload the [dataset I provided earlier](https://drive.google.com/file/d/1WsWLVZhKLb8A0uCJ7Jpk8F5pCNDNsGbH/view?usp=sharing) to your Google Drive under a parent folder called _preparedFinetuneData_ (see the file structure in the image below). 

Make sure to add the parent folder in the root folder for your Google Drive. Also, download [this config file](https://drive.google.com/file/d/1WsWLVZhKLb8A0uCJ7Jpk8F5pCNDNsGbH/view?usp=sharing) and add it to the root folder of your Google Drive.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img.png)
_How your dataset should look in the root folder of Google Drive_

### Link your Google Drive to your Google Colab.

When you run the cell which mounts the Google Drive, you might get a prompt, in which case you can just accept it and ignore the rest of this paragraph. 

If you do not get a prompt, press the files icon (red in the image below), and the Mount Drive Icon (blue in the image below). Then you will get a code snippet that you can run, and now your Google Drive is connected. 

Note that if you have not connected Google Colab to Google Drive before, you have to log into your Google Drive after pressing the Drive icon, and give permission for Colab to access Drive (prompts for this should appear automatically when you try to link the Drive)

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img3.png)
_Files icon (red). Mount Google Drive (blue)_

Finally, **restart your runtime**. After altering files on Google Colab, you always have to restart your runtime to see the latest updates.

## How to Change Parameters

Great! Now you can run the cells in the notebook, and you should receive a fine-tuned model. Remember you can also change the Config parameters to, for example, train for longer, use more workers, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/img6.png)
_Example of Config parameters you can change._

Note that I am working with the Donut model fine-tuned on the [CORD dataset](https://github.com/clovaai/cord), as I want to be able to read receipts. You can also find other Donut models [here](https://github.com/clovaai/donut), with the other options being document parsing, document classification, or document visual question answering (DocVQA).

## Fine-tuning Locally

Fine-tuning can also be run locally, which will be mostly relevant for you if you have a GPU, as CPU training will take a long time. 

To run locally you have to:

1. First, clone [this GitHub repository](https://github.com/clovaai/donut)
2. Add the prepared fine-tuning dataset to the root folder.
3. If you want to save the fine-tuned model, add the line below to train.py line 164, right below _trainer.fit(…)_

```py
#...
trainer.save_checkpoint(f"{Path(config.result_path)}/{config.exp_name}/{config.exp_version}/model_checkpoint.ckpt")
#...
```

4.  You then need to comment out GPU processes in the PyTorch Lightning Trainer, and add the line: _accelerator=”cpu”_:

```py
#train.py file
#... 
trainer = pl.Trainer(
        #Comment out the lines above
        # num_nodes=config.get("num_nodes", 1),
        # devices=torch.cuda.device_count(),
        # strategy="dp",
        # accelerator="gpu",
        accelerator="cpu", #TODO add this line
        plugins=custom_ckpt,
        max_epochs=config.max_epochs,
        max_steps=config.max_steps,
        val_check_interval=config.val_check_interval,
        check_val_every_n_epoch=config.check_val_every_n_epoch,
        gradient_clip_val=config.gradient_clip_val,
        precision=16,
        num_sanity_val_steps=0,
        logger=logger,
        callbacks=[lr_callback, checkpoint_callback, bar],
    )
#...
```

5.  Make sure the max_epochs parameter in your Config file is set to -1 (if not you will get a division by 0 error). You can decide training time by setting the parameter _max_steps_.

6.  You can then run fine-tuning can then be run with the following command in the terminal:

```bash
python train.py --config config/train_cord.yaml
```

Where _train_cord.yaml_ is the Configuration file you want to use.

### Running on CPU

If you are running on CPU after all, you will encounter some problems unless you make some changes:

1. donut/train.py, change the _accelerator_ parameter to “cpu” (from “gpu”), and remove the parameters: _num_nodes_, _devices_, and _strategy_).
2. Then in your Config file (for example _train_cord.yaml_), set _max_epochs_ to -1, and then specify the parameter _max_steps_. This is because you will encounter a division by 0 error if you have _max_epoch_ larger than 0

After these changes, running on a CPU should work as well.

## Conclusion

In this article, I have shown you how to easily fine-tune the Donut model using your own data, something which will hopefully result in improved accuracy for your fine-tuned Donut model. 

The applicabilities of the Donut model are many, and this is just one way to use it, which I hope is useful.

If you are interested and want to learn more about similar topics, you can find me on:

* [✅ Medium](https://medium.com/@oieivind)
* [✅](https://twitter.com/Ravenspike21) [Twitter](https://twitter.com/Ravenspike21)

