from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """imports signals and overrides existing ready method"""
        import checkout.signals
