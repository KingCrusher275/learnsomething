# import cppimport.import_hook
import PricingUtil


if __name__ == "__main__":
    print("Nice work on creating the util! Make sure to check the unit tests!")
    p = PricingUtil.PricingUtil()
    p.calcVal(5, 0, 1)
    print(p.getVal())
