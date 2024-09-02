import pandas as pd
import requests
import json
import datetime as dt

# Define Parameters Dictionary
def basic_insights():
    params = dict()
    params['access_token'] = 'EAAOAWnjWQbIBOzIZCyyeDgxmFMqK76nyojgCYIWuZChdLFFq36nb1KDmPM5SyG1FkSA09nlKlO78U9PnfO6n81tEpM9BZC9XMHGZCIMWbUZACrbgJZAVqii2Vu6lQTUSt4lnTiS1ixW938ZCIdTk8PanKcSJZBw6lyfKWZALgEZBhn3ZA58VTFv9LlkHFMZAqAT0QKgWsZAXXdTAMv0OIs8waRjrefd9I'        # not an actual access token
    params['client_id'] = '985550992851378'                  # not an actual client id
    params['client_secret'] = '780162769e3f77fc645457e2a1e0ad04'     # not an actual client secret
    params['graph_domain'] = 'https://graph.facebook.com'
    params['graph_version'] = 'v20.0'
    params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
    params['page_id'] = '377815892087557'                  # not an actual page id
    params['instagram_account_id'] = '17841467476787144'        # not an actual instagram business account id
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



    #turn data into dataframe
    # df = pd.DataFrame(basic_insight['data'])
    # df.columns = ['id', 'Timestamp', 'Username', 'Likes', 'Comments']
    # print(df.head())
