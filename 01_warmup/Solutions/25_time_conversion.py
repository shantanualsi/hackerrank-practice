if __name__ == '__main__':
    time_input = raw_input()
    time_specifier = time_input[-2:]
    hh,mm,ss = time_input.split(":")
    ss = ss[:2]
    if time_specifier == "PM" and hh != "12":
        hh = int(hh) + 12

    if hh == "12":
        if time_specifier == "AM":
            hh = "00"
        else:
            hh = "12"
    print "%s:%s:%s" %(hh,mm,ss)
