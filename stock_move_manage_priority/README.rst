==============================
Stock Move Priority Management
==============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:fb065c3247dac66fa33df560a64c43855247e801eb01b7acbafa09c5aedcb382
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--workflow-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-workflow/tree/16.0/stock_move_manage_priority
    :alt: OCA/stock-logistics-workflow
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-workflow-16-0/stock-logistics-workflow-16-0-stock_move_manage_priority
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-workflow&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module enables the capability to manage the priority of a stock move
directly on the move itself. The goal is to promote/demote specific moves.

Into the reserving process, the moves are sorted by reservation date, then priority,
then date and finally by sequence. By default, the only way to change the priority
of a move is to change the priority of the picking.  If this default behavior fits
for most of the cases, we can imagine that in some cases, we want to change the
priority of a move without changing the priority of the picking since the stock is
limited for this particular product and we want to be sure that the move will be
reserved before others created before this one for example. This addon allows you
to do it by displaying the priority field into the Operations tree of the picking
form view.

**Table of contents**

.. contents::
   :local:

Usage
=====

The manage move priority setting can be reached by:

- Company: *Settings* - *Inventory* - *Operations*
- or *Inventory* - *Configuration* - *Settings* - *Operations*

Once there you can turn on/off "Manage Move Priority".

The priority can be set on move if:

- The manage move priority setting is turned on
- **and** the user is part of the 'stock move priority manager' group
- **and** the picking of the move is not locked
- **and** the picking state of the move is not 'done' or 'cancel'

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_move_manage_priority%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV

Contributors
~~~~~~~~~~~~

* Hughes Damry <hughes.damry@acsone.eu>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-workflow <https://github.com/OCA/stock-logistics-workflow/tree/16.0/stock_move_manage_priority>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
