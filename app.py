import tkinter as tk

def spam_filter(content):
    spam_keywords = ['buy', 'discount', 'sale', 'money', 'free', 'offer']
    # Convert content to lowercase for case-insensitive matching
    content_lower = content.lower()
    # Check if any spam keyword is present in the content
    for keyword in spam_keywords:
        if keyword in content_lower:
            # Content is identified as spam
            return True
    # Content is not identified as spam
    return False

def check_spam():
    content_to_check = entry.get()
    if spam_filter(content_to_check):
        pop_up_message("Warning", "This content might be spam.", "red")
    else:
        pop_up_message("No Spam", "Content is not identified as spam.", "green")

def pop_up_message(title, message, color):
    popup = tk.Tk()
    popup.title(title)
    label = tk.Label(popup, text=message, fg=color)
    label.pack(padx=10, pady=10)
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(padx=10, pady=5)
    popup.mainloop()

# Creating a simple GUI using tkinter
root = tk.Tk()
root.title("Spam Filter")
label = tk.Label(root, text="Enter content to check:")
label.pack(padx=10, pady=10)
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)
check_button = tk.Button(root, text="Check Spam", command=check_spam)
check_button.pack(padx=10, pady=5)
root.mainloop()