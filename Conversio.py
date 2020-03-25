from PIL import Image, ImageOps
import wave, math, array, sys, timeit

from kivy import platform


def last():
    for i in range(9999, 0, -1):
        if platform == "linux" or platform == "windows":
            if i >= 1000:
                var = "Screenshot%d.png" %(i)
                try:
                    with open("%s" %(var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 100 <= i < 1000:
                var = "Screenshot0%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 10 <= i < 100:
                var = "Screenshot00%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if i < 10:
                var = "Screenshot000%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
        else:
            if i >= 1000:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 100 <= i < 1000:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot0%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if 10 <= i < 100:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot00%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass
            if i < 10:
                var = "/storage/emulated/0/Pictures/Screenshots/Screenshot000%d.png" % (i)
                try:
                    with open("%s" % (var), 'r') as file:
                        return str(var)
                except:
                    pass

def parser():


    minfreq = 2
    maxfreq = 10
    wavrate = 1000
    pxs     = 30
    output  = "%s.wav" %(last()[:14])
    rotate  = False
    invert  = False

    """print('Input file: %s.' % last())
    print('Frequency range: %d - %d.' % (minfreq, maxfreq))
    print('Pixels per second: %d.' % pxs)
    print('Sampling rate: %d.' % wavrate)
    print('Rotate Image: %s.' % ('yes' if rotate else 'no'))"""

    return (last(), output, minfreq, maxfreq, pxs, wavrate, rotate, invert)

def convert(inpt, output, minfreq, maxfreq, pxs, wavrate, rotate, invert):
    img = Image.open(inpt).convert('L')

    # rotate image if requested
    if rotate:
      img = img.rotate(90)

    # invert image if requested
    if invert:
      img = ImageOps.invert(img)

    output = wave.open(output, 'w')
    output.setparams((1, 2, wavrate, 0, 'NONE', 'not compressed'))

    freqrange = maxfreq - minfreq
    interval = freqrange / img.size[1]

    fpx = wavrate // pxs
    data = array.array('h')

    tm = timeit.default_timer()

    for x in range(img.size[0]):
        row = []
        for y in range(img.size[1]):
            yinv = img.size[1] - y - 1
            amp = img.getpixel((x,y))
            if (amp > 0):
                row.append( genwave(yinv * interval + minfreq, amp, fpx, wavrate) )

        for i in range(fpx):
            for j in row:
                try:
                    data[i + x * fpx] += j[i]
                except(IndexError):
                    data.insert(i + x * fpx, j[i])
                except(OverflowError):
                    if j[i] > 0:
                      data[i + x * fpx] = 32767
                    else:
                      data[i + x * fpx] = -32768

        prog = sys.stdout.write("Conversion progress: %d%%   \r" % (float(x) / img.size[0]*100) )
        sys.stdout.flush()

    output.writeframes(data.tobytes())
    output.close()

    tms = timeit.default_timer()

    print("Conversion progress: 100%")
    print("Success. Completed in %d seconds." % int(tms-tm))

def genwave(frequency, amplitude, samples, samplerate):
    cycles = samples * frequency / samplerate
    a = []
    for i in range(samples):
        x = math.sin(float(cycles) * 2 * math.pi * i / float(samples)) * float(amplitude)
        a.append(int(math.floor(x)))
    return a

def exec():
    inpt = parser()
    convert(*inpt)
