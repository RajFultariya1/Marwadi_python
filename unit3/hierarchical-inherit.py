#Hierarchical inheritance: Same base class, multiple derived classes

class SecuritySystem:
    def monitor(self):
        print("System is monitoring")

class IDS(SecuritySystem):
    def record(self):
        print("IDS detects suspicious activity")

class IPS(SecuritySystem):
    def sound_alarm(self):
        print("IPS blocks the malicious traffic")


my_ids = IDS()
my_ips = IPS()

my_ids.monitor()
my_ids.record()

my_ips.monitor()
my_ips.sound_alarm()