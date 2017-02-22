from openerp import api, fields, models, tools, SUPERUSER_ID, _
from openerp.addons.base.res.res_partner import res_partner

import logging
_logger = logging.getLogger(__name__)

# cache old method
super_display_address = res_partner._display_address

def _display_address(self, cr, uid, address, without_company=False, context=None):

    me = address
    _logger.info('CLASS %s' % type(address).__name__)
    if(address.customer == True or address.supplier == True): # only for customers or suppliers
       if address.child_ids: # which has childs (contatcs)
           # of type invoice, active, not company, without use of parent address
           childs = address.child_ids.filtered(lambda r: r.type == "invoice" and r.is_company == False and r.use_parent_address == False and r.active == True)
           if(childs):
               me = childs[0] # replace recordset
    
    # call cached method
    return super_display_address(self, cr, uid, me, without_company, context)

# apply new method
res_partner._display_address = _display_address

