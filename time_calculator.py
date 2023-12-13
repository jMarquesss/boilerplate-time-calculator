DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def to_12_hour_format(hour):
    am_pm = "AM" if hour < 12 else "PM"
    hour %= 12
    if hour == 0:
        hour = 12
    return hour, am_pm

def calculate_new_time(start_hour, start_minute, duration_hours, duration_minutes):
    new_hour = start_hour + duration_hours + (start_minute + duration_minutes) // 60
    new_minute = (start_minute + duration_minutes) % 60
    days_later = new_hour // 24
    new_hour %= 24
    return new_hour, new_minute, days_later

def add_time(start, duration, day=None):
    # Parse start time and AM/PM
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if am_pm == "PM":
        start_hour += 12

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate new time and days later
    new_hour, new_minute, days_later = calculate_new_time(start_hour, start_minute, duration_hours, duration_minutes)

    # Convert new time to 12-hour format
    new_hour, new_am_pm = to_12_hour_format(new_hour)

    # Format new time
    new_time_str = f"{new_hour}:{new_minute:02d} {new_am_pm}"

    # Add day of the week if provided
    if day:
        day_index = (DAYS_OF_WEEK.index(day.capitalize()) + days_later) % 7
        new_time_str += f", {DAYS_OF_WEEK[day_index]}"

    # Add number of days later
    if days_later == 1:
        new_time_str += " (next day)"
    elif days_later > 1:
        new_time_str += f" ({days_later} days later)"

    return new_time_str