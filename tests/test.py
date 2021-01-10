
import numpy as np
import os

import pyspng as m

assert m.__version__ == '0.0.1'

fname = os.path.join(os.path.dirname(__file__), 'test.png')

def ref_compare(fn, spngarr):
    try:
        import PIL.Image
        img = PIL.Image.open(fn).convert('RGB')
        pil_arr = np.array(img)

        # Match that loading the same image with PIL.Image produces
        # the same bits.
        assert np.all((spngarr - pil_arr) == 0)
        print ('PIL image compare ok.')
    except:
        print ('Skipping test.  PIL.Image not installed')


with open(fname, 'rb') as fin:
    sarr = m.load_png(fin.read())
    print (sarr.shape)
    ref_compare(fname, sarr)

try:
    m.load_png(b'this is not a png')
except Exception as e:
    assert 'could not decode image size' in str(e)

print ('All tests ok.')
