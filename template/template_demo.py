"""Main class demonstrating the Template pattern"""
from csv_data_processor import CSVDataProcessor
from xml_data_processor import XMLDataProcessor
from json_data_processor import JSONDataProcessor


def main():
    print("=== Template Pattern Demo - Data Processing System ===\n")
    
    print("--- Processing CSV Data ---")
    csv_processor = CSVDataProcessor()
    csv_processor.process()
    
    print("--- Processing XML Data ---")
    xml_processor = XMLDataProcessor()
    xml_processor.process()
    
    print("--- Processing JSON Data ---")
    json_processor = JSONDataProcessor()
    json_processor.process()
    
    print("=== Demo Complete ===")


if __name__ == "__main__":
    main()
