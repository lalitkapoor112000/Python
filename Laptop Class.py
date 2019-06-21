class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+model_name
    def apply_discount(self,n):
        discount=self.price*(n/100)
        return self.price-discount
        
l1=Laptop('MSI','GL 638RC',59000)
print(l1.brand_name)
print(l1.laptop_name)
print(l1.apply_discount(10))
