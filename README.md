# MasscanParser
This script is designed to parse through [masscan](https://github.com/robertdavidgraham/masscan) xml outputs and then creates a IP:Port lists based on filters.

## Requirements
- Python 3 - from (https://python.org)
- masscan - from [masscan](https://github.com/robertdavidgraham/masscan)

## Banner checking

Below is from the documentation from the [masscan](https://github.com/robertdavidgraham/masscan) documentation when you are not able to grab banners

Masscan can do more than just detect whether ports are open. It can also complete the TCP connection and interaction with the application at that port in order to grab simple "banner" information.

The problem with this is that masscan contains its own TCP/IP stack separate from the system you run it on. When the local system receives a SYN-ACK from the probed target, it responds with a RST packet that kills the connection before masscan can grab the banner.

The easiest way to prevent this is to assign masscan a separate IP address. This would look like the following:

#### masscan 10.0.0.0/8 -p80 --banners --source-ip 192.168.1.200

The address you choose has to be on the local subnet and not otherwise be used by another system.

In some cases, such as WiFi, this isn't possible. In those cases, you can firewall the port that masscan uses. This prevents the local TCP/IP stack from seeing the packet, but masscan still sees it since it bypasses the local stack. For Linux, this would look like:

#### iptables -A INPUT -p tcp --dport 60000 -j DROP
#### masscan 10.0.0.0/8 -p80 --banners --source-port 60000

On Mac OS X and BSD, it might look like this:

#### sudo ipfw add 1 deny tcp from any to any 60000 in
#### masscan 10.0.0.0/8 -p80 --banners --source-port 60000

Windows doesn't respond with RST packets, so neither of these techniques are necessary. However, masscan is still designed to work best using its own IP address, so you should run that way when possible, even when its not strictly necessary.

## Usage

Run [masscan](https://github.com/robertdavidgraham/masscan) -p80 10.0.0.0/8 -oX <output file> --banners 

Then use this script to parser the input file file

python ParseMyList.py <input file>

This will create an output.txt file with IP:Port, Example

10.0.0.3:80

10.0.0.36:80

10.0.0.41:80

## Bugs

Report them [here](https://github.com/bleedingangl/MasscanParser/issues/new)

## Working (Out the Box)

This script works "out of the box" on [Manjaro 17.0.2 x86_x64](https://manjaro.org/) but first install Masscan via Terminal

pacman -S masscan

Next step is to take a look at ""Banner checking"" on the top of this page or [masscan gitgub](https://github.com/robertdavidgraham/masscan)
