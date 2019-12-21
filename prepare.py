def main():
    start_flag= True
    with open('semeion.data') as file:
        # limit = -1
        for line in file.readlines():
            # limit = limit +1 
            # if limit == 100:
            #     break
            row = line.split(' ')
            image_area = row [0 : 256]
            image_area = row_preparer(image_area)
            number_area = row[256 : (len(row)-1)]
            num = counter(number_area)
            image_area.append(str(num))
            with open('semeion.csv','a') as target:
                if start_flag:
                    start_flag = False
                    titles= []
                    for index in range(257):
                        titles.append(f'p{index}')
                    target.write(",".join(titles))
                    target.write("\n")
                else:
                    target.write("\n")
                target.write(','.join(image_area))
            
def counter(arr):
    c = 0
    while True:
        if int(arr[c]) ==1 :
            break
        c = c+1
    return c
def row_preparer(arr):
    res = []
    for item in arr:
        res.append(str(int(float(item))))
    return res
def read():
     with open('semeion.csv','r') as target:
         print(len(target.readlines()))
if __name__ =='__main__':
    main()