
### 1. Python Sets Adventure ########

our_routes = {"LAX", "JFK", "CDG", "DXB"} 
competitor_routes = {"JFK", "CDG", "LHR", "VKK"} 

# 1. Destinations that both airlines fly to.

common_routes = our_routes.intersection(competitor_routes) 
print(f"Destinations both airlines fly to: {common_routes}") 

# 2. Destinations unique to your airline (difference)
unique_to_our_airline = our_routes.difference(competitor_routes) 
print(f"Destinations unique to our airline: {unique_to_our_airline}")
 
# 3. Whether there are any destinations that neither airline shares.
 
exclusive_routes = our_routes.symmetric_difference(competitor_routes) 
print(f"Destinations neither airline shares: {exclusive_routes}")

### 2. Set Operations in Data Analysis  ########

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"] 

# 1. Remove duplicates 
unique_customer_ids = set(customer_ids) 

# 2. Display the unique customer IDs 
print(f"Unique customer IDs: {unique_customer_ids}")