import numpy, pylab
data = numpy.memmap("signals/null.pcm", dtype='h', mode='r')
pylab.plot(data)
pylab.show()


