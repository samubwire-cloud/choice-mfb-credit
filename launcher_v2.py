"""
Choice MFB Credit Intelligence v2.0 — Windows Launcher
Shows a branded splash screen, starts Streamlit, opens the browser.
"""
import subprocess, threading, webbrowser, time, sys, os, socket

APP_PORT = 8501
APP_URL  = f"http://localhost:{APP_PORT}"

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

APP_FILE = os.path.join(BASE_DIR, "choice_mfb_credit_app_v2.py")

def port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def wait_for_server(port, timeout=45):
    start = time.time()
    while time.time() - start < timeout:
        if port_in_use(port): return True
        time.sleep(0.5)
    return False

def launch():
    if port_in_use(APP_PORT):
        webbrowser.open(APP_URL)
        return

    try:
        import tkinter as tk
        from tkinter import ttk

        root = tk.Tk()
        root.title("Choice MFB Credit Intelligence")
        root.geometry("460x260")
        root.resizable(False, False)
        root.configure(bg="#110837")
        root.overrideredirect(True)

        # Centre on screen
        root.update_idletasks()
        x = (root.winfo_screenwidth()  - 460) // 2
        y = (root.winfo_screenheight() - 260) // 2
        root.geometry(f"+{x}+{y}")

        # Try to embed logo
        try:
            import base64
            from PIL import Image, ImageTk
            import io as _io
            logo_path = os.path.join(BASE_DIR, "choice_logo.png")
            if os.path.exists(logo_path):
                img = Image.open(logo_path).resize((220, 50), Image.LANCZOS)
                logo_img = ImageTk.PhotoImage(img)
                logo_lbl = tk.Label(root, image=logo_img, bg="#110837")
                logo_lbl.image = logo_img
                logo_lbl.pack(pady=(30, 5))
            else:
                raise FileNotFoundError
        except:
            tk.Label(root, text="ChoiceBank MICROFINANCE",
                     font=("Segoe UI", 16, "bold"), fg="white",
                     bg="#110837").pack(pady=(30, 5))

        tk.Label(root, text="Credit Intelligence Platform",
                 font=("Segoe UI", 10), fg="#A8C6E8", bg="#110837").pack()
        tk.Label(root, text="", bg="#110837").pack()

        style = ttk.Style()
        style.theme_use('default')
        style.configure("C.Horizontal.TProgressbar",
                        troughcolor="#0D2040", background="#DA2A2F", thickness=6)

        pbar = ttk.Progressbar(root, style="C.Horizontal.TProgressbar",
                                orient="horizontal", length=380, mode="indeterminate")
        pbar.pack(padx=40, pady=8)
        pbar.start(10)

        sv = tk.StringVar(value="Starting application...")
        tk.Label(root, textvariable=sv,
                 font=("Segoe UI", 8), fg="#A8C6E8", bg="#110837").pack()

        tk.Label(root, text="Samuel · Head of Credit · Riverside Branch",
                 font=("Segoe UI", 7), fg="#4A6B8A", bg="#110837").pack(side="bottom", pady=10)

        use_splash = True
    except ImportError:
        use_splash = False

    proc = [None]

    def start():
        sv.set("Loading models...") if use_splash else None

        cmd = [sys.executable, "-m", "streamlit", "run", APP_FILE,
               "--server.port", str(APP_PORT),
               "--server.headless", "true",
               "--browser.gatherUsageStats", "false",
               "--theme.primaryColor", "#DA2A2F",
               "--theme.backgroundColor", "#F5F6FA",
               "--theme.secondaryBackgroundColor", "#FFFFFF",
               "--theme.textColor", "#110837"]

        si = None
        if sys.platform == "win32":
            import subprocess as sp
            si = sp.STARTUPINFO()
            si.dwFlags |= sp.STARTF_USESHOWWINDOW
            si.wShowWindow = sp.SW_HIDE

        proc[0] = subprocess.Popen(cmd, startupinfo=si,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)

        if use_splash: sv.set("Waiting for server...")
        if wait_for_server(APP_PORT, 45):
            if use_splash: sv.set("Opening in browser...")
            time.sleep(0.5)
            webbrowser.open(APP_URL)
            time.sleep(1.0)
            if use_splash: root.after(0, root.destroy)
        else:
            if use_splash: sv.set("Startup failed. Please try again.")
            time.sleep(3)
            if use_splash: root.after(0, root.destroy)

    t = threading.Thread(target=start, daemon=True)
    t.start()

    if use_splash:
        root.mainloop()
    else:
        t.join()

if __name__ == "__main__":
    launch()
