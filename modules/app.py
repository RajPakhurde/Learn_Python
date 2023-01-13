# For importing whole module
import weight_converter
# For importing one specific function
from weight_converter import kg_to_lbs
# If we import specific funtion we don't have to use object name to call it.
print(kg_to_lbs(60))
# If we import whole module than we have to call funtions using object name
print(weight_converter.lbs_to_kg(60))
