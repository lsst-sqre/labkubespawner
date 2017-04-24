# sqre_labkubespawner

Integrate JupyterHub with JupyterLab; this is a cut-down version of 
[jupyterhub-labextension](https://github.com/jupyterhub/jupyterhub-labextension)
modified enough that it will also compile on Python 2.

It hasn't been updated for JupyterLab 0.20 or later yet.


## Prerequisites

* JupyterLab >= 0.17.0, < 0.20.0

## Installation

To install using pip:

```bash
pip install sqre_labkubespawner
jupyter labextension install --py --sys-prefix sqre_labkubespawner
jupyter labextension enable --py --sys-prefix sqre_labkubespawner
```

Edit the JupyterHub configuration file (typically ``jupyterhub_config.py``) to
use the extension's custom spawner command. This is necessary to pass
configuration from JupyterHub into JupyterLab.

```python
c.Spawner.cmd = ['jupyter-singlelabuser']
```

## Development

For a development install (requires npm version 4 or later), do the following in the repository directory:

```bash
npm install
pip install -e .
jupyter labextension install --symlink --py --sys-prefix sqre_labkubespawner
jupyter labextension enable --py --sys-prefix sqre_labkubespawner
```

To rebuild the extension bundle:

```bash
npm run build
```

