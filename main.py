import pytest

def format_user(userdata, format):
    result = ""
    u = userdata["name"]
    if format == "greeting":
        result = "{} {} {}".format(u["title"], u["first"], u["last"])
    elif format == "short":
        result = "{} {}".format(u["title"], u["first"])
    elif format == "country":
        result = userdata["nat"]
    elif format == "table":
        result = "{} | {} | {} | {}".format(u["title"], u["first"], u["last"], userdata["nat"])
    else:
        result = None

    return result


pytest.main(["-v"])