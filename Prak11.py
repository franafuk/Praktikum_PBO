
def honirific(cls):
    class HonirificCls(cls):
        def full_name(self):
            return "Mr." + super().full_name()

    return HonirificCls


@honirific
class Name(object):
    def __init__(self, first_name, middle_name, last_name, nim):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nim = nim

    def full_name(self):
        return " ".join([self.first_name, self.middle_name, self.last_name, self.nim])


result = Name("francisco", "", "", "064002300044").full_name()
print("full name: {0}".format(result))

