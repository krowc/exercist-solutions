"""This module simulates those hormone-ridden peeps out there. 
"""
def response(hey_bob):
    """This function responds to a variety of inputs. This function is bob.
    :param hey_bob: string - anything you want to say to bob?
    :return: string - how bob will react.
    """
    if hey_bob.strip() == "":
        return "Fine. Be that way!"

    if hey_bob.isupper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if hey_bob.strip()[-1] == "?":
        return "Sure."

    return "Whatever."



    