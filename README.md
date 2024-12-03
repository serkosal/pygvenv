# Important note
It was my self-writed solution which, I've used from september 24, but there was a solution which I dont know already existed at that moment, so it consider to use https://github.com/pypa/pipx. 

# pygvenv
pygvenv (Python Global Virtual Environments) is usefull when you want to use global-wide pip packages without interfering with system dependencies and packages. 
 It will also help avoid this annoying warning: 
```error: externally-managed-environment```  

It achieves this by using a separate, isolated Python virtual environment, which will not interfere with system dependencies.

# Requirements
First and obviosly, PYgvenv requires PYTHON to be installed, which is most likely already fulfilled. 
However if it's not installed for some reason, you can easily install it by running a command like:  ```sudo apt install python3```. 
The actual command may depend on your Linux distribution and package manager in use, so search online for how to install Python on your specific distribution.

Next, you should install the pip module. To do so, follow the instructions in this article: https://pip.pypa.io/en/stable/installation/

Lastly, as the name suggests, PyGVEnv also requires Python's ```venv``` module, , which comes by default with Python 3.3 and above.  If, for some reason, it's not available, you can install it using the following command:
```pip install venv```.

If you encounter the following error:
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
```

Follow the error message’s advice and use your package manager instead of pip. For Debian-based distributions, the installation command would be:
```sudo apt install python3-venv```

# Install
- ```git clone https://github.com/serkosal/pygvenv.git```
- ```pygvenv/install.sh```
- ```pygvenv create``` to create the default environment, which located in user's home directory ```~/.pygvenv```

# Usage 
Example usage:
- ```pygvenv pip install httpx```
- ```pygvenv run http --help```

# How it works?
Under the hood, pygvenv simply uses these methods:
- runs ```mkdir -p VENV_PATH && python3 -m venv VENV_PATH``` for creation of regular python virtual environment 
- activates and deactivates virtual environment, when using pygvenv's ```run``` and ```pip``` methods 
