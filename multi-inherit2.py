#Multi level inheritance

class Security:
    def protect(self):
        print("Protection is active")

class NetworkSecurity(Security):
    def monitor_network(self):
        print("Network traffic is monitored")

class Firewall(NetworkSecurity):
    def block_traffic(self):
        print("Malicious traffic is blocked")


my_firewall = Firewall()
my_firewall.protect()
my_firewall.monitor_network()
my_firewall.block_traffic()