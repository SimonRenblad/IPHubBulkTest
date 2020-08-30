import IPHub
import configip

# CONSTANTS #
#############

# File name of ip addresses for checking, preferably in txt format
IN_FILE_NAME = configip.INPUT_FILE

# File name of target good and bad ip addresses
OUT_FILE_NAME_GOOD = configip.GOOD_OUTPUT_FILE
OUT_FILE_NAME_BAD = configip.BAD_OUTPUT_FILE

# The block constraint to be used by IPHub API, ie any ips with block >= BLOCK_CONSTRAINT are 'bad'
BLOCK_CONSTRAINT = configip.BLOCK_CONSTRAINT

# helper function for reading input file to a python list
def get_ip_addresses():
    file1 = open(IN_FILE_NAME, 'r')
    lines = file1.readlines()
    for line in lines:
        line.strip()
    file1.close()
    return lines

# helper function for writing the good and bad ips to diff lists
def write_ip_addresses(good_list, bad_list):
    file2 = open(OUT_FILE_NAME_GOOD, 'w')
    file2.writelines(good_list)
    file2.close()

    file3 = open(OUT_FILE_NAME_BAD, 'w')
    file3.writelines(bad_list)
    file3.close()

# main testing function
def run_test():

    # get addresses as python list
    addresses = get_ip_addresses()

    # keep count of the total number of checks
    count = 0

    # initialize lists
    good_list = []
    bad_list = []

    # iterate over ip addresses
    for add in addresses:

        # request from API
        block = IPHub.Lookup(add)

        # API error
        if block == None:
            print("error getting block value of address")
            break

        # determine good or bad based on block value
        if block < BLOCK_CONSTRAINT:
            good_list.append(add)
        else:
            bad_list.append(add)

        # increment count
        count += 1

    #print the total to the console
    print(f"Finished Testing of {count} addresses\n")

    # write good and bad to text files
    write_ip_addresses(good_list, bad_list)

run_test()
