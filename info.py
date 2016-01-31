# info.py处理以下信息
# title, create, modified


def generate_title(title):
    assert isinstance(title, str), "Title must be strings!"

    return " - {}".format(title)


def generate_time(year, month, day):
    return "{YYYY}.{MM}.{DD}".format(
        YYYY=year,
        MM=month,
        DD=day
    )
