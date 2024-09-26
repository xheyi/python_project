import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

product_per_company = {}
total_product_value_per_company = {}
for product_row in range(2, product_list.max_row + 1):
    company_name = product_list.cell(product_row, 4).value
    inventory = product_list.cell(product_row, 2).value
    price = product_list.cell(product_row, 3).value

    if company_name in product_per_company:
        current_amount = product_per_company.get(company_name)

        product_per_company[company_name] = current_amount + 1

    else:
        product_per_company[company_name] = 1

    if company_name in total_product_value_per_company:
        current_total = total_product_value_per_company.get(company_name)
        total_product_value_per_company[company_name] = current_total + inventory * price

    else:
        total_product_value_per_company[company_name] = inventory * price

print(product_per_company)
print(total_product_value_per_company)