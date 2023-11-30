from q2_sdk.core.install_steps import db_plan
# from q2_sdk.core.install_steps.uux_payload import UUXPayloadScript
# from q2_sdk.models.db_plan_shapes import UserPropertyFeature


class DbPlan(db_plan.DbPlan):

    def __init__(self):
        """
        It is often necessary to configure the database with information
        for an extension to run appropriately. This is your home to do so.

        Each of these attributes corresponds to a table (or set of tables) in the
        database. Instead of forcing all Antilles users to learn the
        database structure of Q2, we've opted for this handy abstraction.
        """

        super().__init__()
        self.ui_text_prefix = 'AccountDashboard'  # Will be used for all self.ui_text_elements
        # self.send_account_list = True  # Populate self.account_list when HQ calls the extension
        # self.send_account_details = True  # Populate HADE data on accounts in self.account_list
        # self.payload_stored_proc = None  # Run a given Stored Procedure to manipulate the call shape from HQ
        # self.account_rights_bit_flag = 0  # Will only send accounts that have access level greater than this flag
        # self.insight_features = []  # Run a list of Insight API Features as part of the install (Custom stored procedures)
        # self.marketplace_features = []  # Run a list of Insight API Marketplace Features as part of the install (Custom stored procedures)
        # self.user_property_feature: UserPropertyFeature = UserPropertyFeature.FeatureGroupCustUser

        # self.api_stored_procs = [db_plan.ApiStoredProc()]
        # self.audit_actions = [db_plan.AuditAction()]
        # self.data_feeds = [db_plan.DataFeed()]
        # self.disclaimers = [db_plan.Disclaimer()]
        # self.gt_data_elements = [db_plan.GTDataElement()]
        # self.host_tran_codes = [db_plan.HostTranCode()]
        # self.products = [db_plan.Product()]
        # self.product_types = [db_plan.ProductType()]
        # self.report_info = [db_plan.ReportInfo()]
        # self.required_forms = [db_plan.RequiredForm()]
        # self.third_party_data_elements = [db_plan.ThirdPartyDataElement()]
        # self.ui_config_property_data = [db_plan.UIConfigPropertyData()]
        # self.ui_text_elements = [db_plan.UiTextElement()]
        # self.user_account_attributes = [db_plan.UserAccountAttribute()]
        # self.user_property_data_elements = [db_plan.UserPropertyDataElement()]
        # self.user_property_data = [db_plan.UserPropertyData()]
        # self.uux_payload = [db_plan.UUXPayload([UUXPayloadScript()])]
        # self.vendors = [db_plan.Vendor()]
        # self.vendor_config = [db_plan.VendorConfig()]
        # self.vault_info = [db_plan.VaultInfo()]
