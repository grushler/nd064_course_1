# Troubleshooting Guide for MacOS

#### Issue with vagrant installation
Official website instructions for installing vagrant do not work as the tap doesn't exist. For installing vagrant, run the command - `brew cask install vagrant` or simply - `brew install vagrant`

---

#### Flask app logging configuration issue which doesn't save logs to file
Issue is that the python logging config in the code is overridden if there is any other imported module that already uses python logging module. To resolve this issue move the logging configuration outside the main function -
```
import logging
logging.basicConfig(
        format='[%(asctime)s] [%(levelname)s] [%(threadName)s] [%(name)s] [%(message)s]',
        level=logging.DEBUG, 
        filename='app.log')
```

---

#### k3s fails with SSL error in Vagrant box (VirtualBox)
Below is the error I got when i used the curl command to download k3s.
```
vagrant@localhost:~> curl -sfL https://get.k3s.io | sh -
[INFO]  Finding release for channel stable
curl: (60) SSL certificate problem: self signed certificate in certificate chain
More details here: https://curl.haxx.se/docs/sslcerts.html
curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
[INFO]  Using v1.21.1+k3s1 as release
[INFO]  Downloading hash https://github.com/k3s-io/k3s/releases/download/v1.21.1+k3s1/sha256sum-amd64.txt
```

Issue was that there was no certificate available on my machine that could be used to for the curl to work. By passing the curl command using `-k` didn't work either because the k3s script has other curl commands that would stop the script from executing. As a workaround, follow below steps which were provided by fellow scholar Florian.Schneider -
* In your browser, open the url https://get.k3s.io. It should download a shell script or load a shell script as text in browser.
* Copy and paste it in your editor. Replace the actual curl commands to have `-k`. It appear in 2 places exactly as commands. Rest all places ignore.
* Save the script. Upload the script to vagrant box using `vagrant upload filename.sh`.
* Login to vagrant shell using `vagrant sh` command. Locate the filename.sh file (it should be in the home directory `cd ~`).
* Run the shell script `sh filename.sh`. k3s should be downloaded without any problem.

On a side note, I have added the shell script file for k3s in this repository under resources folder as `get_k3s_io.sh` file.

---
