from requests_html import HTMLSession

url = 'https://world.einnews.com/all_countries'

session = HTMLSession()
response = session.get(url)
area_list = response.html.xpath("//h2/a[contains(text(), 'Africa')]/@href")[3::]
regions = [region.replace('/region/', '') for region in area_list]
# output regions ['african-island-nations', 
#            'central-africa', 'east-africa', 
#            'horn-of-africa', 'north-africa', 
#            'southern-africa', 'west-africa']

