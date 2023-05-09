# pgp_py3.py

python3 pgp_py3.py `your_email@example.com` `password_for_private_key`

The script will generate a PGP keypair with RSA 4096 and save the public and private keys to the cwd.
Needs python-gnupg.
`pip3 install python-gnupg`

Takes the email address and password for the private key as arguments and saves the keypair as needed in it's respective execution directory.
This script is considered obsolete by me. Please use afterburn.
