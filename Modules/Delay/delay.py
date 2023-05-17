'''Methods to add a time lap of :-\n
-----------------------------------\n
Quarter Second (1/4 or 0.25 seconds)
Method : quarter_second_delay()\n
Half Second (1/2 or 0.5 seconds)
Method : half_second_delay()\n
One Second (1 second)
Method : one_second_delay()\n
Two Seconds (2 seconds)
Method : two_second_delay()\n
Five Seconds (5 seconds)
Method : five_second_delay()\n
Ten Seconds (10 seconds)
Method : ten_second_delay()
-----------------------------------'''
import datetime
def one_second_delay() -> None:
    "Add a time lap of 1 second."
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:21]
    second_ = c[0:2]
    if second_=="59":
        second = "00"
    else:
        second__ = int(second_)
        second___ = second__+1
        second____ = str(second___)
        if len(second____)==1:
            second = f"0{second____}"
        else:
            second = second____
    miliseconds = c[2:4]
    upto_time = second+miliseconds
    while 1==1:
        d = datetime.datetime.today()
        e = str(d)
        f = e[17:21]
        if f==upto_time:
            break
        else:
            continue
def half_second_delay() -> None:
    "Add a time lap of half second."
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:21]
    second_ = c[0:4]
    if second_=="59.5":
        second = "00.0"
    elif second_=="59.6":
        second = "00.1"
    elif second_=="59.7":
        second = "00.2"
    elif second_=="59.8":
        second = "00.3"
    elif second_=="59.9":
        second = "00.4"
    else:
        second__ = float(second_)
        second___ = second__+0.5
        second____ = str(second___)
        if len(second____)==3:
            second = f"0{second____}"
        else:
            second = second____
    upto_time = second
    while 1==1:
        d = datetime.datetime.today()
        e = str(d)
        f = e[17:21]
        if f==upto_time:
            break
        else:
            continue
def quarter_second_delay() -> None:
    "Add a time lap of quarter second"
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:22]
    second_ = c[0:5]
    g = float(second_)
    if second_=="59.75":
        second = "00.00"
    elif g>59.75 and g<60.0:
        h = g+0.25
        i = h%60
        j = str(i)
        if len(j)==3:
            second = f"0{j}0"
        elif len(j)==4:
            k = j[:2]
            l = k.find('.')
            if l==-1:
                second = f"{j}0"
            else:
                second = f"0{j}"
        else:
            second = j
    else:
        second__ = float(second_)
        second___ = second__+0.25
        second____ = str(second___)
        if len(second____)==3:
            second = f"0{second____}0"
        elif len(second____)==4:
            k = second____[:2]
            l = k.find('.')
            if l==-1:
                second = f"{second____}0"
            else:
                second = f"0{second____}"
        else:
            second = second____
    upto_time = second
    while 1==1:
        part1 = datetime.datetime.today()
        part2 = str(part1)
        part3 = part2[17:22]
        if part3==upto_time:
            break
        else:
            continue
def two_second_delay() -> None:
    "Add a time lap of two seconds."
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:21]
    second_ = c[0:2]
    if second_=="58":
        second = "00"
    elif second_=="59":
        second = "01"
    else:
        second__ = int(second_)
        second___ = second__+2
        second____ = str(second___)
        if len(second____)==1:
            second = f"0{second____}"
        else:
            second = second____
    miliseconds = c[2:4]
    upto_time = second+miliseconds
    while 1==1:
        d = datetime.datetime.today()
        e = str(d)
        f = e[17:21]
        if f==upto_time:
            break
        else:
            continue
def five_second_delay() -> None:
    "Add a time lap of five seconds."
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:21]
    second_ = c[0:2]
    if second_=="55":
        second = "00"
    if second_=="56":
        second = "01"
    if second_=="57":
        second = "02"
    if second_=="58":
        second = "03"
    if second_=="59":
        second = "04"
    else:
        second__ = int(second_)
        second___ = second__+5
        second____ = str(second___)
        if len(second____)==1:
            second = f"0{second____}"
        else:
            second = second____
    miliseconds = c[2:4]
    upto_time = second+miliseconds
    while 1==1:
        d = datetime.datetime.today()
        e = str(d)
        f = e[17:21]
        if f==upto_time:
            break
        else:
            continue
def ten_second_delay() -> None:
    "Add a time lap of ten seconds."
    a = datetime.datetime.today()
    b = str(a)
    c = b[17:21]
    second_ = c[0:2]
    if second_=="50":
        second = "00"
    if second_=="51":
        second = "01"
    if second_=="52":
        second = "02"
    if second_=="53":
        second = "03"
    if second_=="54":
        second = "04"
    if second_=="55":
        second = "05"
    if second_=="56":
        second = "06"
    if second_=="57":
        second = "07"
    if second_=="58":
        second = "08"
    if second_=="59":
        second = "09"
    else:
        second__ = int(second_)
        second___ = second__+10
        second____ = str(second___)
        if len(second____)==1:
            second = f"0{second____}"
        else:
            second = second____
    miliseconds = c[2:4]
    upto_time = second+miliseconds
    while 1==1:
        d = datetime.datetime.today()
        e = str(d)
        f = e[17:21]
        if f==upto_time:
            break
        else:
            continue
