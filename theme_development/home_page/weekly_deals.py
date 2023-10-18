```python
import time
from datetime import datetime, timedelta

def renderWeeklyDeals(dealsData):
    """
    Function to render the weekly deals section.
    """
    for deal in dealsData:
        renderDeal(deal)

def renderDeal(deal):
    """
    Function to render a single deal.
    """
    # Create a countdown timer
    countdown_timer(deal['endTime'])

    # Highlight the percentage discount
    highlight_discount(deal['discount'])

def countdown_timer(endTime):
    """
    Function to create a countdown timer showcasing the time left for the deal.
    """
    end_time = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
    while datetime.now() < end_time:
        time_left = end_time - datetime.now()
        print(f"Time left for the deal: {time_left}")

def highlight_discount(discount):
    """
    Function to use badges or tags to highlight the percentage discount.
    """
    print(f"Discount: {discount}%")
```