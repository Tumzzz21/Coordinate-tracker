import win32gui
import win32api
import time

class WindowCoordinateTracker:
    def __init__(self, target_window_title):
        self.target_window_title = target_window_title
        self.active = False
    
    def is_target_window_active(self):
        """Check if our target window is the foreground window"""
        foreground_window = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(foreground_window)
        return self.target_window_title in window_title
    
    def get_relative_mouse_position(self):
        """Get mouse position relative to the target window"""
        hwnd = win32gui.FindWindow(None, self.target_window_title)
        if not hwnd:
            return None
        
        window_rect = win32gui.GetWindowRect(hwnd)
        abs_x, abs_y = win32api.GetCursorPos()
        
        # Calculate relative position
        rel_x = abs_x - window_rect[0]
        rel_y = abs_y - window_rect[1]
        
        # Verify mouse is actually within the window
        if (0 <= rel_x <= (window_rect[2] - window_rect[0]) and 
    0 <= rel_y <= (window_rect[3] - window_rect[1])):
    # Do something

            return rel_x, rel_y
        return None
    
    def track(self):
        """Main tracking loop"""
        print(f"Tracking coordinates only in '{self.target_window_title}' window... (Ctrl+C to stop)")
        try:
            while True:
                if self.is_target_window_active():
                    coords = self.get_relative_mouse_position()
                    if coords:
                        x, y = coords
                        if not self.active:
                            print("\nEntered target window - tracking started")
                            self.active = True
                        print(f"X: {x:4d}, Y: {y:4d}", end='\r')
                    elif self.active:
                        print("\nLeft target window - tracking paused", end='\r')
                        self.active = False
                elif self.active:
                    print("\nLeft target window - tracking paused", end='\r')
                    self.active = False
                
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\nStopped tracking")

# Example usage for File Explorer:
if __name__ == "__main__":
    # For English Windows, File Explorer windows typically include "Folder" in the title
    # You may need to adjust this based on your system language
    tracker = WindowCoordinateTracker("File Explorer")
    tracker.track()