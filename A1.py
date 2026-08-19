import tkinter as tk
from tkinter import ttk, messagebox

class DenominationCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("💰 Denomination Calculator")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        
        # Set dark theme colors
        self.colors = {
            'bg': '#0f0e17',
            'bg2': '#1a1a2e',
            'fg': '#fffffe',
            'fg2': '#a7a9be',
            'accent': '#00d4ff',
            'accent2': '#ff8906',
            'card': '#16213e',
            'card2': '#1e2a4a',
            'input': '#0f3460',
            'hover': '#00b4d8',
            'success': '#00d484',
            'warning': '#ffb703'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Denomination data (in cents)
        self.denominations = [
            (10000, "💰 $100", "💵"),
            (5000, "💰 $50", "💵"),
            (2000, "💰 $20", "💵"),
            (1000, "💰 $10", "💵"),
            (500, "💰 $5", "💵"),
            (200, "💰 $2", "🪙"),
            (100, "💰 $1", "🪙"),
            (25, "🪙 25¢", "🪙"),
            (10, "🪙 10¢", "🪙"),
            (5, "🪙 5¢", "🪙"),
            (1, "🪙 1¢", "🪙"),
        ]
        
        # Track current page
        self.current_page = 'home'
        
        # Create main container
        self.main_container = tk.Frame(self.root, bg=self.colors['bg'])
        self.main_container.pack(fill='both', expand=True)
        
        # Show home page initially
        self.show_home()
        
    def clear_main_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
    
    def show_home(self):
        self.current_page = 'home'
        self.clear_main_container()
        
        # Header
        header_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        header_frame.pack(pady=(30, 10), fill='x')
        
        title_label = tk.Label(
            header_frame,
            text="🧾 Denomination Calculator",
            font=('Segoe UI', 28, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['accent']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Break any amount into bills and coins instantly",
            font=('Segoe UI', 12),
            bg=self.colors['bg'],
            fg=self.colors['fg2']
        )
        subtitle_label.pack(pady=(5, 20))
        
        # Stats Cards
        stats_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        stats_frame.pack(pady=10, padx=40, fill='x')
        
        # Create 3 stat cards in a row
        stats_data = [
            ("💵", "11", "Denominations", self.colors['accent']),
            ("🪙", "6", "Coins", self.colors['accent2']),
            ("💎", "5", "Bills", self.colors['success']),
        ]
        
        for emoji, number, label, color in stats_data:
            card = tk.Frame(
                stats_frame,
                bg=self.colors['card'],
                relief='flat',
                highlightthickness=1,
                highlightcolor=self.colors['bg2']
            )
            card.pack(side='left', expand=True, fill='both', padx=5, pady=5)
            
            emoji_label = tk.Label(
                card,
                text=emoji,
                font=('Segoe UI', 24),
                bg=self.colors['card'],
                fg=color
            )
            emoji_label.pack(pady=(10, 0))
            
            number_label = tk.Label(
                card,
                text=number,
                font=('Segoe UI', 20, 'bold'),
                bg=self.colors['card'],
                fg=self.colors['fg']
            )
            number_label.pack()
            
            desc_label = tk.Label(
                card,
                text=label,
                font=('Segoe UI', 10),
                bg=self.colors['card'],
                fg=self.colors['fg2']
            )
            desc_label.pack(pady=(0, 10))
        
        # Quick Start Button
        start_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        start_frame.pack(pady=30)
        
        start_btn = tk.Button(
            start_frame,
            text="🚀 Start Calculating",
            font=('Segoe UI', 16, 'bold'),
            bg=self.colors['accent'],
            fg='#000000',
            relief='flat',
            cursor='hand2',
            padx=40,
            pady=15,
            command=self.show_calculator
        )
        start_btn.pack()
        
        # Features section
        features_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        features_frame.pack(pady=20, padx=40, fill='x')
        
        features_label = tk.Label(
            features_frame,
            text="✨ Features",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        features_label.pack(pady=(0, 10))
        
        features_grid = tk.Frame(features_frame, bg=self.colors['bg'])
        features_grid.pack(fill='x')
        
        features_list = [
            ("💨", "Quick amount presets"),
            ("🎯", "Instant breakdown"),
            ("🔄", "Clear & recalculate"),
            ("📱", "Scrollable results"),
            ("⌨️", "Keyboard shortcuts"),
            ("🎨", "Dark theme"),
        ]
        
        # Create a 3-column grid
        for i, (emoji, text) in enumerate(features_list):
            row = i // 3
            col = i % 3
            
            feature = tk.Frame(
                features_grid,
                bg=self.colors['card2'],
                relief='flat'
            )
            feature.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            features_grid.grid_columnconfigure(col, weight=1)
            
            feature_label = tk.Label(
                feature,
                text=f"{emoji}  {text}",
                font=('Segoe UI', 10),
                bg=self.colors['card2'],
                fg=self.colors['fg2'],
                pady=8
            )
            feature_label.pack()
        
        # Footer
        footer_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        footer_frame.pack(side='bottom', pady=20)
        
        footer_label = tk.Label(
            footer_frame,
            text="Made with ❤️ for quick cash breakdowns",
            font=('Segoe UI', 9),
            bg=self.colors['bg'],
            fg=self.colors['fg2']
        )
        footer_label.pack()
    
    def show_calculator(self):
        self.current_page = 'calculator'
        self.clear_main_container()
        
        # Back button
        top_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        top_frame.pack(pady=(15, 5), padx=30, fill='x')
        
        back_btn = tk.Button(
            top_frame,
            text="← Home",
            font=('Segoe UI', 10),
            bg=self.colors['card'],
            fg=self.colors['fg'],
            relief='flat',
            cursor='hand2',
            padx=15,
            pady=5,
            command=self.show_home
        )
        back_btn.pack(side='left')
        
        # Title
        calc_title = tk.Label(
            top_frame,
            text="🧾 Calculator",
            font=('Segoe UI', 18, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['accent']
        )
        calc_title.pack(side='left', padx=(20, 0))
        
        # Input Frame
        input_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        input_frame.pack(pady=10, padx=30, fill='x')
        
        # Amount label
        amount_label = tk.Label(
            input_frame,
            text="Enter Amount:",
            font=('Segoe UI', 12, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        amount_label.pack(anchor='w')
        
        # Input row
        input_row = tk.Frame(input_frame, bg=self.colors['bg'])
        input_row.pack(fill='x', pady=(5, 10))
        
        # Dollar sign
        dollar_label = tk.Label(
            input_row,
            text="$",
            font=('Segoe UI', 16, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['accent']
        )
        dollar_label.pack(side='left', padx=(0, 5))
        
        # Entry
        self.amount_var = tk.StringVar()
        self.amount_entry = tk.Entry(
            input_row,
            textvariable=self.amount_var,
            font=('Segoe UI', 14),
            bg=self.colors['input'],
            fg=self.colors['fg'],
            insertbackground=self.colors['accent'],
            relief='flat',
            highlightthickness=2,
            highlightcolor=self.colors['accent'],
            highlightbackground=self.colors['input']
        )
        self.amount_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.amount_entry.bind('<Return>', lambda e: self.calculate())
        
        # Calculate button
        self.calc_btn = tk.Button(
            input_row,
            text="Calculate",
            font=('Segoe UI', 11, 'bold'),
            bg=self.colors['accent'],
            fg='#000000',
            relief='flat',
            cursor='hand2',
            padx=20,
            pady=8,
            command=self.calculate
        )
        self.calc_btn.pack(side='left')
        
        # Quick amount buttons
        quick_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        quick_frame.pack(pady=(0, 15), padx=30, fill='x')
        
        quick_label = tk.Label(
            quick_frame,
            text="⚡ Quick amounts:",
            font=('Segoe UI', 9),
            bg=self.colors['bg'],
            fg=self.colors['fg2']
        )
        quick_label.pack(anchor='w', pady=(0, 5))
        
        quick_btns_frame = tk.Frame(quick_frame, bg=self.colors['bg'])
        quick_btns_frame.pack(fill='x')
        
        quick_amounts = [19.99, 42.50, 99.99, 127.30, 250.75, 999.99]
        for amount in quick_amounts:
            btn = tk.Button(
                quick_btns_frame,
                text=f"${amount}",
                font=('Segoe UI', 9),
                bg=self.colors['card'],
                fg=self.colors['fg'],
                relief='flat',
                cursor='hand2',
                padx=10,
                pady=4,
                command=lambda a=amount: self.set_quick_amount(a)
            )
            btn.pack(side='left', padx=(0, 5))
        
        # Result Frame with scrollbar
        result_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        result_frame.pack(pady=(0, 20), padx=30, fill='both', expand=True)
        
        result_label = tk.Label(
            result_frame,
            text="📊 Breakdown:",
            font=('Segoe UI', 11, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        result_label.pack(anchor='w', pady=(0, 10))
        
        # Canvas for scrolling
        canvas_frame = tk.Frame(result_frame, bg=self.colors['card'])
        canvas_frame.pack(fill='both', expand=True)
        
        self.canvas = tk.Canvas(
            canvas_frame,
            bg=self.colors['card'],
            highlightthickness=0
        )
        scrollbar = ttk.Scrollbar(
            canvas_frame,
            orient='vertical',
            command=self.canvas.yview
        )
        
        self.result_display = tk.Frame(
            self.canvas,
            bg=self.colors['card']
        )
        
        self.canvas.create_window((0, 0), window=self.result_display, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind mousewheel to scroll
        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
        
        self.canvas.bind_all('<MouseWheel>', on_mousewheel)
        
        # Update scroll region
        def configure_scroll_region(event):
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
        self.result_display.bind('<Configure>', configure_scroll_region)
        
        # Clear button at bottom
        bottom_frame = tk.Frame(self.main_container, bg=self.colors['bg'])
        bottom_frame.pack(pady=(0, 20))
        
        clear_btn = tk.Button(
            bottom_frame,
            text="🗑️ Clear All",
            font=('Segoe UI', 10),
            bg='#cc3333',
            fg='white',
            relief='flat',
            cursor='hand2',
            padx=15,
            pady=6,
            command=self.clear
        )
        clear_btn.pack()
        
        # Initial state
        self.show_empty_state()
    
    def set_quick_amount(self, amount):
        self.amount_var.set(f"{amount:.2f}")
        self.calculate()
        
    def calculate(self):
        try:
            amount = float(self.amount_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number, bruv! 💀")
            return
        
        if amount < 0:
            messagebox.showerror("Invalid Input", "Amount can't be negative, bruv! 💀")
            return
        
        if amount == 0:
            self.show_zero_state()
            return
        
        # Convert to cents (fix floating point)
        total_cents = int(round(amount * 100))
        
        # Clear previous results
        for widget in self.result_display.winfo_children():
            widget.destroy()
        
        # Show total
        total_frame = tk.Frame(
            self.result_display,
            bg=self.colors['card'],
            relief='flat'
        )
        total_frame.pack(fill='x', pady=(0, 15))
        
        total_label = tk.Label(
            total_frame,
            text=f"Total: $ {total_cents/100:.2f}",
            font=('Segoe UI', 18, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['accent']
        )
        total_label.pack()
        
        # Calculate and display denominations
        remaining = total_cents
        has_items = False
        
        for value, name, emoji in self.denominations:
            if remaining >= value:
                count = remaining // value
                remaining %= value
                has_items = True
                
                item_frame = tk.Frame(
                    self.result_display,
                    bg=self.colors['card'],
                    relief='flat',
                    pady=5
                )
                item_frame.pack(fill='x', pady=1)
                
                # Add a subtle line
                if has_items:
                    line = tk.Frame(
                        item_frame,
                        bg='#2a2a4a',
                        height=1
                    )
                    line.pack(fill='x', pady=(0, 5))
                
                # Denomination display
                denom_frame = tk.Frame(
                    item_frame,
                    bg=self.colors['card']
                )
                denom_frame.pack(fill='x', padx=5)
                
                # Left: emoji + name
                left_label = tk.Label(
                    denom_frame,
                    text=f"{emoji}  {name}",
                    font=('Segoe UI', 11),
                    bg=self.colors['card'],
                    fg=self.colors['fg']
                )
                left_label.pack(side='left')
                
                # Right: count with highlight
                count_text = f"× {count}"
                count_color = self.colors['accent'] if count > 0 else '#666666'
                count_label = tk.Label(
                    denom_frame,
                    text=count_text,
                    font=('Segoe UI', 13, 'bold'),
                    bg=self.colors['card'],
                    fg=count_color
                )
                count_label.pack(side='right')
        
        if remaining > 0:
            # Should never happen, but just in case
            error_frame = tk.Frame(
                self.result_display,
                bg=self.colors['card']
            )
            error_frame.pack(fill='x', pady=5)
            error_label = tk.Label(
                error_frame,
                text=f"⚠️ Leftover: {remaining} cents (math error)",
                font=('Segoe UI', 10),
                bg=self.colors['card'],
                fg='#ff6666'
            )
            error_label.pack()
        
        # Update scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def show_empty_state(self):
        for widget in self.result_display.winfo_children():
            widget.destroy()
        
        empty_frame = tk.Frame(
            self.result_display,
            bg=self.colors['card']
        )
        empty_frame.pack(expand=True, fill='both')
        
        empty_label = tk.Label(
            empty_frame,
            text="💵\nEnter an amount above\nand click Calculate",
            font=('Segoe UI', 14),
            bg=self.colors['card'],
            fg='#666688',
            justify='center'
        )
        empty_label.pack(expand=True)
        
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def show_zero_state(self):
        for widget in self.result_display.winfo_children():
            widget.destroy()
        
        zero_frame = tk.Frame(
            self.result_display,
            bg=self.colors['card']
        )
        zero_frame.pack(expand=True, fill='both')
        
        zero_label = tk.Label(
            zero_frame,
            text="✨\nAmount is $0.00\nNothing to break down, bruv!",
            font=('Segoe UI', 14),
            bg=self.colors['card'],
            fg='#666688',
            justify='center'
        )
        zero_label.pack(expand=True)
        
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def clear(self):
        self.amount_var.set("")
        self.amount_entry.focus()
        self.show_empty_state()


def main():
    root = tk.Tk()
    app = DenominationCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()