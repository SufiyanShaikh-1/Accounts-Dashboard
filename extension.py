"""
AccountDashboard Extension
"""

from q2_sdk.core.http_handlers.tecton_server_handler import Q2TectonServerRequestHandler
from q2_sdk.core import q2_requests
from base64 import b64encode
# from q2_sdk.hq.models.db_config.db_config import DbConfig
# from q2_sdk.hq.models.db_config.db_config_list import DbConfigList
# from q2_sdk.hq.models.db_config.db_env_config import DbEnvConfig, EnvValue

from .install.db_plan import DbPlan


class AccountDashboardHandler(Q2TectonServerRequestHandler):

    ## REQUIRED_CONFIGURATIONS is a dictionary of key value pairs that are necessary
    ## for the extension to run. If set, ensures the entries are set in the
    ## extension's settings file or the web server will not start.
    ## Keys are names and values are defaults written into the settings file.
    ## To override the defaults, generate the config (`q2 generate_config`) and
    ## then alter the resulting file

    # REQUIRED_CONFIGURATIONS = {
    #    # 'CONFIG1': 'Default',
    #    # 'CONFIG2': 'Default',
    # }

    # # Behaves the same way as REQUIRED_CONFIGURATIONS, but will not stop the web server
    # # from starting if omitted from the extension's settings file
    # OPTIONAL_CONFIGURATIONS = {}

    # # Behaves in a similar manner to REQUIRED_CONFIGURATIONS,
    # # but stores the data in the database instead of the settings file. Will be
    # # written into the database on `q2 install`
    # WEDGE_ADDRESS_CONFIGS = DbConfigList([
    #     # same default for all environments
    #     DbConfig('enableOptionalLogic', False),
    #
    #     # different defaults for each environment
    #     DbEnvConfig('apiUrl', EnvValue(
    #         dev='https://dev.my-domain.com',
    #         stg='https://stage.my-domain.com',
    #         prod='https://my-domain.com'
    #     ))
    # ])

    # Set this to True if you want to change which Core is configured based on database configuration
    DYNAMIC_CORE_SELECTION = False

    # Set this True if you want your extension to be available to unauthenticated users
    # IS_UNAUTHENTICATED = False

    DB_PLAN = DbPlan()

    FRIENDLY_NAME = 'AccountDashboard'  # this will be used for end user facing references to this extension like Central and Menu items.
    DEFAULT_MENU_ICON = 'landing-page'  # this will be the default icon used if extension placed at top level (not used if a child element)

    CONFIG_FILE_NAME = 'AccountDashboard'  # configuration/AccountDashboard.py file must exist if REQUIRED_CONFIGURATIONS exist

    TECTON_URL = 'https://cdn1.onlineaccess1.com/cdn/base/tecton/v1.32.1/q2-tecton-sdk.js'

    def __init__(self, application, request, **kwargs):
        """
        If you need variables visible through the lifetime of this request,
        feel free to add them in this function
        """
        super().__init__(application, request, **kwargs)
        # self.variable_example = 12345

    # # Uncomment this to allow the IDE to give you better hinting on a specific core (Symitar in this example)
    # from q2_cores.Symitar.core import Core as SymitarCore
    # @property
    # def core(self) -> SymitarCore:

    #     # noinspection PyTypeChecker
    #     return super().core

    @property
    def router(self):
        """
        Your extension's routing map. To handle a request, a method must be listed here. When a POST request is
        made to this extension with a routing_key value, the extension will route the request to the method linked
        to that key. The methods referenced here are defined below.
        """
        router = super().router
        router.update({
            'default': self.default,
            'submit': self.submit,
            # Add new routes here
        })

        return router

    def get(self, *args, **kwargs):
        """
        Most Q2 extensions will be handling POSTs from the Online component, but
        GET requests can also be handled here. If you delete this function, GET
        will simply not be a supported Verb for this extension.
        PUT, DELETE, etc can also be handled by creating an appropriately named
        function. This is based off of Tornado's request handling.
        More info at http://www.tornadoweb.org/en/stable/guide/structure.html?highlight=post#subclassing-requesthandler
        """
        self.write("Hello World GET: From AccountDashboard")

    async def default(self):
        # account_models = []
        # for account in self.account_list:
        #     account_models.append({
        #         'account_num': account.host_acct_id,
        #         'account_name': account.product_name,
        #         'account_balance': account.balance_to_display
        #     })
        accounts_list = await self.get_customers_accounts_by_id()
        # quotes_model = {}
        # rates_dictionary = await self.get_currency_rates()
        # for ccy, rate in rates_dictionary.items():
        #     quotes_model[ccy]=rate
        

        template = self.get_template('index.html.jinja2', {
        'accounts': accounts_list
        })

        html = self.get_tecton_form(
            "CashOS Accounts",
            custom_template=template,
            routing_key="submit",
            hide_submit_button=True
        )
        return html

    async def submit(self):
        """
        This route will be called when your form is submitted, as configured above.
        """
        template = self.get_template(
            'submit.html.jinja2',
            {
                'header': "AccountDashboard",
                'message': 'Hello World POST: From "AccountDashboard".<br>',
                'data': self.form_fields
            }
        )

        html = self.get_tecton_form(
            "AccountDashboard",
            custom_template=template,
            # Hide the submit button as there is no form on this route.
            hide_submit_button=True
        )

        return html

    async def get_currency_rates(self):
        url = "https://api.apilayer.com/currency_data/live?source=USD"

        response = await q2_requests.get(
            self.logger,
            url,
            headers={
                'apikey': 'S6TczFkiWjDZy7FElvqKYMogzdcEcoQy'
            }
        )

        print("Status code is : ", response.status_code)
        print("Request URL is : ",response.request.url)
        print("Request body is : ",response.request.body)
        print("Request headers is : ",response.request.headers)

        response_as_dict = response.json()

        try:
            quotes = response_as_dict['quotes']
            quotes_dictionary = {}

            # Reformat our quotes into a more display friendly format
            for quotes_key, quotes_value in quotes.items():
                new_key = quotes_key[3:]
                quotes_dictionary[new_key] = quotes_value

        except KeyError:
            quotes_dictionary = {}

        return quotes_dictionary
    
    
    async def get_customers_accounts_by_id(self):
        token = await self.get_auth_token()
        cust_id = await self.get_customer_uid()
        get_customer_accounts_URL = "https://sandbox-digitalbanking-uat2.finzly.io/api/openbanking/v2/customers/"+cust_id+"/accounts?limit=50&page=1"
        response = await q2_requests.get(
            self.logger, 
            get_customer_accounts_URL,
            headers = {
            'Content-Type' : 'application/json',
            'Authorization': token
        }
         )
        response_dict = response.json()
        accounts_list = response_dict['data']
        # print("Status code is : ", response.status_code)
        # print("Response object is :", accounts_list[0])
        return accounts_list
    
    async def get_auth_token(self):
        auth_token_url = 'https://security-uat2.finzly.io/auth/realms/BANKOS-UAT2-SANDBOX-CUSTOMER/protocol/openid-connect/token'
        api_key = 'sandbox.api.account'
        api_secret = 'c2f3eee1-96d2-476c-b615-5a3390289094'
        token = b64encode(f"{api_key}:{api_secret}".encode('utf-8')).decode("ascii")

        response = await q2_requests.post(
            self.logger,
            auth_token_url,
            headers = {
                'Content-Type' : 'application/x-www-form-urlencoded',
                'Authorization' : 'Basic ' + token,
                'Accept' : 'application/vnd.api+json'
            },
            data ={'grant_type':'client_credentials'}
        )
        auth_token_json = response.json()
        token_type = auth_token_json['token_type']
        token_value = auth_token_json['access_token']
        return token_type + ' ' + token_value
        
    async def get_customer_uid(self):
        token = await self.get_auth_token()
        email_address = self.online_user.email_address
        get_user_url = 'https://sandbox-digitalbanking-uat2.finzly.io/api/useradmin/v2/users/'+email_address+'?type=CUSTOMER'  

        response =  await q2_requests.get(
            self.logger,
            get_user_url,
            headers = {
            'Content-Type' : 'application/json',
            'Authorization': token
        }
        )
        print(response.request.url)
        print(response.status_code)
        response_json = response.json()
        response_data = response_json['data']
        cust_id = response_data['customerId']
        print('CUSTOMER ID for '+email_address+' is '+cust_id)
        return cust_id
