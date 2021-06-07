from dotenv import load_dotenv
from $FUNCTION_NAME.entry import *

# // this function is not a part of the serverless and will not be processed by Lyrid,
# // this is for user to be able to locally test and build their functions

if __name__ == "__main__":
    load_dotenv()
    pre_run()

    LyFnInputParams.update({"InputSample": "Hello"})
    main_run(LyFnInputParams, LyFnOutputParams)

    print("Function Input: " + LyFnInputParams["InputSample"])
    print("Function Output: " + LyFnOutputParams["OutputSample"])

    post_run()