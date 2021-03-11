"""connect to service
nc 18.221.44.9 3133
option 3: AgfJA2rLzNTIyxnLnJrFm3nFzdnTnhmXngqWx2y0yZfSx3a0CJrFyZbTm256nhj9cG==
reverse upper and lower cases
decodebase64: hackdef{base64_3s_d3m4s14d0_f4c1l_p4r4_c0m3nz4r}"""

import base64

def magic(cryptic):
    return ''.join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in list(cryptic))

c = 'AgfJA2rLzNTIyxnLnJrFm3nFzdnTnhmXngqWx2y0yZfSx3a0CJrFyZbTm256nhj9cG=='
print(base64.b64decode(magic(c)))