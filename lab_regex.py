import csv
import re

def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern, address):
    return True
  return False