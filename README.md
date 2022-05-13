# sage-one-tree-planted-hackathon-2022

Code and artifacts of the Sage Tech Hackathon for Good for One Tree Planted

To launch an interactive demo click here [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jeremiq/sage-one-tree-planted-hackathon-2022/v0.2.0?labpath=voila%2Frender%2Fsage_one_tree_planted%2Fnotebooks%2Finteractive_notebook.ipynb)
![screen shot interactive_map
](sage_one_tree_planted/CA_disadvantaged_tracts.png)
# Helping One Tree Planted!
## The Problem
As part of the Sage Tech For Good hackathon, One Tree Planted asked us
to help them prioritize where trees are planted in the USA by
identifying disadvantaged communities that can benefit from having
more trees.

We started with the Climate and Economic Justice screening tool data
from the US Census. Although very detailed, it's not possible to use
this data/tool to identify their most disadvantaged communities or to
filter based on different criteria.

These capabilities are important for answering such questions as
> What are the most disadvantaged places in the US?

> If I get a donation to plant trees in a given state, where in that state should we prioritize?

> If I only want to use some of the Census Bureau's criteria, how can I see only those places that match that criteria?

## Future directions

Although we did not have time to implement it, we believe it would be
valuable to integrate our solution with the [Canopy cover
dataset](https://data.fs.usda.gov/geodata/rastergateway/treecanopycover/)
so that prioritization for planting trees could also take into account
how many trees exist in a given area. We did explore this dataset and
provide a notebook that could facilitate that integration
[here](https://github.com/jeremiq/sage-one-tree-planted-hackathon-2022/blob/main/sage_one_tree_planted/notebooks/Canopy_data_exploration.ipynb)
Using that notebook, you can compute the canopy coverage in a given
Census Tract.

Furthermore, we'd love to optimize the performance of the workbook and
its deployment on Binder to facilitate easier sharing. However,
running the notebook locally is the fastest way to access it at this time.

## The Solution
We've created an interactive workbook that
- Pulls data dynamically from
the Climate and Economic Justice screening tool.
- We present an
interactive display where One Tree Planted can aggregate and filter
that data based on geolocation and community size.
- We allow users to select specific hardship criteria and also see
which communities are most affected by them
- We provid interactive dynamic maps
- We also provide dynamically updating downloadable CVSs of our
  analyses so that results can be easily shared.
- Finally, we make this workbook available as a docker container
  running jupyterlab so that it can be easily deployed and accessed
  from anywhere
- That environment is deployed via JupyterHub Binder for easy access
  and sharing (although the initial deployment does take some time)

### Technical details

Our solution makes is based on a [dynamic data fetcher](https://github.com/jeremiq/sage-one-tree-planted-hackathon-2022/blob/main/sage_one_tree_planted/data/climate_and_economic_justice_dataset.py#L6) that pulls
caches, and provides easy programatic access to their census data.

After data is acquired, we make heavy users of the scientific python
stack (pandas) to imlement custom aggregation and filtering.

Finally our UI is based on a jupyternotebook that makes heavy use of
ipython widgets to provide interactive controlls and generate dynamic
downloadable links of CSVs. All maps are generated using the geopandas
library. [Here's](https://github.com/jeremiq/sage-one-tree-planted-hackathon-2022/blob/main/sage_one_tree_planted/notebooks/interactive_notebook.ipynb) a link to a (non interactive view) of the entire
workbook:

We've provided a convenient [Docker container](https://github.com/jeremiq/sage-one-tree-planted-hackathon-2022/blob/main/Dockerfile) for running and
displaying their full interactive notebook via JupyterHub Binder.



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
   [here](http://127.0.0.1:8888/lab/workspaces/auto-I/tree/sage_one_tree_planted/notebooks/interactive_notebook.ipynb)
