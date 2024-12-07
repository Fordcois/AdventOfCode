import sys

class ProgressChecker:
    def __init__(self, number_to_check):
        self.number_to_check = number_to_check
        self.__number_width = len(str(self.number_to_check))
        self.checks_complete = 0
        
        # Hide the cursor at initialization
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
    
    def update_progress(self):
        self.checks_complete += 1
        
        # Calculate percentage
        percentage = (self.checks_complete / self.number_to_check) * 100
        
        # Colour codes
        neon_blue = '\033[38;5;45m'
        green = '\033[32m'
        reset = '\033[0m'
        bold = '\033[1m'
        
        progress_msg = (f"\r{bold}{green}{percentage:.2f}%{reset} Complete{reset} {neon_blue}-{reset} "
                        f"{str(self.checks_complete).zfill(self.__number_width)}"
                        f"{neon_blue}{bold}\\{reset}{self.number_to_check}")
        
        # Use sys.stdout for immediate printing and flushing
        sys.stdout.write(progress_msg)
        sys.stdout.flush()
        


# Example usage
# progress = ProgressChecker(5000000)
# progress.update_progress()


