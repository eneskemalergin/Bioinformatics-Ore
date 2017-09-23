# This is the small snippet to print the time elapsed
def pretty_timer(start, end):
    exec_time = (end - start)/60
    if exec_time >= 1.0:
        print("Execution time is:", format(exec_time, '.2f'), "minutes")
    elif exec_time < 1.0:
        print("Execution time is:", format(exec_time, '.2f'), "seconds")
