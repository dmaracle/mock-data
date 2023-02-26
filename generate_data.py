import random

# Generate a 2D Array of customer information
def generate_array(num_clients):
    names = generate_names(num_clients)
    address = generate_address(num_clients)
    phone = generate_phone(num_clients)
    city = generate_city(num_clients)
    email = generate_email(num_clients)
    client_type = generate_client_type(num_clients)
    client_acquisition = generate_client_acquisition(num_clients)
    client_occurence = generate_occurence_rate(num_clients)
    job_pricing = generate_prices(num_clients)
    windows_price = generate_window_price(num_clients, job_pricing)
    pressure_wash_price = generate_pressure_wash_price(num_clients, job_pricing)
    handywork_price = generate_handywork_price(num_clients, job_pricing)
    annual_revenue = generate_annual_revenue(num_clients, windows_price, pressure_wash_price, handywork_price, client_occurence)
    expenses = generate_expenses(num_clients, city, annual_revenue)
    profit = generate_annual_profit(num_clients, annual_revenue, expenses)
    master_list = generate_master_list(num_clients, names, address, phone, city, email, client_type, client_acquisition, client_occurence,
                                       windows_price, pressure_wash_price, handywork_price, expenses, profit)
    return master_list

def generate_names(num_clients):
    names = ['Drew', 'Ghazal', 'Troy', 'Elena', 'Tiffany']
    name_list = [random.choices(names, k=num_clients)][0]
    return name_list

def generate_address(num_clients):
    street_name = ['Rosemary', 'Glass', 'Rose', 'Blanket', 'Adams', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    street_suffix = ['Ave', 'Road', 'Boulevard', 'Street', 'Place', 'Corner']
    address_list = []
    for x in range(num_clients):
        random_address = (f"{random.randint(1,999)} {random.choice(street_name)} {random.choice(street_suffix)}")
        address_list.append(random_address)
    return address_list

def generate_phone(num_clients):
    phone_prefix = ['619', '858', '760']
    phone_list = []
    for x in range(num_clients):
        phone_number = f"{random.choices(phone_prefix, weights=(.87, .09, .04))[0]}-{random.randint(100,999)}-{random.randint(1000,9999)}"
        phone_list.append(phone_number)
    return phone_list

def generate_city(num_clients):
    cities = ['Coronado', 'Chula Vista', 'La Jolla', 'East Village', 'North Park', 'Imperial Beach']
    cities_list = [random.choices(cities, weights=(.90, .02, .02, .02, .02, .02, ), k=num_clients)][0]
    return cities_list

def generate_email(num_clients):
    names = generate_names(num_clients)
    email_suffixes = ['@hotmail.com', '@gmx.com', '@gmail.com', '@university.edu']
    email_list = []
    for x in range(num_clients):
        emails = f"{names[x]}{random.randint(1,999)}{random.choice(email_suffixes)}"
        email_list.append(emails)
    return email_list
    
def generate_client_type(num_clients):
    customer_type = ['Residential', 'Contractor', 'Business']
    cust_type_list = [random.choices(customer_type, weights=(.88, .08, .04), k=num_clients)][0]
    return cust_type_list

def generate_client_acquisition(num_clients):
    acquisition_styles = ['Flier', 'Referral', 'Online']
    acquisition_list = [random.choices(acquisition_styles, weights=(.63, .33, .04), k=num_clients)][0]
    return acquisition_list

def generate_occurence_rate(num_clients):
    occurence_rates = [1, 2, 3, 4, 6, 12]
    occurence_list = [random.choices(occurence_rates, weights=(.60, .24, .11, .03, .01, .01), k=num_clients)][0]
    return occurence_list

def generate_prices(num_clients): # RETURNS ARRAY (Index Accordingly)
    num_jobs = [1,2,3]
    pricing_list = []
    for x in range(num_clients):
        jobs = random.choices(num_jobs, weights=(.66, .31, .03))[0]
        roll = random.randint(1,100)
        window_range = generate_ranges(40,130,110,200,210,300,360,450,660,840)
        pressure_wash_range = generate_ranges(60,150,210,300,430,580,640,840,910,1140)
        handywork_range = generate_ranges(30,90,60,150,160,280,340,480,640,960)
        windows_price, pressure_wash_price, handywork_price = 0, 0, 0
        if jobs == 1:
            if roll > 12 and roll <= 100:
                windows_price += window_range
            if roll > 4 and roll <= 12:
                pressure_wash_price += pressure_wash_range
            if roll > 0 and roll <= 4:
                handywork_price += handywork_range   
        elif jobs == 2:
            if roll > 34 and roll <= 100:
                windows_price += window_range
                pressure_wash_price += pressure_wash_range
            if roll > 3 and roll <= 34:
                windows_price += window_range
                handywork_price += handywork_range
            if roll > 0 and roll <= 3:
                pressure_wash_price += pressure_wash_range
                handywork_price += handywork_range
        elif jobs == 3:
                windows_price += window_range
                pressure_wash_price += pressure_wash_range
                handywork_price += handywork_range
        pricing_list.append([windows_price, pressure_wash_price, handywork_price])
    return pricing_list

def generate_window_price(num_clients, job_pricing):
    window_price_list = []
    for x in range(num_clients):
        window_price_list.append(job_pricing[x][0])
    return window_price_list
        
def generate_pressure_wash_price(num_clients, job_pricing):
    pressure_wash_price_list = []
    for x in range(num_clients):
        pressure_wash_price_list.append(job_pricing[x][1])
    return pressure_wash_price_list

def generate_handywork_price(num_clients, job_pricing):
    handywork_price_list = []
    for x in range(num_clients):
        handywork_price_list.append(job_pricing[x][2])
    return handywork_price_list

def generate_annual_revenue(num_clients, windows, pressure_wash, handywork, occurence):
    revenue_list = []
    for x in range(num_clients):
        total = (windows[x] + pressure_wash[x] + handywork[x]) * occurence[x]
        revenue_list.append(total)
    return revenue_list

def generate_expenses(num_clients, city, annual_revenue):
    expense_list = []
    for x in range(num_clients):
        expenses = 0
        if city[x] == 'Coronado':
            short_distance_gas_price = random.randint(3,12)
            expenses+=(((annual_revenue[x] * .05) + short_distance_gas_price))
        else: 
            long_distance_gas_price = random.randint(9, 28)
            expenses+=(((annual_revenue[x] * .05) + long_distance_gas_price))
        expense_list.append(expenses)
    return expense_list

def generate_annual_profit(num_clients, revenue, expenses):
    profit_list = []
    for x in range(num_clients):
        profit_list.append((revenue[x] - expenses[x]))
    return profit_list

def generate_master_list(num_clients, names, address, phone, city, email, client_type, client_acquisition,
                         client_occurence, windows_price, pressure_wash_price, handywork_price, expenses,profit):
    generated_list = []
    for x in range(num_clients):
        loop_list = [
            names[x], address[x], phone[x], city[x], email[x], client_type[x], client_acquisition[x],
            client_occurence[x], windows_price[x], pressure_wash_price[x], handywork_price[x],
            expenses[x], profit[x]]
        generated_list.append(loop_list)
    return generated_list

# Misc Functions      
def generate_ranges(L1,H1,L2,H2,L3,H3,L4,H4,L5,H5):
    range_list = [
        random.randrange(L1,H1,10),
        random.randrange(L2,H2,10),
        random.randrange(L3,H3,10),
        random.randrange(L4,H4,10),
        random.randrange(L5,H5,10)]
    weighted_choice = random.choices(range_list, weights=(.15, .25, .40, .15, .05))[0]
    return weighted_choice