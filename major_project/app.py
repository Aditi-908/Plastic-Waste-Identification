import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from PIL import Image
import util

model = None

class CustomEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return  # Ignore directory events for simplicity

        if isinstance(event, FileCreatedEvent):
            print("File created:" + event.src_path)
            file_name = os.path.basename(event.src_path)
            
            absolute_path = os.path.join(os.getcwd(), event.src_path)
            
            print("Path is:" + file_name)
            assert os.path.isfile(absolute_path)
            time.sleep(1)
            
            # Change the source and destination paths here
            source_directory = sys.argv[1] if len(sys.argv) > 1 else '.'
            destination_directory = sys.argv[2] if len(sys.argv) > 2 else '.'
            
            image_path = os.path.join(destination_directory, file_name)
            result = util.classify_waste(image_path)
            
            print(f'{file_name} is {result}')

if __name__ == "__main__":
    util.load_artifacts()
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Set the default source and destination paths or use command-line arguments
    source_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    destination_path = sys.argv[2] if len(sys.argv) > 2 else '.'
    
    event_handler = CustomEventHandler()
    observer = Observer()
    observer.schedule(event_handler, source_path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
