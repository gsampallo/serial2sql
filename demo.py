from machine import ADC
import time
adc = ADC(0)
i = 0

while(True):
    valor = adc.read()
    a = str(i)+","+str(valor)
    print(a)
    time.sleep_ms(1000)

    i = i + 1