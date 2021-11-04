from ppadb.client import Client
import numpy
import time
from mss import mss

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()


if len(devices) == 0:
    print('No device attached')
    quit()


device = devices[0]


A = {'left': 490, 'top': 190, 'width': 1, 'height': 1}
B = {'left': 680, 'top': 190, 'width': 1, 'height': 1}
C = {'left': 890, 'top': 190, 'width': 1, 'height': 1}
D = {'left': 1085, 'top': 190, 'width': 1, 'height': 1}

E = {'left': 690, 'top': 315, 'width': 1, 'height': 1}
F = {'left': 790, 'top': 315, 'width': 1, 'height': 1}
G = {'left': 980, 'top': 315, 'width': 1, 'height': 1}
H = {'left': 1180, 'top': 315, 'width': 1, 'height': 1}

I = {'left': 490, 'top': 410, 'width': 1, 'height': 1}
J = {'left': 680, 'top': 410, 'width': 1, 'height': 1}
K = {'left': 890, 'top': 410, 'width': 1, 'height': 1}
L = {'left': 1085, 'top': 410, 'width': 1, 'height': 1}


sct = mss()

A_pixel = numpy.array(sct.grab(A))
B_pixel = numpy.array(sct.grab(B))
C_pixel = numpy.array(sct.grab(C))
D_pixel = numpy.array(sct.grab(D))

E_pixel = numpy.array(sct.grab(E))
F_pixel = numpy.array(sct.grab(F))
G_pixel = numpy.array(sct.grab(G))
H_pixel = numpy.array(sct.grab(H))

I_pixel = numpy.array(sct.grab(I))
J_pixel = numpy.array(sct.grab(J))
K_pixel = numpy.array(sct.grab(K))
L_pixel = numpy.array(sct.grab(L))

print(A_pixel, B_pixel, C_pixel, D_pixel, E_pixel, F_pixel,
      G_pixel, H_pixel, I_pixel, I_pixel, K_pixel, L_pixel)

teste = 1500


class BotPVU:
    def ConfiguracoesSom(self):
        device.shell(f'input touchscreen tap {int(teste)} 540')
        time.sleep(1)
        device.shell(f'input touchscreen tap 820 592')

    def IniciarNormal(self):
        time.sleep(1)
        device.shell(f'input touchscreen tap 1395 340')

    def Recomecar(self):
        time.sleep(1)
        device.shell(f'input touchscreen tap 1440 620')

    def abrirQuantidadeP(self):
        time.sleep(1)
        device.shell(f'input touchscreen tap 220 640')

    def UparPlanta(self):
        time.sleep(1)
        device.shell(f'input touchscreen tap 1400 640')


bot = BotPVU()
# bot.IniciarNormal()
