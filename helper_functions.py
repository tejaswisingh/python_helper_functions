import datetime

# In this helper function, the strftime() function is called on the now datetime object with the format string "%d-%m-%Y %I:%M:%S %p". 
# The %d, %m, and %Y are directives representing day, month, and year respectively. The %I directive represents the hour in 12-hour format,
# %M represents minutes, %S represents seconds, and %p represents the AM/PM indicator.
# When you run this function, it will display the current date and time in the specified format, including the AM/PM indicator.
# Here's an example output: "Formatted Date Time is:  07-07-2024 10:26:22 PM"
def formatted_datetime_to_am_pm():
    datetime_now = datetime.datetime.now()
    return datetime_now.strftime("%d-%m-%Y %I:%M:%S %p")
     
if __name__ == "__main__":
    formatted_datetime = formatted_datetime_to_am_pm()
    print(f'Formatted Date Time is:  {formatted_datetime}')