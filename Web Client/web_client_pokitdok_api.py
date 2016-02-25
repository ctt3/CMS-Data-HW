#Import Dependencies
import pokitdok
import webbrowser, os.path

# Connect to API
pd = pokitdok.api.connect('E8zKmnqqOyp7adXyqMBh', 'h4F3Fbigiudk2nDvaRW4nN5JMCUdxaggMJkmeF7m')

# Submit Eligibility Request
response = pd.eligibility({
    "member": {
        "birth_date": "1970-01-01",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "trading_partner_id": "MOCKPAYER"
})

# Define Helper Methods
def filter_for_service(service_type, response):
  return filter(
    (lambda x: 'service_types' in x.keys() and service_type in x['service_types']),
    response
    )

def print_to_file(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()


# Extract copays and deductible
copays = filter_for_service('professional_physician_visit_office', response['data']['coverage']['copay'])
deductible = response['data']['summary']['deductible']

# Interpolate into HTML for display
html = """
    <html>
        <body>
            <h1>Copays JSON</h1>
            <div id='copay_area'>%r</div>
            <h1>Deductible JSON</h1>
            <div id='deductible_area'>%r</div>
        </body>
    </html>
    """ % (copays, deductible)

# Print HTML to file, open in browser
print_to_file(html, "web_client_output.html")
webbrowser.open("file:///" + os.path.abspath("web_client_output.html"))