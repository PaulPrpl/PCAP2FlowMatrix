<h1>Quick start</h1>
<h3>Setup :</h3>
<code>$ git clone https://github.com/PaulPrpl/PCAP2FlowMatrix</code><br>
<code>$ cd PCAP2FlowMatrix</code><br>
<code>$ mkdir captures output</code><br>
<div>Then, place your network PCAP or PCAPNG files in the newly created "captures" folder.</div>
<h3>Run the program for the first time :</h3>
<code>$ chmod u+x pcap2flows && ./$_</code><br>
<div>If you don't want to use Docker or if you do not use Linux, only use the "app" directory and create "captures" and "output" folders inside.</div><br>
<div>Then, while located into the "app" directory, start with :</div>
<code>$ python3 init.py</code>
<h3>Bugs :</h3>
<div>If you create "captures" and "output" directories as root before you launch this app with Docker, you may experience some troubles :</div>
<code>$ chown 1000 captures output # Will fix your issue</code>

<h3>Notes:</h3>
<ul>
  <li>Credits to Scapy library that made this program core : <a href=https://github.com/secdev/scapy>scapy.net</a></li>
  <li>This app uses Docker alongside Docker-Compose with <a href=https://hub.docker.com/r/opensuse/tumbleweed>OpenSUSE tumbleweed</a></li>
  <li>Provided script <code>pcap2flows</code> is written in bash and will not run without it on host.<br>You can use directly python otherwise</li>
</ul>
