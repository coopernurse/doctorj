
import re

orderly_re = re.compile(r"[mM]essage:\s*(\S+).*?\.orderly}(.+?)~~~~", re.DOTALL)

def parse_orderly_blocks(d):
    return orderly_re.findall(d)
