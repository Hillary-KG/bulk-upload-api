import csv
import sys
import random
from datetime import datetime
import secrets

from faker import Faker


def generate_records():
    fake = Faker()

    try:
        number_of_rows = int(sys.argv[1])
    except (IndexError, ValueError):
        number_of_rows = 100000

    data = [
        [
            "first_name",
            "last_name",
            "national_id",
            "birth_date",
            "address",
            "country",
            "phone_number",
            "email",
            "finger_print_signature",
        ]
    ]

    for i in range(number_of_rows):
        # first_name, last_name, national_id, birth_date, address, country, phone_number,email,
        data.append(
            [
                fake.first_name(),
                fake.last_name(),
                str(random.randint(1, 999999)),
                fake.date(),
                fake.address(),
                fake.country(),
                fake.phone_number(),
                fake.email(),
                secrets.token_urlsafe(64),
            ]
        )

    with open(
        f"records_{datetime.now().strftime('%Y%M%d%H%M%S')}.csv", "w", newline=""
    ) as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quotechar='"')
        writer.writerows(data)


if __name__ == "__main__":
    generate_records()
