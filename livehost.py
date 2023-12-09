import nmap

def scan_subnet(subnet):
    """Scan the given subnet and return a list of alive hosts."""
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-sn')  # -sn for Ping Scan
    alive_hosts = [host for host in nm.all_hosts() if nm[host].state() == 'up']
    return alive_hosts

def main():
    subnet = input("Enter the subnet (e.g., 192.168.1.0/24): ")
    alive_hosts = scan_subnet(subnet)

    with open("alive_hosts.txt", "w") as file:
        for host in alive_hosts:
            file.write(host + "\n")

    print("Scan complete. Alive hosts have been written to alive_hosts.txt")

if __name__ == "__main__":
    main()
