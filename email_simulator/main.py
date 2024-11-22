class EmailSimulatorGUI:


    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Email Simulator GUI")

        # Create a Listbox to display emails
        self.inbox_listbox = tk.Listbox(master)
        self.inbox_listbox.pack(pady=10)

        # Create buttons for actions
        self.populate_button = tk.Button(master, text="Populate Inbox", command=self.populate_inbox)
        self.populate_button.pack(pady=5)

        self.read_button = tk.Button(master, text="Read Email", command=self.read_email)
        self.read_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.pack(pady=5)

        # Initialize the EmailSimulator instance
        self.email_simulator = EmailSimulator()


    def populate_inbox(self):
        # Populate the inbox with sample emails
        self.email_simulator.populate_inbox()
        # Update the Listbox to reflect the changes
        self.update_inbox_listbox()


    def update_inbox_listbox(self):
        # Clear the Listbox
        self.inbox_listbox.delete(0, tk.END)
        # Populate the Listbox with email subjects and read status
        for email in self.email_simulator.inbox:
            self.inbox_listbox.insert(tk.END, f"{email.subject_line} - {'Read' if email.has_been_read else 'Unread'}")


    def read_email(self):
        # Get the selected index from the Listbox
        selected_index = self.inbox_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            # Mark the selected email as read
            self.email_simulator.read_email(selected_index)
            # Show a message box indicating the email has been read
            messagebox.showinfo("Read Email", "Email marked as read.")
            # Update the Listbox to reflect the changes
            self.update_inbox_listbox()
        else:
            # Show a warning if no email is selected
            messagebox.showwarning("Read Email", "Please select an email to read.")

class Email:


    def __init__(self, subject_line):
        # Initialize an email with a subject line and unread status
        self.subject_line = subject_line
        self.has_been_read = False

class EmailSimulator:
    def __init__(self):
        # Initialize an empty inbox
        self.inbox = []


    def populate_inbox(self):
        # Populate the inbox with sample emails
        self.inbox = [Email(f"Subject {i}") for i in range(1, 4)]


    def read_email(self, index):
        # Mark the email at the specified index as read
        if 0 <= index < len(self.inbox):
            selected_email = self.inbox[index]
            selected_email.has_been_read = True

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Initialize the EmailSimulatorGUI
    app = EmailSimulatorGUI(root)
    # Start the Tkinter event loop
    root.mainloop()
