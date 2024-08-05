import datetime
import random
import string
import faker

def call_function(name):
    func_name = f"make_random_{name}"
    func = globals().get(func_name)
    return func()

def datetime2wareki(date):
    ERA_DICT = {
        "令和": datetime.datetime(2019, 5, 1),
        "平成": datetime.datetime(1989, 1, 8),
        "昭和": datetime.datetime(1926, 12, 25)
    }

    def to_wareki(date_obj):
        if ERA_DICT["令和"] <= date_obj:
            era_start = ERA_DICT["令和"]
            era = "令和"
        elif ERA_DICT["平成"] <= date_obj:
            era_start = ERA_DICT["平成"]
            era = "平成"
        elif ERA_DICT["昭和"] <= date_obj:
            era_start = ERA_DICT["昭和"]
            era = "昭和"
        jp_year = date_obj.year - era_start.year + 1
        return {"era": era, "year": jp_year, "month": date_obj.month, "day": date_obj.day}

    return to_wareki(date)

FAKE = faker.Faker("ja-JP")
def make_random_string(min_length=1, max_length=10):
    length = random.randint(min_length, max_length+1)
    s = FAKE.sha1()[:length]
    case_1 = random.randint(0, 1)
    if case_1 == 1:
        s = s.upper()
    return s

def make_random_unit():
    length = random.randint(1, 2)
    s = make_random_word()[:length]
    return s

def make_random_num(min_length=1, max_length=4):
    length = random.randint(min_length, max_length+1)
    n = str(random.randint(1,9))
    if length > 1:
        n += "".join(map(str, [random.randint(0,9) for i in range(length)]))
    return n

def make_random_percentage():
    percentage = random.randint(1, 100)
    case_1 = random.randint(0, 2)
    if case_1 == 0:
        percentage = str(round(percentage/100, 2))
    if case_1 == 1:
        percentage = f"{str(percentage)}%"
    if case_1 == 2:
        percentage = f"{str(percentage)}"
    return percentage

def make_random_punctuation():
    punctuation = string.punctuation + " "
    idx = random.randint(0, len(punctuation)-1)
    return punctuation[idx]


def make_random_date():
    date = FAKE.date_time_between_dates(datetime_start=datetime.datetime(1926, 12, 25))
    case_1 = random.randint(0, 7)
    if case_1 == 0:
        date = date.strftime("%Y/%m/%d")
    if case_1 == 1:
        date = date.strftime("%Y-%m-%d")
    if case_1 == 2:
        date = date.strftime("%Y年%m月%d月")
    if case_1 == 3:
        date = date.strftime("%-Y/%-m/%-d")
    if case_1 == 4:
        date = date.strftime("%-Y-%-m-%-d")
    if case_1 == 5:
        date = date.strftime("%-Y年%-m月%-d月")
    if case_1 == 6:
        date_jp = datetime2wareki(date)
        era = date_jp["era"]
        year = date_jp["year"]
        month = date_jp["month"]
        day = date_jp["day"]
        date = f"{era}{year}年{month}月{day}日"
    if case_1 == 7:
        date_jp = datetime2wareki(date)
        era = date_jp["era"].zfill(2)
        year = str(date_jp["year"]).zfill(2)
        month = str(date_jp["month"]).zfill(2)
        day = str(date_jp["day"]).zfill(2)
        date = f"{era}{year}年{month}月{day}日"
    return date

def make_random_amount(min_length=1, max_length=10):
    case_1 = random.randint(0, 1)
    case_2 = random.randint(0, 2)
    amount = make_random_num(min_length, max_length)
    if case_1 == 1:
        amount = "{:,d}".format(int(amount))
    if case_2 == 1:
        amount = "¥" + amount
    elif case_2 == 2:
        amount = "$" + amount
    return amount

def make_random_name():
    case_1 = random.randint(0, 1)
    if case_1 == 0:
        name = FAKE.name()
    if case_1 == 1:
        name = FAKE.last_name()
    return name

def make_random_address():
    return FAKE.address()

def make_random_zipcode():
    return FAKE.zipcode()

def make_random_zipcode_and_address():
    case_1 = random.randint(0, 1)
    zipcode = make_random_zipcode()
    address = make_random_address()
    zip_symbol = ""
    if case_1 == 1:
        zip_symbol = "〒"
    zipcode_and_address = f"{zip_symbol}{zipcode} {address}"
    return zipcode_and_address

def make_random_email():
    return FAKE.email()

def make_random_company():
    return FAKE.company()

def make_random_company_dear():
    case_1 = random.randint(0, 2)
    dear = ""
    if case_1 == 1:
        dear = "御中"
    if case_1 == 2:
        dear = "様"
    return dear

def make_random_word():
    return FAKE.word()

def make_random_title():
    return f"{FAKE.word()}:"

def make_random_text():
    text = FAKE.text()
    text = text.split("\n")[0]
    return text

def make_random_tel():
    case_1 = random.randint(0, 1)
    tel = FAKE.phone_number()
    if case_1 == 1:
        tel = "TEL:" + tel
    if case_1 == 2:
        tel = "電話番号:" + tel
    return tel
