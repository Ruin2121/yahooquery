from ua_generator import generate
import random


def generate_headers():
    # Generate a user-agent and headers for Chrome and Edge browsers
    ua = generate(platform=("windows", "macos"), browser=("chrome", "edge", "safari"))

    # Extend Client Hints by specifying additional headers
    ua.headers.accept_ch("Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List")

    # Retrieve the generated headers
    headers = ua.headers.get()

    # Randomly select values for accept, accept-encoding, and accept-language
    accept_headers = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    ]

    accept_encodings = [
        "gzip, deflate",
        "gzip",
        "gzip, deflate, br",
    ]

    accept_languages = [
        "en-US,it;q=0.7",
        "en-US,en;q=0.7",
        "en-US,en;q=0.9",
        "en-US",
    ]

    # Update the headers dictionary with additional fields
    headers.update(
        {
            "upgrade-insecure-requests": "1",
            "accept": random.choice(accept_headers),
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "accept-encoding": random.choice(accept_encodings),
            "accept-language": random.choice(accept_languages),
        }
    )

    return headers
