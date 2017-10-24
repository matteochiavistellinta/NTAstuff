import RPi.GPIO as GPIO #importa la librerie, e gli assegna il nome GPIO#
import time #importa anche la libreria Time, senza dargli un secondo nome#
GPIO.setmode(GPIO.BCM)#attiva i nomi dei pin#
GPIO.setwarnings(False)#disattiva i messaggi di errore di GPIO#
GPIO.setup(18,GPIO.OUT)#identifica il led 18 come output, ovvero ci deve passare la corrente#
print "LED on"#quando la corente passa per il pin 18, sul pc appare la scritta "LED on"#
GPIO.output(18,GPIO.HIGH)#questa riga manda la corrente al led#
time.sleep(1)#il programma va in pausa 1 secondo#
print "LED off"#qui appare scritto "LED of"
GPIO.output(18,GPIO.LOW)#il led non riceve più corrente#
