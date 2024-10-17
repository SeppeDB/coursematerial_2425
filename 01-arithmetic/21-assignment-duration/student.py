<<<<<<< HEAD
def hours(duration):
    return duration // 3600


def minutes(duration):
    remaining = duration - hours(duration) * 3600
    return remaining // 60


def seconds(duration):
    duration -= hours(duration) * 3600
    duration -= minutes(duration) * 60
    return duration
=======
# write your code here
>>>>>>> 9d2e6f6b0d66889fcf68a22f9172d09f0711fd68
