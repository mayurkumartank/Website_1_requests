import json
import requests
from bs4 import BeautifulSoup

output_data = []

def start_request():
    url = "https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml"

    payload = 'bidSearchResultsForm=bidSearchResultsForm&_csrf=8526c715-ed93-4594-89ca-863aec911199&openBids=true&javax.faces.ViewState=-589997388001284584%3A8092902019790315594&bidSearchResultsForm%3AbidResultId%3Aj_idt373=bidSearchResultsForm%3AbidResultId%3Aj_idt373'
    headers = {
    'authority': 'nevadaepro.com',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'primefaces.download=true; JSESSIONID=CCDA245F5520CA3BCC27B8FCA1CC985C; XSRF-TOKEN=8526c715-ed93-4594-89ca-863aec911199; _ga=GA1.1.1174908931.1704884641; dtCookie=v_4_srv_4_sn_69460D8CE47FD1054DCA10343E8AD49F_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0; _ga_JGSX0KVE09=GS1.1.1705485801.8.1.1705487474.0.0.0; AWSALB=+waOEP/JroQjOIp0gn17Kaf7e2BxNJnJmOd0nnUPmm/Jn3kEmQmxLnWssNUBrVIljGyKrAVFO9st9GAAJ1WQIoBtqTUDtTKt/Kuu8Xf1msEu+Q63MVAPrtmZuaUq; AWSALBCORS=+waOEP/JroQjOIp0gn17Kaf7e2BxNJnJmOd0nnUPmm/Jn3kEmQmxLnWssNUBrVIljGyKrAVFO9st9GAAJ1WQIoBtqTUDtTKt/Kuu8Xf1msEu+Q63MVAPrtmZuaUq; primefaces.download=true; JSESSIONID=FF5A82C4F0A4AAB8D83741CAFB16426D; XSRF-TOKEN=7f7247a8-8b31-47fc-983c-c9040fdc589e; AWSALB=iw0r2rTOE+mtyK/CAt1YKHg3efHWj7l40ZFRkwHr1EFcjo4lHiMQGbteR6aAsBJE76FDdXMGKqQXlDyXOL9k8zxCTPab91JR0BrGFsW0PnFqzlXmom16BxbQ6Lm0; AWSALBCORS=iw0r2rTOE+mtyK/CAt1YKHg3efHWj7l40ZFRkwHr1EFcjo4lHiMQGbteR6aAsBJE76FDdXMGKqQXlDyXOL9k8zxCTPab91JR0BrGFsW0PnFqzlXmom16BxbQ6Lm0; dtCookie=v_4_srv_12_sn_452E5690BF9E97739CA4ADC410F5F027_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0',
    'origin': 'https://nevadaepro.com',
    'referer': 'https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml?openBids=true',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    lines = response.text.split("\n")

    bid_solicitations = set()

    for line in lines[1:]:
        try:
            bid_solicitation = line.split('"')[1]
            bid_solicitations.add(bid_solicitation)
        except IndexError:
            pass

    bid_solicitations_list = list(bid_solicitations)

    for i in bid_solicitations_list:
        url = f"https://nevadaepro.com/bso/external/bidDetail.sdo?docId={i}&external=true&parentUrl=close"
        response = requests.get(url, headers=headers)

        response = requests.get(url, headers=headers)
        response = BeautifulSoup(response.content, 'html.parser')
        fetch_data(response)

def fetch_data(response):

    try:
        bid_number = response.find('td', string='Bid Number:').find_next('td').get_text(strip=True)
    except:
        bid_number = ""
    try:
        description = response.find('td', string="Description:").find_next('td').get_text(strip=True)
    except:
        description = ""
    try:
        bid_opening_date = response.find('td', string="Bid Opening Date:").find_next('td').get_text(strip=True)
    except:
        bid_opening_date = ""
    try:
        purchaser = response.find('td', string="Purchaser:").find_next('td').get_text(strip=True)
    except:
        purchaser = ""
    try:
        organization = response.find('td', string="Organization:").find_next('td').get_text(strip=True)
    except:
        organization = ""
    try:
        department = response.find('td', string="Department:").find_next('td').get_text(strip=True)
    except:
        department = ""
    try:
        location = response.find('td', string="Location:").find_next('td').get_text(strip=True)
    except:
        location = ""
    try:
        fiscal_year = response.find('td', string="Fiscal Year:").find_next('td').get_text(strip=True)
    except:
        fiscal_year = ""
    try:
        type_code = response.find('td', string="Type Code:").find_next('td').get_text(strip=True)
    except:
        type_code = ""
    try:
        allow_electronic_quote = response.find('td', string="Allow Electronic Quote:").find_next('td').get_text(strip=True)
    except:
        allow_electronic_quote = ""
    try:
        alternate_id = response.find('td', string="Alternate Id:").find_next('td').get_text(strip=True)
    except:
        alternate_id = ""
    try:
        required_date = response.find('td', string="Required Date:").find_next('td').get_text(strip=True)
    except:
        required_date = ""
    try:
        available_date = response.find('td', string="Available Date").find_next('td').get_text(strip=True)
    except:
        available_date = ""
    try:
        info_contact = response.find('td', string="Info Contact:").find_next('td').get_text(strip=True)
    except:
        info_contact = ""
    try:
        bid_type = response.find('td', string="Bid Type:").find_next('td').get_text(strip=True)
    except:
        bid_type = ""
    try:
        informal_bid_flag = response.find('td', string="Informal Bid Flag:").find_next('td').get_text(strip=True)
    except:
        informal_bid_flag = ""
    try:
        purchase_method = response.find('td', string="Purchase Method:").find_next('td').get_text(strip=True)
    except:
        purchase_method = ""
    try:
        pre_bid_conference = response.find('td', string="Pre Bid Conference:").find_next('td').get_text(strip=True)
    except:
        pre_bid_conference = ""
    try:
        bulletin_desc = response.find('td', string="Bulletin Desc:").find_next('td').get_text(strip=True)
    except:
        bulletin_desc = ""
    try:
        ship_to_address = response.find('td', string="Ship-to Address:").find_next('td').get_text(strip=True)
    except:
        ship_to_address = ""
    try:
        bill_to_address = response.find('td', string="Bill-to Address:").find_next('td').get_text(strip=True)
    except:
        bill_to_address = ""
    bid_data = {
                "Bid Solicitation": bid_number,
                "Buyer": purchaser,
                "Description": description,
                "Bid Opening Date": bid_opening_date,
                "Bid Number": bid_number,
                "Purchaser": purchaser,
                "Organization": organization,
                "Department": department,
                "Location": location,
                "Fiscal Year": fiscal_year,
                "Type Code": type_code,
                "Allow Electronic Quote": allow_electronic_quote,
                "Alternate Id": alternate_id,
                "Required Date": required_date,
                "Available Date": available_date,
                "Info Contact": info_contact,
                "Bid Type": bid_type,
                "Informal Bid Flag": informal_bid_flag,
                "Purchase Method": purchase_method,
                "Pre Bid Conference": pre_bid_conference,
                "Bulletin Desc": bulletin_desc,
                "Ship-to Address": ship_to_address,
                "Bill-to Address": bill_to_address
            }

    output_data.append(bid_data)

def write_output(output_data):
    with open("output_task_1.json", "w") as json_file:
        json.dump(output_data, json_file, indent=2)

start_request()
write_output(output_data)