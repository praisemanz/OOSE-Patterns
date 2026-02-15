"""Concrete class implementing JSON data processing"""
from data_processor import DataProcessor


class JSONDataProcessor(DataProcessor):
    
    def read_data(self) -> None:
        print("Reading data from JSON file...")
        print("JSON data loaded successfully.")
    
    def process_data(self) -> None:
        print("Processing JSON data:")
        print("  - Parsing JSON structure")
        print("  - Deserializing objects")
        print("JSON processing complete.")
    
    # Uses default validation from parent class (hook method not overridden)
    
    def save_data(self) -> None:
        print("Saving processed JSON data to database...")
        print("JSON data saved successfully.")
