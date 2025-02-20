import tkinter as tk
from tkinter import ttk
import fitz  # PyMuPDF
from PIL import Image, ImageTk

# Change Path to your Desktop's Directories
FORMS = {
    "Rubric": r"D:\Applications\Coding\DesignForms\Design Forms\FM-EEC-15-03_Design Proposal Rubric.pdf",
    "Recommendation Form": r"D:\Applications\Coding\DesignForms\Design Forms\FM-EEC-18-00_Culiminating-Design-Recommendation-Form.pdf",
    "Conformity of Revisions": r"D:\Applications\Coding\DesignForms\Design Forms\FM-EEC-21-00_Design-Conformity-of-Revisions-Form.pdf",
    "Billing Form": r"D:\Applications\Coding\DesignForms\Design Forms\FM-EEC-25_Design-Oral-Presentation-and-Billing-Form.pdf",
}

THESIS_FORMS = {
    "Rubric": r"D:\Applications\Coding\DesignForms\Thesis Forms\FM-EEC-05-02 THESIS 1 RUBRIC .pdf",
    "Recommendation Form": r"D:\Applications\Coding\DesignForms\Thesis Forms\FM-EEC-16-02  Recommendation Form.pdf",
    "Conformity of Revisions": r"D:\Applications\Coding\DesignForms\Thesis Forms\FM-EEC-17-02 Conformity of Revisions.pdf",
    "Billing Form": r"D:\Applications\Coding\DesignForms\Thesis Forms\FM-EEC-01-03-Thesis Oral Presentation and Billing Form.pdf",
}

class DesignFormsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Design Forms Vending Machine")
        self.root.state("zoomed")
        self.current_frame = None 
        self.create_main_menu()  

    def clear_frame(self):
        """Remove all widgets from the current frame before switching screens"""
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.pack_forget()

    def create_main_menu(self):
        """Create the main menu with form selection buttons"""
        self.clear_frame() 
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

       
        label = tk.Label(self.current_frame, text="Design Forms Vending Machine", font=("Arial", 24, "bold"))
        label.pack(pady=20)

        # Design Forms Section
        design_label = tk.Label(self.current_frame, text="Design Forms", font=("Arial", 18, "bold"))
        design_label.pack(pady=10)
        
        for form_name, file_path in FORMS.items():
            button = ttk.Button(self.current_frame, text=form_name, command=lambda path=file_path: self.show_preview(path))
            button.pack(pady=5, ipadx=10, ipady=5, fill=tk.X, padx=50)

        # Thesis Forms Section
        thesis_label = tk.Label(self.current_frame, text="Thesis Forms", font=("Arial", 18, "bold"))
        thesis_label.pack(pady=10)
        
        for form_name, file_path in THESIS_FORMS.items():
            button = ttk.Button(self.current_frame, text=form_name, command=lambda path=file_path: self.show_preview(path))
            button.pack(pady=5, ipadx=10, ipady=5, fill=tk.X, padx=50)
        
        # Exit Fullscreen Button
        exit_button = ttk.Button(self.current_frame, text="Exit Fullscreen", command=self.exit_fullscreen)
        exit_button.pack(pady=20, ipadx=10, ipady=5, side=tk.BOTTOM, anchor='se')

    def show_preview(self, file_path):
        """Show the PDF preview on the same window"""
        self.clear_frame() 
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        # Convert first page of PDF to an image
        doc = fitz.open(file_path)
        images = []
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) 
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        tk_images = []
        for img in images:
            img.thumbnail((screen_width - 100, screen_height - 200), Image.LANCZOS)
            tk_images.append(ImageTk.PhotoImage(img))

        # Display images
        for tk_img in tk_images:
            pdf_label = tk.Label(self.current_frame, image=tk_img)
            pdf_label.image = tk_img  # Keep reference
            pdf_label.pack(pady=5)

        # Return Button
        return_button = ttk.Button(self.current_frame, text="Return to Start", command=self.create_main_menu)
        return_button.pack(pady=20, ipadx=10, ipady=10)

    def exit_fullscreen(self):
        """Exit fullscreen mode"""
        self.root.attributes('-fullscreen', False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DesignFormsApp(root)
    root.mainloop()
