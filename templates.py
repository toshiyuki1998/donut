TEMPLATES = {
    "template_name": ["inv_01b"],
    "見積書": {
        "title": {"B4": "word"},
        "date": {
            "key": {"H4": "title"},
            "value": {"J4": "date"}
        },
        "document_number": {
            "key": {"H5": "title"},
            "value": {"J5": "string"},
        },
        "billed_company": {
            "name": {"B8": "company"},
            "dear": {"D8": "word"},
            "address": {"B9": "zipcode_and_address"},
        },
        "billing_company": {
            "name": {"H8": "company"},
            "zipcode": {"H9": "zipcode"},
            "address": {"H10": "address"},
            "number": {"H11": "string"},
            "tel": {"H12": "tel"},
            "fax": {"H13": "tel"},
            "employee": {"H14": "name"},
        },
        "billing_message": [
            {
                "key": {"B11": "title"},
                "value": {"C11": "word"}
            },
            {
                "key": {"B12": "title"},
                "value": {"C12": "word"}
            },
            {
                "key": {"B13": "title"},
                "value": {"C13": "word"}
            },
            {
                "key": {"B14": "title"},
                "value": {"C14": "word"}
            },
            {
                "key": {"B15": "title"},
                "value": {"C15": "word"}
            },
        ],
        "amount": {
            "key": {"B17": "word"},
            "value": {"C17": "amount"},
            "unit": {"E17": "word"},
        },
        "items": [
            {
                "name": {"B20": "word",},
                "mitigation": {"E20": "word"},
                "number": {"F20": "word"},
                "unit_price": {"H20": "word"},
                "tax": {"I20": "word",},
                "price": {"J20": "word"},
            },
            {
                "name": {"B21": "word"},
                "mitigation": {"E21":"punctuation"},
                "number": {"F21":"num"},
                "number_unit": {"G21":"unit"},
                "unit_price": {"H21": "amount"},
                "tax": {"I21": "percentage"},
                "price": {"J21": "amount"},
            },
            {
                "name": {"B22": "word"},
                "mitigation": {"E22":"punctuation"},
                "number": {"F22":"num"},
                "number_unit": {"G22":"unit"},
                "unit_price": {"H22": "amount"},
                "tax": {"I22": "percentage"},
                "price": {"J22": "amount"},
            },
            {
                "name": {"B23": "word"},
                "mitigation": {"E23":"punctuation"},
                "number": {"F23":"num"},
                "number_unit": {"G23":"unit"},
                "unit_price": {"H23": "amount"},
                "tax": {"I23": "percentage"},
                "price": {"J23": "amount"},
            },
        ],
        "tax_total": [
            {
                "key": {"B30": "word"},
                "price": {"C30": "word"},
                "tax": {"D30": "word"},
            },
            {
                "key": {"B31": "word"},
                "price": {"C31": "amount"},
                "tax": {"D31": "amount"},
            },
            {
                "key": {"B32": "word"},
                "price": {"C32": "amount"},
                "tax": {"D32": "amount"},
            },
        ],
        "total": [
            {
                "key": {"H30": "word"},
                "value": {"J30": "amount"},
            },
            {
                "key": {"H31": "word"},
                "value": {"J31": "amount"},
            },
            {
                "key": {"H32": "word"},
                "value": {"J32": "amount"},
            },
        ],
        "remarks": {
            "key": {"B34": "word"},
            "value": {"B35": "text"},
        },
    },
}
