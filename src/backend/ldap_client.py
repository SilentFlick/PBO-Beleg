import sys

import ldap

LDAP_SERVER = "ldaps://rlux40.rz.htw-dresden.de:636"


def authenticate(username, password):
    try:
        ldapLogin = "uid=" + username + ",ou=people,dc=htw-dresden,dc=de"
        server = ldap.initialize(LDAP_SERVER)
        result = server.simple_bind_s(ldapLogin, password)
        if result:
            print("Successfully bound to server.")
        server.unbind_s()
        return result
    except Exception as e:
        print("Failed to authenticate. Invalid credential:", e)


def main():
    res = authenticate(sys.argv[1], sys.argv[2])
    print(res)


if __name__ == "__main__":
    main()
