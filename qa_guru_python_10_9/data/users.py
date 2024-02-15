import dataclasses


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobbie: str
    photo_name: str
    current_address: str
    state: str
    city: str


@dataclasses.dataclass
class SimpleUsers:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = Users(
    first_name='Georgii',
    last_name='Sergeev',
    email='example@gmail.com',
    gender='Male',
    mobile_number='0123456789',
    year_of_birth='2001',
    month_of_birth='February',
    day_of_birth='16',
    subject='Computer Science',
    hobbie='Reading',
    photo_name='image.png',
    current_address='Moscow, Red Square, 1A',
    state='NCR',
    city='Delhi')


george = SimpleUsers(
    full_name='Georgii Sergeev',
    email='example@gmail.com',
    current_address='Moscow, Red Square, 1A',
    permanent_address='Moscow, Red Square, 1A'
)