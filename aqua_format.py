from collections import OrderedDict
import pandas as pd
from time import sleep
import json
# Replace 'your_file.xlsx' with the actual path to your Excel file
xlsx_file_path = 'test.xlsx'

# Read the Excel file into a pandas DataFrame
data = pd.read_excel(xlsx_file_path)
# Now you can work with the 'data' DataFrame
# For example, you can print the first few rows
# print(data.head())
fields = [
    "Handle",
    "Title",
    "Vendor",
    "Product Category",
    "Type",
    "Tags",
    "Published",
    "Option1 Name",
    "Option1 Value",
    "Option2 Name",
    "Option2 Value",
    "Option3 Name",
    "Option3 Value",
    "Variant SKU",
    "Variant Grams",
    "Variant Inventory Tracker",
    "Variant Inventory Qty",
    "Variant Inventory Policy",
    "Variant Fulfillment Service",
    "Variant Price",
    "Variant Compare At Price",
    "Variant Requires Shipping",
    "Variant Taxable",
    "Variant Barcode",
    "Image Src",
    "Image Position",
    "Image Alt Text",
    "Gift Card",
    "SEO Title",
    "SEO Description	",
    "Google Shopping / Google Product Category	",
    "Google Shopping / Gender	",
    "Google Shopping / Age Group	",
    "Google Shopping / MPN	",
    "Google Shopping / AdWords Grouping	",
    "Google Shopping / AdWords Labels	",
    "Google Shopping / Condition	",
    "Google Shopping / Custom Product	",
    "Google Shopping / Custom Label 0	",
    "Google Shopping / Custom Label 1	",
    "Google Shopping / Custom Label 2	",
    "Google Shopping / Custom Label 3	",
    "Google Shopping / Custom Label 4	",
    "Variant Image	",
    "Variant Weight Unit	",
    "Variant Tax Code	",
    "Cost per item	",
    "Price / International	",
    "Compare At Price / International",
    "Status",
]


def filterText(inp):
    return "-".join(str(inp).strip().split()).lower()


def makeHandle(row):
    productCode = filterText(
        row['Company']) + "-" + filterText(row['Group'])
    if(not pd.isna(row['Model no']) and not pd.isnull(row['Model no'])):
        productCode += '-' + filterText(row['Model no'])
    productCode = "-".join(productCode.split())
    return productCode


def makeTitle(row):
    title = [str(row['Company']), str(row['Group']), str(row['Model no'])]
    return " ".join(title)


def makeBody(row):
    pass


def makeVendor(row):
    return row['Company']


def makeProductCategory(row):
    return 'Home & Garden > Bathroom Accessories > Soap Dishes & Holders'


def makeType(row):
    if not pd.isna(row['Group']) and not pd.isnull(row['Group']) and row['Group'] != '':
        return row['Group']
    else:
        return "GRP 101"


def makeTags(row):
    tags = [
        str(row['Company']),
        str(row['Group']),
        str(row['Model no']),
        'Handle',
    ]

    if not pd.isna(row['Additional identifier']) and not pd.isnull(row['Additional identifier']) and row['Additional identifier'] != '':
        tags.append(str(row['Additional identifier']))

    if not pd.isna(row['HSN']) and not pd.isnull(row['HSN']) and row['HSN'] != '':
        tags.append(str(row['HSN']))

    return tags


def makeColor(row):
    return row['Colour']


def makeSize(row):
    return row['Size']


def makeMaterial(row):
    pass


def makeStyle(row):
    pass


def makeVariantPrice(row):
    if not pd.isna(row['MRP']) and not pd.isnull(row['MRP']) and row['MRP'] != '' and row['MRP'] != "nan":
        return row['MRP']
    else:
        return 1000


def makeVariantCompareAtPrice(row):
    pass


def makeCostPerItem(row):
    return row['Cost price']


def makeVariantGrams(row):
    pass


newRowsList = []

for index, row in data.iterrows():
    newRow = OrderedDict()

    # print(f"Row index: {index}")
    # print(f"Company: {row['Company']}")  # Replace 'ColumnA' with the actual column name
    # print(f"Model no: {row['Model no']}")  # Replace 'ColumnB' with the actual column name
    # print(f"Additional identifier: {row['Additional identifier']}")
    handle = makeHandle(row)
    title = makeTitle(row)
    type = makeType(row)
    company = makeVendor(row)
    variantPrice = makeVariantPrice(row)
    tags = makeTags(row)
    options = {}

    if(not pd.isna(row['Colour']) and not pd.isnull(row['Colour']) and not (row['Colour'] == 'NA' or row['Colour'] == 'na')):
        options['color'] = makeColor(row)

    if(not pd.isna(row['Size']) and not pd.isnull(row['Size']) and (row['Size'] != 'NA' or row['Size'] != 'na')):
        options['size'] = makeSize(row)

    newRow["variant"] = {}

    for i, ele in enumerate(options.keys()):
        newRow["variant"][ele] = options[ele]
        # print(f"Option{i+1} Name :", newRow[f'Option{i+1} Name'], f"Option{i+1} Value :", newRow[f'Option{i+1} Value'])
    # print(options)
    # print(newRow['Option1 Name'], newRow['Option1 Value'])

    # newRow['Handle'] = handle
    newRow['company'] = company
    newRow['productCode'] = handle
    newRow['productTitle'] = title
    newRow['productType'] = type
    if not pd.isna(row['Model no']) and not pd.isnull(row['Model no']) and row['Model no'] != '':
        newRow['modelNumber'] = str(row['Model no'])
    else:
        newRow['modelNumber'] = f"RP {index + 1}"
    newRow['productCategory'] = 'decor bath'
    newRow['tags'] = tags
    newRow['mrp'] = variantPrice

    if not pd.isna(row['Additional identifier']) and not pd.isnull(row['Additional identifier']) and row['Additional identifier'] != '':
        newRow['additionalIdentifier'] = str(row['Additional identifier'])
    if not pd.isna(row['HSN']) and not pd.isnull(row['HSN']) and row['HSN'] != '':
        newRow['hsn'] = str(row['HSN'])

    # newRow['Variant Taxable'] = 'TRUE'
    # newRow['Status'] = 'active'
    # newRow['Gift Card'] = 'False'
    # newRow["Variant Inventory Policy"] = "deny"
    # newRow["Variant Fulfillment Service"] = "manual"

    newRowsList.append(newRow)

    # newRow['Option1 Name'] = Option1_Name
    # newRow['Color'] = color

    # print(newRow)
    # Add more columns as needed
    print(f'{index+1}')

with open("output.json", "w") as json_file:
    json.dump(newRowsList, json_file)
