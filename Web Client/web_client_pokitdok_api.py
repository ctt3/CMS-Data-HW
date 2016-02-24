
# coding: utf-8

# <div class="text-center"><span><h1>Simple Eligibility Request</h1></span><span><h4>Charlie Thiry - February 22, 2016</h4></span></div>

# ### Import PokItDok

# In[2]:

import pokitdok


# ### Connect to API

# In[17]:

pd = pokitdok.api.connect('E8zKmnqqOyp7adXyqMBh', 'h4F3Fbigiudk2nDvaRW4nN5JMCUdxaggMJkmeF7m')


# ### Submit Eligibility Request

# In[18]:

response = pd.eligibility({
    "member": {
        "birth_date": "1970-01-01",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "trading_partner_id": "MOCKPAYER"
})


# ### Define Helper Methods

# In[5]:

def filter_for_service(service_type, response):
  return filter(
    (lambda x: 'service_types' in x.keys() and service_type in x['service_types']),
    response
    )


# ### Display Copay

# In[19]:

copays = filter_for_service('professional_physician_visit_office', response['data']['coverage']['copay'])
for copay in copays: print copay


# ### Display Deductibles

# In[16]:

print response['data']['summary']['deductible']

