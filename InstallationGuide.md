Installation Guide

Install Homebrew Package Manager (Paste the mentioned command in a terminal window)
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Get CUDA 7.0
Install CUDA 7.0 (for OSX) from http://api.viglink.com/api/click?format=go&jsonp=vglnk_1469004594828107&key=3755fbf465dcd24d7f23d703cb98f0bd&libId=iqujwkfz0100su4m000DL1dx1k63d1r2n3&loc=http%3A%2F%2Finstalling-caffe-the-right-way.wikidot.com%2Fstart&v=1&out=https%3A%2F%2Fdeveloper.nvidia.com%2Fcuda-downloads&title=Caffe%20Installation%20-%20Installing%20Caffe%20the%20right%20way&txt=here

We will need to edit the OpenCV installation file a bit
```
brew edit opencv
```
replace the following lines -
```
args « "-DPYTHON#{py_ver}_LIBRARY=#{py_lib}/libpython2.7.#{dylib}"
args « "-DPYTHON#{py_ver}_INCLUDE_DIR=#{py_prefix}/include/python2.7"
```
with -
```
args « "-DPYTHON_LIBRARY=#{py_prefix}/lib/libpython2.7.dylib"
args « "-DPYTHON_INCLUDE_DIR=#{py_prefix}/include/python2.7"
```

Install snappy, leveldb, gflags, glog, szip, lmdb and opencv.
```
brew install -fresh -vd snappy leveldb gflags glog szip lmdb homebrew/science/opencv
```

Install protobuf.
```
brew install -build-from-source -with-python -fresh -vd protobuf
```

Install boost libraries for python.
```
brew install -build-from-source -fresh -vd boost boost-python
```

Download Caffe
```
git clone https://github.com/BVLC/caffe.git
cd caffe
cp Makefile.config.example Makefile.config
```

Edit the Makefile.config file (see example file named 'Makefile.config'

Compile
```
make clean
make all
make test
make runtest
```

Install and configure the python interface to Caffe (PyCaffe)
```
for req in $(cat requirements.txt); do pip install $req; done
make pycaffe
```

Set PYTHONPATH in your ~/.bash_profile
```
export PYTHONPATH=<Your Caffe Home directory>/python:$PYTHONPATH
```

Finally go to the python folder inside your caffe home directory
```
cd <caffe-home>/python
```

Execute python
```
python
```
You will see something like
```
Python 2.7.11 (default, Jan 29 2016, 06:27:40)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import caffe
```

This completed the installation of caffe

