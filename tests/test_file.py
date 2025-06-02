import importlib.util

# Dynamically load the HTMLBuilder module
spec = importlib.util.spec_from_file_location("HTMLBuilder", "./src/Html_Builder_Bradley_Hu/htmlBuilder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HTMLBuilder = module.HTMLBuilder

def test_1():
