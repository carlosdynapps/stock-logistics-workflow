import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-stock-logistics-workflow",
    description="Meta package for oca-stock-logistics-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-delivery_package_default_shipping_weight',
        'odoo14-addon-delivery_procurement_group_carrier',
        'odoo14-addon-delivery_total_weight_from_packaging',
        'odoo14-addon-procurement_auto_create_group_carrier',
        'odoo14-addon-product_supplierinfo_for_customer_picking',
        'odoo14-addon-product_supplierinfo_picking',
        'odoo14-addon-purchase_stock_picking_invoice_link',
        'odoo14-addon-sale_line_returned_qty',
        'odoo14-addon-sale_line_returned_qty_mrp',
        'odoo14-addon-sale_order_global_stock_route',
        'odoo14-addon-sale_stock_mto_as_mts_orderpoint',
        'odoo14-addon-stock_account_product_run_fifo_hook',
        'odoo14-addon-stock_auto_move',
        'odoo14-addon-stock_delivery_note',
        'odoo14-addon-stock_landed_costs_mrp_subcontracting',
        'odoo14-addon-stock_lock_lot',
        'odoo14-addon-stock_lot_on_hand_first',
        'odoo14-addon-stock_lot_product_qty_search',
        'odoo14-addon-stock_lot_production_date',
        'odoo14-addon-stock_lot_scrap',
        'odoo14-addon-stock_move_assign_picking_hook',
        'odoo14-addon-stock_move_change_source_location',
        'odoo14-addon-stock_move_forced_lot',
        'odoo14-addon-stock_move_line_auto_fill',
        'odoo14-addon-stock_move_quick_lot',
        'odoo14-addon-stock_no_negative',
        'odoo14-addon-stock_owner_restriction',
        'odoo14-addon-stock_partner_delivery_window',
        'odoo14-addon-stock_picking_auto_create_lot',
        'odoo14-addon-stock_picking_back2draft',
        'odoo14-addon-stock_picking_backorder_strategy',
        'odoo14-addon-stock_picking_batch_extended',
        'odoo14-addon-stock_picking_cancel_reason',
        'odoo14-addon-stock_picking_default_planned_transfer',
        'odoo14-addon-stock_picking_filter_lot',
        'odoo14-addon-stock_picking_group_by_partner_by_carrier',
        'odoo14-addon-stock_picking_group_by_partner_by_carrier_by_date',
        'odoo14-addon-stock_picking_import_serial_number',
        'odoo14-addon-stock_picking_invoice_link',
        'odoo14-addon-stock_picking_line_sequence',
        'odoo14-addon-stock_picking_mass_action',
        'odoo14-addon-stock_picking_product_link',
        'odoo14-addon-stock_picking_progress',
        'odoo14-addon-stock_picking_purchase_order_link',
        'odoo14-addon-stock_picking_restrict_cancel_with_orig_move',
        'odoo14-addon-stock_picking_return_show_lot',
        'odoo14-addon-stock_picking_sale_order_link',
        'odoo14-addon-stock_picking_send_by_mail',
        'odoo14-addon-stock_picking_show_backorder',
        'odoo14-addon-stock_picking_show_return',
        'odoo14-addon-stock_picking_tier_validation',
        'odoo14-addon-stock_picking_warn_message',
        'odoo14-addon-stock_production_lot_active',
        'odoo14-addon-stock_push_delay',
        'odoo14-addon-stock_putaway_by_route',
        'odoo14-addon-stock_putaway_hook',
        'odoo14-addon-stock_quant_package_dimension',
        'odoo14-addon-stock_quant_package_dimension_total_weight_from_packaging',
        'odoo14-addon-stock_quant_package_product_packaging',
        'odoo14-addon-stock_restrict_lot',
        'odoo14-addon-stock_return_request',
        'odoo14-addon-stock_scheduler_assignation_horizon',
        'odoo14-addon-stock_split_picking',
        'odoo14-addon-stock_valuation_layer_by_category',
        'odoo14-addon-stock_valuation_layer_usage',
        'odoo14-addon-stock_valuation_no_developer_mode',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
