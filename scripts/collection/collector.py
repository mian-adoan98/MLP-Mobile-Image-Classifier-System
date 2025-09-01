## Phase 1: Data Collection 
from abc import abstractmethod, ABC 
import pandas as pd 
import os 
import sys
import requests

# 
# Implementing 3 classes: 
# 
#   - ImageCollector class: collecting images from web browser 
#   - LabelCollector class collecting labels (representing brand names of phone) 
#   - ProductTableCollector class: collecting table of specifications linked for each phone 
#   - RawDataExtractor class: extracting raw data from internet source (URLs, logs, etc. )#

# Implement DataCollector abstract class
class DataCollector(ABC):
    # Initialise attributes for collecting data
    def __init__(self, folder: str):
        self.path = "C:\Development\Projects\MachineLearning\Mobile-Image_Classifier-System\data"
        self.folder_path = os.path.join(self.path, folder)
        # self.source_folder = "data"

    # Abstract method 1: collect data 
    @abstractmethod
    def collect(self, filename: str):
        pass 
        
# Implement DataLoader: 
class DataLoader:
    # Implement method 1: to load data
    def load(self, filename: str, folder: str) -> pd.DataFrame:
        csv_file = self.select_csv_file(filename, folder=folder)
        data = pd.read_csv(csv_file, index_col=0) 

    # Implement method 2: select a folder 
    def select_folder(self, sel_folder: str) -> str:
        # Create source folder variable
        source_folder = os.path.join(self.path, self.source_folder)

        # Iteration: check if all required folders exist
        for folder in os.listdir(source_folder):
            try:
                # Create folder path variable
                folder_path = os.path.join(source_folder, folder)

                # Check if folder exist
                if not os.path.exists(folder_path):
                    # Create a new existing folder
                    new_folder = os.path.join(folder_path, folder)
                    os.mkdir(new_folder)
            except OSError:
                # print(folder_path)
                print(new_folder)

        # Select the required folder 
        if sel_folder in os.listdir(source_folder):
            selected_folder_path = os.path.join(source_folder, sel_folder)
            return selected_folder_path

    # Implement method 3: select a file
    def select_csv_file(self, filename: str, folder: str) -> str:
        # Select a folder
        sel_folder = self.select_folder(folder)
        
        # Select a csv-file (if it exists)
        csv_filename = f"{filename}.csv"
        
        if csv_filename in os.listdir(sel_folder):
            filename_path = os.path.join(sel_folder, csv_filename)
            return filename_path

# Implement WebCollector class 
class WebCollector(DataCollector):
    def __init__(self, folder: str, weblinks: list):
        super().__init__(folder)
        self.weblinks = weblinks

    # Method 1: collect weblinks 
    def collect(self, filename: str):
        # Create a filename 
        weblink_file = os.path.join(self.folder_path, filename)

        # Create a textfile with weblinks 
        with open(weblink_file, "w") as textfile:
            for weblink in self.weblinks:
                textfile.writelines(weblink + "\n")
        print(f"Sucessfully collected {len(self.weblinks)} webpages")


# Implement ImageCollector class
class ImageCollector(DataCollector):
    # Initiliase fields 
    def __init__(self, folder, image_urls):
        super().__init__(folder)
        self.image_urls = image_urls

    # Method 1: loading images 
    def collect(self, folder_name: str) -> pd.DataFrame:
        # Save html content in local device
        image_folder = os.path.join(self.folder_path, f"{folder_name}")
        
        # Check if folder exists
        if not os.path.exists(image_folder):
            os.makedirs(image_folder, exist_ok=True)

        # Store the images into image folder 
        for index, image_url in enumerate(self.image_urls):
            file_name = f"image_{index + 1}.png"
            filepath = os.path.join(image_folder, file_name)

            # Send http-request to web to get access to the image data 
            response = requests.get(image_url)
            if response.status_code == 200:
                # Download image + Store into the matching file path
                with open(filepath, "wb") as item:
                    item.write(response.content)

                print(f"Image stored successfully in path {filepath}.")
            else:
                print(f"Failed to download image. Status code = {response.status_code}.")

        # Store image url in dataset
        image_ds = pd.DataFrame()
        image_ds["ImageLink"] = self.image_urls

        return image_ds
    
    # Method 2: return a textmessage about number of collected images
    def __str__(self):
        return f"Collected {len(self.image_urls)} images."

# Implement LabelCollector class
class LabelCollector(DataCollector):
    # Method: collect labels and store into a dataset
    def collect(self, labels: int, filename: str) -> pd.DataFrame:
        # Create a label dataset
        label_ds = pd.DataFrame()
        label_ds["Labels"] = labels

        # Save label dataset in existing folder 
        labels_data_folder = "label_dataset"
        label_folder_path = os.path.join(self.folder_path, labels_data_folder)
        
        # Check if path exists
        if not os.path.exists(label_folder_path):
            os.makedirs(label_folder_path, exist_ok=True)

        # Save label dataset
        label_file_path = os.path.join(label_folder_path, f"{filename}.csv")
        label_ds.to_csv(label_file_path)

        return label_ds
    
    # # Constructor: send a message (later)
    # def detect_num_labels(extractor: object) -> str:
    #     labels = extractor.extract()

# Implement ProductTAbleCollector class
class ProductTableCollector(DataCollector):
    pass


## ------------------------------------------------------------------------------------------------------------------

# Example code

if __name__ == "__main__":
    pass