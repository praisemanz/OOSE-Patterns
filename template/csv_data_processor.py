"""Concrete class implementing CSV data processing"""
from data_processor import DataProcessor


class CSVDataProcessor(DataProcessor):
    
    def read_data(self) -> None:
        print("Reading data from CSV file...")
        print("CSV data loaded successfully.")
    
    def process_data(self) -> None:
        print("Processing CSV data:")
        print("  - Parsing comma-separated values")
        print("  - Converting to structured format")
        print("CSV processing complete.")
    
    def validate_data(self) -> None:
        print("Validating CSV data:")
        print("  - Checking column count")
        print("  - Verifying data types")
        print("CSV validation passed.")
    
    def save_data(self) -> None:
        print("Saving processed CSV data to database...")
        print("CSV data saved successfully.")
