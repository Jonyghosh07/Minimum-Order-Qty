from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.product_configurator import WebsiteSaleProductConfiguratorController
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class WebsiteSaleProductConfiguratorControllerExtended(WebsiteSaleProductConfiguratorController):

    @http.route(
        route='/website_sale/product_configurator/get_values',
        type='json',
        auth='public',
        website=True,
    )
    def website_sale_product_configurator_get_values(self, *args, **kwargs):
        """
        Override to handle minimum_order_quantity
        """
        print("=== CUSTOM WEBSITE SALE CONTROLLER HIT ===")
        _logger.info(f"Custom website controller hit with kwargs: {kwargs}")
        
        self._populate_currency_and_pricelist(kwargs)

        quantity = kwargs.get('quantity', 1)
        product_template_id = kwargs.get('product_template_id') or (args[0] if args else None)
        
        if product_template_id:
            product_template = request.env['product.template'].browse(product_template_id)
            min_qty = product_template.minimum_order_quantity or 1
            actual_quantity = max(quantity, min_qty)
            
            print(f"Original quantity: {quantity}, Minimum: {min_qty}, Final: {actual_quantity}")
            
            # Update the quantity in kwargs
            kwargs['quantity'] = actual_quantity
        
        # Call the parent's parent method (SaleProductConfiguratorController)
        return super(WebsiteSaleProductConfiguratorController, self).sale_product_configurator_get_values(*args, **kwargs)

    def _get_product_information(
        self,
        product_template,
        combination,
        currency,
        pricelist,
        so_date,
        quantity=1,
        product_uom_id=None,
        parent_combination=None,
        **kwargs,
    ):
        """
        Override to include minimum_order_quantity in the product information.
        """
        
        # Get the original product information
        product_info = super()._get_product_information(
            product_template,
            combination,
            currency,
            pricelist,
            so_date,
            quantity=quantity,
            product_uom_id=product_uom_id,
            parent_combination=parent_combination,
            **kwargs,
        )
        
        # Add minimum_order_quantity to the product information
        min_order_qty = product_template.minimum_order_quantity or 1
        product_info.update({
            'minimum_order_quantity': min_order_qty,
        })
        
        print(f"Added product_info:------------------------------------------------ {product_info}")
        
        return product_info
