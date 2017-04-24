# sqre_labkubespawner

Integrate JupyterHub with JupyterLab


## Prerequisites

* JupyterLab 0.17.0 or later

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

