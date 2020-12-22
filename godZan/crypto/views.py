import binascii


from django.http import HttpResponse
#above all is useless
import urllib.request
from django.shortcuts import render_to_response, render, redirect
from cryptoFunction import ntru_moudle
import json
import numpy as np
import logging
import math




# ntru算法
def ntru(request):
    if request.method=='POST':
        type1 = request.POST['type']
        input = str.encode(request.POST['input'])
        if type1 == 'en':
            input_arr = np.unpackbits(np.frombuffer(input, dtype=np.uint8))
            input_arr = np.trim_zeros(input_arr, 'b')  
            output = ntru_moudle.encrypt("myKey.pub.npz", input_arr, bin_output=True, block=True)
            output = np.packbits(np.array(output).astype(np.int)).tobytes()
            with open('encry_test.txt', 'wb') as file:
                file.write(output)
            return HttpResponse(output)
        if type1 == 'de':
            with open('encry_test.txt', 'rb') as file:
                input  = file.read()
            input_arr = np.unpackbits(np.frombuffer(input, dtype=np.uint8))
            input_arr = np.trim_zeros(input_arr, 'b')
            output = ntru_moudle.decrypt("myKey.priv.npz", input_arr, bin_input=True, block=True)
            output = np.packbits(np.array(output).astype(np.int)).tobytes()
            return HttpResponse(output)
    else:
        return render(request, 'ntru.html',{'output':"",'input':''})    

def gen(request):
    if request.method == 'POST':
        N = int(request.POST['N'])
        q = int(request.POST['q'])
        p = int(request.POST['p'])
        h, f, f_p, g, f_q = ntru_moudle.generate(N, p, q, "myKey.priv", "myKey.pub")
        resp = {'h': str(h), 'f':str(f), 'f_p':str(f_p), 'g':str(g), 'f_q':str(f_q)}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return render(request, 'gen.html', {'output':"",'input':''})