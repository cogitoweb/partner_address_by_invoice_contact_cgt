from openerp import api, fields, models, tools, SUPERUSER_ID, _

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.multi
    def _display_address(self, without_company=False):
    
        me = self
        if(self.customer or self.supplier): # only for customers or suppliers
            if(self.child_id): # which has childs (contatcs)
                # of type invoice, active, not company, without use of parent address
                childs = self.child_ids.filtered(lambda r: r.type == "invoice" and r.is_company == False and r.use_parent_address == False and r.active == True)
                if(childs): 
                    me = childs[0]
        
        return super(me, without_company)