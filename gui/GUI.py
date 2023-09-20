import tkinter as tk
from tkinter import filedialog, messagebox

class PathSelector:
    def __init__(self, master, var_name):
        self.var_name = var_name
        self.frame = tk.Frame(master)
        self.frame.pack(pady=3, fill=tk.X)


        self.btn = tk.Button(self.frame, text="Select Directory", command=self.select_directory)
        self.btn.grid(row=0, column=1, sticky=tk.E)
        

        self.entry = tk.Entry(self.frame, width=20)
        self.entry.grid(row=0, column=0, sticky=tk.E, padx=10)
        

        self.label = tk.Label(self.frame, text=f"{self.var_name}")
        self.label.grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        
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
        self.frame.pack(pady=3, fill=tk.X)
        
        self.label = tk.Label(self.frame, text=f"{self.var_name}")
        self.label.grid(row=0, column=2, sticky=tk.W, padx=(0, 10))
        
        self.entry = tk.Entry(self.frame, width=20)
        self.entry.grid(row=0, column=0, padx=10)
        
        self.btn = tk.Button(self.frame, text="Select File", command=self.select_file)
        self.btn.grid(row=0, column=1, sticky=tk.W)
        
    def select_file(self):
        file_name = filedialog.askopenfilename()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, file_name)

    def get_file(self):
        return self.entry.get()

class CheckbuttonSelector:
    def __init__(self, master, var_name):
        self.var_name = var_name
        self.var = tk.IntVar()  # We'll use this to get the checkbutton's value
        self.frame = tk.Frame(master)
        self.frame.pack(pady=3, fill=tk.X)
        
        self.checkbtn = tk.Checkbutton(self.frame, text=var_name, variable=self.var)
        self.checkbtn.grid(row=0, column=0, sticky=tk.W)

    def is_checked(self):
        return bool(self.var.get())

def format_var_name(name):
    return name.replace(" ", "_").lower()

def run_gui():
    app = tk.Tk()
    app.title("CellProfiler GUI")

    selectors = [
        CheckbuttonSelector(app,"Split Image"),
        PathSelector(app, "Input Folder"),

        CheckbuttonSelector(app,"CellProfiler"),
        PathSelector(app, "CellProfiler Pipeline Folder"),
        FileSelector(app, "Pipeline File"),

        CheckbuttonSelector(app,"CellPose"),
        PathSelector(app, "Cellpose Module Folder"),
        FileSelector(app, "Module File"),

        PathSelector(app,"Output Directory")
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
                    # return
                variables[formatted_var_name] = path
                selected_data[formatted_var_name] = path

            elif isinstance(selector, FileSelector):
                file_name = selector.get_file()
                if not file_name:
                    messagebox.showwarning("Error", f"Please select a file for {selector.var_name}.")
                    # return
                variables[formatted_var_name] = file_name
                selected_data[formatted_var_name] = file_name
            
            elif isinstance(selector, CheckbuttonSelector):
                selected_data[formatted_var_name] = selector.is_checked()

        results_container['data'] = selected_data
        app.quit()  # This will break the mainloop without destroying widgets

    store_btn = tk.Button(app, text="OK", command=store_variable)
    store_btn.pack(pady=20)
    app.mainloop()

    data = results_container['data']
    # app.destroy()  # Destroy app after extracting data
    return data

if __name__ == "__main__":
    data = run_gui()
    print("Selected Data:")
    for key, value in data.items():
        print(f"{key}: {value}")
