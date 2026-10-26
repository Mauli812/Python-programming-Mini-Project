# Password Strength Checker

A modern, real-time desktop security analysis tool built with Python. This application evaluates the structural complexity of user-entered passwords against standard cryptographic baseline rules using regular expressions, providing instantaneous, color-coded visual feedback.

## 👥 Authorship & Project Context
- **Student Name:** Mauli Patel
- **Enrollment Number:** 12502080603011
- **Subject:** Python Programming Project
- **Institution:** ADIT / CVM University

---

## 🚀 Features
- **Real-Time Evaluation:** Intercepts input character streams instantly via asynchronous window event listeners (`<KeyRelease>`).
- **Secure Input Obscuration:** Features a masked text input box (`*`) with a interactive visibility button (`👁` / `🙈`) to toggle plain-text rendering.
- **Dynamic Policy Checklist:** Tracks five separate security criteria simultaneously using intuitive live status badges (❌ / ✔).
- **Multi-Tiered Metrics:** Maps calculated password scores across a four-tiered structural profile matrix (Weak, Medium, Strong, Very Strong).
- **Zero Cloud Footprint:** Operates completely on a local desktop environment without calling external network APIs or cloud logging databases.

---

## 🛠 Core Technologies & Requirements
- **Operating System:** Windows 10/11, macOS 11+, or Linux (Ubuntu/Debian)
- **Language Environment:** Python 3.8 or higher
- **Core Library Dependencies:** 
  - `customtkinter` (v5.0+) - Modern UI component framework with high-DPI scaling and automated theme detection.
  - `re` (Standard Python Library) - Regular expression processing pipeline executing pattern searches in $O(N)$ time complexity.

---

## 📦 Repository Structure
```text
├── 12502080603011_password-strenght-checker-project report.pdf  # Project Documentation Report
├── 12502080603013_Password_Strength_Checker_Presentation.pdf   # Academic Presentation Slides
├── OUTPUT.png                                                    # Application Graphical Interface Screenshot
├── README.md                                                     # Project Documentation & Initial Commit
└── password_checker_code.py                                      # Primary Executable Source Code
```

---

## 📊 Security Grading Matrix

The application evaluates passwords based on 5 parameters: Length ($\ge 8$), Uppercase letters, Lowercase letters, Digits, and Special characters. The aggregated score decides the visual interface output:

| Earned Criteria Count | Length Boundary | Strength Status | Visual UI Accent Color | Normalization Level |
| :---: | :---: | :---: | :---: | :---: |
| **Score $\le$ 2** | Any Length | **Weak** | Red (`#e74c3c`) | `0.25` |
| **Score 3 or 4** | Any Length | **Medium** | Orange (`#f39c12`) | `0.50` |
| **Score == 5** | $\le$ 11 Characters | **Strong** | Green (`#2ecc71`) | `0.75` |
| **Score == 5** | $\ge$ 12 Characters | **Very Strong** | Teal (`#1abc9c`) | `1.00` |

*Note: To reach the maximum safety tier (**Very Strong**), a password must clear all 5 regular expression structural checks and match an extended layout length constraint of 12 or more characters.*

---

## 💻 Source Code (`password_checker_code.py`)

Below is the complete standalone production source code for the application:

```python
import re
import customtkinter as ctk

# Configure look and feel system baseline parameters
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class PasswordCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Define application frame boundaries and identities
        self.title("Password Strength Checker")
        self.geometry("450x520")
        self.resizable(False, False)

        # Initialize core visibility state flags
        self.show_password = False

        # Build main visual container background canvas
        self.main_frame = ctk.CTkFrame(self, corner_radius=12)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Structural Header Elements
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

        # Horizontal layout panel for data input controls
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
        # Anchor evaluation routine directly to real-time keystroke window triggers
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

        # Metric Evaluation Displays
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

        # Transparent enclosure panel for checklist layout strings
        self.checklist_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.checklist_frame.pack(fill="both", expand=True, padx=40, pady=15)

        # Baseline Verification Ruleset Schema
        self.rules = {
            "length": "At least 8 characters long",
            "upper": "Contains an uppercase letter (A-Z)",
            "lower": "Contains a lowercase letter (a-z)",
            "digit": "Contains at least one number (0-9)",
            "special": "Contains a special character (@, #, $, etc.)"
        }

        # Dynamically build visual indicators out of rules schema definitions
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
        """Swaps text box configuration masks dynamically based on state tracking flags."""
        if self.show_password:
            self.password_entry.configure(show="*")
            self.toggle_btn.configure(text="👁")
            self.show_password = False
        else:
            self.password_entry.configure(show="")
            self.toggle_btn.configure(text="🙈")
            self.show_password = True

    def evaluate_password(self, event=None):
        """Processes target string patterns asynchronously and updates visual states."""
        pwd = self.password_entry.get()
        
        # Immediate reset pipeline triggered when input box value is cleared entirely
        if not pwd:
            self.progress_bar.set(0)
            self.progress_bar.configure(progress_color="gray")
            self.status_label.configure(text="Strength: Empty", text_color="gray")
            for lbl in self.labels.values():
                lbl.configure(text=f"❌  {lbl.cget('text')[3:]}", text_color="#e74c3c")
            return

        # Parallel Regex validation engine processing dictionary
        checks = {
            "length": len(pwd) >= 8,
            "upper": bool(re.search(r"[A-Z]", pwd)),
            "lower": bool(re.search(r"[a-z]", pwd)),
            "digit": bool(re.search(r"\d", pwd)),
            "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd))
        }

        # Multi-element checklist UI update iteration routine
        score = 0
        for key, passed in checks.items():
            lbl = self.labels[key]
            text = self.rules[key]
            if passed:
                lbl.configure(text=f"✔  {text}", text_color="#2ecc71")
                score += 1
            else:
                lbl.configure(text=f"❌  {text}", text_color="#e74c3c")

        # Multi-tiered system metric calculation scoring block
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

# Main Application Lifecycle Bootstrap Entrypoint
if __name__ == "__main__":
    app = PasswordCheckerApp()
