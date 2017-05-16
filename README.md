# sqre_labkubespawner

Integrate JupyterHub with JupyterLab; this is a cut-down version of 
[jupyterhub-labextension](https://github.com/jupyterhub/jupyterhub-labextension)
modified enough that it will also compile on Python 2.

It requires Jupyterlab 0.21.0 or later; all Javascript formerly in it is
now part of the jupyterlab-hub npm package.


## Prerequisites

* JupyterLab >= 0.21.0

## Installation

```bash
pip install sqre-labkubespawner
jupyter labextension install jupyterlab-hub
jupyter lab build
```

Edit the JupyterHub configuration file (typically ``jupyterhub_config.py``) to
use the extension's custom spawner command. This is necessary to pass
configuration from JupyterHub into JupyterLab.

```python
c.Spawner.cmd = ['jupyter-singlelabuser']
```


