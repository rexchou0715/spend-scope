# Define keyword-to-category mapping for expenses (Debit)
expense_keywords = {
    'Groceries': [
        'Supermarket', 'Groceries', 'Albert Heijn', 'Jumbo', 'Amazing Oriental', 'Lidl', 'ALL IN SUPERMARKT',
        'Supermarkt Lowiczanka', 'AH', 'Ochama', 'University Shop UU UTRECHT NLD', 'SPAR', 'RIMI', 'Elvi',
        'MAXIMA', 'ALDI', 'Australian', 'Dirk', 'Agnes Harms', 'Time4t Utrecht'
    ],
    'Dining': [
        'Restaurant ', 'Café ', 'Cinema ', 'Pub ', 'Bar ', 'Bars', "McDonald's", 'MCDONALDS', 'MCD', 'KFC', 'STARBUCKS',
        'Pancakes', 'LIDO', 'GRAND CAFE LEBOWSKI', 'COCOLO RAMEN', 'Bistro', 'Ezitis Migla', 'Jozef eten en drinken',
        'Horeca', 'BK', 'Burger King', 'LS Oakberry', 'Bubble Tea', 'Letex', 'IKEA Restaurant', 'Swedish Food', 'COFYZ',
        'Pizza', 'Panuozzo', 'KOHVIK', 'Levain', 'Kims So', 'Wittys', 'THEEHUIS', 'MAAS', 'RADISSON', 'NYX', 'KIMMADE',
        'Kiosk', 'IJskiosk', 'Uncles Canteen', 'SONMAT', 'EL GRECO', 'THE FLORIN', 'T OUDE POTHUYS', 'HSUtrecht015',
        'HMSHost', 'Belgisch Biercafé', 'Food Mood', 'GINGER RIGA LVA', 'Biercafe', 'Shokudo', 'Vermolen',
        'Aux Merveilleux de Fred', 'Saes Foodexpress', 'Gan Bei Barona', 'Pizzeria Tricolore V.o.f.',
        'Cafetaria Ten Beste Corne', 'St. Cambridgebar', 'Vlaams Fritehuis van Gogh', 'Osozai Japanese Deli',
        'Saigon Gelderlandplein', 'FamilyMart', 'Muzikas Nams Daile', 'Coffee Address', 'Bakery', 'Noodle', 'Food',
        'Kong Izakaya', 'Boulangerie', 'Villa Orloff', 'Kodiak Zeeland', 'Bellamy Holding', 'Shou Szu', 'San Shang',
        'Dun Yong'
    ],
    'Entertainment': [
        'EKKO', 'ESN ', 'BuddyGoDutch', 'Fest en Pure', 'PAY.nl Play', 'SoLow', 'Vof Witstijn Van Dam',
        'Eye Filminstituut Nederla', 'Depot Boijmans'
    ],
    'Utilities': [
        'Utility', 'Electricity', 'Water', 'Gas', 'Internet',
        'Plaza Resident Services Nederland B via Stichting Mollie Payments', 'Lebara', 'Miele'
    ],
    'Insurance': ['AON'],
    'Rent': [
        'Rent', 'Landlord', 'Mortgage', 'Camelot Vastgoedbeheer', 'Mosaic World BV',
        'Plaza Resident Services', 'OCO Toren B.V.'
    ],
    'Transportation': [
        'Fuel', 'Train', 'Bus', 'NS ', 'Uber', 'Taxi', 'OV', 'Ticketservice', 'PYD', 'SERVICEWINKEL', 'MOL'
    ],
    'Fitness': ['BasicFit', 'Van Slag', 'Sportcentrum Olympos', 'Decathlon', 'MYPROTEIN'],
    'Medical': [
        'C.P. Goosen Tandarts', 'Lin C T', 'Holland & Barrett', 'Riga 1st hospital',
        'Great Tree Pharmacy', 'Howard Eyewear'
    ],
    'Shopping/Personal Care': [
        'Kruidvat', 'Etos', 'Rituals', 'NORMAL', 'Holland & Barrett '
    ],
    'Shopping/Clothing': [
        'Primark', 'H&M', 'Zalando', 'Uniqlo', 'Snipes', 'Zara', 'Zeeman', 'G Star Raw', 'Merchstore'
    ],
    'Shopping/Electronics': ['MediaMarkt', 'Bol.com', 'Coolblue', 'Apple'],
    'Shopping/Home Goods': ['IKEA', 'Blokker', 'Action', 'HEMA'],
    'Shopping/Miscellaneous': [
        'Amazon', 'AliExpress', 'TK Maxx', 'Flying Tiger', 'SIA AMBER DISTRIBUTION RIGA LVA', 'Janis Roze', 'Xenos',
        'Alipay', 'LEGO Store', 'Far Eastern Department Stores', 'Feestwinkel Witbaard Utrecht', 'tiger'
    ],
    'Shopping/Gift': ['PANDORA'],
    'Education': ['University', 'UNIVERSITEIT', 'Xerox', 'Udemy'],
    'Travel': [
        'KLM', 'Hotel', 'BerlinBrandenburg', 'Ryanair', 'EasyJet', 'airBaltic', 'Citybox Tallinn',
        'Lagardère Travel Retail'
    ],
    'Taxes': ['Tax', 'Belastingdienst'],
    'Repairs': ['Bike Repair', 'City Bike', 'CELIL CITY BIKE'],
    'Facilities': ['One Hundred Northern', 'Public Toilet', 'Restroom', 'SANIFAIR'],
    'Adminstration Fee': ['Trans.Reference', 'holland2stay'],
    'Miscellaneous': [
        'Gift', 'Donation', 'Orderli B.V.', 'Tiqets', 'CM Tickets', 'Gantner', 'Tim Vandeput', 'Kroonenberg Groep', 'Pay.nl'
    ],
    'Transfers': ['Tikkie', 'Transfer', 'Hr', 'Geldmaat', 'Kevin', 'To '],
    'Top Up': ['Revolut']
}


# Define keyword-to-category mapping for income (Credit)
income_keywords = {
    'Salary': ['Salary' , 'Payroll' , 'Employer'],
    'Deposit': ['Deposit', 'Bank Transfer ', 'Incoming '],
    'Refund': ['Refund', 'Return', 'Plaza Resident ServicesNederland '],
    'Insurance Claim': ['AON Nederland C.V.'],
    'Living Allowance': ['Trans.Reference'],
    'Reimbursement': ['AAB INZ TIKKIE', 'SHARED PACKAGING', 'D VIGANTE', 'NS '],
    'Government Allowance': ['BELASTINGDIENST'],
    'Top Up': ['Top-Up' , 'Top Up'],
    'Others': ['Gift' , 'Bonus ', 'Rebate ', 'Referral'],
}