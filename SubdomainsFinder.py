# import module
import requests


# function for scanning subdomains
def domain_scanner(domain_name, sub_subdomains):
    print(f'Found Subdomains in {domain_name}')

    # loop for getting URL's
    for subdomain in sub_subdomains:

        url = f"https://{subdomain}.{domain_name}"

        try:
            requests.get(url)
            print(f' {url}')


        except requests.ConnectionError:
            pass


# main function
if __name__ == '__main__':
    dom_name = input("Enter the Domain Name to scan: ")

    # opening the subdomain text file
    with open('subdomains.txt', 'r') as file:
        f = file.read()

        sub_domain = f.splitlines()

    domain_scanner(dom_name, sub_domain)
