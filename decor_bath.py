from collections import OrderedDict
import pandas as pd
from time import sleep

xlsx_file_path = 'decor bath.xlsx'

data = pd.read_excel(xlsx_file_path, sheet_name=None)

productCount = 0

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
    return row['Group']


def makeTags(row):
    tags = [
        str(row['Company']),
        str(row['Group']),
        str(row['Model no']),
        'Handle',
    ]

    if row['Additional identifier'] != '':
        tags.append(str(row['Additional identifier']))

    if row['HSN'] != '':
        tags.append(str(row['HSN']))

    return ','.join(tags)


def makeColor(row):
    return row['Colour']


def makeSize(row):
    return row['Size']


def makeMaterial(row):
    pass


def makeStyle(row):
    pass


def makeVariantPrice(row):
    return row['MRP']


def makeVariantCompareAtPrice(row):
    pass


def makeCostPerItem(row):
    return row['Cost price']


def makeVariantGrams(row):
    pass


for sheet_name, sheet_df in data.items():
    new_sheet_name = sheet_name.capitalize() + "_" + "Products"

    newRowsList = []

    for index, row in sheet_df.iterrows():
        newRow = OrderedDict()
        for i in fields:
            newRow[i] = ''

        handle = makeHandle(row)
        title = makeTitle(row)
        vendor = makeVendor(row)
        variantPrice = makeVariantPrice(row)
        type = makeType(row)
        tags = makeTags(row)
        options = {}

        if(not pd.isna(row['Colour']) and not pd.isnull(row['Colour']) and not (row['Colour'] == 'NA' or row['Colour'] == 'na')):
            options['Color'] = makeColor(row)

        if(not pd.isna(row['Size']) and not pd.isnull(row['Size']) and (row['Size'] != 'NA' or row['Size'] != 'na')):
            options['Size'] = makeSize(row)

        for i, ele in enumerate(options.keys()):
            newRow[f'Option{i+1} Name'] = ele
            newRow[f'Option{i+1} Value'] = options[ele]
            # print(f"Option{i+1} Name :", newRow[f'Option{i+1} Name'], f"Option{i+1} Value :", newRow[f'Option{i+1} Value'])
        # print(options)
        # print(newRow['Option1 Name'], newRow['Option1 Value'])

        newRow['Handle'] = handle
        newRow['Title'] = title
        newRow['Vendor'] = vendor
        newRow['Variant Price'] = variantPrice
        newRow['Type'] = type
        newRow['Tags'] = tags

        newRow['Variant Taxable'] = 'TRUE'
        newRow['Status'] = 'active'
        newRow['Gift Card'] = 'False'
        newRow["Variant Inventory Policy"] = "deny"
        newRow["Variant Fulfillment Service"] = "manual"

        newRowsList.append(newRow)
        productCount += 1

        # newRow['Option1 Name'] = Option1_Name
        # newRow['Color'] = color

        # print(newRow)
        # Add more columns as needed
        print(f'{index+1}')

    df = pd.DataFrame(newRowsList)

    df.to_csv(f"Items/{new_sheet_name}.csv", index=False)

    print("\n\n\n\n")
    print("Completed for ->", new_sheet_name)
    print("Product Count so far -> ", productCount)
    input()
