import tkinter as tk
from tkinter import filedialog, messagebox

class PathSelector:
    def __init__(self, master, var_name):
        self.var_name = var_name
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)
        
        self.label = tk.Label(self.frame, text=f"{self.var_name}:")
        self.label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        
        self.btn = tk.Button(self.frame, text="Select Directory", command=self.select_directory)
        self.btn.pack(side=tk.LEFT)
        
    def select_directory(self):
        path = filedialog.askdirectory()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, path)

    def get_path(self):
        return self.entry.get()

#define FileSelector

class FileSelector:
    def __init__(self, master, var_name):
        self.var_name = var_name
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)
        
        self.label = tk.Label(self.frame, text=f"{self.var_name}:")
        self.label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        
        self.btn = tk.Button(self.frame, text="Select File", command=self.select_file)
        self.btn.pack(side=tk.LEFT)
        
    def select_file(self):
        file_name = filedialog.askopenfilename()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, file_name)

    def get_file(self):
        return self.entry.get()

def format_var_name(name):
    return name.replace(" ", "_").lower()

def run_gui():
    app = tk.Tk()
    app.title("CellProfiler GUI")

    selectors = [
        PathSelector(app, "Input Folder"),
        PathSelector(app, "Cellpose Module Folder"),
        PathSelector(app, "CellProfiler Pipeline Folder"),
        FileSelector(app, "Module File"),
        FileSelector(app, "Pipeline File")
    ]

    results_container = {'data': None}

    def store_variable():
        variables = {}
        selected_data = {}
        for selector in selectors:
            formatted_var_name = format_var_name(selector.var_name)
            
            if isinstance(selector, PathSelector):
                path = selector.get_path()
                if not path:
                    messagebox.showwarning("Error", f"Please select a path for {selector.var_name}.")
                    return
                variables[formatted_var_name] = path
                selected_data[formatted_var_name] = path

            elif isinstance(selector, FileSelector):
                file_name = selector.get_file()
                if not file_name:
                    messagebox.showwarning("Error", f"Please select a file for {selector.var_name}.")
                    return
                variables[formatted_var_name] = file_name
                selected_data[formatted_var_name] = file_name

        results_container['data'] = selected_data
        app.quit()  # This will break the mainloop without destroying widgets

    store_btn = tk.Button(app, text="OK", command=store_variable)
    store_btn.pack(pady=20)
    app.mainloop()

    data = results_container['data']
    app.destroy()  # Destroy app after extracting data
    return data

if __name__ == "__main__":
    data = run_gui()
    print("Selected Data:")
    for key, value in data.items():
        print(f"{key}: {value}")
