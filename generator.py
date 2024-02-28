from faker import Faker
from enum import Enum

fake = Faker()


class ColumnType(Enum):
    ORGNAME = "org_name"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    EMAIL = "email"
    STREET_ADDRESS = "street_address"
    CITY = "city"
    STATE = "state"
    ZIP = "zip"
    COUNTRY = "country"
    PHONE = "phone"


def genVal(type: ColumnType):
    match type:
        case ColumnType.ORGNAME:
            return fake.name().split(' ')[0] + " Company"
        case ColumnType.FIRST_NAME:
            return fake.name().split(' ')[0]
        case ColumnType.LAST_NAME:
            return fake.name().split(' ')[-1]
        case ColumnType.EMAIL:
            return fake.email()
        case ColumnType.PHONE:
            return fake.phone_number()
        case ColumnType.STREET_ADDRESS:
            return fake.street_address()
        case ColumnType.CITY:
            return fake.city()
        case ColumnType.STATE:
            return fake.address().split(' ')[-2]
        case ColumnType.ZIP:
            return fake.postcode()
        case ColumnType.COUNTRY:
            # return fake.country_code('alpha-2')
            # Using US only to maintain consistency with random state enteries
            return 'US'
        case _:
            raise TypeError("type: ", type, " doesn't match a case")


def genArray(type: ColumnType, n: int) -> list:
    return [genVal(type) for _ in range(0, n)]