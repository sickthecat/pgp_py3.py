import os
import sys
import gnupg

def generate_keypair(email, passphrase):
    gpg = gnupg.GPG()

    key_params = {
        'key_type': 'RSA',
        'key_length': 4096,
        'key_usage': '',
        'subkey_type': 'RSA',
        'subkey_length': 4096,
        'subkey_usage': 'encrypt,sign,auth',
        'name_comment': 'Generated by python-gnupg',
        'name_email': email,
        'expire_date': '0',
        'passphrase': passphrase,
    }

    key_input = gpg.gen_key_input(**key_params)
    key = gpg.gen_key(key_input)

    return key

def save_keypair(gpg, key, directory='.', passphrase=None):
    if not os.path.exists(directory):
        os.makedirs(directory)

    public_key_filename = os.path.join(directory, '{}.pub'.format(key.fingerprint[-8:]))
    with open(public_key_filename, 'w') as f:
        f.write(gpg.export_keys(key.fingerprint, False, passphrase=passphrase))

    print("Public key saved to file: {}".format(public_key_filename))

    private_key_filename = os.path.join(directory, '{}.asc'.format(key.fingerprint[-8:]))
    with open(private_key_filename, 'w') as f:
        f.write(gpg.export_keys(key.fingerprint, True, passphrase=passphrase))

    print("Private key saved to file: {}".format(private_key_filename))

def main():
    email = input("Enter email address: ")
    passphrase = input("Enter passphrase for private key: ")
    gpg = gnupg.GPG()
    key = generate_keypair(email, passphrase)
    save_keypair(gpg, key, passphrase=passphrase)

if __name__ == "__main__":
    main()
