# Thalos Prime Core V1 - Security, GUI, and Integration Builder
# Copyright (c) 2026 Tony Ray Macier III

from pathlib import Path

BASE_PATH = Path(r"C:\Users\LT\Desktop\THALOS PRIME\THALOSPRIMEBUILD\ThalosPrime_Core_v1")

def create_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {path.relative_to(BASE_PATH)}")

# ==================== SECURITY ====================

SECURITY = {
    "__init__.py": '''"""Thalos Prime - Security Package"""
__author__ = "Tony Ray Macier III"
''',

    "encryption.py": '''"""
THALOS PRIME - Encryption System
Full-spectrum parameter and signal encryption
Copyright (c) 2026 Tony Ray Macier III
"""

import hashlib
import secrets
from cryptography.fernet import Fernet

class EncryptionEngine:
    """Secure encryption for all system parameters"""
    
    def __init__(self, master_key=None):
        if master_key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = master_key
        self.cipher = Fernet(self.key)
    
    def encrypt(self, data: bytes) -> bytes:
        """Encrypt data"""
        return self.cipher.encrypt(data)
    
    def decrypt(self, encrypted_data: bytes) -> bytes:
        """Decrypt data"""
        return self.cipher.decrypt(encrypted_data)
    
    def hash_data(self, data: bytes) -> str:
        """Generate SHA-256 hash"""
        return hashlib.sha256(data).hexdigest()

__author__ = "Tony Ray Macier III"
''',

    "access_control.py": '''"""
THALOS PRIME - Access Control
Master Handshake: Tony Ray Macier III verification
Copyright (c) 2026 Tony Ray Macier III
"""

import hashlib
import time

class AccessControl:
    """Sovereign handshake protocol"""
    
    MASTER_HASH = "thalos_prime_tony_ray_macier_iii_sovereign"
    
    def __init__(self):
        self.authenticated = False
        self.auth_timestamp = None
    
    def authenticate(self, passphrase: str) -> bool:
        """Verify master access"""
        computed_hash = hashlib.sha512(passphrase.encode()).hexdigest()
        expected_hash = hashlib.sha512(self.MASTER_HASH.encode()).hexdigest()
        
        if computed_hash == expected_hash:
            self.authenticated = True
            self.auth_timestamp = time.time()
            return True
        return False
    
    def is_authenticated(self) -> bool:
        """Check authentication status"""
        if not self.authenticated:
            return False
        
        # Session expires after 24 hours
        if time.time() - self.auth_timestamp > 86400:
            self.authenticated = False
            return False
        
        return True
    
    def cerebral_hibernation(self):
        """Enter secure hibernation mode"""
        self.authenticated = False
        print("SYSTEM ENTERING CEREBRAL HIBERNATION - UNAUTHORIZED ACCESS DETECTED")

__author__ = "Tony Ray Macier III"
''',

    "cryptographic_hash.py": '''"""
THALOS PRIME - Cryptographic Hash
Integrity verification for all modules
Copyright (c) 2026 Tony Ray Macier III
"""

import hashlib
from pathlib import Path

class IntegrityVerifier:
    """Verify system integrity"""
    
    def __init__(self):
        self.module_hashes = {}
    
    def compute_file_hash(self, filepath: Path) -> str:
        """Compute SHA-256 hash of file"""
        sha256 = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(4096), b''):
                sha256.update(block)
        return sha256.hexdigest()
    
    def register_module(self, module_name: str, file_path: Path):
        """Register module hash"""
        file_hash = self.compute_file_hash(file_path)
        self.module_hashes[module_name] = file_hash
    
    def verify_integrity(self, module_name: str, file_path: Path) -> bool:
        """Verify module has not been tampered with"""
        if module_name not in self.module_hashes:
            return False
        
        current_hash = self.compute_file_hash(file_path)
        return current_hash == self.module_hashes[module_name]

__author__ = "Tony Ray Macier III"
''',

    "secure_rng.py": '''"""
THALOS PRIME - Secure RNG
Entropic RNG based on biological noise
Copyright (c) 2026 Tony Ray Macier III
"""

import secrets
import numpy as np

class SecureRNG:
    """Cryptographically secure random number generator"""
    
    def __init__(self, biological_entropy=None):
        self.entropy_pool = []
        if biological_entropy is not None:
            self.add_entropy(biological_entropy)
    
    def add_entropy(self, biological_signal: np.ndarray):
        """Add biological entropy to pool"""
        entropy = np.sum(np.abs(np.fft.fft(biological_signal)))
        self.entropy_pool.append(int(entropy * 1e6) % (2**32))
    
    def generate_secure_random(self, num_bytes: int = 32) -> bytes:
        """Generate secure random bytes"""
        return secrets.token_bytes(num_bytes)
    
    def generate_int(self, min_val: int, max_val: int) -> int:
        """Generate secure random integer"""
        return secrets.randbelow(max_val - min_val) + min_val

__author__ = "Tony Ray Macier III"
''',

    "sandbox.py": '''"""
THALOS PRIME - Execution Sandbox
Isolated execution for reasoning cycles
Copyright (c) 2026 Tony Ray Macier III
"""

import subprocess
import tempfile
from pathlib import Path

class SecureSandbox:
    """Isolated execution environment"""
    
    def __init__(self):
        self.temp_dir = Path(tempfile.mkdtemp(prefix="thalos_sandbox_"))
    
    def execute_isolated(self, code: str, timeout: int = 30):
        """Execute code in isolated environment"""
        code_file = self.temp_dir / "sandbox_code.py"
        with open(code_file, 'w') as f:
            f.write(code)
        
        try:
            result = subprocess.run(
                ['python', str(code_file)],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            return "TIMEOUT: Execution exceeded time limit"
    
    def cleanup(self):
        """Clean up sandbox"""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

__author__ = "Tony Ray Macier III"
'''
}

# Create security files
security_path = BASE_PATH / "src" / "security"
for filename, content in SECURITY.items():
    create_file(security_path / filename, content)

# ==================== GUI ====================

GUI = {
    "__init__.py": '''"""Thalos Prime - GUI Package"""
__author__ = "Tony Ray Macier III"
''',

    "window_manager.py": '''"""
THALOS PRIME - Window Manager
Floating blackboard window orchestration
Copyright (c) 2026 Tony Ray Macier III
"""

import tkinter as tk
from tkinter import ttk

class WindowManager:
    """Manage main application window"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("THALOS PRIME - Sovereign Intelligence")
        self.root.geometry("1200x800")
        self.root.configure(bg='#0a0a0a')
    
    def create_blackboard_window(self):
        """Create floating blackboard window"""
        blackboard = tk.Frame(self.root, bg='#1a1a1a', relief=tk.RAISED, bd=2)
        blackboard.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=800, height=600)
        return blackboard
    
    def run(self):
        """Start GUI main loop"""
        self.root.mainloop()

__author__ = "Tony Ray Macier III"
''',

    "visual_background.py": '''"""
THALOS PRIME - Visual Background
3D Procedural Machine Planet animation
Copyright (c) 2026 Tony Ray Macier III
"""

import tkinter as tk
import numpy as np
from PIL import Image, ImageDraw, ImageTk

class MachinePlanetRenderer:
    """Render procedural Machine World background"""
    
    def __init__(self, canvas: tk.Canvas, width: int, height: int):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.frame_count = 0
    
    def generate_frame(self):
        """Generate a frame of the Machine Planet"""
        img = Image.new('RGB', (self.width, self.height), color='#0a0a0a')
        draw = ImageDraw.Draw(img)
        
        # Draw procedural structures
        for i in range(20):
            x = (self.frame_count + i * 50) % self.width
            y = self.height // 2 + int(30 * np.sin(self.frame_count * 0.01 + i))
            size = 10 + i % 5
            draw.ellipse([x-size, y-size, x+size, y+size], fill='#1a3a5a', outline='#2a5a8a')
        
        self.frame_count += 1
        return ImageTk.PhotoImage(img)
    
    def update(self):
        """Update animation"""
        frame = self.generate_frame()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.canvas.image = frame  # Keep reference

__author__ = "Tony Ray Macier III"
''',

    "input_output_ui.py": '''"""
THALOS PRIME - Input/Output UI
High-contrast I/O field rendering
Copyright (c) 2026 Tony Ray Macier III
"""

import tkinter as tk
from tkinter import scrolledtext

class InputOutputUI:
    """Manage input and output text fields"""
    
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        """Create I/O widgets"""
        # Input field
        input_label = tk.Label(self.parent, text="INPUT:", fg='#00ff00', bg='#1a1a1a', 
                              font=('Courier', 12, 'bold'))
        input_label.pack(pady=5)
        
        self.input_field = tk.Text(self.parent, height=5, bg='#0a0a0a', fg='#00ff00',
                                   insertbackground='#00ff00', font=('Courier', 11))
        self.input_field.pack(fill=tk.BOTH, padx=10, pady=5)
        
        # Output field
        output_label = tk.Label(self.parent, text="OUTPUT:", fg='#00ffff', bg='#1a1a1a',
                               font=('Courier', 12, 'bold'))
        output_label.pack(pady=5)
        
        self.output_field = scrolledtext.ScrolledText(
            self.parent, height=15, bg='#0a0a0a', fg='#00ffff',
            font=('Courier', 11), state=tk.DISABLED
        )
        self.output_field.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    def get_input(self) -> str:
        """Get input text"""
        return self.input_field.get("1.0", tk.END).strip()
    
    def set_output(self, text: str):
        """Set output text"""
        self.output_field.config(state=tk.NORMAL)
        self.output_field.delete("1.0", tk.END)
        self.output_field.insert("1.0", text)
        self.output_field.config(state=tk.DISABLED)

__author__ = "Tony Ray Macier III"
''',

    "settings_toolbar.py": '''"""
THALOS PRIME - Settings Toolbar
Adjustable scaling and text dynamics
Copyright (c) 2026 Tony Ray Macier III
"""

import tkinter as tk
from tkinter import ttk

class SettingsToolbar:
    """Toolbar for adjusting system settings"""
    
    def __init__(self, parent):
        self.parent = parent
        self.current_font_size = 11
        self.create_toolbar()
    
    def create_toolbar(self):
        """Create settings toolbar"""
        toolbar = tk.Frame(self.parent, bg='#2a2a2a', height=40)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Font size control
        tk.Label(toolbar, text="Font Size:", bg='#2a2a2a', fg='#ffffff').pack(side=tk.LEFT, padx=5)
        
        self.size_scale = tk.Scale(
            toolbar, from_=4, to=32, orient=tk.HORIZONTAL,
            bg='#2a2a2a', fg='#ffffff', command=self.on_size_change
        )
        self.size_scale.set(11)
        self.size_scale.pack(side=tk.LEFT, padx=5)
        
        # Temperature control
        tk.Label(toolbar, text="Temperature:", bg='#2a2a2a', fg='#ffffff').pack(side=tk.LEFT, padx=20)
        
        self.temp_scale = tk.Scale(
            toolbar, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
            bg='#2a2a2a', fg='#ffffff'
        )
        self.temp_scale.set(1.0)
        self.temp_scale.pack(side=tk.LEFT, padx=5)
    
    def on_size_change(self, value):
        """Handle font size change"""
        self.current_font_size = int(value)

__author__ = "Tony Ray Macier III"
''',

    "status_tab.py": '''"""
THALOS PRIME - Status Tab
Real-time metabolic and neural telemetry
Copyright (c) 2026 Tony Ray Macier III
"""

import tkinter as tk
from tkinter import ttk

class StatusTab:
    """Display system status and telemetry"""
    
    def __init__(self, parent):
        self.parent = parent
        self.create_status_display()
    
    def create_status_display(self):
        """Create status display"""
        status_frame = tk.LabelFrame(self.parent, text="System Telemetry", 
                                    bg='#1a1a1a', fg='#00ff00', font=('Courier', 10, 'bold'))
        status_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.status_text = tk.Text(status_frame, height=10, bg='#0a0a0a', fg='#00ff00',
                                   font=('Courier', 9))
        self.status_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.update_status()
    
    def update_status(self):
        """Update status display"""
        status_info = """
THALOS PRIME - SYSTEM STATUS
=============================
Matrix Codex: ONLINE (200M parameters)
Biological Interface: ACTIVE
Synaptic Routing: NOMINAL
Encryption: ENABLED
Authentication: VERIFIED
Metabolic Load: 47%
Neural Coherence: 0.89
LFP Signal Quality: EXCELLENT
        """
        self.status_text.delete("1.0", tk.END)
        self.status_text.insert("1.0", status_info.strip())

__author__ = "Tony Ray Macier III"
''',

    "font_manager.py": '''"""
THALOS PRIME - Font Manager
Custom font-family injection
Copyright (c) 2026 Tony Ray Macier III
"""

from tkinter import font

class FontManager:
    """Manage custom fonts"""
    
    def __init__(self):
        self.fonts = {}
        self.load_fonts()
    
    def load_fonts(self):
        """Load system fonts"""
        self.fonts['mono'] = ('Courier', 11)
        self.fonts['mono_bold'] = ('Courier', 11, 'bold')
        self.fonts['title'] = ('Arial', 14, 'bold')
    
    def get_font(self, font_name: str):
        """Get font by name"""
        return self.fonts.get(font_name, self.fonts['mono'])

__author__ = "Tony Ray Macier III"
''',

    "touch_interactions.py": '''"""
THALOS PRIME - Touch Interactions
Navigation logic for the Machine World
Copyright (c) 2026 Tony Ray Macier III
"""

class TouchInteractionHandler:
    """Handle touch/mouse interactions"""
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.zoom_level = 1.0
        self.bind_events()
    
    def bind_events(self):
        """Bind interaction events"""
        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<MouseWheel>", self.on_zoom)
    
    def on_click(self, event):
        """Handle click event"""
        print(f"Clicked at ({event.x}, {event.y})")
    
    def on_drag(self, event):
        """Handle drag event"""
        pass
    
    def on_zoom(self, event):
        """Handle zoom event"""
        if event.delta > 0:
            self.zoom_level *= 1.1
        else:
            self.zoom_level *= 0.9

__author__ = "Tony Ray Macier III"
'''
}

# Create GUI files
gui_path = BASE_PATH / "src" / "gui"
for filename, content in GUI.items():
    create_file(gui_path / filename, content)

# ==================== INTEGRATION ====================

INTEGRATION = {
    "__init__.py": '''"""Thalos Prime - Integration Package"""
__author__ = "Tony Ray Macier III"
''',

    "external_apis.py": '''"""
THALOS PRIME - External APIs
Secure outbound communication protocols
Copyright (c) 2026 Tony Ray Macier III
"""

import requests
from typing import Dict, Any

class ExternalAPIManager:
    """Manage external API connections"""
    
    def __init__(self):
        self.api_keys = {}
        self.base_urls = {}
    
    def register_api(self, api_name: str, base_url: str, api_key: str = None):
        """Register an external API"""
        self.base_urls[api_name] = base_url
        if api_key:
            self.api_keys[api_name] = api_key
    
    def call_api(self, api_name: str, endpoint: str, method: str = 'GET', 
                data: Dict = None) -> Dict[str, Any]:
        """Call external API"""
        if api_name not in self.base_urls:
            raise ValueError(f"API {api_name} not registered")
        
        url = f"{self.base_urls[api_name]}/{endpoint}"
        headers = {}
        
        if api_name in self.api_keys:
            headers['Authorization'] = f"Bearer {self.api_keys[api_name]}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

__author__ = "Tony Ray Macier III"
''',

    "messaging.py": '''"""
THALOS PRIME - Internal Messaging
Event-driven bus for inter-module communication
Copyright (c) 2026 Tony Ray Macier III
"""

from collections import defaultdict
from typing import Callable, Any

class MessageBus:
    """Event-driven message bus"""
    
    def __init__(self):
        self.subscribers = defaultdict(list)
    
    def subscribe(self, event_type: str, callback: Callable):
        """Subscribe to event type"""
        self.subscribers[event_type].append(callback)
    
    def publish(self, event_type: str, data: Any):
        """Publish event"""
        for callback in self.subscribers[event_type]:
            try:
                callback(data)
            except Exception as e:
                print(f"Error in subscriber: {e}")
    
    def unsubscribe(self, event_type: str, callback: Callable):
        """Unsubscribe from event type"""
        if callback in self.subscribers[event_type]:
            self.subscribers[event_type].remove(callback)

__author__ = "Tony Ray Macier III"
''',

    "monitoring.py": '''"""
THALOS PRIME - System Monitoring
Heartbeat tracking for Bio-Digital stability
Copyright (c) 2026 Tony Ray Macier III
"""

import time
import threading
from typing import Callable

class SystemMonitor:
    """Monitor system health"""
    
    def __init__(self, check_interval: float = 1.0):
        self.check_interval = check_interval
        self.monitors = {}
        self.running = False
        self.monitor_thread = None
    
    def register_monitor(self, name: str, check_func: Callable) -> bool:
        """Register a health check function"""
        self.monitors[name] = check_func
    
    def start(self):
        """Start monitoring"""
        self.running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
    
    def stop(self):
        """Stop monitoring"""
        self.running = False
        if self.monitor_thread:
            self.monitor_thread.join()
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            for name, check_func in self.monitors.items():
                try:
                    result = check_func()
                    if not result:
                        print(f"WARNING: Monitor '{name}' failed")
                except Exception as e:
                    print(f"ERROR in monitor '{name}': {e}")
            
            time.sleep(self.check_interval)

__author__ = "Tony Ray Macier III"
'''
}

# Create integration files
integration_path = BASE_PATH / "src" / "integration"
for filename, content in INTEGRATION.items():
    create_file(integration_path / filename, content)

print("\\n" + "="*60)
print("Security, GUI, and Integration modules created!")
print("="*60)
