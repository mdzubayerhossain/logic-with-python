from subprocess import Popen , PIPE
import requests
import webbrowser as wb 



def execute_return(cmd):
    """This function is used for pre compile the code and take output and error as binary object"""
    args = cmd.split()
    proc = Popen(args,stdout=PIPE,stderr=PIPE)
    out,err = proc.communicate()
    return out,err


def search_err(error):
    """take the error and search it in api and return JSON object"""

    url = "https://api.stackexchange.com/" + "/2.2/search?page=2&order=desc&sort=activity&tagged=python&intitle={}&site=stackoverflow".format(error)
    
    resp = requests.get(url)
    return resp.json()


def get_urls(json_dict):
    """take the json file and spilt the searching link from the json file dictionary"""
    url_list = []
    count = 0
    for i in json_dict["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
        count += 1
        if count == 3 or count == len(i):
            break
        
    for i in url_list:
        wb.open(i)



if __name__ == "__main__":
    op,err = execute_return("python code.py")
    error_message = err.decode("utf-8").strip().split("\r\n")[-1]
    #print(error_message)
    if error_message:
        filter_err = error_message.split(":")
        json1 = search_err(filter_err[0])
        json2 = search_err(filter_err[1])
        json = search_err(error_message)

        get_urls(json1)
        get_urls(json2)
        get_urls(json)
    else:
        print("No Error")

