def hours(duration):
    return duration // 3600


def minutes(duration):
    remaining = duration - hours(duration) * 3600
    return remaining // 60


def seconds(duration):
    duration -= hours(duration) * 3600
    duration -= minutes(duration) * 60
    return duration
