# Automatically move a file to desktop when downloaded


## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Elijah1368/fileMover.git
```

### 2. Open Task Scheduler
- Search for "Task Scheduler" in the Start menu and open it.

### 3. Create a New Task
- Click on "Create Basic Task" or "Create Task" on the right-hand panel.

### 4. Set Task Properties
- Name the task and provide a description if you want.
- Choose the "Trigger" (e.g., at startup, daily, etc.).
- In the "Actions" tab, choose "Start a program" and browse to the location of the script.

### 5. Finish and Test
- Click "Finish" to create the task.
- You can right-click on the task and choose "Run" to test it.

## Changing Watched Files and Folders
To change the folder being watched, the file being watched, or the destination folder, simply edit the following variables in the script:

```python
WATCH_FOLDER = "~/NewFolderToWatch"
WATCHED_FILE = "NewFileToWatch.pdf"
MOVE_TO_FOLDER = "~/NewDestinationFolder"
