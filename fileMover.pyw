import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "~/Downloads"
WATCHED_FILE = "ElijahAmianResume.pdf"
MOVE_TO_FOLDER = "~/Desktop"

class Watcher:
    DIRECTORY_TO_WATCH = os.path.expanduser(WATCH_FOLDER)

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            self.observer.join()

class Handler(FileSystemEventHandler):
    def process(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'moved':
            if WATCHED_FILE  in os.path.basename(event.dest_path):
                desktop_path = os.path.expanduser(f"{MOVE_TO_FOLDER}/{WATCHED_FILE}")
                
                # Delete existing file on Desktop if it exists
                if os.path.exists(desktop_path):
                    os.remove(desktop_path)

                # Move new file to Desktop
                shutil.move(event.dest_path, desktop_path)

    def on_moved(self, event):
        self.process(event)

if __name__ == '__main__':
    w = Watcher()
    w.run()
