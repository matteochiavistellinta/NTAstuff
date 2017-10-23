| Codice   |      Descrizione      |
|-----------------|---------------------------:|
| import RPi.GPIO as GPIO |  In questa prima riga Python sa che deve usare una 'libreria' e che ogni riferimento futuro ai suoi comandi possono essere richiamati con un determinato nome. Questa libreria in particolare abilita le GPIO della Raspi. Una ‘libreria’ dà a un linguaggio di programmazione degli extra poteri "comandi" che servono a creare qualcosa di differente. |
| import time	| Importiamo un'altra libreria che ci permetterà di gestire il tempo nel nostro progetto.|
|GPIO.setmode(GPIO.BCM)|	Ogni pin sulla Raspi ha un nome univoco, e in questo modo diciamo al programma di abilitare il naming dei pin.|
|GPIO.setwarnings(False)|	Questo dice a Python di non stampare a monitor gli eventuali messaggi di errori legati alle GPIO.|
|GPIO.setup(18,GPIO.OUT)|	Questa linea dice all'Interprete di Python che il pin 18 sarà usato come OUTPUT.|
|print "LED on"|	Questa linea scrive sul terminale "LED on".|
|GPIO.output(18,GPIO.HIGH)|	Questa riga invece manda effettivamente 3.3v al pin 18, quindi accende il LED e se non abbiamo messo una resistenza, a volte lo brucia.|
|time.sleep(1)|	Il programma va in pausa per 1 secondo.|
|print "LED off"|	Questa linea scrive sul terminale "LED off".|
|GPIO.output(18,GPIO.LOW)|	Al pin 18 non arriver'pi\ corrente.|
