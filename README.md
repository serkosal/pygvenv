# pygvenv
PyGVEnv (Python Global Virtual Environments) usefull when you want to use global-wide pip packages without messing with system dependencies and packages 
OR will help to avoid this annoying warning: 
```error: externally-managed-environment```  

It achieve it by using separate, isolated python's virtual environment which will not mess with system dependenies.

# Requirements
Firstly and obviosly ```PYTHON global virtual environment``` requires python to be installed, which most probably already fullfied. But if for some reason doesn't, It easily could be installed by running something like ```sudo apt install python3```, actual command depends on your linux distribution and package manager in use, search how to install package in your distro in the Internet.
Secondly, you should install pip module, read this article for to this: https://pip.pypa.io/en/stable/installation/
Lastly as name suggest it's also required python's module called ```venv``` which should come by default from Python's version 3.3 and above. But if for some reason it is not the case you try install it by command.
```pip install venv```
If you get error:
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
```
Use, as the error suggested, your package manager for this, not the pip. For debian based distros installation it'll look like this: 
```sudo apt install python3-venv```

# Install
- ```git clone https://github.com/serkosal/pygvenv.git```
- ```pygvenv/install.sh```
- And then for creation of default environment run command: ```pygvenv create```

# Usage 
Example of usage:
- ```pygvenv pip install httpx```
- ```pygvenv run http --help```

# How it works?
Under the hood PyGVEnv will just use these methods:
- run ```mkdir -p VENV_PATH && python3 -m venv VENV_PATH``` for creation of regular python virtual environment 
- activate and deactivate virtual environment, when using pygvenv's run and pip methods 
