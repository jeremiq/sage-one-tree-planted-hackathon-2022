# sage-one-tree-planted-hackathon-2022

Code and artifacts of the Sage Tech Hackathon for Good for One Tree Planted

To launch an interactive demo click here [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeremiq/sage-one-tree-planted-hackathon-2022/HEAD?labpath=sage_one_tree_planted%2Fnotebooks%2Finteractive_notebook.ipynb)

# Interactive map of disadvantaged census tracts

Here is a map of disadvantaged census tracts that are
in California.

As part of the Sage Tech For Good hackathon, we have created layers of interactive maps that are the visualizations of
various disadvantaged census tracts. One Tree Planted
can use these directly or even embed them in their website, showcasing their progress to the interested
parties.
![screen shot interactive_map ](sage_one_tree_planted/CA_disadvantaged_tracts.png)
![interactive_map](sage_one_tree_planted/DF_PFS_CA.html)

# Repo setup

## Fully local

1. install python, for example with pyenv: `pyenv install 3.10.3`
2. install poetry: `pip install poetry`
3. use poetry to install the dependencies: `poetry install`
4. Fire up a jupyter server and go from there: `poetry run jupyter notebook sage_one_tree_planted/notebooks`

## Via Docker

In case it's easier to work with this data via docker, you can get a
local image and access our interactive workbook via

1. build their image `docker build -t sage-one-tree-planted .`
2. Run the image and access the lab! `docker run -it --rm -p 8888:8888 sage-one-tree-planted jupyter lab --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888`
3. Access our interactive workbook
   [her](http://127.0.0.1:8888/lab/workspaces/auto-I/tree/sage_one_tree_planted/notebooks/interactive_notebook.ipynb)
