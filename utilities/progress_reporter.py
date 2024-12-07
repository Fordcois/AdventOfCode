import sys

class ProgressChecker:
    def __init__(self, number_to_check):
        self.number_to_check = number_to_check
        self.__number_width = len(str(self.number_to_check))
        self.checks_complete = 0
        
        # Hide the cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

    def __del__(self):
        # Ensure cursor is restored when the object is deleted
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
    
    def update_progress(self):
        self.checks_complete += 1
        
        percentage = (self.checks_complete / self.number_to_check) * 100
        
        # Colour codes
        neon_blue = '\033[38;5;45m'
        green = '\033[32m'
        reset = '\033[0m'
        bold = '\033[1m'
        
        progress_msg = (f"\r{bold}{green}{percentage:.2f}%{reset} Complete{reset} {neon_blue}-{reset} "
                        f"{str(self.checks_complete).zfill(self.__number_width)}"
                        f"{neon_blue}{bold}\\{reset}{self.number_to_check}")
        
        sys.stdout.write(progress_msg)
        sys.stdout.flush()
        
        # Ensure a clean newline when complete
        if self.checks_complete >= self.number_to_check:
            sys.stdout.write("\n") 
            sys.stdout.write("\033[?25h")  # Restore cursor
            sys.stdout.flush()
        


# Example usage
# progress = ProgressChecker(5000000)
# progress.update_progress()


