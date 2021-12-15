""" Program to return Company name with highest and lowest stock value.
 Interview question asked in Tiger Analytics for Data Engineer """


def CompanyName(company):
    maxm = max(company.values())
    minm = min(company.values())
    return [k for k, v in company.items() if v == minm], [k for k, v in company.items() if v == maxm]


if __name__ == '__main__':
    company = {'Axis Bank': 4, 'TCS': 11, 'Infosys': 9, 'HCL': 3, 'Wipro': 1,
                       'Standard Chartered': 7}
    print(CompanyName(company))
