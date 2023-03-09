from datetime import datetime, time
from zoomus import ZoomClient


def book_session():
    # Check if current time is within business hours
    business_start_time = time(9, 0, 0)  # 9:00am
    business_end_time = time(17, 0, 0)  # 5:00pm
    current_time = datetime.now().time()
    if current_time < business_start_time or current_time > business_end_time:
        print(
             "Sorry, our business hours are Monday to Friday from 9am to 5pm. Please come back during our business "
             "hours to book a session on Zoom.")
        return

    # Initialize Zoom client with API key and secret
    client = ZoomClient(api_key='wkCcCc2QQVeQIXwOtdUJ_A', api_secret='clBUnpPiHrjSkoyTzAUbAUnKrwMhU8M2ZfH6')

    # Set up meeting details
    meeting_details = {
        'topic': 'Cloud technology session',
        'type': 2,  # Scheduled meeting
        'start_time': '2023-03-10T14:00:00Z',  # Start time in UTC (change to desired date and time)
        'duration': 60,  # Duration in minutes
        'timezone': 'America/New_York',  # Timezone of meeting (change to desired timezone)
        'agenda': 'Discussion of cloud technology tools and best practices',
    }

    # Create meeting
    meeting = client.meeting.create(meeting_details)

    # Get join URL for meeting
    join_url = meeting.get('join_url')

    # Print join URL for user to join the meeting and information about the fee
    print(
        f"Please pay $100 for the session via PayPal or credit card. Once payment is confirmed, you will receive an "
        f"email with the Zoom link to join the meeting.")
    print(f"Please use the following link to join the meeting: {join_url}")
