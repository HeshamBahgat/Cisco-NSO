
class Ip_Calc(object):
    def __init__(self):
     pass

    def binary(self, dec):

        octets_padded = []
        octets_decimal = dec.split(".")

        for octet_index in range(0, len(octets_decimal)):

            binary_octet = bin(int(octets_decimal[octet_index])).split("b")[1]

            if len(binary_octet) == 8:
                octets_padded.append(binary_octet)

            elif len(binary_octet) < 8:
                binary_octet_padded = binary_octet.zfill(8)
                octets_padded.append(binary_octet_padded)

        self.decimal_binary = "".join(octets_padded)
        return self.decimal_binary

    def host_calc(self, binary_mask, binary_ip):

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)  # return positive value for mask /32

        # Obtain the network address and broadcast address from the binary strings obtained above
        self.network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros

        self.fina_cal()
        return self.network_address

    def fina_cal(self):

        net_ip_octets = []
        for octet in range(0, len(self.network_address_binary), 8):
            net_ip_octet = self.network_address_binary[octet:octet + 8]
            net_ip_octets.append(net_ip_octet)


        net_ip_address = []
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))
        host = int(net_ip_address.pop(-1)) + 1
        net_ip_address.append(str(host))

        print(net_ip_address)

        self.network_address = ".".join(net_ip_address)


"""

ip_address = "10.1.10.64"
subnet_mask = "255.255.255.240"

test = Ip_Calc()

i = (test.binary(ip_address))
m = (test.binary(subnet_mask))
print(test.host_calc(m, i))

"""