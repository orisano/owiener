# oWiener
[![Build Status](https://travis-ci.org/orisano/owiener.svg?branch=master)](https://travis-ci.org/orisano/owiener)
[![PyPI version](https://badge.fury.io/py/owiener.svg)](https://badge.fury.io/py/owiener)
[![Python Versions](https://img.shields.io/pypi/pyversions/owiener.svg)](https://pypi.org/project/owiener/)

A Python3 Implementation of the Wiener attack on RSA.

## Installation
```bash
python3 -m pip install owiener
```
or
```bash
curl -O https://raw.githubusercontent.com/orisano/owiener/master/owiener.py
```

## Example
```python
import owiener

e = 30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
n = 109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
    
# Hacked d=4221909016509078129201801236879446760697885220928506696150646938237440992746683409881141451831939190609743447676525325543963362353923989076199470515758399
```

## Reference
Cryptanalysis of Short RSA Secret Exponents:  
https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf  
pablocelayes/rsa-wiener-attack:  
https://github.com/pablocelayes/rsa-wiener-attack  
wihoho/Wiener-s-Attack:  
https://github.com/wihoho/Wiener-s-Attack

## Author
Nao Yonashiro (@orisano)

## License
MIT
