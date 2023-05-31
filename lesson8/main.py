from logging import DEBUG, basicConfig, debug, info, warning, error, critical
basicConfig(level=DEBUG,
            filename='lesson8log.log',
            filemode='a',
            format="We have next loggin massage: %(asctime)s : %(levelname)s - %(message)s")
'''
debug("debug message")
info("info message")
warning("warning message")
error("error message")
critical("critical message")
'''

while(True):
    try:
        digit1 = 10
        digit2 = int(input("Enter digit: "))
        info(f"Enter digit2: {digit2}")
        res = digit1/digit2
        print(res)
    except ZeroDivisionError as zde:
        error(zde)
    except Exception as ex:
        error(ex)
    yes = input("Enter Y for contine or N for stop:")
    if(yes.lower() == "n"):
        break
print("Cycle whilehas stoped")