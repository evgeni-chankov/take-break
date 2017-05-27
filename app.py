import time
import webbrowser

def which_video():
    """ Gets a user specified link to a video to use in the main function """
    preferred_video = raw_input("Please specify a link to your favourite relax website or video: ")
    return preferred_video

def wanted_time_between():
    """Asks the user for an int seconds between take break prompts """
    wanted_time = int(raw_input("Please specify how many minutes you would like to wait before the next prompt: "))
    seconds_wanted = wanted_time * 60
    return seconds_wanted

def max_number_breaks():
    """ Asks what the maximum number of breaks during the day should be """
    max_number_breaks = int(raw_input("Please specify maximum number of breaks during the day: "))
    return max_number_breaks

def take_break():
    """ Launches the app """
    the_video = which_video()
    time_between = wanted_time_between()
    #print time_between
    number_breaks = max_number_breaks()
    #print number_breaks
    i = 0
    while i < number_breaks:
        print "Time to take a break"
        print "Program started on " + time.ctime()
        web_link = webbrowser.open(the_video)
        time.sleep(time_between) 
        i += 1

take_break()
