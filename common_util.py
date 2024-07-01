from _datetime import datetime, timedelta
import calendar

def get_six_months_of_dates():
    """
    :return:
    """
    # Get today's date
    today = datetime.now()

    # Initialize an empty list to store date ranges
    date_ranges = []

    # Iterate over the next 6 months
    for i in range(6):
        if i == 5:  # For the 6th month, the end date is today
            start_date = today.replace(day=1)
            end_date = today
        else:  # For the other months, calculate the start and end dates
            first_day = today.replace(day=1) + timedelta(days=calendar.monthrange(today.year, today.month)[1] * i)
            last_day = first_day.replace(day=calendar.monthrange(first_day.year, first_day.month)[1])
            start_date = first_day
            end_date = last_day

        # Append the date range to the list as strings
        date_ranges.append([start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')])

    # Print the date ranges
    for start_date, end_date in date_ranges:
        print(f"Start Date: {start_date}, End Date: {end_date}")

    return date_ranges


def main():
    """
    main function
    :return:
    """
    get_six_months_of_dates()

if __name__ == "__main__":
    main()
