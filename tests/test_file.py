import importlib.util

# Dynamically load the HTMLBuilder module
spec = importlib.util.spec_from_file_location("Leetify", "./src/Python_leetifyer_Bradley_Hu/Leetify.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_1():
    if module.leetify("HeLlO!")=="|-|[-|_|_()!":
        return True
    else:
        return False