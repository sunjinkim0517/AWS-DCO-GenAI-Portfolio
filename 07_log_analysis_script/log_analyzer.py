import glob
import os
import re

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob("server*.log"))
    
    print(f"{'Server File':<15} | {'CRC Error Count':<17} | {'Link Down Count':<17}")
    print("-" * 55)
    
    total_crc = 0
    total_link_down = 0
    
    for filepath in log_files:
        filename = os.path.basename(filepath)
        crc_count = 0
        link_down_count = 0
        
        # Parse lines into multi-line log entries
        entries = []
        current_entry = []
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip() == "":
                    continue
                # If a line starts with space, tab, or '->', it is part of the previous log entry
                if line.startswith((' ', '\t', '->')):
                    if current_entry:
                        current_entry.append(line.strip())
                else:
                    if current_entry:
                        entries.append("\n".join(current_entry))
                    current_entry = [line.strip()]
            if current_entry:
                entries.append("\n".join(current_entry))
                
        # Analyze each log entry
        for entry in entries:
            entry_lower = entry.lower()
            
            # Count CRC Error: Must contain "crc error" (or space equivalent)
            # but must not contain recovery or "no error" status
            if re.search(r'crc\s+error', entry_lower):
                if 'recover' not in entry_lower and 'no crc error' not in entry_lower:
                    crc_count += 1
                    
            # Count Link Down: Must contain "link down"
            # but must not contain timer reset notifications
            if re.search(r'link\s+down', entry_lower):
                if 'timer' not in entry_lower:
                    link_down_count += 1
                    
        print(f"{filename:<15} | {crc_count:<17} | {link_down_count:<17}")
        total_crc += crc_count
        total_link_down += link_down_count
        
    print("-" * 55)
    print(f"{'Total':<15} | {total_crc:<17} | {total_link_down:<17}")

if __name__ == "__main__":
    analyze_logs()
