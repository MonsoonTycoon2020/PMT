Token Management System based on the Algorand blockchain.
Designed for tracking and scheduling blockchain transactions.

1. Clone repo
2. Install and activate Algorand's Sandbox Node on a Private network using './sandbox up -v' from within its directory
3. Ensure python virtual environment is installed
4. Activate venv and install py-algorand-sdk and Django using pip
5. Run 'python manage.py runserver'
6. Create and fund new testing account using UI, replace retrieve_sender() address with user addres on line 19 in helpers.py
