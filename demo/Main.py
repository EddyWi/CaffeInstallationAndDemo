import caffe
import matplotlib.pyplot as pyplot
import os

# Set display defaults
pyplot.rcParams['figure.figsize'] = (10, 10)        # large images
pyplot.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
pyplot.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a color heatmap

# Check if CaffeNet is present
caffeRoot = '/usr/local/caffe/'
if os.path.isfile(caffeRoot + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'):
    print 'CaffeNet found.'
else:
    quit()







