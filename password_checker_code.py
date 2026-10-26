import re
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PasswordCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Strength Checker")
        self.geometry("450x520")
        self.resizable(False, False)

        self.show_password = False

        self.main_frame = ctk.CTkFrame(self, corner_radius=12)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Password Strength Checker", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.title_label.pack(pady=(25, 5))

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame, 
            text="Enter a password below to test its strength", 
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        self.subtitle_label.pack(pady=(0, 20))

        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_frame.pack(fill="x", padx=30, pady=10)

        self.password_entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="Enter password...",
            show="*",
            height=40,
            font=ctk.CTkFont(size=14)
        )
        self.password_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.password_entry.bind("<KeyRelease>", self.evaluate_password)

        self.toggle_btn = ctk.CTkButton(
            self.input_frame, 
            text="👁", 
            width=40, 
            height=40,
            font=ctk.CTkFont(size=16),
            command=self.toggle_password_visibility
        )
        self.toggle_btn.pack(side="right")

        self.progress_bar = ctk.CTkProgressBar(self.main_frame, height=8, corner_radius=4)
        self.progress_bar.pack(fill="x", padx=30, pady=(15, 5))
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(
            self.main_frame, 
            text="Strength: Empty", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="gray"
        )
        self.status_label.pack(pady=5)

        self.checklist_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.checklist_frame.pack(fill="both", expand=True, padx=40, pady=15)

        self.rules = {
            "length": "At least 8 characters long",
            "upper": "Contains an uppercase letter (A-Z)",
            "lower": "Contains a lowercase letter (a-z)",
            "digit": "Contains at least one number (0-9)",
            "special": "Contains a special character (@, #, $, etc.)"
        }

        self.labels = {}
        for key, text in self.rules.items():
            lbl = ctk.CTkLabel(
                self.checklist_frame, 
                text=f"❌  {text}", 
                anchor="w",
                font=ctk.CTkFont(size=13),
                text_color="#e74c3c"
            )
            lbl.pack(fill="x", pady=4)
            self.labels[key] = lbl

    def toggle_password_visibility(self):
        if self.show_password:
            self.password_entry.configure(show="*")
            self.toggle_btn.configure(text="👁")
            self.show_password = False
        else:
            self.password_entry.configure(show="")
            self.toggle_btn.configure(text="🙈")
            self.show_password = True

    def evaluate_password(self, event=None):
        pwd = self.password_entry.get()
        
        if not pwd:
            self.progress_bar.set(0)
            self.progress_bar.configure(progress_color="gray")
            self.status_label.configure(text="Strength: Empty", text_color="gray")
            for lbl in self.labels.values():
                lbl.configure(text=f"❌  {lbl.cget('text')[3:]}", text_color="#e74c3c")
            return

        checks = {
            "length": len(pwd) >= 8,
            "upper": bool(re.search(r"[A-Z]", pwd)),
            "lower": bool(re.search(r"[a-z]", pwd)),
            "digit": bool(re.search(r"\d", pwd)),
            "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd))
        }

        score = 0
        for key, passed in checks.items():
            lbl = self.labels[key]
            text = self.rules[key]
            if passed:
                lbl.configure(text=f"✔  {text}", text_color="#2ecc71")
                score += 1
            else:
                lbl.configure(text=f"❌  {text}", text_color="#e74c3c")

        if score <= 2:
            self.status_label.configure(text="Strength: Weak", text_color="#e74c3c")
            self.progress_bar.configure(progress_color="#e74c3c")
            self.progress_bar.set(0.25)
        elif score <= 4:
            self.status_label.configure(text="Strength: Medium", text_color="#f39c12")
            self.progress_bar.configure(progress_color="#f39c12")
            self.progress_bar.set(0.5)
        elif score == 5 and len(pwd) <= 11:
            self.status_label.configure(text="Strength: Strong", text_color="#2ecc71")
            self.progress_bar.configure(progress_color="#2ecc71")
            self.progress_bar.set(0.75)
        elif score == 5 and len(pwd) > 11:
            self.status_label.configure(text="Strength: Very Strong", text_color="#1abc9c")
            self.progress_bar.configure(progress_color="#1abc9c")
            self.progress_bar.set(1.0)

if __name__ == "__main__":
    app = PasswordCheckerApp()
    app.mainloop()
