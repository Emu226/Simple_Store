import tkinter as tk
from tkinter import ttk

class ScanWindow(tk.Toplevel):
    def __init__(self, parent, scanned_code):
        super().__init__(parent)
        
        # Window configuration
        self.title("Scan Type Selection")
        self.geometry("300x200")
        self.resizable(False, False)
        
        # Make window modal
        self.transient(parent)
        self.grab_set()
        
        # Store scanned code
        self.scanned_code = scanned_code
        self.result = None
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.create_widgets()
        
        # Center window
        self.center_window()

    def create_widgets(self):
        # Header label
        header_label = ttk.Label(
            self,
            text=f"Scanned Code:\n{self.scanned_code}",
            font=("Helvetica", 12),
            justify="center"
        )
        header_label.grid(row=0, column=0, pady=20, padx=10)

        # Button frame
        button_frame = ttk.Frame(self)
        button_frame.grid(row=1, column=0)

        # Configure button styles
        style = ttk.Style()
        style.configure("Action.TButton", padding=10, font=("Helvetica", 10, "bold"))

        # Article button
        article_btn = ttk.Button(
            button_frame,
            text="📦 Article",
            style="Action.TButton",
            command=lambda: self.on_selection("article")
        )
        article_btn.pack(pady=5, padx=20, fill=tk.X)

        # Storage location button
        storage_btn = ttk.Button(
            button_frame,
            text="🏪 Storage Location",
            style="Action.TButton",
            command=lambda: self.on_selection("storage")
        )
        storage_btn.pack(pady=5, padx=20, fill=tk.X)

        # Cancel button
        cancel_btn = ttk.Button(
            button_frame,
            text="❌ Cancel",
            command=self.on_cancel
        )
        cancel_btn.pack(pady=10)

        # Bind keyboard shortcuts
        self.bind("<Escape>", lambda e: self.on_cancel())
        self.bind("a", lambda e: self.on_selection("article"))
        self.bind("s", lambda e: self.on_selection("storage"))

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_selection(self, selection_type):
        self.result = {
            "type": selection_type,
            "code": self.scanned_code
        }
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()

def show_scan_window(parent, scanned_code):
    """
    Shows the scan window and returns the result.
    Returns: dict with type and code or None if cancelled
    """
    scan_window = ScanWindow(parent, scanned_code)
    scan_window.wait_window()
    return scan_window.result