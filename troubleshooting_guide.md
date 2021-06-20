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

