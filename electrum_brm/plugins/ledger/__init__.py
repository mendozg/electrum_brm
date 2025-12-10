from electrum_brm.i18n import _

fullname = 'Ledger Wallet'
description = 'Provides support for Ledger hardware wallet'
requires = [('ledger_bitraam', 'github.com/LedgerHQ/app-bitraam-new')]
registers_keystore = ('hardware', 'ledger', _("Ledger wallet"))
available_for = ['qt', 'cmdline']
