from implementations.local_file_manager import LocalFileManager
from implementations.zip_compressor import ZipCompressor
from implementations.network_client import NetworkClient

def main():

    print("=== Local File Manager ===")
    file_manager = LocalFileManager()
    file_manager.read_file("test.txt")
    file_manager.write_file("test.txt", "Hello")

    print("\n=== Zip Compressor ===")
    zipper = ZipCompressor()
    zipper.compress_file("test.txt")
    zipper.decompress_file("test.txt")

    print("\n=== Network Client ===")
    client = NetworkClient()
    client.connect_to_server("127.0.0.1", 8080)
    client.send_data(b"Hello Server")
    client.receive_data()


if __name__ == "__main__":
    main()
