from myiqapi.stable_api import IQ_Option
import time
myiq=IQ_Option("email","pass")
Money=1
ACTIVES="EURUSD"
ACTION="call"#or "put"
expirations_mode=1

check,id=myiq.buy(Money,ACTIVES,ACTION,expirations_mode)