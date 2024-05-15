import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/DELL/Downloads"


class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"Hey , {event.src_path} has been created")
        
    def on_deleted(self, event):
        print(f"OOps! Someone deleted {event.src_path}")
        


event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True :
        time.sleep(1)
        print("Running .....")
except KeyboardInterrupt:
    print("Stoped .....")
    observer.stop()