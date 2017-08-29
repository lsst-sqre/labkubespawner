import os
from jupyterlab.labhubapp import SingleUserLabApp


class SQRESingleUserLabApp(SingleUserLabApp):

    def init_webapp(self, *args, **kwargs):
        super().init_webapp(*args, **kwargs)
        settings = self.web_app.settings
        if 'page_config_data' not in settings:
            self.web_app.settings['page_config_data'] = {}
        settings['page_config_data']['LSST'] = 'LSST SQuaRE'
        if 'token' not in settings['page_config_data']:
            settings['page_config_data']['token'] = ''
        api_token = getattr(self, "api_token", None)
        if settings['page_config_data']['token'] == '':
            if not api_token:
                self.api_token = os.getenv('JUPYTERHUB_API_TOKEN')
            settings['page_config_data']['token'] = self.api_token


def main(argv=None):
    return SQRESingleUserLabApp.launch_instance(argv)


if __name__ == "__main__":
    main()
