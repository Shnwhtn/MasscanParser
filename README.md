# MasscanParser
This script is desgined to parse through [masscan](https://github.com/robertdavidgraham/masscan) xml outputs and then creates a IP:Port lists based on filters

## Requirements
- Python 3 - from (https://python.org)
- ProgressBar - from [PyPi] (https://pypi.python.org/pypi/progressbar33)
- masscan - from [masscan](https://github.com/robertdavidgraham/masscan)

### Usage

Run [masscan](https://github.com/robertdavidgraham/masscan) -p80 10.0.0.0/8 -oX scan.xml --banners --source-port 60000

Then use this script to parser the scan.xml file

python ParseMyList.py scan.xml

This will create an output.txt file with IP:Port, Example

10.0.0.3:80
10.0.0.36:80
10.0.0.41:80

