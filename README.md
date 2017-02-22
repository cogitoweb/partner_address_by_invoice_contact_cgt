# partner_address_by_invoice_contact_cgt
Display customer/supplier partner address depending on contact of type invoice

This module overrides \_display_address on res_partner to display (if present) the address of the partner contact of type invoice.
This override is activated only on partners marked as customers or suppliers.
