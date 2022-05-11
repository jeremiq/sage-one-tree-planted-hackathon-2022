#!/usr/local/env python
from  sage_one_tree_planted.data.climate_and_economic_justice_dataset import ClimateAndEconomicJusticeDataset
c = ClimateAndEconomicJusticeDataset(local_data_path="./_data/cej")
c.fetch_data()
