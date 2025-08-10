## Phase 1: Data Collection 
from abc import abstractmethod, ABC 
import pandas 
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
    pass
# Implement ImageCollector class
class ImageCollector(DataCollector):
    pass 
# Implement LabelCollector class
class LabelCollector(DataCollector):
    pass

# Implement ProductTAbleCollector class
class ProductTableCollector(DataCollector):
    pass


