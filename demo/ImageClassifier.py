import caffe
import matplotlib.pyplot as pyplot
import os
import numpy as np

# Function Definitions
def setDisplayDefaults():
    pyplot.rcParams['figure.figsize'] = (10, 10)  # large images
    pyplot.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
    pyplot.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a color heatmap

def isCaffeNetPresent(caffeRoot):
    if os.path.isfile(caffeRoot + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'):
        print 'CaffeNet found.'
    else:
        quit()

def loadCaffenet(caffeRoot):
    model_def = caffeRoot + 'models/bvlc_reference_caffenet/deploy.prototxt'
    model_weights = caffeRoot + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'

    net = caffe.Net(model_def,
                    model_weights,
                    caffe.TEST)
    return net

def loadMeanImagenet(caffeRoot):
    mu = np.load(caffeRoot + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
    mu = mu.mean(1).mean(1)
    print 'mean-subtracted values:', zip('BGR', mu)
    return mu

def loadTransformer(mu):
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

    transformer.set_transpose('data', (2, 0, 1))  # move image channels to outermost dimension
    transformer.set_mean('data', mu)  # subtract the dataset-mean value in each channel
    transformer.set_raw_scale('data', 255)  # rescale from [0, 1] to [0, 255]
    transformer.set_channel_swap('data', (2, 1, 0))  # swap channels from RGB to BGR

    return transformer

def loadImage():
    image = caffe.io.load_image(caffeRoot + 'examples/images/cat.jpg')
    transformedImage = transformer.preprocess('data', image)
    pyplot.imshow(image)
    pyplot.show()
    return transformedImage

def loadImageNetLabels():
    labels_file = caffeRoot + 'data/ilsvrc12/synset_words.txt'
    labels = np.loadtxt(labels_file, str, delimiter='\t')
    return labels

print "------ BEGIN PROGRAM ------"
caffeRoot = '/usr/local/caffe/'

setDisplayDefaults()
isCaffeNetPresent(caffeRoot)

caffe.set_mode_cpu()

# Load CaffeNet
net = loadCaffenet(caffeRoot)

# load the mean ImageNet image for subtraction
mu = loadMeanImagenet(caffeRoot)

# create transformer for the input called 'data'
transformer = loadTransformer(mu)

# set the size of the input
net.blobs['data'].reshape(50,        # batch size
                          3,         # 3-channel (BGR) images
                          227, 227)  # image size is 227x227

# Load an image
transformedImage = loadImage()

# copy the image data into the memory allocated for the net
net.blobs['data'].data[...] = transformedImage

# Perform classification
output = net.forward()
output_prob = output['prob'][0]
print 'predicted class is:', output_prob.argmax()

# load ImageNet labels
labels = loadImageNetLabels()
print 'output label:', labels[output_prob.argmax()]

# sort top five predictions from softmax output
top_inds = output_prob.argsort()[::-1][:5]  # reverse sort and take five largest items
print 'probabilities and labels:'
zip(output_prob[top_inds], labels[top_inds])