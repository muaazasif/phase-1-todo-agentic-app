# VIP Todo CLI Application with Rich Library

This is an upgraded command-line Todo application built with Python and the Rich library. It provides a visually appealing interface with tables, colored text, and enhanced user experience while maintaining all the original functionality.

## Features

- Add Task: Add a new task with a title and an optional description.
- View Tasks: Display all current tasks in a formatted table with color-coded status.
- Update Task: Modify the title or description of an existing task by its ID.
- Delete Task: Remove a task by its ID with confirmation.
- Mark/Unmark Complete: Toggle the completion status of a task by its ID with visual feedback.
- Print Final Record: Generate and save a summary of all tasks to both a timestamped text file and a PDF report in the /src directory, ready for client email.
- Data Persistence: All tasks are automatically saved to a local JSON file and persist between application sessions.
- Excel Export: Export all tasks to a professionally formatted Excel file with color-coded status indicators.
- Email Sending: Send tasks directly via email with optional Excel or PDF attachments.
- Enhanced UI: Rich tables, colored text, progress indicators, and panels for a premium experience.

## Requirements

- Python 3.13+
- Rich library
- ReportLab library
- OpenPyXL library

## Email Configuration

To enable real email sending functionality, configure your email settings using environment variables. See EMAIL_CONFIG.md for detailed setup instructions.

## Data Storage

The application automatically saves all tasks to a local `todos.json` file in the `/src` directory. This file persists between application sessions, so your tasks will remain even after closing and reopening the application.

## Installation

1.  **Navigate to the project directory:**

    ```bash
    cd /path/to/todo-agentic
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    
    Or install rich directly:
    
    ```bash
    pip install rich
    ```

## How to Run

1.  **Navigate to the project directory:**

    ```bash
    cd /path/to/todo-agentic
    ```

2.  **Run the application:**

    ```bash
    python src/app.py
    ```

## Usage

Upon running the application, you will be presented with a visually enhanced menu:

```
Todo Application Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark/Unmark Task Complete
6. Print Final Record
7. Export to Excel
8. Send Email
9. Exit
```

Enter the number corresponding to the action you wish to perform and follow the prompts. The application will display tasks in a formatted table with green for completed tasks and red for incomplete tasks.

## Visual Enhancements

- Tasks are displayed in a rich table format
- Status indicators are color-coded (green for Complete, red for Incomplete)
- Progress indicators when marking tasks complete
- Enhanced input prompts with validation
- Confirmation dialogs for destructive actions
- Welcome panel and styled text throughout the application