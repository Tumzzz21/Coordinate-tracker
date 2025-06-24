import win32gui
import keyboard
import time
import random

class RobloxKeyPresser:
    def __init__(self):
        self.running = False
        self.keys_to_press = ['space', 'w', 's']
        self.min_interval = 1.0  # 1 second minimum
        self.max_interval = 20.0  # 20 seconds maximum
        self.current_window = None

    def is_roblox_active(self):
        """Check if Roblox is the active window"""
        try:
            self.current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            return "Roblox" in self.current_window
        except:
            return False

    def press_random_key(self):
        """Press a random key when Roblox is active"""
        while self.running:
            if self.is_roblox_active():
                key = random.choice(self.keys_to_press)
                keyboard.press(key)
                time.sleep(0.1)  # Short press duration
                keyboard.release(key)
                print(f"Pressed: {key} (Active window: {self.current_window[:20]}...)")
                
                # Random delay between 1-20 seconds
                delay = random.uniform(self.min_interval, self.max_interval)
                time.sleep(delay)
            else:
                # If Roblox isn't active, check every second
                time.sleep(1)

    def start(self):
        """Start the key presser"""
        print("Roblox Key Presser Started")
        print(f"Will press: {', '.join(self.keys_to_press)}")
        print(f"Random intervals: {self.min_interval}-{self.max_interval} seconds")
        print("Note: Only works when Roblox window is active")
        print("Press F3 to stop")
        
        self.running = True
        try:
            self.press_random_key()
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print("Script stopped")

if __name__ == "__main__":
    presser = RobloxKeyPresser()
    
    # Start when F2 is pressed
    keyboard.add_hotkey('F2', presser.start)
    # Stop when F3 is pressed
    keyboard.add_hotkey('F3', lambda: setattr(presser, 'running', False))
    
    print("=== Roblox Auto Key Presser ===")
    print("F2: Start | F3: Stop | F12: Exit")
    print("The script only works when Roblox is the active window")
    
    keyboard.wait('F12')