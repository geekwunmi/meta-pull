import pandas as pd
import requests
import json
import datetime as dt

# Define Parameters Dictionary
params = dict()
params['access_token'] = 'XXXXXXXXXXXXXXXXXXX'        # not an actual access token
params['client_id'] = '111111111111'                  # not an actual client id
params['client_secret'] = '000000000XXXXXXXXXXXX'     # not an actual client secret
params['graph_domain'] = 'https://graph.facebook.com'
params['graph_version'] = 'v12.0'
params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
params['page_id'] = '22222222222222'                  # not an actual page id
params['instagram_account_id'] = '33333333333'        # not an actual instagram business account id
params['ig_username'] = 'galihputrala'
