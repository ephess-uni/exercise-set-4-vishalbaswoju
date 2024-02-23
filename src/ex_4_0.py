""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation
    """
    total_shutdown_events = list()
    
    with open(logfile, 'r') as file_log:
        
        total_events = file_log.read()
    
    all_events = total_events.splitlines()
    
    for log in all_events:
        
        if 'Shutdown initiated' in log :
            
            total_shutdown_events.append(log)
        
    return total_shutdown_events


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
