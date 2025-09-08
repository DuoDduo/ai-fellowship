================= AGROUSSD FLOW TREE (UPDATED) =================

1. Start
   └── Select Language
       ├── 1. English → Main Menu
       ├── 2. Hausa → Main Menu
       ├── 3. Yoruba → Main Menu
       └── 4. Igbo → Main Menu

------------------------------------------------------
2. Main Menu
   ├── 1. Register Farmer
   │     → Enter Full Name
   │     → Enter Age
   │     → Enter Location
   │     → Select Primary Product Category
   │          1. Crops
   │          2. Livestock
   │          3. Processed Goods
   │     → Choose Product
   │          • From predefined list OR
   │          • Enter product manually
   │     → Set 4-digit PIN
   │     → Confirm PIN
   │     → Registration Success → Redirect to Login Farmer

   ├── 2. Register Buyer
   │     → Enter Full Name
   │     → Enter Location
   │     → Set 4-digit PIN
   │     → Confirm PIN
   │     → Registration Success → Redirect to Login Buyer

   ├── 3. Login Farmer
   │     → Enter Registered Name/Phone
   │     → Enter PIN
   │        ├── Success → Farmer Dashboard
   │        │
   │        │   Farmer Dashboard Options:
   │        │   ├── 1. Record Harvest
   │        │   │     → Select Category
   │        │   │          • Crops
   │        │   │          • Livestock
   │        │   │          • Processed Goods
   │        │   │     → Choose Product (list OR manual input)
   │        │   │     → Enter Quantity
   │        │   │     → Enter Asking Price
   │        │   │     → Confirm Save
   │        │   │     → Harvest Saved → Back to Dashboard
   │        │   │
   │        │   ├── 2. View Market Prices
   │        │   │     → Select Category
   │        │   │     → Choose Product
   │        │   │     → Display Prices by Market
   │        │   │          • Kano
   │        │   │          • Abuja
   │        │   │          • Lagos
   │        │   │          • Kaduna
   │        │   │     → Option: Compare Markets
   │        │   │
   │        │   ├── 3. Buyer Directory
   │        │   │     → Search Buyers by Location
   │        │   │     → Show List of Buyers
   │        │   │          • Buyer Name
   │        │   │          • Buyer Location
   │        │   │          • Buyer Contact (Phone)
   │        │   │     → Back to Dashboard
   │        │   │
   │        │   ├── 4. Profile & Settings
   │        │   │     → Update Location
   │        │   │     → Update Products (choose category + product again)
   │        │   │     → Change PIN
   │        │   │     → Back
   │        │   │
   │        │   └── 5. Logout → End Session
   │        │
   │        └── Fail → Retry (Max 3 attempts)
   │              └── Option: Reset PIN
   │                   → Verify Identity (Name + Location)
   │                   → Enter New 4-digit PIN
   │                   → Confirm New PIN
   │                   → PIN Reset Successful → Redirect to Login Farmer

   ├── 4. Login Buyer
   │     → Enter Registered Name/Phone
   │     → Enter PIN
   │        ├── Success → Buyer Dashboard
   │        │
   │        │   Buyer Dashboard Options:
   │        │   ├── 1. View Available Products
   │        │   │     → Select Category
   │        │   │          • Crops
   │        │   │          • Livestock
   │        │   │          • Processed Goods
   │        │   │     → Choose Product (list OR input manually)
   │        │   │     → Display Available Products:
   │        │   │          • Product Name
   │        │   │          • Quantity
   │        │   │          • Price
   │        │   │          • Farmer Name
   │        │   │          • Farmer Location
   │        │   │          • Farmer Contact (Phone)
   │        │   │     → Option: Call/SMS Farmer
   │        │   │     → Back to Dashboard
   │        │   │
   │        │   ├── 2. Market Prices
   │        │   │     → Select Category
   │        │   │     → Choose Product
   │        │   │     → Show Current Prices by Market
   │        │   │     → Option: Compare Markets
   │        │   │
   │        │   ├── 3. Profile & Settings
   │        │   │     → Update Location
   │        │   │     → Change PIN
   │        │   │     → Back
   │        │   │
   │        │   └── 4. Logout → End Session
   │        │
   │        └── Fail → Retry (Max 3 attempts)
   │              └── Option: Reset PIN
   │                   → Verify Identity (Name + Location)
   │                   → Enter New 4-digit PIN
   │                   → Confirm New PIN
   │                   → PIN Reset Successful → Redirect to Login Buyer

   ├── 5. Market Prices (Guest Access)
   │     → Select Category
   │     → Choose Product (list OR input manually)
   │     → Show Prices by Market
   │     → Option to Compare
   │     → Back

   └── 6. Exit → End Session

------------------------------------------------------
3. Navigation Shortcuts (USSD Standards)
   - *0 → Back
   - *9 → Main Menu
   - #00 → Exit

======================================================
