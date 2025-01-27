import psutil
import tkinter as tk
import winsound  # Import the winsound module for sound notifications

# Function to check battery status
def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged

    # Trigger the message when battery is charging and above 60%
    if charging and percent > 90:
        winsound.PlaySound("C:\\Users\\NIRAJ\\Desktop\\bettery\\more.wav", winsound.SND_FILENAME)  # Play custom sound
        show_message(
            f"Battery is at {percent}%!\nPlease unplug the charger.",
            "Unplug Alert",
            bg_color="#E8F5E9",  # Light green background
            button_color="#388E3C",  # Green button
            hover_color="#4CAF50"  # Lighter green on hover
        )
    # Trigger the message when battery is not charging and below 95%
    elif not charging and percent < 25:
        winsound.PlaySound("C:\\Users\\NIRAJ\\Desktop\\bettery\\less.wav", winsound.SND_FILENAME)  # Play custom sound
        show_message(
            f"Battery is critically low at {percent}%!\nPlease plug in the charger.",
            "Low Battery Alert",
            bg_color="#FFEBEE",  # Light red background
            button_color="#D32F2F",  # Red button
            hover_color="#E53935"  # Lighter red on hover
        )

# Function to display the styled message
def show_message(message, title, bg_color, button_color, hover_color):
    # Create the main window
    root = tk.Tk()
    root.title(title)

    # Make the window always on top
    root.attributes("-topmost", True)

    # Set window size and center it on the screen
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = screen_height // 2 - window_height // 2
    position_left = screen_width // 2 - window_width // 2
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')
    root.config(bg=bg_color)  # Background color based on alert type

    # Create a canvas widget for the background effect
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg=bg_color, bd=0, highlightthickness=0)
    canvas.pack()

    # Create a simple, rounded message box with a white background
    canvas.create_oval(20, 20, window_width - 20, window_height - 20, fill='#FFFFFF', outline='#D0D0D0', width=1)

    # Add a frame for better layout and padding
    frame = tk.Frame(root, bg='#FFFFFF', padx=25, pady=25)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create a label with the message
    label = tk.Label(frame, text=message, font=("Roboto", 14, "normal"), fg='#333333', bg='#FFFFFF', justify="center")
    label.grid(row=0, column=0, pady=15)

    # Button hover effects
    def on_enter(event):
        button.config(bg=hover_color, fg='white')

    def on_leave(event):
        button.config(bg=button_color, fg='white')

    # Button design - Rounded corners with flat style
    button = tk.Button(frame, text="Close", font=("Roboto", 12, "bold"), fg="white", bg=button_color, relief="flat", width=15, height=2, command=root.destroy)
    button.grid(row=1, column=0, pady=10)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    # Run the Tkinter event loop to display the window
    root.mainloop()

# Main execution to check the battery status
if __name__ == "__main__":
    check_battery()
