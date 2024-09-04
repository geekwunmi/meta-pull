import requests
import json
import datetime as dt

# Define Parameters Dictionary
def basic_insights():
    params = dict()
    params['access_token'] = ''        # not an actual access token
    params['client_id'] = ''                  # not an actual client id
    params['client_secret'] = ''     # not an actual client secret
    params['graph_domain'] = 'https://graph.facebook.com'
    params['graph_version'] = 'v20.0'
    params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
    params['page_id'] = ''                  # not an actual page id
    params['instagram_account_id'] = ''        # not an actual instagram business account id
    params['ig_username'] = 'adeotaku'

    ###########################################################################
    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'

    #Define Endpoint Parameters
    endpointParams = dict()
    endpointParams['fields'] = 'id,timestamp,comments'
    endpointParams['access_token'] = params['access_token']

    #Requests Data
    data = requests.get(url, endpointParams)
    basic_insight = json.loads(data.content)
    print(basic_insight)

basic_insights()
