---
title: How to Validate your Machine Learning Models Using TensorFlow Model Analysis
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-10-05T14:37:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-machine-learning-models-with-tensorflow-model-analysis
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-159275.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
- name: Validation
  slug: validation
seo_title: null
seo_desc: "My first deployed Machine Learning model was a failure. It was a simple\
  \ Diabetes Diagnosis Model for potential diabetes mellitus patients – and quite\
  \ frankly, I was beyond excited on deployment. \nBut the excitement soon disappeared\
  \ when I received fe..."
---

My first deployed Machine Learning model was a failure. It was a simple Diabetes Diagnosis Model for potential diabetes mellitus patients – and quite frankly, I was beyond excited on deployment. 

But the excitement soon disappeared when I received feedback from users. Simply put, the users felt the model was bad. 

I was saddened by this, but looking back, they were correct. The model may have performed well in terms of top-level metrics. But from the perspective of the consumer, if a machine learning model provides a poor forecast, that person's experience with the model will be bad. 

The issue was that specific model features, or slices of data, were causing the model to perform poorly. 

In short, before deploying any machine learning model, the onus is on machine learning engineers to assess it, make sure it satisfies strict quality standards, and acts as predicted for all pertinent slices of data.

## What is TensorFlow Model Analysis?

To enable Machine Learning engineers to look at the performance of their models at a deeper level, Google created [TensorFlow Model Analysis (TFMA)](https://www.tensorflow.org/tfx/guide/tfma). According to the docs, "TFMA performs its computations in a distributed manner over large amounts of data using Apache Beam."

TFMA, as a tool, enables you to really dig into the model's performance and understand how it varies on different slices of data. It provides support for calculating metrics that were used at training time (that is built-in metrics) as well as metrics defined after the model was saved as part of the TFMA configuration settings. 

In this tutorial, you will analyze and evaluate results on a previously trained machine learning model. The model you will use is trained for a [Chicago Taxi Example](https://github.com/tensorflow/tfx/tree/master/tfx/examples/chicago_taxi_pipeline), which uses the [Taxi Trips dataset](https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew) released by the city of Chicago. You can check out the full dataset [here](https://bigquery.cloud.google.com/dataset/bigquery-public-data:chicago_taxi_trips). 

When you are done with this tutorial, you will be able to use Apache Beam to do a full pass over the specified evaluation dataset. Also, you will not only have a more accurate calculation of metrics, but you'll be able to scale up to massive evaluation datasets, since Beam pipelines can be run using distributed processing back-ends.

## Prerequisites

* Fundamental knowledge of Apache Beam. The [Beam Programming Guide](https://beam.apache.org/documentation/programming-guide/) is a great place to start.
* Fundamental understanding of the workings of machine learning models. 
* A new Google Colab notebook to run the Python code in your Google Drive. You can set this up by following this [tutorial](https://www.freecodecamp.org/news/google-colaboratory-python-code-in-your-google-drive/).

## Step 1 – How to Install TensorFlow Model Analysis (TFMA)

With your Google Colab notebook ready, the first thing to do is to pull in all the dependencies. This will take a while.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-23.png)
_A blank (new) notebook in dark mode_

Rename the file from `Untitled.ipynb` to `TFMA.ipynb`. 

```python
!pip install -U pip
!pip install tensorflow-model-analysis`
```

The first line upgrades `pip` to the latest version. `pip` is the package management system used to install and manage software packages written in Python. It stands for “preferred installer program”. The second line will install TensorFlow Model Analysis, TFMA.  

Now, after that is done, restart the runtime before running the cells below. It is important to restart the runtime before running the cells.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-26.png)

```python
import sys
assert sys.version_info.major==3 
import tensorflow as tf
import apache_beam as beam
import tensorflow_model_analysis as tfma

```

This block of code imports the needed libraries – `sys`, `tensorflow`, `apache_beam` and `tensorflow_model_analysis`. You use the `assert sys.version_info.major==3` command to verify that the notebook is being run using Python 3. 

## Step 2 – How to Load the dataset

You will download the `tar` file and extract it.

```python
import io, os, tempfile
TAR_NAME = 'saved_models-2.2'
BASE_DIR = tempfile.mkdtemp()
DATA_DIR = os.path.join(BASE_DIR, TAR_NAME, 'data')
MODELS_DIR = os.path.join(BASE_DIR, TAR_NAME, 'models')
SCHEMA = os.path.join(BASE_DIR, TAR_NAME, 'schema.pbtxt')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

!curl -O https://storage.googleapis.com/artifacts.tfx-oss-public.appspot.com/datasets/{TAR_NAME}.tar
!tar xf {TAR_NAME}.tar
!mv {TAR_NAME} {BASE_DIR}
!rm {TAR_NAME}.tar

```

The dataset downloaded is in the `tar` file format. It includes the training datasets, evaluation datasets, the data schema and the training and serving saved models along with eval saved models. You will need all of them in this tutorial.

## Step 3 – How to Parse the Schema

You need to parse the downloaded schema so that you can use it with TFMA. 

```python
import tensorflow as tf
from google.protobuf import text_format
from tensorflow.python.lib.io import file_io
from tensorflow_metadata.proto.v0 import schema_pb2
from tensorflow.core.example import example_pb2

schema = schema_pb2.Schema()
contents = file_io.read_file_to_string(SCHEMA)
schema = text_format.Parse(contents, schema)

```

You will parse the schema using the `text_format` method of the `google.protobuf` library to convert the protobuf message to text format and TensorFlow's `schema_pb2`.

## Step 4 – How to Use the Schema to Create TFRecords 

The next course of action would be to give TFMA access to our dataset. For this, we need to create a `TFRecords` file.  We used our schema to create it, since it gives us the correct type for each feature.

```python
import csv
datafile = os.path.join(DATA_DIR, 'eval', 'data.csv')
reader = csv.DictReader(open(datafile, 'r'))
examples = []
for line in reader:
  example = example_pb2.Example()
  for feature in schema.feature:
    key = feature.name
    if feature.type == schema_pb2.FLOAT:
      example.features.feature[key].float_list.value[:] = (
          [float(line[key])] if len(line[key]) > 0 else [])
    elif feature.type == schema_pb2.INT:
      example.features.feature[key].int64_list.value[:] = (
          [int(line[key])] if len(line[key]) > 0 else [])
    elif feature.type == schema_pb2.BYTES:
      example.features.feature[key].bytes_list.value[:] = (
          [line[key].encode('utf8')] if len(line[key]) > 0 else [])
  # Add a new column 'big_tipper' that indicates if the tip was > 20% of the fare. 
  # TODO(b/157064428): Remove after label transformation is supported for Keras.
  big_tipper = float(line['tips']) > float(line['fare']) * 0.2
  example.features.feature['big_tipper'].float_list.value[:] = [big_tipper]
  examples.append(example)
tfrecord_file = os.path.join(BASE_DIR, 'train_data.rio')
with tf.io.TFRecordWriter(tfrecord_file) as writer:
  for example in examples:
    writer.write(example.SerializeToString())
!ls {tfrecord_file}

```

It is worthy of note that TFMA supports a number of different model types including TF Keras models, models based on generic TF2 signature APIs, as well TF estimator-based models. However, for this tutorial, you will configure a Keras-based model. 

In your Keras [setup](https://www.tensorflow.org/tfx/model_analysis/setup), you will add your metrics and plots manually as part of the configuration (see the [metrics](https://www.tensorflow.org/tfx/model_analysis/metrics) guide for information on the metrics and plots that are supported).

## Step 5 – How to Set Up and Run TFMA using Keras

```python
import tensorflow_model_analysis as tfma

```

You'll finally call and use the instance of `tfma` that you previously imported at this point. 

```python
# You will setup tfma.EvalConfig settings
keras_eval_config = text_format.Parse("""
  ## Model information
  model_specs {
    # For keras (and serving models) we need to add a `label_key`.
    label_key: "big_tipper"
  }

  ## You will post training metric information. These will be merged with any built-in
  ## metrics from training.
  metrics_specs {
    metrics { class_name: "ExampleCount" }
    metrics { class_name: "BinaryAccuracy" }
    metrics { class_name: "BinaryCrossentropy" }
    metrics { class_name: "AUC" }
    metrics { class_name: "AUCPrecisionRecall" }
    metrics { class_name: "Precision" }
    metrics { class_name: "Recall" }
    metrics { class_name: "MeanLabel" }
    metrics { class_name: "MeanPrediction" }
    metrics { class_name: "Calibration" }
    metrics { class_name: "CalibrationPlot" }
    metrics { class_name: "ConfusionMatrixPlot" }
    # ... add additional metrics and plots ...
  }

  ## You will slice the information
  slicing_specs {}  # overall slice
  slicing_specs {
    feature_keys: ["trip_start_hour"]
  }
  slicing_specs {
    feature_keys: ["trip_start_day"]
  }
  slicing_specs {
    feature_values: {
      key: "trip_start_month"
      value: "1"
    }
  }
  slicing_specs {
    feature_keys: ["trip_start_hour", "trip_start_day"]
  }
""", tfma.EvalConfig())

```

It's also important that you create a `tfma.EvalSharedModel` that points at the Keras model.

```python
keras_model_path = os.path.join(MODELS_DIR, 'keras', '2')
keras_eval_shared_model = tfma.default_eval_shared_model(
    eval_saved_model_path=keras_model_path,
    eval_config=keras_eval_config)

keras_output_path = os.path.join(OUTPUT_DIR, 'keras')

```

And then you finally run TFMA, ending this step.

```python
keras_eval_result = tfma.run_model_analysis(
    eval_shared_model=keras_eval_shared_model,
    eval_config=keras_eval_config,
    data_location=tfrecord_file,
    output_path=keras_output_path)

```

Now that you have run the evaluation, look at the visualizations using TFMA. For the following examples, you can visualize the results from running the evaluation on the Keras model. 

To view metrics, you will use `[tfma.view.render_slicing_metrics](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/view/render_slicing_metrics)`. By default, the views will display the `Overall` slice. To view a particular slice, you can either use the name of the column (by setting `slicing_column`) or provide a [`tfma.SlicingSpec`](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/SlicingSpec).

## Step 6 – How to Visualize the Metrics and Plots

At this point, it is important that you note that the columns used in the dataset are as follows: 

* `pickup_community_area`
* `fare`
* `trip_start_month`
* `trip_start_hour`
* `trip_start_day`
* `trip_start_timestamp`
* `pickup_latitude`
* `pickup_longitude`
* `dropoff_latitude`
* `dropoff_longitude`
* `trip_miles`
* `pickup_census_tract`
* `dropoff_census_tract`
* `payment_type`
* `company`
* `trip_seconds`
* `dropoff_community_area`, and 
* `tips` 

For a first trial and as an example, you can set `slicing_column` to look at the `trip_start_hour` feature from our previous `slicing_specs`. You are then able to visualize the column. 

```python
tfma.view.render_slicing_metrics(keras_eval_result, slicing_column='trip_start_hour')
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-27.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-28.png)

On running this, you will see that the metrics visualization supports the following interactions:

* Click and drag to pan
* Scroll to zoom
* Right click to reset the view
* Hover over the desired data point to see more details.
* Select from four different types of views using the selections at the bottom.

Note that your initial `tfma.EvalConfig` has created a whole list of `slicing_specs`, which you can visualize by updating slice information passed to `tfma.view.render_slicing_metrics`. Here you can select the `trip_start_day` slice (days of the week).

```python
tfma.view.render_slicing_metrics(keras_eval_result, slicing_column='trip_start_day')

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-29.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-31.png)

TFMA also supports creating feature crosses to analyze combinations of features. To test this, you will create a cross between `trip_start_hour` and `trip_start_day`.

```python
tfma.view.render_slicing_metrics(
    keras_eval_result,
    slicing_spec=tfma.SlicingSpec(
        feature_keys=['trip_start_hour', 'trip_start_day']))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-32.png)

Now, crossing the two columns creates a lot of combinations! But you will narrow down your cross to only look at _trips that start at 1pm_. Then, you will select `binary_accuracy` from the visualization as shown below.

```python
tfma.view.render_slicing_metrics(
    keras_eval_result,
    slicing_spec=tfma.SlicingSpec(
        feature_keys=['trip_start_day'], feature_values={'trip_start_hour': '13'}))

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-33.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-34.png)

## Step 7 – How to Track Your Model's Performance Over Time

You'll use your training dataset for training your model. It will hopefully be representative of your test dataset and the data that will be sent to your model in production.  

But while the data in inference requests may remain the same as your training data, in many cases it will start to change enough so that the performance of your model will change.

That means that you need to monitor and measure your model's performance on an ongoing basis, so that you can be aware of and react to changes.  

Let's look at how TFMA can help.

```python
output_paths = []
for i in range(3):
  # Create a tfma.EvalSharedModel that points to our saved model.
  eval_shared_model = tfma.default_eval_shared_model(
      eval_saved_model_path=os.path.join(MODELS_DIR, 'keras', str(i)),
      eval_config=keras_eval_config)

  output_path = os.path.join(OUTPUT_DIR, 'time_series', str(i))
  output_paths.append(output_path)

  # Run TFMA
  tfma.run_model_analysis(eval_shared_model=eval_shared_model,
                          eval_config=keras_eval_config,
                          data_location=tfrecord_file,
                          output_path=output_path)
  
  eval_results_from_disk = tfma.load_eval_results(output_paths[:2])

tfma.view.render_time_series(eval_results_from_disk)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-35.png)

Using the `tfma`, you can validate and evaluate your machine learning models across different slices of data. 

You can see from the image above that you can evaluate the `auc` (area under the curve), `auc_precision_recall`, `binary_accuracy`, `binary_crossentropy`, `calibration`, `example_count`, `mean_label`, `mean_prediction`, `precision`, and `recall` metrics of the machine learning model. 

## Conclusion

Finally, it is important that TFMA can be configured to evaluate multiple models at the same time. Typically, you do this to compare a new model against a baseline (such as the currently serving model) to determine what the performance differences in metrics (for example AUC) are relative to the baseline. 

When thresholds are configured, TFMA will produce a [`tfma.ValidationResult`](https://www.tensorflow.org/tfx/model_analysis/api_docs/python/tfma/ValidationResult) record indicating whether the performance matches expectations.  
  
If at this point, you have questions about the difference between evaluating machine learning models using [TensorBoard](https://www.freecodecamp.org/news/how-to-evaluate-machine-learning-models-using-tensorboard/) and TensorFlow Metrics Analysis (TFMA), this is a valid concern. Both are tools for providing the measurements and visualizations needed during the Machine Learning workflow. 

But it is important to note that you use them in different stages of the development process. At a high level, you use TensorBoard to analyze the training process itself while TFMA is concerned with the deep analysis of the 'finished' trained model.

Thank you for reading!  



