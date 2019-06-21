guitars={
    {'model1':'Yamaha F310','price':8400},
    {'model2':'Faith NEptune','price':50000},
    {'model3':'faith Apollo Venus','price':35000},
    {'model4':'Taylor 814ce','price':450000}
    }
print(sorted(guitars,key=lambda d:d['price']))
