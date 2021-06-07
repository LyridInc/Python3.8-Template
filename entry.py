import os

# LyFnInputParams user fills up these parameters
# The internal composition of the dict can be changed to fit your usage. Do not change the variable name of dict.
LyFnInputParams = {
    "InputSample": ""
}

# LyFnOutputParams a struct that will be returned
# The internal composition of the dict can be changed to fit your usage. Do not change the variable name of dict.
LyFnOutputParams = {
    "OutputSample": ""
}


# PreRun (optional) will be executed prior to MainRun
def pre_run():
    pass


# MainRun
def main_run(input_params=None, output_params=None):
    output_sample = input_params["InputSample"] + " " + os.getenv("ENV1")

    response = output_params.update({
        "OutputSample": output_sample
    })

    return response


# PostRun (optional) will be executed after Run() is executed
def post_run():
    pass