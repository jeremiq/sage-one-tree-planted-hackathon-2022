import pathlib
import requests
import shutil
import zipfile

class ClimateAndEconomicJusticeDataset:
    def __init__(self):
        self.BASE_DATA_PATH="https://static-data-screeningtool.geoplatform.gov/data-pipeline/data/score"
        self.SCREENING_TOOL_DATA_URL = f"{self.BASE_DATA_PATH}/downloadable/Screening_Tool_Data.zip"
        self.SHAPEFILE_URL = f"{self.BASE_DATA_PATH}/shapefile/usa.zip"
        self.local_path = pathlib.Path("../../_data/cej")
        self.shape_file = self.local_path/"usa"
        self.screening_data=self.local_path/"screening_data"
        self._mkdirs()
        
   
    def _mkdirs(self):
        pathlib.Path(self.shape_file).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.screening_data).mkdir(parents=True, exist_ok=True)
    
    def _is_empty(self, path: pathlib.Path) -> bool:
        return not any(path.iterdir())

    def _fetch_screening_tool_data(self):
        self._download_and_unpack(self.SCREENING_TOOL_DATA_URL, self.screening_data.name)

    def _fetch_shape_file(self):
        self._download_and_unpack(self.SHAPEFILE_URL, self.shape_file.name)

    def _download_and_unpack(self, url: str, data_file_name: str) -> None:
        zipfile = f'{self.local_path}/{data_file_name}.zip'
        outputdir = f'{self.local_path}/{data_file_name}'
        self._download_file(url, local_filename=zipfile)
        self._unzip(zipfile, outputdir)
        pathlib.Path(zipfile).unlink()
        
    def fetch_data(self, clear_cache=False) -> None:
        if self._is_empty(self.shape_file) or clear_cache:
            self._fetch_shape_file()
        if self._is_empty(self.screening_data) or clear_cache:
            self._fetch_screening_tool_data()
        
    
    @staticmethod
    def _unzip(input_zipfile: str, output_foldername: str):
        with zipfile.ZipFile(input_zipfile, 'r') as z:
            z.extractall(output_foldername)

    
    @staticmethod
    def _download_file(url: str, local_filename: str) -> str:
        with requests.get(url, stream=True) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        return local_filename
