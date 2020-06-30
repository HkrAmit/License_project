from reader import reader
from valid import check

while True:
    try:
        data=reader()
        print (data)
        out=check(data)
        print(out)

    except Exception as e:
        print(e)
        print("Invalid Card")
