import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Workout and Diet Planner")
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()
        self.age_label = tk.Label(self.window, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.window)
        self.age_entry.pack()
        self.weight_label = tk.Label(self.window, text="Weight:")
        self.weight_label.pack()
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.pack()
        self.height_label = tk.Label(self.window, text="Height:")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.window)
        self.height_entry.pack()
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        self.submit_button.pack()
        
        self.workout_label = tk.Label(self.window, text="")
        self.workout_label.pack(pady=10)
        
        self.diet_label = tk.Label(self.window, text="")
        self.diet_label.pack(pady=10)
        self.result_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, height=20, width=70)
        self.result_text.pack(pady=10)
        
    def submit(self):
        user_data = {
            'name': self.name_entry.get(),
            'age': self.age_entry.get(),
            'weight': self.weight_entry.get(),
            'height': self.height_entry.get()
        }
        
        response = requests.post('http://localhost:5000/', data=user_data)
        
        if response.status_code == 200:
            result = response.json()
            workout_plan = result.get('workout')
            diet_plan = result.get('diet')
            
            self.result_text.delete(1.0, tk.END)
            
            workout_text = "Workout Plan:\n\n"
            for day, exercises in workout_plan.items():
                workout_text += f"{day}:\n" + "\n".join([f"  - {exercise}" for exercise in exercises]) + "\n\n"
            
            diet_text = "Diet Plan:\n\n"
            for day, meals in diet_plan.items():
                diet_text += f"{day}:\n" + "\n".join([f"  - {meal}" for meal in meals]) + "\n\n"

            self.result_text.insert(tk.INSERT, workout_text)
            self.result_text.insert(tk.INSERT, diet_text)
        else:
            messagebox.showerror("Error", "Failed to generate workout and diet plan")



    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = GUI()
    gui.run()