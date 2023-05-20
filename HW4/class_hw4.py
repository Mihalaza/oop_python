class BaseClass1:
    def __init__(self):
        self.base_attr1 = "Base Attribute 1"

    def base_method1(self):
        print("Base Method 1")

class BaseClass2:
    def __init__(self):
        self.base_attr2 = "Base Attribute 2"

    def base_method2(self):
        print("Base Method 2")

class DerivedClass(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        self.derived_attr = "Derived Attribute"

    def derived_method(self):
        print("Derived Method")

# Створення об'єкту похідного класу
derived_obj = DerivedClass()


print(derived_obj.base_attr1)
derived_obj.base_method1()

print(derived_obj.base_attr2)
derived_obj.base_method2()


print(derived_obj.derived_attr)
derived_obj.derived_method()
