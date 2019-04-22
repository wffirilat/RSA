"# RSA" 
A simple instructional RSA encryption suite.
The RSA and Encrypt files provide simple enciphering which isn't especially resilient to simple susbsitution cipher cracking schemes.
RSA3 and Encrypt3 are more robust but decryption is considerably more computationally intensive because private keys tend to be much larger.

Embedded within RSA and RSA3 is a log time function for computing modular inverses based off of the Extended Euclidean Algorithm.

Computing modular exponents is now done in log time using the method of iterative squares so the RSA and RSA3 schemes now have similar runtimes.
