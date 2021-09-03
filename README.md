# MerakiCrack

Cracking the My.Meraki (MX100) default username.

Logging in to a Meraki device gave the error:

"You've entered incorrect login credentials. The default login is the serial number (e.g. Qxxx-xxxx-xxxx), with no password. The serial number is on the bottom or back of the device."

This made me think of a simliar password cracking project I did with the AT&T 2WIRE router a while back. The default WiFi password used a random 10 digit number that wasn't so random.

A quick google search discovered this site https://community.meraki.com/t5/Security-SD-WAN/Serial-Number-Lookup/td-p/46610 which list the first 4 of the serial number by product. Great that cut out 3 character. 

Next wanted to find some sample serial numbers. Went to ebay as one does.

Samples pulled from ebay pictures:
Q2JN-RQQH-QFMR
Q2JN-2Y9Y-AERC
Q2JN-S5WX-HEUY
Q2JN-2C7P-X2GP
Q2JN-YYM8-8HJT
Q2JN-8UBL-S2KA?

With the minimal data set I made the following assumptions:

- No group of 4 has all numbers.
- The same Letters are not repeated more than three times e.g., YYY or JJJ.
- The same numbers are not repeated more than twice in the same grouping e.g., 11 or 55. but they can be split YYM8-8HJT  
- Removed zero 0 and the letter O not seeing them in ebay samples.

When you take this all into account you can reduce the keyspace by quite I bit. Still not enough to have a chance at cracking it. 

Because the same numbers don't repeat in a grouping but do repeat across the groups (YYM8-8HJT). Combine this with the fact that the first grouping is static, this makes me think that each grouping is generated independently.

I created two scripts and ran them to see there was any improvement independently processing the two groups. (not smart enough to do the math)



# Serial Number to Model Number Table

|  S/N   |  Model |
| ------ | ------ |
|Q2AT    |  MC74 |
|Q2XD    |  MR20 |
|Q2RD    |  MR30H |
|Q2JD    |  MR32 |
|Q2PD    |  MR33 |
|Q2KD    |  MR42 |
|Q2TD    |  MR42E |
|Q2MD    |  MR53 |
|Q2UD    |  MR53E |
|Q2YD    |  MR70 |
|Q2EK    |  MR84 |
|Q2AX    |  MS120-8 |
|Q2CX    |  MS120-8FP |
|Q2KP    |  MS220-24P |
|Q2HP    |  MS220-8P |
|Q2FW    |  MS225-24 |
|Q2GW    |  MS225-24P |
|Q2PW    |  MS250-48LP |
|Q2VP    |  MS350-24 |
|Q2EW    |  MS350-24X |
|Q2XP    |  MS350-48 |
|Q2AW    |  MS410-16 |
|Q2CW    |  MS425-16 |
|Q2EV    |  MV12N |
|Q2GV    |  MV12W |
|Q2BV    |  MV21 |
|Q2HV    |  MV22 |
|Q2JN    |  MX100 |
|Q2SW    |  MX250 |
|Q2KN    |  MX64 |
|Q2QN    |  MX65 |
|Q2FY    |  MX67 |
|Q2HY    |  MX67C-NA |
|Q2MY    |  MX68CW-NA |
|Q2PN    |  MX84 |
|Q2AZ    |  vMX100 |
|Q2HN    |  Z1 |
|Q2TN    |  Z3 |
|Q2PY    |  Z3C-NA |
|Q2QY    |  Z3C-WW |
