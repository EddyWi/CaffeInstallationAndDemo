First, download 2 datasets from the Kaggle competition page: train.zip and test1.zip (https://www.kaggle.com/c/dogs-vs-cats/data)

Prepare the data by running the commands (inside the directory where the zip files are stored)
~~~
unzip train.zip
unzip test1.zip
rm *.zip
~~~

Next, run Preprocessor.py
~~~
python Preprocessor.py
~~~

To generate the mean image of training data
~~~
/usr/local/caffe/build/tools/compute_image_mean -backend=lmdb /Users/harsh/data/train_lmdb /Users/harsh/data/mean.binaryproto
~~~

Model Definition - caffenet_train_val.prototxt

Solver Definition - solver.prototxt

Start training the model by executing the command
~~~
/usr/local/caffe/build/tools/caffe train --solver=/Users/harsh/solver.prototxt --weights /usr/local/caffe/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel 2>&1 | tee /Users/harsh/model_2_train.log
~~~

Run MakePredictions.py to making the predictions
