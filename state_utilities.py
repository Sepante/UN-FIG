import numpy as np
import uuid

import time


# Create a readable title
def create_state_title(topic, post_90, randomize_resolution_direction, remove_local_field, negative_weight_allowed):

    state_title = (
        f"Topic: {topic.upper()} | "
        f"Post-90: {post_90} | "
        f"Randomize Direction: {randomize_resolution_direction} | "
        f"Remove Local Field: {remove_local_field} | "
        f"Negative Weights Allowed: {negative_weight_allowed}"
    )
    

    # Get the current Unix timestamp as an integer
    #timestamp = int(time.time() * 10)
    timestamp = str(uuid.uuid4())

    # Convert the readable title to a filename-safe format and add a unique integer suffix
    # Create the filename with the timestamp
    state_title_filename = f"{state_title.replace(' ', '_').replace(':', '').replace('|', '').replace('-', '')}_{timestamp}"

    return state_title, state_title_filename
