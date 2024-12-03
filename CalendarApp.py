import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Guide")
        self.root.geometry("700x700")

        # Data structures to hold calendar data
        self.calendars = {}
        self.current_calendar = None

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Calendar Selection Dropdown
        self.calendar_label = tk.Label(self.root, text="Select Calendar:")
        self.calendar_label.pack(pady=5)

        self.calendar_var = tk.StringVar()
        self.calendar_menu = ttk.Combobox(self.root, textvariable=self.calendar_var, state="readonly")
        self.calendar_menu.pack(pady=5)
        self.calendar_menu.bind("<<ComboboxSelected>>", self.select_calendar)

        # Add and Remove Calendar Buttons
        self.add_calendar_button = tk.Button(self.root, text="Add Calendar", command=self.add_calendar)
        self.add_calendar_button.pack(pady=5)

        self.remove_calendar_button = tk.Button(self.root, text="Remove Calendar", command=self.remove_calendar)
        self.remove_calendar_button.pack(pady=5)

        # Calendar Widget
        self.calendar = Calendar(self.root, selectmode="day", year=2024, month=12, day=1)
        self.calendar.pack(pady=20)
        self.calendar.bind("<<CalendarSelected>>", self.display_selected_date_content)

        # Buttons for Adding, Removing, and Editing Entries
        self.add_reminder_button = tk.Button(self.root, text="Add Reminder", command=self.add_reminder)
        self.add_reminder_button.pack(pady=5)

        self.add_event_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_event_button.pack(pady=5)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Reminder/Event/Task", command=self.edit_entry)
        self.edit_button.pack(pady=5)

        self.remove_entry_button = tk.Button(self.root, text="Remove Reminder/Event/Task", command=self.remove_entry)
        self.remove_entry_button.pack(pady=5)

        # Display Area for Calendar Content
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=10, fill="both", expand=True)

        self.display_text = tk.Text(self.display_frame, wrap="word", state="disabled")
        self.display_text.pack(padx=10, pady=10, fill="both", expand=True)

    def update_calendar_menu(self):
        self.calendar_menu["values"] = list(self.calendars.keys())

    def select_calendar(self, event=None):
        self.current_calendar = self.calendar_var.get()
        self.display_selected_date_content()

    def add_calendar(self):
        new_calendar_name = simpledialog.askstring("Add Calendar", "Enter calendar name:")
        if new_calendar_name and new_calendar_name not in self.calendars:
            self.calendars[new_calendar_name] = {"reminders": [], "events": [], "tasks": []}
            self.update_calendar_menu()
            messagebox.showinfo("Success", f"Calendar '{new_calendar_name}' added!")
        elif new_calendar_name:
            messagebox.showwarning("Warning", f"Calendar '{new_calendar_name}' already exists.")

    def remove_calendar(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "No calendar selected.")
            return

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete calendar '{self.current_calendar}'?")
        if confirm:
            del self.calendars[self.current_calendar]
            self.current_calendar = None
            self.update_calendar_menu()
            self.display_selected_date_content()
            messagebox.showinfo("Success", "Calendar deleted.")

    def add_reminder(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "Please select a calendar first!")
            return

        selected_date = self.calendar.get_date()
        reminder_time = simpledialog.askstring("Add Reminder", "Enter time (HH:MM):")
        reminder_note = simpledialog.askstring("Add Reminder", "Enter reminder note:")

        if selected_date and reminder_time and reminder_note:
            self.calendars[self.current_calendar]["reminders"].append(
                {"date": selected_date, "time": reminder_time, "note": reminder_note}
            )
            messagebox.showinfo("Success", "Reminder added!")
            self.display_selected_date_content()

    def add_event(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "Please select a calendar first!")
            return

        selected_date = self.calendar.get_date()
        event_name = simpledialog.askstring("Add Event", "Enter event name:")
        if selected_date and event_name:
            self.calendars[self.current_calendar]["events"].append({"name": event_name, "date": selected_date})
            messagebox.showinfo("Success", "Event added!")
            self.display_selected_date_content()

    def add_task(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "Please select a calendar first!")
            return

        task_name = simpledialog.askstring("Add Task", "Enter task description:")
        task_deadline = self.calendar.get_date()
        if task_name and task_deadline:
            self.calendars[self.current_calendar]["tasks"].append({"task": task_name, "deadline": task_deadline})
            messagebox.showinfo("Success", "Task added!")
            self.display_selected_date_content()

    def list_entries(self, entry_type, selected_date):
        """Returns a list of entries of the specified type for the selected date."""
        if entry_type not in ["reminder", "event", "task"]:
            return []

        return [
            (index, entry)
            for index, entry in enumerate(self.calendars[self.current_calendar][f"{entry_type}s"])
            if entry.get("date") == selected_date or entry.get("deadline") == selected_date
        ]

    def choose_entry(self, entry_type, selected_date, action):
        entries = self.list_entries(entry_type, selected_date)
        if not entries:
            messagebox.showinfo("Info", f"No {entry_type}s found for {selected_date}.")
            return None

        options = "\n".join([f"{i + 1}. {entry}" for i, entry in enumerate(entries)])
        choice = simpledialog.askinteger(
            f"{action.capitalize()} {entry_type.capitalize()}",
            f"Select {entry_type} to {action}:\n{options}",
        )
        if choice is None or choice < 1 or choice > len(entries):
            messagebox.showwarning("Warning", "Invalid selection.")
            return None

        return entries[choice - 1][0]  # Return the index

    def remove_entry(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "Please select a calendar first!")
            return

        selected_date = self.calendar.get_date()
        entry_type = simpledialog.askstring("Remove Entry", "Enter type (reminder/event/task):").lower()

        index = self.choose_entry(entry_type, selected_date, "remove")
        if index is not None:
            confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove this {entry_type}?")
            if confirm:
                del self.calendars[self.current_calendar][f"{entry_type}s"][index]
                messagebox.showinfo("Success", f"{entry_type.capitalize()} removed!")
                self.display_selected_date_content()

    def edit_entry(self):
        if not self.current_calendar:
            messagebox.showwarning("Warning", "Please select a calendar first!")
            return

        selected_date = self.calendar.get_date()
        entry_type = simpledialog.askstring("Edit Entry", "Enter type (reminder/event/task):").lower()

        index = self.choose_entry(entry_type, selected_date, "edit")
        if index is not None:
            new_value = simpledialog.askstring("Edit Entry", "Enter new value (format varies by type):")
            if entry_type == "reminder":
                self.calendars[self.current_calendar]["reminders"][index]["note"] = new_value
            elif entry_type == "event":
                self.calendars[self.current_calendar]["events"][index]["name"] = new_value
            elif entry_type == "task":
                self.calendars[self.current_calendar]["tasks"][index]["task"] = new_value

            messagebox.showinfo("Success", f"{entry_type.capitalize()} updated!")
            self.display_selected_date_content()

    def display_selected_date_content(self, event=None):
        if not self.current_calendar:
            self.display_text.configure(state="normal")
            self.display_text.delete("1.0", tk.END)
            self.display_text.insert("1.0", "No calendar selected.")
            self.display_text.configure(state="disabled")
            return

        selected_date = self.calendar.get_date()
        calendar_data = self.calendars[self.current_calendar]

        content = f"Calendar: {self.current_calendar}\n"
        content += f"Selected Date: {selected_date}\n\n"

        reminders = [reminder for reminder in calendar_data["reminders"] if reminder["date"] == selected_date]
        events = [event for event in calendar_data["events"] if event["date"] == selected_date]
        tasks = [task for task in calendar_data["tasks"] if task["deadline"] == selected_date]

        content += "Reminders:\n" + "\n".join([f"- {reminder['time']}: {reminder['note']}" for reminder in reminders]) + "\n\n"
        content += "Events:\n" + "\n".join([f"- {event['name']}" for event in events]) + "\n\n"
        content += "Tasks:\n" + "\n".join([f"- {task['task']}" for task in tasks]) + "\n\n"

        self.display_text.configure(state="normal")
        self.display_text.delete("1.0", tk.END)
        self.display_text.insert("1.0", content)
        self.display_text.configure(state="disabled")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
